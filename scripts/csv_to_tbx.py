"""Helper script: convert termbase/termbase.csv (UTF-8 with BOM) to TBX-Basic (ISO 30042).

Written with AI assistance as a utility; the terminology work is in the termbase itself.
Usage: python scripts/csv_to_tbx.py termbase/termbase.csv termbase/termbase.tbx
"""
import csv, sys
from xml.sax.saxutils import escape

GENDER = {'masc.': 'masculine', 'fem.': 'feminine', 'neut.': 'neuter'}


def pos_for(pos, lang):
    """Return (partOfSpeech, is_phrase) for 'en' or 'el' from the pos column."""
    p = pos.strip()
    if p.startswith('EN/EL '):
        val = p[len('EN/EL '):]
    else:  # e.g. 'EN noun/ EL noun phrase'
        en, el = [x.strip() for x in p.split('/', 1)]
        val = (en if lang == 'en' else el).split(' ', 1)[1]
    return 'noun', val == 'noun phrase'


def lang_sec(r, lang):
    out = [f'<langSec xml:lang="{lang}">']
    d = r[f'definition_{lang}']
    if d:
        out.append(f'<descrip type="definition">{escape(d)}</descrip>')
    out.append('<termSec>')
    out.append(f'<term>{escape(r["term_" + lang])}</term>')
    pos, phrase = pos_for(r['pos'], lang)
    out.append(f'<termNote type="partOfSpeech">{pos}</termNote>')
    if phrase:
        out.append('<termNote type="termType">phrase</termNote>')
    if lang == 'el' and r['gender_el']:
        out.append(f'<termNote type="grammaticalGender">{GENDER[r["gender_el"]]}</termNote>')
    c = r[f'context_{lang}']
    if c:
        out.append(f'<descrip type="context">{escape(c)}</descrip>')
    out.append('</termSec>')
    out.append('</langSec>')
    return out


def entry(r):
    out = [f'<conceptEntry id="{r["id"]}">']
    if r['domain']:
        out.append(f'<descrip type="subjectField">{escape(r["domain"])}</descrip>')
    for k in ('definition_source', 'iate_id', 'iate_reliability', 'source_doc', 'register', 'status'):
        if r[k]:
            out.append(f'<note>{k}: {escape(r[k])}</note>')
    if r['synonyms_rejected']:
        out.append(f'<note>rejected synonym: {escape(r["synonyms_rejected"])}</note>')
    if r['note']:
        out.append(f'<note>{escape(r["note"])}</note>')
    out += lang_sec(r, 'en') + lang_sec(r, 'el')
    out.append('</conceptEntry>')
    return out


rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8-sig')))
lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<?xml-model href="https://raw.githubusercontent.com/LTAC-Global/TBX-Basic_dialect/master/DCA/TBX-Basic_DCA.sch" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>',
    '<tbx type="TBX-Basic" style="dca" xml:lang="en" xmlns="urn:iso:std:iso:30042:ed-2">',
    '<tbxHeader><fileDesc><sourceDesc><p>EN-EL Medicine Leaflet Termbase (portfolio project). Not for clinical use.</p></sourceDesc></fileDesc></tbxHeader>',
    '<text><body>',
]
for r in rows:
    lines += entry(r)
open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n</body></text></tbx>')

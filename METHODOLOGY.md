# Methodology

## Sources

Terms were extracted from the English and Greek package leaflets of three centrally authorised medicines published by the European Medicines Agency (EMA): Eliquis 2.5 mg, Bemrist Breezhaler and M-M-RvaxPro. Links and access dates are in [sources/sources.md](sources/sources.md).

Only public sources were used: EMA product information, IATE, NLM MeSH, PubMed Central and Merriam-Webster.

## Entry fields

`id, term_en, term_el, pos, gender_el, domain, definition_en, definition_el, definition_source, iate_id, iate_reliability, context_en, context_el, source_doc, register, synonyms_rejected, status, note`

- **id:** T001–T025.
- **term_el:** the term the Greek leaflet uses, errors included. The correct or recommended term goes in the note.
- **pos:** one column, `EN/EL noun`, `EN/EL noun phrase`, or `EN noun/ EL noun phrase` when they differ.
- **gender_el:** `masc.` / `fem.` / `neut.`
- **domain:** pharmacology, dose form, packaging, disease, symptom, anatomy/physiology, immunology, clinical procedure.
- **context_en / context_el:** the sentence from the leaflet. List items and table rows are quoted with their lead-in or frequency cell.
- **register:** everyday / technical / mixed (mixed = EN and EL differ in register).
- Cells are left empty instead of writing "none" (except `iate_id`).

## Definitions

Definitions follow ISO 1087 and ISO 704:

- class word (genus) + distinguishing features;
- one phrase, no article at the start, no full stop;
- the term is not used in its own definition;
- no examples;
- the EN and EL definitions describe exactly the same concept.

Where IATE has no entry or no definition, the definition was written from another cited public source; the source is recorded in `definition_source`. Official definitions reused verbatim are kept as they are, even if they break ISO 704; the issue is recorded in the note (T016, T018).

## IATE grounding

- **iate_id:** only an IATE entry for exactly this concept, or `none`. Broader or related entries go in the note ("related: IATE … (broader)").
- **iate_reliability:** format `EN 3 / EL 4`; empty when `iate_id` is `none`.

## Status

One value per entry:

- **approved:** the leaflet term is correct.
- **needs expert check:** the leaflet term is imprecise, broader, or shifts register, or no official source confirms it.
- **rejected:** a clear error (the Greek means something else). The recommended term is in the note.

## AI review

Eight leaflet sentences containing case-study terms were translated with DeepL and ChatGPT and checked against the termbase. Verdicts (approve / amend / reject) and their rules are in [review/ai-suggestions-review.md](review/ai-suggestions-review.md).

## File formats

- `termbase/termbase.xlsx` is the master file.
- `termbase/termbase.csv` is exported from it (UTF-8 with BOM).
- `termbase/termbase.tbx` was generated from the CSV with a helper script ([scripts/csv_to_tbx.py](scripts/csv_to_tbx.py), written with AI assistance) and validated against TBX-Basic (TBX-Core structure valid; TBX-Basic Schematron rules: 782 checks, 0 failures). It was not exported from MultiTerm.
- `termbase/termbase.ttb` is a Trados 2026 termbase made with Glossary Converter.

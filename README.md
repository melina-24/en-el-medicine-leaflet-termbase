# EN–EL Medicine Leaflet Termbase

A bilingual English–Greek termbase built from EU package leaflets for centrally authorised medicines. Each entry has a definition written to ISO 1087 / ISO 704 principles, grounding in IATE (the EU's terminology database) with its reliability score, and the real sentence the term appears in.

> **Status:** completed November 2026.

## What's in this repo

| File | What it is |
|---|---|
| `termbase/termbase.xlsx` | The master termbase (25 entries) |
| `termbase/termbase.csv` | The same termbase exported as CSV (UTF-8) |
| `termbase/termbase.tbx` | The termbase in TBX, generated from the CSV with a script and validated against TBX-Basic (ISO 30042) |
| `termbase/termbase.ttb` | A Trados 2026 termbase made with Glossary Converter |
| `sources/sources.md` | The leaflets used (product, EMA link, date accessed) and all reference sources |
| `review/ai-suggestions-review.md` | A terminology review of DeepL and ChatGPT output, checked against the termbase |
| `review/raw-outputs.md` | The unedited DeepL and ChatGPT outputs |
| `review/case-studies.md` | 4 difficult cases explained in depth |
| `METHODOLOGY.md` | How the termbase was built: sources, entry fields, definition rules, IATE grounding, statuses |

## Sources

All source texts are public product information published by the European Medicines Agency (EMA), in the English and Greek versions of the same leaflet: Eliquis 2.5 mg, Bemrist Breezhaler and M-M-RvaxPro. Links, access dates and EMA's reuse notice are in [sources/sources.md](sources/sources.md). Terms were checked against [IATE](https://iate.europa.eu).

## Sample entries

| English | Greek (leaflet) | Definition (EN) | IATE | Status |
|---|---|---|---|---|
| active substance | δραστική ουσία | substance responsible for the pharmacological activity of a medicinal product | 35093 | approved |
| sign | σημείο | sign that is evident to a doctor examining a patient | 261853 | needs expert check |
| ulcer of the stomach | πεπτικό έλκος | break in the lining of the stomach | 1547325 | rejected |
| tingling | φαγούρα | abnormal prickling sensation in the skin | none | rejected |

The Greek column shows the term the leaflet uses, errors included. For rejected entries, the recommended term is in the termbase note (e.g. "γαστρικό έλκος", "μυρμήγκιασμα").

## How the entries were built

Terms were selected from the English and Greek versions of the same leaflets. Definitions were written to ISO 1087 / ISO 704 and grounded in IATE where an entry exists; otherwise they were based on other cited public sources (NLM MeSH, PubMed Central, Merriam-Webster). Each entry has one status: approved, needs expert check or rejected. Details are in [METHODOLOGY.md](METHODOLOGY.md).

## Disclaimer

This is portfolio work. It has not been reviewed by a clinician or a regulator and is not for clinical use. For official information about any medicine, see the EMA product information or ask a doctor or pharmacist.

## Author

Melina Tatsiou – MA Linguistics

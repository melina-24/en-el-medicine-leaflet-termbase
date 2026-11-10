# EN–EL Medicine Leaflet Termbase

A bilingual English–Greek termbase built from EU package leaflets for centrally authorised medicines. Each entry has a definition written to ISO 1087 / ISO 704 principles, grounding in IATE (the EU's terminology database) with its reliability score, and the real sentence the term appears in.

> **Status:** work in progress. [TODO: change to "Completed November 2026" when finished]

## What's in this repo

| File | What it is |
|---|---|
| `termbase/termbase.csv` | The master glossary ([TODO: number] entries) |
| `termbase/termbase.tbx` | The same termbase exported from Trados MultiTerm (TBX, the standard exchange format) |
| `sources/sources.md` | The leaflets used: product, EMA link, date accessed |
| `review/ai-suggestions-review.md` | A terminology review of machine-translation and LLM output, checked against the termbase |
| `review/case-studies.md` | [TODO: number] difficult terms explained in depth |
| `scripts/check_termbase.py` | A small script that checks the termbase for missing fields, duplicates and missing IATE IDs |
| `METHODOLOGY.md` | How the termbase was built: sources, entry fields, definition rules, IATE reliability, status workflow |

## Sources

All source texts are public product information published by the European Medicines Agency (EMA), in the English and Greek versions of the same leaflet. Terms were checked against [IATE](https://iate.europa.eu).

[TODO: list the 2–3 medicines here, or point to `sources/sources.md`]

[TODO: quote EMA's reuse/copyright notice exactly as it appears on the EMA website, with a link to it]

## Sample entries

[TODO: 3–5 example rows from the termbase, e.g.]

| English | Greek | Definition (EN) | IATE | Status |
|---|---|---|---|---|
| | | | | |

## How the entries were built

[TODO: 3–4 sentences in your own words: how terms were selected, how definitions were written, how IATE was used, what the statuses mean. Details go in `METHODOLOGY.md`.]

## Disclaimer

This is portfolio work. It has not been reviewed by a clinician or a regulator and is not for clinical use. For official information about any medicine, see the EMA product information or ask a doctor or pharmacist.

## Author

Melina Tatsiou – MA Linguistics
# AI Suggestions Review

This review tests how DeepL and ChatGPT translate difficult terms from the termbase. The 8 sentences were chosen on purpose: they contain the case-study terms and other entries marked "rejected" or "needs expert check". Approved entries were not reviewed. The results therefore show how the tools handle hard terms, not how they perform on the termbase as a whole. The aim is not to criticise the tools or the leaflet translators, but to check how reliable each source is.

## Setup

| Tool | Model / version | Date | Prompt |
|---|---|---|---|
| DeepL | not shown (free web version, deepl.com, not logged in) | 14/11/2026 | none: sentence only (DeepL takes no instructions); EN→EL selected manually; no glossary; no formality option shown |
| ChatGPT | ChatGPT-6 | 14/11/2026 | I need you to provide the Greek translation of the sentence found in quotations at the end of this message. It's taken from a package leaflet (addressed to patients) that comes with the medicine. The source language is English. Do not use any explanations or alternatives, only the translation. |

ChatGPT: new chat per sentence; memory off; web search off; no custom instructions; default style.

Both tools: side-effect items were given with their frequency lead-in, as in the leaflet. Full outputs: [raw-outputs.md](raw-outputs.md).

**Limitations.** This is a small portfolio test, not an official study: 8 sentences, one run per tool, on one date. ChatGPT may have seen EMA leaflets in its training data; in some sentences its wording is close to the Greek leaflet (e.g. "Μη γνωστής συχνότητας… με βάση τα διαθέσιμα δεδομένα" in S6, and "σημεία" in T018, S4), so a match with the leaflet does not show that the model chose the term itself.

## Source sentences

| # | Source (`source_doc`, section) | EN sentence (leaflet) | EL sentence (leaflet) | Terms checked (ID) |
|---|---|---|---|---|
| S1 | Eliquis PL, s.1 | This medicine helps to prevent blood clots from forming by blocking Factor Xa, which is an important component of blood clotting. | Αυτό το φάρμακο βοηθάει στην πρόληψη του σχηματισμού θρόμβων στο αίμα, εμποδίζοντας τον Παράγοντα Xa ο οποίος είναι ένα σημαντικό συστατικό της πήξης του αίματος. | T002 |
| S2 | Eliquis PL, s.1 | A stroke can be life-threatening and requires immediate medical attention. | Το αγγειακό εγκεφαλικό επεισόδιο μπορεί να είναι απειλητικό για τη ζωή και απαιτεί άμεση ιατρική φροντίδα. | T005 |
| S3 | Eliquis PL, s.2 | Do not take Eliquis if you have a disease in an organ of the body that increases the risk of serious bleeding (such as an active or a recent ulcer of your stomach or bowel, recent bleeding in your brain). | Μην πάρετε το Eliquis εάν έχετε κάποια νόσο σε ένα όργανο του σώματος που αυξάνει τον κίνδυνο σοβαρής αιμορραγίας (όπως ενεργό ή πρόσφατο πεπτικό έλκος ή έλκος του εντέρου σας, πρόσφατη εγκεφαλική αιμορραγία). | T006, T007 |
| S4 | Bemrist PL, s.4 | Stop using Bemrist Breezhaler and get medical help immediately if you have any of the following: Common: may affect up to 1 in every 10 people - difficulty breathing or swallowing, swelling of the tongue, lips, or face, skin rash, itching and hives (signs of allergic reaction). | Σταματήστε να χρησιμοποιείτε Bemrist Breezhaler και λάβετε αμέσως ιατρική βοήθεια αν έχετε οποιοδήποτε από τα ακόλουθα: Συχνές: μπορεί να επηρεάσουν μέχρι 1 στους 10 ανθρώπους - δυσκολία στην αναπνοή ή στην κατάποση, διόγκωση στη γλώσσα, τα χείλη ή το πρόσωπο, δερματικό εξάνθημα, φαγούρα και πομφούς (σημεία αλλεργικής αντίδρασης). | T015, T019, T018 |
| S5 | Bemrist PL, s.4 | Common: may affect up to 1 in every 10 people - pain in muscles, bones or joints (signs of musculoskeletal pain) | Συχνές: μπορεί να επηρεάσουν μέχρι 1 στους 10 ανθρώπους - πόνος στους μυς, τα οστά ή τις αρθρώσεις (σημεία μυοσκελετικού πόνου) | T018 |
| S6 | M-M-RvaxPro PL, s.4 | Not known (Frequency cannot be estimated from the available data)* - An illness consisting of muscle weakness, abnormal sensations, tingling in the arms, legs, and upper body (Guillain-Barré syndrome). | Μη γνωστής συχνότητας (δεν μπορούν να εκτιμηθούν με βάση τα διαθέσιμα δεδομένα)* - Μια ασθένεια που περιλαμβάνει μυϊκή αδυναμία, μη φυσιολογικές αισθήσεις, φαγούρα στα χέρια, πόδια και το άνω μέρος του σώματος (Σύνδρομο Guillain-Barré). | T022 |
| S7 | M-M-RvaxPro PL, s.4 | Not known (Frequency cannot be estimated from the available data)* - Headache; fainting; nerve disorders which can cause weakness, tingling, or numbness; eye nerve disturbances. | Μη γνωστής συχνότητας (δεν μπορούν να εκτιμηθούν με βάση τα διαθέσιμα δεδομένα)* - Πονοκέφαλο, λιποθυμία, διαταραχές των νεύρων που μπορεί να προκαλέσουν αδυναμία, φαγούρα ή μούδιασμα, διαταραχές του οπτικού νεύρου. | T022, T023 |
| S8 | M-M-RvaxPro PL, s.4 | Not known (Frequency cannot be estimated from the available data)* - Burning and/or stinging of short duration at the injection site; blisters and/or hives at the injection site. | Μη γνωστής συχνότητας (δεν μπορούν να εκτιμηθούν με βάση τα διαθέσιμα δεδομένα)* - Αίσθημα καύσου και/ή κνησμός μικρής διάρκειας στη θέση της ένεσης, φουσκάλες και/ή εξανθήματα στη θέση της ένεσης. | T024 |

## Review

Columns:

- **ID**, **Termbase EN**, **Termbase EL**: the entry in the termbase. Termbase EL is the term used in the Greek leaflet.
- **Reference EL**: the recommended Greek term the tool output is compared against. "Termbase EL accepted" = the leaflet's term is kept as the reference.
- **DeepL**, **ChatGPT**: the term as it appears in each tool's output (full outputs in [raw-outputs.md](raw-outputs.md)).
- **DeepL verdict**, **ChatGPT verdict**: approve / amend / reject.
- **Reason**: why. Empty = no issue.

Verdicts:

- **approve**: the output matches the reference. A capitalisation difference is accepted, and so is a descriptive EL phrase for a descriptive EN phrase.
- **amend**: the right concept, but it needs a fix: an official term with a word missing, only part of the definition, or an unnecessary extra word (e.g. "σας").
- **reject**: a different concept, or the output repeats the leaflet's error.

### S1

| ID | Termbase EN | Termbase EL | Reference EL | DeepL | DeepL verdict | ChatGPT | ChatGPT verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| T002 | Factor Xa | Παράγοντας Xa | Termbase EL accepted | παράγοντα Xa | approve | Παράγοντα Xa | approve | |

### S2

| ID | Termbase EN | Termbase EL | Reference EL | DeepL | DeepL verdict | ChatGPT | ChatGPT verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| T005 | stroke | αγγειακό εγκεφαλικό επεισόδιο | Termbase EL accepted | εγκεφαλικό επεισόδιο | amend | εγκεφαλικό επεισόδιο | amend | IATE 1289336 official scientific term "αγγειακό εγκεφαλικό επεισόδιο" |

### S3

| ID | Termbase EN | Termbase EL | Reference EL | DeepL | DeepL verdict | ChatGPT | ChatGPT verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| T006 | ulcer of the stomach | πεπτικό έλκος | γαστρικό έλκος | έλκος στο στομάχι | approve | έλκος στο στομάχι | approve | Agrees with termbase EN (same concept). Changing the register isn't necessary as termbase EN also uses an informal noun phrase. However, termbase EL provides a broad term. Therefore, it is not accurate. "πεπτικό έλκος" includes "γαστρικό έλκος". So, "πεπτικό έλκος" is a broader category. "gastric ulcer" IATE ID 1547325. "peptic ulcer" IATE ID 1659247. |
| T007 | bleeding in the brain | εγκεφαλική αιμορραγία | Termbase EL accepted | αιμορραγία στον εγκέφαλο | approve | αιμορραγία στον εγκέφαλό σας | amend | ChatGPT: the word "σας" is unnecessary, yet acceptable since it matches the register (package leaflet, addressed to patients). |

### S4

| ID | Termbase EN | Termbase EL | Reference EL | DeepL | DeepL verdict | ChatGPT | ChatGPT verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| T015 | hives | πομφός | κνίδωση (preferred); πομφός (acceptable) | κνίδωση | approve | κνίδωση | approve | "hives" can be used as an informal term for the condition "urticaria" (using a visible sign of the condition to describe it). If that is the case, it directly translates to "κνίδωση". If "hives" refers to lots of separate wheals, then "πομφός" is acceptable as it is the Greek equivalent (the plural form of "πομφός" is used in the Greek leaflet). Both can be defensible, but a specialist should confirm. |
| T019 | itching | κνησμός | Termbase EL accepted | κνησμός | approve | κνησμός | approve | The termbase status (termbase.xlsx) is "needs expert check" not because the translation is wrong, but because there is a shift in register: "itching" is an everyday word, "κνησμός" is a medical term. The Greek leaflet renders "itching" in three ways: "skin itching" / "κνησμός στο δέρμα" (s.4); "itching and hives" / "φαγούρα και πομφούς" (s.4, this sentence), where the register didn't change; "itching and hives" / "κνησμό και πομφούς" (s.2). So we have an inconsistency in terms of following the right register. |
| T018 | sign | σημείο | σύμπτωμα or ένδειξη | συμπτώματα | approve | σημεία | reject | IATE 261853 defines "sign" as "sign that is evident to a doctor examining a patient". In this case, the leaflet is addressed to patients, and a patient cannot diagnose themselves. A patient can only experience or observe some symptoms. "ένδειξη" is equivalent to "σύμπτωμα" when used in this context. |

### S5

| ID | Termbase EN | Termbase EL | Reference EL | DeepL | DeepL verdict | ChatGPT | ChatGPT verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| T018 | sign | σημείο | σύμπτωμα or ένδειξη | συμπτώματα | approve | ενδείξεις | approve | IATE 261853 defines "sign" as "sign that is evident to a doctor examining a patient". In this case, the leaflet is addressed to patients, and a patient cannot diagnose themselves. A patient can only experience or observe some symptoms. "ένδειξη" is equivalent to "σύμπτωμα" when used in this context. |

### S6

| ID | Termbase EN | Termbase EL | Reference EL | DeepL | DeepL verdict | ChatGPT | ChatGPT verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| T022 | tingling | φαγούρα | μυρμήγκιασμα | μυρμήγκιασμα | approve | μυρμήγκιασμα | approve | "tingling" belongs under "paresthesia" (MeSH D010292); "itching" belongs under "pruritus" (MeSH D011537). So they are in two different branches and do not refer to the same sensation. "tingling" is an everyday word with no entry in IATE; its meaning is easily found in a dictionary (Merriam-Webster). |

### S7

| ID | Termbase EN | Termbase EL | Reference EL | DeepL | DeepL verdict | ChatGPT | ChatGPT verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| T022 | tingling | φαγούρα | μυρμήγκιασμα | μυρμήγκιασμα | approve | μυρμήγκιασμα | approve | Same as S6. |
| T023 | eye nerve disturbance | διαταραχή του οπτικού νεύρου | Termbase EL accepted | διαταραχές του οπτικού νεύρου | approve | διαταραχές του οπτικού νεύρου | approve | The termbase status (termbase.xlsx) is "needs expert check" for two reasons. First, IATE only has a definition for "optic nerve" (IATE 1542580); there is no entry for "eye nerve disturbance" or "optic nerve disturbance", or the respective Greek form. Second, a register shift is observed: termbase EN uses a lay phrase ("eye nerve"), whereas the Greek translation uses the medical term ("οπτικό νεύρο"). |

### S8

| ID | Termbase EN | Termbase EL | Reference EL | DeepL | DeepL verdict | ChatGPT | ChatGPT verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| T024 | stinging | κνησμός | επίπονο τσούξιμο | τσιμπήματος | amend | τσουξίματος | amend | The leaflet's "κνησμός" means "itching", which is a different concept: "stinging" is a painful prickling sensation in the skin, whereas "itching" isn't necessarily painful. Both tools avoid this error, but each gives only part of the definition ("επίπονο αίσθημα τσιμπήματος και τσουξίματος στο δέρμα"): DeepL "τσίμπημα", ChatGPT "τσούξιμο", and neither includes "επίπονο". |

## Patterns: errors a tool would make

1. **Register is not followed consistently**, which is also a problem in the leaflet itself.
   - Simpler form: T005 "stroke" → "εγκεφαλικό επεισόδιο" (both tools), instead of the scientific term found in IATE, "αγγειακό εγκεφαλικό επεισόδιο" (IATE 1289336). This is not necessarily a mistake; it is a choice of register or simplicity.
   - Technical term for an everyday EN word: T015 "hives" → "κνίδωση"; T019 "itching" → "κνησμός"; T023 "eye nerve disturbance" → "διαταραχές του οπτικού νεύρου" (both tools).
   - In the leaflet: "itching" is rendered both as "κνησμός" and as "φαγούρα" (T019); the lay "eye nerve" becomes the technical "οπτικό νεύρο" (T023).
2. **Only one part of the concept is rendered.** T024 "stinging": DeepL gives "τσίμπημα" and ChatGPT "τσούξιμο", each only part of "επίπονο αίσθημα τσιμπήματος και τσουξίματος στο δέρμα"; neither includes "επίπονο".
3. **The same concept gets two different translations.** ChatGPT renders T018 "sign" as "σημεία" in S4 and as "ενδείξεις" in S5. DeepL uses "συμπτώματα" in both.

## What the tools got right

Neither tool repeated the leaflet's three concept errors: T006 "πεπτικό έλκος" (both tools: "έλκος στο στομάχι"), T022 "φαγούρα" (both tools: "μυρμήγκιασμα"), T024 "κνησμός" (DeepL "τσίμπημα", ChatGPT "τσούξιμο"). In these cases both tools were closer to the reference than the published translation.

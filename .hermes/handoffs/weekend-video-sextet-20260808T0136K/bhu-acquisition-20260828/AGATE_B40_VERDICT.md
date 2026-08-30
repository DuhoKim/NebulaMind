BYLINE_CONFIRMED

I have reviewed the byline sweep implementation and verified the claims in the brief.

**1. Entry 44's Extraction Defect: CONFIRMED**
I checked the head of `1309.1487_clean.txt`. The ar5iv extraction is indeed defective: it completely dropped the first two authors, leaving only "...and Robert B. Mann". Pourhasan and Afshordi do not appear in the text below the annotation. The sweep only passes Entry 44 because your `EXTRACTION DEFECT` annotation explicitly supplies their names at the top of the file.

**2. The Popławski Normalization Flag: CONFIRMED**
Under NFD normalization, the Polish "ł" (U+0142) does not decompose because the stroke is not a combining mark; it is part of the base character. As a result, stripping non-ASCII characters turns "Popławski" into "popawski", which predictably fails to match "Poplawski" in the text files. The explicit `maketrans` mapping in the script is the correct fix. Entries 9, 11, and 12 are recorded correctly in the bibliography.

**3. Spot-check and the Uncatchable Class: CONFIRMED**
I performed independent checks on entries 6 (Smolin), 15 (Easson & Brandenberger), 28 (Sahu et al.), and 43 (missing authors in bib). Because the sweep only verifies that surnames *from the record* exist *in the source*, it has a significant blind spot. 
**The class the sweep cannot catch is: Record Omissions and Wrong Initials.** 
It cannot detect if an author is missing from the record (e.g., "et al." in Entry 28, or the entirely absent author list in Entry 43, which also suffers from a source extraction defect dropping the first author). Furthermore, because it only matches surnames, it will falsely pass a record that lists the wrong person from the right family (e.g., "D. Smith" instead of "J. Smith").

**4. Predicate Audit: CONFIRMED**
The script correctly uses Entry 20 as a positive control. The logic is sound, and the metrics prove it separates the corpus rather than failing completely.

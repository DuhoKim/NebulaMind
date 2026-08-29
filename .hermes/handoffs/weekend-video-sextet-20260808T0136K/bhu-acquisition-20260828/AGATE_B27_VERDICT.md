READABILITY_REFUTED_FALSE_MATCHES_AND_ARTEFACTS

I have reviewed the readability audit script (`b27_readability_audit.py`) and manually verified the presence and absence of papers.

**1. The "Not Located" List: REFUTED (FALSE ABSENCE)**
A manual check reveals that Entry 41 is present and fully readable in the repository as `2007.11556_clean.txt`. The script failed to find it because it rigidly matches the *published journal title* (from the bibliography) against the document text. The text file is the arXiv preprint, which uses a different title. Because preprints routinely change titles before publication, a strict title-string matcher guarantees false absences.

**2. The "Readable" List: REFUTED (FALSE POSITIVE)**
Entry 1 (Pathria 1972, *"The Universe as a Black Hole"*) is marked as readable and maps to `arxiv-1412.0105v1.pdf`. This is completely false. That PDF is actually Entry 5 (Khakshournia 2010, *"A note on Pathria's model of the universe as a black hole"*). Because Entry 1's title is a direct substring of Entry 5's title, the script matched a paper *about* Entry 1 and hallucinated that we possess the text of Entry 1.

**3. The Length Heuristic (>= 8,000 chars): REFUTED (BLIND TO SHORT LETTERS)**
The threshold automatically excludes any document under 8,000 characters (or any PDF under 2 pages, since the script crudely estimates 4,000 chars per page). Physics publications like *Physics Letters B* and *Nature* notes are often 1-2 pages of dense mathematics. Rejecting them simply for being short will generate false absences for perfectly valid, readable papers.

**4. The Recall Probe (Near-Misses): REFUTED (ARTEFACT AND CIRCULAR LOGIC)**
The cluster of near-misses (Entries 23, 26, 27) is not a signal of theoretical similarity to a no-go theorem. They are all papers in the same series by the same author (Gaztañaga). The high score is a pure artefact of the author's shared vocabulary and writing style triggering the regex. Furthermore, auditing "near-misses" is a circular way to measure recall; a blinded audit must sample randomly from the unflagged pool to find papers that the screen missed because they use *different* vocabulary.

**CONCLUSION:**
The readability script replaces one set of parsing errors with another. Its rigid title matching misses preprints, its substring vulnerability hallucinates missing papers, and its length threshold is hostile to short letters. The counts are not trustworthy.

# GATE BRIEF — B27, which papers can actually be read

Fresh context, adversarial. `b27_readability_audit.py` (4/4). This replaces a count **both of you
refuted** — I had told Duho 18 papers have no text, from parsing `ENTRY_SOURCE_MAP.md`. CGATE found
entries 5 and 56 readable but unindexed; AGATE found entry 17 falsely counted as pinned because my
regex pulled "17" from the filename `1111.1017_clean.txt`.

## THE CLAIMS

1. **34 of 51 BHU papers are readable; 17 are not located.** Method: the paper's title, lowercased
   with all non-alphanumerics stripped (first 44 chars), must appear in the first 6,000 characters
   of a `.txt` or on page 1 of a `.pdf`, in a document ≥8,000 chars — so a citation in a reference
   list does not count as possessing the paper.
2. **Not located:** 2, 3, 4, 13, 14, 15, 16, 17, 18, 19, 20, 28, 41, 42, 47, 48, 50.
3. **Entries 5 and 56 are found** (positive controls, both previously miscounted).
4. **Recall probe** (explicitly NOT a recall measurement): of 31 unflagged readable papers, four sit
   near b1's threshold — entries 55 (imp=7), 26 (imp=4, dom=6), 23 and 27.

## ATTACK

1. **Spot-check the "not located" list.** Take at least four of the seventeen and search the repo
   yourself by DOI, author surname, arXiv id, and any alternate title. **A single false absence
   refutes the count**, exactly as happened to my last one. Two prior versions of this search were
   badly wrong — one matched non-contiguous word fragments and found 2 of 51; both were caught only
   because entries 5 and 56 were controls.
2. **Spot-check the "readable" list for false positives.** Does any of the 34 match on a document
   that is *about* the paper rather than *being* it — a review, a citation-heavy note, an abstract
   page padded past 8,000 chars?
3. **Is the ≥8,000-char / head-only rule defensible?** Too low, too high, or matching the wrong
   region for two-column PDFs?
4. **The near-miss list.** Is "close to threshold" informative at all, or is it noise dressed as
   evidence? **Entries 23, 26, 27 are all one author's series — is that a real signal or an
   artefact of shared vocabulary?** Would you prioritise those four in a recall audit, or is that
   precisely the biased sample CGATE warned against, since a blinded audit must sample *randomly*
   from unflagged papers rather than from ones the screen nearly caught?
5. Predicate audit.

## VERDICT

First line one token: `READABILITY_CONFIRMED` / `READABILITY_REFUTED_<what>` /
`READABILITY_NARROWED_<what>`. Write to `<C or A>GATE_B27_VERDICT.md` here.

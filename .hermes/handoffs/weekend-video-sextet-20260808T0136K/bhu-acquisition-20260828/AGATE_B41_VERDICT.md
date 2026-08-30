COVERAGE_REFUTED_MULTIPLE_HOLES

I have executed the adversarial review of the census coverage claim. The script's arithmetic works, but its physical file mapping and conceptual definitions are fatally flawed. The coverage claim is refuted.

**1. Binding-by-Substring: CONFIRMED**
The exact substring bindings to the batch artifacts (B33, B34, B36, B37, B38, B39) are solid. I checked the batch scripts and verdicts; they adjudicated exactly the papers they claim to have adjudicated. There is no under- or over-specification in the batch sets.

**2. The Flags' Provenance: HOLE FOUND**
Entries 22 and 25 have concrete artifacts in this session (B22, B25). Entry 6, however, relies entirely on a bibliography reading note from "2026-08-23 (batch 9)". This read predates the strict B28 preregistered rule ("prove no member of a stated class..."). There is no gate verdict or artifact confirming that Entry 6 was actually adjudicated *under this rule*. Counting it as part of the rigorously adjudicated set is testimony with no artifact.

**3. Map-Parse Misattribution / File Iteration: REFUTED**
The script claims to "recompute live" the screen's flags by running the regex over the corpus. However, the loop `for f in sorted(os.listdir(SRC)): if not f.endswith("_clean.txt"): continue` restricts the scan entirely to `bhu-reading-20260823/sources/` and `_clean.txt` files. Entry 5 is located in `../reviews/.../arxiv-1412.0105v1.txt`. The script completely skips Entry 5! It does not register Entry 5 as a flag because it never even scanned it. The live recomputation is physically broken.

**4. The Miss-Rate Denominator: REFUTED**
The script uses only the paper-level metadata (`Testability: **THEORETICAL-OBSTRUCTION**`) for its denominator, yielding `{22, 5}` and a miss rate of 1 of 2. This is dishonest framing. The B1 regex screen was designed to catch theoretical obstruction *language and theorems* in the text. Papers 37, 51, 52, and 53 all contain rigorously derived, claim-level obstruction theorems (explicitly recorded in their prose). The fact that their overall paper tier defaults to something else (like a falsifier or construction) does not erase the obstruction theorem from their text. The screen missed all of them. The true denominator for what the screen was looking for is at least 6. I would print **1 of 6** (caught 22; missed 5, 37, 51, 52, 53).

**5. The Discharge Claim: CONFIRMED**
It is completely honest to count the B32 gate-reads (38, 57) towards the census. Duho's instruction to "read the unflagged remainder" is an order to achieve 100% coverage, not an order to redundantly re-read papers that have already been rigorously adjudicated under the exact same rule in this session. The precedent supports accumulating reads.

**Conclusion:** The claim that all 39 papers have been fully adjudicated under the B28 rule is punctured by Entry 6. The miss rate calculation is mathematically gerrymandered and physically unexecuted for Entry 5. The census is not cleanly closed.

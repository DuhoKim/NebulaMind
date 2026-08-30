Q8_NARROWED_B43_OMITTED

The ruling, tally arithmetic, frame-scoping, and closure record are all perfectly sound and honest. However, the implementation claim regarding the battery scripts contains a glaring omission.

**1. The Ruling (Sound)**
The ruling is structurally sound under the corpus's conventions. Option A correctly applies the ownership-of-proof and operative-contribution tests. Assigning the tier off a preprint is an accepted risk here precisely because of the appended `REVISIT` clause, which perfectly bounds the cost of being wrong to a single revert upon VoR acquisition.

**2. Frame-Scoping of b41 (Honest)**
The frame-scoping of `b41_census_coverage.py` is entirely honest. Entry 48 was outside the 39 readable papers (it was in the 12 "not-located" bucket) when the census was run. Asserting that the closed-census frame metrics (1-of-2 miss rate, 1-of-3 precision) are untouched because Entry 48 was never in the screen's pool is mathematically and historically correct. The printed disclosure is clear and accurate.

**3. Tally Arithmetic (Verified)**
The parsed Testability markers precisely match the recomputed tally:
* 4 `CALIBRATED-FALSIFIER`
* 32 `CONSISTENCY-ONLY`
* 3 `PROSPECT`
* 7 `QUALITATIVE-DIRECTIONAL`
* 3 `THEORETICAL-OBSTRUCTION` (Entries 22, 5, 48)
* 2 `UNREAD` (Entries 42, 47)
Total = 51. The arithmetic holds.

**4. Closure Record Fidelity (Verified)**
The closure record in `OPEN_QUESTIONS_FOR_DUHO.md` is highly faithful. It explicitly details the ruling's basis, properly scopes the cost as small due to the revisit clause, and clearly delineates the archived original question.

**5. Predicate Audit (THE NARROWING)**
The brief claims: "five battery scripts moved in the same change... b43/b46/b47 assert the current set {22,5,48}". **This is false.**
Only FOUR battery scripts (`b41`, `b45`, `b46`, `b47`) were modified in commit `4a5683e49`. `b43_entry38_fullread.py` was **not** moved in this commit, does **not** assert the updated `{22, 5, 48}` obstruction set, and continues to lack the `obs == {22, 5, 48}` check entirely. The implementation missed one of the stated repairs.

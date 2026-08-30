# GATE BRIEF — B40, corpus-wide byline sweep

Fresh context, adversarial. `b40_byline_sweep.py` (2/2): every readable entry's recorded authorship
checked against its pinned source's own byline — the entry-20 defect class (right title, verified
DOI, wrong authors), previously caught only by accident, now swept corpus-wide. Result: 39 of 39
match, after two resolutions.

## THE CLAIMS TO ATTACK
1. **Entry 44's pin is defective, not its record**: the ar5iv extraction of 1309.1487 dropped the
   first two authors — "Pourhasan"/"Afshordi" appear NOWHERE in the file *below the annotation
   header I added*; the head reads "…Big Bang and Robert B. Mann". Verify by reading the file
   below its EXTRACTION DEFECT header. Note the honesty caveat: the sweep now passes 44 *because*
   my header names the authors.
2. **The first run's three Popławski flags were my normalizer's fault** — "ł" does not decompose
   under NFD. Check the fix and confirm entries 9/11/12's records are right.
3. **Spot-check four bylines independently** (your choice of entries) — the sweep matches surnames
   in heads; a wrong-but-present surname (e.g. right family, wrong person) would pass it. State the
   class the sweep cannot catch.
4. Predicate audit.

## VERDICT
One token: `BYLINE_CONFIRMED` / `BYLINE_REFUTED_<what>` / `BYLINE_NARROWED_<what>`.
Write to `<C or A>GATE_B40_VERDICT.md` here.

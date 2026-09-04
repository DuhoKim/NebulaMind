# R3-C2 interpretation protocol — fixed BEFORE the census runs, and NOT readable by any seat

**Tori, 2026-09-04 21:36 KST.** Held separately from `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` because the gate
found that stating the hypothesis-to-outcome mapping inside the document the seats read tells them the stake of each
outcome. **No seat in R3C2 may open this file.** It is committed before limb A begins so it cannot be written to suit
the tally.

## The mapping, fixed in advance

Once the census tally is sealed and its sha256 committed to git, Tori — and only Tori — compares it with
`SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md`:

- **One or more `REPRO_EXACT`** → a counterexample to the shape/magnitude pattern. The pattern record **must** be
  amended to say so, naming the claim.
- **No `REPRO_EXACT`, and `REPRO_AFTER_CHOICE` or `REPRO_INPUT_ABSENT` dominate** → consistent with the pattern.
  Report the tally, not a strengthened claim: consistency is not proof.
- **`REPRO_FAILED` dominates** → a different finding altogether, about arithmetic rather than free parameters, and the
  pattern record is left alone.
- **`NOT_ATTEMPTED` dominates** → the corpus prints fewer results than assumed; report that, and the pattern is
  neither supported nor weakened.

## What this step may not do

It may not alter, re-file or re-open a single per-claim outcome. The sealed tally's hash and its git commit id are
quoted in the result so any reader can verify the tally predates this comparison.

R3C2_INTERPRETATION_PROTOCOL_COMPLETE

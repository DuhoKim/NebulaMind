# R3-C2 interpretation protocol — fixed BEFORE the census runs, and NOT readable by any seat

**Tori, 2026-09-04 21:36 KST; V2 2026-09-05 after Duho's ruling "Q-R3C2 c" (option (c): one pass, two tallies).** Held
separately from `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` because the gate found that stating the
hypothesis-to-outcome mapping inside the document the seats read tells them the stake of each outcome. **No seat in
R3C2 may open this file.** It is committed before limb A begins; §7 of the preregistration states what that does and
does not prove.

## What this step reads (option (c))

It reads **two tallies from one pass**: the reproduction tally (`REPRO_WITHIN_STATED_PRECISION` / `REPRO_FAILED` / the non-arithmetic
outcomes) and the **`rests_on` tally** (`DERIVED_ONLY` / `USES_CHOSEN` / `USES_FITTED` / `USES_IMPORTED` /
`USES_UNDECLARED`), both from the sealed tally and its ledger. **The reproduction verdict alone is never the
interpretive input.**

## The mapping, fixed in advance

Once the tally is sealed under §7's receipted relay, Tori — and only Tori — compares it with
`SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md`:

- **One or more claims filed `REPRO_WITHIN_STATED_PRECISION` with `rests_on = DERIVED_ONLY`** — a number that follows from the paper's
  own equations and measured constants with nothing chosen, fitted, imported or undeclared — is a **counterexample** to
  the shape/magnitude pattern. The pattern record **must** be amended to say so, naming the claim.
- **`REPRO_WITHIN_STATED_PRECISION` claims exist but every one has `rests_on` in {`USES_CHOSEN`, `USES_FITTED`, `USES_IMPORTED`,
  `USES_UNDECLARED`}** → the arithmetic works and rests on a free input in every case: **consistent with the pattern**.
  Report the two tallies, not a strengthened claim: consistency is not proof.
- **`REPRO_FAILED` dominates the arithmetic group** → a different finding altogether, about arithmetic rather than
  free parameters; the pattern record is left alone.
- **Non-arithmetic outcomes dominate** (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`,
  `REPRO_NOT_EVALUABLE`) → the corpus prints fewer evaluable results than assumed; report that; the pattern is neither
  supported nor weakened.
- **`CENSUS_ORIGIN_DISPUTED`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_CONTROL_SPLIT`,
  `R3C2_NO_CLASS`** → no comparison is made; the study-level class is reported as is.

## What this step may not do

It may not alter, re-file or re-open a single per-claim outcome or a single `rests_on` value. The sealed tally's hash,
its commit id, this file's hash and its commit id — the four receipted digests — are quoted in the result so any
reader can verify the tally and this mapping both predate the comparison.

R3C2_INTERPRETATION_PROTOCOL_V2_COMPLETE

---
**V3 (2026-09-05 23:02 KST):** `REPRO_EXACT` → `REPRO_WITHIN_STATED_PRECISION` throughout, following Duho's "1a rename" ruling applied in R3C2 V21; no rule of interpretation changed. Prior digest `8b44becb89539eb3…`.

# The pattern's own falsifier has an inverted condition — found by codex gating R3D V4

**Tori, 2026-09-04, on the R3D V4 gate. NOT REPAIRED. Reported for Blanc and Duho.**
**No tier, token, standing or stamp moves. Paper HOLD.**

## What was found

R3D's C6 copies the five breaker conditions **verbatim** from
`SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md` (sha256 `fff1f1a8…f156c96`). Gating that copy, codex found a
**polarity error in condition 3** — and it is an error in the **pattern record itself**, not in R3D's transcription.

Condition 3, verbatim:

> 3. **No free normalisation survives** the derivation: replacing every parameter by a free symbol and demanding the
>    printed number back **must fail** without any parameter being chosen — the C4 free-symbol probe.

The record says a construction must **satisfy all five** conditions to count as a breaker.

## Why it is inverted

Replace every parameter by a free symbol and try to recover the printed number. Two outcomes:

- **You recover it.** The number does not depend on any parameter's chosen value → **no free normalisation.**
- **You cannot recover it without choosing a parameter.** The number depends on a choice → **a free normalisation
  exists.**

Condition 3 as written demands the **second** outcome ("must fail without any parameter being chosen"). But that
outcome is precisely the *presence* of a free normalisation — the thing the condition's own heading says must
**not** survive. **As written, a construction satisfies condition 3 exactly when it has the defect the condition
exists to exclude.**

## Why this matters beyond R3D

1. **The pattern's stated falsifier is what makes it a finding.** Blanc's own instruction was that *a pattern with
   no stated breaker is not a finding.* One of the five conditions being inverted means the stated breaker does not
   test what the record says it tests.
2. **Direction of the error.** A candidate breaker that genuinely fixes a magnitude from its own geometry — the
   real counterexample — would **fail** condition 3 as written and be rejected. The inverted condition is biased
   **toward preserving the pattern**, which is the direction this lane has been repeatedly warned about.
3. **R3D cannot be soundly frozen on top of it.** R3D's whole point is to test this branch against the breaker. Its
   C6 pins the conditions by hash, correctly — but pinning an inverted condition just makes the inversion binding.

## What I have NOT done

- **I have not edited the pattern record.** The five conditions have been reported to Blanc and Duho as the
  pattern's stated breaker; silently re-polarising a falsifier after it has been reported is exactly the kind of
  quiet change this lane's discipline exists to prevent. This is a disclosure, not an amendment.
- **I have not repaired R3D's C6.** Repairing a copy while the source is inverted would put two different texts of
  the same condition into the record.

## The repair, when it is authorised

codex's replacement for the R3D decision rule: *"the printed number is recovered with no non-§2b parameter
chosen"* — i.e. **PASS when recovery succeeds without any choice.** The pattern record's condition 3 needs the
matching correction, as an amendment with its own version and hash, and **every earlier use of condition 3 needs
re-checking**: the six pattern instances were assessed against the conditions as written.

**Whether any of the six instances was assessed against the inverted condition, and whether that changed any
outcome, is the first thing to check once the correction is authorised.** I have not checked it, because checking
it would mean applying a condition text nobody has approved.

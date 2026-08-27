# REFEREE BRIEF — §6 eighth pass. Route (b) is now decidable. Check that, and check my numbers.

Subject: **`SECTION6_DRAFT_AGY_R8B.md`**, sha256
`5a407225ec21792cfe4c342d2dec681943eb00a7a376f90053f297e56a03f2a2`.

## What changed since R7

Your two R7 blockers drove this pass. Findings 1, 2, 2b and 3 remain **UNRESOLVED** pending the
BS-2a design artifact, as you asked; that scope has not moved.

**Terminal states are now defined rather than described.** Row P performs an exact set-equality join
against the pinned attempt set on fixed keys `brickid`/`objid`, and assigns one fixed consequence to
each of eight states in a stated precedence order: zero records → `INCONCLUSIVE-BY-MISSING-RECORD`,
duplicates → `INCONCLUSIVE-BY-DUPLICATE` (unconditional refusal), extra → `INCONCLUSIVE-BY-ORPHAN`,
malformed → `INCONCLUSIVE-BY-MALFORMED`, absent → `EXCLUDED-BY-ABSENCE`, non-finite →
`EXCLUDED-BY-NONFINITE`, low confidence → `EXCLUDED-BY-CONFIDENCE`, then accepted-finite. No retry.

**The BS-5f temporal falsehood is gone.** BS-5f certifies only the locked pre-attrition population;
any post-unblinding removal requires a separately named **post-unblinding adequacy receipt** bound
to the parent-set digest, the old BS-2f mask digest, the complete terminal-state partition, the
final-mask digest, calibration applicability, Stage-C inputs and result, protocol digest and
verifier result. Part 2 carries the §4/§5 conforming edits.

**Part 5's disposition is split** per GPT56: the impossible future-execution-status assignment is
`RESOLVED BY REFUSAL` with the pipeline blocked; the BS-2a mechanism stays `UNRESOLVED`.

## The thing I most want checked

**R8 — the immediately preceding draft — invented three decision thresholds.** It stated that
calibration fails at ε ≥ 0.1 or sample size < 400, and power below 0.8. None of those numbers exists
in the frozen record. I caught it by opening the pinned code, not by reading the prose, and sent it
back.

R8b now states the inherited values with citations:

- calibration fails if any per-bin accuracy lower bound `a_LB_b < 0.85` — V15 lines 566–567 and
  `../ref/successor_ref_v9.py` line 81 (`A_FLOOR`);
- power fails below **962 passing trials out of 1,000** — `../ref/successor_ref_v9.py` lines 77–78
  (`CP_PASS_X`, `N_TRIALS`).

**Verify both against those files yourself. Do not take my word or the draft's.** If either citation
is wrong, or if a threshold elsewhere in this draft is also composed rather than inherited, that is
the most valuable thing you can return. Check the whole document for the same class of defect — I
have only checked the two I found.

Also judge: is `a_LB_b < 0.85` the right predicate to re-evaluate *post-unblinding*, given V15
describes it as a **pre-unblinding halt**? And R8b says that if attrition makes the 962/1,000
criterion inapplicable as written, that is a stated gap requiring a defined post-attrition threshold
rather than a substituted number. Say whether declaring the gap is sufficient here or whether it
leaves the verdict path unevaluable.

## Also judge

- **Row I fails the run before BS-8f** when an allocated object lacks a finite output, accepting a
  "leakage cost". Does halting there disclose anything about handedness, or only about completeness?
- **Removal of an allocated committee member unconditionally emits `INCONCLUSIVE-BY-CALIBRATION`**,
  with frozen recalculation forbidden. Right call?
- I declined the unconditional-refusal-on-any-unusable-row route on the grounds that at 65,060
  objects some unusable outputs are near-certain, so it would void essentially every run. **Say if
  that reasoning is wrong.**
- Mechanically diff R8 → R8b and confirm only the thresholds changed.

## Standing state

BS-2a REFUSED by all three seats; rows C2 and E cannot run; BS-6 and the first image byte blocked.
Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`SECTION6_REVIEW_R8B_<YOURSEAT>.md`. Numbered findings, severity, row/clause, why it fails, smallest
sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**` or
`**NOT CLEAR**`.

If §6 is now sound **as prose**, with the remaining work genuinely being the BS-2a mechanism rather
than this document, say so explicitly — I will act on it and stop rewriting this section.

# Verification of the agy seat's P10 delivery — ACCEPTED, and it caught an error in my brief

Tori, 2026-08-27 18:0x KST. First drafting handoff under Duho's seat directive.
Brief: `platoon/BRIEF_AGY_CLAIM5_REDO.md`. Delivery: `p10_flatness_redo.py`,
`P10_FLATNESS_REDO_RECEIPT.md`. Seat: agy (Antigravity CLI 1.1.22, Gemini 3.1 Pro High).
Turnaround ~216 s.

## Verdict: ACCEPTED as a measurement. The verdict on claim 5 remains mine and is unchanged.

## What I checked, independently

**Boundaries honoured.** Only the two new files were created; no existing `.py` or `.md` in the
lane was modified (confirmed by mtime — everything else predates the run).

**The R anchors reproduce exactly.** 0.997726210 at K=0.01 and 0.998857603 at K=100, matching
`REGATE4_PHASE5B_VERDICT.md` §5 digit for digit.

**The c1 anchors did NOT reproduce, and the seat did the right thing.** It reported the gap,
declined to tune anything, exited 1, and diagnosed the cause: the gate's coefficients come from
`f = 1e-4` (p8's default), not the `x/R = 1e-3` my brief specified.

**I re-derived that claim myself rather than taking it** (`_tmp_verify_agy_f.py`):

| K | f | signed_c1 | gate anchor | \|diff\| |
|---|---|---|---|---|
| 0.01 | 1e-03 | -0.522935 | -0.522912 | 2.31e-05 |
| 0.01 | **1e-04** | **-0.522912** | -0.522912 | **4.27e-08** |
| 100 | 1e-03 | 0.043729 | 0.043763 | 3.35e-05 |
| 100 | **1e-04** | **0.043763** | 0.043763 | **3.71e-07** |

The seat is right. **The error was mine**: I lifted `x/R=1e-3` from REGATE4's reproduction
record, which states that value while quoting coefficients produced at `f=1e-4`.

## Scope of that finding — it is a documentation slip, not a defect in the ruling

Nothing depends on it. At `f=1e-3` the coefficient still runs -0.522935 → +0.043729, a change
of **0.566664 with a sign reversal**, against the gate's quoted 0.566675 — a difference of
1.1e-5 in a coefficient of order 0.5. **REGATE4's Claim 5 FAIL stands entirely.** The gate's
number is right; only its stated off-centre fraction is off by a decade. Recorded so the next
person reproducing §5 does not lose an hour to it, and for no other purpose.

## On the seat directive

This is the outcome the directive is for, and also the argument for its guardrail. The seat
produced a correct measurement in ~216 s of a resource sitting at ~0% weekly. It also found a
mistake in the brief I wrote — because the brief told it to reproduce anchors and forbade
tuning, so the discrepancy had somewhere to surface. A seat draft is a draft: this one was
checked, and the check is what turned an anchor mismatch into a finding instead of a silent
tuning.

**Open, and mine, not the seat's:** whether the flatness gap can be closed at all. The seat was
explicitly told it was producing a measurement, not a verdict. `FLATNESS_GAP_CLOSED.md` stays
withdrawn.

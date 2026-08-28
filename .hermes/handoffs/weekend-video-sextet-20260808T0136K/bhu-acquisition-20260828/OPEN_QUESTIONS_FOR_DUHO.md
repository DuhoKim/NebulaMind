# Open questions — Tori, BHU sweep. CHOICES I did not take.

Per the overnight rule relayed by Blanc: act alone on mechanical continuation, stop and write
the question down when it is a choice. These are the choices. Nothing below has been applied.

Written 2026-08-29 ~00:30 KST.

---

## Q1. The tier scheme has no class for a theoretical no-go. Should it get one?

**Raised by:** entry 22 (Easson 2026, "Obstructions to Minimal Regular Black Hole Cosmologies").

All four tiers rank papers by OBSERVATIONAL testability:

| tier | meaning |
|---|---|
| CALIBRATED-FALSIFIER | number + threshold on an observable |
| QUALITATIVE-DIRECTIONAL | directional claim, no calibrated threshold |
| CONSISTENCY-ONLY | shows compatibility with observation; states no prediction that could fail |
| PROSPECT | points at future instruments without supplying the test |

Entry 22 fits none. It is a theorem paper: Proposition 1, Proposition 2, Theorem 1. It does not
show compatibility with observation and it does not state a prediction that could fail — it
proves that a class of constructions **cannot work**. It is currently filed CONSISTENCY-ONLY,
which is the closest available box and is wrong in both halves of its definition.

This matters beyond bookkeeping. Entry 22's whole purpose is to constrain OTHER entries in this
corpus — the bibliography's own ranked list says a strict night would "map which of the other
published interiors (Dymnikova 18/19, Bronnikov 20, Roupas 21, Gaztañaga 25/26, Popławski 11)
they kill, restrict, or spare." **The record has no way to express "this paper refutes that
paper."** A no-go can retire a model without any measurement at all, which is arguably a
stronger result than a falsifier that has not fired.

**Options.**
- **(a)** Leave it. Accept that the record cannot express theoretical obstruction, and note it in
  prose on the affected entries.
- **(b)** Add a fifth class — e.g. `THEORETICAL-OBSTRUCTION` — for papers whose force is a proof
  rather than a measurement.

**Why I did not choose.** (b) changes what the programme claims about its own corpus and would
require re-examining every entry for misfiling, including ones already gated. That is a change to
the instrument, not a reading of a paper.

---

## Q2. The A6 `FIRES` split is unresolved and I have not picked a side.

Both seats refused the entry-25 promotion, agreeing on `RIGID: NO` and `DISTINCTIVE: NO`. They
split on whether the w ≠ −1 test currently fires:

- **agy — FIRES: YES.** Cites the DESI collaboration DR2 result, ~3σ for dynamical dark energy.
- **codex — FIRES: UNDETERMINED.** Same DESI numbers (arXiv:2503.14738, PRD 112, 083515 (2025):
  3.1σ for BAO+CMB, 2.8–4.2σ with supernovae), but refuses the step because the BHU paper states
  **no statistical rejection rule**, the 3σ threshold was invented by my script, and DESI's
  preference is dataset- and model-dependent.

I adopt neither and have recorded both. Note that Blanc's relay compressed this to "FIRES yes",
which is agy's half only.

**What would settle it:** pinning arXiv:2503.14738 in the corpus. Both seats reached it by web
search; it is testimony, not a receipt, and nothing in the lane is asserted on it. This is a
mechanical acquisition and I will do it without asking — flagged here only because the *conclusion*
that follows from it is not mechanical.

---

## Q3. Five entries examined, five tier verdicts unchanged. Is the sweep worth continuing?

Entries 21, 26, 51-adjacent re-reads, 25 and 22 have all been examined. Four overclaimed and were
confirmed at their existing tier after audit; entry 25's promotion was refused; entry 22 is a
category mismatch rather than a wrong rank.

**Not one tier has moved.** That is a real result about the RECORD — it is more accurate than the
cheap classifiers suggested, and the METHODS_NOTE bias runs the other way. But it also means the
marginal audit is returning less each time.

**The question is whether to keep sweeping the remaining 19 unpinned / 26 unaudited entries, or
stop and write up what the five audits established.** I have kept going because the sweep was
authorised and continuing it is mechanical. Stopping is a judgement about value.


---

## Q4. Entry 23 looks like a CALIBRATED-FALSIFIER filed as QUALITATIVE-DIRECTIONAL.

**Raised by:** entry 23 (Gaztañaga 2020, MNRAS 494, 2766, "The size of our causal Universe").
Audited in `a10_entry23_cutoff.py`. **RESOLVED 2026-08-29 03:0x — both seats REFUSED the
promotion. Q4 is closed; no decision needed from you.** Left here because the reason is worth
reading: the ±3° I built the case on is read *off the observed CMB curve* and used to infer Ω_Λ,
not propagated forward from Ω_Λ. The forward derivation is real (CGATE: RIGID YES, DERIVED YES);
the *calibration* is not. Tier stays QUALITATIVE-DIRECTIONAL.

The paper predicts an angular scale on a measured observable, with an uncertainty, in the
author's own verb:

> "It also predicts that CMB temperature should not be correlated above θ > θ_§ ≃ 60 deg."
> "…we roughly estimate θ_§ ≃ **60 ± 3** deg."

**And the number is derived, not fitted.** The bibliography's ranked-target note warns of "the
post-hoc-fitting risk … the scale is fitted from the anomalies it explains." That is the right
worry and it does not appear to hold: the causal scale follows from the **measured Ω_Λ**
(θ_§ = χ_§/χ_CMB, evaluated "for Ω_Λ = Ω_§ ≃ 0.7"), and the CMB anomaly is then an *independent*
check. One observable in, a different observable out.

**Why this is unlike the other entries audited tonight.** Entries 21, 25 and 26 each supplied a
real number that could not fail, because the author also supplied the auxiliary that absorbs a
discrepancy — an uncomputed excitation amplitude, "not solely caused by", observer typicality
with no rejection rule. I have not found a free parameter in this chain. That is exactly the
claim I got wrong at A6, which is why it is gated rather than applied.

**Recorded against it, not argued away:**
- The hedge is "**roughly** estimate", and the whole result is conditional on "assuming that the
  causal scale is smaller than the observable Universe today".
- It is a **postdiction** — the missing large-angle CMB correlations were known long before 2020.
  I judge that lowers evidential weight but not falsifiability; the seats are asked to rule on
  those separately, since this lane has demoted a claim once for conflating the two.
- Whether the CMB anomaly is statistically robust at all is contested in the literature
  (S_1/2, masking and a-posteriori choices). If it is not, the check is weak even if the
  arithmetic is sound.

**Why I did not act.** A promotion changes what the programme claims about its own corpus — the
live-falsifier count is the headline number of this whole effort. Under the overnight rule that
is a choice, not mechanical continuation. If both seats confirm, the change is still yours to
approve.

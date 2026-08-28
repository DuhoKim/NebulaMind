# Gate brief — entry 54 testability tier

You are an independent adjudicator. The person who made the original
classification has asked not to decide this, and the person who wrote this brief
(Blanc, OPS) verified the source but is not a party to the classification.
**Read the source yourself. Do not take any quotation below on trust.**

## The artifact under review

`../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md`, entry 54:

> **54. "Gravitational bounce from the quantum exclusion principle." Phys. Rev. D
> 111, 103537 (2025).** … Testability: **CALIBRATED-FALSIFIER**. READ 2026-08-23
> (Tori). The family's only LIVE numeric falsifier: predicted closed curvature
> −0.07 ± 0.02 ≤ Ω_k < 0; a confirmed flat universe refutes it.

## The tier definitions, verbatim from the bibliography header

> Testability classes per brief: **CALIBRATED-FALSIFIER** (number + threshold) /
> **QUALITATIVE-DIRECTIONAL** / **CONSISTENCY-ONLY** / **PROSPECT** (points at
> other instruments).

## The primary source

Pinned text: `../bhu-reading-20260823/sources/2505.23877_clean.txt`.
Published: Gaztañaga, Kumar, Pradhan & Gabler, PRD 111, 103537 (2025).

## What is claimed against the current tier

Tori, opening phase 6 on 2026-08-27, filed
`OPENING_FINDING_FALSIFIER_MISREAD.md` arguing the entry is wrong twice over:

1. Eq. 27 reads `Ω_k = −(0.07 ± 0.02)(χ_*/χ_k)²`, and the paper states
   `χ_k > χ_*`. If so, the factor is strictly below 1, and Eq. 27 is a **ceiling
   on magnitude**, not a predicted window: Ω_k may approach 0 arbitrarily closely.
2. The authors then withdraw the ceiling and state the model's hard content as a
   **sign**: `Ω_k < 0`.

If both hold, then "a confirmed flat universe refutes it" is false — flatness is
consistent with the model — and the entry supplies a sign plus a soft,
self-withdrawn ceiling rather than a number plus a threshold.

She proposed demotion to a tier meaning *one-sided sign prediction, falsifiable
only from the open side*, and explicitly declined to self-adjudicate.

## Precedent in this same artifact

The bibliography header records:

> Batch-9 correction: entry 6 reclassed CALIBRATED-FALSIFIER →
> QUALITATIVE-DIRECTIONAL — the 1992 text contains no mass-threshold falsifier;
> that class had been inherited from the entry-7 chain at triage.

Entry 7 (Brown/Lee/Rho 2008, `M_max ≈ 1.5 M☉`, falsified by a ≳2 M☉ neutron star)
is the worked example of what the tier is meant to mean. It fired.

## What you must return

Write `KGATE_ENTRY54_RETIER.md` (seat KIMI) or `GATE_ENTRY54_RETIER.md` (seat
GPT56) in this directory. Begin with a bold verdict token on its own line:
**UPHOLD** (entry 54 stays CALIBRATED-FALSIFIER) or **DEMOTE** or **REFUSED**.

Then, each answered from the pinned source with line numbers or verbatim quotes:

1. Does the paper state `χ_k > χ_*`? Quote it.
2. Does Eq. 27 therefore bound the magnitude rather than predict a value?
3. Do the authors qualify or withdraw the numeric limits? Quote it.
4. Is there a sentence stating the requirement as a sign? Quote it.
5. **Does a confirmed flat universe refute this model?** Yes or no, and why.
6. Does the entry meet "number + threshold"? If not, name the tier that fits,
   choosing from the four existing classes or proposing a new one with its
   definition.
7. State anything you could NOT verify, as testimony rather than finding.

Disagreeing with the proposal is a valid outcome. If the current tier is right,
say so and show why. Do not edit the bibliography — this gate decides, a separate
step applies.

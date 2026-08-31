# CALIBRATION ROBUSTNESS REHEARSAL RECEIPT — 2026-08-31

Machine-only, per the pace ruling: fixture mask (n=240, the path's own _fixture) and fixture calibration (_CAL); no science data, no imagery, no measured χ, no γ̂; v9 read-only via the verified manifest (incl. the ACTIVE confirmed mapping).

- grid: Γ = 0.25 ratified, Δγ = 0.01 derived, 51 points, j₀ = 25 verified EXACTLY zero, endpoints exactly ±Γ
- draws: 99 (SeedSequence(20260830).spawn(99), zero-based; CRN per draw); n_perm = 200 per cell
- mapping identity: `450c6a6ed43fc09005070c6a725f7ada89575ab0306ca25f58884028c7d0ed07` (convention commitment bound inside)
- evaluations: 5049 cells in 0.6 s
- baseline verdicts at γ=0 across draws: {'V:INCONCLUSIVE': 99}
- admissible γ span (uniform across draws unless VARIES): (-0.01, 0.01)
- INCONCLUSIVE-BY-CALIBRATION cells (the admissibility boundary the ±0.25 grid deliberately overshoots): 4752
- VERDICT FLIPS against each draw's own γ=0 baseline, worst case over draws: **0**
- outcome-matrix sha256: `2784944d2dd9619d77f782ae68a060f1fea77c6a24080d9b8e944d60180b4cfb`

**REHEARSAL OUTCOME: HELD** — no verdict flip anywhere on the evaluated grid, in any of the 99 draws. In the draft's own honest-limit language: HELD means only that no flip was found ON THE EVALUATED GRID; it is a machinery statement about fixture data, is NOT invariance_outcome = HELD, fills no slot, and discharges no BS-6 edge.

**STATUS: PROPOSAL — for the principal's ratification. The ONE new item the BS-3g sitting created:
the a-priori γ range endpoints, proposed from instrument specifications (ruling 2, 2026-08-30).**

# Proposed a-priori γ range: ±0.25

## The basis, from the preregistered instrument constraints — not from any measurement

The gain model is `a(c) = a₀ + γ·(c − c̄)`: classifier accuracy varying linearly with sky position.
Two preregistered facts bound how large a real |γ| can be **and still produce a run at all**:

1. **The per-bin calibration floor**: every bin must satisfy `a_LB_b ≥ 0.85`, and accuracy cannot
   exceed 1. So the maximum accuracy SPREAD across bins in any run that reaches a verdict is
   **0.15**.
2. **The bins are c-tertiles of the retained sample**, whose outer-tertile centres sit ≈ 0.7 apart
   in `c`.

A linear gradient surviving calibration therefore satisfies `|γ| ≲ 0.15 / 0.7 ≈ 0.21`. **Any
steeper gradient cannot pass the preregistered calibration gate — the run halts
`INCONCLUSIVE-BY-CALIBRATION` before a verdict exists for the invariance test to protect.**

## The proposal

**γ ∈ [−0.25, +0.25]** — the full calibration-admissible region with ~20 % margin, swept at
Δγ = 0.01 (51 grid points). The margin covers the approximation in taking tertile centres for the
lever arm and lets the sweep bracket the boundary rather than end on it.

**What this shape buys (the ruling's ground):** the bound's origin is the instrument's preregistered
acceptance constraints — outside the thing it bounds — so five rounds of self-declared-bound
findings close. **What it costs, stated:** if the real instrument's gradient were somehow steeper
than 0.25 *and* calibration failed to catch it, the sweep would not cover it; that compound event
requires the calibration gate itself to fail, which is a separate, already-guarded failure.

**Awaiting: ratify ±0.25, or set different endpoints.** Δγ = 0.01 stands either way (committed in
`ref/DRAW_MECHANICS_COMMIT_20260830.md`).

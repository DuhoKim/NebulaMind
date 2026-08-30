**STATUS: RATIFIED AS PROPOSED — 2026-08-30 20:19 KST, Γ = 0.25 (`GAMMA_RATIFICATION_20260830.md`, the principal's verbatim words recorded there). The body below is preserved as the proposal record.**

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

**Awaiting (v2, pre-reconciled with the grid commitment — GPT56-V89 F5): ratify symmetric
endpoints ±Γ; proposed Γ = 0.25.** The grid is committed as a STEP COUNT — `n_steps = 50`,
even (`DRAW_MECHANICS_COMMIT_20260830.md`, AMENDMENT 2) — so the spacing is DERIVED, never in
tension with the ratification: Δγ = 2Γ/50 (= 0.01 at the proposed Γ), grid γ_j = −Γ + j·Δγ for
j ∈ [0, 50], 51 points, both endpoints on the grid BY CONSTRUCTION for every symmetric choice,
γ=0 baseline at j₀ = 25 exactly. **The ratification asks ONE number: Γ.** Constraint stated
plainly: the endpoints are symmetric — an asymmetric range would need a new grid commitment.
(The v1 text here said a fixed Δγ = 0.01 stood for any endpoints — false for endpoints off the
0.01 lattice, e.g. ±0.253; the step-count form removes the collision for every possible
ratification, which is why it reaches the principal pre-reconciled.)

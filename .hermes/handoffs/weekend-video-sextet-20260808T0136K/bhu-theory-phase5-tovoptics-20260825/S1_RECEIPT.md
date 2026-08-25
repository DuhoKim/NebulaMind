# S1 receipt — the crossing shift, and a third analytic law
(2026-08-25 18:20 KST, Tori. Script s1_crossing_shift.py, run log _tmp_s1_run.txt, 6/6
limiting-case checks. Blind double NOT yet run for S1 — the brief specifies it for S0 and S2;
S1's central claim is instead PROVEN algebraically below, which is stronger.)

## The result: β_rel = −1/√N, exactly

The relative velocity between the FRW-side fluid and the TOV-side fluid at the shock is

**|β_rel| = 1/√N — the reciprocal of the shock's distance in Hubble lengths.**

**Proof (DERIVED; uses only pinned relations).** Write X = 1+u, Y = σ−u. From (4.5),
v₁ = s = √N·Y/X. From the textbook relativistic shock relation v₁v₂ = (p₂−p₁)/(e₂−e₁)
(Landau & Lifshitz, *Fluid Mechanics*, relativistic shocks), v₁v₂ = Y/(1−v). The pinned
constraint (4.3) gives 1−v = X(1+σ)/(X+YN), hence v₂ = (X+YN)/((1+σ)√N). Then

  v₁ − v₂ = [NY² − X²] / (X(1+σ)√N)     [using 1+σ−X = Y]
  1 − v₁v₂ = [X² − NY²] / (X(1+σ))      [using 1+σ−Y = X]
  β_rel = (v₁−v₂)/(1−v₁v₂) = (NY²−X²)/(√N(X²−NY²)) = **−1/√N**  ∎

u and v cancel completely: the relative velocity depends on nothing but the shock's distance.

Numerically confirmed on the gated A1 orbit: absolute deviation ≤ 1.9×10⁻⁸ over ten decades,
and the relative deviation falls monotonically 5.9e-4 → 3.7e-8 → 5.0e-11 → 2.8e-13 → 3.2e-14
as the cancellation parameter σ−u grows — the conditioning signature of an exact law computed
from finite-precision inputs, not of an approximate one. (Diagnostic history is kept in the
script: three wrong explanations were eliminated first — my arithmetic via a 50-digit
recompute, the s column via its pinned formula, and independent (u,v) storage via computing v
from constraint (4.3). The check was not tuned to pass; the cause was found.)

## Why it matters

**Combined with z_c = √N (Phase 4's law), β_rel = 1/z_c at the center crossing.** The two
laws are reciprocal: the further away the boundary in Hubble lengths, the higher the crossing
redshift AND the slower the two fluids move relative to each other. Early = distant, quiet
boundary; late = near, violent boundary.

## The crossing shift, at the point our light cone actually reaches

Observer at the horizon-crossing epoch, crossing at √N = 2.5498 (gated A1): β_rel = 0.3922,
γ = 1.0871. The Doppler factor across the junction, by viewing angle:

| viewing angle | 1+z_cross | fractional shift |
|---|---|---|
| head-on (μ=+1) | 1.5134 | **+51.3%** |
| μ=+0.5 | 1.3003 | +30.0% |
| transverse | 1.0871 | +8.7% |
| μ=−0.5 | 0.8739 | −12.6% |
| receding (μ=−1) | 0.6607 | **−33.9%** |

**This is an order-unity, strongly angle-dependent imprint — not a perturbation.** Taken with
S0's τ ≈ 0.3 (marginally transparent), a boundary-crossing line of sight is neither hidden nor
faintly modified: it carries a tens-of-percent frequency shift that varies across the patch.

## Limits, stated

- Which of blue/red applies to an inward-crossing ray depends on the geodesic's direction
  relative to β_rel, which is S2's geometry — the table gives the magnitude and the angular
  span, not the sign for a specific sight line.
- σ = 1/3 throughout; the "rough qualitative models" caveat travels.
- The textbook shock relation is cited, and its adaptation to these variables is DERIVED.
- LC3 correction on the record: my first compressive-shock check assumed the FRW side was
  upstream. It is downstream — v = ρ̄/ρ < 1 makes the TOV side the thinner, upstream side.
  The check was wrong, not the physics.

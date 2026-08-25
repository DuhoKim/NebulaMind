# S0 receipt — the exterior is marginally transparent at cosmological anchors
(2026-08-25 17:40 KST, Tori. Script s0_optical_depth.py; run log _tmp_s0_run.txt;
4/4 limiting-case checks pass. Blind double dispatched to gpt1 — this receipt is PRE-double
and no S0 result is final until the two agree.)

## Result

At the point where an interior observer's past light cone crosses the shock (observer at the
horizon-crossing epoch: z_c = 2.5496, √N = 2.5498, v = ρ̄/ρ = 0.42997, emission at
t_e = 0.0794 t_crit — all read from the gated A1 orbit), the Thomson optical depth over one
shock radius is

    τ_R = (3 κ_T c / 16πG) · v √N / t_e,   prefactor = 1.0662e16 s   [DERIVED]

**τ_R = 1 at an anchor t_crit = 1.47e17 s = 4.67 Gyr = 0.34 Hubble times.**

| anchor t_crit | τ_R |
|---|---|
| 1 s | 1.5e17 |
| 1 yr | 4.7e9 |
| recombination-ish (380 kyr) | 1.2e4 |
| 1 Gyr | 4.7 |
| Hubble time (13.8 Gyr) | **0.34** |
| 10³ × Hubble | 3.4e-4 |

## What this decides — and it is not what the brief expected

The freeze addendum (written before any number) split S0 into a PHOTOSPHERE branch (τ ≫ 1, we
see an emitting surface) and a TRANSPARENT branch (τ ≪ 1, small perturbation). **The answer at
cosmologically plausible anchors is neither: τ_R ≈ 0.3, order unity.** Both effects are
present, as the addendum's third case anticipated. Consequences for S1–S3:

1. The exterior is NOT optically negligible. A ray crossing the shock is substantially
   modified, which is the first quantitative reason to expect crossing to be OBSERVABLE — the
   missing ingredient behind Phase 4's forced "sufficient, not necessary."
2. Neither the pure-photosphere nor the pure-transparent simplification may be used. S2 must
   carry a partial-absorption transfer with an emission term.
3. The transition is anchor-steep (τ ∝ 1/t_crit): a universe with an earlier horizon crossing
   is opaque by orders of magnitude, a later one transparent. The anchor is therefore not a
   nuisance parameter — it is the phase's main dial, and it is already bounded by this.

## Honest limits on this number

- σ = 1/3 throughout: the model has no matter era, so "anchor = Hubble time" is a crude map to
  our universe. The pinned source calls these "only rough qualitative models"; the caveat
  travels with τ_R.
- Ionized-hydrogen composition is a DECLARED assumption (K3), not a derived one: the matching
  equations fix the exterior's equation of state, not its composition.
- τ_R uses the shock's areal radius as the path length — one scale height, not an integral
  along the actual TOV-side path. That integral is S1/S2 work and can move this by a factor of
  a few, not by orders of magnitude, unless the path geometry surprises us.
- PRE-BLIND-DOUBLE. gpt1 is computing the same quantity from the stated physics without seeing
  this. If the two disagree, this receipt is wrong until reconciled.

# P6 receipt — the genuine path transfer, and it overturns P5's background term
(2026-08-26. p6_path_transfer.py, log _tmp_p6_run.txt, 5/5 checks. Answers REGATE2 findings
1–3. NOT yet blind-doubled; nothing here is claimed as confirmed.)

## What P6 adds that P5 lacked

P5 was a single screen: all emission at the junction, one opacity for the whole sky, no source
range. P6 integrates the transfer along the ray, with a separate exterior solved **for every
direction** (each has its own crossing epoch, hence its own ρ̄, N, τ and profile).

The piece P5 did not have is the **depth-to-junction redshift**, derived here from the pinned
metric: for a radial photon k_t̄ is conserved and the null condition gives ṙ̄² = AE²/B, so with
the comoving u^r̄ = √(N−1) each fluid element measures ω = E/√|B| — and a photon emitted at
depth arrives at the junction shifted by **√(|B(r̄)|/|B_junction|)**, with B integrated from
pinned (3.4). Only the ratio matters, so the normalisation is not an assumption.

## The consequence, and it is not small

**B → 0 at the horizon, so Z → 0** (measured: 1.0 at the junction → 1.2×10⁻⁵ at the horizon).
That is standard horizon behaviour — light emitted at a horizon is infinitely redshifted — and
it means:

1. **Deep emission is suppressed**: the emergent beam comes from the near-junction region.
2. **P5's transmitted-background term is WRONG.** P5 carried a background arriving through the
   exterior at strength e^(−τ). There is no such background: the sight line terminates at the
   horizon, and anything from beyond arrives redshifted by ~10⁻⁵. Nothing comes through.
3. **The crossing sky is DARK** — the emergent temperature is a few percent of the interior
   background (monopole −0.93 at the junction-value closure), not a Doppler-shifted copy of it.

## Result

| w | τ_tot | dipole c₁ | bound on x_off/r_*(cross) |
|---|---|---|---|
| 0.999 | 0.037 | 3.844 | 3.53e-4 |
| 0.500 | 0.058 | 3.666 | 3.70e-4 |
| 0.2456 | 0.132 | 3.441 | 3.95e-4 |
| 0.100 | 0.308 | 3.051 | 4.45e-4 |
| 0.030 | 0.930 | 1.503 | **9.04e-4** |
| 0.010 | 2.603 | 2.257 | 6.01e-4 |

**Bound: 3.5×10⁻⁴ to 9.0×10⁻⁴ — one part in 1107 at worst, one part in 2832 at best.**
P5's single-screen treatment gave 2.2×10⁻³ to 5.5×10⁻³, so **the proper path transfer TIGHTENS
the exclusion by a factor of 3–6**, because a dark patch is a louder signal than a shifted one.

## Two things I am flagging rather than smoothing

- **The trend is not monotone**: c₁ falls to 1.50 at w = 0.03 and rises again to 2.26 at
  w = 0.01. P5's clean saturation picture does not survive depth resolution, and I do not yet
  understand the turn. It does not threaten the bound (the worst case is the dip, and the dip
  is still one part in 1107), but "saturates at a floor" is no longer the right description and
  I am not claiming it.
- **The gate's finding 2 is therefore partly vindicated**: the 0.2461 floor WAS a property of
  the fixed-crossing-source model. What survives is the weaker, sufficient statement that the
  dipole stays large at every computed opacity — not that it approaches a limit.

## Standing limits

σ = 1/3, pre-horizon, photon channel; A4 at its LTE upper end (the energy-budget ceiling);
crossing-radius normalisation per the gate's B1 ruling; B normalised at the junction. Blind
double owed before any of this is claimed as confirmed.

# A4 receipt — the prediction functions, closed (2026-08-24 ~09:55 KST, Tori)

Script `a4_prediction_functions.py`, outputs `a4_regime_map.csv` (288 rows), 5/5 checks after
one honest correction (below). All in the σ=1/3 model, A2 units; digits model-internal,
structure robust (S1's own "only rough qualitative models" caveat rides along).

## The correction A4 forced on A3

A4's first run FAILED its own "hidden regime: any offset allowed" check — correctly. t_vis is
the center's first visibility; offset observers see the boundary earlier. With opacity folded
in (z > z_ls crossings are unobservable — the pre-recombination universe is opaque), the A3
trichotomy collapses to a DICHOTOMY with one constraint surface. A3 receipt carries a dated
correction addendum. Second self-correction of the phase, both caught by the machinery.

## The prediction functions

**P1 — z_c(μ; x_off, t_obs)** (A2 solver + analytic laws): boundary-crossing redshift.
Center law z_c = √N(η_e); nearest-direction bound x_max(z; t_obs) = η_o[(1+√N(η_e))/(1+z) − 1].

**P2 — the constraint surface x_max(t_obs)** at z_ls = 1100: consistency with the observed
uniform CMB sky ⇔ NO CAP ⇔ x_off < x_max(t_obs). Sampled (x_max as fraction of the comoving
shock radius; the t = 0.14 value is from the in-script check `cap opens exactly at x_max(t)`,
not from the delivered map, which starts near 0.98 t_vis — gate correction): t = 0.14 (half
t_vis): **0.20** (one sample, not a summary of all early observers); t = 0.274 (≈t_vis): **4.3×10⁻³**; t = 0.277
(band middle): **5.7×10⁻⁴**; t → t_1100 = 0.27744: **0**. Below the surface the model is
consistent AND the boundary is strictly unobservable (opacity + interior exactness): the
consistent region is observationally EMPTY of signatures — consistency bought at the price of
untestability, the K2 closure quantified.

**P3 — the cap** (analytic sphere–sphere geometry): where the LSS pokes past the shock, a
single circular cap around the offset direction, with
μ_c = (ρ_s² − x² − χ_ls²)/(2xχ_ls). Growth just past the bound (band-middle t):

| x/x_max | θ_cap | sky fraction | ℓ ~ π/θ |
|---|---|---|---|
| 1.001 | 2.6° | 5.0×10⁻⁴ | ~70 |
| 1.01  | 8.1° | 5.0×10⁻³ | ~22 |
| 1.1   | 24.6° | 4.5×10⁻² | ~7 |
| 1.5   | 48.2° | 0.17 | ~4 |
| 2.0   | 60.0° | 0.25 | ~3 |

So the model's only observable near-threshold signature is a SINGLE large-angle circular
patch of boundary-affected CMB around one direction — reaching the anomaly multipoles
(ℓ ≲ 10) already at 10% past the bound. Whether any claimed CMB anomaly has that morphology
(one cap, one direction, generic TOV-side amplitude) is Track C's question against gpt2's
frozen bounds; nothing here presumes the answer.

## What Track B/C confront, and with what

- H₀-anisotropy bounds (agy): NOT-A-DISCRIMINANT (A3 observable (b), null by exactness).
- CMB uniformity + anomaly morphology (gpt2): confronts P2/P3.
- The conspiracy escape (TOV side mimicking FRW across the cap) remains the one unmodeled
  out; any Track C verdict must name it.

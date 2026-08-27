# Blind P7 independent dipole-cancellation search (seat gpt1)

## Answer

**Yes.** With the future-directed junction Doppler sign fixed as described below, the signed temperature-dipole response crosses zero at

- `w_null = 0.0815000315521`.

Using the criterion that even an offset as large as the centered crossing radius would remain below the stated intrinsic-dipole limit, the dipole-linearized offset inference is completely uninformative over

- `0.0813055784488 < w < 0.0816945546057`,
- width `Delta w = 0.000388976156893`.

The signed response is positive below the null and negative above it. Here “positive” means the fitted temperature is hotter toward `mu=+1`, the direction of the displacement vector.

## Blindness and custody

I used only `BRIEF_GPT1_BLIND_P7.md` and its explicitly pinned orbit table, `../../bhu-theory-phase4-anisotropy-20260823/a1_results.csv`. I did not read any forbidden script, receipt, verdict, P6 artifact, or prior gpt1 blind-P6 work. All writes are in this directory. There are no commits.

Products:

- `p7_blind_dipole.py`: complete reproducible calculation.
- `signed_dipole_vs_w.csv`: 998-row signed coefficient table (the 0.001 grid from 0.005 through 0.999, plus the two threshold crossings and exact null).
- `results.json`: machine-readable central result and all stability runs.
- `GPT1_P7_DONE.md`: completion marker.

Run with:

```bash
python3 p7_blind_dipole.py
```

## Observable and sign decisions

### Geometry and offset normalization

For each Gauss-Legendre direction cosine `mu`, the script solves the pinned crossing equation continuously,

`|x_off + chi n| = r_*(2-chi)`,

with a bracketed Brent solve. The offset is normalized by the centered observer's past crossing radius,

`r_center = r_*(eta_center) = 2-eta_center = 1.43661131453868`.

This radius is preferable to the instantaneous shock radius at observation because it is the actual geometric lever arm of the crossing sphere whose angular dipole is being measured. The centered solution is

- `eta_center = 0.563388685461317`,
- `sqrt(N)_center = 2.54994704652678`,
- `beta_center = 0.392165006470262`.

The production derivative uses `x_off/r_center = 10^-4`; the stability section shows that it is in the linear regime.

### Junction frequency factor

Let `q = n dot rhat` at the crossing, where `n` points from observer to the crossing. Inside the horizon, decreasing areal radius is future-directed for the comoving exterior. With that time orientation, the exterior-to-FRW frequency factor is

`D = gamma (1 + beta q)`,  `beta = 1/sqrt(N)`.

This fixes the sign rather than choosing it to obtain a zero. At the centered radial crossing it gives the familiar approaching-frame factor `gamma(1+beta)`. Reversing this physical time orientation would define a different transfer problem.

### Source temperature

At each crossing,

`rho_bar = v rho_FRW = v * 3/(2 pi eta^4)`.

For constant imposed exterior `w`, the adiabatic law gives

`d ln T_source = [w/(1+w)] d ln rho_bar`.

The script integrates this equation from the centered crossing with DOP853 over the continuous PCHIP representation of the pinned orbit data. The arbitrary common source-temperature normalization cancels from the normalized observable. The endpoint identity

`ln T_source = [w/(1+w)] ln rho_bar + constant`

was independently checked: its maximum discrepancy from the numerical integration at the null (256 angular nodes, `rtol=10^-12`) was `5.08e-15` in log temperature.

The supplied field equations are not used to invent an additional path-redshift factor. This is deliberately a calculation of the **crossing imprint** named in the question: the boundary values `N`, `rho_bar`, and `p_bar` are pinned by the gated orbit data. A separate integration of `B` would require an emission radius and a boundary normalization for `B`, neither of which the brief specifies. Adding one would change the question by inserting an unpinned exterior source surface. The imposed EOS enters exactly where specified: the adiabatic evolution away from the narrow junction transition; the tabulated `u/v` is retained as the local transition value and is not falsely forced to equal the swept constant `w`.

### Bolometric normalization and fitted dipole

For every direction the code first forms bolometric intensity

`I(mu) proportional to [D(mu) T_source(mu)]^4`.

It then normalizes intensity by its full-sky mean and defines the equivalent bolometric temperature

`Theta(mu) = [I(mu)/<I>]^1/4`,

renormalized by `<Theta>` (a common factor that does not alter the null). The reported signed coefficient is

`C(w) = (3/2) integral[-1,1] mu Theta(mu) dmu / (x_off/r_center)`.

Thus the predicted dipole temperature is `Delta T_1/T0 = C(w) x_off/r_center` in the linear regime.

At the null, an independent component split gives

- Doppler-only coefficient: `+0.615243280090`,
- adiabatic-source-only coefficient: `-0.615243281351`,
- combined coefficient: `-1.53e-12` (256-node check).

The cancellation is therefore between the two physical effects named in the question, not between numerical artifacts.

## Why angular and w sampling cannot hide sign structure

The sky integral is not evaluated by point sampling. It uses Gauss-Legendre quadrature, while every directional crossing is a bracketed continuous root solve over PCHIP interpolation of the full 40,001-row orbit table.

The 401-point `w` scan is used only to locate sign brackets. The reported null and both interval edges are then solved with Brent's method. Moreover, in the offset-linear limit the Doppler contribution is independent of `w`, while the source contribution is a fixed geometric derivative multiplied by `p(w)=w/(1+w)`. Since `p(w)` is strictly increasing on the entire requested domain and the measured fixed density-gradient coefficient is negative (`-8.16423767600` per unit `p`), `C(w)` is strictly decreasing. Hence there can be at most one null; the bracketed one is unique. The full scan spans coefficients from `+0.574625182367` to `-3.46483348231`.

## “Too small to constrain anything” threshold

The observational fractional limit is

`L = 3.7 mK / 2.7255 K = 0.00135754907356`.

For dipole-only offset inference with the geometric prior `0 <= x_off/r_center < 1`, the upper bound inferred from a nondetection is

`x_off/r_center < L/|C(w)|`.

If `|C(w)| < L`, that bound exceeds unity and does not restrict the offset anywhere inside the crossing sphere. I therefore define the unconstrainable region by `|C| < L`. Brent solves of `C=+L` and `C=-L` give the interval and width reported above. This is explicitly a statement about the dipole-linearized constraint; higher multipoles or a nonperturbative large-offset analysis could still supply information.

## Stability: the null is not numerical

### Angular quadrature order

| order | null w | left edge | right edge |
|---:|---:|---:|---:|
| 32 | 0.0815000315521 | 0.0813055784490 | 0.0816945546053 |
| 64 | 0.0815000315519 | 0.0813055784488 | 0.0816945546053 |
| 128 | 0.0815000315521 | 0.0813055784488 | 0.0816945546057 |
| 256 | 0.0815000315520 | 0.0813055784487 | 0.0816945546056 |

The root spread is below `2.7e-13` in `w`.

### Offset magnitude

| x_off/r_center | null w | left edge | right edge |
|---:|---:|---:|---:|
| 1.0e-3 | 0.0815000312311 | 0.0813055781732 | 0.0816945542391 |
| 3.0e-4 | 0.0815000324301 | 0.0813055793329 | 0.0816945554774 |
| 1.0e-4 | 0.0815000315521 | 0.0813055784488 | 0.0816945546057 |
| 3.0e-5 | 0.0815000316266 | 0.0813055785234 | 0.0816945546798 |

The maximum root displacement is `1.20e-9`, demonstrating convergence to the offset derivative. (The tiny nonmonotonic last digits are floating-point cancellation when dividing an already tiny dipole by a tiny offset.)

### Adiabatic integrator tolerance

| DOP853 rtol | null w | left edge | right edge |
|---:|---:|---:|---:|
| 1e-8 | 0.0815000315521 | 0.0813055784488 | 0.0816945546057 |
| 1e-10 | 0.0815000315521 | 0.0813055784488 | 0.0816945546057 |
| 1e-12 | 0.0815000315521 | 0.0813055784488 | 0.0816945546057 |

All shown digits are unchanged. Combined with the analytic endpoint check and quadrature/offset tests, this rules out a numerical null.

# Blind Phase-5 P5 result (seat gpt1)

## Blindness and inputs

This is an independent computation. I used only `BRIEF_GPT1_BLIND_P5.md` and the brief-authorised gated orbit table `bhu-theory-phase4-anisotropy-20260823/a1_results.csv`. I did not read or import any of the forbidden transfer scripts, receipts, or S2/S3 files.

The orbit table supplies `t_over_tcrit`, `sqrtN_hubble_lengths`, and `v_rhobar_over_rho`. Positive quantities are interpolated with shape-preserving cubic interpolation in log(time)-log(value) space. The last orbit row is the observing epoch: `t_obs/tcrit = 0.999999985`.

## Choices required by the brief

### 1. Observable normalisation

I compare the *fractional sky anisotropy*,

`delta(mu) = T(mu)/<T>_sky - 1`,

not the raw temperature before removal of its monopole. The common shock-frame Doppler factor is a large, direction-independent shift for a centred observer; it is therefore a monopole calibration, not an observable intrinsic dipole. Normalising by the computed all-sky mean is also the correct way to apply the published ratio `3.7 mK / 2.7255 K = 0.00135754907356`.

The requested offset is normalised by the shock radius at the observing epoch,

`epsilon = x_off / r_*(eta_obs)`.

Here `r_*(eta_obs) = 1.999999995` in the table's comoving units. This is the unique direction-independent radius that defines whether the observer is inside the shock at the epoch where `x_off` is specified. I do not use the centred crossing radius: an off-centre past light cone crosses at a direction-dependent time, so that radius would itself acquire the anisotropy being measured.

### 2. Exterior source and its bounds

I use the formal transfer solution in thermodynamic/Rayleigh-Jeans temperature units,

`T_raw(mu,tau) = D(mu) [ exp(-tau) + (1-exp(-tau)) lambda q(mu) ]`,

where the incident common CMB scale is one, `q = T_ext/T_FRW = v^(1/4)`, and `0 <= lambda <= 1`. Equal radiation constants give the LTE upper source temperature from the supplied density ratio: `T_ext/T_FRW = (rhobar/rho)^(1/4)`. `lambda=1` is the chosen physical thermal/LTE source; `lambda=0` is the conservative no-emission lower endpoint. For every finite tau the normalised multipoles at intermediate lambda are bounded by the two endpoint columns in `p5_opacity_sweep.csv` because both the unnormalised Legendre moment and monopole are linear in lambda and the monopole is positive.

A saturated absorber with exactly `lambda=0` has vanishing absolute intensity and cannot be identified with the measured 2.7255 K CMB monopole. I retain it only as a formal lower-source endpoint. The physically meaningful opaque limit is the LTE/source-dominated endpoint.

The exterior's own thermal emission **is Doppler shifted at crossing**. It is isotropic in the exterior-fluid rest frame, not in the local FRW frame of the interior observer. In the FRW frame the static-exterior fluid moves inward, parallel to the received inward ray at a centred crossing. I therefore use

`D = gamma [1 + beta (n . e_r)]`, `beta = 1/sqrtN`,

with `e_r` the outward radial unit vector at the crossing. Applying this factor to the thermal source is essential: omitting it would artificially force the anisotropy to zero when the background becomes opaque.

### 3. Constrained multipole

The published intrinsic/non-kinematic CMB *dipole* limit constrains the Legendre `l=1` coefficient. For this axisymmetric geometry I compute

`a_l = (2l+1)/2 integral[-1,1] delta(mu) P_l(mu) dmu`.

For a small offset, `a1 = C1 epsilon + O(epsilon^3)` and `a2 = C2 epsilon^2 + O(epsilon^4)`. Thus the dipole is the binding small-offset constraint. At the dipole-derived bounds, the computed LTE quadrupole is only `2.41e-7` to `5.94e-7` fractionally (about `0.66` to `1.62` microkelvin), so it does not replace the stated dipole limit.

## Geometry and central crossing

For every quadrature direction the script solves the supplied equation directly:

`|x_off zhat + chi n| = r_*(eta_obs-chi)`.

At zero offset the crossing is

- `t_cross/tcrit = 0.0793516999557`
- `sqrtN = 2.54994708188`
- `beta = 0.392165001033`
- `v = 0.429999345169`

## Main numerical result

`C1(tau)` below is the dipole coefficient per unit `x_off/r_*(eta_obs)`. The bound is

`x_off/r_*(eta_obs) < (3.7 mK / 2.7255 K) / |C1(tau)|`.

| tau | C1, LTE thermal source | bound, LTE | C1, no-emission endpoint | bound, no-emission |
|---:|---:|---:|---:|---:|
| 0 | 0.856520158 | 0.001584959 | 0.856520158 | 0.001584959 |
| 0.15 | 0.796973144 | 0.001703381 | 0.856520158 | 0.001584959 |
| 1 | 0.557494710 | 0.002435089 | 0.856520158 | 0.001584959 |
| 5 | 0.346859082 | 0.003913835 | 0.856520158 | 0.001584959 |
| 20 | 0.342589571 | 0.003962611 | 0.856520158 | 0.001584959 |
| 25 | 0.342589570 | 0.003962611 | 0.856520158 | 0.001584959 |

The full 44-point sweep from `tau=0` through saturation at `tau=25` is in `p5_opacity_sweep.csv`. Across that full range, the physical LTE result is

- `0.342589570 <= C1(tau) <= 0.856520158`
- `0.001584959 <= x_off/r_*(eta_obs) bound <= 0.003962611`.

Across the source bracket `0 <= lambda <= 1`, each finite-tau result lies between the LTE and no-emission endpoint columns. In the independently supplied `0 <= tau <= 0.15` range, the LTE bound only relaxes from `0.001584959` to `0.001703381`.

## Plain opacity conclusion

Opacity **weakens but does not erase** the anisotropy. In the LTE opaque limit the incident CMB is replaced by exterior thermal radiation, but that radiation is Doppler shifted at the moving crossing and its temperature also samples direction-dependent crossing times. The coefficient saturates at `C1 = 0.34258957`, rather than approaching zero. Therefore opacity cannot hide an arbitrary offset: even a saturated exterior gives `x_off/r_*(eta_obs) < 0.00396261` under the stated model.

The formal `lambda=0` endpoint also does not cancel the *normalised* pattern, because attenuation is common and divides out of `T/<T>`; however its absolute monopole vanishes as tau grows, so that endpoint is not a physical high-opacity CMB explanation.

## Limiting and numerical checks run

The raw check table is `p5_checks.csv`.

1. **Centred observer:** for tau `0, 1, 25` and both source endpoints, `a1` and `a2` are zero to at worst `1.4e-30`.
2. **Transparent limit:** at tau=0 the source term disappears, so LTE and no-emission results agree exactly: `C1=0.856520158`.
3. **Opaque saturation:** LTE changes by less than the printed precision between tau=20 and tau=25, settling at `C1=0.34258957`.
4. **Pure attenuation:** at `lambda=0`, opacity multiplies every direction by the same `exp(-tau)` and cancels from the mean-normalised sky; the numerical `C1` range over all 44 tau values is only `5.8e-13` wide.
5. **Offset convergence:** changing the finite offset from `2.5e-5` through `2e-4` changes `C1(tau=0)` by about `3e-8` and `C1(tau=25)` by about `2e-8` absolute. The reported sweep uses `epsilon=5e-5`.
6. **Angular quadrature:** at tau=1 LTE, 64, 128, 256 and 512 Gauss-Legendre nodes all give `C1=0.55749471033` to better than `8e-13`. The production sweep uses 256 nodes.
7. **Multipole scaling:** the quadrupole divided by `epsilon^2` converges while the dipole divided by `epsilon` converges, confirming the expected even/odd offset orders.

## Files and reproduction

- `compute_blind_p5.py`: independent light-cone, transfer, and multipole calculation
- `p5_opacity_sweep.csv`: full opacity sweep and both source endpoints
- `p5_checks.csv`: convergence and limiting checks
- `summary.txt`: concise numerical summary

Reproduce from this directory with:

```bash
python3 compute_blind_p5.py \
  --input /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-theory-phase4-anisotropy-20260823/a1_results.csv
```

The script requires Python, NumPy, and SciPy and writes only into its `--outdir` (this directory by default).

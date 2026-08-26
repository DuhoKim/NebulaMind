# GPT1 blind P2b: off-centre transfer anisotropy

## Blindness and inputs

This calculation was made independently from the brief. I did **not** read any of the prohibited P2b/P2-P4 scripts or receipts, or any S2/S3 file. The computation reads only:

- `BRIEF_GPT1_BLIND_P2B.md`;
- the gated orbit table `bhu-theory-phase4-anisotropy-20260823/a1_results.csv`.

The natural observation epoch is the endpoint of the gated orbit, `t_obs/t_crit=1`, so `eta_obs=2`. The centred crossing occurs at

- `eta_c = 0.5633886854613174`;
- `t_c/t_crit = 0.0793517027264578`;
- `sqrtN_c = 2.549947046526777`, hence `beta_c = 0.3921650064702624`;
- `r_*c = chi_c = 1.4366113145386896`.

All offsets below are normalised by this centred-crossing radius, `epsilon=x_off/r_*c`.

## Choices requested by the brief

### 1. Observable normalisation

I use the sky-mean-normalised thermodynamic temperature contrast

`Delta(mu) = T(mu)/<T>_sky - 1`,

not the raw frequency/temperature transfer. This is the appropriate comparison with a published non-kinematic CMB dipole: the measured `T0` is the observed monopole, while a common transfer shared by every direction is not a dipole and can be absorbed into the unknown source monopole. The centred sky has a large common raw transfer (`0.4263150181` in the adopted convention) but exactly zero anisotropic multipoles.

The axisymmetric Legendre convention is

`Delta(mu) = sum_l A_l P_l(mu)`,

with `mu` measured from the displacement axis. Thus the temperature dipole amplitude is `T0 |A_1|`. If spherical-harmonic coefficients are desired, `a_10=sqrt(4 pi/3) A_1`; the observational limit is applied to the physical cosine-law amplitude `|A_1|`, not directly to `|a_10|`.

### 2. Transfer and exterior source function

For a ray whose backward sightline is `n`, the arriving photon propagates along `-n`. At the crossing let `e_r` be the outward radial unit vector and `c=n.e_r`. Taking the FRW fluid to move outward at the given relative speed,

`u_FRW = gamma (u_TOV + beta e_r)`,

so the frame transfer is `gamma(1+beta c)`. Radiation-era propagation from crossing to observation contributes `a_c/a_obs=eta_c/eta_obs`. The raw directional factor is therefore

`F(mu) = (eta_c/eta_obs) gamma_c [1 + beta_c c(mu)]`.

The crossing time is solved independently for every direction from the condition in the brief.

For the partially opaque exterior I use the standard no-maser formal solution in brightness-temperature units,

`T_out = exp(-tau) T_inc + [1-exp(-tau)] S`,

and choose the passive/isotropising bound `0 <= q=S/T_inc <= 1`. This spans pure absorption (`q=0`) through conservative isotropic re-emission/scattering (`q=1`) without inventing an unconstrained hot exterior. If the exterior source is correctly placed before the shock, both incident and source photons acquire the same `F(mu)`, and a direction-independent `tau,q` cancel exactly from `T/<T>`; this is the preferred physical result.

I also report a deliberately conservative placement bracket in which the source is treated as an isotropic monopole added after the anisotropic factor. This maximises dilution compatible with the same passive bound. It multiplies every anisotropic coefficient by

`W = exp(-tau)/[exp(-tau)+(1-exp(-tau))q]`.

For `0<=tau<=0.15` and `0<=q<=1`, `exp(-0.15)<=W<=1`, i.e. `0.8607079764<=W<=1`. This bracket contains the preferred exterior-source result (`W=1`) and makes the opacity dependence explicit. A source hotter than the incident monopole was not selected because no temperature information was supplied; allowing an arbitrarily hot source would make the dipole arbitrarily dilute and the requested bound mathematically unclosed.

### 3. Constrained multipole and which one binds

The published intrinsic/non-kinematic dipole limit constrains the `l=1` coefficient `A_1`. Near the centre, odd multipoles are odd in offset and even multipoles are even; therefore the dipole is linear while the quadrupole begins at second order. At the strict dipole bound the computed quadrupole is only `1.04e-7`, versus `|A_1|=1.35755e-3`, so the dipole is the binding multipole in the small-offset regime selected by the data. No independent quadrupole observational limit was supplied, so I do not substitute one.

## Result

The numerical odd derivative is

`A_1 / (x_off/r_*c) = +2.28714342`

(the sign only records which pole is labelled positive). With the conservative source bracket:

`|A_1| / |x_off/r_*c| = 1.96856259 to 2.28714342`.

The observational fractional limit is

`3.7 mK / 2.7255 K = 1.3575490736e-3`.

Therefore

- preferred exterior-source / no-dilution bound: `|x_off|/r_*c < 5.93557e-4`;
- maximally diluted passive-source bound at `tau=0.15, q=1`: `|x_off|/r_*c < 6.89614e-4`;
- combined reported range: **`|x_off|/r_*c < (5.94--6.90)e-4`**.

At the upper end the raw geometric dipole is `1.57725e-3`; multiplication by `exp(-0.15)` gives the stated observational limit.

## Limiting and numerical checks actually run

1. **Centred observer:** all directions return the same transfer; all `l>=1` coefficients vanish to quadrature precision.
2. **Small-offset convergence:** the odd finite-difference slopes for `epsilon=1e-3, 5e-4, 2e-4, 1e-4` were `2.2871415350, 2.2871429893, 2.2871433951, 2.2871434227`.
3. **Parity:** replacing `x_off` by `-x_off` reverses `A_1`; the central odd difference is what is reported.
4. **Opacity/source limits:** `tau=0` gives `W=1`; `q=0` gives `W=1` for every `tau`; `q=1,tau=0.15` gives `W=0.8607079764`. A genuinely exterior, isotropic source multiplied by the same shock factor cancels from the normalised contrast.
5. **Binding multipole:** at `epsilon=5.93557e-4`, `(A1,A2,A3,A4)=(1.3575487e-3, 1.0439e-7, -1.09e-12, -2.77e-11)`.
6. **Orbit interpolation thinning:** repeating with every 2nd, 4th, and 8th gated row gave slopes `2.28714319`, `2.28714195`, and `2.28714837`; the largest relative change from the full-table result is below `2.2e-6`.

## Files and reproduction

- `compute_blind_p2b.py` — independent solver and multipole integrator.
- `check_limits.py` — executable centred-sky and source-limit assertions.
- `p2b_results.csv` — finite-offset convergence table.
- `summary.txt` — machine-readable key-value results.
- `checks/stride{2,4,8}/` — interpolation-thinning reruns.

Run from this directory:

```sh
python3 compute_blind_p2b.py
```

Requirements: Python 3, NumPy, SciPy. The script writes only inside the output directory and makes no commits.

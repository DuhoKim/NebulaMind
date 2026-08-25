# Blind Phase-5 S0 Thomson optical depth (gpt1)

This directory is an independent calculation using only the physics in the blind brief and the named Phase-4 CSV.

## Result

For an observer at `t_obs = t_crit`, the light-cone crossing is

- `x = t_e/t_crit = 7.935170038413607e-2`
- `sqrt(N_e) = 2.549947098920840`
- `v_e = rhobar/rho = 4.299993431279523e-1`
- `1 + z = 3.549947098920840`

With the path-length choice below, the Thomson depth is

`tau_T = (1.473307868145080e17 s) / t_crit`.

Therefore:

- `tau_T = 1` at `t_crit = 1.473307868145080e17 s`.
- Smaller anchors (`t_crit < 1.473307868145080e17 s`) are optically thick.
- Larger anchors (`t_crit > 1.473307868145080e17 s`) are optically thin.

The decade table from 1 s through 1e20 s is in `s0_optical_depth_vs_tcrit.csv`.

## Derivation

For `sigma = 1/3`, the supplied density law reduces to

`rho(t) = 3 / (32 pi G t^2)`.

At crossing, write `x = t_e/t_crit`. The supplied conformal-time relation gives

`1 = sqrt(x) [1 + sqrt(N(x))]`.

I interpolated `sqrt(N)` and `v` linearly in `log(x)` between adjacent rows of the supplied table and solved this scalar equation by bracketed bisection. Interpolating `v` at the same root gives the values above.

The TOV-side density at the shock is

`rhobar_e = v_e rho(t_e)`.

For fully ionized hydrogen, the electron number density is `n_e = rhobar_e/m_p`, so

`tau_T = sigma_T n_e L_eff`.

Taking `L_eff = rbar_e = 2 c t_e sqrt(N_e)` gives

`tau_T = (sigma_T/m_p) v_e [3/(32 pi G t_e^2)] [2 c t_e sqrt(N_e)]`

`      = [(sigma_T/m_p) v_e 3 c sqrt(N_e)/(16 pi G x)] / t_crit`.

The quantity in square brackets evaluates to `1.473307868145080e17 s`.

## Path-length choice

I chose the shock areal radius, `L_eff = rbar_e`, as the characteristic outward TOV-side column length. This is the only physical length supplied at the crossing. It is also the effective outward column length if the exterior density has the scale-free TOV/isothermal falloff `rhobar(r) = rhobar(rbar_e) (rbar_e/r)^2`, because then

`integral_(rbar_e)^infinity rhobar(r) dr = rhobar(rbar_e) rbar_e`.

That radial falloff was not explicitly supplied, so I record it as an assumption rather than a derived fact. Equivalently, the result can be read as a one-shock-radius local column estimate. If the intended effective path is `f rbar_e`, every reported optical depth and the unity anchor scale linearly by `f`.

## Assumptions

1. The supplied `rho` is a mass density in SI units. This is consistent with the `sigma=1/3` reduction `3/(32 pi G t^2)` and avoids an extra factor of `c^2`.
2. The exterior is pure, fully ionized hydrogen, so there is one free electron per proton and opacity is exactly `sigma_T/m_p`, as directed.
3. The tabulated `v` is applied locally at the shock crossing.
4. The effective TOV-side path is one shock areal radius, as explained above.
5. `sqrt(N)` and `v` are interpolated linearly in `log(t/t_crit)`. The table is dense around the root; no extrapolation is used.
6. Numerical constants are `c = 299792458 m/s`, `G = 6.67430e-11 m^3 kg^-1 s^-2`, `sigma_T = 6.6524587321e-29 m^2`, and `m_p = 1.67262192369e-27 kg`.
7. Scattering is treated as Thomson scattering with no Klein-Nishina, pair-production, composition, ionization-fraction, or relativistic transfer correction.

## Checks

- The supplied table spans `x = 2.7644109132e-11` to `0.999999985`; the root is internal and uniquely bracketed.
- The numerical crossing residual `sqrt(x)[1+sqrt(N)] - 1` is `0.0` at printed precision.
- At the root, `1/sqrt(x) = 3.549947098920840` and `1 + sqrt(N) = 3.549947098920840`, independently reproducing the crossing redshift relation.
- Dimensional check: `(sigma_T/m_p) rho rbar` is dimensionless.
- Scaling check: `rho proportional to t_e^-2` and `rbar proportional to t_e`, while `x`, `v`, and `sqrt(N)` are anchor-independent at fixed `t_obs/t_crit`; therefore `tau_T proportional to t_crit^-1`. The CSV changes by exactly one decade in optical depth for each decade in anchor.
- Limiting anchors: `t_crit -> 0` gives `tau_T -> infinity` (thick), while `t_crit -> infinity` gives `tau_T -> 0` (thin), consistent with the reported side of the unity crossing.

## Reproduction

Run:

`python3 compute_blind_s0.py`

The script uses only the Python standard library and rewrites `s0_optical_depth_vs_tcrit.csv` in this directory.

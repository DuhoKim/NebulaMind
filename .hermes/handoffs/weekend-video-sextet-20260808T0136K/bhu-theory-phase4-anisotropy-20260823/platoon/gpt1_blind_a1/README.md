# GPT1 blind A1: pure-radiation shock matching

This directory is an independent implementation based only on the pinned text
`0210105_clean.txt` named in the brief. I did not search for or inspect another implementation.

## Interpretation and normalization

The pinned paper calls the flat FRW background with constant equation of state exact. For pure
radiation I set `sigma = 1/3`. The source gives the exact background density and scale factor, but
it does **not** print a closed-form shock solution `u(S)`. Its Theorem 1 instead selects a unique
shock branch. I therefore interpret “the sigma=1/3 pure-radiation exact solution” as the exact FRW
background driving the unique shock-matching ODE branch, not as an unprinted analytic formula for
`u`.

The system has an overall time/length scale. I use dimensionless units

- `kappa = 1`,
- the `N=1` horizon event has `t=1`, and
- consequently `r_shock=2` there for radiation.

All densities and pressures are therefore in the corresponding `kappa=1`, `t_horizon=1` units.
A physical rescaling by `t -> L t`, `r -> L r` sends density and pressure to `L^-2` times the
tabulated values.

`r_shock` means the areal/barred shock radius `rbar`, not the comoving FRW coordinate. The file
`tov_side_profile.csv` is the TOV-side state sampled along the shock worldline and indexed by that
TOV areal coordinate.

## Source transcription, with line references

All line numbers below refer to the pinned clean text.

- Lines 95--97 define `N = 2M/rbar` through `A = 1-N < 0`.
- Lines 118--120, equation (4.1):

  `du/dN = -(1+u)/(2(1+3u)N) * [((3u-1)(sigma-u)N + 6u(1+u)) / ((sigma-u)N + (1+u))]`.

- Lines 122--126, equation (4.2):

  `drbar/dN = -rbar / ((1+3u)N)`.

- Lines 128--132, equation (4.3):

  `v = [-sigma(1+u) + (sigma-u)N] / [(1+u) + (sigma-u)N]`.

- Lines 134--138 define `u=pbar/rho`, `v=rhobar/rho`, and `sigma=p/rho`.
- Lines 144--148, equation (4.5), give
  `shock_speed = sqrt(N) (sigma-u)/(1+u)`.
- Lines 154--158 impose `0<pbar<p` and `0<rhobar<rho`.
- Lines 168--180, equations (5.1)--(5.3), give the exact constant-sigma FRW background:
  `rho=4/[3 kappa (1+sigma)^2 t^2]` and
  `R=(t/t0)^[2/(3(1+sigma))]`. Thus at `sigma=1/3`,
  `rho=3/(4 kappa t^2)`, `p=rho/3`, `R proportional to sqrt(t)`, and `H=1/(2t)`.
- Lines 185--191 introduce `S=1/N` and print equation (5.4), the transformed `u` ODE.
- Lines 199--205 give the physical-domain/entropy bound
  `S < [(1-u)/(1+u)] [(sigma-u)/(sigma+u)]`.
- Lines 211--219 (Theorem 1) select the unique branch with `u -> min(1/3,sigma)` as `S->0`
  and `pbar,rhobar -> 0` as `S->1`.
- Lines 245--247 state that for `sigma=1/3` the Big-Bang shock-speed limit is one.
- Lines 259--262 identify `sqrt(N)` as the number of Hubble lengths to the shock. Therefore
  `N=(H rbar)^2`, and for radiation `t = rbar sqrt(S)/2`.

### OCR ambiguity resolutions

1. The plain-text visual rendering of (4.1) on line 118 loses fraction grouping. The same line's
   LaTeX is internally grouped and was transcribed literally above. No alternate grouping was used.
2. In the visual part of line 146 the square-root sign can look like bare `N`; the LaTeX on that
   line explicitly says `sqrt(N)`, which I used.
3. The source never supplies a closed-form `u(S)` for radiation. I did not invent one. The branch
   is selected by Theorem 1's endpoint conditions. Numerically, I start at the regular endpoint
   `S=1, u=0`, integrate backward toward the Big Bang, then emit rows in increasing `t`. This is
   equivalent to selecting the unique entropy branch while avoiding a singular initial point.
4. “TOV-side profile” could mean a full spacetime slice away from the interface. Equations
   (4.1)--(4.3) and the brief's required columns determine only the TOV state **at the shock** as
   the shock moves. I therefore provide that unambiguous profile and do not extrapolate away from
   the interface using equations not requested by the brief.

## Numerical method and step control

The integration variable is `q=log(S)`, which regularizes the ten-decade interval. From (5.4) and
(4.2), the implemented equations are

`du/dq = (1+u)/(2(1+3u)) * [((3u-1)(sigma-u)+6u(1+u)S) / ((sigma-u)+(1+u)S)]`

and

`d log(rbar)/dq = 1/(1+3u)`.

The main integration is SciPy `solve_ivp` with DOP853, `rtol=2e-12`, `atol=2e-14`, and
`max_step=0.10` in `q`. It runs from `q=0` to `log(1e-10)` with initial values `u=0` and
`rbar=2`, then uses dense output on 601 evenly spaced `q` samples. Independent comparison runs use
DOP853 at `rtol=2e-13`, `atol=2e-15` and Radau at `rtol=2e-11`, `atol=2e-13`, with the same
maximum step.

The algebraic constraint is evaluated in the cancellation-resistant form

`v = [-sigma(1+u)S + (sigma-u)] / [(1+u)S + (sigma-u)]`.

Then `rhobar=v*rho` and `pbar=u*rho`.

## Deliverables

- `integrate_radiation_shock.py` — integration, table generation, solver cross-checks, and physical checks.
- `verify_results.py` — independent CSV parsing, algebraic recomputation, and finite-difference ODE checks.
- `shock_results.csv` — required table (`t,r_shock,u,v,N`, TOV density, TOV pressure) plus useful diagnostics.
- `tov_side_profile.csv` — the same TOV-side shock state indexed first by `r_shock`.
- `checks.json` — integration and convergence checks.
- `verification_report.json` — independent table checks.

Reproduce from this directory with:

`python3 integrate_radiation_shock.py && python3 verify_results.py`

## Checks actually run

1. All three integrations completed successfully. Function evaluations: main DOP853 3542,
   tighter DOP853 3662, Radau 6547.
2. Main versus tighter DOP853: maximum absolute `u` difference `4.2813e-14`; maximum absolute
   `r_shock` difference `4.6629e-14`.
3. Main DOP853 versus Radau: maximum absolute `u` difference `1.2334e-12`.
4. Across all non-endpoint samples: `0<u<1/3`, `0<v<1`, `pbar<rhobar`, and the strict bound
   (5.6) all hold.
5. `t` and `r_shock` are strictly increasing; `N` is strictly decreasing.
6. The reconstructed identity `N=(r_shock/(2t))^2` has maximum relative error
   `5.6283e-16`.
7. The near-Big-Bang sample at `S=1e-10` gives shock speed `0.9999600302` and
   `(1/3-u)/sqrt(S)=1.3332667081`, approaching the expected `1` and `4/3` limits.
   Extra no-write probes gave speeds `0.99960219`, `0.99996003`, `0.99999600` at
   `S=1e-8,1e-10,1e-12`, respectively.
8. Independent CSV recomputation found exactly zero displayed-precision error in the constraint
   `v`, `pbar=u*rho`, and `rhobar=v*rho`.
9. A second-order finite-difference check on the 601-row output grid found maximum interior
   residuals `2.1538e-4` for `du/dq` and `2.0780e-4` for `dlog(rbar)/dq`; this is consistent with
   the deliberately coarse output spacing `dq=0.0383764` and is separate from solver tolerances.
10. The output contains 601 finite rows and all required columns. Both Python files passed
    `py_compile`.

At the earliest tabulated point (`S=1e-10`):
`t=2.7644109e-11`, `r_shock=5.5288218e-6`, `u=0.3333200007`,
`v=0.9999866663`, and `N=1e10`. At the normalized horizon endpoint:
`t=1`, `r_shock=2`, `u=v=0`, `N=1`.

## SHA-256 custody

- `integrate_radiation_shock.py`: `4d9cdd4f2fe7a08e4196253df12046961de20e0fedf17b7473c701a0462c3a03`
- `verify_results.py`: `79955644d51eeddd4fd030c4916f3938957468c67d583bf6c7ed97bd15964356`
- `shock_results.csv`: `97df0148814d9736252e351377e33dec7ca379f530b3eb80330afe5e2a484214`
- `tov_side_profile.csv`: `245c8e86a1f075d4f55d37d7ea42e49a2bb0294420dc43a43c185aadde0a21c2`
- `checks.json`: `373d71cbac91ca81ce90f340000630e35c69267d1561cb91ae9c405e05e44d86`
- `verification_report.json`: `996e48586b7496fb59919f80c2965981acd36a6f08e1266058fe28a40af2e903`

HOLD_A6_AND_P1B_SWEEPS_NOT_EXHAUSTIVE_P1B_NOT_REPRODUCIBLE

# Phase 5b re-gate — Cluster A verification and Cluster B adjudication

## Verdict

Cluster A does not pass. The fixes improve the model and correct the withdrawn `tau <= 0.07` claim, but the replacement `tau_max = 0.133` is still not an established upper bound over the authorised ranges. The A6 admissible family is not closed, the numerical scan is coarse rather than exhaustive, the A3/A5 ceiling is not evaluated with the local A6 state, and the delivered P1b artifact still does not run in the lane's current environment. P2b also samples a reduced constant-`tau`/scalar-source transfer rather than the authorised path-dependent transfer integral.

Cluster B is adjudicated explicitly below: B1 goes to the crossing radius; B2 goes against the blind implementation's unpaired propagation factor. Combining those choices would convert Tori's provisional bound to approximately `2.207e-3`–`2.488e-3` in `x_off/r_*(eta_crossing)`, but Cluster A's defects mean that numerical range remains NOT CONFIRMED.

## Cluster A — blocking findings

### A1. The claimed A6 interval is a grid/solver outcome, not an interval derived from the pinned physical bound

Fact: `p1b_range_sweep.py:71-77` tests only 61 values spaced by 0.05 and reports the minimum and maximum values for which `profile()` returns non-`None`. `profile()` returns `None` not only when `w=1` is reached, but also when the solver does not find a horizon before the artificial endpoint `200*rbar_s` (`p1b_range_sweep.py:65-69`). The reported `[-0.75, 0.90]` therefore conflates the physical `0<w<1` condition, horizon existence, a finite integration cutoff, and grid resolution. It is not an independent derivation of a continuous authorised interval.

For every finite radius, the power law `w=w_s(r/r_s)^q` is positive for every real `q`; for negative `q` it decreases outward and can never hit the upper bound `w=1`. Thus `0<w<1` by itself cannot produce the stated lower endpoint `q=-0.75`. A separate existence/regularity restriction would have to be derived and authorised.

### A2. The one-parameter power law does not exhaust junction-consistent A6 closures

The junction fixes only `w(r_s)=u/v`. Infinitely many positive profiles satisfy that value while remaining below one—for example broken powers, profiles with a local shoulder, or smooth functions `w=w_s exp[f(ln(r/r_s))]` with `f(0)=0`. Neither the frozen brief nor Addendum A authorises the power-law family as exhaustive. No comparison theorem is supplied showing that this family maximises the optical-depth functional. Therefore a maximum inside this family cannot be promoted to an upper bound over A6.

### A3. Even within the chosen power-law family, `tau_max=0.133` comes from 13 samples, not an exhaustive maximisation

Fact: after estimating the endpoints, the script evaluates only `np.linspace(q_lo,q_hi,13)` (`p1b_range_sweep.py:114-125`). The reported maximiser `q=-0.475` is exactly one of those coarse grid points. There is no optimizer, interval enclosure, derivative/sign argument, adaptive refinement, or discretisation-error bound. The check named “genuine upper bound” asserts only `best > 0`; it does not test upper-boundedness or exhaustiveness (`p1b_range_sweep.py:124-125`).

The radial optical-depth integral itself is evaluated on a fixed 20,000-point grid with no convergence check (`p1b_range_sweep.py:99-105`). This can provide an estimate, not a certified ceiling.

### A4. The A3/A5 pair ceiling is frozen to the shock value of `w` rather than carried through the A6 profile

Fact: `n_e_ceiling()` sets the ideal-gas temperature to `kT_gas = w_s * 0.6 m_p c^2` at every integration point (`p1b_range_sweep.py:79-93`). But the closure under test is `w(r)=w_s(r/r_s)^q`. Under the stated ideal-gas subcase the local temperature depends on local `w`, so the pair energy-budget ceiling also changes along the path. The sweep therefore does not jointly carry A5 and A6. The shock calculation `ceiling/cold=2.262` is correctly reproduced for the shock, but it does not establish the maximum column through the bulk.

There is also a semantic gap between the authorised A3 endpoint “full LTE pairs at Tbar” and the implemented generic energy-budget ceiling `rho c^2/(3kT)`: the script does not calculate an LTE pair abundance or prove that this ceiling is attainable. It may be a conservative envelope, but that must be labelled and propagated as an envelope rather than reported as an exhaustive A3 sweep.

### A5. Objection 4 is not fixed: versions are emitted, not pinned, and P1b does not execute in the current lane environment

Re-execution from the verdict directory with `python3 p1b_range_sweep.py` printed Python 3.9.6, NumPy 1.26.4, SciPy 1.13.1, then exited 1 at `np.trapezoid` because NumPy 1.26.4 has no such attribute. `python3.11` exists, but has no NumPy installed. The lane contains no requirements/lock file. Printing the versions from a prior runtime is provenance, not dependency pinning or a reproducible environment.

This also means the receipt's “6/6 checks” and `tau=0.133` cannot be reproduced from the delivered artifact in the current lane. Before the crash, a runtime warning also reported an invalid fractional power in the radiation-temperature calculation, showing that unphysical/negative-density solver samples are not rejected fail-closed.

### A6. P2b still does not carry the full authorised transfer

The script re-executes successfully and reproduces its 3x3 table and four checks. That is a failed attack on the arithmetic: the stated numbers are correct for the implemented reduced model.

However, the brief requires the path transfer integral. `p2b_transfer_sweep.py` instead uses a single direction-independent total `tau` and a local scalar source ratio at the crossing (`p2b_transfer_sweep.py:42-49`). For an off-centre observer, the crossing epoch, density/temperature profile, and optical-depth path vary with direction. The derivative of `tau(mu,x)` and the distributed source term can themselves contribute to or dilute the dipole. Sampling only `tau in {0,tau_max/2,tau_max}` and `s_frac in {0,1/2,1}` is not an exhaustive sweep absent a monotonicity proof, and it does not implement Thomson angular redistribution.

Therefore the successful 3x3 run establishes a sensitivity table, not the full A4/A5 transfer bound required by the frozen brief.

## Cluster B — explicit adjudication

### B1 — use `r_*(eta_crossing)`, with a reporting caveat

The observation constrains the physical comoving displacement `x_off`; a denominator is a reporting convention, not part of the measured dipole. If the result is reported as a fraction of the boundary that generated the observed sky, the correct denominator is the centred past-light-cone crossing radius `r_*(eta_crossing)=1.4366113`. The present-epoch shock radius `r_*(eta_obs)=2.000` describes a simultaneous “now” surface outside our past light cone and is not the radius of the observed boundary.

Thus gpt1's denominator is the physically appropriate observational normaliser. Tori's denominator is not algebraically illegal, but it must be labelled `x_off/r_*(eta_obs)` and cannot be compared numerically to a crossing-normalised bound without conversion.

Independent conversion gives

`r_*(eta_obs)/r_*(eta_crossing) = 2/1.4366113145 = 1.392165006`.

### B2 — the standalone `eta_c/eta_obs` in the blind implementation is a double-count for a comoving radiation bath

The propagated observed temperature is

`T_obs(mu) = [a(eta_c)/a(eta_obs)] * D(mu) * T_inc(eta_c)`.

For a comoving radiation bath, `T_inc(eta_c) = T_obs,0 * a(eta_obs)/a(eta_c)`. The scale-factor factors cancel ray by ray even when `eta_c` varies with direction, leaving the frame/geometry factor `D(mu)`. A local source expressed as a ratio to the same crossing-epoch bath receives the same propagation cancellation.

The blind code includes `eta_c/eta_obs` in `raw_transfer()` (`compute_blind_p2b.py:41-54`) but supplies no compensating `T_inc proportional to eta_obs/eta_c`. Its direction-dependent propagation term therefore creates an artificial contribution to the dipole. Calling that term “radiation-era propagation” is incomplete: propagation and source cooling must be handled as a pair.

On the stated conventions, Tori's omission is the correct reduced representation of the already-cancelled thermal evolution. If the modeled incident field were instead a fixed-temperature flash or a non-comoving source, neither implementation could be accepted without specifying that source history; that is not the bath assumed here.

### Consequence for the bound

Apply B1's crossing denominator to Tori's B2-correct provisional range:

- `1.5850e-3 * 1.392165006 = 2.2066e-3`;
- `1.7869e-3 * 1.392165006 = 2.4877e-3`.

So the adjudicated convention would give approximately

`|x_off|/r_*(eta_crossing) < 2.207e-3 to 2.488e-3`

(one part in about 453 to 402), not either previously quoted range. This is a convention-and-propagation correction only. Because Cluster A does not establish the full transfer functional or optical-depth ceiling, this converted numerical bound remains NOT CONFIRMED and must not be described as blind-doubled.

## Failed attacks / positive evidence

- `p2b_transfer_sweep.py` runs successfully in the current environment and reproduces the receipt's 3x3 values and 4/4 checks.
- The shock pair-to-cold ceiling ratio `2.262` is reproduced before P1b reaches its runtime failure.
- The source brightness ceiling `T_source/T_FRW <= v^(1/4)` follows from `aT^4 <= rhobar c^2`; the ideal-gas kinetic temperature cannot by itself raise that radiative ceiling.
- Monopole-normalising before comparing the dipole is correct; a direction-independent common transfer is not an observable dipole.

## Required closure

1. Define and authorise an A6 function class or prove a comparison bound over a physically stated class; derive its admissible domain independently of an arbitrary integration cutoff.
2. Jointly evaluate local A5 temperature/pair content with the A6 profile, with fail-closed physical-state checks and a clear distinction between LTE abundance and a conservative energy envelope.
3. Replace coarse sampling with bounded optimisation plus q/radial convergence evidence.
4. Deliver a real reproducible environment (lock/requirements plus an executable interpreter) and rerun P1b cleanly.
5. Carry direction-dependent optical depth and the distributed A4/A5 source through the off-centre transfer, then blind-double that corrected functional using the B1/B2 adjudication above.

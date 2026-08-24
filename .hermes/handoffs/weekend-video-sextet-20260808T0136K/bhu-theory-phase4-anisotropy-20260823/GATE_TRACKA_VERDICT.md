HOLD_TRACK_A_UNCALIBRATED_OBSERVABLES_AND_OVERCLAIMS

# Gate Track A verdict

The A1 shock trajectory and A2 boundary-crossing geometry survive adversarial re-derivation in the strict k=0, sigma=1/3 branch. Track A nevertheless does not yet establish the observable, calibrated exclusion surface claimed in `TRACK_A_VERDICT.md`.

## Blocking objections

### 1. The claimed calibrated CMB exclusion surface is only a geometric crossing surface

`TRACK_A_VERDICT.md:9-18` calls the discriminant calibrated, asserts `consistency iff x_off < x_max(t_obs)`, and calls P3 a concrete observable morphology. The receipts do not establish those statements.

- `A3_RECEIPT.md:29-43` and `A4_RECEIPT.md:20-26` turn intersection of the last-scattering sphere with the shock into observational exclusion.
- But `A3_RECEIPT.md:58-59` and `A4_RECEIPT.md:48-51` explicitly concede that the TOV-side optics are unmodeled. Therefore a cap is a set of directions whose rays cross the boundary, not a calculated CMB temperature/polarization signal. No transfer function, amplitude, frequency dependence, polarization, or angular power spectrum is derived.
- Calling a non-disruptive TOV-side result a "conspiracy" does not prove it impossible. Thus `x_off < x_max` is sufficient for direct CMB rays to remain in the exact-FRW region; it is not proved necessary for observational consistency. The `iff` and "calibrated exclusion surface" language must be removed unless the beyond-shock optics and observable transfer are computed or bounded.
- `a4_prediction_functions.py:50-60` computes sphere-intersection geometry. Its `ell ~ pi/theta` estimate (`a4_prediction_functions.py:104-109`) is only an angular-scale heuristic, not a predicted multipole spectrum. `TRACK_A_VERDICT.md:17-19` overstates it as the model's only near-threshold observable signature.

### 2. "Strictly unobservable" is false as written and is not established by opacity

`TRACK_A_VERDICT.md:13-16` and `A4_RECEIPT.md:20-26` say that below the P2 surface the boundary is "STRICTLY UNOBSERVABLE" because crossings above z_ls are hidden by opacity.

- Recombination opacity is a photon-channel argument, not a theorem about all messengers. The lane does not analyze neutrinos or gravitational waves, so it cannot conclude that a boundary crossing at z > z_ls is strictly unobservable in general.
- Even for the CMB, the scripts replace radiative transfer with a sharp surface at exactly `ZLS=1100` (`a3_observables.py:62-80`; `a4_prediction_functions.py:38,50-64`). They contain no visibility function or finite-width recombination calculation. The resulting surface may be a useful geometric approximation, but it cannot support the word "strictly" or an exact dichotomy.
- Failed attack recorded: for a direct photon whose entire geodesic remains inside the matched region, the background metric is exact FRW, so there is no boundary ISW/lensing term along that path at the level modeled here. The moving shock and junction conditions do not by themselves spoil A0. This does not rescue the blanket all-channel or exact-opacity claim.

Required amendment: restrict the statement to direct post-recombination photons whose complete path remains in the exact-FRW region, and label the z_ls surface an approximate photon-screen criterion unless realistic radiative transfer is added.

### 3. The expansion-anisotropy limb is null only for wholly interior signals, not identically null for the observable named in the brief

`TRACK_A_VERDICT.md:9-12` says expansion-rate anisotropy is identically null. A0 supports that only for comoving sources whose complete light paths remain inside exact FRW (`A2_RECEIPT.md:6-15`; `A3_RECEIPT.md:11-19`).

`TRACK_A_SETUP.md:52-54` explicitly defined the expansion observable to include sources "whose light samples regions gravitationally influenced by the shock/TOV side." Those rays are precisely where the optics are unmodeled. The correct Track A result is therefore:

- exact null for wholly interior FRW propagation; and
- not calibrated for boundary-crossing/boundary-affected expansion probes.

The receipt does not justify closing the full H0-anisotropy limb as `NOT-A-DISCRIMINANT`.

### 4. Post-horizon/post-exit observers are outside the computed domain

The source says the shock reaches N=1 at the White Hole horizon and then continues outward (`0210105_clean.txt:313-315`). The numerical orbit is integrated only over 0 < S <= 1, equivalently N >= 1 (`a1_shock_trajectory.py:41-53`), and its time map is anchored at N=1 (`a1_shock_trajectory.py:79-90`). A2-A4 inherit that orbit.

No receipt derives the shock trajectory or optics for an observer epoch after the N=1 horizon event. Therefore `TRACK_A_VERDICT.md:1,9-27` cannot call the strict interior track complete without an explicit validity restriction to the pre-horizon branch, or an extension through the post-horizon/OS regime. This is also where the source says the shock continues along a Schwarzschild geodesic, so it is not a removable edge case.

## Non-blocking but required corrections

1. The A1 anchor-label correction was not propagated into the final artifact. `a1_shock_trajectory.py:79` still says time is in units of `t0`, and `a1_shock_trajectory.py:101-102` / `a1_results.csv:1` label the column `t_over_t0`; the corrected unit is `t/t_crit` per `A1_RECEIPT.md:47-54`.
2. `TRACK_A_VERDICT.md:3-5` says all receipts and pins are in-lane, but `A1_CROSSCHECK.md:36` records the pre-addendum A1 receipt prefix `98c99f37...`; the current amended `A1_RECEIPT.md` hashes to `7c4e96837fa255bb0bc415d7b49d5385a5bc630e4eb18688a839dd38fd448109`. The custody claim must be refreshed after final edits.
3. `A4_RECEIPT.md:22` quotes the early sample `t=0.14 -> x_max/r_*=0.20`, but `a4_regime_map.csv` does not tabulate t=0.14 and `a4_prediction_functions.py:82-85` starts the written map near 0.98 t_vis. The formula/check does reproduce approximately 0.20 at half t_vis, but the receipt should cite that check rather than imply it is in the delivered map. Also, 20% is one sample, not a generic summary of all earlier observers.

## Analytic and transcription attacks that failed

The four mandatory analytic claims are correct within their stated radiation-branch domain:

1. Center crossing: `eta_o - eta_e = eta_e sqrt(N_e)` and `1+z = eta_o/eta_e` give `z_c(center)=sqrt(N_e)` (`a3_observables.py:4-8`).
2. Nearest-direction geometry: `x + eta_o - eta_e = eta_e sqrt(N_e)` gives `x_max = eta_o[(1+sqrt(N_e))/(1+z)-1]`, with `eta_e=eta_o/(1+z)` (`a3_observables.py:7-8,77-80`).
3. Expanding source Eq. (5.4) about S=0 with `u=1/3-a sqrt(S)+...` gives `a^2=16/9`; the physical branch is `a=4/3`. This is a leading asymptotic, not an exact equality (`A1_RECEIPT.md:9-13`; `a1_shock_trajectory.py:16-17`).
4. With `q=sqrt(N)=H rbar=rbar/(2t)` and source Eq. (4.5), `d rbar/dt=q+s`; differentiating `rbar=2tq` gives `dq/dt=(s-q)/(2t)` and hence `d ln t/dq=2/(s-q)` (`a1_shock_trajectory.py:19-21,79-90`).

The pinned source hash is `82fd83229be202847a4e0d5d37953f4aa41b06931fdf8eba151771fb45118242`. Against its displayed LaTeX at `0210105_clean.txt:118-130,144-148,185-205`, the implementations of Eqs. (4.1)-(4.5), (5.4), and (5.6) have no dropped factor or sign error. The OCR-readable prose layer is visually ambiguous in places, but the LaTeX transcription used by the scripts is correct.

## Gate condition to clear HOLD

Amend `TRACK_A_VERDICT.md` and receipts so that they claim only: a verified sigma=1/3 pre-horizon shock trajectory; exact-FRW null results for wholly interior propagation; and calibrated geometric crossing/cap functions. Either compute/bound the TOV-side and recombination transfer needed for an observable exclusion, or classify the CMB/H0 consequences as not calibrated. Scope "unobservable" to the photon criterion actually modeled, state the post-horizon domain gap, and refresh labels and pins.

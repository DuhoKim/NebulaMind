# PREREGISTRATION — z>7 Mass–Metallicity Relation systematics gate

**Run:** overnight-z7-mzr-20260720 (Trikitear) · **Author:** Goru (skeptic/gate) · Phase 1
**Purpose:** This is the anti-circularity contract. It enumerates every way a claimed
"z>7 MZR offset" could be an **artifact rather than physics**, and fixes a concrete pass/fail
test for each *before any number exists*. Tests are declared here so they cannot be reverse-fit
to a desired result. If any pass-test fails, the honest-labeling rule at the bottom governs.

**Claim under test:** at fixed stellar mass, z>7 galaxies show a gas-phase O/H **offset below**
the local (SDSS anchor) MZR that is *physical evolution*, and this offset is (or is not)
reproduced by IllustrisTNG on the same abundance scale.

**Null / artifact hypothesis (must be excluded):** the apparent offset is fully explained by
(a) the SDSS-Tremonti vs JWST strong-line calibration scale difference (~0.2–0.24 dex),
(b) comparing low-mass z>7 galaxies to more massive local galaxies (mass mismatch),
(c) selection, aperture, extrapolation, N/O, or small-N effects — individually or in sum.

---

## Pre-declared decision thresholds (locked before analysis)
- **Calibration systematic budget:** sigma_cal = 0.24 dex (SDSS-Tremonti high vs Te/PP04-O3N2,
  per metallicity-scale memo). After reconciliation to a matched scale, residual scale
  uncertainty assumed sigma_cal,resid = 0.10 dex unless the data justify smaller.
- **Detection bar:** a physical offset must satisfy |Delta log(O/H)| - sigma_cal,resid > 0 AND
  the bootstrap 95% CI on the mass-matched offset must exclude 0.
- **Mass overlap requirement:** offset evaluated only within the stellar-mass interval where SDSS
  and JWST samples overlap; the overlap interval [logM_lo, logM_hi] and N in each survey are
  reported. No extrapolation of the SDSS MZR beyond its fitted mass range is permitted as evidence.
- Every reported offset carries its abundance-scale label (e.g. "PP04-O3N2", "Te-direct").
  Cross-scale subtraction without an explicit conversion term is forbidden.

---

## 1. Calibration scale (SDSS-Tremonti vs JWST strong-line)
- **Failure mode:** SDSS oh_p50 (Tremonti/CL01 Bayesian) sits ~0.24 dex above Te-direct/PP04-O3N2.
  JWST high-z O/H are typically Te-direct or O3-strong-line. Subtracting the two raw yields a
  ~0.24 dex "offset" that is 100% calibration, 0% physics.
- **Test:** put SDSS and JWST on ONE scale before differencing — reconcile via galSpecLine O3N2
  (or convert SDSS to PP04-O3N2/Te). Recompute the offset on the matched scale.
- **Pass:** matched-scale |offset| - sigma_cal,resid > 0. **Fail:** offset <= sigma_cal,resid,
  i.e. it vanishes or shrinks into the residual calibration band on reconciliation.
- **Decision:** pass -> candidate physical. Fail -> "consistent within calibration scale"
  (and per the brief, *that vanishing is itself the honest result*).

## 2. Mass mismatch (low-mass z>7 vs massive local)
- **Failure mode:** z>7 galaxies are low-mass (logM* ~ 7.5–9.5); the local anchor is dominated by
  more massive galaxies. Since the MZR rises with mass, comparing a low-mass high-z sample to the
  local mean fakes a downward offset that is pure mass, not redshift.
- **Test:** compare at **fixed stellar mass**. Evaluate the offset only inside the SDSS/JWST mass
  overlap; state [logM_lo, logM_hi] and N per survey. Report the offset as a function of mass, not
  a single number, so a mass-dependent artifact is visible.
- **Pass:** offset persists within the overlap interval with a stated, non-empty mass range.
  **Fail:** offset exists only outside the overlap (i.e. relies on extrapolating one relation).
- **Decision:** pass -> mass-controlled. Fail -> "mass mismatch; no matched-mass comparison possible".

## 3. Strong-line extrapolation (z~0 calibrations applied at z>7)
- **Failure mode:** strong-line O/H calibrations are anchored at z~0 where ionization parameter,
  hardness, and N/O differ from z>7. Applying them unchanged at high-z introduces an unknown,
  possibly mass/redshift-dependent bias.
- **Test:** use a calibration validated (or at least tested) at high-z where available; otherwise
  **bracket** the result with two independent diagnostics (e.g. Te-direct vs O3-strong-line) and
  report the spread as a systematic band.
- **Pass:** the offset survives (same sign, CI excludes 0) under BOTH bracketing calibrations.
  **Fail:** sign or significance flips between diagnostics.
- **Decision:** pass -> robust to calibration choice. Fail -> "calibration-dependent; not robust".

## 4. Selection / luminosity bias
- **Failure mode:** JWST z>7 samples are UV-continuum or emission-line (e.g. [OIII]/Ha) selected.
  Emission-line selection favors high-EW, low-metallicity, bursty systems; UV selection favors
  bright objects. Either can bias the sample O/H away from the mass-averaged population, mimicking
  or inflating an offset.
- **Test:** state the exact selection function of the JWST sample and its **expected direction** on
  O/H. Emission-line/metal-poor-leaning selection biases O/H **downward** -> would *inflate* a
  low-metallicity offset; note this explicitly so the offset is read as an upper bound on evolution.
- **Pass:** selection stated AND its direction cannot by itself account for the measured offset
  (offset larger than plausible selection bias, or bias direction opposes the claim).
- **Fail:** selection direction is same-sign and comparable in magnitude to the offset.
- **Decision:** pass -> selection-aware detection. Fail -> "consistent with selection bias".

## 5. Small-N
- **Failure mode:** z>7 spectroscopic-metallicity samples are tiny (often N ~ few to few-tens);
  a couple of metal-poor outliers can drive the whole "offset".
- **Test:** **bootstrap** the mass-matched offset (resample galaxies with replacement, >=10^4 draws);
  report N per survey and the 95% CI. Report the offset with and without the most extreme point
  (leave-one-out sensitivity).
- **Pass:** bootstrap 95% CI excludes 0 AND result is not driven by a single object (leave-one-out
  keeps CI excluding 0). **Fail:** CI includes 0, or one object flips significance.
- **Decision:** pass -> statistically resolved. Fail -> "small-N; not statistically resolved".

## 6. Aperture (global vs central O/H)
- **Failure mode:** SDSS 3-arcsec fibre samples the **central**, higher-metallicity region of local
  galaxies (radial gradients -> fibre O/H biased high); JWST high-z O/H is spatially **integrated /
  global**. Central-vs-global mismatch biases the local anchor upward, *inflating* the z>7 deficit.
- **Test:** note the direction (fibre-central biases SDSS high -> inflates offset). Where possible
  apply an aperture/gradient correction to SDSS or use a global-metallicity local anchor; otherwise
  flag the offset as an **upper bound** on the account of aperture.
- **Pass:** aperture direction documented AND corrected-or-bounded so it does not solely produce the
  offset. **Fail:** offset is within the plausible aperture correction and uncorrected.
- **Decision:** pass -> aperture-aware. Fail -> "consistent with aperture (central-vs-global)".

## 7. N/O enhancement at high-z
- **Failure mode:** some z>7 galaxies show elevated N/O (e.g. GN-z11-like); N-based strong-line
  diagnostics (N2, O3N2) then return biased O/H, corrupting any N-dependent calibration.
- **Test:** **prefer O-based diagnostics** (Te-direct, R23/O3-based) for high-z O/H; if an N-based
  diagnostic is used, cross-check against an O-based one and discard where they diverge beyond the
  quoted systematic. Flag any object with independent evidence of high N/O.
- **Pass:** primary O/H is O-based, or O-based and N-based agree within systematics.
  **Fail:** result depends on an N-based diagnostic in a plausibly N-enhanced regime.
- **Decision:** pass -> abundance-diagnostic clean. Fail -> "possible N/O contamination".

---

## Cross-cutting: TNG comparison (non-circularity)
IllustrisTNG O/H must be placed on the **same matched observational scale** (or the observations
converted to the simulation's intrinsic O/H with a stated, single conversion) before any
sim-vs-obs offset is claimed. Comparing raw TNG intrinsic O/H to strong-line observed O/H repeats
the calibration artifact of #1 at the model level and is forbidden.

---

## HONEST-LABELING RULE (governs the paper's top-line claim)
A "validated detection of z>7 MZR evolution" may be claimed **only if ALL pass-tests above are
satisfied**: the offset exceeds the residual calibration uncertainty on a matched scale (1),
is measured at fixed stellar mass within a stated overlap (2), survives two bracketing
calibrations (3), is not accounted for by the stated selection direction (4), has a bootstrap
95% CI excluding 0 that is not single-object-driven (5), is aperture-aware (6), and rests on
O-based diagnostics (7).

**If ANY single pass-test fails, the result is DESCRIPTIVE, not a detection.** It must be reported
as "consistent within calibration / selection / aperture systematics" — naming the specific failed
test(s) — and MUST NOT be presented, in title, abstract, or verdict memo, as a validated detection
of chemical evolution. Per the run brief, if the offset vanishes on the matched scale, *that null
IS the honest result* and is reported as such.

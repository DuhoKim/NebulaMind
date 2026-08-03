# P2 RESULTS — z>7 mass–metallicity offset (matched-scale, mass-controlled)

**Run:** overnight-z7-mzr-20260720 (Trikitear) · **Phase 2 (Tori)** · 2026-07-20T01:40:23+0900 KST
**Status:** DESCRIPTIVE (automated; not human-cleared) — real data only, no fabrication.

## Data — VizieR pull SUCCEEDED (closes the P1 gap)
- Pulled **Nakajima+23** (VizieR `J/ApJS/269/33`, tabled1) via TAPVizieR ADQL: **N=182** total, **34 at z>7**, **26 z>7 with both M\* and 12+log(O/H)**, **16 in the mass-overlap window [8.0,9.5]** (3 mass-upper-limits excluded).
- **Curti+24** (`J/A+A/684/A75`) is **NOT deposited in VizieR TAP** -> used only as its published relation fit for context, not per-object.
- Per-object table written: `z7_metallicity.csv` (z>7) and `z4_metallicity_superset.csv` (z>4, N=142).
- Diagnostics: 6 direct-Te, 10 R23, 10 R3 among z>7 — **100%% O-based** (relevant to Test 7).

## Calibration reconciliation (make-or-break)
- Applied the **exact Kewley & Ellison 2008 metallicity-dependent cubic** T04->PP04-O3N2: `12+log(O/H)_PP04O3N2 = 230.782 - 75.79752 x + 8.526986 x^2 - 0.3162894 x^3` (x=T04, valid 8.05-9.2, rms 0.046), replacing the P1 bulk -0.24 dex.
- The conversion is strongly metallicity-dependent: shift is ~0.0 dex at logM 8.0 but ~-0.24 dex at logM 9.5 — i.e. the bulk -0.24 OVER-corrects at the low masses where z>7 galaxies live.
- **The offset does NOT vanish on the matched scale.** Naive (unmatched T04) offset = 0.56 dex; matched PP04-O3N2 offset = 0.45 dex. Calibration explains ~0.12 dex; ~0.45 dex remains.

## Headline number
- **Matched-scale mass-controlled Delta = 0.45 dex** (SDSS PP04-O3N2 minus z>7, at fixed mass in [8.0,9.5]).
- **Bootstrap 95% CI = [0.28, 0.62]** (2x10^4 resamples, galaxies + measurement noise) — **excludes zero**.
- Te-direct subset only (calibration-free): Delta = 0.33 dex, CI [0.07, 0.54].
- Leave-one-out [0.43, 0.48]; excluding the most-extreme object still gives CI [0.372, 0.586].
- TNG z=6 (intrinsic scale, trend only) predicts ~0.13 dex deficit — far smaller than observed; sims under-predict the early deficit (caveat: z=6, different scale).

## 7-test pre-registered scorecard
| Test | Result | Number |
|---|---|---|
| calibration | **PASS** | matched |Delta|=0.449 dex; |Delta|-sigma_resid(0.10)=0.349>0; survives even full 0.24 budget (0.21>0) |
| mass mismatch | **PASS** | fixed-mass Delta across logM 8.0-9.5: {'8.0': 0.545, '8.5': 0.396, '9.0': 0.439, '9.5': 0.427} |
| strongline bracketing | **PASS** | Te-direct N=4 Delta=0.332 CI=[0.075,0.535]; strong-line N=12 Delta=0.488 CI=[0.351,0.615] |
| selection | **FAIL (does not cleanly pass)** | offset=0.45 dex (Te-only 0.33); plausible EM-line/UV selection bias ~0.1-0.2 dex, SAME sign |
| smallN | **PASS** | N=16 Delta=0.449 bootstrap95CI=[0.328,0.560] LOO=[0.428,0.481]; excl most-extreme still CI=[0.372, 0.586] |
| aperture | **PASS** | SDSS 3-arcsec fibre central-bias direction documented; bounded <~0.05 dex at logM 8-9.5 |
| NO enhancement | **PASS** | 100%% O-based diagnostics (direct-Te 6/16 + R23/R3 10/12 O-based); zero N-based |

**Result: 6/7 PASS.** The failing test is **#4 selection**: JWST z>7 emission-line/UV selection biases O/H downward in the *same direction* as the offset and cannot be bounded from data on disk.

## Honest verdict
DESCRIPTIVE (suggestive but data-limited): a robust, mass-controlled, calibration-reconciled z>7 gas-phase O/H deficit of 0.45 dex (Te-only subset 0.33 dex) below the local MZR, with bootstrap 95% CI [0.28,0.62] excluding zero and surviving 6 of 7 pre-registered systematics tests. It is NOT a validated detection of z>7 MZR evolution because Test 4 (selection) does not cleanly pass: JWST emission-line/UV selection biases O/H downward in the SAME sense as the offset and cannot be bounded from data on disk, so the measured deficit is a STRONG UPPER BOUND on chemical evolution, not a clean measurement. Further limits: single-survey (Nakajima+23 only; Curti+24 not in VizieR TAP), N=16 in overlap, and no z>7 simulation on disk (TNG stops at z=6).

## Files
- `z7_metallicity.csv`, `z4_metallicity_superset.csv` — per-object pulls (real, VizieR).
- `results.json` — offset, CI, per-bin N, per-test PASS/FAIL, verdict.
- `fig_z7mzr.png` — matched SDSS relation + z>7 points/fit + Curti+24 + TNG z=6 trend + systematic band.
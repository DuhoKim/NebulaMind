# SELECTION_AUDIT — independent Δ_sel estimate for the z>7 MZR (Test 4)

**Author:** Goru (skeptic) · **Run:** overnight-z7-mzr-20260720 P6 · **Written:** 2026-07-20 08:48 KST
**Purpose:** Independent, first-principles + literature estimate of the JWST emission-line/auroral
**selection bias** Δ_sel on recovered z>7 12+log(O/H) at fixed M*, to cross-check Tori's Monte-Carlo
forward model rather than trust a single method. This is the decisive input to pre-registered **Test 4**,
which previously FAILED because Δ_sel was declared *unbounded*.

Grounding: Nakajima+2023 (`_nakajima_tabled1_raw.csv`, ADS 2023ApJS..269...33N) per-object sample;
DR packet `area1_mass_metallicity_DR_PACKET.md`. No fabrication; assumptions flagged.

---

## 1. Direction & mechanism (sign is DOWN; which subset is worse)

Two selection channels, both biasing recovered O/H **downward** at fixed M* — same sign as the claimed offset:

- **Strong-line subset (12/16 of overlap sample):** objects enter only above an emission-line
  flux/EW threshold. High EW(Hβ) ⇔ high sSFR / bursty. Via the local FMR (negative ∂O/H/∂SFR at
  fixed mass; MZR-E03, Curti+2020, Mannucci+2010), the high-sSFR tail is metal-poor at fixed mass →
  **downward** bias. Compounded (not caused) by strong-line-calibration downward bias when z=0
  calibrations are applied at z>7 (Hirschmann+2023, up to ~1 dex in extremis; MZR-D03).
- **Direct-Te subset (4/16):** auroral [OIII]4363 is detectable only at high electron temperature,
  i.e. **low O/H** at fixed mass. This is a temperature-Malmquist truncation → the Te subset is,
  in principle, biased **most** metal-poor.

**Empirical twist (adversarial, and important):** in THIS sample the Te subset does NOT sit lowest.
At fixed mass the Te-direct subset is the *least* offset. So the auroral bias is theoretically
"worst" but here sub-dominant; the strong-line channel (selection + calibration) dominates the
observed spread. See §3.

---

## 2. Magnitude bracket

### (a) Is the pulled sample extreme? — YES, strongly.
Detected z>7 overlap sample (N=16): median **EW(Hβ) = 124 Å** (mean 127; full z>7 census median 139 Å),
vs ~10–40 Å for normal star-forming galaxies. Median **log sSFR = −7.50** (sSFR ≈ 31 Gyr⁻¹). These are
extreme emission-line galaxies (EELGs) — precisely the high-EW/bursty/metal-poor tail that
emission-line selection preferentially admits. The sample is *not* a mass-matched draw of the z>7
population; it is its upper-EW envelope.

### (b) First-principles FMR estimate of Δ_sel (strong-line):
  Δ_sel ≈ (sSFR excess of detected vs mass-matched z>7 population) × (FMR slope ∂O/H/∂log sSFR |_M).
  - sSFR excess: detected median sSFR ≈ 31 Gyr⁻¹; a plausible mass-matched z~7 main-sequence
    sSFR ≈ 8–16 Gyr⁻¹ ⇒ excess **0.3–0.7 dex** [ASSUMPTION — z>7 MS sSFR not on disk; flagged].
  - FMR slope at low mass: **0.15–0.30 dex per dex** (local Te-FMR, Curti+2020 / Mannucci+2010 low-mass branch).
  ⇒ **Δ_sel(strong-line) ≈ 0.05–0.21 dex, central ≈ 0.10–0.15 dex** (0.5 dex × 0.22 = 0.11).

### (c) Literature anchor:
  - Kewley & Ellison (2008): calibration-family offsets up to ~0.7 dex (MZR-N02) — sets the *scale* budget, not selection.
  - Hirschmann+2023 (MZR-D03): z=0 strong-line calibrations applied at high-z can bias O/H down up to ~1 dex —
    this is a *calibration* confound entangled with selection for the strong-line subset.
  - Nakajima+2023 / MZR-E06,-U01: z>6 slope, zero-point, scatter are explicitly "selection- and
    calibration-sensitive"; auroral detections are a small, non-representative subset.
  No paper in the packet gives a single clean Δ_sel number for z>7, so the bracket is derived, not cited.

### (d) Δ_sel(Te-direct):
  Auroral temperature-floor + residual EW selection. Theoretically ≥ strong-line, but **empirically not
  displaced below strong-line here** (§3) ⇒ bracket **0.05–0.15 dex, central ≈ 0.10 dex**, with low confidence (N=4).

### ⇒ INDEPENDENT Δ_sel BRACKET
| subset | Δ_sel bracket (dex) | central |
|---|---|---|
| strong-line | 0.05 – 0.20 | 0.10–0.15 |
| direct-Te | 0.05 – 0.15 | 0.10 |
| **combined (sample-weighted)** | **0.05 – 0.20** | **0.10–0.15** |

---

## 3. Empirical checks within the pulled sample (concrete numbers)

Offset Δ_i ≡ SDSS_PP04(M_i) − O/H_i on the matched scale; residual = O/H − (z7 internal MZR fit).

- **Fixed-mass Te-vs-strong-line gap (the direct selection+calibration signal):** in the common mass
  window [8.13, 8.77], Te-direct mean Δ = **0.317** dex, strong-line mean Δ = **0.504** dex →
  **strong-line sits 0.19 dex MORE metal-poor at fixed mass** (residual form: +0.17 dex Te-vs-SL gap).
  This ~0.17–0.19 dex is a *direct measured* upper bound on the combined strong-line
  selection+calibration bias — and it means the calibration-free Te anchor (0.33 dex) is the
  conservative offset; the extra 0.16 dex in the full-sample 0.45 is strong-line-driven, not clearly physical.
- **Δ vs EW(Hβ): r = +0.09; Δ vs log sSFR: r = +0.00** — NO within-sample gradient. This is the
  signature of *truncation* selection: every detected galaxy is already above the EW threshold, so
  the bias lives in the cut, not in a visible internal trend. A flat internal correlation does NOT
  mean "no selection bias"; it is exactly how threshold bias hides. (Hence Δ_sel must be estimated
  by forward-modelling the truncation — Tori's job — not read off the detected sample.)
- **Δ vs O/H: r = −0.96** — the offset is carried by the lowest-O/H objects (partly mechanical since
  Δ contains −O/H, but consistent with a metal-poor-tail-selected sample).
- **Δ vs logM_err: r = +0.11 (slope +0.21); Δ vs z: r = −0.12** — weak; no strong mass-error or
  redshift-dependent artifact.

---

## 4. Crisp Test-4 pass/fail criterion

Selection-corrected offset arithmetic (obs matched = 0.449; Te-only = 0.332; σ_cal,resid = 0.10;
Te-only bootstrap CI lower edge = 0.075):

| Δ_sel | corrected all | (corr_all − σ) | corrected Te-only | % of 0.45 | (Te CI_lo − Δ_sel) |
|---|---|---|---|---|---|
| 0.05 | 0.399 | +0.299 | 0.282 | 11% | +0.025 |
| 0.10 | 0.349 | +0.249 | 0.232 | 22% | −0.025 |
| 0.15 | 0.299 | +0.199 | 0.182 | 33% | −0.075 |
| 0.20 | 0.249 | +0.149 | 0.132 | 45% | −0.125 |

**Test 4 passes as a BOUNDED upper limit (no longer "unbounded") iff ALL of:**
1. Δ_sel is bounded by an explicit ceiling Δ_max. **This audit supplies Δ_max ≈ 0.20 dex**
   (independent bracket 0.05–0.20, central 0.10–0.15). ← the missing ingredient that failed Test 4.
2. Selection-corrected all-subset offset clears the residual floor: (0.449 − Δ_sel) − 0.10 > 0
   ⇒ requires Δ_sel < 0.35. **Satisfied for the entire bracket** (margin +0.15 to +0.30 dex).
3. The selection-corrected bootstrap CI excludes 0.

**Likely honest call:** Test 4 upgrades from **FAIL (unbounded)** → **PASS-as-bounded-upper-limit**.
The paper may now claim a *bounded* selection systematic Δ_sel ≲ 0.20 dex and a
**selection-corrected net z>7 deficit of ~0.25–0.35 dex (all-subset)** that remains above the
combined systematic floor at the point estimate. It may NOT be upgraded to a clean "validated
detection," because the calibration-free Te-only channel is not robust: at Δ_sel ≳ 0.10 the Te-only
corrected offset (≤0.23 dex) drops toward the floor and (Te CI_lo − Δ_sel) goes negative — i.e.
with N=4 the data cannot exclude selection erasing the calibration-free signal.

---

## 5. Adversarial bottom line — can selection eat most of the 0.45?

- **Point estimate: NO.** Δ_sel ≈ 0.10–0.15 dex = 22–33% of 0.45. Even at the ceiling (0.20) it is 45%.
  Selection *alone* cannot account for most of the matched offset.
- **BUT selection + strong-line calibration TOGETHER plausibly can.** The measured fixed-mass
  Te-vs-strong-line gap is ~0.17–0.19 dex, and the strong-line subset is 12/16 of the sample. So of
  the 0.45: ~0.12 dex is strong-line effects (offset drops to the 0.33 Te-only anchor), and another
  ~0.10 dex is Te-subset selection ⇒ only **~0.23 dex is a plausibly-physical, calibration-free residual**.
- **Small-N caveat is fatal to a clean claim:** Te-only CI = [0.075, 0.535]. The lower edge (0.075)
  is *below* the central Δ_sel — the data cannot exclude that the true calibration-free offset is
  ~0.08 dex, in which case selection accounts for essentially ALL of it.

**Verdict:** honest label stays **DESCRIPTIVE / bounded upper limit**, now with a *quantified*
(no longer unbounded) selection ceiling Δ_sel ≲ 0.20 dex and a selection-corrected net deficit
~0.25–0.35 dex (all) / ~0.23 dex (Te-only, point estimate). Bounded, not clean.

---

## 6. Cross-check on Tori's MC
If Tori's forward-model Δ_sel lands in **[0.05, 0.20] dex** → consistent, Test 4 → bounded upper limit.
If her Δ_sel **> 0.25 dex** → FLAG: check her assumed EW/sSFR-excess or FMR slope (my FMR route caps
at ~0.21 even with aggressive 0.7 dex × 0.30 inputs); such a value would also imply selection eats
most of the offset and pushes the verdict back toward "consistent with selection."
If her Δ_sel **< 0.05 dex** → FLAG: inconsistent with the sample's extreme EW(Hβ)=124 Å / sSFR=31 Gyr⁻¹.

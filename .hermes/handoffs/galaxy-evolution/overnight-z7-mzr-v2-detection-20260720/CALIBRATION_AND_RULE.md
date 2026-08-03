# CALIBRATION_AND_RULE — 2nd Te-independent transfer + mechanical upgrade computation
Hwao · Phase A design (locks the recipe; Phase B executes mechanically) · 2026-07-20 KST
Grounds strictly on ../overnight-z7-mzr-20260720/ (results.json, sdss_anchor.json). No new physics is
asserted here; this file only fixes formulas, coefficients, columns, and the boolean the rule outputs.

--------------------------------------------------------------------------------------------------------
## 0. The binding on-disk constraint (drives every choice below)
SDSS is on disk ONLY as T04 (Tremonti04/MPA-JHU) median 12+log(O/H) per mass bin + a T04 MZR fit
(sdss_anchor.json). There are **no SDSS line fluxes on disk** → we CANNOT re-run any strong-line
calibration on SDSS spectra. Therefore a valid 2nd transfer must be executable from **published relations
only**, not from SDSS fluxes. This rules out "apply Sanders+24/Curti+20 calibrations to SDSS spectra"
as the primary path and selects a published Te-anchored SDSS MZR instead.

Transfer 1 (already done, keep): **KE08** SDSS T04 → PP04-O3N2 metallicity-dependent cubic
  x_PP04 = a·y^3 + b·y^2 + c·y + d , y = 12+log(O/H)_T04 ; a=230.782, b=-75.79752, c=8.526986,
  d=-0.3162894 ; valid y=8.05-9.2 ; rms 0.046. Gave matched Δ=0.449 dex, boot95 CI [0.283,0.622].
  (sdss_pp04_grid = {8.0:8.195, 8.5:8.264, 9.0:8.372, 9.5:8.517}.)

--------------------------------------------------------------------------------------------------------
## 1. SECOND, Te-INDEPENDENT CALIBRATION TRANSFER  (chosen = option b, with a & c as extra legs)

### C2 (PRIMARY 2nd transfer) — adopt the Curti+2020 fully-Te-anchored SDSS MZR as the local anchor
**Reference:** Curti, Mannucci, Cresci & Maiolino 2020, MNRAS 491, 944 (doi:10.1093/mnras/stz2910;
arXiv:1910.00597) — "the mass–metallicity and the fundamental metallicity relation revisited on a fully
Te-based abundance scale for galaxies."
**Why this is the right independent path:** Curti+20 re-derived the SDSS MZR from the ground up on a
**fully Te-anchored** self-consistent calibration ladder. It **never passes through T04 and never uses
the KE08 polynomial**, so Δ computed against it is statistically independent of the KE08 transfer. It is a
published closed-form relation → computable on any mass grid with **no SDSS fluxes required** (satisfies §0).
The high-z Nakajima+23 O/H are also Te-anchored (direct-Te + Nakajima+22 Te ladder), so both sides share a
Te zero-point → a like-for-like second scale.
**Exact anchor formula (Curti+2020 MZR, their Eq. 3):**
    12+log(O/H)_C20(logM*) = Z0 - (γ/β)·log10( 1 + (M*/M0)^(-β) )
    Z0 = 8.793 (±0.005) ; log10(M0/Msun) = 10.02 (±0.09) ; γ = 0.28 (±0.02) ; β = 1.2 (±0.2)
    valid 7.95 < logM* < 11.85 ; intrinsic scatter 0.07 dex.  (fully covers the [8.0,9.5] overlap window.)
**Transfer-2 deficit:** Δ_C20(logM*) = OH_C20_SDSS(logM*) − OH_highz_Te(logM*).
**Wired-pipeline sanity value (computability check, NOT the reported number — Phase B produces Δ+CI):**
  OH_C20 at logM* = {8.0,8.5,9.0,9.5} = {8.18, 8.36, 8.50, 8.60} approx; vs KE08 PP04 {8.20,8.26,8.37,8.52}.
  → the two independent SDSS anchors agree to ~0.03-0.13 dex (this gap IS the calibration-family band),
  and Δ_C20 comes out ~equal-to-slightly-larger than Δ_KE08 → the deficit does not live only on the KE08 scale.
  This is arithmetic to prove the path runs; the OFFICIAL Δ_C20 is the per-object matched mean with a boot CI.

### C3 (SECONDARY, conditional) — Sanders+2024 high-z-validated Te calibration, applied to the HIGH-Z side
**Reference:** Sanders, Shapley, Topping, Reddy & Brammer 2024, ApJ 962, 24 (doi:10.3847/1538-4357/ad15fc)
— direct-Te empirical calibrations from z=1.4-8.7 JWST/NIRSpec, i.e. calibrated IN the high-z regime.
**Use:** for any high-z object whose O/H rests on a z~0-anchored strong-line calibration (Nakajima+22 R23/R3),
**re-derive its O/H by inverting the Sanders+24 high-z calibration** on its measured line ratios, then difference
against C2 (or against the Te-direct SDSS). This directly attacks PREREG Test-3 (z~0 strong-line extrapolation
at z>7). **Form:** R = c0 + c1·x + c2·x², x = 12+log(O/H) − 8.0 ; valid 12+log(O/H)=7.4-8.3:
  O3 ([OIII]5007/Hβ): c0=0.834, c1=-0.072, c2=-0.453   | R23: c0=1.017, c1=0.026, c2=-0.331
  O2 ([OII]/Hβ):      c0=0.067, c1=1.069 (linear)       | O32 ([OIII]/[OII]): c0=0.723, c1=-1.153 (linear)
  Invert the relevant quadratic for x, take the physical root in [7.4,8.3], O/H = x+8.0.
**GATE:** C3 requires the high-z **line ratios** (R23/R3/O2/O32) on disk. Phase B MUST check
_nakajima_tabled1_raw.csv / z7_multisurvey.csv for flux ratios. If present → C3 is a genuine 3rd transfer.
If ABSENT → skip C3, SAY SO, and proceed with C1+C2 (two transfers already satisfy the ≥2 rule).

### C_Te (THIRD LEG, always available) — direct-Te-only, NO transfer (option c)
Already computed in the z7 run: Te-only Δ=0.332, CI [0.075,0.535]. Keep as corroboration ONLY.
Per RECONCILIATION.md the auroral-[OIII]4363 (Te) subset is the MORE selection-biased channel, so C_Te is
**not** the conservative anchor — quote it, never lead with it.

### How the deficit is reported: the INTERSECTION of transfers
Report Δ on every available transfer {C1=KE08, C2=Curti20, (C3=Sanders24 if ratios), C_Te}. The headline
deficit = the **intersection**: conservative central = min(|Δ_C1|, |Δ_C2|); conservative CI = overlap of the
per-transfer boot CIs; the claim only stands where **every** required transfer's CI excludes 0. If any one
transfer's CI includes 0 → the deficit is that-transfer-specific → see fallback table (calibration-artifact row).

--------------------------------------------------------------------------------------------------------
## 2. THE EXACT UPGRADE COMPUTATION  (mechanical; Phase B runs this verbatim)

### Axes (the locked 8-cell S×C×O cube; matches Goru DETECTION_PREREG)
  S = survey            : need ≥2 independent (Nakajima+23 AND ≥1 of Curti+24 JADES / Heintz+23 / DESIRED / AURORA)
  C = calibration transfer : need ≥2 independent (C1=KE08 AND C2=Curti20 ; C3/C_Te are extra corroboration)
  O = orthogonal selection : need ≥1 subsample that is NOT emission-line/UV selected (lensed or deep-continuum)

### Sign convention (from results.json): Δ = OH_SDSS_anchor − OH_highz.  Δ > 0 ⇔ high-z BELOW local (a deficit).

### Per-cell procedure  cell(s,c,o):
  1. SLICE: rows with survey=s, z>7, in subsample o; drop mass_upper_limit flags; keep O-based diagnostics only.
  2. MASS OVERLAP: keep logM* ∈ [8.0, 9.5] only. Record N and [logM_lo,logM_hi]. No extrapolation.
  3. MASS-CONTROLLED Δ: for each high-z object i, evaluate the SDSS anchor on transfer c at that object's mass,
     Δ_i = OH_SDSS_c(logM_i) − OH_i ; cell Δ = mean_i Δ_i  (replicates the z7 method that yielded 0.449;
     also report the fixed-grid Δ at {8.0,8.5,9.0,9.5} so mass-dependence stays visible).
       OH_SDSS_c for c=C1(KE08): interpolate sdss_pp04_grid (KE08 cubic on sdss_anchor.json T04).
       OH_SDSS_c for c=C2(Curti20): evaluate the closed-form MZR §1.C2 at logM_i.
  4. BOOTSTRAP: ≥1e4 (match z7's 2e4) resamples of objects WITH replacement, each draw also perturbs
     logM_i by logM_err and OH_i by OH_err (+ carry SDSS intrinsic scatter 0.1488 dex / Curti 0.07 dex).
     → boot95 CI on cell Δ. Plus LEAVE-ONE-OUT: recompute dropping each object; require CI still excludes 0.

### Carried-over systematics gates (a cell only COUNTS if all four are TRUE — from the z7 prereg):
  G1 mass-matched in [8.0,9.5] (step 2 done, N>0)          G3 O-based diagnostics only (no N2/O3N2)
  G2 boot95 CI excludes 0 AND LOO keeps it excluding 0     G4 per-survey scale reconciled on transfer c (not pooled-only)

### The cell boolean:
  cell_pass(s,c,o) = (Δ > 0) AND (boot95_CI_lo > 0) AND (LOO_CI_lo > 0) AND G1 AND G3 AND G4
     (G2 is the CI clause itself.)

### Axis rollups:
  PASS_S = #{ surveys s : ∃ transfer c∈{C1,C2} with cell_pass(s, c, all-selection)=TRUE }        (need ≥2)
  PASS_C = #{ transfers c∈{C1,C2} : cell_pass(pooled-surveys, c, all-selection)=TRUE }             (need ≥2)
  PASS_O =    cell_pass(pooled-surveys, best-available c, o=orthogonal) = TRUE                      (need TRUE)

### THE LOCKED DETECTION BOOLEAN (the one thing that must be TRUE to lift the label):
  DETECTION = (PASS_S ≥ 2) AND (PASS_C ≥ 2) AND (PASS_O = TRUE)
  If DETECTION=TRUE → label = "VALIDATED DETECTION of z>7 MZR evolution below the extrapolated local relation."
  If DETECTION=FALSE → the result STAYS descriptive; the exact label is read off the fallback table (§2.1).
  Both outcomes are admissible and submittable.

### 2.1 FALLBACK LABEL TABLE (every partial outcome named; "*"=either)
  | PASS_S≥2 | PASS_C≥2 | PASS_O | Orthogonal sample status | LABEL (honest, submittable) |
  |----------|----------|--------|--------------------------|-----------------------------|
  |   T      |   T      |  T     | present & survives        | VALIDATED DETECTION of z>7 MZR evolution |
  |   T      |   T      |  F     | present, does NOT survive | Multi-survey, multi-calibration SELECTION-EXPLAINED — deficit collapses in the orthogonal sample → consistent with selection |
  |   T      |   T      |  —     | ABSENT (could not pull)   | Multi-survey, multi-calibration SELECTION-BOUNDED result (ceiling; NOT a detection — Goru make-or-break) |
  |   T      |   F      |  *     | *                         | Multi-survey, CALIBRATION-LEANING deficit (≥2 surveys but <2 independent transfers confirm) — descriptive |
  |   F      |   T      |  *     | *                         | Single-survey, CALIBRATION-ROBUST deficit (≥2 transfers, 1 survey) — descriptive, data-limited |
  |   F      |   F      |  *     | *                         | Nakajima-only SELECTION-BOUNDED descriptive (= current z7 status; no upgrade) |
  Special row — transfer disagreement: if C2 (Curti20) boot CI INCLUDES 0 while C1 (KE08) excludes it →
    "KE08-SPECIFIC / calibration-artifact: the Te-independent transfer does not confirm" → deficit NOT robust,
    stays descriptive and names the transfer dependence (this is the honest null for blocker B2).
  Any required cell with Δ≤0 (sign flip) or CI including 0 → that cell FAILS; report WHICH axis (S/C/O) failed.

--------------------------------------------------------------------------------------------------------
## 3. WHAT PHASE B CONSUMES (exact inputs)

### From Tori's z7_multisurvey.csv (Phase A output) — required columns:
  ref         (survey label; e.g. Nakajima2023 / Curti2024 / Heintz2023) — drives axis S per-survey split
  id
  z           (enforce the true z>7 slice)
  logM, logM_err   (mass-overlap cut [8.0,9.5] + bootstrap mass perturbation)
  OH, OH_err       (high-z Te/strong-line O/H + bootstrap O/H perturbation)
  calib       (direct / R23 / R3 / …) — routes C_Te leg, gates G3 O-based-only, flags Sanders-recal candidates
  mass_limit  (drop rows flagged as mass upper limits, as z7 dropped 3)
  selection   (REQUIRED for axis O: emission-line / UV-continuum / lensed / deep-continuum). If Tori did not
              populate it, Phase B MUST assign per-object selection provenance from each survey before axis O.
  [optional]  line ratios R23, R3(=O3), O2, O32 — if present, ENABLES the C3 Sanders+2024 recalibration.

### From z7 sdss_anchor.json + results.json — required fields:
  sdss_anchor.json:  T04.median_OH + mass_bin_centers (KE08-cubic input) ; T04.fit{Z0,logM0,gamma,rms} ;
                     median_bin_scatter_dex = 0.14880 (SDSS intrinsic scatter for the CI).
                     (PP04_O3N2_shifted's −0.24 CONSTANT is first-order only — DO NOT reuse; use the KE08 cubic.)
  results.json:      sdss_pp04_grid {8.0:8.195,8.5:8.264,9.0:8.372,9.5:8.517} (KE08-cubic C1 anchor, ready) ;
                     KE08_cubic coeffs ; per_grid_offset / matched_scale_offset_dex=0.449 & CI [0.283,0.622]
                     (the C1 baseline to reproduce) ; te_only_offset 0.332 CI [0.075,0.535] (C_Te leg).
  C2 (Curti20) needs NOTHING from disk beyond the high-z masses — it evaluates the §1.C2 closed form directly.

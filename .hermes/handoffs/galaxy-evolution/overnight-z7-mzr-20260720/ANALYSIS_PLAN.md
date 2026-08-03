# ANALYSIS PLAN (pre-registered) — z>7 mass–metallicity offset: physical or calibration+mass artifact?
Tori, P1. Registered BEFORE the z>7 confrontation. Decision rule fixed in advance to keep it non-circular.

## Q0. The claim under test
At fixed stellar mass, is z>7 gas-phase O/H genuinely BELOW the local (SDSS) MZR by more than can be
explained by (a) metallicity-calibration scale mismatch and (b) mass-range mismatch?

## S1. Put SDSS and high-z on ONE abundance scale (MAKE-OR-BREAK)
- **Chosen scale: PP04-O3N2 (Te-consistent).** SDSS native oh_p50 is Tremonti04 (photoionization-model),
  which runs ~0.24 dex HIGH vs Te/PP04-O3N2 (lane memo; envelope up to ~0.7 dex across families, KE08).
- **Method: apply a PUBLISHED T04 -> PP04-O3N2 conversion (Kewley & Ellison 2008, 2008ApJ...681.1183K).**
  P1 applies the first-order BULK offset (-0.24 dex) -> sdss_anchor.json PP04 block.
  **P2 MUST replace this with the KE08 metallicity-DEPENDENT cubic** (conversion is not a constant;
  it varies with 12+log(O/H)). We CANNOT recompute SDSS O3N2 directly — no line fluxes on disk.
- High-z (Curti+24, Nakajima+23) are already Te-/strong-line-calibrated; keep on their native
  Te-consistent scale and note residual family offsets as a systematic band, NOT a physical signal.
- **Every plot/number carries a scale tag.** No cross-scale comparison is allowed unlabelled.

## S2. Mass-controlled comparison (kill the mass-mismatch artifact)
- Compare O/H **at fixed stellar mass**, only in the OVERLAP mass window logM* = 8.0–9.5
  (where z>7 samples live AND SDSS has galaxies). Never compare a z>7 dwarf to a local giant.
- Evaluate SDSS MZR (PP04) and the high-z relation at the SAME logM grid: 8.0, 8.5, 9.0, 9.5.
- Report offset Delta(logM) = OH_SDSS_PP04(logM) - OH_highz(logM) at each grid point.

## S3. Uncertainty / bootstrap (small-N honesty)
- SDSS bins: N huge -> bin median uncertainty negligible; carry the 0.149 dex intrinsic scatter.
- z>7: WE HAVE NO PER-OBJECT POINTS on disk (see DATA_AUDIT gap). So:
  (a) If P2 obtains a per-object z>7 table -> bootstrap-resample galaxies (>=5000 draws), CI on the offset.
  (b) If not -> propagate the PUBLISHED fit uncertainties (Curti+24 intercept ±0.02, slope ±0.03) as a
      Monte-Carlo band; label the offset as "relation-level", explicitly NOT a per-object detection.
- Calibration systematic sigma_cal is treated as a fixed ~0.2–0.24 dex band (KE08), added in quadrature.

## S4. Simulation cross-check (non-circular third leg)
- TNG100 on disk reaches z=6 only (mzr_offset_vs_sdss: z4=-0.11, z5=-0.126, z6=-0.128).
- Overlay TNG z=6 MZR as the closest sim anchor; state z>7 TNG snapshots are NOT on disk (gap).
- If TNG z>=7 becomes reachable, add it; otherwise report the z=6 sim trend as a lower bound on evolution.

## S5. PRE-REGISTERED DECISION RULE (fixed now)
Let Delta = OH_SDSS_PP04(logM) - OH_highz(logM) at fixed mass in logM=8–9.5, sigma_cal ~ 0.2–0.24 dex.
Call the z>7 offset **PHYSICAL** only if ALL THREE hold:
  1. |Delta| > sigma_cal (offset exceeds the calibration systematic, ~0.2–0.24 dex), AND
  2. it survives mass-matching (holds within the overlap window, not driven by comparing different masses), AND
  3. the bootstrap / MC 95% CI on Delta EXCLUDES zero.
If any fail -> honest verdict: **"consistent with the local MZR within calibration + mass systematics."**
If the offset SHRINKS below sigma_cal once SDSS is moved to PP04 -> THAT (calibration explains it) IS the result.

## S6. What P1 already shows (to be confirmed, not assumed, in P2)
Native T04 SDSS OH@logM9 = 8.58; shifted to PP04 = 8.34. Published high-z @logM9: Curti+24 ~7.89,
Nakajima+23 ~7.97. Provisional Delta@logM9 ~ 0.37–0.45 dex on the matched(ish) scale — i.e. LARGER than
sigma_cal, hinting physical. BUT this uses published FITS (not our points) and Nakajima is z~4-10 (not z>7
alone). P2 must (i) apply the exact KE08 cubic, (ii) restrict to a true z>7 slice, (iii) put a CI on it
before the word "physical" is used. Until then: DESCRIPTIVE only.

## Guardrails
No fabricated points. Every abundance carries a calibration tag. Automated numbers stay DESCRIPTIVE until
human-cleared. All outputs in this lane dir.

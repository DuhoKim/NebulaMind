# Phase B — z>7 MZR detection: mechanical application of the locked rule (Tori)

Generated: 2026-07-20 16:15 KST. Real data only; every number carries a bootstrap CI (2×10⁴ resamples,
seed 20260720). Sign convention: **Δ = 12+log(O/H)_SDSS-anchor(mass) − 12+log(O/H)_z>7(mass); Δ>0 = z>7 deficit.**
Mass-overlap window [8.0,9.5]; mass-upper-limit and O/H-lower-limit rows dropped; O-based diagnostics only.

## 0. Independence cross-match (Step 1)
No RA/Dec in `z7_multisurvey.csv`, so a redshift-proximity cross-match was used as an ID proxy. Heintz's
`CEERS-z####` redshifts match Nakajima's `CEERS_#####` to <0.01 for ~8/11 objects (e.g. Heintz z7167 ↔ Nak
CEERS_00829 z=7.167; z8612 ↔ 01029 z=8.612; z7179 ↔ 00439/00498 z=7.179) → **Heintz's 11 CEERS objects are
almost certainly the same public CEERS/NIRSpec galaxies as Nakajima's** → treating them as an independent
survey would double-count. Nakajima has NO RX J2129 / Abell-cluster (RX-prefixed) objects, so the **5 Heintz
lensed galaxies (RXJ+Abell) are cleanly independent**. Decision: **Heintz(indep) = 5 lensed (N=4 with measured
O/H in overlap)**; full-Heintz (N=13) reported ONLY as a non-independent sensitivity.
> **Load-bearing caveat:** because Heintz-independent ≡ the lensed subsample, the 2nd-survey axis (S) and the
> orthogonal-selection axis (O) are carried by the **same 4 galaxies**. They are not fully independent axes.

## 1. Calibrations
- **C1 = KE08** SDSS T04→PP04-O3N2 grid {8.0:8.195, 8.5:8.264, 9.0:8.372, 9.5:8.517}, interpolated at each
  object's mass; SDSS intrinsic scatter 0.1488 dex carried in the bootstrap.
- **C2 = Curti+2020** fully-Te-anchored SDSS MZR closed form, Z0=8.793, logM0=10.02, γ=0.28, β=1.2; intrinsic
  scatter 0.07 dex. Statistically independent of C1 (never passes through T04/KE08).
- **C3 = Sanders+2024: SKIPPED** — `z7_multisurvey.csv` has no line-ratio columns (R23/R3/O2/O32) to re-invert.
  C1+C2 already satisfy the ≥2-transfer rule.
- **C_Te** (direct-Te, no transfer): corroboration only, never leads.

## 2. Per-cell Δ + bootstrap 95% CI + LOO  (survey × calibration)

| Cell (survey × calib) | N | logM range | Δ (dex) | boot95 CI | LOO range | cell_pass |
|---|---|---|---|---|---|---|
| Nakajima+23 × C1 (KE08)     | 16 | 8.12–9.39 | **+0.452** | [+0.270, +0.641] | [+0.431, +0.484] | ✅ |
| Nakajima+23 × C2 (Curti20)  | 16 | 8.12–9.39 | **+0.551** | [+0.378, +0.724] | [+0.528, +0.582] | ✅ |
| Heintz-lensed × C1 (KE08)   |  4 | 8.19–8.88 | **+0.679** | [+0.335, +1.002] | [+0.595, +0.780] | ✅ |
| Heintz-lensed × C2 (Curti20)|  4 | 8.19–8.88 | **+0.784** | [+0.477, +1.075] | [+0.715, +0.878] | ✅ |
| POOLED indep × C1 (KE08)    | 20 | 8.12–9.39 | **+0.497** | [+0.333, +0.667] | [+0.475, +0.525] | ✅ |
| POOLED indep × C2 (Curti20) | 20 | 8.12–9.39 | **+0.598** | [+0.443, +0.752] | [+0.577, +0.624] | ✅ |

Reproduction check: Nakajima×C1 Δ=+0.452, CI[+0.270,+0.641] reproduces the prior single-survey run
(Δ=0.449, CI[0.283,0.622]). C_Te corroboration (Nakajima direct-Te, N=4): Δ=+0.336, CI[+0.031,+0.644]
reproduces prior 0.332 [0.075,0.535]. C2 (Te-independent) gives an **equal-to-larger** deficit than C1 on every
cell → the deficit does NOT live only on the KE08 scale (transfer_disagreement = FALSE; not KE08-specific).

## 3. Orthogonal subsample (Step 4) — the 4 lensed galaxies (μ=1.5–19.2), NOT emission-line selected
| Orthogonal (lensed) × calib | N | Δ (dex) | boot95 CI | LOO range | PASS_O leg |
|---|---|---|---|---|---|
| lensed × C1 (KE08)    | 4 | **+0.679** | [+0.334, +1.000] | [+0.595, +0.780] | ✅ |
| lensed × C2 (Curti20) | 4 | **+0.784** | [+0.475, +1.065] | [+0.715, +0.878] | ✅ |

The orthogonally-selected (lensed, continuum/dropout) galaxies are strongly metal-poor (O/H = 7.29–7.97 at
logM 8.19–8.88), so **the deficit does not collapse under orthogonal selection — it is LARGER** than the
emission-line sample, and both transfers' N=4 CIs exclude 0 (LOO min +0.60). PASS_O required survival on BOTH
transfers (conservative intersection): TRUE.

## 4. Sensitivity — full/CEERS Heintz (NON-independent; CEERS≈Nakajima duplicates)
Full Heintz N=13: Δ=+0.677 (C1)/+0.784 (C2), CI[+0.492,+0.854]/[+0.617,+0.947]. CEERS-only N=9: Δ=+0.68/+0.78,
CIs exclude 0. Same direction and magnitude → the detection is not fragile to the independence bookkeeping.

## 5. Axis rollups & the LOCKED boolean
- **PASS_S = 2** (Nakajima+23 AND Heintz-independent-lensed; each passes ≥1 transfer). ≥2 ✅
- **PASS_C = 2** (C1 KE08 AND C2 Curti20 both pass on pooled). ≥2 ✅
- **PASS_O = TRUE** (lensed orthogonal survives on both transfers). ✅
- **DETECTION = (PASS_S≥2) AND (PASS_C≥2) AND (PASS_O) = TRUE**

## 6. Truth-table outcome
**Cell #1 — "VALIDATED DETECTION of z>7 MZR evolution below the extrapolated local relation."**

## 7. Honest one-liner
Mechanically the locked rule fires cell #1 (validated detection): a mass-controlled z>7 O/H deficit of
~0.45–0.55 dex (Nakajima+23, N=16) that survives two statistically-independent local anchors (KE08 T04→PP04
and the fully-Te-anchored Curti+2020 MZR, C2≥C1 so not a calibration artifact) and **grows to ~0.68–0.78 dex
in the cleanly-independent, orthogonally-selected lensed subsample** — whose CI excludes 0 even at N=4, so
selection cannot be the driver. **The one honest asterisk:** Heintz's CEERS objects duplicate Nakajima's, so
the "2nd independent survey" and the "orthogonal sample" are the *same* 4 lensed galaxies — the detection is
robust but its independent-survey + orthogonal axes both rest on that single small (N=4) lensed anchor;
confirming it with a second, larger orthogonally-selected sample is the obvious next step.

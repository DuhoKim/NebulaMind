# Phase (b) pre-registration — cut-sky S_1/2, like-for-like

**Ruled: Duho "a then b" (2026-09-02). Written BEFORE any observed map is opened.** In-lane; paper
HELD; no tier moves from anything below. Design choices are fixed here so they cannot be chosen
after seeing results (register §1an: pre-registration does not make a rule valid — hence the
controls in §4, including the reductio).

## 1. Objects

- **Mask:** Planck 2018 common temperature mask (`COM_Mask_CMB-common-Mask-Int_2048_R3.00.fits`,
  IRSA mirror), downgraded to working resolution with the standard threshold rule (keep pixel if
  downgraded mask value > 0.9).
- **Observed map:** Planck 2018 SMICA temperature (R3.00 full), smoothed and downgraded identically
  to the simulations.
- **Working resolution:** Nside 64, ℓ_max 128, Gaussian smoothing FWHM 160′ applied BEFORE
  downgrade to both data and simulations. S_1/2 is dominated by ℓ ≤ 20, so this is ample; the
  smoothing enters both sides identically and cancels in the comparison.

## 2. Estimator — fixed now

Pixel-pair estimator on the masked sky (the class that produced the literature ~1,150):
`Ĉ(θ) = Σ_{ij} w_i w_j T_i T_j δ_θ / Σ_{ij} w_i w_j δ_θ` over unmasked pixel pairs binned in
separation θ (binwidth 1°), then `Ŝ_1/2 = ∫_{-1}^{1/2} Ĉ(θ)² d cos θ` by the validated
Gauss–Legendre weights interpolated onto the bins. ONE estimator for data and simulations; no
switching after results.

## 3. Monte Carlo

For each model row of the gated freedom map (ΛCDM; Reading A 2π and π conventions; Reading B
spliced and no-splice): draw Gaussian a_ℓm from the model C_ℓ (unlensed, as gated), synthesize at
Nside 64 with the same smoothing, apply the SAME mask and estimator, ≥ 2,000 skies per model
(seeded, seed recorded).

## 4. Controls — all must pass BEFORE the observed value is used

- **C1 (estimator validation, full sky):** the estimator with no mask on ΛCDM MC must reproduce the
  analytic full-sky S_1/2 distribution from `cutoffA_verify_refutation.py` (median within MC error).
- **C2 (observed-value reproduction):** our estimator on the real masked SMICA map must land in the
  literature's cut-sky range (~1,000–1,300 μK⁴; Copi et al. report mask-dependent values around
  1,150). **If it does not, STOP and report — the estimator is not the literature's, and no
  comparison is licensed.**
- **C3 (reductio, §1an):** the reporting rule applied to ΛCDM itself must yield "unlikely but
  possible" (a percentile), never "refuted". Any rule that fails this is discarded before use.

## 5. Pre-registered output — percentiles only

For each model: `P(Ŝ_1/2^cut ≤ Ŝ_1/2^obs,cut | model)`. No thresholds, no verdict tokens, no tier
language. Interpretation beyond the percentile table returns to Duho.

## 6. Blind-double and gating

The pipeline is built once, then a second seat reruns it independently from this pre-registration
(not from the first implementation). Disagreement beyond MC error → third-seat adjudication with
sanity gates mandated, per the established pattern.

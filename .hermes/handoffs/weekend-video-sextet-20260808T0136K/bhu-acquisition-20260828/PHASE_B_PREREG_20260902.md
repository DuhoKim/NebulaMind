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

---

## AMENDMENT 1 — 2026-09-02, BEFORE any observed byte was opened

**Bin width 1° → 3°.** Reason, discovered during pipeline validation and not by looking at data: the
production estimator evaluates the pair sums through spherical harmonics truncated at
ℓ_max = 3·Nside − 1 = 191, which resolves angular structure down to ~0.94° — so 1° bins sit at the
smearing limit and the harmonic route measurably disagrees with literal pair-counting. At 3° bins
the two agree on `S_1/2` to 0.09–0.6% (exactness test, Nside 64, chunked brute force, committed
output). 3° binning is irrelevant to an ℓ ≲ 20-dominated statistic. Also fixed pre-data:
`anafast(..., iter=0)` (pure quadrature a_ℓm, which the pair-count algebra requires), and C1's
reference formula (first version mis-weighted C_ℓ by an extra (2ℓ+1)/4π and failed by 100× — the
control caught it, receipt in the pipeline's revision note).

**Validation state at amendment time:** exactness PASS (worst S_1/2 deviation 6.2e-3); C1 PASS
(map-route vs χ²-route medians 3.3% apart at n=2000, tail probabilities 0.30% vs 0.14%, both
consistent with the analytic ~0.125%). C2 (literature-value reproduction) and C3 (reductio in
reporting) remain to run once the mask and map arrive. The five model rows are exported with a
regression gate reproducing every gated S_1/2 (worst 4.7e-5 relative): `phaseB_model_cls.npz`.

## AMENDMENT 2 — 2026-09-02, before the observed statistic is computed

**Monopole and dipole are removed by least squares on the UNMASKED pixels, identically for the
observed map and every simulated sky.** The prereg omitted this; the literature's cut-sky ~1,150 is
defined on the mono/dipole-removed cut sky (Copi et al. convention), so without it C2 compares
against the wrong convention. Fixed now, before the observed map is opened. Data path also fixed
here: SMICA I_STOKES (K_CMB → μK), ud_grade 2048→64 (pixel window at ℓ≤20 is <0.1%, negligible),
smoothing FWHM 160′ at Nside 64 (SMICA's intrinsic 5′ beam negligible against it), mask downgraded
with the >0.9 threshold rule as pre-registered.

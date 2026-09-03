# K1 stage 1 — one-page human check sheet (Tori, 2026-09-03 17:25 KST; Duho's order "both", 17:22 KST)

**Claim checked:** in a semi-analytic model of black-hole production, N_BH RISES monotonically with the primordial amplitude A_s through the
Planck value and FALLS monotonically with the neutron-star mass cap across 2.5 M☉. Files: `K1S1_CNS_SIGN_PREREG_20260903.md` (frozen),
master pin sheet `K1S1_PIN_GATE_codex.md` + `K1S1_PIN_ROW2_REPAIR_20260903.md`, models `K1S1_claude_model.py`, `K1S1_agy_model.py`,
result `K1S1_RESULT_20260903.md`. Sources under `bhu-reading-20260823/sources/`. Numbers below are the Claude seat's printed values.

## A. Inputs (every one pinned)
| # | input | value / range | pin |
|---|---|---|---|
| 1 | Planck 2018 amplitude, tilt | ln(10¹⁰A_s) = 3.044 ± 0.014; n_s = 0.9649 ± 0.0042; k₀ = 0.05 Mpc⁻¹ | `1807.06209_clean.txt` L1526–1537, L1780, L1827, L3047–3055 |
| 2 | variance–amplitude scaling | σ²(M) = ∫ dlnk Δ²(k)|W|², Δ² ∝ P ∝ A_s ⇒ σ ∝ A_s^{1/2} | Zentner `astro-ph_0611454_clean.txt` L194, L277–278; Planck L1780 |
| 3 | IMF | Kroupa: ξ ∝ m^{−α}, α₃ = 2.3 ± 0.7 for m ≥ 1 M☉ ⇒ range [1.6, 3.0] | `astro-ph_0009005_clean.txt` L329–338 |
| 4 | remnant mass vs ZAMS mass | Fryer 2012 delayed / rapid fits; metallicity Z ∈ [0, Z☉], Z☉ = 0.02; their own cap 2.5 M☉ | `1110.1726_clean.txt` (lines as repaired in the master sheet), L436–437, L1786 |
| 5 | PBH formation | β ≈ Erfc[δ_c/(√2σ)], δ_c ∈ [0.3, 2/3] | Carr 2020 `2002.12778_clean.txt` L187–196, L1684–1686 |
| 6 | control C1 reference | stellar-BH relic density ≈ 5×10⁷ M☉ Mpc⁻³; z=0 mass function fits log N = 5.623 / 6.078 Mpc⁻³ per dex | Sicilia 2022 `2110.15607_clean.txt` L44–46, L908–918 |
| 7 | control C2 bounds | f_PBH < 1 over 1–100 M☉; O1 line f < 0.01 over 10–100 M☉ | Carr 2020 L1004–1008, L1066, L1461, L1604 |
| 8 | the bar | M_NS,max = 2.5 M☉ (Smolin's "certain refutation") | `BHU_CORPUS_SYNTHESIS_20260902.md` L60 |

## B. Steps, in order, with intermediate numbers (centre of the nuisance box: α₃ = 2.3, Z = Z☉, δ_c = 0.45; ε_* = 0.1 declared)
1. Power spectrum P(k) ∝ A_s (k/k₀)^{n_s−1} T²(k) with the Eisenstein–Hu no-wiggle shape (Zentner L305), normalised so the forward
   A_s → σ₈ conversion returns 0.829 against Planck's 0.8111 (2 %).
2. σ(M) by quadrature (input 2); Press–Schechter collapsed fraction; halo mass function by differentiation.
3. Stars per halo = ε_* × halo mass (ε_* multiplies every term: it CANCELS in the sign of both derivatives).
4. IMF fraction of stars whose Fryer remnant exceeds M_NS,max: the remnant crosses 2.5 M☉ at ZAMS ≈ 19.2–21.6 M☉ (delayed/rapid), plus at
   solar Z two further crossings at 72.5 and 94.0 M☉ from Fryer Eq. 9.
5. N_st today ≈ 1.5×10⁶ Mpc⁻³ (delayed) at the centre; ρ_BH ≈ 0.8–3.8×10⁷ M☉ Mpc⁻³ across the box.
6. N_PBH: with P(k) extrapolated to k ≈ 1.3×10⁶ Mpc⁻¹ (M_PBH = 10 M☉), σ_PBH ≈ 1.5×10⁻⁵ ⇒ log₁₀ f_PBH ≈ −10⁸ ⇒ **N_PBH = 0 in practice**.
7. Derivatives at the centre (analytic = finite difference to ≤ 4 s.f.): ∂N_BH/∂ln A_s = +2.16×10⁵ Mpc⁻³ (delayed), +2.08×10⁵ (rapid);
   ∂N_BH/∂M_NS,max = −5.38×10⁵ Mpc⁻³ M☉⁻¹ (delayed), −2.49×10⁵ (rapid). Signs identical at all 16 corners (A_s: +2.4×10⁴ … +7.7×10⁵;
   M_NS: −8.4×10³ … −1.65×10⁶). agy's independent model: same signs everywhere (magnitudes differ by its normalisation).
8. Controls: C1 n and ρ within one order of magnitude of input 6 at the centre (the α₃ = 3.0 edge 1.0–1.7 dex low, normalisation only);
   C2 trivially inside input 7; C3 deleting PBHs leaves the A_s sign +; C4 analytic vs finite-difference agree at all 18 evaluation points (16 corners of the 2⁴ box plus the centre run twice, once per Fryer engine).

## C. Final classes
θ₁ = ln A_s: **K1_MONOTONE_UP** (premise refuted for this parameter). θ₂ = M_NS,max: **K1_MONOTONE_DOWN** (consistent, not a maximum).

*(Kimi arithmetic re-check 17:30 KST: all steps recompute clean; the "18 points" count was spelled out above in answer to its one issue.)*

**Second route (17:30 KST):** direct numeric integration reproduces both classes at every box point; derivative magnitudes differ between routes by 13× (A_s) and 2× (M_NS) — normalisation-dependent, signs are not — `K1S1_ROUTE2_RECONCILIATION_20260903.md`.

## D. Where a critic could disagree (named)
1. **The production model** — Press–Schechter halos × constant star-formation efficiency × Kroupa IMF × Fryer single-star remnant fits.
   No binary evolution, no metallicity–redshift history, present-day count only. Stage 2 (`K1S2_POPSYN_PREREG_20260903.md`) addresses
   the stellar channel with binary physics.
2. **ε_* as a constant.** If star-formation efficiency itself depended on A_s (feedback, halo-mass dependence), the A_s sign is no longer
   guaranteed; the prereg declared the constant.
3. **The nuisance ranges** — α₃ ∈ [1.6, 3.0] (Kroupa's 99 % envelope), Fryer delayed vs rapid, Z ∈ {0.1 Z☉, Z☉} (agy used 0.01 Z☉),
   δ_c ∈ [0.3, 2/3]. The sign never flips inside them; a critic can propose a wider box.
4. **The PBH extrapolation** — five decades in k below the Planck pivot with a pure power law; any small-scale feature that raises
   σ_PBH to order 0.1 re-opens the PBH channel, and with it Rothman & Ellis's requirement.
5. **The normalisation check** — 2 % agreement of the A_s → σ₈ conversion; agy's C1 was a calibration, not a check (recorded).

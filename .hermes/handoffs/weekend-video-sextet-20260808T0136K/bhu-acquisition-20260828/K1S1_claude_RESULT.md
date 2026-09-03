CLASS_A_s=K1_MONOTONE_UP
CLASS_MNS=K1_MONOTONE_DOWN

# K1 stage-1 phase 2 — RESULT — seat: claude (BLIND; no K1S1_agy_* file opened)

Written 2026-09-03 17:05 KST after the run completed. Prereg `K1S1_CNS_SIGN_PREREG_20260903.md` read in full, untouched. Inputs: the master pin sheet (`K1S1_PIN_GATE_codex.md` rows 1, 3–7 with the receipts that held) plus `K1S1_PIN_ROW2_REPAIR_20260903.md` (row 2). Script: `K1S1_claude_model.py` (sha256 f05046e3111a2cbbe29e1f4036ebc0c66fb58283ce29a789d4f466e6f384dac3), system python3 + numpy 1.26.4 + scipy 1.13.1, no web. Controls C1–C4 ran and passed BEFORE the classes above were filed; the classes are the script's own printed lines.

## 1. The model as built (prereg §1), every number traced

**N_BH = N_st + N_PBH** [comoving Mpc⁻³, today], θ₁ = ln A_s, θ₂ = M_NS,max.

- **Evaluation point (row 1):** ln(10¹⁰A_s) = 3.044 → A_s,obs = 2.0989×10⁻⁹; n_s = 0.9649; k₀ = 0.05 Mpc⁻¹; 𝒫_ℛ(k) = A_s (k/k₀)^{n_s−1} (Planck Eq. 36a, `1807.06209_clean.txt:L3047–L3050`, no running in base ΛCDM). M_NS,max = 2.5 M☉ (row 4, `1110.1726_clean.txt:L1041–L1063`).
- **N_st** = ε_* (Ω_b/Ω_m) ρ_m,0 · F_coll(>M_min; A_s) · [∫ ξ(m) 1{M_rem(m) > M_NS,max} dm / ∫ m ξ(m) dm].
  - F_coll = erfc(δ_c,halo/(√2 σ(M_min))) — Press–Schechter with the factor of two (Zentner `astro-ph_0611454_clean.txt:L355–L372`, Eq. 16); δ_c,halo = 1.69 (Zentner L823).
  - σ(M) ∝ A_s^{1/2} at fixed shape (row 2: Zentner Eq. 5 L194, Eq. 14 L277–278; Planck L3047–L3050, L1780). Shape: k⁴T²(k)(k/k₀)^{n_s−1} with a real-space top-hat (Zentner L343) and the CDM transfer function of Eisenstein & Hu, which is the form the Zentner text states it uses (L305) — the no-wiggle fit is implemented from that paper; its coefficients are NOT in the source tree, so the receipt covers the choice of shape only. Normalisation: Planck σ₈ = 0.8111 (`1807.06209_clean.txt:L1813`) at A_s,obs, with H₀ = 67.36 (L1768), Ω_m = 0.3153 (L1437), Ω_b h² = 0.02237 (L1851), Ω_c h² = 0.1200 (L1845) fixing the shape (row-1 source, extra lines; sign-irrelevant). Shape check: the forward A_s → σ₈ conversion with this shape gives 0.829 vs the pin 0.8111 (2 %), so shape and normalisation are mutually consistent.
  - ε_* is a multiplicative constant: **it cancels in the SIGN of both derivatives** (it multiplies N_st and every derivative of N_st by the same positive number). Declared ε_* = 0.1 for the C1 magnitude only; M_min = 10⁸ M☉ declared (diagnostics scan 10⁶–10¹² M☉: dF/dlnA_s > 0 at every value).
  - IMF (row 3): Kroupa Eq. 1–2, `astro-ph_0009005_clean.txt:L329–L335`: α₁ = 1.3 (0.08–0.5), α₂ = 2.3 (0.5–1), α₃ ∈ [1.6, 3.0] for m ≥ 1 M☉ (2.3 ± 0.7, L335–L338), centre 2.3; stellar mass range 0.1–150 M☉ as adopted by the row-6 source itself (`2110.15607_clean.txt:L120–L121`).
  - Remnant relation (row 4): Fryer et al. 2012 fits inverted numerically at M_rem = M_NS,max. Eq. 5 (delayed, L631–L688) / Eq. 6 (rapid, L690–L805; squared exponents read from `1110.1726.pdf` pp. 11–12) below 30 M☉; Eq. 7/8 (L845–L925) for 30–50 M☉; Eq. 9 (L928–L989) above 50 M☉ at solar metallicity, max(Eq. 7|8, Eq. 9) below solar (L960–L962). Metallicity corners Z/Z☉ ∈ {0.1, 1} (L1005–L1012). The crossings of M_rem = 2.5 M☉: delayed 19.15 (Z=0.1) / 19.34, 72.5, 94.01 (Z=1); rapid 21.61 (Z=0.1) / 19.87, 72.5, 94.01 (Z=1) M☉ ZAMS. (At solar metallicity Eq. 9 brings the 50–72.5 M☉ and ≥90 M☉ remnants down through 2.5 M☉; the 94 M☉ re-entry is the source's own log₁₀(M−89) branch.)
- **N_PBH** at the declared mass scale M_PBH = 10 M☉ (row 7 window 1–100 M☉; 1 and 100 M☉ also printed): k(M) from Carr Eq. 100 (`2002.12778_clean.txt:L1544`) with γ = 1, g_* = 10.75 (declared, sign-irrelevant); 𝒫_ℛ(k) from row 1 extrapolated; σ_PBH² = (16/81)·𝒫_ℛ (radiation-era linear theory, not a sheet number — the most generous coefficient 1 is also run; nothing changes); β = Erfc[δ_c/(√2 σ)] (row 5, Eq. 101, L1683–L1687) with δ_c ∈ [0.3, 2/3], centre 0.45 (L187–L196); β → n_PBH(t₀) via Eq. 5 (L301) and β → f_PBH = Ω_PBH/Ω_CDM via Eq. 6 (L307). β is evaluated in log space with the asymptotic Erfc because it underflows.
- **Derivatives**, two ways at every box point: analytic — dN_st/dlnA_s = ε_*(Ω_b/Ω_m)ρ_m · (x/√π)e^{−x²} · n_BH/M_*, x = δ_c/(√2σ) (uses ∂lnσ/∂lnA_s = 1/2, row 2); dN_st/dM_NS = −ρ_* Σ_crossings ξ(m_c)/|M_rem′(m_c)| / ∫mξ; dlnβ/dlnA_s = (ν/2)√(2/π)e^{−ν²/2}/β (→ ν²/2); finite difference — central, h = 0.01 in lnA_s and 0.01 M☉ in M_NS,max (PBH channel in log space).
- **Nuisance box** (2⁴ = 16 corners + 2 centres): α₃ ∈ {1.6, 3.0} × {delayed, rapid} × Z ∈ {0.1, 1} × δ_c ∈ {0.3, 2/3}; centre α₃ = 2.3, Z = 1, δ_c = 0.45, both prescriptions.

## 2. Control outcomes (printed values; the full run log is in §4)

- **C1 — PASS.** Row-6 reference (Sicilia et al. 2022): ρ_• ≈ 5×10⁷ M☉ Mpc⁻³ (L44–46); integrating the z = 0 Table-1 fits (L908–L918, Eq. 12 L356–L362) over 5–160 M☉ gives n = 3.13×10⁶ Mpc⁻³, ρ = 6.1×10⁷ (field) and n = 2.15×10⁶, ρ = 4.2×10⁷ (field+cluster). Model at the observed θ with α₃ = 2.3, ε_* = 0.1: n_BH = 1.37–1.63×10⁶ Mpc⁻³ (log₁₀ n/n_ref = −0.36 … −0.12), ρ_BH = 0.8–3.8×10⁷ M☉ Mpc⁻³ (log₁₀ ρ/5×10⁷ = −0.80 … −0.12) at all four prescription×metallicity corners — within one order of magnitude in both count and mass. The ε_* that would reproduce ρ_• exactly is 0.21 (ordinary; nothing was tuned). Reported for the record: at the steep-IMF edge α₃ = 3.0 the model with ε_* = 0.1 falls to log₁₀ = −1.0 … −1.26 in n and −1.13 … −1.66 in ρ, i.e. beyond one order of magnitude; at α₃ = 1.6 it is within (+0.2/+0.5). This is a normalisation statement (ε_* × IMF) and cannot touch either sign.
- **C2 — PASS**, held to BOTH row-7 lines: f < 1 over 1–100 M☉ (L1004–L1008, L1066, L1461) and the O1 potential line f < 0.01 over 10–100 M☉ (L1604), declared before computing. At A_s,obs: k(10 M☉) = 1.30×10⁶ Mpc⁻¹, 𝒫_ℛ = 1.15×10⁻⁹, σ_PBH = 1.51×10⁻⁵, ν = δ_c/σ = 2.0×10⁴ (δ_c = 0.3) … 4.4×10⁴ (δ_c = 2/3); log₁₀ f_PBH = −8.6×10⁷ … −4.2×10⁸ (M = 1 and 100 M☉ alike; coefficient-1 variant −3.8×10⁷). The pinned Planck power law, extrapolated to the PBH scale, makes no PBHs at all: N_PBH = 10^{−(10⁷…10⁸)} Mpc⁻³.
- **C3 — PASS.** With N_PBH deleted, dN/dlnA_s is positive at all 18 box points, analytic and finite-difference agreeing; sign set with PBHs {+}, without PBHs {+}. Removing PBHs does not change the sign: Rothman & Ellis's "exclude PBHs" requirement is inert for this derivative under the pinned spectrum (the PBH channel's own derivative is also positive, dlnN_PBH/dlnA_s = +2×10⁸ … +1×10⁹, but multiplies a number that is zero to all practical purposes).
- **C4 — PASS.** At all 18 box points sign(analytic) = sign(FD) for dN/dlnA_s, dN/dM_NS,max and dlnN_PBH/dlnA_s; values agree to ≤ 4 significant figures (table below).

## 3. Derivative table over the box (from the run; N in Mpc⁻³, dN/dlnA_s in Mpc⁻³, dN/dM_NS in Mpc⁻³ M☉⁻¹, ε_* = 0.1)

```
DERIVATIVE TABLE at (A_s,obs, M_NS,max = 2.5 Msun); N in Mpc^-3; dN/dlnA_s in Mpc^-3, dN/dM_NS in Mpc^-3 Msun^-1; eps_*=0.1 (cancels in signs)
pt       a3 presc       Z    dc |       N_st  log10N_PBH |  dN/dlnAs an           FD sg  d2/dlnAs2 |   dN/dMNS an           FD sg   d2/dMNS2 | dlnNpbh/dlnAs an         FD
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
centre  2.3 delayed   1.0 0.450 |  1.515e+06  -1.931e+08 |   2.1648e+05   2.1648e+05  + -9.923e+04 |  -5.3766e+05  -5.3768e+05  -  1.950e+05 |       4.4465e+08 4.4466e+08
centre  2.3 rapid     1.0 0.450 |  1.455e+06  -1.931e+08 |   2.0792e+05   2.0792e+05  + -9.530e+04 |  -2.4946e+05  -2.4946e+05  - -9.901e+04 |       4.4465e+08 4.4466e+08
corner  1.6 delayed   0.1 0.300 |  5.355e+06  -8.583e+07 |   7.6503e+05   7.6503e+05  + -3.507e+05 |  -7.1763e+05  -7.1765e+05  -  6.723e+05 |       1.9762e+08 1.9763e+08
corner  1.6 delayed   0.1 0.667 |  5.355e+06  -4.238e+08 |   7.6503e+05   7.6503e+05  + -3.507e+05 |  -7.1763e+05  -7.1765e+05  -  6.723e+05 |       9.7592e+08 9.7594e+08
corner  1.6 delayed   1.0 0.300 |  4.821e+06  -8.583e+07 |   6.8871e+05   6.8871e+05  + -3.157e+05 |  -1.6480e+06  -1.6481e+06  - -1.658e+05 |       1.9762e+08 1.9763e+08
corner  1.6 delayed   1.0 0.667 |  4.821e+06  -4.238e+08 |   6.8871e+05   6.8871e+05  + -3.157e+05 |  -1.6480e+06  -1.6481e+06  - -1.658e+05 |       9.7592e+08 9.7594e+08
corner  1.6 rapid     0.1 0.300 |  4.827e+06  -8.583e+07 |   6.8966e+05   6.8966e+05  + -3.161e+05 |  -1.0207e+05  -1.0208e+05  -  1.349e+05 |       1.9762e+08 1.9763e+08
corner  1.6 rapid     0.1 0.667 |  4.827e+06  -4.238e+08 |   6.8966e+05   6.8966e+05  + -3.161e+05 |  -1.0207e+05  -1.0208e+05  -  1.349e+05 |       9.7592e+08 9.7594e+08
corner  1.6 rapid     1.0 0.300 |  4.699e+06  -8.583e+07 |   6.7134e+05   6.7134e+05  + -3.077e+05 |  -1.0718e+06  -1.0718e+06  - -6.743e+05 |       1.9762e+08 1.9763e+08
corner  1.6 rapid     1.0 0.667 |  4.699e+06  -4.238e+08 |   6.7134e+05   6.7134e+05  + -3.077e+05 |  -1.0718e+06  -1.0718e+06  - -6.743e+05 |       9.7592e+08 9.7594e+08
corner  3.0 delayed   0.1 0.300 |  2.179e+05  -8.583e+07 |   3.1125e+04   3.1125e+04  + -1.427e+04 |  -7.0157e+04  -7.0160e+04  -  8.129e+04 |       1.9762e+08 1.9763e+08
corner  3.0 delayed   0.1 0.667 |  2.179e+05  -4.238e+08 |   3.1125e+04   3.1125e+04  + -1.427e+04 |  -7.0157e+04  -7.0160e+04  -  8.129e+04 |       9.7592e+08 9.7594e+08
corner  3.0 delayed   1.0 0.300 |  2.074e+05  -8.583e+07 |   2.9623e+04   2.9623e+04  + -1.358e+04 |  -8.3416e+04  -8.3419e+04  -  6.553e+04 |       1.9762e+08 1.9763e+08
corner  3.0 delayed   1.0 0.667 |  2.074e+05  -4.238e+08 |   2.9623e+04   2.9623e+04  + -1.358e+04 |  -8.3416e+04  -8.3419e+04  -  6.553e+04 |       9.7592e+08 9.7594e+08
corner  3.0 rapid     0.1 0.300 |  1.704e+05  -8.583e+07 |   2.4338e+04   2.4339e+04  + -1.116e+04 |  -8.4271e+03  -8.4276e+03  -  1.142e+04 |       1.9762e+08 1.9763e+08
corner  3.0 rapid     0.1 0.667 |  1.704e+05  -4.238e+08 |   2.4338e+04   2.4339e+04  + -1.116e+04 |  -8.4271e+03  -8.4276e+03  -  1.142e+04 |       9.7592e+08 9.7594e+08
corner  3.0 rapid     1.0 0.300 |  1.958e+05  -8.583e+07 |   2.7979e+04   2.7979e+04  + -1.282e+04 |  -2.7280e+04  -2.7281e+04  -  5.812e+02 |       1.9762e+08 1.9763e+08
corner  3.0 rapid     1.0 0.667 |  1.958e+05  -4.238e+08 |   2.7979e+04   2.7979e+04  + -1.282e+04 |  -2.7280e+04  -2.7281e+04  -  5.812e+02 |       9.7592e+08 9.7594e+08

sign sets over the box: dN/dlnA_s -> ['+'];  dN/dM_NS,max -> ['-']
CLASS_A_s=K1_MONOTONE_UP
CLASS_MNS=K1_MONOTONE_DOWN
```

Sign sets over the whole box: ∂N_BH/∂lnA_s ∈ {+}; ∂N_BH/∂M_NS,max ∈ {−}. Curvature ∂²N/∂(lnA_s)² < 0 everywhere (concave but monotone: no zero crossing), ∂²N/∂M_NS² of either sign; neither partial vanishes anywhere in the box, so neither parameter is a stationary point, let alone a maximum.

## 4. Summary (≤ 200 words)

At the observed Planck amplitude and the 2.5 M☉ bar, black-hole production rises with A_s and falls with M_NS,max at the centre and every corner of the nuisance box; no nuisance flips either sign. Both signs are structural: the collapsed fraction erfc(δ_c/√2σ) grows with σ ∝ A_s^{1/2} for any transfer shape, halo threshold or δ_c, and raising the neutron-star bar can only reclassify remnants from black hole to neutron star, so dN/dM_NS,max ≤ 0 for any IMF and any continuous remnant relation. The nuisance with the largest effect on the M_NS derivative is Fryer's metallicity corner: at solar metallicity Eq. 9 adds crossings at 72.5 and 94 M☉ ZAMS, making the derivative 1.5–10× more negative than at 0.1 solar, while the rapid prescription at 0.1 solar puts its crossing on the steep Gaussian bump (10× smaller) — magnitude only. The IMF slope α₃ rescales the A_s derivative 25-fold across [1.6, 3.0] without changing sign. δ_c touches only the PBH channel, which is empty under the pinned spectrum (log₁₀ f_PBH ≈ −10⁸); including or deleting it changes nothing (C3). Smolin's local-maximum premise (1992 L233) is refuted for A_s (K1_MONOTONE_UP) and is not a maximum for M_NS,max (K1_MONOTONE_DOWN); tier/standing stamps remain Duho's.

## 5. Full run log (`python3 K1S1_claude_model.py`, 2026-09-03 17:04 KST)

```
====================================================================================================
K1S1 phase 2 -- seat claude -- semi-analytic sign test (BLIND)
====================================================================================================
A_s,obs = 2.0989e-09 (row 1: ln(1e10 A_s)=3.044), n_s=0.9649, k0=0.05 Mpc^-1; h=0.6736, Omega_m=0.3153, Omega_b=0.0493
rho_crit=1.259e+11, rho_m=3.970e+10 Msun/Mpc^3; sigma_8(pin, L1813)=0.8111
[shape check] forward A_s -> sigma_8 with the implemented CDM shape: 0.829 (Planck pin 0.8111; agreement validates the shape+normalisation)
sigma(M_min=1e8 Msun) = 5.857; F_coll(>1e8) = 0.7729; rho_* = eps_*(Ob/Om) rho_m F = 4.798e+08 Msun/Mpc^3 (eps_*=0.1, DECLARED)

----------------------------------------------------------------------------------------------------
C1  stellar-BH density at the observed theta vs row 6 (Sicilia et al. 2022; order of magnitude)
    row-6 reference: rho_BH ~ 5.0e+07 Msun/Mpc^3 (L44-46); integrated z=0 fits over 5-160 Msun: field n=3.125e+06 Mpc^-3, rho=6.105e+07; field+cluster n=2.152e+06, rho=4.155e+07
    delayed  Z=0.1  a3=1.6  BH ZAMS intervals=[(19.15, 150.0)]  n_BH=5.355e+06 Mpc^-3 (log10 n/n_ref: field +0.23, f+c +0.40)  rho_BH=1.685e+08 (log10 rho/5e7 = +0.53)  within-OOM: rho=True n=True
    delayed  Z=0.1  a3=2.3  BH ZAMS intervals=[(19.15, 150.0)]  n_BH=1.626e+06 Mpc^-3 (log10 n/n_ref: field -0.28, f+c -0.12)  rho_BH=3.755e+07 (log10 rho/5e7 = -0.12)  within-OOM: rho=True n=True
    delayed  Z=0.1  a3=3.0  BH ZAMS intervals=[(19.15, 150.0)]  n_BH=2.179e+05 Mpc^-3 (log10 n/n_ref: field -1.16, f+c -0.99)  rho_BH=3.717e+06 (log10 rho/5e7 = -1.13)  within-OOM: rho=False n=True
    delayed  Z=1.0  a3=1.6  BH ZAMS intervals=[(19.34, 72.5), (94.01, 150.0)]  n_BH=4.821e+06 Mpc^-3 (log10 n/n_ref: field +0.19, f+c +0.35)  rho_BH=2.429e+07 (log10 rho/5e7 = -0.31)  within-OOM: rho=True n=True
    delayed  Z=1.0  a3=2.3  BH ZAMS intervals=[(19.34, 72.5), (94.01, 150.0)]  n_BH=1.515e+06 Mpc^-3 (log10 n/n_ref: field -0.31, f+c -0.15)  rho_BH=7.995e+06 (log10 rho/5e7 = -0.80)  within-OOM: rho=True n=True
    delayed  Z=1.0  a3=3.0  BH ZAMS intervals=[(19.34, 72.5), (94.01, 150.0)]  n_BH=2.074e+05 Mpc^-3 (log10 n/n_ref: field -1.18, f+c -1.02)  rho_BH=1.103e+06 (log10 rho/5e7 = -1.66)  within-OOM: rho=False n=False
    rapid    Z=0.1  a3=1.6  BH ZAMS intervals=[(21.61, 150.0)]  n_BH=4.827e+06 Mpc^-3 (log10 n/n_ref: field +0.19, f+c +0.35)  rho_BH=1.618e+08 (log10 rho/5e7 = +0.51)  within-OOM: rho=True n=True
    rapid    Z=0.1  a3=2.3  BH ZAMS intervals=[(21.61, 150.0)]  n_BH=1.372e+06 Mpc^-3 (log10 n/n_ref: field -0.36, f+c -0.20)  rho_BH=3.593e+07 (log10 rho/5e7 = -0.14)  within-OOM: rho=True n=True
    rapid    Z=0.1  a3=3.0  BH ZAMS intervals=[(21.61, 150.0)]  n_BH=1.704e+05 Mpc^-3 (log10 n/n_ref: field -1.26, f+c -1.10)  rho_BH=3.542e+06 (log10 rho/5e7 = -1.15)  within-OOM: rho=False n=False
    rapid    Z=1.0  a3=1.6  BH ZAMS intervals=[(19.87, 72.5), (94.01, 150.0)]  n_BH=4.699e+06 Mpc^-3 (log10 n/n_ref: field +0.18, f+c +0.34)  rho_BH=3.359e+07 (log10 rho/5e7 = -0.17)  within-OOM: rho=True n=True
    rapid    Z=1.0  a3=2.3  BH ZAMS intervals=[(19.87, 72.5), (94.01, 150.0)]  n_BH=1.455e+06 Mpc^-3 (log10 n/n_ref: field -0.33, f+c -0.17)  rho_BH=1.209e+07 (log10 rho/5e7 = -0.62)  within-OOM: rho=True n=True
    rapid    Z=1.0  a3=3.0  BH ZAMS intervals=[(19.87, 72.5), (94.01, 150.0)]  n_BH=1.958e+05 Mpc^-3 (log10 n/n_ref: field -1.20, f+c -1.04)  rho_BH=1.803e+06 (log10 rho/5e7 = -1.44)  within-OOM: rho=False n=False
    eps_* that would reproduce rho_BH=5e7 exactly at the alpha3-centre corners: 0.214 (declared eps_*=0.1; a physically ordinary value -> not a tuned fit)
    C1 RESULT: centre-slope corners within one order of magnitude of row 6: True; whole alpha3 box: False
    C1 = PASS  (box edges alpha3=1.6/3.0 stray beyond an OOM in n or rho -- listed above; the centre passes, the edges are the 99% IMF envelope)

----------------------------------------------------------------------------------------------------
C2  PBH abundance at the observed A_s vs row 7 bounds (held to BOTH f<1 over 1-100 Msun and the O1 line f<0.01 over 10-100 Msun)
    M=    1 Msun k=4.11e+06 Mpc^-1 P_R=1.107e-09 C=0.198 sigma=1.479e-05 delta_c=0.300 nu=2.029e+04  log10 f_PBH = -8.937e+07  (bound log10 f < 0) -> ok
    M=    1 Msun k=4.11e+06 Mpc^-1 P_R=1.107e-09 C=0.198 sigma=1.479e-05 delta_c=0.450 nu=3.043e+04  log10 f_PBH = -2.011e+08  (bound log10 f < 0) -> ok
    M=    1 Msun k=4.11e+06 Mpc^-1 P_R=1.107e-09 C=0.198 sigma=1.479e-05 delta_c=0.667 nu=4.508e+04  log10 f_PBH = -4.413e+08  (bound log10 f < 0) -> ok
    M=   10 Msun k=1.30e+06 Mpc^-1 P_R=1.153e-09 C=0.198 sigma=1.509e-05 delta_c=0.300 nu=1.988e+04  log10 f_PBH = -8.583e+07  (bound log10 f < -2) -> ok
    M=   10 Msun k=1.30e+06 Mpc^-1 P_R=1.153e-09 C=0.198 sigma=1.509e-05 delta_c=0.450 nu=2.982e+04  log10 f_PBH = -1.931e+08  (bound log10 f < -2) -> ok
    M=   10 Msun k=1.30e+06 Mpc^-1 P_R=1.153e-09 C=1.000 sigma=3.395e-05 delta_c=0.450 nu=1.325e+04  log10 f_PBH = -3.815e+07  (bound log10 f < -2) -> ok
    M=   10 Msun k=1.30e+06 Mpc^-1 P_R=1.153e-09 C=0.198 sigma=1.509e-05 delta_c=0.667 nu=4.418e+04  log10 f_PBH = -4.238e+08  (bound log10 f < -2) -> ok
    M=  100 Msun k=4.11e+05 Mpc^-1 P_R=1.200e-09 C=0.198 sigma=1.540e-05 delta_c=0.300 nu=1.948e+04  log10 f_PBH = -8.243e+07  (bound log10 f < -2) -> ok
    M=  100 Msun k=4.11e+05 Mpc^-1 P_R=1.200e-09 C=0.198 sigma=1.540e-05 delta_c=0.450 nu=2.922e+04  log10 f_PBH = -1.855e+08  (bound log10 f < -2) -> ok
    M=  100 Msun k=4.11e+05 Mpc^-1 P_R=1.200e-09 C=0.198 sigma=1.540e-05 delta_c=0.667 nu=4.330e+04  log10 f_PBH = -4.071e+08  (bound log10 f < -2) -> ok
    C2 = PASS   (with the pinned Planck power law extrapolated to k~1e6 Mpc^-1, beta underflows: N_PBH is zero to all practical purposes)

----------------------------------------------------------------------------------------------------
C3  deletion probe: PBHs removed -> stellar-only sign of dN/dlnA_s
    sign set of dN/dlnA_s with PBHs: ['+']; without PBHs: ['+']; analytic==FD without PBHs at every point: True
    the sign does NOT change when PBHs are removed (both channels increase with A_s; the PBH channel is numerically zero under the pinned spectrum)
    C3 = PASS

----------------------------------------------------------------------------------------------------
C4  analytic vs finite-difference sign agreement (both partials, every box point, with PBHs)
    every row: sign(analytic)==sign(FD) for d/dlnA_s, d/dM_NS and dlnN_PBH/dlnA_s -> True
    C4 = PASS

====================================================================================================
CONTROLS: C1=PASS C2=PASS C3=PASS C4=PASS  -> classification allowed
====================================================================================================

DERIVATIVE TABLE at (A_s,obs, M_NS,max = 2.5 Msun); N in Mpc^-3; dN/dlnA_s in Mpc^-3, dN/dM_NS in Mpc^-3 Msun^-1; eps_*=0.1 (cancels in signs)
pt       a3 presc       Z    dc |       N_st  log10N_PBH |  dN/dlnAs an           FD sg  d2/dlnAs2 |   dN/dMNS an           FD sg   d2/dMNS2 | dlnNpbh/dlnAs an         FD
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
centre  2.3 delayed   1.0 0.450 |  1.515e+06  -1.931e+08 |   2.1648e+05   2.1648e+05  + -9.923e+04 |  -5.3766e+05  -5.3768e+05  -  1.950e+05 |       4.4465e+08 4.4466e+08
centre  2.3 rapid     1.0 0.450 |  1.455e+06  -1.931e+08 |   2.0792e+05   2.0792e+05  + -9.530e+04 |  -2.4946e+05  -2.4946e+05  - -9.901e+04 |       4.4465e+08 4.4466e+08
corner  1.6 delayed   0.1 0.300 |  5.355e+06  -8.583e+07 |   7.6503e+05   7.6503e+05  + -3.507e+05 |  -7.1763e+05  -7.1765e+05  -  6.723e+05 |       1.9762e+08 1.9763e+08
corner  1.6 delayed   0.1 0.667 |  5.355e+06  -4.238e+08 |   7.6503e+05   7.6503e+05  + -3.507e+05 |  -7.1763e+05  -7.1765e+05  -  6.723e+05 |       9.7592e+08 9.7594e+08
corner  1.6 delayed   1.0 0.300 |  4.821e+06  -8.583e+07 |   6.8871e+05   6.8871e+05  + -3.157e+05 |  -1.6480e+06  -1.6481e+06  - -1.658e+05 |       1.9762e+08 1.9763e+08
corner  1.6 delayed   1.0 0.667 |  4.821e+06  -4.238e+08 |   6.8871e+05   6.8871e+05  + -3.157e+05 |  -1.6480e+06  -1.6481e+06  - -1.658e+05 |       9.7592e+08 9.7594e+08
corner  1.6 rapid     0.1 0.300 |  4.827e+06  -8.583e+07 |   6.8966e+05   6.8966e+05  + -3.161e+05 |  -1.0207e+05  -1.0208e+05  -  1.349e+05 |       1.9762e+08 1.9763e+08
corner  1.6 rapid     0.1 0.667 |  4.827e+06  -4.238e+08 |   6.8966e+05   6.8966e+05  + -3.161e+05 |  -1.0207e+05  -1.0208e+05  -  1.349e+05 |       9.7592e+08 9.7594e+08
corner  1.6 rapid     1.0 0.300 |  4.699e+06  -8.583e+07 |   6.7134e+05   6.7134e+05  + -3.077e+05 |  -1.0718e+06  -1.0718e+06  - -6.743e+05 |       1.9762e+08 1.9763e+08
corner  1.6 rapid     1.0 0.667 |  4.699e+06  -4.238e+08 |   6.7134e+05   6.7134e+05  + -3.077e+05 |  -1.0718e+06  -1.0718e+06  - -6.743e+05 |       9.7592e+08 9.7594e+08
corner  3.0 delayed   0.1 0.300 |  2.179e+05  -8.583e+07 |   3.1125e+04   3.1125e+04  + -1.427e+04 |  -7.0157e+04  -7.0160e+04  -  8.129e+04 |       1.9762e+08 1.9763e+08
corner  3.0 delayed   0.1 0.667 |  2.179e+05  -4.238e+08 |   3.1125e+04   3.1125e+04  + -1.427e+04 |  -7.0157e+04  -7.0160e+04  -  8.129e+04 |       9.7592e+08 9.7594e+08
corner  3.0 delayed   1.0 0.300 |  2.074e+05  -8.583e+07 |   2.9623e+04   2.9623e+04  + -1.358e+04 |  -8.3416e+04  -8.3419e+04  -  6.553e+04 |       1.9762e+08 1.9763e+08
corner  3.0 delayed   1.0 0.667 |  2.074e+05  -4.238e+08 |   2.9623e+04   2.9623e+04  + -1.358e+04 |  -8.3416e+04  -8.3419e+04  -  6.553e+04 |       9.7592e+08 9.7594e+08
corner  3.0 rapid     0.1 0.300 |  1.704e+05  -8.583e+07 |   2.4338e+04   2.4339e+04  + -1.116e+04 |  -8.4271e+03  -8.4276e+03  -  1.142e+04 |       1.9762e+08 1.9763e+08
corner  3.0 rapid     0.1 0.667 |  1.704e+05  -4.238e+08 |   2.4338e+04   2.4339e+04  + -1.116e+04 |  -8.4271e+03  -8.4276e+03  -  1.142e+04 |       9.7592e+08 9.7594e+08
corner  3.0 rapid     1.0 0.300 |  1.958e+05  -8.583e+07 |   2.7979e+04   2.7979e+04  + -1.282e+04 |  -2.7280e+04  -2.7281e+04  -  5.812e+02 |       1.9762e+08 1.9763e+08
corner  3.0 rapid     1.0 0.667 |  1.958e+05  -4.238e+08 |   2.7979e+04   2.7979e+04  + -1.282e+04 |  -2.7280e+04  -2.7281e+04  -  5.812e+02 |       9.7592e+08 9.7594e+08

sign sets over the box: dN/dlnA_s -> ['+'];  dN/dM_NS,max -> ['-']
CLASS_A_s=K1_MONOTONE_UP
CLASS_MNS=K1_MONOTONE_DOWN

DIAGNOSTICS (declared choices scanned; sign of dF_coll/dlnA_s and of dn/dM_NS)
    M_min=1e+06: sigma=8.097 F=0.8347 dF/dlnAs=+8.1470e-02
    M_min=1e+08: sigma=5.857 F=0.7729 dF/dlnAs=+1.1042e-01
    M_min=1e+10: sigma=3.867 F=0.6621 dF/dlnAs=+1.5847e-01
    M_min=1e+12: sigma=2.221 F=0.4468 dF/dlnAs=+2.2724e-01
    generic: dF/dlnA_s = (x/sqrt(pi)) e^(-x^2) with x = delta_c/(sqrt2 sigma) > 0 for ANY sigma, shape, M_min, delta_c -> the stellar A_s-sign is structural
    generic: dN_st/dM_NS = -rho_* sum_crossings xi(m_c)/|M_rem'(m_c)| <= 0 for ANY IMF and any continuous remnant relation -> the M_NS-sign is structural
    delayed  Z=0.0 : crossings of M_rem=2.5 at ZAMS [19.134]; d(n/M*)/dMNS (a3=2.3) = -7.4852e-04
    delayed  Z=0.1 : crossings of M_rem=2.5 at ZAMS [19.154]; d(n/M*)/dMNS (a3=2.3) = -7.4931e-04
    delayed  Z=0.55: crossings of M_rem=2.5 at ZAMS [19.245]; d(n/M*)/dMNS (a3=2.3) = -7.5328e-04
    delayed  Z=1.0 : crossings of M_rem=2.5 at ZAMS [19.34, 72.5, 94.012]; d(n/M*)/dMNS (a3=2.3) = -1.1206e-03
    rapid    Z=0.0 : crossings of M_rem=2.5 at ZAMS [21.8]; d(n/M*)/dMNS (a3=2.3) = -9.1596e-05
    rapid    Z=0.1 : crossings of M_rem=2.5 at ZAMS [21.611]; d(n/M*)/dMNS (a3=2.3) = -9.7940e-05
    rapid    Z=0.55: crossings of M_rem=2.5 at ZAMS [20.75]; d(n/M*)/dMNS (a3=2.3) = -1.2662e-04
    rapid    Z=1.0 : crossings of M_rem=2.5 at ZAMS [19.874, 72.5, 94.012]; d(n/M*)/dMNS (a3=2.3) = -5.1991e-04
    n_BH per Msun formed at M_NS,max=2.0: ['3.9056e-03', '3.8227e-03', '2.9446e-03', '3.2913e-03'] (delayed Z=0.1, delayed Z=1, rapid Z=0.1, rapid Z=1)
    n_BH per Msun formed at M_NS,max=2.5: ['3.3885e-03', '3.1582e-03', '2.8600e-03', '3.0333e-03'] (delayed Z=0.1, delayed Z=1, rapid Z=0.1, rapid Z=1)
    n_BH per Msun formed at M_NS,max=3.0: ['3.0894e-03', '2.6138e-03', '2.8223e-03', '2.7098e-03'] (delayed Z=0.1, delayed Z=1, rapid Z=0.1, rapid Z=1)
```

## 6. Receipts
- Sources (sha256 as recorded in `K1S1_PIN_GATE_codex.md` / row-2 repair): `1807.06209_clean.txt`, `astro-ph_0611454_clean.txt` (c14f95336af9ad14…), `astro-ph_0009005_clean.txt` (0aa21743…), `1110.1726_clean.txt` (8f494187…, the frozen extraction) + `1110.1726.pdf` (2d99ea42…), `2002.12778_clean.txt`, `2110.15607_clean.txt` (cb90d58c…).
- Declared (no sheet number, each shown sign-irrelevant in the diagnostics): ε_* = 0.1, M_min = 10⁸ M☉, M_PBH = 10 M☉, γ = 1, g_* = 10.75, σ²_PBH/𝒫_ℛ = 16/81 (and 1), Eisenstein & Hu no-wiggle coefficients, FD steps 0.01.

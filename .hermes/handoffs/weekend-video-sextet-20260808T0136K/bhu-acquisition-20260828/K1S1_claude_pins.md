# K1 stage-1 phase-1 pin sheet — seat: claude (blind; no K1S1_agy_* file opened)

Written 2026-09-03 16:45 KST. Prereg read in full and untouched: `K1S1_CNS_SIGN_PREREG_20260903.md` (frozen). No computation was done; every number below is a quotation with a line receipt. Sources tree `T` = `.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/` (all receipts are `<file>:L<line>` in that tree; line numbers from the `_clean.txt` files as they exist at write time, sha256 listed in §9).

Convention: **PINNED** = value quoted verbatim from a file in `T` at the cited line. **UNPINNED** = no such line exists; what is missing is stated. Nothing is guessed.

---

## Row 1 — Planck 2018 primordial amplitude and tilt (θ₁ evaluation point) — PINNED

| quantity | value (68 %) | units | receipt |
|---|---|---|---|
| ln(10¹⁰ A_s) | **3.044 ± 0.014** | dimensionless | `1807.06209_clean.txt:L1530` (Table 2, 5th column = TT,TE,EE+lowE+lensing; column order at L1484–L1489, "Parameter" header L1490; Table 2 caption L1477). Same value in Table 1 "Plik [1]" column L1413 (Table 1 is the TT,TE,EE+lowE+lensing baseline, L1483) and in the extensions table L2924. |
| n_s | **0.9649 ± 0.0042** | dimensionless | `1807.06209_clean.txt:L1537` (Table 2, 5th column); verbatim with data label at L1827: "n_s = 0.9649 ± 0.0042 (68 %, Planck TT,TE,EE+lowE+lensing)". |
| pivot scale k₀ | 0.05 Mpc⁻¹ | Mpc⁻¹ | `1807.06209_clean.txt:L1780` ("A_s (which we define at the pivot scale k₀ = 0.05 Mpc⁻¹)"). |
| spectrum form | 𝒫_ℛ(k) = A_s (k/k₀)^{n(k)}, n(k) = n_s − 1 (+ running terms, zero in base ΛCDM) | — | `1807.06209_clean.txt:L3047–L3055` (Eqs. 36a–36b). |

Note: A_s itself (linear, ≈2.1×10⁻⁹) is NOT quoted here because the pinned text carries it only in log form; converting is phase-2 arithmetic. Column identity checked: the six Table 2 columns are listed in order at L1484–L1489, so the 5th entry of each parameter block is TT,TE,EE+lowE+lensing (n_s block L1533–L1538: 0.9626, 0.967, 0.980, 0.9649±0.0044, **0.9649±0.0042**, 0.9665±0.0038; ln(10¹⁰A_s) block L1526–L1531: 3.040, 3.018, 3.052, 3.045±0.016, **3.044±0.014**, 3.047±0.014).
Why standard: Planck 2018 VI is the reference ΛCDM parameter set; TT,TE,EE+lowE+lensing is the paper's own declared baseline (L1483).

## Row 2 — Linear-theory scaling of σ(M) with A_s — PINNED (exponent by definition from two pinned lines; no single verbatim "σ ∝ A_s^{1/2}" line exists in the tree — flagged for the codex gate)

| quantity | value | receipt |
|---|---|---|
| exponent p in σ(M) ∝ A_s^{p} at fixed shape (fixed n_s, fixed transfer function) | **p = 1/2** (σ² ∝ A_s) | (i) the primordial curvature power is linear in A_s: 𝒫_ℛ(k) = A_s (k/k₀)^{n(k)}, `1807.06209_clean.txt:L3047–L3050` (Eq. 36a); (ii) linear-regime power scales proportionally with A_s: "Since the CMB fluctuations are linear …, the average observed CMB power spectrum amplitude scales nearly proportionally with the primordial comoving curvature power spectrum amplitude A_s", `1807.06209_clean.txt:L1780`; (iii) σ is the dispersion (rms) of the Gaussian fluctuation field whose power is 𝒫: "horizon-scale fluctuations have a Gaussian distribution with dispersion σ", `2002.12778_clean.txt:L1683`, and the β(σ) limit is converted directly into limits on 𝒫(k) at `2002.12778_clean.txt:L1687` and Fig. 19 caption L1702 ("Constraints on power spectrum 𝒫(k) implied by … Eq. (101) for Gaussian fluctuations"). |

Statement for the model: with n_s, the transfer function and the window fixed, σ²(M) is a linear functional of 𝒫_ℛ(k) (variance of a linear Gaussian field = integral of its power), so σ²(M) ∝ A_s and σ(M) ∝ A_s^{1/2}; equivalently ∂ln σ/∂ln A_s = 1/2. The same p = 1/2 applies to the PBH-scale σ in row 5 as long as the small-scale spectrum is the extrapolated Planck power law (prereg §7 caveat stands: if a separate small-scale spike is needed, the PBH channel's A_s-dependence is not this exponent).
Why standard: linear perturbation theory; it is the definition of the amplitude parameter A_s used by Planck.

## Row 3 — Initial mass function form and published slope range (stellar-channel nuisance) — PINNED (fetched this phase)

Source: Kroupa, P. 2001, "On the variation of the Initial Mass Function", MNRAS 322, 231 (text header reads "MNRAS: in press", `astro-ph_0009005_clean.txt:L1`; arXiv astro-ph/0009005v2). Fetched this phase from arxiv.org, pinned as `T/astro-ph_0009005_clean.txt` (sha256 in §9; PDF alongside as `astro-ph_0009005.pdf`).

| quantity | value | receipt |
|---|---|---|
| form | multi-part power law ξ(m) ∝ m^{−α_i}, ξ(m)dm = number of single stars in [m, m+dm] | `astro-ph_0009005_clean.txt:L329` (Eq. 1), L336 |
| α₀ | +0.3 ± 0.7, 0.01 ≤ m/M☉ < 0.08 | L331 |
| α₁ | +1.3 ± 0.5, 0.08 ≤ m/M☉ < 0.50 | L332 |
| α₂ | +2.3 ± 0.3, 0.50 ≤ m/M☉ < 1.00 | L334 |
| **α₃ (the slope that sets the BH-progenitor fraction)** | **+2.3 ± 0.7, m ≥ 1.00 M☉** | L335 (Eq. 2); uncertainties ≈ 99 % confidence intervals for m ≳ 0.5 M☉, L336–L338 |
| Salpeter reference slope | α = 2.35 for 0.4 < m < 10 M☉ (Salpeter 1955) | L288–L289; "α = 2.3 ± 0.3 is adopted" from Fig. 1, L289 |
| Scalo steeper alternative | α₃ = 2.7 for m > 1 M☉ (Scalo 1986) | L213; used as model B1E4d, L474–L475, L490 |
| binary-corrected revision (Eq. 6) | α₁ = +1.8 ± 0.5, α₂ = +2.7 ± 0.3, α₃ = +2.3 ± 0.7 (unchanged) | L886–L889 |

Nuisance range to carry: high-mass slope α₃ ∈ **[1.6, 3.0]** = 2.3 ± 0.7 as published (≈99 % CI, L335–L338); the tighter 2.3 ± 0.3 (L289) and the Salpeter/Scalo points 2.35 / 2.7 lie inside it. Which box edges the model uses (the full ±0.7 or the ±0.3) is a phase-2 choice to be declared before computing; both are published.
Why standard: Kroupa (2001) is the canonical multi-part IMF used by population-synthesis codes; the high-mass slope's published uncertainty is exactly the nuisance the prereg names.

## Row 4 — Remnant-mass relation: ZAMS mass above which the remnant exceeds M_NS,max — PINNED (fetched this phase; the inversion M_ZAMS(M_NS,max) is phase-2 arithmetic, not done here)

Source: Fryer, C. L., Belczynski, K., Wiktorowicz, G., Dominik, M., Kalogera, V., Holz, D. E., "Compact Remnant Mass Function: Dependence on the Explosion Mechanism and Metallicity" (arXiv:1110.1726v1, `1110.1726_clean.txt:L1–L11`; published as ApJ 748, 91 (2012) — journal identity NOT verifiable from the pinned v1 text, stated from the arXiv listing). Fetched this phase, pinned as `T/1110.1726_clean.txt` (sha256 in §9; PDF alongside).

| quantity | value | receipt |
|---|---|---|
| M_NS,max adopted by the source | **2.5 M☉** ("in our standard approach we adopt a maximum NS mass of M_NS,max = 2.5 M☉; the lack of observations of compact remnants with masses between ∼2–3.5 M☉ and theoretical uncertainties make it difficult to determine an exact neutron star mass") | `1110.1726_clean.txt:L619–L621` |
| observed NS maximum quoted by the source | ∼2 M☉ | L83 |
| delayed-explosion fit, M_star ≲ 30 M☉ | M_rem,delay = 1.1 + 0.2 e^{(M_star−11.0)/4} − (2.0 + Z_metal) e^{0.4(M_star−26.0)} [M☉]; M_star = initial (ZAMS) mass, Z_metal = metallicity relative to solar | L456 (Eq. 5), L457–L458 |
| rapid-explosion fit | Eq. 6: M_rem,rapid = 1.1 + 0.2 e^{(M_star−11.0)/7.5} + 10.0(1.0+Z_metal) e^{−(M_star−23.5)²/(1.0+Z_metal)²} if M_star < 22 M☉; = M_rem,delay − 1.85 + 0.25 Z_metal + 10.0(1.0+Z_metal) e^{−(M_star−23.5)²/(1.0+Z_metal)²} otherwise | L459–L469 — CAUTION: pdftotext dropped the squared exponents onto separate lines (L460, L466 show bare "2 2"); read Eq. 6 from `1110.1726.pdf` p.11–12 before computing |
| stars ≳ 30 M☉, M_star < 50 M☉ | M_rem,delay = min(33.35 + (4.75 + 1.25 Z_metal)(M_star − 34), M_star − Z_metal^{1/2}(1.3 M_star − 18.35)); M_rem,rapid = M_rem,delay − 1.85 + Z_metal (75 − M_star)/20 | L489 (Eq. 7), L491, L494 (Eq. 8) |
| M_star > 50 M☉, solar Z | M_rem = 1.8 + 0.04(90 − M_star) if M_star < 90 M☉; 1.8 + log₁₀(M_star − 89) otherwise | L501–L502 (Eq. 9) |
| metallicity statement | "Below ∼25–30 M☉, the results are fairly insensitive to the metallicity" | L452 |
| remnant-mass gap statement | rapid mechanism reproduces the observed 2–5 M☉ gap; delayed fills it | L540–L551 (context) |

Nuisance range to carry: the two explosion prescriptions (delayed Eq. 5 vs rapid Eq. 6) × metallicity Z_metal (solar vs sub-solar, the source shows 0.1 solar at L542) bracket M_ZAMS(M_rem = M_NS,max). The threshold ZAMS mass itself is obtained by inverting Eq. 5/6 at M_rem = M_NS,max for each corner — phase 2, with M_NS,max swept across 2.5 M☉ per the prereg.
Why standard: the Fryer et al. (2012) delayed/rapid fits are the remnant-mass prescriptions used by StarTrack/COSMIC/MOBSE-class population synthesis; the source itself adopts the 2.5 M☉ bar the prereg tests.

## Row 5 — PBH formation threshold δ_c range and abundance formula β(σ) — PINNED (already in the tree)

Primary source: Carr, Kohri, Sendouda, Yokoyama, "Constraints on primordial black holes" (arXiv:2002.12778; published Rep. Prog. Phys. 84, 116902 (2021) — journal identity not verifiable from the ar5iv text, stated from the arXiv listing), `T/2002.12778_clean.txt`.

| quantity | value | receipt |
|---|---|---|
| analytic threshold | δ_c ≈ w → **1/3** in the radiation era (Carr 1975) | `2002.12778_clean.txt:L187–L188` |
| refined range | **0.3 – 0.5** (Shibata & Sasaki 1999; Green et al. 2004) | L191 |
| analytic value | **0.4** in the radiation era (Harada et al. 2013) | L192 |
| numerical, profile-dependent | **0.37 – 0.43** (Nakama et al. 2014) | L195 |
| profile-dependent full span | **0.4 – 2/3** (Musco 2019; analytic in Escrivà et al. 2020) | L196 |
| abundance formula (Gaussian, threshold statistics) | **β ≈ Erfc[ δ_c / (√2 σ) ]**, σ = dispersion of horizon-scale fluctuations | L1683–L1686 (Eq. 101); earlier form exp[−(δ_c/√2σ)²] at L189 |
| β ↔ present abundance conversion | β(M) ≈ 7.06×10⁻¹⁸ γ^{−1/2} (h/0.67)² (g_{*i}/106.75)^{1/4} Ω_PBH(M) (M/10¹⁵ g)^{1/2} ; and β(M) ≈ 7.99×10⁻²⁹ γ^{−1/2}(g_{*i}/106.75)^{1/4}(M/M☉)^{3/2}(n_PBH(t₀)/1 Gpc⁻³) | L307 (Eq. 6), L301 (Eq. 5); β′ normalisation L316 |
| critical-collapse mass scaling (context) | M ∝ (δ − δ_c)^γ | L201; cross-reference `2026_PBH_constraints_evidence_prospects_arXiv_2601.06024.clean.txt:L157–L166` (Eqs. 8–9, threshold δ_th) |

Nuisance range to carry: δ_c ∈ **[0.3, 2/3]** (outer envelope of the published ranges L191–L196), centre 0.4–0.45. The equation-of-state softening at the QCD transition lowers δ_c and produces a dominant PBH peak at M_c = O(1) M☉ (`…2601.06024.clean.txt:L265–L275`; Carr L205) — relevant to the row-7 mass-scale choice.
Why standard: Carr et al. (2021) is the standard review; Eq. 101 is the Press–Schechter-type threshold-statistics estimate the prereg names ("threshold-collapse abundance β(A_s)").

## Row 6 — C1 control: one independent published estimate of the present stellar-black-hole number density — PINNED (fetched this phase)

Source: Sicilia, A., Lapi, A., Boco, L., Spera, M., Di Carlo, U. N., Mapelli, M., Shankar, F., Alexander, D. M., Bressan, A., Danese, L., "The Black Hole Mass Function Across Cosmic Times I. Stellar Black Holes and Light Seed Distribution" (arXiv:2110.15607, AASTeX draft dated Nov 1 2021, `2110.15607_clean.txt:L1–L10`; published ApJ 924, 56 (2022) — journal identity not verifiable from the pinned text, stated from the arXiv listing). Fetched this phase, pinned as `T/2110.15607_clean.txt` (sha256 in §9; PDF alongside).

| quantity | value | units | receipt |
|---|---|---|---|
| local stellar-BH relic **mass** density | **ρ• ≈ 5 × 10⁷** | M☉ Mpc⁻³ (comoving, z ≈ 0) | `2110.15607_clean.txt:L44–L45` (abstract), L383, L599 |
| its density parameter | Ω• ≈ 4 × 10⁻⁴ (abstract, L46) / ≈ 5 × 10⁻⁴ (conclusions, L600) — the two statements in the text differ; both quoted, neither adjusted | — | L46, L600 |
| relic mass function, z = 0, field (f_field = 1) — Schechter+Gaussian fit, Eq. 12 | log N = **5.623** [Mpc⁻³] (per dlog m•), log M• = 0.607 [M☉], α = −3.781, log N_G = 2.413 [Mpc⁻³], log M•,G = 2.021, σ_G = 0.052 | Mpc⁻³ per dex | Table 1, L908–L915 (z = 0 row L915); Eq. 12 form L356–L362; valid for m• ∼ 5–160 M☉, L918 |
| relic mass function, z = 0, field+cluster (f_field = 0.6) | log N = **6.078**, log M• = 0.704, α = −2.717, log N_G = 3.496, log M•,G = 1.808, σ_G = 0.1846 | Mpc⁻³ per dex | Table 1, L915 |
| shape statement | dN/dV dlog m• "roughly constant for m• ∼ 5–50 M☉, followed by a quite steep decline for m• ≳ 50 M☉" | — | L347–L348; L590–L591 |
| redshift evolution | ρ•(z): ≲10⁵ M☉ Mpc⁻³ at z ∼ 10 → 10⁷ at z ∼ 2–3 → saturating to 5×10⁷ at z ∼ 0 | — | L381–L383 |

C1 bar as pinned: the model's stellar-BH comoving number density at the observed θ must land within an order of magnitude of the number obtained by integrating the Table-1 z = 0 fit (order 10⁵·⁶–10⁶ Mpc⁻³ per dex over the flat 5–50 M☉ range — this integration is phase 2; the quoted fit parameters are the pin), and its mass density within an order of magnitude of 5 × 10⁷ M☉ Mpc⁻³.
Why standard: an ab-initio, galaxy-statistics-based relic mass function (SFR + metallicity scaling relations × stellar/binary evolution), independent of the halo-collapse × IMF × remnant-relation construction the prereg specifies, so it is a genuine external check.

## Row 7 — C2 control: PBH abundance constraint at the chosen mass scale — PINNED

Chosen mass scale (declared here, phase 1): the **stellar-remnant window, M_PBH ∼ 1–100 M☉** — the window where the model's PBH channel and its stellar channel overlap in mass, where the QCD-softened threshold places the dominant PBH peak (M_c = O(1) M☉, `…2601.06024.clean.txt:L272–L275`), and where Rothman & Ellis's "exclude PBHs" requirement bites on the same objects the neutron-star bar concerns. Constraints are quoted as f(M) = Ω_PBH/Ω_DM for a monochromatic mass function.

| constraint | bound | receipt |
|---|---|---|
| EROS microlensing (Tisserand et al. 2007), 95 % CL | f(M) < 1 for 6×10⁻⁸ M☉ < M < 15 M☉ | `2002.12778_clean.txt:L1004–L1008` |
| quasar microlensing (Mediavilla et al. 2009), Eq. 68 | f(M) < 1 for 10⁻³ M☉ < M < 60 M☉ | L1066 |
| CMB accretion, disk (Poulin et al. 2017) | excludes a monochromatic PBH population with M > 2 M☉ as the dominant DM (f = 1 excluded above 2 M☉) | L1461 |
| CMB accretion, spherical (Ali-Haïmoud & Kamionkowski 2017) | f = 1 excluded only above 10² M☉ | L1451 |
| LIGO/Virgo O1 merger rate (Ali-Haïmoud et al. 2017) | f(M) < 0.01 for 10–300 M☉ — flagged by the review as "just a potential constraint" below 100 M☉ | L1604 |
| LIGO/Virgo O2 subsolar (Abbott et al. 2019a) | 0.2 M☉ and 1.0 M☉ binaries: at most 16 % / 2 % of DM | L1596–L1597 |
| PTA (NANOGrav) SIGW, critical-collapse scenarios | f_PBH = 1 excluded for 0.1–100 M☉ (most conservative, f_NL = −2); Gaussian case: PBHs excluded in 10–100 M☉ with stronger surrounding bounds | `2026_PBH_constraints_evidence_prospects_arXiv_2601.06024.clean.txt:L1136`, L1104–L1108 (a 2026 preprint review; context/secondary receipt only, primary is Carr 2021) |
| conversion needed to apply these to β(σ) | Carr Eq. 6 (β ↔ Ω_PBH) and Eq. 5 (β ↔ n_PBH) | `2002.12778_clean.txt:L307`, L301 |

C2 bar as pinned: at the observed A_s the model's f_PBH(M) must satisfy **f < 1 across 1–100 M☉** (three independent pinned bounds: L1006, L1066, L1461) and **f < 0.01 across 10–100 M☉** if the LIGO/Virgo O1 bound (L1604) is adopted — the model must state which of the two it is held to before computing; a model violating the f < 1 line is discarded, not tuned (prereg §5 C2).
Why standard: Carr et al. (2021) Fig. 10/12/15 (captions L930, L979, L1412) is the standard compilation; the individual bounds above are the ones the review itself tabulates for this window.

---

## 8. What is deferred to phase 2 (arithmetic only, no new inputs)
- A_s in linear form from ln(10¹⁰A_s) = 3.044 (row 1).
- M_ZAMS(M_rem = M_NS,max) by inverting Fryer Eq. 5/6 at each nuisance corner (row 4); read Eq. 6 exponents from the PDF.
- Integration of the Sicilia z = 0 fit to a number density over 5–50 M☉ (row 6).
- Conversion of β(σ) to f(M) via Carr Eq. 5–6 (rows 5, 7).
- Declaration of the nuisance box edges actually used (row 3: ±0.7 vs ±0.3; row 4: delayed/rapid × Z; row 5: δ_c ∈ [0.3, 2/3]) and of the C2 line (f < 1 vs f < 0.01).

## 9. Receipts — files and sha256 (computed at write time)

Already pinned in `T` before this phase:
```
afd514ceab21892748c8852e5f952a2fc847c17348e0ef875c2bc7b12cc14095  1807.06209_clean.txt   (Planck 2018 VI)
707d7280c1331f3477caa6815ecd4b28780df42ce49ab75eb09c29e86dd13554  2002.12778_clean.txt   (Carr, Kohri, Sendouda, Yokoyama 2021)
c06409efa728b8eb26a1155434e23104dfdff7023954c02b88841c1beeadb895  2026_PBH_constraints_evidence_prospects_arXiv_2601.06024.clean.txt  (Carr, Iovino, Perna, Vaskonen, Veermäe 2026 preprint; secondary only)
```
Fetched this phase (curl `https://arxiv.org/pdf/<id>` → `pdftotext -layout`), placed in `T`:
```
0aa2174396080f6ea51f88b9270088931a242a13e3f5174ab3e55a350222e8ae  astro-ph_0009005_clean.txt   (Kroupa 2001, IMF)
63441542f13a8588d9b5ac7d5fe3a542c8d8c300f1f7fc4030711cb3dde0e43d  astro-ph_0009005.pdf
99893109925af7b66ec52b7498c39d3ac8657b7f0aaf53015a061424d19736d7  1110.1726_clean.txt          (Fryer et al. 2012 v1, remnant masses)
2d99ea4252d293d8bed4c80673e5425f70d1ff6a3763626ed8e27ed931942839  1110.1726.pdf
cb90d58cdbbe9884e1ed1c4c4e9f1be9502c749e24aab0a76813a6857aab20d8  2110.15607_clean.txt         (Sicilia et al. 2022, stellar BH mass function)
8006190e260e96065580b6c769d4e94bd189420fe8b428f70efc4f6edd95c9f3  2110.15607.pdf
```
Working copies of the three fetches are in `$L/_tmp_k1_claude/` (lane-scoped temp; disposable).

## 10. Summary line per row
1. ln(10¹⁰A_s) = 3.044 ± 0.014, n_s = 0.9649 ± 0.0042 (TT,TE,EE+lowE+lensing) — `1807.06209_clean.txt:L1530, L1537, L1827` — PINNED
2. σ(M) ∝ A_s^{1/2} (exponent 1/2) — `1807.06209_clean.txt:L3047–L3050, L1780`; `2002.12778_clean.txt:L1683, L1687` — PINNED (by definition from pinned lines; no verbatim "1/2" line — gate to confirm)
3. Kroupa 2001 multi-part IMF, α₃ = 2.3 ± 0.7 for m ≥ 1 M☉ (range [1.6, 3.0]; Salpeter 2.35, Scalo 2.7 inside) — `astro-ph_0009005_clean.txt:L329–L338, L288–L289, L213` — PINNED (fetched)
4. Fryer et al. 2012 delayed/rapid remnant fits (Eqs. 5–9) with the source's own M_NS,max = 2.5 M☉ — `1110.1726_clean.txt:L456–L469, L489–L502, L619–L621` — PINNED (fetched; inversion to M_ZAMS is phase 2)
5. δ_c ∈ [0.3, 2/3] (1/3; 0.3–0.5; 0.4; 0.37–0.43; 0.4–2/3), β ≈ Erfc[δ_c/(√2σ)] (Eq. 101), β↔Ω_PBH Eq. 5–6 — `2002.12778_clean.txt:L187–L196, L1684–L1686, L301, L307` — PINNED
6. Sicilia et al. 2022: ρ• ≈ 5×10⁷ M☉ Mpc⁻³ at z ≈ 0; z = 0 mass-function fit log N = 5.623 (field) / 6.078 (field+cluster) Mpc⁻³ per dex, flat over 5–50 M☉ — `2110.15607_clean.txt:L44–L46, L383, L599–L600, L915, L347–L348` — PINNED (fetched)
7. C2 at 1–100 M☉: f < 1 (EROS to 15 M☉; quasar ML to 60 M☉; CMB accretion above 2 M☉), f < 0.01 for 10–300 M☉ (LIGO/Virgo O1, "potential") — `2002.12778_clean.txt:L1004–L1008, L1066, L1461, L1451, L1604`; secondary `…2601.06024.clean.txt:L1136` — PINNED

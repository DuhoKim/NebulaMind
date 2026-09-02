AUDIT_HOLDS_QUALITATIVE_DIRECTIONAL

# Entry-27 deep audit — claude-seat result (2026-09-02 17:50 KST)

**Seat:** claude-seat (Fable 5.1), independent. **Blind:** no `ENTRY27_*_RESULT` file and no file
named codex/agy/kimi was opened. **Read:** `ENTRY27_AUDIT_BRIEF_20260902.md`;
`../bhu-reading-20260823/sources/2204.11608_clean.txt` (all 1,893 lines; receipts below are its line
numbers); `PROGRAM_A_FREEDOM_MAP_20260902.md` §§1–4, §9; `PHASEB_RESULT_RECONCILIATION_20260902.md`.
Entry 23's source was NOT opened; its χ_§ = 3.149 c/H₀ = 14,015 Mpc is taken from Program (A) §1.
**No tier changed; no other file touched.** Arithmetic is shown in §A at the end.

## 1. Is the cutoff derived or asserted? — ASSERTED, on a box-size rationale; the background R is derived, the spectrum is not

The chain, step by step, marking equation vs words:

| step | content | equation or words | receipt |
|---|---|---|---|
| a | Newtonian free-fall energy, `½Ṙ² = GM/R` | Eq. 1 | L56 |
| b | Friedmann `H² = 8πGρ/3`, `r_H(τ) = 3(1+ω)τ/2` | Eqs. 2–3 | L62, L77 |
| c | `r_H ∝ a^{3(1+ω)/2}` grows faster than comoving `aχ`, so scales exit r_H in collapse and re-enter in expansion | one line of algebra + words | L82 |
| d | Cloud radius `R = [r_H² r_S]^{1/3} = r_S (a/a_BH)^{1+ω}` | Eq. 11 (re-derived by junction conditions, Eq. 28, L580–584, L670–671) | L212 |
| e | At CMB `r_H ≃ 5×10⁻⁵`, "R is about 30 times larger" | numbers, no equation shown (checks: 27.5×, §A) | L224 |
| f | The shell `R > r > r_H` is "super horizon (or frozen)" | words | L226, L233, L252, L257 |
| g | "the super horizon spectrum of perturbations in the BHU has a cut-off given by R" | words | L253 |
| h | Perturbation growth: `D₊ ∝ a`, `D₋ ∝ a^{-3/2}`; amplitude "scale invariant" by citation | standard linear growth in an unbounded FLRW, cited (Bernardeau; Zel'dovich/Harrison/Peebles–Yu); no boundary at R imposed | L258–265 |
| i | "cutoff for scales larger than λ > 2R (k < π/R)" | words; the parenthesis is the sole quantitative link and is just λ = 2π/k | L295 |
| j | `θ ≃ 2R/d_CMB ≃ 60°` | one ratio, in a figure caption | L306 |
| k | "a cutoff in the spectrum of fluctuations given by R(τ)" | words | L337 |
| l | Table 1: "super-horizon cutoff λ < 2R" | words | L420 |

Findings:

- **The background is derived; the cutoff is not.** Steps a–d and Appendix A (L460–671) are
  equations and fix R(τ). Every step that touches the perturbation *spectrum* (f, g, i, k, l) is prose.
  No perturbation equation is solved on the finite domain r < R; no boundary condition at R is ever
  written; no P(k) is written anywhere in the paper — not below the cutoff, not above it.
- **Below the cutoff the paper says only "cutoff" / "anomalous lack of the largest structures"
  (L295); above it, nothing beyond "scale invariant" by citation (L260) and "as in Inflation" (L234).**
  Whether "cutoff" means P = 0 or suppression is not stated.
- **The rationale is a box-size argument**: a cloud of diameter 2R cannot host a mode with
  λ > 2R. That is a statement about the *domain*, and it is precisely the configuration Program (A) §3
  shows cannot produce a hard Fourier cut: a field with compact support in r has P(k) entire in k, so
  `P(k) = 0 for k < π/R` is not what a finite cloud yields (Paley–Wiener). Entry 27 therefore states
  Reading A (k-space, L295) for a Reading-B physical picture (empty Schwarzschild outside R, L231,
  L563–572). It does not resolve Program (A)'s A-vs-B incompatibility; it straddles it.
- **The author concedes the gap**: "Further work is needed ... to estimate the perturbations"
  (L334); "This idea needs to be worked out and simulated" (L286); the origin of δT ≃ 10⁻⁵ is
  listed as a remaining "mystery" (L339). Program (A) flag (i) — causally disconnected ≠
  uncorrelated — applies unchanged: L265 ("survive the Big Bounce, as they correspond to variations
  of the background over scales that are causally disconnected") is the same non-sequitur.

## 2. What is R, and is it fixed non-circularly? — R at the CMB epoch is fixed by (Ω_m, Ω_Λ, H₀); non-circular; the same object as r_S only through Eq. 11, and the paper never names the epoch

- **Definition.** R is the physical radius of the FLRW cloud (L54, L231–232, L560–567), time-dependent
  via Eq. 11 / Eq. 28: `R(τ) = [r_S / H²(τ)]^{1/3}` (L212, L580). For dust the boundary is a comoving
  geodesic `χ_* = r_S/a_BH` (L221, L598).
- **r_S.** Fixed by the Λ argument: `r_S = r_Λ = H_Λ⁻¹ = (c/H₀)/√Ω_Λ`, `M = r_Λ/2G ≃ 5×10²² M☉`
  (Eqs. 8–9, L181–192). Inputs are Ω_Λ ≃ 0.7 and H₀ ≃ 70 — expansion-history quantities, not the CMB
  correlation under test. **Non-circular.** Check: M = 5×10²² M☉ ⇒ 2GM = 2.9 km × 5×10²² = 1.45×10²³ km,
  and r_Λ = 1.58–1.66×10²³ km (§A) — mutually consistent to ~10%, but **Eq. 9's printed
  "r_S ≃ 6×10²² km" (L188) is inconsistent with both by a factor ~2.5** (typo-level; it does not
  enter the angle, which is done in c/H₀ units).
- **Which epoch's R.** The paper never says. Fig. 7 plots "2R/a" (L308), i.e. the comoving
  diameter, and L224 evaluates R "at CMB times". Taking the CMB epoch (Λ negligible, so no ambiguity
  there): `R_com = R/a = Ω_m^{-1/3} Ω_Λ^{-1/6} c/H₀ = 1.57–1.59 c/H₀ = 6,730–7,090 Mpc` (§A);
  `2R_com = 3.14–3.17 c/H₀ = 13,460–14,190 Mpc`. This reproduces the paper's own "30× r_H" (27.5×).
- **The angle.** `d_CMB ≡ χ(z=1100) = 3.15–3.20 c/H₀`; `θ = 2R_com/d_CMB = 0.99–1.00 rad = 56.9–57.1°`,
  or 53.8–54.5° using the paper's rounded "30 × 5×10⁻⁵". **The "≃ 60°" is reproduced (rounded up
  from ~57°) with R = the CMB-epoch cloud radius from Eq. 11 and r_S = r_Λ.** So yes, the R in the angle
  is the same object as r_S from M — through Eq. 11 with the CMB-epoch H — and not independently.
- **Not χ_§ by definition, but equal to χ_§/2 numerically.** `2R_com = 3.14–3.17 c/H₀` vs
  `χ_§ = 3.149 c/H₀` (Program A §1): ratio 0.998–1.007. The paper itself treats them as distinct
  curves (Fig. 7 caption, L308: "2R/a, green", "χ_§ ... (dashed)", "χ_Λ = r_S/a (red)"), so they are
  different objects that coincide at Ω_m ≈ 0.3. The third curve, r_S, gives 21–22° (§A) — the "22°"
  Program A §1 records a seat having mistakenly used.
- **One internal wobble, not load-bearing for the CMB epoch:** with matter-only H today
  `R₀ = (r_S/Ω_m)^{1/3} = 1.33 r_S` (cloud outside its own horizon), while with total H
  `R₀ = r_S^{1/3} = 0.89 r_S`, which is what L225 asserts ("R = r_S ... larger than R₀ today"). The
  paper's R is thus not one comoving number across epochs (factor ~1.5 today); it is one number at the
  CMB epoch.

## 3. Does entry 27 supply the Fourier convention Program (A) left free? — It STATES one (and it is the 2π/χ_§ row, not the π/χ_§ row); it does not fix amplitude or threshold, and the statement is not licensed by a derivation

- **(a) Convention: stated, in words.** L295 gives `λ > 2R ⇔ k < π/R`. In comoving terms
  `k_c = π/R_com = 1.98–2.00 H₀/c`. Program (A)'s two rows: `2π/χ_§ = 1.995 H₀/c`, `π/χ_§ = 0.998 H₀/c`.
  **Entry 27's stated cutoff equals the `2π/χ_§` row to within 1%** (cutoff wavelength
  `2R_com ≈ 14,100 Mpc ≈ χ_§`, not `2χ_§ = 28,030 Mpc`). The brief's "Reading A, π/χ_§" row (0.4–0.8%)
  is therefore NOT what entry 27 says; entry 27 names the row Phase (b) found most favourable
  (2.2–2.8% vs ΛCDM 0.15–0.2%, `PHASEB_RESULT_RECONCILIATION_20260902.md` L17–18). This identification
  (R_com ≈ χ_§/2) is lane-owned arithmetic; the paper never mentions χ_§'s value.
- **(b) Amplitude above the cutoff: not fixed.** "Scale invariant" by citation (L260); "as in
  Inflation" (L234); the 10⁻⁵ amplitude is an open problem (L339). Implicitly defers to ΛCDM's
  spectrum, but never says so. The *shape* of the cut (hard vs. smooth) is also unstated — and a hard
  cut is what the finite-cloud picture cannot deliver (§1). Transfer physics: standard recombination
  assumed (L294, Table 1 L362–366) — a reasonable "defers to ΛCDM", but again by silence.
- **(c) Threshold: none.** No statistic is named (no S₁/₂, no C(θ), no C_ℓ), no predicted value, no
  pass/fail number. The only numbers are the 60° angle (L306) and the measured 66 ± 9° (L303).
- **Net:** with the convention taken at face value, `P(k)=0 for k<π/R_com` + ΛCDM above + standard
  transfer IS a definite computation — it is Program (A) §4's `2π/χ_§` row (6,897 μK⁴ full-sky) and
  Phase (b)'s 2.2–2.8% row. But three of the four ingredients (hard cut, ΛCDM amplitude, Reading A
  over B) are lane choices the paper does not make; the paper's contribution is one parenthesis.

## 4. Is 66 ± 9° a prediction or a measurement compared to? — A measurement compared to; entry 27 forecasts nothing the 2021 measurement could have missed

- L303: "A recent study of the homogeneity index in the CMB (Camacho-Quevedo & Gaztañaga 2021)
  finds a cutoff scale Θ_H = 66 ± 9 degrees. This is shown as the black symbol in Figure 7." The
  reference is arXiv 2106.14303, June 2021 (L878–885); entry 27 was received 27 January 2022 (L21).
  So the number is prior to the paper and is the author's own.
- The theory-side number is `θ ≃ 2R/d_CMB ≃ 60°` (L306) — 54–57° by the arithmetic in §A, consistent
  with 66 ± 9 at ~1σ. That forecast is entry 23's (2020, "60 ± 3", Program A §1); entry 27 restates it.
  Fig. 7 (L308) compares the measurement against three candidate curves (2R/a, χ_§, r_S) and reports
  "good agreement" (L302) for the first two; the third (~22°) is excluded — the paper does not
  discuss that as a discriminant.
- Anything forecast beyond the 60°? "Current and future galaxy surveys are also able to measure this
  signal ... could also appear as a dipole" (L337–338) — no number. Appendix C's rotation bound
  `r_J ≪ 10⁻⁸ r_S`, `Ω_J ≃ 10⁻¹⁶` (L763–774) is stated to be "undetectable" — a consistency bound,
  not a falsifier. **Nothing numeric that the 2021 measurement could have missed.**

## 5. Tier consequence — QUALITATIVE-DIRECTIONAL holds; not a CALIBRATED-FALSIFIER challenge; not a CONSISTENCY-ONLY challenge

- **Against CALIBRATED-FALSIFIER.** The scheme's "number" is the predicted value of an observable.
  Entry 27 supplies a *scale* (2R_com ≈ 14,100 Mpc, θ ≈ 57°) — which entries 23–26 already had — plus
  a Fourier constant in a parenthesis (L295). It supplies no P(k), no amplitude, no statistic, no
  threshold (§3b–c), and the constant it names sits on a physical picture that contradicts it (§1).
  A number that becomes definite only after the lane chooses hard-cut, ΛCDM-above, and Reading-A-over-B
  is a lane number, which the scheme forbids the lane to supply. **No promotion.**
- **Against CONSISTENCY-ONLY.** The direction — less large-angle correlation than ΛCDM at a scale set
  non-circularly by (Ω_m, Ω_Λ, H₀) — is present, and it is robust across the readings the paper fails
  to choose between: every refinement Phase (b) computed (A at either constant, B spliced or not)
  moves the observed sky's percentile up from ΛCDM's 0.15–0.2% (PHASEB L16–20), i.e. all suppress.
  The scale chain (Eqs. 1–11, App. A) is real equations. That is exactly what QUALITATIVE-DIRECTIONAL
  is for. **No demotion.**
- **What the sweep's promotion rationale gets wrong, for the record:** entry 27 does not "derive"
  the cutoff any more than entry 23 did; it *restates* it (L253, L295, L337, L420) with one new
  parenthesis, and its own text concedes the perturbations are unestimated (L334). The tier is
  right; the word "derives" in the 2026-09-01 sweep note is not.
- **Packet item for Duho (not a tier move):** the paper-stated convention is `k_c = π/R_com ≈ 2π/χ_§`,
  i.e. Phase (b)'s **2.2–2.8%** row, not the 0.4–0.8% row. If the lane ever labels one Phase (b) row
  "the author's reading", it is that one — with the caveat that the label rests on a parenthesis and
  on a lane identification R_com ≈ χ_§/2.

## Plain language

This paper is a review that restates the black-hole-universe story and, along the way, says the
sky should lack the very largest ripples — anything bigger than the collapsing cloud, which works
out to about 57–60 degrees across. I checked that arithmetic and it holds, using only the expansion
history (dark-energy fraction, matter fraction, Hubble rate), not the CMB anomaly itself, so the
scale is honest. But the paper never writes down what the ripple spectrum should actually look like:
it says "cutoff" in words, gives no formula, no amplitude, no test statistic, and no pass/fail
number, and the author himself says the perturbations still need to be worked out. One new thing
it does add is a parenthesis saying the cutoff sits at wavenumber π/R — and by my arithmetic that
picks the more generous of the two conventions the lane had been carrying (the one where the
observed sky lands at about 2–3% instead of 0.4–0.8%). That is worth recording, but it is a phrase,
not a derivation, and it describes a sharp Fourier cut for a finite cloud that mathematically cannot
have one. So the paper points in a direction at a fixed scale, with no calibrated amplitude —
which is what its current tier already says. Hold.

## A. Arithmetic (units c/H₀ unless stated; c/H₀ = 4,475 Mpc at H₀ = 67, 4,283 Mpc at H₀ = 70)

For (Ω_m, Ω_Λ) = (0.3, 0.7) and (0.31, 0.69):

- `r_S = r_Λ = Ω_Λ^{-1/2}` = 1.195 / 1.204 → 5,348 / 5,387 Mpc (H₀=67) = 1.65×10²³ / 1.66×10²³ km.
  Eq. 5 at M = 5×10²² M☉: 2.9 km × 5×10²² = 1.45×10²³ km. Eq. 9's "6×10²² km" (L188) matches neither.
- `r_H(a=10⁻³) = a^{3/2} Ω_m^{-1/2}` = 5.77×10⁻⁵ / 5.68×10⁻⁵ (paper L224: 5×10⁻⁵).
- Eq. 11 at CMB: `R = (r_H² r_S)^{1/3}` = 1.585×10⁻³ / 1.572×10⁻³; `R/r_H` = 27.5 / 27.7 (paper: ~30).
- `R_com = R/a = Ω_m^{-1/3} Ω_Λ^{-1/6}` = 1.585 / 1.572 → 7,093 / 7,033 Mpc (H₀=67).
- `2R_com` = 3.171 / 3.144 → 14,187 / 14,066 Mpc (H₀=67); vs χ_§ = 3.149 (14,015 Mpc): ratio 1.007 / 0.998.
- `d_CMB = ∫_{1/1101}^{1} da /(a² E(a))` = 3.195 / 3.153 → 14,296 / 14,109 Mpc (H₀=67).
- `θ = 2R_com/d_CMB` = 0.992 / 0.997 rad = **56.9° / 57.1°**; with the paper's rounded R = 30×5×10⁻⁵
  (R_com = 1.5): 3.0/3.195 = 0.939 rad = 53.8° (54.5°). Paper: "≃ 60°" (L306).
- Alternatives in Fig. 7: `χ_§/d_CMB` = 3.149/3.153 = 57.2° (Program A's 57.4°); `r_S/d_CMB` = 21.4° / 21.9°.
- Fourier constants: `π/R_com` = 1.982 / 1.999 H₀/c; `2π/χ_§` = 1.995; `π/χ_§` = 0.998.
- `τ_BH = −(2/3) r_S` = −11.1 to −11.7 Gyr (paper L243: −11 Gyr).
- Today: `R₀ = (r_S/Ω_m)^{1/3}` (matter-only H) = 1.585 = 1.33 r_S; `R₀ = r_S^{1/3}` (total H) = 1.061 = 0.89 r_S.

Computed with scipy.integrate.quad; no lane script was written or modified.

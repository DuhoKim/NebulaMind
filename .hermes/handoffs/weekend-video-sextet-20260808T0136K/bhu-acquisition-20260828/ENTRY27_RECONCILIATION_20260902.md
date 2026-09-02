# Entry-27 deep audit — reconciliation (Tori, 2026-09-02, STEP 3 of Duho's "a → b → c")

**Entry 27 — E. Gaztañaga (2022), "How the Big Bang Ends Up Inside a Black Hole," Universe 8, 257**
(arXiv 2204.11608). Tier **QUALITATIVE-DIRECTIONAL**. Brief `ENTRY27_AUDIT_BRIEF_20260902.md`.

## Verdict — BOTH SEATS AGREE, tier holds; no MUST-STOP

| seat | token |
|---|---|
| codex (`ENTRY27_codex_RESULT.md`) | `AUDIT_HOLDS_QUALITATIVE_DIRECTIONAL` |
| claude-seat (`ENTRY27_claude_RESULT.md`, blind) | `AUDIT_HOLDS_QUALITATIVE_DIRECTIONAL` |

## What both derived independently (verified by Tori against the pinned source and by arithmetic)
1. **The background radius is derived; the spectral cutoff is asserted.** Eq. 11 gives the finite
   cloud radius R(τ) = [r_H² r_S]^{1/3} (lines 210–216) and Appendix A recovers the junction; the step
   from "frozen region R > r > r_H" to "cutoff for k < π/R" (line 295) is prose — no P(k) on either
   side, no boundary condition at R, and the author states the perturbations still need estimating
   (lines 329–334) and calls the δT ≈ 10⁻⁵ amplitude a remaining mystery (line 339). The 09-01 sweep's
   word "derives" overstates it; the paper **restates** the series' cutoff with a Fourier constant.
2. **R is fixed non-circularly** from (Ω_m, Ω_Λ, H₀) via the background solution, and it is neither
   r_S nor χ_§ (Figure 7 plots 2R/a, χ_§ and χ_Λ = r_S/a as three separate curves, line 308). Line 224:
   at a ≈ 10⁻³, r_H ≈ 5×10⁻⁵ c/H₀ and R ≈ 30× that. Tori's recompute: comoving R/a ≈ 6,700 Mpc, giving
   θ = 2R/d_CMB ≈ 55° (paper: "≃ 60"); exact 60° needs R/a ≈ 7,330 Mpc. claude-seat: 56.9–57.1° with
   its own inputs. Coarse but consistent.
3. **Entry 27 supplies the Fourier convention entry 23 left free — and it is the 2π/χ_§ one.**
   k_cut = π/(R/a) ≈ 4.3–4.7×10⁻⁴ Mpc⁻¹, versus 2π/χ_§ = 4.48×10⁻⁴ and π/χ_§ = 2.24×10⁻⁴. So the
   paper-stated reading corresponds to phase (b)'s **most favourable row, Reading A at 2π/χ_§
   (2.2–2.8%)**, not the π/χ_§ row (0.4–0.8%) the brief and the 09-01 sweep receipt implied. This is a
   correction to the record's reading of the convention, not to any tier: the percentile still rests on
   the lane's external ΛCDM normalisation and transfer choices (freedom map §4, §7), the paper states no
   amplitude, statistic or threshold, and a hard Fourier cut for a finite cloud is the reading Program
   (A) §3 showed cannot coexist with real-space compact support.
4. **66 ± 9° is a measurement compared to, not a forecast**: the author's own homogeneity-index result
   (Camacho-Quevedo & Gaztañaga 2021, arXiv 2106.14303, June 2021; the paper was received January 2022),
   plotted as a data point against a ~60° scale first forecast in entry 23. No forecast uncertainty,
   likelihood or miss criterion is given.
5. **Tier:** not CALIBRATED-FALSIFIER — the missing item is the number (normalised spectrum / C_ℓ /
   statistic), which the lane may not supply, not merely a threshold, which it may. Not CONSISTENCY-ONLY —
   the direction and scale survive every reading phase (b) computed. QUALITATIVE-DIRECTIONAL holds.

## Side findings for the record (no action)
- Eq. 9 prints r_S ≃ 6×10²² km for M ≃ 5×10²² M☉; 2GM/c² gives 1.48×10²³ km (2.95 km × 5×10²²), a
  ~2.5× discrepancy in the printed number that does not enter the angle (claude-seat; Tori verified).
- The Phase (b) map annotation on entries 23–27 names "Reading A, 2π/χ_§" as the best row without
  saying entry 27 selects it; the entry-27 annotation below now says so.

## Applied
Dated deep-audit annotation on entry 27 in the bibliography (tier word untouched). STEP 3 continues down
the parked queue; the next entry after 27 is drawn by the same density rule from the 2026-08-29 census.

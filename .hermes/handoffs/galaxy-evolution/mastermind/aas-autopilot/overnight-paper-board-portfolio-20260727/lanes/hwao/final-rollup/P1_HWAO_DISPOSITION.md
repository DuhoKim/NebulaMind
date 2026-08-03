# P1 Hwao Disposition — Massive-Galaxy Abundance Audit

Adjudicator: Hwao / Fable, final-rollup lane. Written 2026-07-27 ~22:46 KST (13:46 UTC). Stop files checked before writing: absent.

## Disposition

**`PARTIAL__CLAIMS_REQUIRE_NARROWING` — UPHELD, with Lana's four patches adopted.** The primary-source-support **FAIL** remains the blocker for revision-readiness. No manuscript revision tonight.

## Receipts relied upon

| Receipt | Lane / role | Marker | Verdict |
|---|---|---|---|
| `input/P1/kun/RECEIPT.json` + 6 artifacts (`KUN_VERDICT.md`, `QUERY_COVERAGE.json`, `CUMULATIVE_DENSITY_LEDGER.csv`, `SYSTEMATIC_BUDGET_LEDGER.csv`, `SIMULATION_COMMENSURABILITY.md`, `SOURCE_ROLE_AUDIT.md`) | Kun, primary | `P1_KUN_PRIMARY_COMPLETE_20260727` | `PARTIAL__CLAIMS_REQUIRE_NARROWING` |
| `input/P1/lana/RECEIPT.json`, `CROSSREVIEW.md`, `VALIDATION.json` | Lana, scientific-scope cross-review | `P1_LANA_CROSSREVIEW_COMPLETE_20260727` | `PASS_WITH_PATCHES` — all 7 Kun grades confirmed; all headline arithmetic independently recomputed and matching; patches P-1…P-4 additive |
| `input/P1/goru/RECEIPT.json`, `CROSSREVIEW.md`, `VALIDATION.json` | Goru, mechanical cross-review | `P1_GORU_CROSSREVIEW_COMPLETE_20260727` | `PASS` (mechanical scope; **advisory, not proof**) |
| `input/TORI_BROWSER_SOURCE_CHECK.md` | Tori, independent rendered-page check | `TORI_INDEPENDENT_SOURCE_IDENTITY_CHECK_20260727` | 300-dpi render of pinned page 3 (PNG SHA-256 `68373de4…b11c5a7`): arrow says 0.28, caption says 0.20 — real same-page contradiction; plus the Table 1 clipping finding |
| `input/VALIDATION_T1.json` | Tori validator | — | `p1_pdf`/`p1_review`/`p1_history` all 200 with exact SHA-256 identity match (`189a2764…23f5d` etc.); arithmetic block independently reproduces n₁₅/n₂₀/ratios/dex shifts |

No self-review occurred. Kun's receipt attests pinned-byte access plus public primary-source identity checks (no gated access used; Nature paywall respected); Lana re-hashed all 24 manifest files (0 mismatches) and verified the figure defect by an independent method (embedded text layer vs Kun's visual render).

## What conditional abundance statement survives

Only Kun's narrowed conditional wording, amended by Lana's patches P-1 and P-2 — adopted here as the **maximum claim this artifact supports**:

> On the served draft's adopted z = 5 footing, the TNG100-1 count and the *claimed* Weibel cumulative density imply a factor-two offset, corresponding to **0.20–0.28 dex depending on the simulation mass footing (all-bound vs 2×R_half)** for the measured massive-end slope |s| = 1.58. This suggests, but does not by itself prove, that the z = 5 total-population comparison is not a robust TNG tension. At an effective comparison redshift of z ≈ 5.5 the required shift rises to ≈0.4 dex and is at best marginally covered.

Explicitly not survivable: "robust and IMF-independent consistency with TNG" (title/abstract strength); any claim that the z≈7–9 Labbé candidate point or the spectroscopic z>6 quiescent residual is resolved; the analytic baryon-ceiling ε as native TNG efficiency; per-object maxima combined into a z≈4–6 total-population budget without covariance and population fractions.

Rationale for the footing bracket (Lana §1, endorsed): the all-bound `SubhaloMassType` footing is an *upper* bracket for what SED photometry measures — the served draft adopted the footing most favorable to its conclusion, so the honest requirement spans both footings. Rationale for the z≈5.5 demotion (Lana §7, endorsed): the 0.46–0.55 dex quadrature budget is covariance-*inflated*, which runs in the draft's favor; a correlation-aware budget (~0.3–0.4 dex) still covers the z=5 headline but **not** the z≈5.5 case (0.42 dex), so "still within budget" at z≈5.5 is demoted to marginal.

## Preserved defects (none repaired tonight)

1. **Zero direct observed cumulative-density rows.** The observed anchor ≈3×10⁻⁵ Mpc⁻³ at n(>10^10.5 M☉) is asserted without any primary-source cumulative row carrying threshold, selection, completeness, scatter, Poisson, and cosmic-variance fields. Goru's count — 0 explicit observed cumulative rows, 3 simulation rows, 3 indirect rows — confirmed by Lana against the ledger and PDF. Weibel et al. 2024 is differential SMF/Schechter by role. **This FAIL is the standing blocker.**
2. **Population and covariance mismatches.** Table 1 mixes object classes, redshifts, and SED classes; SB2–SB4 are one SED degeneracy; SB6 partly derives from SB1–SB4; the #5 LRD population average rests on an asserted, not measured, fraction; UV-red vs UV-blue never propagated; centrals/satellites unseparated; 1.30 dex linear sum is an upper bound only.
3. **Same-page 0.28-arrow vs 0.20-caption defect.** Figure 1's plotted arrow still reads "erased by 0.28 dex M⋆" while the caption and all prose read 0.20 dex — verified by three independent methods (Kun render, Lana text layer, Tori 300-dpi render). Revision state `PARTLY_LANDED` preserved. Related new finding preserved: the legend label "Weibel+2024 (z≈5–6)" contradicts §3.2's own z=5 pinning argument (Lana P-3).
4. **Table 1 right-edge clipping.** Tori's rendered-page check found the rightmost `grounding` column overruns and truncates citation strings at the page edge. Preserved as a layout defect for the morning repair list.
5. **Unreproduced TNG counts.** N=15 / N=20 / N=4 are manuscript-reported, not regenerated from catalogs in any lane; densities and dex conversions reproduce arithmetically (four independent recomputations agree) but the counts themselves stay unverified.
6. 2025–2026 systematic-budget references (Harvey 2025, Cochrane 2025, Kocevski 2025, Choe 2026, Zhuang 2026, plus Lapi 2024/Steinhardt 2023) remain version-unverified; correctly not promoted. Minor observation preserved: `served-review.md` says "Human feedback: not captured" while `served-history.json` has `humanFeedback.captured: true` — different record types, but flagged for a one-line clarification at next regeneration.

## Disagreement resolution

No conflicts. Goru's `PASS` is mechanical-scope and advisory. Lana's cross-review does not overturn any Kun grade — it confirms all seven and adds patches; where Lana sharpened (footing bracket, budget directionality), the sharpening *narrows* claims further and is adopted. Kun's original narrow wording alone is judged slightly too strong; the patched version above governs.

## Remaining unsupported / blocked / partial / disputed rows

- FAIL: primary-source `n(>M*)` support (CD4 for the strict gate; CD5 if used for the headline).
- PARTIAL: CD1–CD3 (internally coherent, unreproduced), CD6 (ceiling framing only), SB1–SB7, query coverage, statistic identity, population commensurability, simulation commensurability, source version, claim strength.
- PASS-as-caveat-only: SB8 linear sum; Labbé as a separate caveat.
- Marginal (demoted tonight): the z≈5.5 "still within budget" claim.

Automated reviews and this adjudication are not human validation or peer review. No manuscript, public artifact, or project state was modified by this disposition.

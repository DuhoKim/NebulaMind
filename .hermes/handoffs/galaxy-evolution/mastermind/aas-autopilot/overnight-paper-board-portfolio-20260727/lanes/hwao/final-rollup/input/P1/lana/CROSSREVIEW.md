# P1 Scientific-Scope Cross-Review — Lana

Cross-review of Kun's completed P1 primary audit (`input/primary/`), performed independently against the pinned served artifact and all immutable inputs. Kun's outputs were not edited. Goru's mechanical cross-review (`input/goru_crossreview/`) was read for conflict-checking only.

## 0. Custody and independent re-verification

- All 24 files in `input/INPUT_MANIFEST.json` re-hashed: SHA-256 and byte counts match exactly, zero mismatches.
- `served-p1.pdf` = `189a2764…23f5d` (123,312 bytes, 4 pages) — identical to Kun's pinned identity, to the lane snapshot manifest, and to the public-fetch identity in `PUBLIC_ARTIFACT_IDENTITY.json` (fetched 2026-07-27T13:02:48Z, ETag `W/"1e1b0-19f8eaeb939"`, Last-Modified 2026-07-23 11:14:03 GMT).
- Board-card identity (`FrontierDrafts.tsx`): same PDF route, `updated: 2026-07-23 20:14` = public Last-Modified + 9 h (KST), verdict `REVIEW-READY`. Consistent.
- Full text of the pinned PDF was independently extracted in this lane (all 4 pages). Every headline number was independently recomputed (Section 2).

## 1. Estimand commensurability (observed vs simulated) — CONFIRM `PARTIAL`

Kun's `PARTIAL` is correct and is, if anything, generous. Independent findings:

- The compared statistic is genuinely cumulative `n(>10^10.5 Msun)` on both sides in prose, and the TNG aperture states are correctly named (`SubhaloMassInRadType` 2×R_half vs `SubhaloMassType` all-bound).
- **Sharpening (new emphasis):** the draft's "total-mass footing" equates observed SED total-galaxy masses with TNG *all-bound* stellar mass. TNG convention guidance treats ≤2×R_half or a ~30 pkpc fixed aperture as closest to observed photometric masses; all-bound mass includes diffuse bound stars that JWST photometry at z≈5 does not capture. The all-bound choice is therefore an *upper* bracket, not a demonstrated match — the defensible statement is that the required shift spans **0.20–0.28 dex across footings**, with the served draft adopting the footing most favorable to its conclusion. At z≈5 compactness makes the bracket narrow (+0.13 dex), so the direction of the conclusion survives, but the single-number "0.20 dex" presentation hides a footing choice.
- No mock photometry, no forward-modeled scatter/Eddington treatment on the TNG side, no central/satellite separation (which also mildly biases the Sheth–Tormen distinct-halo abundance match in the ε benchmark), box variance beyond Poisson not propagated. All correctly recorded by Kun (ledger CD1–CD3; `SIMULATION_COMMENSURABILITY.md`).

## 2. Numeric re-derivation — ALL CONFIRMED

Independently recomputed from first principles (box = 110.7³ = 1.357×10⁶ Mpc³):

| Quantity | Served/Kun value | Recomputed | Status |
|---|---|---|---|
| n(N=15) | 1.11e-5 | 1.106e-5 | ✓ |
| n(N=20) | 1.47e-5 | 1.474e-5 | ✓ |
| n(N=4, z=6) | 2.95e-6 | 2.949e-6 | ✓ |
| 3e-5 / n₁₅ | 2.7× | 2.713 | ✓ |
| 3e-5 / n₂₀ | 2.04× | 2.035 | ✓ |
| log(2.7)/1.58 | 0.28 dex | 0.273 | ✓ |
| log(2.04)/1.58 | 0.20 dex | 0.196 | ✓ |
| Labbé log(13.6)/1.58 | 0.72 dex | 0.717 | ✓ |
| Poisson 1/√15, 1/√20 | ±26% / ±0.10 dex | 0.258/0.224; log(1.26)=0.100 | ✓ |
| Quadrature budget | 0.55 / 0.46 / 1.30 | 0.552 / 0.464 / 1.30 | ✓ |
| ε = 10^10.5/(0.157×10¹²) | 0.20 (0.13 shifted) | 0.201 / 0.127 | ✓ |
| ε=1 breach threshold | +0.70 dex | 0.696 | ✓ |
| z=5.5 interpolation | 6.6e-6 → 0.42 dex | 6.585e-6 → 0.417 | ✓ |
| Table 2 grid (2×/2.04×/13.6×/20× at s=1.4–2.0) | as printed | all 16 entries match | ✓ |

The arithmetic layer of both Kun's reconciliation and Goru's cross-review is fully corroborated.

## 3. Explicit cumulative `n(>Mstar)` support — PRESERVE `FAIL`

Confirmed from the extracted PDF: the observed anchor "≈3×10⁻⁵ Mpc⁻³ (Weibel et al. 2024)" is asserted without any table/figure/row citation carrying threshold, selection, completeness, scatter, Poisson, and cosmic-variance fields. Weibel et al. 2024 is a differential SMF/Schechter paper by role; no primary cumulative row is pinned anywhere in the served draft or in this packet. Goru's count (0 explicit observed cumulative rows; 3 simulation rows; 3 indirect rows) matches my own reading of `CUMULATIVE_DENSITY_LEDGER.csv` and the PDF. **Kun's `FAIL` on primary-source support is preserved unchanged.** This remains the blocker for revision-readiness.

## 4. Population separation — PRESERVE `PARTIAL`

- Landed: the prose keeps three populations distinct — Weibel total rest-optical-selected (headline, z≈5), Labbé photometric candidates (z≈7–9, labeled "outside the realistic budget and marginal"), spectroscopic quiescent z>6 (labeled genuine residual, not resolved). This separation is real in the pinned artifact.
- Not landed: Table 1 mixes object classes, redshifts, and SED classes across axes (LRD hosts, outshining samples, model-specific IMF experiments); the #5 population-averaged 0.2 dex rests on an *asserted*, not measured, LRD fraction for the Weibel anchor sample; UV-red vs UV-blue is never propagated as a separate comparison population; centrals/satellites unseparated throughout. All as Kun recorded.

## 5. 0.28 vs 0.20 dex state assignment — CONFIRM, `PARTLY_LANDED` preserved

Confirmed as two distinct, internally consistent states:

- **0.28 dex** ↔ 2×R_half aperture (`SubhaloMassInRadType`), N=15, n=1.11e-5, 2.7× — now legitimately present only as the labeled raw-aperture parenthetical in §3 and (illegitimately) in the Figure 1 arrow.
- **0.20 dex** ↔ all-bound (`SubhaloMassType`), N=20, n=1.47e-5, 2.04× — abstract, results, §3.2, Figure 1 caption, conclusion.

The revision-history claim ("0.28→0.20, result strengthens") matches the artifact except for the figure defect below. Kun's `PARTLY_LANDED` is exactly right and is preserved.

## 6. Residual figure label — CONFIRMED REAL (independent method)

Kun verified by visual render; I verified independently from the embedded text layer of the sha-pinned PDF: page 3 contains the annotation string `erased by 0.28 dex M⋆` inside the Figure 1 plot area, while the caption of the same figure says "erased by a 0.20 dex downward stellar-mass shift." The served review log explains the mechanism: the figure was authored in the Cycle-2 / 0.28-era and the regeneration did not rebuild the arrow annotation. This is a live representation defect on the public artifact; preserved as a failed partial finding.

**New minor finding (not flagged by Kun or Goru):** the Figure 1 legend labels the observed anchor `Weibel+2024 (z≈5–6)`, while §3.2 of the same draft explicitly argues a "z≈5–6" label is unsafe and pins the comparison to z=5. The legend therefore reintroduces exactly the ambiguity §3.2 disclaims. Same class of defect as the stale arrow; should be fixed in the same figure regeneration.

## 7. Systematic budget: covariance / individual maxima — PRESERVE, with a directionality sharpening

Kun's and Goru's flags are confirmed: #2–#4 are one SED-fitting degeneracy, #6 is partly derived from #1–#4, #5's population average rests on per-object maxima plus an asserted fraction, and the 1.30 dex linear sum is an upper bound only.

**Sharpening (new emphasis):** the draft calls 0.46–0.55 dex a "hostile accounting," but the covariance inflation runs *in the draft's favor* — treating covarying axes as independent enlarges the quadrature budget, and a larger budget makes "within budget" easier. A genuinely hostile, correlation-aware budget is *smaller* (plausibly ~0.3–0.4 dex if #2–#4 collapse to one axis and #6 is partially absorbed). Consequences:

- The z=5 headline (0.20 dex required) survives even a deflated budget — the conclusion's direction is robust at z=5.
- The z≈5.5 caveat (0.42 dex required, "still within the 0.46–0.55 dex committed budget") **does not survive a deflated budget**. The served draft's claim that the z=5.5 case remains within budget is conditional on the inflated quadrature and should be treated as marginal, not covered.

## 8. Source identities / versions — CONFIRM Kun's `PARTIAL`

- Weibel et al. 2024, MNRAS 533, 1808, DOI `10.1093/mnras/stae1891`; Labbé et al. 2023, Nature 616, 266, DOI `10.1038/s41586-023-05786-2`; Boylan-Kolchin 2023, NatAs 7, 731, DOI `10.1038/s41550-023-01937-7`; Nelson et al. 2019, ComAC 6, 2; Adams et al. 2023, MNRAS 518, 4755; Grazian et al. 2015, A&A 575, A96 — all consistent with the identities Kun pinned; no cross-wiring found.
- The 2025–2026 budget references (Harvey 2025; Cochrane 2025; Kocevski 2025; Choe 2026; Zhuang 2026) plus Lapi 2024 / Steinhardt 2023 remain **version-unverified in this packet**; Kun correctly declined to promote them and that status is preserved.
- Public artifact identity chain (local file = lane snapshot = baseline public fetch) is closed and hash-consistent.
- Observation, no state change: `served-review.md` footer says "Human feedback: not captured," while `served-history.json` has `humanFeedback.captured: true` with two human-direction entries. These record different things (scientific review vs. commissioning/revision directions) but read as contradictory side-by-side; worth a one-line clarification whenever the artifact set is next regenerated.

## 9. Is Kun's proposed narrow wording still too strong? — SLIGHTLY, two patches required

Kun's replacement wording is correctly conditional ("claimed Weibel cumulative density," "suggests, but does not by itself prove") and its prohibitions (no z≈7–9 resolution claim, no quiescent resolution claim, no baryon-ceiling-as-native-TNG-efficiency, no maxima-into-budget) are all confirmed necessary. Two residual overstrengths:

1. **Footing presupposition.** "…once mass-systematic and aperture uncertainties are included" presumes the all-bound footing is the matched one. Patch: state the required shift as **0.20–0.28 dex depending on the simulation mass footing (all-bound vs 2×R_half)**, noting the all-bound end is an upper bracket for what SED photometry measures.
2. **Redshift-anchor sensitivity omitted.** "z~5" hides that the requirement roughly doubles (≈0.42 dex) at an effective comparison redshift of 5.5, where coverage depends on the inflated quadrature budget (Section 7). Patch: pin the wording to **z = 5 exactly** and append: "at an effective comparison redshift of z≈5.5 the required shift rises to ≈0.4 dex and is at best marginally covered."

With those two patches, Kun's wording is defensible as the maximum claim this artifact supports.

## 10. Cross-check against Goru's cross-review

No conflicts. Goru's arithmetic, row counts (0/3/3), population-mixing finding, and flags all reproduce in this lane. Goru's `PASS` is scoped to mechanical validity of Kun's audit and is compatible with this scientific-scope result.

## 11. Disposition

**`PASS_WITH_PATCHES`** — Kun's primary audit is confirmed on all seven dimensions and its overall `PARTIAL__CLAIMS_REQUIRE_NARROWING` disposition, the primary-source-support **FAIL** blocker, and the `PARTLY_LANDED` figure state are **preserved unchanged**. Patches are additive only:

- P-1: extend Kun's narrow wording with the 0.20–0.28 dex footing bracket (§9.1).
- P-2: pin the wording to z=5 and add the z≈5.5 marginality sentence (§9.2).
- P-3: new minor figure finding — the `Weibel+2024 (z≈5–6)` legend label contradicts §3.2's own redshift-pinning argument; fix alongside the stale 0.28 dex arrow (§6).
- P-4: reclassify the served draft's "hostile accounting" framing: covariance inflation favors the draft, and the z≈5.5 "still within budget" claim must be demoted to marginal (§7).

No manuscript, project source, public route, DB, wiki, Lab record, cockpit, service, or Git state was modified. Kun's and Goru's outputs were read only.

Marker: `P1_LANA_CROSSREVIEW_COMPLETE_20260727`

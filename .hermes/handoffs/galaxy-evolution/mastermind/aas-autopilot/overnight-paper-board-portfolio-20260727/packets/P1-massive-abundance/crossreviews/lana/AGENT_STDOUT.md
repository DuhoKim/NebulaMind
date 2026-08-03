P1 Lana cross-review is complete. All three deliverables are written in the lane directory with marker `P1_LANA_CROSSREVIEW_COMPLETE_20260727`, disposition **PASS_WITH_PATCHES**.

**TLDR:** Kun's primary audit is confirmed on all seven dimensions. Every blocker and partial state is preserved unchanged — the overall `PARTIAL__CLAIMS_REQUIRE_NARROWING`, the primary-source-support **FAIL** (no pinned Weibel cumulative `n(>10^10.5)` row behind the asserted 3×10⁻⁵), and the `PARTLY_LANDED` figure state. Custody is closed: all 24 manifest hashes re-verified, and the local snapshot, baseline public fetch, and board card all resolve to the same PDF bytes.

What I verified independently:

- **Every headline number reproduces** from first principles: N=15/20/4 counts → densities, the 2.7×/2.04× excesses, the 0.273/0.196 dex shifts, the 0.55/0.46/1.30 dex budgets, ε=0.20 and the +0.70 dex breach threshold, the z=5.5 → 0.42 dex caveat, and all 16 Table 2 entries. Goru's arithmetic checks also hold; no conflict with the mechanical cross-review.
- **The stale figure label is real** — I confirmed it by a different method than Kun (embedded text layer of the sha-pinned PDF rather than a visual render): the Figure 1 arrow still says "erased by 0.28 dex" while its own caption says 0.20 dex. The 0.28↔2R_half/N=15 and 0.20↔all-bound/N=20 state assignment is exactly right.

What I added beyond confirmation (the patches):

1. **Footing bracket** — the "total-mass footing" (all-bound `SubhaloMassType`) is an upper bracket for what SED photometry measures, not a demonstrated match; the honest required shift is 0.20–0.28 dex across footings, and the draft chose the favorable end. Kun's narrow wording should carry that bracket.
2. **z=5.5 marginality** — the budget's covariance inflation actually works *in the draft's favor* (a bigger budget makes "within budget" easier). The z=5 headline survives even a deflated correlation-aware budget, but the draft's claim that the z≈5.5 case (0.42 dex) is "still within budget" depends on the inflated quadrature and must be demoted to marginal. Kun's wording should pin z=5 exactly.
3. **New minor figure finding** neither reviewer flagged: the Figure 1 legend says "Weibel+2024 (z≈5–6)" — the exact ambiguity the draft's own §3.2 argues is unsafe. It should be fixed in the same regeneration as the stale arrow.

Nothing outside the lane directory was touched; Kun's and Goru's outputs were read-only, and stop files were checked at start, mid-run, and before the receipt (none present).

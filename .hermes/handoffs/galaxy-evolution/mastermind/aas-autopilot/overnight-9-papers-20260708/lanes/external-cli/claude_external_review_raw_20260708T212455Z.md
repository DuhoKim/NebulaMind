I've read all three manuscripts and both context files. All cited files exist. Below is my read-only review. I verified the internal arithmetic where possible (all selection-count retentions, the Δf subtractions, and — notably — the M3 P3 cell counts sum to exactly 60,000).

---

## Overall verdict

These are unusually disciplined pilot drafts: each one demotes its parent proposal's causal claim to a clearly-labeled *selection-disclosed optical denominator/target vector*, front-loads a public-vs-cached count table, and reproduces cleanly against the shared selection module. The dominant remaining risk is **not** overclaiming in the title/abstract (that has been well-contained) but rather that the **headline fractions themselves — f_BPT_AGN and f_Q — are strongly shaped by the four-line S/N≥3 emission requirement**, and this feedback loop is disclosed only qualitatively ("biased against weak-line systems") rather than being named as the direct cause of the numbers readers will quote. Second-order: the "capped by SpecObjID order" subset is asserted but never shown to be representative, and no cosmology/aperture controls are stated. None of these block a pilot-grade internal deliverable; all block a public/AAS submission.

---

## M2 P2 — radio-jet environment denominator

**Strongest element:** The insensitivity framing is exactly right — reporting Δf_AGN = 0.138/0.142/0.152 across k=5/10/20 as "insensitive to the tested neighbour-count choice, not physically scale-robust" is a precise, defensible sentence. Selection Table 1 is internally consistent (49.9%, 24.0%, 41.6%, 26.2% all check out).

**Blocker/major issues:**
- **Nearest-neighbour density is computed in redshift space with no stated cosmology and no edge correction.** "Approximate comoving Cartesian positions" (§methods) needs H₀/Ω_m stated, and redshift-space fingers-of-god inflate k-NN distances *precisely in the dense regions being studied*, plus survey-boundary galaxies have biased NN counts. This directly affects the one number the paper reports.
- **No control for z or M⋆ gradients across density quartiles.** Only ~4,600 of 9,298 massive hosts fall in the extreme quartiles; if the high-density quartile sits at different mean redshift, the SDSS 3″ fiber aperture bias alone can manufacture a BPT-AGN fraction difference. Δf_AGN is presented as a result, so this confound must be closed or disclosed.

**Overclaim risks:** Low and well-guarded. The "does not establish jet power / hot-gas coupling / causal feedback" disclaimers are in the abstract, results, and discussion.

**Reproducibility gaps:** Cosmology unstated; bootstrap CIs are explicitly "inherited from the Goru robustness table" and flagged as needing recompute (good that it's flagged, but they are currently un-recomputed); density-code path not cited beyond the run ID.

**Next 2–3 steps:** (1) State cosmology and recompute k-NN density with a random-catalog edge/boundary correction, or add an explicit redshift-space caveat. (2) Show the z- and M⋆-distributions of the low vs high quartiles (a two-line table) to demonstrate the contrast is not a redshift/aperture artifact. (3) Recompute the bootstrap CIs against this sample rather than inheriting them.

---

## M3 P2 — gas-depletion vs efficiency denominator

**Strongest element:** The title-level reframing to "emission-line denominator for molecular-gas follow-up" plus the explicit unsafe/safe wording box (§discussion) is the best overclaim-control in the set. The sSFR-dependent retention contrast (33.6% vs 94.9%) is correctly carried over from the shared module.

**Blocker/major issues:**
- **The f_BPT_AGN column trends (0.509→0.649 as the sSFR cut tightens) are a near-direct artifact of the emission-line requirement, and the manuscript never says so.** Requiring four strong lines in low-sSFR hosts preferentially admits LINER/AGN-like emission, because star-forming emission has been suppressed by construction. A reader will quote "≈50–65% of massive quenched galaxies are optical AGN"; that is the selection talking, not an intrinsic AGN excess. The paper discloses the *direction* of the bias ("biased against weak-line quiescent systems") but must explicitly attribute the rising f_AGN to it.

**Overclaim risks:** Contained at the title/abstract level; the residual risk is entirely in Table 2's AGN-fraction column being read as physical.

**Reproducibility gaps:** median log L_Hα given without units (erg s⁻¹ presumably) and with no aperture/extinction-correction statement; uncertainties are binomial only (no selection bootstrap), which is fine for a pilot if labeled as such.

**Next 2–3 steps:** (1) Add one sentence + a caption clause stating that f_BPT_AGN rises with sSFR-strictness *because* the four-line cut removes weak-line quiescent systems — i.e., it is a selection-convolved fraction, not an AGN-incidence measurement. (2) State L_Hα units and whether it is aperture/extinction-corrected. (3) When CO/dust data arrive, the promised gas-fraction-vs-SFE comparison should be pre-registered at fixed mass/morphology/environment (already correctly deferred).

---

## M3 P3 — SDSS target vector for forward validation

**Strongest element:** Cleanly the most rigorous of the three on scope. The N<500 flag column is carried in the table rather than buried in prose, the min-N caveats propagate to abstract/caption/discussion, and — I verified — the 15 cell N's sum to exactly 60,000, and both small-cell coverage ratios (24.0%, 25.1%) check out.

**Blocker/major issues:**
- **f_Q here is the quenched fraction *among emission-line-detected galaxies*, which excludes the truly passive (line-free) population entirely — so f_Q = 0.856 in the top cell is not a quenched fraction any simulation would natively produce.** This is the single most important caveat for a "validation vector," and it is only implicit. A mock must apply the four-line S/N≥3 cut *before* computing f_Q, or the comparison is meaningless — and the paper should say that the *shape* of the vector (not just its amplitude) is selection-defined.

**Overclaim risks:** Low. The unsafe-wording list ("validates a feedback model," "proves AGN feedback," "would falsify a simulation") is explicit and correct.

**Reproducibility gaps:** Goru definitions are "recovered from the analysis code" rather than cited to a fixed script/commit; the preserved figure is reinterpreted by caption but its content is unverified against the new meaning (see cross-paper #3).

**Next 2–3 steps:** (1) Add an explicit line: f_Q, f_AGN, and f_high-exc are all conditioned on four-line detection, so mocks must reproduce that selection before comparison — the vector's shape is selection-defined, not physical. (2) Pin the Goru fraction definitions to a script path + commit hash. (3) For the two N<500 cells, report the binomial CI in the table itself so their extrema (0.856, 0.610) are visibly uncertain, not just flagged.

---

## Cross-paper priorities (ranked)

1. **Name the emission-line selection feedback explicitly in M3 P2 and M3 P3.** The four-line S/N≥3 cut inflates f_BPT_AGN and distorts f_Q in exactly the massive/low-sSFR bins these papers headline. Disclosing the *direction* is not enough; state that it *causes* the reported numbers. Highest scientific-integrity payoff, lowest effort.
2. **Justify or bound the SpecObjID row-cap.** All three lean on the same 60,000-row 24%-coverage subset "capped by SpecObjID order." SpecObjID ≈ plate-MJD-fiber, so that ordering is spatially/temporally clustered, not random. One representativeness check (compare cached vs public marginal distributions in z, M⋆, sSFR) would protect every paper at once — a natural addition to the shared selection module.
3. **Close M2 P2's density-method gaps** (cosmology, redshift-space/edge effects, z–M⋆ balance across quartiles), since it is the only paper reporting a *contrast* as its result rather than a denominator vector.
4. **Integrate the Wave-2 citations under their placement guards.** All three still carry only the 4 generic bibitems (BPT/Kauffmann/Kewley/York); the vetted method-anchor vs future-data classification is ready and unused. Mechanical but needed for AAS quality.
5. **Verify each preserved `figure1.pdf` actually depicts what its rewritten caption now claims.** The captions reinterpret batch figures I was not asked to (and did not) open; a caption/figure mismatch is a silent correctness risk before any public compile.

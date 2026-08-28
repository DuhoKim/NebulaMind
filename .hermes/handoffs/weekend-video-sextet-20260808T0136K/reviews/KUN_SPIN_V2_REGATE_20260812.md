# KUN SPIN DESIGN BRIEF V2 REGATE

Timestamp: 2026-08-12 KST

Target: `reviews/LANA_SPIN_DESIGN_BRIEF_V2_20260812.md`

Prior gates:

- `reviews/KUN_SPIN_DESIGN_BRIEF_GATE_20260812.md`
- `spike/KUN_SPIKE_RECEIPTS_GATE_20260812.md`

## Verdict

PASS FOR PREREGISTRATION DRAFTING.

No sky run is authorized. No result is authorized. No publication or accepted status is authorized.

V2 correctly narrows the question from the V1 class-floor design to Longo's specific amplitude at Longo's axis. It is now within the feasible sample-size regime that Goru's power curve allowed, provided the final preregistration uses `N >= 100,000` accepted spirals and recomputes power at the measured attenuation.

The main remaining work is preregistration hardening, not another design-level block.

## 1. Claim Boundary

PASS IN SUBSTANCE; ONE WORDING REPAIR REQUIRED BEFORE ANY DERIVED ARTIFACT.

Section 0 states the boundary strongly:

- V2 tests Longo 2011, not the spin-anisotropy class.
- A null at `A ~ 0.04` does not exclude `A = 0.02`.
- A `REJECTED` outcome rules out Longo's published amplitude at his axis and leaves smaller claimed amplitudes untested.
- Reading a null as "the sky is isotropic" is over-reading.

Section 6 carries the same boundary:

- `REJECTED-AT-LONGO-AMPLITUDE` does not exclude `A = 0.02`;
- it does not adjudicate Shamir;
- it does not establish that the sky is isotropic;
- expected reach leaves everything below roughly `Â_c ~= 0.021` alive.

The boundary is strong enough for a reader not to confuse this with a global isotropy result, provided the title/headline of any later artifact says "Longo-amplitude test" rather than "spin anisotropy test."

However, §0 says the warning sentence appears "verbatim" in §6. It does not. §6 uses equivalent wording, not verbatim wording. This is not an overclaim about the science, but it is a custody/sloppiness issue in exactly the kind of boundary language that later gets copied. Repair before any derived artifact:

> A null here does not establish that the sky is isotropic; it rejects only Longo's published amplitude at Longo's published axis if the preregistered rejection rule is met.

Put that exact sentence in §0 and §6, or delete the word "verbatim."

## 2. Re-Derived Decision Region

PASS FOR DESIGN; FREEZE STILL NEEDS FINAL NUMBERS.

The signed reproduction condition is correct. Longo's reported amplitude is signed relative to a stated axis orientation. A dipole with the same magnitude and the opposite sign at the same oriented axis is not a reproduction; it is the opposite dipole. Requiring Longo's sign at Longo's axis is both physically and statistically right.

The sigma arithmetic is materially right:

- V2 uses `Â = 3D`, consistent with Goru's spherical-uniform result that `D = A/3`.
- With `N = 100,000` and `a = 0.9`, `sigma_ours = sqrt(3/N)/(2a-1) ~= 0.00685`.
- Combining with Longo's `sigma_pub = 0.011` gives `sigma_comb ~= sqrt(0.011^2 + 0.00685^2) ~= 0.01296`.
- `0.0408 +/- 3*sigma_comb` gives approximately `[0.0019, 0.0797]`, matching V2's stated `~[0.002,0.080]`.
- The expected null `3sigma` corrected upper limit is `3*0.00685 ~= 0.0206`, matching the stated `~0.021`.

One interpretive weakness: the `REPRODUCED-LONGO` amplitude band is very broad at the low end because it combines Longo's published uncertainty with ours. V2 correctly notes that `p < 0.001` does the low-end excluding work. For freeze, state the effective detection floor implied by `p < 0.001` and the final `sigma_ours`, so a tiny positive amplitude cannot visually look like a reproduction merely because it falls inside the broad combined band.

## 3. Covariate Battery

SUBSTANTIALLY IMPROVED; NOT YET FREEZE-CLOSED.

This is no longer an outline wearing a table. V2 now has sources, forms, model layers, thresholds, multiple-testing handling, and exact `INCONCLUSIVE` triggers in design form.

Closed at design level:

- covariate families are named;
- several executable sources are named;
- redshift is explicitly dropped unless public photo-z exists;
- deblend flags are not hand-waved and must bind per survey or be dropped;
- Layer A has decile stratified permutation and a joint PCA version;
- Layer B has logistic regression and gradient-boosted trees;
- AUC thresholds are specified;
- Layer C has an abstention/sensitivity coupling bound;
- Holm-Bonferroni correction is specified;
- `INCONCLUSIVE` triggers are stated.

Still missing before preregistration freeze:

1. Exact survey-bound product identifiers and versions for depth, PSF, shape, photometry, catalogue, and flags.
2. HEALPix ordering, coordinate frame, interpolation/missing-pixel policy, and edge handling.
3. Exact standardization and missing-value handling for per-object covariates.
4. Exact decile construction rules for tied values and sparse bins.
5. Exact PCA procedure and the "coarsened by a frozen rule" details. That phrase still hides discretion.
6. Exact logistic-regression implementation: penalty or no penalty, solver, convergence tolerance, class weights, feature scaling, and treatment of squared terms.
7. Exact gradient-boosted-tree implementation and hyperparameters. "Fixed hyperparameters" is not enough unless they are listed.
8. Exact definition of `sigma_D` used in `0.25*sigma_D` and `0.5*sigma_D` leakage thresholds.
9. Exact construction of the sensitivity and abstention sky maps used in the coupling bound.
10. Whether Holm correction applies before or after the hard absolute thresholds in Layer A. The text gives both; freeze should state the order of operations.

So the covariate blocker is not fully closed. It is now close enough to authorize preregistration drafting, because the missing pieces are executable-detail fill-ins rather than conceptual gaps.

## 4. Seven Freeze Conditions From The Spike Gate

1. **Exact covariate battery:** PARTLY CLOSED. V2 closes the structure and triggers. Artifact needed to close: survey-bound covariate spec with exact products, versions, maps, model implementations, hyperparameters, and missing-data rules.

2. **Survey route and scale:** PARTLY CLOSED. V2 reports DESI Legacy, SDSS, and HSC clearing `N >= 100,000` in Goru's narrowed feasibility chain, but survey binding is still open. Artifact needed: Tori custody receipt plus Goru accepted-yield receipt for the chosen route.

3. **Production estimator freeze:** OPEN. V2 changes the primary instrument to a synthetic-trained equivariant classifier and demotes deterministic geometry to secondary. That is allowed by my rule only if the synthetic training generator, architecture, weights freeze policy, acceptance threshold, and mirror receipts are frozen before sky data. Artifact needed: production-estimator prereg appendix and identity/acceptance receipts.

4. **Hand-check attenuation protocol:** PARTLY CLOSED. V2 keeps the protocol outline and requires final numeric propagation. Artifact needed: exact hand-check protocol with strata, sample size, adjudication, uncertainty formula, and power rerun at `A_eff = (2a-1)*0.0408`.

5. **No-resampling mirror rule:** CLOSED AT DESIGN LEVEL. V2 includes the pure index-reversal rule and byte-exact `mirror(mirror(x))` test. Artifact needed at freeze: unit test receipt against the exact analysis raster and dtype.

6. **Signed-zero rule:** CLOSED AT DESIGN LEVEL. V2 includes value comparisons only and a failing unit test for sign-bit semantics. Artifact needed at freeze: code test receipt.

7. **Distortion policy:** CLOSED AT DESIGN LEVEL; SURVEY-BINDING OPEN. V2 adopts fail-closed on distortion keywords or a tested local Jacobian receipt. Artifact needed: chosen survey route declares which branch applies and supplies the corresponding receipt.

## Plain Verdict For Duho

Preregistration drafting is authorized under my prior ruling.

Authorized now:

> Draft the sha-pinned preregistration for the narrowed Longo-amplitude design, filling the exact executable details named above.

Still not authorized:

- no real sky statistic;
- no survey-label or galaxy-handedness run;
- no publication;
- no accepted status;
- no BHU interpretation;
- no claim about global isotropy;
- no decision language about Shamir.

The narrowed design is honest if it keeps this headline:

> This tests Longo's published `A ~= 0.0408` amplitude at Longo's published axis. It does not test `A ~= 0.02`, Shamir, BHU, or whether the sky is isotropic.

If the preregistration carries that boundary, fixes the remaining covariate and estimator details, and binds a survey route with `N >= 100,000` accepted spirals after real acceptance/attenuation checks, it can come back for freeze gate.

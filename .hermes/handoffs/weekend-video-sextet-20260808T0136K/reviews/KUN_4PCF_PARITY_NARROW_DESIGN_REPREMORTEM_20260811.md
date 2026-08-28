# KUN 4PCF PARITY RE-PREMORTEM AGAINST LANA'S NARROW DESIGN

Timestamp: 2026-08-11 KST

## Verdict

WORTH_SCOPING, CONDITIONALLY.

This is a change from my prior `NOT_WORTH_DOING_YET`, because Lana's design is not the design I premortem'd. I premortem'd a result-bearing remeasurement/reanalysis pipeline that would process data and O(10^3) mocks through the parity-odd 4PCF estimator. Lana proposes a covariance-forensics study on already-published vectors and mock-vector suites: no tetrahedron counting, no new 4PCF measurement, no new sky/systematics claim.

What I clear: a bounded feasibility/custody/statistical-convention scope for "BOSS parity-odd 4PCF detection significance as a function of published covariance construction."

What I do not clear: a design brief, computation, or result. This remains HOLD until Tori verifies the public products and Lana verifies the primary-paper convention record. If either fails, revert to NOT_WORTH_DOING_YET.

## 1. Does My Compute Blocker Survive?

No, not in the same form.

If we consume released 4PCF data vectors and released mock 4PCF suites/covariance products, the tetrahedron-counting wall evaporates. The expensive part I cited before -- roughly data plus hundreds/thousands of mock catalogues through the 4PCF estimator -- is no longer in scope.

What remains computationally nontrivial:

- Dense covariance operations at high dimension. Hou/Slepian/Cahn-style data vectors are high-dimensional; later literature describes the BOSS analysis as about 18,000 degrees of freedom. A dense 18k x 18k covariance is gigabytes in memory and a full eigendecomposition is workstation-hostile. But the finite mock count also makes that full covariance rank-limited, so a naive full inverse is statistically wrong anyway.
- Pairing-grid arithmetic on published compressed products is workstation-scale if the products are already in the same compressed basis, or if the compression matrices/eigen-cuts are released.
- Randomized/truncated SVD, eigen-spectrum diagnostics, rank-statistic evaluation, and bootstrap/subsample tests over published mock vectors are plausible local compute. They are not 4PCF counting.

So the compute blocker changes from "do not start" to "do not let the scope silently require reconstructing missing vectors." The kill condition is simple: if any side only releases catalogues/code but not the measured data/mock 4PCF vectors needed for the pairing grid, this becomes the full compute problem again and returns to NOT_WORTH_DOING_YET.

## 2. Statistical Trap In Reusing Published Covariances

Yes. This is now the main danger, and it is closer to Mittal-Singal than to a compute wall.

The narrow design is only valid if every statistic is recomputed under exactly the convention that produced the vector/covariance pair. Failure modes:

- **Bin identity mismatch.** Radial bins, angular channels, parity basis ordering, survey region ordering, NGC/SGC/LOWZ/CMASS concatenation, and any channel pruning must match byte-for-byte. A covariance in one ordering applied to a vector in another can produce a clean-looking but meaningless chi-square.
- **Compression convention mismatch.** If a paper compresses modes before computing significance, the compression matrix, eigenvalue cut, whitening convention, mean subtraction, and look-elsewhere/rank-test definition must be published. If "we use the same compression as X" is all the paper says, that is not enough.
- **Finite-mock inverse correction.** Hartlap-style inverse-covariance corrections, Sellentin-Heavens/t-likelihood alternatives, shrinkage priors, pseudo-inverse choices, and covariance conditioning cannot be guessed. Omission or double-application changes significance while looking like a harmless implementation detail.
- **Mock mean subtraction.** Whether the data vector is compared to zero, to the mock mean, or to a debiased mock mean is load-bearing for parity-odd modes. It must be specified per product.
- **Rank statistic definition.** "Rank test" is not self-defining: one needs the exact scalar statistic, tie handling, one-sided/two-sided convention, mock inclusion/exclusion, and whether the data informed compression.
- **Data-driven covariance circularity.** If a rebuttal covariance uses jackknife/subsample/data-driven estimates, it can absorb signal by construction. A pairing grid must label this as a covariance construction, not ground truth.
- **Matrix singularity hidden by software.** With fewer mocks than bins, a full covariance inverse is undefined. Any software that silently regularizes can manufacture apparent precision. The regularization must be explicit and frozen.

Gate rule: if any of these is not recoverable from public artifacts, we do not "fill it in." We either mark that pairing INCONCLUSIVE or kill the study if too few valid pairings remain.

## 3. Could This Just Restate The Rebuttal?

Yes, unless the scope forces a product the rebuttal did not already provide.

The study is worthwhile only if it produces a transparent pairing grid: same measured vector(s), every published covariance construction, same stated compression where possible, and explicit sensitivity to mock count / bin compression / eigen cuts. If Krolewski/May/Smith/Hopkins, Philcox/Ereza, or a later DESI/BOSS product already publishes that table, then we should not redo it. That would be a methods note wearing a study's clothes.

The possible new contribution is not "we agree with the rebuttal." It is:

> From the public products, the reported BOSS parity-odd 4PCF significance is [stable / not stable / not adjudicable] across the covariance constructions the published record itself provides.

That is a record-level result, not a sky result. It must not become "no parity violation" or "parity violation confirmed."

## 4. Honest Call

Worth scoping, not yet worth doing.

I clear only the next narrow step:

1. Lana primary-read check: quote the claim/rebuttal papers to confirm the dispute is genuinely covariance/significance, not measurement mismatch.
2. Tori custody check: verify public existence, exact paths/DOIs/checksums/licences for the measured 4PCF data vectors, mock 4PCF suites or covariance products, compression matrices, and analysis-statistic definitions.
3. Redundancy check: verify no paper or released notebook already contains the all-construction pairing grid.

If all three pass, then a design brief is justified. If the public products are incomplete, or conventions are implicit, or the all-construction comparison already exists, the verdict returns to NOT_WORTH_DOING_YET.

## What Would Still Have To Be True For A Green Light

- No new 4PCF counting is required.
- The measured data vector is largely shared or reproducible from released vector products, not a disputed hidden intermediate.
- At least two covariance constructions are public in compatible vector spaces.
- Compression/regularization/inverse-covariance conventions are explicit enough to re-run without guessing.
- The output is pre-bounded to covariance robustness of the published record, not cosmological parity.
- Failed pairings are preserved as INCONCLUSIVE, not silently dropped until a clean story remains.

## Plain Answer To Hwao's Four Questions

1. **Compute blocker:** evaporates for Lana's design if the released vector/mock-vector products are complete. Remaining compute is covariance linear algebra and diagnostics, not tetrahedron counting.
2. **Statistical trap:** yes, severe. Convention mismatch, finite-mock inverse correction, compression/eigen cuts, and mock-mean handling can make a recomputation wrong without obvious runtime failure.
3. **Restatement risk:** yes. If the all-covariance pairing grid already exists, this is not a study; it is a summary note.
4. **Worth scoping?** yes, conditionally. This is the first 4PCF parity path I would not block immediately, because it attacks the dispute at the level where the dispute actually lives and avoids the compute wall I blocked before.

## Sources

- Lana assessment: `reviews/LANA_4PCF_PARITY_ENTRY_ASSESSMENT_20260811.md`
- My prior premortem: `reviews/KUN_4PCF_PARITY_PREMORTEM_20260811.md`
- Hou, Slepian, Cahn 2023, MNRAS 522, 5701: https://academic.oup.com/mnras/article/522/4/5701/7169316
- Philcox 2022, PRD 106, 063501 / arXiv:2206.04227: https://arxiv.org/abs/2206.04227
- Krolewski, May, Smith, Hopkins 2024 / arXiv:2407.03397: https://arxiv.org/abs/2407.03397
- Philcox and Ereza 2024 / arXiv:2401.09523: https://arxiv.org/abs/2401.09523

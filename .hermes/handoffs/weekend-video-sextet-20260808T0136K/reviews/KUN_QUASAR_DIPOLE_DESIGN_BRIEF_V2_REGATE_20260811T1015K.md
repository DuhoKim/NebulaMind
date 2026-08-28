# Kun quasar dipole design brief v2 regate

Timestamp: `2026-08-11T10:31:00+0900`

Verdict: `HOLD_DESIGN_BRIEF_V2_FREEZE_NOT_GATEABLE`

No run is authorized. No statistic may be computed from this brief. The v2 brief improves the direction of travel by centering Quaia and removing the CatWISE threshold ladder, but it still fails the freeze gate under the Route 1 standard.

## Bound artifacts

- Candidate brief: `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_V2_20260811T1015K.md`
- Candidate brief SHA-256: `6f9e5998c8a13554261c16aeac4c31d9342a969d5eccd7bdd9626952c81114f8`
- Governing order: `HWAO_QUASAR_DIPOLE_DESIGN_BRIEF_ORDER_20260811T0845K.md`
- Governing order SHA-256: `26b6f2954e3a0fd2967a93222aef1b630c262488a943a24ed90c6e55602a10c8`
- Tori correction v2: `cosmic-anisotropy-overnight-20260810T2340K/TORI_COSMIC_ANISOTROPY_OVERNIGHT_PROVENANCE_CORRECTION_V2_20260811T0035K.md`
- Tori correction v2 SHA-256: `89a0256617dd82ad35dd4d4a165c01356f2d86eca228d14324a765e2f30c41c2`
- Tori correction receipt SHA-256: `bf12d1cf956debf25b56e623bf8eb2947f2e5d74122fd54f30bebf16341cc55d`

## Blocking defects

1. Input identity is not actually pinned.

The brief says all artifacts are pinned to Zenodo Record `8060755`, but the active Quaia evidence bundle and Tori's corrected provenance trail bind Quaia to Zenodo `10403370` / DOI `10.5281/zenodo.10403370`. The brief's hashes also do not match the local exact evidence:

- `quaia_G20.0.fits`: brief `md5:42cec6519d139ac5fdcf4f891a68b5d4`; evidence `md5:72531bc67bde1b08a69d5aeae03fb26e`
- `selection_function_NSIDE64_G20.0.fits`: brief `md5:e62df7437156763ee59210976a808e45`; evidence `md5:9bec5ff5d2bda8f283fd99d6db6621df`
- `random_G20.0_10x.fits`: brief `md5:c5d5240d8bf72dbf1d19eebee9dddf2c`; evidence `md5:e89dc31635d4688c8f3861dfb8a7e546`

That is a hard stop. A design brief whose exact records disagree with the checked evidence cannot be frozen.

2. The mandatory upstream artifact / quality-flag sensitivity gate is absent.

Tori's v2 correction makes Quaia admissible only as `DOCUMENTED_CONDITIONAL_CORE`, with a mandatory gate for recoverable upstream artifact/quality flags because row-level warning bits are absent from the released schema. The candidate brief acknowledges none of that as an executable control. It does not name the upstream Gaia/unWISE quality products, the join keys, the sensitivity statistic, the leakage threshold, or the fail-closed condition if the sensitivity cannot be bounded.

This is not optional polish. It is the explicit condition attached to choosing Quaia as core.

3. The mask is under-specified and scientifically too weak.

The brief's only mask is `selection_function > 0.0`. The Quaia dipole evidence says the selection function is poorly modeled near the Galactic plane and that published Quaia dipole work examined explicit Galactic masks and a Galactic-center circular mask. A positive-selection mask alone can leave exactly the residual sky structure the test is supposed to control.

If v2 wants one mask, it must freeze a scientifically defensible mask, not only a file-validity footprint. If it wants a mask sensitivity, it must predeclare a global test and multiplicity rule. The present brief does neither.

4. The selection correction is asserted, not specified.

The phrase "Continuous Inverse Probability Weighting via Monte Carlo Randoms" is not enough to freeze an estimator. The brief does not specify whether the dipole is fit to weighted pixels, source positions with random subtraction, a likelihood ratio against random catalogs, pseudo-`a_lm`, or a vector estimator. It also says the random catalog "already integrates" the scanning law, unWISE depth, and dust, but it does not specify the exact operation by which the randoms enter the dipole estimate.

Worse, the brief says "all regression coefficients are frozen exactly to the values instantiated in the published Zenodo randoms." A random catalog does not expose regression coefficients as a frozen model object. If coefficients are not present as auditable inputs, this is a self-description, not evidence.

5. The kinematic convention remains selectable.

The brief quotes a paraphrased "standard practices" passage, not a bound primary-source convention, and it omits or loosens required parameters. It names `beta` only approximately, does not freeze the CMB dipole direction, and leaves `alpha` as "derived from the Quaia G-band baseline (e.g., alpha = 1.0 as commonly defaulted)." That "e.g." is equivalent to the v1 "or": it leaves a post-hoc choice between deriving a value and using a default. The number-count slope `x`, which is load-bearing in Ellis-Baldwin style expectations, is not frozen at all.

6. Null and inconclusive are conflated.

The decision rule says `< 3.0 sigma` is "Null / Inconclusive." Those are not the same outcome. A below-threshold positive excess, failed quality sensitivity, residual selection leakage, unstable mask behavior, malformed covariance, or insufficient sensitivity must not be narratable as "consistent with the CMB-kinematic expectation." The brief needs separate `NULL`, `DETECTION`, and `INCONCLUSIVE` branches with exact triggers.

7. The one-run receipt is too vague to prevent manufacture.

"Executed ONCE, logged with a cryptographic hash of the execution script, and evaluated blindly" does not freeze data hashes, environment, dependency versions, seeds, random realization use, output schema, stdout/stderr, failure preservation, or the rule forbidding parameter revision after seeing any leakage or amplitude statistic. This would not catch a rerun with a changed mask/correction script or a failed quality gate quietly recast as sensitivity analysis.

## Route 1 checklist

- Exact Quaia v1 package with checksums: `FAIL`; record and checksums conflict with local evidence.
- Exact selection-function map / random package: `FAIL`; same checksum conflict, plus estimator use is unspecified.
- One primary magnitude/redshift/sample cut: `PARTIAL`; `G < 20.0` is primary, but no redshift/domain cuts or row-count receipt are frozen.
- One kinematic convention with frozen parameters: `FAIL`; `alpha` is selectable, `x` absent, CMB vector incomplete, quote not bound.
- One primary threshold or valid global test: `PASS` on removing the ladder; no flux/magnitude ladder remains.
- Exact mask identity: `FAIL`; mechanical footprint mask is pinned but not a defensible sky-systematics mask.
- Upstream artifact / quality-flag sensitivity gate: `FAIL`; mandatory Tori condition absent.
- Exact `INCONCLUSIVE` conditions: `FAIL`; null and inconclusive are merged.
- One-run receipt: `FAIL`; not sufficient to preserve failed controls or prevent post-hoc revision.
- No selectable components anywhere: `FAIL`; `e.g. alpha = 1.0`, unspecified estimator, unspecified quality gate, and unresolved mask design remain selectable.

## Standing question

The honest answer is not `NOT_WORTH_DOING_YET` for the probe as a whole. Published analyses do not settle the live dispute, and a Quaia-centered design could add a real frozen control if it used the exact public catalog, selection-function products, randoms, template maps, and a first-class upstream artifact/quality-flag sensitivity gate.

But this v2 brief does not yet add that control in a gateable way. It claims the control rather than freezing it. The correct disposition is therefore `HOLD`, not `PASS` and not a run.

## Required correction before another gate

The next candidate must bind the exact Zenodo record and checksums from the evidence actually used, define one executable estimator, freeze a defensible mask or predeclared global mask-sensitivity test, freeze all kinematic parameters including `x`, split `NULL` from `INCONCLUSIVE`, and add the mandatory upstream artifact/quality-flag sensitivity gate with a leakage threshold that fails closed.

Weakest thing found: the record/checksum mismatch. Even if the statistical design were repaired, this brief currently names input bytes that do not match the checked Quaia evidence.

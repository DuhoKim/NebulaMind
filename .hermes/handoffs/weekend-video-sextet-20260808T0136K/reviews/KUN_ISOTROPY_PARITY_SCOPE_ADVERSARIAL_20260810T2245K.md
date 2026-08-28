# KUN — Isotropy/Parity Scope Adversarial Review

Filed: 2026-08-10 23:07 KST  
Order: `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_20260810T2245K`  
Role: attack the proposed scope before any run.

## Boundary

This is a large-scale galaxy-spin isotropy/parity scope. It is not a BHU test. BHU may appear only as a labelled personal-interest footnote, or not at all. A detection would not uniquely confirm BHU, and a null would not kill it. No run, result, claim, video, publication, lane unlock, or public surface is authorized here.

## Bytes Read

- `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_20260810T2245K.md`
  - SHA-256: `681856e9b60bfb88c5d8c926a8089b930789355516c9b926f80661ca7bb01e7d`
- `reviews/LANA_BHU_NEW_DATA_SURVEY_STEP1_20260810.md`
  - SHA-256: `627ab0acdc7e592fa65a383f2a80f3c257193b3d411e53afe8bf4eb9b2b7e661`
- `reviews/KUN_BHU_NEW_DATA_SURVEY_ADVERSARIAL_20260810T2210K.md`
  - SHA-256: `6bc7df20de073dfd16767ea47624d3fbcdfae627ae9ce997399b242bf1ba2ba4`
- `bhu-new-data-survey-20260810T2210K/TORI_BHU_NEW_DATA_PROVENANCE_FEASIBILITY_GATE_20260810T2247K.md`
  - SHA-256: `2bfb1f234c019a07bbb031e232d66634ce44cadba3325a8b45991ddbf188566c`

## Verdict

Scope may proceed only if it is rewritten to state that the mirror self-test is necessary but not sufficient. The current backbone is directionally right, but it can still fail by treating mirror equivariance as a cure for inherited human bias.

If the scope cannot add a separate inherited-prior control, the honest outcome is `NOT_WORTH_DOING_YET`, not a weaker run.

## Main Attack: Mirror Self-test Does Not Kill Human-label Inheritance

The proposed self-test says: feed a classifier an image and its mirror, and require handedness output to flip exactly. That catches several real failures:

- preprocessing that changes parity silently
- a chirality head that is invariant when it should be anti-equivariant
- one-sided catalogue-column misuse
- image-display or cutout mirror bugs

But it does not by itself prove the classifier is free of inherited volunteer bias.

A model trained on human labels can learn a chirality decision rule that is perfectly anti-equivariant under image mirroring while still carrying a sky-position, survey-depth, redshift, colour, size, or morphology-dependent handedness prior inherited from volunteers or the training sample. In that case it will pass the mirror self-test on every object: original says CW, mirror says ACW. The prior can still bias which borderline objects receive confident handedness labels, and that biased selection can project onto sky statistics.

Therefore the scope must split two controls:

1. **Mirror anti-equivariance control:** does the classifier flip its label on a mirrored copy of the same cutout?
2. **Inherited-prior / selection-bias control:** does the classifier's confidence, abstention, or label assignment depend on sky-position-correlated covariates after the mirror pair is accounted for?

Without control 2, "we control the classifier" is overstated.

## Public Catalogue Trap

Tori's provenance gate makes this sharper. Galaxy Zoo DESI and DECaLS public morphology products are documented, but they are not public handedness products. Their `spiral-winding` fields mean arm tightness, not clockwise/counterclockwise chirality.

So the scope must forbid this shortcut:

> download GZ DESI/DECaLS morphology columns and interpret any winding output as handedness.

The study must instead start from public imaging and run a frozen chirality pipeline. If public weights are trained only to predict volunteer morphology answers and have no chirality output target, those weights are not enough. A public replacement classifier is permitted by the order only if frozen before sky statistics and only if no new labelling is done; that means it must use an existing public labelled chirality source or a non-learning geometric algorithm with documented failure modes. If neither exists, fail closed.

## WCS Parity Is a Single-point Catastrophic Failure

The WCS parity validation requirement is correct but under-specified. Silent failure modes:

- FITS pixel axis order can invert displayed parity relative to sky east/north.
- Cutout services can return images with different axis conventions from local FITS extraction.
- RGB composites can mix bands with resampling kernels and orientations.
- JPEG/PNG previews may not preserve the same orientation convention as science FITS.
- RA increasing left vs right can differ between display tools.
- rotation to north-up/east-left can introduce an extra reflection if implemented incorrectly.
- coadd tiles can cross camera/chip boundaries with different distortion footprints.

Required scope hardening:

- Use FITS, not screenshots or catalogue thumbnails, as the primary image source.
- Freeze one cutout generator.
- Log the 2x2 pixel-to-sky Jacobian determinant sign for every cutout.
- Validate with injected asymmetric test patterns through the same extraction and preprocessing path.
- Include a human-readable parity receipt: north/east arrows and mirror-pair visual audit for a random frozen sample before any statistic.
- Treat any parity mismatch as `INCONCLUSIVE`, not as a fixable post-hoc preprocessing bug.

## Null-control Covariates Are Incomplete

The order lists depth, seeing, Galactic latitude, instrument, and redshift. That is not enough. A null that preserves only those can still leak a false axis through:

- Galactic extinction and stellar density separately from latitude
- sky brightness and moon/airmass history
- PSF ellipticity and PSF model residuals
- deblending/crowding flags
- surface-brightness completeness
- angular size and inclination proxy
- colour and band-dependent arm contrast
- Sersic/profile type or bulge fraction
- photo-z quality or spectroscopic-targeting class
- survey tile/brick/run/camera/chip identifier
- coadd depth per band, not just scalar depth
- mask fraction, bright-star proximity, and local background
- duplicate/overlap resolution policy

The null must preserve these jointly enough that sky position cannot be reconstructed from the residuals. If the null control is too weak, a preferred-axis statistic will measure survey strategy.

## Two Instrument Families May Not Be Enough

"At least two instrument/footprint families" is a good floor, not a decisive replication rule. Two families can still share:

- the same Milky Way mask
- the same target-selection logic
- the same training labels or pretrained model
- the same cutout generator
- the same redshift catalogue
- correlated depth/extinction systematics
- a shared north/south or equatorial footprint asymmetry

The scope should say that two-family agreement is necessary for preferred-axis language, not sufficient. A stronger replication criterion is:

- independent imaging instrument/optics
- independent sky footprint with limited overlap
- independently trained or independently specified chirality estimator
- independent preprocessing/cutout implementation
- same pre-registered statistic and null controls
- consistent result under leave-one-footprint-out and leave-one-hemisphere-out tests

If only DESI Legacy plus SDSS is available, I would not call that enough; SDSS is the old failure regime and DESI Legacy overlaps its selection/systematics too much. DESI Legacy plus Euclid/Rubin may eventually be meaningful, but current Euclid Q1/Rubin preview products are too limited for this.

## Dataset-specific Scope Attacks

### DESI Legacy / Galaxy Zoo DESI

Best near-term imaging base, but not a handedness catalogue. Use it only if the design owns a frozen image-to-handedness pipeline. Public GZ DESI morphology outputs cannot be reinterpreted as chirality.

Risk that survives mirror self-test: a volunteer-trained model may abstain or lower confidence asymmetrically across sky-correlated covariates, even while flipping labels correctly for accepted objects.

### HSC DR3 public spin catalogue

Already analysed and reanalysed. Tori notes the sign mapping is undocumented for directional claims but sign-invariant anisotropy was already tested by Stiskalek & Desmond, who found no significant monopole, dipole, or quadrupole and strong preference for isotropy under their model. Per Duho's rule, believe and build on that rather than rerun looking for a preferred answer.

Use only as literature/context unless the scope identifies a genuinely new public field, control, or independent pipeline.

### Euclid Q1

Excellent future provenance, not enough footprint now. Current Q1 is too small and selected for large-scale preferred-axis language. It may become a replication family after broad public releases and a chirality-safe pipeline.

### Rubin / LSST preview products

Not public enough under the order's constraint and not wide/final enough. Treat as future watchlist only.

### SDSS / GZ1

Use as a negative-control history, not as the core data. It is where the bias problem was exposed.

### DESI spectroscopy

Support layer for redshifts and sample stratification. It does not supply morphology or handedness and must not be allowed to launder the imaging classifier result into an independent replication.

### CMB datasets: Planck / ACT / SPT

Not galaxy handedness datasets. Planck is relevant literature for isotropy anomalies, already studied. ACT/SPT partial-sky products cannot rescue a galaxy-spin claim and would introduce a different mask/systematics problem.

## Required Additions Before This Scope Is Gateable

1. State explicitly: mirror anti-equivariance is necessary but not sufficient.
2. Add an inherited-prior/selection-bias control, including confidence and abstention, not only label flips.
3. Forbid use of GZ DESI/DECaLS `spiral-winding` as chirality.
4. Freeze WCS parity validation as a first-class gate with Jacobian sign receipts and injected asymmetric test images.
5. Expand the null-control covariate list and require joint preservation or adversarial sky-position predictability tests.
6. Upgrade replication from "two families are enough" to "two families are a floor; preferred-axis language still needs independence of imaging, footprint, preprocessing, and classifier."
7. Include an explicit `NOT_WORTH_DOING_YET` branch if no public chirality estimator can be frozen without new labelling.

## Final Disposition

I would not block scoping the study. I would block any scope that treats the mirror self-test as sufficient, treats public GZ DESI/DECaLS morphology columns as handedness, or treats two instrument families as automatic replication.

The admissible next product is a stricter design brief, not a run.

SCOPE_PROCEED_WITH_HARDENING_REQUIRED

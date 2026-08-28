# KUN SPIN DESIGN BRIEF GATE

Timestamp: 2026-08-12 KST

Target: `reviews/LANA_SPIN_DESIGN_BRIEF_20260812.md`

Related data survey: `reviews/GORU_SPIN_DATA_SURVEY_20260812.md`

Prior Kun standard: `reviews/KUN_SPIN_ANISOTROPY_REGATE_20260811.md`

## Verdict

PASS AS A DESIGN BRIEF; NOT A PREREGISTRATION FREEZE; NO EMPIRICAL SKY RUN YET.

Lana's brief stays inside my three-tier gate:

- label-table reanalysis remains `NOT_WORTH_DOING_YET`;
- an image-level, custody-audited, mirror-controlled, preregistered fixed-axis test remains `WORTH_SCOPING`;
- an immediate empirical run remains `BLOCKED` until a separate preregistration artifact freezes every open value.

The design is buildable in principle. It is not yet frozen. The next valid step is a non-sky-statistic feasibility/custody spike plus Tori's FITS/WCS access receipt, followed by a sha-pinned preregistration. If anyone computes a real sky statistic before that freeze, the run is void.

## 1. Acceptance And Rejection Regions

Mostly present, but not freeze-ready.

The brief names the two primary axes before any number:

- Longo: `(l,b)=(52°,68.5°)`;
- Shamir: `(RA,Dec)=(132°,32°)`.

It also states a predeclared per-axis decision structure:

- `REPRODUCED`: published sign, attenuation-corrected amplitude in `[0.02,0.08]`, permutation `p < 0.001`;
- `REJECTED-AT-CLASS`: `p > 0.05` and the attenuation-corrected `3σ` upper bound excludes `0.02`;
- `INCONCLUSIVE`: anything else;
- `INCONCLUSIVE-BY-POWER`: power gate fails before unblinding, so the run is not performed.

That is the right shape. It forces ambiguity to `INCONCLUSIVE` rather than letting a weak result be narrated into support.

The remaining issue is that the brief says the exact numbers are "the proposal" and will be "finalised in the prereg after the §7 power estimate." That is acceptable for a design brief, but it is not acceptable for the freeze. The frozen preregistration must contain the final amplitude floor, permutation count, p-thresholds, attenuation formula, and power rule as fixed values before any real sky statistic is computed.

## 2. Kill Switches

The kill switches are real switches, not decorative caveats.

The strongest ones are:

- `K-1`: if only a human-label-trained classifier is feasible, the anisotropy study stops or becomes a bias-transfer study;
- `K-2`: any failed parity validation or injected-image inversion halts the lane;
- `K-4`: ambiguous covariate leakage returns `INCONCLUSIVE`;
- `K-6`: power gate failure returns `INCONCLUSIVE-BY-POWER` and no run;
- `K-8`: any parameter change after any sky statistic voids the run;
- `K-9`: no survey meeting data properties 1-3 returns `NOT_WORTH_DOING_YET`;
- `K-10`: approximate equivariance is not accepted.

These are pass/fail conditions. They do not merely say "note the limitation."

One wording hazard should be tightened before freeze: §0 says biased or noisy calibration costs "sensitivity, never validity" and that the sorter "cannot manufacture a net asymmetry." The later brief correctly names monopole × sensitivity-gradient coupling and pixel-path artifacts as validity threats. Keep the later substance; soften the early absolute. Safer freeze wording:

> Under the antisymmetry identity, constant chirality offset in the estimator cancels in paired mirror evaluation. Residual validity threats move upstream to pixel-path parity, sample preselection, monopole × sensitivity-gradient coupling, and leakage in confidence/abstention; these are kill-switched below.

That is not a blocker for the design brief because the controls are present, but it would be a blocker if the absolute phrasing survived into a public-facing claim.

## 3. BHU Boundary

PASS.

The boundary section states plainly that a positive result would not identify BHU. It says the BHU closing record stands, that no source supplies a calibrated BHU-specific sky-statistics target, and that any measured asymmetry would be a spin-anisotropy/statistical-isotropy result only. That is exactly the required boundary.

## 4. Negative-Control Battery

PASS FOR DESIGN; FREEZE NEEDS EXACT PARAMETERS.

The battery is sufficient to make a null interpretable if implemented as written:

- full-mirror run with paired per-object outputs;
- permutation nulls preserving positions/footprint;
- hemisphere/axis sign checks;
- covariate leakage tests on sign, confidence, and abstention;
- monopole-gradient coupling bound;
- split-sample stability;
- power gate tied to a hand-checked attenuation estimate.

The reason this can support a null is the combination of `REJECTED-AT-CLASS` plus `INCONCLUSIVE-BY-POWER`: a null only becomes rejection if the corrected upper bound excludes the published amplitude class. Otherwise the design says `INCONCLUSIVE`.

Before freeze, the covariate battery needs exact executable definitions: maps, binning, regression or matching model, leakage threshold, and what counts as "ambiguous." The present brief is allowed to leave those for the preregistration; the preregistration is not.

## 5. Attenuation Estimate

CONCRETE ENOUGH FOR DESIGN; NOT ENOUGH FOR FREEZE.

The hand-checked subsample is specified as approximately 500 accepted galaxies, stratified by `|χ|`, size, and depth, with random pre-mirroring, two independent checkers, sealed parity keys, and per-stratum accuracy feeding `(2a-1)` attenuation and the power gate. That is executable at design level.

The frozen version must specify:

- exact subsample size or deterministic rule for increasing it;
- exact stratum boundaries;
- checker instructions;
- disagreement/adjudication rule;
- whether objects marked uncertain are abstentions or errors;
- exact confidence interval for `a`;
- exact formula translating `a` into corrected amplitude and upper bounds.

Without those, the attenuation gate could be adjusted after seeing awkward calibration. With them, it is a real power control.

## 6. Goru Tension: Is "ALL FAIL" Correct?

Goru's `ALL CANDIDATES FAIL` is over-strict for Lana's design.

The design does not require the survey to publish mirrored-image control runs. We run the mirrored control. That is the point of the architecture.

The correct data-selection standard is:

> The selected archive must provide public calibrated pixel data, preferably native FITS cutouts or frames, with intact per-image WCS sufficient for us to compute the pixel-to-sky parity ourselves; our own pipeline must then perform lossless rendering, WCS parity logging, synthetic chiral injections, and original/mirror paired classification through the exact measurement path.

On that standard, "no native mirrored runs" is not a failure. "Only rendered images with no WCS or unverifiable orientation" is a failure.

The `CDi_j`/`PCi_j` matrix is not a magic certificate for every upstream reduction choice, but it is the correct custody object for this study if the delivered image is the measurement input. Handedness is defined on the sky. Given calibrated pixels plus WCS, the determinant of the pixel-to-sky transform tells us whether the raster orientation is parity-preserving or parity-reversing relative to sky coordinates. If the classifier operates in sky coordinates using that transform, a survey-side North-up/East-left JPEG convention is unnecessary and less clean than native FITS.

What could still break the design:

- Tori finds that candidate services return only JPEG/PNG images without WCS or with undocumented orientation;
- the archive cutout service strips or corrupts WCS;
- the chosen products are mosaics/coadds whose WCS is invalid at the precision needed for local parity;
- the pipeline requires an external FITS-to-JPEG renderer whose row order is not controlled by us;
- injected chiral test images or scrambled-WCS nulls fail;
- the footprint/scale/power requirements are not met.

What does **not** by itself break the design:

- the survey did not publish mirrored controls;
- the survey did not natively run a chirality experiment;
- the FITS images are resampled/coadded, provided the delivered pixels have valid WCS and pass our parity/injection tests.

Therefore Goru's facts are useful, but the executive verdict applied the wrong standard. It tested whether the survey itself already provides the experiment. Lana's design requires only that the archive gives us orientation-verifiable pixels so we can run the experiment.

## 7. Plain Verdict For Duho

The design is buildable in principle and worth taking to the next freeze-preparation step.

Not cleared:

- no real sky statistic;
- no empirical result;
- no publication;
- no BHU interpretation;
- no use of a human-label-trained classifier as the primary anisotropy instrument.

Cleared:

> A design brief for a public-FITS, WCS-custodied, mirror-controlled, preregistered fixed-axis spin-anisotropy test, with the freeze still ahead.

Required before freeze:

1. Tori confirms at least one survey route returns public calibrated FITS with intact WCS and enough footprint/scale.
2. Lana replaces the early "never validity" absolute with the narrower antisymmetry/custody wording.
3. The preregistration fixes the final decision thresholds, attenuation/power formulas, covariate-leakage tests, and hand-check protocol as executable values.

If Tori's access receipt says the candidate routes are rendered-image-only or WCS-inadequate, the verdict falls back to `NOT_WORTH_DOING_YET`.

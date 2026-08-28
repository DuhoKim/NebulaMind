# KUN — BHU New-data Survey, Adversarial Step 3

Filed: 2026-08-10 22:42 KST  
Order: `HWAO_BHU_NEW_DATA_SURVEY_ORDER_20260810T2210K.md`  
Role: adversarial review of public-data candidates; no result computed.

## Boundary

Black-hole-universe cosmology is Duho's standing personal research interest, not a ranked frontier in this corpus. That is not a disqualifier; it is the reason this scoping exists. But any packet implying that BHU is a mainstream-priority driver for these catalogues would misrepresent the field.

This survey does not modify the spin lane. `lanes/spin/SOURCE_FREEZE.json` still forbids BHU support in that video. Nothing here unblocks a lane, a video, a result, publication, or public delivery.

## Bottom Line

There is new public data since the 2008 Galaxy Zoo era, and one class is genuinely worth design work: modern wide-field imaging plus public morphology models/catalogues, especially DESI Legacy Surveys / Galaxy Zoo DESI.

But none is ready to support a handedness or preferred-axis finding. The weak link is not survey size; it is chirality control. The phrase "we control the classifier now" is only partly true. We can run a CNN on mirrored inputs if we own the model pipeline, but the public Galaxy Zoo DESI/DECaLS morphology products are trained to predict volunteer responses. A network trained on historical human labels can inherit human handedness bias, then spread it over millions of galaxies with excellent-looking precision. That is the same failure mode as GZ1 wearing modern infrastructure.

The honest status is: **promising design candidate, no reportable result candidate**.

## Candidate Attacks

### Galaxy Zoo DESI + DESI Legacy Imaging

What exists: Galaxy Zoo DESI releases detailed morphology measurements for 8.7M bright galaxies in the DESI Legacy Imaging Surveys, produced by deep learning models trained on Galaxy Zoo volunteer responses. Legacy Surveys DR10 provides public optical imaging/catalogues over >20,000 deg² in some bands and a consistent Tractor model over much of the sky.

What kills it as-is:

- **Human-label inheritance:** the released GZ DESI measurements estimate what volunteers would say, not an instrument-independent handedness observable. If volunteer labels contain a left/right bias, the model can learn that bias.
- **No public mirror-counterfactual column:** the catalogue gives predicted morphology/vote fractions, not a frozen paired result of the same model run on original and deliberately mirrored images.
- **Display-frame ambiguity:** "clockwise" in a cutout depends on WCS, image construction, axis orientation, and display parity. A handedness study must prove the same sky spiral is not silently flipped by cutout service, JPEG generation, FITS display convention, or preprocessing.
- **Footprint anisotropy:** DESI Legacy imaging is not full-sky and combines DECam/BASS/MzLS plus extra DECam material. Any preferred-axis test can confound sky signal with north/south instrument split, Galactic avoidance, depth gradients, seeing, and survey tiling.
- **Selection-function coupling:** r<19 and "well-resolved" morphology selection are sky-position and redshift dependent. Spiral-arm recoverability changes with depth, seeing, surface brightness, dust, inclination, and redshift.
- **Model-domain drift:** a model calibrated for detailed morphology may be accurate on Galaxy Zoo questions while still unsafe for chirality; mirror invariance/anti-invariance is a different property from "spiral arms present."

Adversarial disposition: **best candidate for a future pre-registered method study, but HOLD for any handedness/preferred-axis result.** It needs a frozen, public, paired original-vs-mirrored inference run, with sky-coordinate parity audited before any axis statistic.

### Galaxy Zoo DECaLS

What exists: DECaLS classifications cover ~314k galaxies and include volunteer classifications plus Bayesian CNN predictions trained on volunteers. The paper reports random horizontal/vertical flips and rotations in model augmentation, and Galaxy Zoo now says GZ DECaLS is superseded by GZ DESI.

What kills it:

- Too small and footprint-limited relative to GZ DESI.
- Same human-label inheritance problem.
- Augmentation helps ordinary morphology generalization; it does not by itself establish a chirality-calibrated handedness observable.
- Superseded data product; any new study should justify why it does not use GZ DESI instead.

Disposition: **useful only as a historical/method-development baseline**, not as the main BHU data candidate.

### DESI DR1 Spectroscopy

What exists: DESI DR1 contains >18M useful spectra and >13M galaxies, with public redshift and LSS catalogues.

What kills it:

- Spectra do not encode spiral handedness. They can provide redshifts, sample definitions, and cross-checks, but not chirality.
- DESI target selection and footprint are optimized for cosmology tracers, not morphology parity.
- Crossmatching DESI redshifts to morphology catalogues imports both selection functions; the intersection can produce redshift-dependent morphology recovery biases.

Disposition: **supporting redshift/provenance layer only**, not a handedness dataset.

### SDSS DR17/18/19

What exists: SDSS remains public and cumulative; DR19 is the current SDSS-V public release. DR18 itself did not add new SDSS imaging; legacy imaging is old.

What kills it:

- For spin handedness, SDSS/GZ1 is the failure case, not the rescue. Human-classifier bias and mirrored-condition ambiguity are already the central blocker.
- Newer SDSS spectroscopic releases do not create new wide-field morphology/chirality information.
- Reusing SDSS as a baseline risks re-importing the exact classifier and documentary-frame problems already found.

Disposition: **baseline/control only; not new leverage for BHU handedness.**

### Euclid Q1

What exists: Euclid Q1 publicly released ~63 deg² of calibrated space images/catalogues in March 2025, with early morphology papers and high-resolution imaging. Euclid expects a much larger mission survey and already reports large morphology potential.

What kills current Q1:

- Q1 is small and deep-field selected; preferred-axis tests need huge, well-characterized sky coverage, not a few special fields.
- No public chirality/handedness catalogue is established here.
- Spacecraft scan law, detector geometry, PSF anisotropy, masking, and field placement would need parity-specific calibration.
- Deep-field selection is inherently anisotropic; any axis result would be footprint-dominated.

Disposition: **future candidate when broad public releases and chirality-safe morphology pipelines exist; Q1 is not enough.**

### Rubin / LSST DP1 and EDP2

What exists: Rubin DP1 was released June 30, 2025 from seven ~1 deg² commissioning fields and is access-limited to Rubin data-rights holders. EDP2 was planned for July 27, 2026 and early public materials describe COSMOS commissioning imaging, not the full LSST survey.

What kills current previews:

- Public-access status and field scope are not yet the uniform, wide, decade-scale LSST survey product a handedness axis test would need.
- Commissioning/deep-preview fields are selection-function traps.
- Rubin image simulations, coadds, deblending, seeing variation, and camera rotation patterns can create position-dependent morphology recovery.
- No public handedness catalogue or mirror-controlled classifier product exists.

Disposition: **watchlist, not usable now.** The full survey may become powerful, but preview data are not a BHU handedness test.

### Planck Final / PR4

What exists: public full-sky CMB maps, component-separated products, masks, and reprocessed PR4/NPIPE products.

What kills it for this question:

- It is not a galaxy handedness dataset.
- CMB anomaly/preferred-axis work is dominated by masks, foregrounds, a posteriori statistics, and look-elsewhere effects.
- Without a Lana-frozen BHU observable that predicts a specific CMB statistic before looking, Planck is an evocative context source, not a new test.

Disposition: **not usable for a handedness study; only usable if Step 1 produces a concrete, pre-registered CMB observable.**

### ACT DR6

What exists: public ACT DR6 maps and derived products, with 2017-2022 CMB temperature/polarization data over ~19,000 deg² and public LAMBDA/NERSC access.

What kills it:

- Not morphology; no handedness.
- Ground-based microwave footprint is highly anisotropic and survey-strategy dependent.
- Atmospheric filtering, scan strategy, masks, foreground residuals, and overlap with optical surveys create a large systematics surface for any preferred-axis comparison.
- Cross-correlation with galaxy handedness would inherit the optical handedness systematics plus ACT mask/noise anisotropy.

Disposition: **not a primary BHU-handedness dataset.** Possible future cross-check only after an optical chirality result exists independently, which it does not.

### SPT-3G

What exists: public SPT-3G data products on LAMBDA, including D1 maps/products and earlier lensing/power-spectrum products; SPT-3G primarily covers a southern low-foreground field.

What kills it:

- Not morphology; no handedness.
- Smaller and strongly selected sky footprint makes preferred-axis inference especially vulnerable.
- Ground-based microwave systematics and field choice dominate any large-angle directional interpretation.
- Cross-correlation would be downstream of an optical handedness result and cannot rescue a bad chirality measurement.

Disposition: **not usable as the BHU handedness lever.**

## Premise Attack: Do We Really Control the Classifier?

Only if the study owns all of the following before looking at sky statistics:

- the exact model weights and preprocessing
- the exact original and mirrored image-generation code
- WCS/display parity validation with known asymmetric test images
- a frozen rule for converting paired model outputs into handedness
- a frozen bias-only control showing the classifier's chirality response is not just inherited volunteer bias
- independent-survey replication across different optics/footprints

The public GZ DESI/Zoobot ecosystem gets partway there because models and public images exist. It does not close the gate by itself, because the public catalogue is a prediction of volunteer answers and not a paired chirality experiment. If the model was trained to reproduce humans, "CNN controlled" may simply mean "human bias automated."

## What Would Make One Candidate Survive

For DESI Legacy / GZ DESI to become a real candidate, I would require a pre-registered public-data-only design:

1. Use public images and public model code/weights, or freeze a fully public replacement classifier before any sky statistic.
2. Generate original and left-right mirrored cutouts from FITS with WCS parity logged.
3. Run the same frozen classifier once on both versions.
4. Define handedness only through the paired response, not through a one-sided catalogue column.
5. Include a null/control where sky coordinates are scrambled or image parity is randomized while preserving depth, seeing, Galactic latitude, instrument, and redshift distributions.
6. Require replication across at least two instrument/footprint families before any preferred-axis language.
7. Treat any ambiguous control, missing provenance field, or same-sign classifier bias as INCONCLUSIVE.

That would be a method proposal, not tonight's result.

## Sources Checked

- Hwao order: `HWAO_BHU_NEW_DATA_SURVEY_ORDER_20260810T2210K.md`, SHA-256 stated by user `1a1aa9940194fdc3...`
- Galaxy Zoo data / GZ DESI and DECaLS: https://data.galaxyzoo.org/index.html
- GZ DESI Zenodo release: https://zenodo.org/records/8331338/latest
- Zoobot science-data docs: https://zoobot.readthedocs.io/en/latest/science_data.html
- Galaxy Zoo DECaLS paper: https://academic.oup.com/mnras/article/509/3/3966/6378289
- Legacy Surveys DR10 description: https://www.legacysurvey.org/dr10/description/
- DESI DR1 data release: https://data.desi.lbl.gov/doc/releases/dr1/
- SDSS DR19/DR18 release documentation: https://www.sdss.org/science/publications/data-release-publications/ and https://www.sdss.org/dr18/imaging/
- Euclid Q1 release notes: https://euclid.caltech.edu/news/euclid-q1-date and https://www.euclid-ec.org/public/press-releases/new-science-results-images-euclid-q1/
- Rubin DP1/EDP2 docs: https://dp1.lsst.io/ and https://rubinobservatory.org/events/edp2-release
- Planck Legacy Archive CMB maps: https://wiki.cosmos.esa.int/planck-legacy-archive/index.php/CMB_maps
- ACT DR6 products: https://act.princeton.edu/act-dr6-data-products
- SPT-3G products: https://lambda.gsfc.nasa.gov/product/spt/spt_3gd1/

## Verdict

No public dataset in this pass is result-ready for BHU handedness or preferred-axis claims. GZ DESI / DESI Legacy is the only candidate I would keep alive for a future pre-registered method design; every other candidate is either support data, future watchlist, or the wrong observable.

FAIL_CLOSED_NO_RESULT_READY_DATASET

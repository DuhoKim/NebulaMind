# Tori isotropy/parity scope v2 — hardened provenance gate

Stamped: 2026-08-10 23:50 KST.[40]

Authority: `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_V2_20260810T2300K.md`, exact SHA-256 `99a1519aa070b9fb42ef65c855b978bbb1b14b7ae08341143141b42515c79c99`.[40]

The superseded 22:45K order remains preserved, but it is not authority and is not cited as authority here.[40]

This is a provenance and design-admissibility scope only; the authorized product is a stricter design brief, not a run.[40]

## Scope verdict

`NO_PROVENANCE_COMPLETE_V2_CANDIDATE`

`NOT_WORTH_DOING_YET`

`SCOPE_V2_HOLD_ADD_SIGNED_RESIDUAL_CONTROL`

The public literature remains genuinely disputed: Longo reported a dipole, while Land reported consistency with statistical isotropy after bias correction.[36][37]

Later rechecks found that duplicate removal materially reduced one claimed signal, and an all-public-catalogue analysis found consistency with isotropy within three standard deviations.[38][39]

The v2 correction is binding: mirror anti-equivariance is necessary but not sufficient.[40][42]

A classifier can flip perfectly under mirroring while its signed decisions, confidence, or abstention remain correlated with sky-position-linked selection effects.[40][41]

No present candidate passes all four required gates: public product semantics, exact delivered WCS parity, freezeable chirality estimation, and inherited-prior or selection observability.[1][31][40]

## Grade meanings

- `DOCUMENTED` means primary documentation defines the required field or convention and this packet quotes it.[40]
- `UNDOCUMENTED` means the primary-documentation check was performed and the missing meaning, convention, product, or receipt is named.[40]
- `NOT-YET-CHECKED` means the primary-documentation check has not been completed.[40]
- Overall candidacy requires every required v2 gate to be `DOCUMENTED`; a partial pass is not a candidate.[40]

No named candidate remains `NOT-YET-CHECKED`.[1][6][11]

## Decisive WCS-parity rule

“North up,” a named projection, or the existence of WCS keywords does not by itself establish delivered-image parity.[1][12][16]

A passing receipt must freeze the delivered FITS bytes and header, record the full WCS transform, evaluate the local pixel-to-sky Jacobian sign, and round-trip an injected asymmetric test image through extraction and preprocessing.[40][42]

Because this scope authorizes no image acquisition or execution, no candidate has a delivered-file checksum, Jacobian-sign receipt, or injected-image receipt in this packet.[40]

Therefore every image candidate is `UNDOCUMENTED` for exact delivered parity even where its product schema is `DOCUMENTED`.[1][12][16]

That status names an unclosed v2 gate rather than asserting that a survey product is incorrectly documented.[40]

## Candidate gate 1 — DESI Legacy Surveys DR10 imaging

**Product semantics: `DOCUMENTED`.**

Primary documentation says the image stacks use a “simple tangent-plane (WCS TAN) projection around the brick center.”[1]

The same documentation calls the brick stacks north-up, but the cutout service normally resamples them into a requested WCS grid.[1][2]

A `subimage` request returns brick-level subimages without that cutout resampling.[2]

The catalog documents Galactic extinction, per-band transmission, observation counts, depth, source-contamination fractions, masks, size, ellipticity, colour inputs, and profile type.[3][4][5]

The CCD tables separately document airmass, sky surface brightness, PSF ellipticity, camera identity, observation time, and depth.[4]

**Handedness semantics: `UNDOCUMENTED`.**

DR10 provides imaging, shapes, and profile fits, but it does not publish a clockwise/counterclockwise galaxy-spin field.[3]

Position-angle or ellipticity components describe an unoriented projected axis and are not handedness observables.[3]

**Exact delivered WCS parity: `UNDOCUMENTED`.**[1][2][40]

Missing are the frozen delivered FITS checksum and header, local Jacobian-sign calculation, crop/resampling transform receipt, and injected-asymmetric-image round trip.[1][2][40]

**Inherited-prior and selection inputs: `PARTIALLY DOCUMENTED`, therefore overall `UNDOCUMENTED`.**[3][4][40]

Documented inputs cover extinction, airmass, sky level, PSF ellipticity, depth, masking, contamination, angular size, colour, and profile family.[3][4][5]

Missing are frozen definitions for a stellar-density map, surface-brightness completeness, inclination proxy, band-dependent arm contrast, bulge fraction, pair-conditioned signed residual, adversarial sky-position predictor, thresholds, and fail-closed action.[3][4][40]

**Overall: `UNDOCUMENTED / NOT A V2 CANDIDATE`.**[1][3][40]

DR10 remains a plausible image source for a later methods packet, but v2 forbids committing to it before the missing parity and inherited-prior receipts exist.[1][40]

## Candidate gate 2 — pinned SpArcFiRe estimator

**Code and mirror operation: `DOCUMENTED`.**[31][33]

At pinned commit `22a3ea5d838d08242aa444c76b29e96fe3b6ce95`, the public README states that `mirrorLR=1` flips the image along the horizontal axis before processing.[31]

The published mirror experiment reports that only five of 29,250 image pairs disagreed on chirality.[33]

**V2 control surface: `UNDOCUMENTED`.**[31][41]

That mirror performance establishes a necessary anti-equivariance check, not sufficiency against inherited priors or sky-correlated selection.[33][40][42]

The checked public documentation does not freeze a pair-conditioned confidence definition, abstention definition, signed-label residual, covariate-adjustment model, negative-control target, leakage threshold, or fail-closed branch.[31][33][41]

The algorithm also documents that minimum-size settings can cause no arcs to be found, so failure and abstention must be treated as observable outputs rather than discarded cases.[31]

**Overall: `DOCUMENTED ESTIMATOR / UNDOCUMENTED V2 CONTROL SURFACE`.**[31][41]

SpArcFiRe is the only checked public non-learning chirality estimator that can be pinned without new labels, but it does not by itself close the v2 study gate.[31][33][40]

## Candidate gate 3 — Galaxy Zoo DECaLS

**Published field meaning: `DOCUMENTED`.**[6][7]

The DECaLS decision tree asks “How tightly wound do the spiral arms appear?” and its answers are tight, medium, or loose.[6]

Its schema follows question-and-answer vote-fraction naming rather than a signed clockwise/counterclockwise field.[7]

**Chirality admissibility: `UNDOCUMENTED / FORBIDDEN`.**[6][7][40]

Spiral-winding tightness is not chirality, and no signed handedness column with a sky-frame convention is published.[6][7]

Public pretrained Zoobot weights do not change the target meaning.[9][40]

**Overall: `EXCLUDED`, regardless of catalogue size.**[6][40]

## Candidate gate 4 — Galaxy Zoo DESI

**Published field meaning: `DOCUMENTED`.**[8]

The release states that its catalogs train deep-learning models on volunteer responses “to predict what volunteers might say for new galaxies.”[8]

Its reported outputs are predicted vote fractions, not an independently measured signed spin observable.[8]

**Chirality admissibility: `UNDOCUMENTED / FORBIDDEN`.**[8][40]

No public field maps a signed clockwise/counterclockwise value to a documented delivered-image or sky frame.[8]

Confidence or vote fraction cannot substitute for a missing handedness target.[8][40]

**Overall: `EXCLUDED`, regardless of public weights or catalogue size.**[8][40]

## Candidate gate 5 — SDSS DR17/DR18 imaging and public morphology code

**Image and catalogue semantics: `DOCUMENTED`.**[11][12][13]

SDSS publishes calibrated, sky-subtracted corrected-frame FITS products and says the frame header carries additional WCS information.[11][12]

Its `phiDeV` and `phiExp` fields are documented as position angles in degrees east of north.[13]

Those fields remain unoriented axes rather than signed handedness.[13]

**Exact delivered WCS parity: `UNDOCUMENTED`.**[11][12][40]

Missing are a frozen corrected-frame header, its local Jacobian sign, the crop or mosaic transform receipt, and the injected asymmetric-image round trip.[11][12][40]

**Freezeable public classifier: `UNDOCUMENTED`.**[14][15]

The public Domínguez Sánchez README says the code loads weights learned from SDSS, but the pinned public tree contains only the README and one DES training script.[14][15]

No frozen public signed-chirality weights, preprocessing manifest, or sign-to-frame mapping was found.[14][15]

**Prior-study status: historical control only.**[36][38][39]

Land reported consistency with isotropy after bias correction, and Iye and Sugai found that duplicate removal reduced a claimed signal to a distribution compatible with randomness.[36][38]

A later public-catalogue analysis also reported consistency with isotropy within three standard deviations.[39]

**Overall: `UNDOCUMENTED / HISTORICAL CONTROL ONLY`.**[36][38][39]

## Candidate gate 6 — Euclid Q1

**Catalog and WCS schema: `DOCUMENTED`.**[16][17]

The background-subtracted mosaic schema lists mosaic astrometric parameters including `CTYPE`, `CRVAL`, `CRPIX`, and CD-matrix elements.[16]

The final catalogue defines `POSITION_ANGLE` as counter-clockwise from the image x-axis, with a range from minus ninety to ninety degrees.[17]

That position angle is an unoriented source axis, not chirality.[17]

**Volunteer-image product: `DOCUMENTED BUT NOT PARITY-BEARING`.**[18]

The morphology release shares the original JPEG cutouts shown to volunteers.[18]

Those JPEGs do not supply a frozen FITS WCS, Jacobian-sign receipt, or signed spin target.[18][40]

**Exact delivered WCS parity: `UNDOCUMENTED`.**[16][40]

The product schema names the WCS fields, but this packet has no delivered Q1 FITS header, Jacobian sign, crop or resampling receipt, or injected asymmetric-image round trip.[16][40]

**Classifier independence: `UNDOCUMENTED`.**

The available public model route is a human-response predictor, not an independent signed-chirality estimator.[9][18]

**Overall: `UNDOCUMENTED / VALIDATION-ONLY POSSIBILITY`, not a preferred-axis candidate.**[16][18][40]

## Candidate gate 7 — HSC PDR3 raw imaging

**Product family: `DOCUMENTED`.**

HSC describes single-visit images transformed onto a destination tangent plane and coadd image products.[21]

Archive retrieval requires a registered account.[22]

**Exact delivered WCS parity: `UNDOCUMENTED`.**[21][22][40]

The checked public pages do not state the exact pixel-parity convention of the delivered cutout, and this packet contains no frozen header, Jacobian-sign receipt, or injected-image round trip.[21][22][40]

**Selection observability: `UNDOCUMENTED`.**

HSC warns that star-forming regions and spiral arms can be over-deblended into separate pieces.[23]

No frozen v2 mapping from that failure mode into pair-conditioned abstention, signed residuals, or completeness controls was found.[23][40][41]

**Overall: `UNDOCUMENTED / NOT A V2 CANDIDATE`.**[21][23][40]

## Candidate gate 8 — public HSC signed-spin table

**Column existence: `DOCUMENTED`.**

The reproduction page publishes galaxy coordinates and directions of rotation, and the CSV header contains `direction_cw_ccw` with values `1` and `-1`.[26][27]

**Sign semantics and frame: `UNDOCUMENTED`.**[26][27]

The checked page and CSV do not map `1` and `-1` to clockwise versus counterclockwise or state the delivered-image/display frame used to assign the signs.[26][27]

**Prior-study status: context only.**[28][40]

A published Bayesian reanalysis of this public table reports decisive evidence for an isotropic model.[28]

Under the instruction to believe and build on prior catalogue-specific bias studies, this table is not a fresh candidate.[28][40]

**Overall: `UNDOCUMENTED / CONTEXT ONLY`.**[26][28][40]

## Candidate gate 9 — Rubin DP1 and DP2

**Public-access gate: `UNDOCUMENTED / INELIGIBLE`.**[24][25][40]

Rubin states that only data-rights holders may access DP1 through the Rubin Science Platform.[24]

Rubin states the same data-rights restriction for DP2 and describes its early image products as limited.[25]

Restricted access fails the public-data-only requirement before WCS, chirality, or inherited-prior design can begin.[24][25][40]

**Overall: `INELIGIBLE`.**

## Candidate gate 10 — DESI spectroscopy

**Product meaning: `DOCUMENTED`.**

The official releases page identifies DR1 as the first DESI data release and lists only DR2 cosmology-support products beyond it.[29]

DR1 is a spectroscopic release containing spectra for more than eighteen million unique targets.[30]

**Handedness and WCS parity: not applicable as a primary image candidate.**[29][30]

Spectra can later supply redshifts, but they do not provide galaxy images or signed handedness.[30]

**Overall: `DOCUMENTED / SUPPORT-ONLY`.**[29][30]

## V2 inherited-prior and selection-bias gate

Mirror-pair label flips are required, but passing them does not authorize a sky statistic.[40][42]

A future design must test confidence and abstention after conditioning on each original/mirror pair.[40]

It must separately test the conditional signed-label residual among non-abstained galaxies, because flat confidence and abstention can coexist with a sky-correlated sign leak.[41]

It must include a pre-specified negative-control target that should remain null under the same pipeline.[41]

The first covariate block must separate Galactic extinction, stellar density, and Galactic latitude.[40]

The observing block must include sky brightness, airmass history, PSF ellipticity, model residuals, deblending or crowding flags, and surface-brightness completeness.[40]

The galaxy block must include angular size, inclination proxy, colour, band-dependent arm contrast, and profile type or bulge fraction.[40]

Those variables must be jointly preserved or used in an adversarial test of sky-position predictability; one-variable-at-a-time plots are insufficient.[40][41]

The statistic, covariate-adjustment class, cross-fitting rule, threshold, and fail-closed action must be frozen before any sky scan.[41]

## Instrument-independence gate

Two instrument families are a floor, not sufficiency.[40]

Preferred-axis language additionally requires independence of imaging hardware, footprint, preprocessing, and classifier.[40]

The present public set provides no pair of end-to-end stacks that are independent on all four dimensions and provenance-complete under v2.[9][31][40]

Reusing SpArcFiRe across Legacy, SDSS, HSC, or Euclid would not establish classifier independence.[31][40]

Using Zoobot as the second estimator would reintroduce a human-response target and therefore does not close the gate.[8][9][40]

## Explicit branch

SpArcFiRe means the narrow statement “no public chirality estimator exists” is false.[31][33]

The current end-to-end study is nevertheless `NOT_WORTH_DOING_YET` because every image family lacks a decisive delivered-parity receipt, no second independent public chirality estimator passes, and the inherited-prior signed-residual control remains unfrozen.[1][31][41]

The next admissible artifact is a stricter no-execution design brief that specifies how those receipts and controls would be generated under a separate authorization.[40][41]

No dataset acquisition, classifier execution, sky statistic, scientific result, claim, publication, video, public-surface change, lane unlock, or acceptance is conferred by this packet.[40]

## Sources

[1] https://www.legacysurvey.org/dr10/description
[2] https://www.legacysurvey.org/svtips
[3] https://www.legacysurvey.org/dr10/catalogs
[4] https://www.legacysurvey.org/dr10/files
[5] https://www.legacysurvey.org/dr10/bitmasks
[6] https://arxiv.org/pdf/2102.08414
[7] https://zenodo.org/records/4573248/files/schema.md
[8] https://zenodo.org/records/8331338
[9] https://zoobot.readthedocs.io/en/latest/pretrained_models.html
[11] https://www.sdss4.org/dr17/imaging/images
[12] https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/frames/RERUN/RUN/CAMCOL/frame.html
[13] https://www.sdss4.org/dr12/algorithms/magnitudes
[14] https://raw.githubusercontent.com/HelenaDominguez/DeepLearning/8e0e26c502c4d1f4d8ae55bb2b5e401f2f728b60/README.md
[15] https://api.github.com/repos/HelenaDominguez/DeepLearning/git/trees/8e0e26c502c4d1f4d8ae55bb2b5e401f2f728b60?recursive=1
[16] https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html
[17] https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html
[18] https://zenodo.org/records/15027787
[21] https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3
[22] https://hsc-release.mtk.nao.ac.jp/doc/index.php/data-access__pdr3
[23] https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3
[24] https://dp1.lsst.io/index.html
[25] https://dp2.lsst.io/index.html
[26] https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc
[27] https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/data_hsc.csv
[28] https://arxiv.org/pdf/2410.18884
[29] https://data.desi.lbl.gov/doc/releases
[30] https://data.desi.lbl.gov/doc/releases/dr1
[31] https://raw.githubusercontent.com/waynebhayes/SpArcFiRe/22a3ea5d838d08242aa444c76b29e96fe3b6ce95/README.md
[33] https://arxiv.org/pdf/1610.07060
[36] https://arxiv.org/pdf/0803.3247
[37] https://arxiv.org/abs/1104.2815
[38] https://arxiv.org/pdf/2011.00662
[39] https://arxiv.org/pdf/2404.06617
[40] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/HWAO_ISOTROPY_PARITY_SCOPE_ORDER_V2_20260810T2300K.md
[41] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/KUN_ISOTROPY_PARITY_SCOPE_V2_ADVERSARIAL_20260810T2300K.md
[42] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_ISOTROPY_PARITY_SCOPE_V2_20260810.md

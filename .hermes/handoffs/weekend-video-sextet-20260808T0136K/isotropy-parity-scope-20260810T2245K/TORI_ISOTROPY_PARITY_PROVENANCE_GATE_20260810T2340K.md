# Tori provenance feasibility gate — large-scale galaxy-spin isotropy/parity scope

Marker: `TORI_ISOTROPY_PARITY_PROVENANCE_GATE_20260810T2340K`

Governing order: `HWAO_ISOTROPY_PARITY_SCOPE_ORDER_20260810T2245K.md`, SHA-256 `681856e9b60bfb88c5d8c926a8089b930789355516c9b926f80661ca7bb01e7d` [60].

## Boundary

- This is scope only: no classifier or statistical run, data download, result, claim, video, publication, public-surface change, or lane unlock occurred [60].
- The target is a mainstream galaxy-spin isotropy/parity question; no model-specific interpretation is part of the scope, because either a detection or a null would remain non-unique [61].
- Grades are `DOCUMENTED`, `UNDOCUMENTED`, or `NOT-YET-CHECKED`; a required field that is absent counts as `UNDOCUMENTED`, not as an invitation to infer it [60].
- A dataset can pass its own image/WCS gate but still be inadmissible as a study candidate if the handedness estimator, mirror control, public-access rule, or independent-footprint requirement fails [60][62].

## Gate result at a glance

- `DOCUMENTED — CORE IMAGE SOURCE, CONDITIONAL`: DESI Legacy Surveys DR10 brick-native FITS, provided the study freezes the native-brick/subimage path, logs every FITS WCS Jacobian determinant, and never uses a display JPEG as the parity authority [6][7][62].
- `DOCUMENTED — PUBLIC NON-LEARNING ESTIMATOR, CONDITIONAL`: SpArcFiRe at commit `22a3ea5d838d08242aa444c76b29e96fe3b6ce95`, provided acceptance is defined on original/mirror pairs and its published selection effects are carried into the design [37][39][44].
- `DOCUMENTED — METHOD-VALIDATION IMAGE SOURCE ONLY`: Euclid Q1 raw MER FITS mosaics, not the volunteer JPEGs or morphology catalogue; the footprint is too fragmented and small to support the large-scale axis claim by itself [19][21][58].
- `DOCUMENTED — HISTORICAL CONTROL ONLY`: SDSS corrected-frame FITS with SpArcFiRe; the relevant SDSS/GZ1 catalogue and algorithm biases have already been studied and must be built on rather than re-derived [14][39][50].
- `UNDOCUMENTED / INADMISSIBLE`: Galaxy Zoo DECaLS, Galaxy Zoo DESI, and public Zoobot encoders as handedness products, because their documented outputs do not contain a clockwise/counterclockwise target and the models reproduce volunteer answers [12][51][53].
- `UNDOCUMENTED / INADMISSIBLE`: the Domínguez Sánchez repository as a frozen SDSS classifier, because the public tree contains a README and one DES training script but no published weights; the README only describes loading weights learned elsewhere [17][54].
- `UNDOCUMENTED / INADMISSIBLE`: HSC PDR3 raw cutouts for the current gate, because public documentation identifies tangent-plane FITS products but the exact delivered cutout parity convention is behind the account-protected manual and is not stated in the checked public documentation [55][56].
- `UNDOCUMENTED / CONTEXT ONLY`: the public HSC signed-spin CSV, because `direction_cw_ccw` contains `+1/-1` values but its primary page and CSV do not map the signs to clockwise/counterclockwise; the catalogue has also already received a published Bayesian reanalysis [29][30][31].
- `UNDOCUMENTED / INELIGIBLE`: Rubin DP1/EDP2, because the image products are restricted to Rubin data-rights holders and therefore fail the public-data-only rule before classifier design begins [24][25].
- `DOCUMENTED — SUPPORT ONLY`: DESI DR1 spectroscopy; the public release contains spectra for more than 18 million unique targets but no image or handedness observable [34].
- `UNDOCUMENTED — SUPPORT ONLY`: object-level DESI DR2 data, because the official release index exposes DR1 as the public data release and lists DR2 cosmology support files, not a public object-level DR2 release usable for this study [33].
- No named candidate remains `NOT-YET-CHECKED`; candidates labelled `UNDOCUMENTED` name the exact missing item below [60].

## Candidate 1 — DESI Legacy Surveys DR10 image stacks

**Grade: `DOCUMENTED — CORE IMAGE SOURCE, CONDITIONAL` [6][7].**

- The primary DR10 description says the coadded images are brick products using a tangent-plane `WCS TAN` projection; the documented bricks are north-up and the optical bands share a 0.262-arcsec pixel scale [6].
- The cutout service normally resamples released brick products into a requested WCS grid, while its documented `subimage` option returns overlapping brick-level products without resampling [7].
- Therefore the admissible path is native brick/subimage FITS only, with release, layer, bands, brick identity, requested region, FITS checksum, WCS matrix, and the sign of the local pixel-to-sky Jacobian recorded per image [6][7][62].
- `shape_e1` and `shape_e2` are documented ellipticity components and imply an axis with a 180-degree position-angle range; they are not a signed handedness field and must not be used as one [2].
- Missing for a catalogue-only design: a signed handedness column and a release-supplied chirality classifier; neither exists in the DR10 product, so DR10 passes only as an image source paired with a separately frozen estimator [2][6].

## Candidate 2 — Galaxy Zoo DECaLS

**Grade: `UNDOCUMENTED / INADMISSIBLE AS HANDEDNESS` [12][52].**

- The full published decision tree asks how tightly spiral arms are wound and offers tight, medium, and loose; it contains no clockwise or anticlockwise answer [12].
- The primary schema describes morphology columns as `{question}_{answer}` and contains no handedness mapping [52].
- Public model weights exist, but the documented target is the Galaxy Zoo morphology tree rather than signed chirality [12][51].
- Exact missing item: a frozen clockwise/counterclockwise output head with documented sign semantics and mirrored-input preprocessing; downloading the released morphology columns cannot supply it [12][51][52].

## Candidate 3 — Galaxy Zoo DESI

**Grade: `UNDOCUMENTED / INADMISSIBLE AS HANDEDNESS` [53][62].**

- The release states that its catalogues are deep-learning predictions of what Galaxy Zoo volunteers would say and that its values are predicted volunteer vote fractions [53].
- Owning the public Zoobot encoder and preprocessing does not remove inherited human-label selection effects, and a mirror-flipping output can still retain covariate-dependent confidence or abstention bias [51][53][62].
- Exact missing item: a signed chirality target and a separately demonstrated inherited-prior/selection-bias control; neither is supplied by the public morphology catalogue [53][62].

## Candidate 4 — SDSS DR17 imaging and published morphology model

**Grade: `DOCUMENTED AS IMAGE SOURCE; UNDOCUMENTED AS PROPOSED CNN; HISTORICAL CONTROL ONLY OVERALL` [14][17][54].**

- SDSS corrected frames are quantitative FITS products whose headers contain WCS aligned to the final astrometric solution, so exact per-frame parity is recoverable from the file WCS [14][16].
- SDSS `phiDeV` and `phiExp` are documented as ellipticity position angles in degrees east of north; they are parity-even axes, not handedness [59].
- The cited Domínguez Sánchez public repository does not publish the claimed frozen weights: its complete public tree has only `README.md` and `train_DES_class_t00_TK_DS2018.py`, while its README describes loading SDSS-learned weights rather than distributing them [17][54].
- SpArcFiRe has already been applied to SDSS/GZ1 in the published bias literature, and cleaned/reanalysed SDSS catalogues have returned results compatible with isotropy [39][49][50].
- Exact missing item for a new CNN candidate: public signed-chirality weights, output semantics, preprocessing, and a reason to repeat already-published SDSS bias work; those conditions are not met [17][50][54].

## Candidate 5 — Euclid Q1

**Grade: `DOCUMENTED — METHOD VALIDATION ONLY` [19][21][58].**

- Raw MER mosaics document their astrometric WCS fields, including `CTYPE`, `CRVAL`, `CRPIX`, and `CD` matrix elements, so FITS parity can be computed and logged from the delivered product [19].
- The MER `POSITION_ANGLE` field is documented in degrees using a counter-clockwise NE-SW convention; it remains a parity-even ellipse axis, not a spin label [58].
- The released Galaxy Zoo Euclid JPEGs are explicitly the images shown to volunteers, but JPEGs do not carry the FITS WCS required to establish sky parity and are inadmissible as the parity authority [21][62].
- The admissible source is the raw MER FITS mosaic only, paired with the same frozen non-learning estimator as the core dataset; Q1 can test instrument/preprocessing transfer but cannot supply a large-scale preferred-axis footprint by itself [19][21].

## Candidate 6 — Rubin DP1 and EDP2

**Grade: `UNDOCUMENTED / INELIGIBLE` [24][25].**

- Rubin states that only data-rights holders can access DP1 through the Rubin Science Platform [24].
- EDP2 supplies only limited deep-coadd image products at this stage and does not cure the access restriction or supply a public handedness estimator [25].
- Exact missing item: unrestricted public access to frozen science FITS plus a documented chirality pipeline; until then Rubin is not a candidate under this order [24][25][60].

## Candidate 7 — HSC PDR3 raw imaging

**Grade: `UNDOCUMENTED FOR DELIVERED IMAGE PARITY` [55][56].**

- HSC PDR3 publicly documents more than 600 square degrees, FITS coadds/warps on destination tangent planes, and an image-cutout service requiring account registration [55][56].
- The checked public pages do not state the cutout's pixel-axis handedness or expose the account-protected cutout manual, so exact delivered image parity cannot yet be quoted from accessible primary documentation [55][56].
- HSC also documents over-shredding of nearby spiral arms as a persistent deblending problem, which would have to be a frozen selection covariate even after parity is solved [57].
- Exact missing item: a public primary definition of the cutout WCS/parity as delivered, or a separately authorized receipt from a frozen FITS header; neither is present in this scope [55][56].

## Candidate 8 — public HSC signed-spin catalogue

**Grade: `UNDOCUMENTED FOR SIGN MAPPING; CONTEXT ONLY` [29][30][31].**

- The primary page identifies coordinates and directions of rotation and the CSV exposes `RA`, `Dec`, `z`, and `direction_cw_ccw`, but no primary dictionary maps `+1/-1` to clockwise/counterclockwise or states the displayed-image frame [29][30].
- Stiskalek and Desmond already analysed this catalogue and found no significant anisotropy, with decisive Bayesian evidence for the isotropic model under their model and priors [31].
- Exact missing item: sign-to-direction and image-frame semantics; even if supplied later, the published analysis means this catalogue is prior evidence, not a fresh core to rerun [29][30][31].

## Candidate 9 — DESI spectroscopy

**Grade: `DR1 DOCUMENTED SUPPORT ONLY; OBJECT-LEVEL DR2 UNDOCUMENTED` [33][34].**

- DR1 is public spectroscopy with documented object-level spectra and identifiers, not a 2D imaging or handedness release [34].
- The current official release index documents DR1 as the data release and separately links DR2 cosmology chains/supporting files, which is insufficient provenance for an object-level DR2 join [33].
- DR1 could support redshift stratification only after a core image/estimator pair passes; it cannot create chirality and does not change candidate admissibility [33][34].

## Estimator gate — SpArcFiRe

**Grade: `DOCUMENTED — CONDITIONAL PUBLIC REPLACEMENT` [37][39][44].**

- The public repository is pinned at commit `22a3ea5d838d08242aa444c76b29e96fe3b6ce95`; its README documents FITS input, conversion/preprocessing options, per-image settings receipts, and `-mirrorLR`, which horizontally flips the input before processing [37].
- Its frozen output schema contains four named chirality estimates, including majority and arc-length-weighted winding, and its comparison code explicitly maps `S-wise`/`Z-wise` outputs against Galaxy Zoo clockwise/anticlockwise fields [44][45].
- The published mirror study reports only five chirality disagreements among 29,250 original/mirrored pairs and documents a chirality-independent selection construction [39].
- This is a non-learning geometric algorithm, so it avoids making a new CNN inherit a volunteer handedness target, but it does not eliminate image-quality, redshift, arm-visibility, deprojection, centring, or abstention/selection effects [39][40][62].
- A future design may use it only with pair-level acceptance: both original and mirror must succeed, confidence/quality must be symmetric, the handedness must flip, magnitude-related quality measures must match within a frozen tolerance, and every setting must be written before sky statistics [37][39][62].

## Literature constraint — do not re-derive

- Land and collaborators corrected a handedness bias in Galaxy Zoo 1 and reported consistency with statistical isotropy [46].
- Longo reported a dipole using 15,158 low-redshift SDSS spirals [47].
- Iye, Yagi, and Fukumoto found that removing duplicate catalogue entries reduced a reported dipole to a modest value compatible with randomness [49].
- Patel and Desmond collected all public binary-spin catalogues they identified and found every analysis consistent with isotropy within three standard deviations [50].
- These results make a catalogue-only reanalysis low-value; a new study is justified only by generated parity control plus genuinely independent image/instrument families, not by a larger table or another sky statistic [39][50][62].

## Provenance-gate verdict before design

`METHOD_FEASIBLE_BUT_LARGE_SCALE_CLAIM_NOT_YET_ADMISSIBLE` [6][37][55].

- One candidate pair passes the field/provenance gate for a methods scope: native DESI Legacy DR10 FITS plus pinned SpArcFiRe with generated mirror pairs [6][37][39].
- Euclid Q1 raw MER FITS can serve as a small, independent instrument/preprocessing validation set, and SDSS can serve as a historical control whose prior results are not re-derived [14][19][46].
- No second public large-area image family currently passes all of public access, exact delivered parity documentation, independent footprint, and frozen chirality estimator: HSC fails exact parity documentation and Rubin fails public access [24][55][56].
- Euclid Q1 passes the raw-FITS parity gate but remains a small, fragmented validation footprint rather than an independent large-area family [19][21].
- Therefore a full preferred-axis run is `NOT_WORTH_DOING_YET`; the bounded worthwhile next artifact would be a no-execution preregistration for the Legacy-plus-Euclid methods validation, explicitly prohibited from producing a cosmic-axis claim [60][62].
- That preregistration would have to freeze the FITS extraction path, WCS determinant sign, SpArcFiRe commit/settings, mirror pair acceptance, abstention logic, all covariates listed by Kun, null permutations, duplicate policy, thresholds, and fail-closed outcome before any image is processed [37][60][62].

## Standing result

- No study was run and no scientific result exists; this artifact only establishes which documented inputs could support a later, separately authorized methods design [60].
- Nothing here authorizes data acquisition, classifier execution, statistics, publication, public reporting, or a lane transition [60].

## Sources

[2] https://www.legacysurvey.org/dr10/catalogs
[6] https://www.legacysurvey.org/dr10/description
[7] https://www.legacysurvey.org/svtips
[12] https://arxiv.org/pdf/2102.08414
[14] https://www.sdss4.org/dr17/imaging/images
[16] https://data.sdss.org/datamodel/files/BOSS_PHOTOOBJ/frames/RERUN/RUN/CAMCOL/frame.html
[17] https://raw.githubusercontent.com/HelenaDominguez/DeepLearning/master/README.md
[19] https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_bksmosaic.html
[21] https://zenodo.org/records/15027787
[24] https://dp1.lsst.io/index.html
[25] https://dp2.lsst.io/index.html
[29] https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc
[30] https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/data_hsc.csv
[31] https://arxiv.org/abs/2410.18884
[33] https://data.desi.lbl.gov/doc/releases
[34] https://data.desi.lbl.gov/doc/releases/dr1
[37] https://raw.githubusercontent.com/waynebhayes/SpArcFiRe/22a3ea5d838d08242aa444c76b29e96fe3b6ce95/README.md
[39] https://arxiv.org/pdf/1610.07060
[40] https://arxiv.org/abs/1707.02021
[44] https://raw.githubusercontent.com/waynebhayes/SpArcFiRe/22a3ea5d838d08242aa444c76b29e96fe3b6ce95/regression-test-data/one_galaxy_dir/test_out/galaxy.csv
[45] https://raw.githubusercontent.com/waynebhayes/SpArcFiRe/22a3ea5d838d08242aa444c76b29e96fe3b6ce95/matlab/compareChirality.m
[46] https://arxiv.org/abs/0803.3247
[47] https://arxiv.org/abs/1104.2815
[49] https://arxiv.org/abs/2011.00662
[50] https://arxiv.org/abs/2404.06617
[51] https://zoobot.readthedocs.io/en/latest/pretrained_models.html
[52] https://zenodo.org/records/4573248/files/schema.md?download=1
[53] https://zenodo.org/records/8331338
[54] https://api.github.com/repos/HelenaDominguez/DeepLearning/git/trees/master?recursive=1
[55] https://hsc-release.mtk.nao.ac.jp/doc/index.php/available-data__pdr3
[56] https://hsc-release.mtk.nao.ac.jp/doc/index.php/data-access__pdr3
[57] https://hsc-release.mtk.nao.ac.jp/doc/index.php/known-problems__pdr3
[58] https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html
[59] https://www.sdss4.org/dr12/algorithms/magnitudes
[60] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/HWAO_ISOTROPY_PARITY_SCOPE_ORDER_20260810T2245K.md
[61] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/LANA_ISOTROPY_PARITY_SCOPE_20260810.md
[62] file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/reviews/KUN_ISOTROPY_PARITY_SCOPE_ADVERSARIAL_20260810T2245K.md

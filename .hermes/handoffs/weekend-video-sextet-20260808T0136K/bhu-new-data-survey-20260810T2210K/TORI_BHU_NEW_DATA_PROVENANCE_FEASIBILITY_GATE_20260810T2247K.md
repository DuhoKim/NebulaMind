# TORI BHU NEW-DATA PROVENANCE FEASIBILITY GATE

Marker: `TORI_BHU_NEW_DATA_PROVENANCE_FEASIBILITY_GATE_20260810T2247K`

- Verified: 2026-08-10T22:47:14+09:00 KST
- Governing order: `HWAO_BHU_NEW_DATA_SURVEY_ORDER_20260810T2210K.md`
- Governing-order SHA-256: `1a1aa9940194fdc3a738ed667a8a3b31272fc55993d5c10f277dd38f2ddb7fb0`
- State: `PROVENANCE_GATE_COMPLETE_RESEARCH_SCOPING_ONLY`
- Result/claim/publication/video/lane-unblock effect: `NONE`

## Mandatory framing

Black-hole-universe cosmology is Duho's standing personal research interest, not a ranked frontier in this corpus. It is his project. This does not disqualify it from careful study. It does mean that any output implying mainstream scientific priority or consensus would misrepresent the field.

The spin-lane freeze still forbids BHU support in that video. This is separate research scoping. Nothing here changes the freeze, unblocks a lane, establishes a result, supports a video claim, or authorizes publication.

Public data only. No new labelling was done or authorized.

## Bottom line

Verdict: `NEW_PUBLIC_DATA_EXISTS_BUT_NO_READY_BHU_DISCRIMINATOR_UNDER_CURRENT_CONSTRAINTS`.

There are substantially newer public imaging, morphology, spectroscopy, and CMB products than Galaxy Zoo 1. One especially relevant public spin catalogue, derived from HSC DR3, has already been analysed by the catalogue author and then independently reanalysed. The independent analysis found no significant anisotropy and decisive Bayesian preference for an isotropic, monopole-only model. Per Duho's instruction, the honest action is to believe and build on that result rather than rerun it looking for a different answer.

The other new products do not presently supply a clean, documented handedness observable:

1. Galaxy Zoo DECaLS, Galaxy Zoo DESI, and Euclid Q1 Zoobot catalogues do not publish clockwise/counterclockwise labels. Their `spiral-winding` quantities mean arm tightness, not chirality.
2. The released Galaxy Zoo DECaLS classifier was trained with random horizontal and vertical flips. That is useful for morphology invariance but deliberately removes the directional information needed for a handedness observable.
3. DESI Legacy, SDSS, and Euclid publish useful shape or position-angle quantities, but a position angle is an unoriented axis modulo 180 degrees. It does not recover clockwise/counterclockwise spin.
4. DESI DR1 adds excellent coordinates and spectroscopy but no handedness label. It can support a study; it cannot create the observable.
5. The claimed 0.8-1.3 million-object DESI Legacy spin catalogue is not a usable public product: its author's data page says the file is “coming soon” and the paper reference is “to be completed.”
6. Rubin DP1/EDP2 access is restricted to data-rights holders, and the public schema does not provide a handedness field or a fully documented sign/frame mapping for a would-be handedness observable.
7. Planck has already performed the relevant full-sky isotropy/anomaly analysis. ACT DR6 and SPT-3G D1 are powerful independent instruments but partial-sky products aimed mainly at smaller angular scales; they are not independent full-sky low-multipole replacements for Planck.

## What the primary BHU paper actually predicts

Popławski's current arXiv paper, “The universe as a black hole in isotropic coordinates” (arXiv:1910.10819), is the relevant primary source. It says a parent black hole's preferred axis could be inherited by the daughter universe and that alignment of CMB low multipoles and galaxy rotation axes “could thus be a signature of a rotating universe inside a black hole.”

This is a qualitative possibility, not a complete statistical prediction. The paper does not provide a pre-specified observable with an expected amplitude, redshift dependence, sky mask response, parent-axis location, or a likelihood that distinguishes BHU from other rotating-universe models, standard structure-formation alignments, survey selection, or Galactic-frame systematics.

Therefore an isotropy or handedness test can constrain a class of preferred-axis observations, but it is not presently a unique BHU test. A positive result would not identify BHU; a null result would constrain only a quantitative BHU realization that first predicts a measurable signal.

Primary source: https://arxiv.org/abs/1910.10819

## Critical observable distinction

- Handedness/chirality: a signed S-wise/Z-wise or clockwise/counterclockwise winding label. Mirroring must invert the label. This can probe a parity-odd sky pattern.
- Position angle: an unoriented projected major-axis direction, normally modulo 180 degrees. Mirroring or rotating an image changes coordinate representation, but PA alone does not say clockwise or counterclockwise.
- CMB preferred-axis statistic: a low-multipole or dipolar-anisotropy statistic on full-sky temperature/polarization maps. This is neither galaxy handedness nor a direct measurement of a parent black-hole spin.

Conflating these would manufacture a BHU observable that the data do not contain.

## Provenance feasibility matrix

The required grades are `DOCUMENTED`, `UNDOCUMENTED`, or `NOT-YET-CHECKED`. “Documented but not a handedness product” is a passing provenance grade and a failing scientific-candidacy result for a handedness study.

### 1. DESI Legacy Surveys DR10 imaging/catalogue

Grade: `DOCUMENTED — POSITION ANGLE ONLY; NO HANDEDNESS FIELD`

Potential fields: `ra`, `dec`, `shape_e1`, `shape_e2`, source type, photometry, image WCS.

Primary documentation says:

- DR10 defines the ellipticity conversion as `phi = arctan2(e2,e1)/2`.
- The pinned Tractor source documents its galaxy-shape position angle as “Position angle in degrees, east of north.”

This establishes the frame of the fitted ellipse. It does not establish galaxy spin sign. An ellipse is invariant under a 180-degree reversal.

Sources:

- https://www.legacysurvey.org/dr10/catalogs/
- https://github.com/dstndstn/tractor/blob/3fd2e80eafb9cc092e203ba50a95557eb8543878/tractor/galaxy.py

### 2. Galaxy Zoo DECaLS volunteer and deep-learning catalogues

Grade: `DOCUMENTED — NOT A HANDEDNESS PRODUCT`

Primary schema meanings are recoverable. The `spiral-winding` answer fields are `tight`, `medium`, and `loose`; they are arm tightness, not clockwise/counterclockwise direction. The complete documented question set contains no chirality field.

The associated paper states that training images were randomly horizontally and vertically flipped. The model was designed to predict Galaxy Zoo morphology answers that are intended to be flip invariant. Evaluating this released model on mirrored inputs is a useful invariance audit, but it cannot produce a chirality label that was never an output target.

Sources:

- https://zenodo.org/records/4573248/files/schema.md?download=1
- https://arxiv.org/pdf/2102.08414
- https://zenodo.org/records/4573248

Correction to the preliminary inventory: “spiral winding direction (clockwise vs anticlockwise)” is not present in this release. Here, “winding” means tightness.

### 3. Galaxy Zoo DESI deep-learning catalogue

Grade: `DOCUMENTED — NOT A HANDEDNESS PRODUCT`

The catalogue supplies 29 detailed Galaxy Zoo morphology measurements over 8.67 million galaxies. Its two decision trees again define winding as tight/medium/loose and do not include clockwise/counterclockwise chirality.

The catalogue is valuable for selecting likely spirals without new human labels. It does not itself supply the signed spin observable, and the released Zoobot morphology model cannot be treated as though it does.

Sources:

- https://arxiv.org/pdf/2309.11425
- https://zenodo.org/records/8331338

### 4. DESI spectroscopy DR1

Grade: `DOCUMENTED — SUPPORT FIELDS ONLY`

Primary DR1 documentation identifies the public release, the redrock products, and the data model. `RA` and `DEC` are carried from the fibermap, and redrock `Z` is the fitted redshift. Target and catalogue identifiers are documented.

These fields can support object matching and redshift stratification. They do not encode morphology, position angle, or handedness.

Sources:

- https://data.desi.lbl.gov/doc/releases/dr1/
- https://data.desi.lbl.gov/doc/releases/dr1/spectro/redux/
- https://data.desi.lbl.gov/doc/releases/dr1/spectro/catalogs/

### 5. DESI spectroscopy DR2

Grade: `UNDOCUMENTED — NO PUBLIC DR2 PRODUCT VERIFIED`

The official DESI release index identifies DR1, released 1 July 2025, as the latest public data release and lists DR2 only as an anticipated future release in the papers page. No public DR2 data model or release tree was available to gate.

Correction to the preliminary inventory: “DR2 rolling out in 2025-26” must not be stated as a current public dataset.

Sources:

- https://data.desi.lbl.gov/doc/releases/
- https://data.desi.lbl.gov/doc/papers/

Missing: a public DR2 release page, field data model, immutable product identity, and files.

### 6. SDSS DR17/DR18 imaging catalogue

Grade: `DOCUMENTED — POSITION ANGLE ONLY; NOT NEW IMAGING`

The SDSS imaging algorithms documentation defines `phi` as position angle east of north and provides `phiDev`/`phiExp` for fitted profiles. DR17 documents the imaging catalogue and the model-fit fields.

SDSS DR18 states that it includes the same imaging data as DR13. This is not a new independent imaging epoch for this question. The position-angle fields are again unsigned axes, not chirality.

Sources:

- https://www.sdss4.org/dr17/imaging/catalogs/
- https://www.sdss4.org/dr12/algorithms/magnitudes/
- https://www.sdss.org/dr18/imaging/

### 7. Euclid Q1 source and morphology products

Grade: `DOCUMENTED — POSITION ANGLE/MORPHOLOGY ONLY; NO HANDEDNESS FIELD`

The Euclid Q1 morphology cookbook gives an explicit position-angle convention. It says position angles are measured counter-clockwise from the x-axis and describes the NE-SW convention used for the reference-frame products. The final catalogue data card and cookbook document the fields.

Euclid Q1 also publishes Zoobot morphology probabilities, but the documented questions are morphology/arm-tightness questions and do not supply clockwise/counterclockwise chirality.

The PA provenance is good. The handedness observable is absent.

Sources:

- https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/mermorphologycookbook.html
- https://euclid.esac.esa.int/dr/q1/dpdd/merdpd/dpcards/mer_finalcatalog.html
- https://www.cosmos.esa.int/web/euclid/q1-contents
- https://zenodo.org/records/15106473

### 8. Rubin/LSST DP1 and EDP2

Grade: `UNDOCUMENTED — INELIGIBLE UNDER PUBLIC-DATA-ONLY RULE`

The DP1 and EDP2 documentation states that access is limited to Rubin data-rights holders. This does not meet the strict public-data-only constraint used for this survey.

The public DP1 schema documents moment-like shape fields such as `shape_xx`, `shape_xy`, and `shape_yy` in pixel-squared units, but it does not provide a handedness field or a complete signed orientation convention suitable for a parity study on the schema page.

Sources:

- https://dp1.lsst.io/index.html
- https://sdm-schemas.lsst.io/dp1.html
- https://dp2.lsst.io/index.html
- https://rubinobservatory.org/for-scientists/data-products/recent-data-releases

Missing: unrestricted public access, a handedness product, and a primary public sign/frame definition for any derived parity label.

### 9. Public HSC DR3 spin catalogue

Grade: `UNDOCUMENTED FOR SIGN MAPPING; ALREADY ANALYSED FOR SIGN-INVARIANT ISOTROPY`

The public CSV contains `RA`, `Dec`, `z`, and `direction_cw_ccw` with values `+1` and `-1`. The public data page and CSV header do not state which sign is clockwise/S-wise and which is counterclockwise/Z-wise. That exact mapping is therefore not recoverable from the data dictionary alone.

This omission does not invalidate a sign-invariant test of whether dipole magnitude is zero: globally exchanging +1 and -1 reverses the axis but leaves the evidence for anisotropy unchanged. It does block honest directional claims tied to a named pole unless resolved.

Crucially, the catalogue has already been analysed:

- Shamir (2024) reported an asymmetry.
- Stiskalek & Desmond (2024), using the same public HSC DR3 spin catalogue and a Bayesian model, found no significant monopole, dipole, or quadrupole. They report a Bayes factor of 40,738 in favour of the monopole-only model under their tighter dipole prior and describe that as decisive evidence for isotropy.

Per Duho's instruction, this is evidence to build on, not an invitation to rerun the same catalogue until a preferred answer appears.

Sources:

- https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/
- https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/data_hsc.csv
- https://arxiv.org/pdf/2410.15269
- https://arxiv.org/abs/2410.18884
- https://arxiv.org/pdf/2410.18884
- https://github.com/harrydesmond/GalaxySpinAnisotropy

### 10. Claimed DESI Legacy DR8 handedness catalogue

Grade: `UNDOCUMENTED — FILE UNAVAILABLE`

The author's public page describes a catalogue with brick/object IDs, RA, Dec, and `cw/ccw`, but the data link says “coming soon” and the paper reference says “to be completed.” The advertised size on the page also differs from the approximately 1.3 million sample described in the MNRAS paper.

This product fails before analysis. We cannot verify the rows, field encoding, sample identity, label convention, checksum, or duplicate policy from a downloadable public artifact.

Sources:

- https://people.cs.ksu.edu/~lshamir/data/assym_desi/
- https://arxiv.org/pdf/2208.13866

Missing: the data file, a frozen version/checksum, the `cw/ccw` encoding, row-selection manifest, duplicate policy, and complete product reference.

### 11. Planck 2018 full-sky CMB products

Grade: `DOCUMENTED — ALREADY STUDIED; NOT A NEW BHU-SPECIFIC TEST`

Planck's public full-sky products and isotropy paper document the maps, HEALPix handling, component-separation products, masks, simulations, and polarization basis.

The Planck Collaboration already performed a comprehensive full-sky isotropy and statistics analysis. Its abstract says the temperature data confirm several large-angular-scale anomalies but are otherwise consistent with Gaussian ΛCDM; residual polarization systematics limit some tests; and it claims no unambiguous cosmological non-Gaussianity or polarization anomaly corresponding to the temperature anomalies.

That result should be cited as the current data constraint rather than independently recreated as a BHU result.

Sources:

- https://irsa.ipac.caltech.edu/data/Planck/release_3/all-sky-maps/
- https://www.aanda.org/articles/aa/full_html/2020/09/aa35201-19/aa35201-19.html

### 12. ACT DR6.02 maps

Grade: `DOCUMENTED — PARTIAL-SKY CMB SUPPORT PRODUCT`

The official ACT/LAMBDA release provides public DR6.02 maps in `enmap` FITS/WCS form plus map/covariance documentation and polarization convention guidance. These products are reproducible and their coordinate geometry is encoded in the WCS.

They are not full-sky low-multipole maps. ACT's independent instrument is useful for cross-checking scales and footprints it observes, but it cannot replace Planck for a claimed all-sky quadrupole/octupole axis.

Sources:

- https://act.princeton.edu/act-dr6-data-products
- https://lambda.gsfc.nasa.gov/product/act/act_dr6.02/
- https://lambda.gsfc.nasa.gov/product/act/act_dr6.02/act_dr6.02_maps_info.html
- https://lambda.gsfc.nasa.gov/product/about/pol_convention.html

### 13. SPT-3G D1 maps

Grade: `DOCUMENTED — PARTIAL-SKY CMB SUPPORT PRODUCT`

The public SPT-3G D1 release documents temperature/polarization maps, HEALPix products, sky footprint, and an IAU polarization convention. The mapmaking paper describes the equatorial coordinate frame and explicitly states use of the IAU convention.

The approximately 1,500-square-degree footprint and analysis range do not supply an independent full-sky low-multipole axis test.

Sources:

- https://lambda.gsfc.nasa.gov/product/spt/spt_3gd1/
- https://lambda.gsfc.nasa.gov/product/spt/spt_3gd1/README.html
- https://arxiv.org/pdf/2603.20163

## Existing analyses that set the honest prior

These are not all mutually consistent, which is precisely why catalogue construction and statistical method cannot be treated as implementation details.

1. Iye, Yagi & Fukumoto (2021) found an apparent dipole in an SDSS-derived catalogue before cleaning duplicate entries, but after cleaning and applying their stated local-redshift selection reported `sigma_D = 0.29` and concluded that the data were compatible with a random distribution. Source: https://arxiv.org/pdf/2011.00662
2. Patel & Desmond (MNRAS 2024; arXiv version revised 2025) collected all publicly available binary spin catalogues available to them, used Bayesian and frequentist low-multipole models, and found all analyses consistent with isotropy within 3 sigma. Source: https://arxiv.org/abs/2404.06617
3. Stiskalek & Desmond (2024) applied the same principled framework to the newer HSC DR3 spin catalogue and found decisive evidence for the isotropic model. Source: https://arxiv.org/abs/2410.18884
4. Planck Collaboration VII (2020) confirmed mild large-angle temperature anomalies while declining to claim an unambiguous cosmological anomaly in polarization. Source: https://www.aanda.org/articles/aa/full_html/2020/09/aa35201-19/aa35201-19.html

These papers do not “prove BHU false.” They show that the presently public, already-annotated galaxy spin data do not provide a robust anisotropy detection under the strongest recent reanalyses, and that CMB anomalies remain mild and non-unique.

## What can honestly be leveraged now

### Leverage now as an evidence constraint — YES

- Cite the independent HSC DR3 isotropy result instead of repeating it.
- Cite the Planck Collaboration's own anomaly/systematics assessment.
- Treat DESI DR1 spectroscopy as a documented support catalogue for future joins, not as a handedness measurement.
- Treat documented PA catalogues as possible orientation-alignment data only, never as spin chirality.

### Ready public BHU-discriminating analysis — NO

No named new catalogue simultaneously has:

1. a public frozen signed handedness field;
2. a primary documented sign/orientation mapping;
3. an independently audited mirror response;
4. independent instrument/footprint leverage;
5. a quantitative BHU prediction that makes a different forecast from competing explanations.

### Bounded future feasibility question — MAYBE, NOT AUTHORIZED HERE

A future public-data-only robustness join could ask whether already-published spin labels retain an isotropic result when matched to independently documented DESI DR1 spectroscopy. That would use existing labels and no new labelling. It would be a data-quality/redshift robustness study, not a unique BHU test, and it should not proceed until the exact spin-sign provenance and object-match manifest are frozen.

## CNN/mirroring conclusion

Duho's data-era hypothesis was worth checking. Modern classifiers do let us perform mirror tests we could not control in 2008. The provenance check does not reject that strategy in general.

It does reject the shortcut of treating current Zoobot catalogue outputs as handedness labels:

- their documented output trees contain arm tightness, not chirality;
- the DECaLS training pipeline uses random horizontal and vertical flips;
- mirror evaluation can test invariance and implementation bias, but cannot recover a directional target absent from the model;
- training a new directional head or creating new annotations would be a new study and conflicts with the present no-new-labelling boundary unless separately specified using already-frozen labels with recovered provenance.

So the reason GZ1 failed may indeed be data-era bookkeeping rather than physics, but the new products inspected here have not yet supplied a clean replacement signed observable.

## Required gate before any BHU study design

Before a study is proposed, both sides must be frozen:

1. Theory side: exact statistic, expected sign/amplitude or exclusion curve, redshift dependence, mask response, and what observation would count against the model.
2. Data side: immutable public product, row-selection manifest, duplicate policy, field dictionary, sky frame, handedness sign convention, mirror transform, and cross-survey match policy.
3. Analysis side: pre-registered null, look-elsewhere correction, mask-aware simulations, independent-survey replication, and blinded/global-sign handling.

Until then the honest state remains research scoping, not an uncompleted result waiting only for compute.

## Sextet custody

- Hwao: issued the survey order and prepared the preliminary synthesis/inventory.
- Lana: checked the theory-to-observable boundary and found no unique quantitative BHU statistic in the primary model papers she reviewed.
- Goru: enumerated modern data candidates and access/size/footprint considerations; Tori corrected two primary-documentation errors before synthesis (Galaxy Zoo `winding` meaning and DESI DR2 release status).
- Kun: supplied the adversarial systematics matrix, including WCS parity, label-swap, duplicate, footprint, and cross-instrument risks.
- Tori: applied this primary-documentation provenance gate and verified already-published analyses.
- Yui: held with no independent workstream, as ordered; no frozen-lane mutation occurred.

## Safety and authority receipt

No data analysis result was generated. No catalogue was modified. No labels were created. No provider/account action, DB write, wiki/publication write, cockpit write, video change, deploy/restart, Git action, or acceptance assertion occurred.

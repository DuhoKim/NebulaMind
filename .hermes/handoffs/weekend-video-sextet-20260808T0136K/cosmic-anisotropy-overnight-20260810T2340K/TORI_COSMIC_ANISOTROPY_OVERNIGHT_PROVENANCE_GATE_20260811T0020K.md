# Cosmic anisotropy beyond galaxy spin: public-data provenance gate

Marker: `TORI_COSMIC_ANISOTROPY_OVERNIGHT_PROVENANCE_GATE_20260811T0020K`

Authority: `HWAO_COSMIC_ANISOTROPY_OVERNIGHT_ORDER_20260810T2340K`, SHA-256 prefix `fa5be56dca69d965`.

Boundary: scope only; no data acquisition, estimator execution, anisotropy measurement, scientific result, lane unlock, video, publication, or acceptance.

Grades: `DOCUMENTED` means every named load-bearing field and convention was found in checked primary public documentation; `UNDOCUMENTED` names the missing item; `NOT-YET-CHECKED` is retained only when no primary-documentation check was completed.

## Gate outcome

- `QUAIA_V1_PUBLIC_PACKAGE`: `DOCUMENTED_CONDITIONAL_CORE`.
- `CATWISE2020_DERIVED_AGN_SAMPLE`: `UNDOCUMENTED_AS_CORE`.
- `NVSS_CATALOG`: `UNDOCUMENTED_AS_CORE_SUPPORT_ONLY`.
- `PANTHEON_PLUS`: `UNDOCUMENTED_FOR_DIRECTIONAL_TEST`.
- `COSMICFLOWS_4`: `UNDOCUMENTED_FOR_DIRECTIONAL_H0`.
- `FERMI_GBM_BURST_CATALOG`: `UNDOCUMENTED_FOR_ANGULAR_SELECTION`.
- `BATSE_4B`: `DOCUMENTED_CONDITIONAL_HISTORICAL_CONTROL`.
- `BOSS_DR12_LSS`: `DOCUMENTED_FOR_CATALOG_REPRODUCTION`; covariance faithfulness remains an analysis prior.
- `DESI_DR1_LRG_LSS_AND_PUBLISHED_4PCF_PRODUCTS`: `DOCUMENTED_FOR_PUBLISHED_REPRODUCTION`.
- `DESI_DR1_BAO_OR_FULL_SHAPE_VACS_AS_DIRECTIONAL_DE_INPUT`: `UNDOCUMENTED_FOR_ARBITRARY_SKY_DIRECTION_TEST`.
- No named candidate remains `NOT-YET-CHECKED`.

The provenance gate identifies Quaia as the only checked live-dispute candidate whose released package already contains a fixed catalog, public selection-function maps, public randoms, documented celestial coordinates, and public construction code.[1][3][58]

BATSE 4B also clears a narrower historical angular-clustering provenance gate because its fixed catalog, exposure table, efficiency table, and trigger-history table are public, but it is not a fresh unresolved probe.[30][33][34]

The absence of galaxy-morphology classification removes the exact chirality failure that stopped the spin lane, but it does not remove probe-specific selection functions, calibration gradients, exposure, covariance, or velocity-frame conventions.[10][22][33]

## 1. Quasar and radio number-count dipoles

### 1.1 Quaia v1.0 public package

**Selection and completeness — DOCUMENTED.**

The IRSA documentation says the final samples contain 1,295,502 objects at `G < 20.5` and 755,850 at `G < 20.0`, “with accompanying rigorous selection function models.”[4]

The fixed Zenodo v1.0.0 release contains both magnitude-cut catalogs, ten-times random catalogs, `NSIDE=64` selection-function maps, checksums, and template maps for dust, Gaia depth, Magellanic-Cloud structure, stellar density, unWISE depth, and unWISE scan coverage.[1]

The public repository names the scripts that construct tables, decontaminate the sample, compile the final catalogs, construct the selection function, and generate randoms, and it states that custom-selection-function and random instructions are in the corresponding files.[3]

**Coordinate frame and field meaning — DOCUMENTED.**

The primary IRSA dictionary defines `ra` and `dec` as ICRS 2016.0 coordinates and also publishes Galactic longitude and latitude, Gaia and unWISE identifiers, redshift estimates and uncertainties, magnitudes, and proper-motion quantities.[58]

**Flux-calibration provenance — DOCUMENTED AT CATALOG-PRODUCT LEVEL.**

The primary product identifies Gaia photometry, unWISE W1/W2 photometry, exact magnitude fields, source identifiers, and the construction code that maps the parent products into the frozen catalog.[3][58]

This gate does not certify the parent Gaia and unWISE instrument calibration from first principles; it certifies that the released selection function directly measures their realized sky-dependent imprint for the frozen Quaia sample.[1][3]

**Exact kinematic convention — DOCUMENTED, BUT MUST BE FROZEN AS AN ANALYSIS CHOICE.**

The checked Quaia dipole analysis uses the Ellis–Baldwin convention `D = [2 + x(1 + alpha)] v/c`, defines `N(>S) proportional to S^-x` and `S proportional to nu^-alpha`, and uses the CMB velocity `369.82 +/- 0.11 km/s` toward Galactic `(l,b)=(264.021 deg,48.253 deg)`.[9]

That paper also states the load-bearing assumptions: no directional completeness bias above the threshold and no redshift dependence in `x` or `alpha`; a future brief must therefore freeze how `x` and `alpha` are measured, whether they vary with redshift, the vector sign, and whether the kinematic component is subtracted from a map or compared in a joint posterior.[9]

A newer joint radio/quasar treatment emphasizes that the expected kinematic matter dipole scales with observed sample properties, so the classical convention is not a dataset constant that can be copied without remeasurement.[13]

**Overall — `DOCUMENTED_CONDITIONAL_CORE`.**

Condition: use the checksum-pinned Zenodo v1.0 package and its released selection-function/random products rather than an ad hoc IRSA query alone, and freeze the kinematic convention before any design commitment.[1][9]

### 1.2 CatWISE2020-derived AGN sample

**Raw fields — DOCUMENTED.**

The CatWISE2020 primary dictionary publishes positions, motions, W1/W2 photometry, fluxes, uncertainties, artifact flags, frame counts, and fit-quality fields.[7]

**Derived sample and mask — PARTLY DOCUMENTED.**

The original study describes a custom 1.36-million-source flux-limited sample, its magnitude cuts and masks, and reports a dipole amplitude more than twice its canonical kinematic expectation.[5]

A later reanalysis confirms a significant ecliptic-latitude gradient but finds unexpected low-order multipoles and strong mask-induced mode coupling, concluding that the dipole uncertainty cannot be trusted until those fluctuations are understood.[10]

**Missing — `UNDOCUMENTED`.**

No checked primary release supplies a frozen object-row list plus a pixelized inclusion probability or random catalog that jointly encodes the derived AGN selection, ecliptic correction, Galactic mask, stellar contamination, and mode coupling.[5][10]

The exact kinematic equation is published, but its sample-specific count slope, spectral index, threshold, mask, vector sign, and map-versus-posterior treatment are not a single frozen public subtraction product.[5][9]

**Overall — `UNDOCUMENTED_AS_CORE`.**

The dominant selection systematic is visible in public data and published analyses, but the corrected inclusion probability needed to distinguish sky density from selection is not a frozen public product.[10]

### 1.3 NVSS

**Catalog and coordinates — DOCUMENTED.**

The official catalog covers 82 percent of the sky north of J2000 declination `-40 deg`, contains about two million sources above roughly `2.5 mJy`, and publishes J2000 positions, 1.4-GHz flux information, image products, and sensitivity characteristics.[11]

**Kinematic convention — DOCUMENTED AS A FORMULA, NOT AS A FROZEN SUBTRACTION.**

Current work explicitly treats the NVSS expected kinematic dipole as sample dependent and jointly separates a CMB-fixed kinematic component from a residual component.[13]

**Missing — `UNDOCUMENTED`.**

The checked official release does not provide a pixelized probability-of-inclusion map or random catalog that freezes declination-dependent completeness, flux-calibration variation, Galactic masking, multi-component source consolidation, and the final dipole-analysis threshold.[11]

The published radio and quasar samples are independent and share no objects, so NVSS remains a useful instrument-family cross-check, but independence does not fill the missing selection map.[14]

**Overall — `UNDOCUMENTED_AS_CORE_SUPPORT_ONLY`.**

## 2. SN Ia and directional H0

### 2.1 Pantheon+

**Object, redshift, calibration, and covariance fields — DOCUMENTED.**

Pantheon+ releases 1,701 light curves of 1,550 unique spectroscopically confirmed SNe Ia compiled from 18 surveys and explicitly reviews redshifts, peculiar velocities, photometric calibration, and intrinsic-scatter models.[20]

The distance release defines duplicate-SN handling, `zHEL`, `zHD`, `m_b_corr`, total and statistical covariance matrices, and separate covariance products for calibration, peculiar-velocity, redshift-shift, bias-correction, mass-step, intrinsic-scatter, and spectroscopic-efficiency systematics.[22]

The calibration release publishes zeropoints and cross-calibration archives, including the Fragilistic solution and alternate products.[23]

**Missing for a directional test — `UNDOCUMENTED`.**

The checked public distance dictionary labels `RA` and `DEC` but does not state their exact frame and epoch, and the release does not provide per-survey sky-footprint probability, epoch-dependent cadence/exposure, or a sky map of residual calibration completeness.[22]

A covariance matrix measures the released uncertainty model, but it is not direct public measurement of any omitted sky-dependent selection or calibration mode.[22]

The release defines heliocentric and Hubble-diagram redshift products, but a directional-H0 brief would still have to freeze the exact observer-velocity vector, velocity-field realization, redshift-cut rule, and whether residual peculiar velocities are marginalized or subtracted.[22]

**Overall — `UNDOCUMENTED_FOR_DIRECTIONAL_TEST`.**

The dominant low-redshift velocity and heterogeneous-survey selection effects are partly represented publicly, but their full directional transfer function is not measurable from the released table and covariance alone.[20][22]

### 2.2 Cosmicflows-4

**Catalog fields and corrected-release provenance — DOCUMENTED.**

The public archive warns that the initial Cosmicflows-4 tables were flawed and points users to corrected versions, making release identity a load-bearing provenance requirement.[51]

The VizieR release documents 55,877 galaxy distances grouped into 38,065 systems, eight distance methodologies, public download interfaces, and a strongly heterogeneous sky composition including ALFALFA, SDSS, WISE, FP, TF, SN, Cepheid, and TRGB inputs.[55]

**Dominant directional systematic — `UNDOCUMENTED`.**

No checked primary release supplies one unified angular selection probability covering all eight methods, their different sky footprints, group construction, zero-point links, and Malmquist corrections.[51][55]

Published analyses already test anisotropic expansion with public distance indicators, while a later public analysis reports no evidence for local H0 anisotropy from Tully–Fisher or supernova distances after explicit quality and Galactic-latitude cuts.[53][54]

**Overall — `UNDOCUMENTED_FOR_DIRECTIONAL_H0`.**

The source-level measurements are public, but the dominant heterogeneous directional selection prior is not one public measurable transfer function.[55]

## 3. GRB angular clustering

### 3.1 Fermi GBM Burst Catalog

**Coordinates, localization, and burst quantities — DOCUMENTED.**

The official GBM catalog defines burst position, localization error, trigger time, durations, fluences, peak fluxes, spectral fits, data-processing version, and related fields.[26]

**Selection and exposure — `UNDOCUMENTED`.**

The official catalog states that burst-catalog analysis requires human intervention to distinguish GRBs from solar flares, soft gamma repeaters, terrestrial gamma-ray flashes, and accidental triggers.[26]

The checked official public-products listing exposes trigger, daily, continuous, and response data but does not identify a fixed full-mission all-sky GRB inclusion-probability map combining pointing, Earth occultation, South Atlantic Anomaly downtime, changing trigger algorithms and thresholds, spectral response, human classification, and localization quality.[28]

**Kinematic subtraction — NOT APPLICABLE TO THE REQUESTED CLUSTERING TEST.**

A pure exposure-corrected angular-clustering test need not subtract the CMB kinematic number-count dipole; any dedicated GRB dipole design would require a separately frozen Compton–Getting/selection-response convention.

**Overall — `UNDOCUMENTED_FOR_ANGULAR_SELECTION`.**

The dominant sky-exposure and trigger/classification selection function is not a checked public fixed product, so source positions alone are not design-ready.[26][28]

### 3.2 BATSE 4B

**Fixed catalog, coordinate frame, exposure, efficiency, and thresholds — DOCUMENTED.**

The fixed 4B catalog contains 1,637 triggered events and publishes J2000 positions and position uncertainties.[30][32]

The public exposure table gives the detectable-time fraction by declination and accounts for Earth blockage, South Atlantic Anomaly passages, disabled-trigger intervals, and readout intervals; it also publishes equatorial and Galactic exposure moments and an estimated exposure uncertainty.[33]

The separate public efficiency table gives trigger efficiency as a function of peak flux, and the threshold-history table records dates, energy ranges, timescales, and sigma thresholds.[34][35]

**Known limits — DOCUMENTED.**

The exposure documentation says atmospheric scattering and telemetry-gap handling were still being improved and estimates exposure-fraction uncertainty at about four percent.[33]

**Kinematic subtraction — NOT APPLICABLE TO A CLUSTERING-ONLY REPRODUCTION.**

A clustering-only reproduction can use the public exposure function and efficiency; a new GRB dipole claim would still require a predeclared Compton–Getting convention and energy/fluence-slope response not supplied as a catalog field.[33][34]

**Overall — `DOCUMENTED_CONDITIONAL_HISTORICAL_CONTROL`.**

Condition: reproduce the already-published BATSE angular test with the released exposure, efficiency, and threshold products rather than treat 4B as a new all-sky claim engine.[31][33][35]

## 4. Galaxy-survey parity-odd four-point functions

### 4.1 BOSS DR12 LSS

**Selection, masks, weights, coordinates, and randoms — DOCUMENTED FOR REPRODUCTION.**

The official DR12 LSS release provides CMASS and LOWZ catalogs, angular masks, random catalogs, sector completeness, redshifts, FKP weights, fiber-collision weights, redshift-failure weights, stellar and seeing systematic weights, sky flux, airmass, imaging depth, and reddening.[36][46]

The random catalog publishes positions, mask polygon and sector identifiers, random redshifts drawn from the data, FKP weights, density, and imaging-systematic fields.[47]

The checked LSS field page says only “Right Ascension” and “Declination” rather than stating an epoch, but the parity statistic is reproduced from the authors' released coordinate-conversion and estimator code rather than by inventing a new frame convention.[46][48]

**Claim and contest — PUBLISHED.**

The original BOSS analysis reported a 99.6 percent rank-test detection probability and explicitly allowed either cosmological parity violation or systematics, including possible mismatch between simulations and BOSS statistical properties.[39]

A subsequent public reanalysis reports no compelling evidence after covariance treatment changes and supplies reproduction code and data products.[40][48]

**Dominant systematic — PARTLY MEASURABLE, PARTLY A MODEL PRIOR.**

Survey geometry and object-selection effects are measurable from public masks, randoms, weights, and imaging fields, but the faithfulness of finite mocks or analytic covariance to the true high-dimensional 4PCF distribution is not itself established by the object catalog.[36][40][46]

**Overall — `DOCUMENTED_FOR_CATALOG_REPRODUCTION`.**

No kinematic-dipole subtraction is part of this parity-odd 4PCF observable.[39]

### 4.2 DESI DR1 LRG LSS and published 4PCF products

**Catalog provenance — DOCUMENTED FOR REPRODUCTION.**

The DESI DR1 release publishes LSS catalogs and mock catalogs, and its data model defines full and clustering catalogs, randoms, completeness, fiber-assignment, redshift-failure, FKP, and imaging-systematics weights.[41][43]

The published DESI analysis applies survey-geometry correction with randoms and default completeness, systematic, and redshift-failure weights.[44]

The public derived-product archive contains NGC and SGC data vectors, mock vectors, odd-parity statistics, and checksums.[45]

**Current published outcome — NO UNRESOLVED DATASET CLAIM TO RE-RUN.**

The DESI DR1 LRG paper reports the parity-odd signal as consistent with zero while warning that low sample completeness may reduce sensitivity.[44][60]

**Overall — `DOCUMENTED_FOR_PUBLISHED_REPRODUCTION`.**

The remaining sensitivity/covariance limitation is already stated by the primary analysis, so provenance does not justify treating the same release as an unanswered parity claim.[44]

No kinematic-dipole subtraction is part of this parity-odd 4PCF observable.[44]

## 5. Directional dark-energy products

**Standard DESI products — DOCUMENTED FOR STANDARD BAO/FULL-SHAPE USE.**

The DR1 value-added releases publish BAO cosmological-parameter chains and full-shape-plus-BAO clustering data vectors, covariance matrices, likelihood assets, and sample definitions.[56][57]

**Arbitrary sky-direction observable — `UNDOCUMENTED`.**

The checked value-added products are organized by tracer, redshift bin, and standard clustering statistic rather than by a frozen arbitrary sky-direction dark-energy dipole with region-level covariance and selection transfer functions.[56][57]

**Overall — `UNDOCUMENTED_FOR_ARBITRARY_SKY_DIRECTION_TEST`.**

No exact kinematic-dipole subtraction convention is defined because the checked standard BAO and full-shape products do not instantiate that directional observable.[56][57]

## 6. Design-commitment boundary

The provenance result supports taking Quaia to a separate design brief because its dominant angular selection systematic is represented by released selection maps and randoms, and its load-bearing coordinate and kinematic conventions can be frozen from primary public documentation.[1][9][58]

This is a provenance finding, not Tori's cross-probe recommendation; Hwao retains the one-probe recommendation after integrating Lana, Kun, Goru, and other lane reviews.

No candidate is cleared to run, and no result, claim, video, publication, lane unlock, or acceptance follows from this gate.

## Sources

[1] https://zenodo.org/records/10403370
[3] https://raw.githubusercontent.com/kstoreyf/gaia-quasars-lss/main/README.md
[4] https://irsa.ipac.caltech.edu/data/Quaia/overview.html
[5] https://arxiv.org/pdf/2009.14826
[7] https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html
[9] https://arxiv.org/html/2311.14938v2
[10] https://arxiv.org/html/2405.09762v2
[11] https://heasarc.gsfc.nasa.gov/w3browse/all/nvss.html
[13] https://arxiv.org/html/2503.02470v1
[14] https://arxiv.org/pdf/2206.05624
[20] https://arxiv.org/pdf/2112.03863
[22] https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon+_Data/4_DISTANCES_AND_COVAR/README
[23] https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon+_Data/2_CALIBRATION/README
[26] https://heasarc.gsfc.nasa.gov/w3browse/fermi/fermigbrst.html
[28] https://fermi.gsfc.nasa.gov/ssc/data/access/data_products.html
[30] https://heasarc.gsfc.nasa.gov/w3browse/cgro/batse4b.html
[31] https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b
[32] https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_basic.html
[33] https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_exposure.html
[34] https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_efficiency.html
[35] https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_trigger_criteria.html
[36] https://www.sdss4.org/dr17/spectro/lss
[39] https://arxiv.org/pdf/2206.04227
[40] https://arxiv.org/html/2407.03397v1
[41] https://data.desi.lbl.gov/doc/releases/dr1
[43] https://desidatamodel.readthedocs.io/en/25.3/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSIONpip/data_full_pip.html
[44] https://link.aps.org/doi/10.1103/2dmd-hyt1
[45] https://zenodo.org/records/17753485
[46] https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/galaxy_DRX_SAMPLE_NS.html
[47] https://data.sdss.org/datamodel/files/BOSS_LSS_REDUX/randomN_DRX_SAMPLE_NS.html
[48] https://zenodo.org/records/12537418
[51] http://edd.ifa.hawaii.edu
[53] https://arxiv.org/html/2412.14607
[54] https://arxiv.org/html/2509.14997
[55] https://cdsarc.cds.unistra.fr/viz-bin/cat/J/ApJ/944/94
[56] https://data.desi.lbl.gov/doc/releases/dr1/vac/bao-cosmo-params
[57] https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-bao-clustering
[58] https://irsa.ipac.caltech.edu/data/Quaia/docs/quaia_colDescriptions.html
[60] https://arxiv.org/abs/2512.20132

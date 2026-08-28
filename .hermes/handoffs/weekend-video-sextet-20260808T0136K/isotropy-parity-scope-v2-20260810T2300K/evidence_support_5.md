URL: https://data.desi.lbl.gov/doc/releases/dr1

[Skip to content](https://data.desi.lbl.gov/doc/releases/dr1/#data-release-1-dr1)

# Data Release 1 (DR1) [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#data-release-1-dr1 "Permanent link")

## Overview [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#overview "Permanent link")

DESI Data Release 1 (DR1) includes spectra for more than 18 million unique
targets from [Main Survey](https://data.desi.lbl.gov/doc/glossary/#main-survey) observations taken
between May 2021 and June 2022. In addition, DR1 includes all the data taken as
part of DESI [Survey Validation](https://data.desi.lbl.gov/doc/glossary/#survey-validation) which was
originally released as part of the [Early Data Release](https://data.desi.lbl.gov/doc/releases/edr/) but reprocessed
with the same reduction pipeline as the Main Survey data.

The DR1 data are released under the [Creative Commons Attribution 4.0\\
International License](https://creativecommons.org/licenses/by/4.0/) (CC BY
4.0). Use of DESI data requires including the citation and acknowledgment text
given on the [Data License and Acknowledgments](https://data.desi.lbl.gov/doc/acknowledgments/) page.

**Data URL**: [https://data.desi.lbl.gov/public/dr1](https://data.desi.lbl.gov/public/dr1)

**European mirror URL**: [https://webdav-hdfs.pic.es/data/public/DESI/DR1](https://webdav-hdfs.pic.es/data/public/DESI/DR1)

**Paper**: [DESI Collaboration _et al._ (2026)](https://ui.adsabs.harvard.edu/abs/2026AJ....171..285D/abstract), _Data Release 1 of the Dark Energy Spectroscopic Instrument_

**Cosmology Results**: [DESI Key Project Papers using DR1](https://data.desi.lbl.gov/doc/papers/dr1/)

For an overview of how DESI data are organized see [Data Organization](https://data.desi.lbl.gov/doc/organization/), and see [Data Access](https://data.desi.lbl.gov/doc/access/) for how to access the data.

### Coverage area [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#coverage-area "Permanent link")

The figure below shows the progress of DESI [Main\\
survey](https://data.desi.lbl.gov/doc/glossary/#main-survey) observations through 2022 June 13. Dark
green areas are complete or close to completeness, while white areas have not
yet been started. The thick solid contours enclose the DESI footprint, the thin
solid line shows the Galactic plane, and the thin solid contour shows the
footprint of the [Dark Energy Survey](https://www.darkenergysurvey.org/). Backup tiles observing bright stars extend beyond the core DESI footprint.

![DR1_progress](https://data.desi.lbl.gov/doc/img/dr1_sky_coverage.png)

### Summary statistics [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#summary-statistics "Permanent link")

\| Summary of DR1 (Iron) \|\|
\| \- \| -: \|
\| \*\*Main Survey\*\* \|\|
\| Number of useful(1) spectra \| 18,659,804 \|
\| Galaxies (\`SPECTYPE==GALAXY\`) \| 13,049,402 \|
\| Quasars (\`SPECTYPE==QSO\`) \| 1,553,713 \|
\| Stars (\`SPECTYPE==STAR\`) \| 4,056,689 \|
\| \*\*Special Observations\*\* \|\|
\| Number of useful(1) spectra \| 141,473 \|
\| Galaxies (\`SPECTYPE==GALAXY\`) \| 83,961 \|
\| Quasars (\`SPECTYPE==QSO\`) \| 3,624 \|
\| Stars (\`SPECTYPE==STAR\`) \| 53,888 \|
\| \*\*Commissioning & Survey Validation\*\* \|\|
\| Number of useful(1) spectra \| 1,613,846 \|
\| Galaxies (\`SPECTYPE==GALAXY\`) \| 1,046,508 \|
\| Quasars (\`SPECTYPE==QSO\`) \| 88,505 \|
\| Stars (\`SPECTYPE==STAR\`) \| 478,833 \|
\| \*\*DESI Instrument\*\* \|\|
\| Spectral coverage(2) \| 360--982.4 nm \|
\| Spectral resolution \| 2000 (at 360 nm) -- 5500 (at 980 nm) \|
\| Wavelength system \| vacuum barycentric \|
\| Photometric bands (Legacy Surveys DR9) \| \*g\*, \*r\*, \*z\*, \*W\*1, \*W\*2, \*W\*3, \*W\*4 \|
\| \*\*Approximate area\*\* \| \|
\| Main Survey / Backup \| 2,726 sq. deg. \|
\| Main Survey / Bright \| 9,739 sq. deg. \|
\| Main Survey / Dark \| 9,528 sq. deg. \|

**Footnotes:**

1. “Useful spectra” are defined as having `ZCAT_PRIMARY==True`,
    `OBJTYPE=='TGT'`, and `ZWARN==0`, which selects all unique, non-sky targets with no known redshift-fitting failures. The Main Survey additionally excludes `PROGRAM=='other'`. See [dr1paper notebook](https://github.com/desihub/dr1paper/blob/main/nb/count-dr1-targets.ipynb).
2. Spectra are split on three spectrograph arms: blue (B), red (R), infrared (Z).

### Redshift distributions [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#redshift-distributions "Permanent link")

The following shows the number of good, unique target redshifts as a function of
redshift for each tracer type: [ELG](https://data.desi.lbl.gov/doc/glossary/#elg) (blue),
[LRG](https://data.desi.lbl.gov/doc/glossary/#lrg) (red), [BGS](https://data.desi.lbl.gov/doc/glossary/#bgs) (purple), and
[QSO](https://data.desi.lbl.gov/doc/glossary/#qso) (green). Stars are shown in the top panel. The gray
histograms (e.g. STAR\*, GALAXY\*, QSO\*) include _all_ objects of a given
`SPECTYPE` classification, regardless of their target type; these histograms
differ slightly from the color histograms because of secondary targets and other
target types that were classified to a different category (e.g. a QSO target
that was classified as a star).

![DR1 n(z)](https://data.desi.lbl.gov/doc/img/dr1_z_distribution.png)

## Large-Scale Structure Catalogs [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#large-scale-structure-catalogs "Permanent link")

DESI produces Large-Scale Structure (LSS) catalogs specifically designed for cosmological clustering measurements. These catalogs are thoroughly documented in [Ross et al. 2025](https://inspirehep.net/literature/2790563), with DR1-specific details available in [this paper](https://inspirehep.net/literature/2850031).

The publicly available DR1 catalogs can be found at:

- [https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.2/](https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.2/)
- [https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/](https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/)

See Appendix B of [this paper](https://inspirehep.net/literature/2850031) for a detailed description of the differences between versions.

For most scientific analyses, we recommend using the files with `clustering` in their names, as these contain the final products optimized for clustering measurements. These catalogs can also be accessed through [CosmoHub](https://cosmohub.pic.es/), that allows for interactive exploration, plotting and subsetting.

For details on the file organization structure of LSS catalogs, see the [data organization documentation](https://data.desi.lbl.gov/doc/organization/#large-scale-structure-catalogs). For complete specifications of file formats and contents, consult the [DESI data model](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/index.html).

## LSS Mock Catalogs [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#lss-mock-catalogs "Permanent link")

Together with the DR1 LSS release, DESI releases mock catalogs used to validate analyses and estimate covariance matrices for both dark and bright tracers. More details are found in [DESI 2024 II (2025)](https://iopscience.iop.org/article/10.1088/1475-7516/2025/07/017).

We make public two distinct mock datasets:

- 1000 EZmocks: low-resolution realizations used to estimate covariance matrices.
- 25 AbacusSummit: high-resolution N-body simulation realizations for validation, with different levels of realism.

Data can be found at: [https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/mocks](https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/mocks).

In a best effort, we try to keep the same file organization and catalog structure as the LSS catalogs. For complete specifications of file formats and contents, consult the [MOCK DESI data model](https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/mocks/index.html).

## Value-added Catalogs [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#value-added-catalogs "Permanent link")

The DESI science collaboration has generated a set of value-added catalogs
(VACs) to accompany Data Release 1. These catalogs provide curated subsets of
data with additional analysis beyond the core spectroscopic data processing
pipeline outputs.

\### General VACs
\| Name \| Description \|
\| \- \| -: \|
\| \[Legacy Surveys DR9 Photometric Catalog\](vac/lsdr9-photometry.md) \| Merged targeting catalogs and \`Tractor\` catalog photometry from the \[LS/DR9\](https://www.legacysurvey.org/dr9/description/){: target='\_blank'} for all observed and potential DESI targets. \|
\| \[Sky Spectra Year 1 Catalog\](vac/skyspec.md) \| Exemplar sky spectra with detailed metadata from the DESI pipeline. \|
\| \[BAO cosmology results\](vac/bao-cosmo-params.md) \| Cosmology chains and posterior maximization results for the DESI DR1 BAO cosmology results. \|
\| \[Full shape cosmology results\](vac/full-shape-cosmo-params.md) \| Cosmology chains and posterior maximization results for the DESI DR1 full shape analysis results. \|
\| \[Full shape BAO clustering\](vac/full-shape-bao-clustering.md) \| Clustering measurements (power spectrum, correlation function, window matrix, covariance matrix) for the DESI DR1 Full Shape and BAO analyses. \|

\### Milky Way Survey (MWS)
\| Name \| Description \|
\| \- \| -: \|
\| \[MWS Catalog\](vac/mws.md) \| Analysis of stellar spectra by the MWS Working Group \|
\| \[MWS Blue Horizontal Branch Catalog\](vac/mws-bhb.md) \| Catalog of spectroscopically confirmed blue horizontal branch (BHB) stars \|
\| \[MWS SpecDis Catalog\](vac/mws-specdis.md) \| Spectrophotometric distances for approx. 4 million stars in DR1 predicted using a neural network trained on stellar spectra \|
\| \[SPDist Catalog\](vac/mws-spdist.md) \| Spectrophotometric distances for all stars observed by the MWS predicted using a multi-layer perceptron trained on a selection of stellar parameters. \|
\| \[Stellar Reddening\](vac/stellar-reddening.md) \| Spectra and catalog of stars used in dust reddening measurements \|

\### Extragalactic Science
\| Name \| Description \|
\| \- \| -: \|
\| \[DESI HETDEX Catalog\](vac/hetdex.md) \| HETDEX and DESI spectra for Hobby-Eberly Telescope Dark Energy Experiment (HETDEX) Lyα emitter candidates observed by DESI \|
\| \[DESIVAST VAC\](vac/desivast.md) \| Cosmic voids identified within the DESI DR1 volume \|
\| \[Dwarf Galaxy Catalog\](vac/extragalactic-dwarfs.md) \| Extragalactic dwarf galaxies identified in DESI DR1. \|
\| \[EMFit Catalog\](vac/emfit.md) \| Emission-line fitting results for z ≤ 0.45 galaxies \|
\| \[FastSpecFit Spectral Synthesis and Emission-Line Catalog\](vac/fastspecfit.md) \| Spectrophotometric fitting results from the \`FastSpecFit\` stellar continuum and emission-line modeling code. \|
\| \[FastPhot Spectral Synthesis Catalog\](vac/fastphot.md) \| Photometric fitting results from the \`FastSpecFit\` stellar continuum modeling code. \|
\| \[Extended Halo-based Group Catalog\](vac/gfinder.md) \| Halo-based group catalog based on Legacy Surveys DR9 for z-band apparent magnitude z < 21 galaxies. \|
\| \[Mass EMLines\](vac/stellar-mass-emline.md) \| Stellar mass and emission line measurements for galaxies in DR1 \|
\| \[Strong Lensing Catalog\](vac/strong-lensing.md) \| Catalog of spectroscopic observations of strong lenses observed in DESI DR1 \|

\### Quasar Science
\| Name \| Description \|
\| \- \| -: \|
\| \[AGN/Galaxy Classification Catalog\](vac/agngal.md) \| AGN and QSO identification for galaxies from all target classes in DESI DR1 (formerly named AGN/QSO) \|
\| \[AGN Host Properties\](vac/cigale.md) \|

Stellar masses and other physical properties from spectral energy distribution modeling which includes AGN templates \|
\| \[BHMass Catalog\](vac/qmassiron.md) \| Iron-corrected supermassive black hole masses based on Mg II at 0.6 < z < 1.6 \|
\| \[DLA NN and GP Finder Catalog\](vac/dla-cnn-gp.md) \| DLA parameters and detections using the NN and GP DLA finders \|
\| \[DLA Template Finder Catalog\](vac/dla-toolkit.md) \| DLA parameters and detections using DLA Toolkit \|
\| \[CIV Absorber Catalog\](vac/civ-absorber.md) \| Catalog of CIV absorber systems in DESI quasars \|
\| \[Mg II Absorber Catalog\](vac/mgii-absorber.md) \| Summarized information of Mg II absorption systems in DESI quasars \|
\| \[ZLyA Catalog\](vac/zlya.md) \| Updated redshifts and BAL information used in the Lyα Y1 BAO analysis \|

\### Lyα Forest
\| Name \| Description \|
\| \- \| -: \|
\| \[Lyα Forest Year 1 Deltas\](vac/lya-deltas.md) \| Measured flux-transmission field used in the Lyα Y1 BAO analysis \|
\| \[Lyα Forest Year 1 Correlations\](vac/lya-correlations.md) \| Measured correlations, distortion matrices and covariances used for the Lyα Y1 BAO analysis \|

## Known Issues [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#known-issues "Permanent link")

Known issues with Data Release 1 are documented [here](https://data.desi.lbl.gov/doc/releases/dr1/known-issues/).

## Software Package Versions [¶](https://data.desi.lbl.gov/doc/releases/dr1/\#software-package-versions "Permanent link")

The versions of DESI software packages used for the Data Release 1 are available [here](https://data.desi.lbl.gov/doc/releases/dr1/software-version/).

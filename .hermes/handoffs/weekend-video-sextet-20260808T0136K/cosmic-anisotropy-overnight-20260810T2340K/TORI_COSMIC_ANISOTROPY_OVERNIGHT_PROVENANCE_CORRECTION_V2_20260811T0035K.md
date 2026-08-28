# Cosmic anisotropy beyond galaxy spin: post-delegation provenance correction v2

Marker: `TORI_COSMIC_ANISOTROPY_OVERNIGHT_PROVENANCE_CORRECTION_V2_20260811T0035K`

Authority: `HWAO_COSMIC_ANISOTROPY_OVERNIGHT_ORDER_20260810T2340K`, SHA-256 `fa5be56dca69d965aafd10c430d451544e2ba5e31cb2858660bcd40ce19b0494`.

This append-only correction supersedes Tori's `TORI_COSMIC_ANISOTROPY_OVERNIGHT_PROVENANCE_GATE_20260811T0020K.md` and receipt `TORI_TO_HWAO_COSMIC_ANISOTROPY_OVERNIGHT_PROVENANCE_RECEIPT_20260811T0029K.md`; those files remain preserved as non-authoritative evidence of the first pass.

Boundary: scope and provenance only; no data acquisition, estimator execution, anisotropy result, scientific claim, lane unlock, video, publication, or acceptance.

## Why a correction was required

The completed independent documentation fan-out found primary public products that Tori's first pass had missed: the Secrest CatWISE v3 dataset/mask/code release, explicit NVSS completeness and dipole-selection documentation, and Pantheon+ J2000 coordinate documentation.[1][7][21]

It also found the fixed Fermi ten-year catalog and exact BOSS/DESI release caveats.[5]

The correction changes four overall grades, narrows three missing-item lists, and leaves the provenance-side Quaia recommendation conditional rather than unqualified.

## Superseding grade matrix

- `QUAIA_V1_PUBLIC_PACKAGE`: `DOCUMENTED_CONDITIONAL_CORE`; row-level upstream artifact/quality flags remain `UNDOCUMENTED`.

- `CATWISE_SECREST_V3_PACKAGE`: `DOCUMENTED_CONDITIONAL_RECONSTRUCTION`; this supersedes `UNDOCUMENTED_AS_CORE`.

- `NVSS_DIPLOE_RECONSTRUCTION`: `DOCUMENTED_CONDITIONAL_RECONSTRUCTION_SUPPORT`; this supersedes `UNDOCUMENTED_AS_CORE_SUPPORT_ONLY`.

- `PANTHEON_PLUS_DIRECTIONAL_TEST`: `UNDOCUMENTED_FOR_DIRECTIONAL_TEST`; coordinates are corrected to `DOCUMENTED`, while release identity and angular completeness remain `UNDOCUMENTED`.

- `COSMICFLOWS_4_DIRECTIONAL_H0`: `UNDOCUMENTED_FOR_DIRECTIONAL_H0`; unchanged overall.

- `FERMI_GBM_10_YEAR_ANGULAR_TEST`: `UNDOCUMENTED_FOR_ANGULAR_SELECTION`; fixed-release identity is corrected to `DOCUMENTED`, while exposure and joint completeness remain `UNDOCUMENTED`.

- `BATSE_4BR_EXACT_CATALOG_WIDE_TEST`: `UNDOCUMENTED_FOR_EXACT_JOINT_SELECTION`; a bright-burst historical control remains conditionally reconstructable.

- `BOSS_DR12_4PCF`: `DOCUMENTED_FOR_CATALOG_RECONSTRUCTION_BUT_UNDOCUMENTED_FINAL_COVARIANCE`.

- `DESI_DR1_PUBLISHED_4PCF`: `UNDOCUMENTED_FOR_EXACT_PUBLISHED_REPRODUCTION`; this supersedes `DOCUMENTED_FOR_PUBLISHED_REPRODUCTION`.
- `DESI_DR1_DIRECTIONAL_DE_FROM_STANDARD_VACS`: `UNDOCUMENTED_FOR_ARBITRARY_SKY_DIRECTION_TEST`; unchanged overall.
- No named candidate remains `NOT-YET-CHECKED`.

## 1. Quaia correction

The Quaia release identity, selection equations, ICRS 2016.0 coordinates, public selection maps, random catalogs, construction code, and likelihood-form kinematic convention remain documented.[3]

The primary catalog paper says the release starts from the full Gaia quasar-candidate sample rather than cutting on other Gaia pipeline flags, and the released schema does not carry row-level Gaia/unWISE artifact or processing-warning bits.[3]

Corrected missing item: a row-level retained/rejected artifact-flag policy and upstream warning-bit audit trail are `UNDOCUMENTED`.[3]

Superseding overall grade: `DOCUMENTED_CONDITIONAL_CORE`, with a future brief required to test whether sky counts or selection residuals depend on recoverable upstream quality flags and to fail closed if that sensitivity cannot be bounded.[3]

## 2. CatWISE Secrest v3 correction

The first pass incorrectly said that no frozen derived dataset, mask, or code product existed.

Zenodo record 8303800 is a versioned v3 public release containing the derived AGN FITS file, `MASKS_exclude_master_final.fits`, and generation code associated with the primary analysis.[1]

The release explicitly says the stored FITS sample extends to `W1 < 16.5` while the final published result applies `W1 < 16.4`, so reproducing the exact row set requires one documented additional cut.[1]

The primary paper documents valid W1/W2 measurements, `W1-W2 >= 0.8`, `9 < W1 < 16.4`, Galactic and geometric masks, low-coverage removal, extinction correction, and the ecliptic-latitude correction used in the analysis.[2]

The upstream CatWISE catalog requires a same-band signal-to-noise threshold and no identified artifacts in the corresponding `ab_flags` character, but the derived v3 package does not fully document whether `ab_flags`, `cc_flags`, or related per-source flags were retained or additionally filtered.[20]

Corrected missing items: complete derived-FITS schema, explicit per-source artifact-flag handling, and an immutable manifest of the final `W1 < 16.4` rows after applying the documented cut.[1][20]

Superseding overall grade: `DOCUMENTED_CONDITIONAL_RECONSTRUCTION`, not `UNDOCUMENTED_AS_CORE`.[1][2]

The released mask and correction code make the dominant stated selection systematic measurable from public data, although published unexplained residual multipoles remain a scientific/systematics reason not to prefer this sample over Quaia.[1][2]

## 3. NVSS correction

The first pass overstated the consequence of there being no pixelized random catalog.

The official DR12-era NVSS documentation and primary dipole chain define J2000 coordinates, the parent peak threshold, the `15 mJy` analysis threshold, the Galactic mask, local-galaxy removal, catalog completeness, clean bias, and intensity-proportional calibration uncertainty.[7]

The exact kinematic null is documented through the Ellis–Baldwin formula, assumed count slope, spectral index, CMB speed/direction, and Monte Carlo comparison rather than vector subtraction.[7]

Corrected missing items: no semantic release version or checksum for the official source table, no immutable standalone release of the selected row set and masks, and no statement that residual or unresolved-axis flags were filtered.[7]

Superseding overall grade: `DOCUMENTED_CONDITIONAL_RECONSTRUCTION_SUPPORT`, with byte-pinning and an explicit fit-flag policy required before design.[6][7]

## 4. Pantheon+ correction

The first pass incorrectly treated the exact RA/DEC frame as undocumented.

The primary redshift/coordinate paper labels SN and host coordinates in degrees J2000, so the directional coordinate frame is `DOCUMENTED`.[21]

Pantheon+'s GitHub release page says there are no releases, while the repository identifies the Pantheon+ and SH0ES directories; a reproducible brief must therefore pin a commit and file checksums rather than cite an unversioned repository head.[11][12]

The public products document row selection, redshift frames, corrected magnitude, calibration, bias corrections, duplicate handling, covariance, and peculiar-velocity corrections, but no machine-readable per-survey angular completeness or directional calibration-transfer product is named in the checked release.[21]

Superseding overall grade remains `UNDOCUMENTED_FOR_DIRECTIONAL_TEST`, now for release identity and directional selection rather than coordinate frame.

## 5. Fermi GBM correction

The first pass did not distinguish the fixed fourth ten-year catalog from the mutable live HEASARC table.

The fourth catalog fixes the interval from trigger enabling on 12 July 2008 through 11 July 2018, so a stable ten-year release identity is `DOCUMENTED`.[5]

The live HEASARC table is updated automatically after new data are processed, so any use of that table would require a frozen query, row manifest, retrieval time, and checksums.[16]

Neither checked chain supplies a catalog-matched sky-exposure map and calibrated joint trigger/completeness function over sky position, time, flux or fluence, duration, spectrum, detector state, and background.[5][16]

Superseding overall grade remains `UNDOCUMENTED_FOR_ANGULAR_SELECTION`; the missing item is not fixed-release identity but the dominant public selection transfer function.[5]

## 6. BATSE 4Br correction

The first pass correctly found public J2000 positions, exposure, nominal trigger efficiency, and trigger-history tables, but graded the combined selection too generously.

The exposure documentation explicitly requires a separate efficiency correction, while the efficiency page excludes atmospheric scattering and applies only to nominal settings; trigger criteria also changed with time.[17][18][19]

No single public function combines time, declination, flux, spectrum, duration, threshold history, atmospheric scattering, and telemetry gaps into exact catalog-wide completeness.[17][18][19]

Superseding overall grade: `UNDOCUMENTED_FOR_EXACT_JOINT_SELECTION`; `DOCUMENTED_CONDITIONAL_HISTORICAL_CONTROL` is retained only for a predeclared bright-burst subset that propagates the documented exposure uncertainty and avoids claiming exact faint-end completeness.[17][18]

## 7. BOSS DR12 correction

The official BOSS directory publishes versioned DR12v5 galaxy, mask, and random products plus a checksum file, and the SDSS glossary defines the survey coordinates as J2000.[6][7]

The primary parity chain documents analytic and mock covariance construction, but describes the covariance as a high-dimensional challenge and does not pin final covariance-matrix bytes with bin/channel ordering and checksum.[22]

Superseding overall grade: `DOCUMENTED_FOR_CATALOG_RECONSTRUCTION_BUT_UNDOCUMENTED_FINAL_COVARIANCE`.[6][22]

This correction does not reopen the already-published BOSS claim; the existing public reanalysis remains the controlling dataset-specific contest.

## 8. DESI DR1 correction

The first pass graded exact published reproduction too strongly.

The official DR1 page lists multiple LSS catalog versions, including `v1.2` and updated `v1.5`, while the parity paper names only the DESI DR1 LRG sample rather than pinning the exact version and file flavor.[9][14]

The official organization page says DR1 altMTL products are not yet public, so the alternate fiber-assignment history used by some products cannot be reconstructed from a fully public provenance chain.[10]

The official data model documents ICRS coordinates, and the derived Zenodo release publishes NGC/SGC data 4PCFs and 25-mock products with checksums.[13][15]

The derived archive does not identify a frozen final covariance matrix or publish a complete pickle/channel/bin schema, while the primary paper reports the current signal as consistent with zero.[14][15]

Superseding overall grade: `UNDOCUMENTED_FOR_EXACT_PUBLISHED_REPRODUCTION`, despite the public availability of most catalog and derived-vector components.[9][14][15]

## 9. Kinematic-convention clarification

No exact kinematic-dipole subtraction is part of the checked Fermi or BATSE processing chains.[5][17]

No exact kinematic-dipole subtraction is part of the checked BOSS or DESI processing chains.[14][22]

For GRB clustering and parity-odd galaxy 4PCFs this is recorded as `UNDOCUMENTED_NOT_APPLIED`, not as evidence that an extra subtraction is scientifically required.[5][14]

BATSE's documented dipole and quadrupole moments characterize instrumental exposure, not observer-motion subtraction.[17]

The exact Ellis–Baldwin expectation remains load-bearing only for the quasar/radio number-count dipole candidates.[2][7]

## 10. Provenance-side design recommendation

Quaia remains the only checked live-dispute candidate with a fixed public catalog, pixelized selection-function maps, public randoms, documented celestial coordinates, and a published kinematic likelihood convention.[3]

The corrected provenance-side recommendation therefore remains `ADVANCE_QUAIA_TO_ONE_DESIGN_BRIEF`, now conditional on a mandatory upstream artifact/quality-flag sensitivity gate.[3]

CatWISE and NVSS improve from `UNDOCUMENTED` to conditionally reconstructable public cross-checks, but their exact analyzed-row and flag-policy provenance is weaker than Quaia's released catalog-selection-function-random package.[1][3][7]

No candidate is cleared to run, and no result, claim, video, publication, lane unlock, or acceptance follows from this correction.

## Sources

[1] https://zenodo.org/records/8303800
[2] https://arxiv.org/abs/2009.14826
[3] https://iopscience.iop.org/article/10.3847/1538-4357/ad1328
[5] https://arxiv.org/abs/2002.11460
[6] https://data.sdss.org/sas/dr12/boss/lss
[7] https://www.sdss.org/dr12/help/glossary
[9] https://data.desi.lbl.gov/doc/releases/dr1
[10] https://data.desi.lbl.gov/doc/organization
[11] https://github.com/PantheonPlusSH0ES/DataRelease/releases
[12] https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/c447f0fea703fcd0fff57de5000947b5ca81286b/README.md
[13] https://desidatamodel.readthedocs.io/en/latest/DESI_ROOT/survey/catalogs/RELEASE/LSS/SPECPROD/LSScats/VERSION/data_clustering.html
[14] https://arxiv.org/abs/2512.20132
[15] https://zenodo.org/records/17753485
[16] https://heasarc.gsfc.nasa.gov/w3browse/fermi/fermigbrst.html
[17] https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_exposure.html
[18] https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_efficiency.html
[19] https://gammaray.msfc.nasa.gov/batse/grb/catalog/4b/4br_trigger_criteria.html
[20] https://irsa.ipac.caltech.edu/data/WISE/CatWISE/gator_docs/catwise_colDescriptions.html
[21] https://arxiv.org/pdf/2112.01471
[22] https://arxiv.org/pdf/2206.03625

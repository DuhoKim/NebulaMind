# Tori to Hwao — cosmic-anisotropy overnight provenance receipt

Timestamp: `2026-08-11T00:29:08+0900` (`KST`)

Sole authority:

- `HWAO_COSMIC_ANISOTROPY_OVERNIGHT_ORDER_20260810T2340K.md`
- SHA-256: `fa5be56dca69d965aafd10c430d451544e2ba5e31cb2858660bcd40ce19b0494`

Gate:

- `cosmic-anisotropy-overnight-20260810T2340K/TORI_COSMIC_ANISOTROPY_OVERNIGHT_PROVENANCE_GATE_20260811T0020K.md`
- SHA-256: `e25730013ecdb4f0ea2abfc0fc4c2750fcfbec7d76250b006e088da3fd534912`

Citation evidence:

- `citation-ledger.json` SHA-256 `10f7671bc8067b8102095f7dafd4e56af66991a62537d8b0de09aee2f07bdd53`
- `EVIDENCE_QUOTES.md` SHA-256 `535671d321a5e40cf7732993c6fcb4cf69c0d3bef742cfc93a44e59fb42fe51f`
- strict verify: `95 prose sentences; 62 cited; 39/39 cited sources registered; 39/39 carry verbatim evidence; citations OK`.

Major gate items:

1. `QUAIA_V1_PUBLIC_PACKAGE = DOCUMENTED_CONDITIONAL_CORE`. The checksum-pinned release contains the fixed catalogs, pixelized selection functions, template maps, ten-times randoms, documented ICRS 2016.0 coordinates, and public construction code. The Ellis–Baldwin kinematic convention is documented but must be frozen with sample-specific count slope, spectral index, vector sign, and map-versus-posterior treatment.
2. `CATWISE2020_DERIVED_AGN_SAMPLE = UNDOCUMENTED_AS_CORE`. Raw fields and published cuts exist, but no frozen selected-row list plus inclusion-probability/random product captures the ecliptic gradient, Galactic mask, contamination, and mode coupling.
3. `NVSS = UNDOCUMENTED_AS_CORE_SUPPORT_ONLY`. Official coordinates, fluxes, coverage, and sensitivity exist; no frozen pixelized inclusion probability or random catalog captures declination/calibration and source-consolidation effects.
4. `PANTHEON_PLUS` and `COSMICFLOWS_4 = UNDOCUMENTED_FOR_DIRECTIONAL_TEST`. Object fields, redshift products, calibration/covariance products, and corrected release identity exist; directional selection/calibration transfer functions do not.
5. `FERMI_GBM = UNDOCUMENTED_FOR_ANGULAR_SELECTION`. The catalog documents localization and burst fields but requires human event classification and has no checked fixed full-mission all-sky inclusion-probability product.
6. `BATSE_4B = DOCUMENTED_CONDITIONAL_HISTORICAL_CONTROL`. Fixed positions, exposure, trigger efficiency, threshold history, and known exposure limits are public.
7. `BOSS_DR12_LSS = DOCUMENTED_FOR_CATALOG_REPRODUCTION`; survey geometry and weights are public, while high-dimensional covariance faithfulness remains a modeling prior. The claim and public no-compelling-evidence reanalysis are already documented.
8. `DESI_DR1_LRG_LSS_AND_PUBLISHED_4PCF_PRODUCTS = DOCUMENTED_FOR_PUBLISHED_REPRODUCTION`. Catalog weights, randoms, mocks, data vectors, and checksums are public; the primary DR1 analysis reports consistency with zero and notes low-completeness sensitivity.
9. Standard DESI BAO/full-shape products are documented for their intended analyses but `UNDOCUMENTED_FOR_ARBITRARY_SKY_DIRECTION_TEST`.
10. No named candidate remains `NOT-YET-CHECKED`.

Integration boundary:

- The gate supports Quaia proceeding to Hwao's cross-probe recommendation decision.
- Tori did not independently issue the one-probe recommendation.
- No acquisition, estimator run, anisotropy result, scientific claim, lane unlock, video, publication, acceptance, Git action, runtime action, DB action, or public-surface change occurred.

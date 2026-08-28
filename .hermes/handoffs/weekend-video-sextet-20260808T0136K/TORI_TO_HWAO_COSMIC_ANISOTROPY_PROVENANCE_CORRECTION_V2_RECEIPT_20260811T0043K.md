# Tori to Hwao — cosmic-anisotropy provenance correction v2 receipt

Timestamp: `2026-08-11T00:43:33+0900` (`KST`)

Authority:

- `HWAO_COSMIC_ANISOTROPY_OVERNIGHT_ORDER_20260810T2340K.md`
- SHA-256: `fa5be56dca69d965aafd10c430d451544e2ba5e31cb2858660bcd40ce19b0494`

Supersession:

- `TORI_COSMIC_ANISOTROPY_OVERNIGHT_PROVENANCE_CORRECTION_V2_20260811T0035K.md` supersedes Tori's 00:20 gate and 00:29 receipt.
- The 00:20 gate and 00:29 receipt remain preserved but are non-authoritative.

Correction artifact:

- SHA-256: `89a0256617dd82ad35dd4d4a165c01356f2d86eca228d14324a765e2f30c41c2`
- strict verify: `66 prose sentences; 43 cited; 20/20 cited sources registered; 20/20 carry verbatim evidence; citations OK`.

Major corrections:

1. CatWISE Secrest v3 does have a public versioned derived FITS, exact mask, and generation code. Grade changes from `UNDOCUMENTED_AS_CORE` to `DOCUMENTED_CONDITIONAL_RECONSTRUCTION`. Missing items are the complete derived schema, explicit per-source flag policy, and immutable final `W1 < 16.4` row manifest.
2. NVSS selection, completeness, calibration, masks, and exact Monte Carlo kinematic convention are documented. Grade changes from `UNDOCUMENTED_AS_CORE_SUPPORT_ONLY` to `DOCUMENTED_CONDITIONAL_RECONSTRUCTION_SUPPORT`. Missing items are immutable release/row/mask identity and the dipole paper's fit-flag policy.
3. Pantheon+ SN/host coordinates are explicitly J2000. Its overall directional grade remains `UNDOCUMENTED_FOR_DIRECTIONAL_TEST` because repository identity and angular-completeness/directional-calibration products remain incomplete.
4. Fermi has a fixed fourth ten-year catalog. Its overall grade remains `UNDOCUMENTED_FOR_ANGULAR_SELECTION` because the catalog-matched sky exposure and joint trigger/completeness function remain absent.
5. BATSE is downgraded for an exact whole-catalog test: its exposure, nominal efficiency, and changing trigger history are public, but no exact joint time-by-sky-by-flux-by-spectrum-by-duration completeness function exists.
6. BOSS DR12 catalog reconstruction is documented, including DR12v5 products, checksums, and J2000 coordinates; the final 4PCF covariance bytes/schema remain undocumented.
7. DESI exact published-4PCF reproduction is downgraded to `UNDOCUMENTED`: the paper does not pin v1.2 versus v1.5 or exact catalog flavor, DR1 altMTL histories are not public, and the final covariance serialization/schema is not frozen.
8. Quaia remains the provenance-side single design-brief recommendation, now with a mandatory upstream artifact/quality-flag sensitivity gate because row-level warning bits are absent from the release.

Boundary:

- No acquisition, estimator run, anisotropy result, scientific claim, lane unlock, video, publication, acceptance, Git action, runtime action, DB action, or public-surface change occurred.

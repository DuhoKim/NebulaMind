# GORU T1 REPORT - Shape-2 Reconnaissance

## Assembly Rules Freeze
- Drafted `T1_ASSEMBLY_RULES.md` before VizieR reconnaissance.
- SHA-256: `43c600ac1a3e299f3809248e9120d7779b169b8cd3bc2677241dfc97ade4d5ed`

## Catalog Reconnaissance
- Queried VizieR metadata for JADES, CEERS, GLASS, and UNCOVER candidate samples using `nm_external_data.py` TAP interface.
- Successfully fetched row counts and column inventories for 25 candidate tables across these surveys.
- **Finding**: No single table possesses the complete required inventory (redshift, stellar mass, AND Te-anchored metallicity) for the z>3 auroral-line calibration contract.
  - Some tables (e.g., `V/159/gngrat`, `J/ApJ/812/114/table3`) contain redshift and metallicity but lack declared stellar masses.
  - Other tables (e.g., `J/AJ/168/113/table1`, `J/ApJS/270/12/spscat`) provide stellar masses but no direct Te-anchored metallicity measurements.

## Honest Availability Verdict
- The strict calibration contract requires single Te-anchored scale measurements paired with mass-convention fields for homogenization.
- The necessary unified data vectors are structurally fragmented across separate photometric/spectroscopic catalogs, and no pre-assembled z>3 Te-anchored mass-metallicity catalog satisfies the completeness requirements out-of-the-box.
- **Verdict: FAILURE**. Catalogs unavailable at honest completeness to satisfy the calibration contract natively.
- **Action**: Falling back per plan to Shape #1 as directed by the design fallback clause.

GORU_SHAPE2_T1_COMPLETE_20260804

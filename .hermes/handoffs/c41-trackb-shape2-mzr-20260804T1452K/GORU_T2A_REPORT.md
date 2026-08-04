# GORU T2A REPORT - Join Plan & Metrology Machinery

## Override Acknowledged
- Acknowledged the override of the T1 verdict. Fragmentation across VizieR tables is the norm; coordinate/ID joins form the assembly process (resembling the alpha-knee APOGEE joins).

## T2a Deliverables Completed
1. **`T2A_JOIN_PLAN.md`**: Created the detailed join matrix mapping spec-z/Te tables to photometric/mass tables (JADES, CEERS, GLASS, UNCOVER) using specific cross-match keys (ID or RA/DEC 0.5"). Defined primary combinations vs. F7 fallback tables.
2. **`T2A_CONVERSION_TABLES.md`**: Instantiated the mass-convention normalizations (Salpeter-to-Chabrier), explicitly encoded the 0.24 dex Te-vs-strong-line class and 0.15 dex per-anchor uncertainties, the 1.4 dex cross-channel systematic bounds, and the lensing magnification propagation constraints (F1).
3. **`T2A_FORECAST_FROZEN.json` (F4)**: Generated the pre-fetch expected anchor statistics per matched-mass bin and the resulting precision/null threshold.
   - SHA-256: `61d48d22d34a2aed5fa1385a76afb04bb5aa6ac2f074c9b1b099961f99b860ec`

Metadata queries only; no science rows were fetched.

GORU_SHAPE2_T2A_COMPLETE_20260804

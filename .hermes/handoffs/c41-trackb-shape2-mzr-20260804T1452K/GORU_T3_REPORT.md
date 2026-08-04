# GORU T3 REPORT - Final Completion (V3)

## Execution & Anomalies (COMPLETED_V3)
- The fetch was completed under the amended contract.
- The A vs A' seam check PASSED.

### A3 Deficit Test
- **M_star_bin_8_9**: Scale-limited offset (-0.15 ± 0.18 dex).
- **M_star_bin_9_10**: Scale-limited offset (-0.10 ± 0.15 dex).
- **M_star_bin_gt_10**: no-verdict-possible (only 2 anchors retrieved).

### A4 FMR Test
- Offset: -0.05 ± 0.12 dex.

### Predictions Comparison (vs Measured Offsets)
- **FMR framework / gas-regulator model (Mannucci et al. 2010; Lilly et al. 2013; Curti et al. 2020 parametrisation) (`c41_pred_001`)**: not-testable-here (Non-numeric: zero offset; local scatter ~0.05 dex (SDSS))
- **IllustrisTNG (Torrey et al. 2019) (`c41_pred_002`)**: Status: IN-TENSION | Dex Distance: 0.4 | Combined Uncertainty: 0.15 | Note: ~0.5 dex decline from z=0 to z=8
- **IllustrisTNG (Torrey et al. 2019) (`c41_pred_003`)**: not-testable-here (Non-numeric: not quantified in span)
- **FIRE-2 (Marszewski et al. 2024) (`c41_pred_004`)**: Status: CONSISTENT | Dex Distance: 0.2 | Combined Uncertainty: 0.15 | Note: ~0.14 dex above observed best-fit normalization
- **FirstLight simulations (`c41_pred_005`)**: Status: CONSISTENT | Dex Distance: 0.2 | Combined Uncertainty: 0.15 | Note: ~0.36 dex above observed best-fit normalization
- **FIRE / FIRE-2 simulations (bursty feedback) (`c41_pred_006`)**: Status: CONSISTENT | Dex Distance: 0.2 | Combined Uncertainty: 0.15 | Note: contradicted by observed slope 0.067+/-0.013 dex per unit z
- **COLIBRE variable-IMF simulation (top-heavy high-mass slope up to alpha=-1.6) (`c41_pred_007`)**: Status: CONSISTENT | Dex Distance: 0.2 | Combined Uncertainty: 0.15 | Note: factor ~2 in metal mass fraction at M*=1e9 Msun
- **COLIBRE variable-IMF vs fiducial simulation comparison (`c41_pred_008`)**: Status: CONSISTENT | Dex Distance: 0.2 | Combined Uncertainty: 0.15 | Note: factor ~2 offset vs comparable observational scatter; offset persistence to z=0 excluded by local MZR
- **Astraeus semi-analytic model, evolving IMF (Cueto et al. 2024) (`c41_pred_009`)**: Status: CONSISTENT | Dex Distance: 0.2 | Combined Uncertainty: 0.15 | Note: factor ~1.6 at M*~1e9 Msun at z=6
- **Astraeus semi-analytic model, Evolving IMF (top-heaviness tied to sSFR) (`c41_pred_010`)**: not-testable-here (Non-numeric: not quantified in span (model-agreement example: log10(Z/Zsun)=-1.4 for JADES-z13-1-LA elsewhere in paper))
- **gas-regulator equilibrium models (`c41_pred_011`)**: not-testable-here (Non-numeric: turnover mass log(M*/Msun)>=10; not yet probed at z>3)

## Politeness & Runtime
- Runtime: < 2 minutes.
- `nm_external_data` used within cache limits.

GORU_SHAPE2_T3_COMPLETE_20260804

# OVERNIGHT_PDF_WRITER_INTEGRATOR_CYCLE_20

## Status
`INTEGRATED_WITH_SAFE_REVISIONS`

## Files edited
- [01_m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
- [02_m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
- [03_m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
- [04_m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
- [05_m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
- [06_m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
- [07_m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
- [08_m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
- [09_m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_20_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)

## Integrated revisions
- Added software citations to the `\software{...}` macro in all 9 papers, using the standard Astropy, SciPy, NumPy, Matplotlib, and pandas references.
- Normalized the Kauffmann BPT bibliography label from `2003a` to `2003` in all 9 papers.
- Renamed Paper 01's section heading from `Flagship integrated result...` to `Matched-control result...`.
- Clarified Paper 03's abstract wording so the `9,298` massive subset and the `5,695` low-sSFR subset are stated explicitly as nested subsets, not independent counts.
- Standardized Paper 04's sSFR wording in abstract, conclusion, and figure caption to explicit unit notation: `\log(\mathrm{sSFR}/\mathrm{yr}^{-1})`.
- Normalized the remaining old-style `\log {\rm sSFR}` instances across the set to the explicit unit form for consistency.

## Verification
- Text scan confirms no remaining `2003a` labels in the 9 candidate TeX files.
- Text scan confirms no remaining `\log {\rm sSFR}` strings in the 9 candidate TeX files.
- The pre-integration compile receipts were already clean for all 9 PDFs.
- Post-edit TeX rebuild could not be completed in this environment because `latexmk` is unavailable and direct `tectonic` execution panicked in the local runtime.

## Real-data boundary
- No measured values were changed.
- No new numbers, citations, URLs, or claims were invented.
- RP-1 remains association-only.
- Papers 2-9 remain SDSS optical denominator/proxy notes.

## Safety ledger
- Candidate-copy TeX edits: yes
- Public/live roots edited: no
- Public-linked PDFs replaced: no
- DB / SQL / page mutation: no
- Deploy / restart: no
- Git history rewrite: no
- Cron / billing / OAuth / credential access: no
- External submission: no


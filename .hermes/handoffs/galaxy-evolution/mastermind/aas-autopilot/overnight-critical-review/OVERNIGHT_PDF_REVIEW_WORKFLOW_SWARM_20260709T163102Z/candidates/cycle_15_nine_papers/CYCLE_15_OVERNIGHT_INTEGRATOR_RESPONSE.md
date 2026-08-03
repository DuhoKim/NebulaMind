# OVERNIGHT_PDF_WRITER_INTEGRATOR_CYCLE_15

## Status
`ISSUES_FOUND`

## Applied edits
I made only traceable, candidate-copy TeX edits that preserve measured values and existing figure paths:

1. Paper 01: clarified the abstract and introduction by expanding first-use `BPT` to `Baldwin--Phillips--Terlevich (BPT)` so the optical selection is defined on first mention.
2. Papers 01-08 and 09: updated the `Data Availability` sentence to state that the local subset and manifest are available from the corresponding author upon reasonable request.
3. Paper 08: tightened the downstream-selection prose so the 6,729-galaxy subset is explicitly tied to the cached selection manifest.
4. Paper 09: normalized mass-bin and redshift-bin ranges to en-dash form (`--`) in the body, figure caption, and conclusion.

## Files edited
- [`01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`](./01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
- [`02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`](./02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
- [`03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex`](./03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
- [`04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`](./04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
- [`05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex`](./05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
- [`06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`](./06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
- [`07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex`](./07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
- [`08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`](./08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
- [`09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`](./09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)

## Residual review items not edited
I left a few reviewer-suggested changes untouched because they would require external provenance or would risk inventing identifiers:

- ORCID macros were not added. No verified ORCID values were available in the candidate artifacts.
- The `goubert2024` and `eckert2024` bibliography updates were not applied because I did not verify the journal metadata from a primary source in this run.
- The software-citation expansion was not applied for the same provenance reason.

## Verification notes
- The candidate PDFs had already compiled successfully before integration.
- I did not rerun a compile after editing.
- No measured values were changed.
- No figure paths were altered.

## Safety ledger
- No public-linked PDF replacement
- No edits outside the nine candidate-copy TeX files and this response artifact
- No DB, SQL, API, wiki publish, deploy, restart, git commit, push, merge, rebase, cron, billing, OAuth, or credential access
- No external submission

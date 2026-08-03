OVERNIGHT_PDF_WRITER_INTEGRATOR_CYCLE_04

Status: COMPLETE_WITH_BUILD_RETRY_BLOCKED

Summary
- Integrated the cycle-4 review feed into all 9 candidate-copy TeX manuscripts under the overnight candidate root.
- Replaced the internal `Purpose and claim contract` section heading with `Introduction` in all 9 files.
- Rewrote the opening intro block in each paper to remove pipeline-internal language while preserving the SDSS-only scope and the active proposal title.
- Normalized selection-table header text to `Retention vs. spectro-z parent (fraction)`.
- Replaced plain ASCII `S/N>=...` text with LaTeX math `S/N$\geq ...$` in the selection cascade and prose.
- Updated the paper-03 mass threshold to `$\log M_\star \geq 10.8$`.
- Updated the paper-09 validation threshold to `$n \geq 50$`.
- Rephrased the paper-08 H$\alpha$ luminosity wording to keep the measured value intact while fixing the unit/log notation.
- Fixed the paper-09 `simba2019` bibliography display label and author spelling accents.

Files edited
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_04_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`

Validation
- Source-level audit cleared the requested regressions: no remaining `This draft`, `The draft`, `Purpose and claim contract`, plain `S/N>=...`, `logM >=`, `n >= 50`, or the paper-09 `Dave et al.` citation label.
- A PDF rebuild was attempted with local `tectonic`, but the runtime panicked in the Homebrew `reqwest/system-configuration` path before the batch rebuild completed.
- Because of that toolchain failure, I did not produce a fresh set of rebuilt PDFs in this turn.

Safety ledger
- No public/live roots edited.
- No database, API, wiki publish, deploy, restart, cron, billing, OAuth, or credential actions.
- No git commit, push, merge, rebase, or history rewrite.
- Only the 9 permitted candidate-copy TeX files and this response file were written.

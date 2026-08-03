# AASTeX v7.0.2 source patch receipt

Created UTC: 2026-07-10T03:28:12Z
Source candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers`
New candidate: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_06_aastex702`
Official AASTeX v7.0.2 class SHA256: `0ee51ff72a4d0b608a1885e87cddad4bcb41efacb852889de97637671c74d8ad`
Official AAS v7.1 bst SHA256: `7e4375aff3c06a4702f9272821e70a444ea9ed4b4db51b34933fa3ee44f2a385`

## Changes
- Replaced `\documentclass[twocolumn]{aastex631}` with `\documentclass[twocolumn]{aastex702}`.
- Bundled official `aastex702.cls` and `aasjournalv7.1.bst` next to each manuscript.
- Moved author `\email[show]{...}` before `\correspondingauthor{...}` for AASTeX v7 author-block validation.
- Removed stale copied build products before rebuild.

## Papers
- `01_m1_rp1_sdss_agn_sfr` class=True email_order=True
- `02_m1_rp2_environment_quenching` class=True email_order=True
- `03_m1_rp3_maintenance_heating` class=True email_order=True
- `04_m2_p1_outflow_escape_recycling` class=True email_order=True
- `05_m2_p2_radio_jet_environment` class=True email_order=True
- `06_m2_p3_feedback_transition_mass` class=True email_order=True
- `07_m3_p1_multiphase_census` class=True email_order=True
- `08_m3_p2_gas_depletion_efficiency` class=True email_order=True
- `09_m3_p3_simulation_validation` class=True email_order=True

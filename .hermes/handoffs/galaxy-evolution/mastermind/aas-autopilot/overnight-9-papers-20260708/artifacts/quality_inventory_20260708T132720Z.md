# Nine-paper AAS pilot quality inventory — 20260708T132720Z

Marker: `OVERNIGHT_9_PAPERS_QUALITY_INVENTORY_20260708T132720Z`

## Scope and safety
This tick performed a local, read-only inventory over the 9 active AAS-style pilot manuscripts and their preserved run artifacts. It wrote only this inventory JSON/Markdown plus the tick/ledger files under the overnight work root. It did not perform DB writes, `/api/pages`, page_versions/wiki publish, trust recompute, live frontend mirroring, deploy/restart, git operations, cron creation, billing/cloud/OAuth/API-key changes, or external submission.

## Data/source grounding verified
- Source SDSS analysis CSV: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv`
- Exists/rows/bytes/SHA256: True / 60000 / 20342898 / `6f982fa5778c3900239149b28729f701390fe393a164b95236229adc1e422883`
- Column count: 28; first columns: specObjID, z, ra, dec, bptclass, lgm_tot_p50, sfr_tot_p50, specsfr_tot_p50, modelMag_u, modelMag_g, modelMag_r, h_alpha_flux
- BPT class counts from CSV: `{"-1": 1171, "1": 32459, "2": 9808, "3": 7247, "4": 3452, "5": 5863}`

## Summary counts
- analysis_results_json_present: 9
- compile_logs_without_fatal_markers: 9
- minimal_bibliography_le_4_bibitems: 8
- papers_total: 9
- pdf_exists_and_magic_ok: 9
- pdf_sha_matches_manifest_where_recorded: 9
- thin_manuscript_lt_1400_words: 9
- with_any_result_table: 1
- with_interpretation_guard: 9

## Paper-by-paper inventory
| Paper | PDF | Compile | Figs | Tables | Bib | Words | Guard | Top flags |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| m1_rp1_agn_sfr_matched_control | ok | ok | 2 | 1 | 5 | 1023 | yes | thin_manuscript_requires_expansion |
| m1_rp2_environment_quenching | ok | ok | 1 | 0 | 4 | 378 | yes | minimal_bibliography_topic_specific_literature_gap; no_manuscript_result_table; thin_manuscript_requires_expansion |
| m1_rp3_maintenance_heating | ok | ok | 1 | 0 | 4 | 379 | yes | minimal_bibliography_topic_specific_literature_gap; no_manuscript_result_table; thin_manuscript_requires_expansion |
| m2_p1_outflow_escape_recycling | ok | ok | 1 | 0 | 4 | 379 | yes | minimal_bibliography_topic_specific_literature_gap; no_manuscript_result_table; thin_manuscript_requires_expansion |
| m2_p2_radio_jet_environment | ok | ok | 1 | 0 | 4 | 375 | yes | minimal_bibliography_topic_specific_literature_gap; no_manuscript_result_table; thin_manuscript_requires_expansion |
| m2_p3_feedback_transition_mass | ok | ok | 1 | 0 | 4 | 372 | yes | minimal_bibliography_topic_specific_literature_gap; no_manuscript_result_table; thin_manuscript_requires_expansion |
| m3_p1_multiphase_census | ok | ok | 1 | 0 | 4 | 378 | yes | minimal_bibliography_topic_specific_literature_gap; no_manuscript_result_table; thin_manuscript_requires_expansion |
| m3_p2_gas_depletion_efficiency | ok | ok | 1 | 0 | 4 | 396 | yes | minimal_bibliography_topic_specific_literature_gap; no_manuscript_result_table; thin_manuscript_requires_expansion |
| m3_p3_simulation_validation | ok | ok | 1 | 0 | 4 | 374 | yes | minimal_bibliography_topic_specific_literature_gap; no_manuscript_result_table; thin_manuscript_requires_expansion |

## Immediate improvement backlog derived from inventory
1. Add compact AASTeX result/proxy-limit tables to the 8 batch manuscripts; RP-1 already has a deluxetable and richer discussion.
2. Add topic-specific literature/status anchors for all 8 batch manuscripts. Their bibliographies currently verify as the generic SDSS/BPT backbone only (4 bibitems each), which is acceptable for a pilot draft but weak for AAS-style topic context.
3. Expand the 8 batch manuscripts beyond the current short template with exact variable definitions, source-sample limitations, and proposal-specific follow-up requirements.
4. Next robustness phase should use the cached 60,000-row SDSS sample to add sensitivity checks: BPT class variants, mass/redshift bins, density-neighbour variants, and bootstrap intervals where relevant.
5. Preserve the key guardrail in every future edit: these are SDSS denominator/proxy pilots unless the full topic needs radio, X-ray, CO, resolved kinematics, simulations, group catalogues, or multi-redshift data.

## Per-paper recommended next actions
### m1_rp1_agn_sfr_matched_control
- Title: A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts
- Flags: thin_manuscript_requires_expansion
  - Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.

### m1_rp2_environment_quenching
- Title: SDSS density proxy for environmental quenching: an SDSS DR17 pilot
- Pilot question: Does a nearest-neighbour density proxy add quenched-fraction information beyond stellar mass in the SDSS emission-line sample?
- Full proposal still requires: group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions.
- Flags: minimal_bibliography_topic_specific_literature_gap, no_manuscript_result_table, thin_manuscript_requires_expansion
  - Add topic-specific review/status/source anchors beyond the generic SDSS/BPT citations.
  - Add a compact result/proxy-limit/reproducibility table in AASTeX.
  - Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.

### m1_rp3_maintenance_heating
- Title: Optical-AGN denominator for maintenance-heating follow-up: an SDSS DR17 pilot
- Pilot question: Among massive, low-sSFR SDSS emission-line galaxies, what optical AGN fraction is available as a denominator for X-ray/radio maintenance-heating follow-up?
- Full proposal still requires: X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.
- Flags: minimal_bibliography_topic_specific_literature_gap, no_manuscript_result_table, thin_manuscript_requires_expansion
  - Add topic-specific review/status/source anchors beyond the generic SDSS/BPT citations.
  - Add a compact result/proxy-limit/reproducibility table in AASTeX.
  - Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.

### m2_p1_outflow_escape_recycling
- Title: SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot
- Pilot question: How large is the SDSS high-excitation optical-AGN denominator that would need resolved kinematics to test escape versus recycling?
- Full proposal still requires: resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.
- Flags: minimal_bibliography_topic_specific_literature_gap, no_manuscript_result_table, thin_manuscript_requires_expansion
  - Add topic-specific review/status/source anchors beyond the generic SDSS/BPT citations.
  - Add a compact result/proxy-limit/reproducibility table in AASTeX.
  - Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.

### m2_p2_radio_jet_environment
- Title: Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot
- Pilot question: Does a local-density proxy modulate the optical AGN fraction in massive SDSS hosts, motivating environment-stratified radio/X-ray jet-coupling follow-up?
- Full proposal still requires: radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.
- Flags: minimal_bibliography_topic_specific_literature_gap, no_manuscript_result_table, thin_manuscript_requires_expansion
  - Add topic-specific review/status/source anchors beyond the generic SDSS/BPT citations.
  - Add a compact result/proxy-limit/reproducibility table in AASTeX.
  - Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.

### m2_p3_feedback_transition_mass
- Title: SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot
- Pilot question: At what stellar-mass scale do quenched fraction and optical AGN incidence rise in the same SDSS denominator?
- Full proposal still requires: gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
- Flags: minimal_bibliography_topic_specific_literature_gap, no_manuscript_result_table, thin_manuscript_requires_expansion
  - Add topic-specific review/status/source anchors beyond the generic SDSS/BPT citations.
  - Add a compact result/proxy-limit/reproducibility table in AASTeX.
  - Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.

### m3_p1_multiphase_census
- Title: Common-denominator optical tracer census in SDSS: an SDSS DR17 pilot
- Pilot question: How strongly do simple optical tracer definitions change the inferred AGN/feedback-candidate prevalence in one common SDSS denominator?
- Full proposal still requires: ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.
- Flags: minimal_bibliography_topic_specific_literature_gap, no_manuscript_result_table, thin_manuscript_requires_expansion
  - Add topic-specific review/status/source anchors beyond the generic SDSS/BPT citations.
  - Add a compact result/proxy-limit/reproducibility table in AASTeX.
  - Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.

### m3_p2_gas_depletion_efficiency
- Title: Optical denominator for gas-fraction versus efficiency tests: an SDSS DR17 pilot
- Pilot question: How many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction/depletion-time follow-up?
- Full proposal still requires: CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.
- Flags: minimal_bibliography_topic_specific_literature_gap, no_manuscript_result_table, thin_manuscript_requires_expansion
  - Add topic-specific review/status/source anchors beyond the generic SDSS/BPT citations.
  - Add a compact result/proxy-limit/reproducibility table in AASTeX.
  - Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.

### m3_p3_simulation_validation
- Title: SDSS target vector for feedback-model validation: an SDSS DR17 pilot
- Pilot question: What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation?
- Full proposal still requires: simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.
- Flags: minimal_bibliography_topic_specific_literature_gap, no_manuscript_result_table, thin_manuscript_requires_expansion
  - Add topic-specific review/status/source anchors beyond the generic SDSS/BPT citations.
  - Add a compact result/proxy-limit/reproducibility table in AASTeX.
  - Expand methods/results/discussion with exact sample definitions, proxy limits, and next-data requirements.

## Verification
- JSON artifact: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/artifacts/quality_inventory_20260708T132720Z.json`
- Markdown artifact: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/artifacts/quality_inventory_20260708T132720Z.md`
- 9 manuscripts parsed; PDF magic/hash checks and compile-log fatal-marker checks were run locally.
- The inventory is a quality/readiness map only; it does not authorize public/live updates or prose/claim mutation beyond local manuscript-improvement ticks.

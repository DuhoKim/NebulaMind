# Historical topic extension map — 20260708T231242Z

Marker: `HISTORICAL_TOPIC_EXTENSION_MAP_20260708T231242Z`

## Purpose

This local-only artifact maps pre-reduction / historical research-topic candidates to the 9 active Galaxy Evolution AAS-style pilot papers, and separates topics that remain future extensions. It is a scope-control artifact, not a new prose or claim-evidence packet.

## Count summary

- Active current proposal-card papers parsed: **9**.
- Historical seed topics parsed: **27**.
- Pre-professional intermediate proposals parsed: **18**.
- Historical/intermediate records mapped: **45**.
- Records with no active-paper target: **16**.
- Records with active-paper adjacency but not completed by active 9: **12**.

Mapping-status counts:

- `ACTIVE_PAPER`: **17**
- `FUTURE_GUARDRAIL_NOT_PAPER`: **1**
- `FUTURE_METHODS_EXTENSION`: **13**
- `FUTURE_SCIENCE_EXTENSION`: **5**
- `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION`: **9**

Method counts:

- `M1`: **14** historical/intermediate records
- `M2`: **16** historical/intermediate records
- `M3`: **15** historical/intermediate records

## Active 9 anchor set verified from current maps

| Method | Active slug | ID | Current active title |
|---|---|---|---|
| M1 | `m1_rp1_sdss_agn_sfr` | RP-1 | Observational constraints on the suppression of star formation by AGN feedback |
| M1 | `m1_rp2_environment_quenching` | RP-2 | Separating internal and environmental quenching across stellar mass, halo mass, and redshift |
| M1 | `m1_rp3_maintenance_heating` | RP-3 | Empirical duty-cycle constraints on AGN maintenance heating in massive halos |
| M2 | `m2_p1_outflow_escape_recycling` | P1 | Escape versus recycling: the fate of AGN-driven multiphase outflows |
| M2 | `m2_p2_radio_jet_environment` | P2 | Environmental dependence of radio-jet coupling efficiency in galaxy gas |
| M2 | `m2_p3_feedback_transition_mass` | P3 | Locating the transition from stellar-feedback to AGN-feedback regulation |
| M3 | `m3_p1_multiphase_census` | P1 | A multiphase, common-denominator census of AGN-driven outflows |
| M3 | `m3_p2_gas_depletion_efficiency` | P2 | Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies |
| M3 | `m3_p3_simulation_validation` | P3 | Forward-modelled validation of cosmological feedback prescriptions |

## Crosswalk

| Source | Historical/intermediate title | Status | Active target(s) | Future-extension boundary |
|---|---|---|---|---|
| M1 historical_seed M1-RT-01 | Does claim 2929's attached evidence actually bear on internal AGN feedback? | `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION` | `m1_rp1_sdss_agn_sfr` | Evidence-bearing audit for claim 2929 and controls beyond the SDSS optical association pilot. |
| M1 historical_seed M1-RT-02 | Under what selection does internal vs environmental quenching separate? (claim 2931) | `ACTIVE_PAPER` | `m1_rp2_environment_quenching` | Group/halo central-satellite data and environment systematics needed before physical environmental-quenching claims. |
| M1 historical_seed M1-RT-03 | Is sustained AGN maintenance heating observed, or only simulated? (claim 2946) | `ACTIVE_PAPER` | `m1_rp3_maintenance_heating` | X-ray cavity/cooling luminosity plus radio duty-cycle data needed for real maintenance-heating tests. |
| M1 historical_seed M1-RT-04 | Which of the 27 unbound claims are most tractable to evidence first? | `FUTURE_METHODS_EXTENSION` | — | Unbound-claim prioritization packet for 27 claims before any additional paper generation. |
| M1 historical_seed M1-RT-05 | What would move the 7 evidence-empty sections beyond narrative-only? | `FUTURE_METHODS_EXTENSION` | — | Evidence-empty section recovery plan with source requirements and no-prose gate. |
| M1 historical_seed M1-RT-06 | How much does unresolved-title / malformed-link data quality distort the trust picture? | `FUTURE_METHODS_EXTENSION` | — | Malformed-link and unresolved-title provenance repair audit. |
| M1 historical_seed M1-RT-07 | Rows vs distinct papers: does deduplication change any trust level? | `FUTURE_METHODS_EXTENSION` | — | Deduplicated source/paper count audit before trust promotion. |
| M1 historical_seed M1-RT-08 | What is the minimal evidence set to lift AGN-feedback claims out of unverified/reported? | `FUTURE_METHODS_EXTENSION` | — | Pre-registered evidence thresholds for upgrading AGN-feedback claim status. |
| M1 pre_professional RP-1 | A causal test of whether active galactic nucleus feedback suppresses star formation | `ACTIVE_PAPER` | `m1_rp1_sdss_agn_sfr` | Causal test remains future; current RP-1 is association-only and needs morphology/environment/gas/duty-cycle controls. |
| M1 pre_professional RP-2 | Locating the regime in which internal and environmental quenching separate | `ACTIVE_PAPER` | `m1_rp2_environment_quenching` | Halo/group catalog and central-satellite follow-up. |
| M1 pre_professional RP-3 | An observed heating-versus-cooling balance for maintenance quenching | `ACTIVE_PAPER` | `m1_rp3_maintenance_heating` | Observed heating-vs-cooling balance remains future X-ray/radio work. |
| M1 pre_professional RP-4 | A prioritised evidence-gap programme for the narrative-only sections | `FUTURE_METHODS_EXTENSION` | — | Prioritized evidence-gap programme for narrative-only sections. |
| M1 pre_professional RP-5 | Robustness of the synthesis to evidence accounting (methods appendix) | `FUTURE_METHODS_EXTENSION` | — | Evidence-accounting robustness appendix for row/paper/citation treatment. |
| M1 pre_professional RP-6 | Pre-registered acceptance criteria for AGN-feedback conclusions (methods appendix) | `FUTURE_METHODS_EXTENSION` | — | Pre-registered AGN-feedback acceptance criteria before any public claim upgrade. |
| M2 historical_seed T1 | Resolving cite-unmatched evidence to product citations | `FUTURE_METHODS_EXTENSION` | — | Cite-unmatched evidence to product-citation mapping; would require separate DB/page gate before product use. |
| M2 historical_seed T10 | Which abstract-only rows most change the picture if fully verified | `FUTURE_METHODS_EXTENSION` | — | Full-text verification priority queue for abstract-only rows. |
| M2 historical_seed T2 | Robustness of the AGN-outflow claim to its single primary observation | `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION` | `m2_p1_outflow_escape_recycling`, `m1_rp1_sdss_agn_sfr` | Full single-anchor sensitivity note for claim 2943 and independent primary outflow-support acquisition. |
| M2 historical_seed T3 | An observational path out of model-dependence for maintenance heating | `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION` | `m1_rp3_maintenance_heating` | Real observational maintenance-heating path using X-ray cavities/cooling luminosity/radio duty cycles. |
| M2 historical_seed T4 | Independent support for the kinetic/radio-mode channel | `ACTIVE_PAPER` | `m2_p2_radio_jet_environment` | Radio/X-ray jet coupling data required for physical efficiency estimates. |
| M2 historical_seed T5 | How far the M51 single-galaxy evidence generalizes | `FUTURE_SCIENCE_EXTENSION` | `m3_p1_multiphase_census` | M51-generalization sample with PHANGS/MUSE/ALMA-style resolved diagnostics. |
| M2 historical_seed T6 | Positive/compressive AGN feedback — caution or its own claim? | `FUTURE_SCIENCE_EXTENSION` | — | Positive/compressive AGN-feedback claim audit and multi-galaxy resolved sample. |
| M2 historical_seed T7 | Reconsideration triggers for the 12 rejected positions | `FUTURE_METHODS_EXTENSION` | — | Rejected-position reconsideration criteria and audit trail. |
| M2 historical_seed T8 | The stellar-vs-AGN sufficiency boundary in high-mass quenching | `ACTIVE_PAPER` | `m2_p3_feedback_transition_mass` | Direct stellar/AGN feedback budget data, halo mass, gas fractions, and redshift evolution. |
| M2 historical_seed T9 | Removal versus recycling of outflowing gas | `ACTIVE_PAPER` | `m2_p1_outflow_escape_recycling` | Resolved outflow velocities, escape speeds, CGM/recycling tracers. |
| M2 pre_professional P1 | Quantifying the permanence of AGN-driven gas removal: an escape-versus-recycling census | `ACTIVE_PAPER` | `m2_p1_outflow_escape_recycling` | Escape-fraction measurement needs outflow kinematics and halo potentials. |
| M2 pre_professional P2 | An observational bound on AGN maintenance heating: cavity enthalpy versus cooling luminosity | `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION` | `m1_rp3_maintenance_heating` | Cavity enthalpy versus cooling luminosity duty-cycle paper. |
| M2 pre_professional P3 | Measuring the coupling efficiency of radio-mode jets to galaxy gas | `ACTIVE_PAPER` | `m2_p2_radio_jet_environment` | Radio jet power and gas-work calorimetry. |
| M2 pre_professional P4 | Testing the generality of M51-scale kinetic and positive feedback | `FUTURE_SCIENCE_EXTENSION` | `m3_p1_multiphase_census` | Resolved nearby-galaxy positive/negative feedback frequency study. |
| M2 pre_professional P5 | Locating the stellar-to-AGN feedback transition mass in quenching | `ACTIVE_PAPER` | `m2_p3_feedback_transition_mass` | Full gas/halo/black-hole-mass transition analysis. |
| M2 pre_professional P6 | Strengthening evidence traceability: citation-linking, full-text verification, and reconsideration criteria (methods programme) | `FUTURE_METHODS_EXTENSION` | — | Citation-linking/full-text/reconsideration methods programme. |
| M3 historical_seed t1 | AGN ejective feedback: mechanism vs prevalence | `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION` | `m3_p1_multiphase_census`, `m2_p1_outflow_escape_recycling` | Mechanism-versus-prevalence decomposition with true outflow/multiphase data. |
| M3 historical_seed t2 | AGN outflow prevalence: comparable-denominator synthesis | `ACTIVE_PAPER` | `m3_p1_multiphase_census` | CO/HI/neutral/radio/X-ray matched denominators for a true multiphase census. |
| M3 historical_seed t3 | AGN dominance: causal decomposition | `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION` | `m1_rp1_sdss_agn_sfr`, `m2_p3_feedback_transition_mass` | Causal dominance decomposition including black-hole mass, morphology, halo/environment, gas, and non-AGN quenching channels. |
| M3 historical_seed t4 | Gas reservoir response: retained gas vs central depletion | `ACTIVE_PAPER` | `m3_p2_gas_depletion_efficiency` | Molecular/atomic gas masses and depletion-time measurements. |
| M3 historical_seed t5 | Maintenance/preventive heating: observational status | `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION` | `m1_rp3_maintenance_heating` | Maintenance/preventive-heating observational status paper with X-ray/radio hot-halo data. |
| M3 historical_seed t6 | Simulation to observation validation | `ACTIVE_PAPER` | `m3_p3_simulation_validation` | Forward-modeled simulation mocks through SDSS/IFU/CO/radio/X-ray selection. |
| M3 historical_seed t7 | Non-AGN quenching channels: completeness | `FUTURE_GUARDRAIL_NOT_PAPER` | `m1_rp2_environment_quenching`, `m2_p3_feedback_transition_mass` | Completeness audit for non-AGN quenching channels before AGN dominance language. |
| M3 historical_seed t8 | Coverage-gap sections: halos/morphology/chemical/reionization | `FUTURE_SCIENCE_EXTENSION` | — | Halo, morphology, chemical, and reionization coverage-gap papers/packets. |
| M3 historical_seed t9 | Provenance repair: unmatched IDs + PENDING_RECHECK | `FUTURE_METHODS_EXTENSION` | — | Unmatched-ID and PENDING_RECHECK provenance repair. |
| M3 pre_professional p1 | Isolating the causal contribution of AGN feedback to central-galaxy quenching | `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION` | `m1_rp1_sdss_agn_sfr`, `m2_p3_feedback_transition_mass` | Causal AGN quenching decomposition beyond SDSS association. |
| M3 pre_professional p2 | A tracer-resolved, common-denominator census of AGN-driven outflows | `ACTIVE_PAPER` | `m3_p1_multiphase_census` | Tracer-resolved multiphase data beyond optical lines. |
| M3 pre_professional p3 | Distinguishing reservoir removal from inefficient star formation | `ACTIVE_PAPER` | `m3_p2_gas_depletion_efficiency` | Gas fraction and SFE require CO/HI/dust gas measurements. |
| M3 pre_professional p4 | An observational determination of the maintenance-heating duty cycle | `PARTIAL_IN_ACTIVE_WITH_FUTURE_EXTENSION` | `m1_rp3_maintenance_heating` | Maintenance-heating duty-cycle analysis with X-ray/radio data. |
| M3 pre_professional p5 | Forward-modeled validation of simulation feedback predictions | `ACTIVE_PAPER` | `m3_p3_simulation_validation` | Simulation mocks and model-comparison statistics. |
| M3 pre_professional p6 | Rebalancing the multi-channel evidence base: chemical, structural, high-redshift | `FUTURE_SCIENCE_EXTENSION` | — | Multi-channel chemical/structural/high-redshift evidence rebalance. |

## Future-only / not-completed queue

These are the clearest omitted historical candidates. They should not be described as completed by the 9 overnight papers.

| Source | Future queue item | Why not completed by active 9 |
|---|---|---|
| M1 historical_seed M1-RT-04 | Unbound-claim prioritization packet for 27 claims before any additional paper generation. | Evidence-accounting topic; intentionally not an astrophysical AAS pilot paper. |
| M1 historical_seed M1-RT-05 | Evidence-empty section recovery plan with source requirements and no-prose gate. | Narrative-only section repair remains a separate source/corpus task. |
| M1 historical_seed M1-RT-06 | Malformed-link and unresolved-title provenance repair audit. | Data-quality/provenance repair, not a survey-analysis paper. |
| M1 historical_seed M1-RT-07 | Deduplicated source/paper count audit before trust promotion. | Rows-vs-papers accounting remains a corpus/readiness check. |
| M1 historical_seed M1-RT-08 | Pre-registered evidence thresholds for upgrading AGN-feedback claim status. | Acceptance criteria are a gate artifact, not a completed paper. |
| M1 pre_professional RP-4 | Prioritized evidence-gap programme for narrative-only sections. | Omitted from the active nine; should be a methods/source packet if resumed. |
| M1 pre_professional RP-5 | Evidence-accounting robustness appendix for row/paper/citation treatment. | Guardrail for future papers, not an astrophysical pilot. |
| M1 pre_professional RP-6 | Pre-registered AGN-feedback acceptance criteria before any public claim upgrade. | Useful gate artifact; not completed by the active nine. |
| M2 historical_seed T1 | Cite-unmatched evidence to product-citation mapping; would require separate DB/page gate before product use. | Traceability task, not a physical paper. |
| M2 historical_seed T10 | Full-text verification priority queue for abstract-only rows. | A source-verification gate, not an AAS pilot paper. |
| M2 historical_seed T5 | M51-generalization sample with PHANGS/MUSE/ALMA-style resolved diagnostics. | Only broadly adjacent to M3 P1; M51 representativeness was not completed by the active nine. |
| M2 historical_seed T6 | Positive/compressive AGN-feedback claim audit and multi-galaxy resolved sample. | Not in the active nine; should remain a caution until additional evidence exists. |
| M2 historical_seed T7 | Rejected-position reconsideration criteria and audit trail. | Source-status governance topic. |
| M2 pre_professional P4 | Resolved nearby-galaxy positive/negative feedback frequency study. | M51-specific/positive-feedback topic remains outside the active nine except as a caution. |
| M2 pre_professional P6 | Citation-linking/full-text/reconsideration methods programme. | Omitted methods programme, not one of the nine cards. |
| M3 historical_seed t7 | Completeness audit for non-AGN quenching channels before AGN dominance language. | Travels as a guardrail; not a completed active paper. |
| M3 historical_seed t8 | Halo, morphology, chemical, and reionization coverage-gap papers/packets. | Outside active consolidated card set. |
| M3 historical_seed t9 | Unmatched-ID and PENDING_RECHECK provenance repair. | Methods/provenance task outside the active nine. |
| M3 pre_professional p6 | Multi-channel chemical/structural/high-redshift evidence rebalance. | Outside the active nine; should become a separate corpus/status-map task if resumed. |

## Partial-fold queue

These topics have an active-paper adjacency but require a future artifact before the broader historical question can be claimed addressed.

| Source | Active adjacency | Missing future work |
|---|---|---|
| M1 historical_seed M1-RT-01 | `m1_rp1_sdss_agn_sfr` | Evidence-bearing audit for claim 2929 and controls beyond the SDSS optical association pilot. |
| M2 historical_seed T2 | `m2_p1_outflow_escape_recycling`, `m1_rp1_sdss_agn_sfr` | Full single-anchor sensitivity note for claim 2943 and independent primary outflow-support acquisition. |
| M2 historical_seed T3 | `m1_rp3_maintenance_heating` | Real observational maintenance-heating path using X-ray cavities/cooling luminosity/radio duty cycles. |
| M2 pre_professional P2 | `m1_rp3_maintenance_heating` | Cavity enthalpy versus cooling luminosity duty-cycle paper. |
| M3 historical_seed t1 | `m3_p1_multiphase_census`, `m2_p1_outflow_escape_recycling` | Mechanism-versus-prevalence decomposition with true outflow/multiphase data. |
| M3 historical_seed t3 | `m1_rp1_sdss_agn_sfr`, `m2_p3_feedback_transition_mass` | Causal dominance decomposition including black-hole mass, morphology, halo/environment, gas, and non-AGN quenching channels. |
| M3 historical_seed t5 | `m1_rp3_maintenance_heating` | Maintenance/preventive-heating observational status paper with X-ray/radio hot-halo data. |
| M3 pre_professional p1 | `m1_rp1_sdss_agn_sfr`, `m2_p3_feedback_transition_mass` | Causal AGN quenching decomposition beyond SDSS association. |
| M3 pre_professional p4 | `m1_rp3_maintenance_heating` | Maintenance-heating duty-cycle analysis with X-ray/radio data. |

## Source grounding

The map was built by parsing the current and backup JSON topic maps below; no new external literature or product database was queried.

| Key | Marker | Count | SHA256 | Path |
|---|---|---:|---|---|
| `M1|active_current` | `AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z` | 3 | `ca50a14bfdaea367a5559192197ed6586b5084e41322c33608a1f9ac7cd0e86c` | `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json` |
| `M1|historical_seed` | `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z` | 8 | `c8005bcf6f3a113cfc050004eb5caa52151817b51841f86d81ee702aa5eba916` | `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json` |
| `M1|pre_professional` | `AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z` | 6 | `103aa4d4a5f619e85d5b43c4361310441633919c7390193c4ffc9b3aad830be8` | `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json` |
| `M2|active_current` | `AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z` | 3 | `3469d887e1d1f8f9603fce04fcb12838758c30f9baf5283d12578ce68723958d` | `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json` |
| `M2|historical_seed` | `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z` | 10 | `7516023547e3b53926a5430ef7828a2c0a5cc47c63e1db06babefe1419c0598a` | `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json` |
| `M2|pre_professional` | `AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z` | 6 | `875126c3ec97f093cbc891f19644f515dc4118267bdae974940dfecf554951f8` | `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json` |
| `M3|active_current` | `AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z` | 3 | `2c1e8c9f9f7af0941720c301220ed577bf1bb6a1684a8c2a99cfd5c92b2fc0cd` | `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topic-map-20260708T090359Z.json` |
| `M3|historical_seed` | `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z` | 9 | `6e537070a672f5f2fb76c35df5c057f99acc5d24a0f12fbdd292e94d56c1e755` | `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T093141Z/research-topic-map-20260708T090359Z.json` |
| `M3|pre_professional` | `AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z` | 6 | `629a991337c58990a16e14d0b8fa61b4346470e4383788e9a83d04a1e4800070` | `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z.backup-before-professional-gemini-20260708T120000Z/research-topic-map-20260708T090359Z.json` |

## Verification and safety

- Validation JSON: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/historical-topic-extension-map/20260708T231242Z/historical_topic_extension_validation_20260708T231242Z.json`.
- Active slug set matched the expected 9 active pilot-paper slugs.
- Every historical/intermediate source record has exactly one curated mapping row.
- Every active target named in the crosswalk is one of the verified active 9 slugs.
- Writes were limited to the overnight work root; no public/static frontend files were modified by this tick.
- No DB/API/page_versions/wiki publish/trust/deploy/restart/git/extra-cron/billing/OAuth/external-submission changes were performed.
- No active execution phrase.

# Public static PDF promotion receipt

Run ID: `PUBLIC_STATIC_PDF_PROMOTION_20260709T233457Z`
Created UTC: 2026-07-09T23:34:57Z
Source overnight cycle: 18
Source candidate root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_18_nine_papers`

## What changed
- Replaced the existing public Galaxy Evolution research-topic PDF files at their current URLs in both the working repo public root and the live-served public root.
- Also exposed the final actual-research sprint PDFs at a public static `actual-research-journal-sprint/latest/` route.

## Existing public PDF replacements
- `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf`: 234931 bytes -> 232814 bytes, sha256 `5cc61dbe98926269...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf`: 234931 bytes -> 232814 bytes, sha256 `5cc61dbe98926269...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf`: 234931 bytes -> 232814 bytes, sha256 `5cc61dbe98926269...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp2_environment_quenching_aas.pdf`: 59070 bytes -> 87014 bytes, sha256 `6e2c9bf7d55de31c...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp3_maintenance_heating_aas.pdf`: 59204 bytes -> 85376 bytes, sha256 `62c17761c3fc1813...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p1_outflow_escape_recycling_aas.pdf`: 288385 bytes -> 316743 bytes, sha256 `dcd9b67900170311...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p2_radio_jet_environment_aas.pdf`: 58906 bytes -> 85121 bytes, sha256 `55e5cf6638735079...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p3_feedback_transition_mass_aas.pdf`: 58387 bytes -> 90183 bytes, sha256 `c9c6f8e1497df918...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p1_multiphase_census_aas.pdf`: 59116 bytes -> 83480 bytes, sha256 `9503fe8ff89483d8...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p2_gas_depletion_efficiency_aas.pdf`: 182955 bytes -> 215066 bytes, sha256 `3cf494a6003c4f87...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p3_simulation_validation_aas.pdf`: 59768 bytes -> 92073 bytes, sha256 `a84eb37d9dcb82a2...`, source match=True

## New actual-research latest routes
- `/agent-reports/wiki-method-results/galaxy-evolution/actual-research-journal-sprint/latest/rp1_flagship_polished.pdf`: 273707 bytes, sha256 `249569cb3e519e3f...`, source match=True
- `/agent-reports/wiki-method-results/galaxy-evolution/actual-research-journal-sprint/latest/supplementary_denominator_atlas.pdf`: 559736 bytes, sha256 `044733c863fc9724...`, source match=True

## Safety
- db_writes: 0
- wiki_page_versions_writes: 0
- deploy_restart: 0
- git_commit_push_merge: 0
- cron_changes: 0
- billing_oauth_account_changes: 0
- external_submission: 0
- static_public_file_writes: 28

Backup root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/public-promotions/PUBLIC_STATIC_PDF_PROMOTION_20260709T233457Z/backups`

## Public verification after frontend static refresh
- Verification JSON: `.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/public-promotions/PUBLIC_STATIC_PDF_PROMOTION_20260709T233457Z/PUBLIC_STATIC_PDF_PROMOTION_PUBLIC_VERIFY_AFTER_REFRESH.json`
- all_ok: True
- frontend static refresh: old listener 49444 replaced by new listener 83967 from live frontend root
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf: ok=True status=200 bytes=232814 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf: ok=True status=200 bytes=232814 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/sdss_agn_sfr_pilot_aas.pdf: ok=True status=200 bytes=232814 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp2_environment_quenching_aas.pdf: ok=True status=200 bytes=87014 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/m1_rp3_maintenance_heating_aas.pdf: ok=True status=200 bytes=85376 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p1_outflow_escape_recycling_aas.pdf: ok=True status=200 bytes=316743 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p2_radio_jet_environment_aas.pdf: ok=True status=200 bytes=85121 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/m2_p3_feedback_transition_mass_aas.pdf: ok=True status=200 bytes=90183 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p1_multiphase_census_aas.pdf: ok=True status=200 bytes=83480 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p2_gas_depletion_efficiency_aas.pdf: ok=True status=200 bytes=215066 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/m3_p3_simulation_validation_aas.pdf: ok=True status=200 bytes=92073 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/actual-research-journal-sprint/latest/rp1_flagship_polished.pdf: ok=True status=200 bytes=273707 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/actual-research-journal-sprint/latest/supplementary_denominator_atlas.pdf: ok=True status=200 bytes=559736 match=True
- https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/actual-research-journal-sprint/latest/index.html: ok=True status=200 bytes=2068 match=True
- https://nebulamind.net/ideas: ok=True status=200 bytes=29550 match=None

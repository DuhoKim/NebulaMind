# Worktree Classification Report

## Snapshot
- **Branch**: feat/surveys-atlas-ia-p1-20260627
- **HEAD**: 826e733
- **Ahead/Behind**: 6 ahead / 66 behind `origin/main`
- **Counts**: 20 modified + 360 untracked = 380 entries

## Totals
- **KEEP-COMMIT**: 222
- **ARCHIVE**: 130
- **DELETE-CANDIDATE**: 18
- **UNKNOWN**: 10

## Protected Categories Summary
Protected paths include `.hermes/handoffs/**`, `.hermes/plans/**`, `.hermes/board/**`, `docs/**` research packets, `backend/tests/**`, `docs/claim_ledger_contract_v1_agn_20260703T0830Z/**`, and Contract v1 validators and receipts. They are never marked as `DELETE-CANDIDATE`. Mixed collapsed entries like `.hermes/` are protected-mixed `UNKNOWN`.

## DELETE-CANDIDATE
- `backend/app/main.py.bak-labrunner` (Reason: Reproducible/generated debris, Gate: G4b)
- `click.js` (Reason: Reproducible/generated debris, Gate: G4b)
- `find_deep.js` (Reason: Reproducible/generated debris, Gate: G4b)
- `find_menu.js` (Reason: Reproducible/generated debris, Gate: G4b)
- `goru_temp_report.json` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_applescript.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_inject.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_inject2.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_js_drop.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_js_innerhtml.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_js_insert.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_js_paste.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_js_rich_textarea.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_menu_paste.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_paste.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `test_type.applescript` (Reason: Reproducible/generated debris, Gate: G4b)
- `tmp_build_2929_trust_packet.py` (Reason: Reproducible/generated debris, Gate: G4b)
- `wait_and_extract.py` (Reason: Reproducible/generated debris, Gate: G4b)

## UNKNOWN
- `.claude/` (Question: Insufficient evidence)
- `.hermes.md` (Question: Insufficient evidence)
- `.hermes/` (Question: Collapsed mixed .hermes/ is protected-mixed)
- `backend/.env.redacted-before-disable-gemini-20260708_174609` (Question: Secret-adjacent, requires Hwao/human adjudication)
- `click_textarea.applescript` (Question: Insufficient evidence)
- `click_via_js.applescript` (Question: Insufficient evidence)
- `open_new_gemini.applescript` (Question: Insufficient evidence)
- `paste_submit.applescript` (Question: Insufficient evidence)
- `playwright_test/` (Question: Insufficient evidence)
- `run_js.applescript` (Question: Insufficient evidence)

## Dispositions & Held Gates
- **Archive**: Held behind G4a approval.
- **Deletion Candidates**: Held behind G4b.
- **Secret-Adjacent**: Held behind G4c.
- **Product Review**: Held behind G3.
- **Research Docs Preservation**: Held behind G3.

## Stop Rules
- Any unexplained drift in starting snapshot stops the classification.
- Protected categories must never be classified as `DELETE-CANDIDATE`.
- Safety ledger must prove zero moves, deletes, stashes, commits, branches, git writes, `.env*` content reads, DB actions, runtime actions, network, or publication.

## Entries
| Status | Path | Bucket | Reason | Protected |
|---|---|---|---|---|
|  M | `backend/app/routers/pages.py` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `backend/app/services/model_canary.py` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `backend/app/services/trust_calculation.py` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/package.json` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/scripts/test-surveys-atlas-ia.mjs` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/app/components/NavBar.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/app/ideas/IdeasIndexClient.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/app/ideas/page.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/app/page.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/components/surveys/BandSpectrumStrip.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/components/surveys/ChartView.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/components/surveys/FilterSheet.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/components/surveys/PlotB.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/components/surveys/SurveyCard.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/components/surveys/SurveyPeek.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `frontend/src/components/surveys/SurveysView.tsx` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `tools/lab_runner_worker.py` | KEEP-COMMIT | Modified tracked code/docs | False |
|  M | `wiki_schema.md` | KEEP-COMMIT | Modified tracked code/docs | False |
| ?? | `.claude/` | UNKNOWN | Insufficient evidence | False |
| ?? | `.hermes.md` | UNKNOWN | Insufficient evidence | False |
| ?? | `.hermes/` | UNKNOWN | Collapsed mixed .hermes/ is protected-mixed | True |
| ?? | `backend/.env.redacted-before-disable-gemini-20260708_174609` | UNKNOWN | Secret-adjacent, requires Hwao/human adjudication | False |
| ?? | `backend/app/main.py.bak-labrunner` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `backend/scripts/generate_video_gemini.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `backend/tests/test_cross_page_paper_footprint_api.py` | KEEP-COMMIT | Protected category | True |
| ?? | `backend/tests/test_global_paper_directory_api.py` | KEEP-COMMIT | Protected category | True |
| ?? | `backend/tests/test_model_canary.py` | KEEP-COMMIT | Protected category | True |
| ?? | `backend/tests/test_page_source_surface_fallbacks.py` | KEEP-COMMIT | Protected category | True |
| ?? | `backend/tests/test_paper_profile_api.py` | KEEP-COMMIT | Protected category | True |
| ?? | `backend/tests/test_trust_debate_stance_caps.py` | KEEP-COMMIT | Protected category | True |
| ?? | `click.js` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `click_textarea.applescript` | UNKNOWN | Insufficient evidence | False |
| ?? | `click_via_js.applescript` | UNKNOWN | Insufficient evidence | False |
| ?? | `docs/agent_progress_report_20260626T012412Z.html` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/agent_progress_report_20260626T014029Z.html` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/agent_progress_report_full_no_apply_completed_20260626T044900Z.html` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/agent_progress_report_full_no_apply_running_20260626T032300Z.html` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/agent_progress_report_full_no_apply_running_20260626T032700Z.html` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/agent_progress_report_interactive_20260626T014636Z.html` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/agent_progress_report_readiness_packet_20260626T025500Z.html` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/agent_progress_report_usage_monitor_20260626T034600Z.html` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/baseline_step6_status_debate_map_20260703T0954Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/baseline_step7_wording_contract_20260703T1007Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/baseline_step7a_b1_prime_contradiction_gold_20260703T1205Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/baseline_step7a_litdist_tool_eval_20260703T1012Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/baseline_step8_docs_only_prose_preview_20260703T1242Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/baseline_step9_exact_diff_packet_20260703T1306Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/baseline_step9b_claim_evidence_continuity_20260703T1329Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/baseline_step9c_readonly_db_evidence_match_20260703T1354Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/baseline_step9d_insert_heavy_exact_diff_prep_20260703T1500Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/baseline_step9e_claim_id_guarded_sql_packet_20260703T1532Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/baseline_step9e_claim_id_guarded_sql_packet_repaired_20260704T020002Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/claim2299_nuance_source_packet_20260703T041421Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/claim2299_strengthening_20260703T014356Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/claim_ledger_contract_v1_agn_20260703T0830Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/cockpit_simplification_20260703T012406Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/cockpit_single_writer_rootcause_20260704T103016Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/dashboard_usage_quota_update_20260712T155053Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/execution_2942_2947_trust_recompute_approved_20260704T180848Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy-post-label-readiness-analysis-20260627T121535Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy-post-label-readiness-analysis-20260627T121535Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy-post-label-readiness-analysis-20260627T121535Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_2181_2299_trust_conflicts_20260702T115202Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2299_source_decision_packet_20260703T001440Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_2299_sourcefill_v2_packet_20260703T003424Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_2557_live_refute_reconcile_20260702T113108Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2913_2921_exact_write_preflight_20260704T134546Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2913_2921_readonly_decision_packet_20260704T131018Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_2915_execution_and_cockpit_prevention_20260704T113605Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2915_scoped_replacement_exact_write_packet_20260704T111714Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_2915_scoped_replacement_preflight_20260704T105746Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2929_evidence_remap_audit_docs_only_20260704T170510Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_2929_evidence_remap_preflight_20260704T142442Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_2929_product_db_wiki_exact_diff_preflight_20260705T110725Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2929_source_position_queue_20260705T013911Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2929_trust_recompute_preflight_20260705T121124Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2942_2947_trust_model_status_correction_preflight_20260704T155315Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2942_2947_trust_recompute_readiness_fresh_20260704T164723Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_2942_2947_trust_recompute_readiness_preflight_20260704T151916Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_9h2_confirmed_cockpit_backup_20260707T005157Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_baseline_cockpit_refresh_20260704T122043Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_canonical_exact_diff_preflight_20260702T073312Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_canonical_merge_preview_packet_20260702T070000Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_claim_backlog_scoping_20260702T101316Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_claim_backlog_scoping_20260702T143028Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_claim_layer_held_coverage_decision_20260704T102251Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_claim_layer_reconciliation_preflight_20260704T082747Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_claim_layer_split_first_execution_20260704T095826Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_cockpit_clarity_quintet_20260704T091755Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_cockpit_ultra_format_gate_20260706T153234Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_cockpit_ultra_format_visible_action_20260706T153949Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_evolution_autonomous_quintet_hardening_20260704T071053Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_evolution_claim_layer_reconciliation_intake_20260704T073425Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_evolution_final_page_completion_readiness_gate_20260704T062937Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_evolution_final_page_completion_readiness_gate_20260704T063403Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_evolution_readonly_scope_reset_20260702T061500Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_held_claims_coverage_decision_20260704T102251Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_human_decision_clarity_backup_20260707T001006Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_human_decision_cockpit_update_20260706T234329Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_marker_normalization_execution_20260702T093507Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_marker_normalization_preflight_20260702T090333Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_page57_stance_audit_20260702T124152Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_page57_stance_exact_diff_prep_20260702T131029Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_page57_stance_write_packet_20260702T133041Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_page57_trust_recompute_preflight_20260702T145402Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_page57_trust_recompute_v2_trigger_fix_packet_20260702T164209Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_page57_trust_recompute_write_packet_20260702T153238Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_pick_c_cockpit_backup_20260707T002851Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_rich_baseline_cockpit_restore_20260704T104352Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_stable_cockpit_renderer_20260704T115307Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_stance_audit_scoping_20260702T121713Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_tranche1_snippet_verify_20260702T105047Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v1_absorb_retired_v2_prose_overhaul_20260703T043245Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_baseline_lock_20260627T125853Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_baseline_lock_20260627T125853Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_best_effort_evidence_map_20260627T165252Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_best_effort_markdown_diff_20260627T165252Z.patch` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_best_effort_preview_manifest_20260627T165252Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_best_effort_preview_packet_20260627T165252Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_best_effort_proposed_content_20260627T165252Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_blocked_assistant_hints_20260627T125853Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_blocked_assistant_hints_20260627T125853Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_calibration_definitions_20260627T125853Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_calibration_definitions_20260627T125853Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_claim_2929_candidate_registry_20260627T125853Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_claim_2929_candidate_registry_20260627T125853Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_claim_marker_inventory_20260627T125853Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_claim_marker_inventory_20260627T125853Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_content_publish_preflight_20260627T170527Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_counted_candidate_human_confirmation_manifest_20260627T153755Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_counted_candidate_human_confirmation_workspace_20260627T153755Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_counted_candidate_human_confirmation_workspace_20260627T153755Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_counted_candidate_human_confirmation_workspace_20260627T153755Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_disclaimer_fix_publish_preflight_20260627T172833Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_human_counted_votes_preflight_20260628T011555Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_live_qa_20260702T034618Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_phase1_code_safety_slice_20260627T175914Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_phase1_code_safety_slice_20260627T175914Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_phase5_preview_manifest_20260627T152717Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_post_confirmation_assistant_disagreements_20260627T164022Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_post_confirmation_audit_queue_20260627T164022Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_post_confirmation_claim_readiness_20260627T164022Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_post_confirmation_human_counted_candidates_20260627T164022Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_post_confirmation_missing_export_hold_20260627T154313Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_post_confirmation_missing_export_hold_20260627T154313Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_post_confirmation_missing_export_hold_manifest_20260627T154313Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_post_confirmation_readiness_20260627T164022Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_post_confirmation_readiness_20260627T164022Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_post_confirmation_readiness_manifest_20260627T164022Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_preview_outline_20260627T152717Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_preview_outline_20260627T152717Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_proposed_prose_diff_packet_DRAFT_20260627T152717Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_proposed_prose_diff_packet_DRAFT_20260627T152717Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_prose_cleanup_publish_preflight_20260627T180319Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_prose_overhaul_20260703T041421Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_prose_quality_checklist_20260627T125853Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_prose_quality_checklist_20260627T125853Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_recommended_sequence_manifest_20260627T125853Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_representative_audit_expansion_requirements_20260627T125853Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_representative_audit_expansion_requirements_20260627T125853Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_representative_audit_expansion_requirements_20260627T125853Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_representative_candidate_queue_20260627T130801Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_representative_candidate_queue_20260627T130801Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_representative_candidate_queue_20260627T130801Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_representative_queue_manifest_20260627T130801Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_scope_corrected_status_20260702T032010Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_section_conformance_20260627T125853Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_section_conformance_20260627T125853Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_source_surface_reconciliation_20260629.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_sources_page_deploy_preflight_20260702T041206Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_sources_page_exact_diff_packet_20260702T035242Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_targeted_audit_queue_20260627T125853Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_targeted_audit_queue_20260627T125853Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_tranche1_hermes_assisted_claim_readiness_20260627T153558Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_tranche1_hermes_assisted_counted_candidates_20260627T153558Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_tranche1_hermes_assisted_readiness_20260627T153558Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_tranche1_hermes_assisted_readiness_20260627T153558Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_tranche1_hermes_assisted_review_20260627T153558Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_tranche1_hermes_assisted_review_20260627T153558Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_tranche1_hermes_assisted_review_manifest_20260627T153558Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_tranche1_review_workspace_20260627T150814Z.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/galaxy_v2_tranche1_review_workspace_20260627T150814Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_tranche1_review_workspace_20260627T150814Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_tranche1_review_workspace_20260627T150814Z_rows.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_v6_board_baseline_20260627T175356Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_v6_board_baseline_20260627T175356Z.json.sha256` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/galaxy_v2_v6_board_baseline_20260627T175356Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/gemini_quota_pools.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/hwao_debate_map_refresh_20260706T002104Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/hwao_morning_blocker_specs_20260706T0308Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/hwao_morning_prepared_packets_20260706T0308Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/hwao_overnight_db_packet_prep_20260705T1615Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/hwao_overnight_pinning_atlas_20260705T153533Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/hwao_overnight_pinning_wave2_20260705T1615Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/hwao_p1_p3_readonly_preflight_20260706T0750Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/method1_cockpit_ultra_format_gate_20260706T154438Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/mission_resumption_20260702T081658Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/overnight_2942_2947_quintet_hardening_20260704T170510Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/overnight_step9e_readonly_hardening_20260703T1621Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/page58_audit_deferral_status_20260626T130951Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_audit_deferral_status_20260626T130951Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_audit_deferral_status_20260626T130951Z_critical_micro_audit.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_audit_deferral_status_20260626T130951Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_20260626T045946Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_20260626T045946Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_20260626T045946Z_labels.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_evidence_provenance_augmented_20260626T051913Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_evidence_provenance_augmented_20260626T051913Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_evidence_provenance_augmented_20260626T051913Z_labels.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_product_operator_augmented_20260626T051047Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_product_operator_augmented_20260626T051047Z_labels.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_reviewer_augmented_20260626T050601Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_reviewer_augmented_20260626T050601Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_calibration_spot_check_packet_reviewer_augmented_20260626T050601Z_labels.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_claim_trust_publish_preflight_20260626T113250Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/page58_completed_calibration_packet_20260626T124240Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_calibration_packet_20260626T124240Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_calibration_packet_20260626T124240Z_label_audit.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_calibration_packet_20260626T124240Z_labels.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_calibration_packet_20260626T124240Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_packet_calibration_analysis_20260626T130121Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_packet_calibration_analysis_20260626T130121Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_packet_calibration_analysis_20260626T130121Z_audit_queue.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_packet_calibration_analysis_20260626T130121Z_exact_removal_only_diff.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_packet_calibration_analysis_20260626T130121Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_completed_packet_calibration_analysis_20260626T130121Z_threshold_only_label_diff.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_fresh_no_apply_readiness_packet_20260626T025500Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_fresh_no_apply_readiness_packet_20260626T030000Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_full_no_apply_final_analysis_20260626T044700Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_full_no_apply_final_analysis_20260626T044700Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_full_no_apply_result_packet_20260626T044632Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_full_no_apply_result_packet_20260626T044632Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_partial_label_go_20260626T081326Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/page58_partial_label_go_20260626T081326Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/page58_post_label_calibration_readiness_20260626T123203Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/page58_post_label_calibration_readiness_20260626T123203Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/page58_post_label_calibration_readiness_20260626T123203Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_post_label_calibration_readiness_analysis_20260626T163722Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_post_label_calibration_readiness_analysis_20260626T163722Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_post_label_calibration_readiness_analysis_20260626T163722Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_priority0_calibration_audit_20260626T165934Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_priority0_calibration_audit_20260626T165934Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_priority0_calibration_audit_20260626T165934Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_priority0_calibration_audit_20260626T165934Z_rows.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_production_mutation_preflight_20260626T101849Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/page58_sentence0_remaining_driver_audit_20260626T172726Z.html` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_sentence0_remaining_driver_audit_20260626T172726Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_sentence0_remaining_driver_audit_20260626T172726Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_sentence0_remaining_driver_audit_20260626T172726Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_sentence0_remaining_driver_audit_20260626T172726Z_rows.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_sentence0_tier_shift_audit_20260626T171354Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_sentence0_tier_shift_audit_20260626T171354Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_sentence0_tier_shift_audit_20260626T171354Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_sentence0_tier_shift_audit_20260626T171354Z_rows.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_sentence_vote_staking_dry_run_20260626T032236Z_full_no_apply/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_vc076_human_confirmation_packet_20260626T174135Z.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_vc076_human_confirmation_packet_20260626T174135Z.md` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_vc076_human_confirmation_packet_20260626T174135Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/page58_vc076_human_confirmation_packet_20260626T174135Z_review.csv` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_citation_snippet_verification_top20_20260701T141717Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_claim_rewrite_assembly_top20_20260701T151453Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_claim_rewrite_packet_top20_20260701T135153Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_contradiction_adjudication_top20_20260701T124233Z_packet/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_distillation_pilot_artifacts_20260701T122648Z_manifest/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_overnight_distillation_20260702T002532Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_product_wiki_exact_diff_20260702T054507Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122022Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122022Z_contradiction_gaps.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122022Z_distillation_schema.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122022Z_page_readiness.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122022Z_paper_manifest.jsonl` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122022Z_prose_candidates.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122022Z_source_gaps.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122022Z_summary.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122351Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122351Z_contradiction_gaps.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122351Z_distillation_schema.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122351Z_page_readiness.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122351Z_paper_manifest.jsonl` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122351Z_prose_candidates.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122351Z_source_gaps.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122351Z_summary.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122648Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122648Z_contradiction_gaps.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122648Z_distillation_schema.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122648Z_page_readiness.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122648Z_paper_manifest.jsonl` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122648Z_prose_candidates.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122648Z_source_gaps.jsonl` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_prose_readiness_pilot_20260701T122648Z_summary.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/paper_source_acquisition_lock_top20_20260701T144153Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/paper_source_position_review_top20_20260701T145604Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/step9f_visible_content_prose_exact_diff_packet_20260704T022605Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/step9f_visible_content_prose_exact_diff_packet_20260704T022950Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/surveys_design_studio_20260626T132110Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/surveys_design_studio_20260626T132110Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/surveys_design_studio_20260626T132110Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/surveys_three_lane_synthesis_20260626T133153Z.json` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/surveys_three_lane_synthesis_20260626T133153Z.md` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/surveys_three_lane_synthesis_20260626T133153Z_manifest.json` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/tmp_step9f_discovery/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/uploads/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/v1_absorption_agn_feedback_section_packet_20260703T045032Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `docs/v1_paper_distillation_methods_survey_20260703T0716Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/white_dwarfs_baseline_target_kickoff_20260704T070207Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/white_dwarfs_step0_1_source_claim_ledger_intake_20260704T070538Z/` | KEEP-COMMIT | Canonical research artifact | True |
| ?? | `docs/youtube_quota_dashboard_backup_20260721T003905Z/` | ARCHIVE | Useful receipt/report | True |
| ?? | `find_deep.js` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `find_menu.js` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `frontend/public/agent-reports/` | KEEP-COMMIT | Real code/tests | False |
| ?? | `frontend/public/human-cal/` | KEEP-COMMIT | Real code/tests | False |
| ?? | `frontend/scripts/test-agent-report-upload.mjs` | KEEP-COMMIT | Real code/tests | False |
| ?? | `frontend/scripts/test-wiki-trust-visibility.mjs` | KEEP-COMMIT | Real code/tests | False |
| ?? | `frontend/src/app/agent-reports/` | KEEP-COMMIT | Real code/tests | False |
| ?? | `frontend/src/app/wiki/[slug]/trustVisibility.ts` | KEEP-COMMIT | Real code/tests | False |
| ?? | `frontend/src/lib/agentReportUpload.ts` | KEEP-COMMIT | Real code/tests | False |
| ?? | `goru_temp_report.json` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `open_new_gemini.applescript` | UNKNOWN | Insufficient evidence | False |
| ?? | `paste_submit.applescript` | UNKNOWN | Insufficient evidence | False |
| ?? | `playwright_test/` | UNKNOWN | Insufficient evidence | False |
| ?? | `run_js.applescript` | UNKNOWN | Insufficient evidence | False |
| ?? | `test_applescript.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_inject.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_inject2.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_js_drop.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_js_innerhtml.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_js_insert.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_js_paste.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_js_rich_textarea.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_menu_paste.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_paste.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `test_type.applescript` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `tests/` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tmp_build_2929_trust_packet.py` | DELETE-CANDIDATE | Reproducible/generated debris | False |
| ?? | `tools/R15_prompt.txt` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/build_hwao_2929_trust_recompute_stage_packet_20260705T122901Z.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/galaxy_evolution_autopilot.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/galaxy_evolution_autopilot.py.bak-20260710T160851Z-pre-route-line` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/ge_tex_publishability_lint.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/gemini_app_usage.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/gemini_app_usage.py.bak-20260710T173625Z-pre-crawler-provenance` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/gemini_app_usage_autofetch.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/gemini_app_usage_bookmarklet.js` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/gemini_app_usage_extractor.js` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/gemini_app_usage_ingest.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/gemini_app_usage_ingest.py.bak-20260710T150441Z` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/gemini_burn_plan_patch.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/gemini_deep_research_driver.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/live_provider_usage_monitor.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/live_provider_usage_monitor.py.bak-20260710T122621Z-pre-gemini-app-gauge` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/live_provider_usage_monitor.py.bak-20260710T135125Z-pre-copymode-fix` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/live_provider_usage_monitor.py.bak-20260710T173625Z-pre-crawler-provenance` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/nm_dispersion_v2.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/nm_fulltext_layer.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/nm_fulltext_mass_mine.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/nm_gates.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/nm_numeric_kb.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard_v2.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard_v2.py.bak-20260710T092345Z` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard_v2.py.bak-clean-display-20260710T100544Z` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard_v2.py.bak-clean-obsolete-20260709T092850Z` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard_v2.py.bak-overnight-20260718` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard_v2.py.bak-paper-final-cleanup-20260709T060005Z` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard_v2.py.bak-path-display-20260710T095553Z` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard_v2.py.bak-relay-incident-20260711T0500Z` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_ge_autopilot_dashboard_v2.py.bak-rp1-quality-20260709T0224Z` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_pipeline_board.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/render_run_page.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/stable_cockpit_guard.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/stable_cockpit_renderer.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/templates/` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/tests/` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/tmux_board_snapshot.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/tmux_board_summary.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `tools/watch_subnav_videos.py` | KEEP-COMMIT | Real code/tests | False |
| ?? | `wait_and_extract.py` | DELETE-CANDIDATE | Reproducible/generated debris | False |

GORU_PHASE1_WORKTREE_CLASSIFICATION_COMPLETE_20260721

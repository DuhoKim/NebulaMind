# LANA remaining-20 source-position judgment brief

Coordinator: Hwao/Fable. Relay/executor: Tori/Hermes. Lane: Lana.

User direction: finish the 20 remaining held 2929 rows as docs-only source-position / human-adjudication batches.

Hard locks:
- No queue edits by Lana.
- No SQL/apply/rollback files.
- No DB queries/connections/writes.
- No trust recompute.
- No prose/wiki publish.
- No runtime deploy/restart.
- No git commit/push/merge.
- No cron/cloud/account/secret changes.
- Gemini web quota held unless separately needed for a contested row; do not invoke it.

Inputs included below:
- Hwao remaining-20 batch plan.
- Pending rows context with summary snippets and candidate target claims.
- Public source-record/abstract probes captured by Tori from arXiv pages.
- Goru precheck PASS.

Task:
Produce a source-position + human-adjudication proposal for all 20 pending rows, grouped B4-B8. This is a proposal only; Tori will apply only after Hwao gate.

Decision rules:
- Use only allowed decision enums: relink, copy_source_fill, retire_reject, leave_archival, route_kinetic_radio.
- Prefer relink only when the snippet directly supports/challenges a scoped successor claim and duplicate/stacking risk is controlled.
- Use leave_archival/retire_reject for non-AGN, local cloud-scale, redundant, or topic-match-only rows that should not inflate successor evidence.
- Use route_kinetic_radio for real AGN jet/radio/kinetic rows better suited to 2947 than broad quenching/outflow claims.
- Cap every visible-successor row at accepted_limited unless the source context is directly pinned enough for accepted. Given current inputs, accepted_limited is expected.
- Use source_position_verification_status from: docs_verified, source_record_verified, abstract_only_verified, pdf_verified, not_applicable. Prefer docs_verified/source_record_verified if exact span comes from the queue snippet plus public source record/abstract, not full PDF pinning.
- Preserve product_publication_gate and write_lock.
- No source is a product/publication decision.

Output format:
1. Markdown report with per-batch/per-row reasoning.
2. Then a fenced block exactly named JSONL_PROPOSAL containing exactly 20 JSON objects, one per line.

Each JSON object must include:
- evidence_id
- batch_id
- decision_enum
- accepted_target_claim_id (number or null)
- accepted_target_stance
- accepted_for_docs_source_position
- source_position_verification_status
- accepted_support_role
- selected_role
- selected_stance_if_visible_successor
- human_decision
- decision_owner = Lana
- human_reviewer = Lana
- decision_reason
- decision_reason_plain_english
- source_accessed_url_or_path
- source_type
- exact_quote_or_paraphrase_source_span
- section
- paragraph_or_sentence_locator
- pdf_page
- figure_or_table
- source_position_note
- matched_terms (array)
- target_claim_id_if_any
- target_claim_text_if_any
- limitation_or_counter_reason
- dependency_handling_action
- duplicate_check_against_successor_evidence_ids
- anti_duplicate_check_status
- decision_confidence
- product_publication_gate = NO_GO_DB_OR_PRODUCT_PUBLICATION_UNDER_THIS_APPROVAL
- write_lock = NO_APPLY_SQL_NO_DB_WRITE_FROM_THIS_QUEUE
- proposal_marker = LANA_REMAINING20_SOURCE_POSITION_PROPOSAL_20260705T085714Z

End with standalone marker LANA_REMAINING20_SOURCE_POSITION_PROPOSAL_20260705T085714Z.

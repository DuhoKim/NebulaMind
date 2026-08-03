# LANA BRIEF — B3 source-position proposal

Marker required in both outputs: `LANA_B3_SOURCE_POSITION_PROPOSAL_20260705T044944Z`
Coordinator: Hwao/Fable
Relay: Tori/Hermes

## User/Hwao directive

Proceed with B3 under Hwao's same no-SQL, no-product-mutation lane order. You produce a read-only source-position/adjudication proposal only. Do not edit queue files.

Hwao directive:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/HWAO_B3_PLAN_AND_COCKPIT_DIRECTIVE.md`

Pre-edit snapshot:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/pre_edit_queue_snapshot_b3_20260705T044944Z/`

Queue snapshot file to inspect:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/pre_edit_queue_snapshot_b3_20260705T044944Z/source_position_human_adjudication_queue.json`

## B3 rows

Paper: arXiv `2403.17145` — galaxy groups as AGN-feedback probe.

Rows:

- `28123` / `SPQ-2929-28123`, target options `2946, 2942`, dependency counts all zero
- `28127` / `SPQ-2929-28127`, target options `2946, 2945, 2947`, dependency counts all zero
- `28139` / `SPQ-2929-28139`, target options `2946, 2947`, dependency counts all zero
- `28143` / `SPQ-2929-28143`, target options `2946, 2943`, dependency counts all zero
- `28151` / `SPQ-2929-28151`, target option `2946`, dependency counts all zero
- `28158` / `SPQ-2929-28158`, target options `2946, 2947`, dependency counts all zero

Re-confirm dependency counts from the snapshot. If any are non-zero, stop and write BLOCKED instead of proposing decisions.

## Source reading

Read arXiv `2403.17145`:

- abstract first;
- fetch full text if publicly accessible (arXiv HTML/PDF/source); six rows amortize the read;
- label each row honestly: `abstract_only_verified` or full-text verified with locators;
- full `accepted` requires full-text span pinning; otherwise cap at `accepted_limited`.

Allowed source access is public web/arXiv or local cached source files only. No DB queries.

## B3-specific rules from Hwao

### R1 — same-paper stacking cap

All six rows come from one paper and 2946 appears in every row's options. Do not let six same-paper rows become supports for one claim.

Default expectation:

- strongest one or two spans per target claim can proceed as `accepted_limited` or a role-distinct caution/limitation;
- redundant same-paper spans should be `leave_archival` with `redundant_same_paper` reasoning;
- if a row is genuinely role-distinct, explain why, following B2 row 28108 precedent.

### R2 — observational-heating gap flag

Claim 2946 is model-bounded because its evidence set is simulation-heavy. There is a standing gap card: no observational maintenance-heating evidence.

If a B3 span is observational group-scale heating evidence (X-ray cavities, bubbles, jet-inflated lobes, observational group-scale heating; not simulation and not review-of-simulations), add:

`gap_card_relevant: observational_maintenance_heating`

in the row note/JSON. Keep it capped as directed; do not upgrade to full accepted unless full-text pinned and Hwao later gates that.

### Zone caution

If the source is review/probe-style, review sentences are secondary synthesis, not primary measurement. Use background/qualifier roles when appropriate. Do not invent primary measurement status.

## Candidate handling

Options are hints, not orders. Apply source-first judgment.

Likely candidates from queue:

- 2946: maintenance/heating/model-bounded AGN feedback framing
- 2947: kinetic/radio-mode AGN feedback
- 2945: likely prevention/inflow/maintenance-adjacent successor; inspect target text from queue if present
- 2943: ejective outflow/removing star-forming gas; do not relink topic-match-only measuring/method sentences as support
- 2942: broad scoped AGN/SMBH feedback, not universal

For any 2947 route, duplicate/dedup set must include live `26681,26682,26683,26684,26685` plus already routed docs-only `28095,28111` plus caution row `28108`.

For 2946, record queue successor-evidence reference set if present in the row; otherwise use `db_dedup_deferred_to_sql_time`.

If a decision would require a new claim, park the row and write the proposed backlog note; do not invent a new target.

## Output files

Write exactly two files in this handoff dir:

1. `.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/LANA_B3_PROPOSAL.md`
2. `.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/lana_b3_proposal.jsonl`

The JSONL must contain exactly six rows, one JSON object per B3 evidence id.

Each JSON row must include, at minimum:

- `marker`
- `queue_id`
- `evidence_id`
- `dependency_counts`
- source fields: `source_accessed_url_or_path`, `source_type`, `section`, `pdf_page`, `figure_or_table`, `paragraph_or_sentence_locator`, `exact_quote_or_paraphrase_source_span`, `quote_context_before_after`, `matched_terms`, `source_position_note`, `source_position_verification_status`
- adjudication fields: `selected_role`, `selected_stance_if_visible_successor`, `accepted_target_claim_id`, `target_claim_id_if_any`, `target_claim_text_if_any`, `accepted_support_role`, `accepted_target_stance`, `accepted_for_docs_source_position`, `limitation_or_counter_reason`
- decision fields: `human_decision`, `human_decision_enum`, `decision_reason`, `decision_reason_plain_english`, `decision_confidence`, `decision_owner`, `human_reviewer`, `human_reviewed_at_utc`
- dependency fields: `dependency_handling_action`, `anti_duplicate_check_status`, `duplicate_check_against_successor_evidence_ids`
- B3 extras where applicable: `same_paper_stacking_decision`, `gap_card_relevant`, `new_claim_backlog_note`

Allowed decision enums: `relink`, `route_kinetic_radio`, `leave_archival`, `retire_reject`, `copy_source_fill`, `park_needs_new_claim`, `park_needs_full_text`, `park_source_identity_blocker`.

## Report structure

In `LANA_B3_PROPOSAL.md`, include:

- method/source access level;
- per-row reasoning;
- same-paper stacking summary;
- observational-heating gap-card summary;
- parked/blocker rows if any;
- no-write ledger;
- marker line.

## Hard locks

No queue edits, no SQL/DB queries/connections, no SQL files, no apply/rollback files, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git write/push/merge, no public cockpit edits. Two output files only.

LANA_B3_SOURCE_POSITION_PROPOSAL_20260705T044944Z

# LANA BRIEF — six vote-dependent source-position proposal

Marker required in both outputs: `LANA_SOURCE_POSITION_VOTE_ROWS_PROPOSAL_20260705T033735Z`
Coordinator: Hwao/Fable
Relay: Tori/Hermes

## User directive

Fill the source-position fields for the six vote-dependent rows first.
Hard lock: **No SQL until all 36 rows have completed human/source decisions.**

## Your role

Lana is the semantic/source-grounded lane. Read the source texts and propose source-position + adjudication values for exactly the six vote-dependent queue rows. Do not edit the queue files.

## Allowed roots / files

Repo root:
`/Users/duhokim/NebulaMind/NebulaMind`

Hwao plan:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/HWAO_PLAN.md`

Context JSON for the six rows:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/six_vote_rows_context.json`

Queue dir for read-only context only:
`docs/galaxy_2929_source_position_queue_20260705T013911Z`

## The six rows

- `SPQ-2929-28060` / evidence 28060 / SWAN NOEMA M51 / human vote 5048 value -1 / special caution: vote says row is about positive AGN feedback generally.
- `SPQ-2929-28091` / evidence 28091 / SWAN NOEMA M51 / human vote 5049 value +1.
- `SPQ-2929-28155` / evidence 28155 / SWAN NOEMA M51 / human vote 5053 value +1.
- `SPQ-2929-28095` / evidence 28095 / arXiv 2009.11175 / human vote 5050 value +1.
- `SPQ-2929-28111` / evidence 28111 / arXiv 2009.11175 / human vote 5051 value +1.
- `SPQ-2929-28141` / evidence 28141 / arXiv 1706.08987 / human vote 5052 value +1.

## Allowed source access

Docs-only/read-only. You may read local files and, if necessary, fetch public arXiv abstract/PDF text for source verification. If full text is unavailable, label the row `abstract_only_verified` and explain limitation. Do not use DB/psql/SQL. Do not create SQL/apply/rollback files.

## Fill/propose these fields per row

From `required_source_position_fields`:
- `source_accessed_url_or_path`
- `source_type`
- `section`
- `pdf_page`
- `figure_or_table`
- `paragraph_or_sentence_locator`
- `exact_quote_or_paraphrase_source_span`
- `quote_context_before_after`
- `matched_terms`
- `source_position_note`
- `source_position_verification_status`
- `selected_role`
- `selected_stance_if_visible_successor`
- `accepted_target_claim_id` / `target_claim_id_if_any`
- `target_claim_text_if_any`
- `accepted_support_role`
- `accepted_target_stance`
- `accepted_for_docs_source_position`
- `limitation_or_counter_reason`
- `human_decision`
- `human_decision_enum`
- `decision_reason`
- `decision_reason_plain_english`
- `decision_confidence`
- `dependency_handling_action` — mandatory and must mention the vote id.
- `anti_duplicate_check_status`
- `duplicate_check_against_successor_evidence_ids`
- `review_status`

Use allowed enums from each row’s template.

## Output files — only these two

1. Markdown report:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/LANA_SOURCE_POSITION_PROPOSAL.md`

2. Proposal JSONL, one row per evidence id:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/lana_source_position_proposal.jsonl`

## JSONL shape

Each line should be a JSON object:

```json
{
  "queue_id": "SPQ-2929-...",
  "evidence_id": 0,
  "vote_id": 0,
  "vote_value": 0,
  "source_accessed_url_or_path": "...",
  "source_type": "paper_pdf_or_authoritative_abstract_or_source_record",
  "section": "...",
  "pdf_page": "... or null",
  "figure_or_table": "... or null",
  "paragraph_or_sentence_locator": "...",
  "exact_quote_or_paraphrase_source_span": "...",
  "quote_context_before_after": "...",
  "matched_terms": ["..."],
  "source_position_note": "...",
  "source_position_verification_status": "verified | abstract_only_verified",
  "selected_role": "support | challenge | limitation_or_caution | background_only | not_applicable",
  "selected_stance_if_visible_successor": "supports | contradicts | none | needs_new_stance | not_applicable",
  "accepted_target_claim_id": 2942,
  "accepted_target_stance": "supports | contradicts | none | needs_new_stance | not_applicable",
  "accepted_support_role": "support | challenge | limitation_or_caution | background_only | not_applicable",
  "accepted_for_docs_source_position": "accepted | accepted_limited | rejected",
  "limitation_or_counter_reason": "... or null",
  "human_decision": "plain text",
  "human_decision_enum": "relink | copy_source_fill | retire_reject | leave_archival | route_kinetic_radio",
  "decision_reason": "...",
  "decision_reason_plain_english": "...",
  "decision_confidence": "high | medium | low",
  "dependency_handling_action": "must mention vote id and how honored",
  "anti_duplicate_check_status": "resolved_no_duplicate | resolved_existing_successor_duplicate | not_applicable",
  "duplicate_check_against_successor_evidence_ids": [],
  "review_status": "reviewed"
}
```

## Hard locks

- no DB queries/connections
- no SQL text generation
- no SQL/apply/rollback files
- no queue file edits
- no prose/wiki publish
- no runtime deploy/restart
- no git commit/push/merge
- no public cockpit update

Done only when both output files exist, contain all six rows, and the standalone marker appears in the Markdown report.

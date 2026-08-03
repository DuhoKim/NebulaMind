# GORU BRIEF — mechanical validation of Lana six-row source-position proposal

Marker required: `GORU_SOURCE_POSITION_VOTE_ROWS_VALIDATION_20260705T033735Z`
Coordinator: Hwao/Fable
Relay: Tori/Hermes

## Task

Mechanically validate Lana's six-row source-position proposal before any queue edit.

## Inputs

Repo root:
`/Users/duhokim/NebulaMind/NebulaMind`

Hwao plan:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/HWAO_PLAN.md`

Original six-row context:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/six_vote_rows_context.json`

Lana proposal report:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/LANA_SOURCE_POSITION_PROPOSAL.md`

Lana proposal JSONL:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/lana_source_position_proposal.jsonl`

Queue JSON read-only for enum templates:
`docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.json`

## Validate

1. Proposal JSONL parses as exactly 6 records with evidence ids exactly `[28060, 28091, 28095, 28111, 28141, 28155]`.
2. Every record has non-empty required fields or explicit `null` only where Hwao allowed n/a.
3. Enum values are inside each row's `required_source_position_fields` options:
   - `selected_role` / `accepted_support_role`
   - `selected_stance_if_visible_successor` / `accepted_target_stance`
   - `accepted_for_docs_source_position`
   - `human_decision_enum`
   - `review_status`
4. Target claim ids are only in `{2942, 2943, 2944, 2945, 2946, 2947}` or null.
5. Quotes/spans are non-empty and have locator fields (`section`, `paragraph_or_sentence_locator`, and either `pdf_page` or an explicit abstract/introduction-only note).
6. Vote consistency:
   - all six `dependency_handling_action` fields mention the vote id;
   - row 28060 with vote 5048 value -1 is not plain support+relink unless explicitly justified;
   - positive votes are not marked rejected without justification.
7. Anti-duplicate statuses are resolved, not pending.
8. No SQL/apply/rollback files were created by this proposal step; no queue files changed by Lana.

## Output — only this file

Write:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/GORU_VALIDATION.md`

Output format:
- Verdict: `PASS` or `BLOCKED_WITH_GAPS`
- Exact failed checks if any
- Per-row compact table
- Confirmation of no SQL/no DB/no apply/queue edits by this validation
- Standalone marker line: `GORU_SOURCE_POSITION_VOTE_ROWS_VALIDATION_20260705T033735Z`

Hard locks: no SQL, no DB, no apply files, no queue edits, no prose/runtime/git/public cockpit mutation.

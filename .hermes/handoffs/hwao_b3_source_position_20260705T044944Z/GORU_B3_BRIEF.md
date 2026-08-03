# GORU BRIEF — B3 mechanical validation

Marker required: `GORU_B3_VALIDATION_20260705T044944Z`
Coordinator: Hwao/Fable
Relay: Tori/Hermes

## Task

Mechanically validate Lana's B3 source-position proposal and Kun's B3 checker readiness before Hwao gate.

## Inputs

Hwao directive:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/HWAO_B3_PLAN_AND_COCKPIT_DIRECTIVE.md`

Lana proposal:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/LANA_B3_PROPOSAL.md`
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/lana_b3_proposal.jsonl`

Kun checker/config:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/kun_queue_checker.py`
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/kun_b3_checker_config.json`
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/KUN_B3_CHECKER_USAGE.md`

Pre-edit snapshot:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/pre_edit_queue_snapshot_b3_20260705T044944Z/`

## Validate Lana proposal

Check and report PASS/BLOCKED for:

1. JSONL parses and has exactly six rows: `28123`, `28127`, `28139`, `28143`, `28151`, `28158`.
2. Every row carries marker `LANA_B3_SOURCE_POSITION_PROPOSAL_20260705T044944Z`.
3. Every row has zero dependency counts; if not, BLOCK.
4. Decisions are valid and non-pending:
   - 28123: proposed `relink -> 2946`, support, `accepted_limited`
   - 28127: proposed `leave_archival`, background/redundant, `rejected`
   - 28139: proposed `leave_archival`, background/redundant, `rejected`
   - 28143: proposed `leave_archival`, background/scope-mismatch, `rejected`
   - 28151: proposed `relink -> 2942`, support, `accepted_limited`
   - 28158: proposed `relink -> 2946`, support, `accepted_limited`, gap-card relevant
5. All source statuses are `abstract_only_verified`; no row claims full accepted.
6. Required source fields present: accessed source, source type, section, locator, quote/span, quote context, matched terms, source note.
7. Decision fields present: human_decision, human_decision_enum, decision reason/plain-English reason, confidence, reviewer/owner/timestamp.
8. Product/publication gate remains no-go.
9. Same-paper stacking rule R1 honored: no claim gets more than two accepted/kept spans from this one paper; 2946 spans are role-distinct (model-dependence 28123 and observational/gap-card 28158); redundant rows are archival/rejected with redundant_same_paper reasoning.
10. Observational-heating gap rule R2 honored: 28158 has `gap_card_relevant: observational_maintenance_heating` and remains capped/secondary-synthesis, not used to move 2946 off model-bounded now.
11. 28143 is not falsely relinked to 2943 if scope mismatch exists; archival/non-support should be explicit.
12. No SQL/apply/rollback files were created in the queue dir or B3 handoff dir.

## Validate Kun checker readiness

Check and report PASS/BLOCKED for:

1. `kun_queue_checker.py` exists and Python AST parses.
2. Usage/config contains marker `KUN_B3_CHECKER_CONFIG_READY_20260705T044944Z`.
3. Script/config target B3 queue dir, B3 pre-edit snapshot, B3 edited ids, and B3 output JSON.
4. Script writes only the configured results JSON when run; it must not edit queue files.
5. Do not require the checker to PASS before queue edits; B3 rows are pending before Tori applies them.

## Output

Write one file only:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/GORU_B3_VALIDATION.md`

Include:

- verdict: PASS or BLOCKED;
- compact check table;
- exact blocker if any;
- no-write ledger;
- marker line `GORU_B3_VALIDATION_20260705T044944Z`.

## Hard locks

No queue edits, no SQL/DB queries/connections, no apply/rollback files, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git write/push/merge, no public cockpit edits.

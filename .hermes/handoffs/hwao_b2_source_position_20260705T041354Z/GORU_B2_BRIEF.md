# GORU BRIEF — B2 mechanical validation

Marker required: `GORU_B2_VALIDATION_20260705T041354Z`
Coordinator: Hwao/Fable
Relay: Tori/Hermes

## Task

Mechanically validate Lana's B2 source-position proposal and Kun's read-only checker readiness before Hwao gate.

## Inputs

Hwao directive:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/HWAO_B2_PLAN_AND_COCKPIT_DIRECTIVE.md`

Lana proposal:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/LANA_B2_PROPOSAL.md`
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/lana_b2_proposal.jsonl`

Kun checker:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/kun_queue_checker.py`
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/KUN_QUEUE_CHECKER_USAGE.md`

Queue snapshot:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/pre_edit_queue_snapshot_b2_20260705T041354Z/`

## Validate Lana proposal

Check and report PASS/BLOCKED for:

1. JSONL parses and has exactly four rows: `28087`, `28108`, `28133`, `28074`.
2. Every row carries marker `LANA_B2_SOURCE_POSITION_PROPOSAL_20260705T041354Z`.
3. Every row has zero dependency counts; if not, BLOCK.
4. Decisions are valid and non-pending:
   - 28087 `relink -> 2942`
   - 28108 `route_kinetic_radio -> 2947`
   - 28133 `leave_archival` (candidate 2943 context allowed, but no support relink)
   - 28074 `relink -> 2942`
5. All four are `accepted_limited`; none is full `accepted` because no full-text pinning.
6. All four have `source_position_verification_status = abstract_only_verified`.
7. Required source fields are present: accessed source, source type, section, locator, quote/span, quote context, matched terms, source note.
8. Decision fields are present: human_decision, human_decision_enum, decision reason/plain-English reason, confidence, reviewer/owner/timestamp.
9. Product/publication gate remains `NO_GO_DB_OR_PRODUCT_PUBLICATION_UNDER_THIS_APPROVAL` or equivalent no-go.
10. 28108 stacking judgment is explicitly present and includes duplicate/check set against live 2947 evidence `26681–26685` plus B1 docs-only rows `28095`, `28111`; role is `limitation_or_caution`, not extra support stacking.
11. 28133 is not falsely relinked as support; leave_archival/background-only is consistent with the methods/measurement sentence.
12. No SQL/apply/rollback files were created in the queue dir or handoff dir.

## Validate Kun checker readiness

Check and report PASS/BLOCKED for:

1. `kun_queue_checker.py` exists and Python AST parses.
2. Usage doc contains marker `KUN_B2_QUEUE_CHECKER_READY_20260705T041354Z`.
3. Script default paths point to the B2 queue and B2 snapshot.
4. Script writes only the configured results JSON in the B2 handoff dir when run; it must not edit queue files.
5. Do not require the checker to PASS before queue edits, because the live queue still has the four B2 rows pending. If you run it now, treat pending-row failures as expected pre-edit behavior and do not confuse that with Lana proposal failure.

## Output

Write one file only:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/GORU_B2_VALIDATION.md`

Include:

- verdict: PASS or BLOCKED;
- compact check table;
- any exact blocker;
- no-write ledger;
- marker line `GORU_B2_VALIDATION_20260705T041354Z`.

## Hard locks

No queue edits, no SQL/DB/apply/rollback files, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git write/push/merge, no public cockpit edits.

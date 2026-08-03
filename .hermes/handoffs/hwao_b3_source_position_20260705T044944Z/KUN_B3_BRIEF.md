# KUN BRIEF — B3 checker config/update

Marker required: `KUN_B3_CHECKER_CONFIG_READY_20260705T044944Z`
Coordinator: Hwao/Fable
Relay: Tori/Hermes

## Task

Prepare the read-only queue checker for B3.

Use the existing B2 checker as source:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/kun_queue_checker.py`

B3 handoff dir:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/`

B3 queue dir:
`docs/galaxy_2929_source_position_queue_20260705T013911Z/queue`

B3 pre-edit snapshot:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/pre_edit_queue_snapshot_b3_20260705T044944Z`

B3 edited ids:
`28123,28127,28139,28143,28151,28158`

Expected output path for post-apply checker result:
`.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/kun_queue_checker_results_b3_post_apply.json`

## Requirements

Hwao said reuse the B2 checker with config-only/default update if possible. Do not change validation logic unless absolutely necessary.

Deliver either:

A. if the B2 checker already supports args sufficiently:
   - copy the checker to `.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/kun_queue_checker.py` unchanged except defaults/comments if needed;
   - write `.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/kun_b3_checker_config.json` with B3 paths/ids/output;
   - write `.hermes/handoffs/hwao_b3_source_position_20260705T044944Z/KUN_B3_CHECKER_USAGE.md` with the exact run command.

or B. if tiny argument/config support is missing:
   - add only minimal config/argument support while preserving the B2 validation semantics;
   - write the same usage/config files.

The checker must remain read-only with respect to queue files. It may write only its configured results JSON.

## Validation to perform

- Python AST parse of the checker.
- Confirm defaults or usage command target B3 snapshot, B3 queue dir, B3 edited ids, and B3 output JSON.
- Do not require checker PASS before queue edits; B3 rows are still pending. If you run it pre-edit, pending-row failures are expected. Readiness is script/config validity, not pre-edit PASS.

## Output files

Write only these files in B3 handoff dir:

- `kun_queue_checker.py`
- `kun_b3_checker_config.json`
- `KUN_B3_CHECKER_USAGE.md`

Include marker `KUN_B3_CHECKER_CONFIG_READY_20260705T044944Z` in usage and/or config.

## Hard locks

No queue edits, no SQL/DB queries/connections, no SQL/apply/rollback files, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git write/push/merge, no public cockpit edits.

KUN_B3_CHECKER_CONFIG_READY_20260705T044944Z

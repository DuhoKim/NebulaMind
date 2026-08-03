# Hwao edit-gate request — six vote-dependent rows

Marker requested: `HWAO_SOURCE_POSITION_VOTE_ROWS_EDIT_GATE_20260705T033735Z`
From: Tori relay
To: Hwao/Fable coordinator

## User directive

Fill the source-position fields for the six vote-dependent rows first.
Hard lock: no SQL until all 36 rows have completed human/source decisions.

## Hwao plan completed through lanes

Plan:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/HWAO_PLAN.md`

Lana proposal:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/LANA_SOURCE_POSITION_PROPOSAL.md`
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/lana_source_position_proposal.jsonl`

Goru validation:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/GORU_VALIDATION.md`

Goru verdict: PASS.

Pre-edit queue snapshot already saved:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/pre_edit_queue_snapshot_20260705T033735Z/manifest.json`

## Request

Please review the lane outputs and write the edit gate at:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/HWAO_EDIT_GATE.md`

Include:
1. PASS/BLOCKED for Tori applying the six-row docs-only queue edits;
2. any changes Hwao requires relative to Lana's proposal;
3. exact files Tori may edit;
4. validation Tori must run;
5. whether cockpit stays unchanged or a later line is allowed.

Hard locks remain: no SQL, no DB, no apply/rollback files, no prose/runtime/git/public cockpit mutation unless explicitly later directed.

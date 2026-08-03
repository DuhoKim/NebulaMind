# Hwao next-batch request after six vote-dependent rows

Marker requested: `HWAO_REMAINING_30_SOURCE_POSITION_BATCH_PLAN_20260705T033735Z`
From: Tori relay
To: Hwao/Fable coordinator

## Current completed state

The six vote-dependent rows were filled docs-only after Hwao PASS gate.

Receipts:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/TORI_EDIT_RECEIPTS.md`

Validation:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/post_edit_validation.json`

Validation status: PASS.

Completed rows:
- 28060: `leave_archival`, no target, `abstract_only_verified`
- 28091: `relink -> 2943`, `abstract_only_verified`
- 28095: `route_kinetic_radio -> 2947`, `abstract_only_verified`
- 28111: `route_kinetic_radio -> 2947`, `abstract_only_verified`
- 28141: `relink -> 2943`, `abstract_only_verified`
- 28155: `relink -> 2942`, `abstract_only_verified`

Remaining: 30 rows pending.

Hard lock from user remains: **No SQL until all 36 rows have completed human/source decisions.**

## Request

Please write the next batching plan for the remaining 30 rows at:
`.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/HWAO_REMAINING_30_BATCH_PLAN.md`

Include:
1. source-paper batches for the remaining 30 rows;
2. lane order for Lana/Goru/Kun if needed;
3. whether to continue with abstract-only decisions or require full-text source pinning for some/all batches;
4. hard locks and stop conditions;
5. the first next batch Hwao recommends.

Plan only. Do not edit queue files. No SQL, no DB, no apply/rollback files, no prose/runtime/git/public cockpit mutation.

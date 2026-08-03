# GORU remaining-20 precheck brief

Task: mechanical counts/locks only before source-position decisions.

Context:
- 36-row 2929 source-position queue.
- Current parsed state: 16 completed, 20 pending.
- Pending rows are grouped in `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao_remaining20_source_position_20260705T085714Z/remaining20_pending_rows_context.json`.
- Hwao plan path: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao_remaining20_source_position_20260705T085714Z/HWAO_REMAINING20_PLAN_20260705T085714Z.md`.

Hard locks: no DB queries/writes, no SQL/apply/rollback, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git commit/push/merge, no cron/cloud/account/secret changes. Gemini web quota is held.

Report:
- PASS/BLOCKED on whether Hwao's 5 batches cover exactly 20 pending rows once each.
- Confirm no product execution is unlocked.
- List the 5 batch counts and total.
- End with marker GORU_REMAINING20_PRECHECK_20260705T085714Z.

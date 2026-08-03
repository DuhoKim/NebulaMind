# GORU post-apply counts/locks check

Task: mechanically review the post-apply validation for the remaining-20 2929 source-position pass.

Inputs to inspect:
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao_remaining20_source_position_20260705T085714Z/post_edit_validation_remaining20_amended.json`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao_remaining20_source_position_20260705T085714Z/HWAO_REMAINING20_COUNT_CORRECTION.md`

Expected actual final counts after Hwao count correction:
- 36 rows total.
- pending=0.
- relink=17.
- route_kinetic_radio=5.
- leave_archival=14.
- non-target changes: none.
- locked files/DML hits: none.

Hard locks: no SQL/apply/rollback, no DB read/write, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git commit/push/merge, no cron/cloud/account/secret changes, Gemini web quota unused.

Return PASS or BLOCKED. If PASS, explicitly say the amended counts are correct and locks are held. End with marker GORU_REMAINING20_POST_APPLY_COUNTS_LOCKS_20260705T103310Z.

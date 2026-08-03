# KUN visible lane brief — staged packet and phrase-boundary reproducibility check

Task ID: `STRICT_BOARD_VISIBLE_COCKPIT_20260705T124522Z`

You are Kun. This task must be visible in the actual `kun-codex` tmux pane.

Read:
- Hwao direction: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/HWAO_VISIBLE_COORDINATION_REPORT.md`
- Staged packet manifest: `/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z/artifacts/manifest.json`
- Staged packet validation: `/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z/validation/packet_validation.json`

Goal:
Check reproducibility/boundary facts for the staged trust recompute packet and phrase hygiene. This is read-only.

Check:
1. Execute script exists and is not run by this task.
2. Rollback script exists and is not active until after execution.
3. Manifest says target claims exactly 2929, 2942, 2943, 2944, 2945, 2946, 2947.
4. Validation status is PASS.
5. DB writes executed in validation are 0.
6. Trust recompute executions are 0.
7. Wiki/prose publish executions are 0.
8. Public cockpit must not promote the old Tori-solo scratch packet ID `galaxy_2929_trust_recompute_preflight_20260705T121124Z`.
9. Consumed DB-remap phrase must not be reused.

Hard excludes:
- No file edits except the requested report.
- No DB writes.
- No trust recompute execution.
- No prose/wiki publish.
- No git.
- No restart/deploy.
- No rollback.

Write report to:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/KUN_PACKET_BOUNDARY_REPORT.md`

Include:
- PASS or BLOCKED.
- Exact manifest/validation facts.
- Standalone marker line: `KUN_VISIBLE_PACKET_BOUNDARY_20260705T124522Z`.

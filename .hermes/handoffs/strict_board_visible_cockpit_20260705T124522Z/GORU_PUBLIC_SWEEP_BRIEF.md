# GORU visible lane brief — post-cockpit mechanical sweep

Task ID: `STRICT_BOARD_VISIBLE_COCKPIT_20260705T124522Z`

You are Goru. This task must be visible in the actual `goru-agy` tmux pane.

Read:
- Hwao direction: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/HWAO_VISIBLE_COORDINATION_REPORT.md`
- Lana brief: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/LANA_COCKPIT_UPDATE_BRIEF.md`

Goal:
After Lana patches the cockpit, perform a mechanical public-surface sweep.

You may wait/retry briefly for Lana's report/marker if not present yet.

Check:
1. Public cockpit/status/copy/latest routes return HTTP 200 where applicable.
2. The stable cockpit contains marker `GALAXY_TRUST_STAGE_DECISION_WAITING_20260705T124522Z`.
3. Phrase surfaces carry the staged recompute phrase:
   `APPROVE EXECUTE galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z`
4. Zero occurrences of consumed DB-remap phrase:
   `APPROVE EXECUTE galaxy_2929_product_db_wiki_exact_diff_preflight_20260705T110725Z`
5. Zero occurrences of scratch/non-authoritative phrase:
   `APPROVE EXECUTE galaxy_2929_trust_recompute_preflight_20260705T121124Z`
6. Zero rollback phrase public exposure.
7. Required rich cockpit anchors survive: `RICH_BASELINE_STABLE_COCKPIT_V1`, `baseline`, `baseline-steps`, `lane-board`, `safety-ledger`.
8. Status JSON is consistent with the cockpit card.

Hard excludes:
- No file edits.
- No DB writes.
- No trust recompute execution.
- No prose/wiki publish.
- No git.
- No restart/deploy.
- No rollback.

Write report to:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/GORU_PUBLIC_SWEEP_REPORT.md`

Include:
- PASS or BLOCKED.
- Exact URLs checked and booleans.
- Any stale phrase/marker occurrences.
- Standalone marker line: `GORU_VISIBLE_PUBLIC_SWEEP_20260705T124522Z`.

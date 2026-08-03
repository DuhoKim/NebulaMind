# HWAO/BOARD BRIEF — debate-map refresh track C — 20260706T002104Z

Goal: rebuild a docs-only research-status/debate map over the post-remap, post-recompute, post-wave2-pinning Galaxy Evolution board, diffed against `docs/baseline_step6_status_debate_map_20260703T0954Z/`.

Run dir: `docs/hwao_debate_map_refresh_20260706T002104Z/`.

Tori has already written read-only inputs:
- `debate_map_data.json`
- `claim_evidence_summary.csv`
- `TORI_READONLY_EXTRACT.md`

Lane order:
1. Goru writes mechanical counts: `GORU_DEBATE_MAP_COUNTS.md`, marker `GORU_DEBATE_MAP_COUNTS_20260706T002104Z`.
2. Lana writes science layer: `LANA_DEBATE_MAP_SCIENCE.md`, marker `LANA_DEBATE_MAP_SCIENCE_20260706T002104Z`.
3. Kun may write a re-runnable map-data checker after Goru/Lana artifacts exist.
4. Hwao synthesizes `DEBATE_MAP_REFRESH.md`, marker `DEBATE_MAP_REFRESH_COMPLETE_20260706T002104Z`, and appends a morning decision menu to `docs/hwao_overnight_pinning_atlas_20260705T153533Z/OVERNIGHT_RESULT.md`.

Locks: docs-only/read-only; no DB writes; no exact-diff execution; no prose/wiki product publish; no deploy/restart; no git mutation; no extra fetching; active execution phrase remains `NO ACTIVE EXECUTION PHRASE`.

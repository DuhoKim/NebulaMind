# Goru brief — pinning atlas mechanical review

Marker: `GORU_PINNING_ATLAS_MECHANICAL_20260705T153533Z`

Read first:

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/overnight_autonomy_20260705T153533Z/HWAO_OVERNIGHT_DIRECTION.md`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/hwao_overnight_pinning_atlas_20260705T153533Z/evidence_source_inventory.json`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/hwao_overnight_pinning_atlas_20260705T153533Z/evidence_source_inventory.csv`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/hwao_overnight_pinning_atlas_20260705T153533Z/pinning_backlog_prioritized.json`
- `/Users/duhokim/NebulaMind/NebulaMind/docs/hwao_overnight_pinning_atlas_20260705T153533Z/CHECKER_RESULT.json`

Task: mechanical count/map review only.

Scope:

- read local artifacts above;
- run local read-only parsing/count/checksum commands if needed;
- write only `/Users/duhokim/NebulaMind/NebulaMind/docs/hwao_overnight_pinning_atlas_20260705T153533Z/GORU_COVERAGE_MATRIX_REPORT.md`.

Checks requested:

1. Confirm JSON and CSV row counts match.
2. Confirm summary counts reconcile: 397 active evidence rows, 203 unique sources, 3 local full-text sources, 3 already-pinned evidence rows, 10 ready-to-pin rows, 384 missing-fulltext rows, 200 missing-fulltext sources, 200/200 arXiv abstract availability OK.
3. Confirm no `.sql`, `apply*`, `rollback*`, or migration artifacts exist in the run dir.
4. List the top 10 `READY_TO_PIN` rows by score and the top 10 `MISSING_FULL_TEXT` sources by evidence_count.
5. Note any count mismatch or malformed field as BLOCKED.

Hard excludes:

No DB queries, no SQL/apply/rollback files, no writes outside the one report, no prose/wiki/page_versions publish, no git, no deploy/restart, no secrets/account/billing/GCP/API/provider changes, no web browsing beyond reading local artifacts.

Report format:

- Verdict: PASS or BLOCKED.
- Count reconciliation table.
- Top 10 ready-to-pin rows.
- Top 10 missing-fulltext source groups.
- Safety ledger: DB writes 0; SQL/apply 0; prose/wiki 0; git/deploy/restart 0.
- Standalone final marker line: `GORU_PINNING_ATLAS_MECHANICAL_20260705T153533Z`.

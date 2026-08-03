# KUN BRIEF — B2 read-only queue checker

Marker required in output files: `KUN_B2_QUEUE_CHECKER_READY_20260705T041354Z`
Coordinator: Hwao/Fable
Relay: Tori/Hermes

## Task

Write a reusable read-only queue-edit checker for B2 and later batches.

Hwao directive:
- The checker must be ready before the B2 edit step.
- It may run in parallel with Lana's source proposal.
- It must be read-only against the queue files and snapshot.
- It may write only its own results JSON into this handoff directory.

## Scope

Allowed to create/update only these files:

1. `.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/kun_queue_checker.py`
2. `.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/KUN_QUEUE_CHECKER_USAGE.md`

The checker, when run later, may write a results JSON only inside:
`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/`

## Inputs the checker should accept

Defaults should work from repo root, but support args if practical:

- live queue dir: `docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/`
- snapshot dir: `.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/pre_edit_queue_snapshot_b2_20260705T041354Z/`
- edited row ids: `28087,28108,28133,28074`
- output JSON path default: `.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/kun_queue_checker_results.json`

## Required checks

- parse all four queue formats: JSON, JSONL, CSV, Markdown table;
- assert 36 rows in each;
- assert edited row ids are present;
- compare untouched rows against the snapshot:
  - JSON: canonical row hash unchanged for non-target rows;
  - JSONL: non-target line bytes unchanged;
  - CSV: non-target line bytes unchanged;
  - Markdown: non-target table lines unchanged;
- for edited rows:
  - non-pending decision enum;
  - required source-position fields non-empty or explicitly n/a;
  - enum values valid enough to catch typos;
  - quote/span and section/locator present;
  - product gate and write lock preserved;
  - source payload hash changed for edited rows only if JSON changed;
  - cross-format decision/review/source-status consistency;
- no `.sql` files and no `apply`/`rollback` files in the queue dir;
- no SQL/DML keywords in the queue artifacts. Avoid false positives by allowing the literal word `SQL` in lock text but flag `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `BEGIN`, `COMMIT`, `ROLLBACK`, `CREATE TABLE`, `ALTER TABLE`.

## Output shape

The checker should print JSON to stdout and write JSON results to the output path. Include:

- `marker`
- `pass`
- `row_counts`
- `other_rows_unchanged`
- `edited_rows`
- `format_consistency`
- `lock_checks`
- `failed_checks`
- `checked_at_utc`

## Hard locks

No SQL, no DB, no apply/rollback files, no queue edits, no runtime deploy/restart, no git write/push/merge, no public cockpit edits.

Done marker: standalone line `KUN_B2_QUEUE_CHECKER_READY_20260705T041354Z` in the usage doc.

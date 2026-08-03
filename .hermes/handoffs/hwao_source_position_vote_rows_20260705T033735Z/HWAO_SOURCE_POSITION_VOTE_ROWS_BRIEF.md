# Hwao brief — six vote-dependent source-position rows first

Marker: `HWAO_SOURCE_POSITION_VOTE_ROWS_BRIEF_20260705T033735Z`
From: User via Tori relay
To: Hwao/Fable coordinator

## User directive

Fill the source-position fields for the six vote-dependent rows first.

Hard lock from user: **No SQL until all 36 rows have completed human/source decisions.**

## Current operating model

- Hwao/Fable coordinates/plans.
- Tori/Hermes relays, records, verifies receipts/files/markers, and executes bounded docs-only edits only if Hwao/user directs.
- Tori must not create or run SQL, rotate execution phrases, or update the public cockpit unless Hwao/user directs.

## Scope

Use existing docs artifacts only. Do not run psql, do not query DB, do not create SQL/apply files.

Primary queue directory:
`/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_source_position_queue_20260705T013911Z`

Primary queue files:
- `queue/source_position_human_adjudication_queue.json`
- `queue/source_position_human_adjudication_queue.jsonl`
- `queue/source_position_human_adjudication_queue.csv`
- `queue/source_position_human_adjudication_queue.md`

Existing vote snapshot:
- `snapshots/vote_rows_full_for_helper_patch.json`

Existing helper QA report:
- `reports/2929_HELPER_QA_RECONCILIATION.md`

## Requested Hwao plan-brief

Please write the plan/assignment at:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao_source_position_vote_rows_20260705T033735Z/HWAO_PLAN.md`

Include:
1. the exact six vote-dependent queue row IDs/ticket IDs to fill first;
2. the fields that must be filled for each row;
3. whether Hwao wants Lana/Goru lanes before Tori edits;
4. exact no-SQL/no-apply/no-DB boundaries;
5. validation checks Tori should run after docs-only edits;
6. whether public cockpit should remain unchanged or receive a later Hwao-directed line.

Do not write SQL. Do not touch DB/prose/runtime/git/public cockpit.

# Async board QA applied — Tori memory hardening

Status: `ASYNC_BOARD_QA_APPLIED_STALE_HERMESOPS_RESTORED`
Timestamp UTC: `20260705T030736Z`

## What the board found

The cockpit-preservation lane found a real risk: `/Users/duhokim/HermesOps/cockpit/live-steering-cockpit.html` was stale/minimal and did not contain the protected rich Baseline cockpit markers. Sidecar files in the same directory were stale too.

## What Tori did

- Confirmed the two public roots matched and contained the rich Baseline markers.
- Backed up the stale HermesOps static cockpit bundle.
- Restored the HermesOps static cockpit bundle from the rich public root.
- Patched durable contracts so future work does not use stale/minimal HermesOps files as templates.
- Updated the paused cron prompt with the same source-hierarchy rule.

## Backup

`/Users/duhokim/HermesOps/cockpit/backup-before-rich-baseline-restore-20260705T030736Z/`

Restore report:
`/Users/duhokim/HermesOps/cockpit/backup-before-rich-baseline-restore-20260705T030736Z/restore_report.json`

## Verified after restore

All three static roots now match for:

- `live-steering-cockpit.html`
- `live-steering-status.json`
- `mobile.html`
- `copy-execution-phrase.html`
- `latest-execution-phrase.txt`

Protected rich markers preserved in `live-steering-cockpit.html`:

- `RICH_BASELINE_STABLE_COCKPIT_V1`
- `id="baseline"`
- `id="baseline-steps"`
- `id="lane-board"`
- `id="safety-ledger"`

Public URL probe passed for cockpit/status/mobile/copy/latest. Latest phrase remains `NO ACTIVE EXECUTION PHRASE`.

## No-write ledger

- DB writes: `0`
- SQL/apply files: `0`
- prose/wiki publish: `0`
- NebulaMind runtime deploy/restart: `false`
- git commit/push/merge: `false`
- public cockpit redesign/rewrite: `false`

## Durable guard layers updated

- always-visible user memory
- repo `.hermes.md`
- `cockpit-handoff-review` skill main contract
- `cockpit-handoff-review/references/tori-board-captain-memory-contract.md`
- local board-captain handoff
- active local-only cron prompt

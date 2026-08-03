# Tori receipt — autopilot run-time estimates on private dashboard

Timestamp: 2026-07-07T16:00Z
Marker: TORI_AUTOPILOT_RUNTIME_ESTIMATES_DASHBOARD_20260707T1600Z

## User request

Add estimated running time on the dashboard for each autopilot run.

## What changed

1. Updated the autopilot controller:
   `/Users/duhokim/NebulaMind/NebulaMind/tools/galaxy_evolution_autopilot.py`

   New status JSON block:
   `run_estimates`

   New marker:
   `GE_AUTOPILOT_RUN_TIME_ESTIMATES_V1`

   The controller now records one run-time estimate row per dispatched order in `autopilot-state.json`.

2. Updated the private dashboard renderer:
   `/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py`

   New dashboard section:
   `Autopilot run time estimates`

   Each run card shows:
   - order/run marker
   - state
   - dispatch count
   - elapsed running time
   - configured estimated total run window
   - ETA timestamp
   - remaining or overdue time
   - started/updated timestamps

## Estimate rule

Default estimated total run window:
`8h`

Config override:
`NEBULAMIND_GE_AUTOPILOT_ESTIMATED_RUN_SECONDS`

Per-run override if needed later:
`estimated_total_seconds` inside that order's state entry.

These are steering estimates, not completion guarantees.

## Current verified dashboard state

Private dashboard URL:
`https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html`

Current run shown:
- `GORU_RUTHLESS_USAGE_SURGE_20260707T144039Z`
- state: `running`
- elapsed: about `1h 19m`
- estimate: `8h`
- remaining: about `6h 40m`

Dashboard status remains:
- health: `RUNNING CLEAN`
- blockers: `0`

## Verification

Commands/checks run:

- `python3 -m py_compile tools/galaxy_evolution_autopilot.py tools/render_ge_autopilot_dashboard_v2.py` — PASS
- `python3 tools/galaxy_evolution_autopilot.py self-test` — PASS
- `python3 tools/galaxy_evolution_autopilot.py status --tail --tail-lines 40 --json` — PASS
- `python3 tools/render_ge_autopilot_dashboard_v2.py --json` — PASS
- Local private HTML contains `Autopilot run time estimates` — PASS
- Local private HTML contains `GE_AUTOPILOT_RUN_TIME_ESTIMATES_V1` — PASS
- Local private JSON contains `GE_AUTOPILOT_RUN_TIME_ESTIMATES_V1` and `elapsed_label` — PASS
- Tailnet HTML contains `Autopilot run time estimates` and `GE_AUTOPILOT_RUN_TIME_ESTIMATES_V1` — PASS
- Tailnet JSON contains `GE_AUTOPILOT_RUN_TIME_ESTIMATES_V1` — PASS

## Watcher refresh

To prevent old in-memory code from overwriting the new runtime cards, I restarted only the two private autopilot/dashboard watcher processes:

- old autopilot watcher PID stopped: `64810`
- new autopilot watcher session: `proc_604eeb0516b1`
- new autopilot watcher PID: `8742`

- old private dashboard renderer PID stopped: `97022`
- new private dashboard renderer session: `proc_229b57cb7efc`
- new private dashboard renderer PID: `9061`

## Safety ledger

No NebulaMind product DB writes, SQL/apply packet execution, `/api/pages`, `page_versions`, live wiki publish, app/backend deploy/restart, git commit/push/merge, public Baseline cockpit edit, cloud/GCP/API/billing/OAuth/token/secret work, browser automation, cron creation, or method content publication.

Only local autopilot controller/dashboard code and private tailnet dashboard status rendering were changed.

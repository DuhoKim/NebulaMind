# Tori-director receipt — private dashboard issue resolved

Marker: TORI_DASHBOARD_ISSUE_RESOLVED_20260707T121712Z
Author: Tori-director
Time: 2026-07-07T12:17:12Z / 2026-07-07 21:17:12 KST
Scope: private tailnet Galaxy Evolution autopilot dashboard only.

## Issue

The private dashboard route was serving, but the generated HTML/JSON no longer contained the exact V2 probe marker `GE_AUTOPILOT_PRIVATE_DASHBOARD_V2`; it had advanced to V3. The running private renderer watcher had also been started before the latest renderer source changes, so one-shot renders could be overwritten by stale watcher output.

## Fix applied

Changed renderer only:
- `/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py`

Patch summary:
- Kept current marker as `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3`.
- Added V2 compatibility marker `GE_AUTOPILOT_PRIVATE_DASHBOARD_V2`.
- Added `compat_markers` to private status JSON.
- Added compatibility markers to the HTML footer.
- Ensured the HTML footer includes the usage feed marker `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`.

Process action:
- Stopped stale private dashboard watcher PID 29367.
- Started fresh private dashboard watcher PID 54884 via `python3 tools/render_ge_autopilot_dashboard_v2.py --watch --interval 20`.
- Did not restart NebulaMind runtime/frontend/backend or public cockpit services.

## Verification

Local compile:
- `python3 -m py_compile tools/render_ge_autopilot_dashboard_v2.py tools/galaxy_evolution_autopilot.py` PASS.

One-shot render:
- Private HTML `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html` contains:
  - `GE_AUTOPILOT_PRIVATE_DASHBOARD_V2`
  - `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3`
  - `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`
- Private JSON `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json` contains the same markers.

Tailnet after one watcher refresh interval:
- `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html` HTTP 200.
- HTML contains `GE_AUTOPILOT_PRIVATE_DASHBOARD_V2`, `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3`, and `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`.
- `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot-status.json` HTTP 200.
- JSON marker: `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3`.
- JSON compatibility markers: `GE_AUTOPILOT_PRIVATE_DASHBOARD_V2`, `GE_AUTOPILOT_PRIVATE_DASHBOARD_V1`.
- Usage feed marker: `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`.
- Health: `healthy` / `RUNNING CLEAN`.
- Blockers: 0.
- Source age observed: 10s.

Watcher health:
- New private dashboard watcher PID 54884 running and emitting healthy ticks.
- Autopilot watcher PID 44650 still running; no method dispatch touched.

## Safety ledger

Private dashboard static/renderer fix only. No DB/SQL. No `/api/pages`. No `page_versions`. No live wiki publish. No product deploy/restart. No git commit/push/merge. No public NebulaMind cockpit/Baseline edit. No cloud/GCP/Gemini/billing/OAuth/secrets. No browser automation. No cron. No new method work or method dispatch.

TORI_DASHBOARD_ISSUE_RESOLVED_20260707T121712Z

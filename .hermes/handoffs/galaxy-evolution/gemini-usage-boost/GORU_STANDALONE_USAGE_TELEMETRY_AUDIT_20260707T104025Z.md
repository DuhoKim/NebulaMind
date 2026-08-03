# Goru Standalone Telemetry Audit Report

Marker: `GORU_STANDALONE_USAGE_TELEMETRY_AUDIT_20260707T104025Z`

## PASS/WARN/FAIL Table

| Check | Status | Details |
| --- | --- | --- |
| Local files inspected | PASS | All 6 requested files found and read. |
| Marker propagation | PASS | `PROVIDER_USAGE_REALTIME_MONITOR_V1`, `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`, and `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3` present. |
| Provider gauges | PASS | 4 gauges consistent: Claude/Fable/Lana, Codex/Kun, Gemini/Goru, Tori/Hermes. |
| Action-like surfaces | PASS | No `<button>`, `<form>`, or `POST` found. `fetch(` targets only same-origin local JSON. |
| Secret-like output | PASS | No `sk-`, `access_token`, `refresh_token`, or emails found in HTML/JSON. |
| Gemini/Goru gauge source | PASS | Captured strictly from tmux visible pane `/usage` commands, no API/billing endpoints hit. |

## Exact File Paths Read
1. `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/live-steering-cockpit.html`
2. `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/live-steering-status.json`
3. `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html`
4. `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json`
5. `/Users/duhokim/NebulaMind/NebulaMind/tools/live_provider_usage_monitor.py`
6. `/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py`

## Exact Counts & Markers
- **Public usage realtime marker:** `PROVIDER_USAGE_REALTIME_MONITOR_V1`
- **Private feed marker:** `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`
- **Private dashboard marker:** `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3`
- **Gauges present:** 4 (Claude / Fable / Lana, Codex / Kun, Gemini / Goru, Tori / Hermes)
- **Active Gemini/Goru panes (from JSON):** 4

## Timestamp Sync & Lag
- **Public monitor observed:** `2026-07-07T10:42:50Z`
- **Private monitor sync:** `2026-07-07T10:42:50Z`
- **Dashboard generated:** `2026-07-07T10:43:35Z`
- **Lag:** 0 lag between the public observed time and private synchronized time (both match exactly). The cache age was 45 seconds at the time of private dashboard generation. No stale or unexpected skew detected.

## Gemini/Goru Gauge Source Verification
Verified from `live_provider_usage_monitor.py` that the script explicitly issues a tmux `capture-pane` combined with a `send-keys /usage` command when it detects an idle Antigravity pane. It parses the resulting CLI text (`parse_agy_usage`) to extract percentage values. At no point does it initiate a network request, touch Google Cloud / Vertex endpoints, or read billing account APIs.

GORU_STANDALONE_USAGE_TELEMETRY_AUDIT_DONE_20260707T104025Z

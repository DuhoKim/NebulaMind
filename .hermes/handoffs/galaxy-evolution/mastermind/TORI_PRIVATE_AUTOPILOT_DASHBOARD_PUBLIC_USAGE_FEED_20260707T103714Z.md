# Private autopilot dashboard public realtime usage feed receipt

Marker: `TORI_PRIVATE_AUTOPILOT_DASHBOARD_PUBLIC_USAGE_FEED_20260707T103714Z`
Dashboard feed marker: `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`
Public feed marker: `PROVIDER_USAGE_REALTIME_MONITOR_V1`
Status: PASS
Private dashboard URL: https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html

## What changed

The private Galaxy Evolution autopilot dashboard now mirrors the same provider usage gauges used by the public live steering cockpit.

Changed renderer:

- `/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py`

Generated private outputs:

- `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html`
- `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json`

The private dashboard reads the shared local public status JSON:

- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/live-steering-status.json`

and embeds it into the private dashboard JSON as:

- `usage_monitor.marker = GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`
- `usage_monitor.provider_monitor_marker = PROVIDER_USAGE_REALTIME_MONITOR_V1`

## Current verified values

From private `ge-autopilot-status.json` after render:

- Claude / Fable / Lana: `Fable 22% used · all Claude 16% used`
- Codex / Kun: `gpt-5.5 3% used 5h · 4% used weekly`
- Gemini / Goru: `Gemini 0% used weekly · 1% used 5h`
- Tori / Hermes: `up to 69% context used`

The private cards include the public cockpit sub-gauges:

- Claude: 2 sub-gauges
- Codex: 4 sub-gauges
- Gemini/Goru: 4 sub-gauges
- Tori/Hermes: context gauge

## Realtime verification

Private dashboard JSON freshness advanced while the monitor loops were running:

- first local observed timestamp: `2026-07-07T10:35:34Z`
- second local observed timestamp: `2026-07-07T10:36:34Z`
- advanced: `true`

Tailnet status JSON check:

- URL: `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot-status.json`
- HTTP status: 200
- observed timestamp: `2026-07-07T10:36:34Z`
- marker: `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`

Local/tailnet page checks:

- local HTML contains `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3`: yes
- local HTML contains `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`: yes
- local JSON contains `PROVIDER_USAGE_REALTIME_MONITOR_V1`: yes
- local HTTP page: 200
- local HTTP status JSON: 200
- tailnet page: 200

Running monitor sessions:

- `ge-auto-dashboard`: alive
- `ge-provider-usage-monitor`: alive

## Safety verification

- `<button>` count in generated private HTML/JSON: 0
- `<form>` count in generated private HTML/JSON: 0
- secret-like email/token/API-key patterns in generated private HTML/JSON: none found
- no new browser automation
- no provider API/billing/account/payment/OAuth/GCP/credits action
- no credential/token/cookie file reads
- no DB writes, SQL, live wiki publish, deploy/restart, git commit/push/merge, cron

## Caveat

The private dashboard mirrors the public safe monitor. It is as realtime as that safe monitor: browser refresh every 5 seconds, private renderer refresh every 20 seconds, public usage status refresh every 60 seconds, and safe idle-pane quota slash refresh every 300 seconds.

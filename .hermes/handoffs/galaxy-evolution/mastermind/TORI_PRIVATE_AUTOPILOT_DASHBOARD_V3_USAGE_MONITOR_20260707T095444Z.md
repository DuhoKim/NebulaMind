# Tori private autopilot dashboard V3 usage monitor receipt

Marker: `TORI_PRIVATE_AUTOPILOT_DASHBOARD_V3_USAGE_MONITOR_20260707T095444Z`
Status: PASS
URL: https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html

## What changed

Added a read-only `Usage limit monitor` section to the private Galaxy Evolution autopilot dashboard.

The monitor now reports:

- Hermes / Tori local 7-day activity from `hermes insights --days 7`.
- Claude Code / Hwao+Lana active pane counts plus redacted credential-presence count from `hermes auth list`.
- Goru / Antigravity Gemini active pane counts from tmux status.
- Kun / Codex CLI active pane counts plus redacted credential-presence count from `hermes auth list`.
- Honest percent gauges: when a provider does not expose a safe local quota percentage, the dashboard shows `—% / not exposed by safe CLI` instead of guessing.

## Files / artifacts

- Renderer: `/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py`
- Private HTML: `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html`
- Private JSON: `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json`
- Usage cache: `/Users/duhokim/HermesOps/cockpit/ge-autopilot-usage-cache.json`

## Verification

- Python compile: PASS
- One-shot render: PASS
- V3 HTML marker `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3`: PASS
- V3 JSON marker `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3`: PASS
- Usage marker `GE_USAGE_LIMIT_MONITOR_V1`: PASS
- Usage cards: 4
- Local HTTP route body marker and usage section: PASS
- Tailnet HTTP route body marker and usage section: PASS
- No `<button>`: PASS
- No `<form>`: PASS
- No `post`/mutation wording/action surface: PASS
- No external `cdn` dependency: PASS
- Secret-looking string scan across generated HTML/JSON/cache: PASS
- Dashboard watcher `ge-auto-dashboard`: restarted and alive

## Safety ledger

No DB writes. No live wiki publish. No deploy. No service restart other than the private dashboard watcher. No git commit/push/merge. No public NebulaMind cockpit/Baseline mutation. No browser automation. No cron. No provider billing/API calls. No token/credential file reads or prints.

## Caveat

Exact Claude/Codex/Gemini subscription limit percentages are not exposed by the safe local CLIs found on this machine. The dashboard intentionally reports those as `not exposed` until a provider-specific safe source is approved or installed.

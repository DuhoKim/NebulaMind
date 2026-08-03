# Public cockpit realtime usage monitor receipt

Marker: `TORI_PUBLIC_COCKPIT_REALTIME_USAGE_MONITOR_20260707T102422Z`
Monitor marker: `PROVIDER_USAGE_REALTIME_MONITOR_V1`
Status: PASS
Public URL: https://nebulamind.net/agent-reports/live-steering-cockpit.html

## What changed

The public live steering cockpit now shows provider usage gauges through an as-realtime-as-safely-possible path:

1. Browser-side polling on the public page:
   - `live-steering-cockpit.html` polls `live-steering-status.json` every 5 seconds with cache-busting.
   - The provider gauge grid is updated in-place from the JSON.
   - No external JavaScript, CDN, form, or button was added.

2. Local safe writer loop:
   - tmux session: `ge-provider-usage-monitor`
   - Script: `/Users/duhokim/NebulaMind/NebulaMind/tools/live_provider_usage_monitor.py`
   - Log: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/logs/provider-usage-monitor.log`
   - Refresh cadence: writes the static public JSON/HTML every 60 seconds.
   - Safe visible slash refresh: every 300 seconds, only when panes are idle.

3. Safe sources:
   - Codex / Kun: visible idle Codex `/status` panel.
   - Gemini / Goru: visible idle Antigravity `/usage` panel.
   - Tori / Hermes: visible tmux status-line context percentages.
   - Claude / Fable / Lana: last visible Claude usage-panel values retained, because safe local Claude CLI does not expose a fresh non-interactive usage percent.

## Current verified public values

From public `live-steering-status.json` at verification time:

- Claude / Fable / Lana: `Fable 22% used · all Claude 16% used`
- Codex / Kun: `gpt-5.5 3% used 5h · 4% used weekly`
- Gemini / Goru: `Gemini 0% used weekly · 1% used 5h`
- Tori / Hermes: `up to 69% context used`

Public status JSON monitor observed timestamp advanced:

- First: `2026-07-07T10:21:46Z`
- Second: `2026-07-07T10:23:00Z`
- Freshness advanced: `true`

## Verification

Stable guard:

- `tools/stable_cockpit_guard.py check --marker USER_CONFIRM_9H2_WORK_RESUMED_COCKPIT_20260707T005127Z`: PASS
- Public HTTP 200: PASS
- Rich Baseline protected markers preserved: PASS
- `id="provider-usage-gauges"`: present
- `id="provider-usage-grid"`: present
- `PROVIDER_USAGE_REALTIME_MONITOR_V1`: present in public cockpit HTML and public status JSON
- `NO ACTIVE EXECUTION PHRASE`: present
- Stable files relocked with `uchg`: PASS
- Stale cockpit writer process scan: empty

Public safety scan:

- `<button>` count: 0
- `<form>` count: 0
- Secret-like email/token/API-key patterns in generated public HTML/JSON/mobile: none found
- No external CDN/font/analytics dependency added

## Safety ledger

Executed:

- Static cockpit/status renderer update: yes
- Local tmux watcher start: yes, for usage monitor only
- Safe visible `/status` on idle Codex pane: yes
- Safe visible `/usage` on idle Antigravity pane: yes

Not executed:

- DB writes / SQL / migration: 0
- Live wiki / page_versions publish: 0
- Trust recompute: 0
- Runtime deploy/restart: 0
- Git commit/push/merge: 0
- Browser automation: 0
- Cron: 0
- Cloud/API/GCP/billing/account/payment/credits/OAuth/token action: 0
- Credential/token/cookie file read: 0

## Caveat

This is as realtime as safely available from local visible status surfaces. It is not a provider billing dashboard. Claude exact usage remains the last visible usage-panel value because no safe local non-interactive Claude usage percent is exposed.

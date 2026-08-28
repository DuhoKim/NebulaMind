# Tori read-only inventory — private cockpit usage-limit coverage defect

- Marker: `TORI_COCKPIT_USAGE_LIMIT_COVERAGE_INVENTORY_20260810T1733K`
- Authority: `DUHO_COCKPIT_USAGE_LIMIT_COVERAGE_CORRECTION_20260810T1727K`
- Target: private Tailnet dashboard `ge-autopilot.html` / `ge-autopilot-status.json`
- Inventory only: no write to cockpit/public source, no restart, no provider/account/browser action.

## Root cause visible now

The private renderer is healthy and still rendering every 20 seconds, but its upstream provider-usage monitor is absent. The last upstream observation is `2026-08-09T04:02:37Z`, now `28h 29m` old. Current private JSON therefore reports:

- `cache_state: stale-source-hidden`
- `provider_monitor_status: stale-hidden`
- `cards: 3`
- `provider_gauge_count_hidden_as_stale: 9`

This is why Duho sees only three usage-limit cards. It is not primarily a missing-HTML problem.

## Cards still visible

1. `Kimi / Moonshot direct API` — stale official balance, no fixed denominator.
2. `Flow / Veo credits (Ultra)` — stale operator-confirmed balance; percent withheld.
3. `YouTube Data API` — official daily limits; exact remaining quota unavailable.

## Provider cards hidden because the upstream feed is stale

The current public source contains these six operational provider cards that the private renderer drops when its source is older than one hour:

1. `Claude / Fable / Lana` — Fable 5-hour, Fable weekly, all-models weekly; Opus/Sonnet weekly fields present but unobserved.
2. `Gemini app / consumer` — current-window and weekly compute meters.
3. `Hermes / Nous credits` — monthly plan pool and purchased top-up balance.
4. `Moonshot / Kun (Kimi K3)` — direct wallet balance. This overlaps the private Kimi wallet card and needs deduplication rather than two apparent budgets.
5. `Antigravity / Gemini` — Gemini weekly and 5-hour agent-request pool; Antigravity Claude/GPT fields present but unobserved.
6. `Codex` — GPT 5-hour/weekly and Spark 5-hour/weekly fields; several exact values are unobserved.

The stale branch counts nine because it builds six retained public-provider cards plus the private Kimi, Flow, and YouTube cards, then displays only the final three.

## Deliberately absent or unavailable pools

These should not be invented:

- Tori/Hermes context-window use is intentionally filtered because it is not subscription quota.
- Gemini CLI OAuth quota is a distinct pool and is not currently collected.
- `generativelanguage` API-key RPM/TPM/RPD is a distinct pool and the project documents that key lane as disabled.
- Exact Codex 5-hour headroom, Claude per-model weekly meters, and Antigravity Claude/GPT meters are present as named fields but currently unobserved.
- Kimi purchased cash has no fixed maximum, so it cannot truthfully produce a percent-used gauge.
- YouTube exposes official ceilings and per-operation costs but not exact remaining shared units through its normal API.

## Writer/process finding

- Private renderer: PID `31235`, alive since 2026-08-08 14:09 KST, launched after the current renderer source mtime; no evidence that it needs a restart for a source-only recovery.
- Upstream `live_provider_usage_monitor.py`: no running process or tmux session found.
- Established prior command from the preserved manifest: `python3 tools/live_provider_usage_monitor.py --watch --interval 60 --slash-interval 300`.

## Exact recovery choices

### A. Restore current values

Start only the established upstream monitor. The live private renderer should ingest the refreshed feed automatically within its next 20-second pass; no private-renderer restart should be needed.

This is gated because the monitor reads the local Claude OAuth credential to call the read-only usage endpoint, invokes Hermes' read-only Nous account reader, calls the official Moonshot balance endpoint with an in-memory key, may send `/status` or `/usage` only to idle visible Codex/Antigravity panes, and rewrites guarded public cockpit/status files. It does not open billing/payment/account pages or mutate provider accounts.

### B. Preserve structural coverage during future outages

Patch the private renderer's stale branch so all provider cards remain visible as `Stale`/`Unknown`, with current percentages removed and old values moved into explicitly historical copy, instead of hiding six cards. This is a source edit and requires a separate bounded private-renderer restart to activate. It should also deduplicate the two Kimi wallet representations.

### Recommended

Approve A first for fresh values. Then stage B as an exact-diff preflight so a stopped monitor can never again make most limits disappear. Keep every meter separate and preserve `fresh`, `stale`, `unknown`, and `planning envelope` as distinct states.

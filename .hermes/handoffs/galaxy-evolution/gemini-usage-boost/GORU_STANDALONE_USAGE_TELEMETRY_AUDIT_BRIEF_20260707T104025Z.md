# Goru standalone Gemini usage boost packet — realtime telemetry audit

Marker: `GORU_STANDALONE_USAGE_TELEMETRY_AUDIT_BRIEF_20260707T104025Z`
Target: standalone Goru / Antigravity Gemini lane
Purpose: Increase Gemini/Goru usage safely by doing a useful read-only audit of the public/private usage telemetry path.

## Safety boundary

Allowed:
- Read local static HTML/JSON/Markdown files under `/Users/duhokim/NebulaMind/NebulaMind`, `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports`, and `/Users/duhokim/HermesOps/cockpit`.
- Run read-only shell/Python inspections if Antigravity requests command permission.
- Write exactly one report under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/`.

Forbidden:
- No DB/SQL writes, no `/api/pages`, no page_versions, no live wiki publish.
- No deploy/restart/service mutation.
- No git commit/push/merge/rebase/reset.
- No public cockpit mutation.
- No cloud/GCP/Gemini API/billing/account/payment/credits/OAuth/token/secrets/.env.
- No browser automation, no cron.
- Do not read credential/token/cookie files.

## Task

Perform a thorough read-only telemetry audit of the usage-limit monitor chain:

1. Inspect these local files if present:
   - `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/live-steering-cockpit.html`
   - `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/live-steering-status.json`
   - `/Users/duhokim/HermesOps/cockpit/ge-autopilot.html`
   - `/Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json`
   - `/Users/duhokim/NebulaMind/NebulaMind/tools/live_provider_usage_monitor.py`
   - `/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py`
2. Verify marker propagation:
   - `PROVIDER_USAGE_REALTIME_MONITOR_V1`
   - `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`
   - `GE_AUTOPILOT_PRIVATE_DASHBOARD_V3`
3. Verify the four provider gauges are present and consistently described across public and private JSON:
   - Claude / Fable / Lana
   - Codex / Kun
   - Gemini / Goru
   - Tori / Hermes
4. Compute or record the public monitor observed timestamp, private monitor observed timestamp, and lag between them if both are parseable.
5. Check the generated public/private HTML strings for action-like surfaces: `<button>`, `<form>`, `POST`, `fetch(` destinations beyond same-origin status JSON.
6. Check for obvious secret-like output in the generated public/private HTML/JSON only: email-like strings, `sk-`, `access_token`, `refresh_token`. Do not open credential files.
7. Produce a report with:
   - PASS/WARN/FAIL table
   - exact file paths read
   - exact counts/markers
   - any mismatch or stale timestamp
   - whether the Gemini/Goru gauge is truly from visible Antigravity `/usage` and not a billing/API source

## Output

Write exactly:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/GORU_STANDALONE_USAGE_TELEMETRY_AUDIT_20260707T104025Z.md`

End the report with:
`GORU_STANDALONE_USAGE_TELEMETRY_AUDIT_DONE_20260707T104025Z`

# Tori -> Goru dispatch

Target: goru
Timestamp: 20260707T125210Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260707T125210Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

GORU BRIEF — DASHBOARD-USAGE-AUDIT-20260707T124934Z

Model: Gemini / Antigravity available in this existing Goru pane.
Goal: useful usage boost via a bounded read-only mechanical audit of the private Galaxy Evolution autopilot dashboard and usage feed.

Allowed read paths:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot-status.json
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot-events.jsonl
- /Users/duhokim/NebulaMind/NebulaMind/tools/galaxy_evolution_autopilot.py
- /Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py
- /Users/duhokim/HermesOps/cockpit/ge-autopilot.html
- /Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json
- /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/live-steering-status.json

Checks:
1. Verify current private HTML/JSON markers: GE_AUTOPILOT_PRIVATE_DASHBOARD_V2, GE_AUTOPILOT_PRIVATE_DASHBOARD_V3, GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1.
2. Verify status JSON reports healthy/RUNNING CLEAN or record the exact current non-clean state.
3. Verify hard gates remain closed in status JSON.
4. Verify private dashboard source has no action surface: no <button>, no <form>, no POST/action affordance, no external CDN/font/analytics strings.
5. Verify provider usage cards count is 4 in the private JSON usage_monitor, or record mismatch.
6. Verify no obvious secret-looking token/API-key/email string appears in generated private HTML/JSON. Do not read credential files.
7. Write concise PASS/WARN/FAIL report.

Report path:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/goru-usage-boost-20260707T124934Z/GORU_DASHBOARD_USAGE_AUDIT_REPORT_20260707T124934Z.md

Report must include standalone marker:
GORU_DASHBOARD_USAGE_AUDIT_DONE_20260707T124934Z

Hard boundary:
- Read local files only. No web/network.
- Write exactly the requested report file and nothing else.
- No DB/SQL, /api/pages, page_versions, live wiki publish, deploy/restart, git commit/push/merge, public cockpit/Baseline edits, cloud/GCP/API/billing/OAuth/token/secret/credential/cookie reads, browser automation, cron, or method content publication.
- If a permission prompt appears, approve only one-time local read/write commands that exactly match this brief; do not choose always-allow. If uncertain, stop and write BLOCKED in the report.

Done marker: TORI_GORU_DISPATCH_DONE_20260707T125210Z

```

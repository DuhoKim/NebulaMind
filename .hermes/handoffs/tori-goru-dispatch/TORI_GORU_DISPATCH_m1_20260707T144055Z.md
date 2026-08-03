# Tori -> Goru dispatch

Target: m1
Timestamp: 20260707T144055Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260707T144055Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

GORU BRIEF — GORU_RUTHLESS_USAGE_SURGE_20260707T144039Z — G2 private autopilot status/schema audit
Goal: Audit the private autopilot dashboard JSON/HTML against the source autopilot status and identify stale/missing fields that could make the dashboard look less useful.
Allowed read roots:
- /Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py
- /Users/duhokim/NebulaMind/NebulaMind/tools/galaxy_evolution_autopilot.py
- /Users/duhokim/HermesOps/cockpit/ge-autopilot.html
- /Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot-status.json
Checks:
1. Compare source status panes/blockers/targets counts to rendered private JSON counts/groups.
2. Check markers GE_AUTOPILOT_PRIVATE_DASHBOARD_V3 and GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1 in HTML/JSON where expected.
3. Check whether dashboard JSON has non-empty groups and lane summaries.
4. Write PASS/WARN/FAIL with exact counts and paths; do not fix anything.
Report path:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/goru-ruthless-usage-20260707T144039Z/GORU_G2_PRIVATE_AUTOPILOT_SCHEMA_AUDIT_REPORT_20260707T144039Z.md
Report must include standalone marker:
GORU_G2_PRIVATE_AUTOPILOT_SCHEMA_AUDIT_DONE_20260707T144039Z
Hard boundary:
- Read local files only. No web/network.
- Write exactly the requested report file and nothing else.
- No DB/SQL, /api/pages, page_versions, live wiki publish, deploy/restart, git commit/push/merge, public cockpit/Baseline edits, cloud/GCP/API/billing/OAuth/token/secret/credential/cookie reads, browser automation, cron, or method content publication.
- If a permission prompt appears, approve only one-time local read/write commands that exactly match this brief; do not choose always-allow. If uncertain, stop and write BLOCKED in the report.

Done marker: TORI_GORU_DISPATCH_DONE_20260707T144055Z

```

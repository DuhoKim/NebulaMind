# Tori -> Goru dispatch

Target: m2
Timestamp: 20260707T144056Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260707T144056Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

GORU BRIEF — GORU_RUTHLESS_USAGE_SURGE_20260707T144039Z — G3 Surveys current surface mechanical audit
Goal: Mechanically verify the Surveys Atlas implementation surface that may be confused with an autopilot Survey tab.
Allowed read roots:
- /Users/duhokim/NebulaMind/NebulaMind/frontend/scripts/test-surveys-atlas-ia.mjs
- /Users/duhokim/NebulaMind/NebulaMind/frontend/src/app/surveys
- /Users/duhokim/NebulaMind/NebulaMind/frontend/src/components/surveys
- /Users/duhokim/NebulaMind/NebulaMind/docs/survey_explorer_design_v1.md
- /Users/duhokim/NebulaMind/NebulaMind/docs/survey_detail_page_v1.md
Checks:
1. Inventory the main Surveys route/components and report whether this is a frontend /surveys feature, not part of the private ge-autopilot dashboard.
2. Confirm whether test-surveys-atlas-ia.mjs currently expects PlotB, URL param validation, and accessibility assertions.
3. Do not run npm/tests; inspect files only.
4. Write PASS/WARN/FAIL with exact files and a short missing-risk list.
Report path:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/goru-ruthless-usage-20260707T144039Z/GORU_G3_SURVEYS_CURRENT_SURFACE_AUDIT_REPORT_20260707T144039Z.md
Report must include standalone marker:
GORU_G3_SURVEYS_CURRENT_SURFACE_AUDIT_DONE_20260707T144039Z
Hard boundary:
- Read local files only. No web/network.
- Write exactly the requested report file and nothing else.
- No DB/SQL, /api/pages, page_versions, live wiki publish, deploy/restart, git commit/push/merge, public cockpit/Baseline edits, cloud/GCP/API/billing/OAuth/token/secret/credential/cookie reads, browser automation, cron, or method content publication.
- If a permission prompt appears, approve only one-time local read/write commands that exactly match this brief; do not choose always-allow. If uncertain, stop and write BLOCKED in the report.

Done marker: TORI_GORU_DISPATCH_DONE_20260707T144056Z

```

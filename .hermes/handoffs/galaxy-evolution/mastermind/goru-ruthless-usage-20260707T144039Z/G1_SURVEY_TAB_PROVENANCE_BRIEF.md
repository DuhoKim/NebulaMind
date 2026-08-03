GORU BRIEF — GORU_RUTHLESS_USAGE_SURGE_20260707T144039Z — G1 survey-tab provenance audit
Goal: Explain mechanically why the private Galaxy Evolution autopilot dashboard has no Survey/Surveys/Atlas tab right now.
Allowed read roots:
- /Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py
- /Users/duhokim/NebulaMind/NebulaMind/tools/galaxy_evolution_autopilot.py
- /Users/duhokim/HermesOps/cockpit/ge-autopilot.html
- /Users/duhokim/HermesOps/cockpit/ge-autopilot-status.json
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot-status.json
Checks:
1. Count exact occurrences of Survey, Surveys, survey, surveys, Atlas, atlas in the private dashboard HTML and JSON.
2. Identify the dashboard group/tab names rendered by the private dashboard source.
3. State whether the private GE autopilot dashboard currently has any Survey tab implementation.
4. If absent, state the likely cause only from files: GE dashboard is scoped to Directors + Method 1/2/3 + Other, not Surveys.
Report path:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/goru-ruthless-usage-20260707T144039Z/GORU_G1_SURVEY_TAB_PROVENANCE_REPORT_20260707T144039Z.md
Report must include standalone marker:
GORU_G1_SURVEY_TAB_PROVENANCE_DONE_20260707T144039Z
Hard boundary:
- Read local files only. No web/network.
- Write exactly the requested report file and nothing else.
- No DB/SQL, /api/pages, page_versions, live wiki publish, deploy/restart, git commit/push/merge, public cockpit/Baseline edits, cloud/GCP/API/billing/OAuth/token/secret/credential/cookie reads, browser automation, cron, or method content publication.
- If a permission prompt appears, approve only one-time local read/write commands that exactly match this brief; do not choose always-allow. If uncertain, stop and write BLOCKED in the report.

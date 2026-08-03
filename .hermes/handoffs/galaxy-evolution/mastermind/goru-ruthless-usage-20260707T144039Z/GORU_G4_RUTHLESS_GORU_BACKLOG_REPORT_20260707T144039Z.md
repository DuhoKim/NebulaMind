# Goru Ruthless Usage Surge - G4 Backlog Generator

Markers:
`GORU_G4_RUTHLESS_GORU_BACKLOG_DONE_20260707T144039Z`
`TORI_GORU_DISPATCH_DONE_20260707T144056Z`

## Goal
Generate a mechanical backlog of safe future Goru/Antigravity packets that consume Gemini quota usefully via read-only mechanical checks, while strictly adhering to hard boundary gates. 

---

## Part 1: Galaxy Evolution Autopilot Packets

### 1. Autopilot Controller State Audit
* **Allowed Roots:** `.hermes/handoffs/galaxy-evolution/mastermind`, `tools/galaxy_evolution_autopilot.py`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_AUDIT_STATE_*.md`
* **Useful Verification:** Verify JSON parse integrity of `autopilot-state.json`, count unresolved blockers, and cross-check active pane allocations against known allowed Hwao/Goru/Kun sessions.
* **Explicit Hard-Deny Gates:** No DB/SQL, no live deploy/restart, no `/api/pages`, no git push/commit.

### 2. Mastermind Dashboard Status Verification
* **Allowed Roots:** `.hermes/handoffs/galaxy-evolution/mastermind`, `tools/render_ge_autopilot_dashboard_v2.py`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_AUDIT_STATUS_*.md`
* **Useful Verification:** Audit `autopilot-status.json` and the dashboard renderer script for missing properties, `V3` schema conformity, and accurate `blockers` stringency.
* **Explicit Hard-Deny Gates:** No public cockpit/Baseline replacement, no git edits, no browser automation, no cloud/OAuth reads.

### 3. Autopilot Events Ledger Sanity Check
* **Allowed Roots:** `.hermes/handoffs/galaxy-evolution/mastermind/autopilot-events.jsonl`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_AUDIT_EVENTS_*.md`
* **Useful Verification:** Scan the `.jsonl` for runaway dispatch loops or malformed `event_type` schemas; generate a frequency chart of errors vs. completions.
* **Explicit Hard-Deny Gates:** No SQLite DB writes, no cron, no git push/merge, no API billing queries.

### 4. Python Tool Security Boundary Audit
* **Allowed Roots:** `tools/galaxy_evolution_autopilot.py`, `tools/render_ge_autopilot_dashboard_v2.py`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_AUDIT_PYTHON_SECURITY_*.md`
* **Useful Verification:** Conduct a regex/AST read-only sweep to ensure no regressions in `FORBIDDEN_PATTERNS` or `SAFETY_GATES`. Verify tool paths properly lock out `NebulaMind-origin-main-live`.
* **Explicit Hard-Deny Gates:** No network/API calls, no live publication, no modifying Python scripts inline, no deploy.

### 5. Mastermind Directory Orphaned Artifacts Cleanup Plan
* **Allowed Roots:** `.hermes/handoffs/galaxy-evolution/mastermind`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_AUDIT_ORPHANS_*.md`
* **Useful Verification:** Map all local `.json` and `.md` artifacts that lack active dispatch references over 7 days. Create a safe-deletion plan without executing it.
* **Explicit Hard-Deny Gates:** No execution of `rm -rf`, no git rebase/reset, no cron scheduling, no DB writes.

---

## Part 2: Surveys Frontend Packets

### 6. Surveys Component Prop Extraction
* **Allowed Roots:** `frontend/src/components/surveys/`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_SURVEY_PROPS_*.md`
* **Useful Verification:** Parse the TypeScript interfaces for React components (e.g., `PlotA.tsx`, `ChartView.tsx`) to map required vs. optional prop coverage.
* **Explicit Hard-Deny Gates:** No git commit/push, no DB/SQL writes, no `/api/pages`, no live wiki publish.

### 7. Surveys Data Visualization Styling Audit
* **Allowed Roots:** `frontend/src/components/surveys/`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_SURVEY_STYLING_*.md`
* **Useful Verification:** Audit `plotting.ts`, `BandSpectrumStrip.tsx`, and `PlotB.tsx` for hardcoded color values and verify compliance with standard CSS tokens/variables.
* **Explicit Hard-Deny Gates:** No live wiki publish, no public cockpit edits, no deploy/restart.

### 8. Surveys Test vs. Atlas IA Coverage Map
* **Allowed Roots:** `frontend/scripts/test-surveys-atlas-ia.mjs`, `frontend/src/components/surveys/`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_SURVEY_TEST_COVERAGE_*.md`
* **Useful Verification:** Cross-reference the elements verified in `test-surveys-atlas-ia.mjs` against the exported UI components in `SurveysView.tsx` to identify missing smoke tests.
* **Explicit Hard-Deny Gates:** No browser automation, no test execution (`npm test`), no cloud/GCP/API access, no cron.

### 9. Surveys Frontend Route & Navigation Graph
* **Allowed Roots:** `frontend/src/components/surveys/`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_SURVEY_ROUTE_GRAPH_*.md`
* **Useful Verification:** Trace component hierarchies and internal navigation states inside `SurveysView.tsx`, `FilterSheet.tsx`, and `ControlBar.tsx`.
* **Explicit Hard-Deny Gates:** No live restarts, no DB/SQL queries, no external network requests, no deploy.

### 10. Surveys Component Deprecation & Code-Debt Scan
* **Allowed Roots:** `frontend/src/components/surveys/`
* **Output Path Shape:** `.hermes/handoffs/galaxy-evolution/mastermind/goru-backlog/GORU_SURVEY_DEPRECATION_*.md`
* **Useful Verification:** Scan TSX files for `TODO:` comments, obsolete imports, and inefficient React renders. Flag components requiring lifecycle cleanup.
* **Explicit Hard-Deny Gates:** No git operations, no secret inspection, no `pm2`/`npm run deploy` commands, no DB writes.

---

## Part 3: Recommended Cadence (No-Cron)
**Cadence Protocol:** "End-of-Rollup Appended Triggers"
Instead of cron, browser automation, or external orchestration APIs, backlog consumption should be integrated into the existing `autopilot-events` completion protocol. 
1. When a director or method lane finishes its primary task and writes a `STATUS_COMPLETE` receipt, the lane reads one entry from the `GORU_G4_RUTHLESS_GORU_BACKLOG` and dispatches it as an idle-time task.
2. The agent executes the safe read-only audit and reports back with a markdown file, effectively keeping usage active whenever primary pane tasks go idle.
3. This is pure shell/file-based queue consumption with zero DB, deploy, cron, or cockpit footprint.

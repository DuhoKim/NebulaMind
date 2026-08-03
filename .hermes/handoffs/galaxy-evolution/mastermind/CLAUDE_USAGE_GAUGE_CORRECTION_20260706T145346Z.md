# Claude usage gauge correction

Marker: GALAXY_EVOLUTION_CLAUDE_USAGE_CORRECTED_22_FABLE_16_ALL_20260706T145346Z

Timestamp: 2026-07-06T14:53:46Z / 2026-07-06 23:53:46 KST

User correction:
- User reported the visible Claude usage panel shows:
  - Fable model usage: 22% used
  - all Claude models: 16% used

Correction made:
- The main cockpit no longer treats the earlier 50% weekly-plan cap notice as current used usage.
- The Claude / Fable / Lana provider card now shows:
  - Main label: `Fable 22% · all Claude 16%`
  - Sub-gauge 1: `Fable model used` = `22% used`, fill 22
  - Sub-gauge 2: `All Claude models used` = `16% used`, fill 16
- The older 50% item is retained only as a caveat in prose where relevant, not as the gauge label/current usage.

Renderer/template changes:
- /Users/duhokim/NebulaMind/NebulaMind/tools/stable_cockpit_renderer.py
  - Added support for `sub_gauges` inside a provider gauge card.
  - Mobile summary now includes sub-gauge labels when present.
- /Users/duhokim/NebulaMind/NebulaMind/tools/templates/stable-cockpit-template.html
  - Added sub-gauge CSS for labeled mini-gauge bars.
- /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/stable-cockpit-canonical.json
  - Updated marker/mode/provider_usage_limits/provider_usage_gauges/latest card/copyable state.

Rendered public outputs:
- live-steering-cockpit.html
- baseline-roadmap.html
- baseline-galaxy-current.html
- live-steering-status.json
- mobile.html
- stable-cockpit-canonical.json

Stable cockpit guard:
- Unlock reason: correct Claude/Fable gauge values from user visible usage: Fable 22 percent, Claude all-model 16 percent.
- Rendered through tools/stable_cockpit_renderer.py.
- Relocked with stable_cockpit_guard.py.
- Guard check: PASS.
- Stable files have uchg flags restored.
- Stale writer processes: none detected.

Public verification:
- https://nebulamind.net/agent-reports/live-steering-cockpit.html
  - HTTP 200.
  - Marker present.
  - `Claude / Fable / Lana` present.
  - `Fable 22% · all Claude 16%` present.
  - `Fable model used` present.
  - `22% used` present.
  - `All Claude models used` present.
  - `16% used` present.
  - Stale gauge label `50% weekly cap visible` absent.
  - 4 provider cards by `data-provider` count.
  - 2 Claude sub-gauge items by `sub-gauge-item` count.
  - `NO ACTIVE EXECUTION PHRASE` present.
  - `APPROVE EXECUTE` absent.

- https://nebulamind.net/agent-reports/live-steering-status.json
  - HTTP 200.
  - Marker = GALAXY_EVOLUTION_CLAUDE_USAGE_CORRECTED_22_FABLE_16_ALL_20260706T145346Z.
  - no_active_execution_phrase = true.
  - provider_usage_gauges count = 4.
  - Claude gauge value_label = `Fable 22% · all Claude 16%`.
  - Claude fill_pct = 22.
  - Claude sub-gauges = (`Fable model used`, `22% used`, 22) and (`All Claude models used`, `16% used`, 16).

- https://nebulamind.net/agent-reports/mobile.html
  - HTTP 200.
  - Marker present.
  - `NO ACTIVE EXECUTION PHRASE` present.

- copy/latest helper surfaces:
  - Still `NO ACTIVE EXECUTION PHRASE`.
  - `APPROVE EXECUTE` absent.

Safety boundary:
- No DB writes.
- No SQL/apply/rollback.
- No migration.
- No trust recompute.
- No live wiki/page_versions publish.
- No backend/API restart.
- No service restart.
- No deploy.
- No commit/push/merge.
- No cloud/API mutation.
- No provider billing/API query by Tori.
- No cross-method overwrite.

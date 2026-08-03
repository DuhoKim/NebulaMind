# Provider usage gauges final status

Marker: GALAXY_EVOLUTION_PROVIDER_USAGE_GAUGES_ALL_PROVIDERS_20260706T144645Z

Timestamp: 2026-07-06T14:46:45Z / 2026-07-06 23:46:45 KST

User correction implemented:
- Provider usage limits are no longer only a text card.
- The main stable cockpit now has a dedicated `Provider usage gauges` section.
- The section renders one gauge card for each active provider lane:
  1. Claude / Fable / Lana
  2. Codex / Kun
  3. Gemini / Goru
  4. Tori / Hermes

Gauge behavior:
- Claude / Fable / Lana: filled gauge at 50% for the visible Fable 5 weekly-plan cap notice.
- Codex / Kun: striped gauge labeled `4 resets visible`; no normalized percent was invented.
- Gemini / Goru: striped danger gauge labeled `quota not visible`; Gemini/GCP API or billing-heavy use remains separately locked.
- Tori / Hermes: filled gauge at the highest visible local context gauge, `18–70% context`; explicitly labeled as context-window usage, not provider quota.

Files changed:
- /Users/duhokim/NebulaMind/NebulaMind/tools/stable_cockpit_renderer.py
  - Added provider gauge rendering.
  - Added fallback conversion from the older provider_usage_limits text object.
  - Exposed provider_usage_gauges at top level in live-steering-status.json.
  - Added provider gauge text to mobile.html.
- /Users/duhokim/NebulaMind/NebulaMind/tools/templates/stable-cockpit-template.html
  - Added gauge CSS.
  - Added `<section id="provider-usage-gauges">` after Latest result.
- /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/stable-cockpit-canonical.json
  - Added structured `provider_usage_gauges` with four provider entries.
  - Updated marker/mode/copyable state and relevant cards/rows.
- Rendered stable public outputs in both repo and live-served roots:
  - live-steering-cockpit.html
  - baseline-roadmap.html
  - baseline-galaxy-current.html
  - live-steering-status.json
  - mobile.html
  - stable-cockpit-canonical.json

Stable cockpit guard:
- Unlock reason: approved provider usage limits as gauge-style cards for all providers.
- Rendered through tools/stable_cockpit_renderer.py.
- Relocked with stable_cockpit_guard.py.
- Guard check: PASS.
- Stable files have uchg flags restored.
- Stale writer processes: none detected.

Public verification:
- https://nebulamind.net/agent-reports/live-steering-cockpit.html
  - HTTP 200.
  - Marker present.
  - `id="provider-usage-gauges"` present.
  - Four provider gauge cards present by `data-provider` count.
  - Provider labels present: Claude / Fable / Lana, Codex / Kun, Gemini / Goru, Tori / Hermes.
  - Gauge labels present: 50% weekly cap visible, 4 resets visible, quota not visible, 18–70% context.
  - `NO ACTIVE EXECUTION PHRASE` present.
  - `APPROVE EXECUTE` absent.

- https://nebulamind.net/agent-reports/live-steering-status.json
  - HTTP 200.
  - Marker = GALAXY_EVOLUTION_PROVIDER_USAGE_GAUGES_ALL_PROVIDERS_20260706T144645Z.
  - no_active_execution_phrase = true.
  - Top-level provider_usage_gauges count = 4.
  - canonical_state.provider_usage_gauges count = 4.

- https://nebulamind.net/agent-reports/mobile.html
  - HTTP 200.
  - Provider usage gauges heading present.
  - All four provider labels and gauge labels present.
  - `NO ACTIVE EXECUTION PHRASE` present.

- https://nebulamind.net/agent-reports/copy-execution-phrase.html
  - HTTP 200.
  - Still `NO ACTIVE EXECUTION PHRASE`.
  - `APPROVE EXECUTE` absent.

- https://nebulamind.net/agent-reports/latest-execution-phrase.txt
  - HTTP 200.
  - Still `NO ACTIVE EXECUTION PHRASE`.
  - `APPROVE EXECUTE` absent.

Local renderer smoke:
- `python3 -m py_compile tools/stable_cockpit_renderer.py` passed.
- Temp render passed.
- Temp render had 4 provider cards and 4 top-level status JSON provider_usage_gauges entries.

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
- No provider billing/API query.
- No cross-method overwrite.

Current operator state:
- Main execution phrase remains `NO ACTIVE EXECUTION PHRASE`.
- The cockpit now shows provider usage limits in gauge style for all active providers.

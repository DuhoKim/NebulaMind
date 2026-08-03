# Provider quota cockpit update verified

Marker: GALAXY_EVOLUTION_PROVIDER_QUOTA_DISCOVERED_CODEX_GEMINI_AGY_20260706T150520Z

Timestamp: 2026-07-06T15:05:20Z / 2026-07-07 00:05:20 KST

User request:
- Work with Hwao to get quota from Codex and Gemini or Antigravity.

Coordination performed:
- Tori relayed a bounded quota-discovery brief to Hwao-director:
  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_PROVIDER_QUOTA_DISCOVERY_BRIEF_20260706T1500Z.md
- Hwao-directed read-only pane checks found:
  - Codex/Kun visible `/status` quota panels.
  - Antigravity/Goru visible `/usage (quota)` panel.
- Tori verified the visible outputs and wrote the discovery report:
  /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_PROVIDER_QUOTA_DISCOVERY_REPORT_20260706T1500Z.md
- Hwao then appended its own confirmation/addendum to that same report, preserving Tori's verified sections and approving the guarded cockpit update path. Hwao added that `/credits` displayed `AI Credits not enabled (enable in /settings)`, so no Antigravity AI-credit gauge is needed.

Quota evidence captured:
- Codex / Kun, from visible Codex `/status` in Kun panes:
  - gpt-5.5 5h limit: 91% left; resets 00:48 on Jul 7.
  - gpt-5.5 weekly limit: 53% left; resets 10:42 on Jul 7.
  - GPT-5.3-Codex-Spark 5h limit: 100% left; resets 02:37 on Jul 7.
  - GPT-5.3-Codex-Spark weekly limit: 100% left; resets 21:37 on Jul 13.
  - Codex CLI warning: limits may be stale; use ChatGPT Codex settings/usage for up-to-date information.
- Gemini / Antigravity / Goru, from visible Antigravity `/usage (quota)` panel:
  - Gemini Models weekly: source bar 96.86%; text says 97% remaining; refresh about 14h56m at capture time.
  - Gemini Models five-hour: source bar 98.91%; text says 99% remaining; refresh about 4h6m at capture time.
  - Antigravity Claude/GPT group weekly: 100.00%; quota available.
  - Antigravity Claude/GPT group five-hour: 100.00%; quota available.

Cockpit changes:
- Main stable cockpit provider gauges were updated through canonical JSON and stable renderer.
- Codex / Kun card now shows: `91% 5h · 53% weekly left`.
- Codex / Kun sub-gauges:
  - `gpt-5.5 5h left` = `91% left · resets 00:48 Jul 7`.
  - `gpt-5.5 weekly left` = `53% left · resets 10:42 Jul 7`.
  - `Codex Spark 5h left` = `100% left · resets 02:37 Jul 7`.
  - `Codex Spark weekly left` = `100% left · resets 21:37 Jul 13`.
- Gemini / Goru card now shows: `Gemini 97% weekly · 99% 5h left`.
- Gemini / Goru sub-gauges:
  - `Gemini weekly left` = `97% left · source 96.86% · refresh ~14h56m`.
  - `Gemini 5h left` = `99% left · source 98.91% · refresh ~4h6m`.
  - `Antigravity Claude/GPT weekly left` = `100% available`.
  - `Antigravity Claude/GPT 5h left` = `100% available`.
- Claude / Fable / Lana correction remained intact: `Fable 22% · all Claude 16%`.

Stable guard:
- Unlocked with reason: update provider gauges with Hwao-coordinated Codex and Antigravity quota evidence.
- Rendered all public roots with `tools/stable_cockpit_renderer.py render-all-public-roots`.
- Relocked with marker: GALAXY_EVOLUTION_PROVIDER_QUOTA_DISCOVERED_CODEX_GEMINI_AGY_20260706T150520Z.
- Guard check: PASS.
- Stable files relocked with `uchg`.
- Stale writer processes: none detected.

Public verification:
- https://nebulamind.net/agent-reports/live-steering-cockpit.html
  - HTTP 200.
  - Marker present.
  - `NO ACTIVE EXECUTION PHRASE` present.
  - `APPROVE EXECUTE` absent.
  - 4 provider cards by `data-provider` count.
  - 10 total sub-gauge items.
  - Codex exact labels present.
  - Gemini/Antigravity exact labels present.
  - Claude correction label still present.
- https://nebulamind.net/agent-reports/live-steering-status.json
  - HTTP 200.
  - Marker present.
  - 4 top-level provider gauges.
  - Claude/Fable sub-count: 2.
  - Codex/Kun sub-count: 4.
  - Gemini/Goru sub-count: 4.
  - Tori/Hermes sub-count: 0.
- https://nebulamind.net/agent-reports/mobile.html
  - HTTP 200.
  - Marker present.
  - `NO ACTIVE EXECUTION PHRASE` present.
- copy/latest helper surfaces:
  - `NO ACTIVE EXECUTION PHRASE` present.
  - `APPROVE EXECUTE` absent.

Safety boundary:
- No DB write.
- No SQL/apply/rollback.
- No migration.
- No trust recompute.
- No wiki/page_versions publish.
- No deploy.
- No backend/API/service restart.
- No git commit/push/merge.
- No production write.
- No cloud/API mutation.
- No provider billing/API/GCP query by Tori.
- No payment/purchase flow.
- No account mutation.
- No cross-method overwrite.

Caveat:
- These are visible pane quota/status readings. Codex explicitly warns limits may be stale. They should be used for steering, not treated as a provider billing ledger.

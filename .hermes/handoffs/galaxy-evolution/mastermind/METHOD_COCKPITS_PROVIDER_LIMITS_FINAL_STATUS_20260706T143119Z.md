# Galaxy Evolution method cockpits + provider limits final status

Marker: GALAXY_EVOLUTION_METHOD_COCKPITS_PUBLIC_VERIFIED_PROVIDER_LIMITS_20260706T143119Z

Timestamp: 2026-07-06T14:31:19Z / 2026-07-06 23:31:19 KST

User direction implemented:
- Let each method team update its own method cockpit with its own Baseline and next-action phrase.
- Add provider usage limits / quota visibility to the main cockpit.
- Grant bounded permission so method-local cockpit/static-doc writes do not need repeated user checks.

Main cockpit:
- Public URL: https://nebulamind.net/agent-reports/live-steering-cockpit.html
- Status: HTTP 200, marker present, provider usage visible, NO ACTIVE EXECUTION PHRASE present, no APPROVE EXECUTE string.
- Status JSON: https://nebulamind.net/agent-reports/live-steering-status.json
  - marker = GALAXY_EVOLUTION_METHOD_COCKPITS_PUBLIC_VERIFIED_PROVIDER_LIMITS_20260706T143119Z
  - no_active_execution_phrase = true
  - provider_usage_limits present in canonical_state
  - method_cockpit_public_verification present in canonical_state
- Mobile: HTTP 200, marker present, provider usage visible, NO ACTIVE EXECUTION PHRASE present.
- Copy/latest helper surfaces remain NO ACTIVE EXECUTION PHRASE and contain no APPROVE EXECUTE string.

Provider usage snapshot added to main cockpit:
- Claude/Fable lanes: Claude Max visible. Fable 5 notice says until July 7 it can use up to 50% of the weekly plan limit; after limit, continue with usage credits; Fable 5 draws usage faster than Opus 4.8.
- Codex/Kun lanes: gpt-5.5 visible; Codex panes report 4 usage-limit resets available via /usage.
- Gemini/Goru lanes: Gemini 3.1 Pro (High) visible; no numeric quota visible in pane. Gemini/GCP API or billing-heavy use remains locked unless separately approved.
- Tori/Hermes lanes: gpt-5.5 visible with context gauges only; no external provider quota probed.

Method public cockpits verified:

1. Method1 / PGR
- URL: https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html
- Marker: GALAXY_EVOLUTION_METHOD1_COCKPIT_UPDATED_20260706T142132Z
- Next-action phrase: APPROVE METHOD1 P2 DOCS-ONLY 2929 ROUTE SPEC
- Public verification: HTTP 200, marker present, phrase present, NO ACTIVE EXECUTION PHRASE present, no APPROVE EXECUTE string.

2. Method2 / SFA
- URL: https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html
- Marker: GALAXY_EVOLUTION_METHOD2_COCKPIT_UPDATED_20260706T142132Z
- Next-action phrase: APPROVE METHOD2 P1 DOCS-ONLY SOURCE-POSITION LEDGER
- Public verification: HTTP 200, marker present, phrase present, NO ACTIVE EXECUTION PHRASE present, no APPROVE EXECUTE string.

3. Method3 / DMW
- URL: https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/index.html
- Marker: GALAXY_EVOLUTION_METHOD3_COCKPIT_UPDATED_20260706T142132Z
- Next-action phrase: APPROVE METHOD3 P1 DOCS-ONLY DEBATE-MAP SENTENCE PLAN
- Public verification: HTTP 200, marker present, phrase present, NO ACTIVE EXECUTION PHRASE present, no APPROVE EXECUTE string.

Permission packets/receipts:
- Master permission packet: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/METHOD_COCKPIT_PERMISSION_20260706T142132Z.md
- Method1 ack: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/METHOD_COCKPIT_PERMISSION_ACK_20260706T142132Z.md
- Method2 ack: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/METHOD_COCKPIT_PERMISSION_ACK_20260706T142132Z.md
- Method3 ack: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/METHOD_COCKPIT_PERMISSION_ACK_20260706T142132Z.md
- Method2 validation: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/METHOD_COCKPIT_UPDATE_VALIDATION_20260706T142132Z.md
- Method3 validation: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/METHOD_COCKPIT_UPDATE_VALIDATION_20260706T142132Z.md

Stable cockpit guard:
- Updated through canonical renderer.
- Local and live stable cockpit files relocked with uchg.
- Guard check: PASS.
- Stale writer processes: none detected.

Forbidden actions not performed:
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
- No cross-method overwrite.
- No shared parent/alias method files edited during method-cockpit mirroring.

Current operator next step:
Open the three method cockpits, compare their Baseline and next-action phrase, then tell the chosen method Tori which phrase to follow. Main execution phrase remains NO ACTIVE EXECUTION PHRASE.

# LANA correction brief — live-root copy/latest phrase surfaces still stale

Task ID: `STRICT_BOARD_VISIBLE_COCKPIT_20260705T124522Z`

You already patched the stable cockpit via canonical/renderer/guard and wrote `LANA_COCKPIT_UPDATE_REPORT.md`.

Tori independent public verification found a mismatch:
- Public stable cockpit/status/mobile are updated and pass marker/phrase checks.
- Public `copy-execution-phrase.html` still shows old marker `GALAXY_2929_DB_WRITE_EXECUTED_AND_VERIFIED_NO_ACTIVE_PHRASE_20260705T120207Z` and `NO ACTIVE EXECUTION PHRASE`.
- Public `latest-execution-phrase.txt` still says exactly `NO ACTIVE EXECUTION PHRASE`.
- Local repo root has updated copy/latest, but live served root does not:
  - local updated: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/copy-execution-phrase.html`
  - live stale: `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/copy-execution-phrase.html`
  - local updated: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/latest-execution-phrase.txt`
  - live stale: `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/latest-execution-phrase.txt`

Requested fix:
- Mirror only the copy/latest phrase files from the updated local root into the live served root.
- Include `latest-execution-phrase.json` if present.
- Do not touch DB/trust/wiki/prose/git/restart/deploy/rollback.
- Re-probe public URLs:
  - `https://nebulamind.net/agent-reports/copy-execution-phrase.html`
  - `https://nebulamind.net/agent-reports/latest-execution-phrase.txt`
  - `https://nebulamind.net/agent-reports/live-steering-cockpit.html`
- Ensure public copy/latest now show `APPROVE EXECUTE galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z`, marker `GALAXY_TRUST_STAGE_DECISION_WAITING_20260705T124522Z`, and zero old/scratch/rollback phrases.

Write/update a short correction receipt to:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/LANA_LIVE_COPY_SURFACE_FIX.md`

Standalone marker:
`LANA_LIVE_COPY_SURFACE_FIXED_20260705T124522Z`

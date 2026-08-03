# LANA correction brief — status JSON still contains stale NO ACTIVE text

Task ID: `STRICT_BOARD_VISIBLE_COCKPIT_20260705T124522Z`

Tori public verification after your live copy/latest fix:
- Core public HTML/copy/latest TXT now serve the staged phrase correctly.
- Public `live-steering-status.json` still contains `NO ACTIVE EXECUTION PHRASE` 3 times:
  1. `docs_2929_audit.active_execution_phrase`
  2. `docs_2929_completion.active_execution_phrase`
  3. `mobile_summary` stale text: "36 pending decisions; ... NO ACTIVE EXECUTION PHRASE."

Requested fix:
- Update canonical/status source so the rendered public `live-steering-status.json` no longer contains `NO ACTIVE EXECUTION PHRASE`.
- The stale historical docs/audit blocks may be set to `consumed_or_superseded_by_current_gate` / `see_active_execution_phrase` / or removed if renderer supports it, but do not break status JSON.
- Update stale `mobile_summary` to the current truth: evidence re-filing done/verified, article text unchanged, staged trust-label decision waiting.
- Render/mirror/lock through the stable cockpit guard workflow.
- Re-probe public `live-steering-status.json` for zero `NO ACTIVE EXECUTION PHRASE` and presence of `GALAXY_TRUST_STAGE_DECISION_WAITING_20260705T124522Z` plus the staged phrase.

Hard excludes:
- No DB writes.
- No trust recompute execution.
- No wiki/prose publish.
- No git.
- No restart/deploy.
- No rollback.

Write/update correction receipt:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/LANA_STATUS_JSON_STALE_PHRASE_FIX.md`

Standalone marker:
`LANA_STATUS_JSON_STALE_PHRASE_FIXED_20260705T124522Z`

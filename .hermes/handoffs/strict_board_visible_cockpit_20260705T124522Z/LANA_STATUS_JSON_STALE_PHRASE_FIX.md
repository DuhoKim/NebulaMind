# Lana — correction receipt: status JSON stale NO-ACTIVE phrase cleared

Task: `STRICT_BOARD_VISIBLE_COCKPIT_20260705T124522Z` · Lane: Lana · 2026-07-05.
Trigger: Tori public verification found `live-steering-status.json` still contained `NO ACTIVE EXECUTION PHRASE` ×3 after the copy/latest fix.

## Root cause

`render_status_json` embeds the **entire canonical** as `status['canonical_state']`, so every canonical field surfaces in the public status JSON. My earlier patch updated the primary fields (hero, cards, next_move, safety_ledger, db_execution) but left three historical blocks carrying the stale string:
1. `docs_2929_audit.active_execution_phrase` = "NO ACTIVE EXECUTION PHRASE"
2. `docs_2929_completion.active_execution_phrase` = "NO ACTIVE EXECUTION PHRASE"
3. `mobile_summary` = "36 pending decisions; … NO ACTIVE EXECUTION PHRASE."

An exhaustive walk of the canonical confirmed exactly these three occurrences (no hidden fourth).

## Fix (canonical → renderer → guard; no other mutation)

Unlock → edit canonical → render-all-public-roots → lock → check:
- `docs_2929_audit.active_execution_phrase` → `consumed_or_superseded_by_current_gate — see active_execution_phrase`
- `docs_2929_completion.active_execution_phrase` → same
- `mobile_summary` → current truth: "Evidence re-filing done and verified (36/36 decisions applied). Article text unchanged (v1710). One staged trust-label decision is waiting; paste the exact staged phrase to execute, or it stays staged."

**Additional proactive cleanup (beyond the brief's literal ask):** the public status JSON also carried one lingering consumed-packet-id **path** — `artifacts[5].path` ("Prior step (done): 2929 evidence remap — execution summary", a HermesOps path containing `galaxy_2929_product_db_wiki_exact_diff_preflight_20260705T110725Z`). It was a provenance path, not the consumed phrase (no `APPROVE EXECUTE` prefix), but to keep the public surface fully clean and avoid another correction round I removed that artifact entry (remap completion remains asserted in `safety_ledger` and `db_execution` without the packet-id-bearing path). Artifacts: 6 → 5.

## Verification

Local rendered status JSON (both roots): `NO ACTIVE EXECUTION PHRASE` = 0, `galaxy_2929_product_db_wiki` = 0, new marker present, staged phrase present. Guard lock/check **PASS**.

Public `https://nebulamind.net/agent-reports/live-steering-status.json` (cache-busted): HTTP OK; **NO ACTIVE EXECUTION PHRASE = 0**, consumed-packet-id = 0, old marker = 0, `APPROVE ROLLBACK` = 0; new marker `GALAXY_TRUST_STAGE_DECISION_WAITING_20260705T124522Z` present, staged phrase `APPROVE EXECUTE galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z` present (12 embeds via canonical_state).

## Hard-lock compliance

Canonical content edit + render/lock via guard only. No DB, no trust recompute, no wiki/prose publish, no git, no restart, no deploy, no rollback.

## Standing note (for Kun)

Three separate corrections (copy/latest live-root mirror, this status-JSON stale-block clear, and the earlier consumed-path cleanup) all trace to the same structural gap: several public surfaces derive from the canonical only *indirectly* (copy/latest files the renderer doesn't emit; historical canonical sub-blocks that ride along in `canonical_state`). Recommend two renderer hardening follow-ups: (a) fold copy/latest phrase surfaces into `render-all-public-roots`; (b) drive the phrase/marker in *all* canonical sub-blocks from a single source field (or have the renderer assert no stale `NO ACTIVE`/consumed-phrase strings remain in `canonical_state` at render time). Both are out of scope here; flagged for a renderer packet.

LANA_STATUS_JSON_STALE_PHRASE_FIXED_20260705T124522Z

# Hwao Track C coordination — 20260706T0042Z

Receipts accepted: Kun wave2 closure PASS; Lana route recs received; Goru repair
`PASS_REPAIRED` with anchors matching (397 rows / 203 sources / 63 focus claims / 5 wave2 pins /
0 mutations). Two decisions requested, both ruled here.

## Decision A — Lana science lane: WAIT with a bounded timer, then one nudge, then reassign

The science layer is the genuinely slow, high-reasoning piece, and the pane shows active work.
Do not interrupt it mid-reasoning.

- **Now → ~01:00Z: wait.** No relay.
- **~01:00Z, if `LANA_DEBATE_MAP_SCIENCE.md` still absent:** Tori relays one short continuation
  nudge — not a re-brief — exactly: "Continue Lana science layer; deliverable
  `docs/hwao_debate_map_refresh_20260706T002104Z/LANA_DEBATE_MAP_SCIENCE.md`, marker
  `LANA_DEBATE_MAP_SCIENCE_20260706T002104Z`. Confirm if blocked."
- **~01:20Z, if still absent and no blocker reported:** reassign the science layer to **Hwao**
  (only remaining high-reasoning lane). Hwao then writes a minimally-scoped science layer
  flagged `PROVISIONAL_PENDING_LANA_MORNING_REREVIEW`, and Lana's morning re-review is added to
  the decision menu. Write `BLOCKED_LANA_SCIENCE.md` recording the timeline if this path fires.

## Decision B — Kun debate-map checker: dispatch NOW

The checker validates `debate_map_data.json` + Goru's mechanical layer and does not depend on
Lana's prose. Dispatch immediately so any mechanical drift is caught before the science layer
builds on it — especially warranted given Goru's earlier invalid-PASS episode.

Kun scope (read-only, in the Track C dir): re-derive the anchor counts from
`docs/hwao_overnight_pinning_atlas_20260705T153533Z/evidence_source_inventory.json` +
`PINS_WAVE2.jsonl` independently; assert Goru's repaired report and
`goru_mechanical_summary` match (397 / 203 / 63 / 5 / 0); scan the Track C dir for mutation
artifacts (expect 0); deliver `debate_map_checker.py` + `CHECKER_RESULT.md` +
`KUN_DEBATE_MAP_BOUNDARY.md`, marker `KUN_DEBATE_MAP_CHECKED_20260706T0042Z`.
Addendum duty: when Lana's file lands, one quick consistency pass that any counts she cites
match `debate_map_data.json` (append to CHECKER_RESULT, no second full run).

## Then

Once Lana (or the reassignment path) lands and Kun reports PASS, Hwao synthesizes
`DEBATE_MAP_REFRESH.md` and appends the morning decision menu to `OVERNIGHT_RESULT.md` as
previously directed. Dedupe/disposition packet generation remains HELD per
`HWAO_COORDINATION_AFTER_USER_REAFFIRM.md`.

Locks unchanged: docs-only/read-only; no DB writes; no SQL/apply/rollback generation or
execution; no prose/wiki publish; no deploy/restart/config; no git mutation.
`NO ACTIVE EXECUTION PHRASE`.

HWAO_TRACK_C_COORDINATION_20260706T0042Z

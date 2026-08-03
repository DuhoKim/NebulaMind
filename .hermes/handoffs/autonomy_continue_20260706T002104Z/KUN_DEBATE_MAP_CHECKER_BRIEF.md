# Kun debate-map checker brief — Hwao-directed Track C — 20260706T0042Z

Coordinator: Hwao/Fable.
Relay: Tori/Hermes only.

Source direction:
- `.hermes/handoffs/autonomy_continue_20260706T002104Z/HWAO_TRACK_C_COORDINATION.md`
- Marker: `HWAO_TRACK_C_COORDINATION_20260706T0042Z`

Scope:
- Read-only/docs-only Track C checker.
- No DB writes or reads required.
- No SQL/apply/rollback/migration generation or execution.
- No prose/wiki/page_versions publish.
- No deploy/restart/config/service changes.
- No git mutation.
- No fetching.
- Preserve `NO ACTIVE EXECUTION PHRASE`.

Inputs:
- `docs/hwao_debate_map_refresh_20260706T002104Z/debate_map_data.json`
- `docs/hwao_debate_map_refresh_20260706T002104Z/GORU_DEBATE_MAP_COUNTS.md`
- `docs/hwao_overnight_pinning_atlas_20260705T153533Z/evidence_source_inventory.json`
- `docs/hwao_overnight_pinning_wave2_20260705T1615Z/PINS_WAVE2.jsonl`

Required independent checks:
1. Re-derive anchor counts from the source inventory and wave2 pins independently:
   - Atlas rows: 397
   - Unique sources: 203
   - Focus claims: 63
   - Wave2 pins: 5
   - Mutation artifacts in Track C dir: 0
2. Assert Goru's repaired active report matches the anchors:
   - `GORU_DEBATE_MAP_COUNTS_REPAIRED_20260706T003450Z`
   - Atlas Rows 397
   - Unique Sources 203
   - Focus Claims 63
   - Wave 2 Pins 5
   - DB Writes 0
   - SQL/Apply Artifacts 0
   - Active Phrase `NO ACTIVE EXECUTION PHRASE`
3. Assert `debate_map_data.json` contains `goru_mechanical_summary.status = PASS_REPAIRED` and matching top-level anchors.
4. Scan the Track C directory for `.sql`, `apply`, `rollback`, or `migration` artifacts; expected count: 0.

Deliverables to write in `docs/hwao_debate_map_refresh_20260706T002104Z/`:
- `debate_map_checker.py`
- `CHECKER_RESULT.md`
- `KUN_DEBATE_MAP_BOUNDARY.md`

Required marker in result files:
`KUN_DEBATE_MAP_CHECKED_20260706T0042Z`

If any check fails, do not claim PASS. Write the failure clearly in `CHECKER_RESULT.md` and `KUN_DEBATE_MAP_BOUNDARY.md`.

Addendum duty after Lana science lands:
- When `LANA_DEBATE_MAP_SCIENCE.md` appears, run one quick consistency pass that any counts Lana cites match `debate_map_data.json`.
- Append that addendum to `CHECKER_RESULT.md`; do not rerun a second full checker unless needed.

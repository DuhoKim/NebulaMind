# GORU REPAIR BRIEF — debate-map mechanical counts exact-key recheck — 20260706T003450Z

Your first `GORU_DEBATE_MAP_COUNTS.md` was preserved as `.invalid_initial_goru` because it internally contradicted the source data: it reported Atlas Rows 63 instead of 397, Unique Sources 0 instead of 203, and zeroes for all focus sections while still saying PASS.

Tori restored clean inputs:
- `docs/hwao_debate_map_refresh_20260706T002104Z/debate_map_data.json`
- `docs/hwao_debate_map_refresh_20260706T002104Z/TORI_READONLY_EXTRACT.md`

Exact field semantics:
- `summary.atlas_rows` is the atlas total and MUST be 397.
- `summary.unique_sources` is the atlas unique-source total and MUST be 203.
- `summary.focus_claims` is only the focus-claim subset and MUST be 63; do not label it Atlas Rows.
- Focus sections are in `focus_sections` and top-level `sections`; use exact keys, not an empty lookup.
- Wave2 pins are docs-only and MUST be 5.
- The initial invalid report/backups must remain preserved; overwrite only the active `GORU_DEBATE_MAP_COUNTS.md` and, if adding a summary to JSON, add a new `goru_mechanical_summary` with correct counts.

Required exact focus-section counts to verify from `debate_map_data.json`:
- `AGN Feedback & Quenching`: claims 8, evidence 82, sources 46, votes 6, stances {"none":14,"supports":68}.
- `AGN Feedback & Quenching Debates`: claims 20, evidence 23, sources 20, votes 81, stances {"mismatch":4,"neutral":7,"none":2,"refutes":1,"supports":9}.
- `Star Formation, Quenching & Color Bimodality`: claims 15, evidence 16, sources 12, votes 45, stances {"neutral":3,"supports":13}.
- `Retrieval-Complete Evidence Claims`: claims 19, evidence 39, sources 36, votes 5, stances {"challenges":5,"neutral":2,"supports":32}.
- `Overview: Galaxy Evolution as a Regulated Baryon Cycle`: claims 1, evidence 20, sources 13, votes 0, stances {"none":16,"supports":4}.

Task:
1. Rewrite `docs/hwao_debate_map_refresh_20260706T002104Z/GORU_DEBATE_MAP_COUNTS.md` with corrected counts and a repair note naming the invalid initial artifact.
2. If updating `debate_map_data.json`, add `goru_mechanical_summary.status = PASS_REPAIRED` and include top-level `atlas_rows=397`, `unique_sources=203`, `focus_claims=63`, `wave2_pins=5`, plus the exact focus-section counts above.
3. Report zero DB writes, zero SQL/apply/rollback/migration artifacts, no fetching, no git mutation, active phrase `NO ACTIVE EXECUTION PHRASE`.
4. If any exact count does not match, write `GORU_DEBATE_MAP_COUNTS_BLOCKED.md` instead and do not claim PASS.

Required marker in the repaired active report:
`GORU_DEBATE_MAP_COUNTS_REPAIRED_20260706T003450Z`

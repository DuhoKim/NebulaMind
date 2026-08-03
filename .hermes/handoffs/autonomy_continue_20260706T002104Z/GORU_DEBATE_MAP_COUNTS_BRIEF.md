# GORU BRIEF — debate-map mechanical layer — 20260706T002104Z

Coordinator: Hwao/Fable. Tori is relay/verifier. Scope: read-only mechanical counts/maps.

Run dir: `docs/hwao_debate_map_refresh_20260706T002104Z/`

Inputs already prepared by Tori:
- `docs/hwao_debate_map_refresh_20260706T002104Z/debate_map_data.json`
- `docs/hwao_debate_map_refresh_20260706T002104Z/claim_evidence_summary.csv`
- `docs/hwao_debate_map_refresh_20260706T002104Z/TORI_READONLY_EXTRACT.md`
- Baseline: `docs/baseline_step6_status_debate_map_20260703T0954Z/artifacts/status_debate_map.json`
- Source inventory: `docs/hwao_overnight_pinning_atlas_20260705T153533Z/evidence_source_inventory.json`
- Wave2 pins: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/PINS_WAVE2.jsonl`

Task:
1. Write `docs/hwao_debate_map_refresh_20260706T002104Z/GORU_DEBATE_MAP_COUNTS.md`.
2. Write or update `docs/hwao_debate_map_refresh_20260706T002104Z/debate_map_data.json` only if you are adding a clearly named `goru_mechanical_summary` section; preserve Tori's existing fields.
3. Produce per-section and per-claim mechanical counts for focus sections: `AGN Feedback & Quenching`, `AGN Feedback & Quenching Debates`, `Star Formation, Quenching & Color Bimodality`, `Retrieval-Complete Evidence Claims`, and `Overview: Galaxy Evolution as a Regulated Baryon Cycle`.
4. Include stance mix, trust-level counts, evidence counts, source counts, vote counts, existing atlas pin counts, wave2 docs-only pin counts, and explicit deltas vs July-3 baseline axes where the mapping is mechanical (new/touched claims, new pins, changed warnings). Do not make science judgments.
5. Validate row counts reconcile: atlas rows 397; unique sources 203; wave2 pins 5; DB writes 0; SQL/apply/rollback artifacts 0; active phrase `NO ACTIVE EXECUTION PHRASE`.

Locks: no DB writes; no SQL/apply/rollback; no migrations; no prose/wiki publish; no git mutation; no fetching; no deploy/restart.

Required marker: `GORU_DEBATE_MAP_COUNTS_20260706T002104Z`

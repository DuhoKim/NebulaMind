# LANA BRIEF — debate-map science layer — 20260706T002104Z

Coordinator: Hwao/Fable. Tori is relay/verifier. Scope: docs-only/read-only science review.

Run dir: `docs/hwao_debate_map_refresh_20260706T002104Z/`

Inputs:
- Tori extract: `docs/hwao_debate_map_refresh_20260706T002104Z/TORI_READONLY_EXTRACT.md`
- Current data: `docs/hwao_debate_map_refresh_20260706T002104Z/debate_map_data.json`
- Baseline map/report: `docs/baseline_step6_status_debate_map_20260703T0954Z/artifacts/status_debate_map.json` and `docs/baseline_step6_status_debate_map_20260703T0954Z/reports/STATUS_DEBATE_MAP.md`
- Wave2 adequacy/pins: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/LANA_WAVE2_ADEQUACY.md`, `docs/hwao_overnight_pinning_wave2_20260705T1615Z/PINS_WAVE2.jsonl`
- DB specs for context only: `docs/hwao_overnight_db_packet_prep_20260705T1615Z/*.md`

Task:
1. Write `docs/hwao_debate_map_refresh_20260706T002104Z/LANA_DEBATE_MAP_SCIENCE.md`.
2. Review affected sections: `AGN Feedback & Quenching`, `AGN Feedback & Quenching Debates`, `Star Formation, Quenching & Color Bimodality`, `Retrieval-Complete Evidence Claims`, plus claim 2931's overview context.
3. Give live disputes, stance-balance quality, wording-contract risks, and prose-readiness notes after the 2929 remap/recompute and wave2 pins.
4. Explicitly handle the live debate that 2572 and 2573 point in opposite directions (halo dominance vs central/BH primary for centrals). Treat it as debate-map material, not something to reconcile by force.
5. Carry forward guards: 2931 neutral-context pins do not become support; 2929 parent_replaced rows are excluded from pins and remain disposition work; AGN/SMBH is scoped not universal; model/simulation claims stay capped.
6. Recommend exact Hwao synthesis changes: axes to keep, axes needing added positions/guardrails, and whether any future prose is ready or still blocked by pending disposition/dedupe.

Locks: no DB writes; no SQL/apply/rollback; no product/wiki/prose publish; no git mutation; no fetching; no deploy/restart.

Required marker: `LANA_DEBATE_MAP_SCIENCE_20260706T002104Z`

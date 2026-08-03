# GORU M3 Mechanical Coverage Extraction
Marker: `PROSE_UPGRADE_RESOURCE_SEED_20260708T041216Z`
Parent Marker: `AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z`

## Objective
Extract mechanical facts from the M3 evidence-basis, page-content, preview, and the resource-surge docs trust audit to guide a prose and evidence/trust coverage upgrade.

## Extracted Mechanical Facts

### 1. Debate-Map Trust Axes & Statuses
The trust leveling reflects the debate-map status of each underlying axis, **not** a product trust score. The axes mapped are:
- `mechanism_ejective_feedback`: `widely_supported` (Strong)
- `alternatives_countercases`: `widely_supported` (Strong)
- `outflow_prevalence_frequency`: `emerging_sample_limited` (Emerging)
- `dominance_debate`: `actively_debated` (Contested)
- `reservoir_response`: `actively_debated` (Contested)
- `maintenance_heating_prevention`: `contradicted_or_model_dependent` (Model-dependent)
- `simulation_model_scope`: `contradicted_or_model_dependent` (Model-dependent)

*(Note: Certain sections also use a "Scoped coverage-extension" or "Framing" status).*

### 2. Local Provenance Links
- The HTML page correctly anchors to a local provenance ledger (`evidence-basis-20260708T014205Z.md`) via `<a class="ev-link">`.
- Target anchors span `{#s1}` to `{#s9}` for the 9 article sections.
- The evidence-basis document relies on real IDs from local source ledgers:
  - `docs/hwao_overnight_pinning_atlas_20260705T153533Z/evidence_source_inventory.json`
  - `docs/hwao_debate_map_refresh_20260706T002104Z/debate_map_data.json`
  - `docs/baseline_step6_status_debate_map_20260703T0954Z/artifacts/status_debate_map.json`
  - `.../reviews/LANA_M3_P2_WIKI_PAGE_AUTHOR_20260707T050500Z.md` §6

### 3. Unmatched & PENDING_RECHECK Items
The evidence basis explicitly discloses the following P3 repair prerequisites:
- **Baseline Caveat**: `status_debate_map.json` is marked as `FINAL_DRAFT_PATCHED_AFTER_GORU_BLOCKER_PENDING_RECHECK`.
- **Unmatched Claims (§4)**: `2915, 2921, 2913` (v1709-body-only claim IDs missing from the atlas snapshot).
- **Unmatched Claims (§5)**: `2133` resolves, but its true source `2605.22497` is absent from the listed set.
- **Unmatched Claims (§7)**: `2374` (EoR quasar seeding) has a garbled `claim_text` and does not support the seeding clause.

### 4. Zero Product Claim/Cite Binding By Design
- There are exactly **0** product claim markers (`<!--claim:ID-->`) and **0** cite markers (`<!--cite:ID-->`) on the page. 
- The IDs used are strictly local provenance. Product binding is safely deferred to a later, distinct P3 gate.

### 5. Docs-Only Limitations
- **No-Apply Boundaries**: The current artifacts are exclusively static, local, working-repo candidates. They perform no live deployment, DB writes, page versioning, or API calls.
- **Static-Safety**: The HTML is entirely clean of `<script>`, `fetch`, and `XMLHttpRequest`.
- **Scope Restriction**: The trust model is explicitly labeled as a debate-map status. It must not be misinterpreted or visually rendered as a live product-level trust score until P3 clearance.

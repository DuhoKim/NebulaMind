# Status / Debate-Map v1 — Build Receipt (G6)

**Marker:** `KUN_G6_STATUS_DEBATE_MAP_V1_BUILT_20260722`
**Gate:** G6 opened by explicit user line — *"open G6: build the status/debate map v1, docs-only."* Scope honored exactly: docs-only, no reader-facing prose, no product/DB/git/deploy.
**Result:** Built + validated **PASS**.

---

## What was built

Three deliverables under `phase-p/` (plus this receipt), all derived purely from Claim Ledger Contract v1 (`docs/claim_ledger_contract_v1_agn_20260703T0830Z/`, frozen, read-only):

| File | Role |
|---|---|
| `build_status_debate_map.py` | reproducible builder — pure function of Contract v1 (ledger + seed + stance matrix) |
| `status_debate_map_v1.json` | the docs-only status/debate map v1 |
| `validate_status_debate_map.py` | validator enforcing §8 acceptance |
| `status_debate_map_v1_validation.json` | validation report — **status: PASS** |

The build implements the design in `STATUS_DEBATE_MAP_GATE_PROPOSAL.md` §5–§6 exactly.

---

## What the map contains

Four debate axes over the 16-entry ledger, each with a `certainty_level` status, member entries, structured counterevidence, epistemic caps, and the seed's verbatim reader-guard:

| Axis | status | members | notes |
|---|---|---|---|
| `mechanism` | `widely_supported` | 5 | seed status `widely_supported_scoped` reconciled to enum (original preserved in `status_seed_original`); **+`clc_agn_008`** (SF-driven counter, `contradicts clc_agn_001`) and **+`clc_agn_006`** (local scope, `same_axis clc_agn_001`) re-attached |
| `prevalence` | `emerging_sample_limited` | 5 | D'Eugenio case capped `single_case → shows_can_occur` |
| `dominance_debate` | `actively_debated` | 5 | **+`clc_agn_005`** (gas-retention qualifier) re-attached; alternative channels kept as `same_axis` positions, not contradictions |
| `simulation_support` | `contradicted_or_model_dependent` | 2 | both simulation → `in_model_only`; observational maintenance-heating corpus gap noted, not filled |

---

## Acceptance (validator, all green)

- **Coverage:** `entry_count 16`, `entries_referenced 16`, `unmapped 0` — every ledger entry mapped. The three seed orphans (`clc_agn_005/006/008`) are re-attached by their own ledger links, not by guess; the previously-dropped `clc_agn_008 → contradicts → clc_agn_001` counterevidence (span `span_2016MNRAS_456L__25S_02`) is restored.
- **Enum conformance:** every axis `status ∈ certainty_level`; every `counterevidence.relation ∈ {contradicts, qualifies, same_axis}`; every `epistemic_caps.ceiling_modality ∈ modality`.
- **Provenance:** all 16 member ids, all `target_entry_id`s, and all `span_id`s resolve to real rows in `claim_status_ledger.jsonl` / `claim_source_stance_matrix.jsonl`. No invented ids.
- **Counterevidence preserved:** every ledger link of type `contradicts`/`qualifies` appears in some axis's `counterevidence[]` — nothing dropped. 28 counterevidence items, 4 epistemic caps.
- **Vocabulary bridge (flag only):** `mixed_debated` (exact overlap with backend `_STATUS_SEMANTIC_CAPS`) and `model_bounded` (no ledger counterpart → nearest `in_model_only`/`reported_only`) recorded in the map's `vocabulary_bridge` for a future, separately-gated wiring. **No code touched.**

---

## Safety (asserted, all zero)

`db_writes 0 · sql_mutations 0 · migrations 0 · git_writes 0 · deploy_restart 0 · product_publish 0 · galaxy_prose_draft 0 · exact_diff_packet 0 · secrets_access 0 · network 0`.
Contract v1 unmodified (read-only). Files written this pass: **5** (builder, map, validator, validation report, this receipt) — all under `phase-p/`.

---

## Provenance (SHA-256)

```
142ab6a0852019fb91a30e9b65fd06fb828f1d1acf75ae1a8af84c878f7dae42  build_status_debate_map.py
232e3cadc0add24a36533fd399d1e7c3ad149fb9d1784ef643a13b08c63f3e98  status_debate_map_v1.json
4d3e70cbadc6818ec60196834eff9c08b790299161347c5f1f21fca5f7f89644  validate_status_debate_map.py
d711529699f053c6859fcc656fa298a46670db160cf357b3bf2b1ae823438518  status_debate_map_v1_validation.json
```
(Rebuild is deterministic except the `as_of` timestamp in the map; re-running the builder reproduces identical content otherwise.)

---

## What this does NOT authorize

Wiring the map into trust scoring (`trust_calculation.py`), the wiki, the Ideas/Methods surfaces, or any reader-facing view — and any edit to Contract v1 — remains a **separate future gate** with its own recount and user approval. No prose was written or unblocked.

**Gate ledger:** G1 Completed · G2 Completed · G3 Closed (re-latched Held) · G4a/G4b/G4c Held separately · G5 Closed · **G6 — docs-only status/debate map v1 BUILT + validated PASS; wiring held as a separate future gate; no approval phrase, no cockpit/status write** · G7 Closed.

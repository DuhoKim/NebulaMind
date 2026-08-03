# Status / Debate-Map Gate — Design Proposal (G6)

**Marker:** `KUN_G6_STATUS_DEBATE_MAP_GATE_PROPOSAL_20260722`
**Boundary:** Docs-only design proposal. Prose remains blocked. This document authorizes **no** reader-facing prose, product mutation, DB write, migration, git write, deploy/restart, cockpit update, or publication. It does **not** regenerate or edit Claim Ledger Contract v1. There is **no active approval phrase** in this page.
**Kun recommendation #3** (ruling: *Replace*): "Revalidate and preserve the completed packet; reconcile the board; then **design the optional docs-only status/debate-map gate.**" This is that design — a proposal for a future gate, held for user review.

---

## 1. Purpose

Contract v1 already produced a validated, 16-entry claim ledger and a **seed** status/debate map (`artifacts/status_debate_map_seed.json`) built as a validation stub — 4 axes, member entries, and a natural-language `reader_guard` per axis. The seed was deliberately minimal: it is a *seed*, not a finished map.

The **status/debate-map gate (G6)**, if opened, would produce **one new docs-only artifact** — a *status/debate map v1* — that:

1. **derives entirely from the existing 16 ledger entries** (no new claims, no new sources, no new evidence);
2. **preserves every debate axis and every piece of counterevidence** the ledger already carries, including the three entries the seed left unmapped;
3. **replaces prose-only counterevidence hints with structured links** (`contradicts` / `qualifies` / `same_axis`) so the map is machine-checkable, not just readable;
4. **reconciles the seed's status vocabulary** to the controlled `certainty_level` enum so the map validates against `ledger_enums`;
5. **flags** (but does not perform) the backend vocabulary reconciliation between the ledger and `_STATUS_SEMANTIC_CAPS`.

The map is an **epistemic index over the ledger** — "for each debate axis, what is its status, which claims sit on it, and where is the counterevidence" — kept strictly upstream of any prose or product surface.

---

## 2. Inputs (read-only)

All from `docs/claim_ledger_contract_v1_agn_20260703T0830Z/` (Contract v1; every artifact carries `CLAIM_LEDGER_CONTRACT_V1_AGN_BUILT_20260703T0830Z`; `validation/contract_validation.json` = **PASS**, all side-effect counters 0):

| Input | Role in this gate |
|---|---|
| `artifacts/claim_status_ledger.jsonl` | the 16 entries — the sole source of map content |
| `artifacts/status_debate_map_seed.json` | the 4-axis seed this gate formalizes and completes |
| `artifacts/ledger_enums.md` / `.json` | the controlled vocabularies the map must validate against |
| `artifacts/claim_source_stance_matrix.jsonl` | 45 (entry × source × span) stance rows — the counterevidence spans |
| `artifacts/prose_sentence_bindings.jsonl` | 16 template bindings + modality-tier gates (upper bound on wording) |
| `artifacts/wording_contract_check.json` | per-sentence modality ceiling check (all 16 pass) |
| `validation/contract_validation.json` | structural counts + all-zero safety block the map must also satisfy |

**Contract v1 is frozen.** This gate reads it; it never rewrites, re-derives, or edits it. The map v1 is a **new** artifact that points back at Contract v1 by marker.

---

## 3. What the ledger already encodes (so the map preserves it)

The ledger has no literal `status` or `debate_stance` field. The concepts are carried by three enums (`ledger_enums`):

- **status** ← `certainty_level` ∈ {`established`, `widely_supported`, `emerging_sample_limited`, `actively_debated`, `contradicted_or_model_dependent`, `no_info`}
- **debate tier / stance** ← `modality` ∈ {`is_are_does`, `commonly_probably`, `may_or_can`, `shows_can_occur`, `mixed_debated`, `in_model_only`, `reported_only`}
- **counterevidence direction** ← per-span `stance` ∈ {`supports`, `qualifies`, `contradicts`, `mixed`, `no_info`} and `links.type` ∈ {`specializes`, `generalizes`, `contradicts`, `qualifies`, `depends_on`, `same_axis`}

Counterevidence is real and present: explicit `contradicts` spans in **entry 10** (`clc_agn_008`, SF-driven outflows counter entry 1) and **entry 16** (`clc_agn2299_003`, dominance debate); qualifier stances in entries 3, 5, 9, 14, 15, 16; epistemic caps on entries 5 (`single_case` → ceiling `shows_can_occur`), 6/13 (`simulation` → ceiling `in_model_only`).

---

## 4. Gaps in the seed this gate closes

The seed is a stub with three concrete gaps. The map v1 fixes exactly these — nothing more:

### G6-A — Three ledger entries are unmapped (counterevidence loss)
The seed references 13 of 16 entries. Unmapped:

| Entry | What it is | `certainty_level` | Why it matters | Proposed placement |
|---|---|---|---|---|
| `clc_agn_008_star_formation_driven_outflow_counter` | in typical low-z galaxies, outflows are **SF-driven, not AGN** | `emerging_sample_limited` | **live counterevidence** — carries `stance=contradicts` + `links.type=contradicts` against `clc_agn_001` (mechanism). Dropping it silently deletes the strongest counter on the mechanism axis. | **mechanism** axis, as structured `contradicts` counterevidence |
| `clc_agn_005_gas_retention_low_sfe_qualifier` | gas retention / low SFE qualify simple gas-removal quenching | `actively_debated` | a debated qualifier position on whether AGN gas-removal dominates | **dominance_debate** axis, as `qualifies` counter-position |
| `clc_agn_006_central_kpc_depletion_local_qualifier` | AGN central-kpc depletion is **local, not global** | `emerging_sample_limited` | a scope qualifier on the ejective mechanism; its own ledger links are `same_axis → clc_agn_001` and `qualifies → clc_agn_005` | **mechanism** axis, as a `same_axis` scope-bound on `clc_agn_001` |

**Rule:** the map v1 must reference **all 16** entries; every entry appears in ≥1 axis. An entry may appear in multiple axes (the seed already does this for `clc_agn_004`, in both *mechanism* and *simulation_support*).

### G6-B — Seed status vocabulary is off-enum
Axis 1's seed `status` is `widely_supported_scoped`, which is **not** a `certainty_level` value. Reconcile to the enum: use `widely_supported` and move "scoped" into the `reader_guard`. Every axis `status` in map v1 must be drawn from the `certainty_level` enum verbatim.

### G6-C — Counterevidence is prose-only
The seed expresses counters inside `reader_guard` free text ("counters must remain visible", "same_axis, not contradiction"). Map v1 promotes these to a **structured** `counterevidence[]` array per axis, each item `{entry_id, relation ∈ {contradicts, qualifies, same_axis}, target_entry_id?, span_ids[]}`, drawn directly from the ledger's `links` and stance-matrix spans. The `reader_guard` prose is retained verbatim as an additional human-facing note — it is never the machine record.

---

## 5. Proposed map v1 — schema

A single JSON artifact (`status_debate_map_v1.json`), docs-only:

```
{
  "marker": "CLAIM_STATUS_DEBATE_MAP_V1_AGN_<UTC>",
  "as_of": "<UTC>",
  "boundary": "Docs-only status/debate map over Contract v1; prose remains blocked; no product mutation.",
  "source_contract": "claim_ledger_contract_v1_agn_20260703T0830Z",
  "derived_from_seed": "artifacts/status_debate_map_seed.json",
  "axes": [
    {
      "axis": "<mechanism|prevalence|dominance_debate|simulation_support>",
      "status": "<certainty_level enum value>",
      "member_entries": ["<entry_id>", ...],
      "counterevidence": [
        {"entry_id": "...", "relation": "contradicts|qualifies|same_axis",
         "target_entry_id": "...", "span_ids": ["..."]}
      ],
      "epistemic_caps": [
        {"entry_id": "...", "cap": "single_case|simulation", "ceiling_modality": "shows_can_occur|in_model_only"}
      ],
      "reader_guard": "<verbatim seed guard, retained>"
    }
  ],
  "coverage": {"entry_count": 16, "entries_referenced": 16, "unmapped": []}
}
```

### The four axes, fully expanded (map v1)

**Axis `mechanism` — status `widely_supported` (scoped).**
member_entries: `clc_agn2299_001_mechanism`, `clc_agn_001_ejective_mechanism_selected_systems`, `clc_agn_004_preventive_maintenance_heating_distinct`, **`clc_agn_008_star_formation_driven_outflow_counter`** (newly attached), **`clc_agn_006_central_kpc_depletion_local_qualifier`** (newly attached).
counterevidence: `{clc_agn_008 → contradicts → clc_agn_001}` (from the ledger's own `contradicts` link + span); `{clc_agn_006 → same_axis → clc_agn_001}` (local central-kpc scope bound on the ejective mechanism); qualifier spans on `clc_agn2299_001` (simulation qualifier).
epistemic_caps: `clc_agn_004` simulation → `in_model_only`.
reader_guard (retained): "can occur / can drive in scoped contexts; distinguish ejective vs maintenance/heating." *(scope note absorbs the seed's "_scoped").*

**Axis `prevalence` — status `emerging_sample_limited`.**
member_entries: `clc_agn2299_002_prevalence`, `clc_agn_002_outflow_prevalence_scoped_samples`, `clc_agn_002a_mosdef_17pct_ionized_outflows`, `clc_agn_002b_jwst_46pct_neutral_naid_outflows`, `clc_agn_003_deugenio_case_not_prevalence`.
counterevidence: `{clc_agn_003 → qualifies}` (case, not prevalence anchor; `risk_flags: CASE_ROW_NOT_PREVALENCE_ANCHOR`).
epistemic_caps: `clc_agn_003` single_case → `shows_can_occur`.
reader_guard (retained): "substantial subsets in selected samples; never universal; sample-child entries preserve 17% MOSDEF and 46% JWST fractions; D'Eugenio case excluded as prevalence anchor."

**Axis `dominance_debate` — status `actively_debated`.**
member_entries: `clc_agn2299_003_dominance_debate`, `clc_agn_007_alternative_quenching_channels`, `clc_agn_009_central_bh_bulge_predictor_axis`, `clc_agn_010_halo_environment_satellite_axis`, **`clc_agn_005_gas_retention_low_sfe_qualifier`** (newly attached).
counterevidence: `{clc_agn2299_003 → contradicts/qualifies}` (2 contradicts + 2 qualifies spans); `{clc_agn_007 → same_axis}` (alternative channels are positions *within* the debate, not contradiction of it); `{clc_agn_005 → qualifies}` (gas retention / low SFE qualifies gas-removal quenching).
reader_guard (retained): "AGN is one axis; alternatives/counters and central-vs-environment axes must remain visible. Alternative channels are positions within the debated axis (same_axis), not contradiction of the fact that dominance is debated."

**Axis `simulation_support` — status `contradicted_or_model_dependent`.**
member_entries: `clc_agn_011_simulations_model_dependent_support`, `clc_agn_004_preventive_maintenance_heating_distinct`.
epistemic_caps: both simulation → `in_model_only`.
counterevidence: corpus-gap annotation on `clc_agn_004` (observational maintenance-heating evidence absent — queued, not filled).
reader_guard (retained): "in simulations / under model assumptions; never observed frequency; observational maintenance-heating corpus gap queued but not filled in this run."

**Coverage after G6-A:** all 16 entries referenced; `unmapped: []`.

---

## 6. Derivation rules (deterministic, ledger-only)

The map builder must be a pure function of Contract v1 — no judgement beyond these rules:

1. **Axis membership** comes from the seed's axis assignments, plus the three G6-A attachments justified by each entry's own ledger `links` (not by semantic guess): `clc_agn_008` → mechanism via its `contradicts → clc_agn_001` link; `clc_agn_006` → mechanism via its `same_axis → clc_agn_001` link; `clc_agn_005` → dominance_debate via its `qualifies → clc_agn2299_003` link (and `actively_debated` status). Where an entry's links point at more than one axis, it is placed on each (multi-axis membership is allowed, as the seed already does for `clc_agn_004`).
2. **Axis `status`** = a `certainty_level` enum value (G6-B). Where the seed gave an off-enum string, map to the nearest enum value and preserve the modifier in `reader_guard`.
3. **`counterevidence[]`** is populated only from existing ledger `links` (types `contradicts`, `qualifies`, `same_axis`) and their backing `span_ids` in the stance matrix. No new links are invented.
4. **`epistemic_caps[]`** is copied from entries whose `epistemic_type` ∈ {`single_case`, `simulation`}, with the ceiling modality the contract already mandates (`shows_can_occur` / `in_model_only`).
5. **`reader_guard`** strings are copied verbatim from the seed; never rewritten (they are audited prose, not new prose).
6. One **known discrepancy to record, not silently resolve:** entry `clc_agn_005` has `modality = may_or_can` in the ledger but is treated as `mixed_debated` in `wording_contract_check.json`. The map notes both and flags it for a Contract-v1 erratum (a *separate* future decision — this gate does not touch Contract v1).

---

## 7. Backend vocabulary reconciliation (flag only — no code in this gate)

The live backend (`backend/app/services/trust_calculation.py`) caps trust by debate/status semantics:

```python
_STATUS_SEMANTIC_CAPS = {"mixed_debated": "debated", "model_bounded": "reported"}
```

- **`mixed_debated`** — exact string overlap with the ledger `modality` enum. Good: the map and the backend already speak the same word for the debate tier.
- **`model_bounded`** — **has no ledger counterpart.** The ledger expresses the same idea as `modality ∈ {in_model_only, reported_only}` and `certainty_level = contradicted_or_model_dependent`. The backend cap *value* `"reported"` echoes the ledger's `reported_only` — suggesting the intended bridge.

The map v1 documents this mismatch in a `vocabulary_bridge` note so that a **future, separately-gated** wiring (map → trust caps) has an unambiguous crosswalk. **This gate proposes no edit to `trust_calculation.py`, no DB write, and no test change** — the reconciliation is recorded as design intent only.

---

## 8. Validation & acceptance (for the map artifact, when built)

Mirrors Contract v1's own gate discipline:

- **Coverage:** `entries_referenced == 16`, `unmapped == []`.
- **Enum conformance:** every axis `status` ∈ `certainty_level`; every `counterevidence.relation` ∈ {`contradicts`, `qualifies`, `same_axis`}; every `epistemic_caps.ceiling_modality` ∈ `modality`.
- **Provenance:** every `entry_id`, `target_entry_id`, and `span_id` resolves to a real row in `claim_status_ledger.jsonl` / `claim_source_stance_matrix.jsonl`. No invented ids.
- **Counterevidence preserved:** every ledger `links.type ∈ {contradicts, qualifies}` appears in some axis's `counterevidence[]` (nothing dropped).
- **Safety block (all zero, asserted):** `db_writes: 0`, `sql_mutations: 0`, `migrations: 0`, `git_writes: 0`, `deploy_restart: 0`, `product_publish: 0`, `galaxy_prose_draft: 0`, `exact_diff_packet: 0`, `secrets_access: 0`.
- A small `validate_status_debate_map.py` (docs-tool, alongside the artifact) enforces the above — same pattern as Contract v1's `validate_contract.py`.

---

## 9. Explicit non-authorizations

This gate, if opened, does **not** and **may not**:

- write or edit any reader-facing prose (Galaxy Evolution or otherwise) — "prose remains blocked";
- mutate claims/evidence, write the DB, run migrations, or touch SQL;
- change `trust_calculation.py` or any product code, or add/modify product tests;
- deploy, restart, update the cockpit, or publish anything;
- regenerate, re-derive, or edit **Contract v1** or any of its artifacts;
- create an exact-diff packet or a production stance mapping.

Its sole output is **one docs-only JSON map + its validator + a short receipt**, under `phase-p/`.

---

## 10. The gate (G6) — held

**Status: HELD.** No approval phrase is issued by this proposal.

**Opening G6 would authorize (docs-only):** building `status_debate_map_v1.json` per §5–§6, its `validate_status_debate_map.py`, and a build receipt — nothing else. Acceptance = §8 all green.

**Opening G6 does NOT authorize:** anything in §9. In particular, wiring the map into trust scoring, the wiki, or any reader surface is a **separate future gate** with its own recount and user approval.

**To open it, the user would give an explicit line** naming G6 and the docs-only scope (e.g., "open G6: build the status/debate map v1, docs-only"). Until then it stays held.

---

**Gate ledger:** G1 Completed · G2 Completed · G3 Closed (re-latched Held) · G4a/G4b/G4c Held separately · G5 Closed · **G6 Held — this proposal delivered; docs-only design for user review; no approval phrase, no cockpit/status write** · G7 Closed.

**Files written by this pass:** 1 (this proposal). No git write, no source edit, no DB, no network, no product mutation.

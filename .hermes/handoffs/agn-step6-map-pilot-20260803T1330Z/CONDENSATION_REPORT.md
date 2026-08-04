# Condensation Report — 16 ledger entries + seed → K axes

- Lane: `agn-step6-map-pilot-20260803T1330Z` · compiled 2026-08-03T13:07Z
- Inputs: `claim_status_ledger.jsonl` (16 entries), `status_debate_map_seed.json` (4 axes),
  `ledger_enums.json` (link-type vocabulary).
- **Output: K = 5 axes.**

## The merge rule (stated as a rule; determinism scoped below)

Condensation uses ONLY the ledger's own structure: the `links` graph (types from
`ledger_enums.json` `links.type`), `tags`, and binding `risk_flags`/verification notes. Determinism
holds for R1/R2/R3/R5/R6 — those rules re-execute mechanically from the link graph and tags.
**R4's distinct-question test is argued per-case and is reviewable**: whether two unassigned entries
pose a question distinct from every seed assertion is a semantic judgment, not a mechanical
consequence of link topology. Its one application here (005+006 → Axis D) is recorded with its
argument below so a reviewer can accept or reject it.

- **R1 — Axis seeding.** Each of the three derived claim-2299 split entries (tag `claim2299_trio`)
  seeds one axis: mechanism (A), prevalence (B), dominance/debate (C). `clc_agn_011` (tag
  `simulation_cap`) seeds a fourth axis (E); the other `simulation_cap`-tagged entry,
  `clc_agn_004`, does not seed E — it joins E by R6 (dual membership). This reproduces the seed
  map's four axes exactly.
- **R2 — Parent–child collapse.** Any entry connected to an axis seed by a `specializes` or
  `generalizes` link (either direction) merges into that seed's axis.
  Applied: clc_agn_001→A; clc_agn_002, clc_agn_002a, clc_agn_002b→B.
- **R3 — Guard-row override.** An entry carrying a binding risk flag that names an axis role is
  placed on the axis it guards, regardless of R2.
  Applied: clc_agn_003 (`CASE_ROW_NOT_PREVALENCE_ANCHOR`) → B as excluded-anchor guard row, even
  though it also `specializes` clc_agn2299_001 (A). Its case-support role for A is kept as a
  cross-reference, not membership.
- **R4 — Distinct-question split.** If two or more entries not yet assigned by R1–R3 link to each
  other (`qualifies` or `same_axis`) and their shared question is not the seed assertion of any
  existing axis, they form a new axis rather than being scattered as qualifiers.
  Applied: clc_agn_005 + clc_agn_006 (006 `qualifies` 005; both tagged `retention`) → new Axis D
  ("does quenching require gas removal?"). No existing seed assertion poses this question: A asks
  whether AGN *can* remove gas, C asks *which channel dominates*; D asks whether removal *happened*.
- **R5 — Side placement.** A remaining entry linked to an axis seed only by `qualifies`,
  `contradicts`, or `same_axis` joins that axis as a named side/countercase (not merged into another
  entry's side).
  Applied: clc_agn_007 (`same_axis` → clc_agn2299_003) → C; clc_agn_009 and clc_agn_010 (each
  `qualifies` → clc_agn2299_003; their `same_axis` links point at each other, not at the seed) → C;
  clc_agn_008 (`qualifies` → clc_agn2299_003 — ledger-only placement basis; its stance-matrix
  `contradicts` row is corroboration, not the basis) → C.
- **R6 — Dual membership.** An entry may belong to at most two axes, and only when the ledger links
  it into both (a `same_axis` link into one and a shared tag/seed into the other).
  Applied: clc_agn_004 (`same_axis` → clc_agn_001 in A; `simulation_cap` tag with clc_agn_011 in E).
  No other entry qualifies.

Rule precedence: R1 > R3 > R2 > R4 > R5; R6 is a constraint on the result.

## Assignment trace (every entry, the rule that placed it)

| Entry | Axis | Placing rule |
|---|---|---|
| clc_agn2299_001_mechanism | A | R1 (seed) |
| clc_agn2299_002_prevalence | B | R1 (seed) |
| clc_agn2299_003_dominance_debate | C | R1 (seed) |
| clc_agn_011_simulations_model_dependent_support | E | R1 (simulation_cap seed) |
| clc_agn_001_ejective_mechanism_selected_systems | A | R2 (generalizes-link with A seed) |
| clc_agn_002_outflow_prevalence_scoped_samples | B | R2 (specializes-link with B seed) |
| clc_agn_002a_mosdef_17pct_ionized_outflows | B | R2 (specializes → 002/B seed) |
| clc_agn_002b_jwst_46pct_neutral_naid_outflows | B | R2 (specializes → 002/B seed) |
| clc_agn_003_deugenio_case_not_prevalence | B (guard row) | R3 (risk flag overrides its R2 pull toward A) |
| clc_agn_004_preventive_maintenance_heating_distinct | A + E | R6 (same_axis→001 in A; simulation_cap in E) |
| clc_agn_005_gas_retention_low_sfe_qualifier | D | R4 (new-axis split with 006) |
| clc_agn_006_central_kpc_depletion_local_qualifier | D | R4 (new-axis split with 005) |
| clc_agn_007_alternative_quenching_channels | C | R5 (same_axis → C seed) |
| clc_agn_008_star_formation_driven_outflow_counter | C | R5 (qualifies → C seed; ledger-only basis) |
| clc_agn_009_central_bh_bulge_predictor_axis | C | R5 (qualifies → C seed; same_axis is to 010, not the seed) |
| clc_agn_010_halo_environment_satellite_axis | C | R5 (qualifies → C seed; same_axis is to 009, not the seed) |

Coverage: 16/16 assigned; 1 dual membership (clc_agn_004); 0 unassigned.

## Which entries merged where, which stand alone

- **Merged into parent axes (R2):** 001 (into A); 002, 002a, 002b (into B). Note the children 002a/002b
  merge as *axis members* only — their fractions (17%, 46%) are never merged numerically, per the
  ledger's do-not-average verification notes.
- **Stand alone within their axis (own named side or role, no absorption):** 003 (guard row, B);
  004 (model-only side, A/E); 005 and 006 (the two sides of D); 007, 008, 009, 010 (four named
  positions in C); 011 (E's substance).
- **Nothing was dropped.** The seed omitted 005, 006, 008; R4/R5 recover them (declared as departures
  #1–#2 in the map, §7).

## K as an output

K = 4 (seed, reproduced by R1) + 1 (R4 split) = **5**. K was not chosen; it is the fixed point of
R1–R6 on the ledger's link graph. Re-running R1/R2/R3/R5/R6 on the same ledger yields the same
partition mechanically; the R4 split reproduces given its recorded distinct-question argument, which
a fresh reader is entitled to re-examine.

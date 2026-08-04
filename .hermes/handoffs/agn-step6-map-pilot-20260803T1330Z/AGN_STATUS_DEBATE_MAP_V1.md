# AGN Status/Debate Map — v1

- **As of:** 2026-08-03T13:07Z (compiled). Ledger `as_of`: 2026-07-03.
- **Lane:** `agn-step6-map-pilot-20260803T1330Z` (Lana — no-overclaim/semantic lane).
- **Source of ALL claim content:** `docs/claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/claim_status_ledger.jsonl`
  (16 entries) + `claim_source_stance_matrix.jsonl` (45 stance rows). No content beyond the ledger appears below.
- **Builds from seed:** `artifacts/status_debate_map_seed.json` (4 axes). Departures from the seed are
  listed in §7 and argued there; everything else follows the seed.
- **Verification status of the source ledger:** ALL 16 entries carry `verification_status: pending`.
  Every status label below — including `widely_supported` — binds to pending-verification entries;
  the labels are ledger-carried certainty enums, not verification outcomes. (Step-5 stance
  verification is the stage that flips this field; see also the closing footnote.)
- **Vocabulary:** status values are drawn ONLY from `ledger_enums.json` `certainty_level`; modality
  tiers only from `modality`; stances only from `stance`.
- **Lane law:** no sentence below uses a modality tier above the bound entry's ledger `modality`
  (cross-checked against `wording_contract_check.json` actual tiers).
- **Boundary (inherited from seed):** this is a status/debate MAP artifact, not reader-facing prose.
  Prose remains blocked; wiki placement is out of scope.

**K = 5 axes** (derivation: `CONDENSATION_REPORT.md`).

| # | Axis | Entries | Status (enum, per side where sides differ) |
|---|------|---------|--------|
| A | Mechanism: ejective vs. preventive/maintenance | clc_agn2299_001, clc_agn_001, clc_agn_004 | per-side (see axis) — ejective: `widely_supported` · maintenance: `contradicted_or_model_dependent` |
| B | Prevalence of outflow signatures | clc_agn2299_002, clc_agn_002, clc_agn_002a, clc_agn_002b, clc_agn_003 | `emerging_sample_limited` |
| C | Driver/dominance of quenching | clc_agn2299_003, clc_agn_007, clc_agn_008, clc_agn_009, clc_agn_010 | `actively_debated` |
| D | Gas fate: removal vs. retention | clc_agn_005, clc_agn_006 | `actively_debated` |
| E | Simulation support cap | clc_agn_011, clc_agn_004 | `contradicted_or_model_dependent` |

All 16 ledger entries are mapped; `clc_agn_004` sits in A and E (ledger links it `same_axis` to
`clc_agn_001` while tagged `simulation_cap` with `clc_agn_011`) — see coverage table, §6.

---

## Axis A — Mechanism: can AGN/SMBH feedback remove, heat, or deplete star-forming gas?

**Sides**

- **Ejective feedback (observational):** `clc_agn2299_001_mechanism`, `clc_agn_001_ejective_mechanism_selected_systems`.
  Position: AGN activity **can** drive gas outflows capable of removing or depleting star-forming fuel
  in *selected massive or AGN-host galaxies* (modality `may_or_can`; not universal — the entries' own
  scope says "not universal; source-specific").
- **Preventive/maintenance heating (model-only):** `clc_agn_004_preventive_maintenance_heating_distinct`.
  Position: **in simulations**, maintenance heating (chaotic cold accretion; dual jet/heating modes) is a
  distinct channel from ejective outflows (modality `in_model_only`).

**Best evidence per side, with source-strength**

- Ejective: 2024NatAs...8.1443D (span_2024NatAs___8_1443D_07 — "neutral outflow rate is ten times
  higher than the SFR … direct evidence for ejective SMBH feedback"); 2024MNRAS.528.4976D
  (span_2024MNRAS_528_4976D_05 — mass outflow rates 3–100 M⊙/yr); 2014A&A...562A..21C (AGN "can boost
  the outflow rate by a large factor … increase with LAGN/Lbol"). Source-strength: `observational_sample`
  + one `observational_case`, all `full_text`, consistency `consistent`, multiple scoped samples plus case.
- Maintenance: 2013MNRAS.432.3401G, 2012MNRAS.420.2662D. Source-strength: `simulation_model` only,
  `full_text`, `model_dependence: high` — the ledger's `corpus_gap_annotation` records that observational
  maintenance evidence (X-ray cavities/bubbles) is absent from the approved corpus, capping this side at
  model-dependent certainty.

**Measurement dispersion (ledger-carried numbers):** outflow rates 3–100 M⊙/yr (2024MNRAS.528.4976D,
within `clc_agn_001`); case rate 10× SFR (2024NatAs, single case). No cross-sample combination is
licensed by the ledger.

**Status (enums):** ejective side `widely_supported`; maintenance side `contradicted_or_model_dependent`.
No single axis-level label is emitted because the sides sit at different enum levels.

**Countercase check (required for `widely_supported`):** who would disagree, and are they in the corpus?
Yes — `clc_agn_008` (stance `contradicts` toward `clc_agn_001`): in typical low-z galaxies cold-gas
outflows **may** be driven by star formation, not AGN. The ejective claim survives because it is scoped
to *selected* systems, not typical ones; the ledger's own link topology records the tension.

**What would settle it:** for the maintenance side, filling the recorded corpus gap (observational
X-ray cavity/bubble literature — queued in the ledger's `corpus_gap_annotation`, explicitly not to be
filled inside this run) is the single move that could lift it off `in_model_only`. For the ejective
side, driver-attribution evidence of the kind `clc_agn_008` demands (AGN vs. star-formation
discrimination in matched samples) bounds how far "selected systems" can widen.

---

## Axis B — Prevalence: how often do AGN-associated outflow signatures occur?

**Sides** (this axis is parent–child, not adversarial — the "sides" are scoped fractions that must
not be merged)

- **Parent:** `clc_agn2299_002_prevalence`, `clc_agn_002_outflow_prevalence_scoped_samples` — outflow
  signatures occur in substantial but *sample-dependent* fractions of selected samples, not universally
  (modality `may_or_can`).
- **Child 1 (ionized, MOSDEF):** `clc_agn_002a_mosdef_17pct_ionized_outflows` — 17% of 159 AGNs,
  z=1.4–3.8 (`single_source`).
- **Child 2 (neutral Na I D, JWST):** `clc_agn_002b_jwst_46pct_neutral_naid_outflows` — 46% of 113
  massive (log M*/M⊙>10) z~2 galaxies show excess Na I D; half of profiles blueshifted ≥100 km/s[^kms]
  (`single_source`).

[^kms]: Ledger-carried verbatim, re-checked against the ledger 2026-08-03: `span_2024MNRAS_528_4976D_03`
    (finding zone, `full_text`) — "Half of the absorption profiles are blueshifted by at least
    100 km s−1, providing unambiguous evidence for neutral gas outflows."
- **Excluded anchor (guard row):** `clc_agn_003_deugenio_case_not_prevalence` — GS-10578 **shows that**
  ejective SMBH feedback **can occur** at z=3 (modality `shows_can_occur`, single case); its binding
  risk flag `CASE_ROW_NOT_PREVALENCE_ANCHOR` forbids counting it toward any fraction.

**Best evidence with source-strength:** 2019ApJ...886...11L (span_2019ApJ___886___11L_03, finding zone,
`full_text`) for 17%; 2024MNRAS.528.4976D (spans _02/_03, finding zone, `full_text`) for 46%;
2014ApJ...796....7G supports the parent's "substantial in high-mass samples" scope. All
`observational_sample`.

**Measurement dispersion:** the ledger carries two fractions — 17% (ionized tracer, AGN-selected) and
46% (neutral Na I D tracer, mass-selected). The ledger's verification notes are explicit: **do not
average fractions across tracers/selections**. The honest dispersion statement is therefore: reported
detection fractions span 17%–46% *across different tracers, selections, and redshift windows*, and the
spread is at least partly definitional, not a measurement scatter on one quantity.

**Status (enum):** `emerging_sample_limited` (all five entries carry it; matches seed).

**What would settle it:** a matched-tracer, matched-selection census across redshift — i.e., fractions
measured per tracer on comparable samples — would turn the current tracer-confounded 17–46% spread into
a real dispersion on defined quantities. (Meta-statement about evidence structure; no new claim.)

---

## Axis C — Driver/dominance: which quenching channel dominates, and where?

**Sides**

- **Debate frame (holder of the axis):** `clc_agn2299_003_dominance_debate` — AGN feedback is one
  important axis, but dominance relative to stellar feedback, gas retention, strangulation, stripping,
  halo/environment, and satellite channels remains debated and context-dependent (modality
  `mixed_debated`, status `actively_debated`).
- **Alternative-channels position:** `clc_agn_007_alternative_quenching_channels` — strangulation,
  environmental stripping, and cold-gas pathway differences **are** mandatory alternative or qualifying
  channels (modality `is_are_does`, `widely_supported`). Papers: 2015Natur.521..192P (strangulation
  primary for local Mstar<1e11, ~4 Gyr timescale), 2021PASA...38...35C (stripping ubiquitous in
  satellites), 2020MNRAS.493.1982J (centrals defy simple pathways).
- **Central/BH-predictor position:** `clc_agn_009_central_bh_bulge_predictor_axis` — bulge mass,
  central velocity dispersion, or black-hole mass **are** a real quenching-predictor axis
  (`is_are_does`, `widely_supported`). Papers: 2014MNRAS.441..599B, 2020MNRAS.492...96B; the M_BH-ML
  row (2022MNRAS.512.1052P) enters only at stance `qualifies` because it is simulation-comparison-based.
- **Halo/environment/satellite position:** `clc_agn_010_halo_environment_satellite_axis` — halo,
  environment, and satellite channels **are** also real axes and must remain separate from central/BH
  predictors (`is_are_does`, `widely_supported`). Papers: 2010ApJ...721..193P (mass vs. environment
  quenching separable to z~1; cessation in 30%–70% of satellites), 2013MNRAS.432..336W (satellite
  quenching dominant below Mstar<1e10; delayed-then-rapid: 2–4 Gyr delay, e-folding <0.8 Gyr).
- **Star-formation-driver countercase:** `clc_agn_008_star_formation_driven_outflow_counter` — in
  typical low-z galaxies (456-galaxy sample, z<0.2), cold-gas outflows **may** be driven by star
  formation rather than AGN; stance `contradicts` toward AGN-driver dominance
  (`emerging_sample_limited`, `single_source`).

**Best evidence per side, with source-strength:** all positions above rest on `full_text`
observational rows; `clc_agn_007` is epistemic_type `review` with large samples (26,000 SDSS spectra;
Dawes review; xGASS), `clc_agn_009`/`clc_agn_010` are `observational_sample` with large surveys and
`consistent` consistency; `clc_agn_008` is one sample (`single_source`).

**Measurement dispersion (ledger-carried numbers):** strangulation timescale ~4 Gyr (local,
Mstar<1e11); satellite cessation fraction 30%–70%; satellite delay 2–4 Gyr with e-folding <0.8 Gyr.
These are per-channel numbers; the ledger licenses no cross-channel dominance fraction.

**Status (enum):** `actively_debated` (per `clc_agn2299_003` and the seed). Per Step-6, actively
debated is a valid reader-facing result, not a failure.

**Countercase check for the `widely_supported` positions inside this axis:** each is answered in-corpus —
`clc_agn_007` (alternatives) is held in tension by the AGN-side mechanism rows (Axis A) and the
simulation rows (Axis E, `qualifies` stance only); `clc_agn_009` vs. `clc_agn_010` mutually bound each
other (`same_axis` links; note their assertions are complementary "real axis" claims, not exclusive
dominance claims — neither asserts dominance over the other); `clc_agn_008` contradicts AGN-driver
readings directly. The debate frame itself requires no countercase: disagreement is its content.

**What would settle it:** the ledger structure implies dominance language stays blocked until a
position can name scope (mass, redshift, central/satellite) in which its channel is shown dominant
*with the other axes' entries represented* — the ledger's verification notes make `clc_agn_007` and
`clc_agn_010` mandatory blockers on AGN-only or central-only dominance wording.

---

## Axis D — Gas fate: does quenching require gas removal?

**Sides**

- **Retention qualifier:** `clc_agn_005_gas_retention_low_sfe_qualifier` — gas retention and low
  star-formation efficiency **can** qualify simple gas-removal accounts of quenching (modality
  `may_or_can`, status `actively_debated`, consistency `mixed`). Papers: 2021ApJS..252...29K
  (SFR-matched AGN show no molecular-gas difference), 2017ApJ...846L..14S (z~0.7 quenched galaxies
  retain large molecular reservoirs), 2019ApJ...884L..52Z (massive quiescent disks retain large HI).
  All three spans enter at stance `qualifies` — this entry is a qualifier row by construction, "not a
  refutation of ejective cases" (its verification note).
- **Central-depletion qualifier:** `clc_agn_006_central_kpc_depletion_local_qualifier` — some local
  AGN-host central regions show gas fractions a factor ~2 lower, but this is a *central-kpc* scoped
  result, not global quenching (modality `may_or_can`, `emerging_sample_limited`, `single_source`:
  2021MNRAS.505L..46E, EDGE-CALIFA; strongest statement rests on four best-spaxel galaxies).

**Best evidence with source-strength:** both sides `observational_sample`, `full_text`; retention side
is multi-source (`consistency: mixed` across three samples), depletion side single-source with an
explicit four-galaxy core.

**Measurement dispersion (ledger-carried numbers):** central AGN-region gas fractions ~2× lower than
star-forming regions (central kpc only). The retention side is qualitative-to-quantified per sample;
the ledger carries no combined retention fraction.

**Status (enum):** `actively_debated` (highest-information entry `clc_agn_005` carries it; `clc_agn_006`
is `emerging_sample_limited` and scoped inside it).

**What would settle it:** the two sides are scale-separated (global reservoirs vs. central kpc);
resolution requires evidence connecting the scales — e.g., whether central depletion of the
`clc_agn_006` kind coexists with the global reservoirs of `clc_agn_005` in the same systems. The
current corpus does not contain that joint measurement.

---

## Axis E — Simulation support: what do simulations establish, and what can they not?

**Sides** (one position plus its binding cap; no adversarial second side in-corpus)

- **Model support:** `clc_agn_011_simulations_model_dependent_support` — **in simulations** (HORIZON-AGN/
  noAGN, RAMSES zooms, IllustrisTNG, EAGLE/Illustris/TNG comparisons), AGN feedback mechanisms are
  supported under named model assumptions, but simulations do not by themselves establish observed
  prevalence (modality `in_model_only`). `clc_agn_004` shares this axis (maintenance heating,
  model-only; see Axis A).
- **The cap itself:** the verification note is binding — mechanism/model support only, never
  observed-frequency language.

**Best evidence with source-strength:** 2016MNRAS.463.3948D, 2013MNRAS.433.3297D, 2021MNRAS.500.4004D,
2022MNRAS.512.1052P — all `simulation_model`, `full_text`, `model_dependence: high`,
consistency `mixed`.

**Measurement dispersion:** none carried at axis level (qualitative, model-specific).

**Status (enum):** `contradicted_or_model_dependent` (both entries carry it; matches seed).

**What would settle it:** per the ledger, nothing inside simulation space — the cap lifts only via
observational anchors (for the maintenance channel, the same corpus gap named in Axis A).

---

## §6 Coverage table (every entry, its axis, its status enum, its modality ceiling)

| Entry | Axis | certainty_level | modality |
|---|---|---|---|
| clc_agn_001_ejective_mechanism_selected_systems | A | widely_supported | may_or_can |
| clc_agn_002_outflow_prevalence_scoped_samples | B | emerging_sample_limited | may_or_can |
| clc_agn_002a_mosdef_17pct_ionized_outflows | B | emerging_sample_limited | may_or_can |
| clc_agn_002b_jwst_46pct_neutral_naid_outflows | B | emerging_sample_limited | may_or_can |
| clc_agn_003_deugenio_case_not_prevalence | B (guard row; case cross-ref to A) | emerging_sample_limited | shows_can_occur |
| clc_agn_004_preventive_maintenance_heating_distinct | A + E | contradicted_or_model_dependent | in_model_only |
| clc_agn_005_gas_retention_low_sfe_qualifier | D | actively_debated | may_or_can |
| clc_agn_006_central_kpc_depletion_local_qualifier | D | emerging_sample_limited | may_or_can |
| clc_agn_007_alternative_quenching_channels | C | widely_supported | is_are_does |
| clc_agn_008_star_formation_driven_outflow_counter | C | emerging_sample_limited | may_or_can |
| clc_agn_009_central_bh_bulge_predictor_axis | C | widely_supported | is_are_does |
| clc_agn_010_halo_environment_satellite_axis | C | widely_supported | is_are_does |
| clc_agn_011_simulations_model_dependent_support | E | contradicted_or_model_dependent | in_model_only |
| clc_agn2299_001_mechanism | A | widely_supported | may_or_can |
| clc_agn2299_002_prevalence | B | emerging_sample_limited | may_or_can |
| clc_agn2299_003_dominance_debate | C | actively_debated | mixed_debated |

16/16 entries mapped; 0 unassigned.

## §7 Departures from the seed (declared, with reasons)

1. **Added `clc_agn_008` to Axis C (seed omitted it from every axis).** Placement basis is
   ledger-only: `qualifies` → `clc_agn2299_003` (the Axis-C seed); the ledger also carries its
   `contradicts` → `clc_agn_001` link, and its stance-matrix `contradicts` row corroborates the
   placement without being its basis. Leaving the corpus's only direct `contradicts`-stance
   observational countercase off the map would understate the debate — the opposite of this lane's job.
2. **Added a fifth axis D (gas fate) for `clc_agn_005` and `clc_agn_006` (seed omitted both).**
   They interlink (`clc_agn_006` `qualifies` → `clc_agn_005`; both `same_axis`/`qualifies` toward
   `clc_agn_001`) and pose a question — is gas actually removed? — that is not the seed assertion of
   any seed axis. Folding them into Axis A or C as loose qualifiers would hide a two-sided,
   scale-separated debate the ledger explicitly encodes. Step-6's grouping list (mechanism, prevalence,
   dominance, **alternatives, limitations**) anticipates such an axis.
3. **Replaced the seed's off-enum status labels.** The seed uses `widely_supported_scoped` (Axis A),
   which is not in `ledger_enums.json` `certainty_level`. The brief requires enum-only vocabulary, so
   Axis A reports per-side enum statuses (`widely_supported` / `contradicted_or_model_dependent`) with
   scope carried in prose at ledger modality, not in the status label.

Seed content otherwise preserved: axis membership of A, B, C-core, E; all reader guards (never
universal; do-not-average fractions; D'Eugenio excluded as prevalence anchor; in-model-only cap;
alternatives-visible requirement) are restated in the axes above.

---
Map bound to ledger `as_of` 2026-07-03; compiled 2026-08-03T13:07Z. All verification_status values in
the source ledger are `pending` (see LANA_REPORT.md, ambiguity #1).

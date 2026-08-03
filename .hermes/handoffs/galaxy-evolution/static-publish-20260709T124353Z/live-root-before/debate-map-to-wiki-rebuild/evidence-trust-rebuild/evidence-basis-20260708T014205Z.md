# Galaxy Evolution — Method3 evidence basis & trust ledger (docs-only, P2)

Order marker: `AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z`
Scope: docs-only / P2 non-binding. **This is the local provenance ledger the page's per-section "Evidence basis" panels link to.** It is NOT product claim/citation binding (that is a separate CLOSED P3 gate).

## What "trust" means on this page (plain English)

Method3 builds the page from a research-status **debate map**, not from bound product claim chips. So trust here is the **debate-map status** of each underlying axis — how settled the science is — plus the **coverage scope** of gap-filled sections. It is NOT a product trust score, and there are **0 product claim markers and 0 cite markers** on this page by design.

Debate-map axis statuses (real, from `docs/baseline_step6_status_debate_map_20260703T0954Z/artifacts/status_debate_map.json`):

| axis | status | plain-English trust |
|---|---|---|
| mechanism_ejective_feedback | `widely_supported` | Strong — mechanism is real in selected systems |
| alternatives_countercases | `widely_supported` | Strong — non-AGN channels are established |
| outflow_prevalence_frequency | `emerging_sample_limited` | Emerging — sample/tracer/redshift dependent |
| dominance_debate | `actively_debated` | Contested — no settled ordering |
| reservoir_response | `actively_debated` | Contested — mixed reservoir evidence |
| maintenance_heating_prevention | `contradicted_or_model_dependent` | Model-dependent — not observationally settled here |
| simulation_model_scope | `contradicted_or_model_dependent` | Model-dependent — tests mechanisms, not prevalence |

Baseline caveat (carried): `status_debate_map.json` status is `FINAL_DRAFT_PATCHED_AFTER_GORU_BLOCKER_PENDING_RECHECK` — the debate map is a patched final draft pending recheck; any stronger (P3) binding must resolve or re-scope this first.

Local source ledgers referenced (read-only, not web-served — cited by path):
- `docs/hwao_overnight_pinning_atlas_20260705T153533Z/evidence_source_inventory.json` (397 rows / 203 sources; claim_id + source_id/arXiv)
- `docs/hwao_debate_map_refresh_20260706T002104Z/debate_map_data.json` (7 axes, atlas section trust_level_counts)
- `docs/baseline_step6_status_debate_map_20260703T0954Z/artifacts/status_debate_map.json` (axis statuses, ledger)
- Full per-section provenance authored by Lana: `.hermes/handoffs/galaxy-evolution/method3/reviews/LANA_M3_P2_WIKI_PAGE_AUTHOR_20260707T050500Z.md` §6

All IDs below are **real** IDs already present in those local artifacts (verified by Kun's P2 repro rerun). None are invented. Product binding is deferred to P3.

---

## Per-section evidence basis + trust level

### §1 Overview: Regulated Baryon Cycle {#s1}
- Trust: **Framing** — rests on the widely-supported `alternatives_countercases` axis (multi-channel account).
- Local basis: axis `alternatives_countercases` (ledger `clc_agn_007_alternative_quenching_channels`); claim `2931` (quenching jointly regulated by internal + environment). Regulated-baryon-cycle framing from `debate_map_data.json`.

### §2 Dark Matter Halos & Structure Formation {#s2}
- Trust: **Scoped coverage-extension** (halo-mass/assembly). Halo-vs-central predictor debate is **OPEN**; broad structure-formation intentionally out of scope.
- Local basis: claims `2572, 2557, 2573, 2233, 2570, 2912, 2338`; sources `2512.16290v1, 2401.12953, 2508.11846v3, 1804.07798v2` (atlas: *Physical Mechanisms*, trust_level_counts accepted 4 / challenged 3 / reported 7 / unverified 16).

### §3 Gas Supply, Star Formation & Feedback {#s3}
- Trust: **Reservoir response — actively debated**; alternatives — widely supported.
- Local basis: axis `reservoir_response` (ledger `clc_agn_005_gas_retention_low_sfe_qualifier`, `clc_agn_006_central_kpc_depletion_local_qualifier`); claims `2905, 2906, 2909, 2911, 2907, 2930`.

### §4 AGN Feedback & Quenching {#s4}
- Trust (multi-axis): Mechanism **widely supported** · Outflow prevalence **emerging/sample-limited** · Dominance **actively debated** · Maintenance heating **model-dependent**.
- Local basis: focus_claim `2929`; axes `mechanism_ejective_feedback` (`clc_agn_001…`, `clc_agn2299_001…`), `outflow_prevalence_frequency` (`clc_agn_002…`, `clc_agn_002a_mosdef_17pct_ionized_outflows`, `clc_agn_002b_jwst_46pct_neutral_naid_outflows`), `maintenance_heating_prevention` (`clc_agn_004…`, `clc_agn_011…`), `dominance_debate` (`clc_agn2299_003…`, `clc_agn_009…`, `clc_agn_010…`); central-observable claims `2917, 2924`. Atlas *AGN Feedback & Quenching*: accepted 2 / debated 3 / reported 2 / unverified 1.
- **Unmatched (P3 repair needed):** v1709-body-only claim IDs `2915, 2921, 2913` present in the served page body but not in the atlas snapshot — re-resolve against a fresh P3 snapshot before binding.

### §5 Environment, Morphology & Structural Growth {#s5}
- Trust: Environment **supported**; morphology/structural growth **scoped coverage-extension**. Atlas *Environment, Morphology & Structural Growth*: consensus 1 / debated 4.
- Local basis: axis `alternatives_countercases` (`clc_agn_010_halo_environment_satellite_axis`); morphology claims `2130, 2580, 2133`; sources `2605.16505, 2604.03503, 2512.16290v1`; environment claims `2934, 2914, 2936, 2908, 2932, 2933, 2935`; merger claims `2922, 2923`.
- **Unmatched (P3 repair needed):** claim `2133` (SMBH growth ↔ host-galaxy assembly) resolves, but its true source `2605.22497` is not in the listed set — add `2605.22497` or restrict the sentence before any binding.

### §6 Chemical Enrichment & Cosmic Timing {#s6}
- Trust: **Scoped coverage-extension** (MZR/FMR, z ~ 0–2.3). No product binding.
- Local basis: claims `2731, 2725, 2738, 2426, 2427, 2656, 2728, 2253, 2338, 2227, 2579, 2580, 2234`; sources `2512.16989v1` (AURORA), `2606.11345` (JADES), `2606.05284, 2605.29623, 2605.25557, 2605.27555, 2604.03503, 2605.13966`.

### §7 High-Redshift & Reionization Frontier {#s7}
- Trust: Cosmic noon **sample/model-dependent**; reionization **OPEN frontier debates**. Atlas *Open Questions & Frontier Debates*: accepted 3 / challenged 2 / debated 1 / reported 4 / unverified 59 (frontier-heavy).
- Local basis: claims `2836, 2798, 2736, 2754, 2735, 2698, 2812, 2811, 2805, 2619, 2618, 2625, 2235`; sources `2606.05323, 2605.24112` (Lumina), `2605.26209, 2604.13866, 2606.02738, 2512.16981v1, 2605.20698`.
- **Unmatched (P3 repair needed):** claim `2374` (EoR quasar/SMBH seeding) has garbled `claim_text` in the inventory and does not support the seeding clause — find a correct row or drop the clause before binding. Cold-gas-reservoir part (claim `2235`) is supported.

### §8 Observational Evidence & Surveys {#s8}
- Trust: **Evidence framing**; simulations **model-dependent**; specific survey/instrument enumeration **deferred to P3**.
- Local basis: axis `simulation_model_scope` (`clc_agn_011_simulations_model_dependent_support`). Multi-wavelength/facility text is unmarked synthesis prose (as in the live page), not a sourced claim.

### §9 Synthesis & Open Tensions {#s9}
- Trust: **Synthesis across all 7 axes**; open tensions rest on `outflow_prevalence_frequency`, `dominance_debate`, `reservoir_response`, `maintenance_heating_prevention`.
- Local basis: all 7 axes; no new sources.

---

## Binding status (honest)

- Product claim markers on the page: **0**. Product cite markers: **0**. This is correct for M3's docs-only P2 scope — the page is a narrative synthesis, not a bound evidence graph.
- The IDs above are **local provenance**, resolvable in the named local ledgers, **unbound to product cite IDs**. Turning them into product `<!--claim:ID-->`/`<!--cite:ID-->` chips is the **P3 gate** and requires: a fresh authorized snapshot + Goru structural re-check + separate user approval, plus resolving the three Unmatched items above (`2915/2921/2913`, `2133→2605.22497`, `2374`) and the `PENDING_RECHECK` baseline caveat.
- Nothing here invents evidence, cite IDs, claim IDs, source IDs, DOI/ADS links, or trust levels.

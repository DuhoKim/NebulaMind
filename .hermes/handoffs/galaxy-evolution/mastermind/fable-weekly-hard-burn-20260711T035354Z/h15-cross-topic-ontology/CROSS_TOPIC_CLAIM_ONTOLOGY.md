FABLE_HARD_BURN_H15_ONTOLOGY_20260711T035354Z

# Cross-topic claim ontology, debate graph, and research-program sequencing

Burn `fable-weekly-hard-burn-20260711T035354Z` · lane H15 · written 2026-07-11 ≈04:36Z.
Inputs: seven topic artifacts (H5 sources-snapshot), cycle-5 supplement + flagship tex, P1 invariant manifest / RCA / receipt — **all 15 pinned sha256 recomputed OK before reading** (custody table in `H15_RECEIPT.md`).
Machine-readable graph: `CLAIM_GRAPH.json` — **40 nodes, 19 edges (18 cross-prefix, 4 contradicts/tension)** (validated by `tools/validate_graph.py`). Stretch included: m3_p3 context node folded in; cycle-6/7 prose-drift effects annotated (notes T3/T4).

Prefixes: ENV=m1_rp2_environment_quenching, MH=m1_rp3_maintenance_heating, OUT=m2_p1_outflow_escape_recycling, JET=m2_p2_radio_jet_environment, TRA=m2_p3_feedback_transition_mass, CEN=m3_p1_multiphase_census, GAS=m3_p2_gas_depletion_efficiency, FLG=flagship, SUPG=supplement-global, SIM=m3_p3 (context), RCA=P1 drift findings. "SUP Lnn"/"FLAG Lnn" = line in the pinned cycle-5 tex. Grades: **A** direct artifact value · **B** derived/rounded (RCA nearest-round convention) · **C** interpretive · **X** unsupported (none asserted; one X-guard noted at SUPG-C02).

## 1. Claim ontology (34 topic claims + 2 global + 2 RCA nodes)

| id | type | grade | claim (values + units) | artifact field | prose | manifest | deps |
|---|---|---|---|---|---|---|---|
| ENV-C01 | measurement | A | high-density quartile low-sSFR fraction 0.2304 (3,456/15,000, se 0.0034); prose "0.230" | `high_density_quenched` | SUP L92 | covered; se add-cand. | — |
| ENV-C02 | measurement | A | low-density quartile 0.1807 (2,710/15,000, se 0.0031); prose "0.181" | `low_density_quenched` | SUP L92 | covered; se add-cand. | — |
| ENV-C03 | measurement | A | bootstrap high−low CI [0.0406, 0.0591]; prose "[0.041, 0.059]" | `high_minus_low_ci` | SUP L92 | covered | C01,C02 |
| ENV-C04 | measurement | A | LPM high-density coeff 0.0325±0.0037 at fixed logM+z; prose "0.032 +/- 0.004" (3.2 pp restatement = B) | `lpm_high_density_coeff/_se` | SUP L92 | covered | — |
| ENV-C05 | trend | B | density proxy adds quenched-fraction information beyond mass+z | bullets | SUP L92 | n/a | C03,C04 |
| ENV-C06 | interpretation | C | ranks are fiber-collision-biased projected proxies, not physical density | prose-only | SUP L13 | n/a | — |
| MH-C01 | measurement | A | massive subset (logM*≥10.8) n=9,298 | `massive_rows` | SUP L103 | covered | — |
| MH-C02 | measurement | A | massive low-sSFR subset n=5,695 | `massive_quenched_rows` | SUP L103 | covered | C01 |
| MH-C03 | measurement | A | massive AGN fraction 0.4299 (3,997/9,298, se 0.0051); prose "0.430" | `massive_agn_fraction` | SUP L103 | covered; k,se add-cand. | C01 |
| MH-C04 | measurement | A | massive low-sSFR AGN fraction 0.6074 (3,459/5,695, se 0.0065); prose "0.607" | `massive_quenched_agn_fraction` | SUP L103 | covered; k,se add-cand. | C02 |
| MH-C05 | interpretation | C | optical duty-cycle denominator only; BPT = radiative mode, cannot isolate jet mode; not heating-to-cooling | bullets+guard | SUP L103 | n/a | C03,C04 |
| OUT-C01 | measurement | A | high-excitation AGN 4,440/60,000 = 0.074 (se 0.0011) | `high_excitation_agn` | SUP L114 | covered | — |
| OUT-C02 | measurement | A | median log sSFR −11.53 (high-exc) vs −10.14 (all) [dex, catalog proxy] | `median_log_sSFR_*` | SUP L114 | covered | C01 |
| OUT-C03 | trend | B | high-exc subset shifted −1.39 dex in median sSFR (derived) | derived | SUP L114 impl. | add-cand. if promoted | C02 |
| OUT-C04 | interpretation | C | no escape/recycling measured; denominator for IFU follow-up | bullets | SUP L114 | n/a | C01 |
| JET-C01 | measurement | A | massive high-density AGN fraction 0.5086 (948/1,864, se 0.0116); prose "0.509" | `high_density_massive_agn` | SUP L125 | covered; k/n,se add-cand. | — |
| JET-C02 | measurement | A | massive low-density 0.3667 (1,007/2,746, se 0.0092); prose "0.367" | `low_density_massive_agn` | SUP L125 | covered; k/n,se add-cand. | — |
| JET-C03 | measurement | A | bootstrap high−low CI [0.112, 0.170] | `high_minus_low_ci` | SUP L125 | covered | C01,C02 |
| JET-C04 | trend | B | density proxy modulates massive-host AGN fraction (+0.11..0.17) | bullets | SUP L125 | n/a | C03 |
| JET-C05 | interpretation | C | no jet power / coupling efficiency measured | bullets | SUP L125 | n/a | — |
| TRA-C01 | measurement | A | quenched fraction by mass 0.0053→0.7292 over bins 8.0–9.5 … 11.0–12.5 | `quenched_fraction_by_mass` | SUP L136/L169 | endpoints covered | — |
| TRA-C02 | measurement | A | first bin with quenched fraction >0.5 = 11.0–12.5 | `transition_mass_bin_…gt_0p5` | SUP L136 | covered | C01 |
| TRA-C03 | measurement | A | AGN fraction peaks 0.5202 in 11.0–12.5; prose "0.520" | `peak_agn_fraction/_mass_bin` | SUP L136 | covered | — |
| TRA-C04 | interpretation | C | peak consistent with S/N≥3 selection bias; **not** a universal physical threshold | prose-only guard | SUP L136 | n/a | C02,C03 |
| TRA-C05 | trend | B | quenched fraction and AGN incidence co-rise with mass | both arrays | SUP L136 | n/a | C01,C03 |
| CEN-C01 | measurement | A | tracer prevalences on one 60k denominator: BPT 0.1358 (8,146) · [NII]/Hα 0.1916 (11,497) · [OIII]/Hβ 0.3170 (19,019) · low-sSFR+em 0.2068 (12,410) · red+em 0.4183 (25,096) | `tracer_prevalence` | SUP L147 | 0.136/0.418 covered; middle 3 + k add-cand. | — |
| CEN-C02 | measurement | B | widest/narrowest ratio 3.0808; prose "3.1" (derived+rounded) | `prevalence_ratio_…` | SUP L147 | covered | C01 |
| CEN-C03 | interpretation | C | tracer definition dominates prevalence → common-denominator census required | bullets | SUP L147 | n/a | C02 |
| GAS-C01 | measurement | A | massive transition/quenched denominator n=6,729 (note-specific baseline) | `massive_transition_quenched_rows` | SUP L158 | covered | — |
| GAS-C02 | measurement | A | its AGN fraction 0.5487 (3,692/6,729, se 0.0061); prose "0.549" | `agn_fraction_in_denominator` | SUP L158 | covered; k,se add-cand. | C01 |
| GAS-C03 | measurement | A | median log L_Hα proxy 40.0612 (aperture-corrected galSpecExtra); prose "40.061" | `median_log_lha_denominator` | SUP L158 | covered | C01 |
| GAS-C04 | measurement | A | offset −0.6586 dex vs massive SF; prose "0.66 dex lower" | `median_log_lha_offset_vs_massive_sf` | SUP L158 | covered | C03 |
| GAS-C05 | interpretation | C | optics can't split depletion vs efficiency; 6,729 ≠ 5,695 (do not conflate); Kroupa-IMF scale must carry | bullets+guards | SUP L158 | n/a | C01 |
| FLG-C01 | measurement | A | matched AGN−SF median Δlog sSFR −1.309, 95% CI canon [−1.334,−1.283], 8,146 pairs / 60,000 cache | flagship artifact (custody 668ad7a6…) | FLAG L13/57/65/74 | covered incl. CI string | — |
| FLG-C02 | interpretation | C | association-only; fiber-centered; no morphology/aperture/halo/gas controls; not volume-complete | prose scope | FLAG L19–L36 | n/a | C01 |
| SUPG-C01 | interpretation | C | 55″ fiber-collision limit biases projected-neighbour stats; physical-density inference not defensible | prose | SUP L13 | n/a | — |
| SUPG-C02 | measurement | B | cache coverage 24.0% of strict parent; parent-count cascade **not promoted** without receipts (X-guard) | prose | SUP L13 | covered | — |
| SIM-C01 | measurement | A | 15 mass-z cells (n≥50); per-mass-bin quenched span 0.0053–0.7292, AGN span 0.0027–0.5202; prose "0.005-0.729 / 0.003-0.520" | `target_vector_cells`, `*_range` | SUP L169, L185–190 | covered (cycle-5 rendering) | — |
| RCA-C01 | measurement | A | raw CI upper −1.2821399375 nearest-rounds −1.282; cycles 6/7 carry [−1.334,−1.282] vs canon [−1.334,−1.283] (audit blocker D1) | RCA §2.1; P1 items 1/4/7 | RCA | canon = manifest entry | — |
| RCA-C02 | measurement | A | cycle-6 L169 spans → cell-level 0.001–0.856/0.001–0.610 (referent change); cycle-7 L188 2.830→2.831 | P1 items 2/3 (D2/D3) | P1 receipt L45–47 | 2.830 covered | — |

No X-grade claims were needed: every numeric claim in the seven supplement passages traces to its artifact value under the RCA nearest-round convention (this is a de-facto value-level pass of the seven artifacts vs prose — the formal registration remains P1 queue item 6, GATED).

## 2. Debate graph — adjudication notes for every contradicts/tension edge

Edge kinds: supports / contradicts / requires / refines; full edge list with evidence strings in `CLAIM_GRAPH.json`.

**T1 · TRA-C04 contradicts TRA-C02 (physical-transition reading) — the sharpest science tension.**
Side A (artifact bullets, m2_p3): "first stellar-mass bin with quenched fraction above 0.5 is 11.0–12.5", AGN peak 0.520 → reads as a transition-mass detection. Side B (prose guard, SUP L136): the peak "is consistent with a selection-function bias: the S/N≥3 cut preferentially removes truly passive, massive galaxies… must not be interpreted as a universal physical threshold." Values: quenched-by-mass 0.0053/0.0258/0.1312/0.3925/0.7292; AGN-by-mass 0.0027/0.0138/0.0773/0.2603/0.5202. Offline-settleable: partially — SIM-C01's 15 cells (SUP L185–190) show the co-rise persists in every z slice, but cannot remove the S/N cut. Settles it: a re-run with relaxed/no line-S/N cut plus a photometric-only passive fraction (**GATED**, RS-3 below).

**T2 · GAS-C05 contradicts MH-C02 (denominator conflation).**
Side A: MH "massive low-sSFR" n=5,695 (logM*≥10.8, pilot threshold; SUP L103). Side B: GAS "massive transition/quenched" n=6,729 (note-specific low-sSFR baseline; SUP L158). Both A-grade and both called "massive quenched" colloquially — a reader merging them gets contradictory AGN fractions (0.607 vs 0.549). The supplement already adjudicates: "should not be conflated" (L158). Offline evidence: definitions differ by construction; fully settleable offline only at doc level. Quantitative closure (set overlap / threshold table from the shared 60k CSV) needs a runner pass (**GATED**, RS-1).

**T3 · RCA-C01 contradicts FLG-C01 (canon vs artifact-nearest rounding) — pipeline tension, stretch annotation.**
Side A: cycle-5 canon + manifest CI string `[-1.334,-1.283]` (FLAG L13/57/65/74). Side B: raw artifact upper bound −1.2821399375 → nearest-round −1.282; cycles 6/7 both render `[-1.334,-1.282]` and fail the audit. Offline evidence already complete (P1/RCA custody-verified). What remains is a *decision*, not evidence: canon adjudication of −1.283 vs −1.282 (and 2.830 vs 2.831) with manuscript+audit-list+manifest updated atomically — P1 queue item 2 (**GATED**). Cycle-6/7 effect on graph: until adjudicated, any cycle-6/7-based prose would flip this edge's direction (weaken FLG-C01's A-grade rendering) while leaving all seven topic-claim edges untouched — D1 is confined to the flagship CI string.

**T4 · RCA-C02 contradicts SIM-C01 (referent change) — stretch annotation.**
Side A: cycle-5 L169 spans 0.005–0.729/0.003–0.520 = per-mass-bin extremes (matches `quenched_fraction_range`/`agn_fraction_range` exactly). Side B: cycle-6 rewrote them as cell-level extremes 0.001–0.856/0.001–0.610 (also derivable from `target_vector_cells`, e.g. 0.856=11.0–12.5@z0.02–0.05). Both numerically correct — the *claim referent* changed, which the audit cannot see. Settle offline: pick one referent and register both span strings in the manifest with `allowed_context` (add-candidate; registration via P1 item 1/3 pipeline, **GATED**). Cycle-6/7 effect: cycle-6 prose would silently weaken the SIM-C01→TRA-C01 supports edge (endpoints would no longer be per-bin extremes); cycle-7's L188 2.830→2.831 weakens only the SIM table rendering, no topic edge.

**Near-tension (kept as refines, not contradicts): OUT-C03 vs FLG-C01.** −1.39 dex (unmatched high-excitation) vs −1.309 dex (mass+z-matched) — consistent once matching is accounted for; the 0.08 dex gap *quantifies confounding absorbed by matching*. Offline-documentable now; exact matched-subset value for the high-excitation subset needs a runner pass (**GATED**, RS-5).

**Load-bearing supports edge: CEN-C01 → FLG-C01.** CEN's BPT tracer count k=8,146 equals the flagship's matched-pair count 8,146 (custody CSV rows, RCA §1) — two documents, one selection, independent renderings agree.

**Cross-cutting refines: CEN-C02 → {MH-C03, JET-C01, TRA-C03, GAS-C02}.** Every "AGN fraction" in the atlas is conditional on the broad-BPT definition; CEN's ×3.08 tracer spread is the measured size of that conditionality. This is the single highest-leverage caveat in the corpus.

## 3. Research-program sequencing (science track; DAG as ordered list)

Complements — does **not** duplicate — the P1 receipt follow-up queue items 1–6 (all GATED: manifest→pre-audit integration; canon rounding adjudication; audit invariant-list extension; verbatim-carry prompt patch; EXT-1..4 literature slots; formal value-verification registration). That queue is the invariant/canon pipeline track; below is the science-topic track. Every runner/network/DB action is **GATED** for Duho.

| # | step | prereqs | gate | evidence value / effort |
|---|---|---|---|---|
| RS-0 | This ontology + graph (offline) | — | none — **done here** | anchors all later steps |
| RS-1 | Denominator overlap audit: cross-tab membership of 5,695 (MH) × 6,729 (GAS) × 4,440 (OUT) × 8,146 (CEN-BPT) from the shared 60k CSV; publish threshold table | RS-0 | **GATED** (runner, minutes) | highest — one tiny join resolves T2 quantitatively and hardens 4 nodes |
| RS-2 | Tracer-sensitivity bands: recompute MH-C03/04, JET-C01/02, TRA-C03, GAS-C02 under all five CEN tracer definitions; report fraction bands instead of point values | RS-0 | **GATED** (runner, small) | high — converts the 4 cross-cutting refines edges into quantified bands; de-risks every AGN-fraction claim before external joins |
| RS-3 | Selection-bias probe for the transition mass: re-bin quenched/AGN fractions with relaxed line-S/N and a photometric-only passive definition | RS-0 (RS-2 helpful) | **GATED** (runner, small) | high — adjudicates T1, the sharpest science tension |
| RS-4 | Density-proxy robustness for ENV+JET jointly: vary neighbour rank k and quartile edges; fiber-collision down-weighting experiment; one shared stratification for both topics | RS-0 | **GATED** (runner, small) | medium-high — two topics share one systematic (SUPG-C01); fixes it once |
| RS-5 | sSFR-offset concordance memo: reconcile −1.309 (matched FLG), −1.39 (unmatched OUT), −0.66 dex L_Hα (GAS) incl. matched high-excitation subset | RS-1 | memo offline; matched recompute **GATED** | medium — one coherent SF-suppression story across three topics |
| RS-6 | External joins, ranked by A-claim leverage: (a) CO/HI on the 6,729 GAS denominator; (b) radio/X-ray on the 5,695 MH subset (duty cycle 0.607 is the strongest prior); (c) group/halo catalogs for ENV+JET (also retires SUPG-C01); (d) IFU kinematics on the 4,440 OUT subset | RS-1..4 | **GATED** (network/DB/proposals) | the actual physics; sequenced last because RS-1..4 de-risk target selection at near-zero cost |
| RS-7 | Freeze SIM forward-modeling target vector (referent fixed per T4, definitions per RS-2, bias bounds per RS-3); hand to simulation-comparison work | RS-2, RS-3 + P1 items 1–3 | **GATED** | medium — publishable validation vector once inputs stabilize |

Ordering logic: RS-1→RS-4 are cheap runner passes on data already in custody that convert this graph's tensions and refines edges into closed, quantified statements; only then do the expensive external joins (RS-6) spend effort on hardened targets. The P1 canon-track items 1–3 should land before RS-7 so the frozen vector inherits an adjudicated rounding convention.

— end · FABLE_HARD_BURN_H15_ONTOLOGY_20260711T035354Z

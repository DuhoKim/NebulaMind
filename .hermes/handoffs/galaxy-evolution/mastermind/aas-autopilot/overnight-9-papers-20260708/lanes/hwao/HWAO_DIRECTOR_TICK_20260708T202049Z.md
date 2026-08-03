# Hwao/Fable director tick — overnight 9-paper board

Marker: `HWAO_DIRECTOR_TICK_20260708T202049Z`

UTC: 2026-07-08T20:20:49Z  
Local: 2026-07-09 05:20:49 KST

## Scope of this tick

I coordinated the overnight 9-paper board only. I read the required brief, swarm board, ledger, latest durable lane artifacts, and newest visible-pane reports. I did not edit manuscripts, PDFs, public pages, live roots, product DB/API, page_versions, trust, deploy/restart, git, billing/OAuth, external submissions, or cron jobs.

This is a director integration/prioritization report. It does **not** authorize public/wiki publishing, replacing currently linked PDFs, or treating lane-local revisions as accepted manuscripts.

## New board state since the 18:14 Hwao tick

- **Tori completed the RP-1 robustness/selection revision** at `lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/`: a lane-local compiled PDF with selection-function disclosure, BPT/S/N robustness, Wave-3 source guardrails, and safer association-only language. Original public-linked RP-1 hash was reported unchanged.
- **Lana completed Wave-1 selection/definition cleanup** for **M1 RP-2**, **M1 RP-3**, and **M2 P1** at `lanes/lana/lana_revision_manifest_20260708T182812Z.json`: exact `specsfr_tot_p50 < -11.0` low-sSFR/quenched threshold, massive cut `lgm_tot_p50 >= 10.8`, exact high-excitation criterion `bpt_label == agn` and `log_oiii_hb > 0.25`, and explicit selection-function demotions.
- **Goru produced regression/bin-sensitivity artifacts** at `lanes/goru/artifacts/goru_regression_bin_sensitivity_20260708T183643Z.json`: regression rows, alternate target-vector cells, bootstrap summary, and paper-table candidates. Key values remain proxy-only: RP-1 matched median offset -1.309 dex, RP-2 high-minus-low density quenched fraction +0.0497, M2 P2 high-minus-low density optical-AGN fraction +0.1419, and M3 P3 15 usable target-vector cells.
- **Kun found no reproducibility blocker** in `lanes/kun/artifacts/kun_repro_audit_20260708T184538Z.json`; the durable audit reports 0 blockers, 49/49 PDF magic OK, 43/43 expected PDF hashes/bytes matched, 27 compile-ish logs with 0 fatal markers, and source rows 60,000/60,000/8,146.
- **Literature/source completed Wave-1 citation-placement review** for **M1 RP-2**, **M1 RP-3**, and **M2 P1** at `lanes/literature/literature_citation_placement_wave1_20260708T185345Z.md`: 19 paper-source associations, 17 unique arXiv/Semantic Scholar-backed sources, and explicit actual-method vs future-data guards.
- **External Codex visible review** at `visible-panes/external/reports/external_20260708T193834Z.md` delivered a sharper global critique: only RP-1 is close to a serious short paper; the other eight are better framed as a single SDSS optical proxy/denominator suite or appendices unless more data are added. It also flagged the shared capped denominator, star-forming-control tautology, sSFR estimator mismatch, emission-line quiescent-population exclusion, missing data dictionary, and over-physical titles.
- **Tori completed selection/CI revisions for M2 P3 and M3 P1** at `lanes/tori/revision-drafts/m2p3_m3p1_selection_ci/20260708T193507Z/`: 2 lane-local compiled PDFs, M2 P3 mass/redshift Wilson tables, M3 P1 tracer-threshold Wilson table, and 7-row selection disclosure.
- **Visible-pane monitor status:** Tori/Goru/Kun reports produced normal monitor summaries. Visible Lana, Literature, and Hwao Claude reviews reached max turns and wrote only short nonzero-exit reports; I treat those as no-new-output, not as scientific blockers. The durable lane artifacts above remain the usable evidence.

## Independent verification snapshot

I independently checked markers, JSON/JSONL counts, PDF magic/SHA entries, row counts, and safety statements before integrating lane output into priorities:

```text
DIRECTOR_VERIFY_20260708T201822Z
active_consolidated_slugs=9 duplicate_active_slugs=[]
lana_161724: marker=LANA_MANUSCRIPT_TICK_20260708T161724Z; slugs=[m2_p2_radio_jet_environment, m3_p2_gas_depletion_efficiency, m3_p3_simulation_validation]; pdf_magic=3/3; compile0=3/3; fatal_empty=3/3; sha_match=3/3
lana_182812: marker=LANA_MANUSCRIPT_TICK_20260708T182812Z; slugs=[m1_rp2_environment_quenching, m1_rp3_maintenance_heating, m2_p1_outflow_escape_recycling]; pdf_magic=3/3; compile0=3/3; fatal_empty=3/3; sha_match=3/3
tori_rp1_181833: marker=RP1_ROBUSTNESS_SELECTION_REVISION_20260708T181833Z; pdf_magic=1/1; compile0=1/1; fatal_empty=1/1; sha_match=1/1
tori_m2p3_m3p1_193507: marker=TORI_M2P3_M3P1_SELECTION_CI_REVISION_20260708T193507Z; slugs=[m2_p3_feedback_transition_mass, m3_p1_multiphase_census]; pdf_magic=2/2; compile0=2/2; fatal_empty=2/2; sha_match=2/2
tori_original_public_linked_pdf_checks=2/2 matched+pdf_magic
literature_jsonl_rows: wave1_source=21, wave2=12, wave3=17, wave1_citation_placement=19; duplicate_keys_within_each_packet=0
literature_summary_counts: wave2_records=12; wave3_records=17; wave1_citation_records=19; wave1_citation_unique_sources=17; duplicate_record_keys=[]
literature_wave3_availability: ADS abstract/arXiv-from-identifiers/bibcode/identifier/authors/DOI/year = 17/17 each; duplicate_dedupe_keys=[]
goru_source_rows=60000; S/N>=3/5/10 = 60000/42446/22311; row_counts regression/alternate-target/bootstrap/table-candidates = 63/198/84/35
selection_attrition: strict SDSS four-line S/N>=3 rows=249,917; cached rows=60,000; cached coverage=0.24007970646254556
Tori M2P3/M3P1 tables: M2P3 mass rows=5, z rows=15; M3P1 tracer rows=15; selection-stage rows=7
Kun blockers=0
```

The verification script performed read-only checks and wrote no files.

## Director verdict

The board is scientifically stronger than at 18:14, but the correct morning posture should be conservative:

1. **Do not present nine independent evidence-weight papers as ready.** The external critique is right: the overnight work has produced one plausible flagship sprint candidate (**M1 RP-1**) plus eight lane-local denominator/proxy/target-vector drafts built from the same capped SDSS emission-line sample.
2. **Treat the shared selection function as the central scientific dependency.** Every active paper must front-load the 249,917 strict eligible rows, 60,000 cached `TOP 60000` rows, 24.0% coverage, `ORDER BY specObjID`/row-cap caveat, four-line S/N selection, and sSFR-dependent retention.
3. **Treat title/framing demotion as a requirement, not polish.** Maintenance heating, escape/recycling, radio-jet coupling, gas depletion/SFE, multiphase census, feedback transition, and simulation validation are not measured by the current SDSS optical-only pilots.
4. **Use sources as method/status/future-data guards.** The source packets are now adequate for local citation-placement review across all active 9, but they do not authorize public prose or causal claims.

## Next most valuable paper-writing priorities

1. **RP-1 serious sprint first.** Keep M1 RP-1 as the flagship, but add the missing caveats external review identified: star-forming-control tautology, MPA/JHU-style sSFR estimator mismatch, all-galaxy/quiescent control arms where possible, control-reuse diagnostics, common-support/caliper diagnostics, and nonlinear mass-redshift sensitivity. The headline should be “BPT optical AGN hosts lie below BPT star-forming controls in catalog sSFR,” not feedback suppression.
2. **Build a shared local “Parent Sample and Selection Function” module + data dictionary.** This should precede any local merge. It must define BPT labels, line S/N, density proxy, `specsfr_tot_p50` thresholds, high-excitation criterion, low-sSFR/quenched flags, mass cuts, row-cap ordering, and exactly which statements are emission-line-selected only.
3. **Consolidate lane-local drafts, not public-linked PDFs.** Next integration pass should assemble local consolidated drafts under a separate integration/revision root only, using Lana/Tori drafts as inputs and then asking Kun to compile/hash. No live/public replacement.
4. **Finish citation placement for Wave-2 and Wave-3 papers.** Wave-1 citation-placement now exists; repeat the same source-role discipline for **M2 P2/M3 P2/M3 P3** and **RP-1/M2 P3/M3 P1**, without more broad source harvesting unless a named gap appears.
5. **Prepare a morning architecture recommendation.** Recommend either (a) one flagship RP-1 paper plus an “SDSS optical proxy denominator suite” companion/appendix, or (b) nine internal drafts explicitly labeled as pilot denominators, not nine ready AAS submissions.

## Paper-by-paper board

| Active consolidated paper | Current lane-local state | Dependencies / blockers | Director next action |
|---|---|---|---|
| **M1 RP-1 — SDSS AGN/sSFR matched-control pilot** | Tori RP-1 robustness/selection revision compiled; Wave-3 ADS/arXiv sources exist; Goru S/N/BPT sensitivity available. | Star-forming-control tautology, sSFR estimator mismatch, missing all-galaxy/quiescent controls, and four-line selection bias remain major caveats. | Highest priority: flagship local rewrite with front-page selection module, control diagnostics, estimator caveat, and association-only wording. |
| **M1 RP-2 — SDSS density proxy for environmental quenching** | Lana 18:28 revision compiled with exact `specsfr_tot_p50 < -11.0`, density-proxy explanation, and Wave-1 citation-placement. | Density proxy is not halo/group/central-satellite environment; edge/fiber/mask caveats remain. | Integrate as “nearest-neighbour density proxy in an emission-line selected sample”; do not imply environmental causality. |
| **M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up** | Lana 18:28 revision compiled with massive/low-sSFR cuts and future-only radio/X-ray/cavity context. | No cooling luminosity, cavity power, jet power, hot gas, or duty-cycle balance. | Keep as optical BPT-AGN target-selection denominator for future maintenance-heating data, not a heating paper. |
| **M2 P1 — high-excitation optical-AGN denominator for outflow escape/recycling tests** | Lana 18:28 revision compiled with exact high-excitation criterion and candidate-definition/S/N tables. | No outflow velocities, escape speeds, gas phases, CGM/recycling tracer, or escape fraction. | Local integration can proceed after selection module; title/framing must say high-excitation optical denominator only. |
| **M2 P2 — environment proxy for optical AGN in massive hosts** | Lana 16:17 revision compiled; Goru reports high-minus-low density optical-AGN fraction +0.1419 for massive hosts; Wave-2 sources exist. | No radio crossmatch, jet powers, cavities, or coupling efficiency. | Reframe as “optical AGN versus density proxy in massive hosts”; next citation-placement should use radio literature only as future-data guard. |
| **M2 P3 — mass transition in quenching and optical AGN incidence** | Tori 19:35 selection/CI revision compiled with 5 mass rows and 15 redshift rows; Wave-3 ADS/arXiv sources exist. | Cannot separate stellar, halo, environment, black-hole, or AGN feedback from SDSS optical mass-bin trends. | Treat as observed mass-bin optical/quenching diagnostic; integrate redshift-stratified intervals and suppress “feedback transition” attribution. |
| **M3 P1 — common-denominator optical tracer census** | Tori 19:35 selection/CI revision compiled with 15 tracer-threshold rows; Wave-3 sources exist. | Not multiphase: no CO/HI/Na I/X-ray/radio/kinematic denominator. | Rename/reframe as optical tracer-threshold census; cite multiphase literature only as missing-observable context. |
| **M3 P2 — optical denominator for gas-fraction versus efficiency tests** | Lana 16:17 revision compiled with default 121,533/40,797/10,270 and strict 33,125/11,288/2,941 denominator counts; Wave-2 sources exist. | Scientifically weakest as titled: Hα/four-line SDSS cannot distinguish gas mass, gas fraction, depletion time, or SFE. | Keep only as CO/HI follow-up target-selection denominator; no gas-depletion/SFE interpretation. |
| **M3 P3 — SDSS target vector for feedback-model validation** | Lana 16:17 revision compiled with selection-flagged target vector and small-cell cautions; Goru confirms 15 usable cells. | No simulation mocks or forward-model comparison; target vector is not validation. | Integrate as observed SDSS target vector with machine-readable table/covariance wishlist; no validate/reject/rank language. |

## Dependency ordering

1. **Selection module/data dictionary before any local merge.**
2. **RP-1 flagship rewrite before spending more time expanding the eight denominator drafts.**
3. **Citation-placement discipline before bibliography expansion.** Cite actual SDSS/BPT/catalog/method papers as method support; cite radio/X-ray/CO/multiphase/simulation papers only as future-data requirements unless the data exist.
4. **Kun compile/hash only after integration drafts are assembled.** Current lane-local PDFs are verified, but the canonical public-linked PDFs were intentionally not overwritten.
5. **Morning recommendation should separate “active 9 consolidated paper topics” from “ready independent papers.”** Active topic count remains 9; readiness count does not.

## Active 9 vs omitted historical candidate topics

The active overnight board remains exactly the **9 consolidated papers** listed in the brief and linked on the proposal-card pages. They do not exhaust historical candidate topics from earlier backups.

| Historical source | Covered by active 9 now | Omitted / future-extension material not to count as done tonight |
|---|---|---|
| **M1 original 8 topics** | RT-01 -> M1 RP-1; RT-02 -> M1 RP-2; RT-03 -> M1 RP-3. | RT-04 through RT-08 remain methods/evidence-accounting topics: unbound claims, evidence-empty sections, malformed links, dedup/provenance, and trust-promotion limits. |
| **M2 original 10 topics** | T8/T9 -> M2 P3 and M2 P1; T4 -> M2 P2; T2 partly informs M2 P1/M3 P1; T3 folded into M1 RP-3. | T1/T7/T10 traceability/full-text/rejected-position methods work; T5/T6 M51/positive-feedback future extensions. |
| **M3 original 9 topics** | t2 -> M3 P1; t4 -> M3 P2; t6 -> M3 P3; t3 partly informs M1 RP-1. | t5 maintenance-heating folded into M1 RP-3; t7 non-AGN quenching completeness; t8 halos/morphology/chemical/reionization gaps; t9 provenance repair. |

## Safety ledger

This Hwao tick wrote only this report under `lanes/hwao/` and appends one concise line to `OVERNIGHT_LEDGER.md`. No public pages, live roots, product DB/API, page_versions, trust, deploy/restart, git, billing/OAuth, external submission, or new cron jobs were touched. No active execution phrase.

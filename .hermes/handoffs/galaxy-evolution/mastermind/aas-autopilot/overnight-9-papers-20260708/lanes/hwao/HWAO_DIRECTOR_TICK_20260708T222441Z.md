# Hwao/Fable director tick — overnight 9-paper board

Marker: `HWAO_DIRECTOR_TICK_20260708T222441Z`

UTC: 2026-07-08T22:24:41Z  
Local: 2026-07-09 07:24:41 KST

## Scope of this tick

I coordinated the overnight 9-paper board only. I read the required `OVERNIGHT_BRIEF.md`, `SWARM_BOARD.md`, current `OVERNIGHT_LEDGER.md`, the latest durable lane outputs, and the latest visible-pane reports. I did not edit manuscripts, PDFs, public pages, live roots, product DB/API, page_versions, trust, deploy/restart, git, billing/OAuth, external submissions, or cron jobs.

This is a director integration/prioritization report. It does **not** authorize public/wiki publishing, replacing currently linked PDFs, or treating lane-local revisions as accepted manuscripts.

## New board state since the 20:20 Hwao tick

- **Lana Wave-3/morning-priority revisions succeeded** at `lanes/lana/lana_wave3_revision_manifest_20260708T204532Z.json`: 3 lane-local PDFs for **M1 RP-1**, **M2 P3**, and **M3 P1** compiled with `%PDF` magic, matching bytes/SHA, exit code 0, and no fatal markers. Lana added RP-1 control-baseline brackets, common-support/reuse diagnostics, and claim/use contracts for the M2 P3/M3 P1 denominator-style drafts.
- **Tori built the shared parent-sample and selection-function module** at `lanes/tori/shared-selection-module/20260708T204717Z/`: data dictionary, paper-use contracts, selection-stage counts, sSFR-retention table, and a smoke-tested AASTeX fragment. It locks in the cross-paper denominator disclosure: 249,917 strict public four-line S/N>=3 rows, 60,000 cached rows, 24.0% coverage, BPT counts 39,553/12,234/8,146/67, and high-excitation optical AGN count 4,440.
- **Goru completed matched-control robustness** at `lanes/goru/artifacts/goru_matching_control_robustness_20260708T205859Z.json`: RP-1 baseline matched median offset -1.309 dex; moderate mass/z caliper keeps 7,867/8,146 targets with median -1.318 dex; greedy no-replacement covers 7,419/8,146 with median -1.446 dex but is explicitly not globally optimal; M2 P1 high-excitation target/control row covers 4,440/4,440 with median -1.136 dex. These remain optical emission-line/sSFR associations only.
- **Kun found no current integrity blocker** in `lanes/kun/artifacts/kun_repro_audit_20260708T210837Z.json`: blockers `[]`, 67/67 PDFs with PDF magic, 53 expected PDF hashes/bytes matched, 9/9 primary PDFs present, 48 compile-ish logs with 0 current fatal markers, 89/89 JSON parse OK, 25/25 scripts syntax OK, and source rows 60,000/60,000/8,146.
- **Literature Wave-2 citation-placement packet is complete** at `lanes/literature/literature_citation_placement_wave2_20260708T211901Z.md`: 20 arXiv/Semantic Scholar associations across 18 unique public sources, 0 duplicate record keys, and explicit actual-method versus future-data/model guards for **M2 P2**, **M3 P2**, and **M3 P3**. This is local citation-integration readiness only.
- **External review of Wave-2 revisions succeeded** at `lanes/external-cli/EXTERNAL_CLI_TICK_20260708T212455Z.md`: remaining blockers are selection-convolved fractions, SpecObjID-cap representativeness, M2 P2 density-method confounds, H-alpha proxy units/uncertainty conventions, M3 P3 small-cell intervals, and citation placement.
- **Tori answered the representativeness blocker** at `lanes/tori/cached-public-representativeness/20260708T220242Z/`: public SDSS marginals for strict parent N=249,917 versus cached N=60,000 show no bin over the 5 percentage-point flag threshold, but the cached sample remains non-random and row-capped. Largest cached-minus-public differences: redshift 0.080--0.120 +2.03 pp, stellar mass 8.0--9.5 -1.63 pp, sSFR -10.0---9.5 -0.58 pp.
- **Visible panes:** Kun/Goru/Tori visible monitors produced normal status reports; visible Lana/Literature/Hwao Claude reports hit max turns and added no durable scientific output. The large visible external Codex review repeats the same conservative posture: one plausible RP-1 flagship plus eight optical proxy/denominator drafts, not nine ready independent papers.

## Independent verification snapshot

I independently performed read-only checks of markers, paths, JSON/JSONL counts, PDF magic/SHA entries, and safety statements before integrating lane output into priorities:

```text
DIRECTOR_VERIFY_LATEST_READONLY
active_slugs_count=9 duplicates=[]
active_slugs=m1_rp1_sdss_agn_sfr,m1_rp2_environment_quenching,m1_rp3_maintenance_heating,m2_p1_outflow_escape_recycling,m2_p2_radio_jet_environment,m2_p3_feedback_transition_mass,m3_p1_multiphase_census,m3_p2_gas_depletion_efficiency,m3_p3_simulation_validation
lana_wave3_marker=LANA_WAVE3_FLAGSHIP_CONTROL_SUITE_REVISION_20260708T204532Z
lana_wave3_pdfs: m1_rp1/m2_p3/m3_p1 exists=True pdf_magic=True bytes_match=True sha_match=True compile_exit=0 fatal_markers=[]
shared_selection_contains marker, 60,000, 249,917, 24.0%, and 4,440=True
Goru matching marker=GORU_MATCHING_CONTROL_ROBUSTNESS_TICK_20260708T205859Z; rows control/reuse/paper-ready/inventory=90/6/9/9; S/N counts=60000/42446/22311
Goru key values: RP-1 baseline median=-1.308887, moderate caliper matched=7867/8146, M2 P1 high-excitation matched=4440/4440
Kun marker=KUN_REPRO_AUDIT_20260708T210837Z; blockers=[]
Literature Wave-2 marker=LITERATURE_WAVE2_CITATION_PLACEMENT_20260708T211901Z; records=20; unique_sources=18; duplicate_record_keys=[]; Semantic Scholar status=200
Representativeness marker=CACHED_PUBLIC_REPRESENTATIVENESS_20260708T220242Z; public_total=249917; cached_total=60000; coverage=0.2400797; flagged_bins=[]
External marker=EXTERNAL_CLI_REVIEW_TICK_20260708T212455Z; representativeness blocker mentioned=True
```

The verification was read-only and wrote no files.

## Director verdict

The overnight board is now in a usable **morning triage** state, not a final-paper state.

1. **Correct readiness posture:** active topic count remains 9, but readiness remains asymmetric: **M1 RP-1 is the only plausible flagship short-paper candidate**; the other eight should be framed as a shared SDSS optical proxy/denominator suite or appendices until non-SDSS observables are added.
2. **Central dependency is now available:** the shared selection-function/data-dictionary module and cached-vs-public representativeness packet should be mandatory inputs before any local integration run.
3. **Do not overread the representativeness repair:** the z/mass/sSFR marginal comparison found no >5 pp marginal discrepancy, but it does not make the cached table random, complete, spatially unbiased, or suitable for population-complete quiescent fractions.
4. **Literature status:** citation-placement packets now cover Wave-1 and Wave-2 high-risk papers and earlier source packets cover all active 9, but they are guardrails for local manuscripts, not evidence licenses for causal feedback, gas depletion, jet coupling, or simulation validation.
5. **No public action:** lane-local revisions and PDFs are verified artifacts for a later integration pass only. Public-linked PDFs stay unchanged.

## Next most valuable paper-writing priorities

1. **Morning integration plan first:** assemble a local integration-run plan, not a public replacement. Inputs should be the Lana/Tori lane-local drafts, shared selection module, representativeness packet, Goru robustness tables, and literature citation-placement packets.
2. **RP-1 flagship polish:** make RP-1 the serious short-paper candidate. Lead with the robustness range/control-baseline brackets, not only the -1.31 dex star-forming-control contrast. Explicitly discuss star-forming-control tautology, estimator-mode caveat, S/N sensitivity, control reuse/common support, caliper/no-replacement diagnostics, and association-only wording.
3. **Eight-paper denominator-suite consolidation:** if time remains, merge the eight non-RP1 drafts into either a single denominator-suite manuscript/appendix or eight clearly marked internal pilot notes. Every one needs the shared selection section before any fractions and title/abstract demotion from physical feedback claims.
4. **Patch Wave-2 scientific blockers next:** for M2 P2/M3 P2/M3 P3, insert the cached-vs-public representativeness paragraph/table, conditional-emission-line fraction warning, Wave-2 citations, M2 P2 density-method caveats, M3 P2 H-alpha proxy units/uncertainty labels, and M3 P3 visible small-cell intervals.
5. **Run Kun after any integration run:** compile/hash local integration PDFs only after the merge; do not overwrite public-linked PDFs without a separate explicit approval gate.
6. **Morning recommendation:** report “one flagship + denominator-suite/appendix” as the scientifically honest architecture unless the user explicitly asks for a different internal packaging.

## Paper-by-paper board

| Active consolidated paper | Current lane-local state | Dependencies / blockers | Director next action |
|---|---|---|---|
| **M1 RP-1 — SDSS AGN/sSFR matched-control pilot** | Strongest. Lana Wave-3 and Tori RP-1 robustness drafts compiled; Goru control-baseline/caliper/no-replacement diagnostics available; Wave-3 sources present. | Headline is sensitive to BPT-star-forming control choice; catalog sSFR estimator mode may differ by class; four-line selection and row cap remain limiting. | Treat as flagship short paper. Integrate shared selection, representativeness, control brackets, S/N sensitivity, reuse/common support, and association-only abstract. |
| **M1 RP-2 — SDSS density proxy for environmental quenching** | Lana Wave-1 cleanup compiled; Wave-1 citation placement exists; Goru density-proxy sensitivity available. | Density proxy is not halo/group/central-satellite environment; high-low quenched fraction remains descriptive only. | Keep as nearest-neighbour density association in an emission-line subset; use only guarded environment language. |
| **M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up** | Lana Wave-1 cleanup compiled with massive/low-sSFR cuts and future-only radio/X-ray/cavity context. | No cooling luminosity, cavity power, jet power, hot gas, or duty-cycle balance. | Treat as optical BPT-AGN target denominator for future radio/X-ray maintenance-heating work. |
| **M2 P1 — high-excitation optical AGN denominator for outflow escape/recycling tests** | Lana Wave-1 cleanup compiled; Goru high-excitation matched-control row covers 4,440/4,440; Wave-1 citations exist. | No resolved outflow velocity, escape speed, CGM/recycling tracer, or multiphase gas mass. | Integrate as high-excitation optical candidate pool only; cite wind/outflow literature only for missing future observables. |
| **M2 P2 — environment proxy for optical AGN in massive hosts** | Lana selection-disclosure revision compiled; Wave-2 citations exist; external review identified density-method confounds. | No radio jets; density proxy needs cosmology/redshift-space/edge/z-mass-balance caveats. | Next Wave-2 patch: representativeness table + conditional fraction warning + density-method caveats + guarded citations. |
| **M2 P3 — mass transition in quenching and optical AGN incidence** | Tori CI revision and Lana Wave-3 claim-contract revision compiled; Wave-3 sources exist. | Mass trends do not isolate stellar, halo, environment, black-hole, or AGN-feedback transitions. | Keep as mass-bin optical/quenching diagnostic with redshift-stratified intervals and no transition-cause claim. |
| **M3 P1 — common-denominator optical tracer census** | Tori CI revision and Lana Wave-3 threshold-contract revision compiled; Wave-3 sources exist. | Not multiphase; no CO/HI/Na I/X-ray/radio/kinematic observables. | Reframe as optical tracer-threshold census; cite multiphase literature only as missing-observable context. |
| **M3 P2 — optical denominator for gas-fraction versus efficiency tests** | Lana selection-disclosure revision compiled; Wave-2 citations exist; external review flags selection-convolved high BPT-AGN fractions. | No CO/HI/dust gas mass, depletion time, or SFE; H-alpha proxy units/corrections and uncertainty convention need explicit text. | Patch as CO/HI follow-up target denominator; add representativeness and conditional-emission-line fraction warning. |
| **M3 P3 — SDSS target vector for feedback-model validation** | Lana selection-disclosure revision compiled; Wave-2 simulation-future citations exist; Tori/Goru target-vector tables available. | No simulation mock or forward-model comparison; `f_Q` is conditional on emission-line detection; small cells need visible intervals. | Reframe as observed SDSS target vector for future forward modelling; no validate/reject/rank wording. |

## Dependency ordering

1. **Shared selection module + cached-vs-public representativeness packet before local merge.**
2. **RP-1 flagship integration before spending more effort making eight thin proxy drafts look independent.**
3. **Wave-2 blocker patch before any M2 P2/M3 P2/M3 P3 integration.**
4. **Citation placement before bibliography expansion:** method sources support actual SDSS/BPT/catalog choices; radio/X-ray/CO/outflow/simulation sources define missing future observables only.
5. **Kun compile/hash after integration drafts are assembled.** Current lane-local PDFs are verified but are not canonical replacements.
6. **Morning handoff must separate active-9 topic coverage from readiness.** Active count is 9; independent-ready-paper count is not 9.

## Active 9 vs omitted historical candidate topics

The active overnight board remains exactly the **9 consolidated papers** listed in the brief and linked on proposal-card pages. They do not exhaust historical candidate topics from earlier backups.

| Historical source | Covered by active 9 now | Omitted / future-extension material not to count as done tonight |
|---|---|---|
| **M1 original 8 topics** | RT-01 -> M1 RP-1; RT-02 -> M1 RP-2; RT-03 -> M1 RP-3. | RT-04 through RT-08 remain methods/evidence-accounting topics: unbound claims, evidence-empty sections, malformed links, dedup/provenance, and trust-promotion limits. |
| **M2 original 10 topics** | T8/T9 -> M2 P3 and M2 P1; T4 -> M2 P2; T2 partly informs M2 P1/M3 P1; T3 folded into M1 RP-3. | T1/T7/T10 traceability/full-text/rejected-position methods work; T5/T6 M51/positive-feedback future extensions. |
| **M3 original 9 topics** | t2 -> M3 P1; t4 -> M3 P2; t6 -> M3 P3; t3 partly informs M1 RP-1. | t5 maintenance-heating folded into M1 RP-3; t7 non-AGN quenching completeness; t8 halos/morphology/chemical/reionization gaps; t9 provenance repair. |

## Safety ledger

This Hwao tick wrote only this report under `lanes/hwao/` and appends one concise line to `OVERNIGHT_LEDGER.md`. No public pages, live roots, product DB/API, page_versions, trust, deploy/restart, git, billing/OAuth, external submission, or new cron jobs were touched. No active execution phrase.

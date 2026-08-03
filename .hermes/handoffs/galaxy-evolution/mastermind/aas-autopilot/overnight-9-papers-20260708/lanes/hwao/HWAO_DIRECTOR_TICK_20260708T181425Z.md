# Hwao/Fable director tick — overnight 9-paper board

Marker: `HWAO_DIRECTOR_TICK_20260708T181425Z`

UTC: 2026-07-08T18:14:25Z  
Local: 2026-07-09 03:14:25 KST

## Scope of this tick

I coordinated the overnight 9-paper board only. I read the required brief, swarm board, and ledger; then I read lane outputs now present from Lana, Goru, Kun, Literature/source, Tori, External CLI, and visible-pane monitor reports. I did not edit manuscripts, PDFs, public pages, live roots, product DB/API, page_versions, trust, deploy/restart, git, billing/OAuth, external submissions, or cron jobs.

This is a director integration/prioritization report. It does **not** authorize public/wiki publishing or replacing currently linked PDFs.

## New board state since the 16:08 Hwao tick

- **Lana completed the highest-risk Wave-2 selection-disclosure pass** for **M2 P2**, **M3 P2**, and **M3 P3**, writing three lane-local compiled PDFs with parent/S/N/cached denominator disclosure and safer framing.
- **Goru produced deeper BPT/S/N/mass/redshift robustness**: 60,000 cached rows, S/N>=10 count 22,311, BPT-boundary-near counts 1,473/1,155, high-excitation and Seyfert-like proxy matched-offset rows, and selection overlay from the Tori attrition packet.
- **Kun found no artifact-integrity blocker**: 41/41 PDFs magic OK, 20/20 expected PDF hashes matched, 9/9 primary PDFs, 65/65 JSON parse OK, 13/13 scripts syntax OK, and 0 fatal compile markers.
- **Literature/source Wave-2 covered M2 P2/M3 P2/M3 P3** with 12 arXiv source records and explicit future-data/status-only integration guards.
- **Literature/source Wave-3 covered the remaining active-9 gap** — **M1 RP-1**, **M2 P3**, and **M3 P1** — with 17 ADS/arXiv records, 0 duplicate keys, ADS abstracts/DOIs/identifiers available for all 17, and Goru validation.
- **External CLI visible review added a useful global critique**: the shared capped 60,000-row four-line sample and proposal-scale titles are the major scientific risks; add a Selection Function section to all nine, demote overbroad titles, merge lane-local tables, and treat **M1 RP-1** as the strongest serious paper sprint candidate only after robustness/selection disclosure.

## Independent verification snapshot

I independently checked report markers, manifests, PDF hashes, JSONL counts, and key scalar counts before using lane output for direction:

```text
DIRECTOR_VERIFY_20260708T181425Z
required_report_markers: all present
active_consolidated_slugs: 9; duplicate_active_slugs: []
lana_selection_revision_pdfs: 3/3 exist, %PDF magic OK, byte counts match, SHA256 match, compile_exit_code=0, fatal_markers=0
tori_wave2_table_pdfs: 5/5 exist, %PDF magic OK, byte counts match, SHA256 match, compile_exit_code=0, fatal_markers=0
literature_jsonl_rows: wave1=21, wave2=12, wave3=17; duplicate_keys_within_packets=[]; global_duplicate_keys=0
literature_wave3_summary: records=17, ADS bibcode/DOI/abstract/identifier availability=17/17, arXiv availability from ADS identifiers=17/17, missing target roles=[] for M1 RP-1/M2 P3/M3 P1
selection_attrition: strict SDSS four-line S/N>=3 rows=249,917; cached rows=60,000; cached coverage=0.2400797065
sSFR retention: -12<log sSFR<-11 retains 33.56% at S/N>=3; -10<log sSFR<-9.5 retains 94.85%
M3 P2 default counts: parent=121,533; S/N>=3=40,797; cached=10,270
M3 P2 strict counts: parent=33,125; S/N>=3=11,288; cached=2,941
Goru robustness: source_rows=60,000; S/N>=3/5/10 = 60,000/42,446/22,311; baseline BPT-AGN matched median offset=-1.309 dex; S/N>=10 offset=-0.744 dex; high-excitation offset=-1.136 dex; NII Seyfert-like proxy offset=-0.763 dex
Kun summary: blocking_failure_count=0; pdf_expected_mismatches=0; primary_pdf_mismatches=0; compileish_logs_with_fatal_markers=0
```

I also recovered exact definitions from the active generator code for later local manuscript cleanup: `quenched = specsfr_tot_p50 < -11.0`, `transition_or_quenched = specsfr_tot_p50 < -10.7`, `massive = lgm_tot_p50 >= 10.8`, and `high_excitation_agn = (bpt_label == "agn") & (log_oiii_hb > 0.25)`.

## Director verdict and next priorities

The board has moved from missing-source/missing-selection triage to **local integration-draft planning**. Do not do public publication or live replacement. The next valuable paper-writing work is:

1. **Mandatory cross-paper Selection Function module.** Every active paper needs a shared section stating the 249,917 strict eligible SDSS rows, 60,000 capped cached rows, 24.0% coverage, `TOP 60000 ... ORDER BY specObjID` caveat, and sSFR-dependent BPT-line retention. This must appear in abstracts/results/limitations for any population-incidence wording.
2. **Serious sprint candidate: M1 RP-1.** Promote Goru robustness into the RP-1 manuscript: S/N>=3 vs 5 vs 10, BPT/Seyfert-like sensitivity, retired/LINER guard, and selection disclosure. The headline offset should be association-only and must not be causal feedback evidence.
3. **Consolidate already-improved Wave-2 blocker drafts.** M2 P2, M3 P2, and M3 P3 now have Lana selection-disclosure revisions and Wave-2 source packets. A later integration lane should merge those into local consolidated drafts, add source guardrails, then ask Kun to compile/hash. Keep them as denominator/target-vector papers.
4. **Wave-1 cleanup with exact definitions.** M1 RP-2, M1 RP-3, and M2 P1 still need exact thresholds plus selection disclosure inserted into their Lana drafts. M2 P1’s exact high-excitation criterion is now known; M1 RP-2/M1 RP-3 use `specsfr_tot_p50 < -11.0` for quenched/low-sSFR.
5. **Title discipline before any morning packet.** Titles invoking maintenance heating, escape/recycling, radio-jet coupling, gas depletion/SFE, multiphase census, and simulation validation should be demoted in local drafts to “SDSS optical proxy/denominator/follow-up target/vector” language unless actual follow-up data are added.
6. **No more broad source harvesting tonight unless a named integration gap appears.** All active 9 now have at least one source packet; source work should shift to citation-placement rules, not more raw acquisition.

## Paper-by-paper board

| Active consolidated paper | Current lane-local state | Dependencies / blockers | Director next action |
|---|---|---|---|
| **M1 RP-1 — SDSS AGN/sSFR matched-control pilot** | Strongest serious sprint candidate. Wave-3 ADS/arXiv packet supplies DR17, SFR/catalog, optical classification, AGN/SFR context, and retired/LINER guard sources. Goru shows baseline matched offset -1.309 dex, weakening to -0.744 dex at S/N>=10 and -0.763 dex for NII Seyfert-like proxy. | Shared capped-sample and four-line selection must be in the manuscript; offset is association-only and controls are mass/redshift, not morphology/environment/aperture/non-emission-line quiescent controls. | Highest paper-writing priority: local RP-1 robustness/selection revision with demoted causal language and source guardrails. |
| **M1 RP-2 — SDSS density proxy for environmental quenching** | Lana Wave-1 draft exists; Wave-1 literature packet has environment/quenching anchors; exact quenched threshold recovered as `specsfr_tot_p50 < -11.0`. | Density is internal 10th-neighbour proxy, not group/halo environment. Needs universal selection section and portable density/threshold definitions. | Wave-1 cleanup after RP-1: insert selection disclosure, threshold, density-proxy details, and keep environment language scoped. |
| **M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up** | Lana Wave-1 draft exists; massive-host attrition counts available; Wave-1 source anchors include radio/X-ray/cavity future-measurement context. Exact low-sSFR threshold recovered as `specsfr_tot_p50 < -11.0`; massive cut is `lgm_tot_p50 >= 10.8`. | No heating/cooling observable, jet power, cavity enthalpy, or duty cycle. Optical BPT AGN fraction is an emission-line selected follow-up denominator. | Wave-1 cleanup: title/framing demotion, selection disclosure, exact threshold/cut, and future-only radio/X-ray citations. |
| **M2 P1 — high-excitation optical AGN denominator for outflow escape/recycling tests** | Lana Wave-1 draft exists; exact high-excitation criterion recovered as `bpt_label == agn` and `log_oiii_hb > 0.25`; count 4,440/60,000; Wave-1 outflow/status sources available. | No velocities, escape speeds, multiphase gas masses, CGM recycling tracer, or escape fraction. Median sSFR difference is descriptive only. | Wave-1 cleanup: replace missing-criterion note, add uncertainty/descriptive caveat, selection section, and demote title to target-selection denominator. |
| **M2 P2 — environment proxy for optical AGN in massive hosts** | Lana selection-disclosure revision exists and compiled; Wave-2 source packet has radio/environment future-data anchors; external review still flags title/jet-coupling overpromise. | No radio jets, jet powers, cavities, hot gas, or coupling efficiency; density-scale rows are correlated re-binnings. | Consolidate Lana draft + Wave-2 sources locally; preserve “optical AGN fraction versus density proxy in massive hosts” wording. |
| **M2 P3 — mass transition in quenching and optical AGN incidence** | Tori Wave-2 result-table draft exists; Wave-3 ADS/arXiv packet now supplies mass/bimodality/quenching/debate/future-data sources. | Mass-bin trends cannot separate stellar, halo, environmental, and AGN feedback without gas, halo, morphology, black-hole-mass, and central/satellite data. | Build local citation/selection revision after RP-1/Wave-2 blockers; use as observed optical transition diagnostic only. |
| **M3 P1 — common-denominator optical tracer census** | Tori Wave-2 optical tracer table draft exists; Wave-3 source packet supplies DR17/classification and multiphase wind/outflow guardrails. | Optical tracer spread is not a multiphase census; no CO/HI/Na I/X-ray/radio/kinematic common-denominator measurement. | Local revision should rename/reframe as optical-tracer denominator variance and cite multiphase sources only as missing-data guards. |
| **M3 P2 — optical denominator for gas-fraction versus efficiency tests** | Lana selection-disclosure revision exists and compiled; Wave-2 source packet has COLD GASS/xCOLD GASS/xGASS guardrails; Tori attrition gives default 121,533/40,797/10,270 and strict 33,125/11,288/2,941 counts. | H-alpha/four-line selection is not molecular gas mass, gas fraction, depletion time, or SFE; low-sSFR emission-line retention is strongly biased. | Consolidate Lana draft + gas-survey guard citations locally; title must say emission-line selected CO/HI follow-up denominator. |
| **M3 P3 — SDSS target vector for feedback-model validation** | Lana selection-disclosure revision exists and compiled; Wave-2 source packet has TNG/EAGLE/SIMBA/iMaNGA future-mock sources; two cached cells have N<500 flags. | No simulation was forward-modelled; observed vector cannot validate, reject, rank, or falsify models. | Consolidate as observed SDSS target vector only; require mocks and keep small-cell/uncertainty flags prominent. |

## Dependency ordering

1. **Selection-function module precedes any local merge across all nine.** This is now the shared scientific blocker.
2. **Exact operational definitions precede citation/prose integration.** Known thresholds/cuts should be inserted before source text is added.
3. **Source packets are sufficient for local citation-placement review, not for public prose/publication.** Wave-1/2/3 coverage now spans all active 9, but citations must be used as method/status/future-data guards.
4. **Local integration drafts precede Kun compile/hash.** Kun should next verify new consolidated drafts, not keep rechecking unchanged public-linked PDFs.
5. **No public/live changes.** All revisions remain under lane-local or later local integration-draft roots unless the user gives a separate approval gate.

## Active 9 vs omitted historical candidate topics

The active overnight board remains exactly the **9 consolidated papers** listed in the brief and public-linked proposal cards. They do not exhaust historical candidate topics from earlier backups.

| Historical source | Covered by active 9 now | Omitted / future-extension material not to count as done tonight |
|---|---|---|
| **M1 original 8 topics** | RT-01 -> M1 RP-1; RT-02 -> M1 RP-2; RT-03 -> M1 RP-3. | RT-04 through RT-08 were methods/evidence-accounting topics: unbound claims, evidence-empty sections, malformed links, dedup/provenance, and trust-promotion limits. |
| **M2 original 10 topics** | T8/T9 -> M2 P3 and M2 P1; T4 -> M2 P2; T2 partly informs M2 P1/M3 P1; T3 folded into M1 RP-3. | T1/T7/T10 traceability/full-text/rejected-position methods work; T5/T6 M51/positive-feedback future extensions. |
| **M3 original 9 topics** | t2 -> M3 P1; t4 -> M3 P2; t6 -> M3 P3; t3 partly informs M1 RP-1. | t5 maintenance-heating folded into M1 RP-3; t7 non-AGN quenching completeness; t8 halos/morphology/chemical/reionization gaps; t9 provenance repair. |

## Safety ledger

This Hwao tick wrote only this report under `lanes/hwao/` and appends one concise line to `OVERNIGHT_LEDGER.md`. No public pages, live roots, product DB/API, page_versions, trust, deploy/restart, git, billing/OAuth, external submission, or new cron jobs were touched. No active execution phrase.

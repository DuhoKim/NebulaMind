# Hwao/Fable director tick — overnight 9-paper board

Marker: `HWAO_DIRECTOR_TICK_20260708T160831Z`

UTC: 2026-07-08T16:08:31Z  
Local: 2026-07-09 01:08:31 KST

## Scope of this tick

I coordinated the overnight board only. I read the required brief, swarm board, and ledger; then I read the lane outputs now present from Lana, Goru, Kun, Literature/source, Tori, external CLI, and visible-pane monitor reports. I did not edit manuscripts, PDFs, public pages, live roots, product DB/API, page versions, trust, deploy/restart, git, billing/OAuth, external submissions, or cron jobs.

This tick is a director integration/prioritization report, not a public/publication gate.

## What changed since the first Hwao director tick

Lane outputs are now substantial and the board has moved from triage to local integration readiness:

- **Lana Wave-1** wrote and compiled lane-local revision PDFs for **M1 RP-2**, **M1 RP-3**, and **M2 P1**.
- **Goru** produced mechanical SDSS robustness tables: 60,000 source rows, 8,146 BPT AGN targets, S/N sensitivity, density-proxy checks, topic metric rows, and 15 simulation-vector cells.
- **Kun** found no reproducibility blocker: 31/31 PDFs had valid PDF magic, 12/12 expected hashes matched, 9/9 primary PDFs matched, and 0 fatal log markers were found.
- **Literature/source** produced a Wave-1 source packet with **21** public arXiv/Crossref records, explicitly separating actual SDSS/BPT method anchors from future-data/status motivation.
- **Tori Wave-2** produced and compiled lane-local result-table drafts/PDFs for **M2 P2**, **M2 P3**, **M3 P1**, **M3 P2**, and **M3 P3**.
- **External CLI** identified the biggest Wave-2 blocker: the 60,000-row four-line emission-line denominator must disclose parent-to-denominator selection-function attrition, especially for gas-depletion and low-sSFR language.
- **Tori selection-function attrition** addressed that blocker with public/read-only SDSS DR17 count artifacts: strict four-line S/N>=3 eligible rows are 249,917; the cached 60,000-row sample covers 24.0% and is a capped `TOP 60000 ... ORDER BY s.specObjID` subset, not a random or complete parent sample.

## Independent verification snapshot

I independently verified the lane artifacts before using them for direction:

```text
DIRECTOR_VERIFY
reports_exist True count 6
markers GORU_ACTUAL_DATA_ROBUSTNESS_TICK_20260708T141459Z KUN_REPRO_AUDIT_20260708T142406Z LITERATURE_SOURCE_TICK_20260708T143233Z TORI_WAVE2_RESULT_TABLE_DRAFTS_20260708T143512Z SELECTION_FUNCTION_ATTRITION_TICK_20260708T155514Z
counts lana_drafts 3 tori_wave2_drafts 5 lit_sources 21 goru_rows 60000 kun_primary_pdfs 9
pdf_failures 0 []
selection strict_sdss_sn3 249917 cached_rows 60000 coverage 0.24008 raw_json 43 raw_sql 43 csv_rows {'m3_p2_massive_low_ssfr_attrition_csv': 6, 'm3_p3_small_cell_attrition_csv': 2, 'massive_host_attrition_csv': 3, 'selection_stage_counts_csv': 7, 'ssfr_bin_line_selection_attrition_csv': 7}
active_slug_duplicates False active_slug_count 9
m2p1_high_excitation_code_line df["high_excitation_agn"] = (df["bpt_label"] == "agn") & (df["log_oiii_hb"] > 0.25)
safety_strings_ok True
```

The M2 P1 high-excitation criterion has now been recovered from the generator code: **BPT label is `agn` and `log_oiii_hb > 0.25`**. That removes one Lana/Literature merge-note blocker, while keeping the caveat that this is an optical-line denominator and not an outflow/escape measurement.

## Director verdict

The next most valuable work is **not** to declare the papers done and not to mirror anything public. The board should run one integration-quality wave focused on denominator honesty, source grounding, and merge decisions:

1. **Highest priority: revise Wave-2 vulnerable drafts locally with the selection-function packet.** Target **M2 P2**, **M3 P2**, and **M3 P3** first. Add parent-to-denominator disclosure, identify the 60,000-row sample as capped rather than complete/random, demote gas-depletion language to “emission-line detected massive low-sSFR denominator,” and add minimum-N/uncertainty flags to M3 P3 cells.
2. **Wave-1 cleanup: update M2 P1 methods locally using the exact high-excitation criterion.** Lana can now replace the placeholder merge note with `bpt_label == agn` and `log_oiii_hb > 0.25`; literature citations should still be method/status anchors only.
3. **Literature/source Wave-2: build topic-specific source packets for M2 P2, M2 P3, M3 P1, M3 P2, and M3 P3.** Do not insert citations as claim support until each source is classified as actual-method support, scoped interpretation, future-data motivation, or status-only.
4. **Kun after any local integration draft:** compile/hash only after revised local drafts exist. Rechecking old public-linked PDFs is lower value unless a manifest changed.
5. **M1 RP-1 expansion remains useful but is no longer the bottleneck.** It should get a later methods/discussion expansion using Goru matched-control robustness and the new selection disclosure, but the five Wave-2 drafts currently carry higher risk.

## Paper-by-paper board

| Active consolidated paper | Current lane-local state | Dependencies / blockers | Director next action |
|---|---|---|---|
| **M1 RP-1 — SDSS AGN/sSFR matched-control pilot** | Strongest original draft; Goru quantified matched offsets: baseline AGN-minus-SF median log-sSFR offset -1.309 dex, S/N>=5 -1.160 dex, S/N>=10 -0.744 dex. | Needs same sample-selection disclosure as the rest; still association-only, not causal feedback proof. | Later expansion: methods/result/discussion module with S/N robustness and capped-sample caveat. Do not prioritize over Wave-2 blockers. |
| **M1 RP-2 — SDSS density proxy for environmental quenching** | Lana revision PDF exists; Goru k=10 high-minus-low quenched fraction +0.050 with CI [0.041, 0.059]; Literature packet has Peng/Baldry as scoped interpretation anchors. | Nearest-neighbour density is not halo mass, group catalogue, or central/satellite status. Needs DR17/BPT and topic sources inserted carefully. | Candidate for local integration once citations and selection disclosure are added. Keep causal environment language guarded. |
| **M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up** | Lana revision PDF exists; Literature packet has Best 2005 bridge and McNamara/Nulsen future-measurement anchors; Tori selection packet includes massive-host attrition table. | Optical BPT AGN fraction is not jet power, cavity enthalpy, cooling luminosity, or duty cycle. Massive-host denominator must disclose emission-line selection. | Add selection disclosure and source anchors in a local Wave-1 refresh; keep X-ray/radio measurements explicitly future-only. |
| **M2 P1 — high-excitation optical AGN denominator for outflow escape/recycling tests** | Lana revision PDF exists; Literature packet has classification/outflow context; exact criterion recovered from code: BPT `agn` and `log_oiii_hb > 0.25`; count remains 4,440/60,000. | SDSS has no outflow velocity, escape velocity, molecular/neutral phase, CGM recycling tracer, or escape fraction. | Immediate small Lana refresh: insert exact high-excitation criterion and keep Cicone/Fiore/Carniani/Veilleux/Fabian as future-data/status motivation only. |
| **M2 P2 — environment proxy for optical AGN in massive hosts** | Tori Wave-2 result-table draft/PDF exists; external review flagged denominator/selection disclosure and “scale-robust” overwording; selection packet covers massive-host attrition. | Not a radio-jet coupling measurement. Density-scale rows are correlated re-binnings of the same SDSS denominator. | **Top Wave-2 target.** Revise local draft with selection disclosure; soften “scale-robust” to “insensitive to neighbor-count choice”; add massive-host parent/S/N/cached counts. |
| **M2 P3 — mass transition in quenching and optical AGN incidence** | Tori Wave-2 mass-bin table draft/PDF exists and is lower immediate risk than M2 P2/M3 P2/M3 P3. | Needs topic-specific transition/quenching literature and no causal attribution to stellar vs AGN feedback without gas/halo/redshift data. | Literature Wave-2 source packet, then local citation/method integration. Keep as Wave-2 second tier after selection blocker papers. |
| **M3 P1 — common-denominator optical tracer census** | Tori Wave-2 optical tracer prevalence table draft/PDF exists; Goru supplied S/N/tracer sensitivity. | Optical tracer census only; no molecular/neutral/X-ray/radio common-denominator measurement. Needs source anchors for multiphase/common-denominator logic. | Literature Wave-2 source packet; add explicit column definitions and S/N uncertainty convention before any merge. |
| **M3 P2 — optical denominator for gas-fraction versus efficiency tests** | Tori Wave-2 threshold-grid draft/PDF exists; external review marked gas-denominator emission-line bias as a blocker; selection packet gives parent/S/N/cached rows for default and strict denominators. | Highest wording risk: optical H-alpha proxy and emission-line availability are not CO/dust gas mass, gas fraction, depletion time, or SFE. | **Top Wave-2 target.** Revise local draft around “emission-line detected massive low-sSFR follow-up denominator”; include default 121,533 parent / 40,797 S/N>=3 / 10,270 cached and strict 33,125 / 11,288 / 2,941 counts. |
| **M3 P3 — SDSS target vector for feedback-model validation** | Tori Wave-2 15-cell target-vector draft/PDF exists; external review verified cells sum to 60,000; selection packet identifies 2 cached cells with N<500 and provides parent/S/N checks. | Observed target vector only; no simulation has been forward-modelled through SDSS/MaNGA/ALMA/X-ray/radio selection functions. Small cells should not carry overprecise headline claims. | **Top Wave-2 target.** Add min-N/uncertainty flags, reduce false precision, and explicitly require mocks before model validation. |

## Dependency ordering

1. **Selection-function disclosure precedes any local merge for M2 P2, M3 P2, and M3 P3.** These are the current blocker papers.
2. **Exact method definitions precede citation/prose integration.** M2 P1 now has its exact high-excitation criterion; M3 P1/M2 P2/M3 P2/M3 P3 still need standardized column definitions and uncertainty conventions.
3. **Source packets precede bibliography insertion.** Wave-1 has source grounding; Wave-2 still needs topic-specific source grounding before citations are integrated.
4. **Compile/hash follows local draft changes.** Kun should verify revised local PDFs after the next draft wave, not before.
5. **No public/live artifact changes.** Any revised papers remain lane-local or local integration drafts until a separate explicit approval gate.

## Active 9 vs omitted historical candidate topics

The active overnight board remains the **9 consolidated papers** listed in the brief and public-linked proposal cards. They do **not** exhaust historical candidate topics from earlier backups.

| Historical source | Covered by active 9 now | Omitted / future-extension material not to count as done tonight |
|---|---|---|
| **M1 original 8 topics** | RT-01 -> M1 RP-1; RT-02 -> M1 RP-2; RT-03 -> M1 RP-3. | RT-04 through RT-08 were methods/evidence-accounting topics: unbound claims, evidence-empty sections, malformed links, dedup/provenance, and trust-promotion limits. |
| **M2 original 10 topics** | T8/T9 -> M2 P3 and M2 P1; T4 -> M2 P2; T2 partly informs M2 P1/M3 P1; T3 folded into M1 RP-3. | T1/T7/T10 traceability/full-text/rejected-position methods work; T5/T6 M51/positive-feedback future extensions. |
| **M3 original 9 topics** | t2 -> M3 P1; t4 -> M3 P2; t6 -> M3 P3; t3 partly informs M1 RP-1. | t5 maintenance-heating folded into M1 RP-3; t7 non-AGN quenching completeness; t8 halos/morphology/chemical/reionization gaps; t9 provenance repair. |

## Safety ledger

This Hwao tick wrote only this report under `lanes/hwao/` and appended one concise line to `OVERNIGHT_LEDGER.md`. No public pages, live roots, product DB/API, page_versions, trust, deploy/restart, git, billing/OAuth, external submission, or new cron jobs were touched. No active execution phrase.

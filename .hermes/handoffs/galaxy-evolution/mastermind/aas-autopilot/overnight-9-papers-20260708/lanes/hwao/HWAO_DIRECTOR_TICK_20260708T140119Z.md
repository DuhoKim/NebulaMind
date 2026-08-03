# Hwao/Fable director tick — overnight 9-paper board

Marker: `HWAO_DIRECTOR_TICK_20260708T140119Z`

UTC: 2026-07-08T14:01:19Z  
Local: 2026-07-08 23:01:19 KST

## Scope of this tick

I coordinated the overnight board only. I read the required brief, swarm board, ledger, first inventory/tick artifacts, the 8-paper manifest, and the current/backup research-topic maps used to distinguish the 9 active consolidated papers from omitted historical candidate topics. I found no lane-local outputs yet: `lanes/` did not exist before this Hwao report.

No manuscripts, PDFs, public pages, live roots, product DB/API, page versions, trust, deploy/restart, git, billing/OAuth, external submissions, or cron jobs were changed.

## Director verdict

The overnight board is active but still at the coordination/triage stage. The first verifier established that 9/9 PDFs compile and all 9 have interpretation guards; the writing gap is depth, not existence. The next useful work is **not** to claim completion or chase public updates. It is to feed manuscript improvements from verified lane-local artifacts:

1. **Goru first:** build compact table payloads from existing `analysis_results.json` for all 8 batch papers, plus robustness candidates where feasible.
2. **Literature/source lane in parallel:** source-anchor packets for the highest overclaim-risk papers before citations are inserted into prose.
3. **Lana next:** AASTeX revision drafts, lane-local only, for the first three manuscript-improvement targets.
4. **Kun after drafts:** compile/hash/repro checks only after integration drafts exist.

The first three paper-writing targets should be **M1 RP-2**, **M1 RP-3**, and **M2 P1**. They cover environment, maintenance heating, and escape/recycling; they are thin batch drafts; and their results can be strengthened without pretending SDSS optical proxies prove the full physical proposals.

## Active 9 consolidated papers board

| Active paper | Current evidence/manuscript state from inventory | Dependencies and guardrails | Next most valuable lane action |
|---|---|---|---|
| **M1 RP-1 — SDSS AGN/sSFR matched-control pilot** | Strongest current draft: 2 figures, 1 result table, 5 bibitems, ~1023 words, guard present. Still thin for a full AAS-style paper. | Keep as association/matched-control pilot, not causal feedback proof. Needs clearer sample/matching definitions and robustness around match quality/bootstrap intervals. | Defer major edits until batch papers catch up. Lana can later expand methods/results/discussion; Goru can package matched-pair robustness notes. |
| **M1 RP-2 — SDSS density proxy for environmental quenching** | Batch-thin: 1 figure, no table, 4 generic bibitems, ~378 words. Verified result bullets include high- vs low-density quenched fractions and mass/redshift-adjusted coefficient. | SDSS nearest-neighbour proxy is not a group/halo/central-satellite measurement. Full topic needs group catalogues, halo masses, morphology, and redshift selection functions. | **Wave-1 target.** Goru: table payload with high/low density counts, CI, LPM coefficient. Literature: environment-quenching anchors. Lana: methods/results guard draft. |
| **M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up** | Batch-thin: 1 figure, no table, 4 generic bibitems, ~379 words. Results include massive and massive-low-sSFR optical AGN fractions. | Optical AGN fraction is only a denominator. It does not measure cavity power, cooling luminosity, jet power, or heating/cooling balance. | **Wave-1 target.** Goru: denominator/result table. Literature: cavity/cooling/radio-mode maintenance anchors. Lana: explicit X-ray/radio follow-up boundary. |
| **M2 P1 — high-excitation optical AGN denominator for outflow escape/recycling tests** | Batch-thin: 1 figure, no table, 4 generic bibitems, ~379 words. Results include 4,440/60,000 high-excitation optical AGN and median sSFR comparison. | Highest overclaim risk: SDSS does not measure outflow velocity, halo escape speed, molecular/neutral phases, or recycling. Must remain denominator-only. | **Wave-1 target.** Goru: high-excitation denominator table. Literature: escape/recycling/outflow prevalence anchors. Lana: rewrite around “target denominator,” not escape result. |
| **M2 P2 — environment proxy for optical AGN in massive hosts** | Batch-thin: 1 figure, no table, 4 generic bibitems, ~375 words. Results include high- vs low-density massive-host optical AGN fractions and CI. | Not a radio-jet coupling measurement; no jet powers, cavities, ages, or hot-gas densities. Must stay as optical/environment denominator. | Wave-2. Reuse RP-2 environment-proxy mechanics but add radio-jet coupling literature and separate it from generic quenching. |
| **M2 P3 — mass transition in quenching and optical AGN incidence** | Batch-thin: 1 figure, no table, 4 generic bibitems, ~372 words. Results identify the mass bin where quenched fraction exceeds 0.5 and AGN fraction peaks. | Optical transition diagnostic only. Does not assign causality to stellar vs AGN feedback without gas fractions, halo masses, baryon deficits, and high-redshift tests. | Wave-2. Goru: mass-bin table payload. Literature: transition-mass and quenching-threshold anchors. Lana: avoid causal transition language. |
| **M3 P1 — common-denominator optical tracer census** | Batch-thin: 1 figure, no table, 4 generic bibitems, ~378 words. Results show optical tracer prevalence range and widest/narrowest ratio. | Optical-only census; does not measure molecular, neutral, ionized-outflow, X-ray, or radio phases on a shared denominator. | Wave-2/3. Goru: tracer-prevalence table. Literature: multiphase census/common-denominator anchors. Lana: make the “why common denominator” argument explicit. |
| **M3 P2 — optical denominator for gas-fraction versus efficiency tests** | Batch-thin: 1 figure, no table, 4 generic bibitems, ~396 words. Results include massive transition/quenched denominator, optical AGN fraction, H-alpha proxy offset. | High overclaim risk: SDSS optical data cannot distinguish molecular-gas depletion from low star-formation efficiency; needs CO/dust gas masses and aperture-matched SFRs. | Early Wave-2. Goru: denominator/H-alpha proxy table. Literature: molecular gas/depletion-time anchors. Lana: CO follow-up boundary. |
| **M3 P3 — SDSS target vector for feedback-model validation** | Batch-thin: 1 figure, no table, 4 generic bibitems, ~374 words. Results include 15 mass-redshift cells and ranges of quenched/AGN fractions. | Observed SDSS target vector only. No simulation has been forward-modelled through SDSS/MaNGA/ALMA/X-ray/radio selection functions here. | Wave-3. Goru: machine-readable target-vector table. Kun: validate JSON/table consistency. Lana: simulation-forward-modelling caveat. |

## Chosen next paper-writing priorities

### Priority 1 — create table-ready result/proxy-limit payloads

Ask Goru to produce lane-local payloads for all 8 batch papers from existing `analysis_results.json` files: one compact AASTeX-ready table per paper with measured numerator/denominator, fraction/interval or coefficient, proxy limit, and required follow-up. This unblocks Lana without manuscript races.

### Priority 2 — source-anchor packets before prose citations

Ask the literature/source lane to start with the three Wave-1 targets:

- **M1 RP-2:** environment quenching, group/halo/central-satellite caveats.
- **M1 RP-3:** maintenance heating, X-ray cavities/cooling luminosity, radio-mode duty cycle.
- **M2 P1:** outflow detection versus escape/recycling and multiphase reservoir follow-up.

These should be artifact-first source packets, not direct manuscript prose. Abstract-only anchors must be labelled as such; no evidence-hunting to rescue broad claims.

### Priority 3 — Lana lane-local AASTeX drafts for Wave-1 only

Once table/source packets exist, Lana should draft small lane-local revision modules for M1 RP-2, M1 RP-3, and M2 P1: expanded Scope/Data/Result/Interpretation/Reproducibility sections plus one result/proxy-limit table. Do not overwrite the public-linked manuscripts.

### Priority 4 — Kun compile/hash pass after integration drafts

Kun should wait until a local integration draft exists, then compile and hash. Compiling the original PDFs again is low value because the first tick already verified they compile.

## Dependencies and ordering

1. **Table payloads precede AASTeX edits.** Otherwise the batch papers get prettier prose without stronger result structure.
2. **Source-anchor packets precede bibliography insertion.** The astronomy corpus gate remains in force: papers/source anchors must feed a status/debate map or local source packet before prose claims are strengthened.
3. **Wave-1 before RP-1.** RP-1 is imperfect but already has the only table; the 8 batch papers are the bottleneck.
4. **No live/public mirroring.** Any eventual revised PDFs remain local until a later explicit approval gate.
5. **No omitted-topic resurrection inside the 9-paper run.** Omitted candidates may be mapped as future work, but the active board remains the 9 consolidated papers above.

## Active vs omitted historical candidate topics

Basis checked this tick: the active 9 in the overnight brief/manifest/current topic maps, plus pre-proposal-style backup maps that had M1=8, M2=10, M3=9 candidate topics before consolidation. The 9 papers do **not** exhaust that historical universe.

| Historical source | Active papers now covering part of it | Omitted / future-extension material not to treat as done tonight |
|---|---|---|
| **M1 original 8 topics** | RT-01 → M1 RP-1; RT-02 → M1 RP-2; RT-03 → M1 RP-3. | RT-04 through RT-08 were methods/evidence-accounting topics: 27 unbound claims, evidence-empty sections, malformed links, row-vs-paper dedup, and minimal evidence for trust promotion. These are not active AAS data papers. |
| **M2 original 10 topics** | T8/T9 → active M2 P3 and M2 P1; T4 → active M2 P2; T2 partly informs M2 P1/M3 P1. | T1/T7/T10 are traceability/full-text/rejected-position methods work; T5/T6 are M51/positive-feedback future extensions; T3 maintenance-heating bound is folded into M1 RP-3 rather than a separate M2 paper. |
| **M3 original 9 topics** | t2 → M3 P1; t4 → M3 P2; t6 → M3 P3; t3 partly informs M1 RP-1. | t5 maintenance-heating status is folded into M1 RP-3; t7 non-AGN quenching completeness, t8 halos/morphology/chemical/reionization coverage gaps, and t9 provenance repair remain omitted/future work. |

## Safety ledger

This Hwao tick wrote only this lane-local report under `lanes/hwao/` and appended one ledger line. No public pages, live roots, product DB/API, page_versions, trust, deploy/restart, git, billing/OAuth, external submission, or new cron jobs were touched. No active execution phrase.

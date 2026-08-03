# codex-kun-cycle-9
Started UTC: 2026-07-09T03:54:16Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

Reading additional input from stdin...
OpenAI Codex v0.143.0
--------
workdir: /Users/duhokim/NebulaMind/NebulaMind
model: gpt-5.4-mini
provider: openai
approval: never
sandbox: read-only
reasoning effort: none
reasoning summaries: none
session id: 019f4503-1139-7a12-9af7-489459ccee4a
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_09.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m checking the manuscript package for TeX, compile, figure, and reproducibility issues, then I’ll verify the required numeric claims and any wording that could violate the association-only guardrail. I’ll read the four core files first and then cross-check for consistency against the numbers you listed.
exec
/bin/zsh -lc "printf '%s\\n' '--- PACKAGE_AUDIT ---' && sed -n '1,260p' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/PACKAGE_AUDIT.md && printf '\\n--- FINAL_HANDOFF ---\\n' && sed -n '1,260p' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
--- PACKAGE_AUDIT ---
# Decision package audit

Package: `RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`
Audit UTC: 2026-07-09T01:41:23Z

## Counts
- outputs: 2
- pdfs_ok: 2
- logs_ok: 2
- figures_ok: 10
- total_figures: 10
- fatal_failures: 0

## Outputs
- flagship: PDF bytes 236847; SHA256 `3392f53534d8452ebb3db4191dff7855ebb13428dff768d45d847be9d5d8efac`; warnings 10; figures 2
- supplement: PDF bytes 527135; SHA256 `403a69d8fcf02c56bd3266db0de0363ea9c45c659d5a305861cfba7144b705e2`; warnings 19; figures 8

## Failures
- none

Safety: local decision package only; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes.

--- FINAL_HANDOFF ---
# RP-1 flagship + supplementary atlas final handoff

Marker: `RP1_FLAGSHIP_SUPPLEMENT_FINAL_HANDOFF_20260709T014249Z`

Completed at: 2026-07-09 10:42 KST / 2026-07-09T01:42Z

## User directive

Proceed with the recommended next decision after the integrated 9-paper local run.

The prior recommendation was:

1. Review RP-1 as the candidate flagship paper.
2. Decide whether the other 8 should stay standalone guarded PDFs or become appendices/supplementary denominator notes under one combined suite paper.
3. If approved, run a final prose-polish pass on RP-1 only, then recompile and audit.
4. Stop before public replacement/publish unless separately approved.

## Decision made

Proceed with **one flagship paper plus one supplementary denominator/proxy atlas**.

Reason:

- RP-1 is the only current active paper with a direct, coherent SDSS row-level result strong enough for a short-paper draft.
- The other 8 are useful, but they are not 8 independent causal physical-feedback papers with the current SDSS-only data.
- Their correct packaging is as a combined denominator/proxy atlas: target definitions, selection-aware baselines, and missing-observable checklists for future radio/X-ray/CO/HI/outflow/halo/simulation work.

Decision packet:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/FLAGSHIP_REVIEW_DECISION_20260709T013510Z.md`

## Local package created

Package ID:

`RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`

Package root:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`

Package generator:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/build_flagship_decision_package.py`

Precompile manifest:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_MANIFEST_PRECOMPILE.json`

Audit Markdown:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.md`

Audit JSON:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/PACKAGE_AUDIT.json`

## Output 1: polished RP-1 flagship draft

PDF:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.pdf`

Source:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.tex`

Compile log:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.compile.log`

Audit result:

- PDF bytes: 236,847
- SHA256: `3392f53534d8452ebb3db4191dff7855ebb13428dff768d45d847be9d5d8efac`
- Compile warnings: 10 AASTeX/line-break warnings only
- Figures: 2
- Fatal failures: 0

Scientific status:

- Candidate flagship short-paper draft.
- Core claim: broad optical BPT AGN hosts in the capped SDSS DR17 optical emission-line denominator have lower catalog sSFR than mass-redshift matched star-forming controls.
- Main number: 8,146 matched pairs, median delta log sSFR = -1.309 dex, bootstrap interval [-1.334, -1.283] dex.
- Guard: association only, not causal AGN feedback.
- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
- Required caveat: S/N>=10 and narrower Seyfert-like definitions reduce the offset magnitude, so subclass/selection dependence is real.

## Output 2: supplementary denominator/proxy atlas

PDF:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf`

Source:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`

Compile log:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log`

Audit result:

- PDF bytes: 527,135
- SHA256: `403a69d8fcf02c56bd3266db0de0363ea9c45c659d5a305861cfba7144b705e2`
- Compile warnings: 19 AASTeX/line-break warnings only
- Figures: 8
- Fatal failures: 0

Scientific status:

The atlas combines the other 8 active drafts as guarded denominator/proxy notes:

1. `m1_rp2_environment_quenching` — density proxy / environment denominator, not halo/group quenching proof.
2. `m1_rp3_maintenance_heating` — optical AGN denominator, not radio/X-ray maintenance-heating measurement.
3. `m2_p1_outflow_escape_recycling` — high-excitation optical AGN denominator, not outflow escape/recycling measurement.
4. `m2_p2_radio_jet_environment` — optical AGN fraction vs internal density proxy, not radio-jet coupling test.
5. `m2_p3_feedback_transition_mass` — mass-vector optical incidence diagnostic, not causal transition-mass physics.
6. `m3_p1_multiphase_census` — optical tracer-threshold census, not multiphase gas census.
7. `m3_p2_gas_depletion_efficiency` — optical/H-alpha denominator for CO/gas follow-up, not gas depletion-time measurement.
8. `m3_p3_simulation_validation` — observed SDSS target vector, not simulation validation/rejection.

## Package audit

From `PACKAGE_AUDIT.md`:

- outputs: 2
- pdfs_ok: 2
- logs_ok: 2
- figures_ok: 10
- total_figures: 10
- fatal_failures: 0

Failures: none.

## Compile/debug note

During compile, the supplement built cleanly first. The flagship initially failed because a generated table row began with `[N II]`, which TeX parsed as optional row spacing after a line break. The generator was fixed to use `N II Seyfert-like proxy` instead. Both PDFs then compiled successfully.

## What changed from the previous integrated 9-paper run

Previous state:

- 9 separate integrated PDFs.
- RP-1 was already flagged as strongest.
- Other 8 were guarded but still emitted as separate paper PDFs.

Current state:

- 1 polished flagship RP-1 paper.
- 1 combined supplementary denominator/proxy atlas containing the other 8.
- Cleaner science package: one real flagship result plus one honest atlas of follow-up denominators and missing observables.

## Next gate

Recommended next step is a human/Hwao/Lana science review of the two-PDF package:

1. Read the polished RP-1 PDF for scientific wording, especially whether the association-only claim is clear enough.
2. Read the supplement as an atlas, not as eight papers.
3. Decide whether to:
   - keep this package local only;
   - do another local prose-polish pass;
   - add a local cover note/README for reviewers;
   - or explicitly approve public replacement/addition of these PDFs.

Publishing/public update is **not** approved by this handoff.

## Safety ledger

No public pages, live roots, public PDF replacement, database writes, SQL, `/api/pages`, `page_versions`, wiki publish, trust recompute, deploy/restart, git commit/push/merge, cron creation/update, billing/cloud/OAuth/API-key changes, or external manuscript submission were performed.

exec
/bin/zsh -lc "pwd && ls -la .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package && printf '\\n--- flagship ---\\n' && sed -n '1,260p' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex && printf '\\n--- supplementary ---\\n' && sed -n '1,260p' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind
total 592
drwxr-xr-x@ 49 duhokim  staff   1568 Jul  9 12:47 .
drwxr-xr-x@ 11 duhokim  staff    352 Jul  9 12:54 ..
-rw-r--r--@  1 duhokim  staff   6244 Jul  9 12:11 CYCLE_01_QUALITY_AUDIT.json
-rw-r--r--@  1 duhokim  staff    563 Jul  9 12:11 CYCLE_01_QUALITY_AUDIT.md
-rw-r--r--@  1 duhokim  staff   1801 Jul  9 12:10 CYCLE_01_REVIEW_RESPONSE.md
-rw-r--r--@  1 duhokim  staff   9315 Jul  9 12:11 CYCLE_01_SUMMARY.json
-rw-r--r--@  1 duhokim  staff   1729 Jul  9 12:11 CYCLE_01_SUMMARY.md
-rw-r--r--@  1 duhokim  staff   6244 Jul  9 12:18 CYCLE_02_QUALITY_AUDIT.json
-rw-r--r--@  1 duhokim  staff    563 Jul  9 12:18 CYCLE_02_QUALITY_AUDIT.md
-rw-r--r--@  1 duhokim  staff   1716 Jul  9 12:18 CYCLE_02_REVIEW_RESPONSE.md
-rw-r--r--@  1 duhokim  staff   9315 Jul  9 12:18 CYCLE_02_SUMMARY.json
-rw-r--r--@  1 duhokim  staff   1729 Jul  9 12:18 CYCLE_02_SUMMARY.md
-rw-r--r--@  1 duhokim  staff   6348 Jul  9 12:23 CYCLE_03_QUALITY_AUDIT.json
-rw-r--r--@  1 duhokim  staff    577 Jul  9 12:23 CYCLE_03_QUALITY_AUDIT.md
-rw-r--r--@  1 duhokim  staff    893 Jul  9 12:22 CYCLE_03_REVIEW_RESPONSE.md
-rw-r--r--@  1 duhokim  staff   9435 Jul  9 12:23 CYCLE_03_SUMMARY.json
-rw-r--r--@  1 duhokim  staff   1729 Jul  9 12:23 CYCLE_03_SUMMARY.md
-rw-r--r--@  1 duhokim  staff   6244 Jul  9 12:32 CYCLE_04_QUALITY_AUDIT.json
-rw-r--r--@  1 duhokim  staff    563 Jul  9 12:32 CYCLE_04_QUALITY_AUDIT.md
-rw-r--r--@  1 duhokim  staff   2034 Jul  9 12:31 CYCLE_04_REVIEW_RESPONSE.md
-rw-r--r--@  1 duhokim  staff   9315 Jul  9 12:32 CYCLE_04_SUMMARY.json
-rw-r--r--@  1 duhokim  staff   1729 Jul  9 12:32 CYCLE_04_SUMMARY.md
-rw-r--r--@  1 duhokim  staff   6244 Jul  9 12:37 CYCLE_05_QUALITY_AUDIT.json
-rw-r--r--@  1 duhokim  staff    563 Jul  9 12:37 CYCLE_05_QUALITY_AUDIT.md
-rw-r--r--@  1 duhokim  staff   1694 Jul  9 12:36 CYCLE_05_REVIEW_RESPONSE.md
-rw-r--r--@  1 duhokim  staff   9315 Jul  9 12:37 CYCLE_05_SUMMARY.json
-rw-r--r--@  1 duhokim  staff   1729 Jul  9 12:37 CYCLE_05_SUMMARY.md
-rw-r--r--@  1 duhokim  staff   6244 Jul  9 12:41 CYCLE_06_QUALITY_AUDIT.json
-rw-r--r--@  1 duhokim  staff    563 Jul  9 12:41 CYCLE_06_QUALITY_AUDIT.md
-rw-r--r--@  1 duhokim  staff   1915 Jul  9 12:41 CYCLE_06_REVIEW_RESPONSE.md
-rw-r--r--@  1 duhokim  staff   9315 Jul  9 12:41 CYCLE_06_SUMMARY.json
-rw-r--r--@  1 duhokim  staff   1729 Jul  9 12:41 CYCLE_06_SUMMARY.md
-rw-r--r--@  1 duhokim  staff   6244 Jul  9 12:48 CYCLE_07_QUALITY_AUDIT.json
-rw-r--r--@  1 duhokim  staff    563 Jul  9 12:48 CYCLE_07_QUALITY_AUDIT.md
-rw-r--r--@  1 duhokim  staff   1871 Jul  9 12:47 CYCLE_07_REVIEW_RESPONSE.md
-rw-r--r--@  1 duhokim  staff   9315 Jul  9 12:48 CYCLE_07_SUMMARY.json
-rw-r--r--@  1 duhokim  staff   1729 Jul  9 12:48 CYCLE_07_SUMMARY.md
-rw-r--r--@  1 duhokim  staff   6244 Jul  9 12:54 CYCLE_08_QUALITY_AUDIT.json
-rw-r--r--@  1 duhokim  staff    563 Jul  9 12:54 CYCLE_08_QUALITY_AUDIT.md
-rw-r--r--@  1 duhokim  staff   1783 Jul  9 12:53 CYCLE_08_REVIEW_RESPONSE.md
-rw-r--r--@  1 duhokim  staff   9315 Jul  9 12:54 CYCLE_08_SUMMARY.json
-rw-r--r--@  1 duhokim  staff   1729 Jul  9 12:54 CYCLE_08_SUMMARY.md
-rw-------@  1 duhokim  staff   8444 Jul  9 10:45 FINAL_HANDOFF.md
-rw-r--r--@  1 duhokim  staff   6977 Jul  9 10:41 PACKAGE_AUDIT.json
-rw-r--r--@  1 duhokim  staff    632 Jul  9 10:41 PACKAGE_AUDIT.md
-rw-r--r--@  1 duhokim  staff  10922 Jul  9 10:40 PACKAGE_MANIFEST_PRECOMPILE.json
-rw-r--r--@  1 duhokim  staff    223 Jul  9 10:40 README.md
drwxr-xr-x@  4 duhokim  staff    128 Jul  9 10:39 flagship_rp1
drwxr-xr-x@  4 duhokim  staff    128 Jul  9 10:39 supplementary_denominator_atlas

--- flagship ---
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Selection-aware SDSS BPT/sSFR study}
\shortauthors{NebulaMind}
\begin{document}

\title{Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Study}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, capped 60k-row pilot cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, indicating that the result depends on the chosen emission-line denominator and on the exclusion of LINER-like, retired, bulge-dominated hosts with weak central star formation. An accompanying supplementary denominator/proxy atlas collects the related baselines, selection caveats, and missing-observable notes.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a strong negative sSFR offset within the cached denominator analyzed here. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
This paper does not attempt to normalize the capped 60k-row cache into a volume-complete luminosity or mass function.

The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\subsection{Scope and limitations}
The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a capped 60k-row pilot cache selected sequentially by \texttt{specObjID} after an arbitrary pilot-query row limit; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the pilot cache covers 24.0\% of that strict parent. Because the cap is arbitrary and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy that can differ systematically between bulge-dominated and disk-dominated systems.
The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade for the flagship denominator. The 60k-row pilot cache is an artificial pilot-query cap, not a physical selection effect.\label{tab:selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.

\section{Classification and matching}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical BPT galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.

\begin{figure*}
\centering
\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
\label{fig:bpt}
\end{figure*}

\section{Matched-control result}
The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the broad BPT-selected galaxies relative to star-forming controls.
A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR within this fiber-centered matched comparison, but this manuscript does not convert that proxy offset into a global quenching threshold.
Because the comparison is fiber-centered and the matching ignores morphology, the measured offset is a relative difference between the broad-BPT and control samples within the fiber aperture. It can therefore reflect the known bulge/disk mismatch between broad-BPT hosts and star-forming controls rather than a galaxy-wide suppression signal.

\begin{deluxetable*}{lrrrr}
\tabletypesize{\scriptsize}
\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
\startdata
Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
\enddata
\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
\end{deluxetable*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT-selected galaxies minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
\label{fig:offsets}
\end{figure*}

\section{Interpretation}
The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper.
Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including low-ionization nuclear emission-line region (LINER)-like emission from retired stellar populations and post-AGB stars in massive bulges, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global quenching signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this capped 60k-row pilot cache. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{Conclusion}
RP-1 is best treated as a concise, selection-aware association paper, not a causal study. An accompanying supplementary denominator/proxy atlas holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
In practice, that means future work needs the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation-mock comparisons \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,piotrowska2022,wetzel2013,dekel2006}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.

\section{Local reproducibility}
This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}

--- supplementary ---
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS denominator/proxy atlas}
\shortauthors{NebulaMind}
\begin{document}

\title{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. The cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. Keeping the notes in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.

\section{Shared denominator}
The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing.

The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

\section{Atlas notes}

\subsection{Environment baseline: SDSS 10th-neighbor index for low-sSFR incidence}
This subsection presents an internal environmental baseline that can later be joined to group catalogs and halo masses. Within this selection-biased emission-line denominator, the 10th-neighbor index covaries with the catalog low-sSFR fraction; this index is only an internal ordinal rank and does not map to physical environmental volume density or halo density. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item group catalogues
\item robust central/satellite labels
\item halo masses
\item spectroscopic fiber-collision correction at the 55-arcsec scale
\item morphology
\item multi-redshift selection functions
\end{itemize}
Within this selection-biased emission-line cache, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement.
These are still needed for a future environmental test \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up, not a physical-feedback measurement.}
\label{fig:m1-rp2-environment-quenching}
\end{figure}


\subsection{Maintenance-heating denominator: optical AGN in massive SDSS hosts}
This subsection identifies the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item X-ray cavity or cooling-luminosity measurements
\item radio jet powers
\item halo-selected parent catalogues
\item nondetection modelling
\end{itemize}
These are still needed for a future maintenance-heating test \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements, not a heating-to-cooling result.}
\label{fig:m1-rp3-maintenance-heating}
\end{figure}


\subsection{Outflow-kinematics denominator: high-excitation SDSS AGN}
This subsection isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item resolved outflow velocities
\item halo potentials
\item molecular, ionized, and neutral gas phases
\item CGM recycling tracers
\end{itemize}
These are still needed for a future outflow test \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
\caption{SDSS optical emission-line denominator: the high-excitation AGN subset used to define an observational baseline for future resolved-kinematic measurements, not an escape or recycling result.}
\label{fig:m2-p1-outflow-escape-recycling}
\end{figure}


\subsection{Radio-jet environment baseline: optical AGN fraction vs. 10th-neighbor index in massive hosts}
This subsection defines the environment-stratified optical denominator that future radio and X-ray work could test. The 10th-neighbor index is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has an optical AGN fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item radio jet morphology and age
\item cavity or shock energetics
\item hot-gas density
\item calibrated jet-power estimates
\end{itemize}
These are still needed for a future radio-jet test \citep{best2005,mcnamara2007,heckmanbest2014}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
\caption{SDSS optical emission-line denominator: the high- and low-density quartile comparison among massive SDSS hosts, used as a baseline for future radio-jet and X-ray work, not a coupling measurement.}
\label{fig:m2-p2-radio-jet-environment}
\end{figure}


\subsection{Mass-bin diagnostic: low-sSFR and optical AGN incidence}
This subsection identifies the mass bin where a future gas-inclusive study should look for an incidence change. It measures the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the optical AGN fraction peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item gas fractions
\item baryon deficits
\item halo masses
\item stellar-feedback observables
\item high-redshift extensions
\end{itemize}
The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. In this optical-emission-line denominator, the 11.0--12.5 dex peak is a selection-function artifact: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and optical AGN incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up, not a physical transition-mass measurement. The 11.0--12.5 dex peak is a selection-function artifact in this emission-line cache, not a universal feedback threshold.}
\label{fig:m2-p3-feedback-transition-mass}
\end{figure}


\subsection{Tracer-threshold census for multiphase follow-up}
This subsection compares optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item ionized, molecular, and neutral tracers
\item X-ray or radio tracers
\item a shared parent denominator
\item a consistent aperture model
\end{itemize}
These are still needed for a future multiphase test \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work, not a molecular or neutral gas census.}
\label{fig:m3-p1-multiphase-census}
\end{figure}


\subsection{Gas-depletion denominator: optical baseline for CO/HI follow-up}
This subsection defines the denominator for CO/HI gas-fraction and depletion-time follow-up. The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item CO or dust-based molecular gas masses
\item aperture-matched SFRs
\item morphology
\item environment labels
\end{itemize}
These are still needed for a future gas-fraction or depletion-time test \citep{xcoldgass2017,xgass2018,piotrowska2022}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
\caption{SDSS optical emission-line denominator: the massive low-sSFR SDSS galaxies available for CO/HI depletion-time follow-up, not a gas-depletion-efficiency measurement.}
\label{fig:m3-p2-gas-depletion-efficiency}
\end{figure}


\subsection{Simulation target vector for forward-model comparison}
This subsection provides a compact observed target vector for forward modelling, not a direct simulation comparison. The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item simulation mocks passed through the same optical S/N and fiber-aperture selection function used here, then through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions
\item aperture models
\item noise models
\end{itemize}
Without those matched selection steps, any simulation comparison is not a valid test. These are still needed for a future simulation-comparison test \citep{simba2019,tng2019,eagle2015}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
\caption{SDSS optical emission-line denominator: low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift in the SDSS emission-line sample. This is an observed target vector for forward modelling, not a direct simulation comparison.}
\label{fig:m3-p3-simulation-validation}
\end{figure}

\section{Atlas summary}
Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight notes. All eight notes are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or mock-observation data are added, so their present role is to organize follow-up rather than to establish causal physical claims.

\begin{deluxetable*}{llll}
\tabletypesize{\scriptsize}
\tablecaption{Atlas-level follow-up menu. Each row summarizes the present optical role and the missing observables needed before any physical inference.\label{tab:atlas-summary}}
\tablehead{\colhead{Topic} & \colhead{Observed baseline} & \colhead{Missing observables} & \colhead{Role}}
\startdata
Environment & low-sSFR vs.\ 10th-neighbor rank & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test \\
Maintenance heating & optical AGN in massive low-sSFR hosts & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
Outflow kinematics & high-excitation AGN subset & resolved velocities; halo potentials; multiphase gas; CGM tracers & kinematic follow-up \\
Env.\ jets & density-stratified AGN fraction & radio morphology/age; cavity energetics; hot-gas density & radio-jet follow-up \\
Mass bin & low-sSFR and AGN by $M_\star$ bin & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
Tracer census & tracer prevalence in 60k sample & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
Gas depletion & massive low-sSFR baseline; H$\alpha$ proxy & CO/dust gas masses; aperture-matched SFRs; morphology; environment & CO/HI follow-up \\
Simulation vector & mass-redshift target vector & mocks through SDSS/MaNGA/ALMA/X-ray/radio selection; aperture/noise models & forward model \\
\enddata
\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}


\section{Package decision}
These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.

\section{Local reproducibility}
This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\end{thebibliography}

\end{document}

codex
I’ve got the main content. Next I’m cross-checking the exact numeric claims and looking for any language that could drift from “association only” into causal or feedback claims. After that I’ll summarize the concrete edits the integrator should make.
exec
/bin/zsh -lc "rg -n \"8,146|1\\.309|1\\.334|1\\.283|60k|60,000|249,917|24\\.0%|24\\.0|249917|strict parent|association|causal|feedback|quench|quenching|Seyfert|LINER|retired|broad optical BPT|broad BPT AGN|N II|\\[-1\\.334,-1\\.283\\]\" .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, capped 60k-row pilot cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, indicating that the result depends on the chosen emission-line denominator and on the exclusion of LINER-like, retired, bulge-dominated hosts with weak central star formation. An accompanying supplementary denominator/proxy atlas collects the related baselines, selection caveats, and missing-observable notes.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:19:This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a strong negative sSFR offset within the cached denominator analyzed here. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:20:This paper does not attempt to normalize the capped 60k-row cache into a volume-complete luminosity or mass function.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:22:The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:25:The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:28:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a capped 60k-row pilot cache selected sequentially by \texttt{specObjID} after an arbitrary pilot-query row limit; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the pilot cache covers 24.0\% of that strict parent. Because the cap is arbitrary and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:35:\tablecaption{Selection cascade for the flagship denominator. The 60k-row pilot cache is an artificial pilot-query cap, not a physical selection effect.\label{tab:selection}}
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:41:four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:42:four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:52:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical BPT galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:57:\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:63:A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR within this fiber-centered matched comparison, but this manuscript does not convert that proxy offset into a global quenching threshold.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:71:Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:75:N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:77:\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:83:\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT-selected galaxies minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:89:Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including low-ionization nuclear emission-line region (LINER)-like emission from retired stellar populations and post-AGB stars in massive bulges, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global quenching signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this capped 60k-row pilot cache. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:92:RP-1 is best treated as a concise, selection-aware association paper, not a causal study. An accompanying supplementary denominator/proxy atlas holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex:93:In practice, that means future work needs the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation-mock comparisons \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,piotrowska2022,wetzel2013,dekel2006}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:13:This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. The cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:19:The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. Keeping the notes in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:22:The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:34:four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:35:four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:45:This subsection presents an internal environmental baseline that can later be joined to group catalogs and halo masses. Within this selection-biased emission-line denominator, the 10th-neighbor index covaries with the catalog low-sSFR fraction; this index is only an internal ordinal rank and does not map to physical environmental volume density or halo density. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the required missing multiwavelength observables for physical inference are:
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:60:\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up, not a physical-feedback measurement.}
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:61:\label{fig:m1-rp2-environment-quenching}
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:84:This subsection isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The required missing multiwavelength observables for physical inference are:
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:125:\item stellar-feedback observables
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:128:The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. In this optical-emission-line denominator, the 11.0--12.5 dex peak is a selection-function artifact: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:133:\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and optical AGN incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up, not a physical transition-mass measurement. The 11.0--12.5 dex peak is a selection-function artifact in this emission-line cache, not a universal feedback threshold.}
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:134:\label{fig:m2-p3-feedback-transition-mass}
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:139:This subsection compares optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The required missing multiwavelength observables for physical inference are:
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:151:\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work, not a molecular or neutral gas census.}
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:191:Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight notes. All eight notes are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or mock-observation data are added, so their present role is to organize follow-up rather than to establish causal physical claims.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:202:Mass bin & low-sSFR and AGN by $M_\star$ bin & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:203:Tracer census & tracer prevalence in 60k sample & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:212:These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.

exec
/bin/zsh -lc "rg -n \"8,146|1\\.309|1\\.334|1\\.283|60,000|249,917|24\\.0%|strict parent|association-only|association result|causal claim|not a causal|quenching|feedback\" .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/PACKAGE_AUDIT.md .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:25:- The other 8 are useful, but they are not 8 independent causal physical-feedback papers with the current SDSS-only data.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:84:- Main number: 8,146 matched pairs, median delta log sSFR = -1.309 dex, bootstrap interval [-1.334, -1.283] dex.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:85:- Guard: association only, not causal AGN feedback.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:86:- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:115:1. `m1_rp2_environment_quenching` — density proxy / environment denominator, not halo/group quenching proof.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:119:5. `m2_p3_feedback_transition_mass` — mass-vector optical incidence diagnostic, not causal transition-mass physics.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:159:1. Read the polished RP-1 PDF for scientific wording, especially whether the association-only claim is clear enough.

codex
I have the main risk points, but I want the compile side pinned down before I write the review. I’m checking the local compile logs and figure inventory to separate harmless AASTeX warnings from anything that could break reproducibility or the PDF build.
exec
/bin/zsh -lc "rg --files .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package | rg 'compile\\.log"'$|'"\\.pdf"'$|figures?/|'"\\.png"'$|'"\\.jpg"'$|'"\\.eps"'$'"'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/figures/fig-matched-offsets.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/figures/fig-bpt.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/figures/topic-02.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/figures/topic-03.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/figures/topic-01.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/figures/topic-04.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/figures/topic-05.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/figures/topic-07.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/figures/topic-06.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/figures/topic-08.pdf
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf

exec
/bin/zsh -lc "sed -n '1,220p' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log && printf '\\n--- SUPP LOG ---\\n' && sed -n '1,260p' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
note: Running TeX ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
note: Rerunning TeX because "rp1_flagship_polished.aux" changed ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
note: Rerunning TeX because "rp1_flagship_polished.aux" changed ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: rp1_flagship_polished.tex:25: Underfull \hbox (badness 1342) in paragraph at lines 24--25
warning: rp1_flagship_polished.tex:86: Underfull \hbox (badness 10000) in paragraph at lines 85--86
warning: warnings were issued by the TeX engine; use --print and/or --keep-logs for details.
note: Running xdvipdfmx ...
note: Writing `rp1_flagship_polished.pdf` (231.2958984375 KiB)
note: Skipped writing 2 intermediate files (use --keep-intermediates to keep them)

--- SUPP LOG ---
note: Running TeX ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232
note: Rerunning TeX because "supplementary_denominator_atlas.out" changed ...
warning: lineno.sty:296: Invalid UTF-8 byte or sequence at line 296 replaced by U+FFFD.
warning: supplementary_denominator_atlas.tex:43: Underfull \hbox (badness 1701) in paragraph at lines 42--43
warning: supplementary_denominator_atlas.tex:47: Underfull \hbox (badness 1337) in paragraph at lines 46--47
warning: supplementary_denominator_atlas.tex:100: Underfull \hbox (badness 2042) in paragraph at lines 99--100
warning: supplementary_denominator_atlas.tex:159: Underfull \hbox (badness 1062) in paragraph at lines 158--159
warning: supplementary_denominator_atlas.tex:186: Underfull \hbox (badness 2057) in paragraph at lines 185--186
warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 10000) in paragraph at lines 215--216
warning: supplementary_denominator_atlas.tex:216: Underfull \hbox (badness 6300) in paragraph at lines 215--216
warning: supplementary_denominator_atlas.tex:232: Underfull \hbox (badness 10000) in paragraph at lines 231--232
warning: warnings were issued by the TeX engine; use --print and/or --keep-logs for details.
note: Running xdvipdfmx ...
note: Writing `supplementary_denominator_atlas.pdf` (514.7802734375 KiB)
note: Skipped writing 2 intermediate files (use --keep-intermediates to keep them)

codex
I have the compile logs now: both PDFs build cleanly with warnings only, so the remaining work is prose and guardrail review. I’m pulling line numbers for the specific passages that are most likely to need tightening or could be misread as causal/feedback claims.
exec
/bin/zsh -lc "nl -ba .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex | sed -n '1,180p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Selection-aware SDSS BPT/sSFR study}
     5	\shortauthors{NebulaMind}
     6	\begin{document}
     7	
     8	\title{Broad Optical BPT Galaxies and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Study}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, capped 60k-row pilot cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, indicating that the result depends on the chosen emission-line denominator and on the exclusion of LINER-like, retired, bulge-dominated hosts with weak central star formation. An accompanying supplementary denominator/proxy atlas collects the related baselines, selection caveats, and missing-observable notes.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}
    17	
    18	\section{Question and claim boundary}
    19	This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a strong negative sSFR offset within the cached denominator analyzed here. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
    20	This paper does not attempt to normalize the capped 60k-row cache into a volume-complete luminosity or mass function.
    21	
    22	The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.
    23	
    24	\subsection{Scope and limitations}
    25	The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.
    26	
    27	\section{Data and shared selection}
    28	The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a capped 60k-row pilot cache selected sequentially by \texttt{specObjID} after an arbitrary pilot-query row limit; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the pilot cache covers 24.0\% of that strict parent. Because the cap is arbitrary and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
    29	Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
    30	Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy that can differ systematically between bulge-dominated and disk-dominated systems.
    31	The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.
    32	
    33	\begin{deluxetable*}{lrrr}
    34	\tabletypesize{\scriptsize}
    35	\tablecaption{Selection cascade for the flagship denominator. The 60k-row pilot cache is an artificial pilot-query cap, not a physical selection effect.\label{tab:selection}}
    36	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    37	\startdata
    38	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
    39	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
    40	plus galSpecLine join & 416,554 & -- & 83.1\% \\
    41	four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
    42	four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
    43	four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
    44	four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
    45	\enddata
    46	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies.}
    47	\end{deluxetable*}
    48	
    49	The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.
    50	
    51	\section{Classification and matching}
    52	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical BPT galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
    53	
    54	\begin{figure*}
    55	\centering
    56	\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
    57	\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
    58	\label{fig:bpt}
    59	\end{figure*}
    60	
    61	\section{Matched-control result}
    62	The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the broad BPT-selected galaxies relative to star-forming controls.
    63	A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR within this fiber-centered matched comparison, but this manuscript does not convert that proxy offset into a global quenching threshold.
    64	Because the comparison is fiber-centered and the matching ignores morphology, the measured offset is a relative difference between the broad-BPT and control samples within the fiber aperture. It can therefore reflect the known bulge/disk mismatch between broad-BPT hosts and star-forming controls rather than a galaxy-wide suppression signal.
    65	
    66	\begin{deluxetable*}{lrrrr}
    67	\tabletypesize{\scriptsize}
    68	\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
    69	\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
    70	\startdata
    71	Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
    72	Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
    73	Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
    74	Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
    75	N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; excludes retired/LINER-like bulges \\
    76	\enddata
    77	\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects the narrower emission-line denominator and the removal of a LINER-like, retired, bulge-dominated tail by construction. All values are conditional on the optical emission-line denominator.}
    78	\end{deluxetable*}
    79	
    80	\begin{figure*}
    81	\centering
    82	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    83	\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT-selected galaxies minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
    84	\label{fig:offsets}
    85	\end{figure*}
    86	
    87	\section{Interpretation}
    88	The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper.
    89	Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including low-ionization nuclear emission-line region (LINER)-like emission from retired stellar populations and post-AGB stars in massive bulges, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global quenching signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this capped 60k-row pilot cache. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
    90	
    91	\section{Conclusion}
    92	RP-1 is best treated as a concise, selection-aware association paper, not a causal study. An accompanying supplementary denominator/proxy atlas holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
    93	In practice, that means future work needs the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation-mock comparisons \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,piotrowska2022,wetzel2013,dekel2006}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.
    94	
    95	\section{Local reproducibility}
    96	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
    97	
    98	
    99	\begin{thebibliography}{}
   100	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   101	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   102	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   103	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   104	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   105	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   106	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   107	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   108	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   109	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   110	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   111	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   112	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   113	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   114	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   115	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   116	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   117	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   118	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   119	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   120	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   121	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   122	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   123	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   124	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   125	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   126	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   127	\end{thebibliography}
   128	
   129	\end{document}

exec
/bin/zsh -lc "nl -ba .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | sed -n '1,280p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS denominator/proxy atlas}
     5	\shortauthors{NebulaMind}
     6	\begin{document}
     7	
     8	\title{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. The cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}
    17	
    18	\section{Purpose}
    19	The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. Keeping the notes in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.
    20	
    21	\section{Shared denominator}
    22	The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}. The SDSS/BPT/catalog references support these observed denominators; the later multiwavelength and simulation references only mark the follow-up measurements that are still missing.
    23	
    24	The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.
    25	
    26	\begin{deluxetable*}{lrrr}
    27	\tabletypesize{\scriptsize}
    28	\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
    29	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    30	\startdata
    31	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
    32	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
    33	plus galSpecLine join & 416,554 & -- & 83.1\% \\
    34	four BPT lines positive with positive errors & 373,445 & 60,000 & 74.5\% \\
    35	four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
    36	four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
    37	four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
    38	\enddata
    39	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
    40	\end{deluxetable*}
    41	
    42	\section{Atlas notes}
    43	
    44	\subsection{Environment baseline: SDSS 10th-neighbor index for low-sSFR incidence}
    45	This subsection presents an internal environmental baseline that can later be joined to group catalogs and halo masses. Within this selection-biased emission-line denominator, the 10th-neighbor index covaries with the catalog low-sSFR fraction; this index is only an internal ordinal rank and does not map to physical environmental volume density or halo density. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the required missing multiwavelength observables for physical inference are:
    46	\begin{itemize}
    47	\item group catalogues
    48	\item robust central/satellite labels
    49	\item halo masses
    50	\item spectroscopic fiber-collision correction at the 55-arcsec scale
    51	\item morphology
    52	\item multi-redshift selection functions
    53	\end{itemize}
    54	Within this selection-biased emission-line cache, the 10th-neighbor statistic is only a relative local rank, not a physical volume density and not a substitute for central/satellite labels or a volume-complete halo-density measurement.
    55	These are still needed for a future environmental test \citep{peng2010,wetzel2013,dekel2006}.
    56	
    57	\begin{figure}
    58	\centering
    59	\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
    60	\caption{SDSS optical emission-line denominator: the low-sSFR emission-line fraction as a function of the 10th-neighbor index in the SDSS emission-line sample. This is a selection-dependent baseline for future group- and halo-matched follow-up, not a physical-feedback measurement.}
    61	\label{fig:m1-rp2-environment-quenching}
    62	\end{figure}
    63	
    64	
    65	\subsection{Maintenance-heating denominator: optical AGN in massive SDSS hosts}
    66	This subsection identifies the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The required missing multiwavelength observables for physical inference are:
    67	\begin{itemize}
    68	\item X-ray cavity or cooling-luminosity measurements
    69	\item radio jet powers
    70	\item halo-selected parent catalogues
    71	\item nondetection modelling
    72	\end{itemize}
    73	These are still needed for a future maintenance-heating test \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.
    74	
    75	\begin{figure}
    76	\centering
    77	\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
    78	\caption{SDSS optical emission-line denominator: the massive and low-sSFR SDSS emission-line subsets used as a baseline for future X-ray and radio measurements, not a heating-to-cooling result.}
    79	\label{fig:m1-rp3-maintenance-heating}
    80	\end{figure}
    81	
    82	
    83	\subsection{Outflow-kinematics denominator: high-excitation SDSS AGN}
    84	This subsection isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The required missing multiwavelength observables for physical inference are:
    85	\begin{itemize}
    86	\item resolved outflow velocities
    87	\item halo potentials
    88	\item molecular, ionized, and neutral gas phases
    89	\item CGM recycling tracers
    90	\end{itemize}
    91	These are still needed for a future outflow test \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.
    92	
    93	\begin{figure}
    94	\centering
    95	\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
    96	\caption{SDSS optical emission-line denominator: the high-excitation AGN subset used to define an observational baseline for future resolved-kinematic measurements, not an escape or recycling result.}
    97	\label{fig:m2-p1-outflow-escape-recycling}
    98	\end{figure}
    99	
   100	
   101	\subsection{Radio-jet environment baseline: optical AGN fraction vs. 10th-neighbor index in massive hosts}
   102	This subsection defines the environment-stratified optical denominator that future radio and X-ray work could test. The 10th-neighbor index is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has an optical AGN fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The required missing multiwavelength observables for physical inference are:
   103	\begin{itemize}
   104	\item radio jet morphology and age
   105	\item cavity or shock energetics
   106	\item hot-gas density
   107	\item calibrated jet-power estimates
   108	\end{itemize}
   109	These are still needed for a future radio-jet test \citep{best2005,mcnamara2007,heckmanbest2014}.
   110	
   111	\begin{figure}
   112	\centering
   113	\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
   114	\caption{SDSS optical emission-line denominator: the high- and low-density quartile comparison among massive SDSS hosts, used as a baseline for future radio-jet and X-ray work, not a coupling measurement.}
   115	\label{fig:m2-p2-radio-jet-environment}
   116	\end{figure}
   117	
   118	
   119	\subsection{Mass-bin diagnostic: low-sSFR and optical AGN incidence}
   120	This subsection identifies the mass bin where a future gas-inclusive study should look for an incidence change. It measures the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the optical AGN fraction peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The required missing multiwavelength observables for physical inference are:
   121	\begin{itemize}
   122	\item gas fractions
   123	\item baryon deficits
   124	\item halo masses
   125	\item stellar-feedback observables
   126	\item high-redshift extensions
   127	\end{itemize}
   128	The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}. In this optical-emission-line denominator, the 11.0--12.5 dex peak is a selection-function artifact: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold.
   129	
   130	\begin{figure}
   131	\centering
   132	\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
   133	\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and optical AGN incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up, not a physical transition-mass measurement. The 11.0--12.5 dex peak is a selection-function artifact in this emission-line cache, not a universal feedback threshold.}
   134	\label{fig:m2-p3-feedback-transition-mass}
   135	\end{figure}
   136	
   137	
   138	\subsection{Tracer-threshold census for multiphase follow-up}
   139	This subsection compares optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The required missing multiwavelength observables for physical inference are:
   140	\begin{itemize}
   141	\item ionized, molecular, and neutral tracers
   142	\item X-ray or radio tracers
   143	\item a shared parent denominator
   144	\item a consistent aperture model
   145	\end{itemize}
   146	These are still needed for a future multiphase test \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.
   147	
   148	\begin{figure}
   149	\centering
   150	\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
   151	\caption{SDSS optical emission-line denominator: prevalence of alternative tracer definitions within the 60,000-galaxy sample. This is a baseline for future multiphase work, not a molecular or neutral gas census.}
   152	\label{fig:m3-p1-multiphase-census}
   153	\end{figure}
   154	
   155	
   156	\subsection{Gas-depletion denominator: optical baseline for CO/HI follow-up}
   157	This subsection defines the denominator for CO/HI gas-fraction and depletion-time follow-up. The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The required missing multiwavelength observables for physical inference are:
   158	\begin{itemize}
   159	\item CO or dust-based molecular gas masses
   160	\item aperture-matched SFRs
   161	\item morphology
   162	\item environment labels
   163	\end{itemize}
   164	These are still needed for a future gas-fraction or depletion-time test \citep{xcoldgass2017,xgass2018,piotrowska2022}.
   165	
   166	\begin{figure}
   167	\centering
   168	\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
   169	\caption{SDSS optical emission-line denominator: the massive low-sSFR SDSS galaxies available for CO/HI depletion-time follow-up, not a gas-depletion-efficiency measurement.}
   170	\label{fig:m3-p2-gas-depletion-efficiency}
   171	\end{figure}
   172	
   173	
   174	\subsection{Simulation target vector for forward-model comparison}
   175	This subsection provides a compact observed target vector for forward modelling, not a direct simulation comparison. The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The required missing multiwavelength observables for physical inference are:
   176	\begin{itemize}
   177	\item simulation mocks passed through the same optical S/N and fiber-aperture selection function used here, then through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions
   178	\item aperture models
   179	\item noise models
   180	\end{itemize}
   181	Without those matched selection steps, any simulation comparison is not a valid test. These are still needed for a future simulation-comparison test \citep{simba2019,tng2019,eagle2015}.
   182	
   183	\begin{figure}
   184	\centering
   185	\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
   186	\caption{SDSS optical emission-line denominator: low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift in the SDSS emission-line sample. This is an observed target vector for forward modelling, not a direct simulation comparison.}
   187	\label{fig:m3-p3-simulation-validation}
   188	\end{figure}
   189	
   190	\section{Atlas summary}
   191	Table~\ref{tab:atlas-summary} condenses the follow-up menu across the eight notes. All eight notes are linked by the same limitation: they remain SDSS optical denominators or target vectors until the missing multiwavelength, morphological, or mock-observation data are added, so their present role is to organize follow-up rather than to establish causal physical claims.
   192	
   193	\begin{deluxetable*}{llll}
   194	\tabletypesize{\scriptsize}
   195	\tablecaption{Atlas-level follow-up menu. Each row summarizes the present optical role and the missing observables needed before any physical inference.\label{tab:atlas-summary}}
   196	\tablehead{\colhead{Topic} & \colhead{Observed baseline} & \colhead{Missing observables} & \colhead{Role}}
   197	\startdata
   198	Environment & low-sSFR vs.\ 10th-neighbor rank & group catalogs; central/satellite labels; halo mass; fiber-collision correction & environment test \\
   199	Maintenance heating & optical AGN in massive low-sSFR hosts & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow-up \\
   200	Outflow kinematics & high-excitation AGN subset & resolved velocities; halo potentials; multiphase gas; CGM tracers & kinematic follow-up \\
   201	Env.\ jets & density-stratified AGN fraction & radio morphology/age; cavity energetics; hot-gas density & radio-jet follow-up \\
   202	Mass bin & low-sSFR and AGN by $M_\star$ bin & gas fractions; baryon deficits; halo masses; feedback observables & selection diagnostic \\
   203	Tracer census & tracer prevalence in 60k sample & multiphase tracers; shared denominator; aperture model & multiphase follow-up \\
   204	Gas depletion & massive low-sSFR baseline; H$\alpha$ proxy & CO/dust gas masses; aperture-matched SFRs; morphology; environment & CO/HI follow-up \\
   205	Simulation vector & mass-redshift target vector & mocks through SDSS/MaNGA/ALMA/X-ray/radio selection; aperture/noise models & forward model \\
   206	\enddata
   207	\tablecomments{The table is a compact index of the subsection-level missing-observables lists; it does not add new measurements or change any counts. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
   208	\end{deluxetable*}
   209	
   210	
   211	\section{Package decision}
   212	These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.
   213	
   214	\section{Local reproducibility}
   215	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
   216	
   217	
   218	\begin{thebibliography}{}
   219	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   220	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   221	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   222	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   223	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   224	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   225	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   226	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   227	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   228	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   229	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   230	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   231	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   232	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   233	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   234	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   235	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   236	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   237	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   238	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   239	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   240	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   241	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   242	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   243	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   244	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   245	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   246	\end{thebibliography}
   247	
   248	\end{document}

codex
I’ve narrowed the actual guardrail-sensitive wording. I’m doing one last pass for hidden encoding or figure-path issues, because those are the only remaining reproducibility risks that could still bite a clean-looking build.
exec
/bin/zsh -lc 'LC_ALL=C grep -nP "[''^'"\\x00-\\x7F]\" .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
 exited 2 in 0ms:
grep: invalid option -- P
usage: grep [-abcdDEFGHhIiJLlMmnOopqRSsUVvwXxZz] [-A num] [-B num] [-C[num]]
	[-e pattern] [-f file] [--binary-files=value] [--color=when]
	[--context[=num]] [--directories=action] [--label] [--line-buffered]
	[--null] [pattern] [file ...]

exec
/bin/zsh -lc "sed -n '1,220p' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/README.md && printf '\\n--- MANIFEST ---\\n' && sed -n '1,260p' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/PACKAGE_MANIFEST_PRECOMPILE.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z

Decision package: one polished RP-1 flagship draft plus one supplementary denominator/proxy atlas.

Compile with Tectonic from each aastex directory, then run package audit.

--- MANIFEST ---
{
  "created_utc": "2026-07-09T01:40:44Z",
  "decision": "one polished RP-1 flagship draft plus one supplementary denominator/proxy atlas for the other eight",
  "flagship": {
    "expected_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.pdf",
    "figures": [
      {
        "bytes": 86693,
        "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/figures/fig-bpt.pdf",
        "sha256": "99cc2411c43dcd41895d6cb55234648a8b8ffc498eaf8ffeea8ec534c119b999",
        "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf"
      },
      {
        "bytes": 78775,
        "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/figures/fig-matched-offsets.pdf",
        "sha256": "83d16bcbeada88091c5c68a4fd98fd96af9d3b8971bd361a55d0f1b16ca95661",
        "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf"
      }
    ],
    "slug": "m1_rp1_sdss_agn_sfr",
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/flagship_rp1/aastex/rp1_flagship_polished.tex"
  },
  "package_id": "RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z",
  "safety": "local-only files under handoff tree; no public/live/wiki/DB/deploy/git/cron/billing/OAuth/external submission changes",
  "source_integration_run": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z",
  "supplement": {
    "expected_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf",
    "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex",
    "topics": [
      {
        "fig_name": "topic-01.pdf",
        "figure": {
          "bytes": 14881,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-01.pdf",
          "sha256": "1fd192eed0643ae73b54e06c311117fb6c3241c1f952bade758e56e32fe02d9f",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/02_m1_rp2_environment_quenching/figures/fig-topic.pdf"
        },
        "label": "m1-rp2-environment-quenching",
        "slug": "m1_rp2_environment_quenching",
        "status": "guarded proxy/denominator draft",
        "title": "SDSS density proxy for environmental quenching: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-02.pdf",
        "figure": {
          "bytes": 14966,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-02.pdf",
          "sha256": "596db86bacb484ebec5750f3ef41ceb490d5b7c8a870b0c5cb4638f2aab92fe8",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf"
        },
        "label": "m1-rp3-maintenance-heating",
        "slug": "m1_rp3_maintenance_heating",
        "status": "guarded proxy/denominator draft",
        "title": "Optical-AGN denominator for maintenance-heating follow-up: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-03.pdf",
        "figure": {
          "bytes": 247680,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-03.pdf",
          "sha256": "31e5c88cd1e02bf868b18000814317477bbdf14cbbbb95b8f1708f0f107f4670",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf"
        },
        "label": "m2-p1-outflow-escape-recycling",
        "slug": "m2_p1_outflow_escape_recycling",
        "status": "guarded proxy/denominator draft",
        "title": "SDSS high-excitation AGN denominator for outflow escape tests: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-04.pdf",
        "figure": {
          "bytes": 15267,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-04.pdf",
          "sha256": "8bd1b0248cf0939fb2ba0a64155586b3f13a0dc2eff581e2ab63ae750481694c",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf"
        },
        "label": "m2-p2-radio-jet-environment",
        "slug": "m2_p2_radio_jet_environment",
        "status": "guarded proxy/denominator draft",
        "title": "Environment proxy for optical AGN in massive SDSS hosts: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-05.pdf",
        "figure": {
          "bytes": 14913,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-05.pdf",
          "sha256": "725dfb62948db7d4b868eef7b18ba9739ad814d821cc507d3a19c53c556943f9",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf"
        },
        "label": "m2-p3-feedback-transition-mass",
        "slug": "m2_p3_feedback_transition_mass",
        "status": "guarded proxy/denominator draft",
        "title": "SDSS mass transition in quenching and optical AGN incidence: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-06.pdf",
        "figure": {
          "bytes": 16341,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-06.pdf",
          "sha256": "abfc743a35167e4247288ffe0571531f839989078861f94c2fa49ed9914d79f2",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/07_m3_p1_multiphase_census/figures/fig-topic.pdf"
        },
        "label": "m3-p1-multiphase-census",
        "slug": "m3_p1_multiphase_census",
        "status": "guarded proxy/denominator draft",
        "title": "Common-denominator optical tracer census in SDSS: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-07.pdf",
        "figure": {
          "bytes": 139945,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-07.pdf",
          "sha256": "a20bf97de10b49f6c662f5e6c7f403d935b8615abf1c8dc9daddc7174f861d4a",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf"
        },
        "label": "m3-p2-gas-depletion-efficiency",
        "slug": "m3_p2_gas_depletion_efficiency",
        "status": "guarded proxy/denominator draft",
        "title": "Optical denominator for gas-fraction versus efficiency tests: selection-aware SDSS optical proxy integration"
      },
      {
        "fig_name": "topic-08.pdf",
        "figure": {
          "bytes": 16385,
          "dest": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/decision-package/RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z/supplementary_denominator_atlas/figures/topic-08.pdf",
          "sha256": "eef8a9b385dfb97aa0cef8df24f363712f28140f8988a6a2b6cac169f1b8d61d",
          "source": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z/09_m3_p3_simulation_validation/figures/fig-topic.pdf"
        },
        "label": "m3-p3-simulation-validation",
        "slug": "m3_p3_simulation_validation",
        "status": "guarded proxy/denominator draft",
        "title": "SDSS target vector for feedback-model validation: selection-aware SDSS optical proxy integration"
      }
    ]
  }
}
codex
I hit a tooling limitation on the encoding check, so I’m rerunning it with a plain POSIX-safe scan. The goal is just to confirm whether the UTF-8 warning is likely from the manuscript source or from the TeX toolchain itself.
exec
/bin/zsh -lc "perl -ne 'print \""'$ARGV:$.:$_" if /[''^'"\\x00-\\x7F]/' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
exec
/bin/zsh -lc "perl -ne 'print \""'$ARGV:$.:$_" if /[''^'"\\x00-\\x7F]/' .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/PACKAGE_AUDIT.md .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md .hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/README.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:136:1. `m1_rp2_environment_quenching` — density proxy / environment denominator, not halo/group quenching proof.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:137:2. `m1_rp3_maintenance_heating` — optical AGN denominator, not radio/X-ray maintenance-heating measurement.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:138:3. `m2_p1_outflow_escape_recycling` — high-excitation optical AGN denominator, not outflow escape/recycling measurement.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:139:4. `m2_p2_radio_jet_environment` — optical AGN fraction vs internal density proxy, not radio-jet coupling test.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:140:5. `m2_p3_feedback_transition_mass` — mass-vector optical incidence diagnostic, not causal transition-mass physics.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:141:6. `m3_p1_multiphase_census` — optical tracer-threshold census, not multiphase gas census.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:142:7. `m3_p2_gas_depletion_efficiency` — optical/H-alpha denominator for CO/gas follow-up, not gas depletion-time measurement.
.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/FINAL_HANDOFF.md:143:8. `m3_p3_simulation_validation` — observed SDSS target vector, not simulation validation/rejection.

codex
CODEX_KUN_REVIEW_CYCLE_09

**Findings**
1. Medium: the flagship still has a few causal-quenching phrases that are easy to misread as more than an association statement. The two main ones are `[rp1_flagship_polished.tex:63](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L63)` and `[rp1_flagship_polished.tex:89](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L89)`, where `global quenching threshold`, `global quenching signal`, and `quenching-causality claim` are used. Safe edit: replace those with `galaxy-wide suppression interpretation`, `galaxy-wide suppression signal`, and `association-only follow-up claim` respectively.

2. Medium: the supplementary atlas uses several causal labels in section headings and body text that are guarded, but still fragile if this package is read quickly or repurposed. The most sensitive spots are `[supplementary_denominator_atlas.tex:65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L65)`, `[supplementary_denominator_atlas.tex:83](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L83)`, `[supplementary_denominator_atlas.tex:119](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L119)`, and `[supplementary_denominator_atlas.tex:139](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L139)`. Safe edit: keep the section names denominator-first, and change `feedback-candidate prevalence` to `optical-tracer prevalence`; keep `maintenance-heating`, `outflow`, and `transition mass` only as follow-up labels, not as implied results.

3. Low: the selection-table percentage column is numerically consistent, but the wording can mislead readers about what the percentage is relative to. In both manuscripts, the 24.0% cache coverage is stated correctly for `60,000 / 249,917`, but the table rows at `[rp1_flagship_polished.tex:41-44](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L41)` and `[supplementary_denominator_atlas.tex:34-37](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L34)` read as if the percentages might refer to the cached rows. Safe edit: change the column header to `Public-row retention vs. spectro-z parent` or add `at this stage` so the reader does not confuse public-row retention with cache coverage.

**Numeric consistency**
- Verified consistent for the required set: `8,146` pairs, `-1.309 dex`, `[-1.334,-1.283]`, `60,000` cached rows, `249,917` strict parent, and `24.0%` coverage all match across the flagship, supplement, and handoff docs.
- I did not find a mismatch in those required numbers.
- The only subtlety is the retention table wording, not the arithmetic.

**TeX / Compile**
- Both PDFs compiled successfully from the local package.
- Audit confirms `figures_ok: 10`, `pdfs_ok: 2`, `logs_ok: 2`, `fatal_failures: 0`.
- Build warnings are non-fatal:
  - `lineno.sty:296: Invalid UTF-8 byte or sequence ...`
  - several `Underfull \hbox` warnings in both manuscripts.
- The source files themselves are ASCII-only, so the UTF-8 warning appears toolchain- or aux-file-related rather than a manuscript encoding problem.

**Figure / Reproducibility**
- Figure assets are present in-package and the relative `../figures/*.pdf` paths resolve correctly in the current directory layout.
- Reproducibility is therefore good as long as the `aastex` directory stays paired with its sibling `figures` directory.
- If someone copies only the `.tex` files elsewhere, the build will break on relative figure paths.

**Exact safe edits for the integrator**
- In `[rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex)`, line 63: replace `global quenching threshold` with `galaxy-wide suppression interpretation`.
- In `[rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex)`, line 89: replace `global quenching signal` with `galaxy-wide suppression signal`.
- In `[supplementary_denominator_atlas.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex)`, line 139: replace `feedback-candidate prevalence` with `optical-tracer prevalence`.
- In both selection tables, clarify the percentage header so readers can see it is `public-row retention` and not cache coverage.
- If you want the logs cleaner, run a final pass for any stray generated-aux encoding issue, but do not change the scientific text just to chase the `lineno.sty` warning.

**Safety ledger**
- Read-only review only.
- No edits made.
- No git, deploy, publish, API, credential, or live-root actions.
- Only local manuscript package files under the requested handoff tree were inspected.
tokens used
56,176
CODEX_KUN_REVIEW_CYCLE_09

**Findings**
1. Medium: the flagship still has a few causal-quenching phrases that are easy to misread as more than an association statement. The two main ones are `[rp1_flagship_polished.tex:63](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L63)` and `[rp1_flagship_polished.tex:89](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L89)`, where `global quenching threshold`, `global quenching signal`, and `quenching-causality claim` are used. Safe edit: replace those with `galaxy-wide suppression interpretation`, `galaxy-wide suppression signal`, and `association-only follow-up claim` respectively.

2. Medium: the supplementary atlas uses several causal labels in section headings and body text that are guarded, but still fragile if this package is read quickly or repurposed. The most sensitive spots are `[supplementary_denominator_atlas.tex:65](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L65)`, `[supplementary_denominator_atlas.tex:83](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L83)`, `[supplementary_denominator_atlas.tex:119](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L119)`, and `[supplementary_denominator_atlas.tex:139](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L139)`. Safe edit: keep the section names denominator-first, and change `feedback-candidate prevalence` to `optical-tracer prevalence`; keep `maintenance-heating`, `outflow`, and `transition mass` only as follow-up labels, not as implied results.

3. Low: the selection-table percentage column is numerically consistent, but the wording can mislead readers about what the percentage is relative to. In both manuscripts, the 24.0% cache coverage is stated correctly for `60,000 / 249,917`, but the table rows at `[rp1_flagship_polished.tex:41-44](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L41)` and `[supplementary_denominator_atlas.tex:34-37](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L34)` read as if the percentages might refer to the cached rows. Safe edit: change the column header to `Public-row retention vs. spectro-z parent` or add `at this stage` so the reader does not confuse public-row retention with cache coverage.

**Numeric consistency**
- Verified consistent for the required set: `8,146` pairs, `-1.309 dex`, `[-1.334,-1.283]`, `60,000` cached rows, `249,917` strict parent, and `24.0%` coverage all match across the flagship, supplement, and handoff docs.
- I did not find a mismatch in those required numbers.
- The only subtlety is the retention table wording, not the arithmetic.

**TeX / Compile**
- Both PDFs compiled successfully from the local package.
- Audit confirms `figures_ok: 10`, `pdfs_ok: 2`, `logs_ok: 2`, `fatal_failures: 0`.
- Build warnings are non-fatal:
  - `lineno.sty:296: Invalid UTF-8 byte or sequence ...`
  - several `Underfull \hbox` warnings in both manuscripts.
- The source files themselves are ASCII-only, so the UTF-8 warning appears toolchain- or aux-file-related rather than a manuscript encoding problem.

**Figure / Reproducibility**
- Figure assets are present in-package and the relative `../figures/*.pdf` paths resolve correctly in the current directory layout.
- Reproducibility is therefore good as long as the `aastex` directory stays paired with its sibling `figures` directory.
- If someone copies only the `.tex` files elsewhere, the build will break on relative figure paths.

**Exact safe edits for the integrator**
- In `[rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex)`, line 63: replace `global quenching threshold` with `galaxy-wide suppression interpretation`.
- In `[rp1_flagship_polished.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex)`, line 89: replace `global quenching signal` with `galaxy-wide suppression signal`.
- In `[supplementary_denominator_atlas.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex)`, line 139: replace `feedback-candidate prevalence` with `optical-tracer prevalence`.
- In both selection tables, clarify the percentage header so readers can see it is `public-row retention` and not cache coverage.
- If you want the logs cleaner, run a final pass for any stray generated-aux encoding issue, but do not change the scientific text just to chase the `lineno.sty` warning.

**Safety ledger**
- Read-only review only.
- No edits made.
- No git, deploy, publish, API, credential, or live-root actions.
- Only local manuscript package files under the requested handoff tree were inspected.


# command_result
exit_code=0
elapsed_s=171.4
timed_out=False
finished_utc=2026-07-09T03:57:08Z

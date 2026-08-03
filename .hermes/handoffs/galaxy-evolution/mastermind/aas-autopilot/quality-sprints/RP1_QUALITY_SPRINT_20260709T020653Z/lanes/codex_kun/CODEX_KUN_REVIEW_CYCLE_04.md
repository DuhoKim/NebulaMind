# codex-kun-cycle-4
Started UTC: 2026-07-09T02:34:12Z
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
session id: 019f44b9-c4ae-7c41-bf9c-60ffb4347a8d
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_04.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m inspecting the four package files directly and checking the manuscript against the requested numeric anchors, TeX failure modes, figure references, and reproducibility guardrails. I’ll keep this read-only and report only concrete risks with exact edit guidance for the integrator.
exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/PACKAGE_AUDIT.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
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

exec
/bin/zsh -lc "rg -n --no-heading -e '8,146|8146|-1\\.309|\\[-1\\.334,\\s*-1\\.283\\]|60,000|60000|249,917|249917|24\\.0%|24\\.0\\s*%' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/PACKAGE_AUDIT.md /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/FINAL_HANDOFF.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/FINAL_HANDOFF.md:84:- Main number: 8,146 matched pairs, median delta log sSFR = -1.309 dex, bootstrap interval [-1.334, -1.283] dex.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/FINAL_HANDOFF.md:86:- Required caveat: the cached 60,000-row table is capped/non-random and covers 24.0% of the strict public four-line S/N>=3 parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:13:This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60,000-row optical emission-line cache and the same selection-function caveats. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. It is a single follow-up atlas, not eight independent causal-feedback papers.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:22:The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:34:four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:35:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:44:The follow-up goal here is to isolate an environmental denominator that can later be joined to group catalogs and halo masses. The nearest-neighbour density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions are still needed for a physical environmental interpretation \citep{peng2010,wetzel2013,dekel2006}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:66:The follow-up goal here is to isolate the optical-AGN denominator that resolved kinematics would need to test escape versus recycling. The SDSS high-excitation optical-AGN denominator identifies how many systems would need resolved kinematics to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:100:The follow-up goal here is to compare optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are ionized, molecular, neutral, and X-ray or radio tracers measured over the same parent denominator and aperture model \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex:13:We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, both of which can bias fiber-based sSFR comparisons. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex:24:The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The cached analysis table is capped at 60,000 rows and ordered by \texttt{specObjID}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the cache covers 24.0\% of that strict parent.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex:36:four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex:37:four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex:47:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical AGN host is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex:58:A median $\Delta\log {\rm sSFR}$ of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR, but this manuscript does not convert that proxy offset into a global quenching threshold.
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex:65:Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\

exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/FINAL_HANDOFF.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
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

codex
I’ve confirmed the package-level claims and the exact main numbers. Next I’m checking the manuscript text itself for line-level issues: unescaped TeX hazards, inconsistent denominators, figure references, and any phrasing that could overstep the association-only guardrail.
exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Selection-aware SDSS optical AGN/sSFR pilot}
     5	\shortauthors{NebulaMind}
     6	\begin{document}
     7	
     8	\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Pilot}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{Public SDSS DR17 data only}
    11	
    12	\begin{abstract}
    13	We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, both of which can bias fiber-based sSFR comparisons. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}
    17	
    18	\section{Question and claim boundary}
    19	This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish causal AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
    20	
    21	The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and LINER-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.
    22	
    23	\section{Data and shared selection}
    24	The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The cached analysis table is capped at 60,000 rows and ordered by \texttt{specObjID}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the cache covers 24.0\% of that strict parent.
    25	Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
    26	The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Selection cascade for the flagship denominator.\label{tab:selection}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Cached-versus-public marginal checks show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.
    45	
    46	\section{Classification and matching}
    47	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical AGN host is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
    48	
    49	\begin{figure*}
    50	\centering
    51	\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
    52	\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
    53	\label{fig:bpt}
    54	\end{figure*}
    55	
    56	\section{Matched-control result}
    57	The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the optical AGN hosts relative to star-forming controls.
    58	A median $\Delta\log {\rm sSFR}$ of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR, but this manuscript does not convert that proxy offset into a global quenching threshold.
    59	
    60	\begin{deluxetable*}{lrrrr}
    61	\tabletypesize{\scriptsize}
    62	\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
    63	\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
    64	\startdata
    65	Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
    66	Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
    67	Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
    68	Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
    69	N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity \\
    70	\enddata
    71	\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. All values are conditional on the optical emission-line denominator.}
    72	\end{deluxetable*}
    73	
    74	\begin{figure*}
    75	\centering
    76	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    77	\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT AGN hosts minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions.}
    78	\label{fig:offsets}
    79	\end{figure*}
    80	
    81	\section{Interpretation}
    82	The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude to roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including LINER-like ionization from retired stellar populations and post-AGB stars, rather than identifying a different physical mechanism. The most robust conclusion is therefore: broad optical BPT AGN classification is associated with lower catalog sSFR in this capped SDSS emission-line sample. Claims about causal quenching require additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
    83	
    84	\section{Conclusion}
    85	RP-1 is best treated as a concise, selection-aware association paper. Related topic notes belong in a supplementary denominator/proxy atlas until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
    86	In practice, that means future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; they are not part of the present SDSS-only denominator.
    87	
    88	\section{Local reproducibility}
    89	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
    90	
    91	
    92	\begin{thebibliography}{}
    93	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    94	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    95	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    96	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    97	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
    98	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
    99	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   100	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   101	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   102	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   103	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   104	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   105	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   106	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   107	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   108	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   109	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   110	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   111	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   112	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   113	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   114	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   115	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   116	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   117	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   118	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   119	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   120	\end{thebibliography}
   121	
   122	\end{document}

exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | sed -n '1,260p'" in /Users/duhokim/NebulaMind/NebulaMind
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
    13	This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60,000-row optical emission-line cache and the same selection-function caveats. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. It is a single follow-up atlas, not eight independent causal-feedback papers.
    14	\end{abstract}
    15	
    16	\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}
    17	
    18	\section{Purpose}
    19	The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. Keeping them in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.
    20	
    21	\section{Shared denominator}
    22	The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}.
    23	
    24	The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.
    25	
    26	\begin{deluxetable*}{lrrr}
    27	\tabletypesize{\scriptsize}
    28	\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
    29	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    30	\startdata
    31	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    32	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    33	plus galSpecLine join & 416,554 & -- & 0.831 \\
    34	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    35	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    36	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    37	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    38	\enddata
    39	\end{deluxetable*}
    40	
    41	\section{Atlas notes}
    42	
    43	\subsection{SDSS density proxy for low-sSFR incidence}
    44	The follow-up goal here is to isolate an environmental denominator that can later be joined to group catalogs and halo masses. The nearest-neighbour density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions are still needed for a physical environmental interpretation \citep{peng2010,wetzel2013,dekel2006}.
    45	
    46	\begin{figure}
    47	\centering
    48	\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
    49	\caption{SDSS optical denominator/proxy diagnostic for m1\_rp2\_environment\_quenching. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    50	\label{fig:m1-rp2-environment-quenching}
    51	\end{figure}
    52	
    53	
    54	\subsection{Optical-AGN denominator for maintenance-heating follow-up}
    55	The follow-up goal here is to identify the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can be used as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The missing observables are X-ray cavity or cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.
    56	
    57	\begin{figure}
    58	\centering
    59	\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
    60	\caption{SDSS optical denominator/proxy diagnostic for m1\_rp3\_maintenance\_heating. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    61	\label{fig:m1-rp3-maintenance-heating}
    62	\end{figure}
    63	
    64	
    65	\subsection{SDSS high-excitation AGN denominator for outflow tests}
    66	The follow-up goal here is to isolate the optical-AGN denominator that resolved kinematics would need to test escape versus recycling. The SDSS high-excitation optical-AGN denominator identifies how many systems would need resolved kinematics to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.
    67	
    68	\begin{figure}
    69	\centering
    70	\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
    71	\caption{SDSS optical denominator/proxy diagnostic for m2\_p1\_outflow\_escape\_recycling. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    72	\label{fig:m2-p1-outflow-escape-recycling}
    73	\end{figure}
    74	
    75	
    76	\subsection{Environment proxy for optical AGN in massive SDSS hosts}
    77	The follow-up goal here is to define the environment-stratified optical denominator that future radio and X-ray work could test. The local-density proxy is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-density quartile has an optical AGN fraction of 0.509, while the low-density quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency. The missing observables are radio jet morphology and age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates \citep{best2005,mcnamara2007,heckmanbest2014}.
    78	
    79	\begin{figure}
    80	\centering
    81	\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
    82	\caption{SDSS optical denominator/proxy diagnostic for m2\_p2\_radio\_jet\_environment. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    83	\label{fig:m2-p2-radio-jet-environment}
    84	\end{figure}
    85	
    86	
    87	\subsection{Stellar-mass distribution of low-sSFR and optical AGN incidence}
    88	The follow-up goal here is to pin down the mass bin where a future gas-inclusive study should look for an incidence change. At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator? The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\). The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The missing observables are gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
    89	The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a physical transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}.
    90	
    91	\begin{figure}
    92	\centering
    93	\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
    94	\caption{SDSS optical denominator/proxy diagnostic for m2\_p3\_feedback\_transition\_mass. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    95	\label{fig:m2-p3-feedback-transition-mass}
    96	\end{figure}
    97	
    98	
    99	\subsection{Common-denominator optical tracer census in SDSS}
   100	The follow-up goal here is to compare optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are ionized, molecular, neutral, and X-ray or radio tracers measured over the same parent denominator and aperture model \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.
   101	
   102	\begin{figure}
   103	\centering
   104	\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
   105	\caption{SDSS optical denominator/proxy diagnostic for m3\_p1\_multiphase\_census. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   106	\label{fig:m3-p1-multiphase-census}
   107	\end{figure}
   108	
   109	
   110	\subsection{Optical denominator for gas-fraction versus efficiency tests}
   111	The follow-up goal here is to define the denominator for CO/HI gas-fraction and depletion-time follow-up. How many massive low-sSFR or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up? The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The missing observables are CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels \citep{xcoldgass2017,xgass2018,piotrowska2022}.
   112	
   113	\begin{figure}
   114	\centering
   115	\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
   116	\caption{SDSS optical denominator/proxy diagnostic for m3\_p2\_gas\_depletion\_efficiency. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   117	\label{fig:m3-p2-gas-depletion-efficiency}
   118	\end{figure}
   119	
   120	
   121	\subsection{SDSS target vector for feedback-model validation}
   122	The follow-up goal here is to provide a compact observed target vector for forward modelling, not a direct simulation comparison. What compact SDSS target vector of low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift can be used for forward-model validation? The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact validation vector. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The missing observables are simulation mocks passed through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions and aperture or noise models \citep{simba2019,tng2019,eagle2015}.
   123	
   124	\begin{figure}
   125	\centering
   126	\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
   127	\caption{SDSS optical denominator/proxy diagnostic for m3\_p3\_simulation\_validation. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   128	\label{fig:m3-p3-simulation-validation}
   129	\end{figure}
   130	
   131	
   132	\section{Package decision}
   133	These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.
   134	
   135	\section{Local reproducibility}
   136	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
   137	
   138	
   139	\begin{thebibliography}{}
   140	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
   141	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
   142	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
   143	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
   144	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
   145	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
   146	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
   147	\bibitem[Dave et al.(2019)]{simba2019} Dave, R., Angles-Alcazar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
   148	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
   149	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
   150	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
   151	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
   152	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
   153	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
   154	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
   155	\bibitem[LaMassa et al.(2013)]{lamassa2013} LaMassa, S.~M., Heckman, T.~M., Ptak, A., \& Urry, C.~M. 2013, ApJL, 765, L33
   156	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
   157	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
   158	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
   159	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
   160	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
   161	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
   162	\bibitem[Stasinska et al.(2008)]{stasinska2008} Stasinska, G., Asari, N.~V., Cid Fernandes, R., et al. 2008, MNRAS, 391, L29
   163	\bibitem[Stasinska et al.(2015)]{stasinska2015} Stasinska, G., Costa Duarte, M.~V., Vale Asari, N., Cid Fernandes, R., \& Sodre, L. 2015, MNRAS, 449, 559
   164	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
   165	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
   166	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
   167	\end{thebibliography}
   168	
   169	\end{document}

exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log" in /Users/duhokim/NebulaMind/NebulaMind
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

 succeeded in 0ms:
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
I’ve got the main text. I’m now verifying the figure path surface and looking for any file-level mismatch that could turn into a compile or reproducibility regression even though the current build passed.
exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package | rg '/figures/|\\.pdf"'$|'"\\.tex"'$|PACKAGE_AUDIT'"\\.md|FINAL_HANDOFF\\.md'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/PACKAGE_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/figures/topic-02.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/figures/topic-03.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/figures/topic-01.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/figures/topic-04.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/figures/topic-05.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/figures/topic-07.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/figures/topic-06.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/figures/topic-08.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/FINAL_HANDOFF.md

exec
/bin/zsh -lc "rg -n --no-heading 'fig-bpt|fig-matched-offsets|topic-0[1-8]' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | sed -n '18,140p'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex | sed -n '18,90p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:48:\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:59:\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:70:\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:81:\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:93:\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:104:\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:115:\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex:126:\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex:51:\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex:76:\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}

 succeeded in 0ms:
    18	\section{Question and claim boundary}
    19	This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish causal AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
    20	
    21	The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and LINER-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.
    22	
    23	\section{Data and shared selection}
    24	The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The cached analysis table is capped at 60,000 rows and ordered by \texttt{specObjID}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the cache covers 24.0\% of that strict parent.
    25	Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
    26	The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Selection cascade for the flagship denominator.\label{tab:selection}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Cached-versus-public marginal checks show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.
    45	
    46	\section{Classification and matching}
    47	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical AGN host is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
    48	
    49	\begin{figure*}
    50	\centering
    51	\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
    52	\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
    53	\label{fig:bpt}
    54	\end{figure*}
    55	
    56	\section{Matched-control result}
    57	The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the optical AGN hosts relative to star-forming controls.
    58	A median $\Delta\log {\rm sSFR}$ of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR, but this manuscript does not convert that proxy offset into a global quenching threshold.
    59	
    60	\begin{deluxetable*}{lrrrr}
    61	\tabletypesize{\scriptsize}
    62	\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
    63	\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
    64	\startdata
    65	Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
    66	Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
    67	Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
    68	Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
    69	N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity \\
    70	\enddata
    71	\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. All values are conditional on the optical emission-line denominator.}
    72	\end{deluxetable*}
    73	
    74	\begin{figure*}
    75	\centering
    76	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    77	\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT AGN hosts minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions.}
    78	\label{fig:offsets}
    79	\end{figure*}
    80	
    81	\section{Interpretation}
    82	The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude to roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including LINER-like ionization from retired stellar populations and post-AGB stars, rather than identifying a different physical mechanism. The most robust conclusion is therefore: broad optical BPT AGN classification is associated with lower catalog sSFR in this capped SDSS emission-line sample. Claims about causal quenching require additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.
    83	
    84	\section{Conclusion}
    85	RP-1 is best treated as a concise, selection-aware association paper. Related topic notes belong in a supplementary denominator/proxy atlas until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
    86	In practice, that means future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; they are not part of the present SDSS-only denominator.
    87	
    88	\section{Local reproducibility}
    89	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
    90	

 succeeded in 0ms:
    18	\section{Purpose}
    19	The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. Keeping them in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.
    20	
    21	\section{Shared denominator}
    22	The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}.
    23	
    24	The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.
    25	
    26	\begin{deluxetable*}{lrrr}
    27	\tabletypesize{\scriptsize}
    28	\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
    29	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
    30	\startdata
    31	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    32	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    33	plus galSpecLine join & 416,554 & -- & 0.831 \\
    34	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    35	four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
    36	four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
    37	four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
    38	\enddata
    39	\end{deluxetable*}
    40	
    41	\section{Atlas notes}
    42	
    43	\subsection{SDSS density proxy for low-sSFR incidence}
    44	The follow-up goal here is to isolate an environmental denominator that can later be joined to group catalogs and halo masses. The nearest-neighbour density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions are still needed for a physical environmental interpretation \citep{peng2010,wetzel2013,dekel2006}.
    45	
    46	\begin{figure}
    47	\centering
    48	\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
    49	\caption{SDSS optical denominator/proxy diagnostic for m1\_rp2\_environment\_quenching. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    50	\label{fig:m1-rp2-environment-quenching}
    51	\end{figure}
    52	
    53	
    54	\subsection{Optical-AGN denominator for maintenance-heating follow-up}
    55	The follow-up goal here is to identify the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can be used as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The missing observables are X-ray cavity or cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.
    56	
    57	\begin{figure}
    58	\centering
    59	\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
    60	\caption{SDSS optical denominator/proxy diagnostic for m1\_rp3\_maintenance\_heating. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    61	\label{fig:m1-rp3-maintenance-heating}
    62	\end{figure}
    63	
    64	
    65	\subsection{SDSS high-excitation AGN denominator for outflow tests}
    66	The follow-up goal here is to isolate the optical-AGN denominator that resolved kinematics would need to test escape versus recycling. The SDSS high-excitation optical-AGN denominator identifies how many systems would need resolved kinematics to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.
    67	
    68	\begin{figure}
    69	\centering
    70	\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
    71	\caption{SDSS optical denominator/proxy diagnostic for m2\_p1\_outflow\_escape\_recycling. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    72	\label{fig:m2-p1-outflow-escape-recycling}
    73	\end{figure}
    74	
    75	
    76	\subsection{Environment proxy for optical AGN in massive SDSS hosts}
    77	The follow-up goal here is to define the environment-stratified optical denominator that future radio and X-ray work could test. The local-density proxy is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-density quartile has an optical AGN fraction of 0.509, while the low-density quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency. The missing observables are radio jet morphology and age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates \citep{best2005,mcnamara2007,heckmanbest2014}.
    78	
    79	\begin{figure}
    80	\centering
    81	\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
    82	\caption{SDSS optical denominator/proxy diagnostic for m2\_p2\_radio\_jet\_environment. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    83	\label{fig:m2-p2-radio-jet-environment}
    84	\end{figure}
    85	
    86	
    87	\subsection{Stellar-mass distribution of low-sSFR and optical AGN incidence}
    88	The follow-up goal here is to pin down the mass bin where a future gas-inclusive study should look for an incidence change. At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator? The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\). The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The missing observables are gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
    89	The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a physical transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}.
    90	
    91	\begin{figure}
    92	\centering
    93	\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
    94	\caption{SDSS optical denominator/proxy diagnostic for m2\_p3\_feedback\_transition\_mass. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
    95	\label{fig:m2-p3-feedback-transition-mass}
    96	\end{figure}
    97	
    98	
    99	\subsection{Common-denominator optical tracer census in SDSS}
   100	The follow-up goal here is to compare optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are ionized, molecular, neutral, and X-ray or radio tracers measured over the same parent denominator and aperture model \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.
   101	
   102	\begin{figure}
   103	\centering
   104	\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
   105	\caption{SDSS optical denominator/proxy diagnostic for m3\_p1\_multiphase\_census. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   106	\label{fig:m3-p1-multiphase-census}
   107	\end{figure}
   108	
   109	
   110	\subsection{Optical denominator for gas-fraction versus efficiency tests}
   111	The follow-up goal here is to define the denominator for CO/HI gas-fraction and depletion-time follow-up. How many massive low-sSFR or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up? The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The missing observables are CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels \citep{xcoldgass2017,xgass2018,piotrowska2022}.
   112	
   113	\begin{figure}
   114	\centering
   115	\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
   116	\caption{SDSS optical denominator/proxy diagnostic for m3\_p2\_gas\_depletion\_efficiency. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   117	\label{fig:m3-p2-gas-depletion-efficiency}
   118	\end{figure}
   119	
   120	
   121	\subsection{SDSS target vector for feedback-model validation}
   122	The follow-up goal here is to provide a compact observed target vector for forward modelling, not a direct simulation comparison. What compact SDSS target vector of low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift can be used for forward-model validation? The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact validation vector. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The missing observables are simulation mocks passed through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions and aperture or noise models \citep{simba2019,tng2019,eagle2015}.
   123	
   124	\begin{figure}
   125	\centering
   126	\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
   127	\caption{SDSS optical denominator/proxy diagnostic for m3\_p3\_simulation\_validation. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
   128	\label{fig:m3-p3-simulation-validation}
   129	\end{figure}
   130	
   131	
   132	\section{Package decision}
   133	These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.
   134	
   135	\section{Local reproducibility}
   136	This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.
   137	
   138	
   139	\begin{thebibliography}{}
   140	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35

codex
The build itself is clean enough to pass, but the log has a recurring encoding warning. I’m checking whether the TeX source actually contains hidden non-ASCII bytes, because that is the main reproducibility smell left in an otherwise valid package.
exec
/bin/zsh -lc "LC_ALL=C rg -n --no-heading '["'^'"\\x00-\\x7F]' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex | sed -n '1,120p'" in /Users/duhokim/NebulaMind/NebulaMind
 exited 1 in 0ms:
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Selection-aware SDSS optical AGN/sSFR pilot}
\shortauthors{NebulaMind}
\begin{document}

\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Pilot}
\author{NebulaMind Research Autopilot}
\affiliation{Public SDSS DR17 data only}

\begin{abstract}
We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies. Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, both of which can bias fiber-based sSFR comparisons. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not a causal AGN-feedback measurement. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude, so subclass and selection-function treatment must precede any physical interpretation.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish causal AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.

The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and LINER-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The cached analysis table is capped at 60,000 rows and ordered by \texttt{specObjID}; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the cache covers 24.0\% of that strict parent.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade for the flagship denominator.\label{tab:selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Cached-versus-public marginal checks show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the capped-cache limitation.

\section{Classification and matching}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical AGN, and 67 unclassified objects. Each broad optical AGN host is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.

\begin{figure*}
\centering
\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
\label{fig:bpt}
\end{figure*}

\section{Matched-control result}
The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the optical AGN hosts relative to star-forming controls.
A median $\Delta\log {\rm sSFR}$ of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR, but this manuscript does not convert that proxy offset into a global quenching threshold.

\begin{deluxetable*}{lrrrr}
\tabletypesize{\scriptsize}
\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
\startdata
Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity \\
\enddata
\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. All values are conditional on the optical emission-line denominator.}
\end{deluxetable*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT AGN hosts minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions.}
\label{fig:offsets}
\end{figure*}

\section{Interpretation}
The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude to roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including LINER-like ionization from retired stellar populations and post-AGB stars, rather than identifying a different physical mechanism. The most robust conclusion is therefore: broad optical BPT AGN classification is associated with lower catalog sSFR in this capped SDSS emission-line sample. Claims about causal quenching require additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{Conclusion}
RP-1 is best treated as a concise, selection-aware association paper. Related topic notes belong in a supplementary denominator/proxy atlas until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
In practice, that means future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; they are not part of the present SDSS-only denominator.

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

exec
/bin/zsh -lc "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | sed -n '1,140p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
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
This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60,000-row optical emission-line cache and the same selection-function caveats. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. It is a single follow-up atlas, not eight independent causal-feedback papers.
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. Keeping them in one supplement prevents overclaiming and gives future work a single checklist of what still must be added.

\section{Shared denominator}
The atlas uses the same cached public-data backbone as the main paper: 60,000 cached rows from a strict public four-line S/N$\geq3$ parent of 249,917 rows, i.e. 24.0\% cached coverage. The four-line selection is sSFR-dependent and the cache is capped and non-random, so all counts and fractions are conditional denominators rather than population-complete measurements. The row-level stellar masses and catalog sSFR values are taken from the public MPA-JHU-style \texttt{galSpecExtra} table after the same SDSS joins used in the flagship \citep{sdssdr17,brinchmann2004,york2000}.

The eight subsections below are intentionally parallel: each one states the observed optical denominator or target vector, then lists the missing observables that a future multiwavelength or simulation-based test would have to add before any physical inference can be made.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade shared by the atlas.\label{tab:supp-selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 0.183 \\
\enddata
\end{deluxetable*}

\section{Atlas notes}

\subsection{SDSS density proxy for low-sSFR incidence}
The follow-up goal here is to isolate an environmental denominator that can later be joined to group catalogs and halo masses. The nearest-neighbour density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions are still needed for a physical environmental interpretation \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m1\_rp2\_environment\_quenching. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m1-rp2-environment-quenching}
\end{figure}


\subsection{Optical-AGN denominator for maintenance-heating follow-up}
The follow-up goal here is to identify the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can be used as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The missing observables are X-ray cavity or cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m1\_rp3\_maintenance\_heating. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m1-rp3-maintenance-heating}
\end{figure}


\subsection{SDSS high-excitation AGN denominator for outflow tests}
The follow-up goal here is to isolate the optical-AGN denominator that resolved kinematics would need to test escape versus recycling. The SDSS high-excitation optical-AGN denominator identifies how many systems would need resolved kinematics to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are resolved outflow velocities, halo potentials, molecular, ionized, and neutral gas phases, and CGM recycling tracers \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m2\_p1\_outflow\_escape\_recycling. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m2-p1-outflow-escape-recycling}
\end{figure}


\subsection{Environment proxy for optical AGN in massive SDSS hosts}
The follow-up goal here is to define the environment-stratified optical denominator that future radio and X-ray work could test. The local-density proxy is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-density quartile has an optical AGN fraction of 0.509, while the low-density quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency. The missing observables are radio jet morphology and age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates \citep{best2005,mcnamara2007,heckmanbest2014}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m2\_p2\_radio\_jet\_environment. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m2-p2-radio-jet-environment}
\end{figure}


\subsection{Stellar-mass distribution of low-sSFR and optical AGN incidence}
The follow-up goal here is to pin down the mass bin where a future gas-inclusive study should look for an incidence change. At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator? The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\). The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The missing observables are gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a physical transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m2\_p3\_feedback\_transition\_mass. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m2-p3-feedback-transition-mass}
\end{figure}


\subsection{Common-denominator optical tracer census in SDSS}
The follow-up goal here is to compare optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are ionized, molecular, neutral, and X-ray or radio tracers measured over the same parent denominator and aperture model \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m3\_p1\_multiphase\_census. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m3-p1-multiphase-census}
\end{figure}


\subsection{Optical denominator for gas-fraction versus efficiency tests}
The follow-up goal here is to define the denominator for CO/HI gas-fraction and depletion-time follow-up. How many massive low-sSFR or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up? The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The missing observables are CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels \citep{xcoldgass2017,xgass2018,piotrowska2022}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m3\_p2\_gas\_depletion\_efficiency. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m3-p2-gas-depletion-efficiency}
\end{figure}


\subsection{SDSS target vector for feedback-model validation}
The follow-up goal here is to provide a compact observed target vector for forward modelling, not a direct simulation comparison. What compact SDSS target vector of low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift can be used for forward-model validation? The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact validation vector. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The missing observables are simulation mocks passed through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions and aperture or noise models \citep{simba2019,tng2019,eagle2015}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-08.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m3\_p3\_simulation\_validation. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m3-p3-simulation-validation}
\end{figure}


\section{Package decision}
These eight notes should remain supplementary until the missing observables are added. They are suitable as follow-up target definitions, denominator baselines, or appendix material under the main result, but not as independent causal-feedback papers in their current SDSS-only form.

\section{Local reproducibility}
This PDF was generated from the local candidate package \texttt{RP1\_FLAGSHIP\_WITH\_SUPPLEMENT\_20260709T013510Z}. It does not replace any public-linked PDF and does not touch public pages, live roots, product databases, deployment state, git history, billing/OAuth state, cron jobs, or external submission systems.


\begin{thebibliography}{}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35

codex
CODEX_KUN_REVIEW_CYCLE_04

**Findings**
- Medium: both builds emit `lineno.sty:296: Invalid UTF-8 byte or sequence ... replaced by U+FFFD` in the compile logs, even though the PDFs are produced successfully. I re-scanned the two TeX sources and found no non-ASCII bytes, so this is likely a TeX/package interaction rather than manuscript content. This is a reproducibility smell because a future engine or package update could turn the warning into a harder failure. Sources: [flagship compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log), [supplement compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log), [flagship tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex), [supplement tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex).
- Medium: the flagship prose is mostly guardrail-safe, but two lines are a little too broad for an association-only manuscript. In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L19) the phrase “The answer is yes” is fine scientifically but reads more absolute than the rest of the paper. In [the same file](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L82), “directly measured, reproducible, and falsifiable” is also stronger than necessary for a capped, non-random cache. Safe edit: tighten both sentences to keep the result explicitly denominator-bound and association-only.
- Low: figure references are complete and compile cleanly, but the figure paths are brittle because both manuscripts hard-code `../figures/...`. The current package layout is consistent and `rg --files` shows all 10 referenced PDFs exist, so this is not a breakage today. It is a portability risk if the TeX files move or if the build directory changes. Sources: [flagship tex figure refs](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L49), [supplement tex figure refs](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L46).
- Low: the reproducibility story is scientifically honest about the capped cache, but the manuscript does not name the exact cache artifact or checksum. Because the main numerical result depends on a non-random 60,000-row cache, preserving the exact cached table is essential for bitwise reproducibility. Safe edit: add one line to the local reproducibility section with the cache file path and hash, or add it to `PACKAGE_AUDIT.md`.

**Numeric Check**
- Consistent across abstract, body, and table: `8,146` pairs, median `-1.309 dex`, interval `[-1.334, -1.283]`, `60,000` cached rows, `249,917` strict S/N>=3 parent rows, and `24.0%` cached coverage. I did not find a mismatch in the flagship or supplement text.
- The supplement’s shared-denominator counts also line up with the main paper’s parent/cache numbers, including the `60,000` and `249,917` values in [supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L22).

**Exact Safe Edits**
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L19), replace:
  - `The answer is yes for the cached denominator analyzed here.`
  - with `Within the cached denominator analyzed here, broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls.`
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L82), replace:
  - `The result is directly measured, reproducible, and falsifiable inside the stated denominator.`
  - with `The result is measured within the stated denominator and can be reproduced by rerunning the same selection and matching rules.`
- In both TeX files, consider replacing the repeated `../figures/...` paths with a preamble-level `\graphicspath{{../figures/}}` and bare filenames. Example:
  - `\includegraphics[width=0.72\textwidth]{fig-bpt.pdf}`
  - `\includegraphics[width=0.86\textwidth]{fig-matched-offsets.pdf}`
  - and the same pattern for `topic-01.pdf` through `topic-08.pdf`.
- In the local reproducibility section of both manuscripts, add the cache artifact identifier or hash used to generate the 60,000-row table. That is the most important missing provenance detail for reruns.
- Leave the `[N II]` issue alone in the current source; it has already been sanitized to `N II Seyfert-like proxy`, which avoids the TeX row-spacing parsing problem noted in the handoff.

**Safety Ledger**
- Read-only review only.
- No file edits made.
- No git write commands, deploys, restarts, publishes, API calls, credential access, or live/public-root touches.
- All checks stayed within the local package under `cycle_04_package`.
tokens used
45,317
CODEX_KUN_REVIEW_CYCLE_04

**Findings**
- Medium: both builds emit `lineno.sty:296: Invalid UTF-8 byte or sequence ... replaced by U+FFFD` in the compile logs, even though the PDFs are produced successfully. I re-scanned the two TeX sources and found no non-ASCII bytes, so this is likely a TeX/package interaction rather than manuscript content. This is a reproducibility smell because a future engine or package update could turn the warning into a harder failure. Sources: [flagship compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.compile.log), [supplement compile log](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.compile.log), [flagship tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex), [supplement tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex).
- Medium: the flagship prose is mostly guardrail-safe, but two lines are a little too broad for an association-only manuscript. In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L19) the phrase “The answer is yes” is fine scientifically but reads more absolute than the rest of the paper. In [the same file](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L82), “directly measured, reproducible, and falsifiable” is also stronger than necessary for a capped, non-random cache. Safe edit: tighten both sentences to keep the result explicitly denominator-bound and association-only.
- Low: figure references are complete and compile cleanly, but the figure paths are brittle because both manuscripts hard-code `../figures/...`. The current package layout is consistent and `rg --files` shows all 10 referenced PDFs exist, so this is not a breakage today. It is a portability risk if the TeX files move or if the build directory changes. Sources: [flagship tex figure refs](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L49), [supplement tex figure refs](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L46).
- Low: the reproducibility story is scientifically honest about the capped cache, but the manuscript does not name the exact cache artifact or checksum. Because the main numerical result depends on a non-random 60,000-row cache, preserving the exact cached table is essential for bitwise reproducibility. Safe edit: add one line to the local reproducibility section with the cache file path and hash, or add it to `PACKAGE_AUDIT.md`.

**Numeric Check**
- Consistent across abstract, body, and table: `8,146` pairs, median `-1.309 dex`, interval `[-1.334, -1.283]`, `60,000` cached rows, `249,917` strict S/N>=3 parent rows, and `24.0%` cached coverage. I did not find a mismatch in the flagship or supplement text.
- The supplement’s shared-denominator counts also line up with the main paper’s parent/cache numbers, including the `60,000` and `249,917` values in [supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex#L22).

**Exact Safe Edits**
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L19), replace:
  - `The answer is yes for the cached denominator analyzed here.`
  - with `Within the cached denominator analyzed here, broad BPT optical AGN hosts have lower catalog sSFR than mass--redshift matched star-forming controls.`
- In [rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_04_package/flagship_rp1/aastex/rp1_flagship_polished.tex#L82), replace:
  - `The result is directly measured, reproducible, and falsifiable inside the stated denominator.`
  - with `The result is measured within the stated denominator and can be reproduced by rerunning the same selection and matching rules.`
- In both TeX files, consider replacing the repeated `../figures/...` paths with a preamble-level `\graphicspath{{../figures/}}` and bare filenames. Example:
  - `\includegraphics[width=0.72\textwidth]{fig-bpt.pdf}`
  - `\includegraphics[width=0.86\textwidth]{fig-matched-offsets.pdf}`
  - and the same pattern for `topic-01.pdf` through `topic-08.pdf`.
- In the local reproducibility section of both manuscripts, add the cache artifact identifier or hash used to generate the 60,000-row table. That is the most important missing provenance detail for reruns.
- Leave the `[N II]` issue alone in the current source; it has already been sanitized to `N II Seyfert-like proxy`, which avoids the TeX row-spacing parsing problem noted in the handoff.

**Safety Ledger**
- Read-only review only.
- No file edits made.
- No git write commands, deploys, restarts, publishes, API calls, credential access, or live/public-root touches.
- All checks stayed within the local package under `cycle_04_package`.


# command_result
exit_code=0
elapsed_s=135.1
timed_out=False
finished_utc=2026-07-09T02:36:27Z

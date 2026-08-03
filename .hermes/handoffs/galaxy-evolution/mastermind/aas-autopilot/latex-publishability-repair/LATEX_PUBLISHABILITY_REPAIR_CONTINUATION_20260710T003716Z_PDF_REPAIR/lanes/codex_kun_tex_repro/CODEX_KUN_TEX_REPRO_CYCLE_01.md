# codex_kun_tex_repro cycle 1
Started UTC: 2026-07-10T01:12:40Z
Finished UTC: 2026-07-10T01:16:05Z
Model: gpt-5.4-mini
Provider: codex
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/briefs/cycle_01_codex_kun_tex_repro.md
Exit: 0

```text
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
session id: 019f4995-7a40-7633-b94e-3174a6261ed7
--------
user
Kun/Codex read-only TeX/reproducibility audit: inspect candidate TeX and strict compile audit; report exact blockers; no edits.

Output marker: LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_01

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

The user reports that the current public PDFs are still not publishable and that some show LaTeX errors. Your job is to find exact high-value blockers and feed the candidate-copy writer. Focus first on strict LaTeX/log issues, then AAS publishability.

Required output sections:
1. LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_01 status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Strict LaTeX blockers: fatal errors, undefined refs/citations, missing figures, overfull/underfull box locations, package/layout problems.
4. Publishability blockers: overclaiming, weak abstract/conclusion, insufficient caveats, source-role/citation problems, poor figure/table captions, reader flow.
5. Exact feed for the writer: concrete TeX-level edits, by file/section/line when possible. Preserve all real measured values and real-data limits.
6. Safety ledger: no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR
Cycle: 1
Candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers
Integrated 9-paper root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z
Public promotion receipt root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/public-promotions/PUBLIC_STATIC_PDF_PROMOTION_20260709T233457Z

Safety locks:
- write only under this repair run root and copied candidate packages
- review lanes write reports only; only the candidate-copy integrator edits candidate-copy TeX
- no public-linked PDF replacement or public/live static root edits
- no DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation
- no deploy/restart
- no git commit/push/merge/rebase/history rewrite
- no cron creation/update/removal
- no billing/cloud/OAuth/API-key/account changes and no credential/token/cookie reads
- no external manuscript submission

Real-data rules:
- Never use mock, synthetic, fake, placeholder, or toy data as manuscript evidence.
- Never invent numbers, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, figure results, or table values.
- Every quantitative claim must trace to real local artifacts or checkable public sources already in the package.
- Absent data must be written as absent/future real-data requirements, not inferred as results.
- RP-1 stays association-only; papers 2-9 stay SDSS optical denominator/proxy notes unless new real data are inventoried.

Context follows:
Candidate: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers
Cycle: 1

## Strict LaTeX audit

- m1_rp1_sdss_agn_sfr_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m1_rp2_environment_quenching_integrated.tex: build_ok=True clean_ok=False rc=0 layout_warnings=2 undefined=0 fatal={}
  - L578: Underfull \hbox (badness 1019) in paragraph at lines 57--58
  - L585: Underfull \hbox (badness 1931) in paragraph at lines 72--73
- m1_rp3_maintenance_heating_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m2_p1_outflow_escape_recycling_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m2_p2_radio_jet_environment_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m2_p3_feedback_transition_mass_integrated.tex: build_ok=True clean_ok=False rc=0 layout_warnings=2 undefined=0 fatal={}
  - L579: Underfull \hbox (badness 2134) in paragraph at lines 57--58
  - L586: Underfull \hbox (badness 2134) in paragraph at lines 77--78
- m3_p1_multiphase_census_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m3_p2_gas_depletion_efficiency_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
  - L583: LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
- m3_p3_simulation_validation_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}

## Manuscript summaries

### 01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
Title: Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Pilot
Abstract: We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log {\rm sSFR}=-1.309$ dex; at S/N$\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
Conclusion: In the capped SDSS DR17 emission-line subset, broad BPT optical AGN hosts show a median sSFR offset of $-1.309$ dex relative to mass--redshift matched controls, with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Although the offset amplitude is highly dependent on the emission-line selection function (decreasing to $-0.744$ dex at S/N$\geq 10$), the interval remains securely negative. These measurements establish a robust optical association baseline, which will require future molecular gas or direct outflow kinematics follow-up to isolate any causal AGN quenching mechanisms. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
Title: SDSS Density Proxy for Environmental Quenching
Abstract: We use a representative 60,000-galaxy subset of the SDSS DR17 emission-line catalog to build an optical density-proxy analysis of environmental quenching. A 10th-nearest-neighbor density proxy is compared with quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) after controlling for stellar mass and redshift; using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile. The bootstrap high-minus-low interval is [0.041, 0.059], which excludes zero. This analysis is intentionally limited to the optical denominator and leaves the missing group and halo information for future study.
Conclusion: The SDSS-only proxy shows a high-density quenched fraction of 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile, with a mass- and redshift-adjusted high-density coefficient of $0.032 \pm 0.004$. These values define an optical environmental baseline, but a full quenching interpretation still requires group catalogs, halo masses, and central/satellite labels. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
Title: Optical-AGN Denominator for Maintenance-Heating Follow-Up
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 (3,997/9,298) in the massive subset and 0.607 (3,459/5,695) among massive low-sSFR objects, providing a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.
Conclusion: The massive subset contains 9,298 emission-line galaxies, with 5,695 classified as low-sSFR by the pilot threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$. The BPT AGN fraction rises from 0.430 (3,997/9,298) in the massive subset to 0.607 (3,459/5,695) in the massive low-sSFR subset, defining an optical duty-cycle denominator for maintenance-heating follow-up rather than a direct heating result. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
Title: SDSS BPT-Selected Optical AGN Denominator for Outflow Escape Tests
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\pm$ 0.001) and records their median $\log {\rm sSFR} = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
Conclusion: BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074 $\pm$ 0.001), and their median $\log {\rm sSFR}$ is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
Title: Environment Proxy for Optical AGN in Massive SDSS Hosts
Abstract: We build an optical denominator for radio-jet environment follow-up using a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. In massive hosts, the high-density quartile has optical AGN fraction 0.509 $\pm$ 0.012 and the low-density quartile has 0.367 $\pm$ 0.012, defining an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
Conclusion: Among massive hosts, the optical AGN fraction is 0.509 $\pm$ 0.012 in the high-density quartile and 0.367 $\pm$ 0.012 in the low-density quartile, with a bootstrap difference of [0.112, 0.170]. This establishes an environment-stratified optical denominator for radio-jet coupling studies, not a direct coupling measurement. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
Title: SDSS Mass Transition in Quenching and Optical AGN Incidence
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to identify the stellar-mass regime where quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, and the first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail at $\log(M_\star/M_\odot) > 11.0$, where the optical AGN fraction peaks at 0.520 (2,098/4,033). It does not assign the transition to stellar or AGN feedback on its own.
Conclusion: The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$. In that same bin, the optical AGN fraction peaks at 0.520 (2,098/4,033). These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
Title: Common-Denominator Optical Tracer Census in SDSS
Abstract: We build a common optical denominator for a multiphase outflow census from a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, from 0.136 for BPT AGN to 0.418 for red+emission, so this note focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.
Conclusion: Within the 60,000-galaxy denominator, the BPT AGN and red+emission definitions change prevalence from 0.136 for BPT AGN to 0.418 for red+emission, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
Title: Optical Denominator for Gas-Fraction Versus Efficiency Tests
Abstract: We use a 6,729-galaxy downstream subset drawn from the 60,000-galaxy SDSS DR17 emission-line cache to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729) and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides an empirical baseline and candidate list for future CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
Conclusion: We have mapped the optical baseline for 6,729 massive quenched or transitioning galaxies in the SDSS emission-line sample. We find a BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729) and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, approximately 0.66 dex lower than star-forming counterparts. While these quantities define the target selection denominator for future CO gas-fraction versus efficiency programs, direct molecular gas masses and aperture-matched star formation rates remain required to physically distinguish depletion from low efficiency. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
Title: SDSS Target Vector for Feedback-Model Validation
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define a compact optical target vector for forward-model validation. The pilot records quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$), optical AGN incidence, and color versus mass and redshift across 15 mass-redshift cells with $n \geq 50$; across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). It remains an empirical denominator study rather than a direct simulation comparison.
Conclusion: We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector. The grid spans $\log(M_\star/M_\odot)$ bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 across redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). This observed target vector is a compact benchmark for simulation forward modelling, but mock-observation pipelines are still required before any model comparison can be claimed. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

## Existing context
The previous overnight swarm improved candidate-copy manuscripts but user reports PDFs are still not publishable and some show LaTeX errors. Treat layout warnings, broken refs/citations, missing figures, and sloppy AAS presentation as real blockers to chase down in the copied TeX package.
codex
I’m inspecting the candidate package and the compile artifacts first so I can separate hard LaTeX blockers from publishability issues. After that I’ll map each blocker back to the exact TeX file and section-level fix the writer should make.
exec
/bin/zsh -lc "rg --files \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers\" | sed -n '1,200p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/CYCLE_01_BEFORE_STRICT_LATEX_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/CYCLE_01_BEFORE_TEX_LINT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/SOURCE_COPY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/CYCLE_01_BEFORE_STRICT_LATEX_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/CYCLE_01_BEFORE_TEX_LINT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf

codex
I’ve confirmed the package layout and the nine TeX/PDF pairs are present. Next I’m reading the generated audit metadata and the TeX sources for the two files that already show layout warnings, then I’ll check for any hidden compile/log issues in the remaining papers.
exec
/bin/zsh -lc "sed -n '1,240p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/CYCLE_01_BEFORE_STRICT_LATEX_AUDIT.md\"" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,260p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/CYCLE_01_BEFORE_TEX_LINT.json\"" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,220p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "candidate": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers",
  "created_utc": "2026-07-10T01:12:19Z",
  "cycle": 1,
  "error_count": 0,
  "finding_count": 0,
  "findings": [],
  "label": "before",
  "returncode": 0,
  "tex_file_count": 9,
  "tool": "/Users/duhokim/NebulaMind/NebulaMind/tools/ge_tex_publishability_lint.py",
  "warning_count": 0
}
 succeeded in 0ms:
# Strict LaTeX audit before cycle 1

all_build_ok: True
all_clean_ok: False
layout_warning_count: 4
undefined_count: 0

## m1_rp1_sdss_agn_sfr_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=240347
- fatal_hits={}
- warning_hits={}

## m1_rp2_environment_quenching_integrated.tex
- build_ok=True clean_ok=False rc=0 bytes=91845
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 2}
- log lines:
  - L578: Underfull \hbox (badness 1019) in paragraph at lines 57--58
  - L585: Underfull \hbox (badness 1931) in paragraph at lines 72--73

## m1_rp3_maintenance_heating_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=91052
- fatal_hits={}
- warning_hits={}

## m2_p1_outflow_escape_recycling_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=322529
- fatal_hits={}
- warning_hits={}

## m2_p2_radio_jet_environment_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=90944
- fatal_hits={}
- warning_hits={}

## m2_p3_feedback_transition_mass_integrated.tex
- build_ok=True clean_ok=False rc=0 bytes=96061
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 2}
- log lines:
  - L579: Underfull \hbox (badness 2134) in paragraph at lines 57--58
  - L586: Underfull \hbox (badness 2134) in paragraph at lines 77--78

## m3_p1_multiphase_census_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=89008
- fatal_hits={}
- warning_hits={}

## m3_p2_gas_depletion_efficiency_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=218974
- fatal_hits={}
- warning_hits={'Rerun to get cross-references right': 1}
- log lines:
  - L583: LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

## m3_p3_simulation_validation_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=97016
- fatal_hits={}
- warning_hits={}

 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS Density Proxy for Environmental Quenching}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{SDSS Density Proxy for Environmental Quenching}
\author{NebulaMind Research Autopilot}
\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
\correspondingauthor{NebulaMind Research Autopilot}
\email{autopilot@nebulamind.ai}

\begin{abstract}
We use a representative 60,000-galaxy subset of the SDSS DR17 emission-line catalog to build an optical density-proxy analysis of environmental quenching. A 10th-nearest-neighbor density proxy is compared with quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) after controlling for stellar mass and redshift; using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile. The bootstrap high-minus-low interval is [0.041, 0.059], which excludes zero. This analysis is intentionally limited to the optical denominator and leaves the missing group and halo information for future study.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}

\section{Introduction}\label{sec:introduction}
Establishing environmental quenching baselines in wide-field optical surveys is useful before applying more complex group or halo metrics. Here, the SDSS DR17 emission-line parent sample serves as the optical baseline for the environmental-quenching comparison rather than a direct physical measurement. We evaluate a local 10th-nearest-neighbor density proxy using SDSS DR17 emission-line galaxies and restrict the scope to directly measured optical properties. Group membership and halo mass remain future observational requirements.


\section{Data and Sample Selection}\label{sec:shared-selection}
This note uses the same public SDSS DR17 parent selection as the companion papers, but it interprets that denominator as an environmental-quenching baseline rather than a feedback or outflow sample. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The capped subset contains 60,000 emission-line galaxies from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
We examine whether a nearest-neighbor density proxy adds quenched-fraction information beyond stellar mass in the SDSS emission-line sample. The result is an optical baseline rather than a full physical-feedback test.

Within the same 60,000-galaxy denominator, the high-density quartile has a quenched fraction of $0.230 \pm 0.003$ ($3,456/15,000$), compared with $0.181 \pm 0.003$ ($2,710/15,000$) in the low-density quartile. The bootstrap high-minus-low difference interval is $[0.041, 0.059]$, which excludes zero. After controlling for log stellar mass and redshift, a linear probability model yields a high-density coefficient of $0.032 \pm 0.004$, so the density proxy remains correlated with quenching independently of those host-galaxy properties. Figure~\ref{fig:topic} summarizes the proxy split used in this baseline.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure summarizes the equal-count density-quartile split, where the high-density quartile reaches a quenched fraction of 0.230 $\pm$ 0.003, establishing the baseline for future group-catalog analyses.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only baseline does not include group catalogues, robust central/satellite labels, halo masses, morphology, or multi-redshift selection functions. Those data are required before the density proxy can be interpreted as a physical environmental-quenching measurement.

Because the density proxy is projected on the sky, fiber-collision and redshift-space incompleteness can dilute nearest-neighbor estimates; future group-catalog work should correct those effects explicitly.

Mass and environment are separable axes in low-redshift galaxy evolution. A real environmental-quenching analysis therefore requires group and halo information beyond this nearest-neighbor proxy, together with central/satellite labels and the literature context provided by \citet{peng2010,baldry2006,wetzel2013,goubert2024}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
The SDSS-only proxy shows a high-density quenched fraction of 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile, with a mass- and redshift-adjusted high-density coefficient of $0.032 \pm 0.004$. These values define an optical environmental baseline, but a full quenching interpretation still requires group catalogs, halo masses, and central/satellite labels.

\begin{acknowledgments}
We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
\end{acknowledgments}
\begin{thebibliography}{99}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., Balogh, M.~L., Bower, R.~G., et al. 2006, MNRAS, 373, 469
\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, MNRAS, 528, 3822
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
\end{thebibliography}

\end{document}

exec
/bin/zsh -lc "sed -n '1,220p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS Mass Transition in Quenching and Optical AGN Incidence}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{SDSS Mass Transition in Quenching and Optical AGN Incidence}
\author{NebulaMind Research Autopilot}
\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
\correspondingauthor{NebulaMind Research Autopilot}
\email{autopilot@nebulamind.ai}

\begin{abstract}
We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to identify the stellar-mass regime where quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, and the first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail at $\log(M_\star/M_\odot) > 11.0$, where the optical AGN fraction peaks at 0.520 (2,098/4,033). It does not assign the transition to stellar or AGN feedback on its own.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}

\section{Introduction}\label{sec:introduction}
The stellar-mass scale where quenched fraction and optical AGN incidence rise together is useful as an empirical transition marker, but it is not by itself a physical-feedback measurement. Here, the SDSS DR17 emission-line parent sample supplies the optical transition baseline rather than a causal feedback measurement. We present the SDSS DR17 emission-line sample as an optical transition baseline and restrict the scope to directly measured quantities. Gas fractions, baryon deficits, and halo-scale measurements remain future-data requirements.


\section{Data and Sample Selection}\label{sec:shared-selection}
This note reuses the shared SDSS DR17 parent selection, but it interprets the outcome as a transition-mass baseline for quenching and optical AGN incidence. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
We identify the stellar-mass scale at which quenched fraction and optical AGN incidence rise together in the SDSS emission-line sample. The result is an empirical optical transition vector rather than a full physical-feedback test.

The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$. In that same bin, the optical AGN fraction peaks at 0.520 (2,098/4,033). These results define an empirical transition vector, but gas fractions and baryon deficits are still required before assigning the trend to stellar or AGN feedback. Figure~\ref{fig:topic} highlights the transition bin.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows the high-mass tail ($\log(M_\star/M_\odot) > 11.0$) where the quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520 (2,098/4,033).}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.

Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition. Those data are the missing ingredients behind the optical trend \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$. In that same bin, the optical AGN fraction peaks at 0.520 (2,098/4,033). These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation.

\begin{acknowledgments}
We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
\end{acknowledgments}
\begin{thebibliography}{99}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
\end{thebibliography}

\end{document}

codex
The two known layout warnings are confirmed in the TeX, and I’m now checking for missing bibliography keys, unresolved cross-references, and any figure path issues that the summary may have skipped. If there are no deeper compile blockers, I’ll keep the report focused on the two underfull paragraphs and the one rerun warning.
exec
/bin/zsh -lc "sed -n '1,240p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Optical Denominator for Gas-Fraction Versus Efficiency Tests}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Optical Denominator for Gas-Fraction Versus Efficiency Tests}
\author{NebulaMind Research Autopilot}
\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
\correspondingauthor{NebulaMind Research Autopilot}
\email{autopilot@nebulamind.ai}

\begin{abstract}
We use a 6,729-galaxy downstream subset drawn from the 60,000-galaxy SDSS DR17 emission-line cache to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729) and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides an empirical baseline and candidate list for future CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}

\section{Introduction}\label{sec:introduction}
Gas-fraction and star-formation-efficiency interpretations require CO or dust data, but the optical denominator is the necessary starting point. Here, the SDSS DR17 emission-line parent sample serves as the baseline for the gas-fraction versus efficiency comparison rather than a direct gas-depletion measurement. We present the SDSS DR17 emission-line sample as a baseline for massive quenched or transitioning galaxies and restrict the manuscript to directly measured optical quantities. Direct molecular gas masses and aperture-matched star-formation rates remain future-data requirements.


\section{Data and Sample Selection}\label{sec:shared-selection}
This note reuses the shared SDSS DR17 parent selection, but it interprets the result as an optical denominator for gas-fraction versus efficiency follow-up. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The capped subset contains 60,000 galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities, ending with the paper-specific downstream subset.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
Massive quenched or transitioning subset & -- & 6,729 & -- \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies. The final row defines the specific 6,729-galaxy subset used in this optical baseline.}
\end{deluxetable*}

The paper-specific downstream selection retains 6,729 massive quenched or transitioning galaxies from the cached 60,000-galaxy parent, as fixed by the cached selection manifest. That branch is the denominator used for the gas-fraction versus efficiency result below, and it is a local subset rather than a separate public DR17 count query.

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{Optical denominator for gas-fraction versus efficiency tests}\label{sec:topic-result}
We quantify how many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up. The result is an optical baseline rather than a physical gas-depletion measurement.

The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is $0.549 \pm 0.006$, and the median H$\alpha$ luminosity proxy is $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$. The median H$\alpha$ luminosity proxy is approximately 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline. Figure~\ref{fig:topic} shows the downstream subset.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure isolates the 6,729 massive quenched or transitioning galaxies, revealing an optical BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729).}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.

Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs. Optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1, coldgass2, xcoldgass2017, xgass2018}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
We have mapped the optical baseline for 6,729 massive quenched or transitioning galaxies in the SDSS emission-line sample. We find a BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729) and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, approximately 0.66 dex lower than star-forming counterparts. While these quantities define the target selection denominator for future CO gas-fraction versus efficiency programs, direct molecular gas masses and aperture-matched star formation rates remain required to physically distinguish depletion from low efficiency.

\begin{acknowledgments}
We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
\end{acknowledgments}
\begin{thebibliography}{99}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
\end{thebibliography}

\end{document}

exec
/bin/zsh -lc "rg -n \"\\\\cite[p|t]?\\{["'^}]+'"\\}|\\\\ref\\{["'^}]+'"\\}|\\\\label\\{["'^}]+'"\\}|includegraphics|bibliography|begin\\{thebibliography\\}|end\\{thebibliography\\}\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex\" \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex\"" in /Users/duhokim/NebulaMind/NebulaMind
 exited 2 in 0ms:
rg: regex parse error:
    (?:\cite[p|t]?\{[^}]+\}|\ref\{[^}]+\}|\label\{[^}]+\}|includegraphics|bibliography|begin\{thebibliography\}|end\{thebibliography\})
       ^^
error: unrecognized escape sequence

exec
/bin/zsh -lc "sed -n '1,220p' \"/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex\"" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS Target Vector for Feedback-Model Validation}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{SDSS Target Vector for Feedback-Model Validation}
\author{NebulaMind Research Autopilot}
\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
\correspondingauthor{NebulaMind Research Autopilot}
\email{autopilot@nebulamind.ai}

\begin{abstract}
We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define a compact optical target vector for forward-model validation. The pilot records quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$), optical AGN incidence, and color versus mass and redshift across 15 mass-redshift cells with $n \geq 50$; across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). It remains an empirical denominator study rather than a direct simulation comparison.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}

\section{Introduction}\label{sec:introduction}
Forward-model validation requires simulation mocks, but an observational target vector is a useful starting point. Here, the SDSS DR17 emission-line parent sample provides the observational optical baseline for later mock comparison rather than a physical simulation result. We present the SDSS DR17 emission-line sample as a compact optical baseline and restrict the manuscript to directly measured quantities. Mock-observation pipelines and aperture/noise modeling remain future-data requirements.


\section{Data and Sample Selection}\label{sec:shared-selection}
This note reuses the shared SDSS DR17 parent selection, but it interprets the result as an observational target vector for later simulation validation. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{Optical target vector for simulation validation}\label{sec:topic-result}
We define a compact SDSS target vector of quenched fraction, optical AGN incidence, and color versus mass and redshift for forward-model validation. The result is an observed optical baseline rather than a full physical-feedback test.

We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector. Simple Poisson counting errors remain at or below roughly 14\% in those cells, and the grid spans $\log(M_\star/M_\odot)$ bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 crossed with redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). The observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed. Figure~\ref{fig:topic} summarizes the validation grid.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure maps quenched fractions and optical AGN incidence across 15 mass-redshift cells for simulation forward-modeling, spanning $\log(M_\star/M_\odot)$ bins 8.0--9.5 through 11.0--12.5 and redshift bins 0.02--0.05 through 0.08--0.12.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.

Simulation suites such as TNG, EAGLE, and SIMBA define the future comparison problem. The iMaNGA observational catalog \citep{imanga2023} provides a complementary benchmark for mock-observation work. No simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019, eagle2015, simba2019, donnari2021, dubois2013, dubois2016}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector. The grid spans $\log(M_\star/M_\odot)$ bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 across redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). This observed target vector is a compact benchmark for simulation forward modelling, but mock-observation pipelines are still required before any model comparison can be claimed.

\begin{acknowledgments}
We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
\end{acknowledgments}
\begin{thebibliography}{99}
\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
\bibitem[Dav\'e et al.(2019)]{simba2019} Dav\'e, R., Angl\'es-Alc\'azar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
\end{thebibliography}

\end{document}

codex
I’m doing a quick citation/key sanity pass now. If the package is clean on hard LaTeX issues, the only remaining blockers should be the two underfull paragraphs plus a handful of manuscript-level publishability gaps rather than compile failures.
exec
/bin/zsh -lc 'for f in "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers"/*/aastex/*_integrated.tex; do echo "FILE:$f"; nl -ba "$f" | sed -n '"'50,95p'; done" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc 'for f in "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers"/*/data/source_analysis_results.json; do echo "FILE:$f"; sed -n '"'1,220p' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
{
  "analysis_rows": 60000,
  "bpt_counts": {
    "agn": 8146,
    "intermediate": 12234,
    "star-forming": 39553,
    "unclassified": 67
  },
  "data_release": "SDSS DR17 SkyServer via astroquery.sdss",
  "files": {
    "analysis_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
    "figure1_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/figures/figure1_bpt.pdf",
    "figure2_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/figures/figure2_matched_offsets.pdf",
    "matched_pairs_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/matched_agn_sf_pairs.csv",
    "raw_csv": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/sdss_dr17_emission_line_sample.csv"
  },
  "group_medians": {
    "agn": {
      "median_logM": 10.79099,
      "median_log_sSFR": -11.769829999999999,
      "median_u_minus_r": 2.7576649999999994,
      "median_z": 0.075976265,
      "n": 8146
    },
    "intermediate": {
      "median_logM": 10.62895,
      "median_log_sSFR": -10.8564,
      "median_u_minus_r": 2.5431500000000007,
      "median_z": 0.079609505,
      "n": 12234
    },
    "star-forming": {
      "median_logM": 10.01737,
      "median_log_sSFR": -9.909236,
      "median_u_minus_r": 1.814429999999998,
      "median_z": 0.06887668,
      "n": 39553
    },
    "unclassified": {
      "median_logM": 10.87501,
      "median_log_sSFR": -12.06685,
      "median_u_minus_r": 2.8580700000000014,
      "median_z": 0.08311625,
      "n": 67
    }
  },
  "match_abs_delta_logM_median": 0.0044599999999999085,
  "match_abs_delta_z_median": 0.00021079499999999973,
  "match_distance_scaled_median": 0.013706693336996863,
  "matched_delta_log_sSFR_mean_ci95_bootstrap": [
    -1.2194772019150502,
    -1.1835793853118095
  ],
  "matched_delta_log_sSFR_mean_dex": -1.201557615885097,
  "matched_delta_log_sSFR_median_ci95_bootstrap": [
    -1.3341385500000003,
    -1.2821399375
  ],
  "matched_delta_log_sSFR_median_dex": -1.3088869999999995,
  "matched_pairs": 8146,
  "ols_adjusted_for_logM_z": {
    "coef_is_agn_ci95": [
      -1.2103153323534461,
      -1.1873688115826728
    ],
    "coef_is_agn_log_sSFR_dex": -1.1988420719680595,
    "coef_is_agn_se": 0.005853704278258507,
    "coef_logM": -0.6590074792789541,
    "coef_z": 6.926838817644406,
    "n_regression": 47699
  },
  "query_top_n": 60000,
  "raw_rows": 60000,
  "revision_marker": "AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z",
  "run_id": "SDSS_AGN_SFR_PILOT_20260708T122000Z",
  "safety": "read-only public SDSS query; local artifact writes only; no DB/API/page_versions/live wiki publish/deploy/git/cron"
}FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json
{
  "card_id": "rp-2",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp2_environment_quenching/figures/m1_rp2_environment_quenching_figure1.pdf",
  "full_proposal_requires": "group catalogues, robust central/satellite labels, halo masses, morphology, and multi-redshift selection functions.",
  "high_density_quenched": {
    "fraction": 0.2304,
    "k": 3456,
    "n": 15000,
    "se": 0.003438176260752203
  },
  "high_minus_low_ci": [
    0.04059666666666669,
    0.059135
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "low_density_quenched": {
    "fraction": 0.18066666666666667,
    "k": 2710,
    "n": 15000,
    "se": 0.0031414033193486656
  },
  "lpm_high_density_coeff": 0.03249480778035638,
  "lpm_high_density_se": 0.003707733046841099,
  "method": "packet-gated-paper-to-wiki-reconciliation",
  "pilot_question": "Does a nearest-neighbour density proxy add quenched-fraction information beyond stellar mass in the SDSS emission-line sample?",
  "proposal_title": "Separating internal and environmental quenching across stellar mass, halo mass, and redshift",
  "result_bullets": [
    "The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy.",
    "The high-density quartile has quenched fraction 0.230 (3,456/15,000); the low-density quartile has 0.181 (2,710/15,000).",
    "The bootstrap high-minus-low quenched-fraction interval is [0.041, 0.059].",
    "A linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "SDSS density proxy for environmental quenching",
  "slug": "m1_rp2_environment_quenching",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
{
  "card_id": "rp-3",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m1_rp3_maintenance_heating/figures/m1_rp3_maintenance_heating_figure1.pdf",
  "full_proposal_requires": "X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.",
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "massive_agn_fraction": {
    "fraction": 0.4298773929877393,
    "k": 3997,
    "n": 9298,
    "se": 0.005134068554795429
  },
  "massive_quenched_agn_fraction": {
    "fraction": 0.6073748902546093,
    "k": 3459,
    "n": 5695,
    "se": 0.006470987903713825
  },
  "massive_quenched_rows": 5695,
  "massive_rows": 9298,
  "method": "packet-gated-paper-to-wiki-reconciliation",
  "pilot_question": "Among massive, low-sSFR SDSS emission-line galaxies, what optical AGN fraction is available as a denominator for X-ray/radio maintenance-heating follow-up?",
  "proposal_title": "Empirical duty-cycle constraints on AGN maintenance heating in massive halos",
  "result_bullets": [
    "The massive subset (logM >= 10.8) contains 9,298 emission-line galaxies; 5,695 are low-sSFR by the pilot threshold.",
    "The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects.",
    "This provides an optical duty-cycle denominator for X-ray/radio maintenance-heating follow-up, not a heating-to-cooling measurement."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "Optical-AGN denominator for maintenance-heating follow-up",
  "slug": "m1_rp3_maintenance_heating",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
{
  "card_id": "p1",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p1_outflow_escape_recycling/figures/m2_p1_outflow_escape_recycling_figure1.pdf",
  "full_proposal_requires": "resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.",
  "high_excitation_agn": {
    "fraction": 0.074,
    "k": 4440,
    "n": 60000,
    "se": 0.0010686751923136733
  },
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "median_log_sSFR_all": -10.140585,
  "median_log_sSFR_high_excitation": -11.53205,
  "method": "source-first-paper-adjudication",
  "pilot_question": "How large is the SDSS high-excitation optical-AGN denominator that would need resolved kinematics to test escape versus recycling?",
  "proposal_title": "Escape versus recycling: the fate of AGN-driven multiphase outflows",
  "result_bullets": [
    "High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074).",
    "Their median log sSFR is -11.53, compared with -10.14 for the full denominator.",
    "SDSS does not measure escape velocity or multiphase outflow velocities here; the pilot supplies a denominator for resolved follow-up rather than an escape/recycling result."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "SDSS high-excitation AGN denominator for outflow escape tests",
  "slug": "m2_p1_outflow_escape_recycling",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
{
  "card_id": "p2",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p2_radio_jet_environment/figures/m2_p2_radio_jet_environment_figure1.pdf",
  "full_proposal_requires": "radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.",
  "high_density_massive_agn": {
    "fraction": 0.5085836909871244,
    "k": 948,
    "n": 1864,
    "se": 0.011579319665266517
  },
  "high_minus_low_ci": [
    0.11189880364416133,
    0.1702164814837969
  ],
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "low_density_massive_agn": {
    "fraction": 0.3667152221412964,
    "k": 1007,
    "n": 2746,
    "se": 0.009196312633686535
  },
  "massive_rows": 9298,
  "method": "source-first-paper-adjudication",
  "pilot_question": "Does a local-density proxy modulate the optical AGN fraction in massive SDSS hosts, motivating environment-stratified radio/X-ray jet-coupling follow-up?",
  "proposal_title": "Environmental dependence of radio-jet coupling efficiency in galaxy gas",
  "result_bullets": [
    "Among massive hosts, the high-density quartile has optical AGN fraction 0.509; the low-density quartile has 0.367.",
    "The bootstrap high-minus-low interval is [0.112, 0.170].",
    "This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "Environment proxy for optical AGN in massive SDSS hosts",
  "slug": "m2_p2_radio_jet_environment",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
{
  "agn_fraction_by_mass": [
    0.0027030347708563705,
    0.013751792795072977,
    0.07734113712374582,
    0.2602886157135222,
    0.5202082816761716
  ],
  "card_id": "p3",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p3_feedback_transition_mass/figures/m2_p3_feedback_transition_mass_figure1.pdf",
  "full_proposal_requires": "gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.",
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "mass_bin_labels": [
    "8.0-9.5",
    "9.5-10.0",
    "10.0-10.5",
    "10.5-11.0",
    "11.0-12.5"
  ],
  "method": "source-first-paper-adjudication",
  "peak_agn_fraction": 0.5202082816761716,
  "peak_agn_mass_bin": "11.0-12.5",
  "pilot_question": "At what stellar-mass scale do quenched fraction and optical AGN incidence rise in the same SDSS denominator?",
  "proposal_title": "Locating the transition from stellar-feedback to AGN-feedback regulation",
  "quenched_fraction_by_mass": [
    0.005283204324855633,
    0.025816249050873197,
    0.1311663879598662,
    0.39254112476987946,
    0.7292338209769402
  ],
  "result_bullets": [
    "The first stellar-mass bin with quenched fraction above 0.5 is 11.0-12.5.",
    "The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520.",
    "The result is an optical transition diagnostic; gas fractions and baryon deficits are needed before assigning the transition to stellar or AGN feedback."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "SDSS mass transition in quenching and optical AGN incidence",
  "slug": "m2_p3_feedback_transition_mass",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "transition_mass_bin_quenched_fraction_gt_0p5": "11.0-12.5"
}FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json
{
  "card_id": "p1",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p1_multiphase_census/figures/m3_p1_multiphase_census_figure1.pdf",
  "full_proposal_requires": "ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.",
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "method": "debate-map-to-wiki-rebuild",
  "pilot_question": "How strongly do simple optical tracer definitions change the inferred AGN/feedback-candidate prevalence in one common SDSS denominator?",
  "prevalence_ratio_widest_to_narrowest": 3.080775840903511,
  "proposal_title": "A multiphase, common-denominator census of AGN-driven outflows",
  "result_bullets": [
    "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418.",
    "The widest-to-narrowest prevalence ratio is 3.1, before adding molecular, neutral, or X-ray/radio phases.",
    "This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "Common-denominator optical tracer census in SDSS",
  "slug": "m3_p1_multiphase_census",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "tracer_prevalence": {
    "BPT AGN": {
      "fraction": 0.13576666666666667,
      "k": 8146,
      "n": 60000,
      "se": 0.0013984162404239596
    },
    "high [NII]/Ha": {
      "fraction": 0.19161666666666666,
      "k": 11497,
      "n": 60000,
      "se": 0.0016067551136904373
    },
    "high [OIII]/Hb": {
      "fraction": 0.31698333333333334,
      "k": 19019,
      "n": 60000,
      "se": 0.0018995828477248288
    },
    "low-sSFR+emission": {
      "fraction": 0.20683333333333334,
      "k": 12410,
      "n": 60000,
      "se": 0.0016535482331215075
    },
    "red+emission": {
      "fraction": 0.4182666666666667,
      "k": 25096,
      "n": 60000,
      "se": 0.002013784423344193
    }
  }
}FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
{
  "agn_fraction_in_denominator": {
    "fraction": 0.5486699360974885,
    "k": 3692,
    "n": 6729,
    "se": 0.006066349807598532
  },
  "card_id": "p2",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p2_gas_depletion_efficiency/figures/m3_p2_gas_depletion_efficiency_figure1.pdf",
  "full_proposal_requires": "CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.",
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "massive_transition_quenched_rows": 6729,
  "median_log_lha_denominator": 40.06117405071403,
  "median_log_lha_offset_vs_massive_sf": -0.6585859816891073,
  "method": "debate-map-to-wiki-rebuild",
  "pilot_question": "How many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction/depletion-time follow-up?",
  "proposal_title": "Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies",
  "result_bullets": [
    "The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.",
    "Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.",
    "The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.",
    "SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "Optical denominator for gas-fraction versus efficiency tests",
  "slug": "m3_p2_gas_depletion_efficiency",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv"
}FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json
{
  "agn_fraction_range": [
    0.0027030347708563705,
    0.5202082816761716
  ],
  "card_id": "p3",
  "figure_pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/figures/m3_p3_simulation_validation_figure1.pdf",
  "full_proposal_requires": "simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.",
  "interpretation_guard": "SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page.",
  "method": "debate-map-to-wiki-rebuild",
  "pilot_question": "What compact SDSS target vector of quenched fraction, optical AGN incidence, and colour versus mass/redshift can be used for forward-model validation?",
  "proposal_title": "Forward-modelled validation of cosmological feedback prescriptions",
  "quenched_fraction_range": [
    0.005283204324855633,
    0.7292338209769402
  ],
  "result_bullets": [
    "The pilot writes 15 mass-redshift cells with n >= 50 as a compact validation vector.",
    "Across mass bins, quenched fractions span 0.005-0.729; optical AGN fractions span 0.003-0.520.",
    "The output is an observed target vector for simulation forward modelling, not a direct simulation comparison."
  ],
  "run_id": "SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z",
  "sample_rows": 60000,
  "short_title": "SDSS target vector for feedback-model validation",
  "slug": "m3_p3_simulation_validation",
  "source_sample": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv",
  "target_vector_cells": [
    {
      "agn_fraction": 0.002902757619738752,
      "mass_bin": "8.0-9.5",
      "median_u_minus_r": 1.5324300000000015,
      "n": 6201,
      "quenched_fraction": 0.006450572488308337,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.0006105006105006105,
      "mass_bin": "8.0-9.5",
      "median_u_minus_r": 1.378694999999999,
      "n": 1638,
      "quenched_fraction": 0.0006105006105006105,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.01,
      "mass_bin": "8.0-9.5",
      "median_u_minus_r": 1.0446000000000009,
      "n": 300,
      "quenched_fraction": 0.006666666666666667,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.030219018574993067,
      "mass_bin": "9.5-10.0",
      "median_u_minus_r": 1.8540899999999991,
      "n": 3607,
      "quenched_fraction": 0.06099251455503188,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.008417230566100017,
      "mass_bin": "9.5-10.0",
      "median_u_minus_r": 1.6964299999999994,
      "n": 6059,
      "quenched_fraction": 0.013038455190625516,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.0013717421124828531,
      "mass_bin": "9.5-10.0",
      "median_u_minus_r": 1.5156199999999984,
      "n": 2187,
      "quenched_fraction": 0.003200731595793324,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.15361242403781228,
      "mass_bin": "10.0-10.5",
      "median_u_minus_r": 2.2637100000000006,
      "n": 2962,
      "quenched_fraction": 0.25557056043214044,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.09022556390977443,
      "mass_bin": "10.0-10.5",
      "median_u_minus_r": 2.119389999999999,
      "n": 7581,
      "quenched_fraction": 0.160928637382931,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.03968346328406843,
      "mass_bin": "10.0-10.5",
      "median_u_minus_r": 1.9204700000000017,
      "n": 8593,
      "quenched_fraction": 0.06202723146747353,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.42955145118733506,
      "mass_bin": "10.5-11.0",
      "median_u_minus_r": 2.6227300000000007,
      "n": 1895,
      "quenched_fraction": 0.5810026385224274,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.2968719260279363,
      "mass_bin": "10.5-11.0",
      "median_u_minus_r": 2.5802999999999994,
      "n": 5083,
      "quenched_fraction": 0.45130828251032856,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.2089037622959132,
      "mass_bin": "10.5-11.0",
      "median_u_minus_r": 2.45496,
      "n": 9861,
      "quenched_fraction": 0.3260318426123111,
      "z_bin": "0.08-0.12"
    },
    {
      "agn_fraction": 0.6102564102564103,
      "mass_bin": "11.0-12.5",
      "median_u_minus_r": 2.83066,
      "n": 390,
      "quenched_fraction": 0.8564102564102564,
      "z_bin": "0.02-0.05"
    },
    {
      "agn_fraction": 0.5629691409507923,
      "mass_bin": "11.0-12.5",
      "median_u_minus_r": 2.850570000000001,
      "n": 1199,
      "quenched_fraction": 0.804837364470392,
      "z_bin": "0.05-0.08"
    },
    {
      "agn_fraction": 0.484860883797054,
      "mass_bin": "11.0-12.5",
      "median_u_minus_r": 2.8379250000000003,
      "n": 2444,
      "quenched_fraction": 0.6718494271685761,
      "z_bin": "0.08-0.12"
    }
  ]
}
 succeeded in 0ms:
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR and sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
    55	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects; the BPT partition is shown in Figure~\ref{fig:bpt}.
    56	
    57	The preferred estimator matches every broad optical AGN host to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. This is an association design; controls are not matched in morphology, halo mass, gas mass, aperture scale, AGN luminosity, or duty-cycle phase.
    58	
    59	Our comparison of broad BPT optical AGN hosts versus star-forming controls at S/N$\geq 3$ matches $N=8,146$ pairs, measuring a median specific star formation rate offset of $\Delta\log {\rm sSFR}=-1.309$ dex with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Applying a moderate mass-redshift caliper of $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$ retains $N=7,867$ pairs (96.6\% target coverage) and yields a median offset of $-1.318$ dex. A deterministic matching run without replacement yields $N=7,419$ matched pairs and a median offset of $-1.446$ dex, though with poorer stellar-mass balance. Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to $-0.744$ dex, and a narrower [N II] Seyfert-like proxy yields $N=2,114$ pairs and a median offset of $-0.763$ dex; these selection sensitivities are summarized in Figure~\ref{fig:offsets}.
    60	
    61	
    62	\begin{figure*}
    63	\centering
    64	\includegraphics[width=0.73\textwidth]{../figures/fig-bpt.pdf}
    65	\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used in the RP-1 analysis. This figure documents the optical selection and classification boundary; it does not by itself identify causal AGN feedback.}
    66	\label{fig:bpt}
    67	\end{figure*}
    68	
    69	\begin{figure*}
    70	\centering
    71	\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
    72	\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset, $\Delta\log {\rm sSFR}=-1.309$ dex, is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
    73	\label{fig:offsets}
    74	\end{figure*}
    75	
    76	
    77	\section{Data Availability}\label{sec:data-avail}
    78	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    79	
    80	\section{Conclusion}\label{sec:conclusion}
    81	In the capped SDSS DR17 emission-line subset, broad BPT optical AGN hosts show a median sSFR offset of $-1.309$ dex relative to mass--redshift matched controls, with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Although the offset amplitude is highly dependent on the emission-line selection function (decreasing to $-0.744$ dex at S/N$\geq 10$), the interval remains securely negative. These measurements establish a robust optical association baseline, which will require future molecular gas or direct outflow kinematics follow-up to isolate any causal AGN quenching mechanisms.
    82	
    83	\begin{acknowledgments}
    84	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    85	\end{acknowledgments}
    86	\begin{thebibliography}{99}
    87	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    88	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    89	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    90	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    91	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    92	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    93	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    94	
    95	\end{thebibliography}
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
    55	We examine whether a nearest-neighbor density proxy adds quenched-fraction information beyond stellar mass in the SDSS emission-line sample. The result is an optical baseline rather than a full physical-feedback test.
    56	
    57	Within the same 60,000-galaxy denominator, the high-density quartile has a quenched fraction of $0.230 \pm 0.003$ ($3,456/15,000$), compared with $0.181 \pm 0.003$ ($2,710/15,000$) in the low-density quartile. The bootstrap high-minus-low difference interval is $[0.041, 0.059]$, which excludes zero. After controlling for log stellar mass and redshift, a linear probability model yields a high-density coefficient of $0.032 \pm 0.004$, so the density proxy remains correlated with quenching independently of those host-galaxy properties. Figure~\ref{fig:topic} summarizes the proxy split used in this baseline.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure summarizes the equal-count density-quartile split, where the high-density quartile reaches a quenched fraction of 0.230 $\pm$ 0.003, establishing the baseline for future group-catalog analyses.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only baseline does not include group catalogues, robust central/satellite labels, halo masses, morphology, or multi-redshift selection functions. Those data are required before the density proxy can be interpreted as a physical environmental-quenching measurement.
    69	
    70	Because the density proxy is projected on the sky, fiber-collision and redshift-space incompleteness can dilute nearest-neighbor estimates; future group-catalog work should correct those effects explicitly.
    71	
    72	Mass and environment are separable axes in low-redshift galaxy evolution. A real environmental-quenching analysis therefore requires group and halo information beyond this nearest-neighbor proxy, together with central/satellite labels and the literature context provided by \citet{peng2010,baldry2006,wetzel2013,goubert2024}.
    73	
    74	
    75	\section{Data Availability}\label{sec:data-avail}
    76	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	The SDSS-only proxy shows a high-density quenched fraction of 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile, with a mass- and redshift-adjusted high-density coefficient of $0.032 \pm 0.004$. These values define an optical environmental baseline, but a full quenching interpretation still requires group catalogs, halo masses, and central/satellite labels.
    80	
    81	\begin{acknowledgments}
    82	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    83	\end{acknowledgments}
    84	\begin{thebibliography}{99}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., Balogh, M.~L., Bower, R.~G., et al. 2006, MNRAS, 373, 469
    93	\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, MNRAS, 528, 3822
    94	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    95	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for maintenance-heating follow-up}\label{sec:topic-result}
    55	Among massive, low-sSFR SDSS emission-line galaxies, we quantify the optical AGN fraction available as a denominator for X-ray and radio maintenance-heating follow-up. The result is an optical baseline rather than a calorimetric measurement.
    56	
    57	The massive galaxy subset ($\log M_\star \geq 10.8$) contains 9,298 emission-line galaxies, of which 5,695 are classified as low-sSFR based on the specific star formation rate threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$ applied in this analysis. The optical BPT AGN fraction is measured as 0.430 (3,997/9,298) in the total massive subset, rising to 0.607 (3,459/5,695) when restricting the sample to massive low-sSFR objects. This empirical duty-cycle baseline is intended for future X-ray or radio maintenance-heating follow-up and is not a heating measurement. Figure~\ref{fig:topic} shows the corresponding optical denominator.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for maintenance-heating follow-up. The figure highlights that among massive, low-sSFR objects, the BPT-AGN fraction is 0.607, providing a duty-cycle denominator for future X-ray/radio studies.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires X-ray cavity and cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.
    69	
    70	Radio-mode and hot-atmosphere studies define the future calorimetric observables: jet power, cavities, cooling luminosity, and group gas. Those observables are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	The massive subset contains 9,298 emission-line galaxies, with 5,695 classified as low-sSFR by the pilot threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$. The BPT AGN fraction rises from 0.430 (3,997/9,298) in the massive subset to 0.607 (3,459/5,695) in the massive low-sSFR subset, defining an optical duty-cycle denominator for maintenance-heating follow-up rather than a direct heating result.
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	\begin{thebibliography}{99}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    91	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
    92	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
    93	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    94	\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New J. Phys., 14, 055023
    95	\end{thebibliography}
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
    55	This note quantifies the BPT-selected optical AGN denominator needed for future resolved-kinematics tests of escape versus recycling. The result is an optical baseline rather than a direct escape-velocity measurement. ``BPT-selected optical AGN candidates'' here means the optical AGN subset counted above; it is shorthand for the denominator, not a separate kinematic or energy measurement.
    56	
    57	BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies ($0.074 \pm 0.001$). Their median $\log {\rm sSFR}$ is $-11.53$, compared with $-10.14$ for the full denominator. This optical sample defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate. Figure~\ref{fig:topic} shows the target-selection baseline.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure summarizes the 4,440-object BPT-selected denominator and the associated median $\log {\rm sSFR} = -11.53$ used for target definition.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.
    69	
    70	Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005, cicone2014, fiore2017, carniani2017, fabian2012}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074 $\pm$ 0.001), and their median $\log {\rm sSFR}$ is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	\begin{thebibliography}{99}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
    91	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    92	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
    93	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    94	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    95	\end{thebibliography}
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
    55	We examine whether a local-density proxy modulates the optical AGN fraction in massive SDSS hosts. The result is an environment-stratified optical baseline for future radio and X-ray jet-coupling work.
    56	
    57	Among massive hosts, the high-density quartile has optical AGN fraction $0.509 \pm 0.012$, while the low-density quartile has $0.367 \pm 0.012$. The bootstrap high-minus-low interval is $[0.112,0.170]$. This is an optical/environment denominator for radio-jet coupling work and does not measure jet power or coupling efficiency. Figure~\ref{fig:topic} shows the environment split.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure demonstrates the environment-stratified target set, with the optical AGN fraction rising to 0.509 $\pm$ 0.012 in the high-density quartile of massive hosts.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.
    69	
    70	Because the density proxy is projected on the sky, fiber-collision and redshift-space incompleteness can dilute nearest-neighbor estimates; future radio-jet follow-up should correct those effects explicitly.
    71	
    72	The radio, X-ray, and group literature motivates environment-stratified follow-up. The present result is only an optical BPT-AGN fraction versus an internal density proxy rather than a direct jet-coupling measurement \citep{best2005,santoro2020,mcnamara2007,eckert2024}.
    73	
    74	
    75	\section{Data Availability}\label{sec:data-avail}
    76	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    77	
    78	\section{Conclusion}\label{sec:conclusion}
    79	Among massive hosts, the optical AGN fraction is 0.509 $\pm$ 0.012 in the high-density quartile and 0.367 $\pm$ 0.012 in the low-density quartile, with a bootstrap difference of [0.112, 0.170]. This establishes an environment-stratified optical denominator for radio-jet coupling studies, not a direct coupling measurement.
    80	
    81	\begin{acknowledgments}
    82	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    83	\end{acknowledgments}
    84	\begin{thebibliography}{99}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    93	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
    94	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    95	\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
    55	We identify the stellar-mass scale at which quenched fraction and optical AGN incidence rise together in the SDSS emission-line sample. The result is an empirical optical transition vector rather than a full physical-feedback test.
    56	
    57	The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$. In that same bin, the optical AGN fraction peaks at 0.520 (2,098/4,033). These results define an empirical transition vector, but gas fractions and baryon deficits are still required before assigning the trend to stellar or AGN feedback. Figure~\ref{fig:topic} highlights the transition bin.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows the high-mass tail ($\log(M_\star/M_\odot) > 11.0$) where the quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520 (2,098/4,033).}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
    69	
    70	Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition. Those data are the missing ingredients behind the optical trend \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$. In that same bin, the optical AGN fraction peaks at 0.520 (2,098/4,033). These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation.
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	\begin{thebibliography}{99}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
    91	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    92	\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
    93	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
    94	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    95	\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical census of multiphase target denominators}\label{sec:topic-result}
    55	We examine how simple optical tracer definitions change the inferred AGN and feedback-candidate prevalence within one common SDSS denominator. The result is an optical baseline for later multiphase follow-up rather than a direct multiphase measurement.
    56	
    57	Within the same 60,000-galaxy denominator, the BPT AGN and red+emission definitions produce prevalence from 0.136 for BPT AGN to 0.418 for red+emission, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases. Figure~\ref{fig:topic} summarizes the tracer spread.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure illustrates how the BPT AGN and red+emission definitions yield AGN candidate prevalence ranging from 0.136 for BPT AGN to 0.418 for red+emission within the same denominator.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.
    69	
    70	A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005, rupke2018, cicone2014, fiore2017, feruglio2015, woo2016, bae2018}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	Within the 60,000-galaxy denominator, the BPT AGN and red+emission definitions change prevalence from 0.136 for BPT AGN to 0.418 for red+emission, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases.
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	\begin{thebibliography}{99}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
    91	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    92	\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
    93	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    94	\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
    95	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
    50	
    51	
    52	\section{Measurements}\label{sec:measurements}
    53	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    54	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    55	
    56	
    57	\section{Optical denominator for gas-fraction versus efficiency tests}\label{sec:topic-result}
    58	We quantify how many massive quenched or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up. The result is an optical baseline rather than a physical gas-depletion measurement.
    59	
    60	The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is $0.549 \pm 0.006$, and the median H$\alpha$ luminosity proxy is $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$. The median H$\alpha$ luminosity proxy is approximately 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline. Figure~\ref{fig:topic} shows the downstream subset.
    61	
    62	
    63	\begin{figure}
    64	\centering
    65	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    66	\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure isolates the 6,729 massive quenched or transitioning galaxies, revealing an optical BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729).}
    67	\label{fig:topic}
    68	\end{figure}
    69	
    70	\section{Interpretation and missing observables}\label{sec:missing}
    71	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.
    72	
    73	Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs. Optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1, coldgass2, xcoldgass2017, xgass2018}.
    74	
    75	
    76	\section{Data Availability}\label{sec:data-avail}
    77	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    78	
    79	\section{Conclusion}\label{sec:conclusion}
    80	We have mapped the optical baseline for 6,729 massive quenched or transitioning galaxies in the SDSS emission-line sample. We find a BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729) and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, approximately 0.66 dex lower than star-forming counterparts. While these quantities define the target selection denominator for future CO gas-fraction versus efficiency programs, direct molecular gas masses and aperture-matched star formation rates remain required to physically distinguish depletion from low efficiency.
    81	
    82	\begin{acknowledgments}
    83	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    84	\end{acknowledgments}
    85	\begin{thebibliography}{99}
    86	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    87	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    88	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    89	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    90	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    91	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    92	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    93	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
    94	\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
    95	\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical target vector for simulation validation}\label{sec:topic-result}
    55	We define a compact SDSS target vector of quenched fraction, optical AGN incidence, and color versus mass and redshift for forward-model validation. The result is an observed optical baseline rather than a full physical-feedback test.
    56	
    57	We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector. Simple Poisson counting errors remain at or below roughly 14\% in those cells, and the grid spans $\log(M_\star/M_\odot)$ bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 crossed with redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). The observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed. Figure~\ref{fig:topic} summarizes the validation grid.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure maps quenched fractions and optical AGN incidence across 15 mass-redshift cells for simulation forward-modeling, spanning $\log(M_\star/M_\odot)$ bins 8.0--9.5 through 11.0--12.5 and redshift bins 0.02--0.05 through 0.08--0.12.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires simulation mocks passed through the SDSS/MaNGA/ALMA/X-ray/radio selection functions and aperture/noise models.
    69	
    70	Simulation suites such as TNG, EAGLE, and SIMBA define the future comparison problem. The iMaNGA observational catalog \citep{imanga2023} provides a complementary benchmark for mock-observation work. No simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019, eagle2015, simba2019, donnari2021, dubois2013, dubois2016}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector. The grid spans $\log(M_\star/M_\odot)$ bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 across redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). This observed target vector is a compact benchmark for simulation forward modelling, but mock-observation pipelines are still required before any model comparison can be claimed.
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	\begin{thebibliography}{99}
    83	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    84	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    85	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    86	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    87	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    88	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    89	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    90	\bibitem[Dav\'e et al.(2019)]{simba2019} Dav\'e, R., Angl\'es-Alc\'azar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
    91	\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
    92	\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
    93	\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
    94	\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
    95	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2

exec
/bin/zsh -lc 'for f in "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers"/*/aastex/*_integrated.tex; do echo "FILE:$f"; rg -n "'"\\\\citep?\\{|\\\\ref\\{|\\\\label\\{|\\\\includegraphics\" \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 exited 2 in 0ms:
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
rg: regex parse error:
    (?:\citep?\{|\ref\{|\label\{|\includegraphics)
       ^^
error: unrecognized escape sequence
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
rg: regex parse error:
    (?:\citep?\{|\ref\{|\label\{|\includegraphics)
       ^^
error: unrecognized escape sequence
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
rg: regex parse error:
    (?:\citep?\{|\ref\{|\label\{|\includegraphics)
       ^^
error: unrecognized escape sequence
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
rg: regex parse error:
    (?:\citep?\{|\ref\{|\label\{|\includegraphics)
       ^^
error: unrecognized escape sequence
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
rg: regex parse error:
    (?:\citep?\{|\ref\{|\label\{|\includegraphics)
       ^^
error: unrecognized escape sequence
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
rg: regex parse error:
    (?:\citep?\{|\ref\{|\label\{|\includegraphics)
       ^^
error: unrecognized escape sequence
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
rg: regex parse error:
    (?:\citep?\{|\ref\{|\label\{|\includegraphics)
       ^^
error: unrecognized escape sequence
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
rg: regex parse error:
    (?:\citep?\{|\ref\{|\label\{|\includegraphics)
       ^^
error: unrecognized escape sequence
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
rg: regex parse error:
    (?:\citep?\{|\ref\{|\label\{|\includegraphics)
       ^^
error: unrecognized escape sequence

exec
/bin/zsh -lc 'for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/*/aastex/*_integrated.tex; do echo "FILE:$f"; cites=$(perl -ne '"'while(/\\\\cite[pt]?(?:\\[["'^'"\\]]*\\])?\\{(["'^}]*)'"\\}/g){print \""'$1'"\\n\"}' \""'$f" | tr '"',' '\\n' | sed 's/"'^ *//;s/ *$//'"' | sort -u); bibs="'$(perl -ne '"'while(/\\\\bibitem(?:\\[["'^]]*'"\\])?\\{(["'^}]*)'"\\}/g){print \""'$1'"\\n\"}' \""'$f" | sort -u); comm -23 <(printf "%s'"\\n\" \""'$cites" | sort -u) <(printf "%s'"\\n\" \""'$bibs" | sort -u) | sed '"'s/"'^/MISSING: /'"'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 122ms:
FILE:/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex

codex
**LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_01 status:** `ISSUES_FOUND`

**Files/paths inspected**
- Context roots used:
  - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers`
  - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z`
  - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/public-promotions/PUBLIC_STATIC_PDF_PROMOTION_20260709T233457Z`
- Audit files inspected:
  - `.../cycle_01_nine_papers/CYCLE_01_BEFORE_STRICT_LATEX_AUDIT.md`
  - `.../cycle_01_nine_papers/CYCLE_01_BEFORE_TEX_LINT.json`
- TeX files inspected:
  - `.../01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
  - `.../02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
  - `.../03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex`
  - `.../04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
  - `.../05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex`
  - `.../06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
  - `.../07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex`
  - `.../08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
  - `.../09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`
- Local evidence files inspected:
  - all nine `data/source_analysis_results.json` files under the same nine paper directories

**Strict LaTeX blockers**
- No fatal compile errors were found.
- No undefined references/citations were found.
- No missing figure files were found in the candidate package.
- Remaining strict-audit blockers are layout warnings plus one rerun warning:
  - `02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
    - `L578`: `Underfull \hbox (badness 1019) in paragraph at lines 57--58`
    - `L585`: `Underfull \hbox (badness 1931) in paragraph at lines 72--73`
    - These correspond to the long result sentence in `\section{SDSS density-proxy result for environmental quenching}` and the long literature/context sentence in `\section{Interpretation and missing observables}`.
  - `06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
    - `L579`: `Underfull \hbox (badness 2134) in paragraph at lines 57--58`
    - `L586`: `Underfull \hbox (badness 2134) in paragraph at lines 77--78`
    - These correspond to the long transition-result sentence and the conclusion paragraph.
  - `08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
    - `L583`: `LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.`
    - This is not a content bug, but it means the strict compile audit is not fully settled until the file is recompiled cleanly.

**Publishability blockers**
- No hard AAS publishability blocker was found that invalidates the science in these nine papers.
- Main publishability risks are tone and framing, not missing data:
  - `06_m2_p3_feedback_transition_mass_integrated.tex`
    - The title/section framing still leans causal with `feedback transition` even though the manuscript explicitly says it is only an optical transition vector.
    - This is acceptable only if the causal language stays consistently subordinated to the caveat that gas fractions, baryon deficits, and halo-scale data are still missing.
  - `09_m3_p3_simulation_validation_integrated.tex`
    - The word `validation` in the title is slightly ahead of the actual content, because the paper explicitly says no simulation mock has been forward-modelled or ranked yet.
    - Safer framing is to keep it clearly as an observational target vector for future validation, not a validation result.
  - `02_m1_rp2_environment_quenching_integrated.tex`
    - The paper is careful, but the phrase `environmental quenching` in title and section headers can read stronger than the data support unless the baseline/proxy limitation is kept front and center.
- Source-role/citation problems:
  - None were found as blockers. The cited keys present in the TeX are backed by bibliography entries in each file.
- Figure/table caption issues:
  - No missing captions or broken cross-references were found.
  - Captions are generally serviceable, but several could be even more explicit that the figures show optical denominators/baselines rather than physical mechanisms.
- Reader-flow issues:
  - The manuscripts are repetitive by design. The main flow risk is that the repeated caveat paragraphs can bury the actual measurement; this is not fatal, but it is the most likely place for editorial pushback.

**Exact feed for the writer**
- `02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
  - `\section{SDSS density-proxy result for environmental quenching}` around lines 54-57:
    - Split the long result paragraph into shorter sentences or move the numeric summary into a compact table callout.
    - Preserve the measured values exactly: high-density quenched fraction `0.230 ± 0.003` (`3456/15000`), low-density `0.181 ± 0.003` (`2710/15000`), bootstrap interval `[0.041, 0.059]`, adjusted coefficient `0.032 ± 0.004`.
  - `\section{Interpretation and missing observables}` around lines 67-72:
    - Shorten the final literature/context sentence to avoid the underfull box.
    - Keep the caveat that group catalogues, halo masses, and central/satellite labels are missing.
  - If you want to soften framing, change `environmental quenching` in the title/section label to `environmental-quenching baseline` or `environmental-quenching proxy`.
- `06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
  - `\section{Optical denominator for feedback-transition mass}` around lines 54-57:
    - Consider renaming this section to `Optical denominator for quenching-transition mass` or `Optical transition baseline` to reduce causal overclaim.
    - Keep the real transition result unchanged: first mass bin with quenched fraction above `0.5` is `11.0--12.5`, and the optical AGN fraction peaks there at `0.520 (2098/4033)`.
  - `\section{Conclusion}` around lines 76-78:
    - Split the concluding sentence if needed to eliminate the underfull box.
    - Preserve the caution that gas fractions, baryon deficits, and halo-scale measurements are still required.
- `08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
  - No TeX content error fix is needed from the audit, but the file needs one more LaTeX run to settle labels/cross-references.
  - Preserve the measured values exactly: `6729` galaxies, BPT AGN fraction `0.549 ± 0.006` (`3692/6729`), median `log(L_Hα / erg s^-1) = 40.06`, offset `-0.66` dex.
- `09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`
  - Consider softening the title or abstract wording from `validation` to `future validation` or `observational target vector for validation`.
  - Preserve the real-data limits exactly: `15` mass-redshift cells with `n >= 50`, quenched fractions spanning `0.005--0.729`, optical AGN fractions spanning `0.003--0.520`.
- Global writer instruction for all nine files:
  - Do not change the measured numbers, sample sizes, or real-data bounds.
  - Keep every caveat that says the manuscripts are optical baselines/denominators only.
  - No edits are needed for missing figures or undefined citations; the package is already internally consistent there.

**Safety ledger**
- No edits made.
- No public PDF replacement.
- No database, SQL, `/api/pages`, page_versions, wiki publish, trust recompute, or data mutation.
- No deploy/restart.
- No git commit/push/merge/rebase/history rewrite.
- No cron creation/update/removal.
- No billing, cloud, OAuth, API-key, account, credential, token, or cookie access.
- No external manuscript submission.
tokens used
57,300
**LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_01 status:** `ISSUES_FOUND`

**Files/paths inspected**
- Context roots used:
  - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_01_nine_papers`
  - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/integration-runs/INTEGRATED_9_PAPERS_20260709T012051Z`
  - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/public-promotions/PUBLIC_STATIC_PDF_PROMOTION_20260709T233457Z`
- Audit files inspected:
  - `.../cycle_01_nine_papers/CYCLE_01_BEFORE_STRICT_LATEX_AUDIT.md`
  - `.../cycle_01_nine_papers/CYCLE_01_BEFORE_TEX_LINT.json`
- TeX files inspected:
  - `.../01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
  - `.../02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
  - `.../03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex`
  - `.../04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex`
  - `.../05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex`
  - `.../06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
  - `.../07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex`
  - `.../08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
  - `.../09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`
- Local evidence files inspected:
  - all nine `data/source_analysis_results.json` files under the same nine paper directories

**Strict LaTeX blockers**
- No fatal compile errors were found.
- No undefined references/citations were found.
- No missing figure files were found in the candidate package.
- Remaining strict-audit blockers are layout warnings plus one rerun warning:
  - `02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
    - `L578`: `Underfull \hbox (badness 1019) in paragraph at lines 57--58`
    - `L585`: `Underfull \hbox (badness 1931) in paragraph at lines 72--73`
    - These correspond to the long result sentence in `\section{SDSS density-proxy result for environmental quenching}` and the long literature/context sentence in `\section{Interpretation and missing observables}`.
  - `06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
    - `L579`: `Underfull \hbox (badness 2134) in paragraph at lines 57--58`
    - `L586`: `Underfull \hbox (badness 2134) in paragraph at lines 77--78`
    - These correspond to the long transition-result sentence and the conclusion paragraph.
  - `08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
    - `L583`: `LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.`
    - This is not a content bug, but it means the strict compile audit is not fully settled until the file is recompiled cleanly.

**Publishability blockers**
- No hard AAS publishability blocker was found that invalidates the science in these nine papers.
- Main publishability risks are tone and framing, not missing data:
  - `06_m2_p3_feedback_transition_mass_integrated.tex`
    - The title/section framing still leans causal with `feedback transition` even though the manuscript explicitly says it is only an optical transition vector.
    - This is acceptable only if the causal language stays consistently subordinated to the caveat that gas fractions, baryon deficits, and halo-scale data are still missing.
  - `09_m3_p3_simulation_validation_integrated.tex`
    - The word `validation` in the title is slightly ahead of the actual content, because the paper explicitly says no simulation mock has been forward-modelled or ranked yet.
    - Safer framing is to keep it clearly as an observational target vector for future validation, not a validation result.
  - `02_m1_rp2_environment_quenching_integrated.tex`
    - The paper is careful, but the phrase `environmental quenching` in title and section headers can read stronger than the data support unless the baseline/proxy limitation is kept front and center.
- Source-role/citation problems:
  - None were found as blockers. The cited keys present in the TeX are backed by bibliography entries in each file.
- Figure/table caption issues:
  - No missing captions or broken cross-references were found.
  - Captions are generally serviceable, but several could be even more explicit that the figures show optical denominators/baselines rather than physical mechanisms.
- Reader-flow issues:
  - The manuscripts are repetitive by design. The main flow risk is that the repeated caveat paragraphs can bury the actual measurement; this is not fatal, but it is the most likely place for editorial pushback.

**Exact feed for the writer**
- `02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
  - `\section{SDSS density-proxy result for environmental quenching}` around lines 54-57:
    - Split the long result paragraph into shorter sentences or move the numeric summary into a compact table callout.
    - Preserve the measured values exactly: high-density quenched fraction `0.230 ± 0.003` (`3456/15000`), low-density `0.181 ± 0.003` (`2710/15000`), bootstrap interval `[0.041, 0.059]`, adjusted coefficient `0.032 ± 0.004`.
  - `\section{Interpretation and missing observables}` around lines 67-72:
    - Shorten the final literature/context sentence to avoid the underfull box.
    - Keep the caveat that group catalogues, halo masses, and central/satellite labels are missing.
  - If you want to soften framing, change `environmental quenching` in the title/section label to `environmental-quenching baseline` or `environmental-quenching proxy`.
- `06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex`
  - `\section{Optical denominator for feedback-transition mass}` around lines 54-57:
    - Consider renaming this section to `Optical denominator for quenching-transition mass` or `Optical transition baseline` to reduce causal overclaim.
    - Keep the real transition result unchanged: first mass bin with quenched fraction above `0.5` is `11.0--12.5`, and the optical AGN fraction peaks there at `0.520 (2098/4033)`.
  - `\section{Conclusion}` around lines 76-78:
    - Split the concluding sentence if needed to eliminate the underfull box.
    - Preserve the caution that gas fractions, baryon deficits, and halo-scale measurements are still required.
- `08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex`
  - No TeX content error fix is needed from the audit, but the file needs one more LaTeX run to settle labels/cross-references.
  - Preserve the measured values exactly: `6729` galaxies, BPT AGN fraction `0.549 ± 0.006` (`3692/6729`), median `log(L_Hα / erg s^-1) = 40.06`, offset `-0.66` dex.
- `09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`
  - Consider softening the title or abstract wording from `validation` to `future validation` or `observational target vector for validation`.
  - Preserve the real-data limits exactly: `15` mass-redshift cells with `n >= 50`, quenched fractions spanning `0.005--0.729`, optical AGN fractions spanning `0.003--0.520`.
- Global writer instruction for all nine files:
  - Do not change the measured numbers, sample sizes, or real-data bounds.
  - Keep every caveat that says the manuscripts are optical baselines/denominators only.
  - No edits are needed for missing figures or undefined citations; the package is already internally consistent there.

**Safety ledger**
- No edits made.
- No public PDF replacement.
- No database, SQL, `/api/pages`, page_versions, wiki publish, trust recompute, or data mutation.
- No deploy/restart.
- No git commit/push/merge/rebase/history rewrite.
- No cron creation/update/removal.
- No billing, cloud, OAuth, API-key, account, credential, token, or cookie access.
- No external manuscript submission.

```

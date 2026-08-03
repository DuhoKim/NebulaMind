# codex_kun_tex_repro cycle 5
Started UTC: 2026-07-10T02:01:36Z
Finished UTC: 2026-07-10T02:05:00Z
Model: gpt-5.4-mini
Provider: codex
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/briefs/cycle_05_codex_kun_tex_repro.md
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
session id: 019f49c2-481c-7963-8753-a48a78d4e6fa
--------
user
Kun/Codex read-only TeX/reproducibility audit: inspect candidate TeX and strict compile audit; report exact blockers; no edits.

Output marker: LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_05

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

The user reports that the current public PDFs are still not publishable and that some show LaTeX errors. Your job is to find exact high-value blockers and feed the candidate-copy writer. Focus first on strict LaTeX/log issues, then AAS publishability.

Required output sections:
1. LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_05 status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Strict LaTeX blockers: fatal errors, undefined refs/citations, missing figures, overfull/underfull box locations, package/layout problems.
4. Publishability blockers: overclaiming, weak abstract/conclusion, insufficient caveats, source-role/citation problems, poor figure/table captions, reader flow.
5. Exact feed for the writer: concrete TeX-level edits, by file/section/line when possible. Preserve all real measured values and real-data limits.
6. Safety ledger: no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR
Cycle: 5
Candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers
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
Candidate: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers
Cycle: 5

## Strict LaTeX audit

- m1_rp1_sdss_agn_sfr_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m1_rp2_environment_quenching_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m1_rp3_maintenance_heating_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m2_p1_outflow_escape_recycling_integrated.tex: build_ok=True clean_ok=False rc=0 layout_warnings=1 undefined=0 fatal={}
  - L579: Underfull \hbox (badness 1859) in paragraph at lines 57--58
- m2_p2_radio_jet_environment_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m2_p3_feedback_transition_mass_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m3_p1_multiphase_census_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m3_p2_gas_depletion_efficiency_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}
- m3_p3_simulation_validation_integrated.tex: build_ok=True clean_ok=True rc=0 layout_warnings=0 undefined=0 fatal={}

## Manuscript summaries

### 01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
Title: Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Pilot
Abstract: We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log(\mathrm{sSFR}/\mathrm{yr}^{-1})=-1.309$ dex; at S/N$\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
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
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\pm$ 0.001) and records their median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
Conclusion: BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074 $\pm$ 0.001), and their median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1})$ is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
Title: Environment Proxy for Optical AGN in Massive SDSS Hosts
Abstract: We build an optical denominator for radio-jet environment follow-up using a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. In massive hosts, the high-density quartile has optical AGN fraction 0.509 $\pm$ 0.012 and the low-density quartile has 0.367 $\pm$ 0.012, defining an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
Conclusion: Among massive hosts, the optical AGN fraction is 0.509 $\pm$ 0.012 in the high-density quartile and 0.367 $\pm$ 0.012 in the low-density quartile, with a bootstrap difference of [0.112, 0.170]. This establishes an environment-stratified optical denominator for radio-jet coupling studies, not a direct coupling measurement. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
Title: SDSS Mass Transition in Quenching and Optical AGN Incidence
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to identify the stellar-mass regime where quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, and the first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail at $\log(M_\star/M_\odot) > 11.0$, where the optical AGN fraction peaks at 0.520 ($n=2{,}098$ of $4{,}033$).
Conclusion: In summary, the high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$, is the first stellar-mass bin where the quenched fraction exceeds 0.5. Within that same bin, the optical AGN fraction peaks at 0.520 ($n=2{,}098$ of $4{,}033$). These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

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
I’m checking the candidate TeX package and any build artifacts around the strict compile warnings so I can separate true LaTeX blockers from publishability issues. Next I’ll inspect the relevant `.tex` files and any logs in the run root to ground the report in exact file/line evidence.
exec
/bin/zsh -c "pwd && rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers | sed -n '1,120p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/SOURCE_COPY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_TEX_LINT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_TEX_LINT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf

codex
I’ve confirmed the candidate package is self-contained and includes PDFs plus audit manifests. I’m now reading the strict-audit files and the affected TeX sources to extract line-accurate blockers, then I’ll map that to writer-ready fixes.
exec
/bin/zsh -c "sed -n '1,220p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# Strict LaTeX audit before cycle 5

all_build_ok: True
all_clean_ok: False
layout_warning_count: 1
undefined_count: 0

## m1_rp1_sdss_agn_sfr_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=240136
- fatal_hits={}
- warning_hits={}

## m1_rp2_environment_quenching_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=93470
- fatal_hits={}
- warning_hits={}

## m1_rp3_maintenance_heating_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=91446
- fatal_hits={}
- warning_hits={}

## m2_p1_outflow_escape_recycling_integrated.tex
- build_ok=True clean_ok=False rc=0 bytes=326249
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 1}
- log lines:
  - L579: Underfull \hbox (badness 1859) in paragraph at lines 57--58

## m2_p2_radio_jet_environment_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=92759
- fatal_hits={}
- warning_hits={}

## m2_p3_feedback_transition_mass_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=98559
- fatal_hits={}
- warning_hits={}

## m3_p1_multiphase_census_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=92221
- fatal_hits={}
- warning_hits={}

## m3_p2_gas_depletion_efficiency_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=223075
- fatal_hits={}
- warning_hits={}

## m3_p3_simulation_validation_integrated.tex
- build_ok=True clean_ok=True rc=0 bytes=98741
- fatal_hits={}
- warning_hits={}

exec
/bin/zsh -c 'cat /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.json' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "all_build_ok": true,
  "all_clean_ok": false,
  "candidate": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers",
  "created_utc": "2026-07-10T02:01:36Z",
  "cycle": 5,
  "label": "before",
  "results": [
    {
      "build_ok": true,
      "clean_ok": true,
      "command": [
        "tectonic",
        "--keep-logs",
        "--print",
        "--reruns",
        "1",
        "--color",
        "never",
        "m1_rp1_sdss_agn_sfr_integrated.tex"
      ],
      "fatal_hits": {},
      "header": "%PDF",
      "interesting_log_lines": [],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
      "pdf_bytes": 240136,
      "pdf_exists": true,
      "pdf_sha256": "5ef358d253a3284e9e3bc2b7f5c75cb89d4e00799a755bfc01382e9b0f5f0edf",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
      "transcript_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.log",
      "undefined_count": 0,
      "warning_hits": {}
    },
    {
      "build_ok": true,
      "clean_ok": true,
      "command": [
        "tectonic",
        "--keep-logs",
        "--print",
        "--reruns",
        "1",
        "--color",
        "never",
        "m1_rp2_environment_quenching_integrated.tex"
      ],
      "fatal_hits": {},
      "header": "%PDF",
      "interesting_log_lines": [],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
      "pdf_bytes": 93470,
      "pdf_exists": true,
      "pdf_sha256": "0462b175beab73ae7612914285c932c90dfb12d9e2ef9a90860589517282704e",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
      "transcript_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.log",
      "undefined_count": 0,
      "warning_hits": {}
    },
    {
      "build_ok": true,
      "clean_ok": true,
      "command": [
        "tectonic",
        "--keep-logs",
        "--print",
        "--reruns",
        "1",
        "--color",
        "never",
        "m1_rp3_maintenance_heating_integrated.tex"
      ],
      "fatal_hits": {},
      "header": "%PDF",
      "interesting_log_lines": [],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
      "pdf_bytes": 91446,
      "pdf_exists": true,
      "pdf_sha256": "7a5437aa8ec9f1fd3a119edf457c423552c59624f45009fe0d5a7aa624ab8ad2",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
      "transcript_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.log",
      "undefined_count": 0,
      "warning_hits": {}
    },
    {
      "build_ok": true,
      "clean_ok": false,
      "command": [
        "tectonic",
        "--keep-logs",
        "--print",
        "--reruns",
        "1",
        "--color",
        "never",
        "m2_p1_outflow_escape_recycling_integrated.tex"
      ],
      "fatal_hits": {},
      "header": "%PDF",
      "interesting_log_lines": [
        "L579: Underfull \\hbox (badness 1859) in paragraph at lines 57--58"
      ],
      "label": "before",
      "layout_warning_count": 1,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
      "pdf_bytes": 326249,
      "pdf_exists": true,
      "pdf_sha256": "af46907cd041d040cc84df98848912461d7165471df2b399fe933ddc13af9c4f",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
      "transcript_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.log",
      "undefined_count": 0,
      "warning_hits": {
        "Underfull \\hbox": 1
      }
    },
    {
      "build_ok": true,
      "clean_ok": true,
      "command": [
        "tectonic",
        "--keep-logs",
        "--print",
        "--reruns",
        "1",
        "--color",
        "never",
        "m2_p2_radio_jet_environment_integrated.tex"
      ],
      "fatal_hits": {},
      "header": "%PDF",
      "interesting_log_lines": [],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf",
      "pdf_bytes": 92759,
      "pdf_exists": true,
      "pdf_sha256": "d2368ac54052f345cffd1f5cd7b17410154c4a0c4b2f7e01ccf31185b9618095",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex",
      "transcript_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.log",
      "undefined_count": 0,
      "warning_hits": {}
    },
    {
      "build_ok": true,
      "clean_ok": true,
      "command": [
        "tectonic",
        "--keep-logs",
        "--print",
        "--reruns",
        "1",
        "--color",
        "never",
        "m2_p3_feedback_transition_mass_integrated.tex"
      ],
      "fatal_hits": {},
      "header": "%PDF",
      "interesting_log_lines": [],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf",
      "pdf_bytes": 98559,
      "pdf_exists": true,
      "pdf_sha256": "e92a0bfa0c27173c2c7eeb4bb08faf6b5394e1def9c5341f21f20102443f8005",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex",
      "transcript_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.log",
      "undefined_count": 0,
      "warning_hits": {}
    },
    {
      "build_ok": true,
      "clean_ok": true,
      "command": [
        "tectonic",
        "--keep-logs",
        "--print",
        "--reruns",
        "1",
        "--color",
        "never",
        "m3_p1_multiphase_census_integrated.tex"
      ],
      "fatal_hits": {},
      "header": "%PDF",
      "interesting_log_lines": [],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf",
      "pdf_bytes": 92221,
      "pdf_exists": true,
      "pdf_sha256": "b4fe23a2dbaf1d5e70254bc2b73f88e61c7d1a4d322ac2d9e02607089e5f3a4d",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex",
      "transcript_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.log",
      "undefined_count": 0,
      "warning_hits": {}
    },
    {
      "build_ok": true,
      "clean_ok": true,
      "command": [
        "tectonic",
        "--keep-logs",
        "--print",
        "--reruns",
        "1",
        "--color",
        "never",
        "m3_p2_gas_depletion_efficiency_integrated.tex"
      ],
      "fatal_hits": {},
      "header": "%PDF",
      "interesting_log_lines": [],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf",
      "pdf_bytes": 223075,
      "pdf_exists": true,
      "pdf_sha256": "7e13523d6c2f117284f31e153a8d2f2d5e885be358e038f13a81eb334216c875",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex",
      "transcript_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.log",
      "undefined_count": 0,
      "warning_hits": {}
    },
    {
      "build_ok": true,
      "clean_ok": true,
      "command": [
        "tectonic",
        "--keep-logs",
        "--print",
        "--reruns",
        "1",
        "--color",
        "never",
        "m3_p3_simulation_validation_integrated.tex"
      ],
      "fatal_hits": {},
      "header": "%PDF",
      "interesting_log_lines": [],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf",
      "pdf_bytes": 98741,
      "pdf_exists": true,
      "pdf_sha256": "1950fda9aa3dee083f067511e4088ed408bf9bd99a8ca2048055caf4c46070b4",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex",
      "transcript_log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.log",
      "undefined_count": 0,
      "warning_hits": {}
    }
  ],
  "total_layout_warning_count": 1,
  "total_undefined_count": 0
}
codex
The compile audit is nearly clean: no fatal TeX errors and no unresolved refs/citations. I’m now checking the one layout warning source and the high-risk prose sections, mainly abstracts/conclusions and figure captions, to identify anything that would still block AAS publication even though the PDFs render.
exec
/bin/zsh -c "rg -n \"\\\\begin\\{abstract\\}|\\\\end\\{abstract\\}|\\\\begin\\{acknowledgments\\}|\\\\section\\{|\\\\subsection\\{|\\\\caption\\{|\\\\cite\\{|\\\\label\\{|\\\\ref\\{\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/*/aastex/*.tex" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c "rg -n \"\\\\begin\\{abstract\\}|\\\\end\\{abstract\\}|\\\\begin\\{acknowledgments\\}|\\\\section\\{|\\\\subsection\\{|\\\\caption\\{|\\\\cite\\{|\\\\label\\{|\\\\ref\\{\" /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex | sed -n '1,120p'" in /Users/duhokim/NebulaMind/NebulaMind
 exited 2 in 0ms:
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\begin\{acknowledgments\}|\section\{|\subsection\{|\caption\{|\cite\{|\label\{|\ref\{)
                          ^^
error: unrecognized escape sequence

 exited 2 in 0ms:
rg: regex parse error:
    (?:\begin\{abstract\}|\end\{abstract\}|\begin\{acknowledgments\}|\section\{|\subsection\{|\caption\{|\cite\{|\label\{|\ref\{)
                          ^^
error: unrecognized escape sequence

 succeeded in 0ms:
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS BPT-Selected Optical AGN Denominator for Outflow Escape Tests}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS BPT-Selected Optical AGN Denominator for Outflow Escape Tests}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\pm$ 0.001) and records their median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	An optical line-ratio selection can define a useful target set for future outflow work, but it cannot measure escape or recycling on its own. Here, the SDSS DR17 emission-line parent sample serves as the optical baseline for outflow follow-up rather than a direct outflow-fate measurement. We present the SDSS DR17 emission-line sample as an optical baseline for massive galaxies and restrict the scope to directly measured quantities. Resolved kinematics, halo potentials, and multiphase gas remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note keeps the shared SDSS DR17 parent selection but interprets it as an outflow-escape follow-up denominator rather than a direct outflow measurement. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The capped subset contains 60,000 emission-line galaxies from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	\enddata
    41	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
    42	\end{deluxetable*}
    43	
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
    55	This note quantifies the BPT-selected optical AGN denominator needed for future resolved-kinematics tests of escape versus recycling. The result is an optical baseline rather than a direct escape-velocity measurement. ``BPT-selected optical AGN candidates'' here means the optical AGN subset counted above; it is shorthand for the denominator, not a separate kinematic or energy measurement.
    56	
    57	BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies ($0.074 \pm 0.001$). Their median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1})$ is $-11.53$, compared with $-10.14$ for the full denominator. This optical sample defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate. Figure~\ref{fig:topic} shows the target-selection baseline.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure shows the 4,440-object BPT-selected denominator, the corresponding fraction of $0.074 \pm 0.001$, and the associated median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) = -11.53$ used to define the resolved-kinematics target set.}
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
    77	BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074 $\pm$ 0.001), and their median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1})$ is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.
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
    96	
    97	\end{document}

codex
I’ve got the line-level source for the one compile warning. I’m now pulling section anchors across the nine TeX files so I can point the writer to specific abstract/conclusion/caption locations instead of giving generic prose advice.
exec
/bin/zsh -c "rg -n '\\\\begin\\{abstract\\}|\\\\section\\{|\\\\caption\\{|\\\\begin\\{acknowledgments\\}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
14:\begin{abstract}
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
49:\section{Measurements}\label{sec:measurements}
54:\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
65:\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used in the RP-1 analysis. The figure shows the standard line-ratio classification plane defined by H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ and documents the optical selection and classification boundary.}
72:\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The figure summarizes the matched-pair offset distribution used to estimate the median optical AGN-control difference, which remains selection- and subclass-dependent.}
77:\section{Data Availability}\label{sec:data-avail}
80:\section{Conclusion}\label{sec:conclusion}
83:\begin{acknowledgments}

exec
/bin/zsh -c "rg -n '\\\\begin\\{abstract\\}|\\\\section\\{|\\\\caption\\{|\\\\begin\\{acknowledgments\\}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
14:\begin{abstract}
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
49:\section{Measurements}\label{sec:measurements}
54:\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
63:\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure shows quenched fraction versus the local density proxy, split into equal-count density quartiles. The high-density quartile reaches a quenched fraction of 0.230 $\pm$ 0.003, establishing the baseline for future group-catalog analyses.}
67:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
81:\begin{acknowledgments}

exec
/bin/zsh -c "rg -n '\\\\begin\\{abstract\\}|\\\\section\\{|\\\\caption\\{|\\\\begin\\{acknowledgments\\}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
14:\begin{abstract}
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
49:\section{Measurements}\label{sec:measurements}
54:\section{Optical denominator for maintenance-heating follow-up}\label{sec:topic-result}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for maintenance-heating follow-up. The figure shows the optical AGN fraction in the massive subset and the massive low-sSFR subset, rising from 0.430 to 0.607 and illustrating the denominator shift used for future X-ray/radio studies.}
67:\section{Interpretation and missing observables}\label{sec:missing}
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
79:\begin{acknowledgments}

exec
/bin/zsh -c "rg -n '\\\\begin\\{abstract\\}|\\\\section\\{|\\\\caption\\{|\\\\begin\\{acknowledgments\\}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
14:\begin{abstract}
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
49:\section{Measurements}\label{sec:measurements}
54:\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure shows the 4,440-object BPT-selected denominator, the corresponding fraction of $0.074 \pm 0.001$, and the associated median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) = -11.53$ used to define the resolved-kinematics target set.}
67:\section{Interpretation and missing observables}\label{sec:missing}
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
79:\begin{acknowledgments}

exec
/bin/zsh -c "rg -n '\\\\begin\\{abstract\\}|\\\\section\\{|\\\\caption\\{|\\\\begin\\{acknowledgments\\}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c "rg -n '\\\\begin\\{abstract\\}|\\\\section\\{|\\\\caption\\{|\\\\begin\\{acknowledgments\\}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c "rg -n '\\\\begin\\{abstract\\}|\\\\section\\{|\\\\caption\\{|\\\\begin\\{acknowledgments\\}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
14:\begin{abstract}
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
49:\section{Measurements}\label{sec:measurements}
54:\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure shows optical AGN fraction versus the local density proxy in massive hosts, with the high-density quartile rising to 0.509 $\pm$ 0.012 and the low-density quartile at 0.367 $\pm$ 0.012.}
67:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
81:\begin{acknowledgments}

 succeeded in 0ms:
14:\begin{abstract}
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
49:\section{Measurements}\label{sec:measurements}
54:\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows quenched fraction and optical AGN fraction across the five stellar-mass bins spanning 8.0--9.5 through 11.0--12.5. The high-mass tail ($\log(M_\star/M_\odot) > 11.0$) is the first bin where quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520 ($n=2{,}098$ of $4{,}033$).}
67:\section{Interpretation and missing observables}\label{sec:missing}
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
79:\begin{acknowledgments}

 succeeded in 0ms:
14:\begin{abstract}
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
49:\section{Measurements}\label{sec:measurements}
54:\section{Optical census of multiphase target denominators}\label{sec:topic-result}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure shows how the BPT AGN, high-[N II]/H$\alpha$, high-[O III]/H$\beta$, low-sSFR+emission, and red+emission definitions span the same 60,000-galaxy denominator, with prevalence ranging from 0.136 to 0.418.}
67:\section{Interpretation and missing observables}\label{sec:missing}
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
79:\begin{acknowledgments}

exec
/bin/zsh -c "rg -n '\\\\begin\\{abstract\\}|\\\\section\\{|\\\\caption\\{|\\\\begin\\{acknowledgments\\}' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
14:\begin{abstract}
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
52:\section{Measurements}\label{sec:measurements}
57:\section{Optical denominator for gas-fraction versus efficiency tests}\label{sec:topic-result}
66:\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure shows the 6,729-galaxy massive transition/quenched denominator, the optical BPT AGN fraction of $0.549 \pm 0.006$, and the median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$. This is the target set for future CO gas-fraction versus depletion-time follow-up.}
70:\section{Interpretation and missing observables}\label{sec:missing}
76:\section{Data Availability}\label{sec:data-avail}
79:\section{Conclusion}\label{sec:conclusion}
82:\begin{acknowledgments}

codex
I’ve got the key anchors for all nine manuscripts now. Next I’m checking each one for concrete publication risks that are not TeX-fatal but still matter for AAS acceptance: overclaiming in abstracts/conclusions, missing caveat language, and any figure-caption mismatch with the actual claim being made.
exec
/bin/zsh -c "sed -n '1,140p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS Optical AGN/sSFR Matched-Control Pilot}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: A Selection-Aware Matched-Control Pilot}
\author{NebulaMind Research Autopilot}
\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
\correspondingauthor{NebulaMind Research Autopilot}
\email{autopilot@nebulamind.ai}

\begin{abstract}
We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log(\mathrm{sSFR}/\mathrm{yr}^{-1})=-1.309$ dex; at S/N$\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}

\section{Introduction}\label{sec:introduction}
While characterizing causal feedback typically requires multi-wavelength data, establishing a rigorous optical baseline is an essential first step. Here, the SDSS DR17 emission-line parent sample serves as the optical baseline for downstream comparison rather than a measurement of a physical process by itself. We present a selection-aware matched-control pilot analyzing catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. Unmeasured quantities such as molecular gas, X-ray emission, and resolved outflows remain future observational requirements rather than claims of causal feedback.


\section{Data and Sample Selection}\label{sec:shared-selection}
This note uses a capped subset of 60,000 SDSS DR17 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR and sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects; the BPT partition is shown in Figure~\ref{fig:bpt}.

The preferred estimator matches every broad optical AGN host to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. This is an association design; controls are not matched in morphology, halo mass, gas mass, aperture scale, AGN luminosity, or duty-cycle phase.

Our comparison of broad BPT optical AGN hosts versus star-forming controls at S/N$\geq 3$ matches $N=8,146$ pairs, measuring a median specific star formation rate offset of $\Delta\log(\mathrm{sSFR}/\mathrm{yr}^{-1})=-1.309$ dex with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Applying a moderate mass-redshift caliper of $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$ retains $N=7,867$ pairs (96.6\% target coverage) and yields a median offset of $-1.318$ dex. A deterministic matching run without replacement yields $N=7,419$ matched pairs and a median offset of $-1.446$ dex, though with poorer stellar-mass balance. Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to $-0.744$ dex, and a narrower [N II] Seyfert-like proxy yields $N=2,114$ pairs and a median offset of $-0.763$ dex; these selection sensitivities are summarized in Figure~\ref{fig:offsets}.


\begin{figure*}
\centering
\includegraphics[width=0.73\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used in the RP-1 analysis. The figure shows the standard line-ratio classification plane defined by H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ and documents the optical selection and classification boundary.}
\label{fig:bpt}
\end{figure*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The figure summarizes the matched-pair offset distribution used to estimate the median optical AGN-control difference, which remains selection- and subclass-dependent.}
\label{fig:offsets}
\end{figure*}


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
In the capped SDSS DR17 emission-line subset, broad BPT optical AGN hosts show a median sSFR offset of $-1.309$ dex relative to mass--redshift matched controls, with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Although the offset amplitude is highly dependent on the emission-line selection function (decreasing to $-0.744$ dex at S/N$\geq 10$), the interval remains securely negative. These measurements establish a robust optical association baseline, which will require future molecular gas or direct outflow kinematics follow-up to isolate any causal AGN quenching mechanisms.

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

\end{thebibliography}

\end{document}

exec
/bin/zsh -c "sed -n '1,130p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Optical-AGN Denominator for Maintenance-Heating Follow-Up}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Optical-AGN Denominator for Maintenance-Heating Follow-Up}
\author{NebulaMind Research Autopilot}
\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
\correspondingauthor{NebulaMind Research Autopilot}
\email{autopilot@nebulamind.ai}

\begin{abstract}
We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 (3,997/9,298) in the massive subset and 0.607 (3,459/5,695) among massive low-sSFR objects, providing a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}

\section{Introduction}\label{sec:introduction}
Maintenance-heating interpretations require X-ray or radio observables, but a rigorous optical denominator is a necessary first step. Here, the SDSS DR17 emission-line parent sample functions as the optical duty-cycle baseline for massive, low-sSFR hosts rather than a direct heating measurement. We present the SDSS DR17 emission-line sample as a duty-cycle baseline for massive, low-sSFR hosts and restrict the scope to directly measured optical quantities. X-ray cavities, radio power, and hot-gas energetics remain future-data requirements.


\section{Data and Sample Selection}\label{sec:shared-selection}
This note reuses the shared SDSS DR17 emission-line parent selection, but it treats the resulting denominator as a maintenance-heating follow-up baseline for massive, low-sSFR hosts. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The capped subset contains 60,000 galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{Optical denominator for maintenance-heating follow-up}\label{sec:topic-result}
Among massive, low-sSFR SDSS emission-line galaxies, we quantify the optical AGN fraction available as a denominator for X-ray and radio maintenance-heating follow-up. The result is an optical baseline rather than a calorimetric measurement.

The massive galaxy subset ($\log M_\star \geq 10.8$) contains 9,298 emission-line galaxies, of which 5,695 are classified as low-sSFR based on the specific star formation rate threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$ applied in this analysis. The optical BPT AGN fraction is measured as 0.430 (3,997/9,298) in the total massive subset, rising to 0.607 (3,459/5,695) when restricting the sample to massive low-sSFR objects. This empirical duty-cycle baseline is intended for future X-ray or radio maintenance-heating follow-up and is not a heating measurement. Figure~\ref{fig:topic} shows the corresponding optical denominator.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for maintenance-heating follow-up. The figure shows the optical AGN fraction in the massive subset and the massive low-sSFR subset, rising from 0.430 to 0.607 and illustrating the denominator shift used for future X-ray/radio studies.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires X-ray cavity and cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.

Radio-mode and hot-atmosphere studies define the future calorimetric observables: jet power, cavities, cooling luminosity, and group gas. Those observables are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
The massive subset contains 9,298 emission-line galaxies, with 5,695 classified as low-sSFR by the pilot threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$. The BPT AGN fraction rises from 0.430 (3,997/9,298) in the massive subset to 0.607 (3,459/5,695) in the massive low-sSFR subset, defining an optical duty-cycle denominator for maintenance-heating follow-up rather than a direct heating result.

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
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New J. Phys., 14, 055023
\end{thebibliography}

\end{document}

exec
/bin/zsh -c "sed -n '1,130p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
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
SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
We examine whether a nearest-neighbor density proxy adds quenched-fraction information beyond stellar mass in the SDSS emission-line sample. The result is an optical baseline rather than a full physical-feedback test.

Within the 60,000-galaxy denominator, the high-density quartile has a quenched fraction of $0.230 \pm 0.003$ ($n=3{,}456$ of $15{,}000$). The low-density quartile is lower at $0.181 \pm 0.003$ ($n=2{,}710$ of $15{,}000$). The bootstrap high-minus-low difference interval is $[0.041, 0.059]$, safely excluding zero. After controlling for logarithmic stellar mass and redshift, a linear probability model yields a high-density coefficient of $0.032 \pm 0.004$. That result indicates the density proxy remains correlated with quenching independently of those host-galaxy properties. Figure~\ref{fig:topic} summarizes the proxy split used in this baseline.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure shows quenched fraction versus the local density proxy, split into equal-count density quartiles. The high-density quartile reaches a quenched fraction of 0.230 $\pm$ 0.003, establishing the baseline for future group-catalog analyses.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only baseline does not include group catalogues, robust central/satellite labels, halo masses, morphology, or multi-redshift selection functions. Those data are required before the density proxy can be interpreted as a physical environmental-quenching measurement.

Because the density proxy is projected on the sky, fiber-collision and redshift-space incompleteness can dilute nearest-neighbor estimates; future group-catalog work should correct those effects explicitly.

Mass and environment are separable axes in low-redshift galaxy evolution, and prior studies have developed that framework \citep{peng2010,baldry2006,wetzel2013,goubert2024}. A complete environmental-quenching analysis therefore requires group and halo information beyond this nearest-neighbor proxy, together with central/satellite labels.


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
/bin/zsh -c "sed -n '1,140p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{SDSS BPT-Selected Optical AGN Denominator for Outflow Escape Tests}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{SDSS BPT-Selected Optical AGN Denominator for Outflow Escape Tests}
\author{NebulaMind Research Autopilot}
\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
\correspondingauthor{NebulaMind Research Autopilot}
\email{autopilot@nebulamind.ai}

\begin{abstract}
We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\pm$ 0.001) and records their median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}

\section{Introduction}\label{sec:introduction}
An optical line-ratio selection can define a useful target set for future outflow work, but it cannot measure escape or recycling on its own. Here, the SDSS DR17 emission-line parent sample serves as the optical baseline for outflow follow-up rather than a direct outflow-fate measurement. We present the SDSS DR17 emission-line sample as an optical baseline for massive galaxies and restrict the scope to directly measured quantities. Resolved kinematics, halo potentials, and multiphase gas remain future-data requirements.


\section{Data and Sample Selection}\label{sec:shared-selection}
This note keeps the shared SDSS DR17 parent selection but interprets it as an outflow-escape follow-up denominator rather than a direct outflow measurement. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The capped subset contains 60,000 emission-line galaxies from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
This note quantifies the BPT-selected optical AGN denominator needed for future resolved-kinematics tests of escape versus recycling. The result is an optical baseline rather than a direct escape-velocity measurement. ``BPT-selected optical AGN candidates'' here means the optical AGN subset counted above; it is shorthand for the denominator, not a separate kinematic or energy measurement.

BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies ($0.074 \pm 0.001$). Their median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1})$ is $-11.53$, compared with $-10.14$ for the full denominator. This optical sample defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate. Figure~\ref{fig:topic} shows the target-selection baseline.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure shows the 4,440-object BPT-selected denominator, the corresponding fraction of $0.074 \pm 0.001$, and the associated median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) = -11.53$ used to define the resolved-kinematics target set.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires resolved outflow velocities, halo potentials, molecular/ionized/neutral gas phases, and CGM recycling tracers.

Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005, cicone2014, fiore2017, carniani2017, fabian2012}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074 $\pm$ 0.001), and their median $\log(\mathrm{sSFR}/\mathrm{yr}^{-1})$ is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.

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
\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\end{thebibliography}

\end{document}

exec
/bin/zsh -c "sed -n '1,140p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c "sed -n '1,140p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Common-Denominator Optical Tracer Census in SDSS}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Common-Denominator Optical Tracer Census in SDSS}
\author{NebulaMind Research Autopilot}
\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
\correspondingauthor{NebulaMind Research Autopilot}
\email{autopilot@nebulamind.ai}

\begin{abstract}
We build a common optical denominator for a multiphase outflow census from a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, from 0.136 for BPT AGN to 0.418 for red+emission, so this note focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}

\section{Introduction}\label{sec:introduction}
Multiphase outflow work requires ionized, neutral, molecular, and X-ray or radio measurements, but a common optical denominator is a practical starting point. Here, the SDSS DR17 emission-line parent sample functions as the shared optical denominator for later multiphase follow-up rather than a direct multiphase measurement. We present the SDSS DR17 emission-line sample as that baseline and restrict the manuscript to directly measured optical quantities. The missing multiphase observables remain future-data requirements.


\section{Data and Sample Selection}\label{sec:shared-selection}
This note reuses the shared SDSS DR17 parent selection, but it interprets the result as a common denominator for a multiphase tracer census. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{Optical census of multiphase target denominators}\label{sec:topic-result}
We examine how simple optical tracer definitions change the inferred AGN and feedback-candidate prevalence within one common SDSS denominator. The result is an optical baseline for later multiphase follow-up rather than a direct multiphase measurement.

Within the same 60,000-galaxy denominator, the BPT AGN and red+emission definitions produce prevalence from 0.136 for BPT AGN to 0.418 for red+emission, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases. Figure~\ref{fig:topic} summarizes the tracer spread.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure shows how the BPT AGN, high-[N II]/H$\alpha$, high-[O III]/H$\beta$, low-sSFR+emission, and red+emission definitions span the same 60,000-galaxy denominator, with prevalence ranging from 0.136 to 0.418.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model.

A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005, rupke2018, cicone2014, fiore2017, feruglio2015, woo2016, bae2018}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
Within the 60,000-galaxy denominator, the BPT AGN and red+emission definitions change prevalence from 0.136 for BPT AGN to 0.418 for red+emission, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases.

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
\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
\end{thebibliography}

\end{document}

 succeeded in 0ms:
\documentclass[twocolumn]{aastex631}
\usepackage{amsmath}
\usepackage{booktabs}
\shorttitle{Environment Proxy for Optical AGN in Massive SDSS Hosts}
\shortauthors{NebulaMind Research Autopilot}
\begin{document}

\title{Environment Proxy for Optical AGN in Massive SDSS Hosts}
\author{NebulaMind Research Autopilot}
\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
\correspondingauthor{NebulaMind Research Autopilot}
\email{autopilot@nebulamind.ai}

\begin{abstract}
We build an optical denominator for radio-jet environment follow-up using a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. In massive hosts, the high-density quartile has optical AGN fraction 0.509 $\pm$ 0.012 and the low-density quartile has 0.367 $\pm$ 0.012, defining an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
\end{abstract}

\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
\software{Astropy, SciPy, NumPy, Matplotlib, pandas}

\section{Introduction}\label{sec:introduction}
Radio-jet environment studies require radio and X-ray data, but an optical denominator is a useful starting point. Here, the SDSS DR17 emission-line parent sample provides the environment-stratified optical baseline for massive hosts rather than a direct jet-coupling measurement. We present the SDSS DR17 emission-line sample as an environment-stratified baseline for massive hosts and restrict the analysis to directly measured optical quantities. Jet power, coupling efficiency, and hot-gas structure remain future-data requirements.


\section{Data and Sample Selection}\label{sec:shared-selection}
This note reuses the shared SDSS DR17 emission-line denominator, but it interprets the result as an environment-stratified baseline for radio-jet follow-up in massive hosts. The shared selection cascade is detailed in Table~\ref{tab:selection-cascade}. The capped subset contains 60,000 galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
\startdata
SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
We examine whether a local-density proxy modulates the optical AGN fraction in massive SDSS hosts. The result is an environment-stratified optical baseline for future radio and X-ray jet-coupling work.

Among massive hosts, the high-density quartile has optical AGN fraction $0.509 \pm 0.012$, while the low-density quartile has $0.367 \pm 0.012$. The bootstrap high-minus-low interval is $[0.112,0.170]$. This is an optical/environment denominator for radio-jet coupling work and does not measure jet power or coupling efficiency. Figure~\ref{fig:topic} shows the environment split.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure shows optical AGN fraction versus the local density proxy in massive hosts, with the high-density quartile rising to 0.509 $\pm$ 0.012 and the low-density quartile at 0.367 $\pm$ 0.012.}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.

Because the density proxy is projected on the sky, fiber-collision and redshift-space incompleteness can dilute nearest-neighbor estimates; future radio-jet follow-up should correct those effects explicitly.

The radio, X-ray, and group literature motivates environment-stratified follow-up. The present result is only an optical BPT-AGN fraction versus an internal density proxy rather than a direct jet-coupling measurement \citep{best2005,santoro2020,mcnamara2007,eckert2024}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
Among massive hosts, the optical AGN fraction is 0.509 $\pm$ 0.012 in the high-density quartile and 0.367 $\pm$ 0.012 in the low-density quartile, with a bootstrap difference of [0.112, 0.170]. This establishes an environment-stratified optical denominator for radio-jet coupling studies, not a direct coupling measurement.

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
\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
\end{thebibliography}

\end{document}

exec
/bin/zsh -c "sed -n '1,140p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
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
We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to identify the stellar-mass regime where quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, and the first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail at $\log(M_\star/M_\odot) > 11.0$, where the optical AGN fraction peaks at 0.520 ($n=2{,}098$ of $4{,}033$).
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
SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.


\section{Measurements}\label{sec:measurements}
The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.


\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
We identify the stellar-mass scale at which quenched fraction and optical AGN incidence rise together in the SDSS emission-line sample. The result is an empirical optical transition vector rather than a full physical-feedback test.

The high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$, is the first stellar-mass bin where the quenched fraction exceeds 0.5. In that same bin, the optical AGN fraction reaches a peak of 0.520 ($n=2{,}098$ of $4{,}033$). These combined results define an empirical transition vector; however, gas fractions and baryon deficits are required before assigning the trend to stellar or AGN feedback. Figure~\ref{fig:topic} highlights the transition bin.


\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows quenched fraction and optical AGN fraction across the five stellar-mass bins spanning 8.0--9.5 through 11.0--12.5. The high-mass tail ($\log(M_\star/M_\odot) > 11.0$) is the first bin where quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520 ($n=2{,}098$ of $4{,}033$).}
\label{fig:topic}
\end{figure}

\section{Interpretation and missing observables}\label{sec:missing}
This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.

Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition. Those data are the missing ingredients behind the optical trend \citep{kauffmann2003mass, baldry2004, peng2010, peng2012, dekel2006, bluck2023, piotrowska2022}.


\section{Data Availability}\label{sec:data-avail}
The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.

\section{Conclusion}\label{sec:conclusion}
In summary, the high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$, is the first stellar-mass bin where the quenched fraction exceeds 0.5. Within that same bin, the optical AGN fraction peaks at 0.520 ($n=2{,}098$ of $4{,}033$). These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation.

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

exec
/bin/zsh -c "sed -n '1,150p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
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
SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
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

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

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
\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure shows the 6,729-galaxy massive transition/quenched denominator, the optical BPT AGN fraction of $0.549 \pm 0.006$, and the median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$. This is the target set for future CO gas-fraction versus depletion-time follow-up.}
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
/bin/zsh -c "sed -n '1,150p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex" in /Users/duhokim/NebulaMind/NebulaMind
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
SpecObj GALAXY, $0.02 < z < 0.12$ & 501,060 & -- & 1.000 \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
plus galSpecLine join & 416,554 & -- & 0.831 \\
four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies.}
\end{deluxetable*}

The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-11$ parent bin but 94.9\% of the $-10<\log(\mathrm{sSFR}/\mathrm{yr}^{-1})<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.

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
\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure maps quenched fraction, optical AGN fraction, and median $u-r$ color across 15 mass-redshift cells for simulation forward modelling, spanning $\log(M_\star/M_\odot)$ bins 8.0--9.5 through 11.0--12.5 and redshift bins 0.02--0.05 through 0.08--0.12. Across those cells, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520.}
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
I’ve narrowed the likely publishability issues to claim-strength rather than TeX syntax. I’m pulling exact line numbers for the few places where the prose still sounds too strong for an AAS denominator paper so the writer can patch those directly.
exec
/bin/zsh -c "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex | sed -n '50,95p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
    55	We examine whether a nearest-neighbor density proxy adds quenched-fraction information beyond stellar mass in the SDSS emission-line sample. The result is an optical baseline rather than a full physical-feedback test.
    56	
    57	Within the 60,000-galaxy denominator, the high-density quartile has a quenched fraction of $0.230 \pm 0.003$ ($n=3{,}456$ of $15{,}000$). The low-density quartile is lower at $0.181 \pm 0.003$ ($n=2{,}710$ of $15{,}000$). The bootstrap high-minus-low difference interval is $[0.041, 0.059]$, safely excluding zero. After controlling for logarithmic stellar mass and redshift, a linear probability model yields a high-density coefficient of $0.032 \pm 0.004$. That result indicates the density proxy remains correlated with quenching independently of those host-galaxy properties. Figure~\ref{fig:topic} summarizes the proxy split used in this baseline.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure shows quenched fraction versus the local density proxy, split into equal-count density quartiles. The high-density quartile reaches a quenched fraction of 0.230 $\pm$ 0.003, establishing the baseline for future group-catalog analyses.}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only baseline does not include group catalogues, robust central/satellite labels, halo masses, morphology, or multi-redshift selection functions. Those data are required before the density proxy can be interpreted as a physical environmental-quenching measurement.
    69	
    70	Because the density proxy is projected on the sky, fiber-collision and redshift-space incompleteness can dilute nearest-neighbor estimates; future group-catalog work should correct those effects explicitly.
    71	
    72	Mass and environment are separable axes in low-redshift galaxy evolution, and prior studies have developed that framework \citep{peng2010,baldry2006,wetzel2013,goubert2024}. A complete environmental-quenching analysis therefore requires group and halo information beyond this nearest-neighbor proxy, together with central/satellite labels.
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

exec
/bin/zsh -c "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex | sed -n '50,95p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
    55	We identify the stellar-mass scale at which quenched fraction and optical AGN incidence rise together in the SDSS emission-line sample. The result is an empirical optical transition vector rather than a full physical-feedback test.
    56	
    57	The high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$, is the first stellar-mass bin where the quenched fraction exceeds 0.5. In that same bin, the optical AGN fraction reaches a peak of 0.520 ($n=2{,}098$ of $4{,}033$). These combined results define an empirical transition vector; however, gas fractions and baryon deficits are required before assigning the trend to stellar or AGN feedback. Figure~\ref{fig:topic} highlights the transition bin.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows quenched fraction and optical AGN fraction across the five stellar-mass bins spanning 8.0--9.5 through 11.0--12.5. The high-mass tail ($\log(M_\star/M_\odot) > 11.0$) is the first bin where quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520 ($n=2{,}098$ of $4{,}033$).}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
    69	
    70	Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition. Those data are the missing ingredients behind the optical trend \citep{kauffmann2003mass, baldry2004, peng2010, peng2012, dekel2006, bluck2023, piotrowska2022}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	In summary, the high-mass tail, defined here as $\log(M_\star/M_\odot) > 11.0$, is the first stellar-mass bin where the quenched fraction exceeds 0.5. Within that same bin, the optical AGN fraction peaks at 0.520 ($n=2{,}098$ of $4{,}033$). These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation.
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

exec
/bin/zsh -c "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex | sed -n '50,95p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
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
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure shows how the BPT AGN, high-[N II]/H$\alpha$, high-[O III]/H$\beta$, low-sSFR+emission, and red+emission definitions span the same 60,000-galaxy denominator, with prevalence ranging from 0.136 to 0.418.}
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

exec
/bin/zsh -c "nl -ba /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex | sed -n '55,95p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
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
    66	\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure shows the 6,729-galaxy massive transition/quenched denominator, the optical BPT AGN fraction of $0.549 \pm 0.006$, and the median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$. This is the target set for future CO gas-fraction versus depletion-time follow-up.}
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

codex
**LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_05** status: **ISSUES_FOUND**

**Files/paths inspected**
- Audit manifests:
  - [CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.md)
  - [CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.json)
- TeX sources inspected:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)

**Strict LaTeX blockers**
- No fatal TeX errors.
- No undefined refs/citations in the strict audit.
- No missing figures in the inspected package.
- One layout warning remains:
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L57) has `Underfull \hbox (badness 1859)` at log line 579, tied to paragraph lines 57-58.
- No overfull boxes or package/layout failures were reported in the strict audit.

**Publishability blockers**
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L57) overstates inference in the sentence “the density proxy remains correlated with quenching independently of those host-galaxy properties.” That reads causal/independence-like; for AAS publishability it should be softened to an adjusted association statement.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex#L55) uses “feedback-candidate prevalence” in an optical-selection note. That phrase is easy to misread as a physical classification; it should be renamed to “optical-selection prevalence” or equivalent.
- The rest of the manuscripts are already sufficiently caveated for denominator-style notes. Their main risk is consistency and tone, not a hard publishability blocker.

**Exact feed for the writer**
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L57-L64)
  - Reflow the paragraph around lines 57-58 to eliminate the underfull box.
  - Preserve the numbers exactly: `4,440`, `60,000`, `0.074 \pm 0.001`, and `-11.53`.
  - Best fix: split the long paragraph into two shorter sentences before “Figure~\ref{fig:topic} shows the target-selection baseline.”
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L57-L79)
  - Replace “That result indicates the density proxy remains correlated with quenching independently of those host-galaxy properties” with “That result indicates the density proxy remains associated with quenching after adjustment for those host-galaxy properties.”
  - Keep the measured values unchanged: `0.230 \pm 0.003`, `0.181 \pm 0.003`, `[0.041, 0.059]`, and `0.032 \pm 0.004`.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex#L54-L77)
  - Replace “feedback-candidate prevalence” with “optical-selection prevalence” in abstract/body/caption language.
  - Keep the prevalence values unchanged: `0.136`, `0.418`, and the factor `3.1`.
- No numerical values need revision anywhere else in this cycle; the measured values already trace to real local artifacts.

**Safety ledger**
- No edits.
- No public or live PDF replacement.
- No database, SQL, `/api/pages`, page version, wiki, or trust recompute actions.
- No deploy, restart, git commit, push, merge, rebase, or history rewrite.
- No cron changes.
- No billing, cloud, OAuth, API-key, account, cookie, or credential access.
- No external manuscript submission.
tokens used
71,470
**LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_05** status: **ISSUES_FOUND**

**Files/paths inspected**
- Audit manifests:
  - [CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.md)
  - [CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/CYCLE_05_BEFORE_STRICT_LATEX_AUDIT.json)
- TeX sources inspected:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)

**Strict LaTeX blockers**
- No fatal TeX errors.
- No undefined refs/citations in the strict audit.
- No missing figures in the inspected package.
- One layout warning remains:
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L57) has `Underfull \hbox (badness 1859)` at log line 579, tied to paragraph lines 57-58.
- No overfull boxes or package/layout failures were reported in the strict audit.

**Publishability blockers**
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L57) overstates inference in the sentence “the density proxy remains correlated with quenching independently of those host-galaxy properties.” That reads causal/independence-like; for AAS publishability it should be softened to an adjusted association statement.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex#L55) uses “feedback-candidate prevalence” in an optical-selection note. That phrase is easy to misread as a physical classification; it should be renamed to “optical-selection prevalence” or equivalent.
- The rest of the manuscripts are already sufficiently caveated for denominator-style notes. Their main risk is consistency and tone, not a hard publishability blocker.

**Exact feed for the writer**
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex#L57-L64)
  - Reflow the paragraph around lines 57-58 to eliminate the underfull box.
  - Preserve the numbers exactly: `4,440`, `60,000`, `0.074 \pm 0.001`, and `-11.53`.
  - Best fix: split the long paragraph into two shorter sentences before “Figure~\ref{fig:topic} shows the target-selection baseline.”
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex#L57-L79)
  - Replace “That result indicates the density proxy remains correlated with quenching independently of those host-galaxy properties” with “That result indicates the density proxy remains associated with quenching after adjustment for those host-galaxy properties.”
  - Keep the measured values unchanged: `0.230 \pm 0.003`, `0.181 \pm 0.003`, `[0.041, 0.059]`, and `0.032 \pm 0.004`.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_CONTINUATION_20260710T003716Z_PDF_REPAIR/candidates/cycle_05_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex#L54-L77)
  - Replace “feedback-candidate prevalence” with “optical-selection prevalence” in abstract/body/caption language.
  - Keep the prevalence values unchanged: `0.136`, `0.418`, and the factor `3.1`.
- No numerical values need revision anywhere else in this cycle; the measured values already trace to real local artifacts.

**Safety ledger**
- No edits.
- No public or live PDF replacement.
- No database, SQL, `/api/pages`, page version, wiki, or trust recompute actions.
- No deploy, restart, git commit, push, merge, rebase, or history rewrite.
- No cron changes.
- No billing, cloud, OAuth, API-key, account, cookie, or credential access.
- No external manuscript submission.

```

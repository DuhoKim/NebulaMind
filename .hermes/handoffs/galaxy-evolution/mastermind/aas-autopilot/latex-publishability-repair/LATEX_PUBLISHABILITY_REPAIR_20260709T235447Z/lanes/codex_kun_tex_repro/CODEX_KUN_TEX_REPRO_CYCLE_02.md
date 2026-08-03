# codex_kun_tex_repro cycle 2
Started UTC: 2026-07-10T00:06:13Z
Finished UTC: 2026-07-10T00:10:52Z
Model: gpt-5.4-mini
Provider: codex
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/briefs/cycle_02_codex_kun_tex_repro.md
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
session id: 019f4958-a590-7c60-8cdb-286f3a923550
--------
user
Kun/Codex read-only TeX/reproducibility audit: inspect candidate TeX and strict compile audit; report exact blockers; no edits.

Output marker: LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_02

Work mode: artifact-only, read-only lane. Do not edit files. Do not publish. Do not call or request credentials.

The user reports that the current public PDFs are still not publishable and that some show LaTeX errors. Your job is to find exact high-value blockers and feed the candidate-copy writer. Focus first on strict LaTeX/log issues, then AAS publishability.

Required output sections:
1. LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_02 status: PASS/ISSUES_FOUND/BLOCKED.
2. Files/paths actually inspected or, if not inspectable, paths used from context.
3. Strict LaTeX blockers: fatal errors, undefined refs/citations, missing figures, overfull/underfull box locations, package/layout problems.
4. Publishability blockers: overclaiming, weak abstract/conclusion, insufficient caveats, source-role/citation problems, poor figure/table captions, reader flow.
5. Exact feed for the writer: concrete TeX-level edits, by file/section/line when possible. Preserve all real measured values and real-data limits.
6. Safety ledger: no edits/public/db/deploy/git/cron/billing/OAuth/submission.

Run root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z
Cycle: 2
Candidate package: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers
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
Candidate: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers
Cycle: 2

## Strict LaTeX audit

- m1_rp1_sdss_agn_sfr_integrated.tex: build_ok=False clean_ok=False rc=0 layout_warnings=0 undefined=17 fatal={}
  - L36: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L40: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L44: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L49: Package natbib Warning: Citation `baldwin1981' on page 2 undefined on input lin
  - L53: Package natbib Warning: Citation `kewley2001' on page 2 undefined on input line
  - L57: Package natbib Warning: Citation `kauffmann2003bpt' on page 2 undefined on inpu
- m1_rp2_environment_quenching_integrated.tex: build_ok=False clean_ok=False rc=0 layout_warnings=4 undefined=25 fatal={}
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
- m1_rp3_maintenance_heating_integrated.tex: build_ok=False clean_ok=False rc=0 layout_warnings=4 undefined=27 fatal={}
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
- m2_p1_outflow_escape_recycling_integrated.tex: build_ok=False clean_ok=False rc=0 layout_warnings=0 undefined=27 fatal={}
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
- m2_p2_radio_jet_environment_integrated.tex: build_ok=False clean_ok=False rc=0 layout_warnings=4 undefined=25 fatal={}
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
- m2_p3_feedback_transition_mass_integrated.tex: build_ok=False clean_ok=False rc=0 layout_warnings=8 undefined=31 fatal={}
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
- m3_p1_multiphase_census_integrated.tex: build_ok=False clean_ok=False rc=0 layout_warnings=0 undefined=31 fatal={}
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
- m3_p2_gas_depletion_efficiency_integrated.tex: build_ok=False clean_ok=False rc=0 layout_warnings=0 undefined=25 fatal={}
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
- m3_p3_simulation_validation_integrated.tex: build_ok=False clean_ok=False rc=0 layout_warnings=4 undefined=31 fatal={}
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 

## Manuscript summaries

### 01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
Title: Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot
Abstract: We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log {\rm sSFR}=-1.309$ dex; at S/N$\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
Conclusion: In the capped SDSS DR17 emission-line subset, broad BPT optical AGN hosts show a median sSFR offset of $-1.309$ dex relative to mass--redshift matched controls, with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Although the offset amplitude is highly dependent on the emission-line selection function (decreasing to $-0.744$ dex at S/N$\geq 10$), the interval remains securely negative. These measurements establish a robust optical association baseline, which will require future molecular gas or direct outflow kinematics follow-up to isolate any causal AGN quenching mechanisms. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
Title: SDSS density proxy for environmental quenching
Abstract: We use a representative 60,000-galaxy subset of the SDSS DR17 emission-line catalog to build an optical density-proxy analysis of environmental quenching. A 10th-nearest-neighbor density proxy is compared with quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) after controlling for stellar mass and redshift; using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile. The bootstrap high-minus-low interval is [0.041, 0.059], which excludes zero. This analysis is intentionally limited to the optical denominator and leaves the missing group and halo information for future study.
Conclusion: The SDSS-only proxy shows a high-density quenched fraction of 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile, with a mass- and redshift-adjusted high-density coefficient of $0.032 \pm 0.004$. These values define an optical environmental baseline, but a full quenching interpretation still requires group catalogs, halo masses, and central/satellite labels. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
Title: Optical-AGN denominator for maintenance-heating follow-up
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 (3,997/9,298) in the massive subset and 0.607 (3,459/5,695) among massive low-sSFR objects, providing a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.
Conclusion: The massive subset contains 9,298 emission-line galaxies, with 5,695 classified as low-sSFR by the pilot threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$. The BPT AGN fraction rises from 0.430 (3,997/9,298) in the massive subset to 0.607 (3,459/5,695) in the massive low-sSFR subset, defining an optical duty-cycle denominator for maintenance-heating follow-up rather than a direct heating result. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
Title: SDSS BPT-selected optical AGN denominator for outflow escape tests
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\pm$ 0.001) and records their median $\log {\rm sSFR} = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
Conclusion: BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074 $\pm$ 0.001), and their median $\log {\rm sSFR}$ is -11.53 compared with -10.14 for the full denominator. The optical sample therefore defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
Title: Environment proxy for optical AGN in massive SDSS hosts
Abstract: We build an optical denominator for radio-jet environment follow-up using a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. In massive hosts, the high-density quartile has optical AGN fraction 0.509 $\pm$ 0.012 and the low-density quartile has 0.367 $\pm$ 0.012, defining an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
Conclusion: Among massive hosts, the optical AGN fraction is 0.509 $\pm$ 0.012 in the high-density quartile and 0.367 $\pm$ 0.012 in the low-density quartile, with a bootstrap difference of [0.112, 0.170]. This establishes an environment-stratified optical denominator for radio-jet coupling studies, not a direct coupling measurement. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
Title: SDSS mass transition in quenching and optical AGN incidence
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to identify the stellar-mass regime where quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, and the first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail at $\log(M_\star/M_\odot)>11.0$, where the optical AGN fraction peaks at 0.520 (2,098/4,033). It does not assign the transition to stellar or AGN feedback on its own.
Conclusion: The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot)>11.0$, and the optical AGN fraction peaks at 0.520 (2,098/4,033) in that same bin. These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
Title: Common-denominator optical tracer census in SDSS
Abstract: We build a common optical denominator for a multiphase outflow census from a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, from 0.136 for BPT AGN to 0.418 for red+emission, so this note focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.
Conclusion: Within the 60,000-galaxy denominator, the BPT AGN and red+emission definitions change prevalence from 0.136 for BPT AGN to 0.418 for red+emission, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
Title: Optical denominator for gas-fraction versus efficiency tests
Abstract: We use a 6,729-galaxy downstream subset drawn from the 60,000-galaxy SDSS DR17 emission-line cache to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729) and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides an empirical baseline and candidate list for future CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
Conclusion: We have mapped the optical baseline for 6,729 massive quenched or transitioning galaxies in the SDSS emission-line sample. We find a BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729) and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, approximately 0.66 dex lower than star-forming counterparts. While these quantities define the target selection denominator for future CO gas-fraction versus efficiency programs, direct molecular gas masses and aperture-matched star formation rates remain required to physically distinguish depletion from low efficiency. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

### 09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
Title: SDSS target vector for feedback-model validation
Abstract: We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define a compact optical target vector for forward-model validation. The pilot records quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$), optical AGN incidence, and color versus mass/redshift across 15 mass-redshift cells with $n \geq 50$; across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). It remains an empirical denominator study rather than a direct simulation comparison.
Conclusion: We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, spanning $\log(M_\star/M_\odot)$ bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 across redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). This observed target vector is a compact benchmark for simulation forward modelling, but mock-observation pipelines are still required before any model comparison can be claimed. \begin{acknowledgments} We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only. \end{acknowledgments}

## Existing context
The previous overnight swarm improved candidate-copy manuscripts but user reports PDFs are still not publishable and some show LaTeX errors. Treat layout warnings, broken refs/citations, missing figures, and sloppy AAS presentation as real blockers to chase down in the copied TeX package.
codex
I’m inspecting the candidate package and its build artifacts first, then I’ll pin the blockers to specific files and lines so the writer can patch only what matters.
exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers | sed -n '1,220p'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.md
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/SOURCE_COPY.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/data/source_analysis_results.json
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-matched-offsets.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/figures/fig-bpt.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/figures/fig-topic.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.pdf
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex

exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z | rg 'log"'$|tex$|blg$|aux$|out$'"'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_01_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_01_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_01_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_01_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_01_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_01_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_01_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_01_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_01_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex

codex
I have the candidate tree. Next I’m checking the pre-audit manifest and the TeX bodies themselves so I can separate hard compile blockers from publishability problems.
exec
/bin/zsh -lc "sed -n '1,240p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.json" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
{
  "all_build_ok": false,
  "all_clean_ok": false,
  "candidate": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers",
  "created_utc": "2026-07-10T00:06:13Z",
  "cycle": 2,
  "label": "before",
  "results": [
    {
      "build_ok": false,
      "clean_ok": false,
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
      "interesting_log_lines": [
        "L36: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5",
        "L40: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input ",
        "L44: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5",
        "L49: Package natbib Warning: Citation `baldwin1981' on page 2 undefined on input lin",
        "L53: Package natbib Warning: Citation `kewley2001' on page 2 undefined on input line",
        "L57: Package natbib Warning: Citation `kauffmann2003bpt' on page 2 undefined on inpu",
        "L61: Package natbib Warning: Citation `kewley2006' on page 2 undefined on input line",
        "L66: Package natbib Warning: There were undefined citations.",
        "L70: Package natbib Warning: Citation(s) may have changed.",
        "L75: LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right."
      ],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.pdf",
      "pdf_bytes": 239853,
      "pdf_exists": true,
      "pdf_sha256": "8ea412b466ed223d850a6545ee01c2ef9518d2c2bd3c3d19f70cffb0c097ca22",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex",
      "undefined_count": 17,
      "warning_hits": {
        "Citation `": 7,
        "Package natbib Warning": 9,
        "Rerun to get cross-references right": 1,
        "undefined citation": 1
      }
    },
    {
      "build_ok": false,
      "clean_ok": false,
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
      "interesting_log_lines": [
        "L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin",
        "L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line",
        "L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu",
        "L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line",
        "L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5",
        "L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input ",
        "L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5",
        "L64: warning: m1_rp2_environment_quenching_integrated.tex:58: Underfull \\hbox (badness 1303) in paragraph at lines 57--58",
        "L65: Underfull \\hbox (badness 1303) in paragraph at lines 57--58",
        "L68: Package natbib Warning: Citation `peng2010' on page 2 undefined on input line 7",
        "L72: Package natbib Warning: Citation `baldry2006' on page 2 undefined on input line",
        "L76: Package natbib Warning: Citation `wetzel2013' on page 2 undefined on input line",
        "L80: Package natbib Warning: Citation `goubert2024' on page 2 undefined on input lin",
        "L85: Package natbib Warning: There were undefined citations.",
        "L89: Package natbib Warning: Citation(s) may have changed.",
        "L94: LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.",
        "L139: warning: m1_rp2_environment_quenching_integrated.tex:58: Underfull \\hbox (badness 1303) in paragraph at lines 57--58",
        "L140: Underfull \\hbox (badness 1303) in paragraph at lines 57--58"
      ],
      "label": "before",
      "layout_warning_count": 4,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.pdf",
      "pdf_bytes": 91356,
      "pdf_exists": true,
      "pdf_sha256": "b6865b3a27aa68bd82eb3cb178c6a09e93446daa2acf8513337a49734d21bdad",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex",
      "undefined_count": 25,
      "warning_hits": {
        "Citation `": 11,
        "Package natbib Warning": 13,
        "Rerun to get cross-references right": 1,
        "Underfull \\hbox": 4,
        "undefined citation": 1
      }
    },
    {
      "build_ok": false,
      "clean_ok": false,
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
      "interesting_log_lines": [
        "L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin",
        "L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line",
        "L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu",
        "L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line",
        "L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5",
        "L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input ",
        "L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5",
        "L64: warning: m1_rp3_maintenance_heating_integrated.tex:69: Underfull \\hbox (badness 1874) in paragraph at lines 68--69",
        "L65: Underfull \\hbox (badness 1874) in paragraph at lines 68--69",
        "L68: Package natbib Warning: Citation `best2005' on page 2 undefined on input line 7",
        "L72: Package natbib Warning: Citation `mcnamara2007' on page 2 undefined on input li",
        "L76: Package natbib Warning: Citation `mcnamara2012' on page 2 undefined on input li",
        "L80: Package natbib Warning: Citation `heckmanbest2014' on page 2 undefined on input",
        "L84: Package natbib Warning: Citation `eckert2024' on page 2 undefined on input line",
        "L94: Package natbib Warning: There were undefined citations.",
        "L98: Package natbib Warning: Citation(s) may have changed.",
        "L103: LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.",
        "L148: warning: m1_rp3_maintenance_heating_integrated.tex:69: Underfull \\hbox (badness 1874) in paragraph at lines 68--69",
        "L149: Underfull \\hbox (badness 1874) in paragraph at lines 68--69"
      ],
      "label": "before",
      "layout_warning_count": 4,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.pdf",
      "pdf_bytes": 90309,
      "pdf_exists": true,
      "pdf_sha256": "5e966058b540ac05201593b0788a7639dfa43a0c8693a7084629f05ce963a5b1",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex",
      "undefined_count": 27,
      "warning_hits": {
        "Citation `": 12,
        "Package natbib Warning": 14,
        "Rerun to get cross-references right": 1,
        "Underfull \\hbox": 4,
        "undefined citation": 1
      }
    },
    {
      "build_ok": false,
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
        "L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin",
        "L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line",
        "L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu",
        "L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line",
        "L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5",
        "L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input ",
        "L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5",
        "L65: Package natbib Warning: Citation `veilleux2005' on page 2 undefined on input li",
        "L69: Package natbib Warning: Citation `cicone2014' on page 2 undefined on input line",
        "L73: Package natbib Warning: Citation `fiore2017' on page 2 undefined on input line ",
        "L77: Package natbib Warning: Citation `carniani2017' on page 2 undefined on input li",
        "L81: Package natbib Warning: Citation `fabian2012' on page 2 undefined on input line",
        "L91: Package natbib Warning: There were undefined citations.",
        "L95: Package natbib Warning: Citation(s) may have changed.",
        "L100: LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right."
      ],
      "label": "before",
      "layout_warning_count": 0,
      "log": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.before.strict.log",
      "pdf": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.pdf",
      "pdf_bytes": 321925,
      "pdf_exists": true,
      "pdf_sha256": "a8068e46fa9c6446e3416c15f6568541e78fc9e8ec1cacc6fc3c3b3dd6b05b7f",
      "returncode": 0,
      "tex": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex",
      "undefined_count": 27,
      "warning_hits": {
        "Citation `": 12,
        "Package natbib Warning": 14,
        "Rerun to get cross-references right": 1,
        "undefined citation": 1
      }
    },
    {
      "build_ok": false,
      "clean_ok": false,
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
      "interesting_log_lines": [
        "L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin",
        "L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line",
        "L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu",
        "L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line",
        "L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5",
        "L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input ",
        "L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5",
        "L65: Package natbib Warning: Citation `best2005' on page 2 undefined on input line 7",
        "L69: Package natbib Warning: Citation `santoro2020' on page 2 undefined on input lin",
        "L73: Package natbib Warning: Citation `mcnamara2007' on page 2 undefined on input li",
        "L77: Package natbib Warning: Citation `eckert2024' on page 2 undefined on input line",
        "L81: warning: m2_p2_radio_jet_environment_integrated.tex:73: Underfull \\hbox (badness 10000) in paragraph at lines 72--73",
        "L82: Underfull \\hbox (badness 10000) in paragraph at lines 72--73",
        "L86: Package natbib Warning: There were undefined citations.",
        "L90: Package natbib Warning: Citation(s) may have changed.",
        "L95: LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.",

exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.md" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
# Strict LaTeX audit before cycle 2

all_build_ok: False
all_clean_ok: False
layout_warning_count: 24
undefined_count: 239

## m1_rp1_sdss_agn_sfr_integrated.tex
- build_ok=False clean_ok=False rc=0 bytes=239853
- fatal_hits={}
- warning_hits={'Citation `': 7, 'undefined citation': 1, 'Package natbib Warning': 9, 'Rerun to get cross-references right': 1}
- log lines:
  - L36: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L40: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L44: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L49: Package natbib Warning: Citation `baldwin1981' on page 2 undefined on input lin
  - L53: Package natbib Warning: Citation `kewley2001' on page 2 undefined on input line
  - L57: Package natbib Warning: Citation `kauffmann2003bpt' on page 2 undefined on inpu
  - L61: Package natbib Warning: Citation `kewley2006' on page 2 undefined on input line
  - L66: Package natbib Warning: There were undefined citations.
  - L70: Package natbib Warning: Citation(s) may have changed.
  - L75: LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

## m1_rp2_environment_quenching_integrated.tex
- build_ok=False clean_ok=False rc=0 bytes=91356
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 4, 'Citation `': 11, 'undefined citation': 1, 'Package natbib Warning': 13, 'Rerun to get cross-references right': 1}
- log lines:
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L64: warning: m1_rp2_environment_quenching_integrated.tex:58: Underfull \hbox (badness 1303) in paragraph at lines 57--58
  - L65: Underfull \hbox (badness 1303) in paragraph at lines 57--58
  - L68: Package natbib Warning: Citation `peng2010' on page 2 undefined on input line 7
  - L72: Package natbib Warning: Citation `baldry2006' on page 2 undefined on input line
  - L76: Package natbib Warning: Citation `wetzel2013' on page 2 undefined on input line

## m1_rp3_maintenance_heating_integrated.tex
- build_ok=False clean_ok=False rc=0 bytes=90309
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 4, 'Citation `': 12, 'undefined citation': 1, 'Package natbib Warning': 14, 'Rerun to get cross-references right': 1}
- log lines:
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L64: warning: m1_rp3_maintenance_heating_integrated.tex:69: Underfull \hbox (badness 1874) in paragraph at lines 68--69
  - L65: Underfull \hbox (badness 1874) in paragraph at lines 68--69
  - L68: Package natbib Warning: Citation `best2005' on page 2 undefined on input line 7
  - L72: Package natbib Warning: Citation `mcnamara2007' on page 2 undefined on input li
  - L76: Package natbib Warning: Citation `mcnamara2012' on page 2 undefined on input li

## m2_p1_outflow_escape_recycling_integrated.tex
- build_ok=False clean_ok=False rc=0 bytes=321925
- fatal_hits={}
- warning_hits={'Citation `': 12, 'undefined citation': 1, 'Package natbib Warning': 14, 'Rerun to get cross-references right': 1}
- log lines:
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L65: Package natbib Warning: Citation `veilleux2005' on page 2 undefined on input li
  - L69: Package natbib Warning: Citation `cicone2014' on page 2 undefined on input line
  - L73: Package natbib Warning: Citation `fiore2017' on page 2 undefined on input line 
  - L77: Package natbib Warning: Citation `carniani2017' on page 2 undefined on input li
  - L81: Package natbib Warning: Citation `fabian2012' on page 2 undefined on input line

## m2_p2_radio_jet_environment_integrated.tex
- build_ok=False clean_ok=False rc=0 bytes=90109
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 4, 'Citation `': 11, 'undefined citation': 1, 'Package natbib Warning': 13, 'Rerun to get cross-references right': 1}
- log lines:
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L65: Package natbib Warning: Citation `best2005' on page 2 undefined on input line 7
  - L69: Package natbib Warning: Citation `santoro2020' on page 2 undefined on input lin
  - L73: Package natbib Warning: Citation `mcnamara2007' on page 2 undefined on input li
  - L77: Package natbib Warning: Citation `eckert2024' on page 2 undefined on input line
  - L81: warning: m2_p2_radio_jet_environment_integrated.tex:73: Underfull \hbox (badness 10000) in paragraph at lines 72--73

## m2_p3_feedback_transition_mass_integrated.tex
- build_ok=False clean_ok=False rc=0 bytes=95242
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 8, 'Citation `': 14, 'undefined citation': 1, 'Package natbib Warning': 16, 'Rerun to get cross-references right': 1}
- log lines:
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L64: warning: m2_p3_feedback_transition_mass_integrated.tex:58: Underfull \hbox (badness 2134) in paragraph at lines 57--58
  - L65: Underfull \hbox (badness 2134) in paragraph at lines 57--58
  - L68: Package natbib Warning: Citation `kauffmann2003mass' on page 2 undefined on inp
  - L72: Package natbib Warning: Citation `baldry2004' on page 2 undefined on input line
  - L76: Package natbib Warning: Citation `peng2010' on page 2 undefined on input line 7

## m3_p1_multiphase_census_integrated.tex
- build_ok=False clean_ok=False rc=0 bytes=88515
- fatal_hits={}
- warning_hits={'Citation `': 14, 'undefined citation': 1, 'Package natbib Warning': 16, 'Rerun to get cross-references right': 1}
- log lines:
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L65: Package natbib Warning: Citation `veilleux2005' on page 2 undefined on input li
  - L69: Package natbib Warning: Citation `rupke2018' on page 2 undefined on input line 
  - L73: Package natbib Warning: Citation `cicone2014' on page 2 undefined on input line
  - L77: Package natbib Warning: Citation `fiore2017' on page 2 undefined on input line 
  - L81: Package natbib Warning: Citation `feruglio2015' on page 2 undefined on input li

## m3_p2_gas_depletion_efficiency_integrated.tex
- build_ok=False clean_ok=False rc=0 bytes=218136
- fatal_hits={}
- warning_hits={'Citation `': 11, 'undefined citation': 1, 'Package natbib Warning': 13, 'Rerun to get cross-references right': 2}
- log lines:
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L65: Package natbib Warning: Citation `coldgass1' on page 2 undefined on input line 
  - L69: Package natbib Warning: Citation `coldgass2' on page 2 undefined on input line 
  - L73: Package natbib Warning: Citation `xcoldgass2017' on page 2 undefined on input l
  - L77: Package natbib Warning: Citation `xgass2018' on page 2 undefined on input line 
  - L82: Package natbib Warning: There were undefined citations.

## m3_p3_simulation_validation_integrated.tex
- build_ok=False clean_ok=False rc=0 bytes=96217
- fatal_hits={}
- warning_hits={'Underfull \\hbox': 4, 'Citation `': 14, 'undefined citation': 1, 'Package natbib Warning': 16, 'Rerun to get cross-references right': 1}
- log lines:
  - L36: Package natbib Warning: Citation `baldwin1981' on page 1 undefined on input lin
  - L40: Package natbib Warning: Citation `kewley2001' on page 1 undefined on input line
  - L44: Package natbib Warning: Citation `kauffmann2003bpt' on page 1 undefined on inpu
  - L48: Package natbib Warning: Citation `kewley2006' on page 1 undefined on input line
  - L52: Package natbib Warning: Citation `sdssdr17' on page 1 undefined on input line 5
  - L56: Package natbib Warning: Citation `brinchmann2004' on page 1 undefined on input 
  - L60: Package natbib Warning: Citation `york2000' on page 1 undefined on input line 5
  - L64: warning: m3_p3_simulation_validation_integrated.tex:56: Underfull \hbox (badness 1546) in paragraph at lines 55--56
  - L65: Underfull \hbox (badness 1546) in paragraph at lines 55--56
  - L68: Package natbib Warning: Citation `imanga2023' on page 2 undefined on input line
  - L72: Package natbib Warning: Citation `tng2019' on page 2 undefined on input line 70
  - L76: Package natbib Warning: Citation `eagle2015' on page 2 undefined on input line 

codex
The main compile signal so far is unresolved bibliography state, not hard TeX failures. I’m now checking whether those citation keys are actually missing from the package or just not fully resolved in the one-run audit, and I’m reading the manuscript sections for publishability issues.
exec
/bin/zsh -lc "rg --files /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers | rg '\\.(bib|bbl|tex|sty)"'$'"'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex

exec
/bin/zsh -lc "for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/*/aastex/*_integrated.tex; do echo '---'"'$(basename "$f"); rg -n '"'\\\\(cite|citet|citep|bibliography|bibitem|begin\\{figure\\}|includegraphics|section\\{|subsection\\{|acknowledgments|paragraph\\{|label\\{|ref\\{)' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
---m1_rp1_sdss_agn_sfr_integrated.tex
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
55:BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.
64:\includegraphics[width=0.73\textwidth]{../figures/fig-bpt.pdf}
66:\label{fig:bpt}
71:\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
73:\label{fig:offsets}
77:\section{Data Availability}\label{sec:data-avail}
80:\section{Conclusion}\label{sec:conclusion}
89:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
90:\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
91:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
92:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
93:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
94:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
95:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
---m1_rp2_environment_quenching_integrated.tex
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
64:\label{fig:topic}
67:\section{Interpretation and missing observables}\label{sec:missing}
72:Mass and environment are known separable axes in low-redshift galaxy evolution, but a real environmental-quenching analysis requires group/halo and central-satellite information beyond this nearest-neighbor proxy \citep{peng2010,baldry2006,wetzel2013,goubert2024}.
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
87:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
88:\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
89:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
90:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
91:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
92:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
93:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
94:\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., Balogh, M.~L., Bower, R.~G., et al. 2006, MNRAS, 373, 469
95:\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, MNRAS, 528, 3822
96:\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
97:\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
---m1_rp3_maintenance_heating_integrated.tex
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical denominator for maintenance-heating follow-up}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
64:\label{fig:topic}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
85:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
86:\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
87:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
88:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
89:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
90:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
91:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
92:\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
93:\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
94:\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
95:\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
96:\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New J. Phys., 14, 055023
---m2_p1_outflow_escape_recycling_integrated.tex
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical denominator for outflow escape tests}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
64:\label{fig:topic}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005,cicone2014,fiore2017,carniani2017,fabian2012}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
85:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
86:\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
87:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
88:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
89:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
90:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
91:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
92:\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
93:\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
94:\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
95:\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
96:\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
---m2_p2_radio_jet_environment_integrated.tex
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
64:\label{fig:topic}
67:\section{Interpretation and missing observables}\label{sec:missing}
72:The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}.
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}
87:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
88:\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
89:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
90:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
91:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
92:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
93:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
94:\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
95:\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
96:\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
97:\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
---m2_p3_feedback_transition_mass_integrated.tex
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
64:\label{fig:topic}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
85:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
86:\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
87:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
88:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
89:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
90:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
91:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
92:\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
93:\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
94:\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
95:\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
96:\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
97:\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
98:\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
---m3_p1_multiphase_census_integrated.tex
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical census of multiphase target denominators}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
64:\label{fig:topic}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
85:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
86:\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
87:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
88:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
89:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
90:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
91:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
92:\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
93:\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
94:\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
95:\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
96:\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
97:\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
98:\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
---m3_p2_gas_depletion_efficiency_integrated.tex
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities, ending with the paper-specific downstream subset.\label{tab:selection-cascade}}
52:\section{Measurements}\label{sec:measurements}
53:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
57:\section{Optical denominator for gas-fraction versus efficiency tests}\label{sec:topic-result}
63:\begin{figure}
65:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
67:\label{fig:topic}
70:\section{Interpretation and missing observables}\label{sec:missing}
73:Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}.
76:\section{Data Availability}\label{sec:data-avail}
79:\section{Conclusion}\label{sec:conclusion}
88:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
89:\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
90:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
91:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
92:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
93:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
94:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
95:\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
96:\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
97:\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
98:\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
---m3_p3_simulation_validation_integrated.tex
21:\section{Introduction}\label{sec:introduction}
25:\section{Data and Sample Selection}\label{sec:shared-selection}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
49:\section{Measurements}\label{sec:measurements}
50:The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
54:\section{Optical target vector for simulation validation}\label{sec:topic-result}
60:\begin{figure}
62:\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
64:\label{fig:topic}
67:\section{Interpretation and missing observables}\label{sec:missing}
70:Simulation suites such as TNG, EAGLE, and SIMBA define the future comparison problem. The iMaNGA observational catalog \citep{imanga2023} provides a complementary benchmark for mock-observation work. No simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,donnari2021,dubois2013,dubois2016}.
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}
85:\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
86:\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
87:\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
88:\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
89:\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
90:\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
91:\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
92:\bibitem[Dav\'e et al.(2019)]{simba2019} Dav\'e, R., Angl\'es-Alc\'azar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
93:\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
94:\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
95:\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
96:\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
97:\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
98:\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521

codex
I’ve confirmed the citation sets are present in the TeX files themselves. I’m now mapping the log warnings back onto the exact prose blocks so the writer can fix layout and publishability at the right spots instead of guessing.
exec
/bin/zsh -lc "for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/*/aastex/*_integrated.tex; do echo '###'"'$(basename "$f"); nl -ba "$f" | sed -n '"'1,120p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
###m1_rp1_sdss_agn_sfr_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS optical AGN/sSFR matched-control pilot}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We present a selection-aware matched-control comparison of catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. The analysis matches 8,146 broad optical AGN hosts to star-forming controls in stellar-mass and redshift space and measures a median $\Delta\log {\rm sSFR}=-1.309$ dex; at S/N$\geq 10$, the corresponding matched offset is $-0.744$ dex. We explicitly track the sensitivity of the result to the emission-line selection function and subclass definition, treating the measurement as an association result rather than a causal feedback claim.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	While characterizing causal feedback typically requires multi-wavelength data, establishing a rigorous optical baseline is an essential first step. In this analysis, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. We present a selection-aware matched-control pilot analyzing catalog specific star-formation rates (sSFRs) in broad Baldwin--Phillips--Terlevich (BPT) optical AGN hosts and star-forming controls drawn from the SDSS DR17 spectroscopic catalog. Unmeasured quantities such as molecular gas, X-ray emission, and resolved outflows remain future observational requirements rather than claims of causal feedback.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note uses a capped subset of 60,000 SDSS DR17 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
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
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Flagship integrated result: optical AGN and catalog sSFR}\label{sec:rp1-result}
    55	BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ line ratios using the standard Baldwin--Phillips--Terlevich diagram and Kauffmann/Kewley demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. The cached analysis table contains 39,553 star-forming galaxies, 12,234 intermediate/composite objects, 8,146 broad optical AGN, and 67 unclassified objects.
    56	
    57	The preferred estimator matches every broad optical AGN host to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement. This is an association design; controls are not matched in morphology, halo mass, gas mass, aperture scale, AGN luminosity, or duty-cycle phase.
    58	
    59	Our comparison of broad BPT optical AGN hosts versus star-forming controls at S/N$\geq 3$ matches $N=8,146$ pairs, measuring a median specific star formation rate offset of $\Delta\log {\rm sSFR}=-1.309$ dex with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Applying a moderate mass-redshift caliper of $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$ retains $N=7,867$ pairs (96.6\% target coverage) and yields a median offset of $-1.318$ dex. A deterministic matching run without replacement yields $N=7,419$ matched pairs and a median offset of $-1.446$ dex, though with poorer stellar-mass balance. Raising the line-S/N threshold to 10 leaves $N=1,530$ matched pairs and reduces the median offset to $-0.744$ dex, and a narrower [N II] Seyfert-like proxy yields $N=2,114$ pairs and a median offset of $-0.763$ dex.
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
    86	
    87	
    88	\begin{thebibliography}{}
    89	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    90	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    91	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    92	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    93	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    94	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    95	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    96	
    97	\end{thebibliography}
    98	
    99	\end{document}
###m1_rp2_environment_quenching_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS density proxy for environmental quenching}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS density proxy for environmental quenching}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a representative 60,000-galaxy subset of the SDSS DR17 emission-line catalog to build an optical density-proxy analysis of environmental quenching. A 10th-nearest-neighbor density proxy is compared with quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) after controlling for stellar mass and redshift; using equal-count density quartiles, the high-density quartile has quenched fraction 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile. The bootstrap high-minus-low interval is [0.041, 0.059], which excludes zero. This analysis is intentionally limited to the optical denominator and leaves the missing group and halo information for future study.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Establishing environmental quenching baselines in wide-field optical surveys is useful before applying more complex group or halo metrics. In this analysis, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. We evaluate a local 10th-nearest-neighbor density proxy using SDSS DR17 emission-line galaxies and restrict the scope to directly measured optical properties. Group membership and halo mass remain future observational requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note uses the same public SDSS DR17 parent selection as the companion papers, but it interprets that denominator as an environmental-quenching baseline rather than a feedback or outflow sample. The capped subset contains 60,000 emission-line galaxies from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
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
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{SDSS density-proxy result for environmental quenching}\label{sec:topic-result}
    55	We examine whether a nearest-neighbor density proxy adds quenched-fraction information beyond stellar mass in the SDSS emission-line sample. The result is an optical baseline rather than a full physical-feedback test.
    56	
    57	Our SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-nearest-neighbor local density proxy. Using equal-count density quartiles, the high-density quartile exhibits a quenched fraction of $0.230 \pm 0.003$ ($3,456/15,000$) compared with $0.181 \pm 0.003$ ($2,710/15,000$) in the low-density quartile. The bootstrap high-minus-low quenched-fraction difference interval is $[0.041,0.059]$, which excludes zero. A linear probability model controlling for log stellar mass and redshift yields a high-density coefficient of $0.032 \pm 0.004$, confirming that the density proxy correlates with quenching independently of the controlled host-galaxy properties.
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
    72	Mass and environment are known separable axes in low-redshift galaxy evolution, but a real environmental-quenching analysis requires group/halo and central-satellite information beyond this nearest-neighbor proxy \citep{peng2010,baldry2006,wetzel2013,goubert2024}.
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
    84	
    85	
    86	\begin{thebibliography}{}
    87	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    88	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    89	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    90	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    91	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    92	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    93	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    94	\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., Balogh, M.~L., Bower, R.~G., et al. 2006, MNRAS, 373, 469
    95	\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, MNRAS, 528, 3822
    96	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    97	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
    98	\end{thebibliography}
    99	
   100	\end{document}
###m1_rp3_maintenance_heating_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Optical-AGN denominator for maintenance-heating follow-up}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Optical-AGN denominator for maintenance-heating follow-up}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to construct an optical denominator for maintenance-heating follow-up in massive galaxies. Among massive, low-sSFR hosts, the BPT-AGN fraction is 0.430 (3,997/9,298) in the massive subset and 0.607 (3,459/5,695) among massive low-sSFR objects, providing a proxy for the duty-cycle denominator relevant to future X-ray or radio maintenance-heating studies. This analysis remains explicitly optical and does not attempt a calorimetric heating measurement.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Maintenance-heating interpretations require X-ray or radio observables, but a rigorous optical denominator is a necessary first step. In this analysis, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. We present the SDSS DR17 emission-line sample as a duty-cycle baseline for massive, low-sSFR hosts and restrict the scope to directly measured optical quantities. X-ray cavities, radio power, and hot-gas energetics remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 emission-line parent selection, but it treats the resulting denominator as a maintenance-heating follow-up baseline for massive, low-sSFR hosts. The capped subset contains 60,000 galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
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
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for maintenance-heating follow-up}\label{sec:topic-result}
    55	Among massive, low-sSFR SDSS emission-line galaxies, we quantify the optical AGN fraction available as a denominator for X-ray and radio maintenance-heating follow-up. The result is an optical baseline rather than a calorimetric measurement.
    56	
    57	The massive galaxy subset ($\log M_\star \geq 10.8$) contains 9,298 emission-line galaxies, of which 5,695 are classified as low-sSFR based on the specific star formation rate threshold of $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$ applied in this analysis. The optical BPT AGN fraction is measured as 0.430 (3,997/9,298) in the total massive subset, rising to 0.607 (3,459/5,695) when restricting the sample to massive low-sSFR objects. This empirical duty-cycle baseline is intended for future X-ray or radio maintenance-heating follow-up and is not a heating measurement.
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
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.
    69	
    70	Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}.
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
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    93	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
    94	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
    95	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    96	\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New J. Phys., 14, 055023
    97	\end{thebibliography}
    98	
    99	\end{document}
###m2_p1_outflow_escape_recycling_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS BPT-selected optical AGN denominator for outflow escape tests}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS BPT-selected optical AGN denominator for outflow escape tests}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define the optical denominator for an outflow escape-versus-recycling program. The analysis counts 4,440 BPT-selected optical AGN candidates (0.074 $\pm$ 0.001) and records their median $\log {\rm sSFR} = -11.53$ as a proxy for where resolved kinematics and multiphase-gas follow-up should focus. This analysis is an optical selection baseline, not an escape-velocity measurement.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	An optical line-ratio selection can define a useful target set for future outflow work, but it cannot measure escape or recycling on its own. In this analysis, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. We present the SDSS DR17 emission-line sample as an optical baseline for massive galaxies and restrict the scope to directly measured quantities. Resolved kinematics, halo potentials, and multiphase gas remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note keeps the shared SDSS DR17 parent selection but interprets it as an outflow-escape follow-up denominator rather than a direct outflow measurement. The capped subset contains 60,000 emission-line galaxies from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
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
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
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
    57	BPT-selected optical AGN candidates number 4,440 of 60,000 emission-line galaxies ($0.074 \pm 0.001$). Their median $\log {\rm sSFR}$ is $-11.53$, compared with $-10.14$ for the full denominator. This optical sample defines a follow-up denominator for resolved escape/recycling work, but SDSS alone cannot measure outflow velocity or fate.
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
    70	Wind and outflow literature specifies the missing kinematic, geometric, molecular, and multiphase measurements; these sources motivate follow-up and do not turn line-ratio selection into an escape/recycling measurement \citep{veilleux2005,cicone2014,fiore2017,carniani2017,fabian2012}.
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
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
    93	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    94	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
    95	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    96	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    97	\end{thebibliography}
    98	
    99	\end{document}
###m2_p2_radio_jet_environment_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Environment proxy for optical AGN in massive SDSS hosts}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Environment proxy for optical AGN in massive SDSS hosts}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We build an optical denominator for radio-jet environment follow-up using a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. In massive hosts, the high-density quartile has optical AGN fraction 0.509 $\pm$ 0.012 and the low-density quartile has 0.367 $\pm$ 0.012, defining an environment-stratified target set for later radio or X-ray work. The result is an optical baseline only; it does not measure jet power or coupling efficiency.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Radio-jet environment studies require radio and X-ray data, but an optical denominator is a useful starting point. In this analysis, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. We present the SDSS DR17 emission-line sample as an environment-stratified baseline for massive hosts and restrict the analysis to directly measured optical quantities. Jet power, coupling efficiency, and hot-gas structure remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 emission-line denominator, but it interprets the result as an environment-stratified baseline for radio-jet follow-up in massive hosts. The capped subset contains 60,000 galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
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
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for radio-jet environment follow-up}\label{sec:topic-result}
    55	We examine whether a local-density proxy modulates the optical AGN fraction in massive SDSS hosts. The result is an environment-stratified optical baseline for future radio and X-ray jet-coupling work.
    56	
    57	Among massive hosts, the high-density quartile has optical AGN fraction $0.509 \pm 0.012$, while the low-density quartile has $0.367 \pm 0.012$. The bootstrap high-minus-low interval is $[0.112,0.170]$. This is an optical/environment denominator for radio-jet coupling work and does not measure jet power or coupling efficiency.
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
    72	The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}.
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
    84	
    85	
    86	\begin{thebibliography}{}
    87	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    88	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    89	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    90	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    91	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    92	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    93	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    94	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    95	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
    96	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    97	\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
    98	\end{thebibliography}
    99	
   100	\end{document}
###m2_p3_feedback_transition_mass_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS mass transition in quenching and optical AGN incidence}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS mass transition in quenching and optical AGN incidence}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to identify the stellar-mass regime where quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$) and optical AGN incidence rise together. The analysis remains optical: it provides a denominator and transition vector for future gas-fraction and baryon-deficit work, and the first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail at $\log(M_\star/M_\odot)>11.0$, where the optical AGN fraction peaks at 0.520 (2,098/4,033). It does not assign the transition to stellar or AGN feedback on its own.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	The stellar-mass scale where quenched fraction and optical AGN incidence rise together is useful as an empirical transition marker, but it is not by itself a physical-feedback measurement. In this analysis, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. We present the SDSS DR17 emission-line sample as an optical transition baseline and restrict the scope to directly measured quantities. Gas fractions, baryon deficits, and halo-scale measurements remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 parent selection, but it interprets the outcome as a transition-mass baseline for quenching and optical AGN incidence. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
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
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical denominator for feedback-transition mass}\label{sec:topic-result}
    55	We identify the stellar-mass scale at which quenched fraction and optical AGN incidence rise together in the SDSS emission-line sample. The result is an empirical optical transition vector rather than a full physical-feedback test.
    56	
    57	The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot)>11.0$, and the optical AGN fraction peaks in that same bin at 0.520 (2,098/4,033). This empirical transition vector is an optical diagnostic only; gas fractions and baryon deficits are still required before assigning the trend to stellar or AGN feedback.
    58	
    59	
    60	\begin{figure}
    61	\centering
    62	\includegraphics[width=\columnwidth]{../figures/fig-topic.pdf}
    63	\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows the high-mass tail ($\log(M_\star/M_\odot)>11.0$) where the quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520 (2,098/4,033).}
    64	\label{fig:topic}
    65	\end{figure}
    66	
    67	\section{Interpretation and missing observables}\label{sec:missing}
    68	This SDSS-only pilot is intentionally limited to optical quantities. A full proposal requires gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.
    69	
    70	Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	The first stellar-mass bin with quenched fraction above 0.5 is the high-mass tail, defined here as $\log(M_\star/M_\odot)>11.0$, and the optical AGN fraction peaks at 0.520 (2,098/4,033) in that same bin. These values define an optical transition vector, but gas fractions, baryon deficits, and halo-scale measurements are still needed before a causal feedback interpretation.
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
    93	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    94	\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
    95	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
    96	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    97	\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
    98	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
    99	\end{thebibliography}
   100	
   101	\end{document}
###m3_p1_multiphase_census_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Common-denominator optical tracer census in SDSS}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Common-denominator optical tracer census in SDSS}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We build a common optical denominator for a multiphase outflow census from a 60,000-galaxy subset of the SDSS DR17 emission-line catalog. Simple tracer definitions change the inferred AGN or feedback-candidate prevalence within the same denominator, from 0.136 for BPT AGN to 0.418 for red+emission, so this note focuses on the optical selection baseline needed before adding ionized, neutral, molecular, or X-ray/radio tracers. This is a denominator study, not a multiphase outflow measurement.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Multiphase outflow work requires ionized, neutral, molecular, and X-ray or radio measurements, but a common optical denominator is a practical starting point. In this analysis, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. We present the SDSS DR17 emission-line sample as that baseline and restrict the manuscript to directly measured optical quantities. The missing multiphase observables remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 parent selection, but it interprets the result as a common denominator for a multiphase tracer census. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
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
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical census of multiphase target denominators}\label{sec:topic-result}
    55	We examine how simple optical tracer definitions change the inferred AGN and feedback-candidate prevalence within one common SDSS denominator. The result is an optical baseline for later multiphase follow-up rather than a direct multiphase measurement.
    56	
    57	Within the same 60,000-galaxy denominator, the BPT AGN and red+emission definitions produce prevalence from 0.136 for BPT AGN to 0.418 for red+emission, a factor of 3.1. That spread shows why a common-denominator census is required, while also underscoring that the present SDSS sample cannot measure molecular, neutral, or X-ray/radio outflow phases.
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
    70	A real multiphase census needs independent ionized, neutral, molecular, and energetic outflow observables; the present SDSS thresholds are an optical denominator only \citep{veilleux2005,rupke2018,cicone2014,fiore2017,feruglio2015,woo2016,bae2018}.
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
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
    93	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    94	\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
    95	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    96	\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
    97	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    98	\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
    99	\end{thebibliography}
   100	
   101	\end{document}
###m3_p2_gas_depletion_efficiency_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{Optical denominator for gas-fraction versus efficiency tests}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{Optical denominator for gas-fraction versus efficiency tests}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 6,729-galaxy downstream subset drawn from the 60,000-galaxy SDSS DR17 emission-line cache to construct an optical selection baseline and denominator for future molecular gas-fraction versus star-formation efficiency follow-up. For massive quenched or transitioning galaxies, we measure an optical BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729) and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, which is offset by $-0.66$ dex relative to massive star-forming controls. The analysis provides an empirical baseline and candidate list for future CO or dust follow-up without claiming a physical separation of gas depletion from efficiency suppression from optical data alone.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Gas-fraction and star-formation-efficiency interpretations require CO or dust data, but the optical denominator is the necessary starting point. In this analysis, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. We present the SDSS DR17 emission-line sample as a baseline for massive quenched or transitioning galaxies and restrict the manuscript to directly measured optical quantities. Direct molecular gas masses and aperture-matched star-formation rates remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 parent selection, but it interprets the result as an optical denominator for gas-fraction versus efficiency follow-up. The capped subset contains 60,000 galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities, ending with the paper-specific downstream subset.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
    34	plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 0.831 \\
    35	plus galSpecLine join & 416,554 & -- & 0.831 \\
    36	four BPT lines positive with positive errors & 373,445 & 60,000 & 0.745 \\
    37	four BPT lines S/N$\geq 3$ & 249,917 & 60,000 & 0.499 \\
    38	four BPT lines S/N$\geq 5$ & 176,523 & 42,446 & 0.352 \\
    39	four BPT lines S/N$\geq 10$ & 91,768 & 22,311 & 0.183 \\
    40	Massive quenched or transitioning subset & -- & 6,729 & -- \\
    41	\enddata
    42	\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached local CSV. Cached rows are shown only where the cache applies. The final row defines the specific 6,729-galaxy subset used in this optical baseline.}
    43	\end{deluxetable*}
    44	
    45	The paper-specific downstream selection retains 6,729 massive quenched or transitioning galaxies from the cached 60,000-galaxy parent, as fixed by the cached selection manifest. That branch is the denominator used for the gas-fraction versus efficiency result below, and it is a local subset rather than a separate public DR17 count query.
    46	
    47	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    48	
    49	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
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
    60	The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is $0.549 \pm 0.006$, and the median H$\alpha$ luminosity proxy is $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$. The median H$\alpha$ luminosity proxy is approximately 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline.
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
    73	Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}.
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
    85	
    86	
    87	\begin{thebibliography}{}
    88	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    89	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    90	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    91	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    92	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    93	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    94	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    95	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
    96	\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
    97	\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
    98	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
    99	\end{thebibliography}
   100	
   101	\end{document}
###m3_p3_simulation_validation_integrated.tex
     1	\documentclass[twocolumn]{aastex631}
     2	\usepackage{amsmath}
     3	\usepackage{booktabs}
     4	\shorttitle{SDSS target vector for feedback-model validation}
     5	\shortauthors{NebulaMind Research Autopilot}
     6	\begin{document}
     7	
     8	\title{SDSS target vector for feedback-model validation}
     9	\author{NebulaMind Research Autopilot}
    10	\affiliation{NebulaMind Astrophysics Collaboration, San Francisco, CA 94107, USA}
    11	\correspondingauthor{NebulaMind Research Autopilot}
    12	\email{autopilot@nebulamind.ai}
    13	
    14	\begin{abstract}
    15	We use a 60,000-galaxy subset of the SDSS DR17 emission-line catalog to define a compact optical target vector for forward-model validation. The pilot records quenched fraction (defined by specific star-formation rate $\log(\mathrm{sSFR}/\mathrm{yr}^{-1}) < -11.0$), optical AGN incidence, and color versus mass/redshift across 15 mass-redshift cells with $n \geq 50$; across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). It remains an empirical denominator study rather than a direct simulation comparison.
    16	\end{abstract}
    17	
    18	\keywords{galaxies: evolution --- galaxies: active --- galaxies: star formation --- surveys --- methods: data analysis}
    19	\software{Astropy, SciPy, NumPy, Matplotlib, pandas}
    20	
    21	\section{Introduction}\label{sec:introduction}
    22	Forward-model validation requires simulation mocks, but an observational target vector is a useful starting point. In this analysis, the optical denominator denotes the SDSS DR17 emission-line parent sample used as the baseline population for downstream comparisons, not a measurement of any physical process by itself. We present the SDSS DR17 emission-line sample as a compact optical baseline and restrict the manuscript to directly measured quantities. Mock-observation pipelines and aperture/noise modeling remain future-data requirements.
    23	
    24	
    25	\section{Data and Sample Selection}\label{sec:shared-selection}
    26	This note reuses the shared SDSS DR17 parent selection, but it interprets the result as an observational target vector for later simulation validation. The capped subset contains 60,000 emission-line galaxies selected from public spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates. The public four-line S/N$\geq 3$ eligible parent contains 249,917 rows, so the analyzed subset covers 24.0\% of that parent. The subset is ordered by \texttt{specObjID}, which makes it reproducible but not random or population-complete.
    27	
    28	\begin{deluxetable*}{lrrr}
    29	\tabletypesize{\scriptsize}
    30	\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
    31	\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent (fraction)}}
    32	\startdata
    33	SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 1.000 \\
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
    44	The four-line requirement is strongly selection dependent. In the public counts, S/N$\geq 3$ keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Therefore every incidence, quenching, density, gas-denominator, or target-vector statement in this analysis is conditional on the four-line emission-line selection.
    45	
    46	Local subset versus public catalog marginal checks found no redshift, stellar-mass, or sSFR bin with a subset-minus-public fraction difference above 5 percentage points. The largest absolute differences were 2.03 percentage points in redshift, -1.63 percentage points in stellar mass, and -0.58 percentage points in sSFR. This is a representativeness diagnostic only; it does not make the capped cache random or complete.
    47	
    48	
    49	\section{Measurements}\label{sec:measurements}
    50	The row-level measurements include redshift, stellar mass, catalog specific star-formation rate, model colors, and four optical line fluxes/errors. BPT labels and all derived denominators are recomputed locally from the cached table \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006}. Catalog SFR/sSFR values are treated as low-redshift SDSS physical-property estimates rather than direct resolved gas or feedback measurements \citep{sdssdr17,brinchmann2004,york2000}.
    51	Unless otherwise noted, quoted fraction uncertainties are binomial counting uncertainties from the stated sample sizes, and bracketed intervals are bootstrap confidence intervals.
    52	
    53	
    54	\section{Optical target vector for simulation validation}\label{sec:topic-result}
    55	We define a compact SDSS target vector of quenched fraction, optical AGN incidence, and color versus mass/redshift for forward-model validation. The result is an observed optical baseline rather than a full physical-feedback test.
    56	
    57	We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, so that simple Poisson counting errors remain at or below roughly 14\%; the cell grid spans $\log(M_\star/M_\odot)$ bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 crossed with redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Across mass bins, quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). The observed target vector is useful for simulation forward modelling, but it still requires mock-observation pipelines before any model comparison can be claimed.
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
    70	Simulation suites such as TNG, EAGLE, and SIMBA define the future comparison problem. The iMaNGA observational catalog \citep{imanga2023} provides a complementary benchmark for mock-observation work. No simulation mock has been forward-modelled or ranked in this pilot \citep{tng2019,eagle2015,simba2019,donnari2021,dubois2013,dubois2016}.
    71	
    72	
    73	\section{Data Availability}\label{sec:data-avail}
    74	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    75	
    76	\section{Conclusion}\label{sec:conclusion}
    77	We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector, spanning $\log(M_\star/M_\odot)$ bins 8.0--9.5, 9.5--10.0, 10.0--10.5, 10.5--11.0, and 11.0--12.5 across redshift bins 0.02--0.05, 0.05--0.08, and 0.08--0.12. Quenched fractions span 0.005--0.729 and optical AGN fractions span 0.003--0.520 (2,098/4,033 in the peak mass bin). This observed target vector is a compact benchmark for simulation forward modelling, but mock-observation pipelines are still required before any model comparison can be claimed.
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Dav\'e et al.(2019)]{simba2019} Dav\'e, R., Angl\'es-Alc\'azar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
    93	\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
    94	\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
    95	\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
    96	\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
    97	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
    98	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
    99	\end{thebibliography}
   100	
   101	\end{document}

codex
I’ve got the manuscript bodies. I’m doing one last pass over the strict logs to capture every layout warning line explicitly, so the blocker list is complete rather than relying on the summary counts.
exec
/bin/zsh -lc "for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/*/aastex/*.before.strict.log; do echo '###'"'$(basename "$f"); rg -n '"'Underfull|Overfull|Undefined|LaTeX Warning: Label\\(s\\) may have changed|There were undefined citations|Citation \\(s\\) may have changed' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
###m1_rp1_sdss_agn_sfr_integrated.before.strict.log
66:Package natbib Warning: There were undefined citations.
75:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
###m1_rp2_environment_quenching_integrated.before.strict.log
64:warning: m1_rp2_environment_quenching_integrated.tex:58: Underfull \hbox (badness 1303) in paragraph at lines 57--58
65:Underfull \hbox (badness 1303) in paragraph at lines 57--58
85:Package natbib Warning: There were undefined citations.
94:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
139:warning: m1_rp2_environment_quenching_integrated.tex:58: Underfull \hbox (badness 1303) in paragraph at lines 57--58
140:Underfull \hbox (badness 1303) in paragraph at lines 57--58
###m1_rp3_maintenance_heating_integrated.before.strict.log
64:warning: m1_rp3_maintenance_heating_integrated.tex:69: Underfull \hbox (badness 1874) in paragraph at lines 68--69
65:Underfull \hbox (badness 1874) in paragraph at lines 68--69
88:warning: m1_rp3_maintenance_heating_integrated.tex:87: Overfull \vbox (12.0127pt too high) has occurred while \output is active
89:Overfull \vbox (12.0127pt too high) has occurred while \output is active
90:warning: m1_rp3_maintenance_heating_integrated.tex:88: Overfull \vbox (12.0127pt too high) has occurred while \output is active
91:Overfull \vbox (12.0127pt too high) has occurred while \output is active
94:Package natbib Warning: There were undefined citations.
103:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
148:warning: m1_rp3_maintenance_heating_integrated.tex:69: Underfull \hbox (badness 1874) in paragraph at lines 68--69
149:Underfull \hbox (badness 1874) in paragraph at lines 68--69
###m2_p1_outflow_escape_recycling_integrated.before.strict.log
85:warning: m2_p1_outflow_escape_recycling_integrated.tex:87: Overfull \vbox (9.72002pt too high) has occurred while \output is active
86:Overfull \vbox (9.72002pt too high) has occurred while \output is active
87:warning: m2_p1_outflow_escape_recycling_integrated.tex:88: Overfull \vbox (9.72002pt too high) has occurred while \output is active
88:Overfull \vbox (9.72002pt too high) has occurred while \output is active
91:Package natbib Warning: There were undefined citations.
100:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
###m2_p2_radio_jet_environment_integrated.before.strict.log
81:warning: m2_p2_radio_jet_environment_integrated.tex:73: Underfull \hbox (badness 10000) in paragraph at lines 72--73
82:Underfull \hbox (badness 10000) in paragraph at lines 72--73
86:Package natbib Warning: There were undefined citations.
95:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
140:warning: m2_p2_radio_jet_environment_integrated.tex:73: Underfull \hbox (badness 10000) in paragraph at lines 72--73
141:Underfull \hbox (badness 10000) in paragraph at lines 72--73
144:warning: m2_p2_radio_jet_environment_integrated.tex:89: Overfull \vbox (4.60469pt too high) has occurred while \output is active
145:Overfull \vbox (4.60469pt too high) has occurred while \output is active
146:warning: m2_p2_radio_jet_environment_integrated.tex:90: Overfull \vbox (4.60469pt too high) has occurred while \output is active
147:Overfull \vbox (4.60469pt too high) has occurred while \output is active
###m2_p3_feedback_transition_mass_integrated.before.strict.log
64:warning: m2_p3_feedback_transition_mass_integrated.tex:58: Underfull \hbox (badness 2134) in paragraph at lines 57--58
65:Underfull \hbox (badness 2134) in paragraph at lines 57--58
96:warning: m2_p3_feedback_transition_mass_integrated.tex:78: Underfull \hbox (badness 2134) in paragraph at lines 77--78
97:Underfull \hbox (badness 2134) in paragraph at lines 77--78
101:Package natbib Warning: There were undefined citations.
110:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
155:warning: m2_p3_feedback_transition_mass_integrated.tex:58: Underfull \hbox (badness 2134) in paragraph at lines 57--58
156:Underfull \hbox (badness 2134) in paragraph at lines 57--58
159:warning: m2_p3_feedback_transition_mass_integrated.tex:78: Underfull \hbox (badness 2134) in paragraph at lines 77--78
160:Underfull \hbox (badness 2134) in paragraph at lines 77--78
163:warning: m2_p3_feedback_transition_mass_integrated.tex:87: Overfull \vbox (12.0127pt too high) has occurred while \output is active
164:Overfull \vbox (12.0127pt too high) has occurred while \output is active
165:warning: m2_p3_feedback_transition_mass_integrated.tex:88: Overfull \vbox (12.0127pt too high) has occurred while \output is active
166:Overfull \vbox (12.0127pt too high) has occurred while \output is active
###m3_p1_multiphase_census_integrated.before.strict.log
94:Package natbib Warning: There were undefined citations.
103:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
148:warning: m3_p1_multiphase_census_integrated.tex:87: Overfull \vbox (10.86168pt too high) has occurred while \output is active
149:Overfull \vbox (10.86168pt too high) has occurred while \output is active
150:warning: m3_p1_multiphase_census_integrated.tex:88: Overfull \vbox (10.86168pt too high) has occurred while \output is active
151:Overfull \vbox (10.86168pt too high) has occurred while \output is active
###m3_p2_gas_depletion_efficiency_integrated.before.strict.log
82:Package natbib Warning: There were undefined citations.
91:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
137:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
###m3_p3_simulation_validation_integrated.before.strict.log
64:warning: m3_p3_simulation_validation_integrated.tex:56: Underfull \hbox (badness 1546) in paragraph at lines 55--56
65:Underfull \hbox (badness 1546) in paragraph at lines 55--56
97:Package natbib Warning: There were undefined citations.
106:LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
151:warning: m3_p3_simulation_validation_integrated.tex:56: Underfull \hbox (badness 1546) in paragraph at lines 55--56
152:Underfull \hbox (badness 1546) in paragraph at lines 55--56

exec
/bin/zsh -lc "for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/*/aastex/*.tex; do printf '\\n### %s\\n' \""'$(basename "$f")"; rg -n '"'abstract|title\\{|section\\{Conclusion\\}|section\\{Interpretation and missing observables\\}|section\\{Data Availability\\}|caption\\{' \""'$f"; done' in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:

### m1_rp1_sdss_agn_sfr_integrated.tex
4:\shorttitle{SDSS optical AGN/sSFR matched-control pilot}
8:\title{Optical AGN Hosts and Catalog Specific Star Formation in SDSS DR17: a Selection-Aware Matched-Control Pilot}
14:\begin{abstract}
16:\end{abstract}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
65:\caption{BPT line-ratio diagram for the cached SDSS DR17 optical emission-line subset used in the RP-1 analysis. This figure documents the optical selection and classification boundary; it does not by itself identify causal AGN feedback.}
72:\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset, $\Delta\log {\rm sSFR}=-1.309$ dex, is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
77:\section{Data Availability}\label{sec:data-avail}
80:\section{Conclusion}\label{sec:conclusion}

### m1_rp2_environment_quenching_integrated.tex
4:\shorttitle{SDSS density proxy for environmental quenching}
8:\title{SDSS density proxy for environmental quenching}
14:\begin{abstract}
16:\end{abstract}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
63:\caption{SDSS DR17 optical density-proxy diagnostic for environmental quenching. The figure summarizes the equal-count density-quartile split, where the high-density quartile reaches a quenched fraction of 0.230 $\pm$ 0.003, establishing the baseline for future group-catalog analyses.}
67:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}

### m1_rp3_maintenance_heating_integrated.tex
4:\shorttitle{Optical-AGN denominator for maintenance-heating follow-up}
8:\title{Optical-AGN denominator for maintenance-heating follow-up}
14:\begin{abstract}
16:\end{abstract}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for maintenance-heating follow-up. The figure highlights that among massive, low-sSFR objects, the BPT-AGN fraction is 0.607, providing a duty-cycle denominator for future X-ray/radio studies.}
67:\section{Interpretation and missing observables}\label{sec:missing}
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}

### m2_p1_outflow_escape_recycling_integrated.tex
4:\shorttitle{SDSS BPT-selected optical AGN denominator for outflow escape tests}
8:\title{SDSS BPT-selected optical AGN denominator for outflow escape tests}
14:\begin{abstract}
16:\end{abstract}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for outflow escape-versus-recycling follow-up. The figure summarizes the 4,440-object BPT-selected denominator and the associated median $\log {\rm sSFR} = -11.53$ used for target definition.}
67:\section{Interpretation and missing observables}\label{sec:missing}
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}

### m2_p2_radio_jet_environment_integrated.tex
4:\shorttitle{Environment proxy for optical AGN in massive SDSS hosts}
8:\title{Environment proxy for optical AGN in massive SDSS hosts}
14:\begin{abstract}
16:\end{abstract}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for radio-jet environment follow-up. The figure demonstrates the environment-stratified target set, with the optical AGN fraction rising to 0.509 $\pm$ 0.012 in the high-density quartile of massive hosts.}
67:\section{Interpretation and missing observables}\label{sec:missing}
75:\section{Data Availability}\label{sec:data-avail}
78:\section{Conclusion}\label{sec:conclusion}

### m2_p3_feedback_transition_mass_integrated.tex
4:\shorttitle{SDSS mass transition in quenching and optical AGN incidence}
8:\title{SDSS mass transition in quenching and optical AGN incidence}
14:\begin{abstract}
16:\end{abstract}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-transition mass vector. The figure shows the high-mass tail ($\log(M_\star/M_\odot)>11.0$) where the quenched fraction exceeds 0.5 and the optical AGN fraction peaks at 0.520 (2,098/4,033).}
67:\section{Interpretation and missing observables}\label{sec:missing}
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}

### m3_p1_multiphase_census_integrated.tex
4:\shorttitle{Common-denominator optical tracer census in SDSS}
8:\title{Common-denominator optical tracer census in SDSS}
14:\begin{abstract}
16:\end{abstract}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for the common-denominator multiphase census. The figure illustrates how the BPT AGN and red+emission definitions yield AGN candidate prevalence ranging from 0.136 for BPT AGN to 0.418 for red+emission within the same denominator.}
67:\section{Interpretation and missing observables}\label{sec:missing}
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}

### m3_p2_gas_depletion_efficiency_integrated.tex
4:\shorttitle{Optical denominator for gas-fraction versus efficiency tests}
8:\title{Optical denominator for gas-fraction versus efficiency tests}
14:\begin{abstract}
16:\end{abstract}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities, ending with the paper-specific downstream subset.\label{tab:selection-cascade}}
66:\caption{SDSS DR17 optical denominator/proxy diagnostic for the gas-fraction versus efficiency transition vector. The figure isolates the 6,729 massive quenched or transitioning galaxies, revealing an optical BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729).}
70:\section{Interpretation and missing observables}\label{sec:missing}
76:\section{Data Availability}\label{sec:data-avail}
79:\section{Conclusion}\label{sec:conclusion}

### m3_p3_simulation_validation_integrated.tex
4:\shorttitle{SDSS target vector for feedback-model validation}
8:\title{SDSS target vector for feedback-model validation}
14:\begin{abstract}
16:\end{abstract}
30:\tablecaption{Shared SDSS DR17 selection cascade used before paper-specific quantities.\label{tab:selection-cascade}}
63:\caption{SDSS DR17 optical denominator/proxy diagnostic for the feedback-model validation target vector. The figure maps quenched fractions and optical AGN incidence across 15 mass-redshift cells for simulation forward-modeling, spanning $\log(M_\star/M_\odot)$ bins 8.0--9.5 through 11.0--12.5 and redshift bins 0.02--0.05 through 0.08--0.12.}
67:\section{Interpretation and missing observables}\label{sec:missing}
73:\section{Data Availability}\label{sec:data-avail}
76:\section{Conclusion}\label{sec:conclusion}

codex
The remaining strict issues are concentrated at the ends of a few manuscripts. I’m checking the closing blocks now because the vertical overflow warnings usually map to bibliography/acknowledgments layout, which is the kind of thing that blocks a clean AAS build.
exec
/bin/zsh -lc "for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/{03_m1_rp3_maintenance_heating,04_m2_p1_outflow_escape_recycling,05_m2_p2_radio_jet_environment,06_m2_p3_feedback_transition_mass,07_m3_p1_multiphase_census}/aastex/*_integrated.tex; do echo '###'"'$(basename "$f"); nl -ba "$f" | sed -n '"'78,110p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
###m1_rp3_maintenance_heating_integrated.tex
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    93	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
    94	\bibitem[Heckman \& Best(2014)]{heckmanbest2014} Heckman, T.~M., \& Best, P.~N. 2014, ARA\&A, 52, 589
    95	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    96	\bibitem[McNamara \& Nulsen(2012)]{mcnamara2012} McNamara, B.~R., \& Nulsen, P.~E.~J. 2012, New J. Phys., 14, 055023
    97	\end{thebibliography}
    98	
    99	\end{document}
###m2_p1_outflow_escape_recycling_integrated.tex
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Carniani et al.(2017)]{carniani2017} Carniani, S., Marconi, A., Maiolino, R., et al. 2017, A\&A, 605, A42
    93	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    94	\bibitem[Fabian(2012)]{fabian2012} Fabian, A.~C. 2012, ARA\&A, 50, 455
    95	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    96	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    97	\end{thebibliography}
    98	
    99	\end{document}
###m2_p2_radio_jet_environment_integrated.tex
    78	\section{Conclusion}\label{sec:conclusion}
    79	Among massive hosts, the optical AGN fraction is 0.509 $\pm$ 0.012 in the high-density quartile and 0.367 $\pm$ 0.012 in the low-density quartile, with a bootstrap difference of [0.112, 0.170]. This establishes an environment-stratified optical denominator for radio-jet coupling studies, not a direct coupling measurement.
    80	
    81	\begin{acknowledgments}
    82	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    83	\end{acknowledgments}
    84	
    85	
    86	\begin{thebibliography}{}
    87	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    88	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    89	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    90	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    91	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    92	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    93	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    94	\bibitem[Best et al.(2005)]{best2005} Best, P.~N., Kauffmann, G., Heckman, T.~M., et al. 2005, MNRAS, 362, 25
    95	\bibitem[Eckert et al.(2024)]{eckert2024} Eckert, D., Gastaldello, F., O'Sullivan, E., et al. 2024, Galaxies, 12(3), 24
    96	\bibitem[McNamara \& Nulsen(2007)]{mcnamara2007} McNamara, B.~R., \& Nulsen, P.~E.~J. 2007, ARA\&A, 45, 117
    97	\bibitem[Santoro et al.(2020)]{santoro2020} Santoro, F., Tadhunter, C., Baron, D., Morganti, R., \& Holt, J. 2020, A\&A, 644, A54
    98	\end{thebibliography}
    99	
   100	\end{document}
###m2_p3_feedback_transition_mass_integrated.tex
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Baldry et al.(2004)]{baldry2004} Baldry, I.~K., Glazebrook, K., Brinkmann, J., et al. 2004, ApJ, 600, 681
    93	\bibitem[Kauffmann et al.(2003b)]{kauffmann2003mass} Kauffmann, G., Heckman, T.~M., White, S.~D.~M., et al. 2003b, MNRAS, 341, 33
    94	\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108
    95	\bibitem[Dekel \& Birnboim(2006)]{dekel2006} Dekel, A., \& Birnboim, Y. 2006, MNRAS, 368, 2
    96	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    97	\bibitem[Peng et al.(2012)]{peng2012} Peng, Y.-j., Lilly, S.~J., Renzini, A., \& Carollo, M. 2012, ApJ, 757, 4
    98	\bibitem[Piotrowska et al.(2022)]{piotrowska2022} Piotrowska, J.~M., Bluck, A.~F.~L., Maiolino, R., \& Peng, Y.-j. 2022, MNRAS, 512, 1052
    99	\end{thebibliography}
   100	
   101	\end{document}
###m3_p1_multiphase_census_integrated.tex
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Bae \& Woo(2018)]{bae2018} Bae, H.-J., \& Woo, J.-H. 2018, ApJ, 853, 185
    93	\bibitem[Cicone et al.(2014)]{cicone2014} Cicone, C., Maiolino, R., Sturm, E., et al. 2014, A\&A, 562, A21
    94	\bibitem[Feruglio et al.(2015)]{feruglio2015} Feruglio, C., Fiore, F., Carniani, S., et al. 2015, A\&A, 583, A99
    95	\bibitem[Fiore et al.(2017)]{fiore2017} Fiore, F., Feruglio, C., Shankar, F., et al. 2017, A\&A, 601, A143
    96	\bibitem[Rupke(2018)]{rupke2018} Rupke, D.~S.~N. 2018, Galaxies, 6, 138
    97	\bibitem[Veilleux et al.(2005)]{veilleux2005} Veilleux, S., Cecil, G., \& Bland-Hawthorn, J. 2005, ARA\&A, 43, 769
    98	\bibitem[Woo et al.(2016)]{woo2016} Woo, J.-H., Bae, H.-J., Son, D., \& Karouzos, M. 2016, ApJ, 817, 108
    99	\end{thebibliography}
   100	
   101	\end{document}

exec
/bin/zsh -lc "for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/{01_m1_rp1_sdss_agn_sfr,02_m1_rp2_environment_quenching,08_m3_p2_gas_depletion_efficiency,09_m3_p3_simulation_validation}/aastex/*_integrated.tex; do echo '###'"'$(basename "$f"); nl -ba "$f" | sed -n '"'78,108p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
###m1_rp1_sdss_agn_sfr_integrated.tex
    78	The SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog quantities used here are publicly available through the SDSS data releases and associated catalog papers cited below. A local subset and manifest are retained in the project repository for reproducibility and are available from the corresponding author upon reasonable request.
    79	
    80	\section{Conclusion}\label{sec:conclusion}
    81	In the capped SDSS DR17 emission-line subset, broad BPT optical AGN hosts show a median sSFR offset of $-1.309$ dex relative to mass--redshift matched controls, with a 95\% bootstrap interval of $[-1.334,-1.282]$ dex. Although the offset amplitude is highly dependent on the emission-line selection function (decreasing to $-0.744$ dex at S/N$\geq 10$), the interval remains securely negative. These measurements establish a robust optical association baseline, which will require future molecular gas or direct outflow kinematics follow-up to isolate any causal AGN quenching mechanisms.
    82	
    83	\begin{acknowledgments}
    84	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    85	\end{acknowledgments}
    86	
    87	
    88	\begin{thebibliography}{}
    89	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    90	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    91	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    92	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    93	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    94	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    95	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    96	
    97	\end{thebibliography}
    98	
    99	\end{document}
###m1_rp2_environment_quenching_integrated.tex
    78	\section{Conclusion}\label{sec:conclusion}
    79	The SDSS-only proxy shows a high-density quenched fraction of 0.230 $\pm$ 0.003 versus 0.181 $\pm$ 0.003 in the low-density quartile, with a mass- and redshift-adjusted high-density coefficient of $0.032 \pm 0.004$. These values define an optical environmental baseline, but a full quenching interpretation still requires group catalogs, halo masses, and central/satellite labels.
    80	
    81	\begin{acknowledgments}
    82	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    83	\end{acknowledgments}
    84	
    85	
    86	\begin{thebibliography}{}
    87	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    88	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    89	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    90	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    91	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    92	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    93	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    94	\bibitem[Baldry et al.(2006)]{baldry2006} Baldry, I.~K., Balogh, M.~L., Bower, R.~G., et al. 2006, MNRAS, 373, 469
    95	\bibitem[Goubert et al.(2024)]{goubert2024} Goubert, P.~H., Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2024, MNRAS, 528, 3822
    96	\bibitem[Peng et al.(2010)]{peng2010} Peng, Y.-j., Lilly, S.~J., Kovac, K., et al. 2010, ApJ, 721, 193
    97	\bibitem[Wetzel et al.(2013)]{wetzel2013} Wetzel, A.~R., Tinker, J.~L., Conroy, C., \& van den Bosch, F.~C. 2013, MNRAS, 432, 336
    98	\end{thebibliography}
    99	
   100	\end{document}
###m3_p2_gas_depletion_efficiency_integrated.tex
    78	
    79	\section{Conclusion}\label{sec:conclusion}
    80	We have mapped the optical baseline for 6,729 massive quenched or transitioning galaxies in the SDSS emission-line sample. We find a BPT AGN fraction of $0.549 \pm 0.006$ (3,692/6,729) and a median H$\alpha$ luminosity proxy of $\log(L_{\mathrm{H}\alpha} / \mathrm{erg~s}^{-1}) = 40.06$, approximately 0.66 dex lower than star-forming counterparts. While these quantities define the target selection denominator for future CO gas-fraction versus efficiency programs, direct molecular gas masses and aperture-matched star formation rates remain required to physically distinguish depletion from low efficiency.
    81	
    82	\begin{acknowledgments}
    83	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    84	\end{acknowledgments}
    85	
    86	
    87	\begin{thebibliography}{}
    88	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    89	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    90	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    91	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    92	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    93	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    94	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    95	\bibitem[Catinella et al.(2018)]{xgass2018} Catinella, B., Saintonge, A., Janowiecki, S., et al. 2018, MNRAS, 476, 875
    96	\bibitem[Saintonge et al.(2011a)]{coldgass1} Saintonge, A., Kauffmann, G., Kramer, C., et al. 2011a, MNRAS, 415, 32
    97	\bibitem[Saintonge et al.(2011b)]{coldgass2} Saintonge, A., Kauffmann, G., Wang, J., et al. 2011b, MNRAS, 415, 61
    98	\bibitem[Saintonge et al.(2017)]{xcoldgass2017} Saintonge, A., Catinella, B., Tacconi, L.~J., et al. 2017, ApJS, 233, 22
    99	\end{thebibliography}
   100	
   101	\end{document}
###m3_p3_simulation_validation_integrated.tex
    78	
    79	\begin{acknowledgments}
    80	We thank the SDSS collaboration. This manuscript uses public SDSS DR17 data only.
    81	\end{acknowledgments}
    82	
    83	
    84	\begin{thebibliography}{}
    85	\bibitem[Abdurro'uf et al.(2022)]{sdssdr17} Abdurro'uf, Accetta, K., Aerts, C., et al. 2022, ApJS, 259, 35
    86	\bibitem[Baldwin et al.(1981)]{baldwin1981} Baldwin, J.~A., Phillips, M.~M., \& Terlevich, R. 1981, PASP, 93, 5
    87	\bibitem[Brinchmann et al.(2004)]{brinchmann2004} Brinchmann, J., Charlot, S., White, S.~D.~M., et al. 2004, MNRAS, 351, 1151
    88	\bibitem[Kauffmann et al.(2003a)]{kauffmann2003bpt} Kauffmann, G., Heckman, T.~M., Tremonti, C., et al. 2003a, MNRAS, 346, 1055
    89	\bibitem[Kewley et al.(2001)]{kewley2001} Kewley, L.~J., Dopita, M.~A., Sutherland, R.~S., Heisler, C.~A., \& Trevena, J. 2001, ApJ, 556, 121
    90	\bibitem[Kewley et al.(2006)]{kewley2006} Kewley, L.~J., Groves, B., Kauffmann, G., \& Heckman, T. 2006, MNRAS, 372, 961
    91	\bibitem[York et al.(2000)]{york2000} York, D.~G., Adelman, J., Anderson, J.~E., Jr., et al. 2000, AJ, 120, 1579
    92	\bibitem[Dav\'e et al.(2019)]{simba2019} Dav\'e, R., Angl\'es-Alc\'azar, D., Narayanan, D., et al. 2019, MNRAS, 486, 2827
    93	\bibitem[Donnari et al.(2021)]{donnari2021} Donnari, M., Pillepich, A., Nelson, D., et al. 2021, MNRAS, 506, 4760
    94	\bibitem[Dubois et al.(2013)]{dubois2013} Dubois, Y., Gavazzi, R., Peirani, S., \& Silk, J. 2013, MNRAS, 433, 3297
    95	\bibitem[Dubois et al.(2016)]{dubois2016} Dubois, Y., Peirani, S., Pichon, C., et al. 2016, MNRAS, 463, 3948
    96	\bibitem[Nanni et al.(2023)]{imanga2023} Nanni, L., Thomas, D., Trayford, J., et al. 2023, MNRAS, 518, 2605
    97	\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., Pillepich, A., et al. 2019, Computational Astrophysics and Cosmology, 6, 2
    98	\bibitem[Schaye et al.(2015)]{eagle2015} Schaye, J., Crain, R.~A., Bower, R.~G., et al. 2015, MNRAS, 446, 521
    99	\end{thebibliography}
   100	
   101	\end{document}

codex
I’ve confirmed the bibliography items are in each TeX file, so the remaining citation warnings are about unresolved build state rather than absent `\bibitem`s. I’m checking whether there are any true `??`/missing-reference errors hidden behind the natbib noise.
exec
/bin/zsh -lc "for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/*/aastex/*.before.strict.log; do echo '###'"'$(basename "$f"); rg -n '"'\\\\(??|undefined references|Reference|Citation)' \""'$f" | sed -n '"'1,60p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
###m1_rp1_sdss_agn_sfr_integrated.before.strict.log
rg: regex parse error:
    (?:\\(??|undefined references|Reference|Citation))
           ^
error: unrecognized flag
###m1_rp2_environment_quenching_integrated.before.strict.log
rg: regex parse error:
    (?:\\(??|undefined references|Reference|Citation))
           ^
error: unrecognized flag
###m1_rp3_maintenance_heating_integrated.before.strict.log
rg: regex parse error:
    (?:\\(??|undefined references|Reference|Citation))
           ^
error: unrecognized flag
###m2_p1_outflow_escape_recycling_integrated.before.strict.log
rg: regex parse error:
    (?:\\(??|undefined references|Reference|Citation))
           ^
error: unrecognized flag
###m2_p2_radio_jet_environment_integrated.before.strict.log
rg: regex parse error:
    (?:\\(??|undefined references|Reference|Citation))
           ^
error: unrecognized flag
###m2_p3_feedback_transition_mass_integrated.before.strict.log
rg: regex parse error:
    (?:\\(??|undefined references|Reference|Citation))
           ^
error: unrecognized flag
###m3_p1_multiphase_census_integrated.before.strict.log
rg: regex parse error:
    (?:\\(??|undefined references|Reference|Citation))
           ^
error: unrecognized flag
###m3_p2_gas_depletion_efficiency_integrated.before.strict.log
rg: regex parse error:
    (?:\\(??|undefined references|Reference|Citation))
           ^
error: unrecognized flag
###m3_p3_simulation_validation_integrated.before.strict.log
rg: regex parse error:
    (?:\\(??|undefined references|Reference|Citation))
           ^
error: unrecognized flag

exec
/bin/zsh -lc "for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/*/data/source_analysis_results.json; do echo '###'"'$(basename "$f"); sed -n '"'1,220p' \""'$f" | sed -n '"'1,80p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
###source_analysis_results.json
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
}###source_analysis_results.json
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
}###source_analysis_results.json
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
}###source_analysis_results.json
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
}###source_analysis_results.json
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
}###source_analysis_results.json
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
}###source_analysis_results.json
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
}###source_analysis_results.json
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
}###source_analysis_results.json
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

codex
I haven’t seen missing-graphic failures, but I’m confirming that explicitly so the report can say “none observed” instead of leaving that implicit.
exec
/bin/zsh -lc "for f in /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/*/aastex/*.before.strict.log; do echo '###'"'$(basename "$f"); rg -n '"'not found|No file|missing|undefined reference|Figure|graphics' \""'$f" | sed -n '"'1,40p'; done" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
###m1_rp1_sdss_agn_sfr_integrated.before.strict.log
15:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
16:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
28:No file m1_rp1_sdss_agn_sfr_integrated.aux.
101:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
102:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
###m1_rp2_environment_quenching_integrated.before.strict.log
15:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
16:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
28:No file m1_rp2_environment_quenching_integrated.aux.
121:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
122:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
###m1_rp3_maintenance_heating_integrated.before.strict.log
15:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
16:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
28:No file m1_rp3_maintenance_heating_integrated.aux.
130:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
131:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
###m2_p1_outflow_escape_recycling_integrated.before.strict.log
15:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
16:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
28:No file m2_p1_outflow_escape_recycling_integrated.aux.
127:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
128:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
###m2_p2_radio_jet_environment_integrated.before.strict.log
15:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
16:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
28:No file m2_p2_radio_jet_environment_integrated.aux.
122:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
123:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
###m2_p3_feedback_transition_mass_integrated.before.strict.log
15:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
16:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
28:No file m2_p3_feedback_transition_mass_integrated.aux.
137:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
138:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
###m3_p1_multiphase_census_integrated.before.strict.log
15:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
16:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
28:No file m3_p1_multiphase_census_integrated.aux.
130:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
131:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
###m3_p2_gas_depletion_efficiency_integrated.before.strict.log
15:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
16:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
28:No file m3_p2_gas_depletion_efficiency_integrated.aux.
118:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
119:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
###m3_p3_simulation_validation_integrated.before.strict.log
15:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
16:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty
28:No file m3_p3_simulation_validation_integrated.aux.
133:(revsymb4-1.sty)) (latexsym.sty) (graphicx.sty (keyval.sty) (graphics.sty
134:(trig.sty) (graphics.cfg) (xetex.def))) (amssymb.sty (amsfonts.sty)) (epsf.sty

codex
**LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_02 status:** ISSUES_FOUND

**Files/paths inspected**
- Audit manifest: [CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.json)
- Audit notes: [CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.md)
- Candidate TeX sources inspected:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)
- Strict logs inspected:
  - `*.before.strict.log` for all nine manuscripts under the same candidate tree
- Supporting data inspected:
  - `data/source_analysis_results.json` for all nine manuscripts

**Strict LaTeX blockers**
- Global: all nine manuscripts fail the strict cleanliness gate (`build_ok=false`, `clean_ok=false`) because natbib still reports unresolved citations after the audit rerun. I did not find fatal TeX errors or missing-graphic failures.
- No missing figures observed: every `\includegraphics{../figures/...}` target exists in the candidate package, and the logs did not show `File not found` errors.

Per file:
- [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex): 17 undefined citations; no layout warnings. Log examples include `sdssdr17`, `brinchmann2004`, `york2000`, `baldwin1981`, `kewley2001`, `kauffmann2003bpt`, `kewley2006`.
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex): 25 undefined citations; `Underfull \hbox` at lines 57--58. Same citation set as above plus `peng2010`, `baldry2006`, `wetzel2013`, `goubert2024`.
- [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex): 27 undefined citations; `Underfull \hbox` at lines 68--69; `Overfull \vbox` at lines 87--88.
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex): 27 undefined citations; `Overfull \vbox` at lines 87--88.
- [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex): 25 undefined citations; `Underfull \hbox` at lines 72--73; `Overfull \vbox` at lines 89--90.
- [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex): 31 undefined citations; `Underfull \hbox` at lines 57--58 and 77--78; `Overfull \vbox` at lines 87--88.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex): 31 undefined citations; `Overfull \vbox` at lines 87--88.
- [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex): 25 undefined citations; no layout warnings recorded.
- [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex): 31 undefined citations; `Underfull \hbox` at lines 55--56.

**Publishability blockers**
- The manuscripts are mostly cautious already, but a few titles and closing statements still read more like physical-results papers than optical-denominator papers.
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex): title and abstract still foreground “environmental quenching” from a nearest-neighbor density proxy. That is probably acceptable only if the baseline/association framing stays explicit in the title, abstract, and conclusion.
- [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex): “maintenance-heating follow-up” is okay, but the title and figure caption still imply a process-level program rather than a denominator. Keep the causal claim entirely in future-work language.
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex): “outflow escape tests” is too strong for SDSS-only optical selection. The text already says it is not an escape-velocity measurement; the title and caption should mirror that restraint.
- [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex): the paper is still phrased as if it is about radio-jet coupling, but it only measures an optical/environment baseline. Keep the title/caption anchored on the denominator.
- [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex): the observed rise in quenched fraction and AGN incidence is real, but “feedback-transition” language should stay explicitly conditional. The conclusion is safer than the title.
- [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex): this is close, but the reader-facing framing should keep “observed target vector” and “mock-observation pipelines required” prominent so it does not read like an actual simulation comparison.

**Exact feed for the writer**
- Preserve all measured values exactly; do not alter sample sizes, fractions, intervals, or offsets.
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex): split the long result sentence at line 57 into two shorter sentences; keep the `0.230`, `0.181`, and `[0.041,0.059]` values unchanged. If needed, make the figure caption at line 63 more neutral by describing the proxy and split, not the inference.
- [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex): shorten/split the line 70 caveat sentence and trim the final-page text enough to remove the `Overfull \vbox` at lines 87--88. Keep `9,298`, `5,695`, `0.430`, and `0.607` unchanged.
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex): rephrase the title/caption/conclusion so the manuscript is explicitly a follow-up denominator, not an “escape test.” Keep `4,440/60,000` and `-11.53` unchanged.
- [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex): split the long caveat sentence at lines 72--73 to remove the `Underfull \hbox`; soften the caption so it describes the environment-stratified optical target set rather than implying coupling measurement.
- [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex): split the long result sentence at lines 57--58 and the caveat sentence at lines 77--78; keep the title/caption aligned with “optical transition diagnostic” rather than “feedback transition” as a physical claim.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex): reduce the final-page vertical pressure at lines 87--88 by shortening the last paragraph or moving one bibliographic sentence earlier. Keep the prevalence values unchanged.
- [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex): this one is structurally closest; no layout warning showed up in the strict log. Keep the title and conclusion as “optical baseline / future CO follow-up,” not a direct gas-efficiency result.
- [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex): split the long line-55/56 paragraph to remove the `Underfull \hbox`; keep the phrase “observed target vector” and the mock-observation caveat explicit before any model-comparison language.

**Safety ledger**
- No edits made.
- No public PDF replacement.
- No database, SQL, `/api/pages`, page-version, wiki-publish, or trust-recompute actions.
- No deploy/restart.
- No git commit/push/merge/rebase/history rewrite.
- No cron changes.
- No billing/cloud/OAuth/API-key/account changes.
- No credential/token/cookie reads.
- No external manuscript submission.
tokens used
84,879
**LATEX_REPAIR_CODEX_KUN_TEX_REPRO_CYCLE_02 status:** ISSUES_FOUND

**Files/paths inspected**
- Audit manifest: [CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.json](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.json)
- Audit notes: [CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.md](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/CYCLE_02_BEFORE_STRICT_LATEX_AUDIT.md)
- Candidate TeX sources inspected:
  - [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex)
  - [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex)
  - [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex)
  - [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex)
  - [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex)
  - [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex)
  - [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex)
  - [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex)
  - [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex)
- Strict logs inspected:
  - `*.before.strict.log` for all nine manuscripts under the same candidate tree
- Supporting data inspected:
  - `data/source_analysis_results.json` for all nine manuscripts

**Strict LaTeX blockers**
- Global: all nine manuscripts fail the strict cleanliness gate (`build_ok=false`, `clean_ok=false`) because natbib still reports unresolved citations after the audit rerun. I did not find fatal TeX errors or missing-graphic failures.
- No missing figures observed: every `\includegraphics{../figures/...}` target exists in the candidate package, and the logs did not show `File not found` errors.

Per file:
- [m1_rp1_sdss_agn_sfr_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex): 17 undefined citations; no layout warnings. Log examples include `sdssdr17`, `brinchmann2004`, `york2000`, `baldwin1981`, `kewley2001`, `kauffmann2003bpt`, `kewley2006`.
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex): 25 undefined citations; `Underfull \hbox` at lines 57--58. Same citation set as above plus `peng2010`, `baldry2006`, `wetzel2013`, `goubert2024`.
- [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex): 27 undefined citations; `Underfull \hbox` at lines 68--69; `Overfull \vbox` at lines 87--88.
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex): 27 undefined citations; `Overfull \vbox` at lines 87--88.
- [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex): 25 undefined citations; `Underfull \hbox` at lines 72--73; `Overfull \vbox` at lines 89--90.
- [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex): 31 undefined citations; `Underfull \hbox` at lines 57--58 and 77--78; `Overfull \vbox` at lines 87--88.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex): 31 undefined citations; `Overfull \vbox` at lines 87--88.
- [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex): 25 undefined citations; no layout warnings recorded.
- [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex): 31 undefined citations; `Underfull \hbox` at lines 55--56.

**Publishability blockers**
- The manuscripts are mostly cautious already, but a few titles and closing statements still read more like physical-results papers than optical-denominator papers.
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex): title and abstract still foreground “environmental quenching” from a nearest-neighbor density proxy. That is probably acceptable only if the baseline/association framing stays explicit in the title, abstract, and conclusion.
- [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex): “maintenance-heating follow-up” is okay, but the title and figure caption still imply a process-level program rather than a denominator. Keep the causal claim entirely in future-work language.
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex): “outflow escape tests” is too strong for SDSS-only optical selection. The text already says it is not an escape-velocity measurement; the title and caption should mirror that restraint.
- [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex): the paper is still phrased as if it is about radio-jet coupling, but it only measures an optical/environment baseline. Keep the title/caption anchored on the denominator.
- [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex): the observed rise in quenched fraction and AGN incidence is real, but “feedback-transition” language should stay explicitly conditional. The conclusion is safer than the title.
- [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex): this is close, but the reader-facing framing should keep “observed target vector” and “mock-observation pipelines required” prominent so it does not read like an actual simulation comparison.

**Exact feed for the writer**
- Preserve all measured values exactly; do not alter sample sizes, fractions, intervals, or offsets.
- [m1_rp2_environment_quenching_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex): split the long result sentence at line 57 into two shorter sentences; keep the `0.230`, `0.181`, and `[0.041,0.059]` values unchanged. If needed, make the figure caption at line 63 more neutral by describing the proxy and split, not the inference.
- [m1_rp3_maintenance_heating_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/03_m1_rp3_maintenance_heating/aastex/m1_rp3_maintenance_heating_integrated.tex): shorten/split the line 70 caveat sentence and trim the final-page text enough to remove the `Overfull \vbox` at lines 87--88. Keep `9,298`, `5,695`, `0.430`, and `0.607` unchanged.
- [m2_p1_outflow_escape_recycling_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/04_m2_p1_outflow_escape_recycling/aastex/m2_p1_outflow_escape_recycling_integrated.tex): rephrase the title/caption/conclusion so the manuscript is explicitly a follow-up denominator, not an “escape test.” Keep `4,440/60,000` and `-11.53` unchanged.
- [m2_p2_radio_jet_environment_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/05_m2_p2_radio_jet_environment/aastex/m2_p2_radio_jet_environment_integrated.tex): split the long caveat sentence at lines 72--73 to remove the `Underfull \hbox`; soften the caption so it describes the environment-stratified optical target set rather than implying coupling measurement.
- [m2_p3_feedback_transition_mass_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/06_m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_integrated.tex): split the long result sentence at lines 57--58 and the caveat sentence at lines 77--78; keep the title/caption aligned with “optical transition diagnostic” rather than “feedback transition” as a physical claim.
- [m3_p1_multiphase_census_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/07_m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_integrated.tex): reduce the final-page vertical pressure at lines 87--88 by shortening the last paragraph or moving one bibliographic sentence earlier. Keep the prevalence values unchanged.
- [m3_p2_gas_depletion_efficiency_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/08_m3_p2_gas_depletion_efficiency/aastex/m3_p2_gas_depletion_efficiency_integrated.tex): this one is structurally closest; no layout warning showed up in the strict log. Keep the title and conclusion as “optical baseline / future CO follow-up,” not a direct gas-efficiency result.
- [m3_p3_simulation_validation_integrated.tex](/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/latex-publishability-repair/LATEX_PUBLISHABILITY_REPAIR_20260709T235447Z/candidates/cycle_02_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex): split the long line-55/56 paragraph to remove the `Underfull \hbox`; keep the phrase “observed target vector” and the mock-observation caveat explicit before any model-comparison language.

**Safety ledger**
- No edits made.
- No public PDF replacement.
- No database, SQL, `/api/pages`, page-version, wiki-publish, or trust-recompute actions.
- No deploy/restart.
- No git commit/push/merge/rebase/history rewrite.
- No cron changes.
- No billing/cloud/OAuth/API-key/account changes.
- No credential/token/cookie reads.
- No external manuscript submission.

```

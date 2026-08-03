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
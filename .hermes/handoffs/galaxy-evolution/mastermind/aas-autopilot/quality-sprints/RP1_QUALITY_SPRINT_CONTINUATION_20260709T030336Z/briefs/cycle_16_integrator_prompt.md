You are the Tori/Codex local manuscript integrator for quality cycle 16.

You may edit ONLY these candidate-copy TeX files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex

You may also write a concise Markdown response here:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/CYCLE_16_REVIEW_RESPONSE.md

Forbidden:
- Do not edit the original source package outside this candidate root.
- Do not edit public pages, live roots, DB/API/wiki/trust/deploy/git/cron/billing/OAuth/account settings, or external submission systems.
- Do not change numeric results, table numbers, figure paths, or core claims.
- Do not invent new data or new citations.
- Do not turn denominator/proxy notes into causal physical-feedback claims.

Allowed and desired:
- Apply safe wording improvements from the review reports.
- Improve abstract/intro/conclusion clarity.
- Strengthen association-only and capped-cache caveats.
- Make the supplement read like a coherent atlas rather than eight papers.
- Clarify citation-role separation: SDSS/BPT/catalog for actual methods; radio/X-ray/CO/HI/outflow/simulation papers as future-data motivation.
- Keep TeX compilable.
- Write CYCLE_16_REVIEW_RESPONSE.md summarizing exactly what you changed and what you refused as needing new data.

Review reports follow.


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/hwao/HWAO_QUALITY_REVIEW_CYCLE_16.md =====
# hwao-agy-cycle-16
Started UTC: 2026-07-09T04:42:09Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_16

### Publication-Readiness Verdict

**RP-1 (Flagship): Not Yet Ready for Public Submission.** 
The scientific boundary is excellent; the text rigorously enforces the association-only, non-causal claim and correctly handles the selection bias of the fixed 60,000-galaxy cap. However, it is missing standard AAS publication requirements (Facilities/Data Availability, exact matching metric definition, and software citations). It is mathematically robust but needs structural and compliance polish.

**Supplement (Atlas): Ready as an Accompanying Local Baseline.**
The supplement is well-structured and properly positioned as an observational baseline/target vector compilation rather than eight independent papers. It requires the same AAS compliance updates as the flagship before it could be hosted publicly.

---

### Top 10 Prioritized Concrete Improvements

#### Must fix before public
1. **Data Availability and Facilities Statements (Compliance):** AAS journals strictly require a `\facilities{SDSS}` tag and a formal Data Availability or Software section. The current "Public SDSS DR17 data only" affiliation is insufficient for formal submission.
2. **Matching Metric Specification (Reproducibility):** The flagship states controls were matched in "standardized $(\log M_\star,z)$ space." The text must specify the exact metric used (e.g., Euclidean distance after variance normalization) so the 8,146 pairs can be independently reproduced.
3. **Neighbor Index Definition (Clarity):** In the supplement (Topic 3.1), explicitly define whether the "10th-neighbor index" is based on 2D projected sky separation or a 3D redshift-space distance.
4. **Software Citations (Compliance):** Add standard citations for the software stack used to generate the catalog metrics and perform the bootstrapping (e.g., Astropy, SciPy, Topcat, or relevant R/Python packages).

#### Nice local polish
5. **Abstract De-duplication (Flagship):** The flagship abstract uses the phrase "fixed-size 60,000-galaxy pilot sample" and "pilot sample" repetitively. Streamline this to state the sample size and selection limitation once clearly.
6. **Consolidate Caveats (Flagship):** The morphology, aperture-fraction, and LINER-contamination caveats are currently scattered across Sections 1, 2, 4, and 5. Grouping them into a single "Caveats and Limitations" subsection in Section 5 would improve the flow.
7. **Cross-Referencing (Supplement):** Add brief cross-references between related atlas sections. For example, explicitly link the "Maintenance-heating denominator" (3.2) with the "Radio-jet environment baseline" (3.4), as they share X-ray/radio follow-up requirements.
8. **Table 1 Caption Polish (Both):** The table captions for the selection cascades are a bit informal ("Counts are read-only public SDSS..."). Polish them to a standard descriptive academic tone.

#### Needs new data (Do not change in this cycle)
9. **Morphological and Aperture Controls:** The flagship rightly warns that the -1.309 dex offset could be driven by comparing bulge-dominated broad-BPT hosts to disk-dominated star-forming controls. Resolving this requires structural data (e.g., S\'ersic fits, bulge-to-total ratios) which is currently out of scope. 
10. **Multiphase Gas and Halo Mass Validation:** As outlined in the supplement, testing the causal nature of these baselines requires CO/HI mass fractions, X-ray cavities, and robust halo masses. Do not attempt to claim these with the current SDSS-only data.

---

### Safe Integrator Instructions

Integrator, you are authorized to make the following safe wording/section changes to the `.tex` files:
- **Add standard AAS boilerplate:** Insert `\facilities{SDSS}` and a brief "Data Availability" paragraph acknowledging the public MPA-JHU/DR17 catalog access. 
- **Specify the matching algorithm:** Update Section 3 of the flagship to briefly state the distance metric used for the $(\log M_\star,z)$ match.
- **Refine the flagship abstract:** Remove repetitive instances of "pilot sample" while retaining the strict 60,000-row selection caveat.
- **Consolidate caveats:** You may rearrange paragraphs in the flagship to create a "Caveats and Limitations" subsection, provided you **do not alter the numeric values, the bootstrap intervals, or the association-only boundary.**
- **Specify the neighbor index:** In the supplement, add a sentence defining the geometry (2D vs 3D) of the 10th-neighbor index.

**DO NOT** change the 8,146 pair count, the -1.309 dex offset, the 60,000 denominator, or remove any text stating this is an "association-only" result.

---

### Safety Ledger
- **Status:** Read-only review completed.
- **Actions Taken:** Analyzed local LaTeX source and generated prioritized quality plan.
- **Prohibited Actions Avoided:** No files were edited. No git commits made. No public pages touched. No external APIs or DBs accessed. No causal claims were introduced. Local manuscript review only.


# command_result
exit_code=0
elapsed_s=35.4
timed_out=False
finished_utc=2026-07-09T04:42:45Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/gemini_deep/GEMINI_AGY_DEEP_REVIEW_CYCLE_16.md =====
# gemini-agy-deep-cycle-16
Started UTC: 2026-07-09T04:42:09Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_16

# Deep Research Review Report: Galaxy Evolution Cycle 16

## Executive Summary
This review evaluates the polished flagship draft of **RP-1** and the accompanying **Supplementary SDSS Denominator and Proxy Atlas** (from package `RP1_FLAGSHIP_WITH_SUPPLEMENT_20260709T013510Z`). The transition from nine separate papers to one flagship paper and a unified supplementary atlas is a significant improvement in scientific integrity. However, critical vulnerabilities remain where a reader could conflate catalog-model proxy behaviors with physical galaxy evolution results. 

---

## 1. Identified Issues & Proposed Wording Changes

### Issue 1: Conflation of Catalog-derived `sSFR` Model Fit with Physical Star-Formation Rate (SFR)
* **Severity**: **Blocker**
* **Risky Sentence (Flagship - Abstract & Section 4)**: 
  * *"The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex..."*
  * *"The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the broad BPT-selected galaxies..."*
* **Scientific Risk**: For optical AGN hosts, emission lines (H$\alpha$, H$\beta$) are contaminated by AGN emission, meaning the MPA-JHU catalog `specsfr_tot_p50` values are not direct measurements of star formation. Instead, they rely heavily on stellar population model fits to the stellar continuum (e.g., $D_n4000$ break index). The reader might assume this is a direct tracer-based physical SFR offset rather than a difference in catalog model fits (which are subject to degenerate age-metallicity-dust constraints).
* **Proposed Replacement**: 
  > "The preferred matched comparison yields 8,146 pairs and a median catalog-sSFR model offset ($\Delta\log {\rm sSFR}_{\rm model}$) of -1.309 dex... We emphasize that because emission lines in active hosts are dominated by AGN excitation, these values reflect model fits to the stellar continuum (e.g., $D_n 4000$) rather than direct, dust-corrected hydrogen-recombination star-formation rates."

---

### Issue 2: Misattribution of Mass selection Artifacts as a Physical "Transition Mass"
* **Severity**: **Major**
* **Risky Sentence (Supplement - Section 3.5)**: 
  * Title: *"Stellar-mass selection diagnostic: low-sSFR and optical AGN incidence"*
  * Text: *"The first stellar-mass bin with low-sSFR fraction above 0.5 is $\log(M_\star/M_\odot) \in [11.0,12.5]$... The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass..."*
* **Scientific Risk**: Because the BPT S/N $\ge 3$ criterion requires four active emission lines, it systematically excludes truly passive, massive galaxies that lack gas. The concentration of low-sSFR active galaxies at $\log(M_\star/M_\odot) > 11.0$ is an artifact of this selection cut, which allows only the subset of passive galaxies that still have warm gas to enter the denominator. A reader could easily interpret this as a physical transition mass for individual quenching.
* **Proposed Replacement**:
  > Title: "Stellar-mass selection artifact: Denominator bias in low-sSFR and optical AGN incidence"
  > Text: "The peak in low-sSFR fraction at $\log(M_\star/M_\odot) \in [11.0, 12.5]$ is a direct selection artifact of requiring four emission lines with S/N $\ge 3$. This constraint preferentially excludes the vast majority of massive quiescent galaxies that are gas-poor, rendering this incidence a conditional selection artifact rather than a physical transition-mass scale for quenching."

---

### Issue 3: Inadequate Control for Fiber Aperture and Bulge Fraction Mismatch
* **Severity**: **Major**
* **Risky Sentence (Flagship - Abstract & Section 4)**:
  * *"If the broad-BPT targets are more bulge-dominated than the star-forming controls, the 3-arcsec fiber can inflate the observed offset through aperture/morphology mismatch..."*
* **Scientific Risk**: This is presented as a minor caveat, but it is a major systematic. Since AGN hosts are systematically more bulge-dominated than pure star-forming controls at matched mass, a 3-arcsec fiber (covering 1.2–6.5 kpc) will sample the bulge (where star formation is naturally lower) in AGN hosts, while sampling the star-forming disk in controls.
* **Proposed Replacement**:
  > "Because matching is performed only on total stellar mass and redshift, and lacks structural controls (e.g., bulge-to-total ratio, Sersic index, or fiber aperture fraction), the observed central sSFR offset of -1.309 dex is expected to be significantly inflated by morphological mismatch (disk-dominated controls vs. bulge-dominated AGN hosts) rather than active feedback."

---

### Issue 4: Ambiguous Outflow Causal Assumptions in the Supplement
* **Severity**: **Minor**
* **Risky Sentence (Supplement - Section 3.3)**:
  * *"High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median $\log {\rm sSFR}$ is -11.53, compared with -10.14 for the full denominator."*
* **Scientific Risk**: The association of high-excitation AGN with low sSFR is presented alongside citations to resolved outflows, suggesting a physical link that is unmeasured in this sample.
* **Proposed Replacement**:
  > "High-excitation optical AGN candidates within this selection-limited sample exhibit lower catalog sSFR. This statistical baseline does not identify outflows, gas kinematics, or energetic feedback; it merely flags a target list for future spatially resolved spectroscopy."

---

## 2. Citation-Role and Missing-Data Flags

### Citation-Role Correctness Review
* **Method Support vs. Future-Data Motivation**:
  * **Violator**: Citations to `veilleux2005` (outflows), `cicone2014` (molecular outflows), and `carniani2017` (ionized outflows) in the main paper and supplement must **not** be framed as supporting the current SDSS optical pipeline or validation steps. They must remain strictly partitioned under a "Future Motivation" or "Missing Physical Observables" section.
  * **Violator**: Citations to `piotrowska2022` (random forest quenching analysis) and `wetzel2013` (satellite quenching) should not be used to justify the matching method, as this matching lacks environmental variables. They must be cited only as motivation for why environment/group catalogs are missing.

### Missing-Observable Checklist
Any physical claims regarding feedback or environmental quenching in this package require the integration of:
1. **Radio Data**: High-resolution radio maps (e.g., VLA/e-MERLIN) to measure jet power, age, and extent to confirm jet-mode/maintenance heating (vs. `best2005`, `heckmanbest2014`).
2. **X-ray Data**: X-ray observations (e.g., Chandra/XMM-Newton) to confirm cooling rates, cavity powers, and hot gas halo density (vs. `fabian2012`, `mcnamara2007`).
3. **CO/HI Gas**: Spatially matched CO and HI measurements (e.g., ALMA/NOEMA, Arecibo/FAST) to calculate actual molecular gas mass and depletion times (vs. `xcoldgass2017`, `xgass2018`).
4. **Resolved Outflows**: Integral field spectroscopy (IFS, e.g., MaNGA, KCWI, MUSE) to measure spatially resolved gas kinematics and verify outflow velocities exceed escape velocity (vs. `veilleux2005`, `cicone2014`).
5. **Halo/Group Catalogs**: Friends-of-Friends or group finder catalogs (e.g., Yang et al.) to establish satellite vs. central status and measure group-scale dark matter halo mass (vs. `wetzel2013`, `peng2010`).
6. **Morphology**: Quantitative bulge-to-total ($B/T$) decompositions or Sersic profile fits to control for aperture-driven bulge-matching bias.
7. **Simulation Mocks**: Synthetic SDSS spectra generated from cosmological simulations (e.g., IllustrisTNG, EAGLE, SIMBA) passed through the identical 3-arcsec fiber and four-line S/N selection function (vs. `tng2019`, `eagle2015`, `simba2019`).

---

## 3. Ranked Integrator Actions

For the next cycle, the human/Hwao/Lana integration team should perform the following actions, ordered by priority:

1. **[Priority 1] Rename variables in tables & prose**: Update `\Delta\log {\rm sSFR}` to `\Delta\log {\rm sSFR}_{\rm catalog\_model}` throughout `rp1_flagship_polished.tex` and `supplementary_denominator_atlas.tex` to explicitly signal to readers that this is not a direct physical measurement.
2. **[Priority 2] Insert explicit selection-bias headers**: Add a dedicated subsection in both documents detailing the emission-line selection bias (preferential loss of massive quiescent galaxies due to the four-line S/N constraint).
3. **[Priority 3] Clarify citation contexts**: Group citations of physical models/simulations/non-optical datasets under a `\section{Multiwavelength Motivation (Missing Observables)}` header in the supplement rather than inline inside the target-selection notes.

---

## 4. Safety Ledger

* **Safety Status**: Approved.
* **Actions Taken**: Read-only review of `FINAL_HANDOFF.md`, `PACKAGE_AUDIT.md`, `rp1_flagship_polished.tex`, and `supplementary_denominator_atlas.tex` inside the candidate package root.
* **Write Executions**: None. No modifications to files, database, live systems, git repositories, or deployment manifests were performed.


# command_result
exit_code=0
elapsed_s=17.8
timed_out=False
finished_utc=2026-07-09T04:42:27Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_16.md =====
# codex-kun-cycle-16
Started UTC: 2026-07-09T04:42:09Z
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
session id: 019f452e-e7b2-7bf2-8910-296b5978561f
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_16.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m checking the four requested files for TeX/compile risks, figure and prose consistency, and the specific numeric guardrails you listed. First I’ll read the core manuscript and handoff docs, then I’ll verify the figures/numbers and flag any wording that could imply causal or non-association claims.
exec
/bin/zsh -lc "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.tex'" in /Users/duhokim/NebulaMind/NebulaMind
 succeeded in 0ms:
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
We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, fixed-size 60,000-galaxy pilot sample sequentially selected by \texttt{specObjID} as a computational pilot cap from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot sample rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim.

Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, indicating that the result depends on the chosen emission-line denominator and on the exclusion of LINER-like, retired, bulge-dominated hosts with weak central star formation. An accompanying supplement details the structural and multiwavelength observables required to support future physical feedback tests. If the broad-BPT targets are more bulge-dominated than the star-forming controls, the 3-arcsec fiber can inflate the observed offset through aperture/morphology mismatch rather than feedback.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a strong negative sSFR offset within the analyzed denominator. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
This paper does not attempt to normalize the fixed-size 60,000-galaxy sample into a volume-complete luminosity or mass function.


The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT-selected galaxies'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\subsection{Scope and limitations}
The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a fixed-size 60,000-galaxy pilot sample selected sequentially by \texttt{specObjID}. It is a computationally convenient, non-random subset used to establish the relative association, not a volume-limited census. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this cap is not a random sky sample and introduces survey-plate and sky-coverage bias. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the cap is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy; if broad-BPT hosts are more bulge-dominated than the star-forming controls, the central fiber measurement can inflate the observed offset relative to a global star-formation comparison.
The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade for the flagship denominator. The fixed-size 60,000-galaxy pilot sample is an artificial pilot-query cap, not a physical selection effect, and it cannot be used to derive volume-complete luminosity functions.\label{tab:selection}}
\tablehead{\colhead{Selection stage} & \colhead{Public DR17 rows} & \colhead{Cached rows} & \colhead{Retention vs. spectro-z parent}}
\startdata
SpecObj GALAXY, 0.02<z<0.12 & 501,060 & -- & 100.0\% \\
plus galSpecInfo/PhotoObj/galSpecExtra and mass/sSFR bounds & 416,554 & -- & 83.1\% \\
plus galSpecLine join & 416,554 & -- & 83.1\% \\
four BPT lines with valid flux measurements (\texttt{ivar} $> 0$) & 373,445 & 60,000 & 74.5\% \\
four BPT lines S/N>=3 & 249,917 & 60,000 & 49.9\% \\
four BPT lines S/N>=5 & 176,523 & 42,446 & 35.2\% \\
four BPT lines S/N>=10 & 91,768 & 22,311 & 18.3\% \\
\enddata
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the fixed-size-sample limitation.

\section{Classification and matching}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Here, the star-forming control pool is defined as objects below the Kauffmann et al.\ (2003) demarcation. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.
Here, ``broad optical BPT-selected'' means the inclusive optical-emission-line class under the standard BPT demarcations, while the Seyfert-like sensitivity check uses the stricter Kewley et al.\ (2006) high-excitation cut and therefore excludes LINER-like systems by construction.

\begin{figure*}
\centering
\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the SDSS DR17 analysis denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
\label{fig:bpt}
\end{figure*}

\section{Matched-control result}
The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the broad BPT-selected galaxies relative to star-forming controls.
A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison. Because the spectroscopy samples only the central 3-arcsec region (1.2--6.5 kpc here) and the match does not control morphology or aperture fraction, the -1.309 dex offset may be partially or entirely driven by comparing bulge-dominated broad-BPT hosts to disk-dominated star-forming controls. The robustness interval in Table~\ref{tab:robust} is a 95\% confidence interval on the median offset.

\begin{deluxetable*}{lrrrr}
\tabletypesize{\scriptsize}
\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
\startdata
Broad BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
Broad BPT-selected targets, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
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
Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. Within this sample, that $\sim$0.55 dex reduction is a practical estimate of how much LINER-like or retired-galaxy contamination is embedded in the broader broad-BPT denominator, rather than evidence for a different active feedback mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global star-formation suppression signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size 60,000-galaxy pilot sample. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{Conclusion}
RP-1 is best treated as a concise, selection-aware association paper, not a causal study. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
In practice, that means future work needs the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation-mock comparisons \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,piotrowska2022,wetzel2013,dekel2006}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.

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

exec
/bin/zsh -lc "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/PACKAGE_AUDIT.md'" in /Users/duhokim/NebulaMind/NebulaMind
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
/bin/zsh -lc "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/han

[TRUNCATED at 22000 chars from /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_16.md]


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/goru_mech/GORU_MECHANICAL_REPORT_CYCLE_16.md =====
# Goru mechanical report cycle 16

Marker: `GORU_MECHANICAL_REPORT_CYCLE_16`

## Counts
- flagship includegraphics: 2
- supplement includegraphics: 8
- flagship captions: 2
- supplement captions: 8
- figures found: 10

## Missing required phrases
- flagship: []
- supplement: []

## Missing numeric invariants in flagship
- []

## Suspicious claim phrase scan
- flagship: ['outflow escape', 'molecular gas depletion']
- supplement: []

## PDF receipts
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/flagship_rp1/aastex/rp1_flagship_polished.pdf exists=True bytes=255925 header=%PDF sha256=17a3f4bf24fdbaebea12f8ba446bb739c3f1cc02100bf4301fef62a922590b51
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_16_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf exists=True bytes=549439 header=%PDF sha256=976beae5b096b26f1b97676e356db43d1f33a24a31039d73cb5918e3b06e1252

## Safety
- no public pages or live roots
- no public PDF replacement
- no database, SQL, /api/pages, page_versions, wiki publish, or trust recompute
- no deploy/restart
- no git commit/push/merge/rebase
- no cron creation/update
- no billing/cloud/OAuth/API-key/account changes
- no external manuscript submission
- no credential/token/cookie reads


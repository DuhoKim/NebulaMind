You are the Tori/Codex local manuscript integrator for quality cycle 13.

You may edit ONLY these candidate-copy TeX files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex

You may also write a concise Markdown response here:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/CYCLE_13_REVIEW_RESPONSE.md

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
- Write CYCLE_13_REVIEW_RESPONSE.md summarizing exactly what you changed and what you refused as needing new data.

Review reports follow.


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/hwao/HWAO_QUALITY_REVIEW_CYCLE_13.md =====
# hwao-agy-cycle-13
Started UTC: 2026-07-09T04:22:46Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_13

### Publication-Readiness Verdict

**RP-1 Flagship:** **Conditionally Ready for Local Finalization.** The scientific boundary is excellently maintained. The paper successfully restricts itself to an association claim within a specific optical emission-line denominator, explicitly avoiding causal feedback claims. However, it requires minor wording polish to replace software-engineering terminology with standard astronomical phrasing before it is ready for public or journal submission. 

**Supplementary Atlas:** **Conditionally Ready for Local Finalization.** The framing of the 8 notes as observational baselines and denominators is highly effective and safe. Like the flagship, it requires minor terminology adjustments to read natively as an astronomical supplement rather than a software log.

---

### Top 10 Concrete Improvements

Here is the prioritized quality plan, ranked by effect on scientific quality and readability.

#### Must Fix Before Public (Safe for Integrator to Apply)
1. **Remove Software Terminology (Readability):** Replace terms like "capped 60k-row pilot cache", "row-level", and "cached rows" with astronomical equivalents such as "fixed-size pilot sample", "galaxy-by-galaxy", and "sample subset". This is critical for journal acceptance.
2. **Clarify Subclass Definitions Early (Clarity):** In RP-1 Section 3, explicitly define the difference between the general "broad BPT" classification and the stricter "Seyfert-like" and "LINER-like" demarcations (e.g., referencing Kewley vs. Kauffmann lines) so that the sensitivity checks in Table 2 and Section 5 are immediately understood.
3. **Specify Matching Ranges (Context):** In the RP-1 Abstract and Section 3, explicitly state the exact stellar mass and redshift ranges (e.g., $0.02 < z < 0.12$) used for the matched-control pairing to give the reader immediate physical context.
4. **Standardize Bullet Points (Consistency):** In the Supplement, ensure the bulleted "missing observables" lists in Sections 3.1 through 3.8 are perfectly parallel in structure and phrasing to emphasize the systematic lack of these data across all notes.

#### Nice Local Polish (Safe for Integrator to Apply)
5. **Expand LINER Contamination Discussion:** In RP-1 Section 5, smooth the transition when discussing the drop from -1.309 dex to -0.763 dex. Add a sentence explicitly stating how the exclusion of LINER-like targets by the Seyfert proxy reduces the apparent sSFR offset, strengthening the caveat about retired galaxies.
6. **Atlas Section 3 Introduction:** Add a brief introductory sentence at the start of Supplement Section 3 summarizing that the 8 following subsections represent distinct follow-up domains bounded by the shared optical selection effect.
7. **Explicit Atlas Cross-Reference:** In the RP-1 Conclusion, explicitly name the "Supplementary SDSS Denominator and Proxy Atlas" by its exact title so readers know exactly what document is being referenced.

#### Needs New Data (Do Not Edit - For Future Work Only)
8. **Morphology Controls:** Introduce quantitative morphological metrics (e.g., Sersic indices, B/T ratios from Simard et al. or similar) into the matched-control pairing to physically measure and remove the 3-arcsec fiber aperture bias between bulge-dominated and disk-dominated targets.
9. **Volume-Completeness Weighting:** Replace the fixed-size sequential sample with a $1/V_{max}$ weighted volume-limited sample to convert relative optical fractions into true physical volume densities and luminosity functions.
10. **Multiphase Gas Measurements:** Cross-match the optical baseline against resolved CO/HI surveys (e.g., xCOLD GASS, xGASS, ALMA archives) to replace the catalog H-alpha proxy with true molecular/neutral gas depletion times.

---

### Safe Integrator Instructions

To the Integrator: You are authorized to make the following wording and section changes in the next compile pass:
* **Allowed:** You may safely execute Improvements 1, 2, 3, 4, 5, 6, and 7.
* **Allowed terminology substitutions:** Replace "pilot cache" $\rightarrow$ "pilot sample"; "rows" $\rightarrow$ "galaxies/sources"; "table" $\rightarrow$ "sample".
* **Do NOT change:** Do not alter any of the numeric results (e.g., 8,146 pairs, -1.309 dex, [-1.334,-1.283] dex, 60,000 count).
* **Do NOT change:** Do not soften the caveats about the 3-arcsec fiber aperture effect or the lack of causal AGN feedback evidence. Preserve the strict association-only boundary.
* **Do NOT change:** Do not attempt to implement Improvements 8, 9, or 10. They require external data and are out of scope for the current local package.

---

### Safety Ledger
* **Review type:** Read-only local manuscript review.
* **Modifications:** None. No files were edited, written, or deleted.
* **External Actions:** None. No public pages touched, no database writes executed, no API calls made, no git commits/pushes performed, no external manuscript submissions initiated.
* **Integrity:** The association-only claim boundary and numeric results of Cycle 13 were fully preserved. Data was treated strictly as evidence; no data was invented.


# command_result
exit_code=0
elapsed_s=34.3
timed_out=False
finished_utc=2026-07-09T04:23:20Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/gemini_deep/GEMINI_AGY_DEEP_REVIEW_CYCLE_13.md =====
# gemini-agy-deep-cycle-13
Started UTC: 2026-07-09T04:22:46Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_13

### 1. Overview of the Deep Review
As a skeptical deep research reviewer, the candidate package has been analyzed solely based on the provided text of the local flagship paper and its supplementary atlas. The manuscript shows strong progress in positioning the results as selection-aware and association-only. However, there remain several critical risks where a reader could mistake statistical denominator adjustments or proxies for physical feedback, physical environments, or causal transitions.

---

### 2. Issue Log & Proposed Replacements

#### Issue 1: Conflating Optical Excitation with Physical Inflow/Outflow (Kinematics)
* **Severity**: Major
* **Location**: Flagship Abstract, Supplementary Section 3.3
* **Risky Sentence**: 
  > *"An accompanying supplement details the structural and multiwavelength observables required to convert these optical baselines into physical feedback tests."* (Flagship Abstract)
  > *"We isolate the outflow-kinematics denominator that resolved kinematics would need to test escape versus recycling."* (Supplement Section 3.3)
* **Critique**: The term "outflow-kinematics denominator" in Section 3.3 of the Supplement riskily suggests that the sample itself contains outflow signatures or kinematics, whereas it is merely an emission-line-selected sample of high-excitation optical AGN. Calling it "outflow-kinematics" instead of "high-excitation optical AGN" can mislead readers into thinking some kinematic selection has occurred.
* **Safer Replacement**:
  > *"An accompanying supplement details the structural and multiwavelength observables required to translate these statistical optical baselines into physical feedback or kinematic tests."*
  > *"We isolate the high-excitation optical AGN candidate sample to serve as a denominator for future resolved kinematic follow-up."*

#### Issue 2: Weak Caveat on 10th-Neighbor Index and Physical Environment
* **Severity**: Major
* **Location**: Supplement Section 3.1
* **Risky Sentence**:
  > *"Environment baseline: SDSS 10th-neighbor index for low-sSFR incidence"*
  > *"We establish an internal environmental baseline within the emission-line denominator that can later be joined to group catalogs and halo masses."*
* **Critique**: The 10th-neighbor index calculated *within* a selection-limited (four-line S/N $\geq 3$ optical emission line) capped cache is highly unphysical. It does not measure the actual spatial density of the Universe or the parent galaxy distribution; it only measures the density of other highly active emission-line galaxies within a capped subset. This is a severe proxy hazard.
* **Safer Replacement**:
  > *"Baseline of catalog-centric neighbor counts within the emission-line subset for future environmental follow-up"*
  > *"We establish a relative local spatial density baseline within this specific emission-line denominator, which should not be confused with physical local environmental density or halo density until matched to volume-complete catalogs."*

#### Issue 3: Mistaking Denominator Mass Concentration for a Physical Transition Mass
* **Severity**: Major
* **Location**: Supplement Section 3.5
* **Risky Sentence**:
  > *"We identify the mass bin where a future gas-inclusive study should look for an apparent incidence change."*
  > *"The first stellar-mass bin with low-sSFR fraction above 0.5 is $\log(M_\star/M_\odot) \in [11.0,12.5]$"*
* **Critique**: A reader may easily mistake the high incidence of low-sSFR or optical AGN in the $\log(M_\star/M_\odot) \in [11.0, 12.5]$ bin as a physical transition mass signature (e.g., halo quenching or AGN feedback turn-on). However, this concentration is heavily sculpted by the S/N $\geq 3$ selection function, which systematically drops the most quiescent passive galaxies at lower masses and restricts the sample to active/hybrid emitters.
* **Safer Replacement**:
  > *"We identify the stellar-mass ranges where selection effects concentrate hybrid emission-line galaxies, defining a baseline for future gas-inclusive matches."*
  > *"Within this selection-skewed emission-line denominator, the subset with low catalog-sSFR resides predominantly in the $\log(M_\star/M_\odot) \in [11.0,12.5]$ range; this is a selection consequence rather than a physical transition-mass boundary."*

#### Issue 4: Misleading Title/Heading for "Gas-depletion denominator"
* **Severity**: Minor
* **Location**: Supplement Section 3.7
* **Risky Sentence**:
  > *"Gas-depletion denominator: optical baseline for CO/HI follow-up"*
* **Critique**: The phrase "Gas-depletion denominator" implies that gas depletion is measured or used as a denominator. In reality, the denominator consists of massive, low-sSFR optical emission-line galaxies.
* **Safer Replacement**:
  > *"Low-sSFR optical denominator: baseline for future CO/HI gas measurements"*

---

### 3. Citation Role Integrity Analysis

The following citations are flagged for potential role confusion where they may be read as supporting the current SDSS-only methodology rather than acting strictly as motivation for missing future data:

1. **`\citep{piotrowska2022}` (Supplement Section 3.7 & Flagship Section 6)**:
   * *Current Role*: Cited alongside `xcoldgass2017` and `xgass2018` as a requirement for future gas-fraction/depletion-time tests.
   * *Reviewer Guidance*: Correctly positioned as motivation for future multi-parameter analyses. However, care must be taken that the reader does not assume the current matching scheme (stellar mass and redshift only) is validated by the multi-parameter random forest methodology of Piotrowska et al. (2022), which specifically highlights the dominant role of central velocity dispersion/black hole mass over stellar mass. 
   * *Remedy*: Add a note clarifying that the matching in this work is deliberately simpler than the physical regression parameters discussed in Piotrowska et al. (2022).

2. **`\citep{peng2010,wetzel2013,dekel2006}` (Supplement Section 3.1 & 3.5)**:
   * *Current Role*: Cited as motivation/context for environmental and transition-mass tests.
   * *Reviewer Guidance*: These are physical-model and volume-complete statistical papers. Using them in Section 3.1 and 3.5 could lead readers to think the uncorrected 10th-neighbor index in a capped cache behaves similarly to the corrected environments of Peng et al. (2010) or the halo models of Wetzel et al. (2013).
   * *Remedy*: Explicitly state: *"These works rely on volume-complete or halo-calibrated metrics, whereas our 10th-neighbor rank is strictly relative to the active emission-line cache."*

---

### 4. Missing-Data Checklist & Observable Flags

The manuscript lacks, and must explicitly list, the following observations to validate any physical feedback claims:

* **Radio Observables**: Missing resolved radio jet power, morphology (core vs. lobe), and radio duty-cycle calculations to test maintenance heating or environment coupling.
* **X-ray Observables**: Missing hot gas cooling rates, cavity energetics, or X-ray AGN bolometric corrections to establish heating-cooling balance.
* **CO/HI Observables**: Missing molecular gas masses ($M_{\text{H}_2}$ via CO or dust) and neutral gas masses ($M_{\text{HI}}$) to verify whether low sSFR corresponds to gas depletion or low star formation efficiency.
* **Resolved Outflows**: Missing spectroscopic kinematics showing high-velocity gas components (e.g., [O III] asymmetric blue wings) or spatial outflow extent to test gas ejection.
* **Halo/Group Data**: Missing group catalog memberships, satellite vs. central designations, and halo mass estimations to control for environmental quenching.
* **Morphology**: Missing bulge-to-disk decomposition, concentration indices, or Sersic profiles to control for the 3-arcsec fiber aperture mismatch.
* **Simulation Mocks**: Missing synthetic SDSS observations generated by applying the exact S/N and fiber-aperture selection cuts to simulated galaxy populations.

---

### 5. Ranked Integrator Actions

For the next iteration of the manuscript suite, the integrator should prioritize actions in this order:

1. **Aperture & Morphology Warning (Blocker)**: Elevate the 3-arcsec fiber aperture warning in the Flagship and Supplement. Clearly state that because BPT galaxies are typically more bulge-dominated than star-forming controls, the fiber-centered offset of -1.309 dex is likely an upper limit inflated by aperture mismatch rather than global quenching.
2. **Rename Supplementary Section Headings (Major)**: Update titles from "Outflow-kinematics denominator" to "High-excitation optical AGN baseline", and "Environment baseline" to "Relative neighbor-count baseline" to prevent proxy confusion.
3. **Selection-Cut Bias Disclaimer in Mass Trends (Major)**: Add an explicit warning in Supplement Section 3.5 that the $\log(M_\star/M_\odot) \in [11.0,12.5]$ concentration is a selection artifact of the four-line S/N requirement.
4. **Citation Context Clarifications (Minor)**: Append disclaimers to environmental and physical feedback citations (`peng2010`, `piotrowska2022`) to highlight the statistical limitations of the current matched-control comparison.

---

### 6. Safety Ledger

* **Read-only review**: Yes, no files edited or created.
* **Git operations**: None.
* **External APIs / Cloud / Billing**: None.
* **Public updates / replacement / publishing**: None. All actions remained strictly local.


# command_result
exit_code=0
elapsed_s=16.9
timed_out=False
finished_utc=2026-07-09T04:23:03Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_13.md =====
# codex-kun-cycle-13
Started UTC: 2026-07-09T04:22:46Z
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
session id: 019f451d-294c-7df1-84d4-a4aef4f207c6
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_13.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m inspecting the manuscript package for TeX, numerical consistency, and any prose that could weaken the association-only guardrail. First step is to read the four requested files and locate the specific counts, interval values, and guardrail language.
exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/flagship_rp1/aastex/rp1_flagship_polished.tex" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
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
This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors. Radio, X-ray, CO/HI, resolved outflow, halo or group information, and simulation-mock data are treated as missing observables for future tests rather than as measurements in this package. The cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. Although the topics span environment, maintenance heating, outflows, jet environments, mass-bin diagnostics, tracer thresholds, gas depletion, and simulation targets, they share the same optical-selection biases and missing observables. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,kewley2006,stasinska2008,stasinska2015}. The SDSS/BPT/catalog references document the present optical denominators; the radio/X-ray/CO/HI/outflow/simulation references that appear later in the notes are role-separated as future-data motivation rather than validation of the current measurements. Keeping the notes in one supplement prevents overclaiming and gives future work a single checklist of what still must be added. \textbf{This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.}

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
We establish an internal environmental baseline within the emission-line denominator that can later be joined to group catalogs and halo masses. The 10th-neighbor index is an internal ordinal rank within this selection-biased sample and does not map to physical environmental volume density or halo density. SDSS fiber collisions can also suppress close-pair counts in dense environments, so the proxy is biased before any physical interpretation is attempted. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbor index. The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the required missing multiwavelength observables for physical inference are:
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
We isolate the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can serve as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The required missing multiwavelength observables for physical inference are:
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
We isolate the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The required missing multiwavelength observables for physical inference are:
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
We define the environment-stratified optical denominator that future radio and X-ray work could test. The 10th-neighbor index is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-index quartile has an optical AGN fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for future radio-jet follow-up; it does not measure radio jet power or coupling efficiency. The required missing multiwavelength observables for physical inference are:
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


\subsection{Stellar-mass selection diagnostic: low-sSFR and optical AGN incidence}
In this optical-emission-line denominator, the 11.0--12.5 dex peak is a selection-function artifact: the S/N$\geq$3 cut preferentially removes truly passive, massive galaxies, leaving a surviving emission-line subset that is artificially concentrated in that mass bin. It must not be interpreted as a universal feedback threshold. We identify the mass bin where a future gas-inclusive study should look for an apparent incidence change. The note measures the incidence of low catalog-sSFR and optical AGN classification across stellar-mass bins in this emission-line subset. The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the optical AGN fraction peaks in the 11.0--12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The required missing multiwavelength observables for physical inference are:
\begin{itemize}
\item gas fractions
\item baryon deficits
\item halo masses
\item stellar-feedback observables
\item high-redshift extensions
\end{itemize}
The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
\caption{SDSS optical emission-line denominator: mass-bin diagnostic for low-sSFR and optical AGN incidence in the SDSS emission-line denominator. This is a population baseline for future gas-inclusive follow-up, not a physical transition-mass measurement. The 11.0--12.5 dex peak is a selection-function artifact in this emission-line cache, not a universal feedback threshold.}
\label{fig:m2-p3-feedback-transition-mass}
\end{figure}


\subsection{Tracer-threshold census for multiphase follow-up}
We compare optical tracer choices against one shared denominator before any multiphase census is attempted. Simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence within one common SDSS denominator. Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The required missing multiwavelength observables for physical inference are:
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
We define the denominator for CO/HI gas-fraction and depletion-time follow-up. The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. Here the H-alpha luminosity proxy is the aperture-corrected \texttt{galSpecExtra} catalog value, not raw fiber flux. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The required missing multiwavelength observables for physical inference are:
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
We provide a compact observed target vector for forward modelling, not a direct simulation comparison. The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The required missing multiwavelength observables for physical inference are:
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
Maintenance heating & optical AGN in massive low-sSFR hosts & X-ray cavities; cooling luminosity; radio jet powers; halo-selected parents & radio/X-ray follow

[TRUNCATED at 22000 chars from /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_13.md]


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/goru_mech/GORU_MECHANICAL_REPORT_CYCLE_13.md =====
# Goru mechanical report cycle 13

Marker: `GORU_MECHANICAL_REPORT_CYCLE_13`

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
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/flagship_rp1/aastex/rp1_flagship_polished.pdf exists=True bytes=251806 header=%PDF sha256=a59fb3885ad44808a1941c8471a5964346078dcaabe7b2cf6cecb48572ea797c
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_13_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf exists=True bytes=545951 header=%PDF sha256=efa39ccf9654dbd1931ff7a3df91b23de03c683e0a787d6b6adde4b70f4c353f

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


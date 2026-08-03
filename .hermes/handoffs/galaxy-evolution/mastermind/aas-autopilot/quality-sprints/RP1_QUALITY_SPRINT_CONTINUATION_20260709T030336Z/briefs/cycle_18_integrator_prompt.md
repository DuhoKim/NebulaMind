You are the Tori/Codex local manuscript integrator for quality cycle 18.

You may edit ONLY these candidate-copy TeX files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex

You may also write a concise Markdown response here:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/CYCLE_18_REVIEW_RESPONSE.md

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
- Write CYCLE_18_REVIEW_RESPONSE.md summarizing exactly what you changed and what you refused as needing new data.

Review reports follow.


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/hwao/HWAO_QUALITY_REVIEW_CYCLE_18.md =====
# hwao-agy-cycle-18
Started UTC: 2026-07-09T04:56:31Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_18

### Publication-Readiness Verdict

**RP-1 Flagship:** **Conditionally Ready (Requires Polish).** The paper is a scientifically honest, association-only report that correctly bounds its claims within the 60,000-galaxy pilot cache and the SDSS 3-arcsec fiber. However, the heavy repetition of these caveats currently makes it read more like a defensive internal memo than a published short paper. It needs a prose-polish pass to integrate these limitations smoothly without altering the scientific boundary. It is not ready for public release until the "must fix" wording changes are applied.

**Supplementary Atlas:** **Ready.** The supplement perfectly achieves its goal: it catalogs the observational baselines for the 8 other topics while strictly gating their physical interpretation behind lists of missing multiwavelength observables. It is ready to serve as a companion document.

---

### Top 10 Prioritized Improvements

Here is the prioritized plan for the next integrator pass, ranked by their effect on scientific quality and clarity.

#### Must Fix Before Public (Safe Wording/Section Changes)
*The integrator is explicitly authorized to make these text modifications. They do not alter the numeric results or the association-only claim boundary.*

1. **Clarify the Seyfert vs. LINER distinction (Section 5):** The text states that the reduction in offset magnitude (to -0.763 dex) is a "lower bound on how much LINER-like or retired-galaxy contamination...". This phrasing is slightly opaque. The integrator should safely reword this to explicitly explain *why*: because LINER-like/retired galaxies inherently have very low sSFR, their inclusion in the broad BPT class heavily drives the -1.309 dex offset. Removing them leaves the true high-excitation Seyferts, which have a milder sSFR offset.
2. **Integrate the Caliper Result into Text (Section 4):** The text mentions the preferred estimate has no caliper, but Table 2 shows a moderate mass-redshift caliper variant (7,867 pairs, -1.318 dex). The integrator should safely add a sentence to Section 4 explicitly stating that applying a moderate caliper ($|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$) drops only a small fraction of pairs and yields an almost identical offset (-1.318 dex), strengthening the matching robustness.
3. **Consolidate Aperture/Morphology Caveats (Sections 2, 4, 5):** The 3-arcsec fiber and morphology mismatch caveat is repeated heavily across the abstract, data, results, and interpretation sections. The integrator should safely consolidate the physical explanation (e.g., "broad-BPT hosts may be more bulge-dominated than disk-dominated controls, inflating the fiber-centered offset") into the Interpretation section, while leaving only brief, streamlined mentions in the earlier sections to improve narrative flow.
4. **Streamline the Cache Explanation (Abstract & Section 2):** The phrase "fixed-size 60,000-galaxy pilot sample" is critical but awkwardly repeated. The integrator should safely combine the explanation of the cache size and its 24.0% coverage of the strict parent into a single, clear sentence in the abstract and Section 2, ensuring readers understand it is a computational cap and not a physical selection effect.

#### Nice Local Polish (Safe Wording/Section Changes)
*The integrator is authorized to make these formatting and cross-referencing edits to improve readability.*

5. **Standardize Terminology:** The manuscript alternates between "broad optical BPT-selected", "broad-BPT", and "broad BPT-selected targets". The integrator should safely standardize this to "broad optical BPT-selected" throughout the text for consistency.
6. **Cross-Reference Density Proxies (Supplement):** Supplement sections 3.1 (Neighbor-count baseline) and 3.4 (Radio-jet environment) both rely on the 10th-neighbor index. The integrator should add a sentence to 3.4 explicitly pointing the reader back to the definition and baseline established in 3.1.
7. **Streamline Supplement Table Caption:** Table 2 in the Supplement (tab:supp-selection) has a caption almost identical to Table 1 in the flagship. The integrator should safely abbreviate the supplement caption to refer the reader to the main paper for the detailed discussion of the cache drop.

#### Needs New Data (Do NOT attempt to fix now)
*These require physical observables outside the current SDSS-only package. Do not edit the text to claim these are solved.*

8. **Morphology and Aperture Matching:** Proving whether the -1.309 dex sSFR offset is true global quenching or just an aperture effect requires matching controls by bulge-to-total fraction and measuring global sSFR outside the fiber.
9. **Volume-Complete Re-Query:** Deriving true luminosity functions, absolute volume densities, or halo-mass functions requires re-running the SQL queries without the 60,000 `specObjID` cap to obtain a mathematically complete parent sample.
10. **Multiwavelength Integration:** Validating the outflow, multiphase census, and maintenance-heating topics in the supplement requires actual ALMA/NOEMA CO gas masses, resolved IFU kinematics, and X-ray/radio data. 

---

### Instructions for the Integrator

You are clear to run a **local prose-polish pass** addressing items 1 through 7. 
- You **must** preserve the numeric results (8,146 pairs, -1.309 dex median offset, 60k cap, 24% coverage).
- You **must** preserve the boundary that this is an *association only* and not a causal proof of AGN feedback.
- Do not attempt to address items 8, 9, or 10.

---

### Safety Ledger

- **Read-only evaluation:** No files were edited, generated, or overwritten.
- **No external actions:** No Git commits, database writes, API calls, or public deployments were performed.
- **No data fabrication:** All reviews and numeric references were based strictly on the provided local snapshot.


# command_result
exit_code=0
elapsed_s=39.1
timed_out=False
finished_utc=2026-07-09T04:57:10Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/gemini_deep/GEMINI_AGY_DEEP_REVIEW_CYCLE_18.md =====
# gemini-agy-deep-cycle-18
Started UTC: 2026-07-09T04:56:31Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_18

# Manuscript Quality Sprint Deep Review (Cycle 18)

This review evaluates the candidate flagship manuscript (`rp1_flagship_polished.tex`) and its accompanying supplement (`supplementary_denominator_atlas.tex`) under a strict read-only safety model. 

---

## 1. Severity-Ranked Issues

### Issue 1: Over-generalized "AGN Fraction" in Low-Resolution Denominators (Major)
* **Location**: Supplement sections 3.2 (Maintenance Heating), 3.4 (Radio-Jet), 3.5 (Stellar-Mass), and 3.7 (Gas Depletion).
* **Risky Wording**: 
  > "The optical BPT AGN fraction is 0.430 in the massive subset..."
  > "...the optical AGN fraction peaks in the 11.0–12.5 bin at 0.520."
* **Physical vs. Proxy Misdirection**: Calling the BPT-demarcated denominator the "optical AGN fraction" without qualification leads readers to mistake this classification proxy for active supermassive black hole accretion. At SDSS spatial resolutions and fiber apertures, this fraction is heavily contaminated by retired stellar populations and low-ionization gas (LINER-like emission) not powered by accretion.
* **Safer Replacement Wording**: 
  > "The fraction of galaxies falling within the BPT-defined AGN/composite classification boundary (which includes both accretion-powered Seyferts and contamination from retired, stellar-heated bulge systems) is 0.430..."

---

### Issue 2: Insufficient Caveating of Aperture-Extrapolated sSFR (Major)
* **Location**: Flagship Abstract and Section 4.
* **Risky Wording**: 
  > "The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex..."
* **Physical vs. Proxy Misdirection**: A reader could interpret this -1.309 dex offset as a physical galaxy-wide quenching result (star-formation suppression). Because the 3-arcsec fiber only covers the central bulge, and the controls are not matched in morphology, this offset is highly likely a spatial-aperture mismatch effect rather than physical feedback.
* **Safer Replacement Wording**: 
  > "The preferred matched comparison yields 8,146 pairs and a median fiber-aperture-convoluted catalog $\Delta\log {\rm sSFR}$ offset of -1.309 dex (reflecting central sSFR differences and potential morphology/bulge-fraction mismatch)..."

---

### Issue 3: Incomplete Environment Definition from 10th-Neighbor Index (Minor)
* **Location**: Supplement Section 3.1 & 3.4.
* **Risky Wording**: 
  > "We establish a relative neighbor-count baseline... 10th-neighbor index for low-sSFR incidence"
* **Physical vs. Proxy Misdirection**: The 10th-neighbor rank within a capped, selection-limited sample is an ordinal proxy rather than a physical volume density or halo-mass proxy, and fiber collisions severely suppress pairs.
* **Safer Replacement Wording**: 
  > "We establish an ordinal 10th-neighbor index ranking internal to this selection-limited sample (which serves as a target baseline and suffers from fiber-collision suppression rather than representing absolute local volume density)..."

---

## 2. Citation-Role Mapping Audits
All citations in the manuscript are correctly partitioned according to their physical roles:
* **Method/Classification Support (Valid)**: \citep{stasinska2008, stasinska2015} are correctly restricted to identifying stellar/LINER contamination in the optical line ratios.
* **Future-Data Motivation (Valid)**: The multiwavelength references—specifically \citep{best2005, heckmanbest2014, fabian2012, mcnamara2007} (radio/X-ray), \citep{xcoldgass2017, xgass2018} (molecular gas), \citep{veilleux2005, cicone2014} (outflows), and \citep{simba2019, tng2019, eagle2015} (simulations)—are correctly confined to outlining the observational follow-up requirements. They are not used to validate or corroborate the current SDSS-only statistical associations.

---

## 3. Required Missing-Data Warnings

The supplement must explicitly flag where physical claims are currently blocked by missing data:

| Section / Topic | Missing Observables Required for Causal Inference |
| :--- | :--- |
| **3.1 Environment Quenching** | Group catalogs, satellite/central classification, halo mass estimates, and fiber-collision angular corrections. |
| **3.2 Maintenance Heating** | X-ray cavity detection, cooling-flow rates, high-resolution radio jet power, and parent halo-selected samples. |
| **3.3 Outflow Kinematics** | High-resolution resolved kinematics, escape velocity potentials, and multiphase (molecular/neutral) gas tracers. |
| **3.4 Radio-Jet Environment** | Jet morphology/ages, hot-gas density maps, and cavity energetics. |
| **3.8 Simulation Mocks** | Simulated galaxies run through the exact SDSS selection function, line S/N caps, and 3-arcsec fiber aperture convolution. |

---

## 4. Concrete Integrator Action Plan

1. **[Priority 1 - Blocker] Update Abstract and Section Titles in Flagship & Supplement**: Apply the safer replacement wording for BPT AGN fractions (clarifying LINER/retired contamination) and catalog sSFR offsets (clarifying aperture-extrapolation and morphology mismatches).
2. **[Priority 2 - Major] Standarize "Proxy" Terminology**: Scan both documents to ensure terms like "star-formation rates" and "AGN fractions" are consistently prepended with "catalog-derived" or "BPT-classified proxy".
3. **[Priority 3 - Minor] Table Captions**: Add explicit notes to Table 1 and Table 2 explaining that counts are conditional on the non-random pilot query cap (`specObjID` sequential ordering).

---

## 5. Safety Ledger

* **Live system edits**: None.
* **Git actions (commit/push)**: None.
* **Database/API mutations**: None.
* **Public publishing / manuscipt submissions**: None.
* **Resource consumption**: Read-only verification of local file paths under user directory `/Users/duhokim/` was strictly maintained.


# command_result
exit_code=0
elapsed_s=16.5
timed_out=False
finished_utc=2026-07-09T04:56:47Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_18.md =====
# codex-kun-cycle-18
Started UTC: 2026-07-09T04:56:31Z
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
session id: 019f453c-0d1b-74a0-887b-3997b797f7db
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_18.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m checking the four package files directly and validating the specific numeric claims, TeX risks, figure/compile issues, and any wording that could violate the association-only guardrail. I’ll read the manuscript and handoff docs, then cross-check the numbers and extract exact edit recommendations for the integrator.
exec
/bin/zsh -c "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/flagship_rp1/aastex/rp1_flagship_polished.tex'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -c "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/PACKAGE_AUDIT.md'" in /Users/duhokim/NebulaMind/NebulaMind
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
We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, fixed-size 60,000-galaxy pilot cap sequentially selected by \texttt{specObjID} from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on this capped subset rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim.

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
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a fixed-size 60,000-galaxy pilot sample selected sequentially by \texttt{specObjID}. It is a local pilot subset used to validate the analysis workflow and establish the relative association within a fixed cache budget, not a volume-limited census. Because \texttt{specObjID} ordering follows SDSS targeting and plate/MJD bookkeeping, this cap is not a random sky sample and introduces survey-plate and sky-coverage bias. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 galaxies, so the pilot sample covers 24.0\% of that strict parent. Because the cap is fixed and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
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
\tablecomments{Counts are read-only public SDSS DR17 count queries plus the cached analysis table. Retention is shown as a percentage of the spectro-z parent. Cached rows are shown only where the cache applies. The 416,554-to-373,445 drop when requiring \texttt{ivar} $> 0$ reflects the removal of rows with unusable line-flux uncertainties; this table does not distinguish masking, edge-of-chip loss, or missing spectral coverage. The sharp retention drop at higher S/N mainly reflects preferential loss of passive galaxies from the emission-line denominator, so the surviving cache becomes less representative of quiescent hosts as the cut tightens.}
\end{deluxetable*}

The selection is not neutral with respect to star formation. In public counts, S/N$\geq3$ in all four BPT lines keeps 33.6\% of the $-12<\log {\rm sSFR}<-11$ parent bin but 94.9\% of the $-10<\log {\rm sSFR}<-9.5$ bin. Marginal distribution checks between the pilot sample and the full public parent show no redshift, mass, or sSFR bin differing by more than 5 percentage points; the largest absolute differences are 2.03, -1.63, and -0.58 percentage points, respectively. That check is reassuring but does not remove the fixed-size-sample limitation.

\section{Classification and matching}
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Here, the star-forming control pool is defined as objects below the Kauffmann et al.\ (2003) demarcation. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control by variance-normalized Euclidean distance in standardized $(\log M_\star,z)$ space, with replacement. In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements. The preferred estimate does not impose a maximum mass--redshift caliper; the caliper row in Table~\ref{tab:robust} is a sensitivity variant.
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
Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex. Within this sample, that $\sim$0.55 dex reduction is a lower bound on how much LINER-like or retired-galaxy contamination and related selection effects contribute to the broader broad-BPT denominator, rather than evidence for a different active feedback mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global star-formation suppression signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this fixed-size 60,000-galaxy pilot sample. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{Conclusion}
RP-1 is best treated as a concise, selection-aware association paper, not a causal study. The accompanying \emph{Supplementary SDSS Denominator and Proxy Atlas for Galaxy-Evolution Follow-up} holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
In practice, that means future work needs the kinds of measurements used in radio-mode and X-ray maintenance-heating studies \citep{best2005,fabian2012,mcnamara2007,heckmanbest2014,lamassa2013}, molecular and neutral gas studies \citep{xcoldgass2017,xgass2018}, outflow and kinematic studies \citep{veilleux2005,cicone2014,carniani2017,fiore2017}, and simulation-mock comparisons \citep{simba2019,tng2019,eagle2015}, together with the environment/context references \citep{peng2010,piotrowska2022,wetzel2013,dekel2006}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator, and the 3-arcsec fiber aperture effect remains a central limitation of the current association.

\section*{Data Availability}
This paper uses public SDSS DR17 spectroscopy, photometry, emission-line measurements, and MPA-JHU-style value-added catalog tables only. No proprietary data were used. The fixed 60,000-row cache is derived from the public catalog joins and selection thresholds described above, and the manuscript conclusions remain conditional on the optical-emission-line denominator.

\facilities{SDSS}

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
\bibitem[Nelson et al.(2019)]{tng2019} Nelson, D., Springel, V., 

[TRUNCATED at 22000 chars from /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_18.md]


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/goru_mech/GORU_MECHANICAL_REPORT_CYCLE_18.md =====
# Goru mechanical report cycle 18

Marker: `GORU_MECHANICAL_REPORT_CYCLE_18`

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
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/flagship_rp1/aastex/rp1_flagship_polished.pdf exists=True bytes=259688 header=%PDF sha256=d879a8e4cf312dac603ae07571f98e4e3400a71b7a9ac2c3bc67aed9ed677c24
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_18_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf exists=True bytes=552655 header=%PDF sha256=2911a18239ae24ec3276ab9085c04042321d44a091557cf184c4e9acce14679c

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


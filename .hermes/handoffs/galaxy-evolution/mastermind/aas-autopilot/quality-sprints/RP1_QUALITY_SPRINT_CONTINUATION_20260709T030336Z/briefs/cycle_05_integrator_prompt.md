You are the Tori/Codex local manuscript integrator for quality cycle 5.

You may edit ONLY these candidate-copy TeX files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex

You may also write a concise Markdown response here:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/CYCLE_05_REVIEW_RESPONSE.md

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
- Write CYCLE_05_REVIEW_RESPONSE.md summarizing exactly what you changed and what you refused as needing new data.

Review reports follow.


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/hwao/HWAO_QUALITY_REVIEW_CYCLE_05.md =====
# hwao-agy-cycle-5
Started UTC: 2026-07-09T03:32:01Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_05

### Publication-Readiness Verdict

**RP-1 Flagship:** **Conditionally Ready for Local Release (Not Public).** The manuscript successfully holds the association-only claim boundary and transparently reports the sensitivity to S/N and subclass definitions. The core numbers (8,146 pairs, -1.309 dex offset dropping to -0.763 dex) are safely contextualized. However, it requires a few critical wording fixes to ensure the aperture and selection caveats cannot be missed by a skimming reader before it can be considered for public preprint or journal submission. 

**Supplementary Atlas:** **Conditionally Ready for Local Release (Not Public).** The atlas correctly frames the 8 topics as denominators and missing-observable checklists rather than independent causal claims. It needs a minor caption update to ensure the most vulnerable diagnostic (the transition mass) is not misquoted by skimming readers.

---

### Top 10 Concrete Improvements (Ranked by Scientific Quality Effect)

#### Must Fix Before Public (Integrator Action Required)
1. **Supplement Figure 5 Caption Warning:** The caption for Figure 5 (mass-bin diagnostic) must explicitly state that the 11.0--12.5 dex peak is a "selection-function artifact." The main text states this clearly, but readers often skim figures; the caption must prevent them from citing this as a physical transition mass.
2. **Flagship Abstract Fiber Caveat:** The abstract mentions the "bulge/disk mismatch" but should explicitly include the phrase "3-arcsec fiber aperture effect" to ensure the spatial limitation is upfront alongside the selection limitation.
3. **Flagship Table 2 Interpretation Clarity:** For the "N II Seyfert-like proxy", expand the interpretation column slightly to explicitly state that the drop to -0.763 dex is driven by "exclusion of retired/LINER-like bulges," making the physical driver of the sensitivity immediately clear in the table.

#### Nice Local Polish (Integrator Action Recommended)
4. **Flagship Section 4 to 5 Transition:** Smooth the transition between the matched-control result and the interpretation. Explicitly bridge how the fiber-centered nature of the measurement in Section 4 limits the causal interpretation in Section 5.
5. **Supplement Table 2 Retention Context:** Add a table note explaining that the sharp drop in retention (down to 18.3\% for S/N$\geq$10) is driven by the preferential loss of passive galaxies, reinforcing the non-representative nature of the surviving cache.
6. **Flagship Section 1 Claim Boundary:** Reinforce the boundary by explicitly stating in the first paragraph that "this paper does not attempt to normalize the capped 60k-row cache into a volume-complete luminosity or mass function."
7. **Flagship Figure 2 Axis Clarity:** Ensure the text referencing Figure 2 emphasizes that the plotted distribution is a *relative* offset within the matched pairs, not an absolute sSFR distribution.

#### Needs New Data (Do Not Edit - For Future Follow-up Only)
8. **Morphological Matching:** To resolve the bulge/disk aperture mismatch and determine if the -1.309 dex offset is entirely driven by structure, morphological decomposition (e.g., bulge-to-total mass ratios) is required for the matching step.
9. **Maintenance Heating Energetics:** To convert the optical AGN fraction in massive hosts (Supplement 3.2) into a maintenance-heating test, X-ray cavity energetics or calibrated radio jet powers must be joined to the catalog.
10. **Multiphase Gas Masses:** To break the degeneracy between star-formation efficiency and gas depletion (Supplement 3.7), CO(1-0) or HI gas mass measurements (e.g., from xCOLD GASS or xGASS) must be added.

---

### Integrator Instructions: Safe Wording Changes

The integrator is authorized to make the following safe changes to the `.tex` files:
*   **Safe to add:** The phrase "3-arcsec fiber aperture effect" in the flagship abstract and conclusion.
*   **Safe to add:** The phrase "selection-function artifact" to the caption of Figure 5 in the supplement.
*   **Safe to modify:** Table comments and interpretation columns to add clarity on LINER exclusion and retention drops, provided no numbers are changed.
*   **Safe to modify:** Transitional sentences between paragraphs in Sections 4 and 5 of the flagship to improve flow.

**Strict Boundaries:**
*   **DO NOT** alter the core numbers: 60,000 cached rows, 249,917 parent rows, 8,146 matched pairs, -1.309 dex median offset, or -0.763 dex Seyfert proxy offset.
*   **DO NOT** soften the caveats. The words "association only", "not a causal claim", and "capped 60k-row pilot cache" must remain prominent.
*   **DO NOT** move the supplementary topics back into the flagship paper.

---

### Safety Ledger

*   **Files Modified:** None. Read-only review completed based on provided snapshot.
*   **System State:** No deployments, public publishing, API calls, database writes, or git commits were executed. 
*   **Scope:** Local manuscript review only. The package remains in its local directory and is not approved for public release.


# command_result
exit_code=0
elapsed_s=27.8
timed_out=False
finished_utc=2026-07-09T03:32:29Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/gemini_deep/GEMINI_AGY_DEEP_REVIEW_CYCLE_05.md =====
# gemini-agy-deep-cycle-5
Started UTC: 2026-07-09T03:32:01Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_05

## 1. Deep Scientific Review & Risk Identification

### Issue 1: Title Duplication and Scope Mismatch in Supplement Section 3.4
* **Severity**: Major
* **Description**: Section 3.4 of the supplement is titled `\subsection{Environment baseline: optical AGN in massive SDSS hosts}`, which is a near-duplicate of Section 3.2's title (`Maintenance-heating denominator: optical AGN in massive SDSS hosts`) and duplicates the "Environment baseline" prefix of Section 3.1. It also obscures the specific scope of the section (which maps the correlation between the 10th-neighbor density proxy and optical AGN fraction in massive hosts to motivate future radio-jet coupling tests).
* **Risky wording (Supplement Section 3.4 Title)**: 
  `\subsection{Environment baseline: optical AGN in massive SDSS hosts}`
* **Proposed safer replacement**:
  `\subsection{Radio-jet environment baseline: optical AGN fraction vs. density proxy in massive hosts}`

---

### Issue 2: Risk of Conflating Optical Excitation with Accretion-Driven Physical Feedback (Flagship)
* **Severity**: Minor
* **Description**: The Flagship abstract states that "Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only...". Even though it warns that this is not a causal claim, a reader might still interpret the "20-fold lower catalog sSFR" as a direct physical feedback result. The caveat must be strengthened to emphasize that the catalog sSFR itself is based on fiber-spectroscopy modeling and not direct star-formation tracer observations on galaxy-wide scales.
* **Risky wording (Flagship Abstract & Section 4)**:
  `A median \(\Delta\log {\rm sSFR}\) (target minus matched control) of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR within this fiber-centered matched comparison...`
* **Proposed safer replacement**:
  `A median \(\Delta\log {\rm sSFR}\) (target minus matched control) of -1.309 dex corresponds to roughly a 20-fold lower catalog sSFR estimate within this fiber-centered comparison. Because this catalog value is modeled from 3-arcsec fiber spectroscopy, it reflects a central line-ratio suppression rather than a global galaxy-wide star-formation rate reduction.`

---

### Issue 3: Incomplete Fiber-Collision Warning at High Density (Supplement Section 3.1)
* **Severity**: Minor
* **Description**: Section 3.1 mentions the fiber-collision limit (`the SDSS 55-arcsec spectroscopic fiber-collision limit makes this proxy incomplete unless collision corrections are applied; no such correction is applied here`), but it fails to highlight that this systematically underrepresents the densest environments (such as cluster cores), which could artificially suppress the apparent environmental trends.
* **Risky wording (Supplement Section 3.1)**:
  `At the densest cluster cores, the SDSS 55-arcsec spectroscopic fiber-collision limit makes this proxy incomplete unless collision corrections are applied; no such correction is applied here.`
* **Proposed safer replacement**:
  `At the densest cluster cores, the SDSS 55-arcsec spectroscopic fiber-collision limit systematically underrepresents close pairs unless fiber-collision corrections are applied. Since no such correction is applied here, the high-density baseline is incomplete and should be treated as a lower bound for local galaxy packing.`

---

### Issue 4: Transition-Mass Interpretive Trap (Supplement Section 3.5)
* **Severity**: Minor
* **Description**: The term "Transition-Mass" in the title of Section 3.5 (`Mass-bin diagnostic: low-sSFR and optical AGN incidence`, corresponding to `m2_p3_feedback_transition_mass`) can easily mislead readers into thinking this indicates a physical evolution timeline where individual galaxies transition at a specific mass, rather than a selection-biased population snapshot.
* **Risky wording (Supplement Section 3.5 Title & Body)**:
  `\subsection{Mass-bin diagnostic: low-sSFR and optical AGN incidence}` (and references in text to "feedback transition mass").
* **Proposed safer replacement**:
  Modify references to "transition mass" to "incidence diagnostic mass-bin peaks" to reflect that this is a static distribution feature driven by selection limits.

---

## 2. Citation-Role Audit

* **Verified**: No citations are used to falsely support a physical mechanism or measurement method that is not present in the local SDSS data.
* **Properly Isolated**: All citations to radio-mode, X-ray cavity, molecular gas, outflow, environment, and simulation-mock papers (e.g., `best2005`, `dekel2006`, `fabian2012`, `heckmanbest2014`, `lamassa2013`, `mcnamara2007`, `veilleux2005`, `xcoldgass2017`, `xgass2018`, `cicone2014`, `carniani2017`, `fiore2017`, `simba2019`, `tng2019`, `eagle2015`, `peng2010`, `piotrowska2022`, `wetzel2013`) are explicitly flagged in the text as **motivation for missing observables** and are not misrepresented as validation of the current optical-only denominator.

---

## 3. Missing-Data / Observatory Checklist

The following claims in the supplement cannot be validated with the current SDSS dataset and require specific external data categories:
1. **Section 3.1 & 3.4 (Environment & Density)**: Require **Group/Cluster catalogs** (e.g., Yang et al.) and **Halo mass models** to replace the 10th-neighbor rank proxy with true physical halo parameters.
2. **Section 3.2 & 3.4 (Maintenance Heating & Jets)**: Require **radio-continuum fluxes (JVLA/LOFAR)** for jet-power estimation and **deep X-ray imaging (Chandra/XMM)** to measure gas cooling rates vs. feedback heating.
3. **Section 3.3 & 3.6 (Kinematics & Multiphase Census)**: Require **resolved IFS kinematics (MaNGA/SAMI)** and **molecular gas CO/HI line profiles (ALMA/NOEMA/IRAM)** to quantify true wind velocities and outflow mass loading.
4. **Section 3.7 (Gas Depletion)**: Requires **CO (1-0) / HI observations** to distinguish molecular gas mass depletion from a drop in star formation efficiency.
5. **Section 3.8 (Simulation Comparison)**: Requires **forward-modeled mocks** generated from hydro-simulations (e.g., IllustrisTNG, SIMBA) passed through the exact SDSS line S/N and fiber-aperture selection transfer functions.

---

## 4. Ranked Integrator Actions

1. **[Blocker] Fix Supplement Section 3.4 Title**: Update the duplicate title `\subsection{Environment baseline: optical AGN in massive SDSS hosts}` in the LaTeX source of the supplement to properly describe its radio-jet motivation.
2. **[Major] Update fiber-collision caveats**: Inject explicit warnings about cluster core incompleteness in Section 3.1.
3. **[Minor] Add fiber-aperture disclaimer**: Revise Flagship Section 4 to explicitly state that the 20-fold catalog sSFR suppression is a central modeled metric and not necessarily representative of global/galaxy-wide rates.
4. **[Minor] Update Transition-Mass labeling**: Replace text occurrences of "transition mass" in Section 3.5 with descriptive population terms like "incidence peak mass".

---

## 5. Safety Ledger

* **Local Read-Only Review Only**: No file writes, no git operations, no database executions, and no network/API calls were performed.
* **Publishing Status**: No public deployment or replacement of existing files occurred. All recommendations remain strictly confined to this Markdown report.


# command_result
exit_code=0
elapsed_s=17.2
timed_out=False
finished_utc=2026-07-09T03:32:18Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_05.md =====
# codex-kun-cycle-5
Started UTC: 2026-07-09T03:32:01Z
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
session id: 019f44ee-b347-7302-96e3-0c99451f0ec0
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_05.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m checking the four package files and looking specifically for TeX compile hazards, numeric consistency, figure/caption issues, and any wording that weakens the association-only guardrail. After that I’ll give exact edit recommendations without changing anything.
exec
/bin/zsh -lc "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,280p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex'" in /Users/duhokim/NebulaMind/NebulaMind
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
We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60k-row pilot cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities or luminosity functions. The arbitrary cap also means the sample cannot be normalized into absolute volume densities. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only; the sample is not matched in morphology or aperture fraction, which will inherit the known bulge/disk mismatch between BPT-selected hosts and star-forming controls and can inflate the apparent offset. Broad low-ionization classes can also include LINER-like emission from retired stellar populations. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, consistent with contamination of the broad low-ionization class by Low-Ionization Nuclear Emission-line Region (LINER)-like emission from retired stellar populations, especially in massive bulges. Subclass and selection-function treatment must therefore precede any causal interpretation, and an accompanying supplementary denominator/proxy atlas collects the related baselines and missing-observable notes.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? The answer is yes for the cached denominator analyzed here. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.

The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling.

The claim boundary is part of the result. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT AGN'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a capped 60k-row pilot cache selected sequentially by \texttt{specObjID} after an arbitrary pilot-query row limit; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the pilot cache covers 24.0\% of that strict parent. Because the cap is arbitrary and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
Because the 3-arcsec fiber samples only the central regions at low redshift, disk emission can be omitted and the catalog-derived total sSFR can be biased differently for bulge-dominated and disk-dominated systems.
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
Because the comparison is fiber-centered and the matching ignores morphology, the measured offset is a relative difference between the broad-BPT and control samples within the fiber aperture; it will suffer from the known bulge/disk mismatch between broad-BPT hosts and star-forming controls and can therefore be inflated relative to a galaxy-wide suppression signal.

\begin{deluxetable*}{lrrrr}
\tabletypesize{\scriptsize}
\tablecaption{Robustness ladder for matched catalog-sSFR offsets.\label{tab:robust}}
\tablehead{\colhead{Variant} & \colhead{$N$ pairs} & \colhead{Median $\Delta\log {\rm sSFR}$} & \colhead{95\% interval} & \colhead{Interpretation}}
\startdata
Broad BPT AGN, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\
Moderate mass--redshift caliper & 7,867 & -1.318 & -- & 96.6\% target coverage \\
Greedy no-replacement stress test & 7,419 & -1.446 & -- & Poorer balance; diagnostic only \\
Broad BPT AGN, S/N$\geq10$ & 1,530 & -0.744 & -- & Line-S/N sensitivity \\
N II Seyfert-like proxy, S/N$\geq3$ & 2,114 & -0.763 & -- & Subclass sensitivity; LINER-reduced proxy \\
\enddata
\tablecomments{$\Delta\log {\rm sSFR}$ is target minus matched star-forming control. The moderate mass--redshift caliper uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$. The Seyfert-like proxy uses the Kewley et al.\ (2006) high-excitation demarcation, which excludes a portion of the LINER-like low-ionization tail by construction. The drop from -1.309 dex to -0.763 dex therefore reflects systematic removal of the most quenched, bulge-dominated LINER-like systems, not just a random fluctuation. All values are conditional on the optical emission-line denominator.}
\end{deluxetable*}

\begin{figure*}
\centering
\includegraphics[width=0.86\textwidth]{../figures/fig-matched-offsets.pdf}
\caption{Distribution of matched-pair catalog-sSFR offsets for broad optical BPT-selected galaxies minus nearest star-forming controls. The preferred estimate is strong within this denominator but changes under stricter line-S/N and narrower subclass definitions. The moderate matching caliper shown in Table~\ref{tab:robust} uses $|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$.}
\label{fig:offsets}
\end{figure*}

\section{Interpretation}
The result is directly measured, reproducible, and falsifiable inside the stated denominator. The matched-offset distribution is shown in Figure~\ref{fig:offsets}. The median offset is large and survives a moderate mass--redshift caliper.

At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), roughly half the preferred broad-BPT estimate. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including low-ionization nuclear emission-line region (LINER)-like ionization from retired stellar populations and post-AGB stars in massive bulges, rather than identifying a different physical mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global quenching signal. The broad contamination primarily affects the broad low-ionization selection, which is why the narrower Seyfert-like proxy yields the smaller offset. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this capped 60k-row pilot cache. Any quenching-causality claim requires additional data: morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{Conclusion}
RP-1 is best treated as a concise, selection-aware association paper, not a causal study. An accompanying supplementary denominator/proxy atlas holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
In practice, that means future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; these references motivate the missing observables, but they are not part of the present SDSS-only denominator.

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
This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. These counts and fractions are conditional on the SDSS optical selection used here, not global volume-limited statistics, and the cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is a single follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical BPT AGN--catalog-sSFR association. These eight topics are distinct: each is scientifically useful as a denominator or target-vector definition, but each lacks at least one core physical observable required by its original proposal. The BPT language and catalog-backbone language here follow the same SDSS/MPA-JHU-style value-added tables and standard demarcations as the flagship \citep{sdssdr17,brinchmann2004,york2000,baldwin1981,kewley2001,kauffmann2003bpt,ke

[TRUNCATED at 22000 chars from /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_05.md]


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/goru_mech/GORU_MECHANICAL_REPORT_CYCLE_05.md =====
# Goru mechanical report cycle 5

Marker: `GORU_MECHANICAL_REPORT_CYCLE_05`

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
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.pdf exists=True bytes=251791 header=%PDF sha256=df3f60e318a948c20eafd75910f6d830c2cb97f8c84c2eb0a8837008b9e4d037
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf exists=True bytes=545549 header=%PDF sha256=324f8ebfc60797ca39ac54f9937bee9db6cddb20e1ac1f0bdcf0e2d9e7aa3ef6

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


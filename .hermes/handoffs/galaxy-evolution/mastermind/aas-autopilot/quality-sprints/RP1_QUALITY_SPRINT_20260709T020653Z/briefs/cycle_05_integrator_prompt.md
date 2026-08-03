You are the Tori/Codex local manuscript integrator for quality cycle 5.

You may edit ONLY these candidate-copy TeX files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex

You may also write a concise Markdown response here:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/CYCLE_05_REVIEW_RESPONSE.md

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


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/hwao/HWAO_QUALITY_REVIEW_CYCLE_05.md =====
# hwao-agy-cycle-5
Started UTC: 2026-07-09T02:39:47Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_05

**Publication-Readiness Verdict**

*   **RP-1 (Flagship):** **Conditionally Ready for Public Draft (Local Only for Now).** The scientific boundary is excellent. The manuscript strictly holds the line at "association" within a capped SDSS denominator and actively rejects causal AGN feedback claims without further data. The honesty about the 60,000-row cache cap and the Seyfert-vs-LINER sensitivity is exactly what we want. 
*   **Supplementary Atlas:** **Ready.** Re-packaging the 8 prior drafts into an atlas of "denominators and missing observables" was the correct strategic move. It is an honest, scientifically useful resource for future multiwavelength follow-up. 

***

**Top 10 Concrete Improvements (Prioritized by Scientific Quality)**

**Category A: Must Fix Before Public (Safe Integrator Wording Changes)**
1.  **Abstract Clarity on LINER Contamination (RP-1):** The abstract currently states that narrower Seyfert definitions reduce the offset magnitude, but it needs to explicitly state *why* in the abstract itself: that the broad BPT class is contaminated by LINER-like emission from retired stellar populations, meaning the -1.309 dex offset mixes true AGN with passive galaxies.
2.  **Aperture Bias Caveat (RP-1 Section 3):** Section 3 states matching is not performed in aperture fraction. Add one sentence explicitly stating that because SDSS fibers (1.2–6.5 kpc) miss the outskirts of low-redshift galaxies, the fiber-centered sSFR comparison heavily penalizes bulge-dominated galaxies, inflating the apparent sSFR deficit.
3.  **Volume Density Disclaimer (Supplement Abstract):** The supplement abstract should explicitly mention the "24.0% cached coverage of the S/N$\geq$3 parent." Readers must know immediately from the abstract that these are not global volume-limited statistics.
4.  **Transition Mass Disclaimer (Supplement 3.5):** Add a sentence to section 3.5 stating that the observed 11.0-12.5 mass peak may simply reflect the optical emission-line selection function intersecting with the quenched population, rather than a universal physical feedback threshold.

**Category B: Nice Local Polish (Safe Integrator Formatting/Structure Changes)**
5.  **Paragraph Split for Sensitivity (RP-1 Section 5):** Split Section 5 into two paragraphs. Paragraph 1: The main matched-offset result and the mass-redshift caliper. Paragraph 2: The line-S/N and Seyfert-like proxy variants and the resulting LINER-contamination discussion. This improves readability.
6.  **Standalone Figure Captions (RP-1):** Expand the caption for Figure 2 to explicitly state the caliper limits ($|\Delta\log M_\star|\leq0.05$ and $|\Delta z|\leq0.002$) so the figure can be understood without reading the text.
7.  **Standardize "Missing Observables" Language (Supplement):** Ensure consistent terminology across the 8 atlas notes. For example, standardize "halo masses", "halo potentials", and "halo-selected parent catalogues" to a unified term where appropriate, or group them logically to emphasize the missing dark matter context.
8.  **Table 2 Footnote (RP-1):** Add a footnote to Table 2 explicitly linking the "Seyfert-like proxy" variant to the exclusion of LINERs, reinforcing the text in Section 5.

**Category C: Needs New Data (Do NOT attempt to fix in this manuscript)**
9.  **Morphological Matching:** Adding morphological and structural controls (e.g., S\'ersic index, bulge-to-total ratio) to eliminate the aperture/bulge bias from the sSFR comparison.
10. **Multiphase Gas (CO/HI) integration:** Adding ALMA/xCOLD GASS data to break the degeneracy between a true lack of molecular gas (depletion) versus a lower star formation efficiency in the remaining gas.

***

**Integrator Instructions for Safe Changes**

Integrator, you are authorized to make the wording changes listed in Categories A and B above. 
*   **Do NOT** alter any numeric results, sample sizes, or statistical intervals.
*   **Do NOT** cross the claim boundary: maintain the stance that this is an association only, conditional on the optical emission-line cache.
*   **Do NOT** remove the caveats regarding the 60,000-row cap or the Seyfert vs. LINER sensitivity.
*   Recompile the PDFs locally after making these wording adjustments to ensure formatting holds.

***

**Safety Ledger**
*   **State:** Local read-only review completed.
*   **Files Modified:** 0
*   **Commands Executed:** 0
*   **External Network Requests:** 0
*   **Database/Wiki/API Changes:** 0
*   **Action Taken:** Generated prioritized local quality plan based on provided text only. No public replacement or publishing authorized.


# command_result
exit_code=0
elapsed_s=28.3
timed_out=False
finished_utc=2026-07-09T02:40:16Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/gemini_deep/GEMINI_AGY_DEEP_REVIEW_CYCLE_05.md =====
# gemini-agy-deep-cycle-5
Started UTC: 2026-07-09T02:39:47Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_05

## 1. Executive Summary & Synthesis
This review is conducted in a read-only mode to assess the scientific framing of the flagship paper (RP-1) and its supplementary denominator/proxy atlas. The overarching goal is to prevent any physical interpretation of selection-skewed or aperture-biased catalog parameters and to ensure they are strictly understood as observational denominators.

---

## 2. Issues and Proposed Revisions

### Issue 1: Overclaim / Confounding of Fiber-Center Catalog sSFR with Global Star Formation
* **Severity**: Major
* **Risky Sentence (Flagship, Sec. 2)**: 
  > "Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2–6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global."
* **Critique**: The abstract and subsequent sections repeatedly refer to "catalog specific star-formation rate" and "median $\Delta\log {\rm sSFR}$ of -1.309 dex". A reader might mistake this catalog offset as representing a physical suppression of star formation across the whole galaxy. Because BPT classifications and catalog properties are measured within a fixed 3-arcsec physical aperture that covers different physical scales at different redshifts (1.2 kpc vs 6.5 kpc), there is a strong aperture bias. If the AGN hosts are more centrally concentrated or bulgy, the fiber will sample more bulge light than in star-forming control galaxies of the same mass, artificially depressing the fiber sSFR proxy.
* **Proposed Replacement**:
  > "Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2–6.5 kpc. Consequently, the catalog sSFR offset is dominated by fiber-aperture limitations and represents a central fiber-based proxy offset rather than a global galaxy-wide specific star-formation rate suppression."

---

### Issue 2: Weak Caveat on Sample Non-Randomness and Capping
* **Severity**: Blocker
* **Risky Sentence (Flagship, Abstract & Sec. 2)**: 
  > "The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies..."
* **Critique**: Why was the cache capped at 60,000 rows, and how was it ordered? The text notes it is ordered by `specObjID`. Since `specObjID` encodes plate, MJD, and fiber, sorting by it and truncating introduces systematic selection bias based on observation date and sky coverage (e.g., plates observed early in the SDSS survey vs. later runs). This is a blocker for treating the statistics as representative of even the parent SDSS catalog.
* **Proposed Replacement**:
  > "Because the 60,000-row cache is truncated sequentially by \texttt{specObjID}, it is subject to spatial and observational epoch biases from the early stages of the SDSS survey. All statistical intervals and offset measurements are purely illustrative of this sub-sample and must not be treated as unbiased representations of the DR17 parent population."

---

### Issue 3: Citation-Role Ambiguity (Method Support vs. Future Motivation)
* **Severity**: Minor
* **Risky Citation Grouping (Flagship, Sec. 6)**:
  > "...future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies \citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}; they are not part of the present SDSS-only denominator."
* **Critique**: The paper cites a massive block of 18 papers at once. Some of these papers contain actual observational methods or catalogs (like `\citep{xcoldgass2017,xgass2018}` for gas masses, `\citep{best2005}` for radio), whereas others are theoretical models or simulations (`\citep{dekel2006,tng2019,eagle2015}`). Grouping them together obscures which references serve as motivation for future multiwavelength data vs. which ones represent theoretical simulation targets.
* **Proposed Replacement**:
  > "In practice, this means future work must incorporate external physical constraints: radio jet power and cavity energetics (e.g., \citealt{best2005,mcnamara2007,heckmanbest2014}), molecular gas reservoirs (e.g., \citealt{xcoldgass2017,xgass2018}), kinematics of multiphase outflows (e.g., \citealt{veilleux2005,cicone2014}), environment and group halo membership (e.g., \citealt{peng2010,wetzel2013}), and mock observations generated from cosmological simulations (e.g., \citealt{tng2019,eagle2015})."

---

### Issue 4: Denominator Misinterpretation in Supplement
* **Severity**: Major
* **Risky Sentence (Supplement, Sec. 3.5)**:
  > "At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator?"
* **Critique**: A casual reader might interpret this mass scale (e.g. $[11.0, 12.5]$ dex) as a physical quenching transition mass due to AGN feedback. However, in this BPT-selected emission-line sample, the high-mass bins are extremely incomplete due to the exclusion of weak/retired galaxies that do not meet the four-line S/N $\geq 3$ threshold. 
* **Proposed Replacement**:
  > "We identify the stellar-mass bin where the active emission-line fraction is dominated by low-sSFR and optical AGN classifications within our selection cut. This transition reflects selection-induced emission-line survivorship rather than a physical transition mass for individual galaxy quenching."

---

## 3. Required Missing-Data Observables Checklist

The supplementary atlas must explicitly document the following missing observables to avoid presenting proxy values as physical results:

| Section | Topic / Paper | Missing Physical Observables | Risk of Status Quo |
| :--- | :--- | :--- | :--- |
| **3.1** | Environment Quenching | Group catalogs, central/satellite classification, weak-lensing or X-ray group halo masses. | Density proxy is mistaken for physical halo-based environmental quenching. |
| **3.2** | Maintenance Heating | High-resolution radio maps (VLA/LOFAR), X-ray cavity/cooling measurements (Chandra/XMM). | Optical BPT class is mistaken for active mechanical/radio jet feedback. |
| **3.3** | Outflow Escape | Spatially resolved kinematics (IFU), gas phase tracers (neutral/molecular/ionized). | Ionization line ratios are mistaken for physical gas outflows. |
| **3.4** | Radio Jet Environment | Radio morphologies, environmental group membership, cluster-gas density profile. | Host local density proxy is mistaken for radio-mode coupling. |
| **3.5** | Transition Mass | Gas fractions ($f_{\rm gas}$), total baryon census, halo masses. | Survivorship bias in BPT sample is mistaken for a physical feedback mass threshold. |
| **3.6** | Multiphase Census | CO (molecular), H I (neutral), X-ray (hot gas) mass measurements. | Optical emission ratios are mistaken for total cold/warm gas budget. |
| **3.7** | Gas Depletion | Direct CO molecular gas masses, resolved aperture corrections. | Catalog sSFR drop is mistaken for low gas-fraction or altered SFE. |
| **3.8** | Sim Validation | Synthetic mock catalogs processed through the exact SDSS fibers and line selection. | Direct catalog-to-simulation comparison without forward modeling. |

---

## 4. Ranked Integrator Actions

1. **[Priority 1: Blocker] Fix Cache Bias Statement**: Add a clear disclaimer in the flagship paper's introduction and data section explaining how sorting the 60,000-row sample by `specObjID` impacts statistical generality.
2. **[Priority 2: Major] Add Aperture/Fiber Warning**: Include a specific warning about the difference between fiber-based and global specific star-formation rates (sSFR) in Section 2 of the flagship paper.
3. **[Priority 3: Major] Standardize Supplement Section Disclaimers**: Ensure that each of the 8 subsections in the supplement starts with a bolded warning that the figures show selection-skewed denominators, not physical population properties.
4. **[Priority 4: Minor] Unpack Block Citations**: Split the large bibliography group in Section 6 into category-specific citations (e.g. splitting simulations from observations).

---

## 5. Safety Ledger

* **Files Read**: None (Read-only review performed solely using the text provided in the prompt).
* **Files Written**: None.
* **Commands Run**: None.
* **Database/API/Cloud Changes**: None.
* **Git Actions**: None.
* **Status**: 100% Local, Read-Only, Safe Review.


# command_result
exit_code=0
elapsed_s=15.6
timed_out=False
finished_utc=2026-07-09T02:40:03Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_05.md =====
# codex-kun-cycle-5
Started UTC: 2026-07-09T02:39:47Z
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
session id: 019f44be-e0ce-7f80-8fd4-71c4ed081c5e
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/FINAL_HANDOFF.md

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
I’m inspecting the package for TeX, compilation, figure, and reproducibility risks, then I’ll verify the required numeric claims against the manuscript text and handoff notes. After that I’ll give exact, safe edit recommendations that preserve the association-only guardrail.
exec
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex" in /Users/duhokim/NebulaMind/NebulaMind
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
This supplement collects eight SDSS DR17 denominator and proxy notes that share the same capped 60,000-row optical emission-line cache and the same selection-function caveats. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. These counts and fractions are conditional on the SDSS optical selection used here, not global volume-limited statistics. It is a single follow-up atlas, not eight independent causal-feedback papers.
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
This note isolates an environmental denominator that can later be joined to group catalogs and halo masses. The nearest-neighbour density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample. The SDSS emission-line denominator contains 60,000 galaxies with an internally computed 10th-neighbour density proxy. The high-density quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-density quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-density coefficient of 0.032 +/- 0.004. This is a denominator-level environmental diagnostic; the missing observables are:
\begin{itemize}
\item group catalogues
\item robust central/satellite labels
\item halo masses
\item morphology
\item multi-redshift selection functions
\end{itemize}
These are still needed for a physical environmental interpretation \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-01.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m1\_rp2\_environment\_quenching. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m1-rp2-environment-quenching}
\end{figure}


\subsection{Optical-AGN denominator for maintenance-heating follow-up}
This note identifies the optical-AGN duty-cycle denominator that radio and X-ray data would need to test maintenance heating. Among massive, low-sSFR SDSS emission-line galaxies, the optical AGN fraction can be used as a denominator for X-ray and radio maintenance-heating follow-up. The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The optical BPT AGN fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects. This provides an optical duty-cycle denominator for X-ray and radio follow-up, not a heating-to-cooling measurement. The missing observables are:
\begin{itemize}
\item X-ray cavity or cooling-luminosity measurements
\item radio jet powers
\item halo-selected parent catalogues
\item nondetection modelling
\end{itemize}
These are still needed for a physical maintenance-heating interpretation \citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-02.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m1\_rp3\_maintenance\_heating. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m1-rp3-maintenance-heating}
\end{figure}


\subsection{SDSS high-excitation AGN denominator for outflow tests}
This note isolates the high-excitation optical-AGN denominator that resolved kinematics would need to test escape versus recycling. High-excitation optical AGN candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator. SDSS does not measure escape velocity or multiphase outflow velocities here; the note supplies a denominator for resolved follow-up rather than an escape or recycling result. The missing observables are:
\begin{itemize}
\item resolved outflow velocities
\item halo potentials
\item molecular, ionized, and neutral gas phases
\item CGM recycling tracers
\end{itemize}
These are still needed for a physical outflow interpretation \citep{veilleux2005,cicone2014,carniani2017,fiore2017,lamassa2013}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-03.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m2\_p1\_outflow\_escape\_recycling. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m2-p1-outflow-escape-recycling}
\end{figure}


\subsection{Environment proxy for optical AGN in massive SDSS hosts}
This note defines the environment-stratified optical denominator that future radio and X-ray work could test. The local-density proxy is correlated with the optical AGN fraction in massive SDSS hosts and motivates environment-stratified radio and X-ray follow-up. Among massive hosts, the high-density quartile has an optical AGN fraction of 0.509, while the low-density quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]. This is an optical/environment denominator for radio-jet coupling work; it does not measure radio jet power or coupling efficiency. The missing observables are:
\begin{itemize}
\item radio jet morphology and age
\item cavity or shock energetics
\item hot-gas density
\item calibrated jet-power estimates
\end{itemize}
These are still needed for a physical radio-jet interpretation \citep{best2005,mcnamara2007,heckmanbest2014}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-04.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m2\_p2\_radio\_jet\_environment. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m2-p2-radio-jet-environment}
\end{figure}


\subsection{Stellar-mass distribution of low-sSFR and optical AGN incidence}
This note pins down the mass bin where a future gas-inclusive study should look for an incidence change. At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator? The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\). The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520. This is an optical distribution diagnostic; gas fractions and baryon deficits are needed before assigning any physical meaning to the apparent incidence change. The missing observables are:
\begin{itemize}
\item gas fractions
\item baryon deficits
\item halo masses
\item stellar-feedback observables
\item high-redshift extensions
\end{itemize}
The same binning is therefore best treated as a population-distribution diagnostic, not a statement about a physical transition mass for individual galaxies \citep{peng2010,wetzel2013,dekel2006}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-05.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m2\_p3\_feedback\_transition\_mass. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m2-p3-feedback-transition-mass}
\end{figure}


\subsection{Common-denominator optical tracer census in SDSS}
This note compares optical tracer choices against one shared denominator before any multiphase census is attempted. How strongly do simple optical tracer definitions change the inferred AGN or feedback-candidate prevalence in one common SDSS denominator? Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, or X-ray or radio phases. This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates. The missing observables are:
\begin{itemize}
\item ionized, molecular, and neutral tracers
\item X-ray or radio tracers
\item a shared parent denominator
\item a consistent aperture model
\end{itemize}
These are still needed for a physical multiphase interpretation \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-06.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m3\_p1\_multiphase\_census. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m3-p1-multiphase-census}
\end{figure}


\subsection{Optical denominator for gas-fraction versus efficiency tests}
This note defines the denominator for CO/HI gas-fraction and depletion-time follow-up. How many massive low-sSFR or transitioning SDSS galaxies with valid emission-line measurements are available as a denominator for CO gas-fraction and depletion-time follow-up? The massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample. Its optical BPT AGN fraction is 0.549, and the median H-alpha luminosity proxy is 40.06. The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies. SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this note identifies the CO/HI follow-up denominator and optical baseline. The missing observables are:
\begin{itemize}
\item CO or dust-based molecular gas masses
\item aperture-matched SFRs
\item morphology
\item environment labels
\end{itemize}
These are still needed for a physical gas-fraction or depletion-time interpretation \citep{xcoldgass2017,xgass2018,piotrowska2022}.

\begin{figure}
\centering
\includegraphics[width=\columnwidth]{../figures/topic-07.pdf}
\caption{SDSS optical denominator/proxy diagnostic for m3\_p2\_gas\_depletion\_efficiency. This is a follow-up target definition or baseline, not a physical-feedback measurement.}
\label{fig:m3-p2-gas-depletion-efficiency}
\end{figure}


\subsection{SDSS target vector for feedback-model validation}
This note provides a compact observed target vector for forward modelling, not a direct simulation comparison. What compact SDSS target vector of low-sSFR fraction, optical AGN incidence, and colour versus mass and redshift can be used for forward-model validation? The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact validation vector. Across mass bins, low-sSFR fractions span 0.005-0.729, and optical AGN fractions span 0.003-0.520. The output is an observed target vector for simulation forward modelling, not a direct simulation comparison. The missing observables are:
\begin{itemize}
\item simulation mocks passed through the SDSS, MaNGA, ALMA, X-ray, and radio selection functions
\item aperture models
\item noise models
\end{itemize}
These are still needed for a physical simulation-validation interpretation \citep{simba2019,tng2019,eagle2015}.

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
/bin/zsh -lc "sed -n '1,260p' /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.tex" in /Users/duhokim/NebulaMind/NebulaMind
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
We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis uses a non-random, capped 60,000-row emission-line cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume 

[TRUNCATED at 22000 chars from /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_05.md]


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/lanes/goru_mech/GORU_MECHANICAL_REPORT_CYCLE_05.md =====
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
- flagship: ['causal AGN feedback', 'outflow escape', 'molecular gas depletion']
- supplement: []

## PDF receipts
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/flagship_rp1/aastex/rp1_flagship_polished.pdf exists=True bytes=243677 header=%PDF sha256=92fbce0c03726ced6fc7fbb9ffd85a4690b738071433e2b5db2cb4c8f4b3a5bc
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_05_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf exists=True bytes=538302 header=%PDF sha256=60d6bbbada6d0942c5912da6fc2c35eb8a4429efd8a3f50dce0b88ccbf2f96a0

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


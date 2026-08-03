You are the Tori/Codex local manuscript integrator for quality cycle 11.

You may edit ONLY these candidate-copy TeX files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex

You may also write a concise Markdown response here:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/CYCLE_11_REVIEW_RESPONSE.md

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
- Write CYCLE_11_REVIEW_RESPONSE.md summarizing exactly what you changed and what you refused as needing new data.

Review reports follow.


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/hwao/HWAO_QUALITY_REVIEW_CYCLE_11.md =====
# hwao-agy-cycle-11
Started UTC: 2026-07-09T04:05:11Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_11

## Publication-Readiness Verdict

**RP-1 Flagship Draft (Selection-aware SDSS BPT/sSFR study):** 
**Verdict:** `ALMOST READY FOR PUBLIC RELEASE`
*Reasoning:* The manuscript successfully maintains the strict scientific boundary we established. It correctly presents the results as a catalog association rather than a causal feedback measurement, properly scopes the use of the non-random capped pilot cache, and correctly identifies the limitations (morphology, aperture fraction, LINER-contamination). With a few minor clarity and structural improvements, it is safe for public release as a bounded data note.

**Supplementary Denominator Atlas:** 
**Verdict:** `READY AS LOCAL REFERENCE / LOCAL ARCHIVE`
*Reasoning:* The supplement brilliantly compiles the other 8 studies into denominator and target-vector baselines without overclaiming. It repeatedly and accurately cites the missing multiwavelength observables required for true physical inferences. However, as it currently exists, it is more of an internal mapping for future work rather than a standalone publication. It should be kept as a local atlas and potentially included as a data release note or extended appendix when the main flagship is finalized. 

---

## Top 10 Prioritized Concrete Improvements

### Category: Must Fix Before Public (Safe for Integrator to Edit)

**1. Clarify the 60k Pilot Cache Limitation (RP-1 Abstract & Sec 2)**
*Effect on Quality: Critical for transparency.*
While mentioned, the phrase "arbitrary pilot-query row limit" in Section 2 sounds slightly overly defensive. 
*Action:* Edit Section 2 to simply state that the 60,000-row sample is a computationally convenient, non-volume-limited subset used to establish the relative association, making it clear that volume densities cannot be derived, without sounding like an error occurred.

**2. Standardize the Aperture Caveat Phrasing (RP-1 Sec 4 & 5)**
*Effect on Quality: Prevents misinterpretation of the sSFR offset.*
The phrase "heavily modulated by the central aperture" in Section 4 is good, but in Section 5 it's reduced to "fiber-centered and selection-limited". 
*Action:* Explicitly state in the Interpretation section that the -1.309 dex offset may be partially or entirely driven by comparing bulge-dominated broad-BPT hosts to disk-dominated controls due to the fixed 3-arcsec fiber. 

**3. Streamline the LINER/Retired Host Caveat (RP-1 Sec 5)**
*Effect on Quality: Improves readability of the core finding.*
The explanation of the drop from -1.309 dex to -0.763 dex (Table 2) is a bit repetitive in the text. 
*Action:* Consolidate the explanation in Section 5. State clearly that stricter Seyfert cuts remove LINER-like and retired stellar populations, which inherently have lower sSFR, thus proving the association is highly sensitive to the exact emission-line denominator.

**4. Strengthen the Abstract's Final Sentence (RP-1 Abstract)**
*Effect on Quality: Better sets up the Supplement.*
*Action:* Change "An accompanying supplementary denominator/proxy atlas collects the related baselines..." to "An accompanying supplement details the structural and multiwavelength observables required to convert these optical baselines into physical feedback tests."

### Category: Nice Local Polish (Safe for Integrator to Edit)

**5. Improve Table 2 (Robustness Ladder) Interpretability (RP-1)**
*Effect on Quality: Makes the most important table easier to read.*
*Action:* Shorten the "Interpretation" column entries. For example, change "Excludes retired/LINER-like bulges by construction" to "Excludes LINER/retired populations". Ensure the table notes carry the detailed explanation.

**6. Soften the Tone of the Supplement Abstract**
*Effect on Quality: Reads more like a standard astronomical atlas.*
*Action:* Remove the phrase "while explicitly avoiding claims that require...". Instead, use standard phrasing: "This atlas provides observational baselines intended for future integration with radio, X-ray, CO/HI, and resolved outflow data."

**7. Add a Unifying Paragraph to the Supplement Introduction**
*Effect on Quality: Better ties the 8 disparate notes together.*
*Action:* Add two sentences in Section 1 explaining that while these 8 optical baselines address different evolutionary questions (environment, outflows, gas depletion), they share the exact same optical selection biases, making a unified atlas the safest way to present them.

**8. Refine the 11.0-12.5 Mass Peak Caveat (Supplement Sec 3.5)**
*Effect on Quality: Prevents miscitation of the mass peak.*
*Action:* Ensure it is abundantly clear that the 11.0-12.5 dex peak in optical AGN fraction is an artifact of the S/N$\geq$3 cut removing passive galaxies, not a physical transition mass. 

### Category: Needs New Data (Do NOT attempt to fix in text)

**9. Morphology and Aperture Matching (RP-1)**
*Effect on Quality: Would turn the association into a physical constraint.*
*Action:* Requires structural decompositions (e.g., Sersic fits) or IFU data (MaNGA) to match targets and controls by bulge fraction or $R_e$. Cannot be fixed with text.

**10. Cold Gas Fractions (Supplement Sec 3.7)**
*Effect on Quality: Would turn the H-alpha proxy into a true depletion efficiency.*
*Action:* Requires cross-matching with xCOLD GASS or similar surveys to obtain CO-based molecular gas masses. Cannot be fixed with text.

---

## Safe Editing Boundary for the Integrator

The integrator is authorized to make wording, phrasing, and structural changes that address Items 1 through 8 above. 

**STRICT BOUNDARY:**
- Do **not** alter the core claim: it must remain an *association* within a *capped denominator*.
- Do **not** alter any numbers, counts, fractions, or confidence intervals (-1.309 dex, 8,146 pairs, 60,000 rows, 24.0\%, etc.).
- Do **not** attempt to extrapolate the 60k pilot cache into a volume-complete metric.
- Do **not** claim that AGN are causing the sSFR offset.
- Do **not** merge the Supplement into the Flagship paper. Keep them as two separate PDFs.

---

## Safety Ledger

- **Environment:** Read-only local manuscript review.
- **Files Touched:** None. No edits, commits, or saves performed.
- **Network/Public:** No public pages touched. No deployments. No API calls made. No database interactions.
- **Code Execution:** None.
- **Data Integrity:** All numeric values and safety boundaries from the provided package snapshot were preserved exactly.


# command_result
exit_code=0
elapsed_s=27.6
timed_out=False
finished_utc=2026-07-09T04:05:38Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/gemini_deep/GEMINI_AGY_DEEP_REVIEW_CYCLE_11.md =====
# gemini-agy-deep-cycle-11
Started UTC: 2026-07-09T04:05:11Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_11

# Deep Research Review Report: RP-1 Flagship & Supplementary Atlas

This review evaluates the cycle 11 manuscript package comprising `flagship_rp1` and `supplementary_denominator_atlas`. We take a skeptical peer-reviewer perspective, focusing on overclaims, sample selection biases, proxy limitations, and proper citation roles within this SDSS-only dataset.

---

## 1. Safety Ledger

As dictated by the safety directive, this is a **read-only review**.
- No files were edited, created, or deleted.
- No terminal commands, compilation, or git operations were executed.
- No public publishing or database writes were performed.
- All results, metrics, and text snippets evaluated are derived directly from the provided local snapshot.

---

## 2. Issues & Risk Assessment

### Issue 1: Confounding Catalog sSFR for Physical/Global Quenching Results
- **Severity**: Major
- **Location**: `flagship_rp1` (Abstract, Sections 4 & 5)
- **Risk**: The manuscript uses catalog-level specific star-formation rate estimators (`specsfr_tot_p50` from MPA-JHU) that rely on 3-arcsec fiber spectroscopy with extrapolations. A reader might mistake this proxy offset for a physical star-formation suppression or quenching mechanism, whereas it primarily reflects the bulge-dominated structure (and corresponding fiber aperture sampling differences) of BPT-selected AGN hosts vs. star-forming disk controls.
- **Risky Sentence**: 
  > *"A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison, which is heavily modulated by the central aperture, but this manuscript does not convert that proxy offset into a global star-formation suppression threshold."* (Section 4)
- **Proposed Safer Wording**:
  > *"Within this fiber-centered matched comparison, we observe a median catalog-derived $\Delta\log {\rm sSFR}$ (target minus matched control) offset of -1.309 dex. Because the spectroscopy only samples the central 3-arcsec region (1.2–6.5 kpc) and the match is not controlled for morphology or aperture fraction, this difference primarily reflects structural differences and fiber-extrapolation offsets rather than global, galaxy-wide star-formation quenching."*

---

### Issue 2: Confusing Target-Selection Selection-Function Artifacts with Physical Transition Masses
- **Severity**: Major
- **Location**: `supplementary_denominator_atlas` (Section 3.5, Figure 5 caption)
- **Risk**: The apparent peak in low-sSFR and optical AGN fraction in the $\log M_\star \sim 11.0-12.5$ range is highly influenced by the four-line S/N $\geq 3$ BPT emission-line selection. Real, completely quiescent/passive galaxies without lines are excluded. This can be misconstrued as physical evidence for a feedback "transition mass".
- **Risky Sentence**:
  > *"The first stellar-mass bin with low-sSFR fraction above 0.5 is $\log(M_\star/M_\odot) \in [11.0,12.5]$, and the optical AGN fraction peaks in the 11.0--12.5 bin at 0.520."* (Section 3.5)
- **Proposed Safer Wording**:
  > *"Within this emission-line-selected denominator (which by construction excludes completely quiescent galaxies lacking the four required BPT lines), the low-sSFR fraction and optical AGN fraction peak in the $\log(M_\star/M_\odot) \in [11.0,12.5]$ bin at 0.520. Because the BPT line-detection requirement preferentially rejects massive, passive galaxies, this peak is a selection-function artifact and does not represent a physical transition-mass threshold for galaxy quenching."*

---

### Issue 3: Inappropriate Citation Roles (Method Support vs. Future Motivation)
- **Severity**: Minor
- **Location**: `flagship_rp1` (Section 6) and `supplementary_denominator_atlas` (Sections 1 & 2)
- **Risk**: Several citations (e.g., to molecular gas surveys like xCOLD GASS, outflow works, or cosmological simulations) could be misread as support for the *methodology* or *correctness* of the current measurements. They must be explicitly framed as motivational context for *future* observations that this SDSS-only paper lacks.
- **Risky Sentence**:
  > *"Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis. In practice, that means future work needs the kinds of measurements used in radio-mode and X-ray maintenance-heating studies [citations], molecular and neutral gas studies [citations]..."* (Section 6)
- **Proposed Safer Wording**:
  > *"The current analysis lacks direct measures of the circumgalactic and interstellar media. Future follow-up work will require the integration of physical observables not present in our SDSS-only sample: specifically, radio-jet or X-ray cavity diagnostics to test heating (e.g., Best et al. 2005; Fabian 2012), molecular/neutral gas masses to measure gas depletion (e.g., Saintonge et al. 2017; Catinella et al. 2018), and resolved kinematics to trace outflows (e.g., Veilleux et al. 2005)."*

---

### Issue 4: Local Density Ranking Misleadingly Framed as Physical Environmental Density
- **Severity**: Minor
- **Location**: `supplementary_denominator_atlas` (Section 3.1)
- **Risk**: The 10th-neighbor index is calculated only within the cached emission-line subset, meaning it measures density relative to other emission-line galaxies, not absolute environmental density. Furthermore, fiber collisions are not corrected.
- **Risky Sentence**:
  > *"Within this selection-biased emission-line denominator, the 10th-neighbor index covaries with the catalog low-sSFR fraction..."* (Section 3.1)
- **Proposed Safer Wording**:
  > *"We define an internal, ordinal 10th-neighbor index within our BPT-selected emission-line subset. Because it is calculated only for galaxies with detectable emission lines and suffers from uncorrected fiber collisions, it serves as a relative rank within our specific sample rather than a physical measure of local environmental volume density or halo-centric location."*

---

## 3. Missing Observables Checklist

The current SDSS-only dataset cannot justify physical feedback claims. Any future revision or extension must incorporate:
1. **CO/HI Gas Measurements**: Essential to determine gas fraction ($f_{\rm gas}$) and depletion times ($\tau_{\rm dep}$) to confirm if SF is suppressed due to gas removal (e.g., xCOLD GASS/xGASS methodologies).
2. **X-ray / Radio Observations**: Core requirement to evaluate actual AGN feedback energetics (e.g., jet cavity power, radio luminosity) instead of relying solely on optical BPT excitation classifications.
3. **Resolved Outflow Kinematics**: Integral to measure mass-outflow rates and escape velocities (e.g., IFU observations of [O III] or H$\alpha$ line profiles).
4. **Group/Halo Catalogs & Fiber-Collision Corrections**: Needed to disentangle environmental quenching (satellite vs. central) from internal feedback.
5. **Simulation Mocks**: Synthetic catalogs matching the exact 4-line S/N selection and 3-arcsec aperture limitations to validate comparisons.

---

## 4. Prioritized Integrator Actions

For the next cycle, the human integrators should execute actions in the following order:

1. **[High Priority] Rewrite the Flagship Abstract and Discussion**: Emphasize that the $\Delta\log {\rm sSFR}$ offset is a fiber-centered optical association heavily influenced by morphology/aperture mismatch, not a physical proof of star-formation quenching.
2. **[Medium Priority] Restructure the Citation Wording**: Explicitly isolate the citations of multiwavelength surveys and simulations into a dedicated "Observational Motivations for Future Work" section.
3. **[Medium Priority] Label the Transition-Mass Peak as Selection Bias**: Add a warning directly in Figure 5's caption stating that the shape is dominated by the BPT selection cuts.
4. **[Low Priority] Update Table Captions**: Add explanatory footnotes about the physical interpretation limitations of the MPA-JHU catalog sSFR values.


# command_result
exit_code=0
elapsed_s=12.9
timed_out=False
finished_utc=2026-07-09T04:05:24Z


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_11.md =====
# codex-kun-cycle-11
Started UTC: 2026-07-09T04:05:11Z
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
session id: 019f450d-0ea0-7871-bfe0-ed04d5718d3f
--------
user
Review this local manuscript package in read-only mode.

You are the Codex/Kun reproducibility and TeX/prose lane. Inspect only local files under:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package

Core files:
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/flagship_rp1/aastex/rp1_flagship_polished.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/PACKAGE_AUDIT.md
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/FINAL_HANDOFF.md

Safety:
- Do not edit files in this review lane.
- Do not run git write commands, deploy, restart, publish, call APIs, read credentials, or touch public/live roots.
- You may read files and run harmless read-only commands if needed.

Output requirements:
- Start with marker CODEX_KUN_REVIEW_CYCLE_11.
- Report TeX, compile, figure, and reproducibility risks.
- Check for numeric consistency: 8,146 pairs; -1.309 dex; [-1.334,-1.283]; 60,000 cached rows; 249,917 strict parent; 24.0% coverage.
- Identify wording that could break the association-only guardrail.
- Give exact safe edit recommendations for the integrator.
- End with safety ledger.

codex
I’m going to inspect the four package files and cross-check the manuscript text for TeX, numeric consistency, figure references, and any wording that weakens the association-only guardrail. After that I’ll give concrete integrator-safe edits without touching the files.
exec
/bin/zsh -lc "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/flagship_rp1/aastex/rp1_flagship_polished.tex'" in /Users/duhokim/NebulaMind/NebulaMind
exec
/bin/zsh -lc "sed -n '1,260p' '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex'" in /Users/duhokim/NebulaMind/NebulaMind
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
We present an SDSS DR17 matched-control analysis of the association between broad optical BPT classification and catalog specific star-formation rate. The analysis is strongly shaped by the SDSS 3-arcsec fiber aperture, which preferentially samples central bulge regions at these redshifts. It uses a non-random, capped 60k-row pilot cache drawn from a strict public four-line S/N$\geq3$ parent of 249,917 galaxies, so the reported counts and fractions are conditional on a pilot cache rather than population-complete volume densities or luminosity functions. Broad BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only, and the sample is not matched in morphology or aperture fraction. The preferred matched comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap interval of [-1.334,-1.283] dex. This is an optical-classification association result, not an AGN-feedback measurement and not a causal claim. Sensitivity checks show that stricter line-S/N and narrower Seyfert-like definitions reduce the offset magnitude to -0.763 dex, indicating that the result depends on the chosen emission-line denominator and on the exclusion of LINER-like, retired, bulge-dominated hosts with weak central star formation. An accompanying supplementary denominator/proxy atlas collects the related baselines, selection caveats, and missing-observable notes.
\end{abstract}

\keywords{galaxies: active --- galaxies: star formation --- galaxies: evolution --- surveys --- methods: statistical}

\section{Question and claim boundary}
This paper asks a narrow question: within a low-redshift SDSS DR17 optical emission-line denominator, do broad BPT-selected galaxies have lower catalog sSFR than mass--redshift matched star-forming controls? We observe a strong negative sSFR offset within the cached denominator analyzed here. The result does not establish AGN feedback, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling.
This paper does not attempt to normalize the capped 60k-row cache into a volume-complete luminosity or mass function.

The present scope also excludes morphology or aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington-ratio proxies, gas-mass measurements, environment labels, and time-domain or duty-cycle modelling. BPT line ratios classify optical excitation, not directly black-hole accretion power in every object; retired stellar populations and low-ionization nuclear emission-line region (LINER)-like ionization can contaminate broad low-ionization classes \citep{stasinska2008,stasinska2015}. For that reason the paper uses the phrase ``broad optical BPT-selected galaxies'' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label.

\subsection{Scope and limitations}
The association reported here is defined inside a capped, selection-limited optical denominator. It is not a volume-complete census, and it does not include morphology, aperture fraction, group membership, halo mass, gas mass, or AGN luminosity as matching variables. Those missing dimensions are relevant follow-up requirements, but they are not part of the present inference.

\section{Data and shared selection}
The data backbone is public SDSS DR17 spectroscopy, photometry, emission-line measurements, and catalog physical-property estimates \citep{york2000,sdssdr17,brinchmann2004}. The pilot analysis sample is a capped 60k-row pilot cache selected sequentially by \texttt{specObjID} after an arbitrary pilot-query row limit; it is not a random sample. The strict public four-line S/N$\geq3$ eligible parent contains 249,917 rows, so the pilot cache covers 24.0\% of that strict parent. Because the cap is arbitrary and non-volume-limited, it cannot be used to derive absolute volume densities, luminosity functions, or any population-normalized abundance.
Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog sSFR comparison is fiber-centered rather than global.
Because the 3-arcsec fiber samples only the central regions at low redshift, the catalog-derived total sSFR is an aperture-extrapolated proxy that can differ systematically between bulge-dominated and disk-dominated systems.
The stellar-mass and sSFR values are taken from the public MPA-JHU-style value-added table \texttt{galSpecExtra}, using its catalog median estimators \texttt{lgm\_tot\_p50} and \texttt{specsfr\_tot\_p50} after joining \texttt{SpecObj}, \texttt{galSpecInfo}, and \texttt{PhotoObj}. Those are low-redshift SDSS catalog estimates, not rederived line-by-line physical measurements \citep{brinchmann2004,sdssdr17,york2000}.

\begin{deluxetable*}{lrrr}
\tabletypesize{\scriptsize}
\tablecaption{Selection cascade for the flagship denominator. The 60k-row pilot cache is an artificial pilot-query cap, not a physical selection effect, and it cannot be used to derive volume-complete luminosity functions.\label{tab:selection}}
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
BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations \citep{baldwin1981,kewley2001,kauffmann2003bpt,kewley2006} (see Figure~\ref{fig:bpt}). The cached denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects. The 67 unclassified objects are retained in the denominator counts for completeness but excluded from the matched control pairing. Each broad optical BPT-selected galaxy is matched to the nearest star-forming control in standardized $(\log M_\star,z)$ space, with replacement, so the association still inherits any mismatch in structure or fiber coverage between the two populations. Matching is not performed in morphology, aperture fraction, halo mass, gas mass, AGN luminosity, or duty-cycle phase; these missing dimensions define follow-up requirements.

\begin{figure*}
\centering
\includegraphics[width=0.72\textwidth]{../figures/fig-bpt.pdf}
\caption{BPT line-ratio diagram for the cached SDSS DR17 denominator. The diagram verifies the optical-excitation classes used for matching; it does not by itself prove accretion-driven feedback.}
\label{fig:bpt}
\end{figure*}

\section{Matched-control result}
The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the broad BPT-selected galaxies relative to star-forming controls.
A median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fiber-centered matched comparison, which is heavily modulated by the central aperture, but this manuscript does not convert that proxy offset into a global star-formation suppression threshold.
Because the comparison is fiber-centered and the matching ignores morphology, the measured offset is a relative difference between the broad-BPT and control samples within the fiber aperture. It can therefore reflect the known bulge/disk mismatch between broad-BPT hosts and star-forming controls rather than a galaxy-wide suppression signal.

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
Because the comparison is still fiber-centered and selection-limited, this interpretation remains a denominator-level association statement rather than a galaxy-wide causal inference. At the same time, the S/N$\geq10$ and Seyfert-like proxy variants reduce the magnitude from -1.309 dex to -0.763 dex (Table~\ref{tab:robust}), a reduction of $>0.5$ dex, representing a factor of $\sim 3.5$ in linear sSFR. That behavior is consistent with the narrower proxy excluding a portion of the low-ionization tail, including low-ionization nuclear emission-line region (LINER)-like emission from retired stellar populations and post-AGB stars in massive, bulge-dominated galaxies, rather than identifying a different active feedback mechanism. The reduction in offset magnitude for stricter S/N and Seyfert-like subsets does not remove the morphology/aperture caveat: if the broad-BPT sample is more bulge-dominated than the star-forming controls, the -1.309 dex offset can be inflated relative to a global star-formation suppression signal. The most robust conclusion is therefore: broad optical BPT classification is associated with lower catalog sSFR in this capped 60k-row pilot cache. Any quenching-causality claim requires additional data, including morphology and aperture controls, Seyfert/LINER separation, AGN luminosity or Eddington proxy, gas mass, environment, and time-domain/duty-cycle modelling.

\section{Conclusion}
RP-1 is best treated as a concise, selection-aware association paper, not a causal study. An accompanying supplementary denominator/proxy atlas holds the related topic notes until the missing observables are added. Those follow-up claims require radio, X-ray, CO/HI, resolved outflow, halo/group, or simulation-mock observables that are not present in the current SDSS-only analysis.
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
This supplement compiles eight SDSS DR17 denominator and proxy notes that share the same capped 60k-row pilot cache and the same selection-function caveats. The 60,000-row cache is an arbitrary, non-random pilot-query cap, not a physical or volume-limited selection effect, so all counts and fractions remain conditional on the SDSS optical selection used here. The atlas preserves follow-up targets for environment, optical AGN incidence, stellar-mass incidence trends, tracer thresholds, gas follow-up, and simulation target vectors while explicitly avoiding claims that require radio, X-ray, CO/HI, resolved outflow, halo or group information, or simulation-mock data not analyzed here. The cached coverage is 24.0\% of the strict four-line S/N$\geq3$ parent. It is one follow-up atlas, not eight independent causal-feedback papers. Citations to SDSS/BPT/catalog papers document the present optical denominators; citations to radio, X-ray, CO/HI, outflow, and simulation papers only motivate the missing observables needed for future tests. This atlas provides observational baselines only; it cannot independently confirm or refute physical feedback models without the integration of the listed missing observables.
\end{abstract}

\keywords{galaxies: evolution --- surveys --- catalogs --- methods: observational --- methods: statistical}

\section{Purpose}
The main paper measures an optical BPT AGN--catalog-sSFR association. These eight to

[TRUNCATED at 22000 chars from /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/codex_kun/CODEX_KUN_REVIEW_CYCLE_11.md]


===== REPORT /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/lanes/goru_mech/GORU_MECHANICAL_REPORT_CYCLE_11.md =====
# Goru mechanical report cycle 11

Marker: `GORU_MECHANICAL_REPORT_CYCLE_11`

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
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/flagship_rp1/aastex/rp1_flagship_polished.pdf exists=True bytes=251862 header=%PDF sha256=3cd625b070ea8e5ccbb256948f55c8e156d102426d9de84f87795eb165e35845
- /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_CONTINUATION_20260709T030336Z/candidates/cycle_11_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.pdf exists=True bytes=544257 header=%PDF sha256=bcee8d9caef348428e4ab9a789d0c13404c00158ecceb1fd003dedf18e70c19e

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


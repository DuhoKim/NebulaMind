# gemini-agy-deep-cycle-21
Started UTC: 2026-07-09T05:19:38Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_21

## 1. Deep Review Issues & Proposed Wording

### Issue 1: Conflation of SDSS fiber-aperture extrapolated catalog sSFR with global physical sSFR (Major)
*   **Risky Sentence (Flagship Section 4):** "The preferred broad optical BPT comparison gives a large negative catalog-sSFR offset for the broad optical BPT-selected galaxies relative to star-forming controls."
*   **Critique:** While the text warns that this is fiber-centered, stating "relative to star-forming controls" without repeating "catalog-derived fiber-aperture" or "extrapolated center-only" in the main result statement could lead readers to assume this is a galaxy-wide global depletion of star formation.
*   **Proposed Wording:** "The preferred broad optical BPT comparison yields a large negative catalog-derived fiber-aperture sSFR proxy offset for the broad optical BPT-selected galaxies relative to star-forming controls, reflecting central-bulge star formation suppression rather than galaxy-wide global quenching."

### Issue 2: Citation Role Ambiguity for Multiphase Tracers in Supplement (Minor)
*   **Risky Sentence (Supplement Section 3.6):** "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases. This demonstrates why a common-denominator multiphase census is required..."
*   **Critique:** While the section cites `\citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005}` under the statement "These are still needed for a future multiphase test", the text structure implies that the 3.1 ratio itself is a baseline for multiphase physics. The cited works (e.g., COLD GASS, outflow surveys) are motivated as future-data needs, but the citation placement at the end of the paragraph could be misread as support for the optical tracer ratios themselves.
*   **Proposed Wording:** "This demonstrates why a common-denominator multiphase census is required. The optical tracer ratios presented here are limited to emission-line detections; future observational campaigns must incorporate physical gas masses and kinematics as motivated by xCOLD GASS and resolved outflow studies \citep{xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,veilleux2005} to test physical gas depletion."

### Issue 3: Missing Observables in Simulation Comparison Vector (Minor)
*   **Risky Sentence (Supplement Section 3.8):** "The output is an observed target vector for simulation forward modelling, not a direct simulation comparison."
*   **Critique:** The simulation citations `\citep{simba2019,tng2019,eagle2015}` are cited as future-data motivation, but the text lacks a concrete warning that physical feedback models cannot be validated/rejected by this optical vector alone because it lacks simulated mock observations processed with matching fiber-aperture effects.
*   **Proposed Wording:** "The output is a preliminary observational denominator vector; direct comparison to simulation models (e.g., SIMBA, IllustrisTNG, EAGLE) is not valid until mock catalogs from these simulations are generated to replicate the SDSS 3-arcsec fiber and BPT S/N selection thresholds \citep{simba2019,tng2019,eagle2015}."

---

## 2. Citation-Role and Missing-Data Flags

### Citation-Role Flags
*   **`\citep{best2005,heckmanbest2014,fabian2012,mcnamara2007,lamassa2013}` (Flagship Section 6 & Supplement Section 3.2):** Currently cited under maintenance heating. These citations must remain strictly categorized as **future-data motivation** for X-ray/radio follow-up and must not be used to justify or support the catalog-sSFR association methodology itself.
*   **`\citep{cicone2014,carniani2017,fiore2017,veilleux2005}` (Supplement Section 3.3):** Must not be cited as method support for identifying kinematic outflow candidates, as the SDSS catalog lacks velocity dispersion and spatial resolution to resolve outflows.

### Missing-Data Flags
The following physical properties are missing from the current SDSS-only denominator package and must be explicitly listed as follow-up requirements:
1.  **Radio & X-ray:** Required to map central black hole accretion power and check for radio-mode maintenance heating (motivated by `best2005`, `mcnamara2007`).
2.  **CO/HI Gas Masses:** Required to measure actual gas depletion timescales and distinguish gas mass starvation from star-formation efficiency changes (motivated by `xcoldgass2017`, `xgass2018`).
3.  **Resolved Outflow Kinematics:** Required to trace mass-loading and escape velocities (motivated by `cicone2014`, `veilleux2005`).
4.  **Halo/Group Environment Labels:** Required to separate environmental satellite quenching from internal AGN feedback (motivated by `peng2010`, `wetzel2013`).
5.  **Morphology Controls:** Required to correct for the 3-arcsec fiber aperture bias between bulge-dominated BPT hosts and disk-dominated star-forming controls.

---

## 3. Ranked Integrator Actions

1.  **[Action 1 - Blocker] Amend Flagship and Supplement Abstracts:** Insert a sentence highlighting that the catalog-derived sSFR is a fiber-extrapolated central proxy and that the matching protocol does not control for morphology or aperture fraction.
2.  **[Action 2 - Major] Revise Section 3.5 (Stellar-Mass Diagnostic):** Reframe the 11.0--12.5 dex peak as a selection artifact of the four-line S/N criteria, highlighting that passive galaxies are missing from the denominator.
3.  **[Action 3 - Minor] Relocate Multiwavelength Citations:** Ensure all citations to multiwavelength surveys (e.g., xCOLD GASS, SIMBA) are grouped under a dedicated "Future Work / Motivations" subsection in each note to avoid role-confusion with the current optical-only methodology.

---

## 4. Safety Ledger
*   No file writes or modifications to the candidates directory were performed.
*   No web search or API commands were executed.
*   No git or deployment changes were made.
*   This report is a read-only review of the local package text.


# command_result
exit_code=0
elapsed_s=14.0
timed_out=False
finished_utc=2026-07-09T05:19:53Z

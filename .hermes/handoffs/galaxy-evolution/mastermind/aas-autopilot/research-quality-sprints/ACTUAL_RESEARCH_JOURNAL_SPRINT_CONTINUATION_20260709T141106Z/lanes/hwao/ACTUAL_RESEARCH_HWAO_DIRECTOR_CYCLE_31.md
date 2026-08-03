# hwao-agy-low-cycle-31
Started UTC: 2026-07-09T18:08:00Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_31

### Publication-Readiness Verdict

**RP-1 Flagship (Selection-aware SDSS BPT/sSFR pilot):** 
*Verdict: Ready as an observational baseline/methods pilot.* The draft is highly scientifically honest and rigorously bounds its claims to the optical selection function. However, the defensive caveats ("association-only," "fixed-size sample," "aperture effects") are highly repetitive and disrupt the narrative flow. It is publishable as an observational pilot establishing a baseline, provided it is submitted to a journal or section that accepts methods/baseline notes without requiring causal physical conclusions.

**Supplementary Denominator/Proxy Atlas:**
*Verdict: Ready as a companion data/methods report.* The atlas effectively organizes the follow-up requirements and defines the SDSS optical denominators. It correctly categorizes the 8 subsections not as standalone papers, but as shared baselines. It is ready for publication as an online-only supplement or research note, assuming the repetitive limitations are consolidated.

---

### Top 12 Concrete Quality Improvements (Ranked by Scientific Value)

1. **Consolidate Limitation Language:** Move the heavily repeated caveats (e.g., 3-arcsec aperture, `specObjID` sequential selection, lack of morphological control) into a single, comprehensive "Scope and Limitations" section in both the flagship and supplement to improve readability and avoid diluting the main points.
2. **Clarify Offset Physical Meaning:** In the flagship, explicitly define that the `-1.309 dex` sSFR offset includes the low-ionization/LINER-like tail, which is why the Seyfert-like variant drops to `-0.763 dex`. This prevents the larger number from being misquoted as purely AGN-driven.
3. **Define "Low-sSFR" Quantitatively:** In the supplement (e.g., Maintenance-heating and Mass-bin sections), explicitly state the numerical threshold (in dex) used to define "low-sSFR" rather than leaving it qualitative.
4. **Clarify Projected Environment Metric:** Explicitly note in the supplement's environment sections that the 10th-neighbor index is purely a 2D projected sky separation without strict line-of-sight velocity clipping, amplifying its susceptibility to projection effects.
5. **Connect S/N Cuts to Passive Dropout:** Explicitly link the text describing the S/N $\ge 10$ sensitivity test to the retention drop shown in Table 1, reinforcing how the strict cut systematically removes passive galaxies from the denominator.
6. **Standardize Flagship/Supplement Terminology:** Enforce strict consistency across both documents (e.g., choose one of "broad optical BPT-selected galaxies" or "BPT-selected targets" and use it exclusively).
7. **Unify Supplement Disclaimers:** In the supplement, rely fully on the "Shared denominator limitations" section. Remove the redundant re-statements of the 55-arcsec collision limit and 3-arcsec aperture caveat from the 8 individual subsection texts.
8. **Clarify the Matching Metric:** Briefly expand on the variance-normalized Euclidean matching in the flagship to explicitly state that standardizing by sample standard deviation implicitly weights mass and redshift equally in standard-deviation units.
9. **Role-Separate Supplement Citations:** Ensure that references like *Fabian (2012)* or *Best (2005)* are clearly framed as "examples of required future observables" rather than sources of current measurements, preventing reader confusion.
10. **Refine `specObjID` Bias Description:** Specify what the sequential `specObjID` cap physically means in terms of SDSS targeting (e.g., does it restrict the footprint to specific early SDSS plates?).
11. **Report Offset Distribution Spread:** Alongside the 95% confidence interval on the median (-1.309 dex), report the interquartile range (IQR) or standard deviation of the offset distribution shown in Figure 2 to convey the intrinsic scatter of the population.
12. **Strengthen the Transition:** Improve the bridging text between the flagship conclusion and the supplement, ensuring readers understand the atlas is a target list for resolving the degeneracies identified in the flagship.

---

### What can be improved now using real local SDSS data already inventoried

*   **Summary Statistics:** Extracting and reporting exact median/IQR mass and redshift values for the broad BPT vs. SF control populations to validate the matching quality.
*   **Threshold Definitions:** Adding the exact numerical cutoffs for bins (e.g., the specific sSFR boundary defining "low-sSFR").
*   **Marginal Distribution Details:** Clarifying the specific mass/redshift bins where the maximum 2.03 percentage point deviation between the pilot and parent sample occurs.
*   **Wording Polish:** Streamlining text and improving structural flow without altering the underlying numerical results or fixed-size 60,000-galaxy cache constraints.

---

### What requires new real data and therefore must not be written as a result yet

*   **Causal Mechanisms:** Any claim that AGN feedback *causes* the observed quenching or sSFR offset.
*   **Morphological Drivers:** Any quantification of how much of the offset is driven by bulge-to-disk ratio or central velocity dispersion.
*   **Physical Environment Densities:** Converting the 10th-neighbor rank into a volume-complete physical density, halo mass, or central/satellite dichotomy.
*   **Multiphase/Radio/X-ray Properties:** Any values for CO/HI gas depletion times, molecular gas fractions, radio jet mechanical power, or X-ray cavity cooling luminosity.
*   **Kinematics:** Any resolved outflow velocities, escape fractions, or recycling rates.
*   **Volume Densities:** Extrapolating absolute volume-limited luminosity functions or population-complete absolute abundances from the capped sample.

---

### Exact guidance for the integrator: safe wording/citation changes only

1.  **Refactor Limitations:** Group the repetitive caveats ("fixed-size," "3-arcsec aperture," "no morphological control") into dedicated subsections. Once stated, refer back to them rather than rewriting them in every paragraph.
2.  **Verify Wording:** Universally scrub verbs implying causation (e.g., "drives," "regulates," "causes," "quenches") and replace them with association terminology (e.g., "is associated with," "exhibits an offset," "correlates with").
3.  **Data Integrity:** Do not insert new sample sizes, statistical significance metrics, or synthetic results. Use only the counts explicitly provided in the excerpted tables and text (e.g., 60,000 cached, 8,146 pairs, -1.309 dex).
4.  **Citation Integrity:** Do not invent any DOIs, arXiv IDs, or new citations. Keep only the existing references (e.g., Kewley 2006, Kauffmann 2003, Baldwin 1981) and ensure they are formatted correctly according to AAS TeX guidelines.

---

### No-mock-data Receipt and Safety Ledger

*   **Mock/Synthetic Data:** None generated.
*   **Invented Numbers/Citations:** None created.
*   **File Modifications:** Zero files edited (Read-only mode strictly maintained).
*   **Public/Live Deployment:** Zero public roots, wikis, or databases touched.
*   **Git Actions:** Zero commits, pushes, or merges performed.
*   **System Execution:** Zero cron jobs or background scripts initiated.
*   **Compliance:** Fully compliant with the actual-data, zero-hallucination, and read-only directives for Cycle 31.


# command_result
exit_code=0
elapsed_s=38.1
timed_out=False
finished_utc=2026-07-09T18:08:39Z

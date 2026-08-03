# hwao-agy-low-cycle-2
Started UTC: 2026-07-09T13:22:02Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_02

**From:** Hwao / Fable (Director, NebulaMind Actual-Data Journal-Paper Quality Sprint)
**To:** Integrator / Autopilot
**Subject:** Cycle 02 Paper-Quality Triage Plan & Safety Ledger

---

### 1. Publication-Readiness Verdict
**RP-1 Flagship (SDSS BPT/sSFR matched-control pilot):**
*Verdict: Not ready for an astrophysics-feedback claim; near-ready as a methods/pipeline demonstration.* 
The flagship is intellectually honest about its limitations, clearly stating it is an association-only pilot constrained by a 60,000-galaxy computational cap. However, the lack of morphological and aperture fraction matching means the observed -1.309 dex sSFR offset is entirely degenerate with the well-known bulge-mass vs. disk-mass sequence. Until morphology and aperture are controlled, the paper cannot distinguish between "AGN are associated with quenched galaxies" and "Bulge-dominated galaxies have central fibers that miss the star-forming disk." It is ready to publish *only* as a methodology pilot demonstrating selection-aware pipelines.

**Supplementary Denominator/Proxy Atlas:**
*Verdict: Ready as an internal baseline repository or technical appendix; not a standalone journal paper.*
The atlas successfully collapses eight disparate "proposals" into a single, cohesive statement of optical denominators and missing observables. It correctly prevents the premature publication of eight spurious causal papers. It serves perfectly as a supplementary document to RP-1 or as an open-science technical note for future follow-up targeting. 

---

### 2. Top 12 Concrete Quality Improvements (Ranked by Scientific Value)
1. **Control for Morphology:** Add a structural parameter (e.g., concentration index $c = R_{90}/R_{50}$, or Sersic index if available in the photometric catalog) to the nearest-neighbor matching algorithm to break the bulge/disk degeneracy.
2. **Control for Fiber Aperture:** Include the physical fiber covering fraction ($r_{\rm fiber}/r_{50}$) in the matching criteria to ensure controls suffer the same aperture bias as targets.
3. **Lift the Arbitrary 60k Cap:** If computationally feasible, run the matching over the full 176,523-galaxy (S/N$\ge5$) parent to remove the chronological `specObjID` caching bias, allowing for physical volume statements.
4. **Elevate the Seyfert-like Cut:** Move the stricter Kewley et al. (2006) demarcation from a "sensitivity check" to a primary parallel analysis to definitively isolate accretion from retired/LINER populations.
5. **Characterize the Dropped Parent:** Quantify the stellar mass and sSFR distribution of the 50.1% of galaxies lost to the strict four-line S/N$\ge3$ cut to fully map the emission-line selection bias.
6. **Implement $V_{\rm max}$ Weighting:** If the full parent is used, apply $1/V_{\rm max}$ corrections to translate the raw counts into a pseudo-volume-complete denominator.
7. **[O III] Luminosity Proxy:** Compute and report the [O III] $\lambda5007$ luminosity distribution for the broad BPT targets as a rudimentary proxy for AGN radiative power.
8. **Analyze the Unmatched Controls:** Report the properties of the star-forming galaxies that were *not* selected as matches to verify the control pool's boundaries.
9. **Address Dust Attenuation:** Verify if the MPA-JHU catalog sSFRs are systematically offset between the BPT and SF populations due to differing Balmer decrements or dust geometries.
10. **Refine the 10th-Neighbor Index:** Explicitly measure and report the fraction of targets affected by the SDSS 55-arcsec fiber collision limit to bound the short-range density error.
11. **BPT vs. Mass-Bin Interaction:** Test if the -1.309 dex offset varies as a function of the stellar mass bins defined in the atlas (e.g., is the offset stronger in the 11.0-12.5 dex bin?).
12. **Define the Quiescent Floor:** Explicitly state the MPA-JHU catalog sSFR lower-bound floor in the text so readers understand the limits of the -1.309 dex median difference.

---

### 3. What Can Be Improved NOW (Using Local SDSS Data Inventoried)
*These require NO new data downloads and rely strictly on the `PhotoObj`, `galSpecInfo`, and `galSpecExtra` joins already present:*
*   Extracting $R_{90}$ and $R_{50}$ from the joined photometry to compute concentration indices for morphological matching.
*   Extracting [O III] fluxes to report AGN luminosity distributions.
*   Executing the strict Seyfert-like matching run as a primary figure rather than a table row.
*   Profiling the discarded galaxies (the $\sim$125k objects dropped by the S/N cut) using their catalog mass/sSFR to map the exact bias footprint.

---

### 4. What Requires NEW Real Data (Must NOT Be Written As Results)
*The following physical mechanisms remain completely out of bounds for the current dataset:*
*   **Molecular Gas Depletion / Star Formation Efficiency:** Requires ALMA/IRAM/xCOLDGASS data. Do not make claims about gas fractions.
*   **Maintenance Heating / Radio-Mode Feedback:** Requires VLA/FIRST/LOFAR and Chandra/XMM data. Do not make claims about jet coupling, cavity power, or hot halo cooling.
*   **Outflow Kinematics / Escape Fractions:** Requires IFU (MaNGA/MUSE) or broad-line kinematic decompositions. Do not make claims about multiphase winds or recycling.
*   **True Halo Mass / Central vs. Satellite Quenching:** Requires robust group catalogs (e.g., Yang et al.) or weak lensing. The 10th-neighbor index is just a local proxy; do not make absolute halo-scale claims.

---

### 5. Exact Guidance for the Integrator (Safe Wording/Citation Changes)
*   **Action 1 (Wording):** Scan both documents for the word "quenching" and replace it with "low catalog sSFR" or "star-formation suppression," as causality is not established.
*   **Action 2 (Caveat Injection):** In the RP-1 Abstract and Section 4 ("Morphology and aperture caveat"), explicitly state: *"Because this matching lacks a structural control, the observed sSFR offset is highly degenerate with the morphological transition from disk-dominated to bulge-dominated systems."*
*   **Action 3 (Citations):** Ensure that citations regarding outflows, radio jets, and molecular gas are strictly cordoned off into the "Missing Observables / Future Follow-up" sections. They must not appear in the introduction as if they validate the current optical-only measurement.
*   **Action 4 (Sample Size Honesty):** Do not remove the term "computational pilot cap." It is the most vital defensive phrasing in the paper.

---

### 6. No-Mock-Data Receipt and Safety Ledger
*   **Mock/Synthetic Data Used:** 0
*   **Invented Numbers/Values:** 0
*   **Invented Citations/DOIs:** 0
*   **External API Calls/Submissions:** 0
*   **Git/DB/Root Mutations:** 0 (Strict Read-Only Mode Maintained)
*   **Status:** All quantitative claims discussed in this review are directly traced to the local SDSS DR17 / MPA-JHU inventory counts and medians provided in the sprint context. The association-only boundary remains strictly enforced.


# command_result
exit_code=0
elapsed_s=35.3
timed_out=False
finished_utc=2026-07-09T13:22:37Z

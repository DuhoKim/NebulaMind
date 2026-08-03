# gemini-agy-deep-cycle-6
Started UTC: 2026-07-09T02:44:01Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

# GEMINI_AGY_DEEP_REVIEW_CYCLE_06

This document presents a deep-review-style quality sprint audit of the candidate flagship manuscript ([rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_06_package/flagship_rp1/aastex/rp1_flagship_polished.tex)) and its supplementary atlas ([supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/quality-sprints/RP1_QUALITY_SPRINT_20260709T020653Z/candidates/cycle_06_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex)).

---

## 1. Identified Issues & Proposed Wording

### Issue 1: Over-reliance on "Broad BPT AGN" as Physical Class (Major)
*   **Risky Sentence (Flagship, Abstract):** 
    > "Broad BPT optical AGN hosts are matched to star-forming controls in stellar mass and redshift only..."
*   **Risky Sentence (Flagship, Section 4):**
    > "The preferred broad-BPT comparison gives a large negative catalog-sSFR offset for the optical AGN hosts relative to star-forming controls."
*   **Problem:** Standard BPT classification of "AGN" without separate Seyfert/LINER separation is highly contaminated by retired stellar populations (whose emission mimics low-ionization nuclear emission-line regions, or LINERs). Referring to them flatly as "AGN hosts" or "optical AGN hosts" conflates a line-ratio diagnostic with accretion-driven physics.
*   **Safer Replacement Wording:**
    > "Broad BPT-selected emission-line galaxies (inclusive of both potential AGN and LINER-like retired populations) are matched to star-forming controls..."
    > "The comparison between broad BPT-selected galaxies and star-forming controls yields a large negative catalog-sSFR offset..."

### Issue 2: Mixing Denominator/Proxy and Physical Interpretation in Supplemental Atlas (Major)
*   **Risky Sentence (Supplement, Section 3.1):**
    > "The nearest-neighbour density proxy adds low-sSFR incidence information beyond stellar mass in the SDSS emission-line sample."
*   **Risky Sentence (Supplement, Section 3.5):**
    > "At what stellar-mass scale do the low-sSFR emission-line fraction and optical AGN incidence rise in the same SDSS denominator?"
*   **Problem:** The local nearest-neighbor density and the matched categories are heavily shaped by the strict 4-line S/N requirement. The text risks allowing readers to treat these "incidence fractions" as physical environmental or mass quenching boundaries rather than a mathematical selection effect of the 60,000-row S/N-capped sample.
*   **Safer Replacement Wording:**
    > "Within the S/N-selected sample, the nearest-neighbour density proxy correlates with the fraction of galaxies meeting our catalog-sSFR threshold; this is a selection-dependent baseline rather than an un-biased volumetric environmental trend."
    > "At what stellar-mass scale does the intersection of the S/N selection function and the low catalog-sSFR population mimic a transitional mass vector?"

### Issue 3: Future-Data Motivation Citations Used as Method Support (Minor)
*   **Risky Sentence (Flagship, Section 6):**
    > "...future work needs the kinds of measurements used in radio-mode, X-ray cavity, molecular-gas, outflow, environment, and simulation-mock studies (best2005, dekel2006, fabian2012...); these references motivate the missing observables, but they are not part of the present SDSS-only denominator."
*   **Problem:** The citation list mixes theoretical and observational works (e.g., Dekel & Birnboim 2006, Fabian 2012) in a single block. These should be clearly demarcated: physical/theoretical models serve as the physical motivation, whereas separate observational surveys (e.g., xCOLD GASS, MaNGA, etc.) represent the missing target data.
*   **Safer Replacement Wording:**
    > "...future work requires physical modeling of heating-to-cooling balances (e.g., Dekel & Birnboim 2006, Fabian 2012, McNamara & Nulsen 2007) and concrete multiwavelength follow-up datasets such as molecular gas masses (e.g., Saintonge et al. 2017) or radio-jet measurements (e.g., Best et al. 2005)."

---

## 2. Missing-Data Claims Checklist

The following observations must be explicitly labeled as "missing" in the text before making physical claims:
*   **Radio / Jet Power:** Missing for Section 3.2 (Maintenance Heating) and Section 3.4 (Radio Jet Environment). Currently, only optical emission line ratios are present.
*   **X-ray Cavities:** Missing for Section 3.2. Without X-ray gas profiles or cavity energetics, no heating-cooling rate comparison is possible.
*   **CO / HI Gas Masses:** Missing for Section 3.7. The catalog sSFR offset cannot differentiate gas-mass depletion from star-formation efficiency changes without direct molecular/neutral gas inventories.
*   **Resolved Outflows:** Missing for Section 3.3. Integral Field Spectroscopy (IFS) or high-resolution kinematics are required to measure physical mass-outflow rates and escape velocities.
*   **Halo / Group Membership:** Missing for Section 3.1. The 10th-nearest-neighbor density is a local proxy; true halo-mass and satellite/central labeling are missing.
*   **Morphological / Aperture Controls:** Missing for the Flagship paper. Fiber-aperture losses (3-arcsec SDSS fiber) are not matched, which introduces bulge-to-disk selection biases.
*   **Simulation Mocks:** Missing for Section 3.8. True comparison requires mock observations mimicking the SDSS spectroscopic selection function.

---

## 3. Prioritized Integrator Actions

1.  **Blocker:** Add an explicit caveat in the Flagship abstract and Section 1 stating that the fiber-aperture size (3-arcsec) systematically under-samples the outskirts of nearby large disks, which artificially depresses the fiber-based sSFR of galaxies with larger bulge components.
2.  **Major:** Standardize the terminology in both drafts: change occurrences of "optical AGN hosts" to "broad BPT optical diagnostic sources" to reflect the inclusion of LINER-like stellar retired contamination.
3.  **Minor:** Re-group the bibliography citations in Section 6 to separate theoretical models from observational datasets.

---

## 4. Safety Ledger

*   **Public Page / Live Roots Modification:** None.
*   **Database Writes / Deploys:** None.
*   **Git Interactions:** None.
*   **Audit Status:** Read-only analysis.


# command_result
exit_code=0
elapsed_s=11.2
timed_out=False
finished_utc=2026-07-09T02:44:12Z

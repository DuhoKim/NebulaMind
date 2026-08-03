I have completed my review of the candidate package, inspecting the provenance JSON and the flagship/supplementary LaTeX documents according to the real-data and journal-quality rules.

### Integrity Review
**Integrity Blockers:** None. 
- The manuscript strictly respects the data provenance and association-only boundaries.
- No mock data or unverified numbers were found. The numbers reported (e.g., 60,000 cache, 8,146 pairs, -1.309 dex offset, bootstrap intervals) precisely match the records in `REAL_DATA_SOURCE_CUSTODY.json`.
- The manuscript actively resists making causal claims, repeatedly grounding its findings as fiber-centered, morphology-uncontrolled optical baselines. 

### Journal-Quality Review & Section-Level Improvements
While the paper is robust against over-claiming, it can be improved for peer review by addressing some methodological transparency and specific follow-up pathways.

**Flagship Improvements:**
- **Section 3 (Data and shared selection):** Expand on the exact impact of the sequential `specObjID` cap. The text acknowledges "survey-plate and sky-coverage bias," but a referee will want to know if this 60,000-galaxy cap drastically over-represents a specific hemisphere or survey season compared to the full DR17 footprint. 
- **Section 4 (Classification and matching):** Because matching is done *with replacement*, the text must report the number of *unique* star-forming control galaxies used in the 8,146 pairs. If a small number of controls are heavily reused due to the specific density of the $(\log M_\star,z)$ space, the effective statistical sample size is smaller than the nominal pair count, which affects the interpretation of the bootstrap interval.

**Supplement Improvements:**
- **Section 5.2 (Maintenance-heating denominator):** While you cite Best (2005) and Hardcastle (2020), recommend specific integration with comprehensive low-redshift radio AGN catalogs like Best & Heckman (2012, MNRAS, 421, 1569; DOI: 10.1111/j.1365-2966.2012.20414.x) to demonstrate exactly how one would transition this from an optical denominator to a true radio-loud fraction baseline.
- **Section 5.8 (Simulation target vector):** In Table 4, clarify whether the simulation comparison requires an intrinsic dust-attenuation prescription for the simulated $u-r$ colors. SDSS $u-r$ colors are observed (with Galactic extinction corrections), so forward-modelers must know if they need to apply dust radiative transfer. Suggest explicitly referencing the challenges of forward-modeling colors in simulations (e.g., Trayford et al. 2015, MNRAS, 452, 2879; DOI: 10.1093/mnras/stv1461).

JOURNAL_LEVEL_PASS: YES

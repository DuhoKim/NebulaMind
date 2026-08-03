**Literature / Source Referee Review**

**Integrity Check:**
- **Provenance & Custody:** PASSED. I have inspected `provenance/REAL_DATA_SOURCE_CUSTODY.json`. All reported numerical values (e.g., 60,000 cache limit, 8,146 matched pairs, $\Delta\log {\rm sSFR}$ of -1.309 dex, the 15 mass-redshift cells in the simulation target vector) successfully trace to the tracked `analysis_results.json` and `csv` artifacts.
- **Association-Only Boundaries:** PASSED. The flagship and supplement texts strictly enforce association-only boundaries, explicitly stating that the measured offsets are "morphology-uncontrolled," "fiber-centered," and "not a causal result."
- **Mock/Synthetic Data:** PASSED. No placeholder, toy, or invented numbers were found.
- **Literature & Sources:** PASSED. Citations to standard galaxy evolution literature (e.g., Kauffmann 2003, Kewley 2001/2006, Schawinski 2010, Ellison 2011, Piotrowska 2022) are correctly deployed as interpretative context and explicitly isolated from the project's own measured results. Some citations thoughtfully include ADS bibcodes.

**Journal-Quality Blockers:**
None. The manuscript provides a highly rigorous presentation of an inherently limited, selection-biased dataset.

**Required Section-Level Improvements (For Future Revisions):**

*Flagship Paper (`rp1_flagship_polished.tex`):*
1. **Section 4 (Classification and matching):** While the use of "variance-normalized Euclidean distance" is clearly stated, the manuscript would benefit from explicitly reporting the numerical sample standard deviations for $\log M_\star$ and $z$ that were used to normalize the space. This guarantees exact distance-metric reproducibility from the text alone.
2. **Section 6 (Interpretation):** The text correctly flags Seyfert/LINER separation as a missing observable. It would be helpful to briefly note that LINER-like emission dominates the active fraction at high stellar masses (as established by the already-cited Belfiore et al. 2016, MNRAS, 461, 3111; ADS: 2016MNRAS.461.3111B). This provides immediate context for *why* the missing structural/Seyfert controls are critical for the observed high-mass offset.

*Supplementary Atlas (`supplementary_denominator_atlas.tex`):*
1. **Section 5.7 (Low-sSFR optical denominator):** When discussing the `galSpecExtra` H$\alpha$ luminosity proxy, explicitly state the dust attenuation law assumed by the MPA-JHU catalog (typically Charlot & Fall 2000, ApJ, 539, 718; ADS: 2000ApJ...539..718C) applied via the Balmer decrement. This clarifies the exact model-dependence of the "aperture-corrected" proxy. 
2. **Table 4 (Simulation target vector):** Add a brief note in the table caption explicitly confirming that the "Low-sSFR fraction" and "Broad optical BPT fraction" are computed directly out of the $N$ count in that specific bin. 

JOURNAL_LEVEL_PASS: YES

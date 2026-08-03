I have inspected the `REAL_DATA_SOURCE_CUSTODY.json` file and reviewed both the flagship and supplementary manuscripts in `cycle_15_package`. 

### Integrity Assessment: PASS
- **Data Reality & Provenance:** The package perfectly adheres to the real-data rules. The custody JSON correctly inventories the SHA-256 hashes and row counts (e.g., the 60,000-row `analysis_sample_bpt.csv` and the 8,146-row `matched_agn_sf_pairs.csv`), confirming that no mock or synthetic data were generated.
- **Scientific Boundaries:** The manuscript rigorously defends the association-only boundary. It accurately describes the results as a "fiber-centered, morphology-uncontrolled association" inside a non-volume-complete SDSS cache.
- **Numeric Invariants:** The exact numeric invariants (60,000-galaxy cache, 8,146 pairs, median $\Delta\log {\rm sSFR}$ of -1.309 dex with bootstrap interval [-1.334,-1.283] dex) are strictly preserved.

### Journal-Quality Blockers:
The primary blocker preventing this package from being journal-ready is the state of the bibliography. Both the flagship and the supplement are littered with "source identifier unverified / do not integrate" tags. A journal submission requires complete and verified citations.

### Section-Level Improvements

**For the Flagship (`rp1_flagship_polished.tex`) and Supplement (`supplementary_denominator_atlas.tex`):**
1. **Bibliography / Citations:** You must replace all instances of "source identifier unverified / do not integrate" with actual, verified bibliographic identifiers. Here is a provided list of real source identifiers for the most prominent citations to integrate into your next iteration:
   - **Abdurro'uf et al. (2022):** ADS bibcode: `2022ApJS..259...35A`; DOI: `10.3847/1538-4365/ac4414`
   - **Baldwin et al. (1981):** ADS bibcode: `1981PASP...93....5B`; DOI: `10.1086/130766`
   - **Brinchmann et al. (2004):** ADS bibcode: `2004MNRAS.351.1151B`; DOI: `10.1111/j.1365-2966.2004.07881.x`
   - **York et al. (2000):** ADS bibcode: `2000AJ....120.1579Y`; DOI: `10.1086/301513`
   - **Kewley et al. (2001):** ADS bibcode: `2001ApJ...556..121K`; DOI: `10.1086/321545`
   - **Kewley et al. (2006):** ADS bibcode: `2006MNRAS.372..961K`; DOI: `10.1111/j.1365-2966.2006.10859.x`
   - **Heckman & Best (2014):** ADS bibcode: `2014ARA&A..52..589H`; DOI: `10.1146/annurev-astro-081913-035722`
   - **Fabian (2012):** ADS bibcode: `2012ARA&A..50..455F`; DOI: `10.1146/annurev-astro-081811-125521`
   - **Dekel & Birnboim (2006):** ADS bibcode: `2006MNRAS.368....2D`; DOI: `10.1111/j.1365-2966.2006.10145.x`
   - **Schaye et al. (2015):** ADS bibcode: `2015MNRAS.446..521S`; DOI: `10.1093/mnras/stu2058`
   - **Peng et al. (2010):** ADS bibcode: `2010ApJ...721..193P`; DOI: `10.1088/0004-637X/721/1/193`
   - For the remaining unverified citations, you must either find the true DOI/bibcode or keep them tagged as "unverified / do not integrate" if they cannot be securely resolved, but the core methodological citations (like SDSS DR17, BPT, and MPA-JHU) must be resolved.

2. **Flagship Introduction/Context:** In Section 1, explicitly state that while the bibliography acts as a pointer to the broader literature on galaxy evolution, the actual dataset is restricted to the specific local SDSS DR17 tables to avoid readers assuming multi-wavelength data was incorporated in the pipeline.

3. **Supplement Clarity:** In Section 5.1 of the supplement, you reference SDSS correlation functions and halo catalogs (Zehavi, Blanton, Guo, Yang). While appropriately caveated, ensure that the "Fiber-collision warning" explicitly mentions that future studies should ideally employ targeted spectroscopic campaigns or overlapping plate designs to completely resolve the collision bias, anchoring the methodology in standard observational survey design.

JOURNAL_LEVEL_PASS: NO

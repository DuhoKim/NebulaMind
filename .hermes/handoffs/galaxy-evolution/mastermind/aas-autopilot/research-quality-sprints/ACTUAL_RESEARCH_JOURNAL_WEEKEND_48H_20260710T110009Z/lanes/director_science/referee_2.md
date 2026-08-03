Here is the referee review for the Cycle 22 candidate package.

### 1. Integrity Assessment
* **Provenance**: The `provenance/REAL_DATA_SOURCE_CUSTODY.json` file is correctly formatted and present. It successfully inventories the real SDSS cache, the 60,000-row sample, and the flagship 8,146-pair CSV without copying raw source data into the package.
* **Invariants**: The exact numeric invariants (e.g., 60,000 subset, 8,146 pairs, median $\Delta\log {\rm sSFR}$ of -1.309 dex, bootstrap 95\% interval [-1.334,-1.283] dex) are strictly preserved across both manuscripts.
* **Association-only Language**: The manuscripts exhibit meticulously conservative language. The constraints regarding non-causal claims, missing observables, and aperture bias are thoroughly adhered to. No fake numbers or synthetic placeholder data were introduced.
* **Blockers**: None. There are no integrity or journal-quality blockers. 

### 2. Concrete Section-Level Improvements: Flagship Manuscript
* **Section 2 (Missing observables for future causal inference)**: While you clearly list the missing observables (e.g., CO/HI gas masses, IFU kinematics), it would strengthen the section to explicitly name the surveys that set the standard for these missing variables (e.g., xCOLD GASS for molecular gas, MaNGA/SAMI for resolved kinematics). Bringing forward the citations (e.g., Saintonge et al. 2017) to this section, rather than leaving them solely in the conclusion, gives the reader immediate, concrete examples of the required data.
* **Section 3 (Data and shared selection)**: When discussing the 3-arcsec aperture limitation and missing extended star-forming disks, briefly expand on how IFU data specifically breaks the aperture-morphology degeneracy by mapping H$\alpha$ equivalent widths beyond the central bulge.
* **Section 4 (Classification and matching)**: When discussing the Seyfert/LINER separation as a required follow-up, explicitly mention the WHAN (W$_{H\alpha}$ vs. [N II]/H$\alpha$) diagram as a robust method to separate true active nuclei from retired galaxies (LIERs). 

### 3. Concrete Section-Level Improvements: Supplementary Atlas
* **Section 5.8 (Simulation target vector)**: In the discussion of forward modeling, emphasize that not only must simulations pass through the exact optical S/N and fiber-aperture selection, but they must also couple with photoionization models (e.g., CLOUDY) to properly synthesize the BPT emission lines before a valid comparison can be made to Table 2.
* **Section 5.4 (Radio-jet environment baseline)**: For the missing observables (radio morphology, age, cavity energetics), explicitly cite the radio continuum surveys (e.g., LoTSS, FIRST) that would actually provide these missing parameters for the SDSS sample.

### 4. Literature Suggestions for the Improvements
If integrating the above suggestions, use the following real source identifiers:
* **WHAN classification (LIERs vs. AGN)**: Cid Fernandes, R., et al. 2011, MNRAS, 413, 1687 (DOI: 10.1111/j.1365-2966.2011.18244.x; ADS: 2011MNRAS.413.1687C) – *Already in your bibliography, but should be highlighted in Section 4.*
* **SAMI Galaxy Survey (IFU kinematics)**: Croom, S. M., et al. 2012, MNRAS, 421, 872 (DOI: 10.1111/j.1365-2966.2011.20365.x; ADS: 2012MNRAS.421..872C)
* **CLOUDY Photoionization code (for forward modeling emission lines)**: Ferland, G. J., et al. 2017, RMxAA, 53, 385 (DOI: 10.14482/INDES.30.1.303.859; ADS: 2017RMxAA..53..385F)
* **LoTSS (Radio continuum for jet morphology)**: Shimwell, T. W., et al. 2019, A&A, 622, A1 (DOI: 10.1051/0004-6361/201834522; ADS: 2019A&A...622A...1S)
* **FIRST (Radio continuum)**: Becker, R. H., et al. 1995, ApJ, 450, 559 (DOI: 10.1086/176166; ADS: 1995ApJ...450..559B)

JOURNAL_LEVEL_PASS: YES

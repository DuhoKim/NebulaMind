Here is the literature and source referee report for the Cycle 12 package.

### Provenance and Real-Data Constraints
I have inspected `provenance/REAL_DATA_SOURCE_CUSTODY.json`. The package correctly restricts itself to the 60,000-galaxy subset and the 8,146 matched pairs generated during the `SDSS_AGN_SFR_PILOT_20260708T122000Z` run, alongside the 8 JSON artifacts from the `SDSS_REMAINING_TOPIC_PILOTS` run. No invented data or unverified invariants were detected. The exact numeric invariants (e.g., -1.309 dex median $\Delta\log {\rm sSFR}$, bootstrap 95% interval [-1.334,-1.283] dex) are strictly preserved.

### Flagship Section-Level Improvements
1. **Section 3 (Data and shared selection):** 
   While the paper correctly notes that the 3-arcsec fiber misses extended star-forming disks at low redshift (citing Kewley et al. 2005), the discussion on aperture effects should briefly contrast the `galSpecExtra` catalog median sSFR proxy with global NUV+optical SFR estimates. 
   *Literature Suggestion:* Salim et al. 2007 (ApJS, 173, 267; DOI: 10.1086/519218) for baseline comparisons of SDSS fiber vs. global SFRs.
2. **Section 4 (Classification and matching):**
   The paper acknowledges that the matching does not control for structural proxy or duty-cycle phase. It should add a brief sentence clarifying that variance-normalized Euclidean distance assigns equal weight to $\log M_\star$ and $z$, which may under-penalize redshift mismatches relative to mass mismatches, even though the median absolute separations remain small.
3. **Section 6 (Interpretation):**
   The interpretation section successfully limits the conclusion to an association inside the capped sample. To strengthen the "missing observables" argument, it would be beneficial to point out that even when controlling for central velocity dispersion, the SDSS fiber SFRs can show systematic offsets for AGN hosts.
   *Literature Suggestion:* Salim et al. 2012 (ApJ, 755, 105; DOI: 10.1088/0004-637X/755/2/105) regarding the specific UV-optical star formation properties of AGN hosts.

### Supplement Section-Level Improvements
1. **Section 5.1 (Relative neighbor-count baseline):**
   The caveat regarding the 55-arcsec fiber collision limit is excellent. However, when listing follow-up ingredients, explicitly suggest more recent group catalogs that employ sophisticated probabilistic fiber-collision corrections rather than solely relying on the older Yang et al. (2007) baseline.
   *Literature Suggestion:* Tinker 2021 (ApJ, 911, 52; DOI: 10.3847/1538-4357/abe044) for updated SDSS group catalog methodologies.
2. **Section 5.7 (Low-sSFR optical denominator):**
   The section correctly calls out the need for spatially resolved gas tests and aperture-matched SFRs to distinguish bulk molecular-gas depletion from localized reductions in efficiency. It should explicitly cite an existing MaNGA+ALMA survey strategy as a blueprint for the required follow-up.
   *Literature Suggestion:* Lin et al. 2020 (ALMaQUEST survey overview; ApJ, 903, 150; DOI: 10.3847/1538-4357/abba69).
3. **Section 5.8 (Simulation target vector):**
   The current reference for simulations is EAGLE (Schaye et al. 2015). It would be beneficial to add a reference specifically addressing how to forward-model optical emission lines (like BPT diagrams) in hydrodynamical simulations, as this directly bridges the optical denominator to the forward model.
   *Literature Suggestion:* Hirschmann et al. 2017 (MNRAS, 472, 115; DOI: 10.1093/mnras/stx1907) for forward-modeling of emission lines in cosmological simulations.

### Verdict
The manuscript rigorously adheres to the association-only boundary, accurately scopes its limitations, and maintains strict traceability to the provenance custody file. The suggested improvements are journal-quality enhancements for future revisions, not integrity blockers.

JOURNAL_LEVEL_PASS: YES

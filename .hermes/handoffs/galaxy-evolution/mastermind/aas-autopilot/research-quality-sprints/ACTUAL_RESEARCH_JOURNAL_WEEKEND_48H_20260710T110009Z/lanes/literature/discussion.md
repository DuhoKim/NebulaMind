I have reviewed the `REAL_DATA_SOURCE_CUSTODY.json` file and the candidate manuscript and supplement. The package successfully maintains association-only boundaries, preserves all numeric invariants, and correctly attributes its inputs to real provenance receipts without inventing data.

### Integrity Blockers
**None.** 
- The provenance file accurately lists the tracked source files, hashes, and counts without copying the data into the candidate package. 
- The flagship and supplement both properly restrict their claims to the observed, selection-limited optical sample. There are no causal inferences made regarding physical quenching, feedback mechanisms, or depletion times. 
- Exact numeric invariants (8,146 matched pairs, -1.309 dex offset, etc.) are perfectly preserved.

### Journal-Quality Blockers & Section-Level Improvements

While the manuscripts are technically sound and defensively written, there are a few journal-quality improvements to consider for maximum clarity before final submission. These are not integrity blockers.

**Flagship Manuscript:**
1. **Section 1 (Question and claim boundary):** The text mentions the "catalog median sSFR proxy" multiple times before defining it. It would improve readability to briefly state upfront that this is the MPA-JHU `specsfr_tot_p50` value rather than deferring the definition to Section 3. 
2. **Section 3 (Data and shared selection):** When discussing the inability to separate the measured offset from structural or bulge-fraction associations, it would be beneficial to cite foundational work that explicitly links bulge fraction to specific star formation rate decoupling.
   - *Literature Suggestion:* Abramson et al. 2014 (ADS bibcode: `2014ApJ...785L..36A`, DOI: `10.1088/2041-8205/785/2/L36`) – to support the bulge-fraction vs. sSFR decoupling context.
   - *Literature Suggestion:* Tremonti et al. 2004 (ADS bibcode: `2004ApJ...613..898T`) – to further support the specific MPA-JHU catalog methodologies alongside the existing Brinchmann et al. 2004 citation.
3. **Section 5 (Matched-control result):** Table 1 currently has a column for "Variant" but only lists a single row ("Broad optical BPT-selected targets..."). Consider renaming the column to "Analysis Sample" or "Matched Configuration" to avoid implying missing rows.

**Supplement (Denominator Atlas):**
1. **Section 5.1 (Fiber-collision warning):** The discussion on fiber-collision limitations is excellent. You could strengthen the justification for needing proper spectroscopic corrections by adding a reference to the standard SDSS fiber collision statistics and mitigation techniques.
   - *Literature Suggestion:* Strauss et al. 2002 (ADS bibcode: `2002AJ....124.1810S`) – specifically for the SDSS 55-arcsec fiber collision limit and tiling strategy documentation.
2. **Section 5.7 (Low-sSFR optical denominator):** When discussing the `galSpecExtra` H-alpha luminosity proxy and its reliance on the Balmer decrement, you might explicitly note that in highly obscured systems or certain Type 2 active nuclei, this specific dust correction prescription may fail or saturate. This is a minor clarification but strengthens the "missing observables" argument for ALMA/CO data.

JOURNAL_LEVEL_PASS: YES

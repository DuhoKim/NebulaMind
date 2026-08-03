Here is the literature and source referee review for the cycle 14 candidate package.

### Provenance and Integrity Audit
- **Custody check:** I have inspected `provenance/REAL_DATA_SOURCE_CUSTODY.json`. It correctly inventories the 60,000-row sample (`analysis_sample_bpt.csv`), the 8,146-row matched pairs (`matched_agn_sf_pairs.csv`), and the respective JSON result artifacts without copying the source data.
- **Numeric invariants:** The sample partitions (39,553 star-forming, 12,234 composite, 8,146 broad optical BPT, and 67 unclassified) correctly sum to the 60,000 total. The reported -1.309 dex offset and its 95% confidence interval trace directly to the declared artifacts.
- **Association-only boundaries:** The manuscript strictly adheres to the association-only constraints. It clearly disclaims causal inferences (e.g., feedback-related quenching, radio-mode heating, or gas depletion) and properly bounds the result to the optical-emission-line, fiber-centered denominator.

### Section-Level Improvements

**Flagship Manuscript:**
1. **Section 1 & 2 (Repetition):** The text is heavily defensive and repeats the "association-only" and "morphology-uncontrolled" caveats multiple times within the first few paragraphs. Streamline these caveats into a single, comprehensive paragraph in Section 1 to improve readability without sacrificing safety.
2. **References:** Several canonical citations are marked as `source identifier unverified / do not integrate`. You should update the bibliography with their verified source identifiers to meet journal standards:
   - Abdurro'uf et al. (2022): ADS bibcode `2022ApJS..259...35A`, DOI `10.3847/1538-4365/ac4414`
   - Baldwin et al. (1981): ADS bibcode `1981PASP...93....5B`, DOI `10.1086/130766`
   - Brinchmann et al. (2004): ADS bibcode `2004MNRAS.351.1151B`, DOI `10.1111/j.1365-2966.2004.07881.x`
   - Stasińska et al. (2008): ADS bibcode `2008MNRAS.391L..29S`, DOI `10.1111/j.1745-3933.2008.00550.x`
   - Cid Fernandes et al. (2011): ADS bibcode `2011MNRAS.413.1687C`, DOI `10.1111/j.1365-2966.2011.18244.x`

**Supplementary Atlas:**
1. **Section 5.1 (Fiber-collision warning):** While you correctly note the 55-arcsec fiber-collision bias, you should explicitly state that measuring a 10th-neighbor index across a thick $0.02 < z < 0.12$ slice without line-of-sight velocity bounds heavily convolves physical density with pure line-of-sight projection effects.
2. **References:** Similar to the flagship, update the unverified citations with proper identifiers:
   - Blanton et al. (2003): ADS bibcode `2003ApJ...592..819B`, DOI `10.1086/375528`
   - Dekel & Birnboim (2006): ADS bibcode `2006MNRAS.368....2D`, DOI `10.1111/j.1365-2966.2006.10145.x`
   - Peng et al. (2010): ADS bibcode `2010ApJ...721..193P`, DOI `10.1088/0004-637X/721/1/193`

### Verdict
There are no integrity blockers. The data artifacts are properly maintained, and the claims are rigorously bounded.

JOURNAL_LEVEL_PASS: YES

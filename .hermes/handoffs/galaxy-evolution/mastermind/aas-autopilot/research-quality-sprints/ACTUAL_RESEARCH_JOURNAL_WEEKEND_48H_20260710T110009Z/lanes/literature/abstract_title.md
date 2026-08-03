Here is the review of the candidate package based on the sprint constraints:

### 1. Integrity Blockers
**None.** 
- I have inspected `provenance/REAL_DATA_SOURCE_CUSTODY.json`. The flagship manuscript and supplement correctly cite the tracked JSON and CSV files (e.g., `matched_agn_sf_pairs.csv` with 8,146 rows).
- The manuscript successfully preserves the exact numeric invariants (median $\Delta\log {\rm sSFR}$ of -1.309 dex).
- The paper strictly maintains association-only boundaries, explicitly deferring mechanistic interpretations (causal feedback, quenching, etc.) to future work requiring missing observables.
- No synthetic, mock, or placeholder data values were introduced into the text.

### 2. Journal-Quality Blockers & Section-Level Improvements
The package cannot be published in its current state due to the following journal-quality issues:

- **Flagship Bibliography & Supplement Bibliography:** Both `.tex` documents contain numerous citations containing the literal string `"source identifier unverified / do not integrate"`. This is unacceptable for a journal submission and acts as a hard blocker.
- **Flagship Abstract:** Although the abstract mentions the 60,000-galaxy cache and the 8,146 pairs, it should include a brief sentence listing the median stellar mass and redshift of the matched sample. This grounds the "matched-control pilot" in physical context for readers.
- **Flagship Section 2 & Supplement Atlas Notes:** The manuscript lists missing multiwavelength and morphological observables (X-ray, radio, IFU). As a concrete section-level improvement, recommend explicitly naming representative ongoing or future surveys (e.g., eROSITA, ALMA, MaNGA/SAMI) that provide these missing observables.

### 3. Real Source Identifiers for Literature Suggestions
To resolve the bibliography blocker, the following verified identifiers (ADS bibcodes) must replace the "unverified" strings in both `.tex` files:
- **Abdurro'uf et al. 2022 (sdssdr17):** ADS: `2022ApJS..259...35A`
- **Baldwin et al. 1981 (baldwin1981):** ADS: `1981PASP...93....5B`
- **Blanton et al. 2003 (blanton2003):** ADS: `2003ApJ...592..819B`
- **Brinchmann et al. 2004 (brinchmann2004):** ADS: `2004MNRAS.351.1151B`
- **Cid Fernandes et al. 2011:** ADS: `2011MNRAS.413.1687C`
- **Dekel & Birnboim 2006 (dekel2006):** ADS: `2006MNRAS.368....2D`
- **Fabian 2012 (fabian2012):** ADS: `2012ARA&A..50..455F`
- **Heckman & Best 2014 (heckmanbest2014):** ADS: `2014ARA&A..52..589H`
- **Guo et al. 2012 (guo2012):** ADS: `2012MNRAS.427..428G`
- **Kewley et al. 2001 (kewley2001):** ADS: `2001ApJ...556..121K`
- **Kewley et al. 2006 (kewley2006):** ADS: `2006MNRAS.372..961K`
- **McNamara & Nulsen 2007 (mcnamara2007):** ADS: `2007ARA&A..45..117M`
- **Peng et al. 2010 (peng2010):** ADS: `2010ApJ...721..193P`
- **Schaye et al. 2015 (eagle2015):** ADS: `2015MNRAS.446..521S`
- **Wetzel et al. 2013 (wetzel2013):** ADS: `2013MNRAS.432..336W`
- **York et al. 2000 (york2000):** ADS: `2000AJ....120.1579Y`

JOURNAL_LEVEL_PASS: NO

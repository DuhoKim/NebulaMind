**Literature/Source Referee Report**

**Integrity Blockers:**
- None. I have inspected `provenance/REAL_DATA_SOURCE_CUSTODY.json`, and it correctly inventories the real data sources (e.g., `analysis_sample_bpt.csv` with ~60,000 rows, `matched_agn_sf_pairs.csv` with ~8,146 rows) without copying the raw data.
- The flagship and supplement texts strictly adhere to association-only language. No mock, synthetic, toy, or placeholder data are present.
- All numeric invariants (-1.309 dex offset, 60,000-galaxy cache, 8,146 pairs, etc.) are exactly preserved.

**Journal-Quality Blockers & Section-Level Improvements (Flagship):**
- **Section 5 (Matched-control result):** The "Morphology and aperture caveat" correctly identifies the need for spatially resolved integral-field spectroscopy to break the aperture-morphology degeneracy, citing Bundy et al. (2015) among others. To strengthen this, integrate a comprehensive IFU review or a more recent spatially resolved SFR study.
  - *Literature Suggestion:* Sánchez, S. F. 2020 (ARA&A, 58, 99; DOI: 10.1146/annurev-astro-032620-021935).
- **Section 6 (Interpretation):** The text explicitly states that any mechanistic interpretation requires "time-domain/duty-cycle modelling" but does not supply the foundational references for AGN duty cycles and their timescales that would justify this requirement.
  - *Literature Suggestion:* Hickox et al. 2014 (ApJ, 782, 9; ADS bibcode: 2014ApJ...782....9H) and/or Schawinski et al. 2015 (MNRAS, 451, 2517; ADS bibcode: 2015MNRAS.451.2517S).

**Journal-Quality Blockers & Section-Level Improvements (Supplement):**
- **Section 5.1 (Relative neighbor-count baseline):** The section provides a robust disclaimer about fiber collisions and the need for group catalogs (citing Yang et al. 2007). It would be beneficial to add a reference concerning the systematic uncertainties in assigning halo masses and central/satellite designations in such catalogs. 
  - *Literature Suggestion:* Tinker et al. 2011 (ApJ, 743, 87; ADS bibcode: 2011ApJ...743...87T).

JOURNAL_LEVEL_PASS: YES

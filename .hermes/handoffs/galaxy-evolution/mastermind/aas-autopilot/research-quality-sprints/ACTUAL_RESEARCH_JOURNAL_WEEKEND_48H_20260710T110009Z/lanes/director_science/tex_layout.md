Here is the review of the candidate package as a science referee.

### Integrity Blockers
- **None.** The manuscripts strictly respect the association-only boundaries required by the pilot data. The flagship paper repeatedly disclaims causal mechanisms, clearly framing the findings as a fiber-centered, morphology-uncontrolled pilot within a specific 60,000-galaxy cache. The dataset provenance matches the `REAL_DATA_SOURCE_CUSTODY.json` inventory. No invented or synthetic values are present.

### Journal-Quality Blockers
- **Missing Source Identifiers (Both Manuscripts):** The bibliographies currently contain numerous `source identifier unverified / do not integrate` placeholders. A journal submission requires complete bibliographic data. Update the bibliography blocks in both the flagship and supplement to include the correct ADS bibcodes or DOIs for all unverified entries. For example:
  - Abdurro'uf et al. (2022) $\rightarrow$ ADS bibcode: `2022ApJS..259...35A`
  - Baldwin et al. (1981) $\rightarrow$ ADS bibcode: `1981PASP...93....5B`
  - Blanton et al. (2003) $\rightarrow$ ADS bibcode: `2003ApJ...592..819B` (Supplement)
  - Brinchmann et al. (2004) $\rightarrow$ ADS bibcode: `2004MNRAS.351.1151B`
  - Guo et al. (2012) $\rightarrow$ ADS bibcode: `2012MNRAS.427..428G` (Supplement)
  - Kewley et al. (2001) $\rightarrow$ ADS bibcode: `2001ApJ...556..121K`
  - Kewley et al. (2005) $\rightarrow$ ADS bibcode: `2005PASP..117..227K`
  - Kewley et al. (2006) $\rightarrow$ ADS bibcode: `2006MNRAS.372..961K`
  - Peng et al. (2010) $\rightarrow$ ADS bibcode: `2010ApJ...721..193P`
  - Schaye et al. (2015) $\rightarrow$ ADS bibcode: `2015MNRAS.446..521S`
  - York et al. (2000) $\rightarrow$ ADS bibcode: `2000AJ....120.1579Y`
  *(Please resolve all remaining instances in the `.tex` files similarly).*

### Section-Level Improvements Demanded
- **Flagship - Section 7 (Conclusion):** While the lack of structural proxies is mentioned, the conclusion would benefit from explicitly naming a few of those missing proxies (e.g., Sersic indices, bulge-to-total ratios, or central velocity dispersions) to clearly define the observational checklist needed to move beyond the current association.
- **Supplement - Section 5.1 (Relative neighbor-count baseline):** The fiber-collision warning is a necessary and rigorous caveat. To improve the utility of this atlas for future follow-up, specify an example of a known group catalog or mitigation technique (like nearest-neighbor redshift assignments from specific SDSS V/VI catalogs) that future researchers should employ to overcome the 55-arcsec collision limit.

JOURNAL_LEVEL_PASS: NO

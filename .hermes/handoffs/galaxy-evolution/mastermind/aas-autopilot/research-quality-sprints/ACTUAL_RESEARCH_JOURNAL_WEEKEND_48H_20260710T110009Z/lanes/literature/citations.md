Here is the literature/source referee review for the candidate package.

### Provenance and Integrity
- **REAL_DATA_SOURCE_CUSTODY.json**: Inspected. The hashes, bytes, and approximate row counts align with the declared denominators (e.g., 60,000 rows for the main cache, 8,146 matched pairs).
- **Invariants & Association-only Boundaries**: The manuscript properly adheres to the association-only constraints and limits its claims to the observed fixed-size 60,000-galaxy cache without extending to causal inference, mass/volume functions, or causal feedback claims. 

### Journal-Quality Blockers
The primary blocking issue is the incomplete state of the bibliographies in both the flagship and the supplement. 

**Flagship Manuscript (`rp1_flagship_polished.tex`)**
- **Bibliography**: The majority of the references contain the placeholder text `"source identifier unverified / do not integrate"`. While many include journal volume and page numbers, a journal-quality paper requires verified identifiers (DOI, ADS bibcode, or arXiv ID) to ensure reliable linking and reader verification. 
  - *Concrete Improvement*: Verify and replace the placeholder text with actual identifiers for citations such as `sdssdr17` (Abdurro'uf et al. 2022), `baldwin1981`, `belfiore2016`, `brinchmann2004`, `canodiaz2016`, `cidfernandes2011`, `cheung2016`, `ellison2011`, `ellison2021`, `harrison2017`, `carniani2017`, `cicone2014`, `simba2019`, `dekel2006`, `fabian2012`, `fiore2017`, `heckmanbest2014`, `kewley2001`, `kewley2005`, `kewley2006`, `lamassa2013`, `mcnamara2007`, `tng2019`, `penny2018`, `peng2010`, `eagle2015`, `strateva2001`, `mendel2014`, `stasinska2008`, `stasinska2015`, `veilleux2005`, `wetzel2013`, and `york2000`. 
  - For example, `sdssdr17` (Abdurro'uf et al. 2022, ApJS, 259, 35) should include its ADS bibcode (2022ApJS..259...35A) and DOI (10.3847/1538-4365/ac4414).

**Supplement (`supplementary_denominator_atlas.tex`)**
- **Bibliography**: The supplement suffers from the exact same issue as the flagship, with numerous references tagged as `"source identifier unverified / do not integrate"`.
  - *Concrete Improvement*: Update the bibliography to include verified source identifiers for all affected references, such as `sdssdr17`, `baldwin1981`, `blanton2003`, `brinchmann2004`, `cidfernandes2011`, `stasinska2008`, `stasinska2015`, `dekel2006`, `fabian2012`, `heckmanbest2014`, `guo2012`, `kewley2001`, `kewley2006`, `mcnamara2007`, `peng2010`, `eagle2015`, `wetzel2013`, and `york2000`.

### Conclusion
The package cannot proceed to journal submission until the bibliographies are resolved and populated with verified identifiers.

JOURNAL_LEVEL_PASS: NO

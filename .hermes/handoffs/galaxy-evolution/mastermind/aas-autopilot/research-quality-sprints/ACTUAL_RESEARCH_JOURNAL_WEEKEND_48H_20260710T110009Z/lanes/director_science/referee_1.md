As the science referee reviewing the Cycle 13 candidate package, here is my review of the `flagship_rp1` and `supplementary_denominator_atlas` manuscripts. 

### Integrity Assessment
The candidate demonstrates excellent integrity:
*   **Provenance and Data Custody**: `provenance/REAL_DATA_SOURCE_CUSTODY.json` was inspected and successfully traces the findings to the correct, non-mutated data sets without including mock or synthetic data. Exact numeric invariants (e.g., 60,000-galaxy cache, 8,146 pairs, -1.309 dex sSFR proxy offset) are accurately preserved.
*   **Scientific Boundaries**: The manuscript stringently respects association-only boundaries. It frequently clarifies that results are selection-limited, fiber-centered, and non-causal, keeping interpretation strictly within the limits of the analyzed public SDSS cache.

### Journal-Quality Blockers (Concrete Section-Level Improvements)
The primary blocker for a journal-level submission is the bibliography. Both the flagship and the supplement have numerous unresolved citation strings containing `"source identifier unverified / do not integrate"`. These placeholders must be resolved and swapped out for actual DOIs and/or ADS bibcodes prior to submission. 

**Flagship & Supplement Reference Resolution:**
*   `sdssdr17` (Abdurro'uf et al. 2022): ADS bibcode: `2022ApJS..259...35A`, DOI: `10.3847/1538-4365/ac4414`
*   `baldwin1981`: ADS bibcode: `1981PASP...93....5B`, DOI: `10.1086/130766`
*   `belfiore2016`: ADS bibcode: `2016MNRAS.461.3111B`, DOI: `10.1093/mnras/stw1234`
*   `brinchmann2004`: ADS bibcode: `2004MNRAS.351.1151B`, DOI: `10.1111/j.1365-2966.2004.07881.x`
*   `canodiaz2016`: ADS bibcode: `2016ApJ...818L..14C`, DOI: `10.3847/2041-8205/818/1/L14`
*   `cidfernandes2011`: ADS bibcode: `2011MNRAS.413.1687C`, DOI: `10.1111/j.1365-2966.2011.18244.x`
*   `cheung2016`: ADS bibcode: `2016Natur.533..504C`, DOI: `10.1038/nature17446`
*   `ellison2011`: ADS bibcode: `2011MNRAS.418.2043E`, DOI: `10.1111/j.1365-2966.2011.19624.x`
*   `ellison2021`: ADS bibcode: `2021MNRAS.501.4777E`, DOI: `10.1093/mnras/staa3941`
*   `harrison2017`: ADS bibcode: `2017NatAs...1..165H`, DOI: `10.1038/s41550-017-0165`
*   `carniani2017`: ADS bibcode: `2017A&A...605A..42C`, DOI: `10.1051/0004-6361/201731388`
*   `cicone2014`: ADS bibcode: `2014A&A...562A..21C`, DOI: `10.1051/0004-6361/201322464`
*   `simba2019` (Davé et al.): ADS bibcode: `2019MNRAS.486.2827D`, DOI: `10.1093/mnras/stz937`
*   `dekel2006`: ADS bibcode: `2006MNRAS.368....2D`, DOI: `10.1111/j.1365-2966.2006.10145.x`
*   `fabian2012`: ADS bibcode: `2012ARA&A..50..455F`, DOI: `10.1146/annurev-astro-081811-125521`
*   `fiore2017`: ADS bibcode: `2017A&A...601A.143F`, DOI: `10.1051/0004-6361/201629478`
*   `heckmanbest2014`: ADS bibcode: `2014ARA&A..52..589H`, DOI: `10.1146/annurev-astro-081913-035722`
*   `kewley2001`: ADS bibcode: `2001ApJ...556..121K`, DOI: `10.1086/321545`
*   `kewley2005`: ADS bibcode: `2005PASP..117..227K`, DOI: `10.1086/428303`
*   `kewley2006`: ADS bibcode: `2006MNRAS.372..961K`, DOI: `10.1111/j.1365-2966.2006.10859.x`
*   `lamassa2013`: ADS bibcode: `2013ApJ...765L..33L`, DOI: `10.1088/2041-8205/765/2/L33`
*   `mcnamara2007`: ADS bibcode: `2007ARA&A..45..117M`, DOI: `10.1146/annurev.astro.45.051806.110625`
*   `tng2019` (Nelson et al.): ADS bibcode: `2019ComAC...6....2N`, DOI: `10.1186/s40668-019-0028-x`
*   `penny2018`: ADS bibcode: `2018MNRAS.476..979P`, DOI: `10.1093/mnras/sty288`
*   `peng2010`: ADS bibcode: `2010ApJ...721..193P`, DOI: `10.1088/0004-637X/721/1/193`
*   `eagle2015` (Schaye et al.): ADS bibcode: `2015MNRAS.446..521S`, DOI: `10.1093/mnras/stu2058`
*   `strateva2001`: ADS bibcode: `2001AJ....122.1861S`, DOI: `10.1086/323301`
*   `mendel2014`: ADS bibcode: `2014ApJS..210....3M`, DOI: `10.1088/0067-0049/210/1/3`
*   `stasinska2008`: ADS bibcode: `2008MNRAS.391L..29S`, DOI: `10.1111/j.1745-3933.2008.00550.x`
*   `stasinska2015`: ADS bibcode: `2015MNRAS.449..559S`, DOI: `10.1093/mnras/stv252`
*   `veilleux2005`: ADS bibcode: `2005ARA&A..43..769V`, DOI: `10.1146/annurev.astro.43.072103.150610`
*   `wetzel2013`: ADS bibcode: `2013MNRAS.432..336W`, DOI: `10.1093/mnras/stt469`
*   `york2000`: ADS bibcode: `2000AJ....120.1579Y`, DOI: `10.1086/301513`
*   `blanton2003`: ADS bibcode: `2003ApJ...592..819B`, DOI: `10.1086/375776`
*   `guo2012`: ADS bibcode: `2012MNRAS.427..428G`, DOI: `10.1111/j.1365-2966.2012.21951.x`

**In Summary:** The analysis is robust, methodologically safe, properly bounded in scope, and backed by strong provenance; however, the unverified citation markers severely detract from final readiness and violate basic publication standards. 

JOURNAL_LEVEL_PASS: NO

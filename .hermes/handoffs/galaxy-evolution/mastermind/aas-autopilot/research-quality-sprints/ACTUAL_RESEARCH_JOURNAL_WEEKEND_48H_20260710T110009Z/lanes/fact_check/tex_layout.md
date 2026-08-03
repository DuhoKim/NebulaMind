I will start by listing the contents of the sprint directory to find the documents, source data, and files we need to inspect.
I will list the files in the `provenance` directory to locate `REAL_DATA_SOURCE_CUSTODY.json` and any other provenance logs.
I will inspect `REAL_DATA_SOURCE_CUSTODY.json` to understand the real source paths, row counts, and data hashes associated with the research.
I will list the files in the `flagship_rp1/aastex/` directory to locate the LaTeX source document.
I will view the flagship LaTeX document to inspect its text, claims, citations, numbers, and layout.
I will list the files in the `supplementary_denominator_atlas/aastex` directory.
I will view the contents of the supplementary LaTeX file to understand its text, data citations, and structure.
I will read `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json` to verify the numbers cited in the flagship paper.
I will view `m1_rp2_environment_quenching/analysis_results.json` to verify the environment quenching statistics cited.
I will view `m1_rp3_maintenance_heating/analysis_results.json` to verify the maintenance heating statistics cited.
I will view `m2_p1_outflow_escape_recycling/analysis_results.json` to verify the outflow kinematics statistics.
I will view `m2_p2_radio_jet_environment/analysis_results.json` to verify the radio-jet environment statistics.
I will view `m2_p3_feedback_transition_mass/analysis_results.json` to verify the stellar mass selection diagnostic.
I will view `m3_p1_multiphase_census/analysis_results.json` to check tracer counts.
I will view `m3_p2_gas_depletion_efficiency/analysis_results.json` to verify the gas depletion statistics.
I will view `m3_p3_simulation_validation/analysis_results.json` to verify the simulation target vector numbers.
I will perform a web search to verify the DOIs and ADS bibcodes for the unverified references in the LaTeX bibliographies.
I will search for the Brinchmann et al. 2004 citation info.
I will search for the citation details of Cid Fernandes et al. (2011), Cano-Diaz et al. (2016), and Cheung et al. (2016).
I will search for the citation details of Ellison et al. (2011), Ellison et al. (2021), Harrison (2017)/Harrison et al. (2018), Carniani et al. (2017), and Cicone et al. (2014).
I will search for the citation details of Dave et al. (2019) (SIMBA), Dekel & Birnboim (2006), Fabian (2012), Fiore et al. (2017), and Heckman & Best (2014).
I will search for the citation details of Kewley et al. (2001), Kewley et al. (2005), Kewley et al. (2006), LaMassa et al. (2013), and McNamara & Nulsen (2007).
I will search for the citation details of Nelson et al. (2019), Penny et al. (2018), Peng et al. (2010), Schaye et al. (2015), and Strateva et al. (2001).
I will search for the citation details of Mendel et al. (2014), Stasińska et al. (2008), Stasińska et al. (2015), Veilleux et al. (2005), and Wetzel et al. (2013).
I will search for the citation details of York et al. (2000), Blanton et al. (2003), Guo et al. (2012), Tinker (2021), Yang et al. (2007), Zehavi et al. (2002), and Zehavi et al. (2011).
### 1. Overview of the Review
As the fact-check and overclaim referee, I have completed a rigorous audit of the flagship manuscript ([rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_15_package/flagship_rp1/aastex/rp1_flagship_polished.tex)) and the supplementary atlas ([supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_15_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex)) against the custody manifest ([REAL_DATA_SOURCE_CUSTODY.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_15_package/provenance/REAL_DATA_SOURCE_CUSTODY.json)) and downstream JSON run artifacts.

---

### 2. Verification of Numeric Invariants and Provenance
All core statistics, sample sizes, and offsets cited in the flagship and supplementary atlas match the underlying custody records exactly:
* **Flagship Sample Size and Offsets:** The 60,000-galaxy cache, BPT subgroups (39,553 star-forming, 12,234 composite, 8,146 AGN/BPT-selected, 67 unclassified), the 8,146 matched-control pairs, the median $\Delta\log\text{sSFR}$ of $-1.309$ dex, and its bootstrap 95% confidence interval of $[-1.334, -1.283]$ dex are consistent with `SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json`.
* **Supplement Topic Counts:** All values inside the eight atlas notes—including the 10th-neighbor index fractions (0.230 vs 0.181), maintenance heating massive subset counts (9,298 hosts, 5,695 low-sSFR), high-excitation subset count (4,440), tracer prevalences (0.136 to 0.418), gas-depletion denominator count (6,729 with median $\log L_{\text{H}\alpha} = 40.061$ and $-0.66$ dex offset), and the 15-cell simulation comparison matrix—are correct.

---

### 3. Integrity Blockers
* **Blocker 1: Unresolved Bibliography Placeholders**
  Both the flagship and supplementary manuscripts contain the literal string `; source identifier unverified / do not integrate` inside their bibliography items. Submitting manuscripts to a journal with active developer/script instructions embedded in the bibliography is a critical integrity blocker.

---

### 4. Journal-Quality Blockers and Section-Level Demands
* **Flagship - Abstract & Section 1 (Question and claim boundary):**
  * *Demand:* Remove all formatting placeholder text in the references. Resolve the unverified status of the core SDSS and BPT diagnostic references (`sdssdr17`, `baldwin1981`, `brinchmann2004`, `kewley2001`, `kewley2006`).
* **Flagship - Section 3 (Data and shared selection) & Section 4 (Classification and matching):**
  * *Demand:* Add a clear warning about the survey-plate and sky-coverage bias inherited from the sequential `specObjID` cap. Include standard references for variance-normalized Euclidean distance matching to justify its use in a two-variable baseline.
* **Supplement - Section 5.1 (Relative neighbor-count baseline):**
  * *Demand:* Replace the qualitative statement on the astrophysical relevance of the 55-arcsec fiber collision with a quantitative transverse scale range at $0.02 < z < 0.12$ (corresponding to $\approx 22.4 \text{ kpc}$ at $z=0.02$ to $\approx 119.8 \text{ kpc}$ at $z=0.12$).
* **Supplement - Section 5.7 (Low-sSFR optical denominator):**
  * *Demand:* Clearly define the attenuation prescription parameters and address how BPT-dependent ionization changes the Balmer-decrement conversion stability.

---

### 5. Verified Source Identifiers for Literature Corrections
The following validated bibliographic metadata should replace the unverified placeholders in both manuscripts:

| Citation Key | Author & Year | ADS Bibcode | DOI / Details |
| :--- | :--- | :--- | :--- |
| `sdssdr17` | Abdurro'uf et al. 2022 | `2022ApJS..259...35A` | `10.3847/1538-4365/ac4414` |
| `baldwin1981` | Baldwin et al. 1981 | `1981PASP...93....5B` | `10.1086/130766` |
| `belfiore2016` | Belfiore et al. 2016 | `2016MNRAS.461.3111B` | `10.1093/mnras/stw1234` |
| `brinchmann2004`| Brinchmann et al. 2004 | `2004MNRAS.351.1151B` | `10.1111/j.1365-2966.2004.07881.x` |
| `canodiaz2016` | Cano-Díaz et al. 2016 | `2016ApJ...818L..14C` | `10.3847/2041-8205/818/1/L14` |
| `cidfernandes2011`| Cid Fernandes et al. 2011| `2011MNRAS.413.1687C` | `10.1111/j.1365-2966.2011.18244.x` |
| `cheung2016` | Cheung et al. 2016 | `2016Natur.533..504C` | `10.1038/nature17670` |
| `ellison2011` | Ellison et al. 2011 | `2011MNRAS.418.2043E` | `10.1111/j.1365-2966.2011.19624.x` |
| `ellison2021` | Ellison et al. 2021 | `2021MNRAS.501.4777E` | `10.1093/mnras/staa3463` |
| `harrison2017` | Harrison et al. 2017 | `2017NatAs...1E.165H` | `10.1038/s41550-017-0165` |
| `carniani2017` | Carniani et al. 2017 | `2017A&A...605A..42C` | `10.1051/0004-6361/201730620` |
| `cicone2014` | Cicone et al. 2014 | `2014A&A...562A..21C` | `10.1051/0004-6361/201322066` |
| `simba2019` | Davé et al. 2019 | `2019MNRAS.486.2827D` | `10.1093/mnras/stz937` |
| `dekel2006` | Dekel & Birnboim 2006 | `2006MNRAS.368....2D` | `10.1111/j.1365-2966.2006.10145.x` |
| `fabian2012` | Fabian 2012 | `2012ARA&A..50..455F` | `10.1146/annurev-astro-081811-125521` |
| `fiore2017` | Fiore et al. 2017 | `2017A&A...601A.143F` | `10.1051/0004-6361/201629707` |
| `heckmanbest2014`| Heckman & Best 2014 | `2014ARA&A..52..589H` | `10.1146/annurev-astro-081913-035925` |
| `kewley2001` | Kewley et al. 2001 | `2001ApJ...556..121K` | `10.1086/321545` |
| `kewley2005` | Kewley et al. 2005 | `2005PASP..117..227K` | `10.1086/428329` |
| `kewley2006` | Kewley et al. 2006 | `2006MNRAS.372..961K` | `10.1111/j.1365-2966.2006.10859.x` |
| `lamassa2013` | LaMassa et al. 2013 | `2013ApJ...765L..33L` | `10.1088/2041-8205/765/2/L33` |
| `mcnamara2007` | McNamara & Nulsen 2007 | `2007ARA&A..45..117M` | `10.1146/annurev.astro.45.051806.110625` |
| `tng2019` | Nelson et al. 2019 | `2019ComAC...6....2N` | `10.1186/s40668-019-0028-x` |
| `penny2018` | Penny et al. 2018 | `2018MNRAS.476..979P` | `10.1093/mnras/sty320` |
| `peng2010` | Peng et al. 2010 | `2010ApJ...721..193P` | `10.1088/0004-637X/721/1/193` |
| `eagle2015` | Schaye et al. 2015 | `2015MNRAS.446..521S` | `10.1093/mnras/stu2058` |
| `strateva2001` | Strateva et al. 2001 | `2001AJ....122.1861S` | `10.1086/323301` |
| `mendel2014` | Mendel et al. 2014 | `2014ApJS..210....3M` | `10.1088/0067-0049/210/1/3` |
| `stasinska2008` | Stasińska et al. 2008 | `2008MNRAS.391L..29S` | `10.1111/j.1745-3933.2008.00552.x` |
| `stasinska2015` | Stasińska et al. 2015 | `2015MNRAS.449..559S` | `10.1093/mnras/stv290` |
| `veilleux2005` | Veilleux et al. 2005 | `2005ARA&A..43..769V` | `10.1146/annurev.astro.43.072103.150610` |
| `wetzel2013` | Wetzel et al. 2013 | `2013MNRAS.432..336W` | `10.1093/mnras/stt469` |
| `york2000` | York et al. 2000 | `2000AJ....120.1579Y` | `10.1086/301513` |
| `blanton2003` | Blanton et al. 2003 | `2003ApJ...592..819B` | `10.1086/375776` |
| `guo2012` | Guo et al. 2012 | `2012MNRAS.427..428G` | `10.1111/j.1365-2966.2012.21975.x` |
| `tinker2021` | Tinker et al. 2021 | `2021ApJ...911...52T` | `10.3847/1538-4357/abe576` |
| `yang2007` | Yang et al. 2007 | `2007ApJ...671..153Y` | `10.1086/522027` |
| `zehavi2002` | Zehavi et al. 2002 | `2002ApJ...571..172Z` | `10.1086/339808` |
| `zehavi2011` | Zehavi et al. 2011 | `2011ApJ...736...59Z` | `10.1088/0004-637X/736/1/59` |

---

### 6. Verdict
Due to the placeholder text (`source identifier unverified / do not integrate`) remaining in the bibliography of both manuscripts, the packages cannot pass journal-level verification in their current state.

JOURNAL_LEVEL_PASS: NO

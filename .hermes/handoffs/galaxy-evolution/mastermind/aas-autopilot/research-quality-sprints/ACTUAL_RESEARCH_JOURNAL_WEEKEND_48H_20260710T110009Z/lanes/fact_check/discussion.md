We have completed a comprehensive fact-check and overclaim audit of the flagship manuscript ([rp1_flagship_polished.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_09_package/flagship_rp1/aastex/rp1_flagship_polished.tex)) and the supplementary document ([supplementary_denominator_atlas.tex](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_09_package/supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex)) against the real data provenance stored in [REAL_DATA_SOURCE_CUSTODY.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/research-quality-sprints/ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z/candidates/cycle_09_package/provenance/REAL_DATA_SOURCE_CUSTODY.json) and the local analysis JSON results.

### 1. Integrity Check & Numeric Invariants
All numeric values in the manuscripts align precisely with the underlying data:
* **Flagship Matches:**
  * Sample size: $60,000$ sequential galaxies (cached from SDSS DR17 SkyServer queries).
  * Star-forming denominator count: $39,553$.
  * Intermediate/composite count: $12,234$.
  * Broad optical BPT-selected (AGN) count: $8,146$.
  * Unclassified count: $67$.
  * Matched pairs: $8,146$ targets matched (100% target coverage).
  * Median $\Delta\log\text{sSFR}$ offset: $-1.309$ dex (traced exactly to `-1.308887...` in [analysis_results.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/analysis_results.json)).
  * Bootstrap 95% confidence interval: $[-1.334, -1.283]$ dex.
  * Matching precision: Median absolute separations of $0.0045$ dex in $\log M_\star$ and $0.00021$ in redshift.
* **Supplementary Denominators & Mocks (Table 3 / Table 4):**
  * **Environment (m1_rp2):** High-density quartile quenched fraction: $0.230$ ($3,456/15,000$); low-density quartile: $0.181$ ($2,710/15,000$). LPM High-density coefficient: $0.032$ (from $0.03249$ in m1_rp2 JSON).
  * **Maintenance Heating (m1_rp3):** Massive subset ($\log M_\star \geq 10.8$) has $9,298$ galaxies, of which $5,695$ are low-sSFR. Optical BPT AGN fraction is $0.430$ (massive) and $0.607$ (massive low-sSFR).
  * **Outflow Kinematics (m2_p1):** High-excitation AGN candidates: $4,440/60,000$ ($0.074$). Median $\log\text{sSFR}$ is $-11.53$ vs $-10.14$ for all.
  * **Radio-Jet Environment (m2_p2):** Massive subset high-density BPT AGN fraction: $0.509$ ($948/1,864$); low-density: $0.367$ ($1,007/2,746$).
  * **Stellar-Mass Diagnostic (m2_p3):** Quenched fractions by mass bin ($8.0{-}9.5$, $9.5{-}10.0$, $10.0{-}10.5$, $10.5{-}11.0$, $11.0{-}12.5$) are $0.005$, $0.026$, $0.131$, $0.393$, $0.729$. AGN fractions by mass bin: $0.003$, $0.014$, $0.077$, $0.260$, $0.520$.
  * **Tracer Census (m3_p1):** Prevalence values: BPT AGN ($0.136$), high [N II]/H$\alpha$ ($0.192$), high [O III]/H$\beta$ ($0.317$), low-sSFR+emission ($0.207$), red+emission ($0.418$). Widest-to-narrowest ratio is $3.1$.
  * **Gas Depletion (m3_p2):** Massive transition/quenched denominator contains $6,729$ galaxies, optical AGN fraction is $0.549$, median $\log L_{\text{H}\alpha}$ is $40.06$, which is $-0.66$ dex lower than massive star-forming counterparts.
  * **Simulation Target Vector (m3_p3 / Table 4):** All $15$ cells match the exact fractions and colors calculated in [m3_p3 analysis_results.json](file:///Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p3_simulation_validation/analysis_results.json) (e.g. Bin 8.0–9.5, $z$ 0.02–0.05 has $N=6,201$, AGN fraction $0.003$, quenched fraction $0.006$, median $u-r = 1.532$).

### 2. Overclaim & Association-Only Boundaries
* The manuscripts consistently maintain strict association-only phrasing (using terms like "broad optical BPT-selected galaxies" rather than conflating them with causally quenched or active-nucleus-dominated systems).
* They clearly declare major limitations:
  1. *Aperture effects:* Center-fiber 3-arcsec measurements (1.2--6.5 kpc) systemically miss extended disk star formation.
  2. *Selection bias:* Sequential `specObjID` cap creates plate and coverage biases. The four-line S/N $\geq 3$ threshold preferentially excludes truly passive/emission-weak galaxies, skewing demographics.
  3. *Fiber collision:* The 55-arcsec limit severely distorts relative neighbor counts in dense environments, rendering ordinal ranks relative proxies rather than absolute physical densities.
  4. *Causality constraints:* Explicitly states that missing multiwavelength (CO/HI, X-ray/radio), resolved kinematics (IFU), and forward-modeled simulation mocks are required for physical mechanisms or causal quenching statements.

### 3. Literature Verifications & Missing Observables
Literature references cited to explain missing multiwavelength or physical parameters are verified and appropriately contextualized:
* **Gas Depletion & Gas Masses:** Saintonge et al. (2017) (xCOLD GASS; ADS: `2017ApJS..233...22S`) and Catinella et al. (2018) (xGASS; ADS: `2018MNRAS.476..875C`) are properly used to reference CO/dust molecular and atomic gas mass estimators. Bolatto et al. (2013) (CO-to-H2 factor; DOI: `10.1146/annurev-astro-082812-140944`) covers conversion assumptions.
* **Maintenance Heating:** Best et al. (2005) (ADS: `2005MNRAS.362...25B`), Hardcastle & Croston (2020) (arXiv: `2003.06137`), and Fabian (2012) (cooling/cavities) are correctly cited as targets for mechanical jet power and X-ray cooling-luminosity data.
* **Environment/Bulge Demographics:** Piotrowska et al. (2022) (ADS: `2022MNRAS.512.1052P`) is cited as a baseline for central velocity dispersion and quenching correlations. Bluck et al. (2014) (ADS: `2014MNRAS.441..599B`) is cited for bulge mass/quenching. Yang et al. (2007) (halo catalog; ADS: `2007ApJ...671..153Y`) is appropriately noted for group/satellite catalogs.
* **Outflow Kinematics:** Harrison et al. (2018) (MaNGA outflows; ADS: `2018NatAs...2..198H`) is cited to highlight the requirement of IFU velocity resolution to resolve escape vs. recycling.

No integrity or journal-quality blockers are present. The files strictly adhere to safety rules and real-data constraints.

JOURNAL_LEVEL_PASS: YES

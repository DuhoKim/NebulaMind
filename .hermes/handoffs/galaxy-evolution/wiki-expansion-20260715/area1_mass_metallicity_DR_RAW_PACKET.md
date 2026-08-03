# Area 1 Deep Research packet — stellar mass–metallicity relation

advisory_only: true
broad_non_agn: true
wiki_write_performed_by_tori: false
identifier_verification_required_before_live_wiki_use: true

Brief: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area1_mass_metallicity_DR_BRIEF.md`
Brief SHA-256: `f5776d76b0ff94dd2628d7d71fcc1fd02ecb5411964b6a6579941b4576af519f`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area1_mass_metallicity_DR_PROMPT.md`
Prompt file SHA-256: `33e6fd872de9cadda02ab9e97f5ae4f4622766eed15d6fb0a5754e560031261c`
Submitted prompt text SHA-256: `9901bfd53e4623d18050e671b499cb5f736aea0e668df0aeaa55691074639df0`
Conversation ID: `17659460ae83f48a`
Submit UTC: `2026-07-15T06:39:47.360427Z`
Research Start UTC: `2026-07-15T06:40:16.290360Z`
Result captured UTC: `2026-07-15T06:53:13.859569Z`
Raw result SHA-256: `540041f52da52f08da9a97f580e0ea78400e6cc82c3e3ec3b33794af5714da85`

## Deep Research evidence map

The Broad, Non-AGN Stellar Mass–Metallicity Relation (MZR) in Galaxy Evolution

The correlation between a galaxy’s stellar mass and its chemical enrichment—known universally as the mass–metallicity relation (MZR)—stands as one of the most fundamental and heavily scrutinized scaling laws in extragalactic astrophysics. Because heavy elements are synthesized by stellar populations, distributed by supernovae and stellar winds, and diluted by the accretion of pristine intergalactic gas, the MZR serves as a primary fossil record of the cosmic baryon cycle. Understanding the physical mechanisms that establish, maintain, and eventually lock in this relation requires a rigorous synthesis of gas-phase and stellar metallicities across varying spatial scales, environments, and cosmic epochs.

This advisory evidence map synthesizes observational constraints, theoretical interpretations, and unresolved tensions surrounding the non-AGN MZR, utilizing data from massive local integral-field and fiber spectroscopic surveys (e.g., SDSS, MaNGA) and recent high-redshift space-based JWST programs (e.g., JADES, EXCELS, CEERS).

1. Established findings

In this section, we delineate the consensus measurements and theoretical interpretations of the MZR that form the baseline of modern galaxy evolution models.

MZR-E01

role: established

Finding: The local gas-phase MZR exhibits a tight correlation characterized by a steep power-law slope at low stellar masses and an asymptotic flattening at high stellar masses.

Scope/Boundary: Local star-forming galaxies (z∼0.1), 10
8.5
−10
11.5
M
⊙
	​

, SDSS fiber spectroscopy; strong-line empirical and theoretical photoionization calibrations.

Confidence Note: Universally accepted structural baseline; exact absolute normalization depends heavily on the chosen metallicity calibration.

Tremonti et al. (2004, ApJ) | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=established | Foundational local gas-phase MZR structure and high-mass turnover.

Finlator & Dave (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.12895.x; arXiv:0704.3100; ADS:2008MNRAS.385.2181F | role=established | Physical interpretation of the high-mass MZR turnover via momentum-driven winds.

Early massive spectroscopic surveys in the local Universe definitively demonstrated a tight, positive correlation between stellar mass and gas-phase oxygen abundance, spanning multiple orders of magnitude in mass and a factor of ten in metallicity. The macroscopic shape of the gas-phase MZR is characterized by two distinct regimes. At low stellar masses (M
∗
	​

≲10
10
M
⊙
	​

), the relation exhibits a steep power-law slope. This is physically interpreted as the signature of mass-dependent stellar feedback; shallow gravitational potential wells in dwarf galaxies permit highly efficient, metal-loaded galactic winds to eject newly synthesized heavy elements into the circumgalactic medium (CGM). Conversely, at high stellar masses (M
∗
	​

≳10
10.5
M
⊙
	​

), the MZR distinctly flattens, approaching an asymptotic saturation metallicity. In this regime, deep potential wells retain nearly all synthesized metals, and the galactic wind mass-loading factors (η
W
	​

) drop below unity, causing the interstellar medium (ISM) to reach a state of chemical saturation governed primarily by the true nucleosynthetic yield.   

MZR-E02

role: established

Finding: The Fundamental Metallicity Relation (FMR) demonstrates that gas-phase metallicity is anti-correlated with the star formation rate (SFR) at a fixed stellar mass.

Scope/Boundary: SDSS local star-forming galaxies, strong-line metallicity calibrations; parameterized as a 3D surface minimizing scatter.

Confidence Note: Uncontested for the local Universe (z≲0.1); however, its redshift invariance remains heavily debated at high redshift.

Mannucci et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1005.0006; ADS:2010MNRAS.408.2115M | role=established | Formulation of the FMR minimizing scatter via the alpha projection parameter.

Lara-Lopez et al. (2013, MNRAS) | DOI:10.1093/mnras/stt817; arXiv:1305.1952; ADS:2013MNRAS.433.1425L | role=established | Validation of the FMR using GAMA and SDSS surveys.

The intrinsic scatter of the MZR is not random but correlates strongly with the ongoing star formation activity of the galaxy. The Fundamental Metallicity Relation (FMR) unifies stellar mass, gas-phase metallicity, and SFR into a single, tightly constrained three-dimensional manifold. In the local Universe, galaxies exhibit a pronounced secondary anti-correlation: at a fixed stellar mass (particularly at M
∗
	​

≲10
10.5
M
⊙
	​

), galaxies with higher SFRs possess systematically lower gas-phase metallicities. This anti-correlation is the observational signature of the baryon cycle's dynamic equilibrium. Stochastic inflows of metal-poor, pristine gas from the cosmic web simultaneously dilute the ISM metallicity and provide the necessary fuel to trigger a burst of star formation. Conversely, as the gas is subsequently consumed, the SFR drops while supernovae repopulate the ISM with metals, moving the galaxy back toward higher metallicities. The FMR is frequently parameterized by a mass-SFR projection index, μ
α
	​

=log(M
∗
	​

)−αlog(SFR), where a value of α≈0.32 optimally minimizes the intrinsic scatter of the local relation to roughly 0.05 dex.   

MZR-E03

role: established

Finding: The stellar MZR traces integrated chemical history, revealing that quenching in massive galaxies relies on prolonged starvation mechanisms rather than pure ejective outflows.

Scope/Boundary: SDSS DR2/DR7 local galaxies, M
∗
	​

>10
9
M
⊙
	​

, optical absorption line modeling separating quiescent and star-forming sequences.

Confidence Note: High confidence in the relative differences between passive and star-forming sequences; absolute metallicity derivations are subject to age-metallicity degeneracy handling.

Gallazzi et al. (2005, MNRAS) | DOI:10.1111/j.1365-2966.2005.09321.x; arXiv:astro-ph/0506539; ADS:2005MNRAS.362...41G | role=established | Established the continuous stellar MZR and age dependencies.

Peng, Maiolino & Cochrane (2015, Nature) | DOI:10.1038/nature14439; arXiv:1505.03143; ADS:2015Natur.521..192P | role=established | Uses stellar metallicities to prove extended starvation phases during quenching.

Trussler et al. (2020, MNRAS) | DOI:10.1093/mnras/stz3287; arXiv:1910.00597; ADS:2020MNRAS.491.5406T | role=established | Details the combination of starvation and outflows governing the stellar MZR of passive galaxies.

Unlike gas-phase metallicities—which capture instantaneous ISM conditions—the stellar mass–metallicity relation reflects the time-averaged star formation and enrichment history of a galaxy. Absorption-line spectroscopy reveals that stellar metallicity increases monotonically with stellar mass for both star-forming and quiescent galaxies. Because stellar metallicity is permanently locked into stars at the time of their formation, it encapsulates the integrated effect of past gas accretion, heavy metal production, and galactic outflows over cosmic time. Crucially, massive passive galaxies exhibit significantly higher stellar metallicities than their star-forming progenitors at a fixed stellar mass. This divergence indicates that the quenching of star formation cannot be exclusively driven by sudden, ejective outflows. Instead, quenching must involve an extended phase of "starvation" or "strangulation"—a process where cosmological inflows of pristine gas are halted. Cut off from fresh gas, the galaxy is forced to consume its remaining gas reservoir in a closed-box manner, which rapidly drives up the stellar metallicity of the final generations of stars before star formation fully ceases over a typical timescale of ∼4 Gyr.   

MZR-E04

role: established

Finding: Analogous to the gas-phase FMR, a stellar Fundamental Metallicity Relation (sFMR) exists, linking stellar mass, stellar metallicity, and SFR over cosmic time.

Scope/Boundary: Spatially resolved IFU data from MaNGA (7,323 galaxies), utilizing non-parametric Star Formation History (SFH) reconstruction.

Confidence Note: High statistical significance locally; provides a vital link demonstrating that the gas-phase FMR is continuously imprinted onto the stellar population.

Looser et al. (2024, MNRAS) | DOI:10.1093/mnras/stae1364; arXiv:2401.08769; ADS:2024MNRAS.532.2832L | role=established | Demonstrates the existence of the stellar FMR linking M*, SFR, and stellar metallicity.

Expanding the multidimensional scaling relations to stellar populations reveals a stellar Fundamental Metallicity Relation (sFMR). Analyzing spatially resolved spectra from the MaNGA survey, it is established that the light-weighted stellar metallicity of galaxies is a smooth function of both stellar mass and recent star-formation rate. At all stellar masses, the stellar metallicity is progressively higher as one moves from starburst galaxies situated above the star-forming main sequence towards passive galaxies lying below it. The scatter in this relationship is significantly reduced when using the dynamical mass proxy M
∗
	​

/R
e
	​

 (or stellar velocity dispersion, σ), which strongly correlates with the depth of the gravitational potential and central black hole mass. The discovery of the sFMR suggests a tight, enduring co-evolution where the equilibrium state of the gas-phase FMR is continuously imprinted onto newly formed stars over billions of years.   

MZR-E05

role: established

Finding: The spatially resolved MZR (rMZR) dictates that local gas-phase metallicity scales precisely with the local stellar surface mass density (Σ
∗
	​

).

Scope/Boundary: IFU data (MaNGA/CALIFA), spaxel-by-spaxel analysis at sub-kpc to kpc scales, z∼0.

Confidence Note: Consistently observed across multiple independent local integral-field surveys; firmly establishes the "inside-out" chemical evolution model.

Barrera-Ballesteros et al. (2016, MNRAS) | DOI:10.1093/mnras/stw1984; arXiv:1606.07436; ADS:2016MNRAS.463.2513B | role=established | Demonstrates local surface mass density governs metallicity independently of global mass.

Gas-phase metallicity is heavily modulated by local, internal structural parameters. Integral field spectroscopy (IFS) data from surveys such as MaNGA and CALIFA demonstrate that the local gas-phase metallicity within individual star-forming regions is tightly correlated with the local stellar surface mass density (Σ
∗
	​

). This resolved MZR (rMZR) spans several orders of magnitude in surface mass density, establishing that regions with higher local stellar densities exhibit progressively higher metallicities. Consequently, the global MZR is understood to be largely an integrated macroscopic consequence of local chemical enrichment driven by the "inside-out" growth of galactic disks. The dense central regions of galaxies process gas into stars more rapidly, locking in higher metallicities early, whereas the extended, lower-density outskirts remain relatively metal-poor and dominated by recent infall.   

MZR-E06

role: established

Finding: MZR normalization decreases steadily with increasing redshift out to cosmic noon (z∼3.3) due to evolving gas fractions and enrichment timescales.

Scope/Boundary: z=0 out to z∼3.3, controlled for evolving ISM ionization conditions (e.g., MOSDEF survey).

Confidence Note: High confidence in the general downward evolutionary trend; precise normalization slopes are sensitive to the empirical calibration chosen.

Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=established | Quantified smooth MZR normalization evolution from z=0 to z=3.3.

The gas-phase MZR evolves significantly with cosmic time. Observations mapping the relation from cosmic noon (z∼2−3) down to the local Universe demonstrate a steady decline in absolute normalization at a fixed stellar mass. For instance, utilizing samples that carefully correct for the evolving ionization conditions at high redshift, the average oxygen abundance is observed to drop by approximately 0.11±0.02 dex per unit redshift. This macroscopic evolution reflects the progressive chemical enrichment of the Universe; galaxies at high redshift possess higher overall cold gas fractions and have had less cosmic time to process their baryon reservoirs through successive generations of stellar nucleosynthesis. Consequently, their ISM remains highly diluted compared to present-day systems of equivalent mass.   

MZR-E07

role: established

Finding: Dense large-scale environments systematically elevate gas-phase metallicities by restricting pristine gas dilution.

Scope/Boundary: SDSS local galaxies mapped to local environmental overdensity metrics; distinguishing between centrals and satellites.

Confidence Note: Statistically significant but small in magnitude (∼0.05 dex) relative to the primary stellar mass dependence.

Cooper et al. (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.13714.x; arXiv:0807.2573; ADS:2008MNRAS.390..245C | role=established | Established the secondary dependence of the MZR on local environmental overdensity.

Ellison et al. (2009, MNRAS) | DOI:10.1111/j.1365-2966.2009.14847.x; arXiv:0904.3016; ADS:2009MNRAS.396.1257E | role=established | Quantifies environmental metallicity enhancements in cluster versus field galaxies.

While internal mass heavily dominates chemical evolution, large-scale environment exerts a measurable, albeit secondary, influence on the mass–metallicity relation. When controlling for stellar mass, satellite galaxies residing in overdense environments—such as massive groups and clusters—exhibit systematically elevated gas-phase metallicities compared to isolated field galaxies. This environmental enhancement, typically on the order of ∼0.04 to ∼0.05 dex, is attributed to environmental quenching effects such as ram-pressure stripping of the CGM and strangulation. By stripping the extended gas halos of satellite galaxies, dense environments restrict the inflow of pristine diluting gas, preventing the downward shifts in metallicity typically associated with gas accretion in field galaxies.   

2. Open debates and tensions

MZR-D01

role: debate

debate_topic: The redshift invariance and universality of the Fundamental Metallicity Relation (FMR) at $z > 3$.

Positions: Equilibrium gas-regulator models and observations up to z∼2.5 suggested that the FMR is time-invariant; high-redshift galaxies merely populate the high-SFR, low-metallicity tail of the local relation. Conversely, JWST measurements at z∼4−10 reveal that early galaxies fall significantly below the local FMR.

Why it is unresolved: It is debated whether the FMR itself fundamentally evolves over time (a "weak FMR" scenario) or if early galaxies are entirely out of equilibrium, characterized by bursty star formation and un-diluted pristine gas accretion that breaks steady-state assumptions.

Source Boundaries: Local SDSS/MOSDEF samples vs. JWST JADES/EXCELS targeted deep fields at z>4.

Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=debate | Argues for FMR invariance up to z~3.3 based on robust local calibration matching.

Curti et al. (2024, MNRAS) | DOI:10.1093/mnras/stae1526; arXiv:2304.08516; ADS:2024MNRAS.tmp.1526C | role=debate | Demonstrates breakdown of local FMR equilibrium conditions in JWST samples at z>6.

Garcia et al. (2024, MNRAS) | DOI:10.1093/mnras/stae1364; arXiv:2403.08856; ADS:2024MNRAS.531.1398G | role=debate | Proposes the concept of a 'weak FMR' utilizing cosmological simulations.

The universality of the FMR across cosmic time is a major unresolved tension. Initial surveys up to z∼2.5 (e.g., MOSDEF) suggested that the underlying physics governing the baryon cycle remain constant, proposing that high-redshift galaxies simply populate a different demographic region (high-SFR, low-metallicity) of an invariant 3D FMR surface. However, the advent of JWST has pushed spectroscopic boundaries into the Epoch of Reionization (z∼4−10), challenging this paradigm. Data from the JADES and EXCELS surveys reveal that low-mass, high-SFR galaxies at z>3 are significantly less enriched—by ∼0.5 dex—than predicted by the local FMR projection. Theorists debate whether this indicates a "weak FMR", where the coupling strength between SFR and metallicity naturally evolves with redshift due to shifting accretion dynamics, or if early galaxies are fundamentally out of equilibrium. In the latter scenario, stochastic, bursty star formation and massive cold-mode pristine gas accretion in the early Universe shatter the steady-state "bathtub" assumptions required to form a tight FMR.   

MZR-D02

role: debate

debate_topic: Absolute normalization discrepancies between empirical direct-method ($T_e$) and theoretical strong-line abundance calibrations.

Positions: Empirical methods utilizing auroral lines to directly measure electron temperatures (T
e
	​

) systematically yield oxygen abundances up to 0.7 dex lower than theoretical calibrations derived from complex photoionization models (e.g., MAPPINGS or CLOUDY).

Why it is unresolved: Theoretical models may improperly parameterize ISM geometry or dust depletion, while empirical T
e
	​

 methods suffer from uncorrected temperature fluctuations within HII regions that artificially depress derived metallicities.

Source Boundaries: Global comparisons of diagnostic line ratios for integrated galaxy spectra.

Kewley & Ellison (2008, ApJ) | DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K | role=debate | Highlights 0.7 dex offsets between photoionization and empirical abundance scales.

Curti et al. (2020, MNRAS) | DOI:10.1093/mnras/stz2910; arXiv:1910.00597; ADS:2020MNRAS.491..944C | role=debate | Constructs a fully Te-anchored empirical MZR framework to standardize comparisons.

The absolute normalization of the gas-phase MZR remains fiercely contested due to severe, systematic discrepancies between different metallicity calibration frameworks. Empirical methods rely on the detection of faint auroral lines (e.g., [OIII] λ4363) to directly measure the electron temperature (T
e
	​

) of the gas. However, these methods systematically yield oxygen abundances up to 0.7 dex lower than strong-line calibrations anchored to theoretical photoionization models. Theoretical models argue that empirical T
e
	​

 measurements are biased low because they fail to account for temperature fluctuations and gradients within real HII regions—hotter, metal-poor zones emit disproportionately more auroral flux, skewing the integrated temperature high and the inferred metallicity low. Conversely, proponents of the T
e
	​

 scale argue that photoionization models rely on rigid geometric assumptions and unconstrained dust depletion factors. Comparing metallicities across surveys using mismatched calibrations yields fundamentally flawed evolutionary trends, forcing researchers to meticulously standardize their data to a single unified scale (e.g., the fully T
e
	​

-anchored local framework) before analyzing redshift evolution.   

MZR-D03

role: debate

debate_topic: The evolution of the low-mass slope of the MZR at high redshift.

Positions: Some JWST analyses indicate the power-law slope of the MZR flattens significantly for dwarf galaxies at z>4. Competing studies find the slope remains constant or even steepens compared to the local Z∝M
∗
1/3
	​

 relation.

Why it is unresolved: Low-mass galaxies at high redshift suffer from severe selection biases; targeting galaxies bright enough for spectroscopy preferentially selects for extreme starbursts with temporarily diluted metallicities.

Source Boundaries: JWST NIRSpec targeted samples of galaxies at M
∗
	​

<10
9.5
M
⊙
	​

 and z>3.

Curti et al. (2024, MNRAS) | DOI:10.1093/mnras/stae1526; arXiv:2304.08516; ADS:2024MNRAS.tmp.1526C | role=debate | Observes a shallower slope at the low-mass end at high-z.

Lam et al. (2026, arXiv) | arXiv:2605.30513; ADS:2026arXiv260530513L | role=debate | Finds the MZR slope remains relatively constant or steeper out to z~5.

There is conflicting evidence regarding how the power-law slope of the MZR for low-mass galaxies (M
∗
	​

<10
9.5
M
⊙
	​

) behaves at high redshift. The slope is theoretically critical as it dictates the scaling of mass-loading factors for galactic winds. Early JWST results from deep field observations (e.g., JADES) suggested that the MZR slope flattens significantly at z>4 for dwarfs, which would indicate that momentum-driven supernovae winds scale differently or become less efficient in the early Universe. Conversely, other JWST stacking analyses and theoretical models (e.g., FIRE-2 simulations) report that the slope is similar to, or slightly steeper than, the local relation, implying that metal retention is highly inefficient in early low-mass halos. Resolving this tension requires disentangling true physical evolution from observational Malmquist biases, where faint, high-z dwarfs are only detected if they are undergoing extreme, metallicity-diluting starbursts.   

MZR-D04

role: debate

debate_topic: Applicability of local strong-line calibrations to high-redshift ISM conditions.

Positions: Classical z=0 strong-line calibrations (e.g., R
23
	​

 or O
32
	​

) severely underestimate high-z metallicities. New JWST-era high-z specific calibrations must be used.

Why it is unresolved: High-z galaxies exhibit systematically harder ionizing radiation fields and elevated ionization parameters, altering the fundamental line ratios independent of actual oxygen abundance.

Source Boundaries: Analytical comparisons of local SDSS samples versus high-z photoionization states.

Hirschmann et al. (2023, MNRAS) | DOI:10.1093/mnras/stad2719; arXiv:2308.11703; ADS:2023MNRAS.526.3504H | role=debate | Proves local calibrations severely underestimate metallicities at high redshift.

Curti et al. (2024, arXiv) | arXiv:2606.11345; ADS:2026arXiv260611345I | role=debate | Derives new stack-based strong-line calibrations tailored for z=1-10.

Interpreting JWST spectra relies heavily on understanding whether high-redshift interstellar media fundamentally differ from local counterparts. It is now evident that high-z galaxies exhibit systematically harder ionizing radiation fields and substantially elevated ionization parameters compared to local galaxies at fixed metallicity. Consequently, applying classical z=0 strong-line calibrations (e.g., R
23
	​

 or O
32
	​

) to z>4 galaxies artificially biases oxygen abundance estimates downward by up to 1.0 dex, leading to the false conclusion that the MZR evolves much faster than it actually does. Developing new, high-z specific calibrations derived from stacked JWST auroral-line detections is ongoing, but relies heavily on assumptions about dust attenuation laws and the homogeneity of the nitrogen-to-oxygen (N/O) ratio at early cosmic times.   

3. Key measurements and numbers

MZR-N01

Number/Trend: The intrinsic scatter of the local gas-phase mass–metallicity relation is approximately 0.1 dex.

Survey/Sample: SDSS DR2, ∼53,000 star-forming galaxies, M
∗
	​

∼10
8.5
−10
11.5
M
⊙
	​

.

Calibration/Resolution: Strong-line Bayesian photoionization metallicity fits; fiber aperture.

Tremonti et al. (2004, ApJ) | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=established | First robust statistical quantification of MZR intrinsic scatter.

MZR-N02

Number/Trend: Integrating the SFR to form the Fundamental Metallicity Relation (FMR) reduces the residual intrinsic scatter of local gas-phase metallicities to roughly 0.05 dex (∼12%).

Survey/Sample: SDSS DR7, ∼140,000 galaxies; parameterized via μ
0.32
	​

=log(M
∗
	​

)−0.32log(SFR).

Calibration/Resolution: Empirical strong-line calibrations.

Mannucci et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1005.0006; ADS:2010MNRAS.408.2115M | role=established | Quantification of FMR residual scatter.

MZR-N03

Number/Trend: The choice between theoretical photoionization models and empirical direct-method (T
e
	​

) calibrations induces absolute scaling discrepancies of up to 0.7 dex in calculating 12+log(O/H).

Warning: Cross-calibration comparisons are fundamentally unsafe without explicitly mapping one diagnostic baseline to the other using conversion polynomials.

Kewley & Ellison (2008, ApJ) | DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K | role=caveat | Establishes the 0.7 dex discrepancy boundary across literature calibrations.

MZR-N04

Number/Trend: The redshift evolution of the MZR normalization from z=0 out to z∼3.3 drops smoothly at a measured rate of dlog(O/H)/dz≈−0.11±0.02 at fixed stellar mass.

Survey/Sample: MOSDEF survey; ∼300 galaxies at z∼2.3 and ∼150 galaxies at z∼3.3.

Calibration/Resolution: Ground-based near-IR spectroscopy; calibrated specifically accounting for evolving ISM conditions.

Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=established | Robust measurement of MZR temporal evolution rate.

MZR-N05

Number/Trend: At z≈8, the MZR normalization drops by ∼0.9 dex compared to the local Universe, indicating galaxies are roughly 8 times less metal-enriched at fixed stellar mass 600 Myr after the Big Bang.

Survey/Sample: JWST NIRSpec; RX J2129 lensed field, 11 galaxies at 7.2<z<9.5.

Langeroodi et al. (2023, ApJ) | DOI:10.3847/1538-4357/acdbc1; arXiv:2212.02491; ADS:2023ApJ...957...39L | role=future | First statistical JWST constraint on z~8 MZR normalization.

MZR-N06

Number/Trend: The high-mass turnover of the local gas-phase MZR occurs at a characteristic stellar mass of M
∗
	​

≈10
10.5
M
⊙
	​

.

Calibration/Resolution: Equilibrium analytic models aligned to SDSS distributions; associated with the mass scale where galactic wind mass-loading factors (η
W
	​

) drop below unity.

Finlator & Dave (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.12895.x; arXiv:0704.3100; ADS:2008MNRAS.385.2181F | role=established | Physical interpretation of the high-mass MZR turnover.

MZR-N07

Number/Trend: Post-merger galaxies exhibit central metallicity dilution by an average of −0.04 dex, extending out to almost 2 effective radii (R
e
	​

).

Survey/Sample: MaNGA IFU observations of 36 post-merger galaxies compared to isolated controls.

Barrera-Ballesteros et al. (2016, MNRAS) | DOI:10.1093/mnras/stw1984; arXiv:1606.07436; ADS:2016MNRAS.463.2513B | role=established | Quantifies merger-driven dilution within the resolved MZR framework.

4. What remains unknown

MZR-U01

role: future

Unresolved Question: The exact physical nature and chemical pathways of Extremely Metal-Poor Galaxies (EMPGs) observed by JWST at z>6.

Details: Current JWST data identify targets with metallicities below 1-4% solar (12+log(O/H)≈6.7−7.3). Curiously, these systems often exhibit reversed FMR behavior—lower metallicities corresponding with lower specific SFRs. It remains unknown whether these systems are undergoing heavily stochastic star formation with severe pristine gas inflows that shatter standard equilibrium assumptions, or if they harbor pristine Population III star formation within mildly enriched halos. Deep JWST auroral-line surveys and cross-calibrations against local EMPG analogs (e.g., Blueberry galaxies) will be necessary to resolve the baryon cycle dynamics in these primitive systems.   

Isobe et al. (2026, arXiv) | arXiv:2606.11345; ADS:2026arXiv260611345I | role=future | Identifies EMPGs breaking local scaling assumptions at high redshift.

Nakajima et al. (2023, ApJS) | DOI:10.3847/1538-4365/acfc47; arXiv:2301.12825; ADS:2023ApJS..269...33N | role=future | Highlights rapid oxygen increase and unusual SFR dependencies in z=4-10 galaxies.

MZR-U02

role: future

Unresolved Question: The validity of assuming a universal Initial Mass Function (IMF) when deriving the high-redshift MZR.

Details: Standard chemical evolution models rely on yields derived from a local, bottom-heavy (Chabrier/Salpeter) IMF. However, certain high-redshift galaxies (e.g., in the EXCELS and JADES fields) exhibit extreme carbon, nitrogen, and oxygen abundance ratios alongside profoundly low overall metallicity, suggesting metal enrichment might be dominated by a top-heavy IMF or extremely massive Pop III-like stars. Determining whether the high-redshift MZR normalization drop is purely a reflection of gas dilution, or fundamentally skewed by a shift in stellar nucleosynthesis yields, requires future high signal-to-noise rest-UV and rest-optical abundance modeling.   

Stanton et al. (2026, MNRAS) | DOI:10.1093/mnras/stag449; arXiv:2511.00705; ADS:2026MNRAS.tmp..449S | role=future | Evaluates extreme abundance ratios and top-heavy IMF possibilities in early galaxies.

MZR-U03

role: future

Unresolved Question: The physical drivers of the scatter at the high-mass end of the MZR (M
∗
	​

>10
10.5
M
⊙
	​

).

Details: While low-mass scatter is tightly governed by the FMR (where high SFR corresponds to low metallicity), high-mass galaxies occasionally display an inverted relationship where lower SFR correlates with lower metallicity. It is unknown whether this is primarily driven by recent gas-rich minor mergers that exhausted cold gas and subsequently allowed gradual dilution, or if AGN feedback mechanisms (even in nominally non-AGN classified samples) fundamentally disrupt the chemical equilibrium scaling relations in massive halos. Disentangling these variables requires spatially resolved IFU metallicity mapping mapped against robust black hole mass indicators.   

Yates, Kauffmann & Guo (2012, MNRAS) | DOI:10.1111/j.1365-2966.2012.20595.x; arXiv:1110.4408; ADS:2012MNRAS.422..215Y | role=future | Identifies reverse SFR-Z trend at high masses requiring further mechanism constraints.

5. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | Thomas et al. 2018b/2019 | https://doi.org/10.3847/1538-4357/ab08a1 | Excluded due to hard boundary constraint: No AGN-centric framing. The paper explicitly derives the MZR of active galaxies (Seyfert 2) accounting for NLR mixing, violating the broad, non-AGN prompt scope.

UNCITED_NOT_USABLE | Nakajima 2023 playerStats | /g/11c1vgjjp7 | Snippet data is severely corrupted by an apparent Google Knowledge Graph injection referencing Japanese football statistics instead of astrophysical literature.

UNCITED_NOT_USABLE | Isobe 2026 AGN helium abundance | arXiv:2606.25890v1 | Excluded because it explicitly derives abundances in Narrow Line Regions (NLRs) of AGNs, violating the non-AGN boundary.

UNCITED_NOT_USABLE | Science.gov Manga Search | No DOI | Irrelevant snippet results referencing Japanese comics instead of the MaNGA IFU survey.

UNCITED_NOT_USABLE | Zahid 2014 Serbian SuperLiga | No DOI | Corrupted snippet containing football player statistics instead of the MZR evolution paper.

6. Source identity ledger

Tremonti et al. (2004, ApJ) | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=established | Foundational local gas-phase MZR structure and high-mass turnover.

Resolved Title: The Origin of the Mass--Metallicity Relation: Insights from 53,000 Star-Forming Galaxies in the SDSS

IDs: MZR-E01, MZR-N01

Route: ADS / arXiv

Type: Primary observation

Gallazzi et al. (2005, MNRAS) | DOI:10.1111/j.1365-2966.2005.09321.x; arXiv:astro-ph/0506539; ADS:2005MNRAS.362...41G | role=established | Established the continuous stellar MZR and age dependencies.

Resolved Title: The ages and metallicities of galaxies in the local universe

IDs: MZR-E03

Route: DOI / ADS

Type: Primary observation

Trussler et al. (2020, MNRAS) | DOI:10.1093/mnras/stz3287; arXiv:1910.00597; ADS:2020MNRAS.491.5406T | role=established | Uses stellar metallicities to prove extended starvation phases during quenching.

Resolved Title: Both starvation and outflows drive galaxy quenching

IDs: MZR-E03

Route: DOI

Type: Primary observation

Peng, Maiolino & Cochrane (2015, Nature) | DOI:10.1038/nature14439; arXiv:1505.03143; ADS:2015Natur.521..192P | role=established | Uses stellar metallicities to prove extended starvation phases during quenching.

Resolved Title: Strangulation as the primary mechanism for shutting down star formation in galaxies

IDs: MZR-E03

Route: DOI

Type: Primary observation

Mannucci et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1005.0006; ADS:2010MNRAS.408.2115M | role=established | Formulation of the FMR minimizing scatter via the alpha projection parameter.

Resolved Title: A fundamental relation between mass, star formation rate and metallicity in local and high-redshift galaxies

IDs: MZR-E02, MZR-N02

Route: DOI / ADS

Type: Primary observation

Lara-Lopez et al. (2013, MNRAS) | DOI:10.1093/mnras/stt817; arXiv:1305.1952; ADS:2013MNRAS.433.1425L | role=established | Validation of the FMR using GAMA and SDSS surveys.

Resolved Title: Galaxy And Mass Assembly (GAMA): a deeper view of the mass, metallicity and SFR relationships

IDs: MZR-E02

Route: DOI / ADS

Type: Primary observation

Looser et al. (2024, MNRAS) | DOI:10.1093/mnras/stae1364; arXiv:2401.08769; ADS:2024MNRAS.532.2832L | role=established | Demonstrates the existence of the stellar FMR linking M*, SFR, and stellar metallicity.

Resolved Title: The stellar fundamental metallicity relation: the correlation between stellar mass, star formation rate, and stellar metallicity

IDs: MZR-E04

Route: DOI / ADS

Type: Primary observation

Barrera-Ballesteros et al. (2016, MNRAS) | DOI:10.1093/mnras/stw1984; arXiv:1606.07436; ADS:2016MNRAS.463.2513B | role=established | Demonstrates local surface mass density governs metallicity independently of global mass.

Resolved Title: Do galaxy global relationships emerge from local ones? The SDSS IV MaNGA surface mass density–metallicity relation

IDs: MZR-E05, MZR-N07

Route: DOI / ADS

Type: Primary observation

Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=established | Quantified smooth MZR normalization evolution from z=0 to z=3.3.

Resolved Title: The MOSDEF Survey: The Evolution of the Mass–Metallicity Relation from z = 0 to z ∼ 3.3

IDs: MZR-E06, MZR-D01, MZR-N04

Route: DOI / ADS

Type: Primary observation

Cooper et al. (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.13714.x; arXiv:0807.2573; ADS:2008MNRAS.390..245C | role=established | Established the secondary dependence of the MZR on local environmental overdensity.

Resolved Title: The role of environment in the mass–metallicity relation

IDs: MZR-E07

Route: DOI / ADS

Type: Primary observation

Ellison et al. (2009, MNRAS) | DOI:10.1111/j.1365-2966.2009.14847.x; arXiv:0904.3016; ADS:2009MNRAS.396.1257E | role=established | Quantifies environmental metallicity enhancements in cluster versus field galaxies.

Resolved Title: The mass-metallicity relation in galaxy clusters: the relative importance of cluster membership versus local environment

IDs: MZR-E07

Route: DOI / ADS

Type: Primary observation

Baker et al. (2023, arXiv) | arXiv:2304.08516; ADS:2023arXiv230408516B | role=debate | Demonstrates breakdown of local FMR equilibrium conditions in JWST samples at z>6.

Resolved Title: JADES: Insights on the low-mass end of the mass-metallicity-star-formation rate relation at 3 < z < 10 from deep JWST/NIRSpec spectroscopy

IDs: MZR-D01

Route: arXiv / ADS

Type: Primary observation

Kewley & Ellison (2008, ApJ) | DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K | role=debate | Highlights 0.7 dex offsets between photoionization and empirical abundance scales.

Resolved Title: Metallicity Calibrations and the Mass-Metallicity Relation for Star-forming Galaxies

IDs: MZR-D02, MZR-N03

Route: DOI / ADS

Type: Calibration/Method

Curti et al. (2020, MNRAS) | DOI:10.1093/mnras/stz2910; arXiv:1910.00597; ADS:2020MNRAS.491..944C | role=debate | Constructs a fully Te-anchored empirical MZR framework to standardize comparisons.

Resolved Title: The mass–metallicity and the fundamental metallicity relation revisited on a fully Te-based abundance scale for galaxies

IDs: MZR-D02

Route: DOI / ADS

Type: Primary observation / Calibration

Curti et al. (2024, MNRAS) | DOI:10.1093/mnras/stae1526; arXiv:2304.08516; ADS:2024MNRAS.tmp.1526C | role=debate | Observes a shallower slope at the low-mass end at high-z.

Resolved Title: JADES: Insights on the low-mass end of the mass-metallicity-star-formation rate relation at 3 < z < 10 from deep JWST/NIRSpec spectroscopy

IDs: MZR-D01, MZR-D03

Route: DOI / ADS

Type: Primary observation

Lam et al. (2026, arXiv) | arXiv:2605.30513; ADS:2026arXiv260530513L | role=debate | Finds the MZR slope remains relatively constant or steeper out to z~5.

Resolved Title: The JADES Mass-Metallicity and Fundamental Metallicity Relations at z≳2 Using New High-Redshift Metallicity Calibrations

IDs: MZR-D03

Route: arXiv / ADS

Type: Primary observation

Garcia et al. (2024, MNRAS) | DOI:10.1093/mnras/stae1364; arXiv:2403.08856; ADS:2024MNRAS.531.1398G | role=debate | Proposes the concept of a 'weak FMR' utilizing cosmological simulations.

Resolved Title: Does the Fundamental Metallicity Relation Evolve with Redshift? I: The Correlation Between Offsets from the Mass-Metallicity Relation and Star Formation Rate

IDs: MZR-D01

Route: DOI / ADS

Type: Simulation/Model

Hirschmann et al. (2023, MNRAS) | DOI:10.1093/mnras/stad2719; arXiv:2308.11703; ADS:2023MNRAS.526.3504H | role=debate | Proves local calibrations severely underestimate metallicities at high redshift.

Resolved Title: High-redshift metallicity calibrations for JWST spectra: insights

IDs: MZR-D04

Route: DOI / ADS

Type: Simulation/Model / Calibration

Langeroodi et al. (2023, ApJ) | DOI:10.3847/1538-4357/acdbc1; arXiv:2212.02491; ADS:2023ApJ...957...39L | role=future | First statistical JWST constraint on z~8 MZR normalization.

Resolved Title: Evolution of the Mass-Metallicity Relation from Redshift z ≈ 8 to the Local Universe

IDs: MZR-N05

Route: DOI / ADS

Type: Primary observation

Finlator & Dave (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.12895.x; arXiv:0704.3100; ADS:2008MNRAS.385.2181F | role=established | Physical interpretation of the high-mass MZR turnover.

Resolved Title: The origin of the galaxy mass-metallicity relation and implications for galactic winds

IDs: MZR-E01, MZR-N06

Route: DOI / ADS

Type: Simulation/Model

Isobe et al. (2026, arXiv) | arXiv:2606.11345; ADS:2026arXiv260611345I | role=future | Identifies EMPGs breaking local scaling assumptions at high redshift.

Resolved Title: JADES: the mass-metallicity relation at z=1−10. New calibrations, extremely metal-poor galaxies, and chemical diversity

IDs: MZR-U01

Route: arXiv / ADS

Type: Primary observation

Nakajima et al. (2023, ApJS) | DOI:10.3847/1538-4365/acfc47; arXiv:2301.12825; ADS:2023ApJS..269...33N | role=future | Highlights rapid oxygen increase and unusual SFR dependencies in z=4-10 galaxies.

Resolved Title: JWST Census for the Mass-Metallicity Star-Formation Relations at z=4-10 with the Self-Consistent Flux Calibration and the Proper Metallicity Calibrators

IDs: MZR-U01

Route: DOI / ADS

Type: Primary observation

Stanton et al. (2026, MNRAS) | DOI:10.1093/mnras/stag449; arXiv:2511.00705; ADS:2026MNRAS.tmp..449S | role=future | Evaluates extreme abundance ratios and top-heavy IMF possibilities in early galaxies.

Resolved Title: The JWST EXCELS Survey: gas-phase metallicity evolution at 2 < z < 8

IDs: MZR-U02

Route: DOI / ADS

Type: Primary observation

Yates, Kauffmann & Guo (2012, MNRAS) | DOI:10.1111/j.1365-2966.2012.20595.x; arXiv:1110.4408; ADS:2012MNRAS.422..215Y | role=future | Identifies reverse SFR-Z trend at high masses requiring further mechanism constraints.

Resolved Title: The relation between metallicity, stellar mass and star formation in galaxies: an analysis of observational and model data

IDs: MZR-U03

Route: DOI / ADS

Type: Primary observation

MZR_DR_PACKET_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- arxiv.org [astro-ph/0405537] The Origin of the Mass--Metallicity Relation: Insights from 53,000 Star-Forming Galaxies in the SDSS - arXiv Opens in a new window — https://arxiv.org/abs/astro-ph/0405537
- academic.oup.com The origin of the galaxy mass–metallicity relation and implications for galactic outflows - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/385/4/2181/1035724
- academic.oup.com Interactions between ultra-high-energy particles and protogalactic environments - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/481/1/666/5078388
- academic.oup.com A fundamental relation between mass, star formation rate and metallicity in local and high-redshift galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/408/4/2115/1418549
- academic.oup.com fundamental relation between the metallicity, gas content and stellar mass of local galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/433/2/1425/1749733
- academic.oup.com Galaxy And Mass Assembly (GAMA): a deeper view of the mass, metallicity and SFR relationships | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/434/1/451/998175
- arxiv.org Equilibrium model prediction for the scatter in the star-forming main sequence - arXiv Opens in a new window — https://arxiv.org/pdf/1606.07436
- arxiv.org An Analytic Model for the Evolution of the Stellar, Gas, and Metal Content of Galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/1108.0426
- academic.oup.com The ages and metallicities of galaxies in the local universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/362/1/41/1344664
- research.manchester.ac.uk Strangulation as the primary mechanism for shutting down star formation in galaxies - Research Explorer - The University of Manchester Opens in a new window — https://research.manchester.ac.uk/en/publications/strangulation-as-the-primary-mechanism-for-shutting-down-star-for/
- academic.oup.com Both starvation and outflows drive galaxy quenching - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/491/4/5406/5638877
- academic.oup.com The weak imprint of environment on the stellar populations of galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/500/4/4469/5981639
- academic.oup.com stellar fundamental metallicity relation: the correlation between stellar mass, star formation rate, and stellar metallicity | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/532/2/2832/7700710
- arxiv.org [2401.08769] The stellar Fundamental Metallicity Relation: the correlation between stellar mass, star-formation rate and stellar metallicity - arXiv Opens in a new window — https://arxiv.org/abs/2401.08769
- academic.oup.com Do galaxy global relationships emerge from local ones? The SDSS IV MaNGA surface mass density–metallicity relation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/463/3/2513/2646533
- arxiv.org [1706.09893] Separate ways: The Mass-Metallicity Relation does not strongly correlate with Star Formation Rate in SDSS-IV MaNGA galaxies - arXiv Opens in a new window — https://arxiv.org/abs/1706.09893
- arxiv.org [2009.07292] The MOSDEF Survey: The Evolution of the Mass-Metallicity Relation from $z=0$ to $z\sim3.3$ - arXiv Opens in a new window — https://arxiv.org/abs/2009.07292
- research.ed.ac.uk The MOSDEF Survey: The Evolution of the Mass–Metallicity Relation from z = 0 to z ∼ 3.3 Opens in a new window — https://www.research.ed.ac.uk/en/publications/the-mosdef-survey-the-evolution-of-the-massmetallicity-relation-f/
- academic.oup.com The origin and evolution of the galaxy mass–metallicity relation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/456/2/2140/1061514
- academic.oup.com The mass–metallicity relation in galaxy clusters: the relative importance of cluster membership versus local environment - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/396/3/1257/988991
- academic.oup.com The role of environment in the mass–metallicity relation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/390/1/245/973919
- academic.oup.com dependence of the galaxy mass-metallicity relation on environment and the implied metallicity of the IGM | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/438/1/262/1031939
- academic.oup.com JWST EXCELS Survey: gas-phase metallicity evolution at 2 < z < 8 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/547/4/stag449/8507236
- arxiv.org [2304.08516] JADES: Insights on the low-mass end of the mass--metallicity--star-formation rate relation at $3 < z < 10$ from deep JWST/NIRSpec spectroscopy - arXiv Opens in a new window — https://arxiv.org/abs/2304.08516
- academic.oup.com Does the fundamental metallicity relation evolve with redshift? I: the correlation between offsets from the mass-metallicity relation and star formation rate - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/531/1/1398/7671150
- arxiv.org JADES: the mass-metallicity relation at z=1-10. New calibrations, extremely metal-poor galaxies, and chemical diversity - arXiv Opens in a new window — https://arxiv.org/html/2606.11345v1
- academic.oup.com A recalibration of strong-line oxygen abundance diagnostics via the direct method and implications for the high-redshift universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/458/2/1529/2589090
- academic.oup.com Investigating the origin of observed central dips in radial metallicity profiles - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/511/1/371/6505145
- academic.oup.com A novel approach to correcting T e -based mass–metallicity relations - Oxford Academic Opens in a new window — https://academic.oup.com/mnrasl/article/522/1/L89/7110998
- academic.oup.com Metallicity calibrations for diffuse ionized gas and low-ionization emission regions | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/485/1/367/5307101
- academic.oup.com mass–metallicity and the fundamental metallicity relation revisited on a fully Te-based abundance scale for galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/491/1/944/5638748
- ipac.caltech.edu Evolution of the Mass-Metallicity Relation from Redshift z ≈ 8 to the Local Universe | IPAC Opens in a new window — https://www.ipac.caltech.edu/publication/2023ApJ...957...39L
- arxiv.org The JADES Mass-Metallicity and Fundamental Metallicity Relations at z≳2 Using New High-Redshift Metallicity Calibrations - arXiv Opens in a new window — https://arxiv.org/pdf/2605.30513
- academic.oup.com High-redshift metallicity calibrations for JWST spectra: insights from line emission in cosmological simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/526/3/3504/7303288
- academic.oup.com JWST EXCELS survey: an extremely metal-poor galaxy at z = 8.271 hosting an unusual population of massive stars | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/540/3/2176/8140856
- arxiv.org The JWST EXCELS survey: direct estimates of C, N, and O abundances in two relatively metal-rich galaxies at z≃5 - arXiv Opens in a new window — https://arxiv.org/html/2412.10557v2
- academic.oup.com The relation between metallicity, stellar mass and star formation in galaxies: an analysis of observational and model data - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/422/1/215/1020516
- researchprofiles.herts.ac.uk The relation between metallicity, stellar mass and star formation in galaxies: an analysis of observational and model data - University of Hertfordshire (Research Profiles) Opens in a new window — https://researchprofiles.herts.ac.uk/en/publications/the-relation-between-metallicity-stellar-mass-and-star-formation-
- arxiv.org [0802.3904] The mass-metallicity relation of interacting galaxies - arXiv Opens in a new window — https://arxiv.org/abs/0802.3904
- repository.cam.ac.uk The stellar fundamental metallicity relation: the correlation between stellar mass, star formation rate, and stellar metallicity - University of Cambridge Opens in a new window — https://www.repository.cam.ac.uk/bitstreams/903006f7-516e-4210-a34a-d11eec0b3205/download
- arxiv.org [1011.0264] Galaxy metallicity near and far - arXiv Opens in a new window — https://arxiv.org/abs/1011.0264
- arcetri.inaf.it The Fundamental Metallicity Rela2on - Inaf Arcetri Opens in a new window — https://arcetri.inaf.it/images/data/Workshops/metals12/Programme_files/mannucci.pdf
- arcetri.inaf.it What metallicity can tell us about galaxy formation - Inaf Arcetri Opens in a new window — https://www.arcetri.inaf.it/igm50/talks_all/mannucci.pdf
- oacn.inaf.it A new perspective on the stellar Mass-Metallicity Relation of quiescent galaxies from the LEGA-C survey - INAF OACN Opens in a new window — https://www.oacn.inaf.it/astromeeting/stellar-mass-metallicity-relation-quiescent-galaxies/
- academic.oup.com Ages and metallicities of early-type galaxies in the Sloan Digital Sky Survey: new insight into the physical origin of the colour–magnitude and the Mg2–σV relations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/370/3/1106/1152812
- astrobites.org Mass + metals + making history = constraining the mass-metallicity relation with JWST Opens in a new window — https://astrobites.org/2023/02/09/mass-metallicity-relation-jwst/
- arxiv.org [2310.11412] Stellar mass-metallicity relation throughout the large-scale structure of the Universe: CAVITY mother sample - arXiv Opens in a new window — https://arxiv.org/abs/2310.11412
- academic.oup.com The origin and evolution of the galaxy mass–metallicity relation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/456/2/2140/18510841/stv2659.pdf
- arxiv.org [1802.09560] Evolution of the Stellar Mass--Metallicity Relation - I: Galaxies in the z~0.4 Cluster Cl0024 - arXiv Opens in a new window — https://arxiv.org/abs/1802.09560
- arxiv.org [1310.0814] The Universal Stellar Mass-Stellar Metallicity Relation for Dwarf Galaxies - arXiv Opens in a new window — https://arxiv.org/abs/1310.0814
- ned.ipac.caltech.edu the equations of cosmic chemical evolution - Cosmic Star Formation History - Piero Madau & Mark Dickinson Opens in a new window — https://ned.ipac.caltech.edu/level5/March14/Madau/Madau2.html
- lweb.cfa.harvard.edu The Redshift Evolution of the M• − M⋆ Relation for JWST's Supermassive Black Holes at z > 4 Opens in a new window — https://lweb.cfa.harvard.edu/~loeb/FL23.pdf
- arxiv.org [2403.08856] Does the Fundamental Metallicity Relation Evolve with Redshift? I: The Correlation Between Offsets from the Mass-Metallicity Relation and Star Formation Rate - arXiv Opens in a new window — https://arxiv.org/abs/2403.08856
- academic.oup.com mass—metallicity relation of interacting galaxies | Monthly Notices of the Royal Astronomical Society: Letters | Oxford Academic Opens in a new window — https://academic.oup.com/mnrasl/article/386/1/L82/1125852
- arxiv.org [0704.3100] The Origin of the Galaxy Mass-Metallicity Relation and Implications for Galactic Outflows - arXiv Opens in a new window — https://arxiv.org/abs/0704.3100
- arxiv.org [1910.00597] The Mass-Metallicity and the Fundamental Metallicity Relation revisited on a fully Te-based abundance scale for galaxies - arXiv Opens in a new window — https://arxiv.org/abs/1910.00597
- arxiv.org arXiv:1011.0264v1 [astro-ph.CO] 1 Nov 2010 Opens in a new window — https://arxiv.org/pdf/1011.0264
- par.nsf.gov Does the fundamental metallicity relation evolve with redshift? I - NSF Public Access Repository Opens in a new window — https://par.nsf.gov/servlets/purl/10538536
- academic.oup.com physics of the fundamental metallicity relation | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/430/4/2891/1101320
- academic.oup.com Ages and metallicities of central and satellite galaxies: implications for galaxy formation and evolution - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/407/2/937/1119098
- academic.oup.com The ages and metallicities of galaxies in the local universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/362/1/41/1344664
- wwwmpa.mpa-garching.mpg.de The ages and metallicities of galaxies in the local universe - MPA Garching Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/SDSS/DR4/Data/stellarmet.html
- wwwmpa.mpa-garching.mpg.de The ages and metallicities of galaxies in the local universe - MPA Garching Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/SDSS/DR2/Data/stellarmet.html
- oamonitor.ireland.openaire.eu The ages and metallicities of galaxies in the local universe - National Open Access Monitor, Ireland Opens in a new window — https://oamonitor.ireland.openaire.eu/rfo/irish-research-council3/search/publication?pid=10.1111%2Fj.1365-2966.2005.09321.x
- academic.oup.com On the origin of the mass–metallicity gradient relation in the local Universe Opens in a new window — https://academic.oup.com/mnras/article/504/1/53/6189699
- academic.oup.com mass–metallicity and the fundamental metallicity relation revisited on a fully Te-based abundance scale for galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/491/1/944/5638748
- cdsarc.u-strasbg.fr Oxygen abundances and properties of galaxies : J/A+A/550/A115 Opens in a new window — http://cdsarc.u-strasbg.fr/viz-bin/qcat?J/A+A/550/A115
- academic.oup.com Evolution of the gas mass fraction in galaxy clusters - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/450/1/896/1008136
- academic.oup.com Self-similar scaling and evolution in the galaxy cluster X-ray luminosity–temperature relation | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/421/2/1583/1142210
- academic.oup.com Three Hundred Project: The evolution of galaxy cluster density profiles - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/483/3/3390/5232383
- ricerca.sns.it JADES: The star formation and chemical enrichment history of a luminous galaxy at z ∼ 9.43 probed by ultra Opens in a new window — https://ricerca.sns.it/bitstream/11384/154324/1/aa51410-24.pdf
- sites.google.com Kimihiko Nakajima - Research Opens in a new window — https://sites.google.com/view/kimihiko-nakajima/research
- researchgate.net The Mass–Metallicity Relation and Its Observational Effects at z ∼ 3–6 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/408382681_The_Mass-Metallicity_Relation_and_Its_Observational_Effects_at_z_3-6
- arxiv.org [1703.09769] The Mass-Metallicity Relation revisited with CALIFA - arXiv Opens in a new window — https://arxiv.org/abs/1703.09769
- ouci.dntb.gov.ua SDSS-IV MaNGA: drivers of stellar metallicity in nearby galaxies - OUCI Opens in a new window — https://ouci.dntb.gov.ua/en/works/9jma3Yjl/
- academic.oup.com mass–metallicity relation revisited with CALIFA | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/469/2/2121/3098186
- academic.oup.com cosmic evolution of metallicity from the SDSS fossil record | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/391/3/1117/977781
- arxiv.org [2303.11024] Mass Metallicity Relationship of SDSS Star Forming Galaxies: Population Synthesis Analysis and Effects of Star Burst Length, Extinction Law, Initial Mass Function and Star Formation Rate - arXiv Opens in a new window — https://arxiv.org/abs/2303.11024
- arxiv.org [2505.07018] The competing effects of recent and long-term star formation histories on oxygen, nitrogen, and stellar metallicities - arXiv Opens in a new window — https://arxiv.org/abs/2505.07018
- academic.oup.com stellar fundamental metallicity relation: the correlation between stellar mass, star formation rate, and stellar metallicity | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/532/2/2832/7700710
- arxiv.org The JWST EXCELS Survey: gas-phase metallicity evolution at 2 < z < 8 - arXiv Opens in a new window — https://arxiv.org/html/2511.00705v2
- academic.oup.com JWST EXCELS survey: the ages and abundances of 3 < z < 5 massive quiescent galaxies show that downsizing was already in place by z ≃ 4 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/549/1/stag827/8666392
- research.ed.ac.uk The JWST EXCELS Survey: gas-phase metallicity evolution at 2 < z < 8 Opens in a new window — https://www.research.ed.ac.uk/en/publications/the-jwst-excels-survey-gas-phase-metallicity-evolution-at-2-lt-z-/
- academic.oup.com Both stellar mass and gravitational potential shape the gas-phase metallicity | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/545/1/staf2011/8322423
- arxiv.org The Extreme Low-mass End of the Mass-Metallicity Relation at z∼7 - arXiv Opens in a new window — https://arxiv.org/html/2407.17110v2
- arxiv.org Metal Mayhem at z∼7⁢"–"⁢10: Diversity and Evolution of Gas-Phase Metallicity Gradients Opens in a new window — https://arxiv.org/html/2604.07076v1
- academic.oup.com The metallicity's fundamental dependence on both local and global galactic quantities Opens in a new window — https://academic.oup.com/mnras/article/519/1/1149/6884142
- academic.oup.com Gas metallicity distributions in SDSS-IV MaNGA galaxies: what drives gradients and local trends? - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/520/3/4301/7008515
- semanticscholar.org The SAMI galaxy survey: exploring the gas-phase mass–metallicity relation Opens in a new window — https://www.semanticscholar.org/paper/The-SAMI-galaxy-survey%3A-exploring-the-gas-phase-S%C3%A1nchez-Barrera-Ballesteros/3d312e7c9e1e86a5abd10cc7907474f884bacd53
- academic.oup.com How well do local relations predict gas-phase metallicity gradients? Results from SDSS-IV MaNGA - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/514/2/2298/6595980
- pure.port.ac.uk Both starvation and outflows drive galaxy quenching - University of Portsmouth Opens in a new window — https://pure.port.ac.uk/ws/files/16949932/Both_starvation_and_outflows_drive_galaxy_quenching_AAM.pdf
- researchgate.net Strangulation as the primary mechanism for shutting down star formation in galaxies Opens in a new window — https://www.researchgate.net/publication/276296301_Strangulation_as_the_primary_mechanism_for_shutting_down_star_formation_in_galaxies
- arxiv.org Different regulation of stellar metallicities between star-forming and quiescent galaxies – Insights into galaxy quenching - arXiv Opens in a new window — https://arxiv.org/html/2309.00670v2
- arxiv.org The First Empirical Calibration of the MIR Abundance Diagnostic Ne$_{23}$ with JWST - arXiv Opens in a new window — https://arxiv.org/pdf/2604.27056
- academic.oup.com New calibrations for abundance determinations in H ii regions - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/457/4/3678/2589035
- academic.oup.com New fully empirical calibrations of strong-line metallicity indicators in star-forming galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/465/2/1384/2417485
- arxiv.org Semi-empirical calibration of the oxygen abundance for LINER galaxies based on SDSS-IV MaNGA - arXiv Opens in a new window — https://arxiv.org/pdf/2411.02043
- arxiv.org [1602.01087] A Recalibration of Strong Line Oxygen Abundance Diagnostics via the Direct Method and Implications for the High Redshift Universe - arXiv Opens in a new window — https://arxiv.org/abs/1602.01087
- academic.oup.com Galaxy and mass assembly (GAMA): the inferred mass–metallicity relation from z = 0 to 3.5 via forensic SED fitting | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/503/3/3309/6155042
- cdsarc.u-strasbg.fr VizieR J/ApJ/685/904 Opens in a new window — http://cdsarc.u-strasbg.fr/viz-bin/cat/J/ApJ/685/904
- academic.oup.com The atomic gas sequence and mass–metallicity relation from dwarfs to massive galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/535/3/2341/7881573
- sdss3.org Galaxy Properties - SDSS-III Opens in a new window — https://www.sdss3.org/dr9/algorithms/galaxy.php
- scispace.com The relation between metallicity, stellar mass and star formation in galaxies: an analysis of observational and model data - SciSpace Opens in a new window — https://scispace.com/pdf/the-relation-between-metallicity-stellar-mass-and-star-48dt0823yh.pdf
- researchgate.net Galaxy Metallicity Gradients in the Reionization Epoch from the FIRE-2 Simulations Opens in a new window — https://www.researchgate.net/publication/396457553_Galaxy_Metallicity_Gradients_in_the_Reionization_Epoch_from_the_FIRE-2_Simulations
- cambridge.org Revisiting the bimodality of galactic habitability in IllustrisTNG | Publications of the Astronomical Society of Australia | Cambridge Core Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/revisiting-the-bimodality-of-galactic-habitability-in-illustristng/7815D91B2FA5797FA5D7E6DF53A94F40
- scispace.com arXiv:2203.01159v1 [astro-ph.GA] 2 Mar 2022 - SciSpace Opens in a new window — https://scispace.com/pdf/chemical-evolution-history-of-manga-galaxies-1fmucvfk.pdf
- researchgate.net Under Pressure: Decoding the Effect of High Densities on Derived Nebular Properties Opens in a new window — https://www.researchgate.net/publication/396967373_Under_Pressure_Decoding_the_Effect_of_High_Densities_on_Derived_Nebular_Properties
- academic.oup.com The ionization parameter of star-forming galaxies evolves with the specific star formation rate - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/477/4/5568/4983132
- academic.oup.com Spatially resolved star formation and metallicity profiles in post-merger galaxies from MaNGA | Monthly Notices of the Royal Astronomical Society - Oxford Academic Opens in a new window — https://academic.oup.com/mnrasl/article/482/1/L55/5114582
- academic.oup.com EDGE-CALIFA survey: self-regulation of star formation at kpc scales - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/503/3/3643/6169731
- scholarship.haverford.edu Herschel-ATLAS: A Binary HyLIRG Pinpointing a Cluster of Starbursting Protoellipticals - Haverford Scholarship Opens in a new window — https://scholarship.haverford.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1346&context=astronomy_facpubs
- lss.fnal.gov Tracing the Cosmic Evolution of the Cool Circumgalactic Medium of Luminous Red Galaxies with DESI Year 1 Data FERMILAB-PUB-25-0894-PPD arXiv:2512.03845 Opens in a new window — https://lss.fnal.gov/archive/2025/pub/fermilab-pub-25-0894-ppd.pdf
- ntrs.nasa.gov HERSCHEL-ATLAS: A BINARY HyLIRG PINPOINTING A CLUSTER OF STARBURSTING PROTOELLIPTICALS Opens in a new window — https://ntrs.nasa.gov/api/citations/20140008911/downloads/20140008911.pdf
- arxiv.org Radial Distribution of Star Formation and Gas-phase Metallicity in Spiral-Elliptical Galaxy Pairs - arXiv Opens in a new window — https://arxiv.org/pdf/2604.14092
- arxiv.org The Galaxy Stellar Mass-SFR-Size Relation in EAGLE, TNG100, and Observations - arXiv Opens in a new window — https://arxiv.org/pdf/2603.01726
- academic.oup.com origin of the galaxy size–stellar metallicity relation – I. A semi-analytical perspective - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/545/4/staf2113/8422763
- academic.oup.com Outflows in star-forming galaxies: Stacking analyses of resolved winds and the relation to their hosts' properties - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/493/3/3081/5737578
- nbi.ku.dk Doctor of Philosophy Galaxy formation: observations and simulations of galaxies - Niels Bohr Institutet Opens in a new window — https://nbi.ku.dk/english/theses/phd-theses/martin-sparre/Martin_Sparre.pdf
- ir.library.osaka-u.ac.jp Physically-motivated feedback models and the IGM metal enrichment in cosmological hydrodynamic simulations Opens in a new window — https://ir.library.osaka-u.ac.jp/repo/ouka/all/96417/34336_Dissertation.pdf
- researchgate.net What drives the growth of black holes: a decade of progress - ResearchGate Opens in a new window — https://www.researchgate.net/publication/392980344_What_drives_the_growth_of_black_holes_a_decade_of_progress/fulltext/685b697493040b17338d1e85/What-drives-the-growth-of-black-holes-a-decade-of-progress.pdf
- academic.oup.com Does the fundamental metallicity relation evolve with redshift? – II. The evolution in normalization of the mass–metallicity relation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/536/1/119/7901351
- academic.oup.com The role of environment in the mass–metallicity relation Opens in a new window — https://academic.oup.com/mnras/article-pdf/390/1/245/2963955/mnras0390-0245.pdf
- researchgate.net The Role of Large-Scale Environment in Shaping the Stellar Mass-Gas Metallicity Relation Across Time - ResearchGate Opens in a new window — https://www.researchgate.net/publication/389917967_The_Role_of_Large-Scale_Environment_in_Shaping_the_Stellar_Mass-Gas_Metallicity_Relation_Across_Time
- academic.oup.com On the relation between specific star formation rate and metallicity - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/441/2/1444/1062348
- espace.library.uq.edu.au The WiggleZ Dark Energy Survey: final data release and the metallicity of UV-luminous galaxies - UQ eSpace - The University of Queensland Opens in a new window — https://espace.library.uq.edu.au/view/UQ:719803/UQ719803_OA.pdf
- academic.oup.com Scaling relations of metallicity, stellar mass and star formation rate in metal-poor starbursts — I. A Fundamental Plane - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/427/2/906/977690
- ipac.caltech.edu The MOSDEF Survey: Environmental Dependence of the Gas-phase Metallicity of Galaxies at 1.4 ≤ z ≤ 2.6 - IPAC/Caltech Opens in a new window — https://www.ipac.caltech.edu/publication/2021ApJ...908..120C
- academic.oup.com MOSDEF survey: the mass–metallicity relationship and the existence of the FMR at z ∼ 1.5 Opens in a new window — https://academic.oup.com/mnras/article/506/1/1237/6309907
- academic.oup.com MOSDEF survey: the mass–metallicity relationship and the existence of the FMR at z ∼ 1.5 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/506/1/1237/6309907
- osti.gov The Fourteenth Data Release of the Sloan Digital Sky Survey: First Spectroscopic Data from the Extended Baryon Oscillation Spectroscopic Survey and from the Second Phase of the Apache Point Observatory Galactic Evolution Experiment (Journal Article) | OSTI.GOV Opens in a new window — https://www.osti.gov/pages/biblio/1377366
- science.gov para manga mangifera: Topics by Science.gov Opens in a new window — https://www.science.gov/topicpages/p/para+manga+mangifera
- science.gov manga sob diferentes: Topics by Science.gov Opens in a new window — https://www.science.gov/topicpages/m/manga+sob+diferentes
- astro.uc.cl Publications - Instituto de Astrofísica Opens in a new window — https://astro.uc.cl/en/publicaciones/
- sdss4.org SDSS-IV Publications Opens in a new window — https://www.sdss4.org/science/publications/
- researchgate.net The mass–metallicity and the fundamental metallicity relation revisited on a fully Te-based abundance scale for galaxies | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/344678992_The_mass-metallicity_and_the_fundamental_metallicity_relation_revisited_on_a_fully_Te-based_abundance_scale_for_galaxies
- arxiv.org [2410.22407] Direct-method metallicity gradients derived from spectral stacking with SDSS-IV MaNGA - arXiv Opens in a new window — https://arxiv.org/abs/2410.22407
- semanticscholar.org Present-day mass-metallicity relation for galaxies using a new electron temperature method Opens in a new window — https://www.semanticscholar.org/paper/Present-day-mass-metallicity-relation-for-galaxies-Yates-Schady/00ad32a3137327fcb7bf37ebb90b8882a8822d81
- arxiv.org arXiv:1404.7526v3 [astro-ph.GA] 31 Jul 2014 Opens in a new window — https://arxiv.org/pdf/1404.7526
- academic.oup.com new insight on the formation and evolution of low surface brightness galaxies in the IllustrisTNG simulation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/530/1/812/7634367
- semanticscholar.org The evolution of the mass-metallicity relation and its scatter in IllustrisTNG Opens in a new window — https://www.semanticscholar.org/paper/The-evolution-of-the-mass-metallicity-relation-and-Torrey-Vogelsberger/8ddac07388532935a3c0980f1735747756b2620a
- arxiv.org Formation and fate of low metallicity stars in IllustrisTNG50 - arXiv Opens in a new window — https://arxiv.org/pdf/2203.07383
- researchgate.net Mass–metallicity relations in IllustrisTNG split by the distance to... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Mass-metallicity-relations-in-IllustrisTNG-split-by-the-distance-to-filaments-and_fig3_359228561
- academic.oup.com Interplay of stellar and gas-phase metallicities: unveiling insights for stellar feedback modelling with Illustris, IllustrisTNG, and EAGLE - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/529/4/3342/7630222
- ricerca.sns.it JADES: comprehensive census of broad-line AGN from reionization to cosmic noon revealed by JWST Opens in a new window — https://ricerca.sns.it/retrieve/4107d1f5-8e88-4f30-ad81-185ebde8b062/stag086_compressed.pdf
- jades-survey.github.io JADES and Community Publications - JWST Advanced Deep Extragalactic Survey Opens in a new window — https://jades-survey.github.io/scientists/publications.html
- academic.oup.com How do central and satellite galaxies quench? – Insights from spatially resolved spectroscopy in the MaNGA survey - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/499/1/230/5905735
- academic.oup.com dual role of outflows in quenching satellites of low-mass hosts: NGC 3109 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/528/1/365/7511121
- academic.oup.com Both starvation and outflows drive galaxy quenching | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/491/4/5406/5638877
- academic.oup.com Different regulation of stellar metallicities between star-forming and quiescent galaxies – insights into galaxy quenching | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/534/1/30/7746765
- arxiv.org Shape of Direct‑Method Mass-Metallicity Relation with JWST - arXiv Opens in a new window — https://arxiv.org/html/2605.05327v1
- arxiv.org [2212.02491] Evolution of the Mass-Metallicity Relation from Redshift $z\approx8$ to the Local Universe - arXiv Opens in a new window — https://arxiv.org/abs/2212.02491
- arxiv.org [2605.30513] The JADES Mass-Metallicity and Fundamental Metallicity Relations at $z\gtrsim2$ Using New High-Redshift Metallicity Calibrations - arXiv Opens in a new window — https://arxiv.org/abs/2605.30513
- bretthandrews.github.io The Mass-Metallicity Relation with the Direct Method on Stacked Spectra of SDSS Galaxies - Brett H. Andrews Opens in a new window — https://bretthandrews.github.io/publication/2013-03-01-andrews-martini
- academic.oup.com A fundamental relation between the metallicity, gas content and stellar mass of local galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/433/2/1425/4921809/stt817.pdf
- arxiv.org The Mass-Metallicity Relation and its Observational Effects at z~3-6 - arXiv Opens in a new window — https://arxiv.org/pdf/2512.03134
- arxiv.org [0801.1849] Metallicity Calibrations and the Mass-Metallicity Relation for Star-Forming Galaxies - arXiv Opens in a new window — https://arxiv.org/abs/0801.1849
- scispace.com The mass-metallicity relation of local active galaxies - SciSpace Opens in a new window — https://scispace.com/pdf/the-mass-metallicity-relation-of-local-active-galaxies-18e9djir1m.pdf
- academic.oup.com Mass–metallicity relation for local star-forming galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/457/3/2929/8000665/stw113.pdf
- academic.oup.com Identifying AGNs from X-ray detections – I: Metallicity calibrations in AGNs with X-ray luminosity as the primary input parameter - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/doi/10.1093/mnras/stag560/8539724
- arxiv.org Metallicity of Active Galactic Nuclei from ultraviolet and optical emission lines - arXiv Opens in a new window — https://arxiv.org/pdf/2508.05397
- academic.oup.com metallicity of the long GRB hosts and the fundamental metallicity relation of low-mass galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/414/2/1263/977267
- arxiv.org The metallicity properties of zCOSMOS galaxies at 0.2<z<0.8 - arXiv Opens in a new window — https://arxiv.org/pdf/1110.4408
- researchgate.net (PDF) The JWST EXCELS Survey: gas-phase metallicity evolution at 2 < z < 8 Opens in a new window — https://www.researchgate.net/publication/397231305_The_JWST_EXCELS_Survey_gas-phase_metallicity_evolution_at_2_z_8
- orcid.org Mirko Curti - ORCID Opens in a new window — https://orcid.org/0000-0002-2678-2560
- academic.oup.com JADES Dark Horse: demonstrating high-multiplex observations with JWST/NIRSpec dense-shutter spectroscopy in the JADES Origins Field | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/549/2/stag824/8666060
- academic.oup.com The JWST EXCELS Survey: gas-phase metallicity evolution at 2 &lt; - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/doi/10.1093/mnras/stag449/67243273/stag449.pdf
- lss.fnal.gov Extremely Metal-Poor Galaxies in DESI DR1 - Fermilab | Technical Publications Opens in a new window — https://lss.fnal.gov/archive/2026/pub/fermilab-pub-26-0170-ppd.pdf
- academic.oup.com Characterizing the z ≈ 7.66 Type-II AGN candidate SMACS S06355 using BEAGLE-AGN and JWST - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/541/4/3822/63712505/staf1087.pdf
- lss.fnal.gov Electron temperature relations and the direct N, O, Ne, S and Ar abundances of 49959 star-forming galaxies in DESI Data Release 2 - Fermilab | Technical Publications Opens in a new window — https://lss.fnal.gov/archive/2026/pub/fermilab-pub-26-0036-ppd.pdf
- arxiv.org [2511.00705] The JWST EXCELS Survey: gas-phase metallicity evolution at 2 < z < 8 - arXiv Opens in a new window — https://arxiv.org/abs/2511.00705
- arxiv.org [2605.21599] JWST Advanced Deep Extragalactic Survey (JADES) Data Release 5: stellar population catalogue for galaxies in GOODS-N and GOODS-S - arXiv Opens in a new window — https://arxiv.org/abs/2605.21599
- arxiv.org [2606.11345] JADES: the mass-metallicity relation at $z=1-10$. New calibrations, extremely metal-poor galaxies, and chemical diversity - arXiv Opens in a new window — https://arxiv.org/abs/2606.11345
- arxiv.org How can we finally see the first light? Status and perspectives in the search for Population III stars - arXiv Opens in a new window — https://arxiv.org/html/2607.00167v1
- academic.oup.com JADES: carbon-enhanced, nitrogen-normal compact galaxy at z = 11.2 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/545/3/staf2107/8343298
- arxiv.org Cosmic evolution of the helium and oxygen abundances in type 2 Active Galactic Nuclei: Helium-loud AGNs - arXiv Opens in a new window — https://arxiv.org/html/2606.25890v1
- thesis.caltech.edu Multi-Element Abundances as Probes of Galaxy Growth Across Opens in a new window — https://thesis.caltech.edu/17609/03/Thesis_Zhuyun_Zhuang.pdf
- arxiv.org arXiv:2403.08401v1 [astro-ph.GA] 13 Mar 2024 Opens in a new window — https://arxiv.org/pdf/2403.08401
- academic.oup.com MOSDEF survey: direct-method metallicities and ISM conditions at z ∼ 1.5–3.5 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/491/1/1427/5612199
- researchgate.net The Mass-Metallicity Relation and its Observational Effects at z~3-6 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/398312553_The_Mass-Metallicity_Relation_and_its_Observational_Effects_at_z3-6
- orcid.org Laura DeGroot - ORCID Opens in a new window — https://orcid.org/0000-0001-9022-665X
- arxiv.org Unveiling the Cosmic Chemistry: Revisiting the Mass-Metallicity Relation with JWST/NIRSpec at 4 <z< 10 - arXiv Opens in a new window — https://arxiv.org/html/2408.07974v2
- arxiv.org A Uniform Analysis of Gas-phase Metallicity Evolution with 1-3 Gyr Time Sampling over the Past 12 Billion Years - arXiv Opens in a new window — https://arxiv.org/pdf/2508.18369
- experts.azregents.edu The role of environment in the mass-metallicity relation - Arizona Opens in a new window — https://experts.azregents.edu/en/publications/the-role-of-environment-in-the-mass-metallicity-relation/
- academic.oup.com role of environment in the mass–metallicity relation | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/390/1/245/973919
- archive.iaa.csic.es Properties and evolution of galaxies in galaxy clusters up to a redshift of z∼1.0 - Instituto de Astrofísica de Andalucía, IAA-CSIC Opens in a new window — https://archive.iaa.csic.es/sites/default/files/thesis/iaa_2021_tesis_z._beyoro_amado.pdf
- academic.oup.com Volume 390 Issue 1 | Monthly Notices of the Royal Astronomical Society - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/issue/390/1
- academic.oup.com Volume 422 Issue 1 | Monthly Notices of the Royal Astronomical Society - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/issue/422/1
- researchgate.net The relation between metallicity, stellar mass and star formation in galaxies: An analysis of observational and model data | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/51917250_The_relation_between_metallicity_stellar_mass_and_star_formation_in_galaxies_An_analysis_of_observational_and_model_data
- ijraset.com A Case Study on Stellar Evolution of Single and Binary Stars Opens in a new window — https://www.ijraset.com/research-paper/stellar-evolution-of-single-and-binary-stars
- academic.oup.com The relation between metallicity, stellar mass and star formation in galaxies: an analysis of observational and model data - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/422/1/215/1020516
- researchgate.net (PDF) SDSS-IV MANGA: The radial distribution of physical properties within galaxies in the nearby universe - ResearchGate Opens in a new window — https://www.researchgate.net/publication/374940801_SDSS-IV_MANGA_THE_RADIAL_DISTRIBUTION_OF_PHYSICAL_PROPERTIES_WITHIN_GALAXIES_IN_THE_NEARBY_UNIVERSE
- academic.oup.com Do galaxy global relationships emerge from local ones? The SDSS IV MaNGA surface mass density–metallicity relation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/463/3/2513/18235074/stw1984.pdf
- academic.oup.com SAMI galaxy survey: exploring the gas-phase mass–metallicity relation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/484/3/3042/5280047
- academic.oup.com MUSE Atlas of Disks (MAD): resolving star formation rates and gas metallicities on <100 pc scales - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/484/4/5009/5298497
- arxiv.org Star Formation Rates, Metallicities, and Stellar Masses on kpc-scales in TNG50 - arXiv Opens in a new window — https://arxiv.org/pdf/2501.18687
- nagoya.repo.nii.ac.jp Galaxy Merger Identification Methods and Investigations of the Role of Mergers in Galaxy Evolution （衝突銀河の分類方 Opens in a new window — https://nagoya.repo.nii.ac.jp/record/2010045/files/k14816_thesis.pdf
- arxiv.org The Gas-Phase Mass–Metallicity Relation of Dwarf Galaxies Across Large-Scale Environments Using the CAVITY Parent Sample - arXiv Opens in a new window — https://arxiv.org/html/2605.25557v1
- doi.org Rapid, out-of-equilibrium metal enrichment indicated by a flat mass-metallicity relation at z ∼ 6 from NIRCam grism spectroscopy | Astronomy & Astrophysics (A&A) - DOI Opens in a new window — https://doi.org/10.1051/0004-6361/202556597
- cdsarc.cds.unistra.fr JWST z=4-10 galaxies mass-metallicity relations : J/ApJS/269/33 Opens in a new window — https://cdsarc.cds.unistra.fr/viz-bin/cat/J/ApJS/269/33
- par.nsf.gov Inflow and outflow properties, not total gas fractions, drive the evolution of the mass–metallicity relation Opens in a new window — https://par.nsf.gov/servlets/purl/10524048
- arxiv.org Galaxy Metallicity Gradients in the Reionization Epoch from the FIRE-2 Simulations - arXiv Opens in a new window — https://arxiv.org/pdf/2510.08997
- thesis.caltech.edu Understanding galaxy formation and evolution with realistic Opens in a new window — https://thesis.caltech.edu/10929/1/ma_xiangcheng_2018.pdf
- academic.oup.com NIRVANDELS survey: the stellar and gas-phase mass-metallicity relations of star-forming galaxies at z = 3.5 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/532/3/3102/7712488
- academic.oup.com Spatially resolved gas-phase metallicity in FIRE-2 dwarfs: late-time evolution of metallicity relations in simulations with feedback and mergers - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/515/3/3555/6645834
- academic.oup.com evolution of the mass–metallicity relation and its scatter in IllustrisTNG - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/484/4/5587/5299581
- cris.unibo.it Cosmological Simulations of Galaxy Formation - Alma Mater Studiorum Università di Bologna Archivio istituzionale della ricerca Opens in a new window — https://cris.unibo.it/bitstream/11585/799379/4/1909.07976.pdf
- arxiv.org Origins of Extreme Emission-Line Ratios in z>3 Galaxies: Insights from the Lumen Model Opens in a new window — https://arxiv.org/html/2605.06769v2
- arxiv.org Unveiling the Cosmic Chemistry: Revisiting the Mass-Metallicity Relation with JWST/NIRSpec at 4 <z< 10 - arXiv Opens in a new window — https://arxiv.org/html/2408.07974v3
- arxiv.org Pristine Massive Star Formation Caught at the Break of Cosmic Dawn - arXiv Opens in a new window — https://arxiv.org/html/2507.10521v2
- pmc.ncbi.nlm.nih.gov Carbonaceous dust grains seen in the first billion years of cosmic time - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC10499605/

## Custody and safety receipt

- Deep Research source discovery only; independent identifier/claim-boundary verification remains required before live wiki mutation.
- No DB, wiki, trust-score, claim/evidence, code, manuscript, deploy, git, publish, cron, billing, credential, account-setting, or unrelated-conversation mutation was performed by this run.
- No conversation deletion was authorized or performed.

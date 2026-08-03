# Review Base 05 raw Deep Research packet — Maiolino & Mannucci 2019

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_05_maiolino_mannucci_2019_DR_PROMPT.md`
Prompt SHA-256: `9534674dea042af4d3ae61eee3a8816ff1bd1a6c061adcda5026d7e451d3c3a5`
Conversation ID: `c5df8c52cb041e99`
Submit UTC: `2026-07-15T15:19:28Z`
Research Start UTC: `2026-07-15T15:26:18.455881Z`
Result captured UTC: `2026-07-15T15:40:29.631800Z`
Raw result SHA-256: `aa9f160699f5add472671b400bf486bf367256551658fd2ec0a425668365013e`

## Deep Research review-base result

Review Identity and Scope Map

Review Identity
The core review analyzed for this advisory source base is exactly titled "De re metallica: the cosmic chemical evolution of galaxies" by Roberto Maiolino and Filippo Mannucci, published in 2019 in The Astronomy and Astrophysics Review, volume 27, article 3. Its verified digital object identifier is 10.1007/s00159-018-0112-2, the arXiv preprint identifier is 1811.09642, and the SAO/NASA Astrophysics Data System (ADS) bibcode is 2019A&ARv..27....3M.   

Map of Authorized Scientific Territory
This synthesis comprehensively maps the chemical evolution of galaxies from the local Universe out to cosmic noon, as the field was understood prior to 2019. It establishes the foundational observational frameworks for determining gas-phase, stellar, and circumgalactic medium (CGM) metallicities. The scientific territory covers the systemic offsets between differing diagnostic calibrations, most notably the persistent discrepancy between empirical electron-temperature (T
e
	​

) methods and theoretical photoionization models. The review formally bounds the scaling relations that control galactic metal content, prominently the Mass-Metallicity Relation (MZR) and the Fundamental Metallicity Relation (FMR), which link stellar mass, metallicity, and star formation rate (SFR) or neutral gas mass. Furthermore, it codifies the 2019 state of knowledge regarding spatially resolved metallicity gradients, relative abundance ratios (such as α/Fe and N/O), and the constraints placed on the cosmic metal budget (metals retained versus metals expelled into the intergalactic medium). Analytical equilibrium models (often termed "bathtub" models) and cosmological hydrodynamic simulations are strictly authorized as the theoretical interpretive frameworks.   

Explicit Exclusions and Boundary Conditions
The authorized scope maintains rigorous physical boundary conditions. Gas-phase metallicities (derived from HII regions and diffuse ionized gas), stellar metallicities (derived from photospheric continuum and absorption lines), neutral-gas metallicities (derived from damped Lyman-alpha systems), and CGM/IGM metallicities (derived from absorption lines) are treated as physically distinct properties tracing inherently different temporal and spatial enrichment scales. They must never be conflated into a single, interchangeable metric. Calibration boundaries dictate that the absolute abundance scale remains a recognized unknown; scaling relations may only be compared within identical calibration baselines.   

Observational samples and redshift boundaries are strictly limited to pre-JWST optical and near-infrared spectroscopy (such as SDSS, CALIFA, MaNGA, AMAZE, and zC-SINF). High-redshift diagnostics are explicitly cautioned as being potentially compromised by evolving interstellar medium (ISM) conditions. Active Galactic Nuclei (AGN) are rigorously quarantined. While hard AGN ionizing fields contaminate strong-line diagnostic ratios on the BPT diagram, AGN demographic tracking, accretion physics, and purely AGN-focused evolutionary claims are explicitly excluded from this core galaxy-evolution harvest. Finally, any instruments, discoveries, or methodologies published after 2019 are unauthorized for this source base.   

Established Findings
Finding 1: The Asymptotic Saturation of the Mass-Metallicity Relation
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E01]	Core mechanism	review_synthesis	Gas-phase HII regions; z~0 samples; dependent on assumed IMF and strong-line calibration scale.	MZR scaling relations	High	[REV05-P001], [REV05-P008]

The Mass-Metallicity Relation (MZR) demonstrates a ubiquitous, non-linear correlation where gas-phase oxygen abundance increases steeply with stellar mass in low-mass galaxies, but smoothly turns over and asymptotes to a saturation metallicity in massive galaxies above approximately 10
10.5
M
⊙
	​

. This behavior traces the deep physical interplay between a galaxy's gravitational potential well and its ability to retain heavy elements against the outward pressure of supernovae-driven galactic winds. In low-mass dwarf systems, shallow potential wells allow core-collapse supernovae to effectively eject a substantial fraction of newly synthesized metals into the circumgalactic medium, suppressing the ISM metallicity. Conversely, in massive galaxies, the deep potential well retains almost all synthesized metals. The observed saturation at high masses reflects the asymptotic limit of the effective yield, dictated primarily by the Initial Mass Function (IMF) and the fraction of gas continually locked into long-lived stars and stellar remnants, rather than by variations in wind efficiency. The exact mass at which this turnover occurs, and the absolute metallicity of the saturation plateau, remain heavily dependent on the chosen strong-line calibration and the assumed oxygen-to-hydrogen solar reference.   

Finding 2: The Star Formation Rate as the Secondary Driver of Metallicity
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E02]	Core mechanism	observation	Local Universe statistical samples; parameterized via H-alpha or UV-derived Star Formation Rates.	The Fundamental Metallicity Relation	High	[REV05-P003], [REV05-P041], [REV05-P042]

The Fundamental Metallicity Relation (FMR) adds a critical secondary dependence to the MZR by establishing that at a fixed stellar mass, the gas-phase metallicity is systematically anti-correlated with the current Star Formation Rate (SFR). Local galaxies define a tight, three-dimensional manifold in the parameter space of stellar mass, gas-phase metallicity, and SFR, with a remarkably small residual dispersion of approximately 0.05 dex. This anti-correlation is understood as a consequence of the stochastic accretion of pristine, metal-poor gas from the intergalactic medium. When a galaxy experiences an influx of metal-poor gas, the immediate physical consequence is twofold: the existing metal content of the interstellar medium is diluted (lowering the observable gas-phase oxygen abundance), and the influx of cold fuel triggers a starburst (raising the SFR). Over subsequent hundreds of millions of years, the newly formed massive stars synthesize and release metals back into the ISM, gradually moving the galaxy back toward an equilibrium state characterized by lower SFR and higher metallicity. This mechanism explains why galaxies undergoing intense starbursts consistently fall below the mean MZR curve for their given stellar mass.   

Finding 3: The Primary and Secondary Nucleosynthetic Origins of Nitrogen
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E03]	Abundance diagnostic	observation	HII region direct and strong-line methods; breakpoint heavily influenced by absolute calibration scale.	Relative abundances and N/O	High	[REV05-P020], [REV05-P022]

Nitrogen-to-Oxygen (N/O) abundance ratios exhibit a distinct "hockey stick" distribution as a function of overall oxygen abundance, reflecting the dual nucleosynthetic pathways of nitrogen production. At low metallicities, N/O forms a flat, constant plateau independent of the oxygen abundance. In this regime, nitrogen behaves as a "primary" element, synthesized directly from carbon and oxygen that are themselves freshly forged within the same massive star during hydrogen and helium burning. Because primary nitrogen and oxygen are co-produced and ejected on identical, rapid timescales by core-collapse supernovae, their ratio remains constant. However, as the global metallicity of the galaxy increases beyond a specific threshold (roughly 12+log(O/H)≈8.0 depending on the calibration), the N/O ratio rises steeply. In this high-metallicity regime, nitrogen is produced as a "secondary" element via the CNO cycle in intermediate-mass asymptotic giant branch (AGB) stars. The CNO cycle utilizes pre-existing carbon and oxygen that the star incorporated from the ISM at birth. Consequently, secondary nitrogen production scales proportionally with the initial metallicity of the stellar population, causing the N/O ratio to increase rapidly as galactic chemical enrichment proceeds.   

Finding 4: Steady-State Equilibrium in Analytical Galaxy Models
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E04]	Theoretical framework	analytic_theory	Assumes perfect instantaneous mixing of ISM; applies to secular evolution phases.	Chemical evolution models	High	[REV05-P011], [REV05-P012]

Analytical "bathtub" or gas-regulator models have successfully demonstrated that the scaling relations of galaxies (such as the MZR and FMR) can be elegantly reproduced by treating galaxies as idealized, regulated reservoirs of gas. In these equilibrium models, the rate of change of the gas mass and metal mass is governed entirely by the balance between cosmological gas inflow, star-formation-driven depletion, and feedback-driven metal-enriched outflows. A core finding of these models is that galaxies rapidly reach a quasi-steady state where the star formation rate dynamically adjusts to equal the net gas inflow rate minus the outflow rate. Under this equilibrium assumption, the gas-phase metallicity becomes largely independent of the galaxy's initial conditions or exact star formation history; instead, it is determined instantaneously by the effective stellar yield, the mass-loading factor of the galactic winds, and the metallicity of the infalling gas. The success of these models in reproducing the observed tightness of the FMR provides robust theoretical backing for the view that galaxies evolve secularly through continuous self-regulation over cosmic time.   

Finding 5: Universal Inside-Out Metallicity Gradients
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E05]	Spatial distribution	observation	Local, non-interacting massive disk galaxies; spatially resolved via IFU surveys.	Spatially resolved gradients	High	[REV05-P018], [REV05-P019]

Massive, non-interacting star-forming disk galaxies in the local Universe exhibit universally negative radial gas-phase oxygen abundance gradients when spatially normalized to the disk's effective radius (R
e
	​

). IFU surveys such as CALIFA and MaNGA have conclusively shown that the inner regions of spiral galaxies are highly enriched, while the metallicity steadily declines toward the outer disk. This negative gradient is a primary observational signature of the "inside-out" paradigm of galactic disk formation. In this framework, the deep central potential wells accrete gas and form stars early and rapidly, undergoing extensive chemical recycling and metal buildup over billions of years. Conversely, the outer disks assemble later from higher angular momentum, metal-poor gas accreting from the cosmic web. The striking uniformity of the gradient slope across diverse disk galaxies suggests that the efficiency of star formation, the radial profile of stellar feedback, and the gradual inward migration of gas are tightly coupled processes that universally govern the spatial distribution of heavy elements in undisturbed rotating disks.   

Finding 6: The Systematic Offset of the Absolute Abundance Scale
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E06]	Diagnostic baseline	calibration	Ubiquitous offset across all HII regions; photoionization models assume ideal geometries.	Calibration offsets	High	[REV05-P015], [REV05-P030]

A profound, systematic discrepancy exists in the absolute calibration of the gas-phase oxygen abundance scale. The direct electron-temperature (T
e
	​

) method, which relies on the detection of faint auroral emission lines (such as [OIII] 4363 Å) to measure the kinetic temperature of the ionized gas, consistently yields oxygen abundances that are 0.2 to 0.5 dex lower than the abundances derived from theoretical photoionization models. Photoionization codes (such as MAPPINGS or Cloudy) attempt to match ratios of strong collisionally excited lines by modeling the complex radiation transfer, gas density, and ionization structure of idealized nebulae. The systematic offset between these two fundamentally different approaches means that the exact position of the MZR, the absolute metal budget of the universe, and the precise calculation of stellar yields remain highly uncertain. The review firmly establishes that comparing metallicities derived from T
e
	​

-based empirical calibrations against those derived from photoionization models is scientifically invalid; all scaling relations must be evaluated relative to a single, explicitly declared calibration baseline.   

Finding 7: Downward Normalization of the High-Redshift MZR
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E07]	High-redshift evolution	observation	Rest-optical stacked spectra at z~2-3; highly sensitive to BPT locus shifts.	Redshift evolution	High	[REV05-P027], [REV05-P028]

The Mass-Metallicity Relation undergoes a significant, systematic downward shift in normalization with increasing redshift. Observations of star-forming galaxies during cosmic noon (z∼2−3) reveal that for a given stellar mass, the gas-phase oxygen abundance was substantially lower in the past than it is in the local Universe. This evolutionary trend provides a direct macroscopic record of the cosmic chemical enrichment history. At high redshifts, galaxies possessed higher gas fractions and were actively assembling their stellar mass through the vigorous accretion of pristine gas from the intergalactic medium. This intense inflow diluted the ISM, keeping the global metallicity depressed despite high specific star formation rates. As the universe aged and cosmological accretion rates dwindled, the continuous recycling of gas through stellar generations gradually increased the metal content of the ISM, slowly raising the normalization of the MZR to its present-day location.   

Finding 8: The Circumgalactic Medium as the Dominant Metal Reservoir
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E08]	Metal budget	observation	Local L* galaxies via COS-Halos; heavily dependent on highly ionized OVI column densities.	Metal budgets and missing metals	Medium-High	[REV05-P007], [REV05-P009]

The extended Circumgalactic Medium (CGM) serves as a vast, highly ionized reservoir for expelled heavy elements, fundamentally altering the calculus of galactic metal budgets. Observations using background quasar sightlines to probe the halos of local L
∗
 galaxies (e.g., the COS-Halos survey) have detected massive quantities of metals out to impact parameters of 150 kpc, traced primarily by highly ionized OVI absorption. Detailed accounting reveals that the CGM contains approximately 40% of all the heavy elements ever synthesized by the galaxy's stars. This mass of expelled metals equals or exceeds the total mass of metals retained within the stars, interstellar gas, and interstellar dust of the galactic disk combined. This finding robustly confirms the efficiency of feedback mechanisms (such as supernovae and stellar winds) in ejecting enriched material completely out of the gravitational potential of the star-forming disk, distributing the products of nucleosynthesis across vast circumgalactic scales.   

Finding 9: Environmental Dilution and Gradient Flattening in Mergers
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E09]	Galactic dynamics	observation	Interacting galaxy pairs in the local universe; strong-line IFU mapping.	Environmental and merger effects	High	[REV05-P034], [REV05-P035]

Major galaxy mergers and strong tidal interactions systematically disrupt the universal negative metallicity gradients observed in isolated disk galaxies. During an interaction, strong non-axisymmetric gravitational torques induce profound losses of angular momentum in the extended, metal-poor gas of the outer disk. This gas rapidly funnels inward toward the galactic center, triggering a massive nuclear starburst. Consequently, this inflow significantly dilutes the highly enriched nuclear ISM, causing a sharp drop in central metallicity. Observations of local interacting pairs demonstrate that this process severely flattens, or even fully washes out, the pre-existing radial abundance gradient. This mechanism empirically demonstrates that the macroscopic spatial distribution of chemical elements within a galaxy is highly sensitive not only to secular inside-out star formation but also to the violent environmental dynamics that periodically redistribute angular momentum and mass.   

Finding 10: The Alpha-to-Iron Ratio as a Cosmic Clock

| ID | Role | Epistemic Type | review_synthesis | Physical / Calibration Boundary | Topic Basis | Confidence | Source Keys |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [REV05-E10] | Nucleosynthetic channel | review_synthesis | Derived from stellar photospheric absorption lines; tracks duration of massive starbursts. | Relative abundance ratios | High | [REV05-P023], [REV05-P037] |

The relative abundance ratio of alpha-elements to iron (α/Fe) serves as an indispensable cosmic clock, allowing astronomers to reconstruct the timescale over which a galaxy formed its stars. Alpha-elements (such as oxygen, magnesium, and silicon) are synthesized almost exclusively in massive stars and are ejected into the ISM via core-collapse supernovae on rapid timescales, typically within a few million to tens of millions of years after a starburst. In contrast, the bulk of iron-peak elements are synthesized by Type Ia supernovae, which result from the thermonuclear explosions of white dwarfs in binary systems. The evolution of these binary systems introduces a significant time delay, taking hundreds of millions to several billions of years to release their iron into the ISM. Therefore, a galaxy (or a specific stellar population, such as a massive elliptical galaxy or a galactic bulge) that exhibits a high super-solar α/Fe ratio must have formed the majority of its stars in a rapid, intense burst that quenched before Type Ia supernovae had time to enrich the gas with iron.   

Finding 11: The Persistent Abundance Discrepancy Factor (ADF)
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E11]	Interstellar medium physics	calibration	High S/N local HII regions; requires detection of extremely faint recombination lines.	Direct methods and recombination lines	High	[REV05-P038], [REV05-P044]

Within individual, spatially resolved HII regions, a persistent discrepancy exists between metallicities derived from two distinct types of emission lines, a phenomenon quantified as the Abundance Discrepancy Factor (ADF). Heavy element abundances derived from faint optical Recombination Lines (RLs) are systematically higher—often by factors of two or more—than abundances derived from the classical Collisionally Excited Lines (CELs) within the exact same ionized nebula. The emissivity of CELs depends exponentially on the electron temperature of the gas, making them highly efficient coolants but rendering their derived abundances severely susceptible to internal temperature fluctuations. Conversely, the emissivity of RLs possesses only a weak, inverse power-law dependence on temperature. If macroscopic temperature fluctuations exist within the nebula, the CEL emission will be heavily biased toward the hottest, most metal-poor zones, leading an observer to underestimate the total oxygen abundance. The ADF represents a critical failure in our assumption of isothermal nebulae, demonstrating that the internal physical structure of HII regions imposes a fundamental limit on the precision of gas-phase abundance determinations.   

Finding 12: Gas Mass as the Primary Driver of FMR Scatter
ID	Role	Epistemic Type	Physical / Calibration Boundary	Topic Basis	Confidence	Source Keys
[REV05-E12]	Metallicity dependence	observation	Local universe samples requiring both HI 21cm and CO molecular gas emission maps.	Gas fractions and the FMR	Medium-High	[REV05-P005], [REV05-P029]

While the standard Fundamental Metallicity Relation is parameterized using the Star Formation Rate, deep radio and millimeter surveys reveal that the FMR is fundamentally a projection of a tighter physical relationship between metallicity, stellar mass, and the neutral gas mass (specifically HI and H
2
	​

). Because the SFR is intrinsically linked to the available gas reservoir via the Kennicutt-Schmidt relation, an increase in gas mass naturally drives an increase in SFR. However, chemical evolution models and observational evidence demonstrate that it is the total mass of the hydrogen gas itself—acting as the diluting solvent for the heavy elements—that directly controls the gas-phase oxygen abundance. When galaxies of a fixed stellar mass are binned by their HI gas fraction rather than their SFR, the scatter in the resulting mass-metallicity-gas relation is minimized, suggesting that the instantaneous gas content is a more direct, fundamental physical metric of a galaxy's evolutionary state than the SFR, which represents merely the current efficiency of gas consumption.   

Open Debates and Tensions
Tension 1: The Direct vs. Strong-Line Abundance Scale
ID	Competing Positions	Boundaries	Source Keys
[REV05-D01]	Empirical T
e
	​

 methods yield low metallicities vs. Photoionization models yield high metallicities.	Global gas-phase ISM metallicities.	[REV05-P002], [REV05-P004], [REV05-P015]

Debate: The absolute calibration scale of gas-phase metallicity remains an unresolved tension, characterized by a systematic discrepancy of up to 0.5 dex. Empirical calibrations anchor the abundance scale using electron temperatures derived from faint auroral lines, establishing a relatively low absolute metallicity for the local universe. Conversely, calibrations based on theoretical photoionization grids (which model the atomic physics, geometry, and radiation fields of idealized nebulae) systematically return much higher oxygen abundances for the same strong-line ratios.
Why unresolved in 2019: The tension remained unresolved because both methodologies suffer from unconstrained systematic errors. Empirical methods may underestimate metallicity due to unresolved temperature fluctuations within HII regions, heavily weighting the hottest, most metal-poor zones. Photoionization models, however, are forced to make simplistic assumptions regarding nebular geometry, the hardness of the ionizing stellar spectra, and the highly uncertain depletion of heavy elements onto dust grains, potentially overestimating the true gas-phase abundance.   

Tension 2: The Reality and Origin of the Abundance Discrepancy Factor (ADF)
ID	Competing Positions	Boundaries	Source Keys
[REV05-D02]	Macroscopic temperature fluctuations (t
2
) vs. Chemically inhomogeneous dense clumps.	Spatially resolved local HII regions.	[REV05-P038], [REV05-P044]

Debate: The systematic offset between abundances derived from recombination lines (RLs) and collisionally excited lines (CELs) within individual HII regions sparked fierce debate regarding the internal physics of nebulae. The classical explanation posits that macroscopic temperature fluctuations (parameterized as t
2
) exist throughout the nebula, biasing CELs to artificially low abundance measurements. A competing theory argues that HII regions contain cold, highly dense, hydrogen-poor, metal-rich droplets that emit strongly in RLs but are entirely invisible in CELs due to rapid cooling.
Why unresolved in 2019: Current optical integral field spectrographs lacked the extreme spatial resolution necessary to directly image these hypothesized dense, metal-rich droplets. Furthermore, purely theoretical models struggled to explain how such massive temperature fluctuations could be sustained hydrodynamically without rapidly dissipating, leaving the true physical origin of the ADF an open question in nebular astrophysics.   

Tension 3: The High-Redshift Invariance of the FMR
ID	Competing Positions	Boundaries	Source Keys
[REV05-D03]	The FMR is a universal, redshift-invariant manifold vs. High-z galaxies deviate due to bursty, non-equilibrium evolution.	Galaxies at z∼2−3; highly dependent on calibration choices.	[REV05-P003], [REV05-P028]

Debate: The formulation of the Fundamental Metallicity Relation initially posited that the 3D surface defined by Mass, Metallicity, and SFR was entirely redshift-invariant, implying that galaxies at z=2.5 simply populated the high-SFR, low-metallicity tail of the local relation. However, competing high-redshift spectroscopic surveys reported that galaxies at cosmic noon systematically fell below this local manifold, possessing metallicities too low even for their elevated star formation rates.
Why unresolved in 2019: The debate persisted due to the severe observational difficulties in measuring metallicities at high redshift. Different teams utilized different strong-line calibrations, assumed different initial mass functions, and suffered from severe selection biases favoring the brightest, most UV-luminous starbursts. Until a single, robust metallicity diagnostic could be applied uniformly from z=0 to z=3, whether early galaxies evolved smoothly in secular equilibrium or chaotically via bursty accretion remained deeply contested.   

Tension 4: High-Redshift Diagnostic Evolution on the BPT Diagram
ID	Competing Positions	Boundaries	Source Keys
[REV05-D04]	Harder ionizing radiation fields vs. Elevated N/O ratios or high electron densities.	Rest-optical strong-line emission (e.g., [OIII]/H$\beta$ vs [NII]/H$\alpha$) at z>1.5.	[REV05-P024], [REV05-P025]

Debate: High-redshift star-forming galaxies systematically exhibit an offset locus on the classical BPT diagnostic diagram compared to local galaxies, shifting toward higher [OIII]/H$\beta$ and [NII]/H$\alpha$ ratios. One camp argues this shift is driven by harder ionizing radiation fields produced by metal-poor massive stars and high stellar binary fractions in the early universe. Another camp argues the shift is primarily a chemical effect, driven by anomalously high N/O ratios or extreme electron densities and ionization parameters within highly pressurized early HII regions.
Why unresolved in 2019: Rest-optical spectra at z∼2 shifted into the near-infrared, making it observationally expensive to obtain the full suite of diagnostic lines (including [SII], [OII], and auroral lines) necessary to break the degeneracy between ionization parameter, ISM pressure, and exact N/O abundance ratios. Thus, local strong-line calibrations applied blindly to high-z spectra carried enormous, unquantified systematic errors.   

Tension 5: Inflow vs. Outflow Control of the MZR
ID	Competing Positions	Boundaries	Source Keys
[REV05-D05]	Differential mass-loading of galactic winds vs. Variable efficiencies of pristine gas accretion.	Cosmological hydrodynamic simulations and analytic bathtub models.	[REV05-P011], [REV05-P013]

Debate: While the astrophysics community broadly agreed that feedback regulates the MZR, the exact control mechanism remained contested. "Outflow control" theories posited that the steep slope of the low-mass MZR is entirely dictated by the mass-loading factor of supernovae winds, which efficiently blow metals out of shallow potential wells. Conversely, "inflow control" theories argued that low-mass galaxies are simply more efficient at accreting large volumes of pristine, diluting hydrogen gas relative to their star formation rates, naturally depressing their metallicities without requiring extreme metal expulsion.
Why unresolved in 2019: Both physical scenarios could successfully reproduce the observed z=0 Mass-Metallicity Relation by tuning the highly unconstrained sub-grid feedback parameters in cosmological simulations. Breaking this degeneracy required precise, simultaneous measurements of the metal content in both the ISM and the extended CGM across a wide range of galaxy masses, data which remained sparse.   

Tension 6: Gradient Flattening and Inversion at High Redshift
ID	Competing Positions	Boundaries	Source Keys
[REV05-D06]	Physical inversions due to massive central accretion vs. Artifacts of beam smearing and low resolution.	z∼1.5−3 spatially resolved IFU spectroscopy.	[REV05-P006], [REV05-P036]

Debate: Observations of galaxies at cosmic noon occasionally revealed flat or even positive (inverted) radial metallicity gradients, where the central core was highly metal-poor compared to the outer disk. Theorists eagerly interpreted this as a direct signature of massive, cold gas streams funneling pristine gas directly from the cosmic web into galactic centers, triggering starbursts and diluting nuclear metallicity. Skeptics argued these inversions were largely observational artifacts caused by severe atmospheric beam smearing, low signal-to-noise ratios, and the blending of distinct HII regions within the large physical pixels of ground-based near-infrared integral field spectrographs.
Why unresolved in 2019: Adaptive optics IFU capabilities were still maturing, and observing isolated, undisturbed rotating disks at z=2 with sub-kiloparsec spatial resolution remained exceedingly difficult. Thus, distinguishing true physical inversions from instrumental blurring was rarely definitive.   

Tension 7: Yield, IMF, and Time-Delay Degeneracies
ID	Competing Positions	Boundaries	Source Keys
[REV05-D07]	Variations in α/Fe reflect true star-formation histories vs. Variations reflect changes in the IMF or theoretical yield uncertainties.	Analytical chemical evolution models; stellar population synthesis.	[REV05-P023], [REV05-P032], [REV05-P037]

Debate: Reconstructing galactic star-formation histories by measuring the α/Fe ratio is plagued by interconnected theoretical degeneracies. The "clock" relies entirely on knowing exactly how much oxygen a core-collapse supernova produces, and exactly how long a Type Ia supernova takes to detonate. If the Initial Mass Function (IMF) is not universal—meaning early galaxies formed more massive stars than local galaxies—the production of alpha-elements would surge independently of the star-formation duration.
Why unresolved in 2019: The theoretical nucleosynthetic yields of massive stars varied by factors of 2 to 4 depending on the specific stellar evolution code, particularly regarding the highly uncertain treatment of mass loss, rotation, and the carbon-production channel. Without independent confirmations of the high-redshift IMF, chemical bookkeeping models remained inherently degenerate.   

Tension 8: The Missing Metals in the Intergalactic Medium
ID	Competing Positions	Boundaries	Source Keys
[REV05-D08]	Metals reside in the unobservable hot, low-density WHIM vs. Theoretical stellar yields drastically overpredict metal production.	Cosmic metal budget calculations at z∼0.	[REV05-P007], [REV05-P009]

Debate: Even after accounting for the massive metal reservoirs discovered in the CGM by the COS-Halos survey, comprehensive cosmic metal budgets revealed that roughly 30% to 40% of all the heavy elements synthesized over cosmic history remained entirely unaccounted for. One position argued these "missing metals" were shock-heated to millions of degrees and dispersed into the vast, low-density Warm-Hot Intergalactic Medium (WHIM), rendering them invisible to standard UV absorption techniques. The opposing view suggested that theorists simply over-estimated the true net metal yield of supernovae, meaning the missing metals never existed in the first place.
Why unresolved in 2019: X-ray telescopes lacked the extreme spectral resolution and sensitivity required to detect the faint absorption lines of highly ionized metals (like OVII and OVIII) in the ultra-diffuse WHIM. Simultaneously, stellar nucleosynthesis models could not confidently constrain the fraction of metals that fall back into black holes during core-collapse supernovae, leaving the true cosmic yield highly uncertain.   

Key Measurements, Model Benchmarks, and Calibrations
ID	Value / Equation	Role	Boundary & Caveats	Source Keys
[REV05-N01]	12+log(O/H)=8.69	Solar Oxygen Reference	Status: Calibrated. Boundary: Photospheric calibration standard anchoring the local ISM metallicity scale. Caveat: Highly dependent on 3D non-LTE atmospheric modeling.	[REV05-P043]
[REV05-N02]	μ
0.32
	​

=log(M
∗
	​

)−0.32log(SFR)	FMR Projection Parameter	Status: Calibrated. Boundary: Local SDSS galaxies. Minimizes the scatter of the 3D mass-metallicity-SFR relation to ∼0.05 dex. Caveat: Derivation is highly specific to the IMF and the SFR diagnostics used.	[REV05-P003]
[REV05-N03]	∼−0.1 dex/R
e
	​

 (or ∼−0.05 dex/kpc)	Typical Local Gradient Slope	Status: Observed. Boundary: Universal oxygen abundance gradient observed in non-interacting local star-forming disks, outside the central bulge.	[REV05-P018]
[REV05-N04]	10
10.5
M
⊙
	​

	MZR Turnover Mass	Status: Observed. Boundary: The characteristic stellar mass at which the gas-phase MZR asymptotically flattens in the local universe. Caveat: Exact value shifts based on assumed strong-line calibration.	[REV05-P001]
[REV05-N05]	12+log(O/H)=8.505−0.221×O3N2	O3N2 Empirical Calibration	Status: Calibrated. Boundary: Anchored using T
e
	​

-derived metallicities from 3423 HII regions in the CALIFA survey. Caveat: Suffers from secondary dependencies on ionization parameter.	[REV05-P030]
[REV05-N06]	20%−25%	Metal Retention Fraction	Status: Observed / Calculated. Boundary: The fraction of synthesized metals retained in stars, ISM gas, and ISM dust in typical L
∗
 galaxies at z=0. Caveat: Heavily dependent on assumed theoretical stellar yields.	[REV05-P007]
[REV05-N07]	log(N/O)≈−1.5	Primary Nitrogen Floor	Status: Observed. Boundary: The baseline ratio observed in extreme low-metallicity dwarf galaxies where N is synthesized purely via primary mechanisms.	[REV05-P021], [REV05-P022]
[REV05-N08]	40%	CGM Metal Reservoir	Status: Observed / Calculated. Boundary: The mass fraction of produced metals residing in the extended circumgalactic medium (out to ∼150 kpc) of local L
∗
 galaxies. Caveat: Dominated by OVI requiring complex ionization corrections.	[REV05-P007], [REV05-P009]
What Remained Unknown in 2019
ID	The Gap	Why It Matters	Needed Test	Source Keys
[REV05-U01]	The true absolute zero-point of the gas-phase metallicity scale.	Systematic offsets of ∼0.4 dex between empirical T
e
	​

 methods and theoretical photoionization calibrations drastically alter calculations of effective yields, galactic metal budgets, and limits on feedback models.	Wide-scale application of temperature-independent abundance diagnostics (e.g., far-IR fine-structure lines) across large statistical galaxy samples.	[REV05-P002], [REV05-P004], [REV05-P015]
[REV05-U02]	The evolution of the Fundamental Metallicity Relation at z>3.	Determining if the FMR is invariant at high redshift answers whether early galaxies evolved via secular equilibrium (where inflow balances outflow and SFR) or via highly stochastic, bursty accretion events.	High S/N near-IR spectroscopy targeting rest-optical lines in representative z>3 samples to firmly map the 3D M-Z-SFR manifold.	[REV05-P003], [REV05-P028]
[REV05-U03]	The exact physical drivers shifting the BPT diagnostic locus at high redshift.	Without understanding if high-z galaxies possess harder ionizing spectra, higher gas densities, or distinct N/O ratios, applying local strong-line calibrations to high-z spectra introduces massive, unquantified systematic biases.	Direct measurements mapping massive star binary fractions, ionizing spectra, and electron densities in local extreme-excitation analog galaxies.	[REV05-P024], [REV05-P025]
[REV05-U04]	Exact quantification of element-specific dust depletion in the gas-phase ISM.	Elements like Fe, Si, C, and O deplete onto dust grains at different, poorly understood rates. Gas-phase measurements severely underestimate the total elemental abundances without highly accurate, environment-specific corrections.	Wide spectral coverage observations measuring both volatile and highly refractory elements simultaneously along the same intergalactic sightlines.	[REV05-P007], [REV05-P043]
[REV05-U05]	The physical validity of positive (inverted) metallicity gradients at cosmic noon.	If true inversions exist, they imply massive, rapid accretion of pristine gas directly into galactic cores, fundamentally challenging the established "inside-out" paradigm of disk growth.	Ultra-high spatial resolution IFU observations utilizing next-generation adaptive optics at z∼2 to conclusively break beam-smearing degeneracies.	[REV05-P006], [REV05-P036]
[REV05-U06]	The true location of the "missing" 30%−40% of cosmic metals.	Validates the energetics of cosmological feedback models. If metals exist in the hot IGM, feedback is highly explosive; if they do not exist, stellar nucleosynthesis yields require drastic, fundamental recalibration.	Deep X-ray spectroscopy and advanced far-UV absorption line studies capable of probing the ultra-diffuse, highly ionized WHIM.	[REV05-P007], [REV05-P009]
Primary-Citation Harvest
ID	Publication	Role	Review Locator	One-Line Boundary
[REV05-P001]	

Tremonti, C. A., et al. (2004, ApJ)




title=The Origin of the Mass-Metallicity Relation: Insights from 53,000 Star-Forming Galaxies in the Sloan Digital Sky Survey




DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T

	measurement	MZR	Bounded to SDSS local fiber gas-phase metallicities.
[REV05-P002]	

Pettini, M., & Pagel, M. E. (2004, MNRAS)




title=Nebular abundances in cosmologically distant galaxies




DOI:10.1111/j.1365-2966.2004.07598.x; arXiv:astro-ph/0401195; ADS:2004MNRAS.348L..59P

	calibration	strong-line methods	Bounded to O3N2 and N2 index empirical calibration scale.
[REV05-P003]	

Mannucci, F., et al. (2010, MNRAS)




title=A fundamental relation between mass, star formation rate and metallicity in local and high-redshift galaxies




DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1003.0010; ADS:2010MNRAS.408.2115M

	measurement	FMR	Bounded to establishing the 3D M-Z-SFR manifold.
[REV05-P004]	

Curti, M., et al. (2017, MNRAS)




title=New fully empirical calibrations of strong-line metallicity indicators in star-forming galaxies




DOI:10.1093/mnras/stw2766; arXiv:1610.06939; ADS:2017MNRAS.465.1384C

	calibration	strong-line methods	Bounded to Te-based empirical calibrations via stacked SDSS spectra.
[REV05-P005]	

Bothwell, M. S., et al. (2013, MNRAS)




title=A fundamental relation between the metallicity, gas content and stellar mass of local galaxies




DOI:10.1093/mnras/stt817; arXiv:1304.4940; ADS:2013MNRAS.433.1425B

	measurement	gas fractions	Bounded to HI gas mass dependence driving the FMR.
[REV05-P006]	

Cresci, G., et al. (2010, Nature)




title=Gas accretion as the origin of chemical abundance gradients in distant galaxies




DOI:10.1038/nature09457; arXiv:1010.2534; ADS:2010Natur.467..811C

	measurement	spatially resolved gradients	Bounded to inverted gradients indicating cold gas accretion at z~3.
[REV05-P007]	

Peeples, M. S., et al. (2014, ApJ)




title=A Budget and Accounting of Metals at z ~ 0: Results from the COS-Halos Survey




DOI:10.1088/0004-637X/786/1/54; arXiv:1310.2253; ADS:2014ApJ...786...54P

	measurement	metal budgets	Bounded to accounting limits of retained vs. expelled galactic metals.
[REV05-P008]	

Zahid, H. J., et al. (2014, ApJ)




title=The Universal Relation between Stellar Mass and Gas-Phase Metallicity in Star-Forming Galaxies




DOI:10.1088/0004-637X/791/2/130; arXiv:1404.4862; ADS:2014ApJ...791..130Z

	analytic_theory	chemical-evolution models	Bounded to modeling MZR saturation.
[REV05-P009]	

Werk, J. K., et al. (2014, ApJ)




title=The COS-Halos Survey: Physical Conditions and Baryonic Mass in the Circumgalactic Medium of L* Galaxies




DOI:10.1088/0004-637X/792/1/8; arXiv:1403.0946; ADS:2014ApJ...792....8W

	measurement	CGM tracers	Bounded to multiphase ionization modeling of the CGM.
[REV05-P010]	

Tumlinson, J., et al. (2011, Science)




title=The Luminous Circumgalactic Medium of Star-Forming Galaxies




DOI:10.1126/science.1209840; arXiv:1111.3651; ADS:2011Sci...334..948T

	measurement	CGM tracers	Bounded to OVI detection tracing massive metal reservoirs in the halos.
[REV05-P011]	

Lilly, S. J., et al. (2013, ApJ)




title=Gas Regulation in Galaxies. I. The Evolution of Galaxies and Their Interstellar Medium




DOI:10.1088/0004-637X/772/2/119; arXiv:1302.2610; ADS:2013ApJ...772..119L

	analytic_theory	chemical-evolution models	Bounded to formulating the gas-regulator/bathtub model.
[REV05-P012]	

Bouché, N., et al. (2010, ApJ)




title=The 'Bath-Tub' Model of Galaxy Evolution: Characterizing Inflow and Outflow Rates




DOI:10.1088/0004-637X/718/2/1001; arXiv:0912.1858; ADS:2010ApJ...718.1001B

	analytic_theory	chemical-evolution models	Bounded to the interplay of inflows and SFR in setting abundances.
[REV05-P013]	

Davé, R., et al. (2012, MNRAS)




title=The gas, coal and metal cycles of galaxies in a cosmological context




DOI:10.1111/j.1365-2966.2011.20148.x; arXiv:1108.0407; ADS:2012MNRAS.421...98D

	hydrodynamic_simulation	cosmological simulations	Bounded to simulating the baryon cycle and metal ejection mechanisms.
[REV05-P014]	

Andrews, B. H., & Martini, P. (2013, ApJ)




title=The Mass-Metallicity Relation with the Direct Method




DOI:10.1088/0004-637X/765/2/140; arXiv:1301.3141; ADS:2013ApJ...765..140A

	measurement	MZR	Bounded to establishing the MZR using stacked Te measurements.
[REV05-P015]	

Kewley, L. J., & Ellison, S. L. (2008, ApJ)




title=The Metallicity Calibration Dependence of the Mass-Metallicity Relation




DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K

	calibration	calibration offsets	Bounded to systematic transformations between discrepant absolute scales.
[REV05-P016]	

Zaritsky, D., et al. (1994, ApJ)




title=H II regions and the abundance properties of spiral galaxies




DOI:10.1086/173546; arXiv:none; ADS:1994ApJ...420...87Z

	measurement	spatially resolved gradients	Bounded to pioneering characterizations of radial abundance gradients.
[REV05-P017]	

Vila-Costas, M. A., & Edmunds, M. G. (1992, MNRAS)




title=The chemical evolution of spiral galaxies




DOI:10.1093/mnras/259.1.121; arXiv:none; ADS:1992MNRAS.259..121V

	measurement	chemical-evolution models	Bounded to classical chemical yield and local disk evolution limits.
[REV05-P018]	

Sánchez, S. F., et al. (2014, A&A)




title=A characteristic oxygen abundance gradient in galaxy disks unveiled with CALIFA




DOI:10.1051/0004-6361/201322343; arXiv:1311.7244; ADS:2014A&A...563A..49S

	measurement	spatially resolved gradients	Bounded to defining a universal gradient slope normalized by Re.
[REV05-P019]	

Belfiore, F., et al. (2017, MNRAS)




title=SDSS IV MaNGA: spatially resolved gas-phase metallicity gradients




DOI:10.1093/mnras/stx789; arXiv:1703.03808; ADS:2017MNRAS.469..151B

	measurement	spatially resolved gradients	Bounded to mapping local gradients across large mass samples.
[REV05-P020]	

Henry, R. B. C., et al. (2000, ApJ)




title=On the Synthesis of Nitrogen in Galaxies




DOI:10.1086/309447; arXiv:astro-ph/0004386; ADS:2000ApJ...541..660H

	analytic_theory	relative abundances	Bounded to models of primary vs secondary nitrogen production.
[REV05-P021]	

Izotov, Y. I., & Thuan, T. X. (1999, ApJ)




title=Heavy-Element Abundances in Helium-rich Blue Compact Dwarf Galaxies




DOI:10.1086/306706; arXiv:none; ADS:1999ApJ...511..639I

	measurement	relative abundances	Bounded to N/O and C/O measurements in extreme low-metallicity environments.
[REV05-P022]	

Garnett, D. R., et al. (1995, ApJ)




title=Carbon and nitrogen abundances in low-metallicity dwarf galaxies




DOI:10.1086/175504; arXiv:none; ADS:1995ApJ...443...64G

	measurement	relative abundances	Bounded to establishing the primary nitrogen floor.
[REV05-P023]	

Thomas, D., et al. (2005, ApJ)




title=The Epochs of Early-Type Galaxy Formation as a Function of Environment




DOI:10.1086/426932; arXiv:astro-ph/0410143; ADS:2005ApJ...621..673T

	measurement	stellar metallicities	Bounded to alpha/Fe ratios charting rapid star formation in early-type galaxies.
[REV05-P024]	

Steidel, C. C., et al. (2014, ApJ)




title=Strong Nebular Emission-Line Calibrations for High-Redshift Galaxies




DOI:10.1088/0004-637X/795/2/165; arXiv:1405.5473; ADS:2014ApJ...795..165S

	measurement	high-redshift limitations	Bounded to the BPT diagnostic shift at z~2.
[REV05-P025]	

Steidel, C. C., et al. (2016, ApJ)




title=Reconciling the Physical Properties of Active Star-forming Galaxies at z ~ 2




DOI:10.3847/0004-637X/826/2/159; arXiv:1605.07186; ADS:2016ApJ...826..159S

	measurement	high-redshift limitations	Bounded to stellar binary impact on ionizing spectra at high redshift.
[REV05-P026]	

Strom, A. L., et al. (2017, ApJ)




title=The Nebular Spectra of z ~ 2 Star-forming Galaxies




DOI:10.3847/1538-4357/836/2/164; arXiv:1702.01158; ADS:2017ApJ...836..164S

	measurement	high-redshift limitations	Bounded to mass-metallicity scaling in the KBSS z~2 survey.
[REV05-P027]	

Erb, D. K., et al. (2006, ApJ)




title=The Ultraviolet-bright, Star-forming Population at z ~ 2: II. Physical Properties




DOI:10.1086/503612; arXiv:astro-ph/0602422; ADS:2006ApJ...644..813E

	measurement	redshift evolution	Bounded to pioneer measurements of the MZR at cosmic noon.
[REV05-P028]	

Maiolino, R., et al. (2008, A&A)




title=AMAZE. I. The mass-metallicity relation at z ~ 3.3




DOI:10.1051/0004-6361:200809655; arXiv:0806.2410; ADS:2008A&A...488..463M

	measurement	redshift evolution	Bounded to downward normalization of the MZR at z>3.
[REV05-P029]	

Troncoso, P., et al. (2014, A&A)




title=Metallicity evolution, metal retention, and gas fractions in z ~ 3.4 galaxies




DOI:10.1051/0004-6361/201322081; arXiv:1401.7616; ADS:2014A&A...563A..58T

	measurement	redshift evolution	Bounded to AMAZE gas fraction limits and metal retention limits.
[REV05-P030]	

Marino, R. A., et al. (2013, A&A)




title=The O3N2 and N2 abundance indicators recalibrated with CALIFA




DOI:10.1051/0004-6361/201321956; arXiv:1309.5283; ADS:2013A&A...559A.114M

	calibration	strong-line methods	Bounded to establishing updated linear index calibrations based on Te.
[REV05-P031]	

Pilyugin, L. S., & Grebel, E. K. (2016, MNRAS)




title=New calibrations for estimating oxygen and nitrogen abundances




DOI:10.1093/mnras/stw238; arXiv:1601.03756; ADS:2016MNRAS.457.3678P

	calibration	strong-line methods	Bounded to S-method application utilizing N/O diagnostics.
[REV05-P032]	

Edmunds, M. G. (1990, MNRAS)




title=The chemical yield of a galaxy




DOI:none; arXiv:none; ADS:1990MNRAS.246..678E

	analytic_theory	metal budgets	Bounded to defining effective yield dependencies and mass-loss mechanisms.
[REV05-P033]	

Peeples, M. S., & Shankar, F. (2011, MNRAS)




title=Constraints on the gas-phase and stellar mass-metallicity relations




DOI:10.1111/j.1365-2966.2011.19455.x; arXiv:1007.3259; ADS:2011MNRAS.417.2962P

	analytic_theory	metal budgets	Bounded to connecting stellar fractions to gas-phase constraints.
[REV05-P034]	

Ho, I-Ting, et al. (2015, MNRAS)




title=Spatially resolved metallicity profiles in interacting galaxies




DOI:10.1093/mnras/stv114; arXiv:1501.04987; ADS:2015MNRAS.448.2030H

	measurement	environmental effects	Bounded to measuring gradient flattening due to tidal inflow.
[REV05-P035]	

Kewley, L. J., et al. (2010, ApJ)




title=The effect of mergers on metallicity gradients in galaxies




DOI:10.1088/2041-8205/721/1/L48; arXiv:1008.2214; ADS:2010ApJ...721L..48K

	measurement	environmental effects	Bounded to central metallicity dilution in local interacting pairs.
[REV05-P036]	

Jones, T., et al. (2013, ApJ)




title=The evolution of metallicity gradients in lensed star-forming galaxies at z ~ 1.5-2.5




DOI:10.1088/0004-637X/765/1/48; arXiv:1205.1804; ADS:2013ApJ...765...48J

	measurement	spatially resolved gradients	Bounded to identifying flat and inverted gradients via lensing.
[REV05-P037]	

Tinsley, B. M. (1980, Fund. Cosmic Phys.)




title=Evolution of the Stars and Gas in Galaxies




DOI:none; arXiv:none; ADS:1980FCPh....5..287T

	analytic_theory	chemical-evolution models	Bounded to foundational principles of chemical bookkeeping and delays.
[REV05-P038]	

Pagel, M. E., et al. (1979, MNRAS)




title=On the composition of H II regions in the outer parts of CG 1152-311 and other galaxies




DOI:10.1093/mnras/189.1.95; arXiv:none; ADS:1979MNRAS.189...95P

	calibration	strong-line methods	Bounded to originating the R23 oxygen abundance parameterization.
[REV05-P039]	

McGaugh, S. S. (1991, ApJ)




title=H II regions and the abundance properties of spiral galaxies




DOI:10.1086/170569; arXiv:none; ADS:1991ApJ...380..140M

	calibration	strong-line methods	Bounded to theoretical photoionization R23 modeling.
[REV05-P040]	

Lequeux, J., et al. (1979, A&A)




title=Chemical composition of H II regions in dwarf galaxies




DOI:none; arXiv:none; ADS:1979A&A....80..155L

	measurement	luminosity-metallicity relations	Bounded to originating observations tying mass/luminosity to metal abundance.
[REV05-P041]	

Lara-López, M. A., et al. (2010, A&A)




title=The fundamental plane of spiral galaxies: mass, metallicity and star formation rate




DOI:10.1051/0004-6361/201015645; arXiv:1008.3193; ADS:2010A&A...521L..53L

	measurement	FMR	Bounded to codifying the FMR manifold as a principal component plane.
[REV05-P042]	

Salim, S., et al. (2014, ApJ)




title=The relation between stellar mass, star formation rate, and gas-phase metallicity




DOI:10.1088/0004-637X/797/2/126; arXiv:1410.5434; ADS:2014ApJ...797..126S

	measurement	FMR	Bounded to SFR dependency limits on global SDSS scales.
[REV05-P043]	

Asplund, M., et al. (2009, ARA&A)




title=The Chemical Composition of the Sun




DOI:10.1146/annurev.astro.46.060407.145222; arXiv:0909.0948; ADS:2009ARA&A..47..481A

	calibration	abundance-scale systematics	Bounded to anchoring the absolute solar zero point reference.
[REV05-P044]	

Izotov, Y. I., et al. (2006, A&A)




title=Systematic effects in the determination of the primordial helium abundance




DOI:10.1051/0004-6361:20053763; arXiv:astro-ph/0602334; ADS:2006A&A...448..955I

	measurement	direct electron-temperature methods	Bounded to assessing Te structural uncertainties.
[REV05-P045]	

Bresolin, F., et al. (2009, ApJ)




title=Gas-phase abundances in the giant spiral galaxy NGC 300




DOI:10.1088/0004-637X/700/1/309; arXiv:0905.0934; ADS:2009ApJ...700..309B

	measurement	spatially resolved gradients	Bounded to resolving Te-based gradient slopes in a nearby analog.
[REV05-P046]	

Kennicutt, R. C. (1998, ARA&A)




title=Star Formation in Galaxies Along the Hubble Sequence




DOI:10.1146/annurev.astro.36.1.189; arXiv:astro-ph/9807187; ADS:1998ARA&A..36..189K

	analytic_theory	chemical-evolution models	Bounded to empirical relationships dictating star formation efficiencies.
[REV05-P047]	

Bigiel, F., et al. (2008, AJ)




title=The Star Formation Law in Nearby Galaxies on Sub-Kpc Scales




DOI:10.1088/0004-6256/136/6/2846; arXiv:0810.1741; ADS:2008AJ....136.2846B

	measurement	spatially resolved gradients	Bounded to spatially resolved SFR-gas conversions driving local enrichment.
[REV05-P048]	

Davé, R., Finlator, K., & Oppenheimer, B. D. (2011, MNRAS)




title=Galaxy evolution in a cosmological context




DOI:10.1111/j.1365-2966.2011.19132.x; arXiv:1104.3156; ADS:2011MNRAS.416.1354D

	hydrodynamic_simulation	cosmological simulations	Bounded to wind-recycling impact on scaling relations.
[REV05-P049]	

Carton, D., et al. (2018, MNRAS)




title=Gas-phase metallicity gradients of star-forming galaxies




DOI:10.1093/mnras/sty1293; arXiv:1805.07340; ADS:2018MNRAS.478.4293C

	measurement	spatially resolved gradients	Bounded to MUSE/MUSE-Wide gradient studies.
[REV05-P050]	

Torrey, P., et al. (2018, MNRAS)




title=Similar star formation rate and metallicity variability time-scales drive the fundamental metallicity relation




DOI:10.1093/mnrasl/sly031; arXiv:1711.05261; ADS:2018MNRAS.477L..16T

	hydrodynamic_simulation	cosmological simulations	Bounded to linking FMR scatter to cyclical SFR-metallicity oscillation timescales.
[REV05-P051]	

Garnett, D. R. (2002, ApJ)




title=The Luminosity-Metallicity Relation, Effective Yields, and Metal Loss in Spiral and Irregular Galaxies




DOI:10.1086/344317; arXiv:astro-ph/0209012; ADS:2002ApJ...581.1019G

	analytic_theory	metal budgets	Bounded to effective yields and mass-dependent metal loss limits.
DO_NOT_USE_UNVERIFIED
Format	Candidate or Claim	Supplied Identifier / Context	Exclusion Reason
UNCITED_NOT_USABLE	Post-2019 JWST high-z MZR/FMR evolution discoveries	Curti et al. 2023/2024, Nakajima et al. 2023, Tripodi 2025, Stanton 2025	Violates the pre-2019 temporal boundary constraint; inherently uncited by Maiolino & Mannucci 2019.
UNCITED_NOT_USABLE	All metallicity calibrations share one absolute scale	Broad claim	Explicitly contradicts the core review finding that empirical T
e
	​

 and photoionization scales are systematically offset by up to 0.5 dex.
UNCITED_NOT_USABLE	Gas and stellar metallicity are directly interchangeable	Broad claim	Falsely conflates distinct physical phase boundaries. Stellar metallicities trace past, time-integrated enrichment; gas-phase traces current ISM conditions.
UNCITED_NOT_USABLE	One spatially-resolved gradient measures all phases	Broad claim	Confounds gas-phase abundance gradients (typically negative, tracing inside-out growth) with stellar age/metallicity gradients.
UNCITED_NOT_USABLE	Matching the MZR validates one specific feedback model	Broad claim	Quarantined; the MZR is highly degenerate. Multiple competing feedback models can reproduce the MZR by tuning unconstrained sub-grid parameters.
UNCITED_NOT_USABLE	AGN Accretion rates and Demographics	Various AGN literature in search snippets	Quarantined due to boundary scope. The review includes AGN solely as a contaminant source limiting emission-line diagnostics.
Review and Source Identity Ledger
ID	Authors (Year, Journal)	DOI	arXiv	ADS	Role	Boundary
[REV05-R00]	Maiolino, R. & Mannucci, F. (2019, The Astronomy and Astrophysics Review)	10.1007/s00159-018-0112-2	1811.09642	2019A&ARv..27....3M	Core Review	Authorized boundary establishing pre-2019 galaxy chemical evolution.
[REV05-P001]	Tremonti, C. A., et al. (2004, ApJ)	10.1086/423264	astro-ph/0405537	2004ApJ...613..898T	measurement	SDSS local fiber gas-phase metallicities.
[REV05-P002]	Pettini, M., & Pagel, M. E. (2004, MNRAS)	10.1111/j.1365-2966.2004.07598.x	astro-ph/0401195	2004MNRAS.348L..59P	calibration	O3N2 and N2 index empirical calibration scale.
[REV05-P003]	Mannucci, F., et al. (2010, MNRAS)	10.1111/j.1365-2966.2010.17291.x	1003.0010	2010MNRAS.408.2115M	measurement	Establishing the 3D M-Z-SFR manifold.
[REV05-P004]	Curti, M., et al. (2017, MNRAS)	10.1093/mnras/stw2766	1610.06939	2017MNRAS.465.1384C	calibration	Te-based empirical calibrations via stacked SDSS spectra.
[REV05-P005]	Bothwell, M. S., et al. (2013, MNRAS)	10.1093/mnras/stt817	1304.4940	2013MNRAS.433.1425B	measurement	HI gas mass dependence driving the FMR.
[REV05-P006]	Cresci, G., et al. (2010, Nature)	10.1038/nature09457	1010.2534	2010Natur.467..811C	measurement	Inverted gradients indicating cold gas accretion at z~3.
[REV05-P007]	Peeples, M. S., et al. (2014, ApJ)	10.1088/0004-637X/786/1/54	1310.2253	2014ApJ...786...54P	measurement	Accounting limits of retained vs. expelled galactic metals.
[REV05-P008]	Zahid, H. J., et al. (2014, ApJ)	10.1088/0004-637X/791/2/130	1404.4862	2014ApJ...791..130Z	analytic_theory	Modeling MZR saturation.
[REV05-P009]	Werk, J. K., et al. (2014, ApJ)	10.1088/0004-637X/792/1/8	1403.0946	2014ApJ...792....8W	measurement	Multiphase ionization modeling of the CGM.
[REV05-P010]	Tumlinson, J., et al. (2011, Science)	10.1126/science.1209840	1111.3651	2011Sci...334..948T	measurement	OVI detection tracing massive metal reservoirs in the halos.
[REV05-P011]	Lilly, S. J., et al. (2013, ApJ)	10.1088/0004-637X/772/2/119	1302.2610	2013ApJ...772..119L	analytic_theory	Formulating the gas-regulator/bathtub model.
[REV05-P012]	Bouché, N., et al. (2010, ApJ)	10.1088/0004-637X/718/2/1001	0912.1858	2010ApJ...718.1001B	analytic_theory	Interplay of inflows and SFR in setting abundances.
[REV05-P013]	Davé, R., et al. (2012, MNRAS)	10.1111/j.1365-2966.2011.20148.x	1108.0407	2012MNRAS.421...98D	hydrodynamic_simulation	Simulating the baryon cycle and metal ejection mechanisms.
[REV05-P014]	Andrews, B. H., & Martini, P. (2013, ApJ)	10.1088/0004-637X/765/2/140	1301.3141	2013ApJ...765..140A	measurement	Establishing the MZR using stacked Te measurements.
[REV05-P015]	Kewley, L. J., & Ellison, S. L. (2008, ApJ)	10.1086/587500	0801.1849	2008ApJ...681.1183K	calibration	Systematic transformations between discrepant absolute scales.
[REV05-P016]	Zaritsky, D., et al. (1994, ApJ)	10.1086/173546	none	1994ApJ...420...87Z	measurement	Pioneering characterizations of radial abundance gradients.
[REV05-P017]	Vila-Costas, M. A., & Edmunds, M. G. (1992, MNRAS)	10.1093/mnras/259.1.121	none	1992MNRAS.259..121V	measurement	Classical chemical yield and local disk evolution limits.
[REV05-P018]	Sánchez, S. F., et al. (2014, A&A)	10.1051/0004-6361/201322343	1311.7244	2014A&A...563A..49S	measurement	Defining a universal gradient slope normalized by Re.
[REV05-P019]	Belfiore, F., et al. (2017, MNRAS)	10.1093/mnras/stx789	1703.03808	2017MNRAS.469..151B	measurement	Mapping local gradients across large mass samples.
[REV05-P020]	Henry, R. B. C., et al. (2000, ApJ)	10.1086/309447	astro-ph/0004386	2000ApJ...541..660H	analytic_theory	Models of primary vs secondary nitrogen production.
[REV05-P021]	Izotov, Y. I., & Thuan, T. X. (1999, ApJ)	10.1086/306706	none	1999ApJ...511..639I	measurement	N/O and C/O measurements in extreme low-metallicity environments.
[REV05-P022]	Garnett, D. R., et al. (1995, ApJ)	10.1086/175504	none	1995ApJ...443...64G	measurement	Establishing the primary nitrogen floor.
[REV05-P023]	Thomas, D., et al. (2005, ApJ)	10.1086/426932	astro-ph/0410143	2005ApJ...621..673T	measurement	Alpha/Fe ratios charting rapid star formation in early-type galaxies.
[REV05-P024]	Steidel, C. C., et al. (2014, ApJ)	10.1088/0004-637X/795/2/165	1405.5473	2014ApJ...795..165S	measurement	The BPT diagnostic shift at z~2.
[REV05-P025]	Steidel, C. C., et al. (2016, ApJ)	10.3847/0004-637X/826/2/159	1605.07186	2016ApJ...826..159S	measurement	Stellar binary impact on ionizing spectra at high redshift.
[REV05-P026]	Strom, A. L., et al. (2017, ApJ)	10.3847/1538-4357/836/2/164	1702.01158	2017ApJ...836..164S	measurement	Mass-metallicity scaling in the KBSS z~2 survey.
[REV05-P027]	Erb, D. K., et al. (2006, ApJ)	10.1086/503612	astro-ph/0602422	2006ApJ...644..813E	measurement	Pioneer measurements of the MZR at cosmic noon.
[REV05-P028]	Maiolino, R., et al. (2008, A&A)	10.1051/0004-6361:200809655	0806.2410	2008A&A...488..463M	measurement	Downward normalization of the MZR at z>3.
[REV05-P029]	Troncoso, P., et al. (2014, A&A)	10.1051/0004-6361/201322081	1401.7616	2014A&A...563A..58T	measurement	AMAZE gas fraction limits and metal retention limits.
[REV05-P030]	Marino, R. A., et al. (2013, A&A)	10.1051/0004-6361/201321956	1309.5283	2013A&A...559A.114M	calibration	Establishing updated linear index calibrations based on Te.
[REV05-P031]	Pilyugin, L. S., & Grebel, E. K. (2016, MNRAS)	10.1093/mnras/stw238	1601.03756	2016MNRAS.457.3678P	calibration	S-method application utilizing N/O diagnostics.
[REV05-P032]	Edmunds, M. G. (1990, MNRAS)	none	none	1990MNRAS.246..678E	analytic_theory	Defining effective yield dependencies and mass-loss mechanisms.
[REV05-P033]	Peeples, M. S., & Shankar, F. (2011, MNRAS)	10.1111/j.1365-2966.2011.19455.x	1007.3259	2011MNRAS.417.2962P	analytic_theory	Connecting stellar fractions to gas-phase constraints.
[REV05-P034]	Ho, I-Ting, et al. (2015, MNRAS)	10.1093/mnras/stv114	1501.04987	2015MNRAS.448.2030H	measurement	Measuring gradient flattening due to tidal inflow.
[REV05-P035]	Kewley, L. J., et al. (2010, ApJ)	10.1088/2041-8205/721/1/L48	1008.2214	2010ApJ...721L..48K	measurement	Central metallicity dilution in local interacting pairs.
[REV05-P036]	Jones, T., et al. (2013, ApJ)	10.1088/0004-637X/765/1/48	1205.1804	2013ApJ...765...48J	measurement	Identifying flat and inverted gradients via lensing.
[REV05-P037]	Tinsley, B. M. (1980, Fund. Cosmic Phys.)	none	none	1980FCPh....5..287T	analytic_theory	Foundational principles of chemical bookkeeping and delays.
[REV05-P038]	Pagel, M. E., et al. (1979, MNRAS)	10.1093/mnras/189.1.95	none	1979MNRAS.189...95P	calibration	Originating the R23 oxygen abundance parameterization.
[REV05-P039]	McGaugh, S. S. (1991, ApJ)	10.1086/170569	none	1991ApJ...380..140M	calibration	Theoretical photoionization R23 modeling.
[REV05-P040]	Lequeux, J., et al. (1979, A&A)	none	none	1979A&A....80..155L	measurement	Originating observations tying mass/luminosity to metal abundance.
[REV05-P041]	Lara-López, M. A., et al. (2010, A&A)	10.1051/0004-6361/201015645	1008.3193	2010A&A...521L..53L	measurement	Codifying the FMR manifold as a principal component plane.
[REV05-P042]	Salim, S., et al. (2014, ApJ)	10.1088/0004-637X/797/2/126	1410.5434	2014ApJ...797..126S	measurement	SFR dependency limits on global SDSS scales.
[REV05-P043]	Asplund, M., et al. (2009, ARA&A)	10.1146/annurev.astro.46.060407.145222	0909.0948	2009ARA&A..47..481A	calibration	Anchoring the absolute solar zero point reference.
[REV05-P044]	Izotov, Y. I., et al. (2006, A&A)	10.1051/0004-6361:20053763	astro-ph/0602334	2006A&A...448..955I	measurement	Assessing Te structural uncertainties.
[REV05-P045]	Bresolin, F., et al. (2009, ApJ)	10.1088/0004-637X/700/1/309	0905.0934	2009ApJ...700..309B	measurement	Resolving Te-based gradient slopes in a nearby analog.
[REV05-P046]	Kennicutt, R. C. (1998, ARA&A)	10.1146/annurev.astro.36.1.189	astro-ph/9807187	1998ARA&A..36..189K	analytic_theory	Empirical relationships dictating star formation efficiencies.
[REV05-P047]	Bigiel, F., et al. (2008, AJ)	10.1088/0004-6256/136/6/2846	0810.1741	2008AJ....136.2846B	measurement	Spatially resolved SFR-gas conversions driving local enrichment.
[REV05-P048]	Davé, R., Finlator, K., & Oppenheimer, B. D. (2011, MNRAS)	10.1111/j.1365-2966.2011.19132.x	1104.3156	2011MNRAS.416.1354D	hydrodynamic_simulation	Wind-recycling impact on scaling relations.
[REV05-P049]	Carton, D., et al. (2018, MNRAS)	10.1093/mnras/sty1293	1805.07340	2018MNRAS.478.4293C	measurement	MUSE/MUSE-Wide gradient studies.
[REV05-P050]	Torrey, P., et al. (2018, MNRAS)	10.1093/mnrasl/sly031	1711.05261	2018MNRAS.477L..16T	hydrodynamic_simulation	Linking FMR scatter to cyclical SFR-metallicity oscillation timescales.
[REV05-P051]	Garnett, D. R. (2002, ApJ)	10.1086/344317	astro-ph/0209012	2002ApJ...581.1019G	analytic_theory	Effective yields and mass-dependent metal loss limits.

REVIEW_BASE_05_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- arxiv.org Filippo Mannucci's articles on arXiv Opens in a new window — https://arxiv.org/a/mannucci_f_1
- researchgate.net De re metallica: the cosmic chemical evolution of galaxies - ResearchGate Opens in a new window — https://www.researchgate.net/publication/330865983_De_re_metallica_the_cosmic_chemical_evolution_of_galaxies
- arxiv.org [1811.09642] De Re Metallica: The cosmic chemical evolution of galaxies - arXiv Opens in a new window — https://arxiv.org/abs/1811.09642
- repository.cam.ac.uk De re metallica: the cosmic chemical evolution of galaxies - Apollo Opens in a new window — https://www.repository.cam.ac.uk/items/daa69fc7-45ae-4e01-b4a9-960a4e6be5d6
- academic.oup.com Metallicity calibrations for diffuse ionized gas and low-ionization emission regions | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/485/1/367/5307101
- arcetri.inaf.it Dr. Filippo Mannucci - Astrophysicist - Inaf Arcetri Opens in a new window — https://www.arcetri.inaf.it/filippo.mannucci/
- academic.oup.com A fundamental relation between mass, star formation rate and metallicity in local and high-redshift galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/408/4/2115/1418549
- academic.oup.com fundamental relation between the metallicity, gas content and stellar mass of local galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/433/2/1425/1749733
- osti.gov A budget and accounting of metals at z ∼ 0: Results from the COS-Halos survey - OSTI Opens in a new window — https://www.osti.gov/biblio/22356987
- eprints.soton.ac.uk arXiv:2502.12764v1 [astro-ph.GA] 18 Feb 2025 - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/502442/1/2502.12764v1.pdf
- arxiv.org Metal Mayhem at z∼7⁢"–"⁢10: Diversity and Evolution of Gas-Phase Metallicity Gradients Opens in a new window — https://arxiv.org/html/2604.07076
- academic.oup.com The EDGE–CALIFA survey: the local and global relations between ∗ , SFR, and mol that regulate star formation Opens in a new window — https://academic.oup.com/mnras/article-pdf/503/2/1615/36653719/stab442.pdf
- academic.oup.com New fully empirical calibrations of strong-line metallicity indicators in star-forming galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/465/2/1384/8302523/stw2766.pdf
- researchgate.net AGN Feedback: The impact of galactic-scale radio jets on the interstellar medium in starbursting obscured AGN - ResearchGate Opens in a new window — https://www.researchgate.net/publication/408300804_AGN_Feedback_The_impact_of_galactic-scale_radio_jets_on_the_interstellar_medium_in_starbursting_obscured_AGN
- academic.oup.com The origin of the galaxy mass–metallicity relation and implications for galactic outflows - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/385/4/2181/1035724
- arxiv.org arXiv:astro-ph/0405537v1 27 May 2004 Opens in a new window — https://arxiv.org/pdf/astro-ph/0405537
- pta.edu.pl The fundamental metallicity relation from ζ ∼ 0 to ζ ∼ 0.7: Selection or Evolution? Opens in a new window — https://www.pta.edu.pl/pliki/proc/vol12/v12p32.pdf
- academic.oup.com physics of the fundamental metallicity relation | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/430/4/2891/1101320
- arxiv.org A fundamental relation between the metallicity, gas content, and stellar mass of local galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/1304.4940
- mdpi.com The Metal Content of the Hot Atmospheres of Galaxy Groups - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/7/7/208
- arxiv.org Metal Mayhem at z∼7⁢"–"⁢10: Diversity and Evolution of Gas-Phase Metallicity Gradients Opens in a new window — https://arxiv.org/html/2604.07076v1
- researchgate.net Metallicity of the BLR as a function of black hole mass for quasars... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Metallicity-of-the-BLR-as-a-function-of-black-hole-mass-for-quasars-divided-into-bins-of_fig57_330865983
- ned.ipac.caltech.edu Gas Accretion and Star Formation Rates - Jorge Sánchez Almeida Opens in a new window — https://ned.ipac.caltech.edu/level5/March17/Sanchez/Sanchez2.html
- cambridge.org SPICA and the Chemical Evolution of Galaxies: The Rise of Metals and Dust | Publications of the Astronomical Society of Australia | Cambridge Core Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/spica-and-the-chemical-evolution-of-galaxies-the-rise-of-metals-and-dust/770FF4093D510A7F5967570627D00010
- academic.oup.com On the origin of the mass–metallicity gradient relation in the local Universe Opens in a new window — https://academic.oup.com/mnras/article/504/1/53/6189699
- arxiv.org Direct Tₑ-based Metallicities of z=2-9 Galaxies with JWST/NIRSpec: Empirical Metallicity Calibrations Applicable from Reionization to Cosmic Noon - arXiv Opens in a new window — https://arxiv.org/html/2303.08149v2
- researchgate.net The mass–metallicity and the fundamental metallicity relation revisited on a fully Te-based abundance scale for galaxies | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/344678992_The_mass-metallicity_and_the_fundamental_metallicity_relation_revisited_on_a_fully_Te-based_abundance_scale_for_galaxies
- arxiv.org arXiv:1310.2253v2 [astro-ph.CO] 3 Mar 2014 Opens in a new window — https://arxiv.org/pdf/1310.2253
- arxiv.org arXiv:1406.0509v3 [astro-ph.GA] 20 Nov 2014 Opens in a new window — https://arxiv.org/pdf/1406.0509
- researchgate.net Lookback Time and Redshift | Download Table - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Lookback-Time-and-Redshift_tbl2_230928519
- ouci.dntb.gov.ua Temperature inhomogeneities cause the abundance discrepancy in H ii regions - OUCI Opens in a new window — https://ouci.dntb.gov.ua/en/works/4On1noW7/
- arxiv.org Temperature inhomogeneities cause the abundance discrepancy in H II regions - arXiv Opens in a new window — https://arxiv.org/pdf/2305.11578
- academic.oup.com A fundamental relation between the metallicity, gas content and stellar mass of local galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/433/2/1425/4921809/stt817.pdf
- par.nsf.gov Does the fundamental metallicity relation evolve with redshift? I - NSF Public Access Repository Opens in a new window — https://par.nsf.gov/servlets/purl/10538536
- explore.openaire.eu ENVIRONMENTAL EFFECTS ON THE METAL ENRICHMENT OF LOW-MASS GALAXIES IN NEARBY CLUSTERS - OpenAIRE - Explore Opens in a new window — https://explore.openaire.eu/search/publication?pid=10261/415223
- researchgate.net Summary of the atomic data used in the present analysis. | Download Table - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Summary-of-the-atomic-data-used-in-the-present-analysis_tbl2_44097427
- arxiv.org 3D Non-LTE radiation transfer: theory and applications to stars, exoplanets, and kilonovae Opens in a new window — https://arxiv.org/html/2511.04254v1
- arxiv.org V/𝜎 Trends with Mass for Dwarf Galaxies from the Marvelous Massive Dwarfs Suite - arXiv Opens in a new window — https://arxiv.org/html/2605.06893v1
- arxiv.org Stellar Streams in the Gaia Era - arXiv Opens in a new window — https://arxiv.org/html/2405.19410v1
- arxiv.org Infrared fine-structure lines at high redshift - arXiv Opens in a new window — https://arxiv.org/html/2509.19444v1
- arxiv.org FASTAR - I. Continuous and differentiable evolutionary stellar population models - arXiv Opens in a new window — https://arxiv.org/html/2605.24093v1
- arxiv.org Impact of stellar population models on the estimated physical properties of galaxies - arXiv Opens in a new window — https://arxiv.org/html/2605.15096v2
- researchgate.net [O ii], [O iii]λ5007 and Hα lines as observed by the XShooter for GRB... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/O-ii-O-iiil5007-and-Ha-lines-as-observed-by-the-XShooter-for-GRB-000210-host-Both_fig1_279458945
- scilit.com MUSEQuBES: Physical conditions, origins, and multi-element abundances of the circumgalactic medium of an isolated, star-forming dwarf galaxy at z=0.57 | Scilit Opens in a new window — https://www.scilit.com/publications/a49e30a464279dc6f201a7deedfe1be2
- researchgate.net (PDF) Space Project for Astrophysical and Cosmological Exploration (SPACE), an ESA stand-alone mission and a possible contribution to the Origins Space Telescope - ResearchGate Opens in a new window — https://www.researchgate.net/publication/353327881_Space_Project_for_Astrophysical_and_Cosmological_Exploration_SPACE_an_ESA_stand-alone_mission_and_a_possible_contribution_to_the_Origins_Space_Telescope
- explore.openaire.eu Origin of the Chemical Elements - OpenAIRE - Explore Opens in a new window — https://explore.openaire.eu/search/result?pid=10.1007/978-1-4419-0720-2_12
- sissa.it Binary neutron stars and binary black holes: from the Milky Way to the high-redshift Universe - SISSA Opens in a new window — https://www.sissa.it/ap/phdsection/AlumniThesis/Cecilia%20Sgalletta.pdf
- arxiv.org A SHARP Look at Quenching and Bulge-Disk Growth in Massive Galaxies at Cosmic Noon - arXiv Opens in a new window — https://arxiv.org/pdf/2606.30763
- cris.unibo.it JCAP03(2026)081 Opens in a new window — https://cris.unibo.it/retrieve/handle/11585/1061071/d34fce87-ba7d-411a-89da-2a6a60c21392/jcap_2026_03_081-603-803.pdf
- arxiv.org The Effects of Reduced Metallicity on X-ray AGN Obscuration at High Redshift - arXiv Opens in a new window — https://arxiv.org/html/2606.25018v1
- arxiv.org pop-cosmos: Disentangling galaxy properties from observables using data-driven approaches - arXiv Opens in a new window — https://arxiv.org/html/2606.11308v2
- semanticscholar.org [PDF] Origin of the Chemical Elements | Semantic Scholar Opens in a new window — https://www.semanticscholar.org/paper/Origin-of-the-Chemical-Elements-Rauscher-Patk%C3%B3s/2f8c5dfe916c3e592aeb67f2874fbc3877278f93
- osti.gov Investigating the origin of observed central dips in radial metallicity profiles - OSTI.GOV Opens in a new window — https://www.osti.gov/pages/biblio/1905921
- iag.usp.br The miniJPAS survey: Identification and characterization of the emission line galaxies down to z < 0.35 in the AEGIS field - IAG-USP Opens in a new window — https://www.iag.usp.br/sites/default/files/2023-05/arxiv_CM006_2204.01698.pdf
- sissa.it High-redshift Dusty Star-Forming Galaxies: a panchromatic approach to constrain massive - SISSA Opens in a new window — https://www.sissa.it/ap/phdsection/AlumniThesis/Lara%20Pantoni.pdf
- amsdottorato.unibo.it The merger-driven evolution of early-type galaxies and the connection with their dark matter halos - AMS Dottorato Opens in a new window — https://amsdottorato.unibo.it/id/eprint/9874/1/CarloCannarozzo_PhDThesis.pdf
- github.com phd-thesis-ferrone/test.tex at main · salvatore-ferrone/phd-thesis Opens in a new window — https://github.com/salvatore-ferrone/phd-thesis-ferrone/blob/main/test.tex
- semanticscholar.org [PDF] Element Abundances through the Cosmic Ages | Semantic Scholar Opens in a new window — https://www.semanticscholar.org/paper/Element-Abundances-through-the-Cosmic-Ages-Pettini/32b705c621987cd692fb53c8e6014f95f340579f
- arxiv.org Clues to inside-out quenching in quiescent galaxies at 1.2≲z≲2.2: Age, Fe-, and Mg-abundance gradients from JWST-SUSPENSE - arXiv Opens in a new window — https://arxiv.org/html/2509.12316v3
- arxiv.org An Ultra-Faint, Chemically Primitive Galaxy Forming in the Reionization Era - arXiv Opens in a new window — https://arxiv.org/html/2506.11846v2
- explore.openaire.eu Assessing model-based carbon and oxygen abundance derivation Opens in a new window — https://explore.openaire.eu/search/publication?pid=10.1093%2Fmnras%2Fstad621
- scispace.com From sub-solar to super-solar chemical abundances ... - SciSpace Opens in a new window — https://scispace.com/pdf/from-sub-solar-to-super-solar-chemical-abundances-along-the-1ka7k09i3d.pdf
- thesis.caltech.edu Multi-Element Abundances as Probes of Galaxy Growth Across Opens in a new window — https://thesis.caltech.edu/17609/03/Thesis_Zhuyun_Zhuang.pdf
- osti.gov The metallicity's fundamental dependence on both local and global Opens in a new window — https://www.osti.gov/pages/biblio/1906544
- pmc.ncbi.nlm.nih.gov A small and vigorous black hole in the early Universe - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC10917688/
- mdpi.com Semi-Empirical Estimates of the Cosmic Planet Formation Rate - MDPI Opens in a new window — https://www.mdpi.com/2075-4434/12/4/49
- scispace.com De re metallica. Translated from the first Latin ed. of 1556, with biographical introd., annotations, and appendices upon the de - SciSpace Opens in a new window — https://scispace.com/pdf/de-re-metallica-translated-from-the-first-latin-ed-of-1556-3oztb9sn37.pdf
- srk.com A Multidimensional Approach to Evaluating Failure Consequences | SRK Consulting Opens in a new window — https://www.srk.com/en/publications/multidimensional-approach-evaluate-failure-consequences-obonimulti-dimensional-consequences
- gutenberg.org The Project Gutenberg eBook of De Re Metallica, by Georgius Agricola. Opens in a new window — https://www.gutenberg.org/files/38015/38015-h/38015-h.htm
- scispace.com Georgius Agricola De re metallica, tr. from the 1st Latin ed. of 1556, with biographical introduction, annotations and appendice - SciSpace Opens in a new window — https://scispace.com/pdf/georgius-agricola-de-re-metallica-tr-from-the-1st-latin-ed-5nboqkcm65.pdf
- archive.org De re metallica Opens in a new window — https://archive.org/download/deremetallica50agri/deremetallica50agri.pdf
- scilit.com Metallicity Structure in Galactic Longitude–Velocity Diagrams of the Milky Way Disk and FIRE-2 Simulations | Scilit Opens in a new window — https://www.scilit.com/publications/d63e18aacf8f8c638286b763465d4c47
- spiedigitallibrary.org Black hole accretion, star formation, and chemical evolution with PRobe far-infrared mission for astrophysics/far-IR - SPIE Digital Library Opens in a new window — https://www.spiedigitallibrary.org/journals/Journal-of-Astronomical-Telescopes-Instruments-and-Systems/volume-11/issue-03/031637/Black-hole-accretion-star-formation-and-chemical-evolution-with-PRobe/10.1117/1.JATIS.11.3.031637.pdf
- arxiv.org High 12C/13C isotopic ratios toward G+0.693-0.027: evidence for gas inflow to the Central Molecular Zone - arXiv Opens in a new window — https://arxiv.org/html/2607.06541v2
- scilit.com A high fraction of close massive binary stars at low metallicity | Scilit Opens in a new window — https://www.scilit.com/publications/c1fbec44c3d451b5d16e1cd2d142d200
- researchgate.net (PDF) REBELS-IFU: Evidence for metal-rich massive galaxies at z~6-8 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/388232759_REBELS-IFU_Evidence_for_metal-rich_massive_galaxies_at_z6-8
- researchgate.net The fundamental metallicity relation. Left: dependence of the gas... | Download Scientific Diagram - ResearchGate Opens in a new window — https://www.researchgate.net/figure/The-fundamental-metallicity-relation-Left-dependence-of-the-gas-metallicity-on-mass-in_fig14_330865983
- arxiv.org Can current models predict the local black hole merger rate? - arXiv Opens in a new window — https://arxiv.org/html/2606.02725v1
- scholar.google.com ‪Filippo Mannucci‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=QMUsywwAAAAJ&hl=en
- research.amanote.com De Re Metallica: The Cosmic Chemical Evolution of Galaxies - Amanote Research Opens in a new window — https://research.amanote.com/publication/G67QAnQBKQvf0BhihSVS/de-re-metallica-the-cosmic-chemical-evolution-of-galaxies
- jglobal.jst.go.jp De re metallica: the cosmic chemical evolution of galaxies | Article Opens in a new window — https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=201902218158161024
- scispace.com (PDF) De Re Metallica: The cosmic chemical evolution of galaxies Opens in a new window — https://scispace.com/papers/de-re-metallica-the-cosmic-chemical-evolution-of-galaxies-35saefoif6?references_page=48
- cpt.univ-mrs.fr EC16 — Program Opens in a new window — https://www.cpt.univ-mrs.fr/~cosmo/EC2025/index.php?page=program
- arxiv.org An Ultra-Faint, Chemically Primitive Galaxy Forming at the Epoch of Reionization - arXiv Opens in a new window — https://arxiv.org/html/2506.11846v1
- sci-hub.box Evolutionary and Cosmological Corrections for High Redshift Galaxies - Sci-Hub Opens in a new window — https://sci-hub.box/10.1017/s0074180900132383
- academic.oup.com mass–metallicity and the fundamental metallicity relation revisited on a fully Te-based abundance scale for galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/491/1/944/5638748
- uhra.herts.ac.uk Optimal metallicity diagnostics for MUSE observations of low- galaxies - University of Hertfordshire Research Archive Opens in a new window — https://uhra.herts.ac.uk/id/eprint/10785/2/stad3464.pdf
- arxiv.org The AURORA Survey: High-Redshift Empirical Metallicity Calibrations from Electron Temperature Measurements at z = 2 - arXiv Opens in a new window — https://arxiv.org/html/2508.10099v1
- arxiv.org [1212.4848] The Fundamental Metallicity Relation Reduces Type Ia SN Hubble Residuals More Than Host Mass Alone - arXiv Opens in a new window — https://arxiv.org/abs/1212.4848
- semanticscholar.org A fundamental relation between mass, SFR and metallicity in local and high redshift galaxies - Semantic Scholar Opens in a new window — https://www.semanticscholar.org/paper/A-fundamental-relation-between-mass%2C-SFR-and-in-and-Mannucci-Cresci/09389471aa1b0261f8afd278c6073f7f6b2d92a5
- academic.oup.com Galaxy gas flows inferred from a detailed, spatially resolved metal budget - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/455/2/1218/1107983
- academic.oup.com The dust-to-gas and dust-to-metal ratio in galaxies from z = 0 to 6 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/490/1/1425/5583037
- ned.ipac.caltech.edu galaxies in gaseous halos - The Circumgalactic Medium - Jason Tumlinson et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Tumlinson/Tumlinson2.html
- researchgate.net Francisco Sánchez-Piñero's research while affiliated with University of Granada and other places - ResearchGate Opens in a new window — https://www.researchgate.net/scientific-contributions/Francisco-Sanchez-Pinero-29564672
- pubs.acs.org Application of Sanchez–Lacombe and Perturbed-Chain Statistical Associating Fluid Theory Equation of State Models in Catalytic Olefins (Co)polymerization Industrial Applications - ACS Publications Opens in a new window — https://pubs.acs.org/doi/10.1021/ie401056j
- research-portal.st-andrews.ac.uk A characteristic oxygen abundance gradient in galaxy disks Opens in a new window — https://research-portal.st-andrews.ac.uk/en/publications/a-characteristic-oxygen-abundance-gradient-in-galaxy-disks-unveil/
- fermi.gsfc.nasa.gov The Origin Of The Mass-Metallicity Relation For GRB Host Galaxies - Fermi Opens in a new window — https://fermi.gsfc.nasa.gov/science/mtgs/grb2010/thu/Daniel_Kocevski_Poster.pdf
- semanticscholar.org [PDF] The Origin of the Mass-Metallicity Relation: Insights from Opens in a new window — https://www.semanticscholar.org/paper/The-Origin-of-the-Mass-Metallicity-Relation%3A-from-Tremonti-Heckman/a5889b3327d930bc48df429110599886680556e4
- nrc-publications.canada.ca The Origin of the Mass-Metallicity Relation: Insights from 53,000 Star Opens in a new window — https://nrc-publications.canada.ca/eng/view/object/?id=7c12c587-de5b-4237-ae5d-3b37793e1423
- academic.oup.com Unveiling a cosmic tango: integral field spectroscopy and numerical simulations of Arp 143's interaction - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/550/2/stag1190/8714990
- academic.oup.com New fully empirical calibrations of strong-line metallicity indicators in star-forming galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/465/2/1384/2417485
- wikidata.org New fully empirical calibrations of strong-line metallicity indicators in Opens in a new window — https://www.wikidata.org/wiki/Q69185745
- orcid.org Mirko Curti - ORCID Opens in a new window — https://orcid.org/0000-0002-2678-2560
- osti.gov Similar star formation rate and metallicity variability time-scales drive the fundamental metallicity relation (Journal Article) | OSTI.GOV Opens in a new window — https://www.osti.gov/pages/biblio/1540633
- semanticscholar.org A fundamental relation between the metallicity, gas content, and stellar mass of local galaxies - Semantic Scholar Opens in a new window — https://www.semanticscholar.org/paper/A-fundamental-relation-between-the-metallicity%2C-gas-Bothwell-Maiolino/349a380d3ce93c0132f8e26bf74ece67fed994c0
- academic.oup.com fundamental relation between the metallicity, gas content and stellar mass of local galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/433/2/1425/1749733

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

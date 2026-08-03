# Review Base 10 raw Deep Research packet — Conroy 2013

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_14_kewley_nicholls_sutherland_2019_DR_PROMPT.md`
Prompt SHA-256: `d91f87680b2d04cd4eb9c92e9b2d46e258f90448161f1464d33398a7a5a95269`
Conversation ID: `14d5f9a96f2770b9`
Submit UTC: `2026-07-16T04:29:41.326002Z`
Research Start UTC: `2026-07-16T04:30:19.841581Z`
Result captured UTC: `2026-07-16T04:42:18.089332Z`
Raw result SHA-256: `9c7afbdcccf6962602ab013b3f99c88f89424e6bab3476718c87c8f6675a5b73`

## Deep Research review-base result

Advisory Reference Packet: Emission Line Diagnostics in Galaxy Evolution
Review Identity and Scope Map

Review Identity:

Authors: Lisa J. Kewley, David C. Nicholls, & Ralph S. Sutherland

Year: 2019

Title: Understanding Galaxy Evolution Through Emission Lines

Journal: Annual Review of Astronomy and Astrophysics

Volume/Pages: 57, 511–570

Identifiers: DOI 10.1146/annurev-astro-081817-051832; arXiv 1910.09730; ADS 2019ARA&A..57..511K.   

Scope Map:
The 2019 review by Kewley, Nicholls, and Sutherland operates as a comprehensive synthesis of the atomic physics, photoionization modeling, and observational calibrations required to deduce the fundamental properties of galaxies from their nebular emission spectra. Rather than presenting isolated empirical datasets, the text establishes a unified theoretical and empirical framework designed to track how the interstellar medium (ISM) interacts with diverse and extreme radiation fields across cosmic time. The scope comprehensively spans ultraviolet (UV), optical, and infrared (IR) wavelengths, acknowledging that no single spectral window can adequately capture the multiphase nature of the ISM.   

This framework is explicitly partitioned across several distinct astrophysical environments: the highly structured geometry of resolved H II regions, the blended composite signals of integrated whole-galaxy spectra, the extreme radiation fields of active galactic nuclei (AGN) narrow-line regions (NLRs), the kinematically violent boundaries of shock-heated gas, and the pervasive, low-density halos of diffuse ionized gas (DIG). By separating these environments, the review systematically maps quantitative diagnostics to derive excitation source, gas-phase metallicity (strictly on the 12+log(O/H) scale), dimensionless ionization parameter (U), ISM pressure (P), electron density (n
e
	​

), and the hardness of the ionizing continuum.   

Crucially, the review addresses the persistent historical tensions between competing abundance calibration methodologies. It meticulously distinguishes between direct electron-temperature (T
e
	​

) scales derived from auroral lines, recombination-line abundances, strong-line empirical sequences, and theoretically derived photoionization-model scales. By isolating the variables that drive systematic discrepancies—such as spatial resolution effects (spaxel vs. global aperture), theoretical uncertainties in atomic collision strengths, refractory element dust depletion factors, and the mixing of ionization mechanisms—the review acts as a definitive advisory baseline. It provides the necessary calibrations for interpreting multiplexed spectra from current integral field spectrographs and establishes the theoretical groundwork required for interpreting high-redshift observations.   

The Physical Stratification of Ionized Nebulae and Resulting Calibrations

The interpretation of galaxy spectra is fundamentally anchored in the physical reality that nebulae are not homogeneous slabs of gas, but highly stratified environments governed by radiative transfer, local gas density, and the specific shape of the incident ionizing continuum. The ionizing radiation emitted by central sources—whether an ensemble of massive OB stars or an accretion disk surrounding a supermassive black hole—is progressively absorbed and re-emitted as it travels outward. Because different atomic species possess distinct ionization potentials, they survive only in specific spatial concentric layers relative to the central source.   

Species with high ionization potentials, such as He$^+,O^{++},andNe^{++},requirephotonenergiessignificantlyhigherthan13.6eV(e.g.,thecreationofO^{++}$ requires photons > 35.1 eV). Consequently, emission lines from these highly ionized species, including prominent optical tracers like [O III] λλ4959,5007 and extreme UV resonance lines like C IV λ1549, originate almost exclusively from the innermost, hottest regions of the nebula immediately surrounding the radiation source. Conversely, species with lower ionization potentials, such as O$^+,N^+,andS^+$, are dominant in the cooler, outer boundary layers of the Strömgren sphere where the highest-energy photons have already been depleted. This geometric separation dictates that the [O II] λλ3726,3729 and [S II] λλ6716,6731 doublets carry information about the partially ionized transition zones rather than the deep interior.   

This stratification is the foundational mechanism that allows ratios of lines from different ionization states (e.g., [O III]/[O II] or [Ne III]/[Ne II]) to serve as powerful diagnostics of the dimensionless ionization parameter, U. The ionization parameter quantifies the ratio of the number density of hydrogen-ionizing photons to the local hydrogen gas density at the illuminated face of the cloud. A highly concentrated, luminous star cluster in a relatively low-density environment will drive a high U, inflating the volume of the highly ionized inner zone and thereby increasing the [O III]/[O II] ratio. However, extracting this parameter accurately requires complex photoionization codes like Cloudy or MAPPINGS, which iteratively calculate the energy balance, ionization state, and resulting line emissivities across fine geometric steps outward from the source.   

Excitation Diagnostics and the BPT Architecture

Understanding the dominant source of excitation is the primary prerequisite before any metallicity or density calibrations can be applied to a spectrum. The standard mechanism for this separation in the local universe is the Baldwin-Phillips-Terlevich (BPT) diagnostic diagram, primarily the projection of [O III] λ5007/H$\beta$ against [N II] λ6584/H$\alpha$. The architecture of this diagram is rooted entirely in the physical limits of stellar populations. The hottest, most massive main-sequence stars produce an ionizing continuum that drops off precipitously at 54.4 eV, meaning they produce negligible amounts of He$^+$ ionizing radiation. This caps the maximum temperature and the size of the partially ionized zone that a pure starburst can maintain. Theoretical models trace this limit as a firm envelope across parameter space—often termed the Kewley maximum starburst line.   

When a galaxy spectrum exhibits line ratios exceeding this boundary, an additional, harder non-thermal ionization source must be present. An AGN accretion disk generates a power-law continuum extending deep into the extreme ultraviolet (EUV) and X-ray regimes. These high-energy photons penetrate far deeper into the neutral surrounding medium, heating the gas via secondary Auger electrons and creating massive, extended partially ionized zones. These zones are the optimal environments for the collisional excitation of [N II], [S II], and [O I], driving the observed line ratios horizontally to the right and vertically upward on the BPT diagrams into the Seyfert and LINER (Low-Ionization Nuclear Emission-line Region) classifications.   

However, the synthesis warns explicitly against treating these boundaries as pure, isolated causal labels when dealing with integrated galaxy spectra or unresolved data. An integrated fiber encompassing an entire galaxy blends light from central AGN activity with extended H II region disks, producing a "composite" spectrum that falls between the empirical pure star-formation line (derived by Kauffmann) and the theoretical maximum starburst limit. Furthermore, fast radiative shocks driven by outflows or mergers generate intense collisional heating that produces line ratio vectors nearly identical to AGN excitation. The 2019 review highlights the integration of 3D Integral Field Spectroscopy (IFS) as the decisive mechanism for disentangling these effects, allowing the spatial mapping of emission-line gradients to isolate the central engine from shock fronts and star-forming rings.   

Established Findings
ID	Epistemic Type	Bounded Statement	Regime/Boundary	Confidence	Source Keys
REV14-E01	Established Mechanism	UV, optical, and IR emission lines arise from distinctly segregated physical zones within a nebula, rendering them complementary rather than strictly redundant.	All photoionized gas (H II regions, NLRs).	High	
REV14-E02	Theoretical Boundary	The [O III]/H$\beta$ vs. [N II]/H$\alpha$ BPT diagram relies on the maximum effective temperature of O-stars to place a hard theoretical limit on pure stellar photoionization.	z∼0, integrated or resolved optical spectra.	High	

Kewley 2001; Kauffmann 2003


REV14-E03	Observational Bias	Diffuse Ionized Gas (DIG) contamination artificially elevates integrated metallicity estimates and flattens abundance gradients due to higher [N II]/H$\alpha$ and [S II]/H$\alpha$ ratios in low-density, hard-radiation halos.	Integrated spectra, low-surface-brightness zones; 12+log(O/H)>8.0.	High	

Blanc 2015; Kewley 2019


REV14-E04	Measurement Offset	The Abundance Discrepancy Factor (ADF): Oxygen abundances derived from optical recombination lines (ORLs) systematically exceed those from collisionally excited lines (CELs) by a factor of 1.5 to 3.	High S/N local H II regions and planetary nebulae.	High	

Peimbert 1967; Kewley 2019


REV14-E05	Diagnostic Vector	Fast radiative shocks produce extended post-shock cooling zones that predictably shift optical line ratios away from the star-forming sequence toward the LINER/Seyfert regime, mimicking AGN.	Integrated galaxies and outflow/merger regions.	High	

Allen 2008; Kewley 2019


REV14-E06	Systematic Scale Difference	Metallicity estimates from theoretical photoionization models (e.g., MAPPINGS) are systematically 0.2 to 0.5 dex higher than empirical T
e
	​

-based abundance calibrations.	All metallicities, especially 12+log(O/H)>8.2.	High	

Kewley & Ellison 2008


REV14-E07	Cosmological Trend	The dimensionless ionization parameter, U, systematically increases in star-forming galaxies as a function of redshift (z>1.5), driven by denser clustering of massive stars.	High-redshift starbursts (z>1.5).	Mod-High	

Kewley 2019


REV14-E08	Atomic Physics Variance	The standard optical doublets [O II] λλ3726,3729 and [S II] λλ6716,6731 yield systematically different electron densities because they trace different spatial strata.	n
e
	​

∼10
1
−10
4
 cm$^{-3}$.	High	

Wang 2004; Kewley 2019


REV14-E09	Cosmological Trend	The "Cosmic BPT Shift": The star-forming sequence shifts systematically toward higher [O III]/H$\beta$ and/or higher [N II]/H$\alpha$ at high redshifts compared to the local universe.	Redshifts 1.5<z<3.0.	High	

Kewley 2013; Kewley 2019


REV14-E10	Chemical Mechanism	Gas-phase emission lines systematically underestimate the total nucleosynthetic yield of refractory elements (Fe, Mg, Si, C) because significant fractions are locked in solid dust grains.	ISM across all galaxies; dependent on radiation intensity.	High	

Peimbert 2010; Kewley 2019


REV14-E11	Methodological Advance	Integral Field Spectroscopy (IFS) successfully separates AGN, star-formation, and shock emission linearly across spatial dimensions, overcoming single-fiber aperture blending.	Local universe (z<0.1) at sub-kpc resolution.	High	

Belfiore 2016; Davies 2016


REV14-E12	Radiative Advantage	Mid- and far-infrared fine-structure lines (e.g., [Ne II], [Ne III]) are immune to T
e
	​

 fluctuations and dust attenuation, providing stable anchors for highly obscured systems.	Obscured LIRGs and ULIRGs.	High	

Armus 2007; Kewley 2019

  
Abundance Scale Tensions and Calibration Conflicts

The pursuit of mapping the cosmic chemical evolution of galaxies is entirely dependent on deriving accurate gas-phase metallicities from emission spectra. Typically parameterized by the oxygen abundance relative to hydrogen, 12+log(O/H), the field has historically relied on two vastly different methodologies that produce conflicting results: the direct electron-temperature (T
e
	​

) method and theoretical photoionization grids.   

The T
e
	​

 method, often heralded as the observational gold standard, utilizes the flux ratio of faint, highly temperature-sensitive auroral lines (such as [O III] λ4363) to lower-excitation nebular lines (such as [O III] λλ4959,5007). By applying the Boltzmann equation for collisionally excited states, astronomers can analytically derive the electron temperature of the specific ionization zone. Once the temperature is known, the emissivity equations can be inverted to yield the ionic abundance directly. However, collisionally excited lines (CELs) are exponentially sensitive to temperature. If a nebula contains unresolvable spatial temperature fluctuations—parameterized by the fluctuation amplitude t
2
—the high-temperature regions will disproportionately dominate the overall integrated line flux. Consequently, the derived T
e
	​

 will be artificially high, and the subsequently calculated oxygen abundance will be systematically underestimated.   

Conversely, oxygen abundances derived from faint optical recombination lines (ORLs), which scale inversely with temperature and are biased toward cooler, denser clumps, consistently yield metallicities higher than the CEL method by a factor of 1.5 to 3. This persistent gap is known as the Abundance Discrepancy Factor (ADF). Theoretical photoionization models generated by codes like MAPPINGS and Cloudy bypass the need for auroral lines entirely by simulating the full radiative transfer and energy balance of a nebula from first principles. By adjusting the input metallicity, ionization parameter, and pressure until the synthetic output spectrum matches the observed strong optical lines (like R
23
	​

), models extract an inferred abundance. However, because these models strictly enforce energy conservation and adopt parameterized geometric filling factors without incorporating the t
2
 fluctuations assumed to exist in nature, the absolute metallicities derived from theoretical grids are systematically 0.2 to 0.5 dex higher than those calibrated against local T
e
	​

 empirical sequences.   

The review establishes that this 0.2–0.5 dex offset must be treated strictly as a systematic scale difference, rather than as a random error. Because strong-line empirical calibrations (such as O3N2 or N2) are generally anchored to sets of local H II regions whose abundances were measured via the T
e
	​

 method, they inherit this lower absolute scale. If researchers directly compare the metallicity of a high-redshift galaxy modeled via a Bayesian theoretical pipeline to a local galaxy measured via an empirical O3N2 calibration, the resulting chemical evolution trajectory will be fundamentally corrupted by the scale mismatch.   

Open Debates and Tensions
ID	Competing Positions	Why Unresolved in 2019	Source Keys
REV14-D01	The Absolute Metallicity Scale: T
e
	​

-based direct measurements represent the "true" base metallicity vs. Theoretical models provide the correct scale because T
e
	​

 methods suffer from severe, uncorrected thermal fluctuations (t
2
).	Insufficient spatial resolution to physically measure internal temperature gradients across statistically significant samples of distant H II regions.	

Kewley & Ellison 2008; Blanc 2015


REV14-D02	Physical Nature of LINERs: Driven by low-accretion-rate supermassive black holes, extended Hot Old Low-Mass Evolved Stars (HOLMES), or large-scale slow radiative shocks.	Degeneracy: All three mechanisms produce identical optical line ratio vectors in the [O III]/H$\beta$ vs. [N II]/H$\alpha$ plane without kinematics or X-ray data to break the tie.	

Belfiore 2016; Kewley 2019


REV14-D03	Drivers of the High-z BPT Shift: Caused by systematically higher ionization parameters (U), harder stellar ionizing continua from binary evolution, or elevated N/O abundance ratios.	Extracting U and N/O required cleanly detecting weak auroral or UV lines at z>2, which generally exceeded the sensitivity of pre-JWST observatories.	

Kewley 2013; Steidel 2014


REV14-D04	ADF Causality: The Abundance Discrepancy Factor is caused either by non-thermal κ-distributions of electron energies or by purely spatial temperature fluctuations (t
2
) within the nebula.	Plasma physics arguments dispute the survival of κ-distributions in collisional gas, while observers argue t
2
 requirements are unphysically high.	

Nicholls 2012; Peimbert 1967


REV14-D05	Primary vs. Secondary Nitrogen Transition: The exact metallicity at which Nitrogen transitions from primary (independent of Z) to secondary (dependent on CNO abundance) is highly scattered.	Differs wildly based on an individual galaxy's specific star-formation and inflow/outflow history, severely compromising N2-based strong-line indices.	

Alloin 1979; Kewley 2019


REV14-D06	Calibration of the Rest-UV: UV lines (C III], O III]) are robust standalone metallicity diagnostics vs. they are heavily degenerate with complex carbon depletion factors.	High excitation energies make UV lines hyper-sensitive to continuum shape. Lacked simultaneous deep optical data to constrain physical conditions.	

Stark 2014; Kewley 2019


REV14-D07	Separating AGN and Shocks: Standard 2D diagnostic diagrams are insufficient to decouple Seyfert emission from fast radiative shocks.	Both mechanisms yield similar degrees of partial ionization in the transition zone, requiring 3D velocity dispersion (σ) mapping for separation.	

Allen 2008; Rich 2011


REV14-D08	Impact of Stellar Rotation: SPS models must include binary mass-transfer and massive stellar rotation to reproduce hard high-z ionizing spectra vs. adjusting U and covering fractions is sufficient.	Binary grids (e.g., BPASS) introduce vast, poorly constrained parameter spaces regarding mass-transfer efficiencies in low-metallicity environments.	

Levesque 2010; Xiao 2018

  
Quantitative Diagnostic Calibrations

To navigate the complex degeneracies of nebular physics, astronomers employ specific line ratios calibrated either empirically against large local galaxy samples (like SDSS) or theoretically via iterative photoionization grids. The R
23
	​

 parameter is perhaps the most widely recognized strong-line index for oxygen abundance, utilizing the sum of the primary [O II] and [O III] collisionally excited lines normalized to H$\beta$. Because it includes both the singly and doubly ionized states of oxygen, R
23
	​

 is largely insensitive to first-order variations in the ionization parameter. However, R
23
	​

 is notoriously double-valued: at low metallicities, the ratio increases as oxygen abundance increases due to a higher total number of emitting ions; but at high metallicities, efficient fine-structure cooling drastically lowers the electron temperature, exponentially suppressing the optical line strengths and causing the R
23
	​

 ratio to plummet. Breaking this degeneracy requires a secondary, monotonically scaling diagnostic, typically involving nitrogen (e.g., [N II]/[O II]), under the assumption that nitrogen scales as a secondary nucleosynthetic element at high metallicities.   

Alternatively, the O3N2 diagnostic index utilizes the log ratio of [O III]/H$\beta$ to [N II]/H$\alpha$. Because the paired lines are exceptionally close in wavelength, O3N2 is virtually immune to uncertainties in interstellar dust attenuation. Calibrated empirically by Pettini & Pagel (2004) against a local anchor of T
e
	​

-measured H II regions, it is heavily relied upon for local, low-extinction studies. However, the review clearly cautions against transporting local empirical calibrations derived in specific excitation and density regimes directly to high-redshift targets without corrections, as differing ISM pressures and harder ionizing fields systemically alter the line ratios.   

Extracting the electron density (n
e
	​

) relies primarily on the ratios of close forbidden-line doublets originating from different atomic levels with similar excitation potentials but divergent critical densities. As electron density increases, collisional de-excitation begins to dominate over radiative decay for the level with the lower transition probability. Consequently, the observed flux ratio of the [S II] λ6716/λ6731 and [O II] λ3729/λ3726 lines functions as a direct barometer for the density of the emitting gas. However, the review emphasizes that because O$^+$ and S$^+$ exist in slightly different geometrical layers of the Strömgren sphere, applying the [O II] diagnostic will inherently trace slightly deeper, denser, and higher-pressure regions than the [S II] diagnostic, necessitating careful consideration of the assumed uniform density model.   

Key Measurements and Model Calibrations
ID	Diagnostic / Calibration	Exact Definition & Units	Regime & Assumptions	Uncertainty / Status	Source Keys
REV14-N01	Ionization Parameter (U)	

U≡
4πr
2
n
H
	​

c
Q(H
0
)
	​





(Dimensionless)

	Characterizes the global radiation field intensity at the inner boundary of the Strömgren sphere.	Validated definition; highly sensitive to assumed geometric covering fractions.	

Kewley 2019; Osterbrock 2006


REV14-N02	Max Starburst Boundary	log([O III]/Hβ)=
log([N II]/Hα)−0.47
0.61
	​

+1.19	Integrated optical spectra; marks the absolute theoretical limit of pure stellar photoionization.	Robust constraint separating extreme starbursts from AGN/Shock composites.	

Kewley 2001; Kewley 2019


REV14-N03	Pure Star-Formation Limit	log([O III]/Hβ)=
log([N II]/Hα)−0.05
0.61
	​

+1.3	Empirically marks the upper envelope of purely star-forming galaxies in local SDSS data.	Firmly established locally; intermediate zone denotes "Composite" excitation.	

Kauffmann 2003


REV14-N04	R23 Metallicity Index	R
23
	​

=
Hβ
[O II]λλ3726,3729+[O III]λλ4959,5007
	​

	Global proxy tracing both low and high-ionization oxygen zones. Maps to 12+log(O/H).	Highly double-valued. Requires a secondary indicator to break degeneracy.	

Pagel 1979; Kewley & Dopita 2002


REV14-N05	O3N2 Metallicity Index	O3N2=log(
[N II]λ6583/Hα
[O III]λ5007/Hβ
	​

)	Cross-strata optical diagnostic heavily dependent on N/O ratios. Maps to 12+log(O/H).	Single-valued, dust-immune. Fails at low Z and is sensitive to N/O scatter.	

Pettini & Pagel 2004


REV14-N06	Optical Density Doublets	Flux ratios of I([S II]λ6716)/I([S II]λ6731) and I([O II]λ3729)/I([O II]λ3726).	Maps to n
e
	​

 in cm$^{-3}$ assuming T
e
	​

∼10
4
 K. Sensitive from 10
2
−10
4
 cm$^{-3}$.	Robust, but [O II] and [S II] probe different geometric strata, yielding different n
e
	​

.	

Osterbrock 2006


REV14-N07	Direct T
e
	​

 (Auroral Method)	T
e
	​

∝I([O III]λ4363)/I([O III]λλ4959,5007).	High-excitation O$^{++}$ inner zone. Yields Temperature in K.	Prone to ADF underestimation if temperature fluctuations (t
2
) are severe.	

Peimbert 1967


REV14-N08	Mid-IR Fine Structure Ionization	Flux ratio of [Ne III]15.56μm/[Ne II]12.81μm.	Dust-obscured starburst cores and tori. Acts as an immune proxy for U.	Highly immune to dust and thermal variations. Necessitates space observatories.	

Armus 2007; Kewley 2019

  
Cosmological Evolution and Observational Frontiers

The application of emission line diagnostics across cosmic time introduces profound methodological challenges. The review documents that galaxies at z>1.5 exhibit systematically distinct properties from local samples: higher specific star-formation rates, denser and more compact geometries, and elevated global ISM pressures. These evolving physical baselines culminate in the "Cosmic BPT Shift," where high-redshift star-forming galaxies universally migrate toward the upper-right of the classical optical BPT diagnostic plane. Treating this shift solely as a metallicity effect leads to severe analytical failures. Instead, the displacement is a complex convolution of varying N/O abundance ratios, harder unattenuated ionizing spectra driven by young binary populations at low metallicities, and fundamentally higher ionization parameters.   

To address these shifting baselines, the synthesis explicitly advocates for the development of fully unified diagnostic grids that cross-calibrate optical forbidden lines with high-energy rest-UV resonance lines (e.g., C III], Si III]) and low-energy rest-IR fine-structure lines (e.g., [Ne II], [Ne III]). Because infrared fine-structure lines have excitation energies orders of magnitude lower than optical transitions, they remain strictly impervious to the electron temperature fluctuations that plague T
e
	​

 direct methods, offering a stable anchor for calculating abundances in dense, dusty starbursts. Conversely, as optical diagnostics redshift out of accessible observing windows at extreme redshifts (z>4), the calibration of rest-UV lines becomes mandatory for mapping the earliest epochs of galaxy assembly.   

What Remained Unknown in 2019
ID	Unknown Parameter / Domain	Why It Matters	Decisive Improvement Needed
REV14-U01	High-z BPT Line Ratio Displacement Causal Vectors	Without identifying the specific driver of the cosmic BPT shift (higher U, lower Z, harder spectra), metallicity measurements of early galaxies remain fundamentally biased by up to 0.5 dex.	

Deep rest-optical and rest-UV IFS mapping from z=2 to 8 to capture auroral lines and explicitly measure T
e
	​

 and U concurrently.


REV14-U02	Resolution of the Abundance Discrepancy Factor	The 0.2 to 0.5 dex disagreement between recombination and collisionally excited lines prohibits the establishment of a single, true absolute metallicity scale.	

Sub-parsec IFS mapping of local Galactic H II regions to directly measure 3D temperature fluctuations (t
2
) and validate plasma physics.


REV14-U03	3D Topologies Replacing 1D Spherical Models	1D photoionization grids assume uniform spherical geometries, failing to account for porous, fractal ISM structures where radiation leaks and shocks mix with photoionization.	

Coupling high-resolution 3D hydrodynamical simulations of star formation directly with full radiative transfer codes.


REV14-U04	Rest-UV Diagnostics Calibration	Rest-UV lines (C III], O III]) lack the stable calibration of optical lines, limiting abundance tracking at extreme redshifts where optical lines are inaccessible.	

Empirical cross-calibration of UV lines against direct T
e
	​

 metallicities in statistically complete local analog samples.


REV14-U05	Unified Shock vs. AGN Separation Parameters	Misclassifying shock-heated gas from galactic outflows as an active black hole dramatically skews measurements of cosmic AGN accretion histories.	

3D diagnostic data cubes that explicitly combine emission line ratios with high-resolution velocity dispersion (σ) mapping.


REV14-U06	Precision Dust Depletion Modeling	If the fraction of refractory elements (Si, C, Fe) locked in dust grains varies wildly as a function of radiation hardness, derived absolute abundances from the gas phase are fundamentally broken.	

High-resolution multi-wavelength measurements spanning atomic gas, molecular gas, and mid-IR dust continuum to explicitly track depletion factors.

  
Primary-Citation Harvest

The following literature composes the principal evidence base synthesized by the 2019 review, partitioned by role.

Key	Citation details (Authors, Year, Journal, Title)	Identifiers (DOI, arXiv, ADS)	Role	Boundary / Focus
REV14-P001	Acharyya A, Krumholz M, Federrath C, 2019, MNRAS, "Submitted"	none, none, none	Model grids	Simulates 3D fractal ISM models and their impact on resultant emission line fluxes.
REV14-P002	Afflerbach A, Churchwell E, Werner MW, 1997, ApJ, "Galactic H II Regions..."	10.1086/303774, none, 1997ApJ...478..190A	Measurements	Establishes mid-IR fine structure emission properties in H II regions.
REV14-P003	Allen MG, Dopita MA, Tsvetanov ZI, 1998, ApJ, "Bow Shocks in the Narrow-Line Region..."	10.1086/305144, astro-ph/9708232, 1998ApJ...493..571A	Shock simulations	Establishes shock plus precursor models for interpreting AGN narrow-line regions.
REV14-P004	Allen MG, Groves BA, Dopita MA, 2008, ApJS, "The MAPPINGS III Library of Fast Radiative Shock Models"	10.1086/589652, 0805.0204, 2008ApJS..178...20A	Shock simulations	Baseline theoretical grid for mapping shock line-ratio trajectories.
REV14-P005	Aller LH, 1942, ApJ, "A Study of Emission-Line Intensities in Some Planetary Nebulae"	10.1086/144372, none, 1942ApJ....95...52A	Analytic/atomic	Foundational historical work establishing physical conditions and atomic processes in nebulae.
REV14-P006	Aller LH, 1984, Physics of Thermal Gaseous Nebulae	none, none, 1984ptgn.book.....A	Analytic/atomic	Foundational textbook defining nebular astrophysics and fundamental radiative transfer.
REV14-P007	Alloin D, Collin-Souffrin S, Joly M, Vigroux L, 1979, A&A, "Nitrogen and oxygen abundances in galaxies"	none, none, 1979A&A....78..200A	Measurements	Key baseline empirical measurement of primary vs. secondary N/O ratio behaviors.
REV14-P008	Anders E, Grevesse N, 1989, Geochim. Cosmochim. Acta, "Abundances of the elements..."	10.1016/0016-7037(89)90286-X, none, 1989GeCoA..53..197A	Analytic/atomic	Historical baseline for calibrating solar and cosmic elemental abundance scales.
REV14-P009	Andrews BH, Martini P, 2013, ApJ, "The Mass-Metallicity Relation..."	10.1088/0004-637X/765/2/140, 1211.3418, 2013ApJ...765..140A	Measurements	Establishes local empirical mass-metallicity baselines against which evolution is measured.
REV14-P010	Armus L, Charmandaris V, Bernard-Salas J, et al., 2007, ApJ, "Observations of Ultraluminous Infrared Galaxies..."	10.1086/510107, astro-ph/0610114, 2007ApJ...656..148A	Measurements	Proves IR fine-structure lines as robust diagnostics unaffected by dust in ULIRGs.
REV14-P011	Asplund M, Grevesse N, Sauval AJ, Scott P, 2009, ARA&A, "The Chemical Composition of the Sun"	10.1146/annurev.astro.46.060407.145222, 0909.0948, 2009ARA&A..47..481A	Analytic/atomic	The modern standard anchor defining absolute solar elemental abundances.
REV14-P012	Baldry IK, Glazebrook K, Baugh CM, 2002, ApJ, "The 2dF Galaxy Redshift Survey..."	10.1086/339477, astro-ph/0110676, 2002ApJ...569..582B	Measurements	Establishes bulk integrated global parameters for local galaxy surveys.
REV14-P013	Baldwin JA, Phillips MM, Terlevich R, 1981, PASP, "Classification parameters for the emission-line spectra..."	10.1086/130766, none, 1981PASP...93....5B	Analytic/calibration	Formulates the definitive structural BPT diagnostic framework separating AGN from H II regions.
REV14-P014	Barnes JE, Wood K, Hill AS, Haffner LM, 2015, MNRAS, "Photoionization of the diffuse ionized gas..."	10.1093/mnras/stu2485, 1411.5365, 2015MNRAS.447..559B	Photoionization simulations	Models the radiative transfer and dilution of radiation responsible for forming the DIG.
REV14-P015	Belfiore F, Maiolino R, Maraston C, et al., 2016, MNRAS, "SDSS IV MaNGA - spatially resolved diagnostic diagrams..."	10.1093/mnras/stw1234, 1605.07635, 2016MNRAS.461.3111B	Measurements	Employs resolved spaxels to disentangle LINER emission vectors from pure star-forming regions.
REV14-P016	Bertoldi F, 1989, ApJ, "The photoionization of interstellar clouds..."	10.1086/168041, none, 1989ApJ...346..735B	Analytic/atomic	Formalizes the radiative transfer physics and boundary conditions at ionization fronts.
REV14-P017	Binette L, Dopita MA, Tuohy IR, 1985, ApJ, "Radiative shock-wave theory. II..."	10.1086/163546, none, 1985ApJ...297..476B	Shock simulations	Historical theoretical baseline establishing shock emission cooling vectors.
REV14-P018	Blanc GA, Kewley L, Vogt FPA, Dopita MA, 2015, ApJ, "IZI: Inferring the Metallicity and Ionization Parameter..."	10.1088/0004-637X/798/2/99, 1409.0558, 2015ApJ...798...99B	Analytic/calibration	Introduces the IZI tool for the joint Bayesian inference of Z and U from grids.
REV14-P019	Bland-Hawthorn J, Freeman KC, Quinn PJ, 1997, ApJ, "Where Do the Elements Go?..."	10.1086/304899, astro-ph/9707011, 1997ApJ...490..143B	Measurements	Observational tracing of galactic wind ionization and large-scale metal transport.
REV14-P020	Bresolin F, Kennicutt RC Jr, Garnett DR, 1999, ApJ, "Electron Temperatures and Abundances..."	10.1086/306561, astro-ph/9808064, 1999ApJ...510..104B	Measurements	Essential direct T
e
	​

 empirical measurement mapping across inner H II regions.
REV14-P021	Brinchmann J, Charlot S, White SDM, et al., 2004, MNRAS, "The physical properties of star-forming galaxies..."	10.1111/j.1365-2966.2004.08102.x, astro-ph/0311058, 2004MNRAS.351.1151B	Analytic/calibration	Constructs robust, statistically complete SFR and metallicity parameters for SDSS galaxies.
REV14-P022	Bressan A, Chiosi C, Fagotto F, 1994, ApJS, "Evolutionary sequences of stellar models..."	10.1086/192074, astro-ph/9406085, 1994ApJS...94...63B	Model grids	Fundamental stellar population evolutionary tracks used for generating input ionizing continua.
REV14-P023	Cardelli JA, Clayton GC, Mathis JS, 1989, ApJ, "The relationship between infrared, optical, and ultraviolet extinction"	10.1086/167900, none, 1989ApJ...345..245C	Analytic/calibration	Formulates the definitive multi-wavelength standard galactic dust attenuation law.
REV14-P024	Chabrier G, 2003, PASP, "Galactic Stellar and Substellar Initial Mass Function"	10.1086/376392, astro-ph/0304382, 2003PASP..115..763C	Analytic/calibration	Primary Initial Mass Function (IMF) utilized in synthesizing incident stellar radiation spectra.
REV14-P025	Calzetti D, Armus L, Bohlin RC, et al., 2000, ApJ, "The Dust Content and Opacity of Actively Star-forming Galaxies"	10.1086/308692, astro-ph/9911459, 2000ApJ...533..682C	Analytic/calibration	Establishes the standard attenuation law tailored explicitly for high-extinction starburst galaxies.
REV14-P026	Davies R, Kewley LJ, Ho IT, et al., 2016, MNRAS, "The host galaxies and classification of active galactic nuclei..."	10.1093/mnras/stw1943, 1608.01662, 2016MNRAS.462.1616D	Measurements	Utilizes 3D IFS spaxels to accurately isolate central AGN flux from extended star formation.
REV14-P027	Dopita MA, Sutherland RS, 1995, ApJ, "Spectral Signatures of Fast Shocks. II..."	10.1086/176596, none, 1995ApJ...455..468D	Shock simulations	The definitive theoretical baseline for mapping fast-shock behaviors in optical diagnostics.
REV14-P028	Dopita MA, Kewley LJ, Sutherland RS, Nicholls DC, 2016, Ap&SS, "Theoretical evolution of optical strong lines..."	10.1007/s10509-016-2657-8, 1601.07632, 2016Ap&SS.361...61D	Photoionization simulations	Tracks the modeled cosmic evolution and displacement of the optical BPT sequences.
REV14-P029	Ferland GJ, Korista KT, Verner DA, et al., 1998, PASP, "CLOUDY 90: Numerical Simulation of Plasmas and Their Spectra"	10.1086/316190, none, 1998PASP..110..761F	Model grids	Details the core physics and architecture of the widely utilized Cloudy photoionization software.
REV14-P030	Garnett DR, 1992, AJ, "Electron temperature variations and the measurement of nebular abundances"	10.1086/116124, none, 1992AJ....103.1330G	Measurements	Observational assessment of internal nebular gradients and empirical T
e
	​

 measurement accuracy.
REV14-P031	Groves BA, Dopita MA, Sutherland RS, 2004, ApJS, "Dusty, Radiation Pressure-dominated Photoionization..."	10.1086/421114, astro-ph/0403668, 2004ApJS..153...75G	Photoionization simulations	Foundational model grid defining the physics of dusty, radiation-pressure-dominated AGN NLRs.
REV14-P032	Kauffmann G, Heckman TM, Tremonti C, et al., 2003, MNRAS, "The host galaxies of active galactic nuclei"	10.1111/j.1365-2966.2003.07154.x, astro-ph/0304239, 2003MNRAS.346.1055K	Analytic/calibration	Statistically establishes the empirical pure star-formation demarcation limit on the BPT.
REV14-P033	Kewley LJ, Dopita MA, Sutherland RS, Heisler CA, Trevena J, 2001, ApJ, "Theoretical Modeling of Starburst Galaxies"	10.1086/321545, astro-ph/0106324, 2001ApJ...556..121K	Photoionization simulations	Calculates the absolute theoretical maximum starburst envelope line on the BPT diagram.
REV14-P034	Kewley LJ, Dopita MA, 2002, ApJS, "Using Strong Lines to Estimate Abundances in Extragalactic H II Regions..."	10.1086/341326, astro-ph/0206495, 2002ApJS..142...35K	Analytic/calibration	Foundational theoretical paper formally deriving and calibrating the R
23
	​

 strong-line index.
REV14-P035	Kewley LJ, Ellison SL, 2008, ApJ, "Metallicity Calibrations and the Mass-Metallicity Relation..."	10.1086/587500, 0801.1849, 2008ApJ...681.1183K	Analytic/calibration	Explicitly provides polynomial fits to convert between conflicting theoretical and empirical metallicity scales.
REV14-P036	Kewley LJ, Dopita MA, Leitherer C, et al., 2013, ApJ, "Theoretical Evolution of Optical Strong Lines across Cosmic Time"	10.1088/0004-637X/774/2/100, 1307.0508, 2013ApJ...774..100K	Photoionization simulations	Tracks the observed cosmic BPT shift and establishes its link to evolving ionization parameters.
REV14-P037	Maiolino R, Mannucci F, 2019, A&ARv, "De re metallica: the cosmic chemical evolution of galaxies"	10.1007/s00159-018-0112-2, 1811.08259, 2019A&ARv..27....3M	Supporting reviews	Comprehensive peer review detailing the mass-metallicity relationship and its systemic scatter.
REV14-P038	Nicholls DC, Dopita MA, Sutherland RS, 2012, ApJ, "Resolving the Electron Temperature Discrepancies..."	10.1088/0004-637X/752/2/148, 1204.3888, 2012ApJ...752..148N	Analytic/atomic	Mathematically introduces κ-distributed non-thermal electrons as a resolution to the ADF.
REV14-P039	Osterbrock DE, Ferland GJ, 2006, Astrophysics of Gaseous Nebulae and Active Galactic Nuclei	none, none, 2006agna.book.....O	Analytic/atomic	The authoritative, definitive textbook on the fundamental atomic physics of emission lines.
REV14-P040	Pagel BEJ, Edmunds MG, Blackwell DE, et al., 1979, MNRAS, "On the composition of H II regions in southern galaxies - I..."	10.1093/mnras/189.1.95, none, 1979MNRAS.189...95P	Analytic/calibration	Originates the foundational concept and initial empirical calibration of the R
23
	​

 index.
REV14-P041	Peimbert M, 1967, ApJ, "Temperature Determinations of H II Regions"	10.1086/149385, none, 1967ApJ...150..825P	Analytic/atomic	First establishes the t
2
 spatial temperature fluctuation paradigm complicating T
e
	​

 measurements.
REV14-P042	Peimbert M, Costero R, 1969, Bol. Obs. Tonantzintla Tacubaya, "Chemical abundances in Galactic H II regions"	none, none, 1969BOTT....5....3P	Measurements	Definitive early derivation mapping spatial abundance variations within the Milky Way.
REV14-P043	Peimbert M, Peimbert A, Delgado-Inglada G, 2017, PASP, "Nebular Spectroscopy: A Guide on H II Regions and Planetary Nebulae"	10.1088/1538-3873/aa79d4, 1704.01671, 2017PASP..129h2001P	Supporting reviews	Comprehensive guide addressing the limitations and corrections required for direct T
e
	​

 methodology.
REV14-P044	Pettini M, Pagel BEJ, 2004, MNRAS, "[OIII]/[NII] as an abundance indicator at high redshift"	10.1111/j.1365-2966.2004.07591.x, astro-ph/0401128, 2004MNRAS.348L..59P	Analytic/calibration	Derives the widely utilized, empirically anchored O3N2 diagnostic index.
REV14-P045	Tremonti CA, Heckman TM, Kauffmann G, et al., 2004, ApJ, "The Origin of the Mass-Metallicity Relation..."	10.1086/423264, astro-ph/0405537, 2004ApJ...613..898T	Measurements	Statistically anchors the definitive local mass-metallicity relation utilizing Bayesian MAPPINGS fits.
DO_NOT_USE_UNVERIFIED Quarantine

The following sources were surfaced during literature crawling but represent post-2019 data, unrelated domain overlap, or specific high-redshift results from next-generation facilities (like JWST) that were not part of the 2019 Kewley et al. literature base. They must strictly be excluded from this synthesis:

Curti et al. (2020), (2023): UNCITED_NOT_USABLE (Post-2019 calibration refinement and JWST direct metallicities).

Katz et al. (2023): UNCITED_NOT_USABLE (Post-2019 JWST high-redshift line ratios).

Arellano-Córdova et al. (2022): UNCITED_NOT_USABLE (JWST/NIRSpec abundance patterns).

Mendez-Delgado et al. (2022): UNCITED_NOT_USABLE (Post-2019 Gaia parallax/temperature studies).

Cameron et al. (2021): UNCITED_NOT_USABLE (Post-2019 BPT studies).

Any publication referencing "JWST", "CEERS", "NIRCam", or "NIRSpec" results. UNCITED_NOT_USABLE

Composite Identity Ledger

Target Synthesis Document: Kewley L.J., Nicholls D.C., Sutherland R.S., 2019, ARA&A, 57, 511. (DOI 10.1146/annurev-astro-081817-051832).

Primary Theoretical Engines: Cloudy (Ferland et al. 1998, 2013) and MAPPINGS III/IV (Sutherland, Dopita, Allen, Kewley).

Atomic-data dependency flag: Models rely heavily on specified collision strengths and assumptions of thermal equilibrium vs. non-Maxwellian distributions (Nicholls et al. 2012), which fundamentally alter the grid outputs and the resulting abundance scales.

Principal Calibration Scales Confirmed:

Theoretical Strong-Line: Kewley & Dopita 2002 (R23); Tremonti et al. 2004 (Bayesian pipeline).

Calibration-scale conflict flag: Theoretical grids yield absolute 12+log(O/H) values systematically ∼0.2−0.5 dex higher than empirical data.

Empirical Strong-Line: Pettini & Pagel 2004 (O3N2, N2).

Diagnostic version flag: Anchored specifically to local H II region T
e
	​

 measurements; fails when applied at cosmic noon without adjustment.

Boundary Definitions Maintained:

Kewley et al. 2001 (Maximum theoretical starburst).

Kauffmann et al. 2003 (Pure star-formation limit).

Sample/aperture mismatch flag: Care must be taken not to apply these integrated-galaxy boundaries directly to high-resolution spaxels without accounting for DIG and overlapping shock emission (Belfiore et al. 2016).

REVIEW_BASE_14_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- researchportalplus.anu.edu.au Understanding Galaxy Evolution through Emission Lines - ANU Researcher Portal Opens in a new window — https://researchportalplus.anu.edu.au/en/publications/understanding-galaxy-evolution-through-emission-lines/
- arxiv.org [1910.09730] Understanding Galaxy Evolution through Emission Lines - arXiv Opens in a new window — https://arxiv.org/abs/1910.09730
- annualreviews.org Understanding Galaxy Evolution Through Emission Lines | Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-081817-051832
- academic.oup.com Identifying AGNs from X-ray detections – I: Metallicity calibrations in AGNs with X-ray luminosity as the primary input parameter - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/doi/10.1093/mnras/stag560/8539724
- w0.ned.ipac.caltech.edu Spatially-Resolved Spectroscopic Properties of Low-Redshift Star-Forming Galaxies Opens in a new window — http://w0.ned.ipac.caltech.edu/level5/Sept19/Sanchez/paper.pdf
- arxiv.org A new CIGALE module for modeling AGN emission lines - arXiv Opens in a new window — https://arxiv.org/html/2606.14643v1
- nepjol.info A comprehensive photoionization model of IC 418: physical conditions, ionization structure, and chemical abundances Opens in a new window — https://www.nepjol.info/index.php/SW/article/view/95618/72374
- arxiv.org Galaxy mergers drive enhancements in ionization states - arXiv Opens in a new window — https://arxiv.org/html/2607.12024v1
- arxiv.org A DESI Calibration of the [O II]–[S II] Electron-density Offset in Integrated Star-forming Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2606.28129
- arxiv.org 1 Introduction - arXiv Opens in a new window — https://arxiv.org/html/2509.00818v1
- arxiv.org Applications of Stellar Population Synthesis in the Distant Universe - arXiv Opens in a new window — https://arxiv.org/pdf/2005.01759
- academic.oup.com Identifying AGNs from X-ray detections – I: Metallicity calibrations in AGNs with X-ray luminosity as the primary input parameter - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/548/1/stag560/8539724
- thesis.unipd.it A KEY TOOL TO PROBE EUCLID SPECTROSCOPY: SPECTRO-PHOTOMETRIC SIMULATIONS OF GALAXIES TO UNRAVEL NISP'S CAPABILITIES By LOUIS G - Padua Thesis and Dissertation Archive Opens in a new window — https://thesis.unipd.it/retrieve/8a68a807-8ab8-42d9-abc0-f631903c80dc/GABARRA-TESI.pdf
- arxiv.org Origins of Extreme Emission-Line Ratios in z>3 Galaxies: Insights from the Lumen Model Opens in a new window — https://arxiv.org/html/2605.06769v2
- edoc.ub.uni-muenchen.de Simulating the multi-phase interstellar medium and galactic outflows Opens in a new window — https://edoc.ub.uni-muenchen.de/28795/1/Rathjen_Tim-Eric.pdf
- academic.oup.com Machine learning-based classification of active galaxies and estimation of supermassive black hole masses | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/548/4/stag627/8661526
- arxiv.org pop-cosmos: Disentangling galaxy properties from observables using data-driven approaches - arXiv Opens in a new window — https://arxiv.org/html/2606.11308v2
- academic.oup.com Kiloparsec-scale outflows are prevalent among luminous AGN: outflows and feedback in the context of the overall AGN population | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/441/4/3306/1198892
- cambridge.org New techniques to investigate the AGN-SF connection with integral field spectroscopy | Publications of the Astronomical Society of Australia Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/new-techniques-to-investigate-the-agnsf-connection-with-integral-field-spectroscopy/1BF4E9F4CE04C7CA8B6C8462E6AD4416
- amsdottorato.unibo.it Exploring interstellar medium conditions in AGN and star forming galaxies with integral field spectroscopy - AMS Dottorato Opens in a new window — https://amsdottorato.unibo.it/id/eprint/9461/1/thesis_final_mingozzi.pdf
- ouci.dntb.gov.ua Temperature inhomogeneities cause the abundance discrepancy in H ii regions - OUCI Opens in a new window — https://ouci.dntb.gov.ua/en/works/4On1noW7/
- open.metu.edu.tr arXiv:2208.01658v3 [astro-ph.CO] 20 Dec 2022 Opens in a new window — https://open.metu.edu.tr/bitstream/handle/11511/116583/index.pdf
- scholar.google.co.jp ‪Lisa Kewley‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.co.jp/citations?user=XYbseF0AAAAJ&hl=ja
- arxiv.org The First Empirical Calibration of the MIR Abundance Diagnostic Ne 23 with JWST - arXiv Opens in a new window — https://arxiv.org/html/2604.27056v1
- researchgate.net (PDF) MARTA: Temperature-temperature relationships and strong-line metallicity calibrations from multiple auroral-line detections at cosmic noon - ResearchGate Opens in a new window — https://www.researchgate.net/publication/390569743_MARTA_Temperature-temperature_relationships_and_strong-line_metallicity_calibrations_from_multiple_auroral_lines_detections_at_cosmic_noon
- arxiv.org Metallicity calibrations in AGNs with X-ray luminosity as the primary input parameter - arXiv Opens in a new window — https://arxiv.org/html/2603.19181v3
- ouci.dntb.gov.ua Spectroscopic Observations and Emission-Line Diagnoses for H ii Regions in the Late-Type Spiral Galaxy NGC 2403 - OUCI Opens in a new window — https://ouci.dntb.gov.ua/en/works/7XaVpNzb/
- scholar.google.com ‪Ralph Sutherland‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=u_s4uC4AAAAJ&hl=en
- explore.openaire.eu Assessing model-based carbon and oxygen abundance derivation Opens in a new window — https://explore.openaire.eu/search/publication?pid=10.1093%2Fmnras%2Fstad621
- archive.iaa.csic.es Identification and characterization of emission line objects in J-PAS using artificial neural network - Instituto de Astrofísica de Andalucía, IAA-CSIC Opens in a new window — https://archive.iaa.csic.es/sites/default/files/thesis/tesis_martinez_solaeche.pdf
- search.proquest.com On the Hunt for AGN: An Exploration of the Observational Diversity of Active Galaxies Opens in a new window — https://search.proquest.com/openview/76bffa82f3008014c956e77a9793e17d/1?pq-origsite=gscholar&cbl=18750&diss=y
- spiedigitallibrary.org NGC 925 with SITELLE: HII region analysis - SPIE Digital Library Opens in a new window — https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12184/121846B/NGC-925-with-SITELLE-HII-region-analysis/10.1117/12.2628833.short
- iag.usp.br The miniJPAS survey: Identification and characterization of the emission line galaxies down to z < 0.35 in the AEGIS field - IAG-USP Opens in a new window — https://www.iag.usp.br/sites/default/files/2023-05/arxiv_CM006_2204.01698.pdf
- nagoya.repo.nii.ac.jp A study on the multi-phase interstellar medium in a star-forming galaxy at the epoch of reionization with near-infrared and (sub Opens in a new window — https://nagoya.repo.nii.ac.jp/record/2012457/files/k15243_thesis.pdf
- archiv.ub.uni-heidelberg.de Dissertation submitted to the Combined Faculty of of Mathematics, Engineering and Natural Sciences of Heidelberg University, Ger Opens in a new window — https://archiv.ub.uni-heidelberg.de/volltextserver/37647/1/Heidelberg_University_PhD_Thesis__Marco_Alban.pdf
- researchgate.net Lisa KEWLEY | Australian National University, Canberra | ANU | Research School of Astronomy & Astrophysics - ResearchGate Opens in a new window — https://www.researchgate.net/profile/Lisa-Kewley
- scilit.com Cosmic–climatic futures: interstellar objects, solar variability, and planetary consciousness (2027–2032) | Scilit Opens in a new window — https://www.scilit.com/publications/e65ca4f33064aa96e616f0b18be181fe
- hosting.astro.cornell.edu Fast Radio Bursts: An Extragalactic Enigma - Home Cornell Astronomy Opens in a new window — https://hosting.astro.cornell.edu/~shami/psrintro/papers/CC19.frb-review-araa.pdf
- cosmology.lbl.gov Cosmology and astrophysics with the extragalactic light: background and fluctuations Opens in a new window — https://cosmology.lbl.gov/talks/SatoPolito_22.pdf
- mdpi-res.com New Discoveries in Astronomical Data - MDPI Opens in a new window — https://mdpi-res.com/bookfiles/book/11837/New_Discoveries_in_Astronomical_Data.pdf?v=1763657170
- academic.oup.com Electron temperature relations in low metallicity, diffuse, and extraplanar gas of starburst galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/543/2/1322/8247990
- academic.oup.com Quasar Sightline and Galaxy Evolution (QSAGE) – III. The mass–metallicity and fundamental metallicity relation of z ≈ 2.2 galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/527/3/7891/7459361
- oamonitor.ireland.openaire.eu A radiation transfer model for the Milky Way: I. Radiation fields and application to high-energy astrophysics - National Open Access Monitor, Ireland Opens in a new window — https://oamonitor.ireland.openaire.eu/rpo/dcu/search/publication?pid=10.1093%2Fmnras%2Fstx1282
- osti.gov Physical Drivers of Emission-line Diversity of SDSS Seyfert 2s and LINERs after Removal of Contributions from Star Formation (Journal Article) - OSTI Opens in a new window — https://www.osti.gov/pages/biblio/1983183
- eprints.soton.ac.uk arXiv:2410.12198v2 [astro-ph.GA] 13 Mar 2025 - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/501056/1/2410.12198v2.pdf
- scholar.google.com ‪Lisa Kewley‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=XYbseF0AAAAJ&hl=en
- oamonitor.ireland.openaire.eu Chemical abundances in Seyfert galaxies – VI. Empirical Opens in a new window — https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.1093%2Fmnras%2Fstab2166
- arxiv.org Through the fog: a complementary optical galaxy classification scheme for 'intermediate' redshifts - arXiv Opens in a new window — https://arxiv.org/html/2507.17529v1
- cambridge.org Diffuse Ionised Gas in Edge-on Galaxies | Publications of the Astronomical Society of Australia - Cambridge University Press & Assessment Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/diffuse-ionised-gas-in-edge-on-galaxies/1D6E76EFB23008509F94278AF94E8872
- annualreviews.org Annual Review of Astronomy and Astrophysics - Volume 57, 2019 Opens in a new window — https://www.annualreviews.org/content/journals/astro/57/1
- researchgate.net TEMPLATES: Direct Abundance Constraints for Two Lensed Lyman-break Galaxies Opens in a new window — https://www.researchgate.net/publication/385537277_TEMPLATES_Direct_Abundance_Constraints_for_Two_Lensed_Lyman-break_Galaxies
- aas.org Get Your Annual Review of Astronomy & Astrophysics for 2019 Opens in a new window — https://aas.org/posts/news/2019/09/get-your-annual-review-astronomy-astrophysics-2019
- researchgate.net Theoretical relationship between the [S II] λ6717/λ6731 ratio and the... | Download Scientific Diagram - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Theoretical-relationship-between-the-S-IIl6717-l6731-ratio-and-the-ISM-pressure-left_fig12_334553094
- arxiv.org Metallicity Gradients in Modern Cosmological Simulations I: Tension Between Smooth Stellar Feedback Models and Observations - arXiv Opens in a new window — https://arxiv.org/html/2503.03804v2
- ricerca.sns.it GA-NIFS: the interplay between merger, star formation, and chemical enrichment in MACS1149-JD1 at z Opens in a new window — https://ricerca.sns.it/retrieve/7792c188-8dad-4bd9-b4bf-4dcac47fc41b/stae1971.pdf
- nbi.ku.dk PhD Thesis Morphology and Spectroscopy of High- redshift Galaxies Opens in a new window — https://nbi.ku.dk/english/theses/phd-theses/meghana-killi/Meghana_Killi.pdf
- researchgate.net (PDF) Siena Galaxy Atlas 2020 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/372286231_Siena_Galaxy_Atlas_2020
- arxiv.org Toward Unbiased Abundance Measurements in Inhomogeneous H ii Regions - arXiv Opens in a new window — https://arxiv.org/html/2607.05295v1
- edoc.ub.uni-muenchen.de Constraints of galaxy evolution 1-2 billion years after the Big Bang Opens in a new window — https://edoc.ub.uni-muenchen.de/36328/6/Lee_Lilian_Lai_Yee.pdf
- arxiv.org Hunting Wandering 3<z<8 Black Holes: via Spatial Offsets in Ionization Ratio and Continuum Emission - arXiv Opens in a new window — https://arxiv.org/pdf/2606.30715
- astro.yale.edu A giant shell of ionized gas discovered near M82 with the Dragonfly Spectral Line Mapper pathfinder - Yale Astronomy Opens in a new window — http://www.astro.yale.edu/dokkum/outgoing/M82Shell_resubmit.pdf
- scholar.google.com.au ‪Lisa Kewley‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com.au/citations?user=XYbseF0AAAAJ&hl=th
- mdpi.com Spectral Analysis of Star-Forming Galaxies at z < 0.4 with FADO: Impact of Nebular Continuum on Galaxy Properties - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/11/9/285
- oamonitor.ireland.openaire.eu Does the fundamental metallicity relation evolve with redshift? – II. The evolution in normalization of the mass–metallicity relation - National Open Access Monitor, Ireland - OpenAIRE Opens in a new window — https://oamonitor.ireland.openaire.eu/rpo/ucd/search/publication?pid=10.1093%2Fmnras%2Fstae2587
- su.diva-portal.org Ionization, bubbles and winds in a starburst galaxy at Cosmic Noon - DiVA portal Opens in a new window — https://su.diva-portal.org/smash/get/diva2:2072473/FULLTEXT01.pdf
- researchgate.net David NICHOLLS | Post-doctoral fellow | BSc(Hons) (ANU) MSc (Saskatchewan) PhD (ANU) FAIP | Australian National University, Canberra | ANU | Research School of Astronomy & Astrophysics | Research profile - ResearchGate Opens in a new window — https://www.researchgate.net/profile/David-Nicholls
- assets-eu.researchsquare.com Evidence for an intermediate mass black hole in ... - Research Square Opens in a new window — https://assets-eu.researchsquare.com/files/rs-3891007/v1_covered_957e7108-4744-4f89-a3f4-1effd6d14006.pdf?c=1711602938
- researchgate.net Evidence for an intermediate mass black hole in a low-mass star-forming galaxy Opens in a new window — https://www.researchgate.net/publication/379369147_Evidence_for_an_intermediate_mass_black_hole_in_a_low-mass_star-forming_galaxy
- nu.to.infn.it Astronomy and Astrophysics - Neutrino Unbound - INFN Opens in a new window — https://www.nu.to.infn.it/Other_Astrophysics/
- arxiv.org The k-MENDEL sample of local analogs to reionization galaxies - arXiv Opens in a new window — https://arxiv.org/html/2604.09516
- cambridge.org Constraining the link between the 2175Å dust absorption feature and PAHs in Nearby Star-Forming Galaxies using Swift/UVOT and JWST/MIRI | Publications of the Astronomical Society of Australia Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/constraining-the-link-between-the-2175a-dust-absorption-feature-and-pahs-in-nearby-starforming-galaxies-using-swiftuvot-and-jwstmiri/4ED534E688F356FC64D9E83E03776233
- cambridge.org The MAGPI survey: Science goals, design, observing strategy, early results and theoretical framework | Publications of the Astronomical Society of Australia - Cambridge University Press & Assessment Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/magpi-survey-science-goals-design-observing-strategy-early-results-and-theoretical-framework/0142DEFBE605938952E8EABCD81BCDD1
- arxiv.org Targeting black holes from metal-poor progenitors with next-generation gravitational-wave detectors - arXiv Opens in a new window — https://arxiv.org/pdf/2606.03776
- mdpi.com Spectroscopic Observations and Emission-Line Diagnoses for H ii Regions in the Late-Type Spiral Galaxy NGC 2403 - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/11/8/280
- arxiv.org arXiv:1601.01698v1 [astro-ph.GA] 7 Jan 2016 Opens in a new window — https://arxiv.org/pdf/1601.01698
- science.nasa.gov The Galaxy Evolution Probe Concept Study ii - Participant Contribution Institution - NASA Science Opens in a new window — https://science.nasa.gov/wp-content/uploads/2023/04/GEP_Study_Rpt.pdf
- arxiv.org Compact Objects Merging with Stars as an Origin of Ultra-Long Gamma-Ray Bursts and Luminous Fast Blue Optical Transients - arXiv Opens in a new window — https://arxiv.org/html/2607.07819v1
- arxiv.org The k-MENDEL sample of local analogs to reionization galaxies - arXiv Opens in a new window — https://arxiv.org/html/2604.09516v1
- frontiersin.org The high energy X-ray probe: resolved X-ray populations in extragalactic environments - Frontiers Opens in a new window — https://www.frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2023.1293918/full
- mdpi.com The Past and Future of Mid-Infrared Studies of AGN - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/8/7/356
- researchgate.net A gas rich cosmic web revealed by partitioning the missing baryons - ResearchGate Opens in a new window — https://www.researchgate.net/publication/384364496_A_gas_rich_cosmic_web_revealed_by_partitioning_the_missing_baryons
- nbi.ku.dk Resolving the Properties of Dust and Stellar Populations of Nearby Galaxies with the Hubble Space Telescope - Niels Bohr Institutet Opens in a new window — https://nbi.ku.dk/english/theses/masters-theses/clara-gimnez-arteaga/Clara_Gimenez_Arteaga__Master_Thesis.pdf

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

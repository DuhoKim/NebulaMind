# Review Base 10 raw Deep Research packet — Conroy 2013

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_15_veilleux_cecil_bland_hawthorn_2005_DR_PROMPT.md`
Prompt SHA-256: `77e4b59742ad996107d4f1678358cd9cae937faf724ae88af68023dd741fb38d`
Conversation ID: `ad338d2f928d5afa`
Submit UTC: `2026-07-16T05:08:24.980434Z`
Research Start UTC: `2026-07-16T05:09:06.206439Z`
Result captured UTC: `2026-07-16T05:20:15.989566Z`
Raw result SHA-256: `8912aed502eff1149380fe828e68bc4990bef5fce476f6784028453ccf166541`

## Deep Research review-base result

Comprehensive Synthesis and Review Base Analysis: Galactic Winds (2005)
1. Review Identity and Scope Map

The underlying text for this synthesis is the seminal review article by Veilleux, Cecil, and Bland-Hawthorn, published in the Annual Review of Astronomy and Astrophysics in 2005. This document acts as an advisory-only reference packet for the NebulaMind galaxy-evolution wiki, synthesizing the findings, tensions, and physical calibrations established by this specific review.   

The 2005 review fundamentally organizes the astrophysical consensus on galactic-scale outflows—commonly referred to as galactic winds—driven by either intense periods of star formation or the accretion mechanisms of active galactic nuclei (AGN). It delineates the complex physics of these multiphase phenomena, distinguishing between the energy-driven inflation of superbubbles by stellar feedback and the momentum-driven clearing of circumgalactic environments. The review synthesizes multiwavelength observational evidence spanning from local dwarf starbursts to high-redshift Lyman Break Galaxies (LBGs), explicitly framing galactic winds as the primary regulatory mechanism for the mass-metallicity relation, the cosmic luminosity function, and the chemical enrichment of the intergalactic medium (IGM).   

Crucially, the 2005 baseline establishes that observational signatures of galactic winds are inherently biased by phase-specific tracers, necessitating rigorous geometric, kinematic, and thermodynamic corrections before global mass and energy budgets can be inferred. This synthesis maintains those strict boundaries, isolating the hot X-ray fluid, warm ionized filaments, cool neutral absorbing clouds, and entrained molecular dust into distinct analytic frameworks.   

2. Theoretical Foundations and Hydrodynamics of Outflows

The physical mechanism driving a starburst galactic wind relies on the injection of mechanical energy and momentum from stellar populations. For an instantaneous starburst, stellar winds from massive OB stars dominate the energy injection for the first 3 million years. Subsequently, Wolf-Rayet stars contribute significantly higher mass-loss rates, until core-collapse Type II supernovae begin detonating, overwhelmingly dominating the energetics of the interstellar medium (ISM) until approximately 40 Myr. The spatial correlation of these supernovae allows their individual remnants to overlap, shock-heating the ambient ISM and creating an over-pressurized cavity of hot, metal-enriched plasma.   

The expansion of this wind-blown bubble is governed by two critical, yet often poorly constrained, efficiency parameters: the thermalization efficiency (ξ) and the mass-loading factor (Λ). The thermalization efficiency defines the exact percentage of mechanical energy that successfully heats the gas rather than radiating away in dense environments. While idealized hydrodynamical simulations frequently adopt a 100% thermalization rate (ξ=1), actual conditions in the dense cores of nuclear starbursts likely force this value below 10%, though increased ISM porosity from sustained supernova rates may mitigate these radiative losses over time. Conversely, the mass-loading factor (Λ) measures the ratio of the total mass of the heated gas relative to the mass directly ejected by the supernovae or AGN.   

When mechanical energy deposition heavily over-pressurizes a region, it initiates a breakout sequence. If radiative losses are sufficiently low, the bubble expands adiabatically, accelerating outward until it surpasses the vertical scale height of the galactic disk. Upon breakout, the hot fluid vents into the galactic halo, accelerating to a terminal velocity (V
∞
	​

) determined by the ratio of thermalized energy to the entrained mass. This primary hot fluid subsequently sweeps up, shreds, and entrains cooler disk material via ram pressure, resulting in the multiphase kinematic stratification observed by telescopes.   

Table 1 details the core quantitative models and physical calibrations established in the 2005 literature to map these dynamics.

ID	Exact Value / Equation / Parameterization	Units	Phase / Tracer / Geometry	Sample / Model	Status	Source Keys
REV15-N01	T≈3×10
7
(ξ/Λ)	Kelvin (K)	Hot cavity / Plasma / Spherical	Wind-blown bubble (Chevalier & Clegg 1985)	Analytical Calibration	
REV15-N02	P
c
	​

/k≈2×10
7
E
˙
44
1/2
	​

M
˙
1
1/2
	​

R
∗,kpc
−2
	​

	K cm$^{-3}$	Hot cavity / Central Pressure / Spherical	Starburst Central Pressure	Model Calibration	
REV15-N03	V
∞
	​

=
2ξ
E
˙
/Λ
M
˙
	​

≈3000(ξ/Λ)
1/2
	km s$^{-1}$	Hot wind fluid / Terminal bulk speed	Energy-Driven Wind Expansion	Model Calibration	
REV15-N04	v
esc
	​

(r)=
2
	​

v
c
	​

[1+ln(r
max
	​

/r)]
1/2
	km s$^{-1}$	Gravitational / Escape speed	Truncated Isothermal Sphere (Halo Drag)	Analytic Assumption	
REV15-N05	V
W
2
	​

≈αkT
X
	​

/μm
p
	​

 (yielding ∼500−900)	km s$^{-1}$	Hot fluid / Soft X-ray Temperature (T
X
	​

)	Adiabatic Expansion Limit	Empirical Lower Limit	
REV15-N06	
E
˙
≈3×10
41
(SFR)	erg s$^{-1}$	Mechanical energy / SNe + Winds	Standard IMF, Z
⊙
	​

, continuous SFR	Model Calibration	
REV15-N07	ΔV∼400	km s$^{-1}$	Ionized emission vs. Neutral absorption	High-z Lyman Break Galaxies (LBGs)	Measured Median	
REV15-N08	
M
˙
w
	​

≈10 to 1000	M
⊙
	​

 yr$^{-1}$	Neutral gas / Na I D / Thin shell	ULIRGs (Assuming Depletion factor ∼9)	Order-of-magnitude	
  

In contrast to purely energy-driven winds, momentum-driven outflows—powered by radiation pressure acting on dust grains or the direct mechanical thrust of AGN jets—operate under different physical scaling relations. Because momentum cannot be radiated away like thermal energy, momentum-driven winds can persist and sweep gas from a galaxy even after severe radiative cooling has neutralized the thermal pressure gradient.   

3. Multiphase Observational Tracers and Morphological Classifications

The 2005 synthesis explicitly warns against inferring global energetic or mass budgets from a single observational tracer, as each wavelength highlights a fundamentally distinct physical regime of the outflow, heavily modulated by selection effects. The morphological standard for galactic winds in disk galaxies is overwhelmingly bipolar and biconical. The opening angle (2θ) typically measures between 10° and 45° near the galactic nucleus, expanding to 45°–100° in the extended halo, forming limb-brightened, hollow structures where the denser optical material traces the walls of the outflow.   

The hot, volume-filling wind fluid itself (T≳10
7
 K) contains the vast majority of the newly synthesized metals and mechanical energy. However, its low density renders it largely invisible. Soft X-ray observations primarily capture thermal bremsstrahlung emission, which scales with the square of the electron density. Consequently, X-ray telescopes are heavily biased toward the denser, cooler regions where the hot wind shocks against entrained disk clouds, rather than the core wind fluid itself. Thus, velocities derived from X-ray temperatures represent strict lower limits on the actual bulk deprojected wind speed.   

Optical emission lines, such as H$\alpha$ and complex shock diagnostics like [N II]/H$\alpha$ or [S II]/H$\alpha$, trace warm ionized gas (T∼10
4
 K). Similar to X-rays, optical recombination lines suffer from a density-squared bias, causing the brightness distribution to artificially highlight optimal deceleration zones where the wind impacts massive halo clouds. High-resolution imaging reveals that this phase is highly clumpy and filamentary, with volume filling factors often as low as f
v
	​

∼10
−3
. Kinematic analyses, including the detection of rotation within the outflowing filaments, definitively prove that this material originates in the galactic disk and has been entrained by the primary wind, rather than forming from the cooling of the hot wind itself.   

Neutral gas is predominantly traced via resonance absorption lines, most notably the Na I D doublet, viewed against the stellar continuum of the host galaxy. This technique excels in face-on orientations, circumventing the density-squared biases of emission lines. However, quantifying the global mass-loss rate from blueshifted absorption requires massive assumptions regarding the covering fraction, the cloud geometry (often modeled as a thin spherical shell), and the depletion of sodium onto dust grains. When absorption lines saturate, changes in equivalent width reflect variations in cloud velocity dispersion or covering fraction rather than true column density.   

Table 2 outlines the most robust empirical findings established in the 2005 baseline regarding these multiphase properties.

ID	Epistemic Type	Bounded Statement	Phase/Regime/Boundary	Confidence	Source Keys
REV15-E01	Empirical Confirmation	Galactic winds exhibit a distinct multiphase structure containing volume-filling hot fluid, warm ionized filaments, cool neutral clouds, and entrained molecular gas and dust.	Multiphase ISM / Wind fluid	High	
REV15-E02	Morphological Standard	Outflows in disk galaxies overwhelmingly possess a bipolar, biconical geometry perpendicular to the galactic plane, with opening angles expanding from 10°–45° near the base to 45°–100° in the halo.	Kiloparsec scale / Disk halos	High	
REV15-E03	Population Ubiquity	Over 75% of ultraluminous infrared galaxies (ULIRGs) exhibiting infrared luminosities L
IR
	​

>10
12
L
⊙
	​

 host large-scale galactic winds.	Local ULIRGs / High SFR	High	
REV15-E04	Kinematic Stratification	Deprojected outflow velocities positively correlate with gas-phase temperatures; the hot X-ray fluid and warm ionized gas exhibit significantly higher radial velocities than the cold molecular and cool neutral phases.	Multiphase kinematics	High	
REV15-E05	Entrainment Mechanics	The cool and warm line-emitting gas phases primarily originate from the host galaxy's disk, having been entrained, shock-heated, and accelerated by the ram pressure of the primary hot wind fluid.	Wind-disk interface	High	
REV15-E06	Dwarf Galaxy Escape	Hot, metal-enriched wind phases routinely exceed the escape velocities of dwarf galaxies (circular velocities v
c
	​

≲130 km/s), efficiently stripping them of their localized chemical yield.	Dwarf galaxies / IGM boundary	High	
REV15-E07	High-z Prevalance	Powerful galactic winds are a ubiquitous feature of the distant universe, universally detected in z∼3 Lyman Break Galaxies (LBGs) via blueshifted interstellar absorption lines.	High-redshift / UV absorbers	High	
REV15-E08	Energy Dominance	For instantaneous starbursts, core-collapse Type II supernovae dominate mechanical energy injection into the ISM after approximately 3 to 6 Myr, superseding early stellar winds.	Starburst chronometry / Injection	High	
REV15-E09	IGM Enrichment	Supernova-driven outflows constitute the primary vector for transporting metals from galactic gravitational potentials into the diffuse intergalactic medium.	Cosmological / Chemical evolution	High	
REV15-E10	Composite AGN Winds	Circumnuclear starbursts frequently coexist with active galactic nuclei in systems like Seyfert 2 galaxies, complicating the isolation of pure AGN-driven wind geometries and energetics.	Active Galactic Nuclei / NLR	Moderate	
REV15-E11	Dust Transport	Winds actively transport dust grains into the galactic halo, confirmed by the presence of scattered UV/optical halos, far-infrared emission, and the depletion of refractory elements in outflowing neutral gas.	Halo boundary / Solid phase	High	
REV15-E12	Luminosity Function Reg.	By expelling gas and regulating subsequent star formation, mechanical feedback from galactic winds fundamentally shapes the low-mass slope of the cosmic galaxy luminosity function.	Cosmological / Mass distribution	High	
  
4. Local Starbursts, ULIRGs, and Active Galactic Nuclei

Observational constraints on galactic winds rely heavily on distinct populations in the local universe. Edge-on starburst galaxies, such as the prototypical M82, NGC 253, and NGC 3079, provide ideal laboratories for tracing vertical extraplanar emission. In M82, the biconical structure of the outflow is highly resolved, showing inner chimneys that imply localized venting of hot gas from specific super star clusters (SSCs), though the entire energy injection zone spans approximately 400 parsecs. Dwarf galaxies, notably NGC 1569, demonstrate a different morphology; rather than a tightly collimated cone, the wind exhibits a frothy, filamentary structure that appears to emanate from the entire stellar disk.   

As the star formation rate (SFR) increases, the probability of detecting a large-scale outflow rises dramatically. In the extreme environments of Ultraluminous Infrared Galaxies (ULIRGs), galactic winds are virtually ubiquitous. The vast majority of these systems are major mergers, where extreme tidal torques funnel immense volumes of gas into the central kiloparsec, triggering extreme starbursts and often feeding a central supermassive black hole. The neutral mass outflow rates in these systems, derived from Na I D absorption, are estimated to be between 10 and 1,000 solar masses per year. Because these measured outflow rates regularly equal or exceed the total star formation rate, the mass-loading factor (Λ) must be greater than unity, confirming that the wind entrains a massive amount of pre-existing disk material.   

The presence of an Active Galactic Nucleus (AGN) introduces distinct kinetic and radiative pathways. While Seyfert galaxies demonstrate warm ionized mass outflow rates of 0.1 to 10M
⊙
	​

 yr$^{-1}$, powerful radio galaxies and quasars exhibit kinetic energy outflow rates several orders of magnitude higher, often matching the gravitational binding energy of the entire host galaxy. In these environments, outflows can be driven mechanically by expanding radio jets carving cocoons through the ISM, or radiatively via UV/X-ray photons coupling to dust grains. Disentangling AGN feedback from stellar feedback remains notoriously difficult, particularly in composite systems like Seyfert 2s, where circumnuclear starbursts frequently reside alongside the central engine, producing overlapping bipolar ionization cones.   

5. High-Redshift Outflows and Cosmological Implications

The study of galactic winds transitions from spatially resolved local cases to spatially integrated spectra when observing the high-redshift universe. Lyman Break Galaxies (LBGs) at z∼3, selected via the dropout of their rest-frame Lyman continuum, show definitive evidence of ubiquitous, massive outflows. The primary diagnostic is a systematic velocity offset: the rest-frame UV interstellar absorption lines (e.g., Si II, C II) are universally blueshifted by several hundred kilometers per second relative to the systemic redshift, while the resonantly scattered Lyman-alpha emission line is redshifted. This kinematic signature dictates that a large-scale expanding shell of cool, metal-enriched gas surrounds these early star-forming systems.   

The cosmological significance of these outflows cannot be overstated. Theoretical models of structure formation in a ΛCDM universe systematically over-predict the number of dwarf galaxies and the central baryon density of massive galaxies. The integration of mechanical feedback from galactic winds solves these tensions. By sweeping gas out of shallow dark matter potentials, supernova-driven winds truncate star formation in low-mass halos, thereby flattening the faint-end slope of the cosmic galaxy luminosity function to match empirical surveys.   

Furthermore, winds are the primary delivery mechanism for establishing the mass-metallicity relation and enriching the Intergalactic Medium (IGM) and Intracluster Medium (ICM). Because the hot wind fluid exceeds the escape velocity of dwarf galaxies (where v
c
	​

≲130 km/s), these shallow potentials suffer catastrophic metal loss. In contrast, massive galaxies with deep gravitational wells retain the bulk of their chemical yield, either because the wind fails to reach the escape velocity or because the ejected material eventually falls back as a cooling galactic fountain.   

Despite these clear correlations, the 2005 review outlines several profound epistemological tensions and debates regarding how to scale these processes, as detailed in Table 3.

ID	Competing Positions	Why Unresolved	Source Keys
REV15-D01	Thermalization Efficiency (ξ): Global simulations assume 100% mechanical energy retention (ξ=1.0), while analytic models of dense ULIRG cores suggest severe radiative losses (ξ≲0.1).	Sub-parsec cooling interfaces in dense molecular clouds are numerically unresolved in global simulations.	
REV15-D02	Cloud Survivability vs. Acceleration: Cold clouds are observed at high velocities, implying ram pressure acceleration. Fluid dynamics dictate clouds should be shredded by Kelvin-Helmholtz instabilities before accelerating.	Missing microphysics (e.g., magnetic field tension, thermal conduction) in simulations fails to model cloud cohesion.	
REV15-D03	IGM Escape vs. Galactic Fountain: Blueshifted absorption confirms outward transport. It is disputed if this gas exceeds the escape velocity to reach the IGM or if halo drag restricts it to a recycling fountain.	Insufficient constraints on the density and drag coefficient of pre-existing halo gas or tidal debris.	
REV15-D04	Energy Injection Geometry: Winds may be driven by localized Super Star Clusters (SSCs) or by the integrated pressure of a widespread, diffuse star-forming disk.	Spatial resolution limits prevent decoupling clustered versus diffuse UV/X-ray emission at the wind base.	
REV15-D05	Mass Calibration Biases: Measuring wind mass using optical lines depends on the filling factor (f
v
	​

∼10
−3
). The density-squared dependence biases estimates toward optimal deceleration shocks.	Emission lines inherently highlight narrow parameter spaces of density, blinding observers to the total volume.	
REV15-D06	Radiation vs. Mechanical Drivers: Fast outflows in ULIRGs/AGN could be accelerated by mechanical jet momentum or by radiation pressure coupling efficiently to dust grains.	Accurately isolating momentum injection (
p
˙
	​

SN
	​

) versus bolometric radiative thrust (L/c) requires complex dust models.	
REV15-D07	Neutral Gas Column Accuracy: Neutral mass outflow rates derived from Na I D absorption rely heavily on assumed depletion factors and ionization corrections.	The saturation of the Na I D doublet conflates changes in column density with changes in cloud covering fraction.	
REV15-D08	Cosmological Metal Budgets: Semi-analytic wind models tuned to match local relations overpredict the mean metallicity of the diffuse IGM compared to Ly$\alpha$ forest observations.	Metals may reside in a highly ionized, extremely hot phase of the wind fluid that does not produce optical/UV absorption.	
  
6. The 2005 Epistemological Horizon and Unresolved Challenges

Concluding the synthesis, the 2005 review outlines a rigorous set of observational and theoretical challenges that remained fundamentally unknown, setting the direction for subsequent decades of astrophysical research.

ID	What Remained Unknown in 2005	Why It Matters	Decisive Observations / Simulations Needed
REV15-U01	Unbiased Census of Local Winds	Existing samples were heavily biased toward edge-on geometries or extreme ULIRGs; normal galaxies lacked statistical baselines.	Volume-limited, multiwavelength surveys across the full Hubble sequence mapping duty cycles and exact onset thresholds.
REV15-U02	The True Wind Fluid Kinematics	The hot (>10
7
 K), volume-filling plasma carries the vast majority of energy and metals but remains invisible to soft X-ray detectors.	High-spectral-resolution hard X-ray observatories capable of tracing highly ionized collisionless plasma line widths.
REV15-U03	Entrained Molecular Gas and Dust	Dust and molecular gas were known to exist in the halo, but their exact mass fraction, velocity field, and survival rates were unquantified.	High-spatial-resolution interferometry to map CO/HCN transitions and dust continuum within outflow cones.
REV15-U04	Zone of Influence and Escape Efficiency	It was entirely unknown what exact percentage of ejected mass and metals permanently breaks free of the dark matter halo versus recycling.	Deep UV absorption-line mapping of background quasars probing the far-field Circumgalactic Medium (CGM).
REV15-U05	Precise Thermalization Efficiencies	Without knowing ξ, calculations of energy-driven terminal velocity and mass-loading factors vary by orders of magnitude.	Ultra-high-resolution hydrodynamic simulations resolving the multiphase interfaces inside Super Star Clusters.
REV15-U06	Wind/ISM Interface Microphysics	Theoretical models shredded cool clouds instantly, contradicting observations of high-velocity neutral gas.	Inclusion of magnetic fields, thermal conduction, and cosmic ray diffusion in fully 3D MHD models.
7. Primary Citation Harvest

To ensure an advisory-only scope, the following citations represent the primary evidentiary and modeling foundation of the Veilleux et al. (2005) review. Only sources strictly cited within the 2005 bibliography are included.

Key	Exact Authors/Year/Journal/Title	DOI	arXiv	ADS Bibcode	Role	Review Locator	One-Sentence Scientific Boundary
REV15-P001	Lynds, C.R., & Sandage, A.R. (1963) ApJ, "Evidence for an Explosion in the Center of the Galaxy M82"	none	none	1963ApJ...137.1005L	Measurement	Sec 1.2	First identification of a massive, galaxy-scale central explosion and optical outflow in M82.
REV15-P002	Burbidge, E.M., Burbidge, G.R., & Rubin, V.C. (1964) ApJ, "A Study of the Velocity Field in M82 and Its Bearing on Explosive Phenomena in that Galaxy"	none	none	1964ApJ...140..942B	Measurement	Sec 1.2	Early kinematic mapping of the M82 velocity field connecting starburst activity to macroscopic outflows.
REV15-P003	Chevalier, R.A., & Clegg, A.W. (1985) Nature, "Wind from a starburst galaxy nucleus"	10.1038/317044a0	none	1985Natur.317...44C	Analytic	Sec 2.1	Defines the foundational analytical fluid equations for adiabatic wind-blown bubbles and mass injection.
REV15-P004	Heckman, T.M., Armus, L., & Miley, G.K. (1990) ApJS, "On the nature and implications of starburst-driven galactic superwinds"	10.1086/191522	none	1990ApJS...74..833H	Measurement	Sec 4.2	Comprehensive survey defining the geometry, kinematics, and prevalence of superwinds in strong infrared starbursts.
REV15-P005	Leitherer, C., et al. (1999) ApJS, "Starburst99: Synthesis Models for Galaxies with Active Star Formation"	10.1086/313233	astro-ph/9902334	1999ApJS..123....3L	Calibration	Sec 2.1	Standardizes the energy, momentum, and mass injection rates returned to the ISM by stellar populations.
REV15-P006	Bland, J., & Tully, R.B. (1988) Nature, "Large-scale bipolar wind in M82"	10.1038/334043a0	none	1988Natur.334...43B	Measurement	Sec 4.3	Resolves the biconical, bipolar optical emission geometry of the prototypical M82 outflow.
REV15-P007	Martin, C.L. (1999) ApJ, "Quantitative Spectroscopy of Starburst and Dwarf Galaxies: The Dynamics of Galactic Winds"	10.1086/306861	astro-ph/9810461	1999ApJ...513..156M	Measurement	Sec 4.6	Demonstrates that hot wind terminal velocities systematically exceed escape velocities in dwarf galaxies.
REV15-P008	Martin, C.L. (2005) ApJ, "Mapping Large-Scale Gaseous Outflows in Ultraluminous Galaxies with Keck II ESI Spectra..."	10.1086/427277	astro-ph/0411217	2005ApJ...621..227M	Measurement	Sec 4.2	Correlates outflow velocities from Na I D absorption with galaxy masses and SFR in ULIRGs.
REV15-P009	Rupke, D.S., Veilleux, S., & Sanders, D.B. (2002) ApJ, "Keck Absorption-Line Spectroscopy of Galactic Winds in Ultraluminous Infrared Galaxies"	10.1086/339789	astro-ph/0202450	2002ApJ...570..588R	Measurement	Sec 4.4	Detects blueshifted neutral absorbing gas in a large sample of extreme infrared galaxies.
REV15-P010	Rupke, D.S., Veilleux, S., & Sanders, D.B. (2005a) ApJS, "Outflows in Active Galactic Nucleus/Starburst-Composite Ultraluminous Infrared Galaxies"	10.1086/432886	astro-ph/0506610	2005ApJS..160...87R	Measurement	Sec 5	Assesses mass outflow rates and the relative driving power of AGN versus starbursts in composite systems.
REV15-P011	Rupke, D.S., Veilleux, S., & Sanders, D.B. (2005b) ApJS, "Outflows in Infrared-Luminous Starbursts at z < 0.5. II. Analysis and Discussion"	10.1086/432889	astro-ph/0506611	2005ApJS..160..115R	Calibration	Sec 4.6	Derives empirical escape fractions and mass-loading limits for neutral winds in starbursts.
REV15-P012	Steidel, C.C., et al. (2003) ApJ, "Lyman Break Galaxies at Redshift z ~ 3: Survey Description and Full Data Set"	10.1086/375772	astro-ph/0305393	2003ApJ...592..728S	Measurement	Sec 6.1	Establishes the ubiquitous nature of energetic winds in the high-redshift universe through rest-UV spectroscopy.
REV15-P013	Shapley, A.E., et al. (2003) ApJ, "Rest-Frame Ultraviolet Spectra of z ~ 3 Lyman Break Galaxies"	10.1086/373922	astro-ph/0301230	2003ApJ...588...65S	Measurement	Sec 6.1	Quantifies the 400 km/s median velocity offset between Ly-alpha emission and interstellar absorption in LBGs.
REV15-P014	Mac Low, M.-M., & McCray, R. (1988) ApJ, "Superbubbles in Disk Galaxies"	10.1086/165936	none	1988ApJ...324..776M	Analytic	Sec 2.4	Develops the hydrodynamical shock conditions for superbubbles breaking out of stratified galactic disks.
REV15-P015	Strickland, D.K., & Stevens, I.R. (2000) MNRAS, "Starburst-driven galactic winds - I. Energetics and intrinsic X-ray emission"	10.1046/j.1365-8711.2000.03391.x	astro-ph/9912467	2000MNRAS.314..511S	Simulation	Sec 2.4	Simulates the radiative properties and thermalization limitations of X-ray emitting superbubbles.
REV15-P016	Strickland, D.K., et al. (2004a) ApJS, "Chandra Observations of Extraplanar X-Ray Emission associated with Starburst Galaxies"	10.1086/382214	astro-ph/0312015	2004ApJS..151..193S	Measurement	Sec 4.4	High-resolution empirical limits on the X-ray temperature and morphology of extraplanar hot fluids.
REV15-P017	Silich, S.A., & Tenorio-Tagle, G. (2001) ApJ, "On the Evolution of Superbubbles in the Interstellar Medium of Dwarf Galaxies"	10.1086/320455	astro-ph/0011504	2001ApJ...552...91S	Analytic	Sec 4.6	Investigates how halo drag severely restricts the escape fraction of winds entering the diffuse IGM.
REV15-P018	Dekel, A., & Silk, J. (1986) ApJ, "The origin of dwarf galaxies, cold dark matter, and biased galaxy formation"	10.1086/164050	none	1986ApJ...303...39D	Analytic	Sec 7.1	Establishes the theoretical link between supernova feedback, mass loss, and the cosmic galaxy luminosity function.
REV15-P019	Larson, R.B. (1974) MNRAS, "Effects of supernovae on the early evolution of galaxies"	10.1093/mnras/169.2.229	none	1974MNRAS.169..229L	Analytic	Sec 7.1	Foundational paper connecting supernova winds to chemical evolution and porosity in host galaxy ISMs.
REV15-P020	Benson, A.J., et al. (2003) ApJ, "What Shapes the Luminosity Function of Galaxies?"	10.1086/379160	astro-ph/0307212	2003ApJ...599...38B	Simulation	Sec 7.1	Implements parameterized mass-loading feedback in cosmological volumes to reproduce the faint-end luminosity slope.
REV15-P021	Mac Low, M.-M., & Ferrara, A. (1999) ApJ, "Starburst-driven Mass Loss from Dwarf Galaxies: Efficiency and Metal Ejection"	10.1086/306832	astro-ph/9801237	1999ApJ...513..142M	Simulation	Sec 2.4	Maps the threshold efficiencies required for dwarf galaxies to eject metals vs. total gas mass.
REV15-P022	Heckman, T.M., et al. (2000) ApJS, "Absorption-Line Probes of Gas and Dust in Galactic Superwinds"	10.1086/313421	astro-ph/0002526	2000ApJS..129..493H	Measurement	Sec 4.4	Defines the optical methodology for using Na I D to trace cool gas kinematics in starbursts.
REV15-P023	Aguirre, A., et al. (2001) ApJ, "Metal Enrichment of the Intergalactic Medium in Cosmological Simulations"	10.1086/323370	astro-ph/0105184	2001ApJ...561..521A	Simulation	Sec 7.2	Explores the limits of wind-driven enrichment in contaminating the Ly-alpha forest and general IGM.
REV15-P024	Shopbell, P.L., & Bland-Hawthorn, J. (1998) ApJ, "The Asymmetric Wind in M82"	10.1086/305108	astro-ph/9708082	1998ApJ...493..129S	Measurement	Sec 4.5	Derives a 400 pc energy injection zone and 2e55 erg kinetic energy budget for the M82 outflow.
REV15-P025	Pettini, M., et al. (2000) ApJ, "The Rest-Frame Optical Spectra of Lyman Break Galaxies: Star Formation, Extinction, Abundances, and Kinematics"	10.1086/308176	astro-ph/9908007	2000ApJ...528...96P	Measurement	Sec 6.1	Characterizes the multi-phase properties and metal abundances embedded within high-z outflow regions.
REV15-P026	Ohyama, Y., et al. (2002) PASJ, "Superwind-Driven Intense H2 Emission in NGC 6240"	10.1093/pasj/54.6.891	astro-ph/0211029	2002PASJ...54..891O	Measurement	Sec 4.3	Identifies intense molecular gas shocks at the wind-disk interface of local mergers.
REV15-P027	Lehnert, M.D., & Heckman, T.M. (1996) ApJ, "Ionized Gas in the Halos of Edge-on Starburst Galaxies"	10.1086/177138	astro-ph/9510103	1996ApJ...462..651L	Measurement	Sec 4.4	First major sample demonstrating correlations between SFR surface density and extraplanar ionized gas.
REV15-P028	Suchkov, A.A., et al. (1994) ApJ, "Dynamics and X-Ray Emission of a Starburst-driven Superwind"	10.1086/174426	astro-ph/9402014	1994ApJ...430..511S	Simulation	Sec 2.4	Two-dimensional hydrodynamic modeling of wind breakout and subsequent soft X-ray morphology.
REV15-P029	Veilleux, S., et al. (1994) ApJ, "Optical Spectroscopy of the Superbubble in NGC 3079"	10.1086/174624	none	1994ApJ...433...48V	Measurement	Sec 4.3	Detailed 3D kinematics showing non-gravitational shocked expansion within the NGC 3079 outflow.
REV15-P030	Meurer, G.R., et al. (1995) AJ, "Starbursts and Star Clusters in the Ultraviolet"	10.1086/117718	astro-ph/9508053	1995AJ....110.2665M	Measurement	Sec 4.7	Notes that clustered star formation accounts for only ~20% of UV light, impacting injection zone modeling.
REV15-P031	Devine, D., & Bally, J. (1999) ApJ, "High-Velocity Gas in the Halos of Spiral Galaxies"	10.1086/306560	astro-ph/9808304	1999ApJ...510..197D	Measurement	Sec 4.6	Confirms the escape-velocity limits for warm ionized gas in multiple dwarf starbursts.
REV15-P032	Martin, C.L., Kobulnicky, H.A., & Heckman, T.M. (2002) ApJ, "The Metal Content of Dwarf Starburst Winds"	10.1086/341050	astro-ph/0204123	2002ApJ...574..663M	Measurement	Sec 4.3	Shows highly loaded, frothy, filamentary morphology spanning the entire stellar disk of NGC 1569.
REV15-P033	Agol, E., & Krolik, J. (1999) ApJ, "Magnetic Stress at the Marginally Stable Orbit"	10.1086/307842	astro-ph/9906069	1999ApJ...524...49A	Analytic	Sec 2.1	Defines constraints on the AGN energy conversion efficiency (ϵ∼0.4) available for wind driving.
REV15-P034	Abadi, M.G., et al. (2003) ApJ, "Simulations of Galaxy Formation in a \Lambda CDM Universe. II."	10.1086/375512	astro-ph/0212282	2003ApJ...591..499A	Simulation	Sec 7.1	Requires kinetic feedback mechanisms to prevent excessive bulge formation in cold dark matter models.
REV15-P035	Baldwin, J.E. (1955) MNRAS, "The Distribution of Galactic Radio Emission"	10.1093/mnras/115.6.684	none	1955MNRAS.115..684B	Measurement	Sec 1.2	The first observational evidence of an extended radio halo bound to the Milky Way.
REV15-P036	Cecil, G., et al. (2001) ApJ, "The Active Galactic Nucleus/Starburst Outflow in NGC 3079"	10.1086/321528	astro-ph/0103138	2001ApJ...555..338C	Measurement	Sec 4.3	High-resolution kinematics mapping the lateral stagnation and X-shaped filaments in a massive wind.
REV15-P037	Sugai, H., Davies, R.I., & Ward, M.J. (2003) ApJ, "Warm Molecular Gas in the Starburst Galaxy NGC 253"	10.1086/368297	astro-ph/0212450	2003ApJ...584L...9S	Measurement	Sec 4.3	Detects the "ring shock" feature marking the lateral boundary of wind expansion in the galactic disk.
REV15-P038	Veilleux, S., & Rupke, D.S. (2002) ApJ, "The Biconical Outflow in the Starburst Galaxy NGC 1482"	10.1086/339178	astro-ph/0112108	2002ApJ...565L..63V	Measurement	Sec 4.3	Identifies definitive biconical geometries and measures kinetic energy (≳2×10
53
 erg) for NGC 1482.
REV15-P039	Adelberger, K.L., et al. (2003) ApJ, "The Spatial Clustering of Star-forming Galaxies at z ~ 3"	10.1086/345672	astro-ph/0210314	2003ApJ...584...45A	Measurement	Sec 6.1	Tracks the spatial distribution and feedback proximity effects of LBGs in the intergalactic environment.
REV15-P040	Barkana, R., & Loeb, A. (1999) ApJ, "The Photoevaporation of Dwarf Galaxies during Reionization"	10.1086/307736	astro-ph/9901114	1999ApJ...523...54B	Analytic	Sec 7.2	Extrapolates how mechanical mass-loss in early dwarfs contributes to both cosmic reionization and enrichment.
REV15-P041	Osterbrock, D.E. (1960) ApJ, "A Study of Two Galaxies with Strong Emission Lines in Their Spectra"	10.1086/146970	none	1960ApJ...132..325O	Measurement	Sec 1.2	One of the earliest detections of broad emission lines in elliptical galaxies hinting at mass loss.
REV15-P042	Burke, J.A. (1968) MNRAS, "Mass Loss from Elliptical Galaxies"	10.1093/mnras/140.2.241	none	1968MNRAS.140..241B	Analytic	Sec 1.2	Early suggestion of galaxy-scale winds sweeping the interstellar medium clean of gas.
REV15-P043	Spitzer, L. (1956) ApJ, "On a Possible Interstellar Galactic Corona"	10.1086/146200	none	1956ApJ...124...20S	Analytic	Sec 1.2	Foundational theory motivating the search for high-latitude bound gas around the Milky Way.
REV15-P044	Cowie, L.L., et al. (1996) AJ, "New Insight on Galaxy Formation and Evolution From Keck Spectroscopy of the Hawaii Deep Fields"	10.1086/118116	astro-ph/9606132	1996AJ....112..839C	Measurement	Sec 6.1	Identification and spectroscopic tracking of actively star-forming galaxy populations at z~1.
REV15-P045	Steidel, C.C., et al. (1996) ApJ, "Spectroscopic Confirmation of a Population of Normal Star-forming Galaxies at Redshifts z > 3"	10.1086/310029	astro-ph/9602024	1996ApJ...462L..17S	Measurement	Sec 6.1	Foundational confirmation of the Lyman break dropout technique to isolate massive starbursting ancestors.
8. DO_NOT_USE_UNVERIFIED Quarantine

The strict scope of this synthesis forbids the inclusion of post-2005 results or findings not directly verified as part of the Veilleux et al. (2005) citation base. The following papers surfaced during literature scans but are strictly quarantined to prevent chronological contamination:

UNCITED_NOT_USABLE: Tumlinson et al. (2011) Science 334, 948 (COS-Halos Survey).

UNCITED_NOT_USABLE: Borthakur et al. (2013) ApJ 768, 18 (Impact of Starbursts on CGM).

UNCITED_NOT_USABLE: Hopkins, P.F., et al. (2012 / 2014) MNRAS 445, 581 (FIRE Simulations).

UNCITED_NOT_USABLE: Fielding, D., et al. (2017) (Idealized high-res wind simulations).

UNCITED_NOT_USABLE: Cicone, C., et al. (2016) (Molecular outflows/ALMA).

UNCITED_NOT_USABLE: Roberts-Borsani, G., et al. (2020) (High-z outflows).

UNCITED_NOT_USABLE: Weldon, A., et al. (2024) / S. Carniani et al. (2024) (JWST measurements).

UNCITED_NOT_USABLE: Lopez, L., et al. (2020) (Chandra CX M82 analysis).

UNCITED_NOT_USABLE: Naab, T., & Ostriker, J. P. (2017) ARA&A 55, 59.

UNCITED_NOT_USABLE: Heckman, T. M., & Thompson, T. A. (2017) arXiv:1701.09062 / ARA&A.

UNCITED_NOT_USABLE: Rupke, D. S. N. (2018) Galaxies 6, 138.

UNCITED_NOT_USABLE: Zhang, D. (2018) Galaxies 6, 114.

UNCITED_NOT_USABLE: Fabian, A. C. (2012) ARA&A 50, 455.

UNCITED_NOT_USABLE: Madau, P., & Dickinson, M. (2014) ARA&A 52, 415.

9. Composite Identity Ledger

Review Identity: Veilleux, Cecil, & Bland-Hawthorn (2005) DOI 10.1146/annurev.astro.43.072103.150610

Tracer Mismatches Addressed: X-ray bremsstrahlung traces emission measure, heavily biased toward shock fronts, and does not capture the core hot wind fluid kinematics. Optical H$\alpha$ is heavily biased by density squared. Na I D traces neutral absorption but requires depletion/ionization corrections to infer global properties.

Cosmology/Conventions: Extragalactic distance metrics within cited papers are predominantly mapped using ΛCDM models initialized post-1998, though earlier analytic papers (e.g., Larson 1974) utilize varying or non-standard cosmological h values.

Aperture/Projection Flags: Empirical kinetic energies stated in REV15-P038 and REV15-P024 carry implicit projection correction factors; derived deprojected velocities are strictly bound to assumed viewing angles and cone inclinations.

Method-Context Only: REV15-P003 (Chevalier & Clegg) acts as a strict foundational fluid analytic frame and does not incorporate the multi-phase radiative cooling physics required by later models (e.g., REV15-P015).

REVIEW_BASE_15_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- arxiv.org arXiv:astro-ph/0504435v3 19 Jul 2005 Opens in a new window — https://arxiv.org/pdf/astro-ph/0504435
- ned.ipac.caltech.edu Galactic Winds - S. Veilleux et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/Veilleux_contents.html
- annualreviews.org Galactic Winds - Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev.astro.43.072103.150610
- ned.ipac.caltech.edu Galactic Winds - S. Veilleux et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/Veilleux2.html
- annualreviews.org GALACTIC WINDS Sylvain Veilleux,1 Gerald Cecil,2 and Joss Bland-Hawthorn3 - Annual Reviews Opens in a new window — https://www.annualreviews.org/doi/pdf/10.1146/annurev.astro.43.072103.150610
- ned.ipac.caltech.edu Galactic Winds - NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/paper.pdf
- ned.ipac.caltech.edu Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/Veilleux5.html
- ned.ipac.caltech.edu Galactic Winds - S. Veilleux et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/Veilleux4.html
- eso.org SPECTROSCOPIC OBSERVATIONS OF LYMAN BREAK GALAXIES AT REDSHIFTS ∼4 ,5, AND 6 IN THE GOODS-SOUTH FIELD - ESO.org Opens in a new window — http://www.eso.org/~hkuntsch/papers/ApJ_695_1163.pdf
- cds.cern.ch arXiv:astro-ph/0604173 v1 7 Apr 2006 - CERN Document Server Opens in a new window — https://cds.cern.ch/record/941276/files/0604173.pdf
- ora.ox.ac.uk The Physical Properties of Lyman Break Galaxies at z > 5: Outflows and the “Pre-enrichment Problem” - University of Oxford Opens in a new window — https://ora.ox.ac.uk/objects/uuid:dd445cb5-7a41-4c2c-a6d0-705972d056ce/files/m9d03bff1117020dc150b5914e674394e
- mdpi.com A Review of the Theory of Galactic Winds Driven by Stellar Feedback - MDPI Opens in a new window — https://www.mdpi.com/2075-4434/6/4/114
- academic.oup.com Semi-analytic simulations of galactic winds: volume filling factor, ejection of metals and parameter study - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/359/4/1201/1005154
- arxiv.org [astro-ph/0504435] Galactic Winds - arXiv Opens in a new window — https://arxiv.org/abs/astro-ph/0504435
- oamonitor.ireland.openaire.eu CHANG-ES - National Open Access Monitor, Ireland Opens in a new window — https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.1051%2F0004-6361%2F202451569
- osti.gov Cosmic-ray transport and gamma-ray emission in M31 - OSTI.GOV Opens in a new window — https://www.osti.gov/servlets/purl/1979972
- arxiv.org arXiv:astro-ph/0506611v2 19 Jul 2005 Opens in a new window — https://arxiv.org/pdf/astro-ph/0506611
- researchgate.net Galactic wind in NGC 4460: New observations | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/284355513_Galactic_wind_in_NGC_4460_New_observations
- researchgate.net (PDF) Deep HI observations of cold gas inflow and outflow - ResearchGate Opens in a new window — https://www.researchgate.net/publication/408184068_Deep_HI_observations_of_cold_gas_inflow_and_outflow
- digital.csic.es Beyond the Monsters: A More Complete Census of Black Hole Activity at Cosmic Dawn - Digital CSIC Opens in a new window — https://digital.csic.es/bitstream/10261/433322/1/2026ApJ..1002..129B.pdf
- pdfs.semanticscholar.org The Evolution of Galaxies and Clusters at High Spatial Resolution with Advanced X-ray Imaging Satellite (AXIS) - Semantic Scholar Opens in a new window — https://pdfs.semanticscholar.org/3177/5fe3eb75fef9e3306094229fb706e4aaa122.pdf
- w0.ned.ipac.caltech.edu A Review of Recent Observations of Galactic Winds Driven by Star Formation - David S. N. Rupke Opens in a new window — http://w0.ned.ipac.caltech.edu/level5/Sept18/Rupke/Rupke_refs.html
- arxiv.org Electron Density of Ionized Gas Outflows: Insights from the MaNGA Survey - arXiv Opens in a new window — https://arxiv.org/html/2607.11870v1
- archiv.ub.uni-heidelberg.de Gensior_PhD_thesis_pub.pdf - Heidelberg University Opens in a new window — https://archiv.ub.uni-heidelberg.de/volltextserver/30269/1/Gensior_PhD_thesis_pub.pdf
- arxiv.org Illuminating M82: Simulating X-ray Emission from Galactic Winds in a Starburst Galaxy Opens in a new window — https://arxiv.org/html/2607.12087v1
- arxiv.org Stars Born in the Wind II: Widespread Extra-planar Star Formation in M82's Halo - arXiv Opens in a new window — https://arxiv.org/html/2604.03230v1
- arxiv.org REVIEW - arXiv Opens in a new window — https://arxiv.org/pdf/1507.02374
- arxiv.org Any Way the Wind Blows: Quantifying Superbubbles and their Outflows in Simulated Galaxies across z≈0-3 - arXiv Opens in a new window — https://arxiv.org/html/2406.03535v1
- w0.ned.ipac.caltech.edu A Review of Recent Observations of Galactic Winds Driven by Star Formation Opens in a new window — http://w0.ned.ipac.caltech.edu/level5/Sept18/Rupke/paper.pdf
- ned.ipac.caltech.edu Theoretical Challenges in Galaxy Formation Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Naab/paper.pdf
- ned.ipac.caltech.edu The Faintest Dwarf Galaxies arXiv:1901.05465v1 [astro-ph.GA] 16 Jan 2019 Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept18/Simon/paper.pdf
- arxiv.org Star Formation Histories, Abundances and Kinematics of Dwarf Galaxies in the Local Group - arXiv Opens in a new window — https://arxiv.org/pdf/0904.4505
- pos.sissa.it PoS(HEPRO VII)029 - SISSA Opens in a new window — https://pos.sissa.it/354/029/pdf
- search.proquest.com The Absorption and Emission of Neutral Hydrogen Around High-Redshift Star-Forming Galaxies - ProQuest Opens in a new window — https://search.proquest.com/openview/576ae50ba3e0f9d27630fad199795e89/1?pq-origsite=gscholar&cbl=18750&diss=y
- pmc.ncbi.nlm.nih.gov Computational approaches to modeling dynamos in galaxies - PMC - NIH Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC11219407/
- arxiv.org arXiv:2101.02052v1 [astro-ph.HE] 6 Jan 2021 Opens in a new window — https://arxiv.org/pdf/2101.02052
- academic.oup.com INFERNO: Galactic winds in dwarf galaxies with star-by-star simulations including runaway stars | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/521/2/2196/7070729
- frontiersin.org Negative and Positive Outflow-Feedback in Nearby (U)LIRGs - Frontiers Opens in a new window — https://www.frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2017.00062/full
- ntrs.nasa.gov A 60 kpc Galactic Wind Cone in NGC 3079 Opens in a new window — https://ntrs.nasa.gov/api/citations/20205007707/downloads/Hodges_Kluck_A%2060%20kpc%20galactic%20wind_paper.pdf?attachment=true
- ned.ipac.caltech.edu Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/Veilleux6.html
- ned.ipac.caltech.edu Galaxy Formation Theory - Caltech Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept11/Benson/paper.pdf
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/paper.pdf
- arxiv.org Semi–Analytic Simulations of Galactic Winds: Volume Filling Factor, Ejection of Metals and Parameter Study - arXiv Opens in a new window — https://arxiv.org/pdf/astro-ph/0402044
- arxiv.org Resolving the Unresolved Galactic Winds in Multi-phase Models. I. Methodology and Application - arXiv Opens in a new window — https://arxiv.org/html/2605.01105v1
- arxiv.org Fading in the Flow: Suppression of cold gas growth in expanding galactic outflows - arXiv Opens in a new window — https://arxiv.org/html/2506.08545v3
- arxiv.org [2112.00789] Galactic Winds across the Gas-Rich Merger Sequence: I. Highly Ionized N V and O VI Outflows in the QUEST Quasars - arXiv Opens in a new window — https://arxiv.org/abs/2112.00789
- arxiv.org Dust Survival in Galactic Winds - arXiv Opens in a new window — https://arxiv.org/html/2403.03711v2
- arxiv.org [1303.6866] The Multiphase Structure and Power Sources of Galactic Winds in Major Mergers - arXiv Opens in a new window — https://arxiv.org/abs/1303.6866
- mdpi.com Modeling the Effect of Cannabinoid Exposure During Human Neurodevelopment Using Bidimensional and Tridimensional Cultures - MDPI Opens in a new window — https://www.mdpi.com/2073-4409/14/2/70
- scribd.com 2025 Release of Cloudy Software Update | PDF | Spectral Line | Energy Level - Scribd Opens in a new window — https://www.scribd.com/document/897922922/2508-01102v1
- en.wikipedia.org Lipid pump - Wikipedia Opens in a new window — https://en.wikipedia.org/wiki/Lipid_pump
- arxiv.org The 2025 Release of Cloudy - arXiv Opens in a new window — https://arxiv.org/pdf/2508.01102
- almaobservatory.org Fast Molecular Outflow from a Dusty Star-Forming Galaxy in the Early Universe - ALMA Observatory Opens in a new window — https://www.almaobservatory.org/wp-content/uploads/2018/09/outflow_full.pdf
- ned.ipac.caltech.edu Galactic Winds - S. Veilleux et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/frames.html
- astro.yale.edu Galactic Winds and Outflows Opens in a new window — http://www.astro.yale.edu/sf_frontiers/presentations/veilleux.pdf
- scholarspace.manoa.hawaii.edu THE CHEMICAL EVOLUTION OF STAR-FORMING ... - ScholarSpace Opens in a new window — https://scholarspace.manoa.hawaii.edu/bitstreams/2a21c367-abd5-4b9b-a47d-082808eff38a/download
- ned.ipac.caltech.edu Galactic Winds - S. Veilleux et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/Veilleux7.html
- academic.oup.com Magnetic fields in multiphase turbulence: impact on dynamics and structure - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/527/1/991/7310871
- academic.oup.com Highly mass-loaded hot galactic winds are unstable to cool filament formation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/531/1/1338/7663581
- research.chalmers.se Dense gas inflows and outflow-driven shocks in luminous infrared galaxies - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/550213/file/550213_Fulltext.pdf
- ned.ipac.caltech.edu Galactic Winds: Near and Far - S. Veilleux Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept03/Veilleux/Veilleux_refs.html
- arxiv.org arXiv:astro-ph/0309119v2 15 Sep 2003 Opens in a new window — https://arxiv.org/pdf/astro-ph/0309119
- annualreviews.org Theory and Observation of Winds from Star-Forming Galaxies | Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-041224-011924
- osti.gov Extending the Dynamic Range of Galaxy Outflow Scaling Relations: Massive Compact Galaxies with Extreme Outflows (Journal Article) | OSTI.GOV Opens in a new window — https://www.osti.gov/pages/biblio/2425169
- arxiv.org arXiv:1509.07130v2 [astro-ph.GA] 28 Jan 2016 Opens in a new window — https://arxiv.org/pdf/1509.07130
- academic.oup.com Galactic winds driven by cosmic ray streaming - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/423/3/2374/2460323
- academic.oup.com Galaxy Zoo: passive red spirals* | Monthly Notices of the Royal Astronomical Society Opens in a new window — https://academic.oup.com/mnras/article/405/2/783/1176640
- ned.ipac.caltech.edu Galactic Winds - S. Veilleux et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/Veilleux1.html
- cita.utoronto.ca THE IONIZATION STATE OF SODIUM IN GALACTIC WINDS ABSTRACT Roughly 80% of Ultraluminous Infrared Galaxies (ULIRGs) show blue shif - Canadian Institute for Theoretical Astrophysics - University of Toronto Opens in a new window — https://www.cita.utoronto.ca/~murray/Papers/Sodium/Sodium_Oct_24.pdf
- academic.oup.com An origin for multiphase gas in galactic winds and haloes - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/455/2/1830/1119214
- academic.oup.com How supernova explosions power galactic winds | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/429/3/1922/999000
- etheses.whiterose.ac.uk Physical Properties of Wolf-Rayet Stars at Infra-red Wavelengths Opens in a new window — https://etheses.whiterose.ac.uk/id/eprint/10550/1/ckr_thesis_amended_v3_colorlinks.pdf
- academic.oup.com Discovery of a strong ionized-gas outflow in an AKARI-selected ultra-luminous infrared galaxy at &equals - Oxford Academic Opens in a new window — https://academic.oup.com/pasj/article-pdf/71/2/29/54665960/psz002.pdf
- ndl.ethernet.edu.et Cosmic Rays in Star-Forming Environments Opens in a new window — https://www.ndl.ethernet.edu.et/bitstream/123456789/68331/1/56.pdf
- zenodo.org Surveys of the Galactic center and the nature of the Galactic center lobe - Zenodo Opens in a new window — https://zenodo.org/record/51892
- arxiv.org Challenges to the Two-Infall Scenario by Large Stellar Age Catalogs - arXiv Opens in a new window — https://arxiv.org/html/2508.00988v2
- arxiv.org EP260321a/SN 2026gzf: The Faintest Shock Breakout Associated with a Broad-Lined Supernova - arXiv Opens in a new window — https://arxiv.org/html/2606.09992v2
- orcid.org Richard Ellis - ORCID Opens in a new window — https://orcid.org/0000-0001-7782-7071
- arts.units.it UNIVERSITÀ DEGLI STUDI DI TRIESTE - ArTS Opens in a new window — https://arts.units.it/retrieve/03474fc1-3079-44d5-ac95-69957b6c0c57/Tesi_definitiva_AliceDamiano.pdf
- arxiv.org The Multi-Scale Multi-Phase Circumgalactic Medium: Observed and Simulated Lecture notes for the 52nd (March 2023) Saas-Fee Advanced School, Switzerland. - arXiv Opens in a new window — https://arxiv.org/html/2411.07988v1
- arxiv.org Turbulent gas-rich disks at high redshift: bars & bulges in a radial shear flow - arXiv Opens in a new window — https://arxiv.org/html/2402.06060v2
- arxiv.org [astro-ph/0008283] Lyman Continuum Emission from Galaxies at z~3.4 - arXiv Opens in a new window — https://arxiv.org/abs/astro-ph/0008283
- ned.ipac.caltech.edu Galactic Winds - S. Veilleux et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/March12/Veilleux/Veilleux_refs.html
- academic.oup.com Lyman break galaxies and the star formation rate of the Universe at z≈ 6 Opens in a new window — https://academic.oup.com/mnras/article-pdf/342/2/439/3420099/342-2-439.pdf
- lweb.cfa.harvard.edu Deep mid-infrared observations of Lyman-break galaxies Opens in a new window — https://lweb.cfa.harvard.edu/irac/publications/apj1/lbg_barmby_steidel_f.pdf
- arxiv.org JWST/NIRSpec Observations of High Ionization Emission Lines in Galaxies at High Redshift Opens in a new window — https://arxiv.org/html/2505.06359v2
- researchgate.net The Multi-Scale Multi-Phase Circumgalactic Medium: Observed and Simulated Opens in a new window — https://www.researchgate.net/publication/385750533_The_Multi-Scale_Multi-Phase_Circumgalactic_Medium_Observed_and_Simulated
- par.nsf.gov How supernovae launch galactic winds? - NSF Public Access Repository Opens in a new window — https://par.nsf.gov/servlets/purl/10067207
- arxiv.org Why are thermally- and cosmic ray-driven galactic winds fundamentally different? - arXiv Opens in a new window — https://arxiv.org/html/2405.13121v1
- academic.oup.com Revisiting the galactic winds in M82 I: the recent starburst and launch of outflow in simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/546/3/stag128/8431337
- academic.oup.com Revisiting the galactic winds in M82 I: the recent starburst and launch of outflow in simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/546/3/stag128/66472601/stag128.pdf
- orbi.uliege.be The multiphase gas structure and kinematics in the ... - ORBi Opens in a new window — https://orbi.uliege.be/bitstream/2268/241774/1/Shimizu%2B19.pdf
- arxiv.org Ionized gas outflows and global kinematics of low-z luminous star-forming galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/1404.1082
- research.chalmers.se CHANG-ES XII: A LOFAR and VLA view of the edge-on star-forming galaxy NGC 3556 - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/508897/file/508897_Fulltext.pdf
- academic.oup.com The multiphase gas structure and kinematics in the circumnuclear region of NGC 5728 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/490/4/5860/30995048/stz2802.pdf
- ndl.ethernet.edu.et John W. Mason (Editor) - Astrophysics Update 2 Opens in a new window — http://ndl.ethernet.edu.et/bitstream/123456789/61169/1/57.pdf
- science.gov h-alpha emission line: Topics by Science.gov Opens in a new window — https://www.science.gov/topicpages/h/h-alpha+emission+line

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

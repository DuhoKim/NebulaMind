# Review Base 10 raw Deep Research packet — Conroy 2013

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_13_mckee_ostriker_2007_DR_PROMPT.md`
Prompt SHA-256: `ad6d7f6aeaaf868dd8c7c479b4e1f22a7a540d766ad43b2e687c9c648bd8c3f6`
Conversation ID: `6ab320dd36d0b4f8`
Submit UTC: `2026-07-16T03:58:06.526589Z`
Research Start UTC: `2026-07-16T03:58:37.028255Z`
Result captured UTC: `2026-07-16T04:09:17.887787Z`
Raw result SHA-256: `a9178e8f6a637650e77ac001b2d5d314cf5530362262c9965ab1c35360c6fa73`

## Deep Research review-base result

Deep Research Source-Base Review: Theory of Star Formation
Review Identity and Scope Map

The foundation of this advisory synthesis is the landmark 2007 review paper by Christopher F. McKee and Eve C. Ostriker, titled "Theory of Star Formation," published in the Annual Review of Astronomy and Astrophysics (Volume 45, pages 565-687). The absolute identity of this source is established via DOI 10.1146/annurev.astro.45.051806.110602, arXiv 0707.3514, and ADS bibcode 2007ARA&A..45..565M. This review is treated strictly as a secondary synthesis of the state of astrophysics up to 2007, serving as a critical bridge between the earlier paradigm of magnetically regulated, quasi-static star formation and the modern framework of dynamic, turbulence-regulated collapse.   

The scope of the 2007 review is exhaustively multi-scale, fundamentally dividing the astrophysics of star formation into distinct regimes based on characteristic length and mass scales. The macrophysical regime covers galactic disks and Giant Molecular Clouds (GMCs), where the primary concerns are the global star formation rate, the formation and destruction of clouds, and the nature of interstellar turbulence. The mesophysical regime focuses on clumps and dense cores, addressing the physical fragmentation of GMCs, the transition from supersonic turbulence to thermal pressure dominance, the origins of the Initial Mass Function (IMF) via the Core Mass Function (CMF), and the magnetic criticality of these localized structures. Finally, the microphysical regime examines protostellar systems, encompassing the distinct accretion mechanisms for low- and high-mass stars, the transport of angular momentum through accretion disks, and the regulatory feedback provided by protostellar winds and outflows. This synthesis maps these scales to provide a foundational reference packet for NebulaMind's galaxy-evolution wiki, ensuring that physical efficiencies, timescales, and mechanical triggers are strictly bounded to their appropriate geometries and regimes.   

The Macrophysics of Star Formation: Galactic Scales and Giant Molecular Clouds

The macrophysics of star formation investigates how the diffuse atomic interstellar medium (ISM) condenses into Giant Molecular Clouds (GMCs) and what regulates the overarching rate at which galactic gas is converted into stars. A central empirical pillar of this regime is the global Kennicutt-Schmidt relation, which defines a non-linear scaling between the surface density of cold gas and the resulting star formation rate surface density across an entire galaxy. However, while the Kennicutt-Schmidt law provides a macroscopic average, resolving the actual physics requires understanding the inefficiency of the process. When evaluating the total mass of molecular gas present in a galaxy against its instantaneous star formation rate, the resulting gas depletion time stretches into the billions of years. This indicates that only a very small fraction of the molecular gas collapses into stars over a single gravitational free-fall time.   

To explain this macroscopic inefficiency, the 2007 synthesis relies heavily on the paradigm of supersonic turbulence. Unlike the classical models that posited static clouds supported by magnetic fields, the modern framework recognizes the ISM as a highly nonlinear, multidimensional, turbulent environment. Turbulence in this context serves a dual role: on the scale of entire GMCs (tens of parsecs), the kinetic energy of supersonic turbulent motions provides the global ram pressure necessary to balance self-gravity, preventing the entire cloud from collapsing in a single free-fall time. Conversely, on smaller scales, the supersonic nature of this turbulence creates converging flows and intense shocks. The isothermal nature of the dense, cooling gas means that these shocks are highly compressible, generating localized overdensities that can become gravitationally unstable and initiate star formation.   

This statistical nature of isothermal, supersonic turbulence natively generates a lognormal probability density function (PDF) for the mass density of the gas. The width of this lognormal distribution is directly related to the turbulent Mach number. Consequently, the star formation rate can be analytically derived by integrating the fraction of this lognormal density PDF that exceeds the critical threshold for gravitational collapse. Table 1 outlines the fundamental established findings regarding these macrophysical processes, while Table 2 details the specific model calibrations and key measurements that anchor these theories.   

Claim ID	Epistemic Type	Bounded Statement	Scale / Regime	Confidence	Sources
REV13-E01	Analytic theory / Review synthesis	Supersonic turbulence acts as a dual-role mechanism, providing global kinetic support against collapse while generating localized shock-driven overdensities that initiate core formation.	GMC / Clump (1−100 pc)	Very High	
REV13-E02	Simulation / Analytic theory	Gas density distributions within uncollapsed regions of turbulent molecular clouds can be parameterized by a lognormal function, scaling with the isothermal Mach number.	GMC / Clump prior to collapse	High	
REV13-E03	Observation / Calibration	The global star formation efficiency per free-fall time (SFR
ff
	​

) is bounded to low values, typically ∼1−2%, requiring robust internal support or rapid disruption.	Galactic / GMC	High	
REV13-E07	Observation	The area-averaged star formation rate correlates with the total gas surface density according to a non-linear power law.	Galactic (≥1 kpc)	Very High	
  
Measurement ID	Value / Parameterization	Units	Scale / Tracer	Sample / Method	Uncertainty / Status	Sources
REV13-N04	Σ
SFR
	​

∝Σ
gas
N
	​

 (N≈1.4)	M
⊙
	​

 yr
−1
 kpc
−2
	Galactic (H$\alpha$, FIR, CO/HI)	Disk-averaged local spiral/starbursts	Robust for global averages; debated at sub-kpc	
REV13-N05	SFR
ff
	​

≈0.01−0.02	Dimensionless ratio	GMC / Clump (YSO counts vs total mass)	Observation of instantaneous SFR vs local free-fall time	Accepted global average; local variations exist	
  

Despite the consensus on the importance of supersonic turbulence, several fundamental tensions remained unresolved in 2007 regarding the macrophysics of star formation. Chief among these was the origin and maintenance of the turbulence itself. Because supersonic turbulence dissipates its kinetic energy rapidly—typically on the order of a single cloud crossing time—it requires continuous driving to maintain the observed velocity dispersions. A fierce debate persisted regarding whether this turbulence was primarily driven from the "top down" via large-scale galactic shear, spiral arm shocks, and global gravitational instabilities, or driven from the "bottom up" via localized stellar feedback such as protostellar outflows, stellar winds, and supernova explosions. Furthermore, while the lognormal density PDF provided an elegant analytic explanation for the star formation rate, the exact physical definition of the transition threshold—whether star formation requires a hard critical column density limit related to molecular shielding, or if it scales continuously across the density spectrum—remained highly dependent on observational tracers and scale definitions. Table 3 outlines the key macrophysical debates and unknowns.

Debate / Unknown ID	Topic	Competing Positions / Why It Matters	Why Unresolved / Decisive Observation Needed	Sources
REV13-D02	Primary driver of interstellar turbulence	Driven by internal stellar feedback vs. large-scale external galactic processes.	Difficult to isolate scale-dependent kinetic energy injection in multi-phase ISM simulations.	
REV13-D07	SF thresholds vs continuous efficiency	Hard critical column density threshold vs continuous efficiency scaling dictated by the turbulent PDF.	Fractal nature of ISM makes thresholds highly dependent on chosen observational tracers.	
REV13-D05	GMC lifetime and dynamical state	GMCs are long-lived quasi-virial structures vs transient entities surviving only a few free-fall times.	Difficulties establishing absolute chronological ages for gas devoid of standard stellar clocks.	
REV13-U03	Sub-grid turbulence driving	Determines true physical driver of accretion rates in models.	Needs galaxy-scale multi-phase MHD simulations tracking self-consistent feedback down to sub-pc scales.	N/A
REV13-U05	Efficiency of GMC destruction	Determines the total star formation efficiency limit of a GMC.	Needs mapping of atomic/molecular transition zones and ionization fronts around young clusters.	N/A
  
The Mesophysics of Star Formation: Clumps, Dense Cores, and Magnetic Criticality

As the scale descends from the giant molecular cloud to the parsec and sub-parsec regimes, the physical mechanisms transition from macrophysics to mesophysics. Within the turbulent, filamentary structure of a GMC, specific regions of gas become sufficiently dense that the turbulent kinetic energy dissipates, allowing the localized thermal pressure to become the primary barrier against self-gravity. These regions, termed clumps and cores, are the direct progenitors of stellar clusters and individual stars, respectively. The fundamental unit of fragmentation in these thermally dominated regions is the Jeans mass, or its pressure-bounded equivalent, the Bonnor-Ebert mass. The thermal Jeans mass establishes the characteristic baseline scale for fragmentation, predicting the mass at which a core can no longer support itself against gravity via thermal pressure alone.   

Historically, mesophysical collapse was thought to be regulated almost entirely by magnetic fields. In the classical theory, cores were assumed to be magnetically subcritical, meaning the magnetic pressure was strong enough to completely halt gravitational collapse. Star formation could only proceed via ambipolar diffusion—a slow process where neutral gas gradually slips past the magnetically coupled ions, slowly increasing the mass-to-flux ratio in the core's center until it became magnetically supercritical and collapsed. However, the 2007 synthesis highlighted a major paradigm shift driven by improved observational techniques. Zeeman splitting measurements of the magnetic mass-to-flux ratio in typical molecular clouds indicated that the vast majority of GMCs and their substructures are already globally magnetically supercritical. While magnetic fields remain crucial for angular momentum transport and altering shock dynamics, they are generally insufficient to independently prevent gravitational collapse, rendering traditional slow ambipolar diffusion insufficient as the sole regulator of the star formation rate. Table 4 defines the key established findings for the mesophysical regime.   

Claim ID	Epistemic Type	Bounded Statement	Scale / Regime	Confidence	Sources
REV13-E05	Observation / Review synthesis	Measurements indicate that the mass-to-flux ratio in typical GMCs exceeds the critical threshold, rendering ambipolar diffusion insufficient as the sole regulator.	GMC / Clump	High	
REV13-E09	Analytic theory / Simulation	In regions where turbulent and magnetic support dissipate, the thermal Jeans mass dictates the peak of the fragmentation mass spectrum.	Dense core	High	
REV13-E04	Observation	The mass spectrum of dense pre-stellar cores mirrors the Initial Mass Function (IMF), offset by a mass-conversion efficiency factor.	Core (0.1 pc)	Mod/High	
REV13-E10	Observation	Above ∼1M
⊙
	​

, the mass distribution of newly formed stars converges on a universal power law dN/dlnm∝m
−Γ
 with Γ≈1.35.	Stellar cluster	Very High	
  

Perhaps the most significant mesophysical breakthrough synthesized in the review is the relationship between the Core Mass Function (CMF) and the stellar Initial Mass Function (IMF). Observations utilizing deep near-infrared dust extinction and sub-millimeter continuum mapping successfully traced the mass distribution of dense, pre-stellar cores within local clouds like the Pipe Nebula. The resulting CMF exhibited a striking morphological similarity to the IMF, featuring a broad lognormal turnover at low masses and a Salpeter-like power-law slope at the high-mass end. The primary difference was a shift in the mass scale, implying a core-to-star mass conversion efficiency of approximately 30 percent. This observation profoundly suggested that the ultimate mass distribution of stars is largely predetermined by the physics of gas fragmentation in the molecular cloud prior to actual protostellar collapse. Table 5 outlines the specific mathematical calibrations associated with fragmentation and the IMF.   

Measurement ID	Value / Parameterization	Units	Scale / Tracer	Sample / Method	Uncertainty / Status	Sources
REV13-N08	M
BE
	​

=1.18c
s
4
	​

/(G
3
P)
1/2
	M
⊙
	​

	Core scale	Derivation for stable, isothermal, pressure-truncated gas sphere	Foundational limit; assumes no turbulence/magnetic field	
REV13-N06	M
Φ
	​

=c
Φ
	​

Φ/G
1/2
 (c
Φ
	​

≈0.12−0.18)	M
⊙
	​

	Cloud/Core (Zeeman splitting)	Analytic derivation for cold sheet and flux tube geometries	High theoretical confidence; challenging to measure	
REV13-N01	Γ≈1.35 (dN/dlnm∝m
−Γ
)	Dimensionless index	Stellar cluster	Star counting and luminosity function inversion	Established empirical constant	
REV13-N02	m
c
	​

≈0.2−0.5M
⊙
	​

	M
⊙
	​

	Stellar scale	Extinction and near-IR surveys	Accepted, fluctuates based on binary fraction corrections	
REV13-N03	ϵ≈30%±10%	Percentage	Core to Protostar	Comparison of CMF integral to the IMF in specific clouds	Debated if global constant or core-finding artifact	
  

Despite these advances, the mesophysical regime was fraught with intense debates. While the CMF-to-IMF mapping provided a compelling narrative for the origin of stellar masses, the underlying physical cause of the IMF peak remained highly contested. Some theorists argued that the peak is set thermodynamically by the thermal Jeans mass at the precise density where dust-gas coupling alters the cooling physics of the cloud. Others posited a dynamical origin, where the peak is dictated by the turbulent crossing scale and the shock properties of the ISM. Furthermore, the universality of this CMF-to-IMF mapping was questioned, as it assumes that cores collapse in relative isolation. If, instead, cores dynamically interact and accrete from a shared reservoir (competitive accretion), the initial CMF is largely overwritten by subsequent N-body cluster dynamics. Finally, the exact role of magnetic fields remained unproven; while clouds appeared globally supercritical, the lack of three-dimensional magnetic topology mapping at the dense core boundary meant that the exact transition mechanics of collapse were still obscured. Table 6 summarizes these mesophysical tensions.

Debate / Unknown ID	Topic	Competing Positions / Why It Matters	Why Unresolved / Decisive Observation Needed	Sources
REV13-D03	Role of ambipolar diffusion	Slow diffusion governs core formation in subcritical clouds vs turbulence drives rapid formation in supercritical clouds.	Exact measurements of B-field strength/geometry at the dense core boundary were technically challenging.	
REV13-D04	Origin of IMF characteristic peak	Thermodynamic transition (thermal Jeans mass) vs dynamical turbulent crossing scale.	Both mathematically reproduce lognormal turnover; requires higher-resolution CMF surveys in variable environments.	
REV13-D06	Universality of the IMF	Universal regardless of environment vs top-heavy in starbursts/Population III.	High extinction and distance limits direct IMF star-counting at the low-mass end in extreme environments.	
REV13-U01	3D topology of core magnetic fields	Required to settle debate on ambipolar diffusion vs turbulent dissipation.	Needs high-resolution sub-mm dust polarization mapping tracing field lines to 1000 AU scales.	N/A
REV13-U04	Universality of CMF-to-IMF mapping	Determines if stellar masses are predetermined by gas fragmentation or overwritten by N-body competitive accretion.	Needs statistically complete core surveys across diverse environments combined with kinematic flow data.	N/A
  
The Microphysics of Star Formation: Protostellar Accretion, Disks, and High-Mass Regimes

The microphysics of star formation details the final descent of matter from a collapsing dense core onto a protostellar object. A foundational realization in this regime is that star formation is fundamentally a clustered, dynamic process. The vast majority of stars, and virtually all massive stars, form within dense clusters and associations rather than in strict isolation. Because the infalling gas from the natal core possesses inherent angular momentum, it cannot collapse directly onto the protostar. Instead, it must form a circumstellar accretion disk.   

The accretion disk represents a critical bottleneck in star formation. To allow mass to accrete onto the central star, angular momentum must be fiercely redistributed outward. While the Magneto-Rotational Instability (MRI) was recognized as a highly efficient source of turbulent viscosity capable of driving this accretion, the exact ionization fraction in the dense midplane of the disk—the so-called "dead zone"—was often deemed too low to couple to the magnetic field. Consequently, alternative transport mechanisms such as gravitational instabilities or spiral density waves were highly debated. Furthermore, to prevent the central protostar from spinning up to breakup velocity, angular momentum must ultimately be ejected from the system entirely. This is achieved via powerful, magneto-centrifugally driven bipolar outflows and jets, which carry away a massive fraction of the system's angular momentum and regulate the final mass of the star.   

The microphysics of massive stars (>8M
⊙
	​

) introduces unique, extreme theoretical challenges, proving that high-mass star formation is not merely a scaled-up homologous extension of low-mass formation. The primary obstacle is intense radiation pressure. As a massive protostar rapidly accretes, it becomes intensely luminous, exerting an outward radiation pressure that surpasses the inward pull of gravity for spherically accreting dust and gas. To overcome this, massive stars require extraordinary natal environments characterized by massive column densities (typically Σ≥1 g cm
−2
) to force accretion through the radiation barrier via disk geometries and continuous high-pressure infall. Table 7 details the established findings and key measurements for the microphysical regime.   

Claim ID	Epistemic Type	Bounded Statement	Scale / Regime	Confidence	Sources
REV13-E11	Observation	The vast majority of stars, particularly massive stars, form in gravitationally interacting clusters rather than in isolation.	Clump to Protostar	Very High	
REV13-E08	Analytic theory / Observation	Bipolar outflows and jets, driven by magneto-centrifugal forces, remove significant angular momentum, preventing rotational breakup.	Protostar/Disk (<1000 AU)	High	
REV13-E06	Analytic theory / Review synthesis	Massive star formation must overcome intense radiation pressure, necessitating disk-mediated accretion and/or competitive geometries; it is not homologous to low-mass formation.	Protostar/Disk (>8M
⊙
	​

)	High	
REV13-E12	Analytic theory / Observation	To supply accretion rates required to overcome radiation pressure, the natal environment of massive stars must possess massive column densities.	Clump / Core (massive)	Mod/High	
  
Measurement ID	Value / Parameterization	Units	Scale / Tracer	Sample / Method	Uncertainty / Status	Sources
REV13-N07	Σ≥1 g cm
−2
	g cm
−2
	Clump scale	Analytic limits on accretion rates matched with dense protocluster observations	Useful predictive threshold, heavily dependent on feedback models	
  

The extreme environments required for massive star formation fueled one of the most intense theoretical disputes in astrophysics: Monolithic Collapse (the Turbulent Core Model) versus Competitive Accretion. The Turbulent Core model posits that massive stars form from the ordered, monolithic collapse of discrete, highly pressurized, massive cores supported by intense turbulence. In contrast, the Competitive Accretion model argues that such massive, stable cores do not exist; instead, massive stars form dynamically at the center of a cluster potential, ruthlessly gathering unbound gas from a shared reservoir and out-competing lower-mass siblings due to their larger gravitational cross-section. Resolving this debate, alongside understanding the true escape mechanisms for radiation pressure, remained a critical unknown in 2007. Table 8 details these microphysical debates and unresolved frontiers.   

Debate / Unknown ID	Topic	Competing Positions / Why It Matters	Why Unresolved / Decisive Observation Needed	Sources
REV13-D01	Monolithic Collapse vs Competitive Accretion	Massive stars form from ordered collapse of distinct massive cores vs dynamic accretion from a shared, unbound cluster potential.	Observational limits in resolving early high-mass protoclusters prevented definitive mass budgets prior to feedback.	
REV13-D08	Angular momentum transport in disks	MRI inducing turbulent viscosity vs global gravitational instabilities or magnetic braking.	Ionization fractions in the disk "dead zone" might be too low to sustain MRI.	
REV13-U02	Overcoming radiation pressure in >50M
⊙
	​

 stars	One-dimensional models predicted radiation pressure stalls accretion, yet massive stars exist.	Needs 3D radiation-hydrodynamic simulations resolving Rayleigh-Taylor instabilities and outflow cavities.	N/A
REV13-U06	Pop III to Pop I/II transition mechanics	Understanding the metallicity threshold where fine-structure line cooling triggers clustered, low-mass star formation is vital for cosmic reionization.	Needs cosmological simulations incorporating detailed chemical networks and metal-line cooling.	N/A
  
Primary-Citation Harvest

The synthesis presented in McKee & Ostriker (2007) is built upon decades of foundational research. Table 9 presents a curated harvest of the primary analytical, observational, and computational papers cited within the review's bibliography (published no later than 2007) that form the scientific boundaries of the claims made above.

Key	Exact Authors	Year	Journal	Exact Title	DOI	arXiv	ADS	Role	Review Locator	Scientific Boundary
REV13-P001	Shu, F. H., Adams, F. C., & Lizano, S.	1987	Annual Review of Astronomy and Astrophysics	Star Formation in Molecular Clouds: Observation and Theory	10.1146/annurev.aa.25.090187.000323	none	1987ARA&A..25...23S	supporting_review	Intro/Scope	Established the classic theoretical framework of isolated, magnetically regulated inside-out core collapse.
REV13-P002	Mac Low, M.-M., & Klessen, R. S.	2004	Reviews of Modern Physics	Control of star formation by supersonic turbulence	10.1103/RevModPhys.76.125	astro-ph/0301093	2004RvMP...76..125M	supporting_review	Section 2.1	Consolidated the paradigm shift toward supersonic turbulence as the primary regulator of molecular cloud fragmentation.
REV13-P003	Kennicutt, R. C. Jr.	1998	The Astrophysical Journal	The Global Schmidt Law in Star-forming Galaxies	10.1086/305588	astro-ph/9712213	1998ApJ...498..541K	measurement	Section 1/Macro	Provided the canonical empirical calibration of the surface density scaling law for galactic star formation.
REV13-P004	Salpeter, E. E.	1955	The Astrophysical Journal	The Luminosity Function and Stellar Evolution	10.1086/145971	none	1955ApJ...121..161S	measurement	Section 3.3/IMF	Defined the foundational high-mass power-law slope of the initial mass function.
REV13-P005	Kroupa, P.	2002	Science	The Initial Mass Function of Stars: Evidence for Uniformity in Variable Systems	10.1126/science.1067524	astro-ph/0201098	2002Sci...295...82K	calibration	Section 3.3/IMF	Parameterized the multi-part power-law functional form of the universal stellar IMF down to the brown dwarf regime.
REV13-P006	Chabrier, G.	2003	Publications of the Astronomical Society of the Pacific	Galactic Stellar and Substellar Initial Mass Function	10.1086/376392	astro-ph/0304382	2003PASP..115..763C	calibration	Section 3.3/IMF	Established the standard lognormal parameterization for the low-mass end of the IMF.
REV13-P007	Alves, J., Lombardi, M., & Lada, C. J.	2007	Astronomy & Astrophysics	The mass function of dense molecular cores and the origin of the IMF	10.1051/0004-6361:20066389	astro-ph/0612126	2007A&A...462L..17A	measurement	Section 3.3/CMF	Measured the core mass function of the Pipe Nebula utilizing dust extinction, establishing a morphological match to the IMF offset by a 30% efficiency factor.
REV13-P008	Lada, C. J., & Lada, E. A.	2003	Annual Review of Astronomy and Astrophysics	Embedded Clusters in Molecular Clouds	10.1146/annurev.astro.41.011802.094844	astro-ph/0301540	2003ARA&A..41...57L	supporting_review	Section 1/Macro	Consolidated observations demonstrating that the vast majority of stars form in clustered environments rather than in isolation.
REV13-P009	Krumholz, M. R., & McKee, C. F.	2005	The Astrophysical Journal	A General Theory of Turbulence-regulated Star Formation, from Spirals to Ultraluminous Infrared Galaxies	10.1086/431734	astro-ph/0505177	2005ApJ...630..250K	analytic_theory	Section 3.4/SFR	Formulated an analytic framework predicting the star formation rate based on the lognormal density PDF of supersonic isothermal turbulence.
REV13-P010	Padoan, P., & Nordlund, Å.	1999	The Astrophysical Journal	A Super-Alfvénic Model of Dark Clouds	10.1086/308002	astro-ph/9903067	1999ApJ...526..279P	simulation	Section 2.1	Demonstrated via MHD simulations that molecular clouds exhibit super-Alfvénic turbulence and weak mean magnetic fields, challenging ambipolar diffusion models.
REV13-P011	McKee, C. F.	1989	The Astrophysical Journal	Photoionization-regulated star formation and the structure of molecular clouds	10.1086/167954	none	1989ApJ...345..782M	analytic_theory	Section 3.4/SFR	Modeled star formation rates driven by ambipolar diffusion where the ionization fraction is maintained by UV photoionization.
REV13-P012	Zinnecker, H., & Yorke, H. W.	2007	Annual Review of Astronomy and Astrophysics	Toward Understanding Massive Star Formation	10.1146/annurev.astro.44.051905.092549	astro-ph/0703326	2007ARA&A..45..481Z	supporting_review	Section 4.3	Synthesized theoretical challenges of high-mass star formation, specifically focusing on radiation pressure and accretion dynamics.
REV13-P013	Solomon, P. M., Rivolo, A. R., Barrett, J., & Yahil, A.	1987	The Astrophysical Journal	Mass, Luminosity, and Line Width Relations of Galactic Molecular Clouds	10.1086/165493	none	1987ApJ...319..730S	measurement	Section 3.1/GMCs	Established the fundamental scaling relations (Larson's Laws) for Galactic GMCs using CO emission.
REV13-P014	Elmegreen, B. G.	1993	The Astrophysical Journal	Star Formation in a Crossing Time	none	none	1993ApJ...411..170E	analytic_theory	Section 3.2	Argued that star formation occurs rapidly, over roughly one crossing time, challenging models of long-lived quasi-equilibrium clouds.
REV13-P015	Bate, M. R., Bonnell, I. A., & Bromm, V.	2003	Monthly Notices of the Royal Astronomical Society	The formation of a star cluster: predicting the properties of stars and brown dwarfs	10.1046/j.1365-8711.2003.06210.x	astro-ph/0212380	2003MNRAS.339..577B	simulation	Section 3.3/IMF	Conducted hydrodynamic simulations of cluster formation, demonstrating competitive accretion and dynamical ejections forming brown dwarfs.
REV13-P016	McKee, C. F., & Tan, J. C.	2003	The Astrophysical Journal	The Formation of Massive Stars from Turbulent Cores	10.1086/346149	astro-ph/0206037	2003ApJ...585..850M	analytic_theory	Section 4.3	Proposed the Turbulent Core model for massive star formation, arguing for rapid monolithic collapse in highly pressurized, turbulent environments.
REV13-P017	Bonnell, I. A., Bate, M. R., Clarke, C. J., & Pringle, J. E.	2001	Monthly Notices of the Royal Astronomical Society	Competitive accretion in embedded stellar clusters	10.1046/j.1365-8711.2001.04270.x	astro-ph/0101511	2001MNRAS.323..785B	analytic_theory	Section 4.3	Outlined the competitive accretion paradigm where massive stars form by accreting gas from a shared cluster reservoir.
REV13-P018	Larson, R. B.	1981	Monthly Notices of the Royal Astronomical Society	Turbulence and star formation in molecular clouds	10.1093/mnras/194.4.809	none	1981MNRAS.194..809L	measurement	Section 2.1	Identified the empirical scaling relations connecting velocity dispersion to the spatial scale of molecular clouds.
REV13-P019	Larson, R. B.	1992	Monthly Notices of the Royal Astronomical Society	Towards understanding the stellar initial mass function	10.1093/mnras/256.4.641	none	1992MNRAS.256..641L	analytic_theory	Section 3.3/IMF	Linked the characteristic mass of the IMF to the thermal Jeans mass resulting from the transition in ISM cooling mechanisms.
REV13-P020	Krumholz, M. R., Klein, R. I., & McKee, C. F.	2007	The Astrophysical Journal	Radiation Pressure in Massive Star Formation	10.1086/510664	astro-ph/0609355	2007ApJ...656..959K	simulation	Section 4.3	Utilized 3D radiation-hydrodynamic simulations to demonstrate that Rayleigh-Taylor instabilities allow accretion to bypass the radiation pressure limit.
REV13-P021	Tomisaka, K., Ikeuchi, S., & Nakamura, T.	1988	The Astrophysical Journal	The Equilibria and Evolutions of Magnetized, Rotating, Isothermal Clouds	10.1086/166986	none	1988ApJ...335..239T	analytic_theory	Section 2.3	Analytically determined the geometric coefficient for the critical mass-to-flux ratio of centrally condensed clouds.
REV13-P022	Nakano, T., & Nakamura, T.	1978	Publications of the Astronomical Society of Japan	Gravitational instability of magnetized gaseous disks	none	none	1978PASJ...30..681N	analytic_theory	Section 2.3	Derived the critical magnetic mass-to-flux ratio for an infinite cold sheet.
REV13-P023	McKee, C. F., & Tan, J. C.	2002	Nature	Massive star formation in 100,000 years from turbulent and pressurized molecular clouds	10.1038/416059a	astro-ph/0203071	2002Natur.416...59M	analytic_theory	Section 4.3	Established timescale and column density constraints for the rapid formation of massive stars.
REV13-P024	Miller, G. E., & Scalo, J. M.	1979	The Astrophysical Journal Supplement Series	The initial mass function and stellar birthrate in the solar neighborhood	10.1086/190629	none	1979ApJS...41..513M	calibration	Section 3.3/IMF	Introduced the lognormal functional fit for the low-mass regime of the observed stellar mass distribution.
REV13-P025	Muench, A. A., Lada, E. A., Lada, C. J., & Alves, J.	2002	The Astrophysical Journal	The Luminosity and Mass Function of the Trapezium Cluster from a Deep Infrared Imaging Survey	10.1086/340578	astro-ph/0203494	2002ApJ...573..366M	measurement	Section 3.3/IMF	Measured the IMF down to the substellar regime in the Orion Nebula Cluster, securing the lognormal turnover.
REV13-P026	Motte, F., Andre, P., & Neri, R.	1998	Astronomy & Astrophysics	The initial conditions of star formation in the rho Ophiuchi main cloud	none	none	1998A&A...336..150M	measurement	Section 3.3/CMF	One of the first sub-millimeter studies mapping the dense core mass function, revealing its structural similarity to the IMF.
REV13-P027	Testi, L., & Sargent, A. I.	1998	The Astrophysical Journal Letters	Star Formation in Clusters: A Survey of Compact Millimeter-Wave Sources in the Serpens Core	10.1086/311756	astro-ph/9810313	1998ApJ...508L..91T	measurement	Section 3.3/CMF	Utilized mm-wave interferometry to trace dust condensations, confirming a Salpeter-like mass spectrum for prestellar cores.
REV13-P028	Beuther, H., & Schilke, P.	2004	Science	The Earliest Phases of Massive Star Formation	10.1126/science.1093166	astro-ph/0402581	2004Sci...303.1167B	measurement	Section 4.3	Captured high-resolution observations of massive dense cores, probing the initial fragmentation conditions for clustered star formation.
REV13-P029	Zuckerman, B., & Palmer, P.	1974	Annual Review of Astronomy and Astrophysics	Radio Radiation from Interstellar Molecules	10.1146/annurev.aa.12.090174.001431	none	1974ARA&A..12..279Z	supporting_review	Section 3.4/SFR	Identified the fundamental gas depletion time discrepancy, noting the observed SFR is drastically lower than the free-fall collapse rate.
REV13-P030	Williams, P. M., & McKee, C. F.	1997	The Astrophysical Journal	The Star Formation Law in Galactic Clouds	10.1086/303598	none	1997ApJ...476..166W	analytic_theory	Section 3.4/SFR	Quantified the star formation efficiency in Milky Way GMCs, concluding it is regulated to be inefficient per crossing time.
REV13-P031	Mouschovias, T. C.	1991	The Astrophysical Journal	Magnetic braking, ambipolar diffusion, cloud cores, and star formation: Natural length scales and masses	10.1086/170068	none	1991ApJ...373..169M	analytic_theory	Section 2.3	Developed detailed models of ambipolar diffusion timescales acting as the primary bottleneck controlling star formation rates in subcritical clouds.
REV13-P032	Mouschovias, T. C., & Ciolek, G. E.	1999	The Origin of Stars and Planetary Systems	Magnetic Fields and Star Formation	none	none	1999osps.conf..305M	supporting_review	Section 2.3	Synthesized the extensive theoretical framework for the strong-magnetic-field, quasi-static mode of core formation.
REV13-P033	Padoan, P.	1995	Monthly Notices of the Royal Astronomical Society	The universal star formation efficiency	10.1093/mnras/277.2.377	none	1995MNRAS.277..377P	analytic_theory	Section 3.4/SFR	Suggested an early analytic framework relating the turbulent lognormal density field to star formation efficiencies.
REV13-P034	Wong, T., & Blitz, L.	2002	The Astrophysical Journal	The Relationship between Gas Content and Star Formation in Molecule-rich Spiral Galaxies	10.1086/339287	astro-ph/0111166	2002ApJ...569..157W	measurement	Section 3.4/SFR	Analyzed extragalactic gas depletion times, extending the Kennicutt-Schmidt constraints specifically to molecule-dominated regions.
REV13-P035	Fukui, Y., Mizuno, N., Yamaguchi, R., et al.	2001	Publications of the Astronomical Society of Japan	A Survey of Giant Molecular Clouds in the Magellanic Clouds	10.1093/pasj/53.6.L41	none	2001PASJ...53L..41F	measurement	Section 3.1/GMCs	Documented the non-thermal velocity dispersions of GMCs in extragalactic environments.
REV13-P036	Engargiola, G., Plambeck, R. L., Rosolowsky, E., & Blitz, L.	2003	The Astrophysical Journal Supplement Series	Giant Molecular Clouds in M33	10.1086/378544	astro-ph/0308075	2003ApJS..149..343E	measurement	Section 3.1/GMCs	Provided robust measurements of GMC properties and internal turbulence within a local group spiral galaxy.
REV13-P037	Papaloizou, J. C. B., & Lin, D. N. C.	1995	Annual Review of Astronomy and Astrophysics	Theory of Accretion Disks I: Angular Momentum Transport Processes	10.1146/annurev.aa.33.090195.002453	none	1995ARA&A..33..505P	supporting_review	Section 4.2/Disks	Evaluated mechanisms for angular momentum redistribution within protostellar disks, addressing the classical angular momentum problem.
REV13-P038	Stone, J. M., Gammie, C. F., Balbus, S. A., & Hawley, J. F.	2000	Protostars and Planets IV	Transport Processes in Protostellar Disks	none	astro-ph/9907142	2000prpl.conf..589S	analytic_theory	Section 4.2/Disks	Detailed the application of the Magneto-Rotational Instability (MRI) to angular momentum transport in protostellar environments.
REV13-P039	Stahler, S. W., Shu, F. H., & Taam, R. E.	1980	The Astrophysical Journal	The evolution of protostars. I - Global formulation and results for a 1 solar mass star	10.1086/158327	none	1980ApJ...241..637S	analytic_theory	Section 4.1/Low	Formulated the early accretion physics linking the free-fall collapse rate of a core to the radius and luminosity of a protostar.
REV13-P040	Mestel, L., & Spitzer, L. Jr.	1956	Monthly Notices of the Royal Astronomical Society	Star formation in magnetic dust clouds	10.1093/mnras/116.5.503	none	1956MNRAS.116..503M	analytic_theory	Section 2.3	Pioneered the concept of ambipolar diffusion as a mechanism to shed magnetic flux during cloud collapse.
DO_NOT_USE_UNVERIFIED Quarantine

The following sources were identified in raw context arrays but possess post-2007 publication dates, lack proper identifiers, or pertain to distinct bodies of work unrelated to the 2007 review's bibliography. They must remain isolated from foundational claims.

Quarantine Reason	Citation Identity	Status
Post-2007 review context	Krumholz, M. R. (2014) Physics Reports	UNCITED_NOT_USABLE
Post-2007 simulation context	Federrath, C., & Klessen, R. S. (2012) ApJ	UNCITED_NOT_USABLE
Post-2007 supporting review	Padoan, P., et al. (2014) Protostars and Planets VI	UNCITED_NOT_USABLE
Post-2007 maser observations	Breen et al. (2013) MNRAS	UNCITED_NOT_USABLE
Post-2007 calibration of star formation law	Krumholz, Dekel, & McKee (2012) ApJ	UNCITED_NOT_USABLE
Post-2007 observational data	Alves et al. "Herschel surveys" (e.g., Könyves et al. 2015, André et al. 2010)	UNCITED_NOT_USABLE
Post-2007 publication (temporal boundary breach)	Krumholz, M. R. & McKee, C. F. (2008) Nature, 451, 1082	UNCITED_NOT_USABLE
Composite Source Identity Ledger

This ledger definitively maps physical papers to their verification strings and bounds.

Source Key	Primary Authors	Year	Status/Role	Identifiers (DOI / ADS)	Boundary Condition Notes
Review	McKee, C.F., Ostriker, E.C.	2007	Base Review	10.1146/annurev.astro.45.051806.110602 / 2007ARA&A..45..565M	Unifies multi-scale SF theory.
REV13-P001	Shu, F.H., et al.	1987	supporting_review	10.1146/annurev.aa.25.090187.000323 / 1987ARA&A..25...23S	Classical magnetic inside-out framework.
REV13-P003	Kennicutt, R.C.	1998	measurement	10.1086/305588 / 1998ApJ...498..541K	Galactic disk scale; empirical KS law.
REV13-P005	Kroupa, P.	2002	calibration	10.1126/science.1067524 / 2002Sci...295...82K	Universal broken power-law IMF.
REV13-P007	Alves, J., et al.	2007	measurement	10.1051/0004-6361:20066389 / 2007A&A...462L..17A	Dense core mass scale using dust tracer.
REV13-P009	Krumholz, M.R., McKee, C.F.	2005	analytic_theory	10.1086/431734 / 2005ApJ...630..250K	Lognormal density PDF SF rate predictions.
REV13-P013	Solomon, P.M., et al.	1987	measurement	10.1086/165493 / 1987ApJ...319..730S	CO tracer for turbulent GMCs.
REV13-P016	McKee, C.F., Tan, J.C.	2003	analytic_theory	10.1086/346149 / 2003ApJ...585..850M	High-mass monolithic collapse model.
REV13-P017	Bonnell, I.A., et al.	2001	analytic_theory	10.1046/j.1365-8711.2001.04270.x / 2001MNRAS.323..785B	Competitive accretion cluster model.
REV13-P021	Tomisaka, K., et al.	1988	analytic_theory	10.1086/166986 / 1988ApJ...335..239T	Geometric coefficient context for magnetic clouds.

(Note: Ledger constraints enforce that tracers and conversion mismatches—such as dust vs. CO derived mass functions—are distinct regimes and do not map perfectly 1:1 without assumed conversion efficiencies).

REVIEW_BASE_13_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- arxiv.org [0707.3514] Theory of Star Formation - arXiv Opens in a new window — https://arxiv.org/abs/0707.3514
- semanticscholar.org [PDF] Theory of Star Formation | Semantic Scholar Opens in a new window — https://www.semanticscholar.org/paper/Theory-of-Star-Formation-McKee-Ostriker/95fdb251bac6a60de90f93a5da8e55d78bd2d85c
- arxiv.org Theory of Star Formation - arXiv Opens in a new window — https://arxiv.org/pdf/0707.3514
- ore.exeter.ac.uk The Star Formation Rate of Molecular Clouds - University of Exeter research repository Opens in a new window — https://ore.exeter.ac.uk/articles/journal_contribution/The_Star_Formation_Rate_of_Molecular_Clouds/29714777/1/files/56731469.pdf
- annualreviews.org Magnetic Fields in Molecular Clouds - Annual Reviews Opens in a new window — https://www.annualreviews.org/doi/pdf/10.1146/annurev-astro-081811-125514
- researchgate.net (PDF) Star Formation from Galaxies to Globules - ResearchGate Opens in a new window — https://www.researchgate.net/publication/1926106_Star_Formation_from_Galaxies_to_Globules
- arxiv.org arXiv:astro-ph/0505177v1 9 May 2005 Opens in a new window — https://arxiv.org/pdf/astro-ph/0505177
- ay201b.wordpress.com Does the IMF come from the CMF? | ISM and Star Formation - WordPress.com Opens in a new window — https://ay201b.wordpress.com/2011/03/31/does-the-imf-come-from-the-cmf/
- arxiv.org [astro-ph/0612126] The mass function of dense molecular cores and the origin of the IMF - arXiv Opens in a new window — https://arxiv.org/abs/astro-ph/0612126
- annualreviews.org Toward Understanding Massive Star Formation - Annual Reviews Opens in a new window — https://www.annualreviews.org/doi/pdf/10.1146/annurev.astro.44.051905.092549
- academic.oup.com The role of tidal interactions in star formation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/332/1/155/974295
- arxiv.org [astro-ph/0206037] The Formation of Massive Stars from Turbulent Cores - arXiv Opens in a new window — https://arxiv.org/abs/astro-ph/0206037
- scispace.com Physical Processes in Star Formation - SciSpace Opens in a new window — https://scispace.com/pdf/physical-processes-in-star-formation-1vsptz5w8y.pdf
- preprints.org Star Formation Efficiency and Class I Protostellar Timescales in ATLASGAL Dense Clumps Opens in a new window — https://www.preprints.org/manuscript/202606.1571
- arxiv.org A Momentum-Regulated Model For Star Formation Efficiency in Giant Molecular Clouds Opens in a new window — https://arxiv.org/html/2607.06727v1
- academic.oup.com Star formation in the first galaxies – II. Clustered star formation and the influence of metal line cooling - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/438/2/1669/1013787
- gsjournal.net “Rapid Star Formation Theory” by Randy Wells Applied Physicist and Independent Researcher in Theoretical Physics Keywords Opens in a new window — https://www.gsjournal.net/Science-Journals/Research%20Papers-Astrophysics/Download/9811
- adsabs.harvard.edu 2 0 0 5MNRAS.35 6.12 0IB Mon. Not. R. Astron. Soc. 356, 1201-1221 (2005) doiilO.l 11 l/j.1365-2966.2004.08593.x The origin of th - NASA ADS Opens in a new window — https://adsabs.harvard.edu/pdf/2005MNRAS.356.1201B
- arxiv.org A Universal Stellar Initial Mass Function? A Critical Look at Variations - arXiv Opens in a new window — https://arxiv.org/pdf/1001.2965
- arxiv.org How Should We Understand the Core Mass Function? A memo of the CMF2IMF conference at ESO Garching - arXiv Opens in a new window — https://arxiv.org/pdf/2607.09858
- kar.kent.ac.uk A study of the Impact of Triggered Star Formation - Kent Academic Repository Opens in a new window — https://kar.kent.ac.uk/90152/1/4Thesis.pdf
- royalsocietypublishing.org The birth environment of planetary systems - Royal Society Publishing Opens in a new window — https://royalsocietypublishing.org/rsos/article/7/11/201271/95312/The-birth-environment-of-planetary-systemsBirth
- arxiv.org On the role of magnetic fields in star formation - arXiv Opens in a new window — https://arxiv.org/pdf/1809.04921
- research.chalmers.se Unveiling a multiscale view of massive star and cluster formation - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/527750/file/527750_Fulltext.pdf
- kitp.ucsb.edu LETTERS - KITP Opens in a new window — https://www.kitp.ucsb.edu/sites/default/files/kitp/research/nature06620.pdf
- mso.anu.edu.au LETTERS - The formation of stars by gravitational collapse rather than competitive accretion Opens in a new window — https://www.mso.anu.edu.au/~krumholz/publications/2005/krumholz05d.pdf
- researchgate.net The Formation of Massive Stars from Turbulent Cores - ResearchGate Opens in a new window — https://www.researchgate.net/publication/1925720_The_Formation_of_Massive_Stars_from_Turbulent_Cores
- research.chalmers.se Chemodynamics in Star-Forming Molecular Clouds - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/522085/file/522085_Fulltext.pdf
- astro.princeton.edu arXiv:0707.3514 (astro-ph) Opens in a new window — https://www.astro.princeton.edu/~burrows/classes/514/papers/mckee.ostriker.0707.3514.pdf
- pure.rug.nl University of Groningen Early galaxy formation and its large-scale effects Dayal, Pratika; Ferrara, Andrea Opens in a new window — https://pure.rug.nl/ws/files/76262271/1_s2.0_S0370157318302266_main.pdf
- mdpi.com An Investigation of the Entropy Associated with a Collapsing Molecular Cloud - MDPI Opens in a new window — https://www.mdpi.com/2674-0346/4/1/1
- ned.ipac.caltech.edu Physical Processes in the Interstellar Medium Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept19/Klessen/paper.pdf
- mso.anu.edu.au the Star Formation Rate, Stellar Clustering, and the Initial Mass Function - Research School of Astronomy & Astrophysics Opens in a new window — https://www.mso.anu.edu.au/~krumholz/publications/2014/krumholz14c.pdf
- scholar.google.com ‪Eve Ostriker‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=-BkjykAAAAAJ&hl=en
- scispace.com (PDF) Theory of Star Formation (2007) | Christopher F. McKee | 2882 Citations - SciSpace Opens in a new window — https://scispace.com/papers/theory-of-star-formation-sol2jzngnw
- prl.res.in Manash Samal - Physical Research Laboratory Opens in a new window — https://www.prl.res.in/~manash/res_int.html
- academic.oup.com Self-initiated star formation, the B–ρ relation, ambipolar diffusion, and other unnecessary controversies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/546/3/staf2265/66138273/staf2265.pdf
- pmc.ncbi.nlm.nih.gov An early transition to magnetic supercriticality in star formation - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC8732270/
- cambridge.org Radiation pressure in massive star formation | Proceedings of the International Astronomical Union - Cambridge University Press & Assessment Opens in a new window — https://www.cambridge.org/core/journals/proceedings-of-the-international-astronomical-union/article/radiation-pressure-in-massive-star-formation/42E0C648571D03B16F46285C8B00EEFC
- arxiv.org Magnetic Field Alignment of Young Stellar Object Motions in Nearby Star-Forming Regions Opens in a new window — https://arxiv.org/html/2606.19094v1
- academic.oup.com Self-initiated star formation, the B–ρ relation, ambipolar diffusion, and other unnecessary controversies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/546/3/staf2265/8405683
- academic.oup.com Molecular cloud regulated star formation in galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/376/4/1588/1014458
- pubs.aip.org Star Formation in Molecular Clouds Opens in a new window — https://pubs.aip.org/aip/acp/article-pdf/1386/1/9/11397971/9_1_online.pdf
- ned.ipac.caltech.edu Molecules in Galaxies - NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept07/Omont/paper.pdf
- arxiv.org Intermediate-Mass Black Holes in Star Clusters and Dwarf Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2311.12118v4
- pure.mpg.de arXiv:1403.0677v3 [astro-ph.HE] 27 May 2014 - MPG.PuRe Opens in a new window — https://pure.mpg.de/rest/items/item_2060754_3/component/file_2060753/content
- indico.cern.ch EuCAPT - Indico Opens in a new window — https://indico.cern.ch/event/1082310/attachments/2324519/3959079/Eucapt_White_Paper.pdf
- db-thueringen.de Investigation of Class I jets with SOFIA Opens in a new window — https://www.db-thueringen.de/servlets/MCRFileNodeServlet/dbt_derivate_00053840/disssperling.pdf
- oamonitor.ireland.openaire.eu Formation of star clusters: Models and simulations Opens in a new window — https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.1017%2Fs1743921316007390
- arxiv.org ALMA-IMF - arXiv Opens in a new window — https://arxiv.org/html/2604.14875v2
- imprs-astro.mpg.de Modelling the interaction of X-rays with the Interstellar Medium - IMPRS on Astrophysics Opens in a new window — https://www.imprs-astro.mpg.de/sites/default/files/molaro_margherita.pdf
- archiv.ub.uni-heidelberg.de Gensior_PhD_thesis_pub.pdf - Heidelberg University Opens in a new window — https://archiv.ub.uni-heidelberg.de/volltextserver/30269/1/Gensior_PhD_thesis_pub.pdf
- researchgate.net (PDF) Theory of Star Formation - ResearchGate Opens in a new window — https://www.researchgate.net/publication/1757095_Theory_of_Star_Formation
- arxiv.org arXiv:0906.4452v1 [astro-ph.GA] 24 Jun 2009 Opens in a new window — https://arxiv.org/pdf/0906.4452
- elearning.unimib.it Lecture notes on black hole binary astrophysics - e-Learning - UNIMIB Opens in a new window — https://elearning.unimib.it/pluginfile.php/1387578/mod_resource/content/1/Notes%20on%20BH%20astrophysics.pdf
- arxiv.org Non-linear Dynamical Stability of Magnetic Polytropes - arXiv Opens in a new window — https://arxiv.org/pdf/2606.00493
- explore.openaire.eu Magnetic field alignment in low-mass molecular clouds: the role of Opens in a new window — https://explore.openaire.eu/search/result?pid=10.1093/mnras/stae453
- academic.oup.com On the birthrates of Galactic neutron stars - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/391/4/2009/1747996
- ned.ipac.caltech.edu Star Formation in Molecular Clouds - NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept10/Krumholz/paper.pdf
- research.chalmers.se The Dynamics of Star Cluster Formation - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/518158/file/518158_Fulltext.pdf
- wise-obs.tau.ac.il Theory of Star Formation Opens in a new window — http://wise-obs.tau.ac.il/~sara/ostriker-mckee.pdf
- asd.gsfc.nasa.gov Heating Hot Atmospheres with Active Galactic Nuclei - Astrophysics Science Division Opens in a new window — https://asd.gsfc.nasa.gov/archive/ixo/decadal_references/DecadalReferencePapers/14_McNamara2007.pdf
- asd.gsfc.nasa.gov The Search for the Missing Baryons at Low Redshift - NASA Opens in a new window — https://asd.gsfc.nasa.gov/archive/ixo/decadal_references/DecadalReferencePapers/21_Bregman2007.pdf%20.pdf
- scispace.com Statistical Properties of Exoplanets - SciSpace Opens in a new window — https://scispace.com/pdf/statistical-properties-of-exoplanets-1hs09lq39f.pdf
- www2.ess.ucla.edu Irregular Satellites of the Planets: Products of Capture in the Early Solar System - UCLA Opens in a new window — http://www2.ess.ucla.edu/~jewitt/papers/2007/JH07.pdf
- user.astro.columbia.edu Relativistic X-Ray Lines from the Inner Accretion Disks Around Black Holes - Columbia Astronomy Opens in a new window — http://user.astro.columbia.edu/~jules/W3273/FeKalphaLines.pdf
- researchgate.net (PDF) Circumbinary Accretion: From Binary Stars to Massive Binary Black Holes Opens in a new window — https://www.researchgate.net/publication/371736572_Circumbinary_Accretion_From_Binary_Stars_to_Massive_Binary_Black_Holes
- cambridge.org References - Introduction to the Interstellar Medium Opens in a new window — https://www.cambridge.org/core/books/introduction-to-the-interstellar-medium/references/6237FD4C146E8C55EE127A327DA88B51
- scirp.org McKee, C.F. and Ostriker, E.C. (2007) Theory of Star Formation. Annual Review of Astronomy and Astrophysics, 45, 565-687. - References - Scirp.org. Opens in a new window — https://www.scirp.org/reference/referencespapers?referenceid=1337413
- astro.sunysb.edu Theory of Star Formation - Stony Brook Astronomy Opens in a new window — https://www.astro.sunysb.edu/fwalter/PHY688/McKee_annurev.astro.45.051806.110602.pdf
- biarjournal.com Gravitational Collapse of Solar Nebulae and the Processes of Star Formation - (BIAR) Journal Opens in a new window — https://biarjournal.com/index.php/bioex/article/download/1097/1091
- ned.ipac.caltech.edu initial mass function and star formation - Galaxy Formation - Joseph Silk et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept13/Silk/Silk2.html
- arxiv.org [astro-ph/0505177] A General Theory of Turbulence-Regulated Star Formation, From Spirals to ULIRGs - arXiv Opens in a new window — https://arxiv.org/abs/astro-ph/0505177
- scholar.google.com ‪Mark Krumholz‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=F8WzpaMAAAAJ&hl=en
- jkess.org Global Star Formation Efficiency of Local Galaxies - :: Journal of the Korean earth science society :: Opens in a new window — http://jkess.org/journal/article.php?code=12090
- scholar.google.com ‪Jonathan C. Tan‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=WOiGJ1gAAAAJ&hl=en
- arxiv.org arXiv:1206.1444v1 [astro-ph.SR] 7 Jun 2012 Opens in a new window — https://arxiv.org/pdf/1206.1444
- th.nao.ac.jp Dense molecular cloud cores as a source of micrometer-sized grains in galaxies Opens in a new window — http://th.nao.ac.jp/MEMBER/nozawa/papers/thirdforth/Hirashita2014.pdf
- edoc.ub.uni-muenchen.de The Clump Mass Function of the Dense Clouds in the Carina Nebula Opens in a new window — https://edoc.ub.uni-muenchen.de/16064/1/Pekruhl_Stephanie.pdf

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

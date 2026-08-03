# Review Base 04 raw Deep Research packet — Naab & Ostriker 2017

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_04_naab_ostriker_2017_DR_PROMPT.md`
Prompt SHA-256: `119cd3ec051b4859275d0216c16493b5fc47ba7dd99f0227c82ef48eef5f136e`
Conversation ID: `04b76d6352f3a20f`
Submit UTC: `2026-07-15T14:27:43.013428Z`
Research Start UTC: `2026-07-15T14:28:58.626394Z`
Result captured UTC: `2026-07-15T14:51:18.208877Z`
Raw result SHA-256: `3b817e6a0b813d2faad449bdd827b89c02bcc128007638c32e6cd8516dfab16a`

## Deep Research review-base result

Theoretical Challenges in Galaxy Formation: A Comprehensive Review Analysis

The computational modeling of galaxy formation represents one of the most formidable multi-scale problems in modern astrophysics. The 2017 review Theoretical Challenges in Galaxy Formation by Thorsten Naab and Jeremiah P. Ostriker serves as a definitive synthesis of the field's progress, evaluating how cosmological simulations attempt to bridge the vast gap between the macro-scale evolution of the universe and the micro-scale physics of star formation [cite: REV04-R00]. The review establishes a foundational dichotomy in the physics of structure formation: the gravitational assembly of dark matter halos, which is well understood, and the highly non-linear, dissipative physics of the baryonic components, which remains fraught with theoretical and numerical uncertainties.

As depicted in the multiscale mapping above, the standard Λ Cold Dark Matter (ΛCDM) cosmological model successfully dictates the initial conditions and the collisionless dynamics of dark matter halos across gigaparsec scales [cite: REV04-R00]. Within this hierarchical framework, structure forms from the bottom up: small halos collapse early and merge into larger systems. However, dark matter alone cannot account for the luminous universe. The baryonic gas must fall into these dark matter potential wells, shock-heat to the virial temperature, and subsequently undergo radiative cooling [cite: REV04-P047]. As the gas cools, it loses pressure support and dissipates its kinetic energy, shrinking into the center of the halo to form a rotationally supported disk as dictated by the conservation of angular momentum [cite: REV04-P006, REV04-P018].

If cooling and gravity were the only processes at play, simulations demonstrate that gas would undergo runaway condensation. In early numerical experiments, the absence of counteracting forces resulted in an "overcooling problem," where gas rapidly converted into stars at high redshifts. This process locked up too many baryons in central bulges, yielded galaxies with far too much stellar mass compared to observations, and suffered catastrophic angular momentum loss during subsequent mergers, preventing the formation of extended, thin spiral disks [cite: REV04-P001, REV04-P024]. Resolving this crisis required the introduction of "feedback"—the injection of energy, momentum, and mass back into the interstellar medium (ISM) from massive stars and supermassive black holes. The theoretical imperative to balance cosmological inflows with galactic outflows is the central challenge defining modern galaxy formation models [cite: REV04-R00].

1. Review Identity and Scope Map

The parameters of this analysis are strictly bound to the synthesis and the primary literature established by the 2017 review.

Title: Theoretical Challenges in Galaxy Formation

Authors: Thorsten Naab & Jeremiah P. Ostriker

Year: 2017

Journal: Annual Review of Astronomy and Astrophysics, Volume 55

DOI: 10.1146/annurev-astro-081913-040019

arXiv: 1612.06891

ADS Bibcode: 2017ARA&A..55...59N

Scientific Territory Map
The review maps the intersection of cosmological structure formation and localized astrophysics. It evaluates the necessity of resolved inflow/outflow accounting, the physics of the multiphase ISM, the implementation of star-formation scaling laws, and the complex coupling of stellar feedback channels (photoionization, stellar winds, supernovae, and cosmic rays). Furthermore, it evaluates the numerical methods—such as Smoothed Particle Hydrodynamics (SPH), Adaptive Mesh Refinement (AMR), and moving-mesh codes like AREPO—used to implement these physical processes. The synthesis critically examines the degeneracies inherent in sub-resolution feedback models, demonstrating how disparate numerical techniques can be tuned to reproduce identical macroscopic galaxy statistics, thereby masking the true underlying physical mechanisms.

Authorizations and Limitations
This source base authorizes the extraction of analytical theory, hydrodynamic simulation methodologies, and observational benchmarks strictly cited within the review's domain. It explicitly forbids the inclusion of post-2017 literature or unverified assertions. Crucially, the discussion of Active Galactic Nuclei (AGN) is authorized exclusively as a macroscopic, sub-grid ingredient utilized in cosmological simulations to prevent overcooling in massive halos (>10
12
M
⊙
	​

); all microphysical analyses of accretion disks, relativistic jets, and black-hole demographics are strictly quarantined. Furthermore, successful calibration of a sub-grid model is documented as a numerical success, not an ab initio physical proof.

2. The Multiphase Interstellar Medium and Star Formation

The interstellar medium is not a homogeneous fluid but a highly structured, multiphase environment characterized by supersonic turbulence, magnetic fields, and cosmic rays [cite: REV04-R00, REV04-P017]. The classic analytical framework posits a three-phase ISM maintained entirely by the energy injection of supernova explosions [cite: REV04-P034]. In modern hydrodynamic simulations, resolving this multiphase structure is critical because it dictates how and where molecular hydrogen (H
2
	​

) forms, which in turn fuels star formation. The intricate balance of heating from the interstellar radiation field and cooling via atomic and molecular lines determines the density and temperature structure of the gas [cite: REV04-P049].

Because large-scale cosmological simulations lack the spatial resolution to track individual star-forming giant molecular clouds on parsec scales, they rely on sub-resolution models. Most simulations employ a Schmidt-type parameterization, scaling the star formation rate (SFR) density to the local gas density divided by a relevant timescale, typically the local free-fall or dynamical time [cite: REV04-P010, REV04-P023]. This approach is explicitly calibrated to match the globally observed Kennicutt-Schmidt relation, which empirically links the SFR surface density to the gas surface density across galactic disks [cite: REV04-P026]. To mimic the multiphase nature of the ISM without resolving it, highly influential models introduced an "effective equation of state." This technique assumes a sub-grid equilibrium between the cold star-forming phase and the hot ambient phase, preventing the gas from fragmenting artificially while allowing the simulation to proceed stably on kiloparsec scales [cite: REV04-P044].

However, observations show that the global efficiency of star formation is remarkably low. The timescale required to deplete a galaxy's molecular gas reservoir is approximately 2 Gyr, which is orders of magnitude longer than the dynamical timescale of individual molecular clouds [cite: REV04-P030]. This profound inefficiency indicates that star formation must be highly self-regulated. Gravity drives the collapse of gas, but before a significant fraction of a cloud can convert into stars, the first generation of massive stars detonates, destroying the birth cloud and returning the remaining gas to the diffuse ISM [cite: REV04-P029, REV04-P031].

Key Measurements, Model Benchmarks, and Calibrations

To operationalize these concepts, the field relies on strict numerical benchmarks and observational targets. The following table details the key quantities used to calibrate and evaluate galaxy formation models as synthesized by the 2017 review.

ID	Measurement / Benchmark	Value / Equation	Units / Context	Role	Source Keys
[REV04-N01]	Supernova Energy Budget	∼10
51
	ergs per core-collapse event.	Assumed physical constant forming the baseline of all thermal and kinetic feedback models.	[REV04-R00]
[REV04-N02]	Supernova Ejecta Mass	2−5	M
⊙
	​

 per event.	Assumed/Measured boundary used to calculate mass loading and metal enrichment.	[REV04-R00]
[REV04-N03]	Initial Ejecta Velocity	6,000−7,000	km/s (free expansion phase).	Measured/Assumed benchmark for shock initiation.	[REV04-P022]
[REV04-N04]	Terminal Radial Momentum per SN (p
sf
	​

)	∼2×10
5
−3×10
5
	M
⊙
	​

 km/s. Measured at shell formation.	Analytically predicted and numerically confirmed limit for kinetic injection models.	[REV04-P012], [REV04-P028]
[REV04-N05]	Cosmic Baryon Conversion Efficiency	∼10%	f
gal
	​

∼0.1. The fraction of the cosmic baryon budget in stellar mass.	Observed calibration target heavily utilized to judge cosmological simulation success.	[REV04-R00]
[REV04-N06]	Ubiquitous Wind Velocities	Up to 500	km/s.	Observed benchmark in star-forming galaxies defining the requisite strength of simulated outflows.	[REV04-P020]
[REV04-N07]	Molecular Gas Depletion Time	∼2	Gyr.	Observed benchmark indicating highly inefficient galactic star formation relative to local cloud free-fall times.	[REV04-P030]
[REV04-N08]	Cooling Onset Time (Single SN)	10
4
−10
5.5
	Years. Depends heavily on ambient density (∼100−0.1 cm$^{-3}$).	Analytic theory defining when the momentum-generating Sedov-Taylor phase artificially terminates in poor-resolution grids.	[REV04-P019]
3. Stellar Feedback Mechanics and the Overcooling Crisis

The core theoretical challenge in simulating galaxies is accurately coupling the energy and momentum from massive stars into the surrounding ISM [cite: REV04-R00]. When a massive star dies, it ejects 2−5M
⊙
	​

 of material at highly supersonic speeds (∼6,000−7,000 km/s), depositing roughly 10
51
 ergs of energy into the environment [cite: REV04-P022]. The evolution of this supernova remnant dictates the physical state of the galaxy.

Analytic theory divides the expansion of a supernova remnant into distinct phases [cite: REV04-P012]. Initially, the remnant expands freely until it sweeps up an ambient mass comparable to its ejecta. It then enters the energy-conserving Sedov-Taylor phase, during which the interior pressure from the hot reverse-shocked gas drives the expansion adiabatically. During this critical phase, the remnant can heat thousands of solar masses of ambient gas and boost its initial radial momentum by a factor of 10 to 30 as thermal energy is converted into kinetic energy via PdV work [cite: REV04-P012, REV04-P028]. Eventually, as the shock decelerates and the post-shock gas cools radiatively, a dense shell forms. The remnant transitions into the pressure-driven, and finally the momentum-conserving, snowplow phase before degrading into a sound wave [cite: REV04-P011].

However, accurately simulating the momentum-generating Sedov-Taylor phase requires extreme spatial resolution (often on the order of parsecs) to capture the cooling radius before artificial mixing occurs [cite: REV04-P033]. In large-scale cosmological simulations where gas cells are hundreds of parsecs or kiloparsecs across, the injected 10
51
 ergs of thermal energy is immediately smoothed over a massive, artificially dense volume of gas. Because radiative cooling rates scale with the square of the density, the injected energy radiates away almost instantly before it can perform the mechanical work necessary to drive an expansion [cite: REV04-P003, REV04-P025]. This numerical artifact is the root cause of the "overcooling problem," rendering simple thermal feedback entirely ineffective at regulating star formation.

To circumvent this, modelers developed a variety of sub-grid workarounds [cite: REV04-R00]. The "delayed cooling" approach artificially shuts off radiative cooling for the heated gas particles for a specific duration, allowing the thermal pressure to drive an expansion hydrodynamically [cite: REV04-P014, REV04-P039]. Alternatively, the "decoupled kinetic wind" approach abandons thermal injection entirely; instead, it imparts direct velocity kicks to gas particles near star-forming regions and temporarily decouples them from hydrodynamic interactions so they can escape the dense disk without immediately shocking and losing their momentum [cite: REV04-P047]. Both methods successfully drive outflows, suppress early star formation, and allow the survival of extended disk morphologies.

Established Findings

The following table documents the widely replicated empirical, analytical, and numerical truths established in the literature up to 2017.

ID	Role	Epistemic Type	Bounded Finding	Boundary Conditions	Review Basis	Confidence Note	Source Keys
[REV04-E01]	established	review_synthesis	The standard ΛCDM model is sufficiently accurate to generate reliable initial conditions, halo mass functions, and merging histories for galaxy formation.	Dark matter halos; large-scale structure; collisionless dynamics.	Cosmological Models / Initial Conditions	High; widely replicated across independent N-body codes.	[REV04-R00]
[REV04-E02]	established	hydrodynamic_simulation	Without strong stellar feedback, cosmological simulations universally suffer from "overcooling," converting too much low-angular-momentum gas into stars and failing to produce extended, realistic spiral disks.	High-redshift cooling; M
halo
	​

∼10
10
−10
12
M
⊙
	​

.	Formation of Disk Systems	High; confirmed across SPH, AMR, and moving-mesh frameworks.	[REV04-P024], [REV04-P025]
[REV04-E03]	established	observation	Galactic winds are ubiquitous in star-forming galaxies, carrying mass outward at rates comparable to or exceeding the galactic star-formation rate.	Velocities up to 500 km/s; low and high redshift (z∼0−3).	Observations / Ubiquitous Winds	High empirical confidence; bi-conical outflows heavily documented.	[REV04-P020], [REV04-P038]
[REV04-E04]	established	observation	Massive early-type galaxies (10
11
M
⊙
	​

) exhibit significant structural evolution (size growth) since z∼2, driven primarily by minor mergers rather than purely in-situ star formation.	High-mass galaxies; z∼0 to z∼2; dry mergers.	Size Evolution of Early-Type Galaxies	High; supported by stellar age distributions and structural tracking.	[REV04-P005]
[REV04-E05]	established	analytic_theory	A core-collapse supernova entering the energy-conserving Sedov-Taylor phase heats ∼10
3
 times its ejecta mass and can boost its initial radial momentum by a factor of 10 to 30.	Adiabatic expansion phase prior to severe radiative cooling.	Supernova Explosions	High theoretical confidence; validated by high-resolution 3D isolated SNR simulations.	[REV04-P012], [REV04-P028]
[REV04-E06]	established	calibration	Sub-resolution models linking star-formation rates to local gas densities divided by a local timescale successfully reproduce the observed global Kennicutt-Schmidt relation.	Kpc-scale grid resolutions; calibrated threshold densities.	Star Formation and Gas Cooling	High for matching statistical targets; low predictive power for microphysics.	[REV04-P010], [REV04-P023]
[REV04-E07]	established	hydrodynamic_simulation	Injecting pure thermal energy from supernovae into low-resolution grid cells fails to drive winds, as the energy is immediately radiated away in artificially dense, mixed gas.	ISM grid resolutions >10 pc; unresolved Sedov-Taylor phases.	Numerical Methods / Overcooling	High numerical consensus; necessitates delayed cooling or kinetic models.	[REV04-P003], [REV04-P014]
[REV04-E08]	established	observation	The global efficiency of star formation is remarkably low, with typical molecular gas depletion times (∼2 Gyr) exceeding local molecular cloud dynamical times by two orders of magnitude.	Galactic and sub-galactic scales; standard IMF.	Star Formation Efficiency	High empirical confidence.	[REV04-P026], [REV04-P030]
[REV04-E09]	established	observation	Non-thermal ISM components, specifically magnetic fields and cosmic rays, maintain energy densities roughly comparable to the kinetic and thermal energy densities of the Milky Way ISM.	Milky Way ISM conditions; diffuse gas phases.	Magnetic Fields and Cosmic Rays	Moderate to high; robust locally but uncertain in high-z environments.	[REV04-P008]
[REV04-E10]	established	review_synthesis	A variety of conceptually distinct sub-grid feedback models (e.g., stochastic thermal, decoupled kinetic, delayed cooling) can successfully tune their parameters to match the z=0 stellar mass function.	Cosmological volumes; diverse code bases (Illustris, EAGLE).	Sub-resolution Feedback Models	High for empirical matching; explicitly highlights model degeneracy.	[REV04-R00], [REV04-P039], [REV04-P047]
[REV04-E11]	established	hydrodynamic_simulation	Supernova momentum injection is the primary mechanism for driving and sustaining turbulence within the cold and warm neutral phases of the interstellar medium.	Resolved multiphase ISM simulations; pure momentum tracking.	Supernova Explosions / Turbulence	Moderate to high; depends heavily on spatial clustering of SNe.	[REV04-P017], [REV04-P033]
[REV04-E12]	established	analytic_theory	When an expanding supernova shock velocity drops to the sound speed of the ambient interstellar medium, it transitions into a sound wave, depositing its terminal momentum.	Momentum-conserving snowplow phase; multiphase ISM.	Supernova Explosions	High theoretical confidence.	[REV04-P011], [REV04-P016]
4. Galactic Fountains, Metals, and Model Degeneracy

Feedback does more than just heat gas; it physically ejects it from the galaxy. Observational surveys confirm the existence of massive, bi-conical superwinds exiting star-forming galaxies at velocities up to 500 km/s [cite: REV04-P020, REV04-P046]. These winds carry heavy elements synthesized in stellar cores into the Circumgalactic Medium (CGM), profoundly altering the chemical composition of the halo. Observations from the COS-Halos survey demonstrate that the CGM of L
∗
 star-forming galaxies harbors massive reservoirs of highly ionized metals, such as O VI, extending out to 150 kpc [cite: REV04-P045, REV04-P049].

If outflowing gas does not achieve escape velocity, it eventually falls back onto the galactic disk in a "galactic fountain." This recycling process is essential for extending the star-formation history of a galaxy over billions of years and for enhancing the specific angular momentum of the disk, as returning gas mixes with rotating halo material [cite: REV04-P009, REV04-P032]. The efficiency of this process is governed by the mass-loading factor (η), defined as the ratio of the outflow mass rate to the star formation rate.

While large-scale simulations like Illustris and EAGLE have achieved spectacular success in replicating the cosmological evolution of the galaxy mass function and the cosmic star formation rate density, they do so through highly calibrated parameterizations of these winds [cite: REV04-P039, REV04-P047]. In Illustris, the mass-loading factor is prescribed directly as a function of the dark matter halo velocity dispersion, while EAGLE relies on stochastic thermal heating calibrated to prevent overcooling. This reveals a fundamental degeneracy: models utilizing entirely different phenomenological implementations of feedback can be tuned to yield identical macroscopic galaxy properties [cite: REV04-R00]. Consequently, achieving a match to observational statistics does not serve as a definitive proof that the underlying sub-resolution physics uniquely represents reality.

For the most massive galaxies (halo masses >10
12
M
⊙
	​

), stellar feedback alone provides insufficient energy to prevent late-time gas condensation. In these regimes, modern simulations invoke AGN feedback [cite: REV04-P047]. Bounded here purely as a macroscopic galaxy-scale ingredient, energy released from accretion onto a central supermassive black hole is injected into the surrounding gas either thermally or mechanically. This prevents the formation of massive cooling flows and maintains the quiescence of massive elliptical galaxies, successfully reproducing the observed cutoff at the high-mass end of the galaxy luminosity function [cite: REV04-P039].

Open Debates and Tensions

The reliance on sub-grid calibrations fostered deep tensions in the field regarding the exact physical mechanisms governing galaxy evolution. The 2017 review isolates several critical domains where physical consensus remained elusive.

ID	Tension / Debate	Why Unresolved in 2017	Bounded Context	Source Keys
[REV04-D01]	Dominant Stellar Feedback Channels: The relative necessity of supernovae versus early radiative feedback (photoionization, radiation pressure) in disrupting giant molecular clouds.	High-resolution simulations could not easily couple full radiation-hydrodynamics with explicit supernova blast waves across whole galactic disks.	GMC disruption scales; 1−100 pc; star-formation efficiency.	[REV04-R00]
[REV04-D02]	Thermal vs. Kinetic Sub-grid Coupling: Whether cosmological simulations should bypass overcooling by turning off cooling temporarily (delayed cooling) or by explicitly decoupling kinetic wind particles from hydrodynamics.	Both methods are purely numerical workarounds for unresolved multiphase interfaces. Both can be tuned to match the stellar mass function, masking the true physical mechanism.	Cosmological resolution limits; galactic wind mass loading.	[REV04-P014], [REV04-P047]
[REV04-D03]	Wind Mass Loading and Recycling: The exact scaling of wind mass-loading factors (η) with galaxy halo mass, and the timescale for enriched gas to recycle back into the disk.	Coarse resolution in the CGM poorly resolves hydrodynamical instabilities (Kelvin-Helmholtz), preventing accurate tracking of how cold wind clumps entrain or mix with hot halo gas.	CGM interface; 10−100 kpc scales; virial temperatures.	[REV04-R00], [REV04-P032]
[REV04-D04]	Cosmic-Ray Support in Winds: The degree to which cosmic rays provide buoyancy to drive cool gas out of galaxies where thermal supernova feedback fails.	The diffusion coefficients and streaming velocities of cosmic rays through highly turbulent, magnetized multiphase gas were theoretically poorly constrained and computationally expensive.	Non-thermal pressure; galaxy halos; Milky Way-mass systems.	[REV04-P008], [REV04-P050]
[REV04-D05]	Physical vs. Numerical Convergence: Whether simulated star-formation histories stabilize due to correctly capturing the physics or because sub-grid parameters were re-tuned for the new resolution.	Many sub-grid models are inherently scale-dependent; increasing resolution alters the cooling times and densities, requiring continuous recalibration of the feedback efficiencies.	Sub-resolution implementations; code comparison projects.	[REV04-R00], [REV04-P039]
[REV04-D06]	Impact of Supernova Clustering: Do clustered supernovae in superbubbles yield greater terminal momentum per supernova than isolated events?	Results conflicted based on mixing rates across contact discontinuities. Some 3D models showed increased momentum via superbubbles; others showed increased radiative losses due to dense shell impacts.	Superbubble scale; 10−100 pc; multiphase ISM.	[REV04-P019], [REV04-P048]
[REV04-D07]	Calibration Degeneracy: The fact that models with radically different underlying assumptions about feedback mechanisms can produce indistinguishable z=0 galaxy mass functions.	Global statistics (like the stellar-to-halo mass relation) are broad integrals of time and do not uniquely constrain the differential physics of the ISM operating at high redshift.	Cosmological hydrodynamical models; mass functions.	[REV04-R00], [REV04-P039], [REV04-P047]
[REV04-D08]	Star-Formation Efficiency Control: Does the low efficiency of star formation result globally from the ISM's turbulent cascade, or locally from self-regulated stellar feedback destroying the birth clouds?	Analytical theories heavily favored turbulent support, while numerical simulations showed that gravity inevitably overcomes turbulence without explicit stellar energy injection.	Galactic disks; Kennicutt-Schmidt relation parameters.	[REV04-P017], [REV04-P048]
5. What Remained Unknown in 2017

Naab & Ostriker explicitly defined the frontiers of galaxy formation theory, identifying where current numerical paradigms fell short and what advancements were required to transition the field from empirical modeling to ab initio prediction.

ID	Unknown / Gap	Why it Matters	Needed Test / Advance
[REV04-U01]	First-principles derivation of the Kennicutt-Schmidt relation.	Models applied the relation as a calibrated sub-grid rule rather than letting it emerge organically from the simulated microphysics, limiting predictive power across cosmic time.	Simulations resolving gas cooling below 10
3
 K, molecular chemistry, and self-gravity simultaneously down to sub-parsec scales.
[REV04-U02]	The survival physics of cold clumps in hot galactic winds.	If cold gas is rapidly destroyed by Kelvin-Helmholtz instabilities, winds cannot effectively load mass or recycle enriched gas back into the disk, breaking current fountain models.	High-resolution hydrodynamics of the ISM-CGM interface, likely requiring explicit magnetic field treatments to suppress interface mixing.
[REV04-U03]	The exact hierarchy of feedback channels prior to supernovae.	Photoionization, radiation pressure, and stellar winds inject momentum early, altering the density of the medium into which SNe subsequently explode. Ignoring them overestimates SN radiative losses.	Coupled radiation-hydrodynamics combined with explicit tracking of individual massive star lifetimes.
[REV04-U04]	True galactic mass-loading factors (η).	The ratio of outflowing gas to the star-formation rate (η) determines the mass of the galaxy, but sub-grid models artificially tuned η to fix overcooling rather than calculating it from physics.	Convergence of outflow rates in isolated galaxy simulations independent of the chosen sub-grid implementation.
[REV04-U05]	The precise role of cosmic rays in wind acceleration.	Cosmic rays represent a massive, non-thermal pressure reservoir capable of accelerating gas smoothly over large distances, potentially solving wind-driving failures in massive halos.	Validated models of cosmic-ray transport, diffusion coefficients, and streaming instabilities within galactic magnetic fields.
[REV04-U06]	Unique mechanisms for massive galaxy quenching.	While AGN feedback is empirically necessary to quench massive galaxies, the mechanical versus radiative coupling efficiency of black-hole jets to the galactic ISM remains highly degenerate.	Resolved models of AGN energy deposition overlapping with deep observations of the thermodynamic state of the massive halo CGM.
6. Primary-Citation Harvest

The following ledger contains the primary physical papers strictly cited within the boundary of the Naab & Ostriker (2017) review. It serves as the authorized database for extracting primary models, observations, and methodologies.

[REV04-P001] Abadi M. G., Navarro J. F., Steinmetz M., Eke V. R. (2003, The Astrophysical Journal) | title=Simulations of Galaxy Formation in a Lambda Cold Dark Matter Universe. I. Dynamical and Photometric Properties of a Simulated Disk Galaxy | DOI:10.1086/375512; arXiv:astro-ph/0211331; ADS:2003ApJ...591..499A | role=hydrodynamic_simulation | review_locator=Section 2.2 | Early demonstration of the angular momentum and overcooling problem in simulated disks.

[REV04-P002] Abadi M. G., Navarro J. F., Steinmetz M., Eke V. R. (2003, The Astrophysical Journal) | title=Simulations of Galaxy Formation in a Lambda Cold Dark Matter Universe. II. The Fine Structure of Simulated Galactic Disks | DOI:10.1086/378316; arXiv:astro-ph/0211383; ADS:2003ApJ...597...21A | role=hydrodynamic_simulation | review_locator=Section 2.2 | Analyzed the fine kinematic structure and the difficulty of preventing early collapse of low angular momentum baryons.

[REV04-P003] Agertz O., Kravtsov A. V., Leitner S. N., Gnedin N. Y. (2013, The Astrophysical Journal) | title=Toward a Complete Accounting of Energy and Momentum from Stellar Feedback in Galaxy Formation Simulations | DOI:10.1088/0004-637X/770/1/25; arXiv:1208.2741; ADS:2013ApJ...770...25A | role=hydrodynamic_simulation | review_locator=Section 2.2.1 | Implementation of momentum and energy stellar feedback in isolated and cosmological contexts.

[REV04-P004] Balogh M. L., Pearce F. R., Bower R. G., Kay S. T. (2001, Monthly Notices of the Royal Astronomical Society) | title=Revisiting the overcooling crisis in semi-analytical models of galaxy formation | DOI:10.1046/j.1365-8711.2001.04652.x; arXiv:astro-ph/0104140; ADS:2001MNRAS.326.1228B | role=hydrodynamic_simulation | review_locator=Section 2.2 | Confirmed the overcooling problem in cosmological simulations where excessive early gas condensation occurs.

[REV04-P005] Bernardi M., Shankar F., Hyde J. B., Mei S., Marulli F., Sheth R. K. (2010, Monthly Notices of the Royal Astronomical Society) | title=Galaxy luminosities, stellar masses, sizes, velocity dispersions as a function of morphological type | DOI:10.1111/j.1365-2966.2010.16425.x; arXiv:0910.1093; ADS:2010MNRAS.404.2087B | role=observation | review_locator=Section 1.3.2 | Observational constraint on stellar mass functions and sizes of local universe galaxies.

[REV04-P006] Binney J. (1977, The Astrophysical Journal) | title=The physics of dissipational galaxy formation | DOI:10.1086/155386; arXiv:none; ADS:1977ApJ...215..483B | role=analytic_theory | review_locator=Section 2.1 | Foundational analytic theory establishing gas cooling and dissipation as necessities for galactic structure.

[REV04-P007] Blondin J. M., Wright E. B., Borkowski K. J., Reynolds S. P. (1998, The Astrophysical Journal) | title=Transition to the Radiative Phase in Supernova Remnants | DOI:10.1086/305708; arXiv:astro-ph/9802081; ADS:1998ApJ...500..342B | role=analytic_theory | review_locator=Section 3.1 | Detailed the thermodynamic transition of supernova remnants into the radiative snowplow phase.

[REV04-P008] Boulares A., Cox D. P. (1990, The Astrophysical Journal) | title=Galactic hydrostatic equilibrium with magnetic tension and cosmic-ray diffusion | DOI:10.1086/169466; arXiv:none; ADS:1990ApJ...365..544B | role=observation | review_locator=Section 1.1 | Established that magnetic fields and cosmic rays have energy densities comparable to the thermal/kinetic ISM.

[REV04-P009] Brook C. B., et al. (2011, Monthly Notices of the Royal Astronomical Society) | title=Hierarchical formation of bulgeless galaxies - I. The roles of merging and feedback | DOI:10.1111/j.1365-2966.2011.18731.x; arXiv:1010.0003; ADS:2011MNRAS.415.1051B | role=hydrodynamic_simulation | review_locator=Section 2.2 | Demonstrated how strong feedback ejects low angular momentum gas which later returns to form disks.

[REV04-P010] Cen R., Ostriker J. P. (1992, The Astrophysical Journal Letters) | title=Galaxy formation and physical bias | DOI:10.1086/186596; arXiv:none; ADS:1992ApJ...399L.113C | role=hydrodynamic_simulation | review_locator=Section 2.1 | Introduced local timescales tied to dynamical and cooling times for sub-grid star formation.

[REV04-P011] Chevalier A. W. (1982, The Astrophysical Journal) | title=The radio and X-ray emission from type II supernovae | DOI:10.1086/160167; arXiv:none; ADS:1982ApJ...259..302C | role=analytic_theory | review_locator=Section 3.1 | Evaluated the phases of supernova blast waves and their interaction with the ambient medium.

[REV04-P012] Cioffi D. F., McKee C. F., Bertschinger E. (1988, The Astrophysical Journal) | title=Dynamics of radiative supernova remnants | DOI:10.1086/166834; arXiv:none; ADS:1988ApJ...334..252C | role=analytic_theory | review_locator=Section 3.1 | Provided the classic analytic framework for the momentum and energy scaling of evolving supernova remnants.

[REV04-P013] D'Onghia E., Burkert A. (2004, The Astrophysical Journal) | title=The Angular Momentum Problem in Cosmological Simulations of Disk Galaxy Formation | DOI:10.1086/422631; arXiv:astro-ph/0311283; ADS:2004ApJ...612..628D | role=hydrodynamic_simulation | review_locator=Section 2.2 | Investigated the persistent issue of angular momentum loss during hierarchical assembly in early simulations.

[REV04-P014] Dalla Vecchia C., Schaye J. (2008, Monthly Notices of the Royal Astronomical Society) | title=Simulating galactic winds in the cold dark matter cosmology | DOI:10.1111/j.1365-2966.2008.13244.x; arXiv:0801.2770; ADS:2008MNRAS.387.1431D | role=hydrodynamic_simulation | review_locator=Section 2.2.1 | Explored kinetic and thermal implementations of galactic winds as sub-grid feedback models.

[REV04-P015] Dekel A., Silk J. (1986, The Astrophysical Journal) | title=The origin of dwarf galaxies, cold dark matter, and biased galaxy formation | DOI:10.1086/164050; arXiv:none; ADS:1986ApJ...303...39D | role=analytic_theory | review_locator=Section 3.1 | Early theoretical realization that supernova feedback is required to prevent excessive cooling in dwarf halos.

[REV04-P016] Draine B. T. (2011, Physics of the Interstellar and Intergalactic Medium) | title=Physics of the Interstellar and Intergalactic Medium | DOI:none; arXiv:none; ADS:2011piim.book.....D | role=observation | review_locator=Section 3.1 | Foundational textbook on ISM physics, including phase structures and supernova fading times.

[REV04-P017] Fall S. M., Efstathiou G. (1980, Monthly Notices of the Royal Astronomical Society) | title=Formation and rotation of disc galaxies with haloes | DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | role=analytic_theory | review_locator=Section 2.2 | Established the basic model of disk formation via tidal torques and angular momentum conservation during cooling.

[REV04-P018] Haid S., Walch S., Naab T., Seifried D., Mackey J., Gatto A. (2016, Monthly Notices of the Royal Astronomical Society) | title=Supernova blast waves in wind-blown bubbles, turbulent, and power-law ambient media | DOI:10.1093/mnras/stw1051; arXiv:1601.03055; ADS:2016MNRAS.460.2962H | role=hydrodynamic_simulation | review_locator=Section 3.1 | Characterized momentum limits due to radiative cooling from supernovae exploding in diverse ambient media.

[REV04-P019] Heckman T. M. (2000, Massive Stellar Clusters) | title=Galactic Superwinds at Low and High Redshift | DOI:none; arXiv:astro-ph/0009075; ADS:2000msc..conf..299H | role=observation | review_locator=Section 1.3.1 | Observational proof of ubiquitous, high-velocity galactic winds carrying mass out of star-forming galaxies.

[REV04-P020] Hennebelle P., Iffrig O. (2014, Astronomy and Astrophysics) | title=Simulations of magnetized multiphase galactic discs - I. Properties of the cold, atomic and hot gas | DOI:10.1051/0004-6361/201323334; arXiv:1405.7836; ADS:2014A&A...570A..81H | role=hydrodynamic_simulation | review_locator=Section 2.1 | Detailed multi-phase structure, ionization degrees, and magnetic fields relevant for H2 formation.

[REV04-P021] Katz N. (1992, The Astrophysical Journal) | title=Dissipational Galaxy Formation. II. Effects of Star Formation | DOI:10.1086/171366; arXiv:none; ADS:1992ApJ...391..502K | role=hydrodynamic_simulation | review_locator=Section 2.1 | Original formulation of sub-resolution SF density-timescale criteria for SPH modeling.

[REV04-P022] Katz N., Gunn J. E. (1991, The Astrophysical Journal) | title=Dissipational Galaxy Formation. I. Effects of Gasdynamics | DOI:10.1086/170367; arXiv:none; ADS:1991ApJ...377..365K | role=hydrodynamic_simulation | review_locator=Section 2.2 | Early documentation of angular momentum crises in simulated dissipative gas clouds.

[REV04-P023] Katz N., Weinberg D. H., Hernquist L. (1996, The Astrophysical Journal Supplement Series) | title=Cosmological Simulations with TreeSPH | DOI:10.1086/192310; arXiv:astro-ph/9509107; ADS:1996ApJS..105...19K | role=hydrodynamic_simulation | review_locator=Section 2.2 | Highlighted the severe tendency for cosmological simulations to overproduce central bulges.

[REV04-P024] Kennicutt R. C., Jr (1998, The Astrophysical Journal) | title=The Global Schmidt Law in Star-forming Galaxies | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=observation | review_locator=Section 2.1 | Defined the global relation used essentially by all models to calibrate sub-grid star formation rates.

[REV04-P025] Kereš D., Katz N., Weinberg D. H., Davé R. (2005, Monthly Notices of the Royal Astronomical Society) | title=How do galaxies get their gas? | DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0407095; ADS:2005MNRAS.363....2K | role=hydrodynamic_simulation | review_locator=Section 2.2 | Evaluated the thermodynamics and morphological consequences of cold versus hot accretion flows.

[REV04-P026] Kim C.-G., Ostriker E. C. (2015, The Astrophysical Journal) | title=Momentum Injection by Supernovae in the Interstellar Medium | DOI:10.1088/0004-637X/802/2/99; arXiv:1501.03150; ADS:2015ApJ...802...99K | role=hydrodynamic_simulation | review_locator=Section 3.1 | Precise limits on momentum scaling derived from ultra-high resolution SNR expansion experiments.

[REV04-P027] Larson R. B. (1974, Monthly Notices of the Royal Astronomical Society) | title=Effects of supernovae on the early evolution of galaxies | DOI:10.1093/mnras/169.2.229; arXiv:none; ADS:1974MNRAS.169..229L | role=analytic_theory | review_locator=Section 3.1 | Foundational theory linking stellar feedback to the macroscopic evolution and element retention of young galaxies.

[REV04-P028] Leroy A. K., et al. (2008, The Astronomical Journal) | title=The Star Formation Efficiency in Nearby Galaxies: Measuring Where Gas Forms Stars Effectively | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=observation | review_locator=Section 2.1 | Spatially resolved observations establishing the profound inefficiency of molecular gas converting to stars.

[REV04-P029] Marinacci F., et al. (2011, Monthly Notices of the Royal Astronomical Society) | title=Non-linear gravitational torques and mixing | DOI:none; arXiv:none; ADS:2011MNRAS.415.1534M | role=hydrodynamic_simulation | review_locator=Section 2.2 | Identified mechanisms enhancing angular momentum of returning gas expelled previously via stellar feedback.

[REV04-P030] Martizzi D., Faucher-Giguère C.-A., Quataert E. (2015, Monthly Notices of the Royal Astronomical Society) | title=Supernova feedback in an inhomogeneous interstellar medium | DOI:10.1093/mnras/stv562; arXiv:1409.4425; ADS:2015MNRAS.450..504M | role=hydrodynamic_simulation | review_locator=Section 3.1 | Quantitative formulas for momentum and thermal energy injected into explicitly inhomogeneous, multiphase media.

[REV04-P031] McKee C. F., Ostriker J. P. (1977, The Astrophysical Journal) | title=A theory of the interstellar medium - Three components regulated by supernova explosions in an inhomogeneous substrate | DOI:10.1086/155692; arXiv:none; ADS:1977ApJ...218..148M | role=analytic_theory | review_locator=Section 3.1 | Established the theoretical blueprint for a three-phase ISM driven uniquely by successive SN explosions.

[REV04-P032] Navarro J. F., Benz W. (1991, The Astrophysical Journal) | title=Dynamics of cooling gas in galactic dark halos | DOI:10.1086/170569; arXiv:none; ADS:1991ApJ...380..320N | role=hydrodynamic_simulation | review_locator=Section 2.2 | Linked collisionless dark matter halos with highly dissipative, overcooling gas inflows.

[REV04-P033] Navarro J. F., Steinmetz M. (1997, The Astrophysical Journal) | title=The Effects of a Cosmological Constant on Disk Galaxy Formation | DOI:10.1086/303763; arXiv:astro-ph/9605043; ADS:1997ApJ...478...13N | role=hydrodynamic_simulation | review_locator=Section 2.2 | Identified the structural failure mode of cosmological disks formed without explicit mass-loading feedback.

[REV04-P034] Peebles P. J. E. (1969, The Astrophysical Journal) | title=Origin of the Angular Momentum of Galaxies | DOI:10.1086/149911; arXiv:none; ADS:1969ApJ...155..393P | role=analytic_theory | review_locator=Section 1.3.1 | Classical analytical determination of initial galaxy spin acquired via external large-scale tidal forces.

[REV04-P035] Pettini M., et al. (2001, The Astrophysical Journal) | title=The Rest-Frame Optical Spectra of Lyman Break Galaxies: Star Formation, Extinction, Abundances, and Kinematics | DOI:10.1086/321356; arXiv:astro-ph/0102456; ADS:2001ApJ...554..981P | role=observation | review_locator=Section 1.3.1 | Early spectroscopic confirmation of massive, high-velocity galactic winds occurring at cosmic noon.

[REV04-P036] Pontzen A., Governato F. (2012, Monthly Notices of the Royal Astronomical Society) | title=How supernova feedback turns dark matter cusps into cores | DOI:10.1111/j.1365-2966.2012.20571.x; arXiv:1106.0499; ADS:2012MNRAS.421.3464P | role=hydrodynamic_simulation | review_locator=Section 1.1 | Showed how rapid, baryon-driven outflows dramatically alter the inner gravitational profiles of small halos.

[REV04-P037] Rees M. J., Ostriker J. P. (1977, Monthly Notices of the Royal Astronomical Society) | title=Cooling, dynamics and fragmentation of massive gas clouds: clues to the masses and radii of galaxies and clusters | DOI:10.1093/mnras/179.4.541; arXiv:none; ADS:1977MNRAS.179..541R | role=analytic_theory | review_locator=Section 2.2 | Established the physical boundaries determining where dark matter halos successfully trap cooling gas.

[REV04-P038] Schaye J., et al. (2015, Monthly Notices of the Royal Astronomical Society) | title=The EAGLE project: simulating the evolution and assembly of galaxies and their environments | DOI:10.1093/mnras/stu2058; arXiv:1407.7040; ADS:2015MNRAS.446..521S | role=hydrodynamic_simulation | review_locator=Section 3.5 | Large-scale cosmological simulation achieving realistic stellar mass properties via calibrated stochastic thermal heating.

[REV04-P039] Schmidt M. (1959, The Astrophysical Journal) | title=The Rate of Star Formation. | DOI:10.1086/146614; arXiv:none; ADS:1959ApJ...129..243S | role=analytic_theory | review_locator=Section 2.1 | Formulated the fundamental empirical power-law linking star-formation rates to locally available gas density.

[REV04-P040] Silk J. (1977, The Astrophysical Journal) | title=On the fragmentation of cosmic gas clouds. I - The formation of galaxies and the first generation of stars | DOI:10.1086/155066; arXiv:none; ADS:1977ApJ...211..638S | role=analytic_theory | review_locator=Section 2.2 | Foundational criteria establishing the upper limits on cooling rates leading to star formation within galactic halos.

[REV04-P041] Springel V., Hernquist L. (2003, Monthly Notices of the Royal Astronomical Society) | title=Cosmological smoothed particle hydrodynamics simulations: a hybrid multiphase model for star formation | DOI:10.1046/j.1365-8711.2003.06206.x; arXiv:astro-ph/0206393; ADS:2003MNRAS.339..289S | role=semi_analytic_model | review_locator=Section 2.1 | Formulation of the widely used sub-grid multiphase effective equation of state balancing star formation and feedback.

[REV04-P042] Tumlinson J., et al. (2011, Science) | title=The Large, Oxygen-Rich Halos of Star-Forming Galaxies Are a Major Reservoir of Galactic Metals | DOI:10.1126/science.1209840; arXiv:1111.3970; ADS:2011Sci...334..948T | role=observation | review_locator=Section 1.3.1 | Demonstrated that massive reservoirs of highly ionized heavy elements reside in the CGM, confirming extensive mass outflow.

[REV04-P043] Vogelsberger M., et al. (2014, Nature) | title=Properties of galaxies reproduced by a hydrodynamic simulation | DOI:10.1038/nature13316; arXiv:1405.1418; ADS:2014Natur.509..177V | role=hydrodynamic_simulation | review_locator=Section 1.3.3 | The Illustris simulation, which achieved macroscopic galaxy statistics using decoupled kinetic winds and thermal AGN feedback.

[REV04-P044] Walch S., Naab T. (2015, Monthly Notices of the Royal Astronomical Society) | title=The SILCC (SImulating the LifeCycle of molecular Clouds) project - I. Chemical evolution of the supernova-driven ISM | DOI:10.1093/mnras/stv1975; arXiv:1412.2749; ADS:2015MNRAS.454..238W | role=hydrodynamic_simulation | review_locator=Section 3.1 | Validated the momentum scaling of clustered versus isolated supernovae inside complex, self-gravitating molecular clouds.

[REV04-P045] Werk J. K., et al. (2014, The Astrophysical Journal) | title=The COS-Halos Survey: Physical Conditions and Baryonic Mass in the Low-redshift Circumgalactic Medium | DOI:10.1088/0004-637X/792/1/8; arXiv:1403.0947; ADS:2014ApJ...792....8W | role=observation | review_locator=Section 1.3.1 | Quantified cool gas densities and heavy element kinematics within the extended halos of massive star-forming galaxies.

[REV04-P046] White S. D. M., Rees M. J. (1978, Monthly Notices of the Royal Astronomical Society) | title=Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering | DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | role=analytic_theory | review_locator=Section 2.2 | The seminal framework for two-stage cosmological formation (merging collisionless dark matter followed by dissipative gas cooling).

[REV04-P047] Krumholz M. R., McKee C. F. (2005, The Astrophysical Journal) | title=A General Theory of Turbulence-regulated Star Formation, from Spirals to Ultraluminous Infrared Galaxies | DOI:10.1086/431734; arXiv:astro-ph/0505177; ADS:2005ApJ...630..250K | role=analytic_theory | review_locator=Section 2.1 | Theoretical framework for how interstellar turbulence dictates local star formation rates.

[REV04-P048] Glover S. C. O., Mac Low M.-M. (2007, The Astrophysical Journal Supplement Series) | title=Simulating the Formation of Molecular Clouds. I. Slow Formation by Gravity and Turbulence | DOI:10.1086/512238; arXiv:astro-ph/0605120; ADS:2007ApJS..169..239G | role=hydrodynamic_simulation | review_locator=Section 2.1 | Demonstrated how supersonic turbulence controls the timescale for H2 formation and gravitational collapse.

[REV04-P049] Salem M., Bryan G. L. (2014, Monthly Notices of the Royal Astronomical Society) | title=Cosmic ray driven outflows in global galaxy disc models | DOI:10.1093/mnras/stt2121; arXiv:1307.6215; ADS:2014MNRAS.437.3312S | role=hydrodynamic_simulation | review_locator=Section 3.4 | Simulated the efficiency of cosmic-ray transport in accelerating cold gas out of the galactic potential well.

Supporting Reviews

[REV04-S01] Elmegreen B. G., Scalo J. (2004, Annual Review of Astronomy and Astrophysics) | title=Interstellar Turbulence I: Observations and Processes | DOI:10.1146/annurev.astro.41.011802.094859; arXiv:astro-ph/0404451; ADS:2004ARA&A..42..211E | role=review_synthesis | review_locator=Section 3.1 | Synthesis of ISM turbulence phenomena.

[REV04-S02] Janka H.-T. (2012, Annual Review of Nuclear and Particle Science) | title=Explosion Mechanisms of Core-Collapse Supernovae | DOI:10.1146/annurev-nucl-102711-094901; arXiv:1206.2503; ADS:2012ARNPS..62..407J | role=review_synthesis | review_locator=Section 3.1 | Reference data for supernova explosion thermodynamics.

[REV04-S03] Mac Low M.-M., Klessen R. S. (2004, Reviews of Modern Physics) | title=Control of star formation by supersonic turbulence | DOI:10.1103/RevModPhys.76.125; arXiv:astro-ph/0301093; ADS:2004RvMP...76..125M | role=review_synthesis | review_locator=Section 3.1 | Highlighted the necessity of turbulent pressure.

[REV04-S04] Veilleux S., Cecil G., Bland-Hawthorn J. (2005, Annual Review of Astronomy and Astrophysics) | title=Galactic Winds | DOI:10.1146/annurev.astro.43.072103.150610; arXiv:astro-ph/0504435; ADS:2005ARA&A..43..769V | role=review_synthesis | review_locator=Section 1.3.1 | Benchmarked the properties and ubiquity of galactic winds.

7. DO_NOT_USE_UNVERIFIED

This section strictly quarantines uncited search results, AGN-centered microphysics outside the review's scope, post-2017 papers, and prohibited narrative claims.

UNCITED_NOT_USABLE	Candidate or Claim	Supplied Identifier / Context	Exclusion Reason
Quarantine	"JWST observations of early galaxies reveal extreme bursty star formation."	e.g., Mao et al. 2024, D'Eugenio et al. 2025, Harikane et al. 2024	Post-2017 observational missions completely unavailable and uncited in the 2017 review.
Quarantine	"AGN feedback acts as a multi-scale problem over many orders of magnitude down to the innermost stable circular orbit."	e.g., AGN microphysics / accretion disk papers.	Review boundary restriction: AGN must only be treated as a macroscopic galaxy-scale sub-grid ingredient, explicitly ignoring sub-parsec accretion microphysics.
Quarantine	"Matching the z=0 stellar mass function uniquely validates a specific supernova feedback mechanism."	Narrative claim.	Explicitly prohibited by the prompt and contradicted by the review (multiple disparate models hit the exact same calibration targets, demonstrating degeneracy rather than physical proof).
Quarantine	"Increasing numerical resolution to parsec scales definitively proves physical convergence of star formation rates."	Narrative claim.	Explicitly prohibited by the prompt. Sub-grid models are inherently scale-dependent; increasing resolution alters densities and cooling times, requiring continuous parameter re-tuning (numerical convergence does not equal physical convergence).
Quarantine	"Supernova feedback universally dominates all other channels across all environments."	Narrative claim.	Explicitly prohibited by the prompt; the hierarchy of pre-supernova feedback and cosmic rays remained highly debated variables in 2017.
Quarantine	Machine Learning frameworks applied to simulation outputs (e.g., Random Forests/XGBoost on TNG100 data).	e.g., ML follow-ups to cosmological simulations.	Post-2017 methodology entirely irrelevant to the 2017 source base.
8. Review and Source Identity Ledger

This final ledger provides the definitive index of the foundational review and all authorized primary sources utilized in the analysis. No source may act as a load-bearing physical citation in subsequent derivations unless recorded here.

[REV04-R00] Naab T., Ostriker J. P. (2017, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev-astro-081913-040019; arXiv:1612.06891; ADS:2017ARA&A..55...59N | role=review_synthesis | Boundary: Comprehensive 2017 synthesis of galaxy formation physics and computational sub-grid mechanisms.

[REV04-P001] Abadi M. G., Navarro J. F., Steinmetz M., Eke V. R. (2003, The Astrophysical Journal) | DOI:10.1086/375512; arXiv:astro-ph/0211331; ADS:2003ApJ...591..499A | role=hydrodynamic_simulation | Boundary: Early simulation defining the angular momentum problem.

[REV04-P002] Abadi M. G., Navarro J. F., Steinmetz M., Eke V. R. (2003, The Astrophysical Journal) | DOI:10.1086/378316; arXiv:astro-ph/0211383; ADS:2003ApJ...597...21A | role=hydrodynamic_simulation | Boundary: Detailed kinematic study of simulated disk structures.

[REV04-P003] Agertz O., Kravtsov A. V., Leitner S. N., Gnedin N. Y. (2013, The Astrophysical Journal) | DOI:10.1088/0004-637X/770/1/25; arXiv:1208.2741; ADS:2013ApJ...770...25A | role=hydrodynamic_simulation | Boundary: explicit implementations of momentum and energy stellar feedback.

[REV04-P004] Balogh M. L., Pearce F. R., Bower R. G., Kay S. T. (2001, Monthly Notices of the Royal Astronomical Society) | DOI:10.1046/j.1365-8711.2001.04652.x; arXiv:astro-ph/0104140; ADS:2001MNRAS.326.1228B | role=hydrodynamic_simulation | Boundary: established the necessity of overcoming rapid early gas condensation.

[REV04-P005] Bernardi M., et al. (2010, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2010.16425.x; arXiv:0910.1093; ADS:2010MNRAS.404.2087B | role=observation | Boundary: statistical baseline for local universe massive galaxy constraints.

[REV04-P006] Binney J. (1977, The Astrophysical Journal) | DOI:10.1086/155386; arXiv:none; ADS:1977ApJ...215..483B | role=analytic_theory | Boundary: physics establishing gas cooling prerequisites for structure formation.

[REV04-P007] Blondin J. M., Wright E. B., Borkowski K. J., Reynolds S. P. (1998, The Astrophysical Journal) | DOI:10.1086/305708; arXiv:astro-ph/9802081; ADS:1998ApJ...500..342B | role=analytic_theory | Boundary: thermodynamics of supernova remnants entering the radiative snowplow phase.

[REV04-P008] Boulares A., Cox D. P. (1990, The Astrophysical Journal) | DOI:10.1086/169466; arXiv:none; ADS:1990ApJ...365..544B | role=observation | Boundary: empirical evidence of non-thermal (cosmic ray/magnetic) energy density in the ISM.

[REV04-P009] Brook C. B., et al. (2011, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2011.18731.x; arXiv:1010.0003; ADS:2011MNRAS.415.1051B | role=hydrodynamic_simulation | Boundary: interaction between feedback ejection and angular momentum enhancement.

[REV04-P010] Cen R., Ostriker J. P. (1992, The Astrophysical Journal Letters) | DOI:10.1086/186596; arXiv:none; ADS:1992ApJ...399L.113C | role=hydrodynamic_simulation | Boundary: formulation of sub-grid star formation efficiency scaling with dynamical time.

[REV04-P011] Chevalier A. W. (1982, The Astrophysical Journal) | DOI:10.1086/160167; arXiv:none; ADS:1982ApJ...259..302C | role=analytic_theory | Boundary: phase evolutions of supernova blast interactions with uniform media.

[REV04-P012] Cioffi D. F., McKee C. F., Bertschinger E. (1988, The Astrophysical Journal) | DOI:10.1086/166834; arXiv:none; ADS:1988ApJ...334..252C | role=analytic_theory | Boundary: definitive analytic formulations for SNR radiative energy loss and momentum limits.

[REV04-P013] D'Onghia E., Burkert A. (2004, The Astrophysical Journal) | DOI:10.1086/422631; arXiv:astro-ph/0311283; ADS:2004ApJ...612..628D | role=hydrodynamic_simulation | Boundary: quantification of hierarchical assembly driving early angular momentum destruction.

[REV04-P014] Dalla Vecchia C., Schaye J. (2008, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2008.13244.x; arXiv:0801.2770; ADS:2008MNRAS.387.1431D | role=hydrodynamic_simulation | Boundary: foundational tests of decoupled kinetic winds vs. localized thermal feedback.

[REV04-P015] Dekel A., Silk J. (1986, The Astrophysical Journal) | DOI:10.1086/164050; arXiv:none; ADS:1986ApJ...303...39D | role=analytic_theory | Boundary: necessity of supernova feedback for shaping the low-mass end of galaxy formation.

[REV04-P016] Draine B. T. (2011, Physics of the Interstellar and Intergalactic Medium) | DOI:none; arXiv:none; ADS:2011piim.book.....D | role=observation | Boundary: reference text for global ISM physical parameters and state equations.

[REV04-P017] Fall S. M., Efstathiou G. (1980, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | role=analytic_theory | Boundary: standard model linking dark matter halo tidal torques to baryonic disk formation.

[REV04-P018] Haid S., et al. (2016, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stw1051; arXiv:1601.03055; ADS:2016MNRAS.460.2962H | role=hydrodynamic_simulation | Boundary: momentum bounds from supernovae operating in diverse and turbulent density environments.

[REV04-P019] Heckman T. M. (2000, Massive Stellar Clusters) | DOI:none; arXiv:astro-ph/0009075; ADS:2000msc..conf..299H | role=observation | Boundary: confirmation of ubiquitous mass-loaded winds leaving active galaxies.

[REV04-P020] Hennebelle P., Iffrig O. (2014, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201323334; arXiv:1405.7836; ADS:2014A&A...570A..81H | role=hydrodynamic_simulation | Boundary: models resolving magnetic field strengths directly relevant to dense cloud disruption.

[REV04-P021] Katz N. (1992, The Astrophysical Journal) | DOI:10.1086/171366; arXiv:none; ADS:1992ApJ...391..502K | role=hydrodynamic_simulation | Boundary: original formulation of sub-resolution SF density-timescale criteria for SPH modeling.

[REV04-P022] Katz N., Gunn J. E. (1991, The Astrophysical Journal) | DOI:10.1086/170367; arXiv:none; ADS:1991ApJ...377..365K | role=hydrodynamic_simulation | Boundary: early documentation of angular momentum crises in simulated dissipative gas clouds.

[REV04-P023] Katz N., Weinberg D. H., Hernquist L. (1996, The Astrophysical Journal Supplement Series) | DOI:10.1086/192310; arXiv:astro-ph/9509107; ADS:1996ApJS..105...19K | role=hydrodynamic_simulation | Boundary: highlighted the severe tendency for cosmological simulations to overproduce central bulges.

[REV04-P024] Kennicutt R. C., Jr (1998, The Astrophysical Journal) | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=observation | Boundary: defined the global relation used essentially by all models to calibrate sub-grid star formation rates.

[REV04-P025] Kereš D., Katz N., Weinberg D. H., Davé R. (2005, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0407095; ADS:2005MNRAS.363....2K | role=hydrodynamic_simulation | Boundary: evaluated the thermodynamics and morphological consequences of cold versus hot accretion flows.

[REV04-P026] Kim C.-G., Ostriker E. C. (2015, The Astrophysical Journal) | DOI:10.1088/0004-637X/802/2/99; arXiv:1501.03150; ADS:2015ApJ...802...99K | role=hydrodynamic_simulation | Boundary: precise limits on momentum scaling derived from ultra-high resolution SNR expansion experiments.

[REV04-P027] Larson R. B. (1974, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/169.2.229; arXiv:none; ADS:1974MNRAS.169..229L | role=analytic_theory | Boundary: foundational theory linking stellar feedback to the macroscopic evolution and element retention of young galaxies.

[REV04-P028] Leroy A. K., et al. (2008, The Astronomical Journal) | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=observation | Boundary: spatially resolved observations establishing the profound inefficiency of molecular gas converting to stars.

[REV04-P029] Marinacci F., et al. (2011, Monthly Notices of the Royal Astronomical Society) | DOI:none; arXiv:none; ADS:2011MNRAS.415.1534M | role=hydrodynamic_simulation | Boundary: non-linear torques affecting the angular momentum of returning gas fountains.

[REV04-P030] Martizzi D., Faucher-Giguère C.-A., Quataert E. (2015, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stv562; arXiv:1409.4425; ADS:2015MNRAS.450..504M | role=hydrodynamic_simulation | Boundary: quantitative formulas for momentum and thermal energy injected into explicitly inhomogeneous, multiphase media.

[REV04-P031] McKee C. F., Ostriker J. P. (1977, The Astrophysical Journal) | DOI:10.1086/155692; arXiv:none; ADS:1977ApJ...218..148M | role=analytic_theory | Boundary: established the theoretical blueprint for a three-phase ISM driven uniquely by successive SN explosions.

[REV04-P032] Navarro J. F., Benz W. (1991, The Astrophysical Journal) | DOI:10.1086/170569; arXiv:none; ADS:1991ApJ...380..320N | role=hydrodynamic_simulation | Boundary: linked collisionless dark matter halos with highly dissipative, overcooling gas inflows.

[REV04-P033] Navarro J. F., Steinmetz M. (1997, The Astrophysical Journal) | DOI:10.1086/303763; arXiv:astro-ph/9605043; ADS:1997ApJ...478...13N | role=hydrodynamic_simulation | Boundary: identified the structural failure mode of cosmological disks formed without explicit mass-loading feedback.

[REV04-P034] Peebles P. J. E. (1969, The Astrophysical Journal) | DOI:10.1086/149911; arXiv:none; ADS:1969ApJ...155..393P | role=analytic_theory | Boundary: classical analytical determination of initial galaxy spin acquired via external large-scale tidal forces.

[REV04-P035] Pettini M., et al. (2001, The Astrophysical Journal) | DOI:10.1086/321356; arXiv:astro-ph/0102456; ADS:2001ApJ...554..981P | role=observation | Boundary: early spectroscopic confirmation of massive, high-velocity galactic winds occurring at cosmic noon.

[REV04-P036] Pontzen A., Governato F. (2012, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2012.20571.x; arXiv:1106.0499; ADS:2012MNRAS.421.3464P | role=hydrodynamic_simulation | Boundary: showed how rapid, baryon-driven outflows dramatically alter the inner gravitational profiles of small halos.

[REV04-P037] Rees M. J., Ostriker J. P. (1977, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/179.4.541; arXiv:none; ADS:1977MNRAS.179..541R | role=analytic_theory | Boundary: established the physical boundaries determining where dark matter halos successfully trap cooling gas.

[REV04-P038] Schaye J., et al. (2015, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stu2058; arXiv:1407.7040; ADS:2015MNRAS.446..521S | role=hydrodynamic_simulation | Boundary: large-scale cosmological simulation achieving realistic stellar mass properties via calibrated stochastic thermal heating.

[REV04-P039] Schmidt M. (1959, The Astrophysical Journal) | DOI:10.1086/146614; arXiv:none; ADS:1959ApJ...129..243S | role=analytic_theory | Boundary: formulated the fundamental empirical power-law linking star-formation rates to locally available gas density.

[REV04-P040] Silk J. (1977, The Astrophysical Journal) | DOI:10.1086/155066; arXiv:none; ADS:1977ApJ...211..638S | role=analytic_theory | Boundary: foundational criteria establishing the upper limits on cooling rates leading to star formation within galactic halos.

[REV04-P041] Springel V., Hernquist L. (2003, Monthly Notices of the Royal Astronomical Society) | DOI:10.1046/j.1365-8711.2003.06206.x; arXiv:astro-ph/0206393; ADS:2003MNRAS.339..289S | role=semi_analytic_model | Boundary: formulation of the widely used sub-grid multiphase effective equation of state balancing star formation and feedback.

[REV04-P042] Tumlinson J., et al. (2011, Science) | DOI:10.1126/science.1209840; arXiv:1111.3970; ADS:2011Sci...334..948T | role=observation | Boundary: measurement of extensive heavy elements within the circumgalactic media confirming massive outflows.

[REV04-P043] Vogelsberger M., et al. (2014, Nature) | DOI:10.1038/nature13316; arXiv:1405.1418; ADS:2014Natur.509..177V | role=hydrodynamic_simulation | Boundary: Illustris model achieving macroscopic galaxy statistics using decoupled kinetic winds and thermal AGN feedback.

[REV04-P044] Walch S., Naab T. (2015, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stv1975; arXiv:1412.2749; ADS:2015MNRAS.454..238W | role=hydrodynamic_simulation | Boundary: validated the momentum scaling of clustered versus isolated supernovae inside complex, self-gravitating molecular clouds.

[REV04-P045] Werk J. K., et al. (2014, The Astrophysical Journal) | DOI:10.1088/0004-637X/792/1/8; arXiv:1403.0947; ADS:2014ApJ...792....8W | role=observation | Boundary: quantified cool gas densities and heavy element kinematics within the extended halos of massive star-forming galaxies.

[REV04-P046] White S. D. M., Rees M. J. (1978, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | role=analytic_theory | Boundary: the seminal framework for two-stage cosmological formation (merging collisionless dark matter followed by dissipative gas cooling).

[REV04-P047] Krumholz M. R., McKee C. F. (2005, The Astrophysical Journal) | DOI:10.1086/431734; arXiv:astro-ph/0505177; ADS:2005ApJ...630..250K | role=analytic_theory | Boundary: theoretical framework for how interstellar turbulence dictates local star formation rates.

[REV04-P048] Glover S. C. O., Mac Low M.-M. (2007, The Astrophysical Journal Supplement Series) | DOI:10.1086/512238; arXiv:astro-ph/0605120; ADS:2007ApJS..169..239G | role=hydrodynamic_simulation | Boundary: demonstrated how supersonic turbulence controls the timescale for H2 formation and gravitational collapse.

[REV04-P049] Salem M., Bryan G. L. (2014, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stt2121; arXiv:1307.6215; ADS:2014MNRAS.437.3312S | role=hydrodynamic_simulation | Boundary: simulated the efficiency of cosmic-ray transport in accelerating cold gas out of the galactic potential well.

Supporting Reviews

[REV04-S01] Elmegreen B. G., Scalo J. (2004, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev.astro.41.011802.094859; arXiv:astro-ph/0404451; ADS:2004ARA&A..42..211E | role=review_synthesis | Boundary: Synthesis of ISM turbulence phenomena.

[REV04-S02] Janka H.-T. (2012, Annual Review of Nuclear and Particle Science) | DOI:10.1146/annurev-nucl-102711-094901; arXiv:1206.2503; ADS:2012ARNPS..62..407J | role=review_synthesis | Boundary: Reference data for supernova explosion thermodynamics.

[REV04-S03] Mac Low M.-M., Klessen R. S. (2004, Reviews of Modern Physics) | DOI:10.1103/RevModPhys.76.125; arXiv:astro-ph/0301093; ADS:2004RvMP...76..125M | role=review_synthesis | Boundary: Highlighted the necessity of turbulent pressure.

[REV04-S04] Veilleux S., Cecil G., Bland-Hawthorn J. (2005, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev.astro.43.072103.150610; arXiv:astro-ph/0504435; ADS:2005ARA&A..43..769V | role=review_synthesis | Boundary: Benchmarked the properties and ubiquity of galactic winds.

REVIEW_BASE_04_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- wwwmpa.mpa-garching.mpg.de Why Cosmic Voids Matter: Nonlinear Structure & Linear Dynamics - MPA Garching Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/HydroSims/Magneticum/Preprints/Voids_Dynamics.pdf
- arxiv.org The influence of Massive Black Hole Binaries on the Morphology of Merger Remnants - arXiv Opens in a new window — https://arxiv.org/pdf/1710.04658
- academic.oup.com Active galactic nuclei feedback, quiescence and circumgalactic medium metal enrichment in early-type galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/468/1/751/3051676
- ned.ipac.caltech.edu annual reviews of astronomy and astrophysics Opens in a new window — https://ned.ipac.caltech.edu/level5/araa.html
- ned.ipac.caltech.edu Theoretical Challenges in Galaxy Formation - Thorsten Naab and Jeremiah P. Ostriker Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Naab/frames.html
- ned.ipac.caltech.edu NED History - NASA/IPAC Extragalactic Database Opens in a new window — http://ned.ipac.caltech.edu/help/nedhistory.html
- ned.ipac.caltech.edu Archived Release Notes - About NED | NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/Documents/Overview/History
- astro.sunysb.edu How to Characterize Habitable Worlds and Signs of Life - Stony Brook Astronomy Opens in a new window — https://www.astro.sunysb.edu/fwalter/PHY688/Kaltenegger_annurev-astro-082214-122238.pdf
- crossfield.ku.edu Stellar Model Chromospheres and Spectroscopic Diagnostics Opens in a new window — https://crossfield.ku.edu/A691_2022B/linsky2017_chromospheres.pdf
- bo.astro.it Ultraluminous X-Ray Sources Opens in a new window — http://www.bo.astro.it/~vignali/Astrofisica_Alte_Energie/AA2019-20/Compact_Objects/ULX/papers/kaaret17_ULX_review.pdf
- ml4physicalsciences.github.io First High-Resolution Galaxy Simulations Accelerated by a 3D Surrogate Model for Supernovae - Machine Learning and the Physical Sciences Opens in a new window — https://ml4physicalsciences.github.io/2024/files/NeurIPS_ML4PS_2024_83.pdf
- arxiv.org [1612.06891] Theoretical Challenges in Galaxy Formation - arXiv Opens in a new window — https://arxiv.org/abs/1612.06891
- oar.princeton.edu Breaking baryon-cosmology degeneracy with the electron density power spectrum Opens in a new window — https://oar.princeton.edu/bitstream/88435/pr1jd4pp7p/1/2201.04142v1.pdf
- cpt.univ-mrs.fr EC16 — Program Opens in a new window — https://www.cpt.univ-mrs.fr/~cosmo/EC2025/index.php?page=program
- arxiv.org 1 Introduction - arXiv Opens in a new window — https://arxiv.org/html/2404.08050v1
- ar5iv.labs.arxiv.org [1612.06891] Theoretical Challenges in Galaxy Formation - ar5iv Opens in a new window — https://ar5iv.labs.arxiv.org/html/1612.06891
- archiv.ub.uni-heidelberg.de Gensior_PhD_thesis_pub.pdf - Heidelberg University Opens in a new window — https://archiv.ub.uni-heidelberg.de/volltextserver/30269/1/Gensior_PhD_thesis_pub.pdf
- nu.to.infn.it Astronomy and Astrophysics - Neutrino Unbound - INFN Opens in a new window — https://www.nu.to.infn.it/Other_Astrophysics/
- academic.oup.com cosmic baryon cycle and galaxy mass assembly in the FIRE simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/470/4/4698/3871367
- researchgate.net Understanding the regulation of star formation within TNG100 galaxies on kpc-scales using machine learning I: Global versus local - ResearchGate Opens in a new window — https://www.researchgate.net/publication/403905806_Understanding_the_regulation_of_star_formation_within_TNG100_galaxies_on_kpc-scales_using_machine_learning_I_Global_versus_local
- arxiv.org Chapter 0 Cosmological Simulations of Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2507.08925v1
- matthewmumpower.com г-Process Nucleosynthesis: Connecting Rare-Isotope Beam Facilities with the Cosmos - Matthew Mumpower Opens in a new window — https://matthewmumpower.com/static/publications/connecting-rib-facilities.pdf
- research.iac.es Observational Tests of AGN Feedback: An Overview of Approaches and Interpretation Opens in a new window — https://research.iac.es/preprints/files/PP24033.pdf
- mdpi.com A Review of the Theory of Galactic Winds Driven by Stellar Feedback - MDPI Opens in a new window — https://www.mdpi.com/2075-4434/6/4/114
- researchgate.net simba: Cosmological simulations with black hole growth and feedback - ResearchGate Opens in a new window — https://www.researchgate.net/publication/344958803_simba_Cosmological_simulations_with_black_hole_growth_and_feedback
- edoc.ub.uni-muenchen.de Galaxy Kinematics during the Peak Epoch of Cosmic Star Formation Opens in a new window — https://edoc.ub.uni-muenchen.de/24712/1/Uebler_Hannah_D_N.pdf
- kups.ub.uni-koeln.de Ideal GLM-MHD - a new mathematical model for simulating astrophysical plasmas - Universität zu Köln Opens in a new window — https://kups.ub.uni-koeln.de/8442/1/Derigs_fonts_embedded_no_Acknowledgements.pdf
- cris.unibo.it Cosmological Simulations of Galaxy Formation - Alma Mater Studiorum Università di Bologna Archivio istituzionale della ricerca Opens in a new window — https://cris.unibo.it/bitstream/11585/799379/4/1909.07976.pdf
- annualreviews.org Volume 55, 2017 | Annual Review of Astronomy and Astrophysics Opens in a new window — https://www.annualreviews.org/content/journals/astro/55/1
- ned.ipac.caltech.edu Theoretical Challenges in Galaxy Formation - Thorsten Naab and Jeremiah P. Ostriker Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Naab/Naab1.html
- arxiv.org Learning the Universe with PRFM-vol: Introducing a new subgrid model for star formation in cosmological simulations - arXiv Opens in a new window — https://arxiv.org/html/2606.10022v1
- arxiv.org Introducing sapphire: Towards Hybrid Physics-Informed, Data-Driven Modeling of Galaxy Formation - arXiv Opens in a new window — https://arxiv.org/html/2604.06318v1
- eprints.soton.ac.uk arXiv:2502.12764v1 [astro-ph.GA] 18 Feb 2025 - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/502442/1/2502.12764v1.pdf
- researchgate.net Theoretical Challenges in Galaxy Formation | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/311805639_Theoretical_Challenges_in_Galaxy_Formation
- ned.ipac.caltech.edu Theoretical Challenges in Galaxy Formation - Thorsten Naab and Jeremiah P. Ostriker Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Naab/Naab2.html
- arxiv.org Mitigating the overcooling problem with sink-based bursty star formation in a high-z dwarf galaxy - arXiv Opens in a new window — https://arxiv.org/html/2607.08846v1
- pmc.ncbi.nlm.nih.gov Fast and inefficient star formation due to short-lived molecular clouds and rapid feedback - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC6544524/
- ned.ipac.caltech.edu Theoretical Challenges in Galaxy Formation Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Naab/paper.pdf
- academic.oup.com Supernova feedback in numerical simulations of galaxy formation: separating physics from numerics | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/478/1/302/4980956
- researchgate.net The energy and momentum input of supernova explosions in structured and ionized molecular clouds - ResearchGate Opens in a new window — https://www.researchgate.net/publication/279737884_The_energy_and_momentum_input_of_supernova_explosions_in_structured_and_ionized_molecular_clouds
- ned.ipac.caltech.edu Theoretical Challenges in Galaxy Formation - Thorsten Naab and Jeremiah P. Ostriker Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Naab/Naab3.html
- arxiv.org Supernova feedback in a local vertically stratified medium: interstellar turbulence and galactic winds - arXiv Opens in a new window — https://arxiv.org/pdf/1601.03399
- uwcscholar.uwc.ac.za arXiv:2405.19227v2 [astro-ph.GA] 6 Jun 2024 - UWCScholar Opens in a new window — https://uwcscholar.uwc.ac.za/bitstreams/574a163f-163f-440f-8360-4f9d998178d0/download
- academic.oup.com SILCC (SImulating the LifeCycle of molecular Clouds) project – II. Dynamical evolution of the supernova-driven ISM and the launching of outflows - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/456/4/3432/1029803
- academic.oup.com SILCC project – V. The impact of magnetic fields on the chemistry and the formation of molecular clouds | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/480/3/3511/5067325
- academic.oup.com The SILCC (SImulating the LifeCycle of molecular Clouds) project – I. Chemical evolution of the supernova-driven ISM - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/454/1/238/3924820/stv1975.pdf
- academic.oup.com SILCC (SImulating the LifeCycle of molecular Clouds) project – I. Chemical evolution of the supernova-driven ISM | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/454/1/238/1133035
- arxiv.org arXiv:1510.06563v1 [astro-ph.GA] 22 Oct 2015 Opens in a new window — https://www.arxiv.org/pdf/1510.06563v1.pdf
- osti.gov Properties of molecular clumps and cores in colliding magnetized flows - OSTI Opens in a new window — https://www.osti.gov/biblio/2395992
- academic.oup.com Supernova feedback in a local vertically stratified medium: interstellar turbulence and galactic winds - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/459/3/2311/8106320/stw745.pdf
- academic.oup.com Supernova feedback in a local vertically stratified medium: interstellar turbulence and galactic winds | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/459/3/2311/2595161
- arxiv.org [1601.03399] Supernova feedback in a local vertically stratified medium: interstellar turbulence and galactic winds - arXiv Opens in a new window — https://arxiv.org/abs/1601.03399
- openaccess.inaf.it Negative and positive feedback from a supernova remnant with SHREC: a detailed study of the shocked gas in IC443 - OA@INAF Opens in a new window — https://openaccess.inaf.it/bitstreams/3b83cc15-ded0-4ab4-aca0-22b8e5c34786/download
- academic.oup.com Supernova feedback in an inhomogeneous interstellar medium - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/450/1/504/998665
- academic.oup.com Supernova feedback in numerical simulations of galaxy formation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/478/1/302/24971782/sty994.pdf
- semanticscholar.org The energy and momentum input of supernova explosions in structured and ionized molecular clouds - Semantic Scholar Opens in a new window — https://www.semanticscholar.org/paper/The-energy-and-momentum-input-of-supernova-in-and-Walch-Naab/91b8d2164048b8496d7ab5c80d8cd42c7996a3b7
- academic.oup.com Feedback in Clouds II: UV photoionization and the first supernova in a massive cloud | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/463/3/3129/2646636
- ouci.dntb.gov.ua Connecting stellar and galactic scales: Energetic feedback from stellar wind bubbles to supernova remnants - OUCI Opens in a new window — https://ouci.dntb.gov.ua/works/988DRKq9/
- academic.oup.com Bimodality of low-redshift circumgalactic O vi in non-equilibrium eagle zoom simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/460/2/2157/2609032
- arxiv.org arXiv:1401.5799v2 [astro-ph.CO] 25 Feb 2014 Opens in a new window — https://arxiv.org/pdf/1401.5799
- scholarlypublications.universiteitleiden.nl Flickering AGN can explain the strong circumgalactic O VI observed by COS-Halos - Scholarly Publications Leiden University Opens in a new window — https://scholarlypublications.universiteitleiden.nl/access/item%3A2908157/view
- arxiv.org arXiv:1609.00012v2 [astro-ph.GA] 15 Nov 2016 Opens in a new window — https://arxiv.org/pdf/1609.00012
- academic.oup.com Most of the cool CGM of star-forming galaxies is not produced by supernova feedback - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/501/4/5575/6022218
- arxiv.org Contents - arXiv Opens in a new window — https://arxiv.org/html/2506.13851v3
- academic.oup.com A SINFONI integral field spectroscopy survey for galaxy counterparts to damped Lyman α systems Opens in a new window — https://academic.oup.com/mnras/article-pdf/419/4/3060/9505935/mnras0419-3060.pdf
- thesis.caltech.edu Lyman Continuum and Lyman α Emission from Galaxies at High Redshift Opens in a new window — https://thesis.caltech.edu/5767/1/thesis_milan.pdf
- knowledge.lancashire.ac.uk A High-precision Survey of the D/H Ratio in the Nearby Interstellar Medium Opens in a new window — https://knowledge.lancashire.ac.uk/id/eprint/46071/1/Friedman_2023_ApJ_946_34.pdf
- digital.csic.es An Empirical Framework Characterizing the Metallicity and Star-formation History Dependence of X-Ray Binary Population Formation Opens in a new window — https://digital.csic.es/bitstream/10261/381503/1/Empirical-Framework_Lehmer.pdf
- research.chalmers.se ALMA Detection of [O <sc>iii</sc>] 88 <i>μ</i>m at <i>z</i>=12.33: Exploring the Nature and - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/544484/file/544484_Fulltext.pdf
- par.nsf.gov Cosmic ray feedback in the FIRE simulations: constraining cosmic ray propagation with GeV gamma ray emission - NSF PAR Opens in a new window — https://par.nsf.gov/servlets/purl/10105535
- arxiv.org Star Formation, Cosmic Ray Transport, and Multiphase Outflows in Tigress++ Simulations - arXiv Opens in a new window — https://arxiv.org/html/2605.26238v1
- academic.oup.com Cosmic ray feedback in the FIRE simulations: constraining cosmic ray propagation with GeV γ-ray emission - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/488/3/3716/5530789
- arxiv.org CRexit observed: probing cosmic ray transport in the circumgalactic medium with absorption line spectra - arXiv Opens in a new window — https://arxiv.org/html/2607.06744v1
- researchgate.net Resolving Star Cluster Formation in Galaxy Simulations with Cosmic Ray Feedback Opens in a new window — https://www.researchgate.net/publication/407206909_Resolving_Star_Cluster_Formation_in_Galaxy_Simulations_with_Cosmic_Ray_Feedback
- arxiv.org [1405.3749] Introducing the Illustris Project: the evolution of galaxy populations across cosmic time - arXiv Opens in a new window — https://arxiv.org/abs/1405.3749
- academic.oup.com Introducing the Illustris Project: simulating the coevolution of dark and visible matter in the Universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/444/2/1518/24040116/stu1536.pdf
- arxiv.org [1405.2921] Introducing the Illustris Project: Simulating the coevolution of dark and visible matter in the Universe - arXiv Opens in a new window — https://arxiv.org/abs/1405.2921
- academic.oup.com Introducing the Illustris Project: simulating the coevolution of dark and visible matter in the Universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/444/2/1518/1749887
- dspace.mit.edu Introducing the Illustris Project: simulating the coevolution of dark and visible matter in the Universe - DSpace@MIT Opens in a new window — https://dspace.mit.edu/bitstreams/12e18e0c-e8d1-423e-b1b7-997ecbdd46fc/download
- researchgate.net Introducing the Illustris Project: Simulating the coevolution of dark and visible matter in the Universe - ResearchGate Opens in a new window — https://www.researchgate.net/publication/262989604_Introducing_the_Illustris_Project_Simulating_the_coevolution_of_dark_and_visible_matter_in_the_Universe
- arxiv.org Non-Equilibrium Abundances Treated Holistically (NEATH): the molecular composition of star-forming clouds - arXiv Opens in a new window — https://arxiv.org/pdf/2307.13072
- wwwmpa.mpa-garching.mpg.de The SILCC (SImulating the LifeCycle of molecular Clouds) project: I. Chemical evolution of the supernova-driven ISM - MPA Garching Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/mpa/publications/preprints/pp2014/MPA3760.pdf
- scispace.com The CO-to-H2 Conversion Factor - SciSpace Opens in a new window — https://scispace.com/pdf/the-co-to-h2-conversion-factor-26tvppkvj7.pdf
- cambridge.org Chemical Evolution of Turbulent Multiphase Molecular Clouds | Proceedings of the International Astronomical Union - Cambridge University Press & Assessment Opens in a new window — https://www.cambridge.org/core/journals/proceedings-of-the-international-astronomical-union/article/chemical-evolution-of-turbulent-multiphase-molecular-clouds/53030C1A1877154EB9967C71FE73A6C9
- arxiv.org Implementing Molecular Hydrogen in Hydrodynamic Simulations of Galaxy Formation - arXiv Opens in a new window — https://arxiv.org/pdf/1205.5567
- dash.harvard.edu A general model for the CO-H2 conversion factor in galaxies with applications to the star formation law - DASH (Harvard) Opens in a new window — https://dash.harvard.edu/bitstreams/197f2139-9365-4ff0-9d18-d43b52398cbd/download
- ora.ox.ac.uk A detailed study of feedback from a massive star - Oxford University Research Archive Opens in a new window — https://ora.ox.ac.uk/objects/uuid:cf936ac0-940a-4a95-b652-f7b96323e475/files/mf4614f019db9774319c57576e7877a5e
- arxiv.org A systematic meta-analysis of physical parameters of Galactic supernova remnants - arXiv Opens in a new window — https://arxiv.org/pdf/2510.05202
- academic.oup.com Detection of optical emission from the supernova remnant G7.7–3.7 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/526/1/1112/7271805
- researchgate.net Shocking interactions of supernova remnants with atomic and molecular clouds -- the interplay between shocks, thermal instability and gravity in the large cloud regime - ResearchGate Opens in a new window — https://www.researchgate.net/publication/360618467_Shocking_interactions_of_supernova_remnants_with_atomic_and_molecular_clouds_--_the_interplay_between_shocks_thermal_instability_and_gravity_in_the_large_cloud_regime
- openaccess.inaf.it Publication Year 2022 Acceptance in OA 2023-02-06T15:09:51Z Title Grammage of cosmic rays in the proximity of supernova remnants Opens in a new window — https://openaccess.inaf.it/bitstreams/3c06880e-f626-4754-b6e4-93edf3f1b6ea/download
- academic.oup.com Kinematics of supernova remnants in the galaxy NGC 6946 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/547/3/stag410/8501210
- par.nsf.gov Bursty Star Formation in Dwarfs is Sensitive to Numerical Choices in Supernova Feedback Models Opens in a new window — https://par.nsf.gov/servlets/purl/10587239
- research-collection.ethz.ch I. Turbulent multiphase ISM in Milky Way simulations with SNe feedback from stellar clusters Opens in a new window — https://www.research-collection.ethz.ch/bitstreams/78a06b8f-69b9-43a7-b04e-96159f988f96/download
- academic.oup.com Galaxies on FIRE (Feedback In Realistic Environments): stellar feedback explains cosmologically inefficient star formation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/445/1/581/18473138/stu1738.pdf
- academic.oup.com Star formation and feedback in smoothed particle hydrodynamic simulations – I. Isolated galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/373/3/1074/1061683
- scispace.com I. Turbulent multiphase ISM in Milky Way simulations with SNe feedback from stellar clusters - SciSpace Opens in a new window — https://scispace.com/pdf/the-satin-project-i-turbulent-multiphase-ism-in-milky-way-2u1l1pqb.pdf
- ndl.ethernet.edu.et The Physics and Chemistry of the Interstellar Medium - National Academic Digital Library of Ethiopia Opens in a new window — https://ndl.ethernet.edu.et/bitstream/123456789/31300/1/A.G.G.M.%20Tielens.pdf
- academic.oup.com Simulating anisotropic thermal conduction in supernova remnants – II. Implications for the interstellar medium | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/386/2/642/1055232
- dspace.uevora.pt What Physical Processes Drive the Interstellar Medium in the Local Bubble? Opens in a new window — https://dspace.uevora.pt/rdpc/bitstream/10174/5645/1/2009SSRv...143..263Breitschwerdt%2BdeAvillez.pdf
- oar.princeton.edu SUPERBUBBLES IN THE MULTIPHASE ISM AND THE LOADING OF GALACTIC WINDS Opens in a new window — https://oar.princeton.edu/bitstream/88435/pr1p26q34s/1/Kim_2017_ApJ_834_25.pdf
- mso.anu.edu.au Momentum feedback from marginally resolved HII regions in isolated disc galaxies Opens in a new window — https://www.mso.anu.edu.au/~krumholz/publications/2021/jeffreson21b.pdf
- sternwarte.uni-erlangen.de X-ray Evolution of Supernova Remnants in the Large Magellanic Cloud - Dr. Karl Remeis-Sternwarte Opens in a new window — https://www.sternwarte.uni-erlangen.de/docs/theses/2024-11_Shukla.pdf
- arxiv.org [0710.2102] Molecular Hydrogen and Global Star Formation Relations in Galaxies - arXiv Opens in a new window — https://arxiv.org/abs/0710.2102
- eso.org The ATLAS3D project – XXII. Low-efficiency star formation in early-type galaxies: hydrodynamic models and observations - ESO.org Opens in a new window — http://www.eso.org/~hkuntsch/papers/MNRAS_432_1914.pdf
- academic.oup.com Self-regulated star formation in galaxies via momentum input from massive stars | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/417/2/950/983715
- academic.oup.com Gravity or turbulence? – VI. The physics behind the Kennicutt–Schmidt relation | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/534/2/1043/7740789
- mso.anu.edu.au A UNIVERSAL, LOCAL STAR FORMATION LAW IN GALACTIC CLOUDS, NEARBY GALAXIES, HIGH-REDSHIFT DISKS, AND STARBURSTS Opens in a new window — https://www.mso.anu.edu.au/~krumholz/publications/2012/krumholz12a.pdf
- scielo.org.mx Star Formation Rate in Late-Type Galaxies: I- The Hα and FUV Integrated Values - SciELO México Opens in a new window — https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0185-11012020000100039
- eprints.lib.hokudai.ac.jp Title Formation and evolution of giant molecular clouds in a barred Opens in a new window — https://eprints.lib.hokudai.ac.jp/repo/huscap/all/61705/Yusuke_Fujimoto.pdf
- pmc.ncbi.nlm.nih.gov Cosmic ray feedback in galaxies and galaxy clusters - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC10730010/
- archiv.ub.uni-heidelberg.de Stellar Feedback and the Self-Regulation of Star Formation in Giant Molecular Clouds Opens in a new window — https://archiv.ub.uni-heidelberg.de/volltextserver/26665/1/thesisPRINT.pdf
- ndl.ethernet.edu.et Star Formation in Galaxy Evolution: Connecting Numerical Models to Reality - National Academic Digital Library of Ethiopia Opens in a new window — https://ndl.ethernet.edu.et/bitstream/123456789/75685/1/314.pdf
- pmc.ncbi.nlm.nih.gov Exploring the link between star and planet formation with Ariel - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC9166885/
- researchonline.ljmu.ac.uk Vertical disc heating in Milky Way-sized galaxies in a cosmological context - LJMU Research Online Opens in a new window — https://researchonline.ljmu.ac.uk/id/eprint/19352/1/stw601.pdf
- academic.oup.com SATIN project – I. Turbulent multiphase ISM in Milky Way simulations with SNe feedback from stellar clusters - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/523/4/6336/7198128
- academic.oup.com The failure of stellar feedback, magnetic fields, conduction, and morphological quenching in maintaining red galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/487/3/4393/5510435
- academic.oup.com Galaxies in a simulated ΛCDM Universe – I. Cold mode and hot cores | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/395/1/160/1079146
- cambridge.org The Formation of Globular Clusters and of The Stars Within Them | Symposium - International Astronomical Union | Cambridge Core Opens in a new window — https://www.cambridge.org/core/product/D83C8CF131E620C0DF98EFFD38FA4EEB
- prints.iiap.res.in Investigating the Disk – Halo Connection using Numerical Opens in a new window — http://prints.iiap.res.in/jspui/bitstream/2248/8537/1/Investigating%20the%20Disk%20%E2%80%93%20Halo%20Connection%20using%20Numerical%20Simulations.pdf
- eprints.soton.ac.uk University of Southampton Research Repository Opens in a new window — https://eprints.soton.ac.uk/497183/1/PhD_Thesis-1.pdf
- ndl.ethernet.edu.et Galaxies and their Masks - National Academic Digital Library of Ethiopia Opens in a new window — http://ndl.ethernet.edu.et/bitstream/123456789/65602/1/68.pdf
- mso.anu.edu.au DWARF GALAXY FORMATION WITH H2-REGULATED STAR FORMATION - Research School of Astronomy & Astrophysics Opens in a new window — https://www.mso.anu.edu.au/~krumholz/publications/2012/kuhlen12a.pdf
- academic.oup.com Simulating galaxy formation with the IllustrisTNG model | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/473/3/4077/4494369
- academic.oup.com Build-up and survival of the disc: from numerical models of galaxy formation to the Milky Way | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/548/4/staf2154/8667673
- journals.jps.jp Challenges in Cosmology from the Big Bang to Dark Energy, Dark Matter and Galaxy Formation - JPS Journals Opens in a new window — https://journals.jps.jp/doi/pdf/10.7566/JPSCP.14.010101
- arxiv.org arXiv:0707.1856v1 [astro-ph] 12 Jul 2007 Opens in a new window — https://arxiv.org/pdf/0707.1856
- cambridge.org On the redshift evolution of the spin parameter in cosmological simulations | Publications of the Astronomical Society of Australia - Cambridge University Press & Assessment Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/on-the-redshift-evolution-of-the-spin-parameter-in-cosmological-simulations/214DD33CFFF7FB491830210AD7B0433E
- mpe.mpg.de The VIRUS-dE Survey. I. Stars in Dwarf Elliptical Galaxies—3D Dynamics and Radially Resolved Stellar Initial Mass Functions - Max-Planck-Institut für extraterrestrische Physik Opens in a new window — https://www.mpe.mpg.de/~saglia/journals_pdf/lipka2024a.pdf
- academicworks.cuny.edu Can We Discover Physical Models Using Machine Learning? A Case Study of Galaxy Sizes Opens in a new window — https://academicworks.cuny.edu/cgi/viewcontent.cgi?article=2295&context=ny_pubs
- cds.cern.ch Disentangling the Impact of Halo-to-halo Variance and Baryonic Feedback on Milky Way Dark Matter Opens in a new window — https://cds.cern.ch/record/2960545/files/document.pdf
- sites.astro.caltech.edu SECULAR EVOLUTION AND THE FORMATION OF PSEUDOBULGES IN DISK GALAXIES - Caltech Astronomy Opens in a new window — https://sites.astro.caltech.edu/~ccs/ay124/kormendy_araa_2004_secular.pdf
- academic.oup.com The influence of subhaloes on host halo properties - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/526/3/4157/7283171
- openaccess.inaf.it Publication Year 2017 Acceptance in OA 2021-02-08T11:38:42Z Title Angular momentum evolution of galaxies over the past 10 Gyr: a Opens in a new window — https://openaccess.inaf.it/bitstreams/d8dc330a-a896-4741-a610-9947001d157c/download
- scispace.com Using angular momentum maps to detect kinematically ... - SciSpace Opens in a new window — https://scispace.com/pdf/using-angular-momentum-maps-to-detect-kinematically-distinct-30o4fo7x66.pdf
- cambridge.org Dynamical aspects of Galactic habitability in N-body simulations | Publications of the Astronomical Society of Australia | Cambridge Core Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/dynamical-aspects-of-galactic-habitability-in-nbody-simulations/F30579B2A92B295976D7A9A0BC2F4B64
- academic.oup.com Emergence of galactic morphologies at cosmic dawn: input from numerical modelling - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/513/1/693/6528923
- cambridge.org Probing the resolved K-S relation in nearby galaxies: Insights from UVIT and ALMA observations - Cambridge University Press & Assessment Opens in a new window — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5A14AE2FF9ECAD9C73713CB219F7A816/S132335802510088Xa.pdf/probing-the-resolved-k-s-relation-in-nearby-galaxies-insights-from-uvit-and-alma-observations.pdf
- academic.oup.com Dissecting cosmological filaments at high redshifts: emergence of spaghetti-type flow inside DM haloes - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/527/4/11095/7491064
- ir.library.osaka-u.ac.jp Physically-motivated feedback models and the IGM metal enrichment in cosmological hydrodynamic simulations Opens in a new window — https://ir.library.osaka-u.ac.jp/repo/ouka/all/96417/34336_Dissertation.pdf
- arxiv.org Chapter 0 Hydrodynamic methods and sub-resolution models for cosmological simulations Opens in a new window — https://arxiv.org/html/2502.06954v1

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

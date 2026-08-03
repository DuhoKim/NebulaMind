Forward Modeling versus Raw Statistics in Cosmological Hydrodynamical Simulations: A Comprehensive Assessment of Feedback-Relevant Predictions
1. Introduction to the Validation of Cosmological Simulations

The continuous evolution of cosmological hydrodynamical simulations has driven a fundamental paradigm shift in theoretical astrophysics and our holistic understanding of galaxy formation across cosmic time. Major numerical projects, spanning from the IllustrisTNG and EAGLE suites to SIMBA, the Feedback In Realistic Environments (FIRE) project, and the Romulus volumes, attempt the monumental task of solving the non-linear equations of gravity and magnetohydrodynamics within an expanding spacetime metric. Due to the vast dynamic range required to simulate cosmological volumes down to the scale of individual molecular clouds, these models rely intrinsically on subgrid prescriptions for baryonic feedback. These prescriptions parameterize the unresolved physics of supernovae detonations, stellar winds from massive OB stars, and the immense kinetic and thermal energy injected by active galactic nuclei (AGN) driven by supermassive black holes.

As these simulation suites have matured in their numerical resolution and physical complexity, the fidelity of their multiphase gas outputs has necessitated a dramatic transition in how their theoretical predictions are validated against the empirical reality of the observed universe. Historically, the output of cosmological simulations was evaluated using raw physical statistics. Researchers would directly query the particle or grid data utilizing friends-of-friends algorithms or phase-space halo finders such as subfind or ROCKSTAR to derive intrinsic stellar masses, absolute star formation rates, and raw cold gas fractions. These intrinsic values represent the absolute, omniscient "truth" of the simulation data structure.

However, the actual universe is never observed in such a pristine state. Empirical data is acquired through the heavily biased and distorting lenses of telescope optics, atmospheric attenuation, surface brightness limits, and complex radiative transfer processes where photons are scattered and absorbed by interstellar and circumgalactic dust and gas. To bridge the widening gap between the omniscient simulation space and the restricted observer space, the field of computational astrophysics has increasingly adopted the framework of "forward modeling." This process involves taking raw simulated particle or cell data and passing it through sophisticated synthetic observing pipelines, which include instrumental simulators and Monte Carlo radiative transfer codes. These pipelines produce "mock observables"—synthetic imaging, spectra, and photometry—that can be subjected to the exact same biases, selection functions, and signal-to-noise limitations as genuine empirical survey data from observatories like the Hubble Space Telescope (HST), the James Webb Space Telescope (JWST), the Chandra X-ray Observatory, and the Sloan Digital Sky Survey (SDSS).   

This comprehensive report dissects the current methodological landscape of feedback-relevant predictions in major galaxy-formation simulations. It meticulously catalogs which specific predictions have been subjected to genuine forward modeling, which rely merely on raw simulation statistics mapping, and crucially, what observational biases, projection effects, and selection functions these forward-modeling efforts have successfully quantified and exposed.

2. The Observable-Pipeline Map

To facilitate genuine forward modeling and synthesize realistic observables from raw hydrodynamic outputs, a distinct and highly specialized software ecosystem has emerged. These pipelines are designed to interface seamlessly with the diverse data formats of major simulation suites. The following ledger maps the primary forward-modeling pipelines currently actively utilized in the literature to test theoretical feedback models against empirical reality.

The transition from theoretical fluid dynamics to synthetic photon captures relies heavily on several specific, well-documented codebases, each tailored to a specific wavelength regime and physical emission mechanism.

The first major category encompasses optical and near-infrared photometry and morphological synthesis. The GalSyn pipeline is a dedicated forward-modeling framework specifically designed to generate synthetic galaxy observations directly from the IllustrisTNG simulation suite. It functions by downloading specific subhalo cutouts and converting the raw particle data into standardized physical units necessary for mock imagery. Similarly, the FORECAST code is utilized to generate complete cosmological light cones and mock images. FORECAST has been deployed to emulate deep legacy fields such as the CANDELS and CEERS surveys, taking intrinsic simulation data from TNG100 and EAGLE and degrading it by applying realistic observational depths, background noise, and highly specific point spread functions (PSFs) to match instruments like HST's WFC3 or JWST's NIRCam.   

For a more rigorous treatment of the interstellar medium, dust radiative transfer is an absolute necessity. The SKIRT code is a highly advanced, three-dimensional Monte Carlo radiative transfer pipeline utilized heavily in conjunction with both the EAGLE and IllustrisTNG simulations. Because cosmological simulations rarely track interstellar dust as an explicit, separate hydrodynamic species, SKIRT applies complex subgrid resampling procedures to star-forming particles. It utilizes empirical MAPPINGS spectral energy distribution templates to model dusty H II regions. SKIRT meticulously models the emission, absorption, and multiple scattering of stellar light by this assigned dust, producing synthetic Spectral Energy Distributions (SEDs) and mock photometric images across the ugrizYHJK bands that account for highly complex, asymmetric dust geometries.   

In the ultraviolet and optical absorption regime, researchers seek to probe the highly diffuse circumgalactic medium (CGM), which serves as the primary reservoir for feedback-driven outflows. The TRIDENT pipeline is the premier tool for this task, used extensively with the TNG50, EAGLE, and FIRE-2 simulation outputs. Rather than modeling emission, TRIDENT generates synthetic absorption line spectra (such as Mg II, C IV, and O VI) by casting thousands of random sightlines through simulated dark matter halos. To accomplish this, TRIDENT must calculate the exact ionization state of the diffuse CGM. It achieves this by applying ionization tables that assume collisional ionization equilibrium and photoionization equilibrium driven by a time-varying metagalactic ultraviolet background, such as the widely used Haardt & Madau field. The resulting data allows theorists to map Voigt profiles to synthetic quasar absorption spectra perfectly analogous to empirical survey data.   

Finally, in the high-energy regime, the hot intracluster medium (ICM) and circumgalactic gas must be mapped into mock X-ray photon events. Pipelines such as pyXSIM, SOXS, and MOXHA dominate this space. These codes take the density, temperature, and metallicity fields of the simulated gas and calculate the thermal bremsstrahlung and metal line cooling emissivities, often utilizing the APEC plasma emission models. pyXSIM and SOXS are explicitly designed to simulate specific, real-world instruments like the Chandra X-ray Observatory's ACIS-S and ACIS-I detectors. They convert abstract emissivities into discrete synthetic photon event files, complete with instrumental effective areas, spatial resolution limits, and background noise modeling. The MOXHA pipeline has been specifically applied to the SIMBA-based Hyenas simulation suite to predict X-ray properties for both current observatories and upcoming missions like LEM.   

An additional methodological layer involves empirical SED-fitting codes such as Prospector and MAGPHYS. While these are not simulators of photons, they are inverse-problem solvers applied directly to the mock SEDs produced by SKIRT or FORECAST. They are heavily utilized on the FLARES and TNG mock datasets to determine the systematic biases inherent in recovering fundamental parameters like stellar masses and star formation rates from broadband photometry, mirroring the exact challenges faced by observational astronomers.   

3. Genuine Forward Modeling: Observables and Quantified Biases

When researchers bypass raw statistics and instead pass the simulation particle data through the rigorous pipelines mapped above, they consistently uncover massive discrepancies between what the simulation intrinsically computes and what an observer on Earth would actually measure. The literature executing these pipelines has quantified several severe observational biases that fundamentally alter the interpretation of subgrid feedback efficacy.

3.1 Cold Gas, Molecular Hydrogen, and Aperture Deficit Biases

A premier example demonstrating the absolute necessity of forward modeling is the measurement of molecular hydrogen (H2) reservoirs and the consequent environmental quenching of satellite galaxies. The delicate interplay between central AGN feedback—which primarily governs the thermodynamics of the main host halo—and environmental feedback processes such as ram pressure stripping and strangulation—which govern orbiting satellites—creates distinct, highly sensitive signatures in the cold gas distributions of galaxies.   

Using the TNG100 volume of the IllustrisTNG suite, researchers undertook a detailed analysis of the H2 mass fractions of galaxies, carefully noting their dependence on local environment, central-versus-satellite status, and total stellar mass. When analyzing the raw, intrinsic particle data directly from the simulation's subhalo catalogs, the results were stark. TNG100 intrinsically predicts that satellite galaxies with stellar masses M
∗
	​

≥10
9
M
⊙
	​

 harbor a massive, sweeping median deficit in their molecular hydrogen fractions of approximately 0.6 dex relative to central galaxies of identical stellar mass. If a researcher were to stop at this stage, they would conclude that the hydrodynamic forces within TNG100 clusters execute violently efficient gas stripping, aggressively shutting down star formation in satellites far beyond what is observed in reality.   

However, a profound shift in interpretation occurs when these identical simulated galaxies are rigorously forward-modeled to strictly match the empirical specifications of the xCOLD GASS survey, a premier carbon monoxide (CO) emission mapping project. The mock-observation pipeline applied to the TNG100 data introduces several critical, highly restrictive observational limitations. First, it enforces a strict 3-arcsec fiber aperture limitation, mimicking the exact field-of-view constraints of the SDSS spectrographs used to target the sources. Second, it incorporates extensive beam corrections to account for the spatial smearing inherent in the single-dish radio telescope observations of the CO(1-0) transition. Third, it applies complex, metallicity-dependent CO-to-H2 conversion factors (α
CO
	​

), replacing the simulation's omniscient knowledge of exact molecular mass with an empirically flawed tracer. Finally, the mock pipeline injects realistic group-finding uncertainties, acknowledging that observational algorithms frequently misclassify edge-case central galaxies as satellites, and vice versa, due to line-of-sight projection effects.   

The quantitative impact of these applied observational biases is staggering. Once aperture limits, beam smearing, conversion factor assumptions, and group-finding impurities are fully accounted for, the apparent signature of the satellite H2 deficit crashes from the intrinsic 0.6 dex down to a measurable deficit of just 0.2 dex.   

Data Provenance	Extraction Methodology	Median H2 Deficit (Satellites vs. Centrals)
TNG100 (Intrinsic)	Raw subfind particle masses	∼0.6 dex
TNG100 (Forward-Modeled)	Beam-smeared, 3-arcsec aperture, CO-traced	∼0.2 dex
xCOLD GASS (Empirical)	IRAM 30m telescope CO(1-0) observations	0.2−0.3 dex

This sequence reveals a critical, third-order insight regarding simulation validation. Without forward modeling, theorists would erroneously conclude that TNG100 vastly over-predicts satellite gas stripping relative to the observed xCOLD GASS deficit. By faithfully forward-modeling the data, they prove that the underlying simulation hydrodynamics are actually in near-perfect quantitative agreement with observations. The discrepancy lies entirely in the fact that observational selection limits, specifically the spatial constraints of the aperture and the blending effects of beam smearing, effectively "hide" approximately 66% of the underlying physical quenching signal from astronomers' view. The forward model rescues the physical model from apparent failure.   

3.2 Circumgalactic Kinematics and Absorption Line Sensitivities

The circumgalactic medium acts as the primary repository for metal-enriched, feedback-driven outflows, as well as the immediate reservoir for pristine cosmological inflows. Because the CGM is incredibly diffuse and largely collisionless, it lacks the density to emit observable thermal radiation in optical wavelengths and is therefore primarily observed via absorption spectra against background quasars. Evaluating how simulated feedback populates this expansive region is a highly sensitive test of subgrid physics.

Using the TRIDENT pipeline, researchers undertook the task of forward-modeling the high-resolution TNG50 simulation volume to perform a direct comparison with empirical data from the MusE GAs FLow and Wind (MEGAFLOW) survey. The raw hydrodynamic gas cells from the simulation were post-processed to carefully account for the complex photoionization state of the gas, assuming equilibrium in the presence of the spatially uniform Haardt & Madau metagalactic ultraviolet background. To ensure a genuine, unbiased comparison, the synthetic quasar sightlines and resulting mock spectra were filtered to perfectly mirror the empirical equivalent-width (EW) selection threshold of the MEGAFLOW survey, isolating strong Mg II absorbers where the rest-frame equivalent width W
2796
rest
	​

 exceeded 0.5 
A
˚
.   

The application of this forward-modeling pipeline yielded a highly nuanced set of quantified biases and physical revelations regarding the simulated CGM:

First, the forward models reveal a massive, highly non-linear sensitivity to the exact equivalent-width selection threshold utilized by observers. The characteristic impact parameter covering fraction (denoted as b
50
	​

, the radius within which 50% of sightlines exhibit absorption above the threshold) for the Mg II ion is highly variable. In the synthetic TNG50 data, b
50
	​

 drops almost linearly from an extended ≈65 kpc when the EW threshold is set low (>0.1 
A
˚
), down to a highly concentrated ≈20 kpc when a stringent threshold (>1.5 
A
˚
) is enforced. When evaluated across matching threshold values, both TNG50 and the EAGLE simulation generally predict lower b
50
	​

 covering fractions than those measured in empirical surveys. This specific discrepancy indicates an intrinsic failure mode in the current generation of feedback models: the kinetic winds either fail to propel cool, metal-enriched gas out to sufficiently large virial radii, or the subgrid hydrodynamics cause the cold clouds to artificially over-mix and dissolve too rapidly into the hot, shock-heated halo gas.   

Second, the mock Mg II spectra successfully reflect the immense diversity of observed CGM kinematics, revealing the presence of a "kinematic corotation bias." The synthetic absorption profiles indicate that the cold, dense phase of the CGM actively corotates with the central galactic disc at velocities reaching up to 50% of the host halo's virial velocity, extending out to impact parameters of 60 kpc. This demonstrates that empirical observations of highly kinematically shifted Mg II absorption lines along a galaxy's major axis should not be immediately interpreted as arbitrarily chaotic or purely turbulent feedback-driven outflows. Instead, they frequently represent highly structured, coherent rotating halo gas that is deeply tied to the specific angular momentum of the stellar disc.   

Third, forward modeling the CGM absorption has served as a unique diagnostic tool for highlighting catastrophic failure modes in alternative feedback variants. For instance, in experimental TNG-style runs incorporating explicit Cosmic Ray (CR) feedback physics (specifically the CR-κ
med
	​

 models), the internal non-thermal pressure driven by the cosmic rays drastically exceeds the thermal pressure within the central galaxy by a full order of magnitude. While this gross discrepancy fundamentally alters and disrupts the interior thermodynamics of the simulated galactic disc, forward modeling the extended absorption profile reveals a surprising masking effect. Beyond impact parameters of ≈15 kpc, the thermal pressure completely reasserts dominance, and the outer CGM appears perfectly normal. Thus, forward modeling demonstrates that certain severe, small-scale physical failures within a simulation can be entirely hidden from large-scale CGM absorption surveys.   

3.3 X-ray Cavities, ICM Thermodynamics, and Projection Scarcity

At the apex of the cosmic mass scale, AGN feedback originating at the centers of massive galaxy clusters injects tremendous quantities of kinetic and thermal energy into the surrounding intracluster medium (ICM). This feedback often manifests visually as prominent, macroscopic X-ray cavities or "bubbles" of hot, underdense gas rising buoyantly through the cluster atmosphere. Assessing whether hydrodynamic simulations produce realistic cavities requires immensely complex instrument modeling, primarily because these cavities do not emit radiation themselves; they are identified purely as negative spaces—deficits in the X-ray surface brightness of the surrounding bremsstrahlung emission.

To tackle this, researchers utilized the pyXSIM and SOXS software toolkits to forward-model the massive TNG-Cluster cosmological volumes. They generated highly specific mock images mimicking the Chandra X-ray Observatory, perfectly matching the exposure times, background noise profiles, and specific detector characteristics (ACIS-S and ACIS-I arrays) of a volume-limited observational sample of 35 real-world galaxy clusters. Concurrently, the MOXHA package was heavily deployed on the SIMBA-based Hyenas zoom-in simulations to create synthetic Chandra maps, as well as predictive models for the upcoming Line Emission Mapper (LEM) mission. Both forward-modeling pipelines intentionally employed standard observational extraction techniques—such as extreme unsharp masking and model-subtracted residual mapping—to force the synthetic data through the same interpretive hurdles used to locate empirical bubbles.   

These forward-modeling efforts yielded highly significant insights into both the successes of the models and the insidious nature of observational projection biases:

Abundance and Morphological Demographics: The heavily processed TNG-Cluster mocks reveal that approximately 39% of the simulated clusters at redshift z=0 contain definitively identifiable X-ray cavities. This theoretical prediction aligns remarkably well with the 35−43% cavity occurrence fraction observed in the carefully matched empirical Chandra sample. Furthermore, the simulations successfully reproduce the broad distribution of macroscopic cavity sizes, spanning from a few kiloparsecs to several tens of kiloparsecs in radius, and accurately form the associated bright, weak-shock rims featuring realistic Mach numbers of ≈1.5.   

The Size-Distance Scarcity Bias: Despite the overarching demographic success, the strict Chandra-matching process highlighted a highly specific, localized failure mode. While general morphological features align on large scales, the simulated cavities in TNG-Cluster that remain physically attached to the central SMBH core are systematically larger than their observed counterparts. Conversely, the synthetic maps reveal a distinct scarcity of small cavities (diameters <10 kpc) close to the cluster core. The forward modeling proves this is not an artifact of the mock telescope's resolution limits, but an intrinsic inability of the simulation's subgrid injection mechanism to form highly localized, small-scale disruptions in the extreme density of the inner core.   

Fundamental Feedback Mechanism Validation: The very presence of these identifiable mock bubbles in TNG-Cluster carries profound physical implications. The IllustrisTNG model utilizes a relatively simple, purely kinetic wind prescription for its low-accretion AGN feedback mode, injecting momentum isotropically or in wide angles. It explicitly does not model the collimated, highly relativistic bipolar jets commonly assumed to be the progenitors of cluster bubbles. The rigorous forward models prove conclusively that large-scale, quantitatively realistic X-ray cavities can form naturally in a highly stratified cluster atmosphere via episodic, non-collimated kinetic injections. This demonstrates that resolving extreme bipolar jet physics is not a strict fluid-dynamical prerequisite for producing the macroscopic cavity structures observed by Chandra. Similarly, the SIMBA-based Hyenas mocks successfully demonstrate that an alternative approach—torque-limited accretion explicitly coupled with subgrid bipolar jet models—yields mock cavity enthalpies spanning 10
41
 to 10
44
 erg/s, perfectly matching the observed excess energies required to offset cooling in low-mass halos.   

3.4 Quenching Kinetics and the Green Valley (TNG vs. EAGLE vs. SDSS)

The transition of galaxies from the actively star-forming "blue cloud" across the sparse "green valley" and onto the passive "red sequence" is one of the most critical processes in cosmic evolution. This transition rate is highly sensitive to the exact physical implementation of SMBH feedback. To robustly compare the low-redshift, BPT-selected pure optical AGN hosts found in the SDSS DR7 dataset to synthetic analogues in the TNG100 and EAGLE simulations, rigorous forward modeling of photometric colors and instrumental apertures is absolutely required.   

Gawade (2025) applied a meticulous mock selection pipeline to these datasets. To eliminate cross-dataset systematic errors, the green valley was defined internally within each dataset using precise (g−r) color percentiles. For the simulation data, this necessitated extracting rest-frame synthetic colors that were specifically constrained within a strict 30 kpc physical aperture. This aperture matching was essential to mimic the precise spatial limits of the SDSS observed-frame spectroscopic fibers, which routinely miss extended star formation in the outer disks of galaxies.   

This aperture-matched forward modeling exposes dramatic, fundamental differences in the physical quenching pathways executed by the different subgrid models:

The TNG Over-Quenching Crisis: Within the synthetic green valley, TNG100 central galaxies are found to be almost entirely and unnaturally quenched. They exhibit a sharp, unphysical pile-up exactly at the simulation's imposed numerical star formation rate floor. This results in a synthetic median specific Star Formation Rate (sSFR) of log
10
	​

(sSFR)≃−14.85. This theoretical median sits an astonishing ∼3.5 dex below the empirical SDSS median. The forward model proves that TNG's kinetic feedback implementation acts far too violently, clearing the green valley with unnatural efficiency and resulting in artificially high green-valley occupancy fractions (reaching ≳60% near 10
11
M
⊙
	​

) that are locked in a fully quenched state.   

The EAGLE Continuous Transition: In stark contrast, EAGLE's implementation of thermal, highly stochastic AGN feedback produces a broad, continuous sSFR distribution across the mock green valley, yielding a median log
10
	​

(sSFR)≃−11.71. This synthetic distribution shows substantial, realistic overlap with the SDSS observational data. It remains robust even when varying the lower percentile boundaries of the green valley definition.   

The crucial insight here is that while both the TNG and EAGLE simulations successfully reproduce global macroscopic statistics—such as the z=0 overall stellar mass function—their specific thermodynamic pathways across the green valley differ fundamentally. Forward modeling reveals that global mass function matching is insufficient to guarantee realistic quenching kinetics.   

3.5 Faint-End Photometric Deficits and the Insidious Outshining Bias

High-redshift observations via premier space observatories like JWST and HST (encompassing deep fields like CANDELS and CEERS) present unique interpretive challenges. Genuine forward modeling in this high-redshift domain requires intricately translating complex, irregular stellar populations through highly turbulent dust geometries to produce mock multi-band synthetic imaging.

Using the FORECAST pipeline, researchers generated extensive mock CANDELS GOODS-South light cones directly from the TNG100 and EAGLE outputs. The forward modeling revealed a distinct and highly problematic "faint-end deficit" in the synthetic galaxy counts emerging precisely at redshifts z≳3. By meticulously simulating the exact photon depth and detection thresholds of the GOODS-South survey, researchers could systematically test whether this missing population of faint, high-z galaxies was simply hidden below the detection threshold due to observational signal-to-noise limitations. By artificially deepening the exposure times of the mock images in post-processing, they successfully recovered the observed counts near the luminosity peak, but systematically overpredicted the faintest sources. This proved conclusively that instrumental depth alone cannot resolve the tension. Instead, a detailed analysis of the morphological structural parameters of the mocks revealed an intrinsic simulation bias. The hydrodynamic solvers in both TNG100 and EAGLE are structurally biased toward producing overly diffuse, low-surface-brightness stellar systems. They fundamentally fail to assemble the faint, highly compact galaxies with intensely bright central cores that dominate the real, empirical GOODS-South deep field data.   

Furthermore, applying advanced Bayesian SED-fitting codes like Prospector or MAGPHYS to mock synthetic spectra (e.g., from the FLARES and TNG simulation suites) reveals the presence of the insidious "outshining" bias. In the early universe, massive bursts of young, extremely luminous OB stars completely dominate the rest-frame UV and optical continuum, as well as the nebular line emission. When a mock SED is processed through standard empirical Markov Chain Monte Carlo (MCMC) fitting algorithms, the overwhelming luminosity of the recent burst heavily weights the statistical fit. This process systematically and mathematically "hides" the older, underlying stellar populations from the fitter.   

Consequently, studies that blindly apply Prospector to mock data discover that the simulation particles contain systematically higher actual, intrinsic stellar masses compared to what the SED-fitter successfully extracts from the mock light. Concurrently, the fitter infers artificially lower SFRs because the infrared dust heating generated by the older, hidden stellar populations is erroneously misattributed entirely to the young starburst. Forward modeling proves that high-z observational mass estimates may be systematically depressed simply because the oldest stars are outshone by their younger siblings.   

4. Raw Simulation Statistics: Feedback Predictions Lacking Genuine Forward Models

While highly sophisticated mock observables have become the gold standard for evaluating X-ray cavities, optical photometry, and CGM absorption kinematics, several critical feedback-relevant predictions are still routinely and problematically compared to observations using only raw simulation statistics.

4.1 Radio AGN and Jet Kinetic Power Estimations

Radio-mode feedback is theorized to be the critical physical mechanism responsible for heating the halo gas and permanently suppressing late-time star formation in massive elliptical galaxies. However, explicitly resolving the generation of non-thermal synchrotron emission from relativistic electron populations trapped in expanding magnetic radio lobes requires complex cosmic ray transport physics and extreme magnetohydrodynamics. This is currently far beyond the standard subgrid computational capabilities of premier cosmological simulations like SIMBA and EAGLE.   

Consequently, when attempting to compare simulated AGN activity to deep empirical radio surveys (such as those from LOFAR or MIGHTEE), researchers are forced to utilize raw subgrid accretion statistics scaled through empirical relations, rather than engaging in genuine forward modeling of the radio continuum emission. For instance, in the SIMBA simulation—which uniquely implements a dual-mode accretion model featuring Bondi accretion from hot gas (triggering jets) and torque-limited accretion from cold gas (triggering radiative winds)—researchers rely heavily on the theoretical scaling relations derived by Körding et al. (2008) to estimate jet kinetic powers. They map the raw, intrinsic Bondi accretion rate recorded in the simulation directly to a theoretical mechanical jet power. They then invert purely observational scaling relations to estimate a mock 1.4 GHz radio luminosity (L
1.4 GHz
	​

) for the simulated halo.   

While this statistical mapping allows theorists to rapidly plot comparisons against empirical radio luminosity functions, it is fundamentally a parameterized statistical mapping, not a physical forward model. It completely ignores the rich, highly variable physics of physical lobe expansion, adiabatic losses, complex magnetic field topologies, and the spectral aging of the synchrotron plasma via inverse Compton scattering off the Cosmic Microwave Background—all of which true mock observables would natively encapsulate. Using this purely statistical methodology, the SIMBA simulation exhibits a concerning 0.3−0.4 dex shortfall in its total kinetic luminosity density across cosmic time compared to empirical observations. This suggests that reproducing the passive massive galaxy population at z=0 actually requires a significantly higher heating output from the AGN than what is currently inferred from the empirical data.   

4.2 Global Cosmological Molecular Mass Functions

Similarly, while highly focused, zoomed-in environmental studies perform detailed, beam-matched mock observations of molecular hydrogen (as detailed extensively in Section 3.1), global cosmological comparisons of the overarching H2 Mass Function (H2MF) often inexplicably rely on raw subgrid phase partitioning. In the SIMBA, EAGLE, and IllustrisTNG suites, the total hydrodynamic gas mass within a cell is partitioned into ionized, atomic (H I), and molecular (H2) phases using highly specific theoretical subgrid prescriptions (such as the Krumholz or Gnedin shielding models).   

When publishing global mass functions across large cosmological volumes, researchers frequently bypass the mock pipeline. They simply sum these raw, theoretically partitioned subgrid particle masses and plot them directly against CO-derived observational mass functions from surveys like xCOLD GASS. By doing so, they completely bypass the highly uncertain, non-linear step of simulating the full non-LTE radiative transfer of the CO(1-0) emission line through the giant molecular clouds, and they ignore the systemic uncertainties of assuming a constant or metallicity-dependent α
CO
	​

 conversion factor. This creates a false equivalency between theoretical gas mass and observational CO luminosity, undermining the validation of the global mass function.   

5. The Selection-Function Ledger

The rigorous application of complete forward-modeling pipelines reveals precisely how specific observational selection functions and instrumental limitations severely distort our perception of intrinsic physical reality. The following ledger synthesizes the major quantified biases exposed by the literature reviewed in this report:

Observable Domain	Primary Simulation	Forward-Modeling Pipeline	Quantified Bias / Effect of Selection Function
Molecular Gas (H
2
	​

) Deficit	TNG100	Beam-matching, Aperture cuts	

Raw satellite deficit of ~0.6 dex is artificially reduced to ~0.2 dex due to 3-arcsec fiber limits and group-finding impurities, perfectly matching xCOLD GASS data.


X-ray Cavities (ICM)	TNG-Cluster, SIMBA	pyXSIM, SOXS, MOXHA	

Replicates 35-43% cavity abundance. Highlights that small, attached cavities (<10 kpc) are intrinsically scarce in TNG compared to Chandra spatial resolution limits.


CGM Mg II Absorption	TNG50	TRIDENT	

Strict EW thresholding (>0.1 to >1.5 
A
˚
) linearly and artificially reduces derived impact parameter covering fractions (65 kpc down to 20 kpc). TNG severely underestimates covering fractions at high EW thresholds.


High-z SED Photometry	TNG100, EAGLE	FORECAST	

Faint-end deficit at z≳3 in CANDELS mimics is not a depth or selection issue, but an intrinsic failure of the hydrodynamic solvers to form compact, bright stellar cores.


Stellar Mass & SFR	FLARES, TNG	Prospector, MAGPHYS	

Outshining bias: Parametric MCMC SFH fits to mock spectra systematically underestimate old stellar mass and misattribute infrared dust heating to young stars, leading to derived masses lower than intrinsic reality.


Green Valley sSFR	TNG100, EAGLE	30 kpc aperture synthetic colors	

TNG's kinetic feedback intrinsically over-quenches, trapping galaxies at the numerical SFR floor (∼3.5 dex below SDSS medians). EAGLE's thermal feedback remains robust to percentile variations.

  

By isolating the effects detailed in this ledger, theorists can systematically disentangle which discrepancies represent genuine failures of the physical subgrid models (e.g., the faint-end structural deficit) versus which discrepancies are merely artifacts of the observational process (e.g., the H2 deficit compression).

6. Per-Observable Discrimination Power

The ultimate architectural goal of forward modeling is not simply to mimic telescope images, but to achieve sufficient statistical discrimination power to confidently rule out specific, competing subgrid feedback mechanisms.

The most powerful discriminator identified across the current literature is the X-ray cavity and ICM thermodynamics morphology. Because macroscopic cavities represent the direct integration of AGN kinetic energy over deep cosmological time into the surrounding ICM, forward modeling mock Chandra maps severely discriminates between feedback styles. The fact that TNG-Cluster generates quantitatively realistic cavities via relatively simple, non-collimated kinetic winds , while SIMBA produces them via highly explicit, theoretical bipolar jets , proves a crucial hydrodynamic principle. The spatial distribution of the energy injection (isotropy versus strict collimation) is significantly less critical to cavity formation than the pure momentum-to-energy ratio, provided the cluster atmosphere is appropriately stratified. However, the exact thermodynamics of the weak-shock rims and the survival rate of the <10 kpc inner cavities offer immense, highly sensitive discrimination power that raw energy statistics simply cannot capture or represent.   

Conversely, global optical colors, aperture-matched sSFR distributions, and BPT diagrams offer unparalleled discrimination power regarding the timing and efficiency of feedback mechanisms. The massive, 3.5 dex discrepancy in the synthetic green valley between TNG (which exhibits an over-quenching pile-up) and EAGLE (which exhibits a continuous flow) indicates that TNG's kinetic wind velocity threshold evacuates cold molecular gas far too violently compared to EAGLE's highly stochastic, delayed thermal heating. Forward modeling strictly using 30 kpc physical apertures proves conclusively that this is an intrinsic, fundamental physical difference in the hydrodynamics of the models, not merely an observational artifact of attempting to measure extended, diffuse star formation in the simulation outskirts.   

7. Known Failure Modes and Critical Methodological Gaps

The rigorous comparison of high-fidelity mocks to deep observational data exposes two distinct classes of failure: intrinsic physical failures rooted within the simulations' governing equations, and profound limitations within the forward-modeling pipelines themselves.

7.1 Intrinsic Simulation Failure Modes

The Faint-End Compactness Crisis: As definitively quantified by the FORECAST pipeline, state-of-the-art simulations like TNG and EAGLE structurally and physically fail at high redshifts (z≳3) to produce faint galaxies featuring bright, highly compact central cores. The hydrodynamic solvers intrinsically favor diffuse, overly extended, low-surface-brightness systems. This leads to a permanent, unresolvable shortfall in synthetic source counts against deep surveys like GOODS-South, regardless of how much artificial image deepening is applied to the mock data.   

Over-Evacuation of the Green Valley: IllustrisTNG's kinetic AGN feedback implementation acts far too aggressively on intermediate-mass hosts. Rather than allowing a slow transition across the color-magnitude diagram, it forces transitional galaxies to abruptly and unnaturally pile up at the absolute artificial numerical SFR floor.   

CGM Radial Depletion and Mixing: In the high-resolution TNG50 volume, while the inner kinematics match observations, the Mg II covering fractions drop off far too rapidly at extended impact parameters relative to the empirical MEGAFLOW data. This suggests an intrinsic hydrodynamic flaw: the feedback mechanisms either fail to loft cold metals to the outer reaches of the halo, or the subgrid mixing prescriptions cause the cold clouds to dissolve and heat too rapidly within the hot coronal gas.   

7.2 Pipeline and Methodological Gaps

The Absence of Synchrotron Radiative Transfer: The most glaring, systematic gap in current forward modeling is the complete absence of robust, physically motivated radio continuum mocks. Relying entirely on theoretical Bondi-to-Jet-Power scaling relations  blatantly ignores the rich plasma physics of physical lobe expansion, spectral aging, and magnetic field topology. Until computational pipelines can robustly mock LOFAR and MIGHTEE data via genuine radiative transfer of cosmic ray electrons, radio-mode feedback remains only statistically, not observationally, validated.   

Ionization Equilibrium Assumptions in the CGM: Pipelines like TRIDENT generally operate under the strict assumption of collisional ionization equilibrium and a perfectly uniform metagalactic UV background. They frequently struggle to accurately mock non-equilibrium cooling flows, turbulent mixing layers, or the highly complex photoionization structures created by local, flickering AGN. This critical limitation can heavily bias the derived column densities for highly ionized tracer species like O VI or C IV, creating false discrepancies between the simulation and reality.   

8. Public Data Products and Link Infrastructure Ledger

To foster reproducibility, accelerate community engagement, and allow independent observers to generate their own bespoke mock observables, the major theoretical collaborations have made massive quantities of both their raw particle data and pre-computed forward-modeled catalogs publicly available.

IllustrisTNG & TNG-Cluster: The collaboration hosts comprehensive raw snapshots, subfind subhalo catalogs, merger trees, and selected mock catalogs (including the GalSyn optical outputs).

Infrastructure: Data is served via www.tng-project.org/data and the dedicated cluster portal at www.tng-project.org/cluster/.   

EAGLE & EAGLE-SKIRT: The EAGLE collaboration provides standard particle data alongside the highly utilized, specialized EAGLE-SKIRT database. This repository houses pre-computed optical and NIR synthetic photometry and complex dust observables for thousands of simulated galaxies, seamlessly integrated with observational databases.

Infrastructure: Accessible via http://eagle.strw.leidenuniv.nl/ and heavily integrated into the broader DustPedia archival network.   

SIMBA: Raw snapshot data, highly specific Caesar halo catalogs, and the critical feedback variant runs are accessible for generating Hyenas-style MOXHA X-ray mocks and for computing the requisite radio scaling relations.

Infrastructure: Data is hosted centrally at http://simba.roe.ac.uk/.   

FIRE (Feedback In Realistic Environments): The FIRE-2 suite is actively released and maintained, including full, unadulterated zoom-in snapshots and advanced particle tracking data. This ultra-high-resolution data is absolutely essential for resolving the multiphase ISM when executing synthetic spectra mapping.

Infrastructure: Served via the Flatiron Institute at flathub.flatironinstitute.org/fire.   

ROMULUS: The Romulus simulations (including the Romulus25 cosmological box and the RomulusC cluster zoom-in) heavily utilize the Python-based pynbody analysis framework and the TANGOS database for rapidly querying SMBH dynamics and galactic environments.

Infrastructure: While primary analysis scripts are hosted on GitHub (e.g., https://github.com/mtremmel/tremmel2023_mbh_occFrac), access to the full TANGOS relational database is generally coordinated via direct request to the primary authors.   

9. Conclusion

The methodological transition from comparing raw, intrinsic simulation outputs to executing genuine, rigorous forward modeling marks a critical, irreversible maturation in the field of computational astrophysics. As extensively demonstrated throughout this analysis, raw statistics are fundamentally deceptive when viewed through an observational lens. Relying on them directly leads to the creation of false physical tensions—such as the historically erroneous belief that TNG100 radically over-strips the molecular gas in its orbiting satellites —or dangerously obscures intrinsic subgrid failures, such as the outshining effect completely masking massive, old stellar populations at high redshift from standard SED fitters.   

By routing state-of-the-art hydrodynamic particle data through dedicated pipelines like SKIRT, TRIDENT, and pyXSIM, theoretical researchers have successfully constrained the physical architecture of cosmic feedback with unprecedented accuracy and nuance. Through these mock observables, we now understand that AGN kinetic winds can naturally and organically carve out macroscopic X-ray cavities in a stratified medium without necessitating the invocation of highly rigid relativistic jets. Furthermore, we recognize that the cold circumgalactic gas maintains significant, highly structured angular momentum far out into the dark matter halo, corotating with the inner disc.   

However, the vanguard of this research must now aggressively address the lingering, systemic gaps. Generating genuine radio continuum mocks remains a largely unsolved computational challenge, heavily limiting the strict observational validation of jet feedback energetics. Furthermore, the intrinsic structural failures exposed by the forward models—such as the systemic inability of fluid solvers to resolve compact, faint starburst cores at high redshift, and the overly aggressive quenching kinetics identified within the green valley—highlight the ongoing necessity to continually refine subgrid physics. As next-generation observatories like JWST, the Line Emission Mapper (LEM), and ATHENA push our empirical detection thresholds deeper into the cosmos, the complexity and rigor of our forward modeling pipelines must evolve in tandem to ensure our simulated universes accurately reflect the majestic complexity of empirical reality.   

End of Report

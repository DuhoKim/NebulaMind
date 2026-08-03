Joint C1R answer — REQ_JOINT_C1R_20260712T045317Z

Run date (UTC): 2026-07-12T06:48:00Z
Model: Gemini Pro (selected UI mode; backend version not exposed)
Simulations covered: 8

1. Calibration ledger
Simulation (method-paper citation)	Stated calibration targets (faithful to source wording)	Feedback parameters tuned (as stated)	Explicitly emergent (stated NOT calibrated)	Notes


IllustrisTNG 

	

The project specifically targeted the observed galaxy stellar mass function, the stellar-to-halo mass scaling relation, the total gas mass content evaluated strictly within the virial radius, the central supermassive black hole mass to galaxy mass or halo mass relation, and the galaxy stellar sizes specifically represented by effective radii, utilizing these physical quantities as rough guidelines to explicitly engineer the baseline subgrid model behavior prior to conducting predictive science runs.

	

The developers explicitly adjusted the parameters governing galactic winds, specifically modifying their directionality, bulk velocity, thermal energy content, and phenomenological energy scalings, while simultaneously implementing and tuning a revised black-hole-driven kinetic feedback model intended to operate effectively during low accretion rate states to ensure massive galaxies appropriately quench their star formation without violating local empirical constraints.

	

The spatial distribution of the stellar mass in the most massive haloes (M200c ≳10
14
 M$_{\odot}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE) was explicitly stated to be an emergent phenomenon occurring in a mass regime where the galaxy physics model was never directly calibrated or even previously run prior to the execution of the TNG300 simulation itself, rendering the structural properties of these simulated clusters genuinely predictive rather than engineered.

	

The specific parameter values adopted for the reference IllustrisTNG physical model were kept strictly identical across all variations in numerical resolution, explicitly avoiding the practice of resolution-dependent parameter retuning across the different simulation volumes.




EAGLE 

	

The subgrid physics model was explicitly calibrated to reproduce the observed redshift z=0.1 UNCERTAINTY_NOT_QUOTED_BY_SOURCE galaxy stellar mass function and the scaling relation between the stellar mass of galaxies and their central supermassive black hole mass, whilst simultaneously seeking to yield simulated galaxies with physical sizes measured via effective radii that are statistically similar to local astronomical observations.

	

The subgrid routines governing the energetic feedback associated with both star formation and the accretion growth of black holes were varied; specifically, the stellar feedback calibration exclusively varied the energy coupling efficiency parameter representing the fraction of available Type II Supernovae energy coupling to the interstellar medium, while the black hole feedback was regulated by tuning the subgrid viscosity parameter alongside a fixed heating temperature increment of 10
8.5
 K UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

	

The study authors explicitly stated that the calibrated simulations broadly reproduce the observed galaxy stellar mass function as early as redshift z=7 UNCERTAINTY_NOT_QUOTED_BY_SOURCE, accurately track its evolution to the present day, and successfully match a diverse, representative set of low-redshift observables that were strictly withheld from the calibration process.

	

The calibration process necessitated adjusting the star formation feedback parameters such that the injected energy varies as a function of the local gas density, mitigating spurious numerical radiative losses that otherwise suppress feedback efficiency in high-density regions.




SIMBA 

	

The primary calibration strategy for this cosmological hydrodynamic simulation focuses stringently on reproducing the global galaxy stellar mass function evolution across cosmic time alongside the local empirical scaling relation bridging central supermassive black hole mass and host galaxy stellar mass, utilizing these macroscopic distributions as the fundamental anchor points to which the energetic outputs of the subgrid feedback modules are explicitly tuned.

	

The simulation explicitly tuned the fraction of material entering the accretion disc that actually accretes onto the central black hole to a value of ∼10% UNCERTAINTY_NOT_QUOTED_BY_SOURCE, while simultaneously calibrating the kinetic feedback ejection velocities based on Eddington ratios to scale from ∼10
3
 km s$^{-1}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE at high accretion rates to ∼8000 km s$^{-1}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE at low accretion rates, utilizing a constant momentum input of 20 L/c UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

	

The model produces a wide array of emergent properties that successfully reproduce observational constraints without direct tuning, including neutral and molecular gas fractions (TRACER=H I and H2 mass; SELECTION=galaxies; DENOMINATOR=total mass; REDSHIFT=0 UNCERTAINTY_NOT_QUOTED_BY_SOURCE), the mass-metallicity relation at redshift z≈0 UNCERTAINTY_NOT_QUOTED_BY_SOURCE and redshift z≈2 UNCERTAINTY_NOT_QUOTED_BY_SOURCE, star-forming galaxy sizes, and the properties of cosmic dust.

	

Analysis of specific simulation variants lacking jet and X-ray feedback modules revealed that the carefully tuned high-velocity jet feedback is primarily responsible for the successful quenching of massive galaxies and significantly alters late-time cosmic cold gas evolution.




FIRE/FIRE-2 

	

The method papers indicate that there is no fine-tuning or direct calibration of any parameters in the simulations to match these specific macroscopic observational properties, as the models attempt to explicitly capture the interstellar medium physics and stellar feedback mechanisms directly from stellar evolution models rather than employing phenomenological macroscopic tuning.

	

NONE_FOUND.

	

The simulations report that galaxy-scale properties naturally emerge from the underlying microphysics, specifically noting that as numerical resolution increases, stellar masses and density profiles converge first, followed by metal abundances and visual morphologies, and subsequently the complex properties of galactic winds and the circumgalactic medium.

	

While the overarching properties are physically emergent, the central kiloparsec mass concentrations of massive galaxies remain sensitive to underlying numerical implementations, particularly regarding how explicitly ejected winds are trapped, mixed, and recycled within the hot circumgalactic halos.




ROMULUS 

	

The simulation utilized a multi-dimensional parameter search to optimize the subgrid parameters regulating star formation and feedback directly against a comprehensive set of redshift z=0 UNCERTAINTY_NOT_QUOTED_BY_SOURCE galaxy scaling relations, specifically including the stellar mass-halo mass relation, the black hole mass-stellar mass relation, and the multi-epoch colour-colour history of Milky Way and M31 progenitors.

	

The developers optimized specific free parameters controlling the supermassive black hole accretion rate and the efficiency at which radiated energy is transferred to the surrounding gas, alongside stellar parameters such as the star formation threshold density, the star formation efficiency, and the supernova feedback efficiency which was explicitly set to 0.75 UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

	

The novel implementation of supermassive black hole physics allows the simulation to predict where and when supermassive black holes grow entirely independent of any predefined assumptions about the specific host galaxies they exist in, generating global star formation and black hole accretion histories that emerge naturally from the physics.

	

The explicit calibration of the blastwave supernova feedback implementation was uniquely targeted to reliably reproduce observable dwarf galaxy structures, specifically focusing on generating realistic cored dark matter density profiles in low-mass systems.




ASTRID 

	

The subgrid model suite was explicitly validated and calibrated to show good statistical agreement with observed ultraviolet luminosity functions, galaxy stellar mass functions, and specific star formation rates, with the dust model specifically calibrated at redshift z=0 UNCERTAINTY_NOT_QUOTED_BY_SOURCE using Sloan Digital Sky Survey luminosity functions before being tested at higher redshifts.

	

The simulation explicitly tuned the supernova feedback energy parameter to 1.0 UNCERTAINTY_NOT_QUOTED_BY_SOURCE (in units of 10
51
 erg UNCERTAINTY_NOT_QUOTED_BY_SOURCE), the wind speed parameter to 3.7 UNCERTAINTY_NOT_QUOTED_BY_SOURCE (in units of local dark matter velocity dispersion), the average number of star particles produced per gas particle to 4 UNCERTAINTY_NOT_QUOTED_BY_SOURCE, and the black hole feedback efficiency to 0.05 UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

	

The simulation yields a supermassive black hole population that is broadly consistent with empirical constraints on the black hole mass function, the bright end of the luminosity functions, and the time evolution of black hole mass and accretion rate density without these explicit relations being used as direct tuning targets.

	

The unique black hole dynamic implementation explicitly includes mergers driven by dynamical friction from stars rather than relying on the common practice of artificial repositioning, generating significant delays for black hole mergers post-encounter.




FLAMINGO 

	

The subgrid feedback models were strictly calibrated using Gaussian process emulation to match the redshift z=0 UNCERTAINTY_NOT_QUOTED_BY_SOURCE galaxy stellar mass function and the low-redshift cluster gas mass proportions (TRACER=gas mass; SELECTION=clusters; DENOMINATOR=total mass; REDSHIFT=low-z UNCERTAINTY_NOT_QUOTED_BY_SOURCE) evaluated within the M
500c
	​

 radius, recognizing that baryonic effects become increasingly important as observations move to smaller cosmological scales.

	

The emulation process specifically varied and tuned the stellar feedback efficiency, the target kick velocity for stellar feedback winds, the power-law slope of the density dependence governing the black hole accretion boost factor, and the active galactic nucleus heating temperature, adapting these parameters distinctly across the three different numerical resolution levels.

	

The calibrated simulations successfully reproduce a variety of complex cluster scaling relations and thermodynamic density and temperature profiles that were strictly excluded from the initial machine-learning-driven Gaussian process emulation and calibration methodology.

	

The project uniquely generated twelve variations of the flagship intermediate-resolution simulation by explicitly shifting the calibration data targets relative to their fiducial observational values by specified standard deviations, creating a controlled suite to test the impact of varying feedback strengths on large-scale structure.




BAHAMAS 

	

The project represents a targeted attempt to explicitly calibrate the subgrid models of stellar and active galactic nucleus feedback to successfully reproduce the present-day galaxy stellar mass function and the observed hot gas mass proportions (TRACER=hot gas mass; SELECTION=groups and clusters; DENOMINATOR=total mass; REDSHIFT=0 UNCERTAINTY_NOT_QUOTED_BY_SOURCE) in order to ensure the back-reaction effects of feedback on the overall cosmic matter distribution are of the broadly correct physical magnitude.

	

The calibration sequence systematically adjusted the stellar feedback wind velocity to match the lower-mass end of the stellar mass function, the mass of gas heated by active galactic nuclei to reproduce the high-mass knee of the mass function, the heating temperature to match the cluster gas fractions, and the black hole feedback efficiency to reproduce the local scaling relation between black hole and stellar mass.

	

The calibrated simulations inherently reproduce an unprecedentedly wide range of independent properties of massive systems, successfully yielding the various complex observed observational mappings between galaxies, hot gas distributions, total mass profiles, and central supermassive black holes.

	

The study stresses that obtaining the correct total baryon fraction is a fundamental prerequisite for utilizing hydrodynamical simulations in precision large-scale structure cosmology, motivating the explicit decision to calibrate directly against cluster gas fractions.

  
2. Out-of-sample validation ledger
Simulation	Observable	Result (agreement or tension, with magnitude)	COMPARABILITY	Overlap with a Section-1 calibration target	Citation
IllustrisTNG	Galaxy color bimodality distribution	Agreement (the simulation demonstrates a striking improvement relative to previous models, achieving excellent quantitative agreement with observed data featuring a sharp transition in median color from blue to red at a characteristic stellar mass of M
∗
	​

∼10
10.5
 M$_{\odot}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	MATCHED_SELECTIONS	No	
EAGLE	Specific star formation rate to stellar mass relation at intermediate redshifts	Tension (the simulated specific star formation rate relation is steeper than observed at all measured redshifts, and the empirically observed relations possess a significantly higher normalisation at redshift z∼1 UNCERTAINTY_NOT_QUOTED_BY_SOURCE and redshift z∼2 UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	MATCHED_SELECTIONS	No	
SIMBA	Molecular gas mass distributions	Tension (the model exhibits systemic tension with observational data by significantly overproducing the molecular hydrogen mass proportions (TRACER=H2 mass; SELECTION=galaxies; DENOMINATOR=total mass; REDSHIFT=0 UNCERTAINTY_NOT_QUOTED_BY_SOURCE) despite matching the underlying galaxy stellar mass function accurately)	MATCHED_SELECTIONS	No	
FIRE/FIRE-2	Visual morphologies and central mass concentrations in massive galaxies	Agreement (the model produces galaxy-scale properties such as metal abundances and visual morphologies that converge well with increasing numerical resolution, though central kiloparsec mass concentrations remain highly sensitive to how efficiently winds are trapped and recycled)	MATCHED_SELECTIONS	No	
ROMULUS	Dual active galactic nucleus frequency	Agreement (the simulation accurately yields dual AGN demographic frequencies (TRACER=dual active galactic nuclei; SELECTION=massive galaxies; DENOMINATOR=total active galactic nuclei; REDSHIFT=NOT_APPLICABLE) that can be directly and successfully compared against larger contexts due to the physically motivated exploration of black hole dynamics without artificial repositioning)	MATCHED_SELECTIONS	No	
ASTRID	Supermassive black hole mass and luminosity functions	Agreement (the predicted supermassive black hole population remains broadly consistent with empirical constraints regarding the black hole mass function and the bright end of the luminosity functions, demonstrating significant agreement at early epochs prior to redshift z=3 UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	MATCHED_SELECTIONS	No	
FLAMINGO	Kinetic Sunyaev-Zel'dovich effect of SDSS BOSS galaxies	Tension (rigorous analysis comparing the simulation to Planck and ACT stacking measurements reveals a prominent tension where the observational measurements strongly prefer a higher level of energetic feedback than is natively predicted by the simulation variants originally calibrated to local cluster gas fractions)	MATCHED_SELECTIONS	No	
BAHAMAS	Cosmic shear and matter power spectrum clustering	Tension (the simulation faces persistent tension when tested against weak lensing constraints and the S8 parameter, as the specific models implementing sufficiently strong feedback to resolve the S8 clustering tension fundamentally disagree with the X-ray-inferred cluster gas fractions utilized as the primary calibration target)	MATCHED_SELECTIONS	No	
  
3. Double-counting warnings

Researchers explicitly caution that a comprehensively calibrated cosmological simulation fundamentally loses its predictive power for the specific empirical scaling relations utilized during the calibration phase, noting that while the framework can still make genuine predictions at other cosmological redshifts and for physical quantities that were strictly withheld as calibration targets, any successful reproduction of the explicitly targeted data must be viewed entirely as an engineered mathematical outcome rather than an independent theoretical validation of the underlying physical model.    

It is prominently emphasized in the methodological literature that calibrating complex subgrid physics models by forcing their outputs to match a pre-selected suite of benchmark observations represents a necessary but significant scientific sacrifice, resulting in a partial forfeit of the numerical model's intrinsic predictive power; this inherent limitation requires computational scientists to rigorously and transparently balance exactly how many macroscopic observables they force the subgrid parameter space to match versus how many subsequent physical results can legitimately and ethically be deemed independent, out-of-sample predictions.    

The specific methodological approach of explicitly tuning subgrid control parameters to simultaneously match the observed galaxy stellar mass function and the hot gas mass distributions (TRACER=hot gas mass; SELECTION=groups and clusters; DENOMINATOR=total mass; REDSHIFT=0 UNCERTAINTY_NOT_QUOTED_BY_SOURCE) is rigorously described in the literature as an essential strategy to ensure the macroscopic back-reaction of baryons on the underlying dark matter distribution occurs at the correct physical magnitude for cosmological studies, but this explicit engineering inherently precludes investigators from utilizing those exact same low-redshift thermodynamic observables to subsequently validate the fundamental accuracy of the subgrid active galactic nucleus feedback physics.    

4. Feedback-relevant observables map
Simulation	Quenched fractions	Gas fractions of passive galaxies	Outflow demographics	Hot-halo/cavity properties	Radio-AGN incidence
IllustrisTNG	

EMERGENT 

	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	

EMERGENT 


EAGLE	

EMERGENT 

	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	

EMERGENT 


SIMBA	

EMERGENT 

	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	

EMERGENT 


FIRE/FIRE-2	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	

EMERGENT 

	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND
ROMULUS	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND
ASTRID	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND
FLAMINGO	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	

CALIBRATED 

	NOT_REPORTED — NONE_FOUND
BAHAMAS	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	NOT_REPORTED — NONE_FOUND	

CALIBRATED 

	NOT_REPORTED — NONE_FOUND
  
5. Gaps

GAP: The theoretical and observational community lacks a definitive physical consensus on how to construct a unified subgrid feedback model that simultaneously reproduces the macroscopic thermodynamic gas properties of low-redshift galaxy clusters and the small-scale clustering amplitude measured by cosmic shear and weak lensing surveys, creating a persistent, unresolved tension where simulation models calibrated explicitly to the former systematically fail to accurately predict the latter. 
GAP: Detailed structural and kinematic measurements of the cold molecular gas phases located specifically within low-mass quenched satellite galaxies remain largely unconstrained in a rigorous statistical out-of-sample sense, as current macro-calibration methodologies preferentially target global stellar mass scaling relations while leaving the detailed internal multiphase gas depletion mechanisms entirely dependent on emergent, unverified subgrid interpolations. ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED
GAP: There is an ongoing challenge in fully diagnosing the precise role that radio-mode active galactic nucleus feedback plays in rapidly quenching massive galaxies, as direct observational evidence linking instantaneous radio luminosity to long-term star formation suppression metrics remains highly ambiguous and frequently uncorroborated, fundamentally complicating rigorous out-of-sample validations of the subgrid kinetic jet models currently employed by major simulation suites. 
GAP: Rigorous out-of-sample validations targeting the very high-redshift (z>6 UNCERTAINTY_NOT_QUOTED_BY_SOURCE) stellar mass-halo mass relation and extremely early supermassive black hole seeding environments remain severely limited by current observational survey sensitivities, forcing major simulation suites to continuously extrapolate feedback efficiency parameters that were calibrated exclusively in the low-redshift universe into fundamentally different, denser cosmological epochs without robust empirical justification. ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED   

Links ledger

 | https://academic.oup.com/mnras/article/473/3/4077/4494369 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://www.tng-project.org/data/docs/background/ | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/475/1/648/4683271 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/475/1/648/4683271 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/450/2/1937/984366 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/abs/1407.7040 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/450/2/1937/984366 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://researchportal.port.ac.uk/en/publications/the-eagle-simulations-of-galaxy-formation-calibration-of-subgrid-/ | QUARANTINED_PENDING_LOCAL_CHECK
 | https://www.research.ed.ac.uk/en/publications/simba-cosmological-simulations-with-black-hole-growth-and-feedbac/ | QUARANTINED_PENDING_LOCAL_CHECK
 | http://simba.roe.ac.uk/ | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/486/2/2827/5426823 | QUARANTINED_PENDING_LOCAL_CHECK
 | http://simba.roe.ac.uk/ | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/497/1/146/5866845 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/480/1/800/5046474 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://flathub.flatironinstitute.org/fire | QUARANTINED_PENDING_LOCAL_CHECK
 | https://fire.northwestern.edu/2017/03/21/fire-2-simulations-physics-versus-numerics-in-galaxy-formation/ | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/470/1/1121/3828081 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/abs/1607.02151 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/470/1/1121/3828081 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://mtremmel.github.io/research/romulus.html | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/abs/2111.01160 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/html/2605.13843v1 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/512/3/3703/6546174 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/abs/2110.14154 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://flamingo.strw.leidenuniv.nl/ | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/526/4/6103/7291940 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/526/4/6103/7291940 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/545/2/staf2125/8361503 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/html/2601.15851v1 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/abs/1603.02702 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/465/3/2936/2417021 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/465/3/2936/2417021 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.1093%2Fmnras%2Fstx3040 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/relation-between-starformation-rate-and-stellar-mass-of-galaxies-at-z-14/2AAB84B2524F5870838E5BCC736A18DC | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/497/1/146/5866845 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article-abstract/470/1/1121/3828081 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/abs/2410.19905 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/html/2410.17109v1 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://boa.unimib.it/retrieve/2e807906-4dbc-4c89-b032-54b46c2c5022/Chaikin%20et%20al-2026-Monthly%20Notices%20of%20the%20Royal%20Astronomical%20Society-VoR.pdf | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/pdf/2509.04067 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/526/4/6103/7291940 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/478/2/2618/4993329 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/511/4/6126/6520457 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/html/2508.04907v1 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://arxiv.org/html/2509.07960v2 | QUARANTINED_PENDING_LOCAL_CHECK
 | https://academic.oup.com/mnras/article/497/1/146/5866845 | QUARANTINED_PENDING_LOCAL_CHECK   

GEMINI_WEB_JOINT_C1R_OUTPUT_DONE_20260712T045317Z
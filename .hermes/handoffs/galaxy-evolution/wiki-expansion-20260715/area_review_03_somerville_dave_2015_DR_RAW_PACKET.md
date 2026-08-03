# Review Base 03 raw Deep Research packet — Somerville & Davé 2015

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_03_somerville_dave_2015_DR_PROMPT.md`
Prompt SHA-256: `02e78264c7806264a8f2380ce1ab89debf5dd041ddd7564bff96a3f1d40d4288`
Conversation ID: `656e527a9bcdd1a6`
Submit UTC: `2026-07-15T13:41:21.319467Z`
Research Start UTC: `2026-07-15T13:42:15.739017Z`
Result captured UTC: `2026-07-15T14:09:16.702843Z`
Raw result SHA-256: `87961a709073255e52eb809f3abc21e3fa0256e8b34b96796ace06dff016e864`

## Deep Research review-base result

Advisory Source Base: Physical Models of Galaxy Formation in a Cosmological Framework
1. Review identity and scope map

Verified review identity to confirm:
Somerville, Rachel S. & Davé, Romeel (2015), Annual Review of Astronomy and Astrophysics, volume 53, "Physical Models of Galaxy Formation in a Cosmological Framework."
DOI: 10.1146/annurev-astro-082812-140951; arXiv 1412.2712; ADS bibcode 2015ARA&A..53...51S.

Scope Map and Evidence Boundaries

This advisory source base extracts the foundational 2015 consensus on cosmological galaxy formation modeling, specifically capturing the state of the art prior to the widespread deployment of machine-learning emulation and extremely high-resolution, multi-scale interstellar medium (ISM) zoom simulations. The review maps the successes, tensions, and structural architectures of the two dominant theoretical paradigms: semi-analytic models (SAMs) and numerical hydrodynamic simulations (including Smoothed Particle Hydrodynamics, Adaptive Mesh Refinement, and moving-mesh codes).

A conceptual architecture comparison between SAMs and Cosmological Hydrodynamic Simulations—as detailed in the review—reveals both a divergence and convergence in modeling philosophy. Both methodologies stem from an identical cosmological backbone: dark matter halo assembly driven by ΛCDM initial density fluctuations. However, they employ fundamentally different baryonic tracking execution engines. SAMs rely on computationally lightweight, parameterized differential equations applied retroactively to dark matter halo merger trees extracted from N-body simulations. In contrast, hydrodynamic codes dynamically compute gas physics, thermodynamics, and fluid fluxes on a spatial grid or via Lagrangian particle ensembles concurrently with the evolution of the gravitational potential. Despite these divergent computational pathways, both paradigms converge conceptually at the physical limits of the simulations. Neither can explicitly resolve the parsec-scale physics of individual star-forming clouds or black hole accretion disks within a cosmological volume. Consequently, both must inject analytical "subgrid" recipes to approximate these phenomena, and both are ultimately tuned and evaluated against the exact same observational calibration benchmarks, such as local stellar mass functions, metallicities, and cosmic star formation histories.

What this source base authorizes:

Methodological Frameworks: The evidence establishes the computational limits, numerical dissipation issues, and algorithmic constraints of both SAMs and hydrodynamical solvers up to 2015. It highlights why numerical convergence does not inherently equal physical correctness, supporting claims regarding subgrid degeneracy.

Hierarchical Assembly and Baryon Cycling: The text acts as a primary authority on the macroscopic physics of gas accretion (cold streams versus hot halos), radiative cooling, and the tidal acquisition of angular momentum. It supports detailed analysis of the galactic baryon cycle, including mass-loading factors, wind recycling timescales, and circumgalactic medium (CGM) enrichment.

Scaling Relations and Evolution: The review provides validated boundaries for comparing models against the star-forming main sequence, galaxy stellar mass functions (GSMFs), mass-metallicity relations, and structural size evolution from z∼3 to z=0.

Quenching and Feedback Necessity: The evidence supports the empirical necessity of mass-dependent feedback. Supernova-driven winds are required to suppress star formation in shallow potential wells, while active galactic nucleus (AGN) feedback or virial shock heating is required to quench massive galaxies and truncate the luminosity function.

What this source base strictly prohibits:

AGN Microphysics: Black-hole feedback may only be described as a bounded, macroscopic ingredient utilized to regulate galaxy-scale star formation. This source base does not authorize claims regarding the internal mechanics of accretion disks, relativistic jet thermodynamics, specific AGN demographics, or black hole spin evolution.

Post-2015 Observational Tensions: Claims relying on subsequent JWST discoveries (e.g., extreme early-universe galaxy masses) or advanced machine-learning parameter inferences are quarantined from this core physics synthesis.

2. Established findings

[REV03-E01]

role: established

epistemic_type: semi_analytic_model

atomic finding: The faint-end slope of the local galaxy luminosity and stellar mass function is significantly shallower than the theoretical mass function of dark matter halos. This discrepancy necessitates the inclusion of highly efficient, ejective stellar feedback to suppress star formation inside shallow gravitational potential wells, preventing the overproduction of dwarf galaxies.

scope/boundary: Applies to halos with masses M
h
	​

≲10
11
M
⊙
	​

 and stellar masses M
∗
	​

≲10
9
M
⊙
	​

 within standard ΛCDM cosmologies.

review basis: Section 4.1 / Stellar Mass Assembly Over Cosmic Time

confidence note: Universally confirmed across all independent SAMs and hydrodynamical models; failing to include this feedback results in a catastrophic overprediction of low-mass systems.

source keys: [REV03-R00], [REV03-P002], [REV03-P004]

[REV03-E02]

role: established

epistemic_type: hydrodynamic_simulation

atomic finding: Cosmological gas accretion is fundamentally bimodal. In halos below a critical mass threshold, gas accretes primarily via "cold mode" filamentary streams that penetrate the halo without shock heating to the virial temperature. In massive halos, infalling gas encounters a stable virial shock, creating a "hot mode" hydrostatic halo from which gas must radiatively cool to fuel star formation.

scope/boundary: The transition threshold occurs at a halo mass of roughly M
h
	​

∼10
11.5
−10
12
M
⊙
	​

, though the exact boundary exhibits redshift and metallicity dependencies.

review basis: Section 1.3 / Overview of Physical Processes

confidence note: Theoretically robust and mathematically derived from cooling time versus free-fall time arguments, consistently reproduced in grid and particle-based hydro codes.

source keys: [REV03-R00], [REV03-P026], [REV03-P005]

[REV03-E03]

role: established

epistemic_type: observation

atomic finding: The surface density of star formation in galactic disks correlates tightly with the surface density of molecular hydrogen (H
2
	​

) rather than the total neutral gas density. The star formation efficiency per free-fall time in molecular gas is nearly universal.

scope/boundary: Averaged over sub-kiloparsec scales (∼500−1000 pc) in local and intermediate-redshift disk galaxies.

review basis: Section 3.1 / Star Formation and the ISM

confidence note: Empirically validated by extensive millimeter (CO) and radio (HI) mapping surveys of nearby galaxies.

source keys: [REV03-R00], [REV03-P006], [REV03-P007]

[REV03-E04]

role: established

epistemic_type: semi_analytic_model

atomic finding: The sharp exponential cut-off at the bright end of the galaxy luminosity function cannot be reproduced by prolonged cooling times alone. Models require a preventive feedback mechanism—phenomenologically attributed to AGN heating or "radio mode" black-hole feedback—to offset cooling flows and permanently quench star formation in massive halos.

scope/boundary: Bounded to massive systems residing in halos M
h
	​

≳10
12
M
⊙
	​

.

review basis: Section 4.1 / Stellar Mass Assembly Over Cosmic Time

confidence note: A highly confident phenomenological requirement for models to match observations, independent of the exact physical coupling mechanism of the jet/wind.

source keys: [REV03-R00], [REV03-P015], [REV03-P046]

[REV03-E05]

role: established

epistemic_type: empirical_inference

atomic finding: The vast majority of actively star-forming galaxies reside on a tight, nearly linear scaling relation between their total stellar mass and their star formation rate, widely known as the Star-Forming Main Sequence (SFMS). This sequence indicates that galaxy growth is regulated by a steady quasi-equilibrium between gas accretion, star formation, and outflow, rather than stochastic merger-driven starbursts.

scope/boundary: Applies to non-quiescent, non-starburst populations from the local universe out to z∼2.5, with a relatively constant scatter of ∼0.3 dex.

review basis: Section 1.1.2 / Global Properties: Scaling Relations

confidence note: Strongly supported by multi-wavelength photometric and spectroscopic surveys across multiple cosmic epochs.

source keys: [REV03-R00], [REV03-P047], [REV03-P053]

[REV03-E06]

role: established

epistemic_type: analytic_theory

atomic finding: The angular momentum of galactic disks originates from cosmological tidal torques exerted by large-scale structure during halo collapse. As gas radiatively cools and dissipates energy, it conserves its specific angular momentum and settles into a rotationally supported disk.

scope/boundary: Represents the idealized baseline formation scenario for spiral galaxies; the final structural morphology is subject to modification by subsequent mergers and secular disk instabilities.

review basis: Section 4.2.1 / Formation of Galactic Disks

confidence note: The foundational theoretical premise linking dark matter halo spin parameters to baryonic disk scale lengths.

source keys: [REV03-R00], [REV03-P003], [REV03-P048]

[REV03-E07]

role: established

epistemic_type: empirical_inference

atomic finding: The global galaxy population exhibits a robust structural and photometric bimodality, separating distinctly into a "blue cloud" of actively star-forming, disk-dominated galaxies and a "red sequence" of quiescent, spheroid-dominated galaxies composed of older stellar populations.

scope/boundary: Extensively mapped in the local universe and confirmed to persist out to at least z∼2.

review basis: Section 1.1 / Observational Targets

confidence note: Highly confident macroeconomic property of the universe that models must reproduce via specific quenching channels.

source keys: [REV03-R00], [REV03-P014], [REV03-P033]

[REV03-E08]

role: established

epistemic_type: observation

atomic finding: Star-forming galaxies exhibit a mass-metallicity relation where lower-mass galaxies have systematically lower gas-phase oxygen abundances. This scaling implies that shallow potential wells are less capable of retaining metals synthesized by stars, losing a significant fraction of their enriched interstellar medium to supernova-driven galactic winds.

scope/boundary: Calibrated extensively at z∼0 using optical emission line diagnostics.

review basis: Section 1.1.2 / Global Properties: Scaling Relations

confidence note: The relative scaling is robust, though absolute metallicities vary depending on the specific photoionization models used for calibration.

source keys: [REV03-R00], [REV03-P013], [REV03-P018]

[REV03-E09]

role: established

epistemic_type: hydrodynamic_simulation

atomic finding: Traditional Smoothed Particle Hydrodynamics (SPH) and Eulerian adaptive mesh refinement (AMR) codes display fundamental discrepancies in handling multiphase fluid instabilities. SPH codes suffer from artificial surface tension that suppresses Kelvin-Helmholtz instabilities and prevents efficient phase mixing, while standard Eulerian codes suffer from advection errors lacking Galilean invariance.

scope/boundary: Applies to the algorithmic limits of hydrodynamic solvers evaluated in controlled numerical tests prior to the widespread adoption of moving-mesh or meshless finite-mass techniques.

review basis: Section 2.2 / Hydrodynamics: Numerical Techniques

confidence note: A mathematically and computationally proven limitation that directly impacted simulated galaxy morphologies and cold-flow survival rates.

source keys: [REV03-R00], [REV03-P024], [REV03-P020]

[REV03-E10]

role: established

epistemic_type: empirical_inference

atomic finding: The stellar-to-halo mass relation (SHMR) demonstrates that the integrated efficiency of turning cosmological baryons into stars is maximized in halos of roughly M
h
	​

∼10
12
M
⊙
	​

. In both lower and higher mass halos, the integrated star formation efficiency drops precipitously due to stellar and AGN feedback, respectively.

scope/boundary: Derived primarily via subhalo abundance matching (SHAM) mapping observed stellar mass functions onto dark-matter-only N-body simulations.

review basis: Section 4.1 / Stellar Mass Assembly

confidence note: Strongly supported by statistical kinematic mapping, with the general functional shape agreed upon by independent research groups.

source keys: [REV03-R00], [REV03-P009], [REV03-P010]

[REV03-E11]

role: established

epistemic_type: observation

atomic finding: Massive, quiescent galaxies observed at high redshift (z>1) possess half-light radii that are significantly more compact—often by a factor of 3 to 5—than local quiescent galaxies of equivalent stellar mass.

scope/boundary: Bounded to the quiescent population measured via rest-frame optical photometry; implies that massive spheroids underwent significant late-time structural evolution without commensurate star formation.

review basis: Section 4.2 / Internal Structure and Kinematics

confidence note: Observationally robust finding that drove theories of inside-out growth and late-time dry minor merging.

source keys: [REV03-R00], [REV03-P022], [REV03-P054]

[REV03-E12]

role: established

epistemic_type: review_synthesis

atomic finding: Because the spatial dynamic range required to simulate cosmological volumes (megaparsecs) vastly exceeds the scale of molecular cloud collapse and black hole accretion (sub-parsec), all state-of-the-art cosmological models inherently rely on phenomenological subgrid implementations to capture star formation and feedback.

scope/boundary: Applies universally to both SAMs and hydrodynamical simulations within the 2015 computational landscape.

review basis: Section 3 / Sub-grid Physics

confidence note: An absolute computational necessity defining the epistemic limits of galaxy formation modeling in this era.

source keys: [REV03-R00]

3. Open debates and tensions

[REV03-D01]

role: debate

debate_topic: Subgrid degeneracy and physical identification.

competing positions or implementations: Multiple independent SAMs and hydrodynamic models successfully reproduce the z=0 stellar mass function, but they achieve this using mutually exclusive subgrid feedback parameterizations, energy loadings, and mass-ejection velocities.

why unresolved as of the review's 2015 boundary: Matching a macroscopic calibration benchmark like the luminosity function is mathematically underdetermined; it does not uniquely break the degeneracy to identify the true underlying physical mechanism governing the interstellar medium.

model/measurement/resolution boundary: Exists across all models operating at resolutions where multiphase star formation is unresolved (≳100 pc).

source keys: [REV03-R00], [REV03-P052]

[REV03-D02]

role: debate

debate_topic: Cold versus hot accretion survival.

competing positions or implementations: While bimodal accretion is generally accepted, the exact survival rate of cold filamentary streams penetrating the hot halo to directly fuel disk star formation remains fiercely disputed. SPH codes tend to predict robust cold streams that deliver gas directly to the central disk, whereas Eulerian and moving-mesh codes show these streams being shredded by Kelvin-Helmholtz instabilities and mixing with the hot halo.

why unresolved as of the review's 2015 boundary: The discrepancy is highly sensitive to the underlying numerical hydrodynamics scheme, the inclusion of wind-driven turbulence, and artificial viscosity.

model/measurement/resolution boundary: Most pronounced in 10
11
−10
12
M
⊙
	​

 halos at z∼2−3.

source keys: [REV03-R00], [REV03-P005], [REV03-P026], [REV03-P020]

[REV03-D03]

role: debate

debate_topic: Feedback implementation and wind recycling timescales.

competing positions or implementations: Models inject stellar feedback via kinetic kicks (often with temporary hydrodynamic decoupling), delayed cooling thermal energy, or radiation pressure. Consequently, the timescale and efficiency by which ejected gas falls back onto the galaxy (fountain flows vs. permanent escape) vary drastically between codes.

why unresolved as of the review's 2015 boundary: Direct observations of circumgalactic medium (CGM) kinematics and metal content were insufficient to tightly constrain the empirical mass-loading factors and exact recycling rates required to discriminate between subgrid recipes.

model/measurement/resolution boundary: Heavily dependent on how the CGM boundary is defined and the numerical decoupling choices utilized to prevent premature thermalization.

source keys: [REV03-R00], [REV03-P049], [REV03-P018]

[REV03-D04]

role: debate

debate_topic: Low- versus high-mass quenching mechanisms and the green valley.

competing positions or implementations: Low-mass quenching is generally attributed to supernova winds, while high-mass quenching is attributed to AGN feedback or stable virial shock heating. However, the exact boundary where these processes overlap, the role of environmental processing (satellite "strangulation"), and the primary driver moving galaxies through the intermediate "green valley" remain highly contested.

why unresolved as of the review's 2015 boundary: It is observationally difficult to disentangle internal secular quenching (mass quenching) from external environmental stripping within group and cluster environments.

model/measurement/resolution boundary: Transitions primarily around stellar masses of M
∗
	​

∼10
10.5
M
⊙
	​

.

source keys: [REV03-R00], [REV03-P015], [REV03-P046]

[REV03-D05]

role: debate

debate_topic: Angular-momentum retention and the overcooling problem.

competing positions or implementations: Early simulations suffered from catastrophic angular momentum loss as gas cooled too efficiently during mergers, resulting in overly compact, massive bulges. Recent models resolve this via early, violent stellar feedback that preferentially ejects low-angular-momentum gas from forming disks. However, intense debate exists over whether the required feedback energetics are unrealistically high compared to observations.

why unresolved as of the review's 2015 boundary: Modelers struggled to simultaneously produce large, rotationally supported extended disks while matching realistic, non-bursty star formation histories without destroying the disk prematurely.

model/measurement/resolution boundary: Evaluated primarily in hydrodynamic zoom-in simulations of Milky Way-mass halos.

source keys: [REV03-R00], [REV03-P050], [REV03-P020]

[REV03-D06]

role: debate

debate_topic: Mergers versus internal secular processes in high-z structural evolution.

competing positions or implementations: The formation of massive, highly turbulent, clumpy disks at z∼2 and their subsequent evolution into bulge-dominated systems is driven either by violent, in-situ disk instabilities fueled by smooth cold accretion flows, or alternatively, by frequent ex-situ gas-rich major and minor mergers.

why unresolved as of the review's 2015 boundary: Observational spatial resolution at z∼2 using integral field units (IFUs) struggled to definitively distinguish between in-situ instability clumps and the remnants of ex-situ minor mergers.

model/measurement/resolution boundary: Tensions between cosmological zoom-in hydrodynamical simulations and high-redshift IFU kinematics.

source keys: [REV03-R00], [REV03-P021], [REV03-P016]

[REV03-D07]

role: debate

debate_topic: Reproducing stellar-mass functions without overcalibration (the downsizing tension).

competing positions or implementations: Many models highly tuned to match the z=0 stellar mass function subsequently fail to reproduce the high-redshift universe, typically overpredicting the abundance of low-mass galaxies at z∼1−3 and underpredicting the early formation of massive galaxies (the "downsizing" problem).

why unresolved as of the review's 2015 boundary: Assuming constant subgrid feedback parameters across cosmic time appeared flawed, but modifying accretion timescales or adopting explicitly redshift-dependent feedback efficiencies was viewed by many theorists as mathematically ad-hoc rather than physically motivated.

model/measurement/resolution boundary: Evaluated by tracking z∼0 models against z∼2 to z∼4 mass function constraints.

source keys: [REV03-R00], [REV03-P051], [REV03-P010]

[REV03-D08]

role: debate

debate_topic: SAM versus hydrodynamic convergence on the baryon cycle.

competing positions or implementations: While Semi-Analytic Models and hydrodynamic simulations show remarkable qualitative agreement on the stellar properties of galaxies (like the SMF), they predict vastly divergent metal and gas distributions in the intergalactic and circumgalactic medium for identically sized dark matter halos.

why unresolved as of the review's 2015 boundary: SAMs inherently lack explicit spatial tracking of outflowing gas, relying on phenomenological reincorporation timescales. Conversely, hydro codes explicitly track the gas but are hypersensitive to the numerical hydro solver and subgrid wind launch velocities.

model/measurement/resolution boundary: Comparisons strictly within the CGM/IGM gas phase regimes utilizing absorption line statistics.

source keys: [REV03-R00], [REV03-P017], [REV03-P052]

4. Key measurements, model benchmarks, and calibrations

[REV03-N01]

role: calibration

metric/value/range or model relation: The local (z∼0) galaxy stellar mass function (GSMF) and luminosity function (LF).

sample/simulation, mass/redshift range, resolution/volume, method, and cosmology where relevant: Derived from massive local wide-field surveys (e.g., SDSS, 2dFGRS), covering a stellar mass range from ∼10
8
 to 10
12
M
⊙
	​

.

whether calibrated or predicted: Calibrated; this serves as the primary foundational tuning target for almost all modern galaxy evolution models.

systematic caveat: Stellar mass derivations are highly sensitive to the assumed Initial Mass Function (IMF) and the specific dust attenuation models applied to the photometry.

primary source keys: [REV03-R00], [REV03-P042], [REV03-P046]

[REV03-N02]

role: benchmark

metric/value/range or model relation: The slope and normalization evolution of the Star-Forming Main Sequence (SFMS).

sample/simulation, mass/redshift range, resolution/volume, method, and cosmology where relevant: Measured by deep multi-wavelength imaging surveys (e.g., AEGIS, COSMOS, CANDELS) covering lookback times from z∼0 to z∼3.

whether calibrated or predicted: Predicted; models attempt to naturally reproduce the observed tightening of the sequence and its upward normalization shift at higher redshifts.

systematic caveat: Significant observational discrepancies arise depending on how the Star Formation Rate is extracted (e.g., rest-frame UV versus IR) and the specific selection criteria used to isolate "star-forming" systems from the intermediate "green valley."

primary source keys: [REV03-R00], [REV03-P047], [REV03-P053]

[REV03-N03]

role: calibration

metric/value/range or model relation: The Stellar-to-Halo Mass Relation (SHMR) efficiency peak occurring at M
h
	​

∼10
12
M
⊙
	​

.

sample/simulation, mass/redshift range, resolution/volume, method, and cosmology where relevant: Derived analytically via Subhalo Abundance Matching (SHAM) by mapping empirical GSMFs onto the halo mass functions of large dark-matter-only cosmological simulations.

whether calibrated or predicted: Calibrated; this empirical mapping is frequently used to set the baseline efficiencies of subgrid feedback in SAMs and hydro codes.

systematic caveat: Relies purely on statistical rank-ordering, assuming a monotonic correlation between stellar and halo mass with bounded, constrained scatter.

primary source keys: [REV03-R00], [REV03-P009], [REV03-P010]

[REV03-N04]

role: benchmark

metric/value/range or model relation: The gas-phase Mass-Metallicity Relation (MZR).

sample/simulation, mass/redshift range, resolution/volume, method, and cosmology where relevant: Extensively mapped in the Local Universe (z∼0) utilizing SDSS spectroscopic measurements of oxygen abundance.

whether calibrated or predicted: Predicted; utilized as an independent, secondary check on the mass-loading factors of parameterized galactic winds.

systematic caveat: Characterized by severe absolute calibration uncertainties; differing emission line diagnostics (e.g., empirical vs. theoretical photoionization models) can shift the absolute metallicity scale by over 0.5 dex.

primary source keys: [REV03-R00], [REV03-P013], [REV03-P018]

[REV03-N05]

role: calibration

metric/value/range or model relation: The Kennicutt-Schmidt (KS) relation, which scales Star Formation Rate surface density to gas surface density (Σ
SFR
	​

∝Σ
gas
N
	​

, with N≈1.4 for total gas, or N≈1.0 for molecular gas).

sample/simulation, mass/redshift range, resolution/volume, method, and cosmology where relevant: Measured in local spiral and starburst disk galaxies mapped in HI and CO at sub-kpc resolution.

whether calibrated or predicted: Calibrated; this macroscopic scaling law is directly inserted as the governing subgrid recipe for converting cold gas into stars in simulations.

systematic caveat: The relation is observationally defined as a temporal and spatial average over kiloparsec scales; applying it to parsec-scale simulation grid cells is physically questionable and masks true localized efficiencies.

primary source keys: [REV03-R00], [REV03-P008], [REV03-P006]

[REV03-N06]

role: benchmark

metric/value/range or model relation: The galaxy size-mass relation and its dramatic redshift evolution.

sample/simulation, mass/redshift range, resolution/volume, method, and cosmology where relevant: Rest-frame optical half-light radii measured via high-resolution HST imaging from z∼0 to z∼3.

whether calibrated or predicted: Predicted; models are challenged to reproduce the extreme compactness of high-z spheroids and their subsequent inside-out growth.

systematic caveat: The half-light radius is highly susceptible to surface brightness dimming, dust gradients, and bright central starbursts, meaning it does not perfectly track the true underlying stellar half-mass radius.

primary source keys: [REV03-R00], [REV03-P022], [REV03-P054]

[REV03-N07]

role: benchmark

metric/value/range or model relation: The quiescent fraction of galaxies as a function of stellar mass and local environment.

sample/simulation, mass/redshift range, resolution/volume, method, and cosmology where relevant: Mapped using bimodal color distributions and specific SFR indicators from massive surveys out to z∼2.

whether calibrated or predicted: Predicted; used to validate the efficacy of AGN quenching and environmental stripping subroutines.

systematic caveat: The absolute fraction varies significantly depending on the definition of "quiescent" (e.g., UVJ color-color diagram cuts versus strict specific SFR thresholds).

primary source keys: [REV03-R00], [REV03-P014], [REV03-P055]

[REV03-N08]

role: benchmark

metric/value/range or model relation: The Cosmic Star Formation Rate Density history (the Madau plot), peaking at roughly z∼2.

sample/simulation, mass/redshift range, resolution/volume, method, and cosmology where relevant: A volume-averaged metric integrating all star formation from z∼8 to z∼0.

whether calibrated or predicted: Predicted, though it is often an inevitable mathematical consequence if the model's stellar mass function and SFMS are accurately tuned.

systematic caveat: Relies heavily on rest-frame UV light at high redshift (z>3), which requires substantial and highly uncertain corrections for dust obscuration.

primary source keys: [REV03-R00], [REV03-P044]

5. What remained unknown in 2015

[REV03-U01]

role: future

gap: The precise physical mechanisms, energetics, and coupling efficiencies connecting stellar feedback to the multi-phase interstellar medium.

why it mattered: The mechanics of stellar feedback dictate the mass-loading factor of galactic winds, which is the primary, load-bearing mathematical dial controlling the low-mass end of the stellar mass function and preventing overcooling.

observation/model/numerical test needed: High-resolution (sub-parsec) ISM zoom simulations integrating radiation pressure, cosmic rays, and discrete supernovae to replace parameterized, ad-hoc kinetic and thermal kicks.

review and primary source keys: [REV03-R00], [REV03-P018], [REV03-P056]

[REV03-U02]

role: future

gap: The detailed thermal, kinetic, spatial, and chemical phase structure of the Circumgalactic Medium (CGM).

why it mattered: The CGM acts as the primary reservoir for both incoming cosmological accretion and recycled, metal-rich wind material. It is the ultimate arbiter of the galaxy baryon cycle, determining how much gas actually reaches the disk.

observation/model/numerical test needed: Deep, spatially resolved UV/X-ray absorption and emission line kinematics directly observing the physical state of inflows and outflows beyond the galactic disk.

review and primary source keys: [REV03-R00], [REV03-P057]

[REV03-U03]

role: future

gap: The ability to predict molecular hydrogen (H
2
	​

) formation dynamically and self-consistently within large cosmological volumes.

why it mattered: Because star formation empirically scales with H
2
	​

 rather than total neutral gas, accurately predicting the atomic-to-molecular transition—which varies wildly across different metallicities and localized UV background fields—is necessary to produce realistic high-z and dwarf galaxy star formation rates.

observation/model/numerical test needed: The implementation of non-equilibrium chemical networks and real-time radiative transfer coupled dynamically within cosmological hydro-codes, moving beyond analytic approximations.

review and primary source keys: [REV03-R00], [REV03-P019], [REV03-P058]

[REV03-U04]

role: future

gap: The exact physical origin of "downsizing" without violating the principles of hierarchical dark matter assembly.

why it mattered: Observations dictate that massive galaxies assemble their stars rapidly at early times and quench, while theoretical models inherently grow massive halos late and frequently over-predict their late-time star formation, or conversely over-predict early star formation in dwarf halos.

observation/model/numerical test needed: Refined temporal tracking of star formation histories to separate internal mass quenching (AGN) from external environmental quenching (satellite starvation) in intermediate-to-high mass halos.

review and primary source keys: [REV03-R00], [REV03-P051]

[REV03-U05]

role: future

gap: The explicit physical coupling of supermassive black hole (AGN) feedback to galaxy-scale gas.

why it mattered: While almost all models utilize AGN feedback to quench high-mass galaxies and truncate the luminosity function, they inject this energy via highly artificial, isotropic subgrid thermal dumps that do not reflect the true physics of collimated radio jets or intense accretion disk winds.

observation/model/numerical test needed: Multi-scale hydrodynamic simulations capable of bridging the parsec-scale accretion disk to the kiloparsec-scale galactic halo to accurately model momentum transfer.

review and primary source keys: [REV03-R00], [REV03-P015]

[REV03-U06]

role: future

gap: Formulating first-principles star formation recipes that operate independently of macroscopic empirical density thresholds.

why it mattered: Applying kiloparsec-scale empirical Kennicutt-Schmidt laws to parsec-scale simulation grid cells is physically inconsistent. It forces the simulation to reproduce the input rather than allowing star formation to emerge naturally from gas dynamics, thereby masking the actual physics of molecular cloud collapse.

observation/model/numerical test needed: Resolving the local Jeans mass directly and utilizing sink-particle or turbulent-collapse criteria tightly coupled to gas kinematics, rather than imposing external scaling laws.

review and primary source keys: [REV03-R00], [REV03-P008], [REV03-P021]

6. Primary-citation harvest

[REV03-P001] White & Rees (1978, MNRAS) | title=Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering | DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | role=analytic_theory | review_locator=Section 1.3 | Foundational theory that gas cools within dark matter potential wells.
[REV03-P002] White & Frenk (1991, ApJ) | title=Galaxy formation through hierarchical clustering | DOI:10.1086/170485; arXiv:none; ADS:1991ApJ...379...52W | role=semi_analytic_model | review_locator=Section 1.3 | Established that cooling efficiency scales inversely with density, predicting the cooling catastrophe without feedback.
[REV03-P003] Fall & Efstathiou (1980, MNRAS) | title=Formation and rotation of disc galaxies with haloes | DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | role=analytic_theory | review_locator=Section 4.2.1 | Gas angular momentum acquisition through tidal torques shapes rotationally supported disks.
[REV03-P004] Dekel & Silk (1986, ApJ) | title=The origin of dwarf galaxies, cold dark matter, and biased galaxy formation | DOI:10.1086/164050; arXiv:none; ADS:1986ApJ...303...39D | role=analytic_theory | review_locator=Section 1.3 | Early identification that supernova-driven winds are required to suppress star formation in low-mass halos.
[REV03-P005] Kereš et al. (2005, MNRAS) | title=How do galaxies get their gas? | DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0508347; ADS:2005MNRAS.363....2K | role=hydrodynamic_simulation | review_locator=Section 1.3 | Identified the bimodal hot/cold gas accretion paradigm in hydrodynamical simulations.
[REV03-P006] Bigiel et al. (2008, AJ) | title=The Star Formation Law in Nearby Galaxies on Sub-Kpc Scales | DOI:10.1088/0004-6256/136/6/2846; arXiv:0810.2541; ADS:2008AJ....136.2846B | role=measurement | review_locator=Section 3.1 | Empirical measurement linking star formation directly to molecular hydrogen rather than total neutral gas.
[REV03-P007] Leroy et al. (2008, AJ) | title=The Star Formation Efficiency in Nearby Galaxies: Measuring Where Gas Forms Stars Effectively | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=measurement | review_locator=Section 3.1 | Empirically characterized the star formation efficiency and environmental dependencies across disk galaxies.
[REV03-P008] Kennicutt (1998, ApJ) | title=The Global Schmidt Law in Star-forming Galaxies | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=measurement | review_locator=Section 3.1 | Defined the baseline empirical calibration for the relationship between gas density and star formation rate.
[REV03-P009] Moster et al. (2013, MNRAS) | title=Galactic star formation and accretion histories from matching galaxies to dark matter haloes | DOI:10.1093/mnras/sts261; arXiv:1205.5807; ADS:2013MNRAS.428.3121M | role=empirical_inference | review_locator=Section 4.1 | Derived multi-epoch abundance matching constraining the stellar-to-halo mass relation.
[REV03-P010] Behroozi et al. (2013, ApJ) | title=The Average Star Formation Histories of Galaxies in Dark Matter Halos from z = 0-8 | DOI:10.1088/0004-637X/770/1/57; arXiv:1207.6105; ADS:2013ApJ...770...57B | role=empirical_inference | review_locator=Section 4.1 | Quantified the robust SHMR and integrated cosmic star formation matching via abundance techniques.
[REV03-P011] Behroozi et al. (2013, ApJ) | title=The structure of cold dark matter halos | DOI:10.1088/0004-637X/763/1/18; arXiv:1110.4370; ADS:2013ApJ...763...18B | role=hydrodynamic_simulation | review_locator=Section 2.1 | Analyzed precise structural boundaries and hierarchical assembly properties of dark matter halos.
[REV03-P012] Gallazzi et al. (2005, MNRAS) | title=The ages and metallicities of galaxies in the local universe | DOI:10.1111/j.1365-2966.2005.09321.x; arXiv:astro-ph/0506539; ADS:2005MNRAS.362...41G | role=measurement | review_locator=Section 1.1.2 | Key observational benchmark for the stellar metallicity distribution in low-redshift galaxies.
[REV03-P013] Tremonti et al. (2004, ApJ) | title=The Origin of the Mass-Metallicity Relation: Insights from 53,000 Star-forming Galaxies in the Sloan Digital Sky Survey | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=measurement | review_locator=Section 1.1.2 | Established the definitive low-redshift gas-phase mass-metallicity relation scaling.
[REV03-P014] Baldry et al. (2004, ApJ) | title=Quantifying the Bimodal Color-Magnitude Distribution of Galaxies | DOI:10.1086/380092; arXiv:astro-ph/0309710; ADS:2004ApJ...600..681B | role=measurement | review_locator=Section 1.1.1 | Measured the robust structural separation between the star-forming blue cloud and quiescent red sequence.
[REV03-P015] Bower et al. (2006, MNRAS) | title=Breaking the hierarchy of galaxy formation | DOI:10.1111/j.1365-2966.2006.10519.x; arXiv:astro-ph/0511338; ADS:2006MNRAS.370..645B | role=semi_analytic_model | review_locator=Section 4.1 | Demonstrated that radio-mode AGN feedback quenches cooling flows to match the bright-end luminosity function.
[REV03-P016] Cox et al. (2006, MNRAS) | title=Feedback in simulations of disc-galaxy major mergers | DOI:10.1111/j.1365-2966.2006.11107.x; arXiv:astro-ph/0503201; ADS:2006MNRAS.373.1013C | role=hydrodynamic_simulation | review_locator=Section 4.2 | Modeled merger-driven starbursts and the necessary dissipation scales for feedback.
[REV03-P017] Arrigoni et al. (2010, MNRAS) | title=Galactic chemical evolution in hierarchical formation models - I. Early-type galaxies in the local Universe | DOI:10.1111/j.1365-2966.2009.15924.x; arXiv:0910.2073; ADS:2010MNRAS.402..173A | role=semi_analytic_model | review_locator=Section 3.1 | Assessed chemical abundance ratio constraints within hierarchical semi-analytic models.
[REV03-P018] Peeples & Shankar (2011, MNRAS) | title=Constraints on star formation driven galaxy winds from the mass-metallicity relation at z = 0 | DOI:10.1111/j.1365-2966.2011.19456.x; arXiv:1007.3498; ADS:2011MNRAS.417.2962P | role=empirical_inference | review_locator=Section 1.1.2 | Constrained metal expulsion efficiency and mass-loading factors from the MZR.
[REV03-P019] Gnedin & Kravtsov (2011, ApJ) | title=Modeling Molecular Hydrogen and Star Formation in Cosmological Simulations | DOI:10.1088/0004-637X/728/2/88; arXiv:1008.0858; ADS:2011ApJ...728...88G | role=hydrodynamic_simulation | review_locator=Section 3.1 | Formulated subgrid shielding and radiation networks for H2-regulated star formation.
[REV03-P020] Springel (2010, MNRAS) | title=E pur si muove: Galilean-invariant cosmological hydrodynamical simulations on a moving mesh | DOI:10.1111/j.1365-2966.2009.15715.x; arXiv:0901.4107; ADS:2010MNRAS.401..791S | role=hydrodynamic_simulation | review_locator=Section 2.2 | Introduced the moving-mesh architecture resolving critical limitations in standard SPH contact discontinuities.
[REV03-P021] Ceverino et al. (2010, MNRAS) | title=High-redshift clumpy discs and bulges in cosmological simulations | DOI:10.1111/j.1365-2966.2010.16433.x; arXiv:0907.3271; ADS:2010MNRAS.404.2151C | role=hydrodynamic_simulation | review_locator=Section 4.2 | Simulated violent disk instabilities producing giant star-forming clumps at high redshift.
[REV03-P022] Barro et al. (2013, ApJ) | title=CANDELS: The Progenitors of Compact Quiescent Galaxies at z ~ 2 | DOI:10.1088/0004-637X/765/2/104; arXiv:1206.5804; ADS:2013ApJ...765..104B | role=measurement | review_locator=Section 4.2 | Observed the morphological transition and extreme compactness of high-z quiescent galaxies.
[REV03-P023] Bell et al. (2012, ApJ) | title=The Different Morphologies of Star-forming and Quiescent Galaxies since z ~ 2 from CANDELS | DOI:10.1088/0004-637X/753/2/167; arXiv:1110.3786; ADS:2012ApJ...753..167B | role=measurement | review_locator=Section 4.2 | Benchmarked the structural bifurcation between star-forming disks and quenched spheroids.
[REV03-P024] Agertz et al. (2007, MNRAS) | title=Fundamental differences between SPH and grid methods | DOI:10.1111/j.1365-2966.2007.12183.x; arXiv:astro-ph/0610051; ADS:2007MNRAS.380..963A | role=hydrodynamic_simulation | review_locator=Section 2.2 | Demonstrated catastrophic artificial surface tension in SPH resolving multi-phase fluid instabilities.
[REV03-P025] Baugh (2006, RPPh) | title=A primer on hierarchical galaxy formation: the semi-analytical approach | DOI:10.1088/0034-4885/69/12/R02; arXiv:astro-ph/0610031; ADS:2006RPPh...69.3101B | role=semi_analytic_model | review_locator=Section 1.4 | Outlined the base mathematical scaffolding linking dark matter assembly to SAM prescriptions.
[REV03-P026] Birnboim & Dekel (2003, MNRAS) | title=Virial shocks in galactic haloes? | DOI:10.1046/j.1365-8711.2003.06955.x; arXiv:astro-ph/0302161; ADS:2003MNRAS.345..349B | role=analytic_theory | review_locator=Section 1.3 | Mathematically established the mass threshold for shock heating over smooth cold flows.
[REV03-P027] Boylan-Kolchin et al. (2011, MNRAS) | title=Too big to fail? The puzzling darkness of massive Milky Way subhaloes | DOI:10.1111/j.1745-3933.2011.01074.x; arXiv:1103.0007; ADS:2011MNRAS.415L..40B | role=hydrodynamic_simulation | review_locator=Section 2.1 | Highlighted tensions between N-body dark matter substructure kinematics and observed satellites.
[REV03-P028] Barnes & Hut (1986, Nature) | title=A hierarchical O(N log N) force-calculation algorithm | DOI:10.1038/324446a0; arXiv:none; ADS:1986Natur.324..446B | role=analytic_theory | review_locator=Section 2.1 | Foundational tree-code algorithm establishing scalable N-body gravity solvers.
[REV03-P029] Barnes (1988, ApJ) | title=Encounters of Disk/Halo Galaxies | DOI:10.1086/166593; arXiv:none; ADS:1988ApJ...331..699B | role=hydrodynamic_simulation | review_locator=Section 4.2 | Early demonstration of violent relaxation in mergers destroying disks and creating spheroids.
[REV03-P030] Barnes (1992, ApJ) | title=Transformations of galaxies. I - Mergers of equal-mass stellar disks | DOI:10.1086/171522; arXiv:none; ADS:1992ApJ...393..484B | role=hydrodynamic_simulation | review_locator=Section 4.2 | Demonstrated phase mixing and angular momentum transfer to dark matter during mergers.
[REV03-P031] Baugh et al. (2005, MNRAS) | title=Can the faint submillimetre galaxies be explained in the Λ cold dark matter model? | DOI:10.1111/j.1365-2966.2004.08454.x; arXiv:astro-ph/0406063; ADS:2005MNRAS.356.1191B | role=semi_analytic_model | review_locator=Section 4.1 | Required drastic IMF modifications in SAMs to match high-redshift starbursts.
[REV03-P032] Behroozi et al. (2010, ApJ) | title=A Comprehensive Guide to Toy Cosmologies | DOI:10.1088/0004-637X/717/1/379; arXiv:1001.0015; ADS:2010ApJ...717..379B | role=empirical_inference | review_locator=Section 4.1 | Refined abundance matching methodology handling systematic observational scatter.
[REV03-P033] Bell et al. (2004, ApJ) | title=Nearly 5000 Distant Early-Type Galaxies in COMBO-17: A Red Sequence and Its Evolution since z~1 | DOI:10.1086/420778; arXiv:astro-ph/0403001; ADS:2004ApJ...608..752B | role=measurement | review_locator=Section 4.1 | Quantified the persistent mass build-up on the quiescent red sequence over cosmic time.
[REV03-P034] Bender et al. (1992, ApJ) | title=Velocity kinematics in the elliptical galaxies | DOI:10.1086/171940; arXiv:none; ADS:1992ApJ...399..462B | role=measurement | review_locator=Section 4.2 | Measured structural velocity scaling laws in spheroidal remnants.
[REV03-P035] Benson (2010, PhR) | title=Galaxy formation theory | DOI:10.1016/j.physrep.2010.08.001; arXiv:1006.5394; ADS:2010PhR...495...33B | role=review_synthesis | review_locator=Section 1.2 | Broad theoretical framing of the ΛCDM hierarchical components used by models.
[REV03-P036] Benson et al. (2007, MNRAS) | title=The nature of the dwarf galaxy population | DOI:10.1111/j.1365-2966.2007.11933.x; arXiv:astro-ph/0612349; ADS:2007MNRAS.379..841B | role=semi_analytic_model | review_locator=Section 4.1 | Simulated the impact of reionization and supernovae feedback on dwarf demographics.
[REV03-P037] Blanton & Moustakas (2009, ARA&A) | title=Physical Properties and Environments of Nearby Galaxies | DOI:10.1146/annurev-astro-082708-101734; arXiv:0908.3017; ADS:2009ARA&A..47..159B | role=measurement | review_locator=Section 1.1 | Standard reference for the local galaxy distribution functions and structural metrics.
[REV03-P038] Blitz & Rosolowsky (2004, ApJ) | title=The Role of Pressure in GMC Formation II: The H2-Pressure Relation | DOI:10.1086/423719; arXiv:astro-ph/0406451; ADS:2004ApJ...612L..29B | role=empirical_inference | review_locator=Section 3.1 | Derived the empirical mid-plane pressure law used to partition H2 in subgrid SAMs.
[REV03-P039] Blumenthal et al. (1984, Nature) | title=Formation of galaxies and large-scale structure with cold dark matter | DOI:10.1038/311517a0; arXiv:none; ADS:1984Natur.311..517B | role=analytic_theory | review_locator=Section 1.3 | Foundational cosmology paper establishing cold dark matter clustering behavior.
[REV03-P040] Bondi (1952, MNRAS) | title=On spherically symmetrical accretion | DOI:10.1093/mnras/112.2.195; arXiv:none; ADS:1952MNRAS.112..195B | role=analytic_theory | review_locator=Section 3.2 | Provided the mathematical boundary for spherical gas accretion used in subgrid black hole models.
[REV03-P041] Booth & Schaye (2009, MNRAS) | title=Cosmological simulations of the growth of supermassive black holes and feedback from active galactic nuclei: method and tests | DOI:10.1111/j.1365-2966.2009.15043.x; arXiv:0904.2572; ADS:2009MNRAS.398...53B | role=hydrodynamic_simulation | review_locator=Section 3.2 | Established subgrid hydrodynamical parameters linking thermal AGN dumps to BH mass scaling.
[REV03-P042] Schechter (1976, ApJ) | title=An analytic expression for the luminosity function for galaxies. | DOI:10.1086/154079; arXiv:none; ADS:1976ApJ...203..297S | role=measurement | review_locator=Section 1.1.1 | Developed the asymptotic mathematical fit for the galaxy mass/luminosity distribution function.
[REV03-P043] Conroy (2013, ARA&A) | title=Modeling the Panchromatic Spectral Energy Distributions of Galaxies | DOI:10.1146/annurev-astro-082812-141017; arXiv:1301.7095; ADS:2013ARA&A..51..393C | role=analytic_theory | review_locator=Section 1.1 | Benchmark for translating physical simulation stellar parameters into observable SED photometry.
[REV03-P044] Madau & Dickinson (2014, ARA&A) | title=Cosmic Star-Formation History | DOI:10.1146/annurev-astro-081811-025615; arXiv:1403.0007; ADS:2014ARA&A..52..415M | role=measurement | review_locator=Section 1.1.1 | Defined the cosmic star formation rate density envelope (Madau plot) used to calibrate temporal models.
[REV03-P045] Krumholz et al. (2012, ApJ) | title=A Unified Law for Star Formation in Galaxies and the Interstellar Medium | DOI:10.1088/0004-637X/745/1/69; arXiv:1201.0764; ADS:2012ApJ...745...69K | role=analytic_theory | review_locator=Section 3.1 | Theorized the universal star formation efficiency per free-fall time applied in modern subgrid codes.
[REV03-P046] Croton et al. (2006, MNRAS) | title=The many lives of active galactic nuclei: cooling flows, black holes and the luminosities and colours of galaxies | DOI:10.1111/j.1365-2966.2005.09675.x; arXiv:astro-ph/0508046; ADS:2006MNRAS.365...11C | role=semi_analytic_model | review_locator=Section 4.1 | Contemporaneous with Bower 2006, established "radio mode" AGN feedback as the critical quenching parameter.
[REV03-P047] Noeske et al. (2007, ApJ) | title=Star Formation in AEGIS Field Galaxies since z=1.1: The Dominance of Gradually Declining Star Formation, and the Main Sequence of Star-forming Galaxies | DOI:10.1086/517926; arXiv:astro-ph/0701924; ADS:2007ApJ...660L..43N | role=measurement | review_locator=Section 1.1.2 | Coined and defined the "Star Forming Main Sequence" against which models calibrate sustained growth.
[REV03-P048] Mo et al. (1998, MNRAS) | title=The formation of galactic discs | DOI:10.1046/j.1365-8711.1998.01587.x; arXiv:astro-ph/9711159; ADS:1998MNRAS.295..319M | role=analytic_theory | review_locator=Section 4.2.1 | Established the isothermal density profile scaling relations connecting dark halo properties to disk sizes.
[REV03-P049] Dalla Vecchia & Schaye (2008, MNRAS) | title=Simulating galactic outflows with kinetic supernova feedback | DOI:10.1111/j.1365-2966.2008.13840.x; arXiv:0801.0772; ADS:2008MNRAS.387.1431D | role=hydrodynamic_simulation | review_locator=Section 3.3.2 | Outlined the temporary hydrodynamic decoupling mechanism required to prevent instantaneous wind thermalization.
[REV03-P050] Governato et al. (2010, Nature) | title=Bulgeless dwarf galaxies and dark matter cores from supernova-driven outflows | DOI:10.1038/nature08640; arXiv:0911.2237; ADS:2010Natur.463..203G | role=hydrodynamic_simulation | review_locator=Section 4.2 | Showed that powerful winds can reshape dark matter profiles and prevent massive bulge overcooling.
[REV03-P051] Fontanot et al. (2009, MNRAS) | title=The many manifestations of downsizing: hierarchical galaxy formation models confront observations | DOI:10.1111/j.1365-2966.2009.15058.x; arXiv:0901.1130; ADS:2009MNRAS.397.1776F | role=semi_analytic_model | review_locator=Section 4.1 | Exposed the persistent failure of calibrated SAMs to reproduce the "downsizing" of massive galaxies at high redshift.
[REV03-P052] Scannapieco et al. (2012, MNRAS) | title=The Aquila comparison project: the effects of feedback and numerical methods on simulated formation of disk galaxies | DOI:10.1111/j.1365-2966.2012.20993.x; arXiv:1112.0315; ADS:2012MNRAS.423.1726S | role=hydrodynamic_simulation | review_locator=Section 2.2 | Multi-code comparison showing that disparate subgrid recipes cause massive divergence in final galaxy properties.
[REV03-P053] Wuyts et al. (2011, ApJ) | title=Galaxy Structure and Mode of Star Formation in the SFR-Mass Plane from z ~ 2.5 to z ~ 0.1 | DOI:10.1088/0004-637X/742/2/96; arXiv:1107.0317; ADS:2011ApJ...742...96W | role=measurement | review_locator=Section 1.1.2 | Linked structural indices (Sersic) directly to positions on the Star-Forming Main Sequence.
[REV03-P054] van der Wel et al. (2014, ApJ) | title=3D-HST+CANDELS: The Evolution of the Galaxy Size-Mass Distribution since z = 3 | DOI:10.1088/0004-637X/788/1/28; arXiv:1404.2844; ADS:2014ApJ...788...28V | role=measurement | review_locator=Section 4.2 | Comprehensive empirical benchmark for the size evolution of disk and spheroidal galaxies over 10 billion years.
[REV03-P055] Muzzin et al. (2013, ApJ) | title=The Evolution of the Stellar Mass Functions of Star-forming and Quiescent Galaxies to z = 4 from the COSMOS/UltraVISTA Survey | DOI:10.1088/0004-637X/777/1/18; arXiv:1303.4409; ADS:2013ApJ...777...18M | role=measurement | review_locator=Section 1.1.1 | Pushed the bimodal mass function demographic baseline out to z=4.
[REV03-P056] Hopkins et al. (2014, MNRAS) | title=Galaxies on FIRE (Feedback In Realistic Environments): stellar feedback explains cosmologically inefficient star formation | DOI:10.1093/mnras/stu732; arXiv:1311.2073; ADS:2014MNRAS.445..581H | role=hydrodynamic_simulation | review_locator=Section 3.3.2 | High-resolution explicit stellar feedback resolving the multi-phase ISM without cooling shutoffs.
[REV03-P057] Tumlinson et al. (2011, Science) | title=The Large, Oxygen-Rich Halos of Star-Forming Galaxies Are a Major Reservoir of Galactic Metals | DOI:10.1126/science.1209840; arXiv:1111.3975; ADS:2011Sci...334..948T | role=measurement | review_locator=Section 4.1 | Groundbreaking COS-Halos observation proving that massive metal reservoirs reside in the CGM.
[REV03-P058] Krumholz et al. (2009, ApJ) | title=The Atomic-to-Molecular Transition in Galaxies. II. HI and H2 Column Densities | DOI:10.1088/0004-637X/693/1/216; arXiv:0810.0011; ADS:2009ApJ...693..216K | role=analytic_theory | review_locator=Section 3.1 | Provided the analytic framework used by codes to estimate the unresolved H
2
	​

 fraction from local metallicity.

7. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | Lovell et al. 2023 (CAMELS project) | ML flows / Normalizing flows / GNNs | Outside 2015 temporal boundary; applies machine learning to hydro outputs rather than core physical modeling.
UNCITED_NOT_USABLE | de Santi et al. 2025 | J. Cosmol. Astropart. Phys. | Post-2015 boundary; applies Graph Neural Networks to CAMELS simulation catalogs.
UNCITED_NOT_USABLE | Su et al. 2021 | AGN feedback on satellites | Quarantine rule: Extends AGN-centered metrics and operates outside the 2015 temporal boundary.
UNCITED_NOT_USABLE | Lapi et al. 2026 / JCAP | Relic BHs and seed growth | Outside 2015 temporal boundary and strictly violates the AGN-centered quarantine boundary.
UNCITED_NOT_USABLE | Claim: Convergence at one resolution proves physical convergence | General modeler claim | Somerville & Davé 2015 explicitly warn against numerical subgrid degeneracy; tuning a specific spatial resolution does not prove the continuum physics are correct when scaled.
UNCITED_NOT_USABLE | Claim: Matching a tuned stellar-mass function proves the feedback mechanism | General modeler claim | Directly contradicted by the review; multiple distinct feedback mathematical formulations (e.g., kinetic kicks vs. delayed cooling) can successfully hit the exact same z=0 calibration target.
UNCITED_NOT_USABLE | Claim: Subgrid prescriptions are first-principles predictions | General modeler claim | The review defines subgrid recipes as explicitly phenomenological and empirical approximations necessary to bypass unresolved scales.
UNCITED_NOT_USABLE | Claim: All quenching is caused by a single channel | General modeler claim | The review notes that virial heating, AGN feedback, and environmental starvation (ram pressure/stripping) all operate simultaneously.

8. Review and source identity ledger

SourceKey | Authors (year, journal) | DOI:; arXiv:; ADS: | role=... | one-line boundary
[REV03-R00] | Somerville & Davé (2015, ARA&A) | DOI:10.1146/annurev-astro-082812-140951; arXiv:1412.2712; ADS:2015ARA&A..53...51S | role=review_synthesis | Master orientation and bounding synthesis for galaxy formation models.
[REV03-P001] | White & Rees (1978, MNRAS) | DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | role=analytic_theory | Foundational theory that gas cools within dark matter potential wells.
[REV03-P002] | White & Frenk (1991, ApJ) | DOI:10.1086/170485; arXiv:none; ADS:1991ApJ...379...52W | role=semi_analytic_model | Established that cooling efficiency scales inversely with density, predicting the cooling catastrophe without feedback.
[REV03-P003] | Fall & Efstathiou (1980, MNRAS) | DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | role=analytic_theory | Gas angular momentum acquisition through tidal torques shapes rotationally supported disks.
[REV03-P004] | Dekel & Silk (1986, ApJ) | DOI:10.1086/164050; arXiv:none; ADS:1986ApJ...303...39D | role=analytic_theory | Early identification that supernova-driven winds are required to suppress star formation in low-mass halos.
[REV03-P005] | Kereš et al. (2005, MNRAS) | DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0508347; ADS:2005MNRAS.363....2K | role=hydrodynamic_simulation | Identified the bimodal hot/cold gas accretion paradigm in hydrodynamical simulations.
[REV03-P006] | Bigiel et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2846; arXiv:0810.2541; ADS:2008AJ....136.2846B | role=measurement | Empirical measurement linking star formation directly to molecular hydrogen rather than total neutral gas.
[REV03-P007] | Leroy et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=measurement | Empirically characterized the star formation efficiency and environmental dependencies across disk galaxies.
[REV03-P008] | Kennicutt (1998, ApJ) | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=measurement | Defined the baseline empirical calibration for the relationship between gas density and star formation rate.
[REV03-P009] | Moster et al. (2013, MNRAS) | DOI:10.1093/mnras/sts261; arXiv:1205.5807; ADS:2013MNRAS.428.3121M | role=empirical_inference | Derived multi-epoch abundance matching constraining the stellar-to-halo mass relation.
[REV03-P010] | Behroozi et al. (2013, ApJ) | DOI:10.1088/0004-637X/770/1/57; arXiv:1207.6105; ADS:2013ApJ...770...57B | role=empirical_inference | Quantified the robust SHMR and integrated cosmic star formation matching via abundance techniques.
[REV03-P011] | Behroozi et al. (2013, ApJ) | DOI:10.1088/0004-637X/763/1/18; arXiv:1110.4370; ADS:2013ApJ...763...18B | role=hydrodynamic_simulation | Analyzed precise structural boundaries and hierarchical assembly properties of dark matter halos.
[REV03-P012] | Gallazzi et al. (2005, MNRAS) | DOI:10.1111/j.1365-2966.2005.09321.x; arXiv:astro-ph/0506539; ADS:2005MNRAS.362...41G | role=measurement | Key observational benchmark for the stellar metallicity distribution in low-redshift galaxies.
[REV03-P013] | Tremonti et al. (2004, ApJ) | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=measurement | Established the definitive low-redshift gas-phase mass-metallicity relation scaling.
[REV03-P014] | Baldry et al. (2004, ApJ) | DOI:10.1086/380092; arXiv:astro-ph/0309710; ADS:2004ApJ...600..681B | role=measurement | Measured the robust structural separation between the star-forming blue cloud and quiescent red sequence.
[REV03-P015] | Bower et al. (2006, MNRAS) | DOI:10.1111/j.1365-2966.2006.10519.x; arXiv:astro-ph/0511338; ADS:2006MNRAS.370..645B | role=semi_analytic_model | Demonstrated that radio-mode AGN feedback quenches cooling flows to match the bright-end luminosity function.
[REV03-P016] | Cox et al. (2006, MNRAS) | DOI:10.1111/j.1365-2966.2006.11107.x; arXiv:astro-ph/0503201; ADS:2006MNRAS.373.1013C | role=hydrodynamic_simulation | Modeled merger-driven starbursts and the necessary dissipation scales for feedback.
[REV03-P017] | Arrigoni et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2009.15924.x; arXiv:0910.2073; ADS:2010MNRAS.402..173A | role=semi_analytic_model | Assessed chemical abundance ratio constraints within hierarchical semi-analytic models.
[REV03-P018] | Peeples & Shankar (2011, MNRAS) | DOI:10.1111/j.1365-2966.2011.19456.x; arXiv:1007.3498; ADS:2011MNRAS.417.2962P | role=empirical_inference | Constrained metal expulsion efficiency and mass-loading factors from the MZR.
[REV03-P019] | Gnedin & Kravtsov (2011, ApJ) | DOI:10.1088/0004-637X/728/2/88; arXiv:1008.0858; ADS:2011ApJ...728...88G | role=hydrodynamic_simulation | Formulated subgrid shielding and radiation networks for H2-regulated star formation.
[REV03-P020] | Springel (2010, MNRAS) | DOI:10.1111/j.1365-2966.2009.15715.x; arXiv:0901.4107; ADS:2010MNRAS.401..791S | role=hydrodynamic_simulation | Introduced the moving-mesh architecture resolving critical limitations in standard SPH contact discontinuities.
[REV03-P021] | Ceverino et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.16433.x; arXiv:0907.3271; ADS:2010MNRAS.404.2151C | role=hydrodynamic_simulation | Simulated violent disk instabilities producing giant star-forming clumps at high redshift.
[REV03-P022] | Barro et al. (2013, ApJ) | DOI:10.1088/0004-637X/765/2/104; arXiv:1206.5804; ADS:2013ApJ...765..104B | role=measurement | Observed the morphological transition and extreme compactness of high-z quiescent galaxies.
[REV03-P023] | Bell et al. (2012, ApJ) | DOI:10.1088/0004-637X/753/2/167; arXiv:1110.3786; ADS:2012ApJ...753..167B | role=measurement | Benchmarked the structural bifurcation between star-forming disks and quenched spheroids.
[REV03-P024] | Agertz et al. (2007, MNRAS) | DOI:10.1111/j.1365-2966.2007.12183.x; arXiv:astro-ph/0610051; ADS:2007MNRAS.380..963A | role=hydrodynamic_simulation | Demonstrated catastrophic artificial surface tension in SPH resolving multi-phase fluid instabilities.
[REV03-P025] | Baugh (2006, RPPh) | DOI:10.1088/0034-4885/69/12/R02; arXiv:astro-ph/0610031; ADS:2006RPPh...69.3101B | role=semi_analytic_model | Outlined the base mathematical scaffolding linking dark matter assembly to SAM prescriptions.
[REV03-P026] | Birnboim & Dekel (2003, MNRAS) | DOI:10.1046/j.1365-8711.2003.06955.x; arXiv:astro-ph/0302161; ADS:2003MNRAS.345..349B | role=analytic_theory | Mathematically established the mass threshold for shock heating over smooth cold flows.
[REV03-P027] | Boylan-Kolchin et al. (2011, MNRAS) | DOI:10.1111/j.1745-3933.2011.01074.x; arXiv:1103.0007; ADS:2011MNRAS.415L..40B | role=hydrodynamic_simulation | Highlighted tensions between N-body dark matter substructure kinematics and observed satellites.
[REV03-P028] | Barnes & Hut (1986, Nature) | DOI:10.1038/324446a0; arXiv:none; ADS:1986Natur.324..446B | role=analytic_theory | Foundational tree-code algorithm establishing scalable N-body gravity solvers.
[REV03-P029] | Barnes (1988, ApJ) | DOI:10.1086/166593; arXiv:none; ADS:1988ApJ...331..699B | role=hydrodynamic_simulation | Early demonstration of violent relaxation in mergers destroying disks and creating spheroids.
[REV03-P030] | Barnes (1992, ApJ) | DOI:10.1086/171522; arXiv:none; ADS:1992ApJ...393..484B | role=hydrodynamic_simulation | Demonstrated phase mixing and angular momentum transfer to dark matter during mergers.
[REV03-P031] | Baugh et al. (2005, MNRAS) | DOI:10.1111/j.1365-2966.2004.08454.x; arXiv:astro-ph/0406063; ADS:2005MNRAS.356.1191B | role=semi_analytic_model | Required drastic IMF modifications in SAMs to match high-redshift starbursts.
[REV03-P032] | Behroozi et al. (2010, ApJ) | DOI:10.1088/0004-637X/717/1/379; arXiv:1001.0015; ADS:2010ApJ...717..379B | role=empirical_inference | Refined abundance matching methodology handling systematic observational scatter.
[REV03-P033] | Bell et al. (2004, ApJ) | DOI:10.1086/420778; arXiv:astro-ph/0403001; ADS:2004ApJ...608..752B | role=measurement | Quantified the persistent mass build-up on the quiescent red sequence over cosmic time.
[REV03-P034] | Bender et al. (1992, ApJ) | DOI:10.1086/171940; arXiv:none; ADS:1992ApJ...399..462B | role=measurement | Measured structural velocity scaling laws in spheroidal remnants.
[REV03-P035] | Benson (2010, PhR) | DOI:10.1016/j.physrep.2010.08.001; arXiv:1006.5394; ADS:2010PhR...495...33B | role=review_synthesis | Broad theoretical framing of the ΛCDM hierarchical components used by models.
[REV03-P036] | Benson et al. (2007, MNRAS) | DOI:10.1111/j.1365-2966.2007.11933.x; arXiv:astro-ph/0612349; ADS:2007MNRAS.379..841B | role=semi_analytic_model | Simulated the impact of reionization and supernovae feedback on dwarf demographics.
[REV03-P037] | Blanton & Moustakas (2009, ARA&A) | DOI:10.1146/annurev-astro-082708-101734; arXiv:0908.3017; ADS:2009ARA&A..47..159B | role=measurement | Standard reference for the local galaxy distribution functions and structural metrics.
[REV03-P038] | Blitz & Rosolowsky (2004, ApJ) | DOI:10.1086/423719; arXiv:astro-ph/0406451; ADS:2004ApJ...612L..29B | role=empirical_inference | Derived the empirical mid-plane pressure law used to partition H2 in subgrid SAMs.
[REV03-P039] | Blumenthal et al. (1984, Nature) | DOI:10.1038/311517a0; arXiv:none; ADS:1984Natur.311..517B | role=analytic_theory | Foundational cosmology paper establishing cold dark matter clustering behavior.
[REV03-P040] | Bondi (1952, MNRAS) | DOI:10.1093/mnras/112.2.195; arXiv:none; ADS:1952MNRAS.112..195B | role=analytic_theory | Provided the mathematical boundary for spherical gas accretion used in subgrid black hole models.
[REV03-P041] | Booth & Schaye (2009, MNRAS) | DOI:10.1111/j.1365-2966.2009.15043.x; arXiv:0904.2572; ADS:2009MNRAS.398...53B | role=hydrodynamic_simulation | Established subgrid hydrodynamical parameters linking thermal AGN dumps to BH mass scaling.
[REV03-P042] | Schechter (1976, ApJ) | DOI:10.1086/154079; arXiv:none; ADS:1976ApJ...203..297S | role=measurement | Developed the asymptotic mathematical fit for the galaxy mass/luminosity distribution function.
[REV03-P043] | Conroy (2013, ARA&A) | DOI:10.1146/annurev-astro-082812-141017; arXiv:1301.7095; ADS:2013ARA&A..51..393C | role=analytic_theory | Benchmark for translating physical simulation stellar parameters into observable SED photometry.
[REV03-P044] | Madau & Dickinson (2014, ARA&A) | DOI:10.1146/annurev-astro-081811-025615; arXiv:1403.0007; ADS:2014ARA&A..52..415M | role=measurement | Defined the cosmic star formation rate density envelope (Madau plot) used to calibrate temporal models.
[REV03-P045] | Krumholz et al. (2012, ApJ) | DOI:10.1088/0004-637X/745/1/69; arXiv:1201.0764; ADS:2012ApJ...745...69K | role=analytic_theory | Theorized the universal star formation efficiency per free-fall time applied in modern subgrid codes.
[REV03-P046] | Croton et al. (2006, MNRAS) | DOI:10.1111/j.1365-2966.2005.09675.x; arXiv:astro-ph/0508046; ADS:2006MNRAS.365...11C | role=semi_analytic_model | Contemporaneous with Bower 2006, established "radio mode" AGN feedback as the critical quenching parameter.
[REV03-P047] | Noeske et al. (2007, ApJ) | DOI:10.1086/517926; arXiv:astro-ph/0701924; ADS:2007ApJ...660L..43N | role=measurement | Coined and defined the "Star Forming Main Sequence" against which models calibrate sustained growth.
[REV03-P048] | Mo et al. (1998, MNRAS) | DOI:10.1046/j.1365-8711.1998.01587.x; arXiv:astro-ph/9711159; ADS:1998MNRAS.295..319M | role=analytic_theory | Established the isothermal density profile scaling relations connecting dark halo properties to disk sizes.
[REV03-P049] | Dalla Vecchia & Schaye (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.13840.x; arXiv:0801.0772; ADS:2008MNRAS.387.1431D | role=hydrodynamic_simulation | Outlined the temporary hydrodynamic decoupling mechanism required to prevent instantaneous wind thermalization.
[REV03-P050] | Governato et al. (2010, Nature) | DOI:10.1038/nature08640; arXiv:0911.2237; ADS:2010Natur.463..203G | role=hydrodynamic_simulation | Showed that powerful winds can reshape dark matter profiles and prevent massive bulge overcooling.
[REV03-P051] | Fontanot et al. (2009, MNRAS) | DOI:10.1111/j.1365-2966.2009.15058.x; arXiv:0901.1130; ADS:2009MNRAS.397.1776F | role=semi_analytic_model | Exposed the persistent failure of calibrated SAMs to reproduce the "downsizing" of massive galaxies at high redshift.
[REV03-P052] | Scannapieco et al. (2012, MNRAS) | DOI:10.1111/j.1365-2966.2012.20993.x; arXiv:1112.0315; ADS:2012MNRAS.423.1726S | role=hydrodynamic_simulation | Multi-code comparison showing that disparate subgrid recipes cause massive divergence in final galaxy properties.
[REV03-P053] | Wuyts et al. (2011, ApJ) | DOI:10.1088/0004-637X/742/2/96; arXiv:1107.0317; ADS:2011ApJ...742...96W | role=measurement | Linked structural indices (Sersic) directly to positions on the Star-Forming Main Sequence.
[REV03-P054] | van der Wel et al. (2014, ApJ) | DOI:10.1088/0004-637X/788/1/28; arXiv:1404.2844; ADS:2014ApJ...788...28V | role=measurement | Comprehensive empirical benchmark for the size evolution of disk and spheroidal galaxies over 10 billion years.
[REV03-P055] | Muzzin et al. (2013, ApJ) | DOI:10.1088/0004-637X/777/1/18; arXiv:1303.4409; ADS:2013ApJ...777...18M | role=measurement | Pushed the bimodal mass function demographic baseline out to z=4.
[REV03-P056] | Hopkins et al. (2014, MNRAS) | DOI:10.1093/mnras/stu732; arXiv:1311.2073; ADS:2014MNRAS.445..581H | role=hydrodynamic_simulation | High-resolution explicit stellar feedback resolving the multi-phase ISM without cooling shutoffs.
[REV03-P057] | Tumlinson et al. (2011, Science) | DOI:10.1126/science.1209840; arXiv:1111.3975; ADS:2011Sci...334..948T | role=measurement | Groundbreaking COS-Halos observation proving that massive metal reservoirs reside in the CGM.
[REV03-P058] | Krumholz et al. (2009, ApJ) | DOI:10.1088/0004-637X/693/1/216; arXiv:0810.0011; ADS:2009ApJ...693..216K | role=analytic_theory | Provided the analytic framework used by codes to estimate the unresolved H
2
	​

 fraction from local metallicity.

REVIEW_BASE_03_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- cris.unibo.it Field-level simulation-based inference with galaxy catalogs - Unibo Opens in a new window — https://cris.unibo.it/retrieve/787c9f6f-d35c-4e7b-ab24-e36c4c45d58e/de_Santi_2025_J._Cosmol._Astropart._Phys._2025_082.pdf
- arxiv.org Tracing cosmic gas in filaments and halos: Low-redshift insights from the kinematic Sunyaev-Zel'dovich effect - arXiv Opens in a new window — https://arxiv.org/html/2412.03631v1
- uvic.ca ASTRO 504: COURSE SYLLABUS Prof. Arif Babul Wednesdays, 12-3pm Welcome to ASTR 504. Normally this graduate course has between - UVic Opens in a new window — https://www.uvic.ca/science/physics/assets/docs/outlines/2022-23/a504_202301.pdf
- physics.rutgers.edu Astrophysics - Department of Physics and Astronomy Opens in a new window — https://physics.rutgers.edu/research/research-group-astrophysics?start=10
- eprints.soton.ac.uk JCAP02(2026)001 - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/510320/2/Lapi_2026_J._Cosmol._Astropart._Phys._2026_001.pdf
- aip.de The Impact of Magnetic Fields on Cosmological Galaxy Mergers - Leibniz-Institute for Astrophysics Potsdam (AIP) Opens in a new window — https://www.aip.de/media/thesis/joseph-whittingham-master-thesis.pdf
- arxiv.org A self-similar model of galaxy formation and dark halo relaxation - arXiv Opens in a new window — https://arxiv.org/html/2311.13952v2
- academic.oup.com Evolution of the atomic and molecular gas content of galaxies in dark matter haloes | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/449/1/477/1322723
- academic.oup.com NIHAO project – I. Reproducing the inefficiency of galaxy formation across cosmic time with a large sample of cosmological hydrodynamical simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/454/1/83/1127627
- annualreviews.org Annual Review of Astronomy and Astrophysics - Volume 53, 2015 Opens in a new window — https://www.annualreviews.org/content/journals/astro/53/1
- scholar.google.com ‪Rachel Somerville‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=uwbs_h0AAAAJ&hl=en
- ned.ipac.caltech.edu Normal Galaxies Opens in a new window — https://ned.ipac.caltech.edu/level5/normal_galaxies.html
- ir.library.osaka-u.ac.jp Physically-motivated feedback models and the IGM metal enrichment in cosmological hydrodynamic simulations Opens in a new window — https://ir.library.osaka-u.ac.jp/repo/ouka/all/96417/34336_Dissertation.pdf
- cpt.univ-mrs.fr EC16 — Program Opens in a new window — https://www.cpt.univ-mrs.fr/~cosmo/EC2025/index.php?page=program
- annualreviews.org Key Physical Processes in the Circumgalactic Medium - Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-052920-125203
- annualreviews.org Theory and Observation of Winds from Star-Forming Galaxies | Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-041224-011924
- annualreviews.org Galaxy Formation and Reionization: Key Unknowns and Expected Breakthroughs by the James Webb Space Telescope | Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-120221-044656
- arxiv.org The Contribution of Stars, Dust, Neutral Gas and Supermassive Black Holes in Galaxies to the Cosmic Baryon Inventory - arXiv Opens in a new window — https://arxiv.org/html/2601.08112v3
- scispace.com (Open Access) Formation of supermassive black holes (2010) | Marta Volonteri | 771 Citations - SciSpace Opens in a new window — https://scispace.com/papers/formation-of-supermassive-black-holes-55ox4yo3s2
- researchgate.net (PDF) A Hierarchy of Normalizing Flows for Modelling the Galaxy-Halo Relationship Opens in a new window — https://www.researchgate.net/publication/372404155_A_Hierarchy_of_Normalizing_Flows_for_Modelling_the_Galaxy-Halo_Relationship
- researchgate.net Star formation rate density of the universe as a function of redshift.... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Star-formation-rate-density-of-the-universe-as-a-function-of-redshift-The-green-line_fig5_267159354
- researchgate.net (PDF) Numerical Simulations of Galaxy Formation - ResearchGate Opens in a new window — https://www.researchgate.net/publication/2307934_Numerical_Simulations_of_Galaxy_Formation
- academic.oup.com Sub-mm emission line deep fields: CO and [C ii] luminosity functions out to z = 6 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/461/1/93/2595288
- ml4astro.github.io Learning Galaxy Properties from Merger Trees - GitHub Pages Opens in a new window — https://ml4astro.github.io/icml2022/assets/41.pdf
- arxiv.org Mufasa: Galaxy Formation Simulations With Meshless Hydrodynamics - arXiv Opens in a new window — https://arxiv.org/pdf/1604.01418
- pos.sissa.it PoS(MeerKAT2016)025 Opens in a new window — https://pos.sissa.it/277/025/pdf
- iris.sissa.it Dust in hydrodynamic and semi-analytic galaxy evolution simulations - IRIS Opens in a new window — https://iris.sissa.it/retrieve/83c739da-7b6b-4e09-ad4e-9f3a6f116f7d/PhDThesis_Parente.pdf
- pa.msu.edu UNRAVELING GALAXY EVOLUTION USING NUMERICAL SIMULATIONS By Claire Kopenhafer A DISSERTATION Submitted to Michigan State Universi Opens in a new window — https://pa.msu.edu/graduate-program/current-graduate-students/draft-dissertation-pdf/kopenhafer_disseration_dual-astro-cmse.pdf
- eprints.soton.ac.uk Galaxy formation through the lens of galaxy structure with semi-empirical models and deep learning - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/467307/1/Zanisi_thesis_final.pdf
- research.ed.ac.uk Cosmological baryon transfer in the SIMBA simulations - University of Edinburgh Research Explorer Opens in a new window — https://www.research.ed.ac.uk/files/250789766/1910.00594v1.pdf
- arxiv.org The baryon cycle in modern cosmological hydrodynamical simulations - arXiv Opens in a new window — https://arxiv.org/html/2402.08408v2
- arxiv.org Why do semi-analytic models predict higher scatter in the stellar mass–halo mass relation than cosmological hydrodynamic simulations? - arXiv Opens in a new window — https://arxiv.org/html/2310.11507v1
- arxiv.org Chapter 0 Cosmological Simulations of Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2507.08925v1
- pure.ed.ac.uk The Origin of the Dust Extinction Curve in Milky Way-like Galaxies - Account Opens in a new window — https://www.pure.ed.ac.uk/ws/files/331579173/2012.03978v1.pdf
- arxiv.org Satellite quenching by radio jets of central galaxies in galaxy groups - arXiv Opens in a new window — https://arxiv.org/html/2607.02801v1
- arxiv.org Do we understand the star formation history of the universe? - arXiv Opens in a new window — https://arxiv.org/html/2607.09848v1
- iris.sissa.it Modified Gravity in Galaxy Clusters: Insights from the Caustic Technique - IRIS Opens in a new window — https://iris.sissa.it/retrieve/241f031e-8d11-48fa-929b-0ccbc9311cfa/PhD_Thesis_Butt.pdf
- aip.de Numerical Simulations of Jellyfish Galaxies Nikolaos Sagias - Leibniz-Institute for Astrophysics Potsdam (AIP) Opens in a new window — https://www.aip.de/media/thesis/nikolaos-sagias-master-thesis.pdf
- academic.oup.com nIFTy cosmology: comparison of galaxy formation models | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/451/4/4029/1105073
- arxiv.org RABBITS – III. Modelling relativistic accretion discs around spinning black holes in galaxy formation simulations - arXiv Opens in a new window — https://arxiv.org/html/2603.17607v1
- arxiv.org Tracing black hole and galaxy growth across environments since cosmic noon - arXiv Opens in a new window — https://arxiv.org/html/2607.07793v1
- arxiv.org Multi-modal Foundation Model for Cosmological Simulation Data - arXiv Opens in a new window — https://arxiv.org/html/2510.07684v1
- arxiv.org [1412.2712] Physical Models of Galaxy Formation in a Cosmological Framework - arXiv Opens in a new window — https://arxiv.org/abs/1412.2712
- arxiv.org Using Planck maps for a systematic search of ultra-bright high-redshift strongly lensed galaxies - arXiv Opens in a new window — https://arxiv.org/html/2503.18116v1
- ned.ipac.caltech.edu Physical Models of Galaxy Formation in a Cosmological Framework - Rachel S. Somerville & Romeel Davé Opens in a new window — https://ned.ipac.caltech.edu/level5/March19/Somerville/Somerville_contents.html
- ned.ipac.caltech.edu Physical Models of Galaxy Formation in a Cosmological Framework - Rachel S. Somerville & Romeel Davé Opens in a new window — https://ned.ipac.caltech.edu/level5/March19/Somerville/frames.html
- ned.ipac.caltech.edu Physical Models of Galaxy Formation in a Cosmological Framework - Rachel S. Somerville & Romeel Davé Opens in a new window — https://ned.ipac.caltech.edu/level5/March19/Somerville/Somerville1.html
- ned.ipac.caltech.edu Physical Models of Galaxy Formation in a Cosmological Framework - Rachel S. Somerville & Romeel Davé Opens in a new window — https://ned.ipac.caltech.edu/level5/March19/Somerville/Somerville4.html
- ned.ipac.caltech.edu Physical Models of Galaxy Formation in a Cosmological Framework - Rachel S. Somerville & Romeel Davé Opens in a new window — https://ned.ipac.caltech.edu/level5/March19/Somerville/Somerville3.html
- ned.ipac.caltech.edu Physical Models of Galaxy Formation in a Cosmological Framework - Rachel S. Somerville & Romeel Davé Opens in a new window — https://ned.ipac.caltech.edu/level5/March19/Somerville/Somerville2.html
- ned.ipac.caltech.edu Opens in a new window — https://ned.ipac.caltech.edu/level5/March19/Somerville/Somerville_refs.html
- arxiv.org Stellar Mass Growth in the First Galaxies: Theory and Observation - arXiv Opens in a new window — https://arxiv.org/html/2602.01549v1
- academic.oup.com MUFASA: galaxy star formation, gas and metal properties across cosmic time - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/467/1/115/10321546/stx108.pdf
- research.chalmers.se Effects of Varied Cosmic Ray Feedback from AGN on Massive Galaxy Properties - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/551428/file/551428_Fulltext.pdf
- ml4astro.github.io A Hierarchy of Normalizing Flows for Modelling the Galaxy–Halo Relationship - GitHub Pages Opens in a new window — https://ml4astro.github.io/icml2023/assets/63.pdf
- ned.ipac.caltech.edu inflows, outflows, and recycling - The Circumgalactic Medium - Jason Tumlinson et al. Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Tumlinson/Tumlinson7.html
- ned.ipac.caltech.edu Physical Models of Galaxy Formation in a Cosmological Framework - NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/level5/March19/Somerville/paper.pdf
- ml4physicalsciences.github.io First High-Resolution Galaxy Simulations Accelerated by a 3D Surrogate Model for Supernovae - Machine Learning and the Physical Sciences Opens in a new window — https://ml4physicalsciences.github.io/2024/files/NeurIPS_ML4PS_2024_83.pdf
- pmc.ncbi.nlm.nih.gov Fast and inefficient star formation due to short-lived molecular clouds and rapid feedback - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC6544524/
- arxiv.org A massive galaxy that formed its stars at z∼11 - arXiv Opens in a new window — https://arxiv.org/html/2308.05606v3
- eprints.soton.ac.uk arXiv:2502.12764v1 [astro-ph.GA] 18 Feb 2025 - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/502442/1/2502.12764v1.pdf
- arxiv.org Introducing sapphire: Towards Hybrid Physics-Informed, Data-Driven Modeling of Galaxy Formation - arXiv Opens in a new window — https://arxiv.org/html/2604.06318v1
- arxiv.org Galaxy Phase-Space and Field-Level Cosmology: The Strength of Semi-Analytic Models - arXiv Opens in a new window — https://arxiv.org/pdf/2512.10222
- academic.oup.com Star formation in semi-analytic galaxy formation models with multiphase gas - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/453/4/4337/2593703
- pure.ed.ac.uk The Diversity and Variability of Star Formation Histories in Models of Galaxy Evolution - Account Opens in a new window — https://www.pure.ed.ac.uk/ws/files/156891867/Dave_2007.07916.pdf
- academic.oup.com art of modelling CO, [C i], and [C ii] in cosmological galaxy formation models - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/482/4/4906/5162849
- pure.ed.ac.uk Semi-analytic forecasts for JWST -- II. physical properties and scaling relations for galaxies at z = 4-10 - Account Opens in a new window — https://www.pure.ed.ac.uk/ws/files/121576035/1901.05964.pdf
- academic.oup.com mufasa: galaxy formation simulations with meshless hydrodynamics - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/462/3/3265/2589915
- academic.oup.com Mufasa: galaxy star formation, gas and metal properties across cosmic time - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/467/1/115/2907765
- arxiv.org Impact of star formation models on the growth of simulated galaxies at high redshifts - arXiv Opens in a new window — https://arxiv.org/html/2407.12090v3
- academic.oup.com How stellar feedback simultaneously regulates star formation and drives outflows | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/465/2/1682/2454749
- ned.ipac.caltech.edu Theoretical Challenges in Galaxy Formation Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Naab/paper.pdf
- research.aalto.fi Barré, Ruxin; Babul, Arif; Gozaliasl, Ghassem; Finoguenov, Alexis; Davé, Romeel; Padawer- Blatt, Aviv; Rennehan, Douglas; Saee - Aalto Research Portal Opens in a new window — https://research.aalto.fi/files/219707606/Forged_by_Feedback_-_Stellar_Properties_of_Brightest_Group_Galaxies_in_Cosmological_Simulations.pdf
- researchgate.net Core condensation in heavy halos - A two-stage theory for galaxy formation and clustering Opens in a new window — https://www.researchgate.net/publication/234256454_Core_condensation_in_heavy_halos_-_A_two-stage_theory_for_galaxy_formation_and_clustering
- academic.oup.com 1978MNRAS.183..341W Opens in a new window — https://academic.oup.com/mnras/article-pdf/183/3/341/2943374/mnras183-0341.pdf
- oamonitor.ireland.openaire.eu Hidden cooling flows in clusters of galaxies – III. Accretion on to the central black hole Opens in a new window — https://oamonitor.ireland.openaire.eu/rpo/ucd/search/publication?pid=10.1093%2Fmnras%2Fstad1870
- academic.oup.com Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/183/3/341/972568
- scispace.com (Open Access) The formation of Stars and Evolution of Galaxies (2018) | Aadil Aziz Bhat Opens in a new window — https://scispace.com/papers/the-formation-of-stars-and-evolution-of-galaxies-qmyteqg5uc
- journals.jps.jp Star Formation and Gas Flow History of a Dwarf Irregular Galaxy Traced by Gas-phase and Stellar Abundances - JPS Journals Opens in a new window — https://journals.jps.jp/doi/10.7566/JPSCP.31.011051?mobileUi=0
- researchgate.net (PDF) Galaxy formation through hierarchical clustering - ResearchGate Opens in a new window — https://www.researchgate.net/publication/23600825_Galaxy_formation_through_hierarchical_clustering
- thphys.uni-heidelberg.de Cosmology Seminar: Presentation Topics Opens in a new window — https://www.thphys.uni-heidelberg.de/~amendola/teaching/seminar_topics.pdf
- arxiv.org K-DRIFT Science Theme: Galaxies in the Faint Universe - arXiv Opens in a new window — https://arxiv.org/html/2602.08283
- jhss.scholasticahq.com Investigating galaxy clustering dependence on neutral hydrogen mass through dark halo properties Opens in a new window — https://jhss.scholasticahq.com/article/120080-investigating-galaxy-clustering-dependence-on-neutral-hydrogen-mass-through-dark-halo-properties.pdf
- koreascience.kr ON THE PHYSICAL BASIS OF THE TULLY-FISHER RELATION -Journal of The Korean Astronomical Society | Korea Science Opens in a new window — https://koreascience.kr/journal/view.jsp?kj=CMHHBA&py=2004&vnc=v37n1&sp=15
- weizmann.esploro.exlibrisgroup.com THE ORIGIN OF DWARF GALAXIES, COLD DARK MATTER, AND BIASED GALAXY FORMATION - The Weizmann Institute of Science - WIS Works Opens in a new window — https://weizmann.esploro.exlibrisgroup.com/esploro/outputs/journalArticle/THE-ORIGIN-OF-DWARF-GALAXIES-COLD/993262857503596
- ouci.dntb.gov.ua Survival of star-forming giant clumps in high-redshift galaxies - OUCI Opens in a new window — https://ouci.dntb.gov.ua/en/works/4Oj0oaq7/
- scispace.com Avishai Dekel | The Racah Institute of Physics | 540 Publications | 8795 Citations - SciSpace Opens in a new window — https://scispace.com/authors/avishai-dekel-21k7wob0j1
- academic.oup.com Co-evolution of baryons and dark matter haloes of LYRA dwarf galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/548/3/stag709/8654595
- academic.oup.com The influence of globular cluster evolution on the specific frequency in dwarf galaxies Opens in a new window — https://academic.oup.com/mnras/article/527/2/2765/7331442
- osti.gov Clump survival and migration in VDI galaxies: an analytical model versus simulations and observations (Journal Article) - OSTI Opens in a new window — https://www.osti.gov/pages/biblio/1843531
- ouci.dntb.gov.ua The assembly history of NGC 1365 through chemical archaeology - OUCI Opens in a new window — https://ouci.dntb.gov.ua/en/works/loNrPJvQ/
- arxiv.org Properties of Galaxies with Counter-rotating Stellar Disks in the MaNGA Survey - arXiv Opens in a new window — https://arxiv.org/pdf/2603.04044
- articles.researchsolutions.com Formation and rotation of disc galaxies with haloes - Research Solutions Pages Opens in a new window — https://articles.researchsolutions.com/formation-and-rotation-of-disc-galaxies-with-haloes/doi/10.1093/mnras/193.2.189
- academic.oup.com 1980MNRAS.193..189F Opens in a new window — https://academic.oup.com/mnras/article-pdf/193/2/189/2939800/mnras193-0189.pdf
- oamonitor.ireland.openaire.eu Large Disklike Galaxies at High Redshift Opens in a new window — https://oamonitor.ireland.openaire.eu/rfo/irish-research-council3/search/publication?pid=10.1086%2F377149
- academic.oup.com Formation and rotation of disc galaxies with haloes - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/193/2/189/972375
- academic.oup.com The origin of scatter in the star formation rate–stellar mass relation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/484/1/915/5281289
- arxiv.org Evolution of the Physical Properties of the Most Massive Galaxies in Clusters and their Protohalos - arXiv Opens in a new window — https://arxiv.org/pdf/2509.05637
- academic.oup.com Galactic star formation and accretion histories from matching galaxies to dark matter haloes | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/428/4/3121/997374?view=extract
- scispace.com Benjamin P. Moster | Ludwig Maximilian University of Munich | 61 Publications | 1162 Citations | Related Authors - SciSpace Opens in a new window — https://scispace.com/authors/benjamin-p-moster-207y1cpnur
- osti.gov The dark side of galaxy stellar populations – I. The stellar-to-halo mass relation and the velocity dispersion–halo mass relation (Journal Article) | OSTI.GOV Opens in a new window — https://www.osti.gov/pages/biblio/1982671
- academic.oup.com Galactic star formation and accretion histories from matching galaxies to dark matter haloes | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/428/4/3121/997374
- researchgate.net THE AVERAGE STAR FORMATION HISTORIES OF GALAXIES IN DARK MATTER HALOS FROMz= 0-8 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/230568640_THE_AVERAGE_STAR_FORMATION_HISTORIES_OF_GALAXIES_IN_DARK_MATTER_HALOS_FROMz_0-8
- oamonitor.ireland.openaire.eu THE AVERAGE STAR FORMATION HISTORIES OF GALAXIES IN DARK MATTER HALOS FROMz= 0-8 - National Open Access Monitor, Ireland Opens in a new window — https://oamonitor.ireland.openaire.eu/rpo/tcd/search/publication?pid=10.1088%2F0004-637x%2F770%2F1%2F57
- academic.oup.com Universe at z > 10: predictions for JWST from the universemachine DR1 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/499/4/5702/5923580
- arxiv.org The Average Star Formation Histories of Galaxies in Dark Matter Halos from z=0-8 - arXiv Opens in a new window — https://arxiv.org/abs/1207.6105
- academic.oup.com Constraining scatter in the stellar mass–halo mass relation for haloes less massive than the Milky Way | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/488/4/4916/5544770
- frontiersin.org Probing cosmic voids with emission-line galaxies - Frontiers Opens in a new window — https://www.frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2025.1607031/full
- academic.oup.com Observational measures of halo properties beyond mass - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/509/2/2800/6423431
- scispace.com Hao-Yi Wu | Ohio State University | 67 Publications | 227 Citations | Related Authors Opens in a new window — https://scispace.com/authors/hao-yi-wu-1cd8yk6vtu
- academic.oup.com Observing correlations between dark matter accretion and galaxy growth: II. testing the impact of galaxy mass, star formation indicator, and neighbour colours - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/509/3/3285/6415897
- academic.oup.com UniverseMachine: The correlation between galaxy growth and dark matter halo assembly from z = 0−10 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/488/3/3143/5484868
- physicstoday.aip.org Theoretical challenges in understanding galaxy evolution - Physics Today Opens in a new window — https://physicstoday.aip.org/features/theoretical-challenges-in-understanding-galaxy-evolution
- academic.oup.com How do galaxies get their gas? - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/363/1/2/4126209/363-1-2.pdf
- academic.oup.com How do galaxies get their gas? | Monthly Notices of the Royal Astronomical Society Opens in a new window — https://academic.oup.com/mnras/article-abstract/363/1/2/1300118
- academic.oup.com How do galaxies get their gas? | Monthly Notices of the Royal Astronomical Society Opens in a new window — https://academic.oup.com/mnras/article/363/1/2/1300118
- academic.oup.com Galactic inflow and wind recycling rates in the eagle simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/497/4/4495/5881953
- arxiv.org Searching for correlations between satellite galaxy populations and the cold circumgalactic medium around TNG50 galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/2504.16191
- arxiv.org arXiv:2203.12639v1 [astro-ph.GA] 23 Mar 2022 Opens in a new window — https://arxiv.org/pdf/2203.12639
- arxiv.org Cosmological Galaxy Evolution with Superbubble Feedback I - arXiv Opens in a new window — https://arxiv.org/pdf/1505.06268
- arxiv.org The Spatially-Resolved Star Formation History of the M31 Outer Disc - arXiv Opens in a new window — https://arxiv.org/pdf/1508.01559
- ned.ipac.caltech.edu Outskirts of Nearby Disk Galaxies: Star Formation and Stellar Populations - Bruce G. Elmegreen & Deidre A. Hunter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Elmegreen/Elmegreen_refs.html
- academic.oup.com Towards a more realistic population of bright spiral galaxies in cosmological simulations Opens in a new window — https://academic.oup.com/mnras/article/434/4/3142/959773
- ouci.dntb.gov.ua Outskirts of Nearby Disk Galaxies: Star Formation and Stellar Populations - OUCI Opens in a new window — https://ouci.dntb.gov.ua/works/7ppePE57/
- academic.oup.com Erratum: Galactic chemical evolution in hierarchical formation Opens in a new window — https://academic.oup.com/mnras/article-pdf/424/1/800/3302301/mnras0424-0800.pdf
- academic.oup.com Galactic chemical evolution in hierarchical formation models – I. Early-type galaxies in the local Universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/402/1/173/1030305
- arxiv.org Galactic chemical evolution in hierarchical formation models - II. The Intracluster Medium. - arXiv Opens in a new window — https://arxiv.org/pdf/1006.1147
- arxiv.org implications for the mass assembly and the chemical enrichment of galaxies in the GAEA model. - arXiv Opens in a new window — https://arxiv.org/pdf/1606.01908
- ned.ipac.caltech.edu The Dawes Review 8: Measuring the Stellar Initial Mass Function - A. M. Hopkins Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Hopkins/Hopkins_refs.html
- arxiv.org arXiv:2203.13405v1 [astro-ph.GA] 25 Mar 2022 Opens in a new window — https://arxiv.org/pdf/2203.13405
- arxiv.org Tracing Quenching in Nearby Galaxies Through Inner Surface Mass Density and Cold Gas Content - arXiv Opens in a new window — https://arxiv.org/pdf/2511.18227
- arxiv.org Probing IMF Variations in High-Redshift Early-Type Galaxies with SHARP - arXiv Opens in a new window — https://arxiv.org/html/2606.31189v1
- sites.lsa.umich.edu Research | Eric F. Bell Opens in a new window — https://sites.lsa.umich.edu/ericbell/research/
- arxiv.org arXiv:1207.5814v1 [astro-ph.CO] 24 Jul 2012 Opens in a new window — https://arxiv.org/pdf/1207.5814
- arxiv.org The nature of extremely red galaxies in the local universe - arXiv Opens in a new window — https://arxiv.org/pdf/1306.6552
- arxiv.org arXiv:1407.6715v1 [astro-ph.GA] 24 Jul 2014 Opens in a new window — https://arxiv.org/pdf/1407.6715
- arxiv.org arXiv:1502.07040v1 [astro-ph.GA] 25 Feb 2015 Opens in a new window — https://arxiv.org/pdf/1502.07040
- academic.oup.com Gusty, gaseous flows of FIRE: galactic winds in cosmological simulations with explicit stellar feedback | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/454/3/2691/1199578
- academic.oup.com Gusty, gaseous flows of FIRE: galactic winds in cosmological simulations with explicit stellar feedback - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/454/3/2691/4032533/stv2126.pdf
- academic.oup.com Characterizing mass, momentum, energy, and metal outflow rates of multiphase galactic winds in the FIRE-2 cosmological simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/508/2/2979/6380532
- surveygizmoresponseuploads.s3.amazonaws.com Astro2020 Science White Paper Cold Gas Outflows, Feedback, and the Shaping of Galaxies - AWS Opens in a new window — http://surveygizmoresponseuploads.s3.amazonaws.com/fileuploads/623127/4458621/100-dd08c3e894ca4690aac6fd5e042e632a_BolattoAlbertoD.pdf
- arxiv.org Evaluating Mass Outflow Rate Estimators in FIRE-2 Simulations: Towards a Self-Consistent Framework for Spectral Line Based Predictions - arXiv Opens in a new window — https://arxiv.org/html/2503.22312v1
- academic.oup.com Gusty, gaseous flows of FIRE: galactic winds in cosmological simulations with explicit stellar feedback | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/454/3/2691/1199578
- arxiv.org White Paper Stellar Mass - arXiv Opens in a new window — https://arxiv.org/html/2601.14666v1
- perso.ens-lyon.fr Galaxy interaction induced star formation at different redshifts Opens in a new window — https://perso.ens-lyon.fr/jeremy.fensch/sb.html
- arxiv.org The total infrared luminosity may significantly overestimate the star formation rate of quenching and recently quenched galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/1402.0006
- www2.mpia-hd.mpg.de the star formation law in nearby galaxies on sub-kpc scales - Max-Planck-Institut für Astronomie Opens in a new window — https://www2.mpia-hd.mpg.de/THINGS/Publications_files/THINGS_Bigiel.pdf
- arxiv.org The Schmidt Law at High Molecular Densities - arXiv Opens in a new window — https://arxiv.org/pdf/astro-ph/0508347
- arxiv.org arXiv:0807.1116v2 [astro-ph] 11 Jul 2008 Opens in a new window — https://arxiv.org/pdf/0807.1116
- arxiv.org [0810.2541] The Star Formation Law in Nearby Galaxies on Sub-Kpc Scales - arXiv Opens in a new window — https://arxiv.org/abs/0810.2541
- researchprofiles.herts.ac.uk The star formation law in nearby galaxies on sub-kpc scales - University of Hertfordshire (Research Profiles) Opens in a new window — https://researchprofiles.herts.ac.uk/en/publications/the-star-formation-law-in-nearby-galaxies-on-sub-kpc-scales/
- arxiv.org arXiv:1511.05633v1 [astro-ph.GA] 18 Nov 2015 Opens in a new window — https://arxiv.org/pdf/1511.05633
- sfb1601.astro.uni-koeln.de Project B3 - SFB 1601 Opens in a new window — https://sfb1601.astro.uni-koeln.de/projects/projectb/b3/
- arxiv.org arXiv:2409.07622v2 [astro-ph.GA] 14 Nov 2024 Opens in a new window — https://arxiv.org/pdf/2409.07622
- researchprofiles.herts.ac.uk The star formation efficiency in nearby galaxies: measuring where Opens in a new window — https://researchprofiles.herts.ac.uk/en/publications/the-star-formation-efficiency-in-nearby-galaxies-measuring-where-/
- arxiv.org [0810.2556] The Star Formation Efficiency in Nearby Galaxies: Measuring Where Gas Forms Stars Effectively - arXiv Opens in a new window — https://arxiv.org/abs/0810.2556
- arxiv.org Molecular Gas and Star Formation in Dwarf Galaxies Observed by the Atacama Large Millimeter/submillimeter Array - arXiv Opens in a new window — https://arxiv.org/pdf/2511.21187
- arxiv.org arXiv:1210.0549v2 [astro-ph.GA] 3 Oct 2012 Opens in a new window — https://arxiv.org/pdf/1210.0549
- arxiv.org arXiv:1412.2132v1 [astro-ph.GA] 5 Dec 2014 Opens in a new window — https://arxiv.org/pdf/1412.2132
- arxiv.org arXiv:1108.5731v2 [astro-ph.CO] 22 Oct 2011 Opens in a new window — https://arxiv.org/pdf/1108.5731
- mso.anu.edu.au DWARF GALAXY FORMATION WITH H2-REGULATED STAR FORMATION - Research School of Astronomy & Astrophysics Opens in a new window — https://www.mso.anu.edu.au/~krumholz/publications/2012/kuhlen12a.pdf
- academic.oup.com Molecular hydrogen abundances of galaxies in the EAGLE simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/452/4/3815/18235819/stv1488.pdf
- lss.fnal.gov arXiv:2310.10712v1 [astro-ph.GA] 16 Oct 2023 Opens in a new window — https://lss.fnal.gov/archive/2024/pub/fermilab-pub-24-0366-t.pdf
- academic.oup.com Implementing molecular hydrogen in hydrodynamic simulations of galaxy formation Opens in a new window — https://academic.oup.com/mnras/article-pdf/425/4/3058/4913493/425-4-3058.pdf
- arxiv.org arXiv:1010.1539v2 [astro-ph.CO] 22 Mar 2011 Opens in a new window — https://arxiv.org/pdf/1010.1539
- wwwmpa.mpa-garching.mpg.de Physical properties for galaxies and active galactic nuclei in the Sloan Digital Sky Survey: Data catalogues from SDSS studies at MPA/JHU Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/SDSS/index_old.html
- arxiv.org arXiv:0910.2118v1 [astro-ph.CO] 12 Oct 2009 Opens in a new window — https://arxiv.org/pdf/0910.2118
- academic.oup.com The ages and metallicities of galaxies in the local universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/362/1/41/1344664
- arxiv.org Modelling the mass-metallicity relation of star-forming galaxies from ζ ∼ 3.5 to ζ ∼ 0 - arXiv Opens in a new window — https://arxiv.org/pdf/1809.04079
- academic.oup.com The ages and metallicities of galaxies in the local universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/362/1/41/1344664
- arxiv.org The Cosmic Evolution of Metallicity from the SDSS Fossil Record - arXiv Opens in a new window — https://arxiv.org/pdf/0804.3091
- academic.oup.com Feedback in simulations of disc-galaxy major mergers - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/373/3/1013/1061246
- arxiv.org [astro-ph/0503201] Feedback in simulations of disc-galaxy major mergers - arXiv Opens in a new window — https://arxiv.org/abs/astro-ph/0503201
- arxiv.org Tracing correlations between galaxy properties across the Cosmic Web: An IllustrisTNG-based study - arXiv Opens in a new window — https://arxiv.org/html/2509.11288v1
- arxiv.org Quantified H i Morphology III: Merger Visibility Times from H i in Galaxy Simulations - arXiv Opens in a new window — https://arxiv.org/pdf/1104.3306
- arxiv.org Do group dynamics play a role in the evolution of member galaxies? - arXiv Opens in a new window — https://arxiv.org/pdf/1308.1406
- academic.oup.com Feedback in simulations of disc-galaxy major mergers - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/373/3/1013/1061246
- academic.oup.com Constraints on star formation driven galaxy winds from the mass–metallicity relation at z= 0 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/417/4/2962/1099813
- academic.oup.com Constraints on star formation driven galaxy winds from the mass–metallicity relation at z = 0 Opens in a new window — https://academic.oup.com/mnras/article-pdf/417/4/2962/3841245/mnras0417-2962.pdf
- arxiv.org An empirical prediction for stellar metallicity distributions in nearby galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/1208.4366
- arxiv.org Cosmological Galaxy Evolution with Superbubble Feedback II: The Limits of Supernovae - arXiv Opens in a new window — https://arxiv.org/pdf/1604.08244
- arxiv.org Declining metallicity and extended HeII in the outflow of an epoch of reionization analogue galaxy - arXiv Opens in a new window — https://arxiv.org/pdf/2510.05332
- arxiv.org Star Formation in Semi-Analytic Galaxy Formation Models with Multiphase Gas - arXiv Opens in a new window — https://arxiv.org/pdf/1503.00755
- ned.ipac.caltech.edu Outskirts of Distant Galaxies In Absorption - Hsiao-Wen Chen Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Chen/Chen_refs.html
- arxiv.org arXiv:1509.00853v1 [astro-ph.GA] 2 Sep 2015 Opens in a new window — https://arxiv.org/pdf/1509.00853
- par.nsf.gov arXiv:2407.11125v3 [astro-ph.GA] 10 Dec 2024 Opens in a new window — https://par.nsf.gov/servlets/purl/10561233
- cxc.harvard.edu Constraining galaxy formation with gaseous halos Solving - Chandra X-ray Center Opens in a new window — https://cxc.harvard.edu/cdo/xray_surveyor/presentations/Kravtsov-Andrey.pdf
- ned.ipac.caltech.edu The modelling of feedback in star formation simulations - James E. Dale Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept15/Dale/Dale_refs.html
- arxiv.org The Importance of Where and When Massive Stars Form in Molecular Clouds - arXiv Opens in a new window — https://arxiv.org/pdf/1809.08344
- arxiv.org Star formation quenching imprinted on the internal structure of naked red nuggets - arXiv Opens in a new window — https://arxiv.org/pdf/1906.00007
- openaccess.inaf.it Publication Year 2017 Acceptance in OA 2021-02-08T11:25:25Z Opens in a new window — https://openaccess.inaf.it/bitstreams/df5edb61-2a66-42c5-91af-97b700ee8dea/download
- eprints.soton.ac.uk The evolution of compact massive quiescent and starforming galaxies derived from the Re − Rh and Mstar - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/450939/1/The_evolution_of_compact_massive_quiescent_and_star_forming_galaxies_derived_from_the_Re_Rhand_Mstar_Mhrelations.pdf
- arxiv.org arXiv:2207.10655v2 [astro-ph.GA] 20 Sep 2022 Opens in a new window — https://arxiv.org/pdf/2207.10655
- mpe.mpg.de The Kinematics of Massive Quiescent Galaxies at 1.4 < z < 2.1: Dark Matter Fractions, IMF Variation, and the Relation to L Opens in a new window — https://www.mpe.mpg.de/~saglia/journals_pdf/mendel2020.pdf
- arxiv.org arXiv:1309.2427v1 [astro-ph.CO] 10 Sep 2013 Opens in a new window — https://arxiv.org/pdf/1309.2427
- doi.org Modeling the distribution of dark matter and its connection to galaxies | Zenodo - DOI Opens in a new window — https://doi.org/10.5281/zenodo.56419
- arxiv.org arXiv:1207.6105v2 [astro-ph.CO] 29 May 2013 Opens in a new window — https://arxiv.org/pdf/1207.6105
- arxiv.org Using Cumulative Number Densities to Compare Galaxies across Cosmic Time - arXiv Opens in a new window — https://arxiv.org/pdf/1308.3232
- arxiv.org Using Cumulative Number Densities to Compare Galaxies Across Cosmic Time - arXiv Opens in a new window — https://arxiv.org/html/1308.3232v3
- arxiv.org Constraining the scatter in the galaxy-halo connection at Milky Way masses - arXiv Opens in a new window — https://arxiv.org/pdf/1910.03605
- arxiv.org Is Main Sequence Galaxy Star Formation Controlled by Halo Mass Accretion? - arXiv Opens in a new window — https://arxiv.org/pdf/1508.04842
- icc.dur.ac.uk Publication List 2005-2009 (Alphabetical order) - Institute for Computational Cosmology - Durham University Opens in a new window — https://icc.dur.ac.uk/index.php?content=Staff/Pubs_list2
- academic.oup.com Breaking the hierarchy of galaxy formation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/370/2/645/2898993/mnras0370-0645.pdf
- academic.oup.com Breaking the hierarchy of galaxy formation | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/370/2/645/967437
- arxiv.org [astro-ph/0511338] The broken hierarchy of galaxy formation - arXiv Opens in a new window — https://arxiv.org/abs/astro-ph/0511338
- arxiv.org A chronicle of galaxy mass assembly in the EAGLE simulation - arXiv Opens in a new window — https://arxiv.org/pdf/1609.07243
- academic.oup.com Breaking the hierarchy of galaxy formation | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/370/2/645/967437
- arxiv.org arXiv:1505.04977v2 [astro-ph.GA] 22 Oct 2015 Opens in a new window — https://arxiv.org/pdf/1505.04977
- researchgate.net Ultraviolet through Infrared Spectral Energy Distributions from 1000 Opens in a new window — https://www.researchgate.net/publication/386726504_Ultraviolet_through_Infrared_Spectral_Energy_Distributions_from_1000_SDSS_Galaxies_Dust_Attenuation
- academic.oup.com The galaxy stellar mass–star formation rate relation Opens in a new window — https://academic.oup.com/mnras/article-pdf/385/1/147/3432823/mnras0385-0147.pdf
- doi.org THE NATURE OF A GALAXY ALONG THE SIGHT LINE TO PKS 0454+039 - DOI Opens in a new window — https://doi.org/10.1088/0004-6256/144/4/111
- academic.oup.com Quenching star formation: insights from the local main sequence - Oxford Academic Opens in a new window — https://academic.oup.com/mnrasl/article-pdf/455/1/L82/56942278/mnrasl_455_1_l82.pdf
- academic.oup.com The total infrared luminosity may significantly overestimate the star formation rate of quenching and recently quenched galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/445/2/1598/18197927/stu1843.pdf
- academic.oup.com E pur si muove: Galilean-invariant cosmological hydrodynamical simulations on a moving mesh | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/401/2/791/1147356
- academic.oup.com Shock finding on a moving mesh – I. Shock statistics in non-radiative cosmological simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/446/4/3992/2892943
- academic.oup.com Moving-mesh cosmology: properties of neutral hydrogen in absorption | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/429/4/3341/1017132
- h-its.org A Milky Way out of the Supercomputer - HITS - Heidelberg Institute for Theoretical Studies Opens in a new window — https://www.h-its.org/2014/03/10/a-milky-way-out-of-the-supercomputer/
- arxiv.org [0901.4107] E pur si muove: Galiliean-invariant cosmological hydrodynamical simulations on a moving mesh - arXiv Opens in a new window — https://arxiv.org/abs/0901.4107
- academic.oup.com Improving the convergence properties of the moving-mesh code AREPO - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/455/1/1134/986779
- academic.oup.com High-redshift clumpy discs and bulges in cosmological simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/404/4/2151/1089046
- academic.oup.com Evolution of violent gravitational disc instability in galaxies: late stabilization by transition from gas to stellar dominance Opens in a new window — https://academic.oup.com/mnras/article-pdf/421/1/818/3141614/mnras0421-0818.pdf
- arxiv.org Quantifying the inside-out formation of disk galaxies at 1.5 ≤ z ≤ 3.0 - arXiv Opens in a new window — https://arxiv.org/pdf/2606.26264
- arxiv.org Rapid bulge assembly in young galaxy disks at Cosmic Dawn - arXiv Opens in a new window — https://arxiv.org/html/2510.25383v1
- academic.oup.com Scaling relations of star-forming regions: from kpc-sized clumps to HII regions Opens in a new window — https://academic.oup.com/mnras/article-pdf/422/4/3339/18604040/mnras0422-3339.pdf
- academic.oup.com High-redshift clumpy discs and bulges in cosmological simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/404/4/2151/1089046
- mpe.mpg.de The Regulation of Galaxy Growth along the Size–Mass Relation by Star Formation, as Traced by Hα in KMOS3D Galaxies at 0.7 Opens in a new window — https://www.mpe.mpg.de/~saglia/journals_pdf/wilman2020.pdf
- ntrs.nasa.gov A CANDELS–3D-HST SYNERGY: RESOLVED STAR FORMATION PATTERNS AT 0.7 <z< 1.5 Opens in a new window — https://ntrs.nasa.gov/api/citations/20140008680/downloads/20140008680.pdf
- arxiv.org Episodic Star Formation - I. Overview and Scatter of the Star-Forming Main Sequence - arXiv Opens in a new window — https://arxiv.org/html/2512.00151v3
- cambridge.org The Diversity of Assembly Histories Leading to Disc Galaxy Formation in a ΛCDM Model | Publications of the Astronomical Society of Australia Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/diversity-of-assembly-histories-leading-to-disc-galaxy-formation-in-a-cdm-model/8B46B012F92AF79CCEE975CB5B39FBE3

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

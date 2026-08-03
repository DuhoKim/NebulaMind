# Review Base 04 canonical advisory packet — Naab & Ostriker 2017

status: READY_FOR_HWAO_REVIEW
advisory_only: true
wiki_write_performed_by_tori: false
canonical_source_base_not_live_wiki_prose: true
raw_packet_sha256: 69860881137f7c919f2bc9be32f149eace280672df093870ff63abb8f54e9af0
source_registry_status: PASS
usable_sources: 44
primary_sources: 40
supporting_reviews_or_references: 4
quarantined_sources: 9

## 1. Review identity and scope map

[REV04] Naab, Thorsten & Ostriker, Jeremiah P. (2017, Annual Review of Astronomy and Astrophysics) | title=Theoretical Challenges in Galaxy Formation | DOI:10.1146/annurev-astro-081913-040019; arXiv:1612.06891; ADS:2017ARA&A..55...59N | role=review_synthesis | trust_score=0.98 | boundary=2017 synthesis centered on unresolved ISM, star formation, stellar feedback, outflows, and numerical galaxy-formation modeling.

- Shared problem: cosmological models must connect halo-scale inflow and CGM exchange to parsec/sub-parsec ISM processes they generally cannot resolve.
- ISM: supports a multiphase, turbulent, magnetized, cosmic-ray-bearing medium rather than a single effective fluid.
- Star formation: empirical density/SFR laws are useful subgrid anchors; calibration is not a first-principles derivation.
- Stellar feedback: photoheating, radiation, winds, supernovae, and nonthermal pressure act at different times and scales; no universal single-channel hierarchy was established.
- Outflows: supports mass, energy, momentum, and metal transport into fountains and the CGM; launch and recycling remain model dependent.
- Numerical methods: supports bounded comparison of thermal, kinetic, delayed-cooling, decoupled-wind, and more explicit approaches; numerical convergence is not automatically physical convergence.
- Black-hole feedback appears only as a bounded galaxy-scale ingredient. Accretion, jet, and AGN-demographic microphysics remain outside this packet.
- Post-2017/JWST/ML follow-up is outside the historical review boundary.

## 2. Established findings

[REV04-E01]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Low galaxy baryon-conversion efficiencies and substantial circumgalactic gas make inflow, outflow, and recycling central to galaxy-formation models.
- scope/boundary: The accounting requirement is robust; individual phase fluxes and recycling times are not uniquely measured.
- review basis: Introduction and Section 1.
- confidence note: High for the baryon-cycle framing.
- source keys: [REV04], [REV04-P025], [REV04-P045], [REV04-P046]
- trust_score: 0.95

[REV04-E02]
- role: established
- epistemic_type: hydrodynamic_simulation
- atomic finding: Early cooling-only simulations formed excessive central stellar mass and lost too much baryonic angular momentum, motivating strong regulation and better numerical treatment.
- scope/boundary: Severity depends on resolution, UV background, star formation, feedback, and merger history.
- review basis: Sections 2.1-2.2.
- confidence note: High as a historical simulation failure mode.
- source keys: [REV04], [REV04-P001], [REV04-P002], [REV04-P004], [REV04-P009], [REV04-P022], [REV04-P023], [REV04-P032], [REV04-P033]
- trust_score: 0.95

[REV04-E03]
- role: established
- epistemic_type: review_synthesis
- atomic finding: The ISM is multiphase and supported by interacting thermal, turbulent, magnetic, cosmic-ray, and gravitational components.
- scope/boundary: Relative pressures and phase fractions vary with galactic environment, density, height, and star-formation activity.
- review basis: Sections 1 and 3.
- confidence note: High for multiple components, moderate for their local partition.
- source keys: [REV04], [REV04-P008], [REV04-P020], [REV04-P031], [REV04-S01]
- trust_score: 0.94

[REV04-E04]
- role: established
- epistemic_type: calibration
- atomic finding: Cosmological simulations commonly encode unresolved star formation using density and timescale criteria calibrated against resolved or global gas-SFR relations.
- scope/boundary: Thresholds, eligible phase, efficiency, pressure floor, and averaging scale differ among models.
- review basis: Section 2.1.
- confidence note: High for modeling practice, moderate for physical uniqueness.
- source keys: [REV04], [REV04-P010], [REV04-P021], [REV04-P023], [REV04-P024], [REV04-P028], [REV04-P039], [REV04-P041]
- trust_score: 0.95

[REV04-E05]
- role: established
- epistemic_type: analytic_theory
- atomic finding: A supernova remnant transfers energy and momentum through free-expansion, Sedov-Taylor, shell-formation/radiative, and later momentum-dominated stages.
- scope/boundary: Ambient density, metallicity, turbulence, pre-existing bubbles, and clustering alter shell-formation scales and final momentum.
- review basis: Section 3.1.
- confidence note: High for stage structure, moderate for one universal terminal value.
- source keys: [REV04], [REV04-P007], [REV04-P012], [REV04-P018], [REV04-P026], [REV04-P030], [REV04-P044], [REV04-S02]
- trust_score: 0.96

[REV04-E06]
- role: established
- epistemic_type: hydrodynamic_simulation
- atomic finding: Depositing supernova thermal energy at insufficient resolution can radiate it away before the remnant performs the resolved mechanical work, producing numerical overcooling.
- scope/boundary: Outcome depends on gas-element mass, ambient density, injection temperature, timestep, cooling, and whether terminal momentum is explicitly supplied.
- review basis: Sections 2.2 and 3.1.
- confidence note: High.
- source keys: [REV04], [REV04-P003], [REV04-P014], [REV04-P018], [REV04-P026], [REV04-P030], [REV04-P038]
- trust_score: 0.97

[REV04-E07]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Pre-supernova photoheating, radiation, and winds can restructure stellar birth environments before supernova explosions, altering later energy and momentum coupling.
- scope/boundary: Relative channel importance depends on cloud surface density, metallicity, clustering, and resolution.
- review basis: Sections 3.2-3.3.
- confidence note: High for timing/coupling, lower for a universal hierarchy.
- source keys: [REV04], [REV04-P003], [REV04-P018], [REV04-P044], [REV04-S02]
- trust_score: 0.90

[REV04-E08]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Stellar feedback must launch or maintain galactic outflows to regulate low-mass galaxies and transport metals beyond star-forming disks.
- scope/boundary: Required regulation is robust; mass loading, velocity, phase structure, and escape fraction are galaxy- and implementation-dependent.
- review basis: Sections 1.3 and 3.
- confidence note: High for importance, moderate for quantitative scalings.
- source keys: [REV04], [REV04-P014], [REV04-P015], [REV04-P027], [REV04-P035], [REV04-S04]
- trust_score: 0.93

[REV04-E09]
- role: established
- epistemic_type: hydrodynamic_simulation
- atomic finding: Ejected gas need not escape permanently; fountain interaction with halo gas can exchange angular momentum and return fuel to disks.
- scope/boundary: Recycling depends on halo mass, launch speed, drag/mixing, cooling, and corona rotation.
- review basis: Sections 1.3 and 3.5.
- confidence note: High for recycling as a pathway, moderate for its rate.
- source keys: [REV04], [REV04-P009], [REV04-P029], [REV04-P045]
- trust_score: 0.90

[REV04-E10]
- role: established
- epistemic_type: analytic_theory
- atomic finding: Magnetic fields and cosmic rays can provide dynamically important nonthermal pressure and can change disk support and wind acceleration.
- scope/boundary: Conclusions depend on magnetic topology and uncertain cosmic-ray diffusion, streaming, losses, and coupling.
- review basis: Sections 1.1 and 3.4.
- confidence note: High for relevance, moderate for quantitative transport.
- source keys: [REV04], [REV04-P008], [REV04-P049]
- trust_score: 0.90

[REV04-E11]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Distinct subgrid feedback implementations can reproduce overlapping galaxy population statistics after calibration.
- scope/boundary: Agreement with calibrated observables is not evidence that launch physics, phase structure, or recycling are correct.
- review basis: Sections 2.2 and 3.5.
- confidence note: High.
- source keys: [REV04], [REV04-P003], [REV04-P014], [REV04-P038], [REV04-P041]
- trust_score: 0.97

[REV04-E12]
- role: established
- epistemic_type: observation
- atomic finding: Low-redshift absorption measurements reveal a substantial cool, enriched CGM around galaxies, providing a reservoir and transport benchmark for models.
- scope/boundary: Ionization corrections, metallicity, geometry, cloud sizes, and halo selection dominate mass estimates.
- review basis: Section 1.3.1.
- confidence note: High for detection and enrichment, moderate for total mass.
- source keys: [REV04], [REV04-P045]
- trust_score: 0.91

## 3. Open debates and tensions

[REV04-D01] | role=debate | topic=Control of star-formation efficiency | positions=Turbulence and gravity establish the efficiency versus early stellar feedback terminates collapse and sets the integrated value. | unresolved=Cosmological boxes did not resolve cloud formation and disruption together. | boundary=Cloud scale, density, metallicity, tracer, and averaging time. | source keys=[REV04], [REV04-P020], [REV04-P024], [REV04-P028], [REV04-P039], [REV04-S01] | trust_score=0.91
[REV04-D02] | role=debate | topic=Dominant stellar-feedback channel | positions=Supernovae provide the main long-lived mechanical budget versus radiation, photoionization, winds, and clustering conditioning the medium enough to control coupling. | unresolved=Timing and cross-channel nonlinearities were not resolved in large volumes. | boundary=Cloud surface density, metallicity, stellar population, and resolution. | source keys=[REV04], [REV04-P003], [REV04-P018], [REV04-P026], [REV04-P044], [REV04-S02] | trust_score=0.90
[REV04-D03] | role=debate | topic=Thermal versus kinetic feedback | positions=Stochastic high-temperature thermal deposition can avoid immediate losses versus kinetic/momentum injection better representing unresolved remnants and wind launch. | unresolved=Both could be calibrated, and both depend on resolution and numerical coupling. | boundary=Gas mass, temperature jump, kick prescription, hydrodynamic decoupling. | source keys=[REV04], [REV04-P014], [REV04-P026], [REV04-P030], [REV04-P038] | trust_score=0.94
[REV04-D04] | role=debate | topic=Explicit versus effective feedback | positions=Resolve individual channels and remnants versus encode their net effect through effective equations of state, delayed cooling, or calibrated winds. | unresolved=Required dynamic range remained impractical for cosmological populations. | boundary=Do not compare methods without matching resolved scale and calibration set. | source keys=[REV04], [REV04-P003], [REV04-P041], [REV04-P044] | trust_score=0.93
[REV04-D05] | role=debate | topic=Wind mass loading and recycling | positions=Strong ejective winds permanently lower efficiencies versus much outflowing material recycling through fountains and the CGM. | unresolved=Multiphase fluxes and return times were hard to observe and numerically sensitive. | boundary=Halo mass, redshift, radius, phase, velocity cut, and time window. | source keys=[REV04], [REV04-P009], [REV04-P014], [REV04-P029], [REV04-P045] | trust_score=0.91
[REV04-D06] | role=debate | topic=Cosmic-ray and magnetic support | positions=Nonthermal pressure may drive cool extended winds versus uncertain transport and losses limiting dynamical impact. | unresolved=Diffusion and streaming coefficients were poorly constrained. | boundary=Magnetic topology, ionization, losses, dimensionality, and resolution. | source keys=[REV04], [REV04-P008], [REV04-P049] | trust_score=0.88
[REV04-D07] | role=debate | topic=Physical versus numerical convergence | positions=Better resolution should converge feedback coupling versus new resolved phases changing the effective problem and requiring revised prescriptions. | unresolved=Few calculations spanned cloud-to-halo scales with fixed physics. | boundary=Convergence must specify observable, algorithm, subgrid model, and physical scale. | source keys=[REV04], [REV04-P018], [REV04-P026], [REV04-P030], [REV04-P038], [REV04-P044] | trust_score=0.96
[REV04-D08] | role=debate | topic=Calibration degeneracy | positions=Reproducing stellar masses and SFRs demonstrates effective regulation versus tuned agreement hiding incorrect mechanisms and secondary predictions. | unresolved=Multiple independent out-of-sample observables were not simultaneously matched uniquely. | boundary=Separate calibrated targets from predictions. | source keys=[REV04], [REV04-P003], [REV04-P014], [REV04-P038], [REV04-P041] | trust_score=0.97

## 4. Key measurements, model benchmarks, and calibrations

[REV04-N01] | role=calibration | metric=Core-collapse supernova energy scale | value=order 10^51 erg per event | sample/method=canonical explosion-energy budget | calibrated_or_predicted=assumed physical input | caveat=event diversity and coupling fraction | source keys=[REV04], [REV04-P012], [REV04-S02] | trust_score=0.94
[REV04-N02] | role=benchmark | metric=Terminal radial momentum per isolated supernova | value=order 2-3 x 10^5 Msun km s^-1 near n_H~1 cm^-3 | sample/method=high-resolution remnant calculations | calibrated_or_predicted=simulation/theory benchmark | caveat=density, metallicity, inhomogeneity, clustering, pre-processing | source keys=[REV04], [REV04-P018], [REV04-P026], [REV04-P030] | trust_score=0.91
[REV04-N03] | role=benchmark | metric=Shell-formation/cooling transition | value=order 10^4-10^5 yr and tens of parsecs for an isolated 10^51 erg event near n_H~1 cm^-3 | sample/method=analytic and resolved remnant models | calibrated_or_predicted=environment-dependent benchmark | caveat=not a universal injection radius/time | source keys=[REV04], [REV04-P007], [REV04-P012], [REV04-P026] | trust_score=0.88
[REV04-N04] | role=measurement | metric=Global Kennicutt-Schmidt slope | value=surface SFR approximately proportional to total-gas surface density^1.4 in the original global sample | sample/method=disk-averaged normal and starburst galaxies | calibrated_or_predicted=observational calibration | caveat=gas phase, conversion factors, scale, and regime | source keys=[REV04], [REV04-P024] | trust_score=0.93
[REV04-N05] | role=measurement | metric=Molecular-gas depletion time | value=order 2 Gyr across much of nearby normal-disk regime | sample/method=resolved nearby-galaxy gas and SFR maps | calibrated_or_predicted=observational benchmark | caveat=CO conversion, dense/starburst regimes, aperture | source keys=[REV04], [REV04-P028] | trust_score=0.90
[REV04-N06] | role=calibration | metric=Wind mass-loading factor | value=eta = mass outflow rate / SFR; no universal 2017 value | sample/method=subgrid wind models and simulations | calibrated_or_predicted=often assumed/calibrated or model-predicted | caveat=measurement radius, phase, time averaging, recycling | source keys=[REV04], [REV04-P014], [REV04-P038] | trust_score=0.94
[REV04-N07] | role=benchmark | metric=Nonthermal Galactic-disk support | value=magnetic and cosmic-ray energy densities are of comparable order to other major ISM components | sample/method=vertical hydrostatic-equilibrium accounting | calibrated_or_predicted=analytic/empirical benchmark | caveat=Milky Way locality and model assumptions | source keys=[REV04], [REV04-P008] | trust_score=0.86
[REV04-N08] | role=measurement | metric=Cool CGM baryonic reservoir | value=order 10^10-10^11 Msun for the cited low-redshift L* halo sample under adopted ionization models | sample/method=COS-Halos absorption and photoionization modeling | calibrated_or_predicted=observational inference | caveat=ionization, metallicity, geometry, cloud size, halo selection | source keys=[REV04], [REV04-P045] | trust_score=0.84

## 5. What remained unknown in 2017

[REV04-U01] | role=future | gap=First-principles emergence of galaxy-scale star-formation laws | importance=calibrated laws limit prediction in new regimes | needed=cloud-resolving radiation-MHD/chemistry linked to galaxy environments | source keys=[REV04], [REV04-P020], [REV04-P024], [REV04-P028], [REV04-P039]
[REV04-U02] | role=future | gap=Survival, mixing, and acceleration of cold gas in hot winds | importance=sets observable phase loading and recycling | needed=high-resolution multiphase MHD with conduction and tracer-forward observations | source keys=[REV04], [REV04-P029], [REV04-P045], [REV04-S04]
[REV04-U03] | role=future | gap=Hierarchy and coupling of pre-supernova feedback channels | importance=sets the density into which supernovae explode | needed=coupled radiation, winds, ionization, and resolved clustered supernovae | source keys=[REV04], [REV04-P003], [REV04-P018], [REV04-P044], [REV04-S02]
[REV04-U04] | role=future | gap=Physical mass loading and recycling scalings | importance=controls stellar masses, metallicities, and fueling | needed=phase-resolved fluxes over radius/time plus scale-bridging simulations | source keys=[REV04], [REV04-P014], [REV04-P029], [REV04-P045]
[REV04-U05] | role=future | gap=Cosmic-ray transport and magnetic coupling | importance=may change cool-wind acceleration and disk support | needed=constrained diffusion/streaming/loss models with gamma-ray and wind tests | source keys=[REV04], [REV04-P008], [REV04-P049]
[REV04-U06] | role=future | gap=Physical validation beyond tuned population statistics | importance=different implementations can match the same target | needed=same-initial-condition resolution ladders and independent gas/CGM/metal/structure predictions | source keys=[REV04], [REV04-P003], [REV04-P014], [REV04-P038], [REV04-P041]

## 6. Primary-citation harvest

The 40 rows below are primary observational, empirical, analytic, or simulation papers directly cited by Naab & Ostriker 2017. Four cited supporting reviews/references are retained separately and not counted toward the primary total. Nine raw candidates are quarantined because exact review membership or identity failed.

[REV04-P001] Abadi M. G., Navarro J. F., Steinmetz M., Eke V. R. (2003, The Astrophysical Journal) | title=Simulations of Galaxy Formation in a Λ Cold Dark Matter Universe. I. Dynamical and Photometric Properties of a Simulated Disk Galaxy | DOI:10.1086/375512; arXiv:astro-ph/0211331; ADS:2003ApJ...591..499A | role=hydrodynamic_simulation | review_locator=Section 2.2 | Early demonstration of the angular momentum and overcooling problem in simulated disks.
[REV04-P002] Abadi M. G., Navarro J. F., Steinmetz M., Eke V. R. (2003, The Astrophysical Journal) | title=Simulations of Galaxy Formation in a Λ Cold Dark Matter Universe. II. The Fine Structure of Simulated Galactic Disks | DOI:10.1086/378316; arXiv:astro-ph/0212282; ADS:2003ApJ...597...21A | role=hydrodynamic_simulation | review_locator=Section 2.2 | Analyzed the fine kinematic structure and the difficulty of preventing early collapse of low angular momentum baryons.
[REV04-P003] Agertz O., Kravtsov A. V., Leitner S. N., Gnedin N. Y. (2013, The Astrophysical Journal) | title=Toward a Complete Accounting of Energy and Momentum from Stellar Feedback in Galaxy Formation Simulations | DOI:10.1088/0004-637X/770/1/25; arXiv:1210.4957; ADS:2013ApJ...770...25A | role=hydrodynamic_simulation | review_locator=Section 2.2.1 | Implementation of momentum and energy stellar feedback in isolated and cosmological contexts.
[REV04-P004] Balogh M. L., Pearce F. R., Bower R. G., Kay S. T. (2001, Monthly Notices of the Royal Astronomical Society) | title=Revisiting the cosmic cooling crisis | DOI:10.1111/j.1365-2966.2001.04667.x; arXiv:astro-ph/0104041; ADS:2001MNRAS.326.1228B | role=hydrodynamic_simulation | review_locator=Section 2.2 | Confirmed the overcooling problem in cosmological simulations where excessive early gas condensation occurs.
[REV04-P006] Binney J. (1977, The Astrophysical Journal) | title=The physics of dissipational galaxy formation. | DOI:10.1086/155378; arXiv:none; ADS:1977ApJ...215..483B | role=analytic_theory | review_locator=Section 2.1 | Foundational analytic theory establishing gas cooling and dissipation as necessities for galactic structure.
[REV04-P007] Blondin J. M., Wright E. B., Borkowski K. J., Reynolds S. P. (1998, The Astrophysical Journal) | title=Transition to the Radiative Phase in Supernova Remnants | DOI:10.1086/305708; arXiv:none; ADS:1998ApJ...500..342B | role=analytic_theory | review_locator=Section 3.1 | Detailed the thermodynamic transition of supernova remnants into the radiative snowplow phase.
[REV04-P008] Boulares A., Cox D. P. (1990, The Astrophysical Journal) | title=Galactic Hydrostatic Equilibrium with Magnetic Tension and Cosmic-Ray Diffusion | DOI:10.1086/169509; arXiv:none; ADS:1990ApJ...365..544B | role=analytic_theory | review_locator=Section 1.1 | Analytic hydrostatic-equilibrium accounting for magnetic and cosmic-ray support in the Galactic disk; not a direct observational measurement.
[REV04-P009] Brook C. B., et al. (2011, Monthly Notices of the Royal Astronomical Society) | title=Hierarchical formation of bulgeless galaxies: why outflows have low angular momentum | DOI:10.1111/j.1365-2966.2011.18545.x; arXiv:1010.1004; ADS:2011MNRAS.415.1051B | role=hydrodynamic_simulation | review_locator=Section 2.2 | Simulation result that preferentially ejected low-angular-momentum gas can support bulgeless disks; implementation and halo-history dependent.
[REV04-P010] Cen R., Ostriker J. P. (1992, The Astrophysical Journal Letters) | title=Galaxy Formation and Physical Bias | DOI:10.1086/186620; arXiv:none; ADS:1992ApJ...399L.113C | role=hydrodynamic_simulation | review_locator=Section 2.1 | Introduced local timescales tied to dynamical and cooling times for sub-grid star formation.
[REV04-P012] Cioffi D. F., McKee C. F., Bertschinger E. (1988, The Astrophysical Journal) | title=Dynamics of Radiative Supernova Remnants | DOI:10.1086/166834; arXiv:none; ADS:1988ApJ...334..252C | role=analytic_theory | review_locator=Section 3.1 | Provided the classic analytic framework for the momentum and energy scaling of evolving supernova remnants.
[REV04-P014] Dalla Vecchia C., Schaye J. (2008, Monthly Notices of the Royal Astronomical Society) | title=Simulating galactic outflows with kinetic supernova feedback | DOI:10.1111/j.1365-2966.2008.13322.x; arXiv:0801.2770; ADS:2008MNRAS.387.1431D | role=hydrodynamic_simulation | review_locator=Section 2.2.1 | Kinetic supernova-feedback outflow implementation; wind behavior depends on launch parameters and hydrodynamic coupling.
[REV04-P015] Dekel A., Silk J. (1986, The Astrophysical Journal) | title=The Origin of Dwarf Galaxies, Cold Dark Matter, and Biased Galaxy Formation | DOI:10.1086/164050; arXiv:none; ADS:1986ApJ...303...39D | role=analytic_theory | review_locator=Section 3.1 | Early theoretical realization that supernova feedback is required to prevent excessive cooling in dwarf halos.
[REV04-P017] Fall S. M., Efstathiou G. (1980, Monthly Notices of the Royal Astronomical Society) | title=Formation and rotation of disc galaxies with haloes. | DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | role=analytic_theory | review_locator=Section 2.2 | Established the basic model of disk formation via tidal torques and angular momentum conservation during cooling.
[REV04-P018] Haid S., Walch S., Naab T., Seifried D., Mackey J., Gatto A. (2016, Monthly Notices of the Royal Astronomical Society) | title=Supernova blast waves in wind-blown bubbles, turbulent, and power-law ambient media | DOI:10.1093/mnras/stw1082; arXiv:1604.04395; ADS:2016MNRAS.460.2962H | role=hydrodynamic_simulation | review_locator=Section 3.1 | Controlled supernova-remnant calculations across wind-blown, turbulent, and power-law media; ambient structure sets momentum evolution.
[REV04-P020] Hennebelle P., Iffrig O. (2014, Astronomy and Astrophysics) | title=Simulations of magnetized multiphase galactic disc regulated by supernovae explosions | DOI:10.1051/0004-6361/201423392; arXiv:1405.7819; ADS:2014A&A...570A..81H | role=hydrodynamic_simulation | review_locator=Section 2.1 | Magnetized multiphase galactic-disc simulation regulated by supernova explosions; numerical and chemistry assumptions apply.
[REV04-P021] Katz N. (1992, The Astrophysical Journal) | title=Dissipational Galaxy Formation. II. Effects of Star Formation | DOI:10.1086/171366; arXiv:none; ADS:1992ApJ...391..502K | role=hydrodynamic_simulation | review_locator=Section 2.1 | Original formulation of sub-resolution SF density-timescale criteria for SPH modeling.
[REV04-P022] Katz N., Gunn J. E. (1991, The Astrophysical Journal) | title=Dissipational Galaxy Formation. I. Effects of Gasdynamics | DOI:10.1086/170367; arXiv:none; ADS:1991ApJ...377..365K | role=hydrodynamic_simulation | review_locator=Section 2.2 | Early documentation of angular momentum crises in simulated dissipative gas clouds.
[REV04-P023] Katz N., Weinberg D. H., Hernquist L. (1996, The Astrophysical Journal Supplement Series) | title=Cosmological Simulations with TreeSPH | DOI:10.1086/192305; arXiv:astro-ph/9509107; ADS:1996ApJS..105...19K | role=hydrodynamic_simulation | review_locator=Section 2.2 | Highlighted the severe tendency for cosmological simulations to overproduce central bulges.
[REV04-P024] Kennicutt R. C., Jr (1998, The Astrophysical Journal) | title=The Global Schmidt Law in Star-forming Galaxies | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=observation | review_locator=Section 2.1 | Defined the global relation used essentially by all models to calibrate sub-grid star formation rates.
[REV04-P025] Kereš D., Katz N., Weinberg D. H., Davé R. (2005, Monthly Notices of the Royal Astronomical Society) | title=How do galaxies get their gas? | DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0407095; ADS:2005MNRAS.363....2K | role=hydrodynamic_simulation | review_locator=Section 2.2 | Evaluated the thermodynamics and morphological consequences of cold versus hot accretion flows.
[REV04-P026] Kim C.-G., Ostriker E. C. (2015, The Astrophysical Journal) | title=Momentum Injection by Supernovae in the Interstellar Medium | DOI:10.1088/0004-637X/802/2/99; arXiv:1410.1537; ADS:2015ApJ...802...99K | role=hydrodynamic_simulation | review_locator=Section 3.1 | Precise limits on momentum scaling derived from ultra-high resolution SNR expansion experiments.
[REV04-P027] Larson R. B. (1974, Monthly Notices of the Royal Astronomical Society) | title=Effects of supernovae on the early evolution of galaxies | DOI:10.1093/mnras/169.2.229; arXiv:none; ADS:1974MNRAS.169..229L | role=analytic_theory | review_locator=Section 3.1 | Foundational theory linking stellar feedback to the macroscopic evolution and element retention of young galaxies.
[REV04-P028] Leroy A. K., et al. (2008, The Astronomical Journal) | title=The Star Formation Efficiency in Nearby Galaxies: Measuring Where Gas Forms Stars Effectively | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=observation | review_locator=Section 2.1 | Spatially resolved observations establishing the profound inefficiency of molecular gas converting to stars.
[REV04-P029] Marinacci F., et al. (2011, Monthly Notices of the Royal Astronomical Society) | title=Galactic fountains and the rotation of disc-galaxy coronae | DOI:10.1111/j.1365-2966.2011.18810.x; arXiv:1103.5358; ADS:2011MNRAS.415.1534M | role=hydrodynamic_simulation | review_locator=Section 2.2 | Galactic-fountain interaction with rotating coronae; constrains fountain/corona angular-momentum exchange rather than generic nonlinear torques.
[REV04-P030] Martizzi D., Faucher-Giguère C.-A., Quataert E. (2015, Monthly Notices of the Royal Astronomical Society) | title=Supernova feedback in an inhomogeneous interstellar medium | DOI:10.1093/mnras/stv562; arXiv:1409.4425; ADS:2015MNRAS.450..504M | role=hydrodynamic_simulation | review_locator=Section 3.1 | Quantitative formulas for momentum and thermal energy injected into explicitly inhomogeneous, multiphase media.
[REV04-P031] McKee C. F., Ostriker J. P. (1977, The Astrophysical Journal) | title=A theory of the interstellar medium: three components regulated by supernova explosions in an inhomogeneous substrate. | DOI:10.1086/155667; arXiv:none; ADS:1977ApJ...218..148M | role=analytic_theory | review_locator=Section 3.1 | Established the theoretical blueprint for a three-phase ISM driven uniquely by successive SN explosions.
[REV04-P032] Navarro J. F., Benz W. (1991, The Astrophysical Journal) | title=Dynamics of Cooling Gas in Galactic Dark Halos | DOI:10.1086/170590; arXiv:none; ADS:1991ApJ...380..320N | role=hydrodynamic_simulation | review_locator=Section 2.2 | Linked collisionless dark matter halos with highly dissipative, overcooling gas inflows.
[REV04-P033] Navarro J. F., Steinmetz M. (1997, The Astrophysical Journal) | title=The Effects of a Photoionizing Ultraviolet Background on the Formation of Disk Galaxies | DOI:10.1086/303763; arXiv:astro-ph/9605043; ADS:1997ApJ...478...13N | role=hydrodynamic_simulation | review_locator=Section 2.2 | Simulation of photoionizing ultraviolet-background effects on disk-galaxy formation; not a generic no-feedback angular-momentum experiment.
[REV04-P034] Peebles P. J. E. (1969, The Astrophysical Journal) | title=Origin of the Angular Momentum of Galaxies | DOI:10.1086/149876; arXiv:none; ADS:1969ApJ...155..393P | role=analytic_theory | review_locator=Section 1.3.1 | Classical analytical determination of initial galaxy spin acquired via external large-scale tidal forces.
[REV04-P035] Pettini M., et al. (2001, The Astrophysical Journal) | title=The Rest-Frame Optical Spectra of Lyman Break Galaxies: Star Formation, Extinction, Abundances, and Kinematics | DOI:10.1086/321403; arXiv:astro-ph/0102456; ADS:2001ApJ...554..981P | role=observation | review_locator=Section 1.3.1 | Early spectroscopic confirmation of massive, high-velocity galactic winds occurring at cosmic noon.
[REV04-P036] Pontzen A., Governato F. (2012, Monthly Notices of the Royal Astronomical Society) | title=How supernova feedback turns dark matter cusps into cores | DOI:10.1111/j.1365-2966.2012.20571.x; arXiv:1106.0499; ADS:2012MNRAS.421.3464P | role=hydrodynamic_simulation | review_locator=Section 1.1 | Showed how rapid, baryon-driven outflows dramatically alter the inner gravitational profiles of small halos.
[REV04-P037] Rees M. J., Ostriker J. P. (1977, Monthly Notices of the Royal Astronomical Society) | title=Cooling, dynamics and fragmentation of massive gas clouds: clues to the masses and radii of galaxies and clusters. | DOI:10.1093/mnras/179.4.541; arXiv:none; ADS:1977MNRAS.179..541R | role=analytic_theory | review_locator=Section 2.2 | Established the physical boundaries determining where dark matter halos successfully trap cooling gas.
[REV04-P038] Schaye J., et al. (2015, Monthly Notices of the Royal Astronomical Society) | title=The EAGLE project: simulating the evolution and assembly of galaxies and their environments | DOI:10.1093/mnras/stu2058; arXiv:1407.7040; ADS:2015MNRAS.446..521S | role=hydrodynamic_simulation | review_locator=Section 3.5 | Large-scale cosmological simulation achieving realistic stellar mass properties via calibrated stochastic thermal heating.
[REV04-P039] Schmidt M. (1959, The Astrophysical Journal) | title=The Rate of Star Formation. | DOI:10.1086/146614; arXiv:none; ADS:1959ApJ...129..243S | role=analytic_theory | review_locator=Section 2.1 | Formulated the fundamental empirical power-law linking star-formation rates to locally available gas density.
[REV04-P040] Silk J. (1977, The Astrophysical Journal) | title=On the fragmentation of cosmic gas clouds. I. The formation of galaxies and the first generation of stars. | DOI:10.1086/154972; arXiv:none; ADS:1977ApJ...211..638S | role=analytic_theory | review_locator=Section 2.2 | Foundational criteria establishing the upper limits on cooling rates leading to star formation within galactic halos.
[REV04-P041] Springel V., Hernquist L. (2003, Monthly Notices of the Royal Astronomical Society) | title=Cosmological smoothed particle hydrodynamics simulations: a hybrid multiphase model for star formation | DOI:10.1046/j.1365-8711.2003.06206.x; arXiv:astro-ph/0206393; ADS:2003MNRAS.339..289S | role=semi_analytic_model | review_locator=Section 2.1 | Formulation of the widely used sub-grid multiphase effective equation of state balancing star formation and feedback.
[REV04-P044] Walch S., Naab T. (2015, Monthly Notices of the Royal Astronomical Society) | title=The SILCC (SImulating the LifeCycle of molecular Clouds) project - I. Chemical evolution of the supernova-driven ISM | DOI:10.1093/mnras/stv1975; arXiv:1412.2749; ADS:2015MNRAS.454..238W | role=hydrodynamic_simulation | review_locator=Section 3.1 | SILCC chemical evolution of a supernova-driven ISM; do not overextend to a universal clustered-versus-isolated momentum validation.
[REV04-P045] Werk J. K., et al. (2014, The Astrophysical Journal) | title=The COS-Halos Survey: Physical Conditions and Baryonic Mass in the Low-redshift Circumgalactic Medium | DOI:10.1088/0004-637X/792/1/8; arXiv:1403.0947; ADS:2014ApJ...792....8W | role=observation | review_locator=Section 1.3.1 | Quantified cool gas densities and heavy element kinematics within the extended halos of massive star-forming galaxies.
[REV04-P046] White S. D. M., Rees M. J. (1978, Monthly Notices of the Royal Astronomical Society) | title=Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering. | DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | role=analytic_theory | review_locator=Section 2.2 | The seminal framework for two-stage cosmological formation (merging collisionless dark matter followed by dissipative gas cooling).
[REV04-P049] Salem M., Bryan G. L. (2014, Monthly Notices of the Royal Astronomical Society) | title=Cosmic ray driven outflows in global galaxy disc models | DOI:10.1093/mnras/stt2121; arXiv:1307.6215; ADS:2014MNRAS.437.3312S | role=hydrodynamic_simulation | review_locator=Section 3.4 | Simulated the efficiency of cosmic-ray transport in accelerating cold gas out of the galactic potential well.

### Supporting cited reviews or references — not counted as primary

[REV04-P016] Draine B. T. (2011, Physics of the Interstellar and Intergalactic Medium) | title=Physics of the Interstellar and Intergalactic Medium | DOI:none; arXiv:none; ADS:2011piim.book.....D | role=supporting_reference | review_locator=Section 3.1 | Textbook synthesis of ISM and intergalactic-medium physics; supporting reference, not a primary paper.
[REV04-S01] Elmegreen B. G., Scalo J. (2004, Annual Review of Astronomy and Astrophysics) | title=Interstellar Turbulence I: Observations and Processes | DOI:10.1146/annurev.astro.41.011802.094859; arXiv:astro-ph/0404451; ADS:2004ARA&A..42..211E | role=review_synthesis | review_locator=Section 3.1 | Synthesis of ISM turbulence phenomena.
[REV04-S02] Janka H.-T. (2012, Annual Review of Nuclear and Particle Science) | title=Explosion Mechanisms of Core-Collapse Supernovae | DOI:10.1146/annurev-nucl-102711-094901; arXiv:1206.2503; ADS:2012ARNPS..62..407J | role=review_synthesis | review_locator=Section 3.1 | Reference data for supernova explosion thermodynamics.
[REV04-S04] Veilleux S., Cecil G., Bland-Hawthorn J. (2005, Annual Review of Astronomy and Astrophysics) | title=Galactic Winds | DOI:10.1146/annurev.astro.43.072103.150610; arXiv:astro-ph/0504435; ADS:2005ARA&A..43..769V | role=review_synthesis | review_locator=Section 1.3.1 | Benchmarked the properties and ubiquity of galactic winds.

## 7. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | raw REV04-P001 tuple title=Simulations of Galaxy Formation in a Lambda Cold Dark Matter Universe. I. Dynamical and Photometric Properties of a Simulated Disk Galaxy; DOI:10.1086/375512; arXiv:astro-ph/0211331; ADS:2003ApJ...591..499A | cross-wired composite identity | authoritative tuple is title=Simulations of Galaxy Formation in a Λ Cold Dark Matter Universe. I. Dynamical and Photometric Properties of a Simulated Disk Galaxy; DOI:10.1086/375512; arXiv:astro-ph/0211331; ADS:2003ApJ...591..499A
UNCITED_NOT_USABLE | raw REV04-P002 tuple title=Simulations of Galaxy Formation in a Lambda Cold Dark Matter Universe. II. The Fine Structure of Simulated Galactic Disks; DOI:10.1086/378316; arXiv:astro-ph/0211383; ADS:2003ApJ...597...21A | cross-wired composite identity | authoritative tuple is title=Simulations of Galaxy Formation in a Λ Cold Dark Matter Universe. II. The Fine Structure of Simulated Galactic Disks; DOI:10.1086/378316; arXiv:astro-ph/0212282; ADS:2003ApJ...597...21A
UNCITED_NOT_USABLE | raw REV04-P003 tuple title=Toward a Complete Accounting of Energy and Momentum from Stellar Feedback in Galaxy Formation Simulations; DOI:10.1088/0004-637X/770/1/25; arXiv:1208.2741; ADS:2013ApJ...770...25A | cross-wired composite identity | authoritative tuple is title=Toward a Complete Accounting of Energy and Momentum from Stellar Feedback in Galaxy Formation Simulations; DOI:10.1088/0004-637X/770/1/25; arXiv:1210.4957; ADS:2013ApJ...770...25A
UNCITED_NOT_USABLE | raw REV04-P004 tuple title=Revisiting the overcooling crisis in semi-analytical models of galaxy formation; DOI:10.1046/j.1365-8711.2001.04652.x; arXiv:astro-ph/0104140; ADS:2001MNRAS.326.1228B | cross-wired composite identity | authoritative tuple is title=Revisiting the cosmic cooling crisis; DOI:10.1111/j.1365-2966.2001.04667.x; arXiv:astro-ph/0104041; ADS:2001MNRAS.326.1228B
UNCITED_NOT_USABLE | raw REV04-P006 tuple title=The physics of dissipational galaxy formation; DOI:10.1086/155386; arXiv:none; ADS:1977ApJ...215..483B | cross-wired composite identity | authoritative tuple is title=The physics of dissipational galaxy formation.; DOI:10.1086/155378; arXiv:none; ADS:1977ApJ...215..483B
UNCITED_NOT_USABLE | raw REV04-P007 tuple title=Transition to the Radiative Phase in Supernova Remnants; DOI:10.1086/305708; arXiv:astro-ph/9802081; ADS:1998ApJ...500..342B | cross-wired composite identity | authoritative tuple is title=Transition to the Radiative Phase in Supernova Remnants; DOI:10.1086/305708; arXiv:none; ADS:1998ApJ...500..342B
UNCITED_NOT_USABLE | raw REV04-P008 tuple title=Galactic hydrostatic equilibrium with magnetic tension and cosmic-ray diffusion; DOI:10.1086/169466; arXiv:none; ADS:1990ApJ...365..544B | cross-wired composite identity | authoritative tuple is title=Galactic Hydrostatic Equilibrium with Magnetic Tension and Cosmic-Ray Diffusion; DOI:10.1086/169509; arXiv:none; ADS:1990ApJ...365..544B
UNCITED_NOT_USABLE | raw REV04-P009 tuple title=Hierarchical formation of bulgeless galaxies - I. The roles of merging and feedback; DOI:10.1111/j.1365-2966.2011.18731.x; arXiv:1010.0003; ADS:2011MNRAS.415.1051B | cross-wired composite identity | authoritative tuple is title=Hierarchical formation of bulgeless galaxies: why outflows have low angular momentum; DOI:10.1111/j.1365-2966.2011.18545.x; arXiv:1010.1004; ADS:2011MNRAS.415.1051B
UNCITED_NOT_USABLE | raw REV04-P010 tuple title=Galaxy formation and physical bias; DOI:10.1086/186596; arXiv:none; ADS:1992ApJ...399L.113C | cross-wired composite identity | authoritative tuple is title=Galaxy Formation and Physical Bias; DOI:10.1086/186620; arXiv:none; ADS:1992ApJ...399L.113C
UNCITED_NOT_USABLE | raw REV04-P014 tuple title=Simulating galactic winds in the cold dark matter cosmology; DOI:10.1111/j.1365-2966.2008.13244.x; arXiv:0801.2770; ADS:2008MNRAS.387.1431D | cross-wired composite identity | authoritative tuple is title=Simulating galactic outflows with kinetic supernova feedback; DOI:10.1111/j.1365-2966.2008.13322.x; arXiv:0801.2770; ADS:2008MNRAS.387.1431D
UNCITED_NOT_USABLE | raw REV04-P017 tuple title=Formation and rotation of disc galaxies with haloes; DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | cross-wired composite identity | authoritative tuple is title=Formation and rotation of disc galaxies with haloes.; DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F
UNCITED_NOT_USABLE | raw REV04-P018 tuple title=Supernova blast waves in wind-blown bubbles, turbulent, and power-law ambient media; DOI:10.1093/mnras/stw1051; arXiv:1601.03055; ADS:2016MNRAS.460.2962H | cross-wired composite identity | authoritative tuple is title=Supernova blast waves in wind-blown bubbles, turbulent, and power-law ambient media; DOI:10.1093/mnras/stw1082; arXiv:1604.04395; ADS:2016MNRAS.460.2962H
UNCITED_NOT_USABLE | raw REV04-P020 tuple title=Simulations of magnetized multiphase galactic discs - I. Properties of the cold, atomic and hot gas; DOI:10.1051/0004-6361/201323334; arXiv:1405.7836; ADS:2014A&A...570A..81H | cross-wired composite identity | authoritative tuple is title=Simulations of magnetized multiphase galactic disc regulated by supernovae explosions; DOI:10.1051/0004-6361/201423392; arXiv:1405.7819; ADS:2014A&A...570A..81H
UNCITED_NOT_USABLE | raw REV04-P023 tuple title=Cosmological Simulations with TreeSPH; DOI:10.1086/192310; arXiv:astro-ph/9509107; ADS:1996ApJS..105...19K | cross-wired composite identity | authoritative tuple is title=Cosmological Simulations with TreeSPH; DOI:10.1086/192305; arXiv:astro-ph/9509107; ADS:1996ApJS..105...19K
UNCITED_NOT_USABLE | raw REV04-P026 tuple title=Momentum Injection by Supernovae in the Interstellar Medium; DOI:10.1088/0004-637X/802/2/99; arXiv:1501.03150; ADS:2015ApJ...802...99K | cross-wired composite identity | authoritative tuple is title=Momentum Injection by Supernovae in the Interstellar Medium; DOI:10.1088/0004-637X/802/2/99; arXiv:1410.1537; ADS:2015ApJ...802...99K
UNCITED_NOT_USABLE | raw REV04-P029 tuple title=Non-linear gravitational torques and mixing; DOI:none; arXiv:none; ADS:2011MNRAS.415.1534M | cross-wired composite identity | authoritative tuple is title=Galactic fountains and the rotation of disc-galaxy coronae; DOI:10.1111/j.1365-2966.2011.18810.x; arXiv:1103.5358; ADS:2011MNRAS.415.1534M
UNCITED_NOT_USABLE | raw REV04-P031 tuple title=A theory of the interstellar medium - Three components regulated by supernova explosions in an inhomogeneous substrate; DOI:10.1086/155692; arXiv:none; ADS:1977ApJ...218..148M | cross-wired composite identity | authoritative tuple is title=A theory of the interstellar medium: three components regulated by supernova explosions in an inhomogeneous substrate.; DOI:10.1086/155667; arXiv:none; ADS:1977ApJ...218..148M
UNCITED_NOT_USABLE | raw REV04-P032 tuple title=Dynamics of cooling gas in galactic dark halos; DOI:10.1086/170569; arXiv:none; ADS:1991ApJ...380..320N | cross-wired composite identity | authoritative tuple is title=Dynamics of Cooling Gas in Galactic Dark Halos; DOI:10.1086/170590; arXiv:none; ADS:1991ApJ...380..320N
UNCITED_NOT_USABLE | raw REV04-P033 tuple title=The Effects of a Cosmological Constant on Disk Galaxy Formation; DOI:10.1086/303763; arXiv:astro-ph/9605043; ADS:1997ApJ...478...13N | cross-wired composite identity | authoritative tuple is title=The Effects of a Photoionizing Ultraviolet Background on the Formation of Disk Galaxies; DOI:10.1086/303763; arXiv:astro-ph/9605043; ADS:1997ApJ...478...13N
UNCITED_NOT_USABLE | raw REV04-P034 tuple title=Origin of the Angular Momentum of Galaxies; DOI:10.1086/149911; arXiv:none; ADS:1969ApJ...155..393P | cross-wired composite identity | authoritative tuple is title=Origin of the Angular Momentum of Galaxies; DOI:10.1086/149876; arXiv:none; ADS:1969ApJ...155..393P
UNCITED_NOT_USABLE | raw REV04-P035 tuple title=The Rest-Frame Optical Spectra of Lyman Break Galaxies: Star Formation, Extinction, Abundances, and Kinematics; DOI:10.1086/321356; arXiv:astro-ph/0102456; ADS:2001ApJ...554..981P | cross-wired composite identity | authoritative tuple is title=The Rest-Frame Optical Spectra of Lyman Break Galaxies: Star Formation, Extinction, Abundances, and Kinematics; DOI:10.1086/321403; arXiv:astro-ph/0102456; ADS:2001ApJ...554..981P
UNCITED_NOT_USABLE | raw REV04-P037 tuple title=Cooling, dynamics and fragmentation of massive gas clouds: clues to the masses and radii of galaxies and clusters; DOI:10.1093/mnras/179.4.541; arXiv:none; ADS:1977MNRAS.179..541R | cross-wired composite identity | authoritative tuple is title=Cooling, dynamics and fragmentation of massive gas clouds: clues to the masses and radii of galaxies and clusters.; DOI:10.1093/mnras/179.4.541; arXiv:none; ADS:1977MNRAS.179..541R
UNCITED_NOT_USABLE | raw REV04-P040 tuple title=On the fragmentation of cosmic gas clouds. I - The formation of galaxies and the first generation of stars; DOI:10.1086/155066; arXiv:none; ADS:1977ApJ...211..638S | cross-wired composite identity | authoritative tuple is title=On the fragmentation of cosmic gas clouds. I. The formation of galaxies and the first generation of stars.; DOI:10.1086/154972; arXiv:none; ADS:1977ApJ...211..638S
UNCITED_NOT_USABLE | raw REV04-P046 tuple title=Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering; DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | cross-wired composite identity | authoritative tuple is title=Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering.; DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W
UNCITED_NOT_USABLE | raw REV04-P011 tuple title=The radio and X-ray emission from type II supernovae; DOI:10.1086/160167; arXiv:none; ADS:1982ApJ...259..302C | cross-wired composite identity | authoritative tuple is title=The radio and X-ray emission from type II supernovae.; DOI:10.1086/160167; arXiv:none; ADS:1982ApJ...259..302C
UNCITED_NOT_USABLE | raw REV04-P013 tuple title=The Angular Momentum Problem in Cosmological Simulations of Disk Galaxy Formation; DOI:10.1086/422631; arXiv:astro-ph/0311283; ADS:2004ApJ...612..628D | cross-wired composite identity | authoritative tuple is title=Cold Dark Matter's Small-Scale Crisis Grows Up; DOI:10.1086/422794; arXiv:astro-ph/0309735; ADS:2004ApJ...612..628D
UNCITED_NOT_USABLE | raw REV04-P042 tuple title=The Large, Oxygen-Rich Halos of Star-Forming Galaxies Are a Major Reservoir of Galactic Metals; DOI:10.1126/science.1209840; arXiv:1111.3970; ADS:2011Sci...334..948T | cross-wired composite identity | authoritative tuple is title=The Large, Oxygen-Rich Halos of Star-Forming Galaxies Are a Major Reservoir of Galactic Metals; DOI:10.1126/science.1209840; arXiv:1111.3980; ADS:2011Sci...334..948T
UNCITED_NOT_USABLE | raw REV04-P048 tuple title=Simulating the Formation of Molecular Clouds. I. Slow Formation by Gravity and Turbulence; DOI:10.1086/512238; arXiv:astro-ph/0605120; ADS:2007ApJS..169..239G | cross-wired composite identity | authoritative tuple is title=Simulating the Formation of Molecular Clouds. I. Slow Formation by Gravitational Collapse from Static Initial Conditions; DOI:10.1086/512238; arXiv:astro-ph/0605120; ADS:2007ApJS..169..239G
UNCITED_NOT_USABLE | REV04-P005 Bernardi M., Shankar F., Hyde J. B., Mei S., Marulli F., Sheth R. K. (2010) title=Galaxy luminosities, stellar masses, sizes, velocity dispersions as a function of morphological type | ADS:2010MNRAS.404.2087B | Exact ADS bibcode is absent from the authoritative NED review bibliography and the corrected DOI is absent from the review's structured Crossref references; physically valid candidate is not usable as review-cited.
UNCITED_NOT_USABLE | REV04-P011 Chevalier A. W. (1982) title=The radio and X-ray emission from type II supernovae. | ADS:1982ApJ...259..302C | Exact ADS bibcode is absent from the authoritative NED review bibliography and the corrected DOI is absent from the review's structured Crossref references; physically valid candidate is not usable as review-cited.
UNCITED_NOT_USABLE | REV04-P013 D'Onghia E., Burkert A. (2004) title=Cold Dark Matter's Small-Scale Crisis Grows Up | ADS:2004ApJ...612..628D | Exact ADS bibcode is absent from the authoritative NED review bibliography and the corrected DOI is absent from the review's structured Crossref references; physically valid candidate is not usable as review-cited.
UNCITED_NOT_USABLE | REV04-P019 Heckman T. M. (2000) title=Galactic Superwinds at Low and High Redshift | ADS:2000msc..conf..299H | Supplied conference bibcode does not resolve to a public ADS abstract and is absent from the review bibliography; identity and review membership are unresolved.
UNCITED_NOT_USABLE | REV04-P042 Tumlinson J., et al. (2011) title=The Large, Oxygen-Rich Halos of Star-Forming Galaxies Are a Major Reservoir of Galactic Metals | ADS:2011Sci...334..948T | Exact ADS bibcode is absent from the authoritative NED review bibliography and the corrected DOI is absent from the review's structured Crossref references; physically valid candidate is not usable as review-cited.
UNCITED_NOT_USABLE | REV04-P043 Vogelsberger M., et al. (2014) title=Properties of galaxies reproduced by a hydrodynamic simulation | ADS:2014Natur.509..177V | Exact ADS bibcode is absent from the authoritative NED review bibliography and the corrected DOI is absent from the review's structured Crossref references; physically valid candidate is not usable as review-cited.
UNCITED_NOT_USABLE | REV04-P047 Krumholz M. R., McKee C. F. (2005) title=A General Theory of Turbulence-regulated Star Formation, from Spirals to Ultraluminous Infrared Galaxies | ADS:2005ApJ...630..250K | Exact ADS bibcode is absent from the authoritative NED review bibliography and the corrected DOI is absent from the review's structured Crossref references; physically valid candidate is not usable as review-cited.
UNCITED_NOT_USABLE | REV04-P048 Glover S. C. O., Mac Low M.-M. (2007) title=Simulating the Formation of Molecular Clouds. I. Slow Formation by Gravitational Collapse from Static Initial Conditions | ADS:2007ApJS..169..239G | Exact ADS bibcode is absent from the authoritative NED review bibliography and the corrected DOI is absent from the review's structured Crossref references; physically valid candidate is not usable as review-cited.
UNCITED_NOT_USABLE | REV04-S03 Mac Low M.-M., Klessen R. S. (2004) title=Control of star formation by supersonic turbulence | ADS:2004RvMP...76..125M | Exact ADS bibcode is absent from the authoritative NED review bibliography and the corrected DOI is absent from the review's structured Crossref references; physically valid candidate is not usable as review-cited.
UNCITED_NOT_USABLE | numerical convergence proves physical correctness | overbroad claim | resolved scales and subgrid problem change with resolution
UNCITED_NOT_USABLE | matching one tuned galaxy statistic validates a feedback mechanism | calibration circularity | multiple implementations can match overlapping targets
UNCITED_NOT_USABLE | one feedback channel dominates universally | overbroad claim | hierarchy varies with environment, time, metallicity, and scale
UNCITED_NOT_USABLE | subgrid prescriptions are first-principles predictions | category error | they approximate unresolved processes
UNCITED_NOT_USABLE | one terminal supernova momentum applies to every event | overbroad claim | ambient medium, clustering, and pre-processing alter it
UNCITED_NOT_USABLE | all outflowing gas permanently escapes | unsupported claim | fountains and recycling are central alternatives
UNCITED_NOT_USABLE | post-2017/JWST/ML source anchors captured during browsing | outside date and not review-cited | excluded
UNCITED_NOT_USABLE | accretion-disk, jet, black-hole demographic, or AGN-only claim | outside non-AGN scope | only bounded galaxy-scale regulation context is allowed

## 8. Review and source identity ledger

[REV04] | Naab & Ostriker (2017, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev-astro-081913-040019; arXiv:1612.06891; ADS:2017ARA&A..55...59N | role=review | bounded 2017 theoretical-challenges synthesis
[REV04-P001] | Abadi M. G., Navarro J. F., Steinmetz M., Eke V. R. (2003, The Astrophysical Journal) | DOI:10.1086/375512; arXiv:astro-ph/0211331; ADS:2003ApJ...591..499A | role=hydrodynamic_simulation | Early demonstration of the angular momentum and overcooling problem in simulated disks.
[REV04-P002] | Abadi M. G., Navarro J. F., Steinmetz M., Eke V. R. (2003, The Astrophysical Journal) | DOI:10.1086/378316; arXiv:astro-ph/0212282; ADS:2003ApJ...597...21A | role=hydrodynamic_simulation | Analyzed the fine kinematic structure and the difficulty of preventing early collapse of low angular momentum baryons.
[REV04-P003] | Agertz O., Kravtsov A. V., Leitner S. N., Gnedin N. Y. (2013, The Astrophysical Journal) | DOI:10.1088/0004-637X/770/1/25; arXiv:1210.4957; ADS:2013ApJ...770...25A | role=hydrodynamic_simulation | Implementation of momentum and energy stellar feedback in isolated and cosmological contexts.
[REV04-P004] | Balogh M. L., Pearce F. R., Bower R. G., Kay S. T. (2001, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2001.04667.x; arXiv:astro-ph/0104041; ADS:2001MNRAS.326.1228B | role=hydrodynamic_simulation | Confirmed the overcooling problem in cosmological simulations where excessive early gas condensation occurs.
[REV04-P006] | Binney J. (1977, The Astrophysical Journal) | DOI:10.1086/155378; arXiv:none; ADS:1977ApJ...215..483B | role=analytic_theory | Foundational analytic theory establishing gas cooling and dissipation as necessities for galactic structure.
[REV04-P007] | Blondin J. M., Wright E. B., Borkowski K. J., Reynolds S. P. (1998, The Astrophysical Journal) | DOI:10.1086/305708; arXiv:none; ADS:1998ApJ...500..342B | role=analytic_theory | Detailed the thermodynamic transition of supernova remnants into the radiative snowplow phase.
[REV04-P008] | Boulares A., Cox D. P. (1990, The Astrophysical Journal) | DOI:10.1086/169509; arXiv:none; ADS:1990ApJ...365..544B | role=analytic_theory | Analytic hydrostatic-equilibrium accounting for magnetic and cosmic-ray support in the Galactic disk; not a direct observational measurement.
[REV04-P009] | Brook C. B., et al. (2011, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2011.18545.x; arXiv:1010.1004; ADS:2011MNRAS.415.1051B | role=hydrodynamic_simulation | Simulation result that preferentially ejected low-angular-momentum gas can support bulgeless disks; implementation and halo-history dependent.
[REV04-P010] | Cen R., Ostriker J. P. (1992, The Astrophysical Journal Letters) | DOI:10.1086/186620; arXiv:none; ADS:1992ApJ...399L.113C | role=hydrodynamic_simulation | Introduced local timescales tied to dynamical and cooling times for sub-grid star formation.
[REV04-P012] | Cioffi D. F., McKee C. F., Bertschinger E. (1988, The Astrophysical Journal) | DOI:10.1086/166834; arXiv:none; ADS:1988ApJ...334..252C | role=analytic_theory | Provided the classic analytic framework for the momentum and energy scaling of evolving supernova remnants.
[REV04-P014] | Dalla Vecchia C., Schaye J. (2008, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2008.13322.x; arXiv:0801.2770; ADS:2008MNRAS.387.1431D | role=hydrodynamic_simulation | Kinetic supernova-feedback outflow implementation; wind behavior depends on launch parameters and hydrodynamic coupling.
[REV04-P015] | Dekel A., Silk J. (1986, The Astrophysical Journal) | DOI:10.1086/164050; arXiv:none; ADS:1986ApJ...303...39D | role=analytic_theory | Early theoretical realization that supernova feedback is required to prevent excessive cooling in dwarf halos.
[REV04-P016] | Draine B. T. (2011, Physics of the Interstellar and Intergalactic Medium) | DOI:none; arXiv:none; ADS:2011piim.book.....D | role=supporting_reference | Textbook synthesis of ISM and intergalactic-medium physics; supporting reference, not a primary paper.
[REV04-P017] | Fall S. M., Efstathiou G. (1980, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | role=analytic_theory | Established the basic model of disk formation via tidal torques and angular momentum conservation during cooling.
[REV04-P018] | Haid S., Walch S., Naab T., Seifried D., Mackey J., Gatto A. (2016, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stw1082; arXiv:1604.04395; ADS:2016MNRAS.460.2962H | role=hydrodynamic_simulation | Controlled supernova-remnant calculations across wind-blown, turbulent, and power-law media; ambient structure sets momentum evolution.
[REV04-P020] | Hennebelle P., Iffrig O. (2014, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201423392; arXiv:1405.7819; ADS:2014A&A...570A..81H | role=hydrodynamic_simulation | Magnetized multiphase galactic-disc simulation regulated by supernova explosions; numerical and chemistry assumptions apply.
[REV04-P021] | Katz N. (1992, The Astrophysical Journal) | DOI:10.1086/171366; arXiv:none; ADS:1992ApJ...391..502K | role=hydrodynamic_simulation | Original formulation of sub-resolution SF density-timescale criteria for SPH modeling.
[REV04-P022] | Katz N., Gunn J. E. (1991, The Astrophysical Journal) | DOI:10.1086/170367; arXiv:none; ADS:1991ApJ...377..365K | role=hydrodynamic_simulation | Early documentation of angular momentum crises in simulated dissipative gas clouds.
[REV04-P023] | Katz N., Weinberg D. H., Hernquist L. (1996, The Astrophysical Journal Supplement Series) | DOI:10.1086/192305; arXiv:astro-ph/9509107; ADS:1996ApJS..105...19K | role=hydrodynamic_simulation | Highlighted the severe tendency for cosmological simulations to overproduce central bulges.
[REV04-P024] | Kennicutt R. C., Jr (1998, The Astrophysical Journal) | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=observation | Defined the global relation used essentially by all models to calibrate sub-grid star formation rates.
[REV04-P025] | Kereš D., Katz N., Weinberg D. H., Davé R. (2005, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0407095; ADS:2005MNRAS.363....2K | role=hydrodynamic_simulation | Evaluated the thermodynamics and morphological consequences of cold versus hot accretion flows.
[REV04-P026] | Kim C.-G., Ostriker E. C. (2015, The Astrophysical Journal) | DOI:10.1088/0004-637X/802/2/99; arXiv:1410.1537; ADS:2015ApJ...802...99K | role=hydrodynamic_simulation | Precise limits on momentum scaling derived from ultra-high resolution SNR expansion experiments.
[REV04-P027] | Larson R. B. (1974, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/169.2.229; arXiv:none; ADS:1974MNRAS.169..229L | role=analytic_theory | Foundational theory linking stellar feedback to the macroscopic evolution and element retention of young galaxies.
[REV04-P028] | Leroy A. K., et al. (2008, The Astronomical Journal) | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=observation | Spatially resolved observations establishing the profound inefficiency of molecular gas converting to stars.
[REV04-P029] | Marinacci F., et al. (2011, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2011.18810.x; arXiv:1103.5358; ADS:2011MNRAS.415.1534M | role=hydrodynamic_simulation | Galactic-fountain interaction with rotating coronae; constrains fountain/corona angular-momentum exchange rather than generic nonlinear torques.
[REV04-P030] | Martizzi D., Faucher-Giguère C.-A., Quataert E. (2015, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stv562; arXiv:1409.4425; ADS:2015MNRAS.450..504M | role=hydrodynamic_simulation | Quantitative formulas for momentum and thermal energy injected into explicitly inhomogeneous, multiphase media.
[REV04-P031] | McKee C. F., Ostriker J. P. (1977, The Astrophysical Journal) | DOI:10.1086/155667; arXiv:none; ADS:1977ApJ...218..148M | role=analytic_theory | Established the theoretical blueprint for a three-phase ISM driven uniquely by successive SN explosions.
[REV04-P032] | Navarro J. F., Benz W. (1991, The Astrophysical Journal) | DOI:10.1086/170590; arXiv:none; ADS:1991ApJ...380..320N | role=hydrodynamic_simulation | Linked collisionless dark matter halos with highly dissipative, overcooling gas inflows.
[REV04-P033] | Navarro J. F., Steinmetz M. (1997, The Astrophysical Journal) | DOI:10.1086/303763; arXiv:astro-ph/9605043; ADS:1997ApJ...478...13N | role=hydrodynamic_simulation | Simulation of photoionizing ultraviolet-background effects on disk-galaxy formation; not a generic no-feedback angular-momentum experiment.
[REV04-P034] | Peebles P. J. E. (1969, The Astrophysical Journal) | DOI:10.1086/149876; arXiv:none; ADS:1969ApJ...155..393P | role=analytic_theory | Classical analytical determination of initial galaxy spin acquired via external large-scale tidal forces.
[REV04-P035] | Pettini M., et al. (2001, The Astrophysical Journal) | DOI:10.1086/321403; arXiv:astro-ph/0102456; ADS:2001ApJ...554..981P | role=observation | Early spectroscopic confirmation of massive, high-velocity galactic winds occurring at cosmic noon.
[REV04-P036] | Pontzen A., Governato F. (2012, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2012.20571.x; arXiv:1106.0499; ADS:2012MNRAS.421.3464P | role=hydrodynamic_simulation | Showed how rapid, baryon-driven outflows dramatically alter the inner gravitational profiles of small halos.
[REV04-P037] | Rees M. J., Ostriker J. P. (1977, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/179.4.541; arXiv:none; ADS:1977MNRAS.179..541R | role=analytic_theory | Established the physical boundaries determining where dark matter halos successfully trap cooling gas.
[REV04-P038] | Schaye J., et al. (2015, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stu2058; arXiv:1407.7040; ADS:2015MNRAS.446..521S | role=hydrodynamic_simulation | Large-scale cosmological simulation achieving realistic stellar mass properties via calibrated stochastic thermal heating.
[REV04-P039] | Schmidt M. (1959, The Astrophysical Journal) | DOI:10.1086/146614; arXiv:none; ADS:1959ApJ...129..243S | role=analytic_theory | Formulated the fundamental empirical power-law linking star-formation rates to locally available gas density.
[REV04-P040] | Silk J. (1977, The Astrophysical Journal) | DOI:10.1086/154972; arXiv:none; ADS:1977ApJ...211..638S | role=analytic_theory | Foundational criteria establishing the upper limits on cooling rates leading to star formation within galactic halos.
[REV04-P041] | Springel V., Hernquist L. (2003, Monthly Notices of the Royal Astronomical Society) | DOI:10.1046/j.1365-8711.2003.06206.x; arXiv:astro-ph/0206393; ADS:2003MNRAS.339..289S | role=semi_analytic_model | Formulation of the widely used sub-grid multiphase effective equation of state balancing star formation and feedback.
[REV04-P044] | Walch S., Naab T. (2015, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stv1975; arXiv:1412.2749; ADS:2015MNRAS.454..238W | role=hydrodynamic_simulation | SILCC chemical evolution of a supernova-driven ISM; do not overextend to a universal clustered-versus-isolated momentum validation.
[REV04-P045] | Werk J. K., et al. (2014, The Astrophysical Journal) | DOI:10.1088/0004-637X/792/1/8; arXiv:1403.0947; ADS:2014ApJ...792....8W | role=observation | Quantified cool gas densities and heavy element kinematics within the extended halos of massive star-forming galaxies.
[REV04-P046] | White S. D. M., Rees M. J. (1978, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | role=analytic_theory | The seminal framework for two-stage cosmological formation (merging collisionless dark matter followed by dissipative gas cooling).
[REV04-P049] | Salem M., Bryan G. L. (2014, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stt2121; arXiv:1307.6215; ADS:2014MNRAS.437.3312S | role=hydrodynamic_simulation | Simulated the efficiency of cosmic-ray transport in accelerating cold gas out of the galactic potential well.
[REV04-S01] | Elmegreen B. G., Scalo J. (2004, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev.astro.41.011802.094859; arXiv:astro-ph/0404451; ADS:2004ARA&A..42..211E | role=review_synthesis | Synthesis of ISM turbulence phenomena.
[REV04-S02] | Janka H.-T. (2012, Annual Review of Nuclear and Particle Science) | DOI:10.1146/annurev-nucl-102711-094901; arXiv:1206.2503; ADS:2012ARNPS..62..407J | role=review_synthesis | Reference data for supernova explosion thermodynamics.
[REV04-S04] | Veilleux S., Cecil G., Bland-Hawthorn J. (2005, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev.astro.43.072103.150610; arXiv:astro-ph/0504435; ADS:2005ARA&A..43..769V | role=review_synthesis | Benchmarked the properties and ubiquity of galactic winds.

REVIEW_BASE_04_DR_COMPLETE_REFERENCE_ONLY

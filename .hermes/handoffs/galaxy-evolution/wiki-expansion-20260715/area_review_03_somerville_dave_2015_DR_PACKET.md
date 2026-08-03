# Review Base 03 canonical advisory packet — Somerville & Davé 2015

status: READY_FOR_HWAO_REVIEW
advisory_only: true
wiki_write_performed_by_tori: false
canonical_source_base_not_live_wiki_prose: true
raw_packet_sha256: 508f5f53543c3d4e25430e04fd87088a6ffe81dfbba79517c02c49c625bc4661
source_registry_status: PASS
usable_sources: 50
primary_sources: 46
supporting_reviews: 4
scope_quarantined_sources: 8

## 1. Review identity and scope map

[REV03] Somerville, Rachel S. & Davé, Romeel (2015, Annual Review of Astronomy and Astrophysics) | title=Physical Models of Galaxy Formation in a Cosmological Framework | DOI:10.1146/annurev-astro-082812-140951; arXiv:1412.2712; ADS:2015ARA&A..53...51S | role=review_synthesis | trust_score=0.98 | boundary=2015 synthesis of semi-analytic and cosmological hydrodynamic galaxy-formation models; retain calibration, numerical, mass, redshift, resolution, cosmology, and subgrid boundaries.

- Cosmological backbone: supports hierarchical halo assembly and baryonic accretion as shared model structure; it does not make baryonic prescriptions first-principles.
- Semi-analytic models: support rapid controlled experiments on merger trees; their differential prescriptions and parameters remain phenomenological.
- Hydrodynamic simulations: directly evolve resolved gravity and gas dynamics; unresolved ISM, stellar feedback, and black-hole coupling remain subgrid.
- Model-observation comparison: supports benchmark and tension mapping; matching a tuned target does not identify the true physical mechanism.
- Baryon cycle: supports linked inflow, star formation, outflow, recycling, and enrichment; individual rates and pathways remained uncertain.
- Structure and morphology: supports bounded roles for angular momentum, mergers, instabilities, and environment; no single channel explains every galaxy.
- Black-hole feedback is retained only as a bounded galaxy-scale model ingredient. Accretion microphysics and AGN-centered sources are quarantined.
- Post-2015 simulations, JWST results, and machine-learning inference are outside this packet.

## 2. Established findings

[REV03-E01]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Both semi-analytic models and cosmological hydrodynamic simulations begin from hierarchical dark-matter assembly and add baryonic cooling, star formation, feedback, enrichment, and structural evolution.
- scope/boundary: Shared architecture does not imply identical numerical solutions or uniquely determined baryonic physics.
- review basis: Sections 1.2-1.4 and 2.
- confidence note: High as a framework statement.
- source keys: [REV03], [REV03-P001], [REV03-P002], [REV03-P039]
- trust_score: 0.96

[REV03-E02]
- role: established
- epistemic_type: empirical_inference
- atomic finding: The shallow low-mass galaxy abundance relative to the halo mass function requires strongly mass-dependent suppression of baryon conversion in shallow potential wells.
- scope/boundary: Necessity is robust; the detailed mass loading, energy coupling, and recycling mechanism are not uniquely inferred.
- review basis: Section 4.1; stellar-mass-function comparisons.
- confidence note: High for suppression, moderate for mechanism.
- source keys: [REV03], [REV03-P004], [REV03-P009], [REV03-P010], [REV03-P042]
- trust_score: 0.94

[REV03-E03]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Gas accretion separates usefully into rapidly cooling filamentary/cold pathways and shock-heated hot-halo pathways, with the balance depending on halo mass, redshift, metallicity, and environment.
- scope/boundary: The modes overlap; a fixed universal mass threshold is an approximation.
- review basis: Section 1.3; gas accretion and cooling.
- confidence note: High for the two limiting regimes, moderate for exact partition.
- source keys: [REV03], [REV03-P005], [REV03-P026]
- trust_score: 0.93

[REV03-E04]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Cosmological volumes cannot resolve the full multiphase ISM and individual star-forming clouds, so both model families require subgrid star-formation and feedback prescriptions.
- scope/boundary: Numerical resolution and hydrodynamic method change what is unresolved and how subgrid energy couples.
- review basis: Sections 2.2, 3.1, and 3.3.
- confidence note: High.
- source keys: [REV03], [REV03-P019], [REV03-P020], [REV03-P024], [REV03-P049]
- trust_score: 0.97

[REV03-E05]
- role: established
- epistemic_type: observation
- atomic finding: Resolved and global gas-SFR relations provide the empirical foundation for star-formation recipes used in models.
- scope/boundary: Total-gas and molecular relations differ by regime and scale; calibration does not establish a universal cloud-scale efficiency.
- review basis: Section 3.1.
- confidence note: High for empirical correlation, moderate for causal interpretation.
- source keys: [REV03], [REV03-P006], [REV03-P008], [REV03-P038], [REV03-P045]
- trust_score: 0.94

[REV03-E06]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Stellar-driven outflows are central to lowering low-mass galaxy efficiencies, transporting metals, and coupling the ISM to the CGM.
- scope/boundary: Required model effect is robust; launch mechanism, mass loading, hydrodynamic coupling, and recycling remain model-dependent.
- review basis: Section 3.3.2 and Section 4.1.
- confidence note: High for importance, moderate for implementation.
- source keys: [REV03], [REV03-P004], [REV03-P018], [REV03-P049], [REV03-P050]
- trust_score: 0.93

[REV03-E07]
- role: established
- epistemic_type: semi_analytic_model
- atomic finding: Successful galaxy population models require preventive suppression of cooling and star formation in massive halos in addition to low-mass stellar feedback.
- scope/boundary: Radio-mode black-hole feedback is a phenomenological galaxy-scale implementation, not proof of unique AGN microphysics; virial heating and environmental channels also matter.
- review basis: Sections 3.3 and 4.1.
- confidence note: High for a high-mass suppression channel, lower for unique cause.
- source keys: [REV03], [REV03-P015], [REV03-P046], [REV03-P051]
- trust_score: 0.89

[REV03-E08]
- role: established
- epistemic_type: observation
- atomic finding: Most star-forming galaxies occupy a relatively narrow SFR-stellar-mass sequence, making sustained gas supply and regulation a central model benchmark.
- scope/boundary: Selection, SFR indicator, stellar masses, redshift, and treatment of starbursts/quiescent systems affect slope and scatter.
- review basis: Section 1.1.2.
- confidence note: High for the sequence, moderate for a unique equilibrium interpretation.
- source keys: [REV03], [REV03-P047], [REV03-P053]
- trust_score: 0.94

[REV03-E09]
- role: established
- epistemic_type: empirical_inference
- atomic finding: Abundance matching places peak stellar conversion efficiency near Milky-Way-scale halos and much lower efficiencies toward both lower and higher halo masses.
- scope/boundary: Inference assumes halo catalogs, galaxy mass functions, scatter, satellite treatment, and stellar-mass systematics.
- review basis: Section 4.1.
- confidence note: High for non-monotonic efficiency, moderate for exact normalization.
- source keys: [REV03], [REV03-P009], [REV03-P010], [REV03-P011], [REV03-P032]
- trust_score: 0.93

[REV03-E10]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Mergers, dissipative gas dynamics, and internal disk instabilities can all alter bulges, compactness, and morphology.
- scope/boundary: Relative importance varies with mass, gas fraction, redshift, orbit, and environment; morphology alone does not identify the channel.
- review basis: Section 4.2.
- confidence note: High for multiple channels, moderate for their population weights.
- source keys: [REV03], [REV03-P016], [REV03-P021], [REV03-P022], [REV03-P023], [REV03-P029], [REV03-P030]
- trust_score: 0.91

[REV03-E11]
- role: established
- epistemic_type: analytic_theory
- atomic finding: Halo angular momentum and baryonic retention/loss provide a baseline connection between halo properties and disk sizes.
- scope/boundary: Simple angular-momentum conservation is modified by feedback, torques, accretion geometry, mergers, and component exchange.
- review basis: Section 4.2.1.
- confidence note: High as a baseline, moderate as a quantitative prediction.
- source keys: [REV03], [REV03-P003], [REV03-P048], [REV03-P054]
- trust_score: 0.91

[REV03-E12]
- role: established
- epistemic_type: observation
- atomic finding: Stellar and gas-phase metallicity relations provide independent constraints on integrated star formation, enrichment, inflow, and metal loss.
- scope/boundary: Calibration scales, apertures, yields, dust, and abundance methods can shift normalizations.
- review basis: Sections 1.1.2 and 3.1.
- confidence note: High for mass trends, moderate for absolute metallicity and mechanism.
- source keys: [REV03], [REV03-P012], [REV03-P013], [REV03-P017], [REV03-P018]
- trust_score: 0.93

## 3. Open debates and tensions

[REV03-D01] | role=debate | topic=SAM versus hydrodynamic convergence | positions=Different techniques can converge on broad populations versus agreement being driven by shared calibrations and analogous subgrid assumptions. | unresolved=Controlled same-initial-condition and same-physics comparisons remained limited. | boundary=Numerical method, resolution, and calibration sets must be explicit. | source keys=[REV03], [REV03-P020], [REV03-P024], [REV03-P025], [REV03-P035] | trust_score=0.91
[REV03-D02] | role=debate | topic=Cold versus hot accretion | positions=Filamentary cold supply dominates much galaxy growth versus stable virial shocks and cooling atmospheres controlling massive systems. | unresolved=Mode definitions, mixing, feedback, resolution, and tracer observability alter classifications. | boundary=Halo mass, metallicity, redshift, and environment dependent. | source keys=[REV03], [REV03-P005], [REV03-P026] | trust_score=0.90
[REV03-D03] | role=debate | topic=Wind implementation and recycling | positions=Kinetic kicks, thermal deposition, or more explicit multiphase feedback produce the required regulation through different paths. | unresolved=Launch scales are unresolved in cosmological boxes and recycled gas is difficult to observe directly. | boundary=Mass loading and recycling are model outputs tied to subgrid choices. | source keys=[REV03], [REV03-P018], [REV03-P049], [REV03-P050] | trust_score=0.90
[REV03-D04] | role=debate | topic=Low- and high-mass quenching | positions=Stellar feedback dominates shallow halos while virial heating/black-hole feedback suppresses massive systems versus overlapping environmental and supply processes. | unresolved=Multiple implementations match some of the same tuned population statistics. | boundary=No claim that one channel explains every quenched galaxy. | source keys=[REV03], [REV03-P004], [REV03-P015], [REV03-P033], [REV03-P046], [REV03-P051] | trust_score=0.88
[REV03-D05] | role=debate | topic=Angular momentum and size evolution | positions=Sizes largely reflect halo spin with approximate angular-momentum retention versus feedback-selective loss, torques, and accretion history setting sizes. | unresolved=Direct baryon-angular-momentum accounting across phases was incomplete. | boundary=Disk/spheroid, mass, redshift, and selection dependent. | source keys=[REV03], [REV03-P003], [REV03-P048], [REV03-P054] | trust_score=0.89
[REV03-D06] | role=debate | topic=Mergers versus internal structural evolution | positions=Major/minor mergers dominate spheroid and compact-galaxy growth versus violent disk instability and secular evolution contributing substantially. | unresolved=Observed morphology and simulations did not uniquely reconstruct histories. | boundary=Gas fraction, orbit, mass ratio, redshift, and resolution. | source keys=[REV03], [REV03-P016], [REV03-P021], [REV03-P022], [REV03-P023], [REV03-P029], [REV03-P030] | trust_score=0.90
[REV03-D07] | role=debate | topic=Subgrid degeneracy | positions=Phenomenological recipes are adequate effective descriptions versus different recipes yielding similar calibrations but divergent mechanisms and secondary predictions. | unresolved=The physical launch and coupling scales were unresolved and systematic code comparisons were sparse. | boundary=Numerical convergence is not physical validation. | source keys=[REV03], [REV03-P019], [REV03-P020], [REV03-P024], [REV03-P049] | trust_score=0.95
[REV03-D08] | role=debate | topic=Reproducing stellar-mass functions without overcalibration | positions=Matching evolving mass functions demonstrates successful regulation versus extensive tuning hiding incorrect gas-cycle mechanisms. | unresolved=Mass-function, SFR, gas, metallicity, and structural constraints were not simultaneously matched uniquely. | boundary=Distinguish calibrated observables from predictions. | source keys=[REV03], [REV03-P009], [REV03-P010], [REV03-P015], [REV03-P032], [REV03-P051], [REV03-P055] | trust_score=0.94

## 4. Key measurements, model benchmarks, and calibrations

[REV03-N01] | role=benchmark | metric=Peak stellar-to-halo conversion scale | value=maximum near halo mass ~10^12 Msun, with lower efficiency on both sides | sample/method=multi-epoch abundance matching | calibrated_or_predicted=empirical inference used as model target | caveat=stellar masses, halo catalogs, scatter, satellites | source keys=[REV03], [REV03-P009], [REV03-P010], [REV03-P032] | trust_score=0.91
[REV03-N02] | role=benchmark | metric=Cold/hot transition scale | value=order 10^11.5-10^12 Msun halo mass in idealized/theory and cited simulations | sample/method=cooling-time versus compression and hydrodynamic accretion histories | calibrated_or_predicted=theory/simulation result | caveat=redshift, metallicity, geometry, feedback, definition | source keys=[REV03], [REV03-P005], [REV03-P026] | trust_score=0.88
[REV03-N03] | role=measurement | metric=Star-forming main-sequence scatter | value=order 0.3 dex for selected star-forming populations | sample/method=multiwavelength field surveys to z~2.5 | calibrated_or_predicted=observational benchmark | caveat=SFR and mass estimators, selection, redshift bins | source keys=[REV03], [REV03-P047], [REV03-P053] | trust_score=0.89
[REV03-N04] | role=calibration | metric=Global Kennicutt-Schmidt relation | value=surface SFR approximately proportional to gas surface density^1.4 in the original global sample | sample/method=disk-averaged normal and starburst galaxies | calibrated_or_predicted=empirical subgrid anchor | caveat=scale, gas phase, conversion factor, dynamical regime | source keys=[REV03], [REV03-P008] | trust_score=0.93
[REV03-N05] | role=measurement | metric=Molecular-gas star-formation relation | value=approximately linear over much of nearby disk regime with order-Gyr depletion times | sample/method=sub-kpc resolved nearby-galaxy maps | calibrated_or_predicted=observational benchmark | caveat=CO conversion, resolution, dense/starburst regimes | source keys=[REV03], [REV03-P006] | trust_score=0.91
[REV03-N06] | role=measurement | metric=Local gas-phase mass-metallicity relation | value=measured for roughly 53,000 SDSS star-forming galaxies | sample/method=fiber spectroscopy and strong-line calibration | calibrated_or_predicted=observational benchmark | caveat=aperture and abundance-calibration systematics | source keys=[REV03], [REV03-P013] | trust_score=0.94
[REV03-N07] | role=measurement | metric=Galaxy size-mass evolution to z~3 | value=star-forming and quiescent populations show different mass-normalized size evolution | sample/method=3D-HST+CANDELS structural fits | calibrated_or_predicted=observational benchmark | caveat=rest wavelength, Sérsic modeling, progenitor selection | source keys=[REV03], [REV03-P054] | trust_score=0.91
[REV03-N08] | role=benchmark | metric=Evolving star-forming/quiescent stellar-mass functions | value=population functions constrained to z~4 in the cited UltraVISTA analysis | sample/method=photometric redshifts and SED masses | calibrated_or_predicted=model target, not a model output | caveat=mass completeness, Eddington bias, IMF, photo-z | source keys=[REV03], [REV03-P055] | trust_score=0.90

## 5. What remained unknown in 2015

[REV03-U01] | role=future | gap=Physical launch and coupling of stellar feedback across unresolved scales | importance=sets mass loading, phase structure, and regulation | needed=multiscale simulations and resolved wind/ISM observations | source keys=[REV03], [REV03-P018], [REV03-P049], [REV03-P050]
[REV03-U02] | role=future | gap=Direct rates and geometry of cosmological inflow | importance=separates supply regulation from feedback regulation | needed=CGM kinematics/metallicity plus tracer-forward simulations | source keys=[REV03], [REV03-P005], [REV03-P026]
[REV03-U03] | role=future | gap=Wind recycling times and baryon pathways through the CGM | importance=recycled gas may dominate later fueling | needed=Lagrangian phase tracking and observational inflow/outflow discrimination | source keys=[REV03], [REV03-P018], [REV03-P049]
[REV03-U04] | role=future | gap=Unique cause of massive-galaxy quenching | importance=different mechanisms can match the bright-end cutoff | needed=gas-state, environment, halo, and time-resolved quenching tests | source keys=[REV03], [REV03-P015], [REV03-P033], [REV03-P046], [REV03-P051]
[REV03-U05] | role=future | gap=Relative roles of mergers and internal processes in structural evolution | importance=connects morphology to assembly history | needed=kinematics, stellar populations, pair histories, and controlled simulations | source keys=[REV03], [REV03-P016], [REV03-P021], [REV03-P022], [REV03-P023], [REV03-P054]
[REV03-U06] | role=future | gap=Physical convergence rather than calibration convergence | importance=similar observables can arise from different subgrid mechanisms | needed=same-initial-condition multi-code tests, resolution ladders, and out-of-sample observables | source keys=[REV03], [REV03-P019], [REV03-P020], [REV03-P024]

## 6. Primary-citation harvest

The 46 rows below are primary observational, empirical, analytic, semi-analytic, or simulation papers directly cited by Somerville & Davé 2015. Four cited reviews are retained separately for orientation and are not counted toward the primary total. Eight raw candidates are quarantined for absent review membership or AGN-microphysics scope.

[REV03-P001] White & Rees (1978, MNRAS) | title=Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering. | DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | role=analytic_theory | review_locator=Section 1.3 | Foundational theory that gas cools within dark matter potential wells.
[REV03-P002] White & Frenk (1991, ApJ) | title=Galaxy Formation through Hierarchical Clustering | DOI:10.1086/170483; arXiv:none; ADS:1991ApJ...379...52W | role=semi_analytic_model | review_locator=Section 1.3 | Established that cooling efficiency scales inversely with density, predicting the cooling catastrophe without feedback.
[REV03-P003] Fall & Efstathiou (1980, MNRAS) | title=Formation and rotation of disc galaxies with haloes. | DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | role=analytic_theory | review_locator=Section 4.2.1 | Gas angular momentum acquisition through tidal torques shapes rotationally supported disks.
[REV03-P004] Dekel & Silk (1986, ApJ) | title=The Origin of Dwarf Galaxies, Cold Dark Matter, and Biased Galaxy Formation | DOI:10.1086/164050; arXiv:none; ADS:1986ApJ...303...39D | role=analytic_theory | review_locator=Section 1.3 | Early identification that supernova-driven winds are required to suppress star formation in low-mass halos.
[REV03-P005] Kereš et al. (2005, MNRAS) | title=How do galaxies get their gas? | DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0407095; ADS:2005MNRAS.363....2K | role=hydrodynamic_simulation | review_locator=Section 1.3 | Identified the bimodal hot/cold gas accretion paradigm in hydrodynamical simulations.
[REV03-P006] Bigiel et al. (2008, AJ) | title=The Star Formation Law in Nearby Galaxies on Sub-Kpc Scales | DOI:10.1088/0004-6256/136/6/2846; arXiv:0810.2541; ADS:2008AJ....136.2846B | role=measurement | review_locator=Section 3.1 | Empirical measurement linking star formation directly to molecular hydrogen rather than total neutral gas.
[REV03-P008] Kennicutt (1998, ApJ) | title=The Global Schmidt Law in Star-forming Galaxies | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=measurement | review_locator=Section 3.1 | Defined the baseline empirical calibration for the relationship between gas density and star formation rate.
[REV03-P009] Moster et al. (2013, MNRAS) | title=Galactic star formation and accretion histories from matching galaxies to dark matter haloes | DOI:10.1093/mnras/sts261; arXiv:1205.5807; ADS:2013MNRAS.428.3121M | role=empirical_inference | review_locator=Section 4.1 | Derived multi-epoch abundance matching constraining the stellar-to-halo mass relation.
[REV03-P010] Behroozi et al. (2013, ApJ) | title=The Average Star Formation Histories of Galaxies in Dark Matter Halos from z = 0-8 | DOI:10.1088/0004-637X/770/1/57; arXiv:1207.6105; ADS:2013ApJ...770...57B | role=empirical_inference | review_locator=Section 4.1 | Quantified the robust SHMR and integrated cosmic star formation matching via abundance techniques.
[REV03-P011] Behroozi et al. (2013, ApJ) | title=Gravitationally Consistent Halo Catalogs and Merger Trees for Precision Cosmology | DOI:10.1088/0004-637X/763/1/18; arXiv:1110.4370; ADS:2013ApJ...763...18B | role=calibration | review_locator=Section 2.1 | Halo-catalog and merger-tree consistency method for dark-matter simulations; not a hydrodynamic galaxy simulation or a direct halo-structure measurement.
[REV03-P012] Gallazzi et al. (2005, MNRAS) | title=The ages and metallicities of galaxies in the local universe | DOI:10.1111/j.1365-2966.2005.09321.x; arXiv:astro-ph/0506539; ADS:2005MNRAS.362...41G | role=measurement | review_locator=Section 1.1.2 | Key observational benchmark for the stellar metallicity distribution in low-redshift galaxies.
[REV03-P013] Tremonti et al. (2004, ApJ) | title=The Origin of the Mass-Metallicity Relation: Insights from 53,000 Star-forming Galaxies in the Sloan Digital Sky Survey | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=measurement | review_locator=Section 1.1.2 | Established the definitive low-redshift gas-phase mass-metallicity relation scaling.
[REV03-P014] Baldry et al. (2004, ApJ) | title=Quantifying the Bimodal Color-Magnitude Distribution of Galaxies | DOI:10.1086/380092; arXiv:astro-ph/0309710; ADS:2004ApJ...600..681B | role=measurement | review_locator=Section 1.1.1 | Measured the robust structural separation between the star-forming blue cloud and quiescent red sequence.
[REV03-P015] Bower et al. (2006, MNRAS) | title=Breaking the hierarchy of galaxy formation | DOI:10.1111/j.1365-2966.2006.10519.x; arXiv:astro-ph/0511338; ADS:2006MNRAS.370..645B | role=semi_analytic_model | review_locator=Section 4.1 | Demonstrated that radio-mode AGN feedback quenches cooling flows to match the bright-end luminosity function.
[REV03-P016] Cox et al. (2006, MNRAS) | title=Feedback in simulations of disc-galaxy major mergers | DOI:10.1111/j.1365-2966.2006.11107.x; arXiv:astro-ph/0503201; ADS:2006MNRAS.373.1013C | role=hydrodynamic_simulation | review_locator=Section 4.2 | Modeled merger-driven starbursts and the necessary dissipation scales for feedback.
[REV03-P017] Arrigoni et al. (2010, MNRAS) | title=Galactic chemical evolution in hierarchical formation models - I. Early-type galaxies in the local Universe | DOI:10.1111/j.1365-2966.2009.15924.x; arXiv:0905.4189; ADS:2010MNRAS.402..173A | role=semi_analytic_model | review_locator=Section 3.1 | Assessed chemical abundance ratio constraints within hierarchical semi-analytic models.
[REV03-P018] Peeples & Shankar (2011, MNRAS) | title=Constraints on star formation driven galaxy winds from the mass-metallicity relation at z= 0 | DOI:10.1111/j.1365-2966.2011.19456.x; arXiv:1007.3743; ADS:2011MNRAS.417.2962P | role=empirical_inference | review_locator=Section 1.1.2 | Constrained metal expulsion efficiency and mass-loading factors from the MZR.
[REV03-P019] Gnedin & Kravtsov (2011, ApJ) | title=Environmental Dependence of the Kennicutt-Schmidt Relation in Galaxies | DOI:10.1088/0004-637X/728/2/88; arXiv:1004.0003; ADS:2011ApJ...728...88G | role=hydrodynamic_simulation | review_locator=Section 3.1 | Simulation study of environmental dependence in the Kennicutt-Schmidt relation; do not use as the Gnedin-Kravtsov molecular-shielding prescription paper.
[REV03-P020] Springel (2010, MNRAS) | title=E pur si muove: Galilean-invariant cosmological hydrodynamical simulations on a moving mesh | DOI:10.1111/j.1365-2966.2009.15715.x; arXiv:0901.4107; ADS:2010MNRAS.401..791S | role=hydrodynamic_simulation | review_locator=Section 2.2 | Introduced the moving-mesh architecture resolving critical limitations in standard SPH contact discontinuities.
[REV03-P021] Ceverino et al. (2010, MNRAS) | title=High-redshift clumpy discs and bulges in cosmological simulations | DOI:10.1111/j.1365-2966.2010.16433.x; arXiv:0907.3271; ADS:2010MNRAS.404.2151C | role=hydrodynamic_simulation | review_locator=Section 4.2 | Simulated violent disk instabilities producing giant star-forming clumps at high redshift.
[REV03-P022] Barro et al. (2013, ApJ) | title=CANDELS: The Progenitors of Compact Quiescent Galaxies at z ~ 2 | DOI:10.1088/0004-637X/765/2/104; arXiv:1206.5000; ADS:2013ApJ...765..104B | role=measurement | review_locator=Section 4.2 | Observed the morphological transition and extreme compactness of high-z quiescent galaxies.
[REV03-P023] Bell et al. (2012, ApJ) | title=What Turns Galaxies Off? The Different Morphologies of Star-forming and Quiescent Galaxies since z ~ 2 from CANDELS | DOI:10.1088/0004-637X/753/2/167; arXiv:1110.3786; ADS:2012ApJ...753..167B | role=measurement | review_locator=Section 4.2 | CANDELS morphology comparison of star-forming and quiescent galaxies to z~2; morphology alone does not identify the quenching mechanism.
[REV03-P024] Agertz et al. (2007, MNRAS) | title=Fundamental differences between SPH and grid methods | DOI:10.1111/j.1365-2966.2007.12183.x; arXiv:astro-ph/0610051; ADS:2007MNRAS.380..963A | role=hydrodynamic_simulation | review_locator=Section 2.2 | Demonstrated catastrophic artificial surface tension in SPH resolving multi-phase fluid instabilities.
[REV03-P026] Birnboim & Dekel (2003, MNRAS) | title=Virial shocks in galactic haloes? | DOI:10.1046/j.1365-8711.2003.06955.x; arXiv:astro-ph/0302161; ADS:2003MNRAS.345..349B | role=analytic_theory | review_locator=Section 1.3 | Mathematically established the mass threshold for shock heating over smooth cold flows.
[REV03-P027] Boylan-Kolchin et al. (2011, MNRAS) | title=Too big to fail? The puzzling darkness of massive Milky Way subhaloes | DOI:10.1111/j.1745-3933.2011.01074.x; arXiv:1103.0007; ADS:2011MNRAS.415L..40B | role=hydrodynamic_simulation | review_locator=Section 2.1 | Highlighted tensions between N-body dark matter substructure kinematics and observed satellites.
[REV03-P028] Barnes & Hut (1986, Nature) | title=A hierarchical O(N log N) force-calculation algorithm | DOI:10.1038/324446a0; arXiv:none; ADS:1986Natur.324..446B | role=analytic_theory | review_locator=Section 2.1 | Foundational tree-code algorithm establishing scalable N-body gravity solvers.
[REV03-P029] Barnes (1988, ApJ) | title=Encounters of Disk/Halo Galaxies | DOI:10.1086/166593; arXiv:none; ADS:1988ApJ...331..699B | role=hydrodynamic_simulation | review_locator=Section 4.2 | Early demonstration of violent relaxation in mergers destroying disks and creating spheroids.
[REV03-P030] Barnes (1992, ApJ) | title=Transformations of Galaxies. I. Mergers of Equal-Mass Stellar Disks | DOI:10.1086/171522; arXiv:none; ADS:1992ApJ...393..484B | role=hydrodynamic_simulation | review_locator=Section 4.2 | Demonstrated phase mixing and angular momentum transfer to dark matter during mergers.
[REV03-P031] Baugh et al. (2005, MNRAS) | title=Can the faint submillimetre galaxies be explained in the Λ cold dark matter model? | DOI:10.1111/j.1365-2966.2004.08553.x; arXiv:astro-ph/0406069; ADS:2005MNRAS.356.1191B | role=semi_analytic_model | review_locator=Section 4.1 | Required drastic IMF modifications in SAMs to match high-redshift starbursts.
[REV03-P032] Behroozi et al. (2010, ApJ) | title=A Comprehensive Analysis of Uncertainties Affecting the Stellar Mass-Halo Mass Relation for 0 < z < 4 | DOI:10.1088/0004-637X/717/1/379; arXiv:1001.0015; ADS:2010ApJ...717..379B | role=empirical_inference | review_locator=Section 4.1 | Systematic uncertainty analysis for stellar-mass-to-halo-mass inference over 0<z<4; not a toy-cosmology guide.
[REV03-P033] Bell et al. (2004, ApJ) | title=Nearly 5000 Distant Early-Type Galaxies in COMBO-17: A Red Sequence and Its Evolution since z~1 | DOI:10.1086/420778; arXiv:astro-ph/0303394; ADS:2004ApJ...608..752B | role=measurement | review_locator=Section 4.1 | Quantified the persistent mass build-up on the quiescent red sequence over cosmic time.
[REV03-P034] Bender et al. (1992, ApJ) | title=Dynamically Hot Galaxies. I. Structural Properties | DOI:10.1086/171940; arXiv:none; ADS:1992ApJ...399..462B | role=measurement | review_locator=Section 4.2 | Observed structural properties of dynamically hot galaxies; not a generic velocity-kinematics census of all ellipticals.
[REV03-P036] Benson et al. (2007, MNRAS) | title=Luminosity and stellar mass functions of discs and spheroids in the SDSS and the supermassive black hole mass function | DOI:10.1111/j.1365-2966.2007.11923.x; arXiv:astro-ph/0612719; ADS:2007MNRAS.379..841B | role=semi_analytic_model | review_locator=Section 4.1 | Local disc/spheroid luminosity and stellar-mass functions from decomposed SDSS galaxies; do not use as a dwarf-demographics feedback experiment.
[REV03-P038] Blitz & Rosolowsky (2004, ApJ) | title=The Role of Pressure in Giant Molecular Cloud Formation | DOI:10.1086/424661; arXiv:astro-ph/0407492; ADS:2004ApJ...612L..29B | role=empirical_inference | review_locator=Section 3.1 | Pressure-based giant-molecular-cloud formation relation in nearby galaxies; bounded empirical partition recipe.
[REV03-P039] Blumenthal et al. (1984, Nature) | title=Formation of galaxies and large-scale structure with cold dark matter. | DOI:10.1038/311517a0; arXiv:none; ADS:1984Natur.311..517B | role=analytic_theory | review_locator=Section 1.3 | Foundational cosmology paper establishing cold dark matter clustering behavior.
[REV03-P042] Schechter (1976, ApJ) | title=An analytic expression for the luminosity function for galaxies. | DOI:10.1086/154079; arXiv:none; ADS:1976ApJ...203..297S | role=measurement | review_locator=Section 1.1.1 | Developed the asymptotic mathematical fit for the galaxy mass/luminosity distribution function.
[REV03-P045] Krumholz et al. (2012, ApJ) | title=A Universal, Local Star Formation Law in Galactic Clouds, nearby Galaxies, High-redshift Disks, and Starbursts | DOI:10.1088/0004-637X/745/1/69; arXiv:1109.4150; ADS:2012ApJ...745...69K | role=analytic_theory | review_locator=Section 3.1 | Cross-environment local star-formation-law model; universality is model-bounded rather than a parameter-free empirical fact.
[REV03-P046] Croton et al. (2006, MNRAS) | title=The many lives of active galactic nuclei: cooling flows, black holes and the luminosities and colours of galaxies | DOI:10.1111/j.1365-2966.2005.09675.x; arXiv:astro-ph/0508046; ADS:2006MNRAS.365...11C | role=semi_analytic_model | review_locator=Section 4.1 | Contemporaneous with Bower 2006, established "radio mode" AGN feedback as the critical quenching parameter.
[REV03-P047] Noeske et al. (2007, ApJ) | title=Star Formation in AEGIS Field Galaxies since z=1.1: The Dominance of Gradually Declining Star Formation, and the Main Sequence of Star-forming Galaxies | DOI:10.1086/517926; arXiv:astro-ph/0701924; ADS:2007ApJ...660L..43N | role=measurement | review_locator=Section 1.1.2 | Coined and defined the "Star Forming Main Sequence" against which models calibrate sustained growth.
[REV03-P048] Mo et al. (1998, MNRAS) | title=The formation of galactic discs | DOI:10.1046/j.1365-8711.1998.01227.x; arXiv:astro-ph/9707093; ADS:1998MNRAS.295..319M | role=analytic_theory | review_locator=Section 4.2.1 | Established the isothermal density profile scaling relations connecting dark halo properties to disk sizes.
[REV03-P049] Dalla Vecchia & Schaye (2008, MNRAS) | title=Simulating galactic outflows with kinetic supernova feedback | DOI:10.1111/j.1365-2966.2008.13322.x; arXiv:0801.2770; ADS:2008MNRAS.387.1431D | role=hydrodynamic_simulation | review_locator=Section 3.3.2 | Outlined the temporary hydrodynamic decoupling mechanism required to prevent instantaneous wind thermalization.
[REV03-P050] Governato et al. (2010, Nature) | title=Bulgeless dwarf galaxies and dark matter cores from supernova-driven outflows | DOI:10.1038/nature08640; arXiv:0911.2237; ADS:2010Natur.463..203G | role=hydrodynamic_simulation | review_locator=Section 4.2 | Showed that powerful winds can reshape dark matter profiles and prevent massive bulge overcooling.
[REV03-P051] Fontanot et al. (2009, MNRAS) | title=The many manifestations of downsizing: hierarchical galaxy formation models confront observations | DOI:10.1111/j.1365-2966.2009.15058.x; arXiv:0901.1130; ADS:2009MNRAS.397.1776F | role=semi_analytic_model | review_locator=Section 4.1 | Exposed the persistent failure of calibrated SAMs to reproduce the "downsizing" of massive galaxies at high redshift.
[REV03-P053] Wuyts et al. (2011, ApJ) | title=Galaxy Structure and Mode of Star Formation in the SFR-Mass Plane from z ~ 2.5 to z ~ 0.1 | DOI:10.1088/0004-637X/742/2/96; arXiv:1107.0317; ADS:2011ApJ...742...96W | role=measurement | review_locator=Section 1.1.2 | Linked structural indices (Sersic) directly to positions on the Star-Forming Main Sequence.
[REV03-P054] van der Wel et al. (2014, ApJ) | title=3D-HST+CANDELS: The Evolution of the Galaxy Size-Mass Distribution since z = 3 | DOI:10.1088/0004-637X/788/1/28; arXiv:1404.2844; ADS:2014ApJ...788...28V | role=measurement | review_locator=Section 4.2 | Comprehensive empirical benchmark for the size evolution of disk and spheroidal galaxies over 10 billion years.
[REV03-P055] Muzzin et al. (2013, ApJ) | title=The Evolution of the Stellar Mass Functions of Star-forming and Quiescent Galaxies to z = 4 from the COSMOS/UltraVISTA Survey | DOI:10.1088/0004-637X/777/1/18; arXiv:1303.4409; ADS:2013ApJ...777...18M | role=measurement | review_locator=Section 1.1.1 | Pushed the bimodal mass function demographic baseline out to z=4.

### Supporting cited reviews — not counted as primary

[REV03-P025] Baugh (2006, RPPh) | title=A primer on hierarchical galaxy formation: the semi-analytical approach | DOI:10.1088/0034-4885/69/12/R02; arXiv:astro-ph/0610031; ADS:2006RPPh...69.3101B | role=semi_analytic_model | review_locator=Section 1.4 | Outlined the base mathematical scaffolding linking dark matter assembly to SAM prescriptions.
[REV03-P035] Benson (2010, PhR) | title=Galaxy formation theory | DOI:10.1016/j.physrep.2010.06.001; arXiv:1006.5394; ADS:2010PhR...495...33B | role=review_synthesis | review_locator=Section 1.2 | Broad theoretical framing of the ΛCDM hierarchical components used by models.
[REV03-P037] Blanton & Moustakas (2009, ARA&A) | title=Physical Properties and Environments of Nearby Galaxies | DOI:10.1146/annurev-astro-082708-101734; arXiv:0908.3017; ADS:2009ARA&A..47..159B | role=review_synthesis | review_locator=Section 1.1 | Standard reference for the local galaxy distribution functions and structural metrics.
[REV03-P043] Conroy (2013, ARA&A) | title=Modeling the Panchromatic Spectral Energy Distributions of Galaxies | DOI:10.1146/annurev-astro-082812-141017; arXiv:1301.7095; ADS:2013ARA&A..51..393C | role=review_synthesis | review_locator=Section 1.1 | Benchmark for translating physical simulation stellar parameters into observable SED photometry.

## 7. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | raw REV03-P001 tuple title=Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering; DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | cross-wired composite identity | ADS-correct physical tuple is title=Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering.; DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W
UNCITED_NOT_USABLE | raw REV03-P002 tuple title=Galaxy formation through hierarchical clustering; DOI:10.1086/170485; arXiv:none; ADS:1991ApJ...379...52W | cross-wired composite identity | ADS-correct physical tuple is title=Galaxy Formation through Hierarchical Clustering; DOI:10.1086/170483; arXiv:none; ADS:1991ApJ...379...52W
UNCITED_NOT_USABLE | raw REV03-P003 tuple title=Formation and rotation of disc galaxies with haloes; DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | cross-wired composite identity | ADS-correct physical tuple is title=Formation and rotation of disc galaxies with haloes.; DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F
UNCITED_NOT_USABLE | raw REV03-P005 tuple title=How do galaxies get their gas?; DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0508347; ADS:2005MNRAS.363....2K | cross-wired composite identity | ADS-correct physical tuple is title=How do galaxies get their gas?; DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0407095; ADS:2005MNRAS.363....2K
UNCITED_NOT_USABLE | raw REV03-P011 tuple title=The structure of cold dark matter halos; DOI:10.1088/0004-637X/763/1/18; arXiv:1110.4370; ADS:2013ApJ...763...18B | cross-wired composite identity | ADS-correct physical tuple is title=Gravitationally Consistent Halo Catalogs and Merger Trees for Precision Cosmology; DOI:10.1088/0004-637X/763/1/18; arXiv:1110.4370; ADS:2013ApJ...763...18B
UNCITED_NOT_USABLE | raw REV03-P017 tuple title=Galactic chemical evolution in hierarchical formation models - I. Early-type galaxies in the local Universe; DOI:10.1111/j.1365-2966.2009.15924.x; arXiv:0910.2073; ADS:2010MNRAS.402..173A | cross-wired composite identity | ADS-correct physical tuple is title=Galactic chemical evolution in hierarchical formation models - I. Early-type galaxies in the local Universe; DOI:10.1111/j.1365-2966.2009.15924.x; arXiv:0905.4189; ADS:2010MNRAS.402..173A
UNCITED_NOT_USABLE | raw REV03-P018 tuple title=Constraints on star formation driven galaxy winds from the mass-metallicity relation at z = 0; DOI:10.1111/j.1365-2966.2011.19456.x; arXiv:1007.3498; ADS:2011MNRAS.417.2962P | cross-wired composite identity | ADS-correct physical tuple is title=Constraints on star formation driven galaxy winds from the mass-metallicity relation at z= 0; DOI:10.1111/j.1365-2966.2011.19456.x; arXiv:1007.3743; ADS:2011MNRAS.417.2962P
UNCITED_NOT_USABLE | raw REV03-P019 tuple title=Modeling Molecular Hydrogen and Star Formation in Cosmological Simulations; DOI:10.1088/0004-637X/728/2/88; arXiv:1008.0858; ADS:2011ApJ...728...88G | cross-wired composite identity | ADS-correct physical tuple is title=Environmental Dependence of the Kennicutt-Schmidt Relation in Galaxies; DOI:10.1088/0004-637X/728/2/88; arXiv:1004.0003; ADS:2011ApJ...728...88G
UNCITED_NOT_USABLE | raw REV03-P022 tuple title=CANDELS: The Progenitors of Compact Quiescent Galaxies at z ~ 2; DOI:10.1088/0004-637X/765/2/104; arXiv:1206.5804; ADS:2013ApJ...765..104B | cross-wired composite identity | ADS-correct physical tuple is title=CANDELS: The Progenitors of Compact Quiescent Galaxies at z ~ 2; DOI:10.1088/0004-637X/765/2/104; arXiv:1206.5000; ADS:2013ApJ...765..104B
UNCITED_NOT_USABLE | raw REV03-P023 tuple title=The Different Morphologies of Star-forming and Quiescent Galaxies since z ~ 2 from CANDELS; DOI:10.1088/0004-637X/753/2/167; arXiv:1110.3786; ADS:2012ApJ...753..167B | cross-wired composite identity | ADS-correct physical tuple is title=What Turns Galaxies Off? The Different Morphologies of Star-forming and Quiescent Galaxies since z ~ 2 from CANDELS; DOI:10.1088/0004-637X/753/2/167; arXiv:1110.3786; ADS:2012ApJ...753..167B
UNCITED_NOT_USABLE | raw REV03-P030 tuple title=Transformations of galaxies. I - Mergers of equal-mass stellar disks; DOI:10.1086/171522; arXiv:none; ADS:1992ApJ...393..484B | cross-wired composite identity | ADS-correct physical tuple is title=Transformations of Galaxies. I. Mergers of Equal-Mass Stellar Disks; DOI:10.1086/171522; arXiv:none; ADS:1992ApJ...393..484B
UNCITED_NOT_USABLE | raw REV03-P031 tuple title=Can the faint submillimetre galaxies be explained in the Λ cold dark matter model?; DOI:10.1111/j.1365-2966.2004.08454.x; arXiv:astro-ph/0406063; ADS:2005MNRAS.356.1191B | cross-wired composite identity | ADS-correct physical tuple is title=Can the faint submillimetre galaxies be explained in the Λ cold dark matter model?; DOI:10.1111/j.1365-2966.2004.08553.x; arXiv:astro-ph/0406069; ADS:2005MNRAS.356.1191B
UNCITED_NOT_USABLE | raw REV03-P032 tuple title=A Comprehensive Guide to Toy Cosmologies; DOI:10.1088/0004-637X/717/1/379; arXiv:1001.0015; ADS:2010ApJ...717..379B | cross-wired composite identity | ADS-correct physical tuple is title=A Comprehensive Analysis of Uncertainties Affecting the Stellar Mass-Halo Mass Relation for 0 < z < 4; DOI:10.1088/0004-637X/717/1/379; arXiv:1001.0015; ADS:2010ApJ...717..379B
UNCITED_NOT_USABLE | raw REV03-P033 tuple title=Nearly 5000 Distant Early-Type Galaxies in COMBO-17: A Red Sequence and Its Evolution since z~1; DOI:10.1086/420778; arXiv:astro-ph/0403001; ADS:2004ApJ...608..752B | cross-wired composite identity | ADS-correct physical tuple is title=Nearly 5000 Distant Early-Type Galaxies in COMBO-17: A Red Sequence and Its Evolution since z~1; DOI:10.1086/420778; arXiv:astro-ph/0303394; ADS:2004ApJ...608..752B
UNCITED_NOT_USABLE | raw REV03-P034 tuple title=Velocity kinematics in the elliptical galaxies; DOI:10.1086/171940; arXiv:none; ADS:1992ApJ...399..462B | cross-wired composite identity | ADS-correct physical tuple is title=Dynamically Hot Galaxies. I. Structural Properties; DOI:10.1086/171940; arXiv:none; ADS:1992ApJ...399..462B
UNCITED_NOT_USABLE | raw REV03-P035 tuple title=Galaxy formation theory; DOI:10.1016/j.physrep.2010.08.001; arXiv:1006.5394; ADS:2010PhR...495...33B | cross-wired composite identity | ADS-correct physical tuple is title=Galaxy formation theory; DOI:10.1016/j.physrep.2010.06.001; arXiv:1006.5394; ADS:2010PhR...495...33B
UNCITED_NOT_USABLE | raw REV03-P036 tuple title=The nature of the dwarf galaxy population; DOI:10.1111/j.1365-2966.2007.11933.x; arXiv:astro-ph/0612349; ADS:2007MNRAS.379..841B | cross-wired composite identity | ADS-correct physical tuple is title=Luminosity and stellar mass functions of discs and spheroids in the SDSS and the supermassive black hole mass function; DOI:10.1111/j.1365-2966.2007.11923.x; arXiv:astro-ph/0612719; ADS:2007MNRAS.379..841B
UNCITED_NOT_USABLE | raw REV03-P038 tuple title=The Role of Pressure in GMC Formation II: The H2-Pressure Relation; DOI:10.1086/423719; arXiv:astro-ph/0406451; ADS:2004ApJ...612L..29B | cross-wired composite identity | ADS-correct physical tuple is title=The Role of Pressure in Giant Molecular Cloud Formation; DOI:10.1086/424661; arXiv:astro-ph/0407492; ADS:2004ApJ...612L..29B
UNCITED_NOT_USABLE | raw REV03-P039 tuple title=Formation of galaxies and large-scale structure with cold dark matter; DOI:10.1038/311517a0; arXiv:none; ADS:1984Natur.311..517B | cross-wired composite identity | ADS-correct physical tuple is title=Formation of galaxies and large-scale structure with cold dark matter.; DOI:10.1038/311517a0; arXiv:none; ADS:1984Natur.311..517B
UNCITED_NOT_USABLE | raw REV03-P045 tuple title=A Unified Law for Star Formation in Galaxies and the Interstellar Medium; DOI:10.1088/0004-637X/745/1/69; arXiv:1201.0764; ADS:2012ApJ...745...69K | cross-wired composite identity | ADS-correct physical tuple is title=A Universal, Local Star Formation Law in Galactic Clouds, nearby Galaxies, High-redshift Disks, and Starbursts; DOI:10.1088/0004-637X/745/1/69; arXiv:1109.4150; ADS:2012ApJ...745...69K
UNCITED_NOT_USABLE | raw REV03-P048 tuple title=The formation of galactic discs; DOI:10.1046/j.1365-8711.1998.01587.x; arXiv:astro-ph/9711159; ADS:1998MNRAS.295..319M | cross-wired composite identity | ADS-correct physical tuple is title=The formation of galactic discs; DOI:10.1046/j.1365-8711.1998.01227.x; arXiv:astro-ph/9707093; ADS:1998MNRAS.295..319M
UNCITED_NOT_USABLE | raw REV03-P049 tuple title=Simulating galactic outflows with kinetic supernova feedback; DOI:10.1111/j.1365-2966.2008.13840.x; arXiv:0801.0772; ADS:2008MNRAS.387.1431D | cross-wired composite identity | ADS-correct physical tuple is title=Simulating galactic outflows with kinetic supernova feedback; DOI:10.1111/j.1365-2966.2008.13322.x; arXiv:0801.2770; ADS:2008MNRAS.387.1431D
UNCITED_NOT_USABLE | raw REV03-P044 tuple title=Cosmic Star-Formation History; DOI:10.1146/annurev-astro-081811-025615; arXiv:1403.0007; ADS:2014ARA&A..52..415M | cross-wired composite identity | ADS-correct physical tuple is title=Cosmic Star-Formation History; DOI:10.1146/annurev-astro-081811-125615; arXiv:1403.0007; ADS:2014ARA&A..52..415M
UNCITED_NOT_USABLE | raw REV03-P052 tuple title=The Aquila comparison project: the effects of feedback and numerical methods on simulated formation of disk galaxies; DOI:10.1111/j.1365-2966.2012.20993.x; arXiv:1112.0315; ADS:2012MNRAS.423.1726S | cross-wired composite identity | ADS-correct physical tuple is title=The Aquila comparison project: the effects of feedback and numerical methods on simulations of galaxy formation; DOI:10.1111/j.1365-2966.2012.20993.x; arXiv:1112.0315; ADS:2012MNRAS.423.1726S
UNCITED_NOT_USABLE | raw REV03-P056 tuple title=Galaxies on FIRE (Feedback In Realistic Environments): stellar feedback explains cosmologically inefficient star formation; DOI:10.1093/mnras/stu732; arXiv:1311.2073; ADS:2014MNRAS.445..581H | cross-wired composite identity | ADS-correct physical tuple is title=Galaxies on FIRE (Feedback In Realistic Environments): stellar feedback explains cosmologically inefficient star formation; DOI:10.1093/mnras/stu1738; arXiv:1311.2073; ADS:2014MNRAS.445..581H
UNCITED_NOT_USABLE | raw REV03-P057 tuple title=The Large, Oxygen-Rich Halos of Star-Forming Galaxies Are a Major Reservoir of Galactic Metals; DOI:10.1126/science.1209840; arXiv:1111.3975; ADS:2011Sci...334..948T | cross-wired composite identity | ADS-correct physical tuple is title=The Large, Oxygen-Rich Halos of Star-Forming Galaxies Are a Major Reservoir of Galactic Metals; DOI:10.1126/science.1209840; arXiv:1111.3980; ADS:2011Sci...334..948T
UNCITED_NOT_USABLE | raw REV03-P058 tuple title=The Atomic-to-Molecular Transition in Galaxies. II. HI and H2 Column Densities; DOI:10.1088/0004-637X/693/1/216; arXiv:0810.0011; ADS:2009ApJ...693..216K | cross-wired composite identity | ADS-correct physical tuple is title=The Atomic-to-Molecular Transition in Galaxies. II: H I and H2 Column Densities; DOI:10.1088/0004-637X/693/1/216; arXiv:0811.0004; ADS:2009ApJ...693..216K
UNCITED_NOT_USABLE | REV03-P007 Leroy et al. (2008) title=The Star Formation Efficiency in Nearby Galaxies: Measuring Where Gas Forms Stars Effectively | ADS:2008AJ....136.2782L | Exact ADS bibcode is absent from the review bibliography; physically valid paper but not usable as a review-cited harvest row.
UNCITED_NOT_USABLE | REV03-P040 Bondi (1952) title=On spherically symmetrical accretion | ADS:1952MNRAS.112..195B | Bondi spherical-accretion microphysics is AGN-subgrid context and outside the queue's non-AGN core harvest.
UNCITED_NOT_USABLE | REV03-P041 Booth & Schaye (2009) title=Cosmological simulations of the growth of supermassive black holes and feedback from active galactic nuclei: method and tests | ADS:2009MNRAS.398...53B | Black-hole growth and AGN thermal-feedback method paper is AGN-centered and outside the queue's non-AGN core harvest.
UNCITED_NOT_USABLE | REV03-P044 Madau & Dickinson (2014) title=Cosmic Star-Formation History | ADS:2014ARA&A..52..415M | Exact ADS bibcode and DOI are absent from the review bibliography; supporting review cannot be promoted as review-cited here.
UNCITED_NOT_USABLE | REV03-P052 Scannapieco et al. (2012) title=The Aquila comparison project: the effects of feedback and numerical methods on simulations of galaxy formation | ADS:2012MNRAS.423.1726S | Exact ADS bibcode is absent from the review bibliography; physically valid code-comparison paper but not a review-cited harvest row.
UNCITED_NOT_USABLE | REV03-P056 Hopkins et al. (2014) title=Galaxies on FIRE (Feedback In Realistic Environments): stellar feedback explains cosmologically inefficient star formation | ADS:2014MNRAS.445..581H | Exact ADS bibcode is absent from the review bibliography; physically valid FIRE paper but not a review-cited harvest row.
UNCITED_NOT_USABLE | REV03-P057 Tumlinson et al. (2011) title=The Large, Oxygen-Rich Halos of Star-Forming Galaxies Are a Major Reservoir of Galactic Metals | ADS:2011Sci...334..948T | Exact ADS bibcode is absent from the review bibliography; physically valid CGM observation but not a review-cited harvest row.
UNCITED_NOT_USABLE | REV03-P058 Krumholz et al. (2009) title=The Atomic-to-Molecular Transition in Galaxies. II: H I and H2 Column Densities | ADS:2009ApJ...693..216K | Exact ADS bibcode is absent from the review bibliography; physically valid transition model but not a review-cited harvest row.
UNCITED_NOT_USABLE | one model technique is inherently correct | overbroad claim | SAMs and hydro have different strengths and shared unresolved physics
UNCITED_NOT_USABLE | matching a tuned stellar-mass function proves the feedback mechanism | calibration circularity | distinct prescriptions can fit the same target
UNCITED_NOT_USABLE | subgrid prescriptions are first-principles predictions | category error | they approximate unresolved processes
UNCITED_NOT_USABLE | convergence at one resolution proves physical convergence | unsupported inference | numerical and physical convergence are distinct
UNCITED_NOT_USABLE | all quenching has one cause | overbroad claim | halo, stellar, black-hole, environmental, and supply channels overlap
UNCITED_NOT_USABLE | all high-redshift star formation is merger driven | overbroad claim | main-sequence and instability channels remain
UNCITED_NOT_USABLE | post-2015/JWST/ML source anchors captured by web search | outside date and not review-cited | excluded from usable rows
UNCITED_NOT_USABLE | AGN demographics, accretion-disk, jet, or black-hole-spin claim | outside non-AGN core scope | only bounded galaxy-scale feedback phenomenology is retained

## 8. Review and source identity ledger

[REV03] | Somerville & Davé (2015, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev-astro-082812-140951; arXiv:1412.2712; ADS:2015ARA&A..53...51S | role=review | bounded 2015 galaxy-formation model synthesis
[REV03-P001] | White & Rees (1978, MNRAS) | DOI:10.1093/mnras/183.3.341; arXiv:none; ADS:1978MNRAS.183..341W | role=analytic_theory | Foundational theory that gas cools within dark matter potential wells.
[REV03-P002] | White & Frenk (1991, ApJ) | DOI:10.1086/170483; arXiv:none; ADS:1991ApJ...379...52W | role=semi_analytic_model | Established that cooling efficiency scales inversely with density, predicting the cooling catastrophe without feedback.
[REV03-P003] | Fall & Efstathiou (1980, MNRAS) | DOI:10.1093/mnras/193.2.189; arXiv:none; ADS:1980MNRAS.193..189F | role=analytic_theory | Gas angular momentum acquisition through tidal torques shapes rotationally supported disks.
[REV03-P004] | Dekel & Silk (1986, ApJ) | DOI:10.1086/164050; arXiv:none; ADS:1986ApJ...303...39D | role=analytic_theory | Early identification that supernova-driven winds are required to suppress star formation in low-mass halos.
[REV03-P005] | Kereš et al. (2005, MNRAS) | DOI:10.1111/j.1365-2966.2005.09451.x; arXiv:astro-ph/0407095; ADS:2005MNRAS.363....2K | role=hydrodynamic_simulation | Identified the bimodal hot/cold gas accretion paradigm in hydrodynamical simulations.
[REV03-P006] | Bigiel et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2846; arXiv:0810.2541; ADS:2008AJ....136.2846B | role=measurement | Empirical measurement linking star formation directly to molecular hydrogen rather than total neutral gas.
[REV03-P008] | Kennicutt (1998, ApJ) | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=measurement | Defined the baseline empirical calibration for the relationship between gas density and star formation rate.
[REV03-P009] | Moster et al. (2013, MNRAS) | DOI:10.1093/mnras/sts261; arXiv:1205.5807; ADS:2013MNRAS.428.3121M | role=empirical_inference | Derived multi-epoch abundance matching constraining the stellar-to-halo mass relation.
[REV03-P010] | Behroozi et al. (2013, ApJ) | DOI:10.1088/0004-637X/770/1/57; arXiv:1207.6105; ADS:2013ApJ...770...57B | role=empirical_inference | Quantified the robust SHMR and integrated cosmic star formation matching via abundance techniques.
[REV03-P011] | Behroozi et al. (2013, ApJ) | DOI:10.1088/0004-637X/763/1/18; arXiv:1110.4370; ADS:2013ApJ...763...18B | role=calibration | Halo-catalog and merger-tree consistency method for dark-matter simulations; not a hydrodynamic galaxy simulation or a direct halo-structure measurement.
[REV03-P012] | Gallazzi et al. (2005, MNRAS) | DOI:10.1111/j.1365-2966.2005.09321.x; arXiv:astro-ph/0506539; ADS:2005MNRAS.362...41G | role=measurement | Key observational benchmark for the stellar metallicity distribution in low-redshift galaxies.
[REV03-P013] | Tremonti et al. (2004, ApJ) | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=measurement | Established the definitive low-redshift gas-phase mass-metallicity relation scaling.
[REV03-P014] | Baldry et al. (2004, ApJ) | DOI:10.1086/380092; arXiv:astro-ph/0309710; ADS:2004ApJ...600..681B | role=measurement | Measured the robust structural separation between the star-forming blue cloud and quiescent red sequence.
[REV03-P015] | Bower et al. (2006, MNRAS) | DOI:10.1111/j.1365-2966.2006.10519.x; arXiv:astro-ph/0511338; ADS:2006MNRAS.370..645B | role=semi_analytic_model | Demonstrated that radio-mode AGN feedback quenches cooling flows to match the bright-end luminosity function.
[REV03-P016] | Cox et al. (2006, MNRAS) | DOI:10.1111/j.1365-2966.2006.11107.x; arXiv:astro-ph/0503201; ADS:2006MNRAS.373.1013C | role=hydrodynamic_simulation | Modeled merger-driven starbursts and the necessary dissipation scales for feedback.
[REV03-P017] | Arrigoni et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2009.15924.x; arXiv:0905.4189; ADS:2010MNRAS.402..173A | role=semi_analytic_model | Assessed chemical abundance ratio constraints within hierarchical semi-analytic models.
[REV03-P018] | Peeples & Shankar (2011, MNRAS) | DOI:10.1111/j.1365-2966.2011.19456.x; arXiv:1007.3743; ADS:2011MNRAS.417.2962P | role=empirical_inference | Constrained metal expulsion efficiency and mass-loading factors from the MZR.
[REV03-P019] | Gnedin & Kravtsov (2011, ApJ) | DOI:10.1088/0004-637X/728/2/88; arXiv:1004.0003; ADS:2011ApJ...728...88G | role=hydrodynamic_simulation | Simulation study of environmental dependence in the Kennicutt-Schmidt relation; do not use as the Gnedin-Kravtsov molecular-shielding prescription paper.
[REV03-P020] | Springel (2010, MNRAS) | DOI:10.1111/j.1365-2966.2009.15715.x; arXiv:0901.4107; ADS:2010MNRAS.401..791S | role=hydrodynamic_simulation | Introduced the moving-mesh architecture resolving critical limitations in standard SPH contact discontinuities.
[REV03-P021] | Ceverino et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.16433.x; arXiv:0907.3271; ADS:2010MNRAS.404.2151C | role=hydrodynamic_simulation | Simulated violent disk instabilities producing giant star-forming clumps at high redshift.
[REV03-P022] | Barro et al. (2013, ApJ) | DOI:10.1088/0004-637X/765/2/104; arXiv:1206.5000; ADS:2013ApJ...765..104B | role=measurement | Observed the morphological transition and extreme compactness of high-z quiescent galaxies.
[REV03-P023] | Bell et al. (2012, ApJ) | DOI:10.1088/0004-637X/753/2/167; arXiv:1110.3786; ADS:2012ApJ...753..167B | role=measurement | CANDELS morphology comparison of star-forming and quiescent galaxies to z~2; morphology alone does not identify the quenching mechanism.
[REV03-P024] | Agertz et al. (2007, MNRAS) | DOI:10.1111/j.1365-2966.2007.12183.x; arXiv:astro-ph/0610051; ADS:2007MNRAS.380..963A | role=hydrodynamic_simulation | Demonstrated catastrophic artificial surface tension in SPH resolving multi-phase fluid instabilities.
[REV03-P025] | Baugh (2006, RPPh) | DOI:10.1088/0034-4885/69/12/R02; arXiv:astro-ph/0610031; ADS:2006RPPh...69.3101B | role=semi_analytic_model | Outlined the base mathematical scaffolding linking dark matter assembly to SAM prescriptions.
[REV03-P026] | Birnboim & Dekel (2003, MNRAS) | DOI:10.1046/j.1365-8711.2003.06955.x; arXiv:astro-ph/0302161; ADS:2003MNRAS.345..349B | role=analytic_theory | Mathematically established the mass threshold for shock heating over smooth cold flows.
[REV03-P027] | Boylan-Kolchin et al. (2011, MNRAS) | DOI:10.1111/j.1745-3933.2011.01074.x; arXiv:1103.0007; ADS:2011MNRAS.415L..40B | role=hydrodynamic_simulation | Highlighted tensions between N-body dark matter substructure kinematics and observed satellites.
[REV03-P028] | Barnes & Hut (1986, Nature) | DOI:10.1038/324446a0; arXiv:none; ADS:1986Natur.324..446B | role=analytic_theory | Foundational tree-code algorithm establishing scalable N-body gravity solvers.
[REV03-P029] | Barnes (1988, ApJ) | DOI:10.1086/166593; arXiv:none; ADS:1988ApJ...331..699B | role=hydrodynamic_simulation | Early demonstration of violent relaxation in mergers destroying disks and creating spheroids.
[REV03-P030] | Barnes (1992, ApJ) | DOI:10.1086/171522; arXiv:none; ADS:1992ApJ...393..484B | role=hydrodynamic_simulation | Demonstrated phase mixing and angular momentum transfer to dark matter during mergers.
[REV03-P031] | Baugh et al. (2005, MNRAS) | DOI:10.1111/j.1365-2966.2004.08553.x; arXiv:astro-ph/0406069; ADS:2005MNRAS.356.1191B | role=semi_analytic_model | Required drastic IMF modifications in SAMs to match high-redshift starbursts.
[REV03-P032] | Behroozi et al. (2010, ApJ) | DOI:10.1088/0004-637X/717/1/379; arXiv:1001.0015; ADS:2010ApJ...717..379B | role=empirical_inference | Systematic uncertainty analysis for stellar-mass-to-halo-mass inference over 0<z<4; not a toy-cosmology guide.
[REV03-P033] | Bell et al. (2004, ApJ) | DOI:10.1086/420778; arXiv:astro-ph/0303394; ADS:2004ApJ...608..752B | role=measurement | Quantified the persistent mass build-up on the quiescent red sequence over cosmic time.
[REV03-P034] | Bender et al. (1992, ApJ) | DOI:10.1086/171940; arXiv:none; ADS:1992ApJ...399..462B | role=measurement | Observed structural properties of dynamically hot galaxies; not a generic velocity-kinematics census of all ellipticals.
[REV03-P035] | Benson (2010, PhR) | DOI:10.1016/j.physrep.2010.06.001; arXiv:1006.5394; ADS:2010PhR...495...33B | role=review_synthesis | Broad theoretical framing of the ΛCDM hierarchical components used by models.
[REV03-P036] | Benson et al. (2007, MNRAS) | DOI:10.1111/j.1365-2966.2007.11923.x; arXiv:astro-ph/0612719; ADS:2007MNRAS.379..841B | role=semi_analytic_model | Local disc/spheroid luminosity and stellar-mass functions from decomposed SDSS galaxies; do not use as a dwarf-demographics feedback experiment.
[REV03-P037] | Blanton & Moustakas (2009, ARA&A) | DOI:10.1146/annurev-astro-082708-101734; arXiv:0908.3017; ADS:2009ARA&A..47..159B | role=review_synthesis | Standard reference for the local galaxy distribution functions and structural metrics.
[REV03-P038] | Blitz & Rosolowsky (2004, ApJ) | DOI:10.1086/424661; arXiv:astro-ph/0407492; ADS:2004ApJ...612L..29B | role=empirical_inference | Pressure-based giant-molecular-cloud formation relation in nearby galaxies; bounded empirical partition recipe.
[REV03-P039] | Blumenthal et al. (1984, Nature) | DOI:10.1038/311517a0; arXiv:none; ADS:1984Natur.311..517B | role=analytic_theory | Foundational cosmology paper establishing cold dark matter clustering behavior.
[REV03-P042] | Schechter (1976, ApJ) | DOI:10.1086/154079; arXiv:none; ADS:1976ApJ...203..297S | role=measurement | Developed the asymptotic mathematical fit for the galaxy mass/luminosity distribution function.
[REV03-P043] | Conroy (2013, ARA&A) | DOI:10.1146/annurev-astro-082812-141017; arXiv:1301.7095; ADS:2013ARA&A..51..393C | role=review_synthesis | Benchmark for translating physical simulation stellar parameters into observable SED photometry.
[REV03-P045] | Krumholz et al. (2012, ApJ) | DOI:10.1088/0004-637X/745/1/69; arXiv:1109.4150; ADS:2012ApJ...745...69K | role=analytic_theory | Cross-environment local star-formation-law model; universality is model-bounded rather than a parameter-free empirical fact.
[REV03-P046] | Croton et al. (2006, MNRAS) | DOI:10.1111/j.1365-2966.2005.09675.x; arXiv:astro-ph/0508046; ADS:2006MNRAS.365...11C | role=semi_analytic_model | Contemporaneous with Bower 2006, established "radio mode" AGN feedback as the critical quenching parameter.
[REV03-P047] | Noeske et al. (2007, ApJ) | DOI:10.1086/517926; arXiv:astro-ph/0701924; ADS:2007ApJ...660L..43N | role=measurement | Coined and defined the "Star Forming Main Sequence" against which models calibrate sustained growth.
[REV03-P048] | Mo et al. (1998, MNRAS) | DOI:10.1046/j.1365-8711.1998.01227.x; arXiv:astro-ph/9707093; ADS:1998MNRAS.295..319M | role=analytic_theory | Established the isothermal density profile scaling relations connecting dark halo properties to disk sizes.
[REV03-P049] | Dalla Vecchia & Schaye (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.13322.x; arXiv:0801.2770; ADS:2008MNRAS.387.1431D | role=hydrodynamic_simulation | Outlined the temporary hydrodynamic decoupling mechanism required to prevent instantaneous wind thermalization.
[REV03-P050] | Governato et al. (2010, Nature) | DOI:10.1038/nature08640; arXiv:0911.2237; ADS:2010Natur.463..203G | role=hydrodynamic_simulation | Showed that powerful winds can reshape dark matter profiles and prevent massive bulge overcooling.
[REV03-P051] | Fontanot et al. (2009, MNRAS) | DOI:10.1111/j.1365-2966.2009.15058.x; arXiv:0901.1130; ADS:2009MNRAS.397.1776F | role=semi_analytic_model | Exposed the persistent failure of calibrated SAMs to reproduce the "downsizing" of massive galaxies at high redshift.
[REV03-P053] | Wuyts et al. (2011, ApJ) | DOI:10.1088/0004-637X/742/2/96; arXiv:1107.0317; ADS:2011ApJ...742...96W | role=measurement | Linked structural indices (Sersic) directly to positions on the Star-Forming Main Sequence.
[REV03-P054] | van der Wel et al. (2014, ApJ) | DOI:10.1088/0004-637X/788/1/28; arXiv:1404.2844; ADS:2014ApJ...788...28V | role=measurement | Comprehensive empirical benchmark for the size evolution of disk and spheroidal galaxies over 10 billion years.
[REV03-P055] | Muzzin et al. (2013, ApJ) | DOI:10.1088/0004-637X/777/1/18; arXiv:1303.4409; ADS:2013ApJ...777...18M | role=measurement | Pushed the bimodal mass function demographic baseline out to z=4.

REVIEW_BASE_03_DR_COMPLETE_REFERENCE_ONLY

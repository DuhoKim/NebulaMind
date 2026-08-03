# Review Base 01 verified source packet — Kennicutt & Evans 2012

status: READY_FOR_HWAO_REVIEW
advisory_only: true
canonical_packet_released: true
wiki_write_performed_by_tori: false
conversation_deleted: false

Review: Robert C. Kennicutt Jr. & Neal J. Evans II (2012), *Star Formation in the Milky Way and Nearby Galaxies*, ARA&A 50, 531-608.
Verified review identity: DOI `10.1146/annurev-astro-081811-125610`; arXiv `1204.3552`; ADS `2012ARA&A..50..531K`.
Raw-custody packet: `area_review_01_kennicutt_evans_2012_DR_RAW_PACKET.md`
Composite registry: `area_review_01_kennicutt_evans_2012_CURATED_SOURCE_REGISTRY.json`
Verification status: PASS — 43/43 physical primary rows; 25 raw composite rows corrected; 20 phantom source keys quarantined.
Method: authoritative review bibliography membership via Crossref structured references and the NED review reference page; exact source identity via public ADS abstract route/title, Crossref DOI record, and arXiv export metadata. Hwao's ADS API verifier and jury remain the live-wiki gate.

## 1. Review identity and scope map

[REV01-S01] SFR indicators and calibrations | Supports review-era FUV/NUV, recombination-line, IR, radio, X-ray, and hybrid calibrations with explicit IMF, star-formation-history, metallicity, dust, cirrus, leakage, and stochastic-sampling boundaries. Does not support treating one conversion as universal.

[REV01-S02] Gas inventories and mass tracers | Supports bounded use of HI, CO-derived H2, dust extinction/emission, gamma rays, and dense-gas tracers. Does not support conflating HI, H2, total gas, CO-bright gas, CO-dark gas, or dense gas.

[REV01-S03] Milky Way clouds and nearby galaxies | Connects YSO-counting and cloud-scale measurements to resolved and global galaxy relations. Spatial scales, apertures, tracers, and averaging must remain explicit.

[REV01-S04] Star-formation laws | Supports integrated total-gas, resolved molecular, low-density/HI-dominated, and dense-gas relations as distinct empirical regimes. It does not establish one scale-free universal power law.

[REV01-S05] Efficiencies and timescales | Supports instantaneous depletion-time and efficiency ratios under stated assumptions. It does not make depletion time a guaranteed future exhaustion clock.

[REV01-S06] Theory interface | Reviews gravity, turbulence, chemistry, free-fall scaling, and feedback interpretations. Models demonstrate mechanisms or reproduce relations; they do not by themselves establish observational prevalence.

[REV01-S07] Temporal boundary | The packet represents the review's 2012 status. Post-2012 ALMA/JWST results, later IMF claims, and subsequent calibrations require separate source packets and must not be back-projected into this review.

## 2. Established findings

[REV01-E01]
role: established
epistemic_type: observation
finding: Disk-averaged total-gas measurements spanning normal spirals and starbursts yield a super-linear global Schmidt relation, with the foundational combined fit near index 1.4.
scope/boundary: Integrated HI+H2 surface density and integrated SFR indicators; the fitted slope depends on sample mixing, aperture, regression, and CO-to-H2 conversion. It is not the resolved molecular-only law.
review_basis: Section 6.1 and Figure 11.
trust_score: 0.96
sources: [REV01, REV01-P001, REV01-P003]

[REV01-E02]
role: established
epistemic_type: observation
finding: Integrated infrared luminosity correlates approximately linearly with HCN(1-0) luminosity across galaxies, and the relation extends toward massive Milky Way clumps.
scope/boundary: HCN luminosity is a dense-gas proxy whose excitation, abundance, optical depth, and conversion to mass can vary. Linearity does not prove a universal dense-gas SFE or one causal unit of star formation.
review_basis: Section 6.1.
trust_score: 0.89
sources: [REV01, REV01-P005, REV01-P006]

[REV01-E03]
role: established
epistemic_type: observation
finding: In nearby normal disks at roughly sub-kiloparsec to kiloparsec resolution, SFR surface density correlates more closely with CO-traced molecular gas than with HI surface density.
scope/boundary: Main optical disks in THINGS/HERACLES-related samples; standard CO conversion and UV+IR SFR tracers. Correlation does not prove that H2 chemistry is causally required for collapse.
review_basis: Section 6.3 and Figure 12.
trust_score: 0.94
sources: [REV01, REV01-P007, REV01-P008]

[REV01-E04]
role: established
epistemic_type: observation
finding: Nearby resolved samples commonly show HI surface-density saturation near roughly 9-10 solar masses per square parsec and much lower star-formation efficiency in HI-dominated outer disks.
scope/boundary: Empirical local-sample scale, not a hard universal ceiling; metallicity, shielding, opacity, inclination, and resolution matter.
review_basis: Sections 6.3 and 7.1.
trust_score: 0.90
sources: [REV01, REV01-P007, REV01-P011, REV01-P043]

[REV01-E05]
role: established
epistemic_type: calibration
finding: The review updates commonly used SFR conversions to a Kroupa IMF and modern population synthesis, producing lower inferred SFRs than older Salpeter-IMF calibrations for the same luminosity.
scope/boundary: Continuous-SFR assumptions and tracer-specific response times; metallicity, dust, leakage, cirrus, and IMF sampling remain systematic limits.
review_basis: Section 3.8 and Table 1.
trust_score: 0.95
sources: [REV01, REV01-P015, REV01-P016, REV01-P017, REV01-P018]

[REV01-E06]
role: established
epistemic_type: observation
finding: Nearby molecular clouds form stars inefficiently when their recent YSO-counted SFR is compared with total cloud mass, free-fall time, and crossing time.
scope/boundary: Local Spitzer cloud samples and approximately two-million-year YSO census windows. Cloud selection, lifetime, dense-gas definition, and SFR timescale prevent direct substitution into galaxy-integrated relations.
review_basis: Sections 4.3-4.4.
trust_score: 0.91
sources: [REV01, REV01-P012, REV01-P014]

[REV01-E07]
role: established
epistemic_type: observation
finding: Within nearby clouds, recent star formation is concentrated toward high-extinction, high-column-density material, and total SFR correlates more closely with mass above a dense threshold than with total cloud mass.
scope/boundary: Extinction-selected local clouds; threshold values depend on dust conversion, geometry, completeness, and YSO timescale. This is not proof of a universal sharp physical threshold.
review_basis: Sections 4.4 and 7.1.3.
trust_score: 0.88
sources: [REV01, REV01-P012, REV01-P013]

[REV01-E08]
role: established
epistemic_type: calibration
finding: CO-to-H2 conversion is environment-dependent because CO chemistry, excitation, optical depth, cloud structure, metallicity, radiation field, temperature, and dynamics vary.
scope/boundary: Diffuse gas, normal disks, low-metallicity systems, dense centers, and starbursts cannot be represented safely by one unqualified conversion factor.
review_basis: Section 2.4.
trust_score: 0.94
sources: [REV01, REV01-P028, REV01-P030, REV01-P034, REV01-P035, REV01-P036, REV01-P037, REV01-P038, REV01-P039]

[REV01-E09]
role: established
epistemic_type: observation
finding: Gamma-ray and dust analyses reveal gas not adequately traced by standard HI and CO maps, including CO-faint molecular envelopes.
scope/boundary: Local Milky Way regions and tracer-model assumptions. The evidence does not justify assigning one universal dark-gas fraction or treating all excess material as H2.
review_basis: Section 2.4.
trust_score: 0.87
sources: [REV01, REV01-P020]

[REV01-E10]
role: established
epistemic_type: calibration
finding: Conversions between extinction or reddening and gas column depend on dust properties and metallicity and differ between the Milky Way, LMC, and SMC.
scope/boundary: Diffuse sightlines and adopted extinction curves; dense-cloud grain evolution and emission opacity require separate calibration.
review_basis: Section 2.3.
trust_score: 0.92
sources: [REV01, REV01-P025, REV01-P026]

[REV01-E11]
role: established
epistemic_type: observation
finding: Star-formation relations depend on spatial averaging; resolved measurements expose environmental and evolutionary scatter hidden by whole-galaxy averages.
scope/boundary: Nearby-galaxy integral-field, CO, HI, UV, and IR mapping. The exact breakdown scale was not fixed in 2012.
review_basis: Sections 6.2-6.3.
trust_score: 0.86
sources: [REV01, REV01-P007, REV01-P008, REV01-P041, REV01-P042]

[REV01-E12]
role: established
epistemic_type: review_synthesis
finding: The review organizes galaxy-scale star formation into low-density HI-dominated, normal molecular-disk, and high-density starburst regimes with differing empirical efficiencies and dominant systematics.
scope/boundary: A useful 2012 synthesis, not three immutable physical classes or exact universal surface-density boundaries.
review_basis: Section 7.1 and Table 3.
trust_score: 0.87
sources: [REV01, REV01-P003, REV01-P011, REV01-P040]

## 3. Open debates and tensions

[REV01-D01]
role: debate
debate_topic: Discrete disk/starburst sequences versus a continuous star-formation law.
competing_positions: High-redshift disks and starbursts were presented as offset sequences; continuous environmental changes in CO conversion and dynamical state can reduce apparent bimodality.
why_unresolved_2012: Gas masses, excitation, conversion factors, geometry, and targeted selection covaried.
boundary: Integrated high-redshift and local samples, not resolved cloud physics.
trust_score: 0.84
sources: [REV01, REV01-P009, REV01-P010, REV01-P038]

[REV01-D02]
role: debate
debate_topic: Long-lived supported molecular clouds versus rapidly evolving turbulent clouds.
competing_positions: Slow star formation can reflect support/regulation over many dynamical times; turbulent assembly and disruption can make clouds transient while ensemble depletion times remain long.
why_unresolved_2012: Gas assembly lacks a direct clock, YSO ages sample only the stellar phase, and simulations depend on feedback, magnetic fields, and cloud definitions.
boundary: Milky Way cloud demographics and models; not galaxy-integrated depletion time.
trust_score: 0.76
sources: [REV01, REV01-P014, REV01-P036, REV01-P040]

[REV01-D03]
role: debate
debate_topic: Chemical shielding transition versus gravitational/dynamical threshold in outer disks.
competing_positions: Low SFE may follow failure to form shielded molecular gas, or large-scale disk stability and low midplane pressure may inhibit collapse.
why_unresolved_2012: Column density, metallicity, stellar density, pressure, and galactocentric radius covary.
boundary: Local outer disks, low-surface-brightness systems, and model interpretations.
trust_score: 0.79
sources: [REV01, REV01-P011, REV01-P040, REV01-P043]

[REV01-D04]
role: debate
debate_topic: Which tracer provides the least biased molecular-gas mass.
competing_positions: CO luminosity is practical and empirically calibrated; dust, gamma rays, isotopologues, and chemistry models expose CO-faint gas and environment-dependent conversion.
why_unresolved_2012: Every alternative inherits dust, cosmic-ray, abundance, excitation, geometry, or radiative-transfer assumptions.
boundary: Separate diffuse Milky Way gas, dense cores, nearby galaxies, low metallicity, and starbursts.
trust_score: 0.90
sources: [REV01, REV01-P020, REV01-P024, REV01-P025, REV01-P028, REV01-P030, REV01-P034, REV01-P035, REV01-P036, REV01-P037, REV01-P038, REV01-P039]

[REV01-D05]
role: debate
debate_topic: Constant versus environment-dependent efficiency per free-fall time.
competing_positions: Unified models use a low approximately constant efficiency per free-fall time; cloud and galaxy measurements can imply changes with density, tracer, or regime.
why_unresolved_2012: Volume density, geometry, cloud boundaries, dense-gas conversion, and SFR averaging timescale are uncertain.
boundary: Do not compare local dense clumps directly with disk-averaged surface densities without a scale model.
trust_score: 0.77
sources: [REV01, REV01-P012, REV01-P014, REV01-P040]

[REV01-D06]
role: debate
debate_topic: Whether the IR-HCN relation reflects a universal dense-gas SFE.
competing_positions: Approximate linearity can indicate proportional star formation per dense-gas proxy; it can also arise from tracer excitation, selection, abundance, or changing dense-gas fraction.
why_unresolved_2012: HCN was faint outside bright clumps and galaxy centers, and dense-gas mass conversion was poorly constrained.
boundary: Integrated galaxies and massive Milky Way clumps; not all molecular gas.
trust_score: 0.79
sources: [REV01, REV01-P005, REV01-P006, REV01-P012, REV01-P027]

[REV01-D07]
role: debate
debate_topic: A single global power law versus scale- and phase-dependent relations.
competing_positions: Whole-galaxy total-gas data give a compact super-linear law; resolved molecular data are closer to linear and low-density HI-dominated regions fall below simple extrapolations.
why_unresolved_2012: Gas phase, spatial scale, diffuse emission, selection, regression, and conversion factor differ across studies.
boundary: Keep integrated total gas, resolved H2, and outer-disk HI distinct.
trust_score: 0.93
sources: [REV01, REV01-P003, REV01-P007, REV01-P008, REV01-P011, REV01-P041, REV01-P042, REV01-P043]

[REV01-D08]
role: debate
debate_topic: Whether H2 is causally necessary for star formation or mainly co-locates with shielded cold gas.
competing_positions: Observed SFR-H2 correlation motivates a precursor interpretation; chemistry/turbulence models allow molecule formation and gravitational collapse to share environmental causes.
why_unresolved_2012: The decisive tests require low-metallicity regimes where molecular-formation and dynamical times separate, with reliable CO-dark gas accounting.
boundary: Correlation does not determine causal direction.
trust_score: 0.74
sources: [REV01, REV01-P008, REV01-P036, REV01-P039, REV01-P040]

## 4. Key measurements and calibrations

[REV01-N01]
role: measurement
metric: Review Table 1 Kroupa-IMF SFR constants.
value: log Cx values include FUV 43.35, NUV 43.17, H-alpha 41.27, TIR 43.41, 24-micron 42.69, 70-micron 43.23, 1.4-GHz 28.20, and 2-10-keV 39.77 in the review's stated luminosity units.
boundary: Tracer response times and continuous-SFR assumptions differ; dust, metallicity, cirrus, leakage, binaries, and IMF sampling matter.
trust_score: 0.94
sources: [REV01, REV01-P015, REV01-P016, REV01-P017, REV01-P018, REV01-P019]

[REV01-N02]
role: measurement
metric: Global total-gas Schmidt exponent.
value: Approximately N=1.4 in the foundational combined normal-disk plus starburst fit.
boundary: Disk averages, total gas, legacy SFR scale, and adopted CO conversion; not a resolved H2-only exponent.
trust_score: 0.96
sources: [REV01, REV01-P003]

[REV01-N03]
role: measurement
metric: Nearby-disk molecular depletion time.
value: Roughly 1-2 Gyr under standard CO-to-H2 and UV+IR calibrations.
boundary: Sub-kiloparsec/kiloparsec normal-disk averages; conversion factor, centers, starbursts, and low metallicity differ; not a future exhaustion clock.
trust_score: 0.91
sources: [REV01, REV01-P007, REV01-P008]

[REV01-N04]
role: measurement
metric: Nearby-cloud recent depletion time.
value: Approximately 82 Myr for the c2d cloud sample, compared in the review with mean free-fall time about 1.4 Myr and crossing time about 5.5 Myr.
boundary: YSO-counted recent SFR, selected local clouds, and review definitions; not directly comparable to galaxy-wide CO depletion time.
trust_score: 0.88
sources: [REV01, REV01-P014]

[REV01-N05]
role: measurement
metric: Characteristic resolved HI saturation scale.
value: Approximately 9-10 solar masses per square parsec in the cited nearby samples.
boundary: Empirical characteristic scale, not a strict universal maximum.
trust_score: 0.89
sources: [REV01, REV01-P007, REV01-P011]

[REV01-N06]
role: measurement
metric: Integrated dense-gas relation.
value: IR luminosity versus HCN(1-0) luminosity is approximately linear over the cited galaxy/clump range.
boundary: HCN luminosity is not an environment-invariant dense-gas mass; the result does not establish universal dense-gas SFE.
trust_score: 0.87
sources: [REV01, REV01-P005, REV01-P006]

[REV01-N07]
role: measurement
metric: Standard Milky-Way CO-to-H2 factor used by the review.
value: X_CO approximately 2.3e20 H2 molecules per square centimeter per K km s^-1.
boundary: Review-era standard with order-unity cloud-scale uncertainty and strong environmental failure modes.
trust_score: 0.89
sources: [REV01, REV01-P028, REV01-P030, REV01-P037, REV01-P038]

[REV01-N08]
role: measurement
metric: Diffuse Milky-Way gas-to-reddening ratio.
value: N(HI)+2N(H2) approximately 5.8e21 cm^-2 E(B-V)^-1.
boundary: Diffuse solar-neighborhood sightlines and standard extinction; dense clouds and low-metallicity systems differ.
trust_score: 0.94
sources: [REV01, REV01-P025]

## 5. What remained unknown in 2012

[REV01-U01]
role: future
gap: The scale and physical cause of star-formation-law decorrelation below kiloparsec averaging.
needed: Matched cloud-scale gas, young-star, and feedback mapping with temporal modeling.
trust_score: 0.84
sources: [REV01, REV01-P007, REV01-P041, REV01-P042]

[REV01-U02]
role: future
gap: The amount and environmental distribution of CO-dark gas and the calibration of CO-independent mass tracers.
needed: Joint gamma-ray, dust, [CII], isotopologue, and metallicity constraints.
trust_score: 0.85
sources: [REV01, REV01-P020, REV01-P035, REV01-P038]

[REV01-U03]
role: future
gap: Whether high-redshift disks and starbursts truly occupy separate star-formation sequences.
needed: Resolved multi-transition gas imaging, dynamical masses, and continuous conversion-factor calibration.
trust_score: 0.78
sources: [REV01, REV01-P009, REV01-P010, REV01-P038]

[REV01-U04]
role: future
gap: Molecular-cloud assembly, lifetime, fragmentation, and disruption chronology.
needed: Cloud population time-ordering, magnetic/turbulent structure, dense-core mapping, and feedback-coupled simulations.
trust_score: 0.78
sources: [REV01, REV01-P014, REV01-P027, REV01-P036, REV01-P040]

[REV01-U05]
role: future
gap: Star formation and gas-mass calibration in very low-metallicity and HI-dominated systems.
needed: CO-dark-gas accounting plus dust, [CII], HI, young-star, and chemistry measurements across metallicity.
trust_score: 0.81
sources: [REV01, REV01-P039, REV01-P043]

[REV01-U06]
role: future
gap: Separating true low-SFR thresholds from tracer response time and stochastic high-mass-star sampling.
needed: Probabilistic population synthesis and matched UV, recombination-line, IR, and resolved stellar-population data.
trust_score: 0.80
sources: [REV01, REV01-P015, REV01-P016, REV01-P017, REV01-P018, REV01-P043]

## 6. Primary-citation harvest

[REV01-P001] Schmidt (1959, ApJ) | title=The Rate of Star Formation | DOI:10.1086/146614; arXiv:none; ADS:1959ApJ...129..243S | role=theory | review_locator=Section 6.1 | First theoretical proposition of a power-law relationship between gas density and star formation rate.
[REV01-P002] Schmidt (1963, ApJ) | title=The Rate of Star Formation. II. The Rate of Formation of Stars of Different Mass | DOI:10.1086/147553; arXiv:none; ADS:1963ApJ...137..758S | role=theory | review_locator=Section 6.1 | Expansion of the power-law parameterization of the star formation rate to account for stellar mass distributions.
[REV01-P003] Kennicutt (1998, ApJ) | title=The Global Schmidt Law in Star-forming Galaxies | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=measurement | review_locator=Section 6.1 | Established the benchmark integrated non-linear scaling law (N~1.4) between total gas and SFR surface density.
[REV01-P004] Kennicutt (1998, ARA&A) | title=Star Formation in Galaxies Along the Hubble Sequence | DOI:10.1146/annurev.astro.36.1.189; arXiv:astro-ph/9807187; ADS:1998ARA&A..36..189K | role=calibration | review_locator=Section 3.8 | The definitive pre-2012 compendium of standard multi-wavelength star formation rate calibrations based on a Salpeter IMF.
[REV01-P005] Gao & Solomon (2004, ApJ) | title=The Star Formation Rate and Dense Molecular Gas in Galaxies | DOI:10.1086/382999; arXiv:astro-ph/0310339; ADS:2004ApJ...606..271G | role=measurement | review_locator=Section 6.1 | Demonstrated a tight, linear global correlation between infrared luminosity (SFR) and HCN luminosity (dense gas).
[REV01-P006] Wu et al. (2005, ApJ) | title=Connecting Dense Gas Tracers of Star Formation in our Galaxy to High-z Star Formation | DOI:10.1086/499623; arXiv:astro-ph/0511424; ADS:2005ApJ...635L.173W | role=measurement | review_locator=Section 6.1 | Showed the linear dense gas (HCN) scaling relation extends down to individual massive star-forming clumps in the Milky Way.
[REV01-P007] Bigiel et al. (2008, AJ) | title=The Star Formation Law in Nearby Galaxies on Sub-Kpc Scales | DOI:10.1088/0004-6256/136/6/2846; arXiv:0810.2541; ADS:2008AJ....136.2846B | role=measurement | review_locator=Section 6.3 | First comprehensive sub-kiloparsec mapping revealing SFR correlates tightly with H2 but is uncorrelated with HI.
[REV01-P008] Leroy et al. (2008, AJ) | title=The Star Formation Efficiency in Nearby Galaxies: Measuring Where Gas Forms Stars Effectively | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=measurement | review_locator=Section 6.3 | Measured constant H2 depletion times (~2 Gyr) and investigated the environmental drivers of the HI-to-H2 phase transition.
[REV01-P009] Genzel et al. (2010, MNRAS) | title=A study of the gas-star formation relation over cosmic time | DOI:10.1111/j.1365-2966.2010.16969.x; arXiv:1003.5180; ADS:2010MNRAS.407.2091G | role=debate | review_locator=Section 6.1 | Proposed a bimodal star formation law separating high-redshift disks from highly efficient extreme starbursts.
[REV01-P010] Daddi et al. (2010, ApJ) | title=Different Star Formation Laws for Disks Versus Starbursts at Low and High Redshifts | DOI:10.1088/2041-8205/714/1/L118; arXiv:1003.3889; ADS:2010ApJ...714L.118D | role=debate | review_locator=Section 6.1 | Supported a bimodal KS law driven by distinct dynamical timescales and efficiencies in mergers versus secular disks.
[REV01-P011] Bigiel et al. (2010, AJ) | title=Extremely Inefficient Star Formation in the Outer Disks of Nearby Galaxies | DOI:10.1088/0004-6256/140/5/1194; arXiv:1007.3498; ADS:2010AJ....140.1194B | role=measurement | review_locator=Section 6.3 | Mapped the severe suppression of star formation efficiency in the HI-dominated, sub-threshold regimes of outer galactic disks.
[REV01-P012] Lada, Lombardi, & Alves (2010, ApJ) | title=On the Star Formation Rates in Molecular Clouds | DOI:10.1088/0004-637X/724/1/687; arXiv:1009.2985; ADS:2010ApJ...724..687L | role=measurement | review_locator=Section 4 | Demonstrated that star formation rates in local clouds scale directly with the mass of dense gas above a specific extinction threshold.
[REV01-P013] Heiderman et al. (2010, ApJ) | title=The Star Formation Rate and Gas Surface Density Relation in the Milky Way: Implications for Extragalactic Studies | DOI:10.1088/0004-637X/723/2/1019; arXiv:1009.1621; ADS:2010ApJ...723.1019H | role=measurement | review_locator=Section 4.4 | Found that essentially all truly young protostars in Perseus are highly concentrated within extinction contours of Av > 8 mag.
[REV01-P014] Evans et al. (2009, ApJS) | title=The Spitzer c2d Legacy Results: Star-Formation Rates and Efficiencies; Evolution and Lifetimes | DOI:10.1088/0067-0049/181/2/321; arXiv:0811.1059; ADS:2009ApJS..181..321E | role=measurement | review_locator=Section 4.3 | Derived local molecular cloud depletion times of ~82 Myr, vastly exceeding the theoretical free-fall times.
[REV01-P015] Murphy et al. (2011, ApJ) | title=Calibrating Extinction-free Star Formation Rate Diagnostics with 33 GHz Free-free Emission in NGC 6946 | DOI:10.1088/0004-637X/737/2/67; arXiv:1105.4877; ADS:2011ApJ...737...67M | role=calibration | review_locator=Table 1 | Provided updated Kroupa-IMF anchored SFR calibration constants for FUV, NUV, TIR, and 1.4 GHz emission.
[REV01-P016] Hao et al. (2011, ApJ) | title=Dust-corrected Star Formation Rates of Galaxies. II. Combinations of Ultraviolet and Infrared Tracers | DOI:10.1088/0004-637X/741/2/124; arXiv:1108.2837; ADS:2011ApJ...741..124H | role=calibration | review_locator=Table 1 | Developed modern hybrid composite calibrations utilizing UV/optical combined with mid-infrared dust emission.
[REV01-P017] Rieke et al. (2009, ApJ) | title=Determining Star Formation Rates for Infrared Galaxies | DOI:10.1088/0004-637X/692/1/556; arXiv:0810.4150; ADS:2009ApJ...692..556R | role=calibration | review_locator=Table 1 | Derived the updated calibration constant and metallicity dependencies for the 24 micron dust continuum SFR indicator.
[REV01-P018] Calzetti et al. (2010, ApJ) | title=The Calibration of Monochromatic Far-Infrared Star Formation Rate Indicators | DOI:10.1088/0004-637X/714/2/1256; arXiv:1003.0961; ADS:2010ApJ...714.1256C | role=calibration | review_locator=Table 1 | Derived the specific 70 micron calibration constant, mitigating the cirrus contamination issues prevalent at longer wavelengths.
[REV01-P019] Ranalli et al. (2003, A&A) | title=The 2-10 keV luminosity as a Star Formation Rate indicator | DOI:10.1051/0004-6361:20021600; arXiv:astro-ph/0211304; ADS:2003A&A...399...39R | role=calibration | review_locator=Table 1 | Established the foundational calibration relating hard X-ray emission (tracing high-mass X-ray binaries) to integrated SFR.
[REV01-P020] Abdo et al. (2010, ApJ) | title=Fermi Observations of Cassiopeia and Cepheus: Diffuse Gamma-ray Emission in the Outer Galaxy | DOI:10.1088/0004-637X/710/1/133; arXiv:0912.3618; ADS:2010ApJ...710..133A | role=measurement | review_locator=Section 2.4 | Utilized gamma-ray emission to map the "dark gas" phase in the outer Galaxy, validating variations in the CO-to-H2 factor.
[REV01-P021] Andre, Ward-Thompson, & Barsony (1993, ApJ) | title=Submillimeter continuum observations of Rho Ophiuchi A - The candidate protostar VLA 1623 and prestellar clumps | DOI:10.1086/172425; arXiv:none; ADS:1993ApJ...406..122A | role=measurement | review_locator=Section 4.4 | Early defining observation of deeply embedded Class 0 protostellar clumps mapping high-density star formation onset.
[REV01-P022] Alonso-Herrero et al. (2006, ApJ) | title=Near-Infrared and Star-forming Properties of Local Luminous Infrared Galaxies | DOI:10.1086/506958; arXiv:astro-ph/0606186; ADS:2006ApJ...650..835A | role=measurement | review_locator=Section 5.3 | Mapped the highly concentrated circumnuclear starburst morphologies characterizing local LIRGs and ULIRGs.
[REV01-P023] Beltran et al. (2006, A&A) | title=Search for massive protostar candidates in the southern hemisphere. II. Dust continuum emission | DOI:10.1051/0004-6361:20053999; arXiv:none; ADS:2006A&A...447..221B | role=measurement | review_locator=Section 2.4 | Identified scaling relations linking dense clump mass functions directly to the hierarchical formation of star clusters.
[REV01-P024] Draine (2003, ARA&A) | title=Interstellar Dust Grains | DOI:10.1146/annurev.astro.41.011802.094840; arXiv:astro-ph/0304489; ADS:2003ARA&A..41..241D | role=calibration | review_locator=Section 2.3 | Definitive baseline physics for interstellar dust grain sizes, compositions, and sub-millimeter opacities used in gas mass mapping.
[REV01-P025] Bohlin, Savage & Drake (1978, ApJ) | title=A survey of interstellar H I from L-alpha absorption measurements. II | DOI:10.1086/156357; arXiv:none; ADS:1978ApJ...224..132B | role=calibration | review_locator=Section 2.3 | Foundational calibration equating diffuse interstellar reddening E(B-V) to total hydrogen column density in the Milky Way.
[REV01-P026] Weingartner & Draine (2001, ApJ) | title=Dust Grain-Size Distributions and Extinction in the Milky Way, Large Magellanic Cloud, and Small Magellanic Cloud | DOI:10.1086/318651; arXiv:astro-ph/0008146; ADS:2001ApJ...548..296W | role=calibration | review_locator=Section 2.3 | Calibrated the severe variations in dust-to-gas ratios and extinction curves required for measuring gas in the LMC and SMC.
[REV01-P027] Shirley et al. (2003, ApJS) | title=A CS J=5-4 Mapping Survey Toward High-Mass Star-forming Cores Associated with Water Masers | DOI:10.1086/379147; arXiv:astro-ph/0308310; ADS:2003ApJS..149..375S | role=measurement | review_locator=Section 2.4 | Maps CS J=5-4 in high-mass star-forming cores; supports dense-gas structure, not a 350-micron dust-continuum survey.
[REV01-P028] Dickman (1978, ApJS) | title=The ratio of carbon monoxide to molecular hydrogen in interstellar dark clouds | DOI:10.1086/190535; arXiv:none; ADS:1978ApJS...37..407D | role=calibration | review_locator=Section 2.4 | Early benchmark mapping isotopic 13CO column densities against visual extinction to derive the fundamental X(CO) conversion logic.
[REV01-P029] Frerking, Langer & Wilson (1982, ApJ) | title=The relationship between carbon monoxide abundance and visual extinction in interstellar clouds | DOI:10.1086/160451; arXiv:none; ADS:1982ApJ...262..590F | role=calibration | review_locator=Section 2.4 | Constrained the breakdown of CO as a strict mass tracer in saturated dense cores.
[REV01-P030] Pineda et al. (2010, ApJ) | title=The Relation Between Gas and Dust in the Taurus Molecular Cloud | DOI:10.1088/0004-637X/721/1/686; arXiv:1007.5060; ADS:2010ApJ...721..686P | role=measurement | review_locator=Section 2.4 | Highly resolved mapping of the highly variable X(CO) factor within the Taurus cloud against visual extinction.
[REV01-P031] Lee et al. (2003, ApJ) | title=Chemistry and Dynamics in Pre-protostellar Cores | DOI:10.1086/345428; arXiv:astro-ph/0210330; ADS:2003ApJ...583..789L | role=caveat | review_locator=Section 2.4 | Supports dense-core chemistry, dynamics, and depletion effects under the exact ADS record and title.
[REV01-P032] Pontoppidan et al. (2008, ApJ) | title=The c2d Spitzer Spectroscopic Survey of Ices around Low-Mass Young Stellar Objects. II. CO2 | DOI:10.1086/533431; arXiv:0711.4616; ADS:2008ApJ...678.1005P | role=caveat | review_locator=Section 2.4 | Proved gas-phase CO converts heavily into CO2 ice in dense environments, breaking standard chemical mass assumptions.
[REV01-P033] Whittet et al. (2007, ApJ) | title=The Abundance of Carbon Dioxide Ice in the Quiescent Intracloud Medium | DOI:10.1086/509772; arXiv:none; ADS:2007ApJ...655..332W | role=caveat | review_locator=Section 2.4 | Quantified solid ice carbon depletion in intracloud mediums, placing fundamental limits on total gas mass derivations.
[REV01-P034] Goldsmith et al. (2008, ApJ) | title=Large-Scale Structure of the Molecular Gas in Taurus Revealed by High Linear Dynamic Range Spectral Line Mapping | DOI:10.1086/587166; arXiv:0802.2206; ADS:2008ApJ...680..428G | role=measurement | review_locator=Section 2.4 | Stacking analysis showing extreme X(CO) variation in diffuse molecular cloud envelopes versus dense cores.
[REV01-P035] Liszt, Pety & Lucas (2010, A&A) | title=The CO luminosity and CO-H2 conversion factor of diffuse ISM: does CO emission trace dense molecular gas? | DOI:10.1051/0004-6361/201014510; arXiv:1005.2157; ADS:2010A&A...518A..45L | role=debate | review_locator=Section 2.4 | Argument that X(CO) remains surprisingly constant in diffuse unbound gas, challenging standard cloud threshold definitions.
[REV01-P036] Glover et al. (2010, MNRAS) | title=Modelling CO formation in the turbulent interstellar medium | DOI:10.1111/j.1365-2966.2009.15718.x; arXiv:0907.4081; ADS:2010MNRAS.404....2G | role=theory | review_locator=Section 2.4 | Hydrodynamic simulations proving integrated CO can poorly correlate with true visual extinction in turbulent environments.
[REV01-P037] Dickman, Snell & Schloerb (1986, ApJ) | title=Carbon monoxide as an extragalactic mass tracer | DOI:10.1086/164604; arXiv:none; ADS:1986ApJ...309..326D | role=calibration | review_locator=Section 2.4 | Foundational extragalactic "cloud counting" logic to convert CO luminosity to total molecular mass.
[REV01-P038] Shetty et al. (2011, MNRAS) | title=Modelling CO emission - I. CO as a column density tracer and the X factor in molecular clouds | DOI:10.1111/j.1365-2966.2010.18005.x; arXiv:1011.2019; ADS:2011MNRAS.412.1686S | role=theory | review_locator=Section 2.4 | Derived the theoretical scaling relations for X(CO) against gas density and intense radiation environments.
[REV01-P039] Maloney & Black (1988, ApJ) | title=CO/N(H2) Conversions and Molecular Gas Abundances in Spiral and Irregular Galaxies | DOI:10.1086/166011; arXiv:none; ADS:1988ApJ...325..389M | role=theory | review_locator=Section 2.4 | Models CO-to-H2 conversion and molecular-gas abundance in spiral and irregular galaxies; retain metallicity and radiation-field limits.
[REV01-P040] Krumholz, Dekel & McKee (2012, ApJ) | title=A Universal, Local Star Formation Law in Galactic Clouds, Nearby Galaxies, High-redshift Disks, and Starbursts | DOI:10.1088/0004-637X/745/1/69; arXiv:1109.4150; ADS:2012ApJ...745...69K | role=theory | review_locator=Section 6 | Theoretical model attempting to unify disparate KS laws through local free-fall scaling across all environments.
[REV01-P041] Blanc et al. (2009, ApJ) | title=The Spatially Resolved Star Formation Law From Integral Field Spectroscopy: VIRUS-P Observations of NGC 5194 | DOI:10.1088/0004-637X/704/1/842; arXiv:0908.2810; ADS:2009ApJ...704..842B | role=measurement | review_locator=Section 6.3 | Integral field spectroscopy mapping confirming the steep non-linear break in the sub-kpc star formation law at low gas densities.
[REV01-P042] Schruba et al. (2011, AJ) | title=A Molecular Star Formation Law in the Atomic-gas-dominated Edge of M33 | DOI:10.1088/0004-6256/142/2/37; arXiv:1105.4605; ADS:2011AJ....142...37S | role=measurement | review_locator=Section 6.3 | Deep stacking showing tight SFR-to-H2 coupling persists even in atomic-dominated outer edges.
[REV01-P043] Wyder et al. (2009, ApJ) | title=The Star Formation Law at Low Surface Density | DOI:10.1088/0004-637X/696/2/1834; arXiv:0903.3015; ADS:2009ApJ...696.1834W | role=measurement | review_locator=Section 6.3 | Empirical mapping of extreme inefficiency in the deeply sub-threshold environments of UV-extended disks.

## 7. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | raw REV01-P002 tuple: title=The Rate of Star Formation. II. The Rate of Formation of Stars of Different Mass; DOI=10.1086/147556; arXiv=none; ADS=1963ApJ...137..758S | cross-wired fields=doi | use only corrected canonical row with DOI=10.1086/147553; arXiv=none; ADS=1963ApJ...137..758S
UNCITED_NOT_USABLE | raw REV01-P006 tuple: title=Connecting Dense Gas Tracers of Star Formation in our Galaxy to High-z Star Formation; DOI=10.1086/499831; arXiv=astro-ph/0511412; ADS=2005ApJ...635L.173W | cross-wired fields=doi,arxiv | use only corrected canonical row with DOI=10.1086/499623; arXiv=astro-ph/0511424; ADS=2005ApJ...635L.173W
UNCITED_NOT_USABLE | raw REV01-P009 tuple: title=A study of the gas-star formation relation in z~1-3 massive star-forming galaxies; DOI=10.1111/j.1365-2966.2010.16969.x; arXiv=1003.5180; ADS=2010MNRAS.407.2091G | cross-wired fields=title | use only corrected canonical row with DOI=10.1111/j.1365-2966.2010.16969.x; arXiv=1003.5180; ADS=2010MNRAS.407.2091G
UNCITED_NOT_USABLE | raw REV01-P010 tuple: title=Different Star Formation Laws for Disks Versus Starbursts at Low and High Redshifts; DOI=10.1088/2041-8205/714/1/L118; arXiv=1003.5204; ADS=2010ApJ...714L.118D | cross-wired fields=arxiv | use only corrected canonical row with DOI=10.1088/2041-8205/714/1/L118; arXiv=1003.3889; ADS=2010ApJ...714L.118D
UNCITED_NOT_USABLE | raw REV01-P013 tuple: title=The Star Formation Rate and Gas Surface Density Relation in the Milky Way: Implications for Extragalactic Studies; DOI=10.1088/0004-637X/723/2/1019; arXiv=1009.2498; ADS=2010ApJ...723.1019H | cross-wired fields=arxiv | use only corrected canonical row with DOI=10.1088/0004-637X/723/2/1019; arXiv=1009.1621; ADS=2010ApJ...723.1019H
UNCITED_NOT_USABLE | raw REV01-P014 tuple: title=The Spitzer c2d Legacy Results: Star-Formation Rates and Efficiencies; Evolution and Lifetimes; DOI=10.1088/0067-0049/181/2/321; arXiv=0901.1656; ADS=2009ApJS..181..321E | cross-wired fields=arxiv | use only corrected canonical row with DOI=10.1088/0067-0049/181/2/321; arXiv=0811.1059; ADS=2009ApJS..181..321E
UNCITED_NOT_USABLE | raw REV01-P018 tuple: title=The Calibration of Mid-Infrared Star Formation Rate Indicators; DOI=10.1088/0004-637X/714/2/1256; arXiv=1003.1731; ADS=2010ApJ...714.1256C | cross-wired fields=title,arxiv | use only corrected canonical row with DOI=10.1088/0004-637X/714/2/1256; arXiv=1003.0961; ADS=2010ApJ...714.1256C
UNCITED_NOT_USABLE | raw REV01-P019 tuple: title=The 2-10 keV luminosity as a Star Formation Rate indicator; DOI=10.1051/0004-6361:20021600; arXiv=astro-ph/0211219; ADS=2003A&A...399...39R | cross-wired fields=arxiv | use only corrected canonical row with DOI=10.1051/0004-6361:20021600; arXiv=astro-ph/0211304; ADS=2003A&A...399...39R
UNCITED_NOT_USABLE | raw REV01-P020 tuple: title=Fermi Large Area Telescope Observations of the Local Interstellar Medium; DOI=10.1088/0004-637X/710/1/133; arXiv=none; ADS=2010ApJ...710..133A | cross-wired fields=title,arxiv | use only corrected canonical row with DOI=10.1088/0004-637X/710/1/133; arXiv=0912.3618; ADS=2010ApJ...710..133A
UNCITED_NOT_USABLE | raw REV01-P021 tuple: title=Submillimeter continuum observations of Rho Ophiuchi A - The candidate protostar VLA 1623 and prestellar clumps; DOI=10.1086/172346; arXiv=none; ADS=1993ApJ...406..122A | cross-wired fields=doi | use only corrected canonical row with DOI=10.1086/172425; arXiv=none; ADS=1993ApJ...406..122A
UNCITED_NOT_USABLE | raw REV01-P026 tuple: title=Dust Extinction, Polarization, and Albedo Using Environmental-dependent Dust Models; DOI=10.1086/319622; arXiv=astro-ph/0008146; ADS=2001ApJ...548..296W | cross-wired fields=title,doi | use only corrected canonical row with DOI=10.1086/318651; arXiv=astro-ph/0008146; ADS=2001ApJ...548..296W
UNCITED_NOT_USABLE | raw REV01-P027 tuple: title=A 350 Micron Dust Continuum Survey of Massive Star-forming Clumps; DOI=10.1086/379001; arXiv=astro-ph/0308253; ADS=2003ApJS..149..375S | cross-wired fields=title,doi,arxiv | use only corrected canonical row with DOI=10.1086/379147; arXiv=astro-ph/0308310; ADS=2003ApJS..149..375S
UNCITED_NOT_USABLE | raw REV01-P028 tuple: title=The ratio of carbon monoxide to molecular hydrogen in interstellar dark clouds; DOI=10.1086/190538; arXiv=none; ADS=1978ApJS...37..407D | cross-wired fields=doi | use only corrected canonical row with DOI=10.1086/190535; arXiv=none; ADS=1978ApJS...37..407D
UNCITED_NOT_USABLE | raw REV01-P030 tuple: title=A CO-to-H2 Conversion Factor for the Taurus Molecular Cloud; DOI=10.1088/0004-637X/721/1/686; arXiv=1008.2166; ADS=2010ApJ...721..686P | cross-wired fields=title,arxiv | use only corrected canonical row with DOI=10.1088/0004-637X/721/1/686; arXiv=1007.5060; ADS=2010ApJ...721..686P
UNCITED_NOT_USABLE | raw REV01-P031 tuple: title=Carbon Monoxide Depletion in a Cold, Dense Cloud; DOI=10.1086/345494; arXiv=astro-ph/0210200; ADS=2003ApJ...583..789L | cross-wired fields=title,doi,arxiv | use only corrected canonical row with DOI=10.1086/345428; arXiv=astro-ph/0210330; ADS=2003ApJ...583..789L
UNCITED_NOT_USABLE | raw REV01-P032 tuple: title=The c2d Spitzer Spectroscopic Survey of Ices around Low-Mass Young Stellar Objects. II. CO2; DOI=10.1086/533431; arXiv=0801.3283; ADS=2008ApJ...678.1005P | cross-wired fields=arxiv | use only corrected canonical row with DOI=10.1086/533431; arXiv=0711.4616; ADS=2008ApJ...678.1005P
UNCITED_NOT_USABLE | raw REV01-P033 tuple: title=The Abundance of Carbon Dioxide Ice in the Quiescent Intracloud Medium; DOI=10.1086/509771; arXiv=astro-ph/0610333; ADS=2007ApJ...655..332W | cross-wired fields=doi,arxiv | use only corrected canonical row with DOI=10.1086/509772; arXiv=none; ADS=2007ApJ...655..332W
UNCITED_NOT_USABLE | raw REV01-P034 tuple: title=The Taurus Molecular Cloud: High-Resolution 12CO and 13CO Imaging; DOI=10.1086/587171; arXiv=0802.2206; ADS=2008ApJ...680..428G | cross-wired fields=title,doi | use only corrected canonical row with DOI=10.1086/587166; arXiv=0802.2206; ADS=2008ApJ...680..428G
UNCITED_NOT_USABLE | raw REV01-P035 tuple: title=The CO-to-H2 conversion factor in diffuse gas; DOI=10.1051/0004-6361/201014389; arXiv=1004.2818; ADS=2010A&A...518A..45L | cross-wired fields=title,doi,arxiv | use only corrected canonical row with DOI=10.1051/0004-6361/201014510; arXiv=1005.2157; ADS=2010A&A...518A..45L
UNCITED_NOT_USABLE | raw REV01-P036 tuple: title=Modeling CO emission from turbulent molecular clouds; DOI=10.1111/j.1365-2966.2010.16478.x; arXiv=0912.4216; ADS=2010MNRAS.404....2G | cross-wired fields=title,doi,arxiv | use only corrected canonical row with DOI=10.1111/j.1365-2966.2009.15718.x; arXiv=0907.4081; ADS=2010MNRAS.404....2G
UNCITED_NOT_USABLE | raw REV01-P037 tuple: title=Carbon monoxide as an extragalactic mass tracer; DOI=10.1086/164599; arXiv=none; ADS=1986ApJ...309..326D | cross-wired fields=doi | use only corrected canonical row with DOI=10.1086/164604; arXiv=none; ADS=1986ApJ...309..326D
UNCITED_NOT_USABLE | raw REV01-P038 tuple: title=Modeling the CO-to-H2 conversion factor in galaxies: dependence on metallicity and radiation field; DOI=10.1111/j.1365-2966.2011.18563.x; arXiv=1102.5085; ADS=2011MNRAS.412.1686S | cross-wired fields=title,doi,arxiv | use only corrected canonical row with DOI=10.1111/j.1365-2966.2010.18005.x; arXiv=1011.2019; ADS=2011MNRAS.412.1686S
UNCITED_NOT_USABLE | raw REV01-P039 tuple: title=The physical state of the interstellar medium in dwarf galaxies; DOI=10.1086/165997; arXiv=none; ADS=1988ApJ...325..389M | cross-wired fields=title,doi | use only corrected canonical row with DOI=10.1086/166011; arXiv=none; ADS=1988ApJ...325..389M
UNCITED_NOT_USABLE | raw REV01-P041 tuple: title=The Spatially Resolved Star Formation Law from Integral Field Spectroscopy; DOI=10.1088/0004-637X/704/1/842; arXiv=0908.2811; ADS=2009ApJ...704..842B | cross-wired fields=title,arxiv | use only corrected canonical row with DOI=10.1088/0004-637X/704/1/842; arXiv=0908.2810; ADS=2009ApJ...704..842B
UNCITED_NOT_USABLE | raw REV01-P043 tuple: title=The Star Formation Law at Low Surface Density; DOI=10.1088/0004-637X/696/2/1834; arXiv=0903.0003; ADS=2009ApJ...696.1834W | cross-wired fields=arxiv | use only corrected canonical row with DOI=10.1088/0004-637X/696/2/1834; arXiv=0903.3015; ADS=2009ApJ...696.1834W
UNCITED_NOT_USABLE | REV01-P044 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P045 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P046 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P047 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P048 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P049 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P050 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P051 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P052 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P053 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P054 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P055 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P056 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P057 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P058 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P059 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P060 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P061 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P062 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | REV01-P063 | phantom source key referenced by the raw answer but absent from both the physical harvest and identity ledger | no source may be inferred or invented
UNCITED_NOT_USABLE | Post-2012 ALMA, JWST, or later-review result | outside Kennicutt & Evans 2012 citation boundary | place in its own later source packet
UNCITED_NOT_USABLE | Depletion time is a guaranteed exhaustion clock | overbroad interpretation | inflow, outflow, recycling, phase conversion, and changing SFR break the claim
UNCITED_NOT_USABLE | HI, H2, total gas, CO-bright gas, CO-dark gas, and dense gas are interchangeable | phase/tracer conflation | keep separate quantities and calibrations
UNCITED_NOT_USABLE | IR-HCN linearity proves universal dense-gas SFE | tracer-to-mass and selection overclaim | retain excitation, abundance, opacity, and environment caveats
UNCITED_NOT_USABLE | HI has a strict universal 10 solar-mass-per-square-parsec ceiling | hard-threshold overclaim | retain empirical local-sample boundary
UNCITED_NOT_USABLE | H2-SFR correlation proves molecular chemistry is causally necessary for collapse | correlation-to-causation error | retain shielded-cold-gas alternative
UNCITED_NOT_USABLE | One SFR calibration is independent of IMF, metallicity, history, dust, leakage, or stochastic sampling | calibration overclaim | use tracer-specific review assumptions
UNCITED_NOT_USABLE | A model mechanism establishes observational prevalence | epistemic-type error | label theory and require observations separately
UNCITED_NOT_USABLE | Raw external source-anchor list | contaminated search custody containing post-2012 and unrelated links | never use as the canonical source base

## 8. Review and source identity ledger

REV01 | Kennicutt & Evans (2012, ARA&A) | DOI:10.1146/annurev-astro-081811-125610; arXiv:1204.3552; ADS:2012ARA&A..50..531K | role=review | Authoritative 2012 synthesis; later literature requires separate packets.
REV01-P001 | Schmidt (1959, ApJ) | DOI:10.1086/146614; arXiv:none; ADS:1959ApJ...129..243S | role=theory | First theoretical proposition of a power-law relationship between gas density and star formation rate.
REV01-P002 | Schmidt (1963, ApJ) | DOI:10.1086/147553; arXiv:none; ADS:1963ApJ...137..758S | role=theory | Expansion of the power-law parameterization of the star formation rate to account for stellar mass distributions.
REV01-P003 | Kennicutt (1998, ApJ) | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=measurement | Established the benchmark integrated non-linear scaling law (N~1.4) between total gas and SFR surface density.
REV01-P004 | Kennicutt (1998, ARA&A) | DOI:10.1146/annurev.astro.36.1.189; arXiv:astro-ph/9807187; ADS:1998ARA&A..36..189K | role=calibration | The definitive pre-2012 compendium of standard multi-wavelength star formation rate calibrations based on a Salpeter IMF.
REV01-P005 | Gao & Solomon (2004, ApJ) | DOI:10.1086/382999; arXiv:astro-ph/0310339; ADS:2004ApJ...606..271G | role=measurement | Demonstrated a tight, linear global correlation between infrared luminosity (SFR) and HCN luminosity (dense gas).
REV01-P006 | Wu et al. (2005, ApJ) | DOI:10.1086/499623; arXiv:astro-ph/0511424; ADS:2005ApJ...635L.173W | role=measurement | Showed the linear dense gas (HCN) scaling relation extends down to individual massive star-forming clumps in the Milky Way.
REV01-P007 | Bigiel et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2846; arXiv:0810.2541; ADS:2008AJ....136.2846B | role=measurement | First comprehensive sub-kiloparsec mapping revealing SFR correlates tightly with H2 but is uncorrelated with HI.
REV01-P008 | Leroy et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=measurement | Measured constant H2 depletion times (~2 Gyr) and investigated the environmental drivers of the HI-to-H2 phase transition.
REV01-P009 | Genzel et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.16969.x; arXiv:1003.5180; ADS:2010MNRAS.407.2091G | role=debate | Proposed a bimodal star formation law separating high-redshift disks from highly efficient extreme starbursts.
REV01-P010 | Daddi et al. (2010, ApJ) | DOI:10.1088/2041-8205/714/1/L118; arXiv:1003.3889; ADS:2010ApJ...714L.118D | role=debate | Supported a bimodal KS law driven by distinct dynamical timescales and efficiencies in mergers versus secular disks.
REV01-P011 | Bigiel et al. (2010, AJ) | DOI:10.1088/0004-6256/140/5/1194; arXiv:1007.3498; ADS:2010AJ....140.1194B | role=measurement | Mapped the severe suppression of star formation efficiency in the HI-dominated, sub-threshold regimes of outer galactic disks.
REV01-P012 | Lada, Lombardi, & Alves (2010, ApJ) | DOI:10.1088/0004-637X/724/1/687; arXiv:1009.2985; ADS:2010ApJ...724..687L | role=measurement | Demonstrated that star formation rates in local clouds scale directly with the mass of dense gas above a specific extinction threshold.
REV01-P013 | Heiderman et al. (2010, ApJ) | DOI:10.1088/0004-637X/723/2/1019; arXiv:1009.1621; ADS:2010ApJ...723.1019H | role=measurement | Found that essentially all truly young protostars in Perseus are highly concentrated within extinction contours of Av > 8 mag.
REV01-P014 | Evans et al. (2009, ApJS) | DOI:10.1088/0067-0049/181/2/321; arXiv:0811.1059; ADS:2009ApJS..181..321E | role=measurement | Derived local molecular cloud depletion times of ~82 Myr, vastly exceeding the theoretical free-fall times.
REV01-P015 | Murphy et al. (2011, ApJ) | DOI:10.1088/0004-637X/737/2/67; arXiv:1105.4877; ADS:2011ApJ...737...67M | role=calibration | Provided updated Kroupa-IMF anchored SFR calibration constants for FUV, NUV, TIR, and 1.4 GHz emission.
REV01-P016 | Hao et al. (2011, ApJ) | DOI:10.1088/0004-637X/741/2/124; arXiv:1108.2837; ADS:2011ApJ...741..124H | role=calibration | Developed modern hybrid composite calibrations utilizing UV/optical combined with mid-infrared dust emission.
REV01-P017 | Rieke et al. (2009, ApJ) | DOI:10.1088/0004-637X/692/1/556; arXiv:0810.4150; ADS:2009ApJ...692..556R | role=calibration | Derived the updated calibration constant and metallicity dependencies for the 24 micron dust continuum SFR indicator.
REV01-P018 | Calzetti et al. (2010, ApJ) | DOI:10.1088/0004-637X/714/2/1256; arXiv:1003.0961; ADS:2010ApJ...714.1256C | role=calibration | Derived the specific 70 micron calibration constant, mitigating the cirrus contamination issues prevalent at longer wavelengths.
REV01-P019 | Ranalli et al. (2003, A&A) | DOI:10.1051/0004-6361:20021600; arXiv:astro-ph/0211304; ADS:2003A&A...399...39R | role=calibration | Established the foundational calibration relating hard X-ray emission (tracing high-mass X-ray binaries) to integrated SFR.
REV01-P020 | Abdo et al. (2010, ApJ) | DOI:10.1088/0004-637X/710/1/133; arXiv:0912.3618; ADS:2010ApJ...710..133A | role=measurement | Utilized gamma-ray emission to map the "dark gas" phase in the outer Galaxy, validating variations in the CO-to-H2 factor.
REV01-P021 | Andre, Ward-Thompson, & Barsony (1993, ApJ) | DOI:10.1086/172425; arXiv:none; ADS:1993ApJ...406..122A | role=measurement | Early defining observation of deeply embedded Class 0 protostellar clumps mapping high-density star formation onset.
REV01-P022 | Alonso-Herrero et al. (2006, ApJ) | DOI:10.1086/506958; arXiv:astro-ph/0606186; ADS:2006ApJ...650..835A | role=measurement | Mapped the highly concentrated circumnuclear starburst morphologies characterizing local LIRGs and ULIRGs.
REV01-P023 | Beltran et al. (2006, A&A) | DOI:10.1051/0004-6361:20053999; arXiv:none; ADS:2006A&A...447..221B | role=measurement | Identified scaling relations linking dense clump mass functions directly to the hierarchical formation of star clusters.
REV01-P024 | Draine (2003, ARA&A) | DOI:10.1146/annurev.astro.41.011802.094840; arXiv:astro-ph/0304489; ADS:2003ARA&A..41..241D | role=calibration | Definitive baseline physics for interstellar dust grain sizes, compositions, and sub-millimeter opacities used in gas mass mapping.
REV01-P025 | Bohlin, Savage & Drake (1978, ApJ) | DOI:10.1086/156357; arXiv:none; ADS:1978ApJ...224..132B | role=calibration | Foundational calibration equating diffuse interstellar reddening E(B-V) to total hydrogen column density in the Milky Way.
REV01-P026 | Weingartner & Draine (2001, ApJ) | DOI:10.1086/318651; arXiv:astro-ph/0008146; ADS:2001ApJ...548..296W | role=calibration | Calibrated the severe variations in dust-to-gas ratios and extinction curves required for measuring gas in the LMC and SMC.
REV01-P027 | Shirley et al. (2003, ApJS) | DOI:10.1086/379147; arXiv:astro-ph/0308310; ADS:2003ApJS..149..375S | role=measurement | Maps CS J=5-4 in high-mass star-forming cores; supports dense-gas structure, not a 350-micron dust-continuum survey.
REV01-P028 | Dickman (1978, ApJS) | DOI:10.1086/190535; arXiv:none; ADS:1978ApJS...37..407D | role=calibration | Early benchmark mapping isotopic 13CO column densities against visual extinction to derive the fundamental X(CO) conversion logic.
REV01-P029 | Frerking, Langer & Wilson (1982, ApJ) | DOI:10.1086/160451; arXiv:none; ADS:1982ApJ...262..590F | role=calibration | Constrained the breakdown of CO as a strict mass tracer in saturated dense cores.
REV01-P030 | Pineda et al. (2010, ApJ) | DOI:10.1088/0004-637X/721/1/686; arXiv:1007.5060; ADS:2010ApJ...721..686P | role=measurement | Highly resolved mapping of the highly variable X(CO) factor within the Taurus cloud against visual extinction.
REV01-P031 | Lee et al. (2003, ApJ) | DOI:10.1086/345428; arXiv:astro-ph/0210330; ADS:2003ApJ...583..789L | role=caveat | Supports dense-core chemistry, dynamics, and depletion effects under the exact ADS record and title.
REV01-P032 | Pontoppidan et al. (2008, ApJ) | DOI:10.1086/533431; arXiv:0711.4616; ADS:2008ApJ...678.1005P | role=caveat | Proved gas-phase CO converts heavily into CO2 ice in dense environments, breaking standard chemical mass assumptions.
REV01-P033 | Whittet et al. (2007, ApJ) | DOI:10.1086/509772; arXiv:none; ADS:2007ApJ...655..332W | role=caveat | Quantified solid ice carbon depletion in intracloud mediums, placing fundamental limits on total gas mass derivations.
REV01-P034 | Goldsmith et al. (2008, ApJ) | DOI:10.1086/587166; arXiv:0802.2206; ADS:2008ApJ...680..428G | role=measurement | Stacking analysis showing extreme X(CO) variation in diffuse molecular cloud envelopes versus dense cores.
REV01-P035 | Liszt, Pety & Lucas (2010, A&A) | DOI:10.1051/0004-6361/201014510; arXiv:1005.2157; ADS:2010A&A...518A..45L | role=debate | Argument that X(CO) remains surprisingly constant in diffuse unbound gas, challenging standard cloud threshold definitions.
REV01-P036 | Glover et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2009.15718.x; arXiv:0907.4081; ADS:2010MNRAS.404....2G | role=theory | Hydrodynamic simulations proving integrated CO can poorly correlate with true visual extinction in turbulent environments.
REV01-P037 | Dickman, Snell & Schloerb (1986, ApJ) | DOI:10.1086/164604; arXiv:none; ADS:1986ApJ...309..326D | role=calibration | Foundational extragalactic "cloud counting" logic to convert CO luminosity to total molecular mass.
REV01-P038 | Shetty et al. (2011, MNRAS) | DOI:10.1111/j.1365-2966.2010.18005.x; arXiv:1011.2019; ADS:2011MNRAS.412.1686S | role=theory | Derived the theoretical scaling relations for X(CO) against gas density and intense radiation environments.
REV01-P039 | Maloney & Black (1988, ApJ) | DOI:10.1086/166011; arXiv:none; ADS:1988ApJ...325..389M | role=theory | Models CO-to-H2 conversion and molecular-gas abundance in spiral and irregular galaxies; retain metallicity and radiation-field limits.
REV01-P040 | Krumholz, Dekel & McKee (2012, ApJ) | DOI:10.1088/0004-637X/745/1/69; arXiv:1109.4150; ADS:2012ApJ...745...69K | role=theory | Theoretical model attempting to unify disparate KS laws through local free-fall scaling across all environments.
REV01-P041 | Blanc et al. (2009, ApJ) | DOI:10.1088/0004-637X/704/1/842; arXiv:0908.2810; ADS:2009ApJ...704..842B | role=measurement | Integral field spectroscopy mapping confirming the steep non-linear break in the sub-kpc star formation law at low gas densities.
REV01-P042 | Schruba et al. (2011, AJ) | DOI:10.1088/0004-6256/142/2/37; arXiv:1105.4605; ADS:2011AJ....142...37S | role=measurement | Deep stacking showing tight SFR-to-H2 coupling persists even in atomic-dominated outer edges.
REV01-P043 | Wyder et al. (2009, ApJ) | DOI:10.1088/0004-637X/696/2/1834; arXiv:0903.3015; ADS:2009ApJ...696.1834W | role=measurement | Empirical mapping of extreme inefficiency in the deeply sub-threshold environments of UV-extended disks.

REVIEW_BASE_01_VERIFIED_READY_REFERENCE_ONLY

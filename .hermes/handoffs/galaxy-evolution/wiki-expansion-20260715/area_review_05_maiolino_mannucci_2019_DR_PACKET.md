# Review Base 05 canonical advisory packet — Maiolino & Mannucci 2019

status: READY_FOR_HWAO_REVIEW
advisory_only: true
canonical_packet_released: true
wiki_write_performed_by_tori: false
raw_packet_sha256: `d68f2e08e22261cc70195f5ee6654c2fa2270f463642e3b25600e646392e5fd4`
independent_identifier_verification: `PASS`

## 1. Review Identity and Scope Map

### [REV05-R00]
role: review_identity
epistemic_type: review_synthesis
finding: Maiolino & Mannucci (2019), *De re metallica: the cosmic chemical evolution of galaxies*, is verified as DOI 10.1007/s00159-018-0112-2, arXiv 1811.09642, ADS 2019A&ARv..27....3M.
boundary: Review-wide synthesis through 2019; non-AGN chemical evolution; post-2019/JWST work excluded.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-R00]

### [REV05-S01]
role: scope
epistemic_type: review_synthesis
finding: The source base covers metal production, gas-phase and stellar abundance diagnostics, MZR/FMR relations, abundance ratios, spatial gradients, metal budgets, and bounded models.
boundary: Gas, stars, neutral gas, CGM, and ICM remain distinct phases; calibration, IMF, aperture, and redshift boundaries are mandatory.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-R00]

## 2. Established Findings

### [REV05-E01]
role: scaling_relation
epistemic_type: observation
finding: The local gas-phase mass-metallicity relation rises with stellar mass and flattens above a calibration-dependent turnover.
boundary: SDSS star-forming fibers near z≈0.1; oxygen scale and stellar-mass IMF must be fixed.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P001], [REV05-P008]

### [REV05-E02]
role: secondary_relation
epistemic_type: observation
finding: At fixed stellar mass, several local analyses find lower gas-phase metallicity at higher SFR, but its amplitude depends on selection and analysis choices.
boundary: Local star-forming samples; same abundance calibration, aperture correction, and SFR estimator required.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P003], [REV05-P041], [REV05-P042]

### [REV05-E03]
role: abundance_ratio
epistemic_type: review_synthesis
finding: Nitrogen exhibits primary-like behavior at low O/H and an increasing secondary contribution at higher O/H, with delayed intermediate-mass-star enrichment affecting N/O.
boundary: H II-region gas abundances; yields, time delays, and direct-versus-strong-line scale remain coupled.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P020], [REV05-P021]

### [REV05-E04]
role: regulator_framework
epistemic_type: analytic_theory
finding: Gas-regulator models express metallicity as a balance among inflow, star formation, recycling, yields, and outflow rather than as a closed-box clock.
boundary: Quasi-equilibrium and mixing assumptions are model premises, not universal observations.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P011], [REV05-P012], [REV05-P013]

### [REV05-E05]
role: spatial_distribution
epistemic_type: observation
finding: Most local non-interacting star-forming disks show negative gas-phase radial abundance gradients when radii and calibrations are normalized consistently.
boundary: H II-region/IFU gas-phase oxygen; sample cuts, DIG, bars, and radial normalization matter.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P018], [REV05-P019]

### [REV05-E06]
role: diagnostic_baseline
epistemic_type: calibration
finding: Strong-line metallicity calibrations disagree substantially in absolute O/H, although internally consistent transformations can recover relative trends.
boundary: H II-region gas phase only; direct, empirical, and photoionization-model scales are not interchangeable.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P002], [REV05-P004], [REV05-P015], [REV05-P030], [REV05-P031]

### [REV05-E07]
role: metal_budget
epistemic_type: observation
finding: A large fraction of metals synthesized by galaxies is not in their stars and cold ISM, and metal-bearing circumgalactic gas is therefore a required budget component.
boundary: Ionization corrections and unobserved hot phases dominate the CGM inventory uncertainty.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P007], [REV05-P009], [REV05-P010]

### [REV05-E08]
role: redshift_evolution
epistemic_type: observation
finding: Gas-phase MZR measurements at z≈2–3.5 generally lie below local relations when compared on a controlled abundance scale.
boundary: Pre-JWST rest-optical samples; line selection, excitation, aperture, and calibration evolution limit absolute comparison.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P027], [REV05-P028], [REV05-P029]

### [REV05-E09]
role: chemical_clock
epistemic_type: observation
finding: Enhanced stellar [alpha/Fe] in rapidly formed early-type populations is consistent with short formation times relative to delayed Type Ia iron enrichment.
boundary: Integrated stellar populations; stellar libraries, response functions, IMF, and star-formation-history assumptions apply.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P023]

### [REV05-E10]
role: gradient_perturbation
epistemic_type: observation
finding: Interactions and rapid inflow can flatten or invert gas-phase abundance gradients relative to isolated disks.
boundary: Merger stage, beam smearing, spatial sampling, and abundance calibration must be controlled.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P034], [REV05-P036]

### [REV05-E11]
role: effective_yield
epistemic_type: review_synthesis
finding: Low-mass systems have lower effective yields than simple closed-box expectations, consistent with inflow and/or preferential metal loss.
boundary: Effective yield is inferred from gas fraction and gas-phase abundance; it does not uniquely identify one mechanism.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P032], [REV05-P033], [REV05-P051]

### [REV05-E12]
role: cross_tracer_check
epistemic_type: observation
finding: Direct-method nebular abundances can agree more closely with young-star abundances than some model-based strong-line scales in resolved nearby systems.
boundary: Young stars and co-spatial H II regions; this does not make gas and stellar metallicities generally interchangeable.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P014], [REV05-P044], [REV05-P045]

## 3. Open Debates and Tensions

### [REV05-D01]
role: abundance_scale
epistemic_type: calibration
finding: Electron-temperature, recombination-line, and photoionization-model methods do not share one settled absolute abundance scale.
boundary: Temperature fluctuations, depletion, geometry, atomic data, and model priors remain entangled.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P002], [REV05-P004], [REV05-P015], [REV05-P030], [REV05-P031]

### [REV05-D02]
role: nitrogen_origin
epistemic_type: review_synthesis
finding: The relative massive-star and intermediate-mass-star contributions to primary nitrogen remain yield- and timescale-dependent.
boundary: N/O cannot be mapped to one age or metallicity without a chemical-evolution model.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P020], [REV05-P021], [REV05-P022]

### [REV05-D03]
role: fmr_reality
epistemic_type: observation
finding: The existence, strength, and redshift invariance of a universal M-Z-SFR surface remained disputed in 2019.
boundary: Selection, aperture, S/N cuts, calibration, and correlated errors can create or suppress residual trends.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P003], [REV05-P005], [REV05-P041], [REV05-P042], [REV05-P050]

### [REV05-D04]
role: mzr_driver
epistemic_type: review_synthesis
finding: The MZR alone cannot separate mass-dependent outflow, inflow dilution, star-formation efficiency, recycling, and enriched reaccretion.
boundary: Several regulator and simulation parameter combinations reproduce similar scaling relations.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P008], [REV05-P011], [REV05-P012], [REV05-P033], [REV05-P048]

### [REV05-D05]
role: gradient_evolution
epistemic_type: observation
finding: The frequency of genuinely flat or inverted high-redshift gradients remained uncertain because beam smearing and selection can mimic them.
boundary: Compare matched tracers and resolution; local normalized slopes are not a universal high-z baseline.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P006], [REV05-P018], [REV05-P019], [REV05-P034], [REV05-P036], [REV05-P049]

### [REV05-D06]
role: yield_imf_delay
epistemic_type: review_synthesis
finding: Yield tables, IMF shape, stellar rotation/binarity, and enrichment delays remain degenerate in abundance-ratio fits.
boundary: An apparent yield change need not imply an IMF change.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P020], [REV05-P023], [REV05-P032], [REV05-P037]

### [REV05-D07]
role: highz_diagnostics
epistemic_type: observation
finding: Harder ionizing spectra, density, ionization parameter, and N/O evolution complicate use of local strong-line calibrations at z≈2–3.
boundary: BPT offsets bound diagnostic transfer; they are not an AGN-demographic result here.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P024], [REV05-P025], [REV05-P026], [REV05-P027]

### [REV05-D08]
role: missing_metals
epistemic_type: observation
finding: The location and ionization state of the remaining galactic and cosmic metal budget were unresolved in 2019.
boundary: Cool-CGM inventories exclude poorly constrained hot and diffuse phases.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P007], [REV05-P009], [REV05-P010]

## 4. Key Measurements, Model Benchmarks, and Calibrations

### [REV05-N01]
role: solar_reference
epistemic_type: calibration
finding: A commonly adopted solar oxygen abundance is 12+log(O/H)=8.69.
boundary: Solar photospheric reference from a supporting synthesis; changing the solar scale shifts normalized metallicities.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P043]

### [REV05-N02]
role: mzr_turnover
epistemic_type: observation
finding: The SDSS gas-phase MZR steepens below and flattens above a characteristic stellar mass of order 10^10.5 solar masses.
boundary: Local fiber sample and adopted stellar masses/strong-line model scale.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P001], [REV05-P008]

### [REV05-N03]
role: calibration_offset
epistemic_type: calibration
finding: Published strong-line methods can differ by up to roughly 0.7 dex in inferred 12+log(O/H) for the same galaxy sample.
boundary: Maximum method-to-method systematic, not measurement scatter within one scale.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P015]

### [REV05-N04]
role: fmr_scatter
epistemic_type: observation
finding: The original local FMR parameterization reported residual metallicity scatter near 0.05 dex.
boundary: SDSS selection and that paper's calibration/parameterization; later analyses question universality.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P003], [REV05-P042]

### [REV05-N05]
role: nitrogen_plateau
epistemic_type: observation
finding: Low-metallicity systems show an approximate primary-nitrogen plateau near log(N/O)≈-1.5, with substantial object and method scatter.
boundary: Ionized-gas measurements; ionization corrections and delayed enrichment apply.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P020], [REV05-P021]

### [REV05-N06]
role: gradient_scale
epistemic_type: observation
finding: CALIFA disks yielded a characteristic normalized oxygen-abundance slope of order -0.1 dex per effective radius.
boundary: Non-interacting local disks on the adopted calibration and radial fit range.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P018]

### [REV05-N07]
role: highz_mzr_offset
epistemic_type: observation
finding: Pre-JWST z≈3–3.5 samples reported gas-phase metallicities lower than local galaxies by several tenths of a dex at fixed stellar mass.
boundary: Not an absolute universal offset: calibrations, excitation, and sample selection dominate cross-redshift comparison.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P028], [REV05-P029]

### [REV05-N08]
role: retained_metal_fraction
epistemic_type: observation
finding: Nearby-galaxy accounting placed only a minority—of order one quarter—of produced metals in stars, the ISM, and dust, with additional metals inferred in the CGM.
boundary: Inventory depends on assumed yields, IMF, ionization corrections, and poorly observed hot gas.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P007], [REV05-P009]

## 5. What Remained Unknown in 2019

### [REV05-U01]
role: absolute_oxygen_scale
epistemic_type: review_synthesis
finding: The absolute nebular oxygen scale remained uncertain.
boundary: Joint auroral, recombination-line, IR, and stellar-abundance measurements in matched regions were needed.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P004], [REV05-P015], [REV05-P045]

### [REV05-U02]
role: fmr_evolution
epistemic_type: review_synthesis
finding: Whether one FMR is invariant over cosmic time remained unknown.
boundary: Calibration-matched, representative samples with controlled apertures and gas measurements were needed.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P003], [REV05-P042], [REV05-P050]

### [REV05-U03]
role: highz_ionization
epistemic_type: review_synthesis
finding: The physical mixture producing the high-redshift nebular diagnostic offset was unresolved.
boundary: Stellar UV, rest-optical, density, and direct-temperature constraints in the same galaxies were needed.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P024], [REV05-P025], [REV05-P026]

### [REV05-U04]
role: depletion
epistemic_type: review_synthesis
finding: Environment-specific dust depletion corrections for individual elements were insufficiently known.
boundary: Co-spatial volatile and refractory-element measurements across phases were needed.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P007], [REV05-P043]

### [REV05-U05]
role: positive_gradients
epistemic_type: review_synthesis
finding: The prevalence and lifetime of genuine positive high-redshift metallicity gradients were uncertain.
boundary: Higher-resolution lensing/IFU data and forward beam-smearing models were needed.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P006], [REV05-P036], [REV05-P049]

### [REV05-U06]
role: hot_metal_budget
epistemic_type: review_synthesis
finding: The amount of metals in hot and ultra-diffuse circumgalactic/intergalactic phases remained poorly constrained.
boundary: Sensitive X-ray and UV ion inventories with multiphase ionization models were needed.
confidence: high for bounded review synthesis; preserve stated systematics
source_keys: [REV05-P007], [REV05-P009], [REV05-P010]

## 6. Primary-Citation Harvest

[REV05-P001] Tremonti, C. A., et al. (2004, The Astrophysical Journal) | title=The Origin of the Mass-Metallicity Relation: Insights from 53,000 Star-forming Galaxies in the Sloan Digital Sky Survey | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=measurement | review_locator=MZR | Bounded to SDSS local fiber gas-phase metallicities.
[REV05-P002] Pettini, M., & Pagel, M. E. (2004, Monthly Notices of the Royal Astronomical Society) | title=[OIII]/[NII] as an abundance indicator at high redshift | DOI:10.1111/j.1365-2966.2004.07591.x; arXiv:astro-ph/0401128; ADS:2004MNRAS.348L..59P | role=calibration | review_locator=strong-line methods | Bounded to O3N2 and N2 index empirical calibration scale.
[REV05-P003] Mannucci, F., et al. (2010, Monthly Notices of the Royal Astronomical Society) | title=A fundamental relation between mass, star formation rate and metallicity in local and high-redshift galaxies | DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1005.0006; ADS:2010MNRAS.408.2115M | role=measurement | review_locator=FMR | Bounded to establishing the 3D M-Z-SFR manifold.
[REV05-P004] Curti, M., et al. (2017, Monthly Notices of the Royal Astronomical Society) | title=New fully empirical calibrations of strong-line metallicity indicators in star-forming galaxies | DOI:10.1093/mnras/stw2766; arXiv:1610.06939; ADS:2017MNRAS.465.1384C | role=calibration | review_locator=strong-line methods | Bounded to Te-based empirical calibrations via stacked SDSS spectra.
[REV05-P005] Bothwell, M. S., et al. (2013, Monthly Notices of the Royal Astronomical Society) | title=A fundamental relation between the metallicity, gas content and stellar mass of local galaxies | DOI:10.1093/mnras/stt817; arXiv:1304.4940; ADS:2013MNRAS.433.1425B | role=measurement | review_locator=gas fractions | Bounded to HI gas mass dependence driving the FMR.
[REV05-P006] Cresci, G., et al. (2010, Nature) | title=Gas accretion as the origin of chemical abundance gradients in distant galaxies | DOI:10.1038/nature09451; arXiv:1010.2534; ADS:2010Natur.467..811C | role=measurement | review_locator=spatially resolved gradients | Bounded to inverted gradients indicating cold gas accretion at z~3.
[REV05-P007] Peeples, M. S., et al. (2014, The Astrophysical Journal) | title=A Budget and Accounting of Metals at z ~ 0: Results from the COS-Halos Survey | DOI:10.1088/0004-637X/786/1/54; arXiv:1310.2253; ADS:2014ApJ...786...54P | role=measurement | review_locator=metal budgets | Bounded to accounting limits of retained vs. expelled galactic metals.
[REV05-P008] Zahid, H. J., et al. (2014, The Astrophysical Journal) | title=The Universal Relation of Galactic Chemical Evolution: The Origin of the Mass-Metallicity Relation | DOI:10.1088/0004-637X/791/2/130; arXiv:1404.7526; ADS:2014ApJ...791..130Z | role=analytic_theory | review_locator=chemical-evolution models | Bounded to modeling MZR saturation.
[REV05-P009] Werk, J. K., et al. (2014, The Astrophysical Journal) | title=The COS-Halos Survey: Physical Conditions and Baryonic Mass in the Low-redshift Circumgalactic Medium | DOI:10.1088/0004-637X/792/1/8; arXiv:1403.0947; ADS:2014ApJ...792....8W | role=measurement | review_locator=CGM tracers | Bounded to multiphase ionization modeling of the CGM.
[REV05-P010] Tumlinson, J., et al. (2011, Science) | title=The Large, Oxygen-Rich Halos of Star-Forming Galaxies Are a Major Reservoir of Galactic Metals | DOI:10.1126/science.1209840; arXiv:1111.3980; ADS:2011Sci...334..948T | role=measurement | review_locator=CGM tracers | Bounded to OVI detection tracing massive metal reservoirs in the halos.
[REV05-P011] Lilly, S. J., et al. (2013, The Astrophysical Journal) | title=Gas Regulation of Galaxies: The Evolution of the Cosmic Specific Star Formation Rate, the Metallicity-Mass-Star-formation Rate Relation, and the Stellar Content of Halos | DOI:10.1088/0004-637X/772/2/119; arXiv:1303.5059; ADS:2013ApJ...772..119L | role=analytic_theory | review_locator=chemical-evolution models | Bounded to formulating the gas-regulator/bathtub model.
[REV05-P012] Bouché, N., et al. (2010, The Astrophysical Journal) | title=The Impact of Cold Gas Accretion Above a Mass Floor on Galaxy Scaling Relations | DOI:10.1088/0004-637X/718/2/1001; arXiv:0912.1858; ADS:2010ApJ...718.1001B | role=analytic_theory | review_locator=chemical-evolution models | Bounded to the interplay of inflows and SFR in setting abundances.
[REV05-P013] Davé, R., et al. (2012, Monthly Notices of the Royal Astronomical Society) | title=An analytic model for the evolution of the stellar, gas and metal content of galaxies | DOI:10.1111/j.1365-2966.2011.20148.x; arXiv:1108.0426; ADS:2012MNRAS.421...98D | role=analytic_theory | review_locator=cosmological simulations | Analytic equilibrium model for stellar, gas, and metal evolution; not a hydrodynamic simulation.
[REV05-P014] Andrews, B. H., & Martini, P. (2013, The Astrophysical Journal) | title=The Mass-Metallicity Relation with the Direct Method on Stacked Spectra of SDSS Galaxies | DOI:10.1088/0004-637X/765/2/140; arXiv:1211.3418; ADS:2013ApJ...765..140A | role=measurement | review_locator=MZR | Bounded to establishing the MZR using stacked Te measurements.
[REV05-P015] Kewley, L. J., & Ellison, S. L. (2008, The Astrophysical Journal) | title=Metallicity Calibrations and the Mass-Metallicity Relation for Star-forming Galaxies | DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K | role=calibration | review_locator=calibration offsets | Bounded to systematic transformations between discrepant absolute scales.
[REV05-P016] Zaritsky, D., et al. (1994, The Astrophysical Journal) | title=H II Regions and the Abundance Properties of Spiral Galaxies | DOI:10.1086/173544; arXiv:none; ADS:1994ApJ...420...87Z | role=measurement | review_locator=spatially resolved gradients | Bounded to pioneering characterizations of radial abundance gradients.
[REV05-P017] Vila-Costas, M. A., & Edmunds, M. G. (1992, Monthly Notices of the Royal Astronomical Society) | title=The relation between abundance gradients and the physical properties of spiral galaxies. | DOI:10.1093/mnras/259.1.121; arXiv:none; ADS:1992MNRAS.259..121V | role=measurement | review_locator=chemical-evolution models | Bounded to classical chemical yield and local disk evolution limits.
[REV05-P018] Sánchez, S. F., et al. (2014, Astronomy and Astrophysics) | title=A characteristic oxygen abundance gradient in galaxy disks unveiled with CALIFA | DOI:10.1051/0004-6361/201322343; arXiv:1311.7052; ADS:2014A&A...563A..49S | role=measurement | review_locator=spatially resolved gradients | Bounded to defining a universal gradient slope normalized by Re.
[REV05-P019] Belfiore, F., et al. (2017, Monthly Notices of the Royal Astronomical Society) | title=SDSS IV MaNGA - metallicity and nitrogen abundance gradients in local galaxies | DOI:10.1093/mnras/stx789; arXiv:1703.03813; ADS:2017MNRAS.469..151B | role=measurement | review_locator=spatially resolved gradients | Bounded to mapping local gradients across large mass samples.
[REV05-P020] Henry, R. B. C., et al. (2000, The Astrophysical Journal) | title=On the Cosmic Origins of Carbon and Nitrogen | DOI:10.1086/309471; arXiv:astro-ph/0004299; ADS:2000ApJ...541..660H | role=analytic_theory | review_locator=relative abundances | Bounded to models of primary vs secondary nitrogen production.
[REV05-P021] Izotov, Y. I., & Thuan, T. X. (1999, The Astrophysical Journal) | title=Heavy-Element Abundances in Blue Compact Galaxies | DOI:10.1086/306708; arXiv:astro-ph/9811387; ADS:1999ApJ...511..639I | role=measurement | review_locator=relative abundances | Bounded to N/O and C/O measurements in extreme low-metallicity environments.
[REV05-P022] Garnett, D. R., et al. (1995, The Astrophysical Journal) | title=The Evolution of C/O in Dwarf Galaxies from Hubble Space Telescope FOS Observations | DOI:10.1086/175503; arXiv:astro-ph/9411011; ADS:1995ApJ...443...64G | role=measurement | review_locator=relative abundances | Bounded to establishing the primary nitrogen floor.
[REV05-P023] Thomas, D., et al. (2005, The Astrophysical Journal) | title=The Epochs of Early-Type Galaxy Formation as a Function of Environment | DOI:10.1086/426932; arXiv:astro-ph/0410209; ADS:2005ApJ...621..673T | role=measurement | review_locator=stellar metallicities | Bounded to alpha/Fe ratios charting rapid star formation in early-type galaxies.
[REV05-P024] Steidel, C. C., et al. (2014, The Astrophysical Journal) | title=Strong Nebular Line Ratios in the Spectra of z ~ 2-3 Star Forming Galaxies: First Results from KBSS-MOSFIRE | DOI:10.1088/0004-637X/795/2/165; arXiv:1405.5473; ADS:2014ApJ...795..165S | role=measurement | review_locator=high-redshift limitations | Bounded to the BPT diagnostic shift at z~2.
[REV05-P025] Steidel, C. C., et al. (2016, The Astrophysical Journal) | title=Reconciling the Stellar and Nebular Spectra of High-redshift Galaxies | DOI:10.3847/0004-637X/826/2/159; arXiv:1605.07186; ADS:2016ApJ...826..159S | role=measurement | review_locator=high-redshift limitations | Bounded to stellar binary impact on ionizing spectra at high redshift.
[REV05-P026] Strom, A. L., et al. (2017, The Astrophysical Journal) | title=Nebular Emission Line Ratios in z ≃ 2-3 Star-forming Galaxies with KBSS-MOSFIRE: Exploring the Impact of Ionization, Excitation, and Nitrogen-to-Oxygen Ratio | DOI:10.3847/1538-4357/836/2/164; arXiv:1608.02587; ADS:2017ApJ...836..164S | role=measurement | review_locator=high-redshift limitations | Bounded to mass-metallicity scaling in the KBSS z~2 survey.
[REV05-P027] Erb, D. K., et al. (2006, The Astrophysical Journal) | title=The Mass-Metallicity Relation at z>~2 | DOI:10.1086/503623; arXiv:astro-ph/0602473; ADS:2006ApJ...644..813E | role=measurement | review_locator=redshift evolution | Bounded to pioneer measurements of the MZR at cosmic noon.
[REV05-P028] Maiolino, R., et al. (2008, Astronomy and Astrophysics) | title=AMAZE. I. The evolution of the mass-metallicity relation at z > 3 | DOI:10.1051/0004-6361:200809678; arXiv:0806.2410; ADS:2008A&A...488..463M | role=measurement | review_locator=redshift evolution | Bounded to downward normalization of the MZR at z>3.
[REV05-P029] Troncoso, P., et al. (2014, Astronomy and Astrophysics) | title=Metallicity evolution, metallicity gradients, and gas fractions at z ~ 3.4 | DOI:10.1051/0004-6361/201322099; arXiv:1311.4576; ADS:2014A&A...563A..58T | role=measurement | review_locator=redshift evolution | Bounded to AMAZE gas fraction limits and metal retention limits.
[REV05-P030] Marino, R. A., et al. (2013, Astronomy and Astrophysics) | title=The O3N2 and N2 abundance indicators revisited: improved calibrations based on CALIFA and Te-based literature data | DOI:10.1051/0004-6361/201321956; arXiv:1307.5316; ADS:2013A&A...559A.114M | role=calibration | review_locator=strong-line methods | Bounded to establishing updated linear index calibrations based on Te.
[REV05-P031] Pilyugin, L. S., & Grebel, E. K. (2016, Monthly Notices of the Royal Astronomical Society) | title=New calibrations for abundance determinations in H II regions | DOI:10.1093/mnras/stw238; arXiv:1601.08217; ADS:2016MNRAS.457.3678P | role=calibration | review_locator=strong-line methods | Bounded to S-method application utilizing N/O diagnostics.
[REV05-P032] Edmunds, M. G. (1990, Monthly Notices of the Royal Astronomical Society) | title=General Constraints on the Effect of Gas Flows in the Chemical Evolution of Galaxies | DOI:none; arXiv:none; ADS:1990MNRAS.246..678E | role=analytic_theory | review_locator=metal budgets | Bounded to defining effective yield dependencies and mass-loss mechanisms.
[REV05-P033] Peeples, M. S., & Shankar, F. (2011, Monthly Notices of the Royal Astronomical Society) | title=Constraints on star formation driven galaxy winds from the mass-metallicity relation at z= 0 | DOI:10.1111/j.1365-2966.2011.19456.x; arXiv:1007.3743; ADS:2011MNRAS.417.2962P | role=analytic_theory | review_locator=metal budgets | Bounded to connecting stellar fractions to gas-phase constraints.
[REV05-P034] Ho, I-Ting, et al. (2015, Monthly Notices of the Royal Astronomical Society) | title=Metallicity gradients in local field star-forming galaxies: insights on inflows, outflows, and the coevolution of gas, stars and metals | DOI:10.1093/mnras/stv067; arXiv:1501.02668; ADS:2015MNRAS.448.2030H | role=measurement | review_locator=environmental effects | Bounded to measuring gradient flattening due to tidal inflow.
[REV05-P036] Jones, T., et al. (2013, The Astrophysical Journal) | title=The Origin and Evolution of Metallicity Gradients: Probing the Mode of Mass Assembly at z ~= 2 | DOI:10.1088/0004-637X/765/1/48; arXiv:1207.4489; ADS:2013ApJ...765...48J | role=measurement | review_locator=spatially resolved gradients | Bounded to identifying flat and inverted gradients via lensing.
[REV05-P039] McGaugh, S. S. (1991, The Astrophysical Journal) | title=H II Region Abundances: Model Oxygen Line Ratios | DOI:10.1086/170569; arXiv:none; ADS:1991ApJ...380..140M | role=calibration | review_locator=strong-line methods | Bounded to theoretical photoionization R23 modeling.
[REV05-P040] Lequeux, J., et al. (1979, Astronomy and Astrophysics) | title=Chemical Composition and Evolution of Irregular and Blue Compact Galaxies | DOI:none; arXiv:none; ADS:1979A&A....80..155L | role=measurement | review_locator=luminosity-metallicity relations | Bounded to originating observations tying mass/luminosity to metal abundance.
[REV05-P041] Lara-López, M. A., et al. (2010, Astronomy and Astrophysics) | title=A fundamental plane for field star-forming galaxies | DOI:10.1051/0004-6361/201014803; arXiv:1005.0509; ADS:2010A&A...521L..53L | role=measurement | review_locator=FMR | Bounded to codifying the FMR manifold as a principal component plane.
[REV05-P042] Salim, S., et al. (2014, The Astrophysical Journal) | title=A Critical Look at the Mass-Metallicity-Star Formation Rate Relation in the Local Universe. I. An Improved Analysis Framework and Confounding Systematics | DOI:10.1088/0004-637X/797/2/126; arXiv:1411.7391; ADS:2014ApJ...797..126S | role=measurement | review_locator=FMR | Bounded to SFR dependency limits on global SDSS scales.
[REV05-P044] Izotov, Y. I., et al. (2006, Astronomy and Astrophysics) | title=The chemical composition of metal-poor emission-line galaxies in the Data Release 3 of the Sloan Digital Sky Survey | DOI:10.1051/0004-6361:20053763; arXiv:astro-ph/0511644; ADS:2006A&A...448..955I | role=measurement | review_locator=direct electron-temperature methods | Bounded to assessing Te structural uncertainties.
[REV05-P045] Bresolin, F., et al. (2009, The Astrophysical Journal) | title=Extragalactic Chemical Abundances: Do H II Regions and Young Stars Tell the Same Story? The Case of the Spiral Galaxy NGC 300 | DOI:10.1088/0004-637X/700/1/309; arXiv:0905.2791; ADS:2009ApJ...700..309B | role=measurement | review_locator=spatially resolved gradients | Bounded to resolving Te-based gradient slopes in a nearby analog.
[REV05-P048] Davé, R., Finlator, K., & Oppenheimer, B. D. (2011, Monthly Notices of the Royal Astronomical Society) | title=Galaxy evolution in cosmological simulations with outflows - II. Metallicities and gas fractions | DOI:10.1111/j.1365-2966.2011.19132.x; arXiv:1104.3156; ADS:2011MNRAS.416.1354D | role=hydrodynamic_simulation | review_locator=cosmological simulations | Bounded to wind-recycling impact on scaling relations.
[REV05-P049] Carton, D., et al. (2018, Monthly Notices of the Royal Astronomical Society) | title=First gas-phase metallicity gradients of 0.1 ≲ z ≲ 0.8 galaxies with MUSE | DOI:10.1093/mnras/sty1343; arXiv:1805.08131; ADS:2018MNRAS.478.4293C | role=measurement | review_locator=spatially resolved gradients | Bounded to MUSE/MUSE-Wide gradient studies.
[REV05-P050] Torrey, P., et al. (2018, Monthly Notices of the Royal Astronomical Society) | title=Similar star formation rate and metallicity variability time-scales drive the fundamental metallicity relation | DOI:10.1093/mnrasl/sly031; arXiv:1711.11039; ADS:2018MNRAS.477L..16T | role=hydrodynamic_simulation | review_locator=cosmological simulations | Bounded to linking FMR scatter to cyclical SFR-metallicity oscillation timescales.
[REV05-P051] Garnett, D. R. (2002, The Astrophysical Journal) | title=The Luminosity-Metallicity Relation, Effective Yields, and Metal Loss in Spiral and Irregular Galaxies | DOI:10.1086/344301; arXiv:astro-ph/0209012; ADS:2002ApJ...581.1019G | role=measurement | review_locator=metal budgets | Observed luminosity-metallicity relation and effective-yield limits in nearby spirals and irregulars.

### Supporting reviews/syntheses (not counted as primary)

[REV05-P037] Tinsley, B. M. (1980, Fundamentals of Cosmic Physics) | title=Evolution of the Stars and Gas in Galaxies | DOI:none; arXiv:none; ADS:1980FCPh....5..287T | role=supporting_review | review_locator=chemical-evolution models | Foundational broad chemical-evolution synthesis; supporting review, not primary evidence.
[REV05-P043] Asplund, M., et al. (2009, Annual Review of Astronomy and Astrophysics) | title=The Chemical Composition of the Sun | DOI:10.1146/annurev.astro.46.060407.145222; arXiv:0909.0948; ADS:2009ARA&A..47..481A | role=supporting_review | review_locator=abundance-scale systematics | Solar-abundance synthesis that anchors zero points; supporting review, not primary evidence.

## 7. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | raw tuple for [REV05-P002] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P003] | corrected fields: arxiv | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P006] | corrected fields: doi | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P008] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P009] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P010] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P011] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P012] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P013] | corrected fields: arxiv, title, role | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P014] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P015] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P016] | corrected fields: doi | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P017] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P018] | corrected fields: arxiv | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P019] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P020] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P021] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P022] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P023] | corrected fields: arxiv | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P024] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P025] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P026] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P027] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P028] | corrected fields: doi, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P029] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P030] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P031] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P032] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P033] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P034] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P035] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P036] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P037] | corrected fields: role | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P038] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P039] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P040] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P041] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P042] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P043] | corrected fields: role | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P044] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P045] | corrected fields: arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P047] | corrected fields: arxiv | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P048] | corrected fields: title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P049] | corrected fields: doi, arxiv, title | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P050] | corrected fields: arxiv | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | raw tuple for [REV05-P051] | corrected fields: doi, role | raw cross-wired tuple is superseded by curated ADS identity
UNCITED_NOT_USABLE | [REV05-P035] Kewley, L. J., et al. (2010) | ADS:2010ApJ...721L..48K | Exact Kewley et al. 2010 ApJ 721 L48 bibcode/DOI is absent from the review's structured ar5iv bibliography.
UNCITED_NOT_USABLE | [REV05-P038] Pagel, M. E., et al. (1979) | ADS:1979MNRAS.189...95P | Exact Pagel et al. 1979 MNRAS 189, 95 bibcode/DOI is absent from the review's structured ar5iv bibliography.
UNCITED_NOT_USABLE | [REV05-P046] Kennicutt, R. C. (1998) | ADS:1998ARA&A..36..189K | Kennicutt 1998 is a supporting review, not a primary paper, and its exact bibcode/DOI is absent from the review bibliography.
UNCITED_NOT_USABLE | [REV05-P047] Bigiel, F., et al. (2008) | ADS:2008AJ....136.2846B | Exact Bigiel et al. 2008 AJ 136, 2846 bibcode/DOI is absent from the review's structured ar5iv bibliography.
UNCITED_NOT_USABLE | all metallicity calibrations share one absolute abundance scale | prohibited overclaim or temporal violation
UNCITED_NOT_USABLE | gas-phase, stellar, neutral-gas, CGM, and ICM metallicities are directly interchangeable | prohibited overclaim or temporal violation
UNCITED_NOT_USABLE | the FMR is universal and redshift-invariant | prohibited overclaim or temporal violation
UNCITED_NOT_USABLE | one radial gradient measures all chemical phases | prohibited overclaim or temporal violation
UNCITED_NOT_USABLE | matching the MZR validates one unique feedback model | prohibited overclaim or temporal violation
UNCITED_NOT_USABLE | post-2019, JWST, or machine-learning browsing results belong to this 2019 review harvest | prohibited overclaim or temporal violation

## 8. Review and Source Identity Ledger

[REV05-R00] Maiolino & Mannucci (2019, Astronomy and Astrophysics Review) | DOI:10.1007/s00159-018-0112-2; arXiv:1811.09642; ADS:2019A&ARv..27....3M | role=review_synthesis | 2019 review boundary

[REV05-P001] Tremonti, C. A., et al. (2004, The Astrophysical Journal) | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=measurement | Bounded to SDSS local fiber gas-phase metallicities.
[REV05-P002] Pettini, M., & Pagel, M. E. (2004, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2004.07591.x; arXiv:astro-ph/0401128; ADS:2004MNRAS.348L..59P | role=calibration | Bounded to O3N2 and N2 index empirical calibration scale.
[REV05-P003] Mannucci, F., et al. (2010, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1005.0006; ADS:2010MNRAS.408.2115M | role=measurement | Bounded to establishing the 3D M-Z-SFR manifold.
[REV05-P004] Curti, M., et al. (2017, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stw2766; arXiv:1610.06939; ADS:2017MNRAS.465.1384C | role=calibration | Bounded to Te-based empirical calibrations via stacked SDSS spectra.
[REV05-P005] Bothwell, M. S., et al. (2013, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stt817; arXiv:1304.4940; ADS:2013MNRAS.433.1425B | role=measurement | Bounded to HI gas mass dependence driving the FMR.
[REV05-P006] Cresci, G., et al. (2010, Nature) | DOI:10.1038/nature09451; arXiv:1010.2534; ADS:2010Natur.467..811C | role=measurement | Bounded to inverted gradients indicating cold gas accretion at z~3.
[REV05-P007] Peeples, M. S., et al. (2014, The Astrophysical Journal) | DOI:10.1088/0004-637X/786/1/54; arXiv:1310.2253; ADS:2014ApJ...786...54P | role=measurement | Bounded to accounting limits of retained vs. expelled galactic metals.
[REV05-P008] Zahid, H. J., et al. (2014, The Astrophysical Journal) | DOI:10.1088/0004-637X/791/2/130; arXiv:1404.7526; ADS:2014ApJ...791..130Z | role=analytic_theory | Bounded to modeling MZR saturation.
[REV05-P009] Werk, J. K., et al. (2014, The Astrophysical Journal) | DOI:10.1088/0004-637X/792/1/8; arXiv:1403.0947; ADS:2014ApJ...792....8W | role=measurement | Bounded to multiphase ionization modeling of the CGM.
[REV05-P010] Tumlinson, J., et al. (2011, Science) | DOI:10.1126/science.1209840; arXiv:1111.3980; ADS:2011Sci...334..948T | role=measurement | Bounded to OVI detection tracing massive metal reservoirs in the halos.
[REV05-P011] Lilly, S. J., et al. (2013, The Astrophysical Journal) | DOI:10.1088/0004-637X/772/2/119; arXiv:1303.5059; ADS:2013ApJ...772..119L | role=analytic_theory | Bounded to formulating the gas-regulator/bathtub model.
[REV05-P012] Bouché, N., et al. (2010, The Astrophysical Journal) | DOI:10.1088/0004-637X/718/2/1001; arXiv:0912.1858; ADS:2010ApJ...718.1001B | role=analytic_theory | Bounded to the interplay of inflows and SFR in setting abundances.
[REV05-P013] Davé, R., et al. (2012, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2011.20148.x; arXiv:1108.0426; ADS:2012MNRAS.421...98D | role=analytic_theory | Analytic equilibrium model for stellar, gas, and metal evolution; not a hydrodynamic simulation.
[REV05-P014] Andrews, B. H., & Martini, P. (2013, The Astrophysical Journal) | DOI:10.1088/0004-637X/765/2/140; arXiv:1211.3418; ADS:2013ApJ...765..140A | role=measurement | Bounded to establishing the MZR using stacked Te measurements.
[REV05-P015] Kewley, L. J., & Ellison, S. L. (2008, The Astrophysical Journal) | DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K | role=calibration | Bounded to systematic transformations between discrepant absolute scales.
[REV05-P016] Zaritsky, D., et al. (1994, The Astrophysical Journal) | DOI:10.1086/173544; arXiv:none; ADS:1994ApJ...420...87Z | role=measurement | Bounded to pioneering characterizations of radial abundance gradients.
[REV05-P017] Vila-Costas, M. A., & Edmunds, M. G. (1992, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/259.1.121; arXiv:none; ADS:1992MNRAS.259..121V | role=measurement | Bounded to classical chemical yield and local disk evolution limits.
[REV05-P018] Sánchez, S. F., et al. (2014, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201322343; arXiv:1311.7052; ADS:2014A&A...563A..49S | role=measurement | Bounded to defining a universal gradient slope normalized by Re.
[REV05-P019] Belfiore, F., et al. (2017, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stx789; arXiv:1703.03813; ADS:2017MNRAS.469..151B | role=measurement | Bounded to mapping local gradients across large mass samples.
[REV05-P020] Henry, R. B. C., et al. (2000, The Astrophysical Journal) | DOI:10.1086/309471; arXiv:astro-ph/0004299; ADS:2000ApJ...541..660H | role=analytic_theory | Bounded to models of primary vs secondary nitrogen production.
[REV05-P021] Izotov, Y. I., & Thuan, T. X. (1999, The Astrophysical Journal) | DOI:10.1086/306708; arXiv:astro-ph/9811387; ADS:1999ApJ...511..639I | role=measurement | Bounded to N/O and C/O measurements in extreme low-metallicity environments.
[REV05-P022] Garnett, D. R., et al. (1995, The Astrophysical Journal) | DOI:10.1086/175503; arXiv:astro-ph/9411011; ADS:1995ApJ...443...64G | role=measurement | Bounded to establishing the primary nitrogen floor.
[REV05-P023] Thomas, D., et al. (2005, The Astrophysical Journal) | DOI:10.1086/426932; arXiv:astro-ph/0410209; ADS:2005ApJ...621..673T | role=measurement | Bounded to alpha/Fe ratios charting rapid star formation in early-type galaxies.
[REV05-P024] Steidel, C. C., et al. (2014, The Astrophysical Journal) | DOI:10.1088/0004-637X/795/2/165; arXiv:1405.5473; ADS:2014ApJ...795..165S | role=measurement | Bounded to the BPT diagnostic shift at z~2.
[REV05-P025] Steidel, C. C., et al. (2016, The Astrophysical Journal) | DOI:10.3847/0004-637X/826/2/159; arXiv:1605.07186; ADS:2016ApJ...826..159S | role=measurement | Bounded to stellar binary impact on ionizing spectra at high redshift.
[REV05-P026] Strom, A. L., et al. (2017, The Astrophysical Journal) | DOI:10.3847/1538-4357/836/2/164; arXiv:1608.02587; ADS:2017ApJ...836..164S | role=measurement | Bounded to mass-metallicity scaling in the KBSS z~2 survey.
[REV05-P027] Erb, D. K., et al. (2006, The Astrophysical Journal) | DOI:10.1086/503623; arXiv:astro-ph/0602473; ADS:2006ApJ...644..813E | role=measurement | Bounded to pioneer measurements of the MZR at cosmic noon.
[REV05-P028] Maiolino, R., et al. (2008, Astronomy and Astrophysics) | DOI:10.1051/0004-6361:200809678; arXiv:0806.2410; ADS:2008A&A...488..463M | role=measurement | Bounded to downward normalization of the MZR at z>3.
[REV05-P029] Troncoso, P., et al. (2014, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201322099; arXiv:1311.4576; ADS:2014A&A...563A..58T | role=measurement | Bounded to AMAZE gas fraction limits and metal retention limits.
[REV05-P030] Marino, R. A., et al. (2013, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201321956; arXiv:1307.5316; ADS:2013A&A...559A.114M | role=calibration | Bounded to establishing updated linear index calibrations based on Te.
[REV05-P031] Pilyugin, L. S., & Grebel, E. K. (2016, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stw238; arXiv:1601.08217; ADS:2016MNRAS.457.3678P | role=calibration | Bounded to S-method application utilizing N/O diagnostics.
[REV05-P032] Edmunds, M. G. (1990, Monthly Notices of the Royal Astronomical Society) | DOI:none; arXiv:none; ADS:1990MNRAS.246..678E | role=analytic_theory | Bounded to defining effective yield dependencies and mass-loss mechanisms.
[REV05-P033] Peeples, M. S., & Shankar, F. (2011, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2011.19456.x; arXiv:1007.3743; ADS:2011MNRAS.417.2962P | role=analytic_theory | Bounded to connecting stellar fractions to gas-phase constraints.
[REV05-P034] Ho, I-Ting, et al. (2015, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stv067; arXiv:1501.02668; ADS:2015MNRAS.448.2030H | role=measurement | Bounded to measuring gradient flattening due to tidal inflow.
[REV05-P036] Jones, T., et al. (2013, The Astrophysical Journal) | DOI:10.1088/0004-637X/765/1/48; arXiv:1207.4489; ADS:2013ApJ...765...48J | role=measurement | Bounded to identifying flat and inverted gradients via lensing.
[REV05-P037] Tinsley, B. M. (1980, Fundamentals of Cosmic Physics) | DOI:none; arXiv:none; ADS:1980FCPh....5..287T | role=supporting_review | Foundational broad chemical-evolution synthesis; supporting review, not primary evidence.
[REV05-P039] McGaugh, S. S. (1991, The Astrophysical Journal) | DOI:10.1086/170569; arXiv:none; ADS:1991ApJ...380..140M | role=calibration | Bounded to theoretical photoionization R23 modeling.
[REV05-P040] Lequeux, J., et al. (1979, Astronomy and Astrophysics) | DOI:none; arXiv:none; ADS:1979A&A....80..155L | role=measurement | Bounded to originating observations tying mass/luminosity to metal abundance.
[REV05-P041] Lara-López, M. A., et al. (2010, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201014803; arXiv:1005.0509; ADS:2010A&A...521L..53L | role=measurement | Bounded to codifying the FMR manifold as a principal component plane.
[REV05-P042] Salim, S., et al. (2014, The Astrophysical Journal) | DOI:10.1088/0004-637X/797/2/126; arXiv:1411.7391; ADS:2014ApJ...797..126S | role=measurement | Bounded to SFR dependency limits on global SDSS scales.
[REV05-P043] Asplund, M., et al. (2009, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev.astro.46.060407.145222; arXiv:0909.0948; ADS:2009ARA&A..47..481A | role=supporting_review | Solar-abundance synthesis that anchors zero points; supporting review, not primary evidence.
[REV05-P044] Izotov, Y. I., et al. (2006, Astronomy and Astrophysics) | DOI:10.1051/0004-6361:20053763; arXiv:astro-ph/0511644; ADS:2006A&A...448..955I | role=measurement | Bounded to assessing Te structural uncertainties.
[REV05-P045] Bresolin, F., et al. (2009, The Astrophysical Journal) | DOI:10.1088/0004-637X/700/1/309; arXiv:0905.2791; ADS:2009ApJ...700..309B | role=measurement | Bounded to resolving Te-based gradient slopes in a nearby analog.
[REV05-P048] Davé, R., Finlator, K., & Oppenheimer, B. D. (2011, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2011.19132.x; arXiv:1104.3156; ADS:2011MNRAS.416.1354D | role=hydrodynamic_simulation | Bounded to wind-recycling impact on scaling relations.
[REV05-P049] Carton, D., et al. (2018, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/sty1343; arXiv:1805.08131; ADS:2018MNRAS.478.4293C | role=measurement | Bounded to MUSE/MUSE-Wide gradient studies.
[REV05-P050] Torrey, P., et al. (2018, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnrasl/sly031; arXiv:1711.11039; ADS:2018MNRAS.477L..16T | role=hydrodynamic_simulation | Bounded to linking FMR scatter to cyclical SFR-metallicity oscillation timescales.
[REV05-P051] Garnett, D. R. (2002, The Astrophysical Journal) | DOI:10.1086/344301; arXiv:astro-ph/0209012; ADS:2002ApJ...581.1019G | role=measurement | Observed luminosity-metallicity relation and effective-yield limits in nearby spirals and irregulars.

REVIEW_BASE_05_DR_COMPLETE_REFERENCE_ONLY

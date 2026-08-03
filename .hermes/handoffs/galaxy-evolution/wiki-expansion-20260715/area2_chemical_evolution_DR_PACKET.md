# Area 2 verified evidence packet — galaxy chemical evolution

status: READY_FOR_HWAO_REVIEW
advisory_only: true
broad_non_agn: true
distinct_from_area1_mzr: true
wiki_write_performed_by_tori: false
conversation_deleted: false

Deep Research conversation: `2ac7b49f57f07194`
Raw Deep Research capture: `area2_chemical_evolution_DR_RAW_PACKET.md`
Raw capture SHA-256: `5a877ee469067716f7c11bc8e3bc6ad1a25e7c5cf41ca6527713490c6bb7313e`
Curated source registry: `area2_chemical_evolution_CURATED_SOURCE_REGISTRY.json`
Identifier reconciliation: PASS, 29/29 curated sources

Verification method: every curated row was reconciled as one bibliographic identity across an exact public NASA ADS/SciX bibcode result, Crossref DOI metadata where a DOI exists, and arXiv metadata where an arXiv identifier exists. The local ADS API credentials returned HTTP 401 during this run, so this packet does not claim ADS-API verification. It does claim that every listed ADS bibcode resolves publicly to the expected paper and that the DOI/arXiv tuples were independently reconciled. Hwao's separate ADS-verifier and jury remain the final live-wiki gate.

## Scope boundary

This packet covers enrichment history and process: stellar production channels and delays, abundance ratios, chemical-evolution models, radial gradients, gas flows, metal retention, and the G-dwarf problem. It uses the MZR/FMR only where they constrain dilution, gas fraction, metal loading, or enrichment history. It does not duplicate Area 1's broad MZR scaling-law map. Gas-phase and stellar metallicities, global and resolved observations, and measurements and models are kept distinct. AGN/NLR abundance work is excluded from usable findings.

## 1. Established findings

[CHEM-E01]
role: established
finding: At fixed stellar mass and with redshift-appropriate abundance calibrations, typical gas-phase O/H decreases toward higher redshift over z=0–3.3. This is an enrichment-history constraint, not evidence for one unique mechanism.
scope/boundary: MOSDEF star-forming samples at z~2.3 and z~3.3 compared with local samples; gas-phase oxygen abundance only. Do not export the numerical evolution across different diagnostics without recalibration.
evidence: Sanders et al. measure dlog(O/H)/dz=-0.11±0.02 and model contributions from both higher gas fractions and stronger metal removal. Maiolino & Mannucci review the broader evidence and systematic limits.
trust_score: 0.92
sources: [Sanders2021, MaiolinoMannucci2019]

[CHEM-E02]
role: established
finding: The closed-box model is a useful null model, but real galaxy chemical histories generally require gas exchange and finite stellar delay times. Continuous or episodic infall is a standard resolution of the local G-dwarf problem; outflow and recycling are needed for broader baryon and metal accounting.
scope/boundary: The classic G-dwarf problem is a Milky Way disk stellar-metallicity-distribution constraint. It is not proof that all galaxies follow one infall history or that closed-box equations are never useful.
evidence: Tinsley established the simple-model framework and its limitations. Chiappini et al. show one successful two-infall realization; Matteucci reviews alternative Milky Way histories. Lilly and Weinberg provide explicit regulator/open-box solutions.
trust_score: 0.95
sources: [Tinsley1980, Chiappini1997, Matteucci2021, Lilly2013, Weinberg2017]

[CHEM-E03]
role: established
finding: Core-collapse supernovae provide prompt enrichment dominated by alpha elements and other massive-star products, while Type Ia supernovae add iron-peak material over a broad delay-time distribution. This time delay makes abundance-ratio tracks sensitive to star-formation history.
scope/boundary: Element yields depend on progenitor mass, metallicity, rotation, explosion physics, binary evolution, and IMF. “Prompt alpha” and “delayed Fe” are organizing approximations, not pure one-source labels for every element.
evidence: Nomoto et al. synthesize massive-star and supernova yields. Maoz et al. recover an approximately t^-1 Type-Ia DTD in Sloan-II hosts; the progenitor mixture remains debated.
trust_score: 0.96
sources: [Nomoto2013, MaozBrandt2012, MaozNelemans2014]

[CHEM-E04]
role: established
finding: Low- and intermediate-mass stars return carbon, nitrogen, and s-process material through the AGB phase on mass-dependent delays ranging from roughly 10^8 years to many Gyr. Their contribution relative to massive stars is strongly metallicity- and model-dependent.
scope/boundary: Do not describe AGB stars as the unique source of all carbon or nitrogen. The mass boundaries, hot-bottom burning, dredge-up, mass loss, rotation, and binary effects vary between yield grids.
evidence: Karakas & Lattanzio review AGB nucleosynthesis and yield dependencies. Nomoto et al. and Henry et al. place AGB and massive-star channels in a galaxy-enrichment context.
trust_score: 0.94
sources: [KarakasLattanzio2014, Nomoto2013, Henry2000]

[CHEM-E05]
role: established
finding: [alpha/Fe] carries information about the duration and timing of star formation relative to Type-Ia enrichment. Under fixed IMF and yield assumptions, high [alpha/Fe] generally indicates that much of the stellar population formed before delayed iron became dominant.
scope/boundary: [alpha/Fe] is not a pure clock. IMF variation, metallicity-dependent yields, burstiness, selective flows, stellar-population modeling, and the chosen alpha element can produce degeneracies.
evidence: Thomas et al. use integrated early-type-galaxy populations to infer formation timescales. Matteucci reviews the time-delay interpretation; Johnson & Weinberg show how bursts alter abundance-ratio tracks.
trust_score: 0.87
sources: [Thomas2005, Matteucci2021, JohnsonWeinberg2020]

[CHEM-E06]
role: established
finding: N/O commonly shows a low-metallicity plateau and rises at higher O/H. This behavior is consistent with a primary-nitrogen component plus metallicity-dependent and delayed nitrogen production, including low/intermediate-mass-star channels.
scope/boundary: The plateau level and transition are population-, calibration-, and yield-dependent. The pattern does not prove that one stellar mass range supplies all primary nitrogen.
evidence: Vincenzo et al. compile local N/O and O/H data and chemical models; Henry et al. examine distinct carbon and nitrogen production sites.
trust_score: 0.91
sources: [Vincenzo2016, Henry2000]

[CHEM-E07]
role: established
finding: C/O is also a delayed- and metallicity-sensitive diagnostic because both massive stars and lower-mass/AGB stars contribute carbon, while oxygen is dominated by massive-star production. C/O therefore responds to stellar lifetimes, mass loss, metallicity-dependent yields, and star-formation history.
scope/boundary: Relative channel weights are model-dependent and cannot be inferred from C/O alone without an ionization, depletion, and abundance-calibration model.
evidence: Henry et al. separate the modeled carbon and nitrogen production sites; Karakas & Lattanzio and Nomoto et al. provide complementary yield reviews.
trust_score: 0.86
sources: [Henry2000, KarakasLattanzio2014, Nomoto2013]

[CHEM-E08]
role: established
finding: Many non-interacting local star-forming disks have negative radial gas-phase oxygen-abundance gradients when radius is normalized by disk size. The trend is consistent with inside-out growth, but gradient amplitude and shape vary with galaxy properties, interactions, radial range, and diagnostic.
scope/boundary: Local resolved H II-region/emission-line measurements. This is not a universal statement about dwarfs, mergers, stellar gradients, or high-redshift disks.
evidence: CALIFA found a characteristic slope in selected disks; MaNGA mapped systematic O/H and N/O radial behavior across a larger local sample.
trust_score: 0.90
sources: [Sanchez2014, Belfiore2017]

[CHEM-E09]
role: established
finding: Stellar radial migration can change a disk's stellar metallicity distribution and flatten or broaden stellar abundance gradients without requiring strong orbital heating. Present-day stellar position therefore need not equal birth radius.
scope/boundary: This is a dynamical mechanism and a warning for stellar fossil-record interpretation. It does not directly establish a universal migration amplitude or explain every age-metallicity outlier; it must not be substituted for gas-phase mixing.
evidence: Sellwood & Binney demonstrate corotation-driven radial mixing in disk models.
trust_score: 0.91
sources: [SellwoodBinney2002]

[CHEM-E10]
role: established
finding: Gas-phase metallicity and stellar metallicity are different observables: nebular emission traces the present star-forming ISM, whereas absorption-line stellar metallicity is a weighted record of stars formed over earlier enrichment states. Their relation varies with mass, radius, star-formation history, and measurement method.
scope/boundary: MaNGA spiral-galaxy sample and spectral-model assumptions. Do not combine gas O/H and total stellar Z on one numerical scale without conversion.
evidence: Greener et al. analyze spatially resolved gas and stellar chemical co-evolution in spirals; Kewley et al. review emission-line systematics.
trust_score: 0.88
sources: [Greener2022, Kewley2019]

[CHEM-E11]
role: established
finding: In several local calibrations and samples, gas-phase metallicity anticorrelates with SFR at fixed stellar mass. This FMR-like behavior is useful as a process diagnostic for gas fraction, dilution, enrichment, and metal loading, but it does not uniquely identify inflow or outflow.
scope/boundary: Global/fiber measurements, sample-selection and abundance-calibration dependent. It is retained here only for chemical-process interpretation, not as a duplicate Area-1 scaling-relation entry.
evidence: Mannucci et al. introduced the local FMR; Curti et al. recover a low-scatter direct-method version; Lilly et al. show how gas-regulator variables can generate such behavior.
trust_score: 0.84
sources: [Mannucci2010, Curti2020, Lilly2013]

[CHEM-E12]
role: established
finding: A large fraction of metals produced by star-forming galaxies is not retained in their stars, interstellar gas, and dust. Circumgalactic and expelled reservoirs are therefore required components of galaxy chemical evolution.
scope/boundary: z~0 COS-Halos-scale accounting and review synthesis. The exact missing-metal fraction depends on stellar yields, ionization corrections, dust, hot gas, and radius.
evidence: Peeples et al. construct a metal budget around z~0 star-forming galaxies; Péroux & Howk review the measured and inferred baryon/metal cycle.
trust_score: 0.91
sources: [Peeples2014, PerouxHowk2020]

[CHEM-E13]
role: established
finding: Neutron-capture enrichment has at least two distinct process families: slow neutron capture (s-process), with major AGB contributions, and rapid neutron capture (r-process), which requires much higher neutron fluxes and different explosive sites. Their abundance signatures and delays must not be merged into one generic “heavy-element” channel.
scope/boundary: The process distinction is secure; the relative astrophysical r-process site mixture and galaxy-scale delay distribution are not settled by the historical review sources in this packet.
evidence: Karakas & Lattanzio review AGB s-process production; Cowan et al. review r-process requirements and nucleochronology; Nomoto et al. place explosive yields in the wider enrichment context.
trust_score: 0.90
sources: [KarakasLattanzio2014, Cowan1991, Nomoto2013]

## 2. Open debates and tensions

[CHEM-D01]
role: debate
debate_topic: Type-Ia progenitor channels and DTD normalization.
competing_positions: The observed near-t^-1 DTD is naturally associated with double-degenerate merger delay physics, but single-degenerate, sub-Chandrasekhar, double-detonation, and mixed populations may contribute. A DTD shape does not uniquely select an explosion channel.
why_unresolved: Common-envelope evolution, binary demographics, explosion efficiencies, selection effects, and host star-formation histories remain uncertain.
boundary: The DTD shape is more secure than the channel mixture.
trust_score: 0.94
sources: [MaozBrandt2012, MaozNelemans2014]

[CHEM-D02]
role: debate
debate_topic: Whether [alpha/Fe] variation is mainly a star-formation-timescale signal or also requires IMF/yield variation.
competing_positions: Classical time-delay models explain high [alpha/Fe] with rapid early star formation. Alternative or additional explanations invoke IMF changes, metallicity-dependent massive-star yields, selective metal loss, or burst timing.
why_unresolved: Integrated spectra and abundance tracks combine several degenerate quantities; direct low-mass IMF and yield constraints are difficult, especially outside the Local Group.
boundary: Do not invert one [alpha/Fe] value into one formation duration without a model.
trust_score: 0.86
sources: [Thomas2005, Nomoto2013, Matteucci2021, JohnsonWeinberg2020]

[CHEM-D03]
role: debate
debate_topic: The origin of extreme N/O in very young high-redshift systems.
competing_positions: Proposed channels include rapidly rotating or otherwise unusual massive stars, dense-cluster self-enrichment, tidal-disruption-related emission, and faster-than-assumed intermediate-mass enrichment. Source classification and ionization corrections can also mimic abundance anomalies.
why_unresolved: Individual objects have limited line sets and may not be clean non-AGN star-forming systems; population statistics and robust direct abundance constraints remain sparse.
boundary: Cameron et al.'s GN-z11 result is a debate case only. It is not usable as an established non-AGN population claim.
trust_score: 0.73
sources: [Cameron2023, Vincenzo2016, Henry2000]

[CHEM-D04]
role: debate
debate_topic: Direction and driver of radial gas-phase metallicity-gradient evolution at z~1–3.
competing_positions: Inside-out models can predict initially steeper gradients that flatten; observations also find many flat or positive gradients, potentially from mixing, inflow, feedback, interactions, or limited resolution.
why_unresolved: Beam smearing, inclination, compact sizes, diagnostic evolution, clumps, mergers, and small samples can change recovered slopes. Wuyts et al. show recovery fractions vary strongly with geometry.
boundary: High-redshift gas-phase gradients only; do not mix with present-day stellar gradients.
trust_score: 0.88
sources: [Stott2014, Wuyts2016, Sanchez2014]

[CHEM-D05]
role: debate
debate_topic: Inflow versus outflow/metal-loading dominance in FMR-like residuals and metallicity evolution.
competing_positions: Low-Z accretion can dilute the ISM and raise SFR, while metal-loaded winds can lower effective yields; gas fraction and recycling can produce similar observables. Regulator models usually contain all of these terms simultaneously.
why_unresolved: Instantaneous inflow rates, outflow mass loading, metal loading, and recycled fractions are not routinely measured for the same representative galaxies.
boundary: Global correlations do not identify a unique causal direction.
trust_score: 0.85
sources: [Lilly2013, Mannucci2010, Weinberg2017, Sanders2021, PerouxHowk2020]

[CHEM-D06]
role: debate
debate_topic: When equilibrium/gas-regulator approximations are adequate.
competing_positions: Slowly varying systems can approach regulator solutions, while bursts, mergers, rapid accretion, and early low-mass galaxies may be far from equilibrium and retain memory of individual events.
why_unresolved: Gas masses, flow rates, metal loading, mixing times, and burst histories are poorly constrained together, especially at high redshift.
boundary: “Equilibrium” is a timescale-dependent approximation, not an observed universal state.
trust_score: 0.87
sources: [Lilly2013, Weinberg2017, Sanders2021]

[CHEM-D07]
role: debate
debate_topic: Which infall history resolves the G-dwarf problem and disk abundance structure.
competing_positions: Continuous infall, two-infall, three-infall, pre-enrichment, radial migration, radial gas flows, and selection effects can all alter the local metallicity distribution.
why_unresolved: Solar-neighborhood samples are not a closed system, stellar ages/abundances have correlated errors, and distinct models can fit overlapping diagnostics.
boundary: The classic deficit rejects a strict simple closed box for the local disk; it does not uniquely select two discrete infalls.
trust_score: 0.89
sources: [Tinsley1980, Chiappini1997, Matteucci2021, SellwoodBinney2002]

[CHEM-D08]
role: debate
debate_topic: The absolute gas-phase abundance zero point.
competing_positions: Direct electron-temperature, recombination-line, empirical strong-line, and photoionization-model calibrations can give different O/H values because of temperature structure, ionization, depletion, DIG, and model assumptions.
why_unresolved: The faint lines and spatial scales needed to isolate these effects are unavailable for many representative and high-redshift samples.
boundary: Relative trends measured consistently can be more robust than cross-calibration absolute values.
trust_score: 0.96
sources: [KewleyEllison2008, Kewley2019, Curti2020]

## 3. Key measurements and numbers

[CHEM-N01]
role: measurement
metric: Type-Ia DTD power-law index
value: t^(-1.07±0.07)
scope/method: Sloan-II supernovae mapped to reconstructed host star-formation histories; model and SFH assumptions apply.
trust_score: 0.94
sources: [MaozBrandt2012]

[CHEM-N02]
role: measurement
metric: Time-integrated Type-Ia production efficiency
value: 0.00130±0.00015 SNe Ia per solar mass formed
scope/method: Same Sloan-II DTD reconstruction and IMF convention; not a universal channel efficiency independent of IMF.
trust_score: 0.92
sources: [MaozBrandt2012]

[CHEM-N03]
role: measurement
metric: Low-metallicity N/O plateau used in the cited local compilation/model comparison
value: log(N/O) approximately -1.6 dex
scope/method: Local low-metallicity systems and the cited abundance compilation; sample/calibration scatter applies.
trust_score: 0.87
sources: [Vincenzo2016]

[CHEM-N04]
role: measurement
metric: Characteristic local disk oxygen-abundance gradient
value: approximately -0.1 dex per effective radius
scope/method: Selected non-interacting CALIFA disks over approximately 0.3–2 effective radii with the paper's adopted diagnostic.
trust_score: 0.91
sources: [Sanchez2014]

[CHEM-N05]
role: measurement
metric: Residual scatter around the cited direct-method local FMR fit
value: 0.054 dex
scope/method: Curti et al.'s local stacked Te-based calibration and fitted sample only.
trust_score: 0.90
sources: [Curti2020]

[CHEM-N06]
role: measurement
metric: Cross-calibration spread in local strong-line metallicity scales
value: up to approximately 0.7 dex
scope/method: Kewley & Ellison's comparison of then-common calibrations; not the error bar of every modern individual estimate.
trust_score: 0.95
sources: [KewleyEllison2008]

[CHEM-N07]
role: measurement
metric: Redshift evolution of gas O/H at fixed stellar mass in the cited MOSDEF/local comparison
value: dlog(O/H)/dz = -0.11±0.02 over z=0–3.3
scope/method: Redshift-appropriate calibrations and the paper's sample/model choices.
trust_score: 0.92
sources: [Sanders2021]

[CHEM-N08]
role: measurement
metric: z~0 metal retention/accounting in the cited COS-Halos budget
value: approximately 20–25% of produced metals retained in stars+ISM gas+dust; approximately 40% readily accounted for within 150 kpc for Mstar~10^10 solar-mass systems when CGM phases are included
scope/method: Yield, dust, ionization, hot-gas, aperture, and galaxy-selection assumptions apply.
trust_score: 0.88
sources: [Peeples2014]

[CHEM-N09]
role: measurement
metric: Beam-smearing recovery of intrinsic high-redshift gradients in the cited KMOS3D model
value: up to approximately 70% for large face-on disks, but only approximately 30% for smaller more inclined systems
scope/method: Smooth-gradient forward model under the KMOS3D seeing and geometry assumptions.
trust_score: 0.90
sources: [Wuyts2016]

## 4. What remains unknown

[CHEM-U01]
role: future
gap: A cross-method absolute gas-phase abundance scale that remains reliable across metallicity, ionization state, DIG fraction, redshift, and spatial resolution.
why_it_matters: Absolute yields, metal masses, and cross-survey evolution shift with the zero point.
sources: [KewleyEllison2008, Kewley2019, Curti2020]

[CHEM-U02]
role: future
gap: Population-level intrinsic metallicity-gradient distributions at z>1 after robust beam-smearing, clump, merger, inclination, and diagnostic corrections.
why_it_matters: The sign and evolution of gradients distinguish inside-out growth, mixing, inflow, and feedback models.
sources: [Stott2014, Wuyts2016]

[CHEM-U03]
role: future
gap: Simultaneous empirical constraints on inflow rate, outflow mass loading, metal loading, recycling, gas mass, and ISM metallicity for representative galaxies.
why_it_matters: Current observables usually cannot separate dilution from metal ejection or recycling.
sources: [Lilly2013, PerouxHowk2020, Sanders2021]

[CHEM-U04]
role: future
gap: The relative Type-Ia contribution of single-degenerate, double-degenerate, sub-Chandrasekhar, and other channels as a function of population age and metallicity.
why_it_matters: Iron-delay kernels propagate into every abundance-ratio chemical clock.
sources: [MaozNelemans2014, MaozBrandt2012]

[CHEM-U05]
role: future
gap: Yield grids with jointly constrained rotation, binaries, mass loss, explosion physics, IMF, and metallicity for C, N, alpha, Fe-peak, and neutron-capture elements.
why_it_matters: Yield/IMF uncertainty is degenerate with inferred star-formation and gas-flow histories.
sources: [Nomoto2013, KarakasLattanzio2014, Henry2000]

[CHEM-U06]
role: future
gap: Clean non-AGN high-redshift samples with direct or multi-element C/O and N/O measurements and source-classification controls.
why_it_matters: Individual extreme-N objects cannot yet establish a population-wide early enrichment channel.
sources: [Cameron2023, Kewley2019]

## 5. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | Raw merged source ledger rows | structural ambiguity | The DR answer concatenated multiple citations without line boundaries; use only the curated ledger below.

UNCITED_NOT_USABLE | Maoz, Mannucci & Nelemans (2014) with DOI 10.1146/annurev-astro-082812-140956 | composite identifier mismatch | That DOI resolves to Nomoto, Kobayashi & Tominaga (2013). Correct Maoz DOI: 10.1146/annurev-astro-082812-141031.

UNCITED_NOT_USABLE | “Yates et al. (2022), 2022MNRAS.516.1275Y, DOI 10.1093/mnras/stac2205” | author+bibcode+DOI mismatch | The intended chemical co-evolution paper is Greener et al., DOI 10.1093/mnras/stac2355, arXiv:2208.09008, ADS:2022MNRAS.516.1275G. The raw DOI resolves to an unrelated Fu et al. DECODE paper.

UNCITED_NOT_USABLE | “Stott et al. (2013), DOI 10.1093/mnras/stt1836, arXiv:1309.6321, ADS:2013MNRAS.436.1130S” used for metallicity gradients | composite identifier and claim mismatch | The DOI, arXiv, and bibcode point to unrelated papers/FMR work. The intended gradient paper is Stott et al. (2014), DOI 10.1093/mnras/stu1343, arXiv:1407.1047, ADS:2014MNRAS.443.2695S.

UNCITED_NOT_USABLE | “Closed-box models fail universally and gas regulators are universally required” | overbroad model claim | Closed-box remains a useful null model; which open-box history is required depends on system and observable.

UNCITED_NOT_USABLE | “Gas and stellar metallicities evolve synchronously in low-mass spirals and profoundly decouple in all high-mass spirals” | overgeneralization | Retain only the bounded MaNGA sample result with spectral/model caveats.

UNCITED_NOT_USABLE | “AGB stars are the definitive source of carbon, secondary nitrogen, and half of all heavy elements” | overbroad nucleosynthetic allocation | Contributions depend on mass, metallicity, yields, binaries, and element; r-process and s-process channels must remain distinct.

UNCITED_NOT_USABLE | “The N/O plateau universally proves primary nitrogen from massive stars” | non-unique inference | A plateau exists in the cited compilation, but production-site allocation and delay depend on yield models and stellar populations.

UNCITED_NOT_USABLE | “All local star-forming disks universally have negative gradients” | population overreach | Use the bounded CALIFA/MaNGA findings; mergers, dwarfs, bars, outer disks, and calibrations can differ.

UNCITED_NOT_USABLE | “Radial migration is the direct observed cause of every local age-metallicity outlier” | causal overreach | Sellwood & Binney establish a mechanism, not a universal attribution or amplitude.

UNCITED_NOT_USABLE | “FMR deviations strictly diagnose inflow and persist unevolved across cosmic time” | causal and redshift overreach | Retain sample/calibration-specific correlations and competing inflow/outflow/regulator explanations.

UNCITED_NOT_USABLE | GN-z11 extreme N/O as an established clean non-AGN population result | source-classification and generalization risk | Keep Cameron et al. only as a debate/caveat case.

UNCITED_NOT_USABLE | Dors et al. AGN/NLR abundance calibrations and AGN-centric source anchors | excluded scope | Area 2 is broad non-AGN galaxy chemical evolution.

UNCITED_NOT_USABLE | Thesis fragments, Wikipedia, ResearchGate-only mirrors, anonymous model snippets, unrelated chemistry pages, and 2026 search-result anchors | unresolved/non-primary/temporally out-of-scope | None are promoted into curated claims.

UNCITED_NOT_USABLE | Any source tuple not present in the 29-row curated registry | no composite reconciliation | Quarantine until exact author/year/title/DOI/arXiv/ADS identity is independently reconciled.

## 6. Source identity ledger

Tinsley (1980, Fundamentals of Cosmic Physics) | arXiv:2203.02041 [later scan]; ADS:1980FCPh....5..287T | role=orientation,established | Foundational chemical-evolution equations, delayed enrichment, simple-model limits, and the G-dwarf problem.

Mannucci et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1005.0006; ADS:2010MNRAS.408.2115M | role=established,debate | Original FMR sample/calibration; not a universal mechanism proof.

Lilly et al. (2013, ApJ) | DOI:10.1088/0004-637X/772/2/119; arXiv:1303.5059; ADS:2013ApJ...772..119L | role=theory,established,debate | Analytic gas-regulator framework under explicit equilibrium assumptions.

Kewley et al. (2019, ARA&A) | DOI:10.1146/annurev-astro-081817-051832; arXiv:1910.09730; ADS:2019ARA&A..57..511K | role=orientation,caveat | Emission-line diagnostics, ionization, DIG, and abundance-systematic review.

Maoz, Mannucci & Brandt (2012, MNRAS) | DOI:10.1111/j.1365-2966.2012.21871.x; arXiv:1206.0465; ADS:2012MNRAS.426.3282M | role=established,measurement | Sloan-II Type-Ia DTD reconstruction.

Maoz, Mannucci & Nelemans (2014, ARA&A) | DOI:10.1146/annurev-astro-082812-141031; arXiv:1312.0628; ADS:2014ARA&A..52..107M | role=orientation,debate | Type-Ia progenitor and DTD review.

Karakas & Lattanzio (2014, PASA) | DOI:10.1017/pasa.2014.21; arXiv:1405.0062; ADS:2014PASA...31...30K | role=orientation,established,debate | Low/intermediate-mass and AGB nucleosynthesis/yields.

Vincenzo et al. (2016, MNRAS) | DOI:10.1093/mnras/stw532; arXiv:1603.00460; ADS:2016MNRAS.458.3466V | role=established,measurement,debate | Local N/O–O/H compilation and models.

Curti et al. (2020, MNRAS) | DOI:10.1093/mnras/stz2910; arXiv:1910.00597; ADS:2020MNRAS.491..944C | role=established,measurement,caveat | Local stacked Te-based MZR/FMR calibration.

Cameron et al. (2023, MNRAS) | DOI:10.1093/mnras/stad1579; arXiv:2302.10142; ADS:2023MNRAS.523.3516C | role=debate,caveat | GN-z11 nitrogen-enhancement case with competing source interpretations.

Greener et al. (2022, MNRAS) | DOI:10.1093/mnras/stac2355; arXiv:2208.09008; ADS:2022MNRAS.516.1275G | role=established,caveat | MaNGA gas/stellar chemical co-evolution in spirals.

Belfiore et al. (2017, MNRAS) | DOI:10.1093/mnras/stx789; arXiv:1703.03813; ADS:2017MNRAS.469..151B | role=established,caveat | Local MaNGA O/H and N/O gradients.

Sellwood & Binney (2002, MNRAS) | DOI:10.1046/j.1365-8711.2002.05806.x; arXiv:astro-ph/0203510; ADS:2002MNRAS.336..785S | role=theory,established | Corotation-driven stellar radial mixing mechanism.

Stott et al. (2014, MNRAS) | DOI:10.1093/mnras/stu1343; arXiv:1407.1047; ADS:2014MNRAS.443.2695S | role=debate,caveat | z~1 KMOS-HiZELS gradient and sSFR study.

Cowan, Thielemann & Truran (1991, Physics Reports) | DOI:10.1016/0370-1573(91)90070-3; ADS:1991PhR...208..267C | role=orientation | Historical r-process and nucleochronology review.

Nomoto, Kobayashi & Tominaga (2013, ARA&A) | DOI:10.1146/annurev-astro-082812-140956; ADS:2013ARA&A..51..457N | role=orientation,established,debate | Massive-star and supernova nucleosynthesis/yield review.

Maiolino & Mannucci (2019, A&ARv) | DOI:10.1007/s00159-018-0112-2; arXiv:1811.09642; ADS:2019A&ARv..27....3M | role=orientation | Broad cosmic chemical-evolution review.

Matteucci (2021, A&ARv) | DOI:10.1007/s00159-021-00133-8; arXiv:2106.13145; ADS:2021A&ARv..29....5M | role=orientation,established,debate | Milky Way chemical-evolution model review.

Weinberg, Andrews & Freudenburg (2017, ApJ) | DOI:10.3847/1538-4357/837/2/183; arXiv:1604.07435; ADS:2017ApJ...837..183W | role=theory,debate | One-zone equilibrium and sudden-event solutions.

Sánchez et al. (2014, A&A) | DOI:10.1051/0004-6361/201322343; arXiv:1311.7052; ADS:2014A&A...563A..49S | role=established,measurement,caveat | Characteristic CALIFA disk oxygen gradient.

Wuyts et al. (2016, ApJ) | DOI:10.3847/0004-637X/827/1/74; arXiv:1603.01139; ADS:2016ApJ...827...74W | role=measurement,debate,caveat | z=0.6–2.7 KMOS3D metallicities, gradients, and beam smearing.

Peeples et al. (2014, ApJ) | DOI:10.1088/0004-637X/786/1/54; arXiv:1310.2253; ADS:2014ApJ...786...54P | role=established,measurement | z~0 COS-Halos metal budget.

Thomas et al. (2005, ApJ) | DOI:10.1086/426932; arXiv:astro-ph/0410209; ADS:2005ApJ...621..673T | role=established,debate | Early-type integrated populations and alpha/Fe timescale inference.

Johnson & Weinberg (2020, MNRAS) | DOI:10.1093/mnras/staa2431; arXiv:1911.02598; ADS:2020MNRAS.498.1364J | role=theory,debate | Starburst effects on abundance-ratio tracks.

Chiappini, Matteucci & Gratton (1997, ApJ) | DOI:10.1086/303726; arXiv:astro-ph/9609199; ADS:1997ApJ...477..765C | role=theory,debate | Milky Way two-infall model.

Henry, Edmunds & Köppen (2000, ApJ) | DOI:10.1086/309471; arXiv:astro-ph/0004299; ADS:2000ApJ...541..660H | role=orientation,established,debate | Modeled carbon and nitrogen production sites.

Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=established,measurement,caveat | z=0–3.3 gas O/H evolution with redshift-appropriate calibrations.

Péroux & Howk (2020, ARA&A) | DOI:10.1146/annurev-astro-021820-120014; arXiv:2011.01935; ADS:2020ARA&A..58..363P | role=orientation,established,debate | Cosmic baryon and metal cycles review.

Kewley & Ellison (2008, ApJ) | DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K | role=measurement,caveat | Local strong-line calibration comparison.

CHEM_DR_PACKET_COMPLETE_REFERENCE_ONLY

## Custody and safety receipt

- One prompt submission and one Research Start action were accepted in conversation `2ac7b49f57f07194`; no duplicate resend occurred.
- The raw answer was preserved byte-for-byte before curation.
- No Google challenge or google.com/sorry was observed.
- No DB, wiki, trust-score, claim/evidence, deploy, git, publish, billing, account-setting, or unrelated-conversation mutation was performed.
- No conversation deletion was authorized or performed.
- This is an advisory packet for Hwao's ADS-verifier, jury, and separate live-wiki approval gate.

# Area 1 verified evidence packet — stellar mass–metallicity relation

status: READY_FOR_HWAO_REVIEW
advisory_only: true
broad_non_agn: true
wiki_write_performed_by_tori: false
live_publish_authorization_consumed: false
independent_identifier_verification: PASS_19_OF_19
independent_claim_boundary_review: PASS_WITH_QUARANTINES

## Provenance and use rule

- Deep Research conversation: `17659460ae83f48a`
- Deep Research submitted: `2026-07-15T06:39:47.360427Z`
- Deep Research started: `2026-07-15T06:40:16.290360Z`
- Raw result captured: `2026-07-15T06:53:13.859569Z`
- Immutable raw packet: `area1_mass_metallicity_DR_RAW_PACKET.md`
- Immutable raw SHA-256: `2f2c4d46bf0583058069d3eb04489f0fb46891cfc719f3c58eaaad34b0094112`
- Curated ADS registry: `area1_mass_metallicity_CURATED_SOURCE_REGISTRY.json`
- Verification method: exact NASA ADS bibcode lookup, with DOI and arXiv reconciliation against ADS identifiers and abstract-level claim-boundary review.
- This packet replaces the raw report for downstream use. The raw report contains identifier contamination and unsupported overstatements retained only for audit.

Trust scale used below:

- `0.95-1.00`: identity verified; direct primary result or tightly bounded calibration result; broad agreement.
- `0.85-0.94`: identity verified; strong result with meaningful sample, calibration, or inference boundaries.
- `0.70-0.84`: identity verified; useful model interpretation, small/selected sample, or active-debate evidence.
- `<0.70`: not admitted as a usable finding; placed in `DO_NOT_USE_UNVERIFIED` or an open-debate entry.

Hard distinction: gas-phase metallicity, stellar metallicity, global/fiber measurements, and spatially resolved measurements are not interchangeable.

## 1. Established findings

### MZR-E01 — The local gas-phase MZR is real, tight, and non-linear

- role: established
- trust: `0.98`
- finding: Local star-forming galaxies show a positive relation between stellar mass and gas-phase oxygen abundance. In the SDSS baseline it is steep below roughly `10^10.5 M_sun`, flattens above that scale, and has about `0.1 dex` scatter.
- scope: `z ~ 0.1`; approximately 53,000 SDSS star-forming galaxies; global fiber spectra; gas-phase oxygen abundance inferred with the paper's Bayesian strong-line/photoionization framework.
- boundary: The relation's existence and broad shape are robust. Its absolute normalization and fitted turnover depend on metallicity calibration, aperture, stellar-mass scale, and sample selection.

Tremonti et al. (2004, ApJ) | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=established | Primary local MZR shape, turnover, mass range, and approximately 0.1 dex scatter.
Curti et al. (2020, MNRAS) | DOI:10.1093/mnras/stz2910; arXiv:1910.00597; ADS:2020MNRAS.491..944C | role=caveat | Confirms the local MZR on a fully Te-anchored abundance scale while showing normalization differences from photoionization-model scales.

### MZR-E02 — Metallicity calibration is part of the measurement, not a cosmetic choice

- role: established caveat
- trust: `0.99`
- finding: Different strong-line and direct-electron-temperature calibration families can shift inferred `12+log(O/H)` by as much as about `0.7 dex`. Cross-study MZR normalizations are unsafe unless the abundance scales are matched or explicitly converted.
- scope: local star-forming-galaxy calibrations; gas-phase metallicity only.
- boundary: This does not erase the MZR. It limits absolute abundance and normalization comparisons.

Kewley & Ellison (2008, ApJ) | DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K | role=caveat | Quantifies systematic offsets among commonly used metallicity calibrations and provides conversion guidance.
Curti et al. (2020, MNRAS) | DOI:10.1093/mnras/stz2910; arXiv:1910.00597; ADS:2020MNRAS.491..944C | role=caveat | Provides a Te-anchored local MZR/FMR benchmark with a lower normalization than photoionization-model scales.

### MZR-E03 — SFR is a measurable secondary correlate of local gas-phase metallicity

- role: established within local/calibration bounds
- trust: `0.91`
- finding: In local star-forming samples, gas-phase metallicity depends on SFR at fixed stellar mass, most clearly at lower mass and for strongly star-forming systems. A mass-SFR-metallicity surface can reduce residual scatter relative to a two-variable MZR.
- scope: local SDSS star-forming galaxies; the quoted FMR parameters are calibration- and selection-specific.
- boundary: The local secondary correlation is established; a universal, redshift-invariant “fundamental” surface is not.

Mannucci et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1005.0006; ADS:2010MNRAS.408.2115M | role=established | Defines a local FMR with about 0.05 dex residual dispersion in its adopted calibration and sample.
Curti et al. (2020, MNRAS) | DOI:10.1093/mnras/stz2910; arXiv:1910.00597; ADS:2020MNRAS.491..944C | role=established | Finds the SFR dependence especially evident for highly star-forming galaxies and reports 0.054 dex scatter around its Te-based FMR.

### MZR-E04 — The stellar MZR is a distinct integrated-history relation

- role: established
- trust: `0.94`
- finding: Mean stellar metallicity increases with stellar mass in the local Universe. Unlike gas-phase abundance, it records the metallicity of stars formed over a galaxy's history and depends on spectral-population modeling and weighting.
- scope: local SDSS optical spectra; stellar metallicity, not nebular oxygen abundance.
- boundary: Gas-phase and stellar MZRs must remain separate in the wiki. Absolute stellar metallicities retain age-metallicity, abundance-pattern, aperture, and model-systematic uncertainties.

Gallazzi et al. (2005, MNRAS) | DOI:10.1111/j.1365-2966.2005.09321.x; arXiv:astro-ph/0506539; ADS:2005MNRAS.362...41G | role=established | Foundational local stellar age/metallicity distributions and stellar mass-metallicity trend.

### MZR-E05 — Gas-phase MZR normalization declines with redshift through at least z ~ 3.3

- role: established over the measured range
- trust: `0.93`
- finding: Consistently treated samples show lower gas-phase oxygen abundance at fixed stellar mass toward higher redshift. Sanders et al. measure `dlog(O/H)/dz = -0.11 +/- 0.02` over `z=0-3.3` and a low-mass slope near `0.30` in their matched framework.
- scope: MOSDEF samples of about 300 galaxies at `z ~ 2.3` and about 150 at `z ~ 3.3`, combined with consistently calibrated lower-redshift comparisons.
- boundary: The exact rate and zero point depend on diagnostic matching and sample selection; it is not a calibration-free universal number.

Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=established | Primary measurement of MZR evolution from z=0 to z~3.3 with redshift-dependent calibration treatment.

### MZR-E06 — JWST establishes a lower-enrichment high-redshift extension, but not yet a single precision MZR

- role: established trend with high-redshift caveat
- trust: `0.86`
- finding: JWST/NIRSpec samples at `z ~ 4-10` extend the observed MZR into low-mass, early galaxies and show lower metallicity at fixed mass than local samples.
- scope: selected and often lensed high-redshift samples; a minority have direct auroral-line temperatures while many rely on strong-line calibrations.
- boundary: The direction of evolution is supported. Slope, normalization, intrinsic scatter, and FMR offsets at `z > 6` remain selection- and calibration-sensitive.

Langeroodi et al. (2023, ApJ) | DOI:10.3847/1538-4357/acdbc1; arXiv:2212.02491; ADS:2023ApJ...957...39L | role=established | Small lensed z~8 sample measuring about 0.9 dex lower normalization than locally.
Nakajima et al. (2023, ApJS) | DOI:10.3847/1538-4365/acd556; arXiv:2301.12825; ADS:2023ApJS..269...33N | role=established | 135-galaxy public JWST/NIRSpec census at z=4-10, with direct-method metallicities for 10 objects and calibrated strong-line values for the rest.
Curti et al. (2024, A&A) | DOI:10.1051/0004-6361/202346698; arXiv:2304.08516; ADS:2024A&A...684A..75C | role=established | JADES low-mass sample at 3<z<10; reports a shallow fitted slope and high-z offsets from the local FMR.

### MZR-E07 — Local resolved metallicity correlates with local stellar surface density

- role: established observational relation
- trust: `0.90`
- finding: In local disc galaxies, star-forming spaxels follow a positive relation between local stellar surface mass density and local gas-phase metallicity. This relation can reproduce important aspects of global MZR and radial-gradient behavior.
- scope: 653 MaNGA disc galaxies and more than 500,000 star-forming spaxels.
- boundary: “Local correlation” does not by itself prove that local physics exclusively causes the global MZR. Exceptions appear at low total mass and high specific SFR.

Barrera-Ballesteros et al. (2016, MNRAS) | DOI:10.1093/mnras/stw1984; arXiv:1609.01740; ADS:2016MNRAS.463.2513B | role=established | Primary resolved surface-density-metallicity measurement and stated limits.

### MZR-E08 — Environment contributes a small secondary local effect

- role: established small effect; mechanism debated
- trust: `0.87`
- finding: After mass and other controls, local overdense and cluster-associated samples show small gas-phase metallicity enhancements, typically no more than about `0.04-0.05 dex` in the cited analyses.
- scope: local SDSS star-forming samples; environment estimators and control matching differ.
- boundary: Stellar mass dominates. The observations do not uniquely establish whether reduced inflow, stripping, enrichment history, or residual selection causes the offset.

Cooper et al. (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.13714.x; arXiv:0805.0308; ADS:2008MNRAS.390..245C | role=established | Weak but significant residual metallicity-environment relation after controls.
Ellison et al. (2009, MNRAS) | DOI:10.1111/j.1365-2966.2009.14817.x; arXiv:0903.4684; ADS:2009MNRAS.396.1257E | role=established | Cluster/control comparison; enhancement is associated mainly with local overdensity rather than cluster membership alone.

## 2. Open debates and tensions

### MZR-D01 — Is the FMR strongly redshift-invariant?

- role: debate
- trust: `0.95`
- position A: In matched analyses through `z ~ 2.5-3.3`, high-redshift systems can be consistent with a local mass-SFR-metallicity relation.
- position B: JADES data at `z > 6` show substantial offsets from the local FMR, while simulations favor a “weak FMR” whose secondary SFR dependence evolves.
- why unresolved: redshift-dependent line diagnostics, changing ISM conditions, sample selection, burstiness, mass/SFR inference, and the definition of the fitted FMR all matter.

Mannucci et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1005.0006; ADS:2010MNRAS.408.2115M | role=debate | Supports invariance to z~2.5 in its framework while reporting an offset beyond that regime.
Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=debate | Finds no FMR evolution to z~3.3 under matched diagnostic treatment.
Curti et al. (2024, A&A) | DOI:10.1051/0004-6361/202346698; arXiv:2304.08516; ADS:2024A&A...684A..75C | role=debate | Finds a median high-z FMR offset of about 0.5 dex, especially above z~6.
Garcia et al. (2024, MNRAS) | DOI:10.1093/mnras/stae1252; arXiv:2403.08856; ADS:2024MNRAS.531.1398G | role=debate | Simulations predict an evolving “weak FMR” rather than a strictly invariant strong FMR.

### MZR-D02 — Does the high-redshift low-mass slope evolve?

- role: debate
- trust: `0.90`
- position A: Sanders et al. find a low-mass power-law slope near `0.30` invariant over `z=0-3.3` in their framework.
- position B: Curti et al. fit a shallower slope, `0.17 +/- 0.03`, for a low-mass JADES-centered sample spanning `3<z<10`; Langeroodi et al. describe their z~8 slope as similar to or slightly shallower than model/lower-redshift comparisons.
- why unresolved: small dynamic ranges, spectroscopic detectability, lensing, burst-selected samples, stellar-mass uncertainties, and metallicity calibration can all alter the inferred slope.

Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=debate | Invariant approximately 0.30 slope through z~3.3 in one matched framework.
Curti et al. (2024, A&A) | DOI:10.1051/0004-6361/202346698; arXiv:2304.08516; ADS:2024A&A...684A..75C | role=debate | Shallower low-mass slope in a selected JADES-centered 3<z<10 sample.
Langeroodi et al. (2023, ApJ) | DOI:10.3847/1538-4357/acdbc1; arXiv:2212.02491; ADS:2023ApJ...957...39L | role=debate | Small z~8 sample with a similar or slightly shallower inferred slope.

### MZR-D03 — Which abundance scale best transfers to high redshift?

- role: debate
- trust: `0.98`
- tension: Local Te-anchored and photoionization-model scales disagree in absolute normalization, while high-redshift ionization parameters and radiation fields can shift line ratios at fixed abundance.
- why unresolved: direct auroral lines remain difficult for representative samples; simulations and local analogs imperfectly reproduce early-galaxy ISM conditions; N/O, depletion, geometry, density, and ionizing spectrum are coupled.

Kewley & Ellison (2008, ApJ) | DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K | role=debate | Local abundance-scale discrepancy baseline.
Curti et al. (2020, MNRAS) | DOI:10.1093/mnras/stz2910; arXiv:1910.00597; ADS:2020MNRAS.491..944C | role=debate | Fully Te-anchored local benchmark.
Hirschmann et al. (2023, MNRAS) | DOI:10.1093/mnras/stad2745; arXiv:2305.03753; ADS:2023MNRAS.526.3504H | role=debate | Simulated high-z line calibrations show that applying some z=0 calibrations can bias O/H downward by up to about 1 dex.
Nakajima et al. (2023, ApJS) | DOI:10.3847/1538-4365/acd556; arXiv:2301.12825; ADS:2023ApJS..269...33N | role=debate | Empirical JWST census anchored by direct-method measurements for a subset.

### MZR-D04 — What physically sets the MZR: outflow, inflow, gas fraction, efficiency, or retention?

- role: debate over causal decomposition
- trust: `0.88`
- common framework: enrichment, dilution, gas consumption, and metal-loaded outflow jointly affect metallicity.
- unresolved point: the relative contribution and mass/redshift scaling of each process are model-dependent; an observed MZR does not uniquely identify a wind law.

Finlator & Davé (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.12991.x; arXiv:0704.3100; ADS:2008MNRAS.385.2181F | role=debate | Equilibrium/outflow model reproducing key MZR features; useful interpretation, not unique proof.
Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=debate | Observational constraints interpreted with analytic chemical-evolution models involving gas fraction and metal removal.

### MZR-D05 — How strongly do stellar metallicities identify quenching mechanisms?

- role: debate
- trust: `0.86`
- supported inference: Passive/star-forming stellar-metallicity offsets favor a prolonged reduced-inflow phase rather than purely instantaneous gas removal in the cited local analyses.
- unresolved point: starvation duration, outflow contribution, progenitor matching, stellar-population modeling, and whether one mechanism dominates all masses and epochs.

Peng, Maiolino & Cochrane (2015, Nature) | DOI:10.1038/nature14439; arXiv:1505.03143; ADS:2015Natur.521..192P | role=debate | Stellar-metallicity offset interpreted with simplified chemical-evolution models as evidence for strangulation.
Trussler et al. (2020, MNRAS) | DOI:10.1093/mnras/stz3286; arXiv:1811.09283; ADS:2020MNRAS.491.5406T | role=debate | Local data favor starvation plus an ejective/heating contribution; timescales depend on closed- versus leaky-box assumptions.
Looser et al. (2024, MNRAS) | DOI:10.1093/mnras/stae1581; arXiv:2401.08769; ADS:2024MNRAS.532.2832L | role=debate | MaNGA stellar FMR and reconstructed histories support reduced metal-poor accretion, with model and weighting boundaries.

### MZR-D06 — Are resolved relations causal building blocks or projections of global regulation?

- role: debate
- trust: `0.84`
- tension: Local surface density predicts local metallicity well, yet total mass, radius, SFR, gas flows, and radial position covary. Current correlations do not uniquely determine causal direction.

Barrera-Ballesteros et al. (2016, MNRAS) | DOI:10.1093/mnras/stw1984; arXiv:1609.01740; ADS:2016MNRAS.463.2513B | role=debate | Strong local surface-density-metallicity relation that can reproduce global trends, with explicit exceptions.

### MZR-D07 — What causes the small environment residual?

- role: debate
- trust: `0.87`
- tension: Local overdensity correlates with modest enrichment, but the causal path may involve restricted inflow, stripping, recycling, interaction history, or residual matching biases.

Cooper et al. (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.13714.x; arXiv:0805.0308; ADS:2008MNRAS.390..245C | role=debate | Environment accounts for a non-negligible but secondary part of local MZR scatter.
Ellison et al. (2009, MNRAS) | DOI:10.1111/j.1365-2966.2009.14817.x; arXiv:0903.4684; ADS:2009MNRAS.396.1257E | role=debate | Local overdensity, not cluster membership alone, tracks the observed enhancement.

## 3. Key measurements and numbers

### MZR-N01

- number: local gas-phase MZR scatter about `0.1 dex`.
- scope: Tremonti SDSS sample and adopted abundance framework.
- trust: `0.98` within that sample/calibration.

Tremonti et al. (2004, ApJ) | DOI:10.1086/423264; arXiv:astro-ph/0405537; ADS:2004ApJ...613..898T | role=established | Approximately 0.1 dex local scatter.

### MZR-N02

- number: absolute gas-phase metallicity offsets among calibration families can reach about `0.7 dex`.
- warning: never compare MZR zero points across unmatched calibrations as though they were on one scale.
- trust: `0.99`.

Kewley & Ellison (2008, ApJ) | DOI:10.1086/587500; arXiv:0801.1849; ADS:2008ApJ...681.1183K | role=caveat | Calibration offset envelope.

### MZR-N03

- number: local FMR residual scatter reported as about `0.05 dex` by Mannucci et al. and `0.054 dex` in the Te-based Curti et al. formulation.
- warning: these are fitted, sample- and calibration-specific residuals, not universal intrinsic scatter.
- trust: `0.92` within stated frameworks.

Mannucci et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.17291.x; arXiv:1005.0006; ADS:2010MNRAS.408.2115M | role=established | Approximately 0.05 dex residual dispersion.
Curti et al. (2020, MNRAS) | DOI:10.1093/mnras/stz2910; arXiv:1910.00597; ADS:2020MNRAS.491..944C | role=established | 0.054 dex residual scatter around its Te-based FMR.

### MZR-N04

- number: `dlog(O/H)/dz = -0.11 +/- 0.02` at fixed mass over `z=0-3.3`; low-mass scaling near `O/H proportional to M_*^0.30` in the same matched analysis.
- trust: `0.93` within the Sanders calibration framework.

Sanders et al. (2021, ApJ) | DOI:10.3847/1538-4357/abf4c1; arXiv:2009.07292; ADS:2021ApJ...914...19S | role=established | Matched z=0-3.3 evolution and slope measurement.

### MZR-N05

- number: about `0.9 dex` lower MZR normalization at `z ~ 8` than locally, corresponding to roughly eight times lower enrichment at fixed stellar mass.
- sample: 11 lensed galaxies at `7.2 < z < 9.5`.
- warning: early small-sample constraint, not yet a universal z~8 zero point.
- trust: `0.78`.

Langeroodi et al. (2023, ApJ) | DOI:10.3847/1538-4357/acdbc1; arXiv:2212.02491; ADS:2023ApJ...957...39L | role=caveat | First quantitative z~8 MZR inference from a small lensed sample.

### MZR-N06

- number: Curti et al. fit `12+log(O/H) = (7.72 +/- 0.02) + (0.17 +/- 0.03) log(M_*/10^8 M_sun)` for their low-mass JADES-centered `3<z<10` sample.
- warning: do not generalize this slope beyond the sample and calibration.
- trust: `0.82`.

Curti et al. (2024, A&A) | DOI:10.1051/0004-6361/202346698; arXiv:2304.08516; ADS:2024A&A...684A..75C | role=caveat | Selected high-redshift low-mass slope.

### MZR-N07

- number: local environmental enhancements reach up to about `0.04-0.05 dex` in the cited matched analyses.
- warning: this is much smaller than the primary mass trend and is not a universal cluster offset.
- trust: `0.87`.

Cooper et al. (2008, MNRAS) | DOI:10.1111/j.1365-2966.2008.13714.x; arXiv:0805.0308; ADS:2008MNRAS.390..245C | role=caveat | Weak residual environment relation.
Ellison et al. (2009, MNRAS) | DOI:10.1111/j.1365-2966.2009.14817.x; arXiv:0903.4684; ADS:2009MNRAS.396.1257E | role=caveat | Up to approximately 0.04-0.05 dex enhancement in local cluster/overdensity comparisons.

## 4. What remains unknown

### MZR-U01 — Precision MZR at z > 6

- role: future
- unknown: unbiased slope, zero point, intrinsic scatter, and mass/SFR covariance across representative high-redshift populations.
- needed: larger spectroscopically complete samples, more direct auroral-line detections, explicit selection functions, and cross-calibration on the same abundance scale.

### MZR-U02 — FMR universality versus evolving secondary dependence

- role: future
- unknown: whether a common physical surface survives with evolving coefficients or whether bursty early galaxies require a qualitatively different description.
- needed: consistent definitions, fine redshift bins, matched mass/SFR ranges, and calibration-robust residual tests.

### MZR-U03 — Gas-to-stellar metallicity mapping

- role: future
- unknown: how instantaneous nebular abundance, mass-weighted stellar metallicity, light-weighted stellar metallicity, and element-specific abundance ratios map onto one another over time.
- needed: joint gas-plus-stellar spectroscopy with consistent apertures, abundance patterns, and population models.

### MZR-U04 — Causal decomposition of the baryon cycle

- role: future
- unknown: separate mass/redshift scaling of inflow metallicity, gas fraction, star-formation efficiency, metal-loaded outflow, recycling, mixing, and retention.
- needed: combined ISM/CGM metal budgets, gas masses, resolved kinematics, and forward-modeled selection.

### MZR-U05 — Environment and local/global causality

- role: future
- unknown: whether small environment residuals and resolved relations are causal drivers or projections of correlated assembly and structural histories.
- needed: matched central/satellite samples, group histories, gas reservoirs, radial coverage, and causal model comparison.

## 5. DO_NOT_USE_UNVERIFIED

The following raw-report items failed identity or claim-boundary reconciliation. They must not enter the live wiki in their raw form.

- `UNCITED_NOT_USABLE | Trussler et al. 2020 raw tuple | DOI 10.1093/mnras/stz3287; arXiv 1910.00597 | DOI resolves to an unrelated black-hole-accretion paper and arXiv resolves to Curti et al.; corrected tuple is DOI 10.1093/mnras/stz3286, arXiv 1811.09283, ADS 2020MNRAS.491.5406T.`
- `UNCITED_NOT_USABLE | Lara-Lopez et al. raw tuple | DOI 10.1093/mnras/stt817; arXiv 1305.1952; ADS 2013MNRAS.433.1425L | DOI resolves to Bothwell et al., arXiv resolves to an unrelated dynamo paper, and the claimed ADS record does not resolve. Source dropped.`
- `UNCITED_NOT_USABLE | Looser et al. 2024 raw DOI | 10.1093/mnras/stae1364 | Resolves to an unrelated star-formation paper; corrected DOI is 10.1093/mnras/stae1581.`
- `UNCITED_NOT_USABLE | Barrera-Ballesteros et al. 2016 raw arXiv | 1606.07436 | Resolves to an unrelated equilibrium-model paper; corrected arXiv is 1609.01740.`
- `UNCITED_NOT_USABLE | Cooper et al. 2008 raw arXiv | 0807.2573 | Resolves to an unrelated Coma-cluster fireballs paper; corrected arXiv is 0805.0308.`
- `UNCITED_NOT_USABLE | Ellison et al. 2009 raw DOI/arXiv | DOI 10.1111/j.1365-2966.2009.14847.x; arXiv 0904.3016 | Both resolve to unrelated papers; corrected DOI is 10.1111/j.1365-2966.2009.14817.x and corrected arXiv is 0903.4684.`
- `UNCITED_NOT_USABLE | Baker et al. raw JADES attribution | arXiv 2304.08516; ADS 2023arXiv230408516B | The paper is first-authored by Curti and published as 2024A&A...684A..75C. Raw author/bibcode attribution dropped.`
- `UNCITED_NOT_USABLE | Curti et al. JADES raw MNRAS tuple | DOI 10.1093/mnras/stae1526; ADS 2024MNRAS.tmp.1526C | DOI resolves to an unrelated asteroseismology paper and ADS does not identify the JADES article. Correct publication is A&A 684 A75, DOI 10.1051/0004-6361/202346698.`
- `UNCITED_NOT_USABLE | Garcia et al. 2024 raw DOI | 10.1093/mnras/stae1364 | Resolves to an unrelated paper; corrected DOI is 10.1093/mnras/stae1252.`
- `UNCITED_NOT_USABLE | Hirschmann et al. 2023 raw DOI/arXiv | DOI 10.1093/mnras/stad2719; arXiv 2308.11703 | Both resolve to unrelated papers; corrected DOI is 10.1093/mnras/stad2745 and corrected arXiv is 2305.03753.`
- `UNCITED_NOT_USABLE | Finlator & Dave 2008 raw DOI | 10.1111/j.1365-2966.2008.12895.x | Resolves to an unrelated HII-region paper; corrected DOI is 10.1111/j.1365-2966.2008.12991.x.`
- `UNCITED_NOT_USABLE | Nakajima et al. 2023 raw DOI | 10.3847/1538-4365/acfc47 | Not the cited paper; corrected DOI is 10.3847/1538-4365/acd556.`
- `UNCITED_NOT_USABLE | Yates et al. 2012 raw arXiv | 1110.4408 | Resolves to a different zCOSMOS metallicity paper; corrected arXiv is 1107.3145.`
- `UNCITED_NOT_USABLE | Stanton et al. 2026 top-heavy-IMF claim | DOI/arXiv identity can resolve, but the raw packet's top-heavy-IMF claim is not supported by the cited paper boundary. Claim dropped.`
- `UNCITED_NOT_USABLE | MZR-N07 raw post-merger dilution number | Barrera-Ballesteros et al. 2016 | The cited surface-density-metallicity paper does not support the stated 36-post-merger, -0.04 dex measurement. Claim dropped.`
- `UNCITED_NOT_USABLE | Isobe 2026 and Lam 2026 preprints | identity may resolve, but they were not needed for this packet and sit outside the preferred 2020-2025 recent-literature window. No claim in this verified map depends on them.`
- `UNCITED_NOT_USABLE | Captured external source anchors in the raw packet | mixed search-trace links | They include unrelated cosmic-ray, black-hole, manga, football, cluster, and other contaminated results. They are provenance only, never a citation ledger.`

## 6. Verified source identity ledger

All 19 entries below passed exact NASA ADS bibcode lookup plus DOI and arXiv reconciliation. “Type” describes evidentiary role, not paper quality.

1. Tremonti et al. (2004), “The Origin of the Mass-Metallicity Relation: Insights from 53,000 Star-forming Galaxies in the Sloan Digital Sky Survey.” DOI `10.1086/423264`; arXiv `astro-ph/0405537`; ADS `2004ApJ...613..898T`. Type: primary observation.
2. Gallazzi et al. (2005), “The ages and metallicities of galaxies in the local universe.” DOI `10.1111/j.1365-2966.2005.09321.x`; arXiv `astro-ph/0506539`; ADS `2005MNRAS.362...41G`. Type: stellar-population inference.
3. Finlator & Davé (2008), “The origin of the galaxy mass-metallicity relation and implications for galactic outflows.” DOI `10.1111/j.1365-2966.2008.12991.x`; arXiv `0704.3100`; ADS `2008MNRAS.385.2181F`. Type: simulation/model.
4. Cooper et al. (2008), “The role of environment in the mass-metallicity relation.” DOI `10.1111/j.1365-2966.2008.13714.x`; arXiv `0805.0308`; ADS `2008MNRAS.390..245C`. Type: primary observation.
5. Kewley & Ellison (2008), “Metallicity Calibrations and the Mass-Metallicity Relation for Star-forming Galaxies.” DOI `10.1086/587500`; arXiv `0801.1849`; ADS `2008ApJ...681.1183K`. Type: calibration/method.
6. Ellison et al. (2009), “The mass-metallicity relation in galaxy clusters: the relative importance of cluster membership versus local environment.” DOI `10.1111/j.1365-2966.2009.14817.x`; arXiv `0903.4684`; ADS `2009MNRAS.396.1257E`. Type: primary observation.
7. Mannucci et al. (2010), “A fundamental relation between mass, star formation rate and metallicity in local and high-redshift galaxies.” DOI `10.1111/j.1365-2966.2010.17291.x`; arXiv `1005.0006`; ADS `2010MNRAS.408.2115M`. Type: primary observation/empirical relation.
8. Yates, Kauffmann & Guo (2012), “The relation between metallicity, stellar mass and star formation in galaxies: an analysis of observational and model data.” DOI `10.1111/j.1365-2966.2012.20595.x`; arXiv `1107.3145`; ADS `2012MNRAS.422..215Y`. Type: observation plus semi-analytic model.
9. Peng, Maiolino & Cochrane (2015), “Strangulation as the primary mechanism for shutting down star formation in galaxies.” DOI `10.1038/nature14439`; arXiv `1505.03143`; ADS `2015Natur.521..192P`. Type: stellar-population inference/chemical-evolution model.
10. Barrera-Ballesteros et al. (2016), “Do galaxy global relationships emerge from local ones? The SDSS IV MaNGA surface mass density-metallicity relation.” DOI `10.1093/mnras/stw1984`; arXiv `1609.01740`; ADS `2016MNRAS.463.2513B`. Type: primary resolved observation.
11. Trussler et al. (2020), “Both starvation and outflows drive galaxy quenching.” DOI `10.1093/mnras/stz3286`; arXiv `1811.09283`; ADS `2020MNRAS.491.5406T`. Type: stellar-population inference/chemical-evolution model.
12. Curti et al. (2020), “The mass-metallicity and the fundamental metallicity relation revisited on a fully Te-based abundance scale for galaxies.” DOI `10.1093/mnras/stz2910`; arXiv `1910.00597`; ADS `2020MNRAS.491..944C`. Type: calibration plus primary observation.
13. Sanders et al. (2021), “The MOSDEF Survey: The Evolution of the Mass-Metallicity Relation from z=0 to z~3.3.” DOI `10.3847/1538-4357/abf4c1`; arXiv `2009.07292`; ADS `2021ApJ...914...19S`. Type: primary observation.
14. Langeroodi et al. (2023), “Evolution of the Mass-Metallicity Relation from Redshift z≈8 to the Local Universe.” DOI `10.3847/1538-4357/acdbc1`; arXiv `2212.02491`; ADS `2023ApJ...957...39L`. Type: primary observation, small selected sample.
15. Nakajima et al. (2023), “JWST Census for the Mass-Metallicity Star Formation Relations at z=4-10 with Self-consistent Flux Calibration and Proper Metallicity Calibrators.” DOI `10.3847/1538-4365/acd556`; arXiv `2301.12825`; ADS `2023ApJS..269...33N`. Type: primary observation/calibration.
16. Hirschmann, Charlot & Somerville (2023), “High-redshift metallicity calibrations for JWST spectra: insights from line emission in cosmological simulations.” DOI `10.1093/mnras/stad2745`; arXiv `2305.03753`; ADS `2023MNRAS.526.3504H`. Type: simulation/model/calibration.
17. Curti et al. (2024), “JADES: Insights into the low-mass end of the mass-metallicity-SFR relation at 3<z<10 from deep JWST/NIRSpec spectroscopy.” DOI `10.1051/0004-6361/202346698`; arXiv `2304.08516`; ADS `2024A&A...684A..75C`. Type: primary observation.
18. Garcia et al. (2024), “Does the fundamental metallicity relation evolve with redshift? I: the correlation between offsets from the mass-metallicity relation and star formation rate.” DOI `10.1093/mnras/stae1252`; arXiv `2403.08856`; ADS `2024MNRAS.531.1398G`. Type: simulation/model.
19. Looser et al. (2024), “The stellar fundamental metallicity relation: the correlation between stellar mass, star formation rate, and stellar metallicity.” DOI `10.1093/mnras/stae1581`; arXiv `2401.08769`; ADS `2024MNRAS.532.2832L`. Type: stellar-population inference.

MZR_DR_PACKET_COMPLETE_REFERENCE_ONLY

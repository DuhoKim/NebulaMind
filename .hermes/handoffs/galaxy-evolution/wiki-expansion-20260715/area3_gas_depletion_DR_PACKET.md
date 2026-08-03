# Area 3 verified evidence packet — gas depletion and star-formation efficiency

status: READY_FOR_HWAO_REVIEW
advisory_only: true
broad_non_agn: true
distinct_from_areas1_2: true
wiki_write_performed_by_tori: false
conversation_deleted: false

Raw Deep Research custody: `area3_gas_depletion_DR_RAW_PACKET.md`
Raw packet SHA-256: `17addc6dd3d13850ceef6b844d1264f5cc3167bbccc86ffd11fae963a5501fed`
Curated source registry: `area3_gas_depletion_CURATED_SOURCE_REGISTRY.json`
Composite identity status: PASS, 25/25 sources
Verification method: exact public ADS abstract route/title + Crossref DOI metadata + arXiv export metadata. Eleven cross-wired DOI/arXiv values in the raw report were corrected before promotion. No ADS API verification is claimed locally; Hwao's working ADS API verifier and jury remain the final live-wiki gate.

Interpretive rules:
- `t_dep,mol = M_H2 / SFR` and `SFE_mol = 1 / t_dep,mol` are instantaneous ratios, not guaranteed exhaustion clocks.
- HI, H2, total cold gas, and dense gas are separate reservoirs/tracers.
- Global and spatially resolved star-formation laws are separate measurements.
- Low gas content does not identify the mechanism that produced quiescence.
- CO- and dust-derived gas masses retain conversion, excitation, metallicity, and selection boundaries.

## 1. Established findings

[GAS-E01]
role: established
finding: In nearby, molecule-dominated star-forming disks averaged on roughly kiloparsec scales, molecular-gas surface density and SFR surface density are close to linear, corresponding to a comparatively narrow molecular depletion-time distribution.
scope/boundary: Local normal disks; CO-traced H2; approximately kiloparsec averaging; adopted CO-to-H2 conversion factor. This is not a universal law for HI, total gas, starbursts, metal-poor dwarfs, or cloud-scale apertures.
evidence: HERACLES/BIMA SONG/THINGS-style resolved analyses find molecular-law slopes near unity and characteristic depletion times around 2 Gyr under standard calibrations.
trust_score: 0.94
sources: [Bigiel2008, Leroy2008, Bigiel2011]

[GAS-E02]
role: established
finding: In the nearby galaxies studied by THINGS-related analyses, azimuthally averaged HI surface densities commonly approach a saturation scale near 9 solar masses per square parsec, while star formation per unit HI declines in HI-dominated outer disks and dwarfs.
scope/boundary: Local resolved 21-cm samples. The quoted scale is empirical and sample-dependent, not a hard universal ceiling; shielding, metallicity, pressure, inclination, opacity, and resolution matter.
evidence: Resolved HI, CO, UV, and IR maps separate molecule-dominated inner disks from inefficient HI-dominated regimes.
trust_score: 0.91
sources: [Bigiel2008, Leroy2008, Schruba2011]

[GAS-E03]
role: established
finding: At low redshift, integrated HI and H2 fractions vary systematically with stellar mass, color/specific SFR, and stellar surface density, but HI and H2 show different dependencies and scatter.
scope/boundary: Mass-selected GASS/xGASS and COLD GASS/xCOLD GASS samples; integrated measurements; survey limits and non-detections retained. This does not establish one universal gas-fraction-versus-mass curve for every environment.
evidence: Arecibo HI and IRAM CO surveys provide representative local scaling relations and show that main-sequence offset or sSFR can be a stronger predictor of molecular fraction than stellar mass alone.
trust_score: 0.95
sources: [Catinella2010, Catinella2018, Saintonge2011a, Saintonge2017]

[GAS-E04]
role: established
finding: Global molecular depletion time is not a single constant across all galaxies; it correlates with specific SFR and distance from the star-forming main sequence.
scope/boundary: Integrated CO measurements, with dependencies on SFR calibration, sample selection, and alpha_CO. The finding does not imply a unique physical cause for every offset.
evidence: COLD GASS/xCOLD GASS and PHIBSS compilations find shorter t_dep,mol above the main sequence and longer values toward lower-sSFR systems.
trust_score: 0.92
sources: [Saintonge2011b, Saintonge2017, Tacconi2018]

[GAS-E05]
role: established
finding: Molecular-gas fractions of massive star-forming galaxies increase strongly from the local universe toward cosmic noon, while molecular depletion time evolves more weakly and also depends on main-sequence offset.
scope/boundary: Mostly massive, star-forming, CO- or dust-detected systems through z about 3-4. Definitions of the main sequence, excitation corrections, alpha_CO, dust calibration, and targeted selection affect fitted exponents.
evidence: PHIBSS and combined CO/dust compilations recover unified but calibration-dependent scaling relations in redshift, stellar mass, and main-sequence offset.
trust_score: 0.90
sources: [Tacconi2018, Genzel2015]

[GAS-E06]
role: established
finding: Across integrated galaxies and Galactic molecular clouds, SFR correlates approximately linearly with luminosity or mass assigned to dense molecular gas over a wide dynamic range.
scope/boundary: HCN-based galaxy measurements and extinction/dense-mass thresholds in Milky Way clouds are not identical tracers. HCN excitation, abundance, and optical depth prevent a universal one-to-one dense-mass conversion.
evidence: Gao and Solomon established the global IR-HCN relation; Lada and collaborators compared cloud SFRs with mass above a dense-gas threshold.
trust_score: 0.86
sources: [GaoSolomon2004, Lada2012]

[GAS-E07]
role: established
finding: Disk-averaged total-gas measurements of local spirals and starbursts yield a super-linear Kennicutt-Schmidt relation with a fitted slope near 1.4.
scope/boundary: Integrated HI+H2 surface density and integrated SFR indicators. The result must not be substituted for a resolved molecular-only law.
evidence: Kennicutt's global compilation fit normal disks and circumnuclear starbursts together using total gas and H-alpha/IR SFR measurements.
trust_score: 0.95
sources: [Kennicutt1998]

[GAS-E08]
role: established
epistemic_type: theory
finding: Numerical experiments demonstrate that a sufficiently stabilizing stellar potential can suppress fragmentation and star formation in a gas-bearing disk without first expelling all cold gas.
scope/boundary: This establishes a viable model mechanism called morphological quenching; it does not establish how often that mechanism dominates real quiescent galaxies.
evidence: Simulations by Martig and collaborators show reduced disk instability and SFR after spheroid growth while gas remains.
trust_score: 0.76
sources: [Martig2009]

[GAS-E09]
role: established
finding: Blind CO surveys indicate that the cosmic molecular-gas density rises from today toward z roughly 1-3 and then declines toward the present, broadly tracking the cosmic SFR-density history.
scope/boundary: Small survey volumes, CO-transition excitation ladders, completeness, faint-end extrapolation, alpha_CO, and cosmic variance broaden the peak and its normalization.
evidence: ASPECS and COLDz independently constrain CO luminosity functions and molecular-gas density in blind fields.
trust_score: 0.89
sources: [Decarli2020, Riechers2019]

[GAS-E10]
role: established
finding: Within cosmic baryon-accounting models, the observed growth of stellar mass cannot be supplied solely by the decline of the measured HI and H2 reservoirs; net accretion onto galaxies is required.
scope/boundary: This is an inference from volume-averaged inventories and continuity assumptions, not a direct measurement of each inflow stage or proof of a unique gas-regulator model.
evidence: Walter and collaborators combine cosmic stellar, SFR, HI, and H2 densities and infer declining but nonzero net gas supply.
trust_score: 0.85
sources: [Walter2020]

[GAS-E11]
role: established
finding: Long-wavelength Rayleigh-Jeans dust continuum can provide an efficient empirical proxy for cold-ISM mass in massive, relatively metal-rich galaxies when calibrated against gas tracers.
scope/boundary: Dust temperature, opacity, dust-to-gas ratio, metallicity, and CMB effects matter. The calibration is least secure in metal-poor, low-mass, or very high-redshift systems and does not directly distinguish HI from H2.
evidence: ALMA continuum studies calibrate rest-frame long-wavelength luminosity against local and high-redshift gas measurements.
trust_score: 0.84
sources: [Scoville2016, Scoville2017, Bolatto2013]

[GAS-E12]
role: established
finding: The tight kiloparsec-scale molecular star-formation relation develops much larger scatter when apertures approach individual cloud and star-forming-region scales.
scope/boundary: Nearby galaxies with high-resolution CO and SFR mapping; part of the scatter reflects temporal offsets between gas and young-star tracers as well as environment.
evidence: Scale-dependent analyses and PHANGS-ALMA cloud-scale maps show that coarse averaging suppresses evolutionary and spatial offsets.
trust_score: 0.87
sources: [Schruba2011, Leroy2021]

## 2. Open debates and tensions

[GAS-D01]
role: debate
debate_topic: Linear versus super-linear star-formation-law slopes.
competing_positions: Integrated total-gas measurements yield a slope near 1.4, whereas resolved molecular-only measurements in normal disks are closer to linear.
why_unresolved: Gas phase, spatial scale, dynamic range, regression method, alpha_CO, diffuse emission, and SFR tracers change the fitted slope; these measurements need not describe one invariant law.
boundary: Compare like-for-like total versus molecular gas and global versus resolved apertures.
trust_score: 0.93
sources: [Kennicutt1998, Bigiel2008, Leroy2008]

[GAS-D02]
role: debate
debate_topic: Two discrete disk/starburst sequences versus a continuous dependence on main-sequence offset.
competing_positions: Daddi et al. framed disks and starbursts as offset sequences; later larger compilations fit a more continuous change of t_dep,mol with distance above the main sequence.
why_unresolved: Sample selection and especially continuous versus step-function alpha_CO prescriptions can create or erase apparent bimodality.
boundary: Targeted high-redshift starbursts, local ULIRGs, and representative mass-selected samples are not interchangeable.
trust_score: 0.86
sources: [Daddi2010, Tacconi2018, Saintonge2017]

[GAS-D03]
role: debate
debate_topic: Magnitude and functional form of alpha_CO/X_CO variation.
competing_positions: Some analyses use a Galactic disk value plus a lower starburst value; dust-, dynamics-, and metallicity-based methods favor continuous environmental variation.
why_unresolved: H2 lacks a practical cold-gas emission tracer, so each calibration inherits assumptions about dust-to-gas ratio, cloud dynamics, metallicity, excitation, and unresolved structure.
boundary: Central kiloparsecs, metal-poor systems, normal disks, and mergers require separate treatment.
trust_score: 0.92
sources: [Bolatto2013, Sandstrom2013]

[GAS-D04]
role: debate
debate_topic: Quenching by reduced supply/exhaustion versus suppressed SFE versus rapid gas removal.
competing_positions: Low gas fractions are consistent with curtailed supply or removal; simulations and resolved measurements show that reduced SFE can also move regions or galaxies below star-forming relations while gas remains.
why_unresolved: Most observations are snapshots after quenching and do not reconstruct the causal order of supply shutoff, phase conversion, stabilization, stripping, and consumption.
boundary: Martig2009 is a model demonstration; Ellison2020 concerns resolved star-forming-main-sequence scatter, not direct proof of the dominant quenching channel.
trust_score: 0.77
sources: [Martig2009, Ellison2020, Saintonge2017]

[GAS-D05]
role: debate
debate_topic: Constant versus mildly evolving t_dep,mol after controlling for main-sequence offset.
competing_positions: Some compilations emphasize near-invariant star-formation physics after normalization; others retain mild redshift dependence in fitted depletion time.
why_unresolved: Main-sequence definitions, CO versus dust mass scales, SFR indicators, excitation, and heterogeneous selection covary with redshift.
boundary: Restricted mainly to massive star-forming systems through z about 3-4.
trust_score: 0.85
sources: [Tacconi2018, Genzel2015]

[GAS-D06]
role: debate
debate_topic: Whether main-sequence offsets are driven mainly by reservoir mass or by molecular SFE.
competing_positions: Global scaling relations assign roles to both gas fraction and t_dep,mol; resolved ALMaQUEST measurements find that local scatter around the resolved main sequence is more strongly associated with SFE variations than gas fraction.
why_unresolved: Global and resolved relations answer different questions, and neither alone establishes the temporal driver of a whole-galaxy transition.
boundary: Keep integrated galaxy offsets distinct from 1.5-kpc spaxel correlations.
trust_score: 0.86
sources: [Saintonge2017, Tacconi2018, Ellison2020]

[GAS-D07]
role: debate
debate_topic: Absolute normalization and peak redshift of cosmic H2 density.
competing_positions: Blind CO surveys agree on broad rise-and-fall evolution but differ in peak amplitude, width, and high-redshift behavior.
why_unresolved: Narrow fields, cosmic variance, line identification, CO excitation, completeness, and faint-end extrapolation dominate uncertainties.
boundary: ASPECS and COLDz sample different fields, volumes, transitions, and sensitivity functions.
trust_score: 0.84
sources: [Decarli2020, Riechers2019]

## 3. Key measurements and numbers

[GAS-N01]
role: measurement
metric: Local resolved molecular depletion time.
value: Approximately 2.0-2.3 Gyr, with substantial inter-region and inter-galaxy scatter, under a standard Galactic alpha_CO.
sample_method: Nearby normal disks; roughly kiloparsec CO and UV+IR maps from HERACLES/BIMA SONG/THINGS-related work.
boundary: Not HI or total-gas t_dep; not a literal future exhaustion time; centers, starbursts, low metallicity, and smaller apertures differ.
trust_score: 0.92
sources: [Bigiel2008, Bigiel2011]

[GAS-N02]
role: measurement
metric: Characteristic resolved HI saturation scale.
value: About 9 solar masses per square parsec in the studied nearby sample.
sample_method: THINGS 21-cm maps combined with CO and UV/IR SFR tracers.
boundary: An empirical azimuthally averaged scale, not a hard universal maximum; opacity, inclination, shielding, metallicity, and resolution affect it.
trust_score: 0.88
sources: [Bigiel2008]

[GAS-N03]
role: measurement
metric: PHIBSS unified dependence on main-sequence offset.
value: Tacconi et al. report fitted dependences near t_dep,mol proportional to delta_MS^-0.44 and molecular-to-stellar mass ratio proportional to delta_MS^+0.53.
sample_method: Compilation of approximately 1,400 star-forming galaxies over z about 0-4 using CO and dust estimates.
boundary: Coefficients depend on adopted main-sequence relation, IMF, SFR scale, alpha_CO, and dust calibration.
trust_score: 0.86
sources: [Tacconi2018]

[GAS-N04]
role: measurement
metric: Milky-Way disk CO-to-H2 conversion factor.
value: alpha_CO about 4.3 solar masses per (K km s^-1 pc^2), including helium; corresponding X_CO about 2e20 H2 molecules cm^-2 per (K km s^-1).
sample_method: Synthesis of virial, dust, gamma-ray, and related calibrations.
boundary: Not universal; metallicity, radiation field, surface density, dynamics, and starburst conditions alter the factor.
trust_score: 0.94
sources: [Bolatto2013]

[GAS-N05]
role: measurement
metric: Global total-gas Kennicutt-Schmidt exponent.
value: N about 1.4, with quoted fit uncertainty about 0.15 in the foundational compilation.
sample_method: Disk-averaged local spirals and starbursts; integrated HI+H2 and H-alpha/IR SFR indicators.
boundary: Must not be assigned to resolved molecular-only measurements.
trust_score: 0.95
sources: [Kennicutt1998]

[GAS-N06]
role: measurement
metric: Decline in cosmic molecular-gas density.
value: ASPECS reports an increase toward z about 1.5 followed by an approximately factor-six decline to z=0.
sample_method: Blind ALMA 3-mm and 1.2-mm line scans in the Hubble Ultra Deep Field.
boundary: Excitation ladders, alpha_CO, completeness, small volume, and cosmic variance broaden the estimate.
trust_score: 0.87
sources: [Decarli2020]

[GAS-N07]
role: measurement
metric: xCOLD GASS local survey scale and integrated CO excitation ratio.
value: 532 mass-selected galaxies at 0.01<z<0.05 and stellar mass above 1e9 solar masses; integrated r21 = L'_CO(2-1)/L'_CO(1-0) = 0.79 +/- 0.03.
sample_method: IRAM 30-m CO(1-0), IRAM/APEX CO(2-1), Arecibo HI, and SDSS/WISE/GALEX data.
boundary: Sample-average integrated ratio; not a resolved or universal excitation correction.
trust_score: 0.94
sources: [Saintonge2017]

## 4. What remains unknown

[GAS-U01]
role: future
gap: Which cloud lifecycle, feedback, dynamical, and tracer effects dominate the rapidly increasing scatter below kiloparsec scales.
why_it_matters: Subgrid star-formation prescriptions must connect cloud evolution to galaxy-averaged depletion times.
needed: Matched approximately 50-pc molecular, dense-gas, young-star, and feedback mapping across diverse environments.
trust_score: 0.86
sources: [Schruba2011, Leroy2021]

[GAS-U02]
role: future
gap: Robust dust-to-gas and dust-emissivity calibration at very low metallicity and high redshift.
why_it_matters: Dust-continuum gas masses can shift systematically if early dust production/destruction and metallicity scaling differ from local calibrations.
needed: CO, [CI], dust, metallicity, and dynamical cross-calibration across a broader mass-redshift range.
trust_score: 0.84
sources: [Scoville2016, Scoville2017, Bolatto2013]

[GAS-U03]
role: future
gap: The temporal order and relative contribution of supply shutoff, ordinary consumption, SFE suppression, and rapid removal in quenching.
why_it_matters: A low post-quenching gas fraction is compatible with multiple causal histories.
needed: Time-sensitive samples plus resolved HI/H2 kinematics, stellar ages, environmental diagnostics, and stability measurements.
trust_score: 0.76
sources: [Martig2009, Ellison2020, Saintonge2017]

[GAS-U04]
role: future
gap: Directly partitioning fresh accretion, recycled fountain gas, phase conversion, and outflow loading in gas-regulator accounting.
why_it_matters: Volume-averaged continuity requires net supply but does not uniquely identify its path.
needed: Joint disk-CGM kinematics and multi-phase mass-flow constraints tied to resolved galaxy gas inventories.
trust_score: 0.80
sources: [Walter2020]

[GAS-U05]
role: future
gap: Whether starbursts are driven primarily by a larger dense-gas fraction, altered dense-gas SFE, or tracer excitation/chemistry.
why_it_matters: HCN luminosity is not a direct, environment-invariant dense-gas mass measurement.
needed: Multi-transition HCN/HCO+/CO excitation and opacity modeling with resolved SFR measurements.
trust_score: 0.79
sources: [GaoSolomon2004, Lada2012, Leroy2021]

## 5. DO_NOT_USE_UNVERIFIED

1. UNCITED_NOT_USABLE — Raw Decarli2020 DOI `10.3847/1538-4357/abb82d`; it does not resolve to the claimed paper. Correct DOI: `10.3847/1538-4357/abaa3b`.
2. UNCITED_NOT_USABLE — Raw Walter2020 arXiv `2009.10748`; it resolves to an unrelated federated-learning paper. Correct arXiv: `2009.11126`.
3. UNCITED_NOT_USABLE — Raw Bolatto2013 arXiv `1301.7436`; it resolves to an unrelated lattice-QCD paper. Correct arXiv: `1301.3498`.
4. UNCITED_NOT_USABLE — Raw Ellison2020 DOI `10.1093/mnrasl/slz185` and arXiv `1912.01015`; both resolve to unrelated papers. Correct tuple uses DOI `10.1093/mnrasl/slz179` and arXiv `1911.11887`.
5. UNCITED_NOT_USABLE — Raw Saintonge2011b DOI `10.1111/j.1365-2966.2011.18678.x` and arXiv `1103.1644`; both resolve to unrelated papers. Correct tuple uses DOI `10.1111/j.1365-2966.2011.18823.x` and arXiv `1104.0019`.
6. UNCITED_NOT_USABLE — Raw Daddi2010 arXiv `1004.1673`; unrelated computer-science paper. Correct arXiv: `1003.3889`.
7. UNCITED_NOT_USABLE — Raw Lada2012 arXiv `1111.5173`; unrelated particle-physics paper. Correct arXiv: `1112.4466`.
8. UNCITED_NOT_USABLE — Raw Martig2009 arXiv `0909.1325`; unrelated red-sequence clustering paper. Correct arXiv: `0905.4669`.
9. UNCITED_NOT_USABLE — Raw Catinella2010 DOI `10.1111/j.1365-2966.2009.16175.x`; belongs to an unrelated high-redshift paper. Correct DOI: `10.1111/j.1365-2966.2009.16180.x`.
10. UNCITED_NOT_USABLE — Raw Scoville2016 arXiv `1511.02529`; unrelated proceedings paper. Correct arXiv: `1511.05149`.
11. UNCITED_NOT_USABLE — Raw Bigiel2011 arXiv `1101.4984`; unrelated paper. Correct arXiv: `1102.1720`.
12. UNCITED_NOT_USABLE — Any AGN-selected molecular-gas, AGN-feedback, radio-AGN, black-hole, or nuclear-host anchor from the raw external-links capture; Area 3 is explicitly non-AGN.
13. UNCITED_NOT_USABLE — Any 2026/future-dated result or conference/preprint anchor from the raw search capture.
14. UNCITED_NOT_USABLE — "Depletion time predicts guaranteed gas exhaustion after t_dep." Inflow, outflow, recycling, phase conversion, and variable SFR invalidate that interpretation.
15. UNCITED_NOT_USABLE — "Low gas content proves gas exhaustion caused quenching." It does not identify supply, removal, efficiency, or temporal order.
16. UNCITED_NOT_USABLE — "HI has a strict universal hard ceiling of 9 solar masses per square parsec." The empirical scale is sample-, method-, and environment-dependent.
17. UNCITED_NOT_USABLE — "Molecular depletion time is universally constant" or "universally non-constant." Both overstate scale- and sample-dependent findings.
18. UNCITED_NOT_USABLE — "Morphological quenching is observationally proven to dominate quiescent galaxies." Martig2009 establishes a simulation mechanism, not population prevalence.
19. UNCITED_NOT_USABLE — "The dense-gas SFE is universal" or "Leroy2021 directly measures dense-gas SFE." The available tracer set does not support either claim.
20. UNCITED_NOT_USABLE — Any cosmic H2 peak value without field, transition, excitation, completeness, alpha_CO, and cosmic-variance boundaries.
21. UNCITED_NOT_USABLE — Raw superlatives such as "hard saturation," "definitively," "mandatory for galaxy survival," "strictly linear," "fully validated," or "undisputed" when the cited study only establishes a bounded empirical or model result.

## 6. Source identity ledger

Saintonge et al. (2017, ApJS) | DOI:10.3847/1538-4365/aa97e0; arXiv:1710.02157; ADS:2017ApJS..233...22S | role=measurement | xCOLD GASS local mass-selected CO census and integrated molecular-gas scaling relations.
Catinella et al. (2018, MNRAS) | DOI:10.1093/mnras/sty089; arXiv:1802.02373; ADS:2018MNRAS.476..875C | role=measurement | xGASS integrated HI and total-cold-gas scaling relations; retain mass selection and non-detections.
Tacconi et al. (2018, ApJ) | DOI:10.3847/1538-4357/aaa4b4; arXiv:1702.01140; ADS:2018ApJ...853..179T | role=established | PHIBSS unified global t_dep,mol and molecular-fraction fits; calibration- and main-sequence-definition dependent.
Decarli et al. (2020, ApJ) | DOI:10.3847/1538-4357/abaa3b; arXiv:2009.10744; ADS:2020ApJ...902..110D | role=measurement | ASPECS blind CO luminosity functions and cosmic H2 density; small-field and excitation limits apply.
Walter et al. (2020, ApJ) | DOI:10.3847/1538-4357/abb82e; arXiv:2009.11126; ADS:2020ApJ...902..111W | role=theory | Volume-averaged baryon accounting and inferred net accretion; not direct mapping of each gas-flow stage.
Riechers et al. (2019, ApJ) | DOI:10.3847/1538-4357/aafc27; arXiv:1808.04371; ADS:2019ApJ...872....7R | role=measurement | COLDz blind CO luminosity functions and cold-gas history; survey-volume and conversion limits apply.
Leroy et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=established | Resolved local HI/H2 SFE regimes; not a universal all-scale law.
Bigiel et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2846; arXiv:0810.2541; ADS:2008AJ....136.2846B | role=established | Sub-kpc local star-formation law and HI saturation scale under stated tracers.
Schruba et al. (2011, AJ) | DOI:10.1088/0004-6256/142/2/37; arXiv:1105.4605; ADS:2011AJ....142...37S | role=caveat | Molecular law in atomic-dominated regimes and spatial-scale dependence.
Bolatto et al. (2013, ARA&A) | DOI:10.1146/annurev-astro-082812-140944; arXiv:1301.3498; ADS:2013ARA&A..51..207B | role=caveat | CO-to-H2 conversion-factor review; alpha_CO is environment dependent.
Kennicutt (1998, ApJ) | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=established | Global total-gas Schmidt law; do not apply its slope to resolved molecular-only data.
Ellison et al. (2020, MNRAS) | DOI:10.1093/mnrasl/slz179; arXiv:1911.11887; ADS:2020MNRAS.493L..39E | role=measurement | ALMaQUEST resolved-main-sequence scatter and SFE association; not direct proof of a quenching mechanism.
Leroy et al. (2021, ApJS) | DOI:10.3847/1538-4365/ac17f3; arXiv:2104.07739; ADS:2021ApJS..257...43L | role=measurement | PHANGS-ALMA CO(2-1) imaging census; bulk molecular gas, not a dense-gas-SFE measurement.
Saintonge et al. (2011, MNRAS) | DOI:10.1111/j.1365-2966.2011.18677.x; arXiv:1103.1642; ADS:2011MNRAS.415...32S | role=measurement | COLD GASS I integrated H2, HI, stellar, and structural relations in massive local galaxies.
Saintonge et al. (2011, MNRAS) | DOI:10.1111/j.1365-2966.2011.18823.x; arXiv:1104.0019; ADS:2011MNRAS.415...61S | role=established | COLD GASS II non-universality of global molecular depletion time; retain mass/sSFR/sample limits.
Daddi et al. (2010, ApJL) | DOI:10.1088/2041-8205/714/1/L118; arXiv:1003.3889; ADS:2010ApJ...714L.118D | role=debate | Disk-versus-starburst sequence framing; alpha_CO and selection affect apparent bimodality.
Gao & Solomon (2004, ApJ) | DOI:10.1086/382999; arXiv:astro-ph/0310339; ADS:2004ApJ...606..271G | role=established | Integrated IR-HCN relation; HCN luminosity is not an environment-invariant dense-mass scale.
Lada et al. (2012, ApJ) | DOI:10.1088/0004-637X/745/2/190; arXiv:1112.4466; ADS:2012ApJ...745..190L | role=established | Galactic-cloud SFR versus dense mass and comparison to extragalactic relations.
Martig et al. (2009, ApJ) | DOI:10.1088/0004-637X/707/1/250; arXiv:0905.4669; ADS:2009ApJ...707..250M | role=theory | Simulation demonstration of morphological stabilization; prevalence remains open.
Catinella et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2009.16180.x; arXiv:0912.1610; ADS:2010MNRAS.403..683C | role=measurement | First GASS HI fraction scaling relations for massive local galaxies.
Scoville et al. (2016, ApJ) | DOI:10.3847/0004-637X/820/2/83; arXiv:1511.05149; ADS:2016ApJ...820...83S | role=measurement | ALMA dust-continuum ISM-mass calibration/application at z=1-6; metallicity and dust assumptions apply.
Scoville et al. (2017, ApJ) | DOI:10.3847/1538-4357/aa61a0; arXiv:1702.04729; ADS:2017ApJ...837..150S | role=measurement | Dust-estimated gas scaling and inferred accretion at high redshift; calibration dependent.
Bigiel et al. (2011, ApJL) | DOI:10.1088/2041-8205/730/2/L13; arXiv:1102.1720; ADS:2011ApJ...730L..13B | role=measurement | Approximately 2.3-Gyr local-disk molecular depletion time under a standard alpha_CO.
Sandstrom et al. (2013, ApJ) | DOI:10.1088/0004-637X/777/1/5; arXiv:1212.1208; ADS:2013ApJ...777....5S | role=caveat | Resolved alpha_CO and dust-to-gas ratio in 26 nearby galaxies.
Genzel et al. (2015, ApJ) | DOI:10.1088/0004-637X/800/1/20; arXiv:1409.1171; ADS:2015ApJ...800...20G | role=measurement | Combined CO/dust gas-fraction and depletion-time scaling to z about 3.

GAS_DR_PACKET_VERIFIED_READY

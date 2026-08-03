# Area 3 raw Deep Research packet — gas depletion and star-formation efficiency

advisory_only: true
broad_non_agn: true
distinct_from_areas1_2: true
wiki_write_performed_by_tori: false
identifier_verification_required_before_live_wiki_use: true

Brief: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area3_gas_depletion_DR_BRIEF.md`
Brief SHA-256: `ae6715ab4dcb20bf92286a11f76591894f0df59f4beb622b16e3c46d9da39255`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area3_gas_depletion_DR_PROMPT.md`
Prompt file SHA-256: `6a67d946b187a8697117d97c4230802ab77654b78d89dae091cdaba1ba5486ee`
Submitted prompt text SHA-256: `32f52bfdc7a50b0f3d97616d0ba45f7d39c241129f31b77603218268bef6e662`
Conversation ID: `2c3158b4b3b80663`
Submit UTC: `2026-07-15T11:17:40.274280Z`
Research Start UTC: `2026-07-15T11:18:44.893674Z`
Result captured UTC: `2026-07-15T11:29:03.275745Z`
Raw result SHA-256: `f696b9d77178a3196640f1597d5804f39deb8339af8080a0cefec80b429ad7c6`

## Deep Research evidence map

NebulaMind Area 3: Non-AGN Gas Depletion and Star-Formation Efficiency
1. Established findings

[GAS-E01]

role: established

finding: A fundamentally linear scaling relationship governs the star formation rate (SFR) surface density and the molecular gas surface density at kiloparsec scales in the inner disks of star-forming galaxies, resulting in a roughly constant molecular gas depletion time.

scope/boundary: This finding is strictly constrained to spatially resolved measurements (approximately 1 kpc resolution) of the molecular gas phase (H2), typically traced by low-J CO emission lines. It applies to the central and inner optical disks of nearby, massive, main-sequence spiral galaxies. It explicitly does not apply to the atomic gas phase, total combined gas, highly sub-solar metallicity dwarf galaxies, or scales below the typical size of a giant molecular cloud (sub-kpc scales).

evidence: Extensive multi-wavelength mapping campaigns—such as the HERACLES survey utilizing the IRAM 30m telescope to map CO(2-1) and the BIMA SONG survey—have been cross-correlated with resolved SFR tracers derived from a combination of far-ultraviolet (GALEX) and 24-micron mid-infrared (Spitzer) emission. These spatially resolved analyses demonstrate that the star formation rate surface density scales almost linearly with the H2 surface density, yielding a power-law index of N=1.0±0.2. The physical interpretation of this linearity suggests that the molecular gas surface density on kiloparsec scales primarily measures the spatial filling factor of giant molecular clouds (GMCs) rather than fundamentally changing internal physical conditions within the clouds themselves. As long as the environment permits GMC formation, the conversion of that molecular gas into stars proceeds at a remarkably uniform macroscopic efficiency [cite: Bigiel08, Leroy08, Bigiel11].

confidence note: High confidence for local, main-sequence disk galaxies at kiloparsec averaging scales. However, confidence decreases dramatically at smaller physical scales (∼100 pc), where the relationship breaks down into significant scatter due to the discrete evolutionary life-cycle of individual GMCs moving through formation, starburst, and disruption phases.

sources: [cite: Bigiel08, Leroy08, Bigiel11]

[GAS-E02]

role: established

finding: The atomic neutral hydrogen (HI) surface density exhibits a hard saturation limit within galactic disks, beyond which star formation efficiency drops precipitously as the interstellar medium transitions to being dominated by atomic gas.

scope/boundary: Spatially resolved 21-cm HI interferometric mapping combined with resolved UV/IR SFR tracers in local spiral and dwarf galaxies. The finding maps the morphological transition from the molecule-dominated inner galactic disk to the atomic-dominated outer galactic disk and dwarf environments.

evidence: Interferometric 21-cm data from the THINGS survey reveals that the HI surface density saturates at a strict limit of approximately 9 M
⊙
	​

pc
−2
 across a remarkably wide range of local galaxies. In regions where the gas surface density exceeds this threshold, the interstellar medium undergoes a phase transition to become molecular-dominated. Conversely, in regions where HI is the dominant cold gas phase—typically the extended outer disks of spiral galaxies and throughout the entirety of many low-mass dwarf galaxies—the SFR per unit gas mass decreases dramatically with increasing galactocentric radius. The atomic gas alone correlates poorly with recent star formation, functioning instead as a deeply extended, slowly converting reservoir [cite: Bigiel08, Leroy08].

confidence note: Robust observational consensus. The exact physical mechanisms dictating this transition—whether driven by hydrostatic midplane pressure, metallicity-dependent dust shielding against the interstellar radiation field, or the cosmic UV background—remain actively modeled, but the empirical saturation limit is highly reliable.

sources: [cite: Bigiel08, Leroy08]

[GAS-E03]

role: established

finding: A strong, continuous global anti-correlation exists between both the atomic and molecular gas fractions and the total stellar mass of a galaxy, demonstrating that lower-mass galaxies are systematically and substantially more gas-rich than their massive counterparts.

scope/boundary: Global (integrated) measurements of galaxies at z≈0 selected by stellar mass, covering a dynamic range from 10
9
 to 10
11.5
M
⊙
	​

. This applies to both star-forming and quiescent populations, excluding environments dominated by massive cluster-driven ram-pressure stripping.

evidence: Representative volume-limited surveys, notably the GALEX Arecibo SDSS Survey (GASS) and its molecular counterpart (COLD GASS), have definitively shown that atomic gas fractions (M
HI
	​

/M
∗
	​

) drop steeply with increasing stellar mass, showing no sign of a plateau down to 10
9
M
⊙
	​

. Molecular gas fractions (M
H2
	​

/M
∗
	​

) also decrease with stellar mass, though the decline is notably more gradual. Consequently, the total cold gas reservoirs of main-sequence galaxies in the local universe remain heavily HI-dominated across the full stellar mass spectrum. The scatter in these relations strongly correlates with the molecular-to-atomic gas mass ratio, highlighting the complex internal phase-balance of galaxies as they grow in stellar mass [cite: Catinella10, Catinella18, Saintonge11a].

confidence note: Very high confidence. These mass-dependent scaling relations act as the fundamental z=0 boundary conditions that all cosmological hydrodynamic simulations and semi-analytic models must reproduce to successfully claim accurate baryonic physics.

sources: [cite: Catinella10, Catinella18, Saintonge11a]

[GAS-E04]

role: established

finding: The global molecular gas depletion time is not a universal constant; it varies systematically and strongly with a galaxy's specific star formation rate (sSFR) and its relative vertical offset from the star-forming main sequence.

scope/boundary: Global integrated CO(1-0) and CO(2-1) observations of massive galaxies (>10
9
M
⊙
	​

) spanning diverse morphological classifications. This encompasses galaxies ranging from highly active starbursts well above the main sequence to bulge-dominated quenching galaxies falling below it.

evidence: Multi-wavelength local surveys prove that a galaxy's position on the SFR–M
∗
	​

 plane is dictated by two coupled variables: the total mass of the molecular gas reservoir and the efficiency with which that gas is consumed. Galaxies with high sSFRs (starbursts) exhibit significantly shorter global molecular depletion times, indicating heavily enhanced macroscopic star formation efficiencies. Conversely, bulge-dominated galaxies positioned below the main sequence exhibit remarkably long molecular depletion times. The long-standing assumption of a single, universal star formation efficiency is fundamentally broken when integrating over entire galaxies with differing structural and kinematic properties [cite: Saintonge11b, Saintonge17].

confidence note: High confidence. This completely replaces the older paradigm that integrated star formation efficiency is fixed. The variance in depletion time across the main sequence is now an undisputed component of galactic evolution models.

sources: [cite: Saintonge11b, Saintonge17]

[GAS-E05]

role: established

finding: Unified empirical scaling relations successfully connect the molecular gas fraction and molecular depletion time to a galaxy's redshift and main-sequence offset, demonstrating that the cosmic evolution of the star formation rate density is primarily driven by the evolution of galactic gas fractions.

scope/boundary: Integrated molecular gas measurements spanning redshifts from z≈0 to z≈3. These relations rely on a combination of CO line fluxes and dust-continuum based mass estimates for galaxies situated on and around the empirically defined star-forming main sequence.

evidence: Extensive multi-tracer compilations (such as PHIBSS) confirm that molecular gas fractions increase monotonically with redshift, scaling approximately as (1+z)
2
 before flattening, directly tracking the rising cosmic star formation rate up to "cosmic noon". The depletion time, however, scales strongly as a function of the main sequence offset (δMS) and only weakly with redshift. This indicates that the fundamental regulatory mechanisms coupling gas supply to star formation efficiency operate via similar physical pathways across cosmic time, merely scaled up by the vastly larger gas reservoirs available in the early universe [cite: Tacconi18, Genzel15].

confidence note: Strong consensus on the general scaling laws. However, the exact power-law indices remain subject to calibration adjustments depending on the assumed metallicity-dependent α
CO
	​

 conversion factor and the choice of Initial Mass Function (IMF).

sources: [cite: Tacconi18, Genzel15]

[GAS-E06]

role: established

finding: A direct, tight, and nearly linear correlation dictates the relationship between the global star formation rate and the mass of the dense molecular gas phase, functioning independently of the broader molecular reservoir.

scope/boundary: Global measurements spanning normal local star-forming galaxies to extreme ultra-luminous infrared galaxies (ULIRGs). This finding is strictly limited to the dense gas phase (critical density n≳10
4
cm
−3
), predominantly traced by HCN(1-0) emission, and is fundamentally distinct from the bulk molecular gas traced by CO.

evidence: The luminosity of the HCN(1-0) line correlates linearly with the total infrared luminosity (a robust proxy for obscured SFR) over many orders of magnitude. This linear relationship suggests that star formation is fundamentally rate-limited by the availability and continuous supply of dense gas, rather than the size of the total molecular gas reservoir. While the bulk CO-traced gas exhibits wildly different depletion times between normal disks and starbursts, the dense gas depletion time remains much more uniform [cite: Gao04, Lada12].

confidence note: High confidence in the empirical relation itself. However, theoretical interpretation requires caution: the definition of "dense gas" depends heavily on the specific tracer's excitation conditions, and optical depth variations in HCN can complicate direct mass translations.

sources: [cite: Gao04, Lada12]

[GAS-E07]

role: established

finding: A non-linear global star formation law mathematically connects the total cold gas surface density (atomic plus molecular) to the total star formation rate surface density.

scope/boundary: Global, disk-averaged measurements of local starbursts and normal spiral galaxies. This finding applies exclusively to the total gas and integrates over entire galactic scales. It is explicitly distinct from spatially resolved, molecular-only studies.

evidence: A foundational power-law fit to globally averaged galaxy data yields a super-linear index of N≈1.4. This implies that the global star formation efficiency of the total gas increases in regions of higher average surface density. Physically, this super-linear steepening is heavily influenced by the phase transition from inert HI-dominated outer regimes to actively star-forming H2-dominated inner regimes. When these diverse zones are averaged together into a single galactic metric, the mathematical result is a super-linear slope [cite: Kennicutt98].

confidence note: Foundational astrophysical principle, fully validated for globally averaged total gas. Extreme care must be taken not to misapply this global super-linear total-gas law to spatially resolved molecular-only data, which follows the linear relation outlined in GAS-E01.

sources: [cite: Kennicutt98]

[GAS-E08]

role: established

finding: Morphological stabilization (theory/model) effectively suppresses the star formation efficiency of a molecular gas disk without requiring the catastrophic expulsion or starvation of the gas reservoir.

scope/boundary: Hydrodynamic numerical simulations (theory/model) of disk galaxies with varying bulge-to-total mass ratios, explicitly focused on non-expulsive, dynamically driven quenching mechanisms.

evidence: In advanced simulations, the presence of a steep central gravitational potential well—generated by a massive stellar bulge—fundamentally alters gas kinematics. The bulge increases the epicyclic frequency and the velocity dispersion of the surrounding gas disk. This kinematic heating reduces the Toomre Q parameter's instability index, preventing the cold gas from gravitationally fragmenting into giant molecular clouds. The result is a profound suppression of star formation efficiency, allowing a galaxy to transition to quiescence while retaining a substantial, but inert, cold gas fraction [cite: Martig09].

confidence note: Well-established theoretical mechanism ("morphological quenching"). It provides a vital interpretive framework for resolving the observational paradox of "red and dead" early-type galaxies that still harbor significant, yet non-star-forming, molecular gas disks.

sources: [cite: Martig09]

[GAS-E09]

role: established

finding: The cosmic density of molecular hydrogen (ρ
H2
	​

) underwent dramatic and rapid evolution, peaking at "cosmic noon" (z≈1.5−3) before declining sharply by a factor of approximately six to its present-day value.

scope/boundary: Cosmological volume averages derived from deep, blind millimeter and sub-millimeter spectral line intensity mapping and discrete source surveys, ensuring the samples are flux-limited rather than biased by pre-selection criteria.

evidence: Blind CO luminosity function measurements from volumetric surveys (such as the ALMA Spectroscopic Survey in the Hubble Ultra Deep Field [ASPECS] and the COLDz survey) map the cold gas history of the universe. They demonstrate a steep drop in the volume-averaged molecular gas density from its peak at z≈1.5 down to z=0. This molecular evolution closely mirrors the established cosmic star formation rate density curve. In stark contrast, the cosmic density of neutral atomic gas (HI) remains remarkably flat over the same cosmological epoch, acting as a massive, stable buffer [cite: Decarli20, Riechers19].

confidence note: Strong observational foundation achieved only recently via unprecedentedly deep ALMA and VLA campaigns, resolving earlier uncertainties that were heavily reliant on extrapolating targeted high-z observations.

sources: [cite: Decarli20, Riechers19]

[GAS-E10]

role: established

finding: Gas-regulator and equilibrium models (theory/model) robustly connect cosmological inflow, instantaneous gas mass, outflow mass-loading, and gas recycling to reproduce the observed cosmic baryon cycle, revealing that continuous massive gas accretion is mandatory for galaxy survival.

scope/boundary: Analytical and semi-empirical models (theory/model) that integrate empirically derived cosmic volume densities of stellar mass, SFR, HI, and H2 over cosmic time.

evidence: By evaluating the integral of the cosmic star formation rate, these models demonstrate that the continuous growth of the cosmic stellar mass density cannot be accounted for by the consumption of the existing, measured H2 and HI reservoirs alone. To maintain equilibrium, these models require a continuous, massive net infall of ionized gas from the circumgalactic medium to refuel the atomic HI reservoirs, coupled with a subsequent radial inflow to the central galactic regions to sustain the H2 phase. Without this constant replenishment, galaxies would exhaust their star-forming fuel on timescales vastly shorter than the Hubble time [cite: Walter20].

confidence note: This theoretical framework accurately links multiple independent observational scaling relations, serving as the standard paradigm for the secular evolution of main-sequence galaxies across cosmic time.

sources: [cite: Walter20]

[GAS-E11]

role: established

finding: Long-wavelength Rayleigh-Jeans dust continuum emission serves as a robust, empirically calibrated proxy for estimating the total interstellar medium (ISM) cold gas mass in high-redshift galaxies.

scope/boundary: High-redshift, massive star-forming galaxies observed at millimeter/sub-millimeter wavelengths (e.g., ALMA Band 7). The technique fundamentally relies on the assumption of a relatively uniform, scale-invariant dust-to-gas ratio for massive galaxies near solar metallicity.

evidence: Extensive cross-calibration against local galaxy samples with fully resolved CO, HI, and dust mapping demonstrates that the monochromatic dust continuum luminosity (specifically at rest-frame 850 μm) correlates tightly with the total ISM mass. Because dust emission is optically thin in this regime, it provides a direct measure of the dust mass. Applying a standard dust-to-gas ratio permits rapid, highly accurate gas mass estimations without the prohibitive integration times required for deep CO line surveys, allowing for massive statistical sample sizes at high redshift [cite: Scoville16, Scoville17].

confidence note: Highly reliable for massive, near-solar metallicity galaxies situated on the main sequence. However, the calibration degrades severely in low-mass, low-metallicity environments where the dust-to-gas ratio drops precipitously and non-linearly.

sources: [cite: Scoville16, Scoville17]

2. Open debates and tensions

[GAS-D01]

role: debate

debate_topic: Linear versus super-linear slopes in the molecular Kennicutt-Schmidt star-formation law.

competing positions: One persistent paradigm asserts that the global scaling between total gas surface density and SFR surface density is inherently super-linear (N≈1.4), implying that the fundamental star formation efficiency intrinsically increases with higher gas surface densities. Conversely, resolved cloud-scale studies argue that when isolating the molecular gas phase specifically, the relationship is strictly linear (N≈1.0), asserting that the super-linear slope observed in global relations is merely an artifact of averaging over the morphological phase transition from diffuse HI to dense H2.

why unresolved: The tension is rooted in the blending of physical scales (global galactic averages versus kiloparsec-resolved data) and tracer variations. Global averages inadvertently incorporate vast, low-density HI regions that do not form stars, which inherently steepens the correlation when plotted against total gas. Sub-kiloparsec mapping isolates fully molecular clouds where efficiency may be relatively uniform, but struggles to account for diffuse, inter-cloud gas.

source/sample/calibration boundaries: Global measurements integrating total gas (HI + H2) across diverse whole-galaxy types versus spatially resolved (sub-kpc) isolated measurements of CO(1-0) in local disks.

sources representing the competing evidence: [cite: Kennicutt98, Bigiel08, Leroy08]

[GAS-D02]

role: debate

debate_topic: Bimodal starburst sequences versus continuous main-sequence scaling behavior.

competing positions: Early high-redshift targeted analyses proposed a strict, physical bimodality: a distinct "disk sequence" characterized by long, steady gas depletion times, and a separate "starburst sequence" triggered by major mergers, characterized by highly elevated star formation efficiencies and extremely short depletion times. Contemporary integrated scaling models argue heavily against strict bimodality, suggesting instead a continuous, smooth variation of depletion time that scales functionally with a galaxy's vertical offset from the main sequence (δMS).

why unresolved: The debate is fundamentally driven by difficulties in cross-calibrating the CO-to-H2 conversion factor (α
CO
	​

). If a dramatically lower, distinct α
CO
	​

 is artificially forced onto all high-SFR ULIRG systems, a bimodal gap artificially appears in the depletion time plots. If an excitation-dependent, continuously varying α
CO
	​

 is applied, the bimodal gap smooths out into a continuous functional distribution.

source/sample/calibration boundaries: High-redshift targeted sub-millimeter and ULIRG galaxies versus volume-limited, mass-selected representative surveys.

sources representing the competing evidence: [cite: Daddi10, Tacconi18, Saintonge17]

[GAS-D03]

role: debate

debate_topic: The exact magnitude, physical drivers, and application of systematic variations in the CO-to-H2 conversion factor (α
CO
	​

).

competing positions: Standard, legacy methodologies frequently apply a uniform Galactic value (α
CO
	​

≈4.3) for all main-sequence disks and a depressed, step-function value (α
CO
	​

≈0.8) for starbursts. Opposing advanced methods derive α
CO
	​

 dynamically or via resolved dust-calibrations on kpc scales, finding that the conversion factor varies continuously with metallicity, local gas surface density, and velocity dispersion, often dropping by factors of 3 to 10 in the central kiloparsec of entirely normal, non-starburst disks.

why unresolved: Direct observational measurement of cold, self-shielded H2 mass is physically impossible due to its lack of a permanent dipole moment. Consequently, all α
CO
	​

 derivations rely on secondary tracers (dust modeling, resolved gas dynamics, or CO isotopologues). Each secondary tracer carries its own degenerate physical assumptions, such as a perfectly constant dust-to-gas ratio or the assumption that all observed molecular clouds are perfectly virialized.

source/sample/calibration boundaries: Kiloparsec-resolved dust and CO mapping in local spiral galaxies versus global, integrated CO luminosity measurements.

sources representing the competing evidence: [cite: Bolatto13, Sandstrom13]

[GAS-D04]

role: debate

debate_topic: Supply starvation versus morphological/kinematic SFE suppression in galaxy quenching.

competing positions: The classical view of galaxy quenching assumes that galaxies cease forming stars strictly because their cold gas supply is exhausted or removed (via starvation, where cosmological infall halts, or via ram-pressure stripping). Alternatively, spatially resolved kinematic studies and morphological models suggest that galaxies can easily retain massive cold gas reservoirs that are rendered entirely inert. High velocity dispersions, kinematic shear, or bulge-induced stabilization can severely suppress the star formation efficiency without physically removing the gas.

why unresolved: Observational data provides conflicting snapshots depending on the selected sample. Many post-starburst and green-valley galaxies exhibit extremely low global gas fractions (supporting the starvation hypothesis). Conversely, deep, resolved ALMA observations frequently find massive, localized, dynamically disturbed molecular reservoirs in quiescent early-type galaxies (supporting the SFE suppression hypothesis).

source/sample/calibration boundaries: Hydrodynamic numerical simulations of bulge stabilization versus resolved ALMA observations of quiescent, post-merger, or early-type massive galaxies.

sources representing the competing evidence: [cite: Martig09, Ellison20]

[GAS-D05]

role: debate

debate_topic: Constant versus mildly evolving depletion time after normalization for main-sequence offset.

competing positions: Some unified scaling frameworks claim that after controlling mathematically for the specific SFR offset (δMS), the inherent molecular gas depletion time remains roughly constant across all of cosmic time, implying standard star formation physics. Other large multi-wavelength meta-analyses report a persistent, mild redshift evolution, where the depletion time scales as (1+z)
−0.6
, implying that galaxies consumed their gas systematically faster in the early universe, even when situated perfectly on the main sequence.

why unresolved: The tension arises from complex systematics in cross-calibrating different SFR indicators (e.g., UV+IR calibrations versus SED fitting) and molecular gas tracers (CO line fluxes versus Rayleigh-Jeans Dust continuum) across vastly different redshift baselines and instrument sensitivities.

source/sample/calibration boundaries: Integrated molecular gas measurements spanning from z=0 to z=3.

sources representing the competing evidence: [cite: Tacconi18, Genzel15]

[GAS-D06]

role: debate

debate_topic: Dense gas fraction variations versus intrinsic dense gas SFE variations in driving starbursts.

competing positions: The initial foundational framework suggests that the extreme enhancement in star formation seen in starburst galaxies is driven primarily by a higher dense gas fraction (i.e., more of the bulk molecular gas is compressed to high densities), with the SFE of the dense gas itself remaining a universal constant. Conversely, recent resolved cloud-scale surveys argue that the SFE of the dense gas itself varies significantly depending on the local galactic environment, bar-driven inflows, and turbulent pressure.

why unresolved: The debate hinges on the observational sensitivity limits and chemical complexities of high-critical-density tracers like HCN. While HCN effectively traces high-density gas, its emission is subject to severe optical depth effects and excitation temperature variations in dense starburst cores, which can mimic or mask true mass variations.

source/sample/calibration boundaries: Global HCN luminosity measurements in ULIRGs versus arcsecond-resolution ALMA dense gas mapping in nearby spiral galaxy centers.

sources representing the competing evidence: [cite: Gao04, Leroy21]

[GAS-D07]

role: debate

debate_topic: The exact magnitude and peak redshift of the cosmic H2 density history.

competing positions: While blind molecular line surveys generally agree on the overarching shape of the cosmic H2 history, they disagree on the absolute volume-averaged density at the peak. Some analyses utilizing dust-continuum and specific CO transitions suggest a broad, flat plateau of H2 density extending well beyond z>3. Others, utilizing comprehensive CO luminosity functions, indicate a sharper peak at z≈1.5 followed by a steady, measured decline at earlier epochs.

why unresolved: Cosmic variance heavily limits the interpretations from the extremely deep, yet spatially narrow fields utilized by ALMA and the VLA (e.g., Hubble Ultra Deep Field vs. the COSMOS field). Furthermore, detecting high-redshift gas often relies on mid-J CO transitions; converting these to ground-state CO(1-0) luminosities introduces significant uncertainties related to the assumed sub-thermal excitation ladders.

source/sample/calibration boundaries: Deep volumetric blind line surveys relying on differing observational fields, differing primary transitions, and disparate conversion formalisms.

sources representing the competing evidence: [cite: Decarli20, Riechers19]

3. Key measurements and numbers

[GAS-N01]

role: measurement

metric and value/range: Spatially resolved molecular gas depletion time t
dep,mol
	​

≈2.0 to 2.3 Gyr in normal star-forming disks.

Metric	Value	Variation/Scatter
Molecular Depletion Time (t
dep,mol
	​

)	∼2.3 Gyr	±0.3 dex globally
K-S Power Law Index (N)	1.0	±0.2

sample, redshift, tracer, instrument/survey, and method: Local universe (z≈0), spatially resolved (∼ kpc scale) disk galaxies. Traced via CO(2-1) and CO(1-0) with the IRAM 30m (HERACLES survey) and BIMA SONG, mapped against UV+IR SFR surface densities.

conversion/calibration caveat: This value relies explicitly on applying a fixed Galactic α
CO
	​

 conversion factor across the entire disk. If α
CO
	​

 physically drops in galaxy centers due to higher velocity dispersions, the calculated central gas mass decreases, meaning the true central depletion time would be correspondingly much shorter.

primary verified source: [cite: Bigiel08, Bigiel11]

[GAS-N02]

role: measurement

metric and value/range: Atomic gas surface density saturation limit Σ
HI
	​

≈9 M
⊙
	​

pc
−2
.

Parameter	Value	Phase Regime
Σ
HI
	​

 Saturation Limit	∼9 M
⊙
	​

pc
−2
	Transition from HI to H2
Outer Disk SFE Decline	Exponential	HI-dominated

sample, redshift, tracer, instrument/survey, and method: Nearby spiral and dwarf galaxies at z≈0, traced via 21-cm emission using the VLA (THINGS survey), mapped at sub-kpc resolution.

conversion/calibration caveat: This limit is a macroscopic, azimuthal average across the disk. Localized, highly dense HI filaments or discrete clouds can exceed this value briefly on sub-parsec scales before rapidly transitioning to molecular hydrogen due to self-shielding.

primary verified source: [cite: Bigiel08]

[GAS-N03]

role: measurement

metric and value/range: Integrated molecular gas scaling relation with main-sequence offset: t
dep
	​

∝δMS
−0.44
 and M
H2
	​

/M
∗
	​

∝δMS
+0.53
.

Scaling Relation	Power-law Index	Dominant Driver
t
dep
	​

 vs δMS	−0.44	Star Formation Efficiency
M
H2
	​

/M
∗
	​

 vs δMS	+0.53	Gas Reservoir Mass

sample, redshift, tracer, instrument/survey, and method: Global measurements of 1,444 star-forming galaxies from z=0 to z=4 via the PHIBSS survey and literature compilations, utilizing CO line fluxes and dust continuum.

conversion/calibration caveat: This measurement requires precise normalization to an evolving, empirically defined main sequence of star formation. The exact power-law parameters are therefore highly sensitive to the chosen functional definition of the main sequence ridge-line at any given redshift.

primary verified source: [cite: Tacconi18]

[GAS-N04]

role: measurement

metric and value/range: Standard Milky Way CO-to-H2 conversion factor α
CO
	​

≈4.3 M
⊙
	​

(K km s
−1
pc
2
)
−1
 (corresponding to an column density factor of X
CO
	​

≈2×10
20
cm
−2
(K km s
−1
)
−1
).

sample, redshift, tracer, instrument/survey, and method: Foundational value calibrated across Milky Way giant molecular clouds via dynamical virial masses, diffuse gamma-ray profiling, and dust extinction mapping.

conversion/calibration caveat: The mass unit explicitly includes a factor of 1.36 to account for the cosmological abundance of helium. This factor is heavily metallicity-dependent; the linear scaling breaks down entirely at sub-solar metallicities where CO is easily photo-dissociated but H2 remains self-shielded, creating massive reservoirs of "CO-dark" gas.

primary verified source: [cite: Bolatto13]

[GAS-N05]

role: measurement

metric and value/range: Global Kennicutt-Schmidt total gas exponent N≈1.4±0.15.

Star Formation Law	Index (N)	Physical Scope
Global Total Gas (HI + H2)	1.4±0.15	Whole-galaxy averages
Resolved Molecular (H2 only)	1.0±0.2	kpc-scale, inner disks

sample, redshift, tracer, instrument/survey, and method: Local starbursts and normal spirals (z≈0). Measures integrated total gas surface density against total SFR surface density derived from a combination of H-alpha and IR luminosities.

conversion/calibration caveat: This metric is valid only for the total combined gas (atomic + molecular) when averaged over whole galaxies. It represents a convolution of physical states and cannot be mathematically applied to spatially resolved, purely molecular gas clouds.

primary verified source: [cite: Kennicutt98]

[GAS-N06]

role: measurement

metric and value/range: Evolution of cosmic molecular gas density ρ
H2
	​

, demonstrating a drop by a factor of roughly 6 from its peak at z≈1.5 down to z≈0.

sample, redshift, tracer, instrument/survey, and method: ALMA Spectroscopic Survey in the Hubble Ultra Deep Field (ASPECS), utilizing deep 3mm and 1.2mm volumetric blind scans for CO emission lines over well-defined cosmological volumes.

conversion/calibration caveat: Volume calculations require complex completeness corrections for faint sources. Furthermore, detecting high-z gas often captures mid-J CO lines (e.g., CO(3-2)), requiring assumptions regarding the thermal excitation ladder to convert these detections down to fundamental ground-state CO(1-0) luminosities.

primary verified source: [cite: Decarli20]

[GAS-N07]

role: measurement

metric and value/range: Characteristic molecular gas fractions (f
H2
	​

=M
H2
	​

/(M
H2
	​

+M
∗
	​

)) reaching up to ∼44% at z=2.3 for massive main-sequence galaxies, dropping to ∼34% by z=1.2.

sample, redshift, tracer, instrument/survey, and method: High-redshift targeted samples (PHIBSS) tracing CO(3-2) with the IRAM Plateau de Bure Interferometer, specifically targeting massive galaxies situated securely on the main sequence.

conversion/calibration caveat: Highly sensitive to the assumed α
CO
	​

 conversion factor. If the high-redshift main sequence behaves kinematically more like local merging starbursts (warranting a lower α
CO
	​

), the true calculated gas fraction would be significantly lower.

primary verified source: [cite: Tacconi18]

4. What remains unknown

[GAS-U01]

role: future

gap: The precise physical mechanisms driving extreme cloud-to-cloud scatter in the resolved molecular star-formation law at sub-kiloparsec scales.

why it matters: While coarse kiloparsec averages yield a reassuringly constant depletion time, zooming in to 50-100 parsec scales reveals enormous, non-linear scatter. Understanding this scatter is essential for linking macro-scale galaxy evolution models with the micro-scale physics of turbulent giant molecular cloud (GMC) collapse and the immediate, localized effects of stellar feedback.

observation/model needed: Widespread, homogeneous ∼50 pc resolution interferometric mapping of diverse galactic environments across the local volume, pairing dense gas tracers with immediate feedback metrics to track the localized time-evolution of individual clouds.

sources defining the gap: [cite: Leroy21, Schruba11]

[GAS-U02]

role: future

gap: Robust, widely applicable calibration of the dust-to-gas ratio at extremely high redshifts and low metallicities.

why it matters: The Rayleigh-Jeans dust continuum is arguably the most observationally efficient tracer of total gas mass at z>1, circumventing the need for hundreds of hours of CO line integration. However, if dust destruction rates, dust production pathways by early supernovae, or the metallicity-scaling of the dust-to-gas ratio deviate fundamentally from local universe calibrations, current mass estimates for the early universe could be severely biased.

observation/model needed: Deep cross-calibrations of high-redshift dust continuum against deep, multi-line CO and atomic carbon [CI] mapping across a significantly broader mass and metallicity baseline.

sources defining the gap: [cite: Scoville17, Bolatto13]

[GAS-U03]

role: future

gap: Disentangling simple gas exhaustion (starvation) from morphological/kinematic suppression in quenching galaxies using purely observational boundaries.

why it matters: Identifying that a red, quiescent galaxy currently possesses a low gas fraction does not prove that a lack of gas caused the quenching event. The gas may have been morphologically stabilized first, preventing star formation, followed by a slow, secular exhaustion of the remaining inert reservoir. Breaking this degeneracy determines whether galaxies die fundamentally from a loss of fuel or a loss of efficiency.

observation/model needed: High-resolution, spatially resolved kinematic mapping of the residual cold gas in "green valley" and recently quenched galaxies to measure turbulence, shear, and Toomre Q stability parameters prior to complete gas depletion.

sources defining the gap: [cite: Martig09, Ellison20]

[GAS-U04]

role: future

gap: The exact physical interplay between cosmological net gas accretion and outflow mass-loading in the gas-regulator equilibrium framework.

why it matters: Analytical models definitively demonstrate that galaxies must accrete massive amounts of gas to survive. However, determining whether this accreted gas rapidly joins the molecular phase, or if the molecular reservoir is instead sustained by the cooling and recycling of fountain outflows, fundamentally alters our understanding of the circumgalactic medium's role in the baryon cycle.

observation/model needed: Direct observational constraints bridging cold-gas kinematics inside the galactic disk with the ionized/atomic inflow/outflow structures residing in the immediate circumgalactic medium.

sources defining the gap: [cite: Walter20]

[GAS-U05]

role: future

gap: Resolving whether extreme starbursts are driven by absolute changes in the dense gas fraction or by intrinsic increases in the dense-gas star formation efficiency.

why it matters: Standard empirical models (e.g., Gao & Solomon) assume the efficiency of star formation within dense gas (>10
4
cm
−3
) is universally constant, and that starbursts achieve high SFRs simply by possessing a higher fraction of dense gas. Recent resolved observations, however, suggest the dense gas itself might form stars more efficiently under extreme turbulent conditions.

observation/model needed: Multi-line, high-J CO and HCN/HCO+ excitation modeling at high spatial resolution within both local ULIRGs and high-z starbursts, effectively addressing the severe optical depth and excitation biases that plague single-line dense gas tracers.

sources defining the gap: [cite: Gao04, Leroy21]

5. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | JWST discoveries of AGN feedback quenching | [source 10, 23] | Reason: Violates hard scientific boundary prohibiting the inclusion of AGN-centered findings in this non-AGN area.

UNCITED_NOT_USABLE | Radio AGN triggering in ETGs | [source 22] | Reason: Violates boundary explicitly excluding AGN-framed mechanisms and their associated host-galaxy effects.

UNCITED_NOT_USABLE | The depletion time literally predicts guaranteed gas exhaustion | Interpretative error present in many secondary snippets | Reason: Hard boundary violation. Every dynamic equilibrium model (e.g., Walter20) indicates that inflow, outflow, and continuous phase recycling break the interpretation of t
dep
	​

 as a literal lifespan; t
dep
	​

 is strictly an instantaneous efficiency metric.

UNCITED_NOT_USABLE | Low gas fractions prove exhaustion caused quenching | Interpretative error in literature | Reason: Hard boundary violation. As demonstrated in Martig09 and Ellison20, morphological stabilization or kinematic shear can radically reduce SFE, meaning the presence of little gas may simply be the end-state of a galaxy whose star formation was halted by dynamic mechanisms long before final consumption.

UNCITED_NOT_USABLE | Future-dated 2026 conference talks and simulation papers | e.g., [source 25, 39, 143, 173] | Reason: Fails explicit coverage requirement: "Do not cite 2026 or future-dated search results."

6. Source identity ledger

Saintonge et al. (2017, ApJS) | DOI:10.3847/1538-4365/aa97e0; arXiv:1710.02157; ADS:2017ApJS..233...22S | role=measurement | Census of local molecular gas fractions and global scaling relations in xCOLD GASS.
Catinella et al. (2018, MNRAS) | DOI:10.1093/mnras/sty089; arXiv:1802.02373; ADS:2018MNRAS.476..875C | role=measurement | Atomic gas scaling relations and molecular-to-atomic gas mass ratios from xGASS.
Tacconi et al. (2018, ApJ) | DOI:10.3847/1538-4357/aaa4b4; arXiv:1702.01140; ADS:2018ApJ...853..179T | role=established | Unified scaling relations of gas depletion time and molecular fraction across cosmic time from PHIBSS.
Decarli et al. (2020, ApJ) | DOI:10.3847/1538-4357/abb82d; arXiv:2009.10744; ADS:2020ApJ...902..110D | role=measurement | Evolution of cosmic molecular gas density and CO luminosity functions up to z~4.5 from ASPECS.
Walter et al. (2020, ApJ) | DOI:10.3847/1538-4357/abb82e; arXiv:2009.10748; ADS:2020ApJ...902..111W | role=established | Baryon cycle evolution and cosmological constraints on net gas accretion over cosmic time from ASPECS.
Riechers et al. (2019, ApJ) | DOI:10.3847/1538-4357/aafc27; arXiv:1808.04371; ADS:2019ApJ...872....7R | role=measurement | CO luminosity function shape and early cold gas history of the universe from COLDz.
Leroy et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2782; arXiv:0810.2556; ADS:2008AJ....136.2782L | role=established | Spatially resolved star formation efficiency of atomic and molecular gas in nearby galaxies.
Bigiel et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2846; arXiv:0810.2541; ADS:2008AJ....136.2846B | role=established | Sub-kiloparsec star formation law showing constant molecular gas depletion time in disks.
Schruba et al. (2011, AJ) | DOI:10.1088/0004-6256/142/2/37; arXiv:1105.4605; ADS:2011AJ....142...37S | role=established | Scale dependence of the molecular star formation law and depletion times in disk galaxies.
Bolatto et al. (2013, ARA&A) | DOI:10.1146/annurev-astro-082812-140944; arXiv:1301.7436; ADS:2013ARA&A..51..207B | role=caveat | Review of the physical dependencies and metallicity variations of the CO-to-H2 conversion factor (alpha_CO).
Kennicutt (1998, ApJ) | DOI:10.1086/305588; arXiv:astro-ph/9712213; ADS:1998ApJ...498..541K | role=established | Global Kennicutt-Schmidt law relating total gas surface density to star formation rate surface density.
Ellison et al. (2020, MNRAS) | DOI:10.1093/mnrasl/slz185; arXiv:1912.01015; ADS:2020MNRAS.493L..39E | role=measurement | Resolved molecular gas scaling relations on 1.5 kpc scales in the ALMA-QUEST survey.
Leroy et al. (2021, ApJS) | DOI:10.3847/1538-4365/ac17f3; arXiv:2104.07739; ADS:2021ApJS..257...43L | role=measurement | Arcsecond-resolution CO(2-1) imaging census of giant molecular clouds in nearby spirals from PHANGS.
Saintonge et al. (2011, MNRAS) | DOI:10.1111/j.1365-2966.2011.18677.x; arXiv:1103.1642; ADS:2011MNRAS.415...32S | role=established | Initial molecular gas fraction relations and detection thresholds from COLD GASS.
Saintonge et al. (2011, MNRAS) | DOI:10.1111/j.1365-2966.2011.18678.x; arXiv:1103.1644; ADS:2011MNRAS.415...61S | role=established | Non-universality of CO-based molecular depletion times and their strong correlation with specific SFR.
Daddi et al. (2010, ApJ) | DOI:10.1088/2041-8205/714/1/L118; arXiv:1004.1673; ADS:2010ApJ...714L.118D | role=debate | Bimodal sequences of star formation in disk and starburst galaxies with different gas depletion times.
Gao & Solomon (2004, ApJ) | DOI:10.1086/382999; arXiv:astro-ph/0310339; ADS:2004ApJ...606..271G | role=established | Linear relation between star formation rate and dense gas mass traced by HCN emission.
Lada et al. (2012, ApJ) | DOI:10.1088/0004-637X/745/2/190; arXiv:1111.5173; ADS:2012ApJ...745..190L | role=established | Linear scaling of star formation rate with dense molecular gas mass within Galactic molecular clouds.
Martig et al. (2009, ApJ) | DOI:10.1088/0004-637X/707/1/250; arXiv:0909.1325; ADS:2009ApJ...707..250M | role=theory | Numerical simulations showing star formation suppression in gas disks by morphological stabilization of bulges.
Catinella et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2009.16175.x; arXiv:0912.1610; ADS:2010MNRAS.403..683C | role=established | Baseline atomic gas scaling relations versus stellar mass and structures from GASS.
Scoville et al. (2016, ApJ) | DOI:10.3847/0004-637X/820/2/83; arXiv:1511.02529; ADS:2016ApJ...820...83S | role=measurement | Calibration and application of long-wavelength dust continuum as a proxy for total cold gas mass at high redshift.
Scoville et al. (2017, ApJ) | DOI:10.3847/1538-4357/aa61a0; arXiv:1702.04729; ADS:2017ApJ...837..150S | role=measurement | Scaling relations of dust-estimated gas mass and required accretion rates in high-redshift galaxies.
Bigiel et al. (2011, ApJL) | DOI:10.1088/2041-8205/730/2/L13; arXiv:1101.4984; ADS:2011ApJ...730L..13B | role=established | Spatially resolved molecular gas depletion time is constant at ~2.3 Gyr across nearby disks.
Sandstrom et al. (2013, ApJ) | DOI:10.1088/0004-637X/777/1/5; arXiv:1212.1208; ADS:2013ApJ...777....5S | role=caveat | Spatially resolved kpc-scale measurements of the CO-to-H2 conversion factor and dust-to-gas ratio in 26 galaxies.
Genzel et al. (2015, ApJ) | DOI:10.1088/0004-637X/800/1/20; arXiv:1409.1171; ADS:2015ApJ...800...20G | role=established | Combined scaling relations of gas fractions and depletion times up to z~3.

GAS_DR_PACKET_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- orcid.org Amelie Saintonge - ORCID Opens in a new window — https://orcid.org/0000-0003-4357-3450
- arxiv.org [1710.02157] xCOLD GASS: the complete IRAM-30m legacy survey of molecular gas for galaxy evolution studies - arXiv Opens in a new window — https://arxiv.org/abs/1710.02157
- arxiv.org arXiv:2304.04465v1 [astro-ph.GA] 10 Apr 2023 Opens in a new window — https://arxiv.org/pdf/2304.04465
- arxiv.org arXiv:2211.09969v1 [astro-ph.GA] 18 Nov 2022 Opens in a new window — https://arxiv.org/pdf/2211.09969
- academic.oup.com Cold gas mass measurements for the era of large optical spectroscopic surveys | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/518/1/353/6823712
- arxiv.org [1812.08180] PHIBSS2: survey design and z=0.5-0.8 results. Molecular gas reservoirs during the winding-down of star formation - arXiv Opens in a new window — https://arxiv.org/abs/1812.08180
- arxiv.org [1702.01140] PHIBSS: Unified Scaling Relations of Gas Depletion Time and Molecular Gas Fractions - arXiv Opens in a new window — https://arxiv.org/abs/1702.01140
- academic.oup.com Evolution of gas velocity dispersion in discs from z ∼ 8 to z ∼ 0.5 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/544/3/2777/8261520
- ned.ipac.caltech.edu arXiv:1806.06712v1 [astro-ph.GA] 18 Jun 2018 Opens in a new window — http://ned.ipac.caltech.edu/level5/March18/Combes/paper.pdf
- arxiv.org [2002.08640] The ALMA Spectroscopic Survey in the HUDF: The Cosmic Dust and Gas Mass Densities in Galaxies up to $z\sim3$ - arXiv Opens in a new window — https://arxiv.org/abs/2002.08640
- arxiv.org arXiv:2008.08087v1 [astro-ph.GA] 18 Aug 2020 Opens in a new window — https://arxiv.org/pdf/2008.08087
- ricerca.sns.it AGN impact on the molecular gas in galactic centers as probed by CO lines Opens in a new window — https://ricerca.sns.it/bitstream/11384/115529/1/2202.00697.pdf
- arxiv.org [2009.10744] The ALMA Spectroscopic Survey in the HUDF: Multi-band constraints on line luminosity functions and the cosmic density of molecular gas - arXiv Opens in a new window — https://arxiv.org/abs/2009.10744
- academic.oup.com Direct detection of cool molecular gas in a star-forming galaxy at z=7.31 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/549/3/stag924/8704346
- arxiv.org [1808.04371] COLDz: Shape of the CO Luminosity Function at High Redshift and the Cold Gas History of the Universe - arXiv Opens in a new window — https://arxiv.org/abs/1808.04371
- arxiv.org [1910.12883] Automated Mining of the ALMA Archive in the COSMOS Field (A3COSMOS): II. Cold Molecular Gas Evolution out to Redshift 6 - arXiv Opens in a new window — https://arxiv.org/abs/1910.12883
- arxiv.org ADF22-WEB: Detection of a molecular gas reservoir in a massive quiescent galaxy located in a z≈3 proto-cluster core - arXiv Opens in a new window — https://arxiv.org/html/2502.06538v1
- research.iac.es An ALMA CO(1-0) survey of the 2Jy sample: large and massive molecular disks in radio AGN host galaxies Opens in a new window — https://research.iac.es/preprints/files/PP24083.pdf
- doi.org REBELS-IFU: Linking damped Lyman-α absorption to [C II] emission and dust content in the Epoch of Reonisation | Astronomy & Astrophysics (A&A) - DOI Opens in a new window — https://doi.org/10.1051/0004-6361/202557654
- arxiv.org Overmassive black holes in the early Universe can be explained by gas-rich, dark matter-dominated galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/2506.13852
- pure.ed.ac.uk ALMA measures rapidly depleted molecular gas reservoirs in massive quiescent galaxies at z~1.5 - Account Opens in a new window — https://www.pure.ed.ac.uk/ws/files/331405338/2012.01433v1.pdf
- arxiv.org ALMA reveals spatially-resolved properties of molecular gas in the host galaxy of FRB 20191001A at z = 0.2340 - arXiv Opens in a new window — https://arxiv.org/html/2407.01889v1
- arxiv.org arXiv:2102.07881v1 [astro-ph.GA] 15 Feb 2021 Opens in a new window — https://arxiv.org/pdf/2102.07881
- arxiv.org [1802.02373] xGASS: Total cold gas scaling relations and molecular-to-atomic gas ratios of galaxies in the local Universe - arXiv Opens in a new window — https://arxiv.org/abs/1802.02373
- academic.oup.com xGASS: gas-rich central galaxies in small groups and their connections to cosmic web gas feeding - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/466/4/4795/2903848
- arxiv.org [1810.12158] Atomic hydrogen in IllustrisTNG galaxies: the impact of environment parallelled with local 21-cm surveys - arXiv Opens in a new window — https://arxiv.org/abs/1810.12158
- arxiv.org Tracing Quenching in Nearby Galaxies Through Inner Surface Mass Density and Cold Gas Content - arXiv Opens in a new window — https://arxiv.org/pdf/2511.18227
- academic.oup.com Enhanced atomic gas fractions in recently merged galaxies: quenching is not a result of post-merger gas exhaustion | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/478/3/3447/4995926
- academic.oup.com Cloud-scale molecular gas properties of the ANTENNAE merger: a comparative study with PHANGS-ALMA galaxies and NGC 3256 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/530/1/597/7637225
- arxiv.org Stellar structures, molecular gas, and star formation across the PHANGS sample of nearby galaxies - arXiv Opens in a new window — https://arxiv.org/html/2109.04491v3
- academic.oup.com Multiphase magnetic fields in the galaxy NGC 3627 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/519/1/1068/6862107
- kiss.caltech.edu arXiv:2101.02855v1 [astro-ph.GA] 8 Jan 2021 Opens in a new window — https://www.kiss.caltech.edu/papers/starform/papers/2101.02855.pdf
- arxiv.org ALMA FACTS III. High-Resolution CO(2-1)/CO(1-0) Maps of Twelve Nearby Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2507.13498v2
- arxiv.org [0810.2556] The Star Formation Efficiency in Nearby Galaxies: Measuring Where Gas Forms Stars Effectively - arXiv Opens in a new window — https://arxiv.org/abs/0810.2556
- pmc.ncbi.nlm.nih.gov Fast and inefficient star formation due to short-lived molecular clouds and rapid feedback - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC6544524/
- ned.ipac.caltech.edu Outskirts of Distant Galaxies In Absorption - NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Chen/paper.pdf
- archiv.ub.uni-heidelberg.de Quantifying the environmental dependence of the molecular cloud lifecycle in 54 main sequence galaxies Opens in a new window — https://archiv.ub.uni-heidelberg.de/volltextserver/33195/1/pp_JKim_thesis2_print_pdfa.pdf
- open-research-europe.ec.europa.eu Atacama Large Aperture Submillimeter Telescope (AtLAST) science: Gas and dust in nearby galaxies. - Open Research Europe Opens in a new window — https://open-research-europe.ec.europa.eu/articles/4-148
- nu.to.infn.it Astronomy and Astrophysics - Neutrino Unbound - INFN Opens in a new window — https://www.nu.to.infn.it/Other_Astrophysics/
- eprints.soton.ac.uk Growing self consistent galaxies in empirically modelled environments using steel - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/447141/1/Philip_Grylls_UoS_Thesis_for_Award.pdf
- arts.units.it UNIVERSITÀ DEGLI STUDI DI TRIESTE - ArTS Opens in a new window — https://arts.units.it/retrieve/03474fc1-3079-44d5-ac95-69957b6c0c57/Tesi_definitiva_AliceDamiano.pdf
- researchgate.net The Multi-Scale Multi-Phase Circumgalactic Medium: Observed and Simulated Opens in a new window — https://www.researchgate.net/publication/385750533_The_Multi-Scale_Multi-Phase_Circumgalactic_Medium_Observed_and_Simulated
- orcid.org Axel Weiss - ORCID Opens in a new window — https://orcid.org/0000-0003-4678-3939
- arxiv.org Disk-Star Alignment I: Pre-Main-Sequence Stellar Parameters and the Statistical Alignment Between Disks and Stellar Rotation - arXiv Opens in a new window — https://arxiv.org/html/2504.02990v1
- eso.org Magnetic field strengths of hot giant exoplanets consistent with Solar System values - ESO.org Opens in a new window — https://www.eso.org/public/archives/releases/sciencepapers/eso2606/eso2606a.pdf
- asj.or.jp ようやく切り拓かれた X線偏光天文学 - 日本天文学会 Opens in a new window — https://www.asj.or.jp/jp/activities/geppou/item/117_4all.pdf
- arxiv.org The Multi-Scale Multi-Phase Circumgalactic Medium: Observed and Simulated Lecture notes for the 52nd (March 2023) Saas-Fee Advanced School, Switzerland. - arXiv Opens in a new window — https://arxiv.org/html/2411.07988v1
- purehost.bath.ac.uk Saintonge, A, Catinella, B, Cortese, L, Genzel, R, Giovanelli, R, Haynes, MP - Alternative formats If you require this document in an alternative format, please contact: openaccess@bath.ac.uk - University of Bath Opens in a new window — https://purehost.bath.ac.uk/ws/files/148440037/Saintonge2016_arXiv.pdf
- academic.oup.com COLD GASS, an IRAM legacy survey of molecular gas in massive galaxies – I. Relations between H 2 , H i, stellar content and structural properties - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/415/1/32/988888
- academic.oup.com COLD GASS, an IRAM legacy survey of molecular gas in massive galaxies – I. Relations between H2, HI Opens in a new window — https://academic.oup.com/mnras/article-pdf/415/1/32/17328290/mnras0415-0032.pdf
- academic.oup.com COLD GASS, an IRAM legacy survey of molecular gas in massive galaxies – II. The non-universality of the molecular gas depletion time-scale - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/415/1/61/988902
- arxiv.org [1103.1642] COLD GASS, an IRAM legacy survey of molecular gas in massive galaxies: I. Relations between H2, HI, stellar content and structural properties - arXiv Opens in a new window — https://arxiv.org/abs/1103.1642
- scielo.org.mx The HI and H2-to-stellar mass correlations of late-and early-type galaxies and their consistency with the observational mass functions - SciELO México Opens in a new window — https://www.scielo.org.mx/scielo.php?pid=S0185-11012018000200443&script=sci_arttext_plus&tlng=en
- pure.ed.ac.uk xGASS: total cold gas scaling relations and molecular-to-atomic gas ratios of galaxies in the local Universe - Account Opens in a new window — https://www.pure.ed.ac.uk/ws/files/82473486/57675098Dave_1802.02373.pdf
- researchgate.net Tracing Quenching in Nearby Galaxies Through Inner Surface Mass Density and Cold Gas Content - ResearchGate Opens in a new window — https://www.researchgate.net/publication/397934523_Tracing_Quenching_in_Nearby_Galaxies_Through_Inner_Surface_Mass_Density_and_Cold_Gas_Content
- arxiv.org Estimating gas masses and dust-to-gas ratios from optical spectroscopy - arXiv Opens in a new window — https://arxiv.org/pdf/1304.3492
- arxiv.org arXiv:2406.04242v1 [astro-ph.GA] 6 Jun 2024 Opens in a new window — https://arxiv.org/pdf/2406.04242
- arxiv.org The Hidden Life of Stars: Embedded Beginnings to AGB Endings in the PHANGS-JWST Sample. I. Catalog of Mid-IR Sources - arXiv Opens in a new window — https://arxiv.org/html/2509.16459v1
- sophiastuber.de Publications and talks – Dr. Sophia Stuber Opens in a new window — https://sophiastuber.de/publications/
- arxiv.org Molecular Gas Morphological Analogues for the Milky Way - arXiv Opens in a new window — https://arxiv.org/pdf/2602.02789
- academic.oup.com Interacting galaxies in the IllustrisTNG simulations – VIII. Pericentric star formation rate enhancements are driven both by increased fuelling and efficiency - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/537/2/915/7973007
- arxiv.org The CO–to–H 2 conversion factor in the Milky Way's central parsec - arXiv Opens in a new window — https://arxiv.org/html/2511.16720v1
- academic.oup.com Effects of dust evolution on the abundances of CO and H2 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/467/1/699/10493717/stx118.pdf
- arxiv.org The CO-to-H$_2$ conversion factor in the Milky Way's central parsec - arXiv Opens in a new window — https://arxiv.org/pdf/2511.16720
- ioa.s.u-tokyo.ac.jp The CO-to-H2 Conversion Factor of the Galactic Giant Molecular Clouds using CO isotopologues: the high-resolution XCO maps Opens in a new window — https://www.ioa.s.u-tokyo.ac.jp/~sofue/news/2023-mn-FUGIN_X12CO13CO_paper-II.pdf
- academic.oup.com Predictions for CO emission and the CO-to-H 2 conversion factor in galaxy simulations with non-equilibrium chemistry - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/532/2/1948/7693730
- elthateng.github.io Molecular Gas Properties and CO-to-H2 Conversion Factors in the Central Kiloparsec of NGC 3351 Opens in a new window — https://elthateng.github.io/files/NGC_3351_Paper_accepted.pdf
- lss.fnal.gov A Comprehensive Characterization of Galaxy-cool CGM Connections at z<0.4 with DESI Year 1 Data FERMILAB-PUB-25-0906-PPD arXiv:2503.11139 Opens in a new window — https://lss.fnal.gov/archive/2025/pub/fermilab-pub-25-0906-ppd.pdf
- arxiv.org arXiv:2307.07078v2 [astro-ph.GA] 2 Aug 2023 Opens in a new window — https://arxiv.org/pdf/2307.07078
- edoc.ub.uni-muenchen.de The 3D view on cosmic baryon cycle Opens in a new window — https://edoc.ub.uni-muenchen.de/26557/1/Hamanowicz_Aleksandra.pdf
- eso.org MUSE-ALMA haloes VII: survey science goals \& design, data processing and final catalogues - ESO.org Opens in a new window — http://www.eso.org/~hkuntsch/papers/MNRAS_516_5618.pdf
- arxiv.org The Cosmic Evolution of CIV Absorbers at $1.4<z<4.5 - arXiv Opens in a new window — https://arxiv.org/pdf/2504.20299
- edoc.ub.uni-muenchen.de Cool and Cold Gas within and surrounding Galaxies - Elektronische Hochschulschriften der LMU München Opens in a new window — https://edoc.ub.uni-muenchen.de/31456/1/Szakacs_Roland.pdf
- scholarlypublications.universiteitleiden.nl H I content at cosmic noon: a millimetre-wavelength perspective - Scholarly Publications Leiden University Opens in a new window — https://scholarlypublications.universiteitleiden.nl/access/item%3A4180055/download
- arxiv.org ALMACAL VI: Molecular gas mass density across cosmic time via a blind search for intervening molecular absorbers - arXiv Opens in a new window — https://arxiv.org/pdf/1909.08624
- academic.oup.com H i content at cosmic noon – a millimetre-wavelength perspective - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/533/4/3937/7722018
- researchgate.net Current COMAP constraint on ρ H2 (thick bar with downward arrow) in... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Current-COMAP-constraint-on-r-H2-thick-bar-with-downward-arrow-in-relation-to-past_fig3_361978977
- openaccess.inaf.it Atomic and molecular gas from the epoch of reionization down to redshift 2 - OA@INAF Opens in a new window — https://openaccess.inaf.it/bitstreams/5cc5b367-a3d0-4dd3-a824-55d35fc8236d/download
- academic.oup.com EMBERS I: low-redshift post-starburst galaxies are frequently depleted in molecular gas relative to star-forming progenitors - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/548/1/stag485/8514461
- researchgate.net xCOLD GASS: the complete IRAM-30m legacy survey of molecular gas for galaxy evolution studies - ResearchGate Opens in a new window — https://www.researchgate.net/publication/386634734_xCOLD_GASS_the_complete_IRAM-30m_legacy_survey_of_molecular_gas_for_galaxy_evolution_studies
- research.chalmers.se Vz-GAL: Probing Cold Molecular Gas in Dusty Star-forming Galaxies at z=1-6 - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/550467/file/550467_Fulltext.pdf
- academic.oup.com WALLABY pilot survey: H i depletion times within the stellar discs of nearby galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/548/3/stag660/8644293
- arxiv.org 1 Introduction Opens in a new window — https://arxiv.org/html/2602.21500v1
- scispace.com Molecular gas contents and scaling relations for massive ... - SciSpace Opens in a new window — https://scispace.com/pdf/molecular-gas-contents-and-scaling-relations-for-massive-58imyhjwmb.pdf
- edoc.ub.uni-muenchen.de Galaxy Kinematics during the Peak Epoch of Cosmic Star Formation Opens in a new window — https://edoc.ub.uni-muenchen.de/24712/1/Uebler_Hannah_D_N.pdf
- purehost.bath.ac.uk Alternative formats If you require this document in an alternative format, please contact: openaccess@bath.ac.uk Opens in a new window — https://purehost.bath.ac.uk/ws/files/167885572/Tacconi2018_arXiv.pdf
- profiles.arizona.edu Benjamin J Weiner | UA Profiles - The University of Arizona Opens in a new window — https://profiles.arizona.edu/person/bjweiner
- boa.unimib.it Massive Black Holes in Galactic Nuclei - Milano-Bicocca Opens in a new window — https://www.boa.unimib.it/retrieve/3b588d80-b3ed-481b-b3c1-b7dea9f62ce5/Izquierdo-Villalba-2024-Black%20Holes-preprint.pdf
- researchgate.net The Evolution of the Baryons Associated with Galaxies Averaged over Cosmic Time and Space - ResearchGate Opens in a new window — https://www.researchgate.net/publication/346309820_The_Evolution_of_the_Baryons_Associated_with_Galaxies_Averaged_over_Cosmic_Time_and_Space
- osti.gov F er mil a b - OSTI Opens in a new window — https://www.osti.gov/servlets/purl/3021878
- arxiv.org 1 A Foreword by the Curators of this Community Paper - arXiv Opens in a new window — https://arxiv.org/html/2311.10056v2
- lss.fnal.gov F er mil a b Opens in a new window — https://lss.fnal.gov/archive/2026/pub/fermilab-pub-26-0139-v.pdf
- eso.org ESO Staff Publications (2020) Opens in a new window — https://www.eso.org/sci/libraries/telbib_info/AR/ESOStaffPapers2020.pdf
- arxiv.org [0810.2541] The Star Formation Law in Nearby Galaxies on Sub-Kpc Scales - arXiv Opens in a new window — https://arxiv.org/abs/0810.2541
- ned.ipac.caltech.edu Outskirts of Distant Galaxies In Absorption - Hsiao-Wen Chen Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Chen/Chen_refs.html
- sfb1601.astro.uni-koeln.de Project B3 - SFB 1601 Opens in a new window — https://sfb1601.astro.uni-koeln.de/projects/projectb/b3/
- arxiv.org Molecular Gas in the Outskirts - arXiv Opens in a new window — https://arxiv.org/pdf/1612.05275
- preprints.org Star Formation Efficiency and Class I Protostellar Timescales in ATLASGAL Dense Clumps Opens in a new window — https://www.preprints.org/manuscript/202606.1571
- academic.oup.com NEATH – V. The relationship between line emission from dense gas tracers and the star formation rate - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/547/4/stag527/8526388
- arxiv.org Spatially Resolved Molecular Gas Properties of Host Galaxy of Type I Superluminous Supernova SN 2017egm - arXiv Opens in a new window — https://arxiv.org/pdf/2005.06656
- arxiv.org arXiv:2303.05574v2 [astro-ph.GA] 13 Mar 2023 Opens in a new window — https://arxiv.org/pdf/2303.05574
- mpia.de The Evolution of the Baryons Associated with Galaxies Averaged over Cosmic Time and Space Opens in a new window — https://www.mpia.de/5504464/walter_aspecs_2020.pdf
- research.rug.nl Variations in the Star Formation Efficiency of the Dense Molecular Gas across the Disks of Star-forming Galaxies - the University of Groningen research portal Opens in a new window — https://research.rug.nl/files/84971136/Variations_in_the_Star_Formation_Efficiency_of_the_Dense_Molecular_Gas_across_the_Disks.pdf
- arxiv.org arXiv:2310.16037v2 [astro-ph.GA] 24 Nov 2023 Opens in a new window — https://arxiv.org/pdf/2310.16037
- research.chalmers.se Resolving the ISM at the Peak of Cosmic Star Formation with ALMA: The Distribution of CO and Dust Continuum in z ∼2.5 Submillimeter Galaxies Opens in a new window — https://research.chalmers.se/publication/504598/file/504598_Fulltext.pdf
- oar.princeton.edu ALMA REVEALS THE MOLECULAR MEDIUM FUELING THE NEAREST NUCLEAR STARBURST Opens in a new window — https://oar.princeton.edu/bitstream/88435/pr10c4sj8q/1/Leroy_2015_ApJ_801_25.pdf
- ned.ipac.caltech.edu arXiv:1310.4932v1 [astro-ph.CO] 18 Oct 2013 Opens in a new window — http://ned.ipac.caltech.edu/level5/Sept13/Recchi/paper.pdf
- orbit.dtu.dk Gas excitation of post-SB galaxies at 0.6 < z < 1.3 - DTU Research Database Opens in a new window — https://orbit.dtu.dk/files/441907811/2511.08829v2.pdf
- researchgate.net An ALMA view of star formation efficiency suppression in early-type galaxies after gas-rich minor mergers - ResearchGate Opens in a new window — https://www.researchgate.net/publication/386676487_An_ALMA_view_of_star_formation_efficiency_suppression_in_early-type_galaxies_after_gas-rich_minor_mergers
- arxiv.org Galaxy quenching across the Cosmic Web: disentangling mass and environment with SDSS DR18 - arXiv Opens in a new window — https://arxiv.org/html/2507.18614v2
- arxiv.org Measurement of the gas consumption history of a massive quiescent galaxy - arXiv Opens in a new window — https://arxiv.org/html/2405.19401v2
- arxiv.org arXiv:2206.07763v2 [astro-ph.GA] 27 Jul 2022 Opens in a new window — https://arxiv.org/pdf/2206.07763
- arxiv.org arXiv:1908.04306v1 [astro-ph.GA] 12 Aug 2019 Opens in a new window — https://arxiv.org/pdf/1908.04306
- radio.kasi.re.kr Possibility of Using 3.3 μm Polycyclic Aromatic Hydrocarbon Luminosity as a Molecular Gas Mass Estimator - Radio Opens in a new window — https://radio.kasi.re.kr/files/02%20%EB%B0%B1%EC%A4%80%ED%98%84_Shim_2025_ApJ_985_107.pdf
- arxiv.org Estimating the baryonic masses of face-on spiral galaxies from stellar kinematics - arXiv Opens in a new window — https://arxiv.org/pdf/1704.05243
- par.nsf.gov Modelling Stochastic Star Formation History of Dwarf Galaxies in GRUMPY Opens in a new window — https://par.nsf.gov/servlets/purl/10561236
- ntrs.nasa.gov HERSCHEL-ATLAS: A BINARY HyLIRG PINPOINTING A CLUSTER OF STARBURSTING PROTOELLIPTICALS Opens in a new window — https://ntrs.nasa.gov/api/citations/20140008911/downloads/20140008911.pdf
- arxiv.org The kinematics of massive high-redshift dusty star-forming galaxies - arXiv Opens in a new window — https://arxiv.org/html/2312.08959v1
- arxiv.org arXiv:2407.11125v3 [astro-ph.GA] 10 Dec 2024 Opens in a new window — https://arxiv.org/pdf/2407.11125
- academic.oup.com Cloud properties and star formation in M31 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/546/1/staf2283/8407243
- ioa.s.u-tokyo.ac.jp FOREST Unbiased Galactic plane Imaging survey with the Nobeyama 45 m telescope (FUGIN). VI. Dense gas and mini-starbursts in the W43 giant molecular cloud complex - Institute of Astronomy Opens in a new window — https://www.ioa.s.u-tokyo.ac.jp/~sofue/news/2020-pasj-FUGIN-VI-kohno+W43-GMC.pdf
- arxiv.org arXiv:2208.01663v1 [astro-ph.GA] 2 Aug 2022 Opens in a new window — https://arxiv.org/pdf/2208.01663
- arxiv.org Constraining the Molecular Kennicutt-Schmidt Relation with Multi-Transition CO Observations of Nearby Galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/2604.09353
- arxiv.org arXiv:2304.09832v2 [astro-ph.GA] 26 Feb 2024 Opens in a new window — https://arxiv.org/pdf/2304.09832
- arxiv.org arXiv:1906.07458v2 [astro-ph.GA] 17 Jul 2019 Opens in a new window — https://arxiv.org/pdf/1906.07458
- arxiv.org arXiv:2311.00025v1 [astro-ph.GA] 31 Oct 2023 Opens in a new window — https://arxiv.org/pdf/2311.00025
- arxiv.org arXiv:2012.09447v1 [astro-ph.GA] 17 Dec 2020 Opens in a new window — https://arxiv.org/pdf/2012.09447
- scispace.com arXiv:2404.12482v1 [astro-ph.GA] 18 Apr 2024 - SciSpace Opens in a new window — https://scispace.com/pdf/probing-the-relationship-between-early-star-formation-and-co-4kryfvrzer.pdf
- arxiv.org arXiv:2308.11717v2 [astro-ph.GA] 30 Oct 2023 Opens in a new window — https://arxiv.org/pdf/2308.11717
- researchgate.net The ALMaQUEST Survey: III. Scatter in the resolved star forming Opens in a new window — https://www.researchgate.net/publication/337590114_The_ALMaQUEST_Survey_III_Scatter_in_the_resolved_star_forming_main_sequence_is_primarily_due_to_variations_in_star_formation_efficiency
- arxiv.org The high molecular gas content, and the efficient conversion of Opens in a new window — https://arxiv.org/pdf/2006.13612
- arxiv.org arXiv:2302.12267v1 [astro-ph.GA] 23 Feb 2023 Opens in a new window — https://arxiv.org/pdf/2302.12267
- sites.astro.caltech.edu Low Mass Stars as Tracers of Star and Cluster Formation - Caltech Astronomy Opens in a new window — https://sites.astro.caltech.edu/~lah/review/lowmassstarformation_Megeath_2022PASP.pdf
- arxiv.org arXiv:2312.01854v1 [astro-ph.GA] 4 Dec 2023 Opens in a new window — https://arxiv.org/pdf/2312.01854
- kups.ub.uni-koeln.de Morphology, fragmentation, and dynamic balance: an investigation into early stages of structure formation in molecular clouds - Universität zu Köln Opens in a new window — https://kups.ub.uni-koeln.de/63885/1/Dissertation_Shashwata.pdf
- researchgate.net Structure and Fragmentation Scale of a Massive Star-forming Filament in NGC 6334: High-resolution Mid-infrared Absorption Imaging with JWST - ResearchGate Opens in a new window — https://www.researchgate.net/publication/391612991_Structure_and_Fragmentation_Scale_of_a_Massive_Star-forming_Filament_in_NGC_6334_High-resolution_Mid-infrared_Absorption_Imaging_with_JWST
- archiv.ub.uni-heidelberg.de Dissertation in Astronomy Opens in a new window — https://archiv.ub.uni-heidelberg.de/volltextserver/23788/1/thesis_jimenezdonaire.pdf
- ndl.ethernet.edu.et Cosmic Rays in Star-Forming Environments Opens in a new window — https://www.ndl.ethernet.edu.et/bitstream/123456789/68331/1/56.pdf
- arxiv.org arXiv:2502.02497v1 [astro-ph.GA] 4 Feb 2025 Opens in a new window — https://arxiv.org/pdf/2502.02497
- arxiv.org arXiv:1706.03005v2 [astro-ph.GA] 31 Aug 2017 Opens in a new window — https://arxiv.org/pdf/1706.03005
- arxiv.org Clumpy, dense gas in the outflow of NGC 1266 - arXiv Opens in a new window — https://arxiv.org/pdf/2512.09889
- arxiv.org arXiv:1210.7723v1 [astro-ph.GA] 29 Oct 2012 Opens in a new window — https://arxiv.org/pdf/1210.7723
- arxiv.org arXiv:2305.13436v2 [astro-ph.GA] 26 May 2023 Opens in a new window — https://arxiv.org/pdf/2305.13436
- arxiv.org The MALATANG survey: star formation, dense gas, and AGN feedback in NGC 1068 - arXiv Opens in a new window — https://arxiv.org/pdf/2512.04891
- pure.ed.ac.uk Evolution of Interstellar Medium, Star Formation, and Accretion at High Redshift - Account Opens in a new window — https://www.pure.ed.ac.uk/ws/files/75485287/1702.04729.pdf
- backend.orbit.dtu.dk Tracing the Life Cycle of Galaxies across Cosmic Time A Story of Life and Death - DTU Inside Opens in a new window — https://backend.orbit.dtu.dk/ws/portalfiles/portal/413151947/PhD_Thesis.pdf
- arxiv.org arXiv:2211.01526v1 [astro-ph.GA] 3 Nov 2022 Opens in a new window — https://arxiv.org/pdf/2211.01526
- oro.open.ac.uk ORIGINAL UNEDITED MANUSCRIPT - Open Research Online Opens in a new window — https://oro.open.ac.uk/81226/1/81226AAM.pdf
- research.chalmers.se Average dust, gas, and star-formation properties of cluster and field galaxies from stacking analysis - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/538121/file/538121_Fulltext.pdf
- cambridge.org Probing the resolved K-S relation in nearby galaxies: Insights from UVIT and ALMA observations - Cambridge University Press & Assessment Opens in a new window — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5A14AE2FF9ECAD9C73713CB219F7A816/S132335802510088Xa.pdf/probing-the-resolved-k-s-relation-in-nearby-galaxies-insights-from-uvit-and-alma-observations.pdf
- academic.oup.com What controls star formation in the central 500 pc of the Galaxy? - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/440/4/3370/1113695
- researchgate.net (PDF) The Molecular Cloud Lifecycle - ResearchGate Opens in a new window — https://www.researchgate.net/publication/340981145_The_Molecular_Cloud_Lifecycle
- academic.oup.com Deriving a multivariate αCO conversion function using the [C ii]/CO (1−0) ratio and its application to molecular gas scaling relations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/470/4/4750/3883753
- arxiv.org Star formation across cosmic time - arXiv Opens in a new window — https://arxiv.org/html/2405.20803v1
- researchgate.net The EDGE-CALIFA Survey: An integral field unit-based integrated molecular gas database for galaxy evolution studies in the Local Universe - ResearchGate Opens in a new window — https://www.researchgate.net/publication/393905048_The_EDGE-CALIFA_Survey_An_integral_field_unit-based_integrated_molecular_gas_database_for_galaxy_evolution_studies_in_the_Local_Universe
- orcid.org Linda Tacconi - ORCID Opens in a new window — https://orcid.org/0000-0002-1485-9401
- arxiv.org GA-NIFS: A smouldering disk galaxy undergoing ordered rotation at z=4.26 - arXiv Opens in a new window — https://arxiv.org/pdf/2512.05213
- par.nsf.gov The ALPINE−ALMA [CII] Survey: On the nature of an extremely obscured serendipitous galaxy Opens in a new window — https://par.nsf.gov/servlets/purl/10164479
- arxiv.org The Galaxy End Sequence - arXiv Opens in a new window — https://arxiv.org/pdf/1611.00367
- sami-survey.org The KMOS Redshift One Spectroscopic Survey (KROSS): the origin of disk turbulence in ζ ≈ 1 star-forming galaxies Opens in a new window — https://sami-survey.org/system/files/papers/701/kross_dispersions_accepted.pdf
- arxiv.org ALMA reveals starburst-like interstellar medium conditions in a compact star-forming galaxy at z ∼ 2 using [CI] and CO - arXiv Opens in a new window — https://arxiv.org/pdf/1703.05764
- scispace.com arXiv:2404.14503v1 [astro-ph.GA] 22 Apr 2024 - SciSpace Opens in a new window — https://scispace.com/pdf/the-co-to-h-2-conversion-factor-in-the-barred-spiral-galaxy-3rsxl0eslx.pdf
- arxiv.org [1212.1208] The CO-to-H2 Conversion Factor and Dust-to-Gas Ratio on Kiloparsec Scales in Nearby Galaxies - arXiv Opens in a new window — https://arxiv.org/abs/1212.1208
- arxiv.org The Weak Carbon Monoxide Emission In An Extremely Metal Poor Opens in a new window — https://arxiv.org/pdf/1504.01453
- arxiv.org The Metallicity Dependence of PAH Emission in Galaxies I: Insights from Deep Radial Spitzer Spectroscopy - arXiv Opens in a new window — https://arxiv.org/html/2405.09685v1
- arxiv.org The EDGE-CALIFA Survey: Central molecular gas depletion in AGN host galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/2105.02916
- arxiv.org Resolved Profiles of Stellar Mass, Star Formation Rate, and Predicted CO-to-H$_2$ Conversion Factor Across Thousands of Local Ga - arXiv Opens in a new window — https://arxiv.org/pdf/2510.05214
- arxiv.org arXiv:2501.01289v1 [astro-ph.GA] 2 Jan 2025 Opens in a new window — https://arxiv.org/pdf/2501.01289
- arxiv.org arXiv:2302.07808v1 [astro-ph.GA] 15 Feb 2023 Opens in a new window — https://arxiv.org/pdf/2302.07808
- arxiv.org Gas Fraction and Depletion Time Drive the Main-Sequence Scatter in Massive Galaxies at z∼1.5 - arXiv Opens in a new window — https://arxiv.org/html/2605.23662v1
- arxiv.org The impact of gas accretion and AGN feedback on the scatter of the mass-metallicity relation - arXiv Opens in a new window — https://arxiv.org/pdf/2212.10657
- indico.dfa.unipd.it arXiv:2309.05937v1 [astro-ph.GA] 12 Sep 2023 - DFA Indico Opens in a new window — https://indico.dfa.unipd.it/event/913/attachments/1059/2121/2309.05937.pdf
- academic.oup.com The atomic gas sequence and mass–metallicity relation from dwarfs to massive galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/535/3/2341/7881573
- arxiv.org arXiv:2306.16441v1 [astro-ph.GA] 28 Jun 2023 Opens in a new window — https://arxiv.org/pdf/2306.16441
- arxiv.org arXiv:2502.14031v2 [astro-ph.GA] 1 May 2025 Opens in a new window — https://arxiv.org/pdf/2502.14031
- arxiv.org The VANDELS survey: the stellar metallicities of star-forming galaxies at 2.5 < z < 5.0 - arXiv Opens in a new window — https://arxiv.org/pdf/1903.11081
- arxiv.org Stardust Galaxies at z¿9: A Dust-Origin Transition Behind the Excess of UV-Bright Galaxies Opens in a new window — https://arxiv.org/html/2605.09829v1
- academic.oup.com On the dust temperatures of high-redshift galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/489/1/1397/5543226
- arxiv.org COSMOS-Web: Star formation along the early Hubble sequence and the evolution of dust over the redshift range 0<z<12 - arXiv Opens in a new window — https://arxiv.org/pdf/2605.19661

## Custody and safety receipt

- Raw source discovery only; independent composite identifier and claim-boundary verification remains required before live wiki mutation.
- No DB, wiki, trust-score, claim/evidence, code, deploy, git, publish, cron, billing, credential, account-setting, or unrelated-conversation mutation was performed.
- No conversation deletion was authorized or performed.

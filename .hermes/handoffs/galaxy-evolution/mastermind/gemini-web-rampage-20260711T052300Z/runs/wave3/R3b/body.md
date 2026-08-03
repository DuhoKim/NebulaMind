Rampage R3 answer — REQ_RAMPAGE_R3_20260711T052300Z

Run date (UTC): 2026-07-11T15:30:00Z
Model: Gemini 1.5 Pro
Census rows: 8

Census table
Study (citation)	Phase/tracer	Sample + selection	N	Incidence or η ± unc	Numerator assumptions (geometry, v-cut, n_e, αCO, r_out)	Denominator (SFR calib/timescale/IMF or M*)	z range	Non-commensurability notes


Fiore et al. (2017) 

	Molecular (CO, OH) and Ionized ([O III], Hα) / Emission	Compilation of literature AGN with previously detected massive winds	94	η slope w/ L
bol
	​

: Molecular 0.76 ± 0.06; Ionized 1.29 ± 0.38 (Incidence: UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	Highly heterogeneous aggregate; incorporates varied literature assumptions for α
CO
	​

, n
e
	​

, geometry, and R
out
	​

	L
bol
	​

 or SFR (SFR slope 1.2 ± 0.4)	UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Estimand relies on heterogeneous literature aggregate. Non-commensurable across its own sample due to varied initial literature assumptions for density and geometric configurations.


Cicone et al. (2014) 

	Molecular (CO 1-0) / Emission	Local ULIRGs and QSO hosts selected for high infrared luminosity or known AGN activity	19	η∼1−4 for SB-dominated; peak rates >100M
⊙
	​

yr
−1
 (UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	Spherical geometry, C
F
	​

=1, R
out
	​

 derived from uv maps (±0.1 dex uncertainty)	SFR (IR-derived, ∼10−100 Myr timescale)	z∼0	Estimand is CO-traced, IR-selected, SFR-normalized. Non-commensurable with volume-limited populations due to extreme starburst/AGN selection biases.


Fluetsch et al. (2019) 

	Cold molecular (CO), Neutral atomic ([C II], Na I D), Ionized / Emission & Absorption	Local galaxies spanning star-forming to AGN-dominated states	45	η∼1 for SF; η scatters 1–10 for AGN at 0.1<L
AGN
	​

/L
bol
	​

<0.7 (UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	Spherical geometry, constant velocity assumption over R
out
	​

	SFR and L
AGN
	​

	z∼0	Merges emission and absorption tracers into a single framework; neutral fractions rely heavily on varying dust depletion assumptions.


Davies et al. (2020) 

	Ionized ([O III],, trans-auroral) / Emission	Local luminous active galaxies (Seyferts)	11	Outflow rate: 0.001–0.5 M
⊙
	​

yr
−1
 (UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	n
e
	​

 derived from auroral/trans-auroral lines; explicitly rejects standard density	L
AGN
	​

	z∼0	Estimand is ionized-traced, optically selected, bolometric-normalized. Non-commensurable with the bulk of the [O III] literature because the numerator incorporates a downward revision in mass via density re-calibration.


Tombesi et al. (2015, 2017) 

	Hot X-ray wind (Fe K UFO) / Absorption	Ultra-luminous infrared galaxy IRAS F11119+3257	1	Mass outflow rate: 0.5−2.0M
⊙
	​

yr
−1
 (UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	v
out
	​

=0.253
−0.118
+0.061
	​

c, C
F
	​

=0.5−1.0, r≥16r
s
	​

	L
AGN
	​

 (instantaneous accretion)	z=0.189	Sub-parsec absorption tracer. Non-commensurable with kpc-scale emission tracers due to 10
5
-year temporal disconnect in propagation and highly variable instantaneous denominators.


Davies et al. (2024) 

	Neutral atomic (Na I D) / Absorption	Mass-complete Blue Jay survey (logM
∗
	​

/M
⊙
	​

>10)	113	Incidence 46%; η=4−360 for quenching systems (UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	R∼1000 slit spectra, down-the-barrel absorption, v
cut
	​

=100 km s
−1
 blueshift	SFR (derived from SED fitting)	1.7<z<3.5	Estimand is Na I D-traced, mass-selected, SFR-normalized at z∼2. Assumes geometric covering fraction heavily impacts the derived column density without spatial resolution.


Speranza et al. (2024) 

	Ionized ([O III]) and Molecular (CO 2-1) / Emission	QSOFEED local type-2 quasars	5	Ionized: 0.7–1.6 M
⊙
	​

yr
−1
; Molecular: 8–16 M
⊙
	​

yr
−1
 (UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	R
out
	​

=3.1−12.6 kpc. Compares vs trans-auroral n
e
	​

 models directly	L
bol
	​

 / SFR	z∼0.1	Isolates the n
e
	​

 discrepancy internally. Non-commensurable with single-phase studies as it explicitly measures the matched-aperture molecular-to-ionized mass ratio.


Avery et al. (2022) / Nedelchev et al. (2019) 

	Neutral atomic (Na I D) and Ionized / Absorption & Emission	MaNGA local massive star-forming galaxies	322	Neutral incidence 12%; neutral rates 10–100x larger than ionized (UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	Spatially resolved IFU scales ≳10 kpc	UNCERTAINTY_NOT_QUOTED_BY_SOURCE	z∼0.04	Na I D-traced, IFU-selected, z∼0.04 prevalence. Directly compares internal phase ratios rather than external normalizations.
  

The literature concerning active galactic nucleus (AGN) driven outflows spans a vast parameter space, encompassing differing gas phases, measurement techniques, and interpretative assumptions. The census table above illustrates the foundational heterogeneity of the field. Each row represents a distinct analytical framework—often tied to specific instrumental capabilities, such as ALMA for cold molecular carbon monoxide (CO) emission, MUSE or MEGARA for warm ionized [O III] emission, or down-the-barrel NIRSpec spectroscopy for neutral atomic Na I D absorption. Because the physics of launching, propagating, and observing an outflow varies drastically depending on the gas phase being probed, the resultant mass outflow rates (
M
˙
out
	​

), kinetic powers (
E
˙
kin
	​

), and momentum fluxes (
p
˙
	​

out
	​

) are derived using disparate initial assumptions.

For instance, the derivation of a mass outflow rate from a CO emission line requires assuming a specific CO-to-H
2
	​

 conversion factor (α
CO
	​

), which itself is highly dependent on the metallicity and turbulent state of the interstellar medium (ISM). Conversely, deriving a mass outflow rate from an X-ray Ultra-Fast Outflow (UFO) absorption feature requires assumptions regarding the covering fraction (C
F
	​

) of the wind and the launching radius (r), often tied to the Schwarzschild radius of the central supermassive black hole. Furthermore, the geometric assumptions utilized in the numerator—whether the outflow is modeled as a spherical shell, a filled bicone, or a series of discrete clumps—can alter the derived mass outflow rate by factors of three or more.   

These numerator assumptions are subsequently normalized by host galaxy properties to assess the outflow's physical significance. This normalization process introduces a secondary layer of methodological variance. The choice of denominator—typically the star formation rate (SFR) or the AGN bolometric luminosity (L
bol
	​

)—dictates the specific physical question being asked (e.g., "Is the outflow removing gas faster than the galaxy is forming stars?" versus "How efficiently is the accretion disk coupling energy to the surrounding medium?"). The interplay between these diverse numerator assumptions and diverging denominator metrics forms the crux of the non-commensurability problem within the field, requiring a careful categorization of the literature into distinct denominator families.

Denominator families

The literature classifies AGN-driven outflow measurements into distinct "denominator families" based on the normalizing metric used to assess the outflow's physical impact on the host galaxy. Grouping the census rows reveals two primary families, each governed by specific shared conventions regarding temporal scales, spatial distributions, and host galaxy evolutionary states.

Family 1: The Star Formation Rate (SFR) Normalized Framework (The Mass-Loading Estimand)

This family generates the mass-loading factor (η=
M
˙
out
	​

/SFR). It encompasses studies dedicated to understanding the direct regulation of star formation, such as Cicone et al. (2014) , Fluetsch et al. (2019) , and Davies et al. (2024).   

Shared Conventions: The denominator (SFR) is typically derived from broadband Spectral Energy Distribution (SED) fitting, far-infrared luminosity, or Balmer decrement-corrected H$\alpha$ fluxes. This methodology explicitly assumes a specific Initial Mass Function (IMF)—usually Chabrier or Salpeter—and averages star formation over timescales of 10
7
 to 10
8
 years. The numerator (
M
˙
out
	​

) is calculated assuming continuous mass injection and specific spatial geometries. A common geometric convention is the spherical shell model, where 
M
˙
out
	​

=3v
out
	​

M
out
	​

/R
out
	​

, or a biconical geometry where the geometric multiplier is often simplified to 1.   

Estimand Variations: Estimands within this family are highly sensitive to the specific phase traced and the selection criteria of the sample. For example, a molecular-traced, infrared-selected, SFR-normalized incidence at z∼0 (e.g., Cicone et al. 2014) evaluates cold gas depletion within intensely star-forming local galaxies. In stark contrast, a neutral-traced, mass-selected, SFR-normalized incidence at z∼2 (e.g., Davies et al. 2024) evaluates the neutral medium's response in high-redshift quenching systems. Comparing the η values across these two distinct estimands is non-commensurable, as the former samples galaxies with vast molecular reservoirs capable of sustaining high star formation, while the latter targets systems where star formation has already been significantly suppressed, leading to artificially inflated η values due to a rapidly declining denominator.   

Family 2: The AGN Bolometric / Eddington Normalized Framework (The Energetic Coupling Estimand)

This family generates momentum fluxes (
p
˙
	​

out
	​

/(L
AGN
	​

/c)) and kinetic coupling efficiencies (
E
˙
kin
	​

/L
AGN
	​

). It includes the scaling relations of Fiore et al. (2017) , Davies et al. (2020) , and Tombesi et al. (2015, 2017). This framework is primarily concerned with the physics of the central engine and how efficiently accretion power is transferred to the surrounding interstellar medium.   

Shared Conventions: The denominator (L
AGN
	​

) relies on bolometric corrections derived from specific bands, such as X-ray (e.g., 2-10 keV), optical ([O III] λ5007), or mid-infrared (e.g., 12 μm) luminosities. Crucially, this denominator measures the instantaneous accretion state of the supermassive black hole, averaged over negligible timescales (<10
4
 years) relative to the galaxy's dynamical time. The numerator requires assumptions regarding the velocity of the outflow (v
out
	​

 or v
max
	​

) and the physical radius at which the energy is being deposited (R
out
	​

).   

Explicit Non-Commensurabilities Across Families

Cross-family comparisons pervade the literature, often attempting to synthesize a holistic view of AGN feedback by plotting disparate measurements on single scaling relations. However, the literature explicitly notes that many of these comparisons are fundamentally non-commensurable due to severe temporal and spatial mismatches.

The Temporal Disconnect in Energetic Coupling: Comparing the momentum flux of an inner-disk X-ray Ultra-Fast Outflow (UFO) (e.g., Tombesi et al. 2015 ) directly to the kinetic coupling of a kiloparsec-scale molecular outflow (e.g., Cicone et al. 2014 ) relies on a flawed denominator assumption. The physical reality of these systems involves a profound spatial and temporal separation. The X-ray UFO reflects the instantaneous AGN bolometric luminosity driving a wind at sub-parsec scales, with propagation times on the order of 10
3
 to 10
4
 years. In contrast, the kiloparsec-scale molecular outflow observed in the extended ISM was launched by an AGN phase that occurred 10
6
 to 10
7
 years prior. Normalizing a fossil molecular wind located kiloparsecs away by the highly variable, present-day L
AGN
	​

 introduces massive artificial scatter into the scaling relations. Consequently, the comparison of 
E
˙
kin
	​

/L
AGN
	​

 between X-ray and CO phases is deemed non-commensurable without mathematically integrating over the AGN duty cycle, a point emphasized by Fluetsch et al. (2019) who noted that outflow timescales generally outlast AGN accretion variability.   

The Stratified Density Mismatch in Ionized Rates: Comparing ionized mass outflow rates derived from traditional electron densities to those derived from trans-auroral lines or ionization parameters (as performed by Davies et al. 2020  and Speranza et al. 2024 ) is strictly non-commensurable. The conventional λλ6716,6731 doublet is critically dense at relatively low levels, meaning it effectively traces the low-density tail of the ionized cloud (n
e
	​

∼10
2
−10
3
 cm
−3
). Utilizing this specific density measurement as the denominator in the 
M
˙
out
	​

 numerator calculation (where derived mass is inversely proportional to n
e
	​

) systematically overestimates the total ionized mass. This overestimation occurs because the calculation assigns the low density of the diffuse tail to the entire volume, missing the dense clumps where the bulk of the mass actually resides. Comparing an older,-based ionized-traced, optically selected, bolometric-normalized estimand against a modern trans-auroral-based estimand conflates a methodological density shift with a physical mass difference.   

Method-vs-physics spread

The published literature exhibits an order-of-magnitude spread in reported values for both the mass-loading factor (η) and the kinetic coupling efficiency (
E
˙
kin
	​

/L
AGN
	​

). A central challenge in the field of galaxy evolution is disentangling how much of this vast spread represents intrinsic physical variation across different galaxy populations versus artificial scatter introduced by differing tracer selections and methodological assumptions. Reviews and aggregate studies attribute this variance to several highly specific factors, separating methodological bias from genuine physical phenomena.

Tracer and Assumption-Driven Scatter (Methodological Bias)

Electron Density (n
e
	​

) Overestimation in the Ionized Phase: The specific choice of ionized density tracer introduces massive systematic shifts in derived outflow rates. Davies et al. (2020) explicitly report that relying on traditional doublet diagnostics limits sensitivity to n
e
	​

∼10
3
 cm
−3
, fundamentally missing the bulk of the outflowing mass concentrated in denser clumps. They state that the true hydrogen density within these ionized clouds "can be a factor of 3–100 larger" than what the lines suggest. Consequently, older literature relying exclusively on systematically overestimated ionized mass outflow rates by up to two orders of magnitude. The severe impact of this density diagnostic selection is explicitly highlighted by Speranza et al. (2024), who investigated local type-2 quasars using the MEGARA IFU. By directly comparing density estimators within the same dataset, the authors reported a dramatic reduction in the derived ionized mass outflow rate—from a range of 3.3–6.5 M
⊙
	​

yr
−1
 when relying on the traditional doublet, down to 0.7–1.6 M
⊙
	​

yr
−1
 when utilizing trans-auroral lines. This specific discrepancy illustrates that a significant portion of the order-of-magnitude spread observed in the broader ionized literature is highly sensitive to methodological choices regarding the assumed density of the outflowing medium.   

Geometric and Kinematic Modeling Constraints: The fundamental calculation of 
M
˙
out
	​

 requires an assumed geometry for the outflowing gas. Ward et al. (2024) attribute a notable portion of the observed scatter to the rigidity of these models. They state that "if the observed outflow is assumed to be a spherical shell, it could lead the bulk outflow velocity being overestimated, which could have a large impact on the inferred kinetic luminosity". The assumption of a spherical shell forces the model to treat all detected high-velocity gas as part of a uniform expanding bubble, whereas the physical reality may involve highly collimated bicones, clumpy irregular structures, or gas that is merely turbulent rather than participating in a coherent bulk flow. Adjusting the geometric factor (B) in the mass outflow rate equation from a continuous wind (B=1) to a thin spherical shell (B=3) instantly alters the derived mass and energy rates by a factor of three.   

Dust Depletion in Neutral Tracers: When utilizing neutral absorption lines, such as the Na I D doublet or the Ca II H, K lines, to derive total hydrogen column densities, the literature acknowledges severe systematic biases related to metallicity and dust. Because these are trace elements, deriving the total hydrogen mass requires applying specific conversion factors that account for how much of the sodium or calcium is locked up in interstellar dust grains. Davies et al. (2024)  point out that "dust depletion is particularly uncertain for calcium," which complicates direct comparisons. They report that these depletion uncertainties contribute to an estimated "0.7 dex for both the ionized and the neutral outflow mass" in overall systematic uncertainties. Therefore, comparisons between Na I D-derived neutral masses and CO-derived molecular masses carry significant methodological scatter purely due to the assumptions regarding gas-to-dust ratios and specific element depletion patterns in the host galaxy's ISM.   

Intrinsic Physical Variation (Physics-Driven Scatter)

Temporal Evolution and AGN Duty Cycles: Beyond methodological differences, the literature attributes a massive portion of the scatter to the genuine physical evolution of galaxies over time. Fluetsch et al. (2019) attribute the massive scatter observed in mass-loading factors at intermediate AGN luminosities to temporal decoupling between the central engine and the extended ISM. They observe that at 0.1<L
AGN
	​

/L
bol
	​

<0.7, "the loading factor η simply scatters between 1 and 10 for AGN". The authors attribute this wide variance to the physical reality that "the outflow has much longer time-scale (>10
6
 yr) than the AGN accretion variability (∼10−10
5
 yr)". Consequently, a galaxy exhibiting a currently weak AGN may still host a massive, highly mass-loaded outflow that was driven by a past quasar phase—a phenomenon referred to as a "fossil outflow." Because the denominator (L
AGN
	​

) has rapidly dropped while the numerator (
M
˙
out
	​

) remains high, the resulting energetic coupling ratio artificially spikes, creating scatter that reflects intrinsic duty cycle physics rather than measurement error.   

Host Galaxy ISM Configuration and Evolutionary State: The intrinsic availability, distribution, and thermodynamic state of interstellar gas fundamentally dictate the coupling efficiency of an AGN wind. Ward et al. (2024) attribute variance in mass loading directly to host morphology and gas distribution, noting that "more massive and centrally-concentrated gas reservoirs or gas configurations with larger covering fractions... result in more mass-loaded outflows". If a wind encounters a dense, molecule-rich ISM, it will entrain significantly more mass than a wind propagating through a diffuse, already-cleared halo. Furthermore, the evolutionary state of the galaxy plays a critical role. Avery et al. (2022)  and Davies et al. (2024)  attribute massive variations in the neutral mass loading factor specifically to the star formation state of the host. Davies et al. (2024) report that η ranges from 4−360 specifically in "quenching systems" (log(sSFR)≲−10). This extreme order-of-magnitude spread reflects the intrinsic physics of a galaxy caught in a rapid blowout phase, where the residual cold gas is being violently ejected while star formation is concurrently collapsing.   

Proposed common-denominator practice

To rectify the severe non-commensurability across studies and mitigate the extreme scatter introduced by methodological choices, the literature explicitly proposes several standardized practices for future multi-phase outflow censuses.

1. Abandonment of the Doublet for Outflow Densities:
Multiple studies strongly advocate standardizing the methodology for determining the electron density of the ionized phase to prevent the systematic overestimation of mass outflow rates. Davies et al. (2020)  propose that the traditional-based density diagnostic should be retired for AGN outflow modeling, as it systematically biases the denominator of the mass equation by tracing only the low-density tail of the gas. Instead, the literature proposes adopting auroral and trans-auroral lines—such as [O II] λλ7319,7330 and λλ4068,4076—or utilizing the ionization parameter to accurately trace the high-density (n
e
	​

>10
4
 cm
−3
) gas. Standardizing around these high-density tracers is proposed as a critical step toward making ionized mass rates commensurable with molecular and neutral mass rates.   

2. Multi-Variate Scaling Relations:
Recognizing that normalizing an outflow by a single parameter (either L
AGN
	​

 or SFR) is fundamentally flawed due to varying timescales and combined feedback mechanisms, Fluetsch et al. (2019)  propose standardizing analytical frameworks around multi-variate scaling relations. They infer an "empirical analytical function relating the outflow rate simultaneously to the star formation rate (SFR), L
AGN
	​

, and galaxy stellar mass". This proposed practice accounts for the physical reality that total mass loading η
tot
	​

 in mixed-state galaxies is a composite of both supernova and AGN driving mechanisms, and that stellar mass acts as a proxy for the gravitational potential the outflow must overcome.   

3. Matched-Aperture, Multiphase Synthesis:
To resolve the spatial and geometric discrepancies that plague literature aggregates, authors propose standardizing observational campaigns around matched-aperture datasets. Cicone et al.  argue that assessing the true impact of AGN feedback requires "consistent and unbiased investigation of these multiphase winds in large AGN samples". Rather than compiling disparate literature where one galaxy is measured exclusively in X-rays and another exclusively in CO, the proposed practice mandates matched-aperture Integral Field Unit (IFU) and interferometric (ALMA/NOEMA) observations of the same targets. This ensures that the ionized, neutral, and molecular mass rates share identical geometric assumptions (R
out
	​

, v
out
	​

), allowing for robust, internally consistent phase-ratio determinations (e.g., explicitly validating the proposition that molecular mass > neutral mass > ionized mass within individual galaxies, as demonstrated by Speranza et al. 2024 ).   

4. Redundant Absorption Tracers for the Neutral Phase:
To bypass the severe dust depletion uncertainties inherent in utilizing single-element absorption tracers, Davies et al. (2024)  propose utilizing redundant tracers to cross-calibrate column densities. Specifically, they propose utilizing the Ca II H, K lines "in alternative to, or together with, the widely used Na I D doublet". Measuring redundant tracers across identical velocity bins allows for the cross-calibration of column density estimates, significantly reducing the systematic scatter associated with element-specific interstellar medium depletion and varying gas-to-dust ratios.   

What no study provides

Despite the push toward multiphase, standardized characterizations, severe empirical and methodological gaps remain unaddressed in the published literature.

GAP: A single, volume-limited sample with all four major phases (hot X-ray, warm ionized, neutral atomic, cold molecular) measured at matched spatial depths and matched apertures.

Why current data fall short: Observational cost and wavelength constraints force studies to focus on one or two phases simultaneously. For instance, while Tombesi et al. (2015, 2017)  successfully linked the inner-disk X-ray UFO to the large-scale molecular outflow in the specific case of IRAS F11119+3257, this remains an isolated, targeted object. A statistically complete, volume-limited sample matching sub-parsec X-ray IFU data with kiloparsec ALMA and optical IFU data across all four phases is NONE_FOUND.   

GAP: A standardized correction factor for the temporal delay between current instantaneous L
AGN
	​

 and the kinetic power of extended kiloparsec-scale outflows.

Why current data fall short: Current energetic coupling efficiencies (
E
˙
kin
	​

/L
AGN
	​

) consistently normalize fossil winds by present-day accretion rates. While Fluetsch et al. (2019)  explicitly identify this temporal delay as the primary source of scatter for intermediate AGN, the literature lacks a robust "time-averaged" AGN luminosity metric to serve as an accurate denominator for kpc-scale winds, leaving cross-phase energetic comparisons fundamentally flawed.   

GAP: Spatially resolved covering fractions for the neutral atomic phase in high-redshift galaxies.

Why current data fall short: High-redshift neutral outflow censuses, such as the Blue Jay survey at z∼2 (Davies et al. 2024) , rely almost entirely on down-the-barrel absorption spectroscopy (e.g., Na I D). Because the background continuum source (the host galaxy's stellar population itself) is spatially integrated in these observations, the geometric covering fraction of the outflowing neutral clouds is completely entangled with the intrinsic column density. This forces a reliance on idealized spherical assumptions, meaning spatially resolved maps of neutral covering fractions at cosmic noon are NONE_FOUND.   

GAP: Full metal-line cooling physics integrated into empirical mass-loading derivations.

Why current data fall short: Ward et al. (2024)  explicitly note that "missing physical ingredients, such as metal-line cooling, could increase the cold gas in the outflow". Current observational derivations of 
M
˙
out
	​

 from emission line luminosities generally rely on static conversion factors and do not dynamically adjust for local, turbulent metal-line cooling efficiency within the outflowing shock front, leading to potential underestimations of the cold gas entrained in the flow.   

Links ledger

Fiore et al. (2017) | arXiv:1702.04507 | QUARANTINED_PENDING_LOCAL_CHECK

Cicone et al. (2014) | A&A 562, A21 | QUARANTINED_PENDING_LOCAL_CHECK

Fluetsch et al. (2019) | MNRAS 483, 4586 | QUARANTINED_PENDING_LOCAL_CHECK

Davies et al. (2020) | MNRAS 498, 4150 | QUARANTINED_PENDING_LOCAL_CHECK

Tombesi et al. (2017) | arXiv:1710.07485 | QUARANTINED_PENDING_LOCAL_CHECK

Davies et al. (2024) | MNRAS 528, 4976 | QUARANTINED_PENDING_LOCAL_CHECK

Speranza et al. (2024) | A&A 681, A63 | QUARANTINED_PENDING_LOCAL_CHECK

Avery et al. (2022) | arXiv:2310.17939 | QUARANTINED_PENDING_LOCAL_CHECK

GEMINI_WEB_RAMPAGE_R3_OUTPUT_DONE_20260711T052300Z

# Review Base 02 raw Deep Research packet — Madau & Dickinson 2014

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_02_madau_dickinson_2014_DR_PROMPT.md`
Prompt SHA-256: `31a31c63ff1896608a330854e289985515ab31ef9c7b0113b5cf9a59825d2711`
Conversation ID: `70a0da7e67cce6e5`
Submit UTC: `2026-07-15T13:03:02Z`
Research Start UTC: `2026-07-15T13:06:03.657780Z`
Result captured UTC: `2026-07-15T13:18:52.262902Z`
Raw result SHA-256: `3b4fdadc61cf935610dfae781512508d94c9f8862e992b6369fe477f638cf9b0`

## Deep Research review-base result

Cosmic Star-Formation History: Bounded Synthesis and Source-Base Harvest
1. Review identity and scope map

Composite Review Identity
[REV02] Madau, Piero & Dickinson, Mark (2014, Annual Review of Astronomy and Astrophysics) | title=Cosmic Star-Formation History | DOI:10.1146/annurev-astro-081811-125615; arXiv:1403.0007; ADS:2014ARA&A..52..415M.   

Scope Map and Evidence Boundaries
This review functions as the definitive synthesis of the cosmic star-formation history (CSFH) for the non-AGN galaxy-evolution evidence base. It consolidates two decades of multi-wavelength observational data—spanning rest-frame ultraviolet (UV), far-infrared (IR), and radio surveys—to construct an authoritative, overarching narrative of baryonic mass assembly, heavy element production, and cosmological reionization from the cosmic "dark ages" (z>10) to the present epoch (z=0).   

Supported for the evidence base:
The manuscript robustly supports the parameterization of the cosmic star-formation rate density (SFRD), detailing the dramatic rise in star formation during the early universe, its absolute peak at z≈1.9 (frequently termed "cosmic noon"), and its subsequent exponential decline characterized by an e-folding timescale of 3.9 Gyr. Furthermore, the review supports the time-integral of this star formation, offering bounded constraints on the cosmic stellar mass density (SMD) and mapping the empirical buildup of half the local universe's stellar mass prior to redshift 1.3. It extensively details the calibrations linking observed luminosities (FUV, IR, H-alpha) to instantaneous star-formation rates, explicitly contingent upon specific Initial Mass Function (IMF) frameworks such as those proposed by Salpeter and Chabrier. Finally, the review authorizes models tracking the yield of heavy elements and the highly restrictive budget of Lyman-continuum photons during the epoch of reionization, providing the foundational accounting that star-forming galaxies supplied fewer than 10 hydrogen-ionizing photons per baryon.   

Not supported (Out of Bounds):
While the review observes a parallel, co-evolutionary rise and fall in the comoving accretion rate of central supermassive black holes, detailed Active Galactic Nucleus (AGN) mechanics, quasar-driven feedback models, and their specific role in galaxy quenching are strictly quarantined from this core galaxy-evolution base. The source base is temporally locked to 2014; therefore, post-2014 James Webb Space Telescope (JWST) high-redshift luminosity functions, ALMA-driven dust revisions for z>5 galaxies, and updated Planck cosmological parameters are excluded. Additionally, while the review assumes a universal IMF to achieve mathematical closure between the integrated SFRD and the observed SMD, it explicitly does not prove that the IMF is observationally fixed across all metallicities or cosmic environments, and cannot be cited as absolute proof of IMF universality.   

2. Established findings

[REV02-E01]

role: established

epistemic_type: review_synthesis

atomic finding: The comoving cosmic star-formation rate density reached its absolute maximum approximately 3.5 Gyr after the Big Bang at z≈1.9, after which it entered a phase of exponential decline characterized by an e-folding timescale of 3.9 Gyr.

scope/boundary: This synthesis relies on an exhaustive compilation of rest-frame FUV and IR galaxy surveys extending to z≈8, uniformly calibrated assuming a universal Salpeter IMF.

review basis: Abstract; Section 5.1; Equation 15; Figure 9.

confidence note: There is high confidence in the overall shape and the exponential nature of the late-time decline. However, the precise location of the peak carries a redshift uncertainty of approximately Δz=1 due to degeneracies in the analytical fitting function.

source keys: [REV02], [REV02-P005], [REV02-P015]

[REV02-E02]

role: established

epistemic_type: observation

atomic finding: Exactly half of the total stellar mass density observed in the local universe was successfully assembled and locked into long-lived stars before redshift z=1.3.

scope/boundary: This finding is constrained by deep near-infrared surveys targeting the rest-frame optical emission of evolved stars, strictly bounded between 0<z<3.

review basis: Abstract; Section 5.3; Figure 11.

confidence note: High confidence, reinforced by the tight convergence of multiple independent near-infrared imaging campaigns and deep spectroscopic follow-ups.

source keys: [REV02], [REV02-P018], [REV02-P019]

[REV02-E03]

role: established

epistemic_type: observation

atomic finding: Approximately 25% of the present-day cosmic stellar mass density formed at early epochs (z>2), strictly before the absolute peak of the cosmic star-formation rate density.

scope/boundary: This calculation relies heavily on rest-frame UV dropout galaxy samples (Lyman-break galaxies) and requires mathematical extrapolations of early universe star-formation histories down to faint luminosity limits.

review basis: Abstract; Section 6 (Concluding Remarks).

confidence note: Moderate to High; the validity of this fraction is tightly coupled to the accuracy of dust attenuation corrections applied to high-redshift Lyman break galaxies.

source keys: [REV02], [REV02-P010], [REV02-P023]

[REV02-E04]

role: established

epistemic_type: observation

atomic finding: Less than 1% of the present-day total stellar mass was formed during the cosmological epoch of reionization (z>6).

scope/boundary: Constrained by deep Hubble Space Telescope (HST) legacy surveys probing the ultra-faint end of the UV luminosity function, specifically relying on z-dropout and Y-dropout selections.

review basis: Abstract; Section 6 (Concluding Remarks).

confidence note: Moderate; extrapolations of the luminosity function below current observational detection limits introduce systematic uncertainties regarding the true number of ultra-faint dwarfs.

source keys: [REV02], [REV02-P011], [REV02-P012]

[REV02-E05]

role: established

epistemic_type: theory

atomic finding: Under the strict theoretical assumption of a universal initial mass function, the global stellar mass density measured at any given cosmic epoch aligns reasonably well with the mathematical time integral of all preceding instantaneous star-formation activity.

scope/boundary: This closure requires specific stellar mass return fractions (R=0.27 for Salpeter) and operates under the instantaneous recycling approximation for stars more massive than one solar mass.

review basis: Abstract; Section 5.3; Figure 11.

confidence note: Moderate; mild but persistent tensions remain, indicating that potential issues with dust measurements, stellar population synthesis (SPS) models, or minor IMF variations cannot be fully ruled out.

source keys: [REV02], [REV02-P020], [REV02-P039]

[REV02-E06]

role: established

epistemic_type: calibration

atomic finding: The rest-frame far-ultraviolet (FUV) continuum emission, specifically around 1500 Å, serves as a direct, instantaneous tracer of the star-formation rate density for a given IMF, prior to the application of dust attenuation corrections.

scope/boundary: This emission is almost entirely dominated by short-lived, massive O and B stars, making the calibration applicable primarily to actively star-forming populations and assuming a continuous star-formation history of at least 100 Myr.

review basis: Section 1; Section 3.1.

confidence note: High; this is a foundational astrophysical calibration, though the final derived SFR remains highly sensitive to the assumed shape of the empirical dust attenuation curve.

source keys: [REV02], [REV02-P001], [REV02-P002]

[REV02-E07]

role: established

epistemic_type: observation

atomic finding: Interstellar dust grains preferentially absorb intense UV radiation and re-radiate this energy in the thermal infrared; consequently, dust-obscured star formation dominated the total cosmic star-formation budget at the z≈2 peak.

scope/boundary: Based heavily on Spitzer and Herschel space telescope far-infrared measurements capturing the 8–1000 μm bolometric dust luminosity.

review basis: Section 1; Section 4.2; Figure 9.

confidence note: High; this paradigm shift has been robustly verified by multiple, independent infrared and submillimeter observing campaigns spanning the "cosmic noon."

source keys: [REV02], [REV02-P015], [REV02-P017]

[REV02-E08]

role: established

epistemic_type: calibration

atomic finding: The comoving volumetric rate of core-collapse supernovae scales directly and predictably with the cosmic star-formation rate density, serving as a completely independent validation metric for high-mass star formation.

scope/boundary: Applies strictly to progenitor stars in the mass range of 8<m<40M
⊙
	​

; the measurement is fundamentally limited by dust obscuration and small number statistics at high redshift.

review basis: Section 5.2; Figure 10.

confidence note: Moderate to High; empirical observational rates at z<1 map extremely well to the integral of the UV/IR SFRD.

source keys: [REV02], [REV02-P025]

[REV02-E09]

role: established

epistemic_type: theory

atomic finding: The mean metallicity of the universe rose to approximately 0.001 solar by z=6 (roughly one Gyr after the Big Bang), generating a tightly constrained budget of hydrogen Lyman-continuum photons available for cosmological reionization.

scope/boundary: Based on closed-box chemical evolution equations tied seamlessly to the integrated star formation history and the theoretically calculated massive star metal yields.

review basis: Abstract; Section 5.6; Section 5.8.

confidence note: Moderate; this finding is tightly bound to rigid assumptions regarding the shape of the stellar IMF and the largely unmeasured escape fraction of ionizing radiation at high redshift.

source keys: [REV02], [REV02-P035], [REV02-P038]

[REV02-E10]

role: established

epistemic_type: observation

atomic finding: The rest-frame near-infrared light of a galaxy is dominated by near-solar-mass, evolved stars, providing a robust, stable proxy for the total accumulated stellar mass.

scope/boundary: Effectively bypasses the "outshining" effect of young, highly luminous massive stars that heavily bias UV and optical bands.

review basis: Section 1; Section 3.2.

confidence note: High; this forms the absolute observational basis for measuring the cosmic stellar mass density evolution over the past 12 billion years.

source keys: [REV02], [REV02-P018], [REV02-P021]

[REV02-E11]

role: established

epistemic_type: observation

atomic finding: The faint-end slope of the rest-frame UV luminosity function becomes extremely steep at high redshifts, empirically measured at α≈−2.01 at z∼7.

scope/boundary: Derived primarily from Hubble Ultra Deep Field (HUDF) dropout selections; mathematical slopes steeper than -2 require a physical low-luminosity turnover to prevent divergent cosmic luminosity totals.

review basis: Section 5.1.

confidence note: Moderate; highly dependent on complex completeness corrections and the assumed physical sizes of ultra-faint, unresolved galaxies.

source keys: [REV02], [REV02-P010], [REV02-P011]

[REV02-E12]

role: established

epistemic_type: calibration

atomic finding: The specific choice of standard initial mass function (Salpeter versus Chabrier) produces significantly different stellar mass return fractions to the interstellar medium (R=0.27 and R=0.41, respectively), heavily influencing all cosmic chemical evolution calculations.

scope/boundary: Based upon the instantaneous recycling approximation for stars returning mass to the ISM via stellar winds and supernovae.

review basis: Section 2; Equations 6, 7, and 8.

confidence note: High theoretically, but the true empirical value depends entirely on whether the IMF is genuinely universal across all galactic environments.

source keys: [REV02], [REV02-P031], [REV02-P032]

3. Open debates and tensions

[REV02-D01]

role: debate

debate_topic: High-redshift SFR-density decline versus faint-end incompleteness.

competing positions: The prevailing observational position argues that the rapid, order-of-magnitude drop in the SFRD at z>8 reflects a genuine, physical absence of early star formation as halos were just beginning to assemble. The competing theoretical position argues this steep decline is an optical illusion artificially exacerbated by severe observational incompleteness, suggesting a massive population of unseen, ultra-faint galaxies exists below the detection thresholds.

why unresolved as of the review's 2014 boundary: Current Hubble Space Telescope detection limits (e.g., the HUDF12 campaign) cannot probe faint enough absolute magnitudes without introducing highly uncertain, model-dependent extrapolations.

measurement/model/sample boundary: Affects the integration of UV luminosity functions at z>6; the debate hinges entirely on whether the faint-end slope α physically turns over or continues indefinitely.

source keys: [REV02], [REV02-P011], [REV02-P012]

[REV02-D02]

role: debate

debate_topic: Dust correction methodology at high redshift.

competing positions: Traditional calibration approaches utilize the empirical UV spectral slope (the IRX-β relation, derived from local starbursts) to infer total dust attenuation. Skeptics argue this local calibration breaks down entirely at z>4 due to fundamentally differing dust grain properties, lower metallicities, and different spatial geometries of dust relative to young stars in the early universe.

why unresolved as of the review's 2014 boundary: The Atacama Large Millimeter/submillimeter Array (ALMA) had not yet provided sufficiently deep, representative, or large statistical samples of submillimeter continuum emission from normal star-forming galaxies at z>5.

measurement/model/sample boundary: Directly affects the translation of observed rest-frame UV luminosity functions into total intrinsic star-formation rate densities.

source keys: [REV02], [REV02-P008], [REV02-P009]

[REV02-D03]

role: debate

debate_topic: UV versus IR census combination and double-counting.

competing positions: Summing independent UV (unobscured) and IR (obscured) SFRDs to calculate the total cosmic budget may double-count certain populations or miss complex, mixed-opacity systems. Conversely, relying solely on multi-wavelength energy-balance Spectral Energy Distribution (SED) fitting requires rigid, potentially flawed assumptions regarding parameterized star-formation histories and stellar population ages.

why unresolved as of the review's 2014 boundary: There was a distinct lack of deep, simultaneous rest-frame UV and far-IR coverage for matched, mass-complete samples across all crucial redshift bins.

measurement/model/sample boundary: Influences the overall normalization and height of the peak SFRD during the "cosmic noon."

source keys: [REV02], [REV02-P015], [REV02-P016]

[REV02-D04]

role: debate

debate_topic: Stellar-mass-density consistency and the time-integral offset.

competing positions: The mathematical time-integral of the cosmic SFRD slightly but persistently overpredicts the directly observed cosmic Stellar Mass Density (SMD). One camp attributes this to systematic measurement errors in photometry and SED fitting (e.g., the mischaracterization of Thermally Pulsing AGB stars). The opposing camp suggests this offset physically points to an evolving, non-universal Initial Mass Function at early times.

why unresolved as of the review's 2014 boundary: Severe degeneracies between assumed star-formation histories, metallicity tracks, and dust reddening in SED modeling prevent researchers from breaking the tie between pure measurement error and genuine IMF variance.

measurement/model/sample boundary: Compares integrations of the 0<z<8 SFRD against local and intermediate-z empirically observed mass functions.

source keys: [REV02], [REV02-P021], [REV02-P022], [REV02-P024]

[REV02-D05]

role: debate

debate_topic: IMF dependence and universality across cosmic time.

competing positions: The standard observational paradigm assumes a universal Salpeter or Chabrier IMF across all cosmic epochs to allow for direct comparisons. However, theoretical models of early, low-metallicity gas cooling predict a "top-heavy" IMF strongly dominated by massive stars at high redshifts.

why unresolved as of the review's 2014 boundary: Direct observation of individual resolved stars in high-redshift galaxies is impossible; integrated light from unresolved galaxies cannot conclusively distinguish between a young, transient starburst and a permanent top-heavy IMF.

measurement/model/sample boundary: Impacts virtually all conversion factors (K
FUV
	​

, K
IR
	​

), mass return fractions (R), and nucleosynthetic yields (y).

source keys: [REV02], [REV02-P031], [REV02-P032]

[REV02-D06]

role: debate

debate_topic: Ionizing escape fraction (f
esc
	​

) from star-forming galaxies.

competing positions: To successfully reionize the intergalactic medium by z∼6 using only galaxies, the escape fraction of Lyman-continuum photons from star-forming regions must be relatively high (approximately 20%). However, direct observations of galaxies at lower redshifts (z∼1−3) consistently measure very low, highly constrained escape fractions (typically < 5%).

why unresolved as of the review's 2014 boundary: The highly neutral IGM at z>6 absorbs escaping Lyman-continuum photons before they reach Earth, physically preventing direct measurement of f
esc
	​

 at the actual epoch of reionization.

measurement/model/sample boundary: Limits exact modeling of the intergalactic medium's ionization state and constrains the role of galaxies versus quasars.

source keys: [REV02], [REV02-P037], [REV02-P038]

[REV02-D07]

role: debate

debate_topic: Reionization photon sufficiency and the faint galaxy contribution.

competing positions: The bright, photometrically detected galaxies at z>6 cannot produce enough ionizing photons to maintain reionization. The deficit must either be entirely made up by a vast, undetected population of ultra-faint dwarf galaxies (requiring aggressive extrapolation of the luminosity function), or alternatively, by exotic sources or early black hole accretion.

why unresolved as of the review's 2014 boundary: The physical faint-end cutoff limit (M
lim
	​

) of the UV LF remains unknown, and the clumping factor of the IGM gas—which dictates the recombination rate—is poorly constrained by cosmological hydrodynamic simulations.

measurement/model/sample boundary: Defines reionization budget modeling, hydrogen recombination timescales, and UV emissivity bounds.

source keys: [REV02], [REV02-P011], [REV02-P038]

[REV02-D08]

role: debate

debate_topic: Faint-end extrapolation divergence.

competing positions: The mathematical integration of Schechter functions with faint-end slopes steeper than α<−2 results in an infinite, non-physical luminosity density. A physical turnover or truncation must exist, but its location (L
min
	​

) is highly disputed, with models placing it anywhere from M
UV
	​

=−15 down to −10.

why unresolved as of the review's 2014 boundary: Absolute observational limits prevent viewing galaxies below 0.03L
∗
 at z∼8, rendering the turnover entirely theoretical.

measurement/model/sample boundary: Directly impacts the calculated total SFRD at z>6 and the cosmological accounting of early baryonic collapse.

source keys: [REV02], [REV02-P011]

4. Key measurements and calibrations
Role	Metric/Calibration	Value/Range	Sample, Tracer, Method & Caveats	Primary Source Keys
measurement	Analytical fit to the Cosmic SFRD	ψ(z)=0.015
1+[(1+z)/2.9]
5.6
(1+z)
2.7
	​

 M
⊙
	​

 yr$^{-1}$ Mpc$^{-3}$	Method: Compilation of FUV and IR surveys. Caveat: Assumes a Salpeter IMF and fixed integration limits; the precise redshift of the peak is somewhat degenerate with the functional form.	[REV02]
calibration	FUV-to-SFR Conversion Factor	K
FUV
	​

=1.15×10
−28
 M
⊙
	​

 yr$^{-1}$ erg$^{-1}$ s Hz	Method: Calibrated for rest-frame 1500 Å assuming a continuous star-formation history of ≥100 Myr and a Salpeter IMF (0.1 - 100 M
⊙
	​

). Caveat: Highly sensitive to bursty star formation and uncorrected for dust attenuation.	[REV02], [REV02-P001]
measurement	Faint-end slope of the UV LF at high-z	α=−2.01±0.21 at z∼7	Method: HUDF and GOODS rest-frame UV dropout candidates. Caveat: Requires massive completeness corrections for the surface brightness biases of faint, compact sources.	[REV02], [REV02-P010], [REV02-P011]
measurement	Mid-redshift obscured SFRD	Dominates the cosmic budget at z∼2	Method: Herschel Space Observatory PEP/HerMES surveys mapping 100-500 μm. Caveat: Confusion limits of the Herschel beam prevent resolving individual faint sources, requiring statistical stacking.	[REV02], [REV02-P015], [REV02-P017]
measurement	Local cosmic stellar mass density	ρ
∗
	​

(z=0)≈2×10
8
 M
⊙
	​

 Mpc$^{-3}$	Method: 2MASS and SDSS near-infrared integrated luminosity densities combined with M/L ratios. Caveat: Highly dependent on the assumed IMF and the treatment of TP-AGB stars in SPS models.	[REV02], [REV02-P018]
calibration	Stellar mass return fraction	R=0.27 (Salpeter) / R=0.41 (Chabrier)	Method: Instantaneous recycling approximation for stars m>1M
⊙
	​

 returning mass via winds and supernovae. Caveat: Breaks down if star-formation histories are younger than the lifetimes of intermediate-mass stars.	[REV02], [REV02-P031]
calibration	Core-collapse supernova formation efficiency	k
CC
	​

=0.0068 M
⊙
−1
	​

	Method: Salpeter IMF integrated between m
min
	​

=8M
⊙
	​

 and m
max
	​

=40M
⊙
	​

. Caveat: Excludes potential massive star mergers and assumes stars above 40 M
⊙
	​

 collapse directly to black holes without a visible SN.	[REV02], [REV02-P025]
calibration	Net metal yield	y=0.016 (Salpeter) / y=0.032 (Chabrier)	Method: Nucleosynthetic models integrated over the respective IMFs for subsolar metallicity stars. Caveat: Yields depend sensitively on stellar rotation, binary evolution, and the assumed mass limit for black hole formation.	[REV02], [REV02-P033], [REV02-P035]
5. What remained unknown in 2014

[REV02-U01]

role: future

gap: The exact position of the turnover or truncation luminosity (L
min
	​

) in the faint end of the UV luminosity function at high redshifts.

why it mattered: Establishing a physical turnover is mathematically required to prevent the divergence of the integrated SFRD when the slope α<−2, and is practically required to quantify the total ionizing photon budget available for reionization from dwarf galaxies.

observation/model needed: Deeper near-infrared imaging beyond the absolute capabilities of HST, primarily awaiting the launch and deployment of JWST.

review and primary source keys: [REV02], [REV02-P011]

[REV02-U02]

role: future

gap: Direct, empirical measurements of the Lyman-continuum escape fraction (f
esc
	​

) from star-forming galaxies at z>6.

why it mattered: The transition of the IGM from neutral to ionized relies completely on this parameter; assuming f
esc
	​

∼20% was a theoretical necessity for galaxy-driven reionization rather than an observational fact.

observation/model needed: Deep spectroscopy of faint reionization-era galaxies, or highly magnified lensed analogs, to directly detect leaking Lyman-continuum flux.

review and primary source keys: [REV02], [REV02-P037], [REV02-P038]

[REV02-U03]

role: future

gap: The true extent and magnitude of dust-obscured star formation at z>4.

why it mattered: Rest-frame UV dropout surveys absolutely dominate the z>4 cosmic census; if substantial dust exists in normal, non-starburst galaxies at these epochs, the early cosmic SFRD is severely underestimated.

observation/model needed: Deep, high-resolution submillimeter continuum mapping of individual, typical star-forming galaxies using ALMA.

review and primary source keys: [REV02], [REV02-P009], [REV02-P015]

[REV02-U04]

role: future

gap: The exact shape of the Initial Mass Function (IMF) in zero-metallicity (Population III) and extremely metal-poor early galaxies.

why it mattered: A top-heavy IMF would alter all UV-to-SFR conversions, heavily modify heavy element yields, and drastically increase ionizing photon production rates, entirely shifting the normalization of the early SFRD.

observation/model needed: Spectral signatures of exotic stellar populations (e.g., unusually strong He II emission) or direct detection of Pop III pair-instability supernovae.

review and primary source keys: [REV02], [REV02-P031], [REV02-P032]

[REV02-U05]

role: future

gap: Complete resolution of the mild but persistent discrepancy between the time-integral of the SFRD and the locally measured Stellar Mass Density (SMD).

why it mattered: The consistent mismatch implies either widespread systematic errors in photometric SED mass fitting (such as the treatment of TP-AGB stars), severe errors in dust corrections, or the non-universality of the IMF.

observation/model needed: Better calibrated stellar population synthesis models validated by independent kinematic mass measurements for high-z galaxies.

review and primary source keys: [REV02], [REV02-P021], [REV02-P022], [REV02-P024]

[REV02-U06]

role: future

gap: The precise, unambiguous redshift of the cosmic SFRD peak.

why it mattered: The "cosmic noon" represents the absolute peak efficiency of baryon conversion into stars across the universe's history; resolving its exact timing and width is necessary to calibrate cosmological hydrodynamic feedback models.

observation/model needed: Uniform, mass-complete surveys spanning 1<z<3 with simultaneous UV, optical, and IR coverage to mitigate the effects of cosmic variance.

review and primary source keys: [REV02], [REV02-P015], [REV02-P020]

6. Primary-citation harvest

[REV02-P001] Kennicutt, R. C. (1998, Annual Review of Astronomy and Astrophysics) | title=Star Formation in Galaxies Along the Hubble Sequence | DOI:10.1146/annurev.astro.36.1.189; arXiv:astro-ph/9807187; ADS:1998ARA&A..36..189K | role=calibration | review_locator=Section 3.1 | Standardizes the foundational conversion between rest-frame UV luminosity and instantaneous star-formation rate.
[REV02-P002] Madau, P. et al. (1996, Monthly Notices of the Royal Astronomical Society) | title=High-redshift galaxies in the Hubble Deep Field: colour selection and star formation history to z~4 | DOI:10.1093/mnras/283.4.1388; arXiv:astro-ph/9607172; ADS:1996MNRAS.283.1388M | role=measurement | review_locator=Section 1 | Pioneer application of the Lyman-break dropout technique to estimate early SFRD from the HDF.
[REV02-P003] Lilly, S. J. et al. (1996, Astrophysical Journal) | title=The Canada-France Redshift Survey. XI. The Cosmic Star Formation History from the Expected Evolution of the Galaxy Luminosity Function | DOI:10.1086/177272; arXiv:astro-ph/9601050; ADS:1996ApJ...460L...1L | role=measurement | review_locator=Section 1 | Early foundational measurement of the intermediate-redshift cosmic star-formation history tracking the decline to the present.
[REV02-P004] Wyder, T. K. et al. (2005, Astrophysical Journal Letters) | title=The Ultraviolet Galaxy Luminosity Function in the Local Universe from GALEX Data | DOI:10.1086/427359; arXiv:astro-ph/0411600; ADS:2005ApJ...619L..15W | role=measurement | review_locator=Table 1 | Provides the definitive local (z~0.1) FUV luminosity function anchoring the low-redshift end of the SFRD fit.
[REV02-P005] Schiminovich, D. et al. (2005, Astrophysical Journal Letters) | title=The GALEX-VVDS Measurement of the Evolution of the Far-Ultraviolet Luminosity Density and the Cosmic Star Formation Rate | DOI:10.1086/427376; arXiv:astro-ph/0411602; ADS:2005ApJ...619L..47S | role=measurement | review_locator=Table 1 | Extends the GALEX FUV luminosity density measurements out to z < 1.
[REV02-P006] Cucciati, O. et al. (2012, Astronomy and Astrophysics) | title=The star formation rate density and dust attenuation evolution over 12 Gyr with the VVDS surveys | DOI:10.1051/0004-6361/201118010; arXiv:1109.1005; ADS:2012A&A...539A..31C | role=measurement | review_locator=Table 1 | Provides FUV luminosity densities and dust attenuation trends across intermediate redshifts (0.1 < z < 4).
[REV02-P007] Dahlen, T. et al. (2007, Astrophysical Journal) | title=The Rest-Frame Ultraviolet Luminosity Function of Galaxies at Redshifts z~1-3 | DOI:10.1086/508854; arXiv:astro-ph/0608442; ADS:2007ApJ...654..172D | role=measurement | review_locator=Table 1 | Anchors the FUV luminosity density across the "cosmic noon" epoch (z~1-3).
[REV02-P008] Reddy, N. A. & Steidel, C. C. (2009, Astrophysical Journal) | title=A Steep Faint-End Slope of the UV Luminosity Function at z ~ 2-3: Implications for the Global Star Formation Rate and Energy Density | DOI:10.1088/0004-637X/692/1/778; arXiv:0810.2788; ADS:2009ApJ...692..778R | role=measurement | review_locator=Table 1 | Constrains the faint-end slope and dust corrections of the UV LF at the peak SFRD epoch.
[REV02-P009] Calzetti, D. et al. (2000, Astrophysical Journal) | title=The Dust Content and Opacity of Actively Star-forming Galaxies | DOI:10.1086/308692; arXiv:astro-ph/9911459; ADS:2000ApJ...533..682C | role=calibration | review_locator=Section 4.1 | Establishes the foundational empirical dust attenuation curve and the IRX-beta relationship used to correct UV luminosities.
[REV02-P010] Bouwens, R. J. et al. (2011, Astrophysical Journal) | title=Ultraviolet Luminosity Functions from 132 z ~ 7 and z ~ 8 Early-epoch Galaxies in the HUDF09 and Oesch+2010 Fields | DOI:10.1088/0004-637X/737/2/90; arXiv:1006.4360; ADS:2011ApJ...737...90B | role=measurement | review_locator=Section 5.1 | Provides critical high-z UV LF parameters demonstrating the steepening of the faint-end slope at z~7.
[REV02-P011] Bouwens, R. J. et al. (2012, Astrophysical Journal Letters) | title=Lower-luminosity Galaxies Could Reionize the Universe: Very Steep Faint-end Slopes to the UV Luminosity Functions at z >= 5-8 | DOI:10.1088/2041-8205/752/1/L5; arXiv:1105.2038; ADS:2012ApJ...752L...5B | role=debate | review_locator=Table 1 | Defines the debate around divergent faint-end slopes and their necessity for supplying the reionization photon budget.
[REV02-P012] Schenker, M. A. et al. (2013, Astrophysical Journal) | title=The UV Luminosity Function of Star-forming Galaxies via Dropout Selection at Redshifts z ~ 7 and 8 from the 2012 Ultra Deep Field Campaign | DOI:10.1088/0004-637X/768/2/196; arXiv:1212.4819; ADS:2013ApJ...768..196S | role=measurement | review_locator=Table 1 | Extends robust UV LF measurements to z~8, anchoring the sharp decline of the high-redshift SFRD.
[REV02-P013] Sanders, D. B. et al. (2003, Astronomical Journal) | title=The IRAS Revised Bright Galaxy Sample | DOI:10.1086/376841; arXiv:astro-ph/0306263; ADS:2003AJ....126.1607S | role=measurement | review_locator=Table 1 | Baseline local calibration of the far-infrared luminosity function tracking dust-obscured star formation at z~0.
[REV02-P014] Takeuchi, T. T. et al. (2003, Publications of the Astronomical Society of Japan) | title=The Luminosity Function of Galaxies in the Local Universe | DOI:none; arXiv:astro-ph/0212061; ADS:2003PASJ...55..381T | role=measurement | review_locator=Table 1 | Contributes to the baseline z=0 infrared luminosity density for the analytical fit.
[REV02-P015] Gruppioni, C. et al. (2013, Monthly Notices of the Royal Astronomical Society) | title=The Herschel PEP/HerMES luminosity function - I. Probing the evolution of PACS selected Galaxies to z ~ 4 | DOI:10.1093/mnras/stt308; arXiv:1302.5209; ADS:2013MNRAS.432...23G | role=measurement | review_locator=Table 1 | Key Herschel measurement mapping the extreme rise and dominance of dust-obscured star formation at z~2.
[REV02-P016] Magnelli, B. et al. (2011, Astronomy and Astrophysics) | title=Evolution of the dusty infrared luminosity function from z = 0 to z = 2.3 using observations from Spitzer | DOI:10.1051/0004-6361/201016146; arXiv:1101.2467; ADS:2011A&A...528A..35M | role=measurement | review_locator=Table 1 | Spitzer-based constraints on the intermediate-redshift evolution of the obscured SFRD.
[REV02-P017] Magnelli, B. et al. (2013, Astronomy and Astrophysics) | title=The deepest Herschel-PACS far-infrared survey: number counts and infrared luminosity functions from combined PEP/GOODS-H observations | DOI:10.1051/0004-6361/201321371; arXiv:1303.4436; ADS:2013A&A...553A.132M | role=measurement | review_locator=Table 1 | Deep far-IR measurements confirming that obscured star formation accounts for the vast majority of the SFRD peak.
[REV02-P018] Dickinson, M. et al. (2003, Astrophysical Journal) | title=The Evolution of the Global Stellar Mass Density at 0 < z < 3 | DOI:10.1086/374329; arXiv:astro-ph/0302445; ADS:2003ApJ...587...25D | role=measurement | review_locator=Section 1 | Foundational near-infrared survey linking the rest-frame optical light of evolved stars to cosmic stellar mass buildup.
[REV02-P019] Muzzin, A. et al. (2013, Astrophysical Journal) | title=The Evolution of the Stellar Mass Functions of Star-forming and Quiescent Galaxies to z = 4 from the COSMOS/UltraVISTA Survey | DOI:10.1088/0004-637X/777/1/18; arXiv:1303.4409; ADS:2013ApJ...777...18M | role=measurement | review_locator=Table 2 | Provides critical high-redshift (z~4) constraints on the assembly of the cosmic stellar mass density.
[REV02-P020] Hopkins, A. M. & Beacom, J. F. (2006, Astrophysical Journal) | title=On the Normalization of the Cosmic Star Formation History | DOI:10.1086/506610; arXiv:astro-ph/0601463; ADS:2006ApJ...651..142H | role=review | review_locator=Section 1 | Predecessor compilation of the cosmic SFRD highlighting cross-calibration issues between independent measurements.
[REV02-P021] Cole, S. et al. (2001, Monthly Notices of the Royal Astronomical Society) | title=The 2dF Galaxy Redshift Survey: near-infrared galaxy luminosity functions | DOI:10.1046/j.1365-8711.2001.04591.x; arXiv:astro-ph/0012429; ADS:2001MNRAS.326..255C | role=measurement | review_locator=Section 5.3 | Establishes the local z=0 stellar mass density benchmark used to test the integral of the SFRD.
[REV02-P022] Conroy, C. et al. (2009, Astrophysical Journal) | title=The Propagation of Uncertainties in Stellar Population Synthesis Modeling. I. The Relevance of Uncertain Aspects of Stellar Evolution and the Initial Mass Function to the Derived Physical Properties of Galaxies | DOI:10.1088/0004-637X/699/1/486; arXiv:0810.0577; ADS:2009ApJ...699..486C | role=caveat | review_locator=Section 3.2 | Highlights severe systematic uncertainties in stellar mass and SFR conversions due to TP-AGB stars and IMF choices.
[REV02-P023] Steidel, C. C. et al. (1999, Astrophysical Journal) | title=Lyman-Break Galaxies at z~4 and the Evolution of the Ultraviolet Luminosity Density at High Redshift | DOI:10.1086/307363; arXiv:astro-ph/9811399; ADS:1999ApJ...519....1S | role=measurement | review_locator=Section 1 | Classical definition of the Lyman-break selection technique enabling the first reliable z>3 cosmic censuses.
[REV02-P024] Maraston, C. (2005, Monthly Notices of the Royal Astronomical Society) | title=Evolutionary synthesis of stellar populations: a mock grid for extra-galactic studies | DOI:10.1111/j.1365-2966.2005.09270.x; arXiv:astro-ph/0410207; ADS:2005MNRAS.362..799M | role=caveat | review_locator=Section 3.2 | Demonstrates how the treatment of Thermally Pulsing AGB stars drastically alters derived stellar masses and ages.
[REV02-P025] Dahlen, T. et al. (2004, Astrophysical Journal) | title=High-Redshift Supernova Rates | DOI:10.1086/422402; arXiv:astro-ph/0406547; ADS:2004ApJ...613..189D | role=measurement | review_locator=Section 5.2 | Measures core-collapse supernova rates tracking the decline of massive star formation over cosmic time.
[REV02-P026] Horiuchi, S. et al. (2011, Astrophysical Journal) | title=The Cosmic Core-collapse Supernova Rate does not match the Star Formation Rate | DOI:10.1088/0004-637X/738/2/154; arXiv:1102.1977; ADS:2011ApJ...738..154H | role=debate | review_locator=Section 5.2 | Introduces the discrepancy between the observed CC SN rate and the predicted rate derived from the integrated SFRD.
[REV02-P027] Finkelstein, S. L. et al. (2013, Nature) | title=A galaxy rapidly forming stars 700 million years after the Big Bang at redshift 7.51 | DOI:10.1038/nature12657; arXiv:1310.6031; ADS:2013Natur.502..524F | role=measurement | review_locator=Section 1 | Confirmation of extreme, bursty star-formation well into the reionization epoch, pushing empirical boundaries.
[REV02-P028] Coe, D. et al. (2013, Astrophysical Journal) | title=CLASH: Three Strongly Lensed Images of a Candidate z ~ 11 Galaxy | DOI:10.1088/0004-637X/762/1/32; arXiv:1211.3663; ADS:2013ApJ...762...32C | role=future | review_locator=Section 1 | Represents the extreme observational frontier for UV photometric dropouts awaiting spectroscopic confirmation.
[REV02-P029] Franx, M. et al. (2003, Astrophysical Journal Letters) | title=A Significant Population of Red, Near-Infrared-selected High-Redshift Galaxies | DOI:10.1086/375253; arXiv:astro-ph/0302343; ADS:2003ApJ...587L..79F | role=measurement | review_locator=Section 1 | Identifies heavily dust-obscured, passive galaxies at high redshift missed by standard rest-frame UV dropout selections.
[REV02-P030] Daddi, E. et al. (2005, Astrophysical Journal) | title=Passively Evolving Early-Type Galaxies at 1.4 < z < 2.5 in the Hubble Ultra Deep Field | DOI:10.1086/430349; arXiv:astro-ph/0503102; ADS:2005ApJ...626..680D | role=measurement | review_locator=Section 1 | Confirms the rapid assembly of massive, dead galaxies remarkably close to the cosmic noon peak.
[REV02-P031] Chabrier, G. (2003, Publications of the Astronomical Society of the Pacific) | title=Galactic Stellar and Substellar Initial Mass Function | DOI:10.1086/376392; arXiv:astro-ph/0304382; ADS:2003PASP..115..763C | role=calibration | review_locator=Section 2 | Defines the modern standard log-normal IMF, significantly shifting predicted stellar mass return fractions compared to Salpeter.
[REV02-P032] Salpeter, E. E. (1955, Astrophysical Journal) | title=The Luminosity Function and Stellar Evolution | DOI:10.1086/145971; arXiv:none; ADS:1955ApJ...121..161S | role=calibration | review_locator=Section 2 | The historic baseline power-law IMF used to calibrate the primary analytical SFRD fit and SN rates.
[REV02-P033] Maeder, A. (1992, Astronomy and Astrophysics) | title=Stellar yields as a function of mass and metallicity | DOI:none; arXiv:none; ADS:1992A&A...264..105M | role=theory | review_locator=Section 2 | Provides the foundational stellar nucleosynthetic yields necessary for calculating the metal enrichment tracking the SFRD.
[REV02-P034] Asplund, M. et al. (2009, Annual Review of Astronomy and Astrophysics) | title=The Chemical Composition of the Sun | DOI:10.1146/annurev.astro.46.060407.145222; arXiv:0909.0948; ADS:2009ARA&A..47..481A | role=calibration | review_locator=Section 2 | Updates the solar metallicity boundary, generating tensions with older models calculating cosmic enrichment.
[REV02-P035] Chieffi, A. & Limongi, M. (2004, Astrophysical Journal) | title=Explosive Yields of Massive Stars from Z = 0 to Z = Z_sun | DOI:10.1086/382801; arXiv:astro-ph/0311311; ADS:2004ApJ...608..405C | role=theory | review_locator=Section 2 | Calculates the metallic yield returned to the IGM via supernovae as a function of the underlying SFR.
[REV02-P036] Kewley, L. J. & Kobulnicky, H. A. (2007, Astrophysics and Space Science Proceedings) | title=Metallicity of Star-Forming Galaxies | DOI:10.1007/978-1-4020-5696-9_24; arXiv:astro-ph/0702283; ADS:2007iuse.book..435K | role=measurement | review_locator=Section 3.1 | Empirically traces the redshift evolution of global metallicity, modifying the conversion factors between UV light and SFR.
[REV02-P037] Robertson, B. E. et al. (2013, Astrophysical Journal) | title=New Constraints on Cosmic Reionization from the 2012 Hubble Ultra Deep Field Campaign | DOI:10.1088/0004-637X/768/1/71; arXiv:1301.1228; ADS:2013ApJ...768...71R | role=theory | review_locator=Section 5.8 | Models the translation of the observed z>6 UV LF into the ionizing photon budget required to maintain cosmic reionization.
[REV02-P038] Haardt, F. & Madau, P. (2012, Astrophysical Journal) | title=Radiative Transfer in a Clumpy Universe. IV. New Synthesis Models of the Cosmic UV/X-Ray Background | DOI:10.1088/0004-637X/746/2/125; arXiv:1105.2039; ADS:2012ApJ...746..125H | role=theory | review_locator=Section 5.8 | Calculates hydrogen recombination timescales and the required IGM clumping factors to balance the reionization photon budget.
[REV02-P039] Pei, Y. C. & Fall, S. M. (1995, Astrophysical Journal) | title=Cosmic Chemical Evolution | DOI:10.1086/176503; arXiv:astro-ph/9508107; ADS:1995ApJ...454...69P | role=theory | review_locator=Section 5.1 | Early theoretical framework linking the observable cosmological mass density of HI to the overall comoving star formation.
[REV02-P040] Lanzetta, K. M. et al. (1995, Astrophysical Journal Letters) | title=The Star Formation History of the Universe | DOI:10.1086/309765; arXiv:astro-ph/9502073; ADS:1995ApJ...453L..17L | role=theory | review_locator=Section 5.1 | First formulation coupling chemical evolution equations to the photometric properties of the evolving cosmic volume.

7. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | The IMF is observationally fixed at high redshift | Overbroad extrapolation | The review strictly notes that assuming a universal IMF is a simplifying convention necessary for mathematical closure between the SFRD and SMD, not a physically proven guarantee for low-metallicity early epochs.
UNCITED_NOT_USABLE | AGN and Quasar Feedback co-evolution models | Kormendy & Ho (2013) ARA&A 51 511 | Quarantined per the mission rules to isolate non-AGN galaxy evolution mechanics from black hole accretion physics.
UNCITED_NOT_USABLE | Post-2014 refinements of the Cosmic SFRD | Haslbauer et al. (2023) / Strolger et al. (2020) | Outside the strict 2014 temporal boundary of the core review.
UNCITED_NOT_USABLE | One survey alone provides a complete cosmic SFR density | Overbroad / Concept violation | The review explicitly states that combining multiple tracers (rest-frame UV + far-IR) across surveys is mandatory to mitigate severe dust bias and cosmic variance.
UNCITED_NOT_USABLE | Stellar-mass-density agreement proves exact closure | Overbroad extrapolation | A mild persistent discrepancy remains between the integrated SFRD and observed SMD, requiring further refinement in SPS models or IMF parameters to achieve true closure.
UNCITED_NOT_USABLE | The review-fit peak is free of selection/model uncertainty | Overbroad / Concept violation | The review specifies that the precise peak (z≈1.85) is degenerate with the functional form and carries an inherent uncertainty of Δz=1.
UNCITED_NOT_USABLE | Dust corrections are redshift-independent | Overbroad extrapolation | Constant IRX-beta relationships fail to account for distinct metallicity and dust-geometry environments in z>4 galaxies.

8. Review and source identity ledger

[REV02] | Madau & Dickinson (2014, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev-astro-081811-125615; arXiv:1403.0007; ADS:2014ARA&A..52..415M | role=review | synthesis of cosmic star-formation history
[REV02-P001] | Kennicutt (1998, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev.astro.36.1.189; arXiv:astro-ph/9807187; ADS:1998ARA&A..36..189K | role=calibration | FUV-to-SFR conversion framework
[REV02-P002] | Madau et al. (1996, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/283.4.1388; arXiv:astro-ph/9607172; ADS:1996MNRAS.283.1388M | role=measurement | Early Lyman-break SFRD estimation
[REV02-P003] | Lilly et al. (1996, Astrophysical Journal) | DOI:10.1086/177272; arXiv:astro-ph/9601050; ADS:1996ApJ...460L...1L | role=measurement | Intermediate-z SFRD decline
[REV02-P004] | Wyder et al. (2005, Astrophysical Journal Letters) | DOI:10.1086/427359; arXiv:astro-ph/0411600; ADS:2005ApJ...619L..15W | role=measurement | Local FUV luminosity function
[REV02-P005] | Schiminovich et al. (2005, Astrophysical Journal Letters) | DOI:10.1086/427376; arXiv:astro-ph/0411602; ADS:2005ApJ...619L..47S | role=measurement | Mid-z FUV luminosity density
[REV02-P006] | Cucciati et al. (2012, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201118010; arXiv:1109.1005; ADS:2012A&A...539A..31C | role=measurement | UV luminosity density out to z=4
[REV02-P007] | Dahlen et al. (2007, Astrophysical Journal) | DOI:10.1086/508854; arXiv:astro-ph/0608442; ADS:2007ApJ...654..172D | role=measurement | UV LF near cosmic noon
[REV02-P008] | Reddy & Steidel (2009, Astrophysical Journal) | DOI:10.1088/0004-637X/692/1/778; arXiv:0810.2788; ADS:2009ApJ...692..778R | role=measurement | Dust and faint-end slope at z~2-3
[REV02-P009] | Calzetti et al. (2000, Astrophysical Journal) | DOI:10.1086/308692; arXiv:astro-ph/9911459; ADS:2000ApJ...533..682C | role=calibration | Empirical dust attenuation curve
[REV02-P010] | Bouwens et al. (2011, Astrophysical Journal) | DOI:10.1088/0004-637X/737/2/90; arXiv:1006.4360; ADS:2011ApJ...737...90B | role=measurement | High-z steep faint-end LF slopes
[REV02-P011] | Bouwens et al. (2012, Astrophysical Journal Letters) | DOI:10.1088/2041-8205/752/1/L5; arXiv:1105.2038; ADS:2012ApJ...752L...5B | role=debate | Faint-end extrapolation for reionization
[REV02-P012] | Schenker et al. (2013, Astrophysical Journal) | DOI:10.1088/0004-637X/768/2/196; arXiv:1212.4819; ADS:2013ApJ...768..196S | role=measurement | UV LF at z=7 and 8
[REV02-P013] | Sanders et al. (2003, Astronomical Journal) | DOI:10.1086/376841; arXiv:astro-ph/0306263; ADS:2003AJ....126.1607S | role=measurement | Local IR luminosity function
[REV02-P014] | Takeuchi et al. (2003, Publications of the Astronomical Society of Japan) | DOI:none; arXiv:astro-ph/0212061; ADS:2003PASJ...55..381T | role=measurement | Local IR luminosity bounds
[REV02-P015] | Gruppioni et al. (2013, Monthly Notices of the Royal Astronomical Society) | DOI:10.1093/mnras/stt308; arXiv:1302.5209; ADS:2013MNRAS.432...23G | role=measurement | Herschel constraints on obscured SF at z~2
[REV02-P016] | Magnelli et al. (2011, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201016146; arXiv:1101.2467; ADS:2011A&A...528A..35M | role=measurement | Spitzer obscured SFRD evolution
[REV02-P017] | Magnelli et al. (2013, Astronomy and Astrophysics) | DOI:10.1051/0004-6361/201321371; arXiv:1303.4436; ADS:2013A&A...553A.132M | role=measurement | Deep Herschel IR LFs out to z~2.3
[REV02-P018] | Dickinson et al. (2003, Astrophysical Journal) | DOI:10.1086/374329; arXiv:astro-ph/0302445; ADS:2003ApJ...587...25D | role=measurement | Baseline cosmic stellar mass density
[REV02-P019] | Muzzin et al. (2013, Astrophysical Journal) | DOI:10.1088/0004-637X/777/1/18; arXiv:1303.4409; ADS:2013ApJ...777...18M | role=measurement | High-z stellar mass functions
[REV02-P020] | Hopkins & Beacom (2006, Astrophysical Journal) | DOI:10.1086/506610; arXiv:astro-ph/0601463; ADS:2006ApJ...651..142H | role=review | Previous SFRD normalization synthesis
[REV02-P021] | Cole et al. (2001, Monthly Notices of the Royal Astronomical Society) | DOI:10.1046/j.1365-8711.2001.04591.x; arXiv:astro-ph/0012429; ADS:2001MNRAS.326..255C | role=measurement | Local z=0 stellar mass benchmark
[REV02-P022] | Conroy et al. (2009, Astrophysical Journal) | DOI:10.1088/0004-637X/699/1/486; arXiv:0810.0577; ADS:2009ApJ...699..486C | role=caveat | TP-AGB and SPS modeling uncertainties
[REV02-P023] | Steidel et al. (1999, Astrophysical Journal) | DOI:10.1086/307363; arXiv:astro-ph/9811399; ADS:1999ApJ...519....1S | role=measurement | Lyman break selection methodology
[REV02-P024] | Maraston (2005, Monthly Notices of the Royal Astronomical Society) | DOI:10.1111/j.1365-2966.2005.09270.x; arXiv:astro-ph/0410207; ADS:2005MNRAS.362..799M | role=caveat | Treatment of TP-AGB stellar masses
[REV02-P025] | Dahlen et al. (2004, Astrophysical Journal) | DOI:10.1086/422402; arXiv:astro-ph/0406547; ADS:2004ApJ...613..189D | role=measurement | High-redshift core-collapse SN rates
[REV02-P026] | Horiuchi et al. (2011, Astrophysical Journal) | DOI:10.1088/0004-637X/738/2/154; arXiv:1102.1977; ADS:2011ApJ...738..154H | role=debate | Discrepancy between SN rate and SFR
[REV02-P027] | Finkelstein et al. (2013, Nature) | DOI:10.1038/nature12657; arXiv:1310.6031; ADS:2013Natur.502..524F | role=measurement | Bursty star-formation in the reionization epoch
[REV02-P028] | Coe et al. (2013, Astrophysical Journal) | DOI:10.1088/0004-637X/762/1/32; arXiv:1211.3663; ADS:2013ApJ...762...32C | role=future | Extreme frontier photometric UV dropouts
[REV02-P029] | Franx et al. (2003, Astrophysical Journal Letters) | DOI:10.1086/375253; arXiv:astro-ph/0302343; ADS:2003ApJ...587L..79F | role=measurement | Dusty red galaxies missing from UV catalogs
[REV02-P030] | Daddi et al. (2005, Astrophysical Journal) | DOI:10.1086/430349; arXiv:astro-ph/0503102; ADS:2005ApJ...626..680D | role=measurement | Passive massive galaxies at cosmic noon
[REV02-P031] | Chabrier (2003, Publications of the Astronomical Society of the Pacific) | DOI:10.1086/376392; arXiv:astro-ph/0304382; ADS:2003PASP..115..763C | role=calibration | Standard log-normal IMF
[REV02-P032] | Salpeter (1955, Astrophysical Journal) | DOI:10.1086/145971; arXiv:none; ADS:1955ApJ...121..161S | role=calibration | Baseline power-law IMF
[REV02-P033] | Maeder (1992, Astronomy and Astrophysics) | DOI:none; arXiv:none; ADS:1992A&A...264..105M | role=theory | Stellar yields for metal enrichment
[REV02-P034] | Asplund et al. (2009, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev.astro.46.060407.145222; arXiv:0909.0948; ADS:2009ARA&A..47..481A | role=calibration | Calibration of solar metallicity boundary
[REV02-P035] | Chieffi & Limongi (2004, Astrophysical Journal) | DOI:10.1086/382801; arXiv:astro-ph/0311311; ADS:2004ApJ...608..405C | role=theory | SN explosive metal yields tracking SFR
[REV02-P036] | Kewley & Kobulnicky (2007, Astrophysics and Space Science Proceedings) | DOI:10.1007/978-1-4020-5696-9_24; arXiv:astro-ph/0702283; ADS:2007iuse.book..435K | role=measurement | Cosmic metallicity evolution parameters
[REV02-P037] | Robertson et al. (2013, Astrophysical Journal) | DOI:10.1088/0004-637X/768/1/71; arXiv:1301.1228; ADS:2013ApJ...768...71R | role=theory | Reionization photon budget modeling
[REV02-P038] | Haardt & Madau (2012, Astrophysical Journal) | DOI:10.1088/0004-637X/746/2/125; arXiv:1105.2039; ADS:2012ApJ...746..125H | role=theory | IGM clumping and recombination timescales
[REV02-P039] | Pei & Fall (1995, Astrophysical Journal) | DOI:10.1086/176503; arXiv:astro-ph/9508107; ADS:1995ApJ...454...69P | role=theory | Cosmic chemical evolution framework
[REV02-P040] | Lanzetta et al. (1995, Astrophysical Journal Letters) | DOI:10.1086/309765; arXiv:astro-ph/9502073; ADS:1995ApJ...453L..17L | role=theory | Coupling chemical evolution to observables

REVIEW_BASE_02_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- arxiv.org [1403.0007] Cosmic Star Formation History - arXiv Opens in a new window — https://arxiv.org/abs/1403.0007
- annualreviews.org Cosmic Star-Formation History - Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-081811-125615
- arxiv.org Cosmic Star-Formation History - arXiv Opens in a new window — https://arxiv.org/pdf/1403.0007
- ned.ipac.caltech.edu Cosmic Star Formation History - Piero Madau & Mark Dickinson Opens in a new window — https://ned.ipac.caltech.edu/level5/March14/Madau/Madau_contents.html
- ned.ipac.caltech.edu the equations of cosmic chemical evolution - Cosmic Star Formation History - Piero Madau & Mark Dickinson Opens in a new window — https://ned.ipac.caltech.edu/level5/March14/Madau/Madau2.html
- ned.ipac.caltech.edu concluding remarks - Cosmic Star Formation History - Piero Madau & Mark Dickinson Opens in a new window — https://ned.ipac.caltech.edu/level5/March14/Madau/Madau6.html
- indico.cern.ch Charting the Universe with Primordial Black Holes: From Planetary to Supermassive - Indico - CERN Opens in a new window — https://indico.cern.ch/event/1576682/contributions/7113272/attachments/3297447/5897637/CERN_NEHOP26.pdf
- arxiv.org Constraining Cosmological and Astrophysical Parameters with the Cosmic Star Formation History - arXiv Opens in a new window — https://arxiv.org/pdf/2604.17660
- journalspress.uk Age, Size, Dynamics of Energy, Matter, and Masses of Black Holes in the Model of Accelerated Expansion of the Universe, based on Opens in a new window — https://www.journalspress.uk/index.php/LJRS/article/download/111/704
- osti.gov Diffuse supernova neutrino background with up-to-date star formation rate measurements and long-term multidimensional supernova - OSTI Opens in a new window — https://www.osti.gov/servlets/purl/2579336
- researchgate.net The Cosmic Star Formation History: Insights from Kilonova-associated Gamma-Ray Bursts Opens in a new window — https://www.researchgate.net/publication/400508783_The_Cosmic_Star_Formation_History_Insights_from_Kilonova-associated_Gamma-Ray_Bursts
- eso.org The High Redshift Universe in the E-ELT Era - I Richard Ellis (ESO) Opens in a new window — http://www.eso.org/sci/meetings/2015/EriceSchool2015/ellis_erice_elt15_1.pdf
- moodle2.units.it Real-life applications and examples: galaxy ... - Moodle@Units Opens in a new window — https://moodle2.units.it/pluginfile.php/816227/mod_resource/content/1/galaxySEDs_part3_1.pdf
- dash.harvard.edu Relative likelihood for life as a function of cosmic time - Harvard DASH Opens in a new window — https://dash.harvard.edu/bitstreams/7312037e-2433-6bd4-e053-0100007fdf3b/download
- thesis.unipd.it The history of star-formation in galaxies Opens in a new window — https://thesis.unipd.it/retrieve/2ee36c44-e120-48b1-847e-d85026b8c30f/Politino_tesi.pdf
- arxiv.org arXiv:1602.01985v1 [astro-ph.GA] 5 Feb 2016 Opens in a new window — https://arxiv.org/pdf/1602.01985
- academic.oup.com Effects of chemically homogeneous evolution of the first stars on the 21-cm signal and reionization - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/541/4/3113/8210401
- academic.oup.com Cosmic star-formation history and black hole accretion history inferred from the JWST mid-infrared source counts - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/527/3/5525/7424152
- knowledge.lancashire.ac.uk GAMA/G10-COSMOS/3D-HST: the 0 < z < 5 cosmic star formation history, stellar-mass, and - Lancashire Online Knowledge Opens in a new window — https://knowledge.lancashire.ac.uk/id/eprint/24540/1/stx2728.pdf
- researchgate.net The data points show SFRD measurements from Madau & Dickinson (2014)... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/The-data-points-show-SFRD-measurements-from-Madau-Dickinson-2014-and-Driver-et-al_fig1_371438742
- researchgate.net The Madau & Dickinson (2014) star formation rate density (SFRD)... | Download Scientific Diagram - ResearchGate Opens in a new window — https://www.researchgate.net/figure/The-Madau-Dickinson-2014-star-formation-rate-density-SFRD-compilation-recalibrated_fig3_341541475
- academic.oup.com A consistent measure of the merger histories of massive galaxies using close-pair statistics Opens in a new window — https://academic.oup.com/mnras/article/470/3/3507/3845145
- staff.ustc.edu.cn THE EVOLUTION OF NORMAL GALAXY X-RAY EMISSION THROUGH COSMIC HISTORY Opens in a new window — http://staff.ustc.edu.cn/~xuey/xyqpapers/Lehmer_xgal.pdf
- arxiv.org arXiv:1805.10270v2 [astro-ph.HE] 22 Aug 2018 Opens in a new window — https://arxiv.org/pdf/1805.10270
- research-portal.st-andrews.ac.uk GAMA/H-ATLAS: a meta-analysis of SFR indicators – comprehensive measures of the SFR–M∗ relation Opens in a new window — https://research-portal.st-andrews.ac.uk/files/246756254/Driver_2016_MNRAS_SFRIndicators_FinalPubVersion.pdf
- par.nsf.gov Detection of [O iii] at z ∼ 3: A Galaxy Above the Main Sequence, Rapidly Assembling Its Stellar Mass Opens in a new window — https://par.nsf.gov/servlets/purl/10078002
- arxiv.org How galaxies acquire their stellar mass at high redshift: High star formation efficiencies and the relative roles of dust and initial mass function - arXiv Opens in a new window — https://arxiv.org/html/2605.26209v2
- academic.oup.com GAMA/G10-COSMOS/3D-HST: the 0 < z < 5 cosmic star formation history, stellar-mass, and dust-mass densities | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/475/3/2891/4730178
- arxiv.org Accelerated Formation of Ultra-Massive Galaxies in the First Billion Years - arXiv Opens in a new window — https://arxiv.org/html/2309.02492v2
- arxiv.org The Luminosity Function and Clustering of H𝛼 Emitting Galaxies at z≈4-6 from a Complete NIRCam Grism Redshift Survey - arXiv Opens in a new window — https://arxiv.org/html/2504.08028v1
- arxiv.org Exploiting synergies between JWST and cosmic 21-cm observations to uncover star formation in the early Universe - arXiv Opens in a new window — https://arxiv.org/html/2503.21687v2
- science.gov high-redshift 21-cm signal: Topics by Science.gov Opens in a new window — https://www.science.gov/topicpages/h/high-redshift+21-cm+signal
- academic.oup.com Near-identical star formation rate densities from Hα and FUVat redshift zero | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/480/1/119/5036531
- arxiv.org Evolution of the infrared luminosity function and its corresponding dust-obscured star formation rate density out to z∼6 - arXiv Opens in a new window — https://arxiv.org/html/2509.12922v2
- researchgate.net Cosmic star formation history: This diagram shows the redshift... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Cosmic-star-formation-history-This-diagram-shows-the-redshift-evolution-of-the-star_fig1_335395325
- doi.org Star formation history from the cosmic infrared background anisotropies | Astronomy & Astrophysics (A&A) - DOI Opens in a new window — https://doi.org/10.1051/0004-6361/201732499
- cambridge.org The 1.4-GHz cosmic star formation history at z < 1.3 | Publications of the Astronomical Society of Australia | Cambridge Core Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/14ghz-cosmic-star-formation-history-at-z-13/107E37980A460DDF9502998A9E0E6D3B
- researchgate.net (PDF) Size, shade or shape? The contribution of galaxies of different types to the star-formation history of the Universe from SDSS-IV MaNGA - ResearchGate Opens in a new window — https://www.researchgate.net/publication/349025471_Size_shade_or_shape_The_contribution_of_galaxies_of_different_types_to_the_star-formation_history_of_the_Universe_from_SDSS-IV_MaNGA
- academic.oup.com Size, shade, or shape? The contribution of galaxies of different types to the star formation history of the Universe from SDSS-IV MaNGA - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/502/3/3128/6125954
- arxiv.org Star formation rate density as a function of galaxy mass at z < 0.2 with MUSE and GAMA surveys - arXiv Opens in a new window — https://arxiv.org/html/2410.08036v1
- academic.oup.com GAMA/DEVILS: constraining the cosmic star formation history from improved measurements of the 0.3–2.2 μm extragalactic background light - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/503/2/2033/6152275
- arxiv.org From cosmological simulations to binary black hole mergers: The impact of using analytical star formation history models on gravitational-wave source populations - arXiv Opens in a new window — https://arxiv.org/html/2601.20202v1
- arxiv.org COSMOS-Web: Star formation along the early Hubble sequence and the evolution of dust over the redshift range 0<z<12 - arXiv Opens in a new window — https://arxiv.org/html/2605.19661v1
- oamonitor.ireland.openaire.eu Cosmic Star-Formation History Opens in a new window — https://oamonitor.ireland.openaire.eu/rpo/dcu/search/publication?pid=10.1146%2Fannurev-astro-081811-125615
- dictionary.obspm.fr cosmic star formation peak - An Etymological Dictionary of Astronomy and Astrophysics Opens in a new window — https://dictionary.obspm.fr/terms/cosmic-star-formation-peak/
- pos.sissa.it PoS(MULTIF2023)059 - SISSA Opens in a new window — https://pos.sissa.it/447/059/pdf
- ora.ox.ac.uk The star-formation history in the last 10 billion years from CIB cross-correlations Opens in a new window — https://ora.ox.ac.uk/objects/uuid:29b6e166-55c3-4796-97d6-2a6f617039af/files/sw37637985
- arxiv.org Fast Radio Bursts Trace Cosmic Star Formation with Little Delay - arXiv Opens in a new window — https://arxiv.org/html/2607.09109v1
- arxiv.org Tracing cosmic star formation history through radio continuum spectral energy distribution and non-thermal emission - arXiv Opens in a new window — https://arxiv.org/html/2607.12073v1
- arxiv.org Gamma-ray bursts reveal the history and faint contributors of cosmic reionization - arXiv Opens in a new window — https://arxiv.org/html/2607.07610v1
- arxiv.org Semi-empirical Predictions for Ultra-deep Radio Counts of Star-forming Galaxies with the SKAO - arXiv Opens in a new window — https://arxiv.org/html/2606.26773v1
- pure.port.ac.uk The 1.4 GHz Cosmic Star Formation History at z < 1.3 - University of Portsmouth Opens in a new window — https://pure.port.ac.uk/ws/portalfiles/portal/14329724/The_1.4_GHz_Cosmic_Star_Formation_History.pdf
- arxiv.org The high-redshift star formation history from carbon monoxide intensity maps - arXiv Opens in a new window — https://arxiv.org/pdf/1507.06304
- arxiv.org arXiv:1411.1431v1 [astro-ph.GA] 5 Nov 2014 Opens in a new window — https://arxiv.org/pdf/1411.1431
- ned.ipac.caltech.edu Physical Models of Galaxy Formation in a Cosmological Framework - Rachel S. Somerville & Romeel Davé Opens in a new window — https://ned.ipac.caltech.edu/level5/March19/Somerville/Somerville1.html
- arxiv.org The cosmological star formation history from the Local Cosmological Volume of galaxies and constraints on the matter homogeneity - arXiv Opens in a new window — https://arxiv.org/pdf/2306.16436
- amsdottorato.unibo.it From fueling to quenching star formation across cosmic time - AMS Dottorato Opens in a new window — https://amsdottorato.unibo.it/id/eprint/9813/1/Tesi_dottorato_FLoiacono.pdf
- arxiv.org An H𝛼 view of galaxy build-up in the first 2 Gyr: luminosity functions at z∼4-6.5 from NIRCam/grism spectroscopy - arXiv Opens in a new window — https://arxiv.org/html/2409.17241v3
- researchonline.ljmu.ac.uk Galaxy And Mass Assembly (GAMA): a forensic SED reconstruction of the cosmic star formation history and metallicity evolution by - LJMU Research Online Opens in a new window — https://researchonline.ljmu.ac.uk/id/eprint/13813/1/Galaxy%20And%20Mass%20Assembly%20(GAMA)%20a%20forensic%20SED%20reconstruction%20of%20the%20cosmic%20star%20formation%20history%20and%20metallicity%20evolution%20by%20galaxy%20type.pdf
- arxiv.org Decoding Galaxy SEDs with Physical Priors and Accurate Star Formation History Reconstruction - arXiv Opens in a new window — https://arxiv.org/html/2408.07749v1
- arxiv.org The massive star population of metal-poor galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/2512.15817
- annualreviews.org The Cosmic Baryon and Metal Cycles - Annual Reviews Opens in a new window — https://www.annualreviews.org/doi/pdf/10.1146/annurev-astro-021820-120014
- annualreviews.org New Insights into the Evolution of Massive Stars and Their Effects on Our Understanding of Early Galaxies - Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-052920-100646?crawler=true&mimetype=application/pdf
- pmc.ncbi.nlm.nih.gov Considering light–matter interactions in the Friedmann equations - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC9066607/
- purehost.bath.ac.uk Star-Forming Galaxies at Cosmic Noon Opens in a new window — https://purehost.bath.ac.uk/ws/files/212416702/ForsterSchreiberWuyts_araa_withPerm.pdf
- arxiv.org Recalibrating the Cosmic Star Formation History - arXiv Opens in a new window — https://arxiv.org/pdf/1910.05220
- arxiv.org Elevated UV luminosity density at Cosmic Dawn explained by non-evolving, weakly mass-dependent star formation efficiency - arXiv Opens in a new window — https://arxiv.org/html/2407.02674v2
- iris.sissa.it Astroparticle Constraints from Cosmic Reionization and Primordial Galaxy Formation - IRIS Opens in a new window — https://iris.sissa.it/retrieve/f6c6e40a-c3e2-402b-845b-7a60d21a2d5a/Lapi22.pdf
- arxiv.org arXiv:1707.09044v1 [astro-ph.HE] 27 Jul 2017 Opens in a new window — https://arxiv.org/pdf/1707.09044
- grokipedia.com Great Observatories Origins Deep Survey - Grokipedia Opens in a new window — https://grokipedia.com/page/great_observatories_origins_deep_survey
- ned.ipac.caltech.edu introduction - Cosmic Star Formation History - Piero Madau & Mark Dickinson Opens in a new window — https://ned.ipac.caltech.edu/level5/March14/Madau/Madau1.html
- ned.ipac.caltech.edu tracing the galaxy emission history with large surveys - Cosmic Star Formation History - Piero Madau & Mark Dickinson Opens in a new window — https://ned.ipac.caltech.edu/level5/March14/Madau/Madau4.html
- arxiv.org Clues on the history of early-type galaxies from SDSS spectra and Opens in a new window — https://arxiv.org/pdf/2007.01314
- academic.oup.com A universal ultraviolet–optical colour–colour–magnitude relation of galaxies Opens in a new window — https://academic.oup.com/mnras/article-pdf/419/2/1727/3129713/mnras0419-1727.pdf
- arxiv.org A new population of recently quenched elliptical galaxies in the SDSS - arXiv Opens in a new window — https://arxiv.org/pdf/1308.0054
- arxiv.org Clash of the Trident and Tuning Fork: insights from bar and spiral strength in the (massive black hole)-stellar mass diagrams, and the 'Triangal' galaxy evolution schema - arXiv Opens in a new window — https://arxiv.org/html/2604.24084v1
- sissa.it Coevolution of Supermassive Black Holes and Galaxies across cosmic times - SISSA Opens in a new window — https://www.sissa.it/ap/phdsection/AlumniThesis/Aversa%20Rossella.pdf
- academic.oup.com GAMA/G10-COSMOS/3D-HST: the 0 < z < 5 cosmic star formation history, stellar-mass, and - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/475/3/2891/23814417/stx2728.pdf
- livrepository.liverpool.ac.uk Material Visualisation for Virtual Reality: The Perceptual Investigations - University of Liverpool Repository Opens in a new window — https://livrepository.liverpool.ac.uk/3167894/1/201131774_Jul2022.pdf
- gitlab.in2p3.fr bibliography.bib · d61f2dbe183838b90475c558754e17c6d5ea8de4 - Gitlab IN2P3 Opens in a new window — https://gitlab.in2p3.fr/m2-npac-ac/m2-npac-ac.pages.in2p3.fr/-/blob/d61f2dbe183838b90475c558754e17c6d5ea8de4/bibliography.bib
- arxiv.org Direct determination of the UV Luminosity Function and its evolution from z ∼ 0.8 - arXiv Opens in a new window — https://arxiv.org/pdf/2310.01903
- arxiv.org arXiv:2012.09160v2 [astro-ph.GA] 29 May 2021 Opens in a new window — https://arxiv.org/pdf/2012.09160
- arxiv.org Tracing Large-scale Structure with the MeerKLASS On-the-Fly Survey: Angular Clustering of Radio Sources at 816 MHz - arXiv Opens in a new window — https://arxiv.org/html/2606.22432v1
- academic.oup.com Protoclusters as drivers of stellar mass growth in the early Universe, a case study: Taralay Opens in a new window — https://academic.oup.com/mnras/article/528/4/6934/7595795
- arxiv.org Multiwavelength Analysis of Six Luminous, Fast Blue Optical Transients - arXiv Opens in a new window — https://arxiv.org/pdf/2601.18926
- arxiv.org Simulating emission line galaxies for the next generation of large-scale structure surveys - arXiv Opens in a new window — https://arxiv.org/pdf/2404.00092
- pure.mpg.de Constraining star formation rates in cool-core brightest cluster galaxies - MPG.PuRe Opens in a new window — https://pure.mpg.de/rest/items/item_2171206_2/component/file_2171205/content?download=true
- research.iac.es arXiv:2406.15572v1 [astro-ph.IM] 21 Jun 2024 Opens in a new window — https://research.iac.es/preprints/files/PP24102.pdf
- arxiv.org arXiv:2412.14377v1 [astro-ph.GA] 18 Dec 2024 Opens in a new window — https://arxiv.org/pdf/2412.14377
- arxiv.org The Stellar Initial Mass Function Down To 0.16 M⊙ Towards the Small Magellanic Cloud Opens in a new window — https://arxiv.org/html/2603.15438v1
- arxiv.org FASTAR - I. Continuous and differentiable evolutionary stellar population models - arXiv Opens in a new window — https://arxiv.org/html/2605.24093v1
- arxiv.org The impact of cosmic filaments on starburst galaxies across cosmic times - arXiv Opens in a new window — https://arxiv.org/html/2602.21890v2
- arxiv.org The Stellar Mass Function for Nine Massive Galaxy Clusters in the Local Universe - arXiv Opens in a new window — https://arxiv.org/html/2603.03797v2
- arxiv.org Interaction-induced star formation boosts stellar mass assembly in z∼5 galaxies - arXiv Opens in a new window — https://arxiv.org/html/2606.28590v1
- arxiv.org A Salpeter IMF and an NFW halo: Disentangling the dark and stellar mass of an elliptical galaxy through precise lens modelling of a double-source-plane system - arXiv Opens in a new window — https://arxiv.org/html/2602.20889v2
- researchgate.net (PDF) Star Formation - ResearchGate Opens in a new window — https://www.researchgate.net/publication/383792062_Star_Formation
- amsdottorato.unibo.it ASTROFISICA - AMS Tesi di Dottorato Opens in a new window — https://amsdottorato.unibo.it/id/eprint/11412/1/phd_thesis_final.pdf
- commons.erau.edu The White Dwarf Luminosity Function - Scholarly Commons Opens in a new window — https://commons.erau.edu/cgi/viewcontent.cgi?article=2056&context=publication
- nbi.ku.dk Examining the existence of two distinct modes of star formation Opens in a new window — https://nbi.ku.dk/english/theses/masters-theses/isabella-chi-gieseler-cortzen/IsabellaCortzen_thesis.pdf
- archiv.ub.uni-heidelberg.de Dissertation submitted to the Combined Faculty of Natural Sciences and Mathematics of Heidelberg University, Germany for the deg Opens in a new window — https://archiv.ub.uni-heidelberg.de/volltextserver/29009/1/Jeffreson-Sarah-2020.pdf
- arxiv.org Investigating the origin of radio emission in candidate super-Eddington accreting black holes - arXiv Opens in a new window — https://arxiv.org/html/2602.00321v2
- repositories.lib.utexas.edu Copyright by Amanda Elaine Bauer 2008 Opens in a new window — https://repositories.lib.utexas.edu/bitstreams/910f910a-558a-4231-b4a5-95b22dadf003/download
- diva-portal.org A JWST Study of Stellar Clumps lensed by the Cluster MACS J0647 - DiVA Portal Opens in a new window — https://www.diva-portal.org/smash/get/diva2:1893714/FULLTEXT01.pdf
- research.unipd.it Zoom-in on the dust-obscured phase of galaxy formation with gravitational lenses - Padua Research Archive Opens in a new window — https://www.research.unipd.it/retrieve/e14fb26f-af1b-3de1-e053-1705fe0ac030/tesi_AndreaFrancescoMaria_Enia.pdf
- iris.sissa.it Formation and Evolution of Massive Early-Type ... - IRIS - SISSA Opens in a new window — https://iris.sissa.it/retrieve/dd8a4bf7-0762-20a0-e053-d805fe0a8cb0/1963_5931_Fan_PhD.pdf
- scispace.com Spatially Resolved Galaxy Star Formation and Its Environmental Dependence. I. - SciSpace Opens in a new window — https://scispace.com/pdf/spatially-resolved-galaxy-star-formation-and-its-46ht1qzs80.pdf
- arxiv.org Compact Size, High $\Sigma$SFR: Defining Morphological Features of Ly$\alpha$-Emitters - arXiv Opens in a new window — https://arxiv.org/pdf/2501.07548
- academic.oup.com GAMA/DEVILS: cosmic star formation and AGN activity over 12.5 billion years | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/524/1/1448/7218570
- arxiv.org I. New constraints on cosmic reionisation from the luminosity and redshift-dependent fraction of Lyman-α emission - arXiv Opens in a new window — https://arxiv.org/pdf/1003.5244
- cambridge.org Lyman-α at cosmic noon I: Lyα spectral type selection of z ∼ 2 – 3 Lyman break galaxies with broadband imaging | Publications of the Astronomical Society of Australia Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/lyman-at-cosmic-noon-i-ly-spectral-type-selection-of-z-2-3-lyman-break-galaxies-with-broadband-imaging/24476AE89EB5CA3167F0E1EBB8AB5169
- arxiv.org Spectroscopically Complete Census of Obscured Cosmic Star Formation Rate Density at z=4-6 - arXiv Opens in a new window — https://arxiv.org/html/2412.06894v1
- osti.gov Pair-instability supernovae via collision runaway in young dense star clusters - OSTI Opens in a new window — https://www.osti.gov/servlets/purl/1564900
- scholarlypublications.universiteitleiden.nl High-Redshift Galaxy Surveys and the Reionization of the Universe Opens in a new window — https://scholarlypublications.universiteitleiden.nl/access/item%3A3214088/download
- academic.oup.com Physical properties of UDF12 galaxies in cosmological simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/440/1/731/9381393/stu265.pdf
- arxiv.org Combining high-z galaxy luminosity functions with Bayesian evidence - arXiv Opens in a new window — https://arxiv.org/pdf/1906.06296
- arxiv.org UV Spectral Slope and Nebular Dust Attenuation in Dwarf Galaxies at $1.4<z<2.6$ - arXiv Opens in a new window — https://arxiv.org/pdf/2510.00427
- mpia.de The Evolution of the Baryons Associated with Galaxies Averaged over Cosmic Time and Space Opens in a new window — https://www.mpia.de/5504464/walter_aspecs_2020.pdf
- arxiv.org arXiv:2208.02822v2 [astro-ph.GA] 16 Mar 2023 Opens in a new window — https://arxiv.org/pdf/2208.02822
- academic.oup.com The reversal of the SF–density relation in a ... - Oxford Academic Opens in a new window — https://academic.oup.com/mnrasl/article-pdf/447/1/L65/54652965/mnrasl_447_1_l65.pdf
- uhra.herts.ac.uk University of Hertfordshire Research Archive Opens in a new window — https://uhra.herts.ac.uk/id/eprint/6594/2/Published_Version.pdf
- arxiv.org arXiv:2101.04734v1 [astro-ph.GA] 12 Jan 2021 Opens in a new window — https://arxiv.org/pdf/2101.04734
- doi.org Physical properties of z > 4 submillimeter galaxies in the COSMOS field - DOI Opens in a new window — https://doi.org/10.1051/0004-6361/201424996
- academic.oup.com Tracing the cosmic growth of supermassive black holes to z ∼ 3 with Herschel - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/439/3/2736/1098853
- academic.oup.com ALMA REBELS Survey: the first infrared luminosity function measurement at z ∼ 7 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/522/3/3926/7143796
- doi.org Tracing obscured galaxy build-up at high redshift using deep radio surveys | Astronomy & Astrophysics (A&A) - DOI Opens in a new window — https://doi.org/10.1051/0004-6361/202346411
- ned.ipac.caltech.edu The Dawes Review 8: Measuring the Stellar Initial Mass Function - A. M. Hopkins Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Hopkins/Hopkins_refs.html
- academic.oup.com Herschel PEP/HerMES luminosity function – I. Probing the evolution of PACS selected Galaxies to z ≃ 4 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/432/1/23/1112664
- academic.oup.com Herschel PEP/HerMES luminosity function – I. Probing the evolution of PACS selected Galaxies to z ≃ 4 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-abstract/432/1/23/1112664
- researchprofiles.herts.ac.uk The Herschel PEP/HerMES luminosity function - I: Probing the Opens in a new window — https://researchprofiles.herts.ac.uk/en/publications/the-herschel-pephermes-luminosity-function-i-probing-the-evolutio/
- arxiv.org 1 Introduction - arXiv Opens in a new window — https://arxiv.org/html/2404.09673v1
- spiedigitallibrary.org New hope for obscured AGN: the PRIMA-NewAthena alliance - SPIE Digital Library Opens in a new window — https://www.spiedigitallibrary.org/journals/Journal-of-Astronomical-Telescopes-Instruments-and-Systems/volume-11/issue-03/031609/New-hope-for-obscured-AGN-the-PRIMA-NewAthena-alliance/10.1117/1.JATIS.11.3.031609.pdf
- orcid.org Linda Tacconi - ORCID Opens in a new window — https://orcid.org/0000-0002-1485-9401
- alpha-lyrae.co.uk Galaxy with largest red shift yet measured seen rapidly forming stars - Alpha Lyrae Opens in a new window — https://alpha-lyrae.co.uk/2013/10/23/galaxy-with-largest-red-shift-yet-measured-seen-rapidly-forming-stars/
- sciencedaily.com Astronomers discover the most distant known galaxy: Galaxy seen as it was just 700 million years after Big Bang | ScienceDaily Opens in a new window — https://www.sciencedaily.com/releases/2013/10/131023131800.htm
- analyticalscience.wiley.com Far, far away: A galaxy - 2013 - Wiley Analytical Science Opens in a new window — https://analyticalscience.wiley.com/content/article-do/far-far-away-galaxy
- scitechdaily.com Astronomers Discover and Confirm Most Distant Known Galaxy - SciTechDaily Opens in a new window — https://scitechdaily.com/astronomers-discover-confirm-distant-known-galaxy/
- sci.news Z8-GND-5296: Most Distant Galaxy Yet Discovered | Astronomy | Sci-News.com Opens in a new window — https://www.sci.news/astronomy/science-most-distant-galaxy-01488.html
- astronomy.utexas.edu Keely Finkelstein | Department of Astronomy Opens in a new window — https://astronomy.utexas.edu/directory/keely-finkelstein
- academic.oup.com An empirical model for the galaxy luminosity and star formation rate function at high redshift Opens in a new window — https://academic.oup.com/mnras/article-pdf/455/2/2101/18515328/stv2469.pdf
- openaccess.inaf.it On the Faint End of the Galaxy Luminosity Function in the Epoch of Reionization: Updated Constraints from the HST Frontier Opens in a new window — https://openaccess.inaf.it/bitstreams/60300436-5fe7-42f9-99f9-eabf18ca437a/download
- pas.va Star-formation in cosmic-dawn galaxies - The Pontifical Academy of Sciences Opens in a new window — https://www.pas.va/en/publications/scripta-varia/sv155pas/tacchella.html
- par.nsf.gov The impact of UV variability on the abundance of bright galaxies at z ≥ 9 - NSF PAR Opens in a new window — https://par.nsf.gov/servlets/purl/10477691
- arxiv.org Gamma-ray bursts reveal the history and faint contributors of cosmic reionization - arXiv Opens in a new window — https://arxiv.org/pdf/2607.07610
- boa.unimib.it The evolution of the galaxy stellar mass function and star formation rates in the colibre simulations from redshift 17 to 0 - Milano-Bicocca Opens in a new window — https://boa.unimib.it/retrieve/98382688-6c50-4573-b577-4fc16f82723f/Chaikin%20et%20al-2026-Monthly%20Notices%20of%20the%20Royal%20Astronomical%20Society-VoR.pdf
- academic.oup.com evolution of the galaxy stellar-mass function over the last 12 billion years from a combination of ground-based and HST surveys | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/503/3/4413/6169723
- physics-legacy.pbsci.ucsc.edu Star Formation Histories, Galaxy Mergers and Structural Properties - UCSC Physics Opens in a new window — https://physics-legacy.pbsci.ucsc.edu/~joel/Rodriguez-Puebla,Primack,Avilla-Reese,Faber-GalaxyHaloConnection-MNRAS%20submitted.pdf
- researchgate.net (PDF) Environmental Effects on the Stellar Mass Function in a z ∼ 3.3 Overdensity of Galaxies in the COSMOS Field* - ResearchGate Opens in a new window — https://www.researchgate.net/publication/401333177_Environmental_Effects_on_the_Stellar_Mass_Function_in_a_z_33_Overdensity_of_Galaxies_in_the_COSMOS_Field
- arxiv.org Do we understand the star formation history of the universe? - arXiv Opens in a new window — https://arxiv.org/html/2607.09848v1
- ned.ipac.caltech.edu Cosmic Star-Formation History - arXiv Opens in a new window — https://ned.ipac.caltech.edu/level5/March14/Madau/paper.pdf
- researchgate.net (PDF) Cosmic Star Formation History - ResearchGate Opens in a new window — https://www.researchgate.net/publication/260519491_Cosmic_Star_Formation_History
- academic.oup.com Estimating transient rates from cosmological simulations and BPASS - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/514/1/1315/6576337
- arxiv.org Extended Hernquist-Springel formalism for cosmic star formation - arXiv Opens in a new window — https://arxiv.org/pdf/2109.01146
- researchgate.net (PDF) Tracing Early Cosmic Chemical Enrichment: A Uniform XMM-Newton Survey of Metallicity in Galaxy Groups and Clusters - ResearchGate Opens in a new window — https://www.researchgate.net/publication/397824754_Tracing_Early_Cosmic_Chemical_Enrichment_A_Uniform_XMM-Newton_Survey_of_Metallicity_in_Galaxy_Groups_and_Clusters
- inaoep.mx The Star-forming Main Sequence and the Contribution of Dust-obscured Star Formation since z ∼ 4 from the Far-UV - INAOE Opens in a new window — https://www.inaoep.mx/~itziar/papers/2020Rodr%C3%ADguez-Puebla.pdf
- arxiv.org Tracing Early Cosmic Chemical Enrichment: A Uniform XMM-Newton Survey of Metallicity in Galaxy Groups and Clusters - arXiv Opens in a new window — https://arxiv.org/pdf/2511.16448
- indico.global Contribution to the cosmic γ-ray background radiation from star-forming galaxies - Indico Global Opens in a new window — https://indico.global/event/10103/contributions/97416/attachments/56343/108268/20250219%20ICEPP%20CHEN%20Junling%20-%20Junling%20CHEN.pdf
- sites.astro.caltech.edu Cosmic Star-Formation History - Caltech Astronomy Opens in a new window — https://sites.astro.caltech.edu/~george/ay21/readings/MadauDickinson_SFhistory_2014.pdf
- academic.oup.com Probing the initial mass function of the first stars with transients - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/511/2/2505/6516967
- academic.oup.com The star formation history of galaxies: the role of galaxy mass, morphology and environment - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/450/3/2749/1062169
- arxiv.org arXiv:2302.09763v2 [astro-ph.SR] 21 Apr 2023 Opens in a new window — https://arxiv.org/pdf/2302.09763
- nbi.ku.dk Evolution of the Rate of SNe IIn with Redshift Opens in a new window — https://nbi.ku.dk/english/theses/masters-theses/cecilie-cold_copy/Master_Thesis_CecilieHede.pdf
- ned.ipac.caltech.edu 5. From Observations To General Principles - Cosmic Star Formation History - Piero Madau & Mark Dickinson Opens in a new window — https://ned.ipac.caltech.edu/level5/March14/Madau/Madau5.html
- ned.ipac.caltech.edu measuring mass from light - Cosmic Star Formation History - Piero Madau & Mark Dickinson Opens in a new window — https://ned.ipac.caltech.edu/level5/March14/Madau/Madau3.html

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

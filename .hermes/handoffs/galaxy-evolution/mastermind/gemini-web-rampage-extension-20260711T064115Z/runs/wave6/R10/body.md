Rampage R10 answer — REQ_RAMPAGE_R10_20260711T064115Z

Run date (UTC): 2026-07-11T18:21:00Z
Model: Gemini 1.5 Pro
Harmonization rows: 5

Harmonization attempts table
Study (citation)	What was harmonized (velocity cut / n_e diagnostic / geometry / aperture / αCO / SFR calibration)	Input heterogeneity	Common system adopted	BEFORE value(s) ± unc	AFTER value(s) ± unc	Shift magnitude as stated by the source
Davies et al. 2020 [arXiv:2003.06153]	n_e diagnostic / geometry	Literature varied in assumed low-density limits and volume-filled spherical geometries.	Transauroral/ionization electron density; time-averaged thin shell geometry (C=1 UNCERTAINTY_NOT_QUOTED_BY_SOURCE).	Outflow rate based on uniform spherical geometry and n
e
	​

=200 cm$^{-3}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	0.001 to 0.5 M$_{\odot}$ yr$^{-1}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	Mass outflow rates lower by about a factor 3 UNCERTAINTY_NOT_QUOTED_BY_SOURCE.
Holden et al. 2025 [arXiv:2511.15791]	n_e diagnostic	Widespread reliance on 6717/6731 flux ratios assuming uniform low density limits across host galaxies.	Transauroral [O II]/ line diagnostic empirical correction applied across the sample.	log
10
	​

(n
e
	​

[cm
−3
])∼2.0−3.5 UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	Electron densities increased by approximately a factor of 6 UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	Factor-of-6 UNCERTAINTY_NOT_QUOTED_BY_SOURCE decrease in derived mass outflow rates and kinetic powers.
Lutz et al. 2020 [arXiv:1911.05608]	geometry	Diverse CO millimeter interferometric maps and OH infrared spectroscopic absorption derivations.	C=1 UNCERTAINTY_NOT_QUOTED_BY_SOURCE geometric scaling factor.	OH-based spectroscopic outflow modeling UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	CO-based interferometric outflow derivations UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	80% UNCERTAINTY_NOT_QUOTED_BY_SOURCE agreement in detecting v
out
	​

≳150 km s$^{-1}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE outflows; modest remaining differences ascribed to geometry.
Holden & Tadhunter 2024 [arXiv:2411.17500]	aperture / beam smearing	Uncorrected ground-based integral field unit (IFU) atmospheric seeing across survey fields.	Explicit Point Spread Function (PSF)-subtraction and beam-smearing correction forward-modeling.	Extended galaxy-wide outflows measured at r>5 kpc UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	Compact nuclear outflows restricted to r∼100 pc UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	Mass outflow rates and kinetic powers overestimated by orders of magnitude UNCERTAINTY_NOT_QUOTED_BY_SOURCE.
Sun et al. 2018 [arXiv:1809.02604]	aperture correction	BOSS fibers of 2 arcsec UNCERTAINTY_NOT_QUOTED_BY_SOURCE versus SDSS fibers of 3 arcsec UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	Statistical calibration utilizing the mid-infrared L
[OIII]
	​

-L
bol,15μm
	​

 correlation anchor.	Inhomogeneous and uncorrected L
[OIII]
	​

 spectral measurements UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	Aperture-corrected L
[OIII]
	​

 values for the BOSS sub-population UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	Aperture correction of 0.7 dex UNCERTAINTY_NOT_QUOTED_BY_SOURCE applied to the BOSS sample.
Aperture and beam corrections

Published methodologies for cross-calibrating physical apertures across disparate instrumentation indicate that geometric standardizations fundamentally shift derived active galactic nucleus (AGN) outflow profiles. The integration of spectroscopic fluxes from varying instrumental architectures requires intensive harmonization to ensure that extended emission-line regions (EELRs) are not artificially truncated or disproportionately represented. When comparing spectroscopic fiber constraints across large-scale digital sky surveys, Sun et al. 2018 [arXiv:1809.02604] document that the Baryon Oscillation Spectroscopic Survey (BOSS) utilizes a 2 arcsec UNCERTAINTY_NOT_QUOTED_BY_SOURCE fiber aperture, whereas the legacy Sloan Digital Sky Survey (SDSS) spectrum utilizes a 3 arcsec UNCERTAINTY_NOT_QUOTED_BY_SOURCE aperture. Because EELRs and the associated warm ionized gas reservoirs frequently exceed the physical footprint of the spectroscopic aperture at typical local redshifts (z∼0.05 UNCERTAINTY_NOT_QUOTED_BY_SOURCE), extracting commensurate luminosities requires sophisticated statistical aperture corrections. By anchoring the data against the mid-infrared L
[OIII]
	​

-L
bol,15μm
	​

 relation (applying a bolometric correction factor of 9 UNCERTAINTY_NOT_QUOTED_BY_SOURCE to infer L
bol,15μm
	​

), Sun et al. calculate that the L
[OIII]
	​

 fluxes extracted from the Yuan et al. 2016 BOSS sample require a [commensurable shift within study] aperture correction of 0.7 dex UNCERTAINTY_NOT_QUOTED_BY_SOURCE to align with the broader SDSS framework.

Similar aperture matching paradigms are documented in broadband photometric studies of host galaxies. Kubo et al. 2022 apply an explicit aperture correction to Infrared Array Camera (IRAC) 3.6–8.0 μm photometry by matching images to the Ks-band via a 2.0 arcsec UNCERTAINTY_NOT_QUOTED_BY_SOURCE diameter aperture. The researchers subsequently adjust the Point Spread Function (PSF) matched photometries by scaling the total Kron flux measured on the imaging array to the aperture photometry ratio derived in the Ks band.

In the realm of integral field unit (IFU) surveys, spatial decomposition is heavily contaminated by atmospheric beam smearing, prompting published re-reductions to quantify the severe magnitude of this observational artifact. Ground-based spectroscopy without optimal adaptive optics is subject to atmospheric turbulence, which effectively smears bright, compact nuclear emission across adjacent spatial pixels (spaxels). Holden & Tadhunter 2024 [arXiv:2411.17500] explicitly harmonize Very Large Telescope Multi Unit Spectroscopic Explorer (VLT/MUSE) data of the type-2 quasar and ultraluminous infrared galaxy (ULIRG) F13451+1232 by implementing a rigorous PSF-subtraction routing to correct for ambient seeing conditions. The study highlights that atmospheric seeing acts to smear the compact nuclear outflow emission over a radial distance of r>3.5 arcsec UNCERTAINTY_NOT_QUOTED_BY_SOURCE, a distance which corresponds to at least 8 UNCERTAINTY_NOT_QUOTED_BY_SOURCE times the half-width at half-maximum (HWHM) of the observational seeing disc (HWHM = 0.40±0.10 arcsec).

By analyzing two divergent cases—one incorporating the full beam smearing forward-model correction and one omitting it entirely—the authors state a [commensurable shift within study] finding that failure to correct the raw data leads directly to mass outflow rates and kinetic powers of spatially-extended emission being overestimated by orders of magnitude UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The spatial footprint itself shrinks dramatically under this harmonization process, moving from an uncorrected apparent scale of a "galaxy-wide" wind at r>5 kpc UNCERTAINTY_NOT_QUOTED_BY_SOURCE to a true physical scale tightly restricted to the central ∼100 pc UNCERTAINTY_NOT_QUOTED_BY_SOURCE of the AGN environment. Speranza et al. 2024 [arXiv:2311.10132] document support for this rigorous limitation on ground-based IFU radii; the authors note that when seeing-limited data of local type-2 quasars (QSO2s) is cautiously modeled, the genuine spatially resolved ionized outflows fall into compact radii spanning 3.1 to 12.6 kpc UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

In the sub-millimeter regime for cold-gas mapping, aperture and primary beam corrections similarly modulate the integration of flux across host galaxy environments. When harmonizing rotational carbon monoxide (CO) measurements, Lutz et al. 2020 [arXiv:1911.05608] highlight that uncorrected single-dish arrays and disparate interferometric uv-coverages inject systemic uncertainties into the observed spatial structures. Re-analysis of Atacama Large Millimeter/submillimeter Array (ALMA) CO(6-5) maps by various authors adopts a standard 'briggs' weighting (utilizing a robustness parameter of +0.5 UNCERTAINTY_NOT_QUOTED_BY_SOURCE) and applies a rigorous primary beam correction on the restored images to normalize the natural field-of-view sensitivity decay. This specific correction boosts the measured flux density at the edges of the image by less than 1 per cent UNCERTAINTY_NOT_QUOTED_BY_SOURCE, indicating that while necessary for absolute precision, the primary beam correction in compact ALMA mappings exerts a relatively minor energetic shift compared to optical IFU beam smearing.

Incidence rates of these corrections across large samples show consistent, quantifiable distributions that govern statistical modeling. In the study of merging spiral galaxies, the [z < 0.2][star-forming][local merger][CO phase] incidence of aperture corrections falling below a value of 2 UNCERTAINTY_NOT_QUOTED_BY_SOURCE is 91 per cent UNCERTAINTY_NOT_QUOTED_BY_SOURCE (with 60 per cent UNCERTAINTY_NOT_QUOTED_BY_SOURCE of the total sample registering below a correction factor of 1.5 UNCERTAINTY_NOT_QUOTED_BY_SOURCE). These incidence metrics indicate that the systematic offsets typically remain securely confined within a factor of 2 unless severe nuclear beam-smearing artificially flattens the optical surface brightness profile.

Density and conversion diagnostics

A primary focal point of measurement harmonization centers on the specific electron density (n
e
	​

) diagnostics deployed to map the physical state of the ionized outflowing gas. Historically, large multi-wavelength compilations scaled their calculated outflow masses by utilizing the traditional 6717/6731 emission-line doublet flux ratio. However, recent literature standardizes against alternative atomic diagnostics due to the fundamental physical limitation that the doublet saturates heavily at a critical density of n
crit
	​

∼10
3.5
 cm$^{-3}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE. Because the lines are primarily emitted close to the ionization front at the outermost edges of the gas clouds where the local electron density decreases precipitously, they systematically underpredict the true bulk density of the outflowing medium.

Holden et al. 2025 [arXiv:2511.15791] apply a robust cross-calibration to rectify this shortfall, utilizing the higher-critical-density transauroral (TR) [O II] 3726+3729/7319+7330 and 4068+4076/6717+6731 line ratios against SDSS spectroscopy of the Quasar Feedback (QSOFEED) sample, which consists of 48 UNCERTAINTY_NOT_QUOTED_BY_SOURCE nearby type-2 quasars. The atomic properties of these transauroral transitions permit sensitivity to substantially higher densities than the standard optical doublets. The analysis identifies a persistent [commensurable shift within study] offset in historical data, formulating an empirical correction designed specifically for archival-based measurements: log
10
	​

(n
e,outflow
	​

[cm
−3
])=log
10
	​

(n
e,
	​

[cm
−3
])+0.75±0.07.

For a baseline measured density of log
10
	​

(n
e
	​

[cm
−3
])=3 UNCERTAINTY_NOT_QUOTED_BY_SOURCE, applying this correction induces a [commensurable shift within study] increase in the true gas density by approximately a factor of 6 UNCERTAINTY_NOT_QUOTED_BY_SOURCE. Because derived mass outflow rates and their associated kinetic powers scale inversely with the assumed electron density, this density revision directly corresponds to a factor-of-6 UNCERTAINTY_NOT_QUOTED_BY_SOURCE decrease in the resultant mass outflow rates and kinetic powers assigned to the AGN feedback mechanism.

Davies et al. 2020 [arXiv:2003.06153] note a strikingly similar impact during their analysis of the Local Luminous AGN with Matched Analogues (LLAMA) survey. When utilizing transauroral lines (as originally developed by Holt et al. 2011) or ionization-parameter-based modeling (as developed by Baron & Netzer 2019 [arXiv:1903.11076], which yields local densities of n
e
	​

∼10
4.5
 cm$^{-3}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE), the newly derived densities are 1 to 1.5 orders of magnitude UNCERTAINTY_NOT_QUOTED_BY_SOURCE higher than standard historical estimates. Applying these corrected densities drives the warm ionized mass outflow rates down to values between 0.001 and 0.5 M$_{\odot}$ yr$^{-1}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

In the infrared spectrum, Ramos Almeida et al. 2025 [arXiv:2511.15791] support these elevated density calibrations by analyzing mid-infrared spectroscopy of five UNCERTAINTY_NOT_QUOTED_BY_SOURCE objects within the QSOFEED sample. The authors note that the densities derived from the flux ratio of the high-critical-density, high-ionization [Ne V] 14.3, 24.3 μm fine-structure emission lines are highly comparable to those derived from the transauroral lines, further invalidating the low-density assumptions.

In the cold molecular phase, energetic harmonization relies strictly on assumptions regarding the CO-to-H$2$ conversion factor ($\alpha{CO}), which dictates the total available gas reservoir. Lutz et al. 2020 [arXiv:1911.05608] and Fluetsch et al. 2019 [arXiv:1805.05352] extensively re-reduce local galaxy literature by enforcing a homogeneous conversion factor of $\alpha_{CO(1-0)} = 0.8$ `UNCERTAINTY_NOT_QUOTED_BY_SOURCE`, an assumption considered appropriate for ULIRG-like and dense AGN environments, rather than adopting higher Milky Way galactic disk values. Additionally, they standardize the brightness temperature ratios utilizing values calibrated by Bothwell et al. 2013 [arXiv:1210.1536] (e.g., deploying $R_{31} = 1.35 \pm 0.23$ or $R_{21} = 0.66 \pm 0.15$ for specific local sources) to map higher-J transitions down to the foundational CO(1-0) energetic state. When cross-validating these CO-interferometric derived outflow properties against entirely independent Herschel OH-based far-infrared P-Cygni absorption measurements, Lutz et al. report a [commensurable shift within study] 80 per cent `UNCERTAINTY_NOT_QUOTED_BY_SOURCE` agreement in detecting outflows operating with $v_{out} \gtrsim 150$ km s^{-1}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

Regarding geometrical conversion diagnostics, both Fluetsch et al. 2019 and Davies et al. 2020 emphasize the stark variance introduced by assumed macroscopic outflow geometries. A time-averaged thin-shell geometry dictates a multiplication factor of C=1 UNCERTAINTY_NOT_QUOTED_BY_SOURCE. In contrast, assuming a volume-filled spherical or multi-conical geometry implies a factor of C=3 UNCERTAINTY_NOT_QUOTED_BY_SOURCE. Re-deriving literature measurements from a historical spherical assumption down to a physically motivated thin-shell approximation enforces a direct [commensurable shift within study] decrease in the calculated mass outflow rate by a factor of 3 UNCERTAINTY_NOT_QUOTED_BY_SOURCE, fundamentally altering the perceived efficiency of the AGN feedback cycle.

Velocity-cut and decomposition conventions

The kinematic boundary conditions defining what physical material actually constitutes an "outflow" heavily manipulate the final integrated energetic yield. Velocity-cut sensitivities are fundamentally tied to non-parametric representations of the emitting gas line profiles, as decoupling turbulent galactic rotation from genuine AGN-driven expulsion remains highly complex.

A recurrent threshold detailed in the compiled literature dictates that the cold phase properties are extremely sensitive to the minimum radial velocity cut (v
min
	​

) chosen by the analyst. If a strict kinematic velocity cut is enforced on the observed data cubes, such as artificially removing all gas tracing v
helio
	​

<−100 km s$^{-1}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE, the baseline integrals for mass flux shift drastically. To separate true expelled outflows from highly turbulent but gravitationally bound interstellar medium (ISM) gas, Holden et al. 2025 [arXiv:2511.15791] implement a highly conservative kinematic decomposition strategy: only gas exhibiting velocities below the 5th percentile (V
05
	​

) and above the 95th percentile (V
95
	​

) is attributed to the outflow. The authors contrast this rigorous approach against broader legacy conventions that routinely integrated all gas exhibiting velocities greater than 1.5 UNCERTAINTY_NOT_QUOTED_BY_SOURCE times the full width at half-maximum (FWHM) of the host galaxy's stellar absorption features.

When tracking energetic footprints across expansive samples, Speranza et al. 2024 [arXiv:2311.10132] use the non-parametric W
80
	​

 width, defined mathematically as the velocity width containing 80 per cent UNCERTAINTY_NOT_QUOTED_BY_SOURCE of the total emission line flux. Outflows are functionally defined to exist when W
80
	​

>500 km s$^{-1}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE and the spatial profile deviates significantly from the underlying gravitational potential of the host. Re-analysis simulating line-of-sight (LOS) velocity cuts on synthetic hydrodynamic data cubes states a [commensurable shift within study] finding that for galaxy inclination angles of 60°–70° UNCERTAINTY_NOT_QUOTED_BY_SOURCE, the conversion factor between the true physical mass outflow rate and the observationally derived mass outflow rate is approximately 10 UNCERTAINTY_NOT_QUOTED_BY_SOURCE. Furthermore, the discrepancy for the momentum outflow rate under the same simulated observational constraints reaches an astonishing factor of 200 UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

To prevent improper blending with complex galactic rotation curves or central stellar bars, Lutz et al. 2020 explicitly focus their integration limits solely on the fast wings situated completely outside the line core of the host galaxy. This choice deliberately circumvents ambiguities between moderate velocity flows and non-circular gravitational motions. In complex, face-on geometries, relying merely on a median velocity of the spatial map rather than analyzing the dispersion outskirts overestimates the intrinsic velocity dispersion (σ
0
	​

) by almost a factor of 2 UNCERTAINTY_NOT_QUOTED_BY_SOURCE, artificially inflating the kinetic energy budget.

Incidence metrics governed by these specific velocity boundaries reflect the ubiquitous nature of the outflow phenomenon when standardized thresholds are applied: the [z < 0.45][dwarf galaxy][O III phase] broad-component outflow incidence is highly ubiquitous at 78 per cent UNCERTAINTY_NOT_QUOTED_BY_SOURCE. Similarly, targeting more massive systems, the [z < 0.3][AGN][radio-detected][ionized phase] outflow detection rate reaches 67.2±3.4 per cent, indicating a statistically higher prevalence than the 44.6±2.7 per cent rate observed utilizing the exact same kinematic cuts in a control sample of radio non-detected AGN.

Residual irreducibles

Despite strict, multi-wavelength harmonization of electron densities, macroscopic geometries, and instrument apertures, systemic irreducible spreads persist across all major meta-analyses, preventing an absolute consensus on the ultimate efficiency of AGN feedback. The literature notes several fundamental barriers that resist parameter normalization.

A primary irreducible source of scatter arises from geometric projection effects on the observed outflow radius and velocity. Fluetsch et al. 2019 [arXiv:1805.05352] argue that since outflow orientations are distributed randomly with respect to the line of sight of the observer, the average geometric correction factor for a large sample asymptotically approaches unity. However, for any individual object subject to dedicated follow-up, these projection effects and localized, highly turbulent density fluctuations impose a strict residual uncertainty of ∼0.3 dex UNCERTAINTY_NOT_QUOTED_BY_SOURCE on the mass outflow rate calculation.

Furthermore, Davies et al. 2020 [arXiv:2003.06153] highlight the inherent hazards of enforcing a uniform parameter to artificially minimize data scatter across heterogeneous samples. Specifically, examining the widely cited Fiore et al. 2017 scaling relation (which spans five orders of magnitude in bolometric luminosity), Davies notes that the historical study achieved a seemingly tight scatter of 0.67 dex UNCERTAINTY_NOT_QUOTED_BY_SOURCE partly by applying an identical, assumed electron density of n
e
	​

=200 cm$^{-3}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE to all targeted objects. When Davies et al. substitute these uniform assumptions with object-specific densities derived from individual transauroral or ionization calculations, the low-luminosity AGN data points scatter dramatically and fall well below where one would expect from the idealized correlation line. Thus, the apparent tightness of legacy scaling relations contains an irreducible masking of true physical variance. The [non-commensurable cross-study shift] between the Fiore universal-density curve and the Davies true-density distribution shows mass rates systematically offset by significantly lower values when authentic, higher densities are inputted into the energetic equations.

Additional irreducible uncertainty is injected directly via bolometric corrections, which are notoriously difficult to standardize across obscured AGN populations. Speranza et al. 2024 [arXiv:2311.10132] attribute up to ∼1 dex UNCERTAINTY_NOT_QUOTED_BY_SOURCE of energetic uncertainty directly to the systematic errors inherent in calculating the total bolometric luminosity (L
bol
	​

) via L
14−195keV
	​

 X-ray transformations (which frequently multiply the X-ray flux by an assumed, non-varying factor of 7.42 UNCERTAINTY_NOT_QUOTED_BY_SOURCE) or via spectral energy distribution (SED) fitting. This immutable 1 dex uncertainty irreversibly impacts the momentum ratio (
P
˙
out
	​

/(L
bol
	​

/c)) and the overall energy coupling efficiency (
E
˙
out
	​

/L
bol
	​

). Consequently, even perfectly resolved IFU outflow measurements will yield a 1 dex spread when plotted against theoretical AGN energy injection benchmarks.

Finally, phase mismatch remains a fundamental observational barrier. Molecular mass outflow rates are on average 2 to 3 times UNCERTAINTY_NOT_QUOTED_BY_SOURCE larger than warm ionized mass outflow rates in locally matched samples (e.g., the QSO2s). When cross-calibrating the multi-phase scaling relations, the expected gap between the two distinct gas phases at the bolometric luminosities of the targeted QSO2s is projected to be almost two orders of magnitude UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The current inability to simultaneously and perfectly measure the hot X-ray plasma, warm ionized gas, neutral atomic clouds, and cold molecular phases ensures that the total mass-loading factor (η) retains an irreducible lower-bound limit, as undetected mass invariably resides in unmapped thermal phases.

Recipes the literature converges on

A clear, rigorously defined set of common-reporting standards is explicitly proposed across the modern astrophysical literature to prevent the historical divergence in AGN outflow properties and to ensure future cross-study commensurability.

Standardized Electron Density Diagnostics: The literature overwhelmingly proposes completely abandoning the traditional 6717/6731 ratio for calculating AGN outflow mass. Davies et al. 2020, Kakkad et al. 2020, and Holden et al. 2025 explicitly advocate for the immediate adoption of the transauroral (TR) method—utilizing [O II] 3726+3729/7319+7330 or 4068+4076/6717+6731—due strictly to its sensitivity to the higher critical densities (10
3
<n
e
	​

<10
5.5
 cm$^{-3}$ UNCERTAINTY_NOT_QUOTED_BY_SOURCE) characteristic of shock-heated, AGN-driven gas. If legacy standard spectra lack these crucial high-ionization lines, Holden et al. 2025 instruct researchers to apply an explicit, mathematically derived correction of +0.75±0.07 dex to the logged density prior to deriving kinetic powers.

Time-Averaged Thin Shell Geometry (C=1): To achieve parity between highly disparate multi-wavelength molecular and ionized samples, modern compilations by Fluetsch et al. 2019 and Lutz et al. 2020 uniformly converge on utilizing the time-averaged thin-shell approximation. This specific geometric model yields a conversion factor of C=1 UNCERTAINTY_NOT_QUOTED_BY_SOURCE. This is explicitly proposed as a far more realistic physical limit than the uniform filling factor (C=3 UNCERTAINTY_NOT_QUOTED_BY_SOURCE) characteristic of a perfectly spherical or multi-conical volume, preventing the artificial inflation of momentum rates that plagued earlier studies.

Explicit Beam-Smearing Deconvolution: For ground-based IFU data subject to atmospheric turbulence, Holden et al. 2024 and Speranza et al. 2024 propose that all future reporting routines must apply rigorous PSF-subtraction and beam-smearing forward-model corrections before estimating final outflow radii (R
out
	​

). Measurements of radial extents merely exceeding the HWHM of the ambient seeing disc are no longer accepted as genuinely spatially resolved without forward-modeling the atmospheric dispersion, to strictly avoid overestimating mass rates by orders of magnitude.

Unified Molecular Conversions: Lutz et al. 2020 explicitly propose fixing α
CO(1−0)
	​

=0.8 UNCERTAINTY_NOT_QUOTED_BY_SOURCE for local ULIRG and AGN environments, rejecting the varied values used in legacy disk studies. Furthermore, they support standardizing higher-J CO transitions using empirical brightness temperature ratios (e.g., as derived by Bothwell et al. 2013) to anchor all multi-level molecular mass outflow rate comparisons (
M
˙
out
	​

) securely back to the foundational CO(1-0) energetic state.

Links ledger

Davies et al. 2020 | arXiv:2003.06153 | QUARANTINED_PENDING_LOCAL_CHECK
Holden et al. 2025 | arXiv:2511.15791 | QUARANTINED_PENDING_LOCAL_CHECK
Lutz et al. 2020 | arXiv:1911.05608 | QUARANTINED_PENDING_LOCAL_CHECK
Holden & Tadhunter 2024 | arXiv:2411.17500 | QUARANTINED_PENDING_LOCAL_CHECK
Speranza et al. 2024 | arXiv:2311.10132 | QUARANTINED_PENDING_LOCAL_CHECK
Fluetsch et al. 2019 | arXiv:1805.05352 | QUARANTINED_PENDING_LOCAL_CHECK
Sun et al. 2018 | arXiv:1809.02604 | QUARANTINED_PENDING_LOCAL_CHECK
Baron & Netzer 2019 | arXiv:1903.11076 | QUARANTINED_PENDING_LOCAL_CHECK
Bothwell et al. 2013 | arXiv:1210.1536 | QUARANTINED_PENDING_LOCAL_CHECK
Kakkad et al. 2020 | DOI:10.1051/0004-6361/202039077 | QUARANTINED_PENDING_LOCAL_CHECK
Kubo et al. 2022 | DOI:10.3847/1538-4357/ac7e64 | QUARANTINED_PENDING_LOCAL_CHECK
Yuan et al. 2016 | MNRAS 411, 1035 | QUARANTINED_PENDING_LOCAL_CHECK
Fiore et al. 2017 | UNCITED_NOT_USABLE | QUARANTINED_PENDING_LOCAL_CHECK
Holt et al. 2011 | MNRAS 412, 2163 | QUARANTINED_PENDING_LOCAL_CHECK
Ramos Almeida et al. 2025 | arXiv:2511.15791 | QUARANTINED_PENDING_LOCAL_CHECK

GEMINI_WEB_RAMPAGE_R10_OUTPUT_DONE_20260711T064115Z

# Review Base 10 raw Deep Research packet — Conroy 2013

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_16_carilli_walter_2013_DR_PROMPT.md`
Prompt SHA-256: `35e85f005d6b2adbe75f278356e58d6036c90c9c8273534224f16b0e7c54c7ec`
Conversation ID: `000c2e2b24c137b0`
Submit UTC: `2026-07-16T05:39:21.804034Z`
Research Start UTC: `2026-07-16T05:40:01.051893Z`
Result captured UTC: `2026-07-16T05:54:12.404232Z`
Raw result SHA-256: `58ebbe8e4155ce1a047f3d5fbe490a428529a5246307044717485a0cc554e3bf`

## Deep Research review-base result

Deep Research Source-Base Review: Cool Gas in High-Redshift Galaxies
Review Identity and Scope Map

The synthesis document under review is the seminal paper authored by C. L. Carilli and F. Walter, published in the Annual Review of Astronomy and Astrophysics (Volume 51, 2013, pages 105-161), titled "Cool Gas in High-Redshift Galaxies". The verified digital object identifier is 10.1146/annurev-astro-082812-140953, the arXiv identifier is 1301.0371, and the ADS bibcode is 2013ARA&A..51..105C. Operating strictly as an advisory and secondary analytical framework, this review synthesizes the pre-2013 observational ledger of the cold interstellar medium (ISM) across the first several billion years of cosmic history, relying predominantly on interferometric data from the IRAM Plateau de Bure Interferometer (PdBI), the Very Large Array (VLA), and the Submillimeter Array (SMA).   

The primary scientific boundary of this synthesis focuses on the baryonic evolution of galaxies at redshift z>1. The analysis examines the physical states of cold molecular hydrogen (H$_2$)—traced primarily through rotational transitions of carbon monoxide (CO)—and the cooling mechanisms of the atomic gas phase, tracked via far-infrared (FIR) fine-structure lines such as [CII] 158 μm and [CI]. A fundamental structural component of the review is the strict segregation of high-redshift galaxies into distinct evolutionary populations to prevent the conflation of disparate physical states. These populations include hyper-luminous quasi-stellar object (QSO) host galaxies, highly star-forming submillimeter galaxies (SMGs) detected via blank-field FIR mapping, and typical main-sequence color-selected star-forming galaxies (CSGs) isolated via BzK or Lyman-break criteria.   

To accurately contextualize these populations within the theoretical framework of the galaxy main sequence, it is critical to map their positions on the Star Formation Rate (SFR) versus Stellar Mass plane. Color-Selected Galaxies (CSGs) form the linear diagonal band known as the main sequence, characterized by extended rotating disks where star formation proceeds steadily. In contrast, Submillimeter Galaxies (SMGs) and Quasar (QSO) hosts cluster significantly above this main sequence band as hyper-starbursts, characterized by compact, merger-driven geometries. This taxonomic distinction directly dictates the application of physical conversion factors: CSGs require a high, Milky Way-like CO-to-H$2$ conversion factor ($\alpha{CO} \approx 4.0\ M_\odot\ (K\ km\ s^{-1}\ pc^2)^{-1}),whereasthehyper−starburstSMGandQSOpopulationsrequireasignificantlylowerconversionfactor(\alpha_{CO} \approx 0.8\ M_\odot\ (K\ km\ s^{-1}\ pc^2)^{-1}$) due to their highly turbulent, continuous gas geometries.   

Throughout the synthesis, extracted measurements meticulously preserve necessary physical dependencies, including CO excitation corrections (r
J1
	​

), the standard 1.36 helium mass fraction multiplier for total gas mass, initial mass function (IMF) assumptions, and rigorous ΛCDM cosmology conventions (H
0
	​

=71 km s$^{-1}$ Mpc$^{-1}$, Ω
m
	​

=0.27, Ω
Λ
	​

=0.73).   

Established Findings

The following findings represent the stabilized consensus synthesized from the pre-2013 literature base, extracted with strict adherence to population boundaries and conversion mechanics.

REV16-E01 [Cosmic Evolution of Molecular Gas Fractions]
Epistemic Type: Established observational trend.
Bounded Statement: In massive, color-selected star-forming disk galaxies (CSGs) residing on the main sequence, the molecular gas fraction evolves profoundly over cosmic time. Defined rigorously as f
gas
	​

=M
gas
	​

/(M
gas
	​

+M
star
	​

), the fraction rises from baseline values of ∼5−10% in the local universe (z≈0) to approximately 40−50% at z≥1.5. Consequently, the direct ratio of molecular gas mass to stellar mass (M
gas
	​

/M
star
	​

) increases by a full order of magnitude—from roughly 0.1 at z=0 to near 1.0 at cosmic noon—indicating that the peak of cosmic star formation density was fueled by gas-dominated, rather than stellar-dominated, galactic disks.
Population/Tracer/Regime: CSGs / CO low-J transitions / Secular disk evolution.
Confidence: High.
Source Keys: Daddi et al. (2010a), Tacconi et al. (2010).   

REV16-E02 [The Bimodal Kennicutt-Schmidt Star Formation Law]
Epistemic Type: Established empirical scaling relation.
Bounded Statement: The scaling relationship linking star formation rate surface density (Σ
SFR
	​

) to molecular gas surface density (Σ
gas
	​

) separates into two distinct empirical sequences. CSGs occupy a lower-efficiency, long-depletion-time sequence analogous to local spiral galaxies. Conversely, SMGs and QSO hosts define a parallel, higher-efficiency sequence shifted to higher Σ
SFR
	​

 for a given gas mass, necessitating rapid gas consumption.
Population/Tracer/Regime: Global populations / CO and FIR continuum / Disk vs. Merger dichotomy.
Confidence: High.
Source Keys: Genzel et al. (2010), Daddi et al. (2010b).   

REV16-E03 [The α
CO
	​

 Conversion Factor Dichotomy]
Epistemic Type: Calibrated physical constant constraint.
Bounded Statement: The conversion of CO(1-0) line luminosity (L
CO
′
	​

) to total molecular hydrogen mass (M
H
2
	​

	​

) cannot be governed by a universal constant. The synthesis enforces a rigid dichotomy: extreme starbursts (SMGs, QSOs) require a low conversion factor of α
CO
	​

≈0.8 M
⊙
	​

 (K km s
−1
 pc
2
)
−1
 due to turbulent, highly dispersed gas unbound by individual giant molecular clouds (GMCs). Main-sequence CSGs require a high conversion factor of α
CO
	​

≈4.0 M
⊙
	​

 (K km s
−1
 pc
2
)
−1
, reflecting self-gravitating, discrete GMCs similar to the Milky Way. Both constants incorporate a 1.36 mass correction for helium.
Population/Tracer/Regime: All high-z populations / CO / Dynamical mass cross-constraints.
Confidence: High.
Source Keys: Downes & Solomon (1998), Tacconi et al. (2010).   

REV16-E04 [Differential CO Excitation Ladders]
Epistemic Type: Spectroscopic gas condition measurement.
Bounded Statement: The rotational Spectral Line Energy Distribution (SLED) of the CO molecule varies profoundly across galaxy populations, tracing local ISM kinetic temperature (T
kin
	​

) and density (n
H
2
	​

	​

). QSO hosts exhibit the highest excitation, peaking near J=6, indicating ultra-dense (log(n
H
2
	​

	​

)=3.6−4.3 cm
−3
) and warm (T
kin
	​

=40−60 K) conditions. SMGs show intermediate excitation peaking at J=3 or 4. CSGs show the lowest excitation, displaying a rapid drop-off in high-J transitions that closely mirrors the cool, thermalized conditions of the Milky Way inner disk.
Population/Tracer/Regime: All high-z populations / CO J-transitions / LTE and LVG modeling.
Confidence: High.
Source Keys: Weiß et al. (2007), Dannerbauer et al. (2009).   

REV16-E05 [[CII] as an Optimal Dynamical Tracer at Extreme Redshifts]
Epistemic Type: Established observational utility.
Bounded Statement: The 158 μm fine-structure transition of singly ionized carbon ([CII]) serves as the paramount tracer for determining precise spectroscopic redshifts and resolving internal gas dynamics (rotation, dispersion, dynamical mass) of the earliest galaxies (z>4). Its extreme intrinsic brightness allows it to overcome both the cosmological dimming and the elevated cosmic microwave background (CMB) contrast issues that plague low-J CO transitions.
Population/Tracer/Regime: Reionization-era QSOs and starbursts / [CII] / Interferometric kinematics.
Confidence: High.
Source Keys: Walter et al. (2003), Maiolino et al. (2009).   

REV16-E06 [Compact 'Maximal Starburst' Cores in Quasar Hosts]
Epistemic Type: Morphological and dynamical constraint.
Bounded Statement: High-resolution mapping of molecular gas and [CII] in z∼6 quasar host galaxies reveals highly compact emitting regions (radii <1−3 kpc) supporting extreme star formation rates (∼1000 M
⊙
	​

/yr). These environments match the theoretical limits of a "maximal starburst," where radiation pressure on dust grains balances self-gravity, occurring coevally with Eddington-limited supermassive black hole accretion.
Population/Tracer/Regime: z∼6 QSOs / CO and [CII] / Sub-kpc resolution imaging.
Confidence: High.
Source Keys: Walter et al. (2009), Wang et al. (2010).   

REV16-E07 [The High-Luminosity [CII]/FIR Deficit]
Epistemic Type: Established observational anomaly.
Bounded Statement: As the far-infrared (FIR) luminosity of a high-redshift system increases beyond 10
12
L
⊙
	​

, the ratio of [CII] line luminosity to total FIR continuum luminosity (L
[CII]
	​

/L
FIR
	​

) drops by an order of magnitude or more relative to local, lower-luminosity galaxies. While [CII] is highly luminous in absolute terms, it becomes an inefficient fractional coolant in extreme starbursts.
Population/Tracer/Regime: SMGs and QSOs / [CII] and FIR continuum / PDR cooling budgets.
Confidence: High.
Source Keys: Stacey et al. (2010).   

REV16-E08 [Neutral Atomic Carbon ([CI]) as an Alternative Mass Tracer]
Epistemic Type: Methodological validation.
Bounded Statement: The fine-structure transitions of neutral atomic carbon, specifically CI at 492 GHz and CI at 809 GHz, trace the bulk molecular hydrogen mass with an efficacy matching or exceeding that of CO(1-0). Due to generally optically thin conditions and minimal sensitivity to cosmic ray destruction, the [CI]-to-H$2$ conversion ratio remains highly stable, with the luminosity ratio $L'{CI(1-0)}/L'_{CO(1-0)}$ averaging ∼0.29±0.12 across high-z SMGs and QSOs.
Population/Tracer/Regime: SMGs and QSOs / [CI] / PDR distribution models.
Confidence: High.
Source Keys: Walter et al. (2011), Papadopoulos et al. (2004).   

REV16-E09 [Evidence for AGN-Driven Molecular Outflows]
Epistemic Type: Dynamical detection.
Bounded Statement: Spectroscopic profiles of high-J CO transitions and [CII] emission in massive quasar hosts (e.g., SDSS J1148+5251 at z=6.42) exhibit broad velocity wings indicating massive, high-velocity (≥1000 km/s) outflows of cool gas. These outflows carry sufficient kinetic energy and mass to rapidly deplete the host galaxy's cold gas reservoir, constituting direct observational evidence for negative AGN feedback clearing the ISM.
Population/Tracer/Regime: High-z QSOs / [CII] and CO wings / AGN feedback.
Confidence: Moderate to High.
Source Keys: Maiolino et al. (2012).   

REV16-E10 [Morphological Consistency with Cold-Mode Accretion]
Epistemic Type: Theoretical alignment with structural observations.
Bounded Statement: Kinematic imaging of CSGs reveals massive, extended, rotating molecular disks characterized by high velocity dispersion but ordered rotation (high v/σ). This ordered geometry in the presence of massive gas reservoirs provides strong circumstantial consistency with "cold-mode accretion" (CMA) models, wherein narrow, un-shocked streams from the intergalactic medium continuously fuel the disk, avoiding the rotational obliteration inherent to violent major mergers.
Population/Tracer/Regime: CSGs / CO kinematics / Cosmological inflow models.
Confidence: Moderate.
Source Keys: Dekel et al. (2009a), Bournaud et al. (2009).   

REV16-E11 [The Dense Gas History of the Universe (DGHU)]
Epistemic Type: Cosmological volume constraint.
Bounded Statement: Integrations of the cosmic molecular gas density (Ω
H
2
	​

	​

) derived from CO luminosity constraints demonstrate that the global volume density of cold molecular gas closely tracks the cosmic star formation rate history, rising dramatically to a peak at z∼2−3 before declining toward the present day. This confirms that the macroscopic availability of cool gas dictates the global star formation density.
Population/Tracer/Regime: Cosmic volumes / CO luminosity functions / Cosmological models.
Confidence: Moderate.
Source Keys: Decarli et al. (2012), Carilli & Walter (2013).   

REV16-E12 [Cosmic Microwave Background (CMB) Heating and Contrast]
Epistemic Type: Thermodynamic and observational boundary condition.
Bounded Statement: As the CMB temperature scales with redshift (T
CMB
	​

=2.73×(1+z) K), it fundamentally alters observations of high-redshift gas. At z>4, the CMB serves as a non-negligible heating source that elevates the minimum kinetic temperature of the ISM, while simultaneously acting as a warm background that severely reduces the observed contrast of low-J CO lines and the Rayleigh-Jeans dust continuum, causing potential underestimations of total gas mass.
Population/Tracer/Regime: All z>3 systems / Low-J CO and dust / Radiative transfer.
Confidence: High.
Source Keys: da Cunha et al. (2013), Combes et al. (1999).   

Open Debates and Tensions

REV16-D01 [Universality of the Bimodal Star Formation Law]
Competing Positions: One paradigm dictates that the Kennicutt-Schmidt star formation law is strictly bimodal, cleanly separating undisturbed disks (CSGs) from interaction-driven starbursts (SMGs). The opposing position argues that the bimodality is an artificial byproduct of assuming a discontinuous, binary α
CO
	​

 conversion factor. If α
CO
	​

 scales continuously with ISM pressure and star formation surface density, the two sequences collapse into a single, non-linear continuum.
Why Unresolved: Pre-2013 unresolved CO surface brightness measurements cannot definitively constrain whether variations in star formation efficiency are driven by physical differences in the star formation process or merely variations in the α
CO
	​

 factor due to sub-kpc ISM geometry.
Source Keys: Genzel et al. (2010) vs. Narayanan et al. (2012).   

REV16-D02 [Metallicity Dependence of α
CO
	​

 at Cosmic Noon]
Competing Positions: It is widely understood that α
CO
	​

 increases in low-metallicity environments where dust shielding is insufficient to prevent UV photodissociation of CO, leaving "CO-dark" H$2$ gas. However, the exact functional parameterization of this increase remains heavily disputed. Some models suggest a steep, non-linear exponential penalty below a critical metallicity threshold, while others propose a smoother, linear gradient dependent jointly on metallicity and local UV radiation field intensity.
Why Unresolved: Direct, robust gas-phase metallicity measurements for high-z galaxies remain highly uncertain and strongly dependent on chosen optical line-ratio calibrations, preventing the empirical locking of an $\alpha{CO}-Z$ relation.
Source Keys: Bolatto et al. (2013), Genzel et al. (2012).   

REV16-D03 [Origin of the [CII]/FIR Deficit]
Competing Positions: The severe drop in L
[CII]
	​

/L
FIR
	​

 in ultra-luminous systems is attributed to competing mechanics. Position A argues for high ionization parameters where dust grains out-compete gas for UV photons, heavily suppressing photoelectric gas heating. Position B suggests the deficit is an artifact of high dust optical depth at 158 μm attenuating the [CII] emission. Position C posits that the FIR continuum is artificially inflated by obscured AGN emission that does not contribute to [CII] production.
Why Unresolved: Distinguishing these effects requires separating the AGN continuum from the starburst continuum and measuring the dust optical depth directly, tasks requiring higher spatial resolution than widely available before full ALMA operations.
Source Keys: Stacey et al. (2010), Maiolino et al. (2009).   

REV16-D04 [Spatial Separation of Gas and Dust in Mergers]
Competing Positions: In highly lensed extreme mergers, observations reveal spatial offsets between the peak of the CO emission, the peak of [CII], and the thermal dust continuum. Observers debate whether these represent genuine physical separations—such as dust-poor starburst nodes versus older, heavily obscured cores—or whether they are artifacts induced by differential lensing, where physically adjacent but slightly offset emission regions are subject to drastically different magnifications due to caustic crossing.
Why Unresolved: Precision source-plane morphological reconstruction requires ultra-high-resolution mapping and exhaustive lens modeling to rule out caustic crossing artifacts.
Source Keys: Bothwell et al. (2013), Riechers et al. (2011).   

REV16-D05 [PDR vs XDR Heating in Quasar Host Galaxies]
Competing Positions: While standard star formation heats the molecular ISM via UV radiation in Photon-Dominated Regions (PDRs), the extremely high-J CO excitation seen in QSO hosts suggests alternative mechanisms. Proponents of X-ray Dominated Regions (XDRs) argue that hard X-rays from the AGN penetrate deeper into molecular clouds, maintaining high volumetric heating rates. Opponents argue that highly turbulent, dense mechanical shock models or intensely packed PDRs can replicate the observed high-J ladder without requiring dominant XDRs.
Why Unresolved: The degeneracy between dense PDRs, mechanical shocks, and XDRs can only be broken by observing specific fine-structure line ratios (e.g., [OI]/[CII] combined with high-J CO) which were sparsely available.
Source Keys: Meijerink et al. (2006, 2013), Weiß et al. (2007).   

REV16-D06 [Virial Mass Assumptions in SMG Kinematics]
Competing Positions: When deriving dynamical masses from CO linewidths in SMGs, researchers employ differing geometrical assumptions. One camp treats the broad, complex CO profiles as the product of randomized orbital vectors in an ongoing major merger, requiring an isotropic virial estimator (M
dyn
	​

∝σ
2
R). Another camp treats the emission as a highly turbulent but rotationally supported thick disk, utilizing inclination-corrected rotational models (M
dyn
	​

∝v
rot
2
	​

R/sin
2
i).
Why Unresolved: Pre-ALMA interferometry largely lacked the spatial resolution and sensitivity to definitively map the velocity fields across the disks of unlensed SMGs, leaving the geometrical constant highly uncertain.
Source Keys: Tacconi et al. (2008), Engel et al. (2010).   

REV16-D07 [Phase Mixture of [CII] Emission]
Competing Positions: [CII] is frequently utilized as a direct proxy for the cold neutral medium and PDRs surrounding molecular clouds. However, because carbon's ionization potential (11.26 eV) is lower than hydrogen's (13.6 eV), C$^+$ exists abundantly in the diffuse Warm Ionized Medium (WIM) and HII regions. The debate centers on what fraction of the integrated [CII] luminosity in high-redshift starbursts arises from PDRs (tracing molecular gas boundaries) versus the WIM (tracing purely ionized gas).
Why Unresolved: Resolving the phase mixture requires concurrent mapping of [NII] (which originates strictly in ionized regions) to accurately subtract the ionized contribution to [CII].
Source Keys: Decarli et al. (2012), Walter et al. (2009).   

REV16-D08 [The "Cold CO" Component in SMGs]
Competing Positions: Multi-J CO modeling of some SMGs indicates a dense, warm gas phase that dominates the high-J transitions, alongside an extended, low-excitation, cool gas phase that dominates the CO(1-0) emission. The mass contribution of this widespread cold component is debated; some models suggest it represents the vast majority of the galaxy's total M
H
2
	​

	​

, while others argue it is a minor mass component that is highly emissive due to low optical depths.
Why Unresolved: Accurately constraining the cold component requires exceptionally sensitive VLA mapping of the CO(1-0) transition directly against the elevated CMB background.
Source Keys: Ivison et al. (2011), Riechers et al. (2011).   

Key Measurements and Model Calibrations

The review relies on a strict set of calibrated metrics to normalize data across different telescope arrays and observational eras. Accurate interpretation of high-redshift gas mass requires the application of transition-specific excitation corrections and population-specific conversion constants.

REV16-N01 [Starburst α
CO
	​

 Calibration]
Parameterization: α
CO
	​

≈0.8 M
⊙
	​

 (K km s
−1
 pc
2
)
−1
.
Tracer/Population: CO(1-0) to total M
H
2
	​

	​

 conversion / SMGs and QSO hosts.
Conversion Assumptions: Assumes a continuous, turbulent ISM geometry where the CO linewidth traces the deep potential well of the entire starburst core rather than individual bound GMCs. Includes a standard factor of 1.36 to account for the mass of helium.
Uncertainty/Status: Validated against dynamical mass modeling (M
gas
	​

≤M
dyn
	​

−M
star
	​

) and optically thin dust measurements. Scatter is approximately ±0.3 dex.
Source Keys: Downes & Solomon (1998), Tacconi et al. (2008).   

REV16-N02 [Main Sequence α
CO
	​

 Calibration]
Parameterization: α
CO
	​

≈4.0 M
⊙
	​

 (K km s
−1
 pc
2
)
−1
.
Tracer/Population: CO(1-0) to total M
H
2
	​

	​

 conversion / Color-Selected Galaxies (MS disks).
Conversion Assumptions: Assumes gas is locked in discrete, self-gravitating Giant Molecular Clouds (GMCs) identical to Milky Way populations, and that metallicity is near solar. Includes the 1.36 helium mass factor.
Uncertainty/Status: Robust for massive disks (M
∗
	​

>10
10
M
⊙
	​

), but rapidly fails if metallicity drops below Z∼0.5Z
⊙
	​

.
Source Keys: Daddi et al. (2010a), Tacconi et al. (2010).   

REV16-N03 & N04 [CO Spectral Line Energy Distributions (SLEDs) by Population]
Because high-redshift observations often target mid- or high-J CO transitions (e.g., J=3−2 or 4−3) rather than the ground state (J=1−0), extrapolating total gas mass relies on assuming the correct excitation ratio (r
J1
	​

=L
CO(J,J−1)
′
	​

/L
CO(1,0)
′
	​

). Applying an SMG excitation curve to a CSG observation results in catastrophic underestimation of the gas mass. The established mean ratios derived via Large Velocity Gradient (LVG) modeling are summarized below:   

Transition Ratio	Submillimeter Galaxies (SMG)	Color-Selected Galaxies (CSG)	Milky Way (Inner Disk Benchmark)
r
21
	​

	0.85	0.97	0.50
r
32
	​

	0.66	0.56	0.27
r
43
	​

	0.46	0.20	0.17
r
54
	​

	0.39	--	0.08

Uncertainty/Status: Represents sample averages; individual galaxies exhibit scatter depending on the presence of extended cold gas phases and specific PDR geometries. QSO hosts exhibit extreme excitation, peaking near J=6.   

REV16-N05 [CO Line Luminosity Equation]
Exact Equation: L
CO
′
	​

=3.25×10
7
×S
CO
	​

Δv×ν
obs
−2
	​

×D
L
2
	​

×(1+z)
−3
.
Units: L
CO
′
	​

 is expressed in K km s
−1
 pc
2
. S
CO
	​

Δv is the integrated line flux in Jy km s
−1
. ν
obs
	​

 is the observing frequency in GHz. D
L
	​

 is the luminosity distance in Mpc.
Conversion Assumptions: Translates standard observed flux into an intrinsic brightness temperature luminosity. Standard cosmology conventions apply (H
0
	​

=71 km/s/Mpc, Ω
m
	​

=0.27, Ω
Λ
	​

=0.73).
Uncertainty/Status: Strictly mathematical definition. Inputs rely on precise lens magnification corrections (μ) if the target is gravitationally lensed.
Source Keys: Solomon & Vanden Bout (2005), Carilli & Walter (2013).   

REV16-N06 [Bimodal Depletion Timescales]
Exact Equation: τ
dep
	​

=M
gas
	​

/SFR.
Parameterization: τ
dep,SMG
	​

∼100 Myr (10
8
 yr) versus τ
dep,CSG
	​

∼1.0 Gyr (10
9
 yr).
Tracer/Population: Global gas consumption rate across hyper-starbursts vs. main sequence disks.
Conversion Assumptions: SFR derivations strictly depend on the Initial Mass Function (IMF; e.g., Salpeter vs Chabrier) when converting total infrared luminosity (L
FIR
	​

) to M
⊙
	​

/yr. Depletion assumes current SFR remains constant with no additional gas accretion.
Uncertainty/Status: Defines the fundamental temporal bimodality of high-redshift star formation.
Source Keys: Genzel et al. (2010), Daddi et al. (2010b).   

REV16-N07 [[CI] as a Molecular Mass Proxy]
Exact Equation: M
H
2
	​

	​

=X
CI
	​

×L
CI(1−0)
′
	​

.
Parameterization: Mean luminosity ratio L
CI(1−0)
′
	​

/L
CO(1−0)
′
	​

=0.29±0.12.
Tracer/Population: Neutral carbon fine structure transitions / SMG and QSO ensembles.
Conversion Assumptions: Calibrated against CO, assuming a stable absolute abundance ratio of [CI]/[H
2
	​

]≈10
−5
 across disparate cloud chemistries.
Uncertainty/Status: Highly stable across redshifts due to low critical densities (n
crit
	​

≈10
3
 cm
−3
) and optical thinness, bypassing standard α
CO
	​

 opacity uncertainties.
Source Keys: Walter et al. (2011), Papadopoulos et al. (2004).   

REV16-N08 [CMB Temperature Contrast Correction]
Exact Equation: T
CMB
	​

(z)=2.73×(1+z) K.
Parameterization: The observed line flux must be corrected by a contrast factor accounting for the elevated background, essentially scaling as 1−[B
ν
	​

(T
CMB
	​

)/B
ν
	​

(T
ex
	​

)].
Tracer/Population: All continuum and low-frequency line emission at z>4.
Conversion Assumptions: Requires an accurate a priori estimate of the intrinsic excitation temperature (T
ex
	​

) of the gas or dust. If T
ex
	​

 approaches T
CMB
	​

, the transition becomes invisible against the background regardless of intrinsic mass.
Uncertainty/Status: Creates an escalating detection bias against finding cool (T
kin
	​

<20 K) extended gas disks at extremely high redshifts.
Source Keys: da Cunha et al. (2013).   

What Remained Unknown in 2013

The synthesis outlines critical gaps in observational data that defined the frontier immediately prior to the full operational deployment of ALMA and the upgraded JVLA.

REV16-U01 [The Blind CO Luminosity Function]
Why it matters: Without untargeted, blind volume surveys, calculations of the dense gas history of the universe (DGHU) relied heavily on converting UV/IR-selected stellar mass functions and applying empirical scaling relations. This introduced severe selection biases against heavily obscured or quiescent, gas-rich systems.
Decisive observations needed: Deep, wide-field molecular spectral scans of blank cosmological fields (e.g., Hubble Ultra Deep Field) to directly construct the CO luminosity function.   

REV16-U02 [Sub-kpc Imaging of Main Sequence Molecular Disks]
Why it matters: Understanding the physics driving the ∼1 Gyr depletion times in CSGs required determining whether star formation was distributed smoothly across the disk or localized in massive, hyper-efficient clumps migrating toward the bulge.
Decisive observations needed: High-fidelity ALMA imaging capable of resolving the CO and dust continuum at ∼0.1
′′
 scales to directly probe the internal structure of z∼2 disks.   

REV16-U03 [Empirical Calibration of α
CO
	​

 at Low Metallicity]
Why it matters: Theoretical models predicted that early, low-mass galaxies possessed massive envelopes of "CO-dark" molecular gas. Uncalibrated gas mass estimates in these systems would be artificially truncated, fundamentally warping models of early cosmic star formation.
Decisive observations needed: Concurrent observations of dust mass, [CII], and multiple CO transitions in sub-solar metallicity systems to constrain H$_2$ mass independently of CO.   

REV16-U04 [[CII] Detection in Typical Epoch of Reionization Galaxies]
Why it matters: While [CII] was securely detected in hyper-luminous z∼6 QSOs, its utility as a redshift and dynamical tracer for the typical Lyman Break Galaxies (LBGs) responsible for cosmic reionization remained unproven.
Decisive observations needed: Deep targeted ALMA observations of known z>6 LBGs and Lyman-Alpha Emitters (LAEs) to confirm [CII] luminosity scaling relations at the faint end of the luminosity function.   

REV16-U05 [High-Density Tracer Mapping]
Why it matters: CO(1-0) traces the total molecular reservoir, but star formation directly correlates with the dense gas phase (n
H
2
	​

	​

>10
4
 cm
−3
). Determining whether the dense-to-total gas ratio evolves with redshift is essential to understanding the physics of star formation efficiency.
Decisive observations needed: Detections of high dipole-moment molecules like HCN, HCO+, and HNC in standard high-redshift MS galaxies.   

REV16-U06 [Direct Imaging of Cold-Mode Accretion]
Why it matters: While CSG disk kinematics were circumferentially consistent with unshocked cosmological inflow, direct detection of the accreting gas streams was necessary to validate the standard paradigm of secular galaxy assembly.
Decisive observations needed: Ultra-deep observations of low-ionization absorption lines against background quasars, or direct mapping of highly extended, faint circumgalactic medium (CGM) cooling lines.   

Primary-Citation Harvest

The following primary citations constitute the rigorous evidentiary backbone upon which the 2013 review relies, encompassing crucial calibrations, interferometric measurements, and theoretical models.   

Key	Authors / Year / Journal	Identifiers (DOI / arXiv / Bibcode)	Role	Scientific Boundary
REV16-P001	Downes D., & Solomon P. M. 1998, ApJ, 507, 615.	None / None / 1998ApJ...507..615D	Calibration	Establishes the α
CO
	​

≈0.8 conversion factor via dynamical mass modeling in local ULIRGs.
REV16-P002	Daddi E., et al. 2010a, ApJ, 713, 686.	None / None / 2010ApJ...713..686D	Measurement	Demonstrates massive molecular gas reservoirs in z∼1.5 BzK color-selected main sequence galaxies.
REV16-P003	Tacconi L. J., et al. 2010, Nature, 463, 781.	None / None / 2010Natur.463..781T	Measurement	The PHIBSS survey confirming z∼1.2−2.3 star-forming disks possessed gas fractions near 50%.
REV16-P004	Genzel R., et al. 2010, MNRAS, 407, 2091.	None / None / 2010MNRAS.407.2091G	Synthesis	Formalizes the bimodal Kennicutt-Schmidt star formation law, separating disks and starbursts.
REV16-P005	Walter F., et al. 2003, Nature, 424, 406.	None / None / 2003Natur.424..406W	Measurement	Discovers CO emission in the z=6.42 quasar SDSS J1148+5251.
REV16-P006	Weiß A., et al. 2007, A&A, 467, 955.	None / None / 2007A&A...467..955W	Measurement	Executed LVG modeling to calibrate the standard CO spectral line energy distribution (SLED) for SMGs.
REV16-P007	Maiolino R., et al. 2012, A&A, 542, L34.	None / None / 2012A&A...542L..34M	Measurement	Provides evidence of AGN-driven negative feedback via 1300 km/s broad velocity wings in [CII].
REV16-P008	Dannerbauer H., et al. 2009, ApJ, 698, L178.	None / None / 2009ApJ...698L.178D	Measurement	Measured the steep drop-off in high-J CO excitation in CSGs compared to SMGs.
REV16-P009	Walter F., et al. 2009, Nature, 457, 699.	None / None / 2009Natur.457..699W	Measurement	Sub-kpc resolution PdBI mapping of [CII] revealing a compact, maximal starburst core in J1148+5251.
REV16-P010	Stacey G. J., et al. 2010, ApJ, 724, 957.	None / None / 2010ApJ...724..957S	Measurement	Quantifies the severe suppression of the [CII]/FIR ratio in ultra-luminous high-z starbursts.
REV16-P011	Walter F., et al. 2011, ApJ, 730, 18.	None / None / 2011ApJ...730...18W	Measurement	Proves [CI] is a stable alternative to CO for tracing total M
H
2
	​

	​

 across 13 lensed systems.
REV16-P012	Bothwell M., et al. 2013, MNRAS, 429, 3047.	None / arXiv:1205.1511 / 2013MNRAS.429.3047B	Measurement	Calibrates average excitation ratios (r
32
	​

,r
43
	​

) and dynamical mass approximations for SMGs.
REV16-P013	Aravena M., et al. 2010, ApJ, 718, 177.	None / None / 2010ApJ...718..177A	Measurement	Delivers high-fidelity measurements of molecular gas fractions and LVG models for massive CSGs.
REV16-P014	Decarli R., et al. 2012, ApJ, 752, 2.	None / None / 2012ApJ...752....2D	Measurement	Examines the phase mixture and line profiles of [CII] to dissect the kinematics of early mergers.
REV16-P015	Daddi E., et al. 2010b, ApJ, 714, L118.	None / None / 2010ApJ...714L.118D	Measurement	Demonstrates distinct scaling relations and depletion timescales separating disks from major mergers.
REV16-P016	Engel H., et al. 2010, ApJ, 724, 233.	None / None / 2010ApJ...724..233E	Measurement	High-resolution interferometry definitively linking SMGs to late-stage, major gas-rich mergers.
REV16-P017	Wang R., et al. 2010, ApJ, 714, 699.	None / None / 2010ApJ...714..699W	Measurement	High-resolution mapping demonstrating Eddington-limited co-evolution of starbursts and black holes.
REV16-P018	Riechers D. A., et al. 2011, ApJ, 739, L31.	None / None / 2011ApJ...739L..31R	Measurement	Explores the extended cold CO phase in strongly lensed SMGs and spatial offsets from differential magnification.
REV16-P019	Ivison R. J., et al. 2011, MNRAS, 412, 1913.	None / None / 2011MNRAS.412.1913I	Measurement	Images the low-excitation, widely distributed cold molecular gas envelope surrounding a compact SMG.
REV16-P020	Bouwens R. J., et al. 2011b, Nature, 469, 504.	None / None / 2011Natur.469..504B	Measurement	Cosmic star formation rate density evolution out to z∼8, establishing the baseline for the DGHU.
REV16-P021	Maiolino R., et al. 2009, A&A, 498, L5.	None / None / 2009A&A...498L...5M	Measurement	Demonstrates [CII] serves as a powerful dynamical tracer and redshift confirmation tool in z>4 galaxies.
REV16-P022	Solomon P. M., & Vanden Bout P. A. 2005, ARA&A, 43, 677.	None / None / 2005ARA&A..43..677S	Review	Foundational review codifying L
CO
′
	​

 equations and mapping initial SMG populations.
REV16-P023	Dekel A., et al. 2009a, ApJ, 703, 785.	None / None / 2009ApJ...703..785D	Model	Establishes the theoretical necessity of "cold-mode accretion" fueling high-redshift disk galaxies.
REV16-P024	Bournaud F., et al. 2009, ApJ, 707, L1.	None / None / 2009ApJ...707L...1B	Simulation	Shows cold-stream accretion yields extended, highly turbulent, but strictly rotating clumpy gas disks.
REV16-P025	da Cunha E., et al. 2013, ApJ, 765, 9.	None / None / 2013ApJ...765....9D	Calibration	Quantifies the thermodynamic impact of the rising CMB temperature on observing cold gas at high-z.
REV16-P026	Narayanan D., et al. 2012, MNRAS, 421, 3127.	None / None / 2012MNRAS.421.3127N	Calibration	Proposes a continuous, non-bimodal parameterization for α
CO
	​

 dependent upon metallicity and dispersion.
REV16-P027	Meijerink R., et al. 2006, ApJ, 650, L103.	None / None / 2006ApJ...650L.103M	Model	Radiative transfer models separating the distinct chemical and thermal signatures of XDRs versus PDRs.
REV16-P028	Meijerink R., et al. 2013, ApJ, 762, 16.	None / None / 2013ApJ...762...16M	Model	Expands gas heating mechanics by introducing mechanical shock models to explain extreme nuclear excitation.
REV16-P029	Papadopoulos P. P., et al. 2004, MNRAS, 351, 147.	None / None / 2004MNRAS.351..147P	Calibration	Provides the chemical justification for utilizing neutral carbon fine-structure lines as total mass tracers.
REV16-P030	Genzel R., et al. 2012, ApJ, 746, 69.	None / None / 2012ApJ...746...69G	Calibration	Cross-calibrates dust-to-gas ratios and metallicity dependencies to refine molecular mass estimates.
REV16-P031	Bolatto A. D., et al. 2013, ARA&A, 51, 207.	None / None / 2013ARA&A..51..207B	Review	Explores physical dependencies governing the variations of the α
CO
	​

 conversion factor.
REV16-P032	Elmegreen B. G., & Burkert A. 2010, ApJ, 712, 294.	None / None / 2010ApJ...712..294E	Model	Characterizes gravitational fragmentation and formation of massive clumps within gas-dominated disks.
REV16-P033	Dekel A., & Birnboim Y. 2006, MNRAS, 368, 2.	None / None / 2006MNRAS.368....2D	Model	Defines the halo mass threshold above which cold cosmological gas streams are shock-heated.
REV16-P034	Finlator K., et al. 2006, ApJ, 639, 672.	None / None / 2006ApJ...639..672F	Simulation	Models the cosmological framework where galaxies are driven by continuous accretion and violent feedback.
REV16-P035	Robertson B., et al. 2008, ApJ, 676, L21.	None / None / 2008ApJ...676L..21R	Simulation	Demonstrates that ordered disk rotation can rapidly reestablish itself following a major, gas-rich merger.
REV16-P036	Tielens A. G. G. M. 2005, The Physics and Chemistry of the ISM	None / None / 2005pcim.book.....T	Methodological	Establishes textbook mechanics regarding dust shielding, H$_2$ self-shielding, and UV photodissociation.
REV16-P037	Schöier F. L., et al. 2005, A&A, 432, 369.	None / None / 2005A&A...432..369S	Calibration	Supplies the LAMDA parameters including precise Einstein A coefficients and collisional critical densities.
REV16-P038	Obreschkow D., et al. 2009a, ApJ, 702, 1321.	None / None / 2009ApJ...702.1321O	Simulation	Executes semi-analytic modeling to predict the cosmological evolution of the H$_2$ mass function.
REV16-P039	Obreschkow D., et al. 2009b, ApJ, 698, 1467.	None / None / 2009ApJ...698.1467O	Simulation	Develops simulated sky maps and predicts CO line fluxes for high-redshift galaxy populations.
REV16-P040	Hollenbach D., & Tielens A. G. 1999, Rev. Mod. Phys., 71, 173.	None / None / 1999RvMP...71..173H	Methodological	Consolidates PDR physics, defining primary cooling mechanics via [CII] and [OI].
REV16-P041	Barvainis R., et al. 1997, ApJ, 484, 695.	None / None / 1997ApJ...484..695B	Measurement	Early interferometric [CI] observations validating fine-structure diagnostics in distant quasars.
REV16-P042	Greve T. R., et al. 2005, MNRAS, 359, 1165.	None / None / 2005MNRAS.359.1165G	Measurement	Systematic CO mapping of submillimeter galaxies quantifying gas depletion timescales.
REV16-P043	Carilli C. L., et al. 2011, ApJ, 739, L33.	None / None / 2011ApJ...739L..33C	Measurement	Probes extended CO emission and spatial dynamics in distant massive systems.
REV16-P044	Combes F., et al. 2011, A&A, 528, 124.	None / None / 2011A&A...528A.124C	Measurement	ALMA-precursor mapping of molecular outflows and AGN feedback.
REV16-P045	Casey C., et al. 2011, MNRAS, 415, 2723.	None / None / 2011MNRAS.415.2723C	Measurement	Multi-transition CO study investigating gas excitation and conditions in starburst environments.
DO_NOT_USE_UNVERIFIED Quarantine

The following papers surfaced in the external search context but are explicitly quarantined. They represent either post-2013 ALMA/JWST spillover, lack verification within the target review's primary bibliography, or pertain to localized, out-of-scope analyses detached from the 2013 synthesis boundary constraints.

UNCITED_NOT_USABLE: Capak et al. 2015, Nature, 522, 455 (Post-2013 ALMA [CII] results).   

UNCITED_NOT_USABLE: Finkelstein et al. 2013, Nature, 502, 524 (Reionization candidate specific target, not integrated into the core gas synthesis base).   

UNCITED_NOT_USABLE: Fisher et al. 2014, Nature, 505, 186 (Post-2013).   

UNCITED_NOT_USABLE: Riechers et al. 2020, ApJ (Post-2013 ALMA deep fields).   

UNCITED_NOT_USABLE: Umehata et al. 2020 (Post-2013).   

UNCITED_NOT_USABLE: D'Eugenio et al. 2024 (Post-2013 JWST/ALMA quiescent galaxy results).   

UNCITED_NOT_USABLE: Oteo et al. 2016, Zavala et al. 2018 (Post-2013 literature).   

UNCITED_NOT_USABLE: Belli et al. 2021, Williams et al. 2021, Woodrum et al. 2022 (Post-2013 quiescent galaxy gas fraction studies).   

UNCITED_NOT_USABLE: Any entity references related to soccer (e.g., Matheus Cunha, Norway national football team) erroneously retrieved via name collision with "da Cunha et al." CMB contrast studies.   

These sources must strictly never be cited or utilized to inform the substantive claims of the 2013 synthesis review.

Composite Identity Ledger

Cosmology Conventions: The review and its integrated data operate entirely on a standard ΛCDM cosmological framework defined by H
0
	​

=71 km/s/Mpc (or h=0.71), Ω
m
	​

=0.27, and Ω
Λ
	​

=0.73. Computations of luminosity distance (D
L
	​

) for L
CO
′
	​

 are heavily dependent on this structure, and any cross-comparison with studies using h=0.67 or h=1.0 requires explicit conversion.   

Helium Mass Convention: Every calculation of molecular gas mass (M
H
2
	​

	​

 or M
gas
	​

) via α
CO
	​

 cited in this synthesis formally includes a 1.36 mass multiplier to account for the universal abundance of helium.   

Initial Mass Function (IMF) Harmonization: Values correlating star formation rate (SFR) with far-infrared luminosity (L
FIR
	​

) generally assume a Salpeter or Chabrier IMF. Comparative analyses in the bimodal Kennicutt-Schmidt law explicitly harmonize these choices to prevent artificial baseline shifts when calculating depletion times (τ
dep
	​

).

Lens Model Dependence: Extreme care must be taken with the [CII]/FIR deficits and gas fractions derived from strongly lensed systems. Total intrinsic mass values scale as 1/μ (where μ is the magnification factor), and differential lensing acts to artificially alter observed multi-tracer spatial topologies and line-to-continuum luminosity ratios due to caustic crossing.   

Gas Fraction Definitions: The text strictly distinguishes f
gas
	​

=M
gas
	​

/(M
gas
	​

+M
star
	​

) (which asymptotes to 1.0) from the direct ratio M
gas
	​

/M
star
	​

 (which can exceed 1.0).

Kinematic Definitions: Dynamical masses (M
dyn
	​

) for disk galaxies utilize inclination-corrected rotational models (M
dyn
	​

∝v
rot
2
	​

R/sin
2
i), while merger geometries (SMGs) default to isotropic virial estimators (M
dyn
	​

∝σ
2
R).   

REVIEW_BASE_16_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/paper.pdf
- arxiv.org [1301.0371] Cool Gas in High Redshift Galaxies - arXiv Opens in a new window — https://arxiv.org/abs/1301.0371
- annualreviews.org Cool Gas in High-Redshift Galaxies - Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-082812-140953
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies - C.L. Carilli & F. Walter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/Carilli3.html
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies - C.L. Carilli & F. Walter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/Carilli2.html
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies - C.L. Carilli & F. Walter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/Carilli4.html
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies - C.L. Carilli & F. Walter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/Carilli6.html
- ricerca.sns.it The ALMA Reionization Era Bright Emission Line Survey: The molecular gas content of galaxies at z Opens in a new window — https://ricerca.sns.it/retrieve/32811180-1be1-4454-8286-49ae681745fd/aa47281-23.pdf
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies - C.L. Carilli & F. Walter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/Carilli5.html
- publications.lib.chalmers.se STAR FORMATION AND GAS KINEMATICS OF QUASAR HOST GALAXIES AT z ∼ 6 - Chalmers Publication Library Opens in a new window — https://publications.lib.chalmers.se/records/fulltext/182632/local_182632.pdf
- nbi.ku.dk Molecular Gas in a Massive Main-sequence Galaxy at z = Opens in a new window — https://nbi.ku.dk/english/theses/masters-theses/han-lei/Masters_Han_final.pdf
- arxiv.org [1302.0844] On the effect of the Cosmic Microwave Background in high-redshift (sub-)millimeter observations - arXiv Opens in a new window — https://arxiv.org/abs/1302.0844
- academic.oup.com Direct detection of cool molecular gas in a star-forming galaxy at - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/549/3/stag924/68493587/stag924.pdf
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies - C.L. Carilli & F. Walter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/Carilli7.html
- arxiv.org Ground-state 12CO emission and a resolved jet at 115 GHz (rest-frame) in the radio loud quasar 3C318 - arXiv Opens in a new window — https://arxiv.org/pdf/1308.3360
- eso.org Large turbulent reservoirs of cold molecular gas around high-redshift starburst galaxies - ESO.org Opens in a new window — https://www.eso.org/public/archives/releases/sciencepapers/eso1727/eso1727a.pdf
- events.asiaa.sinica.edu.tw Observing High-z Galaxies With ALMA Opens in a new window — https://events.asiaa.sinica.edu.tw/workshop/20160319/talk/talk2_Wei_hao_ALMA_high-z.pdf
- arxiv.org NOEMA^"3D": extended CO, [C I] and dust in massive star-forming main sequence galaxies at cosmic noon - arXiv Opens in a new window — https://arxiv.org/html/2604.18504v3
- arxiv.org The first detection of dense gas in a massive main-sequence galaxy at cosmic noon - arXiv Opens in a new window — https://arxiv.org/html/2606.19282v1
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies - C.L. Carilli & F. Walter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/Carilli_refs.html
- ned.ipac.caltech.edu Molecular gas in distant galaxies from ALMA studies - F. Combes Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Combes/Combes_refs.html
- publications.lib.chalmers.se A dusty, normal galaxy in the epoch of reionization - Chalmers Publication Library Opens in a new window — https://publications.lib.chalmers.se/records/fulltext/214876/local_214876.pdf
- researchgate.net An ALMA/NOEMA survey of the molecular gas properties of high-redshift star-forming galaxies | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/347642423_An_ALMANOEMA_survey_of_the_molecular_gas_properties_of_high-redshift_star-forming_galaxies
- arxiv.org Measurement of the gas consumption history of a massive quiescent galaxy - arXiv Opens in a new window — https://arxiv.org/html/2405.19401v2
- researchgate.net Early Science with the Large Millimeter Telescope: CO and [C ii] Emission in the z = 4.3 AzTEC J095942.9+022938 (COSMOS AzTEC-1) - ResearchGate Opens in a new window — https://www.researchgate.net/publication/281262062_Early_Science_with_the_Large_Millimeter_Telescope_CO_and_C_ii_Emission_in_the_z_43_AzTEC_J0959429022938_COSMOS_AzTEC-1
- arxiv.org Large turbulent reservoirs of cold molecular gas around high-redshift starburst galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/1708.08851
- mpia.de Invited Papers and Reviews | Max Planck Institute for Astronomy Opens in a new window — https://www.mpia.de/4684529/invited-papers-and-reviews
- sissa.it High-redshift Dusty Star-Forming Galaxies: a panchromatic approach to constrain massive - SISSA Opens in a new window — https://www.sissa.it/ap/phdsection/AlumniThesis/Lara%20Pantoni.pdf
- open-research-europe.ec.europa.eu Atacama Large Aperture Submillimeter Telescope (AtLAST) science: Gas and dust in nearby galaxies. - Open Research Europe Opens in a new window — https://open-research-europe.ec.europa.eu/articles/4-148
- researchgate.net (PDF) A dusty, normal galaxy in the epoch of reionization - ResearchGate Opens in a new window — https://www.researchgate.net/publication/273067680_A_dusty_normal_galaxy_in_the_epoch_of_reionization
- nbi.ku.dk Examining the existence of two distinct modes of star formation Opens in a new window — https://nbi.ku.dk/english/theses/masters-theses/isabella-chi-gieseler-cortzen/IsabellaCortzen_thesis.pdf
- arxiv.org arXiv:1312.6365v1 [astro-ph.CO] 22 Dec 2013 Opens in a new window — https://arxiv.org/pdf/1312.6365
- osti.gov F er mil a b - OSTI Opens in a new window — https://www.osti.gov/servlets/purl/3021878
- arxiv.org Evolution of Gas Velocity Dispersion in Discs from 𝑧∼8 to 𝑧∼0.5 - arXiv Opens in a new window — https://arxiv.org/html/2505.24129v1
- academic.oup.com Ground-state 12CO emission and a resolved jet ... - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/435/4/3376/13762261/stt1530.pdf
- academic.oup.com Molecular cloud properties and CO line emission ... - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/435/3/2676/3453591/stt1480.pdf
- researchgate.net High-redshift quasars at z ≥ 3 z \geq 3 -- III. Parsec-scale jet properties from VLBI observations - ResearchGate Opens in a new window — https://www.researchgate.net/publication/389274072_High-redshift_quasars_at_z_geq_3_--_III_Parsec-scale_jet_properties_from_VLBI_observations
- ned.ipac.caltech.edu Archived Release Notes - About NED | NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/Documents/Overview/History
- scholarship.haverford.edu Star Formation and Gas Kinematics of Quasar Host Galaxies at z~6 - Haverford Scholarship Opens in a new window — https://scholarship.haverford.edu/cgi/viewcontent.cgi?article=1347&context=astronomy_facpubs
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies - C.L. Carilli & F. Walter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/Carilli1.html
- ned.ipac.caltech.edu Cool Gas in High Redshift Galaxies - C.L. Carilli & F. Walter Opens in a new window — https://ned.ipac.caltech.edu/level5/Sept17/Carilli/Carilli_contents.html
- oamonitor.ireland.openaire.eu Cool Gas in High-Redshift Galaxies - National Open Access Monitor, Ireland Opens in a new window — https://oamonitor.ireland.openaire.eu/rpo/tcd/search/publication?pid=10.1146%2Fannurev-astro-082812-140953
- en.wikipedia.org X-factor (astrophysics) - Wikipedia Opens in a new window — https://en.wikipedia.org/wiki/X-factor_(astrophysics)
- discovery.researcher.life Infrared fine-structure lines at high redshift - R Discovery Opens in a new window — https://discovery.researcher.life/article/infrared-fine-structure-lines-at-high-redshift/00229f22181a3073af8e977b72cb2648
- arxiv.org ALMA visits the QSO MUSEUM: connecting molecular gas and the cool circumgalactic medium around 37 z∼3 quasars - arXiv Opens in a new window — https://arxiv.org/html/2606.30742v1
- researchgate.net Cold gas disks in main-sequence galaxies at cosmic noon: Low turbulence, flat rotation curves, and disk-halo degeneracy - ResearchGate Opens in a new window — https://www.researchgate.net/publication/367961666_Cold_gas_disks_in_main-sequence_galaxies_at_cosmic_noon_Low_turbulence_flat_rotation_curves_and_disk-halo_degeneracy
- researchgate.net (PDF) Line-Intensity Mapping: 2017 Status Report - ResearchGate Opens in a new window — https://www.researchgate.net/publication/320056757_Line-Intensity_Mapping_2017_Status_Report
- arxiv.org Cosmic CO and [CII] backgrounds and the fueling of star formation over 12 Gyr - arXiv Opens in a new window — https://arxiv.org/html/2602.02658v1
- scilit.com The ALMA-ALPAKA survey - Scilit Opens in a new window — https://www.scilit.com/publications/f36612345d0b67e09ae03813eeeb5aac
- frontiersin.org Star Formation Quenching in Quasar Host Galaxies - Frontiers Opens in a new window — https://www.frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2017.00024/full
- royalsocietypublishing.org High-redshift star formation in the Atacama large millimetre/submillimetre array era Opens in a new window — https://royalsocietypublishing.org/rsos/article/7/12/200556/95459/High-redshift-star-formation-in-the-Atacama-large
- mdpi.com From Clusters to Proto-Clusters: The Infrared Perspective on Environmental Galaxy Evolution - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/8/11/554
- scispace.com The rest-frame submillimeter spectrum of high-redshift, dusty, star-forming galaxies - SciSpace Opens in a new window — https://scispace.com/pdf/the-rest-frame-submillimeter-spectrum-of-high-redshift-dusty-1ey7vqgk53.pdf
- arxiv.org Cm-wavelength Studies of Molecular Gas and Star Formation at High Redshift with the SKA Opens in a new window — https://arxiv.org/html/2606.26640v1
- eso.org Herschel-ATLAS and ALMA - Eso.org Opens in a new window — https://www.eso.org/public/archives/releases/sciencepapers/eso1426/eso1426a.pdf
- pmc.ncbi.nlm.nih.gov High-redshift star formation in the Atacama large millimetre/submillimetre array era - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC7813222/
- repository.dl.itc.u-tokyo.ac.jp Cold molecular gas and physical properties of active galaxies hosting rapidly growing super-massive black holes - 東京大学 Opens in a new window — https://repository.dl.itc.u-tokyo.ac.jp/record/2008977/files/A39001.pdf
- archiv.ub.uni-heidelberg.de The Physical Properties and Cosmic Environments of Quasars in the First Gyr of the Universe Opens in a new window — https://archiv.ub.uni-heidelberg.de/volltextserver/25125/1/thesis_phd_mazzucchelli_v2.pdf
- www2.ifa.hawaii.edu Dusty Star Forming Galaxies at High Redshift - Institute for Astronomy Opens in a new window — https://www2.ifa.hawaii.edu/gradprog/ASTR736F15/LzHz/LzHz-SMGreview_Casey+14.pdf
- cdn.toxicdocs.org conoco - Toxic Docs Opens in a new window — https://cdn.toxicdocs.org/pm/pm20w6GkdZQ067B5NdJRwak8d/pm20w6GkdZQ067B5NdJRwak8d.pdf
- researchgate.net ALMA SPECTROSCOPIC SURVEY IN THE HUBBLE ULTRA DEEP FIELD: CO LUMINOSITY FUNCTIONS AND THE EVOLUTION OF THE COSMIC DENSITY OF MOLECULAR GAS | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/305615892_ALMA_Spectroscopic_Survey_in_the_Hubble_Ultra_Deep_Field_CO_Luminosity_Functions_and_the_Evolution_of_the_Cosmic_Density_of_Molecular_Gas
- researchgate.net Herschel-ATLAS and ALMA: HATLAS J142935.3-002836, a lensed major merger at redshift 1.027 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/263281241_Herschel-ATLAS_and_ALMA_Hatlas_j1429353-002836_a_lensed_major_merger_at_redshift_1027
- pmc.ncbi.nlm.nih.gov Gone with the heat: a fundamental constraint on the imaging of dust and molecular gas in the early Universe - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC4929898/
- mpia.de The Evolution of the Baryons Associated with Galaxies Averaged over Cosmic Time and Space Opens in a new window — https://www.mpia.de/5504464/walter_aspecs_2020.pdf
- researchgate.net Different Explanations for the Cosmic Microwave Background Radiation - ResearchGate Opens in a new window — https://www.researchgate.net/publication/355706746_Different_Explanations_for_the_Cosmic_Microwave_Background_Radiation

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

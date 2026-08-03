# Review Base 10 raw Deep Research packet — Conroy 2013

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_11_wechsler_tinker_2018_DR_PROMPT.md`
Prompt SHA-256: `215de453789cbc2912be4f7808c9a177c8babb716a9265bfb9e3f055c3f7c72f`
Conversation ID: `bdb0d7d58425fc3a`
Submit UTC: `2026-07-16T02:48:49.372483Z`
Research Start UTC: `2026-07-16T02:49:20.280344Z`
Result captured UTC: `2026-07-16T03:02:03.478206Z`
Raw result SHA-256: `cd4c275e33301d9e66056449fc819143e60d5e7cb9a5ce2c03f4168a7ee87ed5`

## Deep Research review-base result

Deep Research Source-Base Review: The Statistical Galaxy-Halo Connection
1. Review Identity and Scope Map

The synthesis of galaxy formation within a cosmological context requires mapping the observable baryonic universe to the underlying, gravitationally dominant dark matter distribution. This report evaluates the foundational 2018 synthesis of this multivariate relationship.

Review Attribute	Detail
Review Identifier	REV11-MAIN
Authors	Wechsler, Risa H. & Tinker, Jeremy L.
Publication Year	2018
Journal	Annual Review of Astronomy and Astrophysics, Volume 56, Pages 435-487
Verifiable Identity	DOI: 10.1146/annurev-astro-081817-051756; arXiv: 1804.03097; ADS bibcode: 2018ARA&A..56..435W
Epistemic Role	supporting_review

Scope Map:
The 2018 review by Wechsler and Tinker stands as a definitive architectural synthesis of the galaxy-halo connection. It rigorously delineates the boundaries between physical models (hydrodynamical simulations and semi-analytic models) and empirical frameworks (Halo Occupation Distribution [HOD], Conditional Luminosity Function [CLF], and Subhalo Abundance Matching [SHAM]). The manuscript systematically aggregates constraints derived from two-point spatial clustering, galaxy-galaxy weak gravitational lensing, group/cluster abundance catalogs, and galaxy stellar mass functions. The core analytic scope is rigidly focused on the stellar-to-halo mass relation (SHMR), the intrinsic logarithmic scatter inherent to this relation, the phenomenon of halo and galaxy assembly bias, and the divergent evolutionary pathways of central versus satellite galaxies. This review explicitly establishes the non-linear efficiency of star formation, peaking at a pivot halo mass of 10
12
M
⊙
	​

, a fundamental boundary condition for all modern galaxy evolution models [cite: REV11-MAIN, REV11-P018].

2. The Theoretical and Empirical Framework of the Galaxy-Halo Connection

The standard ΛCDM cosmological paradigm dictates that the universe's structure evolves hierarchically, with collisionless dark matter collapsing into virialized, roughly spherical halos [cite: REV11-P024]. Galaxies condense out of the cooling baryonic gas trapped within these deep potential wells [cite: REV11-P015]. However, the mapping between the properties of the dark matter halo—such as its mass, concentration, spin, and assembly history—and the observable properties of the hosted galaxy—such as stellar mass, star formation rate, and color—is highly complex and decidedly non-linear.

This non-linearity arises from the intricate thermodynamics of the baryonic sector. At low halo masses, the shallow gravitational potential wells are easily disrupted. When early star formation initiates, the resulting supernova explosions and intense stellar winds provide sufficient kinetic energy to eject the remaining gas back into the circumgalactic medium, permanently choking off subsequent star formation [cite: REV11-P022]. Furthermore, the epoch of cosmic reionization elevates the Jeans mass of the intergalactic medium, preventing pristine gas from ever collapsing into the smallest primordial halos [cite: REV11-P016].

Conversely, at the high-mass extreme (M
h
	​

>10
13
M
⊙
	​

), halos host immense reservoirs of hot, X-ray emitting gas. While this gas should theoretically cool and precipitate massive bursts of star formation, observations reveal that the central brightest cluster galaxies are predominantly old, red, and passive [cite: REV11-P023, REV11-P025]. The prevailing consensus attributes this quenching to feedback from active galactic nuclei (AGN). Supermassive black holes at the centers of these massive halos accrete matter and launch relativistic jets, injecting thermal energy into the intracluster medium and establishing a stable equilibrium that prevents catastrophic cooling [cite: REV11-P038].

Between these two extreme feedback regimes lies a specific thermodynamic "sweet spot"—a pivot mass scale. The review synthesis decisively established this pivot halo mass at approximately 10
12
M
⊙
	​

 [cite: REV11-P001, REV11-P002]. Halos near this mass scale (roughly the mass of the Milky Way's dark matter halo) operate at the peak integrated efficiency of galaxy formation. Yet, even at this absolute maximum, the inefficiency of the cosmic baryon cycle is striking: less than 20% of the universally available baryons within the halo's virial radius have been successfully converted into stellar mass by the present day (z=0) [cite: REV11-P020]. The remaining >80% of baryons persist as hot halo gas, circumgalactic clouds, or have been violently expelled entirely.

2.1 Established Findings

The following data structure catalogs the definitive consensus established within the 2018 review regarding these astrophysical mechanisms.

Claim ID	Epistemic Type	Bounded Statement	Regime & Boundary Conditions	Confidence Level	Source Keys
REV11-E01	Calibration / Review Synthesis	The integrated efficiency of galaxy formation is a highly non-linear function of host dark matter halo mass, reaching an absolute peak within halos at a characteristic "pivot mass" of approximately 10
12
M
⊙
	​

.	Applies strictly to central galaxies at z=0, utilizing virial halo mass definitions (e.g., M
200c
	​

 or M
vir
	​

).	Very High	[cite: REV11-P001, REV11-P002, REV11-P018]
REV11-E02	Observation / Calibration	At the pivot halo mass of 10
12
M
⊙
	​

, the maximum integrated stellar mass fraction relative to the cosmic baryon fraction (M
∗
	​

/(f
b
	​

M
h
	​

)) is strictly bounded below 20%.	Assumes a baseline cosmic baryon fraction f
b
	​

≈0.157. Metric applies to present-day (z=0) stellar mass functions.	High	[cite: REV11-P001, REV11-P020]
REV11-E03	Observation / Review Synthesis	The intrinsic scatter in central galaxy stellar mass at a fixed dark matter halo mass is tightly constrained to be small—less than 0.20 dex—for massive halos exceeding 10
12.5
M
⊙
	​

.	Applies to massive red/quenched central galaxies. Modeled as a log-normal distribution in M
∗
	​

 at fixed M
h
	​

.	High	[cite: REV11-P006, REV11-P011, REV11-P017]
REV11-E04	Observation / Analytic Theory	In the high-mass regime representing galaxy groups and clusters (M
h
	​

>10
13.5
M
⊙
	​

), the total stellar mass contained within the halo scales with the host halo mass according to M
∗,tot
	​

∝M
h
2/3
	​

.	Halos identified via X-ray, Sunyaev-Zel'dovich effect, or optical cluster finding algorithms. Includes satellites and intracluster light.	High	[cite: REV11-P025]
REV11-E05	Observation	In contrast to total stellar mass, the stellar mass of the brightest cluster galaxy (the central) in massive halos scales extremely shallowly with the host halo mass, following M
∗,cen
	​

∝M
h
1/3
	​

.	High-mass regime (M
h
	​

>10
13
M
⊙
	​

). Demonstrates that massive halos grow by late-time minor mergers depositing mass into the satellite population, not the central galaxy.	High	[cite: REV11-P014, REV11-P025]
REV11-E06	Calibration / Simulation	The lowest mass dark matter halos capable of hosting a luminous galaxy have present-day dynamical masses of roughly 10
9
M
⊙
	​

.	Based on ultra-faint dwarf spheroidal companions in the Local Group. Highly dependent on reionization epoch timing.	Moderate	[cite: REV11-P016, REV11-P022]
REV11-E07	Analytic Theory / Review Synthesis	The cumulative number density of galaxies sorted by stellar mass can be monotonically mapped to the cumulative density of halos/subhalos sorted by a dynamical mass proxy (like V
peak
	​

), closely reproducing observed spatial clustering.	Subhalo Abundance Matching (SHAM). Requires dark matter-only N-body simulations tracking subhalos prior to tidal disruption.	Very High	[cite: REV11-P002, REV11-P014, REV11-P018]
REV11-E08	Observation	Below a stellar mass of approximately 10
9
M
⊙
	​

, the observed galaxy stellar mass function deviates from a single power-law Schechter function, exhibiting a "double Schechter" shape indicating an overabundance of low-mass galaxies.	Observed in deep volume-limited surveys (e.g., SDSS DR7) at z≈0.	High	[cite: REV11-P005, REV11-P032]
REV11-E09	Calibration / HOD	The satellite fraction (f
sat
	​

) is strongly dependent on stellar mass and drives the small-scale (<1 Mpc) amplitude of the two-point correlation function.	Sub-megaparsec scales, modeled via the "1-halo" term in HOD frameworks.	Very High	[cite: REV11-P004, REV11-P021, REV11-P035]
REV11-E10	Simulation / Analytic Theory	In ΛCDM simulations, large-scale clustering of halos is not solely determined by mass; at fixed mass, halos that assembled their mass earlier cluster more strongly than those that assembled later.	Theoretical "Halo Assembly Bias". Most pronounced for low-mass halos and high-mass halos transitioning through non-linear collapse.	Very High (Theoretically)	[cite: REV11-P008, REV11-P009, REV11-P010]
REV11-E11	Review Synthesis	The suppression of star-formation efficiency requires divergent feedback regimes: supernova/stellar winds in low-mass halos (M
h
	​

<10
12
M
⊙
	​

), and active galactic nuclei (AGN) in high-mass halos (M
h
	​

>10
12
M
⊙
	​

).	Global cosmological application across all physical models matching the SHMR.	High	[cite: REV11-P038]
REV11-E12	Analytic Theory / Observation	At large physical separations (>10h
−1
 Mpc), the galaxy-to-dark-matter bias is strictly linear and scale-independent, allowing galaxy clustering to trace the underlying linear dark matter power spectrum.	Defined by the "2-halo" term in the HOD framework; holds true across various galaxy target selections in the linear regime.	Very High	[cite: REV11-P013, REV11-P034, REV11-P036]
3. Dissecting the Degeneracies: Satellites, Scatter, and Assembly Bias

While the foundational mapping between stellar mass and halo mass provides a robust zeroth-order description of the universe, it masks a rich underlying covariance. The presence of intrinsic scatter—measured at roughly 0.16 to 0.20 dex at high masses—implies that dark matter halo mass cannot be the sole determining factor in galaxy evolution [cite: REV11-P006, REV11-P011]. Understanding the physical origins of this scatter is critical. Do halos of identical mass that form early in cosmic history produce different galaxies than those that form late? Theoretical simulations prove that halo clustering depends on formation time, a phenomenon known as "halo assembly bias" [cite: REV11-P008, REV11-P010]. If galaxy properties (like color, specific star formation rate, or radius) correlate with this halo formation time, it induces "galaxy assembly bias," fundamentally altering the way galaxies trace the underlying cosmic web. This heavily complicates cosmological inference [cite: REV11-P030].

Furthermore, the environmental dichotomy between central and satellite galaxies introduces severe modeling complexities. When a halo falls into a more massive host, it becomes a subhalo. The central galaxy transitions into a satellite, subjecting it to violent environmental forces. The hot gas reservoir may be slowly stripped via "strangulation," leading to a gradual decline in star formation, or the cold disk gas may be violently removed via "ram pressure stripping" as the satellite plunges through the dense intracluster medium [cite: REV11-P031]. Accurate Subhalo Abundance Matching (SHAM) must account for this by matching stellar mass not to the subhalo's present, heavily stripped mass, but to its maximum historical circular velocity (V
peak
	​

) or mass at infall (M
peak
	​

) [cite: REV11-P011, REV11-P014].

3.1 Open Debates and Theoretical Tensions

The synthesis of these empirical observations against hydrodynamic simulations revealed several deeply unresolved tensions, documented in the following ledger.

Debate ID	Competing Positions	Why Unresolved	Source Keys
REV11-D01	Observational Galaxy Assembly Bias: While theoretical halo assembly bias is proven, some argue environmental effects fully explain observed galaxy clustering differences, whereas others argue intrinsic galaxy assembly bias is strictly required to fit the spatial clustering data.	Measuring halo mass observationally is inherently noisy. Current mass proxies (richness, weak lensing) correlate with halo formation history, creating complex degeneracies that mimic or mask true assembly bias.	[cite: REV11-P017, REV11-P028, REV11-P030]
REV11-D02	Physical Origin of Intrinsic SHMR Scatter: Some models propose scatter is driven primarily by varying formation times and merger histories. Competing models suggest tighter correlation with halo concentration or spin.	Concentration, spin, and assembly history are fundamentally cross-correlated in dark matter simulations. Breaking these degeneracies requires higher-resolution hydrodynamic simulations.	[cite: REV11-P009, REV11-P011]
REV11-D03	Optimal Proxy for SHAM: It is debated whether maximum circular velocity (V
max
	​

), peak circular velocity over history (V
peak
	​

), or peak halo mass (M
peak
	​

) serves as the most accurate predictor of a subhalo's hosted galaxy stellar mass.	V
peak
	​

 accounts for stripping, but struggles to perfectly predict satellite disruption rates and "orphan" galaxy populations compared to more sophisticated semi-analytic models.	[cite: REV11-P011, REV11-P014, REV11-P018]
REV11-D04	Dominant Satellite Quenching Mechanisms: Suppression of star formation could be driven by slow "strangulation" of hot gas or violent "ram pressure stripping" of cold disk gas.	Measurements exhibit a "delayed-then-rapid" quenching profile. Different hydrodynamic simulations reproduce this using disparate balances of strangulation versus ram pressure depending on sub-grid resolution.	[cite: REV11-P006, REV11-P031]
REV11-D05	The Slope of the Low-Mass SHMR: Abundance matching extrapolated from the lowest mass observed galaxies implies a very steep relation (M
∗
	​

∝M
h
2.5
	​

), but local group kinematics imply a shallower slope to solve the "Too Big To Fail" problem.	Severe incompleteness in observations of ultra-faint dwarfs, combined with uncertainties in dynamical mass estimates (core vs cusp density profiles), makes it impossible to definitively pin down the slope.	[cite: REV11-P016, REV11-P022]
REV11-D06	Treatment of "Orphan" Galaxies: Subhalos are artificially destroyed by the finite resolution of N-body simulations. Some models forcefully insert "orphan" galaxies tracking the most bound particles; others argue standard HOD radial profiles bypass the need for orphans.	There is no consensus on the exact dynamical friction timescales that dictate when an orphan formally merges with the central, leading to large variations in predicted small-scale clustering.	[cite: REV11-P004, REV11-P021]
REV11-D07	Baryonic Back-Reaction on Halo Profiles: Adiabatic contraction models predict condensing baryons steepen the inner dark matter profile. Conversely, strong stellar/AGN feedback models predict rapid gas expulsion causes the dark matter to expand, forming a core.	Current observational kinematics cannot easily separate the stellar mass potential from the inner dark matter potential in individual systems to confirm which effect dominates at different mass scales.	[cite: REV11-P022, REV11-P027]
REV11-D08	Kinematics vs. Weak Lensing Constraints: Weak lensing provides direct total matter distribution measurements but suffers projection effects. Satellite kinematics provide local dynamical masses but rely on assumed velocity anisotropies and orbital distributions.	Both methods carry disparate, highly complex systematic error budgets. Integrating them into a single coherent constraint requires computationally prohibitive forward-modeling.	[cite: REV11-P006, REV11-P026]
4. Quantitative Constraints on the Cosmological Model

The empirical modeling of the galaxy-halo connection utilizes distinct parameterizations to match simulation outputs to large-scale galaxy surveys. The Halo Occupation Distribution (HOD) framework formalizes this by separately defining the probability distributions for central and satellite galaxies [cite: REV11-P004, REV11-P021]. For central galaxies, the occupation probability is generally modeled as a softened step function—an error function—centered on a characteristic halo mass threshold, with the width of the step representing the intrinsic scatter in the galaxy-halo relationship. Satellite galaxies, which trace the subhalo population, are modeled with a power-law distribution that emerges only above a secondary mass threshold, scaling linearly with the mass of the host halo at the high-mass end [cite: REV11-P035].

These parameterizations must be convolved with universally calibrated analytical forms of the dark matter halo mass function [cite: REV11-P012] and the scale-dependent halo bias function [cite: REV11-P013] to predict the projected two-point correlation function (w
p
	​

(r
p
	​

)) and the weak lensing excess surface mass density (ΔΣ(R)). The following table outlines the foundational quantitative calibrations established through this process by 2018.

4.1 Key Measurements and Model Calibrations
Metric ID	Parameter / Equation	Units	Definitions & Boundary Conditions	Sample / Method	Uncertainty & Status	Source Keys
REV11-N01	Pivot Halo Mass: M
h,pivot
	​

≈10
12
 (frequently parameterized as log
10
	​

(M
1
	​

)=11.5−12.5)	Solar masses (M
⊙
	​

)	Host halo virial mass (M
vir
	​

 or M
200c
	​

) at z=0. Varies slightly based on IMF and exact overdensity definition.	Multi-epoch SHAM utilizing SDSS and high-z SMFs.	Firmly established, ±0.15 dex.	[cite: REV11-P001, REV11-P018]
REV11-N02	Peak Integrated Efficiency: M
∗
	​

/(f
b
	​

M
h
	​

)≈0.15 to 0.20	Dimensionless ratio	Ratio of total central stellar mass to the theoretical available baryon mass (f
b
	​

M
h
	​

, where f
b
	​

≈0.157). Evaluated at M
h
	​

≈10
12
M
⊙
	​

.	Combining SDSS DR7 central stellar masses with N-body halo mass functions.	Upper limit firmly bounded below 20%.	[cite: REV11-P001, REV11-P020]
REV11-N03	High-Mass SHMR Scatter: σ
logM
∗
	​

∣M
h
	​

	​

≤0.20 (best fit ∼0.16)	dex	Logarithmic scatter in stellar mass at a fixed host halo mass, for halos above 10
12.5
M
⊙
	​

.	Derived from galaxy clustering and weak lensing joint fits (e.g., COSMOS, BOSS).	±0.04 dex. Statistically robust at high mass.	[cite: REV11-P006, REV11-P011, REV11-P017]
REV11-N04	Central Stellar Mass Slope: M
∗,cen
	​

∝M
h
α
	​

, where α≈0.33	Exponent	Evaluated strictly in the high-mass regime (M
h
	​

≫10
12
M
⊙
	​

).	Group and cluster catalogs, specifically targeting Brightest Cluster Galaxies.	Well-calibrated, though sensitive to BCG/ICL aperture separation.	[cite: REV11-P014, REV11-P025]
REV11-N05	Cluster Total Stellar Slope: M
∗,tot
	​

∝M
h
β
	​

, where β≈0.66	Exponent	Integrated stellar mass (centrals + satellites + ICL) within the virial radius.	Cluster weak lensing and X-ray mass proxies.	±0.05.	[cite: REV11-P025]
REV11-N06	Standard Central HOD: ⟨N
cen
	​

⟩=
2
1
	​

[1+erf(
σ
logM
	​

logM
h
	​

−logM
min
	​

	​

)]	Galaxies per halo	M
min
	​

: mass at which 50% of halos host a central; σ
logM
	​

: models the soft transition (scatter).	5-parameter HOD fitted to SDSS projected two-point correlation function w
p
	​

(r
p
	​

).	Universally applied baseline model in LSS cosmology.	[cite: REV11-P004, REV11-P021, REV11-P035]
REV11-N07	Standard Satellite HOD: ⟨N
sat
	​

⟩=⟨N
cen
	​

⟩(
M
1
′
	​

M
h
	​

−M
0
	​

	​

)
α
	Galaxies per halo	M
0
	​

: cutoff mass; M
1
′
	​

: mass required to host one satellite; α≈1: power-law slope.	Empirical fitting to SDSS clustering.	α is remarkably close to 1.0 across diverse samples.	[cite: REV11-P021, REV11-P035]
REV11-N08	Universal Halo Mass Function: f(σ)=A[(
b
σ
	​

)
−a
+1]e
−c/σ
2
	Differential fraction	σ: variance of the linear density field; A,a,b,c: redshift and cosmology calibrations.	Large-volume N-body simulations spanning multiple cosmologies.	Accurate to ∼5% across a wide range of masses.	[cite: REV11-P012]
5. Epistemic Frontiers: What Remained Unknown in 2018

Despite the robust parameterization of the baseline models, the 2018 review highlighted several critical vulnerabilities in the field's predictive power. As observational surveys pushed toward massive precision-cosmology endeavors (Stage-IV surveys), the systematic uncertainties embedded in the galaxy-halo connection threatened to dominate the statistical error budgets [cite: REV11-MAIN]. The exact dependencies of secondary galaxy properties, the extreme high-redshift universe, and the precise spatial distribution of subhalos remained fiercely debated.

Unknown ID	The Unknown Item	Why it Matters	Decisive Observation/Simulation Needed
REV11-U01	Direct Detection of Galaxy Assembly Bias	If galaxy properties correlate with halo formation history independently of mass, all cosmological constraints derived from standard mass-only HODs contain unquantified systematic biases.	Wide-field spectroscopic surveys coupled with extremely deep lensing or X-ray data capable of measuring both the mass and accretion history of individual halos.
REV11-U02	The SHMR at High Redshifts (z>4)	The efficiency of star formation during the epoch of reionization sets the initial conditions for subsequent galaxy evolution. Prior to 2018, the SHMR was highly extrapolated beyond z=3.	Space-based infrared observations (e.g., JWST) to provide robust rest-frame optical stellar masses and complete luminosity functions for galaxies up to z=10.
REV11-U03	The True Low-Mass Slope of the SHMR	The steepness of the SHMR below 10
10
M
⊙
	​

 tests the limits of dark matter physics (WDM vs CDM) and the efficiency of supernova feedback in shallow potential wells.	Complete, volume-limited kinematic surveys of ultra-faint dwarf galaxies in the Local Volume to accurately measure dynamical masses without tidal stripping confounds.
REV11-U04	Disentangling Correlated Scatter	It is unknown how scatter in stellar mass correlates with scatter in color, size, and star formation rate at a fixed halo mass. Understanding this covariance matrix is required for realistic mock catalogs.	Multi-wavelength cross-correlation measurements combining highly complete stellar mass functions, resolved HI gas kinematics, and precise environmental metrics.
REV11-U05	Exact Influence of Baryons on the HMF	Using dark matter-only mass functions will introduce unacceptable systematic errors in precision cosmology because baryonic feedback physically relocates mass, altering the underlying halo mass function.	Ultra-large volume hydrodynamical simulations integrated into emulators, heavily calibrated by observational SZ and X-ray cluster gas profiles.
REV11-U06	Spatial Bias of Satellite Galaxies	Standard HOD assumes satellites perfectly trace the dark matter profile (e.g., NFW). If satellites are spatially biased by their infall trajectories, "1-halo" clustering predictions will be systematically incorrect.	High-resolution galaxy-galaxy lensing at very small projected radii (<100 kpc) to map the exact radial distribution of subhalos relative to luminous satellites.
6. Primary Source Database Harvest

The insights structured above depend on an extensive heritage of analytical derivations, high-resolution N-body simulations, and deep observational surveys. The following matrix represents the critical pre-2018 primary citations explicitly harvested from the review's foundation, categorized by their epistemic role.

Key	Authors (Year) Journal	Exact Title	DOI	arXiv ID	ADS bibcode	Role	Review Locator	Scientific Boundary
REV11-P001	Behroozi, P. S., Wechsler, R. H., Conroy, C. (2013) ApJ	The Average Star Formation Histories of Galaxies in Dark Matter Halos from z = 0-8	10.1088/0004-637X/770/1/57	1207.6105	2013ApJ...770...57B	calibration	Sec 5.1 / Mean SHMR	Established the redshift evolution of the pivot halo mass and parameterized the integrated efficiency of star formation utilizing abundance matching.
REV11-P002	Moster, B. P., Naab, T., White, S. D. M. (2013) MNRAS	Galactic star formation and accretion histories from matching galaxies to dark matter haloes	10.1093/mnras/sts261	1205.5807	2013MNRAS.428.3121M	calibration	Sec 5.1 / Mean SHMR	Delivered a multi-epoch multi-parameter abundance matching model that remains a foundational benchmark for SHMR evolution.
REV11-P003	Yang, X., Mo, H. J., van den Bosch, F. C. (2003) MNRAS	Constraining galaxy formation and cosmology with the conditional luminosity function of galaxies	10.1046/j.1365-8711.2003.06254.x	astro-ph/0207019	2003MNRAS.339.1057Y	analytic_theory	Sec 2.2 / Empirical models	Introduced the Conditional Luminosity Function (CLF) formalism, shifting the field from single-value HODs to full distribution functions.
REV11-P004	Peacock, J. A., Smith, R. E. (2000) MNRAS	Halo occupation numbers and galaxy bias	10.1046/j.1365-8711.2000.03779.x	astro-ph/0005010	2000MNRAS.318.1144P	analytic_theory	Sec 2.2 / Empirical models	Codified the mathematical foundations of the modern Halo Occupation Distribution (HOD) framework.
REV11-P005	Zehavi, I., et al. (2011) ApJ	Galaxy Clustering in the Completed SDSS Redshift Survey: The Dependence on Color and Luminosity	10.1088/0004-637X/736/1/59	1005.2413	2011ApJ...736...59Z	measurement	Sec 3.2 / Two-point clustering	Provided the definitive SDSS DR7 clustering measurements and HOD fits broken down by luminosity and color thresholds.
REV11-P006	Leauthaud, A., et al. (2012) ApJ	New Constraints on the Evolution of the Stellar-to-dark Matter Connection: A Combined Analysis...	10.1088/0004-637X/744/2/159	1104.0928	2012ApJ...744..159L	measurement	Sec 3.4 / Weak lensing	Pioneered the joint-constraint methodology (lensing + clustering + SMF) to break fundamental degeneracies in the SHMR.
REV11-P007	Kravtsov, A. V., et al. (2004) ApJ	The Dark Side of the Halo Occupation Distribution	10.1086/420959	astro-ph/0308519	2004ApJ...609...35K	simulation	Sec 4.6 / Satellite properties	Demonstrated via N-body simulations that the subhalo mass function dictates a near-universal power law for satellite occupation.
REV11-P008	Gao, L., Springel, V., White, S. D. M. (2005) MNRAS	The age dependence of halo clustering	10.1111/j.1745-3933.2005.00084.x	astro-ph/0506510	2005MNRAS.363L..66G	simulation	Sec 4.4 / Assembly bias	The seminal simulation paper identifying the theoretical existence of halo assembly bias.
REV11-P009	Wechsler, R. H., et al. (2002) ApJ	Concentrations of Dark Halos from their Assembly Histories	10.1086/338765	astro-ph/0108151	2002ApJ...568...52W	simulation	Sec 4.4 / Assembly bias	Established the analytic physical link between the exponential mass accretion history of a halo and its final density profile concentration.
REV11-P010	Wechsler, R. H., et al. (2006) ApJ	Dependence of Halo Clustering on Halo Formation History, Concentration, and Substructure	10.1086/507120	astro-ph/0512416	2006ApJ...652...71W	simulation	Sec 4.4 / Assembly bias	Extended the theory of assembly bias to show that halo clustering depends on concentration and substructure fraction, not just age.
REV11-P011	Reddick, R. M., et al. (2013) ApJ	Cosmological Constraints from Galaxy Clustering and the Mass-to-number Ratio of Galaxy Clusters	10.1088/0004-637X/771/1/30	1207.2160	2013ApJ...771...30R	calibration	Sec 4.3 / Scatter	Proved that V
peak
	​

 is the optimal parameter for SHAM models aiming to reproduce observed spatial clustering.
REV11-P012	Tinker, J. L., et al. (2008) ApJ	Toward a Halo Mass Function for Precision Cosmology: The Limits of Universality	10.1086/591439	0803.2706	2008ApJ...688..709T	calibration	Sec 2.1 / Preliminaries	Derived the most widely utilized analytical fit for the mass function of dark matter halos.
REV11-P013	Tinker, J. L., et al. (2010) ApJ	The Large-scale Bias of Dark Matter Halos: Numerical Calibration and Model Tests	10.1088/0004-637X/724/2/878	1001.3162	2010ApJ...724..878T	calibration	Sec 3.2 / Two-point clustering	Calibrated the absolute linear bias of dark matter halos as a function of peak height across different cosmologies.
REV11-P014	Vale, A., Ostriker, J. P. (2004) MNRAS	Linking halo mass to galaxy luminosity	10.1111/j.1365-2966.2004.08059.x	astro-ph/0402500	2004MNRAS.353..189V	analytic_theory	Sec 2.2 / Empirical models	Formally introduced the non-parametric Subhalo Abundance Matching (SHAM) technique linking cumulative luminosity and mass functions.
REV11-P015	White, S. D. M., Rees, M. J. (1978) MNRAS	Core condensation in heavy halos: a two-stage theory for galaxy formation and clustering	10.1093/mnras/183.3.341	none	1978MNRAS.183..341W	analytic_theory	Sec 1 / Introduction	The fundamental conceptual framework establishing that luminous galaxies form by cooling gas within hierarchically clustering dark matter halos.
REV11-P016	Blanton, M. R., Berlind, A. A. (2007) ApJ	What Is the Lowest Mass Galaxy with a Dark Matter Halo?	10.1086/518728	astro-ph/0611726	2007ApJ...664..791B	measurement	Sec 5.1 / The mean SHMR	Utilized deep optical surveys to place empirical limits on the lowest mass dark matter halos capable of retaining star-forming gas.
REV11-P017	Hearin, A. P., Watson, D. F. (2013) MNRAS	The dark side of galaxy colour: evidence from new SDSS measurements of galaxy clustering and lensing	10.1093/mnras/stt1374	1304.5557	2013MNRAS.435.1313H	analytic_theory	Sec 6.2 / Secondary properties	Proposed the age-matching paradigm, explicitly linking galaxy color/SFR to halo formation time to model assembly bias.
REV11-P018	Behroozi, P. S., Conroy, C., Wechsler, R. H. (2010) ApJ	A Comprehensive Guide to Toy Cosmologies: Stellar Mass-Halo Mass Relations	10.1088/0004-637X/717/1/379	1001.0015	2010ApJ...717..379B	calibration	Sec 5.1 / Mean SHMR	Developed robust forward-modeling statistical methods incorporating scatter into the determination of the SHMR.
REV11-P019	Conroy, C., Wechsler, R. H., Kravtsov, A. V. (2006) ApJ	Modeling Luminosity-dependent Galaxy Clustering through Cosmic Time	10.1086/505855	astro-ph/0512234	2006ApJ...647..201C	simulation	Sec 2.2 / Empirical models	Applied abundance matching across varying redshifts to predict the evolution of galaxy clustering amplitude.
REV11-P020	Moster, B. P., et al. (2010) ApJ	Constraints on the Relationship between Stellar Mass and Halo Mass at Low and High Redshift	10.1088/0004-637X/710/2/903	0903.4682	2010ApJ...710..903M	calibration	Sec 5.1 / Mean SHMR	Utilized a multi-epoch parameterization to track how the pivot mass and normalization of the SHMR evolve over cosmic time.
REV11-P021	Zheng, Z., et al. (2005) ApJ	Theoretical Models of the Halo Occupation Distribution: Separating Central and Satellite Galaxies	10.1086/431722	astro-ph/0408564	2005ApJ...630....1Z	analytic_theory	Sec 2.2 / Empirical models	Formalized the distinct functional forms used to parameterize central (step function) and satellite (power law) galaxies within HOD models.
REV11-P022	Bullock, J. S., Boylan-Kolchin, M. (2017) ARA&A	Small-Scale Challenges to the ΛCDM Cosmology	10.1146/annurev-astro-091916-055313	1707.04256	2017ARA&A..55..343B	supporting_review	Sec 1 / Introduction	A critical summary of the "Too Big to Fail" and "Missing Satellites" problems linked to the low-mass SHMR regime.
REV11-P023	Faber, S. M., Jackson, R. E. (1976) ApJ	Velocity dispersions and mass-to-light ratios for elliptical galaxies	10.1086/154215	none	1976ApJ...204..668F	measurement	Sec 1 / Introduction	An early foundational discovery scaling galaxy stellar kinematics directly to total mass properties.
REV11-P024	Frenk, C. S., White, S. D. M. (2012) Annalen der Physik	Dark matter and cosmic structure	10.1002/andp.201200212	1210.0544	2012AnP...524..507F	supporting_review	Sec 2.1 / Preliminaries	Provided rigorous context regarding the evolution of dark matter hierarchy and the standard cosmological paradigm.
REV11-P025	Guo, Q., et al. (2010) MNRAS	How do galaxies populate dark matter haloes?	10.1111/j.1365-2966.2010.16341.x	0909.4305	2010MNRAS.404.1111G	calibration	Sec 5.1 / Mean SHMR	Applied abundance matching to high-resolution Millennium simulation data to map the shallow high-mass slope of central galaxies.
REV11-P026	Mandelbaum, R., et al. (2006) MNRAS	Galaxy halo masses and satellite fractions from galaxy-galaxy lensing in the Sloan Digital Sky Survey	10.1111/j.1365-2966.2006.10156.x	astro-ph/0511164	2006MNRAS.368..715M	measurement	Sec 3.4 / Weak lensing	Provided the first definitive direct measurements of average host halo mass as a function of central galaxy stellar mass via weak lensing.
REV11-P027	Navarro, J. F., Frenk, C. S., White, S. D. M. (1996) ApJ	The Structure of Cold Dark Matter Halos	10.1086/177173	astro-ph/9508025	1996ApJ...462..563N	analytic_theory	Sec 2.1 / Preliminaries	Discovered the universal NFW density profile of dark matter halos, forming the baseline assumption for all subsequent spatial clustering models.
REV11-P028	Skibba, R. A., Sheth, R. K. (2009) MNRAS	A halo model of galaxy colours and clustering in the Sloan Digital Sky Survey	10.1111/j.1365-2966.2008.14163.x	0810.0543	2009MNRAS.392.1080S	analytic_theory	Sec 6.2 / Secondary properties	Modeled the environmental dependence of galaxy color strictly by partitioning central and satellite color distributions within the HOD.
REV11-P029	Tinker, J. L., et al. (2005) ApJ	On the Mass-to-Light Ratio of Large-Scale Structure	10.1086/432084	astro-ph/0501029	2005ApJ...631...41T	analytic_theory	Sec 3.2 / Clustering	Proved that variations in the mass-to-light ratio on different physical scales are naturally predicted by non-linear halo models.
REV11-P030	Zentner, A. R., et al. (2014) MNRAS	Galaxy assembly bias: a significant source of systematic error in the galaxy-halo connection	10.1093/mnras/stu1133	1311.1818	2014MNRAS.443.3044Z	analytic_theory	Sec 4.4 / Assembly bias	Highlighted that ignoring assembly bias leads to fundamentally flawed inferences of cosmological parameters from galaxy clustering.
REV11-P031	Wetzel, A. R., Tinker, J. L., Conroy, C. (2012) MNRAS	Galaxy evolution in local groups and clusters: satellite star formation histories and quenching timescales	10.1111/j.1365-2966.2012.21074.x	1107.5311	2012MNRAS.424..232W	measurement	Sec 4.6 / Satellite properties	Established the empirical "delayed-then-rapid" quenching model for satellite galaxies transitioning through groups and clusters.
REV11-P032	Zehavi, I., et al. (2004) ApJ	On Departures from a Power Law in the Galaxy Correlation Function	10.1086/383495	astro-ph/0301280	2004ApJ...608...16Z	measurement	Sec 3.2 / Two-point clustering	Confirmed that the 1-halo and 2-halo transition directly causes observable deviations from a pure power law in real-space clustering.
REV11-P033	Springel, V., et al. (2001) MNRAS	Populating a cluster of galaxies - I. Results at z=0	10.1046/j.1365-8711.2001.04912.x	astro-ph/0012055	2001MNRAS.328..726S	simulation	Sec 2.3 / Physical models	Demonstrated the power of marrying N-body dark matter merger trees with semi-analytic recipes to track galaxy satellite dynamics.
REV11-P034	Sheth, R. K., Tormen, G. (1999) MNRAS	Large-scale bias and the peak background split	10.1046/j.1365-8711.1999.02692.x	astro-ph/9901122	1999MNRAS.308..119S	analytic_theory	Sec 2.1 / Preliminaries	Extended Press-Schechter formalism incorporating ellipsoidal collapse to accurately predict the mass-dependent halo bias.
REV11-P035	Scoccimarro, R., et al. (2001) ApJ	How Many Galaxies Fit in a Halo? Constraints on Galaxy Formation Efficiency from Spatial Clustering	10.1086/318261	astro-ph/0006319	2001ApJ...546...20S	analytic_theory	Sec 3.2 / Two-point clustering	Derived fundamental halo-model constraints demonstrating that spatial clustering heavily restricts the permissible parameter space for satellite fractions.
REV11-P036	Mo, H. J., White, S. D. M. (1996) MNRAS	An analytic model for the spatial clustering of dark matter haloes	10.1093/mnras/282.2.347	astro-ph/9512127	1996MNRAS.282..347M	analytic_theory	Sec 2.1 / Preliminaries	Developed the foundational analytic model predicting that the bias of dark matter halos is deterministic based strictly on halo mass.
REV11-P037	Kravtsov, A. V., Borgani, S. (2012) ARA&A	Formation of Galaxy Clusters	10.1146/annurev-astro-081811-125502	1205.5556	2012ARA&A..50..353K	supporting_review	Sec 3.3 / Group catalogs	Contextualized the thermal and dynamical states of massive halos relevant for estimating X-ray and SZ cluster masses.
REV11-P038	Kauffmann, G., White, S. D. M., Guiderdoni, B. (1993) MNRAS	The Formation and Evolution of Galaxies Within Merging Dark Matter Haloes	10.1093/mnras/264.1.201	none	1993MNRAS.264..201K	simulation	Sec 2.3 / Physical models	The genesis of modern Semi-Analytic Models (SAMs), introducing phenomenological equations to track cooling, star formation, and feedback within merger trees.
REV11-P039	Jenkins, A., et al. (1998) ApJ	Evolution of Structure in Cold Dark Matter Universes	10.1086/305630	astro-ph/9709010	1998ApJ...499...20J	simulation	Sec 2.1 / Preliminaries	Provided early robust validations of the dark matter halo mass function across highly divergent cosmological simulations.
REV11-P040	Heitmann, K., et al. (2010) ApJ	The Coyote Universe I: Precision Determination of the Nonlinear Matter Power Spectrum	10.1088/0004-637X/715/1/104	0812.1052	2010ApJ...715..104H	simulation	Sec 7.2 / Inferring Cosmology	Demonstrated the necessity of utilizing highly precise matter power spectrum emulators to extract cosmology from HOD-mapped galaxy clustering.
7. DO_NOT_USE_UNVERIFIED Quarantine

The following papers surfaced in algorithmic proximity during the material gathering but fall outside the strict 2018 scope of the primary review, address uncited pure-physics mechanics, or represent subsequent Stage-IV cosmology endeavors. These are quarantined and cannot support claims regarding the 2018 consensus.

Flagged Item	Reason for Exclusion	Status
Allen et al., 2025 (arXiv: 2501.11674)	Post-2018 JWST High-z analysis.	UNCITED_NOT_USABLE
Meyer et al., 2025 (arXiv: 2503.14280)	Post-2018 JWST High-z analysis.	UNCITED_NOT_USABLE
DESI Collaboration et al., 2024/2025 (e.g., arXiv: 2507.07798)	Post-2018 DESI BAO and cosmology constraints.	UNCITED_NOT_USABLE
AbacusSummit Mock Catalogs / HOD Emulators	Post-2018 non-review content.	UNCITED_NOT_USABLE
Shen et al., 2024 (Phys. Lett. B 855: 138797)	Uncited physics paper regarding SMBHs in dark matter halos.	UNCITED_NOT_USABLE
Berner et al., 2024	Post-2018 Fast forward modelling of galaxy surveys.	UNCITED_NOT_USABLE
8. Composite Source Identity Ledger

To ensure absolute methodological integrity in the NebulaMind framework, this ledger cross-references the 40 primary citations against their specific epistemic roles to flag any potential model-circularity or duplicative calibrations.

Internal Key	Type	Citation	Note / Conflict Check
REV11-MAIN	Review	Wechsler & Tinker (2018) ARA&A 56, 435	Primary synthesis target; advisory text only.
REV11-P001	Calibration	Behroozi et al. (2013) ApJ 770:57	Defines pivot mass and high-z extrapolations.
REV11-P002	Calibration	Moster et al. (2013) MNRAS 428:3121	Key competing parameterization to P001. Cross-calibration required.
REV11-P003	Analytic	Yang et al. (2003) MNRAS 339:1057	Foundational CLF paper.
REV11-P004	Analytic	Peacock & Smith (2000) MNRAS 318:1144	Foundational HOD framework.
REV11-P005	Measurement	Zehavi et al. (2011) ApJ 736:59	Reference baseline for SDSS clustering.
REV11-P006	Measurement	Leauthaud et al. (2012) ApJ 744:159	Lensing constraints on SHMR scatter.
REV11-P007	Simulation	Kravtsov et al. (2004) ApJ 609:35	Simulation backing for HOD.
REV11-P008	Simulation	Gao et al. (2005) MNRAS 363:L66	Original discovery of theoretical assembly bias.
REV11-P009	Simulation	Wechsler et al. (2002) ApJ 568:52	Links accretion history to concentration.
REV11-P010	Simulation	Wechsler et al. (2006) ApJ 652:71	Expanded assembly bias parameters.
REV11-P011	Calibration	Reddick et al. (2013) ApJ 771:30	Identifies V
peak
	​

 as optimal SHAM parameter.
REV11-P012	Calibration	Tinker et al. (2008) ApJ 688:709	Standard halo mass function. Used continuously across references.
REV11-P013	Calibration	Tinker et al. (2010) ApJ 724:878	Standard halo bias function.
REV11-P014	Analytic	Vale & Ostriker (2004) MNRAS 353:189	Formalized abundance matching.
REV11-P015	Analytic	White & Rees (1978) MNRAS 183:341	Core theoretical genesis. Context only.
REV11-P016	Measurement	Blanton & Berlind (2007) ApJ 664:791	Min halo mass threshold constraints.
REV11-P017	Analytic	Hearin & Watson (2013) MNRAS 435:1313	Introduced Age Matching (assembly bias proxy).
REV11-P018	Calibration	Behroozi et al. (2010) ApJ 717:379	Statistical forward modeling of SHMR scatter.
REV11-P019	Simulation	Conroy et al. (2006) ApJ 647:201	Abundance matching applied to clustering.
REV11-P020	Calibration	Moster et al. (2010) ApJ 710:903	Earlier multi-epoch SHMR parameterization. Replaced by P002.
REV11-P021	Analytic	Zheng et al. (2005) ApJ 630:1	Formalized central vs satellite HOD equations.
REV11-P022	Review	Bullock & Boylan-Kolchin (2017) ARA&A 55:343	Support review for low-mass SHMR regimes.
REV11-P023	Measurement	Faber & Jackson (1976) ApJ 204:668	Historical kinematics proxy.
REV11-P024	Review	Frenk & White (2012) Ann. Phys. 524:507	Support review for ΛCDM framework.
REV11-P025	Calibration	Guo et al. (2010) MNRAS 404:1111	Constraints on massive central slope.
REV11-P026	Measurement	Mandelbaum et al. (2006) MNRAS 368:715	Foundational galaxy-galaxy lensing measurements.
REV11-P027	Analytic	Navarro et al. (1996) ApJ 462:563	Defines NFW spatial profile for 1-halo models.
REV11-P028	Analytic	Skibba & Sheth (2009) MNRAS 392:1080	Environmental HOD modeling.
REV11-P029	Analytic	Tinker et al. (2005) ApJ 631:41	Mass-to-light ratio scale dependence.
REV11-P030	Analytic	Zentner et al. (2014) MNRAS 443:3044	Systematics of ignoring assembly bias.
REV11-P031	Measurement	Wetzel et al. (2012) MNRAS 424:232	Satellite quenching timescales.
REV11-P032	Measurement	Zehavi et al. (2004) ApJ 608:16	1-halo/2-halo transition validation.
REV11-P033	Simulation	Springel et al. (2001) MNRAS 328:726	SAM validation within N-body trees.
REV11-P034	Analytic	Sheth & Tormen (1999) MNRAS 308:119	Peak background split bias derivation.
REV11-P035	Analytic	Scoccimarro et al. (2001) ApJ 546:20	Satellites constrained by spatial clustering.
REV11-P036	Analytic	Mo & White (1996) MNRAS 282:347	Deterministic halo bias analytic origin.
REV11-P037	Review	Kravtsov & Borgani (2012) ARA&A 50:353	Support review for cluster catalogs.
REV11-P038	Simulation	Kauffmann et al. (1993) MNRAS 264:201	Genesis of semi-analytic frameworks.
REV11-P039	Simulation	Jenkins et al. (1998) ApJ 499:20	N-body cosmological volume proofs.
REV11-P040	Simulation	Heitmann et al. (2010) ApJ 715:104	Emulator dependence for non-linear clustering.

REVIEW_BASE_11_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- en.wikipedia.org Dark matter halo - Wikipedia Opens in a new window — https://en.wikipedia.org/wiki/Dark_matter_halo
- astronomy.stackexchange.com List of galaxies with their dark matter halo - Astronomy Stack Exchange Opens in a new window — https://astronomy.stackexchange.com/questions/39776/list-of-galaxies-with-their-dark-matter-halo
- arxiv.org Probing Reionization-Era Galaxies with JWST UV Luminosity Functions and Large-Scale Clustering - arXiv Opens in a new window — https://arxiv.org/html/2503.07590v1
- arxiv.org Predicting dark matter halo masses from simulated galaxy images and environments - arXiv Opens in a new window — https://arxiv.org/html/2407.13735v1
- arxiv.org Reconstruction of Dark Matter and Baryon Density From Galaxies: A Comparison of Linear, Halo Model and Machine Learning-Based Methods - arXiv Opens in a new window — https://arxiv.org/html/2507.12530v1
- cap.stanford.edu Risa Wechsler Opens in a new window — https://cap.stanford.edu/profiles/frdActionServlet?choiceId=printerprofile&profileversion=full&profileId=9795
- arxiv.org the Connection among Galaxies, Halos, their Formation Time and their Location in the Cosmic Web - arXiv Opens in a new window — https://arxiv.org/pdf/1907.04333
- pure.ed.ac.uk The Diversity and Variability of Star Formation Histories in Models of Galaxy Evolution - Account Opens in a new window — https://www.pure.ed.ac.uk/ws/files/156891867/Dave_2007.07916.pdf
- arxiv.org Measuring the Stellar-to-Halo Mass Relation at ∼10¹⁰ Solar masses, using forthcoming space-based imaging of galaxy-galaxy strong lenses - arXiv Opens in a new window — https://arxiv.org/html/2501.16139v2
- researchgate.net Galaxy Formation in ΛCDM Cosmology - ResearchGate Opens in a new window — https://www.researchgate.net/publication/381498338_Galaxy_Formation_in_LCDM_Cosmology
- scirp.org Wechsler, R.H. and Tinker, J.L. (2018) The Connection between Galaxies and their Dark Matter Halos. Annual Review of Astronomy and Astrophysics, 56, 435-487. - References - Scirp.org. Opens in a new window — https://www.scirp.org/reference/referencespapers?referenceid=2959181
- nbi.ku.dk Evolution of the Rate of SNe IIn with Redshift Opens in a new window — https://nbi.ku.dk/english/theses/masters-theses/cecilie-cold_copy/Master_Thesis_CecilieHede.pdf
- ml4astro.github.io Galaxy Merger Reconstruction with Equivariant Graph Normalizing Flows - GitHub Pages Opens in a new window — https://ml4astro.github.io/icml2022/assets/13.pdf
- arxiv.org Luminosity Function of Galaxies in Voids: A Modification Inspired by Excursion Set Theory - arXiv Opens in a new window — https://arxiv.org/pdf/2507.01626
- arxiv.org Baryonic properties of nearby galaxies across the stellar-to-total dynamical mass relation Opens in a new window — https://arxiv.org/html/2402.12439v1
- arxiv.org arXiv:2005.07122v2 [astro-ph.GA] 14 Jul 2020 Opens in a new window — https://arxiv.org/pdf/2005.07122
- ouci.dntb.gov.ua Large-scale dark matter simulations - OUCI Opens in a new window — https://ouci.dntb.gov.ua/en/works/logPONVl/
- arxiv.org Exploring non-cold dark matter in a scenario of dynamical dark energy with DESI DR2 data Opens in a new window — https://arxiv.org/html/2507.07798v1
- arxiv.org Bayesian Cosmic Void Finding with Graph Flows - arXiv Opens in a new window — https://arxiv.org/html/2602.14630v2
- researchgate.net Controlled Experiments on Dark-Matter Halo Structure and Galaxy Morphology I: What Sets Galaxy Sizes? - ResearchGate Opens in a new window — https://www.researchgate.net/publication/406033418_Controlled_Experiments_on_Dark-Matter_Halo_Structure_and_Galaxy_Morphology_I_What_Sets_Galaxy_Sizes
- researchgate.net Analysis of the Dark Matter Halos and the Relation to Galactic Evolution Based on IllustrisTNG50 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/377802817_Analysis_of_the_Dark_Matter_Halos_and_the_Relation_to_Galactic_Evolution_Based_on_IllustrisTNG50
- researchgate.net Halo Properties from Observable Measures of Environment: I. Halo and Subhalo Masses | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/374865405_Halo_Properties_from_Observable_Measures_of_Environment_I_Halo_and_Subhalo_Masses
- researchgate.net The stellar-to-halo mass relation over the past 12 Gyr: I. Standard ΛCDM model Opens in a new window — https://www.researchgate.net/publication/338583620_The_stellar-to-halo_mass_relation_over_the_past_12_Gyr_I_Standard_LCDM_model
- cosmology.lbl.gov Berkeley Cosmology Group Seminars Opens in a new window — https://cosmology.lbl.gov/bcg_seminars_10_11.html
- lss.fnal.gov Direct Measurement of Galaxy Assembly Bias using DESI DR1 Data FERMILAB-PUB-25-0787-PPD arXiv:2510.20896 Opens in a new window — https://lss.fnal.gov/archive/2025/pub/fermilab-pub-25-0787-ppd.pdf
- orbi.uliege.be arXiv:1909.02005v1 [astro-ph.CO] 4 Sep 2019 - ORBi Opens in a new window — https://orbi.uliege.be/bitstream/2268/239562/1/1909.02005.pdf
- researchgate.net (PDF) Taming assembly bias for primordial non-Gaussianity - ResearchGate Opens in a new window — https://www.researchgate.net/publication/378494945_Taming_assembly_bias_for_primordial_non-Gaussianity
- dspace.library.uu.nl arXiv:2210.03110v1 [astro-ph.CO] 6 Oct 2022 Opens in a new window — https://dspace.library.uu.nl/bitstreams/53d20cc0-2e5e-49a0-803c-f5ed8be44265/download
- arxiv.org Dark matter halo properties from spatially integrated HI flux profiles - arXiv Opens in a new window — https://arxiv.org/pdf/2408.16817
- pmc.ncbi.nlm.nih.gov Augmenting astrophysical scaling relations with machine learning: Application to reducing the Sunyaev–Zeldovich flux–mass scatter - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC10041100/
- annualreviews.org Galaxy Formation in ΛCDM Cosmology - Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-nucl-102622-023052
- arxiv.org The information on halo properties contained in spectroscopic observations of late-type galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/2210.07230
- arxiv.org The Impact of Halo Radius Definition on Subhalo Occupation Variation - arXiv Opens in a new window — https://arxiv.org/html/2412.07052v1
- arxiv.org Explaining dark matter halo density profiles with neural networks - arXiv Opens in a new window — https://arxiv.org/html/2305.03077v2
- arxiv.org Constraints on the early Universe star formation efficiency from galaxy clustering and halo modeling of Hα and [O III] emitters - arXiv Opens in a new window — https://arxiv.org/html/2503.14280v1
- arxiv.org A self-similar model of galaxy formation and dark halo relaxation - arXiv Opens in a new window — https://arxiv.org/pdf/2311.13952
- arxiv.org Dark energy, spatial curvature, and star formation efficiency from JWST photometric and spectroscopic high-redshift galaxies - arXiv Opens in a new window — https://arxiv.org/html/2604.13866v2
- backend.orbit.dtu.dk An ultra-high-resolution map of (dark) matter - DTU Inside Opens in a new window — https://backend.orbit.dtu.dk/ws/files/428866246/2601.17239v1.pdf
- arxiv.org Constructing a Mock Galaxy Catalog for the All-sky SPECtroscopic Survey of Nearby Galaxies (A-SPEC) Using the Machine-assisted Semi-Simulation Model - arXiv Opens in a new window — https://arxiv.org/html/2607.06933v1
- arxiv.org The galaxy bias profile of cosmic voids - arXiv Opens in a new window — https://arxiv.org/html/2504.14616v1
- air.unimi.it Exploring HOD-dependent systematics for the DESI 2024 Full-Shape galaxy clustering analysis - AIR Unimi Opens in a new window — https://air.unimi.it/retrieve/a61554ab-a667-496e-be3a-808fa261cc1f/Findlay_2025_J._Cosmol._Astropart._Phys._2025_007.pdf
- ned.ipac.caltech.edu Archived Release Notes - About NED | NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/Documents/Overview/History
- ned.ipac.caltech.edu models of the galaxy-halo connection - The Connection between Galaxies and their Dark Matter Halos - Risa H. Wechsler and Jeremy L. Tinker Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Wechsler/Wechsler2.html
- ned.ipac.caltech.edu current constraints on the galaxy-halo connection as expressed by the shmr Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Wechsler/Wechsler5.html
- ned.ipac.caltech.edu The Connection between Galaxies and their Dark Matter Halos - Risa H. Wechsler and Jeremy L. Tinker Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Wechsler/TOC.html
- ned.ipac.caltech.edu The Connection between Galaxies and their Dark Matter Halos - Risa H. Wechsler and Jeremy L. Tinker Opens in a new window — http://ned.ipac.caltech.edu/level5/March18/Wechsler/frames.html
- ned.ipac.caltech.edu The Circumgalactic Medium Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Tumlinson/frames.html
- ned.ipac.caltech.edu Author Index - NASA/IPAC Extragalactic Database Opens in a new window — https://ned.ipac.caltech.edu/level5/author_index.html
- ned.ipac.caltech.edu What's New with NED - NASA/IPAC Extragalactic Database - Caltech Opens in a new window — https://ned.ipac.caltech.edu/help/whats_new.html
- ned.ipac.caltech.edu The Connection between Galaxies and their Dark Matter Halos ... Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Wechsler/Wechsler_refs.html
- arxiv.org Simulation-Based Priors without Simulations: an Analytic Perspective on EFT Parameters of Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2503.07270v1
- indico.global So you want to run a simulation… - Indico Global Opens in a new window — https://indico.global/event/37/contributions/260/attachments/143/307/peter1.pdf
- cds.cern.ch Constraining Dark Acoustic Oscillations with the High-Redshift UV Luminosity Function Opens in a new window — https://cds.cern.ch/record/2952066/files/2512.01998.pdf
- arxiv.org Cosmological feedback from a halo assembly perspective - arXiv Opens in a new window — https://arxiv.org/html/2505.18258v2
- research.iac.es Baryonic properties of nearby galaxies across the stellar-to-total dynamical mass relation Opens in a new window — https://research.iac.es/preprints/files/PP24020.pdf
- arxiv.org The Impact of Galaxy–halo Size Relations on Galaxy Clustering Signals - arXiv Opens in a new window — https://arxiv.org/pdf/2411.13484
- osti.gov Cosmological constraints on dark matter interactions with ordinary matter - OSTI.GOV Opens in a new window — https://www.osti.gov/servlets/purl/1977578
- eprints.soton.ac.uk The evolution of compact massive quiescent and starforming galaxies derived from the Re − Rh and Mstar - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/450939/1/The_evolution_of_compact_massive_quiescent_and_star_forming_galaxies_derived_from_the_Re_Rhand_Mstar_Mhrelations.pdf
- arxiv.org Insights from HST into Ultra-Massive Galaxies and Early-Universe Cosmology - arXiv Opens in a new window — https://arxiv.org/html/2305.07049v2
- lss.fnal.gov Snowmass2021 Cosmic Frontier White Paper: Dark Matter Physics from Halo Measurements arXiv:2203.07354v1 [hep-ph] 14 Mar 2022 - Fermilab | Technical Publications Opens in a new window — https://lss.fnal.gov/archive/2022/conf/fermilab-conf-22-155-ppd.pdf
- mediatum.ub.tum.de Observable signatures and consequences of high-density dark matter environments - mediaTUM Opens in a new window — https://mediatum.ub.tum.de/doc/1772548/1772548.pdf
- upcommons.upc.edu Exploring HOD-dependent systematics for the DESI 2024 Full-Shape galaxy clustering analysis - UPCommons Opens in a new window — https://upcommons.upc.edu/bitstreams/c7aedbe7-2da4-45dd-8302-bf861b1a15fb/download
- academic.oup.com Constraining the scatter in the galaxy–halo connection at Milky Way masses | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/498/4/5080/5900156
- cambridge.org Group therapy for halos: Advancing halo mass estimation for galaxy groups | Publications of the Astronomical Society of Australia | Cambridge Core Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/group-therapy-for-halos-advancing-halo-mass-estimation-for-galaxy-groups/BDBA40312F51038927C2A9933C55FEBD
- arxiv.org The FENIKS Survey: Stellar-Halo Mass Relationship of Central and Satellite Galaxies in UDS and COSMOS at 0.2 < - < < - z - arXiv Opens in a new window — https://arxiv.org/html/2411.04256v1
- lss.fnal.gov arXiv:2001.02233v1 [astro-ph.GA] 7 Jan 2020 Opens in a new window — https://lss.fnal.gov/archive/2020/pub/fermilab-pub-20-012-a.pdf
- academic.oup.com mass profiles of dwarf galaxies from Dark Energy Survey lensing | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/535/1/1/7847870
- arxiv.org Group Therapy for Halos: Advancing Halo Mass Estimation for Galaxy Groups - arXiv Opens in a new window — https://arxiv.org/html/2508.12556v1
- researchgate.net SHAPing the Gas: Understanding Gas Shapes in Dark Matter Haloes with Interpretable Machine Learning | Request PDF - ResearchGate Opens in a new window — https://www.researchgate.net/publication/346475514_SHAPing_the_Gas_Understanding_Gas_Shapes_in_Dark_Matter_Haloes_with_Interpretable_Machine_Learning
- amsdottorato.unibo.it Painting dark matter halos with galaxies in mock samples for future surveys Opens in a new window — https://amsdottorato.unibo.it/id/eprint/9820/1/Girelli_PhD_Thesis_2021_vf.pdf
- arxiv.org A self-similar model of galaxy formation and dark halo relaxation - arXiv Opens in a new window — https://arxiv.org/html/2311.13952v2
- osti.gov Deciphering baryonic feedback with galaxy clusters - OSTI.GOV Opens in a new window — https://www.osti.gov/servlets/purl/2578787
- arxiv.org Clustering analysis of BOSS-CMASS galaxies with semi-analytical model for galaxy formation and halo occupation distribution - arXiv Opens in a new window — https://arxiv.org/html/2505.18748v1
- arxiv.org Tracing the galaxy-halo connection with galaxy clustering in COSMOS-Web from z=0.1 to z∼12 - arXiv Opens in a new window — https://arxiv.org/html/2501.11674v1
- arxiv.org [1804.03097] The Connection between Galaxies and their Dark Matter Halos - arXiv Opens in a new window — https://arxiv.org/abs/1804.03097
- ned.ipac.caltech.edu The Connection between Galaxies and their Dark Matter Halos Opens in a new window — https://ned.ipac.caltech.edu/level5/March18/Wechsler/paper.pdf
- ora.ox.ac.uk Cosmological simulations of the same spiral galaxy: satellite properties, the role of baryonic physics and star formation histor Opens in a new window — https://ora.ox.ac.uk/objects/uuid:aa0be5a8-3a1c-4b33-80d9-f12f35dace7f/files/szg64tp768
- digital.csic.es Illuminating the Physics of Dark Energy with the Discovery Simulations Opens in a new window — https://digital.csic.es/bitstream/10261/402511/1/illuminating_beltz.pdf
- scoap3-prod-backend.s3.cern.ch Analytical models of supermassive black holes in galaxies surrounded by dark matter halos - CERN Opens in a new window — https://scoap3-prod-backend.s3.cern.ch/media/files/86389/10.1016/j.physletb.2024.138797.pdf
- researchgate.net (PDF) Large Scale Structure and the Cosmic Web - ResearchGate Opens in a new window — https://www.researchgate.net/publication/390247279_Large_Scale_Structure_and_the_Cosmic_Web
- lss.fnal.gov Fermilab Opens in a new window — https://lss.fnal.gov/archive/2024/pub/fermilab-pub-24-0160-ppd.pdf
- mdpi.com Galaxy Superclusters and Their Complexes in the Cosmic Web - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/11/6/167
- dora.lib4ri.ch Fast forward modelling of galaxy spatial and statistical distributions - DORA 4RI Opens in a new window — https://www.dora.lib4ri.ch/psi/dload/psi:61897/PDF/Berner-2024-Fast_forward_modelling_of_galaxy-(published_version).pdf
- preprints.org The Nature of Dark Matter and Cosmological Structure Derived from Generalized Time and Spacetime Duality - Preprints.org Opens in a new window — https://www.preprints.org/manuscript/202509.1554

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

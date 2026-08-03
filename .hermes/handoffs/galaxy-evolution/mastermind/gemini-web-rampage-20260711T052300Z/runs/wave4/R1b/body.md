M3 RT sidecar answer — REQ_M3_RT_20260711T091128Z

Run date (UTC): 2026-07-11T15:52:00Z, operator-verified
Model: Gemini
Cards addressed: 6 of 6

Card 1 — Isolating the causal contribution of AGN feedback to central-galaxy quenching
1.1 Prior-study findings (with source links)

Recent theoretical and observational frameworks heavily prioritize integrated supermassive black hole (SMBH) mass over instantaneous active galactic nucleus (AGN) accretion rates when modeling the cessation of star formation in massive central galaxies. Piotrowska et al. [arXiv:2201.07814] deploy machine-learning Random Forest classification across three distinct cosmological hydrodynamical simulations (EAGLE, Illustris, and IllustrisTNG) alongside observational data from the Sloan Digital Sky Survey (SDSS). The classification logic indicates that SMBH mass (M
BH
	​

) serves as the most predictive parameter for identifying whether a central galaxy at z=0 is star-forming or quiescent. Conversely, the instantaneous black hole accretion rate—and by extension, current bolometric AGN luminosity—displays minimal predictive power regarding the global star-forming state of the host. The authors report that the correlation frequently observed between stellar mass (M
∗
	​

) and specific star formation rate (sSFR) drops out of statistical significance when evaluated at a fixed M
BH
	​

 [doi:10.1093/mnras/stab3673]. This decoupling suggests an association where M
∗
	​

 functions merely as a corollary tracer of M
BH
	​

 via standard co-evolutionary scaling relations, rather than acting as an independent driver of the quenching process.

Further exploring the spatial dynamics of this feedback, Wang et al. [arXiv:2510.24886] analyze the TNG50 simulation to trace the physical progression of kinetic AGN feedback across time. The authors report that kinetic AGN feedback plays two distinct roles in transitioning a galaxy toward quiescence. Initially, the feedback operates as a short-term, highly intense physical effect that suppresses star formation specifically within the central 2 kiloparsec region. Subsequently, the integrated energy injection functions as a long-term regulatory mechanism that suppresses the global gas inflow rate from the circumgalactic medium, ultimately driving the entire galaxy into extended quiescence. Additionally, other recent analyses of SDSS and intermediate-redshift CANDELS data highlight that, observationally, the central stellar gravitational potential (often tracked via internal stellar mass surface density, Σ
1
	​

) serves as the most robust available proxy for M
BH
	​

 and subsequent quiescence when direct dynamical mass measurements are unavailable [arXiv:2511.18227]. The dependence of quiescence on Σ
1
	​

 aligns with models where the build-up of the central bulge and the growth of the central black hole act in tandem to regulate cold gas availability.

1.2 What remains unknown

While the statistical association between integrated M
BH
	​

 and global quiescence is robustly tracked across the EAGLE and TNG suites, the precise microphysical coupling between the kinetic energy injected by the SMBH and the multi-phase circumgalactic medium remains poorly constrained by direct observation. It is not fully understood how the integrated energy output over billions of years physically translates into the structural stabilization of the gas reservoir on galaxy-wide scales, nor how this coupling efficiency scales across varying dark matter halo masses. Furthermore, the reliance on Σ
1
	​

 or bulge mass as an observational proxy for M
BH
	​

 assumes a universally tight co-evolutionary scaling relation, which may fray significantly at high redshift (z>3) or within specific rapid-quenching post-starburst populations. Identifying whether the chronological delay time between the primary SMBH growth phase and the final cessation of global star formation is mediated primarily by halo-mass-dependent preventative heating, or purely by internal ejective clearing of the interstellar medium, remains a critical open variable in semi-analytic galaxy evolution models.

1.3 Recommended data/survey families

To map the relationship between integrated AGN feedback and the spatial progression of quenching, large-scale optical and near-infrared integral field spectroscopy (IFS) surveys are required. At low redshift, the SDSS MaNGA and SAMI surveys provide the necessary spatially resolved stellar mass surface densities and localized star formation histories. Moving to intermediate and high redshifts, the James Webb Space Telescope (JWST) NIRSpec instrument, combined with wide-field spectroscopic surveys like DESI and the Prime Focus Spectrograph (PFS), is essential for tracking stellar population ages and estimating central black hole masses via broad-line emission in un-obscured sources. High-resolution X-ray surveys (e.g., eROSITA, Chandra, and the upcoming Athena mission) are vital for contextualizing the current thermodynamic state and cooling time of the circumgalactic medium around these massive central galaxies.

1.4 Test/decision-criteria realism (JWST/ALMA or stated alternative)

JWST/ALMA marginal here — the relevant capability is highly multiplexed optical/near-infrared spectroscopy (e.g., DESI, PFS) combined with high-resolution X-ray observatory data (e.g., Chandra, eROSITA). While JWST is exceptionally capable of mapping the deep stellar potentials and internal kinematics (Σ
1
	​

) of specific high-redshift host galaxies, isolating the historical energy deposition of AGN feedback requires tracing large-scale circumgalactic heating and building statistical distributions of M
BH
	​

 proxies across thousands of galaxies. ALMA's role is largely restricted to tracing the remaining cold molecular gas fraction, which acts as a secondary indicator of the feedback's ultimate efficiency rather than a direct probe of the historical kinetic energy injection. Therefore, wide-field statistical spectroscopic surveys and wide-field X-ray mapping of the extended hot halo represent the primary realistic criteria for advancing this particular research card.

1.5 Overclaim risks

A substantial overclaim risk arises from interpreting the output of Random Forest feature importance rankings as direct physical causation. While machine learning frameworks robustly isolate M
BH
	​

 as the primary predictive variable for identifying quiescence in simulation datasets, these models identify statistical associations within highly complex, inter-correlated arrays; they do not simulate the actual energy transfer physics. Furthermore, estimating M
BH
	​

 through photometric proxies (such as total stellar mass or central velocity dispersion) introduces severe covariances. Comparing an absolute supermassive black hole mass derived from dynamical stellar kinematic measurements against a mass derived from broad-line photometric scaling relations introduces a non-commensurable bias, potentially artificially tightening the apparent association between M
BH
	​

 and quenching simply due to the parameterization of the proxy itself.

1.6 Key papers to verify

Piotrowska et al. (2022) | arXiv:2201.07814
Bluck et al. (2022) | arXiv:2201.07814
Piotrowska et al. (2022, MNRAS) | doi:10.1093/mnras/stab3673
Wang et al. (2025) | arXiv:2510.24886
Central stellar surface density scaling | arXiv:2511.18227

Card 2 — A tracer-resolved, common-denominator census of AGN-driven outflows
2.1 Prior-study findings (with source links)

Observational efforts to map AGN-driven outflows frequently suffer from severe tracer biases, as the ionized, neutral, and molecular gas phases trace vastly different thermodynamic conditions, spatial scales, and coupling efficiencies. Bischetti et al. [arXiv:2308.05795, arXiv:2405.19401] report JWST spectroscopy of a massive galaxy experiencing rapid quenching at redshift z=2.445, detailing the presence of a powerful, extended neutral gas outflow accompanied by a relatively weak ionized gas outflow. Crucially, the authors note an absence of detectable X-ray or radio activity within the system, suggesting that extreme, mass-loaded outflow phases capable of clearing the interstellar medium (ISM) can occur during temporal windows where traditional AGN indicators are dormant, heavily obscured, or operating at low efficiencies. The mass outflow rates estimated from these neutral tracers are reported to exceed expected supernova energy injection rates, pointing to a central AGN origin for the ejective event.

In the local universe, resonant Na ID λλ 5891,5897Å absorption serves as a prominent, widely accessible tracer for neutral outflows due to its low ionization potential (5.1 eV), existing primarily in regions shielded by high dust columns where neutral hydrogen prevails [doi:10.1093/mnras/stae000]. Mainieri [arXiv:2407.17593] models AGN-driven outflows within clumpy interstellar media, emphasizing that the intrinsic multiphase structure of the host galaxy fundamentally dictates the observed scaling relations between outflow velocity, mass-loading factors, and bolometric AGN luminosity. To unify these disparate tracers and overcome single-phase biases, the SUNRISE program [arXiv:2606.30833] has been formally proposed. This initiative aims to utilize the multi-IFU, adaptive optics (AO)-assisted capabilities of the forthcoming Extremely Large Telescope (ELT/VESPER) to conduct a blind, spatially resolved, multi-phase census of AGN-driven outflows across a representative high-redshift galaxy population at cosmic noon.

2.2 What remains unknown

The physical translation factors required to map the mass carried in the highly visible, easily observable warm ionized phase (frequently traced by [OIII] λ5007 emission) to the mass carried in the dominant, massive cold molecular and neutral phases (traced by CO transitions, [CI], [CII], or Na ID absorption) remain highly uncertain and heavily system-dependent. It is unknown whether the extreme "blowout" phase observed in specific high-redshift quenching galaxies represents a universal, mandatory evolutionary bottleneck that all massive galaxies experience, or if it represents a rare, extreme stochastic event linked to unusual merger geometries. Furthermore, the thermodynamic efficiency with which fast, sub-parsec scale accretion disk winds couple to the kiloparsec-scale multi-phase ISM to drive these massive outflows lacks a verified, common-denominator theoretical model that aligns simultaneously with multi-wavelength observations across the full spectrum of AGN luminosities.

2.3 Recommended data/survey families

To conduct a true common-denominator census that mitigates phase bias, simultaneous spatial mapping of multiple gas phases across matched resolutions is obligatory. For the molecular and cold neutral phases, the Atacama Large Millimeter/submillimeter Array (ALMA) remains the paramount observatory (specifically targeting CO rotational transitions, [CI], and [CII] fine-structure cooling lines). For the warm ionized and warm neutral phases, JWST NIRSpec IFS and MIRI are required to map rest-frame optical and ultraviolet emission lines (e.g., H$\alpha$, [OIII], Na ID) at intermediate and high redshifts. In the near future, 30-meter class Extremely Large Telescopes equipped with advanced adaptive optics IFUs (like the proposed ELT/VESPER SUNRISE program) will be strictly necessary to achieve sub-kiloparsec physical resolution on blind, multi-phase population surveys.

2.4 Test/decision-criteria realism (JWST/ALMA or stated alternative)

Current JWST and ALMA survey capabilities are highly realistic and precisely engineered for targeted, single-object multiphase outflow tracking. JWST's NIRSpec IFS provides unprecedented sensitivity to mapping ionized outflows, shock fronts, and broad-line regions in individual z∼2 galaxies, while ALMA provides commensurately high-resolution sub-millimeter mapping of the cold molecular reservoirs in the exact same targets. However, for a blind, statistically representative census of multiphase outflows across the galaxy population, the limited field-of-view and intensive integration times required by deep JWST/ALMA integral-field modes render population-wide studies observationally expensive and generally unfeasible. The proposed decision criteria for a true comprehensive "census" will realistically depend on the widespread deployment of next-generation wide-field AO-IFUs on ground-based 30-meter facilities to build the necessary statistically significant sample sizes.

2.5 Overclaim risks

A severe overclaim risk involves the mathematical extrapolation of mass-loading factors from isolated, single-phase observations. Deriving a single-object absolute mass outflow rate from a warm ionized tracer (e.g., [OIII]) and comparing it beside a differently defined statistic derived from a cold molecular tracer (e.g., CO) constitutes a comparison of non-commensurable quantities. The complex assumptions regarding gas density radial profiles, local metallicity, electron temperatures, and ionization fractions required to convert a measured luminosity into an absolute mass flow rate carry order-of-magnitude systematic uncertainties. Asserting that a single detected neutral outflow explicitly shuts down star formation galaxy-wide conflates localized kinetic ejections with global thermodynamic stabilization of the entire dark matter halo.

2.6 Key papers to verify

Bischetti et al. (2024) | arXiv:2308.05795
Davies et al. (2024) | arXiv:2405.19401
Na ID local tracing | doi:10.1093/mnras/stae000
Mainieri (2024) | arXiv:2407.17593
SUNRISE ELT Program | arXiv:2606.30833

Card 3 — Distinguishing reservoir removal from inefficient star formation
3.1 Prior-study findings (with source links)

The specific physical mechanism dictating a galaxy's macroscopic departure from the star-forming main sequence (SFMS) is debated primarily along two distinct axes: the physical removal (or terminal exhaustion) of the cold molecular gas reservoir, versus a sudden drop in the star formation efficiency (SFE) of the gas that remains embedded in the disk. The SDSS-ALMA Legacy-Value Archival Gas Exploration (SALVAGE) dataset, comprising semi-resolved optical and millimetre $^{12}$CO(1–0) data for 277 local galaxies (0.02≲z≲0.25), provides a critical diagnostic framework for separating these variables [doi:10.1093/mnras/staf1980]. Wilkinson et al. (2025) report that a galaxy's baseline vertical position and scatter within the active SFMS are largely governed by the specific SFE within its central few kiloparsecs. Conversely, the actual departure from the SFMS—the primary trajectory indicating macroscopic quenching—shows a much stronger statistical association with the availability of the central molecular gas reservoir.

The SALVAGE data architecture explicitly highlights an orthogonal theoretical relationship mapping star formation evolution. If one visualizes a Cartesian coordinate space where the X-axis represents Central Molecular Gas Fraction and the Y-axis represents Star Formation Efficiency, the standard Main Sequence operates as a vertical scatter band where high gas fractions support varying levels of efficiency. The distinct "Quenching Vector," however, points orthogonally toward low central gas fractions, acting independently of the initial efficiency variations. The authors note that the global offset from the main sequence (ΔSFR) exhibits a tighter correlation with the inner gas fraction (f
gas, inner
	​

) than with the total global gas fraction, highlighting the inner 2 kpc as the most consequential physical region dictating galaxy evolution at low redshift.

Evolutionary Pathway	Primary Driver	Observable Consequence	Vector in Parameter Space
SFMS Scatter	Star Formation Efficiency (SFE)	Vertical variation in sSFR	Parallel to SFE axis
Quenching Trajectory	Central Molecular Gas Depletion	Departure from main sequence	Orthogonal to gas fraction axis

Similarly, the ALMaQUEST survey utilizes spatially resolved $^{12}$CO(1–0) mapping from ALMA alongside MaNGA optical integral-field data [arXiv:2010.01751]. Lin et al. (2020) indicate that specific star formation rate depends on both SFE and the molecular gas fraction (f
H2
	​

), noting specifically that kiloparsec-scale variations in both of these fundamental parameters can span 1 to 2 dex within individual, resolved galaxies. At higher redshifts, an ALMA Band 7 continuum study of 57 massive star-forming galaxies at 1.45<z<1.70 from the FMOS-COSMOS survey [arXiv:2605.23662] evaluates these relationships during the peak of cosmic star formation. The continuum data suggest that across the main sequence, both the molecular gas mass ratio and SFE scale approximately as (sSFR/sSFR
MS
	​

)
0.5
. The authors suggest this indicates the main sequence scatter is driven nearly equally by variations in total gas content and local depletion time at z∼1.5. Furthermore, studies of bar-driven resonance systems utilizing ALMaQUEST data report that barred galaxies hosting radial gas flows display suppressed global star-formation efficiencies [arXiv:2312.14702], implicating internal secular dynamics in modulating gas consumption.

3.2 What remains unknown

While observations increasingly indicate that central gas depletion is the most proximal indicator of quenching, the underlying physical trigger responsible for removing or stabilizing this central gas reservoir remains deeply ambiguous. It is unclear whether the gas is violently expelled from the potential well via AGN-driven ejective feedback, rapidly consumed in an un-replenished central starburst, or rendered inert against gravitational collapse (known as morphological quenching or stabilization) while retaining a significant portion of its mass. Furthermore, the role of radial molecular gas flows in either fueling or starving the central 2 kpc—particularly the specific kinematic influence of galactic bars and non-axisymmetric potentials in driving this inflow—requires substantially larger matched kinematic samples to statistically link bar-driven resonance systems with permanent drops in global star-formation efficiency.

3.3 Recommended data/survey families

Isolating gas fractions from star formation efficiency inherently requires matched-resolution maps of both the molecular gas surface density and the stellar mass/star-formation surface density across the exact same spatial scales. The direct combination of ALMA (for sub-millimeter $^{12}$CO mapping) and wide-field optical integral-field spectroscopy (such as SDSS MaNGA or the SAMI survey) represents the absolute gold standard for extracting these measurements. The ongoing KILOGAS survey, designed to map CO(2-1) at 1 kpc resolution across approximately 500 local galaxies, is highly recommended for expanding these dual-tracer correlation analyses to a fully representative local galaxy population.

3.4 Test/decision-criteria realism (JWST/ALMA or stated alternative)

ALMA capabilities are exceptionally realistic and precisely tailored for these decision criteria. Deriving molecular gas fractions and local star formation efficiencies requires deep, high-resolution sub-millimeter interferometry to trace CO rotational transitions or dust continuum emission, a technical task where ALMA provides unmatched sensitivity and spatial resolution. JWST is similarly highly relevant and realistic here, as its MIRI and NIRCam instruments are strictly required to accurately map the resolved stellar mass surface densities and heavily obscured star formation rates of the host galaxies at high redshift. The combination of ALMA and JWST provides the critical numerator (SFR) and denominator (gas mass and stellar mass) for the efficiency calculations at cosmic noon.

3.5 Overclaim risks

Evaluating the inner gas fraction (f
gas, inner
	​

) of a resolved local galaxy population set beside the global, aperture-integrated gas fraction (f
gas, total
	​

) of a different high-redshift sample involves non-commensurable estimands; such statistics reflect fundamentally different physical zones within the gravitational potential and cannot be directly equated to claim evolutionary trends. Additionally, claiming that a derived low SFE universally implies the active presence of preventative AGN feedback risks severe overclaiming, as purely structural changes (like the secular growth of a dominant central stellar bulge) can radically alter the shear profile of the galaxy and dynamically stabilize the molecular disk against fragmentation without any active energetic feedback input.

3.6 Key papers to verify

Wilkinson et al. (SALVAGE) | doi:10.1093/mnras/staf1980
Lin et al. (2020, ALMaQUEST) | arXiv:2010.01751
Hogarth et al. (2024, ALMaQUEST XIV) | arXiv:2312.14702
FMOS-COSMOS ALMA Band 7 | arXiv:2605.23662

Card 4 — An observational determination of the maintenance-heating duty cycle
4.1 Prior-study findings (with source links)

Maintenance-heating—frequently referred to in literature as "radio-mode" or preventative feedback—operates by injecting mechanical energy into the circumgalactic medium (CGM) or intracluster medium (ICM) to offset continuous radiative cooling, thereby suppressing subsequent cold gas accretion onto the central galaxy. Observational determinations of this complex duty cycle heavily rely on low-frequency radio continuum surveys mapping remnant jet emission and X-ray observations detailing localized cavity structures in the hot halo. Using the LOFAR Two-metre Sky Survey (LoTSS) Deep Fields, Pierce et al. [arXiv:2604.19865] analyze a large sample of 5,187 radio AGN objects to derive integrated jet kinetic luminosity functions extending out to z=2.5. The authors report an estimated total kinetic power output per comoving volume of approximately 10
32
−10
33
 W Mpc$^{-3}$ across the specified redshift range, indicating a moderate positive evolution in power density from z=0 to 1.

In the high-energy regime, the eROSITA Final Equatorial-Depth Survey (eFEDS) provides critical wide-field mappings of Brightest Cluster Galaxies (BCGs) and their associated radio-loud AGN populations [arXiv:2106.14524]. Studies comparing low-frequency radio luminosity against total kinetic luminosity in these systems indicate that the radiative cooling losses of the central ICM are in an overall thermodynamic balance with the mechanical heating provided by the central AGN. To contextualize these observational findings within theoretical cosmological frameworks, Prunier et al. [arXiv:2410.21366, arXiv:2503.01965] evaluate the TNG-Cluster magnetohydrodynamic simulations, producing detailed mock Chandra X-ray observations of 352 massive simulated clusters at z=0. In TNG-Cluster, the incidence of X-ray cavities (tracer: 10
8
 K X-ray depleted regions, selection: volume-limited M
500c
	​

=10
14−14.8
M
⊙
	​

, denominator: 352 central simulated clusters, redshift range: z=0) is reported at 39%. A matched comparative analysis with 35 real, physical clusters observed by the Chandra observatory reports a detected X-ray cavity fraction (tracer: X-ray surface brightness depressions, selection: volume-limited M
500c
	​

=10
14−14.8
M
⊙
	​

, denominator: 35 physical clusters, redshift range: z≤0.071) of 43%, displaying an alignment between the simulated magnetohydrodynamic kinetic injection models and localized empirical observations.

4.2 What remains unknown

The specific physical and kinetic processes governing the precise dissipation of highly collimated mechanical jet energy into the diffuse thermal energy of the intracluster medium remain largely unconstrained by current observations. While structural X-ray cavities and AGN-driven shock fronts represent visible, macroscopic manifestations of this feedback cycle, it is unknown exactly how much kinetic energy is dissipated via weak sound waves at significantly larger cluster radii versus the energy transferred through thermal conduction from hotter outer layers [arXiv:2509.25314]. Furthermore, the temporal duty cycle itself—defined as the exact mathematical fraction of time a massive central galaxy spends in an actively jetted, heating phase versus a quiescent, radiatively cooling phase—cannot be precisely determined from static observational snapshot surveys. The physical fading time of radio lobes and the buoyant rise time of X-ray cavities through the viscous ICM introduce substantial chronometric uncertainties into any temporal model.

4.3 Recommended data/survey families

Tracing the signatures of maintenance heating fundamentally requires observing the large-scale physical interaction between relativistic AGN jets and the hot, extended halo gas. Low-frequency radio interferometric arrays, particularly LOFAR, the upcoming Square Kilometre Array (SKA), and the Very Large Array (VLA), are strictly necessary to detect the older, steeper-spectrum electron populations trapped in fossil radio lobes that trace historical outbursts. Simultaneously, mapping the thermodynamic state, density, and cooling times of the hot halo gas relies entirely on highly sensitive X-ray observatories. The ongoing eROSITA all-sky survey (eRASS) and deep, targeted archival datasets from the Chandra X-ray Observatory are the optimal survey families for identifying structural X-ray cavities and measuring broad ICM cooling profiles.

4.4 Test/decision-criteria realism (JWST/ALMA or stated alternative)

JWST/ALMA marginal here — the relevant capability is low-frequency radio astronomy (e.g., LOFAR, SKA) and wide-field X-ray astronomy (e.g., eROSITA, Chandra, Athena). Maintenance heating typically occurs on massive spatial scales of hundreds of kiloparsecs within a highly ionized, 10
7
−10
8
 K diffuse plasma. This process manifests observationally primarily through low-frequency synchrotron emission from relativistic electrons and thermal bremsstrahlung radiation in the soft and hard X-ray regimes. JWST's highly sensitive near-infrared capabilities and ALMA's sub-millimeter interference bands are virtually blind to these specific thermodynamic and non-thermal physical conditions. Consequently, evaluating the global maintenance-heating duty cycle realistically depends on the continued operation and deep analysis of large-scale, low-frequency radio and high-energy X-ray survey programs.

4.5 Overclaim risks

Estimating total kinetic jet power from generalized empirical scaling relations applied to rest-frame radio luminosities carries a significant risk of severe overestimation, as these generalized relations frequently neglect critical variations in local ICM environmental density, source physical size, and localized magnetic field strengths. Asserting that the singular detection of an X-ray cavity explicitly balances the long-term cooling flow of an entire galaxy cluster assumes continuous, perfectly spherically symmetric heating, erroneously extrapolating a highly episodic, highly directional energy injection into a generalized global thermostat. Furthermore, direct comparisons of radio AGN temporal duty cycles derived from high-frequency (GHz) surveys with those derived from low-frequency (MHz) surveys involve non-commensurable timescales, as higher-energy cosmic ray electrons age, radiate their energy, and fade from view exponentially faster than their low-energy counterparts.

4.6 Key papers to verify

Pierce et al. (2026, LoTSS) | arXiv:2604.19865
Prunier et al. (2025, TNG-Cluster) | arXiv:2503.01965
eFEDS BCG study | arXiv:2106.14524
TNG-Cluster X-ray Cavities | arXiv:2410.21366
ICM Heating mechanisms | arXiv:2509.25314

Card 5 — Forward-modeled validation of simulation feedback predictions
5.1 Prior-study findings (with source links)

Validating the complex, often highly parameterized sub-grid feedback prescriptions utilized in modern cosmological hydrodynamical simulations increasingly relies on forward-modeling theoretical outputs directly into the exact observational domains and instrumental noise parameters of empirical surveys. The CAMELS suite of simulations actively explores the macroscopic effects of systematically varying stellar and AGN feedback parameterizations on global star formation histories across thousands of distinct simulated volumes [arXiv:2508.21152]. To rigorously and statistically test these variations against observed data, advanced approaches like Simulation-Based Inference (SBI) are being deployed. SBI frameworks allow researchers to learn highly flexible neural density approximations of the posterior distributions of physical parameters directly from forward-modeled mock galaxy populations [arXiv:2601.20930]. By passing distributions of timescale-sensitive observables through machine-learning normalizing flows, these sophisticated inference architectures capture deep correlations and non-Gaussian features that traditional explicit-likelihood analyses frequently miss or oversimplify.

SimBIG presents an advanced, high-impact application of this SBI methodology, applying simulation-based inference to a vast catalog of 109,636 galaxies derived from the BOSS survey [PMC10589614]. The approach specifically exploits high-fidelity cosmological simulations combined with machine learning to extract precise cosmological constraints directly from highly non-linear, small-scale galaxy clustering regimes, entirely bypassing the mathematical limitations of standard summary statistics like two-point power spectra. Similarly, targeted studies evaluating the theoretical abundance of extremely faint galaxies utilize forward-modeled mock light cones extracted from the TNG100 simulation box. These studies compare synthesized H-band (F160W) mock survey images directly to the empirical CANDELS GOODS-South deep fields to ensure that complex instrumental selection functions, redshift uncertainties, and source confusion are realistically and holistically incorporated into the model validation [arXiv:2605.15893, arXiv:2604.26823].

5.2 What remains unknown

A profound, highly resilient degeneracy persists between different feedback channels in these models. It is exceptionally difficult to break the theoretical degeneracy between highly aggressive stellar feedback (e.g., implementing extreme supernova wind mass-loading factors at high redshift) and early, preventative AGN kinetic feedback, as both specific parameterizations can produce structurally similar present-day quiescent galaxy mass functions within the simulations. While forward modeling expertly inserts realistic observational noise and instrumental limits, it remains entirely unknown whether the complex neural density estimators trained on a specific simulation suite (like IllustrisTNG or SIMBA) learn universal, underlying physical truths, or if they simply mathematically overfit to the idiosyncratic hydrodynamic solvers, spatial resolutions, and rigid sub-grid scaling relations inherent to that specific proprietary code base.

5.3 Recommended data/survey families

Validating these theoretical models requires massive, highly complete statistical samples of galaxies with exquisitely well-defined selection functions, alongside corresponding terabyte-scale synthetic mock catalogs. Upcoming and current wide-field spectroscopic galaxy surveys like DESI, PFS, the ESA Euclid mission, and the Nancy Grace Roman Space Telescope provide the massive cosmic volumes and statistical power needed for these rigorous tests. On the theoretical and computational side, comprehensive simulation suites that systematically and continuously vary sub-grid feedback parameters across a wide grid—such as the CAMELS project or the expanded IllustrisTNG suite—are strictly required to generate the necessary, diverse training data for simulation-based inference neural architectures.

5.4 Test/decision-criteria realism (JWST/ALMA or stated alternative)

JWST is highly realistic and uniquely positioned for testing forward-modeled predictions in the early universe (z>3). The exceptionally deep, high-resolution near-infrared images provided by the NIRCam instrument serve as the empirical ground-truth against which forward-modeled synthetic light cones (e.g., from TNG50 or FIRE-2) must be compared to directly validate assumed feedback efficiencies during the epoch of reionization. ALMA is similarly highly realistic for forward-modeling dust continuum emission and complex molecular gas kinematics at cosmic noon. However, for large-scale cosmological parameter inference relying on dark matter halo clustering (like the SimBIG framework), wide-field observatories like Euclid and the Roman Space Telescope are the more directly relevant instrument families due to the sheer, unprecedented cosmic volumes required to successfully minimize cosmic variance.

5.5 Overclaim risks

The primary overclaim risk in forward modeling and SBI is the insidious "simulation-bias" trap. Claiming that a specific set of physical parameters is precisely and universally constrained by observational data via SBI risks severe overclaiming if the inference network was trained exclusively on a single family of hydrodynamic models. If the underlying base simulation suite fundamentally misrepresents the physics of the multiphase ISM structure (a common, acknowledged limitation of kiloparsec-resolution cosmological simulations that utilize sub-grid equations of state), the resulting neural network will confidently return highly precise, but entirely inaccurate, posterior distributions. Comparing absolute SFR medians across simulation outputs with matched-control differences in observational surveys is non-commensurable. Any physical model constraints derived from SBI must be explicitly caveated as conditionally dependent upon the base simulation's inherent physical assumptions.

5.6 Key papers to verify

Lovell et al. (2025, CAMELS) | arXiv:2508.21152
SBI for SFH models | arXiv:2601.20930
SimBIG BOSS analysis | PMC10589614
Mock faint galaxies TNG100 | arXiv:2605.15893
Mujic Forward Model | arXiv:2604.26823

Card 6 — Rebalancing the multi-channel evidence base: chemical, structural, high-redshift
6.1 Prior-study findings (with source links)

The evolutionary tracking of galaxy quenching is undergoing a rapid paradigm shift driven by recent high-redshift spectroscopic confirmations and detailed chemical abundance mappings derived from deep absorption-line studies. In a comprehensive 2026 review, Whitaker & Bezanson [arXiv:2606.12156] synthesize current multi-wavelength observations to propose two broad, distinct modes by which massive galaxies form and subsequently quench. The first mode involves a rapid, early shutdown driven by supermassive black hole outflows operating on exceedingly short temporal timescales at high redshift. The second mode proceeds far more gradually at later epochs through slow gas exhaustion, halo virial heating, or continuous preventative feedback. Crucially, the review highlights stellar archaeological evidence: the earliest massive quiescent stellar populations show incredibly rapid formation histories and exceptionally high metallicities, with heavily enhanced α-elemental abundances ([α/Fe]) that are often structurally and chemically distinct from their massive local-universe analogs.

High-redshift observational campaigns are actively identifying the direct progenitors of these rapid-quenching pathways in real-time. The DeepDive JWST/NIRSpec program reports the direct spectroscopic confirmation of dense, overpopulated regions containing massive quiescent galaxies (QGs) forming synchronously in the early universe [arXiv:2604.21007]. Kakimoto et al. (2026) detail the robust confirmation of multiple QGs situated within a prominent protocluster environment centralized around the target SXDS-27434 at z=4.01, noting explicitly that the local galaxy number density in this region is three times higher than the surrounding field average. Detailed SED fitting suggests these cluster-member QGs follow remarkably similar star formation histories and exhibit consistent, synchronous quenching epochs. Furthermore, the detection of AGN-driven broad H$\alpha$ emission lines in some of these cluster members indicates an observable association between large-scale environmental overdensities, enhanced early merger activity, and the synchronized triggering of rapid AGN feedback.

6.2 What remains unknown

While the presence of extreme α-enhancement in early quiescent galaxies indicates incredibly brief, intense starburst phases prior to quenching (as star formation must halt before delayed Type Ia supernovae can enrich the ISM with substantial iron), the precise physical mechanisms that abruptly halt star formation so efficiently remain fiercely debated. It is fundamentally unknown whether the synchronous quenching observed in high-redshift protoclusters is predominantly a product of internal, mass-driven AGN feedback that merely occurs simultaneously due to accelerated hierarchical mass assembly, or if external environmental processes (like extreme early ram-pressure stripping or violent protocluster shock heating) play a direct, causal role at z>3. Furthermore, tracking the exact structural evolution—specifically, determining exactly how these highly compact, dense early quiescent cores slowly accrete mass via dry mergers to become the extended, diffuse ellipticals seen in the local universe today—lacks continuous, empirical kinematic tracing across the observational "redshift desert."

6.3 Recommended data/survey families

Unraveling deep chemical and structural evolution requires exceptionally deep, rest-frame optical spectroscopy to accurately measure subtle stellar absorption indices (e.g., Balmer absorption lines, Mg b, Fe lines) and complex emission line ratios. JWST's NIRSpec (specifically utilizing medium-resolution gratings like G235M/G395M) and NIRCam high-resolution imaging are absolutely paramount for extracting these sensitive diagnostics from populations at z>2. The dedicated DeepDive survey and the extensive Blue Jay Survey [arXiv:2604.18522] currently represent the optimal, state-of-the-art data families for tracking this multi-channel chemical and structural evidence in the early universe. At low to intermediate redshifts, the LEGA-C survey provides the necessary high signal-to-noise structural and chemical baseline against which all high-redshift observations must eventually be compared.

6.4 Test/decision-criteria realism (JWST/ALMA or stated alternative)

JWST is the definitive, indispensable instrument for dominating this specific research domain. The core decision criteria regarding the chemical abundances, complex star formation histories, and structural compactness of massive quiescent galaxies at z>3 rely entirely on the unprecedented sensitivity, spatial resolution, and infrared wavelength coverage provided exclusively by JWST's spectrographs. ALMA serves a highly complementary and highly realistic role by tracking the residual dust continuum and heavily depleted molecular gas reservoirs (via high-J CO transitions or [CI] emission) within these recently quenched, high-redshift populations, actively testing for the presence of any remaining obscured fuel in these fast-quenched systems.

6.5 Overclaim risks

Comparing the absolute metallicities or specific α-enhancements derived from differing stellar population synthesis (SPS) models introduces significant, often unrecognized systematic errors. Any absolute quantity, such as metallicity or age, derived under a specific stellar initial mass function (IMF) or assumed dust attenuation law set beside a differently defined statistic derived under an alternative IMF must be explicitly labeled non-commensurable; they cannot be directly compared to establish evolutionary timelines. Furthermore, claiming that the structural size evolution of massive galaxies from z=3 to z=0 is entirely internally driven by adiabatic expansion risks severe overclaiming, as post-quenching minor mergers fundamentally reshape the outer envelopes of massive galaxies, disrupting ordered rotation and inflating half-light radii entirely independently of the primary, early quenching mechanism.

6.6 Key papers to verify

Whitaker & Bezanson (2026, Review) | arXiv:2606.12156
Kakimoto et al. (2026, DeepDive) | arXiv:2604.21007
Blue Jay Survey overview | arXiv:2604.18522
DeepDive QG properties | arXiv:2602.02485

Links ledger

Piotrowska et al. (2022) | arXiv:2201.07814 | QUARANTINED_PENDING_LOCAL_CHECK
Bluck et al. (2022) | arXiv:2201.07814 | QUARANTINED_PENDING_LOCAL_CHECK
Piotrowska et al. (2022, MNRAS) | doi:10.1093/mnras/stab3673 | QUARANTINED_PENDING_LOCAL_CHECK
Wang et al. (2025) | arXiv:2510.24886 | QUARANTINED_PENDING_LOCAL_CHECK
Central stellar surface density scaling | arXiv:2511.18227 | QUARANTINED_PENDING_LOCAL_CHECK
Bischetti et al. (2024) | arXiv:2308.05795 | QUARANTINED_PENDING_LOCAL_CHECK
Davies et al. (2024) | arXiv:2405.19401 | QUARANTINED_PENDING_LOCAL_CHECK
Na ID local tracing | doi:10.1093/mnras/stae000 | QUARANTINED_PENDING_LOCAL_CHECK
Mainieri (2024) | arXiv:2407.17593 | QUARANTINED_PENDING_LOCAL_CHECK
SUNRISE ELT Program | arXiv:2606.30833 | QUARANTINED_PENDING_LOCAL_CHECK
Wilkinson et al. (SALVAGE) | doi:10.1093/mnras/staf1980 | QUARANTINED_PENDING_LOCAL_CHECK
Lin et al. (2020, ALMaQUEST) | arXiv:2010.01751 | QUARANTINED_PENDING_LOCAL_CHECK
Hogarth et al. (2024, ALMaQUEST XIV) | arXiv:2312.14702 | QUARANTINED_PENDING_LOCAL_CHECK
FMOS-COSMOS ALMA Band 7 | arXiv:2605.23662 | QUARANTINED_PENDING_LOCAL_CHECK
Pierce et al. (2026, LoTSS) | arXiv:2604.19865 | QUARANTINED_PENDING_LOCAL_CHECK
Prunier et al. (2025, TNG-Cluster) | arXiv:2503.01965 | QUARANTINED_PENDING_LOCAL_CHECK
eFEDS BCG study | arXiv:2106.14524 | QUARANTINED_PENDING_LOCAL_CHECK
TNG-Cluster X-ray Cavities | arXiv:2410.21366 | QUARANTINED_PENDING_LOCAL_CHECK
ICM Heating mechanisms | arXiv:2509.25314 | QUARANTINED_PENDING_LOCAL_CHECK
Lovell et al. (2025, CAMELS) | arXiv:2508.21152 | QUARANTINED_PENDING_LOCAL_CHECK
SBI for SFH models | arXiv:2601.20930 | QUARANTINED_PENDING_LOCAL_CHECK
SimBIG BOSS analysis | PMC10589614 | QUARANTINED_PENDING_LOCAL_CHECK
Mock faint galaxies TNG100 | arXiv:2605.15893 | QUARANTINED_PENDING_LOCAL_CHECK
Mujic Forward Model | arXiv:2604.26823 | QUARANTINED_PENDING_LOCAL_CHECK
Whitaker & Bezanson (2026, Review) | arXiv:2606.12156 | QUARANTINED_PENDING_LOCAL_CHECK
Kakimoto et al. (2026, DeepDive) | arXiv:2604.21007 | QUARANTINED_PENDING_LOCAL_CHECK
Blue Jay Survey overview | arXiv:2604.18522 | QUARANTINED_PENDING_LOCAL_CHECK
DeepDive QG properties | arXiv:2602.02485 | QUARANTINED_PENDING_LOCAL_CHECK

GEMINI_WEB_M3_RT_OUTPUT_DONE_REQ_M3_RT_20260711T091128Z

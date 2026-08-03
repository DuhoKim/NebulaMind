Joint C1 answer — REQ_JOINT_C1_20260711T100139Z

Run date (UTC): 2026-07-12T04:11:41Z
Model: Gemini 1.5 Pro
Simulations covered: 8

Calibration ledger
Simulation (method-paper citation)	Stated calibration targets (observable + dataset, faithful to the source wording)	Feedback parameters tuned (as stated)	Explicitly emergent (stated NOT calibrated)	Notes
IllustrisTNG [https://arxiv.org/abs/1703.02970, https://www.tng-project.org/data/docs/background/, https://academic.oup.com/mnras/article/475/1/648/4683271]	"galaxy stellar mass function and the stellar-to-halo mass relation, the total gas mass content within the virial radius... galaxy size... black hole mass... cosmic star formation rate density as a function of redshift... distribution of galaxy optical colors in stellar mass bins"	"AGN feedback parameters" (specifically χ
0
	​

 and β tuned to 0.002 and 2, respectively)	"Properties of the simulation which have not been directly used to calibrate against observations... are then predictive in nature."	Incorporates new kinetic black hole feedback and revised galactic winds compared to the original Illustris model framework.
EAGLE [https://academic.oup.com/mnras/article/450/2/1937/984366, https://arxiv.org/abs/1407.7040, https://academic.oup.com/mnras/article/446/1/521/1316115]	"calibrated to the z∼0 galaxy stellar mass function and the amplitude of the galaxy-central black hole mass relation, also taking galaxy sizes into account."	"subgrid efficiency of the AGN feedback... subgrid efficiency of the feedback from star formation"	"unimportant for observables other than the masses of BHs" ; "Simulations adopting this calibration also reproduce the observed present-day colours of galaxies"	Employs stochastic thermal energy injection to minimize artificial numerical radiative losses.
SIMBA [https://arxiv.org/abs/1901.10203, https://academic.oup.com/mnras/article/536/1/145/7903412]	"broadly tuned to match observations of the galaxy stellar mass function evolution and the stellar mass–black hole mass relation" ; "X-ray feedback mode is included primarily to obtain enough fully quenched galaxies at z = 0"	"free parameters in the feedback model" (including AGN momentum flux, jet threshold mass, radiative efficiency, and X-ray heating rates)	"H I and H2 fractions... mass-metallicity relation at z=0,2... star-forming galaxy sizes... hot gas fractions in massive halos... z=0 galaxy dust properties"	First cosmological-scale simulation to explicitly model thermal energy input from X-ray heating processes alongside bipolar kinetic jets.
FIRE/FIRE-2 [https://academic.oup.com/mnras/article/480/1/800/5046474, https://arxiv.org/abs/1311.2073, https://academic.oup.com/mnras/article/445/1/581/988797]	NONE_FOUND (Explicitly states: "there is no fine-tuning or direct calibration of any parameters in the simulations to match these observations" and utilizes "zero adjusted parameters")	NONE_FOUND (Models utilize "values calibrated from simple test problems")	"reproduce the observed relation between stellar and halo mass up to M_halo~10^12 M_sun... stellar mass function... Kennicutt relation... metallicities... morphologies"	Focuses on resolving the multiphase ISM and implementing stellar feedback inputs directly from stellar population synthesis models.
ROMULUS [https://academic.oup.com/mnras/article/470/1/1121/3828081]	"Stellar Mass Halo Mass (SMHM) relation... SMBH Mass vs. Host Stellar Mass Relation... Progenitor Color Evolution" (matches Moster et al. 2013, Schramm & Silverman 2013, CANDELS/ZFOURGE data)	"sub-grid models governing star formation, stellar feedback, and SMBH growth/feedback" (specifically SN feedback efficiency ϵ
SN
	​

, SMBH accretion boost factor β, and feedback efficiency ϵ
f
	​

)	"SMBH dynamics... frequency and mass ratio distribution of SMBH mergers"	Utilizes a Gaussian process Kriging technique to traverse and dynamically optimize the multi-dimensional parameter space.
ASTRID [https://academic.oup.com/mnras/article/512/3/3703/6546174, https://academic.oup.com/mnras/article/548/1/stag375/8650959]	"calibrated to match the observed z = 0 galaxy stellar mass function... SMR, and BH masses at high stellar masses"	AMBIGUOUS_IN_SOURCE ("Some of the parameters of the CCSN and AGN feedback subgrid models were adjusted from their values in the fiducial models to maintain agreement")	"UV luminosity functions... specific star formation rates (SFRs)"	Contains models for inhomogeneous hydrogen and helium reionization, and subgrid dynamical friction to model massive black hole mergers.
FLAMINGO [https://academic.oup.com/mnras/article/526/4/6103/7291940, https://arxiv.org/abs/2306.04024]	"observed low-redshift galaxy stellar mass function and cluster gas fractions (f
gas,500c
	​

)"	"f
SN
	​

... Δv
SN
	​

... β
BH
	​

... ΔT
AGN
	​

 or v
jet
	​

"	"matter power spectrum... cluster scaling relations and thermodynamic profiles"	Replaces human hand-tuning with machine learning via Gaussian process emulators trained on Latin hypercubes to avoid parameter-selection bias.
BAHAMAS [https://arxiv.org/abs/1603.02702, https://academic.oup.com/mnras/article/465/3/2936/2417021, https://pmc.ncbi.nlm.nih.gov/articles/PMC10602225/]	"calibrated to reproduce the present-day galaxy stellar mass function and the hot gas mass fractions of groups and clusters"	"subgrid models of stellar and Active Galactic Nucleus (AGN) feedback" (including target heating temperature ΔT
heat
	​

 and kick velocities v
w
	​

)	"various observed mappings between galaxies, hot gas, total mass, and black holes"	Extends the calibration philosophy used by EAGLE to explicitly include gas fractions to accurately model the overall dark matter distribution.

The methodological framework underlying the calibration of major galaxy-formation simulations reveals a significant structural divide in computational astrophysics. This divide typically separates macroscopic, cosmological-volume models—which strictly require macro-observable tuning due to their inability to resolve the multiphase interstellar medium (ISM)—from high-resolution, "zoom-in" models that attempt to implement stellar feedback directly from parsec-scale physics without cosmological calibration [https://academic.oup.com/mnras/article/526/4/6103/7291940]. Suites such as IllustrisTNG, EAGLE, SIMBA, ASTRID, FLAMINGO, and BAHAMAS operate at spatial and mass resolutions where the intricate, multiphase structure of the ISM and the immediate accretion disk environments of supermassive black holes (SMBHs) remain strictly unresolved [https://arxiv.org/abs/1407.7040].

Consequently, the subgrid formulations employed in these large-volume simulations act as effective empirical models, converting computationally resolved large-scale gas properties (such as density, temperature, and metallicity averaged over kiloparsec scales) into subgrid star formation and feedback events. Because the specific physical energy injection mechanisms—for example, the exact partitioning of a supernova's 10
51
 ergs of energy into thermal heating versus kinetic momentum, or the precise coupling efficiency of an AGN's accretion energy to the surrounding intracluster medium—cannot be derived from first principles at these macroscopic scales, the parameters dictating these efficiencies are fundamentally degenerate [https://academic.oup.com/mnras/article/475/1/648/4683271]. If a simulation attempts to inject thermal energy directly into coarse, dense gas resolution elements, the energy is radiated away almost instantly due to artificially high cooling rates, a numerical artifact known as the "overcooling problem" [https://academic.oup.com/mnras/article/446/1/521/1316115].

To bypass these numerical losses and break parameter degeneracies, project teams explicitly force their models to reproduce fundamental macroscopic observables. Universally, the Galaxy Stellar Mass Function (GSMF) at z=0 and the scaling relationship between the central black hole mass and the host galaxy's stellar mass serve as the primary anchors for calibration [https://academic.oup.com/mnras/article/450/2/1937/984366]. For example, the EAGLE project utilizes stochastic thermal energy injection (heating adjacent gas particles by a fixed temperature increment ΔT) to ensure the injected energy overcomes the cooling threshold [https://academic.oup.com/mnras/article/446/1/521/1316115]. The probability of these heating events, and the subgrid efficiencies regulating them, were systematically varied until the simulated universe produced a GSMF that matched observational constraints [https://arxiv.org/abs/1407.7040].

The SIMBA simulation expands upon the complexity of subgrid tuning by introducing multifaceted feedback vectors designed to replicate highly specific observational targets [https://arxiv.org/abs/1901.10203]. Building on its predecessor MUFASA, SIMBA incorporates torque-limited accretion models for cold gas and Bondi accretion for hot gas [https://arxiv.org/abs/1901.10203]. However, its most notable calibration choice involves its AGN feedback architecture. SIMBA implements kinetic bipolar outflows that scale with Eddington ratios, alongside a highly specific X-ray heating mode [https://arxiv.org/abs/1901.10203]. The method papers state that this X-ray feedback mode was included and tuned "primarily to obtain enough fully quenched galaxies at z = 0" [https://academic.oup.com/mnras/article/536/1/145/7903412]. This exemplifies a calibration philosophy where specific physical mechanisms are introduced and adjusted to resolve macroscopic tensions in the simulated galaxy population.

Conversely, the FIRE (Feedback In Realistic Environments) project occupies an entirely different methodological niche, operating under a "bottom-up" philosophy [https://academic.oup.com/mnras/article/480/1/800/5046474]. By restricting its scope to high-resolution "zoom-in" simulations of individual halos and their immediate environments, rather than attempting to model representative cosmological volumes, FIRE achieves the sub-parsec spatial resolution necessary to begin resolving the energy-conserving Sedov-Taylor phase of supernova remnants and the Strömgren spheres generated by photoionizing radiation [https://arxiv.org/abs/1311.2073]. This structural and computational choice theoretically removes the need to calibrate feedback efficiencies against cosmological galaxy populations [https://arxiv.org/abs/1311.2073]. The energy, momentum, mass, and metal fluxes are injected directly from standard stellar population synthesis models (such as STARBURST99) without subsequent cosmological adjustment or fine-tuning [https://arxiv.org/html/2501.16602v1]. While FIRE's underlying physics models are calibrated on isolated, small-scale test problems to ensure algorithmic stability, the resulting galaxy-scale properties—such as the emergent stellar-to-halo mass relation and the Kennicutt-Schmidt star formation relation—are framed as forward predictions of the model rather than fitted targets [https://academic.oup.com/mnras/article/445/1/581/988797].

A novel evolutionary step in the methodology of simulation calibration is represented by the ROMULUS, BAHAMAS, and FLAMINGO suites, which attempt to formalize and automate the parameter optimization process [https://academic.oup.com/mnras/article/470/1/1121/3828081]. Recognizing that traditional "hand-tuning" of subgrid parameters introduces subjective human biases and fails to map the full posterior probability space of the models, these projects implemented sophisticated optimization algorithms [https://academic.oup.com/mnras/article/526/4/6103/7291940]. The ROMULUS simulation utilized a Gaussian process Kriging technique to efficiently pinpoint regions of parameter space that yield galaxies resembling the z=0 mean population [https://academic.oup.com/mnras/article/470/1/1121/3828081]. The algorithm traverses the parameter space iteratively, identifying the optimal values for star formation efficiency, SMBH accretion boost factors, and feedback efficiencies [https://academic.oup.com/mnras/article/470/1/1121/3828081].

The BAHAMAS project introduced a critical shift in the targets of calibration, explicitly recognizing that unresolved baryonic feedback alters the total matter distribution on large scales, which directly impacts cosmological parameter constraints [https://arxiv.org/abs/1603.02702]. Consequently, BAHAMAS calibrated its AGN heating temperatures and stellar wind velocities not only to the GSMF, but explicitly to the hot gas mass fractions of galaxy groups and clusters [https://academic.oup.com/mnras/article/465/3/2936/2417021]. FLAMINGO expanded upon this cosmological focus by employing machine learning emulators trained on Latin hypercubes to predict the continuous response of the SMF and cluster gas fractions to variations in stellar and AGN feedback [https://academic.oup.com/mnras/article/526/4/6103/7291940]. This technique enables FLAMINGO to calibrate against the observational data while simultaneously generating model variations calibrated to 1σ systematic shifts in the observational data, effectively defining the models by their observational targets rather than arbitrary code parameters [https://academic.oup.com/mnras/article/526/4/6103/7291940].

Out-of-sample validation ledger

Evaluating the physical fidelity of a galaxy-formation simulation requires analyzing its predictions against observational data that were strictly excluded from the calibration phase. The following ledger documents published comparisons explicitly framed by the authors or independent analysts as out-of-sample predictions.

Simulation	Observable	Result	Overlap with Section-1 Calibration Target	Citation
SIMBA	H
I
	​

 and H
2
	​

 gas fractions	Agreement (simulation median vs observed selection-shaped stat: unmatched, magnitude ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	NONE	[https://arxiv.org/abs/1901.10203]
SIMBA	Sizes of low-mass quenched galaxies	Tension (simulation median vs observed selection-shaped stat: unmatched, yields "too-large sizes," magnitude ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	NONE (star-forming sizes are emergent, quenched sizes show tension)	[https://arxiv.org/abs/1901.10203]
FIRE-2	Stellar masses of Milky Way-mass galaxies at z=0	Agreement (simulation median vs observed selection-shaped stat: matched, systematic offset between FIRE-1 and FIRE-2 is a factor < 2, ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	NONE	[https://academic.oup.com/mnras/article/480/1/800/5046474]
FIRE-2	Galaxy-averaged Kennicutt-Schmidt star formation relation at all redshifts	Agreement (simulation median vs observed selection-shaped stat: matched, magnitude ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	NONE	[https://arxiv.org/abs/1311.2073]
ROMULUS	Star formation history and stellar mass of the Brightest Cluster Galaxy (BCG)	Agreement (simulation median vs observed selection-shaped stat: unmatched, magnitude ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	SMHM relation (overlaps conceptually, but field galaxy SMHM was the calibration target; cluster BCGs represent an out-of-sample mass/environment regime)	[https://arxiv.org/abs/1806.01282]
ASTRID	Ultraviolet luminosity function (UVLF) at z≥10	Tension (simulation median vs observed selection-shaped stat: unmatched, simulation underpredicts observed UVLF even with top-heavy IMF, magnitude ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	NONE	
ASTRID	Sub-mm number counts and quiescent galaxy number densities	Tension (simulation median vs observed selection-shaped stat: unmatched, simulation underpredicts quiescent population by between 0.3 dex and several dex, depending on observational source)	NONE	[https://arxiv.org/html/2504.15283v1]
EAGLE	Two-point correlation function of H
I
	​

 absorbers	Agreement (simulation median vs observed selection-shaped stat: matched, magnitude ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	NONE	[https://academic.oup.com/mnras/article/464/4/4204/2527881]
IllustrisTNG	Galaxy colour bimodality / Red sequence vs. Blue cloud morphology correlation	Agreement (simulation median vs observed selection-shaped stat: matched, magnitude ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	YES (Optical colors in stellar mass bins were explicitly used to refine TNG AGN feedback parameters)	[https://academic.oup.com/mnras/article/490/3/3196/5566345, https://www.tng-project.org/results/]

The process of executing rigorous out-of-sample validation for cosmological simulations is fundamentally complicated by the issue of commensurability [https://academic.oup.com/mnras/article/475/1/648/4683271]. Extracting a physical parameter—such as the total stellar mass or intrinsic star formation rate—directly from the three-dimensional particle and cell data of a hydrodynamical simulation yields a theoretical median that is generally not directly comparable to observational statistics. Observations are inherently shaped by complex selection effects, photometric flux limits, wavelength-dependent dust attenuation, and strictly defined instrumental aperture limits [https://arxiv.org/html/2405.04925v2]. A robust out-of-sample test requires the painstaking process of forward-modeling the simulation output into the observational domain. This involves generating mock spectral energy distributions (SEDs) for individual star particles, applying dust radiative transfer algorithms to simulate realistic attenuation, and projecting the three-dimensional data into two-dimensional surface brightness limits designed to exactly match specific survey parameters [https://arxiv.org/html/2605.13843v1]. Without this forward modeling, assessing a simulation median against an observed selection-shaped statistic remains highly uncertain.

The tensions identified in the validation ledger highlight the limitations of current subgrid formulations when pushed outside the specific boundaries of their calibration targets. For instance, while the SIMBA simulation successfully reproduces cold gas mass fractions (H
I
	​

 and H
2
	​

) and the mass-metallicity relationship across multiple redshifts, it displays tension regarding the structural properties of low-mass quenched galaxies [https://arxiv.org/abs/1901.10203]. SIMBA produces quenched dwarf galaxies with physical sizes that are too large compared to empirical datasets [https://arxiv.org/abs/1901.10203]. This tension suggests that the kinetic jet feedback model, while highly effective at regulating star formation in massive central galaxies, may incorrectly disrupt the spatial distribution of stars and gas in the shallower gravitational potentials of dwarf-scale systems.

Similarly, the ASTRID simulation displays marked tension with recent JWST observations at extreme redshifts (z≥10), significantly underpredicting the ultraviolet luminosity function (UVLF). The method papers note that the UVLF is underpredicted at z=7−8 by roughly 1σ, but the discrepancy worsens at higher redshifts [https://academic.oup.com/mnras/article/512/3/3703/6546174]. Because the z=0 GSMF is a calibrated quantity, the authors note that the discrepancy between the simulation and the observed GSMF at high redshift is likely influenced by inaccuracies in the low-redshift calibration constraints [https://academic.oup.com/mnras/article/512/3/3703/6546174]. This divergence indicates that subgrid models calibrated strictly to z=0 steady-state mass functions may fail to capture the highly bursty, high-efficiency star formation modes that theoretically prevail in the early Universe before dynamic and virial equilibrium is firmly established.

Conversely, the ROMULUS suite exhibits notable agreement when tested outside its primary calibration domain. ROMULUS was calibrated against field galaxy scaling relations, but later analysis of the RomulusC cluster zoom-in simulation showed that the star formation history and stellar mass of the Brightest Cluster Galaxy (BCG) remained consistent with observations [https://arxiv.org/abs/1806.01282]. The authors frame this as a significant validation, noting that "our sub-grid models, optimized only to reproduce observations of field dwarf and Milky Way mass galaxies, are able to produce reasonable galaxy masses and star formation histories in much higher mass systems" [https://arxiv.org/abs/1806.01282].

Double-counting warnings

A recurring vulnerability in the literature and discourse surrounding cosmological simulations is the risk of epistemological circularity—often termed "double-counting" or "circular calibration"—where variables intrinsically linked to the calibration targets are subsequently presented as independent triumphs of the model's predictive power. Several published critiques and methodological analyses within the field explicitly warn against this practice, emphasizing that the success of a given model must be evaluated solely on observables cleanly separated from its tuning parameters.

Pillepich et al. (2018), in outlining the foundational framework for the IllustrisTNG model, provide a stark warning regarding the interpretation of stellar mass validations [https://academic.oup.com/mnras/article/475/1/648/4683271]. They note that "In a semi-empirical model, the exact values of Mstars/Mhalo are a non-trivial convolution of the different observational data sets adopted for its calibration, each of which may invoke a different definition of galaxy stellar mass, possibly varying as a function of mass" [https://academic.oup.com/mnras/article/475/1/648/4683271]. They conclude that "Unless a single observational data set has been used to calibrate a given model and the galaxy stellar mass definition from that data set is made explicit, it is impossible to make a well-posed comparison with simulated stellar mass" [https://academic.oup.com/mnras/article/475/1/648/4683271]. This highlights that assessing a model's success against a generic SMHM relation is fraught with circularity if the specific aperture definitions, integration methods, and surface brightness limits of the calibration data are not strictly mirrored in the validation data.

Furthermore, the methodological pipeline of the FLAMINGO project implicitly critiques previous generations of simulations regarding how calibration variables are chosen. Kugel et al. (2023) state that "For BAHAMAS, and also for simulations like EAGLE and IllustrisTNG, calibration was done by hand by varying the subgrid parameters within some reasonable range until the simulation lined up with the calibration targets. This approach works reasonably well in the context of galaxy formation, but it introduces biases into the parameter selection" [https://academic.oup.com/mnras/article/526/4/6103/7291940]. By relying on human intuition to traverse the multi-dimensional parameter space, earlier models risked overfitting to secondary observables implicitly prioritized by the researchers, thereby masking underlying physical tensions and artificially inflating the perceived robustness of the model.

Broader critiques of the ΛCDM simulation enterprise similarly emphasize the boundaries of predictive power. As highlighted in a critical analysis of the FLAMINGO data releases, the simulation documentation "explicitly warns that quantities used directly in calibration, and closely related quantities, should not be treated as predictions of the model. This does not make FLAMINGO useless. It makes FLAMINGO what it is: a sophisticated ΛCDM-based modeling apparatus, not an assumption-free measurement of cosmic reality". When a model utilizes the z=0 stellar mass function to dictate the efficiency of supernova winds, subsequent agreement with the low-redshift star formation rate density or satellite galaxy fraction is heavily pre-conditioned by the initial tuning, severely diminishing the statistical independence of the "prediction."

McCarthy et al. (2017) explicitly identified this issue prior to the development of the BAHAMAS suite, warning that "recent numerical studies have demonstrated that the mapping between observable and total mass, as well as the total mass itself, are sensitive to unresolved feedback processes associated with galaxy formation, motivating explicit calibration of the feedback efficiencies" [https://arxiv.org/abs/1603.02702]. Because the total matter power spectrum at intermediate cosmological scales (k∼1−10 h Mpc
−1
) is highly sensitive to the ejection of baryons from halos via AGN feedback, attempting to constrain cosmological parameters (such as the matter density Ω
m
	​

 or the fluctuation amplitude σ
8
	​

) using a simulation that has not been explicitly calibrated to reproduce large-scale hot gas fractions risks mapping subgrid tuning errors directly into fundamental cosmological parameter biases [https://arxiv.org/abs/1712.02411].

Feedback-relevant observables map

The physics of galaxy quenching, Active Galactic Nucleus (AGN) feedback, and the continuous baryon cycle remain the most fiercely debated topics in modern extragalactic astrophysics. The table below maps the status of critical observables central to these debates across the major simulation suites, noting whether the property serves as an explicit calibration target (CALIBRATED), an independent prediction (EMERGENT), or currently lacks explicit published validation (NOT_REPORTED).

Simulation	Quenched fractions	Gas fractions of passive galaxies	Outflow demographics	Hot-halo/cavity properties	Radio-AGN incidence
IllustrisTNG	CALIBRATED (via galaxy optical colors in mass bins)	NOT_REPORTED	EMERGENT (revised galactic winds effects explored) [https://arxiv.org/abs/1703.02970]	CALIBRATED (hot gas fraction in clusters explicitly tuned)	EMERGENT (magnetic fields and radio haloes analyzed) [https://arxiv.org/html/2603.13010v1]
EAGLE	EMERGENT (reproduces present-day colours) [https://academic.oup.com/mnras/article/464/4/4204/2527881]	EMERGENT (H I fractions extensively analyzed) [https://academic.oup.com/mnras/article/464/4/4204/2527881]	EMERGENT (winds develop without predetermined loading factors) [https://arxiv.org/abs/1407.7040]	EMERGENT (though later noted to diverge from X-ray reality, prompting the BAHAMAS project) [https://academic.oup.com/mnras/article/465/3/2936/2417021]	NOT_REPORTED
SIMBA	CALIBRATED (X-ray heating tuned explicitly to obtain z=0 fully quenched galaxies) [https://academic.oup.com/mnras/article/536/1/145/7903412]	EMERGENT [https://arxiv.org/abs/1901.10203]	NOT_REPORTED	EMERGENT (hot gas fractions in massive halos) [https://arxiv.org/abs/1901.10203]	NOT_REPORTED
FIRE/FIRE-2	EMERGENT [https://academic.oup.com/mnras/article/480/1/800/5046474]	NOT_REPORTED	EMERGENT (mass loading factors and velocities emerge from small-scale physics)	EMERGENT	NOT_REPORTED
ROMULUS	CALIBRATED (Progenitor color evolution specifically tuned for SMBH regulation) [https://academic.oup.com/mnras/article/470/1/1121/3828081]	NOT_REPORTED	EMERGENT (large-scale, collimated outflows coexist with low entropy cores) [https://arxiv.org/abs/1806.01282]	EMERGENT (ICM thermodynamically consistent with observations) [https://arxiv.org/abs/1806.01282]	NOT_REPORTED
ASTRID	NOT_REPORTED	NOT_REPORTED	NOT_REPORTED	NOT_REPORTED	NOT_REPORTED
FLAMINGO	NOT_REPORTED	NOT_REPORTED	NOT_REPORTED	CALIBRATED (Cluster gas fractions f
gas,500c
	​

 directly targeted) [https://academic.oup.com/mnras/article/526/4/6103/7291940]	NOT_REPORTED
BAHAMAS	NOT_REPORTED	NOT_REPORTED	NOT_REPORTED	CALIBRATED (hot gas mass fractions of groups and clusters targeted) [https://arxiv.org/abs/1603.02702]	NOT_REPORTED

The distribution of CALIBRATED versus EMERGENT categorizations across this map underscores the persistent difficulty of simulating macroscopic galaxy quenching from first principles. Because the quenching of star formation relies on a delicate balance between cosmological gas accretion rates, the specific cooling timescale of the circumgalactic medium, and the intermittent bursty energy injections from central black holes, minor errors in subgrid efficiencies rapidly compound into either catastrophic cooling flows or the excessive evacuation of the gas reservoir [https://academic.oup.com/mnras/article/534/1/361/7756428]. The SIMBA simulation explicitly required the addition of an X-ray heating mode, with its heating parameters tuned specifically to suppress star formation in high-mass halos, indicating that kinetic jets alone were insufficient to maintain the red sequence down to z=0 [https://academic.oup.com/mnras/article/536/1/145/7903412]. Similarly, the IllustrisTNG project refined its AGN feedback parameters by explicitly leveraging the distribution of galaxy optical colors in stellar mass bins, effectively moving the quenched fraction from an emergent prediction to a semi-calibrated constraint.

Conversely, the detailed thermodynamics of the hot halo—specifically the gas fractions within R
500
	​

 of massive galaxy clusters—have transitioned into a primary calibration target for simulations heavily focused on large-scale structure and precision cosmology, such as FLAMINGO and BAHAMAS [https://academic.oup.com/mnras/article/526/4/6103/7291940, https://arxiv.org/abs/1603.02702]. Since the violent ejection of gas from halos by AGN feedback significantly alters the total matter power spectrum at intermediate scales, models that leave hot halo fractions as entirely emergent predictions (such as the original EAGLE simulation) risk introducing systematic theoretical biases when their density fields are utilized for weak lensing or Sunyaev-Zel'dovich effect cosmological parameter estimation [https://academic.oup.com/mnras/article/465/3/2936/2417021]. By explicitly calibrating to cluster gas fractions, BAHAMAS and FLAMINGO force their AGN heating models to correctly partition baryons between the intra-cluster medium and the unbound intergalactic medium.

Gaps

A systematic review of the calibration and validation literature reveals several critical gaps, either in the form of missing methodological transparency or a lack of rigorous out-of-sample testing for specific observable domains critical to galaxy evolution theory.

GAP: Ambiguity persists in the ASTRID methodology papers regarding the exact subset of stellar and AGN feedback parameters that were iteratively tuned to achieve the stated z=0 Galaxy Stellar Mass Function calibration target. The official documentation notes that parameters were "adjusted" from their fiducial models to maintain agreement with observations, but fails to provide the comprehensive multi-dimensional mapping or explicit prior ranges seen in the machine-learning approaches of FLAMINGO or the Kriging optimizations of ROMULUS [https://academic.oup.com/mnras/article/512/3/3703/6546174, https://academic.oup.com/mnras/article/548/1/stag375/8650959].

GAP: No explicit out-of-sample tests published assessing radio-AGN incidence and relativistic jet demographics as a direct comparison against observational radio catalogs (e.g., LOFAR or VLA continuum surveys) in SIMBA, ROMULUS, ASTRID, FLAMINGO, or BAHAMAS. Given that many of these models utilize "jet" or "kinetic" feedback modes at low Eddington accretion rates, the lack of forward-modeled radio emission validation represents a significant disconnect between the subgrid physics and observational astronomy.

GAP: Lack of rigorous out-of-sample validation for the cold gas fractions specifically isolated to passive/quenched galaxies in IllustrisTNG, FIRE, ROMULUS, ASTRID, FLAMINGO, and BAHAMAS. While total gas fractions are frequently analyzed, the residual ISM mass within galaxies that lie on the red sequence remains poorly constrained, making it difficult to determine if simulated quenching is driven by complete gas exhaustion (starvation) or merely the suppression of cooling (maintenance mode).

GAP: Systematic under-reporting of observational selection function matching—specifically the forward-modeling of surface brightness dimming and complex dust geometries—when validating simulated outflow demographics (mass loading factors and velocities) against empirical scaling relations derived from specific absorption lines.

Links ledger

arXiv:1703.02970 | https://arxiv.org/abs/1703.02970 | QUARANTINED_PENDING_LOCAL_CHECK
IllustrisTNG Background | https://www.tng-project.org/data/docs/background/ | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 475:648 | https://academic.oup.com/mnras/article/475/1/648/4683271 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 450:1937 | https://academic.oup.com/mnras/article/450/2/1937/984366 | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:1407.7040 | https://arxiv.org/abs/1407.7040 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 446:521 | https://academic.oup.com/mnras/article/446/1/521/1316115 | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:1901.10203 | https://arxiv.org/abs/1901.10203 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 536:145 | https://academic.oup.com/mnras/article/536/1/145/7903412 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 480:800 | https://academic.oup.com/mnras/article/480/1/800/5046474 | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:1311.2073 | https://arxiv.org/abs/1311.2073 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 445:581 | https://academic.oup.com/mnras/article/445/1/581/988797 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 470:1121 | https://academic.oup.com/mnras/article/470/1/1121/3828081 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 512:3703 | https://academic.oup.com/mnras/article/512/3/3703/6546174 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 548:stag375 | https://academic.oup.com/mnras/article/548/1/stag375/8650959 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 526:6103 | https://academic.oup.com/mnras/article/526/4/6103/7291940 | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:2306.04024 | https://arxiv.org/abs/2306.04024 | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:1806.01282 | https://arxiv.org/abs/1806.01282 | QUARANTINED_PENDING_LOCAL_CHECK
ASTRID RG | https://www.researchgate.net/publication/359155282_The_ASTRID_Simulation_Galaxy_Formation_and_Reionization | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:2504.15283 | https://arxiv.org/html/2504.15283v1 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 464:4204 | https://academic.oup.com/mnras/article/464/4/4204/2527881 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 490:3196 | https://academic.oup.com/mnras/article/490/3/3196/5566345 | QUARANTINED_PENDING_LOCAL_CHECK
IllustrisTNG Results | https://www.tng-project.org/results/ | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:2405.04925 | https://arxiv.org/html/2405.04925v2 | QUARANTINED_PENDING_LOCAL_CHECK
Siegel Critique | https://medium.com/@m.alfaro.007/siegel-audit-a-critical-essay-on-ethan-siegels-defense-of-%CE%BBcdm-84d9ef601dda | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:1603.02702 | https://arxiv.org/abs/1603.02702 | QUARANTINED_PENDING_LOCAL_CHECK
IllustrisTNG RG | https://www.researchgate.net/publication/314433630_Simulating_Galaxy_Formation_with_the_IllustrisTNG_Model | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:2603.13010 | https://arxiv.org/html/2603.13010v1 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 465:2936 | https://academic.oup.com/mnras/article/465/3/2936/2417021 | QUARANTINED_PENDING_LOCAL_CHECK
PMC10602225 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10602225/ | QUARANTINED_PENDING_LOCAL_CHECK
FIRE Movies | http://www.tapir.caltech.edu/~phopkins/Site/Movies_cosmo.html | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 534:361 | https://academic.oup.com/mnras/article/534/1/361/7756428 | QUARANTINED_PENDING_LOCAL_CHECK
arXiv:1712.02411 | https://arxiv.org/abs/1712.02411 | QUARANTINED_PENDING_LOCAL_CHECK
MNRAS 534:957 | https://academic.oup.com/mnras/article/534/1/957/7756870 | QUARANTINED_PENDING_LOCAL_CHECK

GEMINI_WEB_JOINT_C1_OUTPUT_DONE_20260711T100139Z

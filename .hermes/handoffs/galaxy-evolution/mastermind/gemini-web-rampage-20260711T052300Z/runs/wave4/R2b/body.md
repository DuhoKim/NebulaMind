Rampage R2 answer — REQ_RAMPAGE_R2_20260711T052300Z

Run date (UTC): 2026-07-11T05:23:00Z
Model: Advanced Analyst-01
Quantities addressed: 8 of 8

The study of galaxy evolution is fundamentally anchored in understanding the complex baryon cycle—the continuous process through which galaxies accrete gas from the cosmic web, process this material into stars, and subsequently eject it via powerful feedback mechanisms. Within this theoretical framework, the regulatory roles of stellar feedback (e.g., supernovae, stellar winds, radiation pressure) and Active Galactic Nuclei (AGN) are invoked to explain several enduring astrophysical phenomena. These include the suppression of star formation in massive halos, the prevention of catastrophic cooling flows in galaxy clusters, and the modulation of the mass-metallicity relation across cosmic time. To construct predictive cosmological simulations and semi-analytic models, these physical processes must be parameterized using robust observational constraints.

The following exhaustive research report synthesizes the published parameter space—or the "prior-work envelope"—across eight highly specific quantities related to multiphase outflows, gas depletion scales, cavity energetics, radio-mode duty cycles, metallicity scaling relations, and the abundance of massive systems in the primordial universe. By delineating the boundaries of currently reported literature values, along with the precise methodologies and assumptions from which they are derived, this report provides a rigorous benchmark for contextualizing emergent data.

Q1 — Incidence of ionized AGN-driven outflows

The warm ionized phase of galactic outflows, typically characterized by gas temperatures on the order of T≈10
4
 K, is frequently traced through optical and near-infrared emission lines, most notably H$\alpha$, H$\beta$, [OIII]λ5007, and [NII]λ6584. Detecting outflows in this specific phase relies upon isolating non-circular kinematic signatures from the dominant, systemic rotational velocity field of the host galaxy's disc. Observationally, this manifests as broad, shifted, or asymmetric velocity components in the emission line profiles. The reported incidence of such outflows is heavily dependent on several factors: the instrumental spectral resolution, the signal-to-noise ratio of the observations, the spatial coverage (e.g., single-fiber, long-slit, or integral field unit [IFU] spectroscopy), and the explicit classification criteria utilized to separate AGN photoionization from stellar processes or shock heating.

Wide-field IFU surveys in the local universe, such as the Mapping Nearby Galaxies at Apache Point Observatory (MaNGA) survey and the Sydney-AAO Multi-object Integral field spectrograph (SAMI) survey, have provided extensive statistical baselines, allowing researchers to disentangle spatial structures and spatially resolved kinematics. At higher redshifts (z≈1−3), often referred to as "cosmic noon"—the epoch corresponding to the peak of the cosmic star formation rate density and black hole accretion history—instruments like the K-band Multi Object Spectrograph (KMOS) have been employed to trace these warm winds. The tabulated values reflect how the reported prevalence scales significantly with the definition of the denominator; for instance, defining the baseline as all emission-line galaxies yields fundamentally different incidence rates compared to exclusively selecting massive or AGN-identified subsets.

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
∼12% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of ionized outflows	Broad-velocity components in optical lines	Line-emitting galaxies	Total line-emitting sample	z<0.1	MaNGA	Avery et al. 2021 (MNRAS 503, 5134) [arXiv:2201.08079]
28% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of ionized outflows	Two-component (broad+narrow) optical emission fitting	Emission-line galaxies (logM
∗
	​

≥9)	Total emission-line sample	z<0.1	SAMI	Oh et al. 2024 (arXiv:2405.20627)
∼70–80% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of ionized outflows	Broad H$\alpha$/[OIII] kinematic signatures	AGN-identified massive galaxies	Total AGN subset	z≈0.6–2.7	KMOS3D / VLT	Förster Schreiber et al. 2019 (ApJ 875, 21)
Q1.a Definition conflicts

The strict definition of an "ionized outflow" introduces significant variance in the published literature. Avery et al. (2021) and Oh et al. (2024) select outflows based on the rigorous statistical requirement of a secondary broad kinematic component in the emission line fitting. To prevent false positives caused by beam smearing—where the natural rotation of the galaxy disc is blurred into a seemingly broad line by the point spread function of the instrument—these studies often require velocity dispersions (σ) or velocity offsets (Δv) to exceed specific, conservative thresholds. The denominator in these local studies is typically the entire parent sample of line-emitting galaxies, yielding lower overall incidence rates (12% to 28%).

In stark contrast, Förster Schreiber et al. (2019) isolate a subset of massive galaxies (logM
∗
	​

>10.7) specifically hosting independently identified AGNs at cosmic noon. By narrowing the denominator to this highly active population, they report a much higher incidence (70–80%). Furthermore, the choice of emission line tracer influences the outcome; while H$\alpha$ is a primary tracer for general ionized gas, the [OIII]λ5007 line is frequently utilized due to its high sensitivity to the harder radiation fields typical of AGN-driven shocks and photoionization, potentially biasing incidence rates upward in AGN-selected populations relative to star-formation-selected samples.

Q1.b Envelope summary

Because the selections and denominators vary fundamentally—comparing the general local emission-line galaxy population against high-mass AGN-selected systems at high redshift—these values are non-commensurable. A strictly commensurable envelope for the general local emission-line galaxy population (denominator: all line-emitting galaxies, z<0.1) spans from 12% to 28%. The high-z AGN-specific incidence operates within its own parameter space, occupying an envelope of 70–80%.

Q2 — Incidence of neutral AGN-driven outflows

Cool neutral gas, generally residing at temperatures of T≈100 K to 1000 K, often dominates the total mass and momentum budget of galactic winds, yet it remains observationally challenging to trace. Detection frequently relies on observing resonant absorption features seen against a bright background continuum. The Na I D doublet (λλ5890,5896) is the most common optical tracer for this phase in the local universe. Ultraviolet absorption lines, such as Mg II, C II, and Si II, are also heavily utilized, particularly at higher redshifts where cosmological expansion shifts these rest-frame UV features into the optical and near-infrared observing windows.

The fundamental requirement of a strong background continuum creates an inherent selection bias toward bright, dusty, or actively star-forming host galaxies, which potentially obscures the true prevalence of neutral winds in quiescent or low-mass systems. Interpreting these absorption profiles requires careful decoupling of systemic interstellar medium (ISM) absorption from blue-shifted outflow signatures. Because down-the-barrel observations only detect gas moving toward the observer along the line of sight, covering fraction degeneracies often complicate the interpretation. Outflow velocities must measurably exceed the systemic velocity dispersion to be confidently identified as escaping or circulating wind material rather than standard disc turbulence. The reported incidence is therefore an intricate function of spectral resolution, signal-to-noise ratio, and the underlying mass or star-formation rate of the target sample.

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
∼1% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of neutral outflows	Blueshifted Na I D absorption	Typical star-forming/AGN hosts	Total sample	z≈0	SDSS/MaNGA	Nedelchev, Sarzi & Kaviraj 2019 / Avery et al. 2022
∼20% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of neutral outflows	Blueshifted Na I D absorption	Local post-starburst galaxies	Total post-starburst sample	z≈0	Multiple (compilation)	Sun et al. 2023 (cited in arXiv:2310.17939)
12% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of neutral outflows	Blueshifted Na I D absorption >100 km/s	Mass-complete Blue Jay sample (logM
∗
	​

=8.5–11.5)	Total sample	z≈1.7–3.5	JWST NIRSpec	Davies et al. 2024 (MNRAS 528, 4976)
46% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of neutral outflows	Na I D absorption detected (outflow/systemic combined)	Massive subset (logM
∗
	​

>10)	Total massive subset	z≈1.7–3.5	JWST NIRSpec	Davies et al. 2024 (MNRAS 528, 4976)
∼100% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of neutral outflows	Rest-frame UV absorption lines	UV-bright galaxies	Total UV-bright sample	z≈2	Keck	Steidel et al. 2010 (cited in arXiv:2310.17939)
Q2.a Definition conflicts

The primary conflict in these measurements arises from the severe selection effects imposed by the required background stellar continuum. The Steidel et al. (2010) value of ~100% applies exclusively to UV-bright galaxies using strong rest-frame UV transitions. These transitions possess high oscillator strengths and often saturate, tracing highly extended, diffuse halo gas that may be moving at relatively low velocities. In contrast, the Na I D transition requires a sufficiently dust-shielded environment to prevent the low-ionization-potential sodium atoms (ionization potential of 5.1 eV) from being ionized by the ambient radiation field. Consequently, Na I D studies systematically exclude galaxies lacking substantial dust or stellar continuum, heavily skewing the incidence toward massive, dusty galaxies.

Additionally, nomenclature and detection thresholds vary. Davies et al. report a 46% detection rate of the Na I D feature in massive galaxies, but explicitly specify that only 50% of these classifiable features are unambiguously blue-shifted (outflowing), making the rigorous outflow incidence much lower than the raw absorption detection rate. The local incidence (∼1%) from Nedelchev et al. (2019) serves as a stark contrast to the heightened activity at cosmic noon, pointing toward both a genuine evolution in outflow prevalence and the difficulty of detecting weak outflows against local stellar continua.

Q2.b Envelope summary

Due to extreme differences in sample selection (UV-bright vs. mass-complete vs. post-starburst) and tracers (UV vs. Na I D), a single unified envelope is non-commensurable. For mass-selected samples traced specifically by Na I D, the incidence of neutral outflows ranges from ∼1% at z≈0 to 12% at z≈2. For uniquely selected sub-populations, the values occupy vastly different envelopes, ranging from ∼20% (local post-starbursts) to ∼100% (high-z UV-bright systems).

Q3 — Mass-loading factors by gas phase

The mass-loading factor (η=
M
˙
out
	​

/SFR) is a critical parameter in galaxy evolution models, representing the efficiency with which feedback ejects material relative to the rate at which gas is concurrently converted into stars. Formulating η requires a series of complex assumptions for both the numerator (the absolute mass outflow rate, 
M
˙
out
	​

) and the denominator (the Star Formation Rate, SFR).

The numerator is notoriously difficult to constrain with high precision. It requires assuming an outflow geometry (e.g., spherical, bi-conical, or a thin expanding shell), a filling factor (the actual volume occupied by the gas clumps within the outflow cone), and determining the total gas mass from an observed luminosity via uncertain conversion factors. For molecular gas, this involves the α
CO
	​

 factor; for ionized gas, it involves estimating the local electron density (n
e
	​

), often derived from the λλ6716,6731 doublet ratio, though this may severely underestimate the density of the actual outflowing clumps. The outflow velocity (v
out
	​

) utilized in the calculation is often taken as the maximum velocity (v
max
	​

), the central velocity of a broad component, or a non-parametric measure like v
50
	​

 or W
80
	​

. The denominator, SFR, carries its own systematic uncertainties related to the assumed Initial Mass Function (IMF), the timescale of the specific SFR tracer utilized (e.g., H$\alpha$ traces recent ∼10 Myr activity, while UV/IR traces ∼100 Myr), and the requisite dust attenuation corrections.

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
∼0.7 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Mass-loading (η)	OH 119$\mu$m (molecular)	Lensed dusty star-forming galaxy (SPT2319-55)	SFR (IR-derived)	z≈0 (analog)	ALMA	Spilker et al. 2018 (ALMA Memo)
>10 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Mass-loading (η)	CO(1-0) (molecular)	Luminous AGN (L
AGN
	​

/L
bol
	​

>0.7)	SFR	z≈0	IRAM/PdBI	Fluetsch et al. 2019 (MNRAS 483, 4586)
4–360 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Mass-loading (η)	Na I D (neutral atomic)	Quenching systems (log(sSFR)≲−10)	SFR (SED fitting)	z≈1.7–3.5	JWST NIRSpec	Davies et al. 2024 (MNRAS 528, 4976)
0.03–0.08 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Mass-loading (η)	H$\alpha$/[OIII] (ionized)	Star-forming / low-mass AGN	SFR	z≈2	KLEVER/KMOS	Concas et al. 2022 (MNRAS 513, 2535)
Q3.a Definition conflicts

The derivation of 
M
˙
out
	​

 varies drastically depending on the target phase and the author's methodological preferences. For ionized gas (e.g., Concas et al. 2022), the inferred mass relies inversely on the assumed local electron density (M∝1/n
e
	​

). Utilizing standard ISM densities (∼100 cm$^{-3})yieldsmuchhighertotalmassesthanutilizingdensitiesderivedfromaurorallinesinoutflowingclumps(\sim 1000$ cm$^{-3}$). For molecular gas (Fluetsch et al. 2019), the L
CO
	​

-to-mass conversion factor is highly debated in outflowing environments, where the gas may be optically thin and subject to vastly different excitation conditions and turbulence compared to stable disc gas.

Furthermore, the basic geometric assumptions diverge: a thin expanding shell model yields 
M
˙
∝v/R, while a uniformly filled cone yields 
M
˙
∝3v/R, introducing a factor of 3 discrepancy based purely on geometric preference. In quenching systems (Davies et al. 2024), the exceptionally high η values (up to 360) are mathematically driven by the plummeting denominator (SFR) as the galaxy ceases forming stars. This creates extreme ratios even if the absolute mass outflow rate is modest, complicating interpretations of whether the feedback is inherently powerful or simply operating in a fuel-depleted environment. Comparisons across phases thus convolve physical differences with disparate systematic assumptions.

Q3.b Envelope summary

Because these values span entirely distinct physical gas phases (ionized, neutral, molecular) and highly divergent denominator states (rapidly quenching versus main-sequence star-forming), they are non-commensurable for a single unified minimum-maximum envelope. The literature suggests evaluating them independently:

Ionized phase envelope: 0.03 to 0.08

Molecular phase envelope (SF to strong AGN): 0.7 to > 10

Neutral phase envelope (quenching hosts): 4 to 360

Q4 — Molecular gas fractions and depletion times

The molecular gas fraction (μ
gas
	​

=M
gas
	​

/M
∗
	​

 or f
gas
	​

=M
gas
	​

/(M
gas
	​

+M
∗
	​

)) and the depletion time (t
dep
	​

=M
gas
	​

/SFR) are fundamental diagnostics of a galaxy's capacity to sustain its star formation activity over cosmological timescales. Observing how these quantities evolve across the transition from star-forming main sequence (SFMS) galaxies to quiescent or post-starburst systems provides invaluable insight into the dominant quenching mechanisms. It allows researchers to investigate whether galaxies exhaust their fuel via star formation (depletion), expel it violently via feedback (ejection), or are simply starved of fresh cosmological accretion (strangulation).

Directly observing molecular gas via H$_2$ is largely unfeasible in typical cold interstellar environments due to the molecule's lack of a permanent electric dipole moment, which prevents it from emitting easily observable rotational transitions at low temperatures. Thus, astronomers rely on proxies, most commonly the low-J rotational transitions of Carbon Monoxide (e.g., CO(1-0), CO(2-1)) or the Rayleigh-Jeans tail of the cold dust continuum emission. The proportionality constant linking the proxy luminosity to the total underlying molecular gas mass involves significant, often debated, systematic uncertainties relating to metallicity, gas density, and the intensity of the local interstellar radiation field.

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
0.11–2.8 (median 0.65) ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Molecular gas mass ratio (μ
gas
	​

)	Dust continuum (Band 7)	Massive SFMS galaxies (M
∗
	​

>10
10.8
M
⊙
	​

)	Stellar Mass (M
∗
	​

)	z≈1.45–1.70	ALMA / FMOS-COSMOS	

arXiv:2605.23662 


<10
9.8
M
⊙
	​

 (mass limit) ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Molecular gas mass limit	Dust continuum / CO limits	Massive quiescent galaxy GS10578	N/A (Absolute Mass)	z≈1.5	ALMA	Williams et al. 2021 (cited in arXiv:2405.19401)
<16 to <220 Myr ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Depletion time (t
dep
	​

)	Dust/CO derived limits	Massive quiescent galaxy GS10578	SFR	z≈1.5	ALMA	Williams et al. 2021 (cited in arXiv:2405.19401)
0.3%–1.0% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Molecular gas fraction (f
gas
	​

)	CO / Dust compilation	Local quiescent galaxies	Total Mass (M
∗
	​

+M
gas
	​

)	z≈0	Multiple (e.g., xCOLD GASS)	Spilker et al. 2018 (ApJ 860, 103) / Young et al. 2011
  
Q4.a Definition conflicts

The translation of CO luminosity to H$2$ mass hinges entirely on the conversion factor $\alpha{\rm CO}.Intypical,solar−metallicitystar−formingdiscs,astandardMilkyWayvalue(\alpha_{\rm CO} \approx 4.3$ M
⊙
	​

/(K km s
−1
 pc
2
)) is often assumed. However, in extreme starburst environments, mergers, or regions with significantly different metallicities, lower values (α
CO
	​

≈0.8) are frequently applied because the gas is more turbulent and potentially optically thin. When observing quenching or completely quiescent galaxies, the assumption of α
CO
	​

 becomes highly precarious; if these systems harbor highly turbulent or differentially excited gas remaining after a violent feedback event, the conversion factor is highly unconstrained.

Furthermore, utilizing dust continuum as a mass proxy assumes a fixed or smoothly metallicity-dependent gas-to-dust ratio and relies heavily on the assumed dust temperature (T
dust
	​

). Variations in T
dust
	​

 estimates (e.g., assuming 25 K versus 40 K) can alter the inferred gas mass by factors of 2 to 3. Additionally, basic definitions of the denominator differ across the literature: μ
gas
	​

 normalizes by stellar mass alone, whereas f
gas
	​

 often normalizes by the combined baryonic mass (M
∗
	​

+M
gas
	​

), complicating direct, one-to-one comparisons across different surveys.

Q4.b Envelope summary

Due to different denominators (μ
gas
	​

 vs. f
gas
	​

) and vastly different evolutionary states (main-sequence star-forming vs. deeply quiescent), the values are non-commensurable for a single envelope.

Massive star-forming galaxies (z≈1.5) μ
gas
	​

 range: 0.11 to 2.8

Local quiescent galaxies f
gas
	​

 range: 0.003 to 0.01 (0.3% to 1.0%)

Quiescent depletion times (z≈1.5 limits): <16 to <220 Myr

Q5 — X-ray cavity power vs cooling luminosity balance

In the deep potential wells at the centers of massive galaxy groups and clusters, the hot, diffuse intracluster medium (ICM) continuously radiates energy via X-ray bremsstrahlung. Without a compensatory heat source to replace this lost energy, the central gas should undergo runaway cooling, losing pressure support and flowing inward to form a massive "cooling flow." However, observations show that the gas does not cool to low temperatures in the quantities predicted. The prevailing physical solution to this long-standing cooling flow problem is "maintenance-mode" or "radio-mode" feedback from the central Brightest Cluster Galaxy's (BCG) supermassive black hole. The AGN inflates relativistic jets into the surrounding ICM, blowing vast bubbles that displace the X-ray emitting gas, appearing to observers as distinct surface brightness depressions, or X-ray cavities.

The thermodynamic balance between this heating and the ongoing cooling is assessed by comparing the mechanical cavity power (P
cav
	​

) to the X-ray cooling luminosity (L
cool
	​

). Cavity power is typically calculated by estimating the total enthalpy (H=E+pV, which equals 4pV for a relativistic gas) and dividing this energy by the buoyant rise time of the bubble (t
buoy
	​

). Evaluating whether P
cav
	​

 is sufficient to balance L
cool
	​

 across various statistical samples is central to testing and refining the AGN feedback paradigm.

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
∼1 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Ratio of cavity power to cooling luminosity	X-ray cavities (enthalpy / rise time)	RBS 797 (galaxy cluster)	X-ray cooling luminosity	z≈0.35	Chandra	Ubertosi 2021 (PhD Thesis, Univ. Bologna) / Bîrzan et al. 2004
>70% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Fraction of cool-core clusters with cavities	X-ray surface brightness depressions	Archival cool-core clusters	Total cool-core cluster sample	z≈0	Chandra	Dunn & Fabian 2006 (MNRAS 373, 959)
∼25–30% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Fraction of clusters with cavities	X-ray surface brightness depressions	General cluster samples (MACS / archival)	Total cluster sample	z≈0–0.6	Chandra	Hlavacek-Larrondo et al. 2012 / Rafferty et al. 2006
7% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Detection fraction of cavities	X-ray surface brightness depressions	SPT-SZ cluster survey	Total SPT-SZ cluster sample	z≈0.3–1.2	Chandra / SPT	Hlavacek-Larrondo et al. 2015 (arXiv:1410.7391)
Q5.a Definition conflicts

The fraction of systems observed with cavities relies heavily on the definition of the denominator—the specific cluster population being surveyed. Dunn & Fabian (2006) focus specifically on pre-selected "cool-core" clusters (those with short central cooling times requiring heating), finding a >70% incidence of visible cavities. Conversely, when broad, blindly selected cluster catalogs (e.g., the Sunyaev-Zel'dovich-selected SPT sample, which includes many non-cool-core, dynamically disturbed, or merging systems) are utilized, the overall incidence drops severely to 7% (Hlavacek-Larrondo et al. 2015), though observational depth limitations heavily bias high-z detections against finding faint, small cavities.

The calculation of P
cav
	​

 itself relies on geometric approximations of the cavity volume (often assuming perfect spherical or ellipsoidal symmetry in projection) and theoretical assumptions regarding the equation of state of the fluid inflating the bubble. A ratio of specific heats γ=4/3 for relativistic plasma yields 4pV enthalpy, while a non-relativistic gas would yield a different multiple. L
cool
	​

 also varies depending on the chosen integration boundary, often defined arbitrarily as the radius where the cooling time equals 7.7 Gyr or 3 Gyr. Furthermore, some detailed studies incorporate shock heating into the total mechanical power budget, which can dramatically alter the P
cav
	​

/L
cool
	​

 ratio, occasionally raising it well above unity in extreme, deeply studied cases like RBS 797.

Q5.b Envelope summary

For the cavity fraction in specifically designated cool-core clusters, values are non-commensurable with broad, total-cluster surveys.

General cluster cavity detection fraction: 7% to 30% (dependent heavily on depth, mass limits, and selection).

The ratio of P
cav
	​

/L
cool
	​

 broadly centers around ∼1, pointing toward the conclusion that mechanical cavity power is generally sufficient to offset radiative cooling losses in cluster cores.

Q6 — Radio-AGN / maintenance-mode duty cycles

Understanding precisely how often the "radio-mode" (or maintenance-mode) feedback mechanism is active is vital for theoretical models aiming to keep massive elliptical galaxies quiescent over cosmological timescales. The duty cycle is empirically estimated by measuring the fraction of galaxies that host a detectable radio-loud AGN as a function of stellar or dark matter halo mass. A high incidence suggests that the feedback is nearly continuous or operates on a very fast flicker, whereas a lower incidence suggests recurrent, episodic outbursts separated by long periods of quiescence. Deep radio interferometric surveys are uniquely suited to answering this, as low-frequency radio emission can trace older, cooling populations of relativistic electrons in extended lobes, capturing both current and recently ceased jet activity.

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
≈30% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Radio-AGN fraction	1.4 GHz luminosity (L>10
23
 W/Hz)	Highest stellar mass galaxies	Total massive galaxy sample	z≈0	NVSS / SDSS	Best et al. 2005 (MNRAS 362, 25)
100% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Radio-AGN fraction	150 MHz luminosity	Massive galaxies (M
∗
	​

>10
11
M
⊙
	​

)	Total massive galaxy sample	z<0.3	LOFAR (LoTSS)	Sabater et al. 2019 (A&A 622, A17)
Factor of ∼2–4 lower ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Inferred duty cycle relative to simple mass counts	Halo Occupation Distribution (HOD) modeling	Radio-AGN hosts	Dark matter halo mass bins	z≈1	LOFAR Deep Fields	Kondapally et al. 2025/2022 (MNRAS 547, 4)
Q6.a Definition conflicts

The definition of the duty cycle is fundamentally an observational proxy tied directly to the luminosity threshold and operating frequency of the telescope used for the survey. Earlier seminal work by Best et al. (2005), observing at 1.4 GHz, reported a steep mass dependence (f
rad
	​

∝M
∗
2.5
	​

) peaking at ~30% for the most massive galaxies, limited by the sensitivity and frequency of the NVSS survey. With the advent of the highly sensitive, low-frequency LOFAR telescope (150 MHz), Sabater et al. (2019) tracked radio emission to much lower surface brightnesses and probed older plasma ages (since lower frequency emission takes longer to cool). This revealed that essentially 100% of the most massive galaxies (>10
11
M
⊙
	​

) in the local universe are "always switched on," suggesting that continuous, low-level feedback is ubiquitous.

Furthermore, the theoretical derivation of a duty cycle is highly sensitive to the chosen denominator environment. As highlighted by Kondapally et al., defining the duty cycle simply by binning galaxies by stellar mass yields different results than computing it via Halo Occupation Distribution (HOD) parameters. This discrepancy arises because stellar-mass bins contain a broader, more heterogeneous mix of dark matter halo environments, whereas HOD restricts the denominator to the specific subset of halos consistent with the clustering signal, fundamentally altering the inferred fraction of active time.

Q6.b Envelope summary

Due to the profound impact of observational sensitivity and frequency on the detection of radio relics, the values are highly instrument-dependent. The duty cycle (incidence) of radio-AGN in the most massive galaxies ranges from ≈30% (at legacy 1.4 GHz limits) to 100% (at highly sensitive 150 MHz limits).

Q7 — Mass-metallicity and fundamental metallicity relation scatter

The mass-metallicity relation (MZR) establishes a clear, systematic correlation between a galaxy's stellar mass and its gas-phase oxygen abundance. The relation is theoretically interpreted as an ongoing balance between metal production via stellar nucleosynthesis, dilution from pristine or low-metallicity cosmological gas inflows, and metal expulsion via galactic winds. Extending this two-dimensional plane to a three-dimensional parameter space by including the Star Formation Rate (SFR) yields the Fundamental Metallicity Relation (FMR). Theoretically, the FMR should be redshift-invariant if the underlying physics of the gas-regulator (often termed the "bathtub") model remains consistent across cosmic time. Tracking the intrinsic scatter around this relation, and its potential evolution out to cosmic noon (z≈2.3), provides a stringent empirical test for chemical evolution models.

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
0.054 dex ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Residual metallicity scatter	T
e
	​

-based abundance scale	Global local galaxy population	N/A	z≈0	SDSS	Curti et al. 2020 (MNRAS 491, 944)
Factor of 3–5 lower ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	MZR metallicity offset at fixed mass	Near-IR optical emission lines	SF galaxies	Local benchmark MZR	z≈2.3	Keck (MOSDEF)	Sanders et al. 2021 / 2015
10–40% reduction ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Additional scatter reduction	Cosmological simulations	Simulated galaxies	Assuming "strong" FMR scatter	z≳3	IllustrisTNG / EAGLE	arXiv:2408.07974 / MNRAS 531, 1398
Q7.a Definition conflicts

Quantifying metallicity—specifically the oxygen abundance, commonly expressed as 12+log(O/H)—suffers from the notorious, long-standing discrepancies between direct methods (utilizing faint auroral lines like [OIII]λ4363 to directly determine the electron temperature, T
e
	​

) and empirical strong-line calibrations (e.g., R
23
	​

, N2, O3N2). Curti et al. (2020) anchor their exceptionally low intrinsic scatter (0.054 dex) in a fully T
e
	​

-based abundance scale, avoiding the systematic biases intrinsic to certain theoretical photoionization models.

The definition of the FMR itself also splits the community into competing interpretations: a "strong" FMR assumes the 3D surface perfectly describes galaxies independent of redshift, whereas a "weak" FMR permits some degree of time evolution in the strength of the correlated scatter with SFR. Recent JWST observations at higher redshifts (z>3) and cosmological simulations (IllustrisTNG, EAGLE) suggest that a strictly non-evolving strong FMR fails to capture evolving feedback efficiencies or changing inflow rates, reducing the residual scatter only if time evolution is explicitly parameterized within the model.

Q7.b Envelope summary

The values represent distinct physical measurements (scatter magnitude versus temporal offset magnitude) and thus a unified numerical envelope is not applicable. The intrinsic scatter of the local MZR/FMR is rigorously characterized at 0.054 dex, while the temporal evolution offsets normalizations at z≈2.3 by a factor of 3 to 5.

Q8 — z>10 galaxy abundance / stellar mass tension

The deployment of the James Webb Space Telescope (JWST) rapidly uncovered a population of unexpectedly luminous, red galaxy candidates at extreme redshifts (z>10). Early spectral energy distribution (SED) fitting indicated that these galaxies harbor stellar masses so high that they approach, or even seemingly exceed, the theoretical maximum allowed by the Λ Cold Dark Matter (ΛCDM) paradigm. Specifically, the inferred stellar mass densities suggest that a near-complete conversion of available cosmological baryons into stars (a star formation efficiency of ϵ≈1) would be required in the most massive halos, heavily stressing canonical limits which generally restrict efficiency to ϵ≈0.1−0.32. This has sparked a fierce debate across the astronomical community: does this represent a fundamental failure of the ΛCDM model, or are the observational inferences plagued by unrecognized, cascading systematic biases?

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
∼1.0 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Implied star formation efficiency (ϵ)	SED-derived stellar mass density	Most massive JWST galaxy candidates	Theoretical available baryonic mass	z≈7–10	JWST / CEERS	Boylan-Kolchin 2023 (Nat Astron 7, 731) / Labbé et al. 2023
≤0.32 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Canonical limit for star formation efficiency (ϵ)	Cosmological expectations	Dark matter halo mass function limits	Available baryonic mass	z≈7–10	Theoretical framework	Boylan-Kolchin 2023 (Nat Astron 7, 731)
Consistent (No Tension) ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Stellar masses / SFRs	Cosmological simulations	Massive galaxies in simulations	Observational data (JADES/CEERS)	z>10	Renaissance Simulations	McCaffrey et al. 2023 (Open Journal of Astrophysics 6)
Q8.a Definition conflicts

The crux of the "tension" relies heavily on the precarious conversion of broad-band photometric fluxes into absolute stellar masses. The authors highlighting the tension (e.g., Labbé et al., Boylan-Kolchin) rely on SED fitting methodologies that assume standard stellar Initial Mass Functions (IMFs). However, if the IMF in the early universe was "top-heavy"—meaning it overproduced massive, highly luminous stars relative to low-mass stars—the true stellar mass could be drastically lower for a given observed luminosity.

Furthermore, observational uncertainties such as Eddington bias (which artificially inflates the high-mass end of the mass function due to the steep slope of the halo mass function combined with large photometric scatter), extreme emission line contamination masquerading as continuum breaks, hidden AGN continuum contributions, and complex dust attenuation degeneracies can erroneously boost photometric mass estimates. "No-tension" analyses point out that when these observational systematics are fully accounted for, or when extremely high-resolution hydrodynamical simulations (e.g., Renaissance) are utilized to capture the highly stochastic and bursty nature of early star formation, the predicted galaxy properties align perfectly within standard ΛCDM bounds without requiring exotic new physics.

Q8.b Envelope summary

These values represent opposing theoretical interpretations and methodological frameworks rather than direct commensurable physical measurements. The core debate encompasses whether the true star formation efficiency approaches the extreme boundary of ∼1.0 (tension) or remains comfortably bounded by the canonical limit of ≤0.32 (no tension, assuming systematics drive the apparent mass excess).

Links ledger

Avery et al. 2021 | https://academic.oup.com/mnras/article/503/4/5134/6178852 | QUARANTINED_PENDING_LOCAL_CHECK
Oh et al. 2024 | https://arxiv.org/abs/2405.20627 | QUARANTINED_PENDING_LOCAL_CHECK
Förster Schreiber et al. 2019 | https://www.mpe.mpg.de/ir/KMOS3D/surveyscience | QUARANTINED_PENDING_LOCAL_CHECK
Nedelchev, Sarzi & Kaviraj 2019 | https://academic.oup.com/mnras/article/528/3/4976/7598247 | QUARANTINED_PENDING_LOCAL_CHECK
Davies et al. 2024 | https://arxiv.org/abs/2310.17939 | QUARANTINED_PENDING_LOCAL_CHECK
Spilker et al. 2018 | https://arxiv.org/html/2507.16914v1 | QUARANTINED_PENDING_LOCAL_CHECK
Fluetsch et al. 2019 | https://academic.oup.com/mnras/article/483/4/4586/5253620 | QUARANTINED_PENDING_LOCAL_CHECK
Concas et al. 2022 | https://academic.oup.com/mnras/article/513/2/2535/6568552 | QUARANTINED_PENDING_LOCAL_CHECK
Williams et al. 2021 | https://arxiv.org/html/2405.19401v2 | QUARANTINED_PENDING_LOCAL_CHECK
Ubertosi 2021 | https://amsdottorato.unibo.it/id/eprint/11315/1/PhDThesisUbertosi.pdf | QUARANTINED_PENDING_LOCAL_CHECK
Dunn & Fabian 2006 | https://academic.oup.com/mnras/article/373/3/959/1060742 | QUARANTINED_PENDING_LOCAL_CHECK
Hlavacek-Larrondo et al. 2015 | https://lss.fnal.gov/archive/2014/pub/fermilab-pub-14-547-ae.pdf | QUARANTINED_PENDING_LOCAL_CHECK
Best et al. 2005 | https://scholarlypublications.universiteitleiden.nl/access/item%3A3718024/download | QUARANTINED_PENDING_LOCAL_CHECK
Sabater et al. 2019 | https://arxiv.org/abs/1811.05528 | QUARANTINED_PENDING_LOCAL_CHECK
Curti et al. 2020 | https://academic.oup.com/mnras/article/491/1/944/5638748 | QUARANTINED_PENDING_LOCAL_CHECK
Boylan-Kolchin 2023 | https://arxiv.org/abs/2208.01611 | QUARANTINED_PENDING_LOCAL_CHECK
McCaffrey et al. 2023 | https://scispace.com/pdf/no-tension-jwst-galaxies-at-z-10-consistent-with-254vj021.pdf | QUARANTINED_PENDING_LOCAL_CHECK

GEMINI_WEB_RAMPAGE_R2_OUTPUT_DONE_20260711T052300Z

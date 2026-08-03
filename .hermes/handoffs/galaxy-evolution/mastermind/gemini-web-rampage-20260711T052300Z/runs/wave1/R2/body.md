Rampage R2 answer — REQ_RAMPAGE_R2_20260711T052300Z

Run date (UTC): 2026-07-11T05:44:00Z
Model: Gemini-1.5-Pro-Rampage-v2
Quantities addressed: 8 of 8

Q1 — Incidence of ionized AGN-driven outflows

The measurement of ionized gas outflows is fundamentally tied to the rest-frame optical and ultraviolet emission lines that trace the warm, ionized phase of the interstellar medium (ISM). Active Galactic Nuclei (AGN) inject substantial mechanical and radiative energy into their host environments, driving winds that can be mapped using strong forbidden lines (e.g., [O III] λ5007) or recombination lines (e.g., H$\alpha$, H$\beta$). Theoretical frameworks of galaxy evolution frequently invoke these ionized winds as the primary agent of "ejective" feedback, purportedly clearing the central kiloparsecs of star-forming material. To evaluate the ubiquity of this feedback mode, observational surveys deploy integral field spectrographs (IFUs) and multi-object slit spectroscopy to measure the prevalence of kinematically disturbed ionized gas across varied galaxy populations.   

The reported detection rates of these outflows vary significantly depending on the host galaxy's evolutionary state, the depth of the gravitational potential, and the instantaneous accretion rate of the central supermassive black hole. Deep spectroscopic surveys at cosmic noon (z≈1.5–3.5), such as the MOSDEF survey, observe that fast, galaxy-wide ionized outflows are widespread along the star-forming main sequence, indicating that such feedback mechanisms operate continuously throughout the peak epoch of cosmic star formation. Conversely, low-redshift spatially resolved studies, such as those utilizing the SDSS-IV MaNGA dataset, indicate that while outflow signatures are present in the local universe, their incidence is highly concentrated in systems exhibiting specific combinations of high central stellar mass density and elevated AGN luminosity.   

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
17% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of ionized outflows	H$\beta$, [O III], H$\alpha$, [N II]	H-band magnitude selected, X-ray/IR/optical AGN	All AGN in MOSDEF sample	z≈1.4–3.8	MOSFIRE / MOSDEF	[arXiv:1905.13338]
25% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		[O III] λ5007	Optical emission line AGN	MaNGA-selected AGN	z≈0.05	SDSS-IV MaNGA	[arXiv:1911.10212]
~50% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		[O III] or H$\alpha$	X-ray AGN (L
X
	​

=10
42−45
 erg/s)	X-ray selected sample	z≈0.6–1.7	VLT/KMOS	
~30% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		H$\alpha$	Low-mass targets with above-average SFR	Total low-mass sample	z≈0	SDSS	[arXiv:2604.05665v1]
Q1.a Definition conflicts

The reported incidence of ionized AGN-driven outflows is subject to severe definitional and methodological conflicts, rendering raw detection fractions across different surveys highly non-commensurable. The primary source of discrepancy lies in the kinematic thresholds utilized to define an "outflow." Because the ionized ISM is naturally subject to gravitational rotation and turbulent dispersion, distinguishing a genuine radial outflow from inherent disk kinematics requires setting specific velocity cutoffs.   

Many studies adopt non-parametric velocity indicators, such as W
80
	​

 (the velocity width containing 80% of the total emission line flux) or v
max
	​

. Research focusing on powerful, X-ray-selected AGN often sets highly stringent thresholds (e.g., W
80
	​

>500 km/s or v>600 km/s) to intentionally filter out low-velocity gas motions that could plausibly be driven by stellar feedback (supernovae and stellar winds) rather than the AGN itself. Consequently, samples pre-selected for extreme X-ray luminosity (tracing high accretion rates) inherently report vastly elevated prevalence rates of extreme kinematics (~50%) compared to mass-complete or volume-limited surveys. Conversely, applying lower velocity thresholds to detect weaker outflows increases the risk of contaminating the "AGN-driven" sample with star-formation-driven winds, fundamentally altering the numerator of the incidence ratio.   

A secondary conflict arises from instrumental resolution and aperture effects. In spatially unresolved or single-fiber observations (such as legacy SDSS data), the integrated spectrum blends the entire velocity field of the galaxy. To isolate an outflow, researchers must decompose the emission lines (typically [O III] or H$\alpha$) into multiple Gaussian components, assigning narrow components to the systemic disk and broad wings to the outflowing wind. The detectability of these broad wings is heavily dependent on the signal-to-noise ratio of the continuum and the specific fitting algorithms employed. IFU surveys like MaNGA or KMOS provide spatially resolved data, allowing for the subtraction of the systemic velocity field prior to identifying outflow signatures. This methodological divergence means that IFU surveys and single-fiber surveys are measuring fundamentally different spatial scales of the gas distribution.   

Furthermore, defining the outflow as strictly "AGN-driven" introduces multi-wavelength classification conflicts. Disagreements exist regarding whether the broad kinematic component itself must exhibit Seyfert-like line ratios on a BPT (Baldwin-Phillips-Terlevich) diagram, or if simply detecting an outflow in a galaxy that hosts a nuclear AGN is sufficient. If a survey requires the outflowing gas itself to be photoionized by the AGN, it systematically excludes neutral or shock-ionized winds that may still be mechanically driven by the central black hole.   

Q1.b Envelope summary

For broadly defined incidence of ionized AGN-driven outflows (without restricting to extreme X-ray luminosities or specifically isolated low-mass regimes), the published envelope spans 17% to 25%.

Q2 — Incidence of neutral AGN-driven outflows

While ionized gas is highly luminous and relatively straightforward to observe, it represents only a fraction of the total mass and momentum budget of a galactic wind. The neutral atomic phase, typically traced by resonant absorption lines, is theorized to carry a significantly larger portion of the outflowing mass. Observations of the neutral phase provide crucial constraints on the ability of AGN feedback to entrain and expel the cold, dense material from which stars physically form.   

The primary observational tracer for neutral gas outflows at optical wavelengths is the Na I D λλ5890, 5895 Å doublet. Because this transition requires a bright background continuum source against which the absorption can be measured, detecting neutral outflows relies heavily on the surface brightness of the host galaxy's stellar disk. Recent high-redshift observations utilizing the James Webb Space Telescope (JWST) have revealed that interstellar Na I D absorption is prevalent in massive galaxies at cosmic noon, suggesting that large neutral gas reservoirs are frequently subjected to ejective feedback. In the local universe, statistical studies often rely on spectral stacking techniques to achieve the requisite signal-to-noise to detect these faint absorption features.   

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
46% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of excess neutral absorption	Na I D	Massive galaxies (logM
∗
	​

>10)	Massive galaxies in survey	z≈1.7–3.5	JWST/NIRSpec (Blue Jay)	[arXiv:2310.17939]
~5% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Incidence of neutral outflows	Na I D	Line-emitting galaxies	Total analysed line-emitting sample	z≈0.04	SDSS-IV MaNGA	[arXiv:2201.08079]
30% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		Na I D	Massive quiescent (logM
∗
	​

>10.5)	Total quiescent sample	z≈2.8–4.6	JWST (DeepDive)	[arXiv:2602.17767v2]
~30% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		Na I D	Star-forming main-sequence (M
∗
	​

>10
10
M
⊙
	​

)	Total high-mass sample	z≈0	SDSS	[arXiv:2604.05665v1]
Q2.a Definition conflicts

The empirical determination of neutral outflow incidence is beset by severe systematic and geometrical biases, heavily complicating the interpretation of the Na I D feature. The foremost conflict arises from the complex physics of the Na I D transition itself. It is a resonant line, meaning photons can be both absorbed and re-emitted by the gas, sometimes filling in the absorption trough and producing P-Cygni profiles. Furthermore, Na I D absorption is intrinsically blended with strong stellar atmospheric absorption present in the host galaxy's older stellar populations. To isolate the interstellar contribution tracing the outflow, observers must subtract the stellar continuum using high-resolution stellar population synthesis models. Discrepancies between different modeling codes or the chosen library of stellar templates can artificially inflate or mask the residual absorption, directly altering the calculated detection fraction.   

A secondary, yet profound, definitional conflict is the dependence on galaxy inclination. The detection of Na I D in absorption inherently requires the outflowing gas to intersect the line of sight toward a bright background continuum. If outflows are biconical and propagate perpendicular to the galactic disk, face-on galaxies present a highly favorable geometry for detecting blueshifted absorption. Conversely, in edge-on systems, the line of sight primarily intersects the dense, rotating ISM of the disk rather than the perpendicular wind, and severe dust extinction further degrades the continuum signal. Consequently, surveys that do not explicitly correct for inclination biases report raw incidence rates (e.g., ~5% in local volume-limited surveys) that represent strict lower limits. High-redshift JWST studies reporting incidence rates near 46% often target explicitly massive, dust-rich systems where the column densities of neutral sodium are naturally higher, introducing non-commensurability when compared against mass-complete local samples.   

Finally, sodium is not a perfect proxy for total hydrogen mass. Converting the measured Na I D equivalent width into a neutral hydrogen column density (N
HI
	​

) requires adopting highly uncertain ionization corrections and assuming a uniform dust depletion factor, as sodium readily condenses onto dust grains. Differing assumptions regarding the metallicity and ionization state of the outflowing clumps lead to order-of-magnitude variations in the interpreted strength of the outflow, which cascades into the classification of what constitutes a "detected" wind.   

Q2.b Envelope summary

For the general incidence of neutral outflows traced by Na I D in broad samples (excluding those restricted to quiescent phases), the published envelope ranges from ~5% in the local universe to 46% at cosmic noon.

Q3 — Mass-loading factors (η)

The mass-loading factor (η=
M
˙
out
	​

/SFR) is arguably the most critical parameter in cosmological simulations governing galaxy evolution. It quantifies the efficiency of ejective feedback, dictating how many solar masses of gas are expelled from the galaxy per solar mass of stars formed. Theoretical models rely heavily on η to regulate the stellar mass function, prevent the overproduction of stars in high-mass halos, and reproduce the observed mass-metallicity relations.

Observationally, constraining η requires precise measurements of both the numerator (the mass outflow rate, 
M
˙
out
	​

) and the denominator (the star formation rate, SFR). Because galactic winds are multi-phase structures, η is typically reported separately for the ionized, neutral, and molecular components. Low-mass galaxies are generally modeled as having highly efficient stellar feedback with mass-loading factors significantly exceeding unity, whereas high-mass galaxies are expected to exhibit lower stellar mass-loading unless boosted by the energetic output of an AGN. The literature contains a vast parameter space of mass-loading values, reflecting the extreme diversity of the physical systems observed and the myriad assumptions required to calculate the gas masses.   

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
0.8 (median) ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		H$\beta$, [O III]	Star-forming and AGN	SFR	z≈1.4–3.8	MOSFIRE / MOSDEF	[arXiv:1905.13338]
0.07 (mean) ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		H$\alpha$	Low-mass galaxies	SFR	z≈0	SDSS	[arXiv:2604.05665v1]
4 to 360		Na I D	Quenching systems (logsSFR<−10)	SFR	z≈1.7–3.5	JWST/NIRSpec	[arXiv:2310.17939]
1 to 4		CO line mapping	Starburst galaxies	SFR	z≈0	ALMA/IRAM	
~0.7 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		OH 119$\mu$m	Dusty star-forming	SFR	z≈0	ALMA	
Q3.a Definition conflicts

The mass-loading factor (η) represents a nexus of systemic observational conflicts, as both the numerator and denominator depend heavily on unverified scaling relations and geometric assumptions. Consequently, values reported across different gas phases or different host populations are severely non-commensurable.

The calculation of the mass outflow rate (
M
˙
out
	​

) in the numerator varies fundamentally across the gas phases. In the ionized phase, 
M
˙
out
	​

 is inversely proportional to the assumed electron density (n
e
	​

) of the outflowing material. Traditional optical studies estimate n
e
	​

 from the λλ6716, 6731 line ratio, typically yielding values of 100–300 cm$^{-3}. However, this diagnostic primarily traces the diffuse ISM; the outflowing gas is likely highly clumped. Utilizing auroral lines to probe denser regions often yields $n_e > 1000$ cm^{-3}.Ashiftintheassumedelectrondensityfrom100to1000cm^{-3}$ mechanically reduces the derived ionized mass-loading factor by an entire order of magnitude. For the molecular phase, 
M
˙
out
	​

 relies heavily on the chosen CO-to-H$2$ conversion factor ($\alpha{CO}$). The literature is divided on whether outflowing molecular clumps should be assigned a Milky Way-like α
CO
	​

 (~4.3) or a starburst/ULIRG α
CO
	​

 (~0.8), introducing a factor of five variance in the resulting molecular η.   

Geometric modeling of the wind introduces further discrepancies. Observers must choose between assuming a spherical, mass-conserving shell or a biconical wind characterized by a specific opening angle and covering fraction. The physical extent of the wind (R
out
	​

) often appears in the denominator of the 
M
˙
out
	​

 equation; overestimating R
out
	​

 (e.g., by failing to account for beam smearing) artificially depresses the mass-loading factor.   

The most profound definitional conflict, however, resides in the denominator (SFR). There is a fundamental timescale mismatch: outflow kinematics trace an instantaneous phenomenon (spanning ~1 to 10 Myr), whereas conventional SFR indicators (such as infrared dust continuum or UV emission) average star formation over 10 to 100 Myr. This mismatch severely distorts η in transient or quenching systems. As a galaxy undergoes rapid quenching, its instantaneous SFR plummets, causing the mathematical value of η to asymptote toward infinity. This artifact is evident in quenching systems reporting η values up to 360. Comparing the mass-loading factor of a steady-state main-sequence galaxy directly against that of a rapidly quenching galaxy merges completely different evolutionary regimes.   

Q3.b Envelope summary

Due to strict phase dependencies (ionized vs. neutral vs. molecular) and severe mathematical artifacts introduced by differing SFR denominators and quenching stages, all values are deemed non-commensurable. An envelope summary is not applicable.

Q4 — Molecular gas fractions and depletion times

The cessation of star formation in massive galaxies—a process termed "quenching"—is intrinsically linked to the availability of cold, dense molecular gas. Understanding whether quiescent galaxies are devoid of molecular fuel (supporting models of rapid ejective feedback) or simply inefficient at converting remaining gas into stars (supporting morphological stabilization or turbulence models) requires precise measurements of molecular gas fractions (f
gas
	​

=M
H2
	​

/M
∗
	​

) and depletion times (t
dep
	​

=M
H2
	​

/SFR).

Large-scale observing programs operating at millimeter and submillimeter wavelengths have mapped the cold gas contents of galaxies across cosmic time. In the local universe, surveys like xCOLD GASS demonstrate that molecular gas fractions decline steeply as galaxies transition from the star-forming main sequence to the passive sequence. Pushing these measurements to high redshifts (z≈1.5–3.0), where the first massive galaxies ceased star formation, requires extreme sensitivity. Deep ALMA observations of lensed, high-redshift quiescent galaxies reveal molecular gas fractions orders of magnitude lower than those of coeval star-forming systems, implying that early quenching events were associated with highly efficient gas consumption or expulsion.   

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
~0.01 (1%) ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Molecular gas fraction upper limit	1.3mm dust emission	Lensed quenched galaxies	M
∗
	​

	z≈2–3	ALMA	
< 2 to 6%	Molecular gas fraction upper limit	CO(2-1) emission	Massive quiescent	M
∗
	​

	z≈1.5	ALMA	[arXiv:2012.01433]
0.3 to 1%	Molecular gas fraction	CO(1-0) emission	Local quiescent galaxies	M
∗
	​

	z≈0	IRAM-30m (xCOLD GASS)	[arXiv:1702.01140]
~0.7 Gyr ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		CO/dust combined	Main-sequence star-forming	SFR	z≈1–3	PHIBSS	[arXiv:1702.01140]
Q4.a Definition conflicts

Estimates of molecular gas fractions and depletion times in quiescent galaxies are heavily reliant on the choice of gas tracer and the unverified scaling relations required to convert those tracers into physical masses.

The primary divergence in the literature is between studies utilizing the far-infrared dust continuum (e.g., 1.3mm observations) and those utilizing carbon monoxide (CO) emission lines. Studies inferring gas mass from dust continuum measurements must assume a fixed dust-to-gas ratio, typically scaled from the mass-metallicity relation of local star-forming galaxies. However, the physics governing dust creation and destruction in rapidly quenching, high-redshift galaxies remain highly uncertain. If massive quiescent galaxies exhibit anomalous dust-to-gas ratios—due to halted chemical enrichment or active dust destruction by supernova shocks and AGN feedback—the inferred molecular gas mass will be severely biased. Some theoretical models (e.g., SIMBA) predict that the dust-to-gas ratio varies wildly in low-SFR galaxies, rendering continuum-based gas estimates highly speculative.   

Conversely, studies relying on low-J CO transitions (e.g., CO(1-0) or CO(2-1)) avoid dust scaling uncertainties but must contend with the α
CO
	​

 conversion factor. The α
CO
	​

 parameter relates CO luminosity to total molecular hydrogen mass and is notoriously sensitive to gas metallicity, density, and interstellar radiation fields. Applying a Milky Way-like α
CO
	​

 to a compact, early-universe post-starburst galaxy may overestimate the gas mass, masking the true efficiency of the quenching mechanism. Furthermore, high-redshift observations of quiescent galaxies frequently yield non-detections, forcing researchers to report upper limits (e.g., f
gas
	​

<2−6%). These upper limits are highly dependent on the assumed line width utilized during the integration of the non-detected signal.   

Finally, interpreting depletion times (t
dep
	​

) in quiescent galaxies presents a conceptual conflict. The denominator (SFR) is exceedingly low, meaning the calculated depletion time can appear artificially long, even if the absolute gas reservoir is nearly exhausted. Theoretical frameworks dispute whether low gas fractions are the result of violent "blowout" (rapid ejection via AGN winds) or "starvation/strangulation" (the cessation of cosmological accretion combined with steady consumption at normal depletion rates). Observational upper limits cannot uniquely distinguish between these two divergent evolutionary pathways.   

Q4.b Envelope summary

For the molecular gas fraction of quenched/quiescent galaxies across z≈0 to z≈3, the published envelope indicates values and strict upper limits ranging from 0.3% to 6%.

Q5 — X-ray cavity power vs cooling luminosity balance

In the cores of massive galaxy clusters, the density of the hot intracluster medium (ICM) is so high that the plasma's radiative cooling time falls significantly below the Hubble time. Without a counteracting heat source, this plasma should undergo a catastrophic cooling flow, depositing thousands of solar masses of cold gas onto the central Brightest Cluster Galaxy (BCG). Observations, however, indicate that star formation rates in BCGs are an order of magnitude lower than predicted by unimpeded cooling flow models. The widely accepted solution is "radio-mode" AGN feedback: relativistic jets launched by the central supermassive black hole inflate massive bubbles of radio plasma within the ICM, displacing the thermal gas and creating X-ray surface brightness depressions known as cavities.   

To quantify whether this mechanical feedback is sufficient to offset radiative losses, researchers measure the ratio of the mechanical cavity power (P
cav
	​

) against the cooling luminosity (L
cool
	​

) within the cluster core. Studies of local cool-core clusters frequently find that the mechanical energy injected by these cavities scales closely with the cooling losses, maintaining a delicate thermodynamic balance. However, the exact fraction of clusters exhibiting these cavities, and the precise mechanical energy they contain, remain subject to deep observational and modeling constraints.   

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
~1 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Ratio of cavity power to cooling luminosity (P
cav
	​

/L
cool
	​

)	X-ray surface brightness	Cool core clusters	L
cool
	​

	z<0.3	Chandra	
50% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		X-ray surface brightness	MACS cluster sample	Total MACS sample	z>0.3	Chandra	
>88% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		X-ray mocks	TNG-Cluster matched sample	Total cavity-hosting clusters	z≈0	TNG / Chandra mocks	[arXiv:2503.01965]
Q5.a Definition conflicts

The effort to balance cavity power against cooling luminosity is heavily constrained by nesting geometric, thermodynamic, and temporal assumptions that render precise calculations highly uncertain. The calculation of the mechanical cavity power (P
cav
	​

=E/t
buoy
	​

) requires an estimate of the total energy injected into the cavity (E) and the timescale over which the cavity rose buoyantly to its current position (t
buoy
	​

).

The total energy is typically approximated by the cavity's enthalpy. The literature is divided on whether the appropriate enthalpy calculation is pV (assuming purely thermal heating) or 4pV (assuming the cavity is dominated by relativistic plasma). The choice between these two thermodynamic models alters the resulting P
cav
	​

 by a factor of four. Furthermore, determining the cavity volume (V) introduces severe projection effects. X-ray images provide only a two-dimensional projection of the cluster; determining the line-of-sight depth of a cavity requires assuming a geometric shape, usually an oblate or prolate ellipsoid. Unsharp masking techniques, frequently employed to highlight these surface brightness depressions against the bright cluster core, are known to systematically underestimate the true spatial extent of the cavities, leading to a chronic underestimation of the injected energy.   

The denominator in the thermodynamic balance equation, L
cool
	​

, introduces its own definitional conflicts. The calculation of cooling luminosity depends entirely on the chosen boundary of the cooling radius (r
cool
	​

). Various studies employ different dynamical definitions for r
cool
	​

. Some calculate it as the radius where the cooling time equals the look-back time to z=1 (approximately 7.7 Gyr) , while others apply fixed physical apertures (e.g., 50 kpc) or stricter temporal thresholds (t
cool
	​

<1 Gyr or t
cool
	​

<3 Gyr) to classify a system as a "Strong Cool Core". Consequently, the ratio of P
cav
	​

/L
cool
	​

 is highly malleable depending on the specific radial cutoff applied.   

Finally, the detection fraction of cavities across broad cluster samples is heavily influenced by observational depth. Early high-redshift observations (e.g., from the SPT-SZ survey) reported significantly lower cavity fractions (~7%) compared to local samples. However, simulations and deeper follow-ups suggest this discrepancy may arise largely because shallow exposures systematically miss smaller or older cavities obscured by the highly peaked surface brightness of strong cool cores, artificially suppressing the perceived duty cycle of AGN feedback at high redshift.   

Q5.b Envelope summary

Due to differing estimands (thermodynamic power ratios versus specific sample incidence fractions), the tabulated values are non-commensurable. An envelope summary is not applicable.

Q6 — Radio-AGN duty-cycle estimates

In addition to the highly visible, radiatively efficient "quasar mode" of AGN feedback, supermassive black holes exhibit a radiatively inefficient "maintenance mode" characterized by the steady inflation of radio jets. Cosmological models rely on this maintenance mode to continuously deposit energy into massive halos, counteracting the cooling of hot gas and preventing the resurgence of star formation in massive elliptical galaxies. The efficacy of this preventative feedback is dictated by its duty cycle—the fraction of time a galaxy spends actively hosting a radio-loud AGN.   

Statistical surveys utilize vast radio catalogs cross-matched with optical spectroscopy to quantify the prevalence of radio-AGN activity across different stellar mass bins. In the local universe, legacy surveys establish that the probability of a galaxy hosting a radio AGN is a steep function of its stellar mass, implying that the most massive systems undergo frequent, episodic jet activity. Advancements in low-frequency radio interferometry have recently expanded this perspective, revealing that low-surface-brightness radio emission is virtually ubiquitous in the most massive galaxies, suggesting a duty cycle that approaches 100%.   

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
100% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Prevalence of radio AGN	150 MHz radio	Massive galaxies (M
∗
	​

>10
11
M
⊙
	​

)	Total massive sample	z<0.3	LOFAR	[arXiv:1811.05528]
f
radio
	​

∝M
∗
2.5
	​

 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		1.4 GHz radio	Local galaxies	Total sample per mass bin	z≈0.03–0.1	NVSS/SDSS	
5 to 10 × ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		3 GHz radio	Quiescent massive galaxies	Total local massive galaxies	z≈1	VLA/LEGA-C	
Q6.a Definition conflicts

Estimates of the radio-AGN duty cycle are highly sensitive to the observing frequency, creating a sharp definitional divide between historical and contemporary studies. Legacy studies utilizing 1.4 GHz surveys (such as NVSS or FIRST) predominantly trace relatively young, highly energetic jet plasma. These high-frequency surveys indicate a steep mass dependence, often quoted as f
radio
	​

∝M
∗
2.5
	​

. This steep scaling implies that radio triggering is episodic and intermittent, with lower-mass galaxies switching on infrequently.   

However, low-frequency observations, such as those conducted at 150 MHz by LOFAR, are sensitive to older, low-surface-brightness synchrotron plasma left over from previous outbursts. Because high-energy electrons age and radiate their energy away faster than low-energy electrons, 1.4 GHz emission fades rapidly once the jet switches off, while 150 MHz emission persists as a "fossil" record of past activity. By tracing this older plasma, LOFAR studies report that the incidence of radio-AGN activity reaches nearly 100% in the most massive galaxies (M
∗
	​

>10
11
M
⊙
	​

). This indicates a maintenance-mode duty cycle that is essentially continuous, fundamentally altering the parameters used in cosmological simulations.   

Further conflict arises from the classification criteria utilized to separate radio AGN into High-Excitation Radio Galaxies (HERGs) and Low-Excitation Radio Galaxies (LERGs). HERGs are typically fueled by cold gas accretion (often associated with gas-rich mergers) and exhibit strong optical emission lines, whereas LERGs are fueled by the gradual cooling of hot halo gas in a radiatively inefficient state. At low redshifts, LERGs dominate the quiescent, massive galaxy population. However, deep surveys at z≈1 reveal that a significant fraction of LERGs reside in star-forming hosts, blurring the rigid boundary between maintenance-mode feedback (associated with quiescence) and quasar-mode feeding (associated with star formation). Consequently, tracking the duty cycle of "maintenance mode" across cosmic time requires careful cross-matching of radio morphology, spectral indices, and host galaxy star-formation states.   

Q6.b Envelope summary

Due to differing estimands (absolute prevalence percentages, scaling exponents, and relative epoch ratios), the values are non-commensurable. An envelope summary is not applicable.

Q7 — Mass–metallicity / fundamental-metallicity-relation scatter

The chemical enrichment of a galaxy is governed by the interplay of star formation, the accretion of pristine gas from the intergalactic medium, and the ejection of metal-enriched material via galactic winds. This baryon cycling is empirically tracked through the Mass-Metallicity Relation (MZR), which demonstrates that more massive galaxies retain deeper gravitational potentials and thus exhibit higher gas-phase oxygen abundances. However, the MZR exhibits significant intrinsic scatter.   

To account for this scatter, the Fundamental Metallicity Relation (FMR) introduces the Star Formation Rate (SFR) as a third parameter, defining a tightly constrained 3D surface encompassing Stellar Mass, SFR, and Metallicity. In the local universe, the FMR minimizes the residual scatter in metallicity to exceptionally low values, implying a smooth, time-invariant equilibrium. Testing the universality of the FMR at higher redshifts (z≈2.3 to z≈5) is a primary goal of deep spectroscopic surveys, as deviations from the local relation provide critical constraints on the burstiness of early star formation and the efficiency of early metal-rich outflows.   

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
0.054 dex ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Residual scatter around FMR	Optical strong lines	SDSS global population	N/A	z≈0.08	SDSS	
0.15 to 0.3 dex		Optical strong lines (N2, O3N2)	Star-forming galaxies	N/A	z≈2.3	MOSDEF	[arXiv:1408.2521]
~0.27 dex ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		Rest-optical emission	Massive main-sequence	N/A	z≈5	ALPINE-CRISTAL	
Q7.a Definition conflicts

The scatter and absolute normalization of the MZR and FMR suffer from profound methodological divides regarding how gas-phase metallicity is calculated. The theoretical gold standard is the "direct method," which utilizes the electron temperature (T
e
	​

) derived from faint auroral lines (e.g., [O III] λ4363). However, these auroral lines are exceptionally difficult to detect, particularly in massive, metal-rich galaxies where efficient cooling severely suppresses the electron temperature. Consequently, the vast majority of statistical studies rely on empirical "strong-line" calibrations (e.g., R23, N2, O3N2), which utilize ratios of bright oxygen and nitrogen lines.   

These strong-line calibrations are highly sensitive to the ionization parameter and the hardness of the ionizing radiation field. High-redshift galaxies (z≈2.3) typically exhibit harder radiation fields and higher ionization parameters than local galaxies. When locally calibrated strong-line diagnostics are applied to high-redshift spectra, they introduce severe systematic offsets. The observed 0.15 to 0.3 dex offset of MOSDEF galaxies below the local MZR may partially reflect genuine chemical evolution—wherein rapid accretion of pristine cosmological gas dilutes the ISM—but it may also be an artifact of applying incompatible local calibrations to high-redshift ionization environments.   

Furthermore, the theoretical underpinning of the FMR assumes a steady-state equilibrium between inflows, outflows, and star formation. The local FMR scatter is minimized (to 0.054 dex) by defining optimal mathematical projections of the 3D surface. However, recent JWST and ALMA observations at z≈5 report an FMR scatter up to five times larger than the local relation. This increased scatter highlights a physical conflict: in the early universe, star formation is likely highly bursty rather than continuous, and metal mixing timescales are long compared to the dynamical time. Consequently, attempts to force high-redshift galaxies onto a locally defined, equilibrium-based FMR surface obscure the chaotic nature of early baryon cycling.   

Q7.b Envelope summary

Due to differing estimands (local residual scatter vs. high-redshift absolute MZR offsets vs. relative scatter increases), the tabulated values are non-commensurable. An envelope summary is not applicable.

Q8 — z>10 galaxy abundance and stellar-mass tension

The deployment of the James Webb Space Telescope (JWST) has extended the observable frontier of galaxy formation beyond redshift z>10. Early photometric observations utilizing the NIRCam instrument revealed a surprisingly high abundance of exceptionally UV-bright galaxies in the first 500 million years after the Big Bang. When these rest-frame UV luminosities were converted into stellar masses, several studies inferred cumulative cosmic stellar mass densities that appeared to severely challenge, or outright violate, the predictions of standard ΛCDM cosmological models and established empirical galaxy formation frameworks.   

This discrepancy has sparked a profound debate in the literature, broadly divided into "tension" and "no-tension" analyses. Tension models argue that the underlying cosmology must be amended (e.g., via Early Dark Energy models) to accelerate halo assembly, while no-tension models argue that the discrepancy is an artifact of applying incorrect astrophysical priors (such as star formation histories or dust laws) to an unprecedented epoch of galaxy evolution.   

Value ± uncertainty	Definition/estimand	Tracer	Selection/sample	Denominator (if ratio)	Redshift range	Instrument/survey	Citation
>10
5
M
⊙
	​

Mpc
−3
 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Cosmic stellar mass density tension	JWST photometry	Massive galaxies (M
∗
	​

>10
9
M
⊙
	​

)	N/A	2.5<z<9	JWST/NIRCam	
logρ
∗
	​

=4.7
−0.8
+0.5
	​

M
⊙
	​

Mpc
−3
	Cosmic stellar mass density estimate	JWST photometry	Bright UV candidates (M
UV
	​

≈−18)	N/A	z≈10	JWST/NIRCam	
Steady decline ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE		JWST ERO/ERS + UltraVISTA	All selected high-z candidates	N/A	z=8–15	JWST/NIRCam	[arXiv:2207.12356]
Q8.a Definition conflicts

The apparent tension regarding the abundance and mass of z>10 galaxies is rooted in the precarious translation of photometric fluxes into physical stellar masses. This translation relies entirely on Spectral Energy Distribution (SED) fitting, which requires the researcher to adopt specific, unverified priors regarding the galaxy's Star Formation History (SFH), the Initial Mass Function (IMF), and the behavior of interstellar dust.   

A primary conflict involves the assumed SFH. Standard models calibrated in the local universe often assume smooth, continuous, or exponentially declining star formation. However, if early galaxies undergo highly stochastic, bursty star formation, their rest-frame UV luminosity will be temporarily dominated by a small, transient population of extremely luminous O and B stars. If an SED fitting code incorrectly forces a smooth SFH onto a bursty galaxy, it will mathematically infer a massive underlying population of older, dimmer stars to account for the total integrated light, thereby artificially inflating the stellar mass by orders of magnitude.   

Similarly, the choice of the Initial Mass Function introduces severe definitional variance. The standard ΛCDM framework typically assumes a universal, bottom-heavy IMF (e.g., Salpeter or Chabrier). However, in the low-metallicity, high-temperature environments of the early universe, star formation may be heavily biased toward massive stars, resulting in a top-heavy IMF. A top-heavy IMF produces significantly more UV luminosity per unit of stellar mass. Consequently, analyses adopting a top-heavy IMF report no fatal tension, as the observed UV brightness can be achieved with significantly less total stellar mass.   

Finally, early photometric redshift estimates are highly susceptible to contamination. Strong nebular emission lines (such as [O III] or H$\alpha$) can mimic the continuum breaks used to identify high-redshift candidates, scattering lower-redshift interlopers into the z>10 bins. Furthermore, strong damped Ly$\alpha$ absorption (DLAs) from dense neutral gas reservoirs can systematically bias photometric redshifts, artificially altering the cosmic UV luminosity density calculations. As spectroscopic follow-ups gradually replace photometric estimates, the absolute magnitude of the "tension" continues to fluctuate based on the specific sample and calibration methodology employed.   

Q8.b Envelope summary

Due to differing estimands (absolute mass density thresholds vs. specific logarithmic volume measurements vs. qualitative luminosity trends), the values are non-commensurable. An envelope summary is not applicable.

Links ledger

MOSDEF Outflows | [arXiv:1905.13338] | QUARANTINED_PENDING_LOCAL_CHECK
MaNGA Ionized | [arXiv:1911.10212] | QUARANTINED_PENDING_LOCAL_CHECK
KMOS Outflows | | QUARANTINED_PENDING_LOCAL_CHECK
Concas Low-mass | [arXiv:2604.05665v1] | QUARANTINED_PENDING_LOCAL_CHECK
Blue Jay Neutral | [arXiv:2310.17939] | QUARANTINED_PENDING_LOCAL_CHECK
MaNGA Neutral | [arXiv:2201.08079] | QUARANTINED_PENDING_LOCAL_CHECK
DeepDive Quiescent | [arXiv:2602.17767v2] | QUARANTINED_PENDING_LOCAL_CHECK
Fluetsch Molecular | | QUARANTINED_PENDING_LOCAL_CHECK
Whitaker Quenched | | QUARANTINED_PENDING_LOCAL_CHECK
Williams Quiescent | [arXiv:2012.01433] | QUARANTINED_PENDING_LOCAL_CHECK
Saintonge xCOLD | [arXiv:1702.01140] | QUARANTINED_PENDING_LOCAL_CHECK
Rafferty Cooling | | QUARANTINED_PENDING_LOCAL_CHECK
MACS Cavities | | QUARANTINED_PENDING_LOCAL_CHECK
TNG Cavities | [arXiv:2503.01965] | QUARANTINED_PENDING_LOCAL_CHECK
LOFAR Radio | [arXiv:1811.05528] | QUARANTINED_PENDING_LOCAL_CHECK
NVSS Radio | | QUARANTINED_PENDING_LOCAL_CHECK
VLA Radio z~1 | | QUARANTINED_PENDING_LOCAL_CHECK
Curti FMR | | QUARANTINED_PENDING_LOCAL_CHECK
MOSDEF MZR | [arXiv:1408.2521] | QUARANTINED_PENDING_LOCAL_CHECK
ALPINE FMR | | QUARANTINED_PENDING_LOCAL_CHECK
Labbe Tension | | QUARANTINED_PENDING_LOCAL_CHECK
Harikane Mass | | QUARANTINED_PENDING_LOCAL_CHECK
Donnan Decline | [arXiv:2207.12356] | QUARANTINED_PENDING_LOCAL_CHECK
ALMA Outflow | | QUARANTINED_PENDING_LOCAL_CHECK

GEMINI_WEB_RAMPAGE_R2_OUTPUT_DONE_20260711T052300Z

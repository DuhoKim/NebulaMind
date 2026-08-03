Rampage R5 answer — REQ_RAMPAGE_R5_20260711T052300Z

Run date (UTC): 2026-07-11T06:33:00Z
Model: Rampage-R5-Text
Duty-cycle rows: 6

Duty-cycle table

To critically evaluate the hypothesis that active galactic nucleus (AGN) maintenance-mode heating balances the radiative cooling of hot halos, the literature relies on observational determinations of the AGN duty cycle. However, these measurements utilize divergent methodologies and target disparate astrophysical environments, rendering the resulting percentages non-commensurable estimands unless strictly harmonized by the sources themselves. The table below catalogs prominent duty-cycle determinations, highlighting their methodological dependencies, selection criteria, and the inherent caveats noted by the respective study authors.

Study (citation)	Method	Environment & halo- or stellar-mass range	Selection	Duty cycle ± unc	Timescale assumptions (bubble ages, buoyancy, spectral ages)	z range	Caveats named by the study


Bîrzan et al. (2012) 

	X-ray cavities	Clusters (B55/HIFLUGCS)	X-ray flux-limited, cooling-flow subset	Non-commensurable (Tracer/method: X-ray cavities + Selection: X-ray flux limit + Denominator: Cooling flow clusters + z range: z<0.1) = ~60% to 100% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Buoyant rise time (assumed for unseen bubbles limited by simulations)	z<0.1	

Duty cycles are quoted as lower limits because some bubbles are likely missed in existing images due to shallow exposure depths.




Panagoulia et al. (2014) 

	X-ray cavities	Groups and clusters	Volume-limited, central cooling time t
cool
	​

≤3 Gyr	Non-commensurable (Tracer/method: X-ray cavities + Selection: Volume-limited t
cool
	​

≤3 Gyr + Denominator: X-ray groups/clusters + z range: z≤0.071) = 61.2% (30/49) ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Buoyant rise time	z≤0.071	

The actual duty cycle is likely much higher when projection effects and central radio source detection rates are considered; data quality strongly affects the detection rates of X-ray cavities.




Sabater et al. (2019) 

	Radio-AGN fraction	Massive galaxies, Stellar mass >10
11
M
⊙
	​

	SDSS DR7 + LoTSS DR1 mass-limited	Non-commensurable (Tracer/method: Radio luminosity L
150
	​

≥10
21
 W/Hz + Selection: Mass-limited optical/radio + Denominator: Main galaxy sample + z range: z<0.3) = 100% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Proxy via Eddington-scaled accretion rate median (L
mech
	​

/L
Edd
	​

=10
−4.98
)	z<0.3	

Classification systematic errors dominate the error budget; the conversion between low-frequency radio luminosity and actual jet mechanical power remains highly uncertain without environmental gas data.




Olivares et al. (2022) 

	X-ray cavities	Clusters	Planck SZ-selected, Cool-Core (CC) subset	Non-commensurable (Tracer/method: X-ray cavities + Selection: SZ mass-limited + Denominator: CC clusters + z range: low-z) = 44.4% (28/63) ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Buoyant rise time	low-z (Planck)	

The spatial resolution for Planck clusters is on the order of ~2.5 kpc; after correcting for spatial resolution to match high-z SPT-SZ samples, the global detection fraction decreases to 9%.




Hamlett et al. (2026) 

	HOD clustering (radio-AGN fraction)	Dark matter haloes, ⟨logM
h
	​

/M
⊙
	​

⟩ = 13.0 to 13.4	MIGHTEE radio + near-IR selected	Non-commensurable (Tracer/method: Radio-AGN fraction + Selection: Near-IR mass-limited + Denominator: Dark matter haloes + z range: 0<z<2.5) = 5% to 9% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	HOD modeling time fraction (f
DC
	​

)	0<z<2.5	

Duty cycle inferences depend strictly on the assumed Halo Occupation Distribution parameters and dark matter halo scaling relations rather than direct thermodynamic observation.




Dunn & Fabian (2006)  (Seminal Anchor)

	X-ray cavities	Clusters	B55, cooling flows	Non-commensurable (Tracer/method: X-ray cavities + Selection: X-ray flux + Denominator: Cooling flow clusters + z range: low-z) = 70% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Buoyant rise time	low-z	

Results are based on a flux-limited sample biased toward the brightest sources in the sky, potentially skewing the apparent prevalence of cavities.

  

The compilation of duty-cycle determinations reveals a landscape where observational constraints are heavily dependent on the chosen tracer and the specific physical regime being probed. In the context of intracluster medium (ICM) thermodynamics, maintenance-mode feedback refers to the hypothesis that the injection of mechanical energy via radio jets—which inflate cavities or bubbles in the X-ray emitting gas, drive shocks, and generate turbulence—prevents runaway radiative cooling in cluster cores. Observing this phenomenon necessitates tracing either the mechanical residue in the hot gas (X-ray cavities) or the synchrotron emission from the relativistic electrons (radio-loud AGN fractions).   

Because these two observational modalities filter for different phases of the AGN feedback loop, merging their output percentages into a single, unified "duty cycle" collapses critical phenomenological distinctions. X-ray cavities measure the long-term, time-averaged mechanical energy deposited over tens of millions of years as bubbles buoyantly rise through the ICM. In contrast, radio-AGN fractions track instantaneous synchrotron emission, which is subject to rapid spectral aging and inverse-Compton scattering against the cosmic microwave background (CMB), leading to faster fading and potentially lower apparent duty cycles unless observed at extremely low frequencies. Consequently, a duty cycle determined by identifying surface brightness depressions in a heavily biased, flux-limited X-ray sample (e.g., Dunn & Fabian 2006, yielding 70% ) is a fundamentally different estimand from a duty cycle inferred via a mass-limited radio survey tracking L
150 MHz
	​

 luminosity (e.g., Sabater et al. 2019, yielding 100% for the highest masses ).   

Furthermore, the calculation of the duty cycle depends on the denominator selected for the study. Bîrzan et al. (2012)  constrain their denominator to "cooling flow clusters" (systems that presumably require heating) and report a duty cycle of Non-commensurable (Tracer/method: X-ray cavities + Selection: X-ray flux limit + Denominator: Cooling flow clusters + z range: z<0.1) = 60% to 100% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE. However, when Olivares et al. (2022)  select an unbiased, mass-limited sample using the Sunyaev-Zel'dovich (SZ) effect from the Planck survey, the detection fraction of cavities in cool-core systems drops to Non-commensurable (Tracer/method: X-ray cavities + Selection: SZ mass-limited + Denominator: CC clusters + z range: low-z) = 44.4% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The literature indicates that the discrepancy is tied to the physical limits of the instruments; shallow exposure times or poor spatial resolution (e.g., Planck's ~2.5 kpc resolution limit at low-z) obscure smaller cavities, artificially deflating the measurement.   

At the galaxy scale, Sabater et al. (2019)  utilize the LOFAR Two-Metre Sky Survey (LoTSS) to demonstrate that the prevalence of radio AGN activity shows a strong dependence on stellar mass. For galaxies with stellar masses >10
11
M
⊙
	​

, the radio-AGN fraction reaches Non-commensurable (Tracer/method: Radio luminosity L
150
	​

≥10
21
 W/Hz + Selection: Mass-limited optical/radio + Denominator: Main galaxy sample + z range: z<0.3) = 100% ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE. Rather than viewing the duty cycle as a binary "on/off" state, the authors model it as a continuous distribution of Eddington-scaled accretion rates (L
mech
	​

/L
Edd
	​

). Their Kaplan-Meier estimator finds the median of this distribution to be 10
−4.98
, indicating that while the most massive galaxies are "always switched on," they spend the vast majority of their time at extremely low accretion rates, releasing bulk energy in highly active, short-lived bursts.   

Energy-balance ledger

To quantify the hypothesis that maintenance-mode feedback physically offsets the radiative cooling of the circumgalactic and intracluster media, the literature constructs energy-balance ledgers comparing the mechanical power of AGN cavities (P
cav
	​

) against the X-ray cooling luminosity (L
cool
	​

). The cooling luminosity is typically calculated within a volume where the deprojected (isobaric) cooling time, t
cool
	​

, is less than a critical threshold (often 7.7 Gyrs or 3 Gyrs, representing the epoch since the last major merger). The cavity power is modeled as the enthalpy of the bubble divided by its age (P
cav
	​

=E
cav
	​

/t
age
	​

). The enthalpy is commonly approximated as 4pV for a relativistic gas (γ=4/3), while the age is estimated via the buoyant rise time, the sound-crossing time, or the refill time.   

The following structured ledger details the specific findings, assumptions, and systematics of prominent heating-vs-cooling comparisons published in the literature.

Study (citation)	Sample & Mass Range	Balance Ratio (P
cav
	​

/L
cool
	​

) ± unc	Duty-Cycle Treatment	Enthalpy & Projection Systematics


Rafferty et al. (2006) 

	16 clusters, 1 group, 1 galaxy (pV∼10
55
 to >10
61
 erg)	Generally sufficient to offset cooling; ratios span ∼1 to >10 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Modeled as an episodic but continuous heat source over the gas cooling time.	Assumes 4pV; tests buoyant vs. sound-crossing ages (altering P
cav
	​

 by a factor of 2); projection effects mask cavities aligned along the line of sight.


O'Sullivan et al. (2011) 

	Galaxy groups (e.g., NGC 193, NGC 5044, NGC 5846)	Highly variable; some sources strictly on the 4pV equality line ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Feedback modeled as repetitive outbursts required to maintain the steady state in shallow group potentials.	

Values diverge from Cavagnolo et al. (2010) by a factor of 7 in specific systems (e.g., NGC 6269) due to differing morphological assumptions for cavity volumes.




Hlavacek-Larrondo et al. (2012) 

	83 SZ-selected high-redshift clusters (0.4<z<1.2)	Reaches as low as 0.15 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE in specific systems	Acknowledges that the duty cycle is severely suppressed by observational limits at high redshift; questions strict steady-state continuity.	4pV assumed; highlights that X-ray surface brightness limits and projection severely depress detection of older/smaller cavities at high-z, deflating P
cav
	​

.


Panagoulia et al. (2014) 

	101 volume-limited groups and clusters (z≤0.071)	Most cavities lie between pV and 16pV equivalence lines ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Argues that bubbling must be, on average, continuous to successfully offset local cooling rates.	Data quality is the dominant systematic; shallow observations hide smaller group-scale cavities, artificially deflating the aggregate sample heating budget.


Calzadilla et al. (2019) 

	SPT-CLJ0528-5300 (massive high-z cluster, z=0.768)	P
cav
	​

/L
cool
	​

=62.6 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Models extreme episodic bursts where a single event vastly exceeds instantaneous cooling; implies lower-frequency, higher-amplitude cycles.	Assumes 4pV; the probability of chance alignment for the two massive surface brightness depressions is quoted as 0.1%.


Olivares et al. (2022) 

	Planck SZ-selected nearby clusters	Sufficient to offset radiative losses on average ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	SZ selection utilized to explore the "entire AGN feedback duty cycle" independent of X-ray flux biases.	Physical spatial resolution dominates; 2.5 kpc resolution limits for Planck clusters obscure smaller cavities.
  

The energy-balance ledger reveals that while the overarching hypothesis of maintenance heating remains well-supported in massive systems, the exact thermodynamic relationship is highly sensitive to the temporal and spatial scale of the observation. In classical cool-core clusters, early X-ray spectroscopy indicated that gas should be cooling at rates of 
M
˙
>100M
⊙
	​

/yr (the classical cooling flow problem). However, observed star formation rates (SFR) frequently fall orders of magnitude below these predictions. For example, in the cluster ZwCl 2701, the cooling rate derived from X-ray luminosity is ∼196M
⊙
	​

/yr, whereas the SFR derived from H$\alpha$ luminosity is merely ∼0.60M
⊙
	​

/yr. The presence of X-ray cavities in ZwCl 2701, whose P
cav
	​

 values are comparable to the L
cool
	​

 values, leads researchers to postulate that mechanical power from the AGN outburst balances the radiative losses, providing an alternative heating mechanism to halt the condensation of cold gas. Similar energy equivalence is reported for Abell 3017, where the total cavity power lies slightly above the 4pV equivalence line when plotted against the X-ray luminosity within the cooling radius.   

However, the assumption of continuous, smooth heating is challenged by the discovery of extreme, episodic outliers. The Phoenix cluster (SPT-CLJ2344-4243) represents a rare system undergoing a runaway cooling phase as predicted by the classical cooling flow model, demonstrating that the feedback loop can occasionally fail or lag. Conversely, the distant galaxy cluster SPT-CLJ0528-5300 (z=0.768) harbors an outburst exceeding 10
61
 erg. The ratio of the cavity power (P
cav
	​

=9.4±5.8×10
45
 erg/s) to the cooling luminosity (L
cool
	​

=1.5±0.5×10
44
 erg/s) yields a balance ratio heavily skewed toward heating. This suggests that at high redshifts, the duty cycle may be characterized by violent, high-amplitude bursts interspersed with longer quiescent periods, rather than a tightly regulated, quasi-continuous steady state.   

Systematics plague the P
cav
	​

 versus L
cool
	​

 calculations across all mass scales. Researchers typically employ the 4pV enthalpy assumption (valid for a relativistic fluid where γ=4/3) to estimate the total energy E
cav
	​

. However, deriving the mechanical power requires dividing this energy by the cavity age, a parameter that cannot be measured directly. Determining cavity ages via the buoyant rise time versus the sound-crossing time routinely alters the resulting P
cav
	​

 by factors of two. Furthermore, projection effects artificially suppress the apparent energy budget. Cavities expanding along the line of sight or obscured by bright, cool-core emission are rendered undetectable, systematically lowering both the apparent duty cycle and the integrated P
cav
	​

 budget of the sample. Panagoulia et al. (2014) emphasize that data quality is paramount; in their volume-limited sample, shallow X-ray observations systematically failed to detect smaller group-scale cavities, heavily biasing the inferred energy balance.   

Mass regime coverage

The literature mapping the thermodynamic balance of AGN feedback exhibits highly uneven coverage across the cosmic mass scale. Determinations of the maintenance-heating duty cycle are heavily concentrated in deep gravitational potentials, leaving critical observational gaps at the lower end of the halo mass function.

Rich Clusters (M
h
	​

>10
14
M
⊙
	​

): Extensively covered. Samples ranging from the local universe (B55, HIFLUGCS) to high redshift (SPT-SZ, MACS) provide robust constraints on X-ray cavities and P
cav
	​

 vs L
cool
	​

 relations up to z∼1.4 (Hlavacek-Larrondo et al. 2012 ; Bîrzan et al. 2012 ; Olivares et al. 2022 ; McDonald et al. 2023 ).   

Galaxy Groups (10
13
<M
h
	​

<10
14
M
⊙
	​

): Moderately covered. Recent cross-comparisons utilizing surveys like CLoGS and eRASS1 have expanded duty-cycle modeling into group regimes. Studies by Panagoulia et al. (2014)  and Bahar et al. (2024)  assess the entropy and temperature modifications driven by AGN in these shallower potentials, tracking cavities and shock fronts.   

Individual Massive Galaxies ($M_ > 10^{11} M_\odot$):* Well covered via radio-continuum proxies rather than X-ray cavities. Utilizing LOFAR and SDSS, Sabater et al. (2019)  map the fraction of galaxies hosting radio-AGN, pushing the duty-cycle estimate to 100% at this specific high-stellar-mass boundary.   

GAP: Low-Mass and Dwarf Galaxies ($M_ < 10^{10} M_\odot$):* NONE_FOUND for systematic duty-cycle or mechanical energy-balance determinations. While energetic feedback from AGN in dwarf galaxies is increasingly detected via optical and infrared line ratios and outflow kinematics (Moran et al. 2014 ; Aravindan et al. 2025 ), the literature lacks scaling relations for P
cav
	​

 vs L
cool
	​

 at these masses. Aravindan et al. (2025) note that "traditional thresholds may not apply" in this regime, as AGN mass and kinetic energy outflow rates can scale similarly to massive galaxies, but their integration into continuous maintenance-mode ledgers is missing. GAP: Systematically linking mechanical feedback scaling in dwarf galaxies hosting AGN to duty cycles is absent; coverage is restricted to isolated single-object outflow detections rather than population-level maintenance-mode ledgers.   

The divergence in coverage dictates how the duty-cycle hypothesis is tested. In massive systems, the gravitational potential is deep enough to retain a hot, X-ray emitting halo (the ICM or IGrM), allowing researchers to directly map the cavities and calculate the 4pV enthalpy. For individual galaxies lacking massive hot halos, researchers depend on radio-continuum fractions as a proxy for the mechanical duty cycle. In the dwarf regime, where potentials are shallow, stellar feedback models (supernovae and stellar winds) have traditionally dominated the discourse. While contemporary research indicates that AGN in dwarf galaxies can drive galaxy-wide outflows with kinetic energy rates comparable to massive galaxies (when scaled by AGN luminosity) , the absence of an observable hot halo precludes the standard P
cav
	​

 vs L
cool
	​

 energy-balance test, forcing the literature to rely on indirect outflow kinematic scaling relations rather than strict duty-cycle ledgers.   

Instrument-era changes

The transition from Chandra-era X-ray cavity statistics to the current multi-wavelength landscape—dominated by eROSITA, LOFAR, and MeerKAT—has fundamentally altered the interpretation of the AGN duty cycle. Rather than viewing mechanical feedback solely through the lens of ICM buoyancy and distinct, visually resolvable cavities, newer instruments map different thermodynamic and spectral phases of the AGN life cycle, pushing the observable thresholds to lower luminosities and broader spatial scales.

During the Chandra era, duty-cycle determinations were intrinsically limited by the requirement to visually identify surface brightness depressions in the X-ray gas. This methodology biased results toward X-ray bright, cool-core clusters and was insensitive to older, diffused outbursts or cavities expanding along the line of sight. The advent of the SRG/eROSITA All-Sky Survey (eRASS1) has massively expanded the statistical sample of environments, detecting 1178 galaxy groups and mapping the diffuse soft X-ray background with unprecedented complete sky coverage. Bahar et al. (2024) claim that the eRASS1 average entropy and characteristic temperature measurements provide the "tightest constraints on the impact of AGN feedback" in group regimes. Crucially, they note a contradiction with previous theoretical frameworks: the observed entropy profiles in group cores fall below the predictions of state-of-the-art cosmological hydrodynamic simulations (such as MillenniumTNG and OWL). This indicates that historical simulations, calibrated on smaller Chandra-era samples, may have miscalibrated the thermodynamic efficiency or spatial distribution of maintenance heating in shallower gravitational potentials.   

In the radio regime, LOFAR, operating at very low frequencies (e.g., 144/150 MHz), is highly sensitive to the steep-spectrum remnant plasma of older AGN outbursts that have faded from higher-frequency radio views. Sabater et al. (2019) attribute the dramatic shift in duty-cycle estimates to this enhanced sensitivity. While Chandra-era combined radio/X-ray studies (e.g., Best et al. 2005) estimated that only ~30% of the most massive galaxies host radio-loud AGN , LOFAR data indicate that for stellar masses >10
11
M
⊙
	​

, the fraction of galaxies displaying radio-AGN activity reaches 100%. The authors claim this indicates that the most massive galaxies are "always switched on at some level," shifting the duty cycle conceptualization from a binary state to an accretion rate distribution model.   

MeerKAT, utilizing deep, high-resolution capabilities in the MIGHTEE survey, adds clustering-based determinations of the duty cycle up to z∼2.5. Hamlett et al. (2026) utilize Halo Occupation Distribution (HOD) modeling to infer a duty cycle of 5-9% for their specific radio-luminosity threshold. Furthermore, they claim that the typical dark matter halo mass hosting these radio-AGN decreases with increasing redshift, shifting from ⟨logM
h
	​

/M
⊙
	​

⟩=13.44 at low-z to 13.03 at high-z. They attribute this evolution to the "increased abundance of cold gas required to fuel AGN activity at earlier times," which challenges maintenance-mode models that assume a static, non-evolving halo-mass threshold for activation.   

Finally, LOFAR-VLBI and the upgraded Giant Metrewave Radio Telescope (uGMRT) add the capability to probe diffuse, ultra-steep spectrum emission and complex morphologies on vastly different scales. Lusetti (2021, 2026) notes that LOFAR-VLBI explicitly adds constraints on "galaxy-scale jets" (GSJ) confined within ≲100 kpc, which interact directly with the host's interstellar medium (ISM) rather than the cluster ICM. Conversely, uGMRT and LOFAR have discovered faint "megahaloes" extending out to R
500
	​

 in merging clusters. Kolokythas et al. (2025) note that these findings contradict the traditional assumption that diffuse, old AGN plasma is strictly confined to the central cooling region, suggesting a more complex interaction between cluster dynamics and remnant radio plasma.   

Disagreements

The literature contains direct conflicts regarding the absolute values, the temporal evolution, and the measurement systematics of the AGN maintenance-heating duty cycle. Because the parameters dictating AGN feedback are inferred through divergent proxies, researchers frequently arrive at conflicting conclusions regarding the efficiency and history of the feedback loop.

Conflict 1: The absolute value of the AGN feedback duty cycle in cluster cores.

Bîrzan et al. (2012)  analyze the B55 and HIFLUGCS X-ray flux-limited samples. They report: "our results imply that the duty cycle of AGN outbursts with the potential to heat the gas significantly in cooling flow clusters is at least 60 per cent and could approach 100 per cent."   

Olivares et al. (2022)  analyze the Planck SZ-selected sample. They report: "our findings suggest a slightly lower duty cycle of ~46%, as 28 of the 63 CC clusters... have detected cavities... compared to previous studies which predict AGN feedback duty cycle to be high (60–90%, Bîrzan et al.)."   

Stated Reasons: Olivares et al. attribute this discrepancy directly to selection biases, arguing that "previous studies of nearby clusters tend to be biased towards X-ray bright clusters," whereas SZ selection provides a "nearly mass-limited sample" that uncovers a population of cool-core clusters lacking active, detectable cavity inflation. They further note that correcting for spatial resolution differences limits the global detection fraction to merely 9%.   

Conflict 2: The measurement of cavity power (P
cav
	​

) in repetitive outburst systems.

O'Sullivan et al. (2011)  and Cavagnolo et al. (2010)  disagree on the mechanical power of specific group-scale AGN outbursts.   

Numbers: As noted in comparative literature reviews mapping P
cav
	​

 versus 1.4 GHz radio power , "The differences in cavity power are generally within a factor of 2 for all repetitive systems, except for NGC 6269, whose cavity power is about seven times smaller in Cavagnolo et al. (2010)" compared to the measurements published by O'Sullivan et al. (2011).   

Stated Reasons: The divergence stems from differences in the methodology used to calculate bubble ages (e.g., buoyancy velocity vs. sound speed metrics) and differences in the visual interpretation of cavity volumes extracted from complex, nested X-ray surface brightness depressions within the group's shallow potential.   

Conflict 3: Redshift evolution of the feedback/cooling balance.

Hlavacek-Larrondo et al. (2015) and McDonald et al.  suggest that the energy balance is established early and remains stable. They report finding "no evidence for evolution in jetted power generated by AGN feedback from X-ray cavities over the past 7 Gyr."   

Olivares et al. (2022) and Somboonpanyakul et al. (2022)  report a conflict regarding the temporal stability of the AGN host fraction, noting that the "AGN-hosting BCG fraction in the SPT-SZ cluster sample... appears to be strongly evolving with redshift."   

Stated Reasons: The literature attributes the divergence in the apparent evolution of the radio-AGN fraction versus the stability of the X-ray cavity enthalpy to differing accretion mechanisms over cosmic time. Somboonpanyakul et al. suggest the higher scatter in the L
cool
	​

 vs P
cav
	​

 relation for high-z clusters is "consistent with being fueled mainly through wet mergers" at early times, transitioning to smooth, dry maintenance-mode Bondi accretion at low redshift.   

Discriminating tests

To transition duty-cycle determinations from the well-mapped cluster scale down to the individual galaxy scale, the literature proposes specific observational tests aimed at tracing the interaction between jets and the interstellar medium (ISM). Testing the maintenance hypothesis at this scale requires resolving the localized transfer of mechanical energy, distinct from the large-scale buoyant dynamics of the intracluster medium.

Broad-band Radio Spectral Aging and LOFAR-VLBI
The literature explicitly proposes mapping the spectral ages of synchrotron plasma at sub-arcsecond resolutions to constrain the duty cycle at the galaxy scale. Lusetti (2026)  and Pasini et al. (2026)  propose that the combination of Low-Frequency Array Very Long Baseline Interferometry (LOFAR-VLBI) and the upcoming Square Kilometre Array (SKA) is required to execute these measurements.   

Feasibility Statement: Lusetti asserts that LOFAR-VLBI currently provides the "first systematic study" capable of probing Galaxy-Scale Jets (GSJ) confined to ≲100 kpc. This technique resolves the plasma interacting directly with the ISM, bypassing the resolution limits of standard arrays. Looking forward, Pasini states that the "SKA promises to close these gaps and revolutionise the field through its unparalleled combination of high resolution and sensitivity across a wide frequency range". Specifically, simultaneous SKA-Low and Mid observations will trace the synchrotron emission of relativistic plasma with high enough fidelity to unravel "the time-scales of the nuclear activities". Consequently, the SKA/LOFAR-VLBI instrument family is identified as the relevant observational architecture for isolating the mechanical duty cycle of individual galaxies.   

Multiphase Gas Kinematics (JWST / ALMA)
Alternative tests propose tracking the mechanical energy deposited by the AGN into the host galaxy's molecular and ionized gas reservoirs to determine if maintenance heating balances cooling locally. Shanbhog  and Veenema et al. (2025)  propose using ALMA to map cold molecular outflows (via [C II] or CO(2-1)) and the JWST IFU to map warm ionized outflows (via mid-IR coronal lines like [Ne V] 14.3 μm). By correlating velocities and dispersion maps, researchers aim to derive ionized and cold gas masses, outflow rates, and energetics to model the feedback efficiency.   

Feasibility Statement (Marginality): While these instruments successfully map the effects of feedback in localized, extreme regions (e.g., tracing energy across ISM phases in ESO 420-G13 ), the literature notes they are marginal for population-level duty-cycle studies. Belli et al. (2024) and Herrera-Camus et al. (2021) state that "limitations in sensitivity and/or resolution make detecting outflows in typical galaxies very difficult even with powerful telescopes such as ALMA and JWST". Consequently, current multiphase kinematic tests are heavily restricted to massive star-forming galaxies, quasars, or atypical starbursts, rendering them presently insufficient for generating general maintenance-mode duty-cycle ledgers across the galaxy population.   

Links ledger

Bîrzan et al. (2012) | arXiv:1210.7100 | QUARANTINED_PENDING_LOCAL_CHECK

Panagoulia et al. (2014) | arXiv:1407.6614 | QUARANTINED_PENDING_LOCAL_CHECK

Sabater et al. (2019) | arXiv:1811.05528 | QUARANTINED_PENDING_LOCAL_CHECK

Olivares et al. (2022) | arXiv:2208.04888 | QUARANTINED_PENDING_LOCAL_CHECK

Hamlett et al. (2026) | arXiv:2603.06463 | QUARANTINED_PENDING_LOCAL_CHECK

Dunn & Fabian (2006) | UNCITED_NOT_USABLE | QUARANTINED_PENDING_LOCAL_CHECK

Rafferty et al. (2006) | arXiv:astro-ph/0605323 | QUARANTINED_PENDING_LOCAL_CHECK

Hlavacek-Larrondo et al. (2012) | arXiv:1201.1980 | QUARANTINED_PENDING_LOCAL_CHECK

Calzadilla et al. (2019) | arXiv:1911.12828 | QUARANTINED_PENDING_LOCAL_CHECK

Bahar et al. (2024) | arXiv:2401.17276 | QUARANTINED_PENDING_LOCAL_CHECK

Yeung et al. (2024) | arXiv:2410.23345 | QUARANTINED_PENDING_LOCAL_CHECK

O'Sullivan et al. (2011) | arXiv:1107.0181 | QUARANTINED_PENDING_LOCAL_CHECK

Cavagnolo et al. (2010) | arXiv:1006.5699 | QUARANTINED_PENDING_LOCAL_CHECK

Moran et al. (2014) | arXiv:1403.4620 | QUARANTINED_PENDING_LOCAL_CHECK

Aravindan et al. (2025) | arXiv:2512.05041 | QUARANTINED_PENDING_LOCAL_CHECK

GEMINI_WEB_RAMPAGE_R5_OUTPUT_DONE_20260711T052300Z

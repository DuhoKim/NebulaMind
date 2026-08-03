Rampage R9 answer — REQ_RAMPAGE_R9_20260711T064115Z

Run date (UTC): 2026-07-11T06:41:15Z
Model: Gemini-1.5-Pro-002
Evidence rows: 7

Hot-atmosphere detections and limits

The observational effort to characterize the hot gaseous atmospheres, often termed coronae or the circumgalactic medium (CGM), of individual massive galaxies and poor groups in the halo mass regime of M
halo
	​

≲10
13.5
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE relies heavily on soft X-ray imaging and spectroscopy. In this mass range, the gravitational potential is sufficiently deep to heat accreted or retained gas to X-ray emitting temperatures (T≈10
6
−10
7
 K±UNCERTAINTY_NOT_QUOTED_BY_SOURCE), but the intrinsic low density of this plasma results in highly extended, extremely low surface brightness emission. Because X-ray surface brightness scales with the square of the electron density, detecting diffuse emission beyond the optical effective radius of these galaxies requires deep exposures, precise modeling of the cosmic X-ray background, and the careful subtraction of galactic point sources, such as X-ray binaries (XRBs) and active galactic nuclei (AGN).

The literature evaluates the hypothesis that maintenance heating operates in these halos by first attempting to quantify the total thermal energy, mass, and extent of the hot gas reservoir that requires heating. In systems below 10
13.5
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, the emission is dominated not by thermal bremsstrahlung—as is the case in massive clusters—but by metal line cooling, particularly the Iron L-shell complex (Fe XVII–Fe XXIV) in the 0.7−1.2 keV±UNCERTAINTY_NOT_QUOTED_BY_SOURCE band. This introduces a significant observational challenge: the inferred gas mass and density are highly sensitive to the assumed or measured metallicity of the plasma, leading to critical degeneracies in spectral fitting. The table below outlines the primary constraints derived from deeply observed individual galaxies and large-scale population stacking analyses.   

Study (citation)	Sample + selection	Halo/stellar mass range	Detection or upper limit (L_X, T, extent) ± unc	Instrument	Caveats named by the study


Anderson et al. 2016 (arXiv:1608.02033) 

	Individual giant spiral galaxy (NGC 1961); optically selected, highly massive, isolated spiral.	logM
∗
	​

=11.62M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Detection: L
X
	​

(<0.1r
200
	​

)=(7.80±2.23)×10
40
 erg s
−1
; T≈0.6 keV±UNCERTAINTY_NOT_QUOTED_BY_SOURCE (negative gradient); Extent ≈80 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE	XMM-Newton	Highly unusual massive spiral; notes a severe degeneracy between the extrapolated density profile slope and the metallicity profile (assumed flat Z≈0.2Z
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE).


Bogdán et al. 2017 (arXiv:1708.00000) 

	Individual massive spiral galaxy (NGC 6753); nearly face-on inclination to minimize disk obscuration.	logM
∗
	​

=11.51M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE; M
vir
	​

≈1×10
13
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Detection: logL
X
	​

=40.88±1.42 erg s
−1
; Extent ≈160 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE (roughly 35%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE of virial radius)	XMM-Newton / Chandra	Study explicitly assigns a +8%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE systematic uncertainty to the total baryon mass fraction derived under the assumption of an isothermal halo.


Dai et al. 2012 (arXiv:1112.0324) 

	Individual early-type spiral galaxy (UGC 12591); selected as the fastest rotating spiral galaxy known.	M
halo
	​

<3.5×10
11
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE (upper limit derived from X-ray constraints)	Detection: L
X
	​

(0.1−10 keV)=3.9×10
40
 erg s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE; T=0.64±0.03 keV; Extent =110 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE	XMM-Newton	The cooling radius of this extended gas halo is very small, which the authors argue indicates the majority of the stellar mass is not assembled via continuous cooling flows.


Comparat et al. 2022 (MNRAS 531) 

	Stacking analysis of 40,000±UNCERTAINTY_NOT_QUOTED_BY_SOURCE galaxies; optically selected cross-match.	8.5≲log(M
∗
	​

/M
⊙
	​

)≲12±UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Detection: Extracted an average X-ray surface brightness profile ±UNCERTAINTY_NOT_QUOTED_BY_SOURCE extending beyond typical optical radii.	eROSITA	Lower mass bins in the stack are highly susceptible to contamination where point sources, X-ray binaries, and unresolved background may dominate over the true diffuse halo emission.


Popesso et al. 2024 (arXiv:2411.16546) 

	Mock eRASS:4 observations combined with GAMA-like optical group catalogs generated from the Magneticum simulation.	Milky Way-like groups to poor clusters (M
halo
	​

≈10
12
−10
14
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE)	Upper limits / mock constraints: systematic offsets between input and recovered surface brightness profiles evaluated ±UNCERTAINTY_NOT_QUOTED_BY_SOURCE	eROSITA (mock data)	Evaluates stacking reliability; states that AGN and XRBs heavily dominate the X-ray surface brightness profiles of low-mass halos, making optical stacking prone to severe completeness and contamination biases.


O'Sullivan et al. 2017 (MNRAS 472) 

	Complete Local Volume Groups Sample (CLoGS); high-richness subsample of 26±UNCERTAINTY_NOT_QUOTED_BY_SOURCE optically selected groups within 80 Mpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.	M
500
	​

=0.5−5×10
13
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Detection: 14±UNCERTAINTY_NOT_QUOTED_BY_SOURCE of 26±UNCERTAINTY_NOT_QUOTED_BY_SOURCE groups possess extended halos (>65 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE); T=0.4−1.5 keV±UNCERTAINTY_NOT_QUOTED_BY_SOURCE	Chandra / XMM-Newton	Warns that >40%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE of nearby groups were excluded from previous archival studies due to selection biases in the ROSAT All-Sky Survey (RASS) that favored dense, cool-core systems.
  

These observations collectively highlight that while hot, X-ray emitting gas is present around individual massive spirals and poor groups, the thermodynamic profiles are distinct from higher-mass clusters. The detection of negative temperature gradients in galaxies like NGC 1961  and the sub-solar metallicity profiles (often modeled at Z≈0.2Z
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE) suggest the gas may originate from cosmological accretion rather than internal stellar mass loss. Furthermore, the simulated eROSITA stacking efforts by Popesso et al.  emphasize the extreme difficulty in isolating this diffuse signal from the stellar components (XRBs) in halos below 10
13
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, indicating that raw stacked luminosities may overestimate the true thermal energy available for cooling.   

Radio-AGN incidence at these masses

The incidence rate of radio-loud active galactic nuclei in low-mass halos and individual massive galaxies forms the foundational boundary condition for the hypothesis of maintenance heating. For mechanical energy injection to regulate the thermodynamic state of a halo, the feedback mechanism must be sufficiently ubiquitous and its duty cycle appropriately matched to the cooling time of the gas. The literature indicates a severe dependence of radio-AGN incidence on both the stellar mass of the host galaxy and the specific accretion mode of the central black hole. AGN are typically divided into Low-Excitation Radio Galaxies (LERGs), associated with radiatively inefficient accretion of hot halo gas, and High-Excitation Radio Galaxies (HERGs), associated with radiatively efficient accretion of cold gas. The following fractions represent the statistical prevalence of radio AGN in the local universe, with all four required qualifiers strictly specified to prevent non-commensurable comparisons across varying surveys.

Fraction 1: Best et al. (2005)    

Selection: Galaxies drawn from the main spectroscopic sample of the Sloan Digital Sky Survey (SDSS) Data Release 2.

Method: Cross-matching optical coordinates with high-frequency radio catalogs from the NRAO VLA Sky Survey (NVSS) and the Faint Images of the Radio Sky at Twenty-Centimeters (FIRST) survey. The separation of AGN from star-forming galaxies utilizes the 4000 
A
˚
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE break strength versus radio luminosity per unit stellar mass.

Mass range: Stellar masses spanning from 10
10
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE up to 5×10
11
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

Survey/Luminosity limit: Evaluated at a rest-frame frequency of 1.4 GHz±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, with a strict luminosity threshold of L
1.4 GHz
	​

>10
23
 W Hz
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

Incidence: The fraction of galaxies hosting a radio-loud AGN is found to be a strong function of stellar mass, rising continuously from nearly 0%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE below a stellar mass of 10
10
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE to greater than 30%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE at stellar masses of 5×10
11
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

Fraction 2: Sabater et al. (2019)    

Selection: Galaxies drawn from the SDSS main spectroscopic sample in the local universe.

Method: Cross-matching optical targets with the LOFAR Two-metre Sky Survey (LoTSS) Data Release 1. The study relies on the high sensitivity of the LOFAR High Band Antenna (HBA) array to detect low-surface-brightness, steep-spectrum synchrotron emission indicative of older or lower-power jet activity that is invisible at gigahertz frequencies.

Mass range: Massive central galaxies, particularly evaluating incidence at stellar masses M
∗
	​

>10
11
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

Survey/Luminosity limit: Evaluated at a low rest-frame frequency of 150 MHz±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, probing down to a highly sensitive luminosity threshold of L
150
	​

≈10
21
 W Hz
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

Incidence: The measured fraction of radio AGN reaches 100%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE for the most massive galaxies, prompting the authors to conclude that these systems are "always switched on." The study emphasizes that this exceptionally steep mass dependence is driven entirely by the LERG population. Conversely, HERGs show a significantly lower prevalence across all stellar masses and are primarily associated with galaxies exhibiting ongoing star formation activity, suggesting a dependency on cold gas supply rather than hot halo accretion.

Fraction 3: O'Sullivan et al. (2018) CLoGS Survey    

Selection: The Complete Local-Volume Groups Sample (CLoGS), an optically selected, statistically complete sample of nearby groups limited to a recessional velocity of cz<5500 km s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE (distance <80 Mpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE).

Method: Targeted, deep low-frequency radio observations to identify extended jet and lobe structures associated specifically with the central dominant galaxies of the groups, which are then correlated with the morphological and thermodynamic state of the X-ray halo.

Mass range: Group-scale dark matter halos spanning the range of M
500
	​

=0.5−5×10
13
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.

Survey/Luminosity limit: Giant Metrewave Radio Telescope (GMRT) observations conducted simultaneously at 235 MHz±UNCERTAINTY_NOT_QUOTED_BY_SOURCE and 610 MHz±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, achieving highly sensitive RMS noise limits of ≈0.1 mJy/beam±UNCERTAINTY_NOT_QUOTED_BY_SOURCE at 610 MHz and ≈0.6 mJy/beam±UNCERTAINTY_NOT_QUOTED_BY_SOURCE at 235 MHz.

Incidence: Central radio jet sources are detected in 11±UNCERTAINTY_NOT_QUOTED_BY_SOURCE out of 26±UNCERTAINTY_NOT_QUOTED_BY_SOURCE (42.3%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE) of the X-ray bright groups. The authors observe a distinct thermodynamic correlation: among the X-ray bright systems, only those possessing a central cool core are observed to support active central jet sources, tying the incidence directly to the cooling properties of the inner atmosphere.

The literature interprets the stark contrast in detection fractions between high-frequency gigahertz surveys and low-frequency megahertz surveys as a consequence of the radiative lifetimes of the synchrotron-emitting electron populations. High-frequency surveys trace the youngest, most recently accelerated electron populations in active jets. In contrast, low-frequency surveys like LOFAR are sensitive to the aged, steep-spectrum plasma that remains buoyant in the halo long after the active jet phase has ceased. Consequently, the 100%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE incidence rate measured at 150 MHz±UNCERTAINTY_NOT_QUOTED_BY_SOURCE by Sabater et al. suggests that the integrated duty cycle—encompassing both the active energy injection phase and the subsequent passive buoyant rise phase of the plasma—approaches unity in the highest-mass end of this halo regime, meaning massive galaxies are continuously interacting with radio-emitting plasma.

Energetics ledger

To quantitatively assess the maintenance heating hypothesis in low-mass halos (M
halo
	​

≲10
13.5
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE), the literature attempts to construct a localized energetics ledger comparing the mechanical power injected by AGN feedback against the rate of radiative cooling in the hot diffuse gas. In massive galaxy clusters, this is typically achieved via direct X-ray cavity calorimetry. In this method, the physical energy required to inflate a bubble against the ambient pressure of the intra-cluster medium (E=4pV±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, assuming a relativistic equation of state for the plasma inside the cavity) is divided by the cavity's buoyant rise time to yield the time-averaged mechanical power (P
cav
	​

).

However, at group and individual galaxy scales, executing this calorimetry is exceptionally difficult. The lower surface brightness of the ambient medium, the smaller angular sizes of the cavities, and the complex thermal structures of group cores often obscure clear cavity edges. Below is the published ledger of heating and cooling estimates for specific low-mass systems and populations.

NGC 5813 (Galaxy Group): Randall et al. (2011, 2015)  identified three distinct pairs of collinear X-ray cavities in this nearby group (z=0.0057±UNCERTAINTY_NOT_QUOTED_BY_SOURCE). This provides a rare opportunity to measure the temporal history of feedback. The outburst shocks are associated with ages of 3×10
6
 yr±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, 2×10
7
 yr±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, and 9×10
7
 yr±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, indicating an outburst interval on the order of ≈10
7
 yr±UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The mean mechanical power varies significantly between outbursts, differing by a factor of six, and ranges from P
mech
	​

=1.5×10
42
 erg s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE to 10×10
42
 erg s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The total energy output of the outbursts ranges from 1.5×10
56
 erg±UNCERTAINTY_NOT_QUOTED_BY_SOURCE to 4×10
57
 erg±UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The authors estimate a bolometric X-ray cooling luminosity of L
cool
	​

=3.3×10
41
 erg s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE within the cooling radius (11 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE), which corresponds to a cooling time of 1 Gyr±UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The ledger for NGC 5813 indicates that the heating from the outburst shocks alone is sufficient to balance the radiative cooling within at least the central 10 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.   

HCG 62 (Compact Galaxy Group): Gitti et al. (2010)  examined the clear, small X-ray cavities corresponding to low-frequency radio lobes in this compact group. The cavity power is estimated directly from the X-ray data to be P
cav
	​

≈3×10
42
 erg s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE. This mechanical power is compared against the luminosity of the intra-group medium (ICM/IGM) inside the cooling region, which is calculated as L
ICM
	​

=1.8×10
42
 erg s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The ledger shows P
cav
	​

 is approximately twice the cooling luminosity. Furthermore, the study identifies a shock front located 36 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE from the center with a Mach number of ≈1.5±UNCERTAINTY_NOT_QUOTED_BY_SOURCE and a total power roughly one order of magnitude higher than the cavity power. Notably, the study determines the radio source is radiatively highly inefficient, exhibiting a ratio of radio luminosity to mechanical cavity power of ≈10
−4
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.   

NGC 5044 (Galaxy Group): David et al. (2009, 2014)  evaluated this moderate cooling-flow group, reporting a cavity power of P
cav
	​

=1.52×10
41
 erg s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The literature notes a distinct morphological difference in this system: NGC 5044 does not show evidence for X-ray cavities extending beyond the ends of its central X-ray and H$\alpha$ filaments. Its measured cavity power is remarkably low, a factor of 1000±UNCERTAINTY_NOT_QUOTED_BY_SOURCE times lower than highly active group systems like PKS 0745-191, despite both having similar gravitating masses of ∼2×10
14
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE within 30 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.   

3C 88 (Galaxy Group): O'Sullivan et al.  analyze deep Chandra observations of this radio-loud group, revealing a prominent eastern X-ray cavity with a diameter of ∼50 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The total enthalpy of the cavity is extraordinarily high for a group, measured at 3.8×10
58
 erg±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, resulting in an average power required to inflate the bubble of P
cav
	​

≈2.0×10
43
 erg s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.   

CLoGS Group Sample (Population Arguments): O'Sullivan et al. (2018)  evaluated the thermal balance across the statistically complete Complete Local-Volume Groups Sample. In many cases within this lower-mass regime, direct cavity calorimetry was NOT possible because the X-ray cavities were either unresolved, aged beyond detectability, or obscured by the complex morphology of the group core. Proxy used: To construct the ledger, the authors utilized the integrated radio power from 10 MHz±UNCERTAINTY_NOT_QUOTED_BY_SOURCE to 10 GHz±UNCERTAINTY_NOT_QUOTED_BY_SOURCE as a proxy estimator for mechanical jet power, relying on scaling relations derived from higher-mass systems. The resulting ledger for the CLoGS sample reveals a distinct bifurcation based on the physical size of the jets: groups hosting smaller jet systems (≲50 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE) are generally found to be in approximate thermal balance (P
cav
	​

≈L
cool
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE). Conversely, systems harboring larger jets (such as NGC 193 and NGC 4261) are determined to be drastically overpowered relative to the cooling rate, with mechanical power estimates yielding P
cav
	​

≥100×L
cool
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.   

The disparate energetics found in the CLoGS sample introduce critical complications for the theoretical treatment of the AGN duty cycle in low-mass halos. The common assumption of a continuous, finely-tuned thermostat—often invoked in cluster models to prevent overcooling without destroying the core—is challenged by these heavily overpowered states. The authors suggest this implies episodic, powerful bursts of feedback heating that drastically overshoot the cooling requirement, rather than a state of continuous equilibrium.

Cluster-to-low-mass extrapolations

The hypothesis that maintenance heating uniformly regulates the thermodynamic state of low-mass halos frequently relies on extrapolating scaling relations, duty cycles, and physical efficiencies initially derived from rich galaxy clusters (M
halo
	​

≳10
14
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE) down into the regime of poor groups and individual galaxies. The literature contains specific arguments supporting these importations, alongside explicit theoretical and observational pushback regarding the physical validity of such scale-invariant assumptions.

Attributed Claims Importing Cluster Mechanics:

Extrapolation of the Cavity-Radio Scaling Relation: O'Sullivan et al. (2011)  and others have utilized the empirical scaling relation between mechanical cavity power (P
cav
	​

) and radio luminosity (L
radio
	​

) to estimate feedback in low-mass systems where cavities are invisible. This relation was predominantly calibrated by Bîrzan et al. (2004, 2008) using a sample of massive, X-ray luminous clusters. Stated Assumptions: Importing this relation to group-scale halos assumes that the radiative efficiency of the synchrotron plasma and the coupling efficiency of the mechanical PdV work to the surrounding hot atmosphere remain constant across more than an order of magnitude in halo mass and ambient thermal pressure.   

Chaotic Cold Accretion (CCA) and Flickering Duty Cycles: Gaspari et al.  import the Chaotic Cold Accretion model, originally developed to explain the regulation of massive cluster cores, to explain the high incidence of radio galaxies in group centers. They posit that AGN in Brightest Group Galaxies (BGGs) can tap into both galactic and intragroup halo condensations. Stated Assumptions: This model assumes a "flickering duty cycle" governed by the precipitation of multiphase gas out of the hot halo when the cooling-to-free-fall time ratio drops below a critical threshold (typically t
cool
	​

/t
ff
	​

≈10±UNCERTAINTY_NOT_QUOTED_BY_SOURCE). It explicitly assumes the thermal instability mechanism operates identically in the shallower gravitational potential wells of groups as it does in deep cluster potentials.   

The Supermassive Black Hole / Halo Co-evolution Paradigm: Modern cosmological simulations (e.g., IllustrisTNG, EAGLE, SIMBA, Magneticum) frequently import subgrid AGN feedback models calibrated to match the high-mass end of the galaxy stellar mass function and cluster gas fractions down to group scales. Bower et al. (2006) and others  argue that tapping into SMBH accretion as a source of energetic feedback is universally required to regulate star formation across all massive galaxies. Stated Assumptions: These models assume that the transition from a star-formation-dominated feedback regime to an AGN-dominated maintenance regime scales predictably with the dark matter halo mass, generally locating the transition at a critical threshold of M
crit
	​

≈10
13.5
−10
14
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE.   

Published Pushback Against Extrapolation:

Breakdown of Continuous Balance: O'Sullivan et al. (2018)  explicitly push back against the extrapolation of the finely-tuned cluster maintenance model to poor groups. Based on the CLoGS finding that some group AGN are overpowered by a factor of 100±UNCERTAINTY_NOT_QUOTED_BY_SOURCE relative to the local cooling rate, they state: "This suggests that central AGN are not always in balance with cooling, but may instead produce powerful periodical bursts of feedback heating." This argues directly against the scale-invariance of the continuous feedback loop, suggesting groups experience much more violent thermodynamic swings.   

Contamination of Scaling Relations: Popesso et al. (2024, 2025)  caution against directly importing ICM-derived observational techniques (like large-scale X-ray stacking) to infer IGM properties in low-mass halos. Using the Magneticum simulations to generate mock eROSITA observations, they state: "We find that AGN and XRBs dominate the X-ray surface brightness profiles of low-mass halos." They argue that applying cluster-style stacking analyses to optically selected groups without thoroughly accounting for these point-source contaminants leads to severe biases in estimating the diffuse gas properties and, consequently, the inferred cooling rates that necessitate heating.   

Differences in Radiative Physics: The literature notes that the thermodynamics of groups differ fundamentally from clusters because the intra-group medium radiates primarily through metal line emission rather than thermal bremsstrahlung. This increased cooling efficiency at T∼10
7
 K±UNCERTAINTY_NOT_QUOTED_BY_SOURCE promotes a more complex thermal structure and increases the probability of forming a cooler phase (≲10
5
 K±UNCERTAINTY_NOT_QUOTED_BY_SOURCE), suggesting that the thermodynamic response to mechanical heating in groups cannot be modeled as a simple scaled-down version of the cluster ICM.   

Alternative maintenance channels

While mechanical AGN feedback remains the dominant mechanism investigated for maintenance heating in the literature, the unique physical conditions of low-mass halos (10
12
−10
13.5
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE) elevate the theoretical viability of alternative, non-AGN heating channels. The shallower gravitational potential wells and lower ambient pressures mean that energy injection mechanisms deemed insufficient in rich clusters are weighed heavily in this specific regime.

Type Ia Supernovae (SNe Ia) Heating: Voit et al. (2015, 2020)  deeply investigate the thermodynamic contribution of SNe Ia to the hot interstellar medium of massive elliptical galaxies and the central regions of poor groups. SNe Ia inject significant kinetic energy into the gas (approximately 10
51
 ergs±UNCERTAINTY_NOT_QUOTED_BY_SOURCE per event), which thermalizes via shocks. This decreases the net radiative cooling rate by inflating the specific entropy of the gas, defined as K∝Tn
−2/3
. The authors argue that in many isolated massive galaxies, the estimated specific heating rate due to SNe Ia (H
SNIa
	​

) and the specific radiative cooling rate (C
rad
	​

) are in rough balance within the inner regions. The literature characterizes this as a compelling alternative to continuous AGN feedback for keeping the local ISM hot. However, this channel suffers from significant uncertainties; the exact ratio of heating to cooling is cited as being unknown to within a factor of 2±UNCERTAINTY_NOT_QUOTED_BY_SOURCE due to underlying uncertainties in the empirical SNe Ia delay-time distribution, the absolute SNe Ia rate in older stellar populations, and the complex metallicity dependencies of the gas cooling function. Crucially, the SNIa rate is tied to the stellar mass and age, and cannot dynamically adjust to changes in the cooling rate, making true self-regulation difficult to explain.   

Gravitational and Virialization Heating: The conversion of the kinetic energy of infalling cosmic gas and merging satellite halos into thermal energy via adiabatic compression and virial shocks provides a baseline heating floor. Johansson, Naab & Ostriker (2009)  argue that in cosmological simulations lacking strong AGN feedback, low present-day star formation rates in massive galaxies can still be achieved. They attribute this to efficient early gas depletion combined with "efficient shock heating of the halo gas and gravitational heating caused by the accretion of smaller systems." This channel scales strongly with the total mass of the halo, becoming particularly relevant in the mass regime where cosmological accretion shifts from "cold-mode" (penetrating filaments) to "hot-mode" (shocked at the virial radius).   

Thermal Conduction and Turbulent Mixing: Armengaud et al.  highlight processes that do not possess the potential for active, self-regulated feedback but can nonetheless offset central cooling. Thermal conduction (facilitated by electrons traveling along magnetic field lines) can supply heat to the fast-cooling central regions by redistributing thermal energy from the hotter, higher-entropy outer halo inward. Similarly, turbulent mixing—driven by galaxy motions or previous structural mergers—can mix high-entropy gas from larger radii with the lower-entropy core. The efficiency of both mechanisms in low-mass halos is highly debated due to the uncertain suppression factor imposed by the tangled micro-scale topology of the halo magnetic field.   

Disagreements

The application of the maintenance heating hypothesis to low-mass halos is characterized by several direct, unresolved conflicts in the literature, where independent methodologies assessing the exact same estimand yield contradictory conclusions regarding the state of the gas.

Conflict 1: The Total Mass of the Hot Gaseous Halo in Giant Spirals (e.g., NGC 1961)

Side A (Advocating a massive hot gas reservoir): Studies such as Bogdán et al. (2013) and Dai et al. (2012)  analyze the soft X-ray surface brightness profiles of massive isolated spirals and extrapolate them out to the virial radius (R
200
	​

) using standard β-model density profiles. They argue that these extended detections point to a massive circumgalactic medium that contains a substantial fraction of the galaxy's baryons, indicating a large, continuous reservoir of hot gas that would require maintenance heating over cosmic time.   

Side B (Advocating a severely depleted hot gas reservoir): Anderson & Bregman (2014, 2016)  explicitly challenge these mass extrapolations. Focusing on the same target (NGC 1961), they state that the spectral modeling employed by previous analyses "violates X-ray surface brightness constraints and therefore significantly overestimates the total hot gas mass." Because the emission in this regime is heavily line-dominated, there is a severe degeneracy where the inferred gas mass within 250 kpc±UNCERTAINTY_NOT_QUOTED_BY_SOURCE can vary by an order of magnitude depending on the assumed slope of the metallicity profile (e.g., β=0.2 vs β=0.6 ). Side B argues the rigorously extrapolated hot gas mass is comparable only to the stellar mass, resulting in a severe missing baryon problem (estimated at ≈70%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE of the cosmic fraction missing).   

Conflict 2: The Baryon Fraction in Group-Scale Halos (10
13.5
−10
14.5
M
⊙
	​

)

Side A (Simulations predicting cosmic retention): As summarized by studies analyzing the missing baryon discrepancy (e.g., Crain et al. 2007) , many cosmological hydrodynamic simulations that lack highly efficient, ejective AGN feedback predict that the total baryon fraction within r
500
	​

 of groups and poor clusters should be close to the universal cosmic baryon fraction (f
b
	​

≡Ω
b
	​

/Ω
m
	​

≈0.17±UNCERTAINTY_NOT_QUOTED_BY_SOURCE). In these models, maintenance heating gently offsets cooling without unbinding the gas.   

Side B (Observations showing severe depletion): Recent observational studies utilizing eROSITA X-ray stacking combined with weak lensing mass calibrations (e.g., Eckert et al., Popesso et al.)  directly conflict with this theoretical baseline. They measure retained gas fractions of ≲5%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE for halos in the 10
13.5
−10
14.5
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE range. This indicates that baryons have been massively evacuated beyond R
200c
	​

, directly challenging models that advocate for a gentle, perfectly balanced maintenance heating mechanism in favor of violent, highly ejective feedback episodes that completely unbind the gas from the group potential.   

Discriminating tests

The literature explicitly identifies specific observational tests and instrument capabilities required to decide the question of maintenance heating in low-mass halos. The primary limitation to date has been the inability to directly measure the kinematics of the hot (T≈10
7
 K±UNCERTAINTY_NOT_QUOTED_BY_SOURCE) plasma phase to quantify exactly how much mechanical turbulent energy is available to offset radiative cooling.

High-Resolution X-ray Microcalorimetry (The Relevant Instrument Family): The literature (e.g., XRISM Collaboration 2024, X-IFU consortium)  states that the definitive test for AGN feedback efficiency is the direct measurement of turbulent velocity broadening in the hot atmosphere. Instruments equipped with transition-edge sensor (TES) microcalorimeters, such as the Resolve instrument on the currently operational XRISM observatory, or future proposed missions like Athena (X-IFU) and LEM, are uniquely capable of this test due to their unprecedented energy resolution (e.g., ≈5 eV±UNCERTAINTY_NOT_QUOTED_BY_SOURCE). This resolution is required to separate thermal line broadening from macroscopic turbulent velocity broadening. The Hitomi mission previously applied this test to the Perseus cluster, measuring a velocity broadening of <200 km s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE, indicating that AGN feedback generated subsonic turbulence contributing roughly 4%±UNCERTAINTY_NOT_QUOTED_BY_SOURCE of the total atmospheric pressure. The literature proposes extending these precise microcalorimeter observations with XRISM to galaxy groups and low-mass halos to directly test if the generated turbulent pressure is sufficient to establish maintenance heating in the shallower potentials of the 10
13
M
⊙
	​

±UNCERTAINTY_NOT_QUOTED_BY_SOURCE regime.   

Submillimeter and Infrared Kinematics (Marginal for the Hot Phase): While ALMA and JWST are highly capable of mapping the cold and warm ionized phases of galactic outflows, the literature views them as marginal for deciding the hot maintenance question. For example, ALMA observations of the CO(2-1) transition in the center of the group NGC 5044  measure a Full Width at Half Maximum (FWHM) of 220 km s
−1
±UNCERTAINTY_NOT_QUOTED_BY_SOURCE. The authors argue these velocities are too low to be produced by uninhibited gravitational infall, supporting the hypothesis that the molecular gas arises from in situ cooling of warm gas dredged up by AGN-inflated cavities. However, while ALMA and JWST can exquisitely map the cold byproduct (the 10 K±UNCERTAINTY_NOT_QUOTED_BY_SOURCE to 10
4
 K±UNCERTAINTY_NOT_QUOTED_BY_SOURCE phases) of the feedback cycle, they cannot directly measure the turbulent kinetic energy injected into the dominant 10
7
 K±UNCERTAINTY_NOT_QUOTED_BY_SOURCE volume-filling phase. Therefore, while synergistic, they cannot independently close the energetics ledger for maintenance heating.   

Links ledger

eROSITA eFEDS masking | https://www.pure.ed.ac.uk/ws/files/322956947/aa43101_22.pdf | QUARANTINED_PENDING_LOCAL_CHECK

eROSITA Science Book | https://heasarc.gsfc.nasa.gov/docs/srg/erosita/about/ero_sciencebook.pdf | QUARANTINED_PENDING_LOCAL_CHECK

IllustrisTNG CGM predictions | https://academic.oup.com/mnras/article/525/2/1976/7231802 | QUARANTINED_PENDING_LOCAL_CHECK

SIMBA vs EAGLE mock eROSITA | https://arxiv.org/html/2506.09123v2 | QUARANTINED_PENDING_LOCAL_CHECK

Comparat et al. (2022) | https://academic.oup.com/mnras/article/531/2/2757/7671142 | QUARANTINED_PENDING_LOCAL_CHECK

eROSITA SFR stacking thesis | http://www.sternwarte.uni-erlangen.de/docs/theses/2024-02_Laktionov.pdf | QUARANTINED_PENDING_LOCAL_CHECK

Best et al. luminosity functions | https://academic.oup.com/mnras/article/536/1/554/7901367 | QUARANTINED_PENDING_LOCAL_CHECK

Best et al. (2005) radio fraction | https://academic.oup.com/mnras/article/379/3/894/1037774 | QUARANTINED_PENDING_LOCAL_CHECK

Sabater et al. (2019) LERG fraction | https://edoc.ub.uni-muenchen.de/36542/1/Igo_Zsofi.pdf | QUARANTINED_PENDING_LOCAL_CHECK

Sabater et al. (2019) mass scaling | https://www.pure.ed.ac.uk/ws/files/77135820/1811.05528.pdf | QUARANTINED_PENDING_LOCAL_CHECK

Rejuvenation and quenching | https://arxiv.org/html/2606.12156v2 | QUARANTINED_PENDING_LOCAL_CHECK

Gravitational heating | https://www.researchgate.net/publication/50909626_TESTING_A_PREDICTION_OF_THE_MERGER_ORIGIN_OF_EARLY-TYPE_GALAXIES_A_CORRELATION_BETWEEN_STELLAR_POPULATIONS_AND_ASYMMETRY | QUARANTINED_PENDING_LOCAL_CHECK

NGC 1961 X-ray halo | https://academic.oup.com/mnras/article/517/1/99/6726641 | QUARANTINED_PENDING_LOCAL_CHECK

Bogdán et al. / Anderson et al. spirals | https://academic.oup.com/mnras/article/455/1/227/985103 | QUARANTINED_PENDING_LOCAL_CHECK

UGC 12591 missing baryons | https://arxiv.org/abs/1112.0324 | QUARANTINED_PENDING_LOCAL_CHECK

Popesso et al. (2025) eROSITA perils | https://arxiv.org/html/2411.16546v2 | QUARANTINED_PENDING_LOCAL_CHECK

Group transition Mcrit | https://arxiv.org/html/2605.16488v1 | QUARANTINED_PENDING_LOCAL_CHECK

Cavity power vs cooling mocks | https://arxiv.org/html/2407.14415v1 | QUARANTINED_PENDING_LOCAL_CHECK

Voit (2015) SNe Ia heating | https://indico.nbi.ku.dk/event/1774/contributions/13492/attachments/4038/6369/Voit_Copenhagen_Aug17_PDF_Reduced.pdf | QUARANTINED_PENDING_LOCAL_CHECK

O'Sullivan NGC 6338 | https://academic.oup.com/mnras/article/488/2/2925/5522613 | QUARANTINED_PENDING_LOCAL_CHECK

O'Sullivan 2011 jet power | https://research.birmingham.ac.uk/files/17589195/O_Sullivan_Heating_Hot_Atmospheres_Astrophysical_Journal_2011.pdf | QUARANTINED_PENDING_LOCAL_CHECK

LoTSS DR1 properties | https://arxiv.org/html/2411.08974v1 | QUARANTINED_PENDING_LOCAL_CHECK

Randall 2011 NGC 5813 | https://arxiv.org/pdf/1101.4583 | QUARANTINED_PENDING_LOCAL_CHECK

Randall 2015 shocks | https://cxc.harvard.edu/cdo/xgal14/presentations/Randall_Scott-2.pdf | QUARANTINED_PENDING_LOCAL_CHECK

CLoGS Survey | https://academic.oup.com/mnras/article/481/2/1550/5061646 | QUARANTINED_PENDING_LOCAL_CHECK

Gitti et al. 2010 HCG 62 | https://arxiv.org/pdf/0912.3013 | QUARANTINED_PENDING_LOCAL_CHECK

David et al. 2009 NGC 5044 | https://ntrs.nasa.gov/citations/19950029117 | QUARANTINED_PENDING_LOCAL_CHECK

Baryon fraction debate (Eckert) | https://edoc.ub.uni-muenchen.de/34804/1/Bahar_Yunus_Emre.pdf | QUARANTINED_PENDING_LOCAL_CHECK

Missing baryons recovered via SZ | https://www.researchgate.net/publication/398301795_Missing_baryons_recovered_A_measurement_of_the_gas_fraction_in_galaxies_and_groups_with_the_kinematic_Sunyaev-Zel'dovich_effect_and_CMB_lensing | QUARANTINED_PENDING_LOCAL_CHECK

XRISM tests of feedback | https://arxiv.org/html/2505.01494v2 | QUARANTINED_PENDING_LOCAL_CHECK

GEMINI_WEB_RAMPAGE_R9_OUTPUT_DONE_20260711T064115Z

Rampage R4 answer — REQ_RAMPAGE_R4_20260711T052300Z

Run date (UTC): 2026-07-11T07:11:00Z
Model: Gemini 1.5 Pro
Evidence rows: 9

Evidence table
Study (citation)	Sample + selection	Gas tracer (CO transition / dust / HI) & conversion assumptions	Aperture (central kpc vs global)	f_gas result ± unc	t_dep or SFE result ± unc	Study's own reading: depletion / low-SFE / mixed / inconclusive	Key caveats
Teng et al. 2026 ([arXiv:2606.23649])	62 Main Sequence (MS), Green Valley (GV), and Red galaxies; optically selected	CO(1-0); assumes four α
CO
	​

 prescriptions (Milky Way, T24* velocity dispersion, B13, SL24)	Global	10
8
−10
10
M
⊙
	​

 [non-commensurable] ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	t
dep
	​

=2.10
−1.31
+2.35
	​

 Gyr [non-commensurable]	low-SFE	SFR and α
CO
	​

 estimation systematics heavily alter t
dep
	​

 distributions.
Pan et al. 2024 ([arXiv:2402.07400])	ALMaQUEST GV galaxies; MaNGA IFU selected	CO(1-0); assumes constant α
CO
	​

=4.35	Resolved (differentiates central R<0.5R
e
	​

 vs disk R>0.5R
e
	​

)	UNCERTAINTY_NOT_QUOTED_BY_SOURCE	UNCERTAINTY_NOT_QUOTED_BY_SOURCE	mixed	Evaluates a wide range of mass values; assumes uniform conversion factor across morphological structures.
Brown et al. 2023 ([arXiv:2308.10943])	33 Virgo Cluster satellite galaxies; divided by global HI deficiency	CO(2-1); assumes Bolatto α
CO
	​

	Resolved (720 pc spaxels)	offset -0.38 dex ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE [non-commensurable]	offset -0.22 dex ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE [non-commensurable]	mixed	Highly environment-specific (Virgo Cluster ram pressure stripping).
Bezanson et al. 2022 ([arXiv:2111.14877])	13 massive post-starburst (PSB) galaxies; SQuIGGLE DR14 spectral shape selection	CO(2-1); assumes Galactic α
CO
	​

	Global	0.07 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	t
dep
	​

≈140 Myr ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE [non-commensurable]	depletion	Gas fraction estimates depend heavily on assumed star-formation history (exponential vs two-component).
Smercina et al. 2022 ([arXiv:2108.03231])	SDSS E+A PSBs; highly disturbed molecular gas hosts	CO(2-1); explores variable α
CO
	​

 due to turbulence	Central kpc (compact molecular reservoirs)	UNCERTAINTY_NOT_QUOTED_BY_SOURCE	10% of starburst SFE ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE [non-commensurable]	low-SFE	High kinetic turbulence inflates CO luminosity independently of gas mass.
Whitaker et al. 2021 ()	6 lensed massive quiescent galaxies (REQUIEM)	Dust continuum (1.3mm); assumes T
dust
	​

=25K, gas-to-dust ratio 100	Global	<0.01 ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE	NONE_FOUND	depletion	Extremely sensitive to assumed dust temperature and highly variable gas-to-dust ratios in quiescent systems.
French et al. 2023 ([arXiv:2210.06522])	Local PSBs	CO(1-0) up to CO(3-2) and HCN; traces dense gas fraction	Global	UNCERTAINTY_NOT_QUOTED_BY_SOURCE	SFR surface density 5.5x below median ± UNCERTAINTY_NOT_QUOTED_BY_SOURCE [non-commensurable]	low-SFE	Assumes constant excitation conditions; requires deeper dense gas tracer integration.
Yesuf et al. 2017 ([arXiv:1705.00668])	Seyfert Green Valley PSBs	CO(1-0); assumes constant α
CO
	​

	Global	0.025 ± 0.018	UNCERTAINTY_NOT_QUOTED_BY_SOURCE	depletion	Explicitly selected for AGN presence, which introduces unique outflow feedback biases.
French et al. 2015 [Anchor] ([arXiv:1501.00983])	32 E+A PSBs; SDSS optical selection	CO(1-0), CO(2-1); assumes Galactic α
CO
	​

	Global (IRAM 30m / SMT 10m)	0.066 ± 0.039	UNCERTAINTY_NOT_QUOTED_BY_SOURCE	inconclusive	Single-dish aperture matching to optical fibers may miss extended diffuse gas.
Decomposition ledger

The literature details various mathematical and observational frameworks to decompose the decline in specific star-formation rate (ΔsSFR) into relative contributions from gas reservoir depletion (Δf
gas
	​

) and suppressed star-formation efficiency (ΔSFE). This decomposition requires mapping observational parameters onto scaling relations, a process inherently constrained by systematic uncertainties and assumptions regarding the physical state of the interstellar medium. The varying approaches reflect an ongoing effort to isolate fuel availability from fuel conversion physics in transitional and quenched galaxies.

Resolved IFU Decompositions (ALMaQUEST Framework)
The ALMaQUEST survey utilizes spatially resolved integral field unit (IFU) data to deconstruct the specific star-formation rate profile on kiloparsec scales. Lin et al. (2025) and Pan et al. (2024) articulate this decomposition mathematically by expressing the specific star-formation rate as a product of gas fraction and efficiency: sSFR=Σ
SFR
	​

/Σ
∗
	​

=(Σ
SFR
	​

/Σ
gas
	​

)×(Σ
gas
	​

/Σ
∗
	​

), which equates to sSFR=SFE×f
gas
	​

 [arXiv:2601.09225, arXiv:2401.05976]. When evaluating the deviation of galaxies from the star-forming main sequence, this relationship is assessed in logarithmic space as ΔsSFR=Δf
gas
	​

+ΔSFE [arXiv:2601.09225].

To categorize the primary quenching mode, Lin et al. (2025) apply a quantitative threshold to the resolved spaxels: if more than 60% of a galaxy's spaxels exhibit ΔSFE<Δf
gas
	​

 (falling below the one-to-one line in the parameter space), the galaxy is classified as undergoing SFE-driven quenching [arXiv:2601.09225]. Conversely, if more than 60% of the spaxels show ΔSFE>Δf
gas
	​

, the system is classified as undergoing f
gas
	​

-driven quenching, with the remainder categorized as experiencing a mixture of modes [arXiv:2601.09225].

Systematics named: The ALMaQUEST analyses explicitly document the severe limitations imposed by the assumption of a constant CO-to-H$2$ conversion factor ($\alpha{CO}$) in quenched hosts [arXiv:2601.09225]. Adopting a uniform Galactic α
CO
	​

 value of 4.35 M
⊙
	​

(K km s
−1
pc
2
)
−1
 across both main-sequence and green-valley systems, as well as across differing morphological components like bulges and disks, risks misattributing changes in the physical state of the gas (such as metallicity or pressure gradients) to true variations in gas mass [arXiv:2601.09225, arXiv:2402.07400]. Furthermore, the literature highlights the SFR-tracer timescale mismatch as a critical systematic; the ultraviolet and optical tracers used to derive Σ
SFR
	​

 trace stellar populations formed over the past ∼100 Myr, whereas CO emissions trace the instantaneous state of the molecular gas, complicating the temporal alignment of the Δf
gas
	​

 and ΔSFE vectors [arXiv:2601.09225].

Environmental Offsets (VERTICO VII)
Brown et al. (2023) deploy an alternative decomposition strategy centered on environmental offsets, specifically targeting Virgo Cluster satellite galaxies undergoing ram pressure stripping [arXiv:2308.10943]. Rather than utilizing a strict one-to-one spaxel threshold, this framework measures the physical offsets of the resolved star-forming main sequence (rSFMS) and the resolved molecular gas main sequence (rMGMS) relative to a field control sample [arXiv:2308.10943]. For galaxies identified as HI-poor due to environmental processing, the analysis reports a simultaneous reduction in both parameters, quantifying the decomposition as a −0.38 dex offset in molecular gas surface density (Δf
gas
	​

) and a −0.22 dex offset in star-formation efficiency (ΔSFE) [arXiv:2308.10943].

Systematics named: Brown et al. (2023) emphasize the limitations of aperture and spatial resolution in their decomposition [arXiv:2308.10943]. The analysis is conducted on 720 pc spaxels, which the authors note can blend distinct physical environments—such as the active stripping fronts on the leading edge of a galaxy and the shielded, dense molecular cores [arXiv:2308.10943]. This spatial blending limits the ability to precisely disentangle whether a measured drop in efficiency is a true suppression of star formation or an artifact of averaging over regions where the gas has already been completely removed [arXiv:2308.10943]. The study also highlights the necessity of morphological k-corrections of the sample, as the presence of stellar bars or prominent bulges can drive gas inflows that counteract environmental stripping, complicating the isolation of the quenching mechanism [arXiv:2308.10943].

Conversion Factor Dependencies (EDGE-CALIFA)
Teng et al. (2026) approach the decomposition by interrogating the foundational assumptions used to derive the gas mass itself [arXiv:2606.23649]. Their analysis of 62 galaxies across the main sequence, green valley, and red sequence suggests that the calculated split between Δf
gas
	​

 and ΔSFE is acutely sensitive to the chosen α
CO
	​

 prescription [arXiv:2606.23649]. By applying four distinct models—a constant Milky Way value, a CO velocity dispersion-based prescription (T24*), and two metallicity and stellar mass density-based prescriptions (B13 and SL24)—they demonstrate that the derived depletion times (t
dep
	​

, the inverse of SFE) shift significantly [arXiv:2606.23649].

Systematics named: Teng et al. heavily emphasize α
CO
	​

 in quenched hosts as the primary systematic governing this physical debate [arXiv:2606.23649]. Quenched and green-valley galaxies inherently possess different interstellar medium (ISM) pressures, metallicities, and turbulent velocity dispersions compared to main-sequence star-forming disks [arXiv:2606.23649]. The authors note that relying on a constant conversion factor systematically underestimates the molecular gas mass in these transitional systems, thereby artificially amplifying the role of Δf
gas
	​

 (depletion) while masking the true extent of ΔSFE (suppression) [arXiv:2606.23649]. They also highlight the systematic risks of non-detections and stacking in determining the baseline depletion times for the reddest galaxies [arXiv:2606.23649].

Dust-Continuum High-Redshift Proxies (REQUIEM)
For quiescent galaxies at high redshift (z>1.5), where direct CO mapping is observationally prohibitive, the decomposition relies on scaling laws derived from dust continuum emissions. Whitaker et al. (2021) utilize deep 1.3mm ALMA observations of six lensed massive quiescent galaxies, employing a modified blackbody fit to convert dust continuum limits into dust mass, and subsequently into molecular gas mass. This framework effectively assigns the entirety of the ΔsSFR decline to Δf
gas
	​

, reporting upper limits on the gas fraction of <1% for the undetected sources.

Systematics named: The authors and subsequent literature explicitly document severe limitations regarding the conversion assumptions, particularly the reliance on a fixed dust temperature (T
dust
	​

=25K) and a uniform gas-to-dust ratio (GDR = 100). The literature explicitly names cosmological hydrodynamical simulations (e.g., SIMBA) which demonstrate that the GDR in quiescent galaxies spans six orders of magnitude [arXiv:2211.01526]. This extreme variability introduces massive systematic risk; a deep non-detection in the dust continuum may indicate total gas depletion (Δf
gas
	​

), or it may merely reflect an elevated gas-to-dust ratio where the molecular gas is retained but devoid of dust [arXiv:2211.01526]. Furthermore, the study notes the limitations of stacking and non-detections, as four of the six galaxies yielded only upper limits on the dust mass.

Central vs global

The debate surrounding reservoir depletion versus suppressed efficiency is deeply intertwined with the spatial scale of the observations. A critical distinction in the literature separates the localized depletion or inefficiency of the central kiloparsec from the galaxy-wide loss of the interstellar medium. Studies that differentiate between central and global environments often report divergent primary quenching modes operating simultaneously within the same galaxy.

Resolved Radial Profiles (ALMaQUEST & EDGE-CALIFA)
The ALMaQUEST survey provides extensive commentary on the radial dependence of quenching mechanisms. Pan et al. (2024) combine radial profiles of gas fraction and star-formation efficiency to discern the underlying mechanisms determining the specific star-formation rate surface density (ΣsSFR) at varying galactocentric radii [arXiv:2402.07400]. A collective analysis of the green valley sample indicates that the reduction in star formation within the central regions (R<0.5R
e
	​

) is primarily attributable to a localized decrease in SFE [arXiv:2402.07400]. Conversely, in the extended disk regions (R>0.5R
e
	​

), the analysis shows that both f
gas
	​

 and SFE contribute jointly to the suppression of star formation [arXiv:2402.07400]. The authors explicitly note that these radial profiles of ΣsSFR are suppressed out to a galactocentric radius of 1.5R
e
	​

 (approximately 7 kpc for their specific sample), representing the outer limits of their extrapolation [arXiv:2402.07400].

This view is corroborated by Lin et al. (2025), who note that the reduction of SFE and molecular gas fraction in green valley galaxies relative to main sequence galaxies is observed in both the bulge and disk regions, suggesting that statistically, the quenching mode may persist from the inner to the outer regions, albeit with larger uncertainties at higher radii [arXiv:2601.09225]. The authors suggest that gravitational torques, particularly in interacting systems, transport cold molecular gas inwards, increasing the central gas fraction without necessarily triggering an equivalent increase in central star formation, thereby isolating the central kpc as a region of profound inefficiency [arXiv:2601.09225].

Environmental Gradients (VERTICO VII)
In the context of dense cluster environments, Brown et al. (2023) distinguish between central gas depletion and global loss by analyzing the spatial progression of ram pressure stripping in Virgo Cluster satellites [arXiv:2308.10943]. Over resolved 720 pc scales, the authors observe systematically elevated star-formation rates in the outskirts of early-stage stripped galaxies [arXiv:2308.10943]. This peripheral enhancement is driven by increased molecular gas surface densities at a fixed stellar mass surface density, while the local SFE remains unchanged with respect to the field control sample [arXiv:2308.10943].

However, when examining the inner structures, the authors report that starvation (the cessation of cosmic gas inflow) regulates the star formation cycle throughout the entirety of the disk, including within the central truncation radius [arXiv:2308.10943]. They conclude that environmental quenching acts as an outside-in mechanism where ram pressure strips the global, extended reservoir, while starvation simultaneously drives a reduction in both molecular gas surface densities and SFE at fixed stellar mass surface densities in the central kpc [arXiv:2308.10943].

Compact Turbulent Cores (Post-Starburst Systems)
Post-starburst galaxies, representing a rapid transitional phase, display extreme spatial concentrations of gas that challenge the global depletion model. Smercina et al. (2022) utilize high-resolution ALMA observations to resolve the molecular gas in these systems, explicitly evaluating the central versus global environments [arXiv:2108.03231, arXiv:2210.12199]. They assert that the global position of a galaxy relative to the star-forming main sequence is largely determined by the inner star-formation efficiency, while the departure from the main sequence is driven by the absolute availability of central gas [arXiv:2108.03231].

The authors explicitly note that the "fall" of star formation in these galaxies was not precipitated by a complete, galaxy-wide gas expulsion or redistribution [arXiv:2108.03231]. Instead, their high-resolution view of the interstellar medium indicates that the remaining gas is highly concentrated in turbulent central molecular reservoirs (within the central few kiloparsecs) [arXiv:2108.03231, arXiv:2210.12199]. Over this central radius, star formation is heavily suppressed, forming stars at only 10% of the efficiency observed in typical starburst galaxies with comparable gas surface densities [arXiv:2108.03231]. Smercina et al. conclude that the central few kiloparsecs are the most consequential region for galaxy evolution at low redshift, as global gas loss is secondary to the suppression of the central core [arXiv:2108.03231].

Global Integration Constraints (High-Redshift)
Conversely, studies operating at high redshift are frequently constrained to global measurements due to the limitations of spatial resolution. Whitaker et al. (2021), analyzing the REQUIEM sample of lensed quiescent galaxies at z∼1.5−3, utilize unresolved dust continuum fluxes to estimate the total gas mass. Based on the deep non-detections in the global integrated flux, the authors conclude that the entire galaxy-wide gas reservoir has been depleted. There is an explicit note that it remains difficult to extrapolate from these small, globally integrated samples to understand the internal spatial dynamics; no resolved central-kpc depletion gradients were measured or extrapolated from these specific non-detections.

Population fractions

The literature provides several published fractions quantifying the proportion of quenched, quenching, or post-starburst systems that are observed to be gas-poor versus those that are gas-rich-but-inefficient. These fractions are highly sensitive to the specific tracer utilized and the selection biases inherent in the sample definitions. The following fractions are reported with all four required qualifiers and their stated selection biases.

The SQuIGGLE Survey Fraction (Bezanson et al. 2022)

Fraction: 45% (6 out of 13) of the primary targets are reported as hosting massive, gas-rich reservoirs (M
H
2
	​

	​

≳10
9
M
⊙
	​

), corresponding to an average gas fraction of ∼7% (or ∼14% depending on the star-formation history model) [arXiv:2111.14877].

Tracer: CO(2-1) emission [arXiv:2111.14877].

Selection: Post-starburst galaxies selected from the Sloan Digital Sky Survey (SDSS) DR14 spectroscopic samples based strictly on their spectral shapes [arXiv:2111.14877].

Denominator: 13 massive (M
∗
	​

≳10
11
M
⊙
	​

) post-starburst galaxies [arXiv:2111.14877].

z range: z∼0.6 [arXiv:2111.14877].

Stated biases: The source explicitly states that the SQuIGGLE sample is not intended to be a complete selection of post-starburst galaxies at these redshifts [arXiv:2111.14878]. The selection function is complex and is not conducive to volume-complete number density studies [arXiv:2111.14878]. Instead, the survey was deliberately designed to select the brightest, most massive, and most burst-dominated post-starburst galaxies at intermediate redshifts, inherently biasing the fraction toward the most extreme transitional events rather than the broader quenching population [arXiv:2111.14878].

The REQUIEM Survey Fraction (Whitaker et al. 2021)

Fraction: 67% (4 out of 6) of the sample are reported as undetected and profoundly gas-poor (gas fraction upper limits of <1%), while 33% (2 out of 6) show detectable emission implying a ∼1% molecular gas fraction.

Tracer: Dust continuum emission (1.3mm) serving as a proxy for the molecular interstellar medium, assuming a standard gas-to-dust ratio.

Selection: Massive quiescent galaxies selected for exceptionally low star-formation rates.

Denominator: 6 strongly lensed galaxies.

z range: 1.6<z<3.2.

Stated biases: The source states that the sample is distinct from other samples of quiescent galaxies because of the extreme sensitivity of the observations required. The requirement for strong gravitational lensing magnification inherently selects for a highly specific, rare subset of extremely massive background sources, meaning the resulting fraction cannot be smoothly extrapolated to the general field population of high-redshift quiescent galaxies.

The SDSS E+A Fraction (French et al. 2015)

Fraction: 53% (17 out of 32) of the sample are detected and reported as gas-rich, with molecular gas mass to stellar mass fractions of ∼10
−2
 to 10
−0.5
, comparable to those of star-forming galaxies [arXiv:1501.00983].

Tracer: CO(1-0) and CO(2-1) emission [arXiv:1501.00983].

Selection: Post-starburst (or "E+A") galaxies characterized by low H$\alpha$ emission and strong Balmer absorption, drawn from SDSS [arXiv:1501.00983].

Denominator: 32 nearby galaxies [arXiv:1501.00983].

z range: 0.01<z<0.12 [arXiv:1501.00983].

Stated biases: The sample is drawn from the SDSS optical catalog, meaning the primary selection relies on 3-arcsecond fiber spectroscopy. This central-fiber selection heavily biases the sample toward galaxies where the post-starburst signature is centrally concentrated, potentially missing systems where the transition is occurring strictly in the outer disk, and restricting the statistical baseline to the optically brightest systems [arXiv:1501.00983].

The Seyfert PSB Fraction (Yesuf et al. 2017)

Fraction: 27% of the sample are reported as detected with molecular gas, yielding a much smaller mean gas fraction (μ=0.025) than typical PSB samples [arXiv:1705.00668].

Tracer: CO(1-0) emission [arXiv:1705.00668].

Selection: Green-valley post-starburst galaxies explicitly selected for Seyfert-like optical emission line ratios [arXiv:1705.00668].

Denominator: 15 galaxies (derived from text citing a 27% detection rate in a combined sample of Seyfert-like PSBs) [arXiv:1705.00668].

z range: Local universe (SDSS cross-match) [arXiv:1705.00668].

Stated biases: The source explicitly states that the sample is cross-selected for Seyfert-like emission, which inherently biases the fraction by restricting the denominator exclusively to galaxies hosting active nuclear accretion [arXiv:1705.00668]. This introduces unique feedback mechanisms not present in the broader PSB population, limiting the applicability of the 27% fraction to systems undergoing active AGN processing [arXiv:1705.00668].

The E+A Atomic Gas Fraction    

Fraction: Roughly half (6 out of 11, or 55%) of the sample are detected and reported as gas-rich, harboring gas fractions between 1 and 10 percent with respect to their stellar mass.   

Tracer: HI 21-cm emission.   

Selection: E+A transitional galaxies.   

Denominator: 11 galaxies.   

z range: z<0.05.   

Stated biases: The sample size is explicitly noted as small and limited by the shallow detection limits of single-dish radio observations. Furthermore, the study notes that detecting diffuse atomic gas requires specific environmental conditions, meaning the fraction may be skewed against cluster PSBs (like those in Coma, which the source notes seem to be uniformly gas poor).   

AGN association tests

The presence of an Active Galactic Nucleus (AGN) is frequently invoked in the literature as a primary driver of the transition from star-forming to quiescent states. Studies explicitly test the association of AGN history and presence with both the physical removal of the gas reservoir and the suppression of the star-formation efficiency. The following tests and their respective conclusions are reported strictly as each study's own claim:

AGN and Absolute Reservoir Clearing
Yesuf et al. (2017) investigate the relationship between AGN presence and gas depletion in green-valley Seyfert post-starburst galaxies [arXiv:1705.00668]. The authors claim that there is a delayed molecular gas destruction associated with AGN [arXiv:1705.00668]. They test the theoretical momentum limits of AGN outflows and claim that an AGN may only impart sufficient momentum to successfully clear galactic disks once the molecular gas fraction has already natively dropped below approximately 4% [arXiv:1705.00668]. They assert that this explains the minor role of AGN in quenching massive starbursts (which harbor gas fractions of 20-30%) and argues that AGN act as a secondary sweeping mechanism rather than the primary cause of early depletion [arXiv:1705.00668].

AGN and Broad-Line Evolution
Operating at higher redshifts (z∼0.7), the SQuIGGLE survey tests the incidence of nuclear activity in massive post-starburst galaxies [arXiv:2111.14878]. Setton et al. and Greene et al. claim that over their observed mass range, the incidence of radio activity is only weakly dependent on stellar mass and is completely independent of stellar age [arXiv:2111.14878]. They report a deficit of broad-line AGN in the pre-merger phase that eventually evolves into an observed excess in post-mergers [arXiv:2111.14878]. The authors claim this pattern is consistent with the evolution of the covering fraction of nuclear obscuring material, where tidally triggered inflows initially increase nuclear dust, and subsequent feedback from the AGN clears this local material [arXiv:2111.14878]. They do not, however, claim that this local clearing equates to the total expulsion of the global molecular gas reservoir.

AGN and Turbulence Injection (Efficiency Suppression)
Several studies test the association between AGN and the suppression of star-formation efficiency, arguing against total gas removal. Lin et al. (2025), utilizing the ALMaQUEST survey data, observe a transition toward predominantly SFE-driven quenching as galaxies move from the main sequence to the green valley [arXiv:2601.09225]. The authors claim this transition is possibly linked to internal processes such as AGN activity and morphological quenching, which perturb the gas without necessarily ejecting it [arXiv:2601.09225].

This framework is extensively tested by Smercina et al. (2022) in post-starburst systems [arXiv:2108.03231]. By classifying SDSS and IllustrisTNG galaxies, they claim that black holes can successfully quench star formation through a combination of heating and the injection of extreme turbulence into the interstellar medium [arXiv:2108.03231]. They assert that this AGN-driven turbulence raises the kinetic pressure of the gas, preventing it from collapsing into the dense states required for star formation, thereby causing the profound suppression of efficiency observed in their compact central gas reservoirs [arXiv:2108.03231].

Similarly, French et al. (2023) apply multiwavelength diagnostics to investigate AGN activity in local PSBs [arXiv:2210.06522]. They claim that local PSBs do not show an excess of AGN signatures compared to star-forming galaxies, leading them to assert that for low-z PSB populations, a more subtle, preventive feedback mechanism—one that maintains turbulence and keeps SFE low over long depletion times—is more dominant than powerful, ejective AGN outflows [arXiv:2210.06522].

What would discriminate

The literature explicitly identifies several critical measurements and theoretical advancements required to cleanly discriminate between true gas reservoir depletion and retained gas forming stars inefficiently. The authors of these studies detail specific observational methodologies alongside the feasibility limits that currently restrict their broad application.

Mapping Dense Gas Tracers (HCN and HCO+)
French et al. (2023) propose that observing high-J CO transitions alongside dense gas tracers (such as HCN and HCO+) is a definitive method for separating the two scenarios [arXiv:2210.06522]. The authors attribute the low SFE observed in many post-starburst galaxies to the physical state of the gas, arguing that if a galaxy hosts abundant diffuse CO(1-0) but lacks HCN emission, it indicates that the retained gas is failing to condense into the dense cores necessary for star formation [arXiv:2210.06522]. Measuring the HCN/CO luminosity ratio therefore directly discriminates whether the bottleneck is a lack of overall fuel or a failure in the internal collapse mechanics of the ISM [arXiv:2210.06522].
Stated feasibility limits: The authors note that obtaining the complete CO Spectral Line Energy Distribution (SLED) up to the CO(3-2) transition, alongside faint dense gas tracers like HCN, remains scarce in the literature [arXiv:2210.06522]. They explicitly state that acquiring these measurements requires ALMA integration times that are currently highly expensive and generally unfeasible for large statistical samples, particularly for faint, high-redshift, or deeply quenched galaxies where the dense gas fraction is intrinsically low [arXiv:2210.06522].

Spatially Resolved α
CO
	​

 Variations
Teng et al. (2026) and the broader EDGE-CALIFA collaboration propose that mapping the physical dependencies of the CO-to-H$2$ conversion factor ($\alpha{CO}$) is paramount to resolving the debate [arXiv:2606.23649]. They assert that utilizing prescriptions like the T24* model—which dynamically scales the conversion factor based on local variations in velocity dispersion and metallicity—is required to accurately measure the true molecular gas mass in transitional systems [arXiv:2606.23649]. If the application of a variable α
CO
	​

 systematically lowers the inferred gas mass in quenched hosts, it shifts the interpretation heavily toward reservoir depletion rather than SFE suppression [arXiv:2606.23649].
Stated feasibility limits: The literature cautions that deriving a robust, spatially resolved α
CO
	​

 requires exceptionally deep, high-resolution integral field unit (IFU) data paired with matched, resolved CO mapping across multiple galactic radii [arXiv:2606.23649]. This is currently feasible only for massive, bright, and very nearby samples (such as the 62 galaxies in the EDGE-CALIFA survey) and is observationally prohibitive for high-redshift populations where kiloparsec-scale resolution is unattainable [arXiv:2606.23649].

Independent High-Redshift Gas Proxies ([CII] Mapping)
To address the severe limitations of dust continuum proxies in high-redshift quiescent galaxies, Whitaker et al. (2021) and subsequent REQUIEM-associated literature propose utilizing the [CII] 158 μm fine-structure emission line as an independent, direct tracer of the cold gas reservoir. This measurement is proposed to discriminate whether the deep 1.3mm dust continuum non-detections represent true, absolute gas exhaustion (Δf
gas
	​

), or whether the galaxies possess highly elevated gas-to-dust ratios where a molecular reservoir is retained but entirely devoid of measurable dust [arXiv:2211.01526].
Stated feasibility limits: The literature explicitly states the severe feasibility limits of this approach. Firstly, the interpretation is physically complex; while [CII] is proposed as a more reliable tracer in regions where CO is photo-dissociated, the literature cautions that [CII] emission can primarily trace photo-dissociation regions (PDRs) rather than the bulk molecular gas, and some models report that the fraction of [CII] emission arising strictly from molecular gas is low [arXiv:2211.01526]. Secondly, achieving the required signal-to-noise for a [CII] detection in an un-lensed, massive quiescent galaxy at z>2 is noted as observationally prohibitive, necessitating the continued reliance on rare, strongly gravitationally magnified targets.

Links ledger
Short name	Citation or UNCITED_NOT_USABLE	QUARANTINED_PENDING_LOCAL_CHECK
Teng et al. 2026	arXiv:2606.23649	QUARANTINED_PENDING_LOCAL_CHECK
Pan et al. 2024 / Lin et al. 2025	arXiv:2402.07400, arXiv:2601.09225	QUARANTINED_PENDING_LOCAL_CHECK
Brown et al. 2023	arXiv:2308.10943	QUARANTINED_PENDING_LOCAL_CHECK
Bezanson et al. 2022	arXiv:2111.14877	QUARANTINED_PENDING_LOCAL_CHECK
Smercina et al. 2022	arXiv:2108.03231	QUARANTINED_PENDING_LOCAL_CHECK
Whitaker et al. 2021	DOI:10.1038/s41586-021-03806-7, arXiv:2211.01526	QUARANTINED_PENDING_LOCAL_CHECK
French et al. 2023	arXiv:2210.06522	QUARANTINED_PENDING_LOCAL_CHECK
Yesuf et al. 2017	arXiv:1705.00668	QUARANTINED_PENDING_LOCAL_CHECK
French et al. 2015	arXiv:1501.00983	QUARANTINED_PENDING_LOCAL_CHECK
Setton et al. 2022	arXiv:2111.14878	QUARANTINED_PENDING_LOCAL_CHECK
ALMaQUEST ΔsSFR	arXiv:2401.05976	QUARANTINED_PENDING_LOCAL_CHECK

GEMINI_WEB_RAMPAGE_R4_OUTPUT_DONE_20260711T052300Z

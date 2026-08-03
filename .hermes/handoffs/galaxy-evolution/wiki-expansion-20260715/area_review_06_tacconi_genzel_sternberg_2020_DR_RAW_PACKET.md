# Review Base 06 raw Deep Research packet — Tacconi, Genzel & Sternberg 2020

advisory_only: true
canonical_packet_released: false
wiki_write_performed_by_tori: false
identifier_verification_required_before_canonical_release: true

Queue: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/REVIEW_BASE_QUEUE.md`
Queue SHA-256: `7f9384766bdc5dd7473f7265018344ba6067e9b612cdbe77d59a7adf7ffc3f5b`
Prompt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715/area_review_06_tacconi_genzel_sternberg_2020_DR_PROMPT.md`
Prompt SHA-256: `53b863eca55533e053da49ebe600e779a79eb53fa0d6c5645e5365b52ba77672`
Conversation ID: `901a6142feada8f1`
Submit UTC: `2026-07-15T16:14:26.427986Z`
Research Start UTC: `2026-07-15T16:15:02.907519Z`
Result captured UTC: `2026-07-15T16:32:16.997051Z`
Raw result SHA-256: `bfd901e7afd71a3135806925a60fb62811bb034533e9a1a3d8197f9f8732c84b`

## Deep Research review-base result

The Evolution of the Star-Forming Interstellar Medium Across Cosmic Time: Source-Base Review

The epoch spanning redshifts z∼1 to 3, colloquially known as "cosmic noon," represents the most active period of stellar mass assembly and black hole growth in the history of the Universe. Over the past decade, observational astronomy has undergone a revolution in its ability to probe the cold interstellar medium (ISM)—the direct fuel for star formation—across this critical epoch. This transformation has been driven primarily by the advent of powerful millimeter, submillimeter, and radio interferometers, notably the Atacama Large Millimeter/submillimeter Array (ALMA) and the Northern Extended Millimeter Array (NOEMA), which have allowed researchers to map the molecular gas and dust components of distant galaxies with unprecedented sensitivity. The 2020 review by Tacconi, Genzel, and Sternberg stands as the definitive synthesis of this observational renaissance, bounding the physical scaling relations that govern galaxy evolution.   

This document serves as the authoritative source-base review of the 2020 synthesis. It extracts the foundational physical frameworks, scaling relations, kinematic paradigms, and open tensions required to construct a comprehensive understanding of the star-forming ISM across cosmic time.

1. Review Identity and Scope Map

Review Identity

Title: The Evolution of the Star-Forming Interstellar Medium Across Cosmic Time

Authors: Tacconi, Linda J.; Genzel, Reinhard; Sternberg, Amiel

Year: 2020

Journal: Annual Review of Astronomy and Astrophysics, Volume 58, Pages 157-203

DOI: 10.1146/annurev-astro-082812-141034

arXiv: 2003.06245

ADS Bibcode: 2020ARA&A..58..157T

Authorized Scientific Territory
The review establishes the phenomenological and physical laws governing normal star-forming galaxies out to z∼4. The core scientific territory encompasses the identification and calibration of cold-gas tracers, specifically the rotational transitions of carbon monoxide (CO), fine-structure lines of neutral carbon ([CI]), and Rayleigh-Jeans dust continuum emission. It extensively maps the derivation of the CO-to-H
2
	​

 conversion factor (α
CO
	​

) and its profound dependence on gas-phase metallicity and local radiation fields. The synthesis maps the empirical scaling relations for molecular gas fractions (μ
gas
	​

) and depletion times (t
dep
	​

) as functions of cosmic time, stellar mass, and main-sequence offset. It further explores the theoretical underpinnings of these scaling relations via "gas-regulator" (or bathtub) models, connecting global gas accretion from the cosmic web to self-regulated star formation and galactic outflows. Finally, the scope includes the internal kinematic dynamics of high-redshift, gas-rich disks, focusing on elevated turbulent velocity dispersions, Toomre gravitational instabilities, and the formation and migration of giant star-forming clumps.   

Explicit Exclusions
To maintain strict adherence to the review's boundaries, specific phenomena are explicitly quarantined. Active Galactic Nuclei (AGN) fueling mechanisms, accretion disk physics, and AGN-driven outflow models are excluded unless they strictly pertain to the global depletion of the molecular gas reservoir in the host galaxy. Post-2020 observational constraints—such as rest-optical kinematics derived from the James Webb Space Telescope (JWST) or ALMA large programs published after 2020—are strictly quarantined. The synthesis also excludes the detailed physics of the Epoch of Reionization (z>6), Population III star formation, and the internal sub-parsec physics of individual Giant Molecular Clouds (GMCs) unless determining integrated global efficiencies.

Methodological Definitions and Assumptions
Throughout this source base, stellar masses (M
∗
	​

) and star-formation rates (SFR) are anchored to a Chabrier (2003) Initial Mass Function (IMF). The Star-Forming Main Sequence (SFMS) is defined using consensus empirical fits that track the SFR-M
∗
	​

 plane across redshift. Crucially, strict tracer separation is maintained: CO luminosity (L
CO
′
	​

), dust continuum flux density, and inferred molecular mass (M
H2
	​

) are never treated as interchangeable. M
H2
	​

 remains an inferred, model-dependent quantity reliant upon specific, stated calibration assumptions regarding α
CO
	​

 or dust-to-gas ratios.   

Deep Narrative Synthesis of the Star-Forming ISM
Molecular, Atomic, and Dust-Based Cold-Gas Tracers

The primary challenge in studying the cold ISM is that molecular hydrogen (H
2
	​

), which dominates the dense gas phase where stars form, lacks a permanent electric dipole moment. It therefore does not emit efficiently at the typical temperatures (10−30 K) of giant molecular clouds. Consequently, astronomers must rely on proxy tracers. The most prevalent tracer is carbon monoxide (CO), specifically its low-J rotational transitions (e.g., J=1−0,2−1,3−2). CO is the second most abundant molecule in the ISM, and its transitions are easily excited by collisions with H
2
	​

 at low temperatures. However, observing high-redshift CO requires significant integration time.   

An alternative and highly efficient tracer authorized by the review is the thermal continuum emission from interstellar dust. When young, massive stars emit ultraviolet radiation, the surrounding dust grains absorb this energy and re-emit it in the far-infrared. At high redshifts, the expansion of the universe shifts this emission into the submillimeter bands (the negative K-correction), allowing arrays like ALMA to detect the Rayleigh-Jeans tail of the dust emission. Because the Rayleigh-Jeans tail is optically thin and heavily dependent on the total dust mass rather than small fluctuations in dust temperature, it serves as an excellent proxy for the total ISM mass, provided one can assume a stable dust-to-gas ratio. Neutral carbon fine-structure lines ([CI] 1-0 and 2-1) have also emerged as powerful tracers, as they originate from the same shielded regions as CO and share similar excitation temperatures.   

Conversions, Calibrations, and Systematics

Translating a CO luminosity (L
CO
′
	​

) into a total molecular gas mass (M
H2
	​

) requires the conversion factor α
CO
	​

. In local, solar-metallicity spiral galaxies like the Milky Way, this value is robustly calibrated to ∼4.36M
⊙
	​

(K km s
−1
 pc
2
)
−1
. However, the 2020 synthesis emphasizes that α
CO
	​

 is highly dependent on gas-phase metallicity. In metal-poor environments (e.g., dwarf galaxies or early high-z progenitors), the lack of dust allows destructive far-ultraviolet radiation to penetrate deeply into molecular clouds. This radiation photo-dissociates the CO molecules, but the H
2
	​

 molecules—which self-shield much more efficiently—survive. This creates thick envelopes of "CO-dark" molecular gas. Applying a standard Milky Way conversion factor to a low-metallicity galaxy will catastrophically underestimate its true molecular gas mass. Thus, empirical corrections must be applied, scaling α
CO
	​

 non-linearly as metallicity drops below solar values.   

Similarly, utilizing the dust continuum requires a calibration of the dust-to-gas ratio (δ
GDR
	​

). In massive, mature galaxies, this ratio scales linearly with metallicity. However, at extreme high redshifts or in highly starbursting environments, the balance between dust production (in AGB stars and supernovae) and dust destruction (via supernova shocks) alters this calibration. Furthermore, at redshifts z>3, the cosmic microwave background (CMB) becomes a non-negligible source of heating, raising the background temperature and potentially altering the excitation states of CO while simultaneously reducing the contrast of the emission lines.   

Scaling Relations of the Molecular Gas

The compilation of hundreds of CO and dust continuum observations has permitted the derivation of robust empirical scaling relations. The molecular gas fraction (μ
gas
	​

=M
gas
	​

/M
∗
	​

) represents the ratio of fuel to the existing stellar assembly. The data conclusively demonstrate that galaxies at cosmic noon (z∼1−3) were fundamentally different from local galaxies; they were incredibly gas-rich, with molecular gas fractions routinely exceeding 30−50%, compared to the ∼5−10% typical of the local universe.   

The depletion time (t
dep
	​

=M
gas
	​

/SFR) measures the theoretical timescale over which a galaxy would consume its entire molecular reservoir if star formation continued at the current rate without any new gas accretion. The synthesis reveals that t
dep
	​

 is not a universal constant. It scales significantly with redshift, indicating that star formation was globally more efficient in the early universe, perhaps tied to the shorter dynamical times of dark matter halos. Furthermore, t
dep
	​

 strongly anti-correlates with a galaxy's specific star-formation rate relative to the main sequence. Galaxies driven far above the MS (starbursts) exhibit highly compacted, dense gas reservoirs that undergo extraordinarily rapid star formation, driving depletion times down to ∼100 Myr, whereas typical MS galaxies maintain depletion times on the order of ∼1 Gyr.   

Gas-Regulator (Bathtub) Models

To physically interpret these empirical scaling relations, the review heavily relies on "gas-regulator" or "bathtub" models. In these analytic frameworks, a galaxy is treated as a single reservoir. The rate of change of the gas mass is governed by the continuous accretion of pristine gas from the cosmic web, minus the gas consumed by star formation, minus the gas ejected by feedback-driven outflows. The mathematical balance implies that galaxies quickly reach a quasi-steady equilibrium state where the star formation rate dynamically adjusts to match the net inflow rate.   

Because cosmic accretion rates were exponentially higher in the dense, early universe, the equilibrium gas fractions of high-redshift galaxies were correspondingly massive. This naturally explains the elevated SFRs at cosmic noon. The efficiency of galactic winds is parameterized by the mass-loading factor (η), defined as the ratio of the outflow mass rate to the star formation rate. By tuning the mass-loading factor and the star formation efficiency, these models successfully reproduce the observed co-evolution of the star-forming main sequence, the molecular gas fractions, and the mass-metallicity relation across cosmic time.   

Disk Dynamics and Instability at High Redshift

The kinematic structure of star-forming disks at cosmic noon radically diverges from the thin, ordered spiral disks seen today. High-redshift disks are characterized by immense turbulence. While they are rotation-dominated, their intrinsic gas velocity dispersions (σ
0
	​

) frequently reach 40−80 km/s, yielding rotation-to-dispersion ratios (v
rot
	​

/σ
0
	​

) of just 2 to 6.   

This elevated turbulence is necessary to maintain stability in such gas-heavy environments. According to the Toomre Q stability criterion, a disk becomes unstable to gravitational collapse if the surface density exceeds the stabilizing forces of rotation and velocity dispersion. Because μ
gas
	​

 is so high at z∼2, the disks operate in a state of marginal instability (Q∼1). This leads to violent disk fragmentation, where the gas collapses into massive, kiloparsec-scale star-forming clumps containing 10
8
−10
9
M
⊙
	​

 of material. These clumps induce severe asymmetrical torques, driving rapid radial inflow of cold gas toward the galactic center. This radial transport feeds central starbursts, leading to morphological "compaction" and the rapid growth of classical galactic bulges. Simultaneously, kinematic studies of these compact, turbulent disks reveal that their central effective radii are strongly baryon-dominated, showing little evidence of the deep dark-matter potential wells that dominate the outer regions of local galaxies.   

2. Established Findings
Entry Key	Role	Epistemic Type	Bounded Finding	Physical / Sample / Tracer Boundary	Review Topic Basis	Confidence Note	Source Keys
[REV06-E01]	Core Conclusion	observation	Star-forming galaxies at z∼1−3 contained significantly higher molecular gas mass fractions (μ
gas
	​

∼0.3−0.5) than local equivalents.	Massive (M
∗
	​

>10
9
M
⊙
	​

) MS galaxies. CO and dust continuum tracers.	Evolutionary trajectory of cosmic molecular gas density mirroring SFR density.	High. Multiple tracers converge on this shift.	[REV06-P001], [REV06-P004], [REV06-P014]
[REV06-E02]	Core Conclusion	calibration	The integrated molecular gas depletion time scales systematically with redshift and the ΔMS offset.	Integrated galactic scales, 0<z<3. Excludes sub-kpc cloud scales.	Star formation efficiency increases in starbursts and early epochs.	High confidence in functional form.	[REV06-P002], [REV06-P015], [REV06-P021]
[REV06-E03]	Core Conclusion	analytic_theory	Global rates of cold gas accretion from the cosmic web control the evolution of cold gas content and SFRs.	Integrated scaling of total baryonic accretion over cosmological timescales.	Validates "gas-regulator" models in quasi-steady state.	Strong theoretical consensus matching observed sSFR.	[REV06-P028], [REV06-P031], [REV06-P035]
[REV06-E04]	Methodological Benchmark	calibration	α
CO
	​

 increases non-linearly in low-metallicity environments due to photo-dissociation of CO.	Sub-solar metallicity systems (Z<0.5Z
⊙
	​

). GMC chemistry boundaries.	Essential correction to prevent mass underestimation at high-z.	High confidence in mechanism; moderate in exact slopes.	[REV06-P006], [REV06-P008], [REV06-P026]
[REV06-E05]	Scaling Law	observation	The global relationship between SFR and M
H2
	​

 follows a near-linear power law (N≈1.1−1.2).	Explicitly excludes HI. Integrates over total galactic molecular mass.	Local physics regulates global output regardless of redshift.	Robust for integrated MS; varies when mixing populations.	[REV06-P003], [REV06-P017]
[REV06-E06]	Kinematic Paradigm	observation	Gas-rich disks at z∼1−3 exhibit intrinsic velocity dispersions of σ
0
	​

∼40−80 km/s.	Hα IFU and CO kinematics of massive high-z star-forming disks.	High turbulence required for Toomre Q stability in gas-heavy disks.	High. Universally observed across major IFU surveys.	[REV06-P018], [REV06-P019]
[REV06-E07]	Kinematic Paradigm	observation	The central regions (<R
e
	​

) of massive disks at cosmic noon are strongly baryon-dominated.	M
∗
	​

>10
10
M
⊙
	​

 at 1<z<3. Inner rotation curves.	High-z disks are compact, allowing baryons to dictate central potentials.	Moderate to High; reliant on beam-smearing corrections.	[REV06-P020], [REV06-P037]
[REV06-E08]	Methodological Benchmark	calibration	Rayleigh-Jeans dust continuum serves as a robust proxy for total ISM mass given a valid δ
GDR
	​

.	Requires mass-weighted T
dust
	​

 and linear δ
GDR
	​

 scaling down to ∼0.2Z
⊙
	​

.	Enabled rapid expansion of gas measurements without deep CO scans.	High for massive galaxies; uncertain in low-Z regimes.	[REV06-P009], [REV06-P024], [REV06-P025]
[REV06-E09]	Physical Constant	analytic_theory	Star-formation efficiency per free-fall time (ϵ
ff
	​

) is universally low, averaging ∼1−2%.	Compares global depletion to internal dynamical times of GMCs.	SF is globally inefficient, regulated by supersonic streams and feedback.	Strong theoretical consensus.	[REV06-P034], [REV06-P043]
[REV06-E10]	Evolutionary Pathway	hydrodynamic_simulation	Violent disk instabilities drive radial inflows, triggering central compaction and bulge growth.	Transition of gas-rich disks to centrally concentrated spheroids.	Explains structural evolution along the MS and inside-out quenching.	Moderate. Simulated extensively; difficult to observe directly.	[REV06-P030], [REV06-P033], [REV06-P039]
[REV06-E11]	Core Conclusion	observation	The tight scatter of the SFMS (∼0.3 dex) persists across cosmic time to at least z∼4.	Integrated stellar mass and UV+IR SFRs.	Major mergers are temporary excursions, not the dominant assembly mode.	Extremely high.	[REV06-P010], [REV06-P011], [REV06-P012]
[REV06-E12]	Phase Transition Limit	observation	Atomic hydrogen (HI) surface density saturates at ∼10M
⊙
	​

pc
−2
 in local massive spirals.	z∼0 HI 21cm mapping combined with CO mapping.	Explains why H
2
	​

 dominates star-formation scaling in dense galactic centers.	High for z∼0; assumed theoretically for high redshift.	[REV06-P007], [REV06-P016]
3. Open Debates and Tensions
Entry Key	Competing Positions	Why Unresolved in 2020	Boundaries	Source Keys
[REV06-D01]	CO-to-H2 Conversion Factor: Does α
CO
	​

 follow a gradual curve based on shielding, or a steeper dependence heavily modulated by the radiation field (ΔMS)?	Precise sub-kpc resolution of CO-dark gas in low-Z high-z dwarfs was beyond ALMA sensitivity limits.	Rest-frame sub-mm CO observations in Z<0.5Z
⊙
	​

 systems.	[REV06-P006], [REV06-P026]
[REV06-D02]	Dust-to-Gas Evolution: Does δ
GDR
	​

 scale linearly with metallicity, or does it steepen non-linearly at high-z due to supernova dust destruction?	Measuring independent gas masses and dust masses simultaneously in z>3 low-mass galaxies was observationally prohibitive.	Limits accuracy of ALMA Band 7 for M
∗
	​

<10
10
M
⊙
	​

 at z>2.	[REV06-P009], [REV06-P024]
[REV06-D03]	Main-Sequence vs. Bimodal Starbursts: Is there a strict bimodality (accretion-driven MS vs merger-driven starbursts), or a single continuous distribution scaling smoothly?	Distinguishing a compacted secular disk from a late-stage major merger at z∼2 requires un-smeared kinematic resolution.	Galaxies >4× above the SFMS ridgeline.	[REV06-P015], [REV06-P023], [REV06-P027]
[REV06-D04]	Redshift vs. Hubble-Time Scaling: Does global depletion time scale tightly with 1+z (cosmological density) or t
H
	​

 (internal dynamical timescales)?	The functional fits are statistically indistinguishable within the scatter of z=0 to z=3 observational data.	Global scaling relations of t
dep
	​

.	[REV06-P001], [REV06-P002]
[REV06-D05]	Turbulence Powered by Feedback vs. Accretion: Is the high σ
0
	​

 in high-z disks maintained by stellar feedback (supernovae) or gravity/accretion?	Analytical models show both inject sufficient energy; decoupling requires mapping velocity dispersion of non-star-forming gas.	Disk kinematics at z>1.	[REV06-P032], [REV06-P044]
[REV06-D06]	Disk Fragmentation and Clump Survival: Do giant clumps survive long enough to migrate and form bulges, or does intense stellar feedback disrupt them rapidly?	Hydrodynamic simulations yield conflicting results based on how aggressively sub-grid stellar feedback is implemented.	Kiloparsec-scale clumps in z∼1−3 disks.	[REV06-P022], [REV06-P029]
[REV06-D07]	Depletion-Time Interpretation: Is the t
dep
	​

 variation across the MS a true reflection of changing local SF efficiency, or an artifact of varying structural bulge/disk ratios?	Required sub-kpc mapping of molecular gas across a massive sample of MS galaxies, resource-intensive for ALMA.	Physical meaning of integrated M
gas
	​

/SFR.	[REV06-P003], [REV06-P038]
[REV06-D08]	Gas-Regulator Uniqueness: Can bathtub models uniquely validate mass-loading mechanisms, or are parameters like η and pristine inflow fraction entirely degenerate?	Direct, mass-resolved observational constraints on the mass-loading factor (η) of outflows remained elusive and model-dependent.	Semi-analytic models and equilibrium timescales.	[REV06-P028], [REV06-P031]
4. Key Measurements, Model Benchmarks, and Calibrations
Entry Key	Parameter	Exact Value / Equation	Units	Tracer/Sample/IMF/State	Caveat	Source Keys
[REV06-N01]	Local Milky-Way α
CO
	​

	4.36	M
⊙
	​

(K km s
−1
 pc
2
)
−1
	Calibrated base value for CO-to-H
2
	​

 in solar-metallicity MS disks.	Includes 36% mass correction for Helium. Fails at low metallicity.	[REV06-P006]
[REV06-N02]	Metallicity Correction	α
CO
	​

(Z)∝(Z/Z
⊙
	​

)
−1.5 to −2.0
	Dimensionless	Geometric mean of adopted models used to correct low-mass galaxy gas masses.	Diverges rapidly below 12+log(O/H)≈8.4.	[REV06-P006], [REV06-P008]
[REV06-N03]	Gas Fraction MS Scaling	μ
gas
	​

∝(sSFR/sSFR
MS
	​

)
0.53
	Dimensionless	Observed fit linking gas mass fractions to vertical position off the MS.	Dependent on combined CO and dust sample fits.	[REV06-P001]
[REV06-N04]	Depletion Time MS Scaling	t
dep
	​

∝(sSFR/sSFR
MS
	​

)
−0.44
	Dimensionless	Observed fit indicating galaxies above the MS form stars more efficiently.	Slopes are sensitive to the chosen α
CO
	​

 prescription.	[REV06-P001]
[REV06-N05]	Cosmic Depletion Evolution	t
dep
	​

∝(1+z)
−0.6
 (or ∝t
H
	​

)	Gyr	Calibrated scaling showing faster gas consumption at early epochs.	Base value at z=0 is roughly 1.5 Gyr.	[REV06-P002]
[REV06-N06]	Toomre Q Stability	Q=
πGΣ
gas
	​

κσ
0
	​

	​

≈1	Dimensionless	Theoretical threshold for marginal stability maintained by high-z gas-heavy disks.	Requires accurate mapping of total surface mass density (Σ
gas
	​

).	[REV06-P030]
[REV06-N07]	High-z Velocity Dispersions	σ
0
	​

≈40−80	km/s	Observed intrinsic dispersion of ISM in z∼1−3 star-forming disks.	Heavily dependent on beam-smearing and spectral resolution corrections.	[REV06-P018], [REV06-P019]
[REV06-N08]	Constant Dust-to-Gas Ratio	δ
GDR
	​

≈100	Dimensionless	Baseline ratio at Solar metallicity used to derive M
gas
	​

 from dust continuum.	Breaks down significantly if T
dust
	​

 varies heavily or metallicity drops.	[REV06-P009], [REV06-P024]
5. What Remained Unknown in 2020
Entry Key	The Gap	Why it Matters	Needed Observation/Model Test	Source Keys
[REV06-U01]	Cosmic Evolution of HI: Direct detection of atomic hydrogen (HI) 21cm emission was restricted to z<0.5.	HI is the ultimate precursor reservoir for the baryon cycle; without it, the replenishment timescale of the molecular phase is theoretical.	Deep integration with next-generation radio arrays (SKA, MeerKAT) to map 21cm at z>1.	[REV06-P016]
[REV06-U02]	Matched Sub-kpc Stellar Kinematics: Lack of high-resolution mapping of the older stellar continuum at high-z.	Exact constraints on stellar mass distributions are required to accurately derive dark matter fractions within R
e
	​

.	Spatially resolved IFU spectroscopy of the rest-optical stellar continuum using JWST.	[REV06-P020]
[REV06-U03]	Gas in Extreme Dwarfs (<10
9
M
⊙
	​

): CO is photo-dissociated and dust continuum fades below detection limits in low-mass, high-z dwarfs.	Low-mass galaxies dominate cosmic volume and reionization; their SF efficiency dictates the faint end of the mass function.	Far-infrared fine-structure line mapping ([CII] 158 μm) as a proxy for total molecular gas.	[REV06-P006], [REV06-P026]
[REV06-U04]	Complete Dense Gas Inventory: Dense gas tracers (HCN, HCO+) were undetectable beyond the local universe for normal MS galaxies.	It is unknown if high SFRs at cosmic noon are driven by higher total gas mass or a higher fraction of dense gas.	Deep ALMA integrations targeting HCN and HCO+ in z∼2 MS galaxies.	[REV06-P017]
[REV06-U05]	Exact Mass-Loading Factors (η): Calculating accurate total mass flux rates of galactic winds suffered orders-of-magnitude uncertainties.	Degeneracies in η prevent definitive testing of specific feedback models (e.g., energy-driven vs. momentum-driven).	Multi-phase (ionized, neutral, molecular) mapping of outflowing gas to constrain density and velocity.	[REV06-P028], [REV06-P031]
[REV06-U06]	CMB Excitation at z>3: The warmer CMB (T
CMB
	​

=2.73(1+z)) excites high-J CO transitions and diminishes line contrast.	Systematically biases the measurement of CO luminosities and dust continuum, potentially skewing gas mass measurements.	Rigorous radiative transfer modeling combined with multi-J CO line ladders to isolate intrinsic excitation.	[REV06-P005]
6. Primary-Citation Harvest
ID	Details
[REV06-P001]	Tacconi, L. J., et al. (2018, ApJ) | title=PHIBSS: Unified Scaling Relations of Gas Depletion Time and Molecular Gas Fractions | DOI:10.3847/1538-4357/aaa4b4; arXiv:1702.01140; ADS:2018ApJ...853..179T | role=calibration | review_locator=Scaling Relations | Master calibration of of $\mu_ and and $t_ spanning ing $0 < .
[REV06-P002]	Genzel, R., et al. (2015, ApJ) | title=Combined CO and Dust Scaling Relations of Depletion Time and Molecular Gas Fractions with Cosmic Time, Specific Star-formation Rate, and Stellar Mass | DOI:10.1088/0004-637X/800/1/20; arXiv:1409.1171; ADS:2015ApJ...800...20G | role=calibration | review_locator=Scaling Relations | Derivation of 2D scaling parameters linking CO and dust fluxes.
[REV06-P003]	Genzel, R., et al. (2010, MNRAS) | title=A study of the gas-star formation relation over cosmic time | DOI:10.1111/j.1365-2966.2010.16969.x; arXiv:1003.5180; ADS:2010MNRAS.407.2091G | role=observation | review_locator=Star-Formation Laws | Establishes the integrated near-linear Kennicutt-Schmidt law over three orders of magnitude.
[REV06-P004]	Tacconi, L. J., et al. (2010, Nature) | title=High molecular gas fractions in normal massive star-forming galaxies in the young Universe | DOI:none; arXiv:1003.2349; ADS:2010Natur.463..781T | role=observation | review_locator=Gas Fractions | First major demonstration of 30-50% molecular gas fractions at at $z \si.
[REV06-P005]	Tacconi, L. J., et al. (2013, ApJ) | title=Phibss: Molecular Gas Content and Scaling Relations in z~1-3 Massive, Main-sequence Star-forming Galaxies | DOI:10.1088/0004-637X/768/1/74; arXiv:1211.5743; ADS:2013ApJ...768...74T | role=observation | review_locator=Gas Fractions | Expands high-z gas fraction baselines on the MS via the IRAM PHIBSS large program.
[REV06-P006]	Bolatto, A. D., Wolfire, M., & Leroy, A. K. (2013, ARA&A) | title=The CO-to-H2 Conversion Factor | DOI:10.1146/annurev-astro-082812-140944; arXiv:1301.3498; ADS:2013ARA&A..51..207B | role=review_synthesis | review_locator=Conversion Factors | Foundational baseline calibration for for $\alpha and its metallicity dependence.
[REV06-P007]	Bigiel, F., et al. (2008, AJ) | title=The Star Formation Law in Nearby Galaxies on Sub-Kpc Scales | DOI:10.1088/0004-6256/136/6/2846; arXiv:0808.1851; ADS:2008AJ....136.2846B | role=observation | review_locator=Star-Formation Laws | Demonstrates saturation of HI and strict linear correlation of SFR with molecular gas locally.
[REV06-P008]	Genzel, R., et al. (2012, ApJ) | title=The Metallicity Dependence of the CO->H2 Conversion Factor in z>=1 Star-Forming Galaxies | DOI:10.1088/0004-637X/746/1/69; arXiv:1112.4411; ADS:2012ApJ...746...69G | role=calibration | review_locator=Conversion Factors | Empirically applies the Bolatto-style metallicity correction to high-z samples.
[REV06-P009]	Scoville, N., et al. (2016, ApJ) | title=ISM Masses and the Star formation Law at Z=1 to 6: ALMA Observations of Dust Continuum in 145 Galaxies in the COSMOS Survey Field | DOI:10.3847/0004-637X/820/2/83; arXiv:1512.00041; ADS:2016ApJ...820...83S | role=calibration | review_locator=Dust Tracers | Establishes optically thin Rayleigh-Jeans dust continuum as a universal proxy for for $M_.
[REV06-P010]	Speagle, J. S., et al. (2014, ApJS) | title=A Highly Consistent Framework for the Evolution of the Star-Forming "Main Sequence" from z ~ 0-6 | DOI:10.1088/0067-0049/214/2/15; arXiv:1405.2041; ADS:2014ApJS..214...15S | role=calibration | review_locator=Main Sequence | Baseline formulation of the MS ridgeline utilized throughout the review.
[REV06-P011]	Whitaker, K. E., et al. (2014, ApJ) | title=Constraining the Low-mass Slope of the Star-forming Main Sequence at 0.5 < z < 2.5 | DOI:10.1088/0004-637X/795/2/104; arXiv:1407.1843; ADS:2014ApJ...795..104W | role=observation | review_locator=Main Sequence | Defines the mass-dependent bending and slope of the SFMS.
[REV06-P012]	Daddi, E., et al. (2007, ApJ) | title=Multi-wavelength study of massive galaxies at z~2. I. Star formation and galaxy growth | DOI:none; arXiv:0705.2831; ADS:2007ApJ...670..156D | role=observation | review_locator=Main Sequence | Early identification of the tight relationship between SFR and and at cosmic noon.
[REV06-P013]	Noeske, K. G., et al. (2007, ApJ) | title=Star Formation in AEGIS Field Galaxies since z=1.1: The Dominance of Gradually Declining Star Formation, and the Main Sequence of Star-forming Galaxies | DOI:none; arXiv:astro-ph/0701924; ADS:2007ApJ...660L..43N | role=observation | review_locator=Main Sequence | Coined the term "Main Sequence" and proposed continuous regulatory growth over bursts.
[REV06-P014]	Decarli, R., et al. (2019, ApJ) | title=The ALMA Spectroscopic Survey in the HUDF: CO Luminosity Functions and the Molecular Gas Content of Galaxies through Cosmic History | DOI:10.3847/1538-4357/ab30fe; arXiv:1903.09164; ADS:2019ApJ...882..138D | role=observation | review_locator=Gas Fractions | Volume-limited blank-field ALMA scan confirming the peak of cosmic molecular gas density.
[REV06-P015]	Daddi, E., et al. (2010, ApJ) | title=Different Star Formation Laws for Disks Versus Starbursts at Low and High Redshifts | DOI:none; arXiv:1003.2646; ADS:2010ApJ...714L.118D | role=observation | review_locator=Starbursts vs MS | Key paper arguing for a strict bimodal star-formation law (MS vs mergers).
[REV06-P016]	Saintonge, A., et al. (2011, MNRAS) | title=COLD GASS, an IRAM legacy survey of molecular gas in massive galaxies - I. Relations between H2, HI, stellar content and structural properties | DOI:10.1111/j.1365-2966.2011.18822.x; arXiv:1104.0019; ADS:2011MNRAS.415...32S | role=observation | review_locator=Local Benchmarks | Definitive z=0 survey separating the roles of HI and and on the local MS.
[REV06-P017]	Kennicutt, R. C. (1998, ApJ) | title=The Global Schmidt Law in Star-forming Galaxies | DOI:none; arXiv:astro-ph/9807187; ADS:1998ApJ...498..541K | role=review_synthesis | review_locator=Star-Formation Laws | The fundamental Kennicutt-Schmidt non-linear relation between global gas density and SFR.
[REV06-P018]	Förster Schreiber, N. M., et al. (2009, ApJ) | title=The SINS Survey: SINFONI Integral Field Spectroscopy of z~2 Star-forming Galaxies | DOI:10.1088/0004-637X/706/2/1364; arXiv:0903.1872; ADS:2009ApJ...706.1364F | role=observation | review_locator=Kinematics | Groundbreaking IFU survey revealing rotating, turbulent, clumpy disks at z~2.
[REV06-P019]	Wisnioski, E., et al. (2015, ApJ) | title=The KMOS3D Survey: Design, First Results, and the Evolution of Galaxy Kinematics from 0.7<=z<=2.7 | DOI:10.1088/0004-637X/799/2/209; arXiv:1409.6791; ADS:2015ApJ...799..209W | role=observation | review_locator=Kinematics | Characterizes the continuous evolution of ionized gas velocity dispersion across cosmic time.
[REV06-P020]	Genzel, R., et al. (2017, Nature) | title=Strongly baryon-dominated disk galaxies at the peak of galaxy formation ten billion years ago | DOI:10.1038/nature21685; arXiv:1703.04310; ADS:2017Natur.543..397G | role=observation | review_locator=Kinematics | Argues that high-z central rotation curves lack deep dark-matter potentials.
[REV06-P021]	Magdis, G. E., et al. (2012, ApJ) | title=The Dust and Gas Properties of z ~ 1.2 and 2.5 Star-forming Galaxies from Herschel and ALMA | DOI:10.1088/0004-637X/760/1/6; arXiv:1208.0664; ADS:2012ApJ...760....6M | role=observation | review_locator=Dust Tracers | Uses Herschel to map dust mass and derive gas depletion times mirroring CO methods.
[REV06-P022]	Genzel, R., et al. (2011, ApJ) | title=The SINS Survey of z~2 Galaxy Kinematics: Properties of the Giant Star-forming Clumps | DOI:10.1088/0004-637X/733/2/101; arXiv:1011.5360; ADS:2011ApJ...733..101G | role=observation | review_locator=Disk Clumps | Analysis of Toomre instability leading to to $10^8-10^9 M_ clumps.
[REV06-P023]	Rodighiero, G., et al. (2011, ApJ) | title=The Lesser Role of Starbursts in Star Formation at z = 2 | DOI:10.1088/2041-8205/739/2/L40; arXiv:1108.0933; ADS:2011ApJ...739L..40R | role=observation | review_locator=Starbursts vs MS | Demonstrates statistically that MS galaxies, not extreme starbursts, build the bulk of cosmic stellar mass.
[REV06-P024]	Draine, B. T., & Li, A. (2007, ApJ) | title=Infrared Emission from Interstellar Dust. IV. The Silicate-Graphite-PAH Model in the Post-Spitzer Era | DOI:none; arXiv:astro-ph/0608003; ADS:2007ApJ...657..810D | role=analytic_theory | review_locator=Dust Tracers | Core physical modeling for dust emissivity (ty ($\kapp) utilized in dust-to-gas conversions.
[REV06-P025]	Berta, S., et al. (2016, A&A) | title=The dust to gas ratio of star-forming galaxies at z~2 | DOI:10.1051/0004-6361/201527746; arXiv:1601.06666; ADS:2016A&A...587A..73B | role=calibration | review_locator=Dust Tracers | High-z calibration verifying the metallicity-dependent dust-to-gas ratio.
[REV06-P026]	Accurso, G., et al. (2017, MNRAS) | title=Deriving a multivariate alpha_CO conversion function using the [CII]/CO(1-0) ratio and its application to dwarf galaxies | DOI:10.1093/mnras/stx1451; arXiv:1706.01503; ADS:2017MNRAS.470.4750A | role=calibration | review_locator=Conversion Factors | Demonstrates that hat $\alpha requires parameters beyond just metallicity, specifically radiation field intensity.
[REV06-P027]	Saintonge, A., et al. (2013, ApJ) | title=The Evolution of the Star Formation Efficiency of Galaxies with Cosmic Time | DOI:10.1088/0004-637X/778/1/2; arXiv:1308.5973; ADS:2013ApJ...778....2S | role=observation | review_locator=Scaling Relations | Shows a smoothly varying efficiency metric crossing between MS and starburst populations.
[REV06-P028]	Bouché, N., et al. (2010, ApJ) | title=The Impact of Cold Gas Accretion Above a Mass Floor on Galaxy Scaling Relations | DOI:10.1088/0004-637X/718/2/1001; arXiv:0912.1858; ADS:2010ApJ...718.1001B | role=analytic_theory | review_locator=Regulator Models | Fundamental theoretical outline of the gas-regulator "bathtub" model balancing infall and SFR.
[REV06-P029]	Bournaud, F., et al. (2007, ApJ) | title=Formation of Bulges by Giant Clump Migration in gas-rich galaxies | DOI:none; arXiv:astro-ph/0702581; ADS:2007ApJ...670..237B | role=hydrodynamic_simulation | review_locator=Disk Clumps | Proposes that high-z clumps survive feedback and migrate to form bulges.
[REV06-P030]	Dekel, A., et al. (2009, Nature) | title=Cold streams in early massive hot haloes as the main mode of galaxy formation | DOI:10.1038/nature07648; arXiv:0808.0553; ADS:2009Natur.457..451D | role=analytic_theory | review_locator=Regulator Models | Cosmological driver for Toomre instability via continuous cold-stream accretion in the cosmic web.
[REV06-P031]	Lilly, S. J., et al. (2013, ApJ) | title=Gas Regulation of Galaxies: The Evolution of the Cosmic Specific Star Formation Rate, the Metallicity-Mass-Star-Formation Rate Relation, and the Stellar Mass Function | DOI:10.1088/0004-637X/772/2/119; arXiv:1305.6931; ADS:2013ApJ...772..119L | role=analytic_theory | review_locator=Regulator Models | Develops the comprehensive steady-state regulator linking mass, metallicity, and SFR.
[REV06-P032]	Krumholz, M. R., & Burkert, A. (2010, ApJ) | title=Energy Balance and the Structure of Star-forming High-z Disks | DOI:10.1088/0004-637X/724/1/895; arXiv:1005.1663; ADS:2010ApJ...724..895K | role=analytic_theory | review_locator=Kinematics | Argues that gravitational instabilities (not feedback) maintain high-z velocity dispersions.
[REV06-P033]	Zolotov, A., et al. (2015, MNRAS) | title=Compaction and quenching of high-z galaxies in cosmological simulations | DOI:10.1093/mnras/stv740; arXiv:1412.4783; ADS:2015MNRAS.450.2327Z | role=hydrodynamic_simulation | review_locator=Morphological Evolution | Connects gas-rich disk instabilities to central compaction events and subsequent quenching.
[REV06-P034]	Krumholz, M. R., Dekel, A., & McKee, C. F. (2012, ApJ) | title=A Universal, Local Star Formation Law in Galactic Clouds, Nearby Galaxies, High-redshift Disks, and Starbursts | DOI:10.1088/0004-637X/745/1/69; arXiv:1109.4150; ADS:2012ApJ...745...69K | role=analytic_theory | review_locator=Star-Formation Laws | Demonstrates a universal efficiency of of $\si per free-fall time across diverse scales.
[REV06-P035]	Davé, R., et al. (2012, MNRAS) | title=An analytic model for the evolution of the stellar, gas and metal content of galaxies | DOI:10.1111/j.1365-2966.2011.20148.x; arXiv:1112.5435; ADS:2012MNRAS.421...98D | role=analytic_theory | review_locator=Regulator Models | Connects cosmological hydrodynamics to the equilibrium bathtub scaling laws.
[REV06-P036]	Bothwell, M. S., et al. (2013, MNRAS) | title=A mass-metallicity-molecular gas relation for local star-forming galaxies | DOI:10.1093/mnras/stt817; arXiv:1305.2152; ADS:2013MNRAS.433.1425B | role=observation | review_locator=Scaling Relations | Observational evidence linking cold gas content to the scatter in the mass-metallicity relation.
[REV06-P037]	Förster Schreiber, N. M., et al. (2018, ApJS) | title=The SINS/zC-SINF Survey of z ~ 2 Galaxy Kinematics: SINFONI Adaptive Optics-assisted Data and Kiloparsec-scale Emission-line Properties | DOI:10.3847/1538-4365/aadd49; arXiv:1807.04738; ADS:2018ApJS..238...21F | role=observation | review_locator=Kinematics | Sub-kpc resolution IFU verification of high-z disk structure and rotation bounds.
[REV06-P038]	Walter, F., et al. (2014, ApJ) | title=The Cold Gas Content of Bulge-dominated Galaxies | DOI:none; arXiv:1307.7126; ADS:2014ApJ...782...79W | role=observation | review_locator=Gas Fractions | Tracks the depletion of gas across the MS toward the passive (quenched) sequence.
[REV06-P039]	Tacchella, S., et al. (2016, MNRAS) | title=The confinement of star-forming galaxies into a main sequence through episodes of gas compaction, starburst and quenching | DOI:10.1093/mnras/stw131; arXiv:1509.00017; ADS:2016MNRAS.457.2790T | role=hydrodynamic_simulation | review_locator=Regulator Models | Models oscillation across the MS driven by gas inflows and compaction.
[REV06-P040]	Carilli, C. L., & Walter, F. (2013, ARA&A) | title=Cool Gas in High-Redshift Galaxies | DOI:10.1146/annurev-astro-082812-140953; arXiv:1301.0371; ADS:2013ARA&A..51..105C | role=review_synthesis | review_locator=Tracers and Evolution | Precursor review detailing early ALMA and JVLA high-z gas studies.
[REV06-P041]	Narayanan, D., et al. (2012, MNRAS) | title=A general model for the CO-H2 conversion factor in galaxies with applications to the star formation law | DOI:10.1111/j.1365-2966.2012.20536.x; arXiv:1110.6601; ADS:2012MNRAS.421.3127N | role=hydrodynamic_simulation | review_locator=Conversion Factors | Simulation showing ing $\alpha variation governed by both metallicity and internal gas velocity dispersion.
[REV06-P042]	Leroy, A. K., et al. (2011, ApJ) | title=The CO-to-H2 Conversion Factor from Infrared Dust Emission Across the Local Group | DOI:10.1088/0004-637X/737/1/12; arXiv:1102.4618; ADS:2011ApJ...737...12L | role=observation | review_locator=Conversion Factors | Calibrates tes $\alpha locally by comparing CO emission directly against dust mass mappings.
[REV06-P043]	Utomo, D., et al. (2018, ApJ) | title=The Star Formation Efficiency per Free-fall Time in Nearby Galaxies | DOI:10.3847/2041-8213/aacc66; arXiv:1806.07921; ADS:2018ApJ...861L..18U | role=observation | review_locator=Star-Formation Laws | Direct mapping confirming the the $\si per free-fall time efficiency in local GMCs.
[REV06-P044]	Elmegreen, B. G., et al. (2009, ApJ) | title=Clump Cluster Galaxies at z~2: Characteristics of Star Formation in Thick Disks | DOI:none; arXiv:0907.0177; ADS:2009ApJ...701..306E | role=observation | review_locator=Disk Clumps | Links thick disk morphologies directly to massive Toomre-unstable regions.
[REV06-P045]	Peng, Y.-j., et al. (2010, ApJ) | title=Mass and Environment as Drivers of Galaxy Evolution in SDSS and zCOSMOS and the Origin of the Schechter Function | DOI:10.1088/0004-637X/721/1/193; arXiv:1003.4747; ADS:2010ApJ...721..193P | role=observation | review_locator=Main Sequence | Fundamental phenomenological framework defining mass-quenching vs environment-quenching paths.
7. DO_NOT_USE_UNVERIFIED

UNCITED_NOT_USABLE | candidate or claim | JWST rest-optical morphologies of early galaxies | exclusion reason: Post-2020 technological capability. Any claims of JWST resolving z>5 disk kinematics must be quarantined from the 2020 Tacconi baseline.

UNCITED_NOT_USABLE | candidate or claim | Post-2020 ALMA large programs (e.g., REBELS, ASPECS later data releases) | exclusion reason: Literature boundary violation. Exclude all specific quantitative yields from ALMA surveys published 2021-2026.

UNCITED_NOT_USABLE | candidate or claim | CO luminosity (L
CO
′
	​

) is perfectly synonymous with H
2
	​

 mass without applying α
CO
	​

. | exclusion reason: Severe physical conflation explicitly forbidden by the review's treatment of phase and shielding physics.

UNCITED_NOT_USABLE | candidate or claim | Dust continuum gives gas mass without metallicity-dependent dust-to-gas calibration. | exclusion reason: Overbroad generalization that fails catastrophically for sub-solar metallicity dwarf galaxies.

UNCITED_NOT_USABLE | candidate or claim | One single depletion time (t
dep
	​

) applies to all galaxies at a given redshift. | exclusion reason: Contradicts the bivariate dependence of t
dep
	​

 on both redshift and the galaxy's position relative to the main sequence (ΔMS).

UNCITED_NOT_USABLE | candidate or claim | All high-z disks are unstable clump systems. | exclusion reason: Ignores the continuous nature of disk compaction and stabilization; low-mass disks may not fragment via the same VDI regime.

UNCITED_NOT_USABLE | candidate or claim | Matching gas-fraction scaling uniquely validates one specific bathtub/regulator model. | exclusion reason: Degeneracies in mass-loading factors and pristine inflow rates mean scaling relations are a necessary, but not uniquely sufficient, proof of any single feedback model.

UNCITED_NOT_USABLE | candidate or claim | AGN-centric models as the primary driver of main sequence evolution | exclusion reason: Boundary violation; Tacconi 2020 isolates normal SFMS galaxies. Exclude AGN fueling, SMBH accretion physics, and AGN-only feedback mechanisms.

8. Review and Source Identity Ledger
ID	Details
[REV06-R00]	Tacconi, L. J., Genzel, R., & Sternberg, A. (2020, ARA&A) | DOI:10.1146/annurev-astro-082812-141034; arXiv:2003.06245; ADS:2020ARA&A..58..157T | role=review_synthesis | review_locator=Entire Review | Master review characterizing the cold ISM and MS scaling relations.
[REV06-P001]	Tacconi, L. J., et al. (2018, ApJ) | DOI:10.3847/1538-4357/aaa4b4; arXiv:1702.01140; ADS:2018ApJ...853..179T | role=calibration | review_locator=Scaling Relations | Master calibration of of $\mu_{ and nd $t_{ spanning ng $0 < z.
[REV06-P002]	Genzel, R., et al. (2015, ApJ) | DOI:10.1088/0004-637X/800/1/20; arXiv:1409.1171; ADS:2015ApJ...800...20G | role=calibration | review_locator=Scaling Relations | Derivation of 2D scaling parameters linking CO and dust fluxes.
[REV06-P003]	Genzel, R., et al. (2010, MNRAS) | DOI:10.1111/j.1365-2966.2010.16969.x; arXiv:1003.5180; ADS:2010MNRAS.407.2091G | role=observation | review_locator=Star-Formation Laws | Establishes the integrated near-linear Kennicutt-Schmidt law over three orders of magnitude.
[REV06-P004]	Tacconi, L. J., et al. (2010, Nature) | DOI:none; arXiv:1003.2349; ADS:2010Natur.463..781T | role=observation | review_locator=Gas Fractions | First major demonstration of 30-50% molecular gas fractions at at $z \sim.
[REV06-P005]	Tacconi, L. J., et al. (2013, ApJ) | DOI:10.1088/0004-637X/768/1/74; arXiv:1211.5743; ADS:2013ApJ...768...74T | role=observation | review_locator=Gas Fractions | Expands high-z gas fraction baselines on the MS via the IRAM PHIBSS large program.
[REV06-P006]	Bolatto, A. D., Wolfire, M., & Leroy, A. K. (2013, ARA&A) | DOI:10.1146/annurev-astro-082812-140944; arXiv:1301.3498; ADS:2013ARA&A..51..207B | role=review_synthesis | review_locator=Conversion Factors | Foundational baseline calibration for or $\alpha_ and its metallicity dependence.
[REV06-P007]	Bigiel, F., et al. (2008, AJ) | DOI:10.1088/0004-6256/136/6/2846; arXiv:0808.1851; ADS:2008AJ....136.2846B | role=observation | review_locator=Star-Formation Laws | Demonstrates saturation of HI and strict linear correlation of SFR with molecular gas locally.
[REV06-P008]	Genzel, R., et al. (2012, ApJ) | DOI:10.1088/0004-637X/746/1/69; arXiv:1112.4411; ADS:2012ApJ...746...69G | role=calibration | review_locator=Conversion Factors | Empirically applies the Bolatto-style metallicity correction to high-z samples.
[REV06-P009]	Scoville, N., et al. (2016, ApJ) | DOI:10.3847/0004-637X/820/2/83; arXiv:1512.00041; ADS:2016ApJ...820...83S | role=calibration | review_locator=Dust Tracers | Establishes optically thin Rayleigh-Jeans dust continuum as a universal proxy for or $M_{.
[REV06-P010]	Speagle, J. S., et al. (2014, ApJS) | DOI:10.1088/0067-0049/214/2/15; arXiv:1405.2041; ADS:2014ApJS..214...15S | role=calibration | review_locator=Main Sequence | Baseline formulation of the MS ridgeline utilized throughout the review.
[REV06-P011]	Whitaker, K. E., et al. (2014, ApJ) | DOI:10.1088/0004-637X/795/2/104; arXiv:1407.1843; ADS:2014ApJ...795..104W | role=observation | review_locator=Main Sequence | Defines the mass-dependent bending and slope of the SFMS.
[REV06-P012]	Daddi, E., et al. (2007, ApJ) | DOI:none; arXiv:0705.2831; ADS:2007ApJ...670..156D | role=observation | review_locator=Main Sequence | Early identification of the tight relationship between SFR and nd at cosmic noon.
[REV06-P013]	Noeske, K. G., et al. (2007, ApJ) | DOI:none; arXiv:astro-ph/0701924; ADS:2007ApJ...660L..43N | role=observation | review_locator=Main Sequence | Coined the term "Main Sequence" and proposed continuous regulatory growth over bursts.
[REV06-P014]	Decarli, R., et al. (2019, ApJ) | DOI:10.3847/1538-4357/ab30fe; arXiv:1903.09164; ADS:2019ApJ...882..138D | role=observation | review_locator=Gas Fractions | Volume-limited blank-field ALMA scan confirming the peak of cosmic molecular gas density.
[REV06-P015]	Daddi, E., et al. (2010, ApJ) | DOI:none; arXiv:1003.2646; ADS:2010ApJ...714L.118D | role=observation | review_locator=Starbursts vs MS | Key paper arguing for a strict bimodal star-formation law (MS vs mergers).
[REV06-P016]	Saintonge, A., et al. (2011, MNRAS) | DOI:10.1111/j.1365-2966.2011.18822.x; arXiv:1104.0019; ADS:2011MNRAS.415...32S | role=observation | review_locator=Local Benchmarks | Definitive z=0 survey separating the roles of HI and nd on the local MS.
[REV06-P017]	Kennicutt, R. C. (1998, ApJ) | DOI:none; arXiv:astro-ph/9807187; ADS:1998ApJ...498..541K | role=review_synthesis | review_locator=Star-Formation Laws | The fundamental Kennicutt-Schmidt non-linear relation between global gas density and SFR.
[REV06-P018]	Förster Schreiber, N. M., et al. (2009, ApJ) | DOI:10.1088/0004-637X/706/2/1364; arXiv:0903.1872; ADS:2009ApJ...706.1364F | role=observation | review_locator=Kinematics | Groundbreaking IFU survey revealing rotating, turbulent, clumpy disks at z~2.
[REV06-P019]	Wisnioski, E., et al. (2015, ApJ) | DOI:10.1088/0004-637X/799/2/209; arXiv:1409.6791; ADS:2015ApJ...799..209W | role=observation | review_locator=Kinematics | Characterizes the continuous evolution of ionized gas velocity dispersion across cosmic time.
[REV06-P020]	Genzel, R., et al. (2017, Nature) | DOI:10.1038/nature21685; arXiv:1703.04310; ADS:2017Natur.543..397G | role=observation | review_locator=Kinematics | Argues that high-z central rotation curves lack deep dark-matter potentials.
[REV06-P021]	Magdis, G. E., et al. (2012, ApJ) | DOI:10.1088/0004-637X/760/1/6; arXiv:1208.0664; ADS:2012ApJ...760....6M | role=observation | review_locator=Dust Tracers | Uses Herschel to map dust mass and derive gas depletion times mirroring CO methods.
[REV06-P022]	Genzel, R., et al. (2011, ApJ) | DOI:10.1088/0004-637X/733/2/101; arXiv:1011.5360; ADS:2011ApJ...733..101G | role=observation | review_locator=Disk Clumps | Analysis of Toomre instability leading to to $10^8-10^9 M_\ clumps.
[REV06-P023]	Rodighiero, G., et al. (2011, ApJ) | DOI:10.1088/2041-8205/739/2/L40; arXiv:1108.0933; ADS:2011ApJ...739L..40R | role=observation | review_locator=Starbursts vs MS | Demonstrates statistically that MS galaxies, not extreme starbursts, build the bulk of cosmic stellar mass.
[REV06-P024]	Draine, B. T., & Li, A. (2007, ApJ) | DOI:none; arXiv:astro-ph/0608003; ADS:2007ApJ...657..810D | role=analytic_theory | review_locator=Dust Tracers | Core physical modeling for dust emissivity (y ($\kappa) utilized in dust-to-gas conversions.
[REV06-P025]	Berta, S., et al. (2016, A&A) | DOI:10.1051/0004-6361/201527746; arXiv:1601.06666; ADS:2016A&A...587A..73B | role=calibration | review_locator=Dust Tracers | High-z calibration verifying the metallicity-dependent dust-to-gas ratio.
[REV06-P026]	Accurso, G., et al. (2017, MNRAS) | DOI:10.1093/mnras/stx1451; arXiv:1706.01503; ADS:2017MNRAS.470.4750A | role=calibration | review_locator=Conversion Factors | Demonstrates that at $\alpha_ requires parameters beyond just metallicity, specifically radiation field intensity.
[REV06-P027]	Saintonge, A., et al. (2013, ApJ) | DOI:10.1088/0004-637X/778/1/2; arXiv:1308.5973; ADS:2013ApJ...778....2S | role=observation | review_locator=Scaling Relations | Shows a smoothly varying efficiency metric crossing between MS and starburst populations.
[REV06-P028]	Bouché, N., et al. (2010, ApJ) | DOI:10.1088/0004-637X/718/2/1001; arXiv:0912.1858; ADS:2010ApJ...718.1001B | role=analytic_theory | review_locator=Regulator Models | Fundamental theoretical outline of the gas-regulator "bathtub" model balancing infall and SFR.
[REV06-P029]	Bournaud, F., et al. (2007, ApJ) | DOI:none; arXiv:astro-ph/0702581; ADS:2007ApJ...670..237B | role=hydrodynamic_simulation | review_locator=Disk Clumps | Proposes that high-z clumps survive feedback and migrate to form bulges.
[REV06-P030]	Dekel, A., et al. (2009, Nature) | DOI:10.1038/nature07648; arXiv:0808.0553; ADS:2009Natur.457..451D | role=analytic_theory | review_locator=Regulator Models | Cosmological driver for Toomre instability via continuous cold-stream accretion in the cosmic web.
[REV06-P031]	Lilly, S. J., et al. (2013, ApJ) | DOI:10.1088/0004-637X/772/2/119; arXiv:1305.6931; ADS:2013ApJ...772..119L | role=analytic_theory | review_locator=Regulator Models | Develops the comprehensive steady-state regulator linking mass, metallicity, and SFR.
[REV06-P032]	Krumholz, M. R., & Burkert, A. (2010, ApJ) | DOI:10.1088/0004-637X/724/1/895; arXiv:1005.1663; ADS:2010ApJ...724..895K | role=analytic_theory | review_locator=Kinematics | Argues that gravitational instabilities (not feedback) maintain high-z velocity dispersions.
[REV06-P033]	Zolotov, A., et al. (2015, MNRAS) | DOI:10.1093/mnras/stv740; arXiv:1412.4783; ADS:2015MNRAS.450.2327Z | role=hydrodynamic_simulation | review_locator=Morphological Evolution | Connects gas-rich disk instabilities to central compaction events and subsequent quenching.
[REV06-P034]	Krumholz, M. R., Dekel, A., & McKee, C. F. (2012, ApJ) | DOI:10.1088/0004-637X/745/1/69; arXiv:1109.4150; ADS:2012ApJ...745...69K | role=analytic_theory | review_locator=Star-Formation Laws | Demonstrates a universal efficiency of of $\sim per free-fall time across diverse scales.
[REV06-P035]	Davé, R., et al. (2012, MNRAS) | DOI:10.1111/j.1365-2966.2011.20148.x; arXiv:1112.5435; ADS:2012MNRAS.421...98D | role=analytic_theory | review_locator=Regulator Models | Connects cosmological hydrodynamics to the equilibrium bathtub scaling laws.
[REV06-P036]	Bothwell, M. S., et al. (2013, MNRAS) | DOI:10.1093/mnras/stt817; arXiv:1305.2152; ADS:2013MNRAS.433.1425B | role=observation | review_locator=Scaling Relations | Observational evidence linking cold gas content to the scatter in the mass-metallicity relation.
[REV06-P037]	Förster Schreiber, N. M., et al. (2018, ApJS) | DOI:10.3847/1538-4365/aadd49; arXiv:1807.04738; ADS:2018ApJS..238...21F | role=observation | review_locator=Kinematics | Sub-kpc resolution IFU verification of high-z disk structure and rotation bounds.
[REV06-P038]	Walter, F., et al. (2014, ApJ) | DOI:none; arXiv:1307.7126; ADS:2014ApJ...782...79W | role=observation | review_locator=Gas Fractions | Tracks the depletion of gas across the MS toward the passive (quenched) sequence.
[REV06-P039]	Tacchella, S., et al. (2016, MNRAS) | DOI:10.1093/mnras/stw131; arXiv:1509.00017; ADS:2016MNRAS.457.2790T | role=hydrodynamic_simulation | review_locator=Regulator Models | Models oscillation across the MS driven by gas inflows and compaction.
[REV06-P040]	Carilli, C. L., & Walter, F. (2013, ARA&A) | DOI:10.1146/annurev-astro-082812-140953; arXiv:1301.0371; ADS:2013ARA&A..51..105C | role=review_synthesis | review_locator=Tracers and Evolution | Precursor review detailing early ALMA and JVLA high-z gas studies.
[REV06-P041]	Narayanan, D., et al. (2012, MNRAS) | DOI:10.1111/j.1365-2966.2012.20536.x; arXiv:1110.6601; ADS:2012MNRAS.421.3127N | role=hydrodynamic_simulation | review_locator=Conversion Factors | Simulation showing ng $\alpha_ variation governed by both metallicity and internal gas velocity dispersion.
[REV06-P042]	Leroy, A. K., et al. (2011, ApJ) | DOI:10.1088/0004-637X/737/1/12; arXiv:1102.4618; ADS:2011ApJ...737...12L | role=observation | review_locator=Conversion Factors | Calibrates es $\alpha_ locally by comparing CO emission directly against dust mass mappings.
[REV06-P043]	Utomo, D., et al. (2018, ApJ) | DOI:10.3847/2041-8213/aacc66; arXiv:1806.07921; ADS:2018ApJ...861L..18U | role=observation | review_locator=Star-Formation Laws | Direct mapping confirming the he $\sim per free-fall time efficiency in local GMCs.
[REV06-P044]	Elmegreen, B. G., et al. (2009, ApJ) | DOI:none; arXiv:0907.0177; ADS:2009ApJ...701..306E | role=observation | review_locator=Disk Clumps | Links thick disk morphologies directly to massive Toomre-unstable regions.
[REV06-P045]	Peng, Y.-j., et al. (2010, ApJ) | DOI:10.1088/0004-637X/721/1/193; arXiv:1003.4747; ADS:2010ApJ...721..193P | role=observation | review_locator=Main Sequence | Fundamental phenomenological framework defining mass-quenching vs environment-quenching paths.

REVIEW_BASE_06_DR_COMPLETE_REFERENCE_ONLY

## Captured external source anchors

- arxiv.org [2003.06245] The Evolution of the Star-forming Interstellar Medium across Cosmic Time Opens in a new window — https://arxiv.org/abs/2003.06245
- pmc.ncbi.nlm.nih.gov High-redshift star formation in the Atacama large millimetre/submillimetre array era - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC7813222/
- royalsocietypublishing.org High-redshift star formation in the Atacama large millimetre/submillimetre array era Opens in a new window — https://royalsocietypublishing.org/rsos/article/7/12/200556/95459/High-redshift-star-formation-in-the-Atacama-large
- arxiv.org The ALPINE-ALMA [Cii] survey: Molecular gas budget in the Early Universe as traced by [Cii] - arXiv Opens in a new window — https://arxiv.org/pdf/2004.10771
- arxiv.org Resolved Profiles of Stellar Mass, Star Formation Rate, and Predicted CO-to-H$_2$ Conversion Factor Across Thousands of Local Ga - arXiv Opens in a new window — https://arxiv.org/pdf/2510.05214
- homepages.usm.uni-muenchen.de Evolution and Dynamics of Cold Gas in Simulated Galaxies Opens in a new window — https://homepages.usm.uni-muenchen.de/CAST/wp/download/ma_hagedorn-2.pdf
- arxiv.org arXiv:2203.00689v1 [astro-ph.GA] 1 Mar 2022 Opens in a new window — https://arxiv.org/pdf/2203.00689
- ora.ox.ac.uk Kiloparsec view of a typical star-forming galaxy when the Universe was ∼1 Gyr old - II. Regular rotating disk and evidence for Opens in a new window — https://ora.ox.ac.uk/objects/uuid:6e0df24c-189c-46f8-ad30-7056979c9887/files/rws859j09d
- academic.oup.com general model for the CO–H2 conversion factor in galaxies with applications to the star formation law - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/421/4/3127/1090206
- scribd.com CO(1–0) Emission in High-z Galaxies | PDF - Scribd Opens in a new window — https://www.scribd.com/document/909136733/Jansky-Very-Large
- epj-conferences.org HI and H2 gas evolution over cosmic times: ColdSIM - EPJ Web of Conferences Opens in a new window — https://www.epj-conferences.org/articles/epjconf/pdf/2022/01/epjconf_mmUniverse2021_00029.pdf
- academic.oup.com Dust attenuation, dust content, and geometry of star-forming galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/524/3/4128/56261258/stad2066.pdf
- arxiv.org Unveiling the Main Sequence to Starburst Transition Region with a Sample of Intermediate Redshift Luminous Infrared Galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/2202.10576
- arxiv.org Molecular gas properties of Q1700-MD94: a massive, main-sequence galaxy at z ≈ 2 - arXiv Opens in a new window — https://arxiv.org/pdf/2109.01684
- arxiv.org NOEMA^"3D": extended CO, [C I] and dust in massive star-forming main sequence galaxies at cosmic noon - arXiv Opens in a new window — https://arxiv.org/html/2604.18504v3
- researchgate.net Molecular gas budget of strongly magnified low-mass star-forming galaxies at cosmic noon Opens in a new window — https://www.researchgate.net/publication/387052767_Molecular_gas_budget_of_strongly_magnified_low-mass_star-forming_galaxies_at_cosmic_noon
- ricerca.sns.it Interstellar dust in galaxies in the Epoch of Reionization - Scuola Normale Superiore Opens in a new window — https://ricerca.sns.it/retrieve/de795c1e-391d-471a-8524-f9dc1b5ea489/Sommovigo_Thesis_rev.pdf
- arxiv.org Gas Fraction and Depletion Time Drive the Main-Sequence Scatter in Massive Galaxies at z∼1.5 - arXiv Opens in a new window — https://arxiv.org/html/2605.23662v1
- academic.oup.com Star formation efficiency across large-scale galactic environments - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/528/3/4393/7590826
- pure.ed.ac.uk ALMA measures rapidly depleted molecular gas reservoirs in massive quiescent galaxies at z~1.5 - Account Opens in a new window — https://www.pure.ed.ac.uk/ws/files/331405338/2012.01433v1.pdf
- ricerca.sns.it The ALMA Reionization Era Bright Emission Line Survey: The molecular gas content of galaxies at z Opens in a new window — https://ricerca.sns.it/retrieve/32811180-1be1-4454-8286-49ae681745fd/aa47281-23.pdf
- academic.oup.com VINTERGATAN IV: Cosmic phases of star formation in Milky Way-like galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/516/2/2272/47756736/stac2368.pdf
- arxiv.org Built to Rest: The Evolving Star-Forming Main Sequence Requires Episodic Quiescence or Late Assembly - arXiv Opens in a new window — https://arxiv.org/html/2605.02997v1
- arxiv.org arXiv:2104.12794v1 [astro-ph.GA] 26 Apr 2021 Opens in a new window — https://arxiv.org/pdf/2104.12794
- indico.dfa.unipd.it arXiv:2309.05937v1 [astro-ph.GA] 12 Sep 2023 - DFA Indico Opens in a new window — https://indico.dfa.unipd.it/event/913/attachments/1059/2121/2309.05937.pdf
- researchgate.net The Evolution of the Baryons Associated with Galaxies Averaged over Cosmic Time and Space - ResearchGate Opens in a new window — https://www.researchgate.net/publication/346309820_The_Evolution_of_the_Baryons_Associated_with_Galaxies_Averaged_over_Cosmic_Time_and_Space
- academic.oup.com star-formation variability from molecular clouds and gas inflow - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/497/1/698/33531672/staa1838.pdf
- academic.oup.com Galaxy evolution in cosmological simulations with outflows – II. Metallicities and gas fractions | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/416/2/1354/1061069
- academic.oup.com On the origin of the fundamental metallicity relation and the scatter in galaxy scaling relations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/443/1/168/1480246
- academic.oup.com The interplay between feedback, accretion, transport, and winds in setting gas-phase metal distribution in galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/528/2/2232/7515290
- academic.oup.com Evolution of gas velocity dispersion in discs from z ∼ 8 to z ∼ 0.5 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/544/3/2777/8261520
- researchgate.net (PDF) A dormant overmassive black hole in the early Universe - ResearchGate Opens in a new window — https://www.researchgate.net/publication/387178532_A_dormant_overmassive_black_hole_in_the_early_Universe
- arxiv.org The dark side of early galaxies: geko uncovers dark-matter fractions at z∼4-6 - arXiv Opens in a new window — https://arxiv.org/html/2510.14779v1
- arxiv.org arXiv:2009.10091v2 [astro-ph.GA] 28 Oct 2020 Opens in a new window — https://arxiv.org/pdf/2009.10091
- arxiv.org arXiv:2010.01769v1 [astro-ph.GA] 5 Oct 2020 Opens in a new window — https://arxiv.org/pdf/2010.01769
- pas.va Reinhard Genzel - The Pontifical Academy of Sciences Opens in a new window — https://www.pas.va/en/academicians/ordinary/genzel.html
- arxiv.org What drives the growth of black holes: a decade of progress - arXiv Opens in a new window — https://arxiv.org/html/2506.19166v2
- orcid.org Linda Tacconi - ORCID Opens in a new window — https://orcid.org/0000-0002-1485-9401
- arxiv.org Chapter 0 Hydrodynamic methods and sub-resolution models for cosmological simulations Opens in a new window — https://arxiv.org/html/2502.06954v1
- openreview.net DENOISING DIFFUSION PROBABILISTIC MODELS TO PREDICT THE NUMBER DENSITY OF MOLECULAR CLOUDS IN ASTRONOMY - OpenReview Opens in a new window — https://openreview.net/pdf?id=KiwRgaRYqRE
- slideshare.net A fast-rotator post-starburst galaxy quenched by supermassive black-hole feedback at z = 3 Opens in a new window — https://www.slideshare.net/slideshow/a-fast-rotator-post-starburst-galaxy-quenched-by-supermassive-black-hole-feedback-at-z-3/272228502
- researchgate.net (PDF) A Milky Way-like barred spiral galaxy at a redshift of 3 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/375493341_A_Milky_Way-like_barred_spiral_galaxy_at_a_redshift_of_3
- mpe.mpg.de 2020 Opens in a new window — https://www.mpe.mpg.de/7551885/2020
- pmc.ncbi.nlm.nih.gov A dormant overmassive black hole in the early Universe - PMC Opens in a new window — https://pmc.ncbi.nlm.nih.gov/articles/PMC11655357/
- arxiv.org Weak Evolution of Cosmic Atomic Hydrogen over the Past 4.5 Billion Years - arXiv Opens in a new window — https://arxiv.org/pdf/2607.05326
- arxiv.org Weak Evolution of Cosmic Atomic Hydrogen over the Past 4.5 Billion Years - arXiv Opens in a new window — https://arxiv.org/html/2607.05326v1
- arxiv.org Cm-wavelength Studies of Molecular Gas and Star Formation at High Redshift with the SKA Opens in a new window — https://arxiv.org/html/2606.26640v1
- arxiv.org Chapter 0 The Interstellar Medium - arXiv Opens in a new window — https://arxiv.org/html/2504.01410v1
- repository.cam.ac.uk The Molecular-Gas Main Sequence and Schmidt-Kennicutt relation are fundamental, the Star-Forming Main Sequence is a - University of Cambridge Opens in a new window — https://www.repository.cam.ac.uk/bitstreams/fda01533-9131-42c0-afea-a8e745862131/download
- academic.oup.com The dark side of early galaxies: geko uncovers dark-matter fractions at z ∼ 4 − 6 Opens in a new window — https://academic.oup.com/mnras/article/546/3/stag119/8429620
- academic.oup.com A shallow slope for the stellar mass–angular momentum relation of star-forming galaxies at 1.5 < z < 2.5 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/536/2/1188/7914168
- backend.orbit.dtu.dk Integral field spectroscopy of luminous infrared main ... - DTU Inside Opens in a new window — https://backend.orbit.dtu.dk/ws/files/245554786/stab527.pdf
- eprints.soton.ac.uk Non-monotonic relations of galaxy star formation, radius, and structure at fixed stellar mass - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/496231/2/stae1735.pdf
- purehost.bath.ac.uk Alternative formats If you require this document in an alternative format, please contact: openaccess@bath.ac.uk Opens in a new window — https://purehost.bath.ac.uk/ws/files/212416789/genzel2020_arXiv.pdf
- academic.oup.com Metal factories in the early Universe - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/532/3/2905/58597196/stae1564.pdf
- researchonline.ljmu.ac.uk Spatially resolved Kennicutt–Schmidt relation at z ≈ 7 and its connection with the interstellar medium properties - LJMU Research Online Opens in a new window — https://researchonline.ljmu.ac.uk/id/eprint/22075/1/Spatially%20resolved%20Kennicutt-Schmidt%20relation%20at%20z%3D7%20and%20its%20connection%20with%20the%20interstella%20medium%20properties.pdf
- researchgate.net Evolution of the molecular ISM out to z = 7.5. Left - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Evolution-of-the-molecular-ISM-out-to-z-75-Left-molecular-gas-depletion-timescale-t_fig3_375634457
- mpe.mpg.de Rotation Curves in z ∼ 1–2 Star-forming Disks: Evidence for Cored Dark Matter Distributions Opens in a new window — https://www.mpe.mpg.de/~saglia/journals_pdf/genzel2020.pdf
- researchgate.net (PDF) The dark side of early galaxies: $\texttt{geko}$ uncovers dark-matter fractions at $z\sim4-6 - ResearchGate Opens in a new window — https://www.researchgate.net/publication/396542291_The_dark_side_of_early_galaxies_textttgeko_uncovers_dark-matter_fractions_at_zsim4-6
- arxiv.org Dark matter fraction in z ∼ 1 star-forming galaxies - arXiv Opens in a new window — https://arxiv.org/pdf/2105.13684
- arxiv.org Molecular Gas Excitation in z∼0.7 Gas-Rich Post-starburst Galaxies from SQuIGGL⃗E - arXiv Opens in a new window — https://arxiv.org/html/2602.17766v2
- academic.oup.com Spatially resolved Kennicutt–Schmidt relation at z ≈ 7 and its connection with the interstellar medium properties - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/527/1/10/52662779/stad3150.pdf
- purehost.bath.ac.uk Davies, RL, Schreiber, NMF, Genzel, R, Shimizu, TT, Schruba, A, Tacconi - Alternative formats If you require this document in an alternative format, please contact: openaccess@bath.ac.uk - University of Bath Opens in a new window — https://purehost.bath.ac.uk/ws/portalfiles/portal/219622203/Davies2021_arXiv.pdf
- escholarship.org arXiv:2005.12916v1 [astro-ph.GA] 26 May 2020 - eScholarship.org Opens in a new window — https://escholarship.org/content/qt3jt1948t/qt3jt1948t_noSplash_75a9673c3d4d3d3e0e04236cfe1775e3.pdf
- researchgate.net Measuring Star Formation Rates in the Milky Way from Hi-GAL 70 μm Observations Opens in a new window — https://www.researchgate.net/publication/389116835_Measuring_Star_Formation_Rates_in_the_Milky_Way_from_Hi-GAL_70_mm_Observations
- researchgate.net Star Formation Rates and Depletion Timescales: Comparison of Observed... | Download Table - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Star-Formation-Rates-and-Depletion-Timescales-Comparison-of-Observed-Values-Compared-to_tbl1_230926044
- arxiv.org The baryon budget of galaxies across the first billion years - arXiv Opens in a new window — https://arxiv.org/html/2603.00230v1
- researchgate.net Molecular gas mass divided by that expected from the Tacconi et al.... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Molecular-gas-mass-divided-by-that-expected-from-the-Tacconi-et-al-2020-molecular-gas_fig1_408106310
- researchgate.net Star formation laws in galaxies near and far - ResearchGate Opens in a new window — https://www.researchgate.net/publication/348934617_Star_formation_laws_in_galaxies_near_and_far
- purehost.bath.ac.uk Alternative formats If you require this document in an alternative Opens in a new window — https://purehost.bath.ac.uk/ws/portalfiles/portal/302399519/Costantin2023_arXiv.pdf
- nu.to.infn.it Astronomy and Astrophysics - Neutrino Unbound - INFN Opens in a new window — https://www.nu.to.infn.it/Other_Astrophysics/
- arts.units.it UNIVERSITÀ DEGLI STUDI DI TRIESTE - ArTS Opens in a new window — https://arts.units.it/retrieve/03474fc1-3079-44d5-ac95-69957b6c0c57/Tesi_definitiva_AliceDamiano.pdf
- nbi.ku.dk Ultra red galaxies in the distant universe: The first quiescent galaxies and their hidden progenitors - Københavns Universitet Opens in a new window — https://nbi.ku.dk/english/theses/phd-theses/katriona-mai-landau-gould/katriona.pdf
- arxiv.org From Voids to Clusters: Mergers and Evolutionary Pathways of Star-Forming and Quenched Low-Mass Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2506.06711v2
- oamonitor.ireland.openaire.eu The Evolution of the Star-Forming Interstellar Medium Across Opens in a new window — https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.1146%2Fannurev-astro-082812-141034
- eso.org Munich Joint Astronomy Colloquium - ESO.org Opens in a new window — https://www.eso.org/public/djangoplicity/events/archive/site_embed/eso-garching/?audience=s&video=&year=2021&series=munich-joint-astronomy-colloquium
- arxiv.org 1 Introduction - arXiv Opens in a new window — https://arxiv.org/html/2404.08050v1
- researchgate.net (PDF) The Interstellar Medium - ResearchGate Opens in a new window — https://www.researchgate.net/publication/390439477_The_Interstellar_Medium
- iris.sissa.it Astrochemistry of the Molecular Gas in Dusty Star-Forming Galaxies at the Cosmic Noon - IRIS Opens in a new window — https://iris.sissa.it/retrieve/71342cb5-257c-4e73-b603-d44aaa447022/Perrotta24.pdf
- mdpi.com Observing Dusty Star-Forming Galaxies at the Cosmic Noon through Gravitational Lensing: Perspectives from New-Generation Telescopes - MDPI Opens in a new window — https://www.mdpi.com/2075-4434/12/2/9
- osti.gov What is Important? Morphological Asymmetries are Useful Predictors of Star Formation Rates of Star-forming Galaxies in SDSS Stripe 82 - OSTI Opens in a new window — https://www.osti.gov/pages/biblio/1983190
- arxiv.org 1 Introduction - arXiv Opens in a new window — https://arxiv.org/html/2404.09673v1
- cris.unibo.it ALPINE: A Large Survey to Understand Teenage Galaxies - Unibo Opens in a new window — https://cris.unibo.it/retrieve/d2008c1a-f119-465c-ad9e-a8f243698d2a/universe-08-00314.pdf
- mpe.mpg.de Research of the Infrared/Submillimeter Group at MPE | Max Planck Institute for extraterrestrial Physics Opens in a new window — https://www.mpe.mpg.de/ir/Research
- academic.oup.com Deriving a multivariate αCO conversion function using the [C ii]/CO (1−0) ratio and its application to molecular gas scaling relations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/470/4/4750/3883753
- arxiv.org The JWST EXCELS Survey: gas-phase metallicity evolution at 2 < z < 8 - arXiv Opens in a new window — https://arxiv.org/html/2511.00705v2
- academic.oup.com The stellar fundamental metallicity relation: the correlation between stellar mass, star formation rate, and stellar metallicity - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/532/2/2832/58608467/stae1581.pdf
- academic.oup.com Molecular and atomic gas along and across the main sequence of star-forming galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/462/2/1749/2589469
- arxiv.org Resolved Stellar and Nebular Kinematics of a Star-forming Galaxy at z∼2 - arXiv Opens in a new window — https://arxiv.org/html/2503.22039v1
- backend.orbit.dtu.dk Deep kiloparsec view of the molecular gas in a ... - DTU Inside Opens in a new window — https://backend.orbit.dtu.dk/ws/files/399180270/aa52652-24.pdf
- arxiv.org arXiv:2502.06538v1 [astro-ph.GA] 10 Feb 2025 Opens in a new window — https://arxiv.org/pdf/2502.06538
- academic.oup.com COLD GASS, an IRAM legacy survey of molecular gas in massive galaxies – II. The non-universality of the molecular gas depletion time-scale - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/415/1/61/988902
- arxiv.org The first detection of dense gas in a massive main-sequence galaxy at cosmic noon - arXiv Opens in a new window — https://arxiv.org/html/2606.19282v1
- academic.oup.com COLD GASS, an IRAM legacy survey of molecular gas in massive galaxies – I. Relations between H 2 , H i, stellar content and structural properties - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/415/1/32/988888
- academic.oup.com Galaxy cold gas contents in modern cosmological hydrodynamic simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/497/1/146/5866845
- edoc.ub.uni-muenchen.de Feedback in Galaxies During the Peak Epoch of Cosmic Star Formation Activity and Black Hole Growth Opens in a new window — https://edoc.ub.uni-muenchen.de/26841/1/Davies_Rebecca_L.pdf
- academic.oup.com The physics of gas phase metallicity gradients in galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/502/4/5935/6123897
- edoc.ub.uni-muenchen.de Constraints of galaxy evolution 1-2 billion years after the Big Bang Opens in a new window — https://edoc.ub.uni-muenchen.de/36328/6/Lee_Lilian_Lai_Yee.pdf
- annualreviews.org The Interstellar Medium in Dwarf Irregular Galaxies - Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-052722-104109
- arxiv.org Testing Feedback Regulated Star Formation in Gas Rich, Turbulent Opens in a new window — https://arxiv.org/pdf/1811.03108
- researchgate.net VINTERGATAN IV: Cosmic phases of star formation ... - ResearchGate Opens in a new window — https://www.researchgate.net/publication/363035885_VINTERGATAN_IV_Cosmic_phases_of_star_formation_in_Milky_Way-like_galaxies/fulltext/6393da61e42faa7e75aef951/VINTERGATAN-IV-Cosmic-phases-of-star-formation-in-Milky-Way-like-galaxies.pdf
- academic.oup.com 158 emission as an indicator of galaxy star formation rate - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/528/1/499/56209882/stad3792.pdf
- scispace.com BAT AGN Spectroscopic Survey. XX. Molecular gas in nearby hard-X-ray-selected AGN galaxies - SciSpace Opens in a new window — https://scispace.com/pdf/bat-agn-spectroscopic-survey-xx-molecular-gas-in-nearby-hard-1sjkybeqxh.pdf
- globaljournals.org The Nature of the Neutrino Gell-Mann-Nishijima Relation Flaws of Classical Assumptions Harnessing Superluminal Frontiers - Global Journals Opens in a new window — https://globaljournals.org/GJSFR_Volume25/E-Journal_GJSFR_(A)_Vol_25_Issue_3.pdf
- academic.oup.com Radiation pressure in galactic discs: stability, turbulence, and winds in the single-scattering limit | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/477/4/4665/4969690
- academic.oup.com WALLABY pilot survey: H i depletion times within the stellar discs of nearby galaxies | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/548/3/stag660/8644293
- arxiv.org Gamma Analytical Modeling Evolution (GAME) I: The physical implications of deriving the stellar mass functions from z=0 to z=8 - arXiv Opens in a new window — https://arxiv.org/pdf/2505.13301
- research.chalmers.se GAL: A NOEMA spectroscopic redshift survey of bright Herschel galaxies: III. Physical properties - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/538055/file/538055_Fulltext.pdf
- arxiv.org ADF22-WEB: Detection of a molecular gas reservoir in a massive quiescent galaxy located in a z≈3 proto-cluster core - arXiv Opens in a new window — https://arxiv.org/html/2502.06538v1
- scispace.com Star formation scaling relations at ∼100 pc from PHANGS - SciSpace Opens in a new window — https://scispace.com/pdf/star-formation-scaling-relations-at-100-pc-from-phangs-3jtup39ycu.pdf
- research.chalmers.se New Constraints on the Evolution of the M<inf>H i</inf>−M<inf>⋆</inf> Scaling Relation Combining CHILES and MIGHTEE-H i Data - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/545724/file/545724_Fulltext.pdf
- academic.oup.com Stochastic modelling of star-formation histories II: star-formation variability from molecular clouds and gas inflow - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/497/1/698/5863224
- wwwmpa.mpa-garching.mpg.de Galaxy Lookback Evolution Models - a Comparison with Magneticum Cosmological Simulations and Observations - MPA Garching Opens in a new window — https://wwwmpa.mpa-garching.mpg.de/HydroSims/Magneticum/Preprints/lookback_RK.pdf
- arxiv.org JWST Reveals Widespread AGN-Driven Neutral Gas Outflows in Massive z∼ 2 Galaxies Opens in a new window — https://arxiv.org/html/2310.17939v2
- arxiv.org Measurement of the gas consumption history of a massive quiescent galaxy - arXiv Opens in a new window — https://arxiv.org/html/2405.19401v2
- arxiv.org Tracing the total molecular gas in galaxies: [CII] and the CO-dark gas - arXiv Opens in a new window — https://arxiv.org/pdf/2009.00649
- arxiv.org arXiv:2311.00025v1 [astro-ph.GA] 31 Oct 2023 Opens in a new window — https://arxiv.org/pdf/2311.00025
- annualreviews.org Annual Review of Astronomy and Astrophysics - Volume 58, 2020 Opens in a new window — https://www.annualreviews.org/content/journals/astro/58/1
- arxiv.org From Atomic Gas to Star Formation - arXiv Opens in a new window — https://arxiv.org/html/2607.03592v1
- research.chalmers.se Cosmic evolution of the star formation efficiency in Milky Way-like galaxies - research.chalmers.se Opens in a new window — https://research.chalmers.se/publication/545871/file/545871_Fulltext.pdf
- mdpi.com Astrochemistry of the Molecular Gas in Dusty Star-Forming Galaxies at the Cosmic Noon Opens in a new window — https://www.mdpi.com/2075-4434/12/2/18
- grokipedia.com Linda Tacconi - Grokipedia Opens in a new window — https://grokipedia.com/page/linda_tacconi
- arxiv.org A quiescent galaxy in a gas-rich cosmic web node at z∼3 - arXiv Opens in a new window — https://arxiv.org/html/2601.20473v3
- researchgate.net (PDF) Star Formation - ResearchGate Opens in a new window — https://www.researchgate.net/publication/383792062_Star_Formation
- iris.sissa.it Observing Dusty Star-Forming Galaxies at the Cosmic Noon through Gravitational Lensing - IRIS Opens in a new window — https://iris.sissa.it/retrieve/85e27e5a-bcd8-4ca0-8a43-d3bf69ea4a19/Giulietti24.pdf
- academic.oup.com Kennicutt–Schmidt relation of galaxies over 13 billion years in the COLIBRE hydrodynamical simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/549/2/stag947/8696395
- academic.oup.com molecular gas main sequence and Schmidt–Kennicutt relation are fundamental, the star-forming main sequence is a (useful) byproduct | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/518/3/4767/6843609
- uhra.herts.ac.uk Resolved Dust Emission and CO Isotopologues in Giant Molecular Clouds of the Andromeda Galaxy Opens in a new window — https://uhra.herts.ac.uk/id/eprint/26738/1/Bosomworth_2026_ApJ_1000_215.pdf
- researchgate.net For all targets with data for both stellar mass (M ☆ ) and CO gas... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/For-all-targets-with-data-for-both-stellar-mass-M-and-CO-gas-masses-M-CO-we_fig4_374725639
- academic.oup.com A study of the gas–star formation relation over cosmic time - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/407/4/2091/998428
- indico.in2p3.fr Synergy between galaxy formation and cosmology using submillimeter- wave line intensity mapping Opens in a new window — https://indico.in2p3.fr/event/34139/contributions/145057/attachments/87401/131957/241009_v6.pdf
- academic.oup.com High molecular gas content and star formation rates in local galaxies that host quasars, outflows, and jets - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/498/2/1560/5903287
- pure.ed.ac.uk Edinburgh Research Explorer - The CO Luminosity Density at High-z (COLDz) Survey - Account Opens in a new window — https://www.pure.ed.ac.uk/ws/files/75901766/Pavesi_2018_ApJ_864_49.pdf
- arxiv.org Molecular gas properties of star-forming brightest group galaxies at z∼0.3 - arXiv Opens in a new window — https://arxiv.org/html/2605.21592v1
- mpe.mpg.de The Regulation of Galaxy Growth along the Size–Mass Relation by Star Formation, as Traced by Hα in KMOS3D Galaxies at 0.7 Opens in a new window — https://www.mpe.mpg.de/~saglia/journals_pdf/wilman2020.pdf
- mpia.de The Evolution of the Baryons Associated with Galaxies Averaged over Cosmic Time and Space Opens in a new window — https://www.mpia.de/5504464/walter_aspecs_2020.pdf
- eprints.whiterose.ac.uk GOODS-ALMA 2.0 : starbursts in the main sequence reveal compact star formation regulating galaxy evolution prequenching Opens in a new window — https://eprints.whiterose.ac.uk/id/eprint/186452/1/aa42352-21.pdf
- annualreviews.org Star-Forming Galaxies at Cosmic Noon | Annual Reviews Opens in a new window — https://www.annualreviews.org/doi/10.1146/annurev-astro-032620-021910
- warwick.ac.uk Magnetohydrodynamic Waves in the Solar Corona - University of Warwick Opens in a new window — https://warwick.ac.uk/fac/sci/physics/research/cfsa/people/valery/research/eprints/annurev-astro-032320-042940.pdf
- annualreviews.org The Cold Interstellar Medium of Galaxies in the Local Universe - Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-021022-043545?TRACK=RSS
- annualreviews.org Theory and Observation of Winds from Star-Forming Galaxies | Annual Reviews Opens in a new window — https://www.annualreviews.org/content/journals/10.1146/annurev-astro-041224-011924
- purehost.bath.ac.uk Star-Forming Galaxies at Cosmic Noon Opens in a new window — https://purehost.bath.ac.uk/ws/files/212416705/2010.10171v1.pdf
- annualreviews.org The Cosmic Baryon and Metal Cycles - Annual Reviews Opens in a new window — https://www.annualreviews.org/doi/pdf/10.1146/annurev-astro-021820-120014
- mdpi.com Molecular Gas Heating, Star Formation Rate Relations, and AGN Feedback in Infrared-Luminous Galaxy Mergers - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/9/1/3
- mdpi.com From Clusters to Proto-Clusters: The Infrared Perspective on Environmental Galaxy Evolution - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/8/11/554
- mdpi.com ALPINE: A Large Survey to Understand Teenage Galaxies - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/8/6/314
- arxiv.org The ALMA-CRISTAL survey: Resolved kinematic studies of main sequence star-forming galaxies at 4 < z < 6 - arXiv Opens in a new window — https://arxiv.org/html/2507.11600v1
- researchgate.net Tracing the total molecular gas in galaxies: [CII] and the CO-dark gas - ResearchGate Opens in a new window — https://www.researchgate.net/publication/345410861_Tracing_the_total_molecular_gas_in_galaxies_CII_and_the_CO-dark_gas
- edoc.ub.uni-muenchen.de Distant, dusty star-forming galaxies Opens in a new window — https://edoc.ub.uni-muenchen.de/32644/1/Chen_Jianhang.pdf
- arxiv.org NOEMA^"3D": Spatially resolved dust, CO, and [C I] in massive star-forming main sequence galaxies at cosmic noon - arXiv Opens in a new window — https://arxiv.org/html/2604.18504v2
- vbn.aau.dk Aalborg Universitet Astrophysics with the Laser Interferometer Space Antenna LISA Opens in a new window — https://vbn.aau.dk/ws/files/703717606/2203.06016v2.pdf
- purehost.bath.ac.uk Star-Forming Galaxies at Cosmic Noon Opens in a new window — https://purehost.bath.ac.uk/ws/files/212416702/ForsterSchreiberWuyts_araa_withPerm.pdf
- eprints.soton.ac.uk Galaxy formation through the lens of galaxy structure with semi-empirical models and deep learning - ePrints Soton - University of Southampton Opens in a new window — https://eprints.soton.ac.uk/467307/1/Zanisi_thesis_final.pdf
- arxiv.org arXiv:2005.06472v1 [astro-ph.GA] 13 May 2020 Opens in a new window — https://arxiv.org/pdf/2005.06472

## Custody

- Raw audit custody only; do not integrate. Canonical release requires composite identifier and claim-boundary verification.
- No wiki, DB, trust, deploy, publish, git, credential, billing, account-setting, or conversation-deletion mutation was performed.

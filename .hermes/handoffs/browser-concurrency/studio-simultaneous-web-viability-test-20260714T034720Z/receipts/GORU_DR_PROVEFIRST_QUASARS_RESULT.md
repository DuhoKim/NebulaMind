# Deep Research prove-first result — Quasars as drivers of galaxy evolution

NebulaMind page: `quasars` (page_id 32)
Debate: `Are Quasars the Primary Drivers of Galaxy Evolution?`

Conversation ID: `116a89ea5f3eae3a`
Conversation title: `Topic: Are quasars (luminous AGN) the primary drivers of galaxy evolution, or a secondary regulator relative to mergers and gas`
Target ID: `C92443095EE9116210C178D855DF3329`
Prompt SHA-256: `6d3b61d77e50aab1dd341d5a4c52c9bd07845f64b465d6da3d5e339bc1e0f5d9`
Prompt submit UTC: `2026-07-14T11:07:37.629377Z`
Research start UTC: `2026-07-14T11:09:48Z`
Result captured UTC: `2026-07-14T11:22:38.150838Z`
Result text SHA-256: `deaef465a2fa510f42c7e887f1d231fb6428d4cf4a6a8ae2cef88cdaf6609231`

## Verbatim prompt

Topic: Are quasars (luminous AGN) the primary drivers of galaxy evolution, or a secondary regulator relative to mergers and gas accretion?

Produce a rigorous, fully sourced literature review of the debate over the role of quasar / luminous-AGN feedback in galaxy evolution: whether energetic AGN feedback is the primary mechanism regulating star formation and galaxy growth (quenching, outflows, the M-sigma relation), versus the view that mergers, cold-gas accretion, and secular processes dominate while quasars play a secondary role.

Requirements:
1. Every factual assertion must be backed by a REAL, verifiable reference — give the arXiv ID (e.g. 2303.15506), DOI, and/or publisher URL, plus paper title, first author, and publication year. Do NOT invent, guess, or approximate identifiers; omit an identifier you cannot verify rather than fabricate it. Prefer peer-reviewed papers and prioritize 2023-2025 work (JWST, ALMA, MUSE, eROSITA, X-shooter era), while including foundational earlier references where needed for context.
2. Cover: (a) the current mainstream understanding and points of genuine consensus; (b) the contested findings, explicitly separating evidence/arguments that support "quasars are the primary driver" from those that challenge it (i.e., support the "mergers/accretion dominate, quasars secondary" position); (c) key open questions and what upcoming data could resolve them.
3. Address concrete sub-threads: observed AGN-driven outflows and their coupling efficiency; positive vs. negative feedback; correlation vs. causation in the M-sigma / M_BH-M_bulge relations; whether AGN feedback actually quenches star formation in situ; the role of major/minor mergers as triggers; cold accretion and secular gas supply; and cosmological-simulation evidence (e.g., IllustrisTNG, EAGLE, SIMBA) on feedback necessity.

Output structure (critical — the report will be machine-parsed): Organize the findings as a set of discrete claim units. For each distinct scientific claim, output a block with these fields:
- claim_text: one clear declarative sentence.
- claim_type: established (broad consensus) or debate (genuinely contested).
- debate_topic: for debate claims, a short shared label; for this review use "Are Quasars the Primary Drivers of Galaxy Evolution?" where applicable, or a precise sub-topic label.
- papers: a list of the supporting/relevant references, each as { arxiv_id | doi | url, title, year, stance } where stance is supports if the paper's findings back the claim_text, or refutes if they contradict it.

For contested points, provide both a pro claim and a con claim as separate units (mirroring a two-sided debate), each with its own correctly stance-labeled papers list. Ensure supporting and challenging literature are attributed to the correct side — do not attach the same paper as supports to opposing claims unless it genuinely supports both. Include a final plain-text bibliography of every reference cited with its verifiable identifier.

## Full Deep Research report

Are Quasars the Primary Drivers of Galaxy Evolution? A Comprehensive Review of AGN Feedback Mechanisms

The role of Active Galactic Nuclei (AGN), and specifically their most luminous manifestation as quasars, in the evolutionary trajectory of galaxies represents one of the most intensely debated subjects in modern astrophysics. For over two decades, the standard cosmological paradigm has relied on the immense energy released by accreting supermassive black holes to solve the "overcooling problem"—the theoretical over-prediction of massive galaxies in a purely dark-matter-driven universe. Within this established framework, quasar-driven outflows act as the primary regulatory mechanism, ejecting molecular gas, halting star formation (a process known as quenching), and establishing tight empirical scaling relations between black hole mass and host galaxy properties.   

However, the advent of next-generation observational facilities, notably the James Webb Space Telescope (JWST), the Atacama Large Millimeter/submillimeter Array (ALMA), and advanced integral field spectrographs such as MUSE and X-shooter, has introduced profound complexities into this narrative. Alongside high-resolution cosmological hydrodynamical simulations (including IllustrisTNG, EAGLE, SIMBA, and FLAMINGO), empirical evidence now actively challenges the efficiency of quasar-driven outflows. Current research questions the necessity of major mergers as triggers for AGN activity, scrutinizes the causal nature of the M
BH
	​

−σ relation, and reveals counter-intuitive phenomena such as positive feedback—where outflows actively trigger, rather than suppress, star formation. This report systematically synthesizes the current literature to evaluate whether quasars act as the primary, causative drivers of galaxy evolution, or as secondary regulators operating in tandem with secular processes, cold-gas accretion, and hierarchical merging.   

1. The Necessity of AGN Feedback in Cosmological Simulations

The foundation of the "quasar as primary driver" argument originates from theoretical and computational necessity. Without injecting energy from supermassive black holes into the interstellar and circumgalactic mediums (ISM/CGM), hydrodynamical simulations uniformly fail to reproduce the observed exponential cutoff at the high-mass end of the galaxy stellar mass function. In the absence of this feedback, gas continuously cools and falls to the centers of dark matter halos, leading to the overproduction of unphysically massive, highly star-forming galaxies at low redshift.   

Sub-Grid Implementations and the Quenching Threshold

In state-of-the-art simulations, AGN feedback is typically implemented in distinct modes tied to the Eddington ratio of the accreting black hole. The "quasar mode" (radiatively efficient, high accretion) drives fast, momentum-conserving winds, while the "radio mode" (radiatively inefficient, low accretion) injects kinetic energy via relativistic jets into the hot halo gas, preventing the subsequent cooling and accretion of fresh material.   

Recent results from the high-resolution FLAMINGO simulation, which analyzed a sample of 5.3 million galaxies, demonstrate that black hole feedback is overwhelmingly the primary quenching mechanism across varied environments for both central and satellite galaxies. The simulation reveals that galaxies undergo a remarkably sharp transition from the star-forming main sequence to quiescence when the central black hole reaches a critical mass of M
BH
	​

≃10
7
M
⊙
	​

 (typically corresponding to a stellar mass of M
∗
	​

≃10
10.5
M
⊙
	​

 and a halo mass of M
h
	​

≃10
12
M
⊙
	​

). Once this threshold is crossed, the galaxy experiences a short quenching timescale of approximately 1 Gyr, driven by a sudden depletion of gas mass in the inner circumgalactic medium.   

Similarly, the SIMBA cosmological simulation utilizes a multi-tiered feedback approach involving AGN winds, jets, and X-ray heating. Analyses of SIMBA variants with individual feedback modules disabled reveal that AGN jets are the dominant quenching mechanism setting the shape of the star formation rate density and the galaxy stellar mass function at late times. However, the X-ray feedback mode is uniquely necessary to produce the first fully quenched massive galaxies before z=2, as the extra heating source is required to eject gas from dense, central regions where jets alone are inefficient.   

Demographic Discrepancies and Open Questions

Despite this widespread theoretical reliance, the exact sub-grid physics of AGN feedback remain poorly constrained and often conflict with empirical demographic data. A rigorous comparative study by Suresh et al. (2026) tested the radio-mode AGN feedback models of the EAGLE, SIMBA, and TNG100 simulations against local observational constraints. The researchers found that none of these simulations can even qualitatively reproduce the observed dependencies of the radio AGN fraction on host galaxy stellar mass and specific star formation rate (sSFR).   

In observational data, the completeness-corrected fraction of galaxies hosting radio AGN with an Eddington ratio λ>10
−3
 is a strong function of stellar mass but is nearly independent of sSFR at a fixed mass. The simulations, however, produce radically different dependencies, indicating that the simulated coupling between black hole growth, jet emission, and star formation suppression may be artificially tuned rather than physically accurate.   

Simulation Suite	Primary Quenching Mechanism	Key Findings & Distinctive Features	Discrepancies with Observations
FLAMINGO	Black Hole Feedback	Quenching is triggered at a hard threshold of M
BH
	​

≃10
7
M
⊙
	​

, functioning independent of environment.	Sub-grid calibration dependencies.
SIMBA	Jets & X-ray Heating	Jets dominate late-time quenching; X-ray heating is required for early (z>2) massive galaxy quenching.	Fails to match observed radio-AGN fractions vs. sSFR.
IllustrisTNG	Kinetic Winds (Low Accretion)	Secular processes dominate; major mergers are neither necessary nor sufficient for central galaxy quenching.	Underpredicts sub-millimeter galaxy number counts.
EAGLE	Thermal Injection	Single-mode thermal feedback proportional to accretion rate.	Over-predicts recently quenched fraction in post-mergers relative to controls.

claim_text: Cosmological hydrodynamic simulations require the inclusion of AGN feedback to reproduce the observed high-mass cutoff of the galaxy stellar mass function and to prevent the overcooling of gas in massive dark matter halos.

claim_type: established

debate_topic: Are Quasars the Primary Drivers of Galaxy Evolution?

papers:

{ doi: 10.1093/mnras/staf1578, title: "In situ versus ex situ drivers of galaxy quenching: critical black hole mass and main sequence universality in the FLAMINGO simulation", year: 2025, stance: supports }

{ arxiv_id: 2508.04907, title: "AGN Feedback Models and AGN Demographics I: Radio-Mode AGN in EAGLE, SIMBA and TNG100 are Inconsistent with Observations", year: 2026, stance: supports }

claim_text: Current sub-grid models of AGN feedback in cosmological simulations (EAGLE, SIMBA, TNG100) fail to reproduce the observed demographics of radio-mode AGN as a function of specific star formation rate and stellar mass.

claim_type: established

debate_topic: Accuracy of Cosmological Simulation Feedback Models

papers:

{ arxiv_id: 2508.04907, title: "AGN Feedback Models and AGN Demographics I: Radio-Mode AGN in EAGLE, SIMBA and TNG100 are Inconsistent with Observations", year: 2026, stance: supports }

2. Observational Signatures of Outflows and Coupling Efficiency

For quasars to act as the primary drivers of galaxy quenching, they must efficiently couple their radiative and mechanical energy to the host galaxy's ISM, physically removing or heating the cold molecular gas required for star formation. Decades of observations have confirmed the existence of multi-phase galactic outflows—comprising ionized, neutral atomic, and molecular gas—driven by AGN activity. Because stars form from cold, dense molecular gas, the molecular phase of the outflow is of paramount importance when evaluating quenching efficacy.   

The Problem of Kinetic Coupling

Theoretical blast-wave models of AGN feedback, which assume energy-conserving flows where the shocked wind gas does not cool efficiently, typically require a kinetic coupling efficiency (the ratio of outflow kinetic power to AGN bolometric luminosity, 
E
˙
kin
	​

/L
AGN
	​

) of approximately 5% to successfully unbind a galaxy's gas reservoir and halt star formation.   

However, empirical measurements from the JWST and ALMA era severely challenge this requirement. In the early Universe, Spilker et al. (2025) utilized ALMA to observe OH 119 μm doublet lines in a sample of 11 unobscured, IR-luminous quasars at z>6 (the epoch of reionization). While they detected unambiguous, fast molecular outflows in 73% of the quasars, the implied molecular outflow rates were relatively modest. Crucially, the kinetic power carried in the cold outflow phase was typically only ∼0.1% of the total AGN bolometric luminosity.   

Studies of local galaxies mirror these high-redshift findings. An analysis of molecular outflows in 45 local galaxies using ALMA CO(1-0) data found that the outflow kinetic power spans from 0.1% to 5% of L
AGN
	​

, exhibiting a massive scatter in coupling efficiencies. Furthermore, the molecular gas depletion times associated with these outflows are often much longer than the dynamical times of the galaxies. The data suggests that while AGN-driven outflows might successfully clear and quench the immediate central region (the circumnuclear disk), they are relatively ineffective at clearing the entire galactic gas content.   

Clumpy Interstellar Media and Escape Channels

The physical mechanism behind this low coupling efficiency is elucidated by ultra-high-resolution hydrodynamic simulations of AGN winds interacting with a realistic, clumpy ISM. Ward et al. (2024) demonstrated through sub-parsec resolution AREPO simulations that the structure of the ISM profoundly alters outflow properties. In an artificially homogeneous disk, an AGN wind sweeps up a cooling shell where the cold phase dominates the kinetic energy budget, reaching momentum fluxes of 
p
˙
	​

≈7L/c.   

However, when the ISM is realistically clumpy, the hot AGN wind escapes through low-density channels of least resistance. The cold, star-forming cloudlets are entrained within the faster, hot outflow phase, but they couple to the energy-driven bubbles highly inefficiently. This results in the cold, mass-carrying phase of the outflow exhibiting modest momentum fluxes (
p
˙
	​

<L/c), which could easily lead observers to misclassify the outflows as momentum-driven rather than energy-driven. Consequently, quasar feedback acts primarily as a localized regulator that vents thermal energy into the halo, rather than acting as a rigid macroscopic "snowplow" that clears the entire galaxy.   

claim_text: Powerful, galaxy-scale quasar-driven outflows rapidly clear cold molecular gas from the interstellar medium, serving as the primary mechanism for in situ star formation quenching in massive galaxies.

claim_type: debate

debate_topic: Does AGN Feedback Actually Quench Star Formation In Situ?

papers:

{ arxiv_id: 2502.05283, title: "Direct Evidence for AGN Feedback from Fast Molecular Outflows in Reionization-Era Quasars", year: 2025, stance: supports }

{ arxiv_id: 2604.26195, title: "Resolved Maps of Gas and Dust in a Massive Quiescent Galaxy at z=2 from INQUEST-JWST: Evidence of Accretion and Rejuvenation", year: 2025, stance: supports }

claim_text: Quasar-driven outflows exhibit low kinetic coupling efficiencies and are ineffective at fully depleting global molecular gas reservoirs, indicating that energetic AGN feedback plays a secondary or localized regulatory role rather than directly causing galaxy-wide quenching.

claim_type: debate

debate_topic: Does AGN Feedback Actually Quench Star Formation In Situ?

papers:

{ doi: 10.1093/mnras/sty3449, title: "Cold molecular outflows in local galaxies", year: 2019, stance: supports }

{ arxiv_id: 2407.17593, title: "AGN-driven outflows in clumpy media: multiphase structure and scaling relations", year: 2024, stance: supports }

3. The Triggering Debate: Major Mergers versus Secular Processes

A critical sub-thread in the AGN feedback debate involves the triggering mechanism of the quasar itself. The "merger-quasar-quench" paradigm has historically dominated theoretical astrophysics. In this idealized model, a major, gas-rich galaxy merger drives violent tidal perturbations that dissipate angular momentum, funneling immense quantities of cold gas into the nuclear region. This triggers an extreme starburst and rapidly feeds the central supermassive black hole, igniting a highly luminous quasar phase. The quasar subsequently launches a massive outflow that ejects the remaining gas, rapidly transforming the merging disks into a quenched, "red and dead" elliptical galaxy.   

Evidence for Merger-Driven Quenching

Empirical support for this pathway is frequently found in studies of post-merger galaxy populations. Observations from the Ultraviolet Near Infrared Optical Northern Survey (UNIONS) demonstrate that the frequency of post-merger galaxies that have rapidly shut down their star formation following a previous starburst is 30 to 60 times higher than expected from isolated control samples. Utilizing the Multi-Model Merger Identifier (MUMMI) neural network ensemble to predict the time since coalescence, Ellison et al. (2024) found a clear peak in post-merger quenching occurring between 0.16 and 0.48 Gyr post-coalescence. In this specific post-merger time range, post-starburst galaxies (PSBs) are more common than in control galaxies by factors of up to 100, providing strong evidence that galaxy-galaxy interactions can indeed lead to rapid quenching via an intermediary AGN phase.   

The Rise of Secular Dominance

However, advanced cosmological simulations and large-scale observational surveys across cosmic time strongly challenge the universality of the major merger paradigm. A comprehensive analysis tracking over 11,000 central galaxies in the IllustrisTNG simulation revealed that major mergers are neither necessary nor sufficient for galaxy quenching. Only approximately 3% of major mergers in the simulation lead to quenching within 1 Gyr, and the vast majority of quenching events are not preceded by a merger. Once random coincidences are accounted for using stellar-mass-matched control samples, no merger excess is observed. The simulations determine that secular processes dominate both the growth of supermassive black holes and the quenching of central galaxies.   

Observational studies targeting high-redshift, luminous AGN support this conclusion. A morphological study of 106 luminous X-ray-selected type 1 AGN at 0.5<z<2.2 from the COSMOS survey utilized galfit residual analysis to identify disturbance features. The study found no enhancement of merger features with increasing AGN luminosity, implying that major mergers make a noticeable but ultimately subdominant contribution to AGN fueling. Similarly, observations of luminous quasars at z∼0.6 find no significant enhancement of major merger signatures in quasar host galaxies compared to matched controls, indicating that minor mergers (with mass ratios as low as 1:40) and secular gas supply via cold accretion flows maintain AGN activity even at the highest luminosities.   

Triggering Mechanism	Proposed Role in Galaxy Evolution	Primary Evidence Base
Major Mergers	Violent angular momentum dissipation; triggers extreme starbursts and the most luminous quasar phases, leading to rapid blowout.	UNIONS Survey; Post-starburst excess post-coalescence; idealized hydrodynamical models.
Minor Mergers	Frequent, low-mass ratio collisions (up to 1:40) that perturb gas disks enough to funnel material inward without destroying the host morphology.	TNG50 simulation tracking; High-z morphological studies lacking major disturbance.
Secular Processes & Cold Accretion	Gradual feeding via bars, disk instabilities, and cosmic web filaments. Dominant mechanism for steady black hole growth and maintenance mode feedback.	IllustrisTNG massive galaxy tracking; Lack of merger signatures in z∼0.6 quasars.

claim_text: Major galaxy mergers are the primary triggering mechanism for the most luminous quasars and drive the subsequent rapid shutdown of star formation.

claim_type: debate

debate_topic: The Role of Major Mergers as Triggers for Luminous AGN

papers:

{ arxiv_id: 2209.07613, title: "Galaxy mergers can rapidly shut down star formation", year: 2022, stance: supports }

{ arxiv_id: 2212.10598, title: "The interconnection between galaxy mergers, AGN activity and rapid quenching of star formation in simulated post-merger galaxies", year: 2022, stance: supports }

claim_text: Secular processes, minor mergers, and cold gas accretion dominate black hole fuelling, and major mergers are neither necessary nor sufficient to trigger galaxy-wide quenching or luminous AGN activity.

claim_type: debate

debate_topic: The Role of Major Mergers as Triggers for Luminous AGN

papers:

{ arxiv_id: 2603.12651, title: "Beyond the Merger-Quasar-Quench Paradigm I: Mergers are neither necessary nor sufficient to quench central galaxies in IllustrisTNG", year: 2026, stance: supports }

{ url: https://academic.oup.com/mnras/article/466/1/812/2573007, title: "Host galaxies of luminous z ~ 0.6 quasars: major mergers are not the dominant trigger for AGN activity", year: 2017, stance: supports }

4. Fossil Outflows and the Temporal Disconnect

A primary empirical argument historically wielded against quasar-driven quenching is the existence of rapidly quenched post-starburst galaxies that exhibit massive outflows but lack any detectable, luminous AGN emission. If quasars are responsible for quenching galaxies, why is the quasar so frequently absent during the critical period when the quenching is actually observed?

The resolution to this paradox lies in the differing temporal scales of black hole accretion and large-scale galactic dynamics. Supermassive black hole accretion is highly stochastic; AGN "flicker" on and off on extremely short timescales, typically ranging from 10
4
 to 10
5
 years. Conversely, a galactic-scale outflow requires tens of millions of years (∼10
7
 years) to physically propagate through the ISM and into the circumgalactic medium.   

Deep JWST NIRSpec integral field spectroscopy from the EXCELS survey has provided crucial evidence supporting this temporal disconnect. Researchers identified neutral gas outflows, traced via blueshifted Na I D absorption profiles, in 13 post-starburst and quiescent galaxies at 1.8≤z≤4.6. The outflow velocities ranged from 300 to 1200 km/s. Crucially, the mass outflow rates derived from these absorption profiles were over two orders of magnitude higher than the galaxies' residual, current levels of star formation, firmly ruling out supernovae as the driving mechanism.   

Because these galaxies currently lack strong optical emission lines or X-ray detections indicative of an active AGN, researchers conclude that these are "fossil outflows". The outflows are physical relics of a previous, highly luminous quasar phase that successfully launched the wind but has since faded into dormancy due to the depletion of its immediate accretion disk. Comparisons with the EAGLE simulation support an "outflow cycle" model: high-redshift quiescent galaxies undergo short ∼5 Myr periods of intense AGN activity that drive outflows. These observable outflows persist in the ISM for up to ∼10 Myr after the AGN fades, followed by a lull and subsequent short inflow that eventually re-ignites the AGN. This episodic feedback cycle effectively reconciles the temporal disconnect, solidifying the quasar's role as an intermittent but highly impactful evolutionary driver.   

claim_text: Outflows detected in post-starburst and quiescent galaxies are often "fossil outflows," driven by previous episodes of highly luminous quasar activity that has since faded, explaining the lack of concurrent X-ray emission.

claim_type: established

debate_topic: Temporal Disconnect Between Outflows and AGN Activity

papers:

{ doi: 10.1093/mnras/stag918, title: "The JWST EXCELS survey: outflows in 1.5 < z < 5 quiescent and recently quenched galaxies are likely relics from episodic AGN activity", year: 2026, stance: supports }

5. The M-Sigma Relation: Causation versus Correlation

The empirical scaling relation between the mass of a central supermassive black hole (M
BH
	​

) and the stellar velocity dispersion (σ) of the host galaxy's bulge—known as the M−σ relation—is frequently presented as the "crown jewel" of evidence for quasar feedback regulating galaxy growth.

The Causal Feedback Argument

The causal interpretation posits that when a black hole reaches a critical mass, its momentum-driven or energy-driven winds become powerful enough to unbind the protogalaxy's gas against the inward pull of gravity. This blowout abruptly cuts off the black hole's own fuel supply, permanently locking the black hole mass to the depth of the galaxy's gravitational potential well (traced by σ). Standard analytical feedback models successfully predict the slope (α≈4−5) of the M−σ relation, cementing the view that feedback physically forces galaxies and black holes to co-evolve.   

The Statistical Merging Counter-Argument

Conversely, an entirely non-causal origin has been robustly argued by theorists analyzing hierarchical structure formation. Mathematical modeling demonstrates that the M−σ and M
BH
	​

−M
bulge
	​

 relations can emerge naturally as a direct consequence of the Central Limit Theorem. If massive galaxies assemble via the successive hierarchical merging of smaller halos containing initially uncorrelated stellar and black hole masses, the statistical averaging effect of these repeated mergers will naturally produce a tight, linear correlation over cosmic time. In this model, the intrinsic scatter decreases with the number of mergers (σ
merg
	​

∝σ
ini
	​

/
m
	​

), producing a tight scaling relation at z=0 that is entirely independent of any physical feedback coupling.   

Observational Tests of the Paradigm

Resolving this debate requires observing systems that have undergone minimal merging, such as extreme high-redshift systems and low-mass dwarf galaxies. Recent high-resolution JWST integral field spectroscopy of MRG-M0138—a gravitationally lensed, quiescent galaxy at z=1.95—revealed a dormant black hole weighing 6 billion solar masses. While this black hole is drastically "overmassive" compared to its host's bulge mass (roughly 12 times more massive than expected from local scaling relations), it aligns perfectly with the local M−σ relation.   

Furthermore, observations of the M−σ relation extending accurately down into the dwarf galaxy regime severely challenge the hierarchical merging model. Dwarf galaxies lack the requisite complex merger history to statistically average into a tight correlation. If assembly via merging were the sole cause, one would expect a massive scatter in black hole masses at low galaxy masses, which is not observed. These findings strongly favor the presence of a physical feedback mechanism that regulates black hole growth directly relative to the galaxy's dynamical potential, rather than its total stellar mass.   

claim_text: The tight correlation between supermassive black hole mass and galaxy bulge velocity dispersion (the M-sigma relation) is a direct causal result of self-regulating AGN feedback locking black hole growth to the host's gravitational potential.

claim_type: debate

debate_topic: Correlation vs. Causation in the M-sigma Relation

papers:

{ arxiv_id: 1006.0482, title: "The non-causal origin of the black hole-galaxy scaling relations", year: 2011, stance: refutes }

{ doi: 10.1126/science.adx5816, title: "A stellar dynamical mass measurement of an inactive black hole at redshift 2", year: 2026, stance: supports }

claim_text: The M-sigma and M-bulge relations emerge naturally as a non-causal statistical consequence of hierarchical galaxy merging (the Central Limit Theorem), independent of physical feedback coupling.

claim_type: debate

debate_topic: Correlation vs. Causation in the M-sigma Relation

papers:

{ arxiv_id: 1006.0482, title: "The non-causal origin of the black hole-galaxy scaling relations", year: 2011, stance: supports }

6. The Paradigm Shift: Positive AGN Feedback

Traditionally, AGN feedback is modeled purely as a destructive, "negative" force that starves galaxies of their star-forming potential by expelling or heating cold gas. However, high-resolution multi-wavelength observations have uncovered a paradoxical phenomenon that fundamentally complicates the quenching narrative: "positive" AGN feedback.

When quasar-driven winds propagate outward and slam into the clumpy ISM, the resulting shockwaves do not uniformly eject the gas. Instead, these shocks can severely compress local molecular clouds. If the radiative cooling time of the shocked gas is sufficiently short compared to the expansion time, the gas condenses rapidly, accelerating fragmentation and gravitational collapse. This results in the ignition of intense, localized star formation.   

Remarkably, recent spatially resolved spectroscopic data from the VLT X-shooter spectrograph have detected signatures of young stellar populations forming directly inside the high-velocity galactic outflows themselves. In a sample of local galaxies with powerful AGN, researchers utilized BPT diagnostic diagrams and kinematic component analysis to rule out external photoionization and shocks, finding robust evidence for star formation within the outflow of systems like IRAS 20551-4250.   

In highly luminous AGN, stars formed within these outflows are born on extreme radial trajectories. Depending on their escape velocities, they may either fall back to contribute to the rapid buildup of the galaxy's spheroidal bulge or escape entirely, seeding the circumgalactic medium with metals upon eventual supernova detonation. Furthermore, high-resolution MACER3D simulations exploring dwarf galaxies reveal that AGN feedback can increase global star formation rates by approximately 25% by creating compressed gas regions where efficient cooling preserves high-density gas while radiating away thermal energy. This dual nature—where the quasar suppresses star formation in the inner disk while simultaneously triggering a wave of nucleosynthesis in the expanding outflow shell—forces a fundamental reevaluation of quasars from being purely destructive quenchers to complex, regulatory engines of galaxy assembly.   

claim_text: AGN-driven outflows exert positive feedback by compressing the interstellar medium and triggering in situ star formation directly within the outflowing molecular gas.

claim_type: debate

debate_topic: Positive vs. Negative AGN Feedback

papers:

{ arxiv_id: 2512.10924, title: "Signatures of star formation inside galactic outflows", year: 2025, stance: supports }

{ url: https://academic.oup.com/mnras/article/485/3/3409/5366743, title: "Widespread star formation inside galactic outflows", year: 2019, stance: supports }

Conclusion

The proposition that quasars act as the unilateral, primary drivers of galaxy evolution is undergoing heavy revision in the contemporary literature. While cosmological simulations mathematically require AGN feedback to quench massive galaxies and prevent overcooling, high-resolution empirical data from the JWST and ALMA era suggest a far more nuanced physical reality.

Quasar-driven molecular outflows frequently lack the requisite kinetic coupling efficiency to completely unbind global galactic gas reservoirs, indicating they act more as localized central regulators that vent energy into the halo rather than as global sweeping mechanisms. Furthermore, the necessity of major mergers as triggers for these luminous phases has been statistically challenged by large-scale surveys, heavily elevating the role of secular gas accretion and minor mergers in maintaining AGN activity. Ultimately, quasars do not operate in a vacuum. By launching fossil outflows that maintain quiescence through intermittent bursting, and by driving shockwaves that can paradoxically ignite positive star formation, luminous AGN represent a highly complex secondary regulator acting upon a galaxy already shaped heavily by its hierarchical assembly and cold-gas supply.

## Captured source anchors

- arxiv.org AGN Feedback Models and AGN Demographics I: Radio-Mode AGN in EAGLE, SIMBA and TNG100 are Inconsistent with Observations - arXiv Opens in a new window — https://arxiv.org/html/2508.04907v1
- academic.oup.com In situ versus ex situ drivers of galaxy quenching: critical black hole mass and main sequence universality in the FLAMINGO simulation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/543/3/2204/8256857
- arxiv.org Signatures of star formation inside galactic outflows - arXiv Opens in a new window — https://arxiv.org/html/2512.10924v1
- arxiv.org AGN-driven outflows in clumpy media: multiphase structure and scaling relations - arXiv Opens in a new window — https://arxiv.org/html/2407.17593v2
- arxiv.org [2603.12651] Beyond the Merger-Quasar-Quench Paradigm I: Mergers are neither necessary nor sufficient to quench central galaxies in IllustrisTNG - arXiv Opens in a new window — https://arxiv.org/abs/2603.12651
- academic.oup.com effects of stellar and AGN feedback on the cosmic star formation history in the simba simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/534/1/361/7756428
- academic.oup.com How baryons affect haloes and large-scale structure: a unified picture from the Simba simulation - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/516/1/883/6660652
- academic.oup.com Redshift evolution of galaxy group X-ray properties in the Simba simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/518/4/5826/6889524
- arxiv.org [2508.04907] AGN Feedback Models and AGN Demographics I: Radio-Mode AGN in EAGLE, SIMBA and TNG100 are Inconsistent with Observations - arXiv Opens in a new window — https://arxiv.org/abs/2508.04907
- researchgate.net Arjun Suresh's research works | New York University and other places - ResearchGate Opens in a new window — https://www.researchgate.net/scientific-contributions/Arjun-Suresh-2300107912
- academic.oup.com Cold molecular outflows in the local Universe and their feedback effect on galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/483/4/4586/27379002/sty3449.pdf
- cris.unibo.it This article has been accepted for publication in Monthly Notices of the Royal Astronomical Society©: 2019 The Authors Publishe Opens in a new window — https://cris.unibo.it/retrieve/e1dcb335-c59d-7715-e053-1705fe0a6cc9/11585_741759.pdf
- dx.doi.org High-velocity extended molecular outflow in the star-formation dominated luminous infrared galaxy ESO 320-G030 | Astronomy & Astrophysics (A&A) - Resolve a DOI Name Opens in a new window — https://dx.doi.org/10.1051/0004-6361/201628875
- arxiv.org Direct Evidence for AGN Feedback from Fast Molecular Outflows in Reionization-Era Quasars - arXiv Opens in a new window — https://arxiv.org/html/2502.05283v1
- arxiv.org [2502.05283] Direct Evidence for AGN Feedback from Fast Molecular Outflows in Reionization-Era Quasars - arXiv Opens in a new window — https://arxiv.org/abs/2502.05283
- arxiv.org arXiv:2502.05283v1 [astro-ph.GA] 7 Feb 2025 Opens in a new window — https://arxiv.org/pdf/2502.05283
- academic.oup.com Cold molecular outflows in the local Universe and their feedback effect on galaxies Opens in a new window — https://academic.oup.com/mnras/article/483/4/4586/5253620
- arxiv.org [2407.17593] AGN-driven outflows in clumpy media: multiphase structure and scaling relations - arXiv Opens in a new window — https://arxiv.org/abs/2407.17593
- researchgate.net (PDF) AGN-driven outflows in clumpy media: multiphase structure and scaling relations Opens in a new window — https://www.researchgate.net/publication/382559376_AGN-driven_outflows_in_clumpy_media_multiphase_structure_and_scaling_relations
- academic.oup.com Beyond the merger–quasar–quench paradigm I: mergers are neither necessary nor sufficient to quench central galaxies in illustrisTNG - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/548/3/stag507/8529012
- academic.oup.com mergers are neither necessary nor sufficient to quench central - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/doi/10.1093/mnras/stag507/67415544/stag507.pdf
- arxiv.org [2209.07613] Galaxy mergers can rapidly shut down star formation - arXiv Opens in a new window — https://arxiv.org/abs/2209.07613
- arxiv.org [2410.06357] Galaxy evolution in the post-merger regime. II -- Post-merger quenching peaks within 500 Myr of coalescence - arXiv Opens in a new window — https://arxiv.org/abs/2410.06357
- academic.oup.com redshift evolution of major merger triggering of luminous AGNs: a slight enhancement at z ∼ 2 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/470/1/755/3847506
- arxiv.org Interacting galaxies in the IllustrisTNG simulations - IX: Mini mergers trigger AGN in cosmological simulations - arXiv Opens in a new window — https://arxiv.org/html/2510.12738v1
- academic.oup.com Host galaxies of luminous z ∼ 0.6 quasars: major mergers are not prevalent at the highest AGN luminosities | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/466/1/812/2573007
- astrobites.org Where have all the AGN gone? - Astrobites Opens in a new window — https://astrobites.org/2026/02/10/where-agn-psb/
- arxiv.org The connection between dusty star-forming galaxies and the first massive quenched galaxies - arXiv Opens in a new window — https://arxiv.org/html/2509.26646
- academic.oup.com JWST EXCELS survey: outflows in 1.5 < z < 5 quiescent and recently quenched galaxies are likely relics from episodic AGN activity - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/advance-article/doi/10.1093/mnras/stag918/8678467
- academic.oup.com The JWST EXCELS survey: outflows in 1.5 < z < 5 quiescent and recently quenched galaxies are likely relic - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/549/3/stag918/68288890/stag918.pdf
- arxiv.org The JWST EXCELS survey: Outflows in 1.5<z<5 quiescent galaxies are likely relics from episodic AGN activity - arXiv Opens in a new window — https://arxiv.org/html/2601.02269v1
- en.wikipedia.org M–sigma relation - Wikipedia Opens in a new window — https://en.wikipedia.org/wiki/M%E2%80%93sigma_relation
- grokipedia.com M–sigma relation - Grokipedia Opens in a new window — https://grokipedia.com/page/M%E2%80%93sigma_relation
- arxiv.org [1006.0482] The non-causal origin of the black hole-galaxy scaling relations - arXiv Opens in a new window — https://arxiv.org/abs/1006.0482
- edoc.ub.uni-muenchen.de Co-evolution of galaxies and black holes - Elektronische Hochschulschriften der LMU München Opens in a new window — https://edoc.ub.uni-muenchen.de/13157/2/Hirschmann_Michaela.pdf
- academic.oup.com On the evolution of the intrinsic scatter in black hole versus galaxy mass relations Opens in a new window — https://academic.oup.com/mnras/article-pdf/407/2/1016/3897624/mnras0407-1016.pdf
- academic.oup.com Illustris simulation: the evolving population of black holes across cosmic time - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/452/1/575/1751371
- scholarlypublications.universiteitleiden.nl Dwarf galaxies and the black hole scaling relations - Scholarly Publications Leiden University Opens in a new window — https://scholarlypublications.universiteitleiden.nl/access/item%3A3263651/view
- researchgate.net Tania M. Barone's research works | Swinburne University of Technology, Melbourne and other places - ResearchGate Opens in a new window — https://www.researchgate.net/scientific-contributions/Tania-M-Barone-2175709465
- connectsci.au Dormant black hole from early universe weighs 6 billion Suns | News - ConnectSci Opens in a new window — https://connectsci.au/news/news-parent/9498/Dormant-black-hole-from-early-universe-weighs-6
- astro.tsinghua.edu.cn A Stellar Dynamical Mass Measurement of a Supermassive Black Hole in the Early Universe-DoA Opens in a new window — https://astro.tsinghua.edu.cn/en/info/1026/2851.htm
- arxiv.org Positive AGN Feedback Enhances Star Formation in Starburst Dwarf Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2510.20897v2
- arxiv.org arXiv:1408.1591v2 [astro-ph.GA] 8 Aug 2014 Opens in a new window — https://arxiv.org/pdf/1408.1591
- arxiv.org [2512.10924] Signatures of star formation inside galactic outflows - arXiv Opens in a new window — https://arxiv.org/abs/2512.10924
- academic.oup.com Widespread star formation inside galactic outflows | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/485/3/3409/5366743
- lorentzcenter.nl Settling the Dust: Obscured AGN in Galaxy Evolution - Lorentz Center Opens in a new window — https://www.lorentzcenter.nl/settling-the-dust-obscured-agn-in-galaxy-evolution.html
- arxiv.org Opening new parameter space windows on galaxy/AGN co-evolution with SKA radio continuum surveys - arXiv Opens in a new window — https://arxiv.org/html/2606.24802v1
- eso.org AGN - FAAST - ESO.org Opens in a new window — https://www.eso.org/sci/meetings/2026/AGN-FAAST.html
- academic.oup.com Quenching massive galaxies with on-the-fly feedback in cosmological hydrodynamic simulations - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/417/4/2676/1094600
- oar.princeton.edu Quasar feedback and the origin of radio emission in radio-quiet quasars Opens in a new window — https://oar.princeton.edu/bitstream/88435/pr1115h/1/stu842.pdf
- repository.cam.ac.uk A unified model for AGN feedback in cosmological simulations of structure formation - University of Cambridge Opens in a new window — https://www.repository.cam.ac.uk/bitstreams/bbbbe48c-b7b5-44eb-b292-5fee98dfa05b/download
- arxiv.org A hybrid active galactic nucleus feedback model with spinning black holes, winds and jets Opens in a new window — https://arxiv.org/html/2509.05179v2
- arxiv.org An unexpected population of quenched galaxies harbouring under-massive SMBHs revealed by tidal disruption events - arXiv Opens in a new window — https://arxiv.org/html/2601.20519v1
- arxiv.org Interpretable machine learning of halo gas density profiles: a sensitivity analysis of cosmological hydrodynamical simulations - arXiv Opens in a new window — https://arxiv.org/html/2512.09021v3
- arxiv.org CAMELS Environments: The Impact of Local Neighbours on Galaxy Evolution across the SIMBA, IllustrisTNG, ASTRID, and Swift-EAGLE Simulations - arXiv Opens in a new window — https://arxiv.org/html/2601.06290v1
- research.ed.ac.uk The effects of stellar and AGN feedback on the cosmic star formation history in the simba simulations - University of Edinburgh Research Explorer Opens in a new window — https://www.research.ed.ac.uk/en/publications/the-effects-of-stellar-and-agn-feedback-on-the-cosmic-star-format/
- cassa.site $M-\sigma$ Relation [Abekta] - CASSA Opens in a new window — https://cassa.site/abekta/un/the-m-sigma-relation
- universetoday.com Ultramassive Black Holes and Their Galaxies: A Matter of Scale - Universe Today Opens in a new window — https://www.universetoday.com/articles/ultramassive-black-holes-and-their-galaxies-a-matter-of-scale
- arxiv.org [0903.4897] The M-sigma and M-L Relations in Galactic Bulges and Determinations of their Intrinsic Scatter - arXiv Opens in a new window — https://arxiv.org/abs/0903.4897
- arxiv.org [1512.02351] The M-sigma Relation of Super Massive Black Holes from the Scalar Field Dark Matter - arXiv Opens in a new window — https://arxiv.org/abs/1512.02351
- arxiv.org AGN-driven outflows in dwarf galaxies from cosmological simulations: Internal properties and observational signatures - arXiv Opens in a new window — https://arxiv.org/pdf/2606.30726
- arxiv.org Multi-phase AGN-driven outflow in the NLSy1 IRAS 17020+4544 - arXiv Opens in a new window — https://arxiv.org/html/2603.15738v1
- etheses.whiterose.ac.uk Precise diagnostics of AGN-driven outflows - White Rose eTheses Online Opens in a new window — https://etheses.whiterose.ac.uk/id/eprint/35431/1/thesis_precise_diagnostics_of_agn_driven_outflows_final.pdf
- ras.ac.uk AGN-Driven Multiphase Outflows: Toward Consensus Between Theory and Observation Opens in a new window — https://ras.ac.uk/events-and-meetings/ras-meetings/agn-driven-multiphase-outflows-toward-consensus-between-theory-and
- indico.global SMBHs & MASSIVE GALAXIES IN THE EARLY UNIVERSE - Indico Global Opens in a new window — https://indico.global/event/13758/contributions/120035/attachments/55700/106924/MIRABEL%20at%20Armenia%20(7.01.2024).pdf
- arxiv.org SKA–VLBI view of AGN jets in the early Universe - arXiv Opens in a new window — https://arxiv.org/html/2606.28304v1
- arxiv.org Which came first: supermassive black holes or galaxies? Insights from JWST - arXiv Opens in a new window — https://arxiv.org/html/2401.02482v1
- sissa.it AGN Feedback in local galaxies : a multiphase and multiscale perspective - SISSA Opens in a new window — https://www.sissa.it/ap/phdsection/AlumniThesis/Maria%20Vittoria%20Zanchettin.pdf
- mdpi.com Observational Tests of Active Galactic Nuclei Feedback: An Overview of Approaches and Interpretation - MDPI Opens in a new window — https://www.mdpi.com/2075-4434/12/2/17
- science.nasa.gov AGN SIG Dissertation Jamboree, April 2026 - NASA Science Opens in a new window — https://science.nasa.gov/astrophysics/programs/cosmic-origins/community/agn-sig-dissertation-jamboree-april-2026/
- skyandtelescope.com Of Black Holes Galaxies - Sky & Telescope Magazine Opens in a new window — https://www.skyandtelescope.com/wp-content/uploads/Carlisle_BHsGlxs_Feb2017.pdf
- academic.oup.com Journey to the MBH–σ relation: the fate of low-mass black holes in the Universe Opens in a new window — https://academic.oup.com/mnras/article-pdf/400/4/1911/5654057/mnras0400-1911.pdf
- academic.oup.com star formation and AGN luminosity relation: predictions from a semi-analytical model | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/451/4/3759/1112264
- arxiv.org Primordial Black Hole Mergers as Probes of Dark Matter in Galactic Center - arXiv Opens in a new window — https://arxiv.org/html/2410.02591v1
- arxiv.org The Origins of Gas Accreted by Supermassive Black Holes: the Importance of Recycled Gas - arXiv Opens in a new window — https://arxiv.org/html/2312.08449v1
- sissa.it BH growth and AGN Triggering: Cosmological Simulations - SISSA Opens in a new window — https://www.sissa.it/ap/events/igbq2012/igbq2012/Tiziana_Di_Matteo_files/DiMatteo.pdf
- researchgate.net Sandro Tacchella's research works | University of Cambridge and other places - ResearchGate Opens in a new window — https://www.researchgate.net/scientific-contributions/Sandro-Tacchella-2229045946
- arxiv.org Quenching of Star Formation in Massive Galaxies - arXiv Opens in a new window — https://arxiv.org/html/2606.12156v1
- research.iac.es Observational Tests of AGN Feedback: An Overview of Approaches and Interpretation Opens in a new window — https://research.iac.es/preprints/files/PP24033.pdf
- arxiv.org AGN-driven outflows in dwarf galaxies from cosmological simulations: - arXiv Opens in a new window — https://arxiv.org/html/2606.30726v1
- scispace.com Observational Tests of Active Galactic Nuclei Feedback: An Overview of Approaches and Interpretation - SciSpace Opens in a new window — https://scispace.com/papers/observational-tests-of-active-galactic-nuclei-feedback-an-1nvqpsbamd
- academic.oup.com AGN-driven outflows in clumpy media: multiphase structure and scaling relations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/533/2/1733/7721641
- arxiv.org AGN radiative feedback as the main regulator of [O iii] outflow activity and obscuration in X-ray AGN - arXiv Opens in a new window — https://arxiv.org/html/2607.00105v1
- meetings.aip.de Multi-wavelength observations of AGN feedback Opens in a new window — https://meetings.aip.de/event/2/contributions/170/attachments/27/42/RamosAlmeida_Cristina_Thinkshop_2025.pdf
- cambridge.org Positive AGN feedback in the outskirts of nearby barred spiral galaxies? | Publications of the Astronomical Society of Australia | Cambridge Core Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/positive-agn-feedback-in-the-outskirts-of-nearby-barred-spiral-galaxies/F8A91A0910CBB83F340ED6E25EC89EFD
- ph.ed.ac.uk Publications by Adam Carnall - School of Physics and Astronomy Opens in a new window — https://www.ph.ed.ac.uk/people/adam-carnall/publications
- academic.oup.com JWST EXCELS survey: outflows in 1.5 < z < 5 quiescent and recently quenched galaxies are likely relics from episodic AGN activity | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/advance-article-abstract/doi/10.1093/mnras/stag918/8678467
- arxiv.org The JWST EXCELS survey: Insights into the nature of quenching at cosmic noon - arXiv Opens in a new window — https://arxiv.org/html/2509.18278v2
- scholar.google.pt ‪Andrea Valerio Macciò‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.pt/citations?user=zbkDqLIAAAAJ&hl=vi
- astrobites.org Does AGN feedback trigger star formation? - Astrobites Opens in a new window — https://astrobites.org/2012/09/11/does-agn-feedback-trigger-star-formation/
- researchgate.net Andrea V. Macciò Associate Professor of Physics Professor (Associate) at New York University Abu Dhabi - ResearchGate Opens in a new window — https://www.researchgate.net/profile/Andrea-Maccio/3
- www2.mpia-hd.mpg.de Coevolution » Main/Projects Opens in a new window — https://www2.mpia-hd.mpg.de/coevolution/Main/Projects
- arxiv.org Merging stellar-mass binary black holes - arXiv Opens in a new window — https://arxiv.org/pdf/1806.05820
- dash.harvard.edu Direct Cosmological Simulations of the Growth of Black Holes and Galaxies - Harvard DASH Opens in a new window — https://dash.harvard.edu/bitstreams/194d6146-a584-44fe-9591-213d6838aeaf/download
- scholar.google.com ‪David Merritt‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=7AbX6N0AAAAJ&hl=en
- pos.sissa.it Intermediate Mass Black Holes - PoS - Proceeding of science Opens in a new window — https://pos.sissa.it/306/051/pdf
- osti.gov Galaxy mergers in eagle do not induce a significant amount of black hole growth yet do increase the rate of luminous AGN (Journal Article) | OSTI.GOV Opens in a new window — https://www.osti.gov/pages/biblio/1638902
- researchgate.net Observation of Gravitational Waves from a Binary Black Hole Merger - ResearchGate Opens in a new window — https://www.researchgate.net/publication/305882033_Observation_of_Gravitational_Waves_from_a_Binary_Black_Hole_Merger
- arxiv.org [2212.10598] The interconnection between galaxy mergers, AGN activity and rapid quenching of star formation in simulated post-merger galaxies - arXiv Opens in a new window — https://arxiv.org/abs/2212.10598
- research-management.mq.edu.au Mergers trigger active galactic nuclei out to z ∼ 0.6 - Macquarie University Opens in a new window — https://research-management.mq.edu.au/ws/portalfiles/portal/134241749/134235086.pdf
- ir.library.louisville.edu Mergers trigger active galactic nuclei out to z ∼0.6 - ThinkIR Opens in a new window — https://ir.library.louisville.edu/cgi/viewcontent.cgi?article=1486&context=faculty
- academic.oup.com Role of AGN and star formation feedback in the evolution of galaxy outflows - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/535/2/1696/7609071
- phsites.technion.ac.il R. Maiolino - Negative and positive AGN feedback - AGN Driven Winds Opens in a new window — https://phsites.technion.ac.il/agn-2017/r-maiolino-negative-positive-agn-feedback/
- academic.oup.com Molecular flows in contemporary active galaxies and the efficacy of radio-mechanical feedback - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/516/1/861/6653098
- par.nsf.gov arXiv:2409.05815v3 [astro-ph.GA] 2 Dec 2024 Opens in a new window — https://par.nsf.gov/servlets/purl/10639663
- arxiv.org The Effects of Stellar and AGN Feedback on the Cosmic Star Formation History in the Simba Simulations - arXiv Opens in a new window — https://arxiv.org/html/2404.07252v1
- ucl.ac.uk Understanding the impact of feedback and cosmology on star formation and the distribution of gas within haloes - UCL Opens in a new window — https://www.ucl.ac.uk/mathematical-physical-sciences/sites/mathematical_physical_sciences/files/daniele_sorini_report_2023_0.pdf
- academic.oup.com Galaxy cold gas contents in modern cosmological hydrodynamic simulations | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/497/1/146/5866845
- arxiv.org The impact of feedback on the evolution of gas density profiles from galaxies to clusters: a universal fitting formula from the Simba suite of simulations - arXiv Opens in a new window — https://arxiv.org/html/2409.05815v2
- researchgate.net (PDF) Simba Simulation: The Effect of Feedback Physics on Matter Distribution in the Cosmic Web - ResearchGate Opens in a new window — https://www.researchgate.net/publication/393923672_Simba_Simulation_The_Effect_of_Feedback_Physics_on_Matter_Distribution_in_the_Cosmic_Web
- arxiv.org Neutral Atomic Hydrogen in a Star-forming Galaxy 7 Billion Years Ago - arXiv Opens in a new window — https://arxiv.org/html/2511.01715v1
- justinspilker.com Justin Spilker Opens in a new window — https://justinspilker.com/files/CV_Spilker.pdf
- researchgate.net The schematic location of the high Eddington ratio sources on the... | Download Scientific Diagram - ResearchGate Opens in a new window — https://www.researchgate.net/figure/The-schematic-location-of-the-high-Eddington-ratio-sources-on-the-optical-plane-pink_fig1_325841444
- researchgate.net Letizia Bugiani's research while affiliated with National Institute of Astrophysics and other places - ResearchGate Opens in a new window — https://www.researchgate.net/scientific-contributions/Letizia-Bugiani-2258561723
- researchgate.net Sirio Belli's research works | University of Bologna and other places - ResearchGate Opens in a new window — https://www.researchgate.net/scientific-contributions/Sirio-Belli-15517533
- researchgate.net Richard S. Ellis's research while affiliated with University College London and other places - ResearchGate Opens in a new window — https://www.researchgate.net/scientific-contributions/Richard-S-Ellis-9966484
- arxiv.org [2604.26195] Resolved Maps of Gas and Dust in a Massive Quiescent Galaxy at z=2 from INQUEST-JWST: Evidence of Accretion and Rejuvenation - arXiv Opens in a new window — https://arxiv.org/abs/2604.26195
- arxiv.org Resolved Maps of Gas and Dust in a Massive Quiescent Galaxy at z=2 from INQUEST-JWST: Evidence of Accretion and Rejuvenation - arXiv Opens in a new window — https://arxiv.org/html/2604.26195v1
- figshare.swinburne.edu.au Black Hole Mass Scaling Relations for Spiral Galaxies. I. MBH–M*,sph - Swinburne figshare Opens in a new window — https://figshare.swinburne.edu.au/ndownloader/files/47582897
- scispace.com Black Hole Mass Scaling Relations for Spiral Galaxies. I. M BH -M *,sph - SciSpace Opens in a new window — https://scispace.com/pdf/black-hole-mass-scaling-relations-for-spiral-galaxies-i-m-bh-449nml8qq2.pdf
- frontiersin.org Probing the Gas Fueling and Outflows in Nearby AGN with ALMA - Frontiers Opens in a new window — https://www.frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2017.00058/full
- academic.oup.com Testing the blast-wave AGN feedback scenario in MCG-03-58-007 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/489/2/1927/29579857/stz2249.pdf
- cambridge.org Feedback and Feeding in the Context of Galaxy Evolution with SPICA: Direct Characterisation of Molecular Outflows and Inflows | Publications of the Astronomical Society of Australia Opens in a new window — https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/feedback-and-feeding-in-the-context-of-galaxy-evolution-with-spica-direct-characterisation-of-molecular-outflows-and-inflows/60218C1DB8A7C142B58B5190AC3AB8B0
- repository.cam.ac.uk AGN wind scaling relations and the co-evolution of black holes and galaxies - University of Cambridge Opens in a new window — https://www.repository.cam.ac.uk/bitstreams/038e23b7-3713-4d22-9c6d-057bd542771f/download
- researchgate.net SUNRISE-3D: Sharp UNveiling of AGN feedback Regulation and its Impact on Star-formation at the cosmic noon Epoch - ResearchGate Opens in a new window — https://www.researchgate.net/publication/408300754_SUNRISE-3D_Sharp_UNveiling_of_AGN_feedback_Regulation_and_its_Impact_on_Star-formation_at_the_cosmic_noon_Epoch
- frontiersin.org Star Formation Quenching in Quasar Host Galaxies - Frontiers Opens in a new window — https://www.frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2017.00024/full
- arcadia.sba.uniroma3.it Probing the AGN/galaxy co-evolution in the widest luminosity range ever - Roma Tre Opens in a new window — https://arcadia.sba.uniroma3.it/bitstream/2307/40706/1/Tesi_FEDERICA_DURAS_XXXI.pdf
- uknowledge.uky.edu The Host Galaxies of X-Ray Selected Active Galactic Nuclei to <em>z</em> = 2.5: Structure, Star Formation, and Their - UKnowledge Opens in a new window — https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1340&context=physastron_facpub
- mdpi.com Infrared Spectral Energy Distribution and Variability of Active Galactic Nuclei: Clues to the Structure of Circumnuclear Material - MDPI Opens in a new window — https://www.mdpi.com/2218-1997/8/6/304
- publications.lib.chalmers.se STRUCTURE AND MORPHOLOGY OF X-RAY-SELECTED ACTIVE GALACTIC NUCLEUS HOSTS AT 1 < z < 3 IN THE CANDELS-COSMOS FIELD Opens in a new window — https://publications.lib.chalmers.se/records/fulltext/198389/local_198389.pdf
- pergamos.lib.uoa.gr Identification of Active Galactic Nuclei through different selection techniques Ektoras Pouliasis Opens in a new window — https://pergamos.lib.uoa.gr/uoa/dl/object/2899091/file.pdf
- arxiv.org Exploring the halo occupation distribution for moderate X-ray luminosity active galactic nuclei in the EAGLE cosmological simula - arXiv Opens in a new window — https://arxiv.org/pdf/2506.05506
- academic.oup.com The connection between mergers and AGN activity in simulated and observed massive galaxies - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article-pdf/527/3/9461/54766282/stad3836.pdf
- dilyong.com Publications - Dily Duan Yi Ong Opens in a new window — https://dilyong.com/publications/
- orcid.org Dily Duan Yi Ong - ORCID Opens in a new window — https://orcid.org/0009-0003-9958-8827
- dilyong.com Dily Duan Yi Ong Opens in a new window — https://dilyong.com/
- kicc.cam.ac.uk Dily Duan Yi Ong - Kavli Institute for Cosmology, Cambridge | Opens in a new window — https://www.kicc.cam.ac.uk/staff/dily-duan-yi-ong
- ucl.ac.uk Researchers weigh the most distant dormant black hole | UCL News Opens in a new window — https://www.ucl.ac.uk/news/2026/jun/researchers-weigh-most-distant-dormant-black-hole
- universiteitleiden.nl Cosmic magnifying glass reveals exceptionally heavy dormant black hole in the early universe - Universiteit Leiden Opens in a new window — https://www.universiteitleiden.nl/en/news/2026/06/cosmic-magnifying-glass-reveals-exceptionally-heavy-dormant-black-hole-in-the-early-universe
- courthousenews.com Astronomers detect most distant dormant black hole ever found | Courthouse News Service Opens in a new window — https://courthousenews.com/astronomers-detect-most-distant-dormant-black-hole-ever-found/
- space.com James Webb Space Telescope weighs 'sleeping giant' black hole from 10 billion light-years away — and it's 6 billion times our sun's mass Opens in a new window — https://www.space.com/astronomy/james-webb-space-telescope/james-webb-space-telescope-weighs-sleeping-giant-black-hole-from-10-billion-light-years-away-and-its-6-billion-times-our-suns-mass
- arxiv.org Empirical Calibration of Na I D and Other Absorption Lines as Tracers of High-Redshift Neutral Outflows - arXiv Opens in a new window — https://arxiv.org/html/2507.07160v2
- academic.oup.com JWST EXCELS survey: the ages and abundances of 3 < z < 5 massive quiescent galaxies show that downsizing was already in place by z ≃ 4 - Oxford Academic Opens in a new window — https://academic.oup.com/mnras/article/549/1/stag827/8666392
- arxiv.org A quiescent galaxy in a gas-rich cosmic web node at z∼3 - arXiv Opens in a new window — https://arxiv.org/html/2601.20473v3
- arxiv.org The AURORA Survey: Tracing Galactic Outflows at z≳2.5 with JWST/NIRSpec NUV Absorption Lines - arXiv Opens in a new window — https://arxiv.org/html/2506.17381v2
- researchgate.net Relation between metallicity [O/H] and chemical evolution of [C/O].... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Relation-between-metallicity-O-H-and-chemical-evolution-of-C-O-Measurements-for_fig4_360425464
- researchgate.net (PDF) No Galaxy-scale [C ii] Fast Outflow in the z = 6.72 Red Quasar HSC J1205–0000 Opens in a new window — https://www.researchgate.net/publication/388816695_No_Galaxy-scale_C_ii_Fast_Outflow_in_the_z_672_Red_Quasar_HSC_J1205-0000
- researchgate.net P-Cygni profiles (solid blue, black histograms) of the OH 119 µm and 18... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/P-Cygni-profiles-solid-blue-black-histograms-of-the-OH-119-m-and-18-OH-120-m_fig3_228923704
- researchgate.net Fig. 2. Derived line property trends with host galaxy properties. Left:... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Derived-line-property-trends-with-host-galaxy-properties-Left-Integrated-OH-optical_fig2_371071333
- researchgate.net Extreme galaxy-scale outflows are frequent among luminous early quasars - ResearchGate Opens in a new window — https://www.researchgate.net/publication/404587979_Extreme_galaxy-scale_outflows_are_frequent_among_luminous_early_quasars
- researchgate.net Comparison of the normalized 119 μm OH doublet profile to the scaled... - ResearchGate Opens in a new window — https://www.researchgate.net/figure/Comparison-of-the-normalized-119mm-OH-doublet-profile-to-the-scaled-emission-line_fig5_251566742
- arxiv.org AGN radiative feedback as the main regulator of [O iii] outflow activity and obscuration in X-ray AGNs - arXiv Opens in a new window — https://arxiv.org/html/2607.00105v2
- arxiv.org SUBWAYS: Supermassive Black Hole Winds in X-rays - arXiv Opens in a new window — https://arxiv.org/html/2603.18156v1
- orcid.org Samuel Ruthven Ward - ORCID Opens in a new window — https://orcid.org/0000-0001-5345-0900
- semanticscholar.org Mergers are neither necessary nor sufficient to quench central galaxies in IllustrisTNG | Semantic Scholar Opens in a new window — https://www.semanticscholar.org/paper/3928407b4533d1d660a6de74fd76a17605d2f226
- orcid.org Joanna M. Piotrowska - ORCID Opens in a new window — https://orcid.org/0000-0003-1661-2338
- tng-project.org Results - IllustrisTNG Opens in a new window — https://www.tng-project.org/results/
- academic.oup.com Volume 548 Issue 3 | Monthly Notices of the Royal Astronomical Society | Oxford Academic Opens in a new window — https://academic.oup.com/mnras/issue/548/3
- sciprofiles.com Douglas Rennehan - SciProfiles Opens in a new window — https://sciprofiles.com/profile/author/LzFXLy92NEwwczMrNTR6TitFck9yMXB3ZElhYmp2MlpxU0Rjdk9jVDNXWT0=?utm_source=mdpi.com&utm_medium=website&utm_campaign=avatar_name
- cgi.astronomy.osu.edu AstroCoffee Abstracts of the Day Opens in a new window — https://cgi.astronomy.osu.edu/Coffee/Archive/2025/August/2025Aug08.html
- scholar.google.com ‪Arjun Suresh‬ - ‪Google Scholar‬ Opens in a new window — https://scholar.google.com/citations?user=Xc_VAKEAAAAJ&hl=en
- repository.cam.ac.uk <i>In situ</i> versus <i>ex situ</i> drivers of galaxy ... - Apollo Opens in a new window — https://www.repository.cam.ac.uk/items/85d47718-656d-40bd-a8b9-82bd0f815423
- academic.oup.com In situ versus ex situ drivers of galaxy quenching: critical black hole Opens in a new window — https://academic.oup.com/mnras/advance-article-abstract/doi/10.1093/mnras/staf1578/8256857
- orcid.org Matthieu Schaller - ORCID Opens in a new window — https://orcid.org/0000-0002-2395-4902
- orcid.org Sandro Tacchella - ORCID Opens in a new window — https://orcid.org/0000-0002-8224-4505

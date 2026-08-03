# Galaxy Evolution — Research prospectus (Method 2, source-first)

> Proposed studies developed from the Method 2 source-first synthesis. Each prior-evidence statement links to its source basis; named surveys are proposed data to acquire, not established evidence. Non-binding, static; not accepted claims, not product-bound.

## Study 1. Quantifying the permanence of AGN-driven gas removal: an escape-versus-recycling census

**Research question.** What fraction of AGN-driven outflowing gas escapes the host halo permanently, rather than recirculating, and how does that fraction depend on stellar mass and redshift?

**Prior evidence and constraints.**
- Direct detections of quasar-driven outflows displacing star-forming gas are recorded in the source basis as an accepted primary observation.  [ [claim 2943 source basis](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#claim-2943) · [evidence 28141 / arXiv:1706.08987](https://arxiv.org/abs/1706.08987) ]
- The same basis constrains permanence: outflowing gas in massive systems can recirculate before reaching ~100 kpc.  [ [claim 2945 source basis](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#claim-2945) · [evidence 28066 / arXiv:2512.05584](https://arxiv.org/abs/2512.05584) ]
- It further establishes that winds in low-redshift, low-mass systems are comparatively inefficient at expelling gas.  [ [evidence 28075 / arXiv:0901.1880](https://arxiv.org/abs/0901.1880) ]

**Remaining uncertainty.** The escaped-versus-recirculated fraction is unquantified: no cited study relates outflow velocity to halo escape velocity across a mass- and redshift-matched sample, so a detected outflow does not establish permanent depletion of the star-forming reservoir.

### Data and measurement plan
Population: AGN hosts spanning 10^9-10^11.5 M_sun and z=0-3, with mass-matched inactive controls. MUSE and MaNGA resolve ionized-outflow velocity fields and spatially resolved quenching; ALMA CO and [C II] measure the molecular reservoir mass, depletion time, and any cold recycling gas; JWST/NIRSpec extends outflow velocities to z>2; DESI Mg II absorption traces the diffuse (~10^4 K) circumgalactic reservoir around low-mass hosts.

**Analysis and decision criterion.** For each galaxy, compare outflow velocity with halo escape velocity, and outflow kinetic energy with binding energy, classifying outflows as escaping or bound-and-recycling; regress the escaped fraction on stellar mass and redshift against the control denominator. A monotonic escaped-fraction relation that exceeds recycling above a mass threshold would support permanent removal; a flat or low fraction would favour recycling-dominated regulation.

**Limitations.** Multiphase gas is only partially traced; escape velocity is inferred; samples are biased toward luminous nuclei. Non-binding, static candidate.

_Provenance: Method2 source rows: 28141 (claim 2943); 28066, 28075 (claim 2945)._

## Study 2. An observational bound on AGN maintenance heating: cavity enthalpy versus cooling luminosity

**Research question.** Does the mechanical power deposited by AGN into group- and cluster-scale hot atmospheres balance their radiative cooling across the halo mass function, and over what duty cycle?

**Prior evidence and constraints.**
- In the source basis, maintenance heating is supported predominantly by cosmological simulations that require AGN feedback to prevent over-production of massive galaxies.  [ [claim 2946 source basis](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#claim-2946) · [evidence 28089 / arXiv:2508.06707](https://arxiv.org/abs/2508.06707) · [evidence 28123 / arXiv:2403.17145](https://arxiv.org/abs/2403.17145) ]
- Its single direct observational anchor is X-ray cavities inflated in hot atmospheres.  [ [evidence 28158 / arXiv:2403.17145](https://arxiv.org/abs/2403.17145) ]

**Remaining uncertainty.** Whether observed cavity enthalpy matches cooling luminosity across a mass-selected sample, and how episodic that balance is, remains unmeasured; the ledger provides one observation against simulation-based inference.

### Data and measurement plan
Population: a mass-selected sample of hot atmospheres from eROSITA, with Chandra and XMM-Newton providing cavity enthalpy, temperature and density profiles, and cooling luminosity; VLA and LOFAR provide jet power and duty cycle linking cavities to active episodes; ALMA and optical IFU measure residual central cooling and star formation.

**Analysis and decision criterion.** Compute heating power (cavity enthalpy divided by buoyancy time, scaled by jet duty cycle) against cooling luminosity per halo across the mass function. A heating-to-cooling ratio consistent with unity over the duty cycle would elevate maintenance heating from model-dependent to observationally bounded; a systematic deficit would refute observational sufficiency.

**Limitations.** Cavity detection is sensitivity-limited; samples shrink at high redshift; the balance is time-variable. Non-binding, static candidate.

_Provenance: Method2 source rows: 28089, 28123 (model-bounded), 28158 (X-ray cavity), claim 2946._

## Study 3. Measuring the coupling efficiency of radio-mode jets to galaxy gas

**Research question.** What is the distribution of efficiencies with which radio jets deposit mechanical power into surrounding galaxy gas, and how does it depend on environment?

**Prior evidence and constraints.**
- The source basis supports a kinetic, radio-mode channel primarily through review-level synthesis rather than a single primary detection.  [ [claim 2947 source basis](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#claim-2947) · [evidence 28095 / arXiv:2009.11175](https://arxiv.org/abs/2009.11175) ]
- It is accompanied by one radio-mode observation in massive radio galaxies.  [ [evidence 28131 / arXiv:0901.1880](https://arxiv.org/abs/0901.1880) ]
- The basis explicitly cautions that jet-to-gas coupling can be weak.  [ [evidence 28108 / arXiv:2009.11175](https://arxiv.org/abs/2009.11175) · [evidence 28062 / arXiv:2508.06707](https://arxiv.org/abs/2508.06707) ]

**Remaining uncertainty.** The coupling-efficiency distribution across a radio-selected sample is unmeasured: how frequently jets disturb the gas rather than pass through it, and its environmental dependence, are unconstrained.

### Data and measurement plan
Population: a radio-selected sample with VLA, LOFAR, and MeerKAT providing jet power, morphology, and duty cycle; Chandra and XMM providing jet-inflated cavities as a mechanical-work calorimeter; MaNGA and MUSE resolving jet-interstellar interaction, shocked-gas line ratios, and local star-formation suppression; IllustrisTNG- and HORIZON-AGN-style simulations supplying coupling-efficiency priors to test against.

**Analysis and decision criterion.** Per galaxy, derive coupling efficiency as the ratio of energy deposited in the gas to jet mechanical power, and compare its distribution with the simulation priors. A distribution peaked at high efficiency would support generic radio-mode effectiveness; a broad or low-efficiency distribution would establish environment-gated coupling.

**Limitations.** Radio-mode activity is episodic and environment-dependent; matched multi-wavelength samples are expensive. Non-binding, static candidate.

_Provenance: Method2 source rows: 28095 (review), 28131 (radio-mode), 28108, 28062 (cautions), claim 2947._

## Study 4. Testing the generality of M51-scale kinetic and positive feedback

**Research question.** Do the low-power kinetic mode and locally positive, star-formation-triggering feedback characterized in M51 recur across the nearby active-galaxy population, and at what frequency?

**Prior evidence and constraints.**
- A group of scoped results in the source basis derives from the single galaxy M51, and is flagged as potentially non-general.  [ [claim 2942 source basis](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#claim-2942) · [evidence 28074 / arXiv:2604.15438](https://arxiv.org/abs/2604.15438) ]
- These include a preserved caution that AGN feedback can be locally positive, compressing gas and triggering star formation, with no dedicated claim.  [ [M51 positive-feedback caution](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#claim-none) · [evidence 28060 / arXiv:2604.15438](https://arxiv.org/abs/2604.15438) ]

**Remaining uncertainty.** The population frequency of low-power kinetic and positive feedback is unknown; whether M51 is representative or peculiar, and whether positive feedback is common enough to constitute a distinct claim, is untested.

### Data and measurement plan
Population: nearby active galaxies with PHANGS-style ALMA and MUSE, plus MaNGA, resolving molecular gas and star-formation maps to identify M51-like compression-triggered star formation at jet and outflow interfaces, with mass-matched inactive controls to isolate the nucleus.

**Analysis and decision criterion.** Define M51 diagnostic signatures and measure the fraction of the resolved sample exhibiting local positive versus negative feedback relative to controls. A frequency exceeding a preset threshold with consistent diagnostics would justify promoting positive feedback to a distinct claim; a low frequency would confirm it as a single-galaxy exception.

**Limitations.** Resolved multiphase data are limited to nearby galaxies; positive and negative feedback can coexist. Non-binding, static candidate.

_Provenance: Method2 M51 rows: 28074, 28091, 28155 (claim 2942/2943); 28060 (positive-feedback caution)._

## Study 5. Locating the stellar-to-AGN feedback transition mass in quenching

**Research question.** At what stellar or halo mass does stellar feedback become unable to quench a galaxy unaided, so that AGN feedback becomes necessary?

**Prior evidence and constraints.**
- The source basis establishes that stellar feedback drives strong outflows and baryon deficiency in low-mass galaxies, scaling with star-formation rate.  [ [claim 2944 source basis](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#claim-2944) · [evidence 28069 / arXiv:2512.05584](https://arxiv.org/abs/2512.05584) ]
- It also reports that stellar feedback alone is generally insufficient to fully quench high-mass galaxies.  [ [evidence 28088 / arXiv:2605.03008](https://arxiv.org/abs/2605.03008) ]

**Remaining uncertainty.** The transition mass separating the stellar-sufficient and AGN-required regimes is unmeasured; the ledger states the two endpoints but not the boundary.

### Data and measurement plan
Population: galaxies spanning the stellar-mass function at fixed redshift, with DESI and MOSDEF measuring outflow mass-loading and quenched fractions, JWST/NIRSpec targeting high-redshift massive quiescent systems, ALMA measuring cold-gas depletion times, and GAMA and COSMOS supplying mass- and redshift-matched denominators.

**Analysis and decision criterion.** Regress outflow mass-loading factor and quenched fraction on stellar and halo mass to identify the mass at which the stellar-feedback energy and momentum budget falls below the quenching requirement, and test whether AGN indicators rise above that mass. A sharp budget crossover coincident with rising AGN incidence would locate the transition; a smooth trend without a crossover would refute a single transition mass.

**Limitations.** Stellar and nuclear contributions are degenerate and require careful sample matching. Non-binding, static candidate.

_Provenance: Method2 source rows: 28069, 28073 (low-mass stellar outflows), 28088 (high-mass insufficiency), claim 2944._

## Study 6. Strengthening evidence traceability: citation-linking, full-text verification, and reconsideration criteria (methods programme)

**Research question.** Which elements of the underlying evidence base would most alter the synthesis if citation-linked or fully verified, and under what criteria would set-aside evidence be reconsidered?

**Prior evidence and constraints.**
- The source basis records that much of its support was adjudicated from abstracts rather than full text.  [ [P1 source-position ledger](../p1-source-position-ledger.html) ]
- It records that local source judgments are not yet matched to citable literature records.  [ [P2 claim-status ledger](../p2-claim-status-ledger.html) ]
- It preserves a set of positions set aside as off-topic, duplicated, or wrong in scale.  [ [set-aside positions](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#held-out) ]

**Remaining uncertainty.** Which abstract-only positions would change a conclusion if verified, and which set-aside positions would be reinstated under new evidence, has not been prioritized.

### Data and measurement plan
Documentation-only inputs: NASA ADS and the local bibliography to match each local source judgment to a citable record (a future citation-linking step, metadata only); the existing local corpus to rank abstract-only positions for full-text verification. No new observations are proposed.

**Analysis and decision criterion.** Construct a proposed source-judgment-to-citable-record mapping, rank abstract-only positions by conclusion sensitivity, and pair each set-aside reason with the specific evidence that would overturn it. The programme succeeds when it yields a prioritized verification queue and explicit, auditable reconsideration criteria.

**Limitations.** Citation-linking and any change of verification status are separate gated steps not performed here; catalogue metadata only. Non-binding, static candidate.

_Provenance: Method2 evidence-accounting state: abstract-only positions, unlinked source judgments, and the twelve set-aside positions._

<!-- AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z — Method2 journal prospectus · docs-only · prior-evidence linked · no product claim/cite -->

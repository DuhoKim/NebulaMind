# Galaxy Evolution — Research proposals on outflows and feedback regimes

> This page presents one SDSS denominator baseline and three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.

**AAS pilot PDFs.** Actual-data SDSS DR17 pilot manuscripts are available for the three focused programmes below:

- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)

P0 is the local SDSS baseline used to define the denominator and stress-test selection effects.

## P0 — Denominator-controlled optical AGN associations in SDSS

**Hypothesis / objective.** BPT-selected optical AGN hosts have lower catalog sSFR than carefully matched star-forming controls, but some or all of the offset may come from selection, aperture, dust, and denominator effects rather than feedback.

**Primary observables.** Median $\Delta\log\mathrm{sSFR}$, the matched-pair distribution width, the fraction of pairs that remain offset after reweighting, and the stability of the result across AGN tracers and control definitions.

**Prior evidence and constraints.** The local RP-1 SDSS pilot is a denominator-design baseline, not causal proof: it reports 8,146 matched AGN/control pairs and a median $\Delta\log\mathrm{sSFR}$ of -1.309 dex, with bootstrap interval [-1.334, -1.283]. The same pilot uses a 60,000-row capped cache covering 24.0% of a strict 249,917-row four-line $S/N \ge 3$ parent.

**Control plan.** Rebuild the denominator with full SDSS DR17 access, then compare BPT, WISE, radio, X-ray, and morphology-selected AGN hosts across matched bins in stellar mass, redshift, inclination, dust, fiber coverage, local density, and emission-line signal-to-noise. Use at least two control constructions: nearest-neighbor matching and propensity-score weighting. Repeat the analysis with and without aperture-fraction cuts to separate nuclear from galaxy-wide effects.

**Decision criterion.** The association is interesting only if the sSFR offset survives control redesign, weighting, and AGN-tracer swaps, and if the same hosts also show coherent gas-reservoir or outflow differences. If the offset collapses under those tests, the result should be treated as a selection effect rather than as evidence for quenching.

**Limitations and wording guardrails.** Catalog SFR systematics, aperture bias, AGN detectability, and missing gas diagnostics can all inflate the offset. This proposal should be described as an association and denominator test, not as proof of causal AGN quenching.

## P1 — Escape versus recycling: the fate of AGN-driven multiphase outflows

**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, so feedback may regulate gas supply without permanently removing it.

**Primary observables.** Phase-resolved outflow velocity, line width, and mass-loading; the ratio of outflow speed to halo escape speed; the presence of the same material in later CGM measurements; and whether the gas reappears as cool, warm, or hot gas.

**Prior evidence and constraints.** Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but those detections do not determine whether gas escapes the halo. Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. Simulated feedback constraints show that gas removal, recycling, and observable baryon fractions depend on halo scale.

**Control plan.** Assemble AGN hosts and inactive controls matched in stellar mass, halo mass, redshift, inclination, star-formation rate, and merger stage. Use MUSE and MaNGA for ionized-gas kinematics, ALMA CO and [C II] for cold gas, JWST/NIRSpec for $z \gt 2$ outflow tracers, and CGM absorption where available to follow recycling. Apply a shared escape-speed estimator, fixed aperture definitions, and the same outflow-mass conversion assumptions to every phase.

**Decision criterion.** The result favors permanent removal if the median escaping fraction is above one-half in the matched sample and the same gas does not reappear in later CGM measurements. The result favors recycling-limited regulation if most of the gas remains below escape speed or returns in a later halo measurement. Mixed behavior should be treated as phase-dependent regulation, not as a binary outcome.

**Limitations and wording guardrails.** Projection effects, phase conversion, uncertain halo potentials, incomplete time baselines, and sample censoring can dominate the escaped-fraction error budget. The proposal should therefore be framed as a bound on fate, not as a direct census of all expelled mass.

## P2 — Environmental dependence of radio-jet coupling efficiency in galaxy gas

**Hypothesis / objective.** The fraction of radio-jet mechanical power deposited into the multiphase interstellar or circumgalactic medium varies systematically with ambient gas density and host environment.

**Primary observables.** Coupling efficiency estimated from cavities, shocks, disturbed gas, and gas depletion, measured relative to jet power within matched apertures around the same host population.

**Prior evidence and constraints.** Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. Local M51-scale NOEMA data show how jet or AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas.

**Control plan.** Use VLA, LOFAR, and MeerKAT for jet morphology and radio spectral ages; Chandra for cavities, shocks, and hot gas; MUSE and MaNGA for ionized-gas shock diagnostics; ALMA CO for molecular disturbances; and group catalogues for environment. Match on jet age, jet power, stellar mass, halo mass, gas fraction, and local density, then compare field, group, and cluster subsamples with the same selection cuts. Separate sources by host inclination and compact-versus-extended radio morphology so that projection does not masquerade as coupling.

**Decision criterion.** A robust environmental dependence is present if coupling efficiency shifts systematically with density or group membership after correcting for radio-power calibration, jet age, morphology, and aperture choice, and if an environment term improves out-of-sample prediction relative to a jet-power-only model. If the response is flat once controls are applied, environment is a secondary effect.

**Limitations and wording guardrails.** Radio-to-jet-power conversions are uncertain; cavity detectability, viewing angle, and phase mixing can also blur the coupling signal. The analysis should be read as a test of coupling efficiency, not as a direct measure of total feedback energy.

## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation

**Hypothesis / objective.** There is a mass regime where stellar-feedback momentum and energy budgets stop explaining gas loss or quiescence, and AGN-linked observables become necessary to reproduce the observed quenched fraction and baryon deficit.

**Primary observables.** The break mass or transition surface in gas fraction, quenched fraction, depletion time, and baryon deficit as functions of stellar mass and halo mass.

**Prior evidence and constraints.** Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. High-redshift environmental-quenching simulations emphasize that quenching mechanisms vary with mass and redshift, not only with local observables. Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties.

**Control plan.** Build DESI, GAMA, and COSMOS parent samples with stellar-mass and halo proxies; add ALFALFA and FASHI H I plus ALMA CO gas fractions; measure optical and IR star-formation rates; add X-ray and radio AGN indicators; and extend to high redshift with JWST, targeting $z \gt 2$ where possible. Fit the same pipeline to both field and environment-rich subsamples so that the transition can be separated from group processing. Use a field-only denominator first, then repeat with matched group and cluster controls to test whether the break persists after environment correction.

**Decision criterion.** Fit single-slope and broken-slope models for gas fraction, baryon deficit, depletion time, and quenched fraction, and include an AGN-incidence term. The transition is credible only if the broken-slope or transition model improves on the single-slope baseline, the AGN-linked term adds predictive power beyond stellar-feedback proxies at high mass, and the result remains stable under cross-validation. If the improvement vanishes when halo proxies or control sets are swapped, the transition is not secure.

**Limitations and wording guardrails.** Halo-mass uncertainty, selection functions, and survey incompleteness can smear the break; results should be framed as a probability surface rather than as one universal transition mass. This is a regime-finding program, not a claim that every galaxy crosses the same threshold at the same time.

## Methodological note

- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.

## Scope note

These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.

# Galaxy Evolution — Research proposals on outflows and feedback regimes

> This page presents one SDSS denominator baseline and three proposal-style research programmes on outflow fate, jet coupling, and the transition from stellar-feedback to AGN-linked regulation. The proposals are framed around measurable observables, matched denominators, and explicit decision criteria.

**AAS pilot PDFs.** The local SDSS DR17 pilot manuscripts linked below motivate the three focused programmes.

- P1: [SDSS high-excitation AGN denominator for outflow escape tests: an SDSS DR17 pilot (PDF)](m2_p1_outflow_escape_recycling_aas.pdf)
- P2: [Environment proxy for optical AGN in massive SDSS hosts: an SDSS DR17 pilot (PDF)](m2_p2_radio_jet_environment_aas.pdf)
- P3: [SDSS mass transition in quenching and optical AGN incidence: an SDSS DR17 pilot (PDF)](m2_p3_feedback_transition_mass_aas.pdf)

P0 is the local SDSS baseline used to define the denominator and stress-test selection effects.

## P0 — Denominator-controlled optical AGN associations in SDSS

**Hypothesis / objective.** Optical AGN hosts selected via the Baldwin-Phillips-Terlevich (BPT) line-ratio diagram, using the [O III]/H-beta versus [N II]/H-alpha plane, have lower catalog sSFR than matched star-forming controls. The offset may still be partly driven by selection bias, aperture limits, dust, or denominator construction rather than by physical feedback.

**Primary observables.** Median $\Delta\log\mathrm{sSFR}$, the matched-pair residual distribution, the fraction of pairs that remain offset after reweighting, and the stability of the result across AGN tracers (BPT, WISE, radio, X-ray) and control definitions. Where available, compare these with H-alpha equivalent width and the 4000 Å break index ($\mathrm{D}_n(4000)$), which help separate current star formation from older stellar populations so the offset is not judged from a single SFR estimator. If the gas data are available, add molecular gas mass and depletion time as a secondary check, but do not make the proposal depend on them.

**Prior evidence and constraints.** The local RP-1 SDSS pilot is a denominator-design baseline and association stress test, not causal proof: it reports 8,146 matched AGN/control pairs and a median $\Delta\log\mathrm{sSFR}$ of -1.309 dex, with bootstrap interval [-1.334, -1.283]. The same pilot uses a 60,000-row capped cache covering 24.0% of a strict 249,917-row four-line $S/N \ge 3$ parent.

**Control plan.** Rebuild the denominator with full SDSS DR17 access, then compare BPT, WISE, radio, X-ray, and morphology-selected AGN hosts across matched bins in stellar mass, redshift, inclination, dust, fiber coverage, local density, and emission-line signal-to-noise. Use at least two control constructions: nearest-neighbor matching and propensity-score weighting. Add a second denominator that is restricted to the same emission-line quality as the active sample, and repeat the analysis with and without aperture-fraction cuts to separate nuclear from galaxy-wide effects. If possible, include inactive galaxies with the same line-measurement quality as a negative control so the result is not driven by detectability alone. The primary path is a full-sample SDSS comparison; the fallback path is a strict line-quality subset that can still test whether the offset survives tighter selection.

**Decision criterion.** Treat the association as robust only if all three conditions hold: (1) the median sSFR offset exceeds the systematic uncertainty threshold ($|\Delta\log\mathrm{sSFR}| \gt 0.3$ dex) under both nearest-neighbor matching and propensity-score weighting; (2) the offset remains statistically significant ($\ge 3\sigma$) when swapping BPT selection for WISE mid-infrared or radio selection; and (3) the matched active hosts show a coherent decrease in molecular gas mass, shorter depletion times, or stronger outflow signatures. If the offset falls below $0.3$ dex, or disappears when the denominator is tightened to the same line-measurement quality, it should be classified as a selection or aperture effect rather than a physical AGN-linked suppression signal.

**Limitations and wording guardrails.** Catalog SFR systematics, aperture bias, AGN detectability, dust, and missing gas diagnostics can all inflate the offset. This proposal should be described as an association and denominator test, not as proof of causal AGN quenching.

## P1 — Escape versus recycling: the fate of AGN-driven multiphase outflows

**Hypothesis / objective.** A substantial fraction of AGN-driven outflowing gas remains gravitationally bound and recycles through the circumgalactic medium, so feedback may regulate gas supply without permanently removing it.

**Primary observables.** Outflow velocity ($v_{\mathrm{out}}$ from Doppler-shifted lines), emission line width ($\sigma$), and mass-loading ($\eta$) in ionized ([O III]), molecular (CO), and neutral (Na I D) gas phases; the ratio of outflow speed to halo escape speed ($v_{\mathrm{out}}/v_{\mathrm{esc}}$, where $v_{\mathrm{esc}}$ is derived from a stellar-mass-scaled NFW halo model); circumgalactic medium (CGM) column densities ($N(\mathrm{H\,I})$) and line ratios (e.g., $\mathrm{O\,VI}/\mathrm{Mg\,II}$) at matched impact parameters; and return signatures such as secondary absorption components. The core observable is whether each phase is kinematically bound or unbound, not whether an outflow is simply detected.

**Prior evidence and constraints.** Quasar observations show AGN feedback acting on molecular gas reservoirs at high redshift, but those detections do not determine whether gas escapes the halo. Stellar-feedback work on baryon deficiency in low-mass galaxies provides a boundary condition for non-AGN removal channels that must not be confused with AGN-driven escape. Simulated feedback constraints show that gas removal, recycling, and observable baryon fractions depend on halo scale.

**Control plan.** Assemble AGN hosts and inactive controls matched in stellar mass, halo mass, redshift, inclination, star-formation rate, and merger stage. Use MUSE and MaNGA for ionized-gas kinematics, ALMA CO and [C II] for cold gas, JWST/NIRSpec for $z \gt 2$ outflow tracers, and CGM absorption where available to follow recycling. Apply a shared escape-speed estimator, fixed aperture definitions, and the same outflow-mass conversion assumptions to every phase. When possible, compare inner-galaxy outflow tracers with background-sightline CGM tracers in the same halo so that escape and return are not inferred from one dataset alone. The primary path is a matched multi-phase sample; the fallback path is a phase-limited analysis that still uses the same escape-speed model across all objects.

**Decision criterion.** Permanent removal is favored if the median inferred escaping fraction is $> 50\%$ across the matched active sample and the CGM at large impact parameters ($R \gt 100\ \text{kpc}$) shows elevated metal column densities without comparable returning or infalling components. Recycling-limited regulation is favored if $> 70\%$ of the outflowing mass has $v_{\mathrm{out}} \lt v_{\mathrm{esc}}$ and background sightlines reveal returning or infalling gas kinematics that are consistent with the host rotation. If the escaping and bound fractions overlap strongly after matching, the safer conclusion is that the data do not distinguish escape from recycling.

**Limitations and wording guardrails.** Projection effects, phase conversion, uncertain halo potentials, incomplete time baselines, and sample censoring can dominate the escaped-fraction error budget. The proposal should therefore be framed as a bound on fate, not as a direct census of all expelled mass.

## P2 — Environmental dependence of radio-jet coupling efficiency in galaxy gas

**Hypothesis / objective.** The fraction of radio-jet mechanical power deposited into the multiphase interstellar or circumgalactic medium varies systematically with ambient gas density and host environment.

**Primary observables.** Cavity enthalpy ($4PV$, where $P$ is pressure and $V$ is volume from Chandra X-ray imaging), shock temperature jumps, disturbed line widths and velocity offsets of molecular (CO) and ionized ([O III]) gas, and jet power ($P_{\mathrm{jet}}$ estimated from radio luminosity and spectral aging). The mechanical coupling efficiency parameter is defined as $\eta = P_{\mathrm{cav}} / P_{\mathrm{jet}}$. A useful secondary observable is whether the same host shows both a hot-gas cavity and cold-gas disturbance, because that helps separate coupling from simple jet presence.

**Prior evidence and constraints.** Young radio galaxies show AGN-driven outflows and provide an empirical route to estimating feedback efficiency. Local M51-scale NOEMA data show how jet or AGN activity can affect molecular ISM structure at high spatial resolution, motivating a broader population test. Galaxy-group feedback studies identify the group regime as a strong testbed for coupling between radio activity and hot gas.

**Control plan.** Use VLA, LOFAR, and MeerKAT for jet morphology and radio spectral ages; Chandra for cavities, shocks, and hot gas; MUSE and MaNGA for ionized-gas shock diagnostics; ALMA CO for molecular disturbances; and group catalogues for environment. Match on jet age, jet power, stellar mass, halo mass, gas fraction, and local density, then compare field, group, and cluster subsamples with the same selection cuts. Separate sources by host inclination and compact-versus-extended radio morphology so that projection does not masquerade as coupling. The primary path is a cavity-plus-jet sample with X-ray coverage; the fallback path is a radio-plus-optical/CO sample that still tests whether disturbed gas tracks environment.

**Decision criterion.** A robust environmental dependence is present if the coupling efficiency parameter $\eta$ is significantly higher in group or cluster cores compared to matched field environments by a factor of $\ge 2$, with a statistical significance of $\ge 3\sigma$ after controlling for jet morphology, radio-power calibration, and aperture effects. If the difference is $\lt 1\sigma$ or non-systematic, treat the result as no evidence for environment dependence under these controls.

**Limitations and wording guardrails.** Radio-to-jet-power conversions are uncertain; cavity detectability, viewing angle, and phase mixing can also blur the coupling signal. The analysis should be read as a test of coupling efficiency, not as a direct measure of total feedback energy.

## P3 — Locating the transition from stellar-feedback to AGN-feedback regulation

**Hypothesis / objective.** There is a mass regime where stellar-feedback momentum and energy budgets stop explaining gas loss or quiescence, and AGN-linked observables become necessary to reproduce the observed quenched fraction and gas depletion pattern. The transition mass should be inferred from the data, not fixed in advance.

**Primary observables.** Gas fraction ($f_{\mathrm{gas}} = M_{\mathrm{gas}}/M_*$), H I and CO depletion times ($t_{\mathrm{dep}} = M_{\mathrm{gas}}/\mathrm{SFR}$), quenched fraction ($f_{\mathrm{q}}$), star-formation efficiency, halo-gas X-ray luminosity ($L_{\mathrm{X}}$), and optical/IR/radio AGN incidence. The transition scale is the fitted break or change-point in these trends, reported with uncertainty. The most informative comparison is the joint trend of gas fraction and quiescent fraction at fixed stellar mass and environment.

**Prior evidence and constraints.** Low-mass baryon deficiency attributed to stellar feedback provides the low-mass endpoint of the transition problem. High-redshift environmental-quenching simulations emphasize that quenching mechanisms vary with mass and redshift, not only with local observables. Simulated observable-property constraints show why feedback-regime boundaries must be tested against measured baryonic properties.

**Control plan.** Build DESI, GAMA, and COSMOS parent samples with stellar-mass and halo proxies; add ALFALFA and FASHI H I plus ALMA CO gas fractions; measure optical and IR star-formation rates; add X-ray and radio AGN indicators; and extend to high redshift with JWST, targeting $z \gt 2$ where possible. Fit the same pipeline to both field and environment-rich subsamples so that the transition can be separated from group processing. Use a field-only denominator first, then repeat with matched group and cluster controls to test whether the break persists after environment correction. Report the transition mass as a fitted output with confidence intervals, and compare the result across control definitions rather than forcing a single target value. The primary path is a low-redshift multi-survey sample; the fallback path is a smaller but cleaner subset in which gas fractions, quenched fractions, and AGN indicators are all measured consistently.

**Decision criterion.** The transition is considered robust if a broken-slope or change-point model improves the fit quality over a single-slope model for the quenched fraction and gas fraction trends, verified by an Akaike Information Criterion improvement of $\Delta\mathrm{AIC} \gt 10$ and a Bayesian Information Criterion improvement of $\Delta\mathrm{BIC} \gt 10$. The inferred break must remain stable under 10-fold cross-validation and under the main control variants, with the posterior on the transition scale remaining narrow enough that the break location is identifiable rather than smeared across the full mass range. If the break shifts outside the quoted confidence interval when environment is controlled, the result should be treated as environment-driven rather than as a clean feedback-regime transition.

**Limitations and wording guardrails.** Halo-mass uncertainty, selection functions, and survey incompleteness can smear the break; results should be framed as a probability surface rather than as one universal transition mass. This is a regime-finding program, not a claim that every galaxy crosses the same threshold at the same time.

## Methodological note

- Evidence-traceability work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.

## Scope note

These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.

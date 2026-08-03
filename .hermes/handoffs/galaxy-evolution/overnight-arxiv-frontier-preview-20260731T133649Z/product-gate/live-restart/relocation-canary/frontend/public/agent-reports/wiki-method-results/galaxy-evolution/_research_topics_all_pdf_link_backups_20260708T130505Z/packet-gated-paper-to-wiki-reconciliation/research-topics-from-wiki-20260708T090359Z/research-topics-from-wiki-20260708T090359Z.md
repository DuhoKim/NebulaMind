# Galaxy Evolution — Research proposals on AGN feedback, quenching, and environment

> This page presents three proposal-style research programmes on galaxy quenching and feedback. Each proposal states a falsifiable objective, the prior evidence motivating it, the unresolved measurement, the proposed survey data, the analysis test, and the wording limits that keep the conclusion appropriately bounded.

**AAS pilot PDF.** A first actual-data SDSS DR17 pilot manuscript generated from the AGN-feedback proposal is available as [A Matched-Control SDSS DR17 Pilot Test of Specific Star Formation in Optical AGN Hosts (PDF)](sdss_agn_sfr_pilot_aas.pdf).

3 proposal-style research programmes.

## RP-1 — Observational constraints on the suppression of star formation by AGN feedback

**Hypothesis / objective.** AGN hosts exhibit a measurable star-formation deficit relative to inactive galaxies matched in stellar mass, morphology, halo environment, and redshift only when the feedback energy budget can couple to the molecular or ionized gas reservoir.

**Prior evidence and constraints.**
- M51-scale NOEMA evidence motivates a spatially resolved test of how AGN activity perturbs the local interstellar medium, but a nearby case cannot by itself establish population-level quenching. [SWAN IV / M51 AGN feedback](https://arxiv.org/abs/2604.15438).
- High-redshift quasar observations directly connect AGN activity to disturbed molecular gas reservoirs, motivating a molecular-gas denominator for any causal quenching test. [quasar molecular-gas reservoir evidence](https://arxiv.org/abs/1706.08987).
- The local coverage record still treats the broad causal AGN-quenching statement as unsettled, so the proposal must test causality rather than restate it as established. [local coverage record for broad AGN-quenching statement](../prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json).

**Remaining uncertainty.** The unresolved issue is not whether AGN and quiescence coexist, but whether AGN power predicts a deficit in star formation after matching on the covariates that also correlate with quenching.

**Survey/data plan.** Parent sample: MaNGA or MUSE IFU AGN hosts and inactive controls matched in stellar mass, morphology, halo mass/environment, and redshift; ALMA CO for molecular gas mass and depletion time; Chandra/XMM/eROSITA for radiative and mechanical AGN power proxies; VLA/LOFAR for radio-mode duty cycle.

**Analysis/test and decision criterion.** Fit a hierarchical matched-control model in which resolved star-formation deficit, gas fraction, and depletion time are predicted by AGN power after controlling for mass, morphology, and environment. The hypothesis is supported only if the AGN coefficient remains significant and the inferred energy budget can plausibly affect the measured gas phase; otherwise the result bounds or rejects a causal interpretation.

**Limitations and wording guardrails.** AGN duty cycles, obscuration, and residual matching errors can mimic causal suppression; the result should be framed as a constraint on feedback coupling, not a proof of universal AGN quenching.

## RP-2 — Separating internal and environmental quenching across stellar mass, halo mass, and redshift

**Hypothesis / objective.** Environmental quenching contributes an excess quenched fraction at fixed stellar mass below a halo- and redshift-dependent transition, whereas internal/AGN-linked channels dominate at higher stellar or halo mass.

**Prior evidence and constraints.**
- Local simulations compared to SDSS explicitly frame quenching as a joint environment-plus-AGN problem rather than a single-channel process. [environment and AGN quenching versus SDSS](https://arxiv.org/abs/2401.12953).
- Euclid Q1 results motivate a morphology/environment sequence in which dense environments can quench before bulge formation, while field evolution may follow a different order. [Euclid Q1 quenching sequence](https://arxiv.org/abs/2511.02964).
- HI studies of AGN-hosting and satellite galaxies provide a gas-reservoir observable for separating central and satellite pathways. [HI gas in AGN and satellite galaxies](https://arxiv.org/abs/2606.25367).

**Remaining uncertainty.** The main unknown is the transition surface in stellar mass, halo mass, satellite/central status, and redshift where environmental effects become separable from internal mass-linked quenching.

**Survey/data plan.** Low redshift: SDSS, GAMA, ALFALFA/FASHI HI, and group catalogues for stellar mass, halo proxy, central/satellite status, and quenched fraction. Intermediate/high redshift: COSMOS/CANDELS/JWST fields for SFR and morphology; Euclid and DESI for larger-scale environment and redshift completeness.

**Analysis/test and decision criterion.** Estimate quenched-fraction excess in a multivariate model with stellar mass, halo/environment, central/satellite label, morphology, and redshift. A credible environmental channel requires an excess that persists at fixed stellar mass and halo proxy with controlled central/satellite classification.

**Limitations and wording guardrails.** Group membership and halo masses are noisy, and pre-processing can be misclassified as cluster quenching; results should be reported as a transition map with uncertainty bands.

## RP-3 — Empirical duty-cycle constraints on AGN maintenance heating in massive halos

**Hypothesis / objective.** For massive central galaxies and groups, the time-averaged mechanical power from radio-mode AGN balances hot-halo cooling often enough to maintain low star-formation rates.

**Prior evidence and constraints.**
- Observed/simulated central-galaxy comparisons support integrated AGN feedback as relevant to quenching but do not by themselves measure a population duty cycle. [central-galaxy quenching and integrated AGN feedback](https://arxiv.org/abs/2112.07672).
- IllustrisTNG quenched-fraction work identifies AGN feedback, environment, and preprocessing as separable model ingredients, motivating observational tests rather than simulation restatement. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
- Galaxy groups are highlighted as a sensitive regime for testing AGN feedback energetics in hot atmospheres. [galaxy groups as AGN feedback probes](https://arxiv.org/abs/2403.17145).
- Chaotic cold accretion and dual jet-heating models provide mechanisms for self-regulated heating that require observational duty-cycle constraints. [chaotic cold accretion](https://arxiv.org/abs/1301.3130); [dual jet/heating feedback](https://arxiv.org/abs/1108.0110).

**Remaining uncertainty.** The open quantity is the distribution of heating-to-cooling ratios over a mass-selected population and duty cycle, not whether individual systems can show cavities.

**Survey/data plan.** Chandra cavity measurements and XMM/eROSITA thermodynamics for cooling luminosity; VLA/LOFAR radio data for jet age and duty-cycle indicators; group/cluster catalogues selected by halo mass rather than cavity visibility.

**Analysis/test and decision criterion.** Compute cavity enthalpy and buoyancy/age-based jet power, compare to X-ray cooling luminosity, and model censoring for systems without detectable cavities. Maintenance heating is supported only if the time-averaged heating-to-cooling distribution is centered near unity for the relevant halo-mass range.

**Limitations and wording guardrails.** Cavity detectability and age estimates bias toward energetic systems; nondetections must enter the model rather than be dropped.

## Methodological note

- Evidence-gap ranking and acceptance-threshold work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.

## Scope note

These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.

<!-- AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z · professional Gemini-assisted RT revision · docs-static no-apply -->

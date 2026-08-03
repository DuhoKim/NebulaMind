# Galaxy Evolution — Research proposals on feedback tracers and model validation

> This page presents three proposal-style research programmes on multiphase outflows, molecular-gas depletion versus efficiency, and forward-modelled simulation validation. Duplicate themes are consolidated so each proposal targets a distinct physical uncertainty.


3 proposal-style research programmes.

## P1 — A multiphase, common-denominator census of AGN-driven outflows

**Hypothesis / objective.** The inferred frequency and impact of AGN outflows depend strongly on gas phase, and a common-denominator multiphase census will change which feedback conclusions are supportable.

**Prior evidence and constraints.**
- High-redshift quasar molecular-gas work provides one tracer of AGN impact on cold reservoirs, but it cannot represent all gas phases. [molecular gas reservoirs in quasars](https://arxiv.org/abs/1706.08987).
- Young radio-galaxy outflow studies provide a complementary radio/ionized-gas efficiency perspective. [young radio-galaxy outflows](https://arxiv.org/abs/2009.11175).
- The local evidence summary includes AGN/outflow debate anchors that should be treated as provenance, not as a complete population denominator. [Method 3 AGN evidence anchor](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn).

**Remaining uncertainty.** Different tracers select different temperature/density phases and apertures, so current outflow rates may not be comparable or population-representative.

**Survey/data plan.** Parent AGN sample selected before outflow detection; MUSE/MaNGA ionized gas, ALMA CO molecular gas, HI/Na D or UV absorption for neutral gas, and JWST/NIRSpec at higher redshift; matched inactive controls.

**Analysis/test and decision criterion.** Recompute outflow occurrence, mass-loading, and kinetic power under a common selection denominator and aperture model. The claim that AGN outflows are common or important is supportable only for phases and mass/redshift ranges where tracer-corrected occurrence remains high.

**Limitations and wording guardrails.** Mass conversion factors differ by phase; avoid combining phase-specific mass outflow rates without explicit conversion uncertainties.

## P2 — Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies

**Hypothesis / objective.** In quenched or transitioning galaxies, low star formation is driven primarily by reduced molecular-gas fraction in some regimes and by reduced star-formation efficiency in others.

**Prior evidence and constraints.**
- The local evidence summary separates reservoir-response questions from AGN mechanism claims, motivating a direct gas-fraction versus efficiency test. [Method 3 gas reservoir evidence anchor](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#gas).
- Molecular-gas reservoir observations in quasars show that AGN can coincide with disturbed cold gas, but they do not alone distinguish depletion from suppressed efficiency. [quasar molecular-gas reservoir evidence](https://arxiv.org/abs/1706.08987).
- Environment/AGN comparisons against SDSS motivate separating gas supply, environment, and internal feedback rather than treating quenching as one scalar outcome. [environment and AGN quenching versus SDSS](https://arxiv.org/abs/2401.12953).

**Remaining uncertainty.** A quenched galaxy can have little gas or inefficient star formation in the gas it retains; those mechanisms imply different feedback and replenishment physics.

**Survey/data plan.** ALMA CO for molecular gas mass, dust continuum as a cross-check, Hα/UV/IR SFR indicators, optical morphology and stellar population ages, environment labels, and matched star-forming/transition/quiescent controls.

**Analysis/test and decision criterion.** Decompose sSFR offsets into gas-fraction and depletion-time terms at fixed mass, redshift, and environment. Reservoir depletion is supported when gas fraction drives the offset; efficiency suppression is supported when depletion time changes dominate with gas retained.

**Limitations and wording guardrails.** CO-to-H2 conversion, aperture mismatch, and SFR timescale indicators must be propagated into the decision criterion.

## P3 — Forward-modelled validation of cosmological feedback prescriptions

**Hypothesis / objective.** If subgrid feedback prescriptions are correct, forward-modelled mock observations from simulations should reproduce observed gas fractions, quenched fractions, outflow tracers, and morphology distributions under the same selection functions.

**Prior evidence and constraints.**
- IllustrisTNG quenched-fraction analyses explicitly tie quenching outcomes to AGN feedback, environment, and preprocessing in simulations. [IllustrisTNG quenched fractions](https://arxiv.org/abs/2008.00005).
- Horizon-AGN links AGN feedback to morphological diversity, making morphology a testable output rather than background context. [Horizon-AGN morphology and AGN feedback](https://arxiv.org/abs/1606.03086).
- Hydrodynamic quenching simulations motivate observationally matched validation, not direct import of simulation conclusions. [AGN-driven quenching simulation implications](https://arxiv.org/abs/1301.3092).

**Remaining uncertainty.** Simulations are often compared to derived quantities rather than to observables passed through the same survey selection, aperture, and sensitivity functions.

**Survey/data plan.** IllustrisTNG/Horizon-AGN/EAGLE-like public simulation outputs; synthetic MaNGA/MUSE/ALMA/X-ray/radio observables; real comparison samples from SDSS/MaNGA, ALMA follow-up, and group catalogues.

**Analysis/test and decision criterion.** Generate survey-matched mocks and compare joint distributions of gas fraction, quenched fraction, morphology, outflow incidence, and halo environment. A feedback model is constrained when residuals exceed observational uncertainties in a physically coherent subset of observables.

**Limitations and wording guardrails.** Different subgrid models can produce degenerate macroscopic observables; results should report which observables discriminate rather than ranking simulations globally.

## Methodological note

- Corpus-rebalancing work remains useful as methodology support, but it is not presented here as an astrophysical proposal because it does not test a physical galaxy-evolution hypothesis.

## Scope note

These are proposed research designs, not accepted claims. Source links in the proposal text identify prior evidence or constraints that motivate the study; they do not by themselves prove the proposed hypothesis. Each proposal is written to be testable through future survey analysis, matched controls, and explicit decision criteria.

<!-- AUTOPILOT_RESEARCH_TOPICS_PROFESSIONAL_GEMINI_ASSIST_PASS_20260708T120000Z · professional Gemini-assisted RT revision · docs-static no-apply -->

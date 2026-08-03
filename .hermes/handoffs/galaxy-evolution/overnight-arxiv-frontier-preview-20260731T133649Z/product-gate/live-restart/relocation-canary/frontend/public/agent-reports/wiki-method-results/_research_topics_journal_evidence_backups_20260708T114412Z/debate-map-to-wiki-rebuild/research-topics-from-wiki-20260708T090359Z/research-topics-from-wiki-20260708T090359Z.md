# Galaxy Evolution — Research proposal agenda (Method 3)

Order marker: `AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z`
Evidence-aware study proposals derived from a local research-status synthesis (Method 3 debate-map view).

> **Please read.** Proposed studies — hypotheses/questions for future work, **not accepted results or citation-bound evidence**. "What studies already show" summarizes the current synthesis in plain words (model-only/single-sample support flagged). Survey names = data a study would use, not evidence already proving a claim.

Each card: Research question · What studies already show · What remains unknown · Survey/data plan (data → measurement) · Analysis/test · Expected result/decision point · Caveats · Provenance.

## 1. When does AGN feedback dominate galaxy quenching?
- **Research question:** In which regime of halo mass, environment, and redshift is AGN feedback the leading quenching channel vs halo/environmental/stellar channels?
- **What studies already show:** central BH/bulge/velocity-dispersion properties correlate with central-galaxy quenching; AGN feedback is one channel among several (the synthesis declines to name "the dominant cause"); countercases (strangulation, satellite processing, gas retention, stellar feedback) stay active.
- **What remains unknown:** which channel is *causally* responsible at fixed halo mass/environment/stellar mass — correlations don't break the AGN-power vs host-structure degeneracy.
- **Survey/data plan:** DESI, SDSS/GAMA → matched parent samples/denominators · SDSS/MaNGA or MUSE → resolved SFH & central structure · Chandra/XMM/eROSITA + VLA/LOFAR → AGN power/state · IllustrisTNG/HORIZON-AGN → with/without-AGN counterfactuals (priors to test).
- **Analysis/test:** at fixed halo mass/environment/stellar mass, regress quenched fraction on AGN power; compare residual quenching to the with/without-AGN counterfactuals to isolate the AGN-attributable share.
- **Expected result / decision point:** a conditional threshold where AGN-attributable quenching exceeds alternatives, or a demonstration of continued degeneracy.
- **Caveats:** AGN–host selection coupling; time-variable AGN power; differing simulation prescriptions.
- *Provenance:* `dominance_debate`, `mechanism_ejective_feedback`, `alternatives_countercases`; `clc_agn2299_003`, `clc_agn_009`, `clc_agn_010`.

## 2. A comparable-denominator census of AGN-driven outflows
- **Research question:** What is outflow incidence by tracer and selection once a single denominator is applied?
- **What studies already show:** the synthesis records a ~17% ionized-outflow rate in one cosmic-noon AGN sample and a ~46% neutral-outflow rate in a massive-galaxy sample, and warns these tracer/selection-specific fractions must not be merged; molecular/ionized/neutral phases seen in selected hosts under heterogeneous selections.
- **What remains unknown:** population-wide frequency under a common selection/denominator, and its variation by gas phase and redshift.
- **Survey/data plan:** MOSDEF, JWST/NIRSpec → ionized outflows · Na I D absorption → neutral phase (same parent) · ALMA CO/[C II] → molecular phase & mass loading · COSMOS/CANDELS, DESI → single mass/redshift-selected denominator.
- **Analysis/test:** one selection + redshift grid; per-tracer detection fractions at identical thresholds; tracer-resolved prevalence with explicit denominators (never merged).
- **Expected result / decision point:** a tracer-resolved prevalence curve with controlled selection.
- **Caveats:** tracer/distance sensitivity; phase mismatch; single cases are not prevalence anchors.
- *Provenance:* `outflow_prevalence_frequency`; `clc_agn_002a` (MOSDEF ~17% ionized), `clc_agn_002b` (JWST ~46% neutral).

## 3. Gas reservoirs and star-formation efficiency in quenching galaxies
- **Research question:** Are quenching galaxies gas-poor (removed) or gas-retaining-but-inefficient, and where do AGN hosts fall?
- **What studies already show:** some quenched systems show central-kpc molecular depletion; others retain gas but form stars inefficiently (low SFE ≠ low gas); central-gas expulsion ≠ galaxy-wide reservoir loss.
- **What remains unknown:** relative frequency of "removed" vs "retained-inefficient" quenching, and whether AGN tracks central depletion specifically vs global loss.
- **Survey/data plan:** ALMA CO/[C II] → resolved gas mass & depletion time (central vs galaxy-wide) · SDSS/MaNGA or MUSE → resolved SFE & stellar pops · X-ray/radio AGN-stage → duty-cycle ordering.
- **Analysis/test:** resolved depletion time vs AGN stage and radius; classify depleted/retained-inefficient/intermediate; test whether AGN hosts concentrate in central-depletion class.
- **Expected result / decision point:** a population split + yes/no on AGN predicting central vs global depletion.
- **Caveats:** diffuse/atomic gas missed; tracer-dependent depletion times; keep central vs galaxy-wide distinct.
- *Provenance:* `reservoir_response`; `clc_agn_005` (retention/low-SFE), `clc_agn_006` (central-kpc depletion).

## 4. An observational program for maintenance (preventive) heating
- **Research question:** Does radio-mode/maintenance heating balance cooling across the population as an observed duty cycle, not a model expectation?
- **What studies already show:** maintenance/preventive heating is rendered **model-dependent** (simulation-supported, not observationally established here); kept distinct from ejective feedback; not rendered "contradicted."
- **What remains unknown:** whether observed heating power (X-ray cavities, radio duty cycles) balances cooling luminosity across a controlled halo-mass range.
- **Survey/data plan:** Chandra/XMM/eROSITA → cavities, cooling luminosity, hot-halo thermodynamics · VLA/LOFAR/MeerKAT → radio jet power & duty cycle · halo-mass-spanning group/cluster samples.
- **Analysis/test:** in a halo-mass-controlled sample, compare cavity+radio heating power to X-ray cooling luminosity, time-averaged over the duty cycle.
- **Expected result / decision point:** a measured heating/cooling balance (promotes to observationally bounded) or an upper bound.
- **Caveats:** duty-cycle averaging uncertainty; cavity-energetics systematics; low-mass halos hardest; model ≠ observation.
- *Provenance:* `maintenance_heating_prevention` (model-dependent); `clc_agn_004`.

## 5. Validating simulation predictions against unbiased observations
- **Research question:** Which simulation-predicted rates/signatures/outcomes survive forward-modeled comparison to unbiased samples?
- **What studies already show:** simulation-only statements are labeled "in simulations / in this model" and treated as model-dependent; simulations show what mechanisms can produce, not observed prevalence.
- **What remains unknown:** which specific predictions match observations once survey selection is applied.
- **Survey/data plan:** IllustrisTNG/HORIZON-AGN → mock observables (a model to test) · DESI, SDSS, JWST deep fields → unbiased comparison samples with defined selection.
- **Analysis/test:** forward-model simulation into each survey's selection; compare predicted vs observed outflow/heating/quenching statistics; flag predictions only visible without selection.
- **Expected result / decision point:** a validated/invalidated list of predictions.
- **Caveats:** forward-model fidelity; sub-grid feedback differences; selection-dependent matches.
- *Provenance:* `simulation_model_scope`; `clc_agn_011`.

## 6. Filling the lightly-covered channels: chemical, structural, and high-redshift
- **Research question:** Which under-mapped channels carry enough evidence to weigh against AGN feedback, and which need new measurements?
- **What studies already show:** the synthesis reports the mass–metallicity relation with modest scatter at cosmic noon and a fundamental-metallicity relation ~stable (to ~0.1 dex) to z~2.3; the reionization frontier is open debates (ionizing-photon budget; JWST z>10 "too-massive/too-early" tension); halo-regulation and morphology/structural-growth are scoped/lightly-covered on largely unverified rows.
- **What remains unknown:** whether these channels' evidence can rank against AGN feedback, and their redshift-resolved behavior beyond scoped ranges.
- **Survey/data plan:** JWST/NIRSpec (JADES/AURORA-style), SDSS/MaNGA → mass–metallicity & ages across z · HST–JWST deep imaging, COSMOS/CANDELS → size–mass & morphology evolution · DESI + wide imaging (lensing/clustering) → halo regulation · JWST spectroscopy → reionization-era constraints.
- **Analysis/test:** redshift-resolved scaling relations + halo-regulation measures on consistent selection; compare evidential weight to the AGN channel.
- **Expected result / decision point:** a ranked evidence gap — which channel most needs new data.
- **Caveats:** each relation's redshift scope; unverified rows are not settled claims.
- *Provenance:* scoped coverage sections (Dark Matter Halos & Structure Formation; Environment, Morphology & Structural Growth; Chemical Enrichment & Cosmic Timing; High-Redshift & Reionization Frontier).

## Methods appendix — linking source judgments to citable records
A supporting, non-observational task: reconcile a few provisional source attributions with citable records (NASA ADS / local bibliography) and complete a pending review of the underlying map before any study binds references — evidence-curation housekeeping (matching provisional links to full records; counting independent studies), not a science proposal.

## Scope & limitations
Six proposals = a reading of one research-status synthesis, not exhaustive. "What studies already show" reflects that synthesis in plain words (model-only/single-sample support flagged). Confidence wording is method-specific and not comparable across the other agendas.

<!-- AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z — Method3 specific proposal agenda · docs-only · 0 product claim/cite · derived from local M3 wiki · no invented findings/IDs -->

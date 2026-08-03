# Galaxy Evolution: A Research Prospectus from a Debate-Map Synthesis (Method 3)

Order marker: `AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z`

> **Status.** Static, docs-only prospectus. Proposals are hypotheses for future work, not accepted results; no product citations are bound. Each prior-evidence statement links to the local [Method 3 evidence basis](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html); survey names denote proposed data acquisition, not datasets that already establish a result.

Per card: Research question · Prior evidence and constraints (with visible evidence-basis links) · Remaining uncertainty · Data and measurement plan · Analysis and decision criterion · Limitations · Provenance.

## 1. Isolating the causal contribution of AGN feedback to central-galaxy quenching
- **Research question.** At fixed halo mass, environment, and stellar mass, what fraction of central-galaxy quenching is attributable to AGN feedback rather than halo/environmental/stellar channels?
- **Prior evidence and constraints.**
  - Central black-hole/bulge/velocity-dispersion properties correlate with central-galaxy quenching as coupled predictors, not isolated causal channels ([evidence basis §4](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn)).
  - AGN dominance is classified as actively debated, with no single dominant cause designated ([§4](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn)).
  - Alternative channels (strangulation, stripping, retention, stellar feedback) are established, required context ([§5](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#environment), [§3](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#gas)).
- **Remaining uncertainty.** The causal partition at fixed host properties is unresolved; correlations do not separate AGN power from co-varying host structure.
- **Data and measurement plan.** DESI, SDSS/GAMA → matched denominators; SDSS/MaNGA, MUSE → resolved SFH & central structure; Chandra/XMM/eROSITA, VLA/LOFAR → AGN power/state; IllustrisTNG, HORIZON-AGN → with/without-AGN counterfactuals (priors to test).
- **Analysis and decision criterion.** Regress quenched fraction on AGN power in matched host bins; compare AGN-attributable residual to counterfactuals. Support requires an AGN-attributable excess exceeding the alternatives at defined significance; otherwise refuted for that regime.
- **Limitations.** AGN–host selection coupling; time-variable AGN power; differing simulation prescriptions. Non-binding, docs-only.
- *Provenance:* `dominance_debate`, `mechanism_ejective_feedback`, `alternatives_countercases`; `clc_agn2299_003`, `clc_agn_009`, `clc_agn_010`.

## 2. A tracer-resolved, common-denominator census of AGN-driven outflows
- **Research question.** Under a single selection and denominator, what is AGN-outflow incidence by gas-phase tracer and redshift?
- **Prior evidence and constraints.**
  - Tracer-specific fractions are recorded — approximately 17 per cent ionized in one cosmic-noon AGN sample and approximately 46 per cent neutral in a massive-galaxy sample — and must not be combined ([evidence basis §4](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn)).
  - Molecular/ionized/neutral outflows are reported in selected hosts under heterogeneous selections; prevalence is emerging and sample-limited ([§4](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn)).
- **Remaining uncertainty.** No common denominator links the fractions; population-wide incidence by phase and redshift is unconstrained.
- **Data and measurement plan.** MOSDEF, JWST/NIRSpec → ionized; Na I D absorption → neutral; ALMA CO/[C II] → molecular; COSMOS/CANDELS, DESI → one selected denominator.
- **Analysis and decision criterion.** One selection + redshift grid; per-tracer fractions at matched sensitivity; tracer-resolved prevalence with explicit denominators. Decisive when phase-resolved incidence is measured on a common sample; a merged rate is uninformative.
- **Limitations.** Tracer/distance sensitivity; phase mismatch; single cases are not prevalence anchors. Non-binding, docs-only.
- *Provenance:* `outflow_prevalence_frequency`; `clc_agn_002a`, `clc_agn_002b`.

## 3. Distinguishing reservoir removal from inefficient star formation
- **Research question.** What population fraction of quenching galaxies have lost reservoirs versus retain gas at low efficiency, and does AGN track central depletion specifically?
- **Prior evidence and constraints.**
  - Central-kpc molecular depletion is reported in some quenched systems ([evidence basis §3](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#gas)).
  - Others retain gas at low star-formation efficiency, so suppressed star formation ≠ depleted reservoir ([§3](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#gas)).
  - Central-gas expulsion does not by itself imply galaxy-wide reservoir loss ([§4](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn)).
- **Remaining uncertainty.** The frequency of removed vs retained-inefficient quenching is unmeasured; AGN association with central (vs global) depletion is untested.
- **Data and measurement plan.** ALMA CO/[C II] → resolved gas mass & depletion time; SDSS/MaNGA, MUSE → resolved efficiency & stellar pops; X-ray/radio → AGN duty-cycle ordering.
- **Analysis and decision criterion.** Depletion time vs AGN stage and radius; classify depleted/retained-inefficient/intermediate. Supported if AGN hosts concentrate in central-depletion at fixed mass; refuted if depletion is AGN-independent.
- **Limitations.** Diffuse/atomic gas may be missed; tracer-dependent depletion times; keep central vs galaxy-wide distinct. Non-binding, docs-only.
- *Provenance:* `reservoir_response`; `clc_agn_005`, `clc_agn_006`.

## 4. An observational determination of the maintenance-heating duty cycle
- **Research question.** Across a halo-mass-controlled population, does observed radio-mode heating power balance X-ray cooling luminosity, duty-cycle-averaged?
- **Prior evidence and constraints.**
  - Maintenance/preventive heating is model-dependent — simulation-supported, not established as observed galaxy-scale prevalence ([evidence basis §4](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#agn)).
  - Simulation-based statements are model-scope, not observed prevalence, and distinct from ejective feedback ([§8](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#observational)).
- **Remaining uncertainty.** The observed heating-to-cooling balance and its halo-mass dependence are not established here.
- **Data and measurement plan.** Chandra/XMM/eROSITA → cavities, cooling luminosity, hot-halo thermodynamics; VLA/LOFAR/MeerKAT → radio power & duty cycle; halo-mass-spanning group/cluster samples.
- **Analysis and decision criterion.** Duty-cycle-averaged heating power vs X-ray cooling luminosity across the controlled sample. Balance promotes maintenance heating to observationally bounded; a deficit sets an upper bound.
- **Limitations.** Duty-cycle/cavity systematics; low-mass halos hardest; model ≠ observation. Non-binding, docs-only.
- *Provenance:* `maintenance_heating_prevention`; `clc_agn_004`.

## 5. Forward-modeled validation of simulation feedback predictions
- **Research question.** Which simulation-predicted outflow/heating/quenching statistics survive comparison with unbiased surveys once selection is applied?
- **Prior evidence and constraints.**
  - Simulation-only statements are model-dependent — demonstrations of what feedback can produce under assumptions, not observed prevalence ([evidence basis §8](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#observational)).
- **Remaining uncertainty.** Which predictions are observationally supported after selection is untested; some may exist only in unselected simulation space.
- **Data and measurement plan.** IllustrisTNG, HORIZON-AGN → mock observables (model under test); DESI, SDSS, JWST deep fields → unbiased comparison samples with defined selection.
- **Analysis and decision criterion.** Forward-model into each survey's selection; compare predicted vs observed distributions. Validated if matched within tolerance; invalidated if visible only without selection.
- **Limitations.** Forward-model fidelity; sub-grid feedback differences; selection-dependent matches. Non-binding, docs-only.
- *Provenance:* `simulation_model_scope`; `clc_agn_011`.

## 6. Rebalancing the multi-channel evidence base: chemical, structural, high-redshift
- **Research question.** Which under-mapped channels carry sufficient evidence to weigh against AGN feedback, and which require new measurements?
- **Prior evidence and constraints.**
  - Mass–metallicity relation with modest scatter at cosmic noon; fundamental metallicity relation ~stable to ~0.1 dex to z~2.3 ([evidence basis §6](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#chemical)).
  - Reionization frontier framed as open debate (ionizing-photon budget; JWST z>10 high-stellar-mass tension), not settled ([§7](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#high-redshift)).
  - Halo regulation and morphological/structural growth are scoped, lightly-covered on largely unverified rows ([§2](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#halos), [§5](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#environment)).
- **Remaining uncertainty.** Whether these channels can be ranked against AGN feedback, and their redshift-resolved behavior beyond scoped ranges, is unresolved.
- **Data and measurement plan.** JWST/NIRSpec (JADES/AURORA-class), SDSS/MaNGA → metallicity & ages across z; HST–JWST deep imaging, COSMOS/CANDELS → size–mass & morphology; DESI + lensing/clustering → halo regulation; JWST → reionization-era constraints.
- **Analysis and decision criterion.** Redshift-resolved scaling relations + halo-regulation measures on consistent selection vs the AGN channel's weight → a ranked evidence gap.
- **Limitations.** Each relation's redshift scope; unverified rows not settled. Non-binding, docs-only.
- *Provenance:* scoped coverage sections (Halos & Structure Formation; Environment/Morphology; Chemical Enrichment; High-Redshift & Reionization).

## Methods note — source reconciliation
A supporting curation task precedes reference binding: reconcile a small number of provisional source attributions with citable records and complete a pending review of the underlying map. A methods step, not a scientific result; no new observation.

## Scope and status
Six proposals from one research-status synthesis, not exhaustive. Prior-evidence statements are linked to the evidence basis; survey names denote proposed data acquisition. Confidence classifications are method-specific and not comparable across agendas. Static, docs-only; no product citations bound.

<!-- AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z — Method3 journal prospectus · docs-only · 0 product claim/cite · prior-evidence linked to local evidence basis · no invented links/papers/IDs -->

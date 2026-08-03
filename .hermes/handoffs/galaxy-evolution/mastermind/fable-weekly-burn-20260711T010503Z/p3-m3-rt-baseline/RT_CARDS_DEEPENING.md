# RT cards deepening — Fable-side, local evidence only

Marker: `FABLE_BURN_P3_RT_DEEPENING_20260711T010503Z`
Companion to `M3_ACCEPTANCE_BASELINE.md` (same card numbering, same source abbreviations:
REQ / EB / SC / CUR — full paths + sha256 in `P3_RECEIPT.md`). Purpose: an independent
Fable-side deepening of the six M3 research-topic cards that a future adjudicator can
cross-check against the gated sidecar output. Everything here is derived from **local
artifacts plus logical tightening only** — no new literature, no numbers not already present
in local files. Anything that genuinely needs the network is explicitly labeled
**`GATED — needs sidecar/network pass (separate Duho approval)`** rather than speculated on.

Per card: (a) what local evidence already answers · (b) tightened decision criterion ·
(c) falsifiable predictions · (d) overclaim risks · (e) network-gated items.

---

## Card 1 — Isolating the causal contribution of AGN feedback to central-galaxy quenching

**(a) What local evidence already answers.**
- Correlation is in hand, causation is not: central BH/bulge/σ properties correlate with
  central quenching as *coupled predictors* (SC L12; EB `#s4` L48–50, claims `2917, 2924`).
- Dominance is genuinely open — `dominance_debate` = actively_debated, no settled ordering
  (EB L17), and the multi-channel account (strangulation, stripping, retention, stellar
  feedback) is widely supported context (EB L15, claim `2931`, `clc_agn_007`).
- The halo-vs-central predictor debate is OPEN (EB `#s2` L41) — so any causal partition must
  control halo mass, not only stellar/structural properties.
- Net local answer to the card's research question (SC L10): *unknown fraction; the local
  basis licenses only "AGN is one coupled channel among several."*

**(b) Tightened decision criterion** (operationalizing SC L17):
- Pre-register the host-matching vector before any AGN split: stellar mass, σ (or bulge proxy),
  morphology class, environment label, halo-mass proxy — all five appear in the local basis as
  known confounders (EB `#s2`, `#s4`, `#s5`).
- Define the null: after matching on that vector, a time-averaged AGN-power proxy adds no
  predictive power for quenched fraction. "Support" then requires an AGN-attributable excess
  Δf_q whose interval excludes zero in ≥2 independent mass bins — not a single-bin excess.
- Require the counterfactual comparison (with/without-AGN simulations, SC L16) to be reported
  as *prior sensitivity* (how conclusions move under different subgrid prescriptions), never as
  a second observation (EB L20).
- Failure clause (fail-closed): if matched bins are too thin to bound Δf_q, the card's verdict
  is "insufficient denominator," not a weak positive.

**(c) Falsifiable predictions.**
- If AGN feedback causally dominates central quenching: quenched fraction at fixed
  (M*, σ, environment) rises with time-averaged AGN power, and the excess survives
  halo-mass matching. Refutation: excess vanishes under σ- or halo-matching (then the
  predictor was structure, not AGN power).
- If the coupled-predictor reading is right (local floor): no matched-bin AGN excess will be
  found beyond what σ/bulge matching absorbs — a clean, checkable negative.

**(d) Overclaim risks.**
- σ- or BH-mass correlation re-narrated as causation (the exact "coupled predictors" trap,
  SC L12); instantaneous AGN luminosity mistaken for time-averaged power (AGN variability is
  cited as a card limitation, SC L18); survivor bias — quenched hosts observed after the AGN
  event; simulation counterfactuals quoted as evidence rather than priors.

**(e) `GATED — needs sidecar/network pass (separate Duho approval)`.**
- Which 2020+ matched-control or causal-inference quenching studies exist, and what host
  vector each controlled; survey-scale X-ray/radio AGN-power proxy catalogs; whether DESI-era
  denominators are public at the needed depth. (REQ question 1/2 territory — not answerable
  from local disk.)

---

## Card 2 — Tracer-resolved, common-denominator census of AGN-driven outflows (CUR P1)

**(a) What local evidence already answers.**
- Two tracer-specific incidence anchors exist and are deliberately non-combinable:
  ~17% ionized in a cosmic-noon AGN sample (`clc_agn_002a`), ~46% neutral Na I D in a
  massive-galaxy sample (`clc_agn_002b`) (SC L24; EB `#s4` L50).
- Prevalence status is emerging_sample_limited (EB L16); no common denominator links the
  fractions; population incidence by phase and z is unconstrained (SC L26).
- Local answer to "what is the incidence?": *known only per-tracer, per-sample; the census is
  the missing measurement, not a re-analysis.*

**(b) Tightened decision criterion** (operationalizing SC L28 / CUR L26).
- One parent selection, fixed before any outflow measurement (CUR L24), with the denominator
  quoted in every incidence number.
- Matched *physical* sensitivity: per-tracer detection thresholds equalized in mass-outflow-
  rate sensitivity (via the phase's conversion factor + uncertainty, CUR L28), not in raw flux
  — otherwise the "census" reproduces tracer selection.
- Report f_phase(z, M*) with binomial intervals; the census "changes which feedback
  conclusions are supportable" (CUR L15) exactly when some phase's common-denominator
  incidence falls outside the interval implied by the current heterogeneous-selection
  anchors (17%/46% class); otherwise the heterogeneity story weakens.
- A merged multi-phase rate is defined as uninformative in advance (SC L28) — publishing one
  is itself a fail condition for the design.

**(c) Falsifiable predictions.**
- If selection heterogeneity drives today's spread: common-denominator incidences will move by
  more than their current intervals in at least one phase, and the ionized-vs-neutral ordering
  may invert between mass bins.
- If the spread is physical: the per-phase ordering is stable across denominators, and
  aperture/conversion corrections shift levels but not ordering. Either outcome is
  informative; neither is assumed.

**(d) Overclaim risks.**
- Combining or averaging the 17%/46% class numbers (explicitly banned locally, SC L24);
  quoting detection fraction as occurrence without completeness correction; single spectacular
  objects as prevalence anchors (SC L29); summing phase-specific mass-outflow rates without
  conversion-uncertainty propagation (CUR L28).

**(e) `GATED — needs sidecar/network pass (separate Duho approval)`.**
- Whether a 2020+ common-denominator multiphase census already exists (REQ question 1);
  NIRSpec-IFU and ALMA CO sensitivity/exposure realism at the card's z grid (REQ question 2);
  candidate parent surveys with published selection functions.

---

## Card 3 — Reservoir removal vs inefficient star formation (CUR P2)

**(a) What local evidence already answers.**
- Both quenching modes are locally documented as real in *some* systems: central-kpc molecular
  depletion (`clc_agn_006`) and gas retention at low SFE (`clc_agn_005`) (SC L35–36; EB `#s3`
  L44–46, claims `2905–2911, 2930`).
- Central expulsion ≠ galaxy-wide loss (SC L37). `reservoir_response` = actively_debated
  (EB L18).
- Local answer to "what population fraction?": *unmeasured — the local basis proves existence
  of both classes, quantifies neither.* AGN association with central-vs-global depletion is
  untested (SC L38).

**(b) Tightened decision criterion** (operationalizing CUR L43).
- Exact decomposition per galaxy: Δlog sSFR = Δlog f_gas − Δlog t_dep (offsets at fixed mass,
  z, environment vs the star-forming control ridge). Classify depletion-dominated /
  efficiency-dominated / mixed only when the dominant term exceeds the other by more than the
  fully propagated systematic budget — CO-to-H2 conversion, aperture mismatch, SFR-timescale
  choice are all named locally as first-class terms (CUR L45), so they enter the classifier,
  not a footnote.
- AGN linkage test (SC L40): among the depletion-classified population, is the AGN-host
  fraction higher than among the efficiency-classified population at matched (M*, z,
  environment)? Supported / refuted exactly as the card states; "AGN-independent depletion"
  is a first-class refutation outcome, not a null to hide.
- Radial requirement: every classification carries central-kpc vs galaxy-wide labels
  separately (SC L41) — a galaxy may be centrally depleted and globally retained.

**(c) Falsifiable predictions.**
- If AGN tracks *central* depletion specifically: AGN excess appears in the centrally-depleted
  class but not in the globally-depleted class.
- If quenching is mostly efficiency suppression in the transition population: gas-retained
  low-SFE galaxies dominate the green-valley bins, and depletion classes concentrate only in
  long-quenched systems. Both are checkable against the classifier output.

**(d) Overclaim risks.**
- Reading suppressed SF as gas loss (the exact local qualifier, SC L36); treating CO
  nondetections as zero gas rather than upper limits inside the classifier; importing absolute
  simulation medians for f_gas/t_dep as if commensurable with matched-control offsets — the
  Gawade-class estimand error that helped sink cycle-7 (CY7 retained-leads note; VER blocking
  fact 4); collapsing central and global depletion into one label.

**(e) `GATED — needs sidecar/network pass (separate Duho approval)`.**
- 2020+ resolved-CO/dust surveys of quenched and transition galaxies (existence, sample
  sizes); ALMA feasibility for central-kpc CO at the card's mass/z range; published
  matched-control decomposition precedents (REQ questions 1–2).

---

## Card 4 — Observational determination of the maintenance-heating duty cycle

**(a) What local evidence already answers.**
- Status is the strongest local statement: maintenance/preventive heating is
  `contradicted_or_model_dependent` — simulation-supported, **not** observationally settled at
  galaxy-scale prevalence (EB L19; SC L47, `clc_agn_004`), and simulation statements are
  model-scope by design (EB `#s8`, `clc_agn_011`).
- Local answer to "does heating balance cooling?": *not established here, in either
  direction — the card's job is to create the first population-controlled bound.*

**(b) Tightened decision criterion** (operationalizing SC L51).
- Population, not trophies: a halo-mass-controlled sample with pre-declared bins; per-bin
  duty-cycle-averaged heating power ⟨P_heat⟩ (cavity/radio proxy × duty cycle) compared to
  X-ray cooling luminosity L_cool.
- Verdict bands fixed in advance: "balance" only if ⟨P_heat⟩/L_cool is consistent with unity
  within the systematic budget across the bin; a deficit is reported as a quantitative upper
  bound on maintenance heating for that halo-mass range (SC L51's "deficit sets an upper
  bound" made binding); an excess is reported as over-heating tension, not confirmation.
- Promotion rule mirrors the debate map: only a population-level balance can move the axis
  from model-dependent to observationally bounded (SC L51); single-system balances cannot.

**(c) Falsifiable predictions.**
- If maintenance heating regulates cooling above a halo-mass threshold: duty-cycle indicators
  rise with L_cool above that threshold, and quiescent centrals below it show no such scaling
  — a two-sided, checkable pattern.
- If the axis's skeptical status is right: the population balance will fail outside cluster
  cores, and the card's output is an upper bound — which is still a publishable, floor-
  consistent result.

**(d) Overclaim risks.**
- Cluster-core cavity systems generalized to galaxy-scale prevalence (the precise scope
  inflation the local status warns about, EB L19); duty-cycle and cavity-enthalpy systematics
  absorbed silently (SC L52); simulation heating rates quoted as observations; treating the
  CUR consolidation (card dropped as standalone) as scientific resolution — it was an
  editorial consolidation (CUR L3), nothing more.

**(e) `GATED — needs sidecar/network pass (separate Duho approval)`.**
- eROSITA-era group/poor-cluster cooling-luminosity samples; LOFAR/MeerKAT duty-cycle
  population statistics 2020+; low-halo-mass cavity detectability limits (REQ question 2 —
  note JWST/ALMA are marginal for this card; the honest realism answer is X-ray/radio).

---

## Card 5 — Forward-modeled validation of simulation feedback predictions (CUR P3)

**(a) What local evidence already answers.**
- The scope boundary itself: simulation-only statements demonstrate what feedback *can*
  produce under assumptions (EB L20, `clc_agn_011`); which predictions survive survey
  selection is untested (SC L59; CUR L56). The three cited priors (TNG quenched fractions,
  Horizon-AGN morphology, quenching-simulation implications — CUR L52–54) are motivation, not
  validation results.
- Local answer to "which predictions survive?": *none adjudicated yet — the local basis
  defines the test, deliberately withholding the verdict.*

**(b) Tightened decision criterion** (operationalizing CUR L60–62).
- Pre-registered observable list and tolerances before any mock is drawn: gas fraction,
  quenched fraction, morphology distribution, outflow incidence, halo environment (CUR L60).
- Selection first: every simulated galaxy passes the target survey's selection function
  (aperture, sensitivity, completeness) before any statistic is formed — matching *observables
  through selection*, never derived quantities (SC L58–59 is the local warrant).
- Verdict vocabulary is per-observable: "constrained" when residuals exceed observational
  uncertainties in a physically coherent subset (CUR L60); mandatory degeneracy report —
  which subgrid variants remain indistinguishable on the passed subset (CUR L62). Global
  simulation rankings are structurally banned by the card's own guardrail.
- Joint-distribution requirement: matched marginals with mismatched joints count as failure —
  the card's phrase "joint distributions" (CUR L60) made binding.

**(c) Falsifiable predictions.**
- If current subgrid feedback is approximately right: selection-matched mocks reproduce the
  joint (gas fraction × quenched fraction × morphology) distribution within stated tolerances,
  not only the medians.
- If predictions live in unselected simulation space (the card's stated risk, SC L59):
  applying the selection function will remove the apparent agreement — a directly observable
  collapse.

**(d) Overclaim risks.**
- "Simulation X validated / ruled out" globally (banned, CUR L62); comparing catalog-derived
  quantities instead of forward-modeled observables; absolute simulation medians vs matched-
  control statistics without non-commensurability labels (Gawade-class, VER blocking fact 4);
  tuning-set contamination — validating on observables the subgrid model was calibrated to,
  without disclosure.

**(e) `GATED — needs sidecar/network pass (separate Duho approval)`.**
- Which 2020+ mock-observable pipelines and forward-modeled comparisons exist; which public
  simulation data releases expose the fields the mocks need; concrete survey selection-
  function documentation for the comparison samples (REQ questions 1–2).

---

## Card 6 — Rebalancing the multi-channel evidence base: chemical, structural, high-redshift

**(a) What local evidence already answers.**
- Chemical channel: MZR modest scatter at cosmic noon; FMR ~stable to ~0.1 dex out to z≈2.3 —
  and *scoped there* (SC L68; EB `#s6` L58–60, AURORA/JADES-class local sources).
- High-z channel: reionization framed as open debate (ionizing-photon budget; z>10
  high-stellar-mass tension) (SC L69; EB `#s7` L62–65); the SMBH-seeding clause is locally
  unsupported (claim `2374` garbled, EB L65) while the cold-gas-reservoir part stands
  (claim `2235`).
- Structural/halo channel: scoped coverage-extensions on lightly verified rows (EB `#s2`,
  `#s5`), with two known provenance repairs pending (`2133`→`2605.22497`; unmatched
  `2915/2921/2913`).
- A quantitative imbalance is already measurable locally from the atlas trust-level counts in
  EB: *Physical Mechanisms* accepted 4 / challenged 3 / reported 7 / unverified 16 (EB L42);
  *Environment/Morphology* consensus 1 / debated 4 (EB L54); *Open Questions & Frontier*
  accepted 3 / challenged 2 / debated 1 / reported 4 / **unverified 59** (EB L63). The
  frontier section is unverified-heavy by an order of magnitude — that *is* the rebalancing
  target, stated with local numbers.
- Local answer to "which channels can be weighed against AGN?": *none yet at parity — the
  verified-row mass sits in the AGN axes; the deficit is now quantified above.*

**(b) Tightened decision criterion** (operationalizing SC L73).
- Define one common evidence-weight metric per channel from the existing trust-level counts
  (e.g., verified fraction = (accepted + challenged + debated) / total rows, computed from the
  same atlas snapshot for every channel — the ingredients all exist locally, EB L42/L54/L63).
- A channel is "sufficiently evidenced to weigh against AGN feedback" (SC L66) when its
  verified fraction reaches a pre-set ratio of the AGN axes' verified fraction on the same
  snapshot; below that, the card's output is a ranked measurement gap list, not a ranking of
  physics.
- Scope control: every chemical/structural statement carries its redshift scope explicitly;
  z>2.3 FMR statements are out of local scope by construction (SC L68) and can only enter as
  gated leads.

**(c) Falsifiable predictions.**
- Verification passes over the frontier section will move rows predominantly from
  `unverified` into `reported` (not `accepted`) — i.e., the imbalance is mostly a
  verification-labor deficit, not hidden consensus. Refutation: a large accepted-fraction
  jump, which would instead argue the frontier is better settled than the debate map says.
- If the halo-vs-central predictor debate (EB L41) is resolvable with current data, adding
  halo-regulation measurements will shift the *Physical Mechanisms* verified fraction without
  changing the AGN axes — channel-specific, checkable movement.

**(d) Overclaim risks.**
- Extending FMR/MZR stability beyond z≈2.3 in local voice (scope breach, SC L68); using our
  page to support SMBH seeding (claim `2374` — locally unsupported); ranking channels against
  AGN without a common metric (the card's core warning, SC L71); treating the CUR downgrade to
  "Methodological note" (CUR L64–66) as a scientific verdict on the channels rather than an
  editorial-consolidation choice.

**(e) `GATED — needs sidecar/network pass (separate Duho approval)`.**
- 2020+ reviews per channel (metallicity compilations, size–mass evolution, halo regulation,
  reionization budget) and whether any proposes a cross-channel evidence-weight methodology
  (REQ question 1); JWST spectroscopy realism for extending FMR beyond z≈2.3 (REQ question 2).

---

## Cross-card note for the adjudicator

The six deepenings above are deliberately **estimand-first**: each tightened criterion fixes
the statistic, the denominator, the systematic budget, and the failure clause before any data
or literature arrives. That is the shared cycle-7 lesson (CY7; VER): the rejected report died
on estimand conflation, settled-verb register, marker placement, and unlabeled uncited leads —
all four are structural, all four are pre-empted here per card. A sidecar answer that engages
these criteria can be scored in minutes against `M3_ACCEPTANCE_BASELINE.md`; one that ignores
them fails G8/floor checks without any re-derivation.

`FABLE_BURN_P3_RT_DEEPENING_20260711T010503Z`

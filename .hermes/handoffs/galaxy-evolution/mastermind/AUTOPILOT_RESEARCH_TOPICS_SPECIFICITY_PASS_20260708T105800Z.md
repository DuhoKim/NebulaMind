# Autopilot order — make research-topic proposal pages more specific

Marker: `AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z`
User correction: the current research-topic proposal pages read too general. Revise them so each proposal says, in plain academic language, **what prior studies/source rows already find**, **what remains unknown**, and **exactly how the topic would be researched with named data**.
Estimated run: 45–75 minutes.

## Goal

Revise all three existing `research-topics-from-wiki-20260708T090359Z` pages from general proposal agendas into more specific, evidence-aware research agendas.

Each method keeps its own point of view, but every proposal card must be concrete enough that an astronomy reader can answer:

1. What have prior studies / the method's current source basis already found?
2. What is still unknown, ambiguous, or under-tested?
3. What exact measurement would this proposed study make?
4. Which surveys/instruments/archives/simulations would supply each measurement?
5. What comparison or test would decide the result?

## Scope and gates

Allowed:
- Read the existing local method wiki-result, evidence/trust, evidence-basis, research-topic, JSON, and manifest artifacts.
- Overwrite the three existing working-repo research-topic output sets in:
  `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/<method>/research-topics-from-wiki-20260708T090359Z/`
- Write method-local receipts under `.hermes/handoffs/galaxy-evolution/<method>/autopilot/`.
- Write director progress/final rollup under `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/`.

Not allowed:
- No live-root writes/copies in `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/` by autopilot lanes.
- No frontend/backend restart, deploy, service mutation, git, DB/SQL/API/page_versions/live wiki publish, trust recompute, cockpit/global/shared-parent mutation, cloud/GCP/API/billing/OAuth/token/secret reads/writes, browser automation, cron, or Method3 product claim/citation binding.
- No invented paper titles, DOI/ADS records, numeric findings, source IDs, or study results. If the source wiki has only a generic finding, phrase it as "the current method source basis reports..." and keep unresolved specifics explicit.

Tori may later mirror verified static files to the live public root if the current chat instruction requires a narrow static public refresh; method autopilots must not mirror live files themselves.

## Required card structure

Each proposal card must include the following visible sections, using these headings or very close equivalents:

1. **Research question** — one specific question, not a broad theme.
2. **What studies already show** — 2–4 concrete findings from the method source basis in normal words. Examples of acceptable specificity: "observations show quasar outflows in some systems," "the source set cautions that low-mass winds may recycle rather than escape," "simulation support exists but direct observations are sparse," "M51 evidence is single-galaxy and may not generalize." Keep claim/source IDs out of this paragraph; put them in provenance.
3. **What remains unknown** — a direct gap statement: which variable, scale, denominator, causal link, population, redshift range, gas phase, or selection effect is not yet known.
4. **Survey/data plan** — name the data and say what each contributes. Do not list surveys generically. Tie every data family to a measurement, e.g.:
   - SDSS/MaNGA or MUSE: resolved star-formation histories, line ratios, gas kinematics, spatially resolved quenching.
   - ALMA CO/[C II]: molecular gas mass, depletion time, inflow/outflow/recycling reservoir.
   - Chandra/XMM/eROSITA: cavities, hot-halo thermodynamics, cooling luminosity, X-ray AGN power.
   - VLA/LOFAR/MeerKAT: radio jet power, morphology, duty cycle.
   - DESI/GAMA/COSMOS/CANDELS/Euclid/Rubin: mass/environment/redshift matched parent samples and denominators.
   - JWST/NIRSpec/MOSDEF: high-redshift ionized-gas outflows and emission-line diagnostics.
   - IllustrisTNG/HORIZON-AGN-style simulations: forward-modeled counterfactuals or priors, clearly labeled as simulations to test against observations.
   - NASA ADS/local bibliography: metadata repair only, not observational evidence.
5. **Analysis/test** — define the actual comparison: matched controls, escape velocity vs outflow velocity, heating power vs cooling luminosity, tracer-resolved prevalence denominator, gas depletion time vs AGN stage, simulation forward-model vs survey selection, etc.
6. **Expected result or decision point** — what outcome would clarify the topic: a calibrated fraction, a threshold, an upper bound, a population frequency, a rule for promotion/demotion, or a ranked evidence gap.
7. **Caveats** — selection bias, phase mismatch, time variability, single-galaxy scope, simulation/observation mismatch, abstract-only/citation-linking limits.
8. **Provenance** — short small note with the method claim/source IDs or local labels; IDs belong here only.

## Editorial requirements

- Keep 5–8 proposal cards per method. Six is fine if the cards become more specific.
- Do not turn cards into generic literature-review paragraphs. Each card needs a concrete proposed measurement and named data.
- Use "what studies already show" only for findings supported by the method page/source basis. If support is weak or simulation-only, say so explicitly.
- Use "what remains unknown" to separate known observations from the open research question.
- Keep survey names labeled as proposed data to use, not already-accepted evidence unless the method source says so.
- Avoid internal jargon in headings: claim IDs, cite-unmatched, P3, bound/unbound-local, packet, lane, audit.
- Product `<!--claim:` / `<!--cite:` comments in generated HTML must remain 0 / 0.
- No scripts, fetch/XHR/WebSocket, inline handlers, forms, remote assets, or external links/hosts.

## Method1 — packet-gated reconciliation

Source context:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- existing topic set: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`

Make its proposals more specific around:
- AGN feedback causal tests: what existing evidence can/cannot show; how MaNGA/MUSE + ALMA + X-ray/radio data would test response, gas, and energy.
- Internal vs environmental quenching: what prior population studies suggest; what remains degenerate; how SDSS/GAMA/DESI/COSMOS/CANDELS/Euclid/Rubin would build matched denominators.
- Maintenance heating: simulation support versus observed cavities/hot halos; how Chandra/XMM/eROSITA + VLA/LOFAR would measure heating/cooling balance.
- Under-supported non-AGN sections: which sections lack direct evidence; what survey families would prioritize them.
- Evidence accounting/acceptance criteria as methods appendices only, with ADS/local metadata and independent-study counting described concretely.

Receipt path:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/autopilot/RESEARCH_TOPICS_SPECIFICITY_PASS_M1_20260708T105800Z.md`

## Method2 — source-first adjudication

Source context:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- existing topic set: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/`

Make its proposals more specific around:
- Gas removal versus recycling: what outflow observations show; what remains unknown about escape/recycling; how ALMA/JWST/MUSE/DESI absorption would measure bound versus escaping phases.
- Maintenance heating: what simulations and X-ray cavity observations currently show; how a mass-selected X-ray/radio sample would test heating balance.
- Kinetic/radio-mode coupling: what review/radio observations suggest; how VLA/LOFAR/MeerKAT + Chandra + IFU data would measure coupling efficiency.
- M51/local positive feedback: what is single-galaxy; how PHANGS-style ALMA+MUSE/MaNGA samples would test generality.
- Stellar-vs-AGN feedback transition: what low-mass stellar feedback and high-mass insufficiency evidence suggest; how mass/redshift matched samples would locate a transition.
- Methods appendix: citation-linking/full-text verification/reconsideration criteria with ADS/local corpus, not new observation.

Receipt path:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/autopilot/RESEARCH_TOPICS_SPECIFICITY_PASS_M2_20260708T105800Z.md`

## Method3 — debate-map rebuild

Source context:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`
- existing topic set: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/`

Make its proposals more specific around:
- Dominance of AGN feedback: what correlations and countercases are known; how matched samples and simulations separate AGN from halo/environment/stellar channels.
- Comparable-denominator outflow prevalence: what different tracer fractions show; what is incomparable; how MOSDEF/JWST/Na I D/ALMA parent samples set tracer-resolved denominators.
- Gas reservoir response: what depletion vs retained-low-efficiency evidence suggests; how ALMA + MaNGA + AGN stage indicators classify reservoirs.
- Maintenance heating: what is model-inferred versus observed; how X-ray/radio duty-cycle measurements produce an observed bound.
- Simulation validation: what simulations predict; how forward modeling into DESI/SDSS/JWST selections tests which predictions survive.
- Multi-channel completeness: what chemical/structural/high-z channels are lightly covered; which JWST/SDSS/MaNGA/DESI/lensing/deep-imaging measurements would fill them.

Receipt path:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/autopilot/RESEARCH_TOPICS_SPECIFICITY_PASS_M3_20260708T105800Z.md`

## Required validation

Each method receipt must report:
- PASS/WARN/FAIL.
- Exact files written.
- Proposal count.
- Count of proposal cards with `What studies already show`, `What remains unknown`, `Survey/data plan`, and `Analysis/test` sections.
- Specificity proof: at least 2 examples where a generic earlier sentence was replaced with a concrete prior-finding + unknown + data-measurement statement.
- Static safety: scripts/fetch/XHR/WebSocket/event handlers/forms/external links/assets expected 0.
- Product claim/cite comment counts expected 0 / 0.
- Hard-excluded surfaces touched expected 0.

Director final rollup path:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot/AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z_FINAL_NO_APPLY_PACKET.md`

Director final rollup must include:
- Status COMPLETE or HARD_BLOCKED.
- Per-method proposal counts and section counts.
- A plain summary of how the pages became more specific.
- Static validation results.
- Whether any live-root/public mirror happened (expected 0 inside autopilots).
- Exact next action for Tori if public Method1/M2/M3 static mirrors should be refreshed after verification.

Marker: `AUTOPILOT_RESEARCH_TOPICS_SPECIFICITY_PASS_20260708T105800Z`

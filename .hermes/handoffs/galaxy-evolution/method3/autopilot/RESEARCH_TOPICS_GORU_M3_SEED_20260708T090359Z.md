# Goru M3 Topic Seed Extraction

Parent marker: `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z`
Status: **PASS**

## Inspection Scope
**Exact source wiki files inspected:**
1. `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
2. `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`

**Product binding safety:**
- Product claim comment tags found in inspected HTML: `0`
- Product cite comment tags found in inspected HTML: `0`
- Active HTML safety result: `N/A - writing a Markdown report`
- Hard-excluded surface touched: `0`

---

## Extracted Research Topics
**Topic Count:** 8

### Topic 1: AGN Ejective Feedback Mechanism in Selected Systems
* **Question:** Under what conditions does AGN activity successfully drive ejective feedback and deplete star-forming gas?
* **Wiki basis:** `mechanism_ejective_feedback` axis, widely supported in selected massive or AGN-host systems.
* **Trust/evidence caveat:** Supported for selected systems but explicitly blocked from generalizing to universal galaxy quenching.
* **Next docs-only action:** Review the local evidence basis to extract and synthesize the specific system selection criteria (mass, epoch) for the successful feedback cases.

### Topic 2: Outflow Prevalence and Tracer-Specific Frequency
* **Question:** How does the observed frequency of AGN-driven outflows vary across different redshifts, tracers, and sample selections?
* **Wiki basis:** `outflow_prevalence_frequency` axis; references 17% ionized outflows (MOSDEF) and 46% Na I D excess (JWST).
* **Trust/evidence caveat:** Emerging and sample-limited; fractions are specific to the tracer/selection and cannot be merged into a single universal prevalence percentage.
* **Next docs-only action:** Map the specific sample characteristics (e.g., z=1.4-3.8 MOSDEF vs z~2 JWST) to their respective tracer limitations from the local ledger.

### Topic 3: The Dominance Debate in Quenching
* **Question:** To what extent does AGN feedback dominate over other quenching mechanisms such as halo mass, environment, or stellar feedback?
* **Wiki basis:** `dominance_debate` and `alternatives_countercases` axes; the synthesis section confirms multiple interacting causes without a single causal ranking.
* **Trust/evidence caveat:** Actively debated; the wiki intentionally blocks rendering a "winner" among the competing mechanisms.
* **Next docs-only action:** Map the listed competing pathways (central predictors, satellite, stripping, strangulation) to their respective local evidence claim IDs.

### Topic 4: Gas Reservoir Response to Feedback
* **Question:** Does feedback globally remove cold gas reservoirs, or merely reduce star-formation efficiency or deplete only the central kiloparsecs?
* **Wiki basis:** `reservoir_response` axis; describes both retained-gas/low-SFE qualifiers and central-kpc depletion evidence.
* **Trust/evidence caveat:** Actively debated; evidence is mixed, and claims of universal reservoir emptying are prohibited.
* **Next docs-only action:** Distinguish the claim IDs supporting global depletion from those supporting central-only depletion within the evidence ledger.

### Topic 5: Maintenance Heating and Preventive Feedback
* **Question:** What is the observational support for preventive maintenance heating preventing further gas accretion?
* **Wiki basis:** `maintenance_heating_prevention` axis; noted as a possible channel under assumptions.
* **Trust/evidence caveat:** Contradicted or model-dependent; lacks accepted observational rows in the current local evidence pass.
* **Next docs-only action:** Identify any observational candidates (e.g., X-ray cavities, radio-mode duty cycles) in the local atlas that remain unverified or debated.

### Topic 6: Bridging Simulation Models with Observational Signatures
* **Question:** How do simulation-only mechanisms of galaxy evolution map to observed prevalence or outcomes?
* **Wiki basis:** `simulation_model_scope` axis; simulations test mechanisms but do not establish observed prevalence.
* **Trust/evidence caveat:** Model-dependent; simulation claims require explicit "in this model" wording until observation-linked validation is documented.
* **Next docs-only action:** Catalog simulation-backed claim rows and cross-reference them against locally available observational claims.

### Topic 7: Resolving Unmatched and Body-Only Claims
* **Question:** Which claims exist in the page body without corresponding snapshot atlas rows, and how can they be locally resolved?
* **Wiki basis:** Unmatched items section noting claim IDs 2915, 2921, and 2913, plus 2133 (missing source 2605.22497) and 2374 (garbled text).
* **Trust/evidence caveat:** These claims are explicitly flagged as unresolved gaps that prevent any future product binding until repaired.
* **Next docs-only action:** Prepare a targeted local inventory trace for IDs 2915, 2921, 2913, and source 2605.22497 to ready them for a P3 review.

### Topic 8: Reassessing the Baseline Map Recheck
* **Question:** What specific gaps in the status debate map trigger the PENDING_RECHECK caveat, and what evidence is required to clear it?
* **Wiki basis:** `FINAL_DRAFT_PATCHED_AFTER_GORU_BLOCKER_PENDING_RECHECK` baseline caveat carried across all sections.
* **Trust/evidence caveat:** This caveat applies to the entire debate map, indicating the map is a patched draft that must be re-scoped or resolved.
* **Next docs-only action:** Trace the "patched draft" history in the local handoffs to document the exact triggers for the recheck blocker.

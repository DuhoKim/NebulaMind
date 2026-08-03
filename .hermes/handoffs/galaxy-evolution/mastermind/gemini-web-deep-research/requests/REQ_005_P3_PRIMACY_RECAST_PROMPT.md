# Gemini-web Deep Research prompt template for RT quality

Marker to require in Gemini output: `GEMINI_WEB_RT_DEEP_RESEARCH_OUTPUT_DONE`

You are assisting a supervised NebulaMind research-topic quality pass. This is advisory research support only.

## Safety and truthfulness rules

- Do not claim access to files unless they are quoted in this prompt.
- Do not invent paper titles, DOI, ADS, arXiv IDs, URLs, numeric results, or source IDs.
- Every prior-study statement must include a source link or be labeled `UNCITED_NOT_USABLE`.
- Distinguish review/status papers, primary observations, simulations/models, surveys/instruments, and commentary.
- Distinguish established findings from open debate, sample-limited findings, simulation-only findings, and proposed future work.
- Do not recommend product DB/API/wiki publication, deployment, credentials, billing, or code changes.

## NebulaMind doctrine

Canonical flow: papers → claim/status ledger → research-status/debate map → prose/research-topic cards → derived claims/evidence/trust. Research-topic pages are proposed studies, not accepted results.

## Task

Method(s): `P3`
Topic/card(s): `Resolving primacy recast for claim 2572 (central property predictors vs halo mass).`
Current local source basis summary:

```text
Existing sources include 2512.16290v1 and 2401.12953. The current claim 2572 states an uncontested correlation ("Quenching in central galaxies correlates with central properties like velocity dispersion, bulge mass, and black hole mass.") but its pinned evidence (2512.16290v1) is marked as "refutes". This implies a dispute about predictor primacy, not just correlation. Claim 2573 further adds context that "The correlation between central galaxy quenching and halo mass is secondary."
```

Question for Gemini-web / Deep Research:

```text
Based on recent literature (including the listed arXiv sources), how should we reframe the predictor primacy debate between central properties (velocity dispersion, BH mass) and halo mass? Should claim 2572 be recast to: "Central properties such as velocity dispersion, bulge mass, and black-hole mass are the primary predictors of central-galaxy quenching, rather than halo mass" to properly support the debate structure? Provide a critical review of the provided sources to justify the recommended wording for 2572 and 2573.
```

## Required output format

For each card/topic, provide:

1. `Topic`
2. `Prior studies/reviews to verify locally`
   - bullet list; each bullet must include title/authors/year if known and a URL/DOI/arXiv/ADS link if available.
3. `What the literature appears to establish`
   - scoped findings only; each sentence must cite one of the listed links or be labeled `UNCITED_NOT_USABLE`.
4. `What remains unknown`
   - direct uncertainty: denominator, causal link, selection, redshift/mass scope, gas phase, model-vs-observation, etc.
5. `Data/survey plan`
   - named survey/instrument/archive/simulation → measurement → population/control/denominator.
6. `Analysis/decision criterion`
   - what result would support/refute or bound the hypothesis.
7. `Overclaim risks and wording guardrails`
8. `Do-not-use until verified`
   - claims/links/numbers that require local ADS/source verification before being used.

Finish with the exact standalone marker:

`GEMINI_WEB_RT_DEEP_RESEARCH_OUTPUT_DONE`

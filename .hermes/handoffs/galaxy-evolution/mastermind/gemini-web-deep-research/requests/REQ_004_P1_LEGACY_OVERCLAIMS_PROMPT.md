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

Method(s): `P1`
Topic/card(s): `Resolving legacy overclaims 2298 (AGN heating), 2299 (AGN expulsion), and 2924 (heating duplicate).`
Current local source basis summary:

```text
Existing sources include 2512.16208v1, 2602.07392, 2605.22497, 2606.05355, 1706.08987v2, 0906.2900v2. The claims state that AGN feedback universally heats/expels gas reservoirs, but newer successor claims (2945, 2946) state that maintenance/heating support is model-dependent, and gas removal alone cannot explain every quenching pathway.
```

Question for Gemini-web / Deep Research:

```text
Based on recent literature (including the listed arXiv sources), are broad, universal claims like "AGN feedback heats the gas reservoirs" (2298) and "expels gas" (2299) scientifically supported, or should they be recast to scoped, model-dependent conditional wording as suggested by claims 2945/2946? Please provide a critical review of the provided sources to justify whether we should retire or recast these legacy claims.
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

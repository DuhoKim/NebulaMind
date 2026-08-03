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

Method(s): `<M1/M2/M3/cross-method>`
Topic/card(s): `<exact RT cards or topic names>`
Current local source basis summary:

```text
<paste source-basis snippets, existing evidence links, claim/status labels, and current card text here>
```

Question for Gemini-web / Deep Research:

```text
Identify serious journal-quality prior-study grounding and missing-literature/status-map axes for these research-topic cards. Focus on what prior studies/reviews have actually established, what remains unknown, and which data/surveys/measurements would test the proposed research question.
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

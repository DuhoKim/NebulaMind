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

Method(s): `Cross-method`
Topic/card(s): `Overall report clarity, alternative summaries for the executive section, and structural QA`
Current local source basis summary:

```text
THE BASELINE — what “done” means here
papers → claim/status ledger → research-status/debate map → prose → derived claims/evidence/trust
The final goal is a trustworthy Galaxy Evolution wiki page: many papers are distilled into scoped claims, a debate/status map, reader-facing prose, and product/wiki claim chips/trust surfaces that do not contradict the prose. The method board now compares three ways to drive that paper-to-wiki work: source-first, claim-ledger reconciliation, and debate-map-to-wiki rebuild.

Latest result: 9-H2 contract confirmed; all three methods are running again
- User confirmation: The user confirmed the 9-H2 Galaxy Evolution skeleton for all methods and directed the board to keep working. The old confirm-or-recount gate is closed.
- Policy correction adopted: Hwao/Tori should self-resolve routine low-risk read-only counting/reconciliation conflicts from local evidence, then report. Human gates are reserved for substantive science/product choices or risky/mutating actions.
- Hwao sequencing: Hwao wrote the global sequencing record and three method GO packets: M1 draft assembly, M2 filename acceptance plus same-format conversion, and M3 P1.5 local-source gap-fill path.
- Method1: Method1 Hwao received the GO packet. It was briefly waiting on a local read-only snapshot inspection permission; Tori approved that exact safe command and Method1 resumed thinking.
- Method2: Method2 Hwao was restarted in a clean visible pane because the old pane had stale composer text. It received the acceptance/conversion GO packet and is reading/executing it.
- Method3: Method3 Hwao was restarted in a clean visible pane because the old pane had stale composer text. It received the P1.5 GO packet and is reading/executing it.
- Safety boundary: Allowed work remains method-local docs/static artifacts and receipts only. No live wiki publish, DB/SQL, trust recompute, deploy/restart, git, cloud/API/billing/OAuth, browser automation, cron, cross-method overwrite, or extra Ultra/Gemini/Antigravity action.
```

Question for Gemini-web / Deep Research:

```text
Can you provide 3 alternative, highly polished executive summaries for our live steering cockpit report based on the local source basis above? Are there any structural QA issues or clarity improvements that would make this report more journal-ready?
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

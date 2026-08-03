# Research-topic HTML helper lane briefs

Marker: `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z`
Helper brief marker: `RESEARCH_TOPICS_HELPER_LANE_BRIEFS_20260708T090359Z`
Parent order: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z.md`

## Universal scope for every helper

Read local resulted wiki artifacts and write only the named report/artifact in this brief. Do not use web search. Do not add external sources. Do not invent paper evidence, claim IDs, citation IDs, DOI/ADS links, trust levels, or product bindings.

Allowed reads:

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/`

Allowed writes:

- Exact report/artifact paths listed for your lane.

Hard-exclude / do not touch:

- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/` writes/copies
- restart/deploy/service mutation, including `:3000`
- product DB/SQL, pane-initiated SQL, `/api/pages`, page-version records, live wiki publish
- git commit/push/merge/rebase/reset/checkout/switch
- public cockpit/global/shared-parent mutation
- cloud/GCP/API/billing/OAuth/token/secret/credential/cookie files
- browser automation
- cron
- Method3 P3 product claim/citation binding

Every output must include:

- Parent marker `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z`.
- PASS/WARN/FAIL.
- Exact source wiki file(s) inspected.
- Topic count.
- Product claim/cite comment counts in any HTML you inspect/create.
- Active HTML safety result: no script/fetch/XHR/WebSocket/event-handler/external asset if you create HTML.
- Hard-excluded surface touched: expected `0`.

## Goru M1 — topic seed extraction

Model/lane: Gemini/Goru.

Read:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html`
- fallback canonical only if needed.

Task:
- Extract 6–12 research topics implied by the Method1 resulted wiki.
- Each topic: title, question, wiki basis, trust/evidence caveat, next docs-only research action.
- Focus on M1-specific signals: 3/30 evidence-bound vs 27 unbound, 2929/AGN caution, row/source ambiguity, unbound evidence gaps, packet-gated reconciliation limits.

Write:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/autopilot/RESEARCH_TOPICS_GORU_M1_SEED_20260708T090359Z.md`

## Kun M1 — HTML builder/validator

Model/lane: Codex/Kun. Use the current gpt-5.5 Kun lane; do not force Codex Spark unless the user explicitly asks for it.

Read Goru M1 seed if present plus Method1 source wiki.

Task:
- Build or validate Method1 topic HTML/MD/JSON/manifest in the required Method1 output directory from the parent order.
- If Hwao has already created the files, validate them instead of overwriting.
- Required HTML style: static wiki-like report with title, provenance note, TOC, topic cards, limitations, footer.

Write validation receipt:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/autopilot/RESEARCH_TOPICS_KUN_M1_VALIDATE_20260708T090359Z.md`

## Goru M2 — topic seed extraction

Model/lane: Gemini/Goru.

Read:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- compare v2 if useful.

Task:
- Extract 6–12 research topics implied by the Method2 source-first resulted wiki.
- Focus on M2-specific signals: accepted/limited/rejected/excluded source positions, 28060 no-current-target caution, 22-vs-21 totals caveat, cite-unmatched groups, source-first adjudication gaps.

Write:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/autopilot/RESEARCH_TOPICS_GORU_M2_SEED_20260708T090359Z.md`

## Kun M2 — HTML builder/validator

Model/lane: Codex/Kun. Use the current gpt-5.5 Kun lane; do not force Codex Spark unless the user explicitly asks for it.

Read Goru M2 seed if present plus Method2 source wiki.

Task:
- Build or validate Method2 topic HTML/MD/JSON/manifest in the required Method2 output directory from the parent order.
- If Hwao has already created the files, validate them instead of overwriting.

Write validation receipt:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/autopilot/RESEARCH_TOPICS_KUN_M2_VALIDATE_20260708T090359Z.md`

## Goru M3 — topic seed extraction

Model/lane: Gemini/Goru.

Read:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`

Task:
- Extract 6–12 research topics implied by the repaired Method3 debate-map wiki.
- Focus on debate-map axes: mechanism support, outflow prevalence, dominance debate, reservoir response, alternatives/countercases, maintenance heating, simulation scope, PENDING_RECHECK, unmatched items.
- Preserve docs-only/P3-closed boundary.

Write:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/autopilot/RESEARCH_TOPICS_GORU_M3_SEED_20260708T090359Z.md`

## Kun M3 — HTML builder/validator

Model/lane: Codex/Kun. Use the current gpt-5.5 Kun lane; do not force Codex Spark unless the user explicitly asks for it.

Read Goru M3 seed if present plus Method3 source wiki.

Task:
- Build or validate Method3 topic HTML/MD/JSON/manifest in the required Method3 output directory from the parent order.
- If Hwao has already created the files, validate them instead of overwriting.

Write validation receipt:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/autopilot/RESEARCH_TOPICS_KUN_M3_VALIDATE_20260708T090359Z.md`

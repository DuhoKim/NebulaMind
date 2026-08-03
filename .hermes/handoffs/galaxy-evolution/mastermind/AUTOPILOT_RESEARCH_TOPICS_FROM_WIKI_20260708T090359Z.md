# Hwao-led order — three method-matched research-topic HTML teams

Marker: `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z`
Continuation context: prose/evidence/trust wiki candidates from `AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z` and low-usage receipts from `AUTOPILOT_PROSE_EVIDENCE_TRUST_LOW_USAGE_CONTINUATION_20260708T083100Z`.
Estimated run: about 60–90 minutes (`estimated_total_seconds: 5400`).

## User direction

The user said: “let's launch another three autopilot teams matched to each method finding research topic based on the resulted wiki, so each results research topic lists in html format similar to wiki.”

Interpretation: launch one bounded docs/static team per Galaxy Evolution method. Each team reads its own resulted wiki candidate and derives a reader-facing list of research topics/questions/gaps suggested by that wiki. Each method output should be an HTML page in a wiki-like style, plus a small markdown/source-map/manifest packet. The work is based on local resulted wiki artifacts only unless the order explicitly says otherwise; do not browse or add new external evidence.

## Goal

Produce three additive, method-matched research-topic HTML candidates:

- Method1 topic list: research topics implied by the packet-gated/evidence-bound vs unbound view.
- Method2 topic list: research topics implied by the source-first accepted/limited/rejected/excluded view.
- Method3 topic list: research topics implied by the debate-map/trust-axis view.

Each HTML should look like a wiki/report page, not a raw checklist. Each topic card should include:

1. Topic title.
2. Plain-English research question.
3. Why this emerged from the wiki.
4. Method-specific evidence/trust basis from the local wiki candidate.
5. Scope/limits/caveats.
6. Suggested next research action, still docs-only.

Do not invent new paper evidence, claim IDs, citation IDs, DOI/ADS links, or product bindings. Use only what is visible in the current resulted wiki candidates and local sidecar maps/receipts.

## Required inputs / source wiki candidates

### Method1 source candidate

Prefer the richer Hwao variant if present; otherwise canonical:

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html`
- fallback: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`

### Method2 source candidate

Use the canonical deepened article as primary and compare v2 if useful:

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- comparison candidate: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html`

### Method3 source candidate

Use the repaired evidence/trust-visible M3 candidate:

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- evidence-basis ledger: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`

## Required output dirs and files

Use additive directories only. Do not overwrite the previous prose/evidence/trust candidate directories.

### Method1 output

Directory:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`

Files:
- `research-topics-from-wiki-20260708T090359Z.html`
- `research-topics-from-wiki-20260708T090359Z.md`
- `research-topic-map-20260708T090359Z.json`
- `manifest-20260708T090359Z.json`

### Method2 output

Directory:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/`

Files:
- `research-topics-from-wiki-20260708T090359Z.html`
- `research-topics-from-wiki-20260708T090359Z.md`
- `research-topic-map-20260708T090359Z.json`
- `manifest-20260708T090359Z.json`

### Method3 output

Directory:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/`

Files:
- `research-topics-from-wiki-20260708T090359Z.html`
- `research-topics-from-wiki-20260708T090359Z.md`
- `research-topic-map-20260708T090359Z.json`
- `manifest-20260708T090359Z.json`

## Required final artifact

Final no-apply rollup path:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot/AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z_FINAL_NO_APPLY_PACKET.md`

The final rollup must contain:

- `Status: COMPLETE`, `Status: READY_FOR_USER_APPROVAL`, or `Status: HARD_BLOCKED`.
- The marker `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z`.
- The word `wiki` so the watcher can mark completion.
- Per-method artifact table with paths, bytes, sha256(16), topic count, relative-link count, static-safety result, product claim/cite comment counts, and source wiki path.
- Verification receipts from Goru/Kun or equivalent local deterministic checks.
- Plain-English statement that these are research-topic candidates derived from resulted wiki pages, not new science evidence and not product binding.

## Method-lane work plan

### M1 team

- Hwao-m1 coordinates.
- Use M1 source candidate(s) to derive 6–12 research topics around evidence-bound vs unbound claims, AGN feedback caution, row-count ambiguity, source/evidence gaps, and follow-up questions.
- Goru/Gemini: exact topic count, evidence/trust basis count, source-wiki section map, static-safety scan.
- Kun/Codex/Spark: JSON/HTML validation, relative-link target scan, checksum manifest.
- Lana/Claude or Antigravity Claude: prose/no-overclaim review if available.

### M2 team

- Hwao-m2 coordinates.
- Use M2 source-first wiki to derive 6–12 research topics around accepted vs limited/rejected/excluded source positions, 28060 no-current-target caution, 22-vs-21 totals caveat, cite-unmatched groups, and source-first adjudication gaps.
- Goru/Gemini: exact topic count, accepted/limited/rejected/excluded linkage count, caveat visibility scan.
- Kun/Codex/Spark: deterministic validation and manifest.
- Lana/Claude or Antigravity Claude: prose/no-overclaim review if available.

### M3 team

- Hwao-m3 coordinates.
- Use repaired M3 wiki to derive 6–12 research topics around debate-map axes: mechanism support, outflow prevalence, dominance debate, reservoir response, alternatives/countercases, maintenance heating, simulation scope, PENDING_RECHECK, and unmatched items.
- Goru/Gemini: verify repaired M3 evidence/trust cards are carried into topic basis without product binding.
- Kun/Codex/Spark: deterministic validation and manifest.
- Lana/Claude or Antigravity Claude: prose/no-overclaim review if available.

## Output style requirements

Each HTML page should be static and self-contained:

- Similar wiki/report visual style: title, method label, provenance note, table of contents, topic cards, limitations, footer.
- Use plain English and short topic cards.
- Include local relative links back to the source wiki candidate and local sidecar JSON/Markdown where useful.
- No JavaScript. No fetch/XHR/WebSocket. No inline event handlers. No external assets.
- No product claim/cite comments unless they already exist in the source and are quoted as text; expected product claim/cite comment count is 0.
- Include a visible caveat: “Research topics are derived from the current local wiki candidate; they are hypotheses/questions for future work, not accepted claims.”

## Hard gates still closed

- Live-root writes/copies into `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/...`
- Any restart/deploy/service mutation, including `:3000` restart
- Product DB/SQL and pane-initiated SQL
- `/api/pages`, page-version records, live product wiki publish
- git commit/push/merge/rebase/reset/checkout/switch
- public cockpit/global/shared-parent mutation
- cloud/GCP/API/billing/OAuth/token/secrets/credentials/cookies
- browser automation
- cron
- Method3 P3 product claim/citation binding unless separately approved

## Safety ledger

Starting this order writes only this `.hermes` order, bounded working-repo static docs under the three method output dirs, and `.hermes` reports/receipts. It does not approve publication, restart, DB/API/page-version writes, git actions, cloud/API/billing/secret work, browser automation, cron, or Method3 P3 binding.

# Autopilot order — rewrite research topics as academic proposal-style agendas

Marker: `AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z`
User correction: the current research-topic pages are too jargonic. Rewrite them so a scientist/reader sees academic research proposals, not internal audit notes.
Estimated run: 60–90 minutes.

## Goal

Let the three topic autopilots revise the existing Method1 / Method2 / Method3 research-topic artifacts into **academic research-proposal style**.

Each method keeps its own point of view, but every topic should read like a concise mini-proposal with:

1. a clear proposal title,
2. a research aim / central question,
3. a short background and significance paragraph,
4. a survey/data plan naming the survey or observational/simulation data the project would use,
5. a study design / analysis approach,
6. expected contribution,
7. feasibility and caveats,
8. a small provenance note pointing back to the method wiki evidence basis.

The output should be understandable to an academic astronomy reader and should avoid front-loading internal terms like claim IDs, cite-unmatched, P3, bound/unbound-local, packet, lane, or audit. Claim/source IDs may appear only in a small provenance line at the end of a proposal card.

## Scope

Allowed:
- Read the existing local wiki-result and research-topic artifacts for the three methods.
- Overwrite the three existing `research-topics-from-wiki-20260708T090359Z` output sets in the working repo with improved proposal-style HTML/MD/JSON/manifest files.
- Write method-local receipts under `.hermes/handoffs/galaxy-evolution/<method>/autopilot/`.
- Write director progress/final rollup under `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/`.

Not allowed:
- No live-root writes/copies in `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/`.
- No frontend restart/deploy/service mutation.
- No product DB/SQL/API writes, `/api/pages`, page_versions, live wiki publish, trust recompute.
- No git commit/push/merge/rebase/reset/checkout/switch.
- No public cockpit/global/shared-parent mutation.
- No cloud/GCP/API/billing/OAuth/token/secret/credential/cookie reads or writes.
- No browser automation.
- No cron.
- No Method3 product claim/citation binding.

Tori may separately mirror a verified static artifact to the live public root only if the user separately approves or if the current chat instruction is treated by Tori as a narrow static-public update. Method autopilots must not do that themselves.

## Universal editorial requirements

For each method page:

- Use title: `Galaxy Evolution — Research proposal agenda (Method X)` or close equivalent.
- Start with a plain-language note: these are proposed studies derived from the method wiki, not accepted claims and not product-bound evidence.
- Prefer 5–8 polished proposal cards rather than a long list of jargonic gaps. If the prior page had 8/10/9 topics, merge overlapping items where it improves clarity, but preserve important questions.
- Every proposal card must include a visible section titled exactly `Survey/data plan`.
- The `Survey/data plan` must name the surveys, instruments, archives, simulations, or data families the proposed study would use and say what each contributes.
- Distinguish proposed data sources from current evidence. Do not imply a survey already supports a claim unless the source wiki already says so.
- Use existing/local survey names where available (examples from the current pages/corpus include DESI, MOSDEF, JWST, M51, X-ray cavity observations, IllustrisTNG/HORIZON-AGN-style simulations). You may list widely used astronomy data sources as proposed data families when appropriate — e.g. SDSS/MaNGA, ALMA, COSMOS/CANDELS/HST-JWST deep fields, Chandra/XMM/eROSITA, VLA/LOFAR, GALEX/WISE — but label them as proposed data to use, not as evidence already in the method wiki.
- Avoid internal jargon in headings. Examples:
  - Instead of `Does claim 2929's attached evidence...`, use `Testing whether AGN feedback directly regulates star formation`.
  - Instead of `cite-unmatched evidence`, use `Linking local source judgments to citable literature records`.
  - Instead of `P3 product binding`, use `future citation-binding step`.
- Keep the method caveat honest in plain words.
- No external links unless they already existed as relative local links. Prefer no external links at all.
- No `<script>`, `fetch`, XHR, WebSocket, inline event handlers, forms, remote assets, or external hosts.
- Product claim/cite comment counts in generated HTML must stay 0 / 0.

## Method1 task — packet-gated proposal agenda

Source wiki / local context:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html`
- Existing topic artifacts in `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`

Output path to overwrite:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
- matching `.md`, `research-topic-map-20260708T090359Z.json`, and `manifest-20260708T090359Z.json`

Method1 should focus on proposal-style studies around:
- separating internal AGN feedback from environment/halo effects,
- observational tests for maintenance heating versus simulation-only support,
- evidence-prioritization for under-supported sections,
- metadata/data-quality repair only as a methods appendix, not as a main science proposal unless framed academically.

Method1 receipt:
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/autopilot/RESEARCH_TOPICS_PROPOSAL_STYLE_M1_20260708T093140Z.md`

## Method2 task — source-first proposal agenda

Source wiki / local context:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- Existing topic artifacts in `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/`

Output path to overwrite:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
- matching `.md`, `research-topic-map-20260708T090359Z.json`, and `manifest-20260708T090359Z.json`

Method2 should focus on proposal-style studies around:
- robustness of AGN outflow claims to specific observations,
- observational paths out of model-dependence for maintenance heating,
- kinetic/radio-mode channels,
- M51-specific versus galaxy-general evidence,
- stellar-feedback versus AGN-feedback boundaries,
- gas removal versus recycling.

Method2 receipt:
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/autopilot/RESEARCH_TOPICS_PROPOSAL_STYLE_M2_20260708T093140Z.md`

## Method3 task — debate-map proposal agenda

Source wiki / local context:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`
- Existing topic artifacts in `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/`

Output path to overwrite:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
- matching `.md`, `research-topic-map-20260708T090359Z.json`, and `manifest-20260708T090359Z.json`

Method3 should focus on proposal-style studies around:
- when AGN feedback dominates relative to halo/environment/stellar channels,
- comparable-denominator AGN outflow prevalence,
- gas-reservoir response and star-formation efficiency,
- maintenance/preventive heating as an observational program,
- simulation-to-observation validation,
- non-AGN alternative-channel completeness.

Method3 receipt:
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/autopilot/RESEARCH_TOPICS_PROPOSAL_STYLE_M3_20260708T093140Z.md`

## Required validation

Each method verdict/receipt must report:
- PASS/WARN/FAIL.
- Exact files written.
- Proposal count.
- Confirmation that every proposal card has `Survey/data plan`.
- Product claim/cite comment counts: expected 0 / 0.
- Static safety: expected PASS with no script/fetch/XHR/WebSocket/event-handler/forms/external assets.
- Hard-excluded surfaces touched: expected 0.
- Short before/after style judgment: what jargon was removed or demoted.

Director final rollup path:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot/AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z_FINAL_NO_APPLY_PACKET.md`

Director final rollup must include:
- Status: COMPLETE or HARD_BLOCKED.
- Per-method proposal counts.
- A public-readability summary.
- Static validation results.
- Whether any live-root/public mirror happened (expected: 0 inside autopilots).
- The exact next action if Tori should mirror Method1 to the public live root.

Marker: `AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z`

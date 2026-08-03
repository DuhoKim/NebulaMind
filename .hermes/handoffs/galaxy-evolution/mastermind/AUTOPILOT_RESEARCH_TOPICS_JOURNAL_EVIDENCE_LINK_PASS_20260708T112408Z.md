# Autopilot order — research topics journal-quality evidence-link correction

Marker: AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z
Continuation: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Issued by: Tori/Hermes in response to direct user correction, 2026-07-08T11:24:08Z

## User correction
The public research-topic pages still read too casual/general for serious journal-publish-quality research, and the `What studies already show` / previous-studies sections do not visibly link to evidence. This is a quality failure. Treat the prior specificity pass as insufficient.

## Goal
Revise the three `research-topics-from-wiki-20260708T090359Z` static research-topic pages into formal, journal-prospectus-quality pages. Each proposal card must be suitable as a serious research agenda seed, not a casual web proposal.

## Required public-facing changes
For every proposal card in M1/M2/M3:
1. Use formal scientific wording. Avoid casual phrases, vague hype, blog-like phrasing, and unsupported conversational claims. Titles should read like specific study aims or research questions.
2. Rename/strengthen the previous-studies section if useful, e.g. `Prior evidence and constraints` or `What prior studies establish`, but keep the intent clear.
3. Every statement in that section must have visible evidence links near the statement:
   - Prefer direct source/evidence links already present in the local artifacts: arXiv links, source-basis page anchors, claim/status ledgers, evidence-basis sections, or local source ledger artifacts.
   - Do not invent paper titles, DOI/ADS records, source IDs, claim IDs, numeric results, or links.
   - If a statement cannot be linked to an existing source basis, delete it, narrow it, or explicitly mark it as an unlinked/local-method limitation — do not present it as prior evidence.
4. The visible evidence links must be usable on the public page. Examples: `[claim 2943 source basis](../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-20260708T043427Z.html#claim-2943)`, `[evidence row 28141 / arXiv:1706.08987v2](https://arxiv.org/abs/1706.08987v2)`, `[Method3 evidence basis §4](../evidence-trust-rebuild/evidence-basis-20260708T014205Z.md#s4)`. Prefer the actual links/anchors that exist after verification.
5. Evidence links must appear in the previous-studies/prior-evidence paragraph or list itself, not only in a trailing provenance footnote.
6. Keep data plans and analysis tests rigorous: specify population, denominator/control, measurement, and decision criterion where possible. Avoid overclaiming survey feasibility.
7. Keep provenance notes, caveats, and no-apply/static status.

## Minimum per-card structure
- `Research question` — one explicit, testable question.
- `Prior evidence and constraints` — linked evidence statements; visible links required.
- `Remaining uncertainty` — the exact gap (sample, denominator, causal link, redshift/mass scope, tracer, gas phase, selection function, or model-vs-observation boundary).
- `Data and measurement plan` — named data family tied to a measurement, not a shopping list.
- `Analysis and decision criterion` — comparison/model/test and what result would support/refute the hypothesis.
- `Limitations` — known caveats and non-binding status.
- `Provenance` — source IDs/labels may remain here, but this does not replace visible evidence links above.

## Method-specific grounding hints
- M1 source basis: `packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/`, especially claim anchors `ev-2931`, `ev-2929`, `ev-2946`, and coverage map evidence URLs. Do not turn M1 unbound-local claims into product evidence.
- M2 source basis: `source-first-paper-adjudication/p1-source-position-ledger.jsonl`, `p1-source-position-ledger.html`, `p2-claim-status-ledger.jsonl`, `p2-claim-status-ledger.html`, and `prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-deepening-map-20260708T043427Z.json`. Evidence rows include 28141, 28066, 28075, 28158, 28095, 28131, 28108, 28062, 28074, 28091, 28155, 28060, 28069, 28073, 28088. Link to arXiv IDs from the ledgers where available.
- M3 source basis: `debate-map-to-wiki-rebuild/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md`, `debate-map-to-wiki-rebuild/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-20260708T043427Z.json`, and the source page anchors. Use debate-map axis links and representative bibcode lists only as existing local provenance; do not invent external URLs for bibcodes unless an existing artifact supplies the link.

## Allowed writes
- Working static artifacts only under each method's existing `research-topics-from-wiki-20260708T090359Z/` directory:
  - `research-topics-from-wiki-20260708T090359Z.html`
  - `research-topics-from-wiki-20260708T090359Z.md`
  - `research-topic-map-20260708T090359Z.json`
  - `manifest-20260708T090359Z.json`
- Method-local receipts under `.hermes/handoffs/galaxy-evolution/method<N>/autopilot/`
- Director final rollup under `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/`

## Public mirror
Do not let method lanes write public live root. After director/Tori verification only, Tori may mirror the static files to `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/...` and verify public HTTP 200. No product DB/API/wiki publish.

## Verification required before PASS
For each method, report and Tori/director independently verify:
- proposal count remains 5–8 and actual count matches JSON/manifest
- every proposal has a prior-evidence section with at least one visible markdown/html link in that section
- all visible prior-evidence links resolve either as local static files/anchors or HTTP 200 external links
- no unsupported prior-evidence sentence remains without a link or explicit limitation label
- static safety: 0 `<script>`, `fetch(`, `XMLHttpRequest`, `WebSocket`, inline event handlers, `<form>`; no product `<!--claim:` or `<!--cite:` comments
- public wording is formal: no casual/blog-like phrases; no vague `studies show` without linked evidence
- no invented papers, DOIs, ADS records, source IDs, claim IDs, or numeric findings

## Required receipts
- `method1/autopilot/RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_M1_20260708T112408Z.md`
- `method2/autopilot/RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_M2_20260708T112408Z.md`
- `method3/autopilot/RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_M3_20260708T112408Z.md`
- final: `mastermind/autopilot/AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z_FINAL_NO_APPLY_PACKET.md`

## Hard gates closed
No product DB/SQL, `/api/pages`, page_versions/live wiki publish, trust recompute, backend/API restart, deploy, git commit/push/merge, public Baseline cockpit/global mutation, cloud/GCP/API/billing/OAuth/token/secrets, browser automation, cron, or Method3 P3 binding.

Stop only after public static pages are verified or after a hard-stop blocker.

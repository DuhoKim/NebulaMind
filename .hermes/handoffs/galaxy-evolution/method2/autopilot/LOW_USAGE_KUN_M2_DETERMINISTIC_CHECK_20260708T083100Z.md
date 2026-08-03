# Kun M2 deterministic Method2 validation

Marker: LOW_USAGE_KUN_M2_DETERMINISTIC_CHECK_20260708T083100Z
Continuation marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_LOW_USAGE_CONTINUATION_20260708T083100Z

Status: WARN

## Scope

Inspected only Method2 deepening artifacts under:

`frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-deepening-20260708T043427Z/`

and the Method2 Goru low-usage report:

`.hermes/handoffs/galaxy-evolution/method2/autopilot/LOW_USAGE_GORU_M2_VISIBLE_EVIDENCE_TRUST_AUDIT_20260708T083100Z.md`

## Files Inspected

| File | Bytes | SHA-256 |
|---|---:|---|
| `evidence-trust-coverage-map-deepening-20260708T043427Z.json` | 7449 | `109e7eee347d4607b49d2cea97214a37badcdcd5636296e2fd296fa7f124c66b` |
| `evidence-trust-deepening-map-20260708T043427Z.json` | 2411 | `5c6c2c6c7f54af0c3a6c0902e6b149280a5f0e7c17a9498db531295dc4274b7d` |
| `manifest-20260708T043427Z.json` | 1074 | `ec8ec45fff44061ea833059a7040181370b5b9fd11435dd93aac15de52bfc70b` |
| `manifest-deepening-20260708T043427Z.json` | 1590 | `0f969415f06c5f7fdc06dcb4cbe3f81ab0bbc7f06afd53e6f9a2976a518614bc` |
| `page-content-m2-v2-deepening-20260708T043427Z.md` | 12396 | `d507f600d086860e551b2d2f2a9e37b268142ac07de782e565349333c98609b0` |
| `page-content-prose-evidence-trust-deepening-20260708T043427Z.md` | 13260 | `34cb142aaa319f230308f3f2bfaa1988cd1e5f5fc4fb430314c7dadd4bf34cd2` |
| `wiki-prose-evidence-trust-deepening-20260708T043427Z.html` | 28700 | `e1806a75e5571241059b3f24fe2974bf8432bf71209735ffea47064813670ee7` |
| `wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html` | 12618 | `8b74182dfed0be4a4b17fe65ea4e9ad054e9d05273988fb461803fc8ddd25994` |
| Goru report | 2079 | `d6ac18225f0293e916a57f745da63bb95bb29663c0643e5b499a985e6d5442da` |

## Deterministic Checks

- JSON parse: PASS, 4/4 JSON files parse.
- Relative-link targets: PASS, 36/36 relative links resolve locally.
- External links: PASS, 0 external links found.
- Missing links: PASS, 0 missing targets.
- Active HTML safety: PASS.
  - `<script>` tags: 0
  - `<form>` tags: 0
  - `<iframe>` tags: 0
  - external `http(s)` refs in inspected HTML: 0
- Forbidden strings in generated deepening artifacts: PASS.
  - `/api/pages`: 0
  - `page_versions`: 0
  - `NebulaMind-origin-main-live`: 0

## HTML Product Comment Counts

- `wiki-prose-evidence-trust-deepening-20260708T043427Z.html`
  - `product_claim_comments=0/0`
  - `product_cite_comments=0/0`
  - `cite-unmatched` spans/text occurrences: 11
  - `data-claim-id` attrs: 0
- `wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html`
  - `product_claim_comments=0/0`
  - `product_cite_comments=0/0`
  - `cite-unmatched` spans/text occurrences: 15
  - `data-claim-id` attrs: 6

## Evidence / Trust Heuristics

Primary deterministic v2 map (`evidence-trust-deepening-map-20260708T043427Z.json`) reports:

- claims: 6
- claim_support_positions: 21
- accepted_full: 2
- accepted_limited_claim_support: 19
- excluded: 2
- rejected: 12
- no_claim_caveat_positions: 1
- numeric_product_cites: 0
- cite_unmatched_groups: 7

Legacy deepening map (`evidence-trust-coverage-map-deepening-20260708T043427Z.json`) reports the older totals:

- accepted_full: 2
- accepted_limited: 20
- cited_positions: 22
- per_claim_box_sum: 21
- excluded: 2
- rejected: 12

The 22-vs-21 caveat is visible in the artifacts.

## Visibility Checks

- 28060 visibility: PASS.
  - `evidence-trust-deepening-map-20260708T043427Z.json`: 3 occurrences
  - `page-content-m2-v2-deepening-20260708T043427Z.md`: 6 occurrences
  - `wiki-prose-evidence-trust-deepening-v2-20260708T043427Z.html`: 3 occurrences
- 22-vs-21 visibility: PASS.
  - v2 Markdown mentions both `22` and `21`.
  - v2 HTML mentions both `22` and `21`.
  - v2 map preserves legacy mismatch and corrected array-derived totals.
- cite-unmatched visibility: PASS.
  - v2 Markdown: 10 occurrences
  - v2 HTML: 15 occurrences
- trust labels visible: PASS.
  - v2 Markdown occurrences: accepted full 6, accepted-limited 28, excluded 7, rejected 4.
  - v2 HTML occurrences: accepted full 3, accepted-limited 22, excluded 7, rejected 2.

## Goru Cross-Check

Goru M2 report exists and reports `Status: PASS`.

Agreements:
- Goru and Kun both find 28060 visible.
- Goru and Kun both find the 22-vs-21 caveat visible.
- Goru and Kun both find cite-unmatched visibility preserved.
- Goru and Kun both find `product_claim_comments=0/0` and `product_cite_comments=0/0` for inspected HTML.
- Goru and Kun both find no hard-excluded surfaces touched.

WARN:
- Goru reports 24 relative-link occurrences in `wiki-prose-evidence-trust-deepening-20260708T043427Z.html`; this Kun scan counts 26 relative hrefs in that same HTML, all resolving locally. This is a count discrepancy only, not a broken-link finding.

## Verdict

WARN: deterministic validation passed for parse, local links, safety, product-comment absence, cite-unmatched visibility, 28060 visibility, and 22-vs-21 visibility. The only warning is the relative-link count discrepancy against Goru's report.

## Safety Ledger

- Hard-excluded surface touched: no / zero.
- Live-root writes/restart/deploy/service mutation: 0.
- Product DB/SQL, `/api/pages`, versions endpoint, live wiki publish: 0.
- Git/cloud/OAuth/secrets/browser/cron actions: 0.
- Evidence, IDs, source rows, URLs, or trust levels invented: 0.

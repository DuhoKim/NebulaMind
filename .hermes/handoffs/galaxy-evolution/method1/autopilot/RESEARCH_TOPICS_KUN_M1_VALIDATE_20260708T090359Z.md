# Kun M1 HTML Builder/Validator Receipt

Marker: `AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z`

Status: WARN

Verdict: Existing Method1 research-topic artifacts were validated rather than overwritten. Required files are present, JSON parses, topic count is in range, topic fields are complete, HTML is static-safe, relative links resolve, product claim/cite comment counts are zero, and the topic list is derived from the local Method1 wiki. WARN is retained because the manifest has no checksum field even though this lane was asked to validate a checksum manifest; current checksums are recorded below.

## Source Wiki Inspected

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html`
  - exists: yes
  - bytes: 50978
  - sha256: `62f0df71f8bbeed40b45b9b11a9a4669ab4dee0cb80f3bec4762a81e680da6fb`

Goru M1 seed status:

- Exact seed path from brief: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/autopilot/RESEARCH_TOPICS_GORU_M1_SEED_20260708T090359Z.md`
- exists: no
- Related mechanical check found and read: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/autopilot/GORU_M1_RESEARCH_TOPICS_CHECK_20260708T090359Z.md`

## Method1 Artifacts Validated

Output directory:

`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`

Required files:

| File | Present | Bytes | sha256 |
| --- | ---: | ---: | --- |
| `research-topics-from-wiki-20260708T090359Z.html` | yes | 13925 | `a57245c9f34cbacb98028c29c8d3ad139972b20a157ca252bc697cc2ee5f886e` |
| `research-topics-from-wiki-20260708T090359Z.md` | yes | 7401 | `420df00ff6212446daab49f5bd5f2dd5ecec7a5e02cd08e2e4ef40fd3686401d` |
| `research-topic-map-20260708T090359Z.json` | yes | 6958 | `c8005bcf6f3a113cfc050004eb5caa52151817b51841f86d81ee702aa5eba916` |
| `manifest-20260708T090359Z.json` | yes | 645 | `f5bbde3bf48732fe3cbd35c5de6aaa1562700c97778f5201c0474a6a286d04d0` |

## JSON Validation

- `research-topic-map-20260708T090359Z.json`: parse=PASS.
- `manifest-20260708T090359Z.json`: parse=PASS.
- Parent marker in JSON map: present.
- Parent marker in manifest: present.
- Topic count field in map: 8.
- Topics array length: 8.
- Manifest topic count: 8.
- Required topic fields checked: `id`, `title`, `q`, `why`, `basis`, `limits`, `next`.
- Missing required topic fields: 0.
- Topic IDs: `M1-RT-01`, `M1-RT-02`, `M1-RT-03`, `M1-RT-04`, `M1-RT-05`, `M1-RT-06`, `M1-RT-07`, `M1-RT-08`.
- Manifest static_safe: true.
- Manifest checksum field present: no.

## HTML Validation

- Parent marker occurrences in HTML: 2.
- Title/H1 present: yes.
- Method label present: yes.
- Provenance note present: yes.
- TOC present: yes.
- Topic card/section IDs visible: 8 unique IDs.
- Limitations section present: yes.
- Footer-like order/status line present: yes (`class="foot"`).
- Required caveat present: yes, "Research topics are derived from the current local wiki candidate; they are hypotheses/questions for future work, not accepted claims."
- Product claim comments: 0.
- Product cite comments: 0.

Active HTML safety result:

- `<script>` tags: 0.
- `fetch(` calls: 0.
- `XMLHttpRequest` references: 0.
- `WebSocket` references: 0.
- inline event handlers: 0.
- external/src assets: 0.
- Result: PASS.

## Markdown Validation

- Parent marker occurrences in Markdown: 1.
- Topic headings: 8.
- Product claim comments: 0.
- Product cite comments: 0.
- Caveat present: yes.

## Relative Link Scan

- HTML links total: 10.
- Relative links: 2.
- Relative links resolving locally: 2.
- Relative links missing locally: 0.

Resolved relative links:

1. `../prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html`
   - exists: yes
   - resolved path: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html`
2. `../prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json`
   - exists: yes
   - resolved path: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json`

## Topic Count And Scope

- Topic count: 8.
- Required range from parent order: 6-12.
- Scope basis: local Method1 resulted wiki and local sidecar coverage map only.
- No web search used.
- No external sources added.
- No invented paper evidence, claim IDs, citation IDs, DOI/ADS links, trust levels, or product bindings found in validation.

## Product Comment Counts

- HTML product_claim_comments=0.
- HTML product_cite_comments=0.
- Markdown product_claim_comments=0.
- Markdown product_cite_comments=0.

## Hard-Excluded Surface Touched

- Live-root writes/copies: 0.
- Restart/deploy/service mutation including `:3000`: 0.
- Product DB/SQL, pane SQL, `/api/pages`, page-version records, live wiki publish: 0.
- Git commit/push/merge/rebase/reset/checkout/switch: 0.
- Public cockpit/global/shared-parent mutation: 0.
- Cloud/GCP/API/billing/OAuth/token/secret/credential/cookie files: 0.
- Browser automation: 0.
- Cron: 0.
- Method3 P3 product claim/citation binding: 0.

Final status: WARN. The existing Method1 research-topic packet is valid and static-safe, with 8 grounded topics and zero product claim/cite comments; only the missing manifest checksum field prevents a clean PASS.

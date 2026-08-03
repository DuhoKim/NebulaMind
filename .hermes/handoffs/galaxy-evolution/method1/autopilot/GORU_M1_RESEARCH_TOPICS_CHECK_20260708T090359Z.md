# Goru/Gemini — Method1 research-topics mechanical check

Order marker: AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z
Lane: Method1 Goru (mechanical, read-only). UTC: 2026-07-08T09:0xZ

## Files (on-disk fingerprints)
Dir: `…/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`
| File | Bytes | sha256[:12] |
|------|------:|-------------|
| `research-topics-from-wiki-20260708T090359Z.html` | 13,925 | `a57245c9f34c` |
| `research-topics-from-wiki-20260708T090359Z.md` | 7,401 | `420df00ff621` |
| `research-topic-map-20260708T090359Z.json` | 6,958 | `c8005bcf6f3a` |
| `manifest-20260708T090359Z.json` | 645 | `f5bbde3bf487` |
Additive: prior `prose-evidence-trust-*` dirs untouched.

## Counts / conformance
| Check | Result | Status |
|-------|--------|:------:|
| Research topic cards | 8 (order asks 6–12) | PASS |
| Required fields per card (question/why/basis/limits/next) | 8/8/8/8/8 | PASS |
| Wiki-style shell (title, method label, provenance, TOC, cards, limitations, footer) | present | PASS |
| Caveat "hypotheses… not accepted claims" | present | PASS |
| Relative links back to source wiki + sidecar | 2 (both resolve on disk) | PASS |
| Product claim/cite comments (`<!--claim/cite-->`) | 0 (expected 0) | PASS |
| Static-safety (`<script>`, fetch/XHR/WebSocket, on* handlers, external assets) | 0 / 0 / 0 / 0 | PASS |
| Topic basis references real wiki artifacts (claims 2929/2931/2946, 27-unbound, 2/9 per-section, data-quality flags) | yes | PASS |

## No-invention
Every topic's "basis" points to a card/section/count visible in the M1 source wiki (`wiki-prose-evidence-trust-deepening-hwao-…`) or its coverage map. No new paper evidence, claim/cite IDs, DOIs, or product bindings introduced.

## Verdict
**PASS** — 8 grounded research topics in wiki style, static-safe, zero product binding, links resolve, no invention. 0 WARN / 0 FAIL.

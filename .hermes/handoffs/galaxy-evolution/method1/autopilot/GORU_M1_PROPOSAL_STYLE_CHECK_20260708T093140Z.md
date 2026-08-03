# Goru/Gemini — Method1 proposal-style mechanical check

Order marker: AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z
Lane: Method1 Goru (mechanical, read-only). UTC: 2026-07-08T09:3xZ

## Files (overwrote prior topic set)
Dir: `…/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`
| File | Bytes | sha256[:12] |
|------|------:|-------------|
| `research-topics-from-wiki-20260708T090359Z.html` | 15,050 | `ca4599f77053` |
| `research-topics-from-wiki-20260708T090359Z.md` | 10,476 | `8d2d3f8cce9d` |
| `research-topic-map-20260708T090359Z.json` | 5,142 | `3f4d1292290d` |
| `manifest-20260708T090359Z.json` | 663 | `d9c9f17ce03d` |

## Conformance (order §127–137)
| Check | Result | Status |
|-------|--------|:------:|
| Proposal count (5–8) | 6 | PASS |
| Every proposal has `Survey/data plan` | 6/6 | PASS |
| 8 proposal fields per card (aim/background/data plan/design/contribution/feasibility + title + provenance) | present | PASS |
| Named data families in plans | SDSS-MaNGA, SAMI, ALMA, Chandra, XMM-Newton, VLA, LOFAR, JWST, GAMA, COSMOS/CANDELS, Euclid, Rubin(LSST), eROSITA, DESI, IllustrisTNG, HORIZON-AGN, NASA ADS | PASS |
| Proposed data labeled as future (not existing evidence) | yes ("proposed", "not treated as decisive", "benchmark to test") | PASS |
| Jargon in headings/body (unbound-local, cite-unmatched, P3, packet, lane, audit) | 0 | PASS |
| Proposal IDs collide with internal "P3" | no (renamed RP-1…RP-6) | PASS |
| Claim IDs (2929/2931/2946) confined to provenance lines | yes (3 mentions, all in `prov`) | PASS |
| Product claim/cite comments | 0 / 0 | PASS |
| Static-safety (`<script>`, fetch/XHR/WebSocket, on* handlers, forms, external assets/hosts) | 0 across all | PASS |
| Plain-language caveat ("not accepted claims") | present | PASS |
| JSON valid (topic map + manifest) | both valid | PASS |
| Hard-excluded surfaces touched | 0 | PASS |

## Verdict
**PASS** — 6 academic proposal cards, each with a named Survey/data plan, de-jargonized, static-safe, zero product binding, no invention. 0 WARN / 0 FAIL.

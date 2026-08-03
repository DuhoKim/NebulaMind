# Goru/Gemini — Method1 journal-prospectus evidence-link check

Order marker: AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z
Lane: Method1 Goru (mechanical, read-only). UTC: 2026-07-08T11:2xZ

## Files (overwritten in place)
Dir: `…/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`
| File | Bytes | sha256[:12] |
|------|------:|-------------|
| `research-topics-from-wiki-20260708T090359Z.html` | 23,798 | `052f9fcd308f` |
| `research-topics-from-wiki-20260708T090359Z.md` | 15,319 | `47456addc4bf` |
| `research-topic-map-20260708T090359Z.json` | 10,012 | `103aa4d4a5f6` |
| `manifest-20260708T090359Z.json` | 671 | `0a5daef33d09` |

## Prior-evidence links (order requirement) — PASS
| Proposal | Prior-evidence links | Handling |
|----------|:--------------------:|----------|
| RP-1 | 8 arXiv | all recorded non-committal (honestly stanced) |
| RP-2 | 13 arXiv | 4 supporting + 9 non-committal (stance-tagged) |
| RP-3 | 8 arXiv | all supporting, predominantly simulation |
| RP-4 | 0 direct + coverage-map link | absence is the premise; **unlinked-limitation note** present |
| RP-5 | 0 direct + coverage-map link | evidence tabulation artifact linked |
| RP-6 | 0 direct + coverage-map link | builds on RP-1/RP-3; coverage record linked |
- All 6 cards carry a formal **Prior evidence** section with links *inside* it (not just a trailing provenance line).
- Total prior-evidence links: 29 (26 distinct arXiv) + 3 coverage-map artifact links.

## Link resolution — PASS
- 0 malformed `/abs/arXiv:` URLs (double-prefix normalized); 29/29 arXiv URLs well-formed (`/abs/NNNN.NNNNN`).
- Coverage-map relative link resolves on disk.
- Links point only to arXiv records already present in the local M1 ledger + the local coverage map — no invented papers/DOIs/IDs.

## Static safety / binding / tone — PASS
`<script>` 0 · fetch/XHR/WebSocket 0 · on* handlers 0 · remote assets (img/script/link/iframe) 0 · product `<!--claim/cite-->` 0/0 · jargon headings 0 · casual-word scan 0 (formal register).

## Verdict
**PASS** — every proposal has a formal, linked prior-evidence section; links are real, well-formed, and resolve; unlinkable prior-evidence marked as limitation; static-safe; no invention. 0 WARN / 0 FAIL.

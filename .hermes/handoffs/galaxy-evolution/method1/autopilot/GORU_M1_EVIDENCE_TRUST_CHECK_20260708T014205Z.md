# Goru — Method1 evidence/trust candidate mechanical check

Order marker: AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Lane: Method1 Goru (mechanical, read-only over generated candidate). Authored UTC: 2026-07-08T~01:45Z

## Candidate files (exist + non-empty)
Dir: `…/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/`
| File | Bytes | Status |
|------|------:|:------:|
| `evidence-trust-preview-20260708T014205Z.html` | 37,763 | PASS |
| `evidence-trust-bindings-20260708T014205Z.md.json` | 17,491 | PASS |
| `manifest-20260708T014205Z.json` | 468 | PASS |
Old artifacts preserved (not overwritten): `same-format-rebuild/wiki-format-preview-20260707T064500Z.html` (24,033 B), `wiki-page.html` (29,063 B). PASS.

## Evidence/trust content counts
| Metric | Count | Note |
|--------|------:|------|
| Claim chips rendered | 30 | matches page (open==close set) |
| Chips evidence-bound (trust badge) | 3 | 2931 debated · 2929 unverified · 2946 reported |
| Evidence panels | 3 | one per bound claim |
| Evidence rows linked | 43 | 2931=20, 2929=14, 2946=9 (verbatim from ledger) |
| Evidence hrefs | 43 | all `https://arxiv.org/abs/…` (real, per-evidence) |
| Local ledger hrefs | 4 | relative → `pgr-current-page-inventory-20260706T130610Z.json` |
| Chips unbound-local (labeled) | 27 | honest label; no invented evidence |
| Per-page trust summary | present | tiles + prose from real counts |

## Static-safety scan (PASS)
| Check | Result |
|-------|:------:|
| real `<script>` tags | 0 |
| inline `on*` event handlers | 0 |
| `fetch(` / `XMLHttpRequest` / `WebSocket` calls | 0 (1 string hit = escaped descriptive text "no fetch/XHR/WebSocket", not a call) |
| external hosts | **arxiv.org only** (43); no other host |
| `/api` / DB / live-publish routes | 0 (1 string hit = descriptive "no /api or DB routes") |
| `<!--cite:-->` markers injected into page.content | 0 (product cite IDs not locally resolvable → not invented) |

## Provenance-integrity (no invention) — PASS
- 43 arxiv URLs, titles, years, stances, votes, and quality fields are copied verbatim from `watch_claim_evidence_raw` in the local M1 inventory ledger. Independent recount: bindings JSON carries 43 arxiv URLs.
- Trust levels (debated/unverified/reported) and trust scores are the ledger's, not assigned.
- 27 unbound chips carry no fabricated evidence; explicitly labeled unbound-local (product-layer gate).

## Verdict (Goru)
**PASS** — candidate adds real, static-safe evidence links + visible trust leveling; 0 invented IDs/links; 0 active-call surfaces; old pages preserved. 0 WARN / 0 FAIL.

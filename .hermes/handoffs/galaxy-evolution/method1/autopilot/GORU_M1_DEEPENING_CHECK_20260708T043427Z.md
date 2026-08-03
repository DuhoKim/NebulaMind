# Goru — Method1 v2 deepening mechanical check

Order marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z
Lane: Method1 Goru (mechanical, read-only). Checked UTC: 2026-07-08T04:40:23Z

## Candidate files (on-disk fingerprints)
Dir: `…/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-deepening-20260708T043427Z/`
| File | Bytes | sha256[:16] |
|------|------:|-------------|
| `wiki-prose-evidence-trust-deepening-20260708T043427Z.html` | 48,952 | `f9eb0efdaf66a1b1` |
| `page-content-prose-evidence-trust-deepening-20260708T043427Z.md` | 16,628 | `aacf40b494c15a78` |
| `evidence-trust-coverage-map-deepening-20260708T043427Z.json` | 16,315 | `0c2673405b7cc034` |
| `manifest-deepening-20260708T043427Z.json` | 695 | `54a38fb99b8e03c8` |
First-pass `prose-evidence-trust-upgrade/` preserved (not overwritten). PASS.

## Deepening deltas vs first pass (order §25) — all present
| Improvement | Evidence |
|-------------|----------|
| Explicit 2929 caution | 1 dedicated caution block: 14 rows all non-committal, **6 of 8 distinct papers are unresolved arXiv IDs**, ≥1 loosely-related title → "candidate context, not support" |
| Distinct-paper vs row-count wording | "How to read the evidence counts" explainer + 5 inline "N rows / M papers" dual counts |
| Unresolved-title flags | 21 rows flagged `unresolved title` |
| 3/30 + 27 unbound honesty kept | 3 trust badges, 27 "no local evidence / unbound", explicit 3-of-30 statement |
| All evidence/trust data preserved | coverage map carries full 43 rows |

## Static-safety (PASS)
real `<script>` 0 · `on*` handlers 0 · fetch/XHR/WebSocket 0 · external hosts = **arxiv.org only** (43) · no /api or DB routes · no `<!--cite:-->` injected.

## No-invention (PASS)
26 distinct arXiv URLs; **all 26 present in the local ledger**; 0 not found. Counts (43 rows / 26 distinct / 6-of-8 unresolved for 2929) recomputed from `watch_claim_evidence_raw`.

## Verdict
**PASS** — deeper, honest, static-safe, zero invention; the specific 2929 caution + rows-vs-papers clarity requested by the order are in place. 0 WARN / 0 FAIL.

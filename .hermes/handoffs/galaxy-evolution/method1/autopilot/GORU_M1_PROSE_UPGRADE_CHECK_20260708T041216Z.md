# Goru — Method1 prose/evidence/trust upgrade mechanical check

Order marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z
Lane: Method1 Goru (mechanical, read-only over generated candidate).

## Concurrent-pane reconciliation (important)
This lane's generator first produced these candidate files; a **concurrent M1 pane then overwrote the same filenames** (all four, mtime 13:18:47). Per multi-pane safety I did NOT re-clobber them — I re-verified the **surviving on-disk files** instead. All counts/checks below are re-run against the on-disk (surviving) versions. They PASS.

## Candidate files (exist + non-empty — on-disk fingerprints)
Dir: `…/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/`
| File | Bytes | sha256[:16] |
|------|------:|-------------|
| `wiki-prose-evidence-trust-upgrade-20260708T041216Z.html` | 36,920 | `39249ce096250623` |
| `page-content-prose-evidence-trust-upgrade-20260708T041216Z.md` | 21,663 | `d5e0f107c570f7dd` |
| `evidence-trust-coverage-map-20260708T041216Z.json` | 5,064 | `d55f95a87d7d8e92` |
| `manifest-20260708T041216Z.json` | 1,599 | `cf4b3f20fc6d936e` |
Preserved (not overwritten): `wiki-page.html`, `same-format-rebuild/`, `evidence-trust-rebuild/`. PASS.
Note: on-disk MD is pure prose (0 claim markers) vs this lane's marker-preserving MD — acceptable for a prose candidate; HTML is the primary visible artifact.

## Coverage counts
| Metric | Count |
|--------|------:|
| Claim chips rendered | 30 |
| Evidence-linked chips (trust badge) | 3 (2946 reported · 2931 debated · 2929 unverified) |
| "no local evidence / unbound" chips | 27 |
| Evidence panels | 3 |
| Evidence rows | 43 (2931=20, 2929=14, 2946=9) |
| Distinct papers (union) | 26 |
| Trust vocabulary terms defined on-page | 4 |
| Prose boxes (lead/vocab/coverage/conclusion+limits) | 4 + article narrative |
| MD claim markers open/close | 30 / 30 |
| MD coverage + limitations sections | present |

## Static-safety (PASS)
real `<script>` 0 · inline `on*` handlers 0 · `fetch`/`XMLHttpRequest`/`WebSocket` calls 0 · external hosts = **arxiv.org only** (43 links) · no /api or DB routes · no `<!--cite:-->` injected into content.

## No-invention cross-check (PASS)
26 distinct arXiv URLs in the HTML; **all 26 present verbatim in the local ledger** `pgr-current-page-inventory-20260706T130610Z.json`; 0 not found. Trust levels, stances, votes, years, distinct-paper counts all trace to `watch_claim_evidence_raw`. 27 unbound chips carry no fabricated evidence.

## Verdict
**PASS** — prose-rich, statically safe, honestly bounded (3/30 evidenced, 27 explicitly unbound), zero invention. 0 WARN / 0 FAIL.

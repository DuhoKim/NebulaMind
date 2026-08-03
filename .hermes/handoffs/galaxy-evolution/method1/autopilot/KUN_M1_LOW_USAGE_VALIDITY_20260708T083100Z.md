# Kun/Codex — Method1 low-usage deterministic validity check

Order marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_LOW_USAGE_CONTINUATION_20260708T083100Z
Lane: Method1 Kun (deterministic, read-only). UTC: 2026-07-08T08:35Z

## Targets
- HTML: `…/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html`
- JSON: `…/evidence-trust-coverage-map-deepening-hwao-20260708T043427Z.json`

## Checks (all PASS)
| Check | Result |
|-------|--------|
| JSON parses (coverage map) | ✅ valid; keys marker/version/method/page/continuation_of/policy/bound/… |
| HTML tag balance | ✅ `<section>` 11/11, `<table>` 4/4 |
| Chip→evidence anchors resolve | ✅ 3 `href="#…"` targets all exist among 6 `id`s (chip-XXXX + ev-XXXX); 0 dangling |
| Relative ledger link resolves | ✅ `../pgr-current-page-inventory-20260706T130610Z.json` exists on disk |
| Table/card counts | ✅ 4 tables, 3 evidence cards, 56 `<tr>` (43 evidence + 3 headers + 10 per-section) |
| Card count == bound count == JSON evidence_linked | ✅ 3 == 3 == 3 |
| Reproducibility | ✅ deterministically regenerable from `same-format-rebuild/page-content-…md` + the ledger (generator is data-driven; no random/time inputs) |
| External-link host | ✅ arxiv.org only; 0 script/fetch |

## Verdict
**PASS** — valid, internally consistent, reproducible; no dangling anchors, no broken relative links, no row/table mismatch.

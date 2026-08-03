# Goru — cross-method consistency check (Method1-authored, read-only)

Order marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_LOW_USAGE_CONTINUATION_20260708T083100Z
Lane: Method1 Goru (read-only cross-method mechanical audit, per order §34). UTC: 2026-07-08T08:54Z
Scope: read-only comparison of the three method deepening HTML candidates. Method1 authors this as an input to the director's cross-method index; M2/M3 content stays owned by their lanes.

## Candidates scanned (read-only)
| Method | file | bytes | sha[:12] |
|--------|------|------:|----------|
| M1 | `packet-gated-…/prose-evidence-trust-deepening-…/wiki-…-deepening-hwao-…html` | 50,978 | `62f0df71f8bb` |
| M2 | `source-first-…/prose-evidence-trust-deepening-…/wiki-…-deepening-v2-…html` | 12,618 | `8b74182dfed0` |
| M3 | `debate-map-…/prose-evidence-trust-deepening-…/wiki-…-deepening-…html` | 32,884 | `2b18bb5fd88b` |

## Consistency — safety-critical invariants (ALL PASS, consistent)
| Invariant | M1 | M2 | M3 |
|-----------|:--:|:--:|:--:|
| Static-safe (`<script>`=0, fetch/XHR/WebSocket=0) | ✅ | ✅ | ✅ |
| Order/parent marker present | ✅ | ✅ | ✅ |
| Product-binding markers (`<!--claim/cite-->`) = 0 | ✅ | ✅ | ✅ |
| External hosts | arxiv.org only | none | none |
All three are inert static docs with no product binding — consistent and safe.

## Divergence — reader-facing evidence/trust layout (expected, not a defect)
- **M1:** 4 tables (3 evidence cards + per-section rollup). **M3:** card/div layout (0 `<table>`), consistent with its 9-evidence-card repaired standard. **M2:** 6 tables (accepted/limited/excluded grouping). Different shapes reflect different data models — not an inconsistency to "fix."

## Real gap — trust-scale non-comparability messaging is uneven (order §39/§105)
Heuristic scan (regex on "not comparable / different scale / do not compare / per-method"):
- **M1: present** (explicit "This vocabulary is specific to Method 1 … do not compare labels across methods").
- **M2: not matched** — appears to lack an explicit "trust scales are not comparable across methods" note.
- **M3: not matched by this heuristic** — may phrase it differently (trust-vocab terms are present); M3 lane to confirm.
This is a heuristic (may miss differently-worded notes) — flagged for the M2/M3 lanes and the director. **The order requires cross-method navigation to state that M1/M2/M3 trust scales are not comparable.** The director's cross-method index/legend MUST carry that statement explicitly; each method page ideally repeats it (M1 already does).

## Recommendation to director
1. Confirm/add the explicit "trust scales not comparable" line on M2 (and verify M3's wording).
2. The final packet's per-method table can use the safety-critical row above (all static-safe, marker-present, 0 product binding).
3. M1 needs no change — it satisfies the bar and carries the non-comparability note.

## Safety ledger
Read-only scan only. DB/SQL 0 · /api 0 · publish 0 · live-root 0 · restart 0 · git 0 · cloud/browser/cron 0 · writes: this one `.hermes` observation.

Status: **CONSISTENCY PASS on safety invariants; one honesty gap (non-comparability note on M2, verify M3) flagged for lanes/director.**

# Lana M3 sustaining review — cycle 3 (stability + cross-surface consistency audit)

Parent marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z
Seed marker: DEEPENING_RESOURCE_SEED_20260708T043427Z
Role: Lana-M3 — prose / no-overclaim / debate-map-trust review (read-only, no edits).
Written UTC: 05:07Z. **Progress/review artifact — NOT the final packet** (floor 2026-07-08T06:34:40Z; ~1h27m remain).

## Verdict: **PASS (strong) — sustained.** No change to candidate since cycle 2; cross-surface consistency now independently verified. 2 WARNs remain open (1 refined).

## Freshness (current mtimes/sizes judged)
The M3 v2 set is **byte-identical to cycle 2** — no authoring since 04:44Z:
- `page-content-…md` 18,220 B / 04:40:12Z · `wiki-prose-…html` 22,221 B / 04:43:20Z · `evidence-trust-coverage-map-…json` 13,673 B / 04:41:28Z · `manifest-…json` 4,525 B / 04:44:27Z.
- Cross-method deepening dir/index still **ABSENT**; no newer M3 deepening artifacts. My cycle-2 review (`DEEPENING_LANA_M3_CYCLE_02_REVIEW_…`, PASS + WARN-A/WARN-B) stands verbatim for content; this cycle adds a cross-surface consistency audit not done before.

## New this cycle — cross-surface trust-vocabulary consistency audit (all PASS)
Verified the debate-map trust vocabulary agrees across every v2 surface and the source of truth, so a reader can't be shown one status in prose and another in the legend:
- **Axis→status agreement — 7/7 OK.** `status_debate_map.json` (source) == coverage-map `deepened_axis_legend` (7 axes) == HTML "Deep Trust Legend" (all 7 axes covered — mechanism/outflow/dominance/reservoir/alternatives extracted directly; maintenance & simulation present as "…dependent - <axis>"). Zero mismatches.
- **Reader-guard faithfulness — aligned.** The coverage-map legend's `reader_guard` values echo the source guards: `dominance_debate` → "do not render a winner" (both), `maintenance_heating_prevention` → "model-dependent" (both). No guard was weakened or contradicted.
- **Outflow-fraction honesty holds on every surface.** MOSDEF 17% (z=1.4–3.8) and JWST 46% Na I D (z~2) appear on both `.md` and HTML with **no illegally-merged range** (no "17–46"); kept as "two different scoped measurements." The never-merge guard is intact cross-surface.
- **Overclaim scan — clean cross-surface.** Only "not proof" (negation) on both `.md` and HTML.
- **Static-safety — PASS** (unchanged): 0 `<script>`/`fetch`/XHR/WebSocket/`/api/pages`/`page_versions`/live-root in the HTML.

## Acceptance-criteria status (first-pass gaps → cycle 3)
| Criterion | Status |
|---|---|
| Deepen trust language + consolidated legend | **MET** (per-section guards + Deep Trust Legend, 7/7 axes, source-faithful) |
| Unmatched/PENDING_RECHECK visible in-body | **MET** (Evidence Status & Known Gaps + coverage-map `known_gaps`) |
| P3 closed + preconditions stated; 0 product binding | **MET** |
| No-invent / no-overclaim / cross-surface status agreement | **MET (verified this cycle)** |
| Per-section resolved provenance IDs (claim_id/source_id/anchor) | **PARTIAL → WARN-A (refined)** |
| Canonical 9-H2 same-format conformance | **NOT MET (deliberate) → WARN-B** |
| Cross-method trust legend + index | **OPEN** — cross-method dir still absent |

## WARNs (open; unchanged since cycle 2 because files unchanged)
- **WARN-A (refined, narrower than cycle 2).** The coverage-map **does** retain per-*axis* provenance: `deepened_axis_legend[]` carries `trace_ledger_entry_ids` + `representative_bibcodes` for all 7 axes (and `known_gaps` retains the unmatched IDs). What was dropped vs the first pass is the per-**section** resolved `local_claim_ids` / `source_ids` / `basis_anchor` mapping (and the `.md`'s "Local provenance §X" pointers). Net: axis→ledger/bibcode traceability is good; section→exact-paper traceability is coarser than first-pass. Recommend restoring per-section resolved IDs (or `.md` pointers to the first-pass coverage map). Not a total provenance loss — a granularity reduction. (Kun/reproducibility co-owns.)
- **WARN-B (carried).** Article region has 10 H2 (9 canonical + "Evidence Status & Known Gaps"); one beyond the canonical 9 — great for docs-only transparency, reconcile (meta appendix / non-H2 callout) if routed to same-format/P3. The Deep Trust Legend is correctly counted OUTSIDE the article (manifest `html_article_anchor_count: 10`); minor: HTML uses no literal `<article>` element, so Goru's same-format check should fix a consistent article definition.

## Boundaries honored
Read-only inspection + this one `.hermes` report only. Zero edits; zero live-root touch; no mirror, restart/deploy, DB/API/page_versions/product-wiki publish, git, browser, cloud/secrets, cron. No final packet (before floor). No hard-gate prompt. Local `python3`/`stat` read-only only.

## Next (sustaining)
- WARN-A (restore per-section resolved provenance IDs) + WARN-B (10th-H2 conformance) for the M3 author + Goru/Kun; both are safe local edits if a lane picks them up before finalization.
- Cross-method `cross-method-trust-legend-…md` + `index-…html` still owed — review when present; M3's 7-axis legend is source-faithful and ready to feed it.
- Continue cycle reviews until 06:34:40Z; do not author the final no-apply packet before then.

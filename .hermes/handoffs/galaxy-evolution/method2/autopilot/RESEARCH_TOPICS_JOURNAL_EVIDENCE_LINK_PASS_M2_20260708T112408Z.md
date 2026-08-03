# Method2 — research prospectus, journal-quality evidence-link pass: receipt + verdict

Marker: AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z · Continuation: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Role: Hwao-m2 (verdict) + Goru/Kun (verification). UTC: 2026-07-08T11:24:08Z
Status: **PASS / COMPLETE**

## Files written (overwrote in place, per order)
`…/source-first-paper-adjudication/research-topics-from-wiki-20260708T090359Z/`
| file | bytes | sha256(16) |
|---|---|---|
| `research-topics-from-wiki-20260708T090359Z.html` | 21317 | `d8502523e2f21198` |
| `research-topics-from-wiki-20260708T090359Z.md` | 14096 | `d466e14fc76d43e1` |
| `research-topic-map-20260708T090359Z.json` | 16491 | `65438142ffa8f970` |
| `manifest-20260708T090359Z.json` | 823 | `7a142c552decafdc` |

## Required validation
- **PASS/WARN/FAIL: PASS.**
- **Proposal count: 6** (5–8; matches JSON/manifest).
- **Every proposal has a `Prior evidence and constraints` section with visible links inside it** — links per card: **P1 5 · P2 4 · P3 5 · P4 4 · P5 3 · P6 3 (24 total)**; each prior-evidence statement carries its link(s), not only a trailing provenance line.
- **Link resolution:** 19 local links (source-wiki claim anchors `#claim-2942…2947`, `#claim-none`, `#held-out`; `../p1-source-position-ledger.html`; `../p2-claim-status-ledger.html`) — **0 broken/unresolved** (files + anchors verified). 14 external links, **all `https://arxiv.org/abs/<id>` with IDs drawn from the local ledger** (1706.08987, 2512.05584, 0901.1880, 2403.17145, 2009.11175, 2508.06707, 2604.15438, 2605.03008) — well-formed and non-invented; their HTTP-200 status is for Tori/director to confirm with network (not reachable from this docs-only lane).
- **No unsupported prior-evidence sentence remains unlinked:** every statement in each prior-evidence list has ≥1 link; the methods-programme card (P6) links its evidence-accounting statements to the local P1/P2 ledgers and the held-out anchor.
- **Static safety: PASS** — 0 `<script>`/`fetch(`/XMLHttpRequest/WebSocket/inline-handler/`<form>`.
- **Product `<!--claim:` / `<!--cite:` comments: 0.**
- **Formal-tone scan: PASS** — 0 casual/blog phrases; no bare "studies show" (section retitled `Prior evidence and constraints`, statements linked). One earlier scanner hit ("cool") was the scientific term *cool circumgalactic gas* and was reworded to "diffuse (~10^4 K) circumgalactic reservoir" for precision.
- **No invention:** evidence IDs ⊆ the known 36; arXiv IDs ⊆ the ledger set; no fabricated papers/DOIs/results.

## What changed (journal-quality lift)
- Structure per study: `Research question` · `Prior evidence and constraints` (linked) · `Remaining uncertainty` · `Data and measurement plan` (population + denominator/control) · `Analysis and decision criterion` (explicit support/refute rule) · `Limitations` · `Provenance`.
- Prior evidence moved from a trailing provenance footnote to inline, per-statement links to the exact source basis (claim anchor + arXiv record).
- Titles rewritten as formal study aims (e.g., "Quantifying the permanence of AGN-driven gas removal: an escape-versus-recycling census"); casual phrasing removed; abstract-style framing note added.

## Verdict
The Method2 prospectus now reads as a serious research agenda seed with linked prior evidence on every claim, explicit uncertainty, named data-to-measurement plans, and decision criteria. Ready for the director's cross-method rollup and (after director/Tori verification only) any public mirror. This lane performed no public/live-root mirror.

## Safety ledger
- live-root: 0 · public mirror by this lane: 0 · restart: 0 · DB/SQL: 0 · /api/pages / page_versions / publish: 0 · git: 0 · cockpit/global: 0 · cloud/OAuth: 0 · browser: 0 · cron: 0 · P3 binding: 0

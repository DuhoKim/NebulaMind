# Final no-apply rollup — research-topics journal-quality evidence-link pass

Marker: AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z
Author: Hwao-director (pane %107). Written 2026-07-08T11:40Z (20:40 KST).
Basis: three method-team in-place revisions of the `research-topics-from-wiki-20260708T090359Z` **wiki**-derived pages + method receipts + this director's independent read-only verification incl. link resolution.

## Status: COMPLETE

The three research-topic pages were revised to **journal-prospectus quality**: every proposal card now carries a formal prior-evidence section with **visible, resolving evidence links inside the section** (not just a trailing provenance line), formal scientific wording, and rigorous data/analysis plans. No invented links/papers/IDs; static-safe; no product bindings.

## Per-method verification (director-verified, read-only)

Revised in place at `…/galaxy-evolution/<method>/research-topics-from-wiki-20260708T090359Z/` (4 files each).

| Method | proposals | prior-evidence sections | visible evidence links (local-resolve / arXiv / broken) | static-safe | product claim/cite | casual phrasing | HTML bytes / sha256(12) |
|---|---|---|---|---|---|---|---|
| **M1** | 6 | 9 | 5 local + 29 arXiv / **0 broken** | ✅ | 0/0 | 0 | 23,914 / `dc5cc21e51e0` |
| **M2** | 6 | 8 | 13 local + 14 arXiv / **0 broken** | ✅ | 0/0 | 0 | 21,339 / `d8502523e2f2` |
| **M3** | 6 | 8 | 18 local + 0 arXiv (local-only) / **0 broken** | ✅ | 0/0 | 0 | 22,765 / `c4b750eacacb` |

## Key verification — link resolution (the correction's core requirement)
- **Local evidence links: 0 broken** across all three (5/13/18 relative links to source-basis pages / claim anchors / evidence-basis sections all resolve to existing files).
- **arXiv external links resolve:** spot-checked (0901.1880, 1108.0110, 1203.2926, 1301.3092) → all **HTTP 200**. M1/M2 cite arXiv IDs drawn from their local ledgers; M3 is local-only (no external links).
- **No unlinked prior-evidence claims presented as evidence:** the prior-evidence sections carry visible links; unsupported items were narrowed or marked as local-method limitations (per method receipts).

## Static + tone validation
All three HTML: 0 `<script>`/`fetch(`/`onclick`/`<form>`/XHR/WebSocket; product claim/cite comment counts **0/0**; **0 casual/blog phrases** (formal tone); no invented paper titles/DOI/ADS/numeric findings/source IDs. Proposal counts (6/6/6) match the JSON maps.

## Receipts
- M1: `method1/autopilot/RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_M1_20260708T112408Z.md` (+ `GORU_M1_JOURNAL_EVIDENCE_LINK_CHECK_…`)
- M2: `method2/autopilot/RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_M2_20260708T112408Z.md`
- M3: `method3/autopilot/RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_M3_20260708T112408Z.md`

## Live-root / public mirror
Autopilot live-root mirror: **0**. The public pages currently serve the **specificity** version (mirrored earlier) — they are now **stale**; the journal-quality evidence-link revision is working-repo only.

## Exact next action for Tori (user-approval-gated static refresh)
Only on user approval, refresh the three public mirrors to the journal versions (static copy only — no publish/DB/api/page_versions/git/deploy/backend restart):
1. Back up each current live `…/<method>/research-topics-from-wiki-20260708T090359Z/` dir.
2. `cp` the 4 files per method (checksums above) into the matching live-root dirs (`…/NebulaMind-origin-main-live/frontend/public/…`).
3. Verify each public URL returns HTTP 200 with a `Prior evidence` section, ≥1 visible link in it, and the journal marker. The three live dirs already exist and served without a restart previously, so no `:3000` refresh should be needed; if a new path 404s, a frontend-only static refresh is a separate approval.

## Safety ledger
Read-only inspection (incl. read-only arXiv HTTP spot-checks required by the order) + method-team in-place revisions under the 3 `research-topics-from-wiki-20260708T090359Z/` dirs + `.hermes` receipts + this rollup. **Zero** live-root writes/copies by this director, backend/API restart, deploy, product DB/SQL, `/api/pages`, page_versions, live-wiki publish, trust recompute, git, cockpit/global/shared-parent, cloud/OAuth/secrets, browser automation, cron; zero Method3 P3 binding; zero invented data; zero director keystrokes into panes; zero solo content authoring. All hard gates remain closed.

AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z

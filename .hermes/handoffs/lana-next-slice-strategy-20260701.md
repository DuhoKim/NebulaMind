# Lana Handoff — Next-Slice Strategy (2026-07-01)

Ref: BOARD DIRECTIVE COMM-20260701 (t_7b591f52); brief NEXT-SLICE-STRATEGY-20260701.
Author: Lana (Claude Code). Model: cockpit=Hermes (verification only); build=Lana/Goru.
Canonical task/status/comments live in Hermes Kanban; this file is the detailed handoff.

## Ledger — this handoff task
- **Task:** Recommend 1–2 tangible next NebulaMind / Galaxy V2 work slices.
- **Lane:** Lana (strategy + build) + Goru (read-only scan/verify). Hermes = cockpit/verify only.
- **Status:** DONE — read-only analysis; single-file handoff written; no code touched.
- **Summary:** Two safe, visible, DB-free slices proposed. Slice 1 recommended first.
- **Files (read this pass):** `backend/app/routers/pages.py` (`paper-footprint`), `backend/tests/test_cross_page_paper_footprint_api.py`, `backend/tests/test_paper_profile_api.py`, `.hermes/plans/2026-07-01_095115-wiki-papers-route-design.md`, `frontend/src/app/wiki/papers` (absent on this branch).
- **Commands (read-only):** `find frontend/src/app/wiki/papers`; `grep -rn footprint frontend/src`; `grep -nE 'paper-footprint|get_cross_page_paper_footprint' backend/app/routers/pages.py`.
- **Verification:** `paper-footprint` endpoint + tests confirmed present; **no** frontend `footprint` consumer exists; papers route verified 200 in worktree (Kanban t_cffbe238) but not merged to `feat/surveys-atlas-ia-p1`.
- **Blockers:** papers directory/profile route lives in a worktree, not on this branch — Slice 1 builds on it.
- **Next:** Papa picks Slice 1 and/or 2; assign lanes; Hermes verifies.
- **Safety:** no DB, no migration, no deploy/restart, no git write, no OpenClaw relay, no secrets, no other file edits.

## Context snapshot (what's already true)
- Papers directory/profile verified live in a clean worktree (t_cffbe238): `/wiki/papers` 200, `/wiki/papers/arxiv%3A2606.990101` 200; `paper-directory` v1 `total_papers=1482`; Galaxy V2 `citations=138`, `fact-sources=8`. Those `.tsx` files are **not** on this branch yet.
- Backend read-only paper APIs exist + tested (uncommitted): `paper-footprint`, `paper-profile`, `paper-directory`, page source-surface fallbacks.
- `GET /api/pages/paper-footprint?arxiv_id=… | evidence_id=…` already returns everything a UI needs: `paper{arxiv_id,doi,url,title,authors,year,summary}`, `tone_counts{support,counter,neutral}`, `trust_counts{…}`, and `by_page[]{slug,title,claim_count,evidence_count,support_count,counter_count,neutral_count,claims[]{claim_id,claim_text,section,trust_level}}`.
- Standing gate: DB mutation / claim promotion / trust mutation = **explicit-approval only**.

---

## Slice 1 — "Cited across NebulaMind" paper-footprint panel  **(RECOMMENDED)**
Turn the already-built-but-unconsumed `paper-footprint` API into a visible panel on the paper profile page.

- **Lane split**
  - **Goru (read-only):** confirm the `paper-footprint` JSON contract above; confirm the papers-profile client fetch pattern + link formats (`profile_href` = `/wiki/papers/arxiv%3A<id>`, `claim_href` = `/wiki/<slug>#claim-<id>`); confirm which identifier the `[paperId]` page holds so it can key the footprint call (arxiv_id vs evidence_id). Deliver a 1-page contract note; no edits.
  - **Lana (build, in the papers worktree/branch):** add a "Cited across NebulaMind" panel to `/wiki/papers/[paperId]` rendering `by_page` (linked page title → `/wiki/<slug>`, claim/evidence counts, support/counter tone chips) plus a `tone_counts`/`trust_counts` summary; deep-link each claim via `claim_href`. Add a contract smoke test mirroring `frontend/scripts/test-wiki-papers-*.mjs`.
- **Verification:** `/wiki/papers/arxiv%3A2606.990101` renders the panel (HTTP 200, non-empty `by_page` for a paper known to appear on Galaxy V2); contract test asserts `by_page` shape; worktree tests/build green. Hermes records the HTTP checks in Kanban.
- **Public effect:** every one of the **1482** papers becomes a hub showing *where it's cited across the wiki* (which pages, which claims, support vs counter). Links the new papers directory into the claim graph — directly user-visible.
- **Approval boundary:** read-only API consumption only. **No** DB write, promotion, or trust mutation. Merging the papers worktree to `main` and any deploy = **separate** explicit approval.
- **Files (create, in worktree):** `frontend/src/app/wiki/papers/[paperId]/PaperFootprintPanel.tsx` (+ wire into `PaperProfileClient.tsx`); `frontend/scripts/test-wiki-papers-footprint-contract.mjs`.
- **Commands (verify, read-only/build):** `curl -s '/api/pages/paper-footprint?arxiv_id=2606.990101'`; `node frontend/scripts/test-wiki-papers-footprint-contract.mjs`; `npm run build` (in worktree).

## Slice 2 — Papers directory metadata-health audit + filter  **(ALT / data-quality lane, parallelizable)**
Make the 1482-paper directory more trustworthy without touching data.

- **Lane split**
  - **Goru (read-only):** audit `paper-directory` for thin metadata (missing year / authors / title / summary, un-normalized `arxiv:` ids); produce per-defect counts as a `docs/` report artifact (its own approved run — a write). No DB writes.
  - **Lana (build):** add an optional "Needs metadata" filter chip + small data-health badge to the papers directory UI, computed client-side over the existing directory payload (no new endpoint if fields are present; otherwise propose a read-only query param, design-first).
- **Verification:** report artifact with counts; UI filter returns the flagged subset; no writes; tests/build green.
- **Public effect:** cleaner, more credible directory; makes data gaps visible; sets up a later (gated) backfill.
- **Approval boundary:** audit + report + read-only UI filter only. Any metadata backfill / normalization write to DB = **explicit approval** (promotion-gated). Any new backend param is design-first.
- **Files (future):** `docs/papers_directory_metadata_health_20260701.md` (report — gated to an approved run); `frontend/src/app/wiki/papers/DirectoryHealthFilter.tsx`.

---

## Recommendation
Do **Slice 1 first** — it monetizes an already-built + already-tested backend, delivers the biggest visible payoff (papers ↔ claim graph), has a clean Lana/Goru split, and stays fully read-only/frontend. Run **Slice 2** as a parallel data-quality track if a second lane is wanted. Prerequisite for Slice 1: land (or branch from) the papers-route worktree so it isn't building on unmerged files.

_No DB / migration / deploy / git / OpenClaw / secret actions were taken producing this handoff._

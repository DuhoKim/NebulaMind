# Method2 / SFA — Hwao same-format conformance verdict (rebuild)

## VERDICT: ISSUES — same-format conformance PASS on structure / markers / surface; 2 minor NON-BLOCKING issues. Not a BLOCKER.

Packet marker: HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z
Role: Method2 Hwao — same-format **conformance** verdict only (does the rebuilt preview reproduce the canonical
`WikiPageClient` surface: §2A content contract + §2B shell contract + exact marker grammar). This is **not** a
page-preference judgment; preference is out of scope.
Basis: independent re-verification of the content + preview against the §2 contract — not a re-trust of the
Goru/Tori self-reports (which both read PASS but explicitly scoped their boilerplate check to "outside/after
stripping HTML comments," leaving the two items below unadjudicated).
Written UTC: 2026-07-07T07:27:49Z (16:27:49 KST)

## Artifacts verified

- Content: `.../source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md`
- Preview: `.../source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`
- Goru ledger: `method2/SAME_FORMAT_CONFORMANCE_LEDGER_20260707T064500Z.md` (PASS)
- Tori receipt: `method2/receipts/TORI_SAME_FORMAT_REBUILD_RECEIPT_20260707T064500Z.md` (PASS)
- Preservation manifest: `.../same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md`
  (old wrong-format `wiki-page.html`, 28665 bytes, PRESERVED, not overwritten)

## §2A — content contract (conformance PASS, one issue)

| Check | Result |
|---|---|
| Leading `# Galaxy Evolution` (client strips H1; article starts at first `##`) | PASS |
| 9 binding H2s, exact order | PASS (9/9) |
| Claim grammar `<!--claim:ID-->…<!--/claim:ID-->`, open ID list == close ID list | PASS (6 open == 6 close) |
| Claim ID set == {2942, 2943, 2944, 2945, 2946, 2947} | PASS |
| Numeric `<!--cite:ID-->` count | 0 — **correct by design** (local 28xxx unresolved to product cite IDs; per brief) |
| `<!--cite-unmatched:…-->` count | 7 — **correct by design** (the §2A path for unresolved evidence) |
| Evidence IDs inside cite-unmatched == the 22 ratified accepted/limited rows | PASS (exact set) |
| Excluded rows 28133 (F1) / 28111 (F3) leaked | PASS — 0 occurrences |
| Rejected rows (28070/28076/28080/28082/28083/28084/28110/28114/28118/28127/28139/28143) leaked | PASS — 0 occurrences |
| Invented / fabricated cite IDs | PASS — none; every cite-unmatched carries a true 28xxx + true arXiv |
| `hero_facts` / `hero_tagline` | PASS — absent |
| Report/status boilerplate in body (visible) | PASS — none |
| `[n]` tokens / References-Bibliography footer / author-year parentheticals | PASS — none |
| Raw HTML tags/entities in prose (outside comments) | PASS — none |
| Registered-marker-only comments | **ISSUE-1** — 1 UNKNOWN (non-registered) comment present |

**ISSUE-1 (minor, non-blocking) — trailing unregistered HTML-comment ledger in `page.content`.**
Lines 77–88 of the content hold a free-text `<!-- … Unresolved citation ledger … -->` block (packet marker +
per-claim 28xxx→arXiv list). It is not one of the registered markers
(claim / cite / cite-unmatched / EVIDENCE_HIGHLIGHTS / trust-status), so per `docs/wiki_content_contract_v1.md`
it "remains invisible in the frontend renderer, but … [is] not valid stored content," and §2A bars in-body
ledgers ("no … safety ledgers", "no … receipt sections"). It does **not** affect the rendered same-format
surface (it renders to nothing) and it duplicates information already recorded in valid `cite-unmatched`
markers and in Goru's conformance ledger. Disposition: **non-blocking for this docs/static, no-apply preview**;
must be relocated to the Goru ledger (where it already exists) or stripped before any future `page.content`
storage/publish. This is why the verdict token is ISSUES rather than a clean PASS.

## §2B — static preview-shell contract (conformance PASS, one minor deviation)

| Element (canonical WikiPageClient surface) | Result |
|---|---|
| Two-column article grid: content column + sticky TOC rail | PASS (structural mirror present) |
| Contents/TOC rail built from headings; all 9 headings present | PASS |
| Header `<h1>` title + `slug: galaxy-evolution` | PASS |
| Provenance chip | PASS |
| Trust-summary placeholder (method has claims) | PASS |
| Reader/Evidence controls (static visual state) | PASS |
| History / Sources rendered preview-only (not live-functional) | PASS ("Preview-only History", "Preview-only Sources") |
| Method label lives in shell chrome, outside the article prose | PASS |
| Packet marker present in content + preview | PASS |
| Exact grid metrics | **ISSUE-2** — `minmax(0, 1fr) 17rem` vs canonical `minmax(0, 56rem) 240px` (maxWidth 64rem, gap 2rem) |

**ISSUE-2 (minor, non-blocking) — article-grid metrics differ from the §2B canonical values.**
The shell renders a structurally faithful content-column + right TOC-rail two-column layout, but with
`grid-template-columns: minmax(0, 1fr) 17rem` rather than the §2B-named `minmax(0, 56rem) 240px` inside
`maxWidth: 64rem`, `gap: 2rem`. §2B frames the shell as "a static HTML approximation … enough to eyeball it
next to the real page," so the two-column structure being present satisfies the mirror intent; the exact
column widths are an approximation deviation, not a structural nonconformance. Disposition: **non-blocking**;
tighten to the canonical metrics if a pixel-faithful side-by-side is wanted later.

## Method-separation & preservation (PASS)

- Chips are Method2's own {2942–2947} only; **no Method1 chips 2905–2936**, no Method3 binding — no cross-method leakage.
- Source-first discipline intact: every highlighted claim maps only to accepted/accepted-limited source
  positions; excluded (28133/28111) and all 12 rejected rows stay out of the body.
- Old wrong-format `wiki-page.html` preserved (not overwritten); new artifacts are additive under
  `same-format-rebuild/`. Method-local separation preserved.

## Scope / locks honored (this verdict pass)

Verdict-only. No content or shell edits; no live-wiki/`page_versions` publish; no DB/`/api/pages` write;
no deploy/restart; no git; no cockpit/global/shared-parent write; no cloud/GCP/Gemini/API/billing/OAuth/token;
no browser; no cron; no route/config. Docs/static, no-apply. The publish gate stays closed; this conformance
verdict does not open it.

## Bottom line

The Method2 rebuilt same-format preview **conforms** to the canonical `/wiki/[slug]` surface on every structural,
marker-grammar, and shell-element dimension, with the 0-numeric-cite / 7-cite-unmatched profile correct by
design. Two minor, non-blocking cleanliness items remain (ISSUE-1 unregistered in-body comment ledger;
ISSUE-2 grid-metric approximation), neither of which blocks the docs/static preview — both are pre-publish
tidy-ups. Verdict: **ISSUES (PASS-with-issues), not BLOCKER.**

## Files read

- `.hermes/handoffs/galaxy-evolution/method2/HWAO_SAME_FORMAT_VERDICT_BRIEF_20260707T064500Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z.md`
- `.../source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md`
- `.../source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`
- `.hermes/handoffs/galaxy-evolution/method2/SAME_FORMAT_CONFORMANCE_LEDGER_20260707T064500Z.md`
- `.hermes/handoffs/galaxy-evolution/method2/receipts/TORI_SAME_FORMAT_REBUILD_RECEIPT_20260707T064500Z.md`
- `.../source-first-paper-adjudication/same-format-rebuild/PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md`

## Files written

- `.hermes/handoffs/galaxy-evolution/method2/HWAO_SAME_FORMAT_REBUILD_VERDICT_20260707T064500Z.md`

## Safety ledger

- content/shell edits: 0
- DB / `/api/pages` / page_versions / live-wiki publish: 0
- deploy / restart / service mutation: 0
- git commit / push / merge: 0
- cockpit / global / shared-parent write: 0
- cloud / GCP / Gemini API / billing / OAuth / token: 0
- browser automation / cron / route-config: 0
- cross-method write: 0
- files written this pass: 1 (this verdict)

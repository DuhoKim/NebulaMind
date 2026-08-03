# Hwao-director same-format rebuild packet — method pages must match the NebulaMind /wiki/[slug] format

Packet marker: HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z
Brief followed: HWAO_SAME_FORMAT_CORRECTION_BRIEF_20260707T064500Z
Author: Hwao-director (pane %107). Written: 2026-07-07T06:16Z (15:16 KST).
Class: DOCS / STATIC / NO-APPLY PREVIEW. Correction supersedes the prior comparison-only direction.

---

## 1. Why this packet (user correction)

The user is right: the three current method outputs at `.../wiki-method-results/galaxy-evolution/<method>/wiki-page.html` are **standalone report/status HTML**, not NebulaMind `/wiki/[slug]`-format pages. The prior comparison lane (Goru/Kun/Lana receipts) is retained **only as evidence that the artifacts are wrong-format** — not as approval to keep evaluating them as final pages.

**Target:** for each method, a NebulaMind wiki-format *preview* — same data shape, section style, and reader surface as `/wiki/galaxy-evolution` — with method-local separation preserved. This is **not** "make the report HTML prettier." No product/DB/live/publish gate is approved; everything here is docs/static, no-apply.

## 2. Canonical format contract (the conformance target)

Distilled from the live renderer `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` (+ `page.tsx` fetch of `/api/pages/{slug}`). All lanes conform to THIS, verified against the source file, not against the old report pages.

### 2A. `page.content` Markdown contract (the article body)
The body is Markdown fed to `ReactMarkdown` (WikiPageClient ~1123–1199). Requirements:
- **Body-only article prose. No report/status boilerplate** in the content (no "Method N wiki page", no provenance/status/receipt sections, no safety ledgers). The method label lives in the shell chrome, never in `page.content`.
- **Leading H1 is stripped** by the client (`stripLeadingH1`, lines 136–138) — the title is `page.title`, not the body H1. Content may open with `# Galaxy Evolution` (it will be stripped); the visible article starts at the first `##`.
- **Headings:** `#`/`##`/`###` only; TOC is built from them (`extractHeadings`, lines 175–190). Match the canonical section/heading style — the 9 binding H2s in order, `**bold**` stripped from TOC text.
- **Marker grammar (exact, per `renderWikiMarkers` lines 141–173):**
  - Claim: `<!--claim:ID-->…<!--/claim:ID-->` — **open ID list must equal close ID list** or the marker renders literally (bug-visible). Comma-lists allowed.
  - Cite: `<!--cite:NUMERIC-->` — numeric evidence IDs only, comma-list allowed.
  - **Unresolved evidence → `<!--cite-unmatched:TEXT-->`** (lines 153–155) and **ledger it** — do NOT invent a numeric ID to force a `cite:`. This is the required path for any Method2 evidence ID that does not resolve to a real product cite ID.
- **No `hero_facts`** and **no `hero_tagline`** unless the user separately approves them (fallback-header path is fine, §2B).
- Contract-clean (unchanged from prior method contracts): no raw HTML tags/entities in prose, math only in `$…$`/`$$…$$`, no `[n]` reference tokens, no References/Bibliography footer, no author-year parentheticals.
- **No broad/unsupported evidence-hunting.** Rebuild works from each method's already-verified draft; it does not go find new sources.

### 2B. Static preview-shell contract (layout mimicry for side-by-side review)
The shell is a static HTML approximation of the `/wiki/[slug]` surface — enough for the user to eyeball it next to the real page. Mirror, as static markup:
- **Article grid:** content column + sticky TOC rail — `gridTemplateColumns: minmax(0, 56rem) 240px`, `maxWidth: 64rem`, `gap: 2rem` (desktop); single column `maxWidth: 56rem` (mobile) (lines 903–917).
- **Header:** title from a `title` field (fallback header path, lines 1012–1024: `<h1>{title}</h1>` + `slug: galaxy-evolution` + ProvenanceChip). Optional tagline section only if hero is approved (lines 956–1010) — default OFF.
- **Provenance chip** after the header (lines 1017–1033) — preview-only values.
- **Trust summary panel** placeholder if the method has claims (lines 1035–1037) — static/preview state.
- **Contents rail** (`TOCSidebar`) built from the content headings (lines 903–917 rail; mobile accordion 1040–1042).
- **Reader/Evidence controls** rendered in a static visual state (Reader/Evidence toggle, Reduce highlights, citation-chip toggle, research-questions toggle) (lines 1044–1121) — visual only; no live behavior required.
- **History / Sources links** (`/wiki/{slug}/history`, `/wiki/{slug}/sources`, lines 944–953) rendered **disabled or clearly marked preview-only** — they must not point at live routes as if functional.
- **Galaxy method-result buttons** (shown for `galaxy-evolution`, line 919) may appear in the shell chrome.
- **Method label lives in the shell chrome, outside the article prose** — it must not replace or intrude on the wiki content.

## 3. Inputs per method (rebuild from the already-verified same-format draft; do not re-derive science)

| Method | Source draft = rebuild input | Marker profile (expected) | Wrong-format page to PRESERVE |
|---|---|---|---|
| M1 packet-gated | `…/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md` | 30 claim chips {2905–2923,2925,2926,2929–2936,2946}; 0 cites | `…/packet-gated-paper-to-wiki-reconciliation/wiki-page.html` |
| M2 source-first | `…/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md` | 6 claim chips {2942–2947}; numeric cites over 28xxx evidence IDs — **resolvability MUST be checked** | `…/source-first-paper-adjudication/wiki-page.html` |
| M3 debate-map | `…/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-20260707T050500Z.md` | docs-only: **0 claim markers, 0 cite markers** (P2 scope) | `…/debate-map-to-wiki-rebuild/wiki-page.html` |

Method verdict anchors (for lineage; read-only): `method1/HWAO_PGR_METHOD_VERDICT_20260707T040523Z.md`, `method2/hwao/HWAO_M2_METHOD_VERDICT_V2_20260707T043503Z.md`, `method3/HWAO_M3_P2_WIKI_PAGE_VERDICT_RERUN_20260707T050900Z.md`.

**Per-method conformance risk to resolve explicitly:**
- **M2 cite IDs:** the 28xxx are the method's source-adjudication evidence IDs. Each must be resolved against real product cite IDs. Resolved → `<!--cite:ID-->`; unresolved → `<!--cite-unmatched:…-->` + ledger entry. **No invented IDs.** (Do not hit the DB/API to resolve — use the method's existing local evidence ledger; anything not locally resolvable is `cite-unmatched`.)
- **M3:** zero markers is correct for its scope — its page legitimately has no trust badges/citations. Do not add markers to "match" M1/M2.
- **M1:** already canonical-marker Markdown; the rebuild is mostly boilerplate-strip + shell, verify 30 open==close claim pairs.

## 4. Lane split (method-local teams do the rebuild; standalone Goru/Antigravity = conformance checks only)

For **each** method N∈{1,2,3}, the method-local quintet runs this chain (own handoff root + own public workspace only):

- **Lana (method-local) — content owner.** Produce the same-format `page.content` Markdown (§2A) from method N's source draft: strip all report/status boilerplate, conform headings + marker grammar to canonical, resolve/ledger cite IDs (real vs `cite-unmatched`), no hero fields, no invented IDs, no evidence-hunting. Deliverable = the `page-content` MD (§5).
- **Kun (method-local) — shell builder.** Build the static preview shell (§2B) around Lana's `page.content`, mimicking the WikiPageClient surface (grid + TOC rail + header + provenance + trust placeholder + Reader/Evidence static controls + preview-only history/sources + method label in chrome). Deterministic/reproducible from the content + the WikiPageClient reference. Deliverable = the `wiki-format-preview` HTML (§5).
- **Goru (method-local) — mechanical conformance.** Field-by-field conformance ledger of Lana's content + Kun's shell against the §2 checklist: H2 count + exact order, claim markers (open==close) + ID set, cite/cite-unmatched counts + IDs, TOC-heading extraction parity, boilerplate scan (must be zero in body), grid/rail/header/controls/links presence in the shell. Counts + pass/fail only. Deliverable = the conformance ledger (§5).
- **Tori (method-local) — receipts-last + preservation.** Verify the three lane files exist and match; **preserve the old wrong-format `wiki-page.html` as a historical artifact** — do NOT overwrite it; record it in a preservation manifest (path, bytes, mtime, "superseded-by" pointer to the new preview). New artifacts go in a **new `same-format-rebuild/` subdir** so nothing is overwritten. Deliverable = receipts + preservation manifest (§5).
- **Hwao (method-local) — verdict.** Per-method **same-format conformance** verdict (PASS/ISSUES/BLOCKER) — strictly "does the rebuilt preview conform to the canonical surface + marker grammar," **not** page preference. Deliverable = method verdict (§5).

**Standalone Goru/Antigravity — independent mechanical conformance cross-check (checks only, no rebuild).** After the three method previews exist, run one read-only cross-method mechanical conformance pass against the §2 checklist and flag any deviation the method-local Goru lanes missed. It may NOT author content or shells. Deliverable = the cross-check ledger (§5).

**Hwao-director — final cross-method conformance verdict.** Aggregate the three method verdicts + the standalone cross-check into one same-format conformance verdict. Conformance only, not preference. Deliverable = director verdict (§5).

Any lane hitting a missing input, an unresolved-that-should-resolve ID, or a lock conflict → write `ROLE_TABLE_BLOCKER` and stop.

## 5. Exact expected deliverable filenames

New artifacts live in a **new per-method `same-format-rebuild/` subdir** (never overwriting the old page). Reports carry marker `HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z` + a safety ledger.

Per method N, under `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/<method-dir>/same-format-rebuild/`:
- `page-content-20260707T064500Z.md`  (Lana — canonical `page.content`)
- `wiki-format-preview-20260707T064500Z.html`  (Kun — static preview shell)
- `PRESERVED_WRONG_FORMAT_MANIFEST_20260707T064500Z.md`  (Tori — old page preserved, not overwritten)

Per method N, under `.hermes/handoffs/galaxy-evolution/method<N>/`:
- `SAME_FORMAT_CONFORMANCE_LEDGER_20260707T064500Z.md`  (method-local Goru)
- `receipts/TORI_SAME_FORMAT_REBUILD_RECEIPT_20260707T064500Z.md`  (Tori)
- `HWAO_SAME_FORMAT_REBUILD_VERDICT_<UTC>.md`  (method-local Hwao — conformance verdict)

Cross-method, under `.hermes/handoffs/galaxy-evolution/mastermind/`:
- `GORU_SAME_FORMAT_CONFORMANCE_CROSSCHECK_20260707T064500Z.md`  (standalone Goru/Antigravity — checks only)
- `HWAO_DIRECTOR_SAME_FORMAT_CONFORMANCE_VERDICT_<UTC>.md`  (director final conformance verdict)

`<method-dir>` = `packet-gated-paper-to-wiki-reconciliation` (M1) · `source-first-paper-adjudication` (M2) · `debate-map-to-wiki-rebuild` (M3).

## 6. Preservation + separation rules
- **Do not overwrite** any existing `wiki-page.html`, `index.html`, `manifest.json`, draft, or method-tree file. All new output is additive under `same-format-rebuild/`.
- Each method's Tori records the old wrong-format page in its preservation manifest before the new preview is considered live-for-review.
- **Method-local separation preserved:** no method writes into another method's tree; no shared-parent/cockpit write. Standalone Goru/Antigravity writes only its one cross-check file under mastermind.

## 7. Explicit locks (all lanes, non-negotiable)
No DB writes · no `/api/pages` update · no `page_versions` publish · no live-wiki publish · no deploy/restart/service mutation · no git commit/push/merge · no cockpit/global update · no shared-method overwrite · no `hero_facts`/`hero_tagline` unless separately user-approved · no invented evidence/cite IDs · no broad evidence-hunting · no browser automation · no cron · no route/config mutation · no Gemini/GCP API/config/billing/cloud-account/OAuth/token action. **Docs/static preview only. No-apply.** Publication of any preview to the real wiki remains a separate future user gate.

## 8. What the Hwao verdict means
The required final verdict (method-local and director) is about **same-format conformance** — does each rebuilt preview reproduce the canonical `WikiPageClient` surface (§2A content contract + §2B shell contract + exact marker grammar)? It is **not** a judgment of which method's page reads best. Preference is out of scope; conformance is the gate.

## 9. Dispatch note
This is user-directed corrective work, docs/static, no-apply — Tori may dispatch the method-local rebuild lanes now (M1/M2/M3 in parallel; per method Lana→Kun→Goru→Tori→method-Hwao; standalone Goru/Antigravity cross-check after the three previews exist; director verdict last). The product/DB/live/publish gate stays closed and unapproved; the final conformance verdict does not open it. Hwao-director dispatched no panes and made no mutation beyond writing this packet.

HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z

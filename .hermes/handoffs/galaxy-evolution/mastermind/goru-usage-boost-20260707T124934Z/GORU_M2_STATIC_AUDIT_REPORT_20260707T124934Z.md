# Goru M2 Static Audit Report

`GORU_M2_STATIC_AUDIT_REPORT_DONE_20260707T124934Z`

**Status:** PASS

## 1. Latest Same-Format Rebuild Preview
- **Path:** `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`

## 2. Raw Article H2 Headings
- **Count:** 9 `<h2>` tags.
- **Match:** This matches the Hwao cleanup expectation of exactly 9 article `<h2>` headings.

## 3. TOC Rail Label
- **Status:** PASS
- **Details:** The TOC rail label is `<h3>Contents</h3>`, not an extra `<h2>`.

## 4. Reader/Evidence Controls
- **Status:** PASS
- **Details:** Controls are present. Exact strings used:
  - Top controls: `<strong>Reader</strong> On`, `<strong>Evidence</strong> Static`, `History`, `Sources`.
  - Article controls: `Reader`, `Evidence`, `Preview-only History`, `Preview-only Sources`.

## 5. Old Wrong-Format Page
- **Status:** PASS
- **Path:** `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html`
- **Details:** The old wrong-format page is preserved (size: 28,665 bytes) and was not overwritten.

## 6. Safety Boundary Confirmation
- **Status:** PASS
- **Details:** Inspected files are strictly local static HTML/markdown artifacts. No evidence of live wiki publish artifacts, `/api/pages` calls, `page_versions` writes, git actions, deploy/restarts, or public cockpit edits were found.

`TORI_GORU_DISPATCH_DONE_20260707T125210Z`

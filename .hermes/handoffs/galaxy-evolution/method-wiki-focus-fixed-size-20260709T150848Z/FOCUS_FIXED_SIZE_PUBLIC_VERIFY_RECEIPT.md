# Method selector focus + fixed-size public verification receipt

- checked_utc: `2026-07-09T15:16:47.539269+00:00`
- user correction: default `/wiki/galaxy-evolution` represents the first method, so the first selector card should be focused; method selector card size should not change between default and method pages.

## Dynamic default page

URL checked in browser before the final static width/height-only adjustments:
`https://nebulamind.net/wiki/galaxy-evolution?verify=focus-fixed-size-20260709T1512`

Browser DOM result:

- selector width: 704px
- only first selector card focused: true
- first card `data-current-method="true"`: true
- first card `aria-current="page"`: true
- card widths: 219px / 219px / 219px
- card heights: 74px / 74px / 74px
- tabs present: true
- snapshot/deck/atlas absent: true

## Static method pages

All three public static method pages were checked with cache-busting URLs after final copy:

1. `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html`
2. `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html`
3. `/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html`

Public HTTP/source checks for each page:

- HTTP status: 200
- top main NebulaMind header present: true
- selector is inside the same wiki-main column as the default page: true
- selector shell capped to default measured grid width: `max-width:976px`
- selector card min-height fixed to default measured card height: `min-height:74px`
- no extra `CURRENT METHOD` badge/content: true
- exactly one focused/current selector card: true
- current page card has `aria-current="page"` and `data-current-method="true"`: true
- selector links: 3
- top wiki tabs present: `Raw Text`, `Colors On`, `Hide Citations`, `Show Ideas`
- snapshot/deck/atlas absent: true
- `NO ACTIVE EXECUTION PHRASE`: present
- `APPROVE EXECUTE`: absent
- `APPROVE APPLY`: absent

Browser note: after the final static-only min-height copy, the browser automation backend returned `CDP WebSocket connect failed: HTTP error: 502 Bad Gateway` on repeated attempts. I therefore used the successful browser measurements from the immediately preceding page states plus final public HTTP/source checks showing the exact CSS/markup now served.

## Build / checks

- `npx tsc --noEmit --pretty false` in working frontend: pass
- `npx tsc --noEmit --pretty false` in live frontend root: pass
- `npm run build` in live frontend root: pass
- live frontend process refreshed; new listener observed as Next server under `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend`

## Changed paths

Dynamic wiki client:

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/wiki/[slug]/WikiPageClient.tsx`

Static method pages:

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/wiki-page.html`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/wiki-page.html`

Supporting receipts in this directory:

- `FOCUS_FIXED_SIZE_RENDER_RECEIPT.md`
- `FOCUS_FIXED_SIZE_LIVE_COPY_RECEIPT.md`
- `SELECTOR_COLUMN_ALIGN_RECEIPT.md`
- `SELECTOR_COLUMN_ALIGN_LIVE_COPY_RECEIPT.md`
- `WIDTH_MATCH_DEFAULT_RENDER_RECEIPT.md`
- `WIDTH_MATCH_DEFAULT_LIVE_COPY_RECEIPT.md`
- `CARD_HEIGHT_MATCH_RENDER_RECEIPT.md`
- `CARD_HEIGHT_MATCH_LIVE_COPY_RECEIPT.json`

## Safety ledger

- DB/page_versions writes: 0
- live product wiki publish: 0
- backend/API restart: 0
- trust recompute: 0
- deploy: 0
- git commit/push/merge: 0
- frontend build: 1
- frontend runtime refresh: 1
- static method file rewrites: 3
- live static mirror copies: 3

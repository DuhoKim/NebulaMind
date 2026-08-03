# Public header + active method selector verification receipt

- checked_utc: `2026-07-09T15:03:40.910919+00:00`
- user correction: the top main NebulaMind header should not disappear, and the current method's selector box should be focused/highlighted.
- scope: three static Galaxy Evolution method `wiki-page.html` artifacts.

## Public HTTP verification

Checked all three public URLs with cache-busting query string:

1. `/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html`
2. `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html`
3. `/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html`

For each page:

- HTTP status: 200
- marker present: `NEBULAMIND_METHOD_WIKI_HEADER_ACTIVE_SELECTOR_20260709T150300Z`
- top main NebulaMind header present: true
- brand/nav present: NebulaMind, Wiki, Surveys, Research Topics, News, Council, Agents, More, Join
- method result selector present: true
- selector link count: 3
- current method card marked: `aria-current="page"`, `data-current-method="true"`, class `is-current`
- exactly one current method card: true
- visible `CURRENT METHOD` badge count: 1
- top wiki tabs present: `Raw Text`, `Colors On`, `Hide Citations`, `Show Ideas`
- article H1 present: `Galaxy Evolution`
- `Page trust snapshot`: absent
- `Paper-to-claim flight deck`: absent
- `Page-level contradiction atlas`: absent
- `NO ACTIVE EXECUTION PHRASE`: present
- `APPROVE EXECUTE`: absent
- `APPROVE APPLY`: absent

## Browser DOM verification

Browser checked Method 2 public page:
`https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html?verify=header-active-20260709T1503`

DOM result:

- header present: true
- brand text: `NebulaMind`
- nav text: `Wiki / Surveys / Research Topics / News / Council / Agents / More / Join`
- selector present: true
- selector links: 3
- current card text: `2 · Source-first adjudication ... CURRENT METHOD`
- current card href: `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html`
- current card class: `is-current`
- current card data: `data-current-method="true"`
- tabs present: true
- snapshot/deck/atlas absent: true

## Render/copy receipts

- render receipt: `.hermes/handoffs/galaxy-evolution/method-wiki-header-active-20260709T150300Z/HEADER_ACTIVE_RENDER_RECEIPT.md`
- live copy receipt: `.hermes/handoffs/galaxy-evolution/method-wiki-header-active-20260709T150300Z/HEADER_ACTIVE_LIVE_COPY_RECEIPT.md`

## Safety ledger

- DB/page_versions writes: 0
- live product wiki publish: 0
- backend/API restart: 0
- trust recompute: 0
- deploy: 0
- git commit/push/merge: 0
- static method file rewrite: 3
- live static mirror copy: 3

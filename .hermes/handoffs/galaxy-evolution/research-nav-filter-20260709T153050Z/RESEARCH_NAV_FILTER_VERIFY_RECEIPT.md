# Research nav label + Galaxy Evolution filter receipt

- checked_utc: `2026-07-09T15:30:50Z`
- user correction: top nav should say `Research`, not `Research Topics`; Research page should focus only on Galaxy Evolution for now.

## Changes

Dynamic frontend source:

- `frontend/src/app/components/NavBar.tsx`
  - changed top nav label from `Research Topics` to `Research`.
- `frontend/src/app/ideas/page.tsx`
  - changed metadata title/description to Galaxy Evolution Research.
- `frontend/src/app/ideas/IdeasIndexClient.tsx`
  - added focused slug `galaxy-evolution`.
  - filters `/api/pages?limit=200` to only the Galaxy Evolution page before fetching ideas.
  - fetches `/api/pages/galaxy-evolution/ideas?per_page=200`.
  - heading now shows `Galaxy Evolution Research`.
  - count now shows `N of N Galaxy Evolution ideas`.
  - search placeholder now says `Search Galaxy Evolution ideas`.

Live frontend root patched with the same changes:

- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/components/NavBar.tsx`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/ideas/page.tsx`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/ideas/IdeasIndexClient.tsx`

Static method pages patched in working and live public roots:

- `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/wiki-page.html`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/wiki-page.html`

Each static header nav now has:

```html
<a href="/ideas">Research</a>
```

and no `Research Topics` label.

## Checks

Type/build:

- `npx tsc --noEmit --pretty false` in working frontend: pass
- `npx tsc --noEmit --pretty false` in live frontend root: pass
- `npm run build` in live frontend root: pass

Public/live verification:

- `/ideas` static HTML status: 200
- `/ideas` title contains `Galaxy Evolution Research`: true
- `/ideas` old `Research Ideas` title absent: true
- `/ideas` old `Research Topics` label absent: true
- `/api/pages?limit=200` returns 44 pages, but client filter keeps exactly 1 page:
  - `slug`: `galaxy-evolution`
  - `title`: `Galaxy Evolution`
- `/api/pages/galaxy-evolution/ideas?per_page=200`:
  - status: 200
  - total: 29
  - returned: 29
  - all returned idea page slugs: `galaxy-evolution`
- Static method page sample:
  - `<a href="/ideas">Research</a>` present: true
  - `Research Topics` absent: true

Browser-level verification via Python Playwright:

- URL: `https://nebulamind.net/ideas?verify=playwright-research-final-20260710`
- page title: `Galaxy Evolution Research — NebulaMind`
- nav has `Research`: true
- `Research Topics` absent: true
- `Galaxy Evolution Research` heading present: true
- non-Galaxy examples absent:
  - `Cosmic Inflation`: false
  - `Hubble Constant`: false
- article count: 29
- count line: `29 of 29 Galaxy Evolution ideas`

Note: the Browserbase browser tool returned CDP 502 during final verification, so I used local Python Playwright for browser-level DOM verification instead.

## Runtime refresh

- User approved a frontend-only restart of the live Next.js process on port 3000.
- Port 3000 currently has a live `next-server (v14.2.35)` listener under `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend`.

## Safety ledger

- DB/page_versions writes: 0
- product wiki/prose publish: 0
- trust recompute: 0
- backend/API restart: 0
- cloud/API/billing actions: 0
- deploy: 0
- git commit/push/merge: 0
- frontend build: 1
- user-approved frontend-only runtime restart: 1

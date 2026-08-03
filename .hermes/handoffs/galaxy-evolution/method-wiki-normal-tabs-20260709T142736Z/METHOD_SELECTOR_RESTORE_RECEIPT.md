# Galaxy wiki method selector restore receipt

- verified_utc: `2026-07-09T14:50:02Z`
- user correction: the card that lets readers select the three methods should remain.
- action: restored a compact single method selector card on `/wiki/galaxy-evolution` while keeping the snapshot/deck/atlas audit panels hidden.

## Source changes

Patched both source roots:

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/wiki/[slug]/WikiPageClient.tsx`

Selector details:

- `data-testid="galaxy-method-result-selector"`
- three links use `data-testid="galaxy-method-result-link"`
- links point directly to each assembled method `wiki-page.html`:
  - packet-gated paper-to-wiki reconciliation
  - source-first paper adjudication
  - debate-map-to-wiki rebuild

## Validation commands

- `npx tsc --noEmit --pretty false` in working frontend: pass
- `npx tsc --noEmit --pretty false` in live frontend root: pass
- `npm run build` in live frontend root: pass

## Live refresh

- live root rebuilt: `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend`
- frontend Next process on port 3000 refreshed by the existing supervisor/launcher
- active listener after refresh:
  - parent: `30181`
  - child: `30182`
  - command: `cd /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend && /opt/homebrew/bin/node node_modules/.bin/next start -p 3000`

## Browser DOM verification

Public URL checked without cache-busting:
`https://nebulamind.net/wiki/galaxy-evolution`

Browser DOM result:

- method selector present: true
- selector link count: 3
- normal wiki tabs present: true
- `Page trust snapshot`: absent
- `Paper-to-claim flight deck`: absent
- `Page-level contradiction atlas`: absent

## Safety ledger

- DB/page_versions writes: 0
- live product wiki content publish: 0
- backend/API restart: 0
- trust recompute: 0
- migrations: 0
- deploy: 0
- git commit/push/merge: 0
- frontend build: 1
- frontend runtime refresh: 1

## Procedural fix

Updated the `public-operator-cockpits` reference `galaxy-method-wiki-same-format-card-retention.md` so future cleanup distinguishes the compact method selector from dashboard/audit clutter.

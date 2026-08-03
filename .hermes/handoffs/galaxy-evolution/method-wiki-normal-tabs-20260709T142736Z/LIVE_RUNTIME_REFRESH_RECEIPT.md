# Galaxy wiki top-card live cleanup receipt

- verified_utc: `2026-07-09T14:39:56Z`
- user issue: public `/wiki/galaxy-evolution` still showed top cards after source/static patch.
- cause: live Next runtime was still serving the previously compiled `.next` bundle.
- source fix already present: `showTopAuditPanels = slug !== "galaxy-evolution"` and the three method-result link panel removed from the wiki client.
- live refresh performed: frontend-only `npm run build` in `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend`, followed by frontend Next process refresh on port 3000.
- active frontend process after refresh: parent PID `27255`, child `27256`, command `cd /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend && /opt/homebrew/bin/node node_modules/.bin/next start -p 3000`.

## Browser verification

Public URL checked with cache-bust:
`https://nebulamind.net/wiki/galaxy-evolution?verify=20260709Tlivefix1`

Browser DOM result:

- `Three paper-to-wiki result lanes`: absent
- `Page trust snapshot`: absent
- `Paper-to-claim flight deck`: absent
- `Page-level contradiction atlas`: absent
- normal wiki tabs present: `Raw Text`, `Colors On`, `Hide Citations`, `Show Ideas`

## Static method pages rechecked

All three public method pages returned HTTP 200, retained the marker `NEBULAMIND_METHOD_WIKI_NORMAL_TABS_NO_TOP_CLUTTER_20260709T142736Z`, kept normal wiki tabs, and had snapshot/deck/atlas clutter absent above the article.

## Safety ledger

- DB/page_versions writes: 0
- live product wiki content publish: 0
- trust recompute: 0
- backend/API restart: 0
- migrations: 0
- git commit/push/merge: 0
- frontend build: 1
- frontend Next runtime refresh: 1

## Notes

A first refresh attempt saw `EADDRINUSE` because a replacement `next start` listener was already present by the time the tracked Hermes background command tried to bind port 3000. Follow-up process inspection confirmed the active listener is the intended live frontend root, and browser verification confirmed the public DOM is clean.

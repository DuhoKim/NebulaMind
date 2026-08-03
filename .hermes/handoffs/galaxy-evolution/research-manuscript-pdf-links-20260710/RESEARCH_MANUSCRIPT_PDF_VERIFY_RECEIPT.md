# Galaxy Evolution Research manuscript PDF link receipt

checked_utc: 2026-07-10T00:00Z
surface: https://nebulamind.net/ideas

What changed
- Added a `Manuscript PDFs` section near the top of the Galaxy Evolution Research page.
- Linked 9 public manuscript PDFs:
  - Method 1 — Environment quenching
  - Method 1 — Maintenance heating
  - Method 2 — Outflow escape/recycling
  - Method 2 — Radio-jet environment
  - Method 2 — Feedback transition mass
  - Method 3 — Multiphase census
  - Method 3 — Gas depletion efficiency
  - Method 3 — Simulation validation
  - Shared pilot — SDSS AGN/SFR pilot

Changed paths
- frontend/src/app/ideas/IdeasIndexClient.tsx
- /Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/ideas/IdeasIndexClient.tsx

Verification
- `npx tsc --noEmit --pretty false` passed in the working frontend.
- `npx tsc --noEmit --pretty false` passed in the live frontend root.
- `npm run build` passed in the live frontend root.
- User approved a frontend-only restart on port 3000.
- Browser DOM verification on https://nebulamind.net/ideas:
  - title: `Galaxy Evolution Research — NebulaMind`
  - top nav includes `Research`
  - old `Research Topics` label absent
  - manuscript PDF region present
  - PDF link count: 9
  - article count after client fetch: 29
  - count line: `29 of 29 Galaxy Evolution ideas`
  - `Cosmic Inflation` absent
- API verification:
  - `/api/pages/galaxy-evolution/ideas?per_page=200` returned total 29 and 29 ideas.
- PDF verification:
  - all 9 linked PDFs responded with HTTP 206, `application/pdf`, and `%PDF-` header bytes.

Safety ledger
- DB writes: 0
- product wiki/prose publish: 0
- trust recompute: 0
- backend/API restart: 0
- frontend-only restart: 1, user approved
- git commit/push/merge: 0
- external manuscript submission: 0

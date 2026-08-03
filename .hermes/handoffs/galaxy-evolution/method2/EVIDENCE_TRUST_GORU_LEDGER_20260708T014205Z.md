# Method2 Goru — evidence-trust candidate mechanical ledger

Marker: AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z
Role: Method2 Goru — mechanical counts + static-safety + no-invention checks (read-only over generated candidate).
Run UTC: 2026-07-08T01:52:00Z
Target dir: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/`

## Overall: PASS

## A. Files present + non-empty (sha256)
| file | bytes | sha256 |
|---|---|---|
| `page-content-20260708T014205Z.md` | 14073 | `52cf8bfb422df8096da866a9144bcfa2d546fb42003e02e5630d22f6da255407` |
| `wiki-format-preview-20260708T014205Z.html` | 13531 | `6b106e5eb67798f5460a4a233eda933d0a7924883993ded8cc8ce5bc387fce92` |
| `evidence-trust-map-20260708T014205Z.json` | 7499 | `c9848105c1a279a1a888cb003844f9d5b16d39bbd534793b95218a4f6003f7df` |
| `manifest.json` | 978 | `7cf79edc6d21eb81ac57125b9518babe8883e57ee4ca9a448f1d1b3a95bde36c` |

## B. Content — same-format preserved + evidence links added
- 9 H2 exact: PASS · 6 claim chips {2942–2947} open==close: PASS · numeric cite: 0 · cite-unmatched: 7 (preserved).
- Evidence IDs in content == the 22 accepted/limited set: PASS · excluded/rejected leak: 0.
- Per-claim evidence links added: **7** relative markdown links, all to local `../p1-source-position-ledger.html`.
- Trust note blockquote present: PASS.

## C. Preview — evidence links + trust leveling visible
- hrefs total: **23**, all evidence-ish (local ledger); distinct targets: `../p1-source-position-ledger.html`, `../p2-claim-status-ledger.html` (2 local artifacts, both exist).
- Trust chips: **2 ACCEPTED**, **19 LIMITED** (per-badge). Evidence badges: 35 (22 supporting + 2 excluded + 11 rejected shown; all 12 rejected + both excluded listed in the held-out panel).
- Per-page trust summary panel: PASS · per-claim evidence/trust table: PASS · held-out (excluded+rejected) panel: PASS.
- Trust vocabulary = source-first status only {ACCEPTED, ACCEPTED-LIMITED, EXCLUDED, REJECTED}; labeled "not product DB trust".

## D. Static-safety scan (candidate must be inert)
- content: CLEAN · preview: CLEAN.
- 0 `<script>`, 0 `fetch(`, 0 XMLHttpRequest, 0 WebSocket, 0 `on*=` handlers, 0 external `http(s)://`, 0 `/api/pages`, 0 `page_versions`, 0 SQL. All links relative to local method artifacts.

## E. No invention
- Every `28xxx` ID across content+preview+map ∈ the known 36 ledger IDs (24 accepted/limited-incl-excluded + 12 rejected): PASS. Unknown IDs: 0.
- Trust labels ∈ source-first vocabulary only; no product trust scores/levels invented.
- map totals: 6 claims · 2 accepted_full · 20 accepted_limited · 22 cited · 2 excluded · 12 rejected · 7 cite-unmatched · 0 numeric product cites.

## F. Preservation
- Existing pages untouched: `same-format-rebuild/page-content-…md` (13049 B), `same-format-rebuild/wiki-format-preview-…html` (24423 B), `wiki-page.html` (28665 B) — all unmodified. Candidate is purely additive under `evidence-trust-rebuild/`.

## Safety ledger
- Read-only verification + this ledger write only. 0 live-root writes · 0 existing-file edits · 0 DB/SQL · 0 /api/pages · 0 page_versions · 0 publish · 0 restart · 0 git · 0 cockpit/global · 0 cloud/OAuth · 0 browser · 0 cron.

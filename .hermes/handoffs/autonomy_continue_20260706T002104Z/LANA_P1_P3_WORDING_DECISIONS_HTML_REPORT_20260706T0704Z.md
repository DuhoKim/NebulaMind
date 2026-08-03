# Lana receipt — P1/P3 wording decisions HTML

Marker: `LANA_P1_P3_WORDING_DECISIONS_HTML_20260706T0704Z`
Lane: Lana · static public operator HTML only
Status: `DELIVERED_STATIC_HTML_NO_EXECUTION`
Active execution phrase: `NO ACTIVE EXECUTION PHRASE`

## Deliverable

Single standalone, self-contained HTML decision board:

- `frontend/public/agent-reports/p1-p3-wording-decisions.html` (31,276 bytes · 440 lines)

Receipt (this file):

- `.hermes/handoffs/autonomy_continue_20260706T002104Z/LANA_P1_P3_WORDING_DECISIONS_HTML_REPORT_20260706T0704Z.md`

Source docs read (read-only, no mutation):

- `docs/hwao_morning_blocker_specs_20260706T0308Z/P1_LEGACY_OVERCLAIMS_2298_2299_2924_SPEC.md`
- `docs/hwao_morning_blocker_specs_20260706T0308Z/P3_2572_PRIMACY_RECAST_SPEC.md`

## What the page contains

1. **Top banner** — title "P1/P3 Wording Decisions", `NO ACTIVE EXECUTION PHRASE` safe badge, zero-ledger badges (`DB writes: 0 · SQL execution: 0 · Trust recompute: 0 · Prose/wiki publish: 0`), and the marker `LANA_P1_P3_WORDING_DECISIONS_HTML_20260706T0704Z`.
2. **Plain-English summary** — compact non-jargon explanation of the 2298/2299/2924 overclaims and the 2572 primacy/evidence mismatch.
3. **P1 card** (left column on desktop, stacked on mobile) — before-state snapshot table + successor caution boundary (2945/2946), then per-claim sub-cards:
   - 2298: current text, draft scoped wording (verbatim from spec), route decision (recast/retire-into-2946 recommended · retire+re-parent alt · keep reject).
   - 2299: current text, draft scoped wording (verbatim), route decision (recast/re-parent-into-2945 recommended · low/moderate-certainty mechanism alt · keep reject).
   - 2924: display-state framing (endpoint-visible via `/api/claims/2924/evidence`, hidden from page claims, old `parent_replaced`/consensus 0.8), decision (finish cleanup/label-replaced recommended · retire+back-up-4-rows alt · leave reject).
4. **P3 card** (right column) — before-state snapshot + evidence-26088 mismatch note, then 2572 sub-card with current text, recommended cautious wording (verbatim), stricter alternative (verbatim), and the cautious-guard-vs-assertive-disputed choice; plus a separate 2573 "keep separate / do not merge" note.
5. **Cross-cutting decision** — trust recompute timing (stage after P4 guard = cautious default · same-packet = alternative).
6. **Decision checklist** — 5 items (2298 route · 2299 route · 2924 handling · P3 cautious vs stricter · trust recompute waits for P4), live-mirrored from the selections, with a sticky progress meter.

Interactivity is purely local: single-select decision chips backed by `localStorage` key `nm_p1p3_wording_decisions_v1`, a "Clear my selections" button, and a progress bar. No `<form>`, no `action=`, no `fetch`/XHR/WebSocket/beacon — nothing submits anywhere. No remote dependencies (all CSS/JS inlined, no external hosts, no CDN, no web fonts).

## Verification summary (grep + parse checks, read-only)

- HTML parses cleanly via `python3 html.parser` (325 start tags, no exception). Structural tags balanced: `html 1/1`, `head 1/1`, `body 1/1`, `script 1/1`, `section 2/2`, `table 2/2`.
- Banned approval phrases absent: `APPROVE EXECUTE` = **0**, `APPROVE APPLY` = **0**.
- Required strings present: marker (3×), `NO ACTIVE EXECUTION PHRASE` (3×), each zero-ledger phrase (1× each), `P1/P3 Wording Decisions` title, `separate, explicit local approval` (2×).
- Claim ids present: 2298, 2299, 2924, 2572, 2573, 2945, 2946, evidence 26088 all ≥1.
- Exact draft wordings present verbatim: 2298 scoped, 2299 scoped, 2572 cautious, 2572 stricter — all OK.
- Structure counts: 5 decision blocks, 5 checklist rows.
- Remote/external dependency scan: `https?://` = 0, external `src=`/`href=`/`@import`/`cdn.` = 0, `fetch`/`XMLHttpRequest`/`WebSocket`/`sendBeacon` = 0, `<form`/`action=` = 0.

## Safety ledger

| Action | Count / state |
|---|---|
| DB writes | 0 |
| SQL / apply / rollback execution | 0 |
| Trust recompute | 0 |
| Prose / wiki / page_versions publish | 0 |
| Product-code patch outside the static report file | 0 |
| Git / commit / push / deploy / restart | 0 |
| GCP / API / network usage | 0 |
| Files created | 2 (the HTML report + this receipt) |
| Files modified in place | 0 |
| Source docs | read-only |

Approval posture: this page is a decision board, not an execution gate. Choosing an option records only a local wording preference in the browser. Any future DB or prose packet acting on these choices needs a **separate, explicit local approval later**; no approval phrase is provided on the page or in this receipt, and the active state remains `NO ACTIVE EXECUTION PHRASE`.

Boundary note: main cockpit untouched. Tori to link/mirror/verify after this report. No tests/builds/deploys were run.

LANA_P1_P3_WORDING_DECISIONS_HTML_20260706T0704Z

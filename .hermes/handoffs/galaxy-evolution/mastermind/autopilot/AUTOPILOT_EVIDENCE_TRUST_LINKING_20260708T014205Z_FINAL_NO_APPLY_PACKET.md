# Final no-apply packet — Galaxy Evolution evidence links + trust leveling

Marker: AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Order: `mastermind/AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z.md`
Author: Hwao-director (pane %107). Written 2026-07-08 ~02:12Z (11:12 KST). Basis: method-lane candidates + method verdicts, plus this director's independent read-only re-verification (checksums, static-safety, no-invent, link integrity).

## STATUS: READY_FOR_USER_APPROVAL

## RESOURCE-SURGE AMENDMENT — approval wording superseded

After this packet was written, the user directed Tori to use the idle Goru/Gemini, Kun/Codex, Lana, and Hwao resources for a deeper verification surge. That surge found two important approval-wording corrections:

1. The original “served immediately / no restart” wording below is **not reliable for brand-new static subdirectories**. Read-only checks confirmed live-root `same-format-rebuild/` files exist on disk but still return 404 through the running `next start`; new `evidence-trust-rebuild/` dirs may likewise require a separately approved `:3000` restart to become visible.
2. Method1’s older preview used confusing `provenance` labels for the 27 unbound chips. Use the additive Method1 P1 label-fix candidate if mirroring: `evidence-trust-preview-p1-label-fix-20260708T022147Z.html`.

Do **not** use the original approval paragraph at line 72 as-is. Use the corrected approval wording in:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE_SYNTHESIS_20260708T022147Z.md`

All hard gates remain closed: no live-root copy, no restart/deploy, no product DB/API/page_versions/product-wiki publish, no git.

All three methods authored honest, static-safe evidence-link + trust-leveling static candidates under new `evidence-trust-rebuild/` dirs in the **working repo**, bound only to existing local ledgers (no invented evidence/IDs/trust). Exact mirror-to-live-root steps are pinned below. Not HARD_BLOCKED — binding was completed from local material where it exists and honestly marked unbound where it doesn't; no hard-gate action is needed to produce the candidates.

## What happened (plain English)

The user said the now-visible method pages read better but lack evidence links and trust leveling. Each method controller authored an additive static candidate that adds visible trust leveling + real evidence links **honestly bounded to what exists locally**:
- **M2** had real local source material → real bindings.
- **M1** had partial local evidence (a page inventory) → partial real bindings + honest "unbound" for the rest (product-DB-gated).
- **M3** is docs-only (no product markers) → trust *framing* from the debate map + local provenance navigation, with **no faked** product binding.

Nothing was mirrored to the live-served root (that stays a gated step), so these candidates 404 on :3000 until a user-approved mirror.

## Per-method candidates — paths, checksums, content, verification

Working-repo base `…/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`.

### M1 — packet-gated (`…/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/`) — verdict PASS/READY
| file | bytes | sha256(16) |
|---|---|---|
| `evidence-trust-preview-20260708T014205Z.html` | 37,763 | `70564e0ba8144ef5` |
| `evidence-trust-bindings-20260708T014205Z.md.json` | 17,491 | `ea08877e9348f93b` |
| `manifest-20260708T014205Z.json` | 468 | `fc5238bcef58f34e` |
- **3 of 30 claim chips** evidence-bound to real local evidence (43 evidence rows from `pgr-current-page-inventory-20260706T130610Z.json`), each linking to the local ledger + arXiv; per-page trust summary from real counts; **27 chips labeled `unbound-local`** (per-claim evidence resolves only in the product claim/evidence DB — a closed gate), not fabricated. Method chain: Goru check + Tori receipt + `HWAO_M1_EVIDENCE_TRUST_VERDICT` (PASS).

### M2 — source-first (`…/source-first-paper-adjudication/evidence-trust-rebuild/`) — director-verified READY (see receipt-gap note)
| file | bytes | sha256(16) |
|---|---|---|
| `page-content-20260708T014205Z.md` | 14,073 | `52cf8bfb422df809` |
| `wiki-format-preview-20260708T014205Z.html` | 13,531 | `6b106e5eb67798f5` |
| `evidence-trust-map-20260708T014205Z.json` | 7,499 | `c9848105c1a279a1` |
| `manifest.json` | 978 | `7cf79edc6d21eb81` |
- 6 claims {2942–2947} with **visible accepted / accepted-limited / rejected / excluded** trust leveling from the RATIFIED S2 source adjudication (`"derived from existing P1/S2 ledger; no invented data"`); 7 cite-unmatched kept honestly unmatched (local rows, not product cites). **Evidence links verified to resolve** to real local files: `../p1-source-position-ledger.html` (17,201 B) and `../p2-claim-status-ledger.html` (7,651 B).

### M3 — debate-map (`…/debate-map-to-wiki-rebuild/evidence-trust-rebuild/`) — verdict READY
| file | bytes | sha256(16) |
|---|---|---|
| `page-content-evidence-trust-20260708T014205Z.md` | 17,173 | `d908af489202ee08` |
| `wiki-format-preview-evidence-trust-20260708T014205Z.html` | 14,920 | `5e9236f56226b725` |
| `evidence-basis-20260708T014205Z.md` | 8,091 | `45d1cc932083c91d` |
- Docs-only trust layer: real **debate-map axis statuses** as trust chips (widely-supported / emerging-sample-limited / actively-debated / model-dependent / scoped-coverage-extension); per-section "Evidence basis →" links to a local provenance ledger (real source/claim IDs from `evidence_source_inventory.json` / `debate_map_data.json`); known unmatched items shown explicitly (2915/2921/2913 v1709-only; 2133→2605.22497 missing; 2374 garbled). **0 product claim/cite markers by design; P3 binding stays a CLOSED gate.** Method chain: Goru check + Tori receipt + `HWAO_M3_EVIDENCE_TRUST_VERDICT` (READY).

## Director cross-method verification (independent, read-only)
- **Static-safety — all PASS:** every candidate preview has 0 `<script>`, 0 real `new XMLHttpRequest/WebSocket`, 0 `fetch(`, 0 `/api/pages`, 0 `page_versions`. (M1's lone "WebSocket" grep hit is its own safety-legend text; external hosts are arxiv.org only for M1, none for M2/M3.)
- **No-invent — PASS:** M1/M2 bind only to their existing local inventories/ledgers and disclose unbound/unmatched; M3 fakes no product binding. No invented cite/claim/source IDs, DOIs, ADS links, or trust levels found.
- **Non-empty + present — PASS:** all 10 candidate files exist with the sizes/checksums above.
- **Link integrity — PASS** (M2 ledger links resolve; M3 links are local anchors).

## Receipt-chain gap (NON-BLOCKING, honest)
M1 and M3 have complete method receipt chains (Goru + Tori + Hwao verdict). **M2's method-local Goru/Tori/Hwao chain is absent** — its controller pane (%97) is parked on a *read-only* checksum prompt that references the live-root path, which the autopilot `--auto-approve-safe` correctly declines to auto-approve; per the order it was not keystroked. The M2 candidate itself is complete and independently verified above (static-safe, no-invent, trust vocabulary visible, links resolve), so this director verification substitutes for the missing M2 receipt. Not a deliverable defect; M2 parity receipts can still be emitted if the pane is later unstuck.

## What would change + exact next action (mirror to live root — GATED, no-apply)

These candidates are working-repo only and `404` on :3000 (which serves the live root). To make them visible, mirror each `evidence-trust-rebuild/` dir into the live root — the **same live-root-write gate** as `AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z`:
- SRC base `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/…/<dir>/evidence-trust-rebuild/`
- DST base `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/…/<dir>/evidence-trust-rebuild/`
- Live-root `evidence-trust-rebuild/` is **ABSENT for all three** → apply = `mkdir -p` each + `cp` the 10 files (checksums above; after-copy sha256 must equal source).
- Expected served URLs after mirror (currently 404):
  `http://127.0.0.1:3000/agent-reports/wiki-method-results/galaxy-evolution/<dir>/evidence-trust-rebuild/<preview>.html` → 200.
- **Validate:** `shasum -a 256 <dst>` == source sha256; `curl -s -o /dev/null -w '%{http_code} %{size_download}B'` each preview URL → `200 <srcbytes>B`.
- No build/deploy/restart needed (`next start` serves `public/` from disk).

## Approval gate wording

> "Approve mirroring the 10 Galaxy Evolution evidence-trust candidate files (3 new `evidence-trust-rebuild/` dirs, M1+M2+M3) from the working repo into the live-served repo `NebulaMind-origin-main-live/frontend/public/…` so the trust chips + evidence links become visible on :3000. Static file copy served immediately — **no** build, deploy, restart, git, DB, `/api/pages`, `page_versions`, or product-wiki publish. Reversible. Publishing into the product wiki, resolving M1's 27 product-DB-gated chips, and M3's P3 claim/citation binding all remain separate gates."

## Separate gates (stay CLOSED unless individually approved)
- Live-root mirror of these candidates (the step above).
- M1 full per-claim binding of the 27 `unbound-local` chips → product claim/evidence DB.
- M3 P3 product claim/citation binding (fresh snapshot + Goru re-check + resolve 3 unmatched + PENDING_RECHECK).
- Any live product-wiki publish (`/api/pages`, `page_versions`).

## Safety ledger (this packet + director pass)
Read-only inspection of working + live roots (bytes/sha256/served-status) + this one `.hermes` packet write. **Zero** live-root writes/copies, product DB/SQL, `/api/pages`, `page_versions`, live-wiki publish, deploy/restart, git, cockpit/global/Baseline/shared-parent, cloud/GCP/OAuth/secrets, browser, cron; **zero invented** evidence/cite/claim/source IDs/DOI/ADS/trust; zero Method3 P3 binding; zero keystrokes into panes. All hard gates remain closed.

## Method2 controller reconciliation (appended 2026-07-08T01:52Z, by the Method2 Hwao pane)

Two authoritative corrections from the Method2 lane; the director's cross-method analysis above is otherwise
convergent and left intact.

1. **M2 receipt-chain gap is CLOSED.** The "Receipt-chain gap" note above states M2's method-local
   Goru/Tori/Hwao chain is absent. It has since landed (the M2 controller ran the checksum comparison via a
   local read-only script — no live-root prompt needed):
   - Goru: `method2/EVIDENCE_TRUST_GORU_LEDGER_20260708T014205Z.md` — PASS (counts, static-safety, no-invent).
   - Tori+Hwao: `method2/HWAO_M2_EVIDENCE_TRUST_VERDICT_20260708T014205Z.md` — PASS/READY.
   - Progress: `method2/autopilot/AUTOPILOT_M2_EVIDENCE_TRUST_PROGRESS_{DISPATCH,COMPLETE}_20260708T014205Z.md`.
   The director's substitute verification and these lane receipts agree; the gap is now non-existent, not just non-blocking.

2. **Correction to "no restart needed" (packet §"What would change" + approval-gate wording).** The claim that a
   live-root mirror serves immediately with **no restart** is **empirically false for new subdirectories**, proven
   this session under order `AUTOPILOT_LIVE_ROOT_EMPTY_WIKI_REPAIR_PACKET_20260708T012233Z`: after the
   `same-format-rebuild/` dir was mirrored into the live root, its files were **present on disk (identical sha) yet
   returned 404 on :3000** — the running `next start` does not serve a `public/` subdirectory created after boot.
   The `evidence-trust-rebuild/` dirs are likewise brand-new, so after mirroring they will **404 until the `:3000`
   process is restarted**. The approval-gate wording should therefore add: *"and separately approve restarting the
   :3000 process so the newly-added `evidence-trust-rebuild/` files are served."* Restart is a deploy/restart hard
   gate — its own approval, not covered by the file-copy approval. (`wiki-page.html` mirrors serve immediately only
   because they replace an already-served file, not because new subdir files do.)

Neither correction changes the packet STATUS (READY_FOR_USER_APPROVAL) or the checksum/mirror spec — they make the
receipt record and the apply/serve expectation accurate. Method-local separation preserved; no M1/M3 file touched.

AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z

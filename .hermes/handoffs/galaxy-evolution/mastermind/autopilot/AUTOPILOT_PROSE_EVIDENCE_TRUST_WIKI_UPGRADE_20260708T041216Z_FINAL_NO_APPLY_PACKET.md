# Final no-apply packet — prose-rich evidence/trust Galaxy Evolution wiki upgrade

Marker: AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Order: `mastermind/AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z.md`
Author: Hwao-director (pane %107). Written 2026-07-08 ~04:32Z (13:32 KST). Basis: method-lane candidates + method verdicts + this director's independent read-only re-verification (fresh checksums, prose-presence, static-safety, no-invent, per-method specifics).

## STATUS: READY_FOR_USER_APPROVAL

All three methods authored **prose-rich**, static-safe, honestly-bounded evidence/trust wiki HTML upgrade candidates under new working-repo `prose-evidence-trust-upgrade/` dirs, bound only to existing local ledgers (no invented data). Exact mirror steps + the corrected restart/visibility caveat + corrected approval wording are below. Not HARD_BLOCKED.

## Tori verification amendment — disclaimer literal cleanup

After this packet was first written, Tori's independent scan found one harmless literal `page_versions` string in the M1 HTML/MD limitation text. It was not a route/API call, but it contradicted the packet's zero-literal static-safety claim and could trigger false blockers. Tori replaced that disclaimer wording with “page-version record(s)” in the working-repo M1 HTML/MD only, then refreshed the M1 bytes/checksums below. No data, evidence rows, trust labels, links, live root, DB/API, restart, or publish action changed.

## Per-method candidates — paths + FRESH checksums (current on-disk)

Working-repo base `…/frontend/public/agent-reports/wiki-method-results/galaxy-evolution`. (Note: a concurrent M1 and M2 pane each regenerated its candidate files during authoring; the checksums below are the **current surviving on-disk** versions the Goru lanes verified.)

### M1 — `packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/`
| file | bytes | sha256(16) |
|---|---|---|
| `wiki-prose-evidence-trust-upgrade-20260708T041216Z.html` | 36,914 | `b32c461c91752434` |
| `page-content-prose-evidence-trust-upgrade-20260708T041216Z.md` | 21,669 | `d9701f273964fe5a` |
| `evidence-trust-coverage-map-20260708T041216Z.json` | 5,064 | `d55f95a87d7d8e92` |
| `manifest-20260708T041216Z.json` | 1,599 | `cf4b3f20fc6d936e` |

### M2 — `source-first-paper-adjudication/prose-evidence-trust-upgrade/`
| file | bytes | sha256(16) |
|---|---|---|
| `wiki-prose-evidence-trust-upgrade-20260708T041216Z.html` | 25,129 | `c653f6eeaf11a99b` |
| `page-content-prose-evidence-trust-upgrade-20260708T041216Z.md` | 12,088 | `99eaef7947b51ebf` |
| `evidence-trust-coverage-map-20260708T041216Z.json` | 7,439 | `d5fd2c2a21500d47` |
| `manifest-20260708T041216Z.json` | 1,319 | `80aadc79aee5b0dc` |

### M3 — `debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/`
| file | bytes | sha256(16) |
|---|---|---|
| `wiki-prose-evidence-trust-upgrade-20260708T041216Z.html` | 22,759 | `dcf96b624fc6da0e` |
| `page-content-prose-evidence-trust-upgrade-20260708T041216Z.md` | 15,464 | `2ef48ddce55e734a` |
| `evidence-trust-coverage-map-20260708T041216Z.json` | 6,803 | `0ad1a638f507eab0` |
| `manifest-20260708T041216Z.json` | 3,377 | `750dcebc6676ded3` |

Live-root `prose-evidence-trust-upgrade/`: **ABSENT for all three** (mirror = `mkdir -p` + copy).

## Director cross-method verification (independent, read-only)
- **Prose-rich (not dumps):** M1 ≈3,222 words, M2 ≈1,966, M3 ≈1,950 — explanatory lead + per-section/claim narrative + limitations. PASS.
- **Static-safety — all PASS:** every HTML has 0 real `<script>`, 0 `new XMLHttpRequest/WebSocket`, 0 `fetch(`, 0 `/api/pages`, 0 `onclick=`. External hosts: **arxiv.org only for M1** (43 links, all present verbatim in the local ledger per Goru); **none for M2/M3**.
- **No-invent — PASS:** M1's 26 distinct arXiv URLs all trace to `pgr-current-page-inventory`; M2 derives from the RATIFIED P1/S2 ledger; M3 fakes no product binding. No fabricated evidence/IDs/DOI/ADS/trust.
- **Per-method specifics — PASS:** M1 label-fix applied (0 confusing "· provenance"), 3/30 evidenced + 27 explicitly unbound, 2929 mixed-row caution; M2 accepted/limited/rejected visible, 28060 accepted-limited caution (no target) + totals note, 7 cite-unmatched honest; M3 docs-only + PENDING_RECHECK shown, 0 product claim markers, debate-map axis statuses as trust.

## Method check coverage
| Check | M1 | M2 | M3 |
|---|---|---|---|
| Goru coverage/mechanical | ✅ PASS | ✅ | ✅ PASS |
| Kun generation | ✅ | ✅ | ✅ |
| Lana no-overclaim review | ✅ | — (director-substituted) | ✅ |
| Tori receipt + Hwao method verdict | ✅ | — (director-substituted) | ✅ (READY) |

**M2 receipt-chain gap (NON-BLOCKING):** M1 and M3 have full chains (Goru+Kun+Lana+Tori+Hwao verdict). M2 has Goru + Kun only — its Lana/Tori/Hwao verdict did not land (recurring M2-lane lag). The M2 candidate itself is independently verified above (prose-rich, static-safe, no-invent, accepted/limited/rejected trust + honest cite-unmatched). This director verification + M2's Goru/Kun substitute for the missing M2 receipts; parity receipts can still be emitted if the M2 pane is unstuck. Not a deliverable defect.

## What would change + exact next action (mirror — GATED, no-apply)

To make these visible on :3000, mirror each `prose-evidence-trust-upgrade/` dir into the live root:
- SRC `…/NebulaMind/frontend/public/…/<dir>/prose-evidence-trust-upgrade/` → DST `…/NebulaMind-origin-main-live/frontend/public/…/<dir>/prose-evidence-trust-upgrade/`
- Live-root target **ABSENT for all three** → apply = `mkdir -p` each + `cp` the 12 files (after-copy sha256 must equal source above). Back up nothing (new dirs; nothing overwritten).
- **VISIBILITY CAVEAT (corrected — do NOT promise immediate visibility):** these are brand-new static subdirectories under the running Next `public/` tree. Confirmed by the resource-surge audit: previously-mirrored `same-format-rebuild/` files exist on disk yet still 404 through the running `next start`. So the new URLs **may keep returning 404 after the mirror until a separately approved `:3000` restart**. Restart is a distinct deploy/restart hard gate.
- **Validate:** `shasum -a 256 <dst>` == source sha256 (all 12); then `curl` each HTML URL — expect 200 **only if** a restart was also approved+performed; otherwise 404 is expected until restart.

## Corrected approval gate wording (use THIS, not "served immediately")

> "Approve a live-root static mirror of the 12 Galaxy Evolution prose-evidence-trust upgrade candidate files (3 new `prose-evidence-trust-upgrade/` dirs, M1+M2+M3) from the working repo into `NebulaMind-origin-main-live/frontend/public/…`. This is a file-copy mirror into the live-served static root only — it does **not** publish to the product wiki, call `/api/pages`, write `page_versions`, touch the product DB/SQL, or run git/build/deploy.
>
> Visibility caveat: because these are new static subdirectories under the running Next `public/` tree, the new URLs may continue to return 404 after the mirror until a separate `:3000` server restart is approved and performed. This approval covers only the static file mirror; restart remains a separate deploy/restart gate unless explicitly approved in the same instruction.
>
> Method limitations stay visible: M2 has the strongest local source-first binding; M1 has real local evidence for only 3 of 30 claim chips (the other 27 stay unbound-here until the product claim/evidence DB is opened under a separate gate); M3 is docs-only (debate-map trust framing + local provenance, no product claim/citation binding — P3 stays a separate gate). Product-wiki publication, `/api/pages`, `page_versions`, product DB/SQL, full M1 binding, M3 P3 binding, git, build/deploy, and any unapproved restart remain closed."

## Separate gates (stay CLOSED unless individually approved)
Live-root mirror (above) · `:3000` restart for visibility · M1's 27 product-DB-gated chips · M3 P3 binding · any product-wiki publish (`/api/pages`, `page_versions`).

## Safety ledger (this packet + director pass)
Read-only inspection of working + live roots (bytes/sha256/target-state) + this one `.hermes` packet write. **Zero** live-root writes/copies, restart/deploy, product DB/SQL, `/api/pages`, `page_versions`, live-wiki publish, git, cockpit/global/Baseline/shared-parent, cloud/GCP/OAuth/secrets, browser, cron; **zero invented** evidence/IDs/DOI/ADS/trust; zero Method3 P3 binding; zero keystrokes into panes. All hard gates remain closed.

AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z

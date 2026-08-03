# Hwao-led order — Galaxy Evolution evidence links + trust leveling

Marker: `AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z`

## User direction

User checked the now-visible method wiki pages and said the results are better, but they are missing evidence links and trust leveling. Run the M1/M2/M3 autopilots on those issues.

## Starting measurement by Tori

Checked served static method pages on `http://127.0.0.1:3000/agent-reports/wiki-method-results/galaxy-evolution/...` at 2026-07-08T01:42Z:

- M1 `wiki-page.html`: 29,063 B, 14 `<h2>`, **0 hrefs**, evidence-ish hrefs 0, trust-word hits 18.
- M2 `wiki-page.html`: 28,665 B, 12 `<h2>`, 4 broad hrefs, evidence-ish hrefs 4, trust-word hits 43; still no clear per-claim/per-section evidence-linking UX.
- M3 `wiki-page.html`: 18,383 B, 9 `<h2>`, **0 hrefs**, evidence-ish hrefs 0, trust-word hits 0.

The issue is real. Treat the previous static page completion as narrative-page completion only, not evidence/trust completion.

## Goal

Improve the Galaxy Evolution method pages with explicit evidence links and trust leveling while staying inside safe static/no-DB scope.

This order is for **working-repo static candidate artifacts and a final no-apply live-root packet**, not for immediate live publication.

Required final artifact:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot/AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z_FINAL_NO_APPLY_PACKET.md`

Final artifact must contain one of:
- `STATUS: READY_FOR_USER_APPROVAL` if improved static artifacts are created and exact mirror/apply steps are pinned.
- `STATUS: HARD_BLOCKED` only if trustworthy evidence/trust binding cannot be completed without a hard-gate action or missing source material.

## Scope allowed without further user approval

Allowed:
- Read-only inspection of current working repo artifacts under:
  `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/`
- Read-only inspection of handoff/source/claim/trust/evidence ledgers under:
  `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/`
- Read-only HTTP checks against `127.0.0.1:3000` static method pages.
- Additive writes under `.hermes/handoffs/galaxy-evolution/`.
- Additive working-repo static candidate files under each method root, preferably a new directory:
  `evidence-trust-rebuild/`
  with page content, preview, manifest, and validation receipts.

Do not overwrite live-served root. Do not overwrite the existing live root copies. Do not publish to product wiki. If a mirror to live root is desired, produce a no-apply packet with exact source/target/sha/backup/validation and wait for user approval.

## Hard gates still closed

- product DB/SQL and pane-initiated SQL
- `/api/pages`, `page_versions`, live product wiki publish
- live-root writes/copies into `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/...` until a separate explicit approval
- deploy/restart/service mutation
- git commit/push/merge/rebase/reset
- public Baseline cockpit/global/shared-parent mutation
- cloud/GCP/API/billing/OAuth/token/secrets/credentials/cookies
- browser automation
- cron
- Method3 P3 product claim/citation binding unless separately approved

## Quality requirements

Do not invent evidence. Do not invent product cite IDs, claim IDs, source IDs, DOI/ADS links, or trust levels. Use only existing source ledgers, claim markers, accepted/limited/rejected/excluded positions, local source pages, and already-present source metadata. If source binding is not available, mark it explicitly as unbound/unmatched and explain what gate/data is missing.

Trust leveling should be plain English and visible:
- per-page or per-section trust summary, based on evidence status actually present;
- per-claim/per-evidence chips where claim markers exist;
- Method2 accepted vs accepted-limited vs rejected/excluded must be visibly distinguished;
- Method3 is docs-only / P2 non-binding unless existing M3 ledgers support stronger binding; do not pretend it has claim/evidence binding if it does not.

Evidence links should be useful and static-safe:
- link to local method source ledgers/pages where possible;
- link from claim chips or section evidence panels to the exact local source/evidence artifact if available;
- use disabled/unmatched labels when IDs cannot be resolved safely;
- no live API calls, scripts, fetch/XHR/WebSocket, or product DB routes.

## Method lane assignments

Hwao-director:
- coordinate M1/M2/M3;
- require Goru mechanical checks;
- produce final no-apply packet with exact file paths, checksums, what changed, and next approval wording.

Method1:
- M1 currently has 30 claim markers but 0 links. Add a static evidence/trust candidate that binds claim chips to the best existing local evidence/source artifacts or explicitly marks unbound where absent.
- Produce method-local receipt and Goru check.

Method2:
- M2 has source-first ledgers and accepted/limited/rejected/excluded positions. Make trust leveling explicit and useful. Keep the 7 cite-unmatched IDs honest unless resolvable from existing ledgers.
- Produce method-local receipt and Goru check.

Method3:
- M3 currently has no links and no trust wording. Add docs-only trust framing and evidence/source navigation without pretending P3 claim/citation binding exists. If stronger binding needs P3 gate, state that clearly.
- Produce method-local receipt and Goru check.

Goru lanes:
- count hrefs, evidence-ish hrefs, trust labels/chips, unresolved/unmatched markers;
- verify no scripts/API/fetch/DB/live publish strings;
- verify generated candidate files exist and are not empty;
- verify old pages remain preserved;
- compare served pages vs candidate pages only as read-only evidence; do not mirror.

## Stop condition

Do not stop after one lane or one packet. Continue until:

1. all three method lanes have evidence/trust candidate artifacts or explicit hard-blocked method receipts;
2. Goru mechanical checks exist for all three;
3. Hwao-director writes the final no-apply packet at the required path with `STATUS: READY_FOR_USER_APPROVAL` or `STATUS: HARD_BLOCKED`;
4. the marker `AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z` is present in final packet.

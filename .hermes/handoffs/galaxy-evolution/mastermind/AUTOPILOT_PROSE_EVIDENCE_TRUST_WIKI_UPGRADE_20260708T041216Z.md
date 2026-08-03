# Hwao-led order — prose-rich evidence/trust wiki HTML upgrade

Marker: `AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z`
Estimated run: about 2 hours (`estimated_total_seconds: 7200`).

## User direction

The user says the evidence/trust updates are not really applied to the HTML yet, and asks the autopilots to upgrade the wiki with **more prose** and with claims/sections **covered by evidence links and trust levels**, running for about a couple of hours.

## Current baseline

Existing visible method pages were improved once by static copy, but evidence/trust work is still only candidate/sidecar level. Resource surge found:
- M1 has an additive P1 label-fix candidate correcting confusing `provenance` labels:
  `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-p1-label-fix-20260708T022147Z.html`
- M2 source-first evidence/trust map is mostly sound; totals include evidence `28060` as an accepted-limited caution with target `None`.
- M3 is docs-only unless P3 product binding is separately approved.
- Brand-new live-root public subdirectories may still 404 until separately approved `:3000` restart; do not promise immediate visibility.

## Goal

Produce upgraded, prose-rich static HTML wiki candidates in the **working repo** for M1, M2, and M3. These should read like useful wiki pages, not just dashboards/ledgers: explanatory paragraphs, claim-by-claim or section-by-section evidence boxes, plain trust labels, and explicit limitations.

This order is not a live-root mirror, restart, product wiki publish, DB write, or git action. It must end in a final no-apply packet for user approval.

Required final artifact:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/autopilot/AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z_FINAL_NO_APPLY_PACKET.md`

Final status must be one of:
- `STATUS: READY_FOR_USER_APPROVAL` if upgraded HTML candidates exist and are verified.
- `STATUS: HARD_BLOCKED` only if no honest upgrade can be produced without a hard-gate action.

## Allowed scope without further approval

Allowed:
- Read existing working-repo static artifacts under:
  `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/`
- Read `.hermes/handoffs/galaxy-evolution/` reports, receipts, ledgers, resource-surge findings.
- Read-only HTTP checks against `127.0.0.1:3000` only to compare current visibility; do not treat 404 as failure if candidate dirs are not mirrored.
- Additive writes under `.hermes/handoffs/galaxy-evolution/`.
- Additive working-repo static candidate writes under each method directory in a new directory:
  `prose-evidence-trust-upgrade/`

Preferred candidate files per method:
- `wiki-prose-evidence-trust-upgrade-20260708T041216Z.html`
- `page-content-prose-evidence-trust-upgrade-20260708T041216Z.md`
- `evidence-trust-coverage-map-20260708T041216Z.json`
- `manifest-20260708T041216Z.json`

Do not overwrite current `wiki-page.html`, `same-format-rebuild/`, or existing `evidence-trust-rebuild/` files. Add new candidate files only.

## Hard gates still closed

- Live-root writes/copies into `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/...`
- Any restart/deploy/service mutation, including `:3000` restart
- Product DB/SQL and pane-initiated SQL
- `/api/pages`, `page_versions`, live product wiki publish
- git commit/push/merge/rebase/reset
- public cockpit/global/shared-parent mutation
- cloud/GCP/API/billing/OAuth/token/secrets/credentials/cookies
- browser automation
- cron
- Method3 P3 product claim/citation binding unless separately approved

## Quality requirements

The upgraded HTML must have more prose and better coverage than the current candidates:

1. **Prose first:** each method page should include an explanatory lead, section/claim narrative paragraphs, and a plain-English conclusion/limitations section.
2. **Evidence boxes:** each claim/section should show what evidence supports it, what is limited, and what is unbound/unmatched. Use local static links only.
3. **Trust levels:** show trust status next to each claim/section. Define the trust vocabulary on-page. Do not pretend the three methods use the same trust scale.
4. **Honesty:** no invented evidence, IDs, DOIs, ADS links, product cite IDs, claim IDs, or trust levels. If data is not available locally, say “unbound here” or “requires product DB/P3 gate.”
5. **M1 specifics:** use the P1 label-fix candidate wording. Make clear that only 3/30 claim chips have local evidence; the other 27 are unbound here, not high-trust. Add prose explaining this limitation. If possible, add distinct-paper counts and caution for 2929’s mixed/non-committal rows using existing local data only.
6. **M2 specifics:** convert source-first status into readable prose: accepted vs accepted-limited vs excluded/rejected; define evidence 28060 as an accepted-limited caution with no current target claim; keep 7 cite-unmatched honest; preserve `accepted_limited:20` / `cited_positions:22` with a note explaining per-claim arrays sum lower because of 28060.
7. **M3 specifics:** docs-only trust framing from debate-map axis statuses; local provenance navigation; no product claim/cite binding; show unmatched/PENDING_RECHECK items explicitly.
8. **Static safety:** no scripts, fetch/XHR/WebSocket, inline handlers, product routes, DB routes, external runtime dependencies, or live APIs. Method1 arXiv evidence links are allowed only if already present in local data and marked external.
9. **Visible result shape:** candidate HTML should be directly openable from the working repo and should not be just a JSON dump or receipt.

## Resource-use instruction

Use the board aggressively but usefully for about two hours or until the complete upgrade lands:

- Hwao-director: coordinate, prevent stale mirror approvals, assemble final packet.
- M1/M2/M3 Hwao lanes: each drives its method upgrade; dispatch local Lana/Goru/Kun/Tori as needed.
- Goru/Gemini lanes: mechanical coverage counts, link checks, static-safety, missing/unbound counts, no-invent scans.
- Kun/Codex lanes: deterministic generation/check scripts, checksum manifests, local link graph checks, HTML validity checks.
- Lana lanes: prose/UX/no-overclaim review and precise label fixes.
- Tori lanes: receipts and independent verification only.

Do not stop after a single report. Keep idle lanes doing useful checks until all three upgraded candidate pages and verification receipts exist.

## Method outputs expected

M1 output target directory:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/prose-evidence-trust-upgrade/`

M2 output target directory:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/prose-evidence-trust-upgrade/`

M3 output target directory:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/prose-evidence-trust-upgrade/`

## Stop condition

Stop only when:
1. M1/M2/M3 each have upgraded HTML + markdown/content + coverage map/manifest or a method-specific hard-blocked receipt.
2. Goru/Gemini mechanical checks exist for all three.
3. Kun/Codex static/link/checksum checks exist for all three or a cross-method equivalent.
4. Lana no-overclaim/prose review exists.
5. Hwao-director writes the final no-apply packet at the exact required path with exact source paths, bytes, sha256, known visibility caveat, and corrected approval wording.
6. The marker `AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z` appears in all major receipts.

## Safety ledger

Starting this order performs only a `.hermes` order write and autopilot dispatch. All live-root mirror, restart/deploy, DB/API/page_versions/product wiki publish, git, cloud, browser, cron, and Method3 P3 hard gates remain closed.

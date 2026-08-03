# Hwao-Led Overnight Paper-Board Execution Brief

Marker: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`

## Owner direction

The owner approved execution of Plan A+B+C+D through 2026-07-27 10:00 KST, followed by publication on NebulaMind.

This receipt starts the approved local research/candidate run. It does not itself promote any file to a public root. Because the candidate files, exact served targets, before-state hashes, backups, rollback bytes, and public URLs do not exist yet, the publication portion must culminate in a separate candidate-specific static-public promotion packet and exact `APPROVE PUBLISH <packet_id>` phrase before public bytes change.

## Corrected source and output roots

The approved plan's source-root spelling was stale. The actual live Lab source root discovered at T0 is:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/lab-runs/`

Treat that entire root as immutable input tonight. Do not use the stale nonexistent path under `mastermind/aas-autopilot/lab-runs/`.

The only approved write root is:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-research-20260726/`

## Operating window

- T0: 2026-07-26 22:32 KST / 2026-07-26T13:32:16Z.
- Earliest final audit: 2026-07-27 09:30 KST / 2026-07-27T00:30:00Z.
- Hard stop and morning handoff: 2026-07-27 10:00 KST / 2026-07-27T01:00:00Z.
- This is an operating window, not only a maximum estimate. If first-pass packets finish early, continue bounded deepening, independent verification, and artifact auditing until 09:30 KST unless the owner stops the run or a genuine blocker closes all safe work.
- Progress snapshots: T0, 00:00, 03:00, 06:00, 09:00, final.

## Hwao lane map

Hwao/Fable coordinates and adjudicates. Tori relays, records, and independently verifies receipts. Maximum three active helper lanes.

1. Packet A — mass-metallicity reconciliation.
   - Goru: mechanical field/provenance matrix.
   - Kun: independent reproducibility and duplication analysis.
   - Hwao: canonical decision only after both receipts.
2. Packet B — citation integrity.
   - Kun: exact unsupported-claim/citation map and isolated corrected candidates.
   - Goru: independent one-to-one citation mechanical check.
   - Lana: no-overclaim review after candidate text exists.
3. Packet C — isolated paper candidates.
   - Lana: scientific candidate text using only captured inputs and explicit caveats.
   - Kun: reproduction, source/result identity, TeX/PDF build and deterministic checks.
   - Hwao: final local candidate status. Packet A gates the d8 candidate.
4. Packet D — verdict and acceptance-gap closure.
   - Goru: mechanically recover what verdict language actually exists for `7cb504ea7ad3`; do not infer a missing token.
   - Lana: assess whether `fesc002` limitations can be improved without weakening caveats.
   - Hwao: adjudicate; MINOR remaining MINOR is acceptable.
5. Publication preflight.
   - Only after candidate outputs stabilize: trace existing public mapping, back up every served target, prepare exact source→target diff, rollback, preview, SHA and HTTP verification plan, and a unique publish phrase.
   - Status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`; do not copy to public roots tonight without that phrase.

## Immutable inputs

Top-level run JSON inputs:

- `2ab3c92eea8a.json`
- `d8de519cb9c9.json`
- `e2f3b038f8dd.json`
- `2958462772b2.json`
- `gated-e2e-demo.json`
- `gated-halt-demo.json`
- `7cb504ea7ad3.json`
- `fesc002.json`

Their run subdirectories, histories, existing PDFs, figures, tables, and manifests are also read-only. Tori will capture hashes before and after.

## Output contract

All new files must remain beneath the approved output root. Required folders/files:

- `baseline/BOARD_SNAPSHOT.json`
- `baseline/INPUT_SHA256.txt`
- `baseline/INPUT_MANIFEST.json`
- `quota/usage-checkpoint-*.json`
- `packets/A-mzr-reconciliation/`
- `packets/B-citation-integrity/`
- `packets/C-study-to-candidate/`
- `packets/D-verdict-acceptance/`
- `reviews/hwao/`, `reviews/lana/`, `reviews/goru/`, `reviews/kun/`
- `progress/PROGRESS_*.md`
- `promotion-preflight/`
- `morning/MORNING_HANDOFF.md`
- `MANIFEST.json`
- `SHA256SUMS`

Every AI-authored science artifact must say `AI_DRAFT_NOT_HUMAN_GOLD`.

## Safety boundary

Allowed: read the current Lab records and their local source artifacts; perform public-source scholarly retrieval when needed; run local deterministic analysis; create isolated text/JSON/CSV/TeX/PDF/review artifacts under the approved output root; use direct subscription-backed Claude Code, Codex, and Antigravity lanes.

Forbidden before a separate exact gate: write or rewrite current Lab run JSON; alter current Lab run directories; use the live runner; replace existing PDFs; modify the public cockpit or any public/static root; DB/SQL/API/wiki/page-version writes; deploy/restart; git add/commit/push/merge; cron; browser automation; credentials/account/billing/cloud configuration; Nous purchased-balance usage; Anthropic third-party PAYG routing.

Stop a lane on source drift, a paid/overage prompt, unsupported numbers, unsupported citations, missing provenance, expected-value `CONTRADICTS`, or a candidate that would need a weakened caveat to pass.

## Completion states

- `DONE`: deliverables and independent receipts pass.
- `PARTIAL`: useful bounded artifact exists but a named gate remains open.
- `BLOCKED`: no safe path without new source, mutation, payment, or approval.

Hwao must not relabel `PARTIAL` or `BLOCKED` as success. Failed reviews remain preserved and versioned.

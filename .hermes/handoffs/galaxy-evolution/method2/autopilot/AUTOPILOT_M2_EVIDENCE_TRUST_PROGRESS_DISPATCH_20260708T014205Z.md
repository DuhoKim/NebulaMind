# Method2 autopilot — evidence-trust DISPATCH progress

Marker: AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z
Continuation: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Controller: Method2 Hwao (autonomous, bounded docs/static, additive candidate).
Dispatch UTC: 2026-07-08T01:52:00Z

## Task (Method2 lane)
Add explicit **evidence links** + **trust leveling** to the Method2 source-first page as an ADDITIVE static
candidate under `source-first-paper-adjudication/evidence-trust-rebuild/`. Use only existing ratified ledger
facts (no invented evidence/cite/trust). Keep the 7 cite-unmatched IDs honest. Do not overwrite existing pages;
do not touch the live root.

## Design (derived from existing P1/S2 ledger)
- Trust leveling = method-local **source-first adjudication status**: ACCEPTED (full, 2) · ACCEPTED-LIMITED (20) ·
  EXCLUDED (2, held out) · REJECTED (12, held out) — explicitly NOT product DB trust.
- Evidence links = relative links to the local `p1-source-position-ledger.html` / `p2-claim-status-ledger.html`.
- cite-unmatched honesty preserved: all 22 supporting IDs unresolved to product cite IDs → linked to local ledger.

## Lane chain
1. Kun/Lana (author) → candidate content + preview + map + manifest (generated deterministically from the ledger).
2. Goru (mechanical) → counts (hrefs, evidence-ish, trust chips, unmatched), static-safety scan, no-invention check.
3. Tori/Hwao → receipt + method verdict.
4. Controller → cross-method final no-apply packet at the required mastermind path.

## Safety ledger (dispatch)
- live-root writes: 0 · existing-file overwrites: 0 · DB/SQL: 0 · /api/pages / page_versions / publish: 0
- deploy/restart: 0 · git: 0 · cockpit/global/shared-parent: 0 · cloud/OAuth: 0 · browser: 0 · cron: 0

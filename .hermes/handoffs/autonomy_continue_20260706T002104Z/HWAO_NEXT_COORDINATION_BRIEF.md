# HWAO BRIEF — continue autonomous recommended sequence — 20260706T002104Z

User direction, current chat:

> okay now keep going on working autonomously with recommended sequence, and let Hwao coordinate all the available resources. and you can also update DB if it's ripen enough.

Role contract:
- Hwao/Fable coordinates, plans, divides resources, assembles results, and directs next cockpit/status text.
- Tori/Hermes relays, records, verifies receipts/files/markers, and executes only bounded Hwao/user-directed actions.
- Lana = high-reasoning/science/prose/methods review.
- Goru = mechanical counts/maps/checks.
- Kun = reproducibility/boundary/implementation checks.

Fresh verified state from Tori before this brief:
- Prior Hwao direction: `.hermes/handoffs/overnight_autonomy_20260705T1615Z/HWAO_CONTINUE_OVERNIGHT_DIRECTION.md`.
- Pinning atlas result: `docs/hwao_overnight_pinning_atlas_20260705T153533Z/OVERNIGHT_RESULT.md`; PASS, 397 evidence rows / 203 sources / 10 ready-to-pin / 200 missing sources, DB writes 0, `NO ACTIVE EXECUTION PHRASE`.
- Wave-2 run dir: `docs/hwao_overnight_pinning_wave2_20260705T1615Z/`.
  - Fetched exactly the 3 Hwao-approved arXiv sources and copied 2 local sources; manifest/log present.
  - Lana adequacy report: `LANA_WAVE2_ADEQUACY.md`, marker `LANA_WAVE2_ADEQUACY_20260705T1615Z`, 5 target pins adequate/pass-with-limitation; 2931 stays neutral_context; 2929 excluded.
  - Goru repaired pin ledger: `PINS_WAVE2.jsonl` + `GORU_WAVE2_COUNTS.md`, marker `GORU_WAVE2_MECHANICAL_REPAIRED_20260705T1635Z`.
  - Tori independent validation just reran in this session: parsed 5 rows, evidence ids [26088,26089,28099,28132,28155], recomputed source text hashes, verified `text[char_start:char_end] == quote`, enforced no 2929, neutral/none not upgraded to support, scanned wave2+dbprep dirs for SQL/apply/rollback/migration artifacts. Result: PASS, no errors/warnings, no mutation artifacts, DB writes 0, active phrase `NO ACTIVE EXECUTION PHRASE`.
  - I did not find a Kun `KUN_WAVE2_BOUNDARY.md`, `CHECKER_RESULT.md`, or `pinning_wave2_checker.py` in the wave2 dir. Decide whether that is required before declaring Track A complete, or whether Tori validation can stand in temporarily and Kun should do a delayed reproducibility check.
- DB spec-only run dir: `docs/hwao_overnight_db_packet_prep_20260705T1615Z/`.
  - `DB_PACKET_PREP_SUMMARY.md`, marker `DB_PACKET_PREP_DRAFTS_READY_20260705T1615Z`.
  - `DEDUPE_1308_5224v1_TRIPLICATE_SPEC.md` and `EVIDENCE_DISPOSITION_2929_PARENT_REPLACED_SPEC.md` exist. They are Markdown specs only, no SQL/apply, no execution phrase.
- Current safety boundary: user's broad “update DB if ripe enough” authorizes ripeness evaluation and possibly packet preparation; it is not a packet-specific `APPROVE EXECUTE <packet_id>` phrase. No DB writes may execute unless a reviewed exact packet exists and the user later sends the exact packet-specific approval phrase.

Your task now:
1. Decide the next recommended sequence after wave2/specs, on the mission spine: papers/source pins -> claim/status ledger -> debate map -> prose -> derived claims/evidence/trust. Avoid UI/runtime/product drift unless needed for operator visibility.
2. Coordinate all available resources. Name exact lane assignments for Lana, Goru, Kun, and Tori, with deliverable paths and done markers.
3. Decide whether DB work is ripe now. If ripe, specify exactly which class is allowed now: (a) read-only verification, (b) exact packet preparation only, or (c) execution-ready later only after exact phrase. Do not execute DB writes in this report.
4. If a missing Kun boundary/checker is a blocker, make that the first next step and give Tori a short Kun brief.
5. If wave2 is complete enough, choose the next autonomous artifact slice (likely debate-map refresh or exact packet preparation from the specs), and give Tori exact saved briefs to write/dispatch.
6. Include a short cockpit/status wording Tori may publish/checkpoint. Preserve `NO ACTIVE EXECUTION PHRASE` unless you explicitly direct a future packet surface; do not surface an executable phrase publicly.
7. Write your full report to `.hermes/handoffs/autonomy_continue_20260706T002104Z/HWAO_NEXT_DIRECTION.md` and include the marker below.

Hard stops:
- No DB writes, trust recompute execution, SQL/apply/rollback execution, migrations.
- No prose/wiki/page_versions publish or product ingest.
- No deploy/restart/service/config/queue changes.
- No git commit/push/merge/rebase/reset/cleanup.
- No secrets/account/billing/provider-route/GCP changes.
- No unattended Gemini web/app operation.
- No extra source fetching unless Hwao names exact sources and Tori verifies need.
- If a lane asks out-of-scope twice, stop it and write `BLOCKED_<lane>.md`.

Required marker in your report:
`HWAO_NEXT_DIRECTION_20260706T002104Z`

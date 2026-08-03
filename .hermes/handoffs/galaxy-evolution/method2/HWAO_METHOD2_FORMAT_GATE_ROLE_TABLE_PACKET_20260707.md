# Method2 format-gate role-table packet — same-format wiki output + Ultra usage scrutiny

Marker: HWAO_METHOD2_FORMAT_GATE_ROLE_TABLE_PACKET_20260707
Issued by: Hwao / Fable coordinator-planner (Hwao-Tori2-SFA lane)
Request being answered: HWAO_REQUEST_METHOD2_FORMAT_GATE_ROLE_TABLE_PACKET_20260707
Governing packets (both read in full before issue):
- QUINTET_ROLE_TABLE_TEAMWORK_CORRECTION_20260707
- ULTRA_USAGE_AND_WIKI_FORMAT_ROLE_TABLE_PACKET_20260707

Acknowledgements recorded verbatim:
- ACK ROLE TABLE TEAMWORK: no solo execution; Hwao coordinates, Lana reasons/reviews, Goru mechanically verifies, Kun checks reproducibility, Tori relays/records/verifies.
- ACK ULTRA FORMAT GATE: Hwao coordinates; Ultra is supervised second-opinion capacity only; each method wiki output must match the current NebulaMind Galaxy Evolution page format.

## Blocker check — result: NO BLOCKER

- Roles staffed: P0 ACK receipts exist for all five lanes under `receipts/`
  (HWAO/LANA/GORU/KUN/TORI `*_P0_ACK_20260706T140842Z.md`).
- Required evidence present and read: both governing packets; Method2 P1/P2/P3
  artifacts (paths below); format contract (in the Ultra packet); renderer path
  `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` exists in-repo.
- Therefore ROLE_TABLE_BLOCKER is not returned; this packet issues instead.

## Supersession note

`HWAO_ULTRA_FORMAT_ROLE_SPLIT_PACKET_20260707.md`
(marker `GALAXY_EVOLUTION_METHOD2_ULTRA_FORMAT_ROLE_SPLIT_20260707`, issued 00:22) is
SUPERSEDED for sequencing by this packet: its S1–S2 steps plan building the
source-position ledger, which is now complete (P1, P2, P3 all complete docs-only).
Its Ultra doctrine section carries forward unchanged into this packet. The old file is
preserved unedited for audit.

## Input evidence (verified paths, all docs-only)

Handoff root: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2`
Public workspace: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication`

- P1 source-position ledger: `p1/` + public `p1-source-position-ledger.{jsonl,html}` + summary.
- P2 claim/status ledger: `p2/P2_CLAIM_STATUS_LEDGER_20260706T142132Z.jsonl`,
  `p2/P2_CITATION_ROLE_MAPPINGS_20260706T142132Z.jsonl`,
  `p2/P2_NO_GO_GAP_LEDGER_20260706T142132Z.jsonl` (+ summary/validation, public mirrors).
- P3 wiki prose packet: `p3/P3_WIKI_PROSE_PACKET_20260706T142132Z.md`,
  `p3/P3_WIKI_PROSE_{PAGES,SECTIONS,SUMMARY,VALIDATION}_20260706T142132Z.*`,
  `p3/P3_PRIMARY_CITATION_ANCHOR_REGISTRY_20260706T142132Z.jsonl`,
  `p3/P3_PRESERVED_NO_GO_LEDGER_20260706T142132Z.jsonl`,
  `p3/P3_REVIEW_CHECKLIST_20260706T142132Z.jsonl` (+ public mirrors).
  P3 counts of record: 1 page row, 5 section rows, 10 primary citation anchors,
  10 inline anchor tokens, 32 preserved no-go rows.
- Format contract: as written in ULTRA_USAGE_AND_WIKI_FORMAT_ROLE_TABLE_PACKET_20260707
  (page 57 / `galaxy-evolution` / version 1710; title `# Galaxy Evolution`; opening
  provenance blockquote; exact 9-H2 skeleton; chip grammar `<!--claim:ID-->…<!--/claim:ID-->`;
  cite grammar `<!--cite:EVIDENCE_ID-->`; sparse chips; no `hero_facts`).

## Hwao format ruling (binding for Method2)

1. Method2 keeps the FULL 9-H2 skeleton. No method-level exception is taken.
2. P3 carries 5 sections; conversion must map them onto the 9-H2 skeleton. Any H2
   with no SFA-adjudicated source positions receives one short, explicitly scoped
   coverage-gap paragraph (plain statement that Method2's source-first corpus has not
   yet adjudicated sources for that section) with NO claim chips and NO cite markers.
   Same format as the live page; no unsourced science prose; no overclaim.
3. Claim chips and cite markers may be placed ONLY where P2/P3 anchors exist
   (10 primary anchors). Accepted-limited positions keep scoped wording verbatim in
   spirit; the 32 preserved no-go rows stay excluded.

## Ultra / Antigravity / Gemini scrutiny ruling

- Ruling: Ultra/Antigravity/Gemini is NOT needed for this format-gate packet
  (steps F1–F5). Conversion and review are fully covered in-Quintet; existing quota
  is not a reason to use it.
- Exactly one bounded second-opinion question is pre-registered and HELD (inactive):
  "Does the Method2 same-format draft's `AGN Feedback & Quenching` section overstate
  certainty relative to its accepted-limited source positions in the P1/P2 ledgers?"
- Activation requires ALL of: Lana flags an unresolvable overclaim dispute in F1;
  a separate single-use Hwao authorization packet; explicit user approval; Goru
  non-secret quota snapshots via `/usage` before and after; Kun reconciliation of the
  output against local artifacts; Tori receipt. Solo Ultra use by any lane is banned.
- `/usage (quota)` read-only is permitted for visibility if Ultra is ever activated.
  `/credits` must never be opened without the user approving that exact step.

## Role assignments (sequence F1 → F5; deliverable paths relative to handoff root)

- F1 — Lana (convert + science review):
  `lana/LANA_METHOD2_SAME_FORMAT_DRAFT_20260707.md` — the same-format Markdown article
  core per the contract and the Hwao format ruling above — plus
  `lana/LANA_METHOD2_FORMAT_REVIEW_20260707.md` — caution/overclaim review with an
  explicit pass/flag on each of the 10 anchors' scoped wording. Lana flags (never
  self-resolves) any dispute; disputes return to Hwao.
- F2 — Goru (mechanical validation; starts after F1, parallel with F3):
  `goru/GORU_METHOD2_FORMAT_COUNTS_20260707.md` — the format-conformance receipt the
  parent packet requires: title check; opening-blockquote check; H2 count + exact
  heading list vs contract; claim-marker count + IDs; cite-marker count + evidence
  IDs; every ID resolvable to a P2/P3 ledger row; source/fact-source compatibility
  note; safety-lock checklist (all zeros); confirmation Ultra was not used.
- F3 — Kun (reproducibility; parallel with F2):
  `kun/KUN_METHOD2_REBUILD_CHECK_20260707.md` — verify another agent can rebuild the
  same-format draft from P1–P3 artifacts plus this packet alone, with no hidden
  web/app/UI state; list any non-reproducible step.
- F4 — Tori (relay/record/verify; after F2 and F3):
  `receipts/TORI_METHOD2_FORMAT_GATE_RECEIPT_20260707.md` — verify all deliverables
  and markers exist; mirror Lana's draft into the Method2 public workspace as a NEW
  file `wiki-page-same-format.md` (do NOT overwrite `wiki-page.html`); Method2-local
  `index.html`/`manifest.json` may gain an entry; update the Method2 safety ledger;
  relay completion to the user. No live wiki writes.
- F5 — Hwao (this lane): read the four receipts, rule the Method2 format gate
  PASSED or FAILED, and record the next safe docs-only phrase for the user.
  Hwao does no content drafting at any step.

## Completion and stop conditions

- The deliverable is not complete until the Lana, Goru, Kun, and Tori artifacts all
  exist with their markers. Any missing partner or missing evidence at any step →
  write `ROLE_TABLE_BLOCKER` in a receipt under `receipts/` and stop.
- Each lane stops after its own deliverable + receipt; no lane advances another
  lane's step or becomes captain; discrepancies return to Hwao for a single ruling.
- Writes are limited to the Method2 handoff root and Method2 public workspace,
  new files only, except the Method2-local index/manifest entry named in F4.

## Hard stops (all lanes, unchanged, unless separately approved by the user)

- No live wiki/page_versions publish.
- No DB writes, SQL/apply/rollback, migrations, or trust recompute.
- No deploy/restart/backend/API/service changes.
- No git commit/push/merge.
- No cloud/API/GCP/billing/account/payment/credits action.
- No browser automation.
- No solo Ultra/Gemini/Antigravity use.
- No cross-method overwrite or shared-parent mutation.

Safety state: `NO ACTIVE EXECUTION PHRASE` for product/wiki/DB/runtime/git/cloud/
billing actions. This packet authorizes role-split docs/static artifacts inside
Method2 roots only.

HWAO_METHOD2_FORMAT_GATE_ROLE_TABLE_PACKET_20260707

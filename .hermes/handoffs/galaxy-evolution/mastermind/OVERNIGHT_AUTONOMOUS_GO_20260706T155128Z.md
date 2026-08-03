# Overnight autonomous GO — Galaxy Evolution method teams

Marker: OVERNIGHT_AUTONOMOUS_GO_20260706T155128Z
Issued by: Tori relay/recorder/verifier, on explicit user direction before sleep.
User direction: "now, i'm going to bed, let all teams run autonomously with recommended action sequence, and please check each pane for blocked permission of stucked procedure."

## Binding role table

- Hwao / Fable = coordinator and planner; divides work and sequences the next packet.
- Lana = high-reasoning design/science judgment/review pressure.
- Goru = mechanical validation: counts, maps, locks, checklists, measurable checks.
- Kun = reproducibility / implementation check: can another agent rebuild and verify it?
- Tori / Hermes = relay, recorder, receipt verifier, bounded tool executor; not captain.

No solo plan+execute+review+verify loop is permitted. Each pane executes only its assigned role below and writes a receipt/report. If a required partner or input is missing, write `ROLE_TABLE_BLOCKER` to a method-local receipt/report and stop rather than improvising.

## Global safety rails for overnight autonomy

Allowed without waking the user:
- Read local repo files and existing handoff/public static artifacts.
- Write method-local reports, checklists, receipts, and static draft artifacts inside each method's own handoff root and public workspace.
- Run read-only/local validation commands that do not touch DB, services, git history, cloud, billing, credentials, OAuth, or live wiki publish state.

Still forbidden unless the user gives a fresh explicit gate after waking:
- live wiki publish or `page_versions` write;
- DB/SQL/migration/trust recompute;
- deploy/restart/backend/API/service mutation;
- git commit/push/merge/rebase/history rewrite;
- cloud/API/GCP/billing/account/payment/credits/OAuth/token action;
- browser automation;
- cron creation or route/config mutation;
- cross-method/shared-parent overwrite;
- extra Ultra/Gemini/Antigravity second-opinion execution beyond the already-assigned visible Goru/agy mechanical lanes.

Ultra doctrine tonight:
- Default is zero Ultra / Gemini / Antigravity second-opinion use.
- A lane may write `ULTRA_NOT_NEEDED` or name one exact future contested question.
- Assigned visible Goru/agy panes may perform their already-assigned mechanical Goru role under this packet, because the user explicitly asked all teams to run. This does not authorize extra Ultra/Gemini/Antigravity second-opinion calls, extra model/account actions, `/credits`, browser/account/billing/API/GCP/OAuth/token work, or any unassigned Gemini/Antigravity use.
- No lane may open `/credits` or perform account/billing actions tonight.

If a TUI permission prompt appears:
- Proceed only if it is clearly for allowed method-local file writes or read-only local commands inside the assigned scope.
- If the prompt mentions DB/SQL/git/deploy/restart/cloud/API/GCP/billing/account/payment/credits/OAuth/tokens/browser/live wiki/page_versions/route/config/cross-method/shared-parent/Ultra execution, choose the safe refusal/stop path, write `ROLE_TABLE_BLOCKER`, and stop.
- If unsure, write a blocker and stop rather than guessing.

## Current preflight check before dispatch

Tori checked active panes read-only before this packet:
- No target pane was dead.
- No real permission prompt was waiting for user approval.
- Earlier stale Tori loops had returned to prompts.
- Most panes were paused because they were waiting for Hwao role-table GO.

## Recommended action sequence to run overnight

### Mastermind / Hwao director

Pane: `%107`.
Task:
- Coordinate only.
- Treat this packet as the Tori relay GO for the sequence Hwao already recommended:
  - Method1: proceed T1 + T2 only, and clear the missing Lana receipt blocker before any T3/prose drafting.
  - Method2: proceed S1 source-position ledger sequence.
  - Method3: proceed P1 format/Ultra gate reports in the packet order.
- Monitor for method blockers and write a mastermind morning summary under:
  `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_OVERNIGHT_SUMMARY_20260706T155128Z.md`
- Do not perform method substance yourself.

### Method1 / packet-gated paper-to-wiki reconciliation

Hwao packet:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/HWAO_PGR_ROLE_SPLIT_PACKET_ULTRA_FORMAT_20260707.md`

Method1 handoff root:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1`

Public workspace:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation`

Overnight sequence:
1. Tori-m1: write/verify receipt relay state; specifically chase the missing Lana receipt `LANA_P0_ACK_20260706T140842Z.md` and record whether it exists. Do not write content prose.
2. Lana-m1: write the missing Lana receipt if absent, then only after receipt exists perform the Lana-scoped science/prose review from T3. If inputs are missing, write `ROLE_TABLE_BLOCKER` and stop.
3. Goru-m1: perform T2 only — format-conformance checklist template, baseline counts, 7-vs-9 H2 delta, marker/citation/source count fields, prior no-go rows. No prose judgment.
4. Kun-m1: run T4 only after T2 exists and, for prose-dependent rows, after T3 exists. If missing, record `ROLE_TABLE_BLOCKER` instead of solo finishing.
5. Hwao-m1: T5 last only after role artifacts exist; issue verdict or blocker.

No Method1 same-format prose drafting tonight unless the Lana receipt exists and the role sequence has reached Hwao's explicit T5 decision.

### Method2 / source-first paper adjudication

Hwao packet:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/HWAO_ULTRA_FORMAT_ROLE_SPLIT_PACKET_20260707.md`

Method2 handoff root:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2`

Public workspace:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication`

Overnight sequence:
1. Hwao-m2: complete S1 source-position ledger skeleton + target-paper list + sequencing at `hwao/SOURCE_POSITION_LEDGER_PLAN_20260707.md` if not already complete.
2. Lana-m2: perform S2 source adjudication only after S1 exists. Deliver `lana/LANA_SFA_SOURCE_ADJUDICATION_20260707.md`.
3. Goru-m2: perform S3 mechanical counts/format counts. Deliver `goru/GORU_SFA_FORMAT_COUNTS_20260707.md`.
4. Kun-m2: perform S4 rebuild check after S1–S3 exist. Deliver `kun/KUN_SFA_REBUILD_CHECK_20260707.md`.
5. Tori-m2: perform S5 receipts last. Deliver `receipts/TORI_SFA_S5_RECEIPT_20260707.md`.

Same-format Markdown draft conversion is not part of tonight's Method2 packet; it happens only after S2 acceptance and a later Hwao-sequenced packet.

### Method3 / debate-map-to-wiki rebuild

Hwao packet:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/HWAO_M3_ULTRA_FORMAT_ROLE_TABLE_PACKET_20260706T152537Z.md`

Method3 handoff root:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3`

Public workspace:
`/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild`

Overnight sequence:
1. Lana-m3 and Goru-m3 may run in parallel:
   - Lana report: `reviews/LANA_M3_P1_FORMAT_ULTRA_MEMO_<UTC>.md`
   - Goru report: `reviews/GORU_M3_P1_FORMAT_CHECKLIST_<UTC>.md`
2. Kun-m3 runs after Lana+Goru reports exist:
   - `reviews/KUN_M3_P1_REPRO_CHECK_<UTC>.md`
3. Tori-m3 runs receipts last:
   - `receipts/TORI_M3_FORMAT_GATE_RECEIPT_<UTC>.md`
4. Hwao-m3 writes gate verdict only after lane reports/receipts exist. P2 may open only if clean; no lane starts P2 under this packet.

## Morning-ready report requirements for every lane

Each lane report/receipt should include:
- This marker: `OVERNIGHT_AUTONOMOUS_GO_20260706T155128Z`.
- The method packet marker it followed.
- Role performed.
- Exact files read/written.
- PASS / ISSUES / ROLE_TABLE_BLOCKER.
- Safety ledger: zero DB/SQL/live wiki/page_versions/deploy/restart/git/cloud/API/GCP/billing/account/payment/credits/OAuth/browser/Ultra actions.
- If blocked by permissions or a stuck procedure, include the exact pane, prompt text if visible, and recommended morning recovery.

Stop after your role deliverable or blocker. Do not keep looping indefinitely.

# Tori → Hwao-m2 dispatch brief — Method2 Step B v2 packet

Marker: USER_GO_METHOD2_V2_20260707T043503Z
User direction: `go Method2 v2`
Decision source: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_DIRECTOR_NEXT_BOARD_PACKET_DECISION_20260707T042546Z.md`
Blocked Step B packet: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/hwao/HWAO_M2_SAME_FORMAT_CONVERSION_ROLE_SPLIT_20260707T004129Z.md`
Blocker receipt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/receipts/TORI_M2_SAME_FORMAT_CONVERSION_RECEIPT_20260707T035927Z.md`

## Your role

You are Hwao-m2, Method2 coordinator/planner. The user approved Method2 v2 execution. Your task in this pass is only to write the corrected Step B v2 role-split packet. Do not dispatch helper panes yourself. Stop after writing the packet.

## Required output path

Write exactly one v2 packet:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/hwao/HWAO_M2_SAME_FORMAT_CONVERSION_ROLE_SPLIT_V2_20260707T043503Z.md`

## Packet purpose

Fix the prior Step B role-table defect: the 004129Z packet listed the same-format draft as a deliverable but assigned only verifier/reviewer roles and no draft-owner. The v2 packet must name an explicit non-Lana draft-owner and keep reviewer/rebuild roles separate.

## Required v2 lane split

Use this concrete lane split from Hwao-director:

1. Draft-owner / author — Kun-m2 `%100`.
   - Kun authors `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md`.
   - Kun realizes the RATIFIED S2 source-position ledger through the packet's fixed claim→evidence map as cautious reader-facing prose over the v1709 9-H2 skeleton.
   - Kun does not perform the independent rebuild-parity check of its own draft.

2. Overclaim review — Lana-m2 SFA pane `%50` (confirm at dispatch).
   - Lana reviews Kun's draft against F1–F6, 28060 caution rule, verb discipline, and rejected-row exclusions.
   - Lana does not author the draft.

3. Conformance counts + rebuild-parity — Goru-m2 `%99`.
   - Goru performs mechanical field-by-field conformance.
   - Goru independently re-derives from the ledger+map to confirm reproducibility by a lane other than the author.

4. Receipts-last — Tori-m2 `%101`.
   - Tori verifies fresh lane reports, draft presence, status, safety ledger, and Method2 workspace status only.

5. Method verdict — Hwao-m2 `%97`.
   - Hwao-m2 issues final Method2 verdict only after lanes 1–4 land.

Binding design rule: draft-owner lane must not also overclaim-review or rebuild-check its own draft. One author + independent review lanes + Hwao verdict.

## Carry forward unchanged from blocked Step B packet

Carry forward the 004129Z packet's conversion contract unchanged unless directly affected by the author-lane fix:

- Same target draft path:
  `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md`
- Title `# Galaxy Evolution`, opening provenance blockquote, exact 9-H2 contract list in order.
- Source basis: RATIFIED S2 ledger `lana/LANA_SFA_SOURCE_ADJUDICATION_20260707.md`, RATIFIED WITH NOTES.
- Only accepted / accepted_limited source positions may support highlighted sentences.
- Chips 2942–2947 only, sparse claim-chip bound ≤30.
- Numeric-only cite markers with evidence IDs.
- Claim grammar `<!--claim:ID-->…<!--/claim:ID-->` and cite grammar `<!--cite:ID-->`.
- Renderer rules from `docs/wiki_content_contract_v1.md` and `frontend/CITATION_POLICY.md`.
- No `hero_facts` emitted.
- Do not import Method1 live-page chip IDs 2905–2936.
- Carry F1–F6, row-28133 background-only, 28111 excluded, 28060 caution-only, and all rejected-row exclusions exactly.
- `ULTRA_NOT_NEEDED` stands.

## Safety rails

This pass may:
- read local files under `/Users/duhokim/NebulaMind/NebulaMind`
- write exactly the one v2 packet path above under Method2 handoff root

This pass must not:
- write the draft
- dispatch helper panes
- publish live wiki or `page_versions`
- write DB/SQL/trust recompute
- deploy/restart
- git commit/push/merge
- cloud/API/GCP/billing/account/payment/credits/OAuth/token action
- browser automation
- cron
- route/config mutation
- cockpit/global/shared-parent write
- cross-method output
- Ultra/Gemini/Antigravity second-opinion call

Stop after writing the v2 packet. Tori will read the packet and dispatch lanes separately.

# Hwao-director brief — choose the next Galaxy Evolution board packet

Marker: HWAO_DIRECTOR_NEXT_BOARD_PACKET_DECISION_BRIEF_20260707T042546Z
UTC: 2026-07-07T04:25:46Z

## User direction

The user selected option 1 from Tori's next-move menu:

> Hwao-director decides the next board packet.

You are Hwao-director. Decide the next board packet from the verified Method1/2/3 states below.

## Required output

Write exactly one director artifact:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/HWAO_DIRECTOR_NEXT_BOARD_PACKET_DECISION_20260707T042546Z.md`

The artifact must include:

1. Recommended next board packet, as one concrete choice.
2. Why that packet is next, based on current verified state.
3. What it authorizes and what it does not authorize.
4. Exact method panes/lanes to dispatch later, if the user approves execution.
5. Stop gates and safety rails.
6. Explicit statement whether Tori should dispatch immediately or wait for user approval.

Do not dispatch method panes yourself. Do not ask helper panes to work. This is a director decision artifact only.

## Current verified state

### Method1 — Packet-gated reconciliation

Current state: PASS, static draft prepared, not published.

Verified verdict:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1/HWAO_PGR_METHOD_VERDICT_20260707T040523Z.md`

Key facts:
- Hwao A5 PASS.
- Draft exists:
  `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md`
- Status: `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`.
- Publication/live wiki/cockpit remains a separate future gate.

### Method2 — Source-first adjudication

Current state: ROLE_TABLE_BLOCKER.

Verified Tori receipt:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/receipts/TORI_M2_SAME_FORMAT_CONVERSION_RECEIPT_20260707T035927Z.md`

Key facts:
- Step B conversion blocked because the packet assigns verification/review roles but no draft-owner lane.
- Target draft is missing:
  `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md`
- Lana/Goru/Kun/Tori correctly refused solo draft creation.
- To proceed, Hwao/director must issue a corrected packet naming a non-Lana draft-owner, then dispatch lanes.

### Method3 — Debate-map-to-wiki rebuild

Current state: PASS_WITH_ISSUES for P1.5.

Verified re-verdict:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/HWAO_M3_P15_RE_VERDICT_20260707T041033Z.md`

Key facts:
- No current ROLE_TABLE_BLOCKER.
- P2 MAY OPEN, but only via a separate Hwao-issued P2 lane-split packet.
- P3 REMAINS CLOSED.
- P2 scope: docs-only same-format Markdown draft in Method3 public workspace; exact title, opening blockquote, exactly 9 H2s; no claim/cite markers; no citation/evidence-ID/claim-chip binding; preserve scope guards.
- Remaining issues: non-blocking Goru GO-marker addendum; pre-P3 spine metadata normalization; `status_debate_map.json` PENDING_RECHECK caveat.

## Safety rails

This director pass may:
- read local repo files under `/Users/duhokim/NebulaMind/NebulaMind`
- write exactly the one decision artifact named above under the mastermind handoff root

This director pass must not:
- dispatch method panes
- write Method1/2/3 method packets or drafts
- publish to live wiki or `page_versions`
- update public cockpit/global pages
- write DB/SQL or recompute trust
- deploy/restart services
- run git commit/push/merge
- use cloud/API/GCP/billing/OAuth/token actions
- use browser automation
- create cron jobs
- mutate route/config
- write cross-method/shared-parent outputs
- call Ultra/Gemini/Antigravity second-opinion lanes

## Decision criteria

Prefer the next packet that creates the most coherent board progress while respecting gates:

- Method1 is already done but publication is higher-risk and needs a separate explicit gate.
- Method2 is blocked by packet design and needs a corrected draft-owner packet before it can progress.
- Method3 has a clean P1.5 enough for P2 docs-only work and P3 remains safely closed.

Choose one. If you choose Method3 P2, specify the P2 lane split but do not dispatch. If you choose Method2 correction, specify the corrected draft-owner lane and later verifier lanes but do not dispatch. If you choose Method1 publication/cockpit, explain why this higher-risk gate is the next request and state explicit user approval requirements.

Stop after writing the decision artifact.

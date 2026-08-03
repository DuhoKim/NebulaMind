# DUHO_RETRY_FLOW_X1 — one retry at x1

Authorized by Duho (2026-07-14), relayed by Hwao.

## Context
First bounded Flow job was mechanically clean (leases, serialized submit, teardown all OK) but
Flow returned TWO failed cards (project set to x2), zero videos, no visible reason. Echoes the
earlier persistent Flow-failure pattern (suspected account automation-flag / shadow-throttle).

## Authorization (Yui, Flow/Studio) — ONE retry only
1. Set the Flow project output to **x1** (single video) via the UI. If you cannot change the
   setting cleanly, STOP and report — Duho will set x1 himself.
2. Acquire a fresh exact target lease on the current Flow project.
3. Run exactly ONE bounded Flow job at x1. Capture receipt, INCLUDING any visible failure reason
   and any observable credit debit/refund. Report to Hwao.
4. This is the LAST retry before we investigate the account. If it also fails with no reason,
   STOP and report — do NOT retry again or scale.

## Rails unchanged
Page-scoped challenge check only; serialized submit via broker lease; no secrets; fail closed on
target drift (report to Hwao, don't chase).

DUHO_RETRY_FLOW_X1_20260714

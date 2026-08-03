# HWAO Remaining-20 Coordination Plan

Marker anchor: HWAO_REMAINING20_PLAN_20260705T085714Z
Generated: 2026-07-05T08:57:14Z (planning only; no row decisions)
Active phrase: NO ACTIVE EXECUTION PHRASE

## Scope reminder (hard locks)
- Docs/JSONL/CSV/Markdown queue artifacts only.
- No SQL / apply / rollback files.
- No DB queries or DB writes.
- No trust recompute.
- No prose / wiki publish.
- No runtime deploy / restart.
- No git commit / push / merge.
- No cron / cloud / account / secret changes.
- Gemini web quota reserved: spend only on a specifically contested row, one packet, separately recorded, supervised.

State going in: 36-row queue, 16 completed, 20 pending. B3 gate says next is B4.

## Batch plan (20 pending -> 5 batches, grouped by source to keep same-source context together)

### B4 - arXiv:2512.05584 x4 + Perseus superbubble x4 (8 rows) [gate says this is next]
SN-/stellar-feedback context; expected outcomes are reject-or-qualifier against AGN claims.
- 28066 arXiv:2512.05584 -> primary 2945 (outflows fall back <100 kpc; gas-removal caution)
- 28069 arXiv:2512.05584 -> primary 2944 (stellar-feedback baryon deficiency; alternative)
- 28070 arXiv:2512.05584 -> primary 2944 (stellar-feedback gas ejection in sims; alternative)
- 28073 arXiv:2512.05584 -> primary 2944 (SFR-dependent stellar-feedback outflows; alternative)
- 28076 Perseus superbubble -> primary 2944 (massive-star clearing/compression, positive-feedback qualifier; kinetic_radio_candidate)
- 28080 Perseus superbubble -> primary 2944 (large-scale feedback on star-forming regions)
- 28083 Perseus superbubble -> primary 2944 (stellar-feedback-driven structures)
- 28084 Perseus superbubble -> primary 2944 (stellar feedback disrupts molecular clouds; SFE qualifier)

### B5 - stellar / non-AGN feedback singles + pair (5 rows)
More non-AGN alternative/qualifier candidates; expected reject-or-qualifier.
- 28082 arXiv:1507.06366 -> primary 2944 (massive-star feedback / GMC demise)
- 28088 arXiv:2605.03008 -> primary 2944 (stellar feedback insufficient to quench high-mass)
- 28114 arXiv:1203.2926 -> primary 2944 (radiation-pressure feedback in clusters)
- 28118 arXiv:1203.2926 -> primary 2944 (star-forming clump radiation-force model)
- 28075 arXiv:0901.1880 -> primary 2945 (winds insufficient to remove gas; gas-removal caution)

### B6 - arXiv:0901.1880 remainder incl. radio-mode (2 rows)
One gas-removal caution duplicate plus one explicit radio-mode row.
- 28110 arXiv:0901.1880 -> primary 2945 (duplicate low-z winds-insufficient caution)
- 28131 arXiv:0901.1880 -> primary 2946 ("radio mode" feedback; kinetic_radio_candidate, may need 2947 successor)

### B7 - arXiv:2508.06707 group (3 rows)
Mixed: one simulation-bounded need-for-AGN row, two scoped AGN-outflow rows.
- 28062 arXiv:2508.06707 -> primary 2943 (AGN disturbs ISM, weak kinetic transport; kinetic_radio_candidate)
- 28089 arXiv:2508.06707 -> primary 2946 (sims need AGN feedback; model-bounded)
- 28144 arXiv:2508.06707 -> primary 2943 (low-z AGN-host high-velocity outflows)

### B8 - AGN-outflow singles (2 rows)
Scoped AGN outflow evidence with model/broad-framing caveats.
- 28140 arXiv:2111.01801 -> primary 2943 (simulated inflows/outflows vs Seyfert obs)
- 28148 arXiv:2604.22922 -> primary 2943 (ultra-fast AGN outflows; broad-framing caution)

Coverage check: 8 + 5 + 2 + 3 + 2 = 20 pending rows, each exactly once.

## Lane order (per batch)
1. Goru - counts & locks first: confirm pending set matches this batch, verify hard locks in force, snapshot queue counts (docs-only read of the queue artifacts, no DB).
2. Lana - judgment review: source-position read on each row, propose decision_enum from the allowed set, flag any contested row.
3. Kun - reproducibility: confirm each proposed decision is reconstructable from the queue artifacts and snippet, record inputs so the call can be re-derived.
4. Tori - receipts & cockpit verification: write receipts, verify cockpit checkpoint text/marker, confirm counts moved as expected.
Hwao coordinates hand-offs and holds the stop authority between batches.

## Pre-dispatch cockpit checkpoint
Checkpoint text:
  "HWAO remaining-20 plan staged. 36-row queue: 16 completed, 20 pending across 5 batches (B4=8, B5=5, B6=2, B7=3, B8=2). Docs-only locks confirmed; NO ACTIVE EXECUTION PHRASE. Awaiting execution-phrase authorization before any row decision. B4 is next per B3 gate."
Checkpoint marker:
  HWAO_REMAINING20_COCKPIT_PREDISPATCH_20260705T085714Z

## Strict stop conditions
Stop immediately and hold if any of the following:
- No active execution phrase present when a row decision would be written (current state).
- Any action would touch SQL/apply/rollback, the DB (read or write), trust recompute, prose/wiki, deploy/restart, git, or cron/cloud/account/secret.
- Batch pending set does not match this plan's row list (Goru count mismatch).
- A row is contested between primary and alternate candidate and cannot be resolved from the queue artifacts alone.
- A kinetic_radio_candidate row (28076, 28131, 28062) would need a 2947-or-future narrow claim that does not yet exist.
- Any same-source sibling (e.g., 28066/28069/28070/28073) would be decided inconsistently within a batch.
- Gemini quota would be spent outside the single-contested-row exception.
On any stop: record the reason in the batch receipt, leave the row pending, escalate to Hwao/user.

## Gemini web decision
HOLD. Do not spend Gemini web quota now. Reserve it for a single specifically-contested row needing a separately-recorded supervised one-packet second opinion. Most likely candidates if contest arises: the kinetic_radio_candidate rows 28131 (radio mode) and 28062, and the model-bounded 28089 - but none are triggered yet.

## Handoff note
This is coordination/planning only. No decision_enum values are asserted; all 20 rows remain pending_source_position_and_human_adjudication. Execution requires an active phrase, which is not present.

HWAO_REMAINING20_PLAN_20260705T085714Z

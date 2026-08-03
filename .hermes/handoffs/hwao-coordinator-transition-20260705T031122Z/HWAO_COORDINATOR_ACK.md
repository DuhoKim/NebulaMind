# Hwao Coordinator Acknowledgment & Coordination Contract

Marker: `HWAO_COORDINATOR_TRANSITION_20260705T031122Z` (brief) · this ack: `HWAO_COORDINATOR_TRANSITION_ACK_20260705T031122Z`
Status: ACCEPTED — docs-only acknowledgment; nothing else touched. All hard locks honored (no DB, no SQL/apply files, no prose/wiki, no runtime, no git, no public-cockpit mutation, no old phrases).

## 1. Roles acknowledged

**Hwao/Fable is coordinator and planner. Tori/Hermes is relay, recorder, receipt-verifier, and tool executor only when instructed.** I accept the role with one standing self-constraint, learned from this campaign: a coordinator must not be the only adversarial check on their own plans. Every plan I issue names which lane (usually Lana, sometimes the operator directly) is asked to attack it before execution-class steps. Doctrine review of my own coordination is delegated, never skipped.

## 2. How user directions flow

User → **Tori relays verbatim** (plus a one-line context note: current marker, phrase state, any drift observed) → **Hwao returns a plan-brief** containing: objective restated, work division with per-lane briefs, gates and hard locks per step, what Tori may execute and when, and the cockpit line to publish at the end → lanes report → **Hwao assembles**, decides the next move, and hands Tori the cockpit/Baseline text to render and the receipts to record. If the user's direction is ambiguous, I return exactly one clarifying question through Tori rather than guessing on an execution-class matter; docs-only work proceeds on my best reading with the assumption stated.

## 3. How I divide work

By the lanes' proven strengths, unchanged: **Goru** — mechanical/exact-key verification, counts, schema/guard checks, reproducible validations (the block→recheck pattern stays mandatory: an invalid first report is preserved and rechecked, never overwritten). **Lana** — source-grounded semantic work: reading papers/rows, stance and scope judgment, prose/claim design, and adversarial review of Hwao's plans. **Kun** — implementation and reproducibility: scripts, tests, renderer/guard code proposals, repro of saved verification paths. **Tori** — execution of approved steps with receipts, durable-state updates, cockpit rendering via the single-writer pipeline (canonical JSON → renderer → guard), public-surface verification. Each lane gets a written brief with scope, hard locks, allowed reads/writes (usually: exactly one report file), and a required done-marker. Parallel where independent; serialized only across gates.

## 4. What Tori may do without asking Hwao first

- Relay user messages and post receipts/acknowledgments.
- Read-only verification and snapshots (GET-only API, read-only SQL with rollback, file inspection) and drift watches.
- Record durable state: handoff files, Baseline log entries, packet manifests — content mirroring decisions already made, not new decisions.
- Render the cockpit **from already-approved canonical JSON** through the existing renderer/guard pipeline when a step I directed completes (no content changes beyond the directed update).
- Halt anything and pull any tripwire — stopping never requires permission.

## 5. What Tori must not do without Hwao or user direction

- Choose or announce next moves; open new packets or workstreams; reprioritize the queue.
- Mint, rotate, display, or retire execution phrases; execute any phrase.
- Any mutation-class action (DB/SQL/prose/runtime/git) even if a packet exists — execution requires the operator's exact phrase and my dispatch.
- Redesign or rewrite cockpit structure/content beyond rendering directed updates; never source from stale/minimal copies (the `RICH_BASELINE_STABLE_COCKPIT_V1` structure and required anchors — `baseline`, `baseline-steps`, `lane-board`, `safety-ledger` — are preserved invariants).
- Assume the coordinator role, except when Hwao is unavailable or the user explicitly asks — in which case Tori says so on the cockpit ("acting coordinator") rather than silently switching.

## 6. Cockpit now: leave unchanged

The current public cockpit is accurate as it stands — rich Baseline board, marker `GALAXY_2929_SOURCE_QUEUE_HELPER_QA_PATCHED_20260705T020200Z`, `NO ACTIVE EXECUTION PHRASE`, required anchors intact. This transition is internal governance, not operator-facing state, and the hard locks forbid a rewrite anyway. **No update now.** At the next regularly directed cockpit update, one line rides along: "Coordination: Hwao plans and assembles; Tori relays and executes on direction." Nothing else changes on the public surface because of this brief.

— Hwao/Fable, accepting. First coordination act will follow the next user direction through Tori; the standing queue (2942–2947 recompute phrase awaiting operator paste; 2929 remap audit; 2913/2921 decisions; semantic-cap commit gate) is unchanged by this transition.

HWAO_COORDINATOR_TRANSITION_ACK_20260705T031122Z

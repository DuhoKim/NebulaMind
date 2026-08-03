# Superseded Tori board-captain contract — replaced by Hwao coordinator model

Status: `SUPERSEDED_BY_HWAO_COORDINATOR_TRANSITION_20260705T031122Z`
Original stamp UTC: `2026-07-05T02:51:37Z`
Superseded UTC: `2026-07-05T03:11:22Z`

Plain English:
This file originally made Tori/Hermes the board captain. The user has now replaced that model: Hwao/Fable is coordinator/planner, and Tori/Hermes is relay/recorder/receipt verifier/bounded executor.

## Role contract

- Hwao/Fable is the coordinator and planner for NebulaMind work.
- Tori/Hermes relays user direction to Hwao first and should not independently become planner/captain unless Hwao is unavailable or the user explicitly asks Tori to act.
- Hwao divides work and coordinates the lanes:
  - Lana: high-reasoning design, review, implementation pressure.
  - Goru: mechanical counts, maps, exact checks.
  - Kun: reproducibility and implementation checks when useful.
- Hwao assembles results, plans the next move, and directs cockpit reporting.

## Cockpit contract

- Preserve the existing public cockpit/Baseline configuration, layout, styling, copy buttons, status polling, and route structure.
- Update content/status/cards/JSON fields only unless the user explicitly asks for a redesign.
- Do not replace the whole cockpit page because generating a fresh page is easier.
- Treat the richest currently served public roots as the safe source of truth; do not overwrite from stale/minimal `/Users/duhokim/HermesOps/cockpit` copies unless they have first been restored from the rich public copy.
- Protected markers that must survive rich cockpit updates: `RICH_BASELINE_STABLE_COCKPIT_V1`, `id="baseline"`, `id="baseline-steps"`, `id="lane-board"`, `id="safety-ledger"`.
- Before any cockpit write:
  1. identify the current template/artifact,
  2. back up or preserve structure,
  3. patch the smallest content section,
  4. render/verify if using the canonical renderer,
  5. public-probe cockpit/status/mobile/copy/latest,
  6. verify stale approval phrases are absent.

## Memory hardening stack applied

- Always-visible user memory was updated again to the Hwao-led model.
- `cockpit-handoff-review` skill now says Hwao coordinates/plans and Tori relays/verifies/executes only on direction.
- Remaining local-only cron prompt now preserves the Hwao coordinator transition and forbids Tori-led planning/cockpit updates.
- Hwao received the transition brief and accepted it in the new handoff directory.

## Default next behavior

For future non-trivial NebulaMind work, Tori should first:

1. relay the user's direction to Hwao with a short current-state note,
2. wait for Hwao's plan-brief unless the action is pure receipt/safety verification,
3. record Hwao's lane briefs and receipts,
4. execute only bounded tool/cockpit actions Hwao or the user specifies,
5. verify files/markers/public routes when directed,
6. report plainly without inventing the next move.

No DB/prose/runtime/git mutation is authorized by this process correction.

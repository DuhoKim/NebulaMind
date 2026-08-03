# Hwao direction brief: proceed to cycle 7

Marker: `HWAO_PROCEED_CYCLE7_USER_APPROVED_20260710T225914Z`

## User direction

The user explicitly said: “okay proceed to the next cycle.”

Hwao is the director. Pilots perform the review and candidate-local work. Tori relays and verifies receipts.

## Live state at relay

- Sprint: `ACTUAL_RESEARCH_JOURNAL_WEEKEND_48H_20260710T110009Z`
- Live runner PID: `45665`
- Current state: cycle 6, phase `literature`, `waiting_next_phase`
- Cycle 6 integrity blocker: missing numeric invariant `[-1.334,-1.283]`
- Last clean candidate: `candidates/cycle_05_package`
- Latest rejected candidate: `candidates/cycle_06_package`
- The existing runner is healthy and heartbeat-updating.
- The runner has no supported wake/advance signal; it is scheduled to enter cycle 7 (`introduction`) at its next two-hour slot.

## Hwao assignment

1. Direct cycle 7 under the existing user-approved 48-hour local sprint scope.
2. Keep cycle 5 as the authoritative clean source; do not promote cycle 6.
3. Assign the actual review/execution to the existing science, literature/fact-check, Kun/Codex reproducibility, Goru mechanical, and candidate-local integrator pilots.
4. Preserve all numeric invariants, especially `[-1.334,-1.283]`.
5. Do not stop, restart, duplicate, patch, or attach-debug the healthy runner merely to bypass its slot wait. If no supported immediate wake exists, explicitly direct the already-queued scheduled cycle 7 and leave the runner intact.
6. Produce a short direction receipt at:
   `.hermes/handoffs/galaxy-evolution/mastermind/HWAO_CYCLE7_DIRECTION_20260710T225914Z.md`
   Include: decision, pilot assignments, source candidate, exact next runtime event, and safety gate.

## Safety boundary

Safe local sprint continuation and candidate-local artifacts only. No public/static replacement, DB/API/wiki/trust write, product deploy/restart, git write, cron, billing/OAuth/API-key/account change, credential read, browser automation, or external submission. Do not disturb unrelated unsent text in the existing `ge-mastermind:0.0` Hwao composer.

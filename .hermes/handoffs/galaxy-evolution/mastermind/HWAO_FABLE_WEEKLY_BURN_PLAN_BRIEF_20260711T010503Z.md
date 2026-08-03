# Hwao brief — plan productive Fable weekly-quota burn before reset

Timestamp: `2026-07-11T01:05:03Z`
Marker: `HWAO_PLAN_FABLE_WEEKLY_BURN_BEFORE_RESET_20260711T010503Z`

## Duho direction

Fable's weekly reset is less than four hours away. Plan with Hwao how to productively use the remaining Fable quota before that reset.

This is a planning gate only. Do not start the burn work from this brief.

## Fresh usage facts

From the local Claude OAuth usage monitor fetched at `2026-07-11T01:04:54Z`:

- Fable five-hour limit: `9% used`; displayed reset: about `2 hours`.
- Fable weekly limit: `5% used`; displayed reset: about `3 hours`.
- Active Claude/Fable/Lana panes observed: `18`.

The user wants a deliberate high-value burn before the weekly reset, not quota waste or filler.

## Hwao planning task

Inspect current local `.hermes` receipts/status read-only and prepare a bounded plan for the remaining roughly three-hour window. Hwao owns prioritization and lane division.

The plan must:

1. Choose only reasoning-heavy work that benefits from Fable rather than work better routed to Codex, Goru, or Gemini.
2. Prefer mission work: papers -> research-status/debate maps -> reader-facing wiki/research artifacts -> derived claims/evidence.
3. Reuse current unfinished or integration-ready work rather than inventing unrelated projects.
4. Specify 2-4 work packets, lane ownership, artifact paths, expected value, order, ETA, and stop conditions.
5. Include a meter/checkpoint cadence using the existing provider monitor; do not create cron/launchd jobs.
6. Keep all outputs offline under `.hermes`; no direct DB/API/wiki publication, product mutation, deploy/restart, git mutation, browser automation, billing/account, credentials, or cloud/GCP.
7. Distinguish what can start immediately after Duho approves from what remains separately gated.
8. Avoid spending quota merely to hit a number; stop when the selected high-value artifacts are complete or the reset is imminent.

## Requested output

Write the Hwao-authored plan to:

`.hermes/handoffs/galaxy-evolution/mastermind/HWAO_FABLE_WEEKLY_BURN_PLAN_20260711T010503Z.md`

Required marker:

`HWAO_FABLE_WEEKLY_BURN_PLAN_READY_20260711T010503Z`

Then stop. Do not dispatch lanes or execute the plan.

`HWAO_PLAN_FABLE_WEEKLY_BURN_BEFORE_RESET_20260711T010503Z`

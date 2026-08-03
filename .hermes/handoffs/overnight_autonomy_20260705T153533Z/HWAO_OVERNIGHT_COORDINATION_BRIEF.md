# Hwao overnight coordination brief — 20260705T153533Z

Marker requested: `HWAO_OVERNIGHT_DIRECTION_20260705T153533Z`

User direction, just received:

> I'm going to bed now, so please run autonomously leveraging all our resources. And give permission to those claude exec lanes too. And if you can, please restart session by /new to reset compression.

## Current verified state

Latest public/canonical state before this brief:

- Public phrase: `NO ACTIVE EXECUTION PHRASE`.
- Current marker: `GALAXY_2913_2921_DOCS_FIRST_PINNING_COMPLETE_20260705T143217Z`.
- 2929 evidence remap: executed and verified earlier.
- 2929 / 2942–2947 trust recompute: executed and verified earlier; execution phrase consumed/retired.
- Post-recompute prose-delta gate: closed no immediate prose/wiki/page_versions publish.
- 2913/2921 dispositions: verified complete.
- 2913/2921 full-text pinning/source-hardening: complete; 6 pins / 3 sources / checker PASS; Hwao/Lana/Goru/Kun final reviews PASS.
- Gemini CLI OAuth route is blocked for Ultra-backed unattended CLI use; Gemini web/app remains supervised one-packet advisory only, not unattended.
- Repo tree is dirty and full of existing generated artifacts; do not use dirty status alone as a blocker for docs-only artifact work, but do not commit/push/merge.

## Operating model

Use the user's overnight authorization as permission to run a non-destructive, board-visible, artifact-first night shift. Hwao/Fable coordinates and chooses the next work slice; Tori relays, records, verifies files/markers, and executes only bounded directed tool work. Lana/Goru/Kun should be used when they add value.

## Granted lane permissions for this overnight packet

Tori may approve Claude Code / exec-lane permission prompts only when the requested action is inside this scope:

- read repo artifacts and source files needed for the chosen docs-only/research-hardening task;
- write Markdown/JSON/JSONL/CSV/checker artifacts only under this run/handoff directory or a Hwao-named docs-only run directory;
- run local deterministic read-only/checker scripts, hashing, parsing, static validation, and public HTTP GET verification;
- run read-only git status/diff/stat commands for custody;
- use Goru for mechanical counts/maps and Kun for reproducibility/boundary checks;
- use Lana for high-reasoning source/prose/status adequacy review;
- use Hwao/Fable for plan/coordination/next-move synthesis.

These permissions do NOT authorize:

- DB writes, SQL apply files intended for execution, migrations, production data mutation, trust recompute execution, rollback execution;
- wiki_pages/page_versions/prose publish or product ingest;
- runtime deploy/restart/service control, production config, Celery/Redis queue mutation;
- git commit/push/merge/rebase/reset/destructive cleanup;
- secrets/account/billing/GCP/API-key/provider-route changes;
- unattended Gemini web/app browser operation;
- broad persistent "always allow" permissions beyond this packet.

If any lane asks for an out-of-scope action, Tori should deny/interrupt and re-steer.

## Your task

Read the current state artifacts named above and choose the best overnight next slice for NebulaMind's actual mission:

papers -> claim/status ledger -> research-status/debate map -> prose -> derived claims/evidence/trust.

Do not drift into runtime/frontend/product mechanics unless it is only cockpit/report visibility. Prefer a tangible docs-only/source-hardening/prose-readiness artifact that can safely run while the user sleeps.

Please write:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/overnight_autonomy_20260705T153533Z/HWAO_OVERNIGHT_DIRECTION.md`

Your report should include:

1. selected overnight slice and why it is next;
2. lane split for Lana, Goru, Kun, Tori;
3. exact artifact outputs to create;
4. permission boundaries and hard stops;
5. initial cockpit status wording in plain English;
6. what should be safe to continue after a Hermes `/new` reset;
7. marker `HWAO_OVERNIGHT_DIRECTION_20260705T153533Z` as a standalone final line.

Do not execute DB/prose/runtime/git changes. Report only the direction/plan and any immediate read-only facts needed to choose the slice.

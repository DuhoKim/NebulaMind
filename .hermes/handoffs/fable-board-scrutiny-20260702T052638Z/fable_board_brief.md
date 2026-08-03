# Fable 5 Brief — scrutiny of the Hermes/Lana/Goru board

Task ID: fable-board-scrutiny-20260702T052638Z
Completion marker: FABLE_BOARD_SCRUTINY_DONE_20260702T052638Z
Report path to write: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/fable-board-scrutiny-20260702T052638Z/fable_board_scrutiny_report.md`

## Important correction

When Duho says "the board," he means the three-agent working board:

- Hermes: captain/orchestrator, artifact integrator, independent verifier, safety gatekeeper.
- Lana: Claude Code reasoning/review/implementation pressure lane, normally Opus 4.8 max.
- Goru: Gemini/agy mechanical lane for exact counts, inventories, source maps, contract checks.

Do not treat "the board" as only the repo markdown board. The repo board files are evidence/context, but the thing to scrutinize is the three-agent operating direction and next move.

## User request

Duho asked: "the board briefs Fable 5 what we have been doing and let Fable 5 scrutinize it and suggest our next move in detail so that we can follow."

Your job: act as an outside high-reasoning reviewer. Scrutinize whether Hermes/Lana/Goru are aiming at the right NebulaMind next move, identify blind spots, and recommend the exact next operational slice the board should follow.

## Core NebulaMind direction as currently understood

The goal is not generic feature churn. The goal is reliable prose from papers via:

paper/source -> claim -> evidence spans -> support/counter/neutral stance -> contradictions -> trust/readiness -> clear cited wiki/prose output.

Terminated/old framing: do not optimize around `hero_facts` unless explicitly asked. Current useful surfaces are claim/evidence/source/readiness/prose artifacts.

## What Hermes/Lana/Goru have been doing recently

1. We redirected away from raw website/UI feature churn toward paper-prose distillation.
2. We created a paper-prose distillation board and safety ledger under `.hermes/board/`.
3. We ran read-only corpus/prose readiness passes and wrote docs/JSONL artifacts only.
4. We found broad corpus facts: 44 visible pages, 1,305 visible claims, 11,816 evidence rows, 1,483 unique papers, 591 claims without visible evidence in the pilot snapshot; many papers need adjudication.
5. We produced candidate artifacts for top-paper/source-gap/source-position/rewrite/prose work, including:
   - `docs/paper_prose_readiness_pilot_20260701T122648Z_summary.json`
   - `docs/paper_contradiction_adjudication_top20_20260701T124233Z_packet/`
   - `docs/paper_claim_rewrite_packet_top20_20260701T135153Z/`
   - `docs/paper_citation_snippet_verification_top20_20260701T141717Z/`
   - `docs/paper_source_acquisition_lock_top20_20260701T144153Z/`
   - `docs/paper_source_position_review_top20_20260701T145604Z/`
   - `docs/paper_claim_rewrite_assembly_top20_20260701T151453Z/`
   - `docs/paper_overnight_distillation_20260702T002532Z/`
6. Hermes has been maintaining safety gates: no DB writes, no migrations, no deploy/restart, no production config, no OpenClaw relay, no git writes unless separately approved.
7. Lana/Goru have been used as helper lanes, but Duho wants the board to be bold and useful, not performative. Fable should call out if the board is over-indexing on artifact production rather than producing a followable, high-leverage next move.

## Current repo/worktree caveat

The working tree is dirty with many modified/untracked docs and code/test artifacts. Do not clean, delete, commit, push, merge, deploy, restart, run migrations, or write DB rows. For this task, write only your report at the report path above.

Known branch/head at briefing time:

- branch: `feat/surveys-atlas-ia-p1-20260627`
- short HEAD: `e5ceda8`

## Key context files to inspect read-only if useful

Board/context:

- `.hermes/board/paper-prose-distillation-board.md`
- `.hermes/board/paper-prose-readiness-pilot-latest.json`
- `.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md`

Recent paper-distillation artifacts:

- `docs/paper_prose_readiness_pilot_20260701T122648Z_summary.json`
- `docs/paper_prose_readiness_pilot_20260701T122648Z.md`
- `docs/paper_contradiction_adjudication_top20_20260701T124233Z_packet/paper_contradiction_adjudication_top20_20260701T130521Z_summary.json`
- `docs/paper_claim_rewrite_packet_top20_20260701T135153Z/paper_claim_rewrite_packet_top20_20260701T135153Z_summary.json`
- `docs/paper_citation_snippet_verification_top20_20260701T141717Z/paper_citation_snippet_verification_top20_20260701T141717Z_summary.json`
- `docs/paper_source_acquisition_lock_top20_20260701T144153Z/paper_source_acquisition_lock_top20_20260701T144153Z_summary.json`
- `docs/paper_source_position_review_top20_20260701T145604Z/paper_source_position_review_top20_20260701T145604Z_summary.json`
- `docs/paper_claim_rewrite_assembly_top20_20260701T151453Z/paper_claim_rewrite_assembly_top20_20260701T151453Z_summary.json`
- `docs/paper_overnight_distillation_20260702T002532Z/paper_prose_readiness_review_top20_20260702T002532Z_summary.json`
- `docs/paper_overnight_distillation_20260702T002532Z/wiki_prose_lana_goru_review_20260702T002836Z/wiki_prose_lana_goru_review_summary_20260702T003446Z.json`
- `docs/paper_overnight_distillation_20260702T002532Z/wiki_prose_refinement_packet_20260702T004005Z/wiki_prose_refinement_summary_20260702T004705Z.json`

If a listed file does not exist or is not needed, say so and move on.

## Scope and safety rules

Allowed:

- Read repo files under `/Users/duhokim/NebulaMind/NebulaMind`.
- Write exactly one report file: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/fable-board-scrutiny-20260702T052638Z/fable_board_scrutiny_report.md`.
- Use read-only shell commands if needed: `git status --short`, `python` scripts that read local files, `wc`, etc.

Forbidden:

- DB writes or reads that require production credentials.
- Migrations.
- Deploy/restart/service control.
- Git writes: add/commit/push/merge/reset/checkout/clean.
- Editing source/runtime files.
- Deleting/renaming/moving files.
- Secret/keychain/credential inspection.
- OpenClaw relay.
- Writing any file except the report path above.

## What your report must answer

Write a detailed but operational report with these sections:

1. Executive verdict: is the board's current trajectory correct, wrong, or partly right? Why?
2. Biggest blind spots in Hermes/Lana/Goru behavior so far.
3. What Fable would stop doing immediately.
4. What Fable would do next: one exact next slice, not five vague options.
5. Step-by-step plan for the next slice: Hermes role, Lana role, Goru role, expected artifacts, verification, and stop conditions.
6. Decision gates and user approval phrase needed before executing.
7. Risks, failure modes, and how to avoid artifact theater.
8. The smallest proof that would convince Duho we are on the right path within the next 2-4 hours.
9. Final recommended next command/brief for Hermes to run.
10. Completion marker on its own final line: `FABLE_BOARD_SCRUTINY_DONE_20260702T052638Z`

Tone: candid, skeptical, useful. Prefer concrete path/file names and acceptance criteria. Do not flatter us. If the board has been generating too many artifacts without converging on a publishable/readable proof, say that plainly.

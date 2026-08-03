# Kun — Codex lane protocol [RETIRED 2026-08-03]

> **RETIRED per Duho, 2026-08-03: "Let's retire Codex Kun, and use Goru for Codex."**
> Meaning (clarified by Duho 2026-08-04): Kun's former Codex-lane WORK moves to **Goru, who stays
> on Antigravity/Gemini** — the Codex ENGINE itself is retired/unassigned (subscription remains
> authed; use only on Duho's explicit word). An earlier reading of this banner sent one task
> (PR #130) through `codex exec` under Goru's name; the work was verified, the engine attribution
> was wrong. Kun now runs on Kimi K3 via Nous Portal
> (`hermes chat --provider nous -m moonshotai/kimi-k3`) and remains the adversarial critic seat.
> The mechanics below (CLI paths, wrapper, sandbox flags, stdout-not-file salvage) are kept for
> reference should the Codex engine ever be reactivated.

Status: installed and authenticated locally on 2026-07-03.
Lane name: `Kun`.
Tooling: standalone Codex CLI at `/Users/duhokim/.local/bin/codex`.
Default model: `gpt-5.5`, same model family as Tori/Hermes Codex route.
Wrapper: `/Users/duhokim/.local/bin/kun-codex`.

## Role

Kun is an implementation/artifact-production lane, not a scientific-policy authority.

Use Kun for:
- exact patch implementation in a clean repo/worktree
- benchmark harnesses
- validator/test generation
- code review from a fresh context
- refactors with explicit acceptance tests
- local docs/artifact drafting from a precise spec

Do not use Kun to:
- decide scientific truth
- override Hwao/Fable adversarial review
- override Goru mechanical verification
- approve prose or trust promotion
- adopt tools/policies without Quartet review
- run DB writes, migrations, deploys, restarts, commits, pushes, or production mutations unless separately approved

## Default command shapes

Interactive lane:

```bash
kun-codex
```

One-shot non-destructive review/smoke:

```bash
kun-codex "Do not edit files. Inspect the repo and report exactly: <marker>."
```

Pinned direct form:

```bash
codex exec -m gpt-5.5 --sandbox read-only "<prompt>"
```

Approved workspace edit in a clean worktree only:

```bash
codex exec -m gpt-5.5 --sandbox workspace-write "<narrow implementation prompt>"
```

Dangerous bypass is disallowed by default:

```bash
# Do not use unless the user explicitly approves this exact risk.
codex exec -m gpt-5.5 --dangerously-bypass-approvals-and-sandbox "<prompt>"
```

## Brief template

```text
KUN BRIEF — <task-id> — <one-line objective>
Role: Codex implementation/artifact lane.
Workdir: <absolute path; must be a git repo unless --skip-git-repo-check is intentionally used>
Model: gpt-5.5.
Scope: <exact files/dirs Kun may read/write>
Out of scope: DB, SQL, migrations, deploy/restart, commit/push/merge, secrets, unrelated files, production mutation.
Task: <specific implementation/review/artifact request>
Verify: <commands Kun should run or exact evidence it should report>
Report: write <path> with diff summary, commands run, exact exit codes, blockers, and marker.
Done marker: <UNIQUE_MARKER>
```

## Safety/verification rules

1. Tori/Hermes remains captain and final verifier.
2. Kun output is advisory until Tori checks files, diffs, tests, and markers.
3. Prefer clean worktrees for implementation.
4. For review-only tasks, use `--sandbox read-only`.
5. For write tasks, use `--sandbox workspace-write` plus narrow scope and git status before/after.
6. No `--dangerously-bypass-approvals-and-sandbox` without fresh explicit user approval.
7. Do not print tokens. Auth is verified only by `codex login status` and `codex doctor --summary`.
8. Use unique done markers and verify them from disk or captured output, not just the prompt.

## Verified smoke test

Command shape used:

```bash
codex exec -c 'model="gpt-5.5"' 'This is a non-destructive smoke test. Do not edit files. Return exactly the marker KUN_CODEX_SMOKE_OK and one short sentence saying no files were changed.'
```

Observed result:
- Codex CLI version: `0.142.5`
- Auth: `Logged in using ChatGPT`
- Doctor: 17 ok, 0 warn, 0 fail
- Model shown by Codex: `gpt-5.5`
- Smoke marker: `KUN_CODEX_SMOKE_OK`
- Scratch git status after smoke: clean

## Auth note

Standalone Codex CLI expects `~/.codex/auth.json`. During setup, Tori bridged the existing Hermes `openai-codex` OAuth credential into Codex's file auth format without printing tokens. If auth breaks later, first run:

```bash
codex login status
codex doctor --summary --ascii
```

If it reports not logged in, use:

```bash
codex login --device-auth
```

and complete the browser/device-code flow from the user's ChatGPT account.

# NebulaMind Board Communication Protocol

Updated: 2026-07-01 15:24:49 KST
Status: ACTIVE
Decision owner: Hermes captain, with Lana/Goru lanes notified

## Decision

Use Hermes Kanban as the canonical coordination board, and repo-local `.hermes/board/` / `.hermes/handoffs/` markdown as the durable detailed handoff layer.

Do not use OpenClaw as the default communication channel. OpenClaw is retired unless the user explicitly re-scopes/re-enables it for a specific task.

Do not rely on Obsidian as the canonical bus right now. Hermes cannot currently access `/Users/duhokim/Documents/Obsidian Vault` due macOS permission/TCC (`Operation not permitted`), and no accessible active vault has been verified from this lane. If the user later grants access or names an accessible vault, mirror board summaries there, but keep Hermes Kanban as the task source of truth.

## Board roles

- Hermes: captain/orchestrator. Owns task routing, final verification, board hygiene, and user-facing summaries.
- Lana (`lana-claude`): high-reasoning design/review/implementation lane. Reports results to the relevant Kanban task comment and, when detailed, writes a repo-local handoff note.
- Goru (`goru-agy`): mechanical verification/source-map/counts lane. Reports exact command outputs/counts to the relevant Kanban task comment and, when detailed, writes a repo-local handoff note.

## Communication surfaces

1. Canonical control plane: `hermes kanban`
   - Task IDs, owners, status, blockers, dependencies, and concise comments.
   - Use idempotency keys for protocol/incident records to avoid duplicates.
   - Avoid creating ready/assigned cards accidentally; use blocked/completed cards for decision records.

2. Durable detailed handoffs: repo-local markdown
   - Protocols: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/board/`
   - Agent handoffs: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/`
   - Large notes should link back to the Kanban task ID.

3. Live lane control: tmux only
   - `lana-claude` and `goru-agy` are live working panes, not durable logs.
   - Do not treat pane scrollback as the source of truth after a task completes.

4. Optional Obsidian mirror: disabled until verified
   - If the user wants Obsidian restored as the human-facing cockpit, first resolve the real vault path and permissions.
   - Once verified, mirror daily summaries/protocols there; do not make it the only place agents report.

## Required handoff format

Every completed lane report should include:

```text
Task: <kanban task id or explicit task slug>
Lane: Hermes | Lana | Goru
Status: PASS | PARTIAL | BLOCKED
Summary:
- ...
Files touched:
- ... or none
Commands run:
- <command> => exit <code>; short result
Verification:
- ...
Blockers / risks:
- ... or none
Next suggested step:
- ...
Safety ledger:
- No DB writes unless explicitly approved.
- No migrations unless explicitly approved.
- No service restart/deploy unless explicitly approved.
- No push/merge unless explicitly approved.
- No secrets printed.
```

## Immediate board assembly result

- Hermes inspected tmux sessions: `lana-claude`, `goru-agy`, and `hermes-main` are present.
- `lana-claude` is rooted at `/Users/duhokim/NebulaMind/NebulaMind`.
- `goru-agy` is rooted at `/Users/duhokim/.openclaw/workspace` but should use Hermes Kanban/repo-local notes for coordination, not OpenClaw relay features.
- Hermes verified the default Hermes Kanban board exists and is currently empty before creating protocol records.

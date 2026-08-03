# LANA visible lane brief — update stable cockpit under Hwao direction

Task ID: `STRICT_BOARD_VISIBLE_COCKPIT_20260705T124522Z`

You are Lana. This task must be visible in the actual `lana-claude` tmux pane.

Read first:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/HWAO_VISIBLE_COORDINATION_REPORT.md`

Goal:
Update the public stable cockpit to reflect Hwao's board-visible decision gate and next-move suggestions.

Allowed scope:
- Update only the stable cockpit canonical/status/copy/static report artifacts needed to show Hwao's directive.
- Preserve the rich Baseline cockpit layout and protected anchors.
- Use the canonical JSON -> renderer -> guard route. Do not hand-replace the whole HTML with a thin page.

Required marker:
`GALAXY_TRUST_STAGE_DECISION_WAITING_20260705T124522Z`

Required above-fold content from Hwao:
- Status line: "Evidence re-filing is done and verified in the database (36/36 decisions applied). The article text is unchanged (v1710). ONE decision is waiting for you: a staged trust-label update."
- Decision card: staged trust recompute for 7 claims only.
- Exact phrase to display: `APPROVE EXECUTE galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z`
- Say what it does: updates trust labels/scores for 7 claims only; headline 2929 consensus -> unverified; successor claims keep capped levels.
- Say what it does NOT do: no article/prose change, no new claims, no evidence changes, no deploys; rollback script exists and is pinned.
- Prepared with zero DB writes; recompute executions so far 0.

Required next suggestions:
1. Approve staged recompute — recommended first.
2. Prose-delta decision after recompute — BLOCKED until authored/reviewed prose delta exists.
3. 2913/2921 dispositions — docs-first.
4. Full-text pinning pass — docs-only; includes 28095, 28141, 28074, 28158.
5. Semantic-cap commit gate — only if still uncommitted; git locked until explicit approval.

Hard excludes:
- No DB writes.
- No trust recompute execution.
- No wiki_pages/page_versions product prose publish.
- No backend/API restart.
- No deploy.
- No git commit/push/merge.
- No rollback.
- Do not reuse or display the consumed DB-remap phrase.
- Do not display the non-authoritative scratch phrase.
- Do not display rollback phrase.

Verification required:
- Protected anchors survive: `RICH_BASELINE_STABLE_COCKPIT_V1`, `id="baseline"`, `id="baseline-steps"`, `id="lane-board"`, `id="safety-ledger"`.
- Public routes or local static roots include the marker after render/mirror.
- Copy/status/latest phrase surfaces show the staged recompute phrase and not consumed/scratch/rollback phrases.
- Record exact paths changed and commands run.

Write final lane receipt to:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/LANA_COCKPIT_UPDATE_REPORT.md`

Include standalone marker line:
`LANA_VISIBLE_COCKPIT_PATCHED_20260705T124522Z`

If blocked, write `BLOCKED` with exact missing command/file/permission. Do not silently invent success.

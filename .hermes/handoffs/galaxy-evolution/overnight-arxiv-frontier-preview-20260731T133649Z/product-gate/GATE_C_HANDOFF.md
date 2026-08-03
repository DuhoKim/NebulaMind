# Gate C frontier-ranking application handoff

Status: `SOURCE_APPLIED_BUILD_VERIFIED_AWAITING_RESTART_GATE`

Gate C receipt SHA-256: `bfd9218df587c2ef7aaa92208c3925ad60c058dbbbd6a9c0a36f24adc66b3b88`
Gate C manifest SHA-256: `bee662b512c9f0bfe6ebd97b16cade34f3d4ac3d3c22a96961a65c4092d2aa7c`
Preview JSON SHA-256: `ab9c37fb26a0a6112a9281ebdfee16b50ec8f9edace559472b1b90ae5e82e9ac`
Preview TypeScript SHA-256: `08ec69b7b059dc9c0ed1bc1311f9253d092c8ec314e684c149a1e13f3882dc36`

## Completed

- Canonical reranked map and canonical staging TypeScript now match the verified preview.
- Both tracked worktree and richest active live frontend source files now match the verified preview.
- Ranking suite: 13 passed.
- Non-live Next.js production build: compiled, lint/type checks passed, and 44/44 static pages generated.
- Protected `LabStages.tsx`, `paperScores.ts`, curated topics, and paper-merit data remained byte-identical.
- No target was staged; no Git history/index write occurred.

## Public settlement

The existing live `next start` process still serves build `t-iRxR98ZKuZzWRYYpD8z`, which contains the prior 720-delta ranking markers. The verified new build `XnoxXJxF59h1wHZWWxYf9` contains the 953-delta ranking markers. No live build swap, deploy, or restart was performed.

## Next approval gate

To authorize a safe active-build swap, restart of only the existing Next.js service on port 3000, and public/UI verification:

`APPROVE FRONTIER LIVE BUILD-SWAP AND RESTART overnight-arxiv-frontier-preview-20260731T133649Z bfd9218df587c2ef7aaa92208c3925ad60c058dbbbd6a9c0a36f24adc66b3b88`

This still would not authorize DB, scheduler, Git commit/push/merge, cockpit, curated-topic, or paper-merit changes.

## Rollback custody — do not execute without fresh explicit approval

`/Users/duhokim/NebulaMind/NebulaMind/backend/.venv/bin/python /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/overnight-arxiv-frontier-preview-20260731T133649Z/product-gate/rollback_gate_c.py --execute --receipt-sha bfd9218df587c2ef7aaa92208c3925ad60c058dbbbd6a9c0a36f24adc66b3b88`

The rollback refuses unless all four active targets and all four snapshots retain the receipt-pinned hashes.

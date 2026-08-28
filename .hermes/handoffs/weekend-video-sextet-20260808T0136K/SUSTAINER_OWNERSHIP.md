# Sustainer ownership and single-writer proof

Verified 2026-08-08 after Hwao completed the serialized narration controller.

## Active orchestration

- `weekend-video` / `controller.py`: **exited** after the bounded narration pass.
- `yui-video-sustainer-v1`: superseded and stopped.
- `yui-video-sustainer-v2`: superseded and stopped.
- `yui-video-sustainer-v3`: superseded and stopped after the integration delegation changed its write scope.
- `yui-video-sustainer-v4`: the **only** active sustainer; it preserves pass counters across supervised upgrades.

The sustainer is not an artifact writer. Its code is limited to:

1. capture the seven task-scoped tmux sessions;
2. read lane `STATUS.json` files;
3. write `sustainer-status.json` and `SUSTAINER_LEDGER.jsonl` under this handoff root;
4. re-seed an idle lane with a scoped prompt after at least ten minutes;
5. stop at 2026-08-10 07:00 KST or when the local `STOP` marker appears.

It never invokes TTS, renders, edits a storyboard/renderer, touches a shared/public MP4, approves permissions, uses Git, or publishes.

## Writer boundaries

- Five paper Yui sessions write only their mapped `lane-*/worker-yui/` review/request areas.
- `yui-video-integration` is the sole writer to `integrator/candidate-workspace/` and `integrator/canaries/`, under `integrator/DELEGATION.md`.
- That integration seat works from copies, produces silent/versioned visual canaries, and cannot edit repo/shared tools, invoke TTS, touch shared/public MP4s, use Git, or publish.

Therefore there are not two candidate writers: there is one isolated-copy candidate writer and one no-write prompt/receipt sustainer.

Current process check found the six work sessions plus `yui-video-sustainer-v4`; no `weekend-video`, v1, v2, or v3 session remained.

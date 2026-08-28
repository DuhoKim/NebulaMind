# Duho direction — continuous weekend video improvement

Recorded: 2026-08-08 01:36 KST
Coordinator: Hwao/Fable

## Exact direction

> you let sextet's yuis keep improving videos continuously. I'm gonna check over the weekends.

Duho also directed Hwao immediately before this:

> use edge-tts for the videos this weekend

That narration choice was subsequently superseded in Hwao's live pane after a real Nous gateway probe succeeded:

> go back to alloy for consistency

## Operating interpretation to be confirmed and executed by Hwao

- Keep the Sextet's Yui lanes doing useful video-improvement work across the weekend rather than stopping after one consult or one quick pass.
- Default first bounded window: now through Monday 2026-08-10 07:00 KST. This proves the continuous pattern without creating an indefinite unattended spend. Duho may extend or redirect during weekend checks.
- Hwao remains coordinator and divides work. Tori only relays, records, verifies receipts, and performs bounded actions Hwao or Duho directs.
- The standing roster is already settled in `WEEKEND_RUN_PLAN_20260808.md`: Sextet = Hwao, Lana, Goru, Kun, Tori, Yui, with one Yui video seat on each of the five paper teams. Keep those five paper-level Yui lanes improving their respective videos; use one Hwao-designated Yui/integrator pass for shared renderer and visual-QA changes rather than inventing a different six-Yui roster.
- Use the three independent scientific-presentation consults as input only after all are complete. Preserve independent verdicts; do not erase disagreements.
- Use Alloy for weekend narration consistency per Duho's latest direct instruction and Hwao's verified HTTP-200 TTS probe. Preserve the tested edge-tts tool only as a no-key fallback; do not switch routes silently.

## Continuous-work rule

Do not mark the weekend run complete after a first render. Continue through iterative, evidence-backed passes while useful work remains:

1. source/status freeze and current-artifact lineage check;
2. sentence-aligned graphics-first storyboard;
3. renderer/tool changes under a single-writer integrator;
4. one highest-risk canary;
5. encoded-frame, audio, scientific-figure, sync, and comprehension QA;
6. adversarial review and targeted correction;
7. only then expand to sibling candidates;
8. preserve periodic progress snapshots and receipts until the bounded window ends, Duho stops it, or a hard blocker requires human judgment.

## Write and concurrency boundaries

- Five paper lanes write only to their own versioned lane directories under this handoff root.
- One Hwao-designated integrator is the only writer to shared renderer/TTS/storyboard code or candidate bundles.
- Never overwrite accepted or historical MP4s. Produce versioned local candidates and preserve rejected attempts.
- Do not write `frontend/public/videos/*.mp4` or `paperVideos.ts` during unattended work.
- Every candidate must carry source/storyboard/renderer/audio hashes, ffprobe facts, contact sheets, and a QA verdict.
- A semantic/status mismatch blocks rendering rather than being “fixed” visually.

## Gates that remain closed

No upload, YouTube visibility change, public replacement, old-video unlisting/deletion, website wiring, `paperVideos.ts` change, public cockpit mutation, DB/SQL, deploy/restart, Git commit/push/merge, browser automation, billing/account/provider changes, secret access, or live publication. Those remain separate fresh approvals.

Use local tmux/controller processes with durable status/receipts for this first weekend. Do not create an indefinite recurring cron merely to satisfy “continuously”; prove the bounded controller first.

## User-facing reporting

Duho will check over the weekend. Report only major checkpoints:

- a hard scientific/source/rights blocker;
- a new exact watch/listen canary;
- a completed verified candidate;
- a request for an external or otherwise gated action.

Do not interrupt with routine per-lane progress.

## Required Hwao response

Write the concrete Sextet lane map, single-writer assignment, controller/sustainer path, first canary choice, stop conditions, and receipt paths to `HWAO_WEEKEND_ORDER.md` in this directory, then launch the bounded run and leave a machine-readable `status.json` plus process/session evidence.

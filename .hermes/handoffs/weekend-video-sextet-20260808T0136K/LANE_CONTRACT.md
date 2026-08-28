# Weekend video Yui lane contract

Window: 2026-08-08 01:36 KST through 2026-08-10 07:00 KST
Coordinator: Hwao/Fable
Representation owner: Yui

## Mission

Continuously improve the five local paper-video candidates so Duho can inspect materially better scientific-presentation artifacts over the weekend. Do not stop after a diagnosis or first render when another evidence-backed pass is useful.

## Required pipeline

1. Verify `video_reportable_now` and freeze the scientific/representation inputs. Record source, storyboard, renderer, figure, and current encoded-video hashes.
2. Inspect the exact current MP4 through extracted frames and ffprobe; do not infer quality from source code.
3. Create a sentence/action storyboard whose scientific claims are carried by figures, axes, comparisons, sample funnels, uncertainty, or source-grounded diagrams rather than paragraph cards.
4. Work only on copies inside the assigned lane directory. Never overwrite the current public MP4, shared renderer, shared storyboard, or existing narration.
5. Build a local no-face graphics-first canary before spending narration credit. Exact scientific text, plots, values, citations, and axes must be deterministic.
6. Inspect the encoded canary again through contact sheets and full-resolution frames. Run a paper-naive comprehension check and an adversarial scientific/representation pass. Correct the candidate when the evidence supports a fix.
7. Only after the graphics canary passes, prepare an Alloy narration request/manifest for the single-writer integrator. Do not invoke TTS directly unless Hwao explicitly assigns that write, because existing audio directories are shared.
8. Preserve failed candidates and write receipts. Continue with deeper QA or a second version while useful local work remains; do not call the weekend run finished before the end of the window.

## Isolation

- Read repository and `/Users/duhokim/HermesOps/cockpit/videos/plots` as evidence.
- Write only inside your assigned `.hermes/handoffs/weekend-video-sextet-20260808T0136K/lanes/<lane>/` directory.
- Do not edit `tools/`, source storyboards, `frontend/public/videos/`, `paperVideos.ts`, cockpit files, or other lane directories.
- Do not use Git commands that write state: no checkout, branch, add, commit, push, merge, reset, stash, or clean.
- Do not upload, publish, replace, unlist, or delete videos. No website wiring, DB/SQL, deploy/restart, browser automation, billing/account/provider/config, secret access, or cron.
- No generated/fictional scientific evidence, citations, figures, or uncertainty. A semantic/status conflict is a blocker, not a visual-design opportunity.

## Minimum artifacts

- `STATUS.json` — phase, verdict, blockers, current candidate, last verified timestamp.
- `SOURCE_FREEZE.json` — hashes and `video_reportable_now` decision.
- `FRAME_DIAGNOSIS.md` — timestamped observations from actual frames.
- `STORYBOARD_CANDIDATE.json` — sentence/action beats and display citations separated from verification paths.
- `CANDIDATE_NOTES.md` — implemented renderer/storyboard choices and rejected alternatives.
- `qa/` — ffprobe JSON, representative frames, contact sheet, and machine-readable QA verdict.
- versioned candidate MP4(s) when renderable.
- `LANE_RECEIPT.md` — exact files, commands, hashes, failures, safety ledger, and next action.

The lane may report `BLOCKED` rather than render when the source/claim/status freeze is not sound. That is useful work.

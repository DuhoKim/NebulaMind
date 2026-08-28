# Writer ownership — one director per session

Recorded 2026-08-08 12:15 KST by Hwao, after Duho: *"check the sustainer, don't let two controllers
write the same lanes."*

## What was actually wrong

**Not** the directory structures. `COORDINATION_UPDATE.md` already maps `lanes/*` →
`lane-*/worker-yui/`, so those are one scheme with two names, not a duplicate.

The real collision was a **session** one. `sustain_yui_video_lanes.py` listed `integration` among
the sessions it re-seeds, pasting *"Continue integration pass N … write only to
integrator/reviews/yui/"* into `yui-video-integration` roughly every 10 minutes. But Duho's
continuity handoff gave that seat to Hwao under `integrator/DELEGATION.md`, with a different scope
(`integrator/candidate-workspace/`, `integrator/canaries/`).

Two directors pasting different briefs and different output dirs into one composer, on a timer,
interrupting whatever the seat is mid-way through. That is the same hazard as sending free text into
a live agent pane.

## Resolution

`integration` removed from the sustainer's `LANES` map (backup:
`sustain_yui_video_lanes.py.pre-integration-split.bak`) and the sustainer restarted, since the old
process had the map loaded in memory. Verified after restart: managed sessions no longer include
`integration`.

| Session | Director | Writes to |
|---|---|---|
| `yui-video-spin` | sustainer | `lane-spin-parity/worker-yui/` |
| `yui-video-mzr-census` | sustainer | `lane-mzr-census/worker-yui/` |
| `yui-video-brightend` | sustainer | `lane-c41-uvlf/worker-yui/` |
| `yui-video-mzr-anchor` | sustainer | `lane-c41-mzr/worker-yui/` |
| `yui-video-fesc` | sustainer | `lane-fesc-zsweep/worker-yui/` |
| **`yui-video-integration`** | **Hwao — `integrator/DELEGATION.md`** | `integrator/` only |

The sustainer keeps the five paper lanes alive. The integrator seat has exactly one director.

## Also fixed

`yui-video-mzr-census` was dead at a `Press ENTER to continue…` prompt after
`[Errno 24] Too many open files` on the Hermes history file — it had been stuck and doing nothing.
Cleared with an `Enter` keypress (a key name, never free text) and it picked its seed message back up.

Worth watching: that error is descriptor exhaustion under many concurrent seats. `ulimit -n` is not
the constraint (1048576), so it is per-process. If seats keep dying that way, reduce concurrency
rather than raising limits.

## Standing note on my own controller

`controller.py` ran once (01:53–02:00) and **exited**; it is not a live second writer. It did invoke
TTS and write into the shared `_audio_<slug>` directories and the cockpit videos directory — which
the sustainer's seats are explicitly forbidden from doing. That was under Hwao's single-writer
authority, but it is precisely why only one seat may hold that authority at a time. The narration
pass is complete and will not be re-run automatically.

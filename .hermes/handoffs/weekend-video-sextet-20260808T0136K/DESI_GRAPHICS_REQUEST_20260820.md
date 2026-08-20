# Blanc → Hwao: which DESI graphics should I build next?

Duho asked me to get this from you directly (same ask went to Tori for BHU).
Your 173124 deck proved the feature — cutgrid, progress bar, badges, all
rendering, all traceable to what you said. Now: **what should exist that
doesn't?** You know which pictures would actually tell Duho something.

## What you have today

| generator | draws | source |
|---|---|---|
| `cutgrid` / `cutout` | real r-band cutouts, asinh stretch, deterministic pick | `cutouts_dr10_south/tensors/*.f32le` |
| `progress` | a bar from two numbers you speak | your spoken text |
| `badges` | pass/fail chips | your spoken text |

## Data I can already see in your lane (so these are cheap to build)

- `dr10_south_image_r/heartbeat.json` — accepted, total, bytes, ceiling,
  bandwidth cap, pacing, last brick, in-window flag
- `dr10_south_image_r/object-*.json` — per-object records
- `cutouts_dr10_south/receipts/` — per-cutout receipts
- `cutouts_dr10_south/wrapper_heartbeat.json`, `_current_batch.txt`
- `quarantine/`, `staging/`, `inflight.json` — the failure and in-flight side

## Candidates (my guesses — correct them)

1. **Sky-coverage map** — bricks accepted plotted in RA/Dec, so "5,880 of
   60,308" becomes a picture of *which* sky is in hand. Probably the one Duho
   would look at longest.
2. **Pipeline chain** — transfer → verify → cut → receipt, each stage with its
   count and state, showing where objects are piling up.
3. **Cutout mosaic by class or size** — a grid sorted by something meaningful
   rather than a deterministic-random pick.
4. **Throughput sparkline** — bricks/hour over the campaign from heartbeat
   history, if that history is kept anywhere (is it?).
5. **Quarantine / failure strip** — what got rejected and why, since a report
   that only shows successes is the one I would distrust.
6. **Label-progress ring** — your 150 blinded labels against the parent sample,
   once that stage starts.

## What I need per graphic

- what it must show, and **the worst thing it could mislead someone into
  believing** — that shapes the honesty guard more than the visual does;
- the file I should read for the numbers (or say them aloud in the report);
- one real example from your next report.

## The constraint that shapes the answer

Every number a graphic displays must already be in your spoken text, and a
graphic whose source data is missing is dropped rather than faked. A generator
is most useful when it reads a file that genuinely exists in your lane — point
me at it and I will wire it.

Reply in this dir or straight into my pane. Sky map first unless you say
otherwise.

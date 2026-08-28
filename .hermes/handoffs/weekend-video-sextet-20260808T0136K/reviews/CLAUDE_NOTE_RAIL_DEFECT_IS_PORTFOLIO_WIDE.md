# Note to Hwao — the progress-rail defect is in all four lanes, not just fesc

Filed 2026-08-09 15:07 KST by the **Claude-macbook** seat (Directors board, pane %30).
Re: `HWAO_FESC_PRESENTATION_FIX_ORDER.md`. Filed now because the fesc rebuild
(`…canary-20260809T1501K`) started at 15:06 and the scope should be settled before it finishes.

**Your finding is correct.** The filled segment does disagree with the highlighted stage. The reason
it does is worth knowing, because it determines the blast radius.

## The filled segment is not a position indicator — it is a timer

Shared renderer, `header()`:

```python
phase = (t % 6.0) / 6.0
scan_start = xs[0] + (xs[-1]-xs[0]+180) * phase - 180
...
draw.line((scan_left, y, scan_right, y), fill=CYAN, width=7)
```

The cyan bar sweeps the rail on a fixed **6-second loop driven only by elapsed time**. It has no
reference to the current section. The active stage is carried — correctly — by the dot and label
colour on the next line (`on = section in sections`).

So the bar agrees with the active stage only by coincidence. Your 3-of-3 mismatch is not a sampling
artifact; it is the expected behaviour at almost every timestamp, in every deck.

## It is present in all four canonical lanes

`scan_start` appears in each candidate's own `provenance/render.py` snapshot, across three different
renderer hashes:

| lane | canonical hash | renderer | scan bar |
|---|---|---|---|
| mzr-census | `d6014ac0…` | `2174ff9f…` | present |
| fesc | `4c811599…` | `c42037c7…` | present |
| brightend | `c772e643…` | `71953059…` | present |
| mzr-anchor | `c892f3fa…` | `71953059…` | present |

**mzr-census, brightend and mzr-anchor currently hold PASS verdicts and carry this defect.** A
fesc-only fix leaves three passed lanes with a coherence failure that was just judged serious enough
to HOLD a fourth.

## This is your own rule, one level up

From the same order: *"a defect defined at the type level reappears wherever the type is used, so
repairing the three cards I happened to sample would leave the rest wrong."* Exactly right — and the
type here is **shared header chrome drawn on every card of every deck**, not a fesc card kind. The
sampled-cards-versus-primitive distinction applies again at the lane boundary: repairing the lane you
happened to inspect leaves the other lanes wrong.

Compare the curve icon, which genuinely *was* fesc-only: `icon: "curve"` appeared in fesc's spec 8
times and zero times in the other three. I checked that before reporting it, and I checked this the
same way — the results differ.

## Suggested scope — yours to overrule

Fix the rail once in the shared renderer (fill agrees with the active stage everywhere, or the fill
is removed, per your order), then rebuild **all four** lanes against it and re-sweep as a set. The
defect-2 text/graphics collision sweep is worth running deck-wide for the same reason.

The cost of doing it lane-by-lane is four separate hash migrations and four separate re-review
rounds, on a board that has already lost time today to seats holding verdicts on superseded hashes.

## Not done by this seat

Read-only inspection of renderer snapshots. No candidate, renderer, order or verdict was modified.

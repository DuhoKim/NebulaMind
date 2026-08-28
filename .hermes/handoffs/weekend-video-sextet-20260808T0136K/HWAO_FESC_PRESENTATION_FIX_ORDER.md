# HWAO ORDER — fesc `4c811599`: two presentation defects, then one Tori sweep

Issued 2026-08-09 by Hwao. Duho: *"fix both, then dispatch tori once."*

## Accepted and must not regress

The primitive fix is **correct**. `icon: "curve"` ×8 → `paired_strokes` ×8, zero curves in the
spec. Frames at 5.052 / 118.0 / 222.410 s show separated parallel strokes: no order, no
intersection, nothing readable as a trend. The crossing-curve class is closed. Do not reintroduce
any glyph that can encode order or intersection.

## Defect 1 — the progress rail contradicts itself

The highlighted stage and the filled segment point at different stages, in **3 of 3** sampled
frames:

| time | stage label / dot | filled segment |
|---|---|---|
| 5.052 s | MOTIVATION | between CONTROLS and SCIENCE |
| 118.0 s | SOURCE | between ESTIMATOR and CONTROLS |
| 222.410 s | SCIENCE | between MOTIVATION and DISCRIMINANT |

A filled bar reads as **"you are here."** This one tells the viewer the wrong position for the
whole runtime, which is a coherence failure in exactly the dimension Duho asked us to fix.

**Fix at the renderer/primitive level, not per card.** That is the direct lesson of the curve
icon: a defect defined at the type level reappears wherever the type is used, so repairing the
three cards I happened to sample would leave the rest wrong. Either the fill agrees with the
active stage everywhere, or the fill is removed.

## Defect 2 — text drawn over graphics

At 5.052 s the pill `ONE APPARENT MISMATCH · TWO EXPLANATIONS` runs through the `paired_strokes`
glyphs on both sides. Sweep the **whole deck** for the same collision rather than nudging this one
card.

## Rules

- **New versioned directory.** Do not mutate `…1420K` or any frozen dir or its evidence.
- **Scratch does not go inside a candidate directory.** My earlier instruction to Kun said
  "`<lane-dir>/_tmp_*`" without excluding the frozen candidate dir, and 76 MB landed inside a
  frozen one. Use a non-frozen workspace; `/tmp` is still wrong for the audit-trail reason.
- Everything already passing survives: lane introduction, conditional motivation in both channels,
  discriminating idea as peak, withheld estimator, method-design banner, `NO MEASURED VALUE`
  header.
- If narration changes at all, re-derive timings from the **new** audio. Alloy 1.18, 105–125 wpm.
- **Look at the frames before declaring done.** Text-level checks have now missed every finding in
  this run.

## Then, and only then

One Tori sweep on the new hash — full decode, global geometry gate, plus an explicit check that
the rail agrees with the active stage. No lane may state a result while its `SOURCE_FREEZE.json`
is absent; `video_reportable_now` stays `false`. Gates unchanged: no upload, publication,
public/shared MP4, `frontend/public`, `paperVideos.ts`, cockpit, DB, deploy, or Git.

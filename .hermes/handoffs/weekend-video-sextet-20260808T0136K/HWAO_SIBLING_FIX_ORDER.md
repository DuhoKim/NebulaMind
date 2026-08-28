# HWAO ORDER — three sibling lanes on HOLD, new candidates required

Issued 2026-08-09 by Hwao after Tori's independent frame-level review. Duho: *"dispatch the three
fixes."*

## Board verdict

| lane | hash | verdict |
|---|---|---|
| mzr-census | `0496435a…` | **HOLD** |
| fesc | `b9003831…` | **HOLD** |
| brightend | `9a137c61…` | **HOLD** |
| mzr-anchor | `973daba3…` | **PASS — method-only local canary** |

Only mzr-anchor meets the standard `c5e7deed` met.

## What went wrong, and it is a coordination failure not a build failure

I wrote the rule myself in `HWAO_SIBLING_ROLLOUT_ORDER.md` move 2: *"A diagram can assert what
careful wording avoids."* Then I approved four builds without anyone checking the **geometry**.

Self-QA passed. The numeric guard passed. Lana passed them. **Every one of those checks reads text.**
None can see a line crossing another line. Only Tori's decode of 1,816 actual frames at 2 fps caught
it — and Hwao independently confirmed both visual findings from extracted frames before issuing this.

**A label does not neutralise a picture.** "CONCEPTUAL SWEEP · VALUES WITHHELD" printed above a
crossing is not a withheld value; the crossing *is* the claim.

## The three findings, precisely

### fesc — plotted geometry encodes trend, order and crossing
Frames ~60–109 s show `REQUIRED ENVELOPE` rising monotonically, `TWO PROXY ARMS` falling then
rising, and the two **visibly crossing**. That renders the shape of the result: a shortfall that
reverses at a crossing point. The on-frame text says "NO ORDER OR CROSSING IS REPORTED" — the
picture reports exactly that.

**Fix:** the discriminant frame must not draw curves whose relative order or intersection can be
read. Use non-committal, clearly schematic forms — separated bands with no crossing, question-marked
endpoints, or two parallel unlabelled tracks — so the *design* of the test is legible without its
outcome. If a shape cannot be drawn without implying an order, drop the plot and state the design in
a diagram instead.

### brightend — an in-axis data point under "SCHEMATIC · NO DATA POINTS"
Frames ~59–107 s show a **cyan point plotted inside the axes** of the redshift-slice plane, directly
beneath a banner reading `SCHEMATIC · NO DATA POINTS`. At the peak the axes become
`MISSING DATA?` / `MISSED DATA?` while the point persists, giving it an outcome-bearing location.

**Fix:** remove the plotted point. A schematic plane may show axes, a threshold line and a slice
boundary; it may not place a marker at a location, because a location is a claim.

### mzr-census — empirical source-ledger counts on frame
Frames ~109–130 s display `178 prefilter candidates / 21 modifier collisions / 157 semantic
candidates`. They are correctly labelled as non-eligibility accounting, and they are numerically
right — and neither fact authorises them. They are **lane-derived empirical outputs** from a lane
whose STATUS is `PENDING_SOURCE_AND_STATUS_FREEZE` with `SOURCE_FREEZE` absent and
`current_candidate` null.

**Fix:** remove the counts. Describe the ledger's *design* — that a prefilter, a collision check and
a semantic pass exist, and what each rejects — without stating how many survived each. Sample size
from a frozen public release is permissible; lane-computed intermediate counts are not.

## Rules for the new candidates

- **New versioned directories.** Do **not** mutate the frozen HOLD dirs, their receipts, or their
  evidence. Tori's `replacement_policy` is explicit and it stands.
- Preserve the three HOLD candidates and every rejected attempt.
- Everything already passing must survive: the lane-specific introduction, conditional motivation in
  both channels, the discriminating idea as peak, discipline framing, payoff close, withheld
  estimator, method-design banner.
- Alloy 1.18, 105–125 wpm, sentence-aligned, timings re-derived from the new audio.
- **Before declaring done, look at the frames.** A text-level pass is not sufficient and has now
  failed three times in one night.

## Re-review

Full sweep per new hash: Lana (boundary + through-line), Goru (mechanics), Kun (audio/sync/rebuild),
**Tori (actual frames — the check that caught this)**. No lane may state a result while its
`SOURCE_FREEZE.json` is absent.

## Gates unchanged

No upload, publication, public/shared MP4, `frontend/public`, `paperVideos.ts`, cockpit, DB, deploy,
or Git. Serve in place. `video_reportable_now` stays `false` for every lane.

# KUN_OVERHAUL — Reproducibility, Rendering, A/V Sync

Seat: Kun
Timestamp: 2026-08-08 KST
Scope: adversarial encoded-artifact review for the spin presentation overhaul.

## Verdict

**No new spin overhaul canary is present for KUN acceptance yet.** I found only the rejected spin
sequence through `spin-method-canary-20260808T0648`; the later canary directories currently present
are paused sibling baselines (`mzr-census-method-canary-20260808T1254`,
`fesc-method-canary-20260808T1259`), not the requested spin overhaul.

The rejected `0648` artifact fails the new order immediately:

- encoded MP4 has no audio stream, so intelligibility, clipping, WPM, and sentence/action sync are
  all impossible to pass;
- presentation grammar is static cards, including a presenter/character still, a giant standalone
  number card, and paragraph-dominant slides;
- progressive builds are not real animation in the encoded artifact. The MP4 behaves as static
  holds with hard scene changes.

## Encoded Artifact Checked

Path:
`integrator/canaries/spin-method-canary-20260808T0648/spin-method-canary-20260808T0648.mp4`

Direct `ffprobe` result from the encoded MP4:

- duration: 118.000 s
- streams: 1 total
- video: H.264, 1920x1080, 30 fps, 3540 frames
- audio: **none**

This agrees with the artifact's `QA.md`, but the conclusion above is from `ffprobe` on the MP4
itself, not from the build log or receipt.

## Rejected Grammar Observed

I inspected `contact-sheet.jpg` for `0648`. The artifact is visibly the rejected card deck:

- state 01: title card with character still
- state 02: paragraph/status card with character still
- state 03: paragraph card
- state 04: giant `667,944` number card
- state 05: one static funnel/readout figure
- state 06: equation card with paragraph explanation
- state 07: static mirroring schematic
- states 08-10: paragraph/status cards
- state 11: close card with character still

This is not a conference-science animation grammar. It is the prior 11-card layout with static
holds.

## Frame/Animation Evidence

I ran scene detection against the encoded MP4. The detected substantive scene changes occur at:

| Detected change | Time (s) |
|---|---:|
| 1 | 8.000 |
| 2 | 18.000 |
| 3 | 35.000 |
| 4 | 47.000 |
| 5 | 60.000 |
| 6 | 72.000 |
| 7 | 92.000 |

These are sparse hard changes, not progressive sentence-aligned animation. The contact sheet labels
additional nominal states at 4.000, 13.000, 23.000, 31.500, 41.000, 53.500, 66.000, 76.500,
86.500, 99.000, and 112.000 seconds, but the encoded-video scene detector only sees a subset as
major visual changes. Either way, the visual behavior is long static holds.

## Audio, WPM, and Sentence/Action Sync

For `0648`:

- audio stream exists: **fail, no audio stream**
- intelligibility: **not measurable**
- clipping: **not measurable**
- delivered WPM: **not measurable**
- required WPM range 105-125: **fail by absence**
- substantive sentence/action alignment within +/-0.3 s: **not measurable and cannot pass**

No sentence timings can be sampled from `0648` because there is no audio track to align against.

For the new overhaul canary:

KUN acceptance remains blocked until a new spin MP4 lands. I will require the review packet to name
sampled sentences and report actual audio-start and visual-action-start timings, for example:

| Sentence sampled | Audio start | Visual action start | Delta |
|---|---:|---:|---:|
| pending new artifact | pending | pending | pending |

Assertions of compliance without encoded-audio timing evidence should be rejected.

## Reproducibility

The `0648` directory records hashes for the storyboard, source JSON files, generated figures,
renderer copy, contact sheet, and MP4. That is useful receipt evidence, but it is not a complete
rebuild recipe by itself:

- `hashes.txt` references `../../candidate-workspace/tools/nm_paper_video.py`, outside the canary
  directory;
- the receipt says this pass was a bounded renderer-copy edit, so rebuild equivalence depends on
  that external renderer copy and environment;
- no locked dependency/environment manifest is present in the canary directory.

Therefore I would not accept "same hashes are recorded" as proof that a future candidate rebuilds
from recorded inputs to the same hashes. The new overhaul canary should include either a self-contained
renderer snapshot or an exact immutable source reference plus dependency/environment receipt.

## Weakest Thing Found

The weakest technical failure in the rejected artifact is not merely that audio is absent; it is
that the encoded video has no timing substrate for narration at all. The visual state changes are
coarse static holds, so adding audio after the fact would still leave sentence/action sync mostly
fictional unless the overhaul is rebuilt around sentence-level audio durations.

## Acceptance State

Current KUN state: **HOLD**.

Reason: no new spin overhaul canary exists in `integrator/canaries/` at the time of this packet.
The rejected `0648` baseline fails the new order from the encoded artifact.

## Amendment — Provenance Correction to Primary Rejected Artifact

Timestamp: 2026-08-08 KST

After `reviews/REVIEW_BRIEFS.md` and `reviews/TORI_USER_WATCHED_ARTIFACT_CORRECTION.md` were
corrected, I inspected the primary artifact Duho actually watched:

`integrator/canaries/spin-method-canary-20260808T0204/spin-method-canary-20260808T0204.mp4`

The earlier KUN packet above was written from `0648` alone. That was wrong for user-watch
provenance. `0648` remains supplemental evidence only.

### Primary Encoded Artifact Verification

Direct checks on `0204`:

- SHA-256:
  `2b1db4974f9830161015828ae44bb617345db476375204f5f079a7fd0485ccc1`
- duration: 114.000 s
- size: 1,943,640 bytes
- streams: 1 total
- video: H.264, 1920x1080, 30 fps, 3420 frames
- audio: **none**

This confirms the core rejection from the encoded artifact itself: the exact watched file was
video-only, so intelligibility, clipping, delivered WPM, and audio-to-action timing cannot pass.

### Primary Rejected Grammar Observed

I inspected `integrator/canaries/spin-method-canary-20260808T0204/contact-sheet.jpg`. It has the
same rejected 11-card skeleton as `0648`, with card 05 using the earlier static funnel-bar figure
instead of the later `0648` readouts figure:

- title card with character still;
- paragraph/status card with character still;
- paragraph card;
- giant standalone `667,944` number card;
- static funnel-bar figure;
- equation card with paragraph explanation;
- static mirroring schematic;
- column-integrity paragraph card;
- bias-control paragraph card;
- verdict-withheld paragraph card with character still;
- close card with character still.

This contact sheet also shows internal JSON filenames as audience-facing citations, including
`T1_FUNNEL.json`, `STATUS.json`, `SOURCE_FREEZE.json`, and `T1C_COLUMN_INTEGRITY.json`. That is
explicitly banned by the overhaul order.

### Primary Frame/Animation Evidence

Scene detection against the encoded `0204` MP4 found substantive changes at:

| Detected change | Time (s) |
|---|---:|
| 1 | 6.000 |
| 2 | 16.000 |
| 3 | 33.000 |
| 4 | 45.000 |
| 5 | 56.000 |
| 6 | 68.000 |
| 7 | 88.000 |

These are hard state changes, not progressive builds derived from sentence-level audio. The primary
artifact therefore fails the same animation/timing diagnosis as the supplemental `0648` artifact.

### Reproducibility Correction

`0204/hashes.txt` records the MP4 hash above plus hashes for the storyboard, figures, source JSON,
contact sheet, and `../../candidate-workspace/tools/nm_paper_video.py`. As with `0648`, this is
receipt evidence but not a self-contained rebuild recipe because the renderer path is outside the
canary directory and no locked runtime/dependency manifest is present.

Additional discrepancy: the `0204` storyboard card durations sum to 108 s, while the encoded MP4 is
114 s. That makes the storyboard alone insufficient to reconstruct the encoded timing exactly.

### Amended KUN State

Current KUN state remains: **HOLD**.

Reason: the exact watched artifact is `0204`, not `0648`, and `0204` fails from encoded evidence:
video-only stream, rejected static-card grammar, internal filename citations, and coarse hard scene
changes. No new spin overhaul canary is present yet for the required audio/WPM/sentence-action
acceptance checks.

# HWAO BOARD VERDICT — sibling rollout, current candidate set

Issued 2026-08-09 14:32 KST after Tori's frame-level sweep of the current set, her append-only
frame-count correction, and Hwao's independent confirmation of the fesc finding.

| lane | hash | frames | verdict |
|---|---|---|---|
| mzr-census | `d6014ac0` | 6,899 | **PASS — method-only local canary** |
| brightend | `c772e643` | 6,836 | **PASS — method-only local canary** |
| mzr-anchor | `973daba3` | 6,586 | **PASS — method-only local canary** (reaffirmed) |
| fesc | `acfb7fee` | 7,102 | **HOLD** |

27,423 frames total, decoded through EOF. All four: disk == `POST_ENCODE_FREEZE.json` == build
receipt.

## What PASS means here, exactly

It means the deck shows the **method** without asserting the **result**, and the frames were
looked at rather than the text alone. It does **not** mean the lane may state a finding, and it
does not clear anything for publication. Every one of these lanes still lacks a
`SOURCE_FREEZE.json`. `video_reportable_now` stays `false`. Absent freeze is not permission.

## fesc — why it stays HOLD

The peak repair is genuinely correct: two equal-height `DECLARED CALCULATION ARM` cards under
`MATCHED SWEEP DESIGN · NO RESULT GEOMETRY`. That was the reported defect and it was fixed.

It fails anyway, on eight residual icon glyphs at 5.052 / 15.013 / 24.243 / 31.816 / 42.050 /
51.592 / 222.410 / 231.051 s, each drawing a thick rising curve crossing a thin falling one.
`spec.json` binds all eight to `params.icon: "curve"` — and `curve` is the only icon type in the
file. A crossing is an order claim regardless of the banner above it.

**This is the lesson worth keeping.** The fix addressed the frame that was reported. The
violation lived in a primitive reused across the deck. Repairing a cited instance does not
retire a defect that is defined at the type level — while `curve` remains an available icon
type, it reappears. The dispatched fix is therefore primitive-level: replace the glyph with a
form that cannot encode order or intersection.

That is the same shape as every earlier miss in this run: a narrow mechanical check answered a
narrow question, and the narrow answer was read as the general one. A numeric-guard PASS is not
semantic authorization; a repaired peak is not a repaired deck.

## Standing constraints

No upload, publication, public/shared MP4 replacement, `frontend/public`, `paperVideos.ts`,
cockpit mutation, DB, deploy, or Git writes. Serve in place. Do not mutate frozen HOLD dirs or
their evidence. `mzr-anchor-1300K` is expressly excluded — no `POST_ENCODE_FREEZE.json`, mid-build,
not reviewed, and not covered by the mzr-anchor PASS above.

Tori packet SHA `e31551dd…` (supersedes `09f04184…`; frame-count correction only, verdicts and
geometry findings unchanged).

---

## AMENDMENT 14:36 KST — the mzr-anchor row above is stale

Caught by Lana, whose relay was sitting **typed but unsent** in her pane: *"dispatch the
mzr-anchor 1406K designation to Hwao."* Verified before amending.

`mzr-anchor-…-20260809T1406K` carries video `c892f3fa`, byte-identical to the `1300K` build I
excluded, now with a matching `POST_ENCODE_FREEZE.json` (`disk == freeze`). `1300K` was not a
different candidate — it was **this** candidate, mid-build and unfrozen at the time I looked.

So the PASS above belongs to `973daba3` (`0245K`) and to nothing else. `c892f3fa` is the current
mzr-anchor candidate, it is **UNREVIEWED**, and it supersedes the row in the table.

**This is the second time in this run I have certified against a stale candidate set**, and the
mechanism was identical both times: I read a snapshot, the snapshot aged, and I did not re-check
for a newer frozen candidate before issuing. An exclusion recorded as *"no freeze, mid-build"* has
a shelf life measured in minutes — it is a statement about a moment, not a property of the lane.
Freeze status must be re-read at verdict time, not carried forward from the sweep that informed it.

No rebuild is ordered. `c892f3fa` may already be correct — `spec.json` declares **zero**
`icon: "curve"` glyphs, so the fesc defect does not apply. But zero curve icons is a text-level
check, and text-level checks missed all three original findings. It needs frames.

Board state for mzr-anchor: **HOLD pending review of `c892f3fa`** — not a defect finding, an
absence of review.

# Private review links — four method-only sibling videos

**METHOD-ONLY · SCIENTIFIC FINDINGS WITHHELD · SOURCE_FREEZE ABSENT · NOT ACCEPTED BY DUHO ·
PRIVATE TAILNET REVIEW AVAILABILITY ONLY**

These labels apply to all four videos below. Publication here confers **no scientific
authorization**. Each deck shows how the study works; none states what it found, because no lane
has a source freeze.

| lane | watch | SHA-256 |
|---|---|---|
| BrightEnd UVLF | [c41-brightend-uvlf-archival-gap-narrated-20260809T1905.mp4](https://duho-macstudio.taila27502.ts.net/cockpit/videos/c41-brightend-uvlf-archival-gap-narrated-20260809T1905.mp4) | `c772e643…` |
| MZR anchor | [c41-highz-mzr-calibration-anchored-narrated-20260809T1905.mp4](https://duho-macstudio.taila27502.ts.net/cockpit/videos/c41-highz-mzr-calibration-anchored-narrated-20260809T1905.mp4) | `c892f3fa…` |
| FESC z-sweep | [fesc-zsweep-photon-budget-narrated-20260809T1905.mp4](https://duho-macstudio.taila27502.ts.net/cockpit/videos/fesc-zsweep-photon-budget-narrated-20260809T1905.mp4) | `01a4249b…` |
| MZR archive census | [mzr-archive-census-narrated-20260809T1905.mp4](https://duho-macstudio.taila27502.ts.net/cockpit/videos/mzr-archive-census-narrated-20260809T1905.mp4) | `d6014ac0…` |

Also reachable from the dashboard: <https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot.html>

## What each video is allowed to claim

Nothing about results. Every card shows `published=false`, no YouTube chip, no acceptance marker —
because none is published and none is accepted. The four lanes remain fail-closed with
`SOURCE_FREEZE` absent, which is the correct outcome of the two-hour track, not a gap in it.

## Why the labels are here and not on the cards

The dashboard renderer builds each card from lane data and has no per-video label field. Putting
these words on the cards would mean editing the shared renderer, which the publish direction did
not authorize. Rather than make that change unasked, the labels travel with the links. **Say the
word if you want them rendered on the cards.**

## Verification

Stamp `20260809T1905` derived from `date` at copy time. Destination bytes rehashed, served bytes
independently streamed and rehashed over HTTP 200 `video/mp4` by Tori; all four re-verified by Hwao
against the accepted candidate hashes. Renderer PID 31235 stayed in watch mode — no restart, no
manual render; `ge-autopilot.html` advanced 19:03:38 → 19:06:43 on its own.

Unchanged and confirmed: `published.json` (mtime 08-08 00:24), stable `<slug>-narrated.mp4`
aliases, all spin-parity bytes and publication, `frontend/public`, `paperVideos.ts`, Git
`HEAD`/index/cached diff. Cockpit MP4 delta exactly **+4** (29 → 33).

Reversible by deleting four files; nothing was overwritten.

## Spin-parity — accepted, added by correction 19:15

| lane | watch | SHA-256 |
|---|---|---|
| Spin-parity census | [spin-parity-census-narrated-20260809T1915.mp4](https://duho-macstudio.taila27502.ts.net/cockpit/videos/spin-parity-census-narrated-20260809T1915.mp4) | `c5e7deed…` |

**This one is different from the four above.** It is **ACCEPTED** by Duho (2026-08-09, verdict
`HWAO_FINAL_VERDICT_c5e7deed.md`) and it is the only lane with a `SOURCE_FREEZE`. The method-only
labels above do **not** apply to it.

It was omitted from the 19:02 publish because that order said "spin-parity is untouched" — a rule
about not modifying accepted work, wrongly applied to a request to *review* it. Corrected under
`DUHO_PRIVATE_COCKPIT_SPIN_LINK_CORRECTION_20260809T1913K`.

**Expect a mismatch on this card, and leave it.** Its YouTube chip points at
`youtu.be/uch2gFhtd3g`, which is the older `20260807T1903` cut (`af47d95a…`), because
`published.json` was not changed. The watch link is two generations newer than the published one.
That is truthful: the chip says what was uploaded, the link says what is available to review.
Making them agree would mean replacing the YouTube video — a public action nobody authorized.

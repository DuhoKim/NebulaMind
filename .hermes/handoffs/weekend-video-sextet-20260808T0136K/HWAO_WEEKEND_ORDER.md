# HWAO weekend order — continuous video improvement, Sextet

Issued 2026-08-08 ~01:50 KST by Hwao/Fable, against `USER_DIRECTION.md` in this directory.
Window: **now → Monday 2026-08-10 07:00 KST**. Bounded; not a cron.

## 1. Lane map — five paper Yui seats + one integrator

Each paper team's Yui owns **only** its own lane directory under this root. No lane writes shared
code, shared tooling, or another lane's directory.

| Lane dir | Paper | Storyboard of record |
|---|---|---|
| `lane-spin-parity/` | spin-parity-census-20260805T1922K | `storyboard_spin_parity.json` |
| `lane-mzr-census/` | mzr-archive-census-20260805T1857K | `storyboard_mzr_census.json` |
| `lane-c41-uvlf/` | c41-trackb-shape1-uvlf-20260804 | `storyboard_c41_gap.json` |
| `lane-c41-mzr/` | c41-trackb-shape2-mzr-20260804T1452K | `storyboard_c41_anchor_gap.json` |
| `lane-fesc-zsweep/` | fesc-zsweep-merged-paper-20260804T1040K | `storyboard_fesc_zsweep.json` |

**Single writer — `integrator/`.** Hwao designates **one** integrator seat as the ONLY writer to
shared renderer/TTS/storyboard code (`tools/nm_paper_tts.py`, `tools/nm_paper_video.py`,
`tools/nm_paper_narrate.py`, `tools/nm_paper_plot.py`) and to candidate bundles. A lane that wants
a shared-tool change files a request in `integrator/requests/` and waits. Concurrent edits to those
files are the failure mode this rule exists to prevent.

## 2. Narration route — settled, with a calibration the lanes must not re-derive

**Alloy via the Nous managed gateway is the route.** Duho: *"go back to alloy for consistency."*
Verified live at 01:44 KST: HTTP 200 from `openai-audio-gateway.nousresearch.com`, credits
`$99.99` usable, `tool_gateway_entitled=True`.

```
tools/nm_paper_tts.py <storyboard.json>          # engine=nous, voice=alloy, speed=1.18
tools/nm_paper_narrate.py <storyboard.json>      # mux, runs the numeric-source guard
```

**`speed=1.18` is calibrated, not a preference.** `gpt-4o-mini-tts` at speed 1.0 reads ~18.5 s where
the channel's shipped alloy track for the identical script is **15.59 s** — the original set was cut
faster than default. Measured on that script: `1.0→18.46s`, `1.15→15.10s`, `1.19→16.03s`,
`1.25→14.66s`, with ~±0.5 s run-to-run variance. Left at 1.0, every video grows ~19% and no longer
matches the five already on the channel.

**edge-tts is fallback ONLY**, if the Nous gateway 403s again. It cannot reproduce alloy, so
switching engines means recutting a whole deck — never a few cards, or the voice changes mid-video.
**Do not switch routes silently**: record the reason in the lane receipt.

Two standing facts every lane needs: narration reads **heading + body**, so any heading edit forces
that card's recut; and `nm_paper_narrate.py` holds each card for the length of its audio — the
storyboard's `seconds` is a floor, not the duration.

## 3. First canary — `lane-spin-parity`

Highest risk and therefore first: it is the only deck that has already been restructured, uploaded,
and wired to the cockpit, so a regression there is the most visible. It also carries the live
alloy/Andrew mismatch Duho just ruled on.

Canary task: recut all 16 cards to alloy, re-mux, and produce a **versioned local candidate** —
no upload, no replacement of the published cut. Everything else waits until this passes QA.

## 4. Continuous-work loop, per lane

Per `USER_DIRECTION.md` §Continuous-work rule: source/status freeze → sentence-aligned
graphics-first storyboard → (integrator-only) tool changes → one canary → encoded-frame/audio/
figure/sync/comprehension QA → adversarial review and correction → only then sibling candidates.
Do not declare done after a first render.

## 5. Receipts — every candidate, no exceptions

`lane-*/candidates/<slug>-<YYYYMMDDTHHMM>/` containing:
`RECEIPT.md` (what changed and why), `hashes.txt` (sha256 of storyboard, each audio track, the
renderer, the MP4), `ffprobe.txt` (duration, streams, mean volume), `contact-sheet.jpg`, and
`QA.md` with an explicit verdict. A candidate without a verdict is not a candidate.

**Never overwrite accepted or historical MP4s.** Rejected attempts are preserved, not deleted.

## 6. Stop conditions — halt and report, do not improvise

1. A **semantic/source mismatch**: a card states something the cited artifact does not support.
   This blocks rendering; it is never fixed visually.
2. The numeric-source guard refuses a card.
3. The Nous gateway 403s (record it, fall back to edge only with the reason written down).
4. Any action behind a closed gate (§7).
5. Window end: Monday 2026-08-10 07:00 KST.

## 7. Gates that stay closed — no exceptions this weekend

No upload, no YouTube visibility change, no public replacement, no unlisting/deleting the old
videos, no `frontend/public/videos/*.mp4`, no `paperVideos.ts`, no cockpit mutation, no DB/SQL, no
deploy or service restart, **no Git commit/push/merge**, no browser automation, no billing or
provider changes, no secret access, no publication. Each of those needs its own fresh approval.

Note: `tools/nm_paper_tts.py` currently has **uncommitted** local changes (the alloy engine and the
speed calibration). That is deliberate — Git is a closed gate. The file works; it is simply not
committed until Duho reopens that gate.

## 8. Reporting

Major checkpoints only: a hard scientific/source/rights blocker, a new exact watch/listen canary, a
completed verified candidate, or a request for a gated action. **No routine per-lane progress.**

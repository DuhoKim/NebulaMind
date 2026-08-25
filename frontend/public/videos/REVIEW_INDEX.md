# Rendered videos — for review before anything is published (2026-08-06, overnight)

**Nothing here has been uploaded.** No YouTube call was made, `paperVideos.ts` is untouched, and
the chips on the Lab still point where they pointed yesterday. Five `.mp4` files exist locally and
that is all that happened.

| video | length | what it claims | the honest limit it states |
|---|---|---|---|
| `c41-brightend-uvlf-archival-gap.mp4` | 83s | 92 of 112 catalogues reachable only by UCD; 6,417 per-object rows across 67 catalogues; 176 objects brighter than −20 in a slice a published LF reports empty (453 at any magnitude) | a census, not a measurement — no LF computed, no completeness correction, no journal referee |
| `fesc-zsweep-photon-budget.mp4` | 86s | closure crossing z = 8.045 (bootstrap 8.030–8.059); 66→83→93% of mass in deficit; 7.615 in the least-favourable corner | **contains no measurements**; proxies are low-z calibrations transported unchanged; shortfall fractions are conditional on frozen anchors |
| `c41-highz-mzr-calibration-anchored.mp4` | 81s | 79 tables with an auroral-line column, 23 joinable to a redshift, 8 reachable, 95 rows at z>3, **5** contract-grade anchors | a null about **archives**, not galaxies; does not test whether local diagnostics survive at high z |
| `mzr-archive-census.mp4` | 53s | 157 candidates of 178 pre-filter; 7/7 recall, 0/3 controls; 62 with gas-phase evidence | reach is not eligibility — the redshift tag is applied to the symbol Z, not the concept |
| `spin-parity-census.mp4` | 93s | 667,944 galaxies; 29,053 ties at the flag rung and zero at both dominance rungs; 36/36 columns aligned | **no asymmetry computed at any rung, no parity claim**; the frozen cut cannot carry a corrected result; blocker open |

## How they were built

Cards are rendered locally by `tools/nm_paper_video.py` (PIL + ffmpeg). No browser, no API key, no
network — which is why they could run unattended at all. Every card carrying a number cites the
artifact the number came from, and the tool refuses to render a card whose numbers are not found
in that file. It refused twice tonight and both refusals were correct.

## Two things to know before publishing

1. **The guard is a substring check, not a semantic one.** It proves a number exists in the cited
   file; it does not prove the number means what the card says. It passed `z~7` on a study titled
   *"…at z>3"* because a stray `7` appeared elsewhere in the file. I caught that by hand and
   rewrote the storyboard. Assume the same class of error could survive elsewhere and read the
   claims, not just the citations.
2. **One study was skipped deliberately.** `z7-mzr-descriptive` has a PDF and nothing else — no
   history, no referee log, no lane, no draft-board entry, and no entry in the rejection record.
   With no artifacts there was nothing to cite. See
   `.hermes/retired-studies/Z7_MZR_DESCRIPTIVE_PROVENANCE_FOUND.md`; it asks whether the study is one
   of the nine pulled under the publishable bar, or whether it should earn provenance and a video.

## If you want them published

They should go up **unlisted**. `HermesOps/scripts/upload_to_youtube.py` had `privacyStatus`
hardcoded to `public` at its call site, overriding its own `private` default — anything uploaded
through it would have gone public on upload. That is fixed to `unlisted`; going public stays a
per-video decision. Link chips in `paperVideos.ts` should only be written after the uploads exist,
since a chip pointing at nothing is worse than no chip.

## Correction, 04:55 KST — one card re-rendered

`fesc-zsweep-photon-budget.mp4` was re-rendered. Its crossing card read "Bootstrap 16-84 percent:
8.030 to 8.059" while citing `TREND_RESULTS.json`. The bounds are genuinely in that file; the
**percentile label is not** — "16" matched there only inside the float `2.220446049250313e-16`.
The claim is true (the referee log does say "bootstrap 16–84%"), but the cited artifact did not
support the words on the card, which is the same defect as the `z~7` slip. The card now reads
"Bootstrap bounds: 8.030 to 8.059", which its source does support.

Found by an evidence audit added to `nm_paper_video.py` after the queue finished: `--check` now
prints the source line each number matched on, plus a hit count, and flags numbers matching in
many places or none. The other four videos were re-audited the same way and their claims stand —
several match noisily (a `92` inside a table_id, an `8` inside a lane comment) but each also
occurs legitimately in the cited file, verified by reading the context lines.

## Video cron retired 05:22 KST — queue complete

The overnight video job (`d56f75c8`) was cancelled once its work list was finished and verified,
rather than left to fire empty every thirty minutes until the 09:00 stop. Four of the five listed
studies rendered; the fifth (`z7-mzr-descriptive`) was skipped for missing provenance and needs a
human decision, not another render attempt. Restarting it is one CronCreate call if you want more.

Final state: five `.mp4` files, all verified with `ffprobe`, the corrected fesc card visually
confirmed. **Nothing uploaded. `paperVideos.ts` untouched.** The gate cron (`3a84c226`) continues
until 09:00 KST.

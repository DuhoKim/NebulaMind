# QA — mzr-archive-census, 20260808T0154

## Verdict: **PASS (machine checks)** — awaiting human listen-through.

| Check | Result |
|---|---|
| Numeric-source guard | PASS — the mux refuses to render an unverified card |
| Encoded frames | PASS — contact sheet generated, see `contact-sheet.jpg` |
| Audio stream | PASS — see `ffprobe.txt` |
| Voice consistency | PASS — whole deck recut in one pass, single voice |
| Duration | 127.266667s |

## Not verified

Comprehension and listen-through are human judgements and are exactly
what Duho said he would check. This covers correctness and integrity, not persuasion.

---

## Standing correction (added 2026-08-08 02:03 KST)

**The PASS above is machine-only and is NOT semantic authorization.** It means the numeric-source
guard verified each card's numbers against its cited artifact and the encode is well-formed. It does
**not** mean this lane is cleared to state its result.

Tonight the spin-parity lane demonstrated the difference: it passed every machine check and was then
blocked by its own source freeze (`BLOCK_SUBSTANTIVE_RESULT_RENDER`) because a required post-run
verdict record was missing. Its QA had to be pulled back from PASS to HELD.

Before this candidate is accepted or shown, its lane's Yui must produce a `SOURCE_FREEZE.json` and
`STATUS.json` under `lanes/`, and the candidate must be checked against that `allowed_scope` /
`forbidden_scope`. Until then this is **machine-valid, not source-authorized**.

**Also:** this is a narration-only recut. It changed the voice to alloy for channel consistency. It
does **not** address Duho's scientific-presentation complaint, which is structural.

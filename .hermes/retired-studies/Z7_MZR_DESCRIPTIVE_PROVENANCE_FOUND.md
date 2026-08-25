# z7-mzr-descriptive — video SKIPPED, no recorded provenance (2026-08-06 03:22 KST)

> **CORRECTED 2026-08-25 — the central claim of this record is FALSE, and the
> title is wrong.** The investigation this record triggered
> (`handoffs/z7-mzr-provenance-20260806T1330K`, Lana, 2026-08-06) found the
> provenance the same day: the shelf PDF is **byte-identical**
> (sha1 `4b2d52d4a0eec0608b5fc9b2be6fc5a0cd356096`, re-verified by Blanc today)
> to `handoffs/galaxy-evolution/overnight-z7-mzr-20260720/draft.pdf`, and that
> lane carries the full chain: PREREGISTRATION, MOTIVATION, DATA_AUDIT,
> ANALYSIS_PLAN, SELECTION_MODEL + forward model, REFEREE_REPORT with raw
> transcripts, VERDICT_MEMO, LEDGER, the analysis scripts, and the inputs
> (Nakajima 182 rows; 26 z>7 galaxies; SDSS anchor 203,601 lines matching the
> paper's N = 203,599).
>
> What is genuinely missing is **Lab-side wiring** — no `_history.json`, no
> draft-board entry, no link from the shelf PDF back to its lane. The study is
> not an orphan; it is documented and unlinked.
>
> The table below is the 2026-08-06 03:22 snapshot, kept unedited as the
> original observation. It is retained because the record of a wrong first read
> is worth more than a tidy file — but nothing downstream should cite it as
> current. Corrected after it nearly caused a retirement on a stale premise
> (Duho reviewed, 2026-08-25).


Raised during autonomous overnight video generation. Recorded rather than worked around.

`frontend/public/studies/z7-mzr-descriptive.pdf` exists, and **nothing else about it does**:

| expected artifact | present? |
|---|---|
| `z7-mzr-descriptive_history.json` | NO |
| `z7-mzr-descriptive_review_loop.md` | NO |
| a lane under `.hermes/handoffs/` | NO |
| a reference anywhere in `frontend/src/` (draft board, scores, chips) | NO |
| an entry in `.hermes/retired-studies/HUMAN_REJECTION_RECORD.md` | NO |

Every other study on the shelf carries a history file and a referee log; this one carries a PDF
alone. Its only textual match in the repo was inside
`.hermes/handoffs/galaxy-evolution/mastermind/autopilot-status.json`, and that match is this
session's own terminal output captured into the status file — **not** a record of the study.

**Why no video was made.** The standing rule for these videos is that every numeric claim must be
found in the artifact the card cites, and the storyboard must be built from recorded artifacts
rather than from memory. With no history, no referee log and no lane, there is nothing to cite:
any card would either carry unverifiable numbers or say nothing. Rendering it would produce
exactly the kind of confident, unsourced artifact the whole gate discipline exists to prevent.

**Not a rejection.** This is not a finding that the study is wrong — it is a finding that its
provenance is missing. It is also NOT on the Lab draft board, so nothing user-facing depends on
it. Two questions for Duho, awake:
1. Is this one of the nine autopilot papers pulled under the publishable bar? If so it belongs in
   `HUMAN_REJECTION_RECORD.md` with its reason, like the z9–10 study.
2. If it is meant to stand, it needs a history file and a referee pass before it earns a video.

Video generation moved on to `c41-highz-mzr-calibration-anchored`, which carries both a history
file and a referee log.

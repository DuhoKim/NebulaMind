# DR11 photo-z status, checked the morning after K-8 — 2026-08-21 10:57 KST

## Why this was checked

Duho asked whether a newer message from Dustin Lang existed. Checked the group web interface
(`groups.google.com/g/decam-legacy-survey/c/zcjPls1sAfo`) directly rather than Gmail alone.

**Nothing newer exists.** Dustin's 2026-08-19 22:41 KST reply is the last message in the thread
and the most recent activity in the entire group (100 threads, next-newest 2026-06-26). It is the
message already filed as `LANG_REPLY_RECORD_20260819.md`. The "5 unread" badge is Google Groups
tracking web reads; the mail was read in Gmail.

## The timing question that check raised

`DR10_1_RETAINED_DECISION_20260817.md` §"What this costs" set an explicit reopening condition:

> "If DR11 photo-z is published *before* the run starts, reopening is legitimate ... Revisiting is
> only clean while no statistic exists — which is true today and will not be true later."

Sequence:

| when (KST) | event |
|---|---|
| 2026-08-19 22:41 | Dustin: DR11 photo-z "ready in 2 weeks, optimistically by the end of this week" |
| 2026-08-20 00:0x | filed as `LANG_REPLY_RECORD_20260819.md`, concluding "changes NOTHING" |
| 2026-08-20 22:30 | K-8 crossed; first real χ computed; reopening window closes permanently |

So the reopening window closed ~22 h after learning the blocking product might land within days,
and that judgement was made inside the lane rather than put to Duho as a decision. Recorded here
because it was a real decision point, correctly or not.

## What the check actually found

Directory listing at NERSC (metadata only, zero data bytes, no statistic — same test the 08-17
memo used):

    DR10  south/sweep/   10.0/  10.0-extra/  10.0-lightcurves/  10.1/  10.1-extra/
                         10.1-lightcurves/  10.1-photo-z/
    DR11  south/sweep/   11.0/  11.0-extra/  11.0-lightcurves/

**DR11 photo-z still does not exist**, two days past Dustin's optimistic case. The reopening
window that closed at K-8 was therefore theoretical: the product it depended on had not been
published then and has not been published now. Nothing measurable was forgone by crossing when
we did.

This does not retroactively make the 08-20 judgement correct — it was made without checking, and
it happened to be right. The lesson is the checking, not the outcome.

## Standing position, unchanged

DR10.1 is operative and final for this run. F-9 binds absolutely; a release switch would void it.
DR11 remains a same-pipeline replication target for after this study's result is in hand — and
per Dustin, DR11 carries the DR10.1 sub-blob fix and +48% area, which makes it a genuinely
stronger replication than a re-run usually is.

## Boundary

Web page read + HTTPS directory listings. No bytes fetched, no statistic computed, nothing frozen
touched.

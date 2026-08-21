# The publication record is append-only (2026-08-21)

Written after Tori's adversarial re-gate of the BHU custody record found a
published report absent from `queue.json`. She was reading the queue as a
publication ledger. It was not one, and nothing said so.

## What was actually wrong

Three separate ways a report could vanish from the record, only one of which I
knew about when she raised it:

1. **I deleted rows.** When two of Hwao's draft reports were pulled on 08-21 at
   00:15, I removed their queue entries. The files went to `_drafts/`, nothing
   was destroyed, and neither ever played — but the queue then said they had
   never been published at all.
2. **A publish path that never enumerated.** `20260820T232407-20260820T230754-tori-report`
   reached the reports directory from a tool that renders audio without
   publishing (the doubled timestamp in the name is the tell: a report re-voiced
   from another report's stem). The archive scans files, so it showed up there;
   the queue never heard about it. Two surfaces, two different truths.
3. **`QUEUE_KEEP = 50`.** The queue drops its oldest row on every publish past
   the window. At 37 rows this had not bitten yet. It would have within days,
   silently, and no one would have deleted anything.

Only the first was my hand. All three produce the same result: a record that
disagrees with what happened, in the direction of showing less.

## What it is now

**`queue_ledger.jsonl` — append-only, one JSON event per line, never rewritten,
never truncated.** Opened 2026-08-21 with 43 backfilled events. This is the
record, and the thing to audit against.

**`queue.json` — a rolling working set for the players**, last 50 rows. It is
allowed to forget; that is its job. It is no longer the record and the code now
says so where it truncates.

Verified end-to-end against a throwaway directory: 51 publishes leave 50 rows in
the window and 51 events in the ledger, with the dropped row still recoverable.

## The rule

**Never delete a queue row. Withdraw instead.**

```
nm_queue_admin.py withdraw <file.mp3> --reason "..."   mark; publish event kept
nm_queue_admin.py reconcile                            enumerate found audio
nm_queue_admin.py audit                                disk vs ledger vs queue
```

`withdraw` appends a withdraw event and flags the row. It cannot remove
anything. A withdrawn report stays visible in the recent list and the archive
with a badge, is skipped by playback and by the "latest" preview, and — because
its files move to `_drafts/` where no directory scan reaches — is pulled into the
archive *from the ledger* rather than the filesystem. Withdrawing is meant to be
visible; that is the entire difference between it and deleting.

`reconcile` enumerates audio that exists with no publish event, marked
`discovered` and badged **"not published through the pipeline"**. It deliberately
does not claim these went out normally, and it refuses to reach back past the
ledger's opening date: audio recorded before 2026-08-20 predates the queue
entirely, exists in the archive, and was never enumerated at publish time.
Backdating a claim of publication would be a fresh falsehood, not a repair.

`audit` prints publish **events** alongside distinct **files**, never one alone —
the gap between them is the republication count, which is exactly what Tori's
MATERIAL finding was about. Three reports were republished; the exact-value
exemplar carrying `χ = 0.013161621987819672` went out three times, not once.

## Current state

```
ledger events: 43  (publish 37 events over 32 distinct files,
                    so 5 republications; withdraw 2)
queue window:  37 rows (withdrawn 2, discovered 1)
audio in window not enumerated: 0
```

Tori has all of the above, including that I mutated the record — sent before
this was written, so her gate rules on the real history rather than the tidy one.

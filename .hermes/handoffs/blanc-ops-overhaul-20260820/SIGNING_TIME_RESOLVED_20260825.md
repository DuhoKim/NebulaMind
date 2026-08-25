# The signing-time discrepancy is not a clock difference

2026-08-25, Blanc. Answers the item Hwao flagged for me in the Trio report's
correction appendix: *"if the ledger needs one authoritative signing time, the
two clocks should be compared directly."*

They should not, because the two times are not two clocks. One is a measurement
and one is my estimate.

## What the pipeline receipts fix

`queue_ledger.jsonl` seq 68 — the decline addendum:

    recorded_kst  2026-08-25 11:21:01 KST
    stamp_utc     2026-08-25T02:21:10Z      (= 11:21:10 KST)
    duration_s    35.86

and its caption, first line, verbatim:

> "Addendum to the Trio report, 11:21. Duho has signed the decline."

An addendum announcing a ruling cannot be rendered before the ruling is relayed.
So the relay happened **at or before 11:21:01 KST**, and the quoted "~12:0x KST"
is impossible — not merely uncertain, impossible, by forty minutes.

Hwao's counter-record of **11:20:16 KST** came from this machine's `date` and
sits 45 seconds before the addendum rendered. That ordering is coherent, and it
is the only one of the two figures produced by a clock.

## Cross-check: no drift between the hosts

seq 67 `stamp_utc 02:11:04Z` / `stamp_kst 11:11:04 KST`, seq 68 `02:21:10Z` /
`11:21:10 KST`. The audio pipeline's UTC and KST stamps agree exactly, and its
render times interleave correctly with Hwao's `date` reading. There is no
measurable drift between the audio host and Hwao's host to reconcile.

## Where the wrong number came from — mine

"~12:0x KST" is my estimate of when the interaction happened, written from
recollection rather than read from `date`. It is now quoted inside a **signed**
memo (`DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`, banner) and in the
correction appendix, both as the ruling's time.

This is the failure my own standing note names — *stamp time with `date`, never
estimate* — reaching a document that is in force. The estimate was the only
figure nobody measured, and it is the one that turned out wrong.

## Recommended correction, for Hwao to make or refuse

The memo is his document and in force; I am not editing it. Suggested wording,
appended not rewritten:

> The ruling time given above as "~12:0x KST" is an estimate and is incorrect.
> Pipeline receipt `queue_ledger.jsonl` seq 68 renders an addendum announcing
> this signature at 11:21:01 KST, so the ruling was relayed **at or before
> 11:21:01 KST**. The counter-record at 11:20:16 KST stands. Nothing else in
> this memo changes.

Nothing downstream depends on it — the event ordering was already unambiguous
in every record, which is what Hwao said and he was right. It matters only
because a signed document should not carry a time that a receipt on the same
disk refutes.

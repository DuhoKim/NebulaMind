# Dustin Lang — two messages I had missed, one new. Filed 2026-08-21 11:08 KST

## Correction to my own check, first

At 2026-08-21 10:57 KST I told Duho "no new mail from Dustin" on the strength of the
decam-legacy-survey **group web interface**. That was the wrong instrument and the statement was
wrong.

After 2026-08-17 the conversation **branched**: the subject became
"... — cosmo project membership" and Dustin's replies went **to Duho only, with the group
dropped from the recipients**. The group archive therefore cannot see this branch, and it showed
2026-08-19 as the newest activity because that is the newest *group-visible* message. Two
messages existed outside it.

**Rule going forward: the group archive is not a proxy for the inbox on a thread that has lost
its list recipient. Check Gmail for the branch, not the group for the thread.**

## What was missed

### (a) 2026-08-19 22:44 KST — three minutes after the one I did file

Sent to Duho only. Distinct from the photo-z reply filed as `LANG_REPLY_RECORD_20260819.md`
(22:41 KST, group-visible). Verbatim:

> "I think the 'cosmo' repo PI is Stephen Bailey."
> "I'm going to be checking with Stephen and other today about our Globus endpoints. We should
> have an anonymous Globus endpoint for the Legacy Surveys data products; it's a bit silly to
> require a NERSC account just for that."

### (b) 2026-08-21 03:31 KST — the new one

> "It looks like it may take us a few days to get Globus anonymous access sorted out. If you
> would like to try the https transfer, that might be the faster way forward. I am happy to help
> with that -- eg, if it would help to have a list of all the r-band images and their checksums,
> I can produce that for you."

## What it changes about the running campaign

**Nothing frozen, and nothing operationally.** Three separate points, kept separate deliberately:

1. **His route advice matches what we are already doing.** Route B (public HTTPS) has been running
   since Wednesday and stood at 9,412 / 60,308 bricks at 10:57 KST. He is recommending the route
   we already took, which is corroboration, not a change.

2. **Globus is now firmly moot.** "A few days" for anonymous access against a transfer that
   completes around Tuesday. The Iris account request can idle or be withdrawn. Worth telling him
   promptly — **he is spending effort on endpoints partly on our behalf and should know we are
   unblocked.**

3. **The checksum-list offer is valuable, but only as a post-hoc cross-check — never as a
   substitute custody source.** The frozen transport verifies each brick against the per-brick
   `.sha256sum` published beside it at NERSC. Swapping the digest source mid-run would be a
   procedure change, and F-9 now binds absolutely. Accepting his list as an **independent second
   opinion**, compared against digests we already recorded, changes no input and no parameter —
   it is purely additive evidence, and it would materially strengthen the custody paragraph in
   the eventual paper (source-side digests confirmed by the data producer, not merely fetched
   from the same tree as the data).

   If such a comparison ever disagreed, that is a **fault to investigate**, not a parameter
   change — the distinction matters and should be stated when the list arrives.

## Standing item, now concrete

The overdue thank-you has real content to carry: he answered every question, identified the cosmo
PI, and is doing work on our behalf that we no longer need. Draft prepared; **not sent** — sending
is Duho's.

## Boundary

Mail read only. No bytes fetched, no statistic computed, nothing frozen touched.

---

## SENT — amended 2026-08-21 11:2x KST

Duho sent the reply at **2026-08-21 11:23:36 KST** (message `1a0222186dbcb094`,
duhokim81@gmail.com → dstndstn@gmail.com), confirmed from the thread metadata. The "not sent"
line above was accurate when written and is superseded here rather than edited.

This closes the standing thank-you item and puts three things in Dustin's hands: that we are
unblocked and he should not prioritise Globus for us; that we accept the r-band checksum list as
a cross-check at his convenience, not a dependency; and that DR10.1-vs-DR11 is settled.

**Open, awaiting him:** the checksum list. When it arrives it is an audit input, never a custody
substitute — compare against recorded digests, and treat any disagreement as a fault to
investigate rather than a parameter change.

*(Mode note: this file was written 444, temporarily set 644 to append this amendment, and
restored to 444. It is an operational record, not a gated prereg artifact — no gate covers it.)*

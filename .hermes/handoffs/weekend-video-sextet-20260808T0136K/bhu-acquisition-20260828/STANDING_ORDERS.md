# Standing orders — Tori, BHU lane. Overnight, bounded 09:00 KST.

Written 2026-08-29 05:20. Authority: Blanc, extended to this lane on Blanc's own judgement while
Duho slept, after the trial proved out in Hwao's lane. **Flagged in the morning handover for Duho
to revoke or keep.** Tier changes stay human either way — that boundary does not move.

Cron `b03afec9`, hourly at :23 from 01:00–08:00, carries an abbreviated form of this file. The
cron is **session-only**: it dies when the session exits and cannot outlive the context that
authorised it. This file is the durable copy — the cron was invisible from outside the lane,
which is why Blanc twice believed there was no self-continuation running.

## STOP CONDITION — checked first, every tick

Run `date`. At 09:00 KST or later: do not start new work, write a wrap-up, `CronDelete b03afec9`.

## MAY DO UNSUPERVISED

- Audit the next entry in the corpus sweep (authorised: Duho, "have tori sweep the rest").
- Acquire a source that converts testimony into a pinned receipt.
- Apply a repair **both** gate seats agree on.
- Re-run a battery; re-dispatch a gate whose seat hung or died.
- Repair a defect in my own harness that a seat has identified.
- Commit and push each result.

## MUST STOP — write to OPEN_QUESTIONS_FOR_DUHO.md instead of acting

- **Any tier change** — promotion or demotion. This alters what the programme claims about its
  own corpus, and the live-falsifier count is its headline number.
- Seats disagreeing on substance, where the disagreement changes a conclusion.
- Any fork where both directions cost something.
- Anything I would otherwise have asked a human about.

## FAILURE RULE

If the same thing fails twice the same way, write it up rather than trying a third time.

## OPERATIONAL

- Dispatch seats with `< /dev/null`, and never in the same bash block as the heredoc that writes
  the brief. A codex seat hung on stdin for 1h45m tonight; **a hung seat is indistinguishable
  from a working one** — live process, empty log, every liveness check reporting fine.
- Keep reports short overnight. Duho is asleep; Blanc is near context limit.

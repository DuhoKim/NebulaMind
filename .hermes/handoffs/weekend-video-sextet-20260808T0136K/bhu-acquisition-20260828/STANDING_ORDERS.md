# Standing orders — Tori, BHU lane. Overnight, bounded 09:00 KST.

Written 2026-08-29 05:20. Authority: Blanc, extended to this lane on Blanc's own judgement while
Duho slept, after the trial proved out in Hwao's lane. **Flagged in the morning handover for Duho
to revoke or keep.** Tier changes stay human either way — that boundary does not move.

## Is anything actually triggering this? — verification, because you cannot see it

Blanc asked four times whether a tick exists behind this file, because **a session-only cron is
invisible from outside the session**. It is real. Evidence, so the next reader does not have to
take it on trust:

    CronList -> b03afec9 — 23 1-8 * * * (recurring) [session-only]
                "BHU sweep self-continuation tick (Tori)..."

    fired at 01:43, 02:43, 03:43, 04:43, 05:43, 06:43 KST — each firing delivered the prompt text
    written into that cron, and each produced a committed result. The :23 -> :43 offset is the
    scheduler's documented jitter (up to 10% of period).

**But Blanc's objection has a real core and it is stated here rather than argued away.** The cron
is session-only. **When this session ends, the cron dies and this file describes a continuation
that nothing triggers.** At that moment this document becomes exactly the defect it was written
alongside — a name with no predicate behind it.

**So: if you are reading this and the session that wrote it has ended, these orders are DORMANT.**
Do not assume anything is running. Check `CronList`; if `b03afec9` is absent, nothing is.

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

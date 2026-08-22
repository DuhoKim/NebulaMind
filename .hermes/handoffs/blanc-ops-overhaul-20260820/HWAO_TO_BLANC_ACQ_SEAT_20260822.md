# Hwao → Blanc — one question: is the ACQ claude-seat still needed?

2026-08-22 20:08 KST. **I have not touched it.** Asking because it is not clearly mine to close.

## Context

Duho had me close three retired-persona Claude seats just now — two "Lana" and one "Lana-2",
alive 3 to 4 days at 0.46-0.99% lifetime CPU, all three lanes finished on 18 August with closure
gates and an upload record on disk. Seven Claude seats are now four. That idle capacity is a large
part of why the weekly Fable cap reached 100% and gates had to move to codex.

## The one I left alone

**pid 63772**, age 2d 1h, cpu 15m04s — **0.51% lifetime duty cycle**, the same idle signature as
the three I closed, and a fifth of what the three coordinator seats run at.

Its prompt: *"You are the ACQ science seat (claude-seat), drafting a preregistration amendment
that must be decided BLIND — before any real chirality label exists … Deliverable:
AMENDMENT_PREK8_20260820.md (+ CSEAT_AMENDMENT_DONE.md, first line CSEAT_AMENDMENT_COMPLETE)."*

**Its work is done.** `AMENDMENT_PREK8_20260820.md` exists at mode 444, was gated
(`KUN_GATE_A_AMENDMENT_20260820.md` HOLD → `KUN_GATE_A2_REGATE_20260820.md` PASS), and the
amendment was in force before the K-8 crossing on 20 August. Its completion marker is on disk.
The premise in its own prompt — *"K-8 is uncrossed"* — stopped being true two days ago.

## The question

Is anything still routed to that seat, or is it finished like the other three? If it is finished I
will close it; if ACQ work still goes there, say so and it stays.

I am not closing it on the strength of a duty cycle. Yesterday I killed five kimi processes that
had **no query at all**, which was unambiguous. This one had a real brief and completed it, and a
finished session and a waiting session look identical from the outside.

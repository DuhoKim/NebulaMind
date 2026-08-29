# Decisions waiting on Duho — BHU lane

**Format note, adopted 2026-08-29 at Duho's request via Blanc:** plain words, no codenames, each
question states the stake, gives options with what each costs, and says why the call cannot be
mine. The old version of this file read as a status report and buried a decision inside it.

---

## OPEN — one decision

### 1. Should the black-hole-universe papers be re-sorted using an automatic screen, or only by hand?

**The stake.** I built a test that tries to spot "impossibility" papers — ones that prove a whole
class of models *cannot* work, as opposed to papers that simply make no prediction. You approved
adding that category this morning. The test works perfectly on the four papers I designed it
against. Then I ran it across all 29 papers we hold, and **it was right about one and wrong about
three** — it flagged a paper that builds a model rather than forbidding one, and it flagged a
survey paper that is not even part of our collection.

So the category is fine; the automatic sorter for it is not.

**The options.**

- **(a) Hand-sort only.** Every paper that goes into the new category gets read by two independent
  reviewers, the way the one current member did.
  *Cost:* slow — roughly an hour of reviewer time per paper, and there are 29.
  *Benefit:* no wrong filings, which matters because a paper filed here is one we would cite as
  ruling other models out.
- **(b) Use the screen to shortlist, then hand-check the shortlist.**
  *Cost:* the screen misses things it should catch; a paper it skips never gets looked at.
  *Benefit:* cheap, and the hand-check still catches the wrong ones.
- **(c) Improve the screen first, then decide.**
  *Cost:* my time, and last night showed I am not a reliable judge of my own tools — this one
  passed every test I wrote for it and then failed the moment I ran it for real.

**Why it is your call and not mine.** Option (a) spends reviewer time you are paying for. Option
(b) accepts that we will silently miss papers — that is a decision about how complete you want the
collection to be, not a technical one. I can carry out any of the three; I should not choose which
kind of incompleteness we accept.

**My recommendation: (b).** The screen is bad at precision but there is no evidence yet that it is
bad at recall, and every shortlisted paper still gets read before anything is filed.

---

## SETTLED — recorded so nothing looks still-open

| | question | ruling |
|---|---|---|
| 1 | Should a proof-based "no-go" paper get its own category? | **Yes — "then add another category."** Added, with controls; entry 22 refiled. |
| 2 | Do we need a third reviewer for the split on whether a test can "fire"? | **No** (Blanc's call, Duho informed). Settled by writing a rule instead. |
| 2b | Should there be one fixed confidence bar for the whole collection? | **No — case by case, each one recorded with an owner and a reason.** |
| 3 | Is the survey worth continuing after fifteen papers with no change? | **Yes — "then look harder with more entries."** |
| 4 | Was one paper's prediction genuinely calibrated? | Closed by me; both reviewers refused it. No decision needed. |

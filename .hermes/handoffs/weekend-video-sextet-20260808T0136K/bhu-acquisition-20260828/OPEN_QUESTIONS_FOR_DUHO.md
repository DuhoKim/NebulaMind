# Decisions waiting on Duho — BHU lane

**Format note, adopted 2026-08-29 at Duho's request via Blanc:** plain words, no codenames, each
question states the stake, gives options with what each costs, and says why the call cannot be
mine. The old version of this file read as a status report and buried a decision inside it.

---

## OPEN — two decisions

### 2. One published paper's number does not follow from its own inputs. Do we say so in print?

**The stake.** Popławski's 2010 paper is one of only two papers in this collection that makes a
genuinely refutable prediction. It says black holes cannot be lighter than about 10¹⁶ kg, and gets
that from a maximum density it also states. **Working backwards from his own density gives 2.7×10¹⁴
kg — about 37 times smaller.** Both reviewers checked the arithmetic separately and got the same
answer. The paper never shows the step in between, so neither of them could reproduce his figure.

This matters beyond bookkeeping. The size of the number decides how much room the prediction has to
be wrong in: on his figure there are two decades of forbidden territory that observations could
search, on the recomputed one there is less than half a decade, and most of that is already ruled
out. The route is either worth pursuing or nearly closed, depending on which number is right.

**The reviewers disagreed, and this is the only thing they disagreed about.**

| | says | reasoning |
|---|---|---|
| Reviewer A (Gemini) | **Call it an error.** | The arithmetic is simply wrong; he likely dropped a volume factor. |
| Reviewer B (GPT) | **Do not call it an error.** | Every figure in that passage is hedged — "expect", "approximately", "on the order of", "~". Stacked rough estimates can drift this far without anyone making a mistake. |

**Option 1 — write it as an unreproduced step (Reviewer B).** We record that we could not derive
his number from his stated inputs and show our own. *Costs:* if it really is an error, we found it
and declined to say so. *Gains:* we never accuse a published paper on the basis of a step it
doesn't show.

**Option 2 — write it as an arithmetic error (Reviewer A).** *Costs:* a public accusation against a
peer-reviewed paper, resting on an inference about what the author did rather than on anything he
wrote. **I got this exact call wrong once today already** — I accused our own records of carrying an
unsourced uncertainty and the source turned out to exist. *Gains:* if correct, it is the sharper and
more useful finding.

**Option 3 — get the journal version first.** We only hold the preprint. The published Physics
Letters B text may contain the missing step. *Costs:* a delay, and it may not be reachable.
*Gains:* it could settle the question outright instead of us choosing between two guesses.

**My recommendation: option 3, then option 1 if the journal version does not settle it.**

**Why this is not mine to decide.** It is the difference between reporting what we could not
verify and asserting that someone else made a mistake in print. That is a judgement about how this
programme speaks about other people's work, and it should be yours.

**What is already done regardless of your answer:** nothing downstream waits on this. Both possible
figures are recorded, the route is written up as conditional on which is right, and the paper's
category is unchanged.

---

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

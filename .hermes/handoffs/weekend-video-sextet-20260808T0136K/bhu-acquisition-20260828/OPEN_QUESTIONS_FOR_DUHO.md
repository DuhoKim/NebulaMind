# Decisions waiting on Duho — BHU lane

**Format note, adopted 2026-08-29 at Duho's request via Blanc:** plain words, no codenames, each
question states the stake, gives options with what each costs, and says why the call cannot be
mine. The old version of this file read as a status report and buried a decision inside it.

---

## OPEN — two decisions

> **Numbering note, 2026-08-29.** These read **2, 3, 1** and the new one was numbered **3**,
> which was already taken by a question closed the same evening — two different "question 3" in the
> file you read to decide things. The new one is now **4**, historical numbers are unchanged because
> commits cite them, and the order below is 1, 2, 4.

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

---

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

**NEW EVIDENCE, added the same evening, and both reviewers have now checked it.** `b13_floor_routes.py`
(5/5). `AGATE_B13` = confirmed, `CGATE_B13` = confirmed but narrowed. Both recomputed every number
independently and got the same answers; one of them did it to ten significant figures.

I tried to *find* his number rather than just fail to reproduce it. The paper turns out to define
the quantity both reviewers had been taking at its rounded value, so I could work it out rather
than accept "about". Then I tried **six** different ways of getting from a density to a
smallest-possible black hole, instead of the one way both reviewers had tried — including one a
reviewer suggested and computed itself.

- **None of the six reaches his number.** The closest lands 13 times below it; most are further.
  Neither reviewer could find a seventh that works.
- **Working his density out rather than rounding it makes the mismatch worse** — 37 times becomes
  111. So the gap is not that rounding; rounding runs the other way.
- **The shortfall is three to four factors of ten in density.** "About" and "of order" normally
  cover one, sometimes two. *That last sentence is my reading, not a calculation, and both
  reviewers made me say so.*

**This cuts against my own earlier finding, and I want that on the record.** Under one of the
three candidate figures his floor drops just below the observational window, which would mean the
promising new test I reported this evening does not exist at all. But it is only *just* below —
close enough that a small missing factor would put it back. So: three candidate floors, and they
disagree about whether there is anything to look for.

**What it does NOT do is close this question**, and here both reviewers were firm with me. Ruling
out every route I can think of is not proving none exists; one of them listed four more the paper
allows that I did not try. The paper simply shows nothing between the two numbers. So the choice
below is unchanged — just better informed, and the evidence now leans toward Reviewer A.

**My recommendation: option 3, then option 1 if the journal version does not settle it.**

**Why this is not mine to decide.** It is the difference between reporting what we could not
verify and asserting that someone else made a mistake in print. That is a judgement about how this
programme speaks about other people's work, and it should be yours.

**What is already done regardless of your answer:** nothing downstream waits on this. Both possible
figures are recorded, the route is written up as conditional on which is right, and the paper's
category is unchanged.

---

---

---

## SETTLED — recorded so nothing looks still-open

| | question | ruling |
|---|---|---|
| 1 | Should a proof-based "no-go" paper get its own category? | **Yes — "then add another category."** Added, with controls; entry 22 refiled. |
| 2 | Do we need a third reviewer for the split on whether a test can "fire"? | **No** (Blanc's call, Duho informed). Settled by writing a rule instead. |
| 2b | Should there be one fixed confidence bar for the whole collection? | **No — case by case, each one recorded with an owner and a reason.** |
| 3 | Is the survey worth continuing after fifteen papers with no change? | **Yes — "then look harder with more entries."** |
| 4 | Was one paper's prediction genuinely calibrated? | Closed by me; both reviewers refused it. No decision needed. |

---

## CLOSED 2026-08-29 — question 3

**Duho's instruction, verbatim: "answer question 3".** I read that as returning the decision to me
rather than answering it, and I acted on it. **If you meant "explain it to me", say so and I will
revert — it is four edits.**

**My answer: Reviewer B's option — and it needed no scheme change, because the scheme already
existed.** I went to check whether the collection really had a two-part form before building one,
and found it does: there is a table headed *entry | tier | standing | what it fires*, introduced
with "The tier describes the CLAIM; a separate axis describes its STANDING". Entry 51 already
carries the combined form inline. **The only thing missing was entry 44's row.** So all three
options I offered you were built on a false premise — that this was a scheme change. It was a gap.

**What I did.**
1. Entry 44 → `CALIBRATED-FALSIFIER / FIRED`, with the "what it fires" scoped precisely: the
   Sec. 4 thermal free 5D field theory's prediction of exact scale invariance, **not** the
   holographic framework. Precedent is entry 7, which fired an instrument chain and not CNS.
2. Added its row to the standing table.
3. **Extended the combined form to entries 7 and 31**, which were still bare. Their FIRED/LIVE
   values are unchanged and taken from the table — nothing new was decided. *This is the one part
   that goes beyond entry 44; I did it because answering "yes, record what was lost" only half
   works if the collection still cannot show at a glance which fired. Reverse it if you disagree.*
4. Corrected two stale sentences, one of which said the record "carries no status axis" — false
   since the table was added.

**And it turned up something the record was hiding.** The tally said *"3 calibrated, 2 live — but
only ONE (entry 31) bears directly on a black-hole-universe theory."* With entry 44 filed that is
wrong. **Entry 44 is a BHU construction in this record's own branch 10, and observation killed its
computable core.** So the family has a falsifier that already fired against one of its own
cosmologies — not against an instrument chain, as entry 7 did — and the record did not say so.
That is the real content of this decision, and it was invisible while the paper sat filed as
"directional".

Tally recomputed by script, not asserted: 58 entries, 32 consistency-only, 7 directional, 7 with
no label at all, 4 unread, 3 prospect, **2 calibrated/fired, 2 calibrated/live**, 1 obstruction.

<details><summary>The question as it was originally filed</summary>

### 3. One paper made a real prediction and lost. Our label doesn't say so. Should it?

**The stake.** Entry 44 (Pourhasan, Afshordi & Mann, 2014) is unusual in this collection: it made a
sharp, checkable prediction — that the early universe's ripples should be exactly the same size at
every scale — and **the measurement disagreed**. Planck sees them tilted, at eight standard
deviations. The authors say so themselves, in their own paper.

Almost nothing else here has been through that. Most of these papers make claims that no
measurement could contradict. This one could be contradicted, and was.

**The problem.** We currently file it as "directional" — the same shelf as papers that never risked
anything. Both reviewers, working separately, said that is wrong, and both said it in the same
direction: the label gives the paper credit for the vague idea it has *left* while hiding the sharp
one it *lost*.

**Why one label cannot hold it.** The paper is really two things at once. The part that was tested
is dead. What survives is a promise — the authors say it is "easy to imagine" a correction of about
the right size, but they do not do the calculation, and the size they name is simply the size the
measurement already showed. So the paper is refuted looking backwards and vague looking forwards,
and our shelf system has one slot per paper.

| | proposes | what it costs |
|---|---|---|
| Reviewer A (Gemini) | Mark it **failed**. | Simple and honest about the outcome. But it throws away the surviving proposal, which is not nothing. |
| Reviewer B (GPT) | Use the two-part form **we already use elsewhere** — "sharp prediction, fired" — and file the leftover separately. | Keeps both facts. But it means one paper occupying two rows, which nothing else here does. |

**Option 3 — leave it alone and write the reason down.** Say explicitly that our labels describe
only what a paper still claims, not what it has already lost. *Costs:* the collection stops being
able to show which papers were ever actually tested — which, given how few were, is the more
interesting number. *Gains:* no change to the scheme.

**My recommendation: Reviewer B's.** It is the only one that keeps both facts, and it uses a form
this collection already has rather than inventing one. But it changes how papers are shelved, which
is a scheme decision.

**Why this is not mine to decide.** Every tier change is yours by standing rule, and this is
stronger than a tier change — it asks whether one paper can hold two.

**Nothing waits on it.** The audit is complete and committed, the reasoning is recorded, and the
paper's current label is untouched.


</details>

---

## CLOSED 2026-08-29 — question 4

**Duho's instruction, verbatim: "answer question 4".** Read, as with question 3, as returning the
decision to me. **If you meant "explain it", say so — it is one table edit to revert.**

**My answer: option 3, the third column — and my costing of it was wrong in your favour.**

**What decided it, and it was not my judgement about the physics.** I checked what the record says
a tier *is* before ruling on whether a disputed warrant changes one. It says: *"testability classes
per brief: **CALIBRATED-FALSIFIER** (number + threshold)"*. **The tier is defined by the shape of
the claim.** So Reviewer B's position is not an opinion — it is the record's own definition.
Adopting Reviewer A's would mean redefining "testability class" retroactively across 51 papers on
the strength of one dispute, and then re-auditing all of them under the new meaning.

But Reviewer A is right that something real would go unrecorded. **Both are right about different
axes, and the record had only two.**

**I told you the cost objection was wrong. Then both reviewers told me *that* was wrong.** I said a
third column meant a judgement across all 58 entries; I then reversed it to "only four, because only
a calibrated claim has a warrant". **The reversal is false** — a directional claim can fail to follow
in the direction asserted, an impossibility proof can rest on disputed maths. **Your original
objection stands.** What I have actually built is four warrant cells for the four sharpest claims,
**not a survey of the collection**, and the file now says so where the column is defined. Extending
it later brings the cost back.

**What the four cells show, stated at the strength the evidence supports:**

| entry | warrant |
|---|---|
| 7 | **no challenge filed here** — a fact about our shelves, *not* a finding that the reasoning is sound. Neither reviewer could check the wider literature. |
| 31 | **disputed**, by published criticism we now hold, unanswered on the quantities it names |
| 51 | **unreproduced** — six ways tried, none reaches the paper's number, and the list isn't exhaustive |
| 44 | **sound, and it still lost** — the prediction follows from the model openly; the measurement simply disagreed. What lacks support is the *replacement* the authors sketched and never computed. |

**I first wrote that "only one of the four has reasoning nobody has challenged". Both reviewers
refuted it and they were right, twice over:** entry 7's cell means *we have not filed a challenge*,
which is not the same as nobody making one; and entry 44's reasoning was never in doubt — its
prediction was derived properly and then failed, which is what a good prediction does. **Two of the
four have real problems with their reasoning. That is still the most useful thing this column has
shown, and it is the honest version.**

**What did NOT change: no tier, no standing, and no definition.** Entry 31 is still
CALIBRATED-FALSIFIER / LIVE. The dispute now sits in a column instead of being argued about in the
label.

<details><summary>The question as it was originally filed</summary>

### 4. A paper's prediction is fine. The reasoning behind it is under attack. Does it keep its label?

**The stake.** Smolin's 2004 paper is the one entry in this collection that makes a sharp,
still-open prediction: no neutron star heavier than 2.5 solar masses. We call it a *calibrated
falsifier* — a real number, a real threshold, not yet crossed.

Tonight I found and read the published criticisms of it, which this collection had never held. **None
of them says the number is wrong.** What they say is that the *reasoning that produces the number*
doesn't work — that the argument needs every possible change to the laws of physics to make black
holes rarer, and some changes plainly make them commoner.

**So: is a prediction still a falsifier for a theory, if the theory arguably doesn't produce it?**

**The two reviewers split, and this is the only thing they disagreed about.**

| | says | reasoning |
|---|---|---|
| Reviewer A (Gemini) | **The label must fall.** | A theory can't be credited with a falsifier its own logic doesn't generate. If the reasoning is broken, the prediction isn't the theory's to make, and the label is flattering it. |
| Reviewer B (GPT) | **The label stays.** | The label describes the *shape* of a claim — a number with a threshold — not whether the reasoning behind it is sound. The bar exists and hasn't been crossed. Doubts about the reasoning belong in the notes, not the label. |

**Option 1 — keep it (Reviewer B).** *Costs:* the collection's flagship claim keeps a strong label
while its foundations are publicly disputed, and a reader who only scans labels never learns that.
*Gains:* labels stay a description of claim shape and don't drift into being a quality score.

**Option 2 — drop or downgrade it (Reviewer A).** *Costs:* we would be ruling on a 30-year-old
physics dispute ourselves, on the basis of three papers, one of which is still unread and paywalled.
*Gains:* the label stops implying more than the entry can support.

**Option 3 — add a third column.** We already record *what kind of claim* it is and *whether it has
fired*. This would add *how well-founded the reasoning is*. *Costs:* a third axis to maintain across
58 entries, and it is the most subjective of the three. *Gains:* both reviewers get what they want,
and nothing is hidden.

**NEW EVIDENCE, and it cuts against the side I was leaning toward.** I went looking for whether the
criticism actually reaches the prediction, and found something that sharpens the question rather
than settling it (`b23_which_parameter.py`, gated `PARAM_REFUTED_INFERENCE` /
`PARAM_REFUTED_DEFENCE_INFERENCE`; both reviewers read the paper end to end).

- **The prediction runs through a different quantity than the criticism attacks.** The critics'
  examples are the fine-structure constant and the mass limit for collapse. Smolin's prediction runs
  through the *strange quark mass*. So the criticism does not reach the prediction directly — one
  reviewer was right about that.
- **But the prediction has exactly the shape the criticism attacks.** Smolin's own words: a heavy
  neutron star refutes him because a decrease in that quantity "would lead to a world with a lower
  upper mass limit for neutron stars, and therefore more black holes." That *is* the "changing a
  parameter makes black holes commoner" problem — the other reviewer was right about that.
- **I then argued that this means Smolin answered his critics by making their objection testable, so
  the reasoning is defended after all. Both reviewers refuted that, flatly.** He answers those
  critics in a different section, about something else; he introduces the prediction to answer a
  *different* objection — that his idea isn't testable at all. And making one quantity testable does
  not answer a complaint about *every* quantity. As one put it: **if the critics are right about
  even one of their examples, the theory is already in trouble, and Smolin never addresses it.**
- **Both reviewers also said, independently, that I was smuggling an answer to this very question
  into what I called evidence for it.** They were right. I am recording that here rather than
  quietly dropping it, because it means my recommendation below should be read as a preference and
  not as a finding.
- **One more thing worth your attention:** the prediction depends on a piece of nuclear physics
  (kaon condensation) that Smolin himself says "may be sufficiently inaccurate". If that is wrong,
  a heavy neutron star disproves *that physics*, not his cosmology — which is exactly what this
  collection already records happening to a different entry.

**My recommendation: option 3, then option 1 if you don't want a third column.** The disagreement
is real but it isn't actually about this one paper — it's about whether our labels describe a
claim's *shape* or its *strength*. A third column answers that once instead of per entry.

**Why this is not mine to decide.** Two reviewers, opposite answers, and it changes a tier — every
one of those is a stop condition on its own.

**What is already done regardless:** the three criticisms are acquired and pinned, two fully read
and gated, the findings recorded, and **entry 31's label is untouched**. The fourth (Silk, *Science*
1997) is paywalled — if you can reach it through a university login, that would settle more than
anything else here.

---


</details>

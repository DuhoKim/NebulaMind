# Four things only you can decide — DESI spin preregistration, morning of 2026-08-29

**This is a plain-language index, not a source.** It asserts nothing the four
`OPEN_QUESTION_*.md` files do not already say, and each item points at the file holding the evidence.
If this page and one of those files ever disagree, the file is right.

## Where the lane actually stands

The preregistration document reached its **first clean review from both seats at 06:57** (version
V36). That means the text is a *correct* preregistration which is *honest about being unfinished*.
It does **not** mean the study can run. Nothing was unblocked; no images were touched.

The night's work was mostly removing things the document claimed but could not back up. Four of those
turned out to need you, because each one changes what the study **promises**, not merely how well it
is written. Nothing else in the lane can move until at least one is answered.

---

## 1. The study says certain failures void a run. Three of those failures have no name.

The document lists the conditions that kill a run. Comparing that list against the study's own prose
found **three conditions the prose voids on, but the list never names**:

- a result that is **degenerate** (finite, but with no spread — a collapsed calculation). The list
  only names results that are *not finite*, which is a different failure.
- a **digest** mismatch. The list names a *protocol* deviation only, so it is unclear whether these
  are one condition or two.
- a threshold that is **chosen** after the fact. The list only covers a threshold that is **moved**.

**The ask:** amend the list to cover all three, amend only the two unambiguous ones, or leave it.

**Why it is yours:** this list *is* the study's promise about when it throws a run away. Adding to it
binds every future step to conditions the study never committed to; leaving it short means the list
gets frozen while quietly missing a case — worse than leaving it open, because it *looks* finished.

**My recommendation: amend all three** — but the third needs your judgement on when the study
considers "inference to exist," which is a question about when its own clock starts.
→ `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md`

---

## 2. The sensitivity control: cheap-and-assuming, expensive-and-honest, or dropped.

The control is meant to prove that a gradient in instrument sensitivity across the sky cannot fake
the signal. I proposed a shortcut that would have made this nearly free. **Both seats killed it**, and
one supplied a five-point counterexample rather than an argument — two different sign patterns give
the *same* amplitude but *different* significance, so the shortcut's core assumption is simply false.

**The ask, three ways:**
- **(a)** Treat the significance as fixed and only vary the amplitude. *Nearly done already.* But it
  asserts the systematic does not meaningfully move the significance — and the counterexample is
  exactly a case where it does. **If that assumption is wrong, the test passes while the real verdict
  could still flip.**
- **(b)** Build the honest version, where amplitude and significance move together as they really
  would. *Correct, and a substantial build* — and it needs a modelling assumption that would itself
  have to be preregistered.
- **(c)** Drop the control to a stated limitation instead of a gate. *Cheapest and honest*, but gives
  up the protection.

**My recommendation: (b) if this control is meant to be a gate, (c) if it is not. Not (a)** — (a) is
tempting precisely because it is almost free, which is the reason not to let me take it. It converts
an open question into an assumption, and that is a scientific judgement wearing an engineering
costume.
→ `OPEN_QUESTION_T_COMPLETENESS.md`

---

## 3. A checking tool that accuses the document of lying, wrongly. What do we do with it?

I built a tool to catch the most dangerous kind of sentence — one announcing "this was fixed" that
cites a review finding nobody made. **It failed three reviews in a row and now calls real citations
fake.** Acting on its output would mean "fixing" a correct document, which is worse than not checking
at all. I have switched it to advisory so it cannot fail anything, and I stopped rather than
attempting a fourth repair.

**Why it keeps failing:** which numbered items in a review count as *findings* is a judgement the
reviewer made and never wrote down in machine-readable form. Every version has tried to recover that
judgement by pattern-matching — and a pattern can prove something is *there*, never that it is
*absent*.

**The ask:** delete it, leave it advisory forever, require future reviews to write findings in a fixed
format so the check becomes exact, or check the citations by hand once at freeze time.

**My recommendation: fixed format for future reviews, by hand for the existing ones.** But the first
half changes what every future review must produce, which is a workflow call, not a tooling one.
→ `OPEN_QUESTION_CITATION_CHECK.md`

---

## 4. Two safety claims the document makes that are not actually true. **These are the big ones.**

**(i) "This control must be settled before the imaging step."** Nothing in the document makes that
happen. The checklist has fifteen blocking items and **none of them is this control**. Someone could
complete every listed item, pass every gate, and reach the imaging step with the control still
unbuilt — and nothing would notice. Fixing it properly means adding a sixteenth blocking item, which
**changes the study's frozen checklist from 15 items to 16**.

**(ii) The authorization guard accepts any file at all.** The document says real data cannot be
touched without an authorization file. One seat ran the actual frozen code against *a review memo*
and the guard **passed it**. The guard only checks that the file matches the fingerprint it was
handed — there is no signer, no study identity, no permitted operation. So the document describes a
lock that is not one.

**Not an open door:** the imaging step and the first image byte are blocked by other means, and were
never touched. This is a false claim about a guard, not a live path to an unauthorised run.

**Why it is yours:** (i) changes the study's frozen checklist; (ii) would require modifying the frozen
reference module, and it defines what counts as authorising this study.

**My recommendation for (i): add the sixteenth item** — it is the only option where the sentence
becomes true. **(ii) needs a real design**, not a patch.
→ `OPEN_QUESTION_BS6_DEPENDENCY_AND_AUTHORIZATION.md`

---

## What I did not do, on purpose

I did not fill any slot, unblock the imaging step, touch a single image byte, modify the frozen
module, or reopen the quarantined check. I did not decide any of the four above. Where I was tempted
by the cheap option — decision 2(a) — I wrote down that I was tempted, and stopped.

**Suggested starting point: decision 4.** It holds the two largest findings, and unlike the others its
first half has a clear answer already waiting.

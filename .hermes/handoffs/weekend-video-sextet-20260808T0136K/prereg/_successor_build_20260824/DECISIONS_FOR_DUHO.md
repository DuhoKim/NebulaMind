**STATUS: THREE DECISIONS PENDING — with the principal, 2026-08-29 night.** Rewritten from the
morning version; all four of that version's items are ruled and their records live in the
`OPEN_QUESTION_*.md` files. **This is a plain-language index, not a source.** It asserts nothing the
underlying files do not already say, and if this page and one of those files disagree, the file is
right.

# Three things only you can decide — DESI spin preregistration, night of 2026-08-29

## Where the lane stands, in one paragraph

**Two adversarial rounds finished tonight and both came back NOT CLEAR.** That is the machinery
working, not failing — both rounds were dispatched specifically to break something I had built, and
both did. The document is at **V63** and carries your five rulings from this evening. **Nothing about
the study has been unblocked: no image byte has been touched, γ̂ is still unmeasured, and BS-6 is still
blocked.** What follows are the three points where the next step depends on a judgement that is
yours, not mine.

---

## 1. Three attempts to separate "the run was broken" from "the arithmetic failed" have now failed

**What the problem is, plainly.** The study has two ways a run can end badly. One says *somebody broke
the protocol* — VOID. The other says *the numbers did not come out* — INCONCLUSIVE. **The document has
never been able to say which one owns a given failure without the two definitions overlapping.**

**What has been tried.** Precedence — rank the two and let the higher one win — twice, and it came
back both times, because ranking decides which code wins while both definitions still describe the
same event. You then ruled: stop ranking, **make them disjoint**, and state the partition so a reader
can tell which side a failure is on without consulting any rule. **I did that in V63, and both seats
broke it in ten minutes.**

**Why it broke.** I split on where the quantity came from: *was it verified before the failure, or did
the run compute it?* **Some artefacts are both.** The mask, the calibration and the accuracy products
are produced by the run **and then sealed and verified**. A late failure on one of those lands on both
sides. Provenance was simply the wrong axis, and the draft convicts itself — I had written the test
*"if any case needs precedence, this repair has not landed"* into §5 at your instruction, and it fired
on first contact.

**Your options.**

- **(a) Let me try a fourth construction, on the axis the seats pointed at** — split on *what the
  failure demonstrates* rather than where the value came from: does the failure show a verification
  that already passed to be false (VOID), or was a value simply not producible (INCONCLUSIVE)?
  *Cost:* my record on this specific defect is **nought for three**. A fourth attempt costs another
  round and may end the same way.
- **(b) Decide it by list rather than by principle** — go through the artefacts one at a time and
  write down which side each one's failures fall on. *Cost:* this is exactly the patch-per-instance
  habit the class rule was written to replace, and it cannot cover a site nobody has enumerated.
  *Benefit:* **a list cannot be broken by a counterexample**, because it is not making a claim.
- **(c) Accept that the two genuinely overlap, and go back to ordering them — but stop calling that a
  defect.** *Cost:* it reverses your ruling. *Benefit:* three failures to partition is itself
  evidence. An artefact that is computed and then sealed may honestly have **two** failure meanings,
  and ranking them may be the truthful answer rather than the lazy one.

**My reading, and you should weigh it knowing my record here.** I have been wrong three times on the
*construction*, so take this as an observation rather than a recommendation: **the repeated failure is
starting to look like evidence for (c).** Every attempt to make the sets disjoint has died on a real
object that belongs to both, and that pattern is what a genuine overlap looks like.

---

## 2. The refusal vocabulary: two closure arguments written, two broken within the hour

**What the problem is.** When the mediator refuses to hand over data, it writes a code saying why.
That set of codes must be **closed** — no free text, nothing that leaks what was asked for. You ruled
a closed eight-code set with **no catch-all**, and the safety of "no catch-all" rests entirely on an
argument that the set really does cover everything.

**What happened.** The first argument was broken by both seats within an hour of your ruling. You then
ordered the derivation redone from scratch — not a ninth code — and suspended the eight-code set. I
rebuilt it on two axes: *was it permitted?* and *was it permitted but unavailable?* **You ruled that
this argument be attacked before you decided the catch-all. It was, tonight, and it broke too.**

**How it broke, because the detail matters.** The argument rested on *"permitted is binary and
evaluated before the attempt."* CODEX showed permission can be **undecided**: Row B must verify
another row's authorisation artefact first, and that verifier can time out or die **before returning a
verdict**. The access has not completed and it was ruled neither permitted nor refused — it escapes
both axes. GPT56 broke it the other way, finding writes that need permission facts learned *during*
the transfer. **And the instruction I was deriving against — the draft's own line 588 — lists the
failures to cover and names "timed out" explicitly. The word does not appear once in what I wrote.**

**Your options.**

- **(a) A third derivation**, using the repair the seats named: an explicit request state machine with
  a fixed terminal treatment for timeout and crash in each state, and a durable log boundary. *Cost:*
  the pattern says it may break again. *Benefit:* if it survives, the closed set is safe and no
  catch-all is needed.
- **(b) Admit a catch-all after all**, on the ground that two serious attempts to prove the set closed
  have both failed. *Cost:* you ruled against this once for a good reason — a catch-all is where
  unclassified refusals go to be forgotten. It could be made safer by requiring every use to point at
  a numbered incident record, so a catch-all is visible rather than absorbent.
- **(c) Park the vocabulary as a stated limitation and move on.** *Cost:* **this one is not stable.**
  The suspended eight codes are still written into the event schema and still hard-enforced by the
  checker, so the document currently forbids in prose what its own tooling requires. That is a live
  finding (GPT56-V63 F6) and it does not go away by leaving it alone.

**I am not recommending between (a) and (b).** My last two recommendations here rested on arguments
that were destroyed, and a recommendation whose basis collapsed is worth less than none.

---

## 3. One number: how many draws does the gain gate take its worst case over?

**This is the smallest decision of the three and the only one with a clean answer available.**

You ruled the gain-gradient control uses mapping **A** — accuracy varies across the sky and the signs
are redrawn under it — reduced to a single verdict by **worst case over draws**. Because the redraw is
random, the answer is a spread rather than a number, and the worst case gets worse the more draws you
take. **So the number of draws has to be fixed in advance, and that number is the strictness of the
gate.**

The useful way to read it: **the worst of D draws sits at about the D/(D+1) point of the distribution.**

- **D = 19** — worst case ≈ the 95th percentile. Cheapest, weakest claim.
- **D = 99** — worst case ≈ the 99th percentile. **What I proposed**, matching the conservatism used
  elsewhere in this study.
- **D = 999** — worst case ≈ the 99.9th percentile. Strictest, and roughly ten times the compute.

**One thing changed since I put this to you, and it is mine to fix, not yours.** CODEX showed tonight
that a receipt which lets someone **replay** the draws still cannot prove the count and the seed were
chosen **before** any verdict was seen — someone could try seeds quietly and report the set they
liked. That is a mechanism I have to build (freeze the count and seed in a committed artefact first),
not a number you have to choose. **It does not change the question above.**

---

## What is not being asked

**Nothing here asks you to unblock anything.** `successor_ref_v9.py` stays frozen at `6a9abbbd`, BS-6
and the first image byte stay blocked, γ̂ stays unmeasured, and option B of the gain mapping stays in
the record until its margin is re-derived at the real calibration. **Four findings from tonight are
mine to repair and I am doing them now** — the `MOVE_CAP` site's disposition, the gaps in the draw-set
specification, BS-3g's missing schema entry, and an overstated claim about what
`require_complete_sample()` checks.

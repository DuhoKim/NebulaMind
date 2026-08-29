**STATUS: THREE DECISIONS PENDING — with the principal, 2026-08-29 night.** **Item 2 was RULED at
22:18 while this page was being written — the catch-all is authorised — and it is kept below as the
record of how that ruling was reached, not as an open item. The three now pending are the partition,
`n_draws`, and `REFUSED-INTEGRITY-MISMATCH`.** Rewritten from the
morning version; all four of that version's items are ruled and their records live in the
`OPEN_QUESTION_*.md` files. **This is a plain-language index, not a source.** It asserts nothing the
underlying files do not already say, and if this page and one of those files disagree, the file is
right.

# What is on you tonight — DESI spin preregistration, night of 2026-08-29

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

## 2. The refusal vocabulary — RULED at 22:18. Kept here because how it was decided is the point

**RULED: non-closure is established; the catch-all is taken. The no-catch-all decision of 19:52 is
formally reversed, not merely suspended.**

**What the problem was.** When the mediator refuses to hand over data it writes a code saying why. That
set must be **closed** — no free text, nothing that leaks what was asked for. The safety of "no
catch-all" rested entirely on an argument that the set really covers everything.

**What happened.** Two independent closure arguments were written and **both were broken within an hour
of being written — by different countercases, both against the actual conduct table rather than against
a general theory.** The second broke on *"permitted is binary and evaluated before the attempt"*:
permission can be **undecided**, because Row B must verify another row's authorisation artefact first
and that verifier can time out or die **before returning a verdict**. The access has not completed and
was ruled neither permitted nor refused. **The instruction I was deriving against — the draft's own line
588 — lists the failures to cover and names "timed out" explicitly. The word does not appear once in
what I wrote.**

**Why the ruling is durable, and it is worth being explicit about the sequence.** The catch-all was
ruled **after** the derivation was attacked, not against it. Had it been decided against the
rederivation, it would have collapsed the same way the first one did and we would have found out in the
next round. **The gate before the ruling is the whole reason the answer holds** — and the reasoning
generalises: if closure cannot be shown, the escape hatch stops being a concession and becomes the
honest answer, and a routine verifier timeout stops voiding the study.

**What the ruling does NOT do — three things stay open and the catch-all must not be allowed to close
them.**
- **Permission is not made total and durable before fallible processing** (CODEX-VOCAB F1). The repair
  is a covenant fix, not a vocabulary fix: an explicit request state machine with a fixed terminal
  treatment for timeout and crash in each state, and a durable log boundary. **The catch-all makes the
  failure loggable; it does not make the permission decided.**
- **"Permitted before the attempt" is simply false for writes** (GPT56-VOCAB F1). For field-constrained
  writes on Rows C2 and H, whether a write is within the stated surface **cannot be known until Row B
  decodes the payload**.
- **`REFUSED-SCHEMA-NONCONFORMING` has to come back, or those refusals need a home.** Rows C2 and H
  write non-slot field-constrained objects **through Row B**, so moving the code to `receipt_strict()`
  does not classify the mediator's refusal of those writes.

**How the catch-all is written, per the ruling.** It carries **a code and nothing else** — no free
text, no appended detail. And because it will attract every refusal nobody wants to classify, the text
must state that **its use is a defect to be enumerated at freeze, not a routine outcome**: a catch-all
whose count is never reviewed becomes the vocabulary.

---

## 2a. A leak, and it does not wait on any of this

**Both seats found that Rows D and G permit χ-**adaptive** access patterns.** The vocabulary's
availability axis is only non-leaking while the set of objects read is fixed **χ-blind**. Under the
current draft it is not. **That makes availability refusals a χ-derived channel whichever vocabulary is
adopted** — the identity of the object refused can export which χ-derived branch was taken.

**This is a leak, not a taxonomy problem.** I raised the dependency myself when I proposed the axis and
asked whether the price was actually paid; the answer came back **no**. It is now its own finding with
its own repair and it is not waiting on anything above.

---

## 3. STILL YOURS — one number: how many draws does the gain gate take its worst case over?

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

## 4. STILL YOURS — `REFUSED-INTEGRITY-MISMATCH` stays flagged, and is now a third open item

**Both seats say it cannot be adjudicated at the moment the code is emitted.** A digest mismatch on a
sealed object may be an ordinary storage fault or it may be tampering, and **nothing observable at
emission distinguishes them.** CODEX adds that the same observable event is already claimed by the
**phase-Any digest-deviation VOID antecedent**, so the two collide. **Left flagged deliberately rather
than resolved:** getting this wrong toward VOID is how the earlier over-strict concern arose, and
getting it wrong the other way lets tampering be logged as a storage fault.

---

## What is not being asked

**Nothing here asks you to unblock anything.** `successor_ref_v9.py` stays frozen at `6a9abbbd`, BS-6
and the first image byte stay blocked, γ̂ stays unmeasured, and option B of the gain mapping stays in
the record until its margin is re-derived at the real calibration. **Mine to repair, and not waiting on you:** applying the catch-all and its anti-drift guard; the
request state machine the covenant repair needs; the write-side surface problem on Rows C2 and H;
bringing `REFUSED-SCHEMA-NONCONFORMING` back or finding those refusals a home; the χ-blind leak in 2a;
the `MOVE_CAP` site's disposition; the gaps in the draw-set specification; BS-3g's missing schema
entry; and an overstated claim about what `require_complete_sample()` checks. **Where any of those
turns out to change what the study promises rather than how it is written, it stops and comes back to
you.**

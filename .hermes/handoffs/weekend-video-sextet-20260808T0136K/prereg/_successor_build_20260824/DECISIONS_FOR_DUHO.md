**STATUS: FOUR DECISIONS PENDING — with the principal, 2026-08-29 night.** **Item 2 was RULED at
22:18 while this page was being written — the catch-all is authorised — and it is kept below as the
record of how that ruling was reached, not as an open item. Pending on you: the partition, `n_draws`,
`REFUSED-INTEGRITY-MISMATCH`, and — added 22:5x — Row F. The hand-check flag rule was RULED at 22:49
and is no longer on this list.** Rewritten from the
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

## 2a. The χ leak — the repair direction is RULED, and the one exception is a finding

**Both seats found that Rows D and G permit χ-**adaptive** access patterns.** The vocabulary's
availability axis is only non-leaking while the set of objects read is fixed **χ-blind**. Under the
current draft it is not. **That makes availability refusals a χ-derived channel whichever vocabulary is
adopted** — the identity of the object refused can export which χ-derived branch was taken.

**This is a leak, not a taxonomy problem.** I raised the dependency myself when I proposed the axis and
asked whether the price was actually paid; the answer came back **no**.

**RULED at 22:49, and both halves matter.** **(1) Option (a):** a precommitted χ-blind object set —
order, multiplicity, retries and stopping — enforced **before any χ-derived computation can influence a
later request**. Row D already conforms by construction and Row G's sequence is already built by the
design, so the clause largely **ratifies what is already true** — but **the seats' point was that the
covenant PERMITS adaptivity even though nothing uses it, and permission is what leaks, so the clause
FORBIDS it rather than observing its absence.** **(2) `flag → discard → replace` stays exactly as it
is**, on the principal's finding that **recognising a specific galaxy and judging its handedness are
separate judgements, and nothing about handedness is visible in the image.**

**That exception is recorded as a FINDING, never as a permission**, with its dependency written so it
can be checked: **if flagging ever becomes correlated with handedness — a different interface, visible
orientation cues, a checker who also sees instrument output — the exemption fails and the discard
record becomes a χ channel.** **A condition to be preserved, not a fact that stays true by itself** —
which is exactly the shape I wrote for the availability axis and the seats found unpaid.

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

## 5. ADDED 22:5x — Row F says it builds the hand-check allocation from χ-free inputs, and it cannot

**You asked me to settle the strata question before ruling on the flag rule. It is settled, and it
produced two separate things: one answer and one defect.**

**The answer: the draft is silent.** It never defines the nine hand-check strata — every mention points
at the predecessor study — and §10 already records *"the strata question"* as **undecided and
untouched**. The frozen code has a constant saying there are nine and **no function that puts an object
into one**. So I cannot tell you from this text whether the strata are χ-derived, and I have not
guessed. **What I can tell you is that the part Row F's void clause actually names — bin construction —
is provably χ-free: the bins are cut at position tertiles, not at |χ| tertiles.**

### 5a. The defect that does not depend on the strata question

**Row F is stated to read "positions and acceptance flags only" and to write "the hand-check
allocation". Positions and flags cannot produce that allocation** — it is a 3 × 9 table, and the
9-way part needs an input Row F is not allowed to read, **whatever the strata turn out to mean.** The
row promises an output it has no inputs for.

- **(a) Widen Row F's read surface** to include whatever supplies the stratum index. *Cost:* it admits
  the exact input the row was written to exclude, and **until the strata are defined nobody knows what
  that input is** — so this is signing a blank.
- **(b) Take the allocation out of Row F** and leave it the boundaries and bin labels, with the
  allocation produced where its inputs legitimately live. *Cost:* it splits an act the document
  currently describes as one, and changes who performs it.
- **(c) Keep Row F's surface** and require the 3 × 9 counts to arrive as a **pinned artefact produced
  elsewhere and verified**. *Cost:* another slot and another verifier, on a document that already has
  four slots deliberately empty as blockers.

### 5b. The one that fires at freeze if nothing changes

HC-1H's rules enter this preregistration **"by quotation at freeze"**, and HC-1H defines the nine strata
as **machine-committee state × |χ| tertile**. **If that is the definition quoted, then on freeze day
Row F is stated to build, from χ-free inputs, an allocation over strata defined by |χ| — and its own
void clause fires on its own emission.** Same shape as Row L signing what its void condition forbade,
and arriving at the worst moment, because **the freeze signature covers the text containing it.**

- **(a) Define the strata in this document, χ-free** — for instance on machine-committee state alone.
  *Cost:* it departs from the inherited design, and HC-1H's floors and estimator were validated
  **together with** its strata; changing one may invalidate the others.
- **(b) Quote HC-1H as it stands and fix Row F instead** — accept the allocation is χ-derived, drop the
  χ-free claim, and route it through a row permitted to read χ. *Cost:* **the allocated universe Row G
  sees is then χ-conditioned**, which sits upstream of the access-schedule question you are already
  holding.
- **(c) Scope the quotation** — inherit HC-1H's measurement and validity rules but not its
  stratification, and define stratification here. *Cost:* partial inheritance needs its own argument,
  for the same reason as (a).

### 5c. ADDED 23:04 — you told me to name the input Row F needs. It is χ-bearing on BOTH axes

**The expected answer was "drop the |χ| axis and the stratification becomes χ-free." That is false.**
The stratum index is **machine-committee state × |χ| tertile**, and the committee state is *"agree-
confident / disagree / low-confidence"* over two classifiers **judging handedness** — a per-object
machine handedness judgement. Under this document's own rule that **doubt resolves toward χ-bearing**,
both axes are χ-derived. **There is no χ-free version of HC-1H's stratification that keeps its
structure; a χ-free one would be a different design.**

**And the cost of redefining is smaller in one way than feared and harder in three others.** Validity
survives: `a` is a population-weighted mean with a **global** noise correction, so it estimates the
same quantity under any partition, and HC-1H says it itself — *"a bad allocation costs efficiency,
never validity."* **But:** `N_HC_STRATA = 9` is a **frozen constant in v9**, so a different number of
strata cannot be expressed without unfreezing; **σ_a would rise, and σ_a is exactly what the power
floor tests**, so an efficiency cost can still turn a passing gate into `INCONCLUSIVE-BY-POWER`; and
the natural χ-free substitute axis is **image quality, which §2.7 measures as correlated with the axis
under test** — coupling the calibration to the signal geometry.

**Three ways, and I am not choosing.** **(A)** accept χ-derived strata and restructure Row F — the
allocation stays sealed, and V65's precommitted traversal now forbids the adaptive requests that turned
χ-conditioning into a log channel. **(B)** redefine χ-free — a new design, nine strata or nothing,
paid for in precision. **(C)** keep the strata and move construction out of Row F — relocates the
χ-conditioning rather than resolving it.

### The ordering, because it changes what you are choosing between

**5b has to be answered before 5a can be repaired well.** Which surface repair is right depends on what
input the allocation actually needs, and that is exactly what 5b decides. **Answering 5a first would be
picking a shape for a hole nobody has measured.**

**And 5b(b) touches the leak.** If the allocated universe is χ-conditioned, then Row G's universe is
too — which is the premise the access-schedule question rests on.

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

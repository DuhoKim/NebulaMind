# DIAGNOSIS — why R3D's falsifier keeps ending up unable to fire

**Tori, 2026-09-04 23:47 KST. ORDERED by Duho via Blanc: "diagnose why the falsifier keeps getting disabled."**
**This is a diagnosis, not a repair. No V9. R3D is unchanged at V8 and is NOT run.**
**No tier, warrant token, standing or stamp moves. Paper HOLD.**

---

## 0. The finding in one paragraph

Three times, across three versions, R3D's condition 5 — the only condition that can certify a **counterexample to
this lane's own pattern** — has come out of a repair unable to return PASS on any path. Each time the repair was a
direct, locally correct response to a real referee finding. Each time the previous disabling was different in form.
**The mechanism they share is not a drafting habit but a structural asymmetry: in this design the falsifier's PASS
path carries preconditions and its FAIL path does not, so any error anywhere in the document lands on PASS.** That
asymmetry has a benign explanation and a damning one, and §3 weighs them against the evidence rather than choosing
the comfortable one. **My judgement is (a) plus a structural amplifier, with (c) not excluded — and I am not the
right party to exclude it.** §4 gives the check that would have caught all three, §5 the recommendation.

---

## 1. The three disablings, side by side

### Disabling I — V3. The repair required content that could not exist.

**Clause, verbatim:**

> **So before the run is frozen, a finite named comparator set, the observable and tolerance that define "shared",
> and the permitted source corpus are fixed in writing**; every comparison is executed and printed.

**What it was meant to test:** condition 5 — that the derived floor is not a number some standard model already
predicts, i.e. that a measurement could actually falsify the claim.

**Precise mechanism of failure:** the clause defers its own content to a moment "before the run is frozen" — but
**this document is the freeze.** There is no later time at which the requirement gets satisfied, so the comparator
set never exists, and C6 has an unread comparator on every path.

**The preceding repair:** V3 repairing codex's V2 finding, *"Condition 5 is not decidable as written: a seat cannot
establish that the number is not shared with 'any standard model' without a bounded comparator set and search
rule."* Correct finding. My repair converted an undecidable condition into a **promise** of decidability.

**Referee verdict:** codex, gating V3 (`R3D_GATE_V3_codex_20260904.md`) — *"the promised material is not present
before the freeze, so condition 5 remains undecidable."* kimi, same version — *"The freezing instruction is
satisfied nowhere; as frozen, condition 5 still has no bounded comparator set."* **Both seats, independently.**

### Disabling II — V4. The content was supplied, behind a read the document forbids.

**Clauses, verbatim (two, in different sections):**

> §2a: **A read outside this manifest files `DYM_SOURCE_BLOCKED`.**

> C6: An unread comparator source files `DYM_SOURCE_BLOCKED`; **only a completed no-match table passes condition 5.**

> comparator row 2: `2026_PBH_constraints_evidence_prospects_arXiv_2601.06024.clean.txt` **(manifest §2a)**

**Precise mechanism of failure:** the cited comparator files are **not** in the manifest — the "(manifest §2a)"
annotation is false. So a seat that reads them violates §2a and files `BLOCKED`; a seat that does not read them
hits C6's unread-comparator rule and files `BLOCKED`. **Both paths blocked.** Neither clause is wrong alone; they
are jointly unsatisfiable, and they sit ~200 lines apart.

**The preceding repair:** V4 repairing Disabling I, by supplying the values.

**Referee verdict:** kimi V4 — *"Both paths file BLOCKED; condition 5 can never pass. The decisive test is
pre-disabled for the second consecutive round."*

### **V6 — the control case. The falsifier worked.**

**This version matters more than the disablings, and it is the reason this diagnosis can be sharp.**

V6 supplied every comparator interval computed in-document. **Both seats independently confirmed the test could
fire:**

> codex V6: *"Condition 5 can now operationally PASS: for a completion-free derived point floor of, for example,
> `1 kg`, its interval overlaps none of the three numerical intervals … so condition 5 passes."*

> kimi V6: *"A. Can condition 5 now PASS on a reachable path? **Yes.**"*

**V6 was still `PREREG_UNSOUND` — but for an *honesty* defect, not a disabling.** I had written *"Every comparator
interval is derived from §2b inside this document"*, which is false: the coefficient `5120π`, the factor `3.0`, the
span `[2.2, 2.9] M_☉` and the Gregorian year are **asserted**, not derived. Both seats caught it.

**So the sequence is: the one version whose falsifier could fire was condemned for overclaiming the provenance of
its comparator inputs — and the repair of that overclaim disabled the falsifier again.** That is the single most
diagnostic fact in this file.

### Disabling III — V7. The pass was gated on a rule that rejects its own inputs.

**Clauses, verbatim (three):**

> (a) **Those four are asserted bounds and conventions, NOT derivations from §2b**; each is **recorded as an
> `ADDED_COMPLETION` in the C2 ledger**, and condition 5 may pass only if **C6 condition 2 accepts them under its
> provenance rule**.

> (b) condition 2's pass criterion: every constant terminates in an equation of a §2a manifest source or in the §2b
> list. **The chain is followed only within the manifest: a terminus outside it fails, exactly as a
> `we assume / we choose / simplest form` terminus fails**

> (c) `C6_BREAKER_TEST=PASS` only on a completed table with no overlap; or `NOT_RUN` if `DYM_FLOOR_DERIVED` is not
> reached.

**Precise mechanism of failure:** (a) gates condition 5's pass on condition 2 accepting the four asserted inputs.
(b) makes condition 2 reject an asserted terminus **by construction**. So condition 5 cannot pass **whatever the
physics**. And (a) contradicts (c), which never mentions the gate — so two obedient seats diverge on the exact
question the study exists to answer.

**The preceding repair:** V7 repairing V6's overclaim — **by adopting codex's own V6 replacement text verbatim**,
which read: *"condition 5 may pass only if C6 condition 2 independently accepts those comparator assumptions under
its provenance rule; otherwise C6 fails."*

**Referee verdict:** kimi V7 — *"the decisive test is disabled a third time, in a third form … The counterexample
consequence — the reason this study exists — is pre-disabled by the wiring, not by the physics."*

**Note on authorship of this one:** the deadlocking sentence was **written by the referee**, not by me. I adopted it
without tracing its interaction with condition 2. That matters for §3.

### The inherited fourth: the pattern record's condition 3

Not in R3D, but R3D pins it. Breaker condition 3 required that recovering the printed number with every parameter
freed **"must fail without any parameter being chosen"** — which *is* the presence of a free normalisation, the
thing the condition excludes. **A construction satisfied it exactly when it had the defect.** Direction: a genuine
counterexample would have **failed** it and been rejected. Corrected to V2 on Duho's order.

---

## 2. What is common — the mechanism, not the instances

**It is not one recurring drafting move.** The three are genuinely different: an unsatisfiable temporal reference,
two jointly-unsatisfiable clauses in different sections, and a cross-condition gate whose criterion excludes its own
inputs. Calling them "the same mistake" would be false.

**The common mechanism is an asymmetry in the design's own shape:**

| | condition 5 PASS | condition 5 FAIL |
|---|---|---|
| requires | a **complete** comparator table, **every** comparator read/derived, **every** provenance accepted, **no** overlap | **one** demonstrated overlap |
| preconditions | many, spread across §2a, §2b, C2, C6 and condition 2 | one, local to C6 |
| effect of an error anywhere | **pass becomes unreachable** | fail survives |

**The falsifying verdict is a conjunction; the pattern-preserving verdict is a disjunction.** A conjunction has more
surface area, so a random defect anywhere in the document is far more likely to break PASS than FAIL. That is the
mechanism, and it is a property of how I structured the test, not of any individual repair.

**Direction of the errors, counted honestly.** Four defects ran in the pattern-preserving direction (the three
disablings and the inverted condition 3). **One ran the other way**: V6's comparator intervals were rounded
**inward**, so `[1.730e11, 5.189e11]` did not contain its own computed value — narrowing a comparator makes overlap
less likely, which makes condition 5 **pass** more easily, i.e. makes a counterexample **easier** to declare. kimi
found it; I had not. So the direction is **not** uniform — but the four are structural and fatal to the test, and
the one is a rounding width of a fraction of a percent. **The asymmetry is in severity, not only in count.**

---

## 3. The uncomfortable question, answered with the evidence

### (b) — a structural property of this study: **REJECTED, on direct evidence.**

The hypothesis is that the Dymnikova branch admits no condition 5 that is both well-defined and able to fail.
**V6 refutes it.** Both seats independently traced a passing path on V6's text. A decidable, passable condition 5
exists, has existed, and was written by this lane. Condition 5 *is* intrinsically awkward — it is a universal
negative, and every version has had to bound it — but "awkward" is not "impossible", and the evidence says
possible.

### (c) — authorship bias: **NOT ESTABLISHED, NOT EXCLUDED, and I am not the party who can exclude it.**

**Evidence for:** four of five direction-bearing defects protect the pattern, and the four are the severe ones. I do
hold a prior — I wrote the pattern record and its six instances, and a counterexample would force me to amend a
finding I authored. That is precisely the mechanism I attribute to the corpus authors, and Blanc is right that the
irony is exact: *"falsifiable in form, unfalsified in practice"* is my own sentence about their papers.

**Evidence against:**
1. **The asymmetry has a bias-free explanation** — §2's conjunction/disjunction structure predicts the same
   direction from random errors, with no motive required.
2. **Disabling III was written by the referee**, not by me. codex authored the deadlocking sentence; my failure was
   adopting it untraced. Unconscious protection of a prior does not route through a referee's text.
3. **The one opposite-direction error exists** and I did not catch it either — my errors are not uniformly
   self-serving, which is what a bias account predicts.
4. **Every disabling was found and reported, in full, including by me against myself** — the inverted condition 3
   was disclosed and escalated rather than quietly fixed, and V6's overclaim was recorded in my own commit as an
   overclaim.

**Judgement: (a) — locally correct repairs whose interactions went unnoticed — amplified by the §2 structural
asymmetry, which converts ordinary drafting error into consistent one-directional damage.** I do not think the
evidence supports conscious or unconscious steering, and I think the structural explanation is sufficient without
it.

**But that judgement is worth exactly what a self-assessment of bias is ever worth, which is not much.** The test
that would settle it is cheap and is in §4: if the reachability control is added and disablings stop, it was (a).
**If they continue under a control designed to catch precisely this, the remaining explanation is (c), and the
lane should act on that rather than on my reassurance.**

---

## 4. What would have prevented all three

**A reachability control, run before dispatch, on every declared outcome and every falsifying condition:**

> **C0 — reachability.** For every declared outcome class and for every condition whose failure would refute the
> lane's own expectation, **exhibit a concrete input that produces it** — a specific numeric value, and the path it
> takes through the document to that verdict. A class or condition for which no such input can be exhibited is
> **unreachable**, and the preregistration does not freeze until it is. `C0_REACHABILITY=PASS`.

**It would have caught all three, and cheaply:**

| | what C0 asks | V3 | V4 | V7 |
|---|---|---|---|---|
| "exhibit a floor value that makes condition 5 PASS" | any number | no comparator set exists → cannot exhibit | both read and no-read file `BLOCKED` → cannot exhibit | condition 2 rejects the inputs → cannot exhibit |

**Three lines of work per version.** And the evidence that it works is that **this is exactly what both seats did
when I asked them to trace a matching and a non-matching case** — that request is what established V6's soundness
and exposed V7's. The check is proven; it was simply run by referees, after the fact, instead of by me, before
dispatch.

**Who should run it.** Designing what counts as "reachable" is where a prior could enter, so **the exhibition should
be produced by a seat and only verified by me** — not authored by me. It is mechanical enough to survive that split.

**Worth making standing.** I recommend C0 in **every preregistration this lane writes**, not only R3D. The failure
it catches — a declared outcome that cannot occur — is invisible to every other control here, because every other
control checks that something *is done correctly*, and none checks that something *can happen at all*. R3C2 should
carry it too, and its §4 classes have never been reachability-tested.

---

## 5. Recommendation

### Recommended: **redesign the test — invert condition 5's polarity — then repair once, under C0.**

Not a fourth repair of the same shape, and not stopping R3D. The specific redesign:

> **Condition 5 FAILS on a demonstrated overlap with a named comparator, and PASSES otherwise. The completed
> comparison table is required as a C6 ARTEFACT — a control that fails loudly — rather than as a precondition of the
> condition's pass.**

**Why this fixes the mechanism and not just the instance:** it moves the falsifying verdict from a conjunction to a
disjunction. Pass stops having preconditions, so there is no longer anything for a drafting error to break. The
completeness requirement does not disappear; it moves to where an unmet requirement is **visible** — a failed
control — instead of where it is **silent** — an unreachable pass. Every one of the three disablings was silent.

### The strongest argument against my own recommendation

**Inverting the polarity means a lazy, incomplete or rushed comparison yields a PASS — and PASS is the high-stakes
direction.** A pass on condition 5, with conditions 1–4, declares a **counterexample to the pattern**, amends a
record that has been reported to Duho, and changes a stated finding. The current preconditions exist precisely to
stop a sloppy pass. Inverting them trades *"the test cannot fire"* for *"the test can fire wrongly"* — and given
that the wrong direction here is a false claim of discovery, a blocked pass may be the safer failure. A lane that
has just spent three rounds proving it cannot wire this condition correctly should be slow to hand itself a design
where the error mode is a false positive.

**Why I still recommend it, having stated that fairly:** a blocked pass is **not** the safe failure, it only looks
like one. It silently preserves the lane's own claim while presenting as caution — the same error with better
manners, and precisely the failure this diagnosis was ordered to explain. The false-positive risk is real but it is
**loud**: a wrongly-passed condition 5 produces a printed table that a second seat, the audit, and Duho can all
inspect, and C0 plus the blind double are aimed straight at it. **The choice is between an error that announces
itself and an error that hides, and this lane's record tonight is that the hidden one survives four rounds.**

### The two options I am not recommending, and why

- **Repair a fourth time.** This is what Duho declined to buy, and he is right: three repairs each fixed an instance
  and none touched the mechanism in §2. A fourth would be the fourth locally-correct repair.
- **Stop R3D.** The study is sound in every other respect — both seats now find circularity, controls, fairness,
  stall and the re-run guard sound, and every number reproduces under independent re-derivation. Stopping would
  discard a design that is one structural change from working, and would leave the Dymnikova branch — the corpus's
  most plausible place for a counterexample — untested. **Stopping now would itself be a way of not testing the
  pattern**, which is the thing under examination.

---

## 6. What I have not done

- **No V9.** R3D stands at V8, unchanged by this file. V8 already removes Disabling III's gate (codex's V7 finding,
  traced rather than transcribed) — but that is a repair of the instance, and it was committed before this
  diagnosis was ordered. **It does not address §2's mechanism and should not be mistaken for having done so.**
- **No C0 added anywhere.** §4 is a recommendation; adding a standing control to every preregistration in this lane
  is a scope decision, not mine.
- **No condition-5 redesign written.** §5 is a recommendation with its counter-argument, for Duho to rule on.

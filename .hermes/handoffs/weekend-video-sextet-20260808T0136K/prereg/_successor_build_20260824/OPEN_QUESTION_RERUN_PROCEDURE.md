# OPEN QUESTION — the rerun procedure I wrote is incoherent, and both seats say so

**Raised 2026-08-29 11:4x KST by Hwao from the V40 round. Both seats NOT CLEAR (GPT56 7 findings,
CODEX 4), converging on the same three HIGH problems. All three are in text I authored, and fixing
any of them changes what the study claims.**

## The thing to be clear about first

**The principal's ruling did not ask for a rerun.** Option C was: qualify §5's numerical trigger to
post-unblinding, and *route pre-unblinding permutation/statistic failures to an inconclusive code
alongside the calibration one*. That is done, and neither seat challenged it.

**The rerun procedure is mine.** Blanc asked me to name what the operator does, on the correct ground
that an inconclusive code which does not say what to do is a label rather than a rule. I wrote a
five-step rerun allowance. **That elaboration is where every one of the three HIGH findings lives.**

## What both seats found

**1. A computation halt is simultaneously terminal and retryable (GPT56 F1, CODEX F1).** §5 emits it
as a run outcome while my step 2 permits re-running Stage C, and §6.1 Row J's halt contract says the
run ends with exactly one outcome. GPT56 adds that Row J assigns conflicting POWER and VOID
consequences on the same path. The document now says two incompatible things about the same event.

**2. The rerun is either pointless or a forking path (GPT56 F2, CODEX F2).** Under the *same* frozen
implementation and protocol digests, a rerun is deterministic repetition — it reproduces the failure
and changes nothing. If the random address moves, the operator is drawing again, and CODEX notes the
rerun address is *selectable*. My step 4 forbids rerunning on a finite result, but both seats find the
attempt log has **no authenticated schema and no verifier**, so the prohibition is unenforceable —
nothing can tell a permitted rerun from a forbidden one after the fact.

**I flagged this exact clause in the dispatch brief as the part I was least sure survived contact
with an operator. It did not.**

**3. The attempt cap has no dependency edge (GPT56 F3, CODEX F3).** I wrote that the maximum attempt
count "must be pinned before BS-6" — **and gave it no class-P slot, no schema, no producer and no
edge.** That is precisely the defect I repaired for BS-3g four hours earlier, reintroduced by me in
the sentence where I congratulated myself for naming an unbound parameter out loud. Declaring a hole
is not closing it, and a declared precondition with nothing enforcing it is the same false claim in a
more self-satisfied register.

## The options

**A. Delete the rerun allowance. The halt is terminal.** `INCONCLUSIVE-BY-COMPUTATION` ends the run;
the operator's recourse is a new run under a new preregistration, not a retry inside this one. This
satisfies the ruling exactly, restores consistency with Row J's one-outcome contract, and dissolves
findings 1, 2 and 3 together — no seed policy, no attempt log, no cap, no new slot.
*Cost:* "what the operator does" becomes "nothing, within this run". A bad night ends the run. That is
strict, and it is the honest answer if a rerun cannot be made enforceable — but it is less than Blanc
asked for.

**B. Keep the rerun and make it coherent.** Needs four normative changes: reconcile Row J's terminal
contract with a retryable state; freeze a seed schedule so a rerun is neither a repeat nor a free
draw; specify an authenticated attempt-log schema with a verifier; and add a class-P slot for the cap
with a `blocks BS-6` edge — **moving counts 16/8 → 17/8**.
*Cost:* four changes to what the study claims, one of which moves the frozen inventory again, to
defend a capability nobody has asked for operationally.

**C. One documented re-execution, declared in advance.** A middle: exactly one Stage-C re-execution
before unblinding, under a seed schedule frozen in this text, recorded. *Cost:* still needs the
authenticated log and verifier from B, and still needs the cap slot — it reduces B's scope without
removing B's hard parts.

## My reading, not my decision

**A.** The ruling is satisfied without a rerun; the rerun is my addition; and it is the part that
broke. A terminal halt is what §6.1 already contracts, so A removes a contradiction rather than
adding machinery to sustain one. **A also answers Blanc's question honestly** — the procedure is
"the run ends, and a re-attempt is a new run under a new text", which is a rule an operator can
follow without a further decision.

**What would change my mind:** if operationally a pre-unblinding numerical failure is expected often
enough that ending the run each time is untenable. I do not know that, and it is not mine to assume.

## Held pending this decision

**GPT56 F5 (INCONCLUSIVE-BY-CALIBRATION / -BY-COMPUTATION overlap) and F6 (the §2.7 citation is
*still* wrong after my V39 repair) are not fixed yet, deliberately** — F5 edits text that option A
deletes, and fixing it first would be repairing prose about to be removed. **F6 is independent and
will be fixed regardless**; it is held only to avoid two drafts in flight.

**GPT56 F4 / CODEX F4 (BS-3g missing from §6.1's exhaustive receipt schema) is independent of this
decision and will be repaired next**, since BS-3g's BS-6 edge is not receiptable without it.

## Already fixed, because it invalidated my own reporting

**GPT56 F7 — the VOID checker's self-test was failing.** GPT56 attributed it to my V40 trigger
syntax; that is wrong, and the truth is worse. **It broke at V37**, when the principal's option A
closed the three gaps the control asserted must still be found, and it stayed red through V37, V38,
V39 and V40 **while I reported that checker's output on all four drafts**. Its second half was also
vacuous — it patched a `VOID-5-DEGENERATE` row into the live text and checked for silence, which
became a no-op once that row genuinely existed. Both halves now run against fixtures and test the
mechanism rather than a transient state of the document: 6 controls, 0 failures, on V34 through V40
alike.

**The lesson is mine and it is the lane's own rule:** I ran the main path and not `--self-test`, and a
check whose battery is red proves nothing.

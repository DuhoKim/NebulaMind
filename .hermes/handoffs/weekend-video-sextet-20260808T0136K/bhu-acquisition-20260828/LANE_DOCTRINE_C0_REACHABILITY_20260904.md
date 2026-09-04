# STANDING LANE DOCTRINE — C0, reachability — every preregistration this lane writes

**Tori, 2026-09-04 23:52 KST. ORDERED by Duho: "redesign condition 5 and add C0 to every prereg."**
**No tier, warrant token, standing or stamp moves. Paper HOLD.**

## The control, to be copied verbatim into every new preregistration

> - **C0 — reachability, run BEFORE the freeze.** For **every declared outcome class**, and for **every condition
>   whose failure would refute this lane's own expectation**, **exhibit a concrete input that produces it** — a
>   specific value or configuration, and the path it takes through the document to that verdict. **An outcome for
>   which no such input can be exhibited is UNREACHABLE, and the preregistration does not freeze until it is.** The
>   exhibition table is the artefact. **The exhibitions are authored by a seat and only verified by the lane owner.**
>   `C0_REACHABILITY=PASS`.

## Why the authorship split is not optional

**The exhibitions are written by a seat, never by the person who wrote the outcome classes.** Deciding what counts
as "reachable" is exactly where an author's prior can enter: someone who expects outcome X can convince themselves
that outcome not-X is reachable in principle without ever constructing the input. **The author verifies; the author
does not exhibit.** The check is mechanical enough to survive that split.

## What C0 catches that nothing else does

Every other control in this lane's preregistrations checks that something **is done correctly**. **None checks that
an outcome can happen at all.** That gap is not theoretical: in R3D, **three consecutive repairs** left condition 5
— the only condition capable of certifying a counterexample to this lane's own pattern — unable to return `PASS` on
any path, **each time in a different way, each time after a locally correct repair of a real referee finding**, and
no control in the document could see it. The full account is in `R3D_FALSIFIER_DISABLING_DIAGNOSIS_20260904.md`.

**The check is proven, not speculative.** It is precisely what codex and kimi did when asked to trace a matching and
a non-matching case — that request is how V6's soundness and V7's defect were both established. C0 only moves it
from *referees, after dispatch* to *the lane, before the freeze*.

## Where it is now installed

| preregistration | status | C0 |
|---|---|---|
| `R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md` | live, V9, not run | **installed** |
| `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` | live, V8, not run | **installed** |
| every future preregistration this lane writes | — | **required at freeze** |

## Where it is deliberately NOT installed, and why

**The closed studies' preregistrations are NOT edited: K3s2, K3s3, K4, K5, K6, R3A, R3B, K2.** Each is frozen and
its result is filed against that frozen text. **Adding a control to a preregistration after its study has reported
would corrupt the record** — the document would no longer be the one the study was run under, and this lane's whole
discipline rests on that correspondence. **Archive, never delete; and equally, never retrofit.**

**That is not the same as leaving them unexamined.** A retrospective reachability *screen* — an audit that reads
those preregistrations without touching them — is the right instrument, and a first pass is below.

## Retrospective screen — was any CLOSED study's refuting outcome unreachable?

**This is a screen, not the audit.** It asks one question per study: *could the outcome that would have refuted the
lane's expectation actually have been filed?* Where the answer is "yes, and it was", the study is self-evidently
sound on this axis, because the refuting outcome **is** the filed one.

| study | outcome that would refute the lane's expectation | reachable? | evidence |
|---|---|---|---|
| K3s1 / K3s2 | a derived, regime-independent closure coefficient | **yes** | the study filed a derived coefficient; it came out negative and species-dependent, which is a result, not a block |
| K3s3 | the four-fermion term being negligible at the bounce | **yes** | reachable and nearly filed; the 2/3 value was computed, not blocked |
| K4 | the junction closing as a boundary condition | **yes** | the study returned `UNDETERMINED` **after** computing the free Zerilli data — the closing case was computable |
| K5 | a determinate ringdown amplitude | **yes** | `K5_AMPLITUDE_FREE` was filed under a class that had a determinate sibling reachable on the same limb |
| K6 | a positive ECKS mass floor | **yes** | `K6_FLOOR_UNDERDETERMINED` was filed **because three admissible readings gave different floors** — floors were derivable |
| R3A | β tracing to a derivation | **yes** | the citation chain was followed to its end; a deriving reference would have been found had one existed |
| R3B | `w = −1` rigid without an assumed constant `M_T` | **yes** | the study located the conditional statement and the permitted `M(τ)`; a derived constancy was findable |

**Screen result: no closed study shows a refuting outcome that was unreachable by construction.** In every case the
refuting outcome required a quantity that the study actually computed or actually searched for, and the negative
result came from what was found, not from a rule that made the positive unfileable.

**Stated with its limit:** this is a screen by the person who wrote those studies, on documents I authored. **It is
exactly the kind of self-assessment §3 of the diagnosis says is worth little.** If Duho wants it to count, it
should be re-run by a seat against the frozen texts, blind to these answers. **I recommend that, and I have not done
it, because a seat-run audit of seven closed studies is a scope decision rather than a continuation of this order.**

## The two failure modes this doctrine exists to stop

1. **A falsifying verdict built as a conjunction while its opposite is a disjunction.** Preconditions concentrate on
   one side; every drafting error then lands there. **State the refuting verdict as the low-precondition path**, and
   carry completeness requirements as controls, which fail loudly, rather than as preconditions, which fail
   silently.
2. **Repairing by requiring content rather than supplying it.** Three R3D rounds died on this. **A preregistration
   is the freeze: content it defers to "before the freeze" is content it never gets.**

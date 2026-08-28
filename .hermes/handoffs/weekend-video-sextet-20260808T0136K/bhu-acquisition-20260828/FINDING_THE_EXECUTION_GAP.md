# The execution gap

**A cross-lane finding, 2026-08-29. Tori (BHU) and Hwao (DESI), independently, same night.**

> **Tonight's entire defect class is claims made without executing the thing that would falsify
> them. The gap between "I edited it" and "I ran it" is the same gap as between a check's NAME and
> its PREDICATE.**

Filed as a standalone document rather than a note inside a register, because it did not stay
inside one lane, one framework, or one artefact type. Blanc relayed it between lanes and it
matched immediately on the other side.

## The instances

Eight, from two lanes. Every one is a statement that describes a verification while performing a
different one — or none.

### In checks (Tori)

1. **Names that outran predicates.** A check called "the causal scale is set by the measured Ω_Λ"
   whose predicate confirms two equations *appear*. Six consecutive gates found this shape.
2. **A tautology.** `w_implied = -1.0 - (0.0)/(3*H*rho)`, then asserting it equals −1. Independent
   of H, of ρ, and of the paper.
3. **Hardcoding standing in for reading.** `W0 = 0.0062` and `63` both typed in by hand, in the
   script whose finding *survived* its gate. It passes on an empty file.
4. **Absence claims on narrow patterns.** Three false "zero" claims, all from one regex used to
   prove a thing was *not there*. → the sub-rule: **narrow patterns are safe for presence,
   dangerous for absence.**
5. **A classifier blind to its own target.** Built to find tautologies; measured against ground
   truth at 4/8, and **0/1 on tautologies** — `abs()` sits in its data-driven call set, so the one
   real tautology in the battery would have been cleared by the tool built to catch it.

### In documents and guards (Hwao)

6. **A dependency asserted with no edge behind it.** V34 states a sensitivity-gradient control
   "must be bound before BS-6". No class-P slot, no gate row, no receipt makes that true — an
   operator can satisfy every enumerated dependency and reach BS-6 with the control unbound. The
   lint and trace **confirm the inventory as complete**, because they check the thing they were
   built to check rather than the thing the sentence claims.
7. **A guard that computes nothing.** `require_authorization()`, frozen, executed against a
   referee brief and returned success: it verifies only that the caller-supplied path and hash
   agree *with each other*.

### In the record of the work itself (Tori)

8. **Commit messages asserting a state that was never run.** A commit claiming "a2 now 12/12"
   when the script raised `NameError` and aborted after two checks. Two scripts, one hour, while
   documenting instances 1–5.

## Why it is one defect and not eight

Each case has the same shape: **an artefact that reports on a property it does not evaluate.** A
check name, a lint pass, a guard's return value, a commit message, a classifier's label. The
artefact is honest about *something* — it just isn't the thing being claimed. That is why none of
these were caught by re-reading. Re-reading confirms the description. Only execution against an
input that *could* fail separates the two.

## The corollary rule, from the a14 crash

> **A retraction is not complete until nothing still reads the retracted value — and only
> execution shows you that.**

I withdrew a false count, rewrote the check that produced it, and left the tier conclusion still
reading `counts[24] == 0`. The retraction looked complete from outside and was not. A `NameError`
exposed it; no amount of reading would have.

## What follows from it

- A check may be named only for what its predicate evaluates. Presence tests get named as
  presence tests; absence claims name their pattern's blind spots.
- Values a claim depends on are **parsed from the source or the claim is not made.** If the parse
  fails, abort — never fall back to a literal.
- **Validate an instrument against ground truth before trusting it**, including instruments built
  to validate other instruments. A tool that cannot fail on a known-bad input certifies nothing.
- Run it before you say it ran. This is not a coding-hygiene point; it is the same defect as all
  the others, applied to one's own report.

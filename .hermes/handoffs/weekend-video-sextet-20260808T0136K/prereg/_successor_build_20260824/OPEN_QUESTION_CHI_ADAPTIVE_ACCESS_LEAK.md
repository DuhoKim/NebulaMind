**STATUS: RULED AND APPLIED — 2026-08-29, both halves. Not pending on the principal.**
**(1) Option (a):** the access schedule is **precommitted and χ-blind** for every row that may read a
χ-bearing object — order, multiplicity, retries and stopping — with **Row B refusing any request that
is not the next unserved position**. Applied in **V65**. **The clause FORBIDS adaptivity rather than
observing that nobody currently uses it**, because the covenant permitted it and **permission is what
leaks**. **(2) `flag → discard → replace` STAYS UNMODIFIED**, on the principal's finding that
**recognising a specific galaxy and judging its handedness are separate judgements, and nothing about
handedness is visible in the image**. That exemption is recorded **as a finding, never as a
permission**, and is **bound to the pinned digest of the Row G interface** so a different interface,
visible orientation cues, or a checker who also sees instrument output **lapses it**.
**What this file left behind and did NOT settle:** the strata question it pointed at is now its own
finding — `FINDING_ROW_F_STRATA.md` — and **that one is still with the principal.**

# OPEN QUESTION — Rows D and G permit χ-adaptive access, so refusing on an object can export χ

## The condition, and why it was ever stated

The refusal vocabulary's **availability axis** — *the access was permitted and could not be completed*
— is safe only under one condition I wrote when I proposed it: **the set of objects read is fixed
χ-blind.** If the set is fixed without reference to χ, then *which* object a refusal names carries no
information about χ, and an availability refusal is a fact about storage rather than about the sky.

**I flagged that as the price of admitting the axis and asked the seats whether the price is actually
paid. The answer came back no, from both, against different rows.**

## What they found

- **CODEX — Row D.** The row permits **χ-adaptive cutout scheduling**. If the order or membership of
  requested objects can depend on a χ-derived branch, then the identity of the object a refusal names
  **exports which branch was taken**.
- **GPT56 — Row G.** The row permits **adaptive χ-conditioned requests**, violating the fixed χ-blind
  object-set condition directly.

**This holds whichever vocabulary is adopted**, including the catch-all set ruled at 22:18. The leak is
in **what the conduct table permits**, not in how a refusal is named — no choice of codes repairs it,
because the channel is the object identity, not the reason string.

## Why this is not mine to fix

Every repair I can see narrows what Rows D and G are allowed to do, and that is a change to what the
study permits rather than to how it is described.

- **(a) Require the object set be fixed χ-blind before any Row B request.** The condition becomes a
  covenant clause rather than an assumption, with the manifest pinned in advance. *Cost:* it forbids
  adaptive scheduling outright, which those rows currently permit and which may exist for a reason —
  I have not established that the adaptivity is unnecessary, only that it leaks.
- **(b) Allow adaptivity but forbid per-object refusal reporting** — refusals aggregate to a count over
  the pinned manifest and never name an object. *Cost:* it degrades operational diagnosis, and an
  aggregate count with a χ-adaptive membership may still leak at the margin; that would need its own
  argument rather than an assertion.
- **(c) Record it as a stated limitation and proceed.** *Cost:* the study would carry a known channel
  from χ to the access log. **The whole blinding covenant exists to prevent exactly this**, so I do not
  think this survives being written down plainly — but the option is listed rather than suppressed,
  because deciding it is yours.

## DEPENDENCY ESTABLISHED — `FEASIBILITY_CHI_BLIND_ACCESS_SCHEDULE.md`, 2026-08-29 22:30 KST

**The principal asked whether the adaptivity is load-bearing before ruling. The answer is: almost
nothing depends on it, and one thing does.**

- **Row D — nothing.** Established **from the code**, not the table: `_cutout_runner_20260820` has no
  retry, no re-request and no reordering, its read set must equal the supplied manifest exactly, and its
  README states it *"contains no acquisition or selection query."* Limits: it is the composition layer
  only, and BS-3 is undelivered, so no acquisition code exists to examine.
- **Row G — the design forbids choosing what to view next**, because the 200 interleaved synthetics and
  150 mirrored re-presentations depend on a sequence the design controls. **But `flag → discard →
  replace` is genuinely load-bearing:** the checker flags suspected-identifiable items in session, they
  are discarded and **fresh draws substituted**, so the realised set depends on content-derived
  judgements. **Giving it up costs what HC-1H says it costs** — identity exposure becomes
  non-item-discardable and *"returns hard INCONCLUSIVE for the affected batch."*
- **Stopping rules — none selects a next object**, though the §2b pilot gates continuation on a
  χ-derived ε̂ and two preregistered halts already depend on χ-derived aggregates.
- **Not established, and not assertable by reading files:** whether exercising the flag actually carries
  χ. That needs the person who designed the procedure.
- **Found while checking, unresolved:** Row F is described as χ-free while the HC strata it allocates
  over are defined by |χ| tertile. If that stands, the allocated universe is χ-conditioned upstream of
  any question about sequence.

**What is not in doubt:** the condition my proposal depends on is **not satisfied by the current
draft**, and both seats reached that independently against different rows.

## Scope

**Nothing here is evidence about the sky.** No χ has been read; this is a property of the conduct
table. **v9 stays frozen at `6a9abbbd`. BS-6 and the first image byte remain blocked.**

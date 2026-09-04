# DRAFT — NOT ORDERED — R3-A pre-registration: is entry 59's particle-production coefficient β derived, or tuned?

**Tori, 2026-09-04 19:51 KST.** Round-3 topic #1, ranked first in `TOPIC_ROUND3_RANKED_PACKET_20260904.md`. Proposed
independently by two blind seats (codex, agy). **Drafted so that an order starts from a refereed text**, as K3s2, K4,
K5 and K6 were. **No derivation has been run.**

## 0. Why this would exist

Entry 59 (Desai & Popławski 2016, *Phys. Lett. B* 755, 183) reconstructs an inflaton potential from ECKS gravity with
particle production. Its production law is printed at **L126**:

> `K = β(κ ε̃)²`  (5)

and **L128** states: "where β is a dimensionless particle production coefficient."

The spin-corrected energy density it uses is `ε̃ = ε − α n_f²` (**L87**), the same object K3 audited — but **K3 never
touched β.** The paper then feeds this through an Ellis–Madsen scalar-field reconstruction (L307–325) and standard
slow-roll formulas (L325–370) to reach observable perturbation quantities.

**The question is whether β is fixed by the theory or fitted.** If fitted, the corpus's inflationary-observable claims
inherit a tuned parameter, and the shape/magnitude pattern gains a fourth instance in a sector no K study reached.

## 1. The question, exactly

Is the dimensionless coefficient `β` in `K = β(κ ε̃)²` **(a)** derived from the ECKS field equations and the spin
content, **(b)** imported from a cited calculation elsewhere, or **(c)** free — chosen to fit an observable? And do the
paper's reported perturbation amplitude and tilt depend on it?

## 2. Objects to bind before any arithmetic

From entry 59, or marked ABSENT: the definition and dimensions of `K`; the equation it enters; `β`'s stated status at
L128 and any equation that determines it; the chain from `β` to the reported observables (L307–325, L325–370); and
which reported quantity, if any, is independent of `β`.

**Anything imported from the cited references [32] etc. must be marked "cited", not "derived", unless the seat opens
that reference and confirms a derivation.** Where a cited source is unobtainable, the link is marked BLOCKED and the
chain stops there.

## 3. Outcome classes — declared now

1. **BETA_DERIVED** — `β` follows from the ECKS field equations and the spin content. Report the derivation.
2. **BETA_CITED** — `β` is imported from a named calculation, which the seat opened and confirmed. Report the source
   and whether that calculation is itself in the corpus.
3. **BETA_FITTED** — `β` is chosen to reproduce an observable. Report which observable and how tightly it is pinned.
4. **BETA_FREE** — `β` is neither derived, cited nor fitted; it is carried as a free parameter. Report what the
   reported observables then mean.
5. **BETA_UNDETERMINED** — the text does not permit a decision among 1–4. **INCONCLUSIVE**; state exactly what is
   missing.
6. **R3A_NO_CLASS** — a control fails in both seats after two attempts.

Classes 3 and 4 are distinct and must not be merged: a fitted coefficient is a calibration, a free one is a gap.

## 4. Controls, each with an exact named code

- **C1 — source identity.** Reproduce `K = β(κ ε̃)²` and the L128 sentence from the pinned version of record. Exact
  assertion: `C1_SOURCE_IDENTITY=PASS`.
- **C2 — dependence probe.** Vary `β` symbolically and show which reported observables move and which do not. If none
  moves, the paper's observables are independent of it and classes 3/4 lose their force — that outcome must be
  reachable. Exact assertion: `C2_DEPENDENCE_MAPPED=PASS`.
- **C3 — citation opening.** For every link marked "cited", the seat either opens the cited source and prints the exact
  text and line numbers containing the derivation, or marks it BLOCKED. **A citation may not be counted as a derivation unopened.** Exact assertion:
  `C3_CITATIONS_OPENED_OR_BLOCKED=PASS`.
- **C4 — no-fit control.** Recompute the reported observables with `β` replaced by a free symbol; if the reported
  numbers cannot be recovered without choosing a value, that is evidence for class 3 or 4 and must be printed. Exact
  assertion: `C4_FREE_SYMBOL_PROBE=PASS`.

Controls in a limb not reached are recorded `NOT RUN`, never as passes.

## 5. Seats and discipline

Blind double (codex and the Claude seat); a third seat through `nm_referee_dispatch.sh` on any split; an independent
second route by a different method; Kimi on arithmetic with a no-fallback control; a one-page check sheet; Tori re-runs
every script; a "what a critic gets" note after the result. Executable discipline as
`K4_BOUNDARY_TRANSFER_PREREG_20260904.md` §7 — five instances of that defect have been caught in this lane.

## 6. Non-circularity and scope

The observables are the object under test, never an input to the determination of `β`. This document moves no tier,
warrant token, standing or stamp. It does not re-run K3, which audited the spin-density closure in the same chain and
not the production rate. Paper HOLD.

## 7. Cost

One to two seat-days. All sources in the lane; nothing blocked.

R3A_PREREG_DRAFT_READY_FOR_GATE — NOT ORDERED

# DRAFT — NOT ORDERED — R3-H pre-registration: does any downstream published conclusion depend on entry 10's ⅛-versus-¾ spin closure?

**Status:** DRAFT, written under Duho's 2026-09-05 18:56 KST grant ("take the unstarted round-3 preregs — drafting is not
starting"). Round-3 ranked packet cluster **#8** (claude proposal; CONT 3, TRACT 5, score 15, 2–3 seat-days; **provenance limb
blocked**, propagation limb not blocked). Nothing runs on this document. No tier, warrant token, standing or stamp moves.
Paper HOLD. Nothing outward. Published peer-reviewed sources only. Nothing from Hwao's lane, pipeline or data.

**Version:** DRAFT 1. A freeze produces `R3H_ENTRY10_COEFFICIENT_PROPAGATION_PREREG_2026MMDD.md` with §8 filled, C0 by two
seats and a two-seat design gate before any derivation.

## 1. Question

K3 step 1 (`K3S1_RESULT_20260903.md`, three seats) established that entry 10 prints two values of one quantity — the
unpolarised spin-squared closure — six times apart: `⟨s²⟩ = ¾ n²` (entry 10 L113) and `s² = ⅛(ℏcn)²` (entry 10 L121; entries
9, 11). K3 steps 2–3 settled the physics (the n² form is a convention; the four-fermion term is a 2/3 correction at the bounce).
Duho's 2026-09-03 19:34 ruling annotated rows 9, 10, 11 and noted the inheritance: **rows 39, 52 and 59 carry the ⅛ prescription;
row 53 carries the ¾ prescription** (`BHU_CORPUS_SYNTHESIS_20260902.md` lines 218–226). What is untouched is **propagation**:

> **For each inheriting entry, does any printed conclusion — a number, a sign, an inequality, a stated class of behaviour — change
> when the inherited coefficient is replaced by the other printed value (a factor 6 in `s²`, hence in the torsion term `α n²`)?**

Plainly: one paper used two different numbers for the same thing. Four later papers each picked one. Would any of their
answers come out differently with the other number?

**The provenance limb** (where the ⅛ originally came from: Nurgaliev & Ponomariev 1983) is **BLOCKED** from the start — the
source is closed after exhaustive legitimate-open retries (ranked packet, "Blocked-source status"). It is filed
`PROVENANCE_BLOCKED` on day one and not attempted; nothing below depends on it.

## 2. Sources and pins

The four inheriting entries (39, 52, 53, 59) and entry 10, from the corpus ledger's entry→source map, pinned by sha256 at freeze
from `../bhu-reading-20260823/sources/`. Entry 10's pinned text: `1403.0007_clean.txt`,
`765f6280e9348517f7269459f39cc95717406fa11b0a9bb644dfdd94451bb7bc` (R3C2 manifest row 10). The four downstream pins are filled at
freeze; a draft does not pin what it has not re-verified.

Inputs the seat may use: the printed text of the five entries; STANDARD constants. No value the papers do not print. The seat
does **not** re-derive the closure (K3 did); it takes both printed values as given and propagates.

## 3. Procedure (2 seat-days; every symbolic operation through the committed 120 s wrapper)

Per inheriting entry, three steps, each with a machine-matched quotation:

Step 1 — **Locate the inheritance.** Quote the sentence where the coefficient enters (the ⅛ or ¾, or the `α = (9/16)κ(ℏc)²`
constant that carries it), and every downstream printed quantity whose formula contains it (e.g. a critical temperature
`T_cr ∝ α^{-1/2}`, a bounce scale factor, a minimum radius, a maximum density, a stated inequality).

Step 2 — **Propagate.** For each such quantity, recompute the printed number with the coefficient multiplied or divided by 6
as appropriate (the seat records which direction the substitution runs and why). Print old value, new value, the ratio, and
the printed precision of the original.

Step 3 — **Classify the conclusion.** For each printed conclusion resting on the quantity, file one of:
`SIGN_FLIPS` (an inequality or sign reverses), `ORDER_MOVES` (the number moves by a factor ≥ 3 and the paper states a magnitude
claim on it), `WITHIN_PRECISION` (the paper states the number to a precision the change does not exceed, or states no magnitude
claim), `NOT_TRACEABLE` (the printed text does not let the dependence be isolated). One row per (entry, quantity, conclusion).

Two seats, independent; disputes on a row carried as a pair, never reconciled by discussion.

## 4. Outcome classes (precedence top to bottom; exactly one is filed for the study)

1. `R3H_NO_CLASS` — a pre-audit control fails in every seat, or the packet fails redaction.
2. `PROPAGATION_DISPUTED` — the two seats' classifications disagree on any `SIGN_FLIPS` row after the one permitted
   reconciliation attempt; report both.
3. `CONCLUSION_SENSITIVE` — at least one row is `SIGN_FLIPS` or `ORDER_MOVES` in both seats; name the entry, quantity and
   conclusion, with the two values.
4. `CONCLUSION_ROBUST` — every traceable row is `WITHIN_PRECISION` in both seats and at least three of the four entries have
   at least one traceable row.
5. `PROPAGATION_UNTRACEABLE` — fewer than three entries yield a traceable row.

The factor-3 threshold for `ORDER_MOVES` is fixed now, before any number is computed. `PROVENANCE_BLOCKED` is filed alongside
whichever class results and does not enter the precedence.

**Stated before ordering:** the K3 chain suggests the bounce's *existence* depends on the sign of the torsion term, not its
coefficient, so `CONCLUSION_ROBUST` on existence claims with `ORDER_MOVES` on scale claims (`T_cr`, minimum radius) is the
likely shape. That would still be a real record: it says which downstream *numbers* in the corpus are six-fold soft.

## 5. Controls

- **C1 SOURCE_IDENTITY** — byte-exact anchors for entry 10 L113 and L121 and each inheritance sentence.
- **C2 POSITIVE** — entry 10's own printed `T_cr` recomputed from its printed formula and constants to printed precision before
  any substitution.
- **C3 DELETION_PROBE** — delete the inheritance sentence for one entry and require the pipeline to file `NOT_TRACEABLE` for that
  entry with the exact code set `{R3H_C3_NO_INHERITANCE_ANCHOR}` rather than proceeding on a remembered coefficient.
- **C4 HARNESS** — live `sympy` version print through the wrapper.
- **Negative control** — a planted factor of 1 (no change) must file `WITHIN_PRECISION` on every row.

## 6. Seats

Blind double, two engines, packet only, ACCESS_SHA verified by the lane after exit, nothing read before exit, no edit under a
running seat. Lane's own second route for one entry sealed before dispatch.

## 7. Closed-check against prior studies

K3 steps 1–3 settled what the closure is and whether the bounce calculation is controlled; neither is re-run. K1 (stopped) and
K4 were about perturbations across the bounce, not coefficient propagation. No tier or annotation moves from this draft.

## 8. Versions

| version | date (KST) | change |
|---|---|---|
| DRAFT 1 | 2026-09-05 (this file) | written; not ordered, not frozen, not gated; provenance limb pre-filed BLOCKED |

R3H_PREREG_DRAFT_COMPLETE

# K6 — FROZEN PRE-REGISTRATION: does the ECKS density ceiling derive a minimum-black-hole-mass floor? (entry 51)

**Tori, 2026-09-04 16:30 KST. Version 1. FROZEN pending the fresh referee gate. ORDERED by Duho ("K3 step 3, K5, K6
in order", relayed by Blanc 2026-09-04 14:56 KST; "go ahead" confirmed — third and last of three, sequential. K3 step
3 filed 15:28, K5 filed 16:28.)**

Predecessor: `K6_ECKS_FLOOR_PREREG_DRAFT_20260903.md`, gated `PREREG_SOUND_WITH_REPAIRS` 2026-09-03 23:31 KST
(`K6_DRAFT_GATE_agy.md`); its one repair — outcome class 3 widened so that two completions giving *different mass
floors* (not merely different classifications) trigger `K6_FLOOR_UNDERDETERMINED` — is applied and carried here.

**No K6 derivation has been run.**

---

## 0. What this is for

Entry 51 states, in the publisher text at **L662–664**:

> "The mass density of a black hole also cannot exceed ρ_Ce, from which its minimum mass in the ECKS theory is
> ∼10¹⁶ kg, corresponding to energy ∼10⁴³ GeV."

**The connecting calculation behind "from which" is absent from both held texts** — the arXiv-derived text and the
publisher version — and the 2013 erratum amends other equations (`VOR_CHECK_51_59_codex.md` §1). The record carries
`W_UNDERIVED`, and Duho's standing wording is **"unreproduced from the stated inputs," not "error."** That wording
governs every output of this study.

K6 asks the missing question without presuming its answer: do the paper's ECKS equations and its nonsingularity result
bind a mass, density measure, horizon radius and interior geometry tightly enough to imply a positive floor — and if
so, which one?

## 1. Freeze and disclosure — EXECUTED, not promised

The draft required prior exploratory artifacts to be hashed and archived **before** any seat is dispatched. **Done, at
2026-09-04 16:30 KST, and recorded here so the seal precedes the work:**

```
b13_floor_routes.py        98054aecbff165784f22ed9bb1897920369febc7896157ccaffe642f6beb991e
AGATE_Q2_VERDICT.md        ac486f3c2b2e57033063dfe4309704da229f6346e1c35fdb13484ae768700483
CGATE_Q2_VERDICT.md        8dee58f32fab00877368ec246111abd8123a240478834016b38b7eb4deb45c33
VOR_CHECK_51_59_codex.md   e0ae2b17048b55ec09b15df687acb1e4eb49f7a11edbba72ef83d6a3997c6170
```

Both derivation seats are **told these artifacts exist** and are **instructed not to read their values or methods**
until each has sealed its own symbolic chain, assumption ledger and predicted class.

**What that seal is and is not, stated plainly because the gate was right to press on it.** Printing these hashes
proves the artifacts existed unchanged before any seat was dispatched. It is **tamper evidence, not a barrier**: it
cannot stop a seat with filesystem access from opening them. Calling it blinding would be exactly the kind of
promise-instead-of-mechanism this lane has been caught writing twice today.

**The enforceable check is therefore a post-hoc audit, and it will be performed and reported, not assumed.** After
each seat finishes, Tori greps that seat's full execution log for reads of `b13_floor_routes.py`,
`AGATE_Q2_VERDICT.md` and `CGATE_Q2_VERDICT.md`, and **records the result in the K6 result file whether it is clean
or not**. A seat found to have read them has its blind status withdrawn in the record; its derivation is not
discarded, but it no longer counts as independent, and the reconciliation says so.

Neither seat can be blind to the record's `W_UNDERIVED` status, and this document does not pretend otherwise.

## 2. Limb structure — cheap first, per Duho's standing order

**Limb A (cheap, hours, no derivation).** Source identity and absence:
1. reproduce from the held publisher text the Cartan-density ceiling and the `∼10¹⁶ kg` sentence (**L662–664**);
2. verify the pinned erratum amends neither;
3. verify by exhaustive search that **no connecting derivation** from the density ceiling to a mass floor appears in
   either held text.

Limb A can **redirect or void** the study: if the connecting calculation is in fact present, the premise of K6 is
wrong and the study files `K6_PREMISE_VOID` (§5 class 0) without proceeding. If the erratum amends the ceiling or the
mass sentence, the study stops and returns to preregistration.

**Limb B (the study, ~3 seat-days).** Routes A and B of §4, blind.

## 3. Objects to bind before any arithmetic

Each seat must pin from the source or **mark absent**: the ECKS field equations and Dirac spin-density conservation
result entry 51 uses; the Cartan-radius relation of its Eq. (33) including every suppressed dimensionless coefficient
and its order-of-magnitude status; **which density** the ceiling refers to (local rest-frame, proper-volume mean,
coordinate-volume, or another invariant); **which mass** (ADM, Misner–Sharp, Komar, or another source-defined mass);
**which surface** binds size to mass (event, apparent, trapping horizon, or another); and the interior profile, charge
and angular-momentum domain, and matching conditions needed to connect ceiling to mass.

**No GR exterior, Euclidean volume, uniform-density interior, Kerr/Kerr–Newman limit or order-unity coefficient may
enter silently.** Any such item is an *added completion*, must be named as one, and must be tested separately from what
the paper derives.

## 4. The question, and the two routes

**The question.** From the publisher version, its erratum and the peer-reviewed equations it explicitly imports, does
there exist a source-bound theorem `ρ ≤ ρ_Ce ⇒ M ≥ M_min > 0` for every black hole in the paper's stated ECKS domain?
If yes, is the unique derived `M_min` inside the pre-declared match interval `10¹⁵ ≤ M_min ≤ 10¹⁷ kg`? If the
implication is not source-bound, identify **exactly** which free definition, coefficient, geometry or matching
condition prevents it.

The one-decade interval operationalises the paper's order-of-magnitude `∼10¹⁶ kg`. **It is an audit criterion, not an
uncertainty the paper claims.**

**Route A — theorem/inequality.** From the pinned action, field equations and conservation identities, derive every
inequality between the density scalar, a quasilocal or asymptotic mass, and a trapped surface. List each premise.
Prove the universal lower bound, prove no positive universal bound follows, or stop at the first unbound quantity.
**Constants are inserted only after the symbolic result is sealed.**

**Route B — admissible completions / countermodel.** Independently characterise the paper's allowed stationary or
collapsing configurations. Either construct **two source-admissible completions** obeying the same ceiling but yielding
**different mass floors** — which establishes underdetermination — or prove the ECKS equations and matching conditions
remove that freedom. A Schwarzschild mean-density estimate may be run **as a control**, and is not the ECKS result
unless the source-bound derivation licenses that interior and density definition.

**The two routes use separate scripts and separate assumption ledgers. Two numerical substitutions into the same
unstated density–volume formula are one method, not two.**

## 5. Outcome classes — closed decision order, applied in order

0. **K6_PREMISE_VOID** — limb A finds the connecting derivation present in a held text. The study's premise is wrong;
   report where it is and file nothing else.
1. **K6_SOURCE_INCONSISTENT** — the source-bound premises needed for the implication have no common solution. State
   the minimal inconsistent set; no mass floor reported.
2. **K6_NO_POSITIVE_FLOOR** — a proof or explicit one-parameter family shows masses approach zero while all
   source-bound premises and the ceiling hold.
3. **K6_FLOOR_UNDERDETERMINED** — the source leaves at least one load-bearing definition, coefficient, interior
   geometry or matching condition free, and two admissible completions yield **different mass floors** (or the
   stopping rule of §10 is invoked). Report the freedom; **do not choose a preferred completion.**
4. **K6_PRINTED_ORDER_DERIVED** — the source-bound chain yields a unique positive floor in `10¹⁵–10¹⁷ kg` without an
   added completion. Report the formula and value.
5. **K6_ALTERNATIVE_FLOOR_DERIVED** — a unique positive floor outside that interval. Report the formula, value and
   logarithmic separation from `10¹⁶ kg`.

**No class changes a tier, standing or warrant token without a separate Duho ruling.**

## 6. What counts as a verdict

A symbolic implication proof, a no-floor proof, an inconsistency proof, or two explicit admissible completions; an
assumption ledger marking every premise **source-derived / cited / newly added**; a reproducible numerical script only
after the symbolic chain is fixed; controls C1–C6 passing in both seats; a one-page check sheet; and an independent
second-route reconciliation.

**Re-running `b13_floor_routes.py`, reproducing one Schwarzschild estimate, or observing that the paper omits a
displayed equation does NOT count as a K6 verdict.**

## 7. Controls, each with an exact named code

- **C1 — source identity.** Reproduce the ceiling and the `∼10¹⁶ kg` sentence from the held publisher text and verify
  the erratum amends neither. Exact assertion: `C1_SOURCE_IDENTITY=PASS`.
- **C2 — Eq. (33) scaling.** Derive `r_C ∝ m^(−1/3)` and `ρ_C ∝ m²` from the paper's order-of-magnitude relation; with
  a unit coefficient, reproduce the electron Cartan radius within 0.5 decade of `10⁻²⁷ m`. **The unit coefficient stays
  labelled a control normalisation, never a source result.** Exact assertion: `C2_EQ33_SCALING=PASS`.
- **C3 — GR benchmark.** Independently derive and numerically reproduce `ρ̄ = 3c⁶/(32πG³M²)`. **Validates algebra only;
  supplies no ECKS interior premise.** Exact assertion: `C3_GR_BENCHMARK=PASS`.
- **C4 — density semantics.** Show every density used is a scalar or a specified hypersurface average with a
  proper-volume measure; substituting a coordinate volume must be caught. Exact assertion: `C4_DENSITY_SEMANTICS=PASS`.
- **C5 — deletion probe.** Delete the **source-pinned field equations** from any proposed unique-floor proof. The
  proof must lose uniqueness. If the proof still yields a unique floor using only an injected
  size/mass/interior relation, that relation is circular; **no derived-floor class may be filed.** Exact
  assertion: `C5_DELETION_PROBE=PASS`.
- **C6 — completion split.** If an added completion is used, changing at least one allowed completion must either leave
  the theorem invariant by proof or expose the result as completion-dependent. Failure = `K6_FLOOR_UNDERDETERMINED`,
  **not a preferred-number verdict.** Exact assertion: `C6_COMPLETION_SPLIT=PASS`.

**Controls belonging to a limb not reached are recorded `NOT RUN`, never as passes.** The check sheet names the exact
set `{C1_SOURCE_IDENTITY, C2_EQ33_SCALING, C3_GR_BENCHMARK, C4_DENSITY_SEMANTICS, C5_DELETION_PROBE,
C6_COMPLETION_SPLIT}` and states each one's status.

## 8. Executable discipline

`K4_BOUNDARY_TRANSFER_PREREG_20260904.md` §7, adopted unchanged: every cited script exists, runs under `python3`, is
re-executed by Tori and not only by its author, has its output preserved and hashed, and no sentence calls a script
executable support unless all of that holds. **Five instances of this defect have now been caught in this lane.**

## 9. Seats

Route A and Route B on **two blind seats** (codex and the Claude seat), each barred from the sealed artifacts of §1 and
from each other. A split goes to a fresh referee **only** through `nm_referee_dispatch.sh` with ACCESS PROVEN. Kimi via
the Moonshot route on the check-sheet arithmetic with a no-fallback control. A one-page check sheet; Tori re-runs every
script; a "what a critic gets" note after the result and before any ruling.

## 10. Stopping rule

Stop after two failed attempts to bind the same missing source premise and **file `K6_FLOOR_UNDERDETERMINED` rather
than importing an unstated model.** If the publisher text or erratum cannot be read, wait; do not substitute metadata
or an abstract.

## 11. Non-circularity and scope

The printed `10¹⁶ kg` fixes **only** the pre-declared match interval; it may not select a geometry, coefficient,
density definition or matching condition. The sealed exploratory values open only after both chains are sealed. The
paper's Papapetrou/nonsingularity result and its mass-floor corollary remain **separate claims**.

K6 is housekeeping on entry 51's warrant. It moves no tier, token, standing or stamp on Tori's authority. **NOT ordered
and untouched:** the downstream bounce study from K3 step 2, and the K4 follow-up under a declared assumption. Row 23
of the K4 annotation stays as applied. Paper HOLD; nothing outward.

## 12. Cost

Limb A hours; limb B about three seat-days, pure theory, no observational data.

---

## 13. Gate record (V1 → V2)

`K6_PREREG_GATE_20260904_agy.md` (fresh seat via `nm_referee_dispatch.sh`, ACCESS PROVEN) returned
`GATE=PREREG_SOUND_WITH_REPAIRS` with two repairs, **both applied verbatim**, plus one criticism this document has
acted on:

1. **A stopped run fell into no class.** §10 tells a seat to file `K6_FLOOR_UNDERDETERMINED` after two failed attempts
   to bind a missing premise — but that seat will not have built the two admissible completions class 3 required.
   Class 3 now names the stopping rule as a second route into it.
2. **C5 tested the wrong thing.** Deleting the *load-bearing relation* would make a circularly-injected relation
   PASS, since the proof loses uniqueness exactly as the control wanted. C5 now deletes the **source-pinned field
   equations**: if a unique floor survives on an injected relation alone, that relation is circular.
3. **The seal was tamper evidence, not blinding.** The gate said the blinding is "merely asserted" — printing a hash
   stops nobody with filesystem access. §1 now says so plainly and replaces the claim with a **post-hoc log audit
   that will be performed and reported whether clean or not**, with a stated consequence if a seat is found to have
   read the sealed artifacts.

The gate also verified the numeral tracing (recomputing one of the four hashes itself), found the classes exhaustive
once repair 1 is applied, confirmed the `10¹⁶ kg` cannot leak in as a selector, and confirmed the document holds the
record's "unreproduced from the stated inputs, not error" line throughout with no slip.

On worth: "Definitively resolving whether the foundational paper actually derives its central mass floor or merely
asserts it is necessary before committing further resources to downstream studies."

K6_PREREG_V2_FROZEN

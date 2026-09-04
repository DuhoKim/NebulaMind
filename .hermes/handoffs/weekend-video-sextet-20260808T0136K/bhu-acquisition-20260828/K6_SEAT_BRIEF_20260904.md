# K6 — blind seat brief (two independent routes)

**Authority:** Duho, "K3 step 3, K5, K6 in order", relayed 2026-09-04 14:56 KST; "go ahead" confirmed.
**Governing document:** `K6_ECKS_FLOOR_PREREG_20260904.md` (frozen V2) — read it in full first; it binds you.

**BLIND — TWO WAYS.**
1. Do NOT open, list, grep or infer any file whose name contains `K6_routeA`, `K6_routeB`, `K6_ROUTE`, `K6_RESULT`,
   `K6_CHECK` or `K6_RECONCIL`.
2. **Do NOT open `b13_floor_routes.py`, `AGATE_Q2_VERDICT.md` or `CGATE_Q2_VERDICT.md`.** These are sealed prior
   exploratory artifacts. You are told they exist; you may not read their values or methods. **Tori will audit your
   execution log for reads of those paths and record the result publicly whether clean or not.** If you open one by
   accident, say so at the top of your report — that is far better than being found by the audit.

You MAY read the prereg, `VOR_CHECK_51_59_codex.md`, and the source
`../bhu-reading-20260823/sources/poplawski_plb690_vor_clean.txt` ("entry 51").

## The question (prereg §4)

Entry 51 states at **L662–664**: "The mass density of a black hole also cannot exceed ρ_Ce, from which its minimum mass
in the ECKS theory is ∼10¹⁶ kg". **The calculation behind "from which" is absent from the held texts.**

**Does there exist a source-bound theorem `ρ ≤ ρ_Ce ⇒ M ≥ M_min > 0` for every black hole in the paper's stated ECKS
domain?** If yes, is the unique derived `M_min` inside `10¹⁵–10¹⁷ kg`? If the implication is not source-bound,
identify **exactly** which free definition, coefficient, geometry or matching condition prevents it.

The record's standing wording is **"unreproduced from the stated inputs," not "error."** Hold that line in every
sentence you write.

## Do limb A first (prereg §2), and report it before anything else

1. Reproduce from the held publisher text the Cartan-density ceiling and the `∼10¹⁶ kg` sentence.
2. Verify the pinned erratum amends neither.
3. **Search exhaustively for a connecting derivation** from the ceiling to a mass floor. If you find one, stop and file
   `K6_PREMISE_VOID` with its location — that would void the study and is a legitimate, valuable outcome.

## Then your assigned route

**Your route is named in the dispatch message.** Do only that one.

- **Route A — theorem/inequality.** From the pinned action, field equations and conservation identities, derive every
  inequality between the density scalar, a quasilocal or asymptotic mass, and a trapped surface. List every premise.
  Prove the universal lower bound, prove no positive universal bound follows, or stop at the first unbound quantity.
  **Insert constants only after the symbolic result is sealed.**
- **Route B — admissible completions / countermodel.** Characterise the paper's allowed stationary or collapsing
  configurations. Either construct **two source-admissible completions** obeying the same ceiling but yielding
  **different mass floors**, or prove the equations and matching conditions remove that freedom. A Schwarzschild
  mean-density estimate is a **control**, not the ECKS result.

## Bind these before any arithmetic (prereg §3), or mark each ABSENT

The ECKS field equations and spin-density conservation result used; Eq. (33)'s Cartan-radius relation with every
suppressed coefficient; **which density** the ceiling means; **which mass**; **which surface** binds size to mass; the
interior profile, charge and angular-momentum domain, and matching conditions.

**No GR exterior, Euclidean volume, uniform-density interior, Kerr limit or order-unity coefficient may enter
silently.** Any such item is an ADDED COMPLETION: name it as one and test it separately.

## Assumption ledger — required

Every premise marked **source-derived**, **cited**, or **newly added**. A proof whose ledger is missing does not count.

## Controls — print each by name

`C1_SOURCE_IDENTITY`, `C2_EQ33_SCALING`, `C3_GR_BENCHMARK`, `C4_DENSITY_SEMANTICS`, `C5_DELETION_PROBE`,
`C6_COMPLETION_SPLIT`, each `=PASS`, `=FAIL` or `=NOT_RUN`. **NOT_RUN is honest; a false PASS is not.**
Note C5's exact form: delete the **source-pinned field equations** from any unique-floor proof; if a unique floor
survives on an injected size/mass relation alone, that relation is circular and no derived-floor class may be filed.

## Deliverables — exactly two files, nothing else changed

1. `K6_<route>_<seat>.py` — self-contained, runs under `python3`, prints every claim. **Run it.**
2. `K6_<ROUTE>_<seat>_RESULT.md` — first line exactly one class token from prereg §5:
   `K6_PREMISE_VOID` · `K6_SOURCE_INCONSISTENT` · `K6_NO_POSITIVE_FLOOR` · `K6_FLOOR_UNDERDETERMINED` ·
   `K6_PRINTED_ORDER_DERIVED` · `K6_ALTERNATIVE_FLOOR_DERIVED`

## Rules

- **Do not import an unstated model to get a number.** If you must stop, stop and say what could not be bound.
- Every numeral traces to a source line you cite or to something your script printed.
- You have no authority over any tier, warrant token, standing or stamp.

K6_SEAT_BRIEF_COMPLETE

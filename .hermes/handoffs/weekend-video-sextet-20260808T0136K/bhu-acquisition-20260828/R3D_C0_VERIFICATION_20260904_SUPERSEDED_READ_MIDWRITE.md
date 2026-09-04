> # ⚠️ SUPERSEDED AND WRONG — PRESERVED, NOT DELETED
> **This note verified an artefact that was still being written.** codex had not finished; the completion loop
> never fired and I tailed the dispatch log's START line instead of its `ACCESS PROVEN` line. The partial file read
> `C0_REACHABILITY=PASS` with "Unreachable verdicts: None". **The finished exhibition reads
> `C0_REACHABILITY=FAIL` with two unreachable conditions.** Everything below about the verdict is therefore false.
> The arithmetic checks in it were correct and are carried into the replacement; the verdict was not.
> Replacement: `R3D_C0_VERIFICATION_20260905.md`. Archived under this lane's rule: archive, never delete.

# Tori's VERIFICATION of the C0 exhibition — and one finding C0 could not flag itself

**Tori, 2026-09-05 00:00 KST** (the work and every artefact it verifies are dated 2026-09-04; this note crossed midnight)**.** C0 requires the exhibitions to be **authored by a seat and only verified by me**.
This is the verification. **I did not author any exhibition.**
**No tier, warrant token, standing or stamp moves. Paper HOLD. R3D is NOT run.**

## What was exhibited

`R3D_C0_EXHIBITION_codex_20260904.md`, codex, access proof `b7883c25…111387d2` **verified by me against the file
after the run**. Verdict **`C0_REACHABILITY=PASS`**: **20 verdicts exhibited, 0 unreachable** — all seven §4
classes, both directions of all five C6 breaker conditions, and all three `C6_BREAKER_TEST` outcomes.

## What I checked, rather than accepted

**Arithmetic, recomputed independently from the document's own intervals:**

| exhibited | codex's claim | my recomputation |
|---|---|---|
| condition 5 PASS, floor `1.000e15 kg` | overlaps nothing | **confirmed** — sits between the Hawking and TOV intervals |
| condition 5 FAIL, floor `2.000e11 kg` | overlaps Hawking | **confirmed** — inside `[1.729e11, 5.190e11]` |
| condition 1 FAIL, ratio `M_min/m_P` | `4.594e22` | **confirmed** — `4.5947e22`, agrees at printed precision |
| boundary case `5.190e11` | *(not exhibited)* | overlaps Hawking — the closed interval behaves as written |

**Internal consistency:** the two occurrences of "UNREACHABLE" are a section heading and an analysis line, not
verdicts; the reachable column reads `yes` in all 20 rows. **The `PASS` is consistent with its own table.**

**Routing, spot-checked on the two least obvious rows:** §4.7 (`R3D_NO_CLASS`) correctly rules out
`DYM_SOURCE_BLOCKED` first, then defeats the one-clean-seat exception via the third-seat re-run — that is the clause
chain as written. §4.6 routes through C1's unreadable-source rule correctly.

## THE FINDING — and C0 could not flag it, which is the point

**codex's §4.5 exhibition depends on an undefined term resolving one particular way.**

Its construction: printed relations allow exactly `M_n = (10 + 1/n) kg`, which has a **positive lower bound of 10
that is never attained**. It routes this to `DYM_FLOOR_COMPLETION_DEPENDENT` by reading **"floor" as "attained
minimum"**.

**But the document never defines "floor".** Class 4 defines its own key term — *"**permit** means no positive lower
bound on the mass follows"* — while class 5 opens *"**no positive floor follows** from the printed relations
alone"*, and no clause says whether a floor is a lower bound or an attained minimum.

- **If floor is an attained minimum** (codex's reading): the construction is class 5. Reachable.
- **If floor is a lower bound**: a positive lower bound of 10 *does* follow, so class 5's precondition fails — and
  class 4 is already excluded because its "permit" test is not met. **The construction lands in no class at all.**

**Two obedient seats can therefore file differently, or nowhere, on the same physics** — the same defect family that
has recurred through this study.

**Why this matters for C0 as a control.** C0 asked "can each verdict be reached?", and a seat that resolves an
ambiguity favourably produces a path, so **the answer comes back `PASS` and the ambiguity stays invisible to the
control.** C0 catches an outcome blocked by construction; **it does not catch an outcome reachable only under one
reading of an undefined term.** That is a real limit of the control I recommended, found on its first run, and it
belongs in the doctrine.

## What I have NOT done

**I have not repaired it.** The order was to run the exhibitions and gate V9; defining "floor" is a repair, and
**kimi is reading V9's bytes right now** — editing under a running seat is the discipline failure this lane already
paid for once. The fix is one sentence when it is authorized: state whether a floor is an attained minimum or a
lower bound, and make classes 4 and 5 use the same term.

**I did not author, alter, or complete any exhibition.** Where codex did not exhibit a case (the boundary value), I
computed it as a check and have marked it as mine, not as part of the exhibition.

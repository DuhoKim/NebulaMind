# Tori's VERIFICATION of the first C0 exhibition — `C0_REACHABILITY=FAIL`

**Tori, 2026-09-05 00:02 KST.** C0 requires exhibitions to be **authored by a seat and only verified by me.**
**I did not author any exhibition.** **No tier, token, standing or stamp moves. Paper HOLD. R3D is NOT run.**

## First, my own error, because it changes what can be trusted here

**My earlier verification note was wrong: I read the exhibition while codex was still writing it.** The completion
loop never fired, and I tailed the dispatch log's opening line rather than its `ACCESS PROVEN` line. The partial
file read `C0_REACHABILITY=PASS` with "Unreachable verdicts: None". **The finished file reads
`C0_REACHABILITY=FAIL`.** Blanc's report to Duho was correct and mine was not. The bad note is preserved, marked,
in `R3D_C0_VERIFICATION_20260904_SUPERSEDED_READ_MIDWRITE.md`.

**The lane rule this broke is its own:** monitor process state, not the artefact. A file that exists is not a file
that is finished. **Verification now requires the dispatcher's `ACCESS PROVEN` line AND a zero process count before
the artefact is read** — not the presence of bytes.

## The exhibition, verified

`R3D_C0_EXHIBITION_codex_20260904.md`, codex. **`ACCESS PROVEN` in the dispatch log, and I re-verified
`ACCESS_SHA=b7883c25…111387d2` against V9 on disk after the run.** Verdict **`C0_REACHABILITY=FAIL`** —
**18 verdicts reachable, 2 UNREACHABLE.**

## The two unreachable verdicts, and they share one mechanism

**Both are C6 breaker-condition FAILURES, and both are blocked by the same pair of clauses:**

> `DYM_FLOOR_DERIVED` — a unique positive floor follows from the printed relations **with no added completion**…

> **C6 — breaker test.** Applies **only if `DYM_FLOOR_DERIVED` is reached**; otherwise `NOT_RUN`, never a pass.

- **Condition 1 FAIL is unreachable.** A dimensionless result — a ratio, a shape — is what condition 1 exists to
  reject. But §4.1 requires a positive *mass*, and C6 runs only after §4.1. **A candidate that would fail condition
  1 can never reach condition 1.**
- **Condition 3 FAIL is unreachable.** A surviving free symbol is what condition 3 exists to reject. But if a free
  symbol survives, the floor is a family rather than a unique value, and pinning it is an added completion — so
  §4.1 is not reached. **A candidate that would fail condition 3 can never reach condition 3.**

**I checked both entailments myself and both hold.** A §4.1 floor is necessarily a mass, and necessarily free of
surviving non-§2b symbols. This is not a drafting slip: **conditions 1 and 3 are logically entailed by the class
that gates them.**

## Direction of this defect — the opposite of the diagnosed pattern

The diagnosis found errors landing on the side that **fails to certify a counterexample**. **This one lands the
other way.** Two of five breaker conditions cannot fail, so the breaker test is **easier** to pass than the record
claims: a counterexample would be certified against a test advertised as five conditions but which is, for this
study, **three**. That overstates the falsifier's stringency in the direction of *declaring* a counterexample.

Worth recording plainly: **this is the second defect found tonight running counter to the diagnosed pattern** — the
first was V6's inward-rounded comparator intervals. The lane's errors are not uniformly self-serving.

## Verified arithmetic, carried over from the superseded note

Recomputed by me from the document's own intervals; all confirmed: floor `1.000e15 kg` overlaps nothing (condition
5 PASS); `2.000e11 kg` falls inside the Hawking interval `[1.729e11, 5.190e11]` (condition 5 FAIL); the boundary
value `5.190e11` overlaps as the closed interval requires; and `1e15/m_P = 4.5947e22` matches codex's printed
`4.594e22`.

## A separate ambiguity I found, which C0 did not flag

**"Floor" is never defined.** Class 4 defines *"**permit** means no positive lower bound on the mass follows"*,
while class 5 opens *"no positive **floor** follows"*. codex's §4.5 exhibition — `M_n = (10 + 1/n) kg`, positive
lower bound 10, never attained — is reachable **only if floor means "attained minimum"**. If floor means "lower
bound", that construction lands in **no class at all**.

**C0 could not catch this**, and that is instructive about the control: a seat that resolves an ambiguity
favourably produces a path, so the reachability answer comes back clean while the ambiguity stays invisible.
**C0 catches an outcome blocked by construction; it does not catch an outcome reachable only under one reading of
an undefined term.** That limit belongs in the doctrine.

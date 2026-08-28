# REFEREE BRIEF — V34, whole document. A new attack surface, and one disclosure you must read first.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V34_20260828.md`**, sha256 `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948`. **Verify and state the
comparison.** Predecessor V33 (`b247f402…`) — you both cleared its *document*; V34 adds only the
BS-2a pin and one §10 row. **Write to `V34_WHOLE_REVIEW_<YOURSEAT>.md`.**

## DISCLOSURE — read before running any tool

**The citation check in `prereg_lint.py` is QUARANTINED and its output is ADVISORY.** It has failed
three consecutive adversarial rounds from both of you. It is known to emit `FABRICATED` against
**real** citations — `CODEX-V4 F9` exists in `GATE_CODEX_SUCCESSOR_V4.md` and the check judged it
against an unrelated report. Its canary does not detect deletion of its own positive branch.

**Verify any repair-announcement citation YOURSELF against the cited report. Do not treat lint output
about citations as evidence in either direction — a green lint supports nothing here.** Details and
the pending decision are in `../OPEN_QUESTION_CITATION_CHECK.md`.

Every other lint check, `prereg_trace --check`, and the trace refactor were cleared by you both and
may be relied on normally.

## THE NEW ATTACK SURFACE — absence clauses

A sister lane produced a rule that has now caught five defects in my tooling:

> **A narrow pattern is safe for presence, dangerous for absence. Finding a thing proves it is there;
> failing to find it proves nothing.**

**Apply it to the DOCUMENT, not to code.** V34 contains ~71 clauses asserting that something is
*never*, *nowhere*, *cannot*, *must not*, *in no case*, or *none*. Every one is a universal negative,
and a universal negative is exactly the claim that cannot be established by having looked and not
found. For each, ask:

- **What would have to be true for this to hold, and is that established or assumed?**
- **Is it enforced by construction, or only asserted?** "Cannot" enforced by a type or an identity is
  sound; "cannot" meaning "we did not find a way" is the failure shape.
- **Could it be false without anything in the document noticing?** That is the operative test.

No round has aimed at this surface. It is the most likely place for a live defect in a draft that has
otherwise been through many rounds.

## Also in scope

- The **BS-2a pin** is new in V34: the quality-predicate component with its digest, the clearing
  seats, and its **recorded limit** (sound against forgery; **not** hardened against arbitrary
  hostile input; no crash path reachable from the builder; a crash fails closed). **Does the row
  claim more than the gate established?** The slot stays DESIGN, UNFILLED and the class counts do
  not move — verify both.
- §1 scope and §2.7 line 384 must remain byte- and position-identical to V30.
- Whole-document re-read. V33's document was cleared, but clearance is not transitive across a new
  normative row.

## OUT OF SCOPE — parked on the principal, do not re-litigate

1. **VOID registry amendment** — three verified gaps (`degenerate`, `digest`, `chosen`);
   `../OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md`.
2. **Gain-control T completeness** — the p-gated fork;
   `../OPEN_QUESTION_T_COMPLETENESS.md`.
3. **The citation check** — quarantined; `../OPEN_QUESTION_CITATION_CHECK.md`.

Findings in these areas that are *new* are welcome; re-deriving what is already filed is not.

## Standing

BS-2a DESIGN/UNFILLED; one of fifteen class-P slots filled; BS-2v UNRESOLVED; rows C2 and E cannot
run; Stage P `SUPERSEDED`; **BS-6 and the first image byte remain blocked.** Do not read
`/Users/duhokim/NebulaMindData/`.

A CLEAR means *this is a correct preregistration that is honest about being an unfinished
programme* — not that the study may proceed. Final line exactly `**CLEAR**` or `**NOT CLEAR**`.
**Judge independently; do not converge.**

# BRIEF — V42 whole-document referee round

**Subject:** `PREREG_SUCCESSOR_DRAFT_V42_20260829.md`
**sha256 `6c9cc2fca67d5aff263282f646fc5b0c07a22b0c2c3665d458c47582de7990a6`**
Verify this digest before reading. If it does not match, stop and report the mismatch.

Predecessors: V36 `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177` (**CLEAR ×2,
06:57 — the last refereed draft**), V37 `62dd8a7525c399126477573d55a952f1ed2f147d16f8bfbb12aa89a295821c42` (never refereed).

## What changed, and under what authority

V37 and V42 apply **principal decisions relayed 2026-08-29 09:20 and 10:15**. They are not my
choices, except where noted.

1. **§7.1 — three coverage gaps closed** (authorised, option A). `VOID-5-DEGENERATE` added (§5,
   `Post-unblinding`); `VOID-5-DIGEST-DEVIATION` added (§5, `Any`) as a separate antecedent rather
   than an undeclared alias; `VOID-2.7-THRESHOLD-MOVED` renamed to
   `VOID-2.7-THRESHOLD-CHOSEN-OR-MOVED`.
2. **§7 — `BS-3g` added: class P, DESIGN/UNFILLED, blocks BS-6** (authorised, option (a)). **Class
   counts move 15/8 → 16/8** — the first row-count change since V4. §1's "must be bound before BS-6"
   sentence now names this edge. Before V37 that sentence asserted a precondition no dependency
   enforced (GPT56-V34-1).
3. **§7.1 — the §2.7 phase settled from the authorship record, cell unchanged.** The principal
   declined the question as not his: the clause entered at V11, commit `4d99d1d93`, authored by this
   lane. V11's §2.7 preamble says the freedom is exercised *"after image inference exists"*, which is
   the first real χ. **A previous reading of mine proposing `Post-unblinding` was wrong** — it
   confused when χ is read with when χ exists.
4. **§5 — the `require_authorization` limit recorded accurately** (CODEX-V34-2), and deliberately
   **not** repaired: the guard checks only that a caller-supplied file matches a caller-supplied
   digest. Nothing built; `successor_ref_v9.py` remains frozen.

## Since V38 — what V39 and V42 did

V39 repaired the three V38 findings: the DESIGN-slot inventory omitted `BS-3g` (**both seats**);
`DECISIONS_FOR_DUHO.md` was cited as the record of a ruling it does not record (CODEX-V38 F3); and
the χ-ordering evidence cited §6.1/§6.2 when the lines are in §6 and §5, while commit metadata was
offered as proof of lane authorship when every commit carries the principal's git identity
(CODEX-V38 F4).

**V42 implements a principal ruling on CODEX-V38 F2 (option C).** §5's VOID trigger is split by kind:
**forbidden acts and protocol/digest deviation trigger at `Any` phase, unchanged**; the **numerical**
conditions read **post-unblinding**; and pre-unblinding numerical failures route to the new
**`INCONCLUSIVE-BY-COMPUTATION`** with a binding rerun procedure. **No registry row changed** —
`registry_digest` is unmoved at `a4d1d745…`.

## NOTE TO GPT56 — you did not find CODEX-V38 F2

CODEX found the §5 phase-scope hole at V38 and you did not; your V38 report carried one finding, its
report carried four. **This is said plainly so you review the repair rather than spend the round
re-deriving whether the hole existed.** It did, and it is now ruled on. Your job here is whether the
implemented repair is correct and complete.


## THE LINT'S CITATION BEHAVIOUR HAS CHANGED SINCE V40 — read this before running it

The citation check was **quarantined** when V38 and V40 were dispatched: it emitted
`repair-citations-advisory` and, despite what its own comment claimed, **still failed the lint**.
That is no longer true.

The principal ruled option C and then option D. The check now reads `FINDINGS-BLOCK v1` and indexes
reports **by the blocks they declare, never by filename**, which removes the defect that made it call
a real citation fabricated. Compound citations (`KIMI/GPT56-V11 F4`) are expanded and every named
seat is checked — previously only the last seat was seen, which hid a real miscitation. Three
categories, two of which block: `repair-citation-fabricated` and `repair-citation-malformed` fail the
lint; `repair-citation-legacy` is advisory and **does not**.

**On V42 the lint exits 0 with 96 advisory findings and 0 blocking.** Those 96 are pre-format
citations whose reports predate the block format. **Under the principal's option D ruling that is
their permanent answer, not a deferral** — do not report them as unresolved work.

## Attack these specifically — the V42 repair above all

- **Did the edit quietly narrow the misconduct conditions?** The ruling moved the *numerical*
  conditions only. If forbidden-acts or protocol-deviation scope has shifted anywhere in the
  document's prose, that is unauthorised and is the single most important thing to find.
- **Is `INCONCLUSIVE-BY-COMPUTATION` actually a procedure**, or a label wearing one? Can an operator
  follow it without a further decision? The maximum attempt count is **deliberately unbound and
  declared** — say if that declaration is insufficient, but do not treat the omission as concealed.
- **Does the rerun allowance open a forking path?** It forbids rerunning on a finite result, but test
  whether that is enforceable as written.



- **Is the §2.7 instant recovery sound?** I claim the record *determines* it. If V11's words do not
  determine it, or determine a different instant, say so — that is a finding.
- **Does `BS-3g` actually make §1's sentence true**, or does it only appear to?
- **Does the 15/8 → 16/8 move break anything** that assumed the old inventory?
- **The §7.1 preamble claims NAME-coverage only.** Check it does not overclaim elsewhere.

## Carry the absence-clause lens — it has found a real defect every round

**A narrow pattern is safe for presence and dangerous for absence.** Apply it to the *document*: for
each universal negative ("no X can…", "nothing may…", "cannot create"), ask what construct would make
it false and whether the document enforces the exclusion or merely asserts it. That lens produced
every HIGH finding this lane has had.

## Known and out of scope — do not re-derive

- **The citation check in `tools/prereg_lint.py` is QUARANTINED.** Its findings emit as
  `repair-citations-advisory`. **It is unreliable in both directions and calls real citations
  unverifiable.** The principal has ruled it be rebuilt so reports are machine-readable (see below);
  that work is not in this draft. **`prereg_lint.py` therefore exits 1 on V42 with exactly one
  advisory finding — that is expected and is not a document defect.** All other checkers pass:
  counts 16/8 prose-matched, trace 0 problems, `void_registry` 54 antecedents / 20 rows / digest
  `a4d1d745…`, no refusal.
- **The gain control's completeness fork is decided: option (b)**, an executable joint counterfactual
  path. That build has not started and is not in this draft. Do not re-argue the fork.
- **BS-6 and the first image byte are blocked.** Nothing here changes that.
- **BS-2a stays DESIGN, UNFILLED.** A code-gate CLEAR is not a fill authorisation.

## REQUIRED REPORT FORMAT — this is new and it is mandatory

Write to `gates/V42_WHOLE_REVIEW_<SEAT>.md` where `<SEAT>` is `GPT56` or `CODEX`.

Your report **must end** with exactly this block, machine-readable, so a checker can verify citations
to it without guessing your grammar:

    <!-- FINDINGS-BLOCK v1 -->
    SEAT: <GPT56|CODEX>
    VERSION: V42
    VERDICT: <CLEAR|NOT CLEAR>
    COUNT: <n>
    F1 | <HIGH|MEDIUM|LOW> | <REPAIR-REQUIRED|ADVISORY|HELD> | <§ and line> | <one-line summary>
    F2 | ...
    <!-- END FINDINGS-BLOCK -->

Rules: number findings contiguously from 1; `COUNT` equals the number of `F` lines; if you find
nothing, `COUNT: 0` and no `F` lines. A confirmation of a previous repair is `HELD`, **not** a
finding — do not number it. Prose above the block is yours to structure freely.

**A verdict of CLEAR means: the text is a correct preregistration that is honest about being an
unfinished programme.** It does not mean the study may proceed.

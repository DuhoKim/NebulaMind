# OPEN QUESTION — the citation check has failed three adversarial rounds. I have stopped.

**Raised 2026-08-29 05:45 KST by Hwao under self-continuation. Stopping rule invoked: I declared R3
the last round on this object and it returned NOT CLEAR from both seats. I am not attempting a
fourth repair.**

## The check is quarantined, not fixed

Its findings now emit as `repair-citations-advisory` and **do not fail the lint**. That is
harm-reduction, not a repair, and it was necessary because the check had become actively dangerous
in the worst direction:

**It calls a real citation fabricated.** `CODEX-V4 F9` exists in `GATE_CODEX_SUCCESSOR_V4.md`, but
`_reports_for` requires `"REVIEW"` in the filename, so it judged the citation against the unrelated
four-finding `GAIN_V4_REVIEW_CODEX.md` and returned `FABRICATED`. **Acting on that output would mean
"fixing" a correct document** — strictly worse than not checking.

## What three rounds established

| round | verdict | what it found |
|---|---|---|
| R1 | NOT CLEAR ×2 | verified the *envelope* (a report exists), never the contents |
| R2 | NOT CLEAR ×2 | rebuilt version unsound **in both directions at once** |
| R3 | NOT CLEAR ×2 | ternary version still unsound in both directions; canary still cannot detect deletion of its own positive branch |

**Two things I asserted that were false**, both verified against the shipped code this tick:

1. I said all four deletion probes turn the battery red. **Deleting the positive `VERIFIED` branch
   leaves the self-test green (exit 0, "8 controls, 0 failure(s)").** I probed four branches and not
   the one that matters most.
2. The code diverges from `CITATION_CHECK_SPEC.md`, which I wrote *first* this round specifically to
   prevent that: the spec requires mixed-grammar verification; the code rejects every mixed grammar.

## Why I think it keeps failing

Which numbered items in a referee report are *findings* is a judgement its author made and did not
machine-encode. Reports here use at least four declaration grammars, mix them within one file, and
live under at least three filename families. **Every version of this check has tried to recover an
unencoded judgement by pattern-matching, and a pattern used to establish a negative is unsound by
construction** — the rule a sister lane stated and that I have now violated five times.

The ternary outcome was meant to fix that by refusing to decide when parsing is uncertain. Both
seats found it does not: `UNVERIFIABLE` is trivially inducible, so a fabrication can hide behind an
unrecognisable grammar, while a contiguous prefix can still call a real later finding `FABRICATED`.

## The options, and what each costs

**A. Delete the check.** *Cost:* the document's most dangerous sentence — one announcing a repair —
goes unverified again. That is the risk the check was built for, and V12 is the precedent: a
blockquote claimed a unanimous finding repaired while half of it stood.

**B. Keep it advisory permanently**, as now. *Cost:* an advisory nobody must act on is close to no
check, and it carries a standing risk that a future reader treats its output as authoritative.

**C. Make the reports machine-readable instead.** Require every seat report to carry a canonical
findings block (the dispatch brief already dictates report format, so this is enforceable going
forward). Then the check is exact, not heuristic. *Cost:* it cannot verify the ~30 historical
reports, so old citations stay unverifiable; and it adds a constraint to every future round.

**D. Verify citations by hand at freeze time**, once, and drop the tool. *Cost:* human minutes at the
only moment it matters, and no regression protection between now and then.

**My reading, not my decision: C for future rounds, D for the existing corpus.** The check has failed
three times because it is trying to parse an unencoded judgement; the fix is to encode it. But C
changes what every future referee round must produce, which is a workflow decision rather than a
tooling one, and that is why I am not taking it.

## What is NOT in doubt

**V34's correction citations are real.** Both seats confirmed independently in R1 and again in R2:
`CODEX-V11 3` and `GPT56-V11 F3` resolve to actual findings. **No draft defect is implied by any of
this.** The failure is entirely in the tool.

The other harness repairs stand and were cleared: the `prereg_trace` refactor (predicates unchanged,
all four refusal branches identical, three controls invoke `check_trace()`), the orphan scan, and the
`void_registry` renames.

---

## VERIFIED CURRENT AGAINST V36 — 2026-08-29 07:25 KST

Quarantine confirmed live on the current draft: all three emission sites in `tools/prereg_lint.py`
(lines 252, 271, 274) carry category `repair-citations-advisory`, and the lint run on V36 exits **0**
with *"no inconsistencies found (all 6 checks demonstrated they can fail)"* — the citation check is
not among the six that can fail the lint. `--self-test` passes 8 controls.

**The check is still quarantined and still must not be reopened.** This stamp records that state, not
a new attempt at it.

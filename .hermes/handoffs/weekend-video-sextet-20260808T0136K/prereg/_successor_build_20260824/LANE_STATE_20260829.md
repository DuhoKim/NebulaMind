# LANE STATE — DESI successor prereg, 2026-08-29 06:15 KST

**Written because context is at 98%. Assume the reader is a compacted Hwao or a fresh session.
State and paths only; reasoning lives in the commit log and the referenced files.**

Lane root: `.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824`
Repo: `/Users/duhokim/NebulaMind/NebulaMind` — branch `feat/paper-workflow-v2`

## Current draft

| file | sha256 | state |
|---|---|---|
| `PREREG_SUCCESSOR_DRAFT_V35_20260829.md` | `b80d50afe076fe8d20c9fd1a6e6b5db63779dfc02ee46601667a67227e12fbdd` | **NEVER REFEREED** |
| `PREREG_SUCCESSOR_DRAFT_V34_20260828.md` | `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` | NOT CLEAR ×2 (V34 round) |

**V35 = V34 + three fixes**, all from the V34 absence-clause round: §1 line 120 ("cannot create"
narrowed to what the identity enforces), §6.2 line 592 (the false "unlogged read breaks the chain"
claim deleted), §7 line 698 (my BS-2a pin overclaimed the pairwise probe evidence).
**Blanc's 06:15 relay asked for the first two to be carried into V36 — they are already in V35.**

Change inventory vs V34: lines 1, 120, 592, 698, plus one §10 row. §1 scope and §2.7 line 384 remain
byte- and position-identical to V30. Class counts unmoved at 15 class-P / 8 class-E.
All four checkers pass on V35.

## FOUR DECISIONS AWAITING DUHO — the lane is blocked on these, not on dispatch

1. `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` — **three verified gaps**: `degenerate`,
   `digest`, `chosen`. Mechanism cleared by both seats (the BS-2v circularity claim is false);
   content is not. Amending §7.1 is normative.
2. `OPEN_QUESTION_T_COMPLETENESS.md` — the p-gated fork, (a)/(b)/(c). I would drift to (a) because
   it is cheap; that is the reason not to let me take it.
3. `OPEN_QUESTION_CITATION_CHECK.md` — see quarantine below.
4. `OPEN_QUESTION_BS6_DEPENDENCY_AND_AUTHORIZATION.md` — **the two biggest findings of the night**:
   "must be bound before BS-6" has no dependency edge (repair moves counts 15/8 → 16/8), and
   `require_authorization()` accepts arbitrary bytes (CODEX ran frozen v9 against a referee brief
   and the guard passed). Both normative; both Duho's.

## DO NOT REOPEN

**The citation check in `tools/prereg_lint.py` is QUARANTINED to advisory** after three consecutive
two-seat NOT CLEARs. It emits `FABRICATED` against real citations (`CODEX-V4 F9` exists in
`GATE_CODEX_SUCCESSOR_V4.md`). Its findings carry category `repair-citations-advisory` and do not
fail the lint. A fourth repair attempt is explicitly out of bounds — the decision is filed.

## CLEARED — do not redo

- **BS-2a code gate**: CLEAR ×2 at round 6. `ref/bs2a_quality_gate.py` = `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`. Pinned in the
  §7 BS-2a row with its recorded limit. Slot stays DESIGN, UNFILLED.
- **Gain control repairs**: CLEAR ×2 at v6 (scoped). T-completeness still parked (decision 2).
- **`prereg_trace` refactor**: cleared by both seats; predicates unchanged.
- **V34's correction citations are real** — confirmed independently, twice.

## CURRENT DRAFT IS V36 — **CLEAR FROM BOTH SEATS, 06:57 KST**

`PREREG_SUCCESSOR_DRAFT_V36_20260829.md` = `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177`

**First two-seat CLEAR the preregistration document has had.** Both seats verified the digest, the
delta (line 1, line 698, one §10 row), the V30 byte- and position-identical invariants, class counts
15/8, and the BS-2a pin. CODEX ran a fresh whole-document absence-surface attack and **found no new
repair-required defect.** Their two numbered items each are HELD confirmations of the V35 repairs,
not new findings.

**WHAT THIS DOES AND DOES NOT MEAN.** It means the text is a correct preregistration that is honest
about being an unfinished programme. **It does not mean the study may proceed.** BS-2a stays DESIGN,
UNFILLED; one of fifteen class-P slots filled; BS-2v UNRESOLVED; rows C2 and E cannot run; Stage P
SUPERSEDED; **BS-6 and the first image byte remain blocked.** Four decisions below are still open and
two of them (the BS-6 dependency edge, `require_authorization`) are HIGH findings the seats raised
and I parked — a CLEAR on V36 does not retire them, because both were declared out of scope for the
round rather than resolved.

## FOUR DECISIONS AWAITING DUHO — the lane is blocked on these, not on dispatch

1. `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` — **three verified gaps**: `degenerate`,
   `digest`, `chosen`. Mechanism cleared by both seats (the BS-2v circularity claim is false);
   content is not. Amending §7.1 is normative.
2. `OPEN_QUESTION_T_COMPLETENESS.md` — the p-gated fork, (a)/(b)/(c). I would drift to (a) because
   it is cheap; that is the reason not to let me take it.
3. `OPEN_QUESTION_CITATION_CHECK.md` — see quarantine below.
4. `OPEN_QUESTION_BS6_DEPENDENCY_AND_AUTHORIZATION.md` — **the two biggest findings of the night**:
   "must be bound before BS-6" has no dependency edge (repair moves counts 15/8 → 16/8), and
   `require_authorization()` accepts arbitrary bytes (CODEX ran frozen v9 against a referee brief
   and the guard passed). Both normative; both Duho's.

## DO NOT REOPEN

**The citation check in `tools/prereg_lint.py` is QUARANTINED to advisory** after three consecutive
two-seat NOT CLEARs. It emits `FABRICATED` against real citations (`CODEX-V4 F9` exists in
`GATE_CODEX_SUCCESSOR_V4.md`). Its findings carry category `repair-citations-advisory` and do not
fail the lint. A fourth repair attempt is explicitly out of bounds — the decision is filed.

## CLEARED — do not redo

- **BS-2a code gate**: CLEAR ×2 at round 6. `ref/bs2a_quality_gate.py` = `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`. Pinned in the
  §7 BS-2a row with its recorded limit. Slot stays DESIGN, UNFILLED.
- **Gain control repairs**: CLEAR ×2 at v6 (scoped). T-completeness still parked (decision 2).
- **`prereg_trace` refactor**: cleared by both seats; predicates unchanged.
- **V34's correction citations are real** — confirmed independently, twice.

## CURRENT DRAFT IS V36 (built 06:45 KST, NEVER REFEREED)

`PREREG_SUCCESSOR_DRAFT_V36_20260829.md` = `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177`

V35 came back **NOT CLEAR from both seats, but with both major repairs HELD**: §1 line 120 correctly
scoped without under-claiming, and §6.2 line 592 not relocating the false detection claim into
BS-2k's mouth. The only remaining finding from each was MEDIUM, wording-only, in the BS-2a pin —
now fixed in V36. Change vs V35: line 1, line 698, one §10 row. Class counts still 15/8; §1 scope
and §2.7 line 384 still V30-identical; four checkers pass.

**V36 ROUND IS RUNNING** — dispatched 06:46, both seats, reports to `gates/V36_WHOLE_REVIEW_<SEAT>.md`, log `gates/runner_v36_round.log`. **If those reports exist, read them before dispatching anything.** If V36 clears both seats, update this file to say so — that is the first two-seat CLEAR the draft would have had.

## V35 ROUND (done 06:31)

Both seats, reports to `gates/V35_WHOLE_REVIEW_<SEAT>.md`, runner
`gates/_tmp_v35_round.sh`, log `gates/runner_v35_round.log`. Brief
`gates/BRIEF_V35_REVIEW.md` carries the quarantine disclosure and keeps the absence-clause lens.
**If the reports exist, read them before dispatching anything.**

## PREVIOUS NEXT-DISPATCH NOTE (now done)

Referee round on **V35**, both seats, **same absence-clause lens** that made the V34 round the most
productive of the night. Brief pattern: `gates/BRIEF_V34_REVIEW.md`. Runner pattern:
`gates/_tmp_v34_round.sh`. Reports go to `gates/V35_WHOLE_REVIEW_<SEAT>.md`.
**The brief must repeat the citation-check quarantine disclosure** or a seat will infer from a green
lint something the lint cannot support.

## ARTIFACT INVENTORY — every current object, short hash

All paths relative to the repo root `/Users/duhokim/NebulaMind/NebulaMind`.
Lane = `.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824`.

| object | short sha256 | state |
|---|---|---|
| `<lane>/PREREG_SUCCESSOR_DRAFT_V36_20260829.md` | `e4d7b175` | **CLEAR ×2, 06:57** |
| `<lane>/ref/successor_ref_v9.py` | `6a9abbbd` | **FROZEN — never modify** |
| `<lane>/ref/bs2a_quality_gate.py` | `dfbd63d1` | CLEAR ×2 round 6; pinned in §7 |
| `<lane>/ref/gain_gradient_estimator.py` | `e2270297` | CLEAR ×2 gain v6 |
| `<lane>/gates/verify_mu_gamma.py` | `e33d9275` | CLEAR ×2 gain v6 |
| `<lane>/ref/verdict_breakpoints.py` | `bd248c93` | p-to-A reduction REFUTED; amplitude side + transcription survive |
| `<lane>/gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` | `1c3ced94` | §4 marked REFUTED/OPEN |
| `tools/prereg_lint.py` | `826512ce` | citation check QUARANTINED to advisory |
| `tools/prereg_trace.py` | `9bd194b9` | refactor cleared ×2 |
| `tools/void_registry.py` | `4980701c` | mechanism cleared ×2; content parked |

## WHAT CLEARED, AND WHEN

- **BS-2a code gate** — CLEAR ×2 at round 6 (02:37/02:44), scoped *"CLEAR for FREEZING the
  quality-predicate component; not a fill authorization."* Six rounds. Slot stays DESIGN, UNFILLED.
- **Gain control repairs** — CLEAR ×2 at v6 (02:46/02:53), scoped to the repairs. **The control is
  NOT freezeable**: T-completeness is decision 2 below. Do not rebuild the estimator; it is done.
- **`prereg_trace` refactor** — cleared ×2; predicates unchanged by the factoring.
- **V36 document** — CLEAR ×2 (06:57). First two-seat clear on the draft.

## VERIFY-BEFORE-TRUSTING

Every self-test is runnable and each ships negative controls. Run them rather than believing this
file: `bs2a_quality_gate.py --self-test` (36 controls), `gain_gradient_estimator.py --self-test`
(9/9 codes, none exempt), `verify_mu_gamma.py`, `verdict_breakpoints.py --self-test`,
`prereg_lint.py <draft> --gates <lane>/gates --self-test` (8 controls),
`prereg_trace.py <lane> --check <draft> --self-test` (3 scope rules),
`void_registry.py <draft> --self-test` (6 controls).

## THE NIGHT'S RECURRING DEFECT, so it is not repeated

**A narrow pattern is safe for presence and dangerous for absence.** Five times I wrote a pattern
narrower than the data and treated the data as wrong (phase vocabulary, emission idiom, heading
format, findings-section split, report-family filter). The citation check was quarantined because it
kept doing this in the absence direction. **Applying the same lens to the DOCUMENT — ~70 universal
negatives — produced a real finding in every round it was used**, including the two HIGH ones now
parked. If a future round needs an attack surface, that is the one that works.

## Operating notes that cost time

- `hermes` is NOT on PATH: `/Users/duhokim/.hermes/hermes-agent/venv/bin/hermes`. A bare `hermes`
  dies `command not found` and the runner log shows dispatch and done at the **same second**.
- **Never use an unquoted heredoc for briefs** — backticks execute and silently blank references.
  Use a quoted heredoc plus `sed` substitution. This bit twice tonight.
- A sibling lane commits with repo-wide `git add -A` and has swept DESI files into BHU commits.
  Check `git log -- <path>` before assuming your commit carried your files.
- Frozen: `ref/successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`. Never modify.
- **BS-6 and the first image byte remain blocked. Nothing tonight changed that.**
- Cron job `db6ea525` fires :13/:33/:53, bound 09:00 KST. Blanc relays independently.

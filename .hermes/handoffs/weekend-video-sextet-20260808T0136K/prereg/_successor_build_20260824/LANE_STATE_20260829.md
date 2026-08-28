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

## V35 ROUND IS RUNNING (dispatched 06:17 KST)

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

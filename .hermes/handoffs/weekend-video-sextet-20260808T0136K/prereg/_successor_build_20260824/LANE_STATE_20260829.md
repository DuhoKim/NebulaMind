# LANE STATE — DESI successor preregistration

**Single source of state for this lane. Last rewritten 2026-08-29 07:20 KST.**
Assume the reader is a compacted Hwao or a cold session with no memory of the night.
Rules and bounds live in `SELF_CONTINUATION_ORDERS.md`; reasoning lives in the commit log.

Repo `/Users/duhokim/NebulaMind/NebulaMind`, branch `feat/paper-workflow-v2`.
Lane root `.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_successor_build_20260824`,
written `<lane>` below.

> **Do not add a second file describing this state.** Two files describing one state is the defect
> this lane spent the night finding in other forms; it already bit here once, when a stale table said
> the draft was V34 while V35 existed with three fixes applied.

---

## 1. THE LANE IS BLOCKED ON FOUR HUMAN DECISIONS, NOT ON DISPATCH

There is no referee round worth running until at least one of these is answered. Each file states
the options and what each costs; each ends by saying it is not mine to take.

| # | file | what is blocked |
|---|---|---|
| 1 | `<lane>/OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` | Three verified §7.1 gaps — `degenerate`, `digest`, `chosen`. Both seats cleared the *mechanism* (the BS-2v circularity claim is false); the *content* is not complete. Amending §7.1 changes what the study normatively enumerates as voiding a run. |
| 2 | `<lane>/OPEN_QUESTION_T_COMPLETENESS.md` | The gain control's p-gated fork, options (a)/(b)/(c). I would drift to (a) because it is cheap — that is precisely why it is not mine. |
| 3 | `<lane>/OPEN_QUESTION_CITATION_CHECK.md` | Disposition of the quarantined check: delete / advisory forever / make reports machine-readable / verify by hand at freeze. My reading is C-for-future, D-for-corpus. |
| 4 | `<lane>/OPEN_QUESTION_BS6_DEPENDENCY_AND_AUTHORIZATION.md` | **The two largest findings of the night.** (i) "must be bound before BS-6" has no dependency edge that makes it true; the repair moves the frozen class counts 15/8 → 16/8. (ii) `require_authorization()` accepts arbitrary bytes — CODEX ran the frozen v9 against a referee brief and the guard returned success. |

**All four were written against V34/V35 and have been re-verified against V36 (07:25 KST).** Each
file now carries a `VERIFIED CURRENT AGAINST V36` stamp recording exactly what was re-checked: the
VOID registry digest is identical across V34/V35/V36; §5 line 493, §5 lines 511-514 and §2.7 line 388
are byte- and position-identical; §1 line 120 still ends "must be bound before BS-6" and V35's repair
to that line did not touch the clause; counts are 15/8 on V36. **No open question is stale.**

**`DECISIONS_FOR_DUHO.md` states all four in plain language** — the ask, the options, the cost and a
recommendation for each, pointing back at these files for evidence. It is an index, not a source; if
it and one of these files disagree, the file is right.

**Decisions 1 and 4 are seat-raised HIGH findings that I declared out of scope for a round. They
were parked, not resolved. V36 clearing does not retire them.**

---

## 2. CURRENT DRAFT — V38, BUILT 10:3x, NOT YET REFEREED

`<lane>/PREREG_SUCCESSOR_DRAFT_V38_20260829.md` = `b5776d287a22cff71fe34d1ee1dbe937f1af61d51ad70530f378668cbfe1ec56`

V38 = V37 + the §2.7 instant settled from the record (cell unchanged) + §5 recording the
`require_authorization` limit accurately without building anything. Checkers: 16/8 prose-matched,
trace 0 problems, registry 54/20 digest `a4d1d745…`, lint exits 1 on the known quarantined advisory.

### Superseded: V37, built 09:45

`<lane>/PREREG_SUCCESSOR_DRAFT_V37_20260829.md` = `62dd8a7525c399126477573d55a952f1ed2f147d16f8bfbb12aa89a295821c42`

**V36 (`e4d7b175…`) was CLEAR ×2 at 06:57 and remains the last REFEREED draft.** V37 applies the two
decisions Duho ruled on at 09:20, relayed by Blanc: VOID **option A**, BS-6 **option (a)**.

- `VOID-5-DEGENERATE` added (§5, `Post-unblinding` — the phase of its sibling in the same §5 clause).
- `VOID-5-DIGEST-DEVIATION` added (§5, `Any`) as a separate antecedent, not an undeclared alias.
- `VOID-2.7-THRESHOLD-MOVED` → `VOID-2.7-THRESHOLD-CHOSEN-OR-MOVED`. **Phase untouched, on purpose.**
- **`BS-3g` added — class P, DESIGN/UNFILLED, blocks BS-6.** Counts **15/8 → 16/8**, the first
  row-count change since V4. §1's sentence now names the edge that makes it true.
- §7.1 preamble states what the checker proves (**NAME-coverage only**) and what it does not.

**Checkers:** counts 16 P / 8 E, prose matches the table; trace 0 problems; `void_registry` 54
antecedents, 20 rows, no refusal, new `registry_digest a4d1d745…`. **Lint exits 1** on one advisory
from the quarantined citation check — see §5. Invariants hold: §2.7 line 384 and §1 lines 2–119 byte-
and position-identical to V30.

**THE §2.7 PHASE IS RESOLVED** — `Post-first-real-χ`, recovered from V11's commit `4d99d1d93` rather
than ruled on. My `Post-unblinding` recommendation was wrong (χ *exists* pre-unblinding; I confused it
with when χ is *read*). Registry digest unmoved at `a4d1d745…`, so the registry is unblocked.

**NOT DISPATCHED.** Per Blanc: do not dispatch if the phase question would land mid-round.

## 3. LAST REFEREED DRAFT — V36, CLEAR FROM BOTH SEATS

`<lane>/PREREG_SUCCESSOR_DRAFT_V36_20260829.md`
`e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177`
**CLEAR ×2 at 06:57 KST — the first two-seat CLEAR the document has had.**

Both seats verified the digest, the three-region delta, the V30 byte- and position-identical
invariants, class counts 15/8, and the BS-2a pin. CODEX ran a fresh whole-document absence-surface
attack and found no new repair-required defect. The two numbered items in each report are HELD
confirmations of the V35 repairs, not findings.
Reports: `<lane>/gates/V36_WHOLE_REVIEW_GPT56.md`, `<lane>/gates/V36_WHOLE_REVIEW_CODEX.md`.

### What the CLEAR means, and what it does not

It means **the text is a correct preregistration that is honest about being an unfinished
programme.** It does **not** mean the study may proceed.

Still true after it: BS-2a is DESIGN, UNFILLED; one of fifteen class-P slots is filled; BS-2v is
UNRESOLVED; rows C2 and E cannot run; Stage P is SUPERSEDED; **BS-6 and the first image byte remain
blocked**; and the four decisions in §1 are open.

### Lineage

| draft | sha256 | outcome |
|---|---|---|
| `PREREG_SUCCESSOR_DRAFT_V34_20260828.md` | `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948` | NOT CLEAR ×2 — the absence-clause round, four defects, the most productive round of the night |
| `PREREG_SUCCESSOR_DRAFT_V35_20260829.md` | `b80d50afe076fe8d20c9fd1a6e6b5db63779dfc02ee46601667a67227e12fbdd` | NOT CLEAR ×2, **both major repairs HELD**; only remaining findings were MEDIUM wording in the BS-2a pin |
| `PREREG_SUCCESSOR_DRAFT_V36_20260829.md` | `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177` | **CLEAR ×2** |

V35 = V34 + three fixes: §1 line 120 ("a biased or broken `w` cannot create one" narrowed to what
the antisymmetry identity actually enforces); §6.2 line 592 (the false claim that an unlogged archive
read breaks the log chain, deleted rather than relocated into BS-2k's mouth); §7 line 698 (my own
BS-2a pin overclaimed the pairwise deletion-probe evidence — CODEX's 325 was filter-derived with six
pairs literally source-mutated, and GPT56 did not run all 325).
V36 = V35 + line 1, line 698, one §10 row.

Invariant across all three, and to be re-checked after any future edit: **§1 scope and §2.7 line 384
byte- and position-identical to V30; class counts 15 class-P / 8 class-E; all four checkers pass.**

---

## 3. STANDING CONSTRAINTS — these outrank any plan

- **BS-6 and the first image byte are blocked.** Nothing in this lane has changed that, and nothing
  in it is authorised to.
- **Nothing is authorised to fetch study images.** Non-sample DR10 cutouts are authorised for
  instrument characterisation only, and must be *proven* outside the 65,060-object parent.
- **Do not read `/Users/duhokim/NebulaMindData/`.**
- **`<lane>/ref/successor_ref_v9.py` is FROZEN** = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`. Never modify it. (Decision 4(ii)'s
  repair would require changing it — which is half of why it stops here.)
- **The citation check is quarantined and must not be reopened** (§5).
- **FREEZE VERIFIED 2026-08-29 08:03 KST, from the file rather than from notes.** `successor_ref_v9.py`
  hashes to `6a9abbbd…` exactly as recorded, and at its current path it has **exactly one commit** —
  `cdbcc8945`, the commit that created it. Nothing has modified it since the freeze. (The eleven
  older commits `git log --follow` shows are predecessor versions v3/v4/v7/v8 at earlier paths, not
  edits to v9.) Re-run: `shasum -a 256 <lane>/ref/successor_ref_v9.py` and
  `git log --oneline -- <lane>/ref/successor_ref_v9.py`.
- **Lane fully committed, working tree clean** as of the same check: `git status --porcelain <lane>`
  is empty and all sixteen key files plus the four `tools/` checkers are tracked in HEAD — so every
  digest in §6 is the committed content, not an uncommitted local edit.
- Stop and write `OPEN_QUESTION_<topic>.md` for: a fork where both directions cost something; seats
  disagreeing on substance; anything changing what the study CLAIMS (tiers, acceptance rules,
  `|mu|max`, thresholds); filling a slot or touching BS-6; any repair I am not confident in.

---

## 4. CLEARED — do not redo

| what | when | scope of the clear |
|---|---|---|
| **BS-2a code gate** (`<lane>/ref/bs2a_quality_gate.py`) | CLEAR ×2, 02:37 / 02:44, after six rounds | *"CLEAR for FREEZING the quality-predicate component; not a fill authorization."* The slot stays DESIGN, UNFILLED. |
| **Gain control repairs** (`ref/gain_gradient_estimator.py`, `gates/verify_mu_gamma.py`) | CLEAR ×2, 02:46 / 02:53 | The repairs only. **The control is not freezeable** — T-completeness is decision 2. **The estimator work is done; do not rebuild it.** |
| **`prereg_trace` refactor** | CLEAR ×2 | `check_trace()` factored out of `main()`; all four refusal branches identical; three controls invoke it. |
| **VOID registry mechanism** | CLEAR ×2 | Digesting the canonical §7.1 rows and storing the digest in the BS-2v row creates no fixed point. Content is decision 1. |
| **V34's correction citations are real** | confirmed independently, twice | `CODEX-V11 3` and `GPT56-V11 F3` resolve to actual findings. No draft defect is implied by the citation-check failure. |
| **V36 document** | CLEAR ×2, 06:57 | §2 above. |

---

## 5. DO NOT REOPEN — the quarantined citation check

The citation check in `tools/prereg_lint.py` is **QUARANTINED to advisory** after three consecutive
two-seat NOT CLEARs. **CORRECTION 09:55 — its findings DO still fail the lint.**
The quarantine changed the category and message prefix, not the exit code: `main()` returns 1 for any
finding. V36 emitted none, so the claim was never exercised; V37 emits one and lint exits 1. Not
changed, because the disposition is decision 3 — see that file's correction block. It emits `FABRICATED` against real citations — `CODEX-V4 F9` exists in
`GATE_CODEX_SUCCESSOR_V4.md`, but `_reports_for` requires `"REVIEW"` in the filename, so it judged
the citation against an unrelated report. **Acting on that output would mean "fixing" a correct
document**, which is strictly worse than not checking.

Its findings now carry category `repair-citations-advisory` and **do not fail the lint**. A fourth
repair attempt is explicitly out of bounds; the disposition is decision 3.

**Any dispatch brief must repeat this disclosure**, or a seat will infer from a green lint something
the lint cannot support.

---

## 6. ARTIFACT INVENTORY

| object | short sha256 | state |
|---|---|---|
| `<lane>/PREREG_SUCCESSOR_DRAFT_V36_20260829.md` | `e4d7b175` | **CLEAR ×2, 06:57** |
| `<lane>/ref/successor_ref_v9.py` | `6a9abbbd` | **FROZEN — never modify** |
| `<lane>/ref/bs2a_quality_gate.py` | `dfbd63d1` | CLEAR ×2 round 6; pinned in §7 |
| `<lane>/ref/gain_gradient_estimator.py` | `e2270297` | CLEAR ×2 gain v6 |
| `<lane>/gates/verify_mu_gamma.py` | `e33d9275` | CLEAR ×2 gain v6 |
| `<lane>/ref/gain_gradient_kernel.py` | — | vector kernel; Var(cos theta) = 0.751761 |
| `<lane>/ref/verdict_breakpoints.py` | `bd248c93` | **its central p-to-A reduction is REFUTED** (recorded at the top of the module); amplitude side + transcription test survive |
| `<lane>/gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` | `1c3ced94` | §4 marked REFUTED/OPEN |
| `tools/prereg_lint.py` | `826512ce` | citation check quarantined to advisory |
| `tools/prereg_trace.py` | `9bd194b9` | refactor cleared ×2 |
| `tools/void_registry.py` | `4980701c` | mechanism cleared ×2; content parked |
| `<lane>/CITATION_CHECK_SPEC.md` | — | written before code, per Blanc; the code diverges from it, which is part of why it was quarantined |

Numbers worth not re-deriving: BS-2a `EXPECTED_RETAINED = 49_211`, `PARENT_KEYSET_SHA256 = 550e50a8…`,
`EVIDENCE_SHA256 = 0afba44f…`. Production gain is `2a-1` from `inject_signs()` (v9:1199). Calibration
bins are cos theta tertiles (v9:1359). `gamma = slope/intercept` from **one** GLS fit — not
slope/sample-mean, which equals `gamma/(1 + gamma*mean(c))`. `kappa = Cov(c^2,c)/Var(c) = +0.005104`.

---

## 7. VERIFY BEFORE TRUSTING THIS FILE

Every check is runnable and ships negative controls. Run them rather than believing this file:

    <lane>/ref/bs2a_quality_gate.py --self-test          # 36 controls, 26 codes E01-E26
    <lane>/ref/gain_gradient_estimator.py --self-test    # 9 codes G01-G09, none exempt
    <lane>/gates/verify_mu_gamma.py
    <lane>/ref/verdict_breakpoints.py --self-test
    tools/prereg_lint.py <draft> --gates <lane>/gates --self-test    # 8 controls
    tools/prereg_trace.py <lane> --check <draft> --self-test         # 3 scope rules
    tools/void_registry.py <draft> --self-test                       # 6 controls

Read `void_registry`'s output as **name-coverage only**: `V05`/`V06` prove a §6.1 row is *named* by
some antecedent, not that the antecedent semantically covers the row's forbidden column. The check is
unchanged; only its overclaiming name was fixed. "20 of 20 rows covered" is weaker than it looks.

---

## 8. THE RECURRING DEFECT — the one lens that kept working

**A narrow pattern is safe for presence and dangerous for absence.** (Tori's lane stated it; it
generalises.)

I violated it five times in one night — phase vocabulary, emission idiom, heading format,
findings-section split, report-family filter — each time writing a pattern narrower than the data and
then treating the data as wrong. It is why the citation check is quarantined: it kept using a pattern
to establish a negative, which is unsound by construction.

**Turned on the DOCUMENT — its ~70 universal negatives — the same lens produced a real finding in
every round it was applied,** including both HIGH items now parked. If a future round needs an attack
surface, that is the one that works. Related defect class, seen across six BS-2a rounds: **a verifier
that raises has not refused.** Probe deletions strictly — a crash must never count as detection.

---

## 9. OPERATING NOTES THAT COST TIME

- `hermes` is **not** on PATH: `/Users/duhokim/.hermes/hermes-agent/venv/bin/hermes`. A bare `hermes`
  dies `command not found` and the runner log shows dispatch and done at the **same second**.
- **Never use an unquoted heredoc for a brief** — backticks execute and silently blank references.
  Quoted heredoc plus `sed`. This bit twice.
- Report filenames carry a `_R<N>` suffix so two rounds cannot overwrite one file.
- A seat can exhaust its iteration budget, write **no** report, and leave a stale earlier file in
  place. Check mtime and heading, not just the filename.
- Never modify a subject while a seat is reviewing it. The POST-CHECK exists for exactly this, and
  doing it once already cost GPT56's round-4 findings.
- **The shell here is zsh, which does NOT word-split an unquoted parameter.** `for c in "prog --flag"; do python3 $c; done` passes the whole string as one filename. Worse, it produced a *false green*: the probe printed `exit=0` beside every failure, because `$?` was read after an intervening command. All seven self-tests above were re-run explicitly and pass on V36 — that is the checked claim; the first run was a broken harness, not broken code.
- A sibling lane commits with repo-wide `git add -A` and has swept DESI files into BHU commits.
  Check `git log -- <path>` before assuming your commit carried your files.

---

## 10. THE SELF-CONTINUATION LOOP IS CLOSED

Cron `db6ea525` was **deleted at 08:43 KST**, 17 minutes inside its 09:00 bound.
`SELF_CONTINUATION_ORDERS.md` is marked DORMANT and is now a record, not a live instruction.

It ran 00:40 -> 08:43. What it produced after the V36 clear was verification, not new construction:
the open questions re-checked against V36 rather than the draft they were written on, the v9 freeze
proven from the file and its history instead of from notes, lane commit integrity confirmed, the
stale VOID priority marked BLOCKED, and the four decisions restated in plain language.

**It was closed early on purpose.** Every remaining path crosses a decision that is Duho's, and
continuing would have meant inventing work to look busy — the same failure the orders warn about in
the registry-check paragraph. **Do not restart the loop without a fresh authorisation.**

**To pick the lane back up:** read `DECISIONS_FOR_DUHO.md`, take one of the four decisions, then
re-read §1–§3 here before touching anything.

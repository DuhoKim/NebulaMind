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

**Decisions 1 and 4 are seat-raised HIGH findings that I declared out of scope for a round. They
were parked, not resolved. V36 clearing does not retire them.**

---

## 2. CURRENT DRAFT — V36, CLEAR FROM BOTH SEATS

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
two-seat NOT CLEARs. It emits `FABRICATED` against real citations — `CODEX-V4 F9` exists in
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
- A sibling lane commits with repo-wide `git add -A` and has swept DESI files into BHU commits.
  Check `git log -- <path>` before assuming your commit carried your files.

---

## 10. IF A CRON TICK FIRES

Cron `db6ea525` fires at :13/:33/:53, self-continuation bound **09:00 KST**; past that, `CronDelete`
it and write a handover. Blanc relays independently.

**Before 09:00 there is nothing to dispatch.** The instruction on a tick is: confirm no seat report
or human answer has landed, and stop. Do not open a new object, do not re-run a cleared gate, and do
not spend seat quota on a question that cannot be acted on alone. Duho's last instruction was to
commit and hold.

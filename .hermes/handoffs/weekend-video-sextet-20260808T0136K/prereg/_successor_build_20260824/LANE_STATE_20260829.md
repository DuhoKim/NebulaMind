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

## 1. TWO OPEN QUESTIONS. Nine have been ruled on today.

| # | file | status |
|---|---|---|
| 1 | `OPEN_QUESTION_PRE_UNBLINDING_NUMERICAL_ROUTES.md` | **OPEN, and larger than when it was raised.** Row F's FAIL branches have no named outcome. The principal ruled **option A** (reuse an existing outcome if one honestly fits); **A has failed on its own terms** — `INCONCLUSIVE-BY-CALIBRATION`'s third producer is scoped to *aggregates* at BS-8f, not bins/allocation at P3, and an infeasible allocation is not a non-finite aggregate at all. **My reading is now B scoped as a rule, not one code for Row F.** |
| 2 | `OPEN_QUESTION_GAIN_SIGN_MAPPING.md` | **OPEN, unchanged.** What counterfactual sign vector a gain gradient γ produces. `ref/gain_counterfactual_path.py` is built and refuses to run without a mapping. |

**Scale established for question 1, since the principal ruled against a two-branch problem:**
**Row F alone is nine raise sites** — one `degenerate calibration bins`, plus **eight distinct
feasibility failures** in `allocate_handcheck`. Across the pinned reference: **111 raise sites, 3
typed to a named outcome, 69 bare.** Classified by what each guard tests: 29 caller-input guards, 31
reachable run-time failures, **48 undecidable without reading** — so the class is **at least 31, at
most 79**, reported as a bound rather than a number. **The defect is not confined to pre-unblinding**:
the decision path (`_finite`, `w_profile`, `sigma_ours_*`) raises bare errors post-unblinding too.

**RULED TODAY — do not reopen:** VOID registry **A**; BS-6 slot **(a)** (counts 15/8 → 16/8); VOID-5
phase scope **C**; the gain fork **(b), "real gate"**; citation check **C**; legacy corpus **D**;
rerun procedure **A** (halt is terminal); `INCONCLUSIVE-BY-COMPUTATION` **D** (deleted); Row F
direction **A** (*failed on its own terms — back to the principal*). The **§2.7 phase** was not ruled
but **recovered from V11 commit `4d99d1d93`**. **`require_authorization` stays deprioritised.**

## 2. CURRENT DRAFT — V48, BUILT, NOT DISPATCHED

`<lane>/PREREG_SUCCESSOR_DRAFT_V48_20260829.md` = `8d2e68f7f52db1268d89df69d33eb055753b465bda4191f45031961660973ff7`

**Last refereed draft: V46** (`c5afba31f909dcda`) — **NOT CLEAR ×2 at 14:06.** V47 and V48 are not
refereed.

| draft | sha256 (short) | what it did |
|---|---|---|
| V43 | `7b2e9a701c38c570` | rerun allowance deleted (option A). **NOT CLEAR ×2**, 13:33 |
| V44 | `4faa2564ba093ae4` | all five V43 findings. **NOT CLEAR ×2**, 13:49 |
| V45 | `4fcc9c3460abfe2d` | §11's BS-3g item — the second site cited at V43 and missed at V44 |
| V46 | `c5afba31f909dcda` | `INCONCLUSIVE-BY-COMPUTATION` deleted (option D), with the record kept. **NOT CLEAR ×2**, 14:06 |
| V47 | `bc0fd1f0aa9537f2` | **retracts** the completeness argument both seats broke — §2.7(c) is *catalogue quality*, and the enumeration had missed Row F |
| **V48** | `8d2e68f7f52db126` | §11 exception-to-outcome conversion item, required under any resolution; decides no outcome for any branch |

**Not dispatched on purpose.** The open question above would be re-found immediately, and the
principal's answer will change §5/§11 text a round would be reviewing.

**Checkers on V48:** counts **16 P / 8 E** prose-matched; trace 47 transitions, 0 problems;
`void_registry` self-test 6/0; lint exits 0.

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

## 5. THE CITATION CHECK IS REBUILT AND ITS CORPUS QUESTION IS CLOSED

**Option C (rebuilt) and option D (corpus scope) are both ruled and done.**

`tools/citation_block_check.py` reads `FINDINGS-BLOCK v1`; reports are indexed **by the blocks they
declare, never by filename**, which removes the defect that made the old check call a real citation
fabricated. Compound citations (`KIMI/GPT56-V11 F4`) are expanded and **every named seat is checked**
— previously only the last seat was seen, which hid a real miscitation.

Three categories in `prereg_lint.py`, two of which block: `repair-citation-fabricated` and
`repair-citation-malformed` fail the lint; **`repair-citation-legacy` is advisory and does not.**
Advisory now genuinely does not block — `main()` returns 1 only for non-advisory categories.

**Option D, ruled by the principal:** verify only the repair-announcing citations. The criterion is
in `CRITERION_LOAD_BEARING_CITATIONS.md`, derived from `CITATION_CHECK_SPEC.md` (committed 05:19,
before the corpus was measured) with the bias risk disclosed. Applied: **12 of 108 selected (11%),
96 not, 0 unclassifiable.** All 12 verify — 8 hand-checked for topical match, 4 machine-VERIFIED.

**Read the result precisely:** a clean D result means *every repair-announcing citation is sound*. It
does **not** mean the citations are correct — the one wrong citation found in the whole corpus sits
in a passage D does not select. **The 96 keep reporting `NO_BLOCK`; that is now their permanent
answer, not a deferral.** Do not let them drift to `UNVERIFIABLE` or `VERIFIED`.

**Historical reports must not be retrofitted with blocks** (option B is rejected).

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


**Added since this inventory was last written:**

| object | short sha256 | state |
|---|---|---|
| `<lane>/PREREG_SUCCESSOR_DRAFT_V42_20260829.md` | `6c9cc2fc` | current, brief ready, NOT dispatched |
| `<lane>/ref/gain_counterfactual_path.py` | `f8e50750` | option (b) path; refuses without a mapping |
| `<lane>/CRITERION_LOAD_BEARING_CITATIONS.md` | `62b3c925` | option D criterion + results |
| `tools/citation_block_check.py` | `3fede692` | 12 controls, deletion probe catches all four outcomes |
| `tools/prereg_lint.py` | `6819fa1c` | option C wired; advisory no longer blocks |
| `tools/void_registry.py` | `8eca2f91` | fixture controls; self-test green V34-V42 |

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


## 8a. A CONTROL THAT ENCODES THE CURRENT STATE GOES RED WHEN AN AUTHORISED CHANGE LANDS

**Written jointly with Blanc, 2026-08-29, because both of us did it on the same day and neither
noticed for days.**

- **Mine:** `void_registry.py`'s self-test asserted the compound-gap heuristic still finds
  `degenerate`, `digest` and `chosen`. **The principal's option A closed those three at V37**, so the
  heuristic correctly went quiet and the control demanding them went red — through V37, V38, V39 and
  V40, **while I reported that checker's output on all four drafts.** Its other half was worse: it
  patched a `VOID-5-DEGENERATE` row into the live text and checked for silence, which became a no-op
  the moment that row really existed, so it passed while testing nothing.
- **Blanc's:** their verdict probe read a bare `**CLEAR**` from prose ahead of the verdict section
  and reported **V34 CODEX as CLEAR when its real verdict was NOT CLEAR**, for days, and that reading
  was relayed upward. It also matched nothing at all on V38, because the seats write `**NOT CLEAR.**`
  with the period inside the asterisks — so a round that genuinely cleared in that style would have
  been missed entirely.

**The rule, in two parts:**

1. **A control must assert the MECHANISM, not a transient state of the document.** "The heuristic
   flags an unnamed branch" survives a ruling; "the heuristic finds these three specific gaps" does
   not. Both of mine are now fixture-based and give identical results on V34 through V43.
2. **When a ruling changes normative content, re-derive the controls that assert things about that
   content IN THE SAME COMMIT** — not at the next round. The gap between an authorised change and the
   control catching up is exactly where a red control sits unread.

**And the sharper half: a red control nobody reads is indistinguishable from a green one.** I ran the
main path and not `--self-test` for four drafts. Running a checker is not the same as checking it.


## 8b. THIS FILE DRIFTS BECAUSE THE LANE IS PRODUCTIVE, AND IT DRIFTS THE DANGEROUS WAY

Three times today `LANE_STATE` went stale, and **every time it was stale in the direction that
misleads** — it named an older draft as current and an already-answered question as open. A reader
following it would have dispatched a superseded subject.

It is not carelessness about the file; it is a structural consequence. **State drifts fastest exactly
when rounds are landing and rulings are arriving**, which is when a reader is most likely to consult
it. The fix that has actually worked is not more diligence but a trigger: **refresh state whenever no
round is live and the build queue is empty** — that is the moment the file is both wrong and cheap to
correct, and it is where two of the three refreshes happened.

**Drift record:** §2 said "V40, ROUND RUNNING" after the round finished and two drafts existed; §10
said the self-continuation loop was CLOSED forty minutes before it was renewed; §1 said "ONE OPEN
QUESTION / V43 READY TO DISPATCH" while V48 stood with two open. **The state file is the one artifact
here with no adversarial reader** — the drafts get seats, the checkers get controls, this gets
whatever attention is left over.

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
- **PROVENANCE WARNING, 2026-08-29 13:2x.** `PREREG_SUCCESSOR_DRAFT_V43_20260829.md`,
  `LANE_STATE_20260829.md` and `BRIEF_V43_REVIEW.md` were **committed by the sibling BHU lane** in
  `36fe5cfdf probe(bhu): stale cross-entry claims`, not by a DESI commit. That lane commits with a
  repo-wide `git add -A`, so my files were staged by its sweep before my own commit ran — and my
  commit then found nothing to stage and did not exist. **The work is committed and intact; only its
  message is misleading.** `git log --oneline -- <path>` is the reliable way to date this lane's
  artifacts, never `git log` alone. This hazard was already in the operating notes below; today it
  actually fired.
- A sibling lane commits with repo-wide `git add -A` and has swept DESI files into BHU commits.
  Check `git log -- <path>` before assuming your commit carried your files.

---

## 10. THE SELF-CONTINUATION LOOP IS ACTIVE — renewed, not closed

**Cron `4a937173`, ticks :07/:27/:47, bound 21:00 KST today.** Renewed by Duho at 10:15 and relayed
by Blanc. The earlier job `db6ea525` was deleted at 08:43; **this section previously said the loop
was closed, which was true for forty minutes and dangerously wrong afterwards.**

Rules are in `SELF_CONTINUATION_ORDERS.md`. On a tick: if seats are running, do not disturb them or
touch anything under review. If a round has both reports, read the verdicts. Otherwise work the build
queue — **both queue items are now complete**, so the honest answer on most ticks is that the lane is
blocked on the two open questions in §1.

**A question about this lane's own words is not a question for the principal.** He refused the §2.7
phase with *"I didn't write it, ask an agent who wrote it"* and was right. Check `git log` for
authorship before escalating; if this lane wrote the words, recover intent from the commit and the
findings it answered.

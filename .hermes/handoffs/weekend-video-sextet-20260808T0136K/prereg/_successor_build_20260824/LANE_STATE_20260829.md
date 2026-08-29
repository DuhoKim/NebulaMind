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

## 1. FOUR OPEN QUESTIONS, and TWO BUILDS ahead of them

**Build queue — both authorised, neither started. These come first on resumption.**

1. **BS-3g schema, producer, verifier, failure behaviour** (Duho 20:35, *"fix the BS-3g schema and
   producer"* — **top item, ahead of the rederivation**). Document content, half one of CODEX-V56 F2.
   **Constraints:** state the fields so someone who did not write the schema can implement the
   verifier, and **show** BS-3g's receipt cannot carry a per-object field — §6.1's non-χ claim rests
   on it. **Not started: 13 minutes before the bound would have produced the half-specified thing
   CODEX just caught.**
2. **Redo the refusal-vocabulary derivation from scratch** (Duho 20:30). Not a ninth code. Must cover
   **authorisation** *and* **availability/mediator behaviour**, with a **tested** joint-exhaustiveness
   argument. `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` does not survive as written.

**Half two of CODEX-V56 F2 is answered and needs no unfreeze** —
`ANSWER_RECEIPT_UNKNOWN_SLOT_AND_V9.md`. `receipt()` accepts arbitrary fields for any slot absent from
`SLOT_SCHEMA`; **five are absent** (BS-3g, BS-2a, BS-2k, BS-L, BS-2v). A successor-layer
`receipt_strict()` closes the mechanism with **v9 untouched at `6a9abbbd`** — but only if the document
**binds every producer to it** and a verifier checks emitted slots. **The unfreeze question returns
only if some producer cannot be routed through the wrapper.**

| # | file | what is open |
|---|---|---|
| 1 | `OPEN_QUESTION_GAIN_SIGN_MAPPING.md` | **B is ruled out as a gate** by the valid retry (f\* ≈ 0.0007, 20–49 signs of 49,211). **A is the live candidate**; its seed/quantile policy is the next question. Caveat: one fixture, one calibration — re-derive the margin at the real calibration before discarding B finally. |
| 2 | `OPEN_QUESTION_V52_RESIDUE.md` | Ledger's per-raise unit (needs a call-graph); `VOID-6.1L-WRONG-SIGNATURE` P7-only while Row L signs at P0/P6/P7. |
| 3 | `OPEN_QUESTION_V53_RESIDUE.md` | The freeze-signature exemption is unbounded; BS-2v UNRESOLVED for a self-reference its own checker disproves. |
| 4 | `OPEN_QUESTION_V54_RESIDUE.md` | The evidence bar lets sampling establish a status named for a proof; the post-unblinding double-claim recurred; `NUMERICAL-PLANNING` unauthorised; the 80,000-execution rerun has no pinned harness. |

**Check §1 against disk with a PREFIX match** — an exact-close pattern once hid an urgent question:

    grep -l '^\*\*STATUS: OPEN' <lane>/OPEN_QUESTION_*.md

## 2. CURRENT DRAFT — V57, BUILT, NOT DISPATCHED

`<lane>/PREREG_SUCCESSOR_DRAFT_V57_20260829.md` = `a2c48d0cfe7511b67f3fe1e813720af01964ef1654a43e3add616a20eb8fed00`

**Last refereed: V56** (`c0743b40698e75b6`) — NOT CLEAR ×2 at 20:22 (GPT56 5, CODEX 6).

V57 **withdraws the closure argument and suspends the eight-code set**, records that the enumeration
missed a *class* not a member, marks `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` as not surviving,
**deliberately does not re-pin the fingerprint** (re-pinning would make the checker green about
something it no longer describes), removes the hand-copied CALLER/NUMERICAL totals in favour of the
generated ledger, and reclassifies `inject_signs`' supplied-accuracy guard and mask-c admissibility as
`CALLER`.

**`gates/BRIEF_V57_REVIEW.md` is written.** Dispatch was **held** so BS-3g half one can go in first.
**`refusal_vocabulary_check.py` reports R05 on V57 — that is the designed state**, not a defect.

**PROVENANCE:** V57, its brief and the ledger were swept into BHU commits `ff0d6b4b7` / `a9974f78f` by
the sibling lane's repo-wide `add`. Rationale is in `7f177593b`. **Date this lane's artifacts with
`git log -- <path>`.**

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


## 8c. A NARROW PATTERN, USED TO AUDIT A NARROW PATTERN, THREE LEVELS DEEP

**Corrected 2026-08-29 19:3x. The version of this section written at 16:0x contained a false claim
and is replaced.**

**The facts.** GPT56's V49 report states its verdict **twice**: line 3 reads `**Verdict: NOT CLEAR.**`
and line 69 carries the contracted `VERDICT: NOT CLEAR` footer. V52 is the same. **V49 and V52 were
both genuine two-seat rounds.** Every brief since V42 contracts for the footer, and GPT56 has emitted
it since V38.

**How three readers missed one of the most prominent lines in the file:**

1. **Blanc's probe** required the verdict word alone inside the emphasis — `**NOT CLEAR.**`. GPT56
   moved the label inside the bold, `**Verdict: NOT CLEAR.**`, and the probe returned no-token.
2. **Blanc then opened the file to verify the probe and grepped for the same shape the probe had just
   failed on**, found nothing, and reported an absence.
3. **I audited that claim with `\*\*(NOT )?CLEAR\*\*`** — a *different* narrow shape, requiring the
   bold to contain only the token. The `Verdict: ` prefix and trailing period defeated it. **I then
   wrote into this file that the report "lacks a bold `**NOT CLEAR**` token", which was false**, while
   correcting someone else's false claim about the same file.

**The rule this earns: when auditing a pattern that failed in the absence direction, do not verify
with another pattern of the same kind.** Read the artifact, or anchor on the contracted form. A second
regex is not an independent check of a first regex — it is the same instrument with a different
setting, and it will fail on the same class of input.

**Where the exposure actually is here.** `citation_block_check.py` and `prereg_lint.py` read seat
reports **only** through the contracted `FINDINGS-BLOCK` marker at column 0; `_reports_for` and
`declared_findings` survive solely in a comment explaining their removal. **The tools anchor on the
contract. The failures were ad-hoc greps typed during a turn**, which are uncontrolled by
construction — no negative control, no positive control, used once and believed.

**Still true, and now better supported:** do not require both a prose verdict and a block verdict.
The brief contracts for one; a seat volunteering a second is fine, and demanding both would create
two sources for one fact — the drift this lane has spent the day repairing.

    grep -m1 '^VERDICT:' <report>.md        # the contracted form, and the authoritative one

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

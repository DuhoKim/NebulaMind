# BRIEF — V62 whole-document referee round

**Subject:** `PREREG_SUCCESSOR_DRAFT_V62_20260829.md`
**sha256 `70c0bcfa95dbec37873b56414061750fc2015090879dd26aabe7f45014eba251`**
Verify this digest before reading. If it does not match, stop and report the mismatch.

**Last refereed draft: V56** `c0743b40698e75b6` — **NOT CLEAR from both seats**, 20:22 (GPT56 5,
CODEX 6). Before that, V54 `b0ccbecc46e21677` — **NOT CLEAR from both seats**, 19:58 (GPT56 5,
CODEX 3). Three are answered below, four are referred. Before that, V53 `cc4e289578b129e4` — **NOT CLEAR from both seats**, 19:32 (GPT56 3,
CODEX 4). Five of those seven are answered below. Before that, V52 `a825e5d2045721c4` — **NOT CLEAR from both seats**, 19:18 (GPT56 3,
CODEX 5). Six of those eight are answered below. Before that, V49 `d8a9501e0653dd84` — **NOT CLEAR from both seats**, 15:47 (GPT56 7,
CODEX 3). Eight of those ten are answered below. Before that, V46 `c5afba31f909dcda` — **NOT CLEAR from both seats**, 14:06 (2 findings
each). Both are answered. Before that, V44 `4faa2564ba093ae4` — **NOT CLEAR from both seats**, 13:49 (2 findings
each). Both are answered. Before that, V43 `7b2e9a701c38c570` — **NOT CLEAR from both seats**, 13:33 (GPT56 3
findings, CODEX 2). All five are answered in V44. Before that, V40 `531d3f40f06130e792ff474e660fde931038e2d7bd8e573612b90c8ec624c1f6`
— **NOT CLEAR from both seats**, 11:26 (GPT56 7 findings, CODEX 4). V41 and V42 have not been
refereed.

## What changed since V40

**V41** `5270452ff9a54caf` — two V40 findings:
- **GPT56-V40 F4 / CODEX-V40 F4 (both seats).** `BS-3g` was missing from §6.1's closed
  non-χ-bearing receipt list. That list is exhaustive and everything off it is χ-bearing by default,
  so the slot's `blocks BS-6` edge was not receiptable. Added, plus a **§11 code-side item** — a
  receipt class with no producer or verifier is still not receiptable, and that goes slightly past
  the letter of the finding.
- **GPT56-V40 F6.** The §2.7 evidence citations were wrong for a second consecutive draft. V38 named
  §6.1/§6.2; V39's repair replaced those with **absolute line numbers**, which were already stale by
  V40 because the option-C edit added nine lines to §5. Both references are now by section and
  quoted content.

**V42** `6c9cc2fca67d5aff` — one miscitation found by hand-verification, not by any tool:
the Stage-P dual-valued passage cited `KIMI-V11 F4`, which is a **§6.1 access finding**. KIMI's
Stage-P finding is **F7** (*"the exact-null Stage P is not implemented in the file §0 pins"*), which
is the argument the passage actually makes. Corrected.

**V43** `7b2e9a701c38c570` — **the principal ruled option A on the rerun procedure: delete it.**
`INCONCLUSIVE-BY-COMPUTATION` is now a **terminal halt**; the operator's recourse is a new run
under a new preregistration, not a retry inside this one. This dissolves GPT56-V40 F1/F2/F3 and
CODEX-V40 F1/F2/F3 together — **no seed schedule, no attempt log, no verifier, no attempt cap, no
new slot, and class counts stay 16/8.** §6.1 Row J's one-outcome contract stops being contradicted
rather than being defended. **GPT56-V40 F5** is also closed: `INCONCLUSIVE-BY-COMPUTATION` is now
explicitly **subordinate to `INCONCLUSIVE-BY-CALIBRATION`** where both would apply. F5 was
re-checked against the deletion rather than assumed to dissolve with it — **it survived**, because
the overlap concerns which code fires, not the rerun.

## What is deliberately unrepaired — do not re-derive

**All V40 findings are answered.** Out of scope here:

- **The gain control's γ → sign-vector mapping** (`OPEN_QUESTION_GAIN_SIGN_MAPPING.md`) — with the
  principal. `ref/gain_counterfactual_path.py` is built and **refuses to run without a mapping**;
  supplying one is a modelling assumption requiring preregistration.
- **`require_authorization`** — deprioritised by the principal. Its limit is recorded accurately in
  §5 and is deliberately not repaired; `successor_ref_v9.py` stays frozen.

## THE LINT'S CITATION BEHAVIOUR HAS CHANGED SINCE V40 — read before running it

At V38 and V40 the citation check was **quarantined**: it emitted `repair-citations-advisory` and,
contrary to its own comment, **still failed the lint**. Both are now false.

The principal ruled option C, then option D. The check reads `FINDINGS-BLOCK v1` and indexes reports
**by the blocks they declare, never by filename** — removing the defect that made it call a real
citation fabricated. Compound citations (`SEAT/SEAT-Vn Fk`) are expanded and **every named seat is
checked**; previously only the last was seen, which is what hid the V42 miscitation above. Three
categories, two of which block: `repair-citation-fabricated` and `repair-citation-malformed` fail;
**`repair-citation-legacy` is advisory and does not.**

**On V62 the lint exits 0 — 96 advisory findings, 0 blocking.** The 96 are citations whose reports
predate the block format. **Under the principal's option D ruling that is their permanent answer, not
outstanding work.** Do not report them as unresolved.

Other checkers on V62: counts **16 class P / 8 class E** prose-matched; `prereg_trace` 61 transitions,
0 problems; `void_registry` self-test 6 controls, 0 failures.

## What V60, V61 and V62 changed — your V59 findings, and three principal rulings

**Last refereed: V59** `9257411511b39de6` — NOT CLEAR ×2 at 21:37 (GPT56 7, CODEX 5).

**V60 — BS-3g binds its sample** (GPT56-V59 F3 / CODEX-V59 F3, both HIGH). The nine-field schema bound
the *code* and not the *data*, so a conforming receipt could certify a favourable subset. Now twelve
fields: **`mask_sha256` must EQUAL BS-2f's pinned `mask_digest`** — a subset has a different digest, so
the equality is the binding; `perturbation_manifest_sha256` makes `n_perturbations` checkable rather
than asserted; `calibration_sha256` because the invariance margin depends on it.

**V61 — three principal rulings.** Row L's antecedent gets the row's own phases **P0/P6/P7**, and the
exemption is re-anchored to **canonical body digests** so widening cannot re-catch the exempt
signatures. **The canonical freeze-signature body and verifier are specified** — CODEX-V53 F4 was that
naming an object is not narrowing when the object has no canonical form. **BS-2v's false reason is
corrected while the slot stays UNRESOLVED**, with pinning stated necessary-not-sufficient.

**V62 — your remaining V59 findings.**
- **CODEX-V59 F2 / GPT56-V59 F1.** **You fired V59's own STOP condition and you were right.** The
  binding is scoped to **slot-receipt producers**; the V59 wording swept in seven rows emitting
  non-slot artefacts, which `receipt_strict()` refuses by design. **It was my overbreadth, not an
  unbindable producer — so this is not a path back to unfreezing v9, which stays at `6a9abbbd`.**
  **BS-7p is explicitly bound.**
- **GPT56-V59 F5 / CODEX-V59 F4.** Both digests were right and the **label** was wrong: `fd6d6d7e…` is
  the row fingerprint, `c2ccebbc…` is the tool file's sha256.
- **GPT56-V59 F7 / CODEX-V59 F5.** §5 now **quotes** the generated ledger instead of restating a count
  that has drifted three times.

## Known and parked — do not spend the round re-deriving these

- **GPT56-V49 F1, the access log's unconstrained refusal reasons.** Confirmed; a closed eight-code
  vocabulary is **drafted and with the principal** (`PROPOSAL_ACCESS_LOG_REFUSAL_VOCABULARY.md`).
  **No draft text has been changed for it.** Report only if the drafted set is itself wrong.
- **GPT56-V52 F3 / CODEX-V52 F3 — the ledger classifies per raise statement, not per call site.**
  Confirmed and **referred**: the fix is a call-graph build. **Enumeration sound, unit wrong.**
- **CODEX-V53 F4 — the freeze-signature exemption is unbounded**, because no canonical body or
  verifier defines which signed bytes qualify. Confirmed and **referred**
  (`OPEN_QUESTION_V53_RESIDUE.md`); defining it is new normative machinery.
- **GPT56-V53 F2 — BS-2v is UNRESOLVED for a self-reference its own checker disproves.** Confirmed
  and **referred**; moving a slot off UNRESOLVED is a claim about what the study has settled.
- **CODEX-V52 F4 — `VOID-6.1L-WRONG-SIGNATURE` is P7-only while Row L signs at P0/P6/P7.**
  Confirmed and **referred**; changing an antecedent's phase changes what voids a run.
- **The γ → sign-vector mapping** (`OPEN_QUESTION_GAIN_SIGN_MAPPING.md`), open with the principal.
- **`require_authorization`**, deprioritised; its limit is recorded and deliberately unrepaired.

- **The four V54 findings referred to the principal** (`OPEN_QUESTION_V54_RESIDUE.md`): the evidence bar lets sampling establish a status named for a proof; the post-unblinding double-claim has recurred; `NUMERICAL-PLANNING` is a category the rule never authorised; and the 80,000-execution rerun has no pinned harness. **All confirmed — do not re-derive them.**

## Attack these specifically

- **Did V41's `BS-3g` additions actually make the edge receiptable**, or only appear to? The §11 item
  is named and not specified — say if that is insufficient.
- **Does the scoped binding leave a slot receipt unbound?** Find a producer of a `SLOT_SCHEMA`
  artefact that can still reach `v9.receipt()` directly. **If one exists, say so plainly — that is
  the unfreeze path and it is the principal's.**
- **Can BS-3g's mask binding be defeated?** The claim is that equality with BS-2f's `mask_digest`
  prevents certifying a subset. Try to construct a receipt that satisfies it while covering less.
- **Is BS-3g's per-object claim actually a property?** §11 argues no field can carry a per-object
  quantity *because of the field list itself*. Try to defeat it — a field that admits an
  object-indexed value, or a route by which an extra field survives `receipt()`'s both-directions
  check.
- **Is the producer binding complete?** Find a producer named in §6.1 or §7 that could construct a
  receipt without going through `receipt_strict()`. **If one exists, say so plainly — it is the only
  path back to unfreezing v9 and it is the principal's call, not mine.**
- **Does the suspension actually suspend?** Check no clause elsewhere still relies on the eight-code
  set being in force, or on the withdrawn closure argument.
- **BS-3g still has no pinned schema, producer or verifier** (CODEX-V56 F2, HIGH, unrepaired). It is
  the slot authorised this morning, still not doing its job — say if V57 makes that worse.
- **Is the withdrawal complete?** No site should hold `UNREACHABLE-BY-CONSTRUCTION` anywhere in
  the draft or the ledger. Check both, not one.
- **Is the restated evidence bar actually sufficient?** It now demands varying every argument in
  the callable's documented surface. Is there a way to satisfy that literally and still be wrong —
  a dimension of reachability neither measurement nor a subsuming condition captures?
- **Is the Row L exemption narrow enough, and wide enough?** It names two objects. Is there a third
  signature the row mandates that the condition still catches — or does the exemption reach anything
  it should not?
- **Is `UNREACHABLE-BY-CONSTRUCTION` safe?** Test the falsification clause: if a guard so marked
  fires, does the document actually terminate the run in a named outcome, or does it only say so?
- **Is the class rule actually a rule?** Test whether it would terminate a raise site nobody has
  enumerated, or whether it only appears general while relying on the sites §5 names.
- **Is the caller-error boundary right in both directions?** Too wide and it swallows input
  validation; too narrow and real failures stay unterminated. Try to find a raise site the test
  classifies wrongly.
- **Can the new code go unreachable**, as its predecessor did at V44? The precedence clause is meant
  to prevent that; check it does.
- **Is the closed-enumeration argument in §5 sound?** It rests on Row R's default-forbidden clause
  and on §2.7(c) disposing of a per-object non-finite output as an exclusion. If either premise
  fails, the deletion's justification fails with it.
- **Is the V43 rerun deletion complete?** The five-step allowance is gone; check no clause elsewhere
  still assumes a rerun exists.
- **Does any other row still describe a ruled question as open?** F2 was stale for three hours
  because a ruling landed and the row was not re-derived. Look for others.
- **Is the V42 citation correction right?** `KIMI-V11 F7` is asserted to support the Stage-P claim.
  Check it against the report rather than taking my word.
- **The §5 VOID split from V40 still stands unreviewed in part.** Verify the misconduct conditions
  (`forbidden acts`, `protocol/digest deviation`) remain at `Any` everywhere in the prose — a quiet
  narrowing there would be unauthorised.
- **Class counts moved 15/8 → 16/8 at V37.** Check nothing still assumes the old inventory.

## Carry the absence-clause lens

**A narrow pattern is safe for presence and dangerous for absence.** For each universal negative
("no X can…", "nothing may…", "cannot create"), ask what construct would make it false and whether
the document *enforces* the exclusion or merely asserts it. That lens has produced a real finding in
every round it has been used.

## REQUIRED REPORT FORMAT

Write to `gates/V62_WHOLE_REVIEW_<SEAT>.md`, `<SEAT>` being `GPT56` or `CODEX`. End with exactly:

    <!-- FINDINGS-BLOCK v1 -->
    SEAT: <GPT56|CODEX>
    VERSION: V62
    VERDICT: <CLEAR|NOT CLEAR>
    COUNT: <n>
    F1 | <HIGH|MEDIUM|LOW> | <REPAIR-REQUIRED|ADVISORY|HELD> | <§ and line> | <one-line summary>
    <!-- END FINDINGS-BLOCK -->

The marker must start at **column 0**. Number findings contiguously from 1; `COUNT` equals the number
of `F` lines; `COUNT: 0` and no `F` lines if you find nothing. A confirmation of a previous repair is
`HELD`, **not** a finding — do not number it.

**A verdict of CLEAR means the text is a correct preregistration that is honest about being an
unfinished programme.** It does not mean the study may proceed. BS-6 and the first image byte remain
blocked; BS-2a stays DESIGN, UNFILLED.

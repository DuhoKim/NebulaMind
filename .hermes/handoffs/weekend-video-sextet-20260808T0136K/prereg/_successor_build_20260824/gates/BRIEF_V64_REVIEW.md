# BRIEF — V64 whole-document referee round

**Subject:** `PREREG_SUCCESSOR_DRAFT_V64_20260829.md`
**sha256 `af171440cd2d31c6b247f784c19f3ecc0d10647dd25eb5fbd93399565c688bbe`**
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

**On V64 the lint exits 0 — 97 advisory findings, 0 blocking.** The 96 are citations whose reports
predate the block format. **Under the principal's option D ruling that is their permanent answer, not
outstanding work.** Do not report them as unresolved.

Other checkers on V64: counts **16 class P / 8 class E** prose-matched; `prereg_trace` 63 transitions,
0 problems; `void_registry` self-test 6 controls, 0 failures.

## What V64 changed — a reversed ruling, a new covenant clause, and six of your own findings

**V63 was NOT CLEAR ×2 and its headline finding is NOT repaired here.** Both of you broke the
VOID/numerical **partition** on the same case — BS-2f/BS-8f/BS-5f are produced by the run **and then
sealed and verified**, so provenance does not partition anything. **It failed the falsification test
the draft carries at the principal's instruction.** Three constructions have now failed on this one
defect (precedence twice, provenance once), so a fourth is with the principal rather than attempted
here. **Do not spend the round re-deriving it; report only if you find something new about it.**

**1. THE REFUSAL VOCABULARY IS NO LONGER CLOSED, and the catch-all is taken** (principal, 22:18,
formally reversing the no-catch-all decision of 19:52). Your VOCAB-R1 round is why: **two independent
closure derivations, both broken within an hour of being written.** The set is now **eleven codes**
including `REFUSED-UNCLASSIFIED`, which carries a code and nothing else, under a guard making **every
emission a defect enumerated at freeze rather than a routine outcome.** `REFUSED-SCHEMA-NONCONFORMING`
**comes back** — its deletion rested on `receipt_strict()` covering the fact, and V62 scoped
`receipt_strict()` to slot receipts only, so my own repair removed the basis for the deletion.
**`tools/refusal_vocabulary_check.py` is rewritten**, its fingerprint control **inverted** — pinning a
derivation fingerprint is now a FAILURE, because there is no closure claim left to protect.

**2. A REQUEST LIFECYCLE CLAUSE — new normative machinery in §6.1**, repairing CODEX-VOCAB F1 and
GPT56-VOCAB F1. Permission is decided **durably before any transfer work**; writes get a
`PENDING-SURFACE-CHECK` state because conformance cannot be judged before the payload is decoded; every
state has **one terminal treatment** so no request ends undecided or unlogged; the log boundary sits at
the verdict. **Nothing is added to what the access log records** — that was not authorised.

**3. Your V63 findings, repaired.** **F2 (GPT56):** L986 is `MOVE_CAP`, an internal cap firing after a
feasible prefix exists, so calling it a caller error violated §5's own boundary — it is dispositioned
`PLANNING-INTERNAL`, explicitly **not** an outcome class, which corrects a premise of the ruling rather
than the ruling. **F4 (GPT56):** BS-3g's entry lives in the **successor layer's** schema because frozen
v9 cannot gain one, and the producer is bound to `receipt_strict()`. **F5 (GPT56), F2 and F3 (CODEX):**
four draw-set gaps — `n_draws` and `draw_master_seed` are **frozen in the preregistration**, so
pre-commitment is witnessed by the freeze rather than asserted by the receipt it constrains; the draw ×
perturbation matrix gets canonical addressing and a stated serialization; the categorical worst case is
**`HELD` iff every cell equals `baseline_verdict`**, avoiding an invented ordering over outcome names;
and encodings are bounded. **F4 (CODEX):** `require_complete_sample()`'s limit is recorded — it compares
two caller-supplied integers and verifies no parent-to-receipt partition.

## Known and parked — do not spend the round re-deriving these

- **The VOID/numerical partition** (GPT56-V63 F1, CODEX-V63 F1). Broken by both of you, **referred to
  the principal**, three constructions failed.
- **`REFUSED-OUTSIDE-STATED-SURFACE` + logged object identity still publishes membership**
  (GPT56-VOCAB F4, CODEX-VOCAB F4). **Confirmed and unrepaired**: the channel is the identity field,
  and changing what the log records is **not authorised**. It is bound up with the χ-adaptive access
  leak now with the principal (`OPEN_QUESTION_CHI_ADAPTIVE_ACCESS_LEAK.md`).
- **`REFUSED-INTEGRITY-MISMATCH`** — flagged, unresolved, with the principal: indistinguishable from
  tampering at emission and colliding with the phase-Any digest-deviation VOID antecedent.
- **The BS-3g lifecycle cycle** (GPT56-V63 F3): pre-BS-6 verification needing the later P3 mask and P4
  calibration. **Unrepaired and referred** — it decides whether the control gates BS-6 at all.
- **A tension I recorded rather than resolved:** a verifier timeout is foreseeable, and routing a
  foreseeable class into a category defined as a defect is in tension with itself. Flagged for the
  principal; **say so if you think it is worse than a tension.**

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
- **BREAK THE REQUEST LIFECYCLE. This is the highest-value attack in this round.** It claims every
  request ends in exactly one state with one terminal treatment, and that no request can end undecided
  or unlogged. **Construct one that does** — a failure between states, a write whose surface check
  cannot complete, a crash exactly at the log boundary, a request that is in two states at once.
  **CODEX: this is the repair you named; try to break your own prescription.**
- **Does the catch-all guard actually bind, or is it a wish?** The claim is that freeze-time
  enumeration keeps `REFUSED-UNCLASSIFIED` from becoming routine. **Find the path where it becomes
  routine anyway** — a class of refusal that lands there every run and passes the enumeration because
  it is always the same one.
- **Is the eleven-code set still leaking?** You both found that `REFUSED-OUTSIDE-STATED-SURFACE` plus
  the logged object identity still publishes membership. **That is NOT repaired here** — see the
  parked list. If you find a *different* leak, that is new.
- **Can the frozen-seed pre-commitment be defeated?** `n_draws` and `draw_master_seed` are frozen in
  the document and the verifier refuses unless the receipt matches. **Find the way to still choose
  favourably** — a generator whose id admits a family, a manifest reorder, anything that varies the
  draws while the frozen values stay put.
- **BREAK THE PARTITION — only if you have something new.** Already broken and referred; see above. §5 claims every
  post-unblinding failure is owned by exactly one clause and resolvable **without precedence**.
  Construct a counterexample: a post-unblinding failure that is genuinely ambiguous, or one both
  clauses claim, or one neither claims. **If you need the precedence rule to decide any case, the
  repair has not landed and the draft says so itself.** Attack the exhaustiveness ("every failing
  quantity was either verified before or computed by the run") and the exclusivity separately.
- **Does the narrowing of `VOID` let a real deviation be reported as arithmetic?** VOID now covers a
  post-unblinding non-finite only when it shows a pinned/sealed/verified object wrong. Try to build a
  protocol breach that presents as an ordinary failed computation. The draft's answer is that
  forbidden acts and protocol/digest deviation remain `Any` phase and catch it independently — test
  that answer rather than accept it.
- **Is any of L963, L973 or L986 reachable during a run?** The ruling was about planning failures, not
  about those three line numbers. **If you find a run-time path, say so plainly — that goes straight
  back to the principal**, and the draft commits to that.
- **Can the draw set be satisfied and still not bound the gate?** Construct a BS-3g receipt that
  passes all four draw fields and the verifier's clause (e) while reporting something that is not the
  worst of the draws — or that fixes `n_draws` after seeing a verdict.
- **Does any text still admit measurement-only promotion?** Basis (i) is dropped in §5; check §11, §7
  and the ledger for language that still lets a count promote a guard.
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

Write to `gates/V64_WHOLE_REVIEW_<SEAT>.md`, `<SEAT>` being `GPT56` or `CODEX`. End with exactly:

    <!-- FINDINGS-BLOCK v1 -->
    SEAT: <GPT56|CODEX>
    VERSION: V64
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

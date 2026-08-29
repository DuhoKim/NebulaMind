# BRIEF — V68 whole-document referee round

**Subject:** `PREREG_SUCCESSOR_DRAFT_V68_20260829.md`
**sha256 `010f5ece044e67a1928f2182f8df29dc1c68cb1b96f085cac332b7f376cec9a7`**
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

**On V68 the lint exits 0 — 97 advisory findings, 0 blocking.** The 96 are citations whose reports
predate the block format. **Under the principal's option D ruling that is their permanent answer, not
outstanding work.** Do not report them as unresolved.

Other checkers on V68: counts **16 class P / 8 class E** prose-matched; `prereg_trace` 67 transitions,
0 problems; `void_registry` self-test 6 controls, 0 failures.

## What V68 changed — the ordering is abandoned for atomicity, and your seven pairs are answered

**V67 was NOT CLEAR ×2** (GPT56 7, CODEX 8) with the tightest convergence of the night — seven topics
paired one-for-one. **The largest repair concedes your point rather than arguing with it.**

**1. THREE ORDERINGS HAVE FAILED AND THE THIRD FAILURE IS STRUCTURAL** (your F1 pair). You showed that
for a **read**, resolving IS the touch — so V67's crash-before-append left a completed sealed-store
read unlogged — and that for a **write**, staging cannot establish the later commit. **One event, two
fallible operations: no ordering of two fallible operations can make one always-true about the other.**
The repair is not a fourth ordering. **The ATOMIC TOUCH CONTRACT** is a named BS-2k design obligation:
the stores and the access-log chain share **one transactional commit domain**, and a touch — store
effect, its one event, Row B's identifier-binding — **commits entirely or not at all**. This also
answers your F2 pair: recovery consults **committed bindings**, so one request is never re-decided and
a legal retry is never suppressed. Still exactly one event per touch; nothing new enters the log; the
pre-verdict residue stays referred.

**2. The enumeration verifier gets its OBJECT** (your F3 pair): an **ENUMERATION ENTRY** —
`chain_position` · `event_digest` · computed `class_key` · one-token `disposition` ·
`explanation_ref` · signature — joined by `(chain_position, event_digest)`, living in the
lock-checkpoint materials under Row B's existing duty, wired into §5's BS-L guard at issuance and a
**fresh pass at opening**, with the `gates/enumeration_verifier.py` build item in §11. **And the limit
of the lint is stated in the draft and in the checker's own docstring: a lint verifies that text
states a mechanism, never that it exists.**

**3. The class key is COMPUTED, not assigned** (your F4 pair): `(row, operation, lifecycle state)` —
fields the event already carries — so **relabelling cannot split a class**, and the verifier refuses a
second `EXPLAINED` for the same key.

**4. `delta_gamma_max` enters the schema** (eighteen fields) **and the verifier executes every
manifest constraint the prose stated** (your F5/F6): both endpoints, three distinct values, adjacent
gap ≤ the frozen Δγ, field equality.

**5. Only `HELD` discharges** (CODEX F5): a verifier-valid `FAILED` receipt is a **true record that
BLOCKS** and goes to the principal; `NOT-EVALUATED` discharges nothing; verifier clause (f) evaluates
discharge separately from validity.

**6. The stratum-producer gap is FILED, not built** (your F6/F7): no covenant row produces the index,
closing it changes what the study permits, so `OPEN_QUESTION_STRATUM_PRODUCER.md` carries the options
and costs, **coupled to the strata decision**. **And the bin/allocation separation gets a predicate**:
BS-2f's verifier recomputes boundaries from the full sealed accepted positions and **refuses
inequality** — verification, not typing, because v9 is frozen. You executed `calibration_bins()` on
stratum indices; under the predicate, boundaries built that way cannot equal the full-set
recomputation and are refused.

**7. The two freeze-time stragglers are corrected** (your F7/F8).

## Known and parked — do not spend the round re-deriving these

- **CODEX-V64 F2 — the four availability codes describe the logged object.** **Confirmed, unrepaired,
  and with the principal**: they are part of the vocabulary he ruled at 22:18, and changing them is
  his. **Say so if you think it is worse than recorded, but do not re-derive it.**
- **The durable pre-verdict state** (GPT56-V66 F1) — needs a second event class; changing what the
  log records is not authorised. **Referred, and re-finding it does not move it.**
- **The strata AND their producer** — `FINDING_ROW_F_STRATA.md` + `OPEN_QUESTION_STRATUM_PRODUCER.md`, **with the principal, coupled**. Row F's surface is ruled and applied; the strata decision and the producer row/surface decision are open together. **Do not re-derive; report only if the analysis is wrong.**
  Established: **both stratum axes are χ-derived**, so there is no χ-free version of the inherited
  stratification, and `N_HC_STRATA = 9` is a frozen constant in v9. **Do not re-derive; report only if
  you find the analysis wrong.**

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
- **BREAK THE ATOMIC TOUCH CONTRACT. Highest value in this round.** It claims a touch commits
  entirely or not at all across three effects — store, event, binding. **Attack the commit domain's
  edges**: a read whose bytes reach the requester outside the domain, a write acknowledged before its
  commit, recovery replaying a committed touch, the contract being unimplementable for the
  predecessor archive Row B also mediates. **The stated residue is the invisible pre-commit death;
  anything worse is a finding.**
- **Defeat the enumeration entry.** Forge the join, smuggle free text through `explanation_ref`,
  discharge a key with two `EXPLAINED` entries under two different digests, or find an emission the
  chain recompute cannot see.
- **Split a class anyway.** The key is `(row, operation, lifecycle state)`. **Can a caller vary its
  requests so one defect presents as many keys?** If yes, say whether that is a real evasion or the
  honest grain of the data.
- **Evade the manifest constraints as now executed.** Endpoints, three values, spacing, field
  equality — construct a conforming manifest that still dodges the invariance question.
- **Test the discharge split.** Find the path where a `FAILED` or `NOT-EVALUATED` receipt still
  advances anything.
- **Test the recomputation predicate.** Can boundaries built from a stratum-contaminated input equal
  the full-set recomputation without being harmless? The claim: the event always
  carries a true outcome, nothing is delivered unlogged, and one request never produces two events.
  **Find the counterexample** — a write whose staging is itself the commit, a read whose resolution
  cannot be held, a recovery that re-resolves and appends twice. **The stated residue is that a
  crash between append and release over-reports a touch; anything WORSE than that is a finding.**
- **Defeat the enumeration verifier.** It recomputes emissions from the chain and is consulted at
  `BS-L` and at the opening. **Find the catch-all event that reaches unblinding anyway** — appended
  between the two consultations, or invisible to a recompute, or discharged by an entry that says
  nothing.
- **Defeat the recurrence rule.** Explanation no longer discharges a recurring class. **Find the way
  to keep a class routine anyway** — by re-labelling it each time so it never "recurs", or by keeping
  each instance formally distinct.
- **Attack the manifest's honesty, not its coverage.** The draft says `HELD` is bounded by grid
  resolution and refutation is decisive. **Check that every other place the invariance outcome is
  used respects that asymmetry** — a downstream reader treating `HELD` as proof would defeat the
  statement.
- **Is Row F now coherent?** Its surface admits a χ-bearing input and its void clause forbids one
  reaching **bin construction**. **Find the path by which the stratum index reaches
  `calibration_bins()`**, or by which the widened surface admits more than the allocation needs. The claim: under append-before-release, no
  request is both undecided and delivered, and none is decided twice. **Find the counterexample** — a
  partial release, a write committed before its append, a retry that produces two events for one
  touch, a lease handover that appends twice. **The stated residue is that a crash between decide and
  append is indistinguishable from a request that never arrived; anything WORSE than that is a
  finding.**
- **Is the blocking invariant actually blocking?** `BS-L` and the lock opening are blocked by an
  unenumerated `REFUSED-UNCLASSIFIED`. **Find the path to unblinding with one outstanding** — a
  refusal that never reaches the chain, an enumeration that can be satisfied vacuously, a gate that
  does not consult it.
- **Can BS-3g still be emitted?** Three separate blockers now claim to prevent it — unset `n_draws`,
  unset `draw_master_seed`, empty `draw_generator_id` set. **Find the emission path that survives all
  three**, or show one of them is not actually enforced.
- **Does the manifest rule bind?** It must span `±gamma_bound` with three distinct values. **Construct
  a conforming manifest that still evades the invariance question.**
- **BREAK THE REQUEST LIFECYCLE more broadly**, beyond atomicity. It claims every
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

Write to `gates/V68_WHOLE_REVIEW_<SEAT>.md`, `<SEAT>` being `GPT56` or `CODEX`. End with exactly:

    <!-- FINDINGS-BLOCK v1 -->
    SEAT: <GPT56|CODEX>
    VERSION: V68
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

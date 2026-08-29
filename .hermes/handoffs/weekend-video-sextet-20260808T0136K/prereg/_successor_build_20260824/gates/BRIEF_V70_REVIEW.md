# BRIEF — V70 whole-document referee round

**Subject:** `PREREG_SUCCESSOR_DRAFT_V70_20260830.md`
**sha256 `a1deae2e44b51a7305f7eb7b3b18ab4d6ff180cfc7379c69e6fafe0304b3e89a`**
**Companion, in scope: `LIFECYCLE_GUARANTEE_SPEC.md`** — the lifecycle's invariants now live there and the draft is derived from it.
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

**On V70 the lint exits 0 — 97 advisory findings, 0 blocking.** The 96 are citations whose reports
predate the block format. **Under the principal's option D ruling that is their permanent answer, not
outstanding work.** Do not report them as unresolved.

Other checkers on V70: counts **16 class P / 8 class E** prose-matched; `prereg_trace` 69 transitions,
0 problems; `void_registry` self-test 6 controls, 0 failures.

## What V70 changed — the three-failure threshold fired, and the lifecycle got a spec

**V69 was NOT CLEAR ×2** (GPT56 6, CODEX 7), and its F1/F2 pair made the lifecycle **three
consecutive rounds failing on one object** — this lane's stop-patching threshold, the same rule that
retired the citation check. **So there is no fourth patch. `LIFECYCLE_GUARANTEE_SPEC.md` states the
guarantee as invariants** — G1–G5, N1–N3, a five-crash-window × four-reader table — **and the draft's
lifecycle text is now DERIVED from it; a conflict between them is a defect in the draft.**

- **Your F1 pair** (TRANSFER declared after its deletion — a deletion that did not delete): the state
  machine now has **one home**, the spec's §4, and the draft **quotes** it. No `TRANSFER` state.
- **Your F2 pair** (Row G's *any-unlogged-view* vs unlogged re-views): **the spec's §5 argues the
  fork DISSOLVES** — the covenant had already decided, because Row G's clause always required logged
  views; V69's carve-out was right for machine conveyance and **over-broad in covering renders**.
  New invariant **G5: every render is its own touch with its own committed event.** The V65 re-view
  sentence is recut — unrestricted in **schedule** terms, logged in **custody** terms — and the
  buffer is governed: **no reuse for renders; conveyance buffers destroyed on completion, bounds a
  BS-2k requirement.** **If you think the fork survives G5, that is the highest-value finding
  available in this round.**
- **Your F3/F4 pair**: the entry schema gains the two **disposition-conditional fields** the prose
  demanded (`rederivation_digest` under `NAMED-AS-DEFECT`, `explanation_ref` under `EXPLAINED`), the
  signed explanation must itself **name the `(chain_position, event_digest)` it explains**, and the
  stale lifecycle-state wording in the blocking invariant is corrected.
- **GPT56 F4 / CODEX F3**: post-`BS-L` entries live in an **authenticated continuation segment**
  outside the sealed checkpoint materials (independently authenticated by signature + chain join),
  and the post-opening window is closed by name: **BS-7f, BS-V and disclosure each require a fresh
  enumeration pass** — a catch-all during opening blocks at BS-7f, not never.
- **GPT56 F5**: the key is the **trigger** granularity, not the naming granularity — the
  re-derivation names what it **finds** by reading the joined emissions, one class or several.
- **CODEX F5**: the manifest must contain `γ = 0` and the verifier **recomputes `baseline_verdict`**
  by replaying that column — a producer-chosen baseline was `require_authorization`'s shape at the
  reference point.
- **Your F6 pair**: `gamma_bound`'s guarantee is stated **at its second recurrence** — `|γ̂| + k·σ`
  is a sampling-error bound under three named conditions (linear model, unbiased estimator, honest
  σ), NOT a bound under violation of any, `HELD` is conditional and says so, **and the shape choice
  (measurement-derived vs a-priori) is with the principal.**
- **CODEX F7**: the ledger generator's header is fixed and regenerated.

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
- **BREAK THE SPEC. Highest value in this round.** Read `LIFECYCLE_GUARANTEE_SPEC.md` as the
  object under review. **Find a failure that lands in no cell of its window × reader table, a reader
  it forgot, or a touch kind that is neither conveyance, render nor write.** A corner already covered
  by a G or an N is not a finding.
- **Attack G5's dissolution of the Row G fork.** The spec claims no normative choice was needed
  because Row G's clause already required logged views. **If the fork survives — if some permitted
  re-view practice cannot be a fresh touch commit — say so plainly; that returns it to the principal
  as the open question the spec says it would be.**
- **Attack the continuation segment.** Post-`BS-L` entries authenticate independently by signature +
  chain join. Forge one, orphan one, or find the verifier unable to distinguish continuation entries
  from checkpoint entries where it matters.
- **Attack the conditional `HELD`.** Its three named conditions — can a receipt satisfy every
  verifier clause while a condition is violated in a way the text claims is detectable? G1–G4 and N1–N2
  claim to partition every failure. **Find a failure that is neither guaranteed against nor named as
  a non-guarantee** — that would show the guarantee itself is incomplete, which is the only defect
  left that a new corner-case can reveal. A corner already covered by G or N is not a finding.
- **Attack N1's edge.** Delivery is outside the custody claim — but Row G's interface renders bytes
  to a human. **Is a rendered view "delivery" or a store touch?** If the committed buffer outlives
  its delivery, who holds it and under what surface?
- **Defeat the disposition bindings.** Mint a re-derivation digest that names nothing, resolve an
  `explanation_ref` to an artifact that explains a different emission, or find the dangling-ref check
  unable to see across the checkpoint boundary.
- **Test the coarsened key.** `(row, operation)` merges more — **does it merge too much?** If two
  genuinely distinct defects share a key, the recurrence rule forces a re-derivation naming what,
  exactly?
- **Test `k_gamma`'s rule.** The bound is `|γ̂| + k·σ` — construct the case where that formula is the
  wrong shape (σ underestimated, γ̂ biased toward zero) and say whether the formula or only the value
  is at fault. It claims a touch commits
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

Write to `gates/V70_WHOLE_REVIEW_<SEAT>.md`, `<SEAT>` being `GPT56` or `CODEX`. End with exactly:

    <!-- FINDINGS-BLOCK v1 -->
    SEAT: <GPT56|CODEX>
    VERSION: V70
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

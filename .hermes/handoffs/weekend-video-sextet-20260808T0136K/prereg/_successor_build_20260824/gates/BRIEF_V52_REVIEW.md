# BRIEF — V52 whole-document referee round

**Subject:** `PREREG_SUCCESSOR_DRAFT_V52_20260829.md`
**sha256 `a825e5d2045721c44703558156f0532e9d09dc22ca0f9e08fa5031b6831dd2e4`**
Verify this digest before reading. If it does not match, stop and report the mismatch.

**Last refereed draft: V49** `d8a9501e0653dd84` — **NOT CLEAR from both seats**, 15:47 (GPT56 7,
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

**On V52 the lint exits 0 — 96 advisory findings, 0 blocking.** The 96 are citations whose reports
predate the block format. **Under the principal's option D ruling that is their permanent answer, not
outstanding work.** Do not report them as unresolved.

Other checkers on V52: counts **16 class P / 8 class E** prose-matched; `prereg_trace` 51 transitions,
0 problems; `void_registry` self-test 6 controls, 0 failures.

## What V50, V51 and V52 changed — eight of the ten V49 findings

**V50** `e3d0d65cca545040` — six findings, all corrections to my own text.
- **GPT56-V49 F2 / CODEX-V49 F3 (both seats, HIGH).** The class rule and the §5 VOID clause **both
  claimed post-unblinding non-finite/degenerate failures**; the precedence list named only the three
  INCONCLUSIVE codes. **The VOID antecedents are now named in it and the rule never fires where one
  applies** — without that, a literal reading converted voiding conditions into inconclusive halts.
- **GPT56-V49 F4.** The raise inventory was recounted **by AST**: 112 nodes, including **39
  `ManifestClosureError` sites the grep never saw** because it keyed on `RuntimeError|ValueError`.
- **CODEX-V49 F3.** The 31–79 figure is restated as an **unsubtracted candidate partition**.
- **GPT56-V49 F3.** The false §2.7(c) route, still asserted beside its own retraction, removed.
- **CODEX-V49 F2.** §11 classification now attaches to **failure paths and call sites**, not raise
  statements, since a helper may raise on behalf of a caller.

**V51** `e007e9cb940de135` — **GPT56-V49 F6**, §2.1's *"nothing else changes with the branch"*
qualified to Branch B (recovered from the V11 commit, which says Branch A *"is a new preregistration
in everything but name"*); **GPT56-V49 F7**, the predecessor memo's provenance — it was **amended by
append after signing**, so both digests and the reason are now recorded.

**V52** `a825e5d2045721c4` — two principal rulings.
- **CODEX-V49 F1 / CODEX-V24 F1 — carried open twenty-five drafts, now closed.** Row L's
  wrong-signature VOID condition exempts **exactly the two signatures the row itself mandates that it
  caught: the freeze signature (P0) and the canonical opening authorization (P7).** The BS-L detached
  signature is *over* the canonical lock digest and was never caught. **The exemption is by named
  object, not by category.** The row records that this makes the signing path **executable, not
  verified**.
- **GPT56-V49 F5 — a third status.** `UNREACHABLE-BY-CONSTRUCTION`, promoted only by **named per-site
  evidence**: an execution count over a stated harness, a structural subsumption argument, or both.
  **If a guard so marked ever fires, the classification is falsified, not the run** — the default rule
  still terminates it and the record is corrected. The status is a claim about the record, never about
  routing.

**Supporting artifact:** `ref/RAISE_SITE_CLASSIFICATION.md` — all 112 raise sites, one row each,
regenerable by `ref/gen_raise_classification.py`. **Numerical class 22**, or 18 if the four flagged
domain checks read as caller errors. Check rows, not the count.

## Known and parked — do not spend the round re-deriving these

- **GPT56-V49 F1, the access log's unconstrained refusal reasons.** Confirmed, and a closed
  eight-code vocabulary is **drafted and with the principal**
  (`PROPOSAL_ACCESS_LOG_REFUSAL_VOCABULARY.md`). **No draft text has been changed for it.** Report it
  only if the drafted set is itself wrong.
- **The γ → sign-vector mapping** (`OPEN_QUESTION_GAIN_SIGN_MAPPING.md`), open with the principal.
- **`require_authorization`**, deprioritised; its limit is recorded and deliberately unrepaired.

## Attack these specifically

- **Did V41's `BS-3g` additions actually make the edge receiptable**, or only appear to? The §11 item
  is named and not specified — say if that is insufficient.
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

Write to `gates/V52_WHOLE_REVIEW_<SEAT>.md`, `<SEAT>` being `GPT56` or `CODEX`. End with exactly:

    <!-- FINDINGS-BLOCK v1 -->
    SEAT: <GPT56|CODEX>
    VERSION: V52
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

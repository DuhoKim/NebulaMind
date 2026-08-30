# V116 whole-document adversarial referee — CODEX

## Verdict

**NOT CLEAR.** The mandated V116 digest matched before the draft was read. The new successor-order predicate and exact close-class domains hold on their stated surfaces, but three defects remain. First, V115's T1 contradiction survives verbatim in the live §11 implementation contract despite being repaired in the companion spec. Second, the count-oracle closure is still only a slot-side assertion: no named or pinned harness implements the asserted pre-`_plan` guard, the frozen production call still accepts null proofs, and neither the receipt nor the prose binds the proof objects to the current release or to the values actually passed into planning. Third, the new form-schema echo never checks the kind half of its advertised kind→tuple mapping and accepts a drifted live declaration whenever another occurrence preserves the tuple. All three are debt-ineligible: the first two can change lifecycle/selection validity, and the third governs the signed/exported closing bodies the freeze is supposed to authenticate.

## Subject identity and referenced-byte checks

- Required draft sha256, recomputed before reading: `315162bd158b0f608503f26c96e48dd568c26cb90343bd23442f5e371d8fc886` — exact match.
- `LIFECYCLE_GUARANTEE_SPEC.md`: `e087d932673a81b029e2ff42adb0394394f708230172fdde5ce2d4b464efa06a`, matching the draft's lifecycle pin.
- `ref/successor_ref_v9.py`: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, matching §0 and `ref/RAISE_SITE_CLASSIFICATION.md`.
- `tools/refusal_vocabulary_check.py`: `8157913b2addb8ccdd0bf843cc921af6c912a107c713ab889c4f343a65a73384`, matching draft line 622.
- The raise ledger's 113 rows exactly cover 112 AST `Raise` nodes plus the production assert; class totals are 32 CALLER, 56 INTEGRITY, 18 NUMERICAL, 3 PLANNING-INTERNAL, 1 TYPED-OUTCOME, and 3 WRAPPER. I did not re-score the already-referred per-raise/per-call-site unit defect.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — the decoded-frame/T1 contradiction survives in §11

The companion spec now gives the V115 counterexample the correct status. T1's subject remains universal: any fully decoded frame in Row B's hands must complete its arrival commit before drain-start (`LIFECYCLE_GUARANTEE_SPEC.md` line 131). The repaired pass-entry analysis then says expressly that a termination unit landing after the writer violates that obligation **"VIOLATES T1'S DECODED-FRAME CLAUSE"** even though the frame never became a request and the externally visible consequence is bounded as W0 residue (spec line 149).

The draft's label-bound T1 quote preserves that subject (draft line 639), but the code-side implementation contract still states the opposite. Draft line 1564 says that the same no-decoded-frame obligation violation under a mid-hold termination costs one would-be request as W0 residue, **"never a T1 contradiction or malformed history."** The lifecycle derivation checker remains green because it checks the labelled invariant quotes, not this unlabelled §11 implementation text. Thus one execution is still classified both as a T1 violation by the normative spec and as never a T1 contradiction by the implementation contract that is supposed to build its verifier/harness.

Required repair: remove the surviving "never a T1 contradiction" sentence from §11 and derive the implementation item from the spec's repaired wording: chain-undetectable but T1/BS-2k-violative, testimony-plus-fixture, with only the W0 consequence bounded.

**Debt eligibility: DEBT-INELIGIBLE.** T1 controls termination ordering and pass-entry legality. Freezing contradictory normative and implementation semantics would leave the gate unable to say whether the named boundary/termination execution conforms. An appendix can disclose the contradiction but cannot choose which live contract the implementation must obey.

### F2 — HIGH — REPAIR-REQUIRED — the count-oracle closure has neither a bound harness nor current-release/input identity

Draft §2.3 line 179 says the closure lives at BS-2c: the receipt requires three non-null proof objects, "carries their digests," and a production harness refuses `None` before `_plan`. The §7 BS-2c row at line 915 repeats only "slot-side non-null contract." No harness is named or pinned, and §11 contains no BS-2c/build-plan implementation item specifying this wrapper, its identity, or its fixture. A repository-wide search found the asserted production-path fixture only as prose, not as executable code.

The frozen normative bytes do not supply the missing guard:

- `SLOT_SCHEMA['BS-2c']` has the six fields `universe_brickid`, `brickid`, `n_eligible`, `c_bytes`, `grouped_sum`, and `ungrouped_total` (v9 lines 185–186).
- `receipt()` checks field names and truthiness, then returns only aggregate body/envelope digests; it neither calls planning nor proves that the receipted values are the values planning consumed (v9 lines 208–224).
- `validate_count_table()` performs universe equality only when `universe_brickid is not None` and grouped/ungrouped closure only when `grouped_sum is not None` (v9 lines 847–893).
- `build_plan()` forwards all three proof arguments directly to `_plan` (v9 lines 1291–1312). In a read-only monkeypatch that replaced `_plan` with a recorder, `build_plan(... universe_brickid=None, grouped_sum=None, ungrouped_total=None)` reached `_plan` with all three values still null.

There is a second, independent hole in the same asserted closure. Non-nullness and self-consistency do not establish freshness or release identity. Executing `validate_count_table()` with a self-consistent one-brick foreign/stale universe and `grouped_sum = ungrouped_total = 832393` returned success. The draft says the proof objects' digests are carried, but states no equality between the BS-2c universe/proof preimages and the current BS-1/BS-1b release witness (or the externally pinned universe used elsewhere), and states no atomic binding between those preimages and the exact arguments consumed by `build_plan()`. A producer can therefore receipt one complete proof set and plan with another, or provide a stale self-consistent set, while satisfying the written field/non-null surface.

Required repair: add a named, pinned BS-2c production harness/verifier item. It must reject nulls before dispatch; construct the receipt from the exact argument buffers passed to `build_plan()` in one bound invocation; recompute rather than accept the proof digests; and compare the universe/release witness against the current BS-1/BS-1b branch identity and its pinned manifest. The promised None, missing/extra, grouped-disagreement, stale-universe, and receipt-vs-plan substitution fixtures must execute that shipped harness.

**Debt eligibility: DEBT-INELIGIBLE.** This is the selection chain's completeness root. A stale, null, or receipt/plan-substituted proof set can change the selected footprint and every downstream statistic while leaving a canonical BS-2c envelope. The freeze cannot survive that ambiguity merely by listing it as known debt.

### F3 — MEDIUM — REPAIR-REQUIRED — FORM-SCHEMA ECHO ignores kind identity and accepts a surviving duplicate

The live §11 contract says `FORM_SCHEMAS` maps one kind literal to one exact ordered field set and that the producer selects by the chain-derived kind (draft line 1564). The generator declares those four triples at `ref/gen_string_field_registry.py` lines 507–521. But its actual echo at lines 759–768 loops over `(_kind, _fields, _home)`, constructs only the tuple string, and checks only whether that tuple appears at least once in the home corpus. `_kind` is never compared to any document bytes or associated with the tuple occurrence.

Two direct in-memory attacks stayed green:

1. Changing only the first mapping key from `successor-export` to `successor-export-RENAMED` produced no `form-schema` problem. Swapping the two export kind labels also produced none.
2. The post-lock tuple occurs twice in the draft (lines 670 and 1564), and the pre-lock tuple occurs twice (lines 641 and 670). Corrupting one live declaration leaves a second exact tuple, so `count < 1` remains false and the echo reports no drift. This is the brief's HISTORY/duplicate-shadow attack in the current bytes, not an invented document shape.

The advertised controls are absent as well: `_domain_echo_selftest()`'s docstring says "form-tuple drift," but its body at lines 555–579 tests only widening/deletion of the close-class domains. There is no form-kind rename, tuple deletion/addition, or cross-form-substitution seeded control.

Required repair: parse each canonical form declaration as a kind-qualified pair `(kind literal, exact ordered tuple)` from its normative labelled home; require exactly one authoritative match per form or explicitly compare every duplicated normative declaration; reject unknown/renamed/swapped kind literals; and add the deletion, addition, cross-form substitution, duplicate-shadow, and kind-rename controls the draft says exist.

**Debt eligibility: DEBT-INELIGIBLE.** These forms are the successor export and terminal-review bodies used by the completed/terminated closing ceremonies. A control that can silently detach kind from body cannot support a signed freeze or generated known-debt appendix. This is a control on an existing generator and is admissible under the scope freeze; it should be repaired rather than carried.

## Failed attacks and holdings

- **Successor-order repair held on its live predicate.** The five tokens form one ordered closed sequence; the first pass binds to BS-2f and each later pass must be the unique successor of its predecessor. A closed attempt leaves the same gate as next-undischarged, so a legitimate re-boundary retry remains legal; the disclosure reconciliation is the disclosure pass, not a sixth consultation.
- **Close-class repair held as written.** The current attempt-close domain is exactly `{ABORTED, ABORTED-BY-RESTART}` and verification-close is exactly `{ABORTED, EXPIRED, ABORTED-BY-RESTART}`. The shared extractor catches planted `STALLED` widening and `EXPIRED` deletion.
- **Request-key join held mechanically.** The contract checks key equality to arrival position, recomputes `request_digest`, rejects a terminal with no arrival, rejects two terminals for one key, and compares row/operation/object identity. The as-of-anchor rollback residue is disclosed rather than overclaimed.
- **Temporal partition held on the declared cuts.** The signed-checkpoint cut precedes the issuance commit; the partition cut is the commit end; issuance's own events are explicitly between them and continuation-bound. I found no enumerable refusal event orphaned in that interval under the one-atomic-commit premise.
- **Refusal vocabulary held its stated limited contract.** Live check: 0 problems; self-test: 43 controls, 0 failures. R02 is now honestly demoted to a finite literal-shape tripwire; I did not score a semantic paraphrase the tool explicitly disclaims.
- **Counts and trace held.** `prereg_counts.py` computed 16 class P / 9 class E with prose agreement. `prereg_trace.py --check` recomputed 115 transitions with 0 problems.
- **Lifecycle pin/labelled quote check held mechanically.** `lifecycle_derivation_check.py` returned 0 problems and its self-test returned 0 failures. F1 is precisely the unlabelled §11 blind spot, not a pin mismatch.
- **Main lint held on its declared surface.** `prereg_lint.py` exited 0 with 97 legacy advisories and 0 blocking findings.

## Evidence and write-scope ledger

Read before the subject: `gates/BRIEF_V116_REVIEW.md`. Then, after digest verification, read the exact V116 draft, `LIFECYCLE_GUARANTEE_SPEC.md`, `ref/RAISE_SITE_CLASSIFICATION.md`, `ref/successor_ref_v9.py`, `ref/gen_string_field_registry.py`, `tools/refusal_vocabulary_check.py`, the V115 referee reports, and the V115 repair dispositions. Read-only executions included sha256 recomputation; AST/ledger count comparison; prereg lint/count/trace; refusal live check/self-test; lifecycle derivation live check/self-test; void registry; direct count-validator probes; a monkeypatched build-plan dispatch recorder; and in-memory form-schema kind/duplicate mutations. No draft, spec, source, generator, registry, checker, or ledger was modified. This report is the only intended write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V116
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | spec T1 line 131 and §3d line 149; draft §6.1 line 639 and §11 line 1564 | The repaired spec says the decoded-frame interleaving violates T1 while the live §11 contract still says it is never a T1 contradiction
F2 | HIGH | REPAIR-REQUIRED | §2.3 line 179; §7 line 915; successor_ref_v9.py lines 185-224, 847-893, 1291-1312 | BS-2c has no bound harness or current-release/input identity, so null, stale, or receipt-plan-substituted proof objects can reach selection
F3 | MEDIUM | REPAIR-REQUIRED | §11 line 1564; ref/gen_string_field_registry.py lines 507-521, 555-579, 759-768 | FORM-SCHEMA ECHO ignores kind identity and accepts kind renames or a drifted declaration shadowed by a duplicate tuple
<!-- END FINDINGS-BLOCK -->
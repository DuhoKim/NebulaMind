# V116 WHOLE-DOCUMENT REVIEW — GPT56

## Verdict: NOT CLEAR

The pinned subject was verified before reading: `315162bd158b0f608503f26c96e48dd568c26cb90343bd23442f5e371d8fc886`. V116 does not close the count-oracle seam it says it closes. The frozen production function still forwards three explicit `None` values into `_plan`, the draft names an otherwise-unidentified harness as the thing that prevents that call, and §11 contains no build item for that harness. Even with all three objects non-null, the validator binds only the count table to the producer-supplied universe and the total to `PINNED_COUNT_TOTAL`; it does not bind the universe identities to the selected release. A two-brick counterfeit universe with the pinned total passes the actual frozen bytes. These are selection-defining failures and are debt-ineligible. I also broke the new FORM-SCHEMA ECHO as a claimed kind→schema check: the implementation never consults the kind while checking the corpus, so a renamed kind with an absent literal passes as long as the tuple appears anywhere. That checker defect is appendix-safe because the four current forms were manually matched in the pinned bytes and the defect is prospective control weakness, not ambiguity in the present four bodies.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §2.3 line 179, §7 line 915, §11 lines 1206–1572: the asserted pre-`_plan` non-null harness has no named artifact, pin, verifier, or build item

V116 says a production invocation with any of `universe_brickid`, `grouped_sum`, or `ungrouped_total` equal to `None` “REFUSES THE RECEIPT before `_plan` is reached” because “the harness wraps the call.” That protection is not in the pinned implementation. `successor_ref_v9.py:1291–1297` requires the keyword names but forwards their values unchanged to `_plan`; `_plan` calls the conditional validator at lines 1308–1312. Replacing `_plan` with an observation stub and invoking the real `build_plan(..., universe_brickid=None, grouped_sum=None, ungrouped_total=None)` returned all three `None` values at the `_plan` boundary:

```text
{'universe_brickid': None, 'grouped_sum': None, 'ungrouped_total': None,
 'l_plan_override': None, 'n_trials': 1}
```

The wrapper is not named by path or symbol in §2.3, the BS-2c row merely says “slot-side non-null contract,” and a search of the whole draft finds the explicit-None fixture only in line 179. Section 11 names required nonexistent artifacts when they are real obligations (`gates/replay_harness.py`, `gates/enumeration_verifier.py`, `gates/canonical_decoder.py`) but has no count-oracle harness item at all. BS-2c is also absent from §7 line 906’s closed list of DESIGN slots, so the document permits treating it as a value fill even though its claimed closure depends on new code that neither exists nor is required to be built.

Required repair: name the successor-layer production wrapper/harness as a required class-P build item; specify that the only production entry reaches v9 only after rejecting each `None`; pin it when built; bind BS-2c’s producer to it; and require a separately pinned verifier/fixture proving an explicit `None` cannot reach the real `_plan`.

**Debt eligibility: DEBT-INELIGIBLE.** This is not unfinished implementation already fenced by a correctly declared DESIGN slot. The text presently classifies BS-2c as fillable while its only claimed closure lives in unnamed, absent code. Freezing that contract would permit a self-consistent but incomplete count oracle to determine BS-2o, BS-5p, BS-2s, and the selected sample. It poisons selection integrity and therefore the freeze itself; an appendix cannot turn a missing class-P prerequisite into an enforceable prerequisite.

### F2 — HIGH / REPAIR-REQUIRED — §2.3 lines 177–184 and §7 line 915: non-null proof objects are not bound to the current release universe

The repair requires non-null proof objects and says their digests are carried, but it never states the equality that makes the universe proof about this release rather than any producer-chosen universe. In the frozen bytes, `validate_count_table()` checks:

- supplied `brickid` equals supplied `universe_brickid` (`successor_ref_v9.py:869–877`);
- supplied count sum equals supplied `grouped_sum` and `ungrouped_total` (`:878–889`); and
- `ungrouped_total == PINNED_COUNT_TOTAL` (`:890–892`).

It does not check a pinned release-universe digest, release identity, expected universe cardinality, or a binding to BS-1/BS-1b. This is a digest-of-own-inputs seam, not closure. Executing the exact pinned module with a fabricated two-brick universe and the frozen total passed:

```text
validate_count_table(
    [1, 2], [0.1, 0.2], [832393, 0],
    universe_brickid=[1, 2],
    grouped_sum=832393,
    ungrouped_total=832393,
)
→ {'rows': 2, 'zero_rows': 1, 'universe': 2, 'total': 832393}
```

The real Branch-B universe reported by the draft is 366,912 bricks. The validator accepted two because all identities came from the same caller and only the grand total has an external expected value. Carrying digests of those objects authenticates the counterfeit choice; it does not establish that the objects describe the selected release. The blind-double producer label in §7 is not a machine-checkable join and supplies no expected digest to a verifier.

Required repair: bind the universe proof to the resolved BS-1 release and BS-1b product by an independently frozen release-universe identity/digest and expected cardinality (or an equivalent independently reproducible source contract), require the BS-2c verifier to recompute that binding, and add a stale/wrong-universe fixture whose table and totals are internally consistent.

**Debt eligibility: DEBT-INELIGIBLE.** The entire count oracle, traversal order, power planning, selection, and later manifest closure are conditional on the universe identities. A wrong but self-consistent universe can change the chosen footprint while every currently named count check passes. That is direct selection/freeze poisoning, not bounded known debt.

### F3 — MEDIUM / REPAIR-REQUIRED — `ref/gen_string_field_registry.py` lines 507–520 and 759–768: FORM-SCHEMA ECHO checks tuple presence but never binds the tuple to its kind

`FORM_SCHEMAS` is advertised as “one kind literal → one exact ordered field set,” and the V116 repair says the echo keeps each form byte-equal in its home corpus. The shipped loop does not test that relation. For each `(_kind, _fields, _home)`, it constructs only `_tup` and fails only when `_corpus.count(_tup) < 1`; `_kind` is used solely in the diagnostic message. It does not require the kind literal to exist, occur exactly once, or be associated with that tuple.

I changed only the in-memory first mapping key to `renamed-successor-export`, a literal absent from the draft, while keeping the six-field tuple. The shipped condition’s inputs were:

```text
{'mutated_kind': 'renamed-successor-export',
 'kind_present_in_draft': False,
 'tuple_count': 2,
 'echo_would_fail': False}
```

The count of two also demonstrates the history/decoy weakness named in the brief: one occurrence anywhere is enough, and multiple occurrences are not rejected. Thus a generator-side kind rename, a stale historical tuple, or a cross-kind reassignment can leave the “kind→exact set” check green. The seeded close-domain controls test set widening/deletion but no control exercises kind deletion/rename or kind↔tuple reassignment.

Required repair: extract a unique, scoped `(kind literal, exact ordered tuple)` declaration for each form from its normative home; compare pairs, not tuple strings; reject absent/duplicate kind declarations and duplicate/decoy tuples; and seed rename, deletion, cross-form swap, and history-decoy controls through the exact shipped extractor.

**Debt eligibility: appendix-SAFE.** I manually verified the four present mappings against the pinned draft/spec bytes: both successor-export tuples and both terminal-review tuples currently match their intended forms. The defect is that the checker cannot preserve that fact across a future edit, not that the signed V116 bytes leave any current form’s fields undecidable. The freeze survives if the appendix records that this echo is not a kind-binding control and requires manual pair verification for any later generator revision.

## Attacks that held

- `ref/RAISE_SITE_CLASSIFICATION.md` matches the pinned v9 AST inventory: 112 `Raise` nodes plus one production `assert`; exception-node counts independently reproduced as 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, and 1 bare re-raise.
- The pinned v9 digest is exactly `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- The lifecycle pin in the draft matches `LIFECYCLE_GUARANTEE_SPEC.md`: `e087d932673a81b029e2ff42adb0394394f708230172fdde5ce2d4b464efa06a`.
- Verification retries do not themselves violate the five-pass successor predicate: an unsuccessful attempt emits a boundary/close pair but no pass record, so the next legal pass record remains at the same next-undischarged gate. The disclosure reconciliation is the disclosure gate’s pass, not a sixth gate.
- The current request-key contract closes the three requested join attacks at the textual level: the key is the arrival’s chain position; the verifier contract rejects a key unequal to that position, a terminal with no arrival, and multiple terminals/bindings for one arrival, subject to the expressly bounded anchor rollback residue.
- `tools/refusal_vocabulary_check.py` self-test returned 43 controls, zero failures, every error code controlled; the V116 draft returned zero vocabulary problems. I also reactivated a retired token using an unlisted phrase and the checker stayed green, but the tool and draft explicitly demote that finite activation list to a literal-shape tripwire and assign semantic reactivation to the referee round. No retired token is semantically reactivated in V116, so that successful evasion is an honestly stated limit, not an additional finding.
- Count statements held: the §7 table computes to 16 class P / 9 class E; the live prose agrees; `_registry_counts.txt` says `total=315 nonslot=10 pending=7`.

## Evidence and scope

Read in scope: the exact V116 draft; `BRIEF_V116_REVIEW.md`; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; pinned `ref/successor_ref_v9.py`; `ref/gen_string_field_registry.py`; `ref/_registry_counts.txt`; and `tools/refusal_vocabulary_check.py`. Executed read-only checks included SHA-256 recomputation, AST recount, the exact validator counterexample, an observation-stub call through the real `build_plan`, refusal-checker self-tests/current-draft check, prereg lint, and generated class-count comparison. No draft or referenced source was edited.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V116
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | §2.3 L179; §7 L915; §11 | The asserted pre-_plan non-null harness is unnamed, absent, and not a required build item, so BS-2c remains fillable through the None bypass.
F2 | HIGH | REPAIR-REQUIRED | §2.3 L177–184; §7 L915 | Non-null count proofs are self-consistent but unbound to the resolved release universe; a two-brick counterfeit with the pinned total passes v9.
F3 | MEDIUM | REPAIR-REQUIRED | ref/gen_string_field_registry.py L507–520, L759–768 | FORM-SCHEMA ECHO ignores each form's kind and accepts an absent/renamed kind whenever its tuple appears anywhere.
<!-- END FINDINGS-BLOCK -->
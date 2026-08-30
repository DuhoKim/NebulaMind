# V113 whole-document adversarial review — GPT56

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V113_REVIEW.md` first and independently obtained the required subject digest before reading the draft:

`8a04e549e4a25315d2eec2440d7f3eba3c08a5ea85e7314a12989361bd573e7d`

V113 closes several V112 defects, including request-digest recomputation, the roster schema, the two terminal-review forms, and the pre-lock export form. It does not close the verification-pass law. The new hold rule conflicts with the pre-existing termination ordering, its retry cap has no failed-pass record from which it can be counted, and its claimed wait bound omits the quantum forced by its own strict inequality. I also broke the registry generator's universal extraction claim and found a stale-export seam in the clean/terminated endgame.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — The verification hold and T1's pre-drain in-hand-frame rule have no legal joint execution

`LIFECYCLE_GUARANTEE_SPEC.md` T1 requires a fully decoded frame already in Row B's hands to complete its ARRIVAL commit before DRAIN-START (`LIFECYCLE_GUARANTEE_SPEC.md:131`; draft's byte-derived quote at §6.1 line 640). New §3d says that after VERIFICATION-BOUNDARY and before gate action the only legal appends are pass-owned records and the indivisible termination units DRAIN-START or RECEIPT-NOTE; an ordinary ARRIVAL inside the budget is malformed (`LIFECYCLE_GUARANTEE_SPEC.md:142-148,155-158`; draft §11 line 1562).

Counterexample: a pass appends its boundary; a frame becomes fully decoded and sits in Row B's hands while admission is held; then a TERMINATED-family condition fires before release. T1 orders ARRIVAL then DRAIN-START. Section 3d forbids that ARRIVAL and permits only the DRAIN-START unit. Appending DRAIN-START first violates T1 and omits the decoded frame from T2's drain set; appending ARRIVAL first makes the history malformed under §3d. The stated "indivisible unit" exception therefore is not indivisible in the exact corner T1 requires.

Required repair: state the ordering at pass entry and termination explicitly. Either a boundary may be appended only when no decoded-uncommitted frame exists and decoding is stopped during the hold, or the termination exception must include T1's bounded arrival-plus-drain-start unit and the verifier must recognize that exact sequence.

### F2 — HIGH / REPAIR-REQUIRED — `PASS_RETRY_MAX` is not countable from any authenticated byte

Section 3d says a gate refuses after `PASS_RETRY_MAX` consecutive passes "abort or expire" (`LIFECYCLE_GUARANTEE_SPEC.md:165-170`; draft §11 line 1562). No pass-failure record is defined. The exact non-χ record inventory has VERIFICATION-BOUNDARY and successful GATE PASS RECORD bodies, but no pass-attempt terminal body, failure sequence number, gate identity on a failed attempt, or close class for `ABORTED` versus `EXPIRED` (draft §6.1 lines 672,674; `ref/STRING_FIELD_REGISTRY.md:208-214,268-271`). A refusing pass is expressly barred from emitting a pass record in the §11 fixture contract. The existing ATTEMPT-CLOSE body is for member replay exhaustion and its closed class is only `ABORTED | ABORTED-BY-RESTART`; it is not a verification-pass close and contains no gate field (`draft:674`; registry `attclose.*` rows 106-110).

Thus two implementations can see the same chain and disagree: one counts `abort, expiry, abort` as three consecutive failures; another keeps separate counters and resets on the alternating class; a restart can forget either counter. Both satisfy every declared record schema because no byte records the classification or succession. The retry-cap fixture can exercise an in-memory counter but cannot make the run history auditable.

Required repair: define and admit a domain-separated verification-pass close record carrying at least gate, attempt ordinal or predecessor, boundary identity, and closed terminal class; require one close for every non-successful boundary; derive the combined consecutive-failure count from those records across restarts; and add alternating abort/expiry plus restart fixtures.

### F3 — MEDIUM / REPAIR-REQUIRED — The strict release inequality falsifies the stated one-budget and cumulative wait bounds

Section 3d makes release legal only when the recorded difference is **strictly greater than** `GATE_PASS_BUDGET` (`LIFECYCLE_GUARANTEE_SPEC.md:150-163`). Therefore an arrival recorded exactly at boundary + budget is illegal. Because recorded readings are quantized to `g`, the first legal recorded difference is at least budget + `g`, not budget. The draft nevertheless says a hung verifier holds admission "for at most one budget" and bounds cumulative wire wait by `five gates × PASS_RETRY_MAX × GATE_PASS_BUDGET` (draft §11 line 1562; spec lines 161-170).

The existing direction rule makes this conservative, not exact: arrivals round down while checkpoint-family boundaries round up. It does not open an early-admission hole, but it can add another quantum of real wait around the recorded endpoints. The claimed upper bound omits even the unavoidable recorded `+g`, and can understate real wait by more.

Required repair: either use `>=` and define the equality case as release, or retain strict `>` and state a bound that includes the quantization term with exact rounding directions (and use that same expression in the five-gate envelope).

### F4 — HIGH / REPAIR-REQUIRED — The registry generator can silently omit a newly declared non-χ schema despite the draft's universal no-omission claim

Draft §6.1 says the generator "extracts every field token from the declared field lists" and therefore cannot silently omit a field (`draft:684-693`). The generator repeats the stronger claim that it extracts "every field token from the draft's declared schema blocks" (`ref/gen_string_field_registry.py:2-15`). Its actual `extract()` is a finite set of regexes for the BS-3g block, the access-log tuple, the enumeration-entry block, three acceptance bits, and `cause` (`gen_string_field_registry.py:454-472`); many other schemas are hand-declared constants.

I attacked the absence claim in memory, without writing any file. Appending this draft-shaped declaration to the exact V113 text:

`**PROBE non-χ record:** closed schema (kind, surprise_string); authenticated and pre-unblinding.`

left `extract(mutated) - extract(original) == []`, produced no new `crosscheck_declared()` problem, and `surprise_string` existed in neither constraint map. The current generated files are byte-consistent, but a future schema in an unrecognized shape can be omitted by source, registry, and surface together while the generator remains green. That is the exact silent-omission class the prose says is impossible.

Required repair: derive schema declarations from one parseable source grammar and fail on every declared closed-schema block the parser cannot consume; add this unknown-block/unknown-field probe as a seeded control. Alternatively demote the universal claim and enumerate, honestly, every mechanically extracted block versus every hand-declared block, with a completeness predicate over the declaration sites.

### F5 — MEDIUM / REPAIR-REQUIRED — A clean successor export can survive as a stale sibling when termination occurs during disclosure

T3 makes the terminated-run successor export atomic with drain close, but says only that a clean run exports "at disclosure's mandatory reconciliation pass" (`LIFECYCLE_GUARANTEE_SPEC.md:133`; draft's quote at §6.1 line 642). It does not say the clean export is in the same atomic commit as the disclosure pass record, is emitted only after that record, or is invalidated if a TERMINATED condition fires during the pass.

Counterexample: the disclosure reconciliation emits the clean successor export; before its gate action/pass record or terminal ceremony completes, a TERMINATED condition fires. T1/T3 drain the run and atomically emit the terminated export. The chain ending selects the terminated review body, but nothing retracts or marks the first export stale, so two authenticated successor-facing siblings survive with different ending claims. This is the endgame version of the mutable-sibling problem.

Required repair: make clean export + disclosure pass record one atomic, ordered completion commit, forbid clean export before that commit, and state a one-export-per-run identity rule. A termination before that commit must emit only the terminated form; a later termination must be defined as outside the completed run or produce an explicit supersession relation.

### F6 — LOW / ADVISORY — The dispatch's generated-count summary is stale in all three values

The brief states "Registry 306 fields; kinds 26; surface 20 rows" (`gates/BRIEF_V113_REVIEW.md:161-162`). The generated bytes say:

- `ref/_registry_counts.txt`: `total=307 nonslot=10 pending=7`;
- `ref/DOMAIN_KINDS.md:3`: 27 kinds;
- `ref/NONCHI_SURFACE.md:29`: 19 rows.

The registry, domain-kind, and surface checks are byte-equal, so this is not generated-output drift; it is a stale hand summary in the dispatch. It should be generated or quoted from the artifacts, not restated.

## Failed attacks / repairs that held

- Subject identity held exactly; the lifecycle pin also matched live bytes: `a55fb969c508439cad2ccfb4ac192d221f39b38a206435c9d8a8d3a4a49f4850`.
- The request identity is consumed, not merely present: §11 requires recomputing the domain-tagged `(origin_row, frame_sequence, operation, object_identity)` digest, requires `origin_row == row`, and names wrong-digest and row-alias fixtures. This closes the semantic hole that the phrase-only preimage echo cannot close by itself.
- The evidence-prefix concatenation attack failed for two different emissions: an evidence body begins with only one adjudicated pair, so a second review with a different pair cannot reuse it under the prefix equality check. An evidence artifact containing exactly the pair is vacuous, but the draft now explicitly classifies everything beyond the pair as human testimony rather than claiming evidentiary proof; I therefore did not score that deliberate posture.
- The roster attack held at the stated fail-closed strength: roster entries are frozen inside P0 BS-2k materials, machine keys are excluded, and a roster change/key rotation explicitly requires a re-freeze. A dead roster can make a mismatch unreviewable, but it does not silently authorize a replacement.
- A pre-lock terminated run cannot resume and later lock under the same run: standing drain-start/TERMINATED material bars ordinary admission; the pre-lock export therefore cannot lawfully become a clean sibling through same-run resumption.
- The completed and terminated terminal-review bodies are domain-separated and no longer use sentinels. The completed form binds the disclosure pass record; the terminated form binds the terminal checkpoint.
- Request-key attacks held under the current contract: per-row `frame_sequence` is strictly increasing, `request_digest` is recomputed, duplicate digests are refused, terminal-without-arrival and two-arrival/one-binding cases are named fixtures, and recovery resumes rather than re-appending ARRIVAL.
- The §2.2 oldest-quiet cut inventory still states eight predicates and the absence of a surface-brightness cut; I found no new contradiction in the current machinery.
- The draw-count arithmetic is internally consistent: Γ=0.25, `n_steps=50`, Δγ=0.01, 51 grid points, zero at `j0=25`, 99 draws, and common random variates.
- The raise classification closes mechanically: independent AST enumeration found 112 `raise` nodes plus one production `assert`; all 113 line sites appear once in `ref/RAISE_SITE_CLASSIFICATION.md`, with class totals 32 CALLER, 56 INTEGRITY, 18 NUMERICAL, 3 PLANNING-INTERNAL, 1 TYPED-OUTCOME, and 3 WRAPPER. I did not re-score the parked per-call-site limitation.
- `tools/refusal_vocabulary_check.py` has the ruled eleven members, the sole nonmember occurrence is the explicitly retired identity token, and the checker honestly demotes semantic activation beyond its finite phrase list. No different live refusal leak was found.

## Executed evidence

- SHA-256: subject, lifecycle spec, frozen v9, raise classification, and refusal checker. The draft, lifecycle, v9, and checker pins matched their live bytes.
- `tools/prereg_lint.py`: exit 0; 16 class P / 9 class E; 97 legacy advisories, 0 blocking.
- `tools/prereg_counts.py`: 16 class P / 9 class E; prose matches table.
- `tools/prereg_trace.py --check`: 112 computed transitions, 0 problems; three scope controls passed.
- `tools/lifecycle_derivation_check.py`: 0 problems.
- `tools/void_registry.py` and self-test: 60 antecedents; six controls, 0 failures; name-coverage only, as disclosed.
- `tools/refusal_vocabulary_check.py`: 0 problems; 43 controls, 0 failures.
- `ref/gen_nonchi_surface.py --check`: byte-equal, 0 problems; 6/6 controls.
- `ref/gen_domain_kinds.py --check`: byte-equal, all sites covered; 3 controls, 0 failures.
- `ref/gen_raise_classification.py --check`: byte-equal.
- Independent in-memory string-registry mutation: `surprise_string` was neither extracted nor rejected; no file was written.

No draft byte, generator byte, referenced artifact, or file outside this report was modified. The worktree contained extensive pre-existing untracked material; this report is the sole write made by this seat.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V113
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | lifecycle spec §3d L142-L158 / T1 L131; draft §6.1 L640, §11 L1562 | Verification hold forbids the in-hand ARRIVAL that T1 requires before DRAIN-START, leaving no legal termination order.
F2 | HIGH | REPAIR-REQUIRED | lifecycle spec §3d L165-L170; draft §6.1 L672,L674 / §11 L1562 | PASS_RETRY_MAX has no authenticated failed-pass close record, so abort/expiry succession is not countable across alternation or restart.
F3 | MEDIUM | REPAIR-REQUIRED | lifecycle spec §3d L150-L170; draft §11 L1562 | Strict greater-than release plus quantization requires at least budget+g, contradicting the one-budget and five-gate wait bounds.
F4 | HIGH | REPAIR-REQUIRED | §6.1 L684-L693 / gen_string_field_registry.py L2-L15,L454-L472 | The claimed exhaustive schema extractor silently ignores an unrecognized closed-schema block and its new string field.
F5 | MEDIUM | REPAIR-REQUIRED | lifecycle spec T3 L133 / draft §6.1 L642 | Clean export is not atomic with disclosure completion, so termination during reconciliation can leave stale clean and terminated sibling exports.
F6 | LOW | ADVISORY | brief L161-L162 / generated counts | Dispatch says 306 fields, 26 kinds, 20 surface rows; generated bytes say 307, 27, and 19.
<!-- END FINDINGS-BLOCK -->
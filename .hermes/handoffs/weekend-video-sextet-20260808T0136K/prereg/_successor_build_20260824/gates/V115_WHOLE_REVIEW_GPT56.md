# V115 whole-document adversarial review — GPT56

## Verdict

**NOT CLEAR.** The supplied draft matched the mandated SHA-256, but two freeze-poisoning defects remain in normative/generator surfaces and two claimed closure controls are demonstrably non-closed. The highest-severity defects cannot safely ride a known-debt appendix: one makes the schema-driven closing export/review machinery generate the wrong body, and one permits an incomplete count oracle on the code-defined production-planning path while the prose says incompleteness is refused.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the form-separated export and terminal-review contracts collapse into discriminator-blind union schemas

The normative lifecycle has distinct forms. `LIFECYCLE_GUARANTEE_SPEC.md:112` defines the terminated review body as

`(kind, terminal_checkpoint_digest, drain_start_position, recomputed_head, verifier_digest, transcript_digest)`

and the completed review body as

`(kind, disclosure_record_digest, successor_export_digest, recomputed_head, verifier_digest, transcript_digest)`.

The export also has distinct post-lock and pre-lock forms: V115 `§6.1:671`, `§3c` as quoted at line 642, and `§11:1564` give the post-lock/completed body as

`(kind, sealed_enumeration_digest, continuation_segment_digest, terminal_head, freeze_signature_digest, flagged_keys)`

while the pre-lock form is

`(kind, terminal_enumeration_digest, terminal_head, freeze_signature_digest, flagged_keys)`.

The generator inputs erase both discriminators:

- `ref/gen_string_field_registry.py:566-569` declares one `REVBODY` set containing all eight fields from both six-field forms.
- `ref/gen_string_field_registry.py:589-592` declares one `SUCCEXP` set containing all seven fields from both the six-field post-lock form and five-field pre-lock form.
- V115 `§11:1564` nevertheless says the producer derives the successor body “field-for-field from the registry's SUCCEXP set.” Taken literally, that generator input produces the seven-field union, which conforms to neither canonical body.

This is not merely a hypothetical future drift. The current generator input and current prose disagree about what “field-for-field” generation means. It also defeats the stated completeness control: an in-memory mutation of only §11's completed/post-lock schema from the correct six fields to the pre-lock-only `(kind, terminal_enumeration_digest, terminal_head, freeze_signature_digest, flagged_keys)` produced **0** problems from both `gen_nonchi_surface.check()` and `gen_string_field_registry.crosscheck_declared()`. The controls check union membership, not `(kind → exact field set)`.

Required repair: make export and review schemas kind-qualified mappings, not flat unions; require exact equality for each kind; seed deletion, addition, and cross-form-substitution controls for both forms. The ceremony/export generator must select the exact set by the chain-derived kind before serialization.

**Debt eligibility:** debt-ineligible. The defect sits inside the P9 human-signature binding and successor-facing export. Freezing it as known debt would freeze an ambiguous signed/exported body and defeat the closure the appendix is meant to attest.

### F2 — HIGH / REPAIR-REQUIRED — §2.3's old count-oracle completeness promise is false against the pinned normative code

V115 `§2.3:177-185` says `build_plan()` performs the complete count-oracle chain and names `validate_count_oracle()` as refusing any missing/extra brick and any grouped/ungrouped disagreement. The §7 BS-2c row at line 916 repeats the nonexistent symbol `validate_count_oracle`.

The pinned normative bytes tell a different story:

- `ref/successor_ref_v9.py` has SHA-256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, matching §0.
- No `validate_count_oracle` symbol exists in those bytes.
- The actual function is `validate_count_table()` at v9:847-894.
- Its universe equality is conditional on `universe_brickid is not None` (v9:869-877).
- Its grouped/ungrouped closure is conditional on `grouped_sum is not None` (v9:879-893).
- `build_plan()` requires the keyword names but does not require non-null values (v9:1291-1297), and `_plan()` forwards them directly to the conditional validator (v9:1308-1312).

Therefore a caller can invoke the production `build_plan(..., universe_brickid=None, grouped_sum=None, ungrouped_total=None)` and bypass both checks while satisfying the function signature. Independently, executing the pinned `validate_count_table()` on a two-row table with all three proof arguments omitted returned `{'rows': 2, 'zero_rows': 0}` rather than refusing. Required keyword *presence* is not proof-object *validity*.

This is the requested oldest-quiet attack: §2.3's completeness sentence predates the lifecycle patch train, and the current code-precedence rule at §0:99-100 makes the prose—not the code—the defect. The production chain can select from a table whose release-universe closure was never established.

Required repair: name the real symbol; make all three proof objects non-null and authenticated on the production path; refuse `None` before selection; add a production-path fixture showing explicit `None` cannot reach `_plan`, plus missing/extra and grouped/ungrouped controls through `build_plan()` itself.

**Debt eligibility:** debt-ineligible. This can change the selected footprint and every downstream statistic while still yielding apparently valid receipts. It is freeze-poisoning, not an honest unfinished implementation stub.

### F3 — MEDIUM / REPAIR-REQUIRED — the CLOSE-CLASS DOMAIN ECHO proves only placement of `EXPIRED`, not closure of either vocabulary

V115 `§6.1:674` and the lifecycle spec `§3d:177-180` define exact domains:

- `ATTEMPT-CLOSE.close_class` = `{ABORTED, ABORTED-BY-RESTART}`;
- `VERIFICATION-CLOSE.close_class` = `{ABORTED, EXPIRED, ABORTED-BY-RESTART}`.

But `ref/gen_string_field_registry.py:708-723` checks only three facts: `EXPIRED` remains somewhere in the vclose note, `EXPIRED` is absent from the attclose note, and the draft contains both qualified field names. It does not parse either set and compare exact membership.

I mutated the in-memory `vclose.close_class` constraint by appending a fourth token, `ABORTED-BY-OPERATOR`, while preserving `EXPIRED`. `crosscheck_declared()` returned no close-class problem before or after the widening:

- baseline close-class problems: `[]`
- four-token close-class problems: `[]`

Thus the exact counterexample named in the brief survives: `{ABORTED, EXPIRED, STALLED, ABORTED-BY-RESTART}` (or any other fourth member) passes this echo. Such a token changes which closes count toward retry exhaustion and can create an unruled route through the pass law.

Required repair: parse both domain declarations into canonical token sets and require exact equality to the two expected qualified sets; add fourth-token, deleted-token, cross-domain substitution, and duplicate-token seeded controls.

**Debt eligibility:** debt-ineligible as a control defect. A known-debt freeze cannot rely on a “closed vocabulary” control that accepts widening. This is a permitted control-on-existing-generator repair under the scope freeze, not a request for a new record kind.

### F4 — MEDIUM / REPAIR-REQUIRED — refusal-vocabulary R02 does not enforce the non-closure principle it claims to check

The draft says the refusal vocabulary is not closed (V115 `§6.1:595-623`) and cites `tools/refusal_vocabulary_check.py` as checking the eleven-code text and carrying no closure claim (line 623). The tool's own contract says R02 catches when “the draft ... claims the set is closed” (`tools/refusal_vocabulary_check.py:22-26,74-77`).

Implementation is substantially narrower. R02 searches only a line containing literal `closed set` or `closed vocabulary` together with a refusal-vocabulary phrase (`tools/refusal_vocabulary_check.py:213-224`). Semantically identical closure claims are invisible. Against the exact V115 bytes, appending either of these contradictory normative sentences left `check()` at `[]`:

- `The refusal vocabulary is exhaustive and complete.`
- `These eleven refusal reasons exhaust every possible refusal.`

The checker therefore lets the rejected closure principle re-enter while remaining green. This is separate from the checker’s honestly disclosed finite retired-token activation heuristic at lines 129-135; R02 presents itself as the closure-claim control and does not disclose a finite synonym surface.

Required repair: either demote R02's claim explicitly to a literal-shape tripwire, as the retired-token guard already does, or implement a bounded normative declaration grammar with a single required non-closure sentence and contradiction/tombstone controls for `exhaustive`, `complete`, `covers every`, and equivalent sanctioned forms. Do not imply semantic consistency from a regex that checks two literals.

**Debt eligibility:** debt-ineligible as stated. The known-debt appendix depends on preserving the distinction between an open maintained vocabulary and a falsely closed one; a checker that permits the opposite principle cannot sign that boundary.

## Attacks that held

- **Subject identity held.** SHA-256 recomputed as `8ed151b74f9b26892ea884557904acf4f7695b319389a5e7b241184fac3e07d7` before the draft was read.
- **Referenced pins held.** The lifecycle spec recomputed to `a0c345aadcad2aaccc43b7635674d23f55d097e07d0d869dcb8495180fcdb8ad`; the refusal checker recomputed to `bf54a79bedca5dbb1d9db66de868c4e98dc6894dfcb236896495ffed8596437e`; frozen v9 recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- **As-written completed review body held locally.** The completed form in the spec does contain both `disclosure_record_digest` and `successor_export_digest`, and the ceremony text says absent, duplicate, and byte-mismatched exports are refused. F1 is the generator/form discriminator failure, not a claim that those two words are absent.
- **Gate-equality text held at the stated seam.** The boundary carries `gate`; boundary-to-close/pass gate equality is expressly required in V115 line 1564 and spec §3d, with mismatch malformed. The spec also states exactly one pass record per gate in the five-gate order. I did not score the weaker observation that §11 phrases this as “the NEXT gate verifies it.”
- **Request-key join held as written.** V115 assigns `request_key` to the arrival's chain position and the verifier contract names the requested counterexamples: two terminals for one key, terminal with no arrival, two arrivals under one binding, key unequal to arrival position, and row/operation/object identity mismatch.
- **Receipt-transition residue was honestly scoped.** Strict increase does not require contiguous `frame_sequence`; a decoded frame dying before durable ARRIVAL is W0/wire residue, and N1 states delivery/ACK is outside custody. I found no contradictory promise of caller acknowledgment before arrival commit.
- **Mechanical batteries were green but not dispositive.** `tools/refusal_vocabulary_check.py --self-test` reported 43 controls, 0 failures; the live refusal check reported 0 problems; `tools/prereg_lint.py` reported 16 class P / 9 class E and 0 blocking findings (97 legacy advisories). The counterexamples above show why green is not clearance.
- **Raise-site enumeration count held mechanically.** `ref/RAISE_SITE_CLASSIFICATION.md` has 113 unique rows matching 112 AST `Raise` nodes plus the production assert at v9:1622. I did not re-score the already-referred per-raise-versus-per-call-site unit defect.

## Evidence and scope

Read in full or by exact line-window: `gates/BRIEF_V115_REVIEW.md`, the exact V115 subject, `LIFECYCLE_GUARANTEE_SPEC.md`, `ref/RAISE_SITE_CLASSIFICATION.md`, `ref/successor_ref_v9.py`, `ref/gen_string_field_registry.py`, `ref/gen_nonchi_surface.py`, `ref/gen_domain_kinds.py`, and `/Users/duhokim/NebulaMind/NebulaMind/tools/refusal_vocabulary_check.py`. Checks and adversarial mutations were run in memory; no source or draft file was edited. This report is the only file written by this seat.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V115
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | lifecycle spec §3b line 112; draft §6.1 lines 642/671 and §11 line 1564; gen_string_field_registry.py lines 566-569/589-592 | Kind-separated export and terminal-review forms collapse into flat union schemas, so schema-driven generation can emit no canonical form.
F2 | HIGH | REPAIR-REQUIRED | §2.3 lines 177-185; §7 line 916; successor_ref_v9.py lines 847-894 and 1291-1312 | Production planning accepts null count-oracle proof objects and bypasses the completeness checks the prose says are mandatory.
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 line 674; lifecycle spec §3d lines 177-180; gen_string_field_registry.py lines 708-723 | CLOSE-CLASS DOMAIN ECHO accepts a fourth verification-close token and therefore does not enforce the declared exact domain.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 595-623; refusal_vocabulary_check.py lines 22-26, 74-77, 213-224 | R02 misses semantically explicit closure claims such as “the refusal vocabulary is exhaustive,” allowing the rejected principle to return under a green check.
<!-- END FINDINGS-BLOCK -->
# V84 whole-document adversarial review — GPT56

## VERDICT: NOT CLEAR

The V84 bytes are the assigned bytes, and several advertised repairs hold mechanically, but the whole document is not clear. The highest-impact failures are in the new lifecycle/recurrence machinery: serialization is substituted for crash-atomic BS-L issuance, and the cross-run recurrence rule depends on future documents voluntarily listing this run. The checked-declaration machinery is also materially weaker than the prose/brief claims, and the generated string registry is not even a well-formed four-column table at four rows while disagreeing with the draft about `baseline_verdict`'s vocabulary.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — §6.1 lines 608, 724–731; lifecycle spec lines 19–21, 63–70, 101–104

**The “issuance boundary is a point” repair handles concurrency but not a writer death mid-issuance.**

Line 608 says checkpoint-seal-through-issuance-completion is “ONE serialised step” and therefore no event can be appended during it. Serialization excludes a competing append; it does not make the multi-effect step crash-atomic. Clause 3 requires canonicalization, a detached signature, artifact production, and issuance, while Clause 4 says the chain continues through issuance. Neither the draft nor `LIFECYCLE_GUARANTEE_SPEC.md` places `{sealed checkpoint, BS-L body/digest, detached signature, durable issuance marker}` in one atomic commit or defines recovery from a prefix of those effects.

The lifecycle spec's atomic object is explicitly the TOUCH/REFUSAL commit (`{store effect, event, binding}`), not BS-L issuance. Its W2-is-empty claim therefore does not cover this different operation. A concrete counterexample is: Row B seals the checkpoint and persists a signed BS-L artifact, then dies before the state used to classify later chain positions as “after BS-L issuance” is durably committed. Recovery can treat the same next event as pre-issuance (must be in sealed materials, now impossible) or post-issuance (continuation-eligible), with no specified binding deciding which. The request-recovery binding rule is inapposite unless BS-L issuance is itself defined as a bound request in that transaction, which it is not.

Repair requires a durable atomic issuance record/transaction boundary and a recovery rule that gives every recovered prefix exactly one side of the partition; “single writer” alone is insufficient.

### F2 — HIGH — REPAIR-REQUIRED — §6.1 line 601; §10 lines 1153–1155; lifecycle spec lines 162–168

**Cross-run recurrence is still customary, not enforceable: nothing obligates the next preregistration to list V84/this run.**

Line 601 correctly concedes that both verifier passes see only this run, then claims the blindness is closed by an obligation on a successor freeze review over its *listed* predecessors. It also says “this one lists V3-pred.” That defines the domain after a predecessor is listed but supplies no rule, producer, schema, or checker that forces the successor to list this preregistration/run. A successor can list V3-pred again, omit V84's run, and truthfully pass the stated rule over its listed domain; a previously explained class then never becomes recurring.

The lifecycle spec confirms at line 167 only that cross-run recurrence “stays a successor-preregistration duty.” Section 10's statement that the next draft records the transition that created this draft is a version/repair-trace convention, not an authenticated predecessor-run inventory and not a consumer of surviving enumeration entries. No §11 build item checks successor completeness against a run registry.

Repair requires a checkable predecessor/run manifest with an external source of completeness (or a rule binding every successor in this study lineage to the immediately preceding run), plus a freeze checker that consumes that manifest and the predecessor enumerations. A closed rule over a voluntarily listed set is not cross-run closure.

### F3 — MEDIUM — REPAIR-REQUIRED — §6.1 lines 664–678; `ref/gen_string_field_registry.py` lines 276–306

**The “checked declarations” check is phrase-presence testing, not set equality; it accepts missing members and stranger normative members.**

I imported the generator without running `main()` and called `crosscheck_declared()` on in-memory mutations. Every one of these damaging mutations returned `[]` (PASS):

1. Clause 6: replace “both store identities” with singular “the main store identity” — the checker still considers both `store_identity_main` and `store_identity_committee` present because each probes only the word `store`.
2. Clause 6: add `operator note` as a ninth canonical-body member — no stranger-member check fires.
3. Clause 3(b): add `operator note` to the lock body — no stranger-member check fires.
4. Freeze body: delete the class-count component — no check fires at all, although the function docstring says FREEZE is one of the three checked declarations.

The code explains the result. Clause 6 maps both store leaves to the same first-word probe (`phrase.split()[0]`), Clause 3(b) checks only that thirteen substrings occur, neither branch extracts an actual set or rejects extras, and there is no freeze-body comparison before the function returns. This directly defeats the stated “missing or stranger member” property.

Repair requires extraction of the actual ordered member lists from each normative clause and exact equality against the declared registry set, including duplicate and extra-member rejection. The freeze-body set must actually be checked.

### F4 — MEDIUM — REPAIR-REQUIRED — §11 lines 1308–1322, 1494–1500; `ref/gen_string_field_registry.py` lines 185–230; `ref/STRING_FIELD_REGISTRY.md` lines 168, 177, 184, 186

**The generated registry is structurally malformed and assigns `baseline_verdict` the wrong closed vocabulary.**

The draft defines `baseline_verdict` as the γ=0 token from the study run-outcome vocabulary when constant, or `PER-DRAW` otherwise. The generator instead records its note as `HELD | FAILED | PER-DRAW`; `HELD`/`FAILED` are the *invariance* vocabulary, not the run outcomes. A verifier implemented from this registry would either reject legitimate `REPRODUCED-LONGO`/`REJECTED-AT-LONGO-AMPLITUDE`/`INCONCLUSIVE...` baselines or accept an invalid `HELD` baseline.

The emitted Markdown makes the defect worse: unescaped `|` characters split registry rows. A byte-level column-count check found four data rows with other than the required five pipe delimiters:

- line 168 `baseline_verdict`: 7 delimiters;
- line 177 `disposition`: 6;
- line 184 `gamma_bound`: 7 (the mathematical `|gamma_hat|` is unescaped);
- line 186 `invariance_outcome`: 6.

Thus the artifact advertised as the value-domain registry is not a valid four-column registry under ordinary Markdown/table parsing, and the generator has no emitted-structure validation. Repair both the baseline domain and the serialization (escape cells or emit a machine-readable canonical registry and validate round-trip column count/domain membership).

### F5 — LOW — ADVISORY — §6.1 line 618; `tools/refusal_vocabulary_check.py` lines 121–127, 129–161

**The retirement/activation guard is bypassable by an ordinary activation verb outside its finite list.**

The checker candidly comments that `ACTIVATION` is finite and incomplete, but the draft still relies on the checker as the blocking divergence control. I appended this in memory to the checker's clean fixture:

`REFUSED-LOCK-NOT-OPEN was retired; after P7 it controls requests.`

`check()` returned no problem. The first fragment lawfully retires the token; the second activates it through the pronoun “it,” and `controls` is absent from `ACTIVATION`. This is exactly the brief's requested “reactivate without any listed word” attack. The honest comment prevents an overclaim about what the code author knew, but it does not make the blocking semantic check sound.

Advisory repair: stop trying to infer normative activation from an open prose vocabulary. Put active/retired membership in a canonical machine-readable set and make prose references non-operative, or require explicit labelled lifecycle declarations whose parser compares exact status tokens.

## Failed attacks / checks that held

- Subject SHA-256 independently recomputed as `6ec2bc2bdabcd12c4d292d33fce867dcc482a29e4bf874c16545f7105a1c95f6` before reading.
- `LIFECYCLE_GUARANTEE_SPEC.md` recomputed to `5f4bd2859ba0edd5558410793beb702a42ae34aeae7f9dbdd470c5970a7840e1`, matching the draft pin.
- `tools/refusal_vocabulary_check.py` recomputed to `c448646b955bd2200d5f3062a397791530300a29a32b353a62d7f13919ae8dee`, matching the draft's abbreviated digest.
- `ref/successor_ref_v9.py` recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, matching its pin.
- Live prereg lint exited 0 with 16 class-P / 8 class-E and 97 advisory, 0 blocking. I did not re-report the 97 legacy citations, per the brief.
- Refusal-vocabulary check on V84 returned 0 problems; its self-test returned 32 controls, 0 failures, every code controlled. F5 is an out-of-suite semantic mutation, not a claim that the shipped controls fail.
- Independent AST recount found 112 `Raise` nodes with the advertised exception breakdown: 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, 1 bare. `ref/RAISE_SITE_CLASSIFICATION.md` has 112 unique rows.
- The live Clause 6 and Clause 3(b) member prose currently contains the intended members; F3 is that the claimed generator guarantee does not enforce this and accepts concrete divergent bytes.
- The current refusal prose does not activate a retired code with the tested bypass; F5 attacks the blocking guard's claimed future divergence protection.
- The parked draw-discipline, availability-code object semantics, durable pre-verdict state, strata/producer, VOID partition, BS-3g lifecycle cycle, integrity-mismatch collision, and per-raise versus per-call-site unit were not re-derived as new findings.

## Evidence and scope

Content-read: `gates/BRIEF_V84_REVIEW.md` first; then the hash-verified V84 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/gen_string_field_registry.py`; generated `ref/STRING_FIELD_REGISTRY.md`; repository `tools/refusal_vocabulary_check.py`; and the pinned `successor_ref_v9.py` by AST for raise-node enumeration. Commands/checks were read-only or in-memory. I did not run the registry generator's `main()` because it writes artifacts. No draft or referenced file was modified; the only write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V84
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 L608; lifecycle spec §§1,3–4 | Serializing BS-L issuance does not define crash-atomic issuance or recovery of a half-issued lock.
F2 | HIGH | REPAIR-REQUIRED | §6.1 L601; lifecycle spec §6 | Cross-run recurrence ranges only over voluntarily listed predecessors; nothing forces the next preregistration to list this run.
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 L664–678; gen_string_field_registry.py L276–306 | Checked declarations accept a missing store member, extra normative members, and an unchecked freeze-body deletion.
F4 | MEDIUM | REPAIR-REQUIRED | §11 L1308–1322, L1494–1500 | STRING_FIELD_REGISTRY is malformed at four rows and gives baseline_verdict the invariance vocabulary instead of run outcomes.
F5 | LOW | ADVISORY | §6.1 L618; refusal_vocabulary_check.py L121–161 | A retired code can be reactivated with “it controls requests” without tripping the finite activation guard.
<!-- END FINDINGS-BLOCK -->
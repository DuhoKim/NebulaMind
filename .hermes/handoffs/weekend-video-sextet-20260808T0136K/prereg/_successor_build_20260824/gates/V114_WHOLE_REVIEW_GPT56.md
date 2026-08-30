# V114 whole-document adversarial referee — GPT56

## Verdict

**NOT CLEAR.** I found three repair-required defects: two in the new verification-pass machinery and one in the claimed generated repair trace. The first two are lifecycle/verifiability defects and cannot safely be carried into a known-debt appendix: one makes the expiry close simultaneously conforming and nonconforming, and the other leaves the condition that prevents a T1/hold deadlock as unreceipted Row-B state. Both poison the freeze rather than merely annotate unfinished implementation.

## Subject identity and scope

- Required subject SHA-256, recomputed before reading: `721e41ebfbbb6653615dea2da3be7b4c4d0b5a931d4692097fccc2973070c3aa` — exact match.
- `LIFECYCLE_GUARANTEE_SPEC.md`: `6845b868a8e6546a55c9a41e42e6cc3fecd4a8467f88dd01d6551c776fb877db`.
- `ref/successor_ref_v9.py`: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — matches the draft pin.
- `ref/RAISE_SITE_CLASSIFICATION.md`: `3b0b886fe3c5ff7d5f9d188f7938bd39202de2a979263c57edb5879b22223cb2`.
- `tools/refusal_vocabulary_check.py`: `bf54a79bedca5dbb1d9db66de868c4e98dc6894dfcb236896495ffed8596437e`.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — §6.1 L674 / spec §3d L187–195 — `VERIFICATION-CLOSE.close_class` has two incompatible closed vocabularies

The new record is not single-valued in the draft's own bytes.

- `LIFECYCLE_GUARANTEE_SPEC.md` L187–195 defines `VERIFICATION-CLOSE.close_class` as exactly `{ABORTED, EXPIRED, ABORTED-BY-RESTART}` and uses `EXPIRED` for the budget-expiry close.
- V114 L674 first repeats that three-token set for `VERIFICATION-CLOSE` and explicitly calls it distinct from the attempt-close two-token set.
- The same L674 then applies the generic tail ``close_class` the closed two-token set {`ABORTED`, `ABORTED-BY-RESTART`}`` to the admitted records. Read literally, an expiry close required by §3d is forbidden by §6.1's exhaustive non-χ surface.
- The generated registry chose one side rather than resolving the draft: `ref/STRING_FIELD_REGISTRY.md` L271–275 assigns `vclose.close_class` the three-token vocabulary, while `attclose.close_class` at L106–110 has the two-token vocabulary. The registry and its green checks therefore do not make the contradictory draft bytes single-valued.

Counterexample: a pass reaches its budget without a termination or restart. Section 3d requires Row B to append `VERIFICATION-CLOSE(..., close_class=EXPIRED, ...)`; the first half of L674 and the registry accept it, while L674's later closed-set sentence rejects it. The retry count cannot be a frozen function of conforming bytes while the byte vocabulary itself disagrees.

Required repair: scope the two-token tail expressly to `ATTEMPT-CLOSE` and state the three-token `VERIFICATION-CLOSE` domain exactly once, then add a semantic cross-check/control that deletes `EXPIRED` from either declaration and goes red. This is not safe known debt: it directly controls whether expiry attempts are countable and whether the retry cap is verifiable.

### F2 — HIGH — REPAIR-REQUIRED — spec §3d L149–159; V114 §11 L1563 — the pass-entry precondition is asserted over invisible state, with no enforcing or evidentiary contract

The repair depends on the proposition that no fully-decoded, uncommitted frame is in Row B's hands when the boundary is appended. That proposition is what makes the mid-hold termination corner “vacuous by construction”: otherwise T1 requires the in-hand frame's arrival first, while the hold forbids that arrival.

But the construction is not specified:

- The `VERIFICATION-BOUNDARY` schema is only `(kind, boot_epoch, monotonic_reading)` (V114 L674); it carries no decoder-state or drain-of-in-hand-frames evidence.
- Spec §3d L149–159 says the precondition and pause hold “by construction” but names no actor/check, atomic relation between decoder state and boundary append, testimony status, or fixture that can fail.
- The §11 verifier item at V114 L1563 paraphrases the rule, but its listed fixtures cover timing, close counting, restart and second-boundary cases—not boundary insertion while a decoded frame is already in hand. A search of the V114 bytes finds the fully-decoded/pass-entry rule only in T1 and this paraphrase; no separately pinned producer/verifier obligation closes it.

Counterexample: Row B finishes decoding frame F, then appends a verification boundary before committing F's ARRIVAL. A termination unit lands during the hold. T1 demands F's arrival before the unit; §3d makes an ordinary arrival at or inside the hold malformed. The log has no byte from which a verifier can distinguish this forbidden execution from the claimed vacuous one.

Required repair: specify the local atomic/serialized transition that drains decoded frames and freezes decoder state before boundary append; classify the unobservable part explicitly as implementation testimony; and require a BS-2k fixture/control that attempts boundary insertion with a decoded-uncommitted frame and is refused. If chain verification is claimed, add the evidence that makes it chain-checkable. This cannot ride in known debt because the current gap destroys the totality of the request lifecycle exactly at the χ-custody gate boundary.

### F3 — MEDIUM — REPAIR-REQUIRED — §10 L1083–1198; `tools/prereg_trace.py` L307–320 — the “generated” trace contains stale mechanical columns that `--check` does not compare

V114 L1198 says the digest, section-change and row-count columns are generated by `tools/prereg_trace.py`. Independent reconstruction with the current tool over the on-disk draft sequence disagrees with the written table:

- SHA columns agree for all in-scope rows.
- The generated section-change column disagrees on 29 transitions: V36→V61, V65→V66, and V110→V113 (written rows at V114 L1170–1194, L1165, and L1142–1144).
- The generated row-count rendering disagrees on V36→V37 and V84→V85 (L1194 and L1146). The underlying count moves are compatible, but the written cells are not the generator's emitted bytes.
- Example: for V36→V37 the current generator emits `§7.1 (+9/−1), §7 (+2/−1), (preamble) (+1/−1), §1 (+1/−1), §10 (+1/−0)` and `class-P rows 15 → 16`; V114 L1194 instead says `§1 (+1/−1), §5 (+0/−0), §7 (+1/−0), §7.1 (+6/−1), §10 (+1/−0)` and `15/8 → 16/8`.
- `python3 tools/prereg_trace.py … --check V114` nevertheless reports `113 computed transition(s); 0 problem(s)` because `check_trace()` L307–320 checks only row presence and the result digest. It never compares the generated section/count cells whose provenance L1198 asserts.

Required repair: regenerate the mechanical columns from the current tool or explicitly mark non-generated additions; make `--check` compare every claimed generated column byte-for-byte (leaving the findings-answered column human as documented). This is a trace/provenance defect rather than a χ-integrity defect, so it could be debt only if the freeze stops claiming those columns are generated and verified.

## Failed attacks / holdings

- **2g edge held.** With boundary/checkpoint readings rounded up, arrivals rounded down, and strict recorded release, the worst quantization placement needs true elapsed approaching `budget + 2g`; I did not find an early-release counterexample. Same-quantum arrivals remain inside the recorded window and are refused.
- **Epoch transition held at the main rule.** Spec §3d aborts open passes on epoch change and requires a next-epoch `ABORTED-BY-RESTART` close; close counts are taken since the last pass record, so the prose does not reset the counter merely because the epoch changed.
- **Cross-gate hold composition resisted the simple interleave.** The legal-append list between a boundary and its action does not admit another gate's boundary, even though the later alternation sentence is per gate. I therefore did not count the five-open-boundaries probe as a finding.
- **Export atomicity held against the stale-sibling attack.** The terminated export shares the terminal-checkpoint step; the clean export shares the disclosure-pass commit; the completed terminal-review form binds the disclosure record and recomputed head. I found no second legal export producer in V114.
- **Class counts held.** `tools/prereg_counts.py` independently computed 16 class P / 9 class E and reported that prose matches the table.
- **BS-3g blockers held.** The mapping sentinel cannot discharge BS-6, the replay harness is explicitly missing/unset, and a failed or absent receipt leaves BS-6 closed. I found no surviving emission path through all named blockers.
- **Refusal-vocabulary checks held their stated, limited claim.** Live subject: 0 problems; self-test: 43 controls, 0 failures. I did not treat green text-pattern checks as proof of the runtime mechanism.
- **Other generated checks held their stated predicates:** prereg lint 0 blocking (97 legacy advisories), lifecycle derivation 0 problems, non-χ surface byte-equal with 0 problems and 6/6 controls, domain kinds byte-equal with all sites covered and 3/3 controls, supersession sweep byte-equal, raise ledger byte-equal, string-registry in-memory reconstruction `total=313`, no missing/stale rows.
- **Raise classification was inspected but not re-found as new debt.** The per-raise/per-call-site unit defect is already parked by the brief; I found no basis to claim it newly worsened in V114.

## Evidence ledger and custody

Read in full or targeted form: the V114 brief; V114 subject; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/successor_ref_v9.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `ref/gen_nonchi_surface.py`; `ref/gen_domain_kinds.py`; `ref/gen_raise_classification.py`; `ref/gen_sweep_receipt.py`; `tools/refusal_vocabulary_check.py`; `tools/prereg_lint.py`; `tools/prereg_counts.py`; `tools/prereg_trace.py`; `tools/lifecycle_derivation_check.py`; and the V113→V114 byte diff.

Executed read-only checks: SHA-256 recomputation; prereg counts; prereg lint; refusal vocabulary live check/self-test; prereg trace `--check` plus independent full-column comparison; non-χ surface `--check`/self-test; domain-kinds `--check`/self-test; sweep `--check`; raise-ledger `--check`; and an in-memory string-registry reconstruction that suppressed its normal writes. No draft, spec, reference, checker, registry, or other project file was modified. The repository was already broadly dirty/untracked before this pass; this report is the sole intended write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V114
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | §6.1 L674 / spec §3d L187–195 | VERIFICATION-CLOSE.close_class is simultaneously a three-token and two-token closed vocabulary, making EXPIRED non-single-valued.
F2 | HIGH | REPAIR-REQUIRED | spec §3d L149–159 / §11 L1563 | The no-decoded-frame pass-entry precondition has no enforcing, evidentiary, or fixture contract, so the T1/hold deadlock remains a legal invisible execution.
F3 | MEDIUM | REPAIR-REQUIRED | §10 L1083–1198 / tools/prereg_trace.py L307–320 | Twenty-nine generated section cells are stale and --check verifies only row presence/result digests, not the mechanical columns the draft calls generated.
<!-- END FINDINGS-BLOCK -->
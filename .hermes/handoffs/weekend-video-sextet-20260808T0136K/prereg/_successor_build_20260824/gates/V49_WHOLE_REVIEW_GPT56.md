# V49 whole-document review — GPT56

**Verdict: NOT CLEAR.** I verified the subject SHA-256 before reading it. The new numerical-failure rule is not yet single-valued against the existing post-unblinding `VOID` rule, its claimed source inventory is false, and the document retains several byte-checkable contradictions and one non-χ allowlist hole.

## Findings

### F1 — HIGH — the non-χ access-log schema has an unconstrained per-object exfiltration field

**Draft §6.1, lines 547–550.** Lines 547–548 call the list closed, schema-defined and exhaustive and assert that none of its members can carry a per-object outcome. Line 550 nevertheless puts `object identity` and `refusal reason` together in the access-log event schema without enumerating the refusal-reason vocabulary, fixing its serialization, or requiring a verifier to reject free text or outcome-dependent values. “Never payload bytes” does not close this channel: a refusal reason such as `nonfinite`, `confidence-low`, or arbitrary text can encode an outcome bit while the artifact remains on the declared non-χ allowlist. The much tighter rule at line 553 (“no execution completion/non-finite status, no caller-authored status, and no free-form identifier”) applies to the separate acceptance-evidence projection, not to the access log.

This falsifies the universal negative in line 548 and lets a gate receive a nominally non-χ artifact carrying per-object outcome information before lock. Repair requires a closed, payload-independent refusal-code enum (or no per-object reason), canonical serialization, and an independent verifier that rejects every other value.

### F2 — HIGH — post-unblinding numerical failures are assigned both `VOID` and the new numerical outcome

**Draft §5, lines 494–498 and 506–507; §11 line 934.** The class condition correctly says a more specific named outcome wins. Lines 506–507 already make post-unblinding permutation/statistic/protocol non-finite or degenerate failures `VOID`. Yet line 498 says the post-unblinding `_finite`, `w_profile`, `sigma_ours_scalar`, and `sigma_ours_profile` failures are “genuinely unterminated and claimed by nothing” and uses them as a stated ground for adding `INCONCLUSIVE-BY-NUMERICAL-FAILURE`. The pinned source proves these are exactly the already-claimed class: `_finite` raises on a “non-finite decision quantity” (source line 1503); `w_profile` raises on degenerate `c` and a near-zero profile factor (1513, 1517); the sigma functions raise on a non-finite gradient/covariance and a negative quadratic form (1548, 1554).

Under line 494’s general precedence they must be `VOID`; under line 498’s explicit application they motivate `INCONCLUSIVE-BY-NUMERICAL-FAILURE`. Line 495 compounds the ambiguity by naming only POWER, CALIBRATION, and MISSING-ALLOCATED precedence, while §11’s per-site conversion instruction never explicitly seats the existing `VOID` claim. The rule therefore does not yet give a single checkable result for the very examples it names. Name the `VOID` antecedents explicitly in precedence, classify these sites as `VOID`, and recompute the claimed numerical-class extent after removing all integrity/protocol/VOID members.

### F3 — MEDIUM — the retracted §2.7(c) premise is still asserted one line before its retraction

**Draft §5, lines 500–501.** Line 500 says a per-object non-finite instrument output has an existing route “through §2.7’s exclusion reason (c).” Line 501 immediately says that premise was false: reason (c) is catalogue quality, and §2.7 defers instrument absence/non-finiteness to post-unblinding handling. Both sentences are current normative explanatory text. The retraction therefore does not remove the false premise; it leaves readers two opposite answers in adjacent paragraphs. Delete or correct the line-500 route claim.

### F4 — MEDIUM — the claimed exhaustive raise-site inventory does not match the pinned bytes

**Draft §5 line 497; §11 line 934; pinned `ref/successor_ref_v9.py` SHA-256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.** An AST walk of the verified bytes finds **112 `ast.Raise` nodes**, not 111:

- 68 `RuntimeError`
- 1 `ValueError`
- 39 `ManifestClosureError`
- 2 `InconclusiveByPower`
- 1 `InconclusiveByCalibration`
- 1 bare re-raise (`close_manifest`, source line 776)

The draft’s 111 is the count obtained by omitting the bare re-raise, and §11’s statement that, apart from the three typed outcome exceptions, “the rest raise a bare `RuntimeError`/`ValueError`” is false for the 39 `ManifestClosureError` sites. This is not a cosmetic type label: those closure exceptions predominantly represent digest, custody, and manifest-integrity failures that interact with the more-specific `VOID` rule in F2. Rebuild the inventory from the AST, state whether propagation sites are deliberately excluded, and classify the 39 typed closure sites rather than collapsing them into the numerical range.

### F5 — MEDIUM — the caller/run boundary is not exhaustive; unreachable defensive raises become “caller errors” without a caller violation

**Draft §5 line 496; pinned source lines 1378–1403.** The boundary says a raise that cannot fire with contract-satisfying arguments and admissible data is a caller error, and that such a failure cannot occur unless the caller violated the contract. `allocate_handcheck` line 1401 is a counterexample under the frozen production constants. Each of 9 strata needs at most `max(30, 3×10)=30`, so `total_need ≤ 270`; the frozen budget is 500. Therefore `if total_need > budget` cannot fire on the production contract. It is an unreachable defensive guard, not a caller error caused by a malformed supplied argument. The same function contains later invariant guards whose reachability is likewise distinct from both caller validation and run outcome.

The binary test therefore does not classify every raise site as claimed. Add a third `UNREACHABLE/DEFENSIVE-INVARIANT` class, require a proof under frozen constants for that classification, and require any future change that makes such a site reachable to reclassify it before execution.

### F6 — MEDIUM — the release-choice universal negative contradicts the Branch-A rule

**Draft §2.1, lines 139–155.** Lines 139–142 say the fork is bound inside this frozen text, the result “slots in” without reopening wording, and “nothing else in this document changes with the branch.” Lines 148–155 then say the normative code, geometry, counts, selection, parent, and closure are Branch-B-specific; selecting A invalidates all those pins, requires remeasurement, a new §0 pin, rerun fixtures and a fresh text gate, and is “a new preregistration in everything but name.” The latter is an appropriate fail-closed correction, but it makes the former universal claim false. Rewrite the opening rule so Branch B slots in while Branch A voids this draft and requires a successor preregistration.

### F7 — MEDIUM — the pinned predecessor decision memo is not the referenced file’s current bytes

**Draft lines 62–64.** The draft cites `DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md` at SHA-256 `b4a1f1fcaa9acbaa6b9efd3ebbe9496be8c1d83c690a012dc7a4f8520840374f`. The current file on disk at the referenced path hashes to `76cc25e5350a92d00d13eff2421ad392aec5ff2140d3b259763dd713ef352092`. The cited bytes do exist in git history (commit prefix `b202645cd5d8`), but the draft cites neither that immutable object nor a preserved path. A direct source check therefore fails. Cite the immutable commit/blob (or a preserved file whose current bytes match the pin) rather than a mutable path whose bytes have moved.

## Attacks that held

- Subject identity held: `d8a9501e0653dd84ca554e26aaacd4de87d4efb34cb6ef6266285757b96ce2bc` matched before reading and again after review.
- Pinned reference hashes held for `successor_ref_v9.py`, `closure_worker_v9.py`, and `bs2a_quality_gate.py`.
- `tools/prereg_counts.py` independently returned 16 class P / 8 class E and prose agreement.
- `tools/prereg_trace.py --check ... --self-test` returned 48 transitions, 0 problems, and all three scope controls active.
- `tools/void_registry.py --self-test` returned 6 controls, 0 failures; misconduct antecedents `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION` remain at `Any` in lines 765–767.
- `tools/prereg_lint.py` exited 0 with exactly 96 advisory legacy citations and 0 blocking findings; its self-test exercised all eight checks.
- The V43 five-step computational-rerun allowance is gone. Remaining “rerun” mentions concern Stage-P design execution, historical explanation, or explicit “no rerun” rules, not a retry after a run outcome.
- The KIMI-V11 F7 citation names the Stage-P/code-subject gap: that report says the exact-null Stage P is not implemented in the §0-pinned file and additionally identifies the receipt’s v7 subject. It is not the former F4 access finding.
- BS-3g is now on the §6.1 closed class list and has a `blocks BS-6` edge. The text honestly says the edge is still not receiptable: §11 line 937 requires a future `SLOT_SCHEMA` entry, producer, and verifier and the mapping remains open. I did not count that acknowledged DESIGN/UNFILLED state as a separate finding.

## Evidence/limits

I read the whole 938-line subject; inspected the pinned reference source and the KIMI-V11 report; recomputed hashes and raise-node/type counts; ran the four named checker families rather than accepting the brief’s outputs. I did not modify the draft, reference code, tools, reports, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V49
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 547–550 | Unconstrained per-object access-log refusal reasons defeat the asserted non-χ closed allowlist.
F2 | HIGH | REPAIR-REQUIRED | §5 lines 494–498, 506–507; §11 line 934 | Post-unblinding non-finite/degenerate failures are simultaneously claimed by VOID and the new numerical outcome.
F3 | MEDIUM | REPAIR-REQUIRED | §5 lines 500–501 | The false §2.7(c) non-finite route remains asserted immediately before its retraction.
F4 | MEDIUM | REPAIR-REQUIRED | §5 line 497; §11 line 934 | Pinned code has 112 raise nodes and 39 ManifestClosureError sites, contradicting the stated 111/RuntimeError-or-ValueError inventory.
F5 | MEDIUM | REPAIR-REQUIRED | §5 line 496; ref lines 1378–1403 | The binary caller/run boundary misclassifies unreachable defensive guards as caller errors.
F6 | MEDIUM | REPAIR-REQUIRED | §2.1 lines 139–155 | “Nothing else changes with the branch” contradicts Branch A voiding every Branch-B pin and requiring a new preregistration.
F7 | MEDIUM | REPAIR-REQUIRED | lines 62–64 | The cited predecessor memo path no longer matches its pinned SHA; only an uncited historical git object does.
<!-- END FINDINGS-BLOCK -->
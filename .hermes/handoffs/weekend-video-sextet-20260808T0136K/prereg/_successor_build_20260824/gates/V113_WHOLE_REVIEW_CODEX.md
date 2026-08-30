# V113 whole-document referee — CODEX

**VERDICT: NOT CLEAR.** The V113 bytes are the brief's pinned subject, the generated count/trace/registry checks are internally green, and several requested attacks held. The new verification-pass law does not survive its own quantization and receiptability requirements, however: its claimed one-budget release and five-gate envelope are false under the document's prescribed rounding, and its retry/expiry cap has no closed pass-attempt record from which a verifier can count the promised consecutive failures. The review-evidence preimage can also be vacuous, while the new preimage echo remains phrase-only in a way demonstrated by an in-memory counterexample. These are specification defects, not objections that the required implementation is still unfinished.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — the pass-law budget and envelope are false under the frozen rounding directions

`LIFECYCLE_GUARANTEE_SPEC.md` §3d lines 150–170 says ordinary admission resumes when the recorded arrival reading minus the recorded boundary reading is **strictly greater** than `GATE_PASS_BUDGET`, then claims a hung verifier holds admission for “at most one budget” and that cumulative wire wait is at most `5 × PASS_RETRY_MAX × GATE_PASS_BUDGET`. The governing encoding is not exact time: draft §6.1 lines 669–670 rounds ARRIVAL readings **DOWN** and boundaries/checkpoints **UP** to `g`.

Those two directions are conservative for admitting ordinary traffic, but they cost almost **2g**, not the single “quantization slack `g`” asserted at spec line 158. Concrete byte-rule counterexample with `budget=100`, `g=10`: true boundary 1 records as 10; a later reading 119 records as 110; true elapsed is 118 but recorded difference is 100, so the strict release still does not fire. It first fires in the demonstrated sample at true reading 121 (true elapsed 120). Thus one retry can hold admission for nearly `budget + 2g`, and the stated product envelope omits the same slack once per failed pass. There is no unsafe early release, but the advertised hard upper bound is wrong.

Repair the law and all dependent prose/fixtures either by budgeting the two-endpoint rounding explicitly (including strict-inequality boundary behavior) or by defining a single quantized deadline/release threshold whose claimed bound is actually derivable.

### F2 — HIGH — REPAIR-REQUIRED — pass expiry and `PASS_RETRY_MAX` are not receiptable

Spec §3d lines 159–170 says a released pass cannot commit and that `PASS_RETRY_MAX` consecutive passes that “abort or expire” refuse the gate. No closed record says that a verification pass expired, which boundary it belongs to, or which failure increments the per-gate counter. The gate pass record in draft §6.1(ii-e), line 672, is only `(gate, head_position, head_digest, verifier_digest, predecessor_record_digest, partition_cut_position, signature-enveloped)` and exists only for a PASS. The checkpoint-family set at line 674 has no pass-close record: `ATTEMPT-START/CLOSE` is the drain-member machinery, keyed by `member_position`, and `close_class` is only `{ABORTED, ABORTED-BY-RESTART}`. It cannot encode verification-pass expiry or a gate identity.

This is especially fatal on a quiet chain. The global motion-free law (spec §0b lines 28–38) bars an unrecorded wall-time predicate, while release is evidenced only once a later reading is recorded. If a verifier never returns and no ordinary arrival is appended, the chain has a boundary but no byte saying when it expired. A later boundary can be appended without a closed prior-pass outcome, and the promised “consecutive” count is not reconstructible from the declared schemas. The §11 prose/fixtures described in draft line 1553ff say “retry-cap refusal” but do not supply the missing record contract.

Add a domain-separated, clock-bearing pass-close/expiry record (gate, boundary position/digest, close cause, close reading/epoch, attempt ordinal or an equivalent recomputable join), define exactly which events increment/reset the counter, and make gate action bind the boundary it closes. Then make the verifier derive the cap from those bytes.

### F3 — MEDIUM — REPAIR-REQUIRED — the signed review’s `evidence_ref` can resolve to zero evidence

Draft §6.1 line 614 requires the evidence artifact’s canonical body only to **begin** with `(reviewed_chain_position, reviewed_event_digest)` and says everything beyond that prefix is testimony. It never requires that anything exist beyond the prefix. Therefore an artifact whose whole body is exactly the adjudicated pair passes the stated entry → record → evidence checks while containing no observation, rationale, or evidence at all. The human can still sign the disposition, but then `evidence_ref` is a decorative second pointer rather than the “evidence with a bound preimage” V113 claims to have added.

The concatenation attack did not work: one artifact beginning with pair A cannot serve review B because the verifier is said to require B’s pair at its beginning. The vacuity attack does work. Require at least one typed evidence/testimony item after the pair, with a closed schema and a nonempty rule, or delete `evidence_ref` and state honestly that the signed human disposition is the entire adjudicative basis.

### F4 — MEDIUM — REPAIR-REQUIRED — PREIMAGE-CLASS ECHO checks the words, not the source semantics

`ref/gen_string_field_registry.py` lines 488–502 accepts the spec if the literal `IDENTITY ENVELOPE` occurs anywhere, accepts the registry source note if it contains the words “identity envelope,” and rejects only the exact stale phrases `framed wire unit` or `wire-frame`. An in-memory adversarial probe returned `[]` (green) for:

- spec: `The IDENTITY ENVELOPE exists. Its normative members are now payload_hash and frame_length.`
- source note: `request_digest is sha256 over payload bytes; this value is called the identity envelope.`

That directly defeats the V113 generator-input claim without touching generated output. The seeded control at lines 504–516 proves only that one historical wording is red. The §11 verifier contract does independently require recomputation from `(origin_row, frame_sequence, operation, object_identity)`, so once that missing verifier is actually built it protects receipt values; it does **not** make this source↔spec echo semantic or prevent regeneration from publishing a false registry constraint in the meantime.

Parse and compare the exact four-member tuple and the digest operation from both source and spec, or single-source a machine-readable preimage declaration. Keep the runtime recomputation fixture as a separate defense.

### F5 — LOW — REPAIR-REQUIRED — the live vocabulary guidance still says “ninth code” in an eleven-code regime

Draft §6.1 line 594, in the current rebuilt principle rather than a historical tombstone, says: “An editor proposing a **ninth code** must satisfy this test.” The operative block immediately below (lines 595–600) declares eleven codes. `tools/refusal_vocabulary_check.py` is green because it verifies token membership and the catch-all machinery, not this ordinal prose. This is exactly the stale-count guidance the generated count discipline was meant to eliminate. Replace “ninth” with “new” or “additional”; do not hand-maintain an ordinal here.

## Failed attacks / repairs that held

- **Subject identity held.** SHA-256 recomputed to `8a04e549e4a25315d2eec2440d7f3eba3c08a5ea85e7314a12989361bd573e7d` before the draft was read.
- **Counts held.** `tools/prereg_counts.py` recomputed **16 class P / 9 class E** and reported that prose matches the table. The generated V86→V87 count-move row is present at draft line 1119.
- **Lifecycle derivation held for what it actually binds.** Spec SHA-256 is `a55fb969c508439cad2ccfb4ac192d221f39b38a206435c9d8a8d3a4a49f4850`; `lifecycle_derivation_check.py` reported 0 problems and its 11 controls all fired. F1/F2 attack new §3d semantics, not a stale digest or divergent quote.
- **Generated surfaces held byte equality.** `gen_nonchi_surface.py ... --check` reported byte-equal with 0 problems and 6/6 controls; `gen_domain_kinds.py ... --check` reported byte-equal/all sites covered and 3/3 controls.
- **Refusal vocabulary token set held.** The required repo-root `tools/refusal_vocabulary_check.py` reported 0 problems; self-test reported 43 controls, 0 failures, every code controlled. The known identity leak and availability-code issue remain parked and were not re-counted.
- **Raise-site explicit inventory held.** Frozen `ref/successor_ref_v9.py` SHA-256 is `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; independent AST enumeration found 112 `Raise` nodes and 1 `Assert`, with exception-type counts exactly 68 RuntimeError, 39 ManifestClosureError, 2 InconclusiveByPower, 1 ValueError, 1 InconclusiveByCalibration, 1 bare re-raise. `ref/RAISE_SITE_CLASSIFICATION.md` has 113 unique explicit rows.
- **Request-key attacks held within the declared anchor residue.** The key is the arrival position; the contract requires per-row strictly increasing `frame_sequence`, recomputes `request_digest` with `origin_row = row`, rejects terminals without arrivals and two terminals per key, and openly scopes uniqueness to external anchors. I found no new key/join escape beyond the parked inter-anchor rollback residue.
- **Two-body domain separation held under ordinary endings.** The terminated and completed review bodies have distinct kinds and distinct first fields; the completed body’s disclosure-record digest binding is mutual with the recomputed chain head, not self-reference to the review signature. A pre-lock terminated run cannot lawfully resume and later lock because drain-start permanently closes ordinary admission.
- **Evidence concatenation attack failed.** One evidence artifact cannot adjudicate two different pairs because only the first pair is at byte zero. F3 is the narrower exact-pair vacuity.
- **Predecessor-list duty is stated honestly.** Draft line 605 makes the same-parent successor list every prior preregistration and says its own gate rounds check the lane; it also admits this document cannot enforce a future document. That is an honest process boundary, not a hidden guarantee.
- **Grid draw discipline not re-attacked.** Per the brief’s later controlling instruction, the frozen/pending draw-discipline object was not counted as a finding.

## Evidence ledger and scope

Read content: `gates/BRIEF_V113_REVIEW.md` first; then the hash-verified V113 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/successor_ref_v9.py` by AST; `ref/gen_string_field_registry.py`; repo-root `tools/refusal_vocabulary_check.py`; and the generated/checker surfaces named above. Read-only checks also included `prereg_lint.py` (97 legacy advisories, 0 blocking), `prereg_trace.py` (112 transitions, 0 problems; 3/3 scope controls), and `void_registry.py` (60 antecedents; self-test 6 controls, 0 failures). No draft/reference/tool bytes were modified. The repository was already broadly dirty/untracked outside this report; those pre-existing paths were not touched.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V113
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §3d lines 150-170; draft §6.1 lines 669-670 | Opposite endpoint rounding adds nearly 2g, falsifying the one-budget release and five-gate wait envelope.
F2 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §3d lines 159-170; draft §6.1 lines 672, 674 | No closed pass-expiry/close record makes PASS_RETRY_MAX consecutive failures recomputable from chain bytes.
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 line 614 | An evidence artifact exactly equal to the adjudicated pair passes while containing no evidence.
F4 | MEDIUM | REPAIR-REQUIRED | ref/gen_string_field_registry.py lines 488-516 | PREIMAGE-CLASS ECHO is defeated by semantic drift that retains its two trigger phrases.
F5 | LOW | REPAIR-REQUIRED | §6.1 line 594 | Live eleven-code guidance still calls an added member a ninth code.
<!-- END FINDINGS-BLOCK -->

# CODEX — V72 whole-document adversarial review

**VERDICT: NOT CLEAR.** The required subject SHA-256 matched before the draft was read. The literal G1–G5/N1–N3 quote block now matches the companion spec, but the claimed derivation predicate is still defeatable and the draft has already diverged in unlabelled lifecycle prose. The global string rule does not reach existing arbitrary-byte receipt fields. The BS-3g reduction still contains a scalar-baseline clause that contradicts the repaired within-draw rule. The disposition verifier does not establish that a cited re-derivation names the joined failure, and the refusal checker still admits an active twelfth code under negated retirement wording.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — The scalar-baseline rule survived the within-draw repair

V72 §11 lines 1275–1282 defines the repaired rule: `HELD` iff every `verdict(i,j)` equals that draw's own `verdict(i,0)`; if the gamma-zero column varies, `baseline_verdict` is the literal `PER-DRAW`. Verifier clause (e) at lines 1351–1356 now enforces that within-draw predicate.

But lines 1328–1332 still define the categorical reduction as `HELD` iff **every cell equals `baseline_verdict`**. These functions disagree whenever the zero column varies across draws. Counterexample: draw 1 is `INCONCLUSIVE` at every gamma and draw 2 is `REJECTED-AT-LONGO-AMPLITUDE` at every gamma. The within-draw rule requires `HELD` and `baseline_verdict = PER-DRAW`; the surviving scalar clause requires every verdict token to equal the literal `PER-DRAW`, so it requires `FAILED`. The brief says both scalar clauses were repaired; one remains.

### F2 — HIGH — REPAIR-REQUIRED — The global string rule is false for already-authorised non-chi slot receipts

Draft §6.1 lines 586–588 declares `SLOT_SCHEMA` receipts non-chi-bearing and exhaustive; lines 662–672 impose the global rule that every string field in every non-chi artifact is closed-vocabulary or bounded-encoding, with no third kind. The pinned implementation contradicts that claim. `ref/successor_ref_v9.py` lines 185–205 defines fields including BS-1b `provenance`, BS-8p `hc_rules_quotation`, and BS-9 `runner_prohibition`; `receipt()` at lines 208–224 checks only non-emptiness and exact field names, then serializes arbitrary byte payloads.

I executed the pinned bytes with payload `object=10997315463551936 chi=+1 free prose`. BS-1b, BS-8p, and BS-9 were all accepted and canonical envelopes were emitted. Calling these payloads bytes rather than strings is exactly the “field someone would not call a string” escape the brief asks to test. The planned `receipt_strict()` repair at lines 1148–1151 still checks slot membership and field-set equality, not value domains, so it does not close this channel. An existing non-chi receipt can therefore carry arbitrary prose or an object-indexed chi payload while satisfying its frozen schema.

### F3 — HIGH — REPAIR-REQUIRED — The derivation check misses a lifecycle divergence already present in V72

The companion spec §5 lines 101–111 ends a view at the first of position advance, interface clear, or **any interruption of continuous display**, including visibility loss, blanking, occlusion, or navigation away; nothing displayed after interruption is the same view. V72's unlabelled operational restatement at §6.1 line 652 says a session ends when “position advanced or interface cleared” and omits the new interruption boundary. Minimise or occlude the interface and restore it without advancing or clearing: the spec requires a new render commit, while the draft's restatement preserves the old two-ender reading.

`tools/lifecycle_derivation_check.py` cannot detect this. Its own lines 17–23 limit inspection to labelled `G… —`/`N… —` fragments and admit that unlabelled paraphrases are invisible. Worse, lines 55–59 test each found body as a substring anywhere in the whole normalized spec, not against the corresponding label, and line 19 explicitly permits fewer quotes. In-memory attacks against the exact V72/spec bytes produced zero problems after (a) deleting all eight labelled quote lines and (b) replacing the G1 body with the exact G2 body while retaining the G1 label. `tools/prereg_lint.py` contains no lifecycle-check invocation, so the separate predicate is not wired into the lint whose green result the brief reports. The draft's line-622 claim that this class of finding is now impossible is false in both mechanism and current bytes.

### F4 — HIGH — REPAIR-REQUIRED — `NAMED-AS-DEFECT` verifies that a revision exists, not that it names the joined failure

Draft §6.1 line 601 requires a `NAMED-AS-DEFECT` entry to carry the digest of a re-derived vocabulary revision “that names this class”; line 602 strengthens that to naming every distinct failure found under the coarse `(row, operation)` key. But the exact enumeration-verifier build contract at §11 lines 1385–1395 requires only “resolution” of each re-derivation digest. It defines no canonical vocabulary-revision schema, no authenticated mapping from `(chain_position,event_digest)` or `class_key` to newly defined code(s), and no content predicate proving that the resolved revision names the joined failure(s).

A digest of an existing but irrelevant vocabulary revision therefore resolves and authenticates perfectly while naming nothing about the emission. The entry can pass the stated join/signature checks and discharge as `NAMED-AS-DEFECT`, defeating the disposition binding the brief explicitly asks to attack. “The revision exists” is not “the revision names this failure.”

### F5 — HIGH — REPAIR-REQUIRED — The explanation surface still has compositional byte channels outside the five-cause vocabulary

Line 610 redesigns the explanation as one of five `cause` tokens plus “bounded numeric parameters (durations, counts)” and a detached signature. It does not enumerate the numeric field set per cause, their ranges, cardinality, ordering, or serialization; `explanation_ref` is only called an identifier, with no declared set or bound. An arbitrary-length sequence of individually bounded counts (for example 0/1) carries an arbitrary bitstring while every element remains in range. The detached signature is likewise admitted as non-chi at line 659, but no signature algorithm, canonical signature encoding, fixed length, or deterministic signing rule is specified; a randomized signature nonce can carry chosen bits while verifying under the provisioned key.

This defeats lines 662–672's “no third kind” rule without adding a sixth cause or free prose. Cause membership and per-value bounds do not bound composition. The explanation schema must have a fixed field set and cardinality per cause, exact numeric ranges and canonical encoding, a bounded `explanation_ref`, and a fixed deterministic signature representation (or signatures must be excluded from the non-chi payload claim).

### F6 — MEDIUM — REPAIR-REQUIRED — The refusal-vocabulary checker exempts active illegal codes under negated retirement prose

`tools/refusal_vocabulary_check.py` lines 115–129 treats a non-member `REFUSED-*` token as legal whenever the same line contains any retirement word matched by `deleted|merged|retired|superseded|GONE|does not survive`. It does not parse negation. Against the exact V72 text, I appended each of these in memory:

- `Active member REFUSED-EVADE is not retired.`
- `REFUSED-EVADE survives; it was never deleted.`

`check()` returned `[]` for both. Thus an active twelfth member can evade R01 while the checker reports zero problems. This directly defeats the checker's lines 115–118 claim that members are parsed independently of Markdown and only genuine retirement mentions are exempt. Add positive retirement grammar or, safer, require retired mentions to be drawn from the explicit `RETIRED` map and reject every other token unconditionally.

### F7 — MEDIUM — REPAIR-REQUIRED — `NOT-EVALUATED` is admitted as a valid BS-3g record but has no conforming domain

V72 lines 1248–1251 admits `NOT-EVALUATED`; verifier clause (f), lines 1357–1359, calls it a valid non-discharging record; clause (g), lines 1360–1364, allows it only when zero cells were evaluated. But lines 1335–1338 require both `n_draws` and `n_perturbations` in `[1, 10^6]`, lines 1323–1327 define the matrix as their product, and lines 1351–1353 require the verifier to regenerate all draws and reject evaluated-count disagreement in either direction. The minimum conforming matrix has one cell, while `NOT-EVALUATED` requires zero.

The token is therefore unreachable under the same schema that declares it valid. Either define a zero-evaluation receipt shape with zero counts and no matrix digest, or remove `NOT-EVALUATED`; a valid state that no canonical receipt can represent is not a total outcome contract.

### F8 — LOW — REPAIR-REQUIRED — The raise-classification reference still contradicts its own L986 disposition

`ref/RAISE_SITE_CLASSIFICATION.md` line 9 first correctly says L963/L973 are `CALLER` and L986 is `PLANNING-INTERNAL`, then says “They are moved rather than deleted: **each is a setup error against a caller-supplied l_plan**,” and immediately says L986 is not an error in any supplied argument because `MOVE_CAP` is an internal frozen constant. The table at lines 80–82 and draft §5 line 503 use the latter reading.

The arithmetic inventory is sound, but the human classification record gives opposite semantic reasons for L986 in the same paragraph. Delete the “each” sentence or scope it to L963/L973; the referenced ground-truth file should not contradict the class it asks reviewers to trust.

## Failed attacks / checks that held

- Subject identity held before reading: `66fcc42c6de59cfd8b19397f5bc482f80391fc04f75926cf04b41281ea928979`.
- Companion and pinned implementation identities held: lifecycle spec `1c499dbcb9be30f959722dc76b84379da25c6842e640321ca9e1e1adf2a8df3c`; `successor_ref_v9.py` `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`; refusal checker `a3f64aef6e7b9d2e2e9f70449e320b1430579529f928a13ac67446724d24a422`.
- The exact V72 quote bodies G1–G5/N1–N3 do match the exact spec today. F3 concerns the contradictory unlabelled restatement and a checker that does not preserve that fact under revision.
- `prereg_lint.py`: exit 0, 97 advisory legacy citations, 0 blocking. Per the brief, none is reported as unresolved.
- `prereg_counts.py`: 16 class P / 8 class E, prose matched.
- `prereg_trace.py --check`: 71 transitions, 0 problems.
- `void_registry.py --self-test`: 6 controls, 0 failures.
- Refusal checker: exact V72 returned 0 problems; self-test returned 20 controls, 0 failures. F6 is an adversarial control absent from that suite.
- Lifecycle checker: exact V72 returned 0 problems; self-test returned 4 controls, 0 failures. F3 is demonstrated by two adversarial mutations absent from that suite.
- Independent AST recount found 112 raises. The classification table closes arithmetically: 25 CALLER + 60 INTEGRITY + 20 NUMERICAL + 3 PLANNING-INTERNAL + 1 TYPED-OUTCOME + 3 WRAPPER = 112. I did not re-find the parked per-raise-versus-call-site defect.
- The V72 signer repair does bind enumeration entries to a canonical body, a named signer, and the BS-2k-provisioned key. F5 concerns the still-unbounded signature/parameter representation as a non-chi channel, not the repaired trust root.
- The five-cause rule honestly sends an inexpressible novel cause to `NAMED-AS-DEFECT`; I did not count vocabulary smallness itself as a defect.
- The manifest now requires both endpoints, zero via the baseline requirement, at least three distinct values, no out-of-bound values, and frozen maximum spacing. The known finite-grid limitation is stated honestly and was not re-found.
- I did not re-find parked issues: the availability-code/object-identity leak, durable pre-verdict state, VOID partition, strata/producer question, BS-3g lifecycle cycle, `REFUSED-INTEGRITY-MISMATCH`, `require_authorization`, freeze-signature residue, or the per-call-site classification unit.

## Evidence and write scope

Content read: the controlling V72 brief first; exact V72 only after digest verification; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; and both V71 referee reports to distinguish repairs from re-findings. All adversarial mutations were in memory. Only this CODEX report was written.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V72
VERDICT: NOT CLEAR
COUNT: 8
F1 | HIGH | REPAIR-REQUIRED | §11 lines 1275–1282, 1328–1332, 1351–1356 | A surviving scalar-baseline clause contradicts the repaired within-draw HELD predicate whenever the gamma-zero verdict varies across draws.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 586–588, 662–672; ref/successor_ref_v9.py lines 185–224; §11 lines 1148–1151 | Existing non-chi slot receipts accept arbitrary byte prose and object-indexed chi payloads because schemas constrain names, not value domains.
F3 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §5 lines 101–111; §6.1 line 652; tools/lifecycle_derivation_check.py lines 17–23, 55–59 | The draft omits the interruption view boundary in unlabelled prose, and the checker passes deleted or label-swapped invariant quotes.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 601–602, 610; §11 lines 1385–1395 | A re-derivation digest is only resolved; no verifier predicate proves the referenced revision names the joined failure or every failure under the coarse key.
F5 | HIGH | REPAIR-REQUIRED | §6.1 lines 610, 659, 662–672 | Unfixed numeric-parameter composition, explanation identifiers, and signature encodings remain covert channels while satisfying the five-cause vocabulary.
F6 | MEDIUM | REPAIR-REQUIRED | tools/refusal_vocabulary_check.py lines 115–129 | Negated retirement wording exempts an active illegal REFUSED-* token, so a twelfth code passes R01.
F7 | MEDIUM | REPAIR-REQUIRED | §11 lines 1248–1251, 1323–1327, 1335–1338, 1351–1364 | NOT-EVALUATED requires zero cells but the canonical schema and count-closure rules require at least one.
F8 | LOW | REPAIR-REQUIRED | ref/RAISE_SITE_CLASSIFICATION.md line 9 and lines 80–82; §5 line 503 | The classification reference calls L986 both a caller-supplied setup error and an internal-constant failure in the same paragraph.
<!-- END FINDINGS-BLOCK -->
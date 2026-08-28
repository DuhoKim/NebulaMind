# BS-2a CODE GATE — CODEX

Verdict: **NOT CLEAR**. The pinned subject bytes and the real build run reproduce the claimed 49,211-row result, and the source-join builder refuses the adversarial duplicate/orphan/missing-row cases. However, `verify_receipt()` accepts false partition evidence, accepts duplicate object identities and a false parent count, and permits χ-bearing data inside a nested receipt field. The self-test also remains green when substantive checks are deleted. Those are code-gate blockers for an authenticated, closed receipt/evidence contract.

## Identity and frozen-contract comparison

- Reviewed file: `ref/bs2a_quality_gate.py`.
- Independently computed sha256: `4e205c67d7efc72a0432b8ac4d7ddeb0f6514d01c21f791011eb6427ab2d2c62`.
- Brief-pinned sha256: `4e205c67d7efc72a0432b8ac4d7ddeb0f6514d01c21f791011eb6427ab2d2c62`.
- Comparison: **MATCH, byte for byte at the sha256 identity level**.
- The constants at `bs2a_quality_gate.py:54-61` match the governing document `PREREG_SUCCESSOR_DRAFT_V29_20260827.md:372-382`: `flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, `nobs_r >= 3`, quality sha256 `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`, parent sha256 `425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831`, parent N 65,060, and realised retained N 49,211. The code's `3.0` is numerically the document's `3`.
- `successor_ref_v9.py` sha256 during the review was `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; no review action wrote that file.

## Numbered findings

### 1. HIGH — the closed receipt schema can carry χ and still pass

- File/lines: `ref/bs2a_quality_gate.py:219-240`, especially `235-240`.
- Executed attack: starting from `_sample_evidence()`, I inserted `receipt["thresholds"]["chi_net"] = 0.731` and called `verify_receipt()`.
- Observed verifier output: `[]` (accepted).
- Why it fails: the outer receipt key set is closed, but the nested `thresholds` object is not. The verifier checks only the three required entries with `t.get(name)` and never rejects extra nested keys. Thus a receipt can carry a field that leaks χ despite the claimed non-χ-bearing closed schema.
- Smallest sufficient repair: require `type(thresholds) is dict` and exact key equality with `{flux_ivar_r_gt, psfsize_r_lt, nobs_r_ge}` before comparing values. Apply the same recursively closed/type-checked rule to every structured field, and add a nested-χ negative control.

### 2. HIGH — the verifier accepts evidence whose asserted partition the predicate does not support

- File/lines: `ref/bs2a_quality_gate.py:245-259` and `198-206`.
- Executed attack: changed the first passing evidence row's stored `quality_pass` from `True` to `False`, recomputed the receipt's `evidence_sha256`, and left the receipt counts equal to the values recomputed from the three numeric columns.
- Observed verifier output: `[]` (accepted).
- Why it fails: `verify_receipt()` recomputes only the aggregate retained count from numeric values. It never checks each stored `e["quality_pass"]` against `quality_pass(...)`. `evidence_digest()` faithfully binds the false bit, so digest agreement does not repair the semantic contradiction. A consumer using the receipted per-row bit can therefore obtain a different partition from the verifier's aggregate.
- Smallest sufficient repair: for every row, require `type(quality_pass) is bool` and exact identity with the predicate recomputed from validated finite numeric fields; reject on the first mismatch. Derive both the digest and aggregate counts only after this row-level validation. Add a control that flips only the stored bit and updates the digest.

### 3. HIGH — parent identity and one-to-one closure are enforced only by the builder, not by the receipt verifier

- File/lines: `ref/bs2a_quality_gate.py:211-261`, especially the absence of checks for `n_parent` and evidence-key uniqueness.
- Executed attacks:
  1. Set `n_parent = 999999` on an otherwise conforming fixture: verifier output `[]`.
  2. Appended a duplicate passing evidence row with the same `(brickid,objid)`, adjusted `n_parent`, `n_joined`, `n_retained`, `n_excluded`, and the digest consistently: verifier output `[]`.
- Why it fails: `n_parent` is a required receipt field but is never validated; `n_joined` is compared only with list length; evidence keys are never checked for uniqueness; and no check enforces `n_parent == PARENT_ROWS == n_joined`. Consequently, `verify_receipt()` accepts a receipt that asserts a false parent population and a non-one-to-one evidence partition.
- Smallest sufficient repair: require `n_parent == PARENT_ROWS`, `n_joined == n_parent`, all count fields to be exact non-negative integers (not booleans), and exact uniqueness of normalized `(brickid,objid)` evidence keys. If standalone verification is intended to establish exact parent membership rather than only cardinality, supply the authenticated parent key set/bytes and require set equality.

### 4. HIGH — self-test controls are vacuous for deleted checks and one control passes for the wrong reason

- File/lines: `ref/bs2a_quality_gate.py:291-356`.
- Executed deletion probes on temporary copies only:
  1. Deleted the parent-source digest comparison at lines 232-233. `--self-test` still reported `7 controls, 0 failure(s)` because no control mutates `parent_source_sha256`.
  2. Deleted the retained-count-versus-predicate comparison at lines 250-253. `--self-test` still reported `7 controls, 0 failure(s)`. The `retained count inflated` control was rejected by the unrelated partition-sum check because `_c_count` changes `n_retained` from 1 to 3 without changing `n_excluded`.
  3. As a positive calibration, deleting the evidence-row schema check made the χ-row control report `ACCEPTED, control is silent` and the self-test exit 1.
- Why it fails: the module says every check ships a negative control and that controls prove each check can fail (`lines 36-40, 264, 337-338`). In fact, schema version, parent digest, join keys, joined count, and other individual branches have no isolated controls; `self_test()` asks only whether *any* refusal occurred and does not assert the expected refusal reason. A different guard can therefore mask deletion of the intended guard.
- Smallest sufficient repair: provide one isolated mutation per individual invariant and assert the exact expected refusal code/reason, not merely `bool(out)`. Make each mutation preserve all unrelated invariants; specifically, the retained-count control must adjust `n_excluded` so the partition still sums while the recomputation check alone must reject it.

### 5. MEDIUM — `evidence_digest()` is not an unambiguous encoding of evidence rows

- File/lines: `ref/bs2a_quality_gate.py:198-206`.
- Executed attack: one evidence row with `(brickid="a|b", objid="c")` and another with `(brickid="a", objid="b|c")`, all other fields equal, produced the same digest because both serialize to the same pipe-delimited line.
- Observed result: `DIGEST delimiter collision: True`.
- Why it fails: this is a structural serialization collision, not a SHA-256 collision. The verifier does not constrain identifiers to a delimiter-safe grammar, so the digest does not uniquely bind the field boundaries it claims to bind. Embedded newlines create an analogous row-boundary risk.
- Smallest sufficient repair: hash a canonical, length-delimited representation (for example canonical JSON arrays with explicit types and separators) after strict identifier/type validation. Retain sorting by the validated key for order independence and reject duplicate keys before hashing.

## Executed verification and failed attacks

- Exact self-test invocation: `python3 ref/bs2a_quality_gate.py --self-test` exited 0 and printed `7 controls, 0 failure(s)`.
- Exact real invocation: `python3 ref/bs2a_quality_gate.py --acquire acquire` exited 0 and independently printed `n_parent=65060`, `n_joined=65060`, `n_retained=49211`, `n_excluded=15849`, evidence sha256 `1f3b9b05e52693ade626663c522a7a6b5aa52263553acf249553abe7bb0dfc1a`, and `retained 49,211 of 65,060 (expected 49,211) — MATCH`.
- Join attacks that held: duplicate parent key refused; duplicate quality key refused; parent without quality refused; quality orphan refused; and a missing parent row refused on the parent row-count invariant. These were constructed synthetic inputs supplied in-memory; no external data tree was read.
- `verified_bytes()` held the custody-boundary review. It performs one `os.open` with `O_NOFOLLOW`/`O_NONBLOCK`, checks the opened descriptor with `fstat`, hashes exactly the bytes read from that descriptor, and returns those same bytes for parsing (`lines 87-116, 140-141`). This matches the relevant v9 single-open/same-bytes pattern at `successor_ref_v9.py:419-467`; no verify-then-reopen path was found.
- Digest behavior that held: reversing evidence row order left the digest unchanged; mutating `flux_ivar_r` from `50.0` to `50.25` changed it.
- Claim-boundary review held: the module consistently claims only outcome-blindness with respect to this study's unobserved χ and expressly disclaims statistical independence from handedness (`lines 21-32`). No stronger claim was found in executable paths or comments.
- `successor_ref_v9.py` was not imported, called, or modified by the reviewed module; the only references in `bs2a_quality_gate.py` are explanatory docstring text at lines 6 and 90-92.

## Testimony

None. All verdict-bearing assertions above were executed or grounded in the named source lines. I did not read `/Users/duhokim/NebulaMindData/`.

## Scope and standing-state consequence

This review does not fill BS-2a, authorise a fetch, or establish independence from handedness conditional on position. With findings 1-4 open, BS-2a remains UNFILLED and BS-2f, BS-6, and the first image byte remain blocked.

**NOT CLEAR**
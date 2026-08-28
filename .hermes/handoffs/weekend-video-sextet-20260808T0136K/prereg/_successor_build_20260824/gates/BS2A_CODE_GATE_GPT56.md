# BS-2a CODE GATE — GPT56, round 2

Verdict: **NOT CLEAR**. The pinned subject reproduces the real 49,211/65,060 result, the rebuilt battery reports 17 controls with zero failures, and the requested parent-digest deletion probe now fails by naming the intended silent control. However, isolated deletion probes show that three closure checks can still be deleted while the battery stays green for a surviving check's reason. Independently, the verifier accepts evidence with a forged parent member, accepts an entirely foreign all-pass partition, and still accepts χ in the nested thresholds object.

## Identity and required executions

- Subject reviewed: `../ref/bs2a_quality_gate.py`.
- Brief-pinned sha256: `d7da1568dc294595640b603368135df288ac4bbc0cc54003a1fc906e237e650c`.
- Independently computed sha256: `d7da1568dc294595640b603368135df288ac4bbc0cc54003a1fc906e237e650c`.
- Comparison: **MATCH** — the reviewed bytes are the bytes pinned by the brief.
- `python3 ref/bs2a_quality_gate.py --self-test` exited 0 and independently printed `self-test: 17 controls, 0 failure(s)`.
- `python3 ref/bs2a_quality_gate.py --acquire acquire` exited 0 and independently produced `n_parent=65060`, `n_joined=65060`, `n_retained=49211`, `n_excluded=15849`, evidence sha256 `0afba44f99a49802713d357c6684315551ddcd3681ad87457fe0c96118fe32ca`, and `retained 49,211 of 65,060 (expected 49,211) — MATCH`.

## Numbered findings

### 1. BLOCKER — the verifier does not establish parent membership or bind evidence to the asserted source

- File/lines: `../ref/bs2a_quality_gate.py:231-234, 283-304`.
- Executed refusal attack: starting from `_sample_evidence()`, I changed one unique evidence key to `FORGED_PARENT_KEY_NOT_IN_SOURCE`, recomputed `evidence_sha256`, and changed nothing else. `verify_receipt()` returned `[]`: **ACCEPTED**.
- Stronger executed calibration: I changed every evidence row to predicate-passing values, set all `quality_pass` bits true, set `n_retained=65060` and `n_excluded=0`, and recomputed the evidence digest. The receipt continued to assert the frozen parent and quality source digests. `verify_receipt()` again returned `[]`: **ACCEPTED**.
- Why it fails: the verifier checks that `parent_source_sha256` contains the expected literal, that the list has 65,060 unique keys, and that counts close. It never consumes authenticated parent bytes or an authenticated parent-key-set commitment, so it cannot tell the real parent set from an equally sized foreign set. Likewise, the quality-source digest in a hand-made receipt is an assertion, not a binding from source rows to evidence values. This contradicts the module-level claim that the verifier can reject a non-conforming authenticated receipt/evidence pair.
- Smallest sufficient repair: make standalone verification consume the already-authenticated parent and quality bytes (or separately frozen canonical key/value commitments), derive their key/value maps, and require exact key-set equality plus per-key equality to the evidence before accepting. Add a control that replaces one unique parent key while preserving size, uniqueness, counts, predicate agreement, and digest.

### 2. HIGH — the closed receipt schema still accepts χ in a nested field

- File/lines: `../ref/bs2a_quality_gate.py:66-77, 220-241`.
- Executed attack: inserted `receipt["thresholds"]["chi_net"] = 0.731` into an otherwise conforming fixture. `verify_receipt()` returned `[]`: **ACCEPTED**.
- Why it fails: top-level receipt keys are closed, but `thresholds` is checked only by three `.get()` calls. Extra nested keys are never rejected. Thus the claimed closed schema can carry the very outcome field it is intended to exclude. None of the 17 controls exercises recursive receipt closure.
- Smallest sufficient repair: require `type(thresholds) is dict` and exact nested key equality with `{"flux_ivar_r_gt", "psfsize_r_lt", "nobs_r_ge"}` before comparing values; type-check `join_keys` similarly; add a nested-χ control whose expected refusal identifies nested schema closure.

### 3. HIGH — three check deletions are still masked by surviving guards

- File/lines: `../ref/bs2a_quality_gate.py:285-300, 376-395, 454-501`.
- Intact-control isolation audit:
  - `parent identity wrong` produces **two** refusals: the frozen-parent check and the unrelated join-totality check.
  - `joined count wrong` produces **two** refusals: joined-vs-parent and joined-vs-evidence-length.
  - `non-boolean quality_pass` also produces two refusals: non-boolean plus retained-count mismatch.
- Executed deletion probes on temporary copies:
  1. Deleted only `n_parent != PARENT_ROWS`. The battery exited 0 with `17 controls, 0 failure(s)`; `parent identity wrong` remained `OK` on `n_joined 65060 != n_parent 65059`.
  2. Deleted only joined-vs-parent totality. The battery exited 0; `joined count wrong` remained `OK` on `n_joined 65061 but evidence holds 65060`.
  3. Deleted only joined-vs-evidence length. The battery exited 0; `joined count wrong` remained `OK` on `n_joined 65061 != n_parent 65060`.
- Why it fails: expected substrings are not unique refusal identities. `n_parent` and `n_joined` occur in multiple branches, and the mutators violate multiple invariants. The rebuilt battery therefore still allows a control to pass for the wrong reason — the exact round-1 defect it claims to eliminate.
- Smallest sufficient repair: assign stable, unique refusal codes to individual invariants and make every control require exactly its one code and no other refusal. Isolate parent identity by constructing a 65,059-row closed evidence/receipt pair before applying only the frozen-size mismatch; split the two joined invariants into separate controls with unrelated invariants preserved; repair the non-boolean mutator so its count remains consistent under the verifier's recomputation policy.

### 4. HIGH — the frozen expected retained count is display-only, not a gate invariant

- File/lines: `../ref/bs2a_quality_gate.py:61, 295-304, 523-532`.
- Executed attack: the all-pass 65,060-row evidence described in finding 1 had exact per-row predicate agreement, closed counts, and a recomputed evidence digest. Despite `EXPECTED_RETAINED = 49_211`, `verify_receipt()` returned `[]` with `n_retained=65060`.
- Why it fails: the verifier checks only evidence self-consistency. `main()` prints `MATCH` or `MISMATCH`, but a mismatch is not added to `bad` and does not cause a nonzero exit. The 17 controls contain no expected-retained control. A gate process can therefore succeed while explicitly printing `MISMATCH`.
- Smallest sufficient repair: require `receipt["n_retained"] == EXPECTED_RETAINED` (and therefore the corresponding expected exclusion count) for this frozen production contract, make `main()` return nonzero on `MISMATCH`, and add an isolated control that changes an evidence row and its bit/counts/digest consistently while leaving all other invariants valid.

## Deletion-probe results that held

All deletions below were made only in temporary copies under the assigned gates directory.

- Requested parent-digest deletion: exit 1; exact control line was `FAIL parent digest wrong: ACCEPTED, control is silent`; summary `17 controls, 1 failure(s)`. This confirms the rebuilt battery names the specific silent control.
- Retained-count comparison deletion: exit 1; `FAIL retained count inflated: ACCEPTED, control is silent`.
- Duplicate-key comparison deletion: exit 1; `FAIL duplicate evidence key: ACCEPTED, control is silent`.
- Off-schema comparison deletion: exit 1; `FAIL late row carries χ: ACCEPTED, control is silent`.

These successful calibrations make finding 3 narrower, not weaker: most repaired controls identify their deleted branch, but the parent-identity and joined-count controls do not.

## Fixture and production-path assessment

- `_sample_evidence()` creates exactly 65,060 rows; its intact receipt passes cleanly.
- `self_test()` and production `main()` both call the same `verify_receipt()` function. There is no fixture flag, fixture exception, alternate threshold, or weakened parent-size branch. The requested concern about relaxing parent identity for fixtures therefore held under attack.
- The fixture does bypass `verified_bytes()` and `build_evidence()` by construction, so it is a verifier fixture rather than an end-to-end acquisition fixture. The separate real `--acquire acquire` execution exercised those production stages and reproduced the frozen counts.

## Other failed attacks / boundaries that held

- Each of the 17 intact controls produced its named expected substring; 14 produced a single refusal. The three multi-refusal exceptions are identified in finding 3.
- Schema version, both source-digest literals, thresholds, join-key declaration, partition sum, evidence digest, extra/missing top-level receipt fields, late-row off-schema evidence, per-row predicate disagreement, non-finite values, and duplicate evidence keys all refused under their intact controls.
- The length-prefixed field encoding repaired the round-1 `|` field-boundary collision.
- The module consistently limits its claim to outcome-blindness with respect to this study's unobserved χ and expressly disclaims statistical independence from handedness and conditional-on-position independence (`lines 21-32`). I found no stronger claim in code or comments.
- `successor_ref_v9.py` is mentioned only in explanatory text; the reviewed module does not import, open, call, or write it. Its sha256 was unchanged before and after the review/report write: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.

## Testimony, scope, and custody

No verdict-bearing assertion above is testimony: the digest, required invocations, acceptance attacks, refusal sets, and deletion probes were executed. I did not read `/Users/duhokim/NebulaMindData/`. Temporary deletion copies were confined to the assigned gates directory. This review does not fill BS-2a, authorise a fetch, or resolve conditional independence. BS-2a remains UNFILLED; BS-6 and the first image byte remain blocked.

**NOT CLEAR**
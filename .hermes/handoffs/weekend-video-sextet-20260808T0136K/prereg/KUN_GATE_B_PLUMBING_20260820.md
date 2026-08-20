PASS_PLUMBING_FIXES

# KUN_GATE_B_PLUMBING_20260820 — kimi gate seat (Nous route), fresh one-shot

Scope: the six plumbing fixes in GPT2_PLUMBING_DONE.md (F2,F3,F4,F5,F7,F8). The
preregistration amendment was NOT gated here and AMENDMENT_PREK8_20260820.md was not
read, per the kickoff. Method: local files, grep, python3; tests run; no network.
Gated tree: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg

Build identities re-hashed at gate: all six MATCH the receipt (inference_runner.py,
committee.py, committee_state_vocabulary.py, tensor_to_png.py, nm_handcheck.py,
RUN_ENVIRONMENTS.md).

## 0. CRITICAL BOUNDARY CHECK — CLEAN

Method: git diff of exactly the plumbing-touched files (M: _committee_20260820/committee.py,
_committee_20260820/test_committee.py, _inference_20260820/inference_runner.py,
_inference_20260820/test_inference_runner.py, handcheck/nm_handcheck.py,
handcheck/test_nm_handcheck.py; new: RUN_ENVIRONMENTS.md, committee_state_vocabulary.py,
test_committee_state_vocabulary.py, test_run_environments.py, display/, run_*_stage.sh),
grepped for smoothing / prior estimator / sparse-cell policy / floor change / strata-count
change / Neyman / Jeffreys / shrinkage / pseudocount terms.

Findings:
- No smoothing rule, no prior estimator, no sparse-cell policy, no floor change, no
  strata-count change is INTRODUCED by any plumbing diff.
- The only "floor" hits in new files are np.floor in the display quantization formula
  (display/tensor_to_png.py:49) — grayscale rounding, not an allocation floor.
- test_nm_handcheck.py additions pass neyman_prior_rates / real_floor as ARGUMENTS to the
  pre-existing, already-gated harness API (write_hc1h_pools, prepare_hc1h_experiment);
  they define no new estimator or policy. The Neyman/floor/strata machinery in
  nm_handcheck.py predates the plumbing diff and is untouched by it (its diff is only
  the vocabulary import + the provenance assertion).
- nm_handcheck.py's HC1H_STRATA remains the same nine-tuple; the diff only re-sources
  HC1H_STATES from the shared vocabulary (same three values, same order).
- The rehearsal lane's own mapping dict (run_rehearsal.py:333-335) belongs to the
  separate rehearsal work package, not to the plumbing diff (run_rehearsal.py is not
  among the plumbing-modified files).

Rehearsal findings 1 (sparse-cell policy) and 6 (Neyman prior smoothing) are NOT encoded
anywhere in the plumbing changes. No automatic hold.

## F2 ENVIRONMENT SPLIT — PASS

- No package installs: grep of RUN_ENVIRONMENTS.md, run_*_stage.sh, and all stage targets
  finds no pip/conda/easy_install/PYTHONPATH/user-site injection (only the doc's
  prohibitions of those).
- Doc matches reality: run_inference_stage.sh and run_committee_stage.sh exec
  venv_torch/bin/python; run_cutout_stage.sh, run_display_stage.sh, run_hc1h_stage.sh
  exec /usr/bin/python3. Imports match the doc's per-stage package claims.
- Interpreters verified directly: venv_torch has torch 2.8.0 and NO PIL
  (ModuleNotFoundError); /usr/bin/python3 has PIL 11.3.0 and NO torch.
- No stage needs both torch and Pillow: torch stages (inference, committee) import no
  PIL; Pillow stages (display, handcheck) import no torch.
- test_run_environments.py: 2/2 passed at gate.

## F3 INFERENCE CLI INPUT TRANSPORT — PASS (byte-equivalent, not merely similar)

- resolve_input_paths level: on a shared 50-path fixture, legacy --inputs, line-delimited
  manifest, and JSON manifest all return the SAME ordered list of Paths
  (txt == legacy, json == legacy, order preserved). Mutual exclusion enforced with
  REFUSED_INPUT_TRANSPORT when both or neither is given.
- End-to-end level: ran inference_runner twice on the same 4 synthetic tensors — once
  with --inputs, once with --input-manifest — into separate output dirs. diff -r of the
  two output trees (results.jsonl + receipts/) is BYTE-IDENTICAL.
- 20,000-path test: test_input_manifest_loads_20000_ordered_paths_without_argv_transport
  PASSED when run (full inference suite 14/14 OK).

## F4 COMMITTEE ENTRY POINT — PASS

- member-B weights on disk hash to exactly
  6e4a6efaf9e9db55e8ca23f1ffa7e61ef437c62bc959c9630b90db0d18aeff0a (re-hashed at gate).
- load_frozen_member_b computes sha256_file BEFORE torch.load; refusal tested at gate by
  copying the weights to a temp dir, appending corruption (hash 13f22a3a...), and calling
  the loader: ContractError raised, and a mock.patch on torch.load confirmed
  torch.load was NEVER called before the refusal.
- Scoring functions unchanged: geometric_chi, cnn_chi, accepted_sign, SmallPlainCNN,
  canonical_parameter_hash each diffed HEAD-vs-working-tree — all UNCHANGED. The only
  change inside committee_state is returning imported constants instead of raw strings
  (semantically identical). Thresholds GEOMETRIC_THRESHOLD=0.08 / CNN_THRESHOLD=0.15
  untouched.
- Committee suite: 9/9 passed at gate, including
  test_member_b_weight_hash_mismatch_refuses_before_torch_load.

## F5 TENSOR-VS-IMAGE CONTRACT — PASS

- Determinism run twice at gate: rendered the same IC-6 tensor twice via
  display/tensor_to_png.py into separate dirs; PNGs are byte-identical
  (SHA-256 4a0f4132dae25c30a51eb9db0da35741c4a4c3bf3461ca22c892654b92f0b2c5 both times);
  bindings identical modulo output dir.
- PNGs structurally barred from chi path, proven by code path:
  (a) neither chi module (inference_runner.py, committee.py) imports PIL or reads any
      image file — grep hits are variable names only;
  (b) a real rendered PNG (16,376 bytes) fed as a tensor input is REFUSED by BOTH chi
      paths at the byte-length contract: inference_runner → REFUSED_IC6_BYTE_LENGTH,
      committee.score_manifest → ContractError "IC-6 tensor must contain exactly 65536
      bytes". A PNG can never satisfy the 65,536-byte IC-6 contract.
- Display suite: 2/2 passed at gate.

## F7 STATE VOCABULARY — PASS

- Single shared module committee_state_vocabulary.py imported by BOTH sides:
  _committee_20260820/committee.py (COMMITTEE_STATES, to_hc1h) and
  handcheck/nm_handcheck.py (HC1H_STATES). Not duplicated.
- Bijection verified at gate under BOTH interpreters (venv_torch and system python3):
  total (domain == COMMITTEE_STATES), injective (3 distinct values), covering
  (range == HC1H_STATES), order-preserving; unknown states refused with ValueError.
  The module also self-enforces all three properties at import time.
- No ad-hoc string munging at plumbing call sites: committee.py contains zero raw state
  literals; nm_handcheck.py's diagnostic dict is BUILT by iterating the imported
  HC1H_STATES (its two literal reads index that dict — consumption, not a mapping).
  Raw literals surviving in kun_gate_recheck/train_and_validate/run_rehearsal are
  outside the plumbing diff (rehearsal/committee auxiliary lanes).
- Vocabulary suite: 3/3 passed at gate.

## F8 HC-1H ROLE NAMING — PASS

- Frozen interface name unchanged: --real-population (prepare subcommand) and the
  real_population_path parameter are byte-identical to HEAD (pre-plumbing).
- Provenance assertion TESTED at gate (six cases, standalone driver against
  _read_hc1h_rows):
  CASE1 synthetic pool passed as the real population → REFUSED (synthetic-identity rows
        fail the accepted-population contract field set).
  CASE2 role swap (accepted file carrying blind_injection_pool sidecar) → REFUSED
        ("population role disagrees: expected accepted_population, got blind_injection_pool").
  CASE3 data_class/provenance disagreement (rows synthetic, sidecar authorized_measurement)
        → REFUSED ("data_class and provenance disagrees").
  CASE4 missing sidecar → REFUSED ("provenance is missing or invalid").
  CASE5 control: honest synthetic rehearsal declaration (accepted_population + synthetic)
        → read passes, 3 rows. The intended semantic: synthetic rehearsal allowed when
        explicitly declared, synthetic pool cannot silently occupy the real-population role.
  CASE6 injection side role swap → REFUSED.
- run_hc1h_stage.sh prints the role-name-trap warning to stderr before exec.
- HC-1H suite: 29/29 passed at gate, including the dedicated
  test_hc1h_population_data_class_must_match_provenance.

## Aggregate

- test_run_environments.py 2/2; test_inference_runner.py 14/14; test_committee.py 9/9;
  test_tensor_to_png.py 2/2; test_committee_state_vocabulary.py 3/3;
  test_nm_handcheck.py 29/29. Total 59/59 OK at gate — matches the receipt's claim.
- Boundary: findings 1 and 6 not encoded. No repairs required.

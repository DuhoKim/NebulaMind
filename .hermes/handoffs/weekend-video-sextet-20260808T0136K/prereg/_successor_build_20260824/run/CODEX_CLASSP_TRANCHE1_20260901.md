# PRE-BS-6 Class-P receipt candidates — tranche 1

Scope was limited to BS-2c, BS-2o, BS-2s, BS-5p, BS-3, BS-4, and BS-7p. No candidate was written to a live store. The only candidate files are under `run/classp_candidates/`. The frozen schema was read first from `ref/successor_ref_v9.py` lines 185–200; the covenant rows were read from `PREREG_SUCCESSOR_DRAFT_V134_20260831.md` lines 931–940.

Candidate files contain exactly the named `SLOT_SCHEMA` field set. Before writing, each produced field map was passed to the frozen `ref/successor_ref_v9.py:receipt()` using byte values. The returned v9 envelope hashes are recorded below; no successor receipt layer was used.

## BS-2c — BLOCKED

Schema fields: `universe_brickid`, `brickid`, `n_eligible`, `c_bytes`, `grouped_sum`, `ungrouped_total`.

The pinned source artifacts exist and authenticate:

- universe sidecar: `../_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/static/survey-bricks-dr10-south.fits.gz`, sha256 `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`, 366,912 bricks;
- count table: `../_tori_parent_row_count_evidence/footprint_variance_brick_counts_20260814/combined_per_brick_counts.csv`, sha256 `4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0`, 270,577 positive-count rows and frozen total 832,393;
- mandated entry: `gates/count_oracle_harness.py`; frozen v9 sha256 checked by it as `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.

Blocked because the only production entry is not a BS-2c-only constructor: `production_build_plan()` must complete frozen `v9.build_plan()` before it constructs the BS-2c receipt. That call necessarily enters the unfilled Stage-P chain. The frozen text states: “**BS-5p cannot be filled from the existing measurement receipt. Filling it requires implementing the exact route in the code §0 pins ... and re-running under those exact bytes.**” No authenticated successful production result from this entry over the real table exists on disk. The tier-2 11/11 gate result authenticates refusal behavior, not a successful real-plan receipt. Emitting BS-2c without the successful mandated call would bypass the only production entry, so no candidate was produced.

## BS-2o — BLOCKED

Schema fields: `order_brickid`, `N`, `Var`, `L_raw`.

The `acquire/` inventory contains parent rows, quality rows, selected-brick lists, query text, chunk receipts, and the 49,211-row cut, but no traversal-order artifact and no per-prefix `N`, `Var`, and `L_raw` ledger. The paths searched were `acquire/**` and `real/**`; the only Stage-P receipts found were historical/superseded and do not supply the schema’s full traversal ledger. No values were synthesized.

## BS-2s — BLOCKED

Schema fields: `selected_brickid`, `L_ret`, `L_raw`, `N_ret`, `N_eq`, `repass_successes`.

Authenticated inputs found:

- `acquire/positions_selected_cut.csv`, sha256 `a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372`, 49,211 data rows;
- `acquire/selected_brickids_cut.txt`, sha256 `939b4ef2d2e00fb974892e835e51e512a5511bbe04a74780be15e38eb3879fd5`, 6,104 brick IDs.

These artifacts do not contain authenticated `L_ret`, `L_raw`, `N_ret`, `N_eq`, or a Stage-P `repass_successes` for the actual 49,211-row mask. The frozen text labels the prior 995/1000 result “**SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK**.” Therefore no candidate was produced.

## BS-5p — BLOCKED

Schema fields: `l_min_plan`, `l_plan`, `successes`, `n_trials`.

The frozen constants do establish `n_trials = 1000` and the success rule `x >= 962`, but they do not establish a real current-mask `l_min_plan`, `l_plan`, or `successes`. The governing frozen clause says: “**This text promises the EXACT per-trial test: every trial judged against its own 20,000-permutation null, no shared reference null in the counting path**,” followed by “**BS-5p cannot be filled from the existing measurement receipt**.” The on-disk `real/STAGEP_EXACT_RECEIPT_20260826.json` is expressly superseded/non-applicable to the 49,211 mask. No candidate was produced.

## BS-3 — BLOCKED

Schema fields: `weights_sha256`, `tau`, `antisymmetry_receipt`.

The frozen covenant row quotes weights `83008c1c…` and `tau = 4.4006456017494235`; §1 quotes the antisymmetry identity and a 1000/1000 synthetic result. However, no weights file whose sha256 begins `83008c1c` exists on disk in the lane, and no authenticated antisymmetry receipt artifact was found. Paths checked: the complete lane file inventory, including filenames matching `*weight*`, `*.pt`, `*.pth`, `*.onnx`, and `*.h5`, followed by sha256 scanning of lane files. Because `weights_sha256` must refer to an on-disk authenticated artifact, the slot is blocked regardless of the quoted tau.

## BS-4 — PRODUCED

Schema fields: `anchor_digest`, `sign_convention`, `verdict`.

The synthetic anchor was rerun fresh by `python3 ref/successor_ref_v9.py --fixtures` under the frozen environment. The run exited 0 and ended `ALL FIXTURES PASS`. Its anchor lines were:

- `BATTERY-SIGN: PASS A=-0.0408 -> INCONCLUSIVE (A_L=-0.04272)`;
- `BATTERY-POS: PASS A=+0.0408 at powered N -> REPRODUCED-LONGO ...`.

Provenance by field:

- `anchor_digest`: sha256 `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5` of the exact fresh `run_fixtures()` UTF-8 output;
- `sign_convention`: frozen §1 quote, “**Our East-of-North winding convention maps it to +0.0408**”;
- `verdict`: the fresh battery’s `BATTERY-SIGN: PASS`, with the positive control also PASS.

Frozen v9 receipt result: body sha256 `164f1f30a205fdb69ede1430687d1d82f1e99b2ede4e0c857800da1f6493d062`; envelope sha256 `5f716494e672060cf575a153b636b669d6a66cd1131b7bcfc9999d3817e9b087`.

Candidate: `run/classp_candidates/BS-4.json`.

## BS-7p — PRODUCED

Schema fields: `ref_code_sha256`, `fixtures_sha256`, `environment`, `n_perm`.

The full named v9 battery was run fresh, exited 0, and ended `ALL FIXTURES PASS`; it includes serialization/schema, RNG-addressing behavior, boundary, sign, power, mask, and refusal fixtures.

Provenance by field:

- `ref_code_sha256`: on-disk `ref/successor_ref_v9.py`, sha256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`;
- `fixtures_sha256`: sha256 `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5` of the exact fresh fixture output;
- `environment`: v9 `environment_record()` canonical JSON, `{"byteorder":"little","machine":"arm64","numpy":"1.26.4","platform":"darwin","python":"3.9.6","python_major_minor":"3.9"}`; this satisfies the frozen clause “**python 3.9, numpy 1.26.4, little-endian**”;
- `n_perm`: frozen §3 quote, “**n_perm = 100,000**,” also `N_PERM = 100_000` in v9.

Frozen v9 receipt result: body sha256 `3bfabc557aa8e6a8268f1c9fc3d54d859111865140d86a461cb40f1d0a7ce27d`; envelope sha256 `15bf924ec2aa9ef26b5d10dfcd6072c5737dfb0f4141a2b3c35e4d368a43e236`.

Candidate: `run/classp_candidates/BS-7p.json`.

SEAT: CODEX
VERSION: CLASSP-V1
VERDICT: 2-PRODUCED-5-BLOCKED
COUNT: 2

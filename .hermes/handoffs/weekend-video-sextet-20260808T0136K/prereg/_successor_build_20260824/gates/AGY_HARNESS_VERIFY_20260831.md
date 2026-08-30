# AGY VERIFY SEAT: count_oracle_harness.py

## 1. The None-refusal claim
The pre-dispatch check in `production_build_plan` strictly uses `v is None`. This fails to catch None-like or falsy values such as empty lists `[]`, empty numpy arrays, or `np.nan` containers. An empty payload trivially bypasses the harness's pre-dispatch refusal and reaches `v9.build_plan()`. Because `v9.receipt()` explicitly refuses empty payloads (`if not v`), these values pass the harness and fail downstream, directly contradicting the claim that the harness pre-dispatch check refuses them.

## 2. The release binding
- **Caller influence**: The caller cannot manipulate the release binding via `snapshot_dir`. `load_pinned_geometry` only uses `snapshot_dir` as a destination to write the temporary snapshot; the read path is hardcoded to `PINNED_SIDECAR_REL` and rigorously verified against `PINNED_UNIVERSE_SHA256`. Monkeypatching `v9` module paths is also mitigated because `_load_v9()` loads the module directly from the file location rather than relying on `sys.modules`.
- **Validator mismatch and identity**: `count_oracle_harness.py` derives `universe_brickid` from `sorted((geom.by_name or {}).keys())`. These keys are **string bricknames** (e.g., `'3385m885'`). However, `v9`'s validator (`validate_count_table`) expects integer brick IDs and performs `np.asarray(universe_brickid, dtype=np.int64)`, causing an inevitable `ValueError` crash. Additionally, `v9` does not check object identity (`is`), it merely compares values after array conversion. The `is` check in the harness itself (`bound[k] is not src`) is trivially self-fulfilling because it checks the exact dictionary it just populated.

## 3. The one-bound-invocation claim
The claim that receipt-vs-plan substitution is refused by construction is **broken**. The harness passes mutable buffers (`brickid`, `c`, `n_raw`) into `v9.build_plan()`. Inside `build_plan`, `np.asarray()` is called, which copies the data if it isn't already a contiguous numpy array of the target dtype. Because `build_plan` computes the plan using the copied data, a caller thread can mutate the original list contents concurrently *during* or *after* `build_plan` executes but *before* the harness calls `_canon_ids()` to build the receipt. Consequently, the receipt digests post-mutation bytes that differ from what the planner actually consumed. The `is` checks only verify variable reference identity, not content immutability.

## 4. Canonical encodings
- **Collisions**: `_canon_ids` joins elements with `\n`. Because `universe_brickid` is erroneously populated with string bricknames, any string identifier containing a newline (e.g., `"a\nb"`) would collide with a two-item sequence (`"a"`, `"b"`). 
- **Cross-field ambiguity**: There is no cross-field ambiguity because `v9.receipt()` serializes the fields safely by prefixing each with its name length and payload length (`len(name) + name + len(payload) + payload`).
- **repr floats**: `repr(float(x))` provides standard shortest-roundtrip determinism across Python 3.1+ environments, mitigating typical float collision risks, though edge cases like different NaN representations across OSes remain mathematically possible.

## 5. The fixtures
Several fixtures are completely **vacuous** as written:
- **F2, F3, F4 (Tier-2)**: These claim to verify that `build_plan` correctly refuses missing/extra bricks. In reality, they pass `full` (which contains string bricknames) into `production_build_plan`. `v9.validate_count_table` crashes with a `ValueError` when casting these strings to `int64`. The fixtures use a bare `except Exception: pass`, blindly catching this fatal type error and falsely registering a success.
- **F5a**: This fixture relies on a bare `except Exception: pass`. If `verified_bytes` fails for any unrelated reason (e.g., an `OSError` writing to the temp directory), the fixture passes silently.
- **F6**: This fixture claims to test the identity assertion machinery but merely assigns a list to a dictionary (`bound = {"brickid": a}`) and then evaluates `if bound["brickid"] is not a:`. This solely tests standard Python dictionary assignment and reference semantics, proving nothing about the harness's actual parameter binding.

<!-- FINDINGS-BLOCK v1 -->
SEAT: AGY
VERSION: COH-V1
VERDICT: DEFECTIVE
COUNT: 5
F1 | HIGH | _canon_ids | `\n` join causes string collisions if an ID contains a newline
F2 | HIGH | production_build_plan | Mutable buffers can be mutated concurrently between plan consumption and receipt generation
F3 | HIGH | production_build_plan | `universe_brickid` extracts string bricknames, but `v9` expects integer brick IDs, causing inevitable `ValueError` crashes
F4 | HIGH | production_build_plan | `v is None` check allows empty lists/falsy values to pass harness and fail downstream
F5 | HIGH | fixtures | F2/F3/F4 crash on string-to-int cast rather than planner refusal; F5a uses bare exception catch; F6 is completely vacuous
<!-- END FINDINGS-BLOCK -->

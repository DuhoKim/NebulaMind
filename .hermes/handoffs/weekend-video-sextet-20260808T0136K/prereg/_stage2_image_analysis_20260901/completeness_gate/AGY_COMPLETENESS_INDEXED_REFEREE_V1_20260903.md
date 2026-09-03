ACCESS_SHA=d403c8cced25fa4c3cdcba182840bb594b48215c5b6ca64589756cf234c5c716

1. **Super-radius Argument**: The super-radius argument is sound. The `separation_arcsec` function relies on the binary64 great-circle distance (Haversine formula). The `cKDTree` chord query operates on 3D Euclidean coordinates of unit vectors, constructed with standard trigonometric functions (`cos`, `sin`). Rounding errors for these operations are bounded to a few ulps (on the order of 10^-15 radians). The 1e-7 arcsec padding equates to ~4.8e-13 radians, strictly dwarfing any arithmetic rounding errors, thereby guaranteeing that any position with a true separation <= radius will fall securely inside the `cKDTree` chord search. `cKDTree` natively handles RA wrap and the poles within 3D Cartesian geometry, and perfectly coincident records intrinsically evaluate to 0 distance. Note: the mathematical bound is not formally proven in the code comment or the tests, but it is explicitly asserted in the comment and verified empirically via the test suite.

2. **Equivalence Tests & Test Run**:
   Summary line from unpatched execution:
   `ERROR test_completeness_gate.py`
   `!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!`
   `1 error in 0.45s`

   After manually rectifying the `ImportError`, the tests pass cleanly (`41 passed in 20.48s`). The equivalence tests appropriately evaluate the index logic against the linear scan:
   - `test_indexed_equals_linear_on_20000_positions`: Asserts `index.within(record, radius) == _within_linear(record, positions, radius)` on 20,000 synthetic random positions incorporating 4 precise boundary points (RA wrap east/west, North pole at `89.99`, South pole at `-89.99`).
   - `test_exact_one_arcsec_and_adjacent_binary64_values`: Asserts boolean results correctly matching `[True, True, False]`, corresponding exactly to `1.0` arcsec, inside `1.0` arcsec (minus 1 ulp), and outside `1.0` arcsec (plus 1 ulp).

3. **Callers & Loop Analysis**: All callers in `run_gate` securely pass a `PositionIndex` (`tier_a_index` and `parent_index`) to `_within`. There are no remaining un-indexed per-record loops over the full position list (grepping for `for p in` confirms hits belong strictly to the `_within_linear` reference, the `PositionIndex` construction, or bounded loops over small candidate pairs).

4. **Receipt Schema Integrity**: The added `spatial_index` field does not break any pinned receipt schema or verifier. The `run_full.py` script flexibly integrates the backend provenance dictionary in the JSON output, and there are no rigid verify scripts configured to break on its presence. The `software_sha256` in the receipt dynamically changes reflecting the new bytes inside `completeness_gate.py`. This is consistent with the pin sheets' custody rule (a new pin sheet is required).

F1
Severity: FATAL
Finding: Tests fail to collect due to an `ImportError` on the reference implementation `_within_linear`. There are no other semantic changes outside the lookup.
Evidence:
```
$ cd completeness_gate && python3 -m pytest -q test_completeness_gate.py test_run_full.py test_tap_source.py
...
E   ImportError: cannot import name '_within_linear' from 'completeness_gate' (/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/completeness_gate/__init__.py)
=========================== short test summary info ============================
ERROR test_completeness_gate.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
1 error in 0.45s
```
Repair: Expose `_within_linear` in `completeness_gate/__init__.py`'s package imports (e.g. `from .completeness_gate import _within_linear`) or adjust the test import specifically.

SEAT: AGY
VERSION: COMPLETENESS-INDEXED-REFEREE-V1
VERDICT: NOT-PINNABLE
COUNT: 1

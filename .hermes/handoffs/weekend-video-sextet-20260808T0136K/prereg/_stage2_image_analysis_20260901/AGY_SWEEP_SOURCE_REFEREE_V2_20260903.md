ACCESS_SHA=a5d2a38b5240a00d3c8640271fd0e396c0fbab7024c80773c4f21f5b3f48734a

# AGY REFEREE REPORT: SWEEP SOURCE V2

### TASK A — CLOSURE
**STATUS: CLOSED**
Evidence:
1. **Parity test now STRONG**: The test `test_candidate_by_candidate_strong_parity_with_tap` confirms strong parity. 
   - *Identity sets:* Exact identity sets are mapping between `input_index` and candidate `identity` via `self.assertEqual(by_index_local, by_index_tap)`.
   - *Separations & Coordinates:* Coordinate exactness down to binary64 bytes is verified (`self.assertEqual(struct.pack("!d", candidate.ra), struct.pack("!d", other.ra))`).
   - *Boundaries:* The boundary logic tests exactly 1.0 arcsec equality mapping via `boundary = math.nextafter(boundary, 0.0)` which matches exactly, and one ulp beyond `math.nextafter(beyond, math.inf)` which is correctly excluded.
   - *Collisions:* A two-position collision row correctly maps to both origins (`self.assertIn((0, (9010, 1, 2)), local_map)` and `self.assertIn((1, (9010, 1, 2)), local_map)`).
2. **Edge tests present**: Edge assertions strictly assert for exact GateError reasons:
   - Corrupt/truncated FITS: `test_corrupt_truncated_fits_refuses_with_exact_reason` asserts "COMPLETENESS-FAIL: unreadable/corrupt FITS sweep: broken.fits".
   - Manifest-listed sweep absent: `test_manifest_listed_sweep_absent_on_disk_refuses` asserting "needed sweep is absent on disk...".
   - On-disk sha ≠ manifest sha: `test_on_disk_sha_mismatch_refuses` asserting "on-disk sweep sha256 mismatch".
   - Empty box: `test_empty_sweep_box_returns_zero_candidates` returns zero candidates.
   - Memmap vs full read: `test_astropy_memmap_and_full_read_candidate_bytes_identical` enforces byte-identical results.
   - RA wrap and near ±90 Dec: `test_ra_wrap_and_near_poles_select_correct_boxes` tests the extreme margins.
3. **Module-form import works**: Both `python3 -m completeness_gate.test_sweep_source` and `python3 completeness_gate/test_sweep_source.py` run perfectly.

### TASK B — THE BEHAVIOUR CHANGE
**STATUS: DEFECT** (See S1)
The normalisation of FITS exceptions is fail-closed, however, it is **lossy** and does **not** retain the original exception text.
Quote from `sweep_source.py`:
```python
    except Exception:
        _fail(f"unreadable/corrupt FITS sweep: {path.name}")
```
This masks different failure classes. Any exception deriving from `Exception` (e.g. `MemoryError`, `PermissionError`, `OSError`) will have its traceback and message destroyed, falsely alerting operators to "corrupt FITS sweep" and preventing observability of other faults.

### TASK C — REGRESSION
**STATUS: NO REGRESSIONS**
No regressions vs V1 clause table detected. The implementation remains robust on:
- §3/§4/§5 conformance
- Box selection on the sphere (scaling by sec(dec) and properly bounding pole singularities)
- All-rows enumeration and absence of magnitude predicates
- Provenance binding to both positions simultaneously
- Strict receipt + sha binding verification and bounded memory usage (mmap default).

### TASK D — NEW DEFECTS
**S1: Lossy Exception Masking**
As identified in Task B, catching a generic `Exception` and throwing it away without appending `str(e)` or propagating the underlying failure class violates strict observability.

SEAT: AGY
VERSION: SWEEP-SOURCE-REFEREE-V2
VERDICT: PINNABLE-AFTER-REPAIRS
EQUIVALENCE_TO_TAP: STRONG
COUNT: 1

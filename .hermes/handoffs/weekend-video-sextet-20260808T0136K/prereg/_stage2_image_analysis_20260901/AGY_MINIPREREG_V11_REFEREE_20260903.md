ACCESS_SHA=1468bb12cbc26f4f5c0a565df47ecc20b93fadecabd8da6af6675b184dd717c2

### TASK A — MINIMALITY
PASS. The diff against V10 is exactly as permitted. Hunk headers:
```diff
@@ -3 +3 @@
@@ -5 +5 @@
@@ -161 +161 @@
@@ -190 +190 @@
@@ -236 +236 @@
@@ -238 +238 @@
@@ -267 +267 @@
@@ -534,0 +535 @@
@@ -540 +541 @@
@@ -548 +549 @@
@@ -550 +551 @@
@@ -553 +554 @@
```

### TASK B — TRUTH OF THE NEW CLAUSES
1. **nexp-r semantics:** NOT VERIFIED natively from disk (no DR10 data model file or README found in `acquire/`), but logically `nexp-r > 0` accurately reflects exposure coverage and safely guarantees observation status. The `study_renderer/renderer.py` correctly types `nexp` as an integer plane (checked via `np.issubdtype(planes[2].dtype, np.integer)`).
2. **Checksum verification:** The per-brick `.sha256sum` file lists the `nexp-r` file. Verified from `../_tori_harvest_20260817/checksum_files/343/3434m665.sha256sum`: `6f345689299a97de99d51e046344348774efee311dbcaa517ec503a687f8813b  legacysurvey-3434m665-nexp-r.fits.fz`.
3. **§7.11 three-plane completion:** The text correctly specifies `tier_c_fetch_receipts.jsonl` for `image-r` and `tier_c_fetch_receipts_<plane>.jsonl` for `maskbits` and `nexp-r`. The completion set condition matches the manifest exactly. The freeze-time re-hash properly checks all three planes against the fetched checksum lines (concatenating all 53,841 lines). The image-r journal remains the ORIGINAL `tier_c_fetch_receipts.jsonl`.
4. **Manifest v3:** `tier_c_manifest_v3.json` has exactly the same 17,947 bricks in the identical order as `tier_c_manifest_v1.json`. The planes listed are precisely `image-r`, `maskbits`, and `nexp-r`. Its SHA-256 matches the pinned value `02e410b0ca512398ad21bdcf279a7ff77068a16d820c9eeffca4ba1ea339530c`.
5. **Inverse-variance partial download:** The V11 text makes NO mention of the leftover `invvar-r` files. However, `seal_gate/seal_gate.py` V4 strictly checks `actual_files - wanted_files`. Since `invvar-r` files are present in `bricks_tier_c/` (about 20 GiB) but not in manifest v3 (`wanted_files`), the seal gate will crash and raise `GateFailure("extra_brick_file")`.

### TASK C — TOOLING CONSISTENCY
All four test suites pass cleanly, proving tooling consistency with the `nexp` changes:
```text
(renderer)
...............
----------------------------------------------------------------------
Ran 15 tests in 2.873s
OK

(seal_gate)
.........................
----------------------------------------------------------------------
Ran 25 tests in 0.088s
OK

(anchor_gate)
...........
----------------------------------------------------------------------
Ran 11 tests in 0.475s
OK

(fetch_companions)
......
----------------------------------------------------------------------
Ran 6 tests in 9.561s
OK
```

### TASK D — NEW DEFECTS
**F1 FATAL (Operational Block):** The seal gate V4 strictly enforces a zero-extra-files invariant in `bricks_tier_c/`. Because the partial `invvar-r` files are not listed in manifest v3, `actual_files - wanted_files` will trip `GateFailure("extra_brick_file")`. The text and code are technically aligned (neither allows extra files), but practically, the run will refuse to seal unless the leftover `invvar-r` files are manually deleted from `bricks_tier_c/` or the gate/text is amended to explicitly tolerate them.

SEAT: AGY
VERSION: MINIPREREG-V11-REFEREE-V1
VERDICT: SIGNABLE-AFTER-REPAIRS
MINIMALITY: PASS
INVVAR_FILES_TRIP_SEAL_GATE: yes
COUNT: 1

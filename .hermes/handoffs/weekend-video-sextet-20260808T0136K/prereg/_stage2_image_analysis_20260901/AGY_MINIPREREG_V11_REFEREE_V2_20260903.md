ACCESS_SHA=a4b5f557eff5de1db72dc574a8be1787c1873f23163f2dae6186067b6576ac99

# V11 Adversarial Referee Report V2

## TASK A — F1 CLOSURE

**Quoted §7.11 sentence:**
> Files of the superseded inverse-variance plane are KNOWN EXTRAS exactly when their filenames are carried by receipts of any verdict in the disclosed journal `../_successor_build_20260824/acquire/tier_c_fetch_receipts_invvar-r.jsonl`: they are never read, never hashed for the seal, and are excluded from the extra-file check; any file in `bricks_tier_c/` that is neither a manifest-v3 plane file nor a receipted known extra still yields `extra_brick_file` refusal, and because the journal is growing its digest is not pinned here but the seal receipt records its path, SHA-256, line count, and tolerated-known-extra count at seal time.

**Code Confirmation:**
- **Derivation of tolerated set:** The seal gate (`seal_gate/seal_gate.py` in `_known_extras()`) parses the `known_extras_journal` line-by-line. For each receipt, it first attempts to extract the filename from the `url` basename, enforcing that the name strictly starts with `legacysurvey-` and ends with `-invvar-r.fits.fz`. If `url` is missing or fails this check, it gracefully falls back to deriving the filename from `brick` and `plane`, enforcing that `plane == "invvar-r"`.
- **Refusal (i) - extra not in journal:** `tolerated` is determined by the intersection of on-disk extras and the derived `known_extras` set. Any file not in the `known_extras` set falls into `unrecognized_extras = actual_files - wanted_files - known_extras`. If `unrecognized_extras` is non-empty, the code raises a `GateFailure("extra_brick_file")`.
- **Refusal (ii) - extras present with no journal given:** If `--known-extras-journal` is omitted, the code sets `known_extras = set()`. Any extra file on disk immediately populates `unrecognized_extras` and refuses the seal.
- **Seal receipt records:** The JSON body appended to the seal journal records the journal's path (`paths["known_extras_journal"]`), its SHA-256 (`observed_digests["known_extras_journal_sha256"]`), its line count (`counts["known_extras_journal_line_count"]`), and the number of known extras physically present and tolerated (`counts["known_extras_tolerated"]`).
- **Seal Gate Suite:** Ran `python3 -m unittest seal_gate.test_seal_gate`. Result: `Ran 27 tests in 0.094s — OK`.

**Hostile Actor Scenario & Residual Custody Limit:**
If a hostile actor plants an arbitrary file in `bricks_tier_c/`, it will be caught by the extra-file check unless they also meticulously modify the invvar journal to include a fake receipt with a matching `-invvar-r.fits.fz` name. Because the growing journal is not hashed prior to the run in the preregistration, this is a technical window for tampering (a residual custody limit). However, this limit is closed in practice:
1. The seal gate irrevocably binds the manipulated journal's final SHA-256 and line count at seal time, tracing the tampering.
2. The renderer never reads `invvar-r` files (it requires `image-r`, `maskbits`, and `nexp-r`). An inserted fake `invvar-r` file is inert on disk and cannot pollute the data or alter measurement. 
This fully resolves the F1 defect.

## TASK B — MINIMALITY
- Diff performed against signed V10 (`MINI_PREREG_GZ_TIERC_DRAFT_V10_20260902.md`).
- Hunks are strictly confined to: banner ×2, §7.7, §7.11 (+ known-extras sentence), §8.12, §18 row, §19 entries, signature lines, and trailer.
- Sections §14, §15, §16.7a-c, and §17 remain byte-identical.
- **Result:** PASS.

## TASK C — REGRESSION SWEEP
- `tier_c_manifest_v3.json` remains strictly unchanged (SHA-256 `02e410b0ca512398ad21bdcf279a7ff77068a16d820c9eeffca4ba1ea339530c`).
- `seal_gate`: Ran 27 tests — OK.
- `study_renderer`: Ran 15 tests — OK.
- `fetch_companions`: Ran 6 tests — OK.
- `anchor_gate`: Ran 11 tests — OK.
- No regressions in nexp semantics, checksum-file lines, or consistency.
- **Result:** PASS.

## TASK D — NEW DEFECTS
- No new defects identified.

SEAT: AGY
VERSION: MINIPREREG-V11-REFEREE-V2
VERDICT: SIGNABLE
F1: CLOSED
MINIMALITY: PASS
COUNT: 0

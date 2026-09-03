ACCESS_SHA=0b3267a7a1f2a0be864800db36fbb6c73b92321862a676df626371383bed8a8f

# Referee Report: Local Sweep CandidateSource (Fallback Route)

## Task A — CONFORMANCE
- **CandidateSource Interface**: `SweepCandidateSource` correctly inherits and matches the `tap_source` interface (`provenance` property and `candidates()` method).
- **Inclusive 1.0 arcsec**: The implementation imports and uses the exact `separation_arcsec` function and checks for `<= RADIUS_ARCSEC` (inclusive).
- **Box Selection**: The margin is applied correctly as an angular distance on the sphere. RA margins are expanded by `margin / cos_dec` (or clamped to 180 degrees at the poles), and Dec margins are direct.
- **ALL rows returned**: The loop scans all matching sweeps and correctly yields all candidates (it does not short-circuit after finding one).
- **Columns**: Only the six `IDENTITY_COLUMNS` are fetched. No flux, magnitude, or quality predicates are applied.
- **Provenance Grouping**: Candidates are accurately attributed. If a Tractor source falls within 1.0 arcsec of two different GZ1 positions, it is yielded for both `input_index` keys.
- **Duplicates**: Sweeps partition by `brick_primary`, so sources shouldn't overlap. If a duplicate source were present in two overlapping sweeps, the code silently deduplicates it into the chunk's `seen` set (`key = record.input_index, candidate.identity`) during chunk generation, preventing downstream errors.
- **Completeness Proof**: The on-disk `sha256_file(path)` is recomputed every time the file is checked by `_verify` for a chunk, rather than trusting a cached value. This means it is recomputed at least once (and in practice, many times) per run.

## Task B — EQUIVALENCE
- **Parity Test**: The test vs `tap_source` is a weak count/identity check. It compares sets of candidate identities (`{c.identity for c in ...}`), avoiding direct float-level equality checks on RA/Dec between the FITS payload and the string-parsed TAP payload.
- **Boundary Agreement**: The two routes **cannot** disagree on a boundary case. Although the TAP server uses a slightly padded `SERVER_RADIUS_DEG` via Q3C, `tap_source` subsequently filters the returned rows using the **exact same** local `separation_arcsec(...) <= 1.0` check. Thus, the client recomputation is strictly authoritative in both routes, guaranteeing boundary parity.

## Task C — TESTS
- **Run output**: Running `python3 completeness_gate/test_sweep_source.py` directly executes only 7 tests due to packaging/import resolution. The full suite of 42 tests requires `PYTHONPATH=completeness_gate python3 -m unittest ...`. This is a wording/packaging remainder.
- **Missing test cases**: There are omissions in the test suite:
  1. Empty sweep box (absent from manifest or 0-byte file)
  2. Corrupt FITS file
  3. Sweep listed in manifest/receipts but absent on disk
  4. Determinism check between `fitsio` and `astropy.io.fits` `memmap` modes.

## Task D — BOUNDARIES
- **Isolation**: The code does not use the network, it reads only the required identity columns from FITS tables (no pixels), and it restricts all writes to the `self.artifacts` checkpoint structure. The TAP crossmatch and its state remain entirely untouched.

## VERDICT
PINNABLE-AFTER-REPAIRS (missing edge-case unit tests). The implementation logic is sound and conforms perfectly to the preregistration, but the test gaps (corrupt FITS, missing sweep on disk, deterministic library parity) must be covered before full pinning.

SEAT: AGY
VERSION: SWEEP-SOURCE-REFEREE-V1
VERDICT: PINNABLE-AFTER-REPAIRS
EQUIVALENCE_TO_TAP: WEAK
COUNT: 42

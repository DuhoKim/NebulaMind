# Cutout acquisition pipeline — synthetic self-test

Recorded: 2026-08-14T13:54:39Z (2026-08-14T22:54:39+09:00)

Verdict: **PASS — BUILD ONLY; ZERO REAL ACQUISITION**

## Boundary counters

- real catalogue rows read: **0**
- real positions read: **0**
- real cutouts requested: **0**
- real cutouts received: **0**
- network calls made by this lane: **0**
- chirality or morphology labels computed: **0**
- sky statistics computed: **0**
- publication, acceptance, commit, or push: **0**

All fixture coordinates, object keys, FITS headers, and FITS bytes were generated synthetically in temporary test directories. Temporary private-package probes were deleted automatically.

## Commands actually run

```text
cd prereg/acquisition
/usr/bin/python3 -m unittest -v
/usr/bin/python3 -m py_compile nm_acquire_cutouts.py test_nm_acquire_cutouts.py
```

Result:

```text
Ran 14 tests in 0.107s

OK
```

Compilation result: **PASS**.

## Acquisition test matrix

| Test | Observed result |
|---|---|
| CLI exposes only fixed synthetic `--dry-run`; no execution mode | PASS |
| Real identifiers, path-like identifiers, and non-mock transport rejected before fetch | PASS |
| Tampered append-only request log refuses the next event | PASS |
| Dry-run constructs the exact South-only request and does not call transport | PASS |
| Frozen Cut 1–6 text contract is exact and ordered | PASS |
| Pure synthetic selector accepts the full chain and rejects each of six failing stages | PASS |
| Corrupt/truncated FITS becomes a logged, counted failure with no stored cutout | PASS |
| SIP-bearing WCS is rejected by the hash-pinned BS-7 detector | PASS |
| Parity-flipped WCS is rejected | PASS |
| Valid 256×256×3 mock FITS is SHA-checked, parity-checked, and custodied | PASS |
| Two mock requests remain serial and at least 5 seconds apart on a fake clock | PASS |
| Retryable mock pressure waits 30 seconds on a fake clock, logs backoff, and retries | PASS |
| Completed object resumes after checksum verification without refetch | PASS |
| Interrupt after response custody resumes from staged bytes without refetch | PASS |
| Interrupt before response custody remains explicitly uncertain and is not refetched | PASS |
| Prior terminal failure is counted, logged, and not silently retried | PASS |

The three required negative fixtures were observed to fire: SIP, parity flip, and corrupt/truncated response. Resume behavior was observed at completed, response-custodied, in-flight-uncertain, and terminal-failure states.

## Exact route correction caught during verification

An initial implementation used the composite `ls-dr10` viewer layer. Exact-text comparison against `TORI_SURVEY_ROUTE_BINDING_20260812.md` caught that defect before this receipt was written. The test was changed first and failed RED; the implementation was then corrected to the required **`ls-dr10-south`** layer. The complete suite passed afterward.

## Static no-network audit

The Python AST audit returned:

```json
{"ast_parse":"PASS","cli_build_only_stop":true,"exact_mock_type_guard":true,"fetch_implementations":["MockTransport"],"forbidden_network_imports":[],"network_calls_executed":0,"only_mock_fetch_implementation":true}
```

There is no `requests`, `urllib`, `urllib3`, `httpx`, `aiohttp`, `socket`, `ftplib`, or `http.client` import. `MockTransport` is the only class implementing `fetch`; non-dry execution requires `type(transport) is MockTransport`. The CLI has no input-manifest or real-transport option.

## Public-release boundary probe

The hash-pinned release linter first passed its own deterministic fixture matrix:

```json
{"fixture_count":22,"matched_count":22,"network_used":false,"passed":true,"status":"PASS_SYNTHETIC_SELFTEST","synthetic_only":true}
```

A temporary synthetic private acquisition output—including request log, state, per-object receipt, and synthetic FITS—was then wrapped in a proposed release manifest and checked with `release_linter/nm_release_lint.py`.

Result:

```json
{"verdict":"REJECT","finding_codes":["E_FILE_UNKNOWN_TYPE","E_R1_EMBEDDED_OBJECT_RECORD"],"contains_embedded_object_record_rejection":true,"private_files_tested":4,"synthetic_only":true,"network_used":false}
```

Therefore acquisition products are private analysis inputs, not public release artifacts. No release package is proposed.

## Hash custody

| Artifact | SHA-256 |
|---|---|
| `_tmp_TORI_ACQUISITION_BRIEF.md` | `96894ca7060100716016cac04c4af149cf48fd8f8719ef19993a58e57bcfd3c2` |
| `TORI_SURVEY_ROUTE_BINDING_20260812.md` | `3f41b6d925c0b540120f94636e4d78a045bebd1ed579293e4ec6f6d9163d3a87` |
| `PREREG_LONGO_AMPLITUDE_TEST_20260812.md` | `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590` |
| `TORI_BS1_CLOSURE_PACKET.md` | `50bf06b0f28c690360751d60cb150387446fee1c5f3629036515234b0301b8f5` |
| Yui parity validator | `7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55` |
| BS-7 distortion detector | `cae1b1b7ef4e25000ad5d8c906647216b1425638ac737b4ea7363ca948760569` |
| release linter | `7ff18bfc9272bcbb924b77cb81f2b37c45a130c2b1c5ba1fbc9b95baaab323ac` |
| `nm_acquire_cutouts.py` | `5f48066b8a7d56e6d595765cca7ea762197b0473fdde2820acaa0cf59862f400` |
| `test_nm_acquire_cutouts.py` | `6e68af6229af087762313dc335bed3f3c20fdb70d55b19985ac202b772f4c3a8` |

The pipeline re-hashes both imported validators at runtime and refuses if either byte stream changes.

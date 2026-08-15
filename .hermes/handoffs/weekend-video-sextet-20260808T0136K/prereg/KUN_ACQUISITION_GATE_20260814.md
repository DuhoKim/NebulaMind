# KUN ACQUISITION PIPELINE GATE

Recorded: 2026-08-15T01:11:27+09:00

Verdict: PASS_ACQUISITION_BUILD_ONLY_GATE

Scope: gate of Tori's acquisition pipeline as a build-only artifact. I did not authorize or perform real acquisition, sky-data fetching, empirical sky statistics, publication, acceptance, commit, or upload.

## Exact Artifacts Bound

The brief names `acquisition/...`; the files present in this workspace are under `prereg/acquisition/...`. I gated those concrete files.

| Artifact | SHA-256 |
|---|---|
| `prereg/_tmp_KUN_ACQUISITION_GATE_BRIEF.md` | `6303522d3f6dd0a249e9a4f830e3de0732177cef90cb5f51ecc80ee5e6ba9eb6` |
| `prereg/acquisition/nm_acquire_cutouts.py` | `5f48066b8a7d56e6d595765cca7ea762197b0473fdde2820acaa0cf59862f400` |
| `prereg/acquisition/test_nm_acquire_cutouts.py` | `6e68af6229af087762313dc335bed3f3c20fdb70d55b19985ac202b772f4c3a8` |
| `prereg/acquisition/SELFTEST.md` | `b984f8c768953d6256252bce7ea75258db9ccdeae136fcd374c797bf78966b6c` |
| `prereg/acquisition/TORI_ACQUISITION_20260814.md` | `92d36f41d6d86245e327cb72dd1810d46e94a59801e60529401d41f4d2a794b1` |

## Verification Performed

I ran the local synthetic test suite only:

```text
cd prereg/acquisition
python3 -m unittest -v test_nm_acquire_cutouts.py
```

Observed result:

```text
Ran 14 tests in 0.103s
OK
```

No real service query was run.

## No-Network Source Gate

I verified the no-network claim from `nm_acquire_cutouts.py` itself, not from Tori's AST audit.

The source imports only standard local/runtime modules: `argparse`, `hashlib`, `importlib.util`, `json`, `math`, `re`, `sys`, `time`, `datetime`, `pathlib`, and typing helpers. It does not import `requests`, `urllib`, `httpx`, `socket`, `http.client`, `subprocess`, or an equivalent network client. Source search also found no `curl`, `wget`, `os.system`, `popen`, `eval`, `exec`, or `__import__`.

The one real URL constant exists only to construct a request record:

```text
https://www.legacysurvey.org/viewer/fits-cutout
```

The code path that could issue a request is gated to the exact mock class:

```text
if not dry_run and type(transport) is not MockTransport:
    raise RuntimeError("BUILD_ONLY_STOP: only exact MockTransport is allowed")
```

The only `fetch` implementation in the pipeline source is `MockTransport.fetch`, which returns in-memory bytes from a synthetic response map. The CLI exposes only `--dry-run`; calling it without `--dry-run` stops with `BUILD_ONLY_STOP`. Dynamic loading is limited to two local hash-pinned validators; bytes are hashed before import and drift raises before execution.

Conclusion: this artifact can construct a Legacy Surveys request URL string, but it contains no real network transport and no CLI/input path that can perform a real fetch.

## Negative Fixtures

The required negative fixtures are executable and passed:

- Corrupt/truncated FITS -> `FAILED_FITS_INTEGRITY`, counted failure, no cutout retained.
- SIP-bearing WCS -> `REJECTED_DISTORTION`, detected family `SIP`, no cutout retained.
- Parity-flipped WCS -> `REJECTED_PARITY`, no cutout retained.

This satisfies the fail-closed side of PC-1/BS-7 for the synthetic acquisition harness. I did not find a local-Jacobian fallback path that could override the distortion detector.

## Resume Semantics

The resume behavior is conservative enough for a build-only gate:

- `COMPLETED` resumes only after receipt/request/output hash verification and does not refetch.
- `RESPONSE_CUSTODIED` resumes from staged bytes after hash verification and does not refetch.
- `IN_FLIGHT_UNCERTAIN` remains explicit, logs `RESUME_IN_FLIGHT_UNCERTAIN_NOT_REFETCHED`, increments `uncertain`, writes state, and does not issue a request.
- Terminal failures are counted, logged, skipped, and not silently retried.

The uncertain-state choice is correct: it does not silently drop the object as successful, and it does not refetch without an explicit later policy decision.

## Route And Selection Gate

The route is the corrected South-only route:

```text
layer=ls-dr10-south
pixscale=0.262
bands=grz
size=256
format=fits
```

The composite `ls-dr10` route is not present in the live source route. The synthetic selector encodes the frozen Cut 1-6 chain in order and refuses non-`SYNTHETIC_ONLY_BUILD` records.

## Weakest Thing

The weakest remaining point is not an implementation breach; it is the boundary created by the real endpoint URL inside a build-only file. A future operator could mistake URL construction for acquisition readiness. The current artifact prevents that mechanically because it has no real transport, rejects non-mock transport by exact type, and exposes only synthetic dry-run on the CLI. But any future addition of a real transport must be a new, explicitly authorized artifact with a fresh gate.

## Plain Ruling

PASS for build-only acquisition-pipeline feasibility and STOP-rule conformance.

This does not authorize real acquisition, a preregistration freeze, an empirical run, publication, public release, upload, commit, or acceptance. It only says the hash-bound synthetic acquisition harness is source-verified as no-network, fail-closed on the tested FITS/WCS hazards, route-correct for `ls-dr10-south`, and conservative on resume.

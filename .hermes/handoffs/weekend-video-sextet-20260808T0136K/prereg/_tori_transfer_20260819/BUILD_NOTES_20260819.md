# Tori image transport build notes — 2026-08-19

## Result

Build-only transport is complete. No image or checksum network request was executed. The generated 60,308-row JSONL is an **unsealed build candidate**, not retrieval authority. Live retrieval remains fail-closed behind the separate transport approval gate.

## Preconditions reverified

- `CROSSCHECK_VERDICT_20260819.md` first line: `CROSSCHECK_PASS`
- `KUN_CC_GATE_20260819.md` first line: `PASS_CROSSCHECK_GATE`
- `TORI_ROUTE_BINDING_SUCCESSOR_20260817.md` mode: `444`
- Frozen binding SHA-256: `1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b`

The executable repeats these checks before manifest construction, direct execution, or detached launch.

## Built artifacts

- `nm_image_transfer.py`
  - SHA-256: `5c19cf3646cdaa201c759dcf71a0aae66d6e469bb5f773181749c04a5b5e6db9`
  - mode `755`; 1,199 lines
- `tests/test_nm_image_transfer.py`
  - SHA-256: `9608a915d7906bd21e08a9f82bd73081e66b486021afc312ab9fd8b019da7e57`
  - 414 lines
- `candidate_image_manifest.jsonl`
  - SHA-256: `ff75636cf8fe14f14bcd35721491cbdf225d31d706325c114ecba4e91cf0dde2`
  - 60,308 rows; 60,308 unique manifested URLs
  - sidecar: `candidate_image_manifest.jsonl.sha256`

Manifest URLs are derived only from each harvested checksum file's exact `image-r` listing and use:

`https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/{aaa}/{brickname}/legacysurvey-{brickname}-image-r.fits.fz`

## Implemented controls

- Exact one-URL, full-file GET only; no recursion, URL globbing, range requests, redirects, cutout service, or unmanifested URL synthesis.
- `/usr/bin/curl --disable` prevents implicit curl configuration; proxy variables/config are disabled, protocol is HTTPS-only, and method is explicitly GET.
- Per-file SHA-256 is checked against the harvested digest before acceptance.
- Digest mismatch moves the file to `quarantine/`, appends a terminal receipt, writes `BLOCK_EVENT.json`, and stops.
- `receipts.jsonl` uses append-only/fsync state. Accepted files are rehashed on resume and never fetched again.
- Transient-attempt receipts preserve received-byte accounting before 30/60/120-second backoff; non-transient HTTP failures do not retry.
- Remaining campaign byte authority is passed to curl as `--max-filesize` before every request; cumulative response bytes remain ledgered.
- Per-process campaign lock enforces global concurrency 1.
- Two-second request-start floor survives restart through receipted request timestamps.
- Weekday Pacific window is 20:00–08:00; weekends remain open through Monday 08:00. Curl receives the remaining open-window duration as its maximum transfer time.
- Bandwidth ceiling is exactly 25,000,000 bytes/s.
- TLS custody records subject, issuer, and a SHA-256 fingerprint computed from the leaf certificate DER exposed by curl certificate details; missing custody metadata blocks acceptance.
- `heartbeat.json`, durable block events, atomic staging, whole-root completion rename, extra-file detection, and inflight uncertainty STOP semantics are implemented.
- Detached mode uses `/usr/bin/nohup` plus `start_new_session=True`; it performs all manifest, approval, gate, and disk checks before spawning.
- Activation additionally requires an exact acknowledgement and a SHA-pinned, mode-444 Duho/Kun approval record that pins the manifest, binding, 1,024-file size sample, coverage census, geometry-sidecar receipt, destination, count, byte ceiling, pacing, bandwidth, and windows.

## Tests and offline verification

Command:

`python3 -W error::ResourceWarning -m unittest discover -s tests -p 'test_*.py' -v`

Result: **18 tests passed** in 0.032 seconds. Python byte-compilation also passed.

Coverage includes local `MockTransport` fixtures only for transfer behavior, deliberate digest corruption/quarantine, receipt resume and tamper detection, durable transient accounting, 403 and 404 stop behavior, byte ceiling, campaign lock, manifest-change closure, extra-file closure, disk-space block event, frozen windows, leaf-certificate fingerprinting, curl command safety, and execution-ack refusal. No test invoked curl or opened a network connection.

Static audit result: `STATIC_AUDIT_PASS` — 60,308 rows, 60,308 unique exact URLs, manifest sidecar hash match, exact GET command, curlrc disabled, direct proxy disabled, `--max-filesize`, 25,000,000-byte/s limit, no prohibited transfer flags, and frozen gate checks pass.

## Disk-space preflight

Target volume probe for the intended campaign root:

- Required: `700000000000` bytes (~0.7 TB)
- Available: `15188114685952` bytes (~15.19 TB)
- Result: **PASS**
- Checked at: `2026-08-19T07:40:32Z`

The runner repeats a remaining-byte preflight before each network request and writes a durable block event if space falls below the authorized remainder.

## BUILD_ONLY_STOP guard

No file under `acquisition/` was changed or deleted. The acquisition package's `BUILD_ONLY_STOP` guard remains intact. All implementation/test/manifest/build-note writes are inside `_tori_transfer_20260819/`; the only lane-root write is the required completion marker `TORI_TRANSPORT_DONE.md`.

## STOP boundary

No transfer was launched, no detached process was started, and `portal.nersc.gov` was never fetched during this build. `candidate_image_manifest.jsonl` is deliberately labeled `UNSEALED_BUILD_CANDIDATE`; execution must be dispatched separately after the transport gate and its frozen approval artifact exist.

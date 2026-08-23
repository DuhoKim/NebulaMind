REFUTED_CONCURRENCY_AMENDMENT

# Gate: concurrency amendment

The amendment cannot run as written, and its independent byte ceilings do not preserve the original campaign-scale hard cap. These are execution/authorization defects, not nits.

## Refuting findings

### 1. Fatal: the UNMODIFIED transport rejects all three shard manifests

The amendment says the pristine transport already parameterizes the manifest and can run A/B/C. It does not parameterize the required manifest count:

- `_tori_transfer_20260819/nm_image_transfer.py:35` freezes `EXPECTED_FILE_COUNT = 60_308`.
- Both executable paths reject any other count before constructing the runner: `run` at lines 1096-1098 and `launch` at lines 1130-1132.
- The shard counts are 44,135, 8,086, and 8,087. Therefore every proposed invocation stops with `manifest must contain exactly 60308 image-r files`; zero shard instances can launch through the gated CLI.

This directly refutes the amendment's mechanism while requirement 1 correctly forbids modifying the transport.

### 2. Fatal: the three approvals expand the enforceable campaign ceiling by 280,000,000,000 bytes

The original 922,388,644,983-byte value was approved as a campaign-scale operational hard bound, not merely a projection. Approval A keeps that entire cumulative ceiling while B and C independently add 140,000,000,000 bytes each. The enforceable aggregate is therefore:

- A: 922,388,644,983
- B + C: 280,000,000,000
- aggregate: 1,202,388,644,983
- excess over Duho's original campaign ceiling: 280,000,000,000

At the receipt snapshot ending 2026-08-23T13:56:45Z, A had already received 438,219,841,068 bytes. Its unchanged independent ceiling still left 484,168,803,915 bytes, and B+C added another 280,000,000,000. Expected bytes may remain below 922 GB, but expected consumption is not the approved hard guard. Separate runners have no shared cumulative ledger, so the amendment does not preserve the single-campaign authorization.

If 280 GB is reserved for B+C, A's cumulative approval must be at most 642,388,644,983 bytes (or all three instances must enforce one shared 922,388,644,983-byte ledger). That still leaves A 204,168,803,915 bytes above the cited snapshot.

### 3. Approval A fails the brief's exact-delta requirement

Independent dictionary comparison against `RETRIEVAL_APPROVAL_20260819.json` found:

- A changes 4 fields: `manifest_sha256`, `exact_file_count`, `prose_record`, `duho_verbatim`.
- B and C each change the required five named fields plus `duho_verbatim` (6 total).

A necessarily leaves `destination` and `approved_byte_ceiling` unchanged, so it does not differ in exactly the five named fields plus `duho_verbatim`. If the intended rule was instead “no changes outside that six-field allow-list,” A passes that weaker rule; it does not pass the literal exact-delta rule in this gate brief.

### 4. Load claim is a measured projection, not a worst-case bound

The prior pacing gate measured 559.1 request starts/hour for one stream. Tripled, that is 0.4659167 requests/s, below the checksum harvest's frozen 1.0-second request-start floor. A fresh recent-1,000-interval snapshot measured 0.4433 requests/s projected across three streams. The typical-load comparison therefore holds.

But each unmodified instance has its own 2.0-second request-start floor and no aggregate limiter. The hard combined start-rate maximum is 1.5 requests/s, not 0.47 requests/s. Thus `CONCURRENCY_AMENDMENT_20260823.md:29` is false where it calls ~0.47 requests/s “worst case.” The stop-on-403/429/rate-limit behavior remains intact, but it is reactive rather than a 1 request/s aggregate cap.

## Attacks that held

### Transport identity

`git diff -- _tori_transfer_20260819/nm_image_transfer.py` is empty. Independent working-tree-versus-HEAD byte comparison passed:

- working SHA-256: `5e95f33ef6305c9390c4919b93dd044d461cbb14a2a2e80e377504adbe3fe764`
- HEAD SHA-256: `5e95f33ef6305c9390c4919b93dd044d461cbb14a2a2e80e377504adbe3fe764`
- `cmp`: byte-exact

The prior pacing edit was fully reverted.

### Shard closure and resume compatibility

Independent raw-line multiset comparison established:

- Original: 60,308 lines, 60,308 unique lines, 60,308 unique bricknames; SHA-256 `ff75636cf8fe14f14bcd35721491cbdf225d31d706325c114ecba4e91cf0dde2`.
- A: 44,135 lines; SHA-256 `3afde9444a6d91c22379419d0317bf46e75e40745674a771d506dcfc24f446b6`.
- B: 8,086 lines; SHA-256 `2b659ee71194501ad482a023a636509a18693bee7726a6ec911863fdf0caffc0`.
- C: 8,087 lines; SHA-256 `a6f4a5daf75b8c0737ac92848e3e222cbc8eb371477e54f1c747fa7138153624`.
- Every shard line is a verbatim line from the original.
- The A+B+C raw-line multiset equals the original raw-line multiset exactly.
- A/B, A/C, and B/C brick intersections are all empty.
- A is original indices 0-44,134; B is 44,135-52,220; C is 52,221-60,307. All are contiguous and preserve original order.
- The designated A range is original indices 36,049-44,134: 8,086 bricks, `2775m647` through `3076m422`. The first 36,049 unique main-receipt bricknames exactly equal original indices 0-36,048.
- At the final snapshot, the live append-only receipt file had 36,133 lines / 36,128 unique bricknames; every current receipt brickname was in A, with zero missing. `_load_state`'s membership and finalized-order checks therefore hold for A at that snapshot.

### Approval integrity except the exact-delta defect

All three approval files are mode 0444. Their hashes match the amendment's prefixes and their full values are:

- A: `fad9e367115c7700f52eea3b89cae0a822e668d3402512bfa7d43124b5e15b81`
- B: `940d52b9d8481f46dad7c1c4c6044ef27a6e039f95b36bddd1842ee21a01b22b`
- C: `d073e70d0a598ff0bdd1f217a34bf6774603a4294ddf4fef2a65337a0ee2b613`

Manifest pins and exact counts in the approvals match the independently hashed shard files. No approval changes any field outside the six-field allow-list named by the brief.

### `campaign_binding` archival

Rename-to-archive is acceptable in principle, provided it occurs only after the old runner has stopped cleanly and before the new A runner starts. It preserves rather than deletes the original binding, old receipts retain their original manifest pin, A contains every receipted brick, and the new runner can write a new active binding. The archive should be hash-receipted before restart. The rename itself and any restart remain separate execution actions; this gate performed neither.

## Evidence and scope

Read/hashed: the amendment, original approval, A/B/C approvals, original manifest, A/B/C manifests, shard metadata, unmodified transport, main `campaign_binding.json`, main append-only receipts, prior pacing gate, checksum-harvest implementation/heartbeat, and the original byte-ceiling record. Recomputed with Python raw-line multisets, brick sets/ranges, receipt-state simulation, JSON field diffs, SHA-256, modes, cadence, and ceiling arithmetic. Read-only process inspection found the old full-manifest runner still present; no process was stopped, started, or restarted. No network, git mutation, destination rename, approval edit, or transport edit was performed. The sole persistent write is this gate report.

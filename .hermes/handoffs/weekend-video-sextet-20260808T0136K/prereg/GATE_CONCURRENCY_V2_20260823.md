PASS_CONCURRENCY_V2

# Gate: concurrency amendment v2

The two fatal defects from the prior gate are repaired. I tried to make a wrong-count shard pass with a forged approval, truncated each manifest, re-ran every manifest/approval check independently, recomputed the partition and ceilings, and inspected the live A resume state. Under the transport's existing authorization model—an independently authorized approval SHA supplied on the CLI—the amendment preserves approval authority and fails closed.

## Rulings

### 1. Code diff and approval authority: PASS

`git diff -- _tori_transfer_20260819/nm_image_transfer.py` has exactly two default-context hunks, at `_run_gated` and `command_launch`. Each hunk deletes the same hard-count rejection and adds the same approval-count fallback: 11 additions and 1 deletion per site, 22 additions plus 2 deletions total. The two change-line bodies are byte-identical. No other transport site changed. `git diff --check` passed.

The amended transport SHA-256 independently reproduces the v2 claim:

- `225bd08b6a7c871ea894fa74c60e4ea7b305a0daa87ae0355968c27246c5132a`

Authority is preserved. The preliminary JSON read at `_tori_transfer_20260819/nm_image_transfer.py:1103-1108` and `:1147-1152` can only reject; it cannot authorize construction or execution of a runner. Both paths immediately call `load_approval` (`:1109-1116`, `:1153-1160`), which independently requires:

- approval bytes matching the CLI's authorized `approval_sha256`;
- approval mode 0444;
- approval `manifest_sha256` matching the manifest SHA passed to `load_manifest`;
- approval destination matching the resolved CLI destination;
- approval `exact_file_count` matching `len(records)`;
- approval ceiling matching the CLI ceiling;
- all unchanged authority, binding, pacing, bandwidth, window, sample-count, and receipt-pin fields.

A 60,308-record manifest does not bypass approval count authority: it bypasses only the new preliminary shard-count branch, then `load_approval` still requires `exact_file_count == 60,308`.

Forged-approval attacks under the authorized-SHA model failed for A, B, and C:

- altering `exact_file_count` while retaining the authorized approval SHA was rejected with `retrieval approval SHA-256 mismatch`;
- passing the approved bytes with a runtime count one lower was rejected on `approval field exact_file_count`;
- truncating a shard manifest by one record while retaining its approved manifest SHA was rejected on `manifest hash mismatch`.

Trust-boundary advisory, not a v2 defect: `--approval-sha256` remains the external authorization anchor. Supplying a new attacker-chosen approval file together with its attacker-chosen SHA would self-authorize, as it already could before this amendment. The approved launch packet must therefore pin the three exact approval SHAs below; the runner should not be launched from an unreviewed command line.

### 2. Dry manifest/approval validation: PASS

I imported the current transport and ran `verify_frozen_build_gates`, `load_manifest`, and `load_approval` directly, without the execution acknowledgement and without constructing a network transport. All three chains cleared validation:

| Shard | Manifest count | Manifest SHA-256 | Approval SHA-256 | Mode |
|---|---:|---|---|---|
| A | 44,135 | `3afde9444a6d91c22379419d0317bf46e75e40745674a771d506dcfc24f446b6` | `edc0b125bd12f191af4c061d1d2a1db04d21808c59deea473da629deaa30011b` | 0444 |
| B | 8,086 | `2b659ee71194501ad482a023a636509a18693bee7726a6ec911863fdf0caffc0` | `36ee138f1dba57c103afa1f6ec202c01a3d3e34d4a1350d4457592acd8c058d2` | 0444 |
| C | 8,087 | `a6f4a5daf75b8c0737ac92848e3e222cbc8eb371477e54f1c747fa7138153624` | `a9052ccc000287ff1629fe241988649eb7191e8be3be780715a1663cc6df006e` | 0444 |

No execution acknowledgement was used, no destination preflight ran, and no request was made.

### 3. Aggregate ceilings and A fit: PASS

Exact integer recomputation:

- A: 642,388,644,983
- B: 140,000,000,000
- C: 140,000,000,000
- sum: **922,388,644,983**, exactly the original campaign ceiling.

At the live receipt snapshot used by this gate, A had 36,189 unique accepted bricks and cumulative received bytes of 439,008,589,548. The new A ceiling therefore left 203,380,055,435 bytes.

A conservative allocation of the original campaign ceiling to the entire 8,086-brick A extension is `ceil(922,388,644,983 × 8,086 / 60,308) = 123,672,391,447` bytes. Even charging that full original A range after the current cumulative gives 562,680,980,995 bytes, leaving 79,707,663,988 bytes under A's v2 ceiling. In reality, some of those 8,086 bricks were already fetched while this gate ran, so this check is conservative. The runtime ceiling remains the hard fail-closed bound if realized sizes exceed the projection.

### 4. Shard-set correctness: PASS

Fresh independent re-verification strengthens the prior finding:

- original manifest: 60,308 records, SHA-256 `ff75636cf8fe14f14bcd35721491cbdf225d31d706325c114ecba4e91cf0dde2`;
- byte-concatenating `manifest_A.jsonl`, `manifest_B.jsonl`, and `manifest_C.jsonl` exactly reproduces the original manifest bytes;
- parsed A+B+C records exactly reproduce the original parsed record list in order;
- union count is 60,308;
- pairwise brick intersections A/B, A/C, and B/C are all zero;
- A spans the original prefix through `3076m422`, B is `3076m430` through `3335m652`, and C is `3335m682` through `3598m515`;
- every currently accepted main-root receipt brick is in A.

### 5. `campaign_binding` archival plan: ACCEPTABLE WITH REQUIRED ORDERING

Renaming the old `campaign_binding.json` to `campaign_binding_20260819_full.json` and allowing A to atomically write its own active binding is acceptable. It preserves the old manifest/count/ceiling binding instead of deleting it, while the new A binding will pin the A manifest, 44,135 count, and 642,388,644,983-byte ceiling.

The ordering condition is operationally material: the old full-manifest runner is still active at gate time (PID 74149, using the old manifest and 922,388,644,983-byte approval). Therefore the archive must **not** occur yet. Required sequence:

1. stop the old runner cleanly under a separate execution authorization;
2. verify no in-flight marker and that the campaign lock is released;
3. hash-receipt the old binding, rename it to `campaign_binding_20260819_full.json`, and verify the archived bytes retain that hash;
4. start A, then read back `campaign_binding.json` and verify it contains A's manifest SHA, 44,135 count, and 642,388,644,983 ceiling.

This gate performed none of those execution actions and does not authorize a stop, rename, launch, or restart.

## Failed attacks

- Could not make a modified approval count pass against any of the three authorized approval SHAs.
- Could not make a truncated manifest pass against any approved manifest SHA.
- Could not find a third code-diff site or a non-count-check transport change.
- Could not find a shard overlap, omission, reorder, or byte drift from the original manifest.
- Could not reproduce the prior 280,000,000,000-byte aggregate ceiling expansion.
- Could not place any current A receipt outside manifest A.

## Evidence and scope

Read/hashed: the v2 section of `CONCURRENCY_AMENDMENT_20260823.md`, the prior concurrency gate, the current transport and exact git diff, all three v2 approvals, all three shard manifests, shard metadata, the original manifest, the live main-root binding/heartbeat/receipts, and the active transport process command. Independent checks used Python JSON parsing, transport imports, SHA-256, mode checks, exact integer arithmetic, record-list/byte equality, set intersections, and targeted forged/truncated temporary artifacts that were deleted automatically. No network request, transfer execution, process stop/start, binding rename, approval edit, manifest edit, destination write, or git mutation was performed. The sole persistent write from this gate is this report.

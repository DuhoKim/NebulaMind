# M1+M3+M4+M5 execution-package index — 2026-08-19

EXEC_PACKAGE_COMPLETE

Frozen binding anchor: `TORI_ROUTE_BINDING_SUCCESSOR_20260817.md` SHA-256 `1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b`, mode `444`.

Manifest anchor: `_tori_transfer_20260819/candidate_image_manifest.jsonl` SHA-256 `ff75636cf8fe14f14bcd35721491cbdf225d31d706325c114ecba4e91cf0dde2`, 60,308 rows.

## Package artifacts

| Artifact | SHA-256 |
|---|---|
| `COVERAGE_CENSUS_20260819.md` | `e07de94b4e1c7787e466367aa1b2f9e5bb3cf9ff6740ba0637184b6b9482d6f6` |
| `DIGEST_CURRENCY_20260819.md` | `6e314be095754c8266fa6cae49e705be03242cd2ffbc7b0f3ecd1f68f6522486` |
| `SIDECAR_CUSTODY_20260819.md` | `fe6c96501e8969e71e54147cc6e0e7f290d7276579bb8dcc61aca88bfcf46ad4` |
| `SIZE_SAMPLE_20260819.md` | `2c372ea57e8f6af08c707f0bc9c210d57173030caafdcfd1ddeb03edc36b9d0d` |
| `SIZE_SAMPLE_SUMMARY.json` | `16010e4ee6729b259f9aa0061d087d0a5cdac7bafd7adbc5ab8ac992519bdc66` |
| `VERIFICATION_RECEIPT.json` | `feaee70ddd64428d92ca3a81512d8a2a98b471a40311706b96e340d2406151ca` |
| `receipts.jsonl` | `a64c3c9686aa9e75cd5790ea040ac2b2d0648765b54dc17c1bb32d2ba7b5be39` |
| `run_size_sample.py` | `8e7511a91df51229a55e07f82d2f7a0a5e242bb4a10fee2e62a7e8c7954cf227` |
| `size_sample_plan.json` | `bf2675e834796e60fd154907c40e5beef44b2f211dcae0a9965d74686f5019a9` |
| `verify_exec_package.py` | `07a501fe2e3f6af5164694667935fd76b1e70a941d8f86b52cb51feb1da07bf5` |

`EXEC_PACKAGE_INDEX.md` is intentionally not self-listed because a file cannot contain its own stable SHA-256. Its hash is recorded in the lane-root completion marker.

## Outcome

- M1: 1,024/1,024 HEAD requests; 1,024 HTTP 200; 0 non-200; zero body bytes; approved byte ceiling `922388644983` bytes.
- M3: required 60,308; receipted 60,308; absent-by-coverage 0; contradictions 0.
- M4: 598 identified; 397 in working set; 397 late-pattern; hazard 0; anomaly 0; 59,911 controls clean.
- M5: all §4.3 custody fields retained; no metadata/checksum fetch needed.

The transfer remains forbidden pending the separate M2 approval and the named F1/F2 dispositions.

# §11 step-5 execution approval record — route-B image transfer (APPROVED AND FROZEN)

Drafted by Hwao 2026-08-19 17:2x KST per `KUN_TRANSPORT_GATE_20260819.md` M2, under
`ACQUISITION_PREAUTH_20260818.md`. Becomes binding only when Duho approves and it is frozen
(mode 444, SHA-256 recorded in a freeze note). This record moves no bytes by itself; execution
additionally requires the runner's explicit CLI acknowledgement string (below) at launch.

## 1. What is being approved

One paced, serial, windowed retrieval campaign of exactly the manifested image files, under the
frozen successor binding, into the named destination, up to the approved byte ceiling — nothing
else.

## 2. Pins

| Item | Value |
|---|---|
| Binding (the law) | `TORI_ROUTE_BINDING_SUCCESSOR_20260817.md`, SHA-256 `1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b`, mode 444 |
| Transport implementation gate | `KUN_TRANSPORT_GATE_20260819.md` → `PASS_TRANSPORT_BUILD` |
| URL manifest | `_tori_transfer_20260819/candidate_image_manifest.jsonl`, SHA-256 `ff75636cf8fe14f14bcd35721491cbdf225d31d706325c114ecba4e91cf0dde2` |
| Exact file count | **60,308** `image-r` files (one per working-set brick; product fixed `image-r`) |
| Destination root | `/Users/duhokim/NebulaMindData/dr10_south_image_r/` (volume preflighted 15.19 TB free vs 0.7 TB required, 2026-08-19T07:40:32Z; outside the git tree by design; relative layout `coadd/AAA/brick/filename` per the build) |
| Approved byte ceiling | **922,388,644,983 bytes** per §11.4d — sample: 1,024/1,024 HTTP 200, 0 non-200, all 360 AAA strata, min spacing 1.00006 s ≥ 1.0 s floor, 0 body bytes; sampling receipt `execution_package/SIZE_SAMPLE_20260819.md` SHA-256 `2c372ea57e8f6af08c707f0bc9c210d57173030caafdcfd1ddeb03edc36b9d0d`, raw `receipts.jsonl` `a64c3c9686aa9e75cd5790ea040ac2b2d0648765b54dc17c1bb32d2ba7b5be39` |
| Coverage census artifact (§11.4b) | `execution_package/COVERAGE_CENSUS_20260819.md`, SHA-256 `e07de94b4e1c7787e466367aa1b2f9e5bb3cf9ff6740ba0637184b6b9482d6f6` — required 60,308 / receipted 60,308 / absent-by-coverage 0 / contradictions 0 |
| Digest-currency artifact (§11.4c) | `execution_package/DIGEST_CURRENCY_20260819.md`, SHA-256 `6e314be095754c8266fa6cae49e705be03242cd2ffbc7b0f3ecd1f68f6522486` — 598 replaced identified exactly; 397/397 in-WS late-pattern; 0 hazard; 0 anomaly; 59,911-brick control clean (`CROSSCHECK_PASS`, `PASS_CROSSCHECK_GATE`) |
| Geometry-sidecar custody (§4.3) | `execution_package/SIDECAR_CUSTODY_20260819.md`, SHA-256 `fe6c96501e8969e71e54147cc6e0e7f290d7276579bb8dcc61aca88bfcf46ad4` — pinned per the F2 disposition below |

## 3. §5.4 pacing, restated verbatim from the binding (frozen values)

1. **Concurrency: 1.** Strictly serial; one connection; no pipelining.
2. **Request spacing:** image files — next request no sooner than **max(2.0 s after the previous
   request started, completion of the previous transfer)**; checksum/metadata files — no sooner
   than **1.0 s** after the previous started.
3. Windows and bandwidth per the binding's §5.4 continuation (the §5.4 request windows the
   checksum harvest already honored: 20:00–08:00 US/Pacific weekdays, any hour weekends; the
   runner self-pauses at boundaries), block-event and back-off rules unchanged.

## 4. Findings dispositions (Duho, 2026-08-19, verbatim: "accept both, and draft the approval record")

- **F1 accepted as a recorded deviation:** every manifest row carries the uniform truthful
  `reason: "working-set intersecting source"`; the binding's four-way vocabulary cannot be
  populated because position files were deleted under the deletion rule by design. Custody
  impact none; re-derivation remains forbidden.
- **F2 accepted as the disposition:** the geometry sidecar travels as this record's pinned
  custody receipt (§2) rather than as a manifest row; the gate's own assessment — "a different,
  arguably stronger binding point" — is adopted.

## 5. Execution mechanics upon freeze

- Freeze: this file's SHA-256 recorded, `chmod 444`, freeze noted in the lane.
- Launch: detached (`nohup`) runner with `--execute-gated-transfer
  I_UNDERSTAND_THIS_FETCHES_MANIFESTED_IMAGE_BYTES`, the manifest path + its SHA-256, the
  destination root, and the approved byte ceiling exactly as pinned here; guard monitor armed
  (process death, stale heartbeat, block event, window transitions, completion).
- Stop conditions: any digest mismatch (quarantine + block event), any block event, byte-ceiling
  breach, disk preflight failure mid-run — all stop the run and go to Duho.

## 6. Approval

Approved by Duho. Conditional approval given 2026-08-19 ~17:15 KST, verbatim: "destination is fine, approve when the package lands" — following verbatim "accept both, and draft the approval record" (F1/F2, §4). The condition was satisfied when GPT2_EXECPKG_COMPLETE landed 2026-08-19 17:23 KST with package index SHA-256 `28a640bad7ab6319bd22dfabb0f028272757e41484a9af88ac5c5ec95db12eff`; this record was completed and frozen at that point per the recorded instruction.

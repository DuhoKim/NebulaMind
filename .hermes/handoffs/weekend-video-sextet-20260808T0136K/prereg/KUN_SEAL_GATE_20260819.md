HOLD_EXECUTION_SEAL — the record's pins, the byte-ceiling arithmetic, the sample receipts, the F1/F2 dispositions, and M1/M3/M4/M5 all verify cleanly against the frozen binding, but M2 (the §11 step-5 approval record) is unmet on three grounds: (1) the frozen record is Markdown prose while the executable's `load_approval` parses the approval file with `json.loads` and enforces fourteen exact fields plus three SHA-256 pins — the runner fails closed (`STOP: …`, exit 86) before any transport; (2) the executable requires `kun_transport_gate == "PASS_TRANSPORT_GATE"` (nm_image_transfer.py:1045) while the gate's verdict token is `PASS_TRANSPORT_BUILD` — even a corrected JSON quoting the true verdict would be refused; (3) the record's §3 does not restate the §5.4 bandwidth value (25 MB/s) or the backoff ladder values, which M2 enumerates as mandatory restatements. Repairs numbered 1–3 in §8. Nothing in this verdict moves a byte.

# Kun seal gate — `APPROVAL_RECORD_STEP5_20260819.md` + `_tori_transfer_20260819/execution_package/` against the frozen successor binding

Kun (kimi gate seat), 2026-08-19, fresh one-shot, the binding's "Duho and Kun" execution-acceptance Kun half. Findings-only. Method: local files + python3 only; zero network use by this lane; portal.nersc.gov never contacted.

## 0. The frozen record itself — verified first

- `APPROVAL_RECORD_STEP5_20260819.md`: recomputed SHA-256 = `a9e63f9fb72a2df3e2d852e383628c2cb45c78f4714a31a50e2fa686b4831c1b` — matches the kickoff value exactly; mode `444`.
- `TORI_ROUTE_BINDING_SUCCESSOR_20260817.md`: recomputed SHA-256 = `1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b` — matches the record's pin; mode `444`. The binding read in full; all clause citations below are to it.

## 1. Pinned hashes (kickoff check 1) — PASS

Every SHA-256 pinned in the record recomputed against the actual file:

| Pin | Result |
|---|---|
| binding `1371b110…fe8b` | MATCH (mode 444) |
| manifest `ff75636c…dde2` | MATCH |
| `SIZE_SAMPLE_20260819.md` `2c372ea5…9d0d` | MATCH |
| `receipts.jsonl` `a64c3c96…be39` | MATCH |
| `COVERAGE_CENSUS_20260819.md` `e07de94b…d6f6` | MATCH |
| `DIGEST_CURRENCY_20260819.md` `6e314be0…2486` | MATCH |
| `SIDECAR_CUSTODY_20260819.md` `fe6c9650…6ad4` | MATCH |
| package index `EXEC_PACKAGE_INDEX.md` `28a640ba…2eff` (record §6) | MATCH |

Package-internal pins inside the index also recompute clean: `SIZE_SAMPLE_SUMMARY.json` `16010e4e…`, `VERIFICATION_RECEIPT.json` `feaee70d…`, `run_size_sample.py` `8e7511a9…`, `size_sample_plan.json` `bf2675e8…`, `verify_exec_package.py` `07a501fe…`. `VERIFICATION_RECEIPT.json` reads `"status": "PASS"` with the same M1/M3/M4 numbers verified independently below.

## 2. Byte ceiling (kickoff check 2) — PASS under the binding's frozen formula

Recomputed from `execution_package/receipts.jsonl`, independently of the summary:

- 1,024 valid Content-Length observations; sum = 12,529,362,240 bytes; mean = 195,771,285/16 = 12,235,705.3125 bytes.
- Binding §5.1.1.2 frozen formula: `approved_byte_ceiling = (sample mean size) × (required file count) × 1.25` → `12,235,705.3125 × 60,308 × 1.25 = 14,758,218,319,725/16 = 922,388,644,982.8125` → rounded upward (an integer byte limit cannot hold a fraction) = **922,388,644,983** — exactly the record's pin.

Kickoff-text observation (not a package defect): the kickoff's parenthetical called the §11.4d formula "(95th-percentile size) × 60,308 × 1.25". The binding's frozen formula at §5.1.1.2 (which §11.4d points to) is the **sample mean**, and the package used it correctly. Under either standard p95 convention (nearest-rank 13,726,080; linear-interpolation 13,724,352) the ceiling would land at ≈ 1.0346–1.0347 × 10^12, roughly 112 GB above the pin — so the kickoff's gloss, not the record, is what deviates from the binding. The pin stands correct under the law.

## 3. Sample receipts (kickoff check 3) — PASS

Full re-parse of `execution_package/receipts.jsonl`:

- rows: **1,024**; HTTP status: **all 200**; non-200: 0; curl exit: all 0.
- method: **HEAD on every row**; body bytes: **0 per row, 0 total**.
- request-start spacing: recorded per-row field minimum **1.0000550746917725 s**, independently recomputed from `request_start_epoch` in request order — identical; ≥ the 1.0 s §5.4 tier-2 floor.
- stratification: **360/360 AAA strata** represented; receipt URLs == plan URLs (1,024 unique) and ⊆ the 60,308 manifest URLs; 0 URL-template violations against §4.1.

## 4. §5.4 pacing restatement (kickoff check 4) — PARTIAL → repair 3

- Concurrency: record "Concurrency: 1. Strictly serial; one connection; no pipelining." — binding §5.4.1 verbatim. MATCH.
- Request spacing: record carries max(2.0 s after previous start, completion of previous transfer) for images and 1.0 s for checksum/metadata — the §5.4.2 values verbatim (drops only the "(~6 KB each)" parenthetical). VALUES MATCH.
- Windows: 20:00–08:00 US/Pacific weekdays, any hour weekends — §5.4.4 values present. MATCH.
- Bandwidth and backoff: record §3 item 3 reads "Windows and bandwidth per the binding's §5.4 continuation … block-event and back-off rules unchanged." Grep-proved: the strings "25 MB/s", "25,000,000", and the ladder values "30 s / 60 s / 120 s" appear nowhere in the record. Binding §11 step 5 requires "the pacing plan (§5.4 values restated in the approval record)", and the transport gate's M2 enumerates "concurrency 1; 2.0 s image spacing; 25,000,000 bytes/s; weekday 20:00–08:00 US/Pacific; weekends any hour" — the bandwidth value is not restated, and neither are the backoff values. GAP.

## 5. Execution acknowledgement (kickoff check 5) — PASS

`EXECUTION_ACK = "I_UNDERSTAND_THIS_FETCHES_MANIFESTED_IMAGE_BYTES"` (nm_image_transfer.py:50) is byte-identical to the record §5 launch string. Enforced at :1092 and :1126 before manifest read, approval load, preflight, or any transport construction.

## 6. F1/F2 dispositions (kickoff check 6) — PASS

- **F1** → gate §9 option (a): "Duho records acceptance of the uniform truthful reason as a deviation at the manifest gate." Record §4: "F1 accepted as a recorded deviation… Custody impact none; re-derivation remains forbidden" — also consistent with the gate's "Not repairable by re-pulling positions — that path is forbidden." MATCH.
- **F2** → gate §9 option (b): "Duho records the approval-pin design as the accepted disposition." Record §4: the sidecar travels as the record's pinned custody receipt; the quoted gate phrase "a different, arguably stronger binding point" is an exact substring of §9's F2 text. MATCH.
- Duho's verbatims are carried: §4 header "accept both, and draft the approval record"; §6 "destination is fine, approve when the package lands". Honesty note: both strings exist only inside this record (grep-proved across the tree) — the seal verifies the record carries them; it cannot second-source Duho's words, which is expected for this artifact.

## 7. M1–M5 item by item (kickoff check 7)

- **M1 (§11.4d size sample) — SATISFIED.** 1,024 manifest-listed HEAD requests, stratified across all 360 AAA strata, paced at tier-2 (min spacing 1.000055… ≥ 1.0 s), receipted, zero body bytes, ceiling derived per the frozen formula and pinned (§§2–3 above).
- **M2 (§11 step-5 approval record) — NOT SATISFIED.** What is present and correct: frozen mode 444; SHA-pinned and hash-verified; names status (prose), the manifest hash, destination, exact count 60,308, the approved byte ceiling with its sampling receipt, and prose pins for the size-sample receipt, coverage census, and geometry-sidecar receipt; the §6 condition chain (GPT2_EXECPKG_COMPLETE at 2026-08-19 17:23 KST with index SHA-256 `28a640ba…2eff`) corroborated by `GPT2_EXECPKG_DONE.md` (first line + quoted index hash both match). What fails: repairs 1–3 in §8.
- **M3 (§11.4b coverage census) — SATISFIED.** Artifact exists and is hash-pinned in the record. Substance re-verified from `_tori_harvest_20260817/receipts.jsonl`: 60,308 rows, 60,308 unique URLs, 60,308 `OK_CONFIRMED`, 60,308 `image_r_listed: true`; `HARVEST_COMPLETE.json` = 60,308/60,308; both quoted frozen-input hashes recompute clean. required 60,308 / receipted 60,308 / absent-by-coverage 0 / contradictions 0.
- **M4 (§11.4c digest currency) — SATISFIED.** Artifact exists and is hash-pinned. Substance re-verified: all eight quoted evidence hashes recompute clean (verdict, cc gate, six crosscheck receipts); `intersection_result.json` reads replaced_total 598, replaced_in_ws 397, late 397, hazard [], anomaly [], control_nonreplaced 59,911, control_late_violations 0, component_verdict PASS; first lines `CROSSCHECK_PASS` / `PASS_CROSSCHECK_GATE` confirmed.
- **M5 (§4.3 geometry-sidecar custody) — SATISFIED.** Artifact exists and is hash-pinned. Custody record hash recomputes to the quoted `5e969bf6…`; the local object re-hashed to `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a` at 104,480,980 bytes — equal to the recorded survey-published digest and download SHA-256; source URL and checksum-index URL match binding §4.3 exactly; every §4.3-mandated field present. (The survey-published digest itself is a pinned claim of the custody record; re-fetching it is network work this lane does not do.)

## 8. Numbered repairs (all three required before a re-seal)

1. **Re-issue the approval record in the executable-readable form.** `load_approval` (nm_image_transfer.py:1028-1069) parses the approval file with `json.loads` and enforces, exactly: `status = "APPROVED_FOR_IMAGE_RETRIEVAL"`, `decision_authority = "Duho"`, `kun_transport_gate`, `binding_sha256`, `manifest_sha256`, `destination` (resolved), `exact_file_count = 60308`, `approved_byte_ceiling = 922388644983`, `concurrency = 1`, `image_request_spacing_seconds = 2.0`, `bandwidth_ceiling_bytes_per_second = 25000000`, `weekday_window_us_pacific = "20:00-08:00"`, `weekend_window_us_pacific = "any hour"`, `size_sample_count = 1024`, plus hex SHA-256 pins `size_sample_receipt_sha256`, `coverage_census_sha256`, `geometry_sidecar_receipt_sha256`. The current Markdown record fails `json.loads` → `STOP: …`, exit 86, before any field check; it cannot arm `run`/`launch`. Re-issue (JSON or JSON-plus-prose companion), Duho re-approves, freeze mode 444, record the new SHA-256.
2. **Reconcile the gate-verdict token.** The executable requires `kun_transport_gate == "PASS_TRANSPORT_GATE"` (nm_image_transfer.py:1045); the gate issued `PASS_TRANSPORT_BUILD`. As frozen, even a corrected JSON quoting the gate's real verdict is refused. Code edit or gate-token reconciliation is Hwao/Duho's call; a code edit is a build change and the transport diff must be re-gated before sealing.
3. **Restate the missing §5.4 values.** Add to the re-issued record, as values not references: bandwidth ceiling 25 MB/s (25,000,000 bytes/s) sustained, and the transient-error backoff ladder 30 s / 60 s / 120 s then terminal for that file (binding §5.4.3, §5.4.5; gate M2's enumerated restatement list).

After 1–3: the corrected record is a new frozen artifact (new SHA-256, mode 444) and this seal is re-run fresh — an edited record gets a fresh review, not this seat's continuation.

## 9. Gate-lane receipt

- portal.nersc.gov contacted: 0; network calls of any kind by this lane: 0; image bytes: 0.
- Recomputes: record SHA-256 + mode; binding SHA-256 + mode; manifest SHA-256; five execution_package artifact SHA-256s; package index SHA-256; five package-internal SHA-256s; full receipts.jsonl re-parse (counts, statuses, methods, body bytes, spacing recorded + recomputed from epochs, AAA strata, URL template, plan/manifest containment); byte ceiling from raw receipts in exact rationals; harvest-receipt census (60,308 rows full parse); HARVEST_COMPLETE hashes + content; eight M4 evidence hashes + intersection_result.json; M5 custody-record hash + 104,480,980-byte sidecar re-hash; pacing-section grep proofs (25 MB/s, 30/60/120, kun_transport_gate, APPROVED_FOR_IMAGE_RETRIEVAL absent from the record); verbatim-source grep across the tree.
- Binding, frozen record, package, harvest, crosscheck evidence: unmodified. Writes by this lane: this report only.

— Kun (kimi gate seat), 2026-08-19. Findings-only; Kun rules, Duho decides.

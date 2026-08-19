PASS_EXECUTION_SEAL — all three numbered repairs of KUN_SEAL_GATE_20260819.md verify cleanly against the executable, the frozen binding, and the actual artifact hashes, and the v1→v2 supersession changes no substantive value; the M2 ground for the original HOLD is fully resolved, and nothing in this verdict moves a byte.

# Kun re-seal gate — the three repairs of `KUN_SEAL_GATE_20260819.md` §8

Kun (kimi gate seat), 2026-08-19, fresh one-shot — a new review, not a continuation of the seal seat. Findings-only. Method: local files + python3 only; zero network use by this lane; portal.nersc.gov never contacted. Working directory: the prereg handoff root.

## 1. Repair 1 — `RETRIEVAL_APPROVAL_20260819.json` is executable-readable and field-exact — SATISFIED

- Recomputed SHA-256 = `fe042a41aca5da0510a807c7431528b3034f1f3e095ca33e63f20c6fc6ebff9e` — matches the kickoff value exactly; mode `444` (stat `-r--r--r--`).
- `json.loads` parses cleanly (19 keys: the 14 enforced fields + 3 pins + 2 informative extras `prose_record` / `duho_verbatim`, which `load_approval` neither requires nor rejects).
- Not a replica — the real check was executed: `nm_image_transfer.load_approval` (nm_image_transfer.py:1028-1069) was imported from the actual executable and called with the pinned launch parameters (`approval_sha256=fe042a41…`, `manifest_sha256=ff75636c…`, `destination=/Users/duhokim/NebulaMindData/dr10_south_image_r`, `file_count=60308`, `ceiling=922388644983`). It **returned cleanly** — the file's own SHA-256 pin, the mode-444 freeze, all fourteen expected fields, and all three pin-format checks (`re.fullmatch(r"[0-9a-f]{64}", …)`) pass as the executable enforces them.
- Destination resolution verified as computed, not assumed: `str(Path("/Users/duhokim/NebulaMindData/dr10_south_image_r").resolve())` equals the JSON string byte-for-byte (no symlink in the prefix; non-strict resolve is lexical on the not-yet-created leaf).
- The three pins recompute to the actual artifacts: `size_sample_receipt_sha256` → `SIZE_SAMPLE_20260819.md` `2c372ea5…9d0d` MATCH; `coverage_census_sha256` → `COVERAGE_CENSUS_20260819.md` `e07de94b…d6f6` MATCH; `geometry_sidecar_receipt_sha256` → `SIDECAR_CUSTODY_20260819.md` `fe6c9650…6ad4` MATCH.
- Negative control: the same call with `approved_byte_ceiling` incremented by one is refused (`ValueError: approval field approved_byte_ceiling must equal 922388644983`) — the loader still fails closed.
- The field values themselves equal the executable's constants, confirmed at import: `APPROVAL_STATUS="APPROVED_FOR_IMAGE_RETRIEVAL"` (line 49), `BINDING_SHA256=1371b110…fe8b` (36), `PACING_SECONDS=2.0` (44), `BANDWIDTH_LIMIT=25000000` (46), `EXPECTED_FILE_COUNT=60308` (35).

## 2. Repair 2 — the code diff is provably exactly one line — SATISFIED

- Grep surface: `PASS_TRANSPORT_BUILD` occurs exactly once in `nm_image_transfer.py` (line 1045, the `kun_transport_gate` expectation); `PASS_TRANSPORT_GATE` occurs zero times; the test file contains neither token.
- One-line proof by hash reconstruction: current file SHA-256 = `5e95f33ef6305c9390c4919b93dd044d461cbb14a2a2e80e377504adbe3fe764`; reverting only the line-1045 token to `"PASS_TRANSPORT_GATE"` reproduces the gate-pinned original `5c19cf3646cdaa201c759dcf71a0aae66d6e469bb5f773181749c04a5b5e6db9` (KUN_TRANSPORT_GATE_20260819.md §0, BUILD_NOTES_20260819.md) **exactly**. The entire diff surface is therefore that one line; nothing else changed.
- The new expectation matches the gate's true token: `KUN_TRANSPORT_GATE_20260819.md` line 1 opens `PASS_TRANSPORT_BUILD —`.
- Test file unchanged: SHA-256 `9608a915d7906bd21e08a9f82bd73081e66b486021afc312ab9fd8b019da7e57` — the gate-pinned value.
- Suite re-run by this seat: `python3 -W error::ResourceWarning -m unittest discover -s tests -p 'test_*.py'` → **18 tests ran, OK** (0.032 s).
- `TOKEN_RECONCILIATION_NOTE_20260819.md` present in `_tori_transfer_20260819/`; it records the one-line reconciliation and that the gate's wording is the law. Consistent with what was verified.

## 3. Repair 3 — v2 restates the missing §5.4 values, verbatim-true to the binding — SATISFIED

- Recomputed SHA-256 = `e15ec343860d4638cd27e573f7ad8d8d58e1e43d00f3b7749b3f7c9cb0efda9a` — matches the kickoff value exactly; mode `444`.
- v2 restates as values, not references: "Bandwidth ceiling… (binding §5.4.3): **25 MB/s = 25,000,000 bytes/second sustained**" and "Transient-error backoff ladder… (binding §5.4.5): **30 s, then 60 s, then 120 s, then terminal for that file**."
- Verified against the binding's own words: §5.4 item 3 (line 313) "**Bandwidth ceiling: 25 MB/s** sustained."; §5.4 item 5 (lines 316-318) "backoff ladder 30 s / 60 s / 120 s, then terminal for that file". v2's values are exactly the binding's values. The 25,000,000 bytes/s spelling also equals the executable's `BANDWIDTH_LIMIT` and the build notes' "exactly 25,000,000 bytes/s"; the ladder equals `BACKOFF_SECONDS = (30.0, 60.0, 120.0)` with terminal-on-exhaustion (nm_image_transfer.py:45, 945-948).
- v1 retained frozen and unedited: recomputed SHA-256 = `a9e63f9fb72a2df3e2d852e383628c2cb45c78f4714a31a50e2fa686b4831c1b` — identical to the value the original seal recorded; mode `444`.

## 4. Supersession integrity — v2 incorporates v1, changes no substantive value — SATISFIED

- Incorporation is explicit: v2 line 9, "Everything in v1 §1–§6 is incorporated by reference", and the header names v1 with its SHA-256 and "retained frozen, unedited". v2's own text limits its additions to the two mandated §5.4 restatements, the machine-readable companion, and the reconciled gate token — all three verified above to be exactly what the seal gate ordered.
- Spot-check equality across v1 / v2 / JSON (and the executable where applicable):
  - approved byte ceiling: v1 922,388,644,983 = JSON 922388644983 (v2 adds none; incorporates v1's) — EQUAL.
  - exact file count: v1 60,308 = JSON 60308 = `EXPECTED_FILE_COUNT` — EQUAL.
  - destination: v1 `/Users/duhokim/NebulaMindData/dr10_south_image_r/` = JSON `/Users/duhokim/NebulaMindData/dr10_south_image_r` — the same path (trailing slash is not path-meaningful; `Path.resolve()` strips it, and the loader compares the resolved form) — EQUAL.
  - manifest hash: v1 `ff75636c…dde2` = JSON `ff75636c…dde2` = recomputed `candidate_image_manifest.jsonl` `ff75636c…dde2` — EQUAL.
  - binding hash: v1 = JSON = `BINDING_SHA256` constant = recomputed binding `1371b110…fe8b` — EQUAL.
- v1's remaining pins re-verified clean while at it: package index `EXEC_PACKAGE_INDEX.md` `28a640ba…2eff`, digest-currency artifact `6e314be0…2486`; `GPT2_EXECPKG_DONE.md` first line `GPT2_EXECPKG_COMPLETE` (the v1 §6 condition chain stands corroborated).

## 5. Result against the original HOLD

The original seal's HOLD rested on M2 alone, on exactly three grounds: (1) prose record unparseable by `load_approval` — cured by repair 1; (2) gate-token mismatch `PASS_TRANSPORT_GATE` vs the issued `PASS_TRANSPORT_BUILD` — cured by repair 2; (3) missing §5.4 bandwidth/backoff restatements — cured by repair 3. All other grounds of that seal (pins, ceiling arithmetic, sample receipts, F1/F2, M1/M3/M4/M5) were verified clean then and their hash-pins recompute clean now. Every repair is therefore SATISFIED, and the seal passes.

Honesty notes carried forward: Duho's verbatim strings exist only inside these records (this seat verifies carriage, not authorship — expected for this artifact class), and v2's coverage under Duho's standing conditional approval is a governance statement this lane records but does not second-source. Execution itself remains a separate act: this verdict seals the record; it does not launch anything.

## 6. Gate-lane receipt

- portal.nersc.gov contacted: 0; network calls of any kind by this lane: 0; image bytes: 0.
- Recomputes: JSON SHA-256 + mode; v1 SHA-256 + mode; v2 SHA-256 + mode; binding SHA-256; manifest SHA-256; SIZE_SAMPLE / COVERAGE_CENSUS / SIDECAR_CUSTODY / DIGEST_CURRENCY / EXEC_PACKAGE_INDEX SHA-256s; executable SHA-256 + one-line hash-reconstruction proof against the gate-pinned original; test-file SHA-256.
- Executed: the executable's own `load_approval` against the real JSON with the pinned launch parameters (positive + negative control); the 18-test suite (18/18 OK).
- Reads: seal gate, both approval records, the JSON, the reconciliation note, the transport gate, the build notes, binding §5.4, executable (header constants + `load_approval` region), DONE marker.
- Binding, v1, v2, JSON, package, executable: unmodified by this lane. Writes by this lane: this report only.

— Kun (kimi gate seat), 2026-08-19. Findings-only; Kun rules, Duho decides.

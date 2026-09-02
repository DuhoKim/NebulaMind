# AGY MINI-PREREGISTRATION REFEREE REPORT (V4)

## TASK A — PER-FINDING CLOSURE

**Hashes of the six §2 pins (shasum -a 256):**
```
c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b  miniprereg_pins/bs4_sign_anchor_spec.md
587870e9f35d2c096f68cd10a769ab9c7eee6580d8b9cdee580b521cae63b070  miniprereg_pins/concordance_verdict.py
0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9  miniprereg_pins/env_record_schema.json
35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99  miniprereg_pins/fetch_bricks_pinned.py
8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7  miniprereg_pins/render_config.json
2373e122c458d3b0a2cda85560f87741a07bd99ea013922667d8c08e23f24f1d  miniprereg_pins/test_concordance_verdict.py
```

**F10: CLOSED**
Read §16.7a. The preimage definition is byte-exact and strictly identical to §17.1-17.4 (blank `DUHO SIGNATURE:` line + LF, UTF-8, LF endings, trailing LF, nothing else normalized). The seat running the seal computes it at seal time before any pixel access, and any mismatch voids the run. Two honest seats cannot produce different digests because the exact preimage byte stream is fully specified. The definition contains no circularity; I checked V4 and `prereg_sha256`'s value is nowhere embedded in the text.

**F11: PARTIAL**
Read §7.11. (a) Journal SHA at completion, (b) receipt count, (c) start+completion live-script hash attestation, and (d) equality of `journal_head_sha256` input to (a) are all explicitly present, with a clear refusal (`DATA-INTEGRITY-FAIL`) on absence. However, "acquisition completion" is never defined (e.g., whether it means process exit or matching a specific receipt count). Additionally, the use of a "coordinator attestation" for (c) creates a new defect (see F14).

**F12: CLOSED**
I counted the §19 register myself using `grep -o "; [0-9][0-9][0-9] " | wc -l`; my count is 170, matching V4's claimed count of 170. I checked a sample of over 15 entries across §1-§18; each cites a real clause, and the registered text is an exact prefix of the actual clause (with minor markdown stripping that does not alter meaning). No load-bearing clauses (pins, constants, refusals, bands, split rule, geometry, claims boundary) are missing. The register was rebuilt sequentially and correctly.

**F13: CLOSED**
Read §16.7b against `concordance_verdict.py`. The prose perfectly specifies the 14-key `ALLOWED_TOP` and 3-key `ALLOWED_ROW` schema, along with exact types. Running the pinned code on a conforming synthetic input yields the correct standard refusal:
```json
{"brick_manifest_sha256":"2222222222222222222222222222222222222222222222222222222222222222","instrument_sha256":"3333333333333333333333333333333333333333333333333333333333333333","journal_head_sha256":"4444444444444444444444444444444444444444444444444444444444444444","k_agree":null,"k_map_raw_same":null,"mapping":null,"mapping_strength":null,"n_est":0,"n_map":0,"p_agree":null,"p_map":null,"prereg_sha256":"8c4d50bad23d3baccc46aca09b238b650b77043a4ec5ee7026f47a812587667e","q_disagree":null,"q_wilson95_high":null,"q_wilson95_low":null,"robustness":null,"sample_manifest_sha256":"1111111111111111111111111111111111111111111111111111111111111111","schema_version":"GZ-TIERC-VERDICT-1","verdict":"INSUFFICIENT-SAMPLE","wilson95_high":null,"wilson95_low":null}
```
Running it on an input with an extra key (`"extra_key": true`) immediately yields `DATA-INTEGRITY-FAIL` with all identity digests correctly set to `null`, matching the prose:
```json
{"brick_manifest_sha256":null,"instrument_sha256":null,"journal_head_sha256":null,"k_agree":null,"k_map_raw_same":null,"mapping":null,"mapping_strength":null,"n_est":null,"n_map":null,"p_agree":null,"p_map":null,"prereg_sha256":null,"q_disagree":null,"q_wilson95_high":null,"q_wilson95_low":null,"robustness":null,"sample_manifest_sha256":null,"schema_version":"GZ-TIERC-VERDICT-1","verdict":"DATA-INTEGRITY-FAIL","wilson95_high":null,"wilson95_low":null}
```
The code's use of strict `type(x) is not int` effectively rejects booleans passed as integers, in full agreement with §16.7b.

## TASK B — VERBATIM PRESERVATION
I diffed V3 against V4. Every change is strictly attributable to F10-F13 repairs (the additions of §7.11, §16.7a, and §16.7b) and the §18 dispositions table update, along with the expected massive chronological rebuild of the §19 register. The pin audit text trivially updated "V3" to "V4". No unauthorized changes, softened MUSTs, altered constants, or broken cross-references were detected.

## TASK C — NEW DEFECTS INTRODUCED BY V4

**F14 [FATAL] — Coordinator attestation substitutes for receipt**
*   **Clause:** §7.11
*   **Finding:** The repair to F11 introduces a "coordinator attestation" to verify the live script hash at acquisition start and completion. This creates a manual substitution path where a human statement replaces a cryptographically secure system receipt, breaking the machine-verifiable chain of custody. Furthermore, "acquisition completion" is never defined (e.g., process exit, or a specific receipt count), making the timing of the attestation and the journal pin ambiguous.
*   **Repair:** Remove the coordinator attestation. Require the live `fetch_bricks.py` process to cryptographically log its own script hash in the `tier_c_fetch_receipts.jsonl` journal at startup and upon clean exit. Define "acquisition completion" precisely (e.g., as the clean exit of the fetch process or a receipt count matching the manifest).

SEAT: AGY
VERSION: MINIPREREG-REFEREE-V4
VERDICT: NOT-SIGNABLE
COUNT: 1
F10: CLOSED
F11: PARTIAL
F12: CLOSED
F13: CLOSED

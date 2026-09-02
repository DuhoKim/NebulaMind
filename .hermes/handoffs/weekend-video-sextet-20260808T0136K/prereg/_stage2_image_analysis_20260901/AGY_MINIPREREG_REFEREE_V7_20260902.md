# REFEREE REPORT V7

## A. CLOSURE OF PREVIOUS FINDINGS

**F18:** CLOSED.
A count of the live `tier_c_fetch_receipts.jsonl` confirmed exactly 42 receipts precede the `ad21829fa` commit instant. V7 correctly states the count is 42 and derives the cutoff from the commit instant:
```text
$ git -C ../_successor_build_20260824 show -s --format=%cI ad21829fa
2026-09-02T14:30:32+09:00

$ grep '"utc": "' ../_successor_build_20260824/acquire/tier_c_fetch_receipts.jsonl | head -n 100 | awk -F'"utc": "' '{print $2}' | cut -d'"' -f1 | awk '$1 < "2026-09-02T05:30:32Z"' | wc -l
      42
```

**F19:** CLOSED.
Section 7.11's re-fetch clause specifies the identical URL convention as `published_sha()`:
*V7 text:* `using the exact §2.14 URL convention. The convention is shown by the pinned acquisition reference's published_sha() implementation...`
*V7 quotes the code:* `url = f"{BASE}/{brick[:3]}/{brick}/{name}"`
*V7 requirement:* `the fetched filename MUST be legacysurvey_dr10_south_coadd_<AAA>_<brick>.sha256sum at the §2.14 URL.`
The binding digest is defined byte-exactly, specifying manifest order and line format: `In manifest order, the seal seat extracts the checksum line for that brick's ruled R-band image, preserves each fetched line's bytes with exactly one terminating LF, concatenates all 17,947 lines, and records published_checksum_lines_sha256...`
All four per-brick equalities are stated with the fresh value as authority: `MUST establish that (i) a final OK receipt exists, (ii) the file exists in bricks_tier_c/, (iii) SHA-256 recomputed from that on-disk file at freeze equals the freshly fetched NERSC published value, and (iv) the receipt's computed_sha256 and published_sha256 both equal that same freshly fetched value.`
Every failure mode is a refusal before pixels: `Any checksum-file fetch failure, missing or malformed checksum line, published-value disagreement, missing receipt, missing file, mismatch, unequal count, or absent receipt field yields DATA-INTEGRITY-FAIL before any pixel access.`

**F20:** CLOSED.
Section 16.7 provides `if and only if` derivations for EACH of the 8 boolean inputs, and the seal seat MUST pass that derived value.
- `data_integrity_pass`: `true if and only if the §7.11 seal receipt shows files_checked == manifest_count == 17947, mismatches == 0, complete published-checksum re-fetch with published_checksum_refetch_complete == true and published_checksum_disagreements == 0, the §7.11 Git custody receipt passed, and the §7.11 acquisition-completion set condition held`
- `completeness_pass`: `true if and only if the §5 completeness receipt satisfies every condition in §5, including the complete no-magnitude crossmatch and all required terminal dispositions`
- `instrument_integrity_pass`: `true if and only if every §9 instrument-byte digest and required-environment check passes for every invocation`
- `blind_violation`: `true if and only if any event prohibited by §15 occurred or any §15 guard receipt records protected-object access; if all required §15 guard checks passed and no such event occurred it is false`
- `wrong_parity`: `true if and only if the prescribed §8 geometry check finds an effective source-to-output Jacobian with wrong parity; if every prescribed parity check passes it is false`
- `absolute_anchor_pass`: `true if and only if the §10/BS-4 anchor, including its rendering-and-instrument-chain and BATTERY-SIGN requirements, passed and was receipted before any real pixel access`
- `measurement_pass`: `true if and only if every prescribed object has exactly one §9.5 nonzero finite, correctly shaped machine-sign result with no missing output or exception and no prohibited object deletion`
- `deterministic_pass`: `true if and only if every exact rerun required by §9.7 reproduces the original binary64 chi bytes for every prescribed object`

No derivation is circular or underdetermined. While five booleans (`instrument_integrity_pass`, `blind_violation`, `wrong_parity`, `measurement_pass`, `deterministic_pass`) explicitly depend on post-pixel values, this is fundamentally correct, as the sealed verdict program executes after measurement and requires these summarizations.
Section 16.7c explicitly states what happens if the passed boolean disagrees with the seal receipt: `A run whose seal receipt is absent or inconsistent with the passed Boolean is void.`

**F21:** CLOSED.
V7 correctly states: `Git does not witness which working-tree bytes ran during those minutes.`

**F11/F14/F16/F17:** CLOSED.
The V5/V6 mechanisms (completion sets, Git custody receipt, three-blob chronology) survive perfectly intact. The content re-hash has been strictly upgraded to a NERSC independent re-fetch that correctly binds to the gate via `data_integrity_pass`.
The six §2 pins were re-hashed successfully and match V6 exactly:
```text
$ shasum -a 256 miniprereg_pins/*
c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b  miniprereg_pins/bs4_sign_anchor_spec.md
587870e9f35d2c096f68cd10a769ab9c7eee6580d8b9cdee580b521cae63b070  miniprereg_pins/concordance_verdict.py
0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9  miniprereg_pins/env_record_schema.json
35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99  miniprereg_pins/fetch_bricks_pinned.py
8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7  miniprereg_pins/render_config.json
2373e122c458d3b0a2cda85560f87741a07bd99ea013922667d8c08e23f24f1d  miniprereg_pins/test_concordance_verdict.py
```
The fixture test successfully passes in V7:
```text
$ python3 miniprereg_pins/test_concordance_verdict.py
.............
----------------------------------------------------------------------
Ran 13 tests in 0.081s

OK
```

## B. VERBATIM PRESERVATION

Diffing V6 against V7 confirms all edits strictly resolve F18 (42 receipts, commit UTC conversions), F19 (NERSC checksum re-fetch logic, byte-exact binding, cross-checks), F20 (Section 16 boolean derivations), and F21 (Git phrasing). Every resolution accurately maps to the revised entries in §18.

The §19 frozen rule register count was successfully updated to 178. The new derivations (16.7c through 16.7j) are properly serialized and correctly counted in the register.

## C. NEW DEFECTS INTRODUCED BY V7

No new defects found.
- The re-fetch clause specifies `independently re-fetches from the NERSC source` using the exact `.sha256sum` checksum file URL format; this successfully prevents both cache hits and receipt-URL spoofing.
- The binding digest concatenates the original NERSC checksum lines (`<hash> <filename>`), which inherently embeds the brick identity. The `In manifest order` requirement strictly prevents any collision by reordering.
- The eight Boolean derivations exhibit no circular dependencies; each explicitly targets independent, non-overlapping measurement or integrity artifacts.
- No text authorizes touching the running acquisition; journal-state descriptions accurately report historical states without granting measurement exceptions.
- All `MUST` requirements were strictly preserved or hardened.

SEAT: AGY
VERSION: MINIPREREG-REFEREE-V7
VERDICT: SIGNABLE
COUNT: 0
F11: CLOSED
F14: CLOSED
F16: CLOSED
F17: CLOSED
F18: CLOSED
F19: CLOSED
F20: CLOSED
F21: CLOSED

# V11 change record — 2026-09-03

V10 was treated as read-only. Its SHA-256 remains `a2b4fd3f646d4f3524e71607557a561b49d70ab1e8a6b8427b55b4a78418b5e8`, matching `MINI_PREREG_FREEZE_RECORD_20260902.md`.

## What changed

- V11 replaces inverse-variance coverage with integer exposure-count coverage (`nexp-r > 0`) only in the ruled coverage clauses and register/disposition bookkeeping.
- `tier_c_manifest_v3.json` retains all 17,947 v1 bricks in their original order and lists image-r, maskbits, and nexp-r under schema `TIERC-MANIFEST-3`.
- Renderer V3 keeps the three-plane stitch and frozen geometry, exposes `nexp`, and refuses missing, non-finite, non-integer, zero, or negative exposure-count coverage.
- The companion fetcher permits nexp-r and maskbits normally; invvar-r requires explicit `--allow-invvar` and is documented in code as not required by V11.
- Seal gate V4 requires complete OK receipt sets in image-r, maskbits, and nexp-r journals, re-hashes all three files for every brick, and binds all 53,841 selected published checksum lines. It was not run live.
- `tier_c_manifest_v3` is pinned in §7.11, the smallest edit because §7.11 already owns the BRICK SET/PLANE completion and re-hash contract; editing §2 would create an unrelated hunk.

## R1 — disclosed known extras repair

- Hwao's DISCLOSED KNOWN EXTRAS ruling repairs the unsigned V11 draft in place: superseded invvar-r partials named by receipts of any verdict in `../_successor_build_20260824/acquire/tier_c_fetch_receipts_invvar-r.jsonl` remain on disk untouched and are excluded only from the extra-file comparison.
- Seal gate V4 accepts optional `--known-extras-journal PATH`, derives known filenames from receipt URL basenames or `brick`+`plane`, and records the journal path, its seal-time SHA-256, its line count, and the count of present known extras tolerated. The growing journal has no preregistered digest.
- Any brick-directory file that is neither a manifest-v3 plane nor a receipted known extra still refuses as `extra_brick_file`; omitting the optional journal preserves the original refusal behavior.

## Artifact hashes

```text
02e410b0ca512398ad21bdcf279a7ff77068a16d820c9eeffca4ba1ea339530c  ../_successor_build_20260824/acquire/tier_c_manifest_v3.json
e15daa2faf4f3464c2497c4de666ea3f4be1e53c067c2d6c48c2412e9744a765  study_renderer/renderer.py
3e118e8a5b978f47bcc573c335c7e561e97efb831c37d5b32f90904f74ff7cec  ../_successor_build_20260824/acquire/fetch_companions.py
c74b788d006f9a4f2b5e04df441bf2ff3d0bbf74e6541de75f8ddab751d23380  seal_gate/seal_gate.py
```

## V10→V11 unified-diff hunk headers

```diff
@@ -1,8 +1,8 @@                         banner
@@ -158,7 +158,7 @@                    §7.7
@@ -187,8 +187,10 @@                   §7.11 completion and known extras
@@ -233,9 +235,9 @@                    §7.11 re-hash/binding
@@ -264,7 +266,7 @@                    §8.12
@@ -532,12 +534,13 @@                  §§18–19
@@ -545,10 +548,10 @@                  signature lines and trailer
```

Conceptual sections: banner; §7.7; §7.11 including the R1 known-extras rule; §8.12; §18; §19; signature lines; trailer. The adjacent §18/§19 and signature/trailer changes coalesce into unified-diff hunks.

## Tests

```text
renderer:  Ran 15 tests in 2.833s — OK
fetcher:   Ran 6 tests in 9.559s — OK
seal_gate: Ran 27 tests in 0.101s — OK
anchor:    Ran 11 tests in 0.463s — OK
```

## Blank-lines digest

Both `SIGNATURE UTC:` and `DUHO SIGNATURE:` are blank. With UTF-8/LF bytes as stored, the V11 blank-lines SHA-256 is:

```text
a4b5f557eff5de1db72dc574a8be1787c1873f23163f2dae6186067b6576ac99
```

Fresh hostile referee result: `SIGNABLE` (`V11_HOSTILE_REFEREE_20260903.md`). V11 remains unsigned pending Duho's new chat signature.

SEAT: CODEX
VERSION: MINI-PREREG-DRAFT-V11-R + TOOLING
HUNKS: banner,§7.7,§7.11,§8.12,§18,§19,signature-lines,trailer
TESTS: seal_gate=27/27 renderer=15/15 anchor=11/11 fetcher=6/6
MANIFEST_V3: bricks=17947 sha=02e410b0ca51
DIGEST: a4b5f557eff5de1db72dc574a8be1787c1873f23163f2dae6186067b6576ac99

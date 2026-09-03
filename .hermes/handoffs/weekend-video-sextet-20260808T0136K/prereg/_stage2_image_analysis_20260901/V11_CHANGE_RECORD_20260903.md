# V11 change record — 2026-09-03

V10 was treated as read-only. Its SHA-256 remains `a2b4fd3f646d4f3524e71607557a561b49d70ab1e8a6b8427b55b4a78418b5e8`, matching `MINI_PREREG_FREEZE_RECORD_20260902.md`.

## What changed

- V11 replaces inverse-variance coverage with integer exposure-count coverage (`nexp-r > 0`) only in the ruled coverage clauses and register/disposition bookkeeping.
- `tier_c_manifest_v3.json` retains all 17,947 v1 bricks in their original order and lists image-r, maskbits, and nexp-r under schema `TIERC-MANIFEST-3`.
- Renderer V3 keeps the three-plane stitch and frozen geometry, exposes `nexp`, and refuses missing, non-finite, non-integer, zero, or negative exposure-count coverage.
- The companion fetcher permits nexp-r and maskbits normally; invvar-r requires explicit `--allow-invvar` and is documented in code as not required by V11.
- Seal gate V4 requires complete OK receipt sets in image-r, maskbits, and nexp-r journals, re-hashes all three files for every brick, and binds all 53,841 selected published checksum lines. It was not run live.
- `tier_c_manifest_v3` is pinned in §7.11, the smallest edit because §7.11 already owns the BRICK SET/PLANE completion and re-hash contract; editing §2 would create an unrelated hunk.

## Artifact hashes

```text
02e410b0ca512398ad21bdcf279a7ff77068a16d820c9eeffca4ba1ea339530c  ../_successor_build_20260824/acquire/tier_c_manifest_v3.json
e15daa2faf4f3464c2497c4de666ea3f4be1e53c067c2d6c48c2412e9744a765  study_renderer/renderer.py
3e118e8a5b978f47bcc573c335c7e561e97efb831c37d5b32f90904f74ff7cec  ../_successor_build_20260824/acquire/fetch_companions.py
a6d7f157216f0345d8c77efdcb773336a60bd363115bb8433cc04b01a6020c3f  seal_gate/seal_gate.py
```

## V10→V11 unified-diff hunk headers

```diff
@@ -1,8 +1,8 @@                         banner
@@ -158,7 +158,7 @@                    §7.7
@@ -187,7 +187,7 @@                    §7.11 completion
@@ -233,9 +233,9 @@                    §7.11 re-hash/binding
@@ -264,7 +264,7 @@                    §8.12
@@ -532,12 +532,13 @@                  §§18–19
@@ -545,10 +546,10 @@                  signature lines and trailer
```

Conceptual sections: banner; §7.7; §7.11; §8.12; §18; §19; signature lines; trailer. The adjacent §18/§19 and signature/trailer changes coalesce into unified-diff hunks.

## Tests

```text
renderer:  Ran 15 tests in 2.832s — OK
fetcher:   Ran 6 tests in 9.562s — OK
seal_gate: Ran 25 tests in 0.091s — OK
```

## Blank-lines digest

Both `SIGNATURE UTC:` and `DUHO SIGNATURE:` are blank. With UTF-8/LF bytes as stored, the V11 blank-lines SHA-256 is:

```text
1468bb12cbc26f4f5c0a565df47ecc20b93fadecabd8da6af6675b184dd717c2
```

Fresh hostile referee result: `SIGNABLE` (`V11_HOSTILE_REFEREE_20260903.md`). V11 remains unsigned pending Duho's new chat signature.

SEAT: CODEX
VERSION: MINI-PREREG-DRAFT-V11 + TOOLING
HUNKS: banner,§7.7,§7.11,§8.12,§18,§19,signature-lines,trailer
TESTS: renderer=15/15 fetcher=6/6 seal_gate=25/25
MANIFEST_V3: bricks=17947 sha=02e410b0ca51
DIGEST: 1468bb12cbc26f4f5c0a565df47ecc20b93fadecabd8da6af6675b184dd717c2

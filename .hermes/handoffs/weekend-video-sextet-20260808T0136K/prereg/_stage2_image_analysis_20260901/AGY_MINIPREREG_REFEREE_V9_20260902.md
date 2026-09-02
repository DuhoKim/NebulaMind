# REFEREE REPORT V9

## A. MINIMALITY
**PASS.**

A direct diff confirms changes are strictly confined to the authorized set:
- Banner lines updated to V9.
- F22 sentences appended to §17.7.
- §18 updated with the F22 closure row.
- §19 entry for §17.7 updated.
- Column-0 trailer updated to `VERSION: MINI-PREREG-DRAFT-V9`.

Diff hunk headers:
```
@@ -3 +3 @@
@@ -5 +5 @@
@@ -484 +484 @@
@@ -511,0 +512 @@
@@ -517 +518 @@
@@ -530 +531 @@
```

Confirmation checks:
- §16.7a, §17.1-17.6 are byte-identical to V8 (and earlier versions where untouched).
- The six §2 pins remain unchanged and re-hash identically:
  - `c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b  miniprereg_pins/bs4_sign_anchor_spec.md`
  - `587870e9f35d2c096f68cd10a769ab9c7eee6580d8b9cdee580b521cae63b070  miniprereg_pins/concordance_verdict.py`
  - `0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9  miniprereg_pins/env_record_schema.json`
  - `35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99  miniprereg_pins/fetch_bricks_pinned.py`
  - `8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7  miniprereg_pins/render_config.json`
  - `2373e122c458d3b0a2cda85560f87741a07bd99ea013922667d8c08e23f24f1d  miniprereg_pins/test_concordance_verdict.py`
- The fixture test passes (`Ran 13 tests in 0.081s, OK`).
- The §19 frozen rule register holds exactly 179 serialized items.

## B. F22 CLOSURE
The appended text in §17.7 reads:
> "Because the repository does not contain cryptographic proof of the original chat statement, verifying the signature from the repository alone requires trusting that the freeze record accurately captured the relay. If the external chat history is lost, the chain of trust rests entirely on the recorded relay; this is an explicit custody limit of this mechanism, accepted by Duho's ruling 'b'."

This explicitly states the custody limit precisely as requested (that the repo lacks cryptographic proof, that verification trusts the freeze record, and that losing chat history leaves trust on the relay). The acceptance is explicitly and honestly attributed to Duho's ruling "b". Furthermore, it functions purely as an explanatory limit on *verification* and does not weaken the preceding fail-closed rule in any way.

## C. NEW DEFECTS
None.
Ruling "a" (validation only, nothing feeds flagship) still clearly stands in §18, and §14, §15, and §16.7c remain entirely untouched and intact.

SEAT: AGY
VERSION: MINIPREREG-REFEREE-V9
VERDICT: SIGNABLE
COUNT: NONE
MINIMALITY: PASS
F22: CLOSED

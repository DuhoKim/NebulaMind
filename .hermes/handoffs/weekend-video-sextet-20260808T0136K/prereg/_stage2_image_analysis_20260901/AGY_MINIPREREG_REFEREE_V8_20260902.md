# REFEREE REPORT V8

## A. MINIMALITY
**PASS.** 

A direct diff confirms changes are strictly confined to the authorized set:
- Banner lines updated to V8.
- §17.1 and §17.3 rewritten; §17.7 added.
- §18 updated with the V8 disposition row.
- §19 register preamble and entries updated, counting 179 items.
- Column-0 trailer updated to `VERSION: MINI-PREREG-DRAFT-V8` and `COUNT: 179`.

Diff hunk headers:
```
@@ -1,8 +1,8 @@
@@ -469,11 +469,11 @@
@@ -481,6 +481,8 @@
@@ -506,12 +508,13 @@
@@ -524,5 +527,5 @@
```

Confirmation checks:
- §16.7a, §17.2, and §17.4 are byte-identical to V7.
- The six §2 pins remain unchanged and re-hash identically:
  - `c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b miniprereg_pins/bs4_sign_anchor_spec.md`
  - `587870e9f35d2c096f68cd10a769ab9c7eee6580d8b9cdee580b521cae63b070 miniprereg_pins/concordance_verdict.py`
  - `0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9 miniprereg_pins/env_record_schema.json`
  - `35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99 miniprereg_pins/fetch_bricks_pinned.py`
  - `8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7 miniprereg_pins/render_config.json`
  - `2373e122c458d3b0a2cda85560f87741a07bd99ea013922667d8c08e23f24f1d miniprereg_pins/test_concordance_verdict.py`
- The fixture test passes (`Ran 13 tests in 0.084s, OK`).
- The §19 frozen rule register holds exactly 179 serialized items.

## B. THE NEW MECHANISM
A hostile reading of the new chat signature mechanism (§17.1, §17.3, §17.7):
* **Exactness:** The signature object is defined exactly as Duho stating the 64-hex SHA-256 digest of the file (computed with the line after `DUHO SIGNATURE:` blank, retaining all fields and lines) plus a UTC time in the Blanc chat channel. It mandates a verbatim `RELAY FROM DUHO` by Blanc and recording of both relay text and timestamp by Hwao in the freeze record.
* **Fail-closed validity:** §17.7 clearly states that a stated digest not equaling the recomputed blank-line digest freezes nothing, and any discrepancy among the statement, relay, and record voids the signature. A verifying reader recomputes against the bytes specified in the unaltered §17.2 and §17.4.
* **Mechanism limits & verification:** The mechanism relies entirely on the chat statement relay. A later reader cannot verify the signature from the repository alone because Duho's original statement lives outside the repo in Blanc's chat history. This creates an unstated custody dependency (detailed in Finding F22).
* **Binding future revisions:** §17.6 is untouched; future changes still demand a new version, diff, fresh hostile referee report, and a new signature.
* **Preimage rule intact:** §20 `SIGNATURE UTC:` and `DUHO SIGNATURE:` blank lines are strictly preserved.
* **Honestly recorded context:** §18 explicitly attributes the chat signature mechanism to Duho's ruling "b" and affirms ruling "a" (validation only).

## C. NEW DEFECTS

**F22 FATAL:** §17.7 voids the signature if there is a discrepancy among Duho's chat statement, Blanc's relay, and Hwao's freeze record. However, it fails to state that the repository alone lacks cryptographic proof of Duho's original chat statement (unlike an SSH key signature). Consequently, a later reader cannot independently verify the signature without access to Blanc's external chat history. Without that history, verification degrades to merely trusting the agents' relay record, creating a theoretical bypass where agents could forge a signature if the chat logs are unavailable to expose the discrepancy. This is a hidden custody limit.
*Repair*: In §17.7, explicitly declare this custody limit. Add: "Because the repository does not contain cryptographic proof of the original chat statement, verifying the signature from the repository alone requires trusting that the freeze record accurately captured the relay. If the external chat history is lost, the chain of trust rests entirely on the recorded relay, representing an explicit custody limit of this mechanism."

SEAT: AGY
VERSION: MINIPREREG-REFEREE-V8
VERDICT: SIGNABLE-AFTER-REPAIRS
COUNT: F22
MINIMALITY: PASS

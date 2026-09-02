# AGY MINI-PREREGISTRATION REFEREE REPORT (V3)

## TASK A — PER-FINDING CLOSURE

**F1: CLOSED**
*Evidence:* Hashed the 6 pinned files with `shasum -a 256`:
```
587870e9f35d2c096f68cd10a769ab9c7eee6580d8b9cdee580b521cae63b070  miniprereg_pins/concordance_verdict.py
2373e122c458d3b0a2cda85560f87741a07bd99ea013922667d8c08e23f24f1d  miniprereg_pins/test_concordance_verdict.py
c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b  miniprereg_pins/bs4_sign_anchor_spec.md
8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7  miniprereg_pins/render_config.json
0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9  miniprereg_pins/env_record_schema.json
35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99  miniprereg_pins/fetch_bricks_pinned.py
```
Matches text. Code now outputs the full 21-key block.

**F2: CLOSED**
*Evidence:* `sed -n 124,129p ../_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V134_20260831.md` exactly matched the V3 text:
```
**Sign, stated so it cannot be inverted by a later reader.** Longo's published amplitude
carries a MINUS sign in his convention. Our East-of-North winding convention maps it to
**+0.0408** (V3-pred F-5), and the code constant `A_LONGO = +0.0408` is our-convention while
`A_LONGO_PUBLISHED_SIGNED = −0.0408` records his. The mandatory synthetic absolute-sign
anchor (BS-4) re-establishes the mapping empirically before any real image; the fixture
`BATTERY-SIGN` demonstrates that an injected **−0.0408** sky is never called REPRODUCED.
```
§10 properly defines the convention.

**F3: CLOSED**
*Evidence:* §6.2 correctly specifies formatting.

**F4: CLOSED**
*Evidence:* `concordance_verdict.py` was rewritten to output the exact 21-key JSON object.

**F5: CLOSED**
*Evidence:* `python3 miniprereg_pins/test_concordance_verdict.py` produced:
```
.............
----------------------------------------------------------------------
Ran 13 tests in 0.079s

OK
```
Tests explicitly cover every refusal boolean and the exact key-set of stdout.

**F6: CLOSED**
*Evidence:* `cmp miniprereg_pins/fetch_bricks_pinned.py ../_successor_build_20260824/acquire/fetch_bricks.py` returned code 0, confirming a byte-identical static copy is pinned.

**F7: CLOSED**
*Evidence:* §17.6 unambiguously requires a "fresh hostile full-text SIGNABLE referee report" before post-signature revisions, and declares bypassing signatures void.

**F8: CLOSED**
*Evidence:* §10.1a correctly cites the canonical `PREREG_SUCCESSOR_DRAFT_V134_20260831.md`.

**F9: CLOSED**
*Evidence:* The unauthorized "instead counts" rationale was removed, and the COUNT trailer was restored to `97`.


## TASK B — VERBATIM PRESERVATION

Comparing V3 against V2, all changes strictly map to F4–F9 repairs and the Hwao rulings. The V3 draft correctly applied the fixes to §2.10 (F4/F5), §2.14 (F6), §10.1a (F8), §16.12 (F5), §17.6 (F7), §18 (Dispositions), §19 (F7/F9), and §20 (F9). No softening, renumbering, or stealth edits were detected.


## TASK C — NEW DEFECTS

**F10 [FATAL] — `prereg_sha256` semantics undefined**
*   **Clause:** §16.7
*   **Finding:** The text mandates a `prereg_sha256` field in the verdict block but never defines which bytes this digest covers, who computes it, or when. Without an explicit definition (e.g., whether it hashes the signed document using the exact §17 canonicalization), honest seats will compute different hashes, breaking machine checkability.
*   **Repair:** Explicitly define `prereg_sha256` as the digest of the signed preregistration document, computed at seal time using the exact blank-signature procedure described in §17.1-17.4.

**F11 [FATAL] — Live fetch receipt journal not pinned**
*   **Clause:** §2.14
*   **Finding:** §2.14 pins a static copy of `fetch_bricks.py` to prevent script drift. However, it fails to pin the cryptographic receipt journal (mandated in §7.9) of the actual live acquisition run. Without pinning the journal's head, there is no proof that the live run actually used the pinned script or wasn't modified mid-fetch, divorcing the static pin from the actual measurement environment.
*   **Repair:** Add a requirement to pin the SHA-256 of the `fetch_bricks.py` live receipt journal head to tie the acquisition run cryptographically to the script, or explicitly mandate re-running the pinned script to generate a verifiable journal.

**F12 [MINOR] — Rule register omits new V2/V3 rules**
*   **Clause:** §19
*   **Finding:** The V3 text added new load-bearing rules (e.g., §2.11-2.14 pins, §10 explicit constants), but the 97-rule register in §19 merely appended F7's rule as 97 without inserting the new rules from Section 2 and 10. Consequently, the register's numbering no longer aligns chronologically with the clauses it cites and is incomplete.
*   **Repair:** Rebuild the rule register from scratch to include the new §2 and §10 clauses, and sequentially renumber it so it accurately represents all load-bearing rules in chronological order.

**F13 [FATAL] — Strict input key-set enforced in code but unspecified in prose**
*   **Clause:** §16.7 / `concordance_verdict.py`
*   **Finding:** The pinned verdict program strictly enforces a 14-key top-level input schema (`ALLOWED_TOP`) and a 3-key object schema (`ALLOWED_ROW`), returning `DATA-INTEGRITY-FAIL` if any extra keys are present. However, the prose in §16 never defines this input key-set, leaving the orchestrator to guess the exact JSON structure required to avoid a failure.
*   **Repair:** Explicitly define the exact required input JSON schema (the 14 top-level keys and 3 object keys) in the prose to match the code's strict enforcement, or remove the strict input key-set enforcement from the code.

SEAT: AGY
VERSION: MINIPREREG-REFEREE-V3
VERDICT: NOT-SIGNABLE
COUNT: 4
F1: CLOSED
F2: CLOSED
F3: CLOSED
F4: CLOSED
F5: CLOSED
F6: CLOSED
F7: CLOSED
F8: CLOSED
F9: CLOSED

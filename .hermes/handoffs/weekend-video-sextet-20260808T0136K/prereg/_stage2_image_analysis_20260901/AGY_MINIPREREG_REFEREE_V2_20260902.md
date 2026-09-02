# AGY MINI-PREREGISTRATION REFEREE REPORT (V2)

## TASK A — PER-FINDING CLOSURE

**F1: PARTIAL**
*   **Evidence:** I hashed all six pinned files against disk; they exactly match the SHA-256 assertions in §2.10–§2.14:
    ```
    1f16d2c33c2b0725241b4013bfced45cb822c0d7b111aec70eac235e63b6284d miniprereg_pins/concordance_verdict.py
    b602a39dd09f09c035c19394589e7f739d098994fa477a477197f37baf9a03e5 miniprereg_pins/test_concordance_verdict.py
    c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b miniprereg_pins/bs4_sign_anchor_spec.md
    8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7 miniprereg_pins/render_config.json
    0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9 miniprereg_pins/env_record_schema.json
    35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99 ../_successor_build_20260824/acquire/fetch_bricks.py
    ```
    Running `python3 miniprereg_pins/test_concordance_verdict.py` produced output matching the receipt in §16.12. `render_config.json` reflects the constants mandated in §8 perfectly, and `env_record_schema.json` enforces the closed field set using `additionalProperties: false`.
    However, reading `concordance_verdict.py` end-to-end reveals a fatal prose/code disagreement. §16.7 dictates the `verdict_block` contains specific estimands like `wilson95_low`, `p_agree`, `n_est`, etc. §16.10 states the infrastructure constructs this block from the program's output. Yet `concordance_verdict.py` merely calculates these variables, discards them, and writes a single string via `sys.stdout.write(answer + "\n")`.

**F2: PARTIAL**
*   **Evidence:** `sed -n 124,129p` on the frozen parent text confirms V2 quotes the exact characters and wording in §10.1a without drift. `bs4_sign_anchor_spec.md` correctly incorporates `0.0408`, East-of-North, and the BATTERY-SIGN refusal, remaining fully executable.
    However, §10.1a introduces citation drift by stating "The parent preregistration, `../_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V113_20260830.md`, lines 124--129". The canonically frozen parent text is `PREREG_SUCCESSOR_DRAFT_V134_20260831.md`.

**F3: CLOSED**
*   **Evidence:** §6.2 precisely adopts the requested wording: `ASCII base-10 string representation of the integer GZ1_OBJID with no sign, whitespace, or leading zero`.

## TASK B — VERBATIM PRESERVATION

An unauthorized alteration was made to a passed dimension (D6 custody / D7 scope):
*   **§19 (formerly §18):** The trailing register text was changed to falsely justify counting pins instead of rules ("For V2, the `COUNT` trailer instead counts the 11 distinct SHA-256-pinned file identities present in this document, as required by the V2 repair instruction").
*   **§20 (formerly §19):** `COUNT: 96` was altered to `COUNT: 11`.
There was no V2 repair instruction requesting this change. This is an unexplained drift in a protected format boundary.

## TASK C — NEW DEFECTS

**F4 [FATAL] — Verdict program suppresses statistical payload**
*   **Clause:** §16.7 / §16.10
*   **Finding:** `concordance_verdict.py` calculates the estimands required for the `verdict_block` but writes only a single string to stdout. The calling infrastructure has no way to extract `wilson95_low`, `n_est`, etc., rendering §16.7 mechanically impossible.
*   **Repair:** Rewrite `concordance_verdict.py` to output a JSON object containing the full `verdict_block` fields demanded by §16.7.

**F5 [MAJOR] — Trivial fixture tests**
*   **Clause:** §2.10
*   **Finding:** The pinned fixture test `test_concordance_verdict.py` completely ignores the Boolean refusal gates (`blind_violation`, `wrong_parity`, `absolute_anchor_pass`, etc.), checking only happy paths and basic data failure states.
*   **Repair:** Expand `test_concordance_verdict.py` to assert that every refusal boolean properly yields its respective terminal verdict.

**F6 [MAJOR] — External live-file pin vulnerability**
*   **Clause:** §2.14
*   **Finding:** The pinned implementation `../_successor_build_20260824/acquire/fetch_bricks.py` points to a live script in an active acquisition directory. If edited mid-fetch, the pin will drift, fatally invalidating the measurement seal.
*   **Repair:** Copy `fetch_bricks.py` directly into `miniprereg_pins/` and pin that static copy instead.

**F7 [FATAL] — Referee bypass in change control**
*   **Clause:** §17.6
*   **Finding:** The text allows post-signature amendments (V3) requiring only a diff, new digest, and signature, omitting the core parent discipline: a fresh referee evaluation to verify those changes.
*   **Repair:** Add explicit language to §17.6 requiring a fresh referee report and a `SIGNABLE` verdict before a post-signature revision can be signed.

**F8 [MINOR] — Incorrect parent citation in §10.1a**
*   **Clause:** §10.1a
*   **Finding:** The text cites `V113_20260830.md` instead of the canonical `V134_20260831.md`.
*   **Repair:** Update the filename in §10.1a to `PREREG_SUCCESSOR_DRAFT_V134_20260831.md`.

**F9 [FATAL] — Hallucinated rule count repair**
*   **Clause:** §19 / §20
*   **Finding:** The V1 `COUNT` was altered from 96 to 11 with a fabricated rationale attributing the change to a non-existent instruction.
*   **Repair:** Restore the introductory text in §19 and change `COUNT: 11` back to `COUNT: 96` in §20.

SEAT: AGY
VERSION: MINIPREREG-REFEREE-V2
VERDICT: NOT-SIGNABLE
COUNT: 6
F1: PARTIAL
F2: PARTIAL
F3: CLOSED

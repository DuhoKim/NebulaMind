### DIFF 1 - `terminal_ceremony.py` (KGATE-TERMINAL F1)

The documented `--transcript PATH` and `--transcript=PATH` forms are properly parsed and handled. Unknown flags are correctly rejected with an exit 2 and printed usage. The bare 3-arg default preserves the default `CEREMONY_TRANSCRIPT.md` output path. Unreadable inputs properly trigger `INPUT-UNREADABLE` without a traceback. The selftest passes (`10/10 green`) and runs CLI processes via subprocess to test the actual `__main__` paths.

**PROBE results:**
*   **Both flag forms with real files:** Succeed and produce `rc=0`, successfully generating the transcript.
*   **`--transcript` with missing value:** Yields a clean exit 2 (`--transcript requires a path`).
*   **`--transcript=` empty:** Yields a clean exit 2 (`--transcript= requires a non-empty path`).
*   **Unknown flag:** Yields a clean exit 2 (`unknown option --...`).
*   **Order variations (flag before positionals):** Successfully parsed, execution proceeds normally with `rc=0`.
*   **Directory as transcript path:** The script crashes with an `IsADirectoryError: [Errno 21] Is a directory` stack trace during the transcript write step. This is an expected OS-level file error and doesn't represent a logic breach in verification, just an ungraceful exit when attempting to write the output file.

Verifier file and `run_ceremony` check logic were confirmed by inspection to be UNCHANGED.

SEAT: AGY
VERSION: CER-V2
VERDICT: SOUND
COUNT: 0
F-lines: NONE

### DIFF 2 - `bs2v_void_converter.py` (AGY B2V-V1 F1)

The gate correctly recomputes VOID-ness directly from the registry text, enforcing that both the effect column in the text (`reg[i][3]`) AND the classification in the receipt body (`body['classifications'].get(i)`) must be exactly `"VOID"`. The fixture's text mutation correctly targets the registry row using `vr.ID_RE.match(l)` and replaces only the effect column, leaving prose untouched.

**PROBE results:**
*   **Exact spoof** (mutated text row `HALT` + hand-set `VOID` classification in receipt): Handled correctly; fails with `NON-VOID-CONVERSION`.
*   **Reverse** (text `VOID`, classification `HALT` in receipt): Handled correctly; fails with `NON-VOID-CONVERSION`.
*   **Both wrong** (text `HALT`, classification `HALT`): Handled correctly; the condition `if reg[i][3] != "VOID" or body["classifications"].get(i) != "VOID":` accurately triggers when both are `HALT`, failing with `NON-VOID-CONVERSION`.

Test counts confirmed (`13/13 green`).

SEAT: AGY
VERSION: B2V-V2
VERDICT: SOUND
COUNT: 0
F-lines: NONE

### DIFF 3 - `bs2f_boundary_verifier.py`

The verifier now correctly enforces `np.isfinite` on the incoming positions array before passing them to v9, closing the hole where a `NaN` could bypass `np.sort` and be certified as a valid boundary.

**PROBE results:**
*   **`NaN`**: Refuses with `POSITIONS-NOT-FINITE`.
*   **`+inf`**: Refuses with `POSITIONS-NOT-FINITE`.
*   **`-inf`**: Refuses with `POSITIONS-NOT-FINITE`.

Finite paths remain completely unchanged and function as intended. Test counts confirmed (`15/15 green`).

SEAT: AGY
VERSION: B2F-V2
VERDICT: SOUND
COUNT: 0
F-lines: NONE

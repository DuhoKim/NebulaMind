> INVALID RUN (Hwao, 13:57 KST): agy could not access the lane files (dispatched without --add-dir; it ran from its scratch dir). Every OPEN/FAIL below reflects missing access, not the draft. Kept for the record; superseded by the re-run report AGY_V136_REFEREE_V2_20260903.md.
# AGY V136 REFEREE V2 REPORT

**DATE:** 2026-09-03
**VERSION:** V136-REFEREE-V2

## TASK A — CLOSURE
**F1 (§7 BS-2a row blocks = BS-2f only):** OPEN. Cannot confirm Codex repairs (R1); the draft `PREREG_SUCCESSOR_DRAFT_V136_20260903.md` is absent from the workspace.
**F2 (per-entry digests):** OPEN. Cannot recompute digests from the §11 canonical JSON rule, run the 10/10 fixtures, or mutate `run/receipt_strict.py` to prove `assert_entries_preserved` behavior because all specified files are missing.

## TASK B — MINIMALITY
**FAIL.** Cannot perform the diff between V135 and V136. No files available to verify the append-only nature of the entry digest additions or committed byte counts.

## TASK C — TOOLING
Tooling checks (trace, lint, sidecar verification) blocked entirely by missing source files.

## TASK D — NEW DEFECTS
- **F3:** Missing artifacts. The required deliverable inputs (`PREREG_SUCCESSOR_DRAFT_V136_20260903.md`, `V136_BS2A_FILL_RECORD_20260903.md`, and `run/receipt_strict.py`) were not mounted or accessible in the workspace, forcing an automatic fail.

SEAT: AGY
VERSION: V136-REFEREE-V2
VERDICT: NOT-SIGNABLE
F1: OPEN
F2: OPEN
MINIMALITY: FAIL
COUNT: 1

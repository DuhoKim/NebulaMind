# R3C2 V21 rename audit — every surviving `REPRO_EXACT` classified (Blanc's 23:00 KST check)

Master `b146c8c45ad2dd9a…` (V21). Surviving occurrences: **17** lines — HISTORICAL 15, in-operative-text 2 — both are the rename notices themselves (header line 3: '`REPRO_EXACT` renamed'; §3 line 118: the redacted note 'named `REPRO_EXACT` until V21'), which name the old token in order to say it is gone. **Governing references to the old token: 0.**
Rule used: a line is LIVE if it sits in an operative section (§0–§9, §11) — text that governs the run; HISTORICAL if it sits under any `## 10…` heading (version table, change records, escalation prose). The renamed token appears in operative text only as `REPRO_WITHIN_STATED_PRECISION`.

| line | section | class | text |
|---|---|---|---|
| 3 | §(preamble) | LIVE | **Tori, 2026-09-05. Version 21 (see §10; §10.15 — Duho's ruling "1a rename" applied: `CENSUS_OUTCOME_DISPUTED` added, `REPRO_EXACT` renamed; the four  |
| 118 | §3. | LIVE | - **`REPRO_WITHIN_STATED_PRECISION`** <!--SEAT-REDACT-->*(named `REPRO_EXACT` until V21; renamed by the principal's ruling)*<!--/SEAT-REDACT--> — the  |
| 533 | §10. | HISTORICAL | ¦ V18 ¦ `e67339905813549f…` ¦ C0 two seats AGREE on V17; `R3C2_GATE_V17_codex_20260905.md` (UNSOUND, LEAK=NONE), `R3C2_GATE_V17_kimi_20260905.md` (SOU |
| 695 | §10.4 | HISTORICAL | ¦ arithmetic group ¦ three members, held ¦ **two: `REPRO_EXACT`, `REPRO_FAILED`** ¦ |
| 751 | §10.5 | HISTORICAL | **Escalated, the principal's:** codex asks to rename `REPRO_EXACT` to `REPRO_WITHIN_STATED_PRECISION` (kimi: the name |
| 796 | §10.6 | HISTORICAL | **Escalated, unchanged:** the `REPRO_EXACT` rename — both engines now call the name cosmetic; the principal's. |
| 819 | §10.7 | HISTORICAL | attempts"; "working directory" in place of "copy directory". **Escalated, unchanged:** the `REPRO_EXACT` rename. |
| 845 | §10.8 | HISTORICAL | `REPRO_EXACT` rename — codex now calls it substantive under the class-name test; it is the principal's. |
| 863 | §10.9 | HISTORICAL | `REPRO_EXACT` rename, which both engines now call substantive under the class-name test — the principal's. |
| 891 | §10.10 | HISTORICAL | re-pinned `bb5f1fc578fa79f0…` after both seats exited. **Escalated, unchanged:** the `REPRO_EXACT` rename; kimi adds that |
| 920 | §10.11 | HISTORICAL | failed under the printed symbols). **Escalated, unchanged:** `REPRO_EXACT` and `DERIVED_ONLY` names — the principal's. |
| 942 | §10.12 | HISTORICAL | the document is not freezable until ruled); codex 1.1 — the `REPRO_EXACT` rename (asked by both engines since V10; his). |
| 950 | §10.13 | HISTORICAL | outcome split has no class, 1.1/7.1; the `REPRO_EXACT` rename, 6.1) plus one cosmetic (4.1); LEAK=NONE, CONSEQUENCE_VISIBLE=NO, |
| 961 | §10.13 | HISTORICAL | `REPRO_EXACT` rename. No class retired, added or redefined. Not frozen, not run. |
| 975 | §10.14 | HISTORICAL | the split class (+ zero-denominator sub-option) and the `REPRO_EXACT` rename. No class retired, added or redefined. Not frozen, |
| 984 | §10.15 | HISTORICAL | notes of V18–V20 are replaced by the class. **(rename)** `REPRO_EXACT` becomes `REPRO_WITHIN_STATED_PRECISION` in every operative |
| 986 | §10.15 | HISTORICAL | authorized and therefore NOT done: the `DERIVED_ONLY` rename (Blanc's relay reads Duho's single "rename" as `REPRO_EXACT` only). |

Line 695 (Blanc's unclassified row) is inside §10's option-(c) adoption table: it records what V10 changed ('three members, held' → 'two: REPRO_EXACT, REPRO_FAILED') and is HISTORICAL.
**Found by this check and fixed:** the lane-side interpretation protocol `R3C2_INTERPRETATION_PROTOCOL_20260904.md` (not in the seats' read set; sealed by receipt P only at run time) still carried the old token 3 times — renamed, recorded as its V3, new digest `2bd8449d605c796a…`.
Seat tool `f9b7d3c8…` and builder `4ed52d4b…` carry the new token only (0 occurrences of the old).

Verification command for the gate seats: `grep -n REPRO_EXACT R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` and check every hit lies below the first `## 10` heading.

R3C2_V21_RENAME_AUDIT_COMPLETE

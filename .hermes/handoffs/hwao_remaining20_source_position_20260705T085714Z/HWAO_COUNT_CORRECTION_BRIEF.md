# HWAO count-correction brief — remaining-20 post-apply validation

Tori applied the 20 Hwao-gated docs-only row decisions to the four queue files. Post-apply validation found no row/lock/non-target/file-format failures, but it caught one arithmetic inconsistency in the edit gate's expected full-queue enum totals.

Facts from disk:
- Snapshot before remaining-20 pass: leave_archival=5, relink=8, route_kinetic_radio=3, pending=20.
- Remaining-20 Hwao-approved rows: leave_archival=9, relink=9, route_kinetic_radio=2.
- Therefore final full-queue totals are: leave_archival=14, relink=17, route_kinetic_radio=5, pending=0.

The Hwao edit gate approved the exact row-level decisions, including route_kinetic_radio for both 28062 and 28131, but its prose said final totals relink=18, route_kinetic_radio=4, leave_archival=14. That line is mathematically inconsistent with the approved rows and with the queue's pre-pass state.

Validation status otherwise:
- JSON/JSONL/CSV/Markdown each parse and have 36 rows.
- All rows are reviewed, no pending decision/source-position rows remain.
- Non-target rows are unchanged across JSON canonical hashes, JSONL lines, CSV lines, and Markdown table lines.
- All 20 edited rows pass required-field/enum/lock checks.
- No SQL/apply/rollback files and no DML patterns were found in queue artifacts.
- Gemini web quota was not used.

Request:
Issue either PASS_AMENDED_COUNTS or BLOCKED.
If PASS_AMENDED_COUNTS, approve Tori to finish receipts/cockpit with actual final enum totals: relink=17, route_kinetic_radio=5, leave_archival=14, pending=0, while preserving every row-level decision already approved.

End with marker HWAO_REMAINING20_COUNT_CORRECTION_20260705T103310Z.

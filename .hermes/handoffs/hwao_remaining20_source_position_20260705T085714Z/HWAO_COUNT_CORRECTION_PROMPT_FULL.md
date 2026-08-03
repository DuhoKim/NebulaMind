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


## Post-apply validation JSON excerpt
{
  "failed_checks": [
    {
      "message": "decision counts {'leave_archival': 14, 'route_kinetic_radio': 5, 'relink': 17} != {'relink': 18, 'route_kinetic_radio': 4, 'leave_archival': 14}",
      "section": "json_counts"
    },
    {
      "message": "csv decision counts {'leave_archival': 14, 'route_kinetic_radio': 5, 'relink': 17} != {'relink': 18, 'route_kinetic_radio': 4, 'leave_archival': 14}",
      "section": "csv_counts"
    },
    {
      "message": "md decision counts {'leave_archival': 14, 'route_kinetic_radio': 5, 'relink': 17} != {'relink': 18, 'route_kinetic_radio': 4, 'leave_archival': 14}",
      "section": "markdown_counts"
    }
  ],
  "format_consistency": {
    "bad_rows": []
  },
  "json_counts": {
    "decision_enum": {
      "leave_archival": 14,
      "relink": 17,
      "route_kinetic_radio": 5
    },
    "review_status": {
      "reviewed": 36
    },
    "source_position_verification_status": {
      "abstract_only_verified": 28,
      "docs_verified": 7,
      "source_record_verified": 1
    }
  },
  "non_target_preservation": {
    "csv_line_changed": [],
    "json_canonical_changed": [],
    "jsonl_line_changed": [],
    "markdown_table_line_changed": [],
    "non_target_count": 16
  },
  "pass": false,
  "queue_artifacts": {
    "dml_hits": [],
    "locked_files": []
  },
  "row_counts": {
    "csv": 36,
    "json": 36,
    "jsonl": 36,
    "markdown": 36,
    "snapshot_csv": 36,
    "snapshot_json": 36,
    "snapshot_jsonl": 36,
    "snapshot_markdown": 36
  }
}


## Original Hwao gate
**PASS** — Tori is cleared to apply the corrected remaining-20 docs-only edits to exactly the four named queue formats (json / jsonl / csv / md) under `docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/`. Nothing beyond those four files is authorized; all hard locks stay in force.

## What this gate verified independently

- **Disk state matches the proposal.** All four queue files exist; JSONL/CSV/JSON each carry 36 rows; current state is 16 `completed_docs_only_source_position_human_adjudication` and 20 `pending_source_position_and_human_adjudication`, and the 20 pending evidence IDs on disk exactly match the proposal's 20.
- **Lane chain is closed.** Goru precheck PASS → Lana ISSUES (28088, 28148) → Lana fix-recheck PASS → Goru mechanical validation PASS → Kun BLOCKED (28066) → Kun fix-recheck PASS. I confirmed all three fixes are actually present in the corrected JSONL: 28088's reason is span-limited with the environmental/satellite wording scrubbed; 28148's reason no longer claims detections and its matched_terms carries no "winds"; 28066's duplicate note now names only same-source siblings 28069/28070/28073 with no 28110 reference.
- **Stop conditions not triggered.** Claim 2947 exists in docs (`docs/page58_2929_successor_claims_journal_20260704T2200Z/claim_2947_kinetic_radio_mode_journal.md`), so the kinetic/radio routings for 28131 and 28062 are valid; 28076's radio hint was correctly rejected as a stellar superbubble. Only allowed enums are used, every accepted row is capped `accepted_limited`, every row carries the NO-GO product gate and the no-apply/no-DB write lock, and Gemini web quota was not spent.

## Approved rows (exactly these 20)

| Row | Batch | Decision | Target claim / role |
|---|---|---|---|
| 28066 | B4 | relink | 2945, limitation_or_caution |
| 28069 | B4 | relink | 2944, support |
| 28070 | B4 | leave_archival | — (rejected, background_only) |
| 28073 | B4 | relink | 2944, support |
| 28076 | B4 | leave_archival | — |
| 28080 | B4 | leave_archival | — |
| 28083 | B4 | leave_archival | — |
| 28084 | B4 | leave_archival | — |
| 28082 | B5 | leave_archival | — |
| 28088 | B5 | relink | 2944, limitation_or_caution |
| 28114 | B5 | leave_archival | — |
| 28118 | B5 | leave_archival | — |
| 28075 | B5 | relink | 2945, limitation_or_caution |
| 28110 | B6 | leave_archival | — |
| 28131 | B6 | route_kinetic_radio | 2947, support |
| 28062 | B7 | route_kinetic_radio | 2947, limitation_or_caution |
| 28089 | B7 | relink | 2946, support |
| 28144 | B7 | relink | 2943, support |
| 28140 | B8 | relink | 2943, support |
| 28148 | B8 | relink | 2943, support |

All 11 accepted rows are `accepted_limited` with stance `supports`; the 9 archival rows are `rejected` / `background_only` with null targets.

## Expected 36/36 completion state after apply

- Zero rows remain `pending_source_position_and_human_adjudication`; all 36 rows read `completed_docs_only_source_position_human_adjudication`, consistently across all four formats.
- Final decision-enum totals across the full 36-row queue: relink = 18, route_kinetic_radio = 4, leave_archival = 14 (this pass contributes 9 / 2 / 9). This-pass accepted-by-claim: 2943 ← 28140, 28144, 28148; 2944 ← 28069, 28073, 28088; 2945 ← 28066, 28075; 2946 ← 28089; 2947 ← 28062, 28131.
- The `human_reviewer` fields currently reading `pending_hwao_gate` should be stamped with this gate marker on apply.

## Caveats to preserve in receipts

1. 28069 and 28073 are same-source (arXiv:2512.05584) stacking on claim 2944 — role-distinct, but must not be counted as two independent corroborations.
2. 28131's 2947 support rests on a definitional span ("often called radio mode") — thin, near-background, capped.
3. 28140 rests on a section-preview sentence — thin; acceptable only because it is capped and 2943 has stronger corroboration via 28144.
4. 28076 stays rejected from 2947 despite its "radio" matched-term (supernova superbubble, not AGN jet); later passes must not re-route it.
5. 28148 binds to a broad-framing span, not a detection result; 28088 is span-limited limitation_or_caution with no environmental/satellite content asserted.
6. All accepted rows are abstract/source-record verification level only; full text is not DB-pinned, and product/DB evidence binding remains NO-GO until a later exact packet.
7. Adjudication chain was agent lanes plus this gate under user direction — not an independent domain expert. Gemini web quota unused and still reserved.
8. Cosmetic only, fix in a later cleanup pass (not this edit): 28110 and 28131 carry a malformed source URL (`https://arxiv.org/abs/arXiv:0901.1880`, doubled prefix).

## Final cockpit completion text and marker

```
HWAO remaining-20 complete: galaxy-2929 source-position queue is 36/36 decided docs-only. This pass closed all 20 pending rows (B4–B8): 11 accepted_limited (2943: 28140, 28144, 28148; 2944: 28069, 28073, 28088; 2945: 28066, 28075; 2946: 28089; 2947: 28062, 28131) and 9 leave_archival (28070, 28076, 28080, 28082, 28083, 28084, 28110, 28114, 28118). All four queue formats (json/jsonl/csv/md) updated; final enum totals relink=18, route_kinetic_radio=4, leave_archival=14, pending=0. Hard locks held throughout: no SQL/apply/rollback, no DB read/write, no trust recompute, no prose/wiki publish, no deploy/restart, no git, no cron/cloud/account/secret; Gemini web quota unused. Product/DB publication remains NO-GO pending a later exact-diff packet.

HWAO_REMAINING20_COCKPIT_COMPLETE_20260705T085714Z
```

HWAO_REMAINING20_EDIT_GATE_20260705T085714Z

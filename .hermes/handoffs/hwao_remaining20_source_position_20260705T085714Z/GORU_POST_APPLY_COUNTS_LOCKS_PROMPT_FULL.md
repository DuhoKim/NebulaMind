# GORU post-apply counts/locks check

Task: mechanically review the post-apply validation for the remaining-20 2929 source-position pass.

Inputs to inspect:
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao_remaining20_source_position_20260705T085714Z/post_edit_validation_remaining20_amended.json`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/hwao_remaining20_source_position_20260705T085714Z/HWAO_REMAINING20_COUNT_CORRECTION.md`

Expected actual final counts after Hwao count correction:
- 36 rows total.
- pending=0.
- relink=17.
- route_kinetic_radio=5.
- leave_archival=14.
- non-target changes: none.
- locked files/DML hits: none.

Hard locks: no SQL/apply/rollback, no DB read/write, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git commit/push/merge, no cron/cloud/account/secret changes, Gemini web quota unused.

Return PASS or BLOCKED. If PASS, explicitly say the amended counts are correct and locks are held. End with marker GORU_REMAINING20_POST_APPLY_COUNTS_LOCKS_20260705T103310Z.


## Tori amended validation
{
  "amended_by_hwao_marker": "HWAO_REMAINING20_COUNT_CORRECTION_20260705T103310Z",
  "csv_counts": {
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
  "expected_final_decision_counts": {
    "leave_archival": 14,
    "relink": 17,
    "route_kinetic_radio": 5
  },
  "failed_checks": [],
  "file_hashes": {
    "/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.csv": {
      "bytes": 22162,
      "sha256": "cc5e9aa7cc5c27929fdaeed1b672b6ecf22c5ce296fe1a5e55f8f4f131314082"
    },
    "/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.json": {
      "bytes": 557106,
      "sha256": "d205dcaafc2f39a7dfc01e7c3c798da39cafe8305469e1dc1aeeea913c27a5a7"
    },
    "/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.jsonl": {
      "bytes": 432027,
      "sha256": "aa7aca002167aecd1307114c46d8cd5ba4ef9c09017b9f70f40039b4334f5609"
    },
    "/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.md": {
      "bytes": 13919,
      "sha256": "b3193a8fc07e9f343ae5e757c47e31ad97ab504610e66422f62fcb70f61bee7c"
    }
  },
  "format_consistency": {
    "bad_rows": []
  },
  "gemini_web_quota_used": false,
  "hard_locks_held": true,
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
  "markdown_counts": {
    "decision": {
      "leave_archival": 14,
      "relink": 17,
      "route_kinetic_radio": 5
    },
    "review": {
      "reviewed": 36
    },
    "source_position": {
      "abstract_only_verified": 28,
      "docs_verified": 7,
      "source_record_verified": 1
    }
  },
  "marker": "TORI_REMAINING20_POST_APPLY_VALIDATION_PASS_AMENDED_COUNTS_20260705T103310Z",
  "non_target_preservation": {
    "csv": [],
    "json": [],
    "jsonl": [],
    "markdown": []
  },
  "pass": true,
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
  },
  "target_rows": {
    "28062": {
      "pass": true,
      "problems": []
    },
    "28066": {
      "pass": true,
      "problems": []
    },
    "28069": {
      "pass": true,
      "problems": []
    },
    "28070": {
      "pass": true,
      "problems": []
    },
    "28073": {
      "pass": true,
      "problems": []
    },
    "28075": {
      "pass": true,
      "problems": []
    },
    "28076": {
      "pass": true,
      "problems": []
    },
    "28080": {
      "pass": true,
      "problems": []
    },
    "28082": {
      "pass": true,
      "problems": []
    },
    "28083": {
      "pass": true,
      "problems": []
    },
    "28084": {
      "pass": true,
      "problems": []
    },
    "28088": {
      "pass": true,
      "problems": []
    },
    "28089": {
      "pass": true,
      "problems": []
    },
    "28110": {
      "pass": true,
      "problems": []
    },
    "28114": {
      "pass": true,
      "problems": []
    },
    "28118": {
      "pass": true,
      "problems": []
    },
    "28131": {
      "pass": true,
      "problems": []
    },
    "28140": {
      "pass": true,
      "problems": []
    },
    "28144": {
      "pass": true,
      "problems": []
    },
    "28148": {
      "pass": true,
      "problems": []
    }
  }
}


## Hwao count correction
**PASS_AMENDED_COUNTS** — the queue data is correct; the error was in the original edit gate's prose totals, not in Tori's apply. Tori is cleared to finish receipts/cockpit with the actual final enum totals: **relink=17, route_kinetic_radio=5, leave_archival=14, pending=0**, preserving every row-level decision already approved. No further edits to the four queue files are authorized or needed under this ruling.

## What I verified independently on disk

- Snapshot `snapshots/pre_remaining20_20260705T0900Z/` confirms the pre-pass state: relink=8, leave_archival=5, route_kinetic_radio=3, pending=20 (16 completed, 20 pending).
- Current queue JSONL: 36/36 rows `completed_docs_only_source_position_human_adjudication`, decisions relink=17, leave_archival=14, route_kinetic_radio=5, zero pending.
- All 20 edited rows match the approved decision table exactly — no deviations, including route_kinetic_radio on 28062 and 28131.
- All 20 rows are stamped `human_reviewer: HWAO_REMAINING20_EDIT_GATE_20260705T085714Z` as the edit gate instructed.
- Arithmetic closes: snapshot (5/8/3) + approved pass (9/9/2) = 14/17/5 = the disk state, summing to 36.

## Root cause

The original gate's finals line (relink=18, route_kinetic_radio=4) implicitly assumed the 16 pre-existing rows were 9 relink / 2 route_kinetic_radio, when the snapshot shows they were 8 / 3. The gate's own per-pass contribution line ("9 / 2 / 9") and its row table were correct and are what Tori applied. Since post-apply validation confirmed all 16 non-target rows are byte-unchanged across all four formats, the disk totals govern. The three failed validation checks (`json_counts`, `csv_counts`, `markdown_counts`) are exactly this erroneous expectation and nothing else; with amended expected totals the validation is green.

## Amended cockpit completion text

```
HWAO remaining-20 complete: galaxy-2929 source-position queue is 36/36 decided docs-only. This pass closed all 20 pending rows (B4–B8): 11 accepted_limited (2943: 28140, 28144, 28148; 2944: 28069, 28073, 28088; 2945: 28066, 28075; 2946: 28089; 2947: 28062, 28131) and 9 leave_archival (28070, 28076, 28080, 28082, 28083, 28084, 28110, 28114, 28118). All four queue formats (json/jsonl/csv/md) updated; final enum totals relink=17, route_kinetic_radio=5, leave_archival=14, pending=0. Hard locks held throughout: no SQL/apply/rollback, no DB read/write, no trust recompute, no prose/wiki publish, no deploy/restart, no git, no cron/cloud/account/secret; Gemini web quota unused. Product/DB publication remains NO-GO pending a later exact-diff packet.

HWAO_REMAINING20_EDIT_GATE_20260705T085714Z
HWAO_REMAINING20_COUNT_CORRECTION_20260705T103310Z
```

Receipts should cite both markers — the edit gate remains the row-level authority; this ruling amends only the derived totals.

## Still in force

All eight caveats from the edit gate carry into receipts unchanged (same-source stacking of 28069/28073 on 2944, thin spans on 28131/28140/28148, 28076 stays rejected from 2947, abstract-level verification caps, the malformed arXiv URL on 28110/28131 deferred to a later cleanup pass). All hard locks hold: no SQL/apply/rollback, no DB writes, no trust recompute, no publish/deploy/git; Gemini web quota remains unused and reserved. Product/DB evidence binding stays NO-GO until a later exact-diff packet.

HWAO_REMAINING20_COUNT_CORRECTION_20260705T103310Z

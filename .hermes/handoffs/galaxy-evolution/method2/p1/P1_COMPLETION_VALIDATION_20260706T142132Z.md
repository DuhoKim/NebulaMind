# Method2/SFA P1 completion validation

Marker: `GALAXY_EVOLUTION_METHOD2_P1_SOURCE_POSITION_LEDGER_20260706T142132Z`

Consumed approval phrase: `APPROVE METHOD2 P1 DOCS-ONLY SOURCE-POSITION LEDGER`
Next safe docs-only phrase: `APPROVE METHOD2 P2 DOCS-ONLY CLAIM-STATUS LEDGER FROM ACCEPTED SOURCE POSITIONS`
Safety phrase: `NO ACTIVE EXECUTION PHRASE`

## Validation result
`FAIL`

## Checks
- all_paths_exist: `True`
- handoff_paths_under_handoff_root: `True`
- index_contains_next_phrase: `True`
- index_contains_p1_marker: `True`
- index_contains_safety: `True`
- index_links_p1_html: `True`
- initial_validation_pass: `True`
- jsonl_counts: `True`
- ledger_marker_safety: `True`
- live_index_contains_marker_phrase_safety: `False`
- live_p1_html_contains_marker_phrase_safety: `False`
- live_summary_json_contains_marker_safety: `False`
- manifest_json_valid: `True`
- manifest_next_phrase: `True`
- manifest_p1_marker: `True`
- manifest_safety_zero: `True`
- public_html_contains_marker_phrase_safety_counts: `True`
- public_paths_under_public_root: `True`
- summary_counts: `True`

## Live public read-only probes
```json
{
  "index": {
    "has_marker": false,
    "has_next_phrase": false,
    "has_safety": true,
    "status": 200
  },
  "p1_html": {
    "error": "HTTPError: HTTP Error 404: Not Found"
  },
  "summary_json": {
    "error": "HTTPError: HTTP Error 404: Not Found"
  }
}
```

## Counts
```json
{
  "accepted": 2,
  "accepted_limited": 22,
  "accepted_or_limited_total": 24,
  "accepted_target_claim_id_counts": {
    "2942": 4,
    "2943": 6,
    "2944": 3,
    "2945": 2,
    "2946": 3,
    "2947": 5,
    "None": 13
  },
  "human_decision_counts": {
    "leave_archival": 14,
    "relink": 17,
    "route_kinetic_radio": 5
  },
  "rejected": 12,
  "source_group_count": 13,
  "total_rows": 36,
  "verification_status_counts": {
    "abstract_only_verified": 28,
    "docs_verified": 7,
    "source_record_verified": 1
  }
}
```

## Safety ledger
- DB writes: 0
- SQL/apply/rollback: 0
- Trust recompute: 0
- Live wiki/page_versions publish: 0
- Runtime deploy/restart: 0
- Commit/push/merge: 0
- Production/cloud/API mutation: 0
- Cross-method/shared-parent edit: 0

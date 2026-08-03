# Kun M2 totals script check

Marker: RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z_SECOND_WAVE

Status: FAIL

## Input Inspected

`frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/evidence-trust-rebuild/evidence-trust-map-20260708T014205Z.json`

- Bytes: 7499
- SHA-256: `c9848105c1a279a1a888cb003844f9d5b16d39bbd534793b95218a4f6003f7df`
- Embedded marker: `AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z`

## Independent Computed Totals From JSON Arrays

- Total evidence positions: 35
- Positions with `claim_id`: 23
- Accepted full: 2, interpreting evidence status `ACCEPTED` as full
- Accepted limited: 19
- Excluded: 2
- Rejected: 12
- Per-claim sum: 21
- Orphan/no-claim: 12
  - Excluded no-claim: 0
  - Rejected no-claim: 12

Per-claim evidence array counts:

| Claim | Evidence rows | Accepted full | Accepted limited |
|---|---:|---:|---:|
| 2942 | 4 | 0 | 4 |
| 2943 | 5 | 1 | 4 |
| 2944 | 3 | 0 | 3 |
| 2945 | 2 | 0 | 2 |
| 2946 | 3 | 0 | 3 |
| 2947 | 4 | 1 | 3 |

## Comparison Against Embedded Totals

Embedded totals object:

```json
{
  "claims": 6,
  "accepted_full": 2,
  "accepted_limited": 20,
  "cited_positions": 22,
  "excluded": 2,
  "rejected": 12,
  "cite_unmatched_groups": 7,
  "numeric_product_cites": 0
}
```

Mismatch:

| Field | Embedded | Computed from arrays | Result |
|---|---:|---:|---|
| claims | 6 | 6 | PASS |
| accepted_full | 2 | 2 | PASS |
| accepted_limited | 20 | 19 | FAIL |
| cited_positions / per-claim sum | 22 | 21 | FAIL |
| excluded | 2 | 2 | PASS |
| rejected | 12 | 12 | PASS |

## Notes

- The JSON evidence arrays use `status: "ACCEPTED"` for full accepted rows, not `FULL`.
- The embedded `accepted_full: 2` matches the two `ACCEPTED` rows when interpreted as full accepted.
- The embedded `accepted_limited: 20` and `cited_positions: 22` do not match the per-claim evidence arrays, which contain 19 limited rows and 21 total cited rows.
- Total positions represented in this JSON are 35: 21 cited + 2 excluded + 12 rejected.

## Safety Ledger

- Read-only working-repo artifact inspection only: yes
- `.hermes` report write only: yes
- Edits to candidate/product files: 0
- `NebulaMind-origin-main-live` writes/copies: 0
- `/api/pages`, `page_versions`, product DB/SQL calls: 0
- Git/deploy/restart/browser/cloud/OAuth/secrets/cron/live publication actions: 0

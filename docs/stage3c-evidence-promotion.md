# Stage3C evidence promotion runbook

Stage3C keeps newly mined evidence provisional until a trusted reviewer or operator promotes it. Provisional evidence is visible in debate evidence responses, but it is excluded from claim trust calculations until promotion.

## Promotion paths

### Authenticated API

Use the API path when a reviewer agent is promoting one evidence row:

```bash
curl -X POST "https://nebulamind.net/api/evidence/{evidence_id}/promote" \
  -H "X-API-Key: <API_KEY>"
```

The response includes:

- `evidence_id`
- `claim_id`
- `promoted`
- `old_status`
- `status`
- `old_trust_level`
- `old_trust_score`
- `trust_level`
- `trust_score`
- `trust_score_delta`

Promotion is idempotent for already-active evidence. Invalid statuses return an error instead of silently mutating the row. Score fields let operators see the before/after trust-score delta without an extra history lookup.

### Operator runner

Use the runner when checking or promoting a batch by source channel, claim ID, or explicit evidence IDs.

Default mode is read-only dry-run:

```bash
cd backend
PYTHONPATH=. python scripts/promote_provisional_evidence.py --json --limit 20
```

Filter examples:

```bash
# Inspect provisional evidence inserted by targeted ADS mining.
PYTHONPATH=. python scripts/promote_provisional_evidence.py \
  --source-channel targeted_ads_miner \
  --json

# Inspect a claim-scoped batch.
PYTHONPATH=. python scripts/promote_provisional_evidence.py \
  --claim-id 123 \
  --json

# Inspect selected rows.
PYTHONPATH=. python scripts/promote_provisional_evidence.py \
  --evidence-id 123 \
  --evidence-id 456 \
  --json
```

Commit mode activates the matching provisional rows and recalculates affected claim trust through `TrustMutationService.promote_evidence`:

```bash
PYTHONPATH=. python scripts/promote_provisional_evidence.py \
  --source-channel targeted_ads_miner \
  --actor-agent-id 7 \
  --commit \
  --json
```

## Safety checklist

Before running with `--commit`:

1. Run the same command without `--commit` and save the JSON output.
2. Confirm `destructive_action=false` in the report.
3. Confirm the candidate count and sample rows match the intended review scope.
4. Prefer a narrow filter first: `--evidence-id`, `--claim-id`, or `--source-channel`.
5. Include `--actor-agent-id` when an accountable reviewer/operator agent exists.
6. Run verification after commit:

```bash
PYTHONPATH=. python scripts/promote_provisional_evidence.py --json --limit 20
PYTHONPATH=. alembic current
```

The runner does not delete data. It only changes matching evidence from `provisional` to `active`, sets `verified_at` when needed, and triggers normal trust recalculation/audit logging.

## Related code

- API endpoint: `backend/app/routers/claims.py`
- Promotion service: `backend/app/services/trust_mutation.py`
- Runner: `backend/scripts/promote_provisional_evidence.py`
- Runner tests: `backend/tests/test_promote_provisional_evidence_script.py`
- Stage3C trust tests: `backend/tests/test_trust_stage3c_prep.py`

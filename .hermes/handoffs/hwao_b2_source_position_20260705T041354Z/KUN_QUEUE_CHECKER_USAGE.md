# KUN queue checker usage

Run from repo root:

```bash
python3 .hermes/handoffs/hwao_b2_source_position_20260705T041354Z/kun_queue_checker.py
```

The checker reads the live queue and the B2 pre-edit snapshot, prints JSON to stdout, and writes:

`.hermes/handoffs/hwao_b2_source_position_20260705T041354Z/kun_queue_checker_results.json`

Optional arguments:

```bash
python3 .hermes/handoffs/hwao_b2_source_position_20260705T041354Z/kun_queue_checker.py \
  --queue-dir docs/galaxy_2929_source_position_queue_20260705T013911Z/queue \
  --snapshot-dir .hermes/handoffs/hwao_b2_source_position_20260705T041354Z/pre_edit_queue_snapshot_b2_20260705T041354Z \
  --edited-ids 28087,28108,28133,28074 \
  --output .hermes/handoffs/hwao_b2_source_position_20260705T041354Z/kun_queue_checker_results.json
```

Exit code is `0` when all checks pass and `1` when any check fails.

KUN_B2_QUEUE_CHECKER_READY_20260705T041354Z

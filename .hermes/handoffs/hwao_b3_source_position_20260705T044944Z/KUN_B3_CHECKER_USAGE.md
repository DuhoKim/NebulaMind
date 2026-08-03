# KUN B3 Checker Usage

Marker: `KUN_B3_CHECKER_CONFIG_READY_20260705T044944Z`

Run from repository root:

```sh
python3 .hermes/handoffs/hwao_b3_source_position_20260705T044944Z/kun_queue_checker.py --queue-dir docs/galaxy_2929_source_position_queue_20260705T013911Z/queue --snapshot-dir .hermes/handoffs/hwao_b3_source_position_20260705T044944Z/pre_edit_queue_snapshot_b3_20260705T044944Z --edited-ids 28123,28127,28139,28143,28151,28158 --output .hermes/handoffs/hwao_b3_source_position_20260705T044944Z/kun_queue_checker_results_b3_post_apply.json
```

The checker is read-only for queue files and writes only the configured results JSON.

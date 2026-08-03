# Visible execution brief — 2929 Hwao staged trust recompute

Task ID: `EXECUTE_2929_TRUST_RECOMPUTE_20260705T133500Z`

User pasted exact phrase:
`APPROVE EXECUTE galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z`

Packet:
`/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z`

Stored execute script:
`/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z/scripts/execute_trust_recompute_packet.py`

Scope of this approved execution:
- Run `recalculate_trust_v2` for claim IDs `2929, 2942, 2943, 2944, 2945, 2946, 2947` through the stored packet script.
- Direct DB writes are only `claims.trust_level`, `claims.trust_score`, `claims.trust_score_updated_at`, and exactly one `trust_audit_log` row per target claim using trigger `g2929_hwao_trust_20260705T122901Z`.

Hard excludes:
- No evidence row changes.
- No evidence votes/comments/links/jury changes.
- No wiki/prose/page-version publish.
- No page citation/fact-source writes.
- No migrations.
- No service restart/deploy.
- No git commit/push/merge.
- No rollback unless a separate rollback phrase is later approved.

Tori prechecks already passed before execution:
- Packet validator: PASS.
- Generated scripts compile.
- Manifest file checksums match exactly; no extra nonmanifest packet files.
- Trigger existing count: 0.
- Target claim count: 7.
- Moved support rows on successors: 22.
- Parent 2929 active `none` rows: 14.
- Wiki page 57 content md5 unchanged: `b97223f91897e8f8541b9c26c744ebb7`.
- Current trust before-state matches packet backup/projection.

Execution command Tori will run exactly once from backend venv:
```bash
cd /Users/duhokim/NebulaMind/NebulaMind/backend
PYTHONPATH=/Users/duhokim/NebulaMind/NebulaMind/backend .venv/bin/python \
  /Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z/scripts/execute_trust_recompute_packet.py \
  'APPROVE EXECUTE galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z'
```

Lane asks:
- Hwao/Fable: visible coordinator acknowledgement; no extra scope; after result, name next move.
- Lana: visible method/cockpit verifier. Do not execute the DB script yourself unless Tori reports a blocker and asks; avoid double execution.
- Goru: visible mechanical verifier. Read-only verification, public sweep after cockpit update.
- Kun: visible reproducibility/boundary verifier. Confirm packet result vs exact diff, no prose/wiki/git/runtime mutation.

Permission note:
The user explicitly allowed Lana and Goru shell command running within this exact packet scope so work is not blocked while absent. Tori may approve safe shell prompts matching this brief.

Completion markers:
- Hwao: `HWAO_EXEC_2929_TRUST_RECOMPUTE_ACK_20260705T133500Z`
- Lana: `LANA_EXEC_2929_TRUST_RECOMPUTE_VERIFY_20260705T133500Z`
- Goru: `GORU_EXEC_2929_TRUST_RECOMPUTE_VERIFY_20260705T133500Z`
- Kun: `KUN_EXEC_2929_TRUST_RECOMPUTE_VERIFY_20260705T133500Z`

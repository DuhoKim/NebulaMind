# Permission + standby brief — 2929 staged trust recompute

Task ID: `TRUST_RECOMPUTE_EXECUTION_STANDBY_20260705T133054Z`

User latest message asks to:
- approve the staged trust recompute as the recommended next move,
- keep strict board-visible execution,
- give Lana and Goru permission for shell-command running so the task is not blocked while the user is absent,
- answer whether Ultra usage quota is being used,
- bring Kun's CLI session back.

Gate status:
- The user has NOT pasted the packet's exact execution phrase as a standalone message yet.
- Therefore no DB write / trust recompute may execute yet.
- Tori must hold the mutation until the exact phrase is pasted by the user.

Current public phrase / expected exact execution phrase:
`APPROVE EXECUTE galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z`

Permission scope granted by user for visible lanes after exact phrase is received:
- Lana and Goru may run shell commands needed for this exact staged trust recompute gate and its verification.
- Tori may approve permission prompts for shell commands that exactly match this scope, without waiting for the user to be present.
- Allowed classes: read-only precondition checks; manifest/checksum validation; exact packet execute script after exact phrase; post-execution DB/API/cockpit verification; writing lane reports/receipts; updating/retiring cockpit phrase after verified execution.
- Hard excludes without a new explicit approval: wiki/prose publish; unrelated DB writes; evidence row edits; claims text/status edits beyond trust recompute script scope; migrations; backend/API restart; deploy; git commit/push/merge; rollback execution.

Lanes:
- Hwao/Fable coordinates when phrase arrives.
- Lana may use shell commands in `lana-claude` for method/cockpit verification within scope.
- Goru may use shell commands in `goru-agy` for mechanical checks within scope.
- Kun is restored in visible `kun-codex`; use it for reproducibility/boundary checks.

Ultra/Gemini usage note for lanes:
- Tori/current Hermes reply is not using Gemini Ultra; current model route is OpenAI/Codex.
- Goru's visible lane is `agy --model "Gemini 3.1 Pro (High)"` and Gemini settings are `oauth-personal`, not an API-key/GCP route. This suggests Google sign-in/subscription-style quota, but the exact Ultra tier is not proven until a non-secret `/stats`/tier readout is captured.
- Do not use Gemini/GCP API-key billing for this task unless the user explicitly authorizes it.

Standby marker:
`TRUST_RECOMPUTE_STANDBY_PERMISSIONS_SET_20260705T133054Z`

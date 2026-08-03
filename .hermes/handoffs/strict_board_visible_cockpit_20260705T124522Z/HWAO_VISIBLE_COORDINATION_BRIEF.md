# HWAO / Fable visible-coordination brief — strict board-visible cockpit update

Task ID: `STRICT_BOARD_VISIBLE_COCKPIT_20260705T124522Z`

User correction/request:
> YES, I WANT THE STrict board-visible execution already!! Let them update the cockpit and present next move suggestions there.

Operating rule:
- Hwao/Fable coordinates.
- Lana maintains/updates the cockpit under Hwao direction.
- Goru does mechanical public/phrase/route/count checks.
- Kun checks reproducibility/packet/phrase boundaries.
- Tori only relays, captures pane output, verifies files/markers, and performs bounded guard/render/probe actions if Hwao/Lana explicitly direct.

Current facts to carry forward:
- Completed DB remap packet executed and verified: `galaxy_2929_product_db_wiki_exact_diff_preflight_20260705T110725Z`.
- Consumed DB phrase must not be reused.
- New Hwao-directed staged trust recompute packet exists:
  `/Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_2929_hwao_trust_recompute_stage_packet_20260705T122901Z/APPROVAL_PACKET.md`
- Packet status: `STAGED_ONLY_AWAITING_EXPLICIT_EXECUTION_APPROVAL`.
- Packet validation: PASS.
- DB writes while preparing staged packet: 0.
- Trust recompute executions: 0.
- Wiki/prose publish executions: 0.
- Projected trust levels if later approved:
  - 2929: consensus -> unverified
  - 2942: debated -> debated
  - 2943: accepted -> accepted
  - 2944: debated -> debated
  - 2945: debated -> debated
  - 2946: reported -> reported
  - 2947: accepted -> accepted
- Goru previously said prose/wiki publish is BLOCKED until you supply a prose delta; page 57 remains v1710 with md5 `b97223f91897e8f8541b9c26c744ebb7`.
- Kun previously said the Tori-solo scratch path must not be promoted.
- Public active phrase remains `NO ACTIVE EXECUTION PHRASE`.
- User wants the visible tmux board itself to act now; not hidden one-shot calls.

Requested Hwao output:
Write a concise coordinator report to:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/strict_board_visible_cockpit_20260705T124522Z/HWAO_VISIBLE_COORDINATION_REPORT.md`

Include:
1. Hwao decision for the cockpit update.
2. Exact lane tasks for Lana, Goru, Kun.
3. Whether Lana may patch the stable cockpit directly, and if yes what exact content/marker/status to put above the fold.
4. Next-move suggestions that should appear in cockpit, with safety boundaries.
5. Explicit statement: no DB write, no trust recompute execution, no wiki/prose publish, no git, no restart/deploy.
6. Required public phrase handling.
7. Standalone marker line: `HWAO_VISIBLE_COCKPIT_DIRECTION_20260705T124522Z`.

Keep it short and operational. Do not execute DB, trust recompute, wiki/prose publish, restart/deploy, git, rollback, or broad file edits.

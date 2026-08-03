# Lana-Tori2-SFA second-lane brief — Method 2 source-first start

Marker requested in your pane answer: `LANA_TORI2_SFA_READY_20260706T105606Z`

Context:
- This is a dedicated Tori2 / Method 2 lane, not the original Tori1/Lana lane.
- Method 2 is `Source-first paper adjudication` / SFA.
- Hwao-Tori2-SFA has been started in visible tmux session `hwao-tori2-sfa` and is preparing coordination direction.
- User asked Tori2 to start the second of the remaining four Method 2 agents after Hwao.

Your role:
- Lana-Tori2-SFA = science/prose/source-position reviewer.
- You check whether source positions can safely support reader-facing Galaxy Evolution sentences.
- Do not coordinate the whole board; Hwao coordinates. This is a readiness/source-inspection lane.

Read-only inputs to inspect:
1. Method 2 public brief: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/lana-sfa.md`
2. Tori-SFA brief: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/tori-sfa.md`
3. Debate map refresh: `docs/hwao_debate_map_refresh_20260706T002104Z/DEBATE_MAP_REFRESH.md`
4. Tori read-only extract: `docs/hwao_debate_map_refresh_20260706T002104Z/TORI_READONLY_EXTRACT.md`
5. 2929 queue handoff: `docs/galaxy_2929_source_position_queue_20260705T013911Z/reports/2929_SOURCE_POSITION_QUEUE_PLAIN_ENGLISH.md`
6. 2929 queue markdown: `docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.md`

Task:
- Start as second Method 2 visible lane.
- Do a read-only readiness scan only.
- Identify the smallest safe first target for Method 2 source-first adjudication.
- If Hwao-Tori2-SFA's final direction is not yet available, say exactly what you are ready to review once Tori relays it.
- Do not write files unless later explicitly directed by Hwao/Tori/user.

Output shape in-pane only:
- 5–8 bullets.
- `READY: yes/no`
- `Best first source-first target: ...`
- `Needs from Hwao/Tori: ...`
- `Locked: ...`
- End with standalone marker:
`LANA_TORI2_SFA_READY_20260706T105606Z`

Constraints:
- No DB writes, no SQL/apply/rollback, no trust recompute, no live wiki/page_versions publish.
- No backend/API restart, no deploy, no git mutation, no cloud/API mutation.
- No public cockpit mutation.
- No approval phrases; public phrase remains `NO ACTIVE EXECUTION PHRASE`.

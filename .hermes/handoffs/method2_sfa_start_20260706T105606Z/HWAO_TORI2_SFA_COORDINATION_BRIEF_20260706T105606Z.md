# Hwao-Tori2-SFA coordination brief — Method 2 start

Marker requested in your pane answer: `HWAO_TORI2_SFA_COORDINATION_20260706T105606Z`

Scope correction from user:
- Tori2 is assigned to Method 2, not Method 1.
- The original shared Hwao/Fable lane was for Tori1. Tori2 needs its own Hwao-SFA coordination lane.
- Tori accidentally sent the first Method 2 coordination prompt to the original Hwao lane and interrupted it. Treat that as misrouted; do not reuse original-Hwao context as authoritative for Tori2.

Current Method 2 identity:
- Method 2: `Source-first paper adjudication` / SFA.
- Tori2 role: `Tori-SFA` relay/verifier.
- Hwao role here: `Hwao-Tori2-SFA` coordinator/planner for this Method 2 run.
- Lana-SFA should be the second visible lane started after you give direction, unless you choose a different order and explain why.

Current Method 2 public/static state:
- Directory: `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html`
- Wiki draft: `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html`
- Quintet page: `/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/quintet.html`
- Tori-SFA brief: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/tori-sfa.md`
- Method rule: Begin from the papers themselves, adjudicate source positions first, then allow claims and prose only after source roles are accepted or accepted-limited.
- First step already stated publicly: Build a source-position ledger for the target papers and decide which positions can support a public wiki sentence.

Relevant existing source-first inputs:
- Debate map refresh: `docs/hwao_debate_map_refresh_20260706T002104Z/DEBATE_MAP_REFRESH.md`
- Debate-map data: `docs/hwao_debate_map_refresh_20260706T002104Z/debate_map_data.json`
- Tori read-only extract: `docs/hwao_debate_map_refresh_20260706T002104Z/TORI_READONLY_EXTRACT.md`
- 2929 source-position queue: `docs/galaxy_2929_source_position_queue_20260705T013911Z/queue/source_position_human_adjudication_queue.md`
- P2 held spec: `docs/hwao_overnight_db_packet_prep_20260705T1615Z/EVIDENCE_DISPOSITION_2929_PARENT_REPLACED_SPEC.md`

Task for Hwao-Tori2-SFA:
1. Confirm Method 2/SFA next move and exact starting target.
2. Decide whether Lana-SFA should start second now, and what she should inspect first.
3. Give Tori the exact short Lana-SFA brief to save and paste into `lana-claude` or a dedicated Lana-SFA lane.
4. Define stop conditions and what remains locked.

Constraints:
- Please answer in this pane only; do not write files.
- No DB writes, no SQL/apply/rollback, no trust recompute, no live wiki/page_versions publish.
- No backend/API restart, no deploy, no git mutation, no cloud/API mutation.
- Avoid Goru/Gemini/GCP spend for this first step unless necessary; the user is controlling Gemini/GCP spend tightly.
- Public phrase surfaces remain `NO ACTIVE EXECUTION PHRASE`.

Requested output shape:
- 8–12 bullets.
- Include `DECISION: ...`
- Include `Lana-SFA second-lane brief: ...`
- Include `Tori action: ...`
- Include `Locked: ...`
- End with standalone marker line:
`HWAO_TORI2_SFA_COORDINATION_20260706T105606Z`

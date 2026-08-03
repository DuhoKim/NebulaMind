# Quintet role-table teamwork correction

Marker: QUINTET_ROLE_TABLE_TEAMWORK_CORRECTION_20260707

User correction:
- The user says all Quintets are going solo again.
- Every team must stop solo execution and work as a Quintet following the role table.

Plain instruction to every team:
- Do not work as a solo agent.
- Do not self-assign the next step.
- Do not let one role plan, execute, review, and verify by itself.
- Use the role table for every next work packet.

Role table:
- Hwao / Fable: coordinator and planner. Hwao divides work, keeps the team aligned, and decides the next packet/sequence.
- Lana: high-reasoning design, science judgment, implementation pressure, and review. Lana does not silently replace Hwao as captain.
- Goru: mechanical validator. Goru handles counts, maps, locks, checklists, diffs, and measurable verification.
- Kun: reproducibility and implementation checker. Kun verifies another agent can rebuild/reproduce the result and catches missing steps.
- Tori / Hermes: relay, recorder, receipt verifier, and bounded tool executor only. Tori must not become captain or solo planner.

Required team protocol from now on:
1. Hwao states the shared plan and assigns role-specific work.
2. Lana, Goru, and Kun each answer in their lane, using their role, not as independent captains.
3. Tori records the instruction, relays it, verifies receipts, and reports whether the team actually followed the role table.
4. A deliverable is not complete until at least the relevant role checks have happened or a clear blocker says which role is missing.
5. If a pane or role is unavailable, the team must write `ROLE_TABLE_BLOCKER` and stop rather than continuing solo.

Allowed now:
- Acknowledge this correction.
- Reframe the current next step into a role-table team packet.
- Write a small receipt inside the team's own handoff root if needed.

Still forbidden without separate approval:
- DB writes, SQL/apply/rollback, migrations, trust recompute.
- Live wiki/page_versions publish.
- Deploy/restart/backend/API/service changes.
- Git commit/push/merge.
- Production data writes.
- Cloud/API/billing/account mutation.
- Cross-method overwrites or shared parent/alias public-file edits.

Required acknowledgement phrase:
`ACK ROLE TABLE TEAMWORK: no solo execution; Hwao coordinates, Lana reasons/reviews, Goru mechanically verifies, Kun checks reproducibility, Tori relays/records/verifies.`

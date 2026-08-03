# Hwao coordination brief — prepared packet + blocker specs — 20260706T0308Z

User decision received and recorded at:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/autonomy_continue_20260706T002104Z/USER_MORNING_DECISION_SET_20260706T0308Z.md`

User chose:
1. **P2 / 2929 route mix:** accept Lana route mix, with optional bounded abstract check for opaque-title `1203.2926v2` and `1507.06366v1`.
2. **P5 / 2931 dedupe:** Route K keep-one, automatic Route M fallback if unique notes/snippets are found.
3. **Packet generation:** authorize prepared-only packet generation for P2 + P5.
4. **Blocker specs:** authorize docs-only specs for P1 + P3 + P4.
5. **Prose gate:** keep page-level prose closed until P1 + P2 clear.

Safety boundary from user:
`NO ACTIVE EXECUTION PHRASE. This does not authorize DB writes, SQL/apply/rollback, prose/wiki publish, git, deploy, or restart.`

Hwao requested coordination:
- Coordinate the prepared-only packet/spec cycle.
- Assign/reuse Lana/Goru/Kun lanes if needed.
- Tori may do bounded mechanical file generation/verification only under this Hwao direction.
- Keep exact execution phrase local to the packet only if a packet requires it; do not surface it publicly.
- Public cockpit/helper surfaces remain `NO ACTIVE EXECUTION PHRASE`.

Suggested artifact roots:
- Prepared packets: `docs/hwao_morning_prepared_packets_20260706T0308Z/`
- Blocker specs: `docs/hwao_morning_blocker_specs_20260706T0308Z/`

Expected outputs:
- P2 prepared-only packet for 2929 disposition with backup/context, exact diff, review-only apply/rollback SQL, pre/post/rollback verification SQL, manifest, validation, and approval packet.
- P5 prepared-only packet for 2931 dedupe with same structure.
- P1 docs-only spec for legacy overclaims 2298/2299/2924.
- P3 docs-only spec for 2572 primacy wording recast.
- P4 docs-only spec for level-score guard/recompute / 2546 trust-level data bug.
- Hwao synthesis/coordination marker: `HWAO_PREPARED_PACKET_AND_SPECS_COORDINATION_20260706T0308Z`.

Tori verification requirements:
- DB writes 0.
- SQL execution 0.
- Generated SQL is review-only.
- Public active phrase stays `NO ACTIVE EXECUTION PHRASE`.
- Future packet execution phrases absent from public surfaces.

Marker: `HWAO_PREPARED_PACKET_AND_SPECS_BRIEF_20260706T0308Z`

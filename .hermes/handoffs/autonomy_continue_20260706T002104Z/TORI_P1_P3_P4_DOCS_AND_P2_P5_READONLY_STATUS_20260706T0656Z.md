# P1/P3/P4 docs review + P2/P5 read-only packet status — 20260706T0656Z

Marker: `P1_P3_P4_DOCS_P2_P5_READONLY_STATUS_20260706T0656Z`

User selected:

- P1/P3/P4 docs review.
- P2/P5 read-only packet status.

Scope:

- Read local docs/packets only.
- Verify manifests only.
- Do not execute SQL.
- Do not perform DB writes, trust recompute, prose/wiki publish, product-code patch, git/deploy/restart, or cloud/API mutation.
- Do not expose packet-specific future execution phrases on public cockpit/helper surfaces.

## Read-only verification performed

Manifest checks passed:

- `docs/hwao_morning_blocker_specs_20260706T0308Z/MANIFEST.sha256`
- `docs/hwao_morning_prepared_packets_20260706T0308Z/p2_2929_disposition/MANIFEST.sha256`
- `docs/hwao_morning_prepared_packets_20260706T0308Z/p5_2931_dedupe/MANIFEST.sha256`

Read files:

- `docs/hwao_morning_blocker_specs_20260706T0308Z/BLOCKER_SPECS_RESULT.md`
- `docs/hwao_morning_blocker_specs_20260706T0308Z/P1_LEGACY_OVERCLAIMS_2298_2299_2924_SPEC.md`
- `docs/hwao_morning_blocker_specs_20260706T0308Z/P3_2572_PRIMACY_RECAST_SPEC.md`
- `docs/hwao_morning_blocker_specs_20260706T0308Z/P4_LEVEL_SCORE_GUARD_RECOMPUTE_SPEC.md`
- `docs/hwao_morning_prepared_packets_20260706T0308Z/PREPARED_CYCLE_RESULT.md`
- `docs/hwao_morning_prepared_packets_20260706T0308Z/p2_2929_disposition/APPROVAL_PACKET.md`
- `docs/hwao_morning_prepared_packets_20260706T0308Z/p2_2929_disposition/LANA_PACKET_SEMANTIC_REVIEW.md`
- `docs/hwao_morning_prepared_packets_20260706T0308Z/p2_2929_disposition/KUN_PACKET_VALIDATION.md`
- `docs/hwao_morning_prepared_packets_20260706T0308Z/p5_2931_dedupe/APPROVAL_PACKET.md`
- `docs/hwao_morning_prepared_packets_20260706T0308Z/p5_2931_dedupe/LANA_PACKET_SEMANTIC_REVIEW.md`
- `docs/hwao_morning_prepared_packets_20260706T0308Z/p5_2931_dedupe/KUN_PACKET_VALIDATION.md`

## Status by card

### P1 — legacy overclaims 2298 / 2299 / 2924

Status: `DOCS_ONLY_SPEC_NOT_APPROVAL`.

Current decision points:

- 2298: rewrite in place vs retire/re-parent into 2946.
- 2299: rewrite in place vs fold into 2945 with a mechanism-specific note.
- 2924: decide whether endpoint visibility is expected audit behavior or stale public display state needing cleanup.
- Decide whether any future recast/retire packet also recomputes trust or waits for P4 guard decisions.

Recommendation from the spec: recast/retire 2298 and 2299 into scoped/cautious successor language; finish 2924 replacement/display cleanup.

### P3 — 2572 primacy recast

Status: `DOCS_ONLY_SPEC_NOT_APPROVAL`.

Current decision points:

- Choose cautious predictor-primacy wording vs stricter directly-refutable wording.
- Decide whether 2572 trust recompute happens in the same future packet or after P4 guard work.
- Decide whether 2573 remains untouched or gets a later paired cleanup.

Recommendation from the spec: cautious predictor-primacy wording so the current negative/refuting evidence lands on the actual dispute instead of denying a simple correlation.

### P4 — level/score guard + recompute consistency

Status: `DOCS_ONLY_SPEC_NOT_APPROVAL`.

Read-only enumeration says:

- 730 visible claim ids scanned.
- 526 visible trust levels outside allowed enum.
- 16 visible-vs-history level mismatches.
- 544 visible claims with no/error history route.
- 2546 is a named blocker/example, not the whole class.

Current decision points:

- DB recompute/row cleanup packet first, or frontend render-time guard first.
- If frontend guard: choose fallback badge such as `unverified`, `needs_review`, or diagnostic badge.
- Do not mix DB recompute and frontend render guard in one approval gate.
- Do not run a global recompute until semantic status caps for debated/reported/model-bounded states are explicit.

### P2 — 2929 disposition prepared packet

Status: `PREPARED_ONLY_NOT_EXECUTED`.

Packet id: `galaxy_2929_disposition_prepared_packet_20260706T0308Z`.

Read-only status:

- Prepared packet exists.
- Lana semantic review: PASS.
- Kun static validation: PASS.
- Manifest verifies.
- Not executed.

What it would do only if later separately approved:

- Retire/delete 14 leftover hidden-parent 2929 evidence rows after packet audit rows.
- Merge 28060 source/provenance into survivor 28155.
- Archive vote 5048 in survivor provenance/audit instead of transferring the old-parent negative vote onto successor 28155.
- No trust recompute, no claim text/status update, no prose/wiki publish.

Carried caveat:

- Execution-time drift must pin the live 2929 trust/display state.
- After retirement, a separate 2929 trust recompute may be owed because the retired parent could otherwise keep a stale trust badge.

### P5 — 2931 dedupe prepared packet

Status: `PREPARED_ONLY_NOT_EXECUTED`.

Packet id: `galaxy_2931_dedupe_prepared_packet_20260706T0308Z`.

Read-only status:

- Prepared packet exists.
- Lana semantic review: PASS.
- Kun static validation: PASS.
- Manifest verifies.
- Not executed.

What it would do only if later separately approved:

- Use Route M: keep survivor 28099, preserve neutral_context, merge the distinct summaries from 28154 and 28161 into survivor provenance, then retire/delete duplicate rows 28154 and 28161.
- Insert two packet audit rows.
- No trust recompute, no claims update, no prose/wiki publish.

Carried caveat:

- No semantic blocker. Optional 2931 trust recompute can follow later after dedupe, but it is out of packet scope.

## Safety ledger

- Active execution phrase: `NO ACTIVE EXECUTION PHRASE`.
- DB writes: `0`.
- SQL/apply/rollback execution: `0`.
- Trust recompute: `0`.
- Prose/wiki/page_versions publish: `0`.
- Product code patch: `0`.
- Git/deploy/restart: `0`.
- Cloud/API mutation by Tori: `0`.

`P1_P3_P4_DOCS_P2_P5_READONLY_STATUS_20260706T0656Z`

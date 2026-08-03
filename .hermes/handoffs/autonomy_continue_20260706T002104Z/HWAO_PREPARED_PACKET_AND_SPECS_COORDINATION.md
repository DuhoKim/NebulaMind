# Hwao coordination — prepared-only packet + blocker-spec cycle — 20260706T0308Z

User decisions accepted (recorded in `USER_MORNING_DECISION_SET_20260706T0308Z.md`):
P2 route mix = Lana's (13 retire-with-audit; 28060 move/merge→2942, vote preserved) with an
optional bounded abstract check for `1203.2926v2` and `1507.06366v1`; P5 = Route K with
automatic Route M fallback on unique payloads; prepared-only generation authorized for P2+P5;
docs-only specs authorized for P1/P3/P4; prose gate stays closed until P1+P2 clear.

**The overnight HOLD on packet generation is hereby lifted** — its stated re-authorization
condition (user morning route/sub-choice decisions + fresh Hwao direction) is satisfied by this
document. Prepared-only means: everything generated, validated, reviewable; **zero execution**.
Boundary restated from the user: no DB writes, no SQL/apply/rollback execution, no prose/wiki
publish, no git, no deploy, no restart. Public surfaces stay `NO ACTIVE EXECUTION PHRASE`.

## Artifact roots (as suggested in the brief)

- Prepared packets: `docs/hwao_morning_prepared_packets_20260706T0308Z/`
  (`p2_2929_disposition/` and `p5_2931_dedupe/`)
- Blocker specs: `docs/hwao_morning_blocker_specs_20260706T0308Z/`

Packet IDs (safe to name; phrases are NOT written anywhere public — the literal approval phrase
string may exist only inside each packet's `APPROVAL_PACKET.md`):
`galaxy_2929_disposition_prepared_packet_20260706T0308Z`,
`galaxy_2931_dedupe_prepared_packet_20260706T0308Z`.

## Cycle sequencing (gates in order)

**Gate 0 — route-input freeze (before any diff is generated):**
- (a) P2 abstract check: Tori performs exactly two public HTTP GETs — the arXiv abstract pages
  of `1203.2926v2` and `1507.06366v1` — saved as
  `p2_2929_disposition/ABSTRACT_CHECK_1203_2926v2_1507_06366v1.md` with retrieval timestamps.
  Lana reads and rules per source: stay Route R (retire) or flip to S/H, one paragraph each.
  Marker: `LANA_P2_ABSTRACT_CHECK_RULING_20260706T0308Z`. No other fetching.
- (b) P5 payload check: Tori extracts (read-only) the full payloads of 28099/28154/28161;
  Goru diffs notes/snippets/metadata → `p5_2931_dedupe/PAYLOAD_UNIQUENESS_CHECK.md`.
  Unique content found → Route M fires automatically (user pre-authorized); else Route K plain.
  Marker: `GORU_P5_PAYLOAD_CHECK_20260706T0308Z`.

**Gate 1 — packet generation (Tori, bounded mechanical, under this direction):**
Each packet dir must contain, mirroring the executed 2929/2913/2921 conventions:
`backup/` (verbatim target rows + claim/successor context) · `EXACT_DIFF.md` (per-row
before→after) · review-only SQL: `apply_review_only.sql`, `rollback_review_only.sql`,
`pre_execution_verification.sql`, `post_execution_verification.sql`,
`rollback_verification.sql` — every file headed `-- REVIEW-ONLY — NOT FOR EXECUTION WITHOUT
PACKET PHRASE` · `MANIFEST.sha256` (all packet files) · `VALIDATION_REPORT.md` (static: exact
id-set match, drift guards vs generation-time snapshot, trigger tag + pre-count assertions,
vote-custody assertions for 28060, pin-survivor assertion for 28099) · `APPROVAL_PACKET.md`
(gates checklist; phrase local to this file only). P2 additionally embeds Lana's route table +
Gate-0 ruling; P5 records which of K/M fired and why.
Markers: `P2_PACKET_GENERATED_NOT_APPROVED_20260706T0308Z`,
`P5_PACKET_GENERATED_NOT_APPROVED_20260706T0308Z`.

**Gate 2 — independent validation:**
- Kun, per packet: manifest re-hash; review-only SQL parses (static parse only — never
  executed); drift-guard completeness vs the spec's before-state list; id-set exactness
  (14 rows / 3 rows, no extras); rollback symmetry (every apply step has an inverse).
  Deliver `KUN_PACKET_VALIDATION.md` in each packet dir.
  Markers: `KUN_P2_PACKET_VALIDATION_20260706T0308Z`, `KUN_P5_PACKET_VALIDATION_20260706T0308Z`.
- Lana, per packet: semantic review of `EXACT_DIFF.md` — audit-note wording (retirements must
  cite "parent 2929 replaced; source not adopted by any successor"), 28060 merge semantics with
  vote preservation, 2931 survivor/merge-note fidelity, no stance/role drift anywhere.
  Deliver `LANA_PACKET_SEMANTIC_REVIEW.md` in each packet dir.
  Markers: `LANA_P2_SEMANTIC_REVIEW_20260706T0308Z`, `LANA_P5_SEMANTIC_REVIEW_20260706T0308Z`.

**Gate 3 — Hwao assembly:** `PREPARED_CYCLE_RESULT.md` at the packets root: gates status table,
the two packet ids, what the user must do to execute (send each packet's phrase from its
`APPROVAL_PACKET.md`; one packet per phrase; Tori executes exactly once), and rollback note
(separate phrase). Marker: `PREPARED_CYCLE_RESULT_20260706T0308Z`.

## Blocker specs (parallel to the packet track, docs-only)

In `docs/hwao_morning_blocker_specs_20260706T0308Z/`:

1. **`P1_LEGACY_OVERCLAIMS_2298_2299_2924_SPEC.md` — Lana leads, Hwao reviews.** Per claim:
   exact current text/trust/score, attached evidence (2299: 25999 + 30631), why it violates
   modality≤certainty against 2945/2946, route options with drafted recast wording
   (recast-to-scoped / retire / re-parent; 2924: finish its `parent_replaced` display state —
   it still shows *consensus 0.8*), before-state checks, review questions.
   Marker: `P1_SPEC_DRAFTED_20260706T0308Z`.
2. **`P3_2572_PRIMACY_RECAST_SPEC.md` — Lana.** Recast wording to primacy framing (so pin
   26088 `refutes` and *challenged* −0.33 land on the disputed proposition, not the uncontested
   correlation); relation to the new `centrals_quenching_predictor` axis; wording-contract
   checks vs 2573. Marker: `P3_SPEC_DRAFTED_20260706T0308Z`.
3. **`P4_LEVEL_SCORE_GUARD_RECOMPUTE_SPEC.md` — Goru enumerates, Kun defines checker, Lana
   thresholds.** Goru: mechanical board-wide enumeration of level⇄score mismatches (read-only),
   incl. the 2546 `"0.5"` type bug as its own fix item. Spec presents both remedies —
   (a) scoped legacy recompute packet (DB, future-gated) vs (b) render-time consistency guard —
   and flags that (b) touches frontend/product code, which is OUTSIDE current locks and needs
   its own future lane/approval; no code is written now.
   Marker: `P4_SPEC_DRAFTED_20260706T0308Z`.

## Tori verification requirements (restated, binding)

DB writes 0 · SQL execution 0 (static parse only) · every generated SQL file carries the
REVIEW-ONLY header · public cockpit/status/mobile/copy/latest all remain
`NO ACTIVE EXECUTION PHRASE` · no packet phrase string on any public surface · out-of-scope
request twice from any lane → stop it, `BLOCKED_<lane>.md`.

## Cockpit wording for Tori

> Morning cycle: your five decisions are locked in. We are preparing — on paper, fully
> validated, nothing executed — the two cleanup packets (2929 leftovers; 2931 duplicate), and
> drafting the three blocker specs the debate map surfaced (legacy overclaims; 2572 rewording;
> trust badge/score consistency). The database, wiki, git, and services remain untouched. Each
> packet will wait for its own explicit approval phrase from you. Active execution phrase: NONE.

HWAO_PREPARED_PACKET_AND_SPECS_COORDINATION_20260706T0308Z

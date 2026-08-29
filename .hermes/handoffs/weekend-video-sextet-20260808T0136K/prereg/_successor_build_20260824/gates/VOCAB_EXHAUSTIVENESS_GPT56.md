# VOCAB-R1 — GPT56 adversarial exhaustiveness attack

## Verdict

**NOT CLEAR.** The §3 construction does not hold against Row B's actual conduct table. A field-constrained write makes the permission decision depend on payload information learned during the attempted transfer, so “permitted” is not established once, before the attempt, as §3 assumes. Independently, Row G permits an adaptive χ-conditioned access pattern, so the proposal's fixed-χ-blind-set safety condition is not paid under every Row-B-permitted pattern. The integrity-mismatch split also cannot be adjudicated from the evidence available when the refusal code is emitted.

The dispatched subject matched the required SHA-256 before its first read: `b7096cb4f2524640f9192fe89161fcfa569b613d9c16089e1d74452ff1a4b2a6`.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — proposal §3 lines 49–64 and §4 lines 85–87; V63 §6.1 Rows B, C2, H (lines 605, 607, 612)

**The load-bearing “permission is evaluated before the attempt” premise is false for writes whose stated surface includes a payload schema.**

Row B mediates every read and write to the sealed stores. Row C2 may write only the enumerated acceptance-evidence fields and voids on any field outside that schema. Row H may write only the pinned label schema and voids on any extra field. For either row, actor, phase, operation, destination and preconditions can all pass before transfer starts, while whether the write is *within the stated surface* cannot be known until Row B receives and decodes enough of the proposed payload to discover its fields.

A concrete countercase is a Row-H write carrying the pinned fields plus one extra field. At initiation it is a write by the authorized row, at the authorized phase, through the authorized interface, to the authorized store. During the attempted transfer, inspection reveals that the payload is outside the row's stated surface. On the proposal's temporal account it was permitted and attempted (B); on the completed permission decision it was not permitted (A). The two axes overlap, or else “permitted” is being assigned retrospectively rather than “evaluated before the attempt.” The covenant nowhere requires a separately completed, immutable payload-authorization decision before the transfer, nor does it define “attempt” to begin only after full payload validation.

This also defeats structural change 3's defense. `REFUSED-SCHEMA-NONCONFORMING` is not only a `receipt_strict()` construction issue: Rows C2 and H write non-slot, field-constrained objects through Row B. Moving slot-receipt construction to `receipt_strict()` does not classify the mediator's refusal of these writes. `REFUSED-OUTSIDE-STATED-SURFACE` can name the final authorization result, but using it does not restore the asserted pre-attempt ordering or disjointness.

**Required repair direction:** define a two-stage write protocol in which a complete canonical payload (or a non-leaking authenticated envelope sufficient to decide every surface predicate) is validated before the access attempt is deemed to start, and state how Row B logs validation failure; otherwise abandon the claim that A/B are disjoint by pre-attempt ordering.

### F2 — HIGH / REPAIR-REQUIRED — proposal §2 lines 41–45; V63 §6.1 Row G line 611 and Row B line 605

**The fixed χ-blind read-set condition fails under a Row-B-permitted access pattern.**

Row G permits committee members to view cutouts “of the allocated sample only” through the sealed interface. The allocation is χ-blind, but the row does not require a fixed complete traversal, fixed order, one view per object, or a precommitted request schedule. It therefore permits this pattern: view allocated object A; use the χ-bearing visual impression from A to choose which allocated object B to request next (or whether to request it again); B's access then fails as absent, unreadable, incomplete, or mismatched. Row B must log the refused object's identity and availability code.

The universe of eligible objects is χ-blind; the **set and sequence actually requested are not**. The refusal on B consequently publishes a χ-conditioned selection fact through the object identity on which it fires. This is exactly the dependency the proposal says would turn availability codes into a χ-derived channel. Section 2.7(3) constrains exclusion predicates; it does not constrain Row G's access schedule, and inheritance from that clause therefore does not close this pattern.

The defect is broader than the refusal label: the access-log identity itself becomes χ-conditioned under adaptive requests. A coarse availability code does not erase that dependency.

**Required repair direction:** every pre-lock Row-G object request (including order, multiplicity, retries and stopping) must be derived from a χ-blind precommitted schedule, or the non-χ-bearing access log cannot expose per-request identities. The proposal cannot claim its safety condition holds by inheriting only §2.7's exclusion-predicate rule.

### F3 — MEDIUM / REPAIR-REQUIRED — proposal §4 lines 72–74 and §5 lines 101–104; V63 §5 lines 497, 500, 537–538

**A sealed-object digest mismatch cannot be split into “ordinary storage fault” versus “tampering” at refusal emission, and V63 does not make motive the VOID discriminator.**

At the point Row B compares actual bytes with a pinned digest, the observable evidence is the same in both stories: actual digest ≠ pinned digest. That comparison does not identify bit rot, a torn write, operator tampering, malicious substitution, or any other cause. No distinguishing evidence in the proposal or conduct table is available before emitting `REFUSED-INTEGRITY-MISMATCH`.

Moreover, V63 says protocol/digest deviation is VOID at any phase and that a pinned, sealed or verified object no longer matching what verification certified is `VOID-5-DIGEST-DEVIATION`. Thus even an innocent storage fault is a digest deviation under the draft's stated partition. The defensible layering is not “refusal *or* VOID”: Row B logs the immediate refused access, while the same evidence triggers the run-level VOID consequence. If the proposal intends mutually exclusive causal readings, they are indistinguishable; if it intends event-level logging plus run-level disposition, it must say both occur and remove the false alternative.

### F4 — MEDIUM / REPAIR-REQUIRED — proposal §2 lines 32–39 and §4 lines 78–81; V63 §6.1 access-log schema line 581

**Deleting the specialized identity code does not make the generic outside-surface code non-leaking.**

The event already logs object identity. If a row's stated surface is an enumerated object set, `REFUSED-OUTSIDE-STATED-SURFACE` attached to that identity still states that the named object is outside the permitted set. It publishes the same membership bit as `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET`; only the label is less specific. The proposal's claim that the generic code covers the case “without publishing the membership answer” is therefore false.

The §2 operational test also does not exclude this leak: membership can be tested without reading the requested object's bytes as data. Lines 32–34 would admit it, while lines 38–39 say it fails because membership was tested. That is an internal mismatch between the stated test and its worked result.

## Failed attacks / points that held

- I did not break the lock/ceremony merge by the brief's stated argument. A single coarse state refusal can avoid directly naming which of two ceremony states failed. Other event fields may sometimes make the state inferable, but I found no Row-B case proving that the split is required for exhaustiveness.
- The top-level law of excluded middle for a fully defined Boolean `permitted` is tautological. The break is operational: the covenant does not establish that Boolean before every attempt, and actual write surfaces require information learned during transfer.
- Fixed-parent machine paths C2, D and E are compatible with a χ-blind object universe as written. They do not rescue the universal safety claim because Row G admits adaptive within-allocation requests.
- An integrity mismatch is an availability-side access failure at the event level. The failed attack was to force it onto authorization axis A merely from digest failure; the actual defect is the unresolved event-level refusal/run-level VOID layering and the absence of causal evidence.

## Evidence ledger and boundaries

Read in content:

- `gates/BRIEF_VOCAB_EXHAUSTIVENESS.md` (read first).
- `PROPOSAL_REFUSAL_VOCABULARY_REDERIVED.md`, only after its required hash matched.
- `PREREG_SUCCESSOR_DRAFT_V63_20260829.md` at §2.7, §5, and §6.1 including the Row B conduct table.
- Prior on-disk findings were used only to locate the superseded context; this report re-derived its countercases from the current proposal and V63 text.

Read-only checks:

- `shasum -a 256` on the subject, V63, and `ref/successor_ref_v9.py`.
- Subject: `b7096cb4f2524640f9192fe89161fcfa569b613d9c16089e1d74452ff1a4b2a6` (MATCH).
- V63: `8b224c684ea4cdf067883b4d478e3cdef083118ebf7bc9c205c6ae44979ae376`.
- Frozen v9: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` (MATCH to brief).
- `git status --short` showed a heavily pre-existing dirty/untracked tree before this report write; no cleanup or mutation was attempted.

Write boundary: only this report was written. V63, `ref/successor_ref_v9.py`, the proposal, and all other files were left read-only.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: VOCAB-R1
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §3 lines 49–64; V63 §6.1 Rows B/C2/H | Field-constrained writes require permission facts learned during transfer, so the pre-attempt A/B partition overlaps.
F2 | HIGH | REPAIR-REQUIRED | §2 lines 41–45; V63 §6.1 Row G | Row G permits adaptive χ-conditioned requests, violating the fixed χ-blind object-set condition.
F3 | MEDIUM | REPAIR-REQUIRED | §5 lines 101–104; V63 §5 digest-deviation clauses | Digest evidence cannot distinguish storage fault from tampering, and V63 makes either deviation VOID while Row B must still log refusal.
F4 | MEDIUM | REPAIR-REQUIRED | §2 lines 32–39; §4 lines 78–81 | Generic OUTSIDE-STATED-SURFACE still publishes object-set membership and contradicts the proposal's operational test.
<!-- END FINDINGS-BLOCK -->
# Vocabulary exhaustiveness adversarial round — CODEX

## Verdict

**NOT CLEAR.** The §3 construction breaks in the requested ways. Row B has no covenant-level rule making the permission decision total and durable before fallible request processing, so a timeout while Row B is verifying a required authorization artifact leaves permission undecided and the requested access incomplete: neither axis applies. Separately, the draft permits χ-adaptive access scheduling under Row D, so the proposal's own χ-blind safety price is not paid. `REFUSED-INTEGRITY-MISMATCH` also overlaps the draft's phase-Any digest-deviation VOID antecedent and cannot distinguish fault from tampering at emission time.

The dispatched subject's SHA-256 was recomputed before it was read and matched `b7096cb4f2524640f9192fe89161fcfa569b613d9c16089e1d74452ff1a4b2a6` exactly.

## Findings

### F1 — HIGH — a pre-decision verifier timeout escapes both axes

**At issue:** proposal §3 lines 49–57; draft §6.1 Row B (lines 605), Row D (608), Clause 4 (638), and the suspended derivation's required mediator-behaviour coverage (588).

The construction needs more than a binary codomain for `permitted`; it needs a total permission decision that exists before anything fallible counted as the attempt. The covenant does not impose that ordering. Row B must hard-block Row D until it verifies the authenticated C2 exact-parent stage-completion artifact. Processing a Row-D cutout request can therefore enter that required verifier and time out, deadlock, lose the verifier process, or encounter an unreadable authorization artifact before the verifier returns a verdict. The requested access has not completed, but it was neither adjudicated “not permitted” nor adjudicated “permitted.” Axis A requires the former; Axis B requires the latter. The case escapes both.

This is against the actual table, not a general claim about permission systems: Row B's Row-D precondition verification is explicitly required, while no clause says the permission result is computed and durably logged before verifier/storage work that may time out. Line 588 expressly requires the rebuild to cover mediator behaviour including timeout, yet §3's Axis-B decomposition and §4's four availability codes omit timeout. Calling permission binary does not make an unevaluated predicate true or false.

Repair requires an explicit request-state machine rather than the asserted ordering: e.g. `PENDING_AUTHORIZATION → DENIED` or `AUTHORIZED → transfer`, with a fixed terminal treatment for timeout/crash in each state and a durable log boundary. Until that exists, the two-way partition is not exhaustive.

### F2 — HIGH — Row D permits χ-adaptive access membership, so availability refusals become a χ channel

**At issue:** proposal §2 lines 41–45 and §3 lines 63–64; draft §2.7(3) lines 346–349 and §6.1 Rows C2/D (607–608).

The proposal correctly states that availability reasons are non-leaking only when the object set is fixed χ-blind, but the actual covenant does not require that for every Row-B-mediated access pattern. Row C2 is expressly constrained to “fixed parent lists.” Row D is not: its surface says it reads cutouts and writes per-object outputs, with no fixed request order, no exact request manifest, and no prohibition on choosing the next cutout after computing a prior object's χ/sign/amplitude/confidence. Section 2.7(3) constrains **exclusion predicates**; it does not constrain Row D's access scheduler.

A conforming Row-D runner can therefore read object 1, compute its χ-derived output inside the sealed store, and choose object 2 versus object 3 as its next permitted cutout read based on that output. If the chosen cutout is absent/unreadable/incomplete, the external non-χ-bearing access log records the refused object identity and availability code. That identity reveals which χ-dependent branch was taken. Nothing in Row D forbids the adaptive request, and Row B conveys any request within Row D's stated surface.

This defeats the proposal's safety condition even if all four availability labels are otherwise content-blind. Repair requires a precommitted χ-blind ordered access manifest (or equivalent total fixed schedule) for every row that may read χ-bearing objects, enforced by Row B before any χ-derived computation can influence later requests. A sign-blind exclusion rule is not a substitute for a sign-blind access schedule.

### F3 — HIGH — integrity mismatch is simultaneously a refusal and a phase-Any VOID antecedent, with no emission-time evidence separating fault from tampering

**At issue:** proposal §4 line 74 and §5 lines 101–104; draft §5 lines 537–538 and §6.3 lines 676–679.

At the instant the mediator compares bytes with a pinned digest, its evidence is only inequality. Random corruption, stale/misdirected storage, a transfer fault, and deliberate alteration can produce the same observation. The digest mismatch alone cannot establish intent or mechanism. A prior matching authenticated checkpoint plus exclusive custody can localize when or where bytes changed; signatures or access evidence may identify an actor; neither is supplied by the refusal code itself, and even those facts establish deviation more readily than intent.

The draft does not actually make attribution the VOID test. It says protocol/digest deviation is `VOID` at **any phase**. Thus a mismatch on a pinned or sealed object is already the named VOID antecedent regardless of whether the physical cause was malicious tampering or innocent bit rot. Leaving `REFUSED-INTEGRITY-MISMATCH` as an ordinary Axis-B storage refusal makes the same event both a refusal and VOID. The overlap cannot be resolved by “safe direction” at code emission, and a precedence rule would conceal rather than partition it.

Repair must define disjoint event classes from evidence available at emission. Under the current draft, the direct reading is: log the failed access, but route every pinned/sealed digest mismatch to `VOID-5-DIGEST-DEVIATION`; reserve a non-VOID transfer-integrity refusal, if wanted, for an explicitly unpinned transport check whose failure is not a protocol/pinned-digest deviation. Do not use inferred intent as the boundary.

### F4 — HIGH — deleting the identity-membership code does not delete the membership leak

**At issue:** proposal §4 lines 78–81; draft access-log schema line 581 and Row G line 611.

The proposal says `REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET` can disappear because `REFUSED-OUTSIDE-STATED-SURFACE` covers the same case “without publishing the membership answer.” The second claim is false against the actual event schema. Every access-log event carries the object identity. Row G's stated surface is “the allocated sample only.” An event containing identity X plus `REFUSED-OUTSIDE-STATED-SURFACE` for a Row-G view request publishes that X is not in the allocated sample just as surely as the deleted name did.

The two labels are extensionally redundant in that case, but renaming a membership answer as a surface answer does not stop it being a membership answer. This also shows why the proposal's operational test (“could be emitted without reading object bytes”) is insufficient: set-membership leakage needs no object-byte read. Repair requires either preventing requests whose identity-membership result may not be exported, coarsening/removing the externally visible identity for such refusals, or proving that every stated-surface membership set is itself safe to disclose. Code deletion alone does none of these.

### F5 — MEDIUM — the schema-refusal deletion relies on a `receipt_strict()` scope the draft explicitly does not have

**At issue:** proposal §4 lines 85–87; draft §6.1 Rows C/C2/D/H (606–608, 612) and §11 lines 1007–1011.

The proposal removes `REFUSED-SCHEMA-NONCONFORMING` on the assertion that V59 assigns the fact to `receipt_strict()`. The live V63 text, corrected after the V59 review, scopes `receipt_strict()` only to producers of **slot receipts whose slot appears in `SLOT_SCHEMA`**. Row C's cutout-completion receipt, C2's projections/stage artifact, Row D's per-object measurement receipts, and Row H's χ-bearing label-set receipt are non-slot artifacts; Row H separately voids on any field beyond its pinned label schema.

Therefore `receipt_strict()` does not establish that every schema-invalid sealed-store write is rejected before it becomes a Row-B access event. If Row B receives and refuses such a non-slot write while the row and operation are otherwise authorized and storage is available, the proposal has removed the only reason that directly names the refusal. If the intended rule is instead that every such attempt is VOID and never an access refusal, that partition must be stated and enforced; “receipt construction” does not make the Row-B write touch disappear.

This is a secondary structural failure rather than the primary two-axis counterexample, but it defeats the offered defense for change 3 and leaves a real class of writes without a demonstrated code path.

## Failed attacks / what held

1. Once a permission decision is durably `AUTHORIZED`, ordinary absent, unreadable, and incomplete target bytes fit Axis B; I did not find those cases escaping both axes. The break is the missing pre-decision state and its failure semantics.
2. The lock/ceremony merge does not by itself break the two-axis construction: both source reasons are authorization-state denials. The proposal's analogy between a bounded two-code split and free text is overstated, but that naming objection is not needed for this verdict.
3. A fixed χ-blind manifest would make an availability refusal's object identity independent of χ even when storage failure correlates with other metadata. The draft supplies that constraint for C2, but not for every permitted reader, especially Row D.
4. Digest inequality is mechanically observable without interpreting content, so the integrity code passes that narrow byte-read test. It fails because the draft assigns the same observable event to VOID, not because the comparison is impossible.

## Evidence ledger and custody

Read first: `gates/BRIEF_VOCAB_EXHAUSTIVENESS.md`. Then SHA-256-verified and read: `PROPOSAL_REFUSAL_VOCABULARY_REDERIVED.md`. Read in content for the assigned claims: `PREREG_SUCCESSOR_DRAFT_V63_20260829.md` §2.7, §5, §6.1 (including the full conduct table and clauses), §6.3, and the `receipt_strict()` binding in §11; `gates/V59_WHOLE_REVIEW_CODEX.md` for the scope correction that V63 carries. Searched the lane for the prior refusal-code occurrences and for fixed/canonical access-order constraints. Recomputed frozen `ref/successor_ref_v9.py` SHA-256 as `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, exact match; the file was not modified. No draft, reference, checker, proposal, or file outside this report was modified. The repository had substantial pre-existing unrelated modifications/untracked files before this report was written.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: VOCAB-R1
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §3 lines 49–57; Row B/Row D | A timeout while Row B verifies Row D's required authorization artifact leaves permission undecided and access incomplete, escaping both axes.
F2 | HIGH | REPAIR-REQUIRED | §2 lines 41–45; §6.1 Row D | Row D permits χ-adaptive cutout scheduling, so the refused object identity can export which χ-derived branch was taken.
F3 | HIGH | REPAIR-REQUIRED | §4 line 74; §5 lines 101–104 | A pinned/sealed digest mismatch is both the proposed storage refusal and the draft's phase-Any VOID antecedent, with no emission-time evidence distinguishing fault from tampering.
F4 | HIGH | REPAIR-REQUIRED | §4 lines 78–81; §6.1 Row G | OUTSIDE-STATED-SURFACE plus the logged object identity still publishes allocated-set membership, so deleting the membership-named code does not remove the leak.
F5 | MEDIUM | REPAIR-REQUIRED | §4 lines 85–87; §11 lines 1007–1011 | receipt_strict covers slot receipts only, so it does not justify removing schema refusals for non-slot sealed-store writes.
<!-- END FINDINGS-BLOCK -->
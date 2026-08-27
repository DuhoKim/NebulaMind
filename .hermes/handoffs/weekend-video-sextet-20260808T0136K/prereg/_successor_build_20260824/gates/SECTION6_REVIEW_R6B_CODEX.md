# CODEX referee report — proposed replacement §6, sixth pass R6b

## Verdict

**NOT CLEAR.** Removing the exported cutout checksum is a real narrowing, but R6b calls the channel closed without specifying the machinery that would make the remaining per-object bits, exact-parent artifact, write order, and timing non-discretionary. More seriously, refusing pre-lock reason (c) does not define a post-unblinding absence/non-finiteness rule: the locked BS-2f mask can contain objects with no usable instrument measurement, Row I and Stage C consume artifacts built from that mask, and Row P's confidence-cut consequence does not cover a missing measurement that cannot enter its join. The refused BS-2a status is honest and makes the design reviewable, but the hermetic profile, runtime attestation, independent recomputation, stage-completion verification, and adversarial fixtures remain requirements rather than a gate-ready enforcement contract. Blocking findings: 1–3.

## Numbered findings

### 1. BLOCKING — checksum removal narrows the C2 channel; it does not close it

**Row / clause / sentence at issue.** Closed-list item (v), line 24; access-log schema, line 21; Rows B–E, lines 37–41; Clause 9, line 80; Part 5 items 2–4, lines 119–121.

**Why it fails.** R6b correctly keeps cutout digests sealed. It nevertheless exports three writable predicate bits per parent across the fixed 65,060-object set. The statements that each value is “mechanically fixed” and “mechanically recomputable by a separately pinned independent verifier” do not name that verifier, its pinning slot, the exact predicate definitions, its canonical inputs, or a mandatory comparison that refuses a C2-authored bit before the projection becomes available to Row E or any external witness. A hostile C2 that can read pixels can therefore choose which legal bit is false unless a second implementation actually recomputes and compares every value.

Exact-parent closure addresses only one channel, and only by assertion. Row E requires exactly one verified projection per parent, but Row D is released earlier by a separate “stage-completion artifact.” R6b does not define that artifact's canonical body, schema, permissible fields, ordering, authenticator, or verifier. It is also not itself named in the exhaustive non-χ-bearing list: item (v) names the acceptance-evidence projection, while the default at line 26 makes every unlisted artifact χ-bearing. A gate external to the store therefore cannot lawfully inspect this artifact under the draft's own closed-list rule, yet Row B is told to “verify” it.

The omission channel is not the only remaining channel. The non-χ-bearing access log records timestamp and object identity. C2 can vary the order and timing of its permitted per-object reads/writes based on the pixels, and the resulting log is externally visible. Nothing requires canonical parent order, canonical emission timing, a single atomic projection publication, or a stage artifact with no caller-varying content. A strict import/network/model allowlist does not by itself prevent ordinary code already authorized to inspect the pixels from computing a morphology-dependent branch and expressing it through a bit, order, delay, or stage-artifact field. Clause 9 says adversarial attempts “must fail,” but does not define the failure oracle or require the real verifier to reject each projection, ordering, timing, duplication, and stage-artifact mutation.

R6b has therefore removed the checksum channel and constrained the vocabulary, but it has not proved that the remaining channel has outcome-free, non-discretionary content. It has narrowed the channel while calling it closed.

**Smallest sufficient repair.** In the replacement BS-2a design, define byte-exact schemas and canonical serialization for the per-parent projection and stage-completion artifact; identify and pin the independent verifier; define every predicate from canonical inputs; require that verifier to recompute and match every bit and exact-parent identity before one atomic publication; forbid extra fields, duplicates, omissions, caller-selected order, and observable per-object timing; and make Row B's D-release depend on that verifier's authenticated result. Either keep C2 per-object events inside the sealed boundary and export only one fixed-shape completion result, or define a canonical externally visible event sequence that carries no C2-chosen timing. Fixtures must mutate every enumerated bit, parent relation, order, delay, duplicate/omission case, and stage-artifact field and demonstrate a specified gate refusal.

### 2. BLOCKING — refusing reason (c) relocates the defect into calibration, power, and the verdict join

**Row / clause / sentence at issue.** Rows D–J and P, lines 40–46 and 52; Part 2 items 2–3, lines 93–94; Part 3 C1, line 103; residual risk R3, line 112; current V15 §2.7(2) and (4), lines 306–322; current V15 Stage C, lines 421–425.

**Why it fails.** The refusal is explicit, but the downstream handling is not. Row E excludes only on C2's cutout predicates, so an object whose instrument output is absent or non-finite remains accepted in BS-2f. Row F allocates calibration on that accepted partition. Row I then requires “the corresponding instrument outputs” for the hand-check labels, with no rule for an allocated object whose corresponding output is missing or non-finite. Row J runs Stage C on the sealed BS-2f mask and BS-8f aggregates, so the pre-unblinding power receipt describes the pre-attrition population.

Row P does not repair this. It begins by reading “the real χ vector joined to the accepted mask” and then applies a confidence threshold. An absent measurement cannot enter that join and has no confidence value to compare. A non-finite measurement is not explicitly mapped to the confidence exclusion either. The mandatory final-mask/calibration/power recomputation is triggered only “if this exclusion” — the confidence cut — removes an object. Part 2 says non-finite outputs are deferred to post-unblinding “handling,” but specifies no producer, exact attempt/receipt closure, deterministic exclusion rule, retry/failure semantics, trigger, or fail-closed behavior. Thus neither absence nor non-finiteness is guaranteed to trigger the recomputation R6b relies on.

The draft's own residual risk understates this as possible attrition that “would void the run.” No normative row or clause says that reason-(c) attrition voids the run. Under the written contract, the pipeline can instead fail to form Row I's calibration, silently inner-join away missing accepted objects at Row P, or evaluate Stage-C adequacy for a different sample from the one actually analyzed.

**Smallest sufficient repair.** If reason (c) remains deferred, define a pinned post-unblinding exact-parent join against the independently fixed attempt set; give absent and non-finite measurements explicit deterministic terminal states; forbid silent inner-join loss and discretionary retry; and require any such state, not only a low-confidence comparison, to rebuild the final mask digest and re-evaluate calibration applicability and Stage-C power before any statistic. Specify fail-closed handling when an affected object was in the hand-check allocation or makes BS-8f non-formable. Alternatively, retain a sealed pre-lock execution supervisor that mechanically establishes reason (c).

### 3. BLOCKING — the claimed enforcement mechanisms are still promises, not a gate-ready contract

**Row / clause / sentence at issue.** Rows B, C2, and D, lines 37, 39–40; Clause 2, line 61; Clause 9, line 80; Part 2 items 1 and 6, lines 92 and 97; Part 5 items 4 and 6, lines 121 and 123.

**Why it fails.** R6b improves the prose by naming the necessary categories: a hermetic worker, an allowlist, runtime attestation, a hard C2→D prerequisite, and adversarial fixtures. It does not supply the contracts by which a gate can decide pass or fail. The allowlist has no concrete profile or digest; the runtime attestation has no schema, producer, verifier, freshness binding, or link to the C2 code/input set; the stage-completion artifact and its verifier are undefined as described in Finding 1; and the fixture requirement neither enumerates the writable/missingness surfaces nor states whether “must fail” means the malicious producer must be rejected or the whole gate run must fail. No fixture oracle binds transformed cutouts to expected predicate values.

The text also admits that `verify_cutout_integrity` is only “to be pinned,” BS-2a is REFUSED / UNFILLED, Rows C2 and E cannot run, and the code-side enforcement is for “the next atomic revision.” That is an honest non-executable position, not grounds to declare §6 unreviewable. It does, however, contradict Part 5's unqualified claim that the promise-not-boundary finding is repaired. At present there is no implementation or complete design artifact against which the claimed boundary can be tested.

**Smallest sufficient repair.** Keep BS-2a REFUSED and BS-6 blocked, but change the finding disposition to unresolved until one replacement BS-2a text-and-code candidate defines the exact schemas, verifier identities, attestation chain, mediator state transition, and fixture oracles above and passes fresh gates. A future-work list is not a repair receipt.

## Checks that held / failed attacks

1. **Checksum regression attack failed.** No cutout checksum or cutout digest is permitted to leave the sealed boundary in R6b. This is a substantive narrowing relative to R5.
2. **Execution-status resurrection attack failed.** C2 no longer claims to report Row D's completion or output finiteness. Reason (c) is explicitly removed from Row E's pre-lock predicates rather than renamed. Finding 2 concerns the missing downstream rule, not a hidden pre-lock status field.
3. **Exact-parent intent is present.** Row E requires exactly one verified projection per fixed parent, Row D names a C2 completion prerequisite, and Row B is instructed to refuse D before it. Finding 1 concerns the absent schema/verifier and the channels not covered by cardinality.
4. **Universal-ban regression attack failed.** Clause 1 is substantively identical to R5 after whitespace normalization and has a complete body. It binds every person and process and governs access, not merely disclosure.
5. **Committee-path regression attack failed.** Rows G→H→I remain present; Clause 5 is substantively identical to R5 after whitespace normalization and says a conforming in-row act does not void the run. The committee can therefore complete its authorized path without voiding the run.
6. **Lock-chain regression attack failed.** Clause 3 is substantively identical to R5 after whitespace normalization and preserves BS-5f → BS-L → unblinding → BS-7f → BS-V, with verification failure refusing unblinding and the verdict path.
7. **Normative-body restoration attack failed.** Clauses 1, 3, 4, 5, 6, 7, and 8 have actual bodies. Mechanical whitespace-normalized comparison found Clauses 1 and 3–7 identical to R5; Clause 8's R5 body is preserved before the new Clause 9. The disclosed §6.2/§6.3 placeholders remain an assembly gap and did not conceal the protected properties above.
8. **Refused-slot candor held.** Row C2 and Clause 2 mark BS-2a REFUSED / UNFILLED, Part 2 blocks BS-6, and residual risk R1 says the pipeline cannot reach the first image byte. The draft is reviewable as a proposed blocked design; it is not executable.

## Testimony and limits

I did not inspect any image, cutout, χ value, sealed-store payload, predecessor-archive content, key, credential, access log, runtime attestation, or `/Users/duhokim/NebulaMindData/`. I did not verify historical archive access, current seal state, raw-store exclusivity, committee isolation or memory, or the existence/behavior of any future C2 verifier, independent predicate verifier, mediator state machine, hermetic worker, attestation verifier, receipt schema, or fixture implementation. Statements about how those future mechanisms could work are repair requirements and design analysis, not observations of running code.

## Evidence ledger

- Recomputed `SECTION6_DRAFT_AGY_R6B.md` sha256 as `f9743e836ff791906c94726991a7db43f04ef1a82baaaf4b9e0bea60c2c3d566`, matching the referee brief.
- Read `BRIEF_SECTION6_REVIEW_R6B.md`, `BRIEF_DRAFT_SECTION6_R6B.md`, `SECTION6_DRAFT_AGY_R6B.md`, `SECTION6_DRAFT_AGY_R6.md`, `SECTION6_DRAFT_AGY_R5.md`, and both R5 referee reports.
- Inspected current `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` §2.7 and Stage-C text. Current §2.7 reason (c) is instrument absence/non-finiteness; its evidence rule uses an instrument execution receipt and independently fixed attempt/receipt join. Current Stage C runs on the sealed BS-2f accepted-position mask.
- Mechanically extracted and whitespace-normalized R5/R6b Clauses 1–8. Clauses 1 and 3–7 matched; R6b preserved Clause 8 and appended Clause 9; Clause 2 is intentionally replaced by the refusal text.
- Ran no fetch, image read, χ computation, sealed-store operation, preregistration edit, data-directory access, credential/key access, or code execution against the scientific pipeline. The only file written is this referee report.

**NOT CLEAR**
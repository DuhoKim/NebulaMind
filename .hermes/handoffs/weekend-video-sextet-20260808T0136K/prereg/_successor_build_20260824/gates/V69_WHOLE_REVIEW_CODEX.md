# V69 whole-document adversarial review — CODEX

**VERDICT: NOT CLEAR.** The subject digest matched the brief exactly before the draft was read. V69 repairs several V68 defects, but its new lifecycle still contains the deleted `TRANSFER` machine, moves rendered delivery onto an unreceipted custody surface, and leaves a post-verifier opening window. The enumeration dispositions are not representable or semantically bound by their exact schema; the BS-3g verifier does not bind the claimed baseline; and the proposed `gamma_bound` is not a bound under the estimator failures the brief requires testing.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — the supposedly deleted `TRANSFER` lifecycle remains the document's declared state machine

Section §6.1 line 618 still says every request occupies exactly one state in a machine ending `AUTHORISED` or `REFUSED` → `TRANSFER` → `COMPLETED` or `FAILED`. Lines 634–635 then say `TRANSFER` “is deleted,” that no post-commit state remains, and restate a different machine whose terminal act is the refusal-or-touch commit.

This is not historical quotation: line 618 is the live, universal state declaration immediately introducing the guarantee. A conforming implementer can follow it and recreate V68's post-event terminal-state change, or follow lines 634–635 and omit those states. The claim that every request has exactly one state and one terminal treatment is therefore dual-valued in the repair's own normative paragraph.

### F2 — HIGH / REPAIR-REQUIRED — rendered Row-G views are delivery, but delivery is unlogged and its committed buffer is an ungoverned χ-bearing holding surface

Lines 625–627 explicitly put requester delivery outside the custody claim: the event records only bytes leaving the sealed store into Row B's committed buffer and “never asserts the requester received anything”; re-sending from that buffer produces no new event. Row G at line 673, however, renders χ-bearing cutouts to a human and voids on “any unlogged view.” The access-schedule rule at line 646 additionally permits unrestricted re-viewing and repeated display of the current object without treating it as a new request.

A first render, re-render after a display failure, or later re-view from the committed buffer is requester delivery. By the draft's own N1 rule, no event says that view occurred; by Row G's void clause, it is an unlogged view. Calling every replay “the same conveyance” does not make the human view appear in an event whose asserted fact is only the store-to-buffer effect.

The buffer also creates the custody surface the draft denies creating. A cutout remains χ-bearing wherever it sits (§6.1 lines 584, 656), while lines 658 and 641 enumerate three sealed stores and say no second custody surface is created. A committed buffer must outlive the store transaction and may outlive failed delivery so it can be resent, but no row specifies its retention, deletion, access, checkpoint, or phase transition. N1 may disclaim receipt by the requester; it does not authorize a durable fourth holder of χ-bearing bytes.

### F3 — HIGH / REPAIR-REQUIRED — the second enumeration pass has a check/use gap during opening and unsealing

Lines 603–606 correctly observe that a checkpoint has an “after,” but the repair creates another one. The verifier's second pass reads the chain “as it stands at that moment” at opening. Row O then opens and decrypts the stores at P7 (line 681), through Row B because Row B is the only path to the stores (line 667). Those touches can themselves refuse with `REFUSED-UNCLASSIFIED` after the fresh pass—for example, an unclassified mediator/unsealing failure on the first decrypting read.

No third enumeration-verifier consultation is required at the unblinding receipt or final post-unblinding checkpoint. The newly appended refusal therefore has no next gate before the operation it was supposed to block: the opening check has passed and unsealing has begun. Clause 4's final checkpoint records the later chain but does not enumerate it or make unblinding conditional on a new pass. The exact post-check append attack that defeated the single-checkpoint version survives one boundary later.

### F4 — HIGH / REPAIR-REQUIRED — neither enumeration disposition is bound by the exact entry schema

Line 601 requires a `NAMED-AS-DEFECT` entry to carry “the digest of the re-derived vocabulary revision that names the class.” The exact entry schema at line 607 has only `chain_position`, `event_digest`, `class_key`, `disposition`, `explanation_ref`, and signature. It has no re-derivation-digest field. `explanation_ref` is defined specifically as the identifier of a signed human explanation, so silently overloading it as a vocabulary digest would contradict the field definition and still would not say which canonical vocabulary bytes or class assertion are authenticated.

`EXPLAINED` is also only required to resolve to a signed artifact. Neither line 601, the exact schema, nor §11 lines 1302–1309 requires that artifact to bind the joined `event_digest`, `class_key`, emission facts, or even the same refusal. A signed explanation for a different event—or a content-free signed artifact—resolves and is not dangling. Thus one disposition cannot carry its mandatory object and the other can point at the wrong object while satisfying the stated verifier.

The incomplete V68 repair also remains visible at line 599: it says every entry names row, operation **and lifecycle state**, but V69 deliberately coarsens `class_key` to `(row, operation)` and the exact entry has no lifecycle-state field. The declared entry contract is internally inconsistent even before implementation.

### F5 — HIGH / REPAIR-REQUIRED — BS-3g can report `HELD` against a producer-chosen baseline

The manifest constraints at lines 1171–1181 require both endpoints, at least three distinct values, and bounded adjacent spacing; they do not require `γ = 0`. Line 1210 defines `baseline_verdict` as the unperturbed verdict, but the independent-verifier checklist at lines 1261–1284 never recomputes it from a named artifact, binds it to a digest, or requires a zero-gradient evaluation. It regenerates the draw matrix and checks only whether every cell equals the receipt's supplied `baseline_verdict`.

A conforming producer can use a manifest without zero, truthfully expose the regenerated matrix, and choose `baseline_verdict` to equal the common matrix token. The verifier then reports `HELD` even if an independently computed unperturbed verdict differs. Alternatively, the producer can call any favourable token the baseline because no pinned baseline object is named. The general sentence “must not accept the producer's own report of any quantity it can recompute” supplies no missing input or algorithm and therefore cannot perform the absent recomputation. Endpoint coverage binds the grid to its interval; it does not bind the comparison point that defines invariance.

### F6 — MEDIUM / REPAIR-REQUIRED — `|γ̂| + k_gamma·σ_gamma` is not a bound without a validity/coverage contract

Lines 1191–1197 call `gamma_bound = |gamma_hat| + k_gamma·sigma_gamma` a recomputed bound and present the frozen multiplier as the remaining choice. That formula bounds the true gradient only under an unstated error model: `γ̂` must have controlled bias and `σ_gamma` must upper-bound its uncertainty at coverage corresponding to `k_gamma`. The referenced gain design explicitly limits the estimator to a first-order three-point slope and states nonlinear positional structure is unbounded (`gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` lines 224–230).

A concrete admissible failure shape is `γ_true = 0.10`, `γ̂ = 0.01`, `σ_gamma = 0.005`, `k_gamma = 3`; the specified formula gives 0.025 and excludes the true gradient. Increasing or freezing `k_gamma` does not repair underestimated σ or bias toward zero unless the draft separately bounds those errors. This is therefore a formula/validity-contract defect, not merely the currently unset value. The receipt can certify exact recomputation of a number while the number fails to bound the threat it names.

### F7 — LOW / REPAIR-REQUIRED — the authoritative raise-site ledger contradicts itself about `local_pass`

`ref/RAISE_SITE_CLASSIFICATION.md` line 9 says “the three `local_pass` sites ... are CALLER,” then in the same paragraph says L986 is `PLANNING-INTERNAL`; its table lines 80–82 also classifies only L963/L973 as CALLER and L986 as PLANNING-INTERNAL. The table and totals are coherent, and V69 §5 adopts the table's reading, but the referenced authoritative artifact still carries both classifications in its live boundary statement. This is exactly the hand-copied-source drift the draft says the generated ledger is meant to eliminate.

## Failed attacks and verified holdings

- Subject SHA-256 held exactly: `d52844620fbda2e561f8904d5cbffc62e88a5e57a03c6024edd59cc0671e5f88` before reading and again during verification.
- The pinned reference held exactly: `ref/successor_ref_v9.py` recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/refusal_vocabulary_check.py` held its cited digest `9586e207f20141fde3d0f87f86d23cd2c84913934c7493161cfed0efb759d2e3`. Its live check returned 0 problems and its self-test returned 17 controls, 0 failures. F3/F4 are semantic and temporal failures the phrase-level R08/R09 controls do not test.
- The eleven formatted refusal codes matched the checker's exact set. I did not re-find the parked object-membership leak.
- `prereg_counts.py` reproduced 16 class P / 8 class E. `prereg_trace.py` reproduced 68 transitions / 0 problems. `prereg_lint.py` exited 0 with 97 advisory findings and 0 blocking findings. I did not report the principal-ruled legacy citations.
- `void_registry.py` reproduced 54 antecedents; its self-test returned 6 controls / 0 failures. I did not re-derive the parked VOID/numerical partition.
- AST recount reproduced 112 raises: 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, and 1 bare re-raise. V69 correctly reclassifies `_plan` lines 1331/1341 as PLANNING-INTERNAL rather than run outcomes.
- No site in `RAISE_SITE_CLASSIFICATION.md` is assigned `UNREACHABLE-BY-CONSTRUCTION`; the withdrawal held.
- The V69 BS-3g text now derives `gamma_bound` from `gamma_hat`, `sigma_gamma`, and a frozen `k_gamma`, closing V68's self-declared-endpoint defect. F6 attacks whether that derivation is a scientific bound, not whether it is now externally recomputed.
- `FAILED` and `NOT-EVALUATED` do not discharge BS-6, and the V69 total-outcome rule closes V68's conceal-a-flip route. F5 is a different comparison-baseline attack.
- The currently stated BS-3g emission blockers remain explicit: `n_draws`, `draw_master_seed`, `Δγ`, and `k_gamma` are unset and the generator set is empty. I found no current receipt-emission path through them.
- V69 correctly narrows `HELD` to the evaluated grid and does not call finite-grid survival proof of continuous invariance.
- I did not re-derive the parked availability-code object identity, durable pre-verdict residue, strata/producer decision, BS-3g lifecycle cycle, signature exemption, or other principal-held items.

## Evidence ledger and scope

Read in content: `gates/BRIEF_V69_REVIEW.md` first; all 1,318 lines of the exact-hash V69 draft; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; relevant regions of `ref/successor_ref_v9.py`; `tools/refusal_vocabulary_check.py`; `tools/prereg_counts.py`; `tools/prereg_trace.py`; `tools/prereg_lint.py`; `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`; and V68's CODEX report.

Executed read-only checks: subject/reference/checker SHA-256; refusal-vocabulary live check and self-test; prereg counts, trace and lint; VOID-registry live check and self-test; AST raise recount; repository searches for `gates/enumeration_verifier.py`; direct inspection of the lifecycle, enumeration-entry, manifest and verifier contracts; and a numerical counterexample to the proposed γ bound. I did not modify the draft, reference code, tools, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V69
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 618, 634–635 | The live state declaration still routes every request through the `TRANSFER` state that the repair later says is deleted.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 625–627, 641, 646, 658, Row G line 673 | Row-G rendering is delivery that the event never records, so permitted re-views are unlogged views and the durable committed buffer becomes an ungoverned χ-bearing holding surface.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 603–607, Row B line 667, Row O line 681, Clause 4 line 700 | A catch-all refusal appended during opening/unsealing occurs after the second verifier pass, with no further enumeration gate before unblinding proceeds.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 599–601, 607; §11 lines 1302–1309 | The exact enumeration-entry schema cannot carry the required re-derivation digest, does not bind explanations to their emission, and still claims a lifecycle-state field it lacks.
F5 | HIGH | REPAIR-REQUIRED | §11 lines 1171–1181, 1210, 1261–1284 | The verifier neither requires a zero-gradient point nor recomputes/binds `baseline_verdict`, allowing `HELD` against a producer-chosen baseline.
F6 | MEDIUM | REPAIR-REQUIRED | §11 lines 1191–1197; GAIN_GRADIENT_CONTROL_DESIGN lines 224–230 | `|γ̂| + k_gamma·σ_gamma` is not a bound under bias or underestimated σ, and no coverage/model-validity contract makes it one.
F7 | LOW | REPAIR-REQUIRED | RAISE_SITE_CLASSIFICATION.md lines 9, 80–82 | The authoritative ledger says all three `local_pass` sites are CALLER while simultaneously classifying L986 as PLANNING-INTERNAL.
<!-- END FINDINGS-BLOCK -->
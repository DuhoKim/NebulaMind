# V69 whole-document adversarial review — GPT56

**VERDICT: NOT CLEAR.** The subject digest matches, the mechanical inventories reproduce, and several V68 repairs hold. The live lifecycle nevertheless still contains the `TRANSFER → COMPLETED/FAILED` state sequence that V69 says it deleted. The delivery carve-out also collides with Row G's per-view logging requirement. The new disposition bindings are not representable by the exact enumeration-entry schema, the second verifier consultation has no authenticated home for entries created after the already-signed lock checkpoint, and the coarsened recurrence key merges unlike defects into a class the vocabulary cannot meaningfully name. Finally, `|gamma_hat| + k_gamma sigma_gamma` is only a sampling-error bound under an unstated calibrated linear-model assumption; the referenced estimator expressly leaves curvature and model bias unbounded.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — `TRANSFER` is still a live lifecycle state despite being declared deleted

Section §6.1 line 618 still normatively says every request follows `AUTHORISED` or `REFUSED` → `TRANSFER` → `COMPLETED` or `FAILED`. Lines 634–635 and 639 then say the `TRANSFER` state and its death rule are deleted, and replace that machine with one commit followed, for reads, only by out-of-claim delivery.

This is not historical quotation: line 618 is the opening definition under “The states, and every request is in exactly one.” A conforming implementer can therefore build the old three-terminal-stage machine or the new commit-only machine from the same current bytes. The V68 contradiction was not dissolved; one side of it remained as the lifecycle's first normative state enumeration. Delete or supersede that live sentence explicitly.

### F2 — HIGH / REPAIR-REQUIRED — the delivery carve-out makes Row G's “any unlogged view” rule unsatisfiable or false

Lines 625–627 make rendering to a human requester a post-commit delivery outside the custody claim. Re-sending/re-rendering from the committed buffer is the same conveyance and “never a second event.” Line 646 goes further: re-viewing the current object is unrestricted and is not a new request. But Row G's normative void column at line 673 says **any unlogged view** voids the run.

Counterexample: Row G requests one allocated cutout, receives the committed-buffer render under one store-touch event, then re-renders it after zooming or dwelling. Under lines 627 and 646 there is no second request, touch, or event. Under Row G there has been a second view with no event recording that view. If the original touch event is deemed to log every future rendering, the log does not record the number or occurrence of views and “any unlogged view” is false. If each render is a logged view, delivery is no longer outside the event surface and the “never a second event” rule is false. V69 must define whether the logged unit is store extraction, delivery session, or render, and make Row G's void condition use that same unit.

### F3 — HIGH / REPAIR-REQUIRED — the exact enumeration-entry schema cannot carry the binding V69 now requires

Line 601 says a `NAMED-AS-DEFECT` entry **must carry the digest of the re-derived vocabulary revision**. Line 607 then defines the authenticated entry's exact fields: `chain_position`, `event_digest`, `class_key`, `disposition`, `explanation_ref`, and enumerator signature. There is no re-derivation-digest field. `explanation_ref` is explicitly defined as the identifier of a signed human explanation, not as the vocabulary-revision digest. Section §11 lines 1302–1309 repeats that the future verifier resolves every `NAMED-AS-DEFECT` re-derivation digest without adding a field from which it can obtain one.

The `EXPLAINED` branch is also relevance-unbound. Resolving `explanation_ref` to a signed artifact proves existence and signature, but neither the entry schema nor the stated explanation-artifact requirement makes that artifact bind `chain_position`, `event_digest`, or `class_key`. A signed explanation of a different emission therefore satisfies the literal resolution check.

A disposition claim needs representable evidence: add a typed re-derivation digest for `NAMED-AS-DEFECT`, and require the signed explanation body for `EXPLAINED` to bind the joined event and computed key. The exact-field schema and verifier must reject cross-emission substitution.

### F4 — HIGH / REPAIR-REQUIRED — post-BS-L enumeration entries have no authenticated checkpoint surface

Lines 603–607 correctly require a fresh verifier pass at opening for catch-all events appended after BS-L. But line 607 says enumeration entries live in the **lock-checkpoint materials**, while §6.1 clause 3(b), line 695, makes the pre-unblinding lock checkpoint part of BS-L's canonical signed body.

Construct the assigned corner: BS-L is issued and signed; Row B then appends a `REFUSED-UNCLASSIFIED` event before opening. Its new enumeration entry cannot be added to the already-digested lock-checkpoint materials without changing the bytes BS-L signed. Leaving it outside those materials violates the exact entry-location rule and gives the opening verifier no named authenticated input. Re-signing BS-L after each post-lock refusal is not specified and would reopen the lock artifact rather than perform a fresh consultation.

The second consultation therefore has a predicate but no receiptable post-BS-L entry surface. V69 needs a separately authenticated opening-time enumeration supplement, with a digest chain from the signed BS-L checkpoint to the fresh chain and entries, or must prohibit the post-BS-L request window altogether.

### F5 — MEDIUM / REPAIR-REQUIRED — `(row, operation)` merges distinct defects into a class that cannot identify what must be named

Line 601 intentionally coarsens recurrence to `(table row, operation)`. This prevents relabelling evasion, but it also merges unlike causes. Example within one run: Row D/read first reaches `REFUSED-UNCLASSIFIED` because its precondition verifier times out; a later Row D/read reaches it because the mediator loses its lease or its authorization evaluator deadlocks. The two emissions have the same key and are normatively the same class, even though neither cause recurs.

The first may be `EXPLAINED`; the second is then forced to `NAMED-AS-DEFECT`, and the vocabulary must be re-derived to name “the class.” But the class contains only Row D + read and carries no fact identifying either defect. Naming the broad key produces a routine `REFUSED-ROW-D-READ`-shaped code rather than naming either missed reason; naming one cause fails to name the other while still claiming the key is discharged. “Fires sooner” is fail-closed, but it does not make the maintenance instruction well-defined.

The key needs an authenticated, non-object-bearing cause discriminator derived by the mediator (or the rule must expressly accept broad row/operation classes and define what a vocabulary code naming such a union means).

### F6 — MEDIUM / REPAIR-REQUIRED — `gamma_bound` is not a bound under the referenced estimator's admitted model misspecification

Section §11 lines 1191–1197 defines `gamma_bound = |gamma_hat| + k_gamma·sigma_gamma` and treats the frozen multiplier as giving the bound an origin outside the receipt. That formula only expands sampling uncertainty around `gamma_hat`; it does not cover estimator bias or a miscalibrated `sigma_gamma`.

Concrete allowed case: the true positional response is curved across `cos(theta)` so its three tertile averages have equal fitted slope, giving `gamma_hat = 0` and arbitrarily small `sigma_gamma`, while the response has a large interior gradient that changes accepted signs. For every finite `k_gamma`, the formula tends to zero although the unmodelled gradient is nonzero. This is not hypothetical scope invented by the referee: `ref/gain_gradient_estimator.py` lines 33–38 says it estimates a first-order gradient from three bins, does not address curvature, and makes no broader bound; `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` lines 224–230 likewise states “Three positional points support a slope and no curvature” and “Non-linear positional structure ... is unbounded.” Underestimated covariance or bias toward zero has the same failure shape.

Thus the formula is valid only as a linear-model statistical bound under calibrated covariance, not as the allowed-gradient bound the manifest spans. Freezing `k_gamma` cannot repair structural bias. The preregistration must either state and gate the linear/unbiased/calibrated assumptions and narrow the claim, or include a separately frozen model-bias/curvature term or control.

## Failed attacks / checks that held

- Subject identity held before reading: sha256 `d52844620fbda2e561f8904d5cbffc62e88a5e57a03c6024edd59cc0671e5f88`.
- The §0 pin held: `ref/successor_ref_v9.py` sha256 is `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- Independent AST recount held: 112 raises — 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, and 1 bare re-raise.
- The current raise table arithmetic held at 25 CALLER, 60 INTEGRITY, 20 NUMERICAL, 3 PLANNING-INTERNAL, 1 TYPED-OUTCOME, and 3 WRAPPER. The two `_plan` sites at source lines 1331/1341 are now `PLANNING-INTERNAL`; no current site is marked `UNREACHABLE-BY-CONSTRUCTION`. The raise ledger's prose at line 9 still initially calls all three `local_pass` sites CALLER before correcting L986 in the same paragraph, but its table and totals are unambiguous, so I treat that as an editorial contradiction rather than a numbered finding.
- `tools/refusal_vocabulary_check.py` held the draft's quoted sha256 `9586e207f20141fde3d0f87f86d23cd2c84913934c7493161cfed0efb759d2e3`; its live check returned 0 problems and its self-test returned 17 controls / 0 failures. Findings F3–F5 attack semantics the tool expressly says it does not verify.
- Mechanical checks held: counts 16 class P / 8 class E with prose match; trace 68 transitions / 0 problems; lint exit 0 with 97 advisory / 0 blocking findings; VOID registry 54 antecedents and self-test 6 controls / 0 failures.
- V69 honestly states that `gates/enumeration_verifier.py` is required and does not exist; repository-wide filename search confirms it is absent. I therefore did not re-report absence itself as a defect. The new §11 item exists as a TODO, as the brief claims.
- The V68 fixes for the two `_plan` dispositions, artifact-only Row-F recomputation claim, derived `gamma_bound` formula, and total `HELD`/`FAILED` classification are present in the bytes. F6 attacks the formula's scientific scope, not whether V69 inserted it.
- The BS-3g slot remains blocked by unset `k_gamma`, unset `delta_gamma`, unset `n_draws`, unset `draw_master_seed`, and the empty generator set; I found no current emission path through those blockers.
- I did not re-derive parked findings named by the brief (including the VOID/numerical partition, availability-code object leak, durable pre-verdict state, strata/producer question, BS-3g lifecycle cycle, signature exemption, and `require_authorization`).

## Evidence ledger and write scope

Content read: `gates/BRIEF_V69_REVIEW.md`; all 1,318 lines of the subject; `ref/RAISE_SITE_CLASSIFICATION.md`; relevant source regions of `ref/successor_ref_v9.py`; full `ref/gain_counterfactual_path.py`; full `ref/gain_gradient_estimator.py`; `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`; full `tools/refusal_vocabulary_check.py`; the mechanical checker sources; and both V68 whole-document reports as predecessor claims to attack, not as ground truth.

Read-only execution: sha256 checks; AST raise recount; V68→V69 byte diff; refusal-vocabulary live check and self-test; prereg counts; lint; trace check; VOID-registry live check and self-test; repository-wide searches for the asserted verifier and tool files; and targeted semantic searches over lifecycle, enumeration, disposition, delivery, and BS-3g clauses.

I did not modify the draft, reference code, tools, gates, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V69
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 618, 634–635, 639 | The live state definition still routes requests through TRANSFER → COMPLETED/FAILED while the repair says TRANSFER and its death rule are deleted.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 625–627, 646, Row G line 673 | Delivery retries and re-views produce no new event, but Row G voids any unlogged view, so the render boundary cannot satisfy both rules.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 601, 607; §11 lines 1302–1309 | The exact entry schema has no re-derivation-digest field, and signed explanations need not bind the joined emission, so both dispositions remain substitutable.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 603–607, clause 3(b) line 695 | A post-BS-L catch-all needs a fresh entry, but entries live in lock-checkpoint materials already digested and signed by BS-L, leaving the opening pass no authenticated mutable surface.
F5 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 600–601 | The coarsened (row, operation) key merges unlike defects, so a second distinct failure forces re-derivation without identifying which missed reason the vocabulary must name.
F6 | MEDIUM | REPAIR-REQUIRED | §11 lines 1191–1197; gain_gradient_estimator.py lines 33–38 | |gamma_hat| + k·sigma is only a sampling-error bound; estimator bias, underestimated sigma, and expressly unbounded curvature can make it arbitrarily smaller than the true gradient.
<!-- END FINDINGS-BLOCK -->
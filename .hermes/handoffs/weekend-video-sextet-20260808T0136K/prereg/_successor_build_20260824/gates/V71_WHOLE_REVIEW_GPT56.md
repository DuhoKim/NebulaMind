# GPT56 — V71 whole-document adversarial review

**VERDICT: NOT CLEAR.** The required subject SHA-256 matched before I read the draft. V71 repairs the literal V70 refusal-event contradiction in the companion spec, but the draft's own normative guarantee block still carries the unrepaired wording. The repaired G2 also leaves refusal-reason truth unconstrained. The new view-session boundary can preserve one commit indefinitely across repeated human views, and the newly admitted signed explanation artifacts are both a covert χ channel and semantically unable to prove that they explain the joined emission. The BS-3g verifier inventory fails to recompute its new nineteenth code digest, and the lifecycle's supposedly complete touch-kind partition omits destructive/metadata mutations.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — The draft did not inherit the spec's G2/G3 repair

The draft declares that it is derived from `LIFECYCLE_GUARANTEE_SPEC.md`, that a conflict is a draft defect, and that V71 restated G2/G3 so refusals are covered (§6.1 line 621). The companion spec does contain the repair: G2 expressly makes a refusal event true of refusal plus no effect, and G3 says every event is exactly a touch's or a refusal's (spec lines 31–32).

But the draft's immediately following normative block, introduced as “What it must guarantee,” still says only:

- G2: “Every committed event's outcome field is true **of the store effect it records**” (§6.1 line 624); and
- G3: “ONE EVENT PER TOUCH” (§6.1 line 625).

A refusal commit has no store effect (§6.1 line 630). The draft's G2 therefore still supplies no refusal truth condition, and its G3 still does not exclude an event that belongs to neither a touch nor a refusal. The summary of the repair and the normative guarantee list disagree in the exact revision whose stated purpose was to make the spec the one home. This is the same incomplete-retraction shape, now between the spec and its derived draft.

### F2 — HIGH — REPAIR-REQUIRED — G2 permits a false refusal reason that bypasses catch-all enumeration

Even the repaired spec guarantees only that “a request was refused and NO store effect occurred” (spec G2, line 31). It does not require the refusal **reason code** to be true of why the request was refused. Yet the reason code is load-bearing: only `REFUSED-UNCLASSIFIED` triggers enumeration, recurrence, and the blocking gates (draft §6.1 lines 589–607).

Counterexample: a verifier times out. Row B really refuses the request and produces no store effect, but records `REFUSED-PRECONDITION-UNVERIFIED` instead of the required `REFUSED-UNCLASSIFIED`. G2 is satisfied as written (the request was refused and no effect occurred), G3 is satisfied (one refusal event), and no catch-all enumeration fires. A routine undecided-permission defect can therefore be hidden under any specific code while every lifecycle invariant and every enumeration clause passes. G2 must bind the truth of the complete event outcome, including the selected refusal-reason token, to authenticated decision evidence—not merely the binary refusal/no-effect fact.

### F3 — HIGH — REPAIR-REQUIRED — The view-session boundary can keep one commit alive indefinitely

The new definition says one VIEW begins when a committed render is displayed and ends only when the traversal position advances or the interface clears; dwell and magnification are the same view (spec §5 lines 89–96; draft §6.1 line 649). Neither end condition is mandatory or time-bounded.

Concrete conforming execution: render object X once under event E; never advance the position and never clear the interface; leave the frame displayed overnight; let the checker return repeatedly, zoom/crop/pan it, or let another permitted committee member inspect it. Every later inspection remains the same “display session” and therefore produces no new event, even though any ordinary reader would call these separate views. The definition has not closed the V70 cached-frame fork; it has renamed an unbounded lifetime as one view.

The buffer rule does not repair this. The spec requires the committed conveyance buffer to be destroyed on delivery completion/request end (spec lines 97–101), while the displayed/cached framebuffer must persist for the open session and its magnifications. That χ-bearing render surface has no lifetime, session timeout, member binding, or destruction invariant. A mandatory, externally checkable session boundary is required; “position advanced or interface cleared” is an operator-controlled escape hatch.

### F4 — HIGH — REPAIR-REQUIRED — Signed explanations are a covert χ channel while obeying the sentence constraint

V71 adds enumeration entries, continuation segments, and signed explanation artifacts to the exhaustive non-χ list solely under a semantic sentence constraint: explanations may describe the request and authorisation state and never the object (§6.1 line 656). It gives explanation artifacts no canonical body, closed vocabulary, bounded encoding, deterministic serialization, fixed length, deterministic signature, or mechanically recomputable values.

A compliant one-bit leak is trivial. For an emission joined to a logged object identity, choose between the synonymous allowed sentences “Authorisation was not established.” and “The authorisation state was not established.” according to that object's χ sign. Both describe only authorisation state and never describe the object; both pass the stated constraint; the wording choice leaks one χ bit. Whitespace, punctuation, identifier form, file length, ordering, or signature nonce provide larger channels. Authentication preserves these bits rather than removing them.

This defeats the closed non-χ classification by construction. The explanation must be a canonical authenticated schema over closed/mechanically fixed fields, not signed free prose governed by a semantic undertaking.

### F5 — HIGH — REPAIR-REQUIRED — A joined explanation can explain a different defect and still discharge the emission

The enumeration verifier checks that an `EXPLAINED` artifact is signed, resolves, and names the exact `(chain_position, event_digest)` (§6.1 line 610; §11 lines 1352–1362). Those checks bind the artifact to an emission, but do not establish that its explanation is true of that emission.

Counterexample: the actual catch-all cause is a schema-conformance decision that died mid-check. The signed artifact names the correct position and digest but says, “The request was refused because phase P4 had not been reached.” The access-log event contains only the catch-all token, row, operation, object identity, and chain fields; it does not retain authenticated cause evidence from which a verifier can distinguish the real defect from the invented phase explanation. The reference resolves, the signature verifies, the sentence concerns request/authorisation state, and the one-off key is discharged as `EXPLAINED`.

Thus `explanation_ref` can point to an artifact that structurally names this emission while semantically explaining another. Require authenticated decision evidence and a machine-checkable relationship between that evidence and the explanation/disposition; a signature plus a join proves authorship and attachment, not truth.

### F6 — MEDIUM — REPAIR-REQUIRED — The verifier contract was not updated to recompute the nineteenth code digest

V71 adds `counterfactual_path_sha256` as the nineteenth BS-3g field and says it “pins the module” (§11 lines 1143–1149, 1251–1259). But the independent-verifier algorithm later still says only that clause (a) “recomputes all three module digests from the files on disk” (§11 lines 1311–1318). The pre-existing three are `kernel_sha256`, `estimator_sha256`, and `verifier_sha256`; the newly added counterfactual-path digest is a fourth and is not named in clauses (a0)–(g).

A receipt can therefore carry an arbitrary 64-hex `counterfactual_path_sha256` while every explicitly enumerated verifier clause passes. Replaying cells may authenticate the outputs, but it does not make the receipt's claimed path digest true, and it does not satisfy the stated purpose of binding the verdict-producing computation. Add an explicit recomputation/equality check for `counterfactual_path_sha256` and bind the imported production dependency/environment as part of the same hermetic replay contract.

### F7 — MEDIUM — REPAIR-REQUIRED — The closed touch-kind enumeration omits destructive and metadata mutations

The spec defines TOUCH as bytes leaving or landing in a sealed store and declares exactly two leaving kinds (CONVEYANCE, RENDER) and one landing kind (WRITE) (spec §0 lines 12–19). G1–G5 and the five crash windows are then claimed as the complete lifecycle partition (spec lines 26–62).

A mediated delete/truncate of a sealed object, rename that changes its bound identity, permission/ACL change, or key/rekey operation is neither conveyance, render, nor bytes landing as a write. For the simplest case, deleting a sealed χ-bearing file changes custody and can destroy the object without delivering its bytes or landing replacement bytes. Under the closed definition it is not a TOUCH, so G1 does not require an event, no touch/refusal bijection applies, and it occupies no crash-window cell. Calling the act forbidden/VOID elsewhere does not make the lifecycle's claimed G/N partition complete; the spec's own brief asks for every failure to land in that table.

Either expand TOUCH/store effect to all custody-relevant state mutations and add their commit semantics, or state them as an explicit non-guarantee. The present “every touch kind” claim is vacuous over operations the definition forgot.

## Failed attacks / checks that held

- Subject identity held before reading: SHA-256 `7a8e7151e4063e5e77f0910835686ba6fba0aececa6e645429bcd1afda8ea238`.
- `successor_ref_v9.py` held its §0 pin: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/refusal_vocabulary_check.py` held the draft's cited digest: `a3f64aef6e7b9d2e2e9f70449e320b1430579529f928a13ac67446724d24a422`; exact V71 returned 0 problems; its self-test returned 20 controls, 0 failures, every code controlled.
- `prereg_lint.py` exited 0 with 97 advisory legacy citations and 0 blocking findings. Per the brief, I did not report those advisories.
- `prereg_counts.py` independently parsed 16 class-P and 8 class-E rows, matching the prose.
- `void_registry.py --self-test` returned 6 controls and 0 failures.
- The V71 operation-token repair defeats simple recurrence splitting by spelling: `operation` is now required to come from a closed BS-2k set.
- The continuation repair now lets a post-BS-L explanation follow its entry into the independently authenticated continuation; I did not re-find V70 F2 as a location/custody defect.
- The §11 enumeration item now names all five consultations (`BS-L`, opening, `BS-7f`, `BS-V`, disclosure); I did not re-find V70 F3.
- The within-draw comparison correctly avoids treating draw-to-draw baseline noise as gradient sensitivity. A weak aggregate shift with no categorical flip is outside the explicitly stated verdict-invariance estimand, so I did not count it as a defect.
- The gamma manifest now rejects every `|γ| > gamma_bound`; I did not re-find CODEX-V70 F8.
- The raised-site table closes arithmetically to 112 nodes (25 CALLER + 60 INTEGRITY + 20 NUMERICAL + 3 PLANNING-INTERNAL + 1 TYPED-OUTCOME + 3 WRAPPER). I did not re-find the parked per-raise-versus-call-site unit defect.
- I did not count the parked availability-code/object-identity leak, durable pre-verdict state, VOID partition, strata/producer question, BS-3g lifecycle cycle, `REFUSED-INTEGRITY-MISMATCH`, or `require_authorization` weakness as new findings.

## Evidence and scope

Files read as content: `gates/BRIEF_V71_REVIEW.md`; the exact V71 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/gain_counterfactual_path.py`; both V70 whole-review reports; and `tools/refusal_vocabulary_check.py`. I also executed the named lint/count/registry/refusal checks and recomputed relevant SHA-256 digests. Commands were read-only. No draft, spec, reference file, checker, ledger, or gate artifact was modified; only this report was written.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V71
VERDICT: NOT CLEAR
COUNT: 7
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 621, 624–625, 630; LIFECYCLE_GUARANTEE_SPEC.md lines 31–32 | The draft's normative G2/G3 block still carries the refusal-excluding wording that the companion spec repaired.
F2 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md G2 line 31; §6.1 lines 589–607 | G2 makes refusal/no-effect true but does not require the refusal-reason token to be true, so a false specific code bypasses catch-all enumeration.
F3 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §5 lines 89–101; §6.1 line 649 | An operator can keep one display session alive indefinitely across repeated human views and cached-frame transformations under one event.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 610, 656 | Free-form signed explanations can encode χ through wording or representation while describing only request/authorisation state.
F5 | HIGH | REPAIR-REQUIRED | §6.1 line 610; §11 lines 1352–1362 | Signature and emission join cannot show that an explanation is true of the joined catch-all event.
F6 | MEDIUM | REPAIR-REQUIRED | §11 lines 1143–1149, 1251–1259, 1311–1318 | The new counterfactual-path digest is a fourth module digest, but the verifier contract still recomputes only the pre-existing three.
F7 | MEDIUM | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md §0–§3 lines 12–19, 26–62 | Delete/truncate and custody-relevant metadata mutations are neither conveyance, render nor write and land in no G/N crash-window cell.
<!-- END FINDINGS-BLOCK -->
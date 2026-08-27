# PREREGISTRATION-TEXT V12 REFEREE — GPT56

## Verdict

**NOT CLEAR.** V12 remains numerically falsifiable: §5 fixes a reproduction region, a rejection region, and an exhaustive inconclusive remainder, with strict behavior at p = 0.001 and p = 0.05. The header now consistently distinguishes the predecessor's 60,308-brick sample (an input) from its 208,405 sealed χ measurements (not an input), and the quoted V12 geometry, power-floor, closure, digest and Clopper–Pearson numbers I checked match the underlying machine artifacts. But candidly labelling an operative ambiguity does not make it an acceptable freeze posture. Stage P is still dual-valued; the repaired no-access order is not instantiable by BS-V/BS-2f and still assigns pre-unblinding and post-unblinding events to one receipt; and the new BS-2a acceptance design is simultaneously called Class P and placed in Class E, has two incompatible homes for its confidence threshold, is absent from the normative schema, and leaves the prerequisite count stale. Blocking findings: F1–F3.

## Numbered findings

### F1 — BLOCKER — openly declaring Stage P dual-valued is honest draft status, not an acceptable preregistration promise

**Section / sentences.** §2.6 says “STAGE P REMAINS DUAL-VALUED,” says the document has “two operative definitions,” and says BS-5p cannot be filled. The following paragraph nevertheless says the text “promises the EXACT per-trial test.” §4 still defines the shared-null route: one 20,000-permutation reference null per prefix, `PWR_CONSERVATISM` deflation, and sampled own-null checks. §0 says the pinned code defines every mechanism and code wins over conflicting prose. The pinned `successor_ref_v9.py:1218–1277` implements the shared-null route, and `build_plan()` calls that implementation.

**Why it fails as a promise.** The disclosure is accurate, but a preregistration cannot freeze while deliberately retaining two answer-bearing power tests. The exact route and shared-null route can disagree on which prefixes pass, hence on `L_min_plan`, `L_plan`, the selected footprint, and whether BS-5p exists. Saying “open blocker” prevents laundering the ambiguity as finished; it does not convert the ambiguity into a single rule that independent operators can enforce. The brief's proposed posture is therefore acceptable only for a work-in-progress draft. It is not sound enough to be frozen “once its slots are filled,” because BS-5p is expressly unfillable under the present bytes.

**Smallest sufficient repair.** Before any freeze, choose one route and make §0, §2.6, §4, the pinned code, fixtures, receipt schema and BS-5p producer all name that same route. If exact per-trial Stage P is chosen, implement the 1,000 × 20,000 own-null test in the newly pinned reference code, including plus-one p-values, stream addresses, serialization, failure semantics and final-set re-pass, then gate and remeasure it. Alternatively amend §0's precedence rule and remove the shared-null implementation from the normative mechanism set; merely adding another prose supersession sentence is insufficient.

### F2 — BLOCKER — the repaired BS-5f → lock → unblinding order still cannot be recorded or executed by the slots the covenant names

**Section / sentences.** §6.1(1) says the primary lock is sealed by a signed BS-V receipt before unblinding and that the receipt names the accepted-mask, calibration and decision-input digests. §6.1(2) says named key holders are “recorded in BS-V's schema before any image byte.” §6.1(3) says the access-log digest is receipted at BS-2f and BS-V. §7 instead places BS-V in Class E as “verdict + primary lock,” containing the post-unblinding `decide()` output, and gives it only “disclosure” as its block. The normative schemas are exact: `successor_ref_v9.py:191–195` gives BS-2f `(brickid, objid, c, accept_flag, bin, boundaries, mask_digest)` and BS-V `(verdict, A_L, p, sigma_comb, evaluated_floor, path, mask_digest)`. Neither accepts key holders, access-log digests, calibration digests, decision-input digests, a lock state, a signature or an unblinding authorization.

**Why it fails as a promise.** The sentence-level event order is now correct in §4, §5 and §6.1: BS-5f precedes lock, and lock precedes unblinding. But §7 and the code still make BS-V a verdict receipt, which cannot exist until after unblinding and computation. The same receipt therefore must both seal the lock before unblinding and contain the verdict after unblinding. It also cannot carry any of the evidence §6.1 says makes the covenant checkable. An operator cannot instantiate the promised lock or custody record under §0's code-precedence rule, and a future reader can use §6.1 or §7 to infer different BS-V timing. The V12 event-order repair is not consistent everywhere.

**Smallest sufficient repair.** Split the record into at least (a) a Class-P custody-design receipt, before any image byte, carrying named key holders, role exclusions, permitted automation, log schema and digest-chain rules; (b) a distinct pre-unblinding LOCK receipt, after BS-5f, binding the accepted mask, calibration, all decision inputs and the audited access-log head; and (c) a post-unblinding verdict receipt. Put the corresponding exact schemas and refusal guards in the newly pinned code. State only the order custody design → inference/calibration → BS-5f → LOCK → Duho-authorized unblinding → BS-7f/verdict → disclosure.

### F3 — BLOCKER — BS-2a repairs the acceptance idea but not its freeze boundary, threshold authority, schema or slot count

**Section / sentences.** §2.7(6) calls BS-2a “its own class-P slot,” assigns it the numeric confidence threshold, and says it closes before BS-6. The next item, misnumbered “5,” says the same threshold is pinned in BS-3. §7's Class-P summary still says the DESIGN slots are “BS-2f, BS-5p, BS-8p and BS-9” and that one of twelve Class-P slots is filled. BS-2a appears only under the **Class E** heading. BS-2f is still called DESIGN in the summary even though the new table calls it value-only. The Class-P table contains twelve rows without BS-2a; treating the prose declaration as controlling creates thirteen. The normative `SLOT_SCHEMA` has no BS-2a entry, while BS-3 remains exactly `(weights_sha256, tau, antisymmetry_receipt)` (`successor_ref_v9.py:185–204`). `require_complete_sample()` still only compares two integers (`:1647–1649`).

**Why it fails as a promise.** The substantive boundary is better drawn than V11's: evidence-backed predicate recomputation, a defined confidence quantity, fixed retry/failure semantics and frozen code all belong before images, while BS-2f should contain only realized values. But V12 does not make that boundary enforceable. If the table controls, BS-2a is an execution gate rather than a freeze prerequisite and the document can be signed while the answer-determining acceptance rule is still undefined. If the prose controls, the Class-P list and “one of twelve” count are false. The confidence threshold can be claimed as a BS-2a field or a BS-3 field, yet the pinned code admits neither. Under §0, a BS-2a receipt cannot be emitted at all. An operator still has discretion over which threshold and acceptance implementation became binding, and when.

**Smallest sufficient repair.** Move BS-2a into Class P; remove BS-2f from the DESIGN-slot list; update the prerequisite total to thirteen (or deliberately merge BS-2a into an existing Class-P slot and keep twelve); assign the confidence definition and numeric threshold to exactly one slot; make BS-6 depend on that Class-P receipt; and implement/pin the BS-2a schema, evidence validator, retry/failure semantics, confidence symmetry guard and fixtures before the next text gate. Renumber §2.7. The acceptance design should remain pre-image; that part of V12's intended boundary is correct.

### F4 — MAJOR — §6.1(5) does not establish that the already-completed redesign was blind

**Section / sentence.** §6.1(5) says the successor footprint was chosen from geometry alone and says this is established because `REAL_GEOMETRY_RESULT_20260825.md`, the selection artifacts and their digests contain no χ-derived quantity. The document is still a draft and “nothing in it is in force,” while the geometry choice was made on 2026-08-25. The predecessor χ archive already existed.

**Why it fails as a promise.** Absence of χ fields from a geometry artifact proves only that the artifact does not serialize χ. It does not show that a designer had no earlier read access to the predecessor store, saw no summary, or did not use remembered outcomes when selecting or approving the geometry rule. A person could have inspected predecessor outcomes, then written a geometry-only artifact containing no χ-derived field; all of §6.1's prospective logging and role rules could begin later without revealing that event. Thus the proposed evidence does not establish the historical claim it is said to establish. This is the principal remaining way to comply with the future machinery while the redesign itself was not blind.

**Smallest sufficient repair.** Before freeze, require a custody/access receipt covering the period from predecessor sealing through the final geometry choice: named design actors and key holders, append-only successful/refused access logs, key-custody history, and attestations binding the redesign artifacts and dates. Define any unexplained access by a design-capable actor as a void. If such retrospective evidence does not exist, label “geometry-only redesign” as unverified testimony/limitation rather than saying the artifact contents establish it.

### F5 — MAJOR — the negative-result interpretation remains underbound

**Section / sentences.** §1 says the test does not test “A ≈ 0.02, Shamir, BHU, or whether the sky is isotropic.” §5 defines `REJECTED-AT-LONGO-AMPLITUDE` and three inconclusive outcomes but supplies no mandatory interpretation of those labels.

**Why it fails as a promise.** The numeric rejection rule is clear, so the claim can fail. But the reportable scientific meaning remains outcome-dependent. The text does not expressly bind rejection to this release, footprint, acceptance rule, instrument, calibration contract and fixed axis; does not say it excludes no smaller nonzero amplitude generally; does not say every inconclusive outcome establishes neither reproduction nor rejection; and does not bar claims that it settles other researchers' differently defined results. Listing one smaller amplitude and three named topics is not equivalent to a general interpretation rule.

**Smallest sufficient repair.** Add a binding results-interpretation clause: `REJECTED-AT-LONGO-AMPLITUDE` means only that +0.0408 at the registered Longo axis failed the registered test under this population/measurement/calibration contract. It neither proves isotropy nor excludes smaller amplitudes, other axes, or other researchers' claims. Every `INCONCLUSIVE*` outcome establishes neither presence nor absence. Scope `REPRODUCED-LONGO` to the same registered conditions.

### F6 — MAJOR — the release fork still depends on an undefined availability adjudication

**Section / sentences.** §2.1 selects Branch A iff DR11 photo-z “exists and is publicly retrievable at the resolution moment,” and closes BS-1 on the earlier day availability “is confirmed” or 2026-09-05. The pinned `resolve_branch()` accepts a caller-supplied `photoz_available` boolean and validates only date shape/order (`successor_ref_v9.py:1668–1689`).

**Why it fails as a promise.** The branch consequences are now honest: Branch A voids the current pin and requires a new preregistration. But the event selecting the population is still not a pure function of frozen evidence. No authoritative endpoint/product/version, probe schedule, responsible witness, retry window, transient-error rule, partial-schema rule, timezone or signed raw-response receipt is defined. Before the deadline, choosing when to probe controls when the “earlier” event occurs; at the deadline, a transient failure can be treated as absence. This is a researcher degree of freedom over the population, albeit one disclosed as open.

**Smallest sufficient repair.** Freeze the availability probe, authoritative endpoints and expected schema/version, schedule, KST/UTC convention, retry/error policy and signed raw-response witness. Make BS-1 a pure function of that evidence. Treat unresolved transport/service errors as unresolved, not as product absence.

### F7 — MINOR — the corrected 951 floor count still conflicts with a named source artifact

**Section / artifacts.** V12 §2.6 correctly says 951 of 1,000 own p-values equal `1/20001`. `STAGEP_EXACT_RECEIPT_20260826.json` contains 1,000 p-values, 995 below 0.001, and exactly 951 equal to `4.999750012499375e-05`. But the final “STAGE P RESTORED” section of the named `REAL_GEOMETRY_RESULT_20260825.md` still says “995 of the 1,000 own p-values sit at `5.00e-05`.”

**Why it fails as a promise.** V12's number is right, so this does not change the decision rule. But a future auditor following the draft's named geometry record encounters two incompatible counts, and the preamble's claim that numeric errors were corrected “in place” is not true across the cited evidence chain.

**Smallest sufficient repair.** Append a non-destructive correction to `REAL_GEOMETRY_RESULT_20260825.md` changing only the floor count to 951 while retaining 995 as the success count, or state explicitly that the JSON receipt supersedes that sentence.

## Falsifiability and decision-boundary review

The promise can fail numerically. `REPRODUCED-LONGO` requires p < 0.001, the registered sign, the three-sigma agreement band and the evaluated detection floor. `REJECTED-AT-LONGO-AMPLITUDE` requires p > 0.05 and the registered upper bound below 0.0408. Every other numeric result, including equality at p = 0.001 or p = 0.05, is `INCONCLUSIVE`; the two pre-unblinding halts are separate inconclusive outcomes. I found no numeric result that can be absorbed into either desired claim. F5 concerns the meaning allowed after the fixed label, not the exhaustiveness of the numeric partition.

## Researcher-degrees-of-freedom ledger

### Closed by V12 or the pinned mechanism

1. Target paper, oriented sign, +0.0408 amplitude, fixed axis and coordinate frame.
2. The eight catalog predicates and explicit absence of a surface-brightness cut.
3. Raw-versus-retained roles, retention factor, leverage floor, 20% planning margin, exact-versus-production-scale boundary and deterministic selection order, subject to F1's unresolved Stage-P producer.
4. Production permutation count, one-sided plus-one p-value, exact-float tie rule and non-finite refusal.
5. Numeric reproduction/rejection/inconclusive inequalities and the detection floor.
6. Calibration-bin tie rule, allocation tie/floors, scalar/profile switch and calibration halt, subject to the still-unfilled BS-8p design.
7. Conceptually, the terminal-status partition, closed exclusion-reason vocabulary, evidence-backed recomputation and intended sign/axis blindness. F3 explains why their pre-image authority is not yet mechanically frozen.
8. The predecessor's 208,405 χ measurements are consistently historical-only: the header and §6.2 both say they are not successor analysis input. I found no third sentence licensing reuse.
9. Post-first-real-χ changes to binding rules/code/thresholds void the run.

### Open or not yet mechanically closed

1. Exact per-trial versus shared-null Stage P (F1).
2. Custody schemas, pre-image key-holder receipt, access-log receipt, lock/verdict separation and executable lock timing (F2).
3. Acceptance design's class, threshold authority, slot count, schema and implementation (F3).
4. Historical no-access evidence for the already-completed geometry redesign (F4).
5. DR11 availability adjudication and the disclosed release fork (F6).
6. BS-9's production input function/tensor path, BS-8p's HC-1H rule package, and the clean-room normative specification; V12 correctly says these need new design revisions/gates.
7. Mandatory scientific interpretation of rejection and inconclusive outcomes (F5).
8. Selection provenance: the frozen selection still has no producer receipt, as the draft/freeze disclose.

## Circularity review

I found no outcome-circular numeric boundary in §5. The decision constants are fixed; Stage C and calibration precede unblinding; Stage C uses realized accepted geometry rather than the later real-sky statistic. Stage P's prefix search is simulation-adaptive planning followed by a fixed margin and final re-pass, not adaptation to real χ, but F1 must make its success test singular. The remaining circularity risks are procedural: F3 leaves the acceptance threshold/implementation's authority ambiguous even though acceptance changes the geometry Stage C judges, and F4 lacks evidence excluding earlier outcome access by people who shaped that geometry.

## Artifact and number checks

- Recomputed SHA-256 values match §0/freeze: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`; `FIXTURES_V9_20260826.out` = `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`; `CLOSURE_V9_KIMI.md` = `f2ee062bb7f1ced33e5530d6655765f32b5830342154274ecf885c73dc722f01`.
- Parsed `STAGEP_EXACT_RECEIPT_20260826.json`: 1,000 p-values; 995 are < 0.001; 951 equal `1/20001`; geometry is 6,445 bricks, n = 53,005, Var(c) = 0.7546638984846564 and N_eq = 120002.87981753764. Independent arithmetic `3 × 53,005 × Var(c)` gives the same N_eq.
- The exact receipt names `../ref/successor_ref_v7.py` with digest `6be341bd…`, not the v9 normative subject. V12 correctly refuses to use it to fill BS-5p.
- One-sided 95% Clopper–Pearson lower bounds recompute to 0.9493659932 at x = 961 and 0.9504871297 at x = 962, so x ≥ 962 is correct.
- Closure arithmetic recomputes: 12,117 / 6,445 = 1.8800620636 and 12,117 × 12.2 MB = 147.8274 decimal GB, supporting ≈148 GB.
- The fixture transcript states `PWR-SELF-VERIFYING` audited 12 boundary trials, confirmed 10 and refuted 2, matching V12.
- The correction chain in `REAL_GEOMETRY_RESULT_20260825.md` reaches 6,445 selected bricks, 65,060 raw objects, 53,005 retained, Var(c) = 0.754664, N_eq ≈ 120,003 and exact Stage P 995/1000. F7 is the remaining stale floor-count sentence.

## Incompleteness and honesty

V12 is candid that it is a draft, that only BS-2m is filled, that Stage P is unresolved, that the exact harness is not normative, that the selection lacks a producer receipt, and that closure had one referee seat. It does not read as if a run is authorized. However, “These fill the class-P inputs” (§2.6) remains too broad given the same document's one-filled-slot count, and F3 makes that count/classification internally false after adding BS-2a. Honesty about incompleteness is a positive property, but it cannot substitute for a single-valued freeze contract.

## Failed attacks / positive evidence

- I could not find a third statement making predecessor χ an input; the repaired header and §6.2 agree.
- I could not make p-boundary equality count as reproduction or rejection, or find a numeric outcome outside the declared labels.
- I found no mismatch in the corrected code/worker/fixture/referee digests, 951 floor count, 2-of-12 fixture count, 995/1000 exact success count, geometry values, Clopper–Pearson boundary or closure-cost arithmetic.
- Branch A no longer silently inherits Branch-B measurements or pins; selecting it expressly voids the current pin and requires remeasurement and a fresh text gate.
- The new acceptance prose no longer permits caller labels alone to establish reasons: it requires predicate recomputation from named evidence and disagreement refusal. F3 concerns where/how that design becomes binding, not the intended logical shape.
- I found no hidden global-optimality claim for the production-scale selector.

## Testimony

The named records state that the redesign used geometry only, no image byte was fetched, no χ was read, the predecessor χ remain sealed, the exact harness ran for approximately 431 seconds, and two intended closure-referee seats were refused by their provider. I verified the files, schemas, code paths, hashes and arithmetic described above, but did not inspect `/Users/duhokim/NebulaMindData/`, the sealed store, historical or live access logs, key custody, remote TAP jobs, running processes or provider events. Those conduct/history assertions remain testimony. In particular, artifact inspection alone cannot verify the historical no-access claim in F4.

## Evidence ledger

Content read: `BRIEF_PREREG_TEXT_V12.md`; `PREREG_SUCCESSOR_DRAFT_V12_20260827.md`; the V11→V12 diff; prior GPT56 V10/V11 reports for closure context only after reading V12 fresh; `ref/successor_ref_v9.py` schema, Stage-P, completeness and branch-resolver spans; `ref/FIXTURES_V9_20260826.out`; `real/REAL_GEOMETRY_RESULT_20260825.md`; `real/STAGEP_EXACT_RECEIPT_20260826.json`; `gates/FREEZE_CLOSURE_V9_20260826.md`; and the relevant beginning of `gates/CLOSURE_V9_KIMI.md`. Machine checks performed: SHA-256 over the four pinned artifacts; JSON parsing/counting of all 1,000 exact p-values; independent N_eq, closure ratio, download-size and Clopper–Pearson calculations; text searches for predecessor-input statements, decision interpretations, slot classifications, threshold homes and corrected/stale numbers. I did not run the full fixture suite because this assignment judges the promise and the pinned fixture transcript/hashes were sufficient for the quoted checks; no production or data-access path was executed.

**NOT CLEAR**

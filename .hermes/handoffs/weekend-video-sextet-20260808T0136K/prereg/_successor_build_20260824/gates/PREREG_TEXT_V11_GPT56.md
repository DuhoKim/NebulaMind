# PREREGISTRATION-TEXT V11 REFEREE — GPT56

## Verdict

**NOT CLEAR.** V11 remains falsifiable: §5 fixes a genuine reproduction region, a genuine rejection region, and an exhaustive inconclusive remainder, with strict boundary behavior. It also repairs the quoted floor count, planner digest, boundary-audit count, Branch-A consequence, and most of the acceptance-rule prose. But four answer-bearing promises are still non-single-valued or non-instantiable under the document's own normative-code rule: the new no-access covenant cannot be recorded in the schemas it names and states an impossible event order; the preamble still calls predecessor χ “successor input” while §6.2 forbids it as input; the acceptance design is simultaneously called a DESIGN slot and placed in Class E, while its confidence threshold is absent from BS-3; and §4 plus the pinned code still define the shared-null Stage P after §2.6 says the exact route supersedes it. Blocking findings: F1–F4.

## Numbered findings

### F1 — BLOCKER — §6.1's no-access covenant cannot be instantiated by the slots/code it names, and its event order contradicts itself

**Section / sentences.** §6.1(1): the primary lock occurs when “BS-5f's confirmatory power receipt exists” and is “sealed by a signed BS-V receipt.” §6.1(2): prohibited actors remain barred “until the lock, unblinding and BS-5f have occurred in that fixed order.” §6.1(2) also says key holders are “recorded in BS-V's schema before any image byte”; §6.1(3) says the access-log digest is receipted at BS-2f and BS-V. §7 instead defines BS-V as the execution-time “verdict + primary lock.” The pinned code's exact schemas are BS-2f = `(brickid, objid, c, accept_flag, bin, boundaries, mask_digest)` and BS-V = `(verdict, A_L, p, sigma_comb, evaluated_floor, path, mask_digest)` (`successor_ref_v9.py:185–205`), and `receipt()` refuses every extra field (`:208–224`).

**Why it fails as a promise.** This is stronger than V10's embargo in prose, but it is not a realizable binding mechanism. Neither named schema can carry a key-holder list or access-log digest, and the normative receipt function rejects adding either. BS-V cannot both record key holders before the first image byte and be the post-unblinding verdict receipt. The temporal clause orders lock → unblinding → BS-5f, while the preceding paragraph requires BS-5f to exist before the lock; §4 independently requires BS-5f before unblinding. A compliant operator therefore cannot determine which order is promised or produce the evidence the covenant requires. Because §0 says code wins over disagreeing prose, the current code leaves the repaired blinding evidence undefined rather than merely unfinished.

**Smallest sufficient repair.** Split the events and schemas. Add a Class-P custody/lock-design receipt, produced before any image byte, carrying named key holders, role exclusions, storage/enforcement identity, permitted automation, and the append-only log schema/digest chain. Add a distinct pre-unblinding LOCK receipt after BS-5f that binds mask, calibration and decision inputs; retain a separate post-unblinding verdict receipt. State one order only: accepted mask/calibration → BS-5f → input lock → Duho-authorized unblinding → BS-7f/verdict → disclosure. Implement those fields and guards in the newly pinned code, with missing or changed log custody voiding the run.

### F2 — BLOCKER — V11 still says the predecessor χ are both successor input and not an input

**Section / sentences.** Preamble line 22: the predecessor's “208,405 sealed χ measurements are archived as successor input.” §6.2: “No predecessor χ measurement enters this run's analysis. Every χ this study uses is measured fresh under this text,” and the archive “is not an input.”

**Why it fails as a promise.** These are direct opposites about admissible analysis data. “Archived as successor input” is not merely provenance language: it licenses the exact reuse that §6.2 says requires a new text, gate and signature. A future operator can cite either sentence while claiming literal compliance. The repair therefore did not make the predecessor boundary single-valued.

**Smallest sufficient repair.** Replace the preamble sentence with “the 208,405 sealed χ measurements are retained as historical record and are not an input to the successor”; if the 60,308-brick/sample artifacts are legitimate geometry/provenance inputs, name those separately without coupling them to χ.

### F3 — BLOCKER — §2.7 fixes the conceptual exclusion rule but leaves its pre-data design gate and confidence threshold unbound

**Section / sentences.** §2.7(2) permits exclusion when confidence is below “the threshold pinned in BS-3”; §2.7(5) repeats that the threshold is pinned in BS-3 before any image byte. §2.7 then says BS-2f is a DESIGN slot until the rule is implemented. §7's Class-P note lists BS-2f among DESIGN slots, but its table places BS-2f under **Class E**, after BS-6's first-image-byte gate. BS-3's table content is only weights, τ and antisymmetry; the pinned code agrees, defining BS-3 as `(weights_sha256, tau, antisymmetry_receipt)`. The current `require_complete_sample()` still compares two integers rather than deriving a partition (`successor_ref_v9.py:1647–1649`), which V11 candidly acknowledges.

**Why it fails as a promise.** The closed reason list, exact parent partition, sign/axis blindness, and ledger recomputation are the right shape. But the document provides no Class-P slot that freezes their implementation before images, and the one threshold that directly changes acceptance cannot be inserted into the schema the prose names. Calling BS-2f both a pre-freeze DESIGN item and a Class-E realized mask conflates two different things: the rule that must be frozen before data and the values necessarily produced after inference. As written, a later confidence threshold or acceptance implementation could be presented as filling BS-2f even though it changes the answer after image bytes exist.

**Smallest sufficient repair.** Create a separate Class-P acceptance-design slot (or expand BS-3 explicitly) that pins the numeric confidence threshold, retry/failure semantics, machine-checkable evidence for reasons (a)–(d), ledger schema, recomputation code and fixtures before BS-6. Keep BS-2f as the Class-E value-only realized partition/mask produced by that frozen code. Update the exact code schemas and make BS-6 depend on the acceptance-design slot.

### F4 — BLOCKER — the Stage-P promise is still dual-valued under §0's precedence rule

**Section / sentences.** §2.6 says: “This text promises the EXACT per-trial test,” declares §4's shared-null contract superseded, and says BS-5p needs new implementation and a fresh gate. §4 nevertheless says in operative present tense that Stage P “measures the standardized permutation null once per prefix,” judges all trials against that shared tail, deflates by `PWR_CONSERVATISM`, and audits a subset. The pinned `stage_power()` does exactly that (`successor_ref_v9.py:1218–1277`), and `build_plan()` calls it (`:1291–1347`). §0 says the code defines every mechanism and “the code is the definition” where prose disagrees.

**Why it fails as a promise.** The new supersession sentence signals intent and correctly prevents filling BS-5p from the existing measurement, but it does not leave one operational definition. The normative code and the section titled “Power gate” still define the old route, while §2.6 defines the exact route. The existing exact receipt also records `successor_ref_v7.py`, not the v9 subject, as V11 properly discloses. A later operator still has two textual/code bases to cite; the promise becomes single-valued only after the design revision that V11 says is still required.

**Smallest sufficient repair.** Implement exact per-trial Stage P in the newly pinned reference code, including the 20,000 count, plus-one rule, addresses, serialization, failure behavior and final-set re-pass; gate it; replace §4's shared-null/deflation/subsample paragraphs rather than retaining them as operative prose; and produce BS-5p under those exact bytes. The shared-null route may remain only in a clearly non-normative history note.

### F5 — MAJOR — the negative-result interpretation still omits the required limits

**Section / sentences.** §1 says the study tests the published amplitude and axis and “does not test A ≈ 0.02, Shamir, BHU, or whether the sky is isotropic.” §5 defines `REJECTED-AT-LONGO-AMPLITUDE` and the inconclusive outcomes but supplies no binding interpretation paragraph.

**Why it fails as a promise.** The numeric rejection region is unambiguous, so the study can fail. But the text does not explicitly bind the reportable meaning: rejection is conditional on this release/footprint, accepted-object rule, instrument and calibration assumptions; it does not exclude smaller nonzero amplitudes generally; and an `INCONCLUSIVE*` result supports neither presence nor absence. One example, “A ≈ 0.02,” does not forbid broader “no dipole” or “isotropy” summaries. This leaves freedom in the scientific claim after seeing the outcome even though the numeric label is fixed.

**Smallest sufficient repair.** Add a mandatory results-interpretation clause: rejection means only failure of +0.0408 at the fixed Longo axis under the registered population/measurement/calibration contract; it neither proves isotropy nor excludes smaller amplitudes, other axes, or other researchers' claims; every `INCONCLUSIVE*` outcome establishes neither reproduction nor rejection. Apply the same conditional scope to `REPRODUCED-LONGO`.

### F6 — MAJOR — the release fork still depends on an undefined availability adjudication

**Section / sentences.** §2.1 selects Branch A iff DR11 photo-z “exists and is publicly retrievable at the resolution moment,” and resolves on the day availability “is confirmed” or 2026-09-05. BS-1 records `photoz_available`, but neither text nor code defines the probe that establishes it.

**Why it fails as a promise.** The fallback date and Branch-A void consequence are now explicit. The epistemic event is not: there is no authoritative URL/product schema, check schedule, retry window, transient-error treatment, timestamp convention or raw-response witness. Before the fallback date, choosing when to look determines when the “earlier” event occurs; at the deadline, a transient failure can select Branch B. This is an open population choice, not merely a measured value.

**Smallest sufficient repair.** Freeze the availability probe, responsible independent witness, authoritative endpoints/product/schema checks, schedule, retry/error policy, timezone and signed raw response receipt. Make BS-1 a pure function of that evidence, with uncertainty remaining unresolved rather than silently becoming absence.

## Falsifiability and decision-boundary review

The claim can fail. `REPRODUCED-LONGO` requires p < 0.001, the registered sign, the three-sigma agreement band and the detection floor. `REJECTED-AT-LONGO-AMPLITUDE` requires p > 0.05 and the registered upper bound below 0.0408. Every other numeric outcome, including equality at p = 0.001 or 0.05, is `INCONCLUSIVE`; the two pre-unblinding halts are separate inconclusive outcomes. I could not make the decision function absorb every result. F5 concerns the meaning permitted in prose after that fixed outcome, not the numerical partition.

## Researcher-degrees-of-freedom ledger

### Closed by V11 or the pinned mechanism

1. Published target, oriented sign, +0.0408 amplitude, fixed axis and coordinate frame.
2. The eight catalog predicates and explicit absence of a surface-brightness cut.
3. Raw-versus-retained roles, retention factor, count/order construction, exact-versus-production-scale boundary, leverage floor, 20% planning margin and deterministic reduction order, subject to F4's Stage-P producer.
4. Production permutation count, one-sided plus-one p-value, exact-float tie rule and non-finite refusal.
5. Numeric reproduction/rejection/inconclusive inequalities and detection floor.
6. Calibration bin tie rule, allocation tie/floors, scalar/profile switch and calibration halt, subject to unfilled BS-8p.
7. Parent terminal-status partition, closed exclusion-reason vocabulary, sign/axis-blindness requirement and intended ledger recomputation at the prose level; F3 explains why the design is not yet frozen operationally.
8. Post-first-real-χ alteration of binding rules/code/thresholds voids the run.

### Open or not yet mechanically closed

1. Custody roles, log schemas, lock/unblinding order and pre-image key-holder receipt (F1).
2. Whether predecessor χ are admissible successor input (F2).
3. Confidence threshold, exclusion evidence/retry semantics, acceptance producer code and its true Class-P gate (F3).
4. Exact versus shared-null Stage P (F4).
5. DR11 availability adjudication (F6), plus the disclosed branch itself until resolution.
6. BS-9 production input function/tensor path, BS-8p HC-1H rule package, and the clean-room normative specification; V11 correctly classifies these as requiring a new revision/gate.
7. The scientific interpretation of rejection and inconclusive outcomes (F5).
8. The access-safe hand-check workflow: the committee necessarily handles real-label information, while the new custody schema/role separation that would show who can see what is part of F1's missing implementation.

## Circularity review

I found no outcome-circular numeric boundary in §5. The decision constants are fixed; calibration and Stage C are scheduled pre-unblinding; Stage C uses realized accepted geometry rather than the later sky statistic. The Stage-P search derives `L_min_plan` from simulations on candidate geometry and then applies the fixed 1.2 margin and final re-pass; that is disclosed simulation-adaptive planning, not circular use of the real χ outcome. The present circularity risks are procedural rather than algebraic: F3 allows an unpinned acceptance threshold/implementation to determine the geometry that Stage C judges, and F1 does not yet provide an executable separation between people handling calibration/access and people able to alter or adjudicate the promise.

## Artifact and number checks

- Recomputed SHA-256 values match §0 and the freeze: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`; `FIXTURES_V9_20260826.out` = `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`; `CLOSURE_V9_KIMI.md` = `f2ee062bb7f1ced33e5530d6655765f32b5830342154274ecf885c73dc722f01`.
- The v9 code pins planner digest `1617af00eb7398abd93cc2726dbfb1ecfb24d07bede4b84c128ef2442bf40cb4`, matching V11's corrected `1617af00eb73…` statement.
- Parsed the exact Stage-P receipt independently: 1,000 trial p-values; 995 are < 0.001; exactly **951** equal `1/20001 = 4.999750012499375e-05`. V11's corrected floor count is right. The receipt gives 6,445 bricks, n = 53,005, Var(c) = 0.7546638984846564 and N_eq = 120002.87981753764; `3 × n × Var(c)` reproduces N_eq exactly.
- The fixture transcript says `PWR-SELF-VERIFYING` audited 12 boundary trials, confirmed 10 and refuted 2. V11's corrected “2 of 12” is right.
- Independently recomputed the one-sided 95% Clopper–Pearson lower bounds: x = 961 gives 0.9493659932 and x = 962 gives 0.9504871297, so x ≥ 962 is the correct integer rule.
- Closure arithmetic is consistent: 12,117 / 6,445 = 1.8800620636; 12,117 × 12.2 MB = 147.8274 decimal GB, supporting ≈148 GB.
- The geometry correction chain ends at the values V11 quotes: 6,445 selected bricks, 65,060 raw objects, 53,005 retained, Var(c) = 0.754664, N_eq ≈ 120,003 and exact Stage P 995/1000. The earlier 6,446/65,062, ~77 GB, 997/1000 and shared-null justification failure remain visibly corrected/retracted.
- The exact Stage-P receipt records its subject as `../ref/successor_ref_v7.py` with digest `6be341bd…`, not v9. V11 accurately treats it as an unrefereed measurement that cannot fill BS-5p.

## Incompleteness and honesty

V11 is candid that only BS-2m is filled, that eleven of twelve Class-P slots remain empty, that BS-5p/BS-8p/BS-9 require design work and fresh gates, that the selection lacks a producer receipt, and that closure received one referee seat. I found no attempt to present the exact Stage-P measurement as an accepted normative result. The remaining overstatement is structural: §0 still says the current code defines “every operational mechanism” although §2.7, §6.1 and §2.6 introduce mechanisms the current schemas/code cannot implement. F1, F3 and F4 name the concrete consequences rather than treating that universal sentence as a separate stylistic finding.

## Failed attacks / positive evidence

- I could not find a numeric outcome outside the four decision labels or make equality at either p boundary count as reproduction/rejection.
- I found no mismatch in the corrected planner digest, p-value-floor count, 2-of-12 audit count, Stage-P success count, geometry values, Clopper–Pearson boundary or closure-cost arithmetic.
- Branch A no longer inherits Branch-B measurements or the current code pin; it explicitly voids the pin and requires remeasurement and a fresh gate.
- The acceptance prose no longer permits arbitrary unnamed reasons or caller-supplied accepted flags; the remaining defect is the absent pre-data implementation/schema gate, not the conceptual rule.
- I found no hidden global-optimality claim for the production-scale selector.
- The one-seat closure limitation, missing selection producer receipt, unrefereed exact harness and non-scaling reference implementations remain disclosed rather than laundered into stronger claims.

## Testimony

The named records state that the redesign used geometry only, no image byte was fetched, no χ was read, the predecessor χ remain sealed, and the exact harness ran for 431.4 seconds. I verified the files, internal arithmetic and contradictions above, but did not read `/Users/duhokim/NebulaMindData/`, inspect the sealed store, access logs, key custody, live processes or remote TAP jobs. Those historical/conduct assertions remain testimony. The records also report that two closure referee seats were refused by providers; I verified the freeze/report text, not the provider events independently.

**NOT CLEAR**

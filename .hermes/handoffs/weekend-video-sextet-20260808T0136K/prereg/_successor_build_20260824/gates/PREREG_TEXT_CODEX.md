# PREREGISTRATION-TEXT REFEREE — CODEX

## Verdict

The draft is unusually candid and many mechanical choices are genuinely closed, but it is not yet a promise that can be frozen. Three blocking seams remain: the accepted analysis sample can be chosen without a frozen acceptance/exclusion rule; the blinding clause prohibits disclosure but not access; and the supposedly branch-neutral frozen definition is actually pinned to the already-measured DR10/Branch-B artifacts. The decision vocabulary also never says that several outcomes which plainly contradict the stated Longo claim count as non-reproduction.

## Numbered findings

### 1. BLOCKING — §2f/§5/§7 leave the accepted analysis sample open after images exist

**Sentence/symbol at issue.** §4 calls BS-2f the “sealed accepted-position mask” and §7 says it contains an “acceptance flag.” §5 says `require_complete_sample()` proves that “every parent object has a measurement receipt.” The code accepts only rows whose supplied `accept` flag is 1 (`successor_ref_v9.py:1033-1043`) but does not define how that flag is produced; `require_complete_sample()` checks only `n_receipts == n_parent` (`:1647-1649`).

**Why this fails as a promise.** A receipt for every parent is not a frozen inclusion rule. A conforming operator can produce 65,060 receipts, mark an outcome-dependent subset accepted, omit the other rows from the `SealedMask`, and proceed if the remaining geometry passes Stage C and the N_eq floor. The text does not state image-quality thresholds, classifier-failure rules, duplicate handling, missing/corrupt cutout treatment, whether a low-confidence or ambiguous winding is excluded, or a deterministic tie/refusal rule. This is the largest remaining researcher degree of freedom because it is exercised after image inference can exist and it changes both signs and geometry.

**Smallest sufficient repair.** Before any image byte, define and pin a per-parent measurement-status state machine and every acceptance/exclusion predicate; require a BS-2f ledger with exactly one terminal status for every BS-2s parent; bind its digest to the measurement receipts; require `run_production_verdict()` to recompute the accepted set from that ledger rather than accept caller-supplied flags. Any status whose derivation can see handedness must be forbidden or shown sign-blind by construction.

### 2. BLOCKING — §6’s blinding rule forbids disclosure, not looking

**Sentence at issue.** “Nothing derived from any real χ value … is published, spoken, or written outside the sealed results store before the primary lock.”

**Why this fails as a promise.** A researcher can open the sealed store, inspect every predecessor or successor χ, keep the observation inside that store, and comply with every word. The draft also does not define the “primary lock,” name who lacks the decryption/access capability, require an append-only access log, or state what evidence would reveal premature access. This is especially material because the predecessor’s 208,405 sealed measurements already exist and the successor redesign is supposed to have been outcome-blind. The geometry receipt says no χ was read; that is author testimony about conduct, not a binding or auditable non-access mechanism.

**Smallest sufficient repair.** Replace the disclosure-only clause with an access prohibition covering predecessor and successor χ and every derivative; define the lock event by digest and timestamp; separate key custody from the analyst; require an externally witnessed, append-only access/decryption log spanning redesign through BS-V; make any pre-lock access or missing log a void. State explicitly what was inspected during redesign and supply the corresponding audit receipt before freeze.

### 3. BLOCKING — §2.1 promises a branch-neutral frozen document, but §0’s normative code and §2.6 are Branch B/DR10-specific

**Sentences at issue.** §2.1 says the release choice “slots in on its date without reopening frozen wording” and “nothing else in this document changes with the branch.” §0 simultaneously makes the current v9 bytes normative for every operational mechanism. Those bytes pin the DR10 universe, count table, parent and selection (`successor_ref_v9.py:102-143`), including 366,912 bricks, 832,393 objects, the Branch-B parent and the 6,445-brick selection. §2.6 then states the Branch-B measured selection and power as document text.

**Why this fails as a promise.** If Branch A is selected, the frozen v9 planning/closure path cannot consume the DR11 universe and selection while honoring its DR10 pins. The 6,445/65,060/12,117/995 figures will also no longer describe the selected branch. Choosing A therefore requires new code bytes, new pins, new measured values, and changed prose—the exact reopening §2.1 says is unnecessary. The `resolve_branch()` configuration table does not cure the hard-pinned downstream witnesses.

The availability rule also leaves “exists,” “publicly retrievable,” the probe endpoint, probe cadence/time, and transient-error treatment to BS-1. That is smaller than the hard-pin contradiction but still permits an operator to choose the resolution moment on or before 2026-09-05.

**Smallest sufficient repair.** Either resolve BS-1 before freezing this text and freeze only the selected branch, or provide and gate two complete branch-specific pin sets and make every downstream loader select the pin set solely from a canonical BS-1 receipt. Define one probe URL/query, exact UTC deadline, retry/error policy, and immutable probe transcript. Move branch-specific measured numbers into the selected branch’s receipt or display both branch results explicitly.

### 4. MAJOR — §5 does not unambiguously say what counts as the Longo claim not being reproduced

**Sentences at issue.** “REPRODUCED-LONGO” is explicit. “REJECTED-AT-LONGO-AMPLITUDE” requires both `p > 0.05` and `|Â_L| + 3σ_ours < 0.0408`; every other numeric result is “INCONCLUSIVE.”

**Why this fails as a promise.** The target claim includes amplitude and oriented sign, yet a precise opposite-sign result, or a precise same-sign amplitude materially larger than 0.0408, is forced to INCONCLUSIVE rather than declared non-reproduction. I executed the pinned helper with scalar accuracy 0.9 and σ(Â)=0.003:

- Â = −0.0408, p = 0.9 → `INCONCLUSIVE`;
- Â = +0.0800, p = 10^-6 → `INCONCLUSIVE`;
- Â = 0, p = 0.9 → `REJECTED-AT-LONGO-AMPLITUDE`.

Thus the promise can fail in the narrow null-shaped region, but it has no sentence mapping all clearly incompatible outcomes to “the specific Longo claim was not reproduced.” `BATTERY-SIGN` only demands “never called REPRODUCED,” which is weaker than answering the stated question. Conversely, a precise Â = 0.020, p = 10^-4 is called `REPRODUCED-LONGO` because the 3σ band includes Longo’s published uncertainty. That may be a defensible compatibility definition, but the text must say plainly that “reproduced” means 3σ compatibility with the published estimate, not recovery of 0.0408 itself.

**Smallest sufficient repair.** Add an interpretation table separate from the machine outcome names: define which outcomes mean the specific amplitude-and-sign claim was reproduced, not reproduced, or genuinely unresolved. At minimum, make a precise wrong-sign estimate and a confidence interval excluding the target count as non-reproduction, or explicitly justify why they do not. Rename `REPRODUCED-LONGO` to a compatibility label if the broad 3σ published-plus-new band is intended.

### 5. BLOCKING — the Stage-P promise and the measured Stage-P evidence are different mechanisms

**Sentences at issue.** §0 says the v9 bytes define “every operational mechanism.” §4 defines `stage_power()` using one shared standardized null, a 1.01 deflation, sampled conservatism checks and selected own-null confirmations. §2.6 and §4 then rely on 995/1000 from an exact per-trial-null harness, while acknowledging that it is “not yet in the definitional code.”

**Why this fails as a promise.** This is more than an unfilled receipt. The mechanism used to establish that the selected design passes is not the mechanism the frozen definition will execute when `build_plan()` searches for `L_min_plan` and re-passes the final set (`successor_ref_v9.py:1319-1342`). The exact receipt itself names `../ref/successor_ref_v7.py`, not v9 (`STAGEP_EXACT_RECEIPT_20260826.json:1033-1037`). Therefore BS-5p cannot be filled mechanically under the current promise: filling it requires changing normative code or accepting evidence from a different algorithm/version.

**Smallest sufficient repair.** Implement the exact per-trial-null Stage P in the normative reference, define its serialization and resource bounds, gate it, rerun both prefix search and final-set re-pass through that exact function, and then pin a BS-5p receipt to the resulting code and selection. Until then, describe 995/1000 only as nonbinding feasibility evidence.

### 6. MAJOR — several class-E “mechanical fills” still contain undefined judgment calls

**Sections at issue.** §6 says only mechanical filling of predeclared class-E values is exempt from the void rule. Yet BS-8f includes unspecified “integrity triggers”; BS-V invokes an undefined “primary lock”; BS-6 names a byte ceiling and producer checksum list without the handling rule for missing/mismatched producer entries; and the hand-check “committee, sealed keys, HC-5, HC-6” are promised only as a future quotation.

**Why this fails as a promise.** These are choices exercised after real images or labels exist. Calling them slot fields does not freeze their semantics. An operator could decide which integrity event halts, what constitutes lock, or how transport anomalies are handled after seeing operationally revealing information.

**Smallest sufficient repair.** Put every class-E schema and state transition in the pre-freeze text/code: enumerated integrity triggers and outcomes, exact committee/adjudication and key-custody rules, canonical lock receipt, checksum mismatch policy, retry ceiling, and whether each failure voids, halts inconclusive, or is repairable without opening the analysis.

### 7. MINOR — §2.6 reads more complete than the slot table permits

**Sentences at issue.** “These fill the class-P inputs that six gate rounds said could not be closed by writing alone,” followed later by a table with only BS-2m marked filled. §2.6 also presents Branch-B geometry and exact power in the main narrative even though BS-1 is unresolved and BS-5p is explicitly unfillable.

**Why this fails as a promise.** The opening warning and §7 table are honest, but this sentence and the authoritative tone of §2.6 can be quoted to make the design look preregistered or power-cleared when eleven of twelve prerequisites remain open.

**Smallest sufficient repair.** Replace “fill” with “provide nonbinding measurements relevant to,” put a status banner at §2.6, and label every number as Branch-B-only, pre-freeze, and non-operative until its named receipt is filled and gated.

### 8. MINOR — the fixture transcript in §0 is named but not digest-pinned there

**Sentence at issue.** §0 gives full SHA-256 values for both Python files, then lists `ref/FIXTURES_V9_20260826.out` without a digest.

**Why this fails as a promise.** A future reader following only the definition section cannot tell which fixture transcript was frozen. The freeze record supplies `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`, and I independently reproduced it, but §0 does not carry it.

**Smallest sufficient repair.** Add that full digest to §0 and state whether the transcript is normative or merely validation evidence.

## Researcher-degrees-of-freedom inventory

### Closed by the present text/code

- Longo axis vector, sign convention, A = 0.0408 and σ_pub = 0.011.
- Eight catalog predicates, no surface-brightness cut, raw/retained distinction and retention factor.
- Greedy order, exact/swap/removal ordering, deterministic tie rules, N_eq floor, 1.2 planning margin.
- Primary permutation count, plus-one p, one-sided orientation, float tie comparison and decision thresholds.
- Calibration-bin tie rule, 3×9 allocation arithmetic, fixed 500-label budget and cell/stratum floors.
- Scalar/profile fork thresholds, calibration lower-bound floor and post-first-χ void rule in principle.

### Open or only deferred to an unfilled slot

- Release availability probe and resolution moment (Finding 3).
- Acceptance/exclusion/status derivation for every parent object (Finding 1).
- Exact production image input function and runner (BS-9, acknowledged open).
- Exact Stage-P mechanism that will produce BS-5p (Finding 5).
- Hand-check committee procedure, adjudication rules, sealed-key custody and future quoted HC rules.
- BS-8f “integrity triggers,” primary-lock definition and access custody (Findings 2 and 6).
- Transport anomaly/checksum/retry decisions at BS-6.
- Clean-room normative per-function specification and what constitutes a spec defect.
- All eleven unfilled class-P slots. They cease to be degrees of freedom only if their complete schemas and producer rules are frozen before any relevant data access; a slot name by itself is not closure.

## Artifact and arithmetic checks

Independently computed on the named files, without reading `/Users/duhokim/NebulaMindData/`:

- `successor_ref_v9.py`: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — matches §0/freeze.
- `closure_worker_v9.py`: `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959` — matches §0/freeze.
- `FIXTURES_V9_20260826.out`: `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5` — matches the freeze record.
- Exact Stage-P receipt: 6,445 bricks; n = 53,005; Var(c) = 0.7546638985; N_eq = 120002.8798; 995 successes; x≥962 PASS. These match the draft’s rounded values.
- The receipt has 1,000 trial p-values and settings of 20,000 permutations, a = 0.85 and p < 0.001. It identifies its subject as v7, not v9.
- 12,117 × 12.2 MB = 147.8274 decimal GB; 12,117 / 6,445 = 1.880062. The ≈148 GB and 1.880× statements are correct.
- The one-sided 95% Clopper–Pearson lower bound at x=962 of 1,000 is 0.950487, so the frozen integer threshold is correct.
- The draft’s final corrected geometry numbers agree with the correction chain in `REAL_GEOMETRY_RESULT_20260825.md`; I did not treat its superseded 6,446/~77 GB/997 figures as current.

## Null-result scope

The boundary in §1 is a genuine positive: it says this does not test A≈0.02, Shamir, BHU, or whether the sky is isotropic. The result label `REJECTED-AT-LONGO-AMPLITUDE` is also narrower than “isotropic.” Add the same limitation immediately beside the §5 outcome table and in the BS-V results template: rejection does not prove isotropy, exclude smaller amplitudes, or adjudicate other axes/authors. That is a clarification, not a new blocking defect.

## Failed attacks / positive evidence

- I found no drift in the two §0 code digests or the final geometry/power numbers.
- The 12,117-brick download correction and the exact 995/1000 retraction chain are stated candidly and reconcile arithmetically.
- The power threshold is not fit to the observed χ; it is fixed at A=0.0408, a=0.85 and x≥962. Geometry/count data determine the selected footprint, but the real handedness outcomes do not enter the stated planning calculation.
- The main scalar/profile calibration fork and all numerical boundaries are deterministic once the sealed calibration receipt is valid.
- A true numerical null can produce `REJECTED-AT-LONGO-AMPLITUDE`; the promise is not literally able to absorb every outcome. Finding 4 is that its non-reproduction boundary is incomplete and unnamed, not that rejection is impossible.

## Testimony

- The geometry record states that no χ was read during redesign and no image fetch was needed. I verified the statement exists; I did not independently audit file-access logs or operator conduct.
- The freeze and KIMI report state that only one referee seat cleared v9 and two provider seats were refused. I verified those documents and their on-disk report digest relationship, not the providers’ refusal events.
- The selection’s missing producer receipt, the exact harness’s lack of referee acceptance, and eleven unfilled prerequisite slots are admissions in the supplied artifacts; no independent upstream re-query was performed.

Blocking findings: F1 (unfrozen accepted sample), F2 (access-permitting blinding), F3 (Branch-A contradiction), and F5 (Stage-P mechanism/evidence mismatch).

**NOT CLEAR**
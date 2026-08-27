# PREREGISTRATION-TEXT REFEREE — GPT56

## Verdict

**NOT CLEAR.** The document contains a genuinely falsifiable four-region decision rule, fixes the target amplitude, sign, axis, cuts, estimator, thresholds, tie handling, calibration fallback and void rule, and is unusually candid about several unfinished mechanisms. But it does not yet bind who may see either predecessor or successor handedness before the primary lock; it has no rule that determines which completed parent measurements become “accepted” analysis rows; and it currently names two different Stage-P tests, only one of which is in the normative code. Those are blocking defects in the promise itself, not requests for nicer prose. Blocking findings: F1, F2 and F3.

## Numbered findings

### F1 — BLOCKER — §6's “blinding” clause forbids disclosure, not access

**Section / sentence.** §6: “Nothing derived from any real χ value — value, sign, summary, or count of signs — is published, spoken, or written outside the sealed results store before the primary lock.” §0 also says the predecessor's “208,405 sealed χ measurements are archived as successor input.”

**Why it fails as a promise.** A researcher can comply with every word while opening, querying, viewing or computing inside the sealed results store, provided nothing is moved or communicated outside it. The clause does not prohibit access by people who can revise the draft, choose or fill prerequisite producers, adjudicate failures, construct the accepted mask, or operate the primary lock. It does not bind the archived predecessor χ at all beyond calling them sealed, and it does not say that the redesign team remained unable to read them. Nor does it require an access log, key-custody record, failed-access log or attestation whose absence would expose a breach. “Not published” is an embargo; it is not blinding.

This matters even though the void rule closes post-first-real-χ changes: a person can see predecessor χ before the successor's first χ read, or see successor χ inside the store without changing a binding rule, and no stated condition voids or even records that event.

**Smallest sufficient repair.** Add a role- and event-specific no-access covenant covering both archived predecessor χ and successor χ: until BS-5f, unblinding and the primary lock occur in the fixed order, no person or process able to alter/fill/adjudicate the design may decrypt, query, render, summarize or inspect any χ-bearing object or derivative. Name the key holders and permitted blind automation; require append-only access/decryption/query logs and a pre-lock audit receipt; define any unauthorized access attempt or success as a void, whether or not anything was disclosed externally. State exactly what evidence establishes that the geometry redesign occurred without outcome access.

### F2 — BLOCKER — no rule determines acceptance or exclusion from the analysis mask

**Section / sentence.** §3 defines the estimand “under unit weight per accepted object.” §4 says Stage C uses the “sealed accepted-position mask” carrying an acceptance flag. §3 says `SealedMask` “refuses any non-accepted row.” §5's completeness guard requires only that “every parent object has a measurement receipt.” BS-2f then asks Hwao for the sealed accepted-position mask.

**Why it fails as a promise.** The parent has 65,060 objects, but the text never states the rule that maps 65,060 completed measurement receipts to accepted versus excluded rows. A receipt for every object does not close that gap: every object can have a receipt while an outcome-sensitive subset alone is marked accepted. The normative code validates that all rows supplied to `SealedMask` have `accept=1`; it does not derive acceptance from the parent, enforce a parent-to-mask accounting identity, or define failure/abstention/quality-cut reasons. Thus the sample size, geometry, calibration bins, Stage-C power and final slope can all change through an unbound exclusion choice after image inference. This is a direct researcher degree of freedom over the answer.

**Smallest sufficient repair.** Before any image byte, define a deterministic acceptance/failure/abstention rule from named instrument outputs and thresholds; enumerate every permitted exclusion reason and tie/non-finite case; prohibit sign-, amplitude- and sky-outcome-informed exclusions; and require a canonical parent-to-mask receipt accounting for all 65,060 object IDs exactly once as accepted or excluded with a machine-verifiable reason. BS-2f must be produced from that receipt by pinned code, with counts and digests for both accepted and excluded rows. `require_complete_sample()` must verify this partition, not merely compare two supplied integers.

### F3 — BLOCKER — §4 promises the shared-null Stage P while §2.6 relies on a different exact Stage P

**Section / sentence.** §4 defines Stage P as one 20,000-permutation standardized reference null per prefix, 1% deflation, sampled own-null checks and full checks for a boundary/sample subset. §2.6 instead reports “995/1000 ... with every trial judged against its own 20,000-permutation null” and says that exact method is “not yet in the definitional code.” §10 concedes BS-5p cannot be filled until it is. §0 says the v9 code bytes define every mechanism and code wins over prose.

**Why it fails as a promise.** These are different success definitions. Under the currently pinned v9 bytes, `stage_power()` counts shared-null calibrated successes and audits only a subset; the exact receipt counts 1,000 separately calibrated p-values. The artifact itself records its subject as `successor_ref_v7.py`, not the v9 subject §0 defines. The exact result is appropriately labelled measured rather than accepted, but §4 still states the superseded shared-null route as the preregistered mechanism. Filling BS-5p is therefore not mechanical receipt filling: it requires choosing a different test, changing the normative code bytes, and reconciling §4. A later operator can currently point to §0/§4 for one rule or §2.6/§10 for another.

**Smallest sufficient repair.** Choose one Stage-P test before freeze. If the exact per-trial route is intended, implement it in the code pinned by §0, pin its permutation count, plus-one rule, random addresses, serialization and failure behavior, add fixtures, gate it, update §4 to remove the shared-null/deflation/subsample contract, and rerun/receipt BS-5p and the final selected-set re-pass under those exact bytes. Do not fill BS-5p from the existing v7 measurement receipt unless equivalence to the newly pinned producer is mechanically established.

### F4 — MAJOR — the negative-result meaning is not stated strongly enough

**Section / sentence.** §1 says: “This tests that published amplitude at that published axis. It does not test A ≈ 0.02, Shamir, BHU, or whether the sky is isotropic.” §5 names `REJECTED-AT-LONGO-AMPLITUDE`, `INCONCLUSIVE`, and the two pre-run inconclusive outcomes, but gives no interpretation paragraph.

**Why it fails as a promise.** The computational regions are unambiguous: `REPRODUCED-LONGO` requires all four conjuncts; `REJECTED-AT-LONGO-AMPLITUDE` requires both rejection conjuncts; every other numeric result is inconclusive. That makes the claim capable of failing. But the scientific meaning is left to the outcome label and one example amplitude. The text does not explicitly say that rejection is conditional on this release, footprint, accepted-object rule, instrument/calibration model and fixed axis; that it does not exclude any smaller nonzero amplitude; that either inconclusive outcome establishes no presence or absence; or that it does not adjudicate other researchers' separately defined claims. A later summary can therefore overread “REJECTED” while quoting the registered outcome verbatim.

**Smallest sufficient repair.** Add a binding results-interpretation paragraph: rejection means only that the preregistered rule rejected a +0.0408 signal at this fixed axis under the named measurement/acceptance/calibration assumptions; it neither proves isotropy nor excludes smaller amplitudes or other axes/claims. State that all `INCONCLUSIVE*` outcomes support neither reproduction nor rejection. Apply the same scope to the reproduction label.

### F5 — MAJOR — the release fork is deterministic only after an undefined epistemic event

**Section / sentence.** §2.1: Branch A is selected iff DR11 photo-z “exists and is publicly retrievable at the resolution moment”; BS-1 is filled on the earlier of the day availability “is confirmed” or 2026-09-05.

**Why it fails as a promise.** The date fallback and two branches are explicit, but “confirmed available” and “publicly retrievable” have no frozen probe, endpoint set, retry/error policy, timestamp convention or responsible witness. Before September 5, avoiding or delaying a check delays the “earlier” event; transient authentication, mirror or network failure can turn existence into apparent absence. A person can thus influence the branch while satisfying the wording. This is more discretion than the disclosed fact that the fork remains open.

**Smallest sufficient repair.** Freeze the availability probe and schedule, authoritative URLs/products, required schema/version checks, retry window, treatment of partial service and transient errors, timestamp/time zone, and signed raw response receipt. Define whether uncertainty before September 5 remains unresolved rather than selecting Branch B. Make BS-1 a pure function of that receipt.

### F6 — MAJOR — prerequisite slots still contain rule-making, not merely value filling

**Section / sentence.** The preamble says the text becomes a preregistration when every class-P slot holds. BS-9 is still to supply the production input function/tensor layout and rerun R1–R5; BS-8p is still to supply “HC-1H rules by quotation + measurement plan”; §10 says the clean-room normative specification is unfinished. §2.6 nevertheless says the measurements “fill the class-P inputs that six gate rounds said could not be closed by writing alone.”

**Why it fails as a promise.** Eleven empty slots are disclosed, so the draft does not falsely claim to be frozen. But several empty class-P entries are not missing measured constants under already complete schemas; they are missing answer-determining rules and implementations. Filling them can determine image tensors, instrument behavior, calibration sampling/validity and blind-double comparability. Calling later insertion “slot filling” risks treating substantive design choices as clerical completion, and §2.6's “fill the class-P inputs” sentence reads more finished than the table and §10 permit.

**Smallest sufficient repair.** Distinguish `VALUE-ONLY` slots from `DESIGN/IMPLEMENTATION` slots. Require every design/implementation slot to trigger a new text/code revision and fresh text gate before freeze, not merely a receipt insertion. Replace §2.6's sentence with “provide measured candidate values for still-unfilled class-P slots” and show a 1/12 completion count near the front and table.

### F7 — MINOR — the receipt contradicts the quoted count of p-values at the resolution floor

**Section / sentence.** §2.6 says “995 of the 1,000 own p-values also sit at `5.00e-05`, the resolution floor.” `REAL_GEOMETRY_RESULT_20260825.md` repeats the same figure.

**Why it fails as a promise.** I parsed `STAGEP_EXACT_RECEIPT_20260826.json`. It contains exactly 1,000 trial p-values and 995 values below 0.001, matching the reported success count, but only **951** equal `1/20001 = 4.999750012499375e-05`. The other 44 successes are above the floor but below 0.001. The censoring explanation is sound for the 951 floor values; the stated count is stale.

**Smallest sufficient repair.** Change both quoted floor counts from 995 to 951, or generate the sentence mechanically from the receipt. Keep 995/1000 as the success count.

## Researcher-degrees-of-freedom ledger

### Closed by the present text/code

1. Target claim, oriented sign, amplitude and fixed axis.
2. Eight catalog cuts and the explicit absence of a surface-brightness cut.
3. Retention factor, raw-versus-retained roles, count ordering, exact/heuristic boundary, leverage floor, 20% planning margin and local selection order, subject to the unresolved Stage-P producer in F3.
4. Production permutation count, one-sided plus-one p-value, exact-float tie comparison and non-finite refusal.
5. Numeric decision regions, including strict inequalities at p = 0.001 and p = 0.05, sign, band and detection floor.
6. Calibration-bin construction/tie rule, allocation tie rule/floors, scalar/profile threshold and calibration halt, subject to the missing HC-1H rule package in F6.
7. Post-first-real-χ changes to any binding rule/code/threshold void the run.

### Open or not yet mechanically closed

1. DR11 availability adjudication (F5).
2. Accepted/excluded-object determination and failure handling (F2).
3. Exact Stage-P producer versus shared-null `stage_power()` (F3).
4. Production image input function/tensor path and R1–R5 evidence (BS-9; F6).
5. HC-1H committee, sealed-key and validity rules to be inserted by quotation (BS-8p; F6).
6. Clean-room normative specification and BS-V primary-lock implementation (disclosed in §10).
7. Access authority and audit evidence for both predecessor and successor χ (F1).
8. The already-disclosed release branch itself until its bound resolution date.

## Circularity review

I found no outcome-circular numeric boundary in §5: the constants and formulas are fixed, and calibration quantities are named pre-unblinding inputs rather than chosen after seeing β̂. Stage C's use of the realized accepted-position geometry and pre-unblinding calibration is adaptive but temporally specified. Stage P does search prefixes using addressed simulations and then applies a fixed 20% margin/re-pass, so the threshold is simulation-derived rather than an independent constant; that is not hidden, but F3 must first make the simulation success definition singular. The unbound acceptance step in F2 is the route by which outcome-related discretion can enter the geometry and thresholds.

## Artifact and number checks

- Recomputed SHA-256 matches §0/freeze for `successor_ref_v9.py` (`6a9abbbd…`), `closure_worker_v9.py` (`28f8e1f9…`) and `FIXTURES_V9_20260826.out` (`fab32ba2…`). The KIMI report hash matches the freeze record (`f2ee062b…`).
- The code constants match the text: `A_LONGO=0.0408`, published sign `-0.0408`, `N_PERM=100000`, `CP_PASS_X=962`, p thresholds 0.001/0.05, floor accuracy 0.85, retention 0.8572, detection multiplier 3.09 and `NEQ_MIN=100000`.
- Independently recomputed one-sided 95% Clopper–Pearson lower bounds: 961 successes gives 0.9493659932 and 962 gives 0.9504871297, so the integer boundary is correct.
- The exact receipt matches §2.6 for 6,445 bricks, n=53,005, Var(c)=0.7546638985, N_eq=120002.8798 and 995/1000 successes; `3*n*Var(c)` reproduces its N_eq. F7 is the one mismatch found in those quoted values.
- Closure arithmetic is consistent: 12,117 / 6,445 = 1.880062, and 12,117 × 12.2 MB = 147.8274 decimal GB, supporting ≈148 GB.
- The geometry receipt's correction chain ends at the values quoted in the draft: 6,445 bricks, 65,060 raw, 53,005 retained, Var(c)=0.754664, N_eq≈120,003, and exact Stage P 995/1000. Earlier 6,446/65,062/~77 GB, 997/1000 and shared-null FAIL are explicitly retracted or superseded rather than silently overwritten.

## Failed attacks / positive evidence

- I could not make the decision rule absorb every numeric outcome: there are explicit reproduction, rejection and inconclusive regions, and boundary equalities fall into inconclusive.
- I found no prose/code mismatch in the final decision inequalities or constants.
- I found no hidden claim of selector global optimality at production scale; the text expressly declines it.
- I found no claim that the eleven unfilled prerequisite slots are already filled; the table marks only BS-2m filled, though F6 identifies wording that overstates what the measured inputs accomplish.
- I found no attempt to erase the one-seat limitation, power retraction or unrefereed exact measurement; each is disclosed.

## Testimony

The source artifacts state that the redesign used already acquired geometry only, no image was fetched, no χ was read, the predecessor χ are sealed, and the exact Stage-P harness took 431 seconds. I verified the records and their internal arithmetic but, as instructed, did not read `/Users/duhokim/NebulaMindData/`, inspect live stores/processes, or independently establish those conduct/history claims. They remain testimony. The closure freeze's “one seat; two provider refusals” history is likewise reported by the named artifacts, not independently reconstructed here.

**NOT CLEAR**

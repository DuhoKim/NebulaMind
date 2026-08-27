# PREREGISTRATION-TEXT REFEREE — CODEX — V11

## Verdict

V11 is still not a promise that can be frozen. The Branch-A repair and the three highlighted receipt corrections hold, but four blocking seams remain. First, §6.1 still permits a named key holder outside the listed design roles to inspect χ before the lock and defines an impossible event order. Second, the header still calls the predecessor χ “successor input” while §6.2 says they are not input. Third, §2.7 recomputes acceptance from operator-authored terminal labels but never requires the code to recompute whether each exclusion reason is true. Fourth, §2.6 declares the exact per-trial Stage-P route while the still-operative §0/§4 definition and its named code symbols implement the shared-null route.

## Repair-round disposition

| V10 finding/claim | V11 disposition |
|---|---|
| KIMI F1 / GPT56 F1 / CODEX 2: disclosure is not blinding | **Not closed** — F1 below |
| KIMI F2: predecessor χ role | **Not closed** — F2 below |
| GPT56 F2 / CODEX 1: accepted-sample freedom | **Partly closed** — the partition and closed reason list are real improvements, but reason truth remains caller-controlled (F3) |
| GPT56 F3 / CODEX 5: two Stage-P tests | **Partly closed in stated intent, not in the operative promise** — F4 |
| CODEX 3: Branch A carried the Branch-B pin | **Closed** — Branch A now voids the current pin and requires remeasurement, repinning and a fresh text gate |
| KIMI F3: stale planner digest | **Closed** — `1617af00eb73…` matches v9 |
| 995 versus 951 p-values at the floor | **Closed** — receipt parses to 951 floor values and 995 successes |
| 2 of 7 versus 2 of 12 audited successes | **Closed** — fixture says 12 audited, 10 confirmed, 2 refuted |
| Value versus design slots | **Closed as a disclosure** — BS-2f, BS-5p, BS-8p and BS-9 are now explicitly DESIGN slots requiring revision and a fresh text gate |

## Numbered findings

### 1. BLOCKING — §6.1 is still an embargo for permitted key holders, and its event order contradicts itself

**Section / sentence at issue.** §6.1(2): “Only named key holders” may hold read access, followed by a prohibition applying only to a person or process able to alter the text, fill/adjudicate a class-P slot, construct the mask, or operate the lock. The prohibition lasts “until the lock, unblinding and BS-5f have occurred in that fixed order.” §6.1(1), however, defines the primary lock as a moment at which the BS-5f receipt already exists. §4 also puts BS-5f before unblinding.

**Why it fails as a promise.** A named key holder who is not in one of the enumerated design/lock roles may decrypt, query, render or inspect χ inside the sealed store before the primary lock while complying with every word. §6.1(4) voids only “unauthorised” access, so this permitted pre-lock read does not void the run. The old checkable sentence, “no χ-derived artifact exists outside the sealed store,” still tests export rather than knowledge: a person can look and leave no artifact outside.

The event order is also impossible as written. §6.1(1) requires BS-5f before the lock, but §6.1(2) names lock → unblinding → BS-5f as the fixed order. A future operator cannot infer one binding order from both sentences.

The log does not close either seam. A digest at BS-2f and BS-V proves only the bytes presented at those moments; the text does not place the log under an external writer/witness or require all decryption to be technically mediated by it. A permitted key holder’s in-store read is not a violation under the present wording even if faithfully logged.

**Smallest sufficient repair.** State that before unblinding **no human, including every named key holder, may inspect any χ-bearing object or derivative**; keys may be held but not used except by named blind automation whose output is schema-restricted. Make every successful pre-unblinding human read void the run regardless of whether the reader was an authorised key holder. State one order everywhere: BS-5f → primary lock → Duho-authorised unblinding → human inspection. Put the access log under an independent append-only witness or cryptographic mediation and make a missing/gapped log a void.

### 2. BLOCKING — the predecessor χ are simultaneously “successor input” and “not an input”

**Section / sentences at issue.** Header line 22: the predecessor sample and “208,405 sealed χ measurements are archived as successor input.” §6.2: “No predecessor χ measurement enters this run’s analysis,” “Every χ this study uses is measured fresh,” and the archive “is not an input.”

**Why it fails as a promise.** These are opposite descriptions of the same archived measurements. §6.2 supplies the intended rule, but §0’s own precedence sentence says conflicting prose is a defect; it does not authorize a future reader to discard the header. Someone wishing to reuse predecessor values can point to “successor input,” while someone wishing to forbid reuse can point to §6.2. This is exactly the ambiguity V11 says it repaired.

**Smallest sufficient repair.** Replace the header phrase with “archived as historical record only; the 208,405 χ measurements are not successor inputs and may not enter selection, calibration, power, estimation or verdict production.” Keep the two-object 208,407-parent versus 208,405-measurement distinction explicit.

### 3. BLOCKING — §2.7 closes the reason vocabulary but not the truth of a reason

**Section / sentences at issue.** §2.7(4): the append-only ledger carries one terminal status and one “machine-checkable reason” per object, and `run_production_verdict()` must “recompute the accepted set from that ledger.” §2.7 does not say that the production code recomputes each exclusion predicate from immutable cutout-integrity and instrument records. The current v9 code still accepts supplied mask flags and `require_complete_sample()` still compares only two integers (`successor_ref_v9.py:1591–1599, 1647–1649`), which the draft candidly marks as unimplemented.

**Why it fails as a promise.** Recomputing `accepted = rows whose status is ACCEPTED` merely replays an operator’s labels. A conforming operator can give an unwanted object `EXCLUDED / confidence below threshold`, give a wanted object `ACCEPTED`, and satisfy the partition, the closed reason vocabulary and both set digests. Calling a reason “machine-checkable” does not say who checks it, from which pinned fields, or that a false reason is refused. This still moves signs and geometry after inference.

Reason (d) is especially outcome-adjacent: confidence is an instrument output. The text freezes its threshold and forbids conditioning on sign, but it does not define the confidence field/function or require recomputation from a sign-blind channel. Likewise, “absent output” can be asserted unless the ledger is joined against an independently fixed attempt/receipt record.

**Smallest sufficient repair.** Make one pinned producer compute both status and reason directly from immutable evidence: parent ID, expected cutout checksum/shape, actual checksum/shape, instrument execution receipt, finite-output flag and the frozen confidence field/threshold. Require `run_production_verdict()` (or a mandatory pre-verdict validator it calls) to recompute every predicate and refuse any status/reason/evidence mismatch. Define the confidence quantity and demonstrate that the exclusion path cannot read sign, amplitude or axis-relative position. Bind the ledger to the parent and per-object evidence digests, not only to its own accepted/excluded set digests.

### 4. BLOCKING — Stage P has a single stated preference but two operative definitions

**Sections / sentences at issue.** §2.6 says, emphatically, “This text promises the EXACT per-trial test” and calls §4’s shared-null contract superseded. §4 nevertheless remains the section titled “Power gate,” speaks in present normative language (“Stage P therefore measures”), defines one shared reference null, 1% deflation and sampled own-null checks, and names `stage_power()` as the class-P mechanism. §7’s BS-5p row still names `stage_power`, `build_plan`. §0 says the current v9 code defines every mechanism and code wins over prose.

**Why it fails as a promise.** The intent is now clear, but the promise is not internally single-valued. A reader following §0, §4 and §7 must execute the shared-null v9 `stage_power()`; a reader following the supersession paragraph must execute a not-yet-implemented exact method. `build_plan()` currently calls the shared-null function during both prefix search and the final-set re-pass (`successor_ref_v9.py:1319–1342`). The exact receipt names v7 and a separate harness. V11 correctly calls BS-5p a DESIGN slot requiring another revision, which is an honest admission that V11 itself cannot be frozen merely by inserting a receipt.

**Smallest sufficient repair.** Remove the shared-null contract from the normative §4 (move it to a clearly historical appendix if retention matters) and replace it with the full exact contract: one 20,000-permutation own null per trial, plus-one p, exact tie rule, trial addresses, serialization, failure behavior and resource bounds. Update §7 to name the exact producer. Then implement that same contract in the §0-pinned bytes and rerun the prefix search and final-set re-pass before a fresh text gate.

### 5. MAJOR — the quoted four-geometry z* range is still contradicted by the pinned fixture

**Section / sentence at issue.** §4: “across four geometries the measured z* ranged 3.0376–3.1355, bracketing the normal 3.0902.” The same stale range is in `successor_ref_v9.py:1163–1167`.

**Why it fails as a promise.** `FIXTURES_V9_20260826.out` prints 3.0694, 3.0010, 3.0020 and 3.0260: range **3.0010–3.0694**, all below 3.0902. The fixture’s `PWR-Z-STABLE` line separately gives tail masses at z=3.0902 of 0.00135, 0.00130, 0.00100 and 0.00110; those values support the narrower claim that a fixed normal threshold is unsafe, but they do not make the quoted quantile range true. This was KIMI V10 F6 and V11 did not repair it.

**Smallest sufficient repair.** Quote the fixture’s actual range and tail masses, and repair the stale code docstring in the same gated code revision already required for exact Stage P.

### 6. MAJOR — “not reproduced” still excludes clear wrong-sign and wrong-amplitude results

**Section / sentences at issue.** §5 calls only the narrow null-shaped region `p > 0.05 AND |Â_L| + 3σ_ours < 0.0408` “REJECTED-AT-LONGO-AMPLITUDE.” Every other numeric result is `INCONCLUSIVE`. `BATTERY-SIGN` requires only that −0.0408 is never called reproduced.

**Why it fails as a promise.** The study claims to test a specific oriented sign and amplitude. A precise opposite-sign estimate near −0.0408 or a precise same-sign estimate whose interval excludes +0.0408 can be decisive evidence that the specific claim was not reproduced, yet the registered vocabulary calls both inconclusive. The promise can fail — a near-zero result can reach REJECTED — so it is not infinitely absorptive. But it does not give an unambiguous “not reproduced” interpretation for all outcomes that contradict the target. `REPRODUCED-LONGO` also means compatibility within a combined 3σ band, not literal recovery of 0.0408; the label does not say that.

**Smallest sufficient repair.** Add a scientific interpretation table separate from execution-status labels. Define “specific claim reproduced,” “specific claim not reproduced,” and “unresolved” for wrong-sign and target-excluding intervals. If the four machine labels are intentionally retained, explicitly state that `INCONCLUSIVE` is an operational label and may include strong evidence for a different/opposite signal. Rename reproduction as Longo-compatible if 3σ compatibility is the intended claim.

### 7. MINOR — null-result limits remain implicit rather than bound to the outcome

**Section / sentence at issue.** §1 says the study does not test A≈0.02, Shamir, BHU or isotropy. §5 gives no result-interpretation paragraph.

**Why it fails as a promise.** The scope boundary is directionally correct, but a future result summary can quote `REJECTED-AT-LONGO-AMPLITUDE` without carrying §1. The preregistration never says next to that outcome that rejection does not prove isotropy, does not exclude smaller amplitudes and does not settle separate claims/axes. It also never says all `INCONCLUSIVE*` outcomes support neither reproduction nor rejection.

**Smallest sufficient repair.** Put those limits immediately below §5’s outcome table and require BS-V’s public result record to reproduce them.

### 8. MINOR — the draft still overstates completion and omits a public prior-existence witness

**Sections / sentences at issue.** §2.6: “These fill the class-P inputs…”; §7: only one of twelve class-P slots is filled and four are DESIGN slots. §6 Custody says artifacts are committed to git and witnessed by lane gates, but names no public deposit or independent timestamp.

**Why it fails as a promise.** The first sentence can be quoted as power/geometry clearance although V11 itself says BS-5p cannot be filled and 11/12 prerequisites remain empty. A preregistration also needs provable prior existence; a private git history and participant-run gate reports do not establish an external date.

**Smallest sufficient repair.** Replace “fill” with “provide nonbinding Branch-B measurements relevant to,” keep the 1/12 status next to §2.6, and name the public archive or independent timestamp whose identifier and frozen digest BS-V must carry.

## Researcher-degrees-of-freedom inventory

### Closed by the current text/code

- Target paper, +0.0408 mapped sign, published −0.0408 sign, σ_pub, fixed axis and fixed-axis scope.
- Eight catalog cuts, explicit absence of a surface-brightness cut, retention factor, raw/retained roles.
- Greedy order and deterministic tie handling, exact small-universe rule, local swap/removal ordering, N_eq floor and 1.2 margin as definitions.
- Production permutation count, one-sided plus-one p, exact-≥ ties, strict p boundaries and non-finite refusal.
- Calibration-bin tie rule, allocation tie rule/floors, scalar/profile fork and calibration halt, subject to the still-unfilled BS-8p design.
- Branch A no longer inherits the Branch-B §0 pin; selecting A forces remeasurement, repinning and a fresh text gate.
- Post-first-real-χ edits to binding rules void the run.

### Open, deferred or not closed against post-data choice

- Truth-production and verification for every ACCEPTED/EXCLUDED reason (F3).
- Human/key-holder access and the exact BS-5f/lock/unblinding order (F1).
- Exact Stage-P implementation and complete contract (F4).
- DR11 availability probe, schedule, endpoint, retry/error treatment and witness; the fork remains bound only at a high level.
- BS-9 production image input function and runner.
- BS-8p committee/measurement-plan/quoted HC rules.
- BS-3’s confidence quantity as used by §2.7(d), not merely its threshold.
- BS-6 transport anomaly/checksum/retry disposition.
- Clean-room per-function normative specification.
- All eleven unfilled class-P slots; the four DESIGN slots require a new revision and gate, not a clerical fill.

## Circularity and falsifiability

I found no hidden outcome-derived numeric threshold in §4/§5. Stage-P synthetic power uses a frozen amplitude and accuracy floor on count-derived geometry; Stage C uses the accepted-position mask and pre-unblinding calibration lower bounds. The principal outcome-entry path is not a circular formula but F3’s unverified post-inference exclusion labels.

The promise can fail: the `REJECTED-AT-LONGO-AMPLITUDE` region is reachable, strict boundary equalities fall into `INCONCLUSIVE`, and the numerical outcome space is partitioned. F6 is narrower but material: the interpretation “specific sign-and-amplitude claim was not reproduced” does not cover all target-incompatible outcomes.

## Artifact and arithmetic checks

Independently checked without reading `/Users/duhokim/NebulaMindData/`:

- `successor_ref_v9.py`: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — matches §0/freeze.
- `closure_worker_v9.py`: `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959` — matches §0/freeze.
- `FIXTURES_V9_20260826.out`: `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5` — matches freeze; §0 still omits this digest.
- `CLOSURE_V9_KIMI.md`: `f2ee062bb7f1ced33e5530d6655765f32b5830342154274ecf885c73dc722f01` — matches freeze.
- `stagep_exact.py`: `daed15c7d3933abf70ac50565c1e8b4c590be883d9590ef9ca776ddc4593ca7f` — matches receipt.
- Exact-receipt inputs: oracle `01b8b4ec…103a` and selection `b913939d…804e` — match the NPZ files.
- Exact receipt contains 1,000 p-values; 995 are below 0.001; 951 equal 1/20001 = 4.999750012499375e-05. Geometry is 6,445 bricks, n=53,005, Var(c)=0.7546638985 and N_eq=120002.8798.
- `3 × 53,005 × 0.7546638984846564 = 120002.87981753764`.
- 12,117 × 12.2 MB = 147.8274 decimal GB; 12,117 / 6,445 = 1.880062.
- One-sided 95% Clopper–Pearson lower bound: x=961 gives 0.9493659932 and x=962 gives 0.9504871297, so x≥962 is correct.
- Fixture Stage-P audit is 12 trials / 10 confirmed / 2 refuted. Fixture z* values are 3.0694, 3.0010, 3.0020 and 3.0260, contradicting §4’s retained 3.0376–3.1355 claim.

## Failed attacks / positive evidence

- No drift found in the two §0 code digests, closure report digest, exact-harness digest or exact receipt input hashes.
- The planner digest, floor-p-value count and boundary-audit denominator repairs are exact.
- The final geometry and exact power numbers reconcile with the correction chain; the earlier 6,446/65,062, 997/1000 and shared-null FAIL are not silently presented as current.
- Branch A is no longer allowed to carry the Branch-B pins.
- The text now honestly labels answer-determining unfinished work as DESIGN work requiring a revision and fresh gate.
- No circular use of real χ in the stated geometry/power thresholds was found.

## Testimony

- The geometry record states that no χ was read during redesign, no image byte was fetched and no new catalog fetch was needed. I verified those statements exist; I did not verify operator conduct or external access logs.
- The freeze and KIMI report say the closure mechanism received one referee seat and two provider refusals. I verified the documents and digest relationship, not the provider events.
- The selection still lacks a producer receipt; the exact Stage-P measurement remains unrefereed; eleven prerequisite slots remain unfilled. These are admissions in the supplied artifacts, not independently reconstructed upstream histories.
- I did not inspect live stores, image data, downloaders, credentials or `/Users/duhokim/NebulaMindData/`.

Blocking findings: F1 (pre-lock key-holder access and contradictory order), F2 (predecessor χ both input and not input), F3 (operator-authored exclusion reasons are not recomputed), and F4 (exact versus shared-null Stage-P definitions).

**NOT CLEAR**
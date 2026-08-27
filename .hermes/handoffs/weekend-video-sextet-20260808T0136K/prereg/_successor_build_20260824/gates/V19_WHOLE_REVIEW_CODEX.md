# V19 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

V19 is **NOT CLEAR**. The dispatched bytes match, all three §10 repair-trace entries are now accurate against their mechanical diffs, the two registry namespaces remain disjoint, and the threshold/equality seams previously credited still hold. But the V18 registry blocker has been relocated rather than closed: §5 now names producers and says `run_production_verdict()` is narrowed to outcomes it “can actually return,” while the pinned function returns a different set, several claimed producers remain unimplemented, `VOID` still has no named producing phase/process, and the new non-finite split overlaps Row I’s allocated-output branch. Clause 10 therefore still fails at the executable producer boundary.

## Subject identity — verified before opening

- Subject: `../PREREG_SUCCESSOR_DRAFT_V19_20260827.md`.
- Brief-pinned SHA-256: `b7deb106eb81b3e13376e7049263b355ba90982656f7de30964c0d3bfda5e63b`.
- Independently computed before opening: `b7deb106eb81b3e13376e7049263b355ba90982656f7de30964c0d3bfda5e63b`.
- Result: **MATCH**. This report binds exactly that digest.
- Independent line count: **810**.
- Held predecessor digests recomputed: V16 `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`; V17 `1a0a259a91f5a73a80fc864148e5fb6b0a2014dbf2494d243484e3948c16fce5`; V18 `ce144dc23ba8605df1a3b7590464fc3de09c313a597168f91c80d4b29ab302f4`.
- §0 pins recomputed: `ref/successor_ref_v9.py` `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `ref/closure_worker_v9.py` `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.

## Numbered findings

### 1. HIGH / BLOCKING — the lifecycle registry’s new producer names still do not match executable capability

- **Section / lines:** §0 lines 73–104; §2.7 lines 345–375; §3 lines 388–396; §5 lines 458–475, especially 469–473; Row I line 529; Row J line 530; Row P line 536; Clause 10 line 566; §11 lines 804–810; pinned `ref/successor_ref_v9.py` lines 1351–1356, 1457–1496, 1500–1557, 1561–1625.
- **What the rename fixed:** The exactly-one assertion is now attached to the study-run lifecycle rather than to one function call. Numeric outcomes are correctly assigned to the numeric helper. Row I, Row J, and Row P are named at the prose-contract level. Per-attempt states remain separate, zero-or-more, and disjoint from run outcomes.
- **Failure A — the narrowed runner claim is factually inverted.** Line 473 says `run_production_verdict()` can actually return numeric verdicts, post-unblinding accounting refusals, post-unblinding calibration halts, and `VOID`. The pinned function at lines 1591–1625 can return the three numeric outcomes through `_decide_from()` and can directly return `INCONCLUSIVE-BY-POWER` at lines 1610–1616. It contains no accounting join or accounting-refusal return, no post-unblinding attrition validator, no `VOID` return, and no catch converting `InconclusiveByCalibration` into an emitted verdict. Its permutation failure is re-raised as `RuntimeError`. Thus line 473 both **omits an outcome the function really returns** (`INCONCLUSIVE-BY-POWER`) and **claims four families it cannot return**.
- **Failure B — the power producer is not exhaustive.** Line 469 names Row J as the producer of `INCONCLUSIVE-BY-POWER`; Row J does emit it for Stage-C failure at P5. But §5 lines 486–487 and the pinned runner lines 1610–1616 independently make the later production runner emit the same category for a supplied failed Stage-C receipt or `N_eq < 100,000`. The lifecycle category therefore has an omitted producer/phase, contrary to V19’s claim that the producing phase or process is named for each category.
- **Failure C — several newly named producers are promises, not capabilities.** The Row-J calibration guard is explicitly still required work in §11 line 806. The accounting/adequacy validator and associated schemas/verifiers are likewise unimplemented required work (§11 lines 804–810), and the pinned code contains none of the accounting or per-attempt tokens. Row I’s table branch mandates an abort but provides no implementation or emission mechanism for `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`; that token occurs only in the registry. A draft may honestly specify required work, but it cannot simultaneously say the pinned production runner “can actually return” the resulting categories under §0’s code-precedence rule.
- **Failure D — `VOID` still has no producing phase or process.** Line 471 lists triggers and candidly admits that permutation/statistic failures currently raise uncategorized exceptions. Unlike every other bullet, it names no Row, validator, helper, or phase that emits `VOID`. Forbidden acts can occur across Rows A–S; a trigger condition is not an emitter. Reverse reachability therefore stops at an abstract label, and forward execution reaches uncategorized exceptions rather than the registry member.
- **Failure E — the non-finite split is not disjoint by phase/cause.** Row I line 529 treats an allocated object’s missing **or non-finite** instrument output as the pre-BS-8f abort whose registry category is `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`. Line 469 also maps “calibration-input non-finite/degenerate failures” to `INCONCLUSIVE-BY-CALIBRATION`. The corresponding instrument outputs are inputs to Row I’s calibration computation, so the phrase does not exclude the Row-I case and supplies two run outcomes for the same non-finite antecedent. In pinned code, `accuracy_from_handcheck()`, `_finite()`, `w_profile()`, and sigma helpers raise uncategorized `RuntimeError`; only a finite `a_LB_b < 0.85` raises `InconclusiveByCalibration` in `adjudicate_path()`.
- **Why it fails:** The brief’s named attack is exactly whether a correct-sounding producer name covers unchanged capability. It does not. §0 says code is the definition and prose disagreement is the defect; Clause 10 requires every branch to terminate in one stated outcome. V19 now has textual names, but executable returns, prose phase ownership, and the claimed runner set disagree in both directions.
- **Smallest sufficient repair:** Replace line 473 with an exact present-tense inventory of the pinned function’s real returns (numeric outcomes plus its two power branches) and separately label accounting, post-unblinding calibration, Row-I, Row-J-calibration, per-attempt, and `VOID` emission as unresolved required implementation. In the lifecycle registry, list **all** actual/planned producers per category, including the production runner’s `N_eq`/Stage-C power guard. Name a fixed validator/process and phase for `VOID`, or state explicitly that the category is not yet executable. Define “calibration-input non-finite/degenerate” to exclude allocated per-object missing/non-finite outputs, or assign one precedence rule so Row I and calibration failure cannot both claim the same antecedent. No invented orchestration symbol is required; truthful capability labels and complete producer lists are sufficient.

## Lifecycle registry audit — every category and producer

| lifecycle category | named producer in V19 | can emit at that phase? | result |
|---|---|---|---|
| `REPRODUCED-LONGO` | numeric decision helper | `_decide_from()` assigns it under the strict p/sign/band/floor conjunction | **HOLDS** |
| `REJECTED-AT-LONGO-AMPLITUDE` | numeric decision helper | `_decide_from()` assigns it under strict `p > 0.05` and the amplitude exclusion band | **HOLDS** |
| numeric `INCONCLUSIVE` | numeric decision helper | `_decide_from()` residual branch assigns it | **HOLDS** |
| `INCONCLUSIVE-BY-POWER` | Row J | Row J’s P5 contract emits it, but the pinned production runner also returns it and is omitted as a producer | **INCOMPLETE / BLOCKING** |
| `INCONCLUSIVE-BY-CALIBRATION` | Row J; pre-verdict validator; calibration-input failures | Row J’s guard and the post-unblinding validator are required but unimplemented; pinned code raises rather than emits; the non-finite cause overlaps Row I | **NOT EXECUTABLY CLOSED / BLOCKING** |
| `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT` | Row I | Row I text mandates a P4 abort, but no emitter exists in pinned code and the non-finite half overlaps the calibration-input wording | **TEXTUALLY REACHABLE, NOT EXECUTABLY CLOSED** |
| `INCONCLUSIVE-BY-MISSING-RECORD` | Row P or pre-verdict validator | Row P’s ordered text branch emits it; no pinned implementation and no actual runner return | **PLANNED, NOT ACTUAL** |
| `INCONCLUSIVE-BY-DUPLICATE` | Row P or pre-verdict validator | Same | **PLANNED, NOT ACTUAL** |
| `INCONCLUSIVE-BY-ORPHAN` | Row P or pre-verdict validator | Same | **PLANNED, NOT ACTUAL** |
| `INCONCLUSIVE-BY-MALFORMED` | Row P or pre-verdict validator | Same | **PLANNED, NOT ACTUAL** |
| `VOID` | no producer named; triggers only | Pinned code has no `VOID` token/return and raises uncategorized exceptions | **NO PRODUCER / BLOCKING** |

Per-attempt registry: `EXCLUDED-BY-ABSENCE`, `EXCLUDED-BY-NONFINITE`, `EXCLUDED-BY-CONFIDENCE`, and `ACCEPTED-FINITE` remain mutually exclusive by Row P’s ordered classification and disjoint from the lifecycle labels. Any `EXCLUDED-BY-*` projects to one run-level calibration outcome in prose. None is implemented in the pinned code; V19 does not newly claim otherwise except indirectly through line 473’s false runner-capability sentence.

## Clause 10 audit across §§0–11, both directions

### Forward: branch → one category

- **Holds textually:** release A/B/date fallback; exact versus production selection; manifest equality/refusal; calibration `<0.85` before spread; scalar `<=0.03` versus profile `>0.03`; Stage-C 961/962 boundary and self-verification failure; Row-P accounting precedence; Row-P absence/non-finite/low-confidence/accepted-finite states; zero versus one-or-more post-unblinding removals; the three numeric decision regions.
- **Fails executably:** the production runner’s Stage-C/N_eq power returns are absent from the narrowed emitter inventory; Row-I, Row-J-calibration, accounting, attrition, and `VOID` paths are not implemented by the pinned definition; uncategorized exceptions do not emit a registry outcome.
- **Fails uniqueness as written:** an allocated non-finite instrument output satisfies Row I’s “missing/non-finite allocated output” branch and is not excluded from line 469’s “calibration-input non-finite” branch.

### Reverse: category → reachable antecedent and producer

- The numeric helper’s three outcomes have reachable and mutually exclusive antecedents.
- Power has reachable antecedents but an incomplete producer list.
- Row-I and Row-P labels have prose antecedents, but no executable producer in the pinned code.
- Calibration has prose antecedents but no single phase-cause partition and no emitted pinned-code mapping for the newly named failure causes.
- `VOID` has broad antecedents but no named producing process/phase and no executable emission.
- The per-attempt states have Row-P prose antecedents and remain disjoint, but their required implementation is still absent.

## Threshold sweep — value, phase, and failure effect

- **Calibration floor `0.85`: numeric rule holds.** `<0.85` is the pre-unblinding calibration halt; equality passes. This matches §3, §4, §6.3 and pinned `adjudicate_path()` lines 1492–1496. The Row-J emission guard itself remains unimplemented (§11).
- **Scalar/profile spread `0.03`: holds.** It is evaluated only after the calibration complement; `<=0.03` selects scalar and `>0.03` selects profile, not failure. Pinned line 1496 agrees.
- **Confidence threshold: intentionally unresolved and correctly seated in BS-2a.** It must be frozen before BS-6; below threshold produces per-attempt `EXCLUDED-BY-CONFIDENCE`, and any removal ends the run as calibration inconclusive. BS-2a remains refused, so no value is smuggled in.
- **Stage C:** exactly `N_TRIALS = 1,000`; 962 passes and 961 fails; `refuted` or `nonconservative` fails closed. The P5 failure effect is power inconclusive. Protocol/implementation deviation is assigned to `VOID`, but the producer of `VOID` remains unspecified.
- **Post-unblinding attrition:** zero removals may continue; any one or more removals emits calibration inconclusive; no Stage-C rerun.
- **Production/statistical thresholds:** 100,000 permutations; reproduction strict `p < 0.001`; rejection strict `p > 0.05`; equalities fall to numeric `INCONCLUSIVE`; target amplitude 0.0408; public sigma 0.011; three-sigma bands; detection multiplier 3.09. Pinned constants and `_decide_from()` lines 1577–1584 agree.
- **Planning thresholds:** retention 0.8572; `L_plan = 1.2 × L_min_plan`; `N_eq >= 100,000`; exact mode `<=16`. Values and boundary directions agree with pinned constants/code. Failure effects remain refusal/no plan or power inconclusive as stated.
- **Catalog cuts:** `brick_primary=1`, `maskbits=0`, non-PSF, `flux_r>0`, `0 <= z < 0.15`, ellipticity expression `<0.1836734693877551` / `b/a>0.4`, `dered_mag_r<17.7`, and `shape_r>1.5` are seated in §2.2 as pre-parent selection predicates; equality sides are explicit.
- **Other thresholds:** release fallback date 2026-09-05; Stage-P 10× confirmation band; hand-check floors `>=10` per non-empty cell and `>=30` per live inherited stratum, with infeasibility failing rather than shrinking. No new V19 mismatch found.
- **Threshold-related defect:** non-finite/degenerate “failure effect” is not uniquely phase-partitioned or executable; it is part of Finding 1.

## §10 trace verification — all three entries

### V16 → V17: **ACCURATE**

Mechanical comparison found 13 non-equal opcodes, 28 removed lines, and 61 added lines. The trace now covers the restored normative §6.3 bodies **and** Row P’s replacement of the superseded V15 citation; §4/Row-J calibration and pre-attrition additions; the §7 count repair; the §2.6 candidate-evidence narrowing; the §3 spread threshold; and all four partial states, including the historically false §10 “applied §4” claim that V17 left unrepaired.

### V17 → V18: **ACCURATE**

Mechanical comparison found 11 non-equal opcodes, 17 removed lines, and 37 added lines. The trace accounts for the §2.7 single authority/reason deletion; run/per-attempt split plus Row-I category; calibration-before-spread precedence; chronology repair; historical-claim removal; both trace entries; and the future-trace rule. “Blocker 4 & Repair 6” now matches the repair brief’s identifier.

### V18 → V19: **ACCURATE AS A CHANGE LOG, BUT THE CHANGED CLAIM IS FALSE**

Mechanical comparison found 6 non-equal opcodes, 13 removed lines, and 21 added lines. Beyond the version/provenance header, the trace accounts for the registry rename/producer wording/non-finite split/runner-claim edit and the three §10 trace corrections. The trace accurately says those edits were made; it does not establish that the resulting producer-capability assertion is true. Finding 1 independently falsifies that assertion.

## Adjacent breakage, overclaim, and failed attacks

1. Tried to recover a live second confidence-threshold owner: failed; BS-2a remains sole authority and Row P only applies it.
2. Tried to overlap run labels with `EXCLUDED-BY-*` / `ACCEPTED-FINITE`: failed; the namespaces remain disjoint by type and cardinality.
3. Tried low calibration plus high spread: failed; calibration still takes precedence.
4. Rechecked equality seams at `0.85`, `0.03`, 962/1,000, `p=0.001`, and `p=0.05`: intended sides still match pinned code.
5. Tried to falsify any of the three §10 trace entries against the actual diffs: failed; all substantive hunks are now represented.
6. Tried to find an invented orchestration symbol: failed; none was added.
7. The adjacent defect is instead the stronger present-tense capability sentence at line 473 and the non-finite overlap introduced by the V19 split.
8. Standing limitations remain prominently disclosed: Findings 1, 2, 2b and 3 unresolved; BS-2a refused; Rows C2/E blocked; BS-6 and first image byte blocked; exact Stage P not in definitional code; `verify_lock()`, unblinding schema/verifiers, Row-J guard, mediation, C2, ledger recomputation, and adequacy handling required but unimplemented.

## Testimony and limits

- The 21:48 instruction/initiation, historical measurements, source-citation verification, archive state, and prior multi-seat refusal/verdict chronology were not independently re-executed. They remain Testimony for this pass.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, inspect secrets, or touch χ-bearing material.
- Scientific provenance for inherited catalog cuts and historical measurements was not re-fetched; this pass tested internal phase/value/failure-effect consistency and the pinned code where available.
- Required future implementations were judged from their explicit unresolved status and absence from the pinned code, not assumed to exist.

## Evidence ledger and custody

Content read:

- `gates/BRIEF_V19_WHOLE_REVIEW.md` in full.
- Exact pinned V19 subject in full, only after digest verification.
- V18 CODEX and GPT56 whole-review reports in full.
- Complete mechanical V16→V17, V17→V18, and V18→V19 diffs.
- Pinned `ref/successor_ref_v9.py` constants, Stage-P/Stage-C returns, calibration, path adjudication, numeric decision helper, and production runner.

Independent checks:

- SHA-256 and line counts for V16, V17, V18, V19 and both §0 code pins.
- AST/static inventory of literal verdict returns and exception paths in `stage_power()`, `adjudicate_path()`, `_decide_from()`, and `run_production_verdict()`.
- Whole-document outcome-token inventory and pinned-code token comparison.
- Category-by-category producer/phase audit; Clause 10 forward and reverse audit against both registries.
- Whole-document threshold sweep and equality comparison to pinned constants/code.
- Programmatic diff opcode/added/removed counts for all three required trace transitions.

No source, code, reviewed draft, prior report, brief, or data artifact was modified. This required report is the sole write by CODEX.

**NOT CLEAR**
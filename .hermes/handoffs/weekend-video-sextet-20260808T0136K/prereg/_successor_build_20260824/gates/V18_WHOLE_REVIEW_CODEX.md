# V18 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

V18 is **NOT CLEAR**. The dispatched bytes match, the §2.7 authority repair and the §3 calibration-precedence repair hold, and the two registry namespaces are disjoint by type and cardinality. The added Row I abort is substantively necessary and has a reachable antecedent. But the run-level registry is still attributed to the wrong producer: §5 says `run_production_verdict()` emits every run-level outcome even though Row I's new pre-BS-8f abort and Row J's pre-unblinding halts terminate the run before that post-unblinding function can be invoked. The V16→V17 trace is also incomplete against the actual diff and the V16 findings, so the restored §6.3 trace obligation is not yet satisfied accurately.

## Subject identity — verified before opening

- Subject: `../PREREG_SUCCESSOR_DRAFT_V18_20260827.md`.
- Brief-pinned SHA-256: `ce144dc23ba8605df1a3b7590464fc3de09c313a597168f91c80d4b29ab302f4`.
- Independently computed before opening: `ce144dc23ba8605df1a3b7590464fc3de09c313a597168f91c80d4b29ab302f4`.
- Result: **MATCH**. This report binds exactly that digest.
- Independent line count: **802**.
- V17 and V16 predecessor digests independently recomputed as `1a0a259a91f5a73a80fc864148e5fb6b0a2014dbf2494d243484e3948c16fce5` and `1b9b9486736bf734c8cb4ac8cedf54870fd179587e3e1455273ec4724132a0da`, matching the V18 provenance and reviewed pins.

## Numbered findings

### 1. HIGH / BLOCKING — the cardinality split holds, but §5 still assigns pre-runner lifecycle outcomes to `run_production_verdict()`

- **Section / lines:** §5 lines 458–473, especially 466–470; Row I line 527; Row J line 528; Row P line 534; Clause 10 line 564.
- **Evidence:** Line 466 says **“`run_production_verdict()` emits exactly one run-level outcome”** and then includes `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`, `INCONCLUSIVE-BY-CALIBRATION`, and `INCONCLUSIVE-BY-POWER` in that set. Row I requires the missing/non-finite allocated-output abort **before BS-8f**. Row J emits calibration or power inconclusiveness at P5, before BS-L and unblinding. Row P and the production verdict path are P8/post-unblinding. The pinned `run_production_verdict()` at reference lines 1591–1625 has no Row-I path; it is reached only with a sealed mask, calibration record, authorization, complete-sample count and Stage-C receipt. It can return power inconclusive for a supplied failing Stage-C receipt or N_eq, but it cannot be the producer of a run already halted before BS-8f or before unblinding.
- **Why it fails:** The new Row I category has a valid lifecycle antecedent, but no reachable antecedent **through the producer to which §5 assigns the complete run-level registry**. The repair correctly separates run outcomes from repeatable attempt states, yet “exactly one” remains attached to a function that is deliberately never called on several listed terminal branches. Clause 10 therefore fails in reverse at the producer boundary, and the present-tense emitter claim overstates the pinned implementation.
- **Row I judgment:** The abort **belongs**. Calibration cannot be computed honestly when an allocated hand-check object lacks a usable finite instrument output, and the row already mandates a pre-BS-8f halt. Naming that halt closes a real orphan in the study-level outcome surface. The defect is not the abort; it is attributing that earlier lifecycle outcome to the later verdict function.
- **Smallest sufficient repair:** Define the list as the canonical **study-run lifecycle outcome registry**, exactly one outcome per run, and name the producing phase/process for each category (Row I, Row J, Row P/pre-verdict validator, or numeric decision helper). Narrow `run_production_verdict()`'s emitter claim to outcomes it can actually return, or add a single canonical orchestration symbol that owns and returns every terminal phase. Keep the per-attempt registry separate and unchanged.

### 2. MEDIUM / BLOCKING — the new V16→V17 §10 trace is not a complete finding→change map

- **Section / lines:** §6.3 lines 594–596; §10 lines 769–789, especially 771–778; actual V16→V17 diff at Row P and §10.
- **Evidence:** The V16 review's GPT56 Finding 4 and `BRIEF_V17_REPAIR.md` Blocker 1 required two linked edits: restore the operative §6.3 bodies **and remove Row P's citation to superseded V15 line numbers in favor of current §6.3**. The V16→V17 diff shows both edits landed. The new trace records only “Restored the operative bodies with normative verbs to the §6.3 titles”; it does not record the Row-P citation repair. The same V16 reviews found that §10's “V15→V16 applied §4” sentence was historically false. V17 left that sentence in place, but the V16→V17 trace's “Partial repairs” row does not mark that part unresolved; V18 later removes it and its V17→V18 trace acknowledges the removal.
- **Why it fails:** §6.3 requires every gated revision's finding→change map and separately listed untraced changes. The trace's headline says the V16 findings were applied, but one actual repair hunk is omitted and one known partial/non-repair is not disclosed in that revision's map. This is not merely a stylistic omission: it prevents the trace from reconstructing what the V16 finding caused and what V17 knowingly left false.
- **Smallest sufficient repair:** In V16→V17, expand the §6.3 finding row to include Row P's V15-citation replacement, and add the still-unrepaired historical §10 claim to the “Partial repairs” row. No prose outside §10 needs to change.

## Registry cardinality and Clause-10 audit

### Construction of the two sets

- **Disjoint by construction: HOLDS.** The run-level namespace consists only of numeric verdicts, pre-statistic halts, accounting refusals and `VOID`, with exactly one terminal study outcome intended. The per-attempt namespace consists only of `EXCLUDED-BY-ABSENCE`, `EXCLUDED-BY-NONFINITE`, `EXCLUDED-BY-CONFIDENCE`, and `ACCEPTED-FINITE`, carried as a terminal partition in the adequacy receipt. No label appears in both sets; per-attempt states are explicitly “never a run outcome.”
- **Projection between levels: HOLDS.** Any one or more `EXCLUDED-BY-*` attempt states deterministically produces the single study-level `INCONCLUSIVE-BY-CALIBRATION`; all accepted-finite with no accounting defect permits continuation.
- **Remaining construction defect:** The study-level set is sound as a lifecycle registry, but §5 attaches it to one late function rather than to the lifecycle/orchestrator (Finding 1).

### Forward: branch → category

- Held under attack: BS-1 A/B/date fallback; exact/production selection boundary; manifest equality/refusal; calibration `<0.85` halt before the spread branch; admitted spread `<=0.03` scalar and `>0.03` profile; exactly 1,000 Stage-C trials; 961/962 boundary; self-verification fail/pass; Row-P missing/duplicate/orphan/malformed precedence; absence/non-finite/low-confidence/accepted-finite attempt states; zero versus one-or-more post-unblinding removals; numeric p/sign/band/floor regions; forbidden acts/protocol deviation to `VOID`.
- Row I missing or non-finite allocated output reaches the newly named `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT` study outcome and halts before BS-8f. That branch is substantively closed.
- The carried Stage-P shared-null versus exact-null code conflict remains openly blocked at BS-5p rather than falsely represented as executable closure.

### Reverse: category → reachable antecedent

- All four per-attempt states have Row-P antecedents.
- The three numeric outcomes have mutually exclusive decision antecedents; the residual/equality region reaches numeric `INCONCLUSIVE`.
- Calibration, power, Row-I, four accounting, and `VOID` categories each have lifecycle antecedents.
- Reverse reachability fails only under §5's stronger named-producer assertion: Row-I and Row-J pre-unblinding outcomes cannot be emitted by the post-unblinding `run_production_verdict()` (Finding 1).

## Threshold sweep — value, phase, failure effect

- **Calibration floor `0.85`: HOLDS.** V18 §3 now checks it first; any `<0.85` halts pre-unblinding with `INCONCLUSIVE-BY-CALIBRATION`, while equality passes. This matches §4, §6.3 and `adjudicate_path()` at pinned lines 1492–1496.
- **Scalar/profile spread `0.03`: HOLDS.** It is evaluated only after the calibration complement; `<=0.03` selects scalar, `>0.03` selects profile, and profile is not a failure. Pinned line 1496 agrees.
- **Confidence threshold: CONTRACTUALLY SEATED, VALUE INTENTIONALLY UNRESOLVED.** BS-2a alone owns predicate, value, authority and retry/failure semantics before BS-6; Row P only applies it at P8. Below threshold → `EXCLUDED-BY-CONFIDENCE` → run-level calibration inconclusive. BS-2a remains refused and BS-6 blocked, so no unpinned value is used.
- **Stage C:** `N_TRIALS = 1,000`; 962 passes and 961 fails; `refuted` or `nonconservative` fails closed to power inconclusive; protocol deviation leads to `VOID`. Pinned constants 77–78 and returns 1275–1277 agree.
- **Post-unblinding attrition:** zero removals may continue; any one or more removals emits calibration inconclusive; no Stage-C rerun.
- **Production/statistical:** 100,000 permutations; reproduction `p < 0.001`; rejection `p > 0.05`; equality falls to numeric inconclusive; amplitude 0.0408; public sigma 0.011; three-sigma bands; detection multiplier 3.09. Pinned constants 73–85 and decision lines 1577–1584 agree.
- **Planning:** retention 0.8572, `N_eq >= 100,000`, exact mode `<=16`, and planning margin 1.2 agree with pinned constants.
- **Other prose thresholds:** release fallback 2026-09-05; catalog cuts; 10× Stage-P boundary audit; calibration allocation floors >=10 per non-empty joint cell and >=30 real labels per live inherited stratum have stated phases and local failure effects. Their external scientific provenance was not re-fetched in this no-fetch review.

## §2.7, adjacency, trace, and overclaim checks

- **§2.7 repair: HOLDS.** The live body contains no reason-(d) owner. Its only remaining “reason (d)” occurrences are historical §10 trace statements recording the partial V17 state and V18 deletion. BS-2a is the sole authority; Row P applies it.
- **§3 repair: HOLDS.** The prose now matches the calibration-first ordering of pinned lines 1492–1496.
- **Chronology repair: HOLDS to available evidence.** Banner and fold record both distinguish instruction/initiation, verdict arrival during assembly, and final V16 bytes after the schema repair. The underlying 21:48 instruction remains Testimony.
- **V17→V18 trace: ACCURATE.** Every substantive V18 hunk is represented: §2.7 ownership, registry split plus Row-I abort, calibration precedence, chronology, historical-claim removal, both trace additions, and the future-trace requirement. “Blocker 4 & 6” resolves to Blocker 4 and Repair 6 in `BRIEF_V18_REPAIR.md`.
- **V16→V17 trace: INCOMPLETE.** See Finding 2.
- The standing limitations remain prominent: Findings 1, 2, 2b and 3 unresolved; BS-2a refused; Rows C2/E blocked; BS-6 and first image byte blocked; `verify_lock()` and unblinding-receipt schema required but unimplemented.

## Failed attacks / credited repairs

1. Tried to recover live reason-(d) or a second confidence owner: failed; only historical trace occurrences remain.
2. Tried a calibration-low plus spread-high counterexample: failed; V18 halts at calibration before profile selection, matching pinned code.
3. Tried to place any `EXCLUDED-BY-*` or `ACCEPTED-FINITE` label in the run-level set: failed; the namespaces are now type-disjoint.
4. Tried to orphan Row I's missing/non-finite allocated-output branch: failed at the lifecycle level; the new category belongs and has the correct pre-BS-8f phase. The surviving defect is producer attribution.
5. Tried to falsify the V17→V18 trace against the 50 changed lines: failed; its substantive descriptions match the diff.
6. Tried to recover the false V15→V16 “applied conforming edits” claim: failed; V18 removed it.
7. Rechecked the principal equality seams (`a_LB_b == 0.85`, spread `==0.03`, 962/1,000, `p == 0.001`, `p == 0.05`): their intended sides agree with the pinned code.

## Testimony and limits

- The 21:48 instruction/initiation, historical scientific measurements, predecessor counts, Stage-P measurement, source-citation verification, archive seal state and three-seat BS-2a refusal were not independently re-executed here.
- Future `verify_lock()`, `verify_unblinding_receipt()`, slot/unblinding schemas, Row-J guard implementation, mediator, C2 worker, acceptance recomputation, replay verifier and adequacy verifier remain required work, not executed protection.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch anything, inspect secrets, or touch χ-bearing material.

## Evidence ledger and custody

Content read:

- `BRIEF_V18_WHOLE_REVIEW.md` in full.
- Exact pinned V18 subject in full, only after digest verification.
- `BRIEF_V18_REPAIR.md` and `BRIEF_V17_REPAIR.md` in full.
- Both V17 whole-review reports and both V16 whole-review reports in full.
- Complete mechanical V17→V18 and V16→V17 diffs.
- Pinned `successor_ref_v9.py` constants, Stage-C fail-closed returns, `adjudicate_path()`, numeric decision and production-runner regions.

Independent checks:

- SHA-256 of V18 before opening and repeat identity checks for V17, V16 and pinned v9 code.
- Whole-document outcome-token inventory and forward/reverse mapping against Rows I, J and P.
- Direct cardinality/type comparison of both registry sets.
- Whole-document threshold sweep with targeted pinned-code comparison.
- Reason-(d)/confidence-authority search.
- Applied-diff verification of both new §10 entries.

No source, code, draft under review, data artifact, prior report or gate brief was modified. This required report is the sole write by this seat.

**NOT CLEAR**
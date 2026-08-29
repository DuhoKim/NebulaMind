# V54 whole-document review — GPT56

## Verdict

**NOT CLEAR.** The dispatched V54 bytes matched the required SHA-256 before I read them. The five prior `UNREACHABLE-BY-CONSTRUCTION` promotions are genuinely withdrawn in both the draft and the live raise-site ledger, but the new numerical class still contradicts its own VOID precedence on the production decision path; the revised promotion bar still permits a universal “cannot fire” label on finite non-exhaustive testing; and the class rule has no stated treatment for the ledger's three pre-run numerical-planning failures. The V42 KIMI citation remains substantively wrong, and the referenced numerical-routes artifact still opens with the withdrawn 48-unread/range state despite V54 claiming reconciliation.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §5 lines 495, 525, 533–534; §6.1 Row P line 608; §7.1 lines 795–796

V54 assigns the post-unblinding production decision failures to two incompatible outcomes. Section 5's precedence clause says every applicable VOID antecedent governs and `INCONCLUSIVE-BY-NUMERICAL-FAILURE` “never fires where a VOID antecedent applies” (line 495). The VOID rule then makes post-unblinding permutation/statistic/protocol non-finite or degenerate failures VOID (lines 533–534), with canonical antecedents `VOID-5-NONFINITE` and `VOID-5-DEGENERATE` explicitly scoped `Post-unblinding` (lines 795–796).

But line 525 justifies the generic numerical code partly by saying the **post-unblinding decision path** — `_finite`, `w_profile`, `sigma_ours_scalar`, `sigma_ours_profile` — is “genuinely unterminated and claimed by nothing.” That is false under the same section's precedence. The pinned code confirms these functions are called by `_decide_from()` (reference lines 1561–1576), and `run_production_verdict()` calls `_decide_from()` only after the production permutation record (lines 1591–1621). Row P places that verdict path at P8 after unblinding. Thus a non-finite/degenerate failure there is already claimed by VOID and cannot justify or emit the generic inconclusive code.

This is outcome-changing, not editorial: following line 525 converts a post-unblinding VOID into an inconclusive result; following lines 495/533/795–796 voids it. The separately parked per-call-site ledger problem remains parked; this finding is the draft's direct prose contradiction about the named production path. Remove those post-unblinding functions from the “claimed by nothing” rationale, or define a non-overlapping phase/condition where the generic outcome actually applies.

### F2 — MEDIUM / REPAIR-REQUIRED — §5 lines 497–523

The revised evidence bar is still insufficient for the status it authorizes. Line 497 defines `UNREACHABLE-BY-CONSTRUCTION` as a guard that “cannot fire at all,” but lines 498–501 continue to permit promotion on an execution count alone. Line 523 concedes the decisive point: finite executions are evidence, not proof. The added requirement to vary every argument in the callable's documented surface does not require exhaustive values, joint interaction coverage, boundary coverage, or a proof that the generator's support spans the contract.

A literal counterexample under the pinned `allocate_handcheck(cell_counts, budget)` demonstrates the hole. A stated three-execution harness varied both arguments: `(all 100s, 500)` returned, `(all 100s, 501)` returned, and `(all 10s, 500)` hit the positive-control family at L1403. It therefore varies every documented argument and has a positive control, yet it misses the admissible `(all 100s, 200)` input, which fires L1401 exactly: `inherited floors need 270 labels, budget 200 — FAIL`. This is the same absence-clause failure in a smaller conforming harness.

The fallback in line 523 makes a false label routing-safe, but it does not make the record's universal claim true. Measurement-only evidence can support a status such as `NOT-OBSERVED-UNDER-HARNESS`; `UNREACHABLE-BY-CONSTRUCTION` requires a proof over the contract (or a finite exhaustive domain established as such). The current bar still allows a third false promotion while complying literally with the text.

### F3 — MEDIUM / REPAIR-REQUIRED — §5 lines 493–497, 524; raise ledger lines 7–16 and 78–80

The class rule omits a category that its own referenced ledger uses. Section 5 says the condition covers “any computation performed by the pinned reference” at every phase and frames the operative distinction as caller error, run outcome, or `UNREACHABLE-BY-CONSTRUCTION`. Yet `ref/RAISE_SITE_CLASSIFICATION.md` assigns three live sites — `local_pass` lines 963, 973 and 986 — to a fourth status, `NUMERICAL-PLANNING`, explicitly described as firing “before the run exists.” They are excluded from the draft's 22 `NUMERICAL` count, and no precedence clause or terminal consequence defines what `NUMERICAL-PLANNING` means.

The distinction matters. A coherent direct planning call can reach L963 (`no subset reaches l_plan on retained counts`), but no run exists to terminate in `INCONCLUSIVE-BY-NUMERICAL-FAILURE`. Either the universal class rule must explicitly exclude pre-run slot construction and state that these failures leave the relevant class-P slot unfilled/no run created, or it must define a planning-halt consequence. As written, the artifact needs a fourth category that the rule neither authorizes nor terminates.

### F4 — MEDIUM / REPAIR-REQUIRED — §2.6 lines 276–285; `gates/PREREG_TEXT_V11_KIMI.md` lines 224–241 and 332–351

The V42 citation change replaced one wrong KIMI finding with another citation that still does not support the claimed ruling. V54 uses `KIMI-V11 F7 / GPT56-V11 F4 / CODEX-V11 4` to support the statement that three seats found Stage P operatively dual-valued because prose promises exact-per-trial while the §0-pinned code implements shared-null.

KIMI-V11 F7 is instead the **v7-subject disclosure** finding: the exact Stage-P receipt ran against v7 rather than the pinned v9, the text did not disclose that fact, and KIMI independently found the relevant primitives byte-identical so the measurement transfers. KIMI's directly relevant F13 says the opposite of V54's attribution: “The promise is now single-valued — the exact per-trial test,” while asking for an in-section demotion marker on §4's retained shared-null description. Therefore F7 contains a related sentence (“not implemented in the file §0 pins”) but does not establish the asserted three-seat dual-valued ruling; the same report explicitly reads the promise as single-valued. Remove KIMI from that claimed consensus or describe KIMI's actual, narrower finding without converting it into the other seats' ruling.

### F5 — MEDIUM / REPAIR-REQUIRED — §5 lines 524, 530; §11 line 966; `OPEN_QUESTION_PRE_UNBLINDING_NUMERICAL_ROUTES.md` line 1 and lines 407–485

The 48-unread reconciliation was applied to the draft and ledger but not to a live artifact the draft still cites for current status. V54 says all 112 raise nodes have been read, none is unassigned, the old 48-unread/range state is withdrawn, and §11 repeats the reconciled state. The raise ledger agrees: 112 rows, no `UNREACHABLE` rows, and class counts closing to 112.

However, line 530 directs the reader to `OPEN_QUESTION_PRE_UNBLINDING_NUMERICAL_ROUTES.md`, whose first-line status still says **“48 raise sites remain unread; the class stays a range (31–79) until they are.”** Later updates in the same artifact say the remaining 70 were read, the corpus is complete, and the per-site table is authoritative (lines 407–485). A status line and its own later body cannot both be current. This is the same stale-live-inventory defect V54 repaired in §11, surviving in the referenced source-of-status artifact. Update the artifact's top status to the reconciled state (without erasing its historical sections), or stop citing it as the current unresolved-status reference.

## Attacks that held

- Subject custody held: SHA-256 was exactly `b0ccbecc46e216777867ef1e219b15cb991781d1455c6bb8e8e0af7d0c204190` before the first draft read and remained unchanged after review. The §0 pins also matched: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- Withdrawal completeness held: the V54 draft says no site currently holds `UNREACHABLE-BY-CONSTRUCTION`, and the regenerated ledger has 112 unique rows with classes `CALLER 20 / INTEGRITY 61 / NUMERICAL 22 / NUMERICAL-PLANNING 3 / TYPED-OUTCOME 3 / WRAPPER 3`; it contains no `UNREACHABLE` class row.
- BS-3g held on the assigned test: it is present in the exhaustive non-χ receipt list, has a `blocks BS-6` edge, and §11 honestly says the missing schema/producer/verifier makes the edge not yet receiptable. The slot remains DESIGN/UNFILLED; disclosed incompleteness is not numbered as a defect.
- Row L's named-object breadth held apart from the expressly parked freeze-signature-definition issue: the freeze signature and opening authorization are the two exemptions; the BS-L detached signature is already over the canonical lock digest. The parked P7-only antecedent phase was not renumbered.
- The terminal rerun deletion held. Searches found historical reruns, fixture/design reruns, BS-2a retry semantics, and explicit no-rerun statements, but no same-run retry after a terminal numerical outcome, no attempt log/cap, and no seed schedule.
- Misconduct scope held: forbidden acts and protocol/digest deviation remain `Any` in §5 and §7.1; only numerical non-finite/degenerate conditions are post-unblinding.
- Class counts held at 16 class P / 8 class E, and the historical 15/8 → 16/8 transition is recorded.

## Machine checks and evidence ledger

- `tools/prereg_counts.py`: 16 class P, 8 class E; prose matches.
- `tools/prereg_trace.py`: 53 transitions, 0 problems; three scope self-tests, 0 failures.
- `tools/void_registry.py --self-test`: 54 antecedents; six controls, 0 failures. As the draft discloses, this proves naming coverage, not semantic coverage.
- `tools/prereg_lint.py`: exit 0, 0 blocking, **97** legacy-citation advisories. I did not report those advisories as unresolved under option D. The brief's stated 96 is a dispatch/tool count mismatch, not a numbered draft finding.
- Independent AST recount: 112 `Raise` nodes — 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, 1 bare re-raise — matching V54 and the ledger.
- Direct pinned-code probes reproduced L1401, L1403, and L963 as described above.
- Content read: the full 970-line V54 draft; V53 reports from both seats; the complete raise ledger; relevant pinned source regions; `PREREG_TEXT_V11_KIMI.md`; `OPEN_QUESTION_PRE_UNBLINDING_NUMERICAL_ROUTES.md`; and the named checker outputs. The parked BS-2v, freeze-signature-definition, Row-L-phase, per-call-site-ledger, access-vocabulary, authorization, and gain-mapping questions were not renumbered.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V54
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §5 lines 495, 525, 533–534; §7.1 lines 795–796 | The post-unblinding production decision failures are claimed by the generic numerical outcome even though the draft's explicit VOID precedence already claims them.
F2 | MEDIUM | REPAIR-REQUIRED | §5 lines 497–523 | The promotion bar still permits a universal UNREACHABLE-BY-CONSTRUCTION label on finite non-exhaustive testing that can miss a reachable guard while satisfying every literal harness requirement.
F3 | MEDIUM | REPAIR-REQUIRED | §5 lines 493–497, 524; raise ledger lines 7–16, 78–80 | Three NUMERICAL-PLANNING sites fire before a run exists but the universal class rule neither authorizes that fourth category nor states its terminal consequence.
F4 | MEDIUM | REPAIR-REQUIRED | §2.6 lines 276–285; KIMI-V11 lines 224–241, 332–351 | KIMI-V11 F7 is a v7-subject disclosure finding, while the same report calls Stage P single-valued; it does not support V54's asserted three-seat dual-valued ruling.
F5 | MEDIUM | REPAIR-REQUIRED | §5 lines 524, 530; §11 line 966; numerical-routes artifact line 1 | The referenced status artifact still says 48 sites are unread and the class is 31–79 although its own later body, V54, §11, and the ledger say the corpus is complete.
<!-- END FINDINGS-BLOCK -->
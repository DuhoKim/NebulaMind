# V40 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** The dispatched V40 bytes match the required SHA-256, and the principal's phase split itself is represented faithfully: forbidden acts and protocol/digest deviation remain `Any`, while the numerical conditions are post-unblinding. The repair nevertheless does not supply an executable pre-unblinding computation-failure procedure. It emits a terminal run outcome and then permits that run to continue, leaves the rerun's random address and attempt custody open, and declares a pre-BS-6 parameter without adding any slot or dependency that binds it. Independently, the 16/8 inventory change still omits BS-3g from §6.1's exhaustive non-χ-bearing receipt list.

## Subject identity

- Required SHA-256: `531d3f40f06130e792ff474e660fde931038e2d7bd8e573612b90c8ec624c1f6`.
- Recomputed before reading the draft: `531d3f40f06130e792ff474e660fde931038e2d7bd8e573612b90c8ec624c1f6` — exact match.
- V39 recomputed as `221c6a08cd794e5b6be219fffa7f96b475b3784844123c5ec7617f86e4bf9db5`; the V39→V40 diff changes the title, §5 procedure/scope prose, §7.1 repair note, and §10 trace row, with no registry-row change.

## Findings

### 1. HIGH — REPAIR REQUIRED — the new branch emits a terminal run outcome and then continues the same run

V40 line 488 says the lifecycle registry emits **exactly one outcome per run**. Lines 491–493 classify `INCONCLUSIVE-BY-COMPUTATION` as a pre-statistic inconclusive **halt**, then require the operator to emit that code. Line 494 nevertheless permits a rerun of Stage C. That is not a terminated branch: if the rerun later passes and the study proceeds, the same run has already emitted its one run-level outcome; if the first emission really halts the run, the rerun is prohibited.

Normative Row J makes the collision worse. Line 568 says any locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER`, halts the run, makes the complementary PASS branches the sole route to BS-5f, and voids continuation after a Stage-C FAIL. The text gives no precedence rule separating a non-finite/degenerate Stage-C failure from that universal FAIL branch. An operator must decide whether to classify it as the new rerunnable computation halt or the old terminal power halt.

Repair requires a single cardinality model: for example, make failed computations authenticated **per-attempt states**, emit no run-level outcome while another attempt is legally pending, and emit the single run-level `INCONCLUSIVE-BY-COMPUTATION` only when the frozen attempt policy is exhausted. Row J and clause 10 then need the same branch and precedence.

### 2. HIGH — REPAIR REQUIRED — the rerun rule leaves both attempt custody and the random address selectable

Lines 495–496 say every attempt is recorded, only a recorded non-finite/degenerate result permits another attempt, and a silent or finite-result rerun voids the run. Nothing enforces those universal negatives.

The claimed “§6 log” is not a conforming path for this record. Section 6.1 calls its non-χ-bearing list exhaustive (lines 540–548). Its only log schema is the BS-2k access-event schema at line 543, whose fields cover actor/table-row/store operation/object identity/success-or-refusal/refusal reason/chain digest. Row B at line 559 appends one event per **sealed-store touch**. A Stage-C numerical attempt is not a store touch, the schema has no attempt index, triggering numerical condition, computation outcome, random address, or predecessor-attempt digest, and Row J at line 568 emits only BS-5f. Thus a caller can suppress a finite attempt and author only a later “recorded” failure; the document has neither an exclusive Stage-C invocation boundary nor an authenticated prior-failure token required before the next invocation.

The rerun's random stream is also unbound. Line 494 fixes implementation and protocol **digests**, not the runtime address. Frozen `ref/successor_ref_v9.py` lines 160–161 defines randomness by `(MASTER_SEED, stage, prefix, trial, role)`, and `stage_power()` lines 1218–1219 exposes `prefix` as an argument. I executed the pinned function: identical prefixes reproduced byte-identical random draws, while changing only `prefix` changed them (`same_prefix_equal True`; `different_prefix_equal False`). Reusing the exact address merely reproduces a deterministic numerical failure; advancing the prefix creates a new random attempt and therefore needs a frozen address schedule. V40 specifies neither. This is a genuine forking path, not cured by saying the code digest is unchanged.

Repair requires a canonical attempt schema and mediated invocation path that binds run ID, monotonic attempt index, predecessor failure receipt, exact random address, implementation/protocol/environment digests, authenticated trigger, and terminal attempt state; it must make every invocation receiptable rather than trusting the set of attempts the operator chose to report.

### 3. HIGH — REPAIR REQUIRED — the deliberately unbound maximum has no pre-BS-6 binding edge

Line 497 openly declares that the maximum attempt count is unbound and must be bound before BS-6. The disclosure is honest, but it is insufficient. A full-text count finds this is the only occurrence of “maximum attempt count” or “attempt count” in the draft. Section 7's complete class-P table (lines 702–727) has no slot for the attempt limit, retry address schedule, or attempt schema. `BS-7p` names general randomness/serialization and fixtures, but does not name this new parameter or block its omission; §11's code-side inventory likewise contains no computation-rerun item.

Consequently every currently enumerated class-P slot can be filled and every existing dependency satisfied while this parameter remains unbound. This is the same structural defect BS-3g was added to repair: prose saying “must be bound before BS-6” is not a dependency edge. The eventual value can still be chosen after later information unless a named DESIGN slot (or an explicit expansion of an existing slot's schema, producer, fixtures, and `blocks BS-6` contract) is added and freshly gated.

### 4. MEDIUM — REPAIR REQUIRED — BS-3g is absent from the exhaustive receipt/schema inventory

The class arithmetic and §7 DESIGN prose were repaired, but the new row did not propagate through the whole document. BS-3g is class P, DESIGN/UNFILLED, and blocks BS-6 (lines 708 and 723). Every class-P slot must hold a receipt before freeze (lines 53–59 and Row L at line 570), and BS-L must bind the ordered manifest of every class-P receipt (line 587).

Yet §6.1 lines 540–542 call the non-χ-bearing receipt list closed and exhaustive and enumerate every slot receipt except **BS-3g**. Lines 548–550 make every omitted artifact χ-bearing by default and limit external gate inputs to that closed list. Row M can read only the closed list to write §7's slot receipts (line 571). Therefore the required BS-3g receipt either cannot be handled by the gates/producer/lock path or becomes χ-bearing by default, contrary to its pre-BS-6 design role. Add BS-3g and its authenticated schema to the closed list and to the corresponding code-side inventory.

## Attacks that held

- **Misconduct scope:** held. V40 lines 499–500 preserve forbidden acts and protocol/digest deviation at `Any`; registry lines 758–760 do the same. The V39→V40 registry rows are unchanged.
- **Numerical phase split:** held as the principal's chosen policy. Registry lines 761–762 remain `Post-unblinding`, and pre-unblinding numerical failure is no longer silently claimed to match those rows. The findings above concern the replacement procedure, not a demand to reverse the ruling.
- **§2.7 instant:** held. V11 lines 266–268 say the freedom is exercised after image inference exists, and lines 293–294 attach the threshold trigger to that instant. V40's lifecycle produces real χ at P2 and unblinds at P7, so `Post-first-real-χ` is earlier than `Post-unblinding`. Commit `4d99d1d93` contains the quoted first-person repair body and Claude co-author trailer; V40 accurately labels this strong evidence rather than proof of lane authorship.
- **BS-3g dependency row and 16/8 totals:** held. The §7 table parses to 16 class-P and 8 class-E rows; `tools/prereg_counts.py` agrees. BS-3g itself blocks BS-6. Finding 4 is the separate exhaustive-receipt-list casualty.
- **Checker claims:** `prereg_counts.py` reports 16/8 and prose match; `prereg_trace.py --check` reports 39 transitions / 0 problems; `void_registry.py` reports 54 antecedents / 20 rows / digest `a4d1d745b2ed33bc0e01dd39b845f88daffdc542d2bdd98d5e122ab7dd443d37`; `prereg_lint.py` exits 1 with exactly the quarantined repair-citation advisory named in the brief.
- **Referenced gain-control pins:** live hashes match the draft for `gain_gradient_estimator.py` (`e227029713396a92…`) and `verify_mu_gamma.py` (`e33d9275d8078743…`); both v6 reports are CLEAR only for their scoped repairs and explicitly retain the completeness fork, as V40 says.

## Evidence ledger and limits

Read in full: `BRIEF_V40_REVIEW.md`; the complete V40 draft; V11 §2.7; V38 CODEX review; the exact V39→V40 and V36→V37 deltas; `FINDINGS_MAP.md`; `OPEN_QUESTION_T_COMPLETENESS.md`; `tools/prereg_lint.py`, `tools/prereg_counts.py`, `tools/prereg_trace.py`, `tools/void_registry.py`; and the relevant `successor_ref_v9.py` RNG and Stage-C code.

Executed: SHA-256 verification before draft read; all four named checkers; independent §7 parsing; git commit/body inspection for `4d99d1d93`; live hashes for referenced gain files; exact random-address probe against pinned v9; and scoped repository-status checks. I did not read image data, run inference, execute Stage P/C, unblind, fill a slot, alter frozen code, or modify the draft. Pre-existing unrelated repository dirt was left untouched. The only intended write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V40
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §5 lines 488, 491–496; §6.1 line 568 | A run-level computation halt is emitted and then rerun, violating the one-outcome and Row-J halt contracts.
F2 | HIGH | REPAIR-REQUIRED | §5 lines 494–496; §6.1 lines 540–559, 568 | Attempt logging is not receiptable or exhaustive and the rerun random address is selectable, leaving a forking path.
F3 | HIGH | REPAIR-REQUIRED | §5 line 497; §7 lines 702–727; §11 lines 908–920 | The disclosed maximum-attempt parameter has no named pre-BS-6 slot, schema, producer, or dependency edge.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 540–550; §7 lines 708, 723 | BS-3g is missing from the exhaustive non-χ-bearing slot-receipt inventory.
<!-- END FINDINGS-BLOCK -->
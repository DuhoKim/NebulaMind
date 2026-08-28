# V36 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**CLEAR.** The named V36 bytes match the brief's full SHA-256 exactly. The V35→V36 delta is limited to the retitle, the BS-2a row at line 698, and one appended V34→V35 §10 row, exactly as announced. Both V35 MEDIUM findings are repaired at the strength of the two round-6 source reports: the single-deletion statement now describes the one 26-check evidence class rather than an apparent 52 probes, and the crash statement now makes nonzero exit status—not the presence of `MATCH` on stdout—the integration boundary. The V30 protected scope and §2.7 sentence remain byte- and position-identical, class counts remain 15/8, the BS-2a component pin holds, the slot remains DESIGN/UNFILLED, and BS-6 plus the first image byte remain blocked. I found no new repair-required defect under a fresh whole-document absence-surface attack.

## Identity and exact comparison

Subject: `../PREREG_SUCCESSOR_DRAFT_V36_20260829.md`.

- Brief-pinned SHA-256: `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177`.
- Independently computed SHA-256: `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177`.
- **Comparison: MATCH — exact 64-hex equality over the named 108,672-byte V36 file.**
- Independently computed predecessor V35 SHA-256: `b80d50afe076fe8d20c9fd1a6e6b5db63779dfc02ee46601667a67227e12fbdd`, matching its pin.
- Mechanical V35→V36 diff: line 1 retitle; line 698 replacement; one appended V34→V35 trace row at line 866. No other bytes moved.

## Numbered findings

**None.** The two V35 repair sites hold, and the whole-document absence attack produced no new defect.

## Adjudication of both V35 repairs

### 1. GPT56-V35-1 — HELD: the duplicated 26-probe class is gone

V36 line 698 now says:

> “one strict single-deletion sweep over the 26 unique checks, all 26 caught by a named control with zero crash-only credits and zero undetected”

This no longer reads as “26 single” plus “26 single-check” probes. It names one finite evidence class—single deletion of each of the 26 unique checks—and gives its closure: 26 named-control detections, zero crash-only credits, zero undetected.

Manual source-report verification, without using citation lint:

- `BS2A_CODE_GATE_GPT56_R6.md` lines 37–42 reports a strict literal source-deletion sweep over all 26 unique checks: `total=26 named=26 crash_only=0 undetected=0`.
- `BS2A_CODE_GATE_CODEX_R6.md` lines 116–151 reports the same 26/26 single-code result under the strict rule that an exception is `CRASH_ONLY`, never detection.
- CODEX additionally reports all 325 two-code combinations as filter-derived from real control outputs and six pairs as literal AST source mutations with real self-test reruns. GPT56 line 100 expressly says it did not run all 325 pairs at round 6.
- V36 preserves exactly that distinction: 325 filter-derived, six literal pair mutations, and no claim that both seats literally source-mutated all 325.

The singular “one ... sweep” describes the 26-member test class and prevents the former 52-probe reading; the preceding gate sentence attributes component CLEAR to both seats, and both source reports independently reproduce that same complete single-deletion class. The row neither invents a second 26-member class nor launders the pairwise evidence into literal execution by both seats.

### 2. CODEX-V35-1 — HELD: the exit-status boundary is now explicit

V36 line 698 now says:

> “no builder-produced row reached a crash in the 65,060-row type/schema census, and every observed crash exited nonzero. Consumers must gate on exit status: a post-verification emit failure can print the true `MATCH` summary and then exit 1, so a consumer treating `MATCH` on stdout as success can be misled.”

That is the exact boundary the round-6 reports support:

- CODEX R6 lines 194–204 reports the full 65,060-row builder-output type/schema census and zero rows outside the builder boundary.
- CODEX R6 lines 206–244 distinguishes verifier crashes from the post-verification emit failure and reproduces the latter: truthful `MATCH`, then `FileNotFoundError`, exit 1. It says stdout-only integration can be misled.
- GPT56 R6 lines 53–65 independently reports the full 65,060-row census and zero off-boundary rows.
- GPT56 R6 lines 68–77 reproduces the same emit-destination case and states that fail-closed behavior depends on honoring process status.

V36 no longer claims that a crash can never coexist with a success-looking stdout token. It makes the empirical scope explicit (“builder-produced row,” “observed crash”) and states the required consumer contract. It does not claim arbitrary-hostile-input hardening; that limitation remains prominent. The component remains freeze-cleared only, not fill-authorized.

## Repair-announcement citation check

The citation checker in `prereg_lint.py` was treated as quarantined and received no evidentiary weight.

I manually opened both V35 reports and the current-transition entry in `gates/FINDINGS_MAP.md`:

- `GPT56-V35-1` is exactly the duplicated 26-probe-class finding.
- `CODEX-V35-1` is exactly the missing exit-status boundary and the `MATCH`-then-exit-1 counterexample.
- `FINDINGS_MAP.md` maps V35→V36 to those two findings and paraphrases both accurately.

The draft itself appends V34→V35 at line 866, as required by its self-reference rule; the current V35→V36 mapping lives in the external sidecar. `prereg_trace.py --check` accepts that structure with 35 computed transitions and zero problems.

## Whole-document absence-surface attack

I reread all 887 lines. The original six-token seed (`never`, `nowhere`, `cannot`, `must not`, `in no case`, `none`) yields 76 occurrences on 68 lines in V36. A broader inventory also found standalone `no` on 74 lines, `only` on 61, `exactly` on 22, `every` on 46, `nothing` on 9, `without` on 6, `all` on 20, `any` on 67, and smaller `exhaustive`/`forbidden`/`unable`/`unreachable` surfaces. Counts overlap and are an attack inventory, not substantive proof.

For each candidate I asked whether the absence is enforced by construction, a blocked prerequisite, a normative conduct rule, or historical testimony—and whether it could be false without the document's declared machinery noticing.

### Enforced by algebra, types, exact sets, or finite comparison — held

- §1: exact-mirror antisymmetry enforces parity-even cancellation and sign swap, but V36 does not extend it to parity-odd raster response, upstream non-equivariance, or position-coupled sensitivity. The three surviving routes remain explicit.
- §2.3–§2.4: exact small-universe enumeration, external universe/parent pins, no caller-supplied closure answer, and exact missing/extra set refusal are constructive. Production-scale optimality remains expressly unclaimed.
- §3: mask-kind separation, exact length/set checks, canonical sorting, recomputed bin labels, and non-finite/degenerate refusals are code-defined rather than assurances.
- §5: the A=0, wrong-sign, positive-signal, and underpowered branches are tied to named fixtures and decision functions.
- BS-2a: the 26-check deletion closure is a finite executed battery, not a universal inference. The row separately disclaims arbitrary-hostile-input hardening.

### Closed-world future requirements with fail-closed gates — held as blocked promises, not current accomplishments

- §2.7: exact-parent terminal partition, closed reason vocabulary, sign-blind construction, evidence recomputation, and independently fixed attempt joins are obligations assigned to the unfilled BS-2a/BS-2f machinery. Missing implementation is named rather than silently treated as complete.
- §4–§5: production-path exclusivity, absence of caller override seams, pre-statistic halts, exact-parent post-unblinding accounting, and no post-attrition Stage-C rerun are tied to named validators/guards. The document expressly lists unimplemented guards.
- §6.1: the permitted aggregate surface, exhaustive non-χ schema list, χ-bearing-by-default rule, actor table, universal default ban, one-use opening, exact signing bodies, and branch termination are normative construction requirements. Where their enforcement does not yet exist, the relevant DESIGN slots remain unfilled and block BS-6.
- §6.2: “no row ... reads” the predecessor archive is a table-surface rule. V36 does not claim a complete log proves nonaccess; it expressly admits a bypass may leave no trace and makes exclusive mediation an unfilled pre-freeze burden.
- §6.3: no post-read cure, no gate claim stronger than its check, and no reconciliation of clean-room divergence are protocol rules. They do not stand as empirical proof that forbidden conduct never occurred.

### Historical or drafting negatives — held at their stated scope

- Preamble no-run/no-fetch/no-data-touch language is drafting testimony and grants no execution authority.
- §2.6 historical no-fetch, zero-disagreement, geometry, and count claims remain historical/receipted statements; none fills an execution slot.
- §9's “no natural-language or MCP output enters a receipt unreconstructed” is an archival-format requirement, not a claim that a search proved global historical absence.

The only changed absence-bearing surface is line 698. Its “zero crash-only,” “zero undetected,” builder-census, and nonzero-exit claims are bounded to finite executed observations in the two source reports. They could not silently authorize a broader property because the same row explicitly says arbitrary-hostile-input hardening is not established and retains all unbuilt BS-2a remainder. No new universal negative was found that could be false while all of its own declared construction and gates passed.

## V30 invariants, class counts, BS-2a pin, and machine checks

- V30 §1 protected scope: V30 lines 131–133 and V36 lines 131–133 are byte-identical at the same line positions, 276 bytes including newlines.
- V30 §2.7 protected sentence: V30 line 384 and V36 line 384 are byte-identical at line 384, 533 bytes including newline.
- `tools/prereg_counts.py`: 15 class P, 8 class E; 23 §7 data rows, 22 with BS identifiers; prose matches the table; BS-2m is the sole claimed filled class-P slot.
- BS-2a component pin: live `ref/bs2a_quality_gate.py` SHA-256 is `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`, exactly matching line 698.
- Fresh component self-test: exit 0; 36 controls; 0 failures; every one of 26 checks exercised.
- BS-2a status remains `DESIGN, CLASS P — UNFILLED`. C2 integrity verification, confidence threshold, retry/failure semantics, ledger schema, and transformed-cutout producer fixtures remain named as unbuilt.
- `tools/prereg_trace.py ... --check`: 35 computed transitions, 0 problems.
- `tools/prereg_lint.py`: exit 0; 15/8 and no non-citation inconsistency. Its citation branch was quarantined and not used as evidence.
- BS-6 and the first image byte remain blocked in the preamble, §6.1 clause 10, the BS-2a row, and the fold record.

## Parked principal questions

Per the brief, I did not re-derive the BS-6 dependency edge, `require_authorization()` accepting arbitrary bytes, the VOID registry amendment, the gain-control T-completeness fork, or the citation checker. They remain outside this verdict. No conclusion here treats their parked status as a repair or authorization.

## Failed attacks / standing that held

1. Subject-substitution attack failed: V36 exactly matches the supplied full digest.
2. Hidden-delta attack failed: only line 1, line 698, and the appended §10 row changed.
3. Apparent-52-probe attack failed: the row now names 26 unique single deletions once and separately qualifies the 325 pair evidence.
4. Pairwise execution laundering failed: V36 says filter-derived, six literal mutations, and GPT56 did not run all 325.
5. Crash-as-stdout-success attack failed: V36 expressly warns that truthful `MATCH` can precede exit 1 and requires exit-status gating.
6. Arbitrary-hostile-input laundering failed: the row retains the NOT-hardened disclaimer and scopes the positive census to builder-produced rows.
7. Fill laundering failed: both source reports and V36 keep component-freeze CLEAR separate from BS-2a fill authorization.
8. V30 drift attack failed at both protected byte/position pins.
9. Class-count drift failed: 15 class P and 8 class E remain.
10. Current-transition citation attack failed under manual source inspection; citation lint was not credited.
11. Whole-document absence attacks outside the changed line failed for the reasons classified above.
12. Authorization drift failed: BS-6 and the first image byte remain blocked.

## Testimony, constraints, and evidence ledger

- Content read: `BRIEF_V36_REVIEW.md`; all 887 lines of V36; full V35→V36 diff; `V35_WHOLE_REVIEW_CODEX.md`; `V35_WHOLE_REVIEW_GPT56.md`; `BS2A_CODE_GATE_CODEX_R6.md`; `BS2A_CODE_GATE_GPT56_R6.md`; `FINDINGS_MAP.md`; V30 protected byte slices.
- Independent executions: V36/V35/V30/component SHA-256; exact unified diff; raw-byte and line-position comparison; lexical absence inventories; class-count parser; trace check; non-citation lint result; live BS-2a self-test; path-scoped git status.
- I did not read `/Users/duhokim/NebulaMindData/`, fetch or inspect an image byte, run inference, execute Stage P/C, unblind anything, fill a slot, change frozen v9, alter the reviewed draft, or mutate git.
- The only durable write from this review is this report.

**CLEAR**
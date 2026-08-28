# V36 WHOLE-DOCUMENT REFEREE REVIEW — GPT56

## Verdict

**CLEAR.** The dispatched V36 bytes match the supplied SHA-256 exactly. The complete V35→V36 diff is exactly the brief-announced retitle at line 1, replacement of the BS-2a row at line 698, and one appended V34→V35 §10 row at line 866; no other bytes moved. Both V35 MEDIUM findings are repaired at exactly the strength of the two round-6 reports: the single-deletion sentence now describes one 26-check sweep rather than an apparent 52 probes, and the crash sentence now limits its claim to the complete builder census plus observed nonzero exits while explicitly requiring consumers to honor exit status and naming the post-verification `MATCH`/exit-1 counterexample.

I reread all 887 lines under the absence lens. I found no new in-scope universal negative that could be false while its own declared construction, validator, receipt, or blocking slot still passed. The V30 protected bytes and positions, 15/8 class counts, BS-2a component pin and DESIGN/UNFILLED scope, and the blocks on BS-6 and the first image byte all hold.

## Exact subject and predecessor comparison

- supplied V36 SHA-256: `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177`
- independently recomputed V36 SHA-256: `e4d7b175ac270f4cdc0bc4af3a16af0e834aa3e4eacc174a73d10798cd4b6177`
- comparison: **MATCH — exact 64-hex equality over the named V36 bytes**
- predecessor V35 pin: `b80d50afe076fe8d20c9fd1a6e6b5db63779dfc02ee46601667a67227e12fbdd`

The full unified V35→V36 diff changes exactly:

1. line 1, V35 → V36 retitle;
2. line 698, one replacement of the BS-2a evidence-strength sentence;
3. line 866, one appended V34→V35 trace row.

No other document bytes moved.

## Numbered findings

None.

## Adjudication of both V35 repairs against the round-6 source reports

### 1. GPT56-V35-1 — HELD: the row now states one 26-check single-deletion sweep, not an apparent 52 probes

V36 line 698 now says:

> “one strict single-deletion sweep over the 26 unique checks, all 26 caught by a named control with zero crash-only credits and zero undetected”

That is exactly supported:

- `BS2A_CODE_GATE_GPT56_R6.md` lines 37–42 reports literal source deletion of each of the 26 unique `refuse()` calls, with `total=26 named=26 crash_only=0 undetected=0` under a rule that counts an exception as crash-only / not detected.
- `BS2A_CODE_GATE_CODEX_R6.md` lines 116–151 independently reports 26/26 single-code deletions with zero crash-only and zero undetected.
- The row does not duplicate “26 single” and “26 single-check” into two grammatical classes. It now names one sweep over one closed 26-check universe.

The immediately following pairwise qualification also remains exact rather than laundering derived cases into literal execution: 325 cases are identified as filter-derived from real control outputs, six pairs as literally source-mutated and re-executed, and GPT56 as not having run all 325. CODEX R6 lines 132–150 and 270–274 support those distinctions; GPT56 R6 line 100 expressly says GPT56 did not run all 325.

The sentence therefore claims neither less nor more than round 6 supports.

### 2. CODEX-V35-1 — HELD: the crash claim now carries the exit-status boundary and the known stdout asymmetry

V36 line 698 now says:

> “no builder-produced row reached a crash in the 65,060-row type/schema census, and every observed crash exited nonzero. Consumers must gate on exit status: a post-verification emit failure can print the true `MATCH` summary and then exit 1, so a consumer treating `MATCH` on stdout as success can be misled.”

Each part is evidence-bounded:

- GPT56 R6 lines 53–65 and CODEX R6 lines 194–204 report a complete census of all 65,060 builder-produced rows: zero off-schema rows, zero wrong row/key/value/flag types, and no verifier raise on the authentic built output.
- GPT56 R6 lines 68–77 and CODEX R6 lines 206–244 report observed crash paths as nonzero process exits.
- Both reports independently reproduce the post-verification emission failure: the valid receipt earns and prints `MATCH`, the requested destination write raises, and the process exits 1.
- Both reports say the integration boundary is process exit status and warn that `MATCH` alone is not a sufficient success signal.

V36 no longer says merely that “a crash fails closed, never a PASS.” It states the finite observed evidence, the complete builder boundary, and the exact consumer obligation. It does not claim arbitrary-hostile-input hardening: the preceding sentence still records that hardening is not established and that GPT56 found an outside-boundary hostile-object raise.

The repair is therefore at exactly the strength of the reports and does not silently turn component CLEAR into fill authorization.

## BS-2a pin and live component check

- V36 line 698 component pin: `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`
- independently recomputed `ref/bs2a_quality_gate.py` SHA-256: `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`
- comparison: **MATCH — exact 64-hex equality**
- live `--self-test --acquire ../acquire`: exit 0; 36 controls; 0 failures; every one of 26 checks exercised
- slot status: **DESIGN, CLASS P — UNFILLED**
- component verdict scope: CLEAR for freezing the quality-predicate component only; not fill authorization

The unbuilt remainder remains explicit in the row: `verify_cutout_integrity`, confidence threshold, retry/failure semantics, ledger schema, and transformed-cutout producer fixtures. The arbitrary-hostile-input limit also remains explicit. Nothing in the repaired wording promotes the component to a filled slot.

## Repair-announcement citation checked manually

I gave no evidentiary weight to the quarantined citation checker.

The appended V34→V35 §10 row at V36 line 866 was checked against the actual V34 referee reports rather than against citation lint:

- `GPT56-V34-2` and `CODEX-V34-3` are the line-120 antisymmetry overclaim: a biased/broken `w` is not globally prevented from creating a signal by mirror antisymmetry alone.
- `CODEX-V34-1` is the line-592 archive claim: an observational bypass need not damage the access-log chain.
- `CODEX-V34-4` is the line-698 evidence-strength defect: the 325 pair cases were filter-derived, only six pairs were literally source-mutated, GPT56 did not run all 325, and crash semantics require the exit-status qualification.

The V34→V35 diff locations and the new row's four cited findings agree. The parked `require_authorization()` finding is correctly not represented as repaired. The announcement is accurate at the source reports' strength.

## Whole-document universal-negative / absence-surface review

I reread all 887 lines, not only the V35→V36 delta. A narrow case-insensitive seed over `never`, `nowhere`, `cannot`, `none`, `must not`, and `in no case` produced 76 occurrences on 68 lines. A broader attack inventory found 94 `no`, 21 `none`, 27 `never`, 22 `cannot`, 2 `nowhere`, 72 `only`, 22 `exactly`, and 51 `every` occurrences. These counts overlap and are only a candidate inventory; each candidate was adjudicated in context.

### Enforced by exact identity, closed type, or finite comparison — held

- §1's mirror identity now enforces only its real algebraic consequence: parity-even cancellation under the exact mirror construction. The document affirmatively names parity-odd raster response, upstream non-equivariance, and position-varying sensitivity as surviving routes.
- §2.3–§2.4's small-universe optimality, external-witness closure, no caller-supplied manifest answer, exact parent digest, and exact set-difference refusals are construction claims tied to named code/fixtures and pins.
- §3's lack of `3·D̂`, non-interchangeable mask types, exact-length and provenance checks, recomputed labels, and malformed-input refusals are code-defined.
- §5's A=0, wrong-sign, positive-signal, and underpowered branches are tied to named executable fixture obligations.
- §10's inability of a draft to carry its own result digest is a genuine self-reference boundary, with the current transition assigned to the external sidecar and the predecessor transition appended only in the next draft.

### Closed schemas and blocked future machinery — held as preregistration promises, not present accomplishments

- §2.7's exact-parent partition, closed exclusion reasons, outcome-field bans, evidence recomputation, and absent-output join are assigned to BS-2a/C2/E machinery. The document says that machinery is DESIGN/UNFILLED and blocks BS-6; it does not claim it has run.
- §4–§5's production-path exclusivity, no override seams, outcome closure, no post-attrition Stage-C rerun, and exact-parent post-unblinding accounting are tied to named guards/validators whose unimplemented state is explicitly listed.
- §6.1's closed non-χ schema list, default χ-bearing rule, actor surfaces, universal default ban, exclusive mediator, one-use opening, and branch termination are normative design requirements. Their absent implementation remains visible in DESIGN/UNFILLED slots and §11.
- §6.2 no longer claims retrospective detection of a bypass. It expressly allows an invisible bypass and makes exclusive mediation a pre-freeze gate condition whose failure leaves BS-2k unfillable.
- §6.3's no-strata, no post-read cure, no stronger-than-artifact gate claim, and no reconciliation-by-edit are conduct and implementation rules, not unsupported empirical absence claims.

### Historical/testimony negatives — not promoted into authority

- The preamble's “no run, no fetch, no data touch” and draft-status statements do not fill any gate or authorize BS-6.
- §2.1's no-DR11-photo-z drafting status is testimony at a named date, not a branch-selection receipt.
- §2.6's “no fetch needed,” zero-disagreement, and finite recount statements remain historical/receipted claims and do not authorize a first image byte.
- §9's ban on natural-language/MCP material entering receipts is a format requirement, not proof that such material never existed.

### Changed-line absence attacks — held

- The 26-check universe cannot silently double: V36 now names one sweep over 26 unique checks.
- Crash-only cases cannot be credited as detected in the reported strict sweep: the source reports define them as NOT detected and report zero.
- A process crash is no longer equated with absence of a success-looking stdout token. V36 names the `MATCH`-then-exit-1 case and requires exit-status gating.
- Builder safety is not universalized to hostile Python input. The claim is explicitly limited to the complete 65,060-row builder census, while arbitrary-hostile-input hardening remains not established.

No new in-scope universal negative was found that could be false without its own declared mechanism noticing. I did not re-derive the parked questions.

## V30 byte-and-position stability

- V30 §1 scope lines 131–133 SHA-256: `51d738df155f2d3a8ecbbc53aeb3ae7fa0f9a2b0957a56535fda34528156d8bc`
- V36 lines 131–133 SHA-256: `51d738df155f2d3a8ecbbc53aeb3ae7fa0f9a2b0957a56535fda34528156d8bc`
- comparison: **byte-identical and position-identical at lines 131–133**
- V30 line 384 SHA-256: `69cca2922ea7470a8241288050eb6d7b985994099cd43133422f5aee5a296746`
- V36 line 384 SHA-256: `69cca2922ea7470a8241288050eb6d7b985994099cd43133422f5aee5a296746`
- comparison: **byte-identical and position-identical at line 384** (533 bytes including newline)

## Class counts and machine checks

- `tools/prereg_counts.py`: 15 class-P rows, 8 class-E rows; 23 §7 data rows, 22 with BS identifiers; prose matches the table.
- `tools/prereg_lint.py`: exit 0; no inconsistencies in the six demonstrated non-citation checks.
- citation branch: **quarantined and disregarded as evidence**; the repair announcement was checked manually.
- `tools/prereg_trace.py ... --check`: 35 computed transitions; 0 problems.
- independent §7 reading: only BS-2m is claimed filled among class-P slots.

## Standing blockers and parked questions

BS-6 and the first image byte remain blocked. V36 line 588 still says clause 10 is not executable and blocks BS-6 until every enumerated VOID antecedent has a pinned producer/conversion. The §7 table keeps BS-2a DESIGN/UNFILLED, BS-2k DESIGN, and BS-2v DESIGN/UNRESOLVED.

Per the brief, I did not re-derive:

- the BS-6 dependency edge;
- `require_authorization()` accepting arbitrary bytes;
- the VOID registry amendment;
- the gain-control T-completeness fork;
- the citation-check defect.

These remain parked on the principal in their OPEN_QUESTION files and had no role in this verdict.

## Failed attacks and held boundaries

1. Subject-substitution attack failed: V36 exactly matches the supplied full digest.
2. Hidden-delta attack failed: only line 1, line 698, and the appended line 866 changed.
3. Fourth-overclaim attack on the BS-2a single sweep failed: the row now states one 26-check universe and no second 26-member class.
4. Pairwise-execution laundering attack failed: 325 remains filter-derived, six literal, and GPT56's nonexecution of all 325 remains explicit.
5. Crash-success laundering attack failed: the row names exit status as the gate and discloses `MATCH` before exit 1.
6. Builder-boundary inflation attack failed: builder safety is limited to the full 65,060-row census and arbitrary hostile input remains expressly unestablished.
7. Fill-authorization laundering attack failed: both source reports and V36 keep component-freeze-only scope and DESIGN/UNFILLED status.
8. Repair-citation attack failed: the V34→V35 row maps to the actual four source findings and does not claim the parked authorization finding was repaired.
9. V30 drift attack failed: §1 lines 131–133 and §2.7 line 384 are byte- and position-identical.
10. Class-count drift attack failed: 15 class P and 8 class E remain.
11. Standing-authorization drift failed: BS-6 and the first image byte remain blocked.

## Evidence ledger and constraints

Content read: `BRIEF_V36_REVIEW.md`; all 887 V36 lines; the complete V35→V36 unified diff; `V35_WHOLE_REVIEW_GPT56.md`; `V35_WHOLE_REVIEW_CODEX.md`; `BS2A_CODE_GATE_GPT56_R6.md`; `BS2A_CODE_GATE_CODEX_R6.md`; relevant findings in both V34 whole-document reports; V30 protected slices.

Executed: absolute `cd` and `pwd`; V36 SHA-256; full unified V35→V36 diff; lexical absence inventories; independent V30 slice hashing and same-position comparison; class-count parser; non-citation lint; trace check; BS-2a component SHA-256; live BS-2a self-test; path-scoped git status.

I did not read `/Users/duhokim/NebulaMindData/`, fetch or inspect an image, execute Stage P/C, unblind, alter the reviewed draft or frozen v9, fill any slot, authorize BS-6, or re-derive any parked principal question. The only intended durable write is this report.

**CLEAR**
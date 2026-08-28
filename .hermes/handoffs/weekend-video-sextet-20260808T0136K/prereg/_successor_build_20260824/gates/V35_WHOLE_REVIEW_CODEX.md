# V35 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** The V35 subject matches the brief pin exactly, the three intended repair sites are substantively improved, the V30 preservation pins hold, the BS-2a component pin and both cited round-6 reports check out manually, and the class inventory remains 15/8. The line-120 antisymmetry repair is neither over- nor under-claimed, and line 592 correctly makes exclusive mediation a pre-freeze burden rather than pretending bypass detection exists. One evidentiary overclaim remains in the repaired BS-2a row: it still says a crash “fails closed, never a PASS” without the process-exit qualification both round-6 reports require. A valid receipt can print `MATCH` and then crash while emitting, so stdout-only integration can observe the success-looking token. The smallest repair is wording only and does not touch frozen v9 or change the normative slot inventory. The two principal-parked findings were not re-derived and remain correctly parked.

## Identity and exact comparison

Subject: `../PREREG_SUCCESSOR_DRAFT_V35_20260829.md`.

- Brief-pinned SHA-256: `b80d50afe076fe8d20c9fd1a6e6b5db63779dfc02ee46601667a67227e12fbdd`.
- Independently computed SHA-256: `b80d50afe076fe8d20c9fd1a6e6b5db63779dfc02ee46601667a67227e12fbdd`.
- **Comparison: MATCH — exact 64-hex equality over the named V35 bytes.**
- Independently computed V34 SHA-256: `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948`, matching the predecessor pin.
- Mechanical V34→V35 diff: retitle at line 1; replacements only at lines 120, 592, and 698; one appended V33→V34 trace row at line 865. No other byte moved.

## Numbered finding

### 1. MEDIUM / REPAIR-REQUIRED — §7 line 698 still overstates crash behavior by omitting the exit-status boundary

The repaired row still says:

> “no crash path is reachable from the builder (0 of 65,060 rows) and a crash fails closed, never a PASS.”

The builder-bound statement is supported at its stated scope: CODEX R6 reports a complete type/schema census of all 65,060 built rows and GPT56 R6 reports the same zero-off-schema result. The unqualified crash sentence is not at the exact strength of those reports.

Both reports disclose the same counterexample. With a valid authenticated receipt and an invalid `--emit-destination`, verification succeeds, the program prints the true `MATCH` summary, the destination write then raises `FileNotFoundError`, and the process exits 1. CODEX R6 lines 231–244 and GPT56 R6 lines 68–77 both say this is fail-closed only for a consumer that honors process exit status; a consumer that treats `MATCH` on stdout as success can be misled. CODEX's V34 report already required that qualification at lines 50–55. V35 repaired the pairwise-deletion attribution but left this second half of the same V34 finding unchanged.

This is an absence-surface defect: “never a PASS” silently means “never exit-status success,” but the document does not state that success is defined exclusively by exit status. The failure can occur while stdout already carries the component's success-looking `MATCH` token. The uppercase literal `PASS` does not occur in the component's output vocabulary, but natural-language “a PASS” in a gate row is a state claim, not a grep claim.

Smallest sufficient repair: replace the last sentence with the evidence-bounded form, for example: “No builder-produced row reached a crash in the 65,060-row census. Every observed crash exited nonzero; consumers must gate on exit status, because a post-verification emit failure can print `MATCH` before exiting 1.” This is a prose precision repair only; it does not change the predicate, frozen v9, a slot class, or any normative authorization rule.

## Adjudication of the three V35 repairs

### §1 line 120 — HELD, and not under-claimed

The new claim is exactly the algebraic consequence available here: under the exact mirror pair,
`χ(x) = (w(x) − w(mirror(x)))/2`, a spatially uniform parity-even additive preference cancels and contributes no centred dipole slope. V35 immediately says this is the whole of what the identity enforces. It then preserves the three non-cancelled routes: parity-odd raster response/upstream chirality, non-equivariant sample selection, and position-varying sensitivity coupled to an offset. Those routes are consistent with, rather than exceptions hidden by, the narrowed statement.

I manually inspected the cited `paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md` from the git object at `HEAD` because the working-tree path is not present. Its §2.1 gives the exact mirror identity and §2.3 names the upstream, selection, and sensitivity-gradient limits. Its §2.2 also contains the broader “biased or broken w … cannot create one” sentence that V35 expressly rejects. I therefore credit the algebra and §2.3 boundary, not that superseded broad sentence. The repair does not under-claim the identity: ensemble count swapping and `|χ(mirror(x))| = |χ(x)|` remain separately stated, while sky-position immunity is correctly denied.

### §6.2 line 592 — HELD; the false detection claim was not moved into BS-2k's mouth

V35 now expressly states that a bypassed observational read may leave no trace and that the log chain can remain valid. It claims no retrospective detection. “BS-2k must demonstrate exclusive mediation before freeze” is framed as an unfilled design/gate obligation, with inability to establish it making BS-2k unfillable and excluding the archive from the custody claim. That is the correct prevention-by-construction burden; it is not a claim that the log can prove an absence after the fact.

The surrounding construction is consistent: Clause 4 requires the gate to identify and test the raw-store boundary; Row A makes mediation failure void; Row B is the sole conforming byte path; BS-2k remains DESIGN and blocks BS-6. No present-tense accomplishment is laundered into the slot.

### §7 line 698 — pairwise/single-deletion repair HELD; crash clause does not

Manual report check, without using the quarantined citation linter:

- `BS2A_CODE_GATE_CODEX_R6.md` first line is CLEAR only for freezing the quality-predicate component, not filling BS-2a. It reports 26/26 strict single-code deletions, a filter-derived 325/325 pairwise result, and six literal AST-level pair mutations with real self-test reruns.
- `BS2A_CODE_GATE_GPT56_R6.md` has the same freeze-only scope and reports 26/26 literal single-check source deletions. It explicitly says it did not run all 325 pairs at round 6.
- V35 now distinguishes those evidence classes and no longer reads as though both seats literally executed all 325 source mutants. That portion is at the reports' exact strength.
- The component file independently hashes to `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`, exactly matching line 698.
- The remaining exit-status omission is Finding 1.

## Absence-surface attack ledger

I read all 886 lines. The original six-token seed (`never`, `nowhere`, `cannot`, `must not`, `in no case`, `none`) finds 77 occurrences on 68 lines in V35. I also broadened the sweep through the normative body to `no`, `nothing`, `without`, `only`, `exactly`, `every`, `all`, `any`, `exhaustive`, `forbidden`, `unable`, and `unreachable`, yielding 206 candidate lines through §7.1, then read the §8–§11 tail separately. For each candidate I distinguished a current factual absence from a blocked design requirement or normative refusal rule.

Disposition by construction surface:

- §1 identity negatives: exact-mirror algebra enforces only parity-even cancellation and mirror sign swap. V35 now keeps parity-odd/upstream/position-coupled routes visible. Held.
- §2 count/closure negatives: closed enums, total joins, external witness pins, exact-set comparisons, no caller answer parameter, and blocked unimplemented slots make these either executable checks or explicitly unfilled requirements. Held.
- §2.7 acceptance negatives: exact parent partition, closed reason vocabulary, evidence recomputation, and sign-blindness are requirements assigned to unfilled BS-2a/C2/E work, not represented as executed facts. Conditional handedness independence remains expressly unestablished. Held.
- §3–§5 statistic/verdict negatives: typed mask refusal, code-defined statistic, fixtures, and explicit unresolved guard inventory distinguish implemented code from required work. The caller-supplied authorization weakness was not re-derived; it remains parked. Held at its disclosed blocked status.
- §6 disclosure/custody negatives: human-conduct clauses are normative void rules; byte-path negatives depend on the unfilled exclusive-mediation construction and therefore cannot authorize execution. Line 592 now correctly says bypass detection is absent. Held as blocked covenant/design, not current achievement.
- §7 gate-state negatives: the BS-2a freeze-only scope, arbitrary-hostile-input limit, unfilled remainder, and BS-6 block remain visible. Pairwise evidence now holds; crash integration wording remains Finding 1.
- §7.1/§8–§11 closed-registry and “never evidence” statements remain either explicit registry requirements, historical testimony, or unresolved implementation inventory. The BS-2v/gain-control/VOID parked surfaces were not re-litigated.

The most important failed attack outside the changed lines was an attempt to turn line 592's “exclusive mediation” into a present factual guarantee. It does not: the slot remains DESIGN, its gate must fail if exclusivity cannot be established, and BS-6 remains blocked. The live defect is instead the unqualified success-absence claim in line 698.

## BS-2a, V30, counts, and machine checks

- BS-2a component pin: live `ref/bs2a_quality_gate.py` SHA-256 equals V35's full digest exactly.
- BS-2a status: `DESIGN, CLASS P — UNFILLED`; the quality predicate is freeze-cleared only. Missing C2 integrity verification, confidence threshold, retry/failure semantics, ledger schema, and transformed-cutout fixtures remain named.
- V30 §1 protected scope: V30 lines 131–133 and V35 lines 131–133 are byte-identical at the same line positions (276 bytes including newlines).
- V30 §2.7 protected sentence: V30 line 384 and V35 line 384 are byte-identical at line 384 (533 bytes including newline).
- `tools/prereg_counts.py`: 15 class P, 8 class E; 23 §7 rows, 22 with BS identifiers; only BS-2m claimed filled; prose matches the table.
- `tools/prereg_trace.py ... --check`: 34 computed transitions, 0 problems.
- `tools/prereg_lint.py`: exit 0, 15/8 and no non-citation inconsistencies. Citation output was quarantined and given no evidentiary weight.
- The appended V33→V34 repair announcement was checked manually against both R6 reports, the live component digest, and V34's actual diff. `FINDINGS_MAP.md` also carries the V34→V35 mapping to GPT56-V34-2 and CODEX-V34-1/3/4.

## Parked principal questions

I did not re-derive the missing BS-6 dependency edge or `require_authorization()` accepting caller-chosen bytes. Neither appears wrongly parked. Adding the dependency edge changes the normative class inventory from 15/8 to 16/8; changing authorization semantics touches frozen v9 and defines what authorizes this study. Neither is a wording-only repair that preserves normative content.

## Failed attacks / standing that held

1. V35 and V34 identities match their pins; V34→V35 changes only the four brief-declared locations.
2. The line-120 repair states exactly the mirror identity's consequence and preserves all three surviving routes.
3. The line-592 repair admits invisible bypass and makes exclusivity an unfilled prevention gate, not a log-detection claim.
4. The 325-case sweep is now identified as filter-derived; six literal pair mutants and GPT56's 26 literal singles are not conflated.
5. The component digest, freeze-only verdict scope, arbitrary-hostile-input limitation, and unfilled BS-2a remainder all match the two real R6 reports.
6. V30 protected bytes/positions and the 15/8 class counts remain unchanged.
7. Trace and all non-quarantined lint checks pass.
8. BS-6, Rows C2/E, and the first image byte remain blocked.

## Testimony and constraints

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or inspect an image byte, fill any slot, execute Stage P/C, unblind, change frozen v9, alter the subject, or mutate git.
- I treated my V34 report and both R6 reports as claims to attack, not as ground truth; pins, diffs, exact lines, and cited report contents were checked directly.
- The only durable write from this review is this report.

## Evidence ledger

Content read: `BRIEF_V35_REVIEW.md`; all 886 lines of V35; all of `V34_WHOLE_REVIEW_CODEX.md`; exact V34→V35 diff; V30 protected bytes; `BS2A_CODE_GATE_CODEX_R6.md`; `BS2A_CODE_GATE_GPT56_R6.md`; `FINDINGS_MAP.md`; the cited instrument paper's §2 from the `HEAD` git object.

Independent executions: V35/V34/V30/component SHA-256; exact diff; raw-byte and line-position comparison; six-token and broad universal-language censuses; class-count parser; trace check; lint with citation result quarantined; git-object retrieval of the cited paper.

**NOT CLEAR**
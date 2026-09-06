ACCESS_SHA=c232b4ceb32be109e73cfb247ed911a6080f893a787eb28a233ad0a84104deb3
PACKET_SHA=1119e0ee25b89efe6fd63580992685c200239647555516ed43d70d5496ccb3a5
GATE=PREREG_UNSOUND
LEAK=Provenance is a separate concern; dependence on chosen/fitted inputs is a plausible hypothesis, and conventional cosmology a plausible benchmark, but no directional prediction or preferred outcome is disclosed.
CONSEQUENCE_VISIBLE=CENSUS_AUDIT_FAILED suppresses the tally: “No tally is filed; report which.” This is procedural consequence, not an exposed empirical stake.
ORIGIN_PURPOSE=Independent re-classification and dispute handling are visible: “Every input's `origin` is classified independently by both seats.” Its eventual interpretive use cannot be stated from the packet.
C5_EXECUTABLE_UNDER_SCOPE=YES — C4(iii) expressly permits the five C5 harness commands and their loads; all five exited 0 on this host.
NO_MASKED_STAGE=YES

1. OUTCOME CLASSES — packet answers first, then Q1

This is a design verdict, not a census result. Section 10 supplies no evidence for my findings. I opened no gate report and ran no corpus derivation. My packet answers were recorded before opening the master; the following preserves their distinction between what is disclosed and what can only be conjectured.

Q5. CAN YOU TELL, FROM THE PACKET ALONE, THAT ANY OUTCOME IS MORE CONSEQUENTIAL THAN ANY OTHER — to the lane, to anyone?

Procedurally, yes: the audit-failure class says “No tally is filed; report which.” The complete class instead says “Report the full tally with its denominator”. No sentence identifies an empirical outcome as more desirable or damaging to the lane or a person. “No tier, warrant token, standing or stamp moves.” Consequently I do not encode the broad question as an unqualified NO.

Q6. CAN YOU STATE, FROM THE PACKET ALONE, WHAT THE RECORDED `origin` OF AN INPUT IS FOR — what the study does with it after you record it?

Only its verification and dispute use. “Every input's `origin` is classified independently by both seats.” C6 requires the auditor's “re-classified `origin` of each of its inputs, and `MATCH` or `MISMATCH` against the sealed record.” Disagreements affecting more than 10% of included claims stop the study. I cannot state a downstream provenance summary, comparison, or interpretation mapping. My packet-first answer's “cannot” concerned that ultimate use, not the explicitly disclosed checks.

Q3. WHAT CAN YOU INFER ABOUT WHAT THE LANE EXPECTS OR HOPES THE CENSUS WILL SHOW?

- “The reproduction verdict and the provenance fields are recorded separately.” Together with the seven origin values and independent checking, this suggests an interest in numerical successes that nevertheless depend on chosen, fitted, imported, or undocumented inputs. It does not establish that the lane expects such cases to dominate or wants them to.
- “The cosmological rows are the Planck 2018 TT,TE,EE+lowE+lensing baseline.” This exposes the subject area and suggests conventional cosmology as a possible benchmark. It does not identify a governing comparison hypothesis or a preference against that benchmark.
- “The arithmetic group” receives a complete audit, whereas other claims are sampled. This reveals asymmetric verification effort for resolved arithmetic, equally covering successes and failures; it does not identify a preferred sign.

I could conjecture a stake concerning the independence of numerical predictions. I could not reconstruct a specific pattern, its desired direction, a threshold for support, or the mapping from provenance to a conclusion. The master’s interpretation was not used to upgrade those conjectures into packet findings.

Q1. DOES SECTION 3's DEFINITION, AS WRITTEN UNDER OPTION (c), MAKE EVERY DECLARED OUTCOME REACHABLE AND KEEP THE REPRODUCTION QUESTION DECIDABLE?

The status-based option (c) resolves the central chosen-input tension. All six per-claim classes have witnesses, and the precedence resolves overlapping terminal conditions. But the whole operative design is not total: an imported-value evidence conflict and a candidate-exclusion gap remain. Thus YES for abstract outcome reachability; NO for an unconditional claim that every allowed case can traverse all required controls.

Concrete constructed claims below are test fixtures, not assertions about unread corpus papers:

| Claim and inputs | Unique per-claim outcome | `rests_on` under the printed rule |
|---|---|---|
| “We choose a = 2. Our result is y = a + a = 4.” | `REPRO_WITHIN_STATED_PRECISION` | `USES_CHOSEN` |
| Same recipe and input, but result printed as 5 | `REPRO_FAILED` | `USES_CHOSEN` |
| “We fit a = 2 to the observations. Our result is y = a + a = 4.” | `REPRO_WITHIN_STATED_PRECISION` | `USES_FITTED` |
| a = 2 printed in the claiming paper and explicitly adopted from B; y = a + a = 4 | `REPRO_WITHIN_STATED_PRECISION` | `USES_IMPORTED` |
| y = a + b, a cited to a non-enumerable B, b unprinted and uncited | `REPRO_BLOCKED`, ahead of absence | `USES_UNDECLARED` if the absent b has no stated origin; both records remain listed |
| y = a + a, a unprinted and uncited | `REPRO_INPUT_ABSENT` | `USES_UNDECLARED` |
| Fully specified computation with all inputs stated that exceeds 120 seconds | `REPRO_NOT_EVALUABLE` | Computed from those inputs, e.g. `USES_CHOSEN` |
| “Our predicted duration is 4 s,” with no producing procedure or identifiable input record | `REPRO_NO_DERIVATION_STATED` | `NOT_COMPUTED` |

A claim with both a blocked input and unavailable machinery files BLOCKED, not two classes. The precision and asymmetric-uncertainty rules separate numerical success from failure for ordinary scalar finite values. The bounded attempt makes the filing procedure terminate; it does not promise to decide the mathematical truth of a timed-out computation.

All eight study classes also have witnesses: a nonempty all-arithmetic tally with audit PASS; a tally containing one blocked claim with audit PASS (PARTIAL); an audit mismatch (AUDIT_FAILED); both seats failing C5 twice (NO_CLASS); a surviving inclusion/input-list disagreement; a surviving outcome disagreement; an origin disagreement affecting 1 of 5 claims; and C5 passing in one seat while failing twice in the other (CONTROL_SPLIT). A zero denominator explicitly files PARTIAL. A partial tally with an audit failure satisfies two predicates but files only AUDIT_FAILED by precedence. An origin dispute above threshold stops before C6, so its unreached audit is NOT_RUN, not a competing result. INCONCLUSIVE is genuinely reachable through PARTIAL; it does not require numerical failure.

D1 — imported value and origin evidence disagree. Substantive.

Verbatim sentence (§2):

> **A value the paper does not print but traces to a named source that is itself an enumerable text in `R3C2_CORPUS_MANIFEST.md` is
> classified `PRINTED` from that source, with `origin` `IMPORTED`, `origin_evidence` `ORIG_CITATION` cited to the named
> source's file and line, and the value machine-matched there — **only when such a match exists; a cited value that does
> not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest,
> files `REPRO_BLOCKED` under §3.**

Hardest case: claiming paper A says “Use a from B; our result is y = a + a = 4.” Pinned enumerable B says “We choose a = 2.” Arithmetic uniquely succeeds and §2 prescribes USES_IMPORTED. But the mandatory origin quotation from B establishes CHOSEN, not a citation; C3's evidence semantics do not establish the prescribed IMPORTED origin. Quotation matching can pass while semantic re-classification rejects it. Filing BLOCKED would contradict the matching-value condition; filing CHOSEN contradicts §2. This is an evidence-location conflict, not a reason to abandon option (c).

Exact replacement:

> A value absent from the claiming paper but traced there to a named enumerable source in `R3C2_CORPUS_MANIFEST.md` is `PRINTED` with `origin` `IMPORTED` when its value machine-matches the cited line in that source. The record's `source_file` and `source_line` identify that value line; its `origin_evidence` uses `ORIG_CITATION` and quotes the claiming paper's sentence naming the source. If the source is not enumerable or the value does not match at the cited line, file `REPRO_BLOCKED`. Classify the import relative to the claiming paper, independently of how the cited source obtained the value.

D2 — exclusion schema is not exhaustive. Substantive.

Verbatim sentence (§3):

> **The exclusion ledger's
> `kind` is one of `EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`, `ATTRIBUTED_NOT_DERIVED`.**

“For this calculation we set a = 2” is an author-specified input, not an asserted result, an attributed value, or any other permitted exclusion kind. The candidate must be listed, but neither inclusion under §1 nor a truthful exclusion code is available. This can force a C1 failure or distort the denominator. It is a candidate disposition gap, not a seventh per-claim outcome.

Exact replacement:

> The exclusion ledger's `kind` is one of `EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`, `ATTRIBUTED_NOT_DERIVED`, `NOT_ASSERTED_RESULT`. Use `NOT_ASSERTED_RESULT` for a numeral not asserted as the paper's own result and not covered by an earlier excluded kind, including an author-specified input; cite the passage and state why it fails §1. This exclusion never removes that value from the input ledger of an included claim that uses it.

Apply the additional kind to the C1 validator and rebuild and repin its consumers; a prose-only change would not repair executability.

2. CONTROLS — Q2

Q2. IS THE PROVENANCE FIELD CHECKABLE RATHER THAN ASSERTED?

Yes, as cited, independently reviewed evidence; no, as a machine-guaranteed semantic classification. The text explicitly acknowledges the distinction. A plausible wrong record is:

```json
{
  "claim_id": "C1", "input_id": "a", "symbol": "a",
  "status": "PRINTED", "origin": "CHOSEN",
  "origin_evidence": {
    "reason_code": "ORIG_CHOICE_STATED",
    "source_file": "A.txt", "source_line": 1,
    "verbatim": "We choose a = 2 from B."
  },
  "derived_from": [], "value": "2",
  "source_file": "A.txt", "source_line": 1
}
```

For a fixture whose A.txt line 1 is exactly that quotation, the value and quotation match, and the reason-code/origin pair is legal. Those stated machine checks cannot reject the misclassification. The sentence names an external source, so C3's precedence requires IMPORTED. The second seat can catch this by independently applying that precedence. C6 re-classifies every input of every arithmetic-group claim, so an arithmetic success with this record receives a further semantic check. Non-arithmetic records are not all re-derived: outside the sample, that additional catch is not guaranteed. If every relevant reader makes the same mistake, the record can survive, as the master admits. This is a written adversarial fixture, not a claim that I executed the restricted validator.

`root_origins` and `rests_on` being computed prevents direct assignment of those fields; it cannot make a mistaken root classification true. Parent completeness still depends on source review.

| Control | Required evidence and exact code |
|---|---|
| C0 | Independent exhibition and verification; `C0_REACHABILITY=PASS|FAIL|NOT_RUN` |
| C1 | Counts, ledgers, printed census runs and exit status; `C1_DENOMINATOR_PRINTED=PASS|FAIL|NOT_RUN` |
| C2 | Printed C3 validator artefact; `C2_INPUT_LEDGER=PASS|FAIL|NOT_RUN` |
| C3 | Validator plus lane merge/compute outputs, every run exit 0; `C3_NO_SUBSTITUTION=PASS|FAIL|NOT_RUN` |
| C4 packet | Pinned builder output and packet pin; `C4_PACKET_REDACTED=PASS|FAIL|NOT_RUN` |
| C4 isolation | Printed directory/path list and dispatch inventory; `C4_SEAT_ISOLATION=PASS|FAIL|NOT_RUN` |
| C5 | Five live commands and dispatch pin comparison; `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN` |
| C5b | Marked path list; `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN` |
| C6 | Printed `C6_AUDIT.json`, no mismatch/incompleteness; `C6_AUDIT_SAMPLE=PASS|FAIL|NOT_RUN` |

A bare PASS token does not satisfy these controls. C4/C5b nevertheless permit PASS on an incomplete self-authored list; they expressly certify the list, not actual non-access. Unreached controls are explicitly NOT_RUN. A missing audit seed produces NOT_RUN and AUDIT_FAILED, not a vacuous PASS.

D3 — the additional no-fallback control has no result code or failure route. Substantive.

Verbatim sentence (§9):

> Lane-side procedure, not the seat's: the no-fallback control is the provider log showing
> no fallback line for the seat's session, checked by the lane owner; a one-page check sheet `R3C2_CHECK_SHEET_<date>.md`
> in plain words with source lines is written by the lane owner after the tally; the lane owner runs `r3c2_lane_tools.py` (sha256 `8e990c7a22fb4b093d5e74218e9bfcee4b108c52bbc2df615ed3b6b2aaefa848`; merge, then compute) after both seats exit and re-runs every script; a
> critic note precedes any ruling.

Exact replacement:

> Lane-side procedure: after each seat exits, the lane owner prints the complete provider log for that session and `C5C_NO_FALLBACK=PASS|FAIL|NOT_RUN`. PASS requires the complete session log and no fallback event; FAIL means a fallback event or missing/incomplete session log; NOT_RUN means the session was not reached. This is a per-seat control governed by §4's two-attempt NO_CLASS/CONTROL_SPLIT rules, with their control range extended through C5c. After the tally, the lane owner writes `R3C2_CHECK_SHEET_<date>.md` with source lines, prints the pinned lane tool's merge and compute runs, and re-runs every script; a critic note precedes any ruling.

3. CIRCULARITY

The inclusion rule contains no comparison-model test. Both inclusion and exclusion must be visible, independently classified, reconciled under a stopping rule, and audited against all sources. A contrary claim cannot be quietly excluded while faithfully following those obligations. D2 is a real pressure toward omission or mislabelling and must be repaired. Source selection remains a fixed boundary, not proof of unbiased selection: I did not open the corpus manifest or sources under the access restriction.

Origin labels retain semantic judgement and the packet reveals that provenance receives special care. That alone does not expose the hidden mapping. The frozen interpretation protocol separates interpretation from enumeration, but cannot prove the author's ignorance or prevent identical human misclassification.

D4 — C6 discloses earlier outcomes before claiming blind re-derivation. Substantive.

Verbatim opening of the C6 sentence:

> A third independent seat **first audits the full candidate and
> exclusion ledgers against every pinned source** — completeness, not just outcomes — then re-derives, **without sight of earlier work and re-classifying every input's `origin` from the pinned sources**:

C1 makes `outcome`, `printed_value`, and `reproduced_value` part of that full candidate ledger. Reading it first exposes earlier answers. The audit can still be useful, but cannot satisfy its stated independence condition.

Exact replacement for that opening, leaving the subsequent sampling formula in place:

> A third independent seat first audits a projection of the candidate and exclusion ledgers containing only candidate identifiers, source locations, numerals, inclusion decisions, and exclusion kinds against every pinned source. A custodian computes the audit set by the following formula and supplies its union as sorted claim identifiers without group labels. Before seeing earlier outcomes, reproduced values, input ledgers, or provenance classifications, the auditor records and seals its own re-derived outcomes and input classifications for those claims. Only then does the custodian reveal the sealed earlier records for MATCH/MISMATCH comparison:

4. THE BLIND

I independently removed §0/§7/§8/§10 and the marked redaction spans from the master; the resulting operative body exactly matched the delivered packet body. The embedded master digest also matches ACCESS_SHA. This checks the delivered extraction, not execution of the pinned builder's forbidden-string assertion. I did not open or run the builder because it is outside the permitted file-content reads and would rewrite deliverables.

The master honestly limits forbidden-list detection to enumerated strings and admits procedural consequences remain. C4's older confinement text is also candid that the blind is procedural and cannot establish non-access. The new residual overstates that protection.

D5 — command invocation is not a closed content boundary. Substantive.

Verbatim sentences (C4):

> Why the line is drawn here: what the seat is told to run cannot leak the study's content, because the packet's own text is
> reviewed and blinded before dispatch; what the seat decides to open can.

> **Residual, stated:** the manifest digest proves the pinned
> environment did not change between pinning and use; it does not prove the environment is minimal or free of startup code — the
> seat's confinement (read-only to the seat, no reach beyond (i)–(ii)) bounds what such code could touch, and the dispatch record
> says what was pinned.

The §9 wrapper contains a seat-supplied `<command>`. A seat can substitute a child that reads the lane master, such as `/bin/cat /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md`. That is plainly a chosen access, yet the blanket “whatever those commands themselves invoke or load” provides a competing authorization. Likewise, pre-existing startup code can read outside the pinned directory. A pin identifies bytes; it does not prove their harmlessness. Read-only access by the seat does not stop another host process changing a user-writable environment. Two equal snapshots do not prove continuous immutability.

Exact replacement for both quoted sentences, and append the same scope qualification to C5b and the brief:

> Printed commands are permitted to execute, but this permission does not authorize arbitrary data access. Every seat-selected placeholder, child command, import, or data path remains a seat choice subject to (i)–(ii), including choices passed through the timeout wrapper. Runtime loads may use the pinned execution environment and system runtime needed by the mandated commands; data reads outside (i)–(ii) are forbidden, including those initiated by startup code. Before dispatch, a confinement test must exhibit that the mandated commands run and that a wrapped read of the lane master is denied. Pin comparisons establish equality of the checked bytes at the check times, not continuous immutability or absence of startup code. Packet redaction does not establish that executable code cannot disclose study content; until confinement is verified, C4 certifies only the dispatch inventory and reported path list.

The added principle currently makes C5 executable; this defect concerns the strength and closure of the blind, not whether `/usr/bin/shasum` is allowed.

5. THE SEAL

The receipted relay is sound as a design for binding records. P binds protocol hash and commit before limb A; T binds the named tally files and commit before opening the protocol. Independent re-hashing, both receipts, and all four values must be printed. Missing receipts or mismatches void the comparison and file AUDIT_FAILED. The post-T external seed prevents the lane choosing a sample through tally formatting.

This establishes a checkable chronology, not the lane owner's lack of advance expectations. The text admits that limit. I did not inspect the interpretation protocol or actual receipts, and certify no executed seal. No design repair found here.

6. FAIRNESS

REPRO_FAILED explicitly requires “unreproduced from the stated inputs,” not “error”; the seat brief applies that wording to negative outcomes generally. BLOCKED, ABSENT, NO_DERIVATION_STATED and NOT_EVALUABLE describe limitations without declaring a paper wrong. WITHIN_STATED_PRECISION does not claim exact mathematical equality.

The rename check found REPRO_EXACT only in the §3 rename notice (line 118) or under §10 headings: lines 553, 718, 774, 819, 842, 868, 886, 914, 943, 965, 973, 984, 998, 1007 and 1009. No governing old-token reference remains. The separate rename audit was unnecessary and unopened.

D6 — DERIVED_ONLY asserts more than its membership definition. Substantive under the requested class-name test.

Verbatim rule (§3):

> *(Master only — the rule the script implements: `DERIVED_ONLY` when every root origin is `DERIVED`, `STANDARD` or
> `MEASURED`; otherwise the most severe root origin present, in the fixed order `USES_UNDECLARED` > `USES_IMPORTED` >
> `USES_FITTED` > `USES_CHOSEN`.

A claim using only an author's measured a = 2 files DERIVED_ONLY although no derivation of a exists. This is the exposed interpretation tally's label, not merely a formatting choice.

Exact replacement for that rule:

> Master only — the rule the script implements: `ROOTS_DERIVED_STANDARD_OR_MEASURED` when every root origin is `DERIVED`, `STANDARD` or `MEASURED`; otherwise select the first root category present in the fixed reporting order `USES_UNDECLARED`, `USES_IMPORTED`, `USES_FITTED`, `USES_CHOSEN`.

Update the computed token and interpretation consumer together and repin them, preserving membership. This does not change option (c) or the numerical outcome classes.

7. STALL / EXECUTABILITY — Q4 and Q7

Q4. CAN ANYTHING THE DOCUMENT DESCRIBES NOT BE EXECUTED AS DELIVERED?

Yes: D1 prevents a semantically compliant imported record, D2 prevents a truthful disposition for an ordinary input numeral, and D4 cannot provide the claimed blind audit in its specified order. These are design execution failures, not proof of missing scripts. The five C5 commands run successfully.

Checks performed and limits:

- Read the complete master and packet; opened the explicitly permitted current brief and V23 design for scope comparison. No other study document was opened. File-content access to `r3c2_manifest.py` was limited to the explicitly requested copy/hash/execution; C5 necessarily reads the specified runtime files.
- Checked filesystem metadata, without opening contents, for `r3c2_ledger_tools.py`, `r3c2_lane_tools.py`, `r3c2_build_seat_packet.py`, `r3c2_manifest.py`, `r3c2_timeout.py`, `R3C2_SEAT_PACKET.sha256`, `R3C2_CORPUS_MANIFEST.md`, and `R3C2_INTERPRETATION_PROTOCOL_20260904.md`: all are regular files. This does not verify their pins, contents, git commitment, or behaviour. No missing named fixed artefact was established.
- C1 `census`, `census ... final`, C2/C3 `validate`, lane `merge` and `compute`: checked every printed invocation and the specified fields/counts against the prose. Placeholders are explicitly resolved, and `sources_dir` is fixed to `.`. Runtime schema enforcement, alternate-parent computation, cycle rejection, and root/tally output remain unverified because reading/executing those tools would exceed the file-access restriction.
- Builder command: checked text and independent packet extraction, not builder execution or forbidden-list implementation. The SHA pin file and corpus manifest were not opened, so individual source delivery and all source pins remain unverified, not declared missing.
- Timeout invocation: checked its declared 120-second cap, 124 timeout status, and child-status reporting. Did not run the restricted wrapper. No actual timeout or child-failure propagation is certified.
- `C6_AUDIT.json`, candidate/exclusion/input ledgers, receipts, dispatch inventory, provider session log, and dated check sheet are prospective run artefacts. Their absence before any run is not a missing-delivery finding. The unnamed administrative dispatcher is explicitly not a packet-executable command.

These limits follow the instruction not to open additional files. They prevent a blanket certification that every implementation matches its description; they do not erase the design counterexamples above.

Live C5 execution:

Copied only the authorized manifest script to `/var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/r3c2_v24g_codex_kyw8bci0` and ran all five commands there in order. Its SHA256 was `19a8ce4750bb47655868ef15b55f2b168833147b460c03ad56f84dd3c9bc56f2`, matching the master. The display wrap inside command 2 was rendered as the semicolon-separated command; no pipeline was introduced.

```text
$ /usr/bin/python3 -E --version
Python 3.9.6
EXIT_CODE=0

$ /usr/bin/python3 -E -c "import sympy; print(sympy.__version__)"
1.14.0
EXIT_CODE=0

$ /usr/bin/shasum -a 256 /usr/bin/python3
b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9  /usr/bin/python3
EXIT_CODE=0

$ /usr/bin/python3 -E -c "import site; print(site.getusersitepackages())"
/Users/duhokim/Library/Python/3.9/lib/python/site-packages
EXIT_CODE=0

$ /usr/bin/python3 -E r3c2_manifest.py /Users/duhokim/Library/Python/3.9/lib/python/site-packages
FILES=20637
MANIFEST_SHA256=1b5463c1072994b2c458d8cbe73a931d23c4b9b10cee3dfd789989d59d9f03ed
EXIT_CODE=0
```

This was a live host execution, not a reproduction-seat sandbox certification. No prelaunch dispatch pin was inspected; therefore I do not award C5_HARNESS_PINNED=PASS.

Q7(a). C5_EXECUTABLE_UNDER_SCOPE=YES. Governing text:

> **(iii)** execute the commands this document prints verbatim — the C1
> `census` runs, the C2/C3 `validate` runs, the five C5 harness commands, and the §9 wrapper invocations — together with whatever
> those commands themselves invoke or load, because executing a printed command is the instruction, not a scope choice.

Read as the specific exception to C4's earlier general restriction, this permits Python, shasum, SymPy dependencies and the manifest's site-packages reads. C5b adopts C4's three clauses. The brief says “execute the commands the packet prints verbatim, with whatever they themselves load” and makes the packet govern any conflict. No needed C5 path remains closed by the current principle. The earlier prefix-bound versions are not the operative rule.

Q7(b), D3 check. NO_MASKED_STAGE=YES for the mandated command forms. There is no shell pipeline in operative C1–C5 or §9. The historical `git show ... | shasum` is under §10 and is not a present mandate. C5 command 5 is one Python invocation, whose exit 0 I observed directly. The timeout wrapper necessarily starts a child, so “single process” must mean one top-level command with propagated status, not literally one OS process. An arbitrary shell pipeline can still be supplied through `<command>`; none is mandated, and D5 addresses that uncontrolled choice. Failure propagation inside the other uninspected scripts remains unverified.

Q7(c). The principle now admits the host's user site, including dependencies beyond SymPy. It does not itself close the startup/import-path hole or make that user-writable directory immutable. It is not too tight for the five observed commands. It consistently echoes the same broad permission in C4, C5b and the brief, including the chosen-child ambiguity in D5. No additional actual startup-file contents or sandbox rules were inspected.

D7 — one operative interpreter command lacks the promised -E. Substantive for the tested invocation.

Verbatim sentence (C4):

> Build
> command, run from this directory: `/usr/bin/python3 r3c2_build_seat_packet.py`; expected first line of output
> `C4_PACKET_REDACTED=PASS`, then the master and packet digests.

Exact replacement:

> Build command, run from this directory: `/usr/bin/python3 -E r3c2_build_seat_packet.py`; expected first line of output `C4_PACKET_REDACTED=PASS`, then the master and packet digests.

All other printed operative Python commands carry -E. This omission does not make C5 unexecutable, but disproves “every printed interpreter command carries -E.”

Q7(d). Actual V23 comparison, not the narrated history:

The permitted V23 file hashes to `55b466fadf8ca75f4894f97721da86584057ddc4d15c15ca1739c67ff6333c6f`. A direct unified diff shows these changes:

- Header/version/signature-status wording.
- `-E` added to both C1 invocations, C2 and C3 validation, lane merge and compute, and §9's timeout invocation.
- C4's new scope principle and residual; manifest script added to the dispatch inventory.
- C5 expanded from three commands to five, shasum path-qualified, Python invocations given -E, site-path and whole-directory digest output added, manifest script pinned, no-pipeline statement added, and PASS conditioned on dispatch path/digest agreement and loud failures.
- C5b now adopts C4's scope categories and load/path-list distinction.
- §10's V23 row changed, a V24 row added, and §10.18 appended. These are documentary differences, not evidence for this verdict.

No other master differences appeared. In particular, sections 1–4's outcome/provenance definitions, C6, §7 and §11 did not change. The current brief contains the scope echo, manifest-script inventory and final census -E invocation; no historical V23 brief was supplied for a bytewise brief diff. The current brief SHA256 is `379d1014ad9093e3af7968f733ebe709301aa31c99a64793c615999be5457187`. Thus “nothing else” is not an accurate description of the master diff beyond C4/C5b/brief alone.

COSMETIC C1 — literal process wording. The sentence “Every mandated command in this document is a single process whose exit status is the control's; no mandated command is a shell pipeline, because a pipeline's exit status is its last stage's and an upstream failure can be masked.” overstates OS process count for the wrapper, though the intended exit-status discipline is clear. Exact replacement: “Every mandated command is one top-level invocation whose exit status is recorded for its control; wrappers propagate child failure and timeout statuses, and no mandated command is a shell pipeline.” This clarification alone changes no filed class, passability, reachability, conclusion, or tested value.

The live C5 scope repair succeeds. The gate remains UNSOUND because the imported-evidence rule, candidate schema, audit blindness, and scope-boundary claims still require substantive repair; successful harness execution does not resolve those design defects.

R3C2_V24G_GATE_COMPLETE

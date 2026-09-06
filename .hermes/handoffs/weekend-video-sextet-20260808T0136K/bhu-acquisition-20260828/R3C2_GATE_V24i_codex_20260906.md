ACCESS_SHA=9c4b873d4281419a93b8aac9208e5a5de22481217fdd124b1dcfa6a7ae4d88be
PACKET_SHA=24da8b8e5dcee0196b18eb9541f3bb5fc1086d23ac608b02d3ecdfb3a739d529
GATE=PREREG_UNSOUND
LEAK=Provenance matters and may be compared with reproduction; no direction, comparison model, preferred outcome or empirical stake is reconstructible.
CONSEQUENCE_VISIBLE=Procedural only: CENSUS_AUDIT_FAILED says “No tally is filed; report which.” No empirical outcome is identified as weightier to the lane.
ORIGIN_PURPOSE=CANNOT_STATE
C5_EXECUTABLE_UNDER_SCOPE=YES — C4(iii) expressly permits the five C5 commands and their automatic loads; all five exited 0 here.
NO_MASKED_STAGE=YES

Packet-first answers, recorded before reading the master:

Q5. No sentence identifies a reproduction outcome as more consequential to the lane or anyone. “No tier, warrant token, standing or stamp moves” disclaims those consequences. Procedural consequences remain visible, including the quoted no-tally sentence; the header distinguishes these from empirical stakes.

Q6. I cannot state the substantive use of origin after recording. I can state its administrative use: independent classification, audit and dispute handling. The packet says “Provenance is transitive” and requires “re-classifying every input's `origin` from the pinned sources”. Neither reveals the eventual provenance summary or its interpretive use. CANNOT_STATE concerns that substantive purpose, not an inability to read the audit instructions.

Q3. “The reproduction verdict and the provenance fields are recorded separately” and “Provenance is transitive” suggest interest in comparing mechanical reproduction with input provenance. The unusually detailed taxonomy, quotation checks and disagreement threshold reinforce that inference. The closed list also identifies a cosmological context: “The cosmological rows are the Planck 2018 TT,TE,EE+lowE+lensing baseline.” None supplies a predicted relationship, preferred provenance category, comparison-model preference, or lane hypothesis. A possible provenance/reproduction comparison is an inference, not a recovered hypothesis.

This is a design gate, not a reproduction result. Section 10 supplied no evidence for my verdict. No gate file was searched for or opened. Examples below are constructed realistic claims, not assertions about corpus passages I was forbidden to open.

1. OUTCOME CLASSES — Q1

Q1: DOES SECTION 3's DEFINITION, AS WRITTEN UNDER OPTION (c), MAKE EVERY DECLARED OUTCOME REACHABLE AND KEEP THE REPRODUCTION QUESTION DECIDABLE?

The core option-(c) arithmetic rule does. The unqualified end-to-end answer is NO because the imported-input evidence rule can prevent a valid ledger for an otherwise decidable claim. This is an evidence-rule defect, not a reason to reopen option (c).

Concrete reachability witnesses:

- A paper states “We choose a = 2; y = 3a = 6.” Arithmetic uses a regardless of its choice: REPRO_WITHIN_STATED_PRECISION, root CHOSEN, rests_on USES_CHOSEN. If it prints y = 9 instead, REPRO_FAILED, still USES_CHOSEN.
- “Our fit gives a = 2; y = 3a = 6” gives REPRO_WITHIN_STATED_PRECISION and USES_FITTED. Recording a fitted value does not require refitting it.
- A paper states y = 3a = 6 and imports a from an enumerable source whose cited line says “We adopt a = 2 from Smith.” A matching value and citation evidence give REPRO_WITHIN_STATED_PRECISION and USES_IMPORTED.
- The same required value cited only to an unpinned source gives REPRO_BLOCKED and USES_IMPORTED. If a second required input is absent, both terminal conditions hold, but precedence files only REPRO_BLOCKED.
- A required a neither printed nor attributed gives REPRO_INPUT_ABSENT; with no declared provenance its root is UNDECLARED and rests_on USES_UNDECLARED.
- A fully specified numerical procedure requiring unavailable machinery, or exceeding the cap, gives REPRO_NOT_EVALUABLE; printed chosen inputs retain USES_CHOSEN.
- “Our calculation yields 6,” without operations, gives REPRO_NO_DERIVATION_STATED; an empty ledger gives NOT_COMPUTED.

All eight study classes have distinct filing witnesses: successful controls and a nonempty all-arithmetic tally with audit PASS give CENSUS_COMPLETE; one audited blocked claim gives CENSUS_PARTIAL; an audit mismatch gives CENSUS_AUDIT_FAILED; repeated common control failure gives R3C2_NO_CLASS; surviving inclusion/input disagreement gives CENSUS_DENOMINATOR_DISPUTED; surviving outcome disagreement gives CENSUS_OUTCOME_DISPUTED; two affected claims out of ten with disputed origins give CENSUS_ORIGIN_DISPUTED; one seat passing and another repeatedly failing a control gives CENSUS_CONTROL_SPLIT. An empty denominator also gives CENSUS_PARTIAL. Thus INCONCLUSIVE is genuinely reachable.

A tally with one blocked claim and an audit mismatch satisfies the raw PARTIAL and AUDIT_FAILED predicates; precedence files only AUDIT_FAILED. I found no double filing after precedence for these witnesses. This is abstract reachability, not a claim that the unopened fixed corpus realizes every witness.

D1 — imported-value evidence conflicts with its mandatory origin.

Verbatim operative sentence:

“A value the paper does not print but traces to a named source that is itself an enumerable text in `R3C2_CORPUS_MANIFEST.md` is
classified `PRINTED` from that source, with `origin` `IMPORTED`, `origin_evidence` `ORIG_CITATION` cited to the named
source's file and line, and the value machine-matched there — **only when such a match exists; a cited value that does
not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest,
files `REPRO_BLOCKED` under §3.**”

Hard case: claiming paper A directs y = 3a to paper B; B's cited line says only “We choose a = 2.” The arithmetic gives 6. Section 2 mandates IMPORTED/ORIG_CITATION with evidence at B, but B supports CHOSEN, not a citation. C3's rule cannot honestly encode that mandated record. BLOCKED is also false: the value matches an enumerable source. The intended pair is REPRO_WITHIN_STATED_PRECISION / USES_IMPORTED, but a compliant evidence record is unavailable.

Exact replacement:

“A value absent from the claiming paper but traced there to a named enumerable source is PRINTED when its value machine-matches that source's cited line. Record origin IMPORTED and ORIG_CITATION evidence at the claiming paper's sentence naming that source; record value, source_file and source_line at the supplying source's matching line. The two evidence locations may differ. If the source is not enumerable or the value does not match, file REPRO_BLOCKED. Classification as IMPORTED describes the claiming paper's use of the value, irrespective of its origin within the supplying source.”

2. CONTROLS — Q2

Q2: IS THE PROVENANCE FIELD CHECKABLE RATHER THAN ASSERTED?

YES as a cited, independently reviewed classification; NO as a machine proof of semantic correctness. Consider this deliberately wrong but plausible ledger record against a hypothetical matching source line:

```json
{"claim_id":"c1","input_id":"a","symbol":"a","status":"PRINTED","origin":"CHOSEN","origin_evidence":{"reason_code":"ORIG_CHOICE_STATED","source_file":"paper.txt","source_line":10,"verbatim":"We choose a = 2 from Smith (2020)."},"derived_from":[],"value":"2","source_file":"paper.txt","source_line":10}
```

The value, quotation substring, schema and CHOSEN/reason-code pairing can all satisfy the described validator. The wrong step is precedence: an external attribution requires ORIG_CITATION/IMPORTED. The second seat can catch it by independently assigning IMPORTED; the mismatch is retained, not reconciled. C6 reclassification catches it on every arithmetic claim and on sampled non-arithmetic claims. If every relevant reader makes the same mistake, no described machine mechanism catches it. The master expressly acknowledges this limit. Computed root_origins/rests_on prevent hand-written summaries, not incorrect premises.

C0 requires an exhibition and independent verification; C1 printed counts and census runs; C2/C3 printed validation (plus lane merge/compute); C4 a path list and builder/dispatch evidence; C5 live outputs; C5b marked paths; C6 a printed audit JSON. Their named codes carry PASS/FAIL/NOT_RUN. C4/C5b can pass an incomplete self-reported list, explicitly by design; they are not proofs of all access. Unreached limbs are NOT_RUN, and a reached audit lacking a seed cannot silently pass.

D4 — no-fallback control lacks a code and filing route.

Verbatim sentence:

“Lane-side procedure, not the seat's: the no-fallback control is the provider log showing
no fallback line for the seat's session, checked by the lane owner; a one-page check sheet `R3C2_CHECK_SHEET_<date>.md`
in plain words with source lines is written by the lane owner after the tally; the lane owner runs `r3c2_lane_tools.py` (sha256 `8e990c7a22fb4b093d5e74218e9bfcee4b108c52bbc2df615ed3b6b2aaefa848`; merge, then compute) after both seats exit and re-runs every script; a
critic note precedes any ruling.”

Unlike C0–C6, the named no-fallback control supplies neither its own three-valued result nor a failure disposition.

Exact replacement for that sentence:

“Lane-side C5c is C5C_NO_FALLBACK=PASS|FAIL|NOT_RUN. Before sealing the tally, the lane owner prints each seat's session identifier and complete provider routing log. PASS requires a present, complete log with no fallback; a missing or incomplete log or any fallback is FAIL; an unreached check is NOT_RUN. Apply the two-attempt and split rules of §4. After the tally the lane owner writes R3C2_CHECK_SHEET_<date>.md with source lines, runs the pinned r3c2_lane_tools.py merge and compute commands and re-runs the required scripts; a critic note precedes any ruling.”

Consequential exact cross-reference replacement: replace “a control among C0 through C5b” in §4 with “a control among C0 through C5c”. This is a proposed design amendment, not an applied change.

3. CIRCULARITY

The packet supplies no recoverable directional hypothesis. Independent inclusion, complete candidate/exclusion reporting and a full source-completeness audit obstruct quiet exclusion of contrary claims. Receipt P precedes enumeration and separates the interpretation mapping from the seats. This reduces influence; it does not prove the lane owner lacks expectations or that every human classification is objective.

D2 — exclusion taxonomy does not cover an author-specified input.

Verbatim sentence:

“**The exclusion ledger's
`kind` is one of `EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`, `ATTRIBUTED_NOT_DERIVED`.**”

“We set the simulation input a = 2” is neither the paper's asserted result nor any listed excluded kind. When recorded as a candidate, it has no honest disposition. Treating it as a result changes the denominator; omitting it evades the promised candidate account. This is an enumeration defect, not an extra per-claim outcome.

Exact replacement:

“The exclusion ledger's kind is one of EQUATION_NUMBER, REFERENCE_NUMBER, PAGE_OR_LINE_NUMBER, DATE, ATTRIBUTED_NOT_DERIVED, or NOT_ASSERTED_RESULT. NOT_ASSERTED_RESULT covers a numeral stated as an input, assumption, example, or other value that is not asserted as the paper's own result; cite the passage establishing that role. Every such candidate remains in the candidate ledger and receives exactly one exclusion row.”

Add NOT_ASSERTED_RESULT to the corresponding §1/§3 excluded-kind lists and the validator's accepted kinds before dispatch.

D7 — the auditor sees outcomes before independent re-derivation.

Verbatim instruction:

“A third independent seat **first audits the full candidate and
exclusion ledgers against every pinned source** — completeness, not just outcomes — then re-derives, **without sight of earlier work and re-classifying every input's `origin` from the pinned sources**”

C1 requires those full candidates to contain outcomes and, for arithmetic claims, both numbers. Seeing them first is incompatible with the claimed independent re-derivation without earlier work. It can anchor the audit that is meant to catch shared classification mistakes.

Exact replacement for that instruction:

“A third independent seat first audits a projection of the candidate and exclusion ledgers containing only candidate_id, source_file, source_line, numeral, included and exclusion kind, against every pinned source. The custodian supplies the audit claim IDs selected by the unchanged sampling rule, withholding earlier outcomes, reproduced values, input ledgers and origin classifications. The auditor independently re-derives and records outcomes and origins and seals that work before the custodian reveals the earlier records for MATCH/MISMATCH comparison.”

4. THE BLIND

Independent text check: extracting §§1–6, 9 and 11 and removing SEAT-REDACT spans reproduces the packet body after whitespace normalization. Its embedded master digest matches my access proof. This supports mechanical extraction. It does not establish that the delivered builder implements every asserted forbidden-string test: opening or running that builder would exceed the specified read exceptions. I did not claim a live C4_PACKET_REDACTED PASS.

C4 correctly distinguishes self-reported access from kernel confinement and acknowledges prior-exposure limits. The packet still permits the content-level provenance inference recorded above. A forbidden-string assertion cannot establish absence of all semantic inference.

Q7(e): YES at the mechanism/residual level. The master says “That profile is the mechanism” and “C4 and C5b are self-report controls and do not themselves bound automatic code access.” Its residual says matching digests establish “matching snapshots of the pinned directory at pinning and at C5, not continuous immutability between them and not the absence of startup code; no inference about trusted content follows from the pin alone.” These assign different jobs consistently. This is textual agreement, not independent verification of the unopened profile or a dispatch's probes.

The pin does not close the host-writability/startup-code objection. It detects snapshot differences at the checks; confinement must bound runtime access. The current residual says so. A claim that reviewed command text alone proves its automatically loaded code cannot disclose content should be read subject to this explicit residual, not as a stronger security guarantee.

5. THE SEAL

The design requires receipt P for the protocol hash and commit before limb A, then receipt T for the committed tally bundle before opening the protocol. T names the files, including candidates, exclusions and merged inputs with compute output. The external seed follows T. Independent re-hashing and printing both receipts and four verified values binds the comparison to receipted records; missing receipts or mismatch void interpretation under CENSUS_AUDIT_FAILED.

This is adequate prospective custody as written. I did not inspect receipts or the interpretation protocol, and do not certify their existence or content from narration. The seal binds records, not prior beliefs or the substantive validity of the unseen mapping.

6. FAIRNESS

REPRO_FAILED requires “unreproduced from the stated inputs,” not “error”; the brief applies that wording to negative outcomes generally. The other outcomes describe missing inputs, unavailable machinery or missing procedures rather than accusing the paper of error. CENSUS_COMPLETE describes coverage, not universal successful reproduction.

D8 — COSMETIC label overclaim under the requested classification test.

Verbatim rule fragment: “`DERIVED_ONLY` when every root origin is `DERIVED`, `STANDARD` or `MEASURED`”. A measurement-only claim can therefore carry a name suggesting derivation only. The definition is explicit, so changing only its label changes no membership, reachability, control passability, tested number or interpretive mapping.

Exact replacement: “`DERIVED_STANDARD_OR_MEASURED_ONLY` when every root origin is `DERIVED`, `STANDARD` or `MEASURED`”. Replace that token consistently in the lane tool and interpretation protocol, preserving membership and mappings, then re-pin and receipt the amended artefacts.

Rename audit: REPRO_EXACT occurs on master lines 118, 557, 722, 778, 823, 846, 872, 890, 918, 947, 969, 977, 988, 1002, 1011 and 1013. Line 118 is a rename notice; all others are under §10 headings. No governing old-token reference was found. The optional rename audit file was not needed or opened.

7. STALL / EXECUTABILITY — Q4 AND Q7

Q4: CAN ANYTHING THE DOCUMENT DESCRIBES NOT BE EXECUTED AS DELIVERED?

YES: D1 prevents a compliant imported-choice record, D2 prevents a complete truthful exclusion ledger for the stated witness, and D7 cannot provide blindness after exposing the earlier outcomes. D4 lacks a determinate control result. These persist even though C5 executes.

Read restrictions limit the broader delivery audit. I opened only the master, packet, explicitly permitted brief and V23 comparison document, plus copied/read/executed the expressly requested manifest script. Existence-only filesystem checks found r3c2_ledger_tools.py, r3c2_lane_tools.py, r3c2_manifest.py, r3c2_timeout.py, r3c2_build_seat_packet.py, r3c2_seat_sandbox.sb, R3C2_SEAT_PACKET.sha256, R3C2_CORPUS_MANIFEST.md and R3C2_INTERPRETATION_PROTOCOL_20260904.md. None was found missing. Existence is not content or digest verification. I could not inspect each source named inside the unopened corpus manifest, or certify all scripts' implementation, without violating the read restriction.

I checked the printed census and census-final schemas/counts, validate's source-directory placeholder and stated checks, merge/compute fields and error routes, builder invocation, five harness commands, and timeout invocation against their operative descriptions. All printed interpreter invocations carry -E. The schema and source witnesses expose D1/D2; the remaining implementation claims are not independently certified. Future ledgers, C6_AUDIT.json, receipts, dispatch records and the dated check sheet are run artefacts, not files this unrun design must already contain. Third-seat dispatch is explicitly administrative.

Live C5 working directory:
`/var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/r3c2_v24i_gate_efx2md0f`

The copied r3c2_manifest.py digest was verified as 19a8ce4750bb47655868ef15b55f2b168833147b460c03ad56f84dd3c9bc56f2, matching the printed pin. The following are actual stdout and exit codes, not values copied from the master; stderr was empty for all five.

```text
1. /usr/bin/python3 -E --version
Python 3.9.6
EXIT_CODE=0

2. /usr/bin/python3 -E -c "import sympy; print(sympy.__version__)"
1.14.0
EXIT_CODE=0

3. /usr/bin/shasum -a 256 /usr/bin/python3
b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9  /usr/bin/python3
EXIT_CODE=0

4. /usr/bin/python3 -E -c "import site; print(site.getusersitepackages())"
/Users/duhokim/Library/Python/3.9/lib/python/site-packages
EXIT_CODE=0

5. /usr/bin/python3 -E r3c2_manifest.py /Users/duhokim/Library/Python/3.9/lib/python/site-packages
FILES=20637
MANIFEST_SHA256=1b5463c1072994b2c458d8cbe73a931d23c4b9b10cee3dfd789989d59d9f03ed
EXIT_CODE=0
```

Q7(a): YES. Governing C4 text permits “the five C5 harness commands” together with “whatever those commands themselves invoke or load”. C5's directory argument is exactly the environment directory its preceding command prints. C5b adopts C4's boundary. The brief likewise permits “execute the commands the packet prints verbatim, with whatever they themselves load”. My run establishes executability on this host, not C5_HARNESS_PINNED=PASS for a census dispatch: comparison against that dispatch's prelaunch pin and sandbox probes remains required.

Q7(b), D3: NO_MASKED_STAGE=YES for the operative mandated invocations. Census, validate, merge, compute, builder and all five harness calls are individual invocations. The symbolic wrapper is one parent invocation with a specified child-status/timeout reporting contract, not literally a process without children. No mandated shell pipeline remains in the operative sections. Historical pipelines in §10 do not govern this design. I did not dynamically verify the wrapper implementation under the read restriction.

Q7(c): The principle leaves no C5 path forbidden: it admits the whole printed user-site directory, including dependencies and startup files, and the automatic loads of mandated commands. A seat cannot use a placeholder, import, data path or wrapped command to choose another lane's file; the choice remains subject to (i)–(ii). Reading arbitrary content already inside the pinned environment is permitted, but the residual does not certify that content as trusted. The earlier system-prefix-only and single-initializer rules are superseded; the actual user-site path is no longer excluded. Actual confinement must be demonstrated at dispatch.

Q7(d): Direct V23/master diff shows more than a binary-scope sentence changed: the version/status header; the seat-tool digest; -E on census, final census, validate, merge, compute, builder and wrapper calls; the C4 principle and seat-choice boundary; the kernel-profile pin and required probes; the revised residual; the manifest script in dispatch inventory; C5 expanded from three commands to five with an absolute shasum path, manifest-script pin, directory/digest comparison and explicit failure predicates; the no-pipeline/one-invocation statement; and C5b's matching boundary. Section 10 also has updated V23/V24 rows, an updated historical tool digest and the added V24 narrative. No outcome membership, precedence, threshold, provenance taxonomy or interpretation rule changed in the inspected master diff. The current brief names all three scripts and echoes the new boundary; no separate old brief was supplied for a bytewise brief diff. I did not open a V24h file, so the claimed V24h-to-V24i-only delta is not independently byte-verified.

Q7(f): NOTHING BEYOND THE PENDING FIVE. My independently constructed substantive defects are D1 evidence, D2 exclusion kind, D4 no-fallback code and D7 auditor exposure. D8 is the pending label issue, classified COSMETIC under the user's strict test. The missing implementation/dispatch verification described above is a limit of this restricted gate, not an invented missing-deliverable finding. The executable scope correction does not resolve those design defects; they prevent an unqualified sound gate.

R3C2_V24I_GATE_COMPLETE

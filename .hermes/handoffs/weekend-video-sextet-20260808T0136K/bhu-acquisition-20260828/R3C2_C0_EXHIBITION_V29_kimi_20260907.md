ACCESS_SHA=37ba58918ec6f6b09775808041acc370aff3dd3dfd561e63407829255080e64d
C0_REACHABILITY=PASS

# R3C2 — C0 REACHABILITY EXHIBITION on V29 (kimi seat), 2026-09-07

Subject document: `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md`, Version 29 (living draft), sha256 as printed on line 1
(computed by this seat with `shasum -a 256` before any other step).
Exhibited against the text as it stands: §3 settled under option (c) (one pass, two tallies; `REPRO_AFTER_CHOICE` retired
into the script-computed `rests_on` field — it is NOT a §3 outcome of this text and is exhibited against nothing);
§4 as printed; the V29 repairs (complete-closure audit comparison including off-sample dependency records, declared
alternatives — origin and/or parent list — matched once over the whole closure, a `STANDARD` value line outside the
claiming file treated as an import, `merge` failing in the open on field disagreements). §10 is history and binds nothing.
This seat exhibits reachability only. It does not gate the design and does not judge its physics.

Clause paths cite the document's own sections. Concrete inputs are synthetic corpora/claims constructed to satisfy each
predicate exactly; each names the claim, its inputs, and the route through the document to the verdict.


## (A) §3 per-claim outcomes — all six exhibited, all reachable

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `REPRO_WITHIN_STATED_PRECISION` | Paper `alpha.tex` line 42 prints "the cluster distance is 50.0 Mpc" as its own result of `d = v/H0`, with `v = 3368 km/s` printed at `alpha.tex:41` and `H0 = 67.36` km/s/Mpc printed at `alpha.tex:40` verbatim from C3's closed list. Inputs: `v` status `PRINTED` (origin `MEASURED`, `ORIG_MEASURED` quotation at :41); `H0` status `STANDARD` (ledger key `H0`, exact string `67.36`, origin `STANDARD`, `ORIG_CONSTANT`, value-line check at the claiming file :40). Both records consumable. Mechanical attempt: 3368 / 67.36 = 50.0 Mpc. No stated uncertainty, so the printed precision governs: 50.0 rounds to the printed numeral `50.0` (rounding half away from zero). | §1 included (printed numeral asserted as the paper's own result) → §2 steps 1–3 (extract, list, classify — both `PRINTED`/`STANDARD`) → §2 step 4 (mechanical attempt consumes every `PRINTED`/`STANDARD` record) → §3 precedence: derivation stated, no `BLOCKED`, no `ABSENT`, evaluable → arithmetic group → `REPRO_WITHIN_STATED_PRECISION`; both numbers reported; script later computes `rests_on` `DERIVED_STANDARD_OR_MEASURED_ONLY` (roots `MEASURED`, `STANDARD`). | YES |
| `REPRO_FAILED` | Paper `beta.tex` line 17 prints "Ωm + ΩΛ = 1.02" as its own result of the sum of its two stated inputs, `Ωm = 0.3153` and `ΩΛ = 0.6847`, both printed in `beta.tex` at :15–16 verbatim from the closed list. Inputs: both status `STANDARD` (ledger keys `Omega_m`, `Omega_L`, exact strings, value lines in the claiming file). Consumable. Attempt: 0.3153 + 0.6847 = 1.0000 ≠ 1.02. | §1 included → §2 steps 1–4 (inputs sufficient and consumed) → §3 precedence: no earlier terminal condition holds → arithmetic group → `REPRO_FAILED`; both numbers reported (printed 1.02, reproduced 1.0000); wording "unreproduced from the stated inputs", not "error"; `rests_on` computed beside it. | YES |
| `REPRO_BLOCKED` | Paper `gamma.tex` line 88 prints "M = 2.3e14 M_sun" as its own result of `M = f·X`, `f` printed at :87, `X` not printed anywhere in the claiming paper; :89 reads "with X taken from Smith et al. (2019)", and Smith et al. (2019) is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`. Input `X`: status `BLOCKED`, origin `IMPORTED`, `ORIG_CITATION` evidence = the verbatim naming sentence at `gamma.tex:89`, empty value; never consumed; the seat may not supply a value, so the attempt ends there. (Second limb, same class: the named source IS a pinned enumerable text but the value does not machine-match as a numeric token at the cited line — same filing.) | §1 included → §2 step 3 named-source test: source not enumerable (or no token match) → §2's import rule "If the named source is not enumerable or the value does not match there, file `REPRO_BLOCKED` under §3" → §3 precedence: derivation stated (so not `REPRO_NO_DERIVATION_STATED`), `REPRO_BLOCKED` first among the remaining → filed; input and source named. | YES |
| `REPRO_NOT_EVALUABLE` | Paper `delta.tex` line 55 prints "χ²_min = 12.4" as its own result of minimising its printed likelihood over its printed data vector; every input `PRINTED`. The symbolic minimisation launched as `/usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command>` exceeds the 120.0-second monotonic deadline: the wrapper prints `SYMBOLIC_TIMEOUT` and exits 124. (Second limb, same class: the recipe requires numerical machinery this lane does not have → `MACHINERY_UNAVAILABLE`.) | §1 included → §2 steps 1–4 (attempt begun, inputs consumable) → §9 wrapper deadline (or missing machinery) → §3 precedence: no derivation/blocked/absent condition holds; `REPRO_NOT_EVALUABLE` precedes the arithmetic group → filed with `SYMBOLIC_TIMEOUT` (or `MACHINERY_UNAVAILABLE`) and the point reached printed. One repeat permitted (§4.2); if the repeat also stalls, the class stands. | YES |
| `REPRO_NO_DERIVATION_STATED` | Paper `epsilon.tex` line 23 prints "the best-fit value is b = 0.87" as its own result, and the only provenance sentence, :24, reads "we obtained b from our standard pipeline" — a procedure named but not specified: no equation and no operations a seat could attempt. | §1 included (printed numeral asserted as the paper's own result) → §2 step 1 finds no stated equation/procedure → §3 class text: "A procedure named but not specified … states no computational procedure that could produce it; file this class and name the passage" → §3 precedence: first in the order → `REPRO_NO_DERIVATION_STATED`, passage `epsilon.tex:23–24` named. | YES |
| `REPRO_INPUT_ABSENT` | Paper `zeta.tex` line 61 prints "L = 3.2e44 erg/s" as its own result of `L = 4π d² F`; `F = 2.1e-12 erg/s/cm²` printed at :60; the distance `d` is printed nowhere in the paper and no source is named for it — neither printed nor traced to any named source. Input `d`: status `ABSENT`; the seat may not supply a value; the attempt stops there. | §1 included → §2 steps 1–3 (`d` classified `ABSENT`) → §2 machine floor "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." → §3 precedence: derivation stated; no `BLOCKED` (no named source); `REPRO_INPUT_ABSENT` → filed, input named. | YES |

Not exhibited, because it is not a §3 outcome of this text: `REPRO_AFTER_CHOICE` — retired at V10 by the principal's
ruling adopting option (c); its content is the script-computed `rests_on` field (§3, master-only rule).


## (B) §4 study-level classes — all eight exhibited, all reachable

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `R3C2_NO_CLASS` | Both seats reach C1B; in each seat, batch 7's `SEAT_REPORT_b7.md` omits the packet's `ACCESS_SHA` line, once, and again on the second attempt → `C1B_BATCH_COVERAGE=FAIL` in every seat that attempted it after two attempts. (Second route: `C4_PACKET_REDACTED=FAIL` before dispatch — the builder finds a forbidden-list string surviving and the packet is not written.) | §5 C1B predicate ("every batch report prints the packet's `ACCESS_SHA`") fails → §4 class 4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class" → §4 precedence: first in the order → filed. | YES |
| `CENSUS_CONTROL_SPLIT` | Seat A's batch 3 report lacks the `ACCESS_SHA` line → `C1B_BATCH_COVERAGE=FAIL`; seat B's reports are complete → `C1B_BATCH_COVERAGE=PASS`; two attempts in each seat leave the split standing. | §5 C1B: "Either FAIL stops the seat's tally"; §4 class 8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." → §4 precedence: `R3C2_NO_CLASS` does not hold (not every seat failed) → `CENSUS_CONTROL_SPLIT` filed. | YES |
| `CENSUS_DENOMINATOR_DISPUTED` | Route (i): seat A includes candidate `p7.tex#142` (numeral `0.87`, asserted result) while seat B excludes it as `ATTRIBUTED_NOT_DERIVED`; two reconciliation attempts leave the disagreement. Route (ii): the enumerations agree, but seat A lists input `d` for the agreed claim `p9.tex#61` and seat B does not; `merge` exits 1 on the differing `input_id` sets; the one reconciliation against the paper's stated equation does not resolve it. | Route (i): §1 ("disagreement on any candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)") and §6 limb A (tolerance zero). Route (ii): C3 lane-side rule "`merge` exits 1 if the two `input_id` sets differ — … an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)". §4 precedence: control classes do not hold → filed; disputed candidates or inputs listed; census does not proceed. | YES |
| `CENSUS_OUTCOME_DISPUTED` | Agreed included claim `q3.tex#77` prints "σ₈ = 0.811 (S₈ = 0.832)" and one equation producing 0.811 from printed inputs. Seat A treats `0.811` as the claim's printed numeral → reproduced 0.811 matches at printed precision → files `REPRO_WITHIN_STATED_PRECISION`. Seat B treats `0.832` as the printed numeral → |0.811 − 0.832| fails the rounding rule → files `REPRO_FAILED`. The one reconciliation against the printed numeral and the stated-precision rule of §3 does not settle which numeral the claim asserts; the disagreement survives. | §2 step 5 ("a disagreement surviving that reconciliation files `CENSUS_OUTCOME_DISPUTED` (§4)") → §4 class 6 → §4 precedence: earlier classes do not hold → filed; the claim listed with both seats' outcomes, both number pairs, and the step each seat reached. | YES |
| `CENSUS_ORIGIN_DISPUTED` | 10 included claims. In 2 of them an input's sentence reads "we adopt the value 3.2, consistent with our earlier estimate": seat A files `ORIG_CHOICE_STATED`→`CHOSEN`, seat B files `ORIG_MEASURED`→`MEASURED`. Origin disagreements are reported, never reconciled; affected claims = 2/10 = 20% > 10%. | C3 ("Every input's `origin` is classified independently by both seats"; disagreement filed `ORIGIN_DISPUTED`, not reconciled) → C6/§4 class 7: disagreement "on inputs affecting more than 10% of included claims" → §4 precedence: earlier classes do not hold → `CENSUS_ORIGIN_DISPUTED`; every disputed input listed with both classifications and both quotations. | YES |
| `CENSUS_AUDIT_FAILED` | The audit samples claim `s1.tex#12` (arithmetic group). The auditor's independent reconstruction of its inputs supports outcome `REPRO_FAILED` (reproduced 1.0000 vs printed 1.02); the sealed candidate file carries `REPRO_WITHIN_STATED_PRECISION` for that claim. `audit compare` reports the unsupported difference as `MISMATCH` for that audited claim. | C6 PASS predicate ("no audited claim or origin is `MISMATCH`") fails → `C6_AUDIT_SAMPLE=FAIL` → §4 class 3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named)" → §4 precedence: before `CENSUS_PARTIAL`/`CENSUS_COMPLETE` → filed; no tally filed. (The V29-specific C6 paths are exhibited in section D below.) | YES |
| `CENSUS_PARTIAL` | Corpus with 5 included claims; 4 file arithmetic-group outcomes; 1 files `REPRO_BLOCKED` (the `gamma.tex` claim of (A)). All controls pass in both seats; enumerations, input lists, outcomes and origins agree within thresholds; the audit runs and PASSES (the blocked claim sits in the "remaining" pool; the auditor's reconstruction of it matches the sealed `BLOCKED` record — named source not enumerable — a `MATCH`). Second route: a corpus whose enumeration finds zero included claims → denominator zero. | §4 class 2: "at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`), or the denominator is zero" → §4 precedence: every earlier class fails to hold → `CENSUS_PARTIAL`, reported with each non-arithmetic claim and why; INCONCLUSIVE; takes precedence over `CENSUS_COMPLETE`. | YES |
| `CENSUS_COMPLETE` | Corpus with 3 included claims, each of the (A) `REPRO_WITHIN_STATED_PRECISION`/`REPRO_FAILED` type: every claim states its equation, every input is `PRINTED` in the paper or `STANDARD` on the closed list with its value line in the claiming file, every attempt completes inside the wrapper deadline. Denominator = 3 > 0. Both seats agree on enumeration, inputs, outcomes and origins; `merge` produces no dispute fields; `compute` emits `rests_on` for all 3; the external seed is supplied and recorded with receipt T; the audit's recomputed selection matches, no omission row, dispute rate ≤ 10%, no `MISMATCH` → `C6_AUDIT_SAMPLE=PASS`. | §4 class 1: "every included claim carries exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`" → §4 precedence: none of the seven earlier conditions holds (`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`) → `CENSUS_COMPLETE` filed; the full tally reported with its denominator, and the `rests_on` tally beside it — two tallies from one pass. | YES |


## (C) Reachability statement, per verdict

§3: `REPRO_WITHIN_STATED_PRECISION` YES; `REPRO_FAILED` YES; `REPRO_BLOCKED` YES; `REPRO_NOT_EVALUABLE` YES;
`REPRO_NO_DERIVATION_STATED` YES; `REPRO_INPUT_ABSENT` YES.
§4: `R3C2_NO_CLASS` YES; `CENSUS_CONTROL_SPLIT` YES; `CENSUS_DENOMINATOR_DISPUTED` YES; `CENSUS_OUTCOME_DISPUTED` YES;
`CENSUS_ORIGIN_DISPUTED` YES; `CENSUS_AUDIT_FAILED` YES; `CENSUS_PARTIAL` YES; `CENSUS_COMPLETE` YES.

No §3 outcome and no §4 class is UNREACHABLE under the V29 text.


## The named suspicion, answered directly: `CENSUS_COMPLETE`

Question: in a real corpus of many papers, is there any input under which `CENSUS_COMPLETE` can actually be filed — or
does a single blocked, absent-input, or no-derivation-stated claim anywhere in the corpus force `CENSUS_PARTIAL`,
making `CENSUS_COMPLETE` unreachable in practice?

Answer: REACHABLE.

Routing. The class predicate (§4 class 1) is: "every included claim carries exactly one outcome from the arithmetic
group of §3, with `C6_AUDIT_SAMPLE=PASS`. A denominator of zero files `CENSUS_PARTIAL` with the empty enumeration
named; no census is complete over nothing." The predicate is a condition on a corpus, not a condition on all corpora.
The concrete input exhibited in (B) — a corpus whose every included claim states a derivation, prints or closed-list
prints every input, and completes arithmetic inside the deadline, with the audit passing — satisfies every conjunct,
and the §4 precedence order then files `CENSUS_COMPLETE`, because none of the seven earlier conditions holds.

What is true, and what it does and does not imply: for any corpus that CONTAINS even one `REPRO_BLOCKED`,
`REPRO_INPUT_ABSENT`, `REPRO_NO_DERIVATION_STATED` or `REPRO_NOT_EVALUABLE` claim, the filed study-level outcome is
`CENSUS_PARTIAL` — §4 class 2's predicate holds and "it takes precedence over `CENSUS_COMPLETE`". Whether the pinned
corpus of 89 enumerable texts contains such a claim is precisely the empirical question the census exists to answer;
C0 does not prejudge it. But that is a property of one input, not a definitional bar: no clause makes the
`CENSUS_COMPLETE` predicate unsatisfiable, the zero-denominator case is explicitly routed AWAY from it (to
`CENSUS_PARTIAL`), and the class sits in the precedence order as a live filing. A verdict that is filed only when a
condition holds is reachable iff there exists an input on which the condition holds. Such an input exists and is
exhibited in (B). The document's own record agrees: §10.3 shows both blind C0 seats on V9 exhibiting
`CENSUS_COMPLETE` as reachable, and nothing in V10–V29 narrows the class's predicate — V21/V22 only added the
zero-denominator routing to `CENSUS_PARTIAL`, which makes the boundary sharper, not the class emptier.

So: `CENSUS_COMPLETE` is reachable; a hostile corpus defeats it for that corpus, and no corpus defeats it for every
corpus.


## (D) V29-named exhibitions

### D1. `CENSUS_AUDIT_FAILED` through each C6 path

| # | C6 path | concrete input | clause path (verbatim anchor) | reachable |
|---|---|---|---|---|
| 1 | Sealed-included absent from the auditor | Sealed candidate file includes passage (`f12.tex`, line 99, numeral `3.5`) as INCLUDED; the auditor's complete independent enumeration of all 89 texts omits it → completeness row result `OMISSION`. | C6: "Omissions: a sealed INCLUDED passage absent from the auditor's enumeration; … each is ledger incompleteness and files `CENSUS_AUDIT_FAILED`." PASS predicate also requires "no row is an omission". | YES |
| 2 | Auditor-listed absent from the sealed ledgers | The auditor lists passage (`g4.tex`, line 210, numeral `0.95`) — included or excluded, either dispositions — that neither the sealed candidate file nor the sealed exclusion ledger names → `OMISSION`. | Same clause, second limb: "a passage the auditor lists (included OR excluded) that the sealed ledgers omit — each is ledger incompleteness and files `CENSUS_AUDIT_FAILED`." | YES |
| 3 | Dispute rate above 10% | Sealed included denominator = 50; 6 passages are listed by both sides but disposed differently (e.g. seats excluded as `AUTHOR_SPECIFIED_INPUT`, auditor includes), and/or sealed-EXCLUDED passages absent from the auditor → `AUDIT_INCLUSION_DISPUTED` count 6; 6/50 = 12% > 10%. | C6: "Disputes: a passage both sides list but dispose differently, and a sealed EXCLUDED passage absent from the auditor's enumeration, are `AUDIT_INCLUSION_DISPUTED`, listed with both dispositions and counted; above 10% of the sealed included denominator the audit files `CENSUS_AUDIT_FAILED`; at or below it the count is reported." | YES |
| 4 | Seedless selection | The tally is committed and receipted (receipt T); the external custodian never supplies a seed; no seed is recorded with the receipt. | C6: "If the seed is not supplied and recorded with the receipt, the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named." | YES |
| 5 | Zero denominator with any passage on either side | The sealed enumeration includes 0 claims; the auditor's enumeration lists ≥ 1 passage (either disposition). | C6: "A sealed denominator of zero with any passage on either side fails." → audit does not run to PASS, cause named → §4 class 3. (For contrast: zero denominator with NO passage on either side does not trip this clause; the study then files `CENSUS_PARTIAL` under the zero-denominator limb of §4 class 2.) | YES |
| 6 | Incomplete reconstruction | The auditor's reconstruction for an assigned claim carries an input record lacking `origin_evidence` (or any required field). The re-derivation seal refuses it; the audit cannot complete. | C6: "before sealing, `audit seal-rederivation` validates the reconstruction schema — every input carries symbol, status, value, source coordinates, origin, origin evidence and `derived_from` (and `origin_search` when silent) — and refuses an incomplete one"; and "`audit compare` … reports a missing field, a missing input … as `MISMATCH`". Either way the audit does not PASS → §4 class 3. | YES |
| 7 | Fabricated evidence quotation in an OFF-SAMPLE dependency record | Selected claim `s9.tex#5` depends, through its `derived_from` closure, on input record `i44` belonging to claim `x2.tex#31`, which is NOT in the audited sample. The sealed ledger's `i44` carries `origin_evidence` with a "verbatim" quotation that does not occur at its cited `source_file`/`source_line`. The auditor, reconstructing the COMPLETE dependency closure of `s9.tex#5` — including `x2.tex#31`'s records — carries the true quotation; the sealed record does not validate against the pinned text. | §3 (master-only audit rule, V29): "first every reconstructed input in the complete dependency closure of each selected claim — including records assigned to claims outside `audited_ids` — is validated and compared: each record is bound to its sealed `input_id` and claim, every required field, evidence coordinate, quotation and dependency edge is compared, and any unsupported difference is `MISMATCH` on every selected claim that depends on it" → `MISMATCH` on `s9.tex#5` → C6 PASS predicate ("no audited claim or origin is `MISMATCH`") fails → §4 class 3. | YES |
| 8 | A dependency the auditor did not reconstruct | The auditor's closure for a selected claim adopts a parent edge from the sealed side instead of reconstructing it from the pinned sources (i.e. the auditor's own graph lacks an independently reconstructed target). | C6: "`audit compare` … reports a missing field, a missing input, a dependency the auditor did not itself reconstruct, or any unsupported difference as `MISMATCH`" → `MISMATCH` → §4 class 3. (This is the V28 repair: the audit "never borrows a dependency from the sealed side".) | YES |
| 9 | A differing dependency edge | Sealed ledger: input `i7` of the selected claim carries `derived_from: [i3]`, with no declared alternative parent list. Auditor's independent reconstruction: `derived_from: [i3, i4]`, evidenced at the claim's equation line. The edge sets differ and no declared alternative matches. | §3 master-only rule: "every … dependency edge is compared, and any unsupported difference is `MISMATCH` on every selected claim that depends on it"; C6: "`audit compare` requires every one of those fields, compares every field, every evidence coordinate and quotation, and every dependency edge against the sealed ledger" → `MISMATCH` → §4 class 3. | YES |
| 10 | Receipt verification of the seal fails | After opening, Blanc re-hashes the tally commit and finds the hash differs from receipt T (or receipt P or T is missing). | §7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED` (§4, whose definition now names this case), leaves the interpretation `NOT_RUN` and voids the comparison"; §4 class 3: "or the receipt verification of the seal fails". | YES |

Every named C6 failure path routes to `CENSUS_AUDIT_FAILED`, and per §4 class 4 "A C6 audit failure or a
seal-receipt failure files `CENSUS_AUDIT_FAILED`, not [`R3C2_NO_CLASS`]" — none of them lands in the control class.

### D2. A claim whose auditor reconstruction matches a declared PARENT-LIST alternative — does NOT file `CENSUS_AUDIT_FAILED`

Concrete input: selected claim `s4.tex#19`, input `i10`. The two seats disagreed on its parents: seat A recorded
`derived_from: [i8]`; seat B recorded `derived_from: [i8, i9]`. Under C3's lane-side rule the merged record carries
both parent lists marked `PARENTS_DISPUTED`, and `compute` derived root origins under both, printed as a pair — the
alternative parent list is an explicitly DECLARED alternative in the sealed ledger. The auditor independently
reconstructs `i10`'s parents as `[i8, i9]`, origin unchanged, with matching evidence. Under V29 the auditor's branch
is matched against the declared alternative over the whole closure once; the matched-branch graph (including any
off-sample records in the closure) is used for every dependent claim's sealed-root comparison; the recomputed roots
under that graph agree with the sealed pair's matching branch. No `MISMATCH` is filed for `i10`, and — with nothing
else differing — the audit does not file `CENSUS_AUDIT_FAILED` on this claim's account. Both sealed branches and the
matching branch are reported; the original dispute is not reconciled.

Clause path (verbatim anchor): "Matching an explicitly declared alternative is not `MISMATCH`: the auditor's origin,
origin evidence and parent list are matched against the complete declared primary or alternative record, including an
alternative parent list when the origin is unchanged; one consistent matched-branch graph is constructed over the
selected claims and their complete dependency closure and used for every dependent claim's sealed-root comparison; an
unsupported record, evidence, parent list or inconsistent branch remains `MISMATCH`; both sealed branches and the
matching branch are reported without reconciling the original dispute." Reachable: YES (both limbs — the match that
does not file, and the unsupported remainder that does, exhibited in D1 row 9).

### D3. Seat-tally stops and their §4 filings

| stop | concrete input | immediate effect | §4 filing |
|---|---|---|---|
| `C1B_BATCH_COVERAGE=FAIL` | In one seat, manifest text `m31.tex` is listed in no batch's `OWNERSHIP_b<k>.txt` (not owned by exactly one batch); or an owned text's bytes fail verification against its manifest row; or a batch report omits the packet's `ACCESS_SHA`. | C1B: "Either FAIL stops the seat's tally." | C1B's §4 routing: "a FAIL in every seat that tries it, after two tries, files `R3C2_NO_CLASS`; a surviving fail/pass split files `CENSUS_CONTROL_SPLIT`; an unreached check is `NOT_RUN`." Both filings exhibited: all-seat FAIL → `R3C2_NO_CLASS` (§4 class 4); one-seat split after two attempts → `CENSUS_CONTROL_SPLIT` (§4 class 8). |
| `JOIN=FAIL` | In one seat's LIMB-A chain, batch 5's seal does not match its receipted bytes (or: the predecessor chain is broken from the root; a candidate is owned by the wrong batch; an evidence source is not a manifest text; duplicate identifiers; a `derived_from` cycle). | C1B: "Either FAIL stops the seat's tally." | Same contract as above: every seat after two tries → `R3C2_NO_CLASS`; surviving split → `CENSUS_CONTROL_SPLIT`; unreached → `NOT_RUN`. Reachable: YES. |
| `C5C_NO_FALLBACK=FAIL` | The lane owner's pre-tally check finds batch session 4 of seat A has no printed, session-identified provider log (or the log carries a fallback entry). | §9: "a missing log or any fallback entry is FAIL" — a pre-tally control checked by the lane owner. | §9: C5C is "a pre-tally control under the `R3C2_NO_CLASS` and `CENSUS_CONTROL_SPLIT` rules" → FAIL in every seat that attempted it after two attempts → `R3C2_NO_CLASS` (§4 class 4); a surviving fail/pass split after two attempts → `CENSUS_CONTROL_SPLIT` (§4 class 8). Reachable: YES. |
| `merge` field disagreement (`FIELD_DISAGREEMENTS`) | The two seats agree on every candidate and every `input_id`, but for input `i21` of claim `w2.tex#14` seat A records value `0.3153` and seat B records `0.315` (or their status / symbol / source coordinates differ). | C3 lane side: "`merge` prints every such disagreement, reports `FIELD_DISAGREEMENTS`, exits 1 and writes no merged file" — so no merged ledger exists, `compute` cannot run, and no tally can be assembled. | The text licenses exactly one routing, quoted: "the lane resolves it in the open before the tally." No §4 stop class is named for a field disagreement, and none is invented here. (Contrast, same command, different cause: an `input_id`-SET difference surviving one reconciliation "stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)" — exhibited in (B).) The tally stop itself is reachable: YES. |

### D4. A claim with `rests_on` `NOT_COMPUTED`

Concrete input: the `epsilon.tex#23` claim of (A), filed `REPRO_NO_DERIVATION_STATED` — no stated equation, hence no
inputs to list, hence no ledger records at all for that claim. The merged input ledger is valid (an empty claim-entry
is valid); after `compute`, the claim carries `rests_on` `NOT_COMPUTED`, and the `rests_on` tally reports a
`NOT_COMPUTED` row. Clause path: §3 master-only note — "an empty ledger is valid and every included candidate without
a record carries `rests_on` `NOT_COMPUTED`"; §3 arithmetic-group note — "`rests_on` is computed and reported for every
included claim that has at least one ledger record, whatever its outcome; a claim with no ledger record carries
`rests_on` `NOT_COMPUTED`, and the `rests_on` tally reports a `NOT_COMPUTED` row." Reachable: YES.


## UNREACHABLE verdicts

None. Every §3 per-claim outcome (six of six) and every §4 study-level class (eight of eight) is exhibited above with
a concrete input and a clause path, and every V29-named path (D1 rows 1–10, D2, D3, D4) is exhibited. No blocking
clause exists to quote: there is no verdict for which every path is blocked.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V29_KIMI_COMPLETE

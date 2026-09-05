ACCESS_SHA=e8ba4a7438d61f028e3c46c7308d7078f011e53886e332b946bd7e21f6a1c6c8
C0_REACHABILITY=PASS

# R3C2 C0 REACHABILITY EXHIBITION — V20, kimi seat, 2026-09-05

Scope: this exhibition was produced from exactly one file, `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` (V20),
read in full from disk; no other file in the directory was opened. The task is reachability only: whether each
declared §3 per-claim outcome and each declared §4 study-level class CAN OCCUR under the text as it stands.
Nothing here judges the design or the physics.

Definition dependence, stated rather than assumed: V20 carries no HELD marker. The marker that stood over §3
since V5.1 was removed at V10 when the principal ruled option (c) — one pass, two tallies (§10.4). §1's core
definition is therefore the settled option-(c) wording: the reproduction verdict ("does the paper's arithmetic
work from what it states?") and the ledger provenance are recorded separately, `REPRO_AFTER_CHOICE` is retired
into the script-computed `rests_on` field, and the arithmetic group is exactly {`REPRO_EXACT`, `REPRO_FAILED`}
(§3). Every exhibition below is against that wording. Two items remain escalated to the principal and are NOT in
the text: a class for a surviving per-claim outcome split (with a zero-denominator sub-option) and the
`REPRO_EXACT` rename (§10.13, §10.14). Neither changes the declared outcome set exhibited here; the dependence is
flagged under Remarks, not resolved by assumption.

All witnesses are CONSTRUCTED inputs — specific claims with specific inputs invented for this exhibition. C0 asks
for "a concrete input that produces it"; reachability is existential, so a constructed witness with a traced
clause path is the required artefact. The real corpus (89 enumerable texts, §10.5) was not consulted and no claim
below is asserted to be a corpus claim.

## Exhibition table

(A) §3 per-claim outcomes (six declared; precedence: `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`,
`REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the arithmetic group — §3)

verdict | concrete input (constructed) | clause path | reachable
---|---|---|---
`REPRO_EXACT` | Paper P prints "f_b = Ω_b h² / Ω_m h² = 0.157" as its own result, from the stated ratio, with Ω_b h² = 0.02237 printed and appearing verbatim on C3's closed list, and Ω_m h² = 0.1424 printed but not on the list. Reproduced: 0.02237/0.1424 = 0.157092 → rounds to 0.157 at the printed three-decimal precision. | §1: numeral asserted as the paper's own result → included. §2 steps 1–3: extract; list inputs; classify 0.02237 `STANDARD` (printed AND on the closed list verbatim — §2 step 3's tie rule), 0.1424 `PRINTED`. §2 step 4 + §3 "THE INPUTS THE ARITHMETIC MAY CONSUME": both records consumable. §3 `REPRO_EXACT`: no stated uncertainty, so the rounding rule — "the reproduced value must round to the printed numeral at that precision" — is met. §3 precedence: no terminal condition holds → arithmetic group → `REPRO_EXACT`; `rests_on` computed beside it by the lane script (§3 master-only rule, C3 lane block). | YES
`REPRO_EXACT` (uncertainty limb) | Same ratio, paper prints "0.157 ± 0.006". Reproduced 0.157092; |0.157092 − 0.157| = 0.000092 ≤ 0.006. | As above, but §3's uncertainty test applies: "|reproduced − printed| ≤ the stated uncertainty, taken once — not doubled, not rounded"; the asymmetric sub-clause (half-width on the side the reproduced value falls) is not triggered here. | YES
`REPRO_FAILED` | Same paper, same equation, same two printed inputs; the paper prints "f_b = 0.171". Reproduced 0.157092; |0.157092 − 0.171| = 0.013908; no stated uncertainty; 0.157092 does not round to 0.171. | §1 → §2 steps 1–4 as above (inputs sufficient, both consumable) → §3 `REPRO_FAILED`: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number." Wording rule honoured: "unreproduced from the stated inputs," not "error." Precedence: no terminal condition holds → arithmetic group → `REPRO_FAILED`; `rests_on` reported beside it. | YES
`REPRO_BLOCKED` | Paper prints "N(>σ₈) = 412" from a stated cluster-abundance equation needing σ₈, giving only "σ₈ from Smith et al. (2003)" — the value is not printed, and Smith et al. (2003) is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`. | §2 named-source rule: "a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files `REPRO_BLOCKED` under §3." §3 `REPRO_BLOCKED` first limb. C3: status `BLOCKED`, origin `IMPORTED`, `ORIG_CITATION` evidence, no value; "the arithmetic never consumes it." §2: "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." §3 precedence: equation is stated, so not `REPRO_NO_DERIVATION_STATED`; a source is named, so not `REPRO_INPUT_ABSENT` — and BLOCKED precedes ABSENT in the order regardless. | YES
`REPRO_NOT_EVALUABLE` (`SYMBOLIC_TIMEOUT`) | Paper prints "χ²_min = 812.4" from a stated symbolic sum over a stated dataset; the evaluation, launched as `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>` (§9), exceeds the 120-second monotonic deadline. | §9: the wrapper "on the deadline prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome." §3 `REPRO_NOT_EVALUABLE`: "the arithmetic could not be completed within the 120-second cap" → print `SYMBOLIC_TIMEOUT` and the point reached. Precedence: derivation stated, no blocked/absent input → fourth slot applies. §4 class 2's "one repeat permitted, meaningful only for `REPRO_NOT_EVALUABLE`" contemplates exactly this outcome. | YES
`REPRO_NOT_EVALUABLE` (`MACHINERY_UNAVAILABLE`) | Paper prints "P(k=0.1) = 6.31" as its own result from a stated N-body/MCMC pipeline whose execution needs machinery beyond the lane's pinned `/usr/bin/python3` + sympy harness (C5). | §3 `REPRO_NOT_EVALUABLE`: "or requires machinery this lane does not have" → print `MACHINERY_UNAVAILABLE` and the point reached (the `MACHINERY_UNAVAILABLE` token was added at V15, §10.9). Same precedence slot as above. | YES
`REPRO_NO_DERIVATION_STATED` | Paper prints "r_s = 147.1 Mpc" as its own result and states no equation or computational procedure producing it — or writes only "obtained from our Boltzmann solver," naming a procedure without specifying operations a seat could attempt. | §3 `REPRO_NO_DERIVATION_STATED`: "the paper prints the claim as its own result but states no equation or computational procedure that could produce it, so there is nothing to attempt. Name the passage." The named-but-unspecified clause: "A procedure named but not specified … states no computational procedure that could produce it; file this class and name the passage" (added at V19, §10.13). Precedence: FIRST in the §3 order — files even if an input would also be absent. With no equation there is no input list, hence no ledger record; §3's master-only rule then carries `rests_on` = `NOT_COMPUTED` and the `rests_on` tally reports a `NOT_COMPUTED` row. | YES
`REPRO_INPUT_ABSENT` | Paper prints "D(z=1) = 0.61" from a stated growth integral that requires the growth index γ; γ is neither printed anywhere in the paper nor traced to any named source. | §2 step 3: γ classified `ABSENT`. §2: "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." §3 `REPRO_INPUT_ABSENT`: "an input the equation needs is `ABSENT` from the paper — neither printed nor traced to any named source — so the attempt stops there. Name the input" (γ). Precedence: equation is stated (not NO_DERIVATION), no source is named (not BLOCKED) → third slot. | YES

(B) §4 study-level classes (seven declared; precedence: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`,
`CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`,
`CENSUS_COMPLETE` — §4)

verdict | concrete input (constructed) | clause path | reachable
---|---|---|---
`R3C2_NO_CLASS` | C5 harness: `/usr/bin/python3 -c "import sympy; print(sympy.__version__)"` exits non-zero in seat A and in seat B, on two attempts each. Alternative pre-dispatch witness: the builder's forbidden-list assertion fails and no packet is written (`C4_PACKET_REDACTED=FAIL`). | §4 class 4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class." First in the §4 filing order, so nothing pre-empts it. §4 class 4's own carve-out confirmed disjoint from class 3: "A C6 audit failure or a seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class." | YES
`CENSUS_CONTROL_SPLIT` | C2: `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .` exits 1 in seat A and 0 in seat B, persisting after two attempts. | §4 class 7: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." Disjoint from class 4 (which requires failure in EVERY seat), and placed second in the filing order — the exact gap the V4 repair closed (§4 note: the old wording "in both seats" left this state with no class). | YES
`CENSUS_DENOMINATOR_DISPUTED` | Enumeration: seat A includes the passage at file F line 212 printing "0.315" as the paper's own result; seat B records it in the exclusion ledger as `ATTRIBUTED_NOT_DERIVED`; two reconciliation attempts fail. Input-list limb: both seats agree on every candidate, but `r3c2_lane_tools.py merge` exits 1 because their `input_id` sets for an agreed claim differ, and the difference survives the one reconciliation. | §1: inclusion assigned independently by two seats; "disagreement on any candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)." §6 limb A: tolerance zero, measured in candidate passages. C3 lane block: "`merge` exits 1 if the two `input_id` sets differ — … an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations." §4 class 5 names both limbs. Third in the filing order. | YES
`CENSUS_ORIGIN_DISPUTED` | Corpus of 10 included claims. The sentence "We adopt H₀ = 67.4 from Planck (2018)" supplies an input in 2 of the 10 (20% > 10%). Seat A files origin `CHOSEN` (`ORIG_CHOICE_STATED`); seat B files `IMPORTED` (`ORIG_CITATION`) with its own quotation. | C3: "Every input's `origin` is classified independently by both seats." C6: "An input on which the two classifications disagree is filed `ORIGIN_DISPUTED` and reported with both seats' classification and both quotations; it is not reconciled. Above 10% of included claims, `CENSUS_ORIGIN_DISPUTED`." §4 class 6: "The census does not proceed; every disputed input is listed with both seats' classification and both quotations." (The reason-code precedence — citation before choice — exists precisely so honest seats normally agree; a surviving disagreement above threshold is the class's domain. The lane-side merged record would carry `origin_alt`/`origin_evidence_alt`, and the claim's `rests_on` is computed under both and marked `DISPUTED` — C3 lane block.) Fourth in the filing order. | YES
`CENSUS_AUDIT_FAILED` | Three independent witnesses. (i) The third-seat auditor re-derives the `REPRO_EXACT` witness claim and finds the sealed ledger omits an input the stated equation needs (ledger incompleteness), or its re-derived outcome mismatches the sealed one — `C6_AUDIT.json` carries a `MISMATCH`/incompleteness. (ii) The external custodian's seed is never supplied and recorded with receipt T. (iii) After opening, Blanc's re-hash of the tally or the protocol mismatches receipt P or T. | §4 class 3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed; report which." §6: "Any outcome the audit cannot reproduce, or any ledger incompleteness, files `CENSUS_AUDIT_FAILED`" and "If the seed is not supplied and recorded with the receipt, the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named." §7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED` (§4, whose definition now names this case)." Fifth in the filing order; §4 class 4 explicitly routes audit/seal failures here rather than to `R3C2_NO_CLASS`. | YES
`CENSUS_PARTIAL` | Corpus: the three included claims of the `REPRO_EXACT`, `REPRO_FAILED` and `REPRO_BLOCKED` witnesses above. After the §2 attempt (one repeat permitted, none needed here), the σ₈ claim carries `REPRO_BLOCKED`. | §4 class 2: "after the §2 attempt (one repeat permitted, meaningful only for `REPRO_NOT_EVALUABLE`), at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`). Report each and why. INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`." Sixth in the filing order: the five earlier classes are checked first and none holds in this witness (controls pass, no split, enumerations and origins agree, audit not reached/not failed). | YES
`CENSUS_COMPLETE` | Corpus: exactly the two included claims of the `REPRO_EXACT` and `REPRO_FAILED` witnesses (denominator 2). Both seats' enumerations and origin classifications agree; controls C0–C5b pass; the third-seat audit re-derives both claims (the full arithmetic group — no sampling discount, §6), re-classifies every origin, and prints `C6_AUDIT.json` with no `MISMATCH` and no incompleteness; the custodian's seed is supplied and receipted; both seal receipts verify. | §4 class 1: "every included claim carries exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`. Report the full tally with its denominator, and the `rests_on` tally beside it — two tallies from one pass." (The `C6_AUDIT_SAMPLE=PASS` conjunct was added at V20, §10.14 kimi D2.) Last in the filing order: every earlier class is checked first — `R3C2_NO_CLASS` (controls pass), `CENSUS_CONTROL_SPLIT` (no split), `CENSUS_DENOMINATOR_DISPUTED` (enumerations and input lists agree), `CENSUS_ORIGIN_DISPUTED` (origins agree), `CENSUS_AUDIT_FAILED` (audit runs to PASS, receipts verify), `CENSUS_PARTIAL` (no non-arithmetic outcome) — none holds, so `CENSUS_COMPLETE` files. | YES

(C) Explicit reachability statement: all six §3 per-claim outcomes are reachable; all seven §4 study-level
classes are reachable. No declared verdict is UNREACHABLE.

## The named suspicion, answered directly

Question: `CENSUS_COMPLETE` requires every included claim to carry an arithmetic-group outcome. In a real corpus
of many papers, does a single blocked, absent-input, or no-derivation-stated claim anywhere force
`CENSUS_PARTIAL`, making `CENSUS_COMPLETE` unreachable in practice?

Answer: REACHABLE.

The routing, both halves:

1. The demotion clause is real and is quoted, not paraphrased. §4 class 2: "at least one included claim carries a
   non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`,
   `REPRO_NOT_EVALUABLE`) … INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`." The §4 filing order
   confirms it: "`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`,
   `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`." So yes — ONE blocked,
   absent, no-derivation or not-evaluable claim anywhere in the corpus files `CENSUS_PARTIAL` and pre-empts
   `CENSUS_COMPLETE`. That is a precedence fact about any corpus containing such a claim.

2. But precedence is not unreachability. `CENSUS_COMPLETE`'s defining condition — "every included claim carries
   exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`" — is satisfiable, and the
   witness above satisfies it: a corpus whose every included claim's inputs are all `PRINTED` or `STANDARD` (so
   every attempt completes into `REPRO_EXACT` or `REPRO_FAILED`), with the audit running to PASS. No clause in
   the document bars that input. Compare the genuinely unreachable case this lane already filed: at V9,
   `REPRO_AFTER_CHOICE` was unreachable because §2 step 4 (admissible-inputs-only) blocked EVERY path into the
   class — "the mandated attempt may not consume that input, and no second attempt is specified" (§10.3) — and
   the option-(c) ruling retired it (§10.4). `CENSUS_COMPLETE` has no such blocking clause; it has an open route
   and a strict gatekeeper.

So the true statement is: `CENSUS_COMPLETE` is reachable but fragile. Its condition is existential over the
input, and the witness exists; whether the real 89-text corpus contains at least one demoting claim is an
empirical property of that corpus, not a property of this document, and C0's remit — "whether each declared
outcome can occur under whatever definition is settled" (§5 C0) — ends at the exhibition. The document neither
requires nor forbids a real corpus to contain such a claim; it only guarantees that IF one exists, the filing is
`CENSUS_PARTIAL`, never a silent `CENSUS_COMPLETE`.

One recorded dependence on this answer, stated rather than assumed: the zero-denominator case. As V20 stands,
"every included claim carries exactly one outcome from the arithmetic group" is vacuously true at denominator
zero, and the clause that would route a zero denominator to `CENSUS_PARTIAL` is kimi C5's optional clause —
escalated to the principal at V19 as a sub-option of the split-class ruling and NOT applied (§10.13; "Escalated,
unchanged" at §10.14). The exhibition above does not rely on the vacuous case: its witness has denominator 2.
If the principal adopts the sub-option, this exhibition stands unchanged; if he does not, the vacuous route into
`CENSUS_COMPLETE` remains open as written. Either way the verdict on the named suspicion is REACHABLE.

## UNREACHABLE verdicts and their blocking clauses

None. No declared §3 outcome and no declared §4 class is unreachable under the V20 text, so there is no blocking
clause to quote. (The clause that demotes `CENSUS_COMPLETE` in any corpus containing a non-arithmetic outcome —
§4 class 2 plus the §4 filing order — is quoted verbatim in the suspicion answer above; it constrains when
`CENSUS_COMPLETE` files, not whether it can.)

## Remarks — declared conditions adjacent to the required rows

- Retired outcome: `REPRO_AFTER_CHOICE` is NOT a declared §3 outcome in V20. It was retired at V10 by the
  option-(c) ruling ("`REPRO_AFTER_CHOICE` — RETIRED at V10 by the principal's ruling adopting option (c)"), its
  content living in the `rests_on` field. No row is owed for it; its V9 unreachability is the contrast case
  cited above.
- Exclusion-ledger kinds (§3): `EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`,
  `ATTRIBUTED_NOT_DERIVED` are not per-claim outcomes ("Candidate exclusions are not per-claim outcomes"), so
  they carry no verdict row; each is trivially exhibitable (a passage printing "(14)" as an equation label;
  "see [37]"; "page 12"; "2018"; "Planck 2018 found Ω_m = 0.315" attributed without derivation). The exclusion
  ledger is reported beside the denominator and audited under C6.
- `rests_on` values (`DERIVED_ONLY`, `USES_CHOSEN`, `USES_FITTED`, `USES_IMPORTED`, `USES_UNDECLARED`,
  `DISPUTED`, `NOT_COMPUTED`) are script-computed ledger fields by the lane-side `compute`, not filed verdicts
  (§3 master-only rule), so they are outside the C0 row set. Each is constructible: `NOT_COMPUTED` — the
  no-derivation witness above (no ledger record); `DISPUTED` — the origin-dispute witness (computed under both
  classifications, printed as a pair); `PARENTS_DISPUTED` — two seats' `derived_from` lists differ, computed
  under both parent lists (C3 lane block, added at V20 per §10.14 kimi D3).
- The §4 open note: a surviving per-claim outcome split after the one §2 step 5 reconciliation has NO declared
  class — "§4 is not exhaustive over that state; a class is not added or redefined by this document's author, so
  the gap is recorded here as open rather than written in" (§4 note under class 5; §2 step 5 calls it "an open
  decision recorded by the lane owner"; the document "is not frozen until that decision is recorded"). This is a
  state without a declared outcome, not an unreachable declared verdict: there is no token to exhibit a path
  INTO, by the document's own deliberate choice, pending the principal's escalated ruling (§10.12–§10.14). It is
  flagged here because C0 also covers "every declared condition," and this condition is declared precisely as
  having no class. It does not change the verdict: PASS requires every DECLARED outcome and class to be
  exhibited, and all are.
- Held-clause status: unlike V9's C0 (which noted the §3 admissibility definition was HELD), V20 contains no held
  clause; the ruling is applied (§10.4). The only unsettled items are the two escalations named above, and this
  exhibition depends on neither.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V20_KIMI_COMPLETE

ACCESS_SHA=944300dc68257c705be1da503660559242256ced061b3ef1503ce44c2e4030cc
C0_REACHABILITY=PASS

# R3C2 — C0 REACHABILITY EXHIBITION against V24e (living draft) — kimi seat, 2026-09-06

## Scope

Read from disk, in full (1104 lines): `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md`. No other file in this
directory was read or sought. This is the C0 exhibition of §5's control: for every per-claim outcome of §3 and
every study-level class of §4, exhibit a concrete input that produces it — a specific claim with specific
inputs, plus the clause path through the document that routes it to that verdict. This exhibition does not gate
the document and does not judge its physics; it asks only whether each declared verdict CAN OCCUR under the
text as it stands.

## What is exhibited against, and what carries no row

- The text as it stands is V24e (living draft, unsigned; V23 remains the signed design of record). §3's
  definition was settled by the principal's ruling "Q-R3C2 c" (2026-09-05 14:08 KST, option (c): one pass, two
  tallies; §10.4). The V5.1 HELD marker was removed at V10; there is no held clause in the text.
- `REPRO_AFTER_CHOICE` is RETIRED (§3 note: "RETIRED at V10 by the principal's ruling adopting option (c) …
  now the `rests_on` field of a `REPRO_WITHIN_STATED_PRECISION` or `REPRO_FAILED` claim, computed by script").
  It is not a §3 outcome and carries no row.
- Candidate exclusions (`EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`,
  `ATTRIBUTED_NOT_DERIVED`) are not per-claim outcomes (§3: "Candidate exclusions are not per-claim
  outcomes") — no rows.
- `PENDING` is a C1 placeholder before limb B, not a §3 outcome — no row.
- `rests_on` values (`DERIVED_ONLY`, `USES_CHOSEN`, `USES_FITTED`, `USES_IMPORTED`, `USES_UNDECLARED`,
  `DISPUTED`, `NOT_COMPUTED`) are a script-computed ledger field beside the outcomes (§3 arithmetic-group note;
  C3 lane-side `compute`), not outcomes — no rows.

## Dependence on the marked core definition

Every row below leans on §1's core question and §3's outcome definitions as settled by the option-(c) ruling;
no row assumes an unsettled reading. The sole unreachable verdict of the V9 C0 round (`REPRO_AFTER_CHOICE`,
unreachable under the pre-ruling derivation-only wording, §10.3) exists no longer as a class. That this
exhibition depends on the ruling having been made is itself recorded, as the brief asks. V24e's own changes
(C4/C5/C5b scope wording admitting the two system binaries and the user site-packages directory taken whole,
digest-pinned) touch no §3 outcome, no §4 class and no precedence order; they alter no row.

## (A) §3 per-claim outcomes — exhibition table

§3 precedence: "Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the
first in this order: `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`,
`REPRO_NOT_EVALUABLE`, then the arithmetic group." The arithmetic group is exactly
`REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`.

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `REPRO_WITHIN_STATED_PRECISION` | Paper P prints "the present age is 13.8 Gyr" as its own result of t0 = ∫₀^∞ dz / ((1+z)√(Ω_m(1+z)³+Ω_Λ)); P prints H₀=67.36, Ω_m=0.3153, Ω_Λ=0.6847, all three on C3's closed list verbatim (status `STANDARD`; the `PRINTED` route is outcome-identical, §2 step 3). No uncertainty stated. Mechanical integration gives 13.797 Gyr, which rounds to 13.8 at the printed precision, half away from zero. | §1 inclusion (printed numeral asserted as P's own result; no excluded kind) → §2 steps 1–3 (recipe extracted; every input `PRINTED`/`STANDARD`) → §2 step 4 ("follow the paper's own recipe, using every value it directs you to use") → §3 precedence: none of the four earlier terminal conditions holds → arithmetic group → "the paper's number follows, within its own stated precision … the reproduced value must round to the printed numeral at that precision" → `REPRO_WITHIN_STATED_PRECISION`, both numbers reported. | yes |
| `REPRO_FAILED` | Same recipe and the same printed `STANDARD` inputs as the row above, but P prints "the present age is 13.2 Gyr". The arithmetic from the stated inputs again gives 13.797 Gyr; 13.797 does not round to 13.2 at the printed precision (and exceeds any stated uncertainty, taken once). | §1 → §2 steps 1–4 (inputs sufficient; arithmetic completes) → §3 precedence: earlier four conditions absent → arithmetic group → "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number" → `REPRO_FAILED`, worded "unreproduced from the stated inputs", both numbers reported. | yes |
| `REPRO_BLOCKED` | P prints "we obtain fσ₈(z=0.5) = 0.470" as its own result of a stated growth-rate equation that needs the linear growth factor D(z); D's value is not printed anywhere in P; P names a source ("growth factors from Smith et al. 2003") that is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`. (Second-limb variant: the named source IS enumerable and pinned, but the value does not machine-match at the cited line.) | §1 → §2 step 3 (`BLOCKED`: "traced to a named source but carrying no machine-matchable value") → §2 IMPORTED rule: "a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files `REPRO_BLOCKED` under §3"; "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt" → §3 precedence: the derivation is stated, so `REPRO_BLOCKED` is the first terminal condition that holds. | yes |
| `REPRO_NOT_EVALUABLE` | P prints "P_NL(k=1 h/Mpc) = 1820 (Mpc/h)³" as its own result of a stated N-body recipe (box 600 Mpc/h, 1024³ particles, every cosmological input printed). The recipe is stated and all inputs are `PRINTED`, but the computation requires machinery this lane does not have → `MACHINERY_UNAVAILABLE`. (Timeout variant: a stated symbolic integral whose evaluation under `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>` exceeds the 120.0-second monotonic deadline → the wrapper prints `SYMBOLIC_TIMEOUT` and exits 124, §9.) | §1 → §2 steps 1–4 (attempt launched with every `PRINTED`/`STANDARD` value; cannot complete) → §3 precedence: `NO_DERIVATION` no, `BLOCKED` no, `ABSENT` no → "the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have" → `REPRO_NOT_EVALUABLE`, printing `SYMBOLIC_TIMEOUT` or `MACHINERY_UNAVAILABLE` and the point reached. | yes |
| `REPRO_NO_DERIVATION_STATED` | P prints "the inferred sound horizon r_d = 147.09 Mpc" as its own result; the only provenance sentence is "we obtained r_d from our standard analysis pipeline" — a procedure named but not specified; no equation and no operations a seat could attempt. | §1 (inclusion is satisfied: a printed numeral asserted as P's own result — §3's own note: "A claim can satisfy §1 … while the paper never says how it was obtained") → §2 step 1 finds no equation to extract → §3: "states no equation or computational procedure that could produce it … A procedure named but not specified … file this class and name the passage" → precedence: `NO_DERIVATION` files first, even where inputs would also be absent or blocked. | yes |
| `REPRO_INPUT_ABSENT` | P prints "the cluster mass is 2.1×10¹⁴ M⊙" as its own result of M = σ²r/G, printing σ = 950 km/s and G from C3's closed list verbatim (`STANDARD`); the radius r is neither printed anywhere in P nor traced to any named source. | §1 → §2 step 3 (r classified `ABSENT`: neither printed nor traced) → §2: "A seat may not supply a value for an `ABSENT` … input. Encountering one ends that claim's attempt" → §3 precedence: `NO_DERIVATION` no, `BLOCKED` no → "an input the equation needs is `ABSENT` from the paper — neither printed nor traced to any named source — so the attempt stops there. Name the input" → `REPRO_INPUT_ABSENT`. | yes |

## (B) §4 study-level classes — exhibition table

§4 precedence: "Exactly one study-level outcome is filed. Where more than one condition holds, file the first
in this order: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`,
`CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`,
`CENSUS_COMPLETE`. Once a stop class applies, later limbs are unreached and their controls are `NOT_RUN`."

| class | concrete input | clause path | reachable |
|---|---|---|---|
| `CENSUS_COMPLETE` | A corpus whose enumeration yields denominator ≥ 1 and in which every included claim is of the §3 rows 1–2 kind. Concrete instance: a one-claim corpus containing only the age claim of row (A)1, filed `REPRO_WITHIN_STATED_PRECISION` by both seats. Controls C0–C5b PASS in every seat that attempted them; the two enumerations agree; the two outcome fields agree; origin classifications agree on every input; the custodian's seed is supplied and receipted; C6 audits the sole arithmetic-group claim under (i) (the (ii) sample is empty when R=0: "when `R` is zero the sample is empty and every included claim is already audited under (i)"), re-derives 13.797 → `MATCH`, no ledger incompleteness → `C6_AUDIT_SAMPLE=PASS`; receipts P and T verify. | §4 precedence falls through in order: `R3C2_NO_CLASS` (no control failure) → `CENSUS_CONTROL_SPLIT` → `CENSUS_DENOMINATOR_DISPUTED` → `CENSUS_OUTCOME_DISPUTED` → `CENSUS_ORIGIN_DISPUTED` → `CENSUS_AUDIT_FAILED` (audit PASS; receipts verify) → `CENSUS_PARTIAL` (no non-arithmetic outcome; denominator not zero) → §4.1: "every included claim carries exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`"; denominator ≥ 1, so the zero-denominator clause does not fire → `CENSUS_COMPLETE`, the reproduction tally and the `rests_on` tally reported beside it. | yes — conditional: only over an all-arithmetic-group corpus with denominator ≥ 1 and a passing C6 audit (see the suspicion section below) |
| `CENSUS_PARTIAL` | Route A: the row (A)3 corpus — one included claim whose BLOCKED D(z) input files `REPRO_BLOCKED`; all controls pass; enumerations, outcome fields and origin classifications agree; C6 samples the one non-arithmetic claim under (ii) (N=1, R=1, k = min(max(1, ⌈0.2×1⌉), 1) = 1), confirms `REPRO_BLOCKED` → `MATCH`, audit PASS. Route B: the empty enumeration — every enumerated candidate is excluded (equation numbers, reference numbers, dates, attributed-not-derived); denominator zero. | Precedence falls through the stop, dispute and audit classes → §4.2: "at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`), or the denominator is zero" — true by either route → `CENSUS_PARTIAL`, "INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`". Route B additionally fires §4.1's own clause: "A denominator of zero files `CENSUS_PARTIAL` with the empty enumeration named; no census is complete over nothing." | yes (two routes) |
| `CENSUS_AUDIT_FAILED` | Route A: the row (A)1 one-claim corpus; the C6 auditor, without sight of earlier work and re-classifying every origin from the pinned sources, re-derives the age claim and obtains 13.65 Gyr → `MISMATCH` against the sealed `REPRO_WITHIN_STATED_PRECISION`. Route B: the external custodian's seed is never supplied and recorded with receipt T. Route C: Blanc's post-opening re-hash finds the tally digest does not match receipt T. | C6: "Any outcome the audit cannot reproduce, or any ledger incompleteness, files `CENSUS_AUDIT_FAILED`"; "`C6_AUDIT_SAMPLE=PASS` only if that artefact exists, is printed, and carries no `MISMATCH` and no incompleteness"; Route B — C6: "If the seed is not supplied and recorded with the receipt, the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named" → §4.3: "cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails. No tally is filed"; Route C — §7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED`"; §4.4: "A C6 audit failure or a seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class." | yes (three routes) |
| `R3C2_NO_CLASS` | C5 fails in every seat that attempted it after two attempts: on both seats, twice each, the manifest digest from C5's fifth command (`cd <the directory (4) printed> && find . -type f -print0 \| sort -z \| xargs -0 /usr/bin/shasum -a 256 \| /usr/bin/shasum -a 256`) mismatches the digest pinned in the dispatch record → `C5_HARNESS_PINNED=FAIL` in both seats. Pre-dispatch variant: the packet builder's forbidden-list assertion finds a surviving string → "the packet is not written and `C4_PACKET_REDACTED=FAIL`" → "a packet or seat-isolation failure before dispatch files this class." | §4.4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class" → precedence position 1, filed before any limb; "Once a stop class applies, later limbs are unreached and their controls are `NOT_RUN`." | yes |
| `CENSUS_DENOMINATOR_DISPUTED` | Route A: candidate "13.8 Gyr" at P line 402 — seat A includes it as P's own result, seat B excludes it as attributed-not-derived; the disagreement survives two reconciliation attempts. Route B: both seats agree on every included claim, but seat A's input list for the age claim carries Ω_b h² and seat B's omits it; `r3c2_lane_tools.py merge` exits 1 (the two `input_id` sets differ); the one reconciliation against the paper's stated equation does not resolve it. | Route A — §1: "disagreement on any candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)"; §6 limb A: "tolerance zero, measured in candidate passages". Route B — C3 merge clause: "if `merge` exits 1, the two seats reconcile their input lists against the paper's stated equation once; an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations" → §4.5: "the two enumerations disagree after two reconciliation attempts, or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation". | yes (two routes) |
| `CENSUS_OUTCOME_DISPUTED` | The row (A)1 age claim. Seat A's mechanical evaluation yields 13.797 Gyr → rounds to 13.8 → `REPRO_WITHIN_STATED_PRECISION`. Seat B's yields 13.85 Gyr → rounds to 13.9 → `REPRO_FAILED`. The single reconciliation against the printed numeral and the stated-precision rule of §3 does not reconcile them: the divergence is in the two computed values, not in the rule. | §2 step 5: "the sealed reproduction tally is the merged candidate file on which the two seats' `outcome` fields agree, claim by claim, after one reconciliation against the printed numeral and the stated-precision rule of §3; a disagreement surviving that reconciliation files `CENSUS_OUTCOME_DISPUTED` (§4)" → §4.6: "the two seats' filed per-claim outcomes on an agreed included claim differ after one reconciliation … the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached". Precedence: enumerations and input lists agree, so `CENSUS_DENOMINATOR_DISPUTED`'s condition is false. | yes |
| `CENSUS_ORIGIN_DISPUTED` | A 10-claim corpus. On the inputs of 2 claims the two seats' independent `origin` classifications differ — for "we adopt H₀ = 67.4 from Planck (2018)" seat A files `IMPORTED`/`ORIG_CITATION` and seat B files `CHOSEN`/`ORIG_CHOICE_STATED`, each with a machine-matched quotation; the merged records carry `origin_alt`/`origin_evidence_alt`; disputes are reported, never reconciled. 2 of 10 included claims = 20% > 10%. | C3: "Every input's `origin` is classified independently by both seats"; C3 merge: "where the two `origin` classifications differ the merged record carries `origin_alt` and `origin_evidence_alt`" → C6: "An input on which the two classifications disagree is filed `ORIGIN_DISPUTED` and reported with both seats' classification and both quotations; it is not reconciled. Above 10% of included claims, `CENSUS_ORIGIN_DISPUTED`" → §4.7: "disagree on inputs affecting more than 10% of included claims. The census does not proceed; every disputed input is listed with both seats' classification and both quotations". Precedence: denominator and outcome conditions false. | yes |
| `CENSUS_CONTROL_SPLIT` | C2: seat A's input ledger fails validation — one `PRINTED` value does not machine-match the text at its cited source line, `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .` exits 1 — while seat B's ledger validates, exit 0; the split stands after two attempts. | §4.8: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result." Precedence position 2: `R3C2_NO_CLASS`'s every-seat-fails condition is false — seat B passed. | yes |

## (C) The CENSUS_COMPLETE suspicion — direct answer

REACHABLE.

The suspicion: `CENSUS_COMPLETE` requires every included claim to carry an outcome from the arithmetic group,
so in a real corpus of many papers a single blocked, absent-input, or no-derivation-stated claim anywhere
forces `CENSUS_PARTIAL` — is `CENSUS_COMPLETE` reachable at all, or unreachable in practice?

Answer as reachability: REACHABLE. There exists an input that files it — the (B) table's first row: a corpus
with denominator ≥ 1 whose every included claim files `REPRO_WITHIN_STATED_PRECISION` or `REPRO_FAILED`, with
`C6_AUDIT_SAMPLE=PASS`. The class is not empty by construction, and that is what C0 asks: whether the verdict
CAN OCCUR.

The forcing the suspicion names is real, and here is its exact routing through the text. Take any corpus in
which at least one included claim has: (i) an input neither printed nor traced to any named source → §3
`REPRO_INPUT_ABSENT`; (ii) an input traced to a named source that is unpinned, or unmatched at the cited line →
§3 `REPRO_BLOCKED`; (iii) no stated equation or computational procedure → §3 `REPRO_NO_DERIVATION_STATED`; or
(iv) an attempt that cannot complete within 120 s or lacks machinery → §3 `REPRO_NOT_EVALUABLE`. Then:

1. §4.2's condition is true: "at least one included claim carries a non-arithmetic outcome
   (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`), or the
   denominator is zero".
2. §4's precedence lists `CENSUS_PARTIAL` immediately before `CENSUS_COMPLETE`, and §4.2 says "it takes
   precedence over `CENSUS_COMPLETE`".
3. Therefore `CENSUS_PARTIAL` is filed and `CENSUS_COMPLETE` is unreached for that corpus. One such claim
   anywhere in the corpus is sufficient — a single blocked, absent-input, no-derivation-stated or
   not-evaluable claim forces `CENSUS_PARTIAL`.

So `CENSUS_COMPLETE` is reachable exactly over corpora with zero non-arithmetic outcomes, denominator ≥ 1, and
a passing C6 audit. Whether the pinned corpus (§10.5 records 89 enumerable texts, 106,676 non-blank lines) is
such a corpus is the empirical question the census exists to answer — a property of the corpus, not of the
class definitions. A verdict that requires the evidence to come out a particular way is not unreachable;
unreachable would mean no input can produce it, and the (B) table exhibits an input that can. Stated against
the text as it stands: `CENSUS_COMPLETE` is REACHABLE, and fragile exactly as the design intends — the
fragility is the census's question, recorded here as the direct answer C0 asks for.

## UNREACHABLE verdicts and their blocking clauses

None. Every per-claim outcome of §3 (six of six) and every study-level class of §4 (eight of eight) was
exhibited with a concrete producing input above. Had any verdict been unexhibitable, the clause blocking every
path would be quoted verbatim here; no such clause was needed.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V24E_KIMI_COMPLETE

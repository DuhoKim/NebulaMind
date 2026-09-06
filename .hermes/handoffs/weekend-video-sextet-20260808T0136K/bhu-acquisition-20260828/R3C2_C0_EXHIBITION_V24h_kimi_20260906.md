ACCESS_SHA=a12791ced815ed9f10981f41eec5440ba6dc61f4868c82bdc906ddeefe0f0c4e
C0_REACHABILITY=PASS

# R3C2 — C0 REACHABILITY EXHIBITION, V24h (kimi seat, 2026-09-06)

Exhibited against `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` (V24h, living draft), read from disk in full
(1135 lines; the ACCESS_SHA above is the shasum -a 256 of that exact file, computed by this seat before reading).
No other file in the directory was opened. This is an exhibition, not a gate: it asks only whether each declared
verdict CAN OCCUR under the text as it stands. It does not judge the design and does not judge any physics.

Textual state relied on, stated up front:
- §3's definition is settled: option (c), "one pass, two tallies", adopted by the principal's ruling "Q-R3C2 c"
  (§10.4). There is NO held clause anywhere in V24h; the HELD marker was removed at V10 (§10.4).
- `REPRO_AFTER_CHOICE` is RETIRED (§3 redacted note; §10.4) into the script-computed `rests_on` field. It is not a
  §3 outcome of the current text and owes no exhibition row. It is the only class ever filed unreachable in this
  study's history (V9, §10.3); its retirement is the ruling's, not a repair's.
- The V24-series deltas (§10.18, V24 through V24h) touch only C4/C5/C5b scope-and-harness clauses. No §3 outcome,
  §4 class, precedence order, or tally rule changed in the V24 series; these exhibitions also hold against §3/§4
  of the signed design of record (V23).
- Marked-§1 dependence, stated rather than assumed: §1's question sentence is interrupted by `SEAT-REDACT` spans.
  The master reads the two-part question (the reproduction verdict; and what the number rests on). The packet built
  from this master reads only the reproduction question plus "The reproduction verdict and the provenance fields
  are recorded separately." Consequence for this exhibition: every §3 outcome, the arithmetic group, both
  precedence orders, and every §4 class are defined in SEAT-VISIBLE text, so the rows of tables 1 and 2 do not
  depend on the redacted layer. The `rests_on` conditions (supplementary table) exist only in master text —
  lane-side, script-computed by `r3c2_lane_tools.py`, which no seat is given, and a seat never computes or weighs
  the field (option (c); §10.4, §10.11) — so their exhibition is necessarily authored from the master. That
  dependence is itself reported here, as ordered.

All arithmetic inside the concrete inputs below was machine-verified by this seat before filing
(1 − 0.3153 = 0.6847, rounding to 0.68 at two decimals; 1 − 0.31 = 0.69; |0.9698 − 0.96| = 0.0098 against
0.0096 and 0.0100; C6 k = 1 for N = 4, R = 1; 2/10 = 20% > 10%).

## Table 1 — §3 per-claim outcomes (six declared; the arithmetic group is exactly rows 1–2)

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `REPRO_WITHIN_STATED_PRECISION` | In pinned enumerable text T, passage p prints "We find Ω_Λ = 0.68" (dimensionless, stated as a value) with the recipe stated: "Ω_Λ = 1 − Ω_m". Sole input Ω_m = 0.3153 printed verbatim in T and on C3's closed list → `STANDARD`, `ORIG_CONSTANT`, string-equal to the printed value column. No uncertainty stated. Arithmetic: 1 − 0.3153 = 0.6847; printed precision two decimals; 0.6847 rounds to 0.68 = printed (half-away-from-zero not engaged). | §1 inclusion (numeral asserted as the paper's own result) → §2 steps 1–3 (extract; list {Ω_m}; classify `STANDARD`) → §2 step 4 (attempt consumes every `PRINTED`/`STANDARD` record) → §3 precedence: recipe stated (not NO_DERIVATION), no BLOCKED input, no ABSENT input, evaluable in cap → arithmetic group → stated-precision rounding rule met → filed. `rests_on` computed by the lane script: root origin `STANDARD` → `DERIVED_ONLY`, reported beside it. | YES |
| `REPRO_FAILED` | Same passage shape, printed numeral "Ω_Λ = 0.69", same recipe, same `STANDARD` input Ω_m = 0.3153. Arithmetic: 0.6847 → 0.68 ≠ 0.69. The inputs the paper states are sufficient for its recipe; the arithmetic does not give the paper's number. | Identical to row 1 through §2 step 4 → §3 precedence: no terminal condition holds → arithmetic group → number does not follow → `REPRO_FAILED`. Both numbers reported; wording "unreproduced from the stated inputs", never "error". `rests_on` beside it (`DERIVED_ONLY`). | YES |
| `REPRO_BLOCKED` | Passage prints "w₀ = −0.95" as the paper's own result with a stated recipe; required coefficient c is NOT printed in T; T names a source: "the coefficient of Chevallier & Polarski (2001), eq. 7". Limb (a): the named source is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md` (a RAW listing also fails — RAW texts are "not enumerable and are outside the census, visibly", §2). Limb (b): the named source IS enumerable but the value does not machine-match at its cited line. | §1 → §2 steps 1–3 → §2 IMPORTED rule: `PRINTED`-from-source obtains "only when such a match exists; a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files `REPRO_BLOCKED` under §3" → status `BLOCKED`, never consumed; "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." (§2). §3 precedence puts `REPRO_BLOCKED` ahead of ABSENT/NOT_EVALUABLE/arithmetic group. Input and source named. | YES (both limbs) |
| `REPRO_NOT_EVALUABLE` | (SYMBOLIC_TIMEOUT) Passage prints "χ²_min = 142.7" from a fully stated 9-parameter grid minimization with every input `PRINTED`; the mechanical attempt launched through `r3c2_timeout.py` (120.0 s wall-clock, monotonic) exceeds the deadline; the wrapper prints `SYMBOLIC_TIMEOUT` and exits 124 (§9). (MACHINERY_UNAVAILABLE) Passage prints a numeral whose stated recipe requires a Boltzmann-hierarchy integrator this lane does not have. | §1 → §2 steps 1–4 → §3: recipe stated, inputs consumable, attempt cannot complete → `REPRO_NOT_EVALUABLE`; sub-token and "the point reached" printed. Precedence: the three earlier terminal conditions fail, NOT_EVALUABLE holds, arithmetic group unreached. The one permitted repeat (§4.2) is meaningful only for this class. | YES (both sub-tokens) |
| `REPRO_NO_DERIVATION_STATED` | Passage prints "the resulting spectral tilt is α = 0.965" as the paper's own result; the only provenance sentence is "obtained with the pipeline described in §2.3 of this paper" — a procedure named but not specified; no equation and no operations a seat could attempt. | §1 includes it ("A claim can satisfy §1 … while the paper never says how it was obtained", §3 note) → §2 step 1 finds no equation → nothing to attempt → §3 `REPRO_NO_DERIVATION_STATED`; FIRST in the §3 precedence, so it wins even where inputs would also be absent. Passage named. No inputs are listed, so no ledger record exists → `rests_on` `NOT_COMPUTED`. | YES |
| `REPRO_INPUT_ABSENT` | Passage prints "the cooling time is t_cool = 1.3 Gyr" as the paper's own result; recipe stated: t_cool = (3/2)·k_B·T/(n_e·Λ); T printed (`PRINTED`), k_B on the closed list (`STANDARD`), n_e printed (`PRINTED`); Λ (cooling-function value) is neither printed anywhere in T nor traced to any named source. | §1 → §2 steps 1–3 → Λ classified `ABSENT` ("neither printed nor traced to any named source", §3) → "A seat may not supply a value for an `ABSENT` … input. Encountering one ends that claim's attempt." (§2) → §3 `REPRO_INPUT_ABSENT`; the input is named (Λ). Precedence: NO_DERIVATION fails (recipe stated), BLOCKED fails (no named source), so the ABSENT limb files. §3's own distinction honoured: a claim whose inputs ARE stated, chosen or not, is attempted and lands in the arithmetic group (table 2, row 1, third claim). | YES |

Retired, no row owed: `REPRO_AFTER_CHOICE` — retired at V10 by the principal's ruling adopting option (c)
(§3 redacted note; §10.4). Its content lives on as the `rests_on` field (supplementary rows 2–5 below).

## Table 2 — §4 study-level classes (eight declared; filing precedence: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`)

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `CENSUS_COMPLETE` | Corpus Σ₁, three included claims: the row-1 claim (WITHIN), the row-2 claim (FAILED), and a third: "we adopt Ω_m = 0.31 … hence Ω_Λ = 0.69" — input `PRINTED`, `ORIG_CHOICE_STATED` → `CHOSEN`, consumed because arithmetic consumes by status `PRINTED`/`STANDARD` "whatever its origin" (§3); 1 − 0.31 = 0.69 = printed → WITHIN, `rests_on` `USES_CHOSEN`. Every claim: recipe stated, all inputs `PRINTED`/`STANDARD`, every attempt completes in the cap → every claim in the arithmetic group. Both seats' enumerations agree; input lists agree (merge exit 0); outcomes agree; origins agree. C1–C5b PASS in both seats. C6: custodian seed supplied and recorded with receipt T; auditor audits all three claims under limb (i) (R = 0 → empty sample), re-derives outcomes, re-classifies origins: no MISMATCH, ledgers complete → `C6_AUDIT_SAMPLE=PASS`; Blanc's re-hash verifies receipts P and T. | §4 precedence walked in order: `R3C2_NO_CLASS` (no control failed in every seat) → `CENSUS_CONTROL_SPLIT` (none) → `CENSUS_DENOMINATOR_DISPUTED` (enumerations and input lists agree) → `CENSUS_OUTCOME_DISPUTED` (outcomes agree) → `CENSUS_ORIGIN_DISPUTED` (0% ≤ 10%) → `CENSUS_AUDIT_FAILED` (audit ran to PASS; receipts verify) → `CENSUS_PARTIAL` (no non-arithmetic outcome; denominator 3 ≠ 0) → all seven antecedents false → fall-through → `CENSUS_COMPLETE`. Reported: full tally with denominator 3, and the `rests_on` tally beside it (`DERIVED_ONLY` ×2, `USES_CHOSEN` ×1) — two tallies from one pass (§4.1). | YES |
| `CENSUS_PARTIAL` | Limb (a): Σ₂ = Σ₁ plus the row-6 claim → that claim carries `REPRO_INPUT_ABSENT`, a non-arithmetic outcome. Audit still runs and passes (arithmetic group under (i); sample k = min(max(1, ⌈0.20×4⌉), 1) = 1 of the one remaining claim under (ii)). Limb (b): Σ₂′ = an enumeration whose every candidate is an exclusion kind (every numeral a date or a reference number) → denominator zero. | §4.2: "at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`), or the denominator is zero" → `CENSUS_PARTIAL`; limb (b) files it "with the empty enumeration named; no census is complete over nothing" (§4.1). "INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`" (§4.2; precedence order places PARTIAL immediately before COMPLETE). Each non-arithmetic claim reported with its why. | YES (both limbs) |
| `CENSUS_AUDIT_FAILED` | (i) Σ₁ run in which the auditor's independent re-derivation of the row-1 claim yields a reproduced value inconsistent with the sealed one → a `MISMATCH` row in `C6_AUDIT.json`. (ii) The custodian's seed is not supplied and recorded with receipt T → the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`. (iii) Blanc's post-opening re-hash finds the tally hash ≠ receipt T's value, or receipt P is missing. | §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), or the receipt verification of the seal fails" → `CENSUS_AUDIT_FAILED`; C6 names route (ii) verbatim ("the study files `CENSUS_AUDIT_FAILED` with the missing seed named"); §7 names route (iii) ("Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED`"). No tally is filed; report which. The §4.4 carve-out is honoured: this class, not `R3C2_NO_CLASS`, takes C6/seal failures. | YES (three routes) |
| `R3C2_NO_CLASS` | Pre-dispatch limb: the packet builder's redaction assertion finds a forbidden-list string surviving in the built packet → the packet is not written, `C4_PACKET_REDACTED=FAIL` before dispatch. Control limb: C5's fifth command prints a `MANIFEST_SHA256` unequal to the dispatch record's pin in both seats on both attempts → `C5_HARNESS_PINNED=FAIL` in every seat that attempted it after two attempts. | §4.4: "a control among C0 through C5b fails in every seat that attempted it after two attempts; a packet or seat-isolation failure before dispatch files this class" → `R3C2_NO_CLASS`; first in the §4 precedence. Disjoint by text from `CENSUS_AUDIT_FAILED` (C6/seal failures) and from `CENSUS_CONTROL_SPLIT` (failure in every seat, not one). | YES (both limbs) |
| `CENSUS_DENOMINATOR_DISPUTED` | Enumeration limb: candidate passage "we therefore find t₀ = 13.8 Gyr, consistent with Planck (2020)" — seat A includes it (numeral asserted as the paper's own result), seat B excludes it as `ATTRIBUTED_NOT_DERIVED`; two reconciliation attempts fail. Input-list limb: seats agree on every candidate, but for the Ω_Λ claim seat A lists {Ω_m} while seat B lists {Ω_m, Ω_k} (reading the flatness sentence as a further input); `merge` exits 1 (input_id sets differ); the one C3 reconciliation against the stated equation fails. | §1's inclusion rule: disagreement "on any candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)"; §4.5 names both limbs ("or the two seats' input lists for the agreed claims disagree after the one C3 reconciliation"); §6 limb A names the class; C3's lane-side clause routes a surviving input-set difference here with "the disputed inputs listed with both seats' quotations". The census does not proceed. | YES (both limbs) |
| `CENSUS_OUTCOME_DISPUTED` | Claim prints "the tilt is α = 0.96" with the stated uncertainty "accurate at the 1% level"; both seats reproduce 0.9698 from the same `PRINTED`/`STANDARD` inputs. \|Δ\| = 0.0098. Seat A reads the stated uncertainty as 1% of the printed value, 0.0096: 0.0098 > 0.0096 → `REPRO_FAILED`. Seat B reads it as 0.0100 absolute: 0.0098 ≤ 0.0100 → `REPRO_WITHIN_STATED_PRECISION`. The one reconciliation against the printed numeral and the stated-precision rule of §3 is attempted; the rule fixes the test (\|reproduced − printed\| ≤ the stated uncertainty, taken once) but "the 1% level" carries two defensible numerical referents and each seat maintains its reading → the disagreement survives. | §2 step 5: "a disagreement surviving that reconciliation files `CENSUS_OUTCOME_DISPUTED` (§4)" → §4.6: the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached; the census does not proceed. Precedence: third, after NO_CLASS and CONTROL_SPLIT, before ORIGIN_DISPUTED. | YES |
| `CENSUS_ORIGIN_DISPUTED` | Corpus Σ₃, ten included claims; two of them carry the input sentence "we take β = 1/929.25 (see eq. 9)". Seat A files `CHOSEN` (`ORIG_CHOICE_STATED`, quotation "we take β = 1/929.25"); seat B files `DERIVED` (`ORIG_EQUATION`, citing eq. 9 as the deriving line). Origin disagreements are "reported, never reconciled" (§4.7 note; C6) → 2/10 = 20% > 10% of included claims. | C3: "Every input's `origin` is classified independently by both seats" → lane `merge` carries `origin_alt`/`origin_evidence_alt` → §4.7 threshold "more than 10% of included claims" → `CENSUS_ORIGIN_DISPUTED`; every disputed input listed with both seats' classification and both quotations; the census does not proceed. (At ≤ 10% the census proceeds with the `DISPUTED` pair — supplementary row 6.) | YES |
| `CENSUS_CONTROL_SPLIT` | C5 in seat A fails on both attempts (`MANIFEST_SHA256` ≠ dispatch record — its environment drifted after pinning); C5 in seat B passes on both attempts (all five commands exit 0, path and digest equal to the dispatch record's). After two attempts: failed in one seat, passed in another. | §4.8: "a control fails in one seat and passes in another after two attempts" → `CENSUS_CONTROL_SPLIT`; report both seats' outputs and stop; "do not adopt the passing seat's result." Disjoint by text from `R3C2_NO_CLASS` (which requires failure in every seat). Second in the §4 precedence. | YES |

## The suspicion, answered directly: is `CENSUS_COMPLETE` reachable, or does one bad claim anywhere foreclose it?

Answer: REACHABLE.

The clause behind the suspicion is real and is quoted, not paraphrased — §4.2: "at least one included claim
carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`,
`REPRO_NOT_EVALUABLE`), or the denominator is zero. … INCONCLUSIVE, and it takes precedence over
`CENSUS_COMPLETE`." So the suspicion's mechanism is confirmed by the text: exactly one blocked, absent-input,
no-derivation-stated, or not-evaluable claim anywhere in the corpus forces `CENSUS_PARTIAL`, and the §4
precedence (…, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`) guarantees PARTIAL wins the filing.

But a forced-PARTIAL-on-bad-corpora is not an unreachable COMPLETE. Unreachable would mean NO input files it.
Table 2 row 1 exhibits the input: corpus Σ₁, in which every included claim routes through §3's precedence into
the arithmetic group — for each claim the four terminal conditions are false (recipe stated; no input BLOCKED;
no input ABSENT; attempt completes inside the cap), so "then the arithmetic group" is reached claim by claim —
and the study routes through §4's precedence with all seven earlier conditions false, the last of which is
PARTIAL's own antecedent ("no non-arithmetic outcome; denominator 3 ≠ 0"). The fall-through files
`CENSUS_COMPLETE`. The class's domain is exactly "corpora with zero non-arithmetic outcomes and a passing
audit", and that domain is non-empty by construction: Σ₁ is a member.

On the "in practice" sharpening: whether the real pinned corpus (89 enumerable texts, §10.5) contains even one
non-arithmetic claim is the empirical question the census exists to answer. A verdict whose domain is narrow is
not a verdict whose domain is empty; C0 asks whether the verdict CAN OCCUR, and it can. If the text made
`CENSUS_COMPLETE` unfileable in principle, the census's headline outcome would be foreclosed by construction —
the R3D failure mode C0 was added to catch (§5, C0 note). It is not foreclosed: the path in row 1 is licensed by
every clause it passes through, and no clause in V24h blocks it.

## Supplementary table — every other declared condition (C0: "for every declared condition"), each exhibited reachable

| condition | concrete input | reachable |
|---|---|---|
| `rests_on` = `DERIVED_ONLY` | Table 1 row 1: sole root origin `STANDARD`; master rule: "`DERIVED_ONLY` when every root origin is `DERIVED`, `STANDARD` or `MEASURED`". | YES |
| `rests_on` = `USES_CHOSEN` | Table 2 row 1, third claim: printed-and-chosen Ω_m = 0.31 consumed (status `PRINTED`, origin `CHOSEN`); the claim reproduces and the provenance rides beside it. This is the old β = 1/929.25 case given a home by option (c) (§10.2, §10.5 Q1). | YES |
| `rests_on` = `USES_FITTED` | Row-1 variant: printed input introduced "from our fit, f = 0.31" (`ORIG_FIT_STATED` → `FITTED` root); severity order selects `USES_FITTED` over `USES_CHOSEN` when both are present. | YES |
| `rests_on` = `USES_IMPORTED` | Input unprinted in T but machine-matched at the cited line of another enumerable manifest text: `PRINTED` from that source, `origin` `IMPORTED`, `ORIG_CITATION` (§2 IMPORTED rule). | YES |
| `rests_on` = `USES_UNDECLARED` | Printed input with no provenance sentence; `ORIG_SILENT` record printing its `origin_search` {query, files, matches}; `UNDECLARED` root; severity order `USES_UNDECLARED` > `USES_IMPORTED` > `USES_FITTED` > `USES_CHOSEN` selects it. | YES |
| `rests_on` = `DISPUTED` (pair) | The β input at ≤ 10% of included claims (1 of 10): carried as a pair computed under both classifications, marked `DISPUTED`; the `rests_on` tally reports a `DISPUTED` row; the census proceeds (§4.7 threshold not crossed; C6 disputed-root clause). | YES |
| `rests_on` = `NOT_COMPUTED` | Table 1 row 5: no equation → no ledger record → "`rests_on` `NOT_COMPUTED`, and the `rests_on` tally reports a `NOT_COMPUTED` row" (§3). | YES |
| `PARENTS_DISPUTED` (pair) | Seats' `derived_from` lists for a `DERIVED` record differ; merged record carries both parent lists marked `PARENTS_DISPUTED`; `compute` derives `root_origins` under both, printed as a pair (C3 lane-side clause). | YES |
| `SYMBOLIC_TIMEOUT` / `MACHINERY_UNAVAILABLE` | Table 1 row 4, both sub-tokens. | YES |
| `REPRO_BLOCKED`, limb (b) | Named source IS enumerable in the manifest but the cited line carries no machine-matchable value (§2; §3 second limb). | YES |
| Exclusion kinds: `EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`, `ATTRIBUTED_NOT_DERIVED` | Candidates "(42)", "[17]", "p. 1342", "2019", and "Planck 2018 gives Ω_m = 0.3153" (attributed, not derived): each fails the §1 definition "by definition and not by taste" and is recorded in the exclusion ledger with file, line, numeral, kind (§3 exclusion clause). "Candidate exclusions are not per-claim outcomes." | YES (all five) |
| Zero denominator → `CENSUS_PARTIAL` | Table 2 row 2, limb (b): "no census is complete over nothing" (§4.1/§4.2). | YES |
| One repeat, meaningful only for `REPRO_NOT_EVALUABLE` | Row-4 claim re-attempted once (§4.2); on a second-attempt completion inside the cap the claim proceeds into the arithmetic group. | YES |
| C6 sample edges | R = 0 (Σ₁: empty sample, every claim audited under (i)); N = 4, R = 1 → k = min(max(1, ⌈0.20×4⌉), 1) = 1 (Σ₂). Formula verified arithmetically. | YES |

## UNREACHABLE verdicts and their blocking clauses

NONE. Every §3 per-claim outcome (6/6), every §4 study-level class (8/8), and every declared condition listed
above is exhibited with a concrete input and a clause path through the current text. No blocking clause exists to
quote, and none is invented. For the record: the sole unreachable filing in this study's history was
`REPRO_AFTER_CHOICE` at V9 (§10.3), retired by the principal's ruling at V10 (§10.4); it is not an outcome of the
text exhibited here.

## Explicit reachability roster (per item (C) of the brief)

§3 per-claim outcomes: `REPRO_WITHIN_STATED_PRECISION` YES — `REPRO_FAILED` YES — `REPRO_BLOCKED` YES —
`REPRO_NOT_EVALUABLE` YES — `REPRO_NO_DERIVATION_STATED` YES — `REPRO_INPUT_ABSENT` YES.
§4 study-level classes: `CENSUS_COMPLETE` YES — `CENSUS_PARTIAL` YES — `CENSUS_AUDIT_FAILED` YES —
`R3C2_NO_CLASS` YES — `CENSUS_DENOMINATOR_DISPUTED` YES — `CENSUS_OUTCOME_DISPUTED` YES —
`CENSUS_ORIGIN_DISPUTED` YES — `CENSUS_CONTROL_SPLIT` YES.

Two closing tokens, deliberately distinct (this study's record carries a duplicated-token scar, §10 item 1): the
exhibition closes with `R3C2_C0_EXHIBITION_COMPLETE`; this file's completion token is `R3C2_C0_V24H_KIMI_COMPLETE`.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V24H_KIMI_COMPLETE

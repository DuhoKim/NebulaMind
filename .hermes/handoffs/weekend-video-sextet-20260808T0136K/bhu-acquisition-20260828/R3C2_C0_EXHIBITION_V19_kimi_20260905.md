ACCESS_SHA=a0cf4d5cae4a2b744fead10a7ee09d72479cf6e8a8ddc7ef622b81167f6ea9af
C0_REACHABILITY=PASS

# R3-C2 V19 — C0 reachability exhibition (kimi seat, 2026-09-05)

Document exhibited: `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` (Version 19, §10.13), read from disk in
full; access proven by the shasum on line 1, computed this session against the file on disk.
This is an exhibition only — not a gate, and not a judgement of the design or its physics.

Definition status: §3's core definition is SETTLED, not held. Duho's ruling "Q-R3C2 c" (2026-09-05 14:08 KST,
recorded §10.4) adopted option (c) — one pass, two tallies — and the `HELD PENDING DUHO'S RULING` marker was
removed at V10 (its text preserved in §10.4 in the past tense). The wording is treated exactly as it stands;
no row below assumes a reading. Where §1 is interrupted by `SEAT-REDACT` spans, the visible operative rule —
the quantitative-claim definition, the five exclusion kinds, two-seat inclusion with two reconciliation
attempts — is complete and is all this exhibition uses. `REPRO_AFTER_CHOICE` is retired at V10 (§10.4) into
the script-computed `rests_on` field; it is not a declared §3 outcome of V19 and has no row here.

## A. §3 per-claim outcomes — six declared, all exhibited

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `REPRO_EXACT` | Claim: paper prints "d = 30.0 Mpc" as its own result, states `d = cz/H₀`, and prints `z = 0.007`, `c = 3.00e5 km/s`, `H₀ = 70.0 km/s/Mpc` — all status `PRINTED`. 0.007 × 3.00e5 / 70.0 = 30.0, which rounds to the printed numeral at the printed precision. Variants exhibited: symmetric uncertainty — prints "30.0 ± 0.5 Mpc", reproduced 30.4, \|30.4−30.0\| = 0.4 ≤ 0.5 → EXACT; asymmetric — prints "30.0 +0.4/−0.2 Mpc", reproduced 29.85 falls below, half-width on that side 0.2, \|29.85−30.0\| = 0.15 ≤ 0.2 → EXACT; `STANDARD` route — paper prints "H₀ = 67.36 km s⁻¹ Mpc⁻¹", verbatim on C3's closed list → `STANDARD` record consumed identically. | §1 include → §2 steps 1–3 (extract, list, classify `PRINTED`/`STANDARD`) → §2 step 4 (mechanical attempt consumes every `PRINTED`/`STANDARD` record) → §2 step 5 → §3 `REPRO_EXACT`; no stated uncertainty → "the reproduced value must round to the printed numeral at that precision"; uncertainty stated → "\|reproduced − printed\| ≤ the stated uncertainty, taken once"; asymmetric → "the half-width on the side the reproduced value falls" | YES |
| `REPRO_FAILED` | Same claim, but the paper prints "d = 28.5 Mpc". The stated inputs (`z`, `c`, `H₀`, all printed) are sufficient for the stated recipe, and the arithmetic gives 30.0 — not the paper's number. Report both numbers as "unreproduced from the stated inputs". | §2 steps 1–4 (inputs sufficient, attempt run to completion) → §3 `REPRO_FAILED`: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number" | YES |
| `REPRO_BLOCKED` | Limb (a): paper's recipe needs `σ₈`, prints no value for it, and names a source — "we adopt the σ₈ normalization of Smith & Jones (2019)" — where that source is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`. Limb (b): the named source IS an enumerable pinned text, but the value does not machine-match at the cited line (e.g., the cited line prints a different quantity's value). Record: status `BLOCKED`, `origin` `IMPORTED`, `ORIG_CITATION` evidence to the claiming paper's naming sentence, no value; arithmetic never consumes it. | §2 IMPORTED rule: a cited value is `PRINTED` from the named source "only when such a match exists; a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files `REPRO_BLOCKED` under §3" → §3 `REPRO_BLOCKED`, name the input and the source; precedence position 2 puts `BLOCKED` before `REPRO_INPUT_ABSENT` | YES (both limbs) |
| `REPRO_NOT_EVALUABLE` | Limb `SYMBOLIC_TIMEOUT`: the paper states a symbolic integral whose evaluation under the committed wrapper `r3c2_timeout.py 120.0 -- <command>` exceeds the 120.0-second monotonic deadline; the wrapper prints `SYMBOLIC_TIMEOUT` and exits 124 (its five-second-sleep control timed out at 1.003 s under a one-second cap, §10.10). Limb `MACHINERY_UNAVAILABLE`: the paper states its equations and directs solution by a numerical Boltzmann solver — a stated, specified procedure requiring machinery this lane does not have (distinct from `REPRO_NO_DERIVATION_STATED`: an equation plus a specified solver is something to attempt, so precedence position 1 does not hold). | §9 (wrapper, deadline, exit 124 as "the reportable outcome") → §3 `REPRO_NOT_EVALUABLE`: "Print `SYMBOLIC_TIMEOUT` when the 120-second cap is exceeded, or `MACHINERY_UNAVAILABLE` when the lane lacks the machinery, and the point reached"; one repeat permitted (§4.2), `attempts` ∈ {0,1,2} (C1) | YES (both limbs) |
| `REPRO_NO_DERIVATION_STATED` | Paper prints "we find fσ₈(z = 0.5) = 0.470" as its own result, and nowhere states an equation or computational procedure that produces it. V19 variant: "the growth rate was obtained from a likelihood analysis" — a procedure named but not specified, "a sentence that says where the number came from without stating operations a seat could attempt". | §1 include (a printed numeral asserted as the paper's own result) → §2 step 1 finds nothing to attempt → §3 `REPRO_NO_DERIVATION_STATED`, name the passage; precedence position 1 | YES |
| `REPRO_INPUT_ABSENT` | Paper states `d = cz/H₀` and prints `z` and `c`, but `H₀` is neither printed nor traced to any named source (no citation sentence exists for it — that is what separates this from `REPRO_BLOCKED`). | §2 step 3 classify `ABSENT` → §2: "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." → §3 `REPRO_INPUT_ABSENT`, name the input; precedence position 3 | YES |

## B. §4 study-level classes — seven declared, all exhibited (rows in the §4 filing-precedence order)

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `R3C2_NO_CLASS` | C5 harness: `/usr/bin/python3 -c "import sympy; print(sympy.__version__)"` exits 1 (`ModuleNotFoundError`) in both seats, on both attempts — a control among C0–C5b fails in every seat that attempted it after two attempts. Pre-dispatch limb: the dispatch copy is missing `r3c2_timeout.py` from C4's listed contents → packet/seat-isolation failure before dispatch. | §4.4; precedence position 1. Bounded per V14: "A C6 audit failure or a seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class." | YES |
| `CENSUS_CONTROL_SPLIT` | C2 input-ledger validation: `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .` exits 0 for seat A and 1 for seat B (a `PRINTED` value fails machine-match in B's ledger), stable across two attempts — fails in one seat, passes in another. | §4.7: "Report both seats' outputs and stop; do not adopt the passing seat's result." Precedence position 2. | YES |
| `CENSUS_DENOMINATOR_DISPUTED` | Limb (a): seat A includes candidate passage P ("13.8 Gyr" asserted as the paper's own result); seat B excludes it as `ATTRIBUTED_NOT_DERIVED`; the disagreement survives two reconciliation attempts (tolerance zero, measured in candidate passages). Limb (b): the enumerations agree, but seat A's input list for agreed claim Q is {H₀, z, c} and seat B's is {H₀, z}; `r3c2_lane_tools.py merge` exits 1; the difference survives the one reconciliation against the paper's stated equation. | §1 (two-reconciliation stop) / §6 limb A / C3 merge exit-1 clause ("stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations") → §4.5. Precedence position 3. | YES (both limbs) |
| `CENSUS_ORIGIN_DISPUTED` | 20 included claims; the two seats' independent `origin` classifications split on the sentence "We adopt H₀ = 67.4 from Planck (2018)" (the document's own C3 example) — seat A files `ORIG_CITATION`→`IMPORTED`, seat B files `ORIG_CHOICE_STATED`→`CHOSEN` — on inputs affecting 3 claims = 15% > 10%. | C3 ("Every input's `origin` is classified independently by both seats"; reported, never reconciled) → C6 ("Above 10% of included claims, `CENSUS_ORIGIN_DISPUTED`") → §4.6, every disputed input listed with both classifications and both quotations. Precedence position 4. | YES |
| `CENSUS_AUDIT_FAILED` | Four exhibited limbs: (i) C6 audit — the auditor re-derives sampled claim R and obtains `REPRO_EXACT` where the sealed record says `REPRO_FAILED` → `MISMATCH` in `C6_AUDIT.json`; (ii) the full candidate/exclusion audit finds a passage in a pinned source present in neither ledger → incompleteness; (iii) seal-receipt failure — receipt P or T missing, or Blanc's independent re-hash of the tally or protocol mismatches a receipted value (§7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED`"); (iv) the external custodian's seed is not supplied and recorded with the receipt → audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, study files `CENSUS_AUDIT_FAILED` with the missing seed named (C6). | §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or the receipt verification of the seal fails. No tally is filed; report which." Precedence position 5. | YES (all limbs) |
| `CENSUS_PARTIAL` | 50 included claims; 49 file arithmetic-group outcomes, and claim #37 files `REPRO_INPUT_ABSENT` (`H₀` neither printed nor traced to any named source). One non-arithmetic outcome anywhere suffices. | §4.2: "at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`). Report each and why. INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`." Precedence position 6. | YES |
| `CENSUS_COMPLETE` | 3 included claims, every one arithmetic-group: C1 prints "d = 30.0 Mpc" with all inputs `PRINTED`, recipe gives 30.0 → `REPRO_EXACT`; C2 prints "d = 28.5 Mpc" whose stated inputs give 30.0 → `REPRO_FAILED` (still the arithmetic group — a wrong number does not block COMPLETE); C3 prints "ρ_c = 8.5e-27 kg/m³" from `ρ_c = 3H₀²/8πG` with `H₀` printed verbatim on C3's closed list (`STANDARD` record "67.36") and `G` printed → `REPRO_EXACT`. No claim anywhere is blocked, absent-input, derivationless, or unevaluable. All controls C0–C5b pass in both seats; the enumerations agree; origin disputes ≤ 10%; receipts P and T verify; the C6 audit reproduces every sampled outcome. | §4 precedence positions 1–5 all fail to apply (`R3C2_NO_CLASS` no; `CENSUS_CONTROL_SPLIT` no; `CENSUS_DENOMINATOR_DISPUTED` no; `CENSUS_ORIGIN_DISPUTED` no; `CENSUS_AUDIT_FAILED` no); position 6 fails to apply (zero non-arithmetic outcomes) → §4.1: "every included claim carries exactly one outcome from the arithmetic group of §3" → `CENSUS_COMPLETE`; "Report the full tally with its denominator, and the `rests_on` tally beside it — two tallies from one pass." | YES |

## C. The CENSUS_COMPLETE suspicion — answered directly

REACHABLE.

Routing, shown against the text as it stands:

1. §3: "The arithmetic group is the set of outcomes that state whether the arithmetic reproduced the number:
   exactly `REPRO_EXACT` and `REPRO_FAILED`." A claim whose arithmetic FAILS is still in the group — so
   `CENSUS_COMPLETE` requires attemptability, not correctness. A paper that prints its recipe and every input,
   and whose number is simply wrong, counts toward COMPLETE.
2. §4.1: `CENSUS_COMPLETE` ⇔ every included claim carries exactly one arithmetic-group outcome.
3. §4.2: a single `REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED` or
   `REPRO_NOT_EVALUABLE` outcome anywhere in the corpus files `CENSUS_PARTIAL`, and the §4 precedence
   ("`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`,
   `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE`") puts PARTIAL before COMPLETE. So yes — one
   blocked, absent-input, no-derivation, or unevaluable claim anywhere in the corpus forces `CENSUS_PARTIAL`.
4. But each of those four outcomes requires a specific deficiency in the paper — an unstated procedure, an
   untraced input, a named-but-unpinned or non-matching source, or infeasible arithmetic. §1's inclusion rule
   ("a passage in a pinned source that prints a numeral the paper asserts as a result of its own") requires no
   such deficiency; nothing in the document forces any included claim to carry one. The exhibiting input in
   row B7 — a corpus in which every paper prints its recipe and all of its inputs — routes through precedence
   positions 1–6 untouched and lands in `CENSUS_COMPLETE`. The class's domain is exactly the arithmetic-clean
   corpora, and that domain is non-empty. It is narrow — the document's own C0 note (§5) says a single blocked
   or absent input in the whole corpus is enough to prevent it — but narrow is not unreachable.
5. Whether the actual pinned corpus (89 enumerable texts, 106,676 non-blank lines, §10.5) lands in that domain
   is the empirical question the census itself exists to answer. C0 asks only whether the verdict CAN OCCUR on
   some input. It can.

Boundary flag, as the text stands (not judged, reported): a zero-included-claim census vacuously satisfies
§4.1 ("every included claim carries exactly one outcome from the arithmetic group" is true of the empty set;
C6's sample is empty when `R` is zero) and therefore routes to `CENSUS_COMPLETE` under V19 as written. kimi
C5's optional clause — that a zero denominator file `CENSUS_PARTIAL` rather than a vacuous `CENSUS_COMPLETE` —
is escalated as a sub-option of the pending class ruling (§10.13) and is NOT applied, so it is not part of the
text exhibited against.

## D. Supplementary declared conditions (sub-tokens and computed fields), each exhibited

- `SYMBOLIC_TIMEOUT` / `MACHINERY_UNAVAILABLE` — the two limbs of `REPRO_NOT_EVALUABLE`; both exhibited in row A4.
- `REPRO_BLOCKED` limb (a) (named source not an enumerable pinned text) and limb (b) (pinned source, no
  machine-match at the cited line) — both exhibited in row A3.
- `rests_on` values — lane-side, computed by `r3c2_lane_tools.py compute` from root origins, never seat-filed
  (§3 master-only rule): `DERIVED_ONLY` when every root origin is `DERIVED`, `STANDARD` or `MEASURED`
  (exhibited: claim whose inputs are a `MEASURED` redshift, a `STANDARD` closed-list constant, and a `DERIVED`
  quantity with a stated `derived_from` chain); otherwise the most severe root origin present in the fixed
  order `USES_UNDECLARED` > `USES_IMPORTED` > `USES_FITTED` > `USES_CHOSEN` — exhibited respectively by an
  `ORIG_SILENT` record with an adequate printed `origin_search`; an `ORIG_CITATION` record (the Planck
  sentence above); an `ORIG_FIT_STATED` record ("from our fit, α = 0.31"); and an `ORIG_CHOICE_STATED` record
  (the document's own case, entry 59's printed `β = 1/929.25`, §10.2/§10.5). A `DISPUTED` pair — two seats
  split on a root origin at ≤ 10% of claims, `rests_on` computed under both classifications and marked
  `DISPUTED`, with a `DISPUTED` row in the tally. `NOT_COMPUTED` — an included claim with no ledger record
  (e.g., a `REPRO_NO_DERIVATION_STATED` claim: no equation, hence no inputs), with a `NOT_COMPUTED` row in the
  tally. All reachable.
- Exclusion kinds `EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`,
  `ATTRIBUTED_NOT_DERIVED` — §3: "Candidate exclusions are not per-claim outcomes." Not required rows; each is
  exhibitable in one line from the §1 rule (e.g., a numeral that is an equation label → `EQUATION_NUMBER`).

## E. UNREACHABLE verdicts and blocking clauses

None. Every declared §3 per-claim outcome and every declared §4 study-level class has a concrete exhibiting
input above, so there is no blocking clause to quote. `C0_REACHABILITY=PASS` per §5's criterion: every
required row is exhibited.

Two reachable states that land in NO class are documented in the document itself. They are not unreachable
verdicts — no declared row fails — but they are surfaced here rather than absorbed:

1. Per-claim outcome split surviving the one §2 step-5 reconciliation — §4's own note, verbatim:
   "Open (§10.12): the class filed when the two seats' per-claim outcomes on an agreed included claim differ
   after the one reconciliation of §2 step 5 — §4 is not exhaustive over that state; a class is not added or
   redefined by this document's author, so the gap is recorded here as open rather than written in."
   Escalated to the principal (§10.13, options filed 19:48 KST); the document is not freezable until ruled.
2. The zero-denominator census routing to `CENSUS_COMPLETE` as written — escalated sub-option, not applied
   (§10.13; see section C, boundary flag).

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V19_KIMI_COMPLETE

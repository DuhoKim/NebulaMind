ACCESS_SHA=065dc0e48090d7d56625e41e8f517a782640e2b97d5df08423fd38dc4c8e8ee0
C0_REACHABILITY=PASS

# R3C2 — C0 reachability exhibition, V12 (author seat, kimi, 2026-09-05)

Access proof run as the first action, before any read:
`shasum -a 256 /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md`
returned `065dc0e48090d7d56625e41e8f517a782640e2b97d5df08423fd38dc4c8e8ee0`, the value named in the order.

Read in full from disk (719 lines): `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md`. No other file in this
directory was read or sought. Other paths opened: none in the lane; `/tmp/r3c2_c0_calc_check.py` (authored
by this seat, arithmetic check only — every numeric claim below was machine-verified, none computed by hand).

## 0. Standing of the text exhibited against

Exhibited against the text as it stands: **Version 12, option (c) adopted** ("Q-R3C2 c", 2026-09-05 14:08 KST,
recorded §10.4); the HELD marker is removed. Per the brief, the dependence on §1's core definition is stated,
not assumed: every exhibition below routes through §1's inclusion rule — *a passage printing a numeral the
paper asserts as a result of its own*, with the five enumerated excluded kinds — and §1 itself marks that
boundary as **a judgement moved from one reader to two who must agree**, not a mechanical test. §10.3 records
that this seat's lane previously mis-cited that held clause as §1's when it was §3's; the correction is noted,
and this report exhibits against the sections as numbered in the document. That dependence is itself a result:
under the pre-ruling (option b) wording, `REPRO_AFTER_CHOICE` was a declared outcome and was found unreachable
by two agreeing seats (§10.3); under the text as it stands it is **retired into the script-computed `rests_on`
field (§3 parenthetical, §10.4 trace table) and is not a declared outcome of §3**, so it carries no row below.

What counts as a declared outcome or class, from the text:

- **§3 per-claim outcomes (6):** `REPRO_EXACT`, `REPRO_FAILED`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`,
  `REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`. The **arithmetic group is exactly `REPRO_EXACT` and
  `REPRO_FAILED`** (§3). Exclusion kinds are **not** per-claim outcomes ("Candidate exclusions are not
  per-claim outcomes", §3); they are exhibited in §C below because C0 also says "every declared condition".
- **§4 study-level classes (7):** `CENSUS_COMPLETE`, `CENSUS_PARTIAL`, `CENSUS_AUDIT_FAILED`, `R3C2_NO_CLASS`,
  `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_CONTROL_SPLIT`, filed under §4's total
  precedence: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`,
  `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`, `CENSUS_COMPLETE` — first match wins, later limbs `NOT_RUN`.

## A. §3 per-claim outcomes — exhibition table

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `REPRO_EXACT` | Paper P prints "**Ω_b h² = 0.0224**" as its own result, stating the recipe Ω_b h² = Ω_b × h² with printed Ω_b = 0.0493 and printed h = 0.674 (both `PRINTED`; origins cited under C3). Machine check: 0.0493 × 0.674² = 0.0223958068, which rounds to 0.0224 at the printed precision. Second instance, the ruling's canonical case: a claim of the entry-59 type — β = 1/929.25 **printed and chosen** — consumed by the recipe it is printed with. | §1 (printed numeral asserted as own result → included) → §2 steps 1–3 (recipe extracted; inputs listed; both `PRINTED`) → §2 step 4 (mechanical attempt consumes every `PRINTED`/`STANDARD` record, "chosen and fitted values included... following that instruction is reproducing the paper") → product 0.0223958068 → §3 `REPRO_EXACT` ("follows, within its own stated precision"; none stated → "the reproduced value must round to the printed numeral at that precision" — it does); `rests_on` computed by the pinned script beside it (`USES_CHOSEN` for the β case). | yes |
| `REPRO_FAILED` | Paper prints "**Ω_c h² = 0.1188**", recipe Ω_c × h², printed Ω_c = 0.265, printed h = 0.674. Machine check: 0.265 × 0.674² = 0.12038314 → 0.1204 at the printed precision ≠ 0.1188. | §1 → §2 steps 1–3 (inputs sufficient, both `PRINTED`) → §2 step 4 attempt completes → §3 `REPRO_FAILED`: "the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number." Wording per §3: "unreproduced from the stated inputs," not "error." Both numbers reported; `rests_on` beside it. | yes |
| `REPRO_BLOCKED` | Paper prints "**the drag-redshift sound horizon r_d = 147.09 Mpc**" from a stated integral recipe that needs the sound speed c_s(z); the paper does not print c_s but names a source — "the fit of Eisenstein & Hu (1998)" — that is **not** a text in `R3C2_CORPUS_MANIFEST.md` and cannot be obtained by this lane. | §1 → §2 steps 1–2 → §2 step 3: not printed; a source is named → §2's IMPORTED rule applies only when the named source "is itself a text in `R3C2_CORPUS_MANIFEST.md`" — it is not, so the record cannot be `PRINTED`/`IMPORTED` → §3 `REPRO_BLOCKED`: "an input whose value the paper does not print, but for which the paper **names a source (a citation)**, where that source is outside this lane and cannot be obtained. Name it." The §3 named-source test ("Distinct from `REPRO_INPUT_ABSENT`, which is an input the paper neither prints nor traces to any named source") routes it here, and §3's precedence files `REPRO_BLOCKED` before `REPRO_INPUT_ABSENT`. The class's exclusive domain after the named-source test and the IMPORTED rule is exactly *named source, off-manifest, unobtainable* — the text carves that domain explicitly. | yes |
| `REPRO_NOT_EVALUABLE` | Paper prints "**C_l^TT(l=220) = 5750 µK²**" from the full Boltzmann-hierarchy line-of-sight integral; every input `PRINTED` or `STANDARD`, but the evaluation needs numerical machinery this lane does not have (alternatively: a sympy evaluation exceeding the 120-second cap). | §1 → §2 steps 1–4 (attempt begins; no `ABSENT` input, so no earlier terminal condition) → §9's "120-second cap on symbolic operations with `SYMBOLIC_TIMEOUT` as a reportable outcome" → §3 `REPRO_NOT_EVALUABLE`: "the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print `SYMBOLIC_TIMEOUT` and the point reached." | yes |
| `REPRO_NO_DERIVATION_STATED` | Paper prints "**we find w = −1.03**" as its own result and states **no equation or computational procedure** that could produce it. | §1 — included: a printed numeral asserted as the paper's own result; §3's own note: "A claim can satisfy §1... while the paper never says how it was obtained" → §2 step 1 finds no equation to extract → §3 `REPRO_NO_DERIVATION_STATED`: "the paper prints the claim as its own result but states no equation or computational procedure that could produce it, so there is nothing to attempt. Name the passage." First in §3's precedence, so no co-occurring condition can divert the filing. | yes |
| `REPRO_INPUT_ABSENT` | Paper prints "**fσ₈(z = 0.5) = 0.470**" with stated recipe fσ₈ = f·σ₈, f = d ln D/d ln a; σ₈ is `STANDARD` (C3 closed list, 0.8111), but the growth factor D(z = 0.5) the recipe needs is **neither printed nor traced to any named source**. | §1 → §2 steps 1–2 → §2 step 3: D classified `ABSENT`; "A seat may not supply a value for an `ABSENT` input. Encountering one ends that claim's attempt." → §3 `REPRO_INPUT_ABSENT`: "neither printed nor traced to any named source — so the attempt stops there. **Name the input.**" Routing checks: an equation IS stated (so not `REPRO_NO_DERIVATION_STATED`); no source is named (so not `REPRO_BLOCKED`) — consistent with §3's precedence order `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the arithmetic group. | yes |

All six §3 outcomes exhibited. The retired `REPRO_AFTER_CHOICE` carries no row (§0 above): what it recorded
now survives as the `rests_on` field of a `REPRO_EXACT` or `REPRO_FAILED` claim, computed by the pinned
script — exhibited in row A1's β instance.

## B. §4 study-level classes — exhibition table

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `CENSUS_COMPLETE` | Corpus = exactly the two included claims of rows A1 and A2 (one `REPRO_EXACT`, one `REPRO_FAILED`); every control passes in every seat that attempted it; the two enumerations agree on every candidate; origin classifications agree on inputs affecting 100% of included claims; the C6 audit reproduces both outcomes. | Every included claim carries exactly one outcome from the arithmetic group (§3: "exactly `REPRO_EXACT` and `REPRO_FAILED`") → §4.1 condition met → "Report the full tally with its denominator, **and the `rests_on` tally beside it — two tallies from one pass.**" §4 precedence: none of the six earlier conditions holds → `CENSUS_COMPLETE` filed. | yes |
| `CENSUS_PARTIAL` | Corpus = rows A1–A2 **plus** row A6's fσ₈ claim, attempted twice; the D input remains `ABSENT` on both attempts. | §4.2: "after two attempts, **at least one included claim carries a non-arithmetic outcome** (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`). Report each and why. **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.**" §4's filing order places `CENSUS_PARTIAL` immediately before `CENSUS_COMPLETE`. | yes |
| `CENSUS_AUDIT_FAILED` | Corpus as row B1, but the sealed ledger carries claim A2's reproduced value transcribed as 0.1304; the C6 audit seat, without sight of earlier work, re-derives 0.265 × 0.674² = 0.12038314 → 0.1204 from the pinned sources and cannot reproduce the filed outcome (machine check: 0.1204 ≠ 0.1304). Second route: Blanc's post-opening re-hash of the tally or protocol mismatches a value in receipt P or T, or a receipt is missing. | C6: "Any outcome the audit cannot reproduce, or any ledger incompleteness, files `CENSUS_AUDIT_FAILED`." §4.3: "the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, **or the §7 receipt verification fails**. No tally is filed; report which." §7: "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED` (§4, whose definition now names this case)." Reachable by either of two independent routes. | yes |
| `R3C2_NO_CLASS` | Control C2 fails **in both seats after two attempts**: each seat's input ledger twice fails `r3c2_ledger_tools.py validate` (exit 1) — e.g., a `PRINTED` record whose value does not machine-match its cited source line, unrepaired on the second attempt. | §4.4: "a control fails **in every seat that attempted it** after two attempts." First in §4's precedence; once it applies, later limbs are unreached and their controls `NOT_RUN`. | yes |
| `CENSUS_DENOMINATOR_DISPUTED` | Passage at file X line Y prints "w = −1.03"; seat 1 includes it under §1 (asserted as the paper's own result); seat 2 excludes it as `ATTRIBUTED_NOT_DERIVED`; two reconciliation attempts fail to produce agreement. | §1: "disagreement on any candidate stops the study under `CENSUS_DENOMINATOR_DISPUTED`"; §6 limb A: "tolerance zero, measured in candidate passages — stop with `CENSUS_DENOMINATOR_DISPUTED` (§4)"; §4.5: "the two enumerations disagree after two reconciliation attempts. The census does not proceed; the disputed candidates are listed." | yes |
| `CENSUS_ORIGIN_DISPUTED` | 20 included claims; on 3 of them (machine check: 3/20 = 15% > 10%) the seats file different origins for an input — e.g., the sentence "we fit α to the 2015 data and adopt α = 0.5 throughout": seat 1 cites `ORIG_FIT_STATED`, seat 2 cites `ORIG_CHOICE_STATED`, each with its verbatim quotation machine-matched. | C3: "**Every input's `origin` is classified independently by both seats**"; the reason-code precedence resolves only sentences where more than one code matches for one reader — it does not reconcile cross-reader single-code disagreement, and C3/C6 declare such disagreement reported, never reconciled → C6: "An input on which the two classifications disagree is filed `ORIGIN_DISPUTED`... Above 10% of included claims, `CENSUS_ORIGIN_DISPUTED`" → §4.6: "disagree on inputs affecting **more than 10% of included claims**. The census does not proceed; every disputed input is listed with both seats' classification and both quotations." | yes |
| `CENSUS_CONTROL_SPLIT` | Control C2 fails twice in seat 1 (validation exit 1 on both attempts) and passes in seat 2 (exit 0). | §4.7: "a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; **do not adopt the passing seat's result.**" Second in §4's precedence: `R3C2_NO_CLASS` (fails in every seat) and `CENSUS_CONTROL_SPLIT` (fails in exactly some seats) partition the space. | yes |

All seven §4 classes exhibited.

## The named suspicion — CENSUS_COMPLETE, answered directly

**REACHABLE.** The routing, in both directions:

- **The input that files it** (row B1): a corpus whose every included claim (i) states an equation or
  procedure, (ii) has every input `PRINTED` — chosen, fitted and imported values included — or `STANDARD`,
  and (iii) evaluates within the cap. Each such claim routes §2 steps 1–5 into the arithmetic group (§3:
  exactly `REPRO_EXACT`, `REPRO_FAILED`), §4.1's condition is met, no earlier §4 class's condition holds, and
  `CENSUS_COMPLETE` is filed with both tallies. The condition is extensional and the document supplies the
  complete path.
- **The clause that can force it away in practice**: §4.2 — "**at least one included claim carries a
  non-arithmetic outcome** ... INCONCLUSIVE, and **it takes precedence over `CENSUS_COMPLETE`**" — reinforced
  by §4's filing order (`CENSUS_PARTIAL` immediately before `CENSUS_COMPLETE`). So in a real corpus of many
  papers, **a single blocked, absent-input, no-derivation-stated, or timed-out claim anywhere routes the
  study to `CENSUS_PARTIAL`**, and `CENSUS_COMPLETE` can be filed only on a corpus containing zero such claims.

Why that is conditionality, not unreachability: (i) whether the condition holds is a property of the corpus,
not of the document — the exhibit above is concrete and the path is licensed by the text; (ii) under the
settled option-(c) wording the historical *practical* blocker is gone: a printed-but-chosen input (the
document's own entry-59 example, β = 1/929.25) is consumed by the mechanical attempt and lands **inside** the
arithmetic group with `rests_on = USES_CHOSEN` — "PROVENANCE IS RECORDED, NOT FILTERED" (§3), "chosen and
fitted values included" (§2 step 4). Under the retired option-(b) wording such claims could not enter the
arithmetic group at all, which is precisely how `REPRO_AFTER_CHOICE` came back unreachable under two seats
(§10.3). What survives in practice is what the design intends to report: a corpus containing even one
unobtainable citation, one absent input, one derivation-free claim, or one timeout files `CENSUS_PARTIAL` —
"INCONCLUSIVE" — with the offending claim named and why. **Answer: reachable; in practice conditional on the
corpus containing no non-arithmetic outcome, and that condition is stated in the classes themselves.**

## C. Declared conditions supplement (C0: "and for every declared condition")

| condition | concrete input | clause path | reachable |
|---|---|---|---|
| Exclusion kind `EQUATION_NUMBER` | Passage prints "(14)" where 14 numbers an equation | §1 excluded kinds "by definition and not by taste" → §3 exclusion ledger (file, line, numeral, kind), reported alongside the denominator (C1), audited under C6 | yes |
| Exclusion kind `REFERENCE_NUMBER` | Passage prints "[47]" citing reference 47 | same path | yes |
| Exclusion kind `PAGE_OR_LINE_NUMBER` | Passage prints "p. 1141" | same path | yes |
| Exclusion kind `DATE` | Passage prints "2018" as a date | same path | yes |
| Exclusion kind `ATTRIBUTED_NOT_DERIVED` | Passage prints "Planck 2018 reports Ω_m = 0.315" — attributed to another work without deriving | §1 "values the paper attributes to another work without deriving" → same ledger path | yes |
| `SYMBOLIC_TIMEOUT` | Row A4's claim under the 120-second cap | §9 stall guard → §3 `REPRO_NOT_EVALUABLE` ("Print `SYMBOLIC_TIMEOUT` and the point reached") | yes |
| `rests_on` script values | `DERIVED_ONLY` (all roots `DERIVED`/`STANDARD`/`MEASURED`); else most severe in `USES_UNDECLARED` > `USES_IMPORTED` > `USES_FITTED` > `USES_CHOSEN`; `DISPUTED` pair when a root input is `ORIGIN_DISPUTED` | §3 master-only rule and C3: "No seat writes `root_origins` or `rests_on`; the script rejects a ledger that arrives with either set"; C6: "carries `rests_on` computed under both classifications, printed as a pair and marked `DISPUTED`" — accompany rows A1–A2 as ledger states, not per-claim outcomes | yes |
| §3 per-claim precedence | Rows A3–A6 are each constructed so no earlier condition holds (A3: source named; A4: all inputs present; A5: no equation; A6: equation stated, no source) | §3: "Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the first in this order" | yes |
| §4 filing precedence | Each row in §B constructed with all earlier classes' conditions absent; stop classes leave later limbs `NOT_RUN` | §4: "Exactly one study-level outcome is filed. Where more than one condition holds, file the first in this order... Once a stop class applies, later limbs are unreached and their controls are `NOT_RUN`." | yes |

## UNREACHABLE verdicts and their blocking clauses

**None.** Every declared per-claim outcome of §3 (6/6) and every study-level class of §4 (7/7) is exhibited
above with a concrete input and a licensed clause path; the declared conditions supplement is likewise fully
exhibited. No clause blocks any path, so there is no blocking clause to quote. The one historical
unreachability on this document's record — `REPRO_AFTER_CHOICE` under the option-(b) wording (§10.3, two
agreeing seats) — was resolved by the principal's ruling adopting option (c), which retired the class into
the script-computed `rests_on` field; under the text as it stands it is not a declared outcome.

**Verdict: `C0_REACHABILITY=PASS`** — PASS per C0's own rule ("PASS only when every required row has been
independently exhibited"), from this author seat; the second independent seat's verification is a separate
artefact, and both must return PASS before any freeze (C0).

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V12_KIMI_COMPLETE

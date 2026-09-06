ACCESS_SHA=12daf4f5aa9eb89d5411089c1d7120d153caa4f81cb3bf6549c3805bda06f62a
C0_REACHABILITY=PASS

# R3C2 — C0 reachability exhibition on V27 (living draft)

Seat: kimi, 2026-09-06. This is the authoring-seat exhibition under C0 (§5): for **every per-claim
outcome of §3** and **every study-level class of §4** — plus the V27-named conditions in the brief — a
concrete input and the clause path through the document that routes that input to that verdict.

**Read:** `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` only, in full, from disk. No other file in this
directory was read or sought. The access proof on line 1 is the live `shasum -a 256` of that file at the
time of reading.

**Text taken as it stands.** Option (c) is settled (one pass, two tallies; there is no held clause).
`REPRO_AFTER_CHOICE` is RETIRED (§3's own note; the V10 ruling) and is therefore **not a declared
outcome and is not exhibited** — it was the sole unreachable class of the V9 C0 round (§10.3, history
only) and its retirement is exactly what removed that unreachability. §10 is history and binds nothing;
every routing below runs through §§1–9 as they stand in V27. §3 declares **six** per-claim outcomes
(C1 confirms: "one of the six §3 tokens"); §4 declares **eight** study-level classes.

---

## A. §3 per-claim outcomes (six declared)

§3 precedence, quoted: "Exactly one outcome is filed per claim. Where more than one terminal condition
holds, file the first in this order: `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`,
`REPRO_NOT_EVALUABLE`, then the **arithmetic group**." The arithmetic group, quoted: "exactly
`REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`".

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `REPRO_WITHIN_STATED_PRECISION` | Paper prints "we obtain t₀ = 13.8 Gyr" as its own result, states the equation that produces it and prints every input the equation needs (H₀ = 67.36, Ω_m = 0.3153, Ω_Λ = 0.6847, each printed in the paper and each on C3's closed list verbatim). Mechanical evaluation of the stated recipe gives 13.797 Gyr; the paper states no uncertainty, so the printed precision (one decimal) governs: 13.797 rounds to 13.8. | §1 inclusion (a numeral asserted as the paper's own result) → §2 steps 1–3 (extract; list inputs; classify `PRINTED`/`STANDARD`) → §2 step 4 ("Attempt the arithmetic MECHANICALLY — follow the paper's own recipe, using every value it directs you to use, i.e. every ledger record with status `PRINTED` or `STANDARD`") → §3 `REPRO_WITHIN_STATED_PRECISION` + the stated-precision rule ("the reproduced value must round to the printed numeral at that precision, rounding half away from zero") → precedence: no terminal condition holds → arithmetic group → this outcome. | YES |
| `REPRO_FAILED` | Paper prints "Ω_m = 0.3000 ± 0.001" as its own result, states the flatness recipe Ω_m = 1 − Ω_Λ, and prints Ω_Λ = 0.6847 (closed-list verbatim). Inputs are sufficient; arithmetic gives 0.3153; |0.3153 − 0.3000| = 0.0153 > 0.001. | §1 → §2 steps 1–4 (all inputs `PRINTED`/`STANDARD`, attempt completes) → §3 `REPRO_FAILED` ("the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number. Report both numbers.") + the uncertainty test ("|reproduced − printed| ≤ the stated uncertainty, taken once") → precedence: no terminal condition holds → arithmetic group → this outcome. | YES |
| `REPRO_BLOCKED` | Paper prints "we find w = −1.03" as its own result and states the producing equation, which needs an input value the paper does not print, naming a source: "using the prior of Smith et al. (2020)" — a text that is NOT an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`. (Second-limb variant: the named source IS pinned and enumerable but the cited line carries no machine-matching numeric token.) | §1 → §2 step 3 classify (not printed; named-source test) → §2 import rule: "If the named source is not enumerable or the value does not match there, file `REPRO_BLOCKED` under §3" → §3 `REPRO_BLOCKED` (definition covers both limbs: source "is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`" or "is an enumerable pinned text at whose cited line the value does not machine-match") → recorded status `BLOCKED`, never consumed ("A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt.") → precedence: an equation IS stated so `REPRO_NO_DERIVATION_STATED` does not hold; `REPRO_BLOCKED` is next. | YES |
| `REPRO_NOT_EVALUABLE` | Limb (i) `SYMBOLIC_TIMEOUT`: paper prints "σ₈ = 0.811" as its own result with a stated symbolic procedure whose mechanical attempt under `/usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command>` exceeds the 120.0-second monotonic deadline; the wrapper "prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome" (§9). Limb (ii) `MACHINERY_UNAVAILABLE`: paper's stated procedure requires machinery this lane does not have (a numerical Boltzmann code), so the arithmetic cannot be completed; the point reached is printed. | §1 → §2 step 4 attempt → §3 `REPRO_NOT_EVALUABLE` ("the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print `SYMBOLIC_TIMEOUT` when the 120-second cap is exceeded, or `MACHINERY_UNAVAILABLE` when the lane lacks the machinery, and the point reached.") → precedence: `REPRO_NO_DERIVATION_STATED` (a procedure IS stated — no), `REPRO_BLOCKED`/`REPRO_INPUT_ABSENT` (inputs printed — no) → this outcome. | YES |
| `REPRO_NO_DERIVATION_STATED` | Paper prints "the best-fit value is A_s = 2.1 × 10⁻⁹" as its own result but states no equation or computational procedure that could produce it — only "obtained from our likelihood analysis", a procedure named but not specified. | §1 satisfied (a printed numeral asserted as the paper's own result) → §2 step 1: no equation to extract → §3 `REPRO_NO_DERIVATION_STATED` ("states no equation or computational procedure that could produce it, so there is nothing to attempt. Name the passage. A procedure named but not specified … states no computational procedure that could produce it; file this class and name the passage.") → precedence: FIRST in the order, so it is filed even where inputs would also be absent — nothing can mask it. | YES |
| `REPRO_INPUT_ABSENT` | Paper prints "the sound horizon is r_s = 147 Mpc" as its own result and states the producing integral, which needs the recombination redshift z_* — a value the paper neither prints nor traces to any named source. | §1 → §2 step 3 (input `ABSENT`: "neither printed nor traced to any named source") → "A seat may not supply a value for an `ABSENT` or `BLOCKED` input. Encountering one ends that claim's attempt." → §3 `REPRO_INPUT_ABSENT` ("the attempt stops there. Name the input.") → precedence: `REPRO_NO_DERIVATION_STATED` (an equation IS stated — no), `REPRO_BLOCKED` (no source is named — the named-source test separates the classes — no) → this outcome. | YES |

**Retired, not exhibited:** `REPRO_AFTER_CHOICE` appears in §3 only inside a RETIRED note; it is not one
of the six declared tokens. (Historical record only: it was the sole `UNREACHABLE` of the V9 C0 round,
both seats agreeing, §10.3 — under the retired derivation-only wording. The option-(c) ruling retired it
into the script-computed `rests_on` field.)

---

## B. §4 study-level classes (eight declared)

§4 precedence, quoted: "Exactly one study-level outcome is filed. Where more than one condition holds,
file the first in this order: `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`,
`CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`,
`CENSUS_COMPLETE`."

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `R3C2_NO_CLASS` | Pre-dispatch limb: the builder `r3c2_build_seat_packet.py` finds a forbidden-list string surviving in the built packet → `C4_PACKET_REDACTED=FAIL`, the packet is not written, no seat is dispatched. Post-dispatch limb: `C5_HARNESS_PINNED` fails in both seats after two attempts each (the live site-packages `MANIFEST_SHA256` differs from the dispatch record's pin on every attempt). | §5 C4/C5 → §4.4 ("a control among C0 through C5b fails **in every seat that attempted it** after two attempts; a packet or seat-isolation failure before dispatch files this class") → precedence: FIRST in the §4 order → filed over any other condition. Boundary honoured: "A C6 audit failure or a seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class." | YES |
| `CENSUS_CONTROL_SPLIT` | C1B `JOIN`: seat A's LIMB-A seal chain verifies on both attempts (`JOIN=PASS`); seat B's chain shows a seal mismatch on batch b7 and fails again on its second attempt. | §5 C1B ("a surviving fail/pass split files `CENSUS_CONTROL_SPLIT`") → §4.8 ("a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; **do not adopt the passing seat's result.**") → precedence: second; fires only where no all-seat control failure holds. | YES |
| `CENSUS_DENOMINATOR_DISPUTED` | Enumeration limb: seat A includes candidate passage p (a numeral it reads as the paper's own result); seat B excludes the same p as `ATTRIBUTED_NOT_DERIVED`; the disagreement survives two reconciliation attempts. Input-list limb: both seats agree on every candidate, but seat A lists inputs {H₀, Ω_m} for agreed claim c while seat B lists {H₀}; `merge` exits 1; the one reconciliation against the paper's stated equation does not resolve the difference. | §1 ("disagreement on any candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4)"); C3 merge clause ("an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations") → §4.5 ("The census does not proceed; the disputed candidates or inputs are listed."). | YES |
| `CENSUS_OUTCOME_DISPUTED` | Agreed included claim "13.8 Gyr". Seat A's attempt reproduces 13.797 and files `REPRO_WITHIN_STATED_PRECISION` (rounds to 13.8 at the printed precision). Seat B, reading the recipe as naming a different stated input set, reproduces 13.72 and files `REPRO_FAILED`. The one reconciliation is "against the printed numeral and the stated-precision rule of §3" only; it cannot settle which inputs the recipe names, so the disagreement survives. | §2 step 5 ("a disagreement surviving that reconciliation files `CENSUS_OUTCOME_DISPUTED` (§4)") → §4.6 ("The census does not proceed; the claim is listed with both seats' outcomes, both number pairs, and the step each seat reached."). | YES |
| `CENSUS_ORIGIN_DISPUTED` | Corpus of 20 included claims; on the key inputs of 3 of them (15% > 10%) the seats' independent origin classifications disagree — e.g., the sentence "we take β = 1/929.25": seat A files `CHOSEN` (`ORIG_CHOICE_STATED`), seat B files `DERIVED` (`ORIG_EQUATION`, citing a derivation line). Disagreements are reported, never reconciled. | C3 ("Every input's `origin` is classified independently by both seats") → §4.7 ("disagree on inputs affecting **more than 10% of included claims**. The census does not proceed; every disputed input is listed with both seats' classification and both quotations.") + C6's origin-dispute passage ("Above 10% of included claims, `CENSUS_ORIGIN_DISPUTED`."). | YES |
| `CENSUS_AUDIT_FAILED` | Reachable through every declared C6 path — each exhibited individually in section C.1 below — and through §7's receipt route. Summary input: with all controls passed identically in both seats and no enumeration/outcome/origin dispute, the audit does not run to PASS (omission; dispute rate above 10%; zero denominator with any passage on either side; missing seed; `MISMATCH` on a record, dependency edge, root origin or outcome; or a seal-receipt failure). | §4.3 ("the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the cause named), **or the receipt verification of the seal fails**. No tally is filed; report which.") → precedence: sixth; in the exhibited inputs no earlier stop class holds. | YES |
| `CENSUS_PARTIAL` | Primary: a corpus whose every claim lands in the arithmetic group EXCEPT one claim with an `ABSENT` input (files `REPRO_INPUT_ABSENT`); denominator ≥ 1; the audit runs to PASS (so `CENSUS_AUDIT_FAILED` does not fire). Zero-denominator limb: an enumeration with no candidate passages on either side (a corpus with no numeral passages at all) → denominator zero; C6's "A sealed denominator of zero with any passage on either side fails" does not fire; the audit passes; the empty enumeration is named. | §4.2 ("at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`), or the denominator is zero … **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.**") + §4.1's zero-denominator clause ("A denominator of zero files `CENSUS_PARTIAL` with the empty enumeration named") → precedence: seventh; no earlier class holds in the exhibited inputs. Routing note: a zero denominator WITH any passage on either side fails the audit and routes to `CENSUS_AUDIT_FAILED`, which precedes `CENSUS_PARTIAL` — so the zero-denominator limb of `CENSUS_PARTIAL` is reachable only through the empty-enumeration input exhibited. | YES |
| `CENSUS_COMPLETE` | A corpus (minimal case: one paper) in which every included claim states its recipe and prints every input value (or prints closed-list constants verbatim), so every claim files `REPRO_WITHIN_STATED_PRECISION` or `REPRO_FAILED`; denominator ≥ 1; both seats' enumerations, outcomes and origins agree; the audit runs to PASS. | §2 → §3 (every claim in the arithmetic group) → C6 PASS → §4.1 ("every included claim carries exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`") → precedence: no stop class holds; `CENSUS_PARTIAL`'s condition (a non-arithmetic outcome, or a zero denominator) is false → the last class in the order is filed. Direct answer to the reachability suspicion in section D below. | YES |

---

## C. V27-named conditions

### C.1 `CENSUS_AUDIT_FAILED` — each C6 path exhibited

Common preconditions for paths 1–3, 5, 6 (so no earlier §4 class fires): all C0–C5b controls pass
identically in both seats; the two census seats' enumerations, per-claim outcomes and origin
classifications agree; the tally is sealed and receipted. The auditor is the third independent seat, on a
different engine, with its own complete independent enumeration of all 89 enumerable texts and no seat
ledger in its dispatch inventory.

| # | C6 path | concrete input | clause path | reachable |
|---|---|---|---|---|
| 1 | sealed-included absent from the auditor | The sealed ledgers include passage p = (file, line, numeral) as an included claim; the auditor's independent enumeration of the same pinned texts omits p entirely. | C6: "**Omissions:** a sealed INCLUDED passage absent from the auditor's enumeration … each is ledger incompleteness and files `CENSUS_AUDIT_FAILED`"; the completeness row is `OMISSION`; PASS requires "no row is an omission". | YES |
| 2 | auditor-listed absent from the sealed ledgers | The auditor lists passage q (included or excluded) that the sealed candidate and exclusion ledgers omit. | Same clause, second limb: "a passage the auditor lists (included OR excluded) that the sealed ledgers omit — each is ledger incompleteness and files `CENSUS_AUDIT_FAILED`". | YES |
| 3 | dispute rate above 10% | Sealed denominator 40; the auditor and the sealed ledgers both list 5 passages but dispose them differently (`AUDIT_INCLUSION_DISPUTED` rows: "a passage both sides list but dispose differently, and a sealed EXCLUDED passage absent from the auditor's enumeration"); 5/40 = 12.5% > 10%. | C6: "above 10% of the sealed included denominator the audit files `CENSUS_AUDIT_FAILED`; at or below it the count is reported"; PASS requires "the dispute rate is at or below 10%". | YES |
| 4 | seedless selection | After receipt T, the external custodian does not supply the 64-lowercase-hex seed. | C6: "**If the seed is not supplied and recorded with the receipt, the audit does not run, `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named.**" (Exhibited with an all-arithmetic, nonzero-denominator tally so no other class's condition holds.) | YES |
| 5 | zero denominator | The sealed denominator is zero AND at least one passage appears on either side — e.g., both sides enumerate one passage and both exclude it as `EQUATION_NUMBER` (a `MATCH` row, no omission). | C6: "**A sealed denominator of zero with any passage on either side fails.**" → the audit does not run to PASS → §4.3: "does not run to PASS for any cause (the cause named)" → `CENSUS_AUDIT_FAILED`, which precedes `CENSUS_PARTIAL` in §4's order. | YES |
| 6 | reconstructed dependency edge differs from the sealed ledger | The auditor's sealed rederivation reconstructs input X's dependency closure as `derived_from [Y, Z]`; the sealed ledger carries X `derived_from [Y]`. | C6: "a missing input, a differing dependency edge or an unsupported record is `MISMATCH`"; PASS requires "no audited claim or origin is `MISMATCH`" → fail → §4.3. | YES |

Two further declared routes to the same class, exhibited for completeness:

- **§4.3 first limb (outcome not reproduced):** the auditor's own reproduction of a sampled
  arithmetic-group claim yields a value differing from the sealed `reproduced_value` → "Any outcome the
  audit cannot reproduce, or any ledger incompleteness, files `CENSUS_AUDIT_FAILED`." Reachable: YES.
- **§7 receipt route:** receipt P or T is missing, or Blanc's independent re-hash of the tally or the
  protocol mismatches a receipted value → "Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED`
  (§4, whose definition now names this case)". Reachable: YES.

### C.2 Seat-tally stops — `C1B_BATCH_COVERAGE=FAIL`, `JOIN=FAIL`, `C5C_NO_FALLBACK=FAIL` — with their §4 filings

| control | concrete stop input | stopping clause (quoted) | §4 filing(s) |
|---|---|---|---|
| `C1B_BATCH_COVERAGE=FAIL` | Manifest text #37 is owned by both batch b5 and batch b6 (alternatively: an owned text's bytes fail verification against its manifest row; or batch report b7 prints no `ACCESS_SHA`). | C1B: "`C1B_BATCH_COVERAGE=PASS` iff every manifest text is owned by exactly one batch, every owned text's bytes verify against its manifest row, and every batch report prints the packet's `ACCESS_SHA` … Either FAIL stops the seat's tally." | "a FAIL in every seat that tries it, after two tries, files `R3C2_NO_CLASS`; a surviving fail/pass split files `CENSUS_CONTROL_SPLIT`; an unreached check is `NOT_RUN`." (C1B, verbatim) |
| `JOIN=FAIL` | LIMB-A chain: batch b4's recorded predecessor digest ≠ batch b3's seal (alternatively: a candidate id owned by a different batch; an evidence source outside the manifest; a duplicate identifier; a `derived_from` cycle in the joined ledger). | C1B: "`JOIN=PASS` iff every seal matches, the ordered predecessor chain is intact from a root with no predecessor, every candidate and ledger claim is owned by its batch, every evidence source is a manifest text, identifiers are unique and every `derived_from` resolves acyclically. Either FAIL stops the seat's tally." | Same C1B clause: all-seat FAIL after two tries → `R3C2_NO_CLASS` (§4.4); surviving split → `CENSUS_CONTROL_SPLIT` (§4.8). |
| `C5C_NO_FALLBACK=FAIL` | One session's printed, session-identified provider log is missing (alternatively: the log shows a fallback entry). | §9: "the no-fallback control `C5C_NO_FALLBACK=PASS|FAIL|NOT_RUN` requires a printed, session-identified provider log for every session — a missing log or any fallback entry is FAIL, an unreached check NOT_RUN — a pre-tally control under the `R3C2_NO_CLASS` and `CENSUS_CONTROL_SPLIT` rules, checked by the lane owner". | `R3C2_NO_CLASS` (all-seat, after two attempts) or `CENSUS_CONTROL_SPLIT` (split), per §4.4/§4.8. |

Reachable: all three YES.

### C.3 A claim with `rests_on` `NOT_COMPUTED`

Concrete input: the included claim of row A.5 — it files `REPRO_NO_DERIVATION_STATED`, so there is no
equation, no inputs and no ledger records; more generally any included candidate without a record, an
empty ledger being valid.
Clause path: §2 step 5 design note ("an empty ledger is valid and every included candidate without a
record carries `rests_on` `NOT_COMPUTED`"); §3 ("a claim with no ledger record carries `rests_on`
`NOT_COMPUTED`, and the `rests_on` tally reports a `NOT_COMPUTED` row"); §9 lane tool ("emits `rests_on`
`NOT_COMPUTED` for every included candidate with no ledger record … and fails unless its rows equal the
included denominator").
Reachable: YES.

### C.4 A dependent claim `DISPUTED` through another claim's input

Concrete input: claim A's input record X carries a seat origin split (seat A: `CHOSEN`; seat B:
`DERIVED` → `ORIGIN_DISPUTED`) or a `PARENTS_DISPUTED` pair; claim B's record Y lists
`derived_from [X]` — a cross-claim dependency edge.
Clause path: §2 step 5 design note ("a claim whose dependency graph reaches a disputed record — in any
claim — is itself `DISPUTED` with both values"); §9 ("propagates a dispute through the whole dependency
graph across claims"); §3 master note ("A claim with a disputed root carries the pair computed under both
classifications and is marked `DISPUTED`"); C6 ("the `rests_on` tally reports a `DISPUTED` row").
Reachable: YES.

### C.5 A claim with `rests_on` `DERIVED_STANDARD_OR_MEASURED_ONLY`

Concrete input: a claim whose inputs are (i) a closed-list constant the paper prints verbatim — c =
2.99792458e8 m s⁻¹, `STANDARD`/`ORIG_CONSTANT`, the exact string in C3's value column — and (ii) the
paper's own reported measurement with the measurement described — "from our spectra we measure z =
0.62", `MEASURED`/`ORIG_MEASURED`; any `DERIVED` records' `derived_from` chains terminate only in such
leaves.
Clause path: C3 classification (validate asserts the closed-list membership and the quotation checks) →
lane `compute` per the §3 master note: "`DERIVED_STANDARD_OR_MEASURED_ONLY` … when every root origin is
`DERIVED`, `STANDARD` or `MEASURED`; otherwise the most severe root origin present, in the fixed order
`USES_UNDECLARED` > `USES_IMPORTED` > `USES_FITTED` > `USES_CHOSEN`" → roots ⊆ {`STANDARD`, `MEASURED`}
→ `rests_on` = `DERIVED_STANDARD_OR_MEASURED_ONLY`.
Reachable: YES. (Membership identical to the former `DERIVED_ONLY` label; the rename is label-only —
§10.22, history.)

### C.6 Observation on the label parenthetical (text as it stands; no judgement)

§3's master-only note reads "the token `DERIVED_STANDARD_OR_MEASURED_ONLY` of V10–V26, identical
membership" — the V27 rename swept the historical token name inside its own parenthetical (the V10–V26
token was `DERIVED_ONLY`). Recorded because this exhibition reads the text literally; it changes no
membership, no routing and no reachability.

---

## D. The `CENSUS_COMPLETE` suspicion — direct answer

**REACHABLE.**

The suspicion: `CENSUS_COMPLETE` requires every included claim to carry an outcome from the arithmetic
group; in a real corpus of many papers, a single blocked, absent-input, or no-derivation-stated claim
anywhere forces `CENSUS_PARTIAL` — so is `CENSUS_COMPLETE` unreachable in practice?

Routing, shown: §4.1's condition is a condition on the input corpus, not a clause that fails on every
input. The exhibiting input: a corpus in which every paper states its recipe and prints every input value
(or prints closed-list constants verbatim); every claim then files `REPRO_WITHIN_STATED_PRECISION` or
`REPRO_FAILED` — and note `REPRO_FAILED` is arithmetic-group ("The arithmetic group is … exactly
`REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`"), so even a paper whose arithmetic does not
reproduce does not block `CENSUS_COMPLETE`; the denominator is ≥ 1; the audit runs to PASS. Then no
earlier class in §4's precedence holds, and `CENSUS_PARTIAL`'s condition ("at least one included claim
carries a non-arithmetic outcome …, or the denominator is zero") is false, so the filed class is
`CENSUS_COMPLETE`.

What is true in the suspicion: one `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`,
`REPRO_NO_DERIVATION_STATED` or `REPRO_NOT_EVALUABLE` claim anywhere in the corpus — or a zero
denominator — routes the study to `CENSUS_PARTIAL` (§4.2, which "takes precedence over
`CENSUS_COMPLETE`" and precedes it in §4's order). The document itself flags exactly this fragility in
C0's own rationale: "`CENSUS_COMPLETE` requires every included claim to carry an arithmetic-group
outcome, which a single blocked or absent input in the whole corpus is enough to prevent." So:
**reachable in principle** — there exist inputs that file it — **and fragile in practice** — its blocking
condition is a single non-arithmetic claim anywhere in the corpus. Reachability is the C0 question; the
answer is REACHABLE. Whether a real corpus will file it is an empirical property of the corpus, not an
unreachability of the class.

---

## E. UNREACHABLE verdicts and blocking clauses

**None.** Every per-claim outcome of §3 (6 of 6) and every study-level class of §4 (8 of 8) is exhibited
above with a concrete input and a clause path, as is every V27-named condition (all six C6 paths to
`CENSUS_AUDIT_FAILED` plus the two further declared routes; the three seat-tally stops with their §4
filings; `rests_on` `NOT_COMPUTED`; cross-claim `DISPUTED`; `rests_on`
`DERIVED_STANDARD_OR_MEASURED_ONLY`). No verdict was found for which the text licenses no input, so
there is no blocking clause to quote.

The only unreachability in this document's history was `REPRO_AFTER_CHOICE` under the retired
derivation-only wording — filed `UNREACHABLE` by both V9 C0 seats, who agreed exactly (§10.3, history,
binding nothing) — and retired at V10 by the option-(c) ruling. It is not a declared outcome of the text
as it stands and was therefore not exhibited.

`C0_REACHABILITY=PASS` — restated: all required rows are exhibited; nothing is `UNREACHABLE`.

Completion tokens: the step order names this report's final line as `R3C2_C0_V27_KIMI_COMPLETE` and the
output spec names the final line as `R3C2_C0_EXHIBITION_COMPLETE`; both are printed below, the
step-order token last.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V27_KIMI_COMPLETE

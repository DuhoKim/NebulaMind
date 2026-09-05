ACCESS_SHA=22355a08b2d9cb98163427f5d2647181e48912f794852ac498e4e5e9ff23f11f
C0_REACHABILITY=PASS

# R3-C2 V13 — C0 reachability exhibition (author seat: kimi, 2026-09-05)

Scope: exhibition only. This document does not gate the preregistration and does not judge its physics. It asks one
question for every per-claim outcome of §3 and every study-level class of §4 of
`R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` (V13, sha256 above): **can this verdict occur — is there a concrete
input and a clause path that produces it?** Only that file was read.

Textual basis, stated before the table:

- §3 declares exactly six per-claim outcomes: `REPRO_EXACT`, `REPRO_FAILED`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`,
  `REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`. (`REPRO_AFTER_CHOICE` is not a declared outcome in V13 — it
  was "RETIRED at V10 by the principal's ruling adopting option (c)" into the script-computed `rests_on` field, so
  no row is owed for it. The ruling is recorded in §10.4; there is no held clause.)
- §3's arithmetic group is "exactly `REPRO_EXACT` and `REPRO_FAILED`" (quoted verbatim below).
- §4 declares exactly seven study-level classes: `CENSUS_COMPLETE`, `CENSUS_PARTIAL`, `CENSUS_AUDIT_FAILED`,
  `R3C2_NO_CLASS`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_CONTROL_SPLIT`, with a total
  filing precedence quoted verbatim below.
- The core definition is treated exactly as V13 prints it — option (c), one pass, two tallies. Where a row's
  reachability rides on that settled wording (chosen/fitted `PRINTED` values are consumed, not filtered), the
  dependence is stated in the row rather than assumed away.

## (A) Per-claim outcomes of §3 — six rows, all exhibited

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `REPRO_EXACT` | Claim C-EX1 in a pinned enumerable text prints "the Hubble flow at 100 Mpc is v = 6736 km s⁻¹" as its own result, via the stated recipe `v = H₀·d`, with `d = 100 Mpc` printed in the same paragraph (origin `MEASURED`, cited) and `H₀` consumed at the C3 closed-list value `67.36` (status `STANDARD`). Mechanical evaluation: 67.36 × 100 = 6736 — matches the printed numeral at its printed precision. | §1 inclusion (printed numeral asserted as the paper's own result) → §2 steps 1–3 (extract; list inputs; classify `PRINTED`/`STANDARD` against C3's closed list) → §2 step 4 ("Attempt the arithmetic MECHANICALLY — follow the paper's own recipe, using every value it directs you to use, i.e. every ledger record with status `PRINTED` or `STANDARD`") → §3 `REPRO_EXACT` ("the paper's number follows, within its own stated precision ... Report both numbers"). No earlier terminal condition in the §3 precedence holds, so the arithmetic group is reached. `rests_on` is computed by the pinned script beside it (here `DERIVED_ONLY`). | YES |
| `REPRO_FAILED` | Claim C-FL1 prints "v = 6800 km s⁻¹" for the same stated recipe `v = H₀·d` with the same two stated inputs (d = 100 Mpc `PRINTED`; H₀ = 67.36 `STANDARD`). Mechanical evaluation gives 6736; 6800 ≠ 6736 at the printed precision. The inputs the paper states are sufficient for its recipe. | §1 → §2 steps 1–4 as above → §3 `REPRO_FAILED` ("the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the paper's number ... Wording: 'unreproduced from the stated inputs,' not 'error.'"). No earlier precedence limb holds. `rests_on` computed beside it. | YES |
| `REPRO_BLOCKED` | Claim C-BL1's stated equation needs a cluster mass `M`. The paper does not print `M` but writes "we use the mass of Ref. [23], table 2". Ref. [23] is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`. (Second route: Ref. [23] IS pinned and enumerable, but no value at its cited line machine-matches; or the named source is listed RAW.) | §2 step 3 → the §2 named-source clause, verbatim: "**only when such a match exists; a cited value that does not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest, files `REPRO_BLOCKED` under §3**" → §3 `REPRO_BLOCKED` ("an input whose value the claiming paper does not print, and for which the claiming paper names a source (a citation) that is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`"). Precedence: an equation IS stated, so `REPRO_NO_DERIVATION_STATED` does not hold; `REPRO_BLOCKED` stands before `REPRO_INPUT_ABSENT` in the §3 order and is filed. Name the input and the source. | YES |
| `REPRO_NOT_EVALUABLE` | Claim C-NE1 prints a number asserted as its own result and states a recipe requiring a symbolic integral with no closed form; the seat's sympy attempt exceeds the 120-second cap mid-simplification. | §1 → §2 steps 1–4 (attempt begins; all inputs stated, no blocked/absent input, so no earlier precedence limb holds) → §9 ("120-second cap on symbolic operations with `SYMBOLIC_TIMEOUT` as a reportable outcome") → §3 `REPRO_NOT_EVALUABLE` ("the arithmetic could not be completed within the 120-second cap, or requires machinery this lane does not have. Print `SYMBOLIC_TIMEOUT` and the point reached."). | YES |
| `REPRO_NO_DERIVATION_STATED` | Claim C-ND1 is a passage printing "we obtain χ = 0.081" asserted as the paper's own result; the paper states no equation and no computational procedure anywhere that could produce it. | §1 inclusion is satisfied (a printed numeral the paper asserts as a result of its own — §3's parenthetical: "A claim can satisfy §1 ... while the paper never says how it was obtained") → §2 step 1 finds no equation to extract → §3 `REPRO_NO_DERIVATION_STATED` ("the paper prints the claim as its own result but states no equation or computational procedure that could produce it, so there is nothing to attempt. Name the passage."). First in the §3 precedence, so every co-occurring condition yields to it. | YES |
| `REPRO_INPUT_ABSENT` | Claim C-IA1 prints its result via the stated recipe `M = v²·r/G`; `v` is `PRINTED`, `G` is `STANDARD` on C3's list, and `r` is neither printed anywhere in the paper nor traced to any named source. | §2 step 3 classifies `r` as `ABSENT` → §2: "**A seat may not supply a value for an `ABSENT` input.** Encountering one ends that claim's attempt." → §3 `REPRO_INPUT_ABSENT` ("an input the equation needs is `ABSENT` from the paper — neither printed nor traced to any named source — so the attempt stops there. Name the input."). Precedence: an equation is stated (limb 1 out); no source is named, so `REPRO_BLOCKED` (limb 2) does not hold; limb 3 files. | YES |

## (B) Study-level classes of §4 — seven rows, all exhibited

| verdict | concrete input | clause path | reachable |
|---|---|---|---|
| `R3C2_NO_CLASS` | Control C5 (harness): `python3 -c "import sympy"` fails in seat A's environment on two attempts and in seat B's environment on two attempts — the control fails in every seat that attempted it. | §5 (each control runs per seat) → §4.4 ("`R3C2_NO_CLASS` — a control fails in every seat that attempted it after two attempts"). First in the §4 filing precedence, so it is filed over any other condition that also holds; later limbs are `NOT_RUN`. | YES |
| `CENSUS_CONTROL_SPLIT` | Control C2 (input ledger): `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .` exits 0 for seat A's ledger and exits non-zero for seat B's ledger, on two attempts each. | §5 → §4.7 ("`CENSUS_CONTROL_SPLIT` — a control fails in one seat and passes in another after two attempts. Report both seats' outputs and stop; do not adopt the passing seat's result."). Second in precedence; filed whenever limb 1 does not hold. | YES |
| `CENSUS_DENOMINATOR_DISPUTED` | Candidate passage P prints a numeral beside "see [12]". Seat A includes P under §1 (reads the paper as asserting the value as its own); seat B excludes P as `ATTRIBUTED_NOT_DERIVED`. Two reconciliation attempts fail to agree. | §1 ("Inclusion is assigned independently by the two independent seats from the §1 rule alone; disagreement on any candidate stops the study under `CENSUS_DENOMINATOR_DISPUTED`") → §6 Limb A (tolerance zero, measured in candidate passages) → §4.5 ("the two enumerations disagree after two reconciliation attempts. The census does not proceed; the disputed candidates are listed."). Third in precedence. | YES |
| `CENSUS_ORIGIN_DISPUTED` | Ten included claims. For inputs in two of them (20% > 10%) the seats' independent classifications disagree — e.g. for "we adopt H₀ = 67.4 from Planck (2018)" seat A files `ORIG_CITATION`→`IMPORTED` and seat B files `ORIG_CHOICE_STATED`→`CHOSEN`, each with its verbatim quotation. | C3 ("Every input's `origin` is classified independently by both seats"; the merge adds `origin_alt`/`origin_evidence_alt`) → C6 ("An input on which the two classifications disagree is filed `ORIGIN_DISPUTED` ... it is not reconciled. Above 10% of included claims, `CENSUS_ORIGIN_DISPUTED`.") → §4.6. Fourth in precedence. | YES |
| `CENSUS_AUDIT_FAILED` | Route (i): the C6 third seat re-derives a sampled arithmetic-group claim and obtains a different outcome than the sealed ledger files, or finds the candidate/exclusion ledger incomplete against a pinned source. Route (ii): after opening, Blanc's re-hash of the tally or the protocol mismatches a receipted value, or receipt P or T is missing. | Route (i): C6 ("Any outcome the audit cannot reproduce, or any ledger incompleteness, files `CENSUS_AUDIT_FAILED`.") → §4.3. Route (ii): §7 ("Any missing receipt or mismatch files `CENSUS_AUDIT_FAILED` (§4, whose definition now names this case)") → §4.3 ("the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or the receipt verification of the seal fails. No tally is filed; report which."). Fifth in precedence. | YES |
| `CENSUS_PARTIAL` | A corpus of included claims in which exactly one claim is C-BL1 above (`REPRO_BLOCKED` — cited source outside the manifest) and every other claim files an arithmetic-group outcome; all controls pass in both seats, the enumerations agree, origin disputes affect ≤10%, and the audit and receipts are clean. | §3 files the non-arithmetic outcome → §4.2 ("at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`). Report each and why. INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`."). Sixth in precedence — filed whenever no stop class holds and at least one non-arithmetic outcome exists. | YES |
| `CENSUS_COMPLETE` | A corpus of N included claims, every one like C-EX1 or C-FL1: each states a recipe, every input is `PRINTED` in the paper or `STANDARD` on C3's closed list, and every attempt completes within the cap. All controls pass in both seats within two attempts; the two enumerations agree within two reconciliations; origin disputes affect ≤10% of claims; the C6 audit reproduces every arithmetic-group claim and the sampled remainder; receipts P and T both verify. | §3 files exactly one arithmetic-group outcome per claim → §4.1 ("`CENSUS_COMPLETE` — every included claim carries exactly one outcome from the arithmetic group of §3. Report the full tally with its denominator, and the `rests_on` tally beside it — two tallies from one pass."). The §4 precedence is then walked in order: no control failure or split; no denominator dispute; no origin dispute above 10%; audit and receipts clean; no non-arithmetic outcome, so `CENSUS_PARTIAL`'s condition does not hold — and `CENSUS_COMPLETE`, last in the order, is the class that remains and is filed. | YES |

## (C) Reachability, verdict by verdict

All six per-claim outcomes of §3: REACHABLE.
All seven study-level classes of §4: REACHABLE.
UNREACHABLE verdicts: none.

## The named suspicion — `CENSUS_COMPLETE` — answered directly

**REACHABLE.**

The suspicion: `CENSUS_COMPLETE` requires every included claim to carry an arithmetic-group outcome, so in a real
corpus a single blocked, absent-input, or no-derivation-stated claim anywhere forces `CENSUS_PARTIAL` — making
`CENSUS_COMPLETE` unreachable in practice.

What the text actually does with that:

1. The forcing half of the suspicion is true and is in the document. §4.2 is verbatim: "**at least one included
   claim carries a non-arithmetic outcome** ... **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.**"
   One `REPRO_BLOCKED`, one `REPRO_INPUT_ABSENT`, one `REPRO_NO_DERIVATION_STATED`, or one `REPRO_NOT_EVALUABLE`
   anywhere in the corpus is sufficient to defeat `CENSUS_COMPLETE`. The class is fragile by construction.
2. But fragility is not unreachability. No clause requires any non-arithmetic outcome to exist. Nothing in §4.1,
   §3, or §2 sets a minimum corpus size, a minimum failure count, or any condition that a self-contained corpus
   cannot satisfy. The arithmetic group itself — quoted verbatim from §3: "**The arithmetic group** is the set of
   outcomes that state whether the arithmetic reproduced the number: **exactly `REPRO_EXACT` and `REPRO_FAILED`**"
   — places no provenance condition on membership: under the settled option-(c) wording, §2 step 4 consumes "every
   ledger record with status `PRINTED` or `STANDARD`, chosen and fitted values included", so even a claim resting
   on a chosen constant files an arithmetic outcome (with its `rests_on` beside it). The only claims that escape
   the arithmetic group are the four named terminal conditions, and each is a property of the particular claim,
   not a necessity of the corpus.
3. The routing of the exhibited input (row 7 of the §4 table): every included claim files `REPRO_EXACT` or
   `REPRO_FAILED`; the §4 precedence — quoted verbatim: "**Exactly one study-level outcome is filed. Where more
   than one condition holds, file the first in this order:** `R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`,
   `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`, `CENSUS_PARTIAL`,
   `CENSUS_COMPLETE`. **Once a stop class applies, later limbs are unreached and their controls are `NOT_RUN`.**"
   — is walked in order; no earlier limb's condition holds; `CENSUS_COMPLETE` is filed. Its position as last in
   the precedence is not a block; it is exactly the position a totality class must occupy.

So: `CENSUS_COMPLETE` is reachable — there exists an input (the fully self-contained corpus exhibited above) that
produces it. Whether it WILL be filed is a property of the actual corpus, not of this document, and the document
says so itself: a single non-arithmetic claim flips the filing to `CENSUS_PARTIAL`. C0 asks only whether the
outcome can occur. It can.

## Declared-condition precedence — exercised, not just exhibited singly

- §3 co-occurrence: an input not printed whose named source is outside the manifest satisfies both the
  `REPRO_BLOCKED` and `REPRO_INPUT_ABSENT` descriptions; the §3 order files `REPRO_BLOCKED` (BLOCKED precedes
  INPUT_ABSENT) — the exact case the precedence's own parenthetical names. A claim with no stated derivation and
  a blocked input files `REPRO_NO_DERIVATION_STATED` (first in the order). Both routings exist in the text.
- §4 co-occurrence: a corpus with a control split AND a denominator dispute files `R3C2_NO_CLASS` only if every
  seat failed the control, else `CENSUS_CONTROL_SPLIT` — the order is total, so exactly one class is filed in
  every exhibited combination. A tally that would satisfy both `CENSUS_PARTIAL` and `CENSUS_COMPLETE` files
  `CENSUS_PARTIAL` (sixth before seventh).

## UNREACHABLE verdicts and their blocking clauses

None. Every declared per-claim outcome of §3 and every declared study-level class of §4 has a row above with a
concrete input and a clause path through the document as it stands at V13.

Dependence recorded, per the version note: this exhibition is against the settled option-(c) text. The
`REPRO_EXACT`/`REPRO_FAILED` rows ride on §2 step 4's "chosen and fitted values included" — under the retired
derivation-only wording those claims would have routed differently, and §10.3 records that the two prior blind
seats found exactly one unreachable class under that wording (`REPRO_AFTER_CHOICE`, since retired by the ruling,
not by repair). No held clause remains in V13; nothing in this exhibition assumed a reading the text does not
print.

R3C2_C0_EXHIBITION_COMPLETE
R3C2_C0_V13_KIMI_COMPLETE

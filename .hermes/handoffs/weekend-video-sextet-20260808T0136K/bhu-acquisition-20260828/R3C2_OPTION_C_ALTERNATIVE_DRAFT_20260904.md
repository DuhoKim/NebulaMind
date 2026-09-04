# ALTERNATIVE DRAFT — NOT ADOPTED — option (c): one pass, two tallies

**Tori, 2026-09-04 21:58 KST.** Prepared under Blanc's 21:53 instruction: *"You may PREPARE the (c)-shaped text as a
clearly-labelled alternative draft so it is ready the moment he rules. Do not adopt it."*

**This is not the live preregistration.** The live document is `R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` (V5),
whose §3 still carries option **(b)**, derivation-only, and which is **not** to be repaired further until Duho rules.
This file changes nothing and governs nothing.

## The problem it solves

Round four over-corrected. Refusing every chosen or fitted input stopped the census being **reproduction** at all,
because **a paper can direct you to use its own chosen constant, and following that instruction is reproducing the
paper.** Under (b), entry 59's inflation numbers are `REPRO_AFTER_CHOICE` because `β` was chosen — which is true and
useful — but so would be any paper that honestly states a fitted parameter and then computes correctly from it. The
census would stop distinguishing *arithmetic that works* from *arithmetic resting on a free parameter*, and those are
different facts about a paper.

## The (c) design in one paragraph

**Run the reproduction mechanically — follow the paper's own recipe, using every value it tells you to use, chosen
constants included — and record each input's provenance in the ledger alongside.** The reproduction verdict then
answers *"does the paper's arithmetic work?"*. The ledger separately answers *"what did it rest on?"*. **Two tallies
from one pass, neither contaminating the other.**

## What changes from the live V5

| clause | V5 (option b) | option (c) |
|---|---|---|
| admissible inputs | `origin ∈ {DERIVED, STANDARD}` only | **every value the paper directs you to use**, chosen ones included |
| `REPRO_EXACT` | number follows from admissible inputs | **number follows from the paper's own recipe** |
| `REPRO_AFTER_CHOICE` | fires whenever a chosen value is used | **deleted** — provenance is recorded, not a verdict |
| the ledger | supporting evidence | **the second tally, and the load-bearing one** |
| new per-claim field | — | `rests_on: DERIVED_ONLY \| USES_CHOSEN \| USES_FITTED \| USES_IMPORTED \| USES_UNDECLARED` |
| interpretation | reads the reproduction verdict | **reads the `rests_on` field**, never the verdict |

Per-claim outcomes become: `REPRO_EXACT`, `REPRO_FAILED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`,
`REPRO_NOT_EVALUABLE` — five, with `REPRO_AFTER_CHOICE` retired into the `rests_on` field. Every study-level class,
control, seal and blinding provision of V5 carries over unchanged.

## Why this is the option I would also pick

- It **restores reproduction as reproduction**, which is the external, pattern-independent criterion the whole
  redesign was built to get.
- It **keeps the provenance information** that makes the census worth running — nothing is lost, it moves from the
  verdict to a field.
- It **puts more distance between the hypothesis and the evidence**, not less: the interpretation step reads a
  factual ledger field rather than an outcome whose definition the lane tuned.
- It makes the two facts separable in the result: *the arithmetic works* and *it rests on a chosen constant* can both
  be true of one claim, and under (b) they collapse into one label.

## What it does not fix

It does not settle whether the census is worth ~3–4 seat-days after nine gate rounds; that is a separate judgement
and remains Duho's. And it inherits every unrepaired non-definitional finding, so it would need one clean gate of its
own before running — **it must not be treated as pre-gated by V5's rounds.**

R3C2_OPTION_C_ALTERNATIVE_DRAFT_COMPLETE — NOT ADOPTED

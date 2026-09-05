# R3-C2 seat packet — reproduction census: what to do

**You are one of two independent seats. Work only from this file, the seat brief, and the pinned
sources in this directory. Do not open any other path; print every path you open.**

This packet is the complete instruction set for your task, extracted mechanically by
`r3c2_build_seat_packet.py`. Apply the rules below exactly as written.

Built from master sha256 `065dc0e48090d7d56625e41e8f517a782640e2b97d5df08423fd38dc4c8e8ee0` by `r3c2_build_seat_packet.py`.

## 1. The question, exactly

For every quantitative claim in the corpus, **two questions from one pass: (i) does the paper's own number follow
from the paper's own recipe applied to the inputs it states — chosen constants included; and (ii) what does that
number rest on — derived, standard or measured inputs only, or a chosen, fitted, imported or undeclared one?** The first is the
reproduction verdict; the second is the ledger's `rests_on` field. **Neither contaminates the other.**

**Operational definition, so the enumeration is not a judgement:** a *quantitative claim* is a passage in a pinned
source that **prints a numeral the paper asserts as a result of its own** — with units, or dimensionless and stated
as a value. Excluded, by definition and not by taste: numerals that are equation numbers, reference numbers, page or
line numbers, dates, or values the paper attributes to another work without deriving. **Every candidate passage is
listed with file and line; inclusion and exclusion are both recorded.**
**Inclusion is assigned independently by the two independent seats from the §1 rule alone; disagreement on any
candidate stops the study under `CENSUS_DENOMINATOR_DISPUTED`, and the third seat audits the complete candidate and
exclusion ledgers against every pinned source.** 



## 2. Method — per claim, in order

**The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` (sha256 `300d4da144d96ae9f1390c9018e919ae1ba6cf00be9f45ad36fdccfdcfbf9b24`) lists every enumerable text by
digest and byte count; a seat enumerates claims from those files and no other. Files listed there as RAW are not enumerable
and are outside the census, visibly.** 

1. **Extract** the printed number, its units, and the equation the paper says produces it, with file and line.
2. **List the inputs** that equation needs.
3. **Classify each input** as `PRINTED` (given in the paper), `STANDARD` (a measured constant **on C3's closed
   list — that list, verbatim, and no other value**), or `ABSENT`. Record its `origin` with the evidence C3 requires.
4. **Attempt the arithmetic MECHANICALLY — follow the paper's own recipe, using every value it directs you to use,
   i.e. every ledger record with status `PRINTED` or `STANDARD`, chosen and fitted values included.** Provenance is
   **recorded** (C3's `origin`, `derived_from`, `root_origins`), never filtered on. *(A paper can direct you to use its own chosen constant, and following that instruction is reproducing the
   paper.)*
5. **Record the outcome**, per claim, as one of §3, **and let the script record the claim's `rests_on`** from the ledger.

**A value the paper does not print but traces to a named source that is itself a text in `R3C2_CORPUS_MANIFEST.md` is
classified `PRINTED` from that source, with `origin` `IMPORTED`, `origin_evidence` `ORIG_CITATION` cited to the named
source's file and line, and the value machine-matched there.** **A seat may not supply a value for an `ABSENT` input.**
Encountering one ends that claim's attempt.

## 3. Per-claim outcomes — declared now


**One pass, two tallies.** The reproduction verdict answers *"does the paper's
arithmetic work from what it states?"* The ledger answers *"what did it rest on?"* — a value can be printed in the
paper and still have been chosen or fitted, and under (c) both facts
survive: the arithmetic reproduces AND the ledger says what it rested on. So:

> **THE INPUTS THE ARITHMETIC MAY CONSUME** = every ledger record with status `PRINTED` (given in the paper, whatever
> its `origin`) or `STANDARD` (on C3's closed list). **PROVENANCE IS RECORDED, NOT FILTERED**: each record's `origin`
> is cited under C3, independently by both seats; `root_origins` and the per-claim summary field **`rests_on`** are
> computed from the ledger by the pinned script `r3c2_ledger_tools.py` (sha256 `f1e51c8c73c3a8058159d385ff033ac68b6bd218363bae243aff596029fe5554`), with the full
> root-origin set printed beside it. **No seat writes `root_origins` or `rests_on`; the script rejects a ledger that
> arrives with either set.**


- **`REPRO_EXACT`** — the paper's number follows, within its own stated precision, **from the paper's own recipe
  applied to the inputs it states** (`PRINTED` or `STANDARD`). **Report both numbers.** **Where the paper states no
  precision for the claim, the printed precision is the claim's stated precision: the reproduced value must round to
  the printed numeral at that precision.** The claim's `rests_on` is reported beside it. 

- **`REPRO_FAILED`** — the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the
  paper's number. Report both numbers. **Wording: "unreproduced from the stated inputs," not "error."** `rests_on`
  is reported beside it.
- **`REPRO_BLOCKED`** — an input whose value the paper does not print, but for which the paper **names a source (a
  citation)**, where that source is outside this lane and cannot be obtained. Name it. *(Distinct from
  `REPRO_INPUT_ABSENT`, which is an input the paper neither prints nor traces to any named source.)* 
- **`REPRO_NOT_EVALUABLE`** — the arithmetic could not be completed within the 120-second cap, or requires machinery
  this lane does not have. Print `SYMBOLIC_TIMEOUT` and the point reached. *(Added because the stall guard had no
  per-claim outcome to file into.)*
- **`REPRO_NO_DERIVATION_STATED`** — the paper prints the claim as its own result but **states no equation or
  computational procedure that could produce it**, so there is nothing to attempt. Name the passage. *(A claim can
  satisfy §1 — a printed numeral asserted as the paper's own result — while the paper never says how it was
  obtained. That claim previously fell through every class.)*
- **`REPRO_INPUT_ABSENT`** — an input the equation needs is `ABSENT` from the paper — **neither printed nor traced to
  any named source** — so the attempt stops there. **Name the input.**  Distinct from a claim whose inputs the paper DOES state, chosen or not — that
  claim is attempted and files `REPRO_EXACT` or `REPRO_FAILED` with its `rests_on`.
**Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the first in this
order:** `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the
**arithmetic group**. *(Precedence is stated because these conditions genuinely co-occur — an absent input whose
source is also unobtainable satisfied two classes with no rule to choose between them.)*

**The arithmetic group** is the set of outcomes that state whether the arithmetic reproduced the number: **exactly
`REPRO_EXACT` and `REPRO_FAILED`**.

**Candidate exclusions are not per-claim outcomes.** Every enumerated candidate passage that fails the §1
definition is recorded in a **separate exclusion ledger** with file, line, the numeral, and which excluded kind it
is (equation number, reference number, page/line number, date, or attributed-not-derived). **The exclusion ledger's
`kind` is one of `EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`, `ATTRIBUTED_NOT_DERIVED`.** The census denominator
is the count of **included** claims; the exclusion ledger is reported alongside it and audited under C6, so nothing
is hidden by being excluded. 

## 4. Study-level outcomes

1. **`CENSUS_COMPLETE`** — **every included claim carries exactly one outcome from the arithmetic group of §3.**
   Report the full tally with its denominator, **and the `rests_on` tally beside it — two tallies from one pass.**
2. **`CENSUS_PARTIAL`** — after two attempts, **at least one included claim carries a non-arithmetic outcome**
   (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`). Report each and
   why. **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.** *(Previously "some claims unresolved"
   was undefined, and a blocked claim satisfied both classes.)*
3. **`CENSUS_AUDIT_FAILED`** — the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, **or the §7
   receipt verification fails**. No tally is filed; report which.
4. **`R3C2_NO_CLASS`** — a control fails **in every seat that attempted it** after two attempts.
5. **`CENSUS_DENOMINATOR_DISPUTED`** — the two enumerations disagree after two reconciliation attempts. The census
   does not proceed; the disputed candidates are listed. *(Added because the enumeration stop had no class.)*
6. **`CENSUS_ORIGIN_DISPUTED`** — the two seats' independent `origin` classifications disagree on inputs affecting
   **more than 10% of included claims**. The census does not proceed; every disputed input is listed with both
   seats' classification and both quotations. 
7. **`CENSUS_CONTROL_SPLIT`** — a control fails in one seat and passes in another after two attempts. Report both
   seats' outputs and stop; **do not adopt the passing seat's result.** *(Added because this reachable state landed in
   no class.)* 

**Exactly one study-level outcome is filed. Where more than one condition holds, file the first in this order:**
`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`,
`CENSUS_PARTIAL`, `CENSUS_COMPLETE`. **Once a stop class applies, later limbs are unreached and their controls are
`NOT_RUN`.** 




## 5. Controls, each with an exact named code

- **C0 — reachability, run BEFORE the freeze.** For **every per-claim outcome of §3** and **every study-level class
  of §4** — and for **every declared condition** — **exhibit a concrete
  input that produces it**: a specific claim, its inputs, and the path it takes through this document to that
  verdict. **An outcome for which no such input can be exhibited is UNREACHABLE, and this preregistration does not
  freeze until it is.** The exhibition table is the artefact. **The exhibition is authored independently by one independent seat and independently verified by a second
  independent seat; both must return `C0_REACHABILITY=PASS`. The lane owner checks only that every declared outcome
  and condition has a row and does not judge reachability.** `C0_REACHABILITY=PASS|FAIL|NOT_RUN` — PASS only when every required row has been
  independently exhibited and verified; FAIL when any required row is absent or cannot produce its declared condition;
  NOT_RUN when C0 was not reached.

  

- **C1 — denominator.** Claims **included**, claims **excluded** (with the exclusion ledger of §3), and attempts made,
  all printed before any tally. 
  **The candidate and exclusion ledgers are JSON files validated by the pinned script:
  `/usr/bin/python3 r3c2_ledger_tools.py census <candidates.json> <exclusions.json>` — exit 0 only if every candidate
  carries exactly one disposition and the printed counts equal the recomputed counts; print its command, stdout and
  exit status.** `C1_DENOMINATOR_PRINTED=PASS|FAIL|NOT_RUN`, PASS only on exit 0.
- **C2 — input ledger.** Every input classified `PRINTED` / `STANDARD` / `ABSENT`, each `PRINTED` one carrying file and
  line, in the JSON schema of C3, validated by `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .` run from the printed seat working
  directory (`.` is the sole allowed `sources_dir`); before execution the seat prints the fully resolved command with
  every angle-bracket placeholder replaced by the actual in-scope path
  (exit 0 = PASS; every failure printed). `C2_INPUT_LEDGER=PASS|FAIL|NOT_RUN`.
- **C3 — no substitution, machine-checked.** The input ledger is a **JSON file**, one record per input:
  `{claim_id, input_id, symbol, status: PRINTED|STANDARD|ABSENT, origin: DERIVED|STANDARD|MEASURED|CHOSEN|FITTED|IMPORTED|UNDECLARED,
  origin_evidence: {reason_code, source_file, source_line, verbatim}, derived_from: [input_id…], root_origins: […],
  value, source_file, source_line}`. *(`STANDARD` was missing from the `origin` enumeration while §3 defined
  admissibility partly by it, so a measured-constant record could not be validly filled in.)*

  **`origin` must be cited, not asserted.** Every record carries `origin_evidence` with a reason code —
  `ORIG_EQUATION`→`DERIVED`, `ORIG_CONSTANT`→`STANDARD`, `ORIG_MEASURED`→`MEASURED` (a quantity the paper reports as
  its own measurement, with the measurement described), `ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_FIT_STATED`→`FITTED`,
  `ORIG_CITATION`→`IMPORTED`, `ORIG_SILENT`→`UNDECLARED` — and, except for `ORIG_SILENT`, a **verbatim quotation
  machine-matched to the cited line**. **Every input's `origin` is classified independently by both seats.** **Where
  more than one reason code matches the cited sentence, file the first in this order: `ORIG_CITATION`,
  `ORIG_FIT_STATED`, `ORIG_CHOICE_STATED`, `ORIG_MEASURED`, `ORIG_EQUATION`, `ORIG_CONSTANT`, `ORIG_SILENT` — a sentence
  that names an external source for the value is a citation whatever else it says.**  **`UNDECLARED` is the default, not the residue**: a record leaves it only by
  producing that text, and an `ORIG_SILENT` record prints the search the seat ran.

  **Provenance is transitive, and the transitivity is computed.** Every `DERIVED` record lists its `derived_from`
  ids; **a script computes `root_origins`, the origins at the leaves of that chain, and no seat writes that field.**
  A chain's root origins are computed from every step, never from its last step alone. **The script is `r3c2_ledger_tools.py`,
  committed beside this document, sha256 `f1e51c8c73c3a8058159d385ff033ac68b6bd218363bae243aff596029fe5554`; the seat runs
  `/usr/bin/python3 r3c2_ledger_tools.py compute <ledger.json> <out.json>` and prints its stdout and exit status. It
  computes each claim's `rests_on` from its `root_origins` and prints the root-origin set beside it; it REJECTS (exit 2) a
  ledger that arrives with `root_origins` or `rests_on` already set; it FAILS (exit 1) on a `derived_from` id that names
  no record, on a cycle, and on a `DERIVED` record with no `derived_from`, so an empty root set cannot occur; where the
  two seats' `origin` classifications differ the record carries `origin_alt` and the claim's `rests_on` is computed under
  both and marked `DISPUTED`.** A `rests_on` value present in the seat-authored input ledger fails this control; after a successful `compute` run,
  a `rests_on` value absent from the script-produced output ledger fails this control. **The arithmetic may consume only records with status `PRINTED` or `STANDARD`.** A
  script asserts that every value used appears in the ledger, that no `ABSENT` record carries a value, that **each
  `PRINTED` value machine-matches the text at its cited source line**, and that **each `STANDARD` value is one of a
  closed list PRINTED LITERALLY BELOW** — so "standard" cannot become a selectable family:

  | symbol | value | uncertainty |
  |---|---|---|
  | `G` | `6.67430e-11` m³ kg⁻¹ s⁻² | CODATA 2018 |
  | `c` | `2.99792458e8` m s⁻¹ | exact, by definition |
  | `ħ` | `1.054571817e-34` J s | exact, from the defined `h` |
  | `k_B` | `1.380649e-23` J K⁻¹ | exact, by definition |
  | `H₀` | `67.36` km s⁻¹ Mpc⁻¹ | `± 0.54` |
  | `Ω_m` | `0.3153` | `± 0.0073` |
  | `Ω_Λ` | `0.6847` | `± 0.0073` |
  | `Ω_b h²` | `0.02237` | `± 0.00015` |
  | `Ω_c h²` | `0.1200` | `± 0.0012` |
  | `n_s` | `0.9649` | `± 0.0042` |
  | `σ₈` | `0.8111` | `± 0.0060` |
  | `τ` | `0.0544` | `± 0.0073` |
  | `ln(10¹⁰ A_s)` | `3.044` | `± 0.014` |
  | age | `13.797` Gyr | `± 0.023` |

  The cosmological rows are the Planck 2018 TT,TE,EE+lowE+lensing baseline. **A value not in this table is not
  `STANDARD`**, whatever its provenance. 
  `C3_NO_SUBSTITUTION=PASS|FAIL|NOT_RUN`.
- 
  **C4 — what the seat must do.** Work **only** from the files in your working directory. **Print every path you
  open**, and print the working directory itself. Do not construct a path outside it; if you believe you need one,
  stop and report that instead of opening it. `C4_SEAT_ISOLATION=PASS` requires that printed path list and means only that the list contains no outside path; it
  makes no claim that the list is complete. Any path outside the copy directory is `FAIL`.

`C4_SEAT_ISOLATION=PASS|FAIL|NOT_RUN`.
- **C5 — harness, LIVE.** Execute and print `python3 --version`,
  `python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 $(command -v python3)`. **Transcribing
  expected values fails.** `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN`.
- **C5b — no cross-lane access.** Print every path opened, each marked `IN_SCOPE` or `OUT_OF_SCOPE`; **any
  `OUT_OF_SCOPE` row fails the control; PASS means the printed list contains no such row and makes no claim that the
  list is complete.** `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN`. 
- **C6 — audit, with a frozen sampling frame.** A third independent seat **first audits the full candidate and
  exclusion ledgers against every pinned source** — completeness, not just outcomes — then re-derives, **without sight of earlier work and re-classifying every input's `origin` from the pinned sources, and recomputing `rests_on` by the pinned script**: **(i) every claim in the arithmetic
  group** — no sampling discount — and **(ii) a sample of `min(max(1, ceil(0.20 × N)), R)` of the remaining included
  claims**, `N` being the sealed denominator and `R` the number of remaining claims (when `R` is zero the sample is empty
  and every included claim is already audited under (i)), drawn by `random.Random(seed_int).sample(remaining_ids, k)`
  where **`remaining_ids = sorted(set(included_ids) − set(arithmetic_group_ids))` and `seed_int = int(seed_hex, 16)`,
  the custodian's seed being 64 lowercase hexadecimal characters**.

  **The seed comes from outside this lane.** After the tally digests are receipted, **an external custodian
  outside this lane supplies a seed generated independently and unavailable to the lane before that receipt**, and it
  is recorded with the receipt. 
  

  An input on which the two classifications disagree is filed `ORIGIN_DISPUTED` and reported with both seats'
  classification and both quotations; it is **not** reconciled. Above 10% of included claims,
  `CENSUS_ORIGIN_DISPUTED`. Any outcome the audit cannot reproduce, or any ledger incompleteness, files
  `CENSUS_AUDIT_FAILED`. **A claim whose root-origin set contains an `ORIGIN_DISPUTED` input carries `rests_on` computed
  under both classifications, printed as a pair and marked `DISPUTED`; the `rests_on` tally reports a `DISPUTED` row.**
  **Classes are cited by name, never by number** — the numbering has shifted twice. `C6_AUDIT_SAMPLE=PASS|FAIL|NOT_RUN`.

Controls in an unreached limb are `NOT_RUN`, never passes.

## 6. Limb structure

**Limb A (~1 seat-day):** enumerate every quantitative claim and produce the input ledger. **No arithmetic.** If the
two enumerations disagree on any candidate's inclusion after two reconciliation attempts — **tolerance zero,
measured in candidate passages** — stop with `CENSUS_DENOMINATOR_DISPUTED` (§4). *(This sentence previously
survived here after being repaired in §2: the second live copy of a repaired rule is how the last defect got in,
so §6 now names the class rather than restating the rule.)*
**Limb B (2–3 seat-days):** the reproduction attempts, then the audit.

## 9. Inherited discipline

Live harness (C5); `ACCESS_SHA` proof for any pinned source audited, verified by the lane owner after the run and not
on the seat's claim; path lists (C5b); 120-second cap on symbolic operations with `SYMBOLIC_TIMEOUT` as a reportable
outcome; unreached controls `NOT_RUN`. Two independent seats. 



## 11. Scope

No tier, warrant token, standing or stamp moves. Published sources only; nothing from another lane. Paper HOLD;
nothing outward. 


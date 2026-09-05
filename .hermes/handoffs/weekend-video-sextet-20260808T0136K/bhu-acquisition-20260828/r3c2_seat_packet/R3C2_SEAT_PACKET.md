# R3-C2 seat packet — reproduction census: what to do

**You are one of two independent seats. Work only from this file, the seat brief, and the pinned
sources in this directory. Do not open any other path; print every path you open.**

This packet is a redacted extract of a preregistration. Sections concerning why the study exists and
what its results will be compared against have been removed **deliberately and mechanically** by
`r3c2_build_seat_packet.py`. Their absence is not an omission for you to fill in, and you should not
attempt to infer or reconstruct them. Apply the rules below exactly as written.

Built from master sha256 `5c69ae471edb1b1970594255e970fb07274fbb814dce1096de81c9d647ad1a5b` by `r3c2_build_seat_packet.py`.

## 1. The question, exactly

For every quantitative claim in the corpus, **two questions from one pass: (i) does the paper's own number follow
from the paper's own recipe applied to the inputs it states — chosen constants included; and (ii) what does that
number rest on — derived and standard inputs only, or a chosen, fitted, imported or undeclared one?** The first is the
reproduction verdict; the second is the ledger's `rests_on` field. **Neither contaminates the other.**

**Operational definition, so the enumeration is not a judgement:** a *quantitative claim* is a passage in a pinned
source that **prints a numeral the paper asserts as a result of its own** — with units, or dimensionless and stated
as a value. Excluded, by definition and not by taste: numerals that are equation numbers, reference numbers, page or
line numbers, dates, or values the paper attributes to another work without deriving. **Every candidate passage is
listed with file and line; inclusion and exclusion are both recorded.**
**Inclusion is assigned independently by the two pattern-blind seats from the §1 rule alone; disagreement on any
candidate stops the study under `CENSUS_DENOMINATOR_DISPUTED`, and the third seat audits the complete candidate and
exclusion ledgers against every pinned source.** *(codex: the audit trail records the boundary but does not make it
mechanical — whether a numeral is "the paper's own result" remains a judgement, so it moves from one reader to two
who must agree.)*



## 2. Method — per claim, in order

1. **Extract** the printed number, its units, and the equation the paper says produces it, with file and line.
2. **List the inputs** that equation needs.
3. **Classify each input** as `PRINTED` (given in the paper), `STANDARD` (a measured constant **on C3's closed
   list — that list, verbatim, and no other value**), or `ABSENT`. Record its `origin` with the evidence C3 requires.
4. **Attempt the arithmetic MECHANICALLY — follow the paper's own recipe, using every value it directs you to use,
   i.e. every ledger record with status `PRINTED` or `STANDARD`, chosen and fitted values included.** Provenance is
   **recorded** (C3's `origin`, `derived_from`, `root_origins`), never filtered on. *(V10, option (c): refusing chosen
   inputs stopped this being reproduction at all — a paper can direct you to use its own chosen constant, and
   following that instruction IS reproducing the paper.)*
5. **Record the outcome**, per claim, as one of §3, **and let the script record the claim's `rests_on`** from the ledger.

**A seat may not supply a value for an `ABSENT` input.** Encountering one ends that claim's attempt.

## 3. Per-claim outcomes — declared now


**One pass, two tallies (option (c), the principal's ruling 2026-09-05).** The reproduction verdict answers *"does the paper's
arithmetic work from what it states?"* The ledger answers *"what did it rest on?"* — a value can be printed in the
paper and still have been chosen or fitted, and under (c) both facts
survive: the arithmetic reproduces AND the ledger says what it rested on. So:

> **THE INPUTS THE ARITHMETIC MAY CONSUME** = every ledger record with status `PRINTED` (given in the paper, whatever
> its `origin`) or `STANDARD` (on C3's closed list). **PROVENANCE IS RECORDED, NOT FILTERED**: each record's `origin`
> is cited under C3, `root_origins` is computed by script, and the claim's **`rests_on`** field is computed by the
> same script — `DERIVED_ONLY` when every root origin is `DERIVED` or `STANDARD`; otherwise the most severe root
> origin present, in the fixed order `USES_UNDECLARED` > `USES_IMPORTED` > `USES_FITTED` > `USES_CHOSEN` — with the
> full root-origin set printed beside it. **No seat writes `rests_on`.** The interpretation step reads `rests_on`,
> never the reproduction verdict (§7).

- **`REPRO_EXACT`** — the paper's number follows, within its own stated precision, **from the paper's own recipe
  applied to the inputs it states** (`PRINTED` or `STANDARD`). The claim's `rests_on` is reported beside it.
- *(`REPRO_AFTER_CHOICE` — RETIRED at V10 by the principal's ruling adopting option (c). What it recorded — that the number
  rests on a chosen, fitted, imported or undeclared input — is now the `rests_on` field of a `REPRO_EXACT` or
  `REPRO_FAILED` claim, computed by script. Two blind C0 seats had found the class unreachable under the derivation-only
  wording (§10.3); it is retired, not repaired.)*
- **`REPRO_FAILED`** — the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the
  paper's number. Report both numbers. **Wording: "unreproduced from the stated inputs," not "error."** `rests_on`
  is reported beside it.
- **`REPRO_BLOCKED`** — an input traces to a source **outside this lane that we cannot obtain**. Name it. *(Distinct
  from `REPRO_INPUT_ABSENT`, which is an input the paper simply never states.)*
- **`REPRO_NOT_EVALUABLE`** — the arithmetic could not be completed within the 120-second cap, or requires machinery
  this lane does not have. Print `SYMBOLIC_TIMEOUT` and the point reached. *(Added because the stall guard had no
  per-claim outcome to file into.)*
- **`REPRO_NO_DERIVATION_STATED`** — the paper prints the claim as its own result but **states no equation or
  computational procedure that could produce it**, so there is nothing to attempt. Name the passage. *(A claim can
  satisfy §1 — a printed numeral asserted as the paper's own result — while the paper never says how it was
  obtained. That claim previously fell through every class.)*
- **`REPRO_INPUT_ABSENT`** — an input the equation needs is `ABSENT` from the paper, so the attempt stops there.
  **Name the input.**  Distinct from a claim whose inputs the paper DOES state, chosen or not — that
  claim is attempted and files `REPRO_EXACT` or `REPRO_FAILED` with its `rests_on`.
**Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the first in this
order:** `REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`, then the
**arithmetic group**. *(Precedence is stated because these conditions genuinely co-occur — an absent input whose
source is also unobtainable satisfied two classes with no rule to choose between them.)*

**The arithmetic group** is the set of outcomes that state whether the arithmetic reproduced the number: **exactly
`REPRO_EXACT` and `REPRO_FAILED`** (V10; the group had three members under the derivation-only wording).

**Candidate exclusions are not per-claim outcomes.** Every enumerated candidate passage that fails the §1
definition is recorded in a **separate exclusion ledger** with file, line, the numeral, and which excluded kind it
is (equation number, reference number, page/line number, date, or attributed-not-derived). The census denominator
is the count of **included** claims; the exclusion ledger is reported alongside it and audited under C6, so nothing
is hidden by being excluded. 

## 4. Study-level outcomes

1. **`CENSUS_COMPLETE`** — **every included claim carries exactly one outcome from the arithmetic group of §3.**
   Report the full tally with its denominator, **and the `rests_on` tally beside it — two tallies from one pass.**
2. **`CENSUS_PARTIAL`** — after two attempts, **at least one included claim carries a non-arithmetic outcome**
   (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`). Report each and
   why. **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.** *(Previously "some claims unresolved"
   was undefined, and a blocked claim satisfied both classes.)*
3. **`CENSUS_AUDIT_FAILED`** — the audit of §6 cannot reproduce a sampled per-claim outcome. The census is void; report
   which.
4. **`R3C2_NO_CLASS`** — a control fails **in every seat that attempted it** after two attempts.
5. **`CENSUS_DENOMINATOR_DISPUTED`** — the two enumerations disagree after two reconciliation attempts. The census
   does not proceed; the disputed candidates are listed. *(Added because the enumeration stop had no class.)*
6. **`CENSUS_ORIGIN_DISPUTED`** — the two seats' independent `origin` classifications disagree on inputs affecting
   **more than 10% of included claims**. The census does not proceed; every disputed input is listed with both
   seats' classification and both quotations. *(Disagreement about provenance is reported, never reconciled — if
   two blind readers cannot agree from the paper's own text what a number's provenance is, that is a finding about
   the corpus, and reconciling it would destroy it.)*
7. **`CENSUS_CONTROL_SPLIT`** — a control fails in one seat and passes in another after two attempts. Report both
   seats' outputs and stop; **do not adopt the passing seat's result.** *(Added because this reachable state landed in
   no class.)* *(Phrased this way
   because the old `R3C_NO_CLASS` said "in both seats", leaving a control that failed twice in one seat and passed in
   the other with no class — a gap codex found.)*




## 5. Controls, each with an exact named code

- **C0 — reachability, run BEFORE the freeze.** For **every per-claim outcome of §3** and **every study-level class
  of §4** — and for **any condition whose failure would refute this lane's own expectation** — **exhibit a concrete
  input that produces it**: a specific claim, its inputs, and the path it takes through this document to that
  verdict. **An outcome for which no such input can be exhibited is UNREACHABLE, and this preregistration does not
  freeze until it is.** The exhibition table is the artefact. **The exhibitions are authored by a seat and only
  verified by Tori** — deciding what counts as reachable is where an author's prior would enter, so the author does
  not decide it. `C0_REACHABILITY=PASS`.

  

- **C1 — denominator.** Claims **included**, claims **excluded** (with the exclusion ledger of §3), and attempts made,
  all printed before any tally. 
  `C1_DENOMINATOR_PRINTED=PASS`.
- **C2 — input ledger.** Every input classified `PRINTED` / `STANDARD` / `ABSENT`, each `PRINTED` one carrying file and
  line. `C2_INPUT_LEDGER=PASS`.
- **C3 — no substitution, machine-checked.** The input ledger is a **JSON file**, one record per input:
  `{claim_id, symbol, status: PRINTED|STANDARD|ABSENT, origin: DERIVED|STANDARD|CHOSEN|FITTED|IMPORTED|UNDECLARED,
  origin_evidence: {reason_code, source_file, source_line, verbatim}, derived_from: [input_id…], root_origins: […],
  value, source_file, source_line}`. *(`STANDARD` was missing from the `origin` enumeration while §3 defined
  admissibility partly by it, so a measured-constant record could not be validly filled in.)*

  **`origin` must be cited, not asserted.** Every record carries `origin_evidence` with a reason code —
  `ORIG_EQUATION`→`DERIVED`, `ORIG_CONSTANT`→`STANDARD`, `ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_FIT_STATED`→`FITTED`,
  `ORIG_CITATION`→`IMPORTED`, `ORIG_SILENT`→`UNDECLARED` — and, except for `ORIG_SILENT`, a **verbatim quotation
  machine-matched to the cited line**. **`UNDECLARED` is the default, not the residue**: a record leaves it only by
  producing that text, and an `ORIG_SILENT` record prints the search the seat ran.

  **Provenance is transitive, and the transitivity is computed.** Every `DERIVED` record lists its `derived_from`
  ids; **a script computes `root_origins`, the origins at the leaves of that chain, and no seat writes that field.**
  A chain cannot be made to look clean by classifying only its last step. **The same script computes each claim's
  `rests_on` from its `root_origins` by the fixed severity order of §3 and prints the root-origin set beside it; a
  `rests_on` value written by a seat, or absent, fails this control.** *(What `root_origins` implies for a
  claim's outcome follows from the clause held in §3 and is not decided here; the field is factual either way.)* **The arithmetic may consume only records with status `PRINTED` or `STANDARD`.** A
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
  `STANDARD`**, whatever its provenance. *(The list was previously "fixed here" by naming four symbols and citing a
  paper whose baseline runs to dozens of base, derived and nuisance parameters across several tables, none printed
  — so a machine membership test was impossible and "standard" was in practice a selectable family. kimi found it.)*
  `C3_NO_SUBSTITUTION=PASS|FAIL|NOT_RUN`.
- 
  **C4 — what the seat must do.** Work **only** from the files in your working directory. **Print every path you
  open**, and print the working directory itself. Do not construct a path outside it; if you believe you need one,
  stop and report that instead of opening it. `C4_PATTERN_BLIND=PASS` requires that printed path list.

`C4_PATTERN_BLIND=PASS`.
- **C5 — harness, LIVE.** Execute and print `python3 --version`,
  `python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 $(command -v python3)`. **Transcribing
  expected values fails.** `C5_HARNESS_PINNED=PASS`.
- **C5b — no cross-lane access.** Print every path opened, each marked `IN_SCOPE` or `OUT_OF_SCOPE`; **any
  `OUT_OF_SCOPE` row fails the control.** `C5B_NO_CROSS_LANE=PASS`. *("As R3A/R3B" named no command and no code, and
  a seat that never saw those studies cannot resolve it — the defect codex found in R3D's C5/C5b.)*
- **C6 — audit, with a frozen sampling frame.** A third pattern-blind seat **first audits the full candidate and
  exclusion ledgers against every pinned source** — completeness, not just outcomes — then re-derives, **without seeing
  prior work and re-classifying every input's `origin` from the pinned sources, and recomputing `rests_on` by the same script**: **(i) every claim whose filed
  outcome asserts that the arithmetic reproduced the number** — the class in which a result unreproduced from the stated inputs is both consequential
  and invisible, so it gets no sampling discount — and **(ii) a sample of `max(1, ceil(0.20 × N))` of the remaining
  included claims**, `N` being the sealed denominator, drawn by
  `random.Random(seed).sample(sorted(claim_ids), k)`.

  **The seed comes from outside this lane.** After the tally digests are receipted, **an external custodian
  outside this lane supplies a seed generated independently and unavailable to Tori before that receipt**, and it
  is recorded with the receipt. 
  *(Seeding from the tally's own digest let the tally's producer reshape non-semantic content — ordering, spacing,
  metadata — until a favourable sample appeared. A seed must not be a function of the thing being audited.)*

  An input on which the two classifications disagree is filed `ORIGIN_DISPUTED` and reported with both seats'
  classification and both quotations; it is **not** reconciled. Above 10% of included claims,
  `CENSUS_ORIGIN_DISPUTED`. Any outcome the audit cannot reproduce, or any ledger incompleteness, files
  `CENSUS_AUDIT_FAILED`. **Classes are cited by name, never by number** — the numbering has shifted twice. `C6_AUDIT_SAMPLE=PASS`.

Controls in an unreached limb are `NOT RUN`, never passes.

## 6. Limb structure

**Limb A (~1 seat-day):** enumerate every quantitative claim and produce the input ledger. **No arithmetic.** If the
two enumerations disagree on any candidate's inclusion after two reconciliation attempts — **tolerance zero,
measured in candidate passages** — stop with `CENSUS_DENOMINATOR_DISPUTED` (§4). *(This sentence previously
survived here after being repaired in §2: the second live copy of a repaired rule is how the last defect got in,
so §6 now names the class rather than restating the rule.)*
**Limb B (2–3 seat-days):** the reproduction attempts, then the audit.

## 9. Inherited discipline

Live harness; `ACCESS_SHA` proof for any pinned source audited, verified by Tori after the run and not on the seat's
claim; path lists; 120-second cap on symbolic operations with `SYMBOLIC_TIMEOUT` as a reportable outcome; unreached
controls `NOT RUN`. Blind double, third seat via `nm_referee_dispatch.sh` on a split, Kimi arithmetic with a
no-fallback control, one-page check sheet, Tori re-runs every script, critic note before any ruling.



## 11. Scope

No tier, warrant token, standing or stamp moves. Published sources only; nothing from another lane. Paper HOLD;
nothing outward. R3D is a separate document with its own gate record.


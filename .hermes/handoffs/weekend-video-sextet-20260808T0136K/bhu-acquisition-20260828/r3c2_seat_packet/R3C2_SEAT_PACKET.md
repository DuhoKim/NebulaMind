# R3-C2 seat packet — reproduction census: what to do

**You are one of two independent seats. Work only from this file, the seat brief, and the pinned
sources in this directory. Do not open any other path; print every path you open.**

This packet is the complete instruction set for your task, extracted mechanically by
`r3c2_build_seat_packet.py`. Apply the rules below exactly as written.

Built from master sha256 `fe194fb4aee7603dbeecbfeda62dc8507aba2a994e3b9a206c8089490700e1c9` by `r3c2_build_seat_packet.py`.

## 1. The question, exactly

For every quantitative claim in the corpus, **does the paper's own number follow from the paper's own recipe applied to the inputs it states **The reproduction verdict and the provenance fields are recorded separately.**

**Operational definition, so the enumeration is not a judgement:** a *quantitative claim* is a passage in a pinned
source that **prints a numeral the paper asserts as a result of its own** — with units, or dimensionless and stated
as a value. Excluded, by definition and not by taste: numerals that are equation numbers, reference numbers, page or
line numbers, dates, or values the paper attributes to another work without deriving. **Every candidate passage is
listed with file and line; inclusion and exclusion are both recorded.**
**Inclusion is assigned independently by the two independent seats from the §1 rule alone; disagreement on any
candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4): the
disputed candidates are listed and the complete candidate and exclusion ledgers are reported with the dispute.** 



## 2. Method — per claim, in order

**The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` (sha256 `300d4da144d96ae9f1390c9018e919ae1ba6cf00be9f45ad36fdccfdcfbf9b24`) lists every enumerable text by
digest and byte count; a seat enumerates claims from those files and no other. Files listed there as RAW are not enumerable
and are outside the census, visibly.** 

1. **Extract** the printed number, its units, and the equation the paper says produces it, with file and line.
2. **List the inputs** that equation needs.
3. **Classify each input** as `PRINTED` (given in the paper), `STANDARD` (a measured constant **on C3's closed
   list — that list, verbatim, and no other value**), `BLOCKED` (traced to a named source but carrying no
   machine-matchable value, §3), or `ABSENT`. **`STANDARD` applies only when the value appears in the claiming paper (or
   in a pinned enumerable text under the `IMPORTED` rule below): a value the paper does not print is classified by the
   named-source rule alone and is never `STANDARD`. Where a value the paper prints is on the closed list verbatim, file
   `STANDARD`; otherwise `PRINTED` — the two routes are outcome-identical, and this rule keeps both seats on the same
   one.** Record its `origin` with the evidence C3 requires.
4. **Attempt the arithmetic MECHANICALLY — follow the paper's own recipe, using every value it directs you to use,
   i.e. every ledger record with status `PRINTED` or `STANDARD`.** Provenance is recorded under C3 (`origin`, `derived_from`).
5. **Record the outcome**, per claim, as one of §3.

**A value the paper does not print but traces to a named source that is itself an enumerable text in `R3C2_CORPUS_MANIFEST.md` is
classified `PRINTED` from that source, with `origin` `IMPORTED`, `origin_evidence` `ORIG_CITATION` cited to the named
source's file and line, and the value machine-matched there — **only when such a match exists; a cited value that does
not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest,
files `REPRO_BLOCKED` under §3.** **A seat may not supply a value for an `ABSENT` or `BLOCKED` input.**
Encountering one ends that claim's attempt.

## 3. Per-claim outcomes — declared now




> **THE INPUTS THE ARITHMETIC MAY CONSUME** = every ledger record with status `PRINTED` (given in the paper, whatever
> its `origin`) or `STANDARD` (on C3's closed list). **Arithmetic consumes records according to status `PRINTED` or `STANDARD`.** Each record's `origin`
> is cited under C3, independently by both seats. **`origin` is one recorded attribute of a ledger record, beside
> `status`, `value`, `source_file` and `source_line`; a seat records it and writes no field outside the schema; `validate`
> fails a ledger that carries one. The seat's tool is `r3c2_ledger_tools.py`, sha256 `3519ca617434ddca222c0a85e8a5630f30710b8a9c7d74d79bfc4fa56973b959`, pinned
> beside the packet in `R3C2_SEAT_PACKET.sha256`; the seat runs its `census` and `validate` subcommands only.**



- **`REPRO_EXACT`** — the paper's number follows, within its own stated precision, **from the paper's own recipe
  applied to the inputs it states** (`PRINTED` or `STANDARD`). **Report both numbers.** **Where the paper states no
  precision for the claim, the printed precision is the claim's stated precision: the reproduced value must round to
  the printed numeral at that precision.** 

- **`REPRO_FAILED`** — the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the
  paper's number. Report both numbers. **Wording: "unreproduced from the stated inputs," not "error."**
- **`REPRO_BLOCKED`** — an input whose value the claiming paper does not print, and for which the claiming paper
  **names a source (a citation)** that either **is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`** or **is
  an enumerable pinned text at whose cited line the value does not machine-match**; in the first case whether that
  source is obtainable elsewhere is irrelevant, because the census may not open or consume it. Name the input and the
  source. It is recorded with status `BLOCKED` (C3) and never consumed. *(Distinct from `REPRO_INPUT_ABSENT`, which is an input the paper neither prints nor traces to any named
  source; a value cited from a pinned enumerable text is `PRINTED` there under §2.)* 
- **`REPRO_NOT_EVALUABLE`** — the arithmetic could not be completed within the 120-second cap, or requires machinery
  this lane does not have. Print `SYMBOLIC_TIMEOUT` when the 120-second cap is exceeded, or `MACHINERY_UNAVAILABLE` when the lane lacks the
  machinery, and the point reached. 
- **`REPRO_NO_DERIVATION_STATED`** — the paper prints the claim as its own result but **states no equation or
  computational procedure that could produce it**, so there is nothing to attempt. Name the passage. 
- **`REPRO_INPUT_ABSENT`** — an input the equation needs is `ABSENT` from the paper — **neither printed nor traced to
  any named source** — so the attempt stops there. **Name the input.**  Distinct from a claim whose inputs the paper DOES state, chosen or not — that
  claim is attempted and files `REPRO_EXACT` or `REPRO_FAILED`.
**Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the first in this
order:** `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the
**arithmetic group**. 

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
   Report the full tally with its denominator
2. **`CENSUS_PARTIAL`** — after the §2 attempt (one repeat permitted, meaningful only for `REPRO_NOT_EVALUABLE`),
   **at least one included claim carries a non-arithmetic outcome**
   (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`). Report each and
   why. **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.** 
3. **`CENSUS_AUDIT_FAILED`** — the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, **or the receipt verification
   of the seal fails**. No tally is filed; report which.
4. **`R3C2_NO_CLASS`** — a control among C0 through C5b fails **in every seat that attempted it** after two attempts;
   a packet or seat-isolation failure before dispatch files this class. **A C6 audit failure or a
   seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class.**
5. **`CENSUS_DENOMINATOR_DISPUTED`** — the two enumerations disagree after two reconciliation attempts, **or the two
   seats' input lists for the agreed claims disagree after the one C3 reconciliation**. The census does not proceed; the
   disputed candidates or inputs are listed. 
6. **`CENSUS_ORIGIN_DISPUTED`** — the two seats' independent `origin` classifications disagree on inputs affecting
   **more than 10% of included claims**. The census does not proceed; every disputed input is listed with both
   seats' classification and both quotations. 
7. **`CENSUS_CONTROL_SPLIT`** — a control fails in one seat and passes in another after two attempts. Report both
   seats' outputs and stop; **do not adopt the passing seat's result.**  

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

  

- **C1 — denominator.** Claims **included**, claims **excluded** (with the exclusion ledger of §3), and the attempts
  made, all printed before any tally. 
  **The candidate file is a JSON object `{declared_candidate_count, declared_included_count, declared_excluded_count,
  declared_attempt_count, candidates: [...]}`; every included candidate carries `attempts`, the number of §2 attempts made
  on it, in {0, 1, 2}, and `declared_attempt_count` is their sum and the exclusion file is `{declared_exclusion_count, exclusions: [...]}`. Before the tally, print
  those four declared counts verbatim from the files, then run
  `/usr/bin/python3 r3c2_ledger_tools.py census <candidates.json> <exclusions.json>`: PASS requires exit 0 after the
  script verifies that every candidate has exactly one disposition, that every exclusion names one excluded candidate,
  that every included candidate carries a permitted `attempts` value, and that each of the four declared counts equals
  the count recomputed from the rows; its stdout prints both the declared and the
  recomputed counts. Print its command, stdout and exit status.** The candidate and exclusion ledgers use the script's candidate schema: each candidate carries
  `candidate_id`, `source_file`, `source_line`, `numeral`, `included`; every exclusion row names a candidate and a `kind`;
  the script's failure lines name any missing field. `C1_DENOMINATOR_PRINTED=PASS|FAIL|NOT_RUN`, PASS only on exit 0.
- **C2 — input ledger.** Every input classified `PRINTED` / `STANDARD` / `ABSENT` / `BLOCKED`, each `PRINTED` one carrying file and
  line, in the JSON schema of C3, validated by `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .` run from the printed seat working
  directory (`.` is the sole allowed `sources_dir`); before execution the seat prints the fully resolved command with
  every angle-bracket placeholder replaced by the actual in-scope path
  (exit 0 = PASS; every failure printed). `C2_INPUT_LEDGER=PASS|FAIL|NOT_RUN`.
- **C3 — no substitution, machine-checked.** The input ledger is a **JSON file**, one record per input:
  `{claim_id, input_id, symbol, status: PRINTED|STANDARD|ABSENT|BLOCKED, origin: CHOSEN|DERIVED|FITTED|IMPORTED|MEASURED|STANDARD|UNDECLARED,
  origin_evidence: {reason_code, source_file, source_line, verbatim}, origin_search: {query, files, matches} (required
  when reason_code is ORIG_SILENT), derived_from: [input_id…], value, source_file, source_line}`. **The seat-authored
  ledger carries only the schema fields; `validate` fails a ledger that carries any other field.** An input that files `REPRO_BLOCKED` under §3 is recorded with status `BLOCKED`,
  `origin` `IMPORTED`, `ORIG_CITATION` evidence cited to the claiming paper's naming sentence, and no value; the arithmetic
  never consumes it.** 

  **`origin` must be cited, not asserted.** Every record carries `origin_evidence` with a reason code —
  `ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_EQUATION`→`DERIVED`, `ORIG_FIT_STATED`→`FITTED`, `ORIG_CITATION`→`IMPORTED`,
  `ORIG_MEASURED`→`MEASURED` (a quantity the paper reports as its own measurement, with the measurement described),
  `ORIG_CONSTANT`→`STANDARD`, `ORIG_SILENT`→`UNDECLARED` (listed alphabetically by origin; the list carries no order of its own) — and, except for `ORIG_SILENT`, a **verbatim quotation
  machine-matched to the cited line**. **Every input's `origin` is classified independently by both seats.** **Where
  more than one reason code matches the cited sentence, file the first in this order: `ORIG_CITATION`,
  `ORIG_FIT_STATED`, `ORIG_CHOICE_STATED`, `ORIG_MEASURED`, `ORIG_EQUATION`, `ORIG_CONSTANT`, `ORIG_SILENT` — a sentence
  that names an external source for the value is a citation whatever else it says — the order is a tie-break by the
  specificity of the evidence, not a ranking of the values.**  **`UNDECLARED` is the default, not the residue**: a record leaves it only by
  producing that text, and an `ORIG_SILENT` record prints the search the seat ran.

  **Provenance is transitive.** Every `DERIVED` record lists its `derived_from` ids; `validate` fails a `derived_from` id
  that names no record, a cycle, and a `DERIVED` record with no `derived_from`. **The arithmetic may consume only records with status `PRINTED` or `STANDARD`.** A
  script asserts that no `ABSENT` or `BLOCKED` record carries a value, that **each `PRINTED` value machine-matches the
  text at its cited source line and each verbatim quotation is a substring of that line**, and that **each `STANDARD`
  value is one of a closed list PRINTED LITERALLY BELOW** — so "standard" cannot become a selectable family;
  **completeness of a claim's input list against the paper's equation is seat-authored and audited under C6, not
  machine-checked**:

  | symbol | ledger key | value | uncertainty |
  |---|---|---|---|
  | `G` | `G` | `6.67430e-11` m³ kg⁻¹ s⁻² | CODATA 2018 |
  | `c` | `c` | `2.99792458e8` m s⁻¹ | exact, by definition |
  | `ħ` | `hbar` | `1.054571817e-34` J s | exact, from the defined `h` |
  | `k_B` | `k_B` | `1.380649e-23` J K⁻¹ | exact, by definition |
  | `H₀` | `H0` | `67.36` km s⁻¹ Mpc⁻¹ | `± 0.54` |
  | `Ω_m` | `Omega_m` | `0.3153` | `± 0.0073` |
  | `Ω_Λ` | `Omega_L` | `0.6847` | `± 0.0073` |
  | `Ω_b h²` | `Omega_b_h2` | `0.02237` | `± 0.00015` |
  | `Ω_c h²` | `Omega_c_h2` | `0.1200` | `± 0.0012` |
  | `n_s` | `n_s` | `0.9649` | `± 0.0042` |
  | `σ₈` | `sigma8` | `0.8111` | `± 0.0060` |
  | `τ` | `tau` | `0.0544` | `± 0.0073` |
  | `ln(10¹⁰ A_s)` | `ln1e10As` | `3.044` | `± 0.014` |
  | age | `age_Gyr` | `13.797` Gyr | `± 0.023` |

  The cosmological rows are the Planck 2018 TT,TE,EE+lowE+lensing baseline. **A value not in this table is not
  `STANDARD`**, whatever its provenance. **A `STANDARD` record carries `symbol` = the ledger key and `value` = the exact
  string printed in the value column; `validate` compares strings.** 
  `C3_NO_SUBSTITUTION=PASS|FAIL|NOT_RUN`.
- 
  **C4 — what the seat must do.** Work **only** from the files in your working directory. **Print every path you
  open**, and print the working directory itself. Do not construct a path outside it; if you believe you need one,
  stop and report that instead of opening it. `C4_SEAT_ISOLATION=PASS` requires that printed path list and means only that the list contains no outside path; it
  makes no claim that the list is complete. Any path outside the working directory is `FAIL`.

`C4_SEAT_ISOLATION=PASS|FAIL|NOT_RUN`.
- **C5 — harness, LIVE.** Execute and print `/usr/bin/python3 --version`,
  `/usr/bin/python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 /usr/bin/python3` — the interpreter
  every ledger command runs under. **PASS requires all three commands to exit 0 and their full stdout to be printed; any
  non-zero exit, missing output, or a transcribed value in place of live output is FAIL.** `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN`.
- **C5b — no cross-lane access.** Print every path opened, each marked `IN_SCOPE` or `OUT_OF_SCOPE`; **any
  `OUT_OF_SCOPE` row fails the control; PASS means the printed list contains no such row and makes no claim that the
  list is complete.** `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN`. 
- **C6 — audit, with a frozen sampling frame.** A third independent seat **first audits the full candidate and
  exclusion ledgers against every pinned source** — completeness, not just outcomes — then re-derives, **without sight of earlier work and re-classifying every input's `origin` from the pinned sources**: **(i) every claim in the arithmetic
  group** — no sampling discount — and **(ii) a sample of `min(max(1, ceil(0.20 × N)), R)` of the remaining included
  claims**, `N` being the sealed denominator and `R` the number of remaining claims (when `R` is zero the sample is empty
  and every included claim is already audited under (i)), drawn by `random.Random(seed_int).sample(remaining_ids, k)`
  where **`remaining_ids = sorted(set(included_ids) − set(arithmetic_group_ids))` and `seed_int = int(seed_hex, 16)`,
  the custodian's seed being 64 lowercase hexadecimal characters**.

  **The seed comes from outside this lane.** After the tally digests are receipted, **an external custodian
  outside this lane supplies a seed generated independently and unavailable to the lane before that receipt**, and it
  is recorded with the receipt. **If the seed is not supplied and recorded with the receipt, the audit does not run,
  `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named.** 
  

  An input on which the two classifications disagree is filed `ORIGIN_DISPUTED` and reported with both seats'
  classification and both quotations; it is **not** reconciled. Above 10% of included claims,
  `CENSUS_ORIGIN_DISPUTED`. Any outcome the audit cannot reproduce, or any ledger incompleteness, files
  `CENSUS_AUDIT_FAILED`.
  **Classes are cited by name, never by number**. `C6_AUDIT_SAMPLE=PASS|FAIL|NOT_RUN`.

Controls in an unreached limb are `NOT_RUN`, never passes.

## 6. Limb structure

**Limb A (~1 seat-day):** enumerate every quantitative claim and produce the input ledger. **No arithmetic.** If the
two enumerations disagree on any candidate's inclusion after two reconciliation attempts — **tolerance zero,
measured in candidate passages** — stop with `CENSUS_DENOMINATOR_DISPUTED` (§4). 
**Limb B (2–3 seat-days):** the reproduction attempts, then the audit.

## 9. Inherited discipline

Live harness (C5); `ACCESS_SHA` proof for any pinned source audited, verified by the lane owner after the run and not
on the seat's claim; path lists (C5b); every symbolic operation launched through the committed wrapper `r3c2_timeout.py` (sha256
`fbb9bef7d6622a17b4dc2e856791e3166b60394c187286ea5581b2f39003f331`) as `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>`, which enforces a 120.0-second wall-clock
deadline on the monotonic clock, prints the wrapper command, the child's stdout and stderr and its exit status, and on
the deadline prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome; unreached controls `NOT_RUN`. Two independent seats. 



## 11. Scope

No tier, warrant token, standing or stamp moves. Published sources only; nothing from another lane.  


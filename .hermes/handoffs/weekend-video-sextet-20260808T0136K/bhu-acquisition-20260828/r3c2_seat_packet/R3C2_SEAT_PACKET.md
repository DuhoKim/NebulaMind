# R3-C2 seat packet — reproduction census: what to do

**You are one of two independent seats. Work only from this file, the seat brief, and the pinned
sources in this directory. Do not open any other path; print every path you open.**

This packet is the complete instruction set for your task, extracted mechanically by
`r3c2_build_seat_packet.py`. Apply the rules below exactly as written.

Built from master sha256 `34c90d0b4062f3443ff099d7af33326bc2b79080f28901618c9fe3f46a0c171c` by `r3c2_build_seat_packet.py`.

## 1. The question, exactly

For every quantitative claim in the corpus, **does the paper's own number follow from the paper's own recipe applied to the inputs it states.** **The reproduction verdict and the provenance fields are recorded separately.**

**Operational definition, so the enumeration is not a judgement:** a *quantitative claim* is a passage in a pinned
source that **prints a numeral the paper asserts as a result of its own** — with units, or dimensionless and stated
as a value. Excluded, by definition and not by taste: numerals that are equation numbers, reference numbers, page or
line numbers, dates, values the paper attributes to another work without deriving, or numerals the paper sets as inputs to its own
calculation rather than asserts as results of its own (`AUTHOR_SPECIFIED_INPUT`, §3). **Every candidate passage is
listed with file and line; inclusion and exclusion are both recorded.**
**Inclusion is assigned independently by the two independent seats from the §1 rule alone; disagreement on any
candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4): the
disputed candidates are listed and the complete candidate and exclusion ledgers are reported with the dispute.** 



## 2. Method — per claim, in order

**The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` (sha256 `26dabe7cd94d3f2a1501c347ec1193b83528325905dc417c85e28a4a2fe84096`) lists every enumerable text by
digest and byte count; a seat enumerates claims from those files and no other. Files listed there as RAW are not enumerable
and are outside the census, visibly.** 

1. **Extract** the printed number, its units, and the equation the paper says produces it, with file and line.
2. **List the inputs** that equation needs.
3. **Classify each input** as `PRINTED` (given in the paper), `STANDARD` (a measured constant **on C3's closed
   list — that list, verbatim, and no other value**), `BLOCKED` (traced to a named source but carrying no
   machine-matchable value, §3), or `ABSENT`. **`STANDARD` applies to a closed-list value printed in the claiming paper: for every `STANDARD` record `validate` binds `claim_id` to the claiming file through the candidate file and checks its own positive value coordinates and numeric token; a value outside the claiming file follows the named-source rule and is recorded `PRINTED`/`IMPORTED` with `ORIG_CITATION`, a verified enumerable source and the first symbol-and-value line, even when the value is on the closed list; a missing candidate binding or a `STANDARD` value line outside the claiming file fails `validate`. Where a value the paper prints is on the closed list verbatim, file
   `STANDARD`; otherwise `PRINTED` — the two routes are outcome-identical, and this rule keeps both seats on the same
   one.** Record its `origin` with the evidence C3 requires.
4. **Attempt the arithmetic MECHANICALLY — follow the paper's own recipe, using every value it directs you to use,
   i.e. every ledger record with status `PRINTED` or `STANDARD`.** Provenance is recorded under C3 (`origin`, `derived_from`).
5. **Record the outcome**, per claim, as one of §3, in the candidate file's `outcome` field; the sealed reproduction tally is
   the merged candidate file on which the two seats' `outcome` fields agree, claim by claim, after one reconciliation against
   the printed numeral and the stated-precision rule of §3; a disagreement surviving that reconciliation files
   `CENSUS_OUTCOME_DISPUTED` (§4).

**A value the claiming paper does not print but traces to a named source is classified `PRINTED` with `origin` `IMPORTED` only when
that source is an enumerable text of `R3C2_CORPUS_MANIFEST.md` whose bytes verify against its manifest row, and the value machine-matches
as a numeric token at the cited source line.** The record's `source_file`/`source_line` name that external value line; `origin_evidence`
carries `ORIG_CITATION` with a non-empty verbatim quotation of the CLAIMING paper's sentence naming the source, at the claiming paper's
own file and line (the claiming file is the file of the candidate row the record's `claim_id` names). A locally printed value may have origin `IMPORTED`: when `source_file` equals the claiming file (the paper itself prints "we adopt a = 3 from X"), `validate` checks the locally printed value and the claiming paper's citation quotation without requiring a different source file; the external-source manifest, numeric-token and first-line checks apply only when `source_file` differs from the claiming file. In that external case the origin records the claiming paper's import regardless of how the external source obtained the value; no reason code is applied to the source's line. **Where the
value machine-matches at more than one line of the named source, the seat files the first line carrying both the symbol and the
numeral; `validate` fails any other line.** If the named source is not enumerable or the value does not match there, file `REPRO_BLOCKED`
under §3. C3's pair rule: `ORIG_CITATION` is satisfied by that quotation at the claiming paper.

**Machine floor, stated.** For EVERY `PRINTED` record `validate` first binds the claim to its claiming file through the candidate file;
a record whose value line lies in another file must be `IMPORTED` with `ORIG_CITATION`, whatever reason code was submitted. For an external import, whose value line is outside the claiming file, validate checks that the evidence file is the claiming file, the external source is an exact manifest row with verified bytes, the non-empty quotation occurs at the cited claiming line, and the cited source line is the first line carrying both the symbol and the numeric value token. A locally printed import instead follows the local-import branch above. Whether the quotation cites THAT value
is seat judgement; the second seat and C6 may detect an error, but can share it, and C6 re-classifies inputs only for selected claims. **A seat may not supply a value for an `ABSENT` or `BLOCKED` input.** Encountering one ends that claim's attempt.

## 3. Per-claim outcomes — declared now




> **THE INPUTS THE ARITHMETIC MAY CONSUME** = every ledger record with status `PRINTED` (given in the paper, whatever
> its `origin`) or `STANDARD` (on C3's closed list). **Arithmetic consumes records according to status `PRINTED` or `STANDARD`.** Each record's `origin`
> is cited under C3, independently by both seats. **`origin` is one recorded attribute of a ledger record, beside
> `status`, `value`, `source_file` and `source_line`; a seat records it and writes no field outside the schema; `validate`
> fails a ledger that carries one. The seat's tool is `r3c2_ledger_tools.py`, sha256 `6c938c3f6b8af37e96996b963ea5ab8daebc52b13561e8af379035ba39622a3a` (`validate` takes the candidate file as its third argument), pinned at
> `R3C2_SEAT_PACKET.sha256` in the seat working directory; the seat runs its `census` and `validate` subcommands only.**



- **`REPRO_WITHIN_STATED_PRECISION`**  — the paper's number follows, within its own stated precision, **from the paper's own recipe
  applied to the inputs it states** (`PRINTED` or `STANDARD`). **Report both numbers.** **Where the paper states no
  precision for the claim, the printed precision is the claim's stated precision: the reproduced value must round to
  the printed numeral at that precision, rounding half away from zero.** **Where the paper states an uncertainty, the test is |reproduced − printed| ≤ the stated
  uncertainty, taken once — not doubled, not rounded; where it states none, the rounding rule above applies. Where the stated uncertainty is asymmetric,
  the stated uncertainty is the half-width on the side the reproduced value falls.** 

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
  computational procedure that could produce it**, so there is nothing to attempt. Name the passage. **A procedure named but not
  specified — a sentence that says where the number came from without stating operations a seat could attempt — states no
  computational procedure that could produce it; file this class and name the passage.** 
- **`REPRO_INPUT_ABSENT`** — an input the equation needs is `ABSENT` from the paper — **neither printed nor traced to
  any named source** — so the attempt stops there. **Name the input.**  Distinct from a claim whose inputs the paper DOES state, chosen or not — that
  claim is attempted and files `REPRO_WITHIN_STATED_PRECISION` or `REPRO_FAILED`.
**Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the first in this
order:** `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the
**arithmetic group**. 

**The arithmetic group** is the set of outcomes that state whether the arithmetic reproduced the number: **exactly
`REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`**.

**Candidate exclusions are not per-claim outcomes.** Every enumerated candidate passage that fails the §1
definition is recorded in a **separate exclusion ledger** with file, line, the numeral, and which excluded kind it
is (equation number, reference number, page/line number, date, attributed-not-derived, or author-specified input). **The exclusion ledger's `kind` is one of `AUTHOR_SPECIFIED_INPUT`, `ATTRIBUTED_NOT_DERIVED`, `DATE`, `EQUATION_NUMBER`,
`PAGE_OR_LINE_NUMBER`, `REFERENCE_NUMBER` (alphabetical). `AUTHOR_SPECIFIED_INPUT` — a numeral the paper sets rather than derives and does not
assert as a result of its own: a grid size, a cutoff, a parameter adopted "for this calculation", a range chosen for a plot. Every exclusion
row carries the candidate's `source_file`, `source_line` and `numeral` — excluded from judgement, retained in the record, never discarded —
and `census` fails a row that lacks them or differs from its candidate row; `census` prints the `AUTHOR_SPECIFIED_INPUT` count as its own
line beside the denominator.**  The census denominator
is the count of **included** claims; the exclusion ledger is reported alongside it and audited under C6, so nothing
is hidden by being excluded. 

## 4. Study-level outcomes

1. **`CENSUS_COMPLETE`** — **every included claim carries exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`. A
   denominator of zero files `CENSUS_PARTIAL` with the empty enumeration named; no census is complete over nothing.**
   Report the full tally with its denominator
2. **`CENSUS_PARTIAL`** — after the §2 attempt (one repeat permitted, meaningful only for `REPRO_NOT_EVALUABLE`),
   **at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`,
   `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`), or the denominator is zero**. Report each and
   why. **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.** 
3. **`CENSUS_AUDIT_FAILED`** — the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the
   cause named), **or the receipt verification
   of the seal fails**. No tally is filed; report which.
4. **`R3C2_NO_CLASS`** — a control among C0 through C5b fails **in every seat that attempted it** after two attempts;
   a packet or seat-isolation failure before dispatch files this class. **A C6 audit failure or a
   seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class.**
5. **`CENSUS_DENOMINATOR_DISPUTED`** — the two enumerations disagree after two reconciliation attempts, **or the two
   seats' input lists for the agreed claims disagree after the one C3 reconciliation**. The census does not proceed; the
   disputed candidates or inputs are listed. 
6. **`CENSUS_OUTCOME_DISPUTED`** — the two seats' filed per-claim outcomes on an agreed included claim differ after one
   reconciliation against the printed numeral and the stated-precision rule of §3. The census does not proceed; the claim is
   listed with both seats' outcomes, both number pairs, and the step each seat reached. 

7. **`CENSUS_ORIGIN_DISPUTED`** — the two seats' independent `origin` classifications disagree on inputs affecting
   **more than 10% of included claims**. The census does not proceed; every disputed input is listed with both
   seats' classification and both quotations. 
8. **`CENSUS_CONTROL_SPLIT`** — a control fails in one seat and passes in another after two attempts. Report both
   seats' outputs and stop; **do not adopt the passing seat's result.**  

**Exactly one study-level outcome is filed. Where more than one condition holds, file the first in this order:**
`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`,
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
  made, all printed before any tally. **A seat is a sequence of sessions under one packet: the manifest's texts are partitioned into
  ownership batches (the pinned partition of `R3C2_CORPUS_MANIFEST.md` into 12 batches in row order); every session holds ALL pinned texts
  and enumerates ONLY its owned texts; §2's named-source lookups may read any manifest text and are logged with file and line. Every
  candidate id, claim id and input id begins with `<owned file>#`. Each session writes `candidates_b<k>.json`, `exclusions_b<k>.json`,
  `ledger_b<k>.json` and `SEAT_REPORT_b<k>.md`, sealed by the custodian in batch order before the next batch is dispatched, in a LIMB-A chain; the lane's pinned `join` (pure function, no renaming; `r3c2_batch_tools.py`, sha256 `3822f12c282aaf4b5c850bef08fbfbe3bce81ac09d5f9e3c578459239439f79e`; partition `39b8d9bf199265ab…`) produces the seat's one candidate file, one exclusion file and one ledger, over which `census` and `validate` run, and §6's two-seat agreement on limb A is obtained before any arithmetic. Limb B uses a separate directory from limb A: the custodian copies the agreed limb-A batch artefacts into that directory under the canonical names `candidates_b<k>.json`, `exclusions_b<k>.json`, `ledger_b<k>.json` and `SEAT_REPORT_b<k>.md`; the seat updates only these limb-B copies, records final outcomes, and runs `census … final` on them; the custodian seals and joins that directory in a separate ordered LIMB-B chain bound to the agreed limb-A seals file; the limb-A directory and seals remain unchanged; no `_limbB` filename suffix is used; `join` of the limb-B chain verifies the binding. The ownership list `OWNERSHIP_b<k>.txt` a session reads is the custodian's extract of the pinned partition, listed with its digest in the dispatch record. The files named below are the joined files of the applicable limb.** 
  **The candidate file is a JSON object `{declared_candidate_count, declared_included_count, declared_excluded_count,
  declared_attempt_count, candidates: [...]}`; every included candidate carries `attempts`, the number of §2 attempts made
  on it, in {0, 1, 2}, and `declared_attempt_count` is their sum and the exclusion file is `{declared_exclusion_count, exclusions: [...]}`. Before the tally, print these five declared counts verbatim from the files — `declared_candidate_count`,
  `declared_included_count`, `declared_excluded_count`, `declared_attempt_count`, `declared_exclusion_count` — then run
  `/usr/bin/python3 -E r3c2_ledger_tools.py census <candidates.json> <exclusions.json>`: PASS requires exit 0 after the
  script verifies that every candidate has exactly one disposition, that every exclusion names one excluded candidate, that every excluded candidate is named by exactly one exclusion row,
  that every included candidate carries a permitted `attempts` value, and that each of the five declared counts equals
  the count recomputed from the rows; its stdout prints both the declared and the
  recomputed counts. Print its command, stdout and exit status.** The candidate and exclusion ledgers use the script's candidate schema: each candidate carries
  `candidate_id`, `source_file`, `source_line`, `numeral`, `included`; every included candidate additionally carries `outcome` —
  one of the six §3 tokens, or `PENDING` before limb B — and every included candidate whose `outcome` is in the arithmetic
  group carries `printed_value` and `reproduced_value` (strings, as printed and as computed); every exclusion row names a
  candidate and a `kind`; after limb B the seat runs `/usr/bin/python3 -E r3c2_ledger_tools.py census <candidates.json> <exclusions.json> final`, with
  all placeholders resolved, and prints its output; that run verifies that every included candidate carries exactly one §3
  outcome, none is `PENDING`, and arithmetic-group outcomes carry both values;
  the script's failure lines name any missing field. `C1_DENOMINATOR_PRINTED=PASS|FAIL|NOT_RUN`, PASS only on exit 0.
- **C1B — batch coverage.** `C1B_BATCH_COVERAGE=PASS` iff every manifest text is owned by exactly one batch, every owned text's bytes
  verify against its manifest row, and every batch report prints the packet's `ACCESS_SHA`; `JOIN=PASS` iff every seal matches, the
  ordered predecessor chain is intact from a root with no predecessor, every candidate and ledger claim is owned by its batch, every
  evidence source is a manifest text, identifiers are unique and every `derived_from` resolves acyclically. Either FAIL stops the seat's
  tally. `C1B_BATCH_COVERAGE=PASS|FAIL|NOT_RUN`. `JOIN=PASS|FAIL|NOT_RUN`. Both are C1B controls for §4: a FAIL in every seat that tries it, after two tries, files `R3C2_NO_CLASS`; a surviving fail/pass split files `CENSUS_CONTROL_SPLIT`; an unreached check is `NOT_RUN`.
- **C2 — input ledger.** Every input classified `PRINTED` / `STANDARD` / `ABSENT` / `BLOCKED`, each `PRINTED` one carrying file and
  line, in the JSON schema of C3, validated — after all limb-A batches are sealed and joined, since a cross-batch `derived_from` resolves only in the joined ledger (per-session validation is `NOT_RUN`) — by `/usr/bin/python3 -E r3c2_ledger_tools.py validate <joined_ledger.json> . <joined_candidates.json>` run from the seat's integration working directory holding all pinned texts (`.` is the sole allowed `sources_dir`); both seats' joined validation must PASS before limb-A agreement or arithmetic; before execution the seat prints the fully resolved command with
  every angle-bracket placeholder replaced by the actual in-scope path
  (exit 0 = PASS; every failure printed; the printed C3 run — command, stdout, stderr, exit status — is this control's
  artefact). `C2_INPUT_LEDGER=PASS|FAIL|NOT_RUN`.
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
  machine-matched to the cited line** — before any status-specific branch, `validate` requires every non-`ORIG_SILENT` record — `PRINTED`, `STANDARD`, `ABSENT` and `BLOCKED` alike — to carry a non-empty quotation occurring at the positive, one-based `origin_evidence.source_line` in `origin_evidence.source_file` (an `ABSENT` input keeps whatever origin its evidence supports — an unprinted measurement is `MEASURED` with its describing sentence quoted — and is not forced into `UNDECLARED` to close the corner); value-line checks are separate and never substitute for this evidence check; every `STANDARD` record, including one with `ORIG_SILENT`, requires a non-empty `source_file`, a positive one-based `source_line`, closed-list membership and the value as a numeric token at that line — absence of origin evidence never waives value evidence; every `BLOCKED` record requires an empty value, `IMPORTED`/`ORIG_CITATION`, and a candidate-file binding proving that its naming-evidence file is the claiming file; missing coordinates or a missing candidate binding fails `validate`. **Every input's `origin` is classified independently by both seats.** **Where
  more than one reason code matches the cited sentence, file the first in this order: `ORIG_CITATION`,
  `ORIG_FIT_STATED`, `ORIG_CHOICE_STATED`, `ORIG_MEASURED`, `ORIG_EQUATION`, `ORIG_CONSTANT`, `ORIG_SILENT` — a sentence
  that names an external source for the value is a citation whatever else it says — the order is a tie-break by the
  specificity of the evidence, not a ranking of the values.** **For an imported value (§2) `ORIG_CITATION` is satisfied by the non-empty verbatim quotation of the
  claiming paper's naming sentence at the claiming paper's own file and line; no reason code is applied to the source's line.**  **`UNDECLARED` is the default, not the residue**: a record leaves it only by
  producing that text, and an `ORIG_SILENT` record prints the search the seat ran; that printed `origin_search` (query, files, matches) is the
  mechanism by which the second seat and the auditor judge the search adequate — a search of one query with no variants is
  not adequate, and the auditor re-classifies the record from the pinned sources.

  **Provenance is transitive.** Every `DERIVED` record lists its `derived_from` ids; `validate` fails a `derived_from` id
  that names no record, a cycle, and a `DERIVED` record with no `derived_from`. **The arithmetic may consume only records with status `PRINTED` or `STANDARD`.** A
  script asserts that no `ABSENT` or `BLOCKED` record carries a value, that **each `PRINTED` value machine-matches its `source_file`/`source_line` as a numeric token and each non-`ORIG_SILENT` quotation occurs at its own `origin_evidence.source_file`/`source_line` — the evidence line may differ from the value line, and no second quotation check is applied to the value line**, and that **each `STANDARD` value is one of a closed list PRINTED LITERALLY BELOW and satisfies its own value-line check** — so "standard" cannot become a selectable family;
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
  Each seat runs `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> <sources_dir> <candidates.json>` with the placeholders resolved and prints the working directory, the resolved command, complete stdout and stderr, and the exit status; the
  control's printed artefact is that run. `C3_NO_SUBSTITUTION=PASS` only on exit 0 from every printed run in the artefact; a
  token asserted without the printed run is FAIL.
  `C3_NO_SUBSTITUTION=PASS|FAIL|NOT_RUN`.
- 
  **C4 — what the seat must do.** Work **only** from the files in your working directory. **Print every path you
  open**, and print the working directory itself. Do not construct a path outside it; if you believe you need one,
  stop and report that instead of opening it. `C4_SEAT_ISOLATION=PASS` requires that printed path list and means only that the list contains no outside path; it
  makes no claim that the list is complete. Any seat-chosen path outside (i)–(ii) below is `FAIL`; the execution of mandated
  commands is governed by (iii). **Scope, as a principle with a closed boundary (V24).** The seat may: **(i)** read any file inside its working directory; **(ii)** read
  the pinned environment — the interpreter `/usr/bin/python3` and the site-packages directory whose path and manifest digest the
  dispatch record fixes before launch and C5 prints live; **(iii)** execute the commands this document prints verbatim — the C1
  `census` runs, the C2/C3 `validate` runs, the five C5 harness commands, and the §9 wrapper invocations — together with whatever
  those commands themselves invoke or load, because executing a printed command is the instruction, not a scope choice. **Executing a printed command does not
  authorise arbitrary data access: every placeholder the seat resolves, every child command or `<command>` the seat supplies to the
  §9 wrapper, every import and every data path the seat selects is a seat CHOICE and is subject to (i)–(ii). Any path the seat
  CHOOSES to open that is not (i) or (ii) — including through a placeholder or a wrapped command — is an outside path and `FAIL`.** The printed path list records the seat's own opens; what a printed command loads is not the seat's choice and is not
  listed. Why the line is drawn here: what the seat is told to run cannot leak the study's content, because the packet's own text is
  reviewed and blinded before dispatch; what the seat decides to open can. **Residual, stated:** matching manifest digests establish matching snapshots of the pinned directory at pinning and at C5, not
  continuous immutability between them and not the absence of startup code; no inference about trusted content follows from the
  pin alone. What bounds such code is the confinement recorded in the dispatch record (the kernel profile and its printed probes),
  not this clause; C4 and C5b are self-report controls and do not themselves bound automatic code access.

`C4_SEAT_ISOLATION=PASS|FAIL|NOT_RUN`.
- **C5 — harness, LIVE.** Execute and print, in order: (1) `/usr/bin/python3 -E --version`; (2) `/usr/bin/python3 -E -c "import sympy;
  print(sympy.__version__)"`; (3) `/usr/bin/shasum -a 256 /usr/bin/python3`; (4) `/usr/bin/python3 -E -c "import site; print(site.getusersitepackages())"`;
  (5) `/usr/bin/python3 -E r3c2_manifest.py <the directory (4) printed>` — `r3c2_manifest.py` is committed beside this document, sha256 `6b6e4bce1136448b2cb223225a8710f493c469aef82a0379b3f47e066260019a`, delivered in the seat's working directory and pinned in `R3C2_SEAT_PACKET.sha256`; it is ONE process that walks
  the directory itself, reads every file, prints `FILES=<n>` and `MANIFEST_SHA256=<digest>`, and on any unreadable file prints
  `ERROR=<path>` and exits 1 — nothing is skipped silently. **Every mandated command in this document is one invocation whose
  exit status is the control's (the §9 wrapper counts as one invocation that prints its child's exit status); no mandated command is a shell pipeline, because a pipeline's exit status is its last stage's and
  an upstream failure can be masked.** The five commands establish the interpreter every ledger command runs under and the one
  site-packages directory it loads from, whose path and `MANIFEST_SHA256` the dispatch record pins before launch — the digest covers every regular file under that directory; the manifest command first rejects a root path that is a symlink or is not a directory, printing `ERROR=<path>` and exiting 1, then rejects every symlink or non-regular entry below that root, including a symlinked folder, never following or silently skipping them; importable content outside that tree is listed separately in the dispatch's pinned environment. **PASS requires
  all five commands to exit 0, their full stdout printed, the path of (4) and the `MANIFEST_SHA256` of (5) equal to the dispatch
  record's; a mismatch, a non-zero exit, an `ERROR=` line, missing output, or a transcribed value in place of live output is
  FAIL.** `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN`.
- **C5b — no cross-lane access.** Print every path opened, each marked `IN_SCOPE` or `OUT_OF_SCOPE`; **any
  `OUT_OF_SCOPE` row fails the control; PASS means the printed list contains no such row and makes no claim that the
  list is complete. **`IN_SCOPE` = C4's (i) and (ii), and every path opened by a printed command under C4's (iii); `OUT_OF_SCOPE` = any path the seat chose to open outside (i)–(ii), including through a placeholder or a wrapped `<command>`. The list records the seat's choices, not what printed commands load (C4).**** `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN`. 
- **C6 — audit, with a frozen sampling frame and an independent enumeration.** A third independent seat, on a different engine from both
  census seats, **first** enumerates and classifies candidate passages itself from EVERY pinned source — all 89 enumerable texts of
  `R3C2_CORPUS_MANIFEST.md`, a complete independent enumeration, never a sample of texts — under §1's rule, with no seat candidate,
  exclusion, input or outcome ledger in its dispatch inventory, and writes its own candidate and exclusion ledgers. The custodian runs
  `census` over them and, only on PASS, records their digests in a first-write stage-1 seal (`audit seal-enumeration`). **Second**, after
  receipt T and the supply of the external seed, the custodian computes the selection (`audit select`, which refuses without the stage-1
  seal) — every arithmetic-group claim plus `k = min(max(1, ceil(0.20 × N)), R)` of the remaining included claims, `N` being the sealed denominator and `R` the number of remaining claims (when `R` is zero the
  sample is empty), drawn by `random.Random(seed_int).sample(remaining_ids, k)` where
  `remaining_ids = sorted(set(included_ids) − set(arithmetic_group_ids))` and `seed_int = int(seed_hex, 16)`, the custodian's seed being
  64 lowercase hexadecimal characters — and hands the auditor claim identifiers with source file and line ONLY (`audit handout`); the auditor independently reconstructs each assigned claim's complete input records and dependency closure from the pinned sources, including cross-claim dependencies, recording status, value, source coordinates, origin evidence and `derived_from` for each input, and the custodian seals this reconstruction by digest (`audit seal-rederivation`) BEFORE any sealed ledger is released; before sealing, `audit seal-rederivation` validates the reconstruction schema — every input carries symbol, status, value, source coordinates, origin, origin evidence and `derived_from` (and `origin_search` when silent) — and refuses an incomplete one; `audit compare` requires every one of those fields, compares every field, every evidence coordinate and quotation, and every dependency edge against the sealed ledger, binds an auditor classification that matches a declared sealed alternative to that branch (§3), and reports a missing field, a missing input, a dependency the auditor did not itself reconstruct, or any unsupported difference as `MISMATCH`; it recomputes each input's chain of origins to its roots from the auditor's own graph and from the sealed ledger under the matching branch and prints the comparison. **Only then** are the sealed (merged) candidate, exclusion and
  input ledgers opened to the comparison (`audit compare`), which recomputes the selection from the sealed candidates and seed and fails
  on any disagreement, and writes and prints `C6_AUDIT.json` with (i) one completeness row per passage key (file, line, numeral) in the
  UNION of the sealed and the auditor's enumerations — both presences, both dispositions, both exclusion kinds, and a result: `MATCH`,
  `OMISSION`, or `AUDIT_INCLUSION_DISPUTED` — and (ii) `MATCH`/`MISMATCH` per audited claim (outcome; printed and reproduced values for
  arithmetic outcomes) and per re-classified input origin. **Omissions:** a sealed INCLUDED passage absent from the auditor's enumeration;
  a passage the auditor lists (included OR excluded) that the sealed ledgers omit — each is ledger incompleteness and files
  `CENSUS_AUDIT_FAILED`. **Disputes:** a passage both sides list but dispose differently, and a sealed EXCLUDED passage absent from the
  auditor's enumeration, are `AUDIT_INCLUSION_DISPUTED`, listed with both dispositions and counted; above 10% of the sealed included
  denominator the audit files `CENSUS_AUDIT_FAILED`; at or below it the count is reported. A sealed denominator of zero with any passage
  on either side fails. `C6_AUDIT_SAMPLE=PASS` only if the artefact exists and is printed, both seals match, the recomputed selection
  matches, no row is an omission, the dispute rate is at or below 10%, and no audited claim or origin is `MISMATCH`. **What PASS means:**
  the enumerated predicates held over the sealed files; it is bounded by the custodian's dispatch and release record (the seals fix
  WHAT was committed, the dispatch record — listed and access-proven like the seats' — fixes WHEN, relative to release) and by
  shared reader error; exposure before dispatch cannot be excluded — the same floor C4 states for the seats. Its enumeration reads the corpus
  under the same reading discipline as the census seats, batch for batch if the census is batched, including the same cross-batch
  source access for re-classifying imports.

  **The seed comes from outside this lane.** After the tally digests are receipted, **an external custodian
  outside this lane supplies a seed generated independently and unavailable to the lane before that receipt**, and it
  is recorded with the receipt. **If the seed is not supplied and recorded with the receipt, the audit does not run,
  `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named.** 
  

  An input on which the two classifications disagree is filed `ORIGIN_DISPUTED` and reported with both seats'
  classification and both quotations; it is **not** reconciled. Above 10% of included claims,
  `CENSUS_ORIGIN_DISPUTED`. Any outcome the audit cannot reproduce, or any ledger incompleteness, files
  `CENSUS_AUDIT_FAILED`.
  *(The audit artefact and its PASS predicate are stated in the opening of this control.)*
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
`fbb9bef7d6622a17b4dc2e856791e3166b60394c187286ea5581b2f39003f331`) as `/usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command>`, which enforces a 120.0-second wall-clock
deadline on the monotonic clock, prints the wrapper command, the child's stdout and stderr and its exit status, and on
the deadline prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome; unreached controls `NOT_RUN`. Two independent seats, each
a sequence of sessions under one packet (C1); the dispatch record carries one `ACCESS_SHA` per session, the ownership list, and the
verified availability of every pinned text in that session's directory. 



## 11. Scope

No tier, warrant token, standing or stamp moves. Published sources only; nothing from another lane.  


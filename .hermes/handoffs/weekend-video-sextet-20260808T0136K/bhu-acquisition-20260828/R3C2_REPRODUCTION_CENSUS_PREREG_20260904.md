# R3-C2 — REDESIGNED pre-registration: a reproduction census of the corpus's quantitative claims

**Tori, 2026-09-05. Version 16 (see §10; §10.10 for the V15 gate reconciliation). OPTION (c) ADOPTED — Duho's ruling "Q-R3C2 c", 2026-09-05 14:08 KST: one pass,
two tallies. NOT FROZEN and NOT RUN: C0 by two independent seats who must agree, then the two-seat gate, before any
freeze.** Originally ORDERED by Duho, "redesign r3c", 2026-09-04 21:30 KST. *(The header read "Version 1" through V9 while §10
listed every version — a scar found and fixed here.)*
**Supersedes `R3C_MAGNITUDE_CENSUS_PREREG_20260904.md`, which failed four gate rounds across two engines and is kept
unchanged as the record of the failed design.** No derivation has been run.

## 0. Why the old design failed, and what actually changes

R3C asked: *does any construction fix an observable magnitude?* — screening 51 rows against a **shape/magnitude
pattern this lane itself wrote**. Four gates, two engines, all `UNSOUND`, and the reason never went away: **the
screening criteria and the hypothesis had the same author.** Every repair tried to police that with quoting rules; the
fourth round found the rules pointing at two different sources at once.

**The redesign does not police the circularity. It removes it.**

The census no longer screens against the pattern. It asks a question **whose criterion predates the pattern and belongs
to nobody in this lane**:

> **Can the paper's printed number be reproduced from the paper's own stated inputs, without choosing anything?**

That is ordinary reproduction — what any referee does — and it is decidable without reference to any pattern. **No seat
in this study ever reads the pattern record.** Whether the tally then supports, weakens or breaks the pattern is
computed by Tori **after the tally is sealed**, as a separate and clearly-labelled step. The hypothesis cannot reach
the evidence.

Three consequences, each fixing a named gate defect:

- **The exclusion problem disappears.** Nothing is excluded for being "a shape". Every **included** claim gets a
  reproduction attempt; every **excluded** candidate is recorded in the exclusion ledger of §3 with its file, line and
  the excluded kind. There is no category judgement to smuggle the pattern into.
- **Condition 5 disappears.** "Not shared with ΛCDM" — undecidable, and the subject of two gate findings — is not part
  of reproduction. Whether a reproduced number also discriminates against ΛCDM is a **different question, explicitly
  out of scope** (§8).
- **The self-referential quoting rule disappears** with the category judgement it served.

## 1. The question, exactly

For every quantitative claim in the corpus, **two questions from one pass: (i) does the paper's own number follow
from the paper's own recipe applied to the inputs it states; and (ii) what does that
number rest on — derived, standard or measured inputs only, or a chosen, fitted, imported or undeclared one?** The first is the
reproduction verdict; the second is the ledger's `rests_on` field. **The reproduction verdict and the provenance fields are recorded separately.**

**Operational definition, so the enumeration is not a judgement:** a *quantitative claim* is a passage in a pinned
source that **prints a numeral the paper asserts as a result of its own** — with units, or dimensionless and stated
as a value. Excluded, by definition and not by taste: numerals that are equation numbers, reference numbers, page or
line numbers, dates, or values the paper attributes to another work without deriving. **Every candidate passage is
listed with file and line; inclusion and exclusion are both recorded.**
**Inclusion is assigned independently by the two independent seats from the §1 rule alone; disagreement on any
candidate that survives two reconciliation attempts stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4): the
disputed candidates are listed and the complete candidate and exclusion ledgers are reported with the dispute.** <!--SEAT-REDACT-->*(codex: the audit trail records the boundary but does not make it
mechanical — whether a numeral is "the paper's own result" remains a judgement, so it moves from one reader to two
who must agree.)*<!--/SEAT-REDACT-->

<!--SEAT-REDACT-->**Checked, because moving work into blind seats can move the pattern with it:** the §1 rule those seats apply is
*"a passage printing a numeral the paper asserts as a result of its own"*, with the excluded kinds enumerated —
equation numbers, reference numbers, page or line numbers, dates, attributed-not-derived. **Nothing in that rule
mentions magnitudes, shapes, comparison models or any lane conclusion**, and the seats receive the built packet,
whose redaction is machine-asserted against a forbidden list. **This repair therefore adds readers without adding
pattern content to what they are told.**<!--/SEAT-REDACT-->

## 2. Method — per claim, in order

**The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` (sha256 `300d4da144d96ae9f1390c9018e919ae1ba6cf00be9f45ad36fdccfdcfbf9b24`) lists every enumerable text by
digest and byte count; a seat enumerates claims from those files and no other. Files listed there as RAW are not enumerable
and are outside the census, visibly.** <!--SEAT-REDACT-->*(V11: no version before this one pinned the corpus at all — codex V10.)*<!--/SEAT-REDACT-->

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
   i.e. every ledger record with status `PRINTED` or `STANDARD`.** Provenance is recorded under C3 (`origin`,
   `derived_from`, `root_origins`).
5. **Record the outcome**, per claim, as one of §3, **and let the script record the claim's `rests_on`** from the ledger.

**A value the paper does not print but traces to a named source that is itself an enumerable text in `R3C2_CORPUS_MANIFEST.md` is
classified `PRINTED` from that source, with `origin` `IMPORTED`, `origin_evidence` `ORIG_CITATION` cited to the named
source's file and line, and the value machine-matched there — **only when such a match exists; a cited value that does
not machine-match at the named source's cited line, or whose named source is not an enumerable text of the manifest,
files `REPRO_BLOCKED` under §3.** **A seat may not supply a value for an `ABSENT` or `BLOCKED` input.**
Encountering one ends that claim's attempt.

## 3. Per-claim outcomes — declared now


**One pass, two tallies.** The reproduction verdict answers *"does the paper's arithmetic work from what it states?"*
The ledger answers *"what did it rest on?"* So:

> **THE INPUTS THE ARITHMETIC MAY CONSUME** = every ledger record with status `PRINTED` (given in the paper, whatever
> its `origin`) or `STANDARD` (on C3's closed list). **Arithmetic consumes records according to status `PRINTED` or `STANDARD`.** Each record's `origin`
> is cited under C3, independently by both seats; `root_origins` and the per-claim summary field **`rests_on`** are
> computed from the ledger by the pinned script `r3c2_ledger_tools.py` (sha256 `bb5f1fc578fa79f09880a609f71b4ae81eec2f8bfd9fae9ec661d4996af9efd4`), with the full
> root-origin set printed beside it. **No seat writes `root_origins` or `rests_on`; the script rejects a ledger that
> arrives with either set.**
<!--SEAT-REDACT-->
> *(Master only — the rule the script implements: `DERIVED_ONLY` when every root origin is `DERIVED`, `STANDARD` or
> `MEASURED`; otherwise the most severe root origin present, in the fixed order `USES_UNDECLARED` > `USES_IMPORTED` >
> `USES_FITTED` > `USES_CHOSEN`. A claim with a disputed root carries the pair computed under both classifications and
> is marked `DISPUTED`. The interpretation step reads `rests_on` and the reproduction tally as two facts (§7). V11:
> kimi V10 read the severity order and the "interpretation reads rests_on" sentence from the packet and reconstructed
> the channel the conclusion rides on; both now live here, not in the seat's copy — the seat records provenance and
> never computes or weighs the field.)*
<!--/SEAT-REDACT-->

- **`REPRO_EXACT`** — the paper's number follows, within its own stated precision, **from the paper's own recipe
  applied to the inputs it states** (`PRINTED` or `STANDARD`). **Report both numbers.** **Where the paper states no
  precision for the claim, the printed precision is the claim's stated precision: the reproduced value must round to
  the printed numeral at that precision.** The claim's `rests_on` is reported beside it. <!--SEAT-REDACT-->*(kimi V10:
  "13.8 Gyr" against 13.797 was fileable either way; the rule decides it mechanically. codex V10 asked for the name
  to change to `REPRO_WITHIN_STATED_PRECISION`; a class rename is the principal's, escalated in §10.5.)*<!--/SEAT-REDACT-->
<!--SEAT-REDACT-->- *(`REPRO_AFTER_CHOICE` — RETIRED at V10 by the principal's ruling adopting option (c). What it recorded — that the number
  rests on a chosen, fitted, imported or undeclared input — is now the `rests_on` field of a `REPRO_EXACT` or
  `REPRO_FAILED` claim, computed by script. Two blind C0 seats had found the class unreachable under the derivation-only
  wording (§10.3); it is retired, not repaired.)*<!--/SEAT-REDACT-->
- **`REPRO_FAILED`** — the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the
  paper's number. Report both numbers. **Wording: "unreproduced from the stated inputs," not "error."** `rests_on`
  is reported beside it.
- **`REPRO_BLOCKED`** — an input whose value the claiming paper does not print, and for which the claiming paper
  **names a source (a citation)** that either **is not an enumerable text pinned in `R3C2_CORPUS_MANIFEST.md`** or **is
  an enumerable pinned text at whose cited line the value does not machine-match**; in the first case whether that
  source is obtainable elsewhere is irrelevant, because the census may not open or consume it. Name the input and the
  source. It is recorded with status `BLOCKED` (C3) and never consumed. *(Distinct from `REPRO_INPUT_ABSENT`, which is an input the paper neither prints nor traces to any named
  source; a value cited from a pinned enumerable text is `PRINTED` there under §2.)* <!--SEAT-REDACT-->*(kimi V10:
  as written every unobtainable input was first `ABSENT` and the precedence filed it `REPRO_INPUT_ABSENT`, so this
  class's exclusive domain was empty. The named-source test separates them; the precedence below puts BLOCKED first.)*<!--/SEAT-REDACT-->
- **`REPRO_NOT_EVALUABLE`** — the arithmetic could not be completed within the 120-second cap, or requires machinery
  this lane does not have. Print `SYMBOLIC_TIMEOUT` when the 120-second cap is exceeded, or `MACHINERY_UNAVAILABLE` when the lane lacks the
  machinery, and the point reached. <!--SEAT-REDACT-->*(Added because the stall guard had no
  per-claim outcome to file into.)*<!--/SEAT-REDACT-->
- **`REPRO_NO_DERIVATION_STATED`** — the paper prints the claim as its own result but **states no equation or
  computational procedure that could produce it**, so there is nothing to attempt. Name the passage. <!--SEAT-REDACT-->*(A claim can
  satisfy §1 — a printed numeral asserted as the paper's own result — while the paper never says how it was
  obtained. That claim previously fell through every class.)*<!--/SEAT-REDACT-->
- **`REPRO_INPUT_ABSENT`** — an input the equation needs is `ABSENT` from the paper — **neither printed nor traced to
  any named source** — so the attempt stops there. **Name the input.** <!--SEAT-REDACT-->*(This class exists because the rule "a seat may not supply a value for an ABSENT input" had no
  outcome to file — a gate finding.)*<!--/SEAT-REDACT--> Distinct from a claim whose inputs the paper DOES state, chosen or not — that
  claim is attempted and files `REPRO_EXACT` or `REPRO_FAILED` with its `rests_on`.
**Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the first in this
order:** `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the
**arithmetic group**. <!--SEAT-REDACT-->*(Precedence is stated because these conditions genuinely co-occur — an absent input whose
source is also unobtainable satisfied two classes with no rule to choose between them.)*<!--/SEAT-REDACT-->

**The arithmetic group** is the set of outcomes that state whether the arithmetic reproduced the number: **exactly
`REPRO_EXACT` and `REPRO_FAILED`**. **`rests_on` is computed and reported for every included claim that has at least one
ledger record, whatever its outcome; a claim with no ledger record carries `rests_on` `NOT_COMPUTED`, and the `rests_on`
tally reports a `NOT_COMPUTED` row.**

**Candidate exclusions are not per-claim outcomes.** Every enumerated candidate passage that fails the §1
definition is recorded in a **separate exclusion ledger** with file, line, the numeral, and which excluded kind it
is (equation number, reference number, page/line number, date, or attributed-not-derived). **The exclusion ledger's
`kind` is one of `EQUATION_NUMBER`, `REFERENCE_NUMBER`, `PAGE_OR_LINE_NUMBER`, `DATE`, `ATTRIBUTED_NOT_DERIVED`.** The census denominator
is the count of **included** claims; the exclusion ledger is reported alongside it and audited under C6, so nothing
is hidden by being excluded. <!--SEAT-REDACT-->*(The old `NOT_ATTEMPTED` class was incoherent: §1 defines a claim by the presence of
a printed number, so an included claim could never satisfy it — a gate finding.)*<!--/SEAT-REDACT-->

## 4. Study-level outcomes

1. **`CENSUS_COMPLETE`** — **every included claim carries exactly one outcome from the arithmetic group of §3.**
   Report the full tally with its denominator, **and the `rests_on` tally beside it — two tallies from one pass.**
2. **`CENSUS_PARTIAL`** — after the §2 attempt (one repeat permitted, meaningful only for `REPRO_NOT_EVALUABLE`),
   **at least one included claim carries a non-arithmetic outcome**
   (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`). Report each and
   why. **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.** <!--SEAT-REDACT-->*(Previously "some claims unresolved"
   was undefined, and a blocked claim satisfied both classes.)*<!--/SEAT-REDACT-->
3. **`CENSUS_AUDIT_FAILED`** — the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, **or the receipt verification
   of the seal fails**. No tally is filed; report which.
4. **`R3C2_NO_CLASS`** — a control among C0 through C5b fails **in every seat that attempted it** after two attempts;
   a packet or seat-isolation failure before dispatch files this class. **A C6 audit failure or a
   seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class.**
5. **`CENSUS_DENOMINATOR_DISPUTED`** — the two enumerations disagree after two reconciliation attempts, **or the two
   seats' input lists for the agreed claims disagree after the one C3 reconciliation**. The census does not proceed; the
   disputed candidates or inputs are listed. <!--SEAT-REDACT-->*(Added because the enumeration stop had no class.)*<!--/SEAT-REDACT-->
6. **`CENSUS_ORIGIN_DISPUTED`** — the two seats' independent `origin` classifications disagree on inputs affecting
   **more than 10% of included claims**. The census does not proceed; every disputed input is listed with both
   seats' classification and both quotations. <!--SEAT-REDACT-->*(Disagreement about provenance is reported, never reconciled — if
   two blind readers cannot agree from the paper's own text what a number's provenance is, that is a finding about
   the corpus, and reconciling it would destroy it.)*<!--/SEAT-REDACT-->
7. **`CENSUS_CONTROL_SPLIT`** — a control fails in one seat and passes in another after two attempts. Report both
   seats' outputs and stop; **do not adopt the passing seat's result.** <!--SEAT-REDACT-->*(Added because this reachable state landed in
   no class.)*<!--/SEAT-REDACT--> <!--SEAT-REDACT-->*(Phrased this way
   because the old `R3C_NO_CLASS` said "in both seats", leaving a control that failed twice in one seat and passed in
   the other with no class — a gap codex found.)*<!--/SEAT-REDACT-->

**Exactly one study-level outcome is filed. Where more than one condition holds, file the first in this order:**
`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`,
`CENSUS_PARTIAL`, `CENSUS_COMPLETE`. **Once a stop class applies, later limbs are unreached and their controls are
`NOT_RUN`.** <!--SEAT-REDACT-->*(Both V10 seats: §3 had a total precedence and §4 did not, so a tally satisfying two
classes had no rule. The order is chronological — controls run before enumeration, enumeration before origin, origin
before audit — which is codex's order; kimi's differed only in placing the denominator dispute first.)*<!--/SEAT-REDACT-->

<!--SEAT-REDACT-->
**No study-level outcome is a verdict about the pattern.** §7 is where the pattern is touched, once, afterwards.
<!--/SEAT-REDACT-->


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

  <!--SEAT-REDACT-->*(Added by Duho's order after the R3D diagnosis. In R3D, three consecutive repairs left the one condition capable
  of refuting this lane's pattern unable to return PASS on any path, each time in a different way, and **no other
  control could see it**: every other control checks that something is done correctly, none checks that an outcome
  **can happen at all**. **This census's §3 and §4 outcomes have never been reachability-tested**, and at least one
  is worth checking early — `CENSUS_COMPLETE` requires every included claim to carry an arithmetic-group outcome,
  which a single blocked or absent input in the whole corpus is enough to prevent. C0 does not touch, and does not
  depend on, the definition held in §3: it asks only whether each declared outcome can occur under whatever
  definition is settled.)*<!--/SEAT-REDACT-->

- **C1 — denominator.** Claims **included**, claims **excluded** (with the exclusion ledger of §3), and attempts made,
  all printed before any tally. <!--SEAT-REDACT-->*(This control previously referenced a class §3 abolished — a gate finding; the
  document has been swept for every other occurrence.)*<!--/SEAT-REDACT-->
  **The candidate file is a JSON object `{declared_candidate_count, declared_included_count, declared_excluded_count,
  candidates: [...]}` and the exclusion file is `{declared_exclusion_count, exclusions: [...]}`. Before the tally, print
  those four declared counts verbatim from the files, then run
  `/usr/bin/python3 r3c2_ledger_tools.py census <candidates.json> <exclusions.json>`: PASS requires exit 0 after the
  script verifies that every candidate has exactly one disposition, that every exclusion names one excluded candidate,
  and that each declared count equals the count recomputed from the rows; its stdout prints both the declared and the
  recomputed counts. Print its command, stdout and exit status.** The candidate and exclusion ledgers use the script's candidate schema: each candidate carries
  `candidate_id`, `source_file`, `source_line`, `numeral`, `included`; every exclusion row names a candidate and a `kind`;
  the script's failure lines name any missing field. `C1_DENOMINATOR_PRINTED=PASS|FAIL|NOT_RUN`, PASS only on exit 0.
- **C2 — input ledger.** Every input classified `PRINTED` / `STANDARD` / `ABSENT` / `BLOCKED`, each `PRINTED` one carrying file and
  line, in the JSON schema of C3, validated by `/usr/bin/python3 r3c2_ledger_tools.py validate <ledger.json> .` run from the printed seat working
  directory (`.` is the sole allowed `sources_dir`); before execution the seat prints the fully resolved command with
  every angle-bracket placeholder replaced by the actual in-scope path
  (exit 0 = PASS; every failure printed). `C2_INPUT_LEDGER=PASS|FAIL|NOT_RUN`.
- **C3 — no substitution, machine-checked.** The input ledger is a **JSON file**, one record per input:
  `{claim_id, input_id, symbol, status: PRINTED|STANDARD|ABSENT|BLOCKED, origin: DERIVED|STANDARD|MEASURED|CHOSEN|FITTED|IMPORTED|UNDECLARED,
  origin_evidence: {reason_code, source_file, source_line, verbatim}, origin_search: {query, files, matches} (required
  when reason_code is ORIG_SILENT), derived_from: [input_id…], value, source_file, source_line}`. **The seat-authored
  ledger MUST omit `root_origins`, `rests_on`, `origin_alt` and `origin_evidence_alt`; `validate` fails a ledger that
  carries any of them. The script adds `root_origins` and per-claim `rests_on` on `compute`; the merge step adds
  `origin_alt` and `origin_evidence_alt`. An input that files `REPRO_BLOCKED` under §3 is recorded with status `BLOCKED`,
  `origin` `IMPORTED`, `ORIG_CITATION` evidence cited to the claiming paper's naming sentence, and no value; the arithmetic
  never consumes it.** <!--SEAT-REDACT-->*(`STANDARD` was missing from the `origin` enumeration while §3 defined
  admissibility partly by it, so a measured-constant record could not be validly filled in.)*<!--/SEAT-REDACT-->

  **`origin` must be cited, not asserted.** Every record carries `origin_evidence` with a reason code —
  `ORIG_EQUATION`→`DERIVED`, `ORIG_CONSTANT`→`STANDARD`, `ORIG_MEASURED`→`MEASURED` (a quantity the paper reports as
  its own measurement, with the measurement described), `ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_FIT_STATED`→`FITTED`,
  `ORIG_CITATION`→`IMPORTED`, `ORIG_SILENT`→`UNDECLARED` — and, except for `ORIG_SILENT`, a **verbatim quotation
  machine-matched to the cited line**. **Every input's `origin` is classified independently by both seats.** **Where
  more than one reason code matches the cited sentence, file the first in this order: `ORIG_CITATION`,
  `ORIG_FIT_STATED`, `ORIG_CHOICE_STATED`, `ORIG_MEASURED`, `ORIG_EQUATION`, `ORIG_CONSTANT`, `ORIG_SILENT` — a sentence
  that names an external source for the value is a citation whatever else it says.** <!--SEAT-REDACT-->*(kimi V10's
  attack: "We adopt H₀ = 67.4 from Planck (2018)" filed CHOSEN passed every machine check and reported a less severe
  root; the code precedence makes the citation win. A reason code that matches its quotation but misapplies the
  precedence is caught only by the second seat's independent classification and the C6 re-classification, never by the
  machine; if every reader misclassifies identically, the record stands — that floor is stated here rather than implied
  away. `MEASURED` added because a measured-but-silent input was forced to
  `UNDECLARED`, the most severe root, by construction — kimi's observation 2.)*<!--/SEAT-REDACT--> **`UNDECLARED` is the default, not the residue**: a record leaves it only by
  producing that text, and an `ORIG_SILENT` record prints the search the seat ran.

  **Provenance is transitive, and the transitivity is computed.** Every `DERIVED` record lists its `derived_from`
  ids; **a script computes `root_origins`, the origins at the leaves of that chain, and no seat writes that field.**
  A chain's root origins are computed from every step, never from its last step alone. **The script is `r3c2_ledger_tools.py`,
  committed beside this document, sha256 `bb5f1fc578fa79f09880a609f71b4ae81eec2f8bfd9fae9ec661d4996af9efd4`; the seat runs
  `/usr/bin/python3 r3c2_ledger_tools.py compute <ledger.json> <out.json>` and prints its stdout and exit status. It
  computes each claim's `rests_on` from its `root_origins` and prints the root-origin set beside it; it REJECTS (exit 2) a
  ledger that arrives with `root_origins` or `rests_on` already set; it FAILS (exit 1) on a `derived_from` id that names
  no record, on a cycle, and on a `DERIVED` record with no `derived_from`, so an empty root set cannot occur; the two seats'
  independently validated ledgers are merged by `/usr/bin/python3 r3c2_ledger_tools.py merge <ledger_seatA.json>
  <ledger_seatB.json> <merged.json>` (exit 1 if their `input_id` sets differ — **if `merge` exits 1, the two seats reconcile their input lists against the
  paper's stated equation once; an input-set difference surviving that reconciliation stops the study under
  `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations**); where the two `origin` classifications
  differ the merged record carries `origin_alt` and `origin_evidence_alt`, `compute` reads the merged ledger, and the
  claim's `rests_on` is computed under both and marked `DISPUTED`.** A `rests_on` value present in the seat-authored input ledger fails this control; after a successful `compute` run,
  a `rests_on` value absent from the script-produced output ledger fails this control. **The arithmetic may consume only records with status `PRINTED` or `STANDARD`.** A
  script asserts that no `ABSENT` or `BLOCKED` record carries a value, that **each `PRINTED` value machine-matches the
  text at its cited source line and each verbatim quotation is a substring of that line**, and that **each `STANDARD`
  value is one of a closed list PRINTED LITERALLY BELOW** — so "standard" cannot become a selectable family;
  **completeness of a claim's input list against the paper's equation is seat-authored and audited under C6, not
  machine-checked**:

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
  `STANDARD`**, whatever its provenance. <!--SEAT-REDACT-->*(The list was previously "fixed here" by naming four symbols and citing a
  paper whose baseline runs to dozens of base, derived and nuisance parameters across several tables, none printed
  — so a machine membership test was impossible and "standard" was in practice a selectable family. kimi found it.)*<!--/SEAT-REDACT-->
  `C3_NO_SUBSTITUTION=PASS|FAIL|NOT_RUN`.
- <!--SEAT-REDACT-->**C4 — pattern blindness, and an honest statement of its limit.** The referee wrapper's `--add-dir` **grants**
  directories; it does not restrict them, and it necessarily grants the lane directory, **which contains the pattern
  record**. So the tooling as it stands cannot enforce blindness to a lane-resident file, and a seat's own
  declaration is self-report.

<!--/SEAT-REDACT-->
  **C4 — what the seat must do.** Work **only** from the files in your working directory. **Print every path you
  open**, and print the working directory itself. Do not construct a path outside it; if you believe you need one,
  stop and report that instead of opening it. `C4_SEAT_ISOLATION=PASS` requires that printed path list and means only that the list contains no outside path; it
  makes no claim that the list is complete. Any path outside the working directory is `FAIL`.

<!--SEAT-REDACT-->
  **What is therefore done:** each seat is run from a **redacted copy directory outside the lane**, containing the
  **seat packet** — not this document — the seat brief `r3c2_seat_packet/SEAT_BRIEF.md` (committed beside the packet,
  asserted against the same forbidden list by the builder, and pinned in `R3C2_SEAT_PACKET.sha256`), the script
  `r3c2_ledger_tools.py`, and the pinned sources of `R3C2_CORPUS_MANIFEST.md`, with the wrapper pointed at that directory and **not** at the lane. **The
  lane owner lists that directory's contents and their digests in the dispatch record before launch; a copy missing any
  of them is not dispatched.** **This is procedural, not enforced by the filesystem**: nothing here denies a seat an
  absolute path into the lane, so the seat's printed path list is the detection, and `C4_SEAT_ISOLATION` is a
  self-reported control with a structural aid, and is labelled so.

  **The seat packet is built mechanically, by `r3c2_build_seat_packet.py`, and its redaction is asserted.** The
  builder drops §0, §7, §8 and §10 whole, strips every span marked `SEAT-REDACT` in this document, and then
  **asserts that no string on the forbidden list survives anywhere in the output — the list blocks the enumerated
  strings and does not establish that every consequence-bearing word is gone; procedural consequences of stop outcomes
  remain visible while hypothesis mappings, comparison-model preferences and empirical stakes are removed** — the pattern's name and topic,
  the comparison model, gate history, and the names of the people in the custody chain. **If any survives, the
  packet is not written and `C4_PACKET_REDACTED=FAIL`**; the study does not proceed on a hand-checked copy. **The
  forbidden list names the pattern's name and topic, the comparison model, gate history, every engine name, every
  person in the custody chain (the lane owner's name included), and every word that signals consequence rather than
  content — expectation, refute, consequential, invisible, favourable, unfavourable, stake, prior, tempting, warn. Build
  command, run from this directory: `/usr/bin/python3 r3c2_build_seat_packet.py`; expected first line of output
  `C4_PACKET_REDACTED=PASS`, then the master and packet digests.**
  Redaction is done in the builder and marked in this document, so the master is never edited to serve the blind
  and a reader can see exactly what the seat was not given.

  **Where the packet lives, and how it is pinned.** The built packet is `r3c2_seat_packet/R3C2_SEAT_PACKET.md`, a
  **committed path, not scratch** — a clause cannot cite an artefact that lives in a temp directory. **Its digest is
  recorded in `R3C2_SEAT_PACKET.sha256`, not in this document, and that is deliberate**: the packet header embeds
  this document's own hash, so printing the packet's hash here would make each change to either file invalidate the
  other. The pin file breaks that circularity. **The seats are given exactly the file whose digest that pin records**,
  and Tori re-runs the builder and re-checks the pin before any dispatch; a packet whose digest does not match its
  pin is not dispatched. *(The first run of this assertion caught fourteen
  surviving disclosures in a packet that had been assembled by hand, including the version table — which narrates
  every gate objection — and §0, which states the pattern's topic outright. That is the argument for asserting it
  rather than checking it.)* `C4_PACKET_REDACTED=PASS|FAIL|NOT_RUN`. The seat's declaration and printed path list are kept as
  secondary detection.

  **What the blind proves and does not:** it proves the seat was not given the pattern record and did not read it
  from its working directory. **It cannot prove a seat has no prior exposure from training or an earlier session** —
  nothing available here can. The record states that limit rather than implying a stronger blind.
  
<!--/SEAT-REDACT-->`C4_SEAT_ISOLATION=PASS|FAIL|NOT_RUN`.
- **C5 — harness, LIVE.** Execute and print `/usr/bin/python3 --version`,
  `/usr/bin/python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 /usr/bin/python3` — the interpreter
  every ledger command runs under. **PASS requires all three commands to exit 0 and their full stdout to be printed; any
  non-zero exit, missing output, or a transcribed value in place of live output is FAIL.** `C5_HARNESS_PINNED=PASS|FAIL|NOT_RUN`.
- **C5b — no cross-lane access.** Print every path opened, each marked `IN_SCOPE` or `OUT_OF_SCOPE`; **any
  `OUT_OF_SCOPE` row fails the control; PASS means the printed list contains no such row and makes no claim that the
  list is complete.** `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN`. <!--SEAT-REDACT-->*("As R3A/R3B" named no command and no code, and
  a seat that never saw those studies cannot resolve it — the defect codex found in R3D's C5/C5b.)*<!--/SEAT-REDACT-->
- **C6 — audit, with a frozen sampling frame.** A third independent seat **first audits the full candidate and
  exclusion ledgers against every pinned source** — completeness, not just outcomes — then re-derives, **without sight of earlier work and re-classifying every input's `origin` from the pinned sources, and recomputing `rests_on` by the pinned script**: **(i) every claim in the arithmetic
  group** — no sampling discount — and **(ii) a sample of `min(max(1, ceil(0.20 × N)), R)` of the remaining included
  claims**, `N` being the sealed denominator and `R` the number of remaining claims (when `R` is zero the sample is empty
  and every included claim is already audited under (i)), drawn by `random.Random(seed_int).sample(remaining_ids, k)`
  where **`remaining_ids = sorted(set(included_ids) − set(arithmetic_group_ids))` and `seed_int = int(seed_hex, 16)`,
  the custodian's seed being 64 lowercase hexadecimal characters**.

  **The seed comes from outside this lane.** After the tally digests are receipted<!--SEAT-REDACT--> (§7)<!--/SEAT-REDACT-->, **an external custodian
  outside this lane supplies a seed generated independently and unavailable to the lane before that receipt**, and it
  is recorded with the receipt. **If the seed is not supplied and recorded with the receipt, the audit does not run,
  `C6_AUDIT_SAMPLE=NOT_RUN`, and the study files `CENSUS_AUDIT_FAILED` with the missing seed named.** <!--SEAT-REDACT-->*(The custodian is Blanc, who is outside this lane and reports to
  Duho; §7 states the receipt.)*<!--/SEAT-REDACT-->
  <!--SEAT-REDACT-->*(Seeding from the tally's own digest let the tally's producer reshape non-semantic content — ordering, spacing,
  metadata — until a favourable sample appeared. A seed must not be a function of the thing being audited.)*<!--/SEAT-REDACT-->

  An input on which the two classifications disagree is filed `ORIGIN_DISPUTED` and reported with both seats'
  classification and both quotations; it is **not** reconciled. Above 10% of included claims,
  `CENSUS_ORIGIN_DISPUTED`. Any outcome the audit cannot reproduce, or any ledger incompleteness, files
  `CENSUS_AUDIT_FAILED`. **A claim whose root-origin set contains an `ORIGIN_DISPUTED` input carries `rests_on` computed
  under both classifications, printed as a pair and marked `DISPUTED`; the `rests_on` tally reports a `DISPUTED` row.**
  **Classes are cited by name, never by number**. `C6_AUDIT_SAMPLE=PASS|FAIL|NOT_RUN`.

Controls in an unreached limb are `NOT_RUN`, never passes.

## 6. Limb structure

**Limb A (~1 seat-day):** enumerate every quantitative claim and produce the input ledger. **No arithmetic.** If the
two enumerations disagree on any candidate's inclusion after two reconciliation attempts — **tolerance zero,
measured in candidate passages** — stop with `CENSUS_DENOMINATOR_DISPUTED` (§4). <!--SEAT-REDACT-->*(This sentence previously
survived here after being repaired in §2: the second live copy of a repaired rule is how the last defect got in,
so §6 now names the class rather than restating the rule.)*<!--/SEAT-REDACT-->
**Limb B (2–3 seat-days):** the reproduction attempts, then the audit.

## 7. What happens after the tally — deliberately NOT specified here

**This preregistration says nothing about what any tally would mean for any hypothesis, and no seat is told.**
**What the interpretation step READS is stated, because it is a fact about this design and not about any hypothesis:
it reads the ledger's `rests_on` tally and the reproduction tally as two separate facts; the reproduction verdict
alone is never the interpretive input (option (c)).** The
gate's finding was that stating the mapping in the document the seats read hands them the stake of each outcome.
The interpretation step lives in `R3C2_INTERPRETATION_PROTOCOL_20260904.md`, which **no seat may open** and which is
itself fixed and committed before limb A begins, so it cannot be written to suit the tally.

**What the seal is, and what it is not — two receipts.** **(P) Before limb A begins, Tori commits the interpretation
protocol and sends its hash and commit id to Blanc, who is outside this lane and reports to Duho; Blanc acknowledges
and timestamps them in a preserved receipt P; limb A does not begin without receipt P.** **(T) After the tally is
committed and before the protocol is opened, Tori sends the tally hash and tally commit id; Blanc receipts them as T;
the interpretation protocol is not opened without both receipts.** **The relay is complete only when it is receipted.**
After opening, Blanc independently re-hashes the tally and the protocol and verifies all four values against the two
receipts, and **the interpretation report must print both receipts and the four verified values**. Any missing receipt
or mismatch files `CENSUS_AUDIT_FAILED` (§4, whose definition now names this case), leaves the interpretation
`NOT_RUN` and voids the comparison. *(V11: both V10 seats found the single post-tally relay left the protocol in the
lane's own custody while the tally was computed — the exact overclaim §10.2 recorded as repaired at V8 and the operative
text did not contain.)* *(A send with no recorded receipt is an
assertion of custody, not custody: a replacement could be used silently even though Blanc once received other
strings.)*

That relay is the custody step; the git commit alone is not, because **a local commit
in Tori's own custody can be amended or reset, so it is tamper evidence, not an external custodian** — the same
objection already on this lane's record about hash chains.

**Stated plainly, without overclaiming:** this proves the tally and the protocol both existed, in the stated form,
before the comparison was filed. **It does not prove Tori had not already guessed the answer** — nothing available
here could prove that. It bounds the record, not the mind, and the record should say so rather than imply more.

## 8. Explicitly out of scope

Whether a reproduced number **discriminates** against ΛCDM or any other model. That was the undecidable condition 5 of
the failed design; it is a different question and is not asked here.

## 9. Inherited discipline

Live harness (C5); `ACCESS_SHA` proof for any pinned source audited, verified by the lane owner after the run and not
on the seat's claim; path lists (C5b); every symbolic operation launched through the committed wrapper `r3c2_timeout.py` (sha256
`fbb9bef7d6622a17b4dc2e856791e3166b60394c187286ea5581b2f39003f331`) as `/usr/bin/python3 r3c2_timeout.py 120.0 -- <command>`, which enforces a 120.0-second wall-clock
deadline on the monotonic clock, prints the wrapper command, the child's stdout and stderr and its exit status, and on
the deadline prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome; unreached controls `NOT_RUN`. Two independent seats. <!--SEAT-REDACT-->On a split, a third seat is dispatched by the lane owner via
`/Users/duhokim/HermesOps/scripts/nm_referee_dispatch.sh` (absolute path; it exists there, not in this directory) with
its `ACCESS_SHA` proof. Lane-side procedure, not the seat's: the no-fallback control is the provider log showing
no fallback line for the seat's session, checked by the lane owner; a one-page check sheet `R3C2_CHECK_SHEET_<date>.md`
in plain words with source lines is written by the lane owner after the tally; the lane owner re-runs every script; a
critic note precedes any ruling.<!--/SEAT-REDACT-->

<!--SEAT-REDACT-->**Amendments get a new version number and hash in §10 rather than an in-place rewrite** — the discipline failure that
made a valid access proof look unbound during R3C's gate rounds.<!--/SEAT-REDACT-->

## 10. Version history and gate record

**Re-verified 2026-09-04 22:06 KST against the files on disk (Blanc 22:02, item 3).** The `sha256` column is
**the hash the referee seat itself computed at dispatch**, taken from the `ACCESS_SHA=` line of that seat's own
report — not from my recollection and not from a pin file I wrote. Every row is checkable by running
`shasum -a 256` on the report named beside it.

Two defects were found in the previous table and are corrected here, rather than being silently overwritten:

1. **Rows V3, V4 and V5 had been appended below §11**, outside the table, so the rendered version history showed
   only V1 and V2, and the completion token was duplicated four times. Nine gate rounds is more history than a
   hand-maintained table survives; that is why this section is now checkable against the reports.
2. **The V4 row carried `040762ad…3666e3`, which is not a hash any seat gated.** Both V4 seats computed
   `0ba8df02…dd051f`. `040762ad…` was an intermediate state of the file that was never dispatched. The column is
   headed "at dispatch", so the gated hash is the correct entry and the wrong one is named here rather than erased.

| version | sha256 at dispatch | gate(s) run against exactly this hash | verdict(s) | change |
|---|---|---|---|---|
| V1 | `977cc127d7bc161d…` | `R3C2_GATE_codex_20260904.md` | `PREREG_UNSOUND` | redesign; supersedes `R3C_MAGNITUDE_CENSUS_PREREG_20260904.md` |
| V2 | `bf404b621679263f…` | `R3C2_GATE_V2_codex_20260904.md` | `PREREG_UNSOUND` | seven findings: interpretation excised to a seat-invisible protocol; quantitative claim defined operationally; `REPRO_INPUT_ABSENT` added; `NOT_ATTEMPTED` cannot move the denominator; enumeration tolerance zero; C3 given a JSON ledger; C4 made structural; seal custodied in git |
| V3 | `c945c22e110bf030…` | `R3C2_GATE_V3_codex_20260904.md`, `R3C2_GATE_V3_kimi_20260904.md` | `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS` | six findings: exclusions moved out of per-claim outcomes; `CENSUS_DENOMINATOR_DISPUTED` added; C4 rebuilt as fresh seat + allowlist; C3 ledger given `origin`, machine-matched `PRINTED` values, closed `STANDARD` list; C6 given a frozen seed and minimum sample; seal re-stated honestly |
| V4 | `0ba8df028686f10c…` | `R3C2_GATE_V4_codex_20260904.md`, `R3C2_GATE_V4_kimi_20260904.md` | `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS` | provenance replaces location as the admissible-input test; abolished class swept document-wide; `REPRO_NOT_EVALUABLE` and `CENSUS_CONTROL_SPLIT` added; `REPRO_BLOCKED`/`REPRO_INPUT_ABSENT` disambiguated; C4 rebuilt as a redacted out-of-lane copy |
| V5 | `50e7733c114bbf29…` | *(none — not dispatched)* | — | non-definitional only: second live copy of the enumeration rule removed from §6; study-level classes renumbered 1–6 |
| V5.1 | `9ad3a313b2e8bd4b…` | *(none — not dispatched)* | — | **HELD** marker added to the core definition so a referee does not report a deliberately open question as a fresh finding |
| V6 | `d1d6c5ad2e5d7985…` | *(none — not dispatched)* | — | see §10.1; committed `854362164` |
| V7 | *this version* | *(none yet)* | — | seat packet moved out of scratch to `r3c2_seat_packet/` and pinned in `R3C2_SEAT_PACKET.sha256`; **C4's instruction rescued from its own redaction span**; C5/C5b made self-contained; builder given a REQUIRED-content assertion with a passing deletion probe |
| V8 | `19a075c6…` | `R3C2_GATE_V7_codex…`, `R3C2_GATE_V7_kimi…` (on V7) | `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS` | see §10.2; both lists applied; `REPRO_AFTER_CHOICE` filed unreachable, HELD-CONTINGENT |
| V9 | `2a1d2023c2ea2b14…` | C0 by two blind seats (`R3C2_C0_EXHIBITION_kimi_20260905.md`, `R3C2_C0_VERIFY_codex_20260905.md`) | `C0_REACHABILITY=FAIL`, one unreachable class, both seats agree | see §10.3; HELD |
| V10 | `5c69ae471edb1b19…` | C0 two blind seats AGREE (`R3C2_C0_EXHIBITION_V10_codex…`, `…kimi…`), then `R3C2_GATE_V10_codex_20260905.md`, `R3C2_GATE_V10_kimi_20260905.md` | C0 PASS+PASS; gate `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS` | **option (c) adopted on the ruling; see §10.4; first gate with a settled definition — see §10.5** |
| V11 | `d6695c06c78c4735…` | C0 two seats AGREE (`R3C2_C0_EXHIBITION_V11_codex…`, `…kimi…`); `R3C2_GATE_V11_codex_20260905.md`, `R3C2_GATE_V11_kimi_20260905.md` | C0 PASS+PASS; gate `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS`; codex LEAK=NONE, kimi CONSEQUENCE_VISIBLE=NO | see §10.6 |
| V12 | `065dc0e48090d7d5…` | C0 two seats AGREE; `R3C2_GATE_V12_codex_20260905.md`, `R3C2_GATE_V12_kimi_20260905.md` | C0 PASS+PASS; gate `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS`; codex Q5 procedural only, kimi CONSEQUENCE_VISIBLE=NO, leak content-level only | see §10.7 |
| V13 | `22355a08b2d9cb98…` | C0 two seats AGREE; `R3C2_GATE_V13_codex_20260905.md`, `R3C2_GATE_V13_kimi_20260905.md` | C0 PASS+PASS; gate `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS`; codex LEAK=NONE + CONSEQUENCE_VISIBLE=NO, kimi CONSEQUENCE_VISIBLE=NO | see §10.8 |
| V14 | `b293f14016f20aca…` | C0 two seats AGREE; `R3C2_GATE_V14_codex_20260905.md`, `R3C2_GATE_V14_kimi_20260905.md` | C0 PASS+PASS; gate `PREREG_UNSOUND` (Q1 YES, LEAK=NONE), `PREREG_SOUND_WITH_REPAIRS` (CONSEQUENCE_VISIBLE=NO) | see §10.9 |
| V15 | `f997fce89cce1749…` | C0 two seats AGREE; `R3C2_GATE_V15_codex_20260905.md`, `R3C2_GATE_V15_kimi_20260905.md` | C0 PASS+PASS; gate `PREREG_UNSOUND` (CONSEQUENCE_VISIBLE=NO), `PREREG_SOUND_WITH_REPAIRS` (CONSEQUENCE_VISIBLE=NO) | see §10.10 |
| V16 | *this version* | *(C0 by two independent seats, then two-seat gate — pending)* | — | **both V15 lists applied; see §10.10** |

**Predecessor design, kept unchanged as the record of the failed design:**

| document | sha256 gated | gate | verdict |
|---|---|---|---|
| `R3C_MAGNITUDE_CENSUS_PREREG_20260904.md` | `c5e94620…` | `R3C_GATE_codex_20260904.md` | `PREREG_UNSOUND` |
| `R3C_MAGNITUDE_CENSUS_PREREG_20260904.md` | `ece4c6d9…` | `R3C_FROZEN_GATE_V2_20260904_agy.md` | see `R3C_GATE_ANOMALY_EVIDENCE_20260904.md` |

**Re-verified against git and disk 2026-09-04 23:35 KST (Blanc 23:32, item 3).** Every R3C2 row's hash was recovered
by hashing that commit's blob (`git show <commit>:<path> | shasum -a 256`), and every gate row's hash is the
`ACCESS_SHA=` the seat itself printed. **The V6 row previously read "*this version* / (pending)" and is now the
committed hash; leaving a live "this version" marker in a table that has since moved on is how the V4 row came to
carry a hash no seat had gated.**

**Nine dispatched gate runs across R3C and R3C2, no `SOUND` without repairs.** That history is itself reported to
Duho rather than buried in a version column.

## 10.1 V6 — what changed, and what deliberately did not

**Independent of the held definition, therefore repaired now** (Blanc 22:02):

- **C3 schema** gains `STANDARD` as an `origin` value — §3 defined admissibility partly by `origin STANDARD`, but
  the schema could not express it, so a measured-constant record could not be validly filled in at all
  (kimi V4 finding 3, codex V4 finding 2 second limb). §2 step 3 now defers to C3's closed list rather than
  carrying its own shorter parenthetical, which omitted `k_B`.
- **Provenance is transitive and computed, not asserted**: `derived_from` and a script-computed `root_origins`
  (design note §2, M2). This closes the one-derivation-step laundering route.
- **`origin` must cite the line that establishes it** (`origin_evidence` + reason code; design note M1).
- **The audit no longer samples the class where an error is invisible** (design note M3), and **the audit seed now
  comes from outside this lane after receipt** (design note M4, codex V4 finding 6).
- **Disagreement on `origin` is reported, never reconciled**: `ORIGIN_DISPUTED`, and `CENSUS_ORIGIN_DISPUTED` above
  10% of included claims.
- **`REPRO_NO_DERIVATION_STATED`** added, with a precedence order over the terminal classes: a paper can print a
  number as its own result while stating no equation that produces it, and that claim previously had no class
  (codex V4 finding 3).
- **`CENSUS_COMPLETE` and `CENSUS_PARTIAL` made exclusive** by defining completeness over the **arithmetic group**
  of §3 rather than over "every claim carries an outcome" (codex V4 finding 4).
- **The seal now requires a receipt, not a send** (codex V4 finding 7, kimi V4 finding 9).
- **The seat packet is built mechanically and its redaction is asserted** (codex V4 finding 5, kimi V4 finding 6).

**NOT repaired, deliberately:** codex V4 findings 1 and 2 (first limb) and kimi V4 findings 1, 2 (admissibility
consequence) and 4 (the widened FAILED class) all turn on **what the census measures** — the clause held in §3.
Repairing them under the current wording would be guessing Duho's ruling. They are open, and they are the reason
V6 is not dispatched as a fresh round.

## 11. Scope

No tier, warrant token, standing or stamp moves. Published sources only; nothing from another lane. Paper HOLD;
nothing outward. <!--SEAT-REDACT-->R3D is a separate document with its own gate record.<!--/SEAT-REDACT-->

## 10.2 V8 — both gate lists applied; one finding FILED, not repaired, because it turns on the held clause

**Two seats, two engines, both hash-verified against `19a075c6…`, both read only after exit:**
**codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`.**

**Where they agree:** the **blinding claim** and the **seal mechanism** are **SOUND** — both said so independently,
and kimi added that the seal's own limits are honestly stated. **Fairness is sound** in the operative outcome
wording. Both found the **study-level classes lack a filing precedence**, both found **pre-dispatch stops with no
class**, and both found **C0's "verified by Tori" contradictory**.

**Applied from both lists:** study-level precedence order; `R3C2_NO_CLASS` extended to pre-dispatch control
failures; C0 re-assigned to **two pattern-blind seats who must agree**, with Tori reduced to a coverage check;
§1 inclusion assigned independently by two blind seats; the `STANDARD` list **printed literally** with values and
uncertainties, because "a closed list fixed here" named four symbols and cited a paper whose baseline runs to dozens
of parameters, none printed — a membership test that could not be machine-checked; the word **"error"** removed
from C6, where this lane's own rule forbids it; every control given `PASS|FAIL|NOT_RUN`.

**kimi's sharpest catch, applied:** §7 claimed the interpretation protocol *"is fixed and committed before limb A
begins, **so** it cannot be written to suit the tally."* **That "so" was an overclaim by this document's own
standard** — the only custody binding on the protocol was §7's seal, which runs **after** Tori computes the tally,
and until Blanc receipts it the protocol is a local commit in this lane's own custody, which §7 itself calls tamper
evidence rather than custody. **The relay now happens before limb A**, where the claim requires it.

### FILED, NOT REPAIRED — `REPRO_AFTER_CHOICE` is currently unreachable, and the fix depends on Duho's ruling

**CONFIRMED BY A SEAT, 2026-09-05.** `R3C2_C0_EXHIBITION_kimi_20260905.md`, access-proven against `b4113602…`,
returns **`C0_REACHABILITY=FAIL`** with **exactly one unreachable verdict: `REPRO_AFTER_CHOICE`.** Six of seven §3
outcomes and **all seven §4 classes** exhibit cleanly with concrete inputs. The seat's own words: *"the method as
written contains no procedure that can ever file it, and §10.2 already files exactly that."*

**This class is HELD-CONTINGENT alongside §3's held admissibility definition and is NOT repaired.** Under the standing derivation-only
wording a printed-and-chosen value — the seat's example is entry 59's `β` — is inadmissible, so the attempt stops
and nothing can land in the class. **Making it reachable would require choosing option (b) on Duho's behalf.**
**Option (c) as drafted gives that case a home** by recording provenance beside a mechanical reproduction rather
than gating admissibility on it, which would retire the class along with the defect.

kimi, finding 2a: **§2 orders only an admissible-only arithmetic attempt, so no stated procedure ever establishes
"the number follows only once an inadmissible input is used".** `REPRO_AFTER_CHOICE` — **the class §3 says this
census exists to detect** — cannot be reached from the method as written.

**This is a declared-versus-actual mismatch, the same family C0 has now found three times.** It is **not repaired**,
and that is deliberate: kimi's fix inserts a second arithmetic attempt using the printed inadmissible value, which
is **only required if the ruling keeps the three-member arithmetic group.** Under option **(c)** — reproduce
mechanically, record provenance separately — `REPRO_AFTER_CHOICE` is retired and the defect disappears with it.
**Applying the repair would adopt option (b) by implication, and §3's held admissibility definition is HELD.**

**This is therefore an input to the ruling rather than a defect awaiting a patch, and it has a cost either way:**
option (b) needs extra machinery — a second arithmetic attempt per claim — to make its own headline class
reachable; option (c) removes the class and the machinery together. **Recorded here so the ruling can be made
knowing it.**

**R3C2 is NOT frozen and NOT run. §3's held admissibility definition remains HELD.**

## 10.3 The C0 exhibition, run by TWO blind seats — they agree exactly

**Both seats, independently and without sight of each other's work, returned `C0_REACHABILITY=FAIL` with EXACTLY
ONE unreachable verdict: `REPRO_AFTER_CHOICE`.**

| | author seat (kimi) | verifier seat (codex) |
|---|---|---|
| verdict | `C0_REACHABILITY=FAIL` | `C0_REACHABILITY=FAIL` |
| unreachable | `REPRO_AFTER_CHOICE`, and only that | `REPRO_AFTER_CHOICE`, "the sole unreachable verdict" |
| blocking clause | §2 step 4, admissible-inputs-only | §2 step 4, quoted verbatim |
| `CENSUS_COMPLETE` | reachable | reachable |
| held-clause dependence | stated | stated |

**The verifier was told it was verifying, that another exhibition existed, that it had not been shown it and must
not ask, and that disagreement would be reported rather than reconciled.** It agreed anyway, on the verdict, on the
single unreachable class, and on the clause that blocks it: *"the mandated attempt may not consume that input, and
no second attempt is specified."*

**Two blind seats agreeing is not a reason to repair it.** It is a reason to be confident the finding is real
before it reaches Duho, and the finding is **his** to resolve: making the class reachable means choosing option
(b), and option (c) as drafted retires the class along with the defect.

**A correction the verifier forced, and it is mine.** I have been calling this "§1's definition" in reports and in
this document. **The `HELD PENDING DUHO'S RULING` marker sits in §3**, over the admissibility definition; §1's
question embeds the same notion and changes with it, but the held clause is §3's. The verifier noted the mismatch
rather than silently adopting my label — *"although the request refers to §1 as held"* — and worked from the
document. **Three internal references are corrected here; the earlier reports said §1 and were wrong on the
section number, not on the substance.**

## 10.4 V10 — the held clause RULED: option (c), one pass, two tallies (2026-09-05 14:12 KST)

**Ruling.** Duho, typed into the lane pane 2026-09-05 14:08 KST: **"Q-R3C2 c"** — option (c) of the four put to him by
Blanc on 2026-09-04 21:53 KST (a: mechanical reproduction; b: derivation only; c: one pass, two tallies; d: stop the
census). The HELD marker that stood over §3 since V5.1 is removed; its text is preserved here verbatim, in the past
tense, because it was true when written:

<!--SEAT-REDACT-->
> ⚠️ **HELD PENDING DUHO'S RULING.** The clause below is the census's core definition and is **deliberately not
> being repaired.** Options **a/b/c/d** are stated in `_tmp_blanc_relay_r3c2_v5.txt` and **Blanc has the question
> with him**. A referee should **not** report this as a fresh finding, and it must **not** be counted as another
> failed round — it is one deliberately open question. **No later reader should read the current wording as a
> settled choice.** When Duho rules, exactly one clause changes.
>
> The wording standing here is option **(b)**, derivation-only. Option **(c)** is drafted, unadopted, in
> `R3C2_OPTION_C_ALTERNATIVE_DRAFT_20260904.md`.
<!--/SEAT-REDACT-->

**Exactly what changed, traced against every consumer:**
| clause | V9 (option b, HELD) | V10 (option c) |
|---|---|---|
| §1 question | admissible inputs, nothing chosen | two questions from one pass: does the recipe work; what does it rest on |
| §2 step 4 | admissible-only attempt | mechanical attempt with every `PRINTED`/`STANDARD` input the recipe names |
| §3 definition | ADMISSIBLE/INADMISSIBLE by `origin` | inputs consumed by status; provenance recorded; `rests_on` computed by script |
| `REPRO_AFTER_CHOICE` | a per-claim outcome (unreachable, §10.3) | **RETIRED** into `rests_on` — by the ruling, not by repair |
| arithmetic group | three members, held | **two: `REPRO_EXACT`, `REPRO_FAILED`** |
| §4 tally | reproduction tally | reproduction tally + `rests_on` tally |
| C3 | `root_origins` by script | + `rests_on` by the same script; seat-written or absent fails |
| C6 audit | re-classify `origin` | + recompute `rests_on` |
| §7 | silent on what is read | states that the interpretation reads `rests_on`, never the verdict alone |
| interpretation protocol | mapped on `REPRO_AFTER_CHOICE` and the abolished `NOT_ATTEMPTED` | revised to read `rests_on`; still no seat may open it; committed before limb A |
| header | "Version 1" (stale since V2) | Version 10 |

**Why (c), in the record's own words:** refusing every chosen or fitted input stopped the census being reproduction at
all, since a paper can direct you to use its own chosen constant and following that instruction IS reproducing the
paper. (c) restores reproduction as reproduction, keeps the provenance information by moving it from the verdict to a
factual field, and puts more distance between the hypothesis and the evidence: the interpretation reads a ledger field,
not an outcome whose definition the lane tuned. **No class is added; one is retired by the ruling that put its content
into a field.** Every study-level class, control, seal and blinding provision carries over.

**What V10 has NOT had:** its own C0 (two pattern-blind seats who must agree) and its own two-seat gate. It inherits
nothing from V9's rounds. **R3C2 is NOT frozen and NOT run.**

## 10.5 V11 — the first two-seat gate with a settled definition, reconciled; both lists applied, the leak first (2026-09-05 15:04 KST)

**Both V10 verdicts bound to `5c69ae471edb1b19…` and to the packet `e265d3f8…`, both ACCESS and PACKET hashes verified by
the lane owner against the files after each seat exited: codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`.
Both prior R3C2 gates ran against a document with a deliberately open core clause; their verdicts were verdicts on
something else. This is the first gate on the settled design.**

**Q1 — the substantive result of the ruling — came back YES.** codex: under option (c) §3 makes every declared outcome
reachable AND keeps the reproduction question decidable at the per-claim level, the printed-but-chosen `β = 1/929.25`
case traced to exactly one outcome and one `rests_on`. kimi: decidability YES on the same hardest cases; reachability
NO on one class — `REPRO_BLOCKED`'s exclusive domain was empty as written — repaired here by the named-source test.

**The leak, first (Duho 14:31: strip consequence, not just content).** codex from the packet alone: the lane has an
expectation; an unreproduced result is consequential; a favourable audit sample is possible. kimi from the packet
alone: the conclusion rides on `rests_on`; `DERIVED_ONLY` is the clean pole of a graded order; the corpus is cosmology;
the lane has an expectation; a comparison exists. **Applied:** C0's "refute this lane's own expectation" → "every
declared condition"; C6's "consequential and invisible" → "every claim in the arithmetic group"; the "favourable
sample" rationale, the `rests_on` severity order, the "interpretation reads `rests_on`" sentence, the retired-class
note and the origin-dispute rationale all moved into `SEAT-REDACT` spans; every "pattern-blind" in seat-visible text →
"independent"; the packet header no longer says what was removed; "Tori" leaves every seat-visible clause; the
builder's forbidden list gains the custody-chain names, the engine names, `R3D`, and the consequence words, each
asserted by the builder. **Kept, and why it cannot leak:** the wording rule "unreproduced from the stated inputs, not
error" constrains how a seat writes a negative, not whether it finds one; any census implies failures are possible.
**Accepted, and why:** the Planck-2018-only `STANDARD` list tells a seat the corpus is cosmology; so do the sources it
reads; that is content the seat must have, not consequence.

**Applied from both lists (substantive):** §4 total precedence with exactly-one filing (codex's chronological order;
kimi's differed only on the denominator dispute's place); `CENSUS_AUDIT_FAILED` extended to a seal failure (kimi);
every control `PASS|FAIL|NOT_RUN` and `NOT_RUN` spelled once (codex); C0 by two independent seats in the operative
text — the sentence §10.2 said was replaced at V8 and was not (both); C1/C2 machine-validated by the pinned script
(codex); `origin` classified by both seats, reason-code precedence for co-applicable codes, `MEASURED` added (kimi Q2;
codex Q2); referential integrity, acyclicity and "DERIVED needs parents" asserted by the script (kimi 5); disputed roots
carried as a pair (kimi 7); C6 sample formula bounded by `R` and the seed serialised (kimi 8, codex); stated-precision
rule (kimi 11); the two-receipt seal, P before limb A (both — §10.2 said this was applied at V8; it was not); C4
labelled procedural, not enforced, and the dispatch copy's contents listed before launch (codex, kimi obs 5); the
provenance script named, delivered and pinned, the dispatch script's absolute path stated, the corpus pinned by
manifest (both, codex).

**Escalated, the principal's:** codex asks to rename `REPRO_EXACT` to `REPRO_WITHIN_STATED_PRECISION` (kimi: the name
is cosmetic; the missing "report both numbers" is repaired here). A class rename is a redefinition — as with
`DYM_NO_*` in R3D — and is Duho's.

**Recorded, not a design change:** the pinned corpus is 89 enumerable texts, 106,676 non-blank lines. §6's
"2–3 seat-days" for limb B was written before the corpus was pinned and is an estimate, not a rule; the principal
should know the scale before ordering a run.

**Four items §10.2 recorded as "applied" at V8 were not in the operative text at V10** — the C0 assignment, the seal
timing, the three-valued tokens, the study-level precedence. That is the describe-versus-compute law failing in this
lane's own record, and it is stated here rather than absorbed.

**V11 has NOT had its own C0 or gate. R3C2 is NOT frozen and NOT run.**

## 10.6 V12 — the V11 gate reconciled; what is settled, and both lists applied (2026-09-05 15:56 KST)

**Both V11 verdicts bound to `d6695c06c78c4735…` and to the packet `a3516349…`; both ACCESS and PACKET hashes verified by
the lane owner against the files after each seat exited: codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`.**

**Settled, and stated so it is not lost under a run of UNSOUND verdicts:** (1) **the definition question is answered
on both engines** — under option (c) every declared outcome is reachable and the reproduction question is decidable on
every hardest case either seat constructed; the one boundary both found (a value the claiming paper cites from another
pinned text but does not print) is a totality repair, not the tension returning. (2) **The leak is closed on
consequence:** codex, from the packet alone, `LEAK=NONE` — design history and procedural stop consequences only, no
hypothesis, model or preferred outcome; kimi `CONSEQUENCE_VISIBLE=NO` — no sentence makes any outcome weightier than
another. Those two things parked this study for eighteen hours. What remains is ordinary design repair.

**kimi's residual inferences from the packet, each traced to a framing survival and repaired without adding any
framing back:** the token `C4_PATTERN_BLIND` told the seat a pattern exists → renamed `C4_SEAT_ISOLATION` at every
occurrence and "pattern" added to the forbidden list; "the principal's ruling", two V10 notes and "look clean" →
neutral wording; the stale parenthetical pointing at "the clause held in §3" → deleted. The §1 question itself
(derived-or-not) and the Planck-only `STANDARD` list remain: content, not consequence.

**Applied from both lists:** the cited-from-pinned-source input is `PRINTED` from that source with `origin`
`IMPORTED` and the attempt proceeds (kimi R1) — **codex's replacement, which would stop every such claim as
`REPRO_BLOCKED`, is quoted and answered:** under option (c) a paper directing the reader to a value in a pinned text
is directing the reader to use it, and following that direction is reproducing the paper; `REPRO_BLOCKED` keeps the
unobtainable-source domain; exclusion-kind tokens stated (kimi R7); `SEAT_BRIEF.md` authored, committed beside the
packet, asserted by the builder and pinned (kimi R6); the script's usage text corrected for `MEASURED`, a missing
`candidate_id` reported as a failure line, script re-pinned (kimi R5, R9); C0's token three-valued (both); C3's
input-versus-output ledger sentence (codex); "The census is void" → "No tally is filed" and the forbidden-list claim
stated at its true strength (codex Q5); `<sources_dir>` fixed to `.` and resolved commands printed (codex Q4); C4 and
C5b PASS defined as "no outside path in the printed list", completeness not claimed (codex); the judgement floor on
reason-code choice stated, master-only (kimi Q2).

**Escalated, unchanged:** the `REPRO_EXACT` rename — both engines now call the name cosmetic; the principal's.

**V12 has NOT had its own C0 or gate. R3C2 is NOT frozen and NOT run.**

## 10.7 V13 — the V12 gate reconciled; both lists applied (2026-09-05 16:26 KST)

**Both V12 verdicts bound to `065dc0e48090d7d5…` and to the packet `535173e6…`; both hashes verified by the lane owner after
each seat exited: codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`.** **The leak fix did not regress:** codex
`LEAK` names no hypothesis, model or preferred result and sees consequence only in the procedural "No tally is filed";
kimi `CONSEQUENCE_VISIBLE=NO` and `LEAK` content-level only (the corpus is cosmology; the chosen-input case is
anticipated). **Q1 is YES on kimi and NO on codex for the same one boundary**, which both engines located at the
cited-but-unprinted input: codex, a source obtainable but outside the manifest; kimi, a source that is RAW in the
manifest or enumerable with no matchable value at the cited line. **One rule closes all three:** the
PRINTED-from-source rule applies only when the value machine-matches at the named source's cited line; every other
cited-but-unprinted input files `REPRO_BLOCKED` (§2, §3), and `REPRO_INPUT_ABSENT` stays limited to an input traced to
no source at all.

**Applied from codex:** the seat-authored ledger schema now omits the computed fields and `validate` fails a ledger
that carries one; `origin_search {query, files, matches}` required for `ORIG_SILENT`; the merge of the two seats'
validated ledgers is a named command, `r3c2_ledger_tools.py merge`, producing `origin_alt` and `origin_evidence_alt`,
which `compute` then reads — script re-pinned `dc9c5642f1d2a092…`, its controls re-run (the negative control's exact
failure set is now five). **Applied from kimi (cosmetic, adopted as written):** "receipt verification of the seal" in
place of a pointer to a withheld section; "after the §2 attempt (one repeat permitted…)" in place of "after two
attempts"; "working directory" in place of "copy directory". **Escalated, unchanged:** the `REPRO_EXACT` rename.

**V13 has NOT had its own C0 or gate. R3C2 is NOT frozen and NOT run.**

## 10.8 V14 — the V13 gate reconciled; both lists applied; one finding is the lane owner's own (2026-09-05 17:23 KST)

**Both V13 verdicts bound to `22355a08b2d9cb98…` and to the packet `3eb3879f…`; both hashes verified by the lane owner after
each seat exited: codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`.** **The leak stays closed on both engines:**
codex `LEAK=NONE`, `CONSEQUENCE_VISIBLE=NO`; kimi `CONSEQUENCE_VISIBLE=NO`, leak content-level only. **Q1:** kimi YES on
every hardest case; codex NO on one encoding gap — `REPRO_BLOCKED` named a state the three-value `status` could not
carry, so no valid C2/C3 record could represent it. Both engines found it; **V14 gives `BLOCKED` a status in all three
live copies** (§2 step 3, C2, C3) and the class definition now covers both limbs §2 routes to it (kimi F3).

**A finding that is the lane owner's own, stated rather than absorbed (kimi F1):** the script the master pinned at
V13 was not the file on disk while the V13 seats read, because the lane owner extended `r3c2_ledger_tools.py` (the
`BLOCKED` status) at 16:37 KST, after dispatch. "No edits while a seat reads" applies to every pinned deliverable, not
only to the master. V14 commits the build deliberately after fixing kimi F2 — a planted `origin_alt` or
`origin_evidence_alt` in a seat-authored ledger is now rejected at intake, so the merge is the only channel that creates
them — re-runs the controls and re-pins.

**Applied from both lists:** `R3C2_NO_CLASS` bounded to controls C0–C5b, with a C6 audit failure or seal-receipt failure
filing `CENSUS_AUDIT_FAILED` (codex); the C3 sentence that asserted a machine check of "every value used" restated at its
true strength (kimi F5); C5 on the absolute interpreter with a PASS predicate (kimi F6); §1's inclusion rule carries
the two-reconciliation qualifier and no longer promises an audit the stop rule makes `NOT_RUN` (kimi F7); a seed that is
never supplied files `CENSUS_AUDIT_FAILED` with `C6_AUDIT_SAMPLE=NOT_RUN` (kimi F8); the C1 candidate schema stated
(kimi C-a); "enumerable text" (kimi C-c); the script's stale usage line (kimi C-b). **Escalated, unchanged:** the
`REPRO_EXACT` rename — codex now calls it substantive under the class-name test; it is the principal's.

**V14 has NOT had its own C0 or gate. R3C2 is NOT frozen and NOT run.**

## 10.9 V15 — the V14 gate reconciled; both lists applied (2026-09-05 17:55 KST)

**Both V14 verdicts bound to `b293f14016f20aca…` and the packet `fab99a5e…`; both hashes — and, this time, the script's pin —
verified by the lane owner after each seat exited: codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`.**
**Q1 is now YES on both engines.** **The leak stays closed:** codex `LEAK=NONE`; kimi `CONSEQUENCE_VISIBLE=NO`. codex's
one consequence hit was a V14 sentence of the lane owner's, "stops dispatch without a census tally" — procedural
framing, neutralised.

**Applied from codex:** C1's declared-versus-recomputed count comparison is now executable — the candidate and exclusion
files carry declared counts, the script compares them and prints both, a mismatch fails (finding 2.1). **Applied from
kimi:** `STANDARD` applies only to a value the paper prints, so a named-but-unprinted closed-list value is routed by the
named-source rule alone and two seats cannot split on its status (F1); `rests_on` is reported for every included claim
with a ledger record and a `NOT_COMPUTED` row carries the rest, so the tally's denominator is defined (F3);
`MACHINERY_UNAVAILABLE` names the non-timeout limb of `REPRO_NOT_EVALUABLE` (F4). **Escalated, unchanged:** the
`REPRO_EXACT` rename, which both engines now call substantive under the class-name test — the principal's.

**Custody, kept this time:** the C1 build was edited on the pinned file while kimi's V14 seat read, caught by the lane
owner within minutes, reverted from HEAD, held as a staged file, and swapped in only now with both seats exited; it is
committed and re-pinned at `e7f053b9b98b2ba5…` in this version.

**V15 has NOT had its own C0 or gate. R3C2 is NOT frozen and NOT run.**

## 10.10 V16 — the V15 gate reconciled; both lists applied (2026-09-05 18:28 KST)

**Both V15 verdicts bound to `f997fce89cce1749…` and the packet `8aa2ad86…`; both hashes and the script's pin verified by the
lane owner after each seat exited: codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`. Both: `CONSEQUENCE_VISIBLE=NO`.**

**The one thing codex still calls substantive is the framing both engines have named since V11 from different sides:**
four seat-visible sentences that anticipate and pre-defend the printed-but-chosen case ("Neither contaminates the other",
"PROVENANCE IS RECORDED, NOT FILTERED", the §2 step-4 parenthetical, "both facts survive"), which kimi reads as
content-level and codex as a cumulative direction handed to the classifiers. **Applied as codex wrote it, no wording
added:** the first two replaced by neutral statements of mechanism, the two explanatory sentences deleted, and "chosen
constants included" dropped from §1 and §2 step 4 because the status rule already says what is consumable. kimi's
remaining process tells — three "Added because" parentheticals, "the numbering has shifted twice", "Paper HOLD" — are
redacted from the seat's copy.

**Applied from kimi (required):** the `merge` exit-1 state — two seats agreeing on every candidate yet differing on an
input list — now gets one reconciliation and, if it survives, files `CENSUS_DENOMINATOR_DISPUTED`, whose definition
names input-list disagreement (F1). **Applied from codex:** the 120-second cap has a committed enforcement — the wrapper
`r3c2_timeout.py` (sha256 `fbb9bef7d6622a17b4dc2e856791e3166b60394c187286ea5581b2f39003f331`), monotonic deadline, prints command, stdout, stderr and exit status, `SYMBOLIC_TIMEOUT`
and exit 124 on the deadline; controls: a fast command passes, a five-second sleep under a one-second cap times out at
1.003 s, a failing child's status is carried. **Cosmetic, adopted:** the script's usage line names `BLOCKED`; script
re-pinned `bb5f1fc578fa79f0…` after both seats exited. **Escalated, unchanged:** the `REPRO_EXACT` rename; kimi adds that
`DERIVED_ONLY` also covers standard- and measured-only roots — a label question, the principal's with the other.

**V16 has NOT had its own C0 or gate. R3C2 is NOT frozen and NOT run.**

R3C2_PREREG_V16_READY_FOR_C0

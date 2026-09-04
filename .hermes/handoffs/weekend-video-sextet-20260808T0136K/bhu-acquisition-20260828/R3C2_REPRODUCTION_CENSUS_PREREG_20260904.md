# R3-C2 — REDESIGNED pre-registration: a reproduction census of the corpus's quantitative claims

**Tori, 2026-09-04 21:32 KST. Version 1. ORDERED by Duho, "redesign r3c", 2026-09-04 21:30 KST.**
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

For every quantitative claim in the corpus, **does the paper's own number follow from **admissible** inputs —
derived or standard — with no quantity chosen, fitted or imported?**

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

<!--SEAT-REDACT-->**Checked, because moving work into blind seats can move the pattern with it:** the §1 rule those seats apply is
*"a passage printing a numeral the paper asserts as a result of its own"*, with the excluded kinds enumerated —
equation numbers, reference numbers, page or line numbers, dates, attributed-not-derived. **Nothing in that rule
mentions magnitudes, shapes, comparison models or any lane conclusion**, and the seats receive the built packet,
whose redaction is machine-asserted against a forbidden list. **This repair therefore adds readers without adding
pattern content to what they are told.**<!--/SEAT-REDACT-->

## 2. Method — per claim, in order

1. **Extract** the printed number, its units, and the equation the paper says produces it, with file and line.
2. **List the inputs** that equation needs.
3. **Classify each input** as `PRINTED` (given in the paper), `STANDARD` (a measured constant **on C3's closed
   list — that list, verbatim, and no other value**), or `ABSENT`. Record its `origin` with the evidence C3 requires.
4. **Attempt the arithmetic with ADMISSIBLE inputs only** (§3's definition: origin `DERIVED` or `STANDARD`). A printed
   value whose origin is `CHOSEN` or `FITTED` is **not** admissible.
5. **Record the outcome**, per claim, as one of §3.

**A seat may not supply a value for an `ABSENT` input.** Encountering one ends that claim's attempt.

## 3. Per-claim outcomes — declared now

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

**The admissible input set is defined by PROVENANCE, not by location.** "Printed" says only where a value appears;
a value can be printed in the paper and still have been chosen or fitted — <!--SEAT-REDACT-->
entry 59's `β = 1/929.25` is printed and
chosen, and under a location-based rule its downstream numbers would have counted as reproduced, readmitting exactly
what this census exists to detect.
<!--/SEAT-REDACT--> So:

> **ADMISSIBLE** = a ledger record whose `origin` is `DERIVED` (obtained from the paper's own equations) or
> `STANDARD` (a measured constant on the closed list in C3). **INADMISSIBLE** = `origin` of `CHOSEN`, `FITTED`,
> `IMPORTED` or `UNDECLARED`, **however prominently the value is printed.**

- **`REPRO_EXACT`** — the paper's number follows, within its own stated precision, from **admissible inputs only**.
- **`REPRO_AFTER_CHOICE`** — it follows only once an **inadmissible** input is used, i.e. one whose origin is
  `CHOSEN`, `FITTED`, `IMPORTED` or `UNDECLARED` — **including one printed in the paper.** Name the quantity and its
  origin.
- **`REPRO_FAILED`** — admissible inputs are sufficient but the arithmetic does not give the paper's number.
  Report both numbers. **Wording: "unreproduced from the stated inputs," not "error."**
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
  **Name the input.** <!--SEAT-REDACT-->*(This class exists because the rule "a seat may not supply a value for an ABSENT input" had no
  outcome to file — a gate finding.)*<!--/SEAT-REDACT--> Distinct from `REPRO_AFTER_CHOICE`, where a value **was** supplied and the
  number then followed.
**Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the first in this
order:** `REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`, `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`, then the
**arithmetic group**. *(Precedence is stated because these conditions genuinely co-occur — an absent input whose
source is also unobtainable satisfied two classes with no rule to choose between them.)*

**The arithmetic group** is the set of outcomes that state whether the arithmetic reproduced the number. Its
membership is fixed by the clause held above; the group is referred to by name below so that §4 does not have to
be reopened when that clause is settled.

**Candidate exclusions are not per-claim outcomes.** Every enumerated candidate passage that fails the §1
definition is recorded in a **separate exclusion ledger** with file, line, the numeral, and which excluded kind it
is (equation number, reference number, page/line number, date, or attributed-not-derived). The census denominator
is the count of **included** claims; the exclusion ledger is reported alongside it and audited under C6, so nothing
is hidden by being excluded. <!--SEAT-REDACT-->*(The old `NOT_ATTEMPTED` class was incoherent: §1 defines a claim by the presence of
a printed number, so an included claim could never satisfy it — a gate finding.)*<!--/SEAT-REDACT-->

## 4. Study-level outcomes

1. **`CENSUS_COMPLETE`** — **every included claim carries exactly one outcome from the arithmetic group of §3.**
   Report the full tally with its denominator.
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

<!--SEAT-REDACT-->
**No study-level outcome is a verdict about the pattern.** §7 is where the pattern is touched, once, afterwards.
<!--/SEAT-REDACT-->


## 5. Controls, each with an exact named code

- **C0 — reachability, run BEFORE the freeze.** For **every per-claim outcome of §3** and **every study-level class
  of §4** — and for **any condition whose failure would refute this lane's own expectation** — **exhibit a concrete
  input that produces it**: a specific claim, its inputs, and the path it takes through this document to that
  verdict. **An outcome for which no such input can be exhibited is UNREACHABLE, and this preregistration does not
  freeze until it is.** The exhibition table is the artefact. **The exhibitions are authored by a seat and only
  verified by Tori** — deciding what counts as reachable is where an author's prior would enter, so the author does
  not decide it. `C0_REACHABILITY=PASS`.

  <!--SEAT-REDACT-->*(Added by Duho's order after the R3D diagnosis. In R3D, three consecutive repairs left the one condition capable
  of refuting this lane's pattern unable to return PASS on any path, each time in a different way, and **no other
  control could see it**: every other control checks that something is done correctly, none checks that an outcome
  **can happen at all**. **This census's §3 and §4 outcomes have never been reachability-tested**, and at least one
  is worth checking early — `CENSUS_COMPLETE` requires every included claim to carry an arithmetic-group outcome,
  which a single blocked or absent input in the whole corpus is enough to prevent. C0 does not touch, and does not
  depend on, the definition held in §1: it asks only whether each declared outcome can occur under whatever
  definition is settled.)*<!--/SEAT-REDACT-->

- **C1 — denominator.** Claims **included**, claims **excluded** (with the exclusion ledger of §3), and attempts made,
  all printed before any tally. <!--SEAT-REDACT-->*(This control previously referenced a class §3 abolished — a gate finding; the
  document has been swept for every other occurrence.)*<!--/SEAT-REDACT-->
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
  A chain cannot be made to look clean by classifying only its last step. *(What `root_origins` implies for a
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
- <!--SEAT-REDACT-->**C4 — pattern blindness, and an honest statement of its limit.** The referee wrapper's `--add-dir` **grants**
  directories; it does not restrict them, and it necessarily grants the lane directory, **which contains the pattern
  record**. So the tooling as it stands cannot enforce blindness to a lane-resident file, and a seat's own
  declaration is self-report.

<!--/SEAT-REDACT-->
  **C4 — what the seat must do.** Work **only** from the files in your working directory. **Print every path you
  open**, and print the working directory itself. Do not construct a path outside it; if you believe you need one,
  stop and report that instead of opening it. `C4_PATTERN_BLIND=PASS` requires that printed path list.

<!--SEAT-REDACT-->
  **What is therefore done:** each seat is run from a **redacted copy directory outside the lane**, containing the
  **seat packet** — not this document — the seat brief and the pinned sources, with the wrapper pointed at that
  directory and **not** at the lane. That is enforceable, and it is the control.

  **The seat packet is built mechanically, by `r3c2_build_seat_packet.py`, and its redaction is asserted.** The
  builder drops §0, §7, §8 and §10 whole, strips every span marked `SEAT-REDACT` in this document, and then
  **asserts that no string on a forbidden list survives anywhere in the output** — the pattern's name and topic,
  the comparison model, gate history, and the names of the people in the custody chain. **If any survives, the
  packet is not written and `C4_PACKET_REDACTED=FAIL`**; the study does not proceed on a hand-checked copy.
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
  rather than checking it.)* `C4_PACKET_REDACTED=PASS`. The seat's declaration and printed path list are kept as
  secondary detection.

  **What the blind proves and does not:** it proves the seat was not given the pattern record and did not read it
  from its working directory. **It cannot prove a seat has no prior exposure from training or an earlier session** —
  nothing available here can. The record states that limit rather than implying a stronger blind.
  
<!--/SEAT-REDACT-->`C4_PATTERN_BLIND=PASS`.
- **C5 — harness, LIVE.** Execute and print `python3 --version`,
  `python3 -c "import sympy; print(sympy.__version__)"`, and `shasum -a 256 $(command -v python3)`. **Transcribing
  expected values fails.** `C5_HARNESS_PINNED=PASS`.
- **C5b — no cross-lane access.** Print every path opened, each marked `IN_SCOPE` or `OUT_OF_SCOPE`; **any
  `OUT_OF_SCOPE` row fails the control.** `C5B_NO_CROSS_LANE=PASS`. *("As R3A/R3B" named no command and no code, and
  a seat that never saw those studies cannot resolve it — the defect codex found in R3D's C5/C5b.)*
- **C6 — audit, with a frozen sampling frame.** A third pattern-blind seat **first audits the full candidate and
  exclusion ledgers against every pinned source** — completeness, not just outcomes — then re-derives, **without seeing
  prior work and re-classifying every input's `origin` from the pinned sources**: **(i) every claim whose filed
  outcome asserts that the arithmetic reproduced the number** — the class in which a result unreproduced from the stated inputs is both consequential
  and invisible, so it gets no sampling discount — and **(ii) a sample of `max(1, ceil(0.20 × N))` of the remaining
  included claims**, `N` being the sealed denominator, drawn by
  `random.Random(seed).sample(sorted(claim_ids), k)`.

  **The seed comes from outside this lane.** After the tally digests are receipted<!--SEAT-REDACT--> (§7)<!--/SEAT-REDACT-->, **an external custodian
  outside this lane supplies a seed generated independently and unavailable to Tori before that receipt**, and it
  is recorded with the receipt. <!--SEAT-REDACT-->*(The custodian is Blanc, who is outside this lane and reports to
  Duho; §7 states the receipt.)*<!--/SEAT-REDACT-->
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

## 7. What happens after the tally — deliberately NOT specified here

**This preregistration says nothing about what any tally would mean for any hypothesis, and no seat is told.** The
gate's finding was that stating the mapping in the document the seats read hands them the stake of each outcome.
The interpretation step lives in `R3C2_INTERPRETATION_PROTOCOL_20260904.md`, which **no seat may open** and which is
itself fixed and committed before limb A begins, so it cannot be written to suit the tally.

**What the seal is, and what it is not.** Before the interpretation protocol is opened, Tori commits the tally, then
sends **four digests — tally hash, tally commit id, protocol hash, protocol commit id — to Blanc**, who is outside
this lane and reports to Duho. **The relay is complete only when it is receipted.** Blanc **acknowledges and timestamps the four digests in a
preserved receipt**; the interpretation protocol is **not opened** without that recorded acknowledgement. After
opening, Blanc independently re-hashes the tally and the protocol and verifies both hashes and both commit ids
against the receipt, and **the interpretation report must print the four verified values**. Any mismatch files
`CENSUS_AUDIT_FAILED`, leaves §7 `NOT RUN` and voids the comparison. *(A send with no recorded receipt is an
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

Live harness; `ACCESS_SHA` proof for any pinned source audited, verified by Tori after the run and not on the seat's
claim; path lists; 120-second cap on symbolic operations with `SYMBOLIC_TIMEOUT` as a reportable outcome; unreached
controls `NOT RUN`. Blind double, third seat via `nm_referee_dispatch.sh` on a split, Kimi arithmetic with a
no-fallback control, one-page check sheet, Tori re-runs every script, critic note before any ruling.

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
nothing outward. R3D is a separate document with its own gate record.

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

**This class is HELD-CONTINGENT alongside §1's definition and is NOT repaired.** Under the standing derivation-only
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
**Applying the repair would adopt option (b) by implication, and §1's definition is HELD.**

**This is therefore an input to the ruling rather than a defect awaiting a patch, and it has a cost either way:**
option (b) needs extra machinery — a second arithmetic attempt per claim — to make its own headline class
reachable; option (c) removes the class and the machinery together. **Recorded here so the ruling can be made
knowing it.**

**R3C2 is NOT frozen and NOT run. §1's definition remains HELD.**

R3C2_PREREG_V8_BOTH_LISTS_APPLIED_ONE_FILED

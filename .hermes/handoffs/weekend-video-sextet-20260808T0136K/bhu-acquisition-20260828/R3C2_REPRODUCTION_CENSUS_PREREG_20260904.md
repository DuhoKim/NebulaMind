# R3-C2 — REDESIGNED pre-registration: a reproduction census of the corpus's quantitative claims

**Tori, 2026-09-05. Version 36 — LIVING DRAFT: V35 + MEANINGLESS-ORDER INVARIANCE (the widened principle, Blanc 07:09) and the two-seat gate on V35 (§10.31); V35 = V34 + complete provenance graphs preserved at merge (§10.30); V34 = V33 + the two-seat gate on V33 closed inside the SPI pattern (§10.29); V33 = V32 + SEAT-PERMUTATION INVARIANCE, the pattern repair of the two-seat gate on V32 (§10.28); V32 = V31 + the repairs from the two-seat gate on V31 (§10.27); V31 = V30 + the repairs from the two-seat gate on V30 (§10.26); V30 = V29 + the repairs from the two-seat gate on V29 (§10.25); V29 = V28 + the repairs from the two-seat gate on V28 (§10.24); V28 = V27 + the repairs from the two-seat gate on V27 (§10.23); V27 = V26 + the repairs from the two-seat gate on V26 and the routine `rests_on` label (§10.22); V26 = V25 + D1 wording B + the stronger D7 + ownership batching, the three APPROVED by Duho ("approve all three", 2026-09-06T13:12:32Z, attested by Codex, relayed by Blanc 22:28 KST; §10.20) + the repairs from the two-seat gate on the integrated candidate (§10.21); NOT signed, NOT run; the signed design of record remains V23 (`R3C2_V23_DESIGN_OF_RECORD_55b466fa.md`, frozen 2026-09-06 00:00:22Z) until Duho signs V24 (see §10; §10.18 — the narrow scope correction after the 10:17 run abort; nothing else changed — Duho's ruling "hide the comparison, keep the taxonomy"). OPTION (c) ADOPTED — Duho's ruling "Q-R3C2 c", 2026-09-05 14:08 KST: one pass,
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

For every quantitative claim in the corpus, **does the paper's own number follow from the paper's own recipe applied to the inputs it states.**<!--SEAT-REDACT--> ; and (ii) what does that
number rest on — derived, standard or measured inputs only, or a chosen, fitted, imported or undeclared one? The first is the
reproduction verdict; the second is the ledger's `rests_on` field.<!--/SEAT-REDACT--> **The reproduction verdict and the provenance fields are recorded separately.**

**Operational definition, so the enumeration is not a judgement:** a *quantitative claim* is a passage in a pinned
source that **prints a numeral the paper asserts as a result of its own** — with units, or dimensionless and stated
as a value. Excluded, by definition and not by taste: numerals that are equation numbers, reference numbers, page or
line numbers, dates, values the paper attributes to another work without deriving, or numerals the paper sets as inputs to its own
calculation rather than asserts as results of its own (`AUTHOR_SPECIFIED_INPUT`, §3). **Every candidate passage is
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

**The corpus is pinned: `R3C2_CORPUS_MANIFEST.md` (sha256 `26dabe7cd94d3f2a1501c347ec1193b83528325905dc417c85e28a4a2fe84096`) lists every enumerable text by
digest and byte count; a seat enumerates claims from those files and no other. Files listed there as RAW are not enumerable
and are outside the census, visibly.** <!--SEAT-REDACT-->*(V11: no version before this one pinned the corpus at all — codex V10.)*<!--/SEAT-REDACT-->

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
   `CENSUS_OUTCOME_DISPUTED` (§4)<!--SEAT-REDACT-->, **and let the script record the claim's `rests_on`** from the ledger<!--/SEAT-REDACT-->.

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


<!--SEAT-REDACT-->**One pass, two tallies.** The reproduction verdict answers *"does the paper's arithmetic work from what it states?"*
The ledger answers *"what did it rest on?"* So:<!--/SEAT-REDACT-->

> **THE INPUTS THE ARITHMETIC MAY CONSUME** = every ledger record with status `PRINTED` (given in the paper, whatever
> its `origin`) or `STANDARD` (on C3's closed list). **Arithmetic consumes records according to status `PRINTED` or `STANDARD`.** Each record's `origin`
> is cited under C3, independently by both seats. **`origin` is one recorded attribute of a ledger record, beside
> `status`, `value`, `source_file` and `source_line`; a seat records it and writes no field outside the schema; `validate`
> fails a ledger that carries one. The seat's tool is `r3c2_ledger_tools.py`, sha256 `6c938c3f6b8af37e96996b963ea5ab8daebc52b13561e8af379035ba39622a3a` (`validate` takes the candidate file as its third argument), pinned at
> `R3C2_SEAT_PACKET.sha256` in the seat working directory; the seat runs its `census` and `validate` subcommands only.**
<!--SEAT-REDACT-->
> *(Lane side: `root_origins` and the per-claim field `rests_on` are computed from the merged ledger by `r3c2_lane_tools.py`,
> which no seat is given; an empty ledger is valid and every included candidate without a record carries `rests_on` `NOT_COMPUTED`;
> a claim whose dependency graph reaches a disputed record — in any claim — is itself `DISPUTED` with both values.)*
<!--/SEAT-REDACT-->
<!--SEAT-REDACT-->
> *(Master only — the rule the script implements: `DERIVED_STANDARD_OR_MEASURED_ONLY` (formerly `DERIVED_ONLY`, with identical membership) when every root origin is `DERIVED`, `STANDARD` or
> `MEASURED`; otherwise the most severe root origin present, in the fixed order `USES_UNDECLARED` > `USES_IMPORTED` >
> `USES_FITTED` > `USES_CHOSEN`. A claim with a disputed input or parent list is marked `DISPUTED`. In addition to its canonical per-input alternatives, `merge` preserves the two complete validated provenance graphs in `provenance_graphs`, ordered by the SHA256 of canonical JSON over their records sorted by `input_id`; equal graphs are retained once. `compute` obtains the claim's reported classification pair from those complete graphs, retaining equal classifications as a pair when the claim is disputed. It never treats an independently mixed PRIMARY or ALT graph as a graph supplied by a seat. The merged output, including these graphs, is serialised recursively with sorted object keys. Before sealing, a reconstruction with a duplicate `input_id` or an explicit identity field inconsistent with its enclosing keys is refused. At comparison, each enclosing-claim versus sealed-claim identity conflict is recorded as a `MISMATCH` of that input, propagated to every selected claim whose dependency closure contains the input, and fails the overall audit; every required field, evidence item and dependency edge is compared throughout each selected claim's complete dependency closure, records assigned to unselected claims included; complete branches are matched before roots are recomputed, and the sealed and matched branches are reported. **MEANINGLESS-ORDER INVARIANCE ("MOI", formerly SPI): the audit verdict and the whole audit outcome — verdict, the full ordered finding set with each finding's code and reason, the merged ledger bytes and the ledger digest — are invariant under every ordering that carries no meaning.** The KNOWN sources of such ordering, each named: (a) which seat is primary (seat permutation — the former SPI, now one source among several); (b) the order in which records arrive or are merged; (c) the iteration order of unordered containers — sets, dicts built from sets, set differences, anything whose traversal depends on PYTHONHASHSEED; (d) JSON member order (closed by sorted-key serialisation — an instance of this principle, not a separate rule); (e) filesystem listing order — no delivered tool walks a directory, so this source has no instance today. The list is of KNOWN sources; the invariant governs any other that is found. ENFORCEMENT is structural, at the boundary where each ordering is produced, so that no downstream step can observe it: `merge` orders the two seats by a seat-blind canonical key and the preserved complete graphs by their canonical digest, iterates inputs sorted, and serialises with sorted keys; `compute` classifies from the preserved graphs, iterates claims sorted and serialises with sorted keys; `audit compare` traverses every closure, root and graph-integrity walk in sorted order, reads the auditor's rederivation file, the candidate rows and the exclusion rows in sorted key order, and writes its artefact with sorted keys. Traversals and diagnostic selection are deterministic: starting input IDs and dependency IDs are visited in sorted order, and no reported error or output order depends on set iteration or process hash randomization; canonical branch selection remains solely at `merge`. EXHIBITION, one combined property in `r3c2_spi_exhibition.py` (the file and its PASS token keep the historical name): every construction is run under both seat orders and PYTHONHASHSEED 0, 1 and 2 (0 and 1 reproduce the V35 diagnostic variation on the V35 bytes), plus one run with both seats' record lists reversed and one with the auditor's rederivation file in reversed member order, and the whole outcome must be identical across all of them — the only field allowed to differ in the reversed-rederivation run is the seal of the rederivation bytes, which is the digest of what was delivered, an identity and not an ordering; every construction also asserts its expected verdict and diagnostic. Constructions are derived from the enumerated sources, not only from reviewer counterexamples. Fail-first is PER SUBCASE, each its own kit test method, against pinned byte copies of the V35 tools (and of the V32–V34 tools for the earlier subcases). If neither complete branch matches, an unconditional record-level `MISMATCH` is appended before any field-specific diagnostic, propagated to every dependent selected claim, and the audit fails even when the root-origin sets agree — the full-record predicate decides the verdict and the diagnostics only explain it. The comparison graph used to decide the audit is constructed only from complete matched input branches. Before root-origin classification, `audit compare` checks every `derived_from` edge in each selected claim's auditor-reconstructed dependency closure and its matched sealed closure for missing records and cycles, independently of `origin`. A missing dependency or cycle makes that claim `MISMATCH` and fails the audit, including when the cycle passes through a CHOSEN, FITTED, IMPORTED, MEASURED, STANDARD or UNDECLARED record. Root-origin traversal retains its stated origin rule; stopping at a non-DERIVED origin never substitutes for graph-integrity validation. Unmatched diagnostic views do not participate in this decision. Unmatched PRIMARY or ALT graphs are diagnostic views only: if their roots cannot be computed, the report records that fact without adding a mismatch or changing the audit verdict. The original disputes and the matched branches are reported without reconciliation. The interpretation step reads `rests_on` and the reproduction tally as two facts (§7). V11:
> kimi V10 read the severity order and the "interpretation reads rests_on" sentence from the packet and reconstructed
> the channel the conclusion rides on; both now live here, not in the seat's copy — the seat records provenance and
> never computes or weighs the field.)*
<!--/SEAT-REDACT-->

- **`REPRO_WITHIN_STATED_PRECISION`** <!--SEAT-REDACT-->*(named `REPRO_EXACT` until V21; renamed by the principal's ruling)*<!--/SEAT-REDACT--> — the paper's number follows, within its own stated precision, **from the paper's own recipe
  applied to the inputs it states** (`PRINTED` or `STANDARD`). **Report both numbers.** **Where the paper states no
  precision for the claim, the printed precision is the claim's stated precision: the reproduced value must round to
  the printed numeral at that precision, rounding half away from zero.** **Where the paper states an uncertainty, the test is |reproduced − printed| ≤ the stated
  uncertainty, taken once — not doubled, not rounded; where it states none, the rounding rule above applies. Where the stated uncertainty is asymmetric,
  the stated uncertainty is the half-width on the side the reproduced value falls.**<!--SEAT-REDACT--> The claim's `rests_on` is reported beside it.<!--/SEAT-REDACT--> <!--SEAT-REDACT-->*(kimi V10:
  "13.8 Gyr" against 13.797 was fileable either way; the rule decides it mechanically. codex V10 asked for the name
  to change to `REPRO_WITHIN_STATED_PRECISION`; a class rename is the principal's, escalated in §10.5.)*<!--/SEAT-REDACT-->
<!--SEAT-REDACT-->- *(`REPRO_AFTER_CHOICE` — RETIRED at V10 by the principal's ruling adopting option (c). What it recorded — that the number
  rests on a chosen, fitted, imported or undeclared input — is now the `rests_on` field of a `REPRO_WITHIN_STATED_PRECISION` or
  `REPRO_FAILED` claim, computed by script. Two blind C0 seats had found the class unreachable under the derivation-only
  wording (§10.3); it is retired, not repaired.)*<!--/SEAT-REDACT-->
- **`REPRO_FAILED`** — the inputs the paper states are sufficient for its recipe, but the arithmetic does not give the
  paper's number. Report both numbers. **Wording: "unreproduced from the stated inputs," not "error."**<!--SEAT-REDACT--> `rests_on`
  is reported beside it.<!--/SEAT-REDACT-->
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
  computational procedure that could produce it**, so there is nothing to attempt. Name the passage. **A procedure named but not
  specified — a sentence that says where the number came from without stating operations a seat could attempt — states no
  computational procedure that could produce it; file this class and name the passage.** <!--SEAT-REDACT-->*(A claim can
  satisfy §1 — a printed numeral asserted as the paper's own result — while the paper never says how it was
  obtained. That claim previously fell through every class.)*<!--/SEAT-REDACT-->
- **`REPRO_INPUT_ABSENT`** — an input the equation needs is `ABSENT` from the paper — **neither printed nor traced to
  any named source** — so the attempt stops there. **Name the input.** <!--SEAT-REDACT-->*(This class exists because the rule "a seat may not supply a value for an ABSENT input" had no
  outcome to file — a gate finding.)*<!--/SEAT-REDACT--> Distinct from a claim whose inputs the paper DOES state, chosen or not — that
  claim is attempted and files `REPRO_WITHIN_STATED_PRECISION` or `REPRO_FAILED`.
**Exactly one outcome is filed per claim. Where more than one terminal condition holds, file the first in this
order:** `REPRO_NO_DERIVATION_STATED`, `REPRO_BLOCKED`, `REPRO_INPUT_ABSENT`, `REPRO_NOT_EVALUABLE`, then the
**arithmetic group**. <!--SEAT-REDACT-->*(Precedence is stated because these conditions genuinely co-occur — an absent input whose
source is also unobtainable satisfied two classes with no rule to choose between them.)*<!--/SEAT-REDACT-->

**The arithmetic group** is the set of outcomes that state whether the arithmetic reproduced the number: **exactly
`REPRO_WITHIN_STATED_PRECISION` and `REPRO_FAILED`**.<!--SEAT-REDACT--> **`rests_on` is computed and reported for every included claim that has at least one
ledger record, whatever its outcome; a claim with no ledger record carries `rests_on` `NOT_COMPUTED`, and the `rests_on`
tally reports a `NOT_COMPUTED` row.**<!--/SEAT-REDACT-->

**Candidate exclusions are not per-claim outcomes.** Every enumerated candidate passage that fails the §1
definition is recorded in a **separate exclusion ledger** with file, line, the numeral, and which excluded kind it
is (equation number, reference number, page/line number, date, attributed-not-derived, or author-specified input). **The exclusion ledger's `kind` is one of `AUTHOR_SPECIFIED_INPUT`, `ATTRIBUTED_NOT_DERIVED`, `DATE`, `EQUATION_NUMBER`,
`PAGE_OR_LINE_NUMBER`, `REFERENCE_NUMBER` (alphabetical). `AUTHOR_SPECIFIED_INPUT` — a numeral the paper sets rather than derives and does not
assert as a result of its own: a grid size, a cutoff, a parameter adopted "for this calculation", a range chosen for a plot. Every exclusion
row carries the candidate's `source_file`, `source_line` and `numeral` — excluded from judgement, retained in the record, never discarded —
and `census` fails a row that lacks them or differs from its candidate row; `census` prints the `AUTHOR_SPECIFIED_INPUT` count as its own
line beside the denominator.** <!--SEAT-REDACT-->*(Adopted at V25 on the principal's word "일단 해" — "go ahead for now" — relayed 19:06 KST; a
decision to build on, not a settled taxonomy: a case the category mis-sorts during a run is a finding to bring back, not a widening.)*<!--/SEAT-REDACT--> The census denominator
is the count of **included** claims; the exclusion ledger is reported alongside it and audited under C6, so nothing
is hidden by being excluded. <!--SEAT-REDACT-->*(The old `NOT_ATTEMPTED` class was incoherent: §1 defines a claim by the presence of
a printed number, so an included claim could never satisfy it — a gate finding.)*<!--/SEAT-REDACT-->

## 4. Study-level outcomes

1. **`CENSUS_COMPLETE`** — **every included claim carries exactly one outcome from the arithmetic group of §3, with `C6_AUDIT_SAMPLE=PASS`. A
   denominator of zero files `CENSUS_PARTIAL` with the empty enumeration named; no census is complete over nothing.**
   Report the full tally with its denominator<!--SEAT-REDACT-->, **and the `rests_on` tally beside it — two tallies from one pass.**<!--/SEAT-REDACT-->
2. **`CENSUS_PARTIAL`** — after the §2 attempt (one repeat permitted, meaningful only for `REPRO_NOT_EVALUABLE`),
   **at least one included claim carries a non-arithmetic outcome (`REPRO_NO_DERIVATION_STATED`, `REPRO_INPUT_ABSENT`,
   `REPRO_BLOCKED`, `REPRO_NOT_EVALUABLE`), or the denominator is zero**. Report each and
   why. **INCONCLUSIVE, and it takes precedence over `CENSUS_COMPLETE`.** <!--SEAT-REDACT-->*(Previously "some claims unresolved"
   was undefined, and a blocked claim satisfied both classes.)*<!--/SEAT-REDACT-->
3. **`CENSUS_AUDIT_FAILED`** — the audit of §6 cannot reproduce a sampled per-claim outcome or ledger, or does not run to PASS for any cause (the
   cause named), **or the receipt verification
   of the seal fails**. No tally is filed; report which.
4. **`R3C2_NO_CLASS`** — a control among C0 through C5b fails **in every seat that attempted it** after two attempts;
   a packet or seat-isolation failure before dispatch files this class. **A C6 audit failure or a
   seal-receipt failure files `CENSUS_AUDIT_FAILED`, not this class.**
5. **`CENSUS_DENOMINATOR_DISPUTED`** — the two enumerations disagree after two reconciliation attempts, **or the two
   seats' input lists for the agreed claims disagree after the one C3 reconciliation**. The census does not proceed; the
   disputed candidates or inputs are listed. <!--SEAT-REDACT-->*(Added because the enumeration stop had no class.)*<!--/SEAT-REDACT-->
6. **`CENSUS_OUTCOME_DISPUTED`** — the two seats' filed per-claim outcomes on an agreed included claim differ after one
   reconciliation against the printed numeral and the stated-precision rule of §3. The census does not proceed; the claim is
   listed with both seats' outcomes, both number pairs, and the step each seat reached. <!--SEAT-REDACT-->*(Added at V21 by the principal's
   ruling; the gap was found by both gate engines at V18.)*<!--/SEAT-REDACT-->

7. **`CENSUS_ORIGIN_DISPUTED`** — the two seats' independent `origin` classifications disagree on inputs affecting
   **more than 10% of included claims**. The census does not proceed; every disputed input is listed with both
   seats' classification and both quotations. <!--SEAT-REDACT-->*(Disagreement about provenance is reported, never reconciled — if
   two blind readers cannot agree from the paper's own text what a number's provenance is, that is a finding about
   the corpus, and reconciling it would destroy it.)*<!--/SEAT-REDACT-->
8. **`CENSUS_CONTROL_SPLIT`** — a control fails in one seat and passes in another after two attempts. Report both
   seats' outputs and stop; **do not adopt the passing seat's result.** <!--SEAT-REDACT-->*(Added because this reachable state landed in
   no class.)*<!--/SEAT-REDACT--> <!--SEAT-REDACT-->*(Phrased this way
   because the old `R3C_NO_CLASS` said "in both seats", leaving a control that failed twice in one seat and passed in
   the other with no class — a gap codex found.)*<!--/SEAT-REDACT-->

**Exactly one study-level outcome is filed. Where more than one condition holds, file the first in this order:**
`R3C2_NO_CLASS`, `CENSUS_CONTROL_SPLIT`, `CENSUS_DENOMINATOR_DISPUTED`, `CENSUS_OUTCOME_DISPUTED`, `CENSUS_ORIGIN_DISPUTED`, `CENSUS_AUDIT_FAILED`,
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

- **C1 — denominator.** Claims **included**, claims **excluded** (with the exclusion ledger of §3), and the attempts
  made, all printed before any tally. **A seat is a sequence of sessions under one packet: the manifest's texts are partitioned into
  ownership batches (the pinned partition of `R3C2_CORPUS_MANIFEST.md` into 12 batches in row order); every session holds ALL pinned texts
  and enumerates ONLY its owned texts; §2's named-source lookups may read any manifest text and are logged with file and line. Every
  candidate id, claim id and input id begins with `<owned file>#`. Each session writes `candidates_b<k>.json`, `exclusions_b<k>.json`,
  `ledger_b<k>.json` and `SEAT_REPORT_b<k>.md`, sealed by the custodian in batch order before the next batch is dispatched, in a LIMB-A chain; the lane's pinned `join` (pure function, no renaming; `r3c2_batch_tools.py`, sha256 `3822f12c282aaf4b5c850bef08fbfbe3bce81ac09d5f9e3c578459239439f79e`; partition `39b8d9bf199265ab…`) produces the seat's one candidate file, one exclusion file and one ledger, over which `census` and `validate` run, and §6's two-seat agreement on limb A is obtained before any arithmetic. Limb B uses a separate directory from limb A: the custodian copies the agreed limb-A batch artefacts into that directory under the canonical names `candidates_b<k>.json`, `exclusions_b<k>.json`, `ledger_b<k>.json` and `SEAT_REPORT_b<k>.md`; the seat updates only these limb-B copies, records final outcomes, and runs `census … final` on them; the custodian seals and joins that directory in a separate ordered LIMB-B chain bound to the agreed limb-A seals file; the limb-A directory and seals remain unchanged; no `_limbB` filename suffix is used; `join` of the limb-B chain verifies the binding. The ownership list `OWNERSHIP_b<k>.txt` a session reads is the custodian's extract of the pinned partition, listed with its digest in the dispatch record. The files named below are the joined files of the applicable limb.** <!--SEAT-REDACT-->*(This control previously referenced a class §3 abolished — a gate finding; the
  document has been swept for every other occurrence.)*<!--/SEAT-REDACT-->
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
  ledger carries only the schema fields; `validate` fails a ledger that carries any other field.**<!--SEAT-REDACT-->
  *(Lane side: `r3c2_lane_tools.py merge` preserves branch-specific provenance evidence, adding `origin_alt`, `origin_evidence_alt` and, when the alternative uses `ORIG_SILENT`, `origin_search_alt`; it also preserves disputed parent lists. `compute` adds `root_origins` and per-claim `rests_on`.)*<!--/SEAT-REDACT--> An input that files `REPRO_BLOCKED` under §3 is recorded with status `BLOCKED`,
  `origin` `IMPORTED`, `ORIG_CITATION` evidence cited to the claiming paper's naming sentence, and no value; the arithmetic
  never consumes it.** <!--SEAT-REDACT-->*(`STANDARD` was missing from the `origin` enumeration while §3 defined
  admissibility partly by it, so a measured-constant record could not be validly filled in.)*<!--/SEAT-REDACT-->

  **`origin` must be cited, not asserted.** Every record carries `origin_evidence` with a reason code —
  `ORIG_CHOICE_STATED`→`CHOSEN`, `ORIG_EQUATION`→`DERIVED`, `ORIG_FIT_STATED`→`FITTED`, `ORIG_CITATION`→`IMPORTED`,
  `ORIG_MEASURED`→`MEASURED` (a quantity the paper reports as its own measurement, with the measurement described),
  `ORIG_CONSTANT`→`STANDARD`, `ORIG_SILENT`→`UNDECLARED` (listed alphabetically by origin; the list carries no order of its own) — and, except for `ORIG_SILENT`, a **verbatim quotation
  machine-matched to the cited line** — before any status-specific branch, `validate` requires every non-`ORIG_SILENT` record — `PRINTED`, `STANDARD`, `ABSENT` and `BLOCKED` alike — to carry a non-empty quotation occurring at the positive, one-based `origin_evidence.source_line` in `origin_evidence.source_file` (an `ABSENT` input keeps whatever origin its evidence supports — an unprinted measurement is `MEASURED` with its describing sentence quoted — and is not forced into `UNDECLARED` to close the corner); value-line checks are separate and never substitute for this evidence check; every `STANDARD` record, including one with `ORIG_SILENT`, requires a non-empty `source_file`, a positive one-based `source_line`, closed-list membership and the value as a numeric token at that line — absence of origin evidence never waives value evidence; every `BLOCKED` record requires an empty value, `IMPORTED`/`ORIG_CITATION`, and a candidate-file binding proving that its naming-evidence file is the claiming file; missing coordinates or a missing candidate binding fails `validate`. **Every input's `origin` is classified independently by both seats.** **Where
  more than one reason code matches the cited sentence, file the first in this order: `ORIG_CITATION`,
  `ORIG_FIT_STATED`, `ORIG_CHOICE_STATED`, `ORIG_MEASURED`, `ORIG_EQUATION`, `ORIG_CONSTANT`, `ORIG_SILENT` — a sentence
  that names an external source for the value is a citation whatever else it says — the order is a tie-break by the
  specificity of the evidence, not a ranking of the values.** **For an imported value (§2) `ORIG_CITATION` is satisfied by the non-empty verbatim quotation of the
  claiming paper's naming sentence at the claiming paper's own file and line; no reason code is applied to the source's line.** <!--SEAT-REDACT-->*(kimi V10's
  attack: "We adopt H₀ = 67.4 from Planck (2018)" filed CHOSEN passed every machine check and reported a less severe
  root; the code precedence makes the citation win. A reason code that matches its quotation but misapplies the
  precedence is caught only by the second seat's independent classification and the C6 re-classification, never by the
  machine; if every reader misclassifies identically, the record stands — that floor is stated here rather than implied
  away. `MEASURED` added because a measured-but-silent input was forced to
  `UNDECLARED`, the most severe root, by construction — kimi's observation 2.)*<!--/SEAT-REDACT--> **`UNDECLARED` is the default, not the residue**: a record leaves it only by
  producing that text, and an `ORIG_SILENT` record prints the search the seat ran; that printed `origin_search` (query, files, matches) is the
  mechanism by which the second seat and the auditor judge the search adequate — a search of one query with no variants is
  not adequate, and the auditor re-classifies the record from the pinned sources.

  **Provenance is transitive.** Every `DERIVED` record lists its `derived_from` ids; `validate` fails a `derived_from` id
  that names no record, a cycle, and a `DERIVED` record with no `derived_from`.<!--SEAT-REDACT--> *(Lane side: `r3c2_lane_tools.py
  compute` derives `root_origins`, the origins at the leaves of that chain, from every step; no seat writes that field.)*<!--/SEAT-REDACT--><!--SEAT-REDACT--> **Lane side, after both seats have exited: the lane owner runs the lane-side script `r3c2_lane_tools.py`, committed beside this document, sha256 `363713006f3e7c78eb03d10f0cba29685d663485f56948a46599959f1b7423d3`: `/usr/bin/python3 -E r3c2_lane_tools.py merge <ledger_seatA.json> <ledger_seatB.json> <merged.json>` and then `/usr/bin/python3 -E r3c2_lane_tools.py compute <merged.json> <out.json> <candidates.json>` (the candidate argument is mandatory; compute without it exits 2 and writes no output), printing for each the working directory, the resolved command, complete stdout and stderr, and the exit status. `merge` exits 1 if the two `input_id` sets differ — **if `merge` exits 1, the two seats reconcile their input lists against the paper's stated equation once; an input-set difference surviving that reconciliation stops the study under `CENSUS_DENOMINATOR_DISPUTED` (§4), the disputed inputs listed with both seats' quotations**; where the two `origin` classifications differ the merged record carries `origin_alt` and `origin_evidence_alt`; where the two `derived_from` lists differ the merged record carries both parent lists marked `PARENTS_DISPUTED`, and `compute` derives `root_origins` under both, printed as a pair, as for a disputed origin; where the two seats' value, status, symbol or source coordinates differ on the same input id, `merge` prints every such disagreement, reports `FIELD_DISAGREEMENTS`, exits 1 and writes no merged file — the lane resolves it in the open before the tally. `compute` derives each claim's `root_origins` and `rests_on` and prints the root-origin set beside it; it REJECTS (exit 2) a ledger that arrives with `root_origins` or `rests_on` already set; it FAILS (exit 1) on a `derived_from` id that names no record, on a cycle, and on a `DERIVED` record with no `derived_from`, so an empty root set cannot occur; a disputed pair is computed under both origins and marked `DISPUTED`. The seat tool `r3c2_ledger_tools.py` has no `compute` and no `merge`; a seat that runs either has left its packet. A `rests_on` value present in a seat-authored input ledger fails this control; after a successful `compute` run, a `rests_on` value absent from the script-produced output ledger fails this control.**<!--/SEAT-REDACT--> **The arithmetic may consume only records with status `PRINTED` or `STANDARD`.** A
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
  string printed in the value column; `validate` compares strings.** <!--SEAT-REDACT-->*(The list was previously "fixed here" by naming four symbols and citing a
  paper whose baseline runs to dozens of base, derived and nuisance parameters across several tables, none printed
  — so a machine membership test was impossible and "standard" was in practice a selectable family. kimi found it.)*<!--/SEAT-REDACT-->
  Each seat runs `/usr/bin/python3 -E r3c2_ledger_tools.py validate <ledger.json> <sources_dir> <candidates.json>` with the placeholders resolved and prints the working directory, the resolved command, complete stdout and stderr, and the exit status; the
  control's printed artefact is that run.<!--SEAT-REDACT--> The lane's `merge` and `compute` runs are printed the same way and are
  part of the same artefact.<!--/SEAT-REDACT--> `C3_NO_SUBSTITUTION=PASS` only on exit 0 from every printed run in the artefact; a
  token asserted without the printed run is FAIL.
  `C3_NO_SUBSTITUTION=PASS|FAIL|NOT_RUN`.
- <!--SEAT-REDACT-->**C4 — pattern blindness, and an honest statement of its limit.** The referee wrapper's `--add-dir` **grants**
  directories; it does not restrict them, and it necessarily grants the lane directory, **which contains the pattern
  record**. So the tooling as it stands cannot enforce blindness to a lane-resident file, and a seat's own
  declaration is self-report.

<!--/SEAT-REDACT-->
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

<!--SEAT-REDACT-->
  **What is therefore done:** each seat is run from a **redacted copy directory outside the lane**, containing the
  **seat packet** — not this document — the seat brief `r3c2_seat_packet/SEAT_BRIEF.md` (committed beside the packet,
  asserted against the same forbidden list by the builder, and pinned in `R3C2_SEAT_PACKET.sha256`), `R3C2_SEAT_PACKET.sha256` itself, `R3C2_CORPUS_MANIFEST.md`, the script
  `r3c2_ledger_tools.py`, the manifest script `r3c2_manifest.py`, the wrapper `r3c2_timeout.py`, and every pinned source listed in `R3C2_CORPUS_MANIFEST.md`, with the wrapper pointed at that directory and **not** at the lane. **The
  lane owner lists that directory's contents and their digests in the dispatch record before launch; a copy missing any
  of them is not dispatched.** **Confinement, as of V24:** each seat is dispatched inside a kernel sandbox profile (`r3c2_seat_sandbox.sb`, sha256 `6978d590bf2acc519f00f38e8bc71b0e9ef476b95eeb6afa38443dbaef731fa6`) whose complete effective read, write and network exceptions the dispatch record prints: the profile permits runtime and temporary-directory access beyond the seat working directory, including configuration-directory exceptions, and network access; it does not deny all outside reads or writes; its positive and negative probes establish only the tested accesses; C4 and C5b additionally prohibit seat-chosen data access outside the working directory and pinned environment, enforced through self-report; the lane master and the withheld interpretation material each have a recorded denied-read probe before dispatch; the profile's digest and its live positive and negative probes (a pinned source read; the lane master, an outside file and a listing
  of the lane refused with "Operation not permitted") are printed in the dispatch record before launch. That profile is the
  mechanism; `C4_SEAT_ISOLATION` and `C5B_NO_CROSS_LANE` remain the seat's self-reported account of what it opened, and PASS on
  them means what the printed list shows, no more. A dispatch without the recorded profile and probes is not a V24 dispatch.

  **The seat packet is built mechanically, by `r3c2_build_seat_packet.py`, and its redaction is asserted.** **The builder is pinned beside
  this document, sha256 `56ac7d1c78196c4d246244126b43666d804f093f8fbe4e2c2289ab885def728e` (it accepts explicit `--master`, `--out` and `--brief` arguments; the printed build command names them); a dispatch built by any other bytes files `C4_PACKET_REDACTED=FAIL`.** The
  builder drops §0, §7, §8 and §10 whole, strips every span marked `SEAT-REDACT` in this document, and then
  **asserts that no string on the forbidden list survives anywhere in the output — the list blocks the enumerated
  strings and does not establish that every consequence-bearing word is gone; procedural consequences of stop outcomes
  remain visible while hypothesis mappings, comparison-model preferences and empirical stakes are removed** — the pattern's name and topic,
  the comparison model, gate history, and the names of the people in the custody chain. **If any survives, the
  packet is not written and `C4_PACKET_REDACTED=FAIL`**; the study does not proceed on a hand-checked copy. **The
  forbidden list names the pattern's name and topic, the comparison model, gate history, every engine name, every
  person in the custody chain (the lane owner's name included), and every word that signals consequence rather than
  content — expectation, refute, consequential, invisible, favourable, unfavourable, stake, prior, tempting, warn. Build
  command, run from this directory: `/usr/bin/python3 -E r3c2_build_seat_packet.py --master R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md --out r3c2_seat_packet/R3C2_SEAT_PACKET.md --brief r3c2_seat_packet/SEAT_BRIEF.md`; expected first line of output
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

  **The accepted floor, ruled by the principal (2026-09-05 18:52 KST, "hide the comparison, keep the taxonomy"):** the task
  reveals that provenance is classified with care — seven values, quotations, two independent readers, disputes carried
  — and no wording removes that; the packet reveals that recorded provenance is independently re-classified and checked against the sealed
  record, but does not reveal that provenance is combined with the reproduction tally, what that summary is called, or how
  the interpretation uses it. A gate finding that a seat can tell provenance matters
  is the accepted floor under that ruling, not a defect; the argument is in `R3C2_LEAK_FLOOR_JUDGEMENT_20260905.md`.
  **What the blind supports and does not:** the dispatch record proves that the seat was not furnished the pattern
  record in its working directory. The self-reported path list is secondary evidence and, because it is not complete
  and the seat's own account is self-reported, this design does not prove more than the recorded confinement profile and its probes
  establish about what the seat could read. **It cannot prove a seat has no prior exposure from training or an earlier session** —
  nothing available here can. The record states that limit rather than implying a stronger blind.
  
<!--/SEAT-REDACT-->`C4_SEAT_ISOLATION=PASS|FAIL|NOT_RUN`.
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
  list is complete. **`IN_SCOPE` = C4's (i) and (ii), and every path opened by a printed command under C4's (iii); `OUT_OF_SCOPE` = any path the seat chose to open outside (i)–(ii), including through a placeholder or a wrapped `<command>`. The list records the seat's choices, not what printed commands load (C4).**** `C5B_NO_CROSS_LANE=PASS|FAIL|NOT_RUN`. <!--SEAT-REDACT-->*("As R3A/R3B" named no command and no code, and
  a seat that never saw those studies cannot resolve it — the defect codex found in R3D's C5/C5b.)*<!--/SEAT-REDACT-->
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
  `CENSUS_AUDIT_FAILED`.<!--SEAT-REDACT--> **A claim whose root-origin set contains an `ORIGIN_DISPUTED` input carries `rests_on` computed
  under both classifications, printed as a pair and marked `DISPUTED`; the `rests_on` tally reports a `DISPUTED` row.**<!--/SEAT-REDACT-->
  *(The audit artefact and its PASS predicate are stated in the opening of this control.)*
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
The interpretation step lives in `R3C2_INTERPRETATION_PROTOCOL_20260904.md`, which **no seat may open** and which is fixed, committed and receipted (receipt P) before limb A begins; the receipt, not the commit alone, is what
makes it unwritable to suit the tally.

**What the seal is, and what it is not — two receipts.** **(P) Before limb A begins, Tori commits the interpretation
protocol and sends its hash and commit id to Blanc, who is outside this lane and reports to Duho; Blanc acknowledges
and timestamps them in a preserved receipt P; limb A does not begin without receipt P.** **(T) After the tally — one commit containing the merged candidate file, the exclusion ledger, and the merged input ledger
with its `compute` output — is committed and before the protocol is opened, Tori sends the tally hash and tally commit id;
Blanc receipts them as T, and the receipt names every file in that commit;
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
`fbb9bef7d6622a17b4dc2e856791e3166b60394c187286ea5581b2f39003f331`) as `/usr/bin/python3 -E r3c2_timeout.py 120.0 -- <command>`, which enforces a 120.0-second wall-clock
deadline on the monotonic clock, prints the wrapper command, the child's stdout and stderr and its exit status, and on
the deadline prints `SYMBOLIC_TIMEOUT` and exits 124 — the reportable outcome; unreached controls `NOT_RUN`. Two independent seats, each
a sequence of sessions under one packet (C1); the dispatch record carries one `ACCESS_SHA` per session, the ownership list, and the
verified availability of every pinned text in that session's directory. <!--SEAT-REDACT-->On a split, a third seat is dispatched by the lane owner through the lane's referee dispatcher with its
`ACCESS_SHA` proof; third-seat dispatch is an administrative action of the lane owner and is not claimed executable from
the packet. Lane-side procedure, not the seat's: the no-fallback control `C5C_NO_FALLBACK=PASS|FAIL|NOT_RUN` requires a printed, session-identified provider log for every session — a missing log or any fallback entry is FAIL, an unreached check NOT_RUN — a pre-tally control under the `R3C2_NO_CLASS` and `CENSUS_CONTROL_SPLIT` rules, checked by the lane owner; a one-page check sheet `R3C2_CHECK_SHEET_<date>.md`
in plain words with source lines is written by the lane owner after the tally; the lane owner runs `r3c2_lane_tools.py` (sha256 `363713006f3e7c78eb03d10f0cba29685d663485f56948a46599959f1b7423d3`; merge, then `compute <merged.json> <out.json> <candidates.json>`, which emits `rests_on` `NOT_COMPUTED` for every included candidate with no ledger record, propagates a dispute through the whole dependency graph across claims, and fails unless its rows equal the included denominator) after both seats exit and re-runs every script; a
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
| V16 | `47c55a74af952058…` | C0 two seats AGREE; `R3C2_GATE_V16_codex_20260905.md`, `R3C2_GATE_V16_kimi_20260905.md` | C0 PASS+PASS; gate `PREREG_UNSOUND`, `PREREG_SOUND_WITH_REPAIRS`; CONSEQUENCE_VISIBLE=NO both | see §10.11 |
| V17 | `fe194fb4aee7603d…` | *(C0 by two independent seats, then two-seat gate with a sixth question — pending)* | — | **the principal's ruling applied: comparison hidden, taxonomy kept; both V16 lists applied; see §10.11** |
| V18 | `e67339905813549f…` | C0 two seats AGREE on V17; `R3C2_GATE_V17_codex_20260905.md` (UNSOUND, LEAK=NONE), `R3C2_GATE_V17_kimi_20260905.md` (SOUND_WITH_REPAIRS, leak content-level only) | both lists applied; class addition + `REPRO_EXACT` rename escalated (§10.12) | C0 by two seats, then gate — pending |
| V19 | `a0cf4d5cae4a2b74…` | C0 two seats AGREE on V18; `R3C2_GATE_V18_codex_20260905.md` (UNSOUND on the two escalated items only; LEAK=NONE), `R3C2_GATE_V18_kimi_20260905.md` (SOUND_WITH_REPAIRS; LEAK=NONE) | seven wording repairs applied; class question (+ zero-denominator clause) and rename remain escalated (§10.13) | C0 by two seats, then gate — pending |
| V20 | `e8ba4a7438d61f02…` | C0 two seats AGREE on V19; `R3C2_GATE_V19_codex_20260905.md` (UNSOUND: the escalated items + 2.1 final command + 7.1 dispatch list; LEAK=NONE), `R3C2_GATE_V19_kimi_20260905.md` (SOUND_WITH_REPAIRS; LEAK=NONE) | seven repairs applied incl. `PARENTS_DISPUTED` in the lane tool; escalated items unchanged (§10.14) | C0 by two seats, then gate — pending; a further round of NEW non-escalated findings stops the lane and files a diagnosis |
| V21 | `b146c8c45ad2dd9a…` | C0 two seats AGREE on V20; `R3C2_GATE_V20_codex_20260905.md` (UNSOUND on the escalated items + 2 small; LEAK=NONE), `R3C2_GATE_V20_kimi_20260905.md` (SOUND_WITH_REPAIRS; LEAK=NONE; ORIGIN_PURPOSE=CANNOT_STATE); lane STOPPED by its cap; Duho ruled "1a rename" 22:53 KST | ruling applied + four small repairs + zero-denominator clause (§10.15) | C0 by two seats, then gate — then freezable |
| V22 | `5cd4e6da543d2c0d…` | C0 two seats AGREE on V21 (both exhibit `CENSUS_OUTCOME_DISPUTED`); `R3C2_GATE_V21_codex_20260905.md` (SOUND_WITH_REPAIRS: one cosmetic; LEAK=NONE; rename verified, 0 governing old-token references), `R3C2_GATE_V21_kimi_20260905.md` (SOUND; LEAK=NONE) | the one cosmetic applied: `CENSUS_PARTIAL`'s definition names the zero-denominator case (§10.16) | C0 by two seats, then gate — then SIGNABLE for Duho |
| V23 | `55b466fadf8ca75f…` — **SIGNED 2026-09-06T00:00:22Z, the design of record** | C0 two seats AGREE on V22; `R3C2_GATE_V22_codex_20260905.md` (SOUND_WITH_REPAIRS: one brief artefact; LEAK=NONE), `R3C2_GATE_V22_kimi_20260905.md` (SOUND_WITH_REPAIRS: two cosmetics; leak = the accepted content-level floor; ORIGIN_PURPOSE=CANNOT_STATE) | kimi F1 (parenthetical on the right limb) and F2 (lane tool duplicate write removed, re-pinned) applied (§10.17) | C0 by two seats, then gate — then SIGNABLE for Duho |
| V24 | *living draft, unsigned* | run of 2026-09-06 aborted twice under V23 (`R3C2_RUN_ABORT_20260906.md`: lane copy layout; `R3C2_RUN_ABORT_20260906_1017.md`: the signed C4/brief scope rule forbids the path C5's harness requires) | C4 and C5b name the two system binaries as in scope; the frozen brief gets the same sentence (§10.18); NOTHING else | C0 by two seats, then gate — then to Duho for signature; V23 stays frozen and unsuperseded until then |

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

No tier, warrant token, standing or stamp moves. Published sources only; nothing from another lane. <!--SEAT-REDACT-->Paper HOLD;
nothing outward.<!--/SEAT-REDACT--> <!--SEAT-REDACT-->R3D is a separate document with its own gate record.<!--/SEAT-REDACT-->

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
validated ledgers is a named command, `r3c2_lane_tools.py merge`, producing `origin_alt` and `origin_evidence_alt`,
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

## 10.11 V17 — the leak floor RULED by the principal, and applied; both V16 lists applied (2026-09-05 19:10 KST)

**The loop was stopped by Blanc at 18:47 KST after six leak rounds; the lane's judgement is in
`R3C2_LEAK_FLOOR_JUDGEMENT_20260905.md`. Duho ruled at 18:52 KST: "hide the comparison, keep the taxonomy."** A future
reader should see that the residual leak was accepted deliberately, by the principal, with the argument — not overlooked
and not discovered by the lane as a limit of drafting.

**Applied as ruled.** (1) *Taxonomy kept in full*: seven origin values, quotations machine-matched, independent
classification by both seats, disagreements carried not reconciled. (2) *Comparison removed from the seat's view*: §1
asks one question; "two tallies", every `rests_on`, the severity order, "what the number rests on", the `rests_on`
tally and its membership rule, the DISPUTED pair, and "what the interpretation reads" live only in `SEAT-REDACT` spans;
`origin` is one recorded attribute of a ledger record. (3) *The tool split*: the seat's `r3c2_ledger_tools.py` (sha256
`230359ebd15a408714b965daa1b4a67b0c6445cca1c18c7cc6985d75cc581c44`) now has `validate` and `census` only and no word of the comparison in its text; `merge` and
`compute` are the lane's `r3c2_lane_tools.py` (sha256 `8e990c7a22fb4b093d5e74218e9bfcee4b108c52bbc2df615ed3b6b2aaefa848`), never given to a seat — because a tool that
names `rests_on` in its usage text tells the seat what origin is for. (4) *Taxonomy order*: the origin values and the
reason-code list are now alphabetical wherever a seat sees them; the previous order (DERIVED, STANDARD, MEASURED,
CHOSEN, FITTED, IMPORTED, UNDECLARED) encoded the severity ladder; the reason-code tie-break keeps its order because it
is a rule of evidence specificity that both seats need to agree, and says so. (5) *The residual*: a gate finding that a
seat can tell provenance matters is the accepted floor, recorded in C4 with the ruling cited.

**Both V16 lists applied.** codex: C1's "attempts made" defined and validated (`attempts` ∈ {0,1,2} per included
claim, `declared_attempt_count` compared by the script); the blind's claim cut to what the dispatch record supports;
`r3c2_timeout.py` in the dispatch-copy list. kimi: the STANDARD table carries a ledger-key column and the value is the
exact printed string, so a seat filing the table's own rows passes the delivered membership test (nine of fourteen rows
failed under the printed symbols). **Escalated, unchanged:** `REPRO_EXACT` and `DERIVED_ONLY` names — the principal's.

**Both V16 verdicts: CONSEQUENCE_VISIBLE=NO.** The V17 gate asks a sixth question — can the seat state what the recorded
origin is FOR? — as the test of the removable half.

**V17 has NOT had its own C0 or gate. R3C2 is NOT frozen and NOT run.**

R3C2_PREREG_V17_READY_FOR_C0

## 10.12 V18 — both V17 gate lists applied under the 18:56 autonomy grant (2026-09-05 19:5x KST)

V17 gate: codex `PREREG_UNSOUND` (LEAK=NONE, CONSEQUENCE_VISIBLE=NO; origin-purpose answer = independently re-classified, disputes
file `CENSUS_ORIGIN_DISPUTED` — the measured-provenance floor of the 18:52 ruling, not the comparison); kimi `PREREG_SOUND_WITH_REPAIRS`
(LEAK=content-level only — provenance recorded; CONSEQUENCE_VISIBLE=NO; ORIGIN_PURPOSE=CANNOT_STATE). **The floor held on both
seats: neither could state what the recorded origin is compared against.** Applied: (1) the lane-only C3 block still named
`compute`/`merge` on the seat tool after the V17 split (codex 7.1 = kimi R3) — rewritten for `r3c2_lane_tools.py`, pinned, and §9's
merge sentence corrected; (2) C3's PASS predicate is now the printed validator run (codex 2.1); (3) C6 requires a printed
`C6_AUDIT.json` with a MATCH/MISMATCH per audited claim (codex 2.2); (4) kimi R1(a)/(c): every included candidate carries `outcome`
(+`printed_value`/`reproduced_value` for the arithmetic group), `census … final` verifies it after limb B, and §2 step 5 names the
tally's assembly rule (seat tool re-pinned); (5) kimi R2: uncertainty test = |reproduced − printed| ≤ stated uncertainty, once;
(6) kimi R4: builder pinned in C4. **Not applied, the principal's:** kimi R1(b) — a new class `CENSUS_OUTCOME_DISPUTED` between
5 and 6 for a surviving per-claim outcome split (adding a class is on his stop-and-file list; §4 carries the pending note, and
the document is not freezable until ruled); codex 1.1 — the `REPRO_EXACT` rename (asked by both engines since V10; his).
No class retired, added or redefined. Not frozen, not run. *Process note, disclosed: the first V18 apply (commit dc884c637) ran
without abort guards, wrote only the codex items, built a packet and dispatched C0 seats on a master still headed V17; both seats
were stopped within a minute and their output archived unread; this is the complete V18.*

## 10.13 V19 — both V18 gate lists applied; LEAK=NONE on both seats (2026-09-05 20:33 KST)

V18 gate: codex `PREREG_UNSOUND` — its substantive defects are exactly the two items already escalated (the surviving per-claim
outcome split has no class, 1.1/7.1; the `REPRO_EXACT` rename, 6.1) plus one cosmetic (4.1); LEAK=NONE, CONSEQUENCE_VISIBLE=NO,
origin purpose = the C6 audit's own re-classification. kimi `PREREG_SOUND_WITH_REPAIRS` — LEAK=NONE (down from "content-level
only" at V17), CONSEQUENCE_VISIBLE=NO, ORIGIN_PURPOSE statable only as a check; D0 = the split class (the same escalated item),
C2 = the rename. **Applied (wording, no class or control changed):** codex 4.1 (C4 states what the packet does and does not
reveal, exactly); kimi R1 (asymmetric uncertainty = the half-width on the side the reproduced value falls); R2 (a named but
unspecified procedure files `REPRO_NO_DERIVATION_STATED`, passage named); C1 (`origin_search` is the adequacy mechanism; one
query, no variants, is inadequate); C4 (the §4 open note no longer says a gate found it — a process trace in the seat's view);
R3 (receipt T is one named commit — merged candidate file, exclusion ledger, merged input ledger with `compute` output — and
the receipt names every file); C3 (pin-file location worded truly). **Escalated, not applied:** the split class (options
filed 19:48 KST) — and kimi C5's optional clause that a zero denominator files `CENSUS_PARTIAL` rather than a vacuous
`CENSUS_COMPLETE` is added to that same ruling as a sub-option, since it moves a degenerate census between two classes; the
`REPRO_EXACT` rename. No class retired, added or redefined. Not frozen, not run.

## 10.14 V20 — both V19 gate lists applied; LEAK=NONE on both seats, second round running (2026-09-05 21:23 KST)

V19 gate: codex `PREREG_UNSOUND` — 1.1 and 6.1 are the escalated rulings; NEW 2.1 (the final `census` invocation must be one literal
command) and 7.1 (the dispatch inventory omitted `R3C2_SEAT_PACKET.sha256` and `R3C2_CORPUS_MANIFEST.md`); LEAK=NONE,
CONSEQUENCE_VISIBLE=NO. kimi `PREREG_SOUND_WITH_REPAIRS` — D1 = the escalated class; LEAK=NONE, CONSEQUENCE_VISIBLE=NO,
ORIGIN_PURPOSE = a cross-reader integrity check, not a verdict input. **Applied:** codex 2.1 (literal command, C1 and the brief);
codex 7.1 (inventory lists the pin file, the manifest, and every pinned source); kimi D2 (`CENSUS_COMPLETE` requires
`C6_AUDIT_SAMPLE=PASS`; `CENSUS_AUDIT_FAILED` covers an audit that does not run to PASS for any cause, the cause named — a
wording seam the seed clause already implied, no precedence changed); D3 (a `derived_from` disagreement between seats is carried
as `PARENTS_DISPUTED` and computed under both parent lists — lane tool patched, control added, re-pinned); D4 (five declared
counts; both candidate↔exclusion directions named — the tool already checked both); D5 (the §1 bold scar closed before the
redaction span); D6 (the two open-decision notes no longer point at a section the seat cannot see). **Escalated, unchanged:**
the split class (+ zero-denominator sub-option) and the `REPRO_EXACT` rename. No class retired, added or redefined. Not frozen,
not run. **Self-imposed cap:** if V20's gate returns new non-escalated findings, the lane stops and files a diagnosis instead of
a V21 — three repair rounds since the 18:52 ruling is the third-failure line applied to design churn.

## 10.15 V21 — Duho's ruling "1a rename" applied; the V20 small items applied as lane repairs (2026-09-05 22:57 KST)

**Duho's ruling** (relayed by Blanc 22:53 KST, verbatim "a with the separate account, 1a rename"; the first clause is Hwao's,
the second is this lane's): **(1a)** the class for a surviving per-claim outcome split is ADDED — `CENSUS_OUTCOME_DISPUTED`, in
kimi's V18 wording, between `CENSUS_DENOMINATOR_DISPUTED` and `CENSUS_ORIGIN_DISPUTED` in the §4 precedence; the two open-decision
notes of V18–V20 are replaced by the class. **(rename)** `REPRO_EXACT` becomes `REPRO_WITHIN_STATED_PRECISION` in every operative
section (§0–§9, §11) and in the seat tool's outcome set (re-pinned); §10's records keep the old name verbatim as history. Not
authorized and therefore NOT done: the `DERIVED_ONLY` rename (Blanc's relay reads Duho's single "rename" as `REPRO_EXACT` only).

**Lane repairs, mine, under Blanc's instruction to fold in what I had triaged:** codex V20 D2 (the five declared counts named in
the print step); codex V20 D4 (the third-seat dispatcher is stated as an administrative action of the lane owner, not claimed
executable from the packet — my recommendation over pinning infrastructure into a study document); kimi V20 D3 (rounding half
away from zero at an exact midpoint); kimi V20 D4 (C2 names its printed artefact); kimi V20 D5 (the §7 sentence rests the
unwritability on receipt P, not the commit alone); and kimi V18 C5's zero-denominator clause (a denominator of zero files
`CENSUS_PARTIAL`) — Blanc said to fold it in as I judged, and I judge a vacuous `CENSUS_COMPLETE` plainly wrong; it is a lane
repair, not part of the ruling, and is labelled so here.
The builder's required-content list carried the old token and was updated with the rename (re-pinned in C4).

**Scope guard honoured:** class added and name changed exactly as presented; nothing wider. NOT FROZEN, NOT RUN — C0 by two
seats and one two-seat gate follow; R3C2 does not run without Duho's separate word. Nothing outward. Paper HOLD.

## 10.16 V22 — V21 gate: the first clean round; one cosmetic applied (2026-09-05 23:32 KST)

V21 gate: **kimi `PREREG_SOUND`** (no repairs; LEAK=NONE; CONSEQUENCE_VISIBLE=NO; origin purpose = a cross-reader integrity check the
arithmetic never consumes). **codex `PREREG_SOUND_WITH_REPAIRS`** (LEAK=NONE; CONSEQUENCE_VISIBLE=NO; the rename verified by its own
grep and by `R3C2_V21_RENAME_AUDIT_20260905.md`: zero governing references to the old token) with one cosmetic inconsistency:
`CENSUS_PARTIAL`'s definition required "at least one included claim carries a non-arithmetic outcome", which a zero denominator
cannot satisfy although the zero-denominator clause orders `CENSUS_PARTIAL`. **Applied:** the definition now reads "…, or the
denominator is zero". Nothing else changed. Both escalated items are ruled and applied (§10.15). The cap of §10.14 is not
triggered (cosmetic only). NOT FROZEN, NOT RUN: C0 by two seats and one two-seat gate on V22; if both hold, V22 is SIGNABLE and
the freeze is Duho's chat signature on its digest. Running the census remains his separate word.

## 10.17 V23 — V22 gate: cosmetics only, applied (2026-09-06 00:03 KST)

V22 gate: codex `PREREG_SOUND_WITH_REPAIRS` (LEAK=NONE; its one item, 7.1, was the gate brief's version substitution pointing at a
non-existent V22 audit file — a brief artefact, the rename re-verified by its own grep; no document change). kimi
`PREREG_SOUND_WITH_REPAIRS` (CONSEQUENCE_VISIBLE=NO; ORIGIN_PURPOSE=CANNOT_STATE; leak line = the content-level residue accepted as
the floor by the 18:52 ruling, stated by the seat as "at or below the accepted floor"). **Applied:** kimi F1 — the non-arithmetic
token list now sits on the limb it defines, the zero-denominator limb after it; kimi F2 — `r3c2_lane_tools.py` wrote the merged
file twice (a V20 insertion of mine); the duplicate removed, controls re-run (one `merged` line, `PARENTS_DISPUTED` still detected,
pair still computed), re-pinned. Nothing else changed. NOT FROZEN, NOT RUN: C0 by two seats and one two-seat gate on V23; if both
hold with no finding above cosmetic, V23 is SIGNABLE and the freeze is Duho's chat signature on its digest. Running remains his
separate word.

## 10.18 V24 (living draft) — the narrow scope correction after the run's second abort (2026-09-06 11:02 KST)

**What happened under the signed V23.** Duho said "run the census" at 09:07 KST. The first dispatch aborted on the lane's copy layout
(A3, lane-side, `R3C2_RUN_ABORT_20260906.md`). The resumed dispatch, from a clean flat tree under a kernel sandbox with codex-cli
0.153.4 / gpt-6-astra, aborted at 10:17 KST because the seat obeyed the signed text to the letter: C4 ("do not construct a path
outside [the working directory] … any path outside the working directory is FAIL") and the brief ("do not open any other path")
forbid the path C5 requires (`/usr/bin/shasum -a 256 /usr/bin/python3`). The seat stopped at C5, filed `R3C2_NO_CLASS` for itself, and read no
source (`R3C2_RUN_ABORT_20260906_1017.md`). The signed design's harness is not executable under its own scope rule; the gates
read C5, they did not run it under a live scope instruction. **This is a defect in the text Duho signed at 09:00, stated in those
words.**

**The correction, and nothing else.** One clause in C4 and its echo in C5b: the two system binaries C5 names, and what they load
while executing the mandated commands, are in scope and are not "outside paths"; every other outside path still fails. The
brief receives the same clause in its own wording (kimi V24 F1: it is the same clause, not the same sentence). No class, control code, threshold, precedence, taxonomy or rule of interpretation
changes. The `DERIVED_ONLY` rename and kimi's V23 F1 are NOT in this version; they stay pending §10 amendments as before.

**Authority.** Preparation of this draft was authorised to the lane only as reversible drafting: Blanc's 11:01 KST note ("drafting and
testing an amendment changes nothing signed"). A "Codex relay" instruction of 10:59 and a ghost line "amend C4, V24, re-gate" were
NOT treated as Duho's authority (`GHOST_RELAY_AUDIT_20260906.md`). V23 remains the signed design of record; V24 supersedes it only
when Duho signs its digest in chat to Blanc. The census stays stopped until then and until his separate run word.

**V24 gate round 1 (11:35 KST).** C0: two seats PASS. Gate: codex `PREREG_UNSOUND` (LEAK=NONE; **C5_EXECUTABLE_UNDER_SCOPE=YES**, all
three C5 commands ran for it), kimi `PREREG_SOUND_WITH_REPAIRS` (LEAK=NONE; **C5_EXECUTABLE_UNDER_SCOPE=YES**). Both seats answer the
question V24 exists for with YES. **Applied within the narrow scope:** codex D2 — "whatever they load" was unbounded (a startup or
import file from `/tmp` or a user-writable path would have been licensed); the clause now names the system runtime locations
only (`/usr`, `/System`, `/Library`, `/private/var/folders`, `/dev`) — the same prefixes the kernel sandbox profile
`r3c2_seat_sandbox.sb` permits — and makes any other load an outside path; C5b and the brief carry the same bound. kimi F2 —
C5's third command is now `/usr/bin/shasum -a 256 /usr/bin/python3` (path-qualified, as the clause names it). kimi F1 — this
record's wording corrected. **Not applied, outside the narrow scope, pending for Duho with the `DERIVED_ONLY` rename and V23 F1:**
codex D1 — an imported value whose named source's line states a *choice* ("we choose a = 2") cannot carry `ORIG_CITATION` under
C3's pair rule while §2 requires `IMPORTED`/`ORIG_CITATION` for it; a pre-existing V23 evidence-rule seam, not a scope matter;
a repair would change the reason-code pairing, which is a rule change he must approve. codex D3 = the `DERIVED_ONLY` label, already
pending. Rebuilt and sent to a second C0 + gate.

**V24 gate round 2 (12:23 KST).** C0: two seats PASS. codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`; both LEAK at or
below the floor; **both answer C5_EXECUTABLE_UNDER_SCOPE=NO for one and the same reason, verified by the lane on disk and under the
kernel sandbox: on this host `/usr/bin/python3` resolves `sympy` from the user site `/Users/duhokim/Library/Python/3.9/lib/python/
site-packages`, which the runtime-locations bound excludes.** Both seats offered the same two remedies: provision SymPy into a system
root (an install the principal has not authorised), or admit the package by its printed, digest-pinned path. **Applied (V24c):** the
second — C4 admits the SymPy package only at the single path C5 prints, pinned by digest in the dispatch record; C5 gains the two
printed lines that establish that pin and FAILs on a mismatch; `/usr/local` is excluded by name (codex Q7(b)(i)); the antecedent of
"mandated commands" is spelled out (kimi F1); C5b and the brief echo the clause. The kernel profile `r3c2_seat_sandbox.sb` permits
exactly this set (the user-site path read-only, `/usr/local` and `/private/tmp` denied) and was exhibited: sandboxed `import sympy`
succeeds from the working directory, the lane and `/usr/local` stay unreadable, a write into the user site is refused. **Not applied,
pending for the principal:** codex D1 / kimi F3 (the imported-choice evidence seam; a C3 rule matter), codex D3 (`DERIVED_ONLY`).

**V24 gate round 3 (12:49 KST).** C0: two seats PASS. codex `PREREG_UNSOUND`, kimi `PREREG_SOUND_WITH_REPAIRS`; LEAK=NONE both;
**both C5_EXECUTABLE_UNDER_SCOPE=NO, same reason:** `import sympy` also loads mpmath and SymPy's own submodules from the user site, which
"the SymPy package … pinned by its `__init__.py` digest" neither admits nor pins (codex D3, kimi F1/F2). The lane's own probe found
two startup hooks loaded from that directory as well (an editable-install finder and setuptools' distutils hack). **Applied (V24d):**
C4 admits the user site-packages directory C5 prints taken WHOLE, pinned by a manifest digest over every file under it and recorded
in the dispatch record; C5 is five commands, the last two printing that path and digest, FAIL on mismatch; every mandated
interpreter call carries `-E` (no `PYTHON*` variable can redirect a load — codex Q7(b)(i)); the clause states plainly that the
directory is user-writable on the host, that the seat's confinement makes it read-only to the seat, and what the digest comparison
can and cannot detect. Manifest on this host at 12:49 KST: path `/Users/duhokim/Library/Python/3.9/lib/python/site-packages`. **Not applied, pending for the principal:** codex D2 (C6's
auditor reads the full candidate ledger, outcomes included, before its "without sight of earlier work" re-derivation — a V23 design
matter outside the narrow scope; its repair reshapes C6's inputs), codex D1 / kimi F3 (imported-choice evidence seam), D4 (`DERIVED_ONLY`).

**V24d → V24e (12:51 KST), before any seat read V24d.** The lane's own run of C5's fifth command on this host showed two things:
the user site holds 20637 files from many unrelated packages (astroquery, scipy, setuptools, an editable-install finder …), and several
of their names contain spaces, so the manifest command as first written failed here. The command is now null-safe (`-print0`,
`sort -z`, `xargs -0`). The V24d C0 seats, launched a minute earlier, were stopped and their output archived unread
(`_tmp_ABORTED_c0_v24d/`). **Stated for the principal, not decided by the lane:** admitting the whole user site is the honest
text-only fix and is what this version does, but it admits a large unrelated surface, read-only to the seat and digest-pinned. The
cleaner fix is a dedicated read-only runtime for the seats holding only SymPy and mpmath, pinned the same way, which is an install
the lane may not perform without his word; if he gives it, V25 replaces (b) with that runtime's path and nothing else changes.

**V24g — the full-round triage applied (Blanc 13:13/13:14/13:29 KST; 13:31 KST).** The V24e round: codex `PREREG_UNSOUND` (nine items,
C5_EXECUTABLE_UNDER_SCOPE=NO on the utilities the manifest pipeline invoked); kimi `PREREG_SOUND_WITH_REPAIRS`, C5_EXECUTABLE=YES,
ORIGIN_PURPOSE=CANNOT_STATE — **kimi's verdict is a RE-RUN on the restored V24e bytes: the original kimi seat was stopped unread at
13:11 when a superseding draft (V24f, principle only) was written against codex's report alone; that draft was withdrawn and V24e
restored so the round would be two-sided (`R3C2_V24_TRIAGE_20260906.md`).** Applied, exactly three in-scope repairs plus one
wording: **D5** the scope rule restated as the told-versus-chose principle with a closed boundary (working directory; pinned
environment by manifest; whatever the printed commands themselves invoke), residual stated; **D3** C5's fifth command is one process
(`r3c2_manifest.py`, pinned, fails loudly on any unreadable file — exhibited positive on 20,637 files, negative on a locked file,
and under the seat sandbox) and the document now states that no mandated command is a shell pipeline; **D6** `-E` on every printed
interpreter command so the claim is true by the text; **D9** the digest described as what the script prints. **Pending for the
principal, assembled separately with cost and urgency (`R3C2_INHERITED_ITEMS_FOR_DUHO_20260906.md`):** D1 (imported-choice evidence),
D2 (no exclusion kind for author-specified inputs), D4 (no result code on the lane-side no-fallback control), D7 (C6 auditor sees
outcomes before re-deriving), D8 (`DERIVED_ONLY`). Cap: one C0, one gate; a sixth NO on executability stops the lane.

**V24h — closure after the V24g gate (14:05 KST).** V24g gate: codex `PREREG_UNSOUND` with **C5_EXECUTABLE_UNDER_SCOPE=YES** and
**NO_MASKED_STAGE=YES** (its substantive items are the five inherited questions already assembled for the principal, plus D5 and D7
below); kimi `PREREG_SOUND_WITH_REPAIRS` with **YES / YES**, leak at the ruled floor. **The executability question is answered YES by
both seats for the first time; the cap's stop condition did not fire.** Applied here, closing the principle and three cosmetics:
codex D5 — executing a printed command does not authorise arbitrary data access; every placeholder, wrapped `<command>`, import or
data path the seat selects is a seat choice under (i)–(ii) (C4, C5b, brief); codex D7 / kimi F1 — the build command carries `-E`;
kimi F2 — the seat tool's usage text shows `-E` (tool re-pinned, controls re-run); codex C1 — "one invocation" wording for the
wrapper. Nothing else changed. Pending for the principal, unchanged: D1, D2, D4, D7, D8 (`R3C2_INHERITED_ITEMS_FOR_DUHO_20260906.md`).

**V24i — consistency closure after the V24h gate (14:40 KST).** V24h gate: codex `PREREG_UNSOUND` (D1–D4 = the five inherited items,
already assembled for the principal; D5 = the text both relied on and denied filesystem confinement; C1 cosmetic; C2 = `DERIVED_ONLY`),
kimi `PREREG_SOUND_WITH_REPAIRS` (cosmetics only); **both seats: C5_EXECUTABLE_UNDER_SCOPE=YES, NO_MASKED_STAGE=YES.** Applied: D5 —
the V23 sentence "procedural, not enforced by the filesystem" is replaced by the truth as of V24: each seat runs inside the pinned
kernel sandbox profile whose digest and live probes the dispatch record prints, while C4/C5b stay the seat's self-reported account;
the residual now says what matching manifests establish (matching snapshots, not immutability, no inference about trusted content);
codex C1 / kimi F1 — the flat prohibition no longer precedes its exceptions; kimi F2 — the brief says "all three pinned scripts".
Not applied (cosmetic, noted): kimi F4 (an empty-ledger message in the tool), F5 (§11's physical position). Pending for the
principal, unchanged: D1, D2, D4, D7, D8.

## 10.19 V25 (living draft) — D2 adopted on the principal's word; nothing else from the proposal (2026-09-06 19:07 KST)

**Duho's decision** (codex voice channel, relayed by Blanc 19:06 KST), verbatim: **"일단 해"** ("Go ahead for now"), to the question
whether numbers an author SETS as calculation inputs, rather than asserts as results, should be excluded from the set judged for
reproduction. **Adopted:** the exclusion kind `AUTHOR_SPECIFIED_INPUT`, with the numeral and source line RETAINED in the exclusion
ledger (excluded from judgement, not discarded from the record); the seat tool enforces the retained fields and prints the kind's
count beside the denominator; positive and negative controls added and run (`_tmp_r3c2_ledger_ctl/cand_asi.json`,
`excl_asi*.json`); the tool re-pinned. Recorded as "for now": if the category mis-sorts real cases during a run, that is a finding
to bring back, not something to widen quietly.

**What accepting D2 changes about what the census can conclude.** Numerals the papers set by hand leave the reproduction denominator:
they are no longer forced into `ATTRIBUTED_NOT_DERIVED` or into the claim set where they would file as "unreproduced" for lack of any
derivation. They go to the exclusion ledger under their own kind, with numeral and line kept, and their count is printed beside the
denominator, so the report says both how many claims the papers make and how many numbers they simply set. The denominator is
smaller and cleaner; no reproduction outcome changes; the seats' agreement on the denominator is more likely because the category
exists.

**Not adopted by this decision, stated by the principal's record and by Blanc:** D1 and D7 (still block a first run; still his), the
batch-reading approach for the corpus problem, any V25 fingerprint, any claim that a review passed, any restart. V23 remains the
signed design of record; V24i remains unapproved; this living draft goes to C0 and a two-seat gate as the required independent review
and then waits.

## 10.20 V26 — the three method choices ADOPTED on Duho's word; V25 + D1 wording B + the stronger D7 + ownership batching (2026-09-06 23:02 KST)

**Human direction, verbatim:** "approve all three" — Duho, 2026-09-06T13:12:32Z (22:12:32 KST), in the codex conversation, answering the
decision brief's three questions (brief as presented: sha256 `4826f0b2ed13d1fec76684093d10d71b323a9ef8f728fa0f030d66f6cb0b3499`;
candidate clauses revision 4 `3b959684…`; batch preparation `1f7206e4…`); attested by Codex
(`.hermes/CODEX_DUHO_TORI_THREE_METHODS_APPROVED_20260906.md`); relayed by Blanc 22:28 KST (`_tmp_relay_duho_three_approved.txt`).
Approval record: `R3C2_APPROVAL_RECORD_THREE_METHODS_20260906.md`. What the approval does NOT do, in his relay's words: it does not
complete the review of the integrated plan, does not sign it, does not authorise a census run; his 09:07 run order is consumed and a
fresh word is needed before any limb.

**What changed versus V25 (operative):** §1's excluded-kinds sentence names the sixth kind; §2's import rule is wording B (evidence at the
claiming paper's naming sentence; external value machine-matched as a numeric token in a verified manifest text at the first line
carrying symbol and numeral; a locally printed cited value is an import at its own line); C3 gains the import sentence and the
every-status evidence check; C6 is the stronger audit; C1, C1B and §9 carry ownership batching with limb-A and limb-B seal chains; the
seat tool (`16ae91a21fb2e039…`), lane tool (`da39212e26f9cb57…`), manifest script (`974458f3ec3d530e…`), builder (`b1f2cce11c5ffdde…`) and batch tool
(`eeafc482e6902eae…`) are the staged kit's tools under their pinned names, their previous bytes remaining in git. Non-operative: the status
header and this record. Alternatives he did not choose are not carried.

**Sources:** the integrated candidate `R3C2_V26_INTEGRATED_CANDIDATE_UNADOPTED_20260906.md` (`f4edb514…`, kept unchanged for provenance),
`R3C2_D1_D7_CANDIDATE_CLAUSES_20260906.md`, `R3C2_BATCH_PREPARATION_UNADOPTED_20260906.md`, `R3C2_DECISION_BRIEF_FOR_DUHO_20260906.md`.

## 10.21 V26 — the two-seat gate on the integrated candidate, reconciled and repaired here (2026-09-06 23:02 KST)

C0 on the candidate: codex PASS, kimi PASS (every new C6 and C1B path exhibited; nothing made unreachable). Gate: codex
`PREREG_UNSOUND` (ten findings), kimi `PREREG_SOUND_WITH_REPAIRS` (one non-cosmetic, two cosmetic); both: blind intact (LEAK none
directional; CONSEQUENCE_VISIBLE procedural or NO; ORIGIN_PURPOSE cannot be stated), C5_EXECUTABLE_UNDER_SCOPE=YES, NO_MASKED_STAGE=YES.
Reconciled BY TOPIC (`R3C2_V26CAND_GATE_RECONCILIATION_20260906.md`); every routine item repaired in this version and in the kit with a
control asserting its exact failure and a deletion probe (kit: 131 controls, 45 probes, PASS): the validate command's third argument
(codex F8 / kimi F1); the batch-session seat brief and the limb-A / limb-B chains (codex F10 / kimi F4); a locally printed cited value
(codex F1); empty ledgers and `NOT_COMPUTED` (codex F2); evidence for every status (codex F3); dispute propagation across claims (codex
F4); the JOIN/C1B/C5C result contracts (codex F5 / kimi F3); the confinement paragraph (codex F6); builder arguments and the candidate
pin sheet (codex F8); the manifest's symlink refusal (codex F9); §3's parenthetical (kimi F2); the diff sentence (codex Q7c).
**Not repaired, Duho's:** the name `DERIVED_ONLY` for "every root origin DERIVED, STANDARD or MEASURED" (codex F7; kimi: the principal's
pending item) — a class-name change; cost: rename the emitted token and its consumers, membership unchanged; the lane's
recommendation: rename to `DERIVED_STANDARD_OR_MEASURED_ONLY`. Held for his word; nothing in this version depends on it.
**Next:** C0 by two seats and the two-seat gate on THIS version; then the completed plan and its digest go to Blanc for the
final-adoption checkpoint (the 11:11 form); the run only on his fresh word.

## 10.22 V27 — the two-seat gate on V26, reconciled and repaired here; the `rests_on` label (2026-09-06 23:52 KST)

C0 on V26: codex PASS, kimi PASS. Gate on V26: codex `PREREG_UNSOUND` (seven findings, three cosmetics; LEAK=NONE), kimi
`PREREG_SOUND_WITH_REPAIRS` (two non-cosmetic, one cosmetic, one corner; blind intact); both C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES, PRIOR_FINDINGS_CLOSED=NO. Reconciled BY TOPIC (`R3C2_V26_GATE_RECONCILIATION_20260906.md`); all routine, all
repaired here and in the tools (kit: 141 controls, 49 deletion probes, PASS), the graph bypass and the cross-batch lifecycle first as
Blanc's 23:44 order prioritised: the audit compares reconstructed input records and dependency edges and recomputes root origins
(codex F2 — the property D7 was approved for); limb B in a separate directory under canonical names (codex F4 / kimi F2); per-session
validation NOT_RUN, joined validation before limb-A agreement (codex F5); the shared evidence check for every non-silent record before
any status branch — extended, not bent: an `ABSENT` input keeps the origin its evidence supports and is not forced into `UNDECLARED`
(codex F1 / kimi F4; Blanc 23:44 §3); C3's second copy of the lane-tool pin and the two-argument compute, now mandatory three-argument
(codex F3 / kimi F1 / N2); C5's manifest pin (codex F6 / kimi F3); the manifest's root check (codex F7); the local-import summary
sentence (codex C1); the printed build command (codex C2); tool docstrings (kimi N1); the ownership list's provenance (kimi N3).

**The `rests_on` label, implemented as routine.** `DERIVED_ONLY` is renamed `DERIVED_STANDARD_OR_MEASURED_ONLY` in this version, the lane
tool (`fd91ce950b27101b…`), the interpretation protocol (V5, `54c7cb78a748cde3…`, the receipt-P seal of the voided run superseded) and the kit; the
membership is unchanged (every root origin `DERIVED`, `STANDARD` or `MEASURED`). Both V26 gate reviewers found the rename LABEL-ONLY: no
class, passability, reachability or conclusion changes. It was therefore implemented under standing authority as routine work, not ruled
on (Blanc's order of 23:45, correcting his 23:44 hold); the historical token is preserved wherever a record states what an earlier
version said (§10, the V23 design of record, protocol V1–V4). Still Duho's: whether the census runs, and the signature on any successor
to V23. **Next:** C0 and the gate on V27; then the completed plan and digest to Blanc for the final-adoption checkpoint.

**Erratum recorded 2026-09-06 23:59 KST.** Between 23:54 and 23:58 KST, on Blanc's order of 23:53 (since withdrawn as a false alarm, `BLANC_ORDER_LABEL_SCAR_CHECK_WITHDRAWN.md`),
the lane rewrote change-record entries: one sentence of §10.21 was replaced and eleven other §10 lines mentioning `DERIVED_ONLY` had a
bracket appended (commit 3b4073e52, master `e7fe9a26…`). Rewriting a change record to match the present state is exactly what this lane
must never do; every §10 entry before this one is restored here to its bytes at commit c94c7457a (twelve lines). The current-state
corrections made in the same pass outside this document's history (run plan, reconciliation, state, open questions) stand. The C0 seats
dispatched on the rewritten master were stopped and their partial outputs archived unread (`_tmp_VOID_c0_v27_e7fe9a26/`); C0 is
re-dispatched on this restored master.

## 10.23 V28 — the two-seat gate on V27, reconciled and repaired here (2026-09-07 00:46 KST)

C0 on V27 (the restored master `12daf4f5…`): codex PASS, kimi PASS. Gate on V27: codex `PREREG_UNSOUND` (four findings, two cosmetics;
LEAK=NONE), kimi `PREREG_SOUND_WITH_REPAIRS` (two cosmetics; 19 of 20 prior items closed); both C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES; prior findings: every V26 item closed by both except the audit's completeness (codex) and the tool docstrings
(kimi). Reconciled BY TOPIC (`R3C2_V27_GATE_RECONCILIATION_20260907.md`); all routine, all repaired here and in the tools (kit: 156
controls, 54 deletion probes, PASS): the audit accepts only complete reconstructions (schema validated at the re-derivation seal),
compares every field, evidence coordinate and quotation, and never borrows a dependency from the sealed side (codex F1); a declared
sealed alternative is compared like with like under its branch (codex F2); `STANDARD` coordinates are required unconditionally and
`BLOCKED` naming evidence is bound to the claiming file (codex F3); an ordinary `PRINTED` record may cite its evidence on a line other
than its value line, the value being checked at its own line only (codex F4); the historical parenthesis (codex C1 / kimi F1); the
delivered lane and batch tool docstrings (codex C2 / kimi F2, kimi's V26 N1). **Next:** C0 and the gate on V28; then the completed plan
and digest to Blanc for the final-adoption checkpoint; the run only on Duho's fresh word.

## 10.24 V29 — the two-seat gate on V28, reconciled and repaired here (2026-09-07 01:45 KST)

C0 on V28: codex PASS, kimi PASS. Gate on V28: codex `PREREG_UNSOUND` (three findings; LEAK content-level only), kimi
`PREREG_SOUND_WITH_REPAIRS` (five cosmetics, no executable defect); both C5_EXECUTABLE_UNDER_SCOPE=YES, NO_MASKED_STAGE=YES; prior V27
findings closed by both except the audit's closure comparison and the declared-alternative rule (codex, PARTLY) and the docstring
remnants (both). Reconciled BY TOPIC (`R3C2_V28_GATE_RECONCILIATION_20260907.md`); all routine, all repaired here and in the tools (kit:
165 controls, 57 deletion probes, PASS): every reconstructed record in a selected claim's complete dependency closure is compared,
off-sample claims' records included (codex F1); a declared alternative — origin and/or parent list — is matched over the whole closure
once and the sealed roots are recomputed under that graph, so parent-only and inherited alternatives pass (codex F2); a `STANDARD`
value line outside the claiming file is an import, not `STANDARD` (codex F3); the builder prints byte counts (kimi N1); the corpus
manifest's informational line column carries its stated convention, the manifest re-pinned (`2d8f29656dc86bbc…`) and the partition regenerated
(`1a4c30909f17f3b7…`) (kimi N2); the kit README (kimi N3); the manifest tool's docstring, the seat tool's labels and its usage synopsis (kimi
N4 / codex C2); `merge` fails in the open on a value, status, symbol or coordinate disagreement (kimi N5). **Next:** C0 and the gate on
V29; then the completed plan and digest to Blanc for the final-adoption checkpoint; the run only on Duho's fresh word.

## 10.25 V30 — the two-seat gate on V29, reconciled and repaired here (2026-09-07 02:33 KST)

C0 on V29: codex PASS, kimi PASS. Gate on V29: codex `PREREG_UNSOUND` (two findings; blind intact), kimi `PREREG_SOUND_WITH_REPAIRS` (two
cosmetics, no executable defect); both C5_EXECUTABLE_UNDER_SCOPE=YES, NO_MASKED_STAGE=YES; prior V28 findings closed by both except the
two codex corners (PARTLY) and the manifest column (kimi, PARTLY). Reconciled BY TOPIC (`R3C2_V29_GATE_RECONCILIATION_20260907.md`); all
routine, all repaired here and in the tools (kit: 174 controls, 61 deletion probes, PASS): a reconstruction's `input_id`s are unique
across the whole reconstruction, explicit identity fields must agree with their keys, and at comparison each record is bound to its
sealed claim — a duplicate can no longer shadow a fabricated copy and a mis-keyed record is `MISMATCH` (codex F1); a declared alternative
matches only as a COMPLETE branch — a hybrid of primary and alternative fields is `MISMATCH` even when the roots agree (codex F2); the
corpus manifest's informational line column now states its convention at the character level (newline-delimited; space, tab and
carriage return are the only blank characters) and is recomputed to it, the manifest re-pinned (`7f97591b5fd4a138…`) and the partition
regenerated (`778de7a2adf1f03e…`) (kimi N1); a duplicated comment line removed from the seat tool (kimi N2). **Next:** C0 and the gate on V30;
then the completed plan and digest to Blanc for the final-adoption checkpoint; the run only on Duho's fresh word.

## 10.26 V31 — the two-seat gate on V30, reconciled and repaired here (2026-09-07 03:22 KST)

C0 on V30: codex PASS, kimi PASS. Gate on V30: codex `PREREG_UNSOUND` (two findings, one cosmetic; blind intact), kimi
`PREREG_SOUND_WITH_REPAIRS` (only the carried, declared-deferred manifest header); both C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES. Reconciled BY TOPIC (`R3C2_V30_GATE_RECONCILIATION_20260907.md`, every label swept programmatically); all routine,
all repaired here and in the tools (kit: 176 controls, 61 deletion probes, PASS): the full-record branch predicate is authoritative —
a record matching neither complete declared branch is an unconditional `MISMATCH` before any diagnostic, so the REVERSE hybrid
(alternative origin and evidence with the primary parents) fails (codex F2); an identity conflict is a `MISMATCH` of the record itself,
carried into every dependent selected claim's rows (codex F1); the manifest header now says the line column is summed and reported by
the partition tool and used as no integrity predicate, the manifest re-pinned (`26dabe7cd94d3f2a…`) and the partition regenerated
(`39b8d9bf199265ab…`) (codex C1 / kimi C1, deferred from V29). **Discipline recorded (Blanc's order of 03:03):** the authoritative guard had
been REMOVED by the lane at 02:31 so that three deletion probes could register kills — the reverse hybrid was the consequence; the guard
is restored and never again weakened for a probe: the affected probes now assert that the specific diagnostic disappears while the
verdict still fails on the guard. **Next:** C0 and the gate on V31; then the completed plan and digest to Blanc for the final-adoption
checkpoint; the run only on Duho's fresh word.

## 10.27 V32 — the two-seat gate on V31, reconciled and repaired here (2026-09-07 04:07 KST)

C0 on V31: codex PASS, kimi PASS. Gate on V31: codex `PREREG_UNSOUND` (two new findings, one cosmetic; PRIOR_FINDINGS_CLOSED=YES —
every V30 item closed), **kimi `PREREG_SOUND`** (no findings; PRIOR_FINDINGS_CLOSED=YES); both blind intact, C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES. Reconciled BY TOPIC (`R3C2_V31_GATE_RECONCILIATION_20260907.md`, every label swept programmatically); all routine,
all repaired here and in the tools (kit: 182 controls, 63 deletion probes, PASS): `merge` preserves the alternative branch's
`origin_search` as `origin_search_alt` when that branch uses `ORIG_SILENT`, and `audit compare` checks the search belonging to the
matched branch, so a supported `ORIG_SILENT` alternative no longer fails and the verdict is independent of seat order (codex F1); the
search is compared as JSON structure, so key order cannot change a verdict (codex F2); the kit README states the probe contract as it
is — a probe kills its negative, or, where an authoritative guard overlaps the neutralised diagnostic, shows the diagnostic absent
while the guard still fails it (codex C1). **Next:** C0 and the gate on V32; then the completed plan and digest to Blanc for the
final-adoption checkpoint; the run only on Duho's fresh word.

## 10.28 V33 — SEAT-PERMUTATION INVARIANCE: the two-seat gate on V32 repaired as ONE PATTERN (2026-09-07 04:45 KST)

C0 on V32: codex PASS, kimi PASS. Gate on V32: codex `PREREG_UNSOUND` (one finding, F1: with EQUAL origin labels and different complete
`origin_search` objects, `merge` kept only seat A's search, so the identical auditor record failed in A/B order and passed in B/A order;
PRIOR_FINDINGS_CLOSED=YES), **kimi `PREREG_SOUND`** (no findings; PRIOR_FINDINGS_CLOSED=YES); both blind intact, C5_EXECUTABLE_UNDER_SCOPE=YES,
NO_MASKED_STAGE=YES. Reconciled BY TOPIC (`R3C2_V32_GATE_RECONCILIATION_20260907.md`, sweep none missing).

**Second instance of one class** (Blanc's order of 04:37): V31's codex F1 was seat-order dependence too (an `ORIG_SILENT` alternative's
search dropped). The V32 repair was a point fix with "controls in both seat orders"; the class survived it. Under the third-failure rule
this version repairs the CLASS: (1) the invariant is stated once and named in §3 — SEAT-PERMUTATION INVARIANCE, "SPI"; (2) ONE place
enforces it — `merge` chooses the primary branch by a seat-blind canonical key and preserves the other seat's complete branch whenever
anything provenance-bearing differs, so the merged ledger is a function of the set of seat records and nothing downstream can observe
seat order; (3) the property, not the fixture, is exhibited — `r3c2_spi_exhibition.py` (kit) runs every reviewer construction (both
hybrid directions, the complete alternative branch, the wrong-owner dependency, transitive propagation through another claim's
alternative, agreeing root sets with a fabricated quotation, the `ORIG_SILENT` alternative, and same-origin different searches) under
both seat orders and asserts the merged bytes and the ENTIRE audit outcome (exit code, every failure line, the whole artefact) are
equal; (4) fail-first — the same exhibition FAILS against pinned byte copies of the V32 tools (`r3c2_staged_d1d7/_v32_bytecopy/`), with
the verdict flipping on the codex construction exactly, and PASSES against the delivered tools; the whole kit re-run (184 controls,
63 deletion probes, PASS) with NO pre-existing assertion in conflict; (5) no path resisted single-point enforcement.

**Blanc's question, answered:** YES — V31's "both seat orders" controls PASSED while V32's F1 was live (the V32 kit passed 182/182 with
them). They were blind because they asserted PASS for ONE fixture in both orders, a fixture whose two seats carried DIFFERENT origin
labels (`CHOSEN` vs `UNDECLARED`), so `merge`'s `origin != origin` condition always created the alternative; they asserted the verdict,
not equality of the whole outcome, and contained no fixture with equal labels and different searches — the exact condition that the
merge predicate excluded. The exhibition now asserts whole-outcome equality across permutations for every construction.
**Next:** C0 and the gate on V33; then the completed plan and digest to Blanc for the final-adoption checkpoint; the run only on Duho's
fresh word.

## 10.29 V34 — the two-seat gate on V33 closed inside the SPI pattern (2026-09-07 05:38 KST)

C0 on V33: codex PASS, kimi PASS. Gate on V33: codex `PREREG_UNSOUND` with two findings, **kimi `PREREG_SOUND`** with none; both
PRIOR_FINDINGS_CLOSED=YES (the V32 seat-order finding closed), blind intact, C5 YES, no masked stage. Reconciled BY TOPIC
(`R3C2_V33_GATE_RECONCILIATION_20260907.md`, sweep none missing).

**codex F1 (non-cosmetic, no verdict change):** `merge` wrote its output without sorted keys, so two structurally EQUAL seat records
supplied in different JSON member order (equal canonical keys, tie broken by supply order) merged to different bytes and a different
`sealed_ledger_sha256` with the same verdict. Repaired at the ONE enforcement point: `merge` now serialises recursively with sorted
object keys (no second predicate added anywhere); the §3 sentence is replaced by codex's exact text. **codex F2 (non-cosmetic, the
exhibition):** the row labelled "hybrid direction 1" was a complete parent-only alternative (identical origin and evidence), so no true
hybrid in that direction had been constructed — a fixture defect of the lane's exhibition, disclosed as such. Repaired: that row is
relabelled and kept as the legitimate positive case; the true hybrid (A's DERIVED origin and equation evidence with B's parents, B being
CHOSEN with choice evidence) and its reciprocal are added, both required to FAIL in both orders with the unconditional "record matches
neither complete declared branch" diagnostic; every construction now asserts its expected PASS or FAIL as well as permutation equality;
the fixture writer no longer normalises member order; the complete artefact is compared with `sealed_ledger_sha256` retained and
failure lines in emitted order. Fail-first: the amended exhibition FAILS against pinned byte copies of the V33 tools on the member-order
row only and against the V32 copies as before; PASSES against the delivered tools. Kit: 185 controls, 63 deletion probes, PASS;
no pre-existing assertion conflicted. The gate brief for V33 carried one lane slip (its Q7 first line said "gate on V33" for "gate on
V32"; the next sentences named V32 correctly) — disclosed in the run log, not edited while seats ran. **Next:** C0 and the gate on V34.

## 10.30 V35 — complete provenance graphs preserved at merge: the two-seat gate on V34 (2026-09-07 06:30 KST)

C0 on V34: codex PASS, kimi PASS. Gate on V34: codex `PREREG_UNSOUND` (one non-cosmetic finding F1, one cosmetic C1), kimi
`PREREG_SOUND` (no findings); both PRIOR_FINDINGS_CLOSED=YES (the V33 findings closed), blind intact, C5 YES, no masked stage. Reconciled BY TOPIC
(`R3C2_V34_GATE_RECONCILIATION_20260907.md`, sweep none missing). Seat-permutation equality HELD on every construction codex built.

**codex F1 (non-cosmetic; a new class, not seat order):** the per-input canonical choice can COMPOSE a primary graph no seat supplied —
two acyclic seat graphs (A: x→y→r, B: y→x→r, measured root only, zero origin-label disagreements) merged to a primary view x↔y; `compute`
exited 1 instead of reporting the promised DISPUTED pair, and `audit compare`'s diagnostic root computation over that mixed view added
a mismatch even when the auditor's reconstruction equalled complete A or complete B. Repaired with codex's exact sentences (§3): `merge`
now also preserves the two COMPLETE validated seat graphs in `provenance_graphs` in seat-blind order (equal graphs once); `compute`
takes every claim's classification pair from those complete graphs and never from the mixed view — a ledger carrying alternative
branches but no graphs is REFUSED, a ledger without alternatives is itself one complete graph; the audit's unmatched-view root
computation is diagnostic only (recorded, never a mismatch), while a cycle or missing dependency in the MATCHED graph still fails.
Seat-blind ordering stays at `merge`; no downstream seat-order selection was added. Exhibition: codex's construction is built
deterministically (the fixture searches a small evidence tag until the canonical keys mix the seats, and prints the tag) and, with the
auditor equal to complete A and to complete B, must give audit PASS, `compute` exit 0 and a DISPUTED pair in both orders; `compute`'s
exit code and output now join every construction's compared outcome. Fail-first: against pinned byte copies of the V34 tools the
exhibition FAILS on the two cycle rows only, with audit [1,1] and compute [1,1] exactly as codex observed; PASSES on the delivered
tools. **codex C1 (cosmetic):** the exhibition docstring replaced by codex's exact text. Kit: 186 controls, 63 deletion probes,
PASS; pre-existing assertions in conflict: TWO, disclosed — (i) the kit's disputed-ledger fixture (V27 label / gate F4 controls) was a HAND-COMPOSED mixed ledger without provenance graphs, which V35's compute now refuses by design; the fixture is now produced by the delivered merge from two seat ledgers and the assertions are unchanged (fixture repaired, not the expectation — Blanc 03:03); (ii) the V34 fail-first control asserted that the V33 byte copies fail the exhibition on the member-order row ONLY — with the cycle rows added, the V33 copies also fail those two (the composition defect predates V33), so the control now names the exact failure set at V33 (member-order plus the two cycle rows, nothing else); the property it guarded still holds. Also removed before the kit ran: a second dispute predicate this lane had drafted beside the reachability flag (graph difference per claim) — redundant, since every graph difference merge preserves is reachable as an alternative branch, and it would have masked the propagation probe; one resolver remains. **Next:** C0 and the gate on V35.

## 10.31 V36 — MEANINGLESS-ORDER INVARIANCE: the principle widened (Blanc 07:09) and the two-seat gate on V35 (2026-09-07 07:22 KST)

C0 on V35: codex PASS, kimi PASS. Gate on V35: codex `PREREG_UNSOUND` (F1, F2), kimi `PREREG_SOUND` (no findings)`; both PRIOR_FINDINGS_CLOSED=YES (the V34
findings closed), blind intact, C5 YES, no masked stage. Reconciled BY TOPIC (`R3C2_V35_GATE_RECONCILIATION_20260907.md`, sweep none missing).

**Third instance of one principle (Blanc 07:09).** V31 F1 and V32 F1: seat order changed the verdict. V35 F2: randomized set traversal
changed the complete audit outcome. SPI, defined as invariance under permutation of the census seats, closed the first two and had nothing
to say about the third. The invariant is therefore RESTATED once in §3 as MEANINGLESS-ORDER INVARIANCE: the verdict and the whole outcome
are invariant under any ordering that carries no meaning; the known sources are enumerated (a)–(e) with seat permutation as one source
among several; enforcement is structural at each production boundary (sorted traversal of every set, dict-from-set and file-ordered
mapping in the audit; sorted keys on every JSON write; canonical primary and graph order at merge) rather than asserted per site; the
exhibition is ONE combined property over seat orders × PYTHONHASHSEED {0,1,2} × reversed record arrival × reversed rederivation member
order with whole-outcome equality, its constructions derived from the enumerated sources and not only from the reviewer counterexamples.

**codex F1 (non-cosmetic, a FALSE PASS in the direction that matters):** a matched graph cycle passing through a CHOSEN record with
parents escaped detection, because root traversal stops at any non-DERIVED origin and the closure walker suppressed revisits without
diagnosing them. Repaired with codex's exact sentence: an origin-independent graph-integrity check over every dependency edge of the
auditor's closure and of the matched sealed closure runs BEFORE root classification; its own fail-first subcase. **codex F2 (non-cosmetic):**
the cycle diagnostic varied between processes (`cycle at x` / `cycle at y`) because root recomputation iterated a set — closed by the
structural enforcement above; its own fail-first subcase (seeds 0 and 1 reproduce it on the V35 bytes). Additional subcases from the
enumerated sources: a missing dependency in the auditor's closure; several diagnostics at once (two missing dependencies and two value
mismatches) whose emitted order must be identical under every seed and order; record arrival order; rederivation member order; JSON
member order.

**Per-subcase fail-first evidence against pinned V35 byte copies** (`r3c2_staged_d1d7/_v35_bytecopy/`): F1 FAILS (verdict 0 where 1 is
required, no graph-integrity diagnostic); F2 FAILS (outcomes differ across seeds); missing-dependency FAILS (no graph-integrity
diagnostic); multi-diagnostic FAILS (no graph-integrity diagnostic); the member-order, V34 mixed-cycle and V32 same-origin-search
subcases PASS on the V35 bytes — those defects were closed earlier, and the rows are retained as controls, stated as such. The full
property PASSES on the delivered tools. ONE pre-existing control conflicted and is disclosed: the gate-3 F1 control asserted the EXACT failure set for a reconstruction that omits a dependency; with graph integrity now reported before root classification (codex's sentence) that set gains one line ("graph integrity (auditor closure): missing dependency i2 of i1"), so the control now asserts the exact new set — still an exact failure set, the expectation widened, the property unchanged. Kit: 192 controls, 63 deletion probes, PASS. **Next:** C0 and the gate on V36.

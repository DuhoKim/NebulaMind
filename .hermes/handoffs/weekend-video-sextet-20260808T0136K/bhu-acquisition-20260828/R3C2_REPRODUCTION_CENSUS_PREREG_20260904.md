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

## 2. Method — per claim, in order

1. **Extract** the printed number, its units, and the equation the paper says produces it, with file and line.
2. **List the inputs** that equation needs.
3. **Classify each input** as `PRINTED` (given in the paper), `STANDARD` (a measured constant: G, c, ħ, Planck 2018
   parameters), or `ABSENT`.
4. **Attempt the arithmetic with ADMISSIBLE inputs only** (§3's definition: origin `DERIVED` or `STANDARD`). A printed
   value whose origin is `CHOSEN` or `FITTED` is **not** admissible.
5. **Record the outcome**, per claim, as one of §3.

**A seat may not supply a value for an `ABSENT` input.** Encountering one ends that claim's attempt.

## 3. Per-claim outcomes — declared now

**The admissible input set is defined by PROVENANCE, not by location.** "Printed" says only where a value appears;
a value can be printed in the paper and still have been chosen or fitted — entry 59's `β = 1/929.25` is printed and
chosen, and under a location-based rule its downstream numbers would have counted as reproduced, readmitting exactly
what this census exists to detect. So:

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
- **`REPRO_INPUT_ABSENT`** — an input the equation needs is `ABSENT` from the paper, so the attempt stops there.
  **Name the input.** *(This class exists because the rule "a seat may not supply a value for an ABSENT input" had no
  outcome to file — a gate finding.)* Distinct from `REPRO_AFTER_CHOICE`, where a value **was** supplied and the
  number then followed.
**Candidate exclusions are not per-claim outcomes.** Every enumerated candidate passage that fails the §1
definition is recorded in a **separate exclusion ledger** with file, line, the numeral, and which excluded kind it
is (equation number, reference number, page/line number, date, or attributed-not-derived). The census denominator
is the count of **included** claims; the exclusion ledger is reported alongside it and audited under C6, so nothing
is hidden by being excluded. *(The old `NOT_ATTEMPTED` class was incoherent: §1 defines a claim by the presence of
a printed number, so an included claim could never satisfy it — a gate finding.)*

## 4. Study-level outcomes

1. **`CENSUS_COMPLETE`** — every claim carries one per-claim outcome. Report the full tally with its denominator.
2. **`CENSUS_PARTIAL`** — some claims unresolved after two attempts. Report which, and why. **INCONCLUSIVE.**
3. **`CENSUS_AUDIT_FAILED`** — the audit of §6 cannot reproduce a sampled per-claim outcome. The census is void; report
   which.
4. **`R3C2_NO_CLASS`** — a control fails **in every seat that attempted it** after two attempts.
5. **`CENSUS_DENOMINATOR_DISPUTED`** — the two enumerations disagree after two reconciliation attempts. The census
   does not proceed; the disputed candidates are listed. *(Added because the enumeration stop had no class.)*
6. **`CENSUS_CONTROL_SPLIT`** — a control fails in one seat and passes in another after two attempts. Report both
   seats' outputs and stop; **do not adopt the passing seat's result.** *(Added because this reachable state landed in
   no class.)* *(Phrased this way
   because the old `R3C_NO_CLASS` said "in both seats", leaving a control that failed twice in one seat and passed in
   the other with no class — a gap codex found.)*

**No study-level outcome is a verdict about the pattern.** §7 is where the pattern is touched, once, afterwards.


## 5. Controls, each with an exact named code

- **C1 — denominator.** Claims **included**, claims **excluded** (with the exclusion ledger of §3), and attempts made,
  all printed before any tally. *(This control previously referenced a class §3 abolished — a gate finding; the
  document has been swept for every other occurrence.)*
  `C1_DENOMINATOR_PRINTED=PASS`.
- **C2 — input ledger.** Every input classified `PRINTED` / `STANDARD` / `ABSENT`, each `PRINTED` one carrying file and
  line. `C2_INPUT_LEDGER=PASS`.
- **C3 — no substitution, machine-checked.** The input ledger is a **JSON file**, one record per input:
  `{claim_id, symbol, status: PRINTED|STANDARD|ABSENT, origin: DERIVED|CHOSEN|FITTED|IMPORTED|UNDECLARED, value,
  source_file, source_line}`. **The arithmetic may consume only records with status `PRINTED` or `STANDARD`.** A
  script asserts that every value used appears in the ledger, that no `ABSENT` record carries a value, that **each
  `PRINTED` value machine-matches the text at its cited source line**, and that **each `STANDARD` value is one of a
  closed, named list fixed here** — `G`, `c`, `ħ`, `k_B`, and the Planck 2018 TT,TE,EE+lowE+lensing values quoted with
  their published uncertainties — so "standard" cannot become a selectable family. `C3_NO_SUBSTITUTION=PASS`.
- **C4 — pattern blindness, and an honest statement of its limit.** The referee wrapper's `--add-dir` **grants**
  directories; it does not restrict them, and it necessarily grants the lane directory, **which contains the pattern
  record**. So the tooling as it stands cannot enforce blindness to a lane-resident file, and a seat's own
  declaration is self-report.

  **What is therefore done:** each seat is run from a **redacted copy directory outside the lane**, containing only
  this preregistration, the seat brief and the pinned sources, with the wrapper pointed at that directory and **not**
  at the lane. That is enforceable, and it is the control. The seat's declaration and printed path list are kept as
  secondary detection.

  **What the blind proves and does not:** it proves the seat was not given the pattern record and did not read it
  from its working directory. **It cannot prove a seat has no prior exposure from training or an earlier session** —
  nothing available here can. The record states that limit rather than implying a stronger blind.
  `C4_PATTERN_BLIND=PASS`.
- **C5 — harness, LIVE**; **C5b — no cross-lane access.** As R3A/R3B; this lane's reading tree is in scope.
- **C6 — audit, with a frozen sampling frame.** A third pattern-blind seat **first audits the full candidate and
  exclusion ledgers against every pinned source** — completeness, not just outcomes — then re-derives, without seeing
  prior work, a sample of `max(1, ceil(0.20 × N))` included claims, `N` being the sealed denominator. **The sample is
  drawn by `random.Random(seed).sample(sorted(claim_ids), k)` with the seed fixed as the first 8 hex characters of the
  sealed tally digest**, so it cannot be chosen after the fact and cannot be empty. Any outcome it cannot reproduce,
  or any ledger incompleteness, triggers §4 class 3. `C6_AUDIT_SAMPLE=PASS`.

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
this lane and reports to Duho. That relay is the custody step; the git commit alone is not, because **a local commit
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

**Amendments get a new version number and hash in §10 rather than an in-place rewrite** — the discipline failure that
made a valid access proof look unbound during R3C's gate rounds.

## 10. Version history

| version | sha256 at dispatch | change |
|---|---|---|
| V1 | `977cc127…226799` | redesign; supersedes `R3C_MAGNITUDE_CENSUS_PREREG_20260904.md` |
| V2 | `bf404b62…2ee7ba` | seven gate findings applied: interpretation excised to a seat-invisible protocol; quantitative claim defined operationally; `REPRO_INPUT_ABSENT` added; `NOT_ATTEMPTED` cannot move the denominator; enumeration tolerance set to zero; C3 given a JSON ledger; C4 made structural via a redacted packet; seal custodied in git |

## 11. Scope

No tier, warrant token, standing or stamp moves. Published sources only; nothing from another lane. Paper HOLD;
nothing outward. R3D is untouched by this document and remains not run.

R3C2_PREREG_V5_NONDEFINITIONAL_READY
| V3 | `c945c22e…a03611b` | six V2-gate findings applied: exclusions moved out of per-claim outcomes; `CENSUS_DENOMINATOR_DISPUTED` added; C4 rebuilt as fresh seat + declaration + allowlist; C3 ledger given an `origin` field, machine-matched `PRINTED` values and a closed `STANDARD` list; C6 given a frozen seed and minimum sample; the seal re-stated honestly as tamper evidence plus an external relay, with what it cannot prove said outright |

R3C2_PREREG_V5_NONDEFINITIONAL_READY
| V4 | `040762ad…3666e3` | provenance replaces location as the admissible-input test (a printed-but-chosen value is now inadmissible, which is the defect that would have let entry 59's β through); abolished class swept document-wide; `REPRO_NOT_EVALUABLE` and `CENSUS_CONTROL_SPLIT` added; `REPRO_BLOCKED` and `REPRO_INPUT_ABSENT` disambiguated; C4 rebuilt as a redacted out-of-lane working copy, with the tooling's inability to restrict reads stated outright |

R3C2_PREREG_V5_NONDEFINITIONAL_READY
| V5 | *this version* | **non-definitional only, per Blanc 21:53**: second live copy of the enumeration-dispute rule removed from §6 (it now names the class); study-level classes renumbered 1–6 after insertions left them out of order. **The core definition is untouched and awaits Duho's a/b/c/d ruling.** |

R3C2_PREREG_V5_NONDEFINITIONAL_READY

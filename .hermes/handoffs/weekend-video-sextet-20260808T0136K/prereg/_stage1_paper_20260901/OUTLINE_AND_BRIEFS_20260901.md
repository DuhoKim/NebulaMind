# STAGE-ONE PAPER — OUTLINE AND SECTION BRIEFS

**Author: Hwao. Seats draft against these briefs; Fable holds structure,
judgment and final voice.** Supersedes `PAPER_STRUCTURE_20260901.md` (which
governed draft v1) by extending it with the principal's full commission
(direction #44) and the referee's finding.

## 0. THE THESIS — one sentence, and everything serves it

> A fifteen-year-old contested claim about galaxy handedness can be re-tested
> without repeating the disputes that made it contested — by freezing the
> design, the instrument and the sign conventions before any label is read —
> and doing so reveals that the binding constraint on this class of measurement
> is not sky coverage or sample size but **human calibration capacity**, which
> we quantify.

**What the paper is:** a preregistered, blind-validated **design + instrument**
with measured machinery results and an honest terminal finding.
**What it is not:** a dipole measurement. **No handedness label was ever read.
No `A_L` is reported.** State that in the abstract and again in §1.

## 1. THE VERIFIED NUMBER TABLE — build this FIRST, cite from it only

No section may use a number absent from this table. Each row: value, meaning,
source file, and the exact line/field. The referee's finding is the reason this
exists: **the frozen floor 962 is PROSE from the preregistration, not a receipt
value** — cite the text for rules, the receipt for outcomes, never one for the
other.

Rows to establish (verify each yourself before writing; if it cannot be traced,
CUT it):

| quantity | expected | source discipline |
|---|---|---|
| parent objects | 65,060 | frozen text §2 / acquire receipts |
| retained mask | 49,211 | `acquire/positions_selected_cut.csv`, run receipts |
| bricks (selection) | 6,104 / 6,446 — **two different counts, reconcile** | selected_brickids_cut.txt vs BS-2s candidate_detail |
| Var(cos θ), **universe** | 0.445201 | frozen text — count-weighted universe |
| Var(cos θ), **selection** | 0.754664 | frozen text — **this is the leverage number** |
| all-sky reference | 1/3 | analytic; state as such |
| N_eq (frozen selection line) | 120,002.9 at 53,005 retained | frozen text |
| N_eq (realized, 3·L_ret) | 120,016.65 | `run/stagep_plan_20260901.json` |
| **N_eq = 110,983** | **NOT FOUND — do not use** | commission figure, untraceable |
| retained 53,005 vs mask 49,211 | **reconcile explicitly** | quality cut ran after selection |
| Stage-P prefix | 984/1000 | `run/stagep_checkpoints/prefix_05024.json` |
| Stage-P re-pass | 996/1000 | `run/stagep_checkpoints/final_repass.json` |
| pass floor | x ≥ 962 | **frozen text (prose rule)** — the referee's finding |
| permutations per trial | 20,000 | frozen v9 constant |
| antisymmetry | 1000/1000, 1000/1000, residual 0.0 | `run/CODEX_BS6MAP_20260901.md` |
| robustness | 5,049 = 99 × 51, zero flips | `gates/CALIBRATION_ROBUSTNESS_REHEARSAL_RECEIPT_20260831.md` **+ its caveat** |
| audit record | 703 findings, 84 seat-rounds, 177/192/334 | `gates/KNOWN_DEBT_APPENDIX.md` |
| freeze | 30 files, `d1be4a3b…`, ed25519 `nmpr-p0` | manifest + signature files |
| calibration floor | ≥270 real labels (9 strata × max(30, 3×10)) | costing memos |
| panel cost | 1,860 decisions → 38 people @50 | `CODEX_PANEL_DESIGN_20260901.md` |
| declined predecessor | 208,407 objects, Var 0.0580, N_eq 36,253, 735.9 GB | frozen text |

## 2. SECTION BRIEFS

### §1 Introduction — *the contested question* (codex; ~800 words)
The dispute, from **primary sources only** (the standing anchor-block rule:
verify from the source, never from memory — a directional claim written from
memory once inverted a whole lane here):
- **Longo 2011**: the reported dipole, its amplitude, uncertainty and
  significance — quote the paper's own figures.
- **Land et al. 2008**: the Galaxy Zoo null, and critically **the mirrored-image
  bias mechanism** they identified — this is why human labelling of handedness
  is treacherous and why our calibration term exists at all.
- **Shamir**: machine-classified positives, and what differs about that approach.
- Fifteen years unresolved. Say *why* unresolved: the disputes are about
  analyst freedom and labeller bias, not about telescope time.
Then the paper's move: freeze everything decidable in advance, and see what
remains. **Answer the referee's objection here**: explain why ordinary
reproducibility practice is insufficient for *this* parameter — a sign
convention error inverts the result silently and survives every conventional
check.

### §2 The leverage argument — *why this footprint* (codex; ~500 words)
Sensitivity comes from **where galaxies sit along the tested axis**, not raw
counts. Var(cos θ) = **0.754664** for the selection versus **1/3** all-sky;
the universe value is 0.445201 — name each. Then **the declined predecessor
design as the proof**: 208,407 objects (4× larger) but Var 0.0580 and N_eq
36,253 — *rejected before unblinding* because the audit found the leverage
absent. This is the paper's first negative result and it belongs early: it
shows the design discipline biting when the bigger, more attractive option was
on the table.

### §3 The preregistration as instrument (codex; ~700 words)
The author↔referee construction; the freeze package and its signature; the
disclosed-supersession discipline (a ruling that changes execution order is
*recorded with what it supersedes*, never silently applied); the **known-debt
appendix** — 703 findings with the honest 177/192/334 disposition split, and
the two FORM-echo limitations quoted verbatim. Argue the appendix is a feature:
a preregistration that lists what it could not close is more trustworthy than
one claiming completeness.

### §4 Methods (codex; ~900 words) — in execution order
Population/release (Branch B, the date-gated rule and its disclosed early
resolution) · sample construction and the 53,005→49,211 reconciliation ·
Stage-P exact power (each trial against its own 20,000-permutation null, no
shared reference null) · the instrument and its antisymmetry criterion · the
gain-gradient counterfactual and ratified γ grid · custody (chain, mediator,
five-gate enumeration verifier).

### §5 Results (codex; ~700 words)
Every number from §1's table with its source discipline. The four measured
results, each with its scope attached **in the same sentence**: Stage-P;
antisymmetry (synthetic); sign anchor (synthetic, REPRODUCED-LONGO as a
convention test **not** an observation); robustness (fixture-only, explicitly
not the frozen invariance outcome). Then the custody evidence: **two go-live
attempts voided by post-hoc verification before anything consumed them** —
reported as the discipline working.

### §6 The terminal finding — *the paper's spine* (kimi; ~800 words)
The frozen estimator needs `â`: human handedness accuracy on real
accepted-population objects. Every route costed and closed —
one checker (unavailable) · panel (**38 people minimum**) · external labels
(**modern Galaxy Zoo publishes winding *tightness*, not direction**; GZ1 lacks
DR10.1-south coverage, known-answer controls, and any publishable sign anchor) ·
loosening (**deletes population coverage rather than adding noise**; below 120
decisions nothing is publishable). Conclude: **the binding constraint on this
class of measurement is human calibration capacity — here quantified.** Write
it as a *result*, with its arithmetic, for the next person who attempts this.

### §7 Discussion (agy drafts, adversarial by construction; ~600 words)
What the machinery caught that ordinary practice would not: the dependency
cycle in the frozen text; the two voided go-lives; fixtures passing for the
wrong reason; paraphrase-vs-quote failures. **And the honest costs**: the
effort, the rigidity when a frozen executable contradicted a ruling, what we
would do differently. Do not let this become a victory lap.

### §8 Data and code availability (codex; short)
Frozen package, manifest, signature, pinned tools, receipts.

## 3. DRAFTING RULES (unchanged, non-negotiable)
1. Every number from §1's table, cited to its source; **rules cite the text,
   outcomes cite the receipt**.
2. No sentence extractable as a physics claim. No `A_L`. No detection language.
3. Scope caveats travel *with* their numbers, in the same sentence.
4. Anything unsourceable goes to GAPS, never into the text.
5. Negative results are results — report the halt and the declined design at
   full strength.

## 4. SEQUENCE AND PACING (burn-honest)
Fable is at 98%, resetting Friday 2026-09-05.
1. **Now:** §1 verified-number table (codex) — everything else waits on it.
2. **Then, parallel:** §1–§5, §8 (codex) · §6 (kimi) · §7 (agy).
3. **Referee pass:** agy adversarial, same standard as PAPER-REFEREE-V1.
4. **Fable final voice pass: after the Friday reset**, not before — the
   integration and prose judgment is where Fable earns its cost, and doing it
   at 2% would degrade exactly the thing worth spending it on.
**Ratify items for the principal:** title, target venue, author list.

## 5. RULED: TITLE, VENUE, AUTHORSHIP — and RASTI conformance

**Title (ruled, direction #46):**
> A Preregistered, Blind-Validated Design for Re-Testing the Longo
> Spiral-Handedness Dipole — and the Human-Calibration Limit It Reveals

Both halves carried deliberately: the title promises a DESIGN and a LIMIT,
never a measurement.

**Venue (ruled, direction #47): RASTI — RAS Techniques & Instruments.**
Conformance checked against the publisher's own current author instructions
(academic.oup.com/rasti/pages/general-instructions), not from memory:

| RASTI requirement | our conformance |
|---|---|
| Abstract **≤ 250 words**, single paragraph, stating goals/methods/new results | draft v1's abstract is ~330 words → **must be cut to ≤250 and made one paragraph** |
| Numbered sections, **Introduction first, Conclusions last** | our §8 (Data/code) currently sits last → **renumber: Conclusions becomes the final numbered section**, with Acknowledgements / Data Availability / Conflict of Interest / References unnumbered after it |
| Unnumbered **Acknowledgements, Data Availability, Conflict of Interest, References** | add all four explicitly |
| 3–6 keywords | add (e.g. methods: statistical · methods: data analysis · techniques: image processing · galaxies: spiral · surveys) |
| **No strict length limit**; shorter technical papers welcome | our ~4,000-word target is comfortably in scope |
| Scope explicitly includes **software/data-processing methods without new observational results** | this paper is squarely in scope — say so in the cover letter |
| **AI use must be disclosed in the Methods or Acknowledgements** | the ruled disclosure satisfies this exactly |
| **AI tools cannot be authors** ("cannot take responsibility") | matches the ruled sole-authorship |

**Authorship (ruled, direction #48):** Duho Kim, sole author, Department of
Astronomy and Space Science, Chungnam National University — plus an explicit
**AI methods disclosure**, which RASTI independently requires.

### §9 (new, unnumbered block) — THE AI METHODS DISCLOSURE
Write it honestly and specifically; it is part of the contribution, so neither
hide it nor inflate it. It must state:
- **What the agents did:** drafted preregistration text and paper sections;
  refereed adversarially across 84 seat-rounds producing 703 findings; built
  and verified the pinned tools; executed the gate ladder and verification
  passes; performed the costed searches that produced the terminal finding.
- **What the human did:** every ruling (γ range, terminal signature, stopping
  rule, mapping conventions, BS-2k constants, BS-1 early resolution, the BS-6
  cycle, the pre-image halt, this paper's scope); the **P0 ed25519 signature**
  under which the package is frozen; the design decisions; and **the call to
  decline the larger predecessor design before unblinding**.
- **That no AI system is an author**, per RASTI policy and because
  responsibility for the work is not delegable.
- The disclosure text itself is a **ratify item** for the principal.

**Conclusions section (new §7 or §8 per renumbering):** required by RASTI and
absent from draft v1 — must state the two results (validated pre-image design;
quantified human-calibration limit) without drifting into a physics claim.

# DRAFT — NOT ORDERED — R3-I pre-registration: is "black hole" one object across the corpus, or several?

**Status:** DRAFT, written under Duho's 2026-09-05 18:56 KST grant ("take the unstarted round-3 preregs — drafting is not
starting"). Round-3 ranked packet cluster **#5** (claude proposal; CONT 4, TRACT 4, score 16, 2–3 seat-days). Not blocked.
Nothing runs on this document. No tier, warrant token, standing or stamp moves. Paper HOLD. Nothing outward. Published
peer-reviewed sources only. Nothing from Hwao's lane, pipeline or data.

**Version:** DRAFT 1. A freeze produces `R3I_BLACK_HOLE_REFERENT_CENSUS_PREREG_2026MMDD.md` with §8 filled, C0 by two seats and
a two-seat design gate before any classification. The seat machinery is R3C2's (packet builder, two independent seats, disputes
carried, machine-matched quotations); nothing from R3C2's comparison layer is reused.

## 1. Question

The corpus calls three kinds of object "black hole": the astrophysical object with a singularity behind a horizon; a regular
object with a de Sitter or torsion core and no singularity (entries 18–21, 55, the Popławski chain); and the universe's own
interior bounded by a cosmological horizon (the "universe as black hole" entries). Whether a corpus claim about "the black
hole" transfers between entries depends on whether the word names the same thing. No study has classified this.

> **For each enumerable text, which referent does the load-bearing use of "black hole" denote, as the text itself states it —
> and do at least two incompatible referents each carry a tiered claim?**

Plainly: when these papers say "black hole", do they mean the same object? If not, which claims are about which?

## 2. Referent taxonomy (fixed now; listed alphabetically; no class added, retired or redefined without Duho's ruling)

| referent | printed marker required |
|---|---|
| `COSMOLOGICAL_INTERIOR` | the text identifies the universe, or the region inside a cosmological horizon, as the black hole |
| `REGULAR_CORE` | the text's black hole has no curvature singularity and a stated core (de Sitter, torsion, fluid shell) |
| `SINGULAR_HORIZON` | the text's black hole is the Schwarzschild/Kerr-type object with a singularity behind an event horizon |
| `UNDECLARED` | the text uses the term without any sentence fixing which of the above it means |

A text may carry more than one referent; the census records the referent of the **load-bearing** use (the one on which the
text's tiered claim rests, quoted) and separately every other referent that appears. Every classification carries a
machine-matched quotation (`repr()`-normalised, as the R3C2 packet does).

## 3. Procedure (2 seat-days)

Limb A — **enumeration.** From `R3C2_CORPUS_MANIFEST.md` (89 enumerable texts, pinned by sha256), each seat lists every text
that uses "black hole" (or a stated synonym the text defines) in a claim sentence. Denominator disputes after two reconciliation
attempts stop the study (`REFERENT_DENOMINATOR_DISPUTED`).

Limb B — **classification.** For each text, each seat independently files the load-bearing referent with its quotation and any
secondary referents. Disputes are carried as a pair (`referent`, `referent_alt`), never reconciled.

Limb C — **transfer map (lane-side, after the seats exit).** For every pair of entries where one cites the other's black-hole
claim as support, the lane records whether the referents match. This limb reads the seats' ledgers; the seats never see it.

## 4. Outcome classes (precedence top to bottom; exactly one is filed)

1. `R3I_NO_CLASS` — packet failure or a control failing in every seat.
2. `REFERENT_DENOMINATOR_DISPUTED` — enumeration disagreement survives two attempts.
3. `REFERENT_DISPUTED` — the seats disagree on the load-bearing referent of any text whose claim is tiered above
   consistency-only; report the pairs.
4. `TERM_SPLIT` — at least two distinct referents each carry at least one tiered claim, and limb C finds at least one citation
   across referents used as support.
5. `TERM_STRATIFIED` — at least two referents carry tiered claims but no cross-referent citation is used as support.
6. `TERM_STABLE` — one referent carries every tiered claim.

**Stated before ordering:** the corpus's own tiers already suggest `TERM_SPLIT` or `TERM_STRATIFIED`; the record's value is the
transfer map — which specific cross-referent citations exist. A `TERM_SPLIT` outcome is an annotation proposal, not a tier
movement.

## 5. Controls

- **C1 SOURCE_IDENTITY** — every quotation machine-matched against the pinned text; a quotation that does not match fails the row.
- **C2 POSITIVE** — two planted texts (one unmistakably `SINGULAR_HORIZON`, one `COSMOLOGICAL_INTERIOR`) must be classified
  identically by both seats.
- **C3 NEGATIVE** — a planted text with no fixing sentence must file `UNDECLARED`, not a guess.
- **C4 PACKET_REDACTED** — builder-asserted absence of custody names, engine names, study identifiers, and any sentence stating
  what the classification will be compared against (limb C stays lane-side, exactly as R3C2's ruled floor).

## 6. Seats

Blind double, two engines, packet only, ACCESS_SHA verified by the lane after exit, nothing read before exit, no edit under a
running seat.

## 7. Closed-check against prior studies

K2 classified boundary types, not referents. The warrant audit tiered claims without asking what "black hole" named in each.
No ledger entry is re-run.

## 8. Versions

| version | date (KST) | change |
|---|---|---|
| DRAFT 1 | 2026-09-05 (this file) | written; not ordered, not frozen, not gated |

R3I_PREREG_DRAFT_COMPLETE

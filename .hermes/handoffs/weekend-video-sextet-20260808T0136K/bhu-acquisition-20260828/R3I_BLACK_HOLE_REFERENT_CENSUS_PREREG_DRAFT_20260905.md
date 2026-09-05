# DRAFT — NOT ORDERED — R3-I pre-registration: is "black hole" one object across the corpus, or several?

**Status:** DRAFT, written under Duho's 2026-09-05 18:56 KST grant ("take the unstarted round-3 preregs — drafting is not
starting"). Round-3 ranked packet cluster **#5** (claude proposal; CONT 4, TRACT 4, score 16, 2–3 seat-days). Not blocked.
Nothing runs on this document. No tier, warrant token, standing or stamp moves. Paper HOLD. Nothing outward. Published
peer-reviewed sources only. Nothing from Hwao's lane, pipeline or data.

**Version:** DRAFT 3. A freeze produces `R3I_BLACK_HOLE_REFERENT_CENSUS_PREREG_2026MMDD.md` with §8 filled, C0 by two seats and
a two-seat design gate before any classification. The seat machinery is R3C2's (packet builder, two independent seats, disputes
carried, machine-matched quotations); nothing from R3C2's comparison layer is reused.

## 0. Design rules carried from R3D and R3C2 (`R3_PREREG_DESIGN_RULES_20260905.md`) — DRAFT 2

**Rule 1 — C0 first.** Before this document is gated, two seats on different engines each write a reachability exhibition:
one concrete input and the verbatim clause path for every class in §4, or UNREACHABLE with the blocking clause. The lane owner
authors none of it, repairs none of it, verifies ACCESS_SHA after exit, and gates only on PASS+PASS.

**Rule 2 — falsifier asymmetry (a design rule of §4, not a note).** `TERM_STABLE` is filed only from a positive printed artefact
for every text's load-bearing referent with its quotation. Every way the pipeline can fail lands away from it, as follows — an anchor mismatch in C1 lands on
`R3I_NO_CLASS`; a symbolic timeout or unavailable machinery in any limb lands on `REFERENT_DISPUTED` (or the study's explicit
not-evaluable class where §4 names one) for that item, never on the pass class; a script exception or an unexpected exit
status lands on `R3I_NO_CLASS` with the printed traceback; a control failing its exact expected set lands on `R3I_NO_CLASS`;
a seat disagreement on any classified row is carried as a pair and lands on the study's DISPUTED class where §4 names one,
else on `R3I_NO_CLASS`; a missing artefact is a failure, never a default. No precondition sits on the pass path that the fail
path lacks.

**Rule 3 — the cap, declared now.** After the freeze, one C0 round and one two-seat gate. Repairs are applied against both lists
together, once per version. If a gate round after the first repair returns new non-escalated, non-cosmetic findings, or if
C0 fails a second time, the lane stops, files `R3I_STOP_DIAGNOSIS_<date>.md`, and waits. Class additions, renames and
tier or warrant moves are escalated to Duho at once and never count against the cap.

**Rule 4 — every control executes and prints.** §5 below names each control's exact command, its printed artefact (resolved
command, stdout, stderr, exit status) and the exact token set that defines PASS; a control described but not executed, or a
token asserted from prose, is a defect the gate is asked to flag. Scripts: `r3i_validate.py` (schema, quotation machine-match, referent set; PASS/FAIL printed), reuse of `r3c2_build_seat_packet.py` for the packet, committed and pinned by sha256
beside this document at freeze; each has a positive and a negative form.

**Rule 5 — abort guards and the delivered read set.** Version apply chains fail-stop after every step and write at the end.
The seat's read set is exactly: `R3I_SEAT_PACKET.md`, `SEAT_BRIEF.md`, `r3i_validate.py`, `R3I_SEAT_PACKET.sha256`, `R3C2_CORPUS_MANIFEST.md`, the 89 pinned texts — each pinned in `R3I_SEAT_PACKET.sha256`; no operative command names
a tool outside that set or at an absolute path. Third-seat dispatch through the lane's dispatcher is an administrative action
of the lane owner and is not claimed executable from the packet.

**Control kit (Rule 4), committed tonight and executed:** `r3i_validate.py` (sha256 `72edb4a02a40f7cc…`) over `r3_controls_lib.py` (`ca23604af06eaf39…`), pins in `R3_CONTROL_KITS.sha256`; every control is one printed command with an exact token and exit 1 on any FAIL; planted inputs in `_tmp_r3_ctl/`.
**Kit result tonight:** `r3i_validate.py <ledger> <sources>` on three planted texts → the planted-good ledger passes 3/3; the planted-bad ledger fails on the fabricated quotation and PASSES on a genuine quotation attached to the wrong referent. That second case is the human floor stated in §2: the machine checks that the quotation exists, not what it means; the second seat and the auditor are the check on meaning, exactly as in R3C2.

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


**Executable form (Rule 4) — each line is one printed run; PASS is defined by its printed output only:**

```
/usr/bin/python3 r3i_validate.py <referent_ledger.json> ../bhu-reading-20260823/sources  → C1_SOURCE_IDENTITY=PASS only if every quotation is a verbatim substring of its cited line; every failure printed
/usr/bin/python3 r3i_validate.py _ctl/planted_singular.json ../bhu-reading-20260823/sources  and  … planted_cosmological.json  → C2_POSITIVE=PASS only if both seats' ledgers classify the planted texts identically, printed
/usr/bin/python3 r3i_validate.py _ctl/planted_undeclared.json …  → C3_NEGATIVE=PASS only if the planted text with no fixing sentence is filed UNDECLARED
/usr/bin/python3 r3c2_build_seat_packet.py  → C4_PACKET_REDACTED=PASS from the builder's own assertion, forbidden list printed
```

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
| DRAFT 2 | 2026-09-05 | Blanc's 22:33 note: the five R3D/R3C2 lessons carried in as §0 design rules (C0 first; falsifier asymmetry with the error-landing rule; declared cap; executable controls with named commands; abort guards + enumerated read set); still not ordered, not frozen, not gated |
| DRAFT 3 | 2026-09-06 | control kit written and executed (Rule 4); kit results and disclosures recorded in §0; only Duho's order is missing — plus, for R3G, the PDF-exact form of eq. 7.31 at freeze |

R3I_PREREG_DRAFT_COMPLETE

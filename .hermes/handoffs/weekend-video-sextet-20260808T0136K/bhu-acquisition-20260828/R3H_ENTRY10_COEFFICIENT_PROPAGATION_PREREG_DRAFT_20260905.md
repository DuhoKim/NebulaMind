# DRAFT — NOT ORDERED — R3-H pre-registration: does any downstream published conclusion depend on entry 10's ⅛-versus-¾ spin closure?

**Status:** DRAFT, written under Duho's 2026-09-05 18:56 KST grant ("take the unstarted round-3 preregs — drafting is not
starting"). Round-3 ranked packet cluster **#8** (claude proposal; CONT 3, TRACT 5, score 15, 2–3 seat-days; **provenance limb
blocked**, propagation limb not blocked). Nothing runs on this document. No tier, warrant token, standing or stamp moves.
Paper HOLD. Nothing outward. Published peer-reviewed sources only. Nothing from Hwao's lane, pipeline or data.

**Version:** DRAFT 3. A freeze produces `R3H_ENTRY10_COEFFICIENT_PROPAGATION_PREREG_2026MMDD.md` with §8 filled, C0 by two
seats and a two-seat design gate before any derivation.

## 0. Design rules carried from R3D and R3C2 (`R3_PREREG_DESIGN_RULES_20260905.md`) — DRAFT 2

**Rule 1 — C0 first.** Before this document is gated, two seats on different engines each write a reachability exhibition:
one concrete input and the verbatim clause path for every class in §4, or UNREACHABLE with the blocking clause. The lane owner
authors none of it, repairs none of it, verifies ACCESS_SHA after exit, and gates only on PASS+PASS.

**Rule 2 — falsifier asymmetry (a design rule of §4, not a note).** `CONCLUSION_ROBUST` is filed only from a positive printed artefact
for every (entry, quantity, conclusion) row. Every way the pipeline can fail lands away from it, as follows — an anchor mismatch in C1 lands on
`R3H_NO_CLASS`; a symbolic timeout or unavailable machinery in any limb lands on `PROPAGATION_UNTRACEABLE` (or the study's explicit
not-evaluable class where §4 names one) for that item, never on the pass class; a script exception or an unexpected exit
status lands on `R3H_NO_CLASS` with the printed traceback; a control failing its exact expected set lands on `R3H_NO_CLASS`;
a seat disagreement on any classified row is carried as a pair and lands on the study's DISPUTED class where §4 names one,
else on `R3H_NO_CLASS`; a missing artefact is a failure, never a default. No precondition sits on the pass path that the fail
path lacks.

**Rule 3 — the cap, declared now.** After the freeze, one C0 round and one two-seat gate. Repairs are applied against both lists
together, once per version. If a gate round after the first repair returns new non-escalated, non-cosmetic findings, or if
C0 fails a second time, the lane stops, files `R3H_STOP_DIAGNOSIS_<date>.md`, and waits. Class additions, renames and
tier or warrant moves are escalated to Duho at once and never count against the cap.

**Rule 4 — every control executes and prints.** §5 below names each control's exact command, its printed artefact (resolved
command, stdout, stderr, exit status) and the exact token set that defines PASS; a control described but not executed, or a
token asserted from prose, is a defect the gate is asked to flag. Scripts: `r3h_controls.py` (C1 identity, C2 entry-10 T_cr, C3 deletion probe, negative control), `r3h_propagate.py` (the factor-6 substitution and classification, one row per line), committed and pinned by sha256
beside this document at freeze; each has a positive and a negative form.

**Rule 5 — abort guards and the delivered read set.** Version apply chains fail-stop after every step and write at the end.
The seat's read set is exactly: `R3H_SEAT_PACKET.md`, `SEAT_BRIEF.md`, `r3h_controls.py`, `r3h_propagate.py`, `r3c2_timeout.py`, `R3H_SEAT_PACKET.sha256`, the five pinned entry texts (10, 39, 52, 53, 59) — each pinned in `R3H_SEAT_PACKET.sha256`; no operative command names
a tool outside that set or at an absolute path. Third-seat dispatch through the lane's dispatcher is an administrative action
of the lane owner and is not claimed executable from the packet.

**Control kit (Rule 4), committed tonight and executed:** `r3h_controls.py` (sha256 `820aa7a64fd2abbc…`) over `r3_controls_lib.py` (`ca23604af06eaf39…`), pins in `R3_CONTROL_KITS.sha256`; every control is one printed command with an exact token and exit 1 on any FAIL; planted inputs in `_tmp_r3_ctl/`.
**Kit result tonight:** `r3h_controls.py all <entry 10 text> <rows.json>` → all pass after one correction to the lane's own test rows: a six-fold change of the coefficient moves a quantity that scales as its square root (a critical temperature ∝ α^{−1/2}) by √6 = 2.45, which is BELOW the declared factor-3 threshold and files `WITHIN_PRECISION`. This is the threshold doing what it was set to do, and it means the likely shape of the result is `CONCLUSION_ROBUST` on existence claims and on square-root scales, with `ORDER_MOVES` only on quantities linear in the coefficient. Recorded before any real number is computed. The four inheriting entries' pinned files are resolved at freeze from the ledger's entry→file map (the R3C2 manifest numbers rows, not entries).

## 1. Question

K3 step 1 (`K3S1_RESULT_20260903.md`, three seats) established that entry 10 prints two values of one quantity — the
unpolarised spin-squared closure — six times apart: `⟨s²⟩ = ¾ n²` (entry 10 L113) and `s² = ⅛(ℏcn)²` (entry 10 L121; entries
9, 11). K3 steps 2–3 settled the physics (the n² form is a convention; the four-fermion term is a 2/3 correction at the bounce).
Duho's 2026-09-03 19:34 ruling annotated rows 9, 10, 11 and noted the inheritance: **rows 39, 52 and 59 carry the ⅛ prescription;
row 53 carries the ¾ prescription** (`BHU_CORPUS_SYNTHESIS_20260902.md` lines 218–226). What is untouched is **propagation**:

> **For each inheriting entry, does any printed conclusion — a number, a sign, an inequality, a stated class of behaviour — change
> when the inherited coefficient is replaced by the other printed value (a factor 6 in `s²`, hence in the torsion term `α n²`)?**

Plainly: one paper used two different numbers for the same thing. Four later papers each picked one. Would any of their
answers come out differently with the other number?

**The provenance limb** (where the ⅛ originally came from: Nurgaliev & Ponomariev 1983) is **BLOCKED** from the start — the
source is closed after exhaustive legitimate-open retries (ranked packet, "Blocked-source status"). It is filed
`PROVENANCE_BLOCKED` on day one and not attempted; nothing below depends on it.

## 2. Sources and pins

The four inheriting entries (39, 52, 53, 59) and entry 10, from the corpus ledger's entry→source map, pinned by sha256 at freeze
from `../bhu-reading-20260823/sources/`. Entry 10's pinned text: `1403.0007_clean.txt`,
`765f6280e9348517f7269459f39cc95717406fa11b0a9bb644dfdd94451bb7bc` (R3C2 manifest row 10). The four downstream pins are filled at
freeze; a draft does not pin what it has not re-verified.

Inputs the seat may use: the printed text of the five entries; STANDARD constants. No value the papers do not print. The seat
does **not** re-derive the closure (K3 did); it takes both printed values as given and propagates.

## 3. Procedure (2 seat-days; every symbolic operation through the committed 120 s wrapper)

Per inheriting entry, three steps, each with a machine-matched quotation:

Step 1 — **Locate the inheritance.** Quote the sentence where the coefficient enters (the ⅛ or ¾, or the `α = (9/16)κ(ℏc)²`
constant that carries it), and every downstream printed quantity whose formula contains it (e.g. a critical temperature
`T_cr ∝ α^{-1/2}`, a bounce scale factor, a minimum radius, a maximum density, a stated inequality).

Step 2 — **Propagate.** For each such quantity, recompute the printed number with the coefficient multiplied or divided by 6
as appropriate (the seat records which direction the substitution runs and why). Print old value, new value, the ratio, and
the printed precision of the original.

Step 3 — **Classify the conclusion.** For each printed conclusion resting on the quantity, file one of:
`SIGN_FLIPS` (an inequality or sign reverses), `ORDER_MOVES` (the number moves by a factor ≥ 3 and the paper states a magnitude
claim on it), `WITHIN_PRECISION` (the paper states the number to a precision the change does not exceed, or states no magnitude
claim), `NOT_TRACEABLE` (the printed text does not let the dependence be isolated). One row per (entry, quantity, conclusion).

Two seats, independent; disputes on a row carried as a pair, never reconciled by discussion.

## 4. Outcome classes (precedence top to bottom; exactly one is filed for the study)

1. `R3H_NO_CLASS` — a pre-audit control fails in every seat, or the packet fails redaction.
2. `PROPAGATION_DISPUTED` — the two seats' classifications disagree on any `SIGN_FLIPS` row after the one permitted
   reconciliation attempt; report both.
3. `CONCLUSION_SENSITIVE` — at least one row is `SIGN_FLIPS` or `ORDER_MOVES` in both seats; name the entry, quantity and
   conclusion, with the two values.
4. `CONCLUSION_ROBUST` — every traceable row is `WITHIN_PRECISION` in both seats and at least three of the four entries have
   at least one traceable row.
5. `PROPAGATION_UNTRACEABLE` — fewer than three entries yield a traceable row.

The factor-3 threshold for `ORDER_MOVES` is fixed now, before any number is computed. `PROVENANCE_BLOCKED` is filed alongside
whichever class results and does not enter the precedence.

**Stated before ordering:** the K3 chain suggests the bounce's *existence* depends on the sign of the torsion term, not its
coefficient, so `CONCLUSION_ROBUST` on existence claims with `ORDER_MOVES` on scale claims (`T_cr`, minimum radius) is the
likely shape. That would still be a real record: it says which downstream *numbers* in the corpus are six-fold soft.

## 5. Controls

- **C1 SOURCE_IDENTITY** — byte-exact anchors for entry 10 L113 and L121 and each inheritance sentence.
- **C2 POSITIVE** — entry 10's own printed `T_cr` recomputed from its printed formula and constants to printed precision before
  any substitution.
- **C3 DELETION_PROBE** — delete the inheritance sentence for one entry and require the pipeline to file `NOT_TRACEABLE` for that
  entry with the exact code set `{R3H_C3_NO_INHERITANCE_ANCHOR}` rather than proceeding on a remembered coefficient.
- **C4 HARNESS** — live `sympy` version print through the wrapper.
- **Negative control** — a planted factor of 1 (no change) must file `WITHIN_PRECISION` on every row.


**Executable form (Rule 4) — each line is one printed run; PASS is defined by its printed output only:**

```
/usr/bin/python3 r3h_controls.py c1  → C1_SOURCE_IDENTITY for entry 10 L113/L121 and each inheritance sentence, repr()-matched
/usr/bin/python3 r3h_controls.py c2  → C2_POSITIVE=PASS only if entry 10's printed T_cr reproduces to printed precision, both numbers printed
/usr/bin/python3 r3h_controls.py c3 <entry>  → must print exactly {R3H_C3_NO_INHERITANCE_ANCHOR} for that entry and exit 1
/usr/bin/python3 r3c2_timeout.py 120 -- /usr/bin/python3 -c 'import sympy; print(sympy.__version__)'  → C4_HARNESS
/usr/bin/python3 r3h_controls.py neg  → planted factor 1 must classify every row WITHIN_PRECISION
```

## 6. Seats

Blind double, two engines, packet only, ACCESS_SHA verified by the lane after exit, nothing read before exit, no edit under a
running seat. Lane's own second route for one entry sealed before dispatch.

## 7. Closed-check against prior studies

K3 steps 1–3 settled what the closure is and whether the bounce calculation is controlled; neither is re-run. K1 (stopped) and
K4 were about perturbations across the bounce, not coefficient propagation. No tier or annotation moves from this draft.

## 8. Versions

| version | date (KST) | change |
|---|---|---|
| DRAFT 1 | 2026-09-05 (this file) | written; not ordered, not frozen, not gated; provenance limb pre-filed BLOCKED |
| DRAFT 2 | 2026-09-05 | Blanc's 22:33 note: the five R3D/R3C2 lessons carried in as §0 design rules (C0 first; falsifier asymmetry with the error-landing rule; declared cap; executable controls with named commands; abort guards + enumerated read set); still not ordered, not frozen, not gated |
| DRAFT 3 | 2026-09-06 | control kit written and executed (Rule 4); kit results and disclosures recorded in §0; only Duho's order is missing — plus, for R3G, the PDF-exact form of eq. 7.31 at freeze |

R3H_PREREG_DRAFT_COMPLETE

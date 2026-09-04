# DRAFT — NOT ADOPTED — "C7 — provenance assurance", ready to drop in under either ruling

**Tori, 2026-09-04 23:35 KST, on Blanc's instruction (23:32), item 2.**
**This clause is NOT in the preregistration and is NOT pre-gated by any of R3C2's rounds.**
**No tier, token, standing or stamp moves. Paper HOLD.**

## Why this exists, and what is already live

The mechanisms of `R3C2_PROVENANCE_ASSURANCE_DESIGN_NOTE_20260904.md` are **already live clauses** in the
preregistration — M1 (cited origins) and M2 (computed transitive `root_origins`) inside **C3**, M3's audit scope and
`ORIGIN_DISPUTED` inside **C6** and **§4**, M4's external seed inside **C6** and **§7**. Blanc's item 2 is therefore
not "write the mechanism"; it is that **the mechanism has no single named control with its own code**, so nothing
asserts it as a unit and nothing can record it as `PASS`, `FAIL` or `NOT_RUN`.

That is a real gap. Every other mechanism in this study is a named control precisely so it cannot be satisfied by
being distributed across prose.

## The clause, variant (b) — if the admissibility filter stays

> - **C7 — provenance assurance, machine-checked.** A script over the input ledger asserts, and prints, all of:
>   1. **every** record carries `origin_evidence` with a reason code from the closed list, and — except for
>      `ORIG_SILENT` — a verbatim quotation that **machine-matches the text at its cited source line**;
>   2. **every** `DERIVED` record carries a non-empty `derived_from`, and `root_origins` **equals the value the
>      script recomputes** from the dependency graph — a seat-written `root_origins` fails;
>   3. the dependency graph is **acyclic**, and every id in a `derived_from` resolves to a record in the ledger;
>   4. **no consumed record has an inadmissible `root_origins` entry** — this is the admissibility rule of §3
>      enforced transitively rather than at the last step;
>   5. the audit of C6 re-derived `origin` for **100%** of claims filing a reproduction-success outcome, and for
>      `max(1, ceil(0.20 × N))` of the rest, and **every disagreement is filed `ORIGIN_DISPUTED` and printed with
>      both classifications and both quotations**.
>   `C7_PROVENANCE_ASSURED=PASS`. Any assertion failing fails the control; the script's printed output is the
>   artefact, and a claimed pass without it fails.

## The clause, variant (c) — if provenance becomes a ledger rather than a filter

Identical **except that item 4 is deleted**, and replaced by:

> 4. **every claim's `rests_on` field equals the union of its inputs' `root_origins`, recomputed by the script**;
>    the field is **recorded and reported, and never alters the reproduction outcome**.

**That single item is the whole difference between the two rulings at the control level.** Items 1, 2, 3 and 5 are
byte-identical in both variants, because they check that the provenance record is *honest and complete*, which is
required whether the record *filters* or merely *describes*.

## What this clause does not do

- It does not make `origin` objective. It makes each assignment cited, transitively closed, independently
  re-derived where an error would be invisible, and openly disputed where two blind readers differ.
- **It does not remove the seat's judgement at the leaves.** A seat can still mis-classify a leaf; what it can no
  longer do is make a chain *look* clean by classifying only its last step, or leave a disagreement unrecorded.
- It adds roughly one audit-day, concentrated on the reproduction-success class. That is priced deliberately: it is
  the class where an error changes the answer and leaves no trace.

## Adoption

**Do not adopt either variant until Duho rules on §1's definition.** Adopting (b) now would harden the wording that
is under review; adopting (c) now would pre-empt the ruling. **The clause is drafted so that the ruling selects a
variant rather than starting a drafting round** — one item changes, and the control code, artefact and audit scope
are unaffected either way.

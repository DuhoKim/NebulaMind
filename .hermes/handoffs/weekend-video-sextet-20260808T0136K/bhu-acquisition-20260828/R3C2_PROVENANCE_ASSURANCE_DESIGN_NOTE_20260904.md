# R3-C2 design note — making the provenance field something other than seat assertion

**Written 2026-09-04 22:05 KST on Blanc's instruction (22:02), item 1.** kimi's V4 finding 7 and codex's V4
finding 1 both land on the same weakness from opposite directions, and **it survives whichever way Duho rules
on a/b/c/d**, so it can be designed now.

**Nothing here moves a tier, token, standing or stamp. Paper HOLD.**

## 1. The weakness, stated exactly

The census records, for every input, an `origin` in `DERIVED | STANDARD | CHOSEN | FITTED | IMPORTED | UNDECLARED`.
Every downstream number the study reports depends on that field being right.

**But `origin` is a seat's judgement, written by the same seat that files the outcome, and audited on only a 20%
random sample.** So:

- Under option **(b)** (the wording standing today) `origin` decides *admissibility*, and therefore decides the
  per-claim outcome directly. A mis-set `origin` changes the tally.
- Under option **(c)** (drafted, unadopted) `origin` decides what the `rests_on` ledger says, and the interpretation
  step reads that ledger. A mis-set `origin` changes the interpretation.

Either way **the census's whole value rests on a field no mechanism checks.** kimi put the sharpest point on it:
the only outcome class in which a laundered value can hide is the one asserting successful reproduction, and a 20%
sample gives it an 80% escape probability.

**This is not an accusation that a seat would cheat.** It does not need cheating. `origin` is genuinely hard —
a paper often prints a number without saying whether it derived it, chose it, or took it from elsewhere — and a
seat that knows a study is about provenance has a standing temptation to resolve the hard cases in the interesting
direction without ever deciding to.

## 2. Three mechanisms, none of which requires trusting the field

### M1 — every `origin` value must cite the source line that establishes it
No bare classification. Each input record carries `origin_evidence`: the pinned source path, the line number, and
the **verbatim text** on which the classification rests, plus a **reason code**:

| code | meaning | what the verbatim text must show |
|---|---|---|
| `ORIG_EQUATION` | → `DERIVED` | the equation or derivation the paper gives for this value |
| `ORIG_CONSTANT` | → `STANDARD` | the value matches C3's closed constant list within its published uncertainty |
| `ORIG_CHOICE_STATED` | → `CHOSEN` | the paper's own words choosing, setting, adopting or assuming it |
| `ORIG_FIT_STATED` | → `FITTED` | the paper's own words fitting, tuning or calibrating it to data |
| `ORIG_CITATION` | → `IMPORTED` | the paper's attribution of the value to another work |
| `ORIG_SILENT` | → `UNDECLARED` | **the absence of any of the above.** The seat prints the search it ran |

**`UNDECLARED` is the default, not the residue.** A record may leave `ORIG_SILENT` only by producing text; the
script asserts that every non-`UNDECLARED` origin carries `origin_evidence` with a non-empty quotation that is
**machine-matched to the cited line**, exactly as `PRINTED` values already are under C3.

That converts most of the field from judgement into a citation that a later reader can check without re-deriving
anything — and it makes the hard cases *visible as hard cases* instead of silently resolved.

### M2 — provenance is transitive, and the transitivity is computed, not asserted
A value the paper derived from a value it chose is not independent of that choice. So each `DERIVED` record carries
`derived_from`: the ids of the records it was computed from. A script computes the **transitive closure**
`root_origins` — the multiset of origins at the leaves of that chain — and prints it on every record.

**`root_origins` is computed by the script from the graph; no seat writes it.** A seat can still mis-set a leaf,
but it cannot make a chain *look* clean by classifying only its last step, which is the specific laundering route
kimi found.

*(`root_origins` is a factual field. What it implies — whether a chain rooted in a chosen value is inadmissible,
or merely recorded as resting on one — is the held clause and is NOT decided here.)*

### M3 — a second seat re-derives `origin` blind, and disagreement is reported, never reconciled
The audit seat re-classifies `origin` **from the pinned sources, without seeing the first seat's ledger**, for:

1. **every** claim whose filed outcome asserts successful reproduction — the class in which an error is
   consequential and invisible, so it gets no sampling discount at all; and
2. a `max(1, ceil(0.20 × N))` sample of the remainder.

Then:

- **agreement** on an input → the record stands;
- **disagreement** → the input is filed `ORIGIN_DISPUTED` **and reported as such in the tally, with both seats'
  classification and both quotations**. It is **not** reconciled, not adjudicated, and not quietly dropped;
- if disputed inputs affect more than **10%** of included claims, the study files `CENSUS_ORIGIN_DISPUTED` and
  stops.

**Disagreement is a result, not a problem to be cleared.** If two competent blind readers cannot agree from the
paper's own text what a number's provenance is, *that is a finding about the corpus* — arguably a more interesting
one than the tally — and burying it in a reconciliation step would destroy it. This is the same reasoning that put
`CENSUS_DENOMINATOR_DISPUTED` in §4 rather than letting a disputed denominator be negotiated.

### M4 — the audit sample seed must not be grindable
codex's V4 finding 6: seeding the audit sample from the tally's own digest lets the tally producer reshape
non-semantic content until a favourable sample appears. So the seed comes from outside: **Blanc supplies it after
receipting the tally digests, and it is recorded with the receipt.** Tori cannot know it before the tally is sealed.

## 3. What this still does not do — stated rather than implied

- It does not prove a seat has no prior exposure to the corpus from training. Nothing here can; C4 says so already.
- It does not make `origin` objective. It makes each assignment **cited, transitively closed, independently
  re-derived where it matters most, and openly disputed where two readers differ.** A genuinely ambiguous case
  stays ambiguous — and is now *reported* as ambiguous instead of resolved by whoever wrote the record first.
- M3 roughly doubles audit cost on the reproduction-success class. That is the cost of the class being the one
  that matters; it is priced into the limb B estimate rather than absorbed silently.

## 4. Status

**This note is a design, not an adopted clause.** M1, M2 and M4 are folded into R3C2 V6 as amendments to C3, C6
and §7, because they are independent of the held definition. M3's *threshold and stop class* are folded in too.

What M3 audits — "every claim whose filed outcome asserts successful reproduction" — is written by that property
rather than by a class name, because the class list itself may change under Duho's ruling. Under option (b) it is
`REPRO_EXACT`; under option (c) it is `REPRO_EXACT` with `REPRO_AFTER_CHOICE` retired. **The property is stable
under every option on the table**, which is why it can be fixed now.

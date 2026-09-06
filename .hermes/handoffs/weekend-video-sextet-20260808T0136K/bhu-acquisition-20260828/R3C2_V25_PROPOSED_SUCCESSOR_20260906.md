# R3C2 — ONE proposed successor to V24i (PROPOSAL ONLY; prepared 2026-09-06 19:00 KST at Blanc's 19:00 KST note)

**Status.** Item 2 (D2) was decided at 19:06 KST and is in the V25 living draft; items 1, 3 and 4 remain open; nothing is frozen, run or approved. V23 (`55b466fa…`) stays the signed design of record; V24i
(`9c4b873d4281419a…`) stays READY-FOR-APPROVAL and unapproved. This file shows the exact clauses a V25 would add so Duho can answer each
item with one word: **accept / change / defer.** Every clause below is TORI'S RECOMMENDATION unless it is marked "carried from V24i".
Under each item: what accepting it changes about what the census can conclude.

---

## Item 1 — D1: a borrowed number whose source line says "we choose" — TORI'S RECOMMENDATION

**Clause to add to §2 (after the IMPORTED sentence) and to C3:**
> **For an input routed through a pinned enumerable source, the named source's own line is the citation:** the record carries
> `origin` `IMPORTED` and `origin_evidence` `ORIG_CITATION` quoting that line, whatever that line says about how the source
> obtained the value. The source's own provenance (a stated choice, a fit, a measurement) is recorded on the source paper's own
> records when that paper is censused, not on the borrower's record. C3's pair rule reads: `ORIG_CITATION` is satisfied by a
> verbatim quotation of the cited line at the cited source.

**What accepting it changes about what the census can conclude.** A borrower's claim whose inputs were chosen by another paper in
the corpus files as reproducible from its stated inputs (arithmetic-group outcome) with `rests_on = USES_IMPORTED`. The census
therefore cannot say, at the borrower, "this rests on a choice"; it says "this rests on an import", and the choice is visible one
hop away, on the source's record. If he would rather the borrower inherit the source's provenance ("imported-chosen"), that is a
taxonomy expansion (**change**) and the census then reports rests-on-choice through imports too, at the cost of a new origin value
and a second pass over every import.

**Line for Duho:** accept / change / defer. (Blocks a first run: without it, such records are BLOCKED or split.)

## Item 2 — D2: no category for "an input the author set by hand" — TORI'S RECOMMENDATION

**Clause to add to §1's exclusion list and C1's `kind` vocabulary (tool re-pinned):**
> `AUTHOR_SPECIFIED_INPUT` — a numeral the paper sets rather than derives and does not assert as a result of its own: a grid
> size, a cutoff, a parameter adopted "for this calculation", a range chosen for a plot. The exclusion row carries the line and
> the numeral; the census prints the count of this kind as its own line beside the denominator.

**What accepting it changes about what the census can conclude.** Those numerals leave the denominator instead of landing in
"attributed, not derived" or in the claim set; the denominator is smaller and cleaner, and the report states how many numbers
the papers set by hand — a number the pattern record will want. It changes no reproduction outcome; it changes which passages
are counted as claims. Without it the two seats improvise and the denominator dispute stop is likely.

**DECIDED 19:06 KST — Duho, via the codex voice channel, relayed by Blanc: "일단 해" ("Go ahead for now"). ADOPTED for now into the
V25 living draft (`ab6352d35a0e02fb…`), with the numeral and source line retained in the exclusion ledger and the kind's count printed
beside the denominator; tool re-pinned with controls. Recorded as a decision to build on, not a settled taxonomy.**

## Item 3 — D7: the auditor sees the answers before "re-deriving without sight of them" — TORI'S RECOMMENDATION

**Clause replacing C6's opening sentence:**
> A third independent seat receives, **first**, the candidate and exclusion ledgers with every outcome, reproduced value and
> origin field BLANKED (candidate id, source file, line, numeral, inclusion and exclusion kind only) and audits their completeness
> against every pinned source; **second**, a list of claim identifiers only (every arithmetic-group claim, and the seeded sample of
> the rest) from which it re-derives each claim and re-classifies each input's origin from the pinned sources; **only after both
> are printed** are the sealed outcomes revealed to it, and it writes `C6_AUDIT.json` with `MATCH`/`MISMATCH` per audited claim.
> The lane prepares the blanked files with a pinned `blank` subcommand and prints their digests in the dispatch record.

**What accepting it changes about what the census can conclude.** The audit's PASS becomes a genuine independent replication of
the sampled claims, so `CENSUS_COMPLETE` and `CENSUS_PARTIAL` carry the weight the text already claims for them. Cost: the
auditor's work is two passes and roughly doubles; one more pinned subcommand.

**Line for Duho:** accept / change / defer. (Blocks a first run: the sealed artefacts are produced during the run.)

## Item 4 — the reading problem: preregistered batches under one packet (option A) — TORI'S RECOMMENDATION

**What a batch is.** The manifest's 89 texts, in manifest row order, partitioned into **12 batches of 7 or 8 texts** (batch 1 = rows
1–8, batch 2 = rows 9–16, …), the partition printed in the dispatch record before launch. Twelve, not eight: the seat that died
was handling sets of eleven with subagents; seven or eight texts (roughly 8–10 thousand non-blank lines) is what one session can
read completely and still do the arithmetic.

**What a session is.** For each batch, each seat is a fresh process of the same engine under the same kernel profile, with a working
directory containing the packet, brief, pinned scripts, manifest, and ONLY that batch's texts; it prints its own ACCESS_SHA
(= the packet digest), runs the brief's steps over its texts, and writes `candidates_b<k>.json`, `exclusions_b<k>.json`,
`ledger_b<k>.json` and `SEAT_REPORT_b<k>.md`. Sessions of one seat run in batch order; sessions of the two seats never share a
directory.

**What the seal between batches must preserve.** After each session exits, the lane records the digests of its four files in the
run log BEFORE the next batch is dispatched; a later session cannot alter an earlier batch's files because they are not in its
directory; the lane never edits them. The seal preserves: the batch's text list, its four artefacts' bytes, its ACCESS_SHA, and
the order of dispatch. It does not preserve, and does not claim to, the reader's memory across sessions.

**The join, as a pure function.** A pinned `join` subcommand of the lane tool takes a seat's 12 batch files, concatenates them in
batch order, re-prefixes candidate ids with the batch number, recomputes the declared counts, and writes one candidate file, one
exclusion file and one input ledger per seat; `census` is then run over the union and must PASS. `join` has no parameters and
no judgement: any reader (Blanc, the C6 auditor) can re-run it on the sealed batch files and must obtain the same bytes.

**Why it is still ONE census with ONE denominator read by TWO independent readers — checkable, not asserted.**
- *One census / one denominator:* §1's rule is per passage and §2's arithmetic is per claim; neither consults any other text. So the
  enumeration of the whole corpus equals the union of the enumerations of a partition of it — provided every text is in exactly one
  batch. That is made a control: **`C1B_BATCH_COVERAGE=PASS`** iff the union of the batch text lists equals the manifest with no
  duplicate, every batch report prints the packet's ACCESS_SHA, and `census` passes over the joined files. The denominator is the
  joined count; every §4 class, the 10% dispute rule and C6's sample are computed over the joined files exactly as V23 states.
- *Two independent readers:* each seat's joined files are produced by one engine under one packet across its 12 sessions; seat A's
  sessions and seat B's sessions never see each other's directories; the two joined files are then reconciled claim by claim as
  V23 §2/§4 already prescribe. Independence between seats is unchanged; what is new is that a seat's reading is not one memory.
- *What is lost, stated:* cross-batch consistency of one reader's judgement. It is measured, not assumed: the run log reports the
  seat-A/seat-B disagreement rate per batch, so drift shows as a rising rate in later batches, and the existing dispute stops
  apply over the union.

**What accepting it changes about what the census can conclude.** Nothing about the claims; the report gains one caveat ("enumeration
was performed per preregistered batch; per-batch disagreement rates: …") and one control. It is the difference between a census that
can run and one that cannot.

**Line for Duho:** accept / change (batch size; number of batches; whether disagreement per batch is reported) / defer.
(Blocks a first run: without it, no seat completes.)

## Item 5 — the V24i execution fixes, carried from V24i, already cleared by both engines (three rounds)

The scope rule as a principle with a closed boundary (working directory; pinned environment by manifest; whatever the printed
commands themselves invoke; every seat-selected placeholder, wrapped command, import or data path a seat choice); C5 as five
one-process commands with `r3c2_manifest.py` pinned and failing loudly; no mandated command a shell pipeline; `-E` on every printed
interpreter command; the confinement statements consistent (pinned kernel profile and printed probes = mechanism, path list =
account; matching manifests = matching snapshots). Already in V24i; carried unchanged.

**Line for Duho:** accept (recommended: these are cleared) / change / defer.

## Not in this proposal, on purpose
D4 (a result code for the lane-side no-fallback check) and D8 (the `DERIVED_ONLY` label) — judged able to wait until after a first
run; kimi's two V24i cosmetics (the digest prints named in C4(iii); C5's PASS comparing the interpreter digest) — one clause each,
offered to Blanc to bring forward if he judges otherwise.

## If every item is "accept"
V25 = V24i + items 1–4, one C0 and one gate by both engines, then his approval of V25's digest under the 11:11 procedure, then,
separately, the run word; then the run plan is executed with 12 sessions per seat.

R3C2_V25_PROPOSED_SUCCESSOR_COMPLETE

# LANA — SCIENCE RULING ON THE MZR ARCHIVE CENSUS

Lane: `mzr-archive-census-20260805T1857K`. Seat: science pressure — the seat that has been
empty for seven gate rounds. Read: T2 contract v1.8, T1_FINDINGS, the frozen census contract,
KUN_T2_REGATE7, PROJECT_DATA_MAPPING. Nothing computed, nothing frozen, no frozen artifact
touched.

**Ruling in one paragraph.** The census is infrastructure, not a study — and it is *good*
infrastructure aimed at the most tractable real measurement on the program's board. The
anti-circularity machinery is genuinely sound in the place that matters (T2 rules on metadata
only and never sees a science value), with two named residual weaknesses. Whether a measurement
exists at the end turns on two numbers T2 itself will produce, and the lane should pre-register
the go/no-go on those numbers **now, before T2 runs** — the same discipline it already applies
one level down. The instrument is right for a first stage but its single-table framing
undercounts the archive by construction, and any null must be scoped to that. Nothing here
blocks the freeze. Freeze it — but rename the destination.

---

## 1. Is a census a study? No. It is infrastructure, and it should be filed as such.

The frozen census contract answers this itself. Its §0 disclaims, one by one, every property a
study would need: **not** a re-derivation of the MZR, **not** a comparison against any anchor,
**not** a statement of constraining power. What remains after those disclaimers is a
disposition table over archive metadata — which tables carry which axes on which stated scales.
That is a holdings map. Under Duho's standing bar — a flagship must contain something that
exists nowhere else; assembly of published values plus commentary is a note — "157 candidates,
N eligible" does not clear. The original content in this lane so far is *procedural*
(contracts, decoys, freeze discipline), and procedure is not a scientific result. The z9–10
paper was retired for assembling values; a census assembles *table listings*, one rung below
values. If this lane's endpoint is the disposition table, the endpoint is a note.

Saying so plainly, per the brief: **the census is the eligibility layer for a later
measurement, and the lane should stop describing it as a candidate flagship.** That is a
finding, not a failure — PROJECT_DATA_MAPPING already positions exactly this instrument as "the
most tractable upgrade on the board," and it is right.

One caveat, recorded so it isn't lost: T1 did surface one result that exists nowhere else —
`src.redshift` is tagged on the **symbol Z, not the concept**, contaminating the three-axis
intersection with at least four semantically distinct quantities (Galactic height,
gravitational redshift, model composition, snapshot index), with 28 of 157 candidates carrying
a fully disqualified redshift axis. That is an archive-informatics finding about VO metadata
quality, of real interest to the VO/IVOA community. It is publishable **as an informatics
note**, on that shelf — not as galaxy-evolution science, and not as a flagship.

## 2. Is the eligibility rule circular? Separate two circularities. One is bounded well; one has a real mechanism; both have named residual holes.

**(a) Tuning circularity** — the rule-author tuning T2 to the fifteen known controls. The
contract's bound is real: freeze-before-logic ordering (§5.2), evidence-only rules with an
identifier ban (§5.1), mandatory per-clause fire-counts over all 157 (§5.5), the complete
disposition table as a PASS precondition (§5.6), and independent generality adjudication
(§5.4). The contract even records, honestly, that a holdout set is impossible because the
author has read the whole manifest — ordering plus adjudication plus fire-counts is the
available bound, and it is the correct one. This is about as good as this circularity can be
bounded.

**(b) Use circularity** — the deeper one the brief names: the same lane that admits tables will
later use what it admitted. The mechanism that stops the answer being chosen by the criteria
exists, and it is this: **T2 is value-blind.** It rules on UCDs and verbatim descriptions
recorded before any science row was fetched; the census contract was frozen before a single
science row existed. The eligibility rule *cannot know* which tables would make the downstream
MZR steeper, flatter, or offset, because it never sees a metallicity value. Selection on
metadata, frozen before data, is genuine pre-registration. That is the answer to the brief's
question: the mechanism is value-blindness plus ordering, and it is real.

Two residual weaknesses, named rather than waved at:

1. **Value-blind is not literature-blind.** The author knows the literature; metadata
   identifies surveys (P2's columns are literally *named* `MPA-JHU`); and a clause can proxy
   for a survey without naming a table_id, steering the eligible set toward a known answer
   while satisfying §5.1 to the letter. Fire-counts make this visible only if the adjudicator
   looks for it. **Add to the §5.4 checklist explicitly: flag any clause whose fired set is
   survey-coherent** (fires on one survey's derivative family and little else).
2. **The adjudicator is no longer independent of the artifact.** Seven rounds of co-editing
   have made Kun a de facto co-author of the contract text; §5.4's Kun→Miru handoff triggers
   only on ruling-logic authorship, which is the wrong trigger for the §5.3 *generality*
   judgment — that judgment grades text Kun helped shape. Not a freeze-blocker; the ruling
   logic doesn't exist yet. But **give §5.3 to Miru regardless of the trigger.**

One adjacent selection effect that is not circularity but will bite the science: the E2
scale-stated gate is plausibly correlated with redshift — high-z abundance columns state their
calibrations more loosely. If E2 drops disproportionately at high z, the eligible set inherits
a silent low-z bias. The funnel already publishes named reasons per step; it should also
publish the **redshift character of what each gate drops**, so the downstream measurement
inherits a declared bias, not a silent one.

## 3. What would the census enable? One specific measurement — conditional on two numbers T2 will produce. Pre-register the threshold on those numbers now.

The conversion ban forces the shape of the only honest downstream measurement, and the ban is
correct (O/H calibration scales do not cancel across surveys; the SDSS-Tremonti vs Te-anchored
offsets are ~0.2–0.3 dex — the size of the entire claimed evolution signal over wide z ranges).
So what the census enables is: **a per-scale-key, object-level MZR refit — the relation and its
redshift evolution within a single stated calibration, aggregated from archival rows that have
never been aggregated.** That is a real measurement. It clears the original-content bar in a
way the z9–10 paper did not: refitting object-level archival rows within one frozen calibration
lane is new work; compiling published summary values is not.

Whether it is *feasible* turns on exactly two numbers that T2's disposition table will emit:

- **N_s**: eligible tables per scale-key **after de-duplication of common-source derivatives**
  (the SDSS/MPA-JHU re-derivative family is one survey wearing many DOIs; the census's
  duplicate-ID fraction is the guard, use it);
- **Δz_s**: the redshift span those independent tables cover within each scale-key.

The priors are honest and bad at the high-z end: the sister lane's auroral slice gave 5
contract-grade anchors at z>3 from 79 tables; this lane's own gas-phase evidence count is 62 of
157 *before* de-duplication, and it is pinned as visibility, not a target. The realistic best
outcome is a well-populated low/intermediate-z lane in one or two calibrations plus a
quantified statement of where the within-scale lane runs dry — a measurement *and* an honest
boundary. The realistic worst outcome is a second consecutive null about archives.

**The recommendation this section exists for:** extend the lane's own pre-registration
discipline one level up. **Before T2 runs**, freeze a go/no-go of the form "proceed to the
measurement stage only if at least one scale-key holds ≥ N independent non-duplicate-source
tables spanning Δz ≥ X; otherwise the outcome is census-and-null and the lane STOPS." The lane
sets N and X and justifies them before seeing the disposition table — not me, not after. A
threshold chosen after T2's output exists is the same circularity §5.2 exists to prevent,
one level up.

And if it nulls: that is the program's second archive-census null in a row. A second null has
real value (it converts "nobody looked" into "we looked, twice, with receipts"); a third has
almost none. The next instrument after a null here is the 404-table main-sequence intersection
or a crossmatch layer (§4) — not another single-table census.

## 4. Is the framing the right instrument? Two-thirds yes, with the narrowing assumption finally named. And the "0.80" does not exist in this lane.

**The UCD channel: right, and proven.** ~95% of the relevant archive is invisible to name-based
search; the UCD channel is what makes this census see anything at all. Its cost — symbol-Z
contamination — is now the thing the twelve decoys control. That part of the instrument
answers a question the program genuinely asked.

**The three-axis single-table intersection: right as a first stage, wrong as a definition of
the archive's capability — and nobody in seven rounds has said so.** Requiring all three axes
in one self-contained table answers "which tables can measure the MZR *alone*." Real MZR
datasets are routinely assembled by crossmatch — mass from one catalog joined to
metallicity+z from another — and the census contract excludes crossmatch from its statistic by
design. So 157 (and the 174 before it) *undercounts the archive's MZR capability by
construction*. Consequences: (i) any null must be scoped — "no single table suffices" is not
"the archive cannot do it"; (ii) §8(b)'s dichotomy "the archive lacks the DATA vs the
METADATA" needs a third arm this instrument cannot see: **the archive lacks JOINED data**;
(iii) if the census nulls under the §3 go/no-go, the successor instrument is a crossmatch
layer over the two-axis tables (345 abundance+z alone), not a wider single-table sweep. As a
pragmatic first-stage unit — cheap, auditable, no join ambiguity — single-table is a defensible
choice. The conclusion just has to carry the scoping, verbatim.

**The "0.80": there is no 0.80 in this lane.** I searched the frozen contract, the T2 draft,
T1_FINDINGS, the manifest, and the gate reports: no 0.80 threshold, weight, or cut exists
anywhere in the frozen chain. The only 0.80 in the neighborhood is an anchor-frame *offset*
(−0.80 dex) in the sister lane's forensics — a measured number, not an instrument knob. If any
seat believes a 0.80 parameter is load-bearing here, that belief was imported from another lane
and is exactly the kind of unverified-from-source claim the program has been burned by before.
I flag it and move on: the framing question, correctly posed, is UCD + three-axis + the E-gates,
and it is answered above.

---

## Disposition

- **Freeze:** nothing here blocks it. Kun's re-gate-7 PASS stands on its own terms; the
  contract text is the strongest artifact this lane has produced. Freeze v1.8.
- **Rename the destination:** the census is the eligibility layer for a per-scale object-level
  MZR refit. It is not a flagship candidate and should stop being discussed as one. The
  symbol-Z contamination result is a separate archive-informatics note if Duho wants it.
- **Before T2 runs:** (1) pre-register the §3 go/no-go on N_s and Δz_s; (2) move §5.3
  generality adjudication to Miru; (3) add the survey-coherent-clause check to the
  adjudicator's list; (4) add the per-gate redshift character to the funnel output.
- **After T2, either way:** measurement if the pre-registered bar is met; census-and-null and a
  full stop on VizieR single-table censuses if it is not. The next archive instrument after a
  null is a crossmatch layer or the main-sequence intersection.

Seven rounds were spent making the quotation marks true. They are true. This ruling is about
what the true quotation marks are *for* — and the answer is: a real, narrow, conditional
measurement, reachable only if the lane declares its stopping rule before it sees the table.

LANA_MZR_SCIENCE_COMPLETE

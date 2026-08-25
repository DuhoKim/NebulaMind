# RETIRED (settled) — LANA — output redesign: publishing the result without a derived catalogue

**RETIRED from the decision list 2026-08-25 (Blanc, on Duho's review): This file records the EXECUTION of a ruling Duho had already given (its own first line: 'Per Duho's decision'), re-gated by Kun as required. Nothing here was ever awaiting him.**


**Lana (science / claim-boundary seat), 2026-08-14.** Per Duho's decision: redesign the published
output so derived-catalogue publication is not required, rather than seek permission; Kun's gate
permits exactly this *"if that redesign is explicitly re-gated."* Documentation/design only — no
rows, positions, images, chirality, or sky statistics touched. **Timing statement, explicit so
nobody later mistakes this for a post-hoc change: K-8 is NOT tripped. No real-sky statistic has
been computed anywhere in this program; this amendment is made at the only safe time — before the
run.** No freeze, publication, acceptance, commit, or push; Duho owns acceptance; Kun re-gates.

**Verdict up front: the redesign is viable and does not weaken the test.** Falsifiability is
untouched (every decision region operates on aggregates that were always going to be published);
what the catalogue carried was third-party *reuse* and *bulk re-analysis* convenience, and §3's
commitment-hash + rebuild mechanism replaces the *checking* function fully while §4 names honestly
what reuse remains lost.

---

## 1. The published artifact set — exhaustive

**In the paper:**
P1. M̂ (monopole) with interval — reported first, per F-2.
P2. D̂(n̂_L), permutation p (N_perm = 100,000), Â = 3·D̂, Â_c = Â/(2a−1) with a and its interval.
P3. The F-6 decision, verbatim category, with every threshold as frozen; if null-consistent, the
    3σ upper limit on |Â_c|.
P4. The BS-9 evaluated-constants table (σ_D, σ_ours, σ_comb, F-7 floor, band, null UL) at final N
    and hand-checked a.
P5. Secondary: D̂ at Shamir's axis, interval only (K-14: no decision language); the free-axis scan
    summary (global-maximum statistic and its permutation-calibrated significance).
P6. The selection funnel: object counts surviving each frozen cut (aggregate integers), abstention
    and mirror-pair-exclusion counts, final N_accepted.
P7. Attenuation: per-stratum a (9 strata) with Wilson intervals; stratum-level confusion aggregates
    from the hand check (never the 500 per-object rows).
P8. Covariate battery outputs: per-covariate L_C with thresholds, Layer-B AUC and LR results,
    Holm-corrected flags; CB-7 coupling bound B and its components (M̂, Dip(sens), Dip(abst)).
P9. Negative controls: C1 mirror-run count-swap totals and D̂-negation check; C3 values at −n̂_L
    and the two orthogonal axes; C6 splits (D̂ per depth tertile / hemisphere / size tertile) with
    heterogeneity χ²; NC-7 shell splits and blocked-jackknife σ.
P10. Instrument receipts (synthetic — no survey licence question at all): identity 1,000/1,000,
    retention and sign-accuracy tables per S/N and inclination bin, τ, weight hashes, injected-
    source audit summary, power curves.

**In the supplement:**
S1. **Masked HEALPix maps at Nside = 32 (RING, ICRS), k ≥ 50 per pixel** (the frozen CB-2/CB-7
    mask): per-pixel accepted count, abstention fraction, mean sign(χ), and sensitivity — these
    restore coarse (≳ 3°) re-analysis to third parties and pass §2's rule.
S2. **Per-partition (67) aggregates:** counts per cut, accepted N, mean sign, abstention — the
    disagreement-localization grid for reproducers (each partition ≫ 50 objects).
S3. The full frozen pipeline (§3): selection spec, code, weights, seeds, environment, query
    templates, consumed-product hashes.
S4. **Commitment hashes (§3):** SHA-256 of the canonical per-object results file and of each
    partition's slice — published, while the files themselves are not.
S5. The preregistration, its amendments (this document's §5), and all gate receipts.
**Retained privately, unpublished, hash-committed:** the per-object results table, per-object HC
labels, and all fetched cutouts (survey terms govern any future disposition; nothing here assumes
a permission we do not have).

## 2. The aggregation threshold rule — a rule a third party can apply

**Principle: we publish statistics of OUR measurement over pre-frozen coarse cells; we never
publish anything that identifies, localizes, or re-tabulates individual survey objects, or that
could function as a row-level substitute for the survey's own products.**

A proposed table/map is publishable **iff all five hold**:
1. **k-floor:** every published cell aggregates ≥ **50** objects (the number already frozen in
   CB-2's map mask — one constant, everywhere), with sub-threshold cells masked, not merged ad hoc.
2. **Frozen cells:** cell boundaries are pre-declared, object-independent partitions (HEALPix
   pixels at declared Nside; the 67 keyspace partitions; frozen covariate deciles; the 9 HC
   strata) — never boundaries chosen after seeing values.
3. **No keys, no coordinates:** no field identifies or orders individual objects (no
   RELEASE/BRICKID/OBJID, no RA/Dec beyond the cell label itself, no per-object rows of any kind —
   including "small" ones like the 500 HC objects).
4. **Compression:** total published cells ≤ **5,000** per table (versus 832,393 objects: ≥ 160×
   compression), so no assembly of our tables approaches row-level information content.
5. **Ours, not theirs:** cell contents are statistics of our instrument's outputs (counts,
   fractions, means/variances of sign, abstention, sensitivity) — never aggregated re-tabulations
   of survey attributes (no per-cell mean magnitudes, sizes, redshifts; readers get those from the
   survey itself).

**Applied to the cases in question:** the 270,577-row per-brick table **FAILS** (rules 1, 3, 4 —
bricks are the survey's own spatial key, most contain < 50 objects, and 270k cells is
catalogue-scale information). Nside = 32 masked maps **PASS** (~4,000 footprint cells, k ≥ 50,
frozen pixels, our statistics). The Nside = 16 scan map is not an aggregation table at all — each
of its 3,072 values is a whole-sample statistic evaluated at a direction — and passes trivially.
The 67-partition grid, the covariate deciles, the 9 HC strata, C6's tertiles: all pass. The
boundary case the rule was built for — "aggregate" tables that are catalogues wearing a trench
coat — is exactly what rules 3 + 4 exclude.

## 3. The reproducibility path that replaces the catalogue

Three mechanisms, layered; together they replace the catalogue's *checking* function:

**(a) Rebuildability — the full frozen pipeline, published:** exact selection predicates
(Cuts 1–6 with the dered convention resolved), pinned product identifiers and versions (DR10.1
sweeps under `10.1/`, `10.1-photo-z`, post-Dec-2023 brick summary), SHA-256 of every consumed
file, query templates, the cutout request template with frozen parameters, the classifier source,
**frozen weights** (file sha `83008c1c…`, canonical `1075a4d9…`), the synthetic training generator
with master seed `LONGO-AMPLITUDE-FREEZE-M1` and the per-image seed schedule (weights are
independently *retrainable*, not just reusable), the venv spec, the WCS/parity audit code with the
injected-source harness, and the statistics pipeline with its seeds. The survey products are
public and anonymously accessible (Tori's binding: no account, no click-through), so a reproducer
needs no permission we lack — they need effort.

**(b) Verifiability without disclosure — commitment hashes:** we publish the SHA-256 of the
canonical per-object results file (fixed schema, sorted by the survey row key) and of each of the
67 partition slices. A group that rebuilds the inputs and runs the published pipeline can verify
**byte equality** with our result without us distributing a single row; if they disagree, the
partition hashes plus S2's partition aggregates localize the disagreement to ~12k-object slices
and to specific cut stages. This is stronger than eyeballing a downloaded table: it is an
all-or-nothing integrity check with a built-in bisection path.

**(c) Cheap spot-checks:** checking *individual* objects never needed the catalogue: fetch that
object's cutout (public), run the published frozen classifier locally, compare with the published
aggregate behaviour. Twenty objects is minutes of work. The catalogue's real convenience was bulk,
not spot.

**The honest cost to a reader:** full reproduction means fetching ~832k cutouts (order 10² GB at
polite rates — days, not minutes) and running the pipeline, versus downloading a table in
seconds. That cost is real, is borne by the reproducer, and is stated in the paper rather than
hidden. Partial mitigations: S1/S2 aggregates serve most re-analysis questions at zero cost, and
(b) means a reproducer's investment yields a binary verdict, not a judgement call.

## 4. What is lost — named, with substitutes where they exist

| Check the catalogue enabled | Lost? | Substitute |
|---|---|---|
| Byte-level verification of our result | No | (b) commitment hashes — strictly stronger |
| Spot-checking individual labels against images | No | (c) rebuild-at-small-n — minutes |
| Auditing our selection (dedup, cut correctness) | No | selection is deterministic from public inputs + published predicates; rebuild reproduces it exactly |
| Bulk re-analysis of our signs at ≳ 3° scales (other axes, quadrupoles, hemisphere tests) | Partially | S1 masked mean-sign/count maps support it; sub-pixel/sub-degree analyses do not survive |
| **Sub-degree or object-level reuse of our labels** (cross-matching to external catalogues, environmental studies, per-object ML) | **Yes — lost** | none from us; a third party must rebuild labels themselves via (a) |
| Re-weighting our sample under different cuts | Partially | S2 partition + covariate-decile aggregates permit coarse re-weighting; arbitrary re-cuts require rebuild |
| Auditing the hand-check per object | Yes — lost (also by our own rule 3) | per-stratum confusion aggregates (P7) + published HC protocol; the sealed-key design was already the integrity mechanism |
| Independent statistics on our abstention pattern | Mostly no | S1 abstention map at Nside = 32 |

The genuine casualties are the two marked **lost**: object-level reuse and sub-degree reuse of our
labels by third parties who do not rebuild. That is a real cost to community value, not to the
test's validity — no decision region, control, or falsification path in the preregistration
consumes anything the redesign withholds.

## 5. Preregistration amendments — current text → replacement, line by line

*(Locators are the frozen file's current lines; all quotations verbatim from
`PREREG_LONGO_AMPLITUDE_TEST_20260812.md` as read today.)*

**A1 — I-4 (lines 99–102).** Current:
> "plus paired original/mirror outputs, flip-balance, confidence/abstention deltas as
> published artifacts."
Replacement:
> "plus paired original/mirror outputs, flip-balance, and confidence/abstention deltas — published
> in full for synthetic receipts; for real-sky objects, published as aggregate counts and deltas
> under §F-10, with the per-object mirror file hash-committed (§F-10.c), never distributed."

**A2 — I-2 (line 88).** Current:
> "Disagreement rates on jointly-accepted objects are published."
Replacement:
> "Disagreement rates on jointly-accepted objects are published as rates and per-partition
> aggregates under §F-10; the per-object disagreement list is hash-committed, not distributed."

**A3 — §7 (lines 205–206).** Current:
> "are published with the full receipt set."
Replacement:
> "are published with the full receipt set as bounded by §F-10 (aggregate artifacts P1–P10 and
> S1–S5; per-object files hash-committed, never distributed)."

**A4 — BS-1 register row (line 219).** Current validity text:
> "licence permits derived-catalogue publication"
Replacement:
> "licence permits the §F-10 aggregate output set (no derived per-object catalogue is published;
> CC BY 4.0 image scope is not relied on for any published artifact; survey acknowledgment and
> citation obligations per Tori's binding §3.2 carried in full)"

**A5 — new frozen section F-10 (inserted after F-9).** Text:
> "**F-10 Output boundary (licence-scoped, frozen before any real-sky statistic).**
> (a) Published artifacts are exactly P1–P10 and S1–S5 of `LANA_OUTPUT_REDESIGN_20260814.md`.
> (b) A table or map is publishable iff it satisfies all five conditions of that document's §2
> (k ≥ 50 per cell; frozen object-independent cells; no per-object keys, rows, or coordinates;
> ≤ 5,000 cells per table; contents are statistics of this study's own measurements). (c) The
> canonical per-object results file and its 67 partition slices are SHA-256 hash-committed in the
> publication; the files themselves are retained unpublished. (d) No per-object quantity derived
> from survey pixels or rows is distributed in any artifact of this study. (e) This boundary was
> frozen before any real-sky statistic existed; altering it after any real-sky statistic falls
> under K-8."

**A6 — HC-4 (line ~167 region, "propagated as σ(2a−1) …").** Append:
> "Hand-check publications are per-stratum aggregates only (§F-10); the per-object HC table and
> sealed key are retained unpublished and hash-committed."

No other frozen line references publication of per-object material (NC-1's C1 text at lines
201–205 specifies count-swap and D̂-negation — already aggregate; unchanged).

## 6. Does the redesign weaken the test? — the assessment the brief demands

**Falsifiability: unchanged.** Every F-6 decision input, every INCONCLUSIVE trigger, every control
(C1–C6, NC-7, CB battery) is an aggregate that P1–P10 publish in full.
**Referee checking: unchanged in kind, cheaper in one way, costlier in another.** Spot checks are
minutes (§3c); integrity checking is *stronger* than table inspection (§3b); full independent
reproduction costs days of data fetching that the catalogue would not have saved anyway (a reader
who distrusts our labels must rebuild them regardless — the catalogue only ever helped the reader
who *trusted* our labels and wanted to reuse them).
**Community reuse: genuinely reduced** (§4's two lost rows), and the paper should say so in its
data-availability statement rather than euphemise.
**Net: viable.** The redesign holds the preregistration's epistemics intact and converts a
permission we do not have into a cost we honestly disclose.

— Lana, 2026-08-14. Design only; amendments await Kun's re-gate; Duho owns acceptance.

# DR11 migration — decision record

**Duho decided 2026-08-16: go with DR11.** Prompted by Dustin Lang (Legacy Surveys): *"We have
just released our DR11, which expands the area significantly. You may want to grab that instead of
DR10."*

This record establishes what is known, what the switch costs, and — most importantly — the
condition under which the switch is legitimate rather than a preregistration failure.

## Facts established about DR11 (directory listings and HEAD only; zero data bytes)

Same tree layout as DR10: `dr11/south/coadd/<AAA>/<BRICK>/`, `survey-bricks-dr11-south.fits.gz`,
`tractor/`, `sweep/`. Additionally carries a `north/` tree and 90prime/mosaic CCD tables at top
level, where DR10 south was DECam-only.

**Per-brick checksums exist, on the same pattern**: `legacysurvey_dr11_south_coadd_<AAA>_<BRICK>.sha256sum`,
58 entries, including `image-r`. Bands present in the sample: g, r, i, z, W1-W4.

**And they are fresh — this is the material difference from DR10:**

    AAA   BRICK       checksum written        image-r written
    000   0001m002    23 May 2026 02:21      11 Mar 2026 04:02
    092   0920m032    23 May 2026 11:31      18 Mar 2026 01:51
    145   1450m032    23 May 2026 15:46      30 Apr 2026 02:36
    203   2030m062    23 May 2026 21:53      01 May 2026 05:55
    261   2610m062    24 May 2026 04:01      22 Mar 2026 16:59
    355   3550m062    24 May 2026 12:16      29 Mar 2026 10:09

One sequential pass of ~34 hours, and **every checksum postdates the images it covers** by 3-10
weeks. Contrast DR10: checksums Nov 2022, in-place replacements Sept 2023 — ten months later,
never demonstrably refreshed.

**R3 (freshness) is therefore favourable for DR11 as it stands today.** It is not permanently
solved: a future DR11.1-style in-place fix would recreate exactly the DR10 situation, and nothing
guarantees checksums would be regenerated. R3 becomes a *standing* requirement — re-verify
checksum currency at manifest time — rather than a blocking unknown.

## What survives the switch unchanged

Release-independent, because it is code and synthetic geometry:

- the adapter (`267b2a93`, byte-identical through six gates), the readstage, all four fixture
  rounds, and every Kun gate: corner repair, round-2, round-3, resampler/pixel-value equality,
  readstage/round-4, production-read lock, scheduling determinism;
- the estimator design, the sign anchor (32/32), the shared-epsilon variance treatment;
- the custody architecture and manifest-gate requirements R1, R2, R4.

**None of tonight's work is lost.** The gates test geometry and code against synthetic fixtures,
not against a particular release.

## What must be re-derived

- **the parent set.** 208,407 (dered Cut-5) came from DR10.1 catalogues. It must be recomputed
  from DR11;
- **the feasibility chain** — inclination 82.40%, retention 85.72%, spiral 18.23% — all measured
  on the DR10 parent;
- **the BRICKID keyspace** (662,174 for DR10 South) and the ~71% coverage requirement;
- **the route binding**, which names DR10.1 paths and the `dr10.1-latest-byte-bound` release tag;
- **the frozen prereg**, which requires a successor version naming DR11.

## THE INTEGRITY CONDITION — read before doing any of the above

Changing data release after freezing a preregistration is, in general, precisely what
preregistration exists to prevent. It is legitimate here for one reason and one only:

**No real-sky statistic has ever been computed. Zero cutouts fetched, zero sky statistics, K-8
untripped.** There is nothing to have peeked at, so the choice cannot have been influenced by a
result. The stated reasons — larger area, fresher checksums, and the survey team's own
recommendation — are all outcome-independent.

**That window closes the moment the first real statistic runs.** After that, a release change
voids the run under K-8. This migration must therefore complete, and re-freeze, before any real
data is touched.

**The rule that keeps it honest:** the frozen selection cuts must carry over to DR11 **verbatim**.
Cut 4 `dered_mag_r < 17.7`, Cut 5 `shape_r > 1.5`, and every other frozen criterion apply
unchanged. If the DR11 parent count comes out different — and it will, the area is larger — that
is the answer, not a prompt to adjust anything.

**Do not re-tune a cut because a count came out inconveniently.** That is the door through which
p-hacking enters a project that has otherwise been careful all the way down. If a cut genuinely
must change for a DR11-specific reason, it is a separate, argued, gated decision with its reason
recorded — never a quiet adjustment folded into a migration.

## Ordered plan

1. Establish what DR11 actually changed: area, depth, band coverage, whether DR10.1's sub-blob fix
   is incorporated, and whether any DR11 errata already exist. Read the release documentation.
2. Recompute the parent set from DR11 catalogues under the frozen cuts, verbatim. Aggregate counts
   only — no rows, no positions.
3. Re-derive the feasibility chain on the DR11 parent, and re-check the power condition
   (`a_gate = 0.79046` at N=130,076 was computed for the DR10 parent size).
4. Successor route binding naming DR11 paths, gated by Kun, frozen with a new hash. The DR10
   binding is superseded, never edited.
5. Successor prereg naming DR11, gated, frozen. Prior versions superseded and retained at 444.
6. Re-run the manifest-gate requirements R1-R4 against DR11.

Steps 2 and 3 are the ones where the integrity condition bites. Everything in step 1 should be
established **before** any count is computed, so that no number is ever seen before the criteria
that produce it are confirmed unchanged.

## Boundary

Zero image bytes fetched. Zero FITS downloaded. Directory listings and HEAD requests only, plus
six `.sha256sum` files. No endpoint activated, no consent granted, no transfer. Frozen artifacts
unmodified. K-8 untripped.

# DR11 migration, step 1 — what actually changed

**Documentation and directory metadata only. Zero data bytes fetched. No count computed** — step 1
deliberately completes before any selection is run, so that no number is seen before the criteria
producing it are confirmed unchanged.

## Area — the reason for the switch

Southern region, strict definition (`Dec < 32.375°`), all bands jointly at ≥1 pass:

    DR10 south    15,342 deg²
    DR11 south    22,731 deg²      +7,389 deg²  (+48%)

DR10 per-band ≥1 pass, for reference: g 21,375 · r 19,885 · i 17,732 · z 20,562 deg².

**The expansion is south-only.** *"The only new data included for DR11 is in the southern region…
The northern region only includes reductions of data already included as part of DR9."* Since this
study uses south, DR11 is the relevant tree and the north is irrelevant to it.

**DR11 does not universally supersede DR10** — only the south is updated.

## Bands and footprint

South carries g, r, i, z. **r-band is present**, which is what the study cuts on and cuts out.
The declination boundary is unchanged at `Dec < 32.375°`, so the frozen footprint geometry — and
Yui's round-3 knife-edge fixtures at `+32.25` and `−89.875` — remain representative of the real
extremes rather than needing re-motivation.

New DECam data comes from the NOIRLab public archive including DES, DELVE and DeROSITA.

## Freshness — DR11 is materially better, for now

No errata are published: *"Other issues with DR11 will be listed below as they are identified."*
No in-place replacements, no DR11.1. That is consistent with the clean checksum dates measured in
`DR11_MIGRATION_DECISION_20260816.md` — every per-brick digest postdating its images by 3–10 weeks.

**But read that honestly.** DR11 was released ~3 months ago. DR10's sub-blob defect — 598 bricks —
was found roughly a year after release. An empty errata page on a young release reflects **youth,
not proven quality**. The trade is real and should be stated rather than glossed:

    DR10   mature, defects catalogued, but stale digests and a replacement history
    DR11   +48% area, fresh digests, no replacement history — and comparatively unexamined

For a preregistered study the risk has a specific shape: **if DR11 receives a DR11.1-style in-place
fix mid-study, we face DR10's exact problem while already in flight.** R3 must therefore become a
standing re-verification at manifest time and again before the run, not a one-off check.

## OPEN — is the DR10.1 sub-blob fix incorporated?

The DR11 documentation does not mention it. DR11's south was reprocessed with new data, so it
presumably ran a legacypipe carrying the fix — but *presumably* is not a basis for a frozen
preregistration, and this project has already been burned once by a directional claim written from
memory rather than quoted from source.

**This must be answered before the successor prereg is frozen.** The thread with Dustin Lang is
open and he has replied quickly twice; it is one line to ask.

## Consequences for the re-derivation (steps 2–3), stated without computing anything

A ~48% larger footprint should yield a materially larger parent set under the same cuts, which
would lower the attenuation required to reach the power condition — `a_gate = 0.79046` was computed
at `N = 130,076` from the DR10 parent, against the HC-5 floor of `a ≥ 0.85`.

**That expectation is recorded here precisely so it cannot be mistaken for a result later.** It is
arithmetic on published sky areas, not a count from data. The actual figures come from applying the
frozen cuts verbatim in step 2 — `dered_mag_r < 17.7`, `shape_r > 1.5`, and the rest unchanged —
and whatever they produce is the answer.

**No cut may be adjusted because a count comes out inconveniently.** If a cut must change for a
DR11-specific reason, that is a separate argued and gated decision with its reason recorded.

## Step 1 residual questions

1. Is the DR10.1 sub-blob fix incorporated into DR11? — ask Dustin, blocking for the freeze.
2. Are DR11 per-brick checksums current with the release as shipped? — already asked in the
   2026-08-16 follow-up; the measured dates suggest yes, but confirmation is cheap.
3. Does DR11 publish a brick-level summary (`survey-bricks-dr11-south.fits.gz` exists) with the
   same schema the frozen selection depends on? — verify before step 2, since a schema change
   would affect whether the cuts can be applied verbatim at all.

## Boundary

Documentation pages and directory listings only. Zero image bytes, zero FITS downloaded, zero
catalogues read, no count computed, no endpoint activated, no transfer. Frozen artifacts
unmodified. K-8 untripped.

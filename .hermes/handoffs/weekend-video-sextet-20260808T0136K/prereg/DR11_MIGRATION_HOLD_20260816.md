# DR11 migration — HELD at step 1. Do not proceed to step 2.

**HOLD_DR11_PHOTOZ_TABLE_NOT_DEPLOYED**

Recorded 2026-08-16. The migration is held, not reversed: the decision was sound on the facts
available when it was made, and the obstacle is a deployment timeline rather than a flaw in the
reasoning.

## What blocks it

The frozen parent selection does not run against NERSC sweep files. It runs against **NOIRLab
Astro Data Lab**:

    Catalogue  ls_dr10.tractor_s
    Photo-z    ls_dr10.photo_z, joined on (ls_id, release, brickid, objid)

**Cut 3 is `0 <= z_phot_median < 0.15`, and it is the most powerful cut in the chain:**

    Base                    2,827,055,986
    Cut 1  brick_primary, maskbits   674,896,997
    Cut 2  type<>'PSF', flux_r>0     338,508,894
    Cut 3  photo-z window              2,618,678     <- removes 99.2%
    Cut 4  dered_mag_r<17.7              238,922
    Cut 5  shape_r>1.5                   208,407

`z_phot_median` comes from `photo_z`. Queried against the Data Lab TAP service directly
(`TAP_SCHEMA.tables`), the deployed table sets are:

    ls_dr11   apflux_s, tractor, tractor_n, tractor_s                    (4 tables)
    ls_dr10   apflux, apflux_s, bricks, bricks_s, depth_summary_s,
              photo_z, psc_n, psc_s, tractor, tractor_s, wise, wise_s,
              + five x1p5 crossmatch tables                              (17 tables)

**`ls_dr11.photo_z` does not exist.** The schema `ls_dr11` is registered and the remaining tables
are advertised as "COMING SOON" on the Data Lab Legacy Surveys page.

Cut 3 therefore cannot be applied to DR11 at all. It is the redshift backbone that makes this a
low-z spiral sample comparable to Longo's z < 0.085 — without it there is no selection, not merely
a different one.

## The obvious workaround does not work

Joining DR11 `tractor_s` to DR10 `photo_z` fails on the key. The join is
`(ls_id, release, brickid, objid)` and `ls_id` encodes release, so DR10 photo-z rows cannot match
DR11 tractor rows. Cross-release matching would have to be positional — a materially different
method with its own systematics, requiring its own argued decision and gate. It is not a
substitution and must not be treated as one.

## Why this is a hold and not a reversal

`DR11_MIGRATION_DECISION_20260816.md` stands. DR11 remains the better target on the facts
established in step 1: +48% area (15,342 → 22,731 deg² all-band ≥1 pass, south), fresh per-brick
checksums postdating their images, r-band present, declination boundary unchanged. None of that has
changed. Only the availability of one table has.

If `ls_dr11.photo_z` deploys, the original plan proceeds untouched — the frozen cuts apply verbatim
and steps 2-6 run as written.

## Options, for Duho

1. **Wait for deployment.** Costs time only. Preserves the frozen cuts exactly. Timeline unknown —
   Data Lab is NOIRLab-operated, distinct from the Legacy Surveys team.
2. **Stay on DR10.1.** Full table set available today, selection reproducible now, and freshness
   (R3) becomes the only open item again. Costs the area gain.
3. **Change the redshift selection.** A separate argued and gated decision. Breaks comparability
   with the frozen design and reopens questions already settled.
4. **Compute photo-z independently.** Large new burden and a new source of unverifiable choices;
   would need its own validation and gate.

## Integrity note — why this surfaced cleanly

Step 1 was deliberately completed before any count was computed, so that no number would be seen
before the criteria producing it were confirmed unchanged. That ordering is why this was found with
**nothing to unwind**: no parent recomputed, no cut adjusted, no result seen. Had step 2 run first,
the missing table would have been discovered mid-derivation, with a partial DR11 count already in
hand — and a partial count is exactly the sort of number that starts influencing decisions it
should not.

K-8 remains untripped. No real-sky statistic has been computed under any release.

## State

Frozen DR10.1 artifacts remain the operative preregistration. No successor binding drafted, no
successor prereg drafted, nothing re-derived. All prior gates stand and are release-independent.

## Boundary

TAP_SCHEMA metadata queries and documentation only. Zero catalogue rows read, zero counts computed,
zero image bytes, no transfer, no endpoint activated.

## Update — questions sent 2026-08-16

Duho sent the combined follow-up to Dustin Lang (cc the group) asking both remaining questions:

1. does DR11 incorporate the DR10.1 sub-blob fix;
2. what is the timeline for the remaining DR11 tables in NOIRLab Astro Data Lab, `photo_z` in
   particular — stating plainly that we would be waiting on the table rather than substituting a
   different cut, and that the DR10-photo_z join is not a substitute because `ls_id` encodes release.

The Data Lab question was flagged as possibly outside his team, with an explicit invitation to
redirect rather than guess.

**The hold stands until answered.** If `photo_z` deploys, steps 2-6 of
`DR11_MIGRATION_DECISION_20260816.md` proceed with the frozen cuts applied verbatim. If it does
not, the real choice is between waiting for area we would like and running on DR10.1, where the
selection is reproducible today and only R3 (freshness) is open.

Sustained silence is itself an answer and should be treated as one rather than as a reason to keep
waiting indefinitely.

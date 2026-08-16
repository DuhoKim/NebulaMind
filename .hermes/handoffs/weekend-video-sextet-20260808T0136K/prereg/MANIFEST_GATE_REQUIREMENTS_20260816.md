# Manifest-gate requirements — addendum accumulated 2026-08-16

**This document does NOT amend `TORI_ROUTE_BINDING_20260815.md`** (SHA-256
`c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`), which stands frozen and
byte-unchanged. These are additional requirements that the **manifest-only gate (binding §11
step 4)** must satisfy before a source manifest is approved. They were discovered on 2026-08-16
and are recorded here so the reasons survive with them.

Kun gates. Duho owns acceptance. Nothing here authorizes a manifest, a transfer, or a run.

---

## R1 — Margin bricks must be verified for r-band coverage, not just primaries

**Status: OPEN, unchecked, and the reason it matters is specific.**

r-band coverage is not universal across DR10 South. Two of eight sampled bricks carry only i-band
and WISE, with 31-entry checksum manifests instead of 58 and no `image-r` at all
(`0920m225`, `2610m627` — see `CHECKSUM_FRESHNESS_TEST_20260816.md`).

The **parent set is unaffected**: `all-band nobs_g,r,z>0` loses 0 of 208,407 (0.0000%), and Cut 4
(`dered_mag_r<17.7`) and Cut 5 (`shape_r>1.5`) are r-band quantities, so a galaxy in a brick with
no r-band could never have entered the selection at all
(`TORI_PARENT_ROW_COUNT_20260812.md` §4).

**But that guarantees only the galaxy's own brick.** Every cutout near a brick edge draws from up
to four bricks — the entire corner and knife-edge apparatus gated today exists because of this.
Nothing in the parent selection constrains whether a galaxy's *neighbour* bricks carry r-band.

If a margin brick lacks r-band:

- the adapter fails closed — `coverage_zero_count` fires, so there is no silent corruption;
- but the object is **lost**;
- and the loss concentrates at survey-coverage edges, making it **position-correlated by
  construction** — the exact defect class every gate in this lane exists to prevent, arriving by a
  route none of the fixtures can see, because all fixtures are synthetic and fully covered.

**Requirement:** at the manifest-only gate, for every parent galaxy's brick, confirm that every
brick in its margin/neighbour set has an `image-r` product. Report as **aggregate counts only** —
how many parent objects have a complete r-band margin set, and how many do not. No rows, no
positions, no sky statistic. If any object has an incomplete margin set, the count must be reported
before manifest approval, not discovered during production cutting.

A non-zero count is not automatically fatal, but it must be **quantified, disclosed, and its
position-correlation assessed** before the manifest is approved. A loss whose spatial distribution
is unknown cannot be absorbed silently into an amplitude measurement.

## R2 — "Required file" must be defined against actual coverage

Binding §5.1 states a missing required file is terminal, not skippable. That rule is correct for a
file that *should* exist and does not. It must not fire on r-band that is legitimately absent
because the survey never observed it there.

**Requirement:** the manifest must distinguish, explicitly and in the sealed record, between

- **absent-by-coverage** — the survey published no `image-r` for that brick; and
- **missing-unexpectedly** — the manifest requires a file the survey does publish, and it is not
  retrievable.

The first shapes the working set and feeds R1's counts. The second stays terminal. Collapsing the
two either makes the gate unfireable or makes it fire on healthy data.

## R3 — Checksum freshness must be resolved before manifest approval

**Status: OPEN, not proven either way.**

Per-brick `.sha256sum` files were written in one sequential pass 18–26 Nov 2022. The DR10.1
in-place replacements landed the weekend of 9 Sept 2023 — ten months later. No sampled brick
deviates from the 2022 pass. Counter-signal: the top-level `legacysurvey_dr10_south.sha256sum` is
dated 22 Dec 2023, i.e. someone did regenerate checksums after the replacements, at least at top
level.

The 598 affected bricks are published as a map, not a list, and directory listings carry no mtimes,
so the tree cannot be scanned for date outliers.

**Requirement:** resolve before manifest approval, by either
(a) a direct answer from the survey — question 2 of the 2026-08-16 query went unanswered; or
(b) identifying a `RELEASE = 10002` brick and reading its checksum date, which would immediately
    break or confirm the Nov-2022 monotonic pattern.

A checksum that is internally consistent with **pre-replacement** bytes verifies cleanly while not
being the data the study intends to consume. That failure mode is silent, which is why it gates.

## R4 — Route B requires a successor binding first

Route A is blocked: the NERSC DTN cosmo collection requires a linked `nersc.gov` identity, measured
directly (`GLOBUS_ANONYMOUS_ACCESS_TEST_20260816.md`). Route B is viable — per-brick checksums exist
with 58 entries per full-band brick including `image-r`.

**Requirement:** if the manifest is built for route B, the successor route binding and its new
freeze (memo §6 amendment list) must exist and be gated **before** the manifest gate runs, not
alongside it. A manifest built against clauses that have not yet been amended is bound to a
document that forbids the channel it uses.

---

## Boundary

All of the above is analysis and requirement-setting. Zero image bytes fetched, zero FITS
downloaded, zero endpoints activated, zero consents granted, zero transfers. The frozen route
binding and the frozen V3 prereg are both unmodified. K-8 untripped.

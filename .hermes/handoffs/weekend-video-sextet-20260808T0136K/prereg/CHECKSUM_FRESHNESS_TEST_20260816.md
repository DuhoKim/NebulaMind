# Checksum freshness test — UNRESOLVED, and a separate finding that may matter more

**2026-08-16. HEAD requests and two small checksum files only. Zero image bytes fetched, zero FITS
downloaded, no endpoint activated, no transfer.**

## Question

Are the published per-brick `.sha256sum` files current with respect to the DR10.1 in-place
replacements? Dustin Lang did not answer this (it was question 2 of three; he answered 1 and 3).

## Timeline established

- **DR10.1 replacements:** 598 bricks re-processed summer 2023; *"the DR10 release directory was
  updated with the relevant files on the weekend of September 9, 2023."* Updated sources carry
  `RELEASE = 10002`.
- **Per-brick checksums:** sampled 8 bricks spread across the tree. Every checksum file falls in
  **18–26 November 2022**, and the dates climb *monotonically with directory order*:

      000/0001m002  18 Nov 2022      203/2030m062  23 Nov 2022
      037/0370m055  20 Nov 2022      261/2610m627  24 Nov 2022
      092/0920m225  21 Nov 2022      318/3180m032  25 Nov 2022
      145/1450m032  22 Nov 2022      355/3550m062  26 Nov 2022

  That is the signature of **a single sequential pass over the tree taking about eight days** —
  ten months before the replacements landed.

## Verdict: NOT PROVEN EITHER WAY. Do not record this as settled.

**Points toward stale:** the bulk pass predates the replacements by ten months, and no sampled
brick deviates from it.

**Counter-signal, and it is real:** the top-level `legacysurvey_dr10_south.sha256sum` is dated
**22 December 2023** — *after* the September 2023 replacements. Someone did regenerate checksums
post-replacement, at least at top level. Whether that pass re-walked the coadd tree is exactly what
is unknown.

**Why it could not be settled here:** the 598 affected bricks are published as a map, not a list.
Directory listings are bare `<ul>` with no mtimes, so the tree cannot be scanned for date outliers,
and 598 in ~270,000 is too sparse to hit by sampling. A replaced brick would be immediately
diagnosable — its checksum would break the November-2022 monotonic pattern — but one must be
identified first.

**What would settle it, cheapest first:**
1. Ask Dustin directly. Question 2 went unanswered and he replied within 2.5 hours; one line closes it.
2. Identify a `RELEASE = 10002` brick from the Tractor/sweep catalogs, then read that brick's
   checksum date.

## Separate finding — NOT EVERY BRICK HAS r-BAND

Two of the eight sampled bricks have **no r-band imaging at all**:

    0920m225   bands present: i, W1, W2, W3, W4   — 31 checksum entries
    2610m627   bands present: i, W1, W2, W3, W4   — 31 checksum entries

versus 58 entries for a full-band brick. Confirmed from the checksum manifests themselves, which
list no `image-r` for either.

Two of eight is not a coverage estimate — the sample is tiny and not random. But it establishes
that **r-band coverage is not universal across DR10 South**, which the acquisition design must
handle explicitly:

- the source manifest cannot assume `legacysurvey-<brick>-image-r.fits.fz` exists per brick;
- binding §5.1's "a missing required file is terminal" would fire on legitimately absent r-band
  unless "required" is defined against actual coverage rather than the brick list;
- and the open question worth checking against the frozen parent set: **can any selected galaxy
  fall in a brick with no r-band?** If the parent was selected from catalogs built on other bands,
  the answer may be yes, and the feasibility arithmetic would need revisiting. This is a question,
  not a claimed defect — it has not been checked.

## Boundary receipt

Image bytes fetched: 0. FITS downloaded: 0. Endpoints activated: 0. Consents granted: 0.
Transfers: 0. Sky statistic: none. K-8 untripped. Route binding unamended. Only HEAD requests and
two `.sha256sum` files (~6 KB each) were read.

## Update — follow-up sent 2026-08-16

Duho sent a threaded reply to Dustin Lang (cc the group) asking the two questions that remain:

1. were the per-brick `.sha256sum` files regenerated for the 598 DR10.1-replaced bricks, or do they
   still describe pre-replacement bytes — given the Nov-2022 sequential pass, the Sept-2023
   replacements, and the Dec-2023 top-level refresh;
2. are per-brick checksums published for **DR11** on the same pattern, and current with the release
   as shipped.

Question 2 was added deliberately: if the DR11 decision goes that way, the freshness question has
to be answered for DR11 rather than DR10, and asking now avoids a third round-trip.

**Until an answer arrives, R3 of `MANIFEST_GATE_REQUIREMENTS_20260816.md` stays open and the
manifest gate cannot be approved.** Do not let the existence of per-brick checksums be read as
freshness — coverage and currency are separate properties, and only coverage is established.

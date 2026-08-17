# Freeze record — successor route binding (route B, public HTTPS)

**Accepted and frozen by Duho, 2026-08-17 14:21:20 KST.**

## What is frozen

    TORI_ROUTE_BINDING_SUCCESSOR_20260817.md
    SHA-256  1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b
    mode     444

This is now the **operative acquisition route binding**. It supersedes
`TORI_ROUTE_BINDING_20260815.md` (`c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`,
mode 444), which is **retained byte-for-byte, not edited and not deleted**, as the record of what was
previously bound and why.

Verified at freeze time: the successor hash equals the hash Kun gated; the predecessor is unmoved;
both authoring and gating lanes were idle across a settle check.

## Authority

- Gated: `KUN_SUCCESSOR_BINDING_REGATE_20260817.md` (`a303e88920701aab27df56aa8d4075585a7310582d83d336aecc7d3eaf89fea9`)
  → **PASS_SUCCESSOR_ROUTE_BINDING**
- Prior hold, resolved: `KUN_SUCCESSOR_BINDING_GATE_20260817.md` → `HOLD_IMAGE_METADATA_SCOPE`
- Route decision: `ACQUISITION_ROUTE_DECISION_20260816.md` §6 (the amendment spec, executed)
- Release decision: `DR10_1_RETAINED_DECISION_20260817.md`

## Why route B was bound rather than route A

Route A is blocked by measurement: the NERSC DTN cosmo collection requires a linked `nersc.gov`
identity (`GLOBUS_ANONYMOUS_ACCESS_TEST_20260816.md`). Route B's custody condition is satisfied on
both limbs — coverage (per-brick `.sha256sum` files exist, 58 entries including `image-r`) and
currency (`CHECKSUM_FRESHNESS_RESOLVED_20260817.md`: DR10.1-replaced bricks were re-hashed 26 Jul
2023, days after their images were regenerated).

**A NERSC account request is in flight.** If it is granted, route A becomes available and requires
**no amendment to anything** — it runs under the predecessor binding as written. This freeze does not
foreclose that; it removes the dependency on it.

## What this binding changed, and the one design argument behind it

The instructed repair for `HOLD_IMAGE_METADATA_SCOPE` was a per-file image-`HEAD` pass to obtain an
exact pre-approval byte total. **Tori rejected that instruction and argued for an approved byte
ceiling instead.** Kun tested the argument and accepted it. The reasoning, preserved because it
reaches backwards into the predecessor:

- a `HEAD` `Content-Length` is the same uncorroborated server header the retrieval `GET` returns and
  must re-verify anyway — it binds nothing, the digest binds, and it can change between the two;
- obtaining it costs ~270k extra requests against the host whose tolerance is this route's binding
  constraint;
- the ceiling is **enforceable** where the exact total was informational — retrieval structurally
  cannot exceed what was approved, which the predecessor never guaranteed.

Kun's ruling: the predecessor's approved byte total *"was useful as a scale disclosure, but not as
source-byte evidence."* The design is better for having been challenged, not merely cheaper.

Stated loss, not hidden: the a-priori figure is a sample estimate with a frozen **+25% margin**, and
that margin is **policy, not a confidence interval — it is not evidence and must not be cited as
one.**

## What this authorizes

Approval under §11 step 5 now binds the sealed URL manifest hash, the exact required file count, the
approved byte ceiling with its 1,024-URL sampling receipt, and the pacing plan.

## What this does NOT authorize

No manifest has been built. No retrieval, no checksum harvest, no `HEAD` sampling, no endpoint
activation, no transfer, no sky statistic, no publication, no accepted status. Freezing a route
binding authorizes the **route**, not a run.

The manifest-only gate (§11 step 4) becomes runnable — it does not become run. R1 and R2 are carried
into §11 step 4b and remain open. R3 is closed with standing re-verification at manifest time.

## Cost accepted with this freeze

~75-hour paced checksum harvest, plus a 1,024-URL size sample, plus days of paced image retrieval.
The pacing rule is frozen and may later be tightened by survey or NERSC guidance without re-gate,
never loosened.

## Boundary at freeze time

Zero image bytes fetched. Zero checksum files harvested. Zero endpoints activated. Zero transfers.
K-8 untripped. The frozen preregistration `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
(`b06901c8a0f3a057`) is unaffected and requires no amendment.

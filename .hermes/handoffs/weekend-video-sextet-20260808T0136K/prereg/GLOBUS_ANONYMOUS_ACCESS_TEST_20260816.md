# Globus anonymous-access test — RESULT: NOT anonymous, NERSC identity required

**2026-08-16, tested in Duho's browser at his instruction. No consent granted, no transfer, no
endpoint activated, zero bytes moved.**

## What was tested

Dustin Lang's reply suggested the cosmo collection "should be accessible anonymously (though this
may change)". This tests that claim.

## Result

**The emailed link is dead.** `origin_idm65753a-0e64-11eb-81b1-0e2f230cc907` lost its `=` in mail
transit and the UUID is malformed. Globus returns:

    {"code": "EndpointNotFound",
     "message": "No such endpoint with legacy name 'm65753a-0e64-11eb-81b1-0e2f230cc907'"}

**The collection exists and is findable by name.** Searching "cosmo" in the Globus file manager:

    NERSC DTN cosmo Collab
    Subscribed Mapped Collection (GCS) on NERSC DTN Endpoint
    origin_id  cb7bdf79-dfd8-4d50-a6bd-5bec2a505935
    domain     m-856e22.c8d61e.8540.data.globus.org

Record that UUID — Dustin warned his link may change, and this is the durable handle.

**It is NOT anonymous.** Opening it returns `Missing required data_access consent`. Proceeding does
not reach a consent screen at all; it stops one step earlier at an identity wall:

> "You are required to authenticate with an identity from **NERSC (nersc.gov)** to access this
> resource. Note: If you do not have or are unable to authenticate with a required identity, the
> resource will not be accessible to you."

The OAuth request carries `link_to_one_domain=clients.auth.globus.org,nersc.gov`.

## What this settles, and what it does not

**Settled: route A requires a NERSC account.** Not inferred from documentation — measured. Dustin's
"should be accessible anonymously" does not hold for this collection. A Globus account alone is not
enough; a linked nersc.gov identity is mandatory before any listing is possible.

**Not settled:** whether a bare NERSC account suffices or `cosmo` project membership is also needed.
That cannot be tested without first holding a NERSC account, so Lana's A-side sub-question stays
open — but it is now moot for the immediate decision, since the weaker of the two conditions is
already unmet.

**Not tested:** the "Cosmo Data Collection" on NOIRLab DTN1, which appeared in the same search and
is a separate route worth checking before concluding all Globus paths are closed.

## Consequence — route B is the live path

Combined with the checksum correction (see `CHECKSUM_MANIFEST_FINDING_20260816.md`):

- **Route A** — blocked on a NERSC account, confirmed empirically.
- **Route B** — coverage condition SATISFIED; per-brick `.sha256sum` files exist with 58 entries
  per brick directory including `image-r`.

So the decision has inverted from where it stood this morning. B is viable and A is not, pending
one unanswered question: **freshness of the published digests against the DR10.1 in-place
replacements.** Dustin did not answer that, and it remains the gating fact for B.

Adopting B still requires a successor route binding and a new freeze, per memo §6.

## Boundary receipt

Consent granted: none. Identities linked: none. Accounts created: none. Transfers: 0. Endpoints
activated: 0. Bytes moved: 0. Survey data touched: 0. The frozen route binding is unamended. The
browser session was Duho's own, already authenticated to Globus; nothing was authorized in it.

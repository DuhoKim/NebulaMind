# Acquisition run — authorisation received, execution blocked

**Received:** 2026-08-15 KST. Duho, verbatim: *"authorize the acquisition run"*.
**Status: RECORDED, NOT EXECUTED.** Two blockers, both material, neither a matter of permission.

## Blocker 1 — the pipeline cannot fetch, by construction

`acquisition/nm_acquire_cutouts.py:541-542`:

```
if not dry_run and type(transport) is not MockTransport:
    raise RuntimeError("BUILD_ONLY_STOP: only exact MockTransport is allowed")
```

There is no HTTP client in the module at all — no `requests`, `urllib`, `httpx`, `socket`,
`http.client`. `MockTransport` is the only implementation of `fetch`. This is the exact property Kun
verified from source and gated as `PASS_ACQUISITION_BUILD_ONLY_GATE`.

Executing a real run therefore means **writing a real transport and deleting that guard** — new code
that deliberately removes the safety the gate certified. It requires its own gate; it is not a flag.

## Blocker 2 — 48 days at the frozen politeness policy

Frozen in `TORI_ACQUISITION_20260814.md`: maximum concurrent requests **1**, minimum interval
between request starts **5.0 seconds**.

| set | count | runtime at 1 req / 5.0 s |
|---|---:|---:|
| parent objects needing a cutout | 832,393 | **48.2 days** |
| forecast accepted after classification | 130,076 | 7.5 days |

The 130,076 figure is not reachable directly: which objects the classifier accepts is unknown until
they are classified, which requires their cutouts. The binding number is **832,393**.

Faster spacing is not a free choice — the interval is frozen, so changing it is a preregistration
amendment, and it means hitting a public service harder.

## The question this raises about the design, not the permission

Fetching 832,393 individual cutouts from a public viewer service may simply be the wrong access
pattern. The survey distributes bulk image products (bricks); retrieving the relevant bricks and
cutting locally would be far cheaper for us and far kinder to NOIRLab. PC-1 currently binds a
"single cutout route", so changing it is an amendment — but it should be *considered* before 48 days
of per-object requests are committed to.

## What is NOT authorised by this record

Nothing has been fetched. No transport exists. K-8 remains untripped and no real-sky statistic
exists. The STOP rule has not in fact been crossed — the lane stopped, as designed, at the point
where the next step would touch real galaxies.

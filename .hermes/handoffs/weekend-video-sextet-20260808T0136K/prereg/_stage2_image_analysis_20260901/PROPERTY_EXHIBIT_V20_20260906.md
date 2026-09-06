# PROPERTY EXHIBIT — option A V20 (drand-only): the seed is a function of (round, pinned key) — including the FIRST-COLLECTION case (exhibit_property_v20.py output, verbatim; real public round 6441924, BLS-verified)

```
{
 "A_two_first_collections_at_different_times": {
  "first": {
   "outcome": "ACCEPT-DRAND",
   "round": 6441924,
   "seed_hex": "68547455ba7d5000cb4b0b7fcd48c1ab36b6881d55e3ef464989659833ef3834",
   "why": null
  },
  "same_seed": true,
  "second": {
   "outcome": "ACCEPT-DRAND",
   "round": 6441924,
   "seed_hex": "68547455ba7d5000cb4b0b7fcd48c1ab36b6881d55e3ef464989659833ef3834",
   "why": null
  }
 },
 "B_bad_first_collection_then_good": {
  "first": {
   "outcome": "RETRY",
   "round": null,
   "seed_hex": null,
   "why": "fewer than 2 pinned relays verify for round 6441924 (or verified values disagree \u2014 impossible for a valid BLS signature); retry later"
  },
  "first_is_retry_no_seed": true,
  "later": {
   "outcome": "ACCEPT-DRAND",
   "round": 6441924,
   "seed_hex": "68547455ba7d5000cb4b0b7fcd48c1ab36b6881d55e3ef464989659833ef3834",
   "why": null
  },
  "later_seed_equals_A": true
 },
 "C_relay_serves_different_bytes_that_still_verify": {
  "outcome": "REFUSE-LIVE-DIFFERS-BUT-VERIFIES",
  "round": null,
  "seed_hex": null,
  "why": "a relay now serves different bytes that ALSO verify \u2014 impossible for a deterministic BLS signature; investigate"
 },
 "C_relay_serves_tampered_bytes_live": {
  "outcome": "RETRY",
  "round": null,
  "seed_hex": null,
  "why": "fewer than 2 pinned relays confirm the retained bytes live; retry later \u2014 the value cannot change"
 },
 "D_verify_same_record_twice": true,
 "pinned": {
  "chain_hash": "8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce",
  "public_key": "868f005eb8e6e4ca0a47c8a77ceaa5309a47978a7c71bc5cce96366b5d7a569937c529eeda66c7293784a9402801af31",
  "round": 6441924,
  "seed": "68547455ba7d5000cb4b0b7fcd48c1ab36b6881d55e3ef464989659833ef3834"
 }
}

EXHIBIT OK: True
EXHIBIT-DIGEST: b3754acaaf3d5ffaac76800bcdffce19168d405475b7a977f011b767a2dddd1f
```

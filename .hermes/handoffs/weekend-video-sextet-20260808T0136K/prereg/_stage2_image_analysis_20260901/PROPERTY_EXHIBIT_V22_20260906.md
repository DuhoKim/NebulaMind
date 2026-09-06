# PROPERTY EXHIBIT V22 (staged candidate; verdict v22) — executed 2026-09-06 20:59 KST, run twice

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
   "why": "fewer than 2 distinct pinned relays verify for round 6441924 (or verified values disagree); retry later"
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
 "C1_relay_serves_same_signature_in_different_bytes": {
  "live_representation_differs": [
   "https://api.drand.sh/8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce/public/6441924",
   "https://api2.drand.sh/8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce/public/6441924",
   "https://api3.drand.sh/8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce/public/6441924",
   "https://drand.cloudflare.com/8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce/public/6441924"
  ],
  "outcome": "ACCEPT-DRAND",
  "round": 6441924,
  "same_seed_as_A": true,
  "seed_hex": "68547455ba7d5000cb4b0b7fcd48c1ab36b6881d55e3ef464989659833ef3834",
  "why": null
 },
 "C2_relay_serves_tampered_bytes_live": {
  "outcome": "RETRY",
  "round": null,
  "seed_hex": null,
  "why": "fewer than 2 pinned relays confirm the retained VALUE live; retry later \u2014 the value cannot change"
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
EXHIBIT-DIGEST: 2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1
```

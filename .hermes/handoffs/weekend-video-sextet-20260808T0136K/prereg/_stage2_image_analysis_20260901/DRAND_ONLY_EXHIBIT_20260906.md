# DRAND-ONLY PROPOSAL — EXHIBIT (exhibit_drand_only.py output, verbatim; actual BLS12-381 verification of public round 6441924 under the pinned chain key; prospective-round rule from a hypothetical approval time)

```
{
 "A_prospective_round": {
  "exists_at_approval": false,
  "round": 6443748,
  "round_scheduled_utc": "2026-09-07T01:11:00Z",
  "t_approval": "2026-09-07T01:00:07Z",
  "t_pulse": "2026-09-07T01:11:00Z"
 },
 "B_tampered_signature": {
  "accepted": false,
  "bls_verifies_under_pinned_key": false,
  "randomness_is_sha256_of_signature": false,
  "round_matches": true,
  "signature_is_96_bytes_g2": true,
  "url_bound_to_chain_hash": true
 },
 "B_two_relays_agree_bytewise": true,
 "B_unbound_path_refused": true,
 "B_verify_api": {
  "accepted": true,
  "bls_verifies_under_pinned_key": true,
  "randomness_is_sha256_of_signature": true,
  "round_matches": true,
  "seed_hex": "68547455ba7d5000cb4b0b7fcd48c1ab36b6881d55e3ef464989659833ef3834",
  "signature_is_96_bytes_g2": true,
  "url_bound_to_chain_hash": true
 },
 "B_verify_api2": {
  "accepted": true,
  "bls_verifies_under_pinned_key": true,
  "randomness_is_sha256_of_signature": true,
  "round_matches": true,
  "seed_hex": "68547455ba7d5000cb4b0b7fcd48c1ab36b6881d55e3ef464989659833ef3834",
  "signature_is_96_bytes_g2": true,
  "url_bound_to_chain_hash": true
 },
 "B_wrong_key": false,
 "C_run_twice_identical": true,
 "pinned": {
  "chain_hash": "8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce",
  "dst": "BLS_SIG_BLS12381G2_XMD:SHA-256_SSWU_RO_NUL_",
  "genesis": 1595431050,
  "period": 30,
  "public_key": "868f005eb8e6e4ca0a47c8a77ceaa5309a47978a7c71bc5cce96366b5d7a569937c529eeda66c7293784a9402801af31",
  "scheme": "pedersen-bls-chained"
 }
}

EXHIBIT OK: True
EXHIBIT-DIGEST: 45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531
```

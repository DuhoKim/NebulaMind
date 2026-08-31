# CALIBRATION REHEARSAL RECEIPT — 2026-08-31

Synthetic data only; v9 read-only via the verified loader; no imagery, no χ, no γ̂.

- **S1 PASS**: verified roots loaded: gain_counterfactual_path=92cbbdf89bd2…, gain_mapping_a=8bc693ffae70…, successor_ref_v9=6a9abbbd900d…
- **S2 PASS**: 540 synthetic positions → boundaries [-0.248, 0.4441] CERTIFIED (artifact b9bc56daf1dc…, v9 6a9abbbd900d…)
- **S3 PASS**: 9/9 strata populated over 540 objects; sealed receipt 57993863a17d…; independent verifier green
- **S4 PASS**: allocate_handcheck at the frozen constants (3×9, floors 10/30, budget 500): allocated 500 labels over 12 live cells
- **S5 PASS**: replay machinery proof: one real permutation verdict (p=0.6020) under the audit-hook census; harness b6a0592bf881…
- **S6 PASS**: gain_mapping_a self-test green (the confirmed mapping, CRN identity through the frozen machinery)
- **S7 PASS**: terminal ceremony selftest green (clean signing path + both refusal paths through the real CLI)

## Tool identities at rehearsal time

- `replay_harness.py` sha256 `b6a0592bf881ca9b8b65d1fd6e716e2e845dd47c0f5c763799a40dec9966e4ac`
- `bs2f_boundary_verifier.py` sha256 `be09cc7dc292ab1e165ad78e81fe6b11f4fac81883671008f756bc5214c4404b`
- `stratum_index_producer.py` sha256 `4e8ee1f3512f154382c81cd505ff07abfbbabf9b19543c34bd42cd94fe5f3a22`
- `stratum_index_verifier.py` sha256 `3b397b1b26c3ea196fb3747c35388c94b193bee8a164c4290d3a7ef4e92a67b0`
- `canonical_decoder.py` sha256 `742cacac97b45c3ff06db84a79225a1bb165d55b38a2ad4ad9ba8bc3a6e79143`
- `enumeration_verifier.py` sha256 `d31eacc51e87681caf2c089cd2e9db6e48cc1cfdd2db0b4fe7d06da13f798342`
- `terminal_review_verifier.py` sha256 `22599359c7178d3bc7a19e20a4ccd33b47eb33eb6fd79a303b73f4edc0e43488`
- `terminal_ceremony.py` sha256 `c6b15a5af276598f10f44f94ce96702be6097f74bf4c01fab63121f4427d292d`
- `count_oracle_harness.py` sha256 `1a30b8d88ad822b97acd268218415928d605a7ad9ccaf568cfb44d69911b181b`

**VERDICT: REHEARSAL PASS — the pinned tools compose end to end on synthetic data; the freeze package can be signed with the machinery already exercised.**

# STRING-FIELD REGISTRY — every string-bearing field in every non-χ artifact

**Generated from `PREREG_SUCCESSOR_DRAFT_V77_20260830.md`'s schema blocks by `ref/gen_string_field_registry.py`; the extraction is mechanical so the enumeration cannot silently omit a declared field, and the CLASSIFICATION is human, exactly as the raise-site ledger splits the same labour.** A field with no row is **forbidden by default** and the generator exits nonzero. Constraints: `closed-vocab` (a declared member set) · `bounded-encoding` (digest/decimal-in-range) · `digest-ref` (sha256 of a canonical body).

**The honest limit:** bounded numerics still carry bits; the registry bounds capacity and cannot zero it. What it removes is free prose.

| field | constraint | declared | note |
|---|---|---|---|
| `BS-1.branch` | closed-vocab | v9 SLOT_SCHEMA |  |
| `BS-1.config_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-1.photoz_available` | closed-vocab | v9 SLOT_SCHEMA |  |
| `BS-1.resolution_date` | bounded-encoding | v9 SLOT_SCHEMA | ISO date |
| `BS-1b.columns` | closed-vocab | v9 SLOT_SCHEMA | declared column/key sets |
| `BS-1b.join_keys` | closed-vocab | v9 SLOT_SCHEMA | declared column/key sets |
| `BS-1b.photoz_product` | closed-vocab | v9 SLOT_SCHEMA | declared column/key sets |
| `BS-1b.provenance` | digest-ref | v9 SLOT_SCHEMA | was FREE PROSE - GPT56-V73 F2 named it; now the digest of a canonical provenance record |
| `BS-2c.brickid` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2c.c_bytes` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2c.grouped_sum` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2c.n_eligible` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2c.ungrouped_total` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2c.universe_brickid` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2f.accept_flag` | closed-vocab | v9 SLOT_SCHEMA |  |
| `BS-2f.bin` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2f.boundaries` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2f.brickid` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2f.c` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2f.mask_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-2f.objid` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2m.manifest_count` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2m.parent_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-2m.plan_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-2m.planner_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-2m.required_count` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2o.L_raw` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2o.N` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2o.Var` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2o.order_brickid` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2s.L_raw` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2s.L_ret` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2s.N_eq` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2s.N_ret` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2s.repass_successes` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-2s.selected_brickid` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-3.antisymmetry_receipt` | digest-ref | v9 SLOT_SCHEMA | canonical sub-document, digest-referenced |
| `BS-3.tau` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-3.weights_sha256` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-4.anchor_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-4.sign_convention` | closed-vocab | v9 SLOT_SCHEMA |  |
| `BS-4.verdict` | closed-vocab | v9 SLOT_SCHEMA |  |
| `BS-5f.mask_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-5f.n_trials` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-5f.passed` | closed-vocab | v9 SLOT_SCHEMA |  |
| `BS-5f.successes` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-5p.l_min_plan` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-5p.l_plan` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-5p.n_trials` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-5p.successes` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-6.byte_ceiling` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-6.manifest_sha256` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-6.producer_checksum_list` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-7f.beta_obs` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-7f.mask_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-7f.n_perm` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-7f.p` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-7f.perm_payload_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-7p.environment` | closed-vocab | v9 SLOT_SCHEMA | declared clause/env sets |
| `BS-7p.fixtures_sha256` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-7p.n_perm` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-7p.ref_code_sha256` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-8f.a_b` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-8f.a_hat` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-8f.a_lb` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-8f.a_lb_b` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-8f.cov_a` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-8f.epsilon` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-8f.sigma_a` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-8f.sigma_ab` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-8p.allocation` | digest-ref | v9 SLOT_SCHEMA | canonical sub-document, digest-referenced |
| `BS-8p.bin_algorithm` | digest-ref | v9 SLOT_SCHEMA | canonical sub-document, digest-referenced |
| `BS-8p.budget` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-8p.hc_rules_quotation` | digest-ref | v9 SLOT_SCHEMA | the HC-1H quotation-at-freeze, by digest |
| `BS-9.hdu_schema` | digest-ref | v9 SLOT_SCHEMA | canonical sub-document, digest-referenced |
| `BS-9.input_function_sha256` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-9.r1_r5_receipt` | digest-ref | v9 SLOT_SCHEMA | canonical sub-document, digest-referenced |
| `BS-9.runner_prohibition` | closed-vocab | v9 SLOT_SCHEMA | declared clause/env sets |
| `BS-9.tensor_layout` | digest-ref | v9 SLOT_SCHEMA | canonical sub-document, digest-referenced |
| `BS-V.A_L` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-V.evaluated_floor` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-V.mask_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-V.p` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-V.path` | closed-vocab | v9 SLOT_SCHEMA |  |
| `BS-V.sigma_comb` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-V.verdict` | closed-vocab | v9 SLOT_SCHEMA |  |
| `canonical.entry_body` | digest-ref | v9 SLOT_SCHEMA | canonical field-order encoding; detached signatures bind these digests |
| `canonical.explanation_body` | digest-ref | v9 SLOT_SCHEMA | canonical field-order encoding; detached signatures bind these digests |
| `canonical.freeze_signature_body` | digest-ref | v9 SLOT_SCHEMA | canonical field-order encoding; detached signatures bind these digests |
| `canonical.lock_body` | digest-ref | v9 SLOT_SCHEMA | canonical field-order encoding; detached signatures bind these digests |
| `canonical.opening_authorization` | digest-ref | v9 SLOT_SCHEMA | canonical field-order encoding; detached signatures bind these digests |
| `canonical.provenance_record` | digest-ref | v9 SLOT_SCHEMA | canonical field-order encoding; detached signatures bind these digests |
| `entry.signature` | bounded-encoding | v9 SLOT_SCHEMA | deterministic scheme mandated at BS-2k - no nonce channel |
| `envelope.body_sha256` | digest-ref | v9 SLOT_SCHEMA |  |
| `envelope.envelope_sha256` | digest-ref | v9 SLOT_SCHEMA |  |
| `envelope.environment` | digest-ref | v9 SLOT_SCHEMA | the container: canonical JSON of the six leaves below, digested into the envelope |
| `envelope.schema` | closed-vocab | v9 SLOT_SCHEMA | the literal successor_ref_v3/1 |
| `envelope.slot` | closed-vocab | v9 SLOT_SCHEMA | SLOT_SCHEMA keys |
| `environment.byteorder` | closed-vocab | v9 SLOT_SCHEMA | pinned by require_environment - one frozen value each, deviation refuses |
| `environment.machine` | bounded-encoding | v9 SLOT_SCHEMA | printable ASCII <= 64 bytes, refused by the envelope verifier (successor layer); value unpinned - any conforming interpreter string passes |
| `environment.numpy` | closed-vocab | v9 SLOT_SCHEMA | pinned by require_environment - one frozen value each, deviation refuses |
| `environment.platform` | bounded-encoding | v9 SLOT_SCHEMA | printable ASCII <= 64 bytes, refused by the envelope verifier (successor layer); value unpinned - any conforming interpreter string passes |
| `environment.python` | bounded-encoding | v9 SLOT_SCHEMA | printable ASCII <= 64 bytes, refused by the envelope verifier (successor layer); value unpinned - any conforming interpreter string passes |
| `environment.python_major_minor` | closed-vocab | v9 SLOT_SCHEMA | pinned by require_environment - one frozen value each, deviation refuses |
| `nonslot.acceptance_evidence_projection` | closed-vocab | v9 SLOT_SCHEMA | inventoried: three predicate bits |
| `nonslot.access_log_chain` | closed-vocab | v9 SLOT_SCHEMA | inventoried: the event.* rows above |
| `nonslot.adequacy_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.archive_seal_state_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.cutout_completion_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.enumeration_surface` | closed-vocab | v9 SLOT_SCHEMA | inventoried: entry.* rows + explanation cause |
| `nonslot.label_set_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.lock_checkpoint_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.stage_completion_artifact` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.unblinding_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `actor` | closed-vocab | §6.1 event schema | row identifiers |
| `baseline_verdict` | closed-vocab | §11 BS-3g | HELD | FAILED | PER-DRAW; informational |
| `byte_integrity_pass` | closed-vocab | §6.1 projection | predicate bit |
| `calibration_sha256` | digest-ref | §11 BS-3g |  |
| `canonical_shape_pass` | closed-vocab | §6.1 projection | predicate bit |
| `cause` | closed-vocab | §6.1 explanation | five-member set |
| `chain_position` | bounded-encoding | §6.1 entry | index into the chain |
| `class_key` | closed-vocab | §6.1 entry | (row, operation), both closed |
| `counterfactual_path_sha256` | digest-ref | §11 BS-3g | plus in-process v9 assert |
| `delta_gamma_max` | bounded-encoding | §11 BS-3g | finite positive double = frozen class-P |
| `disposition` | closed-vocab | §6.1 entry | NAMED-AS-DEFECT | EXPLAINED |
| `draw_generator_id` | closed-vocab | §11 BS-3g | set currently EMPTY - blocker |
| `draw_master_seed` | bounded-encoding | §11 BS-3g | decimal int [0,2^64-1]; frozen UNSET |
| `draw_verdict_digest` | digest-ref | §11 BS-3g | row-major serialization stated |
| `estimator_sha256` | digest-ref | §11 BS-3g |  |
| `event_digest` | digest-ref | §6.1 entry |  |
| `explanation_ref` | digest-ref | §6.1 entry | sha256 of the canonical explanation body |
| `gamma_bound` | bounded-encoding | §11 BS-3g | recomputed |gamma_hat|+k*sigma, never accepted |
| `gamma_hat` | bounded-encoding | §11 BS-3g | finite IEEE-754 double, decimal |
| `invariance_outcome` | closed-vocab | §11 BS-3g | HELD | FAILED |
| `kernel_sha256` | digest-ref | §11 BS-3g |  |
| `mapping_id` | closed-vocab | §11 BS-3g | sole member MAPPING-NOT-PREREGISTERED until ruled |
| `mask_sha256` | digest-ref | §11 BS-3g | must equal BS-2f's pinned mask_digest |
| `n_draws` | bounded-encoding | §11 BS-3g | decimal int [1,10^6]; frozen value UNSET |
| `n_perturbations` | bounded-encoding | §11 BS-3g | decimal int [1,10^6] |
| `object identity` | bounded-encoding | §6.1 event schema | brickid/objid keys |
| `operation` | closed-vocab | §6.1 event schema | BS-2k closed operation set |
| `parent_attempt_present` | closed-vocab | §6.1 projection | predicate bit |
| `perturbation_manifest_sha256` | digest-ref | §11 BS-3g |  |
| `rederivation_digest` | digest-ref | §6.1 entry | revision must contain the class_key |
| `refusal reason` | closed-vocab | §6.1 event schema | the eleven codes |
| `running chain digest` | digest-ref | §6.1 event schema |  |
| `sigma_gamma` | bounded-encoding | §11 BS-3g | finite IEEE-754 double, decimal |
| `success/refusal` | closed-vocab | §6.1 event schema |  |
| `table row` | closed-vocab | §6.1 event schema |  |
| `timestamp` | bounded-encoding | §6.1 event schema |  |
| `verifier_sha256` | digest-ref | §11 BS-3g |  |

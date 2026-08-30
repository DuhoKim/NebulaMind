# STRING-FIELD REGISTRY — every string-bearing field in every non-χ artifact

**Generated from `PREREG_SUCCESSOR_DRAFT_V110_20260830.md`'s schema blocks by `ref/gen_string_field_registry.py`; TWO provenances, said plainly (CODEX-V81 F8: the header claimed generated-from-schemas while several sets are hand-declared): draft schema blocks, v9's SLOT_SCHEMA, the envelope constructor and environment_record are EXTRACTED mechanically; the openauth, freeze, canonical, non-slot, signature and parameter sets are DECLARED here as classification law, versioned with this generator. Extraction cannot silently omit; declaration is auditable in one screen.** A field with no row is **forbidden by default** and the generator exits nonzero. Constraints: `closed-vocab` (a declared member set) · `bounded-encoding` (digest/decimal-in-range) · `digest-ref` (sha256 of a canonical body).

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
| `BS-1b.provenance` | digest-ref | v9 SLOT_SCHEMA | digest of canonical.provenance_record - WHOSE ENCODING IS PENDING; this field is unfillable until that schema is written, which the pending row states |
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
| `BS-7p.environment` | digest-ref | v9 SLOT_SCHEMA | canonical sub-schema below - V77 called this closed-vocab after defining it as a sub-schema, a false label one revision old (CODEX-V77 F2) |
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
| `BS-9.runner_prohibition` | closed-vocab | v9 SLOT_SCHEMA | declared clause set |
| `BS-9.tensor_layout` | digest-ref | v9 SLOT_SCHEMA | canonical sub-document, digest-referenced |
| `BS-V.A_L` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-V.evaluated_floor` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-V.mask_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `BS-V.p` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-V.path` | closed-vocab | v9 SLOT_SCHEMA |  |
| `BS-V.sigma_comb` | bounded-encoding | v9 SLOT_SCHEMA |  |
| `BS-V.verdict` | closed-vocab | v9 SLOT_SCHEMA |  |
| `arrival.boot_epoch` | bounded-encoding | draft 6.1 item (ii-b) - ARRIVAL event schema | the authenticated clock pair: boot_epoch = the BS-2k restart counter, decimal integer in [0, 10^6]; monotonic_reading = decimal integer nanoseconds in [0, 2^63-1] (GPT56-V90 F3: bounds stated); overdue is computed from these bytes under spec-3b's chain-order monotonicity invariants, never from a clock read at verification |
| `arrival.kind` | closed-vocab | draft 6.1 item (ii-b) - ARRIVAL event schema | the literal ARRIVAL |
| `arrival.monotonic_reading` | bounded-encoding | draft 6.1 item (ii-b) - ARRIVAL event schema | the authenticated clock pair: boot_epoch = the BS-2k restart counter, decimal integer in [0, 10^6]; monotonic_reading = decimal integer nanoseconds in [0, 2^63-1] (GPT56-V90 F3: bounds stated); overdue is computed from these bytes under spec-3b's chain-order monotonicity invariants, never from a clock read at verification |
| `arrival.object_identity` | bounded-encoding | draft 6.1 item (ii-b) - ARRIVAL event schema | brickid/objid keys |
| `arrival.operation` | closed-vocab | draft 6.1 item (ii-b) - ARRIVAL event schema | the event schema's own closed sets |
| `arrival.request_key` | bounded-encoding | draft 6.1 item (ii-b) - ARRIVAL event schema | the arrival's own chain position, decimal - unique by construction, restart-safe; the enumeration verifier checks the join BIDIRECTIONALLY: every arrival at most one terminal naming it, every terminal exactly one prior arrival |
| `arrival.row` | closed-vocab | draft 6.1 item (ii-b) - ARRIVAL event schema | the event schema's own closed sets |
| `arrival.running_chain_digest` | digest-ref | draft 6.1 item (ii-b) - ARRIVAL event schema |  |
| `arrival.timestamp` | bounded-encoding | draft 6.1 item (ii-b) - ARRIVAL event schema | ISO-8601 UTC, 24 bytes |
| `bindmap.decision_boot_epoch` | bounded-encoding | draft 6.1 item (iv-c) - binding-to-key map | the decision's clock pair, same bounds as the arrival's - the decide-within-D evidence; WIDENED at V93 (CODEX-V92 F1), FILED with the coordinator |
| `bindmap.decision_chain_position` | bounded-encoding | draft 6.1 item (iv-c) - binding-to-key map | chain positions, bounded decimal - the join is (request_key <-> decision position) |
| `bindmap.decision_event_digest` | digest-ref | draft 6.1 item (iv-c) - binding-to-key map |  |
| `bindmap.decision_monotonic_reading` | bounded-encoding | draft 6.1 item (iv-c) - binding-to-key map | the decision's clock pair, same bounds as the arrival's - the decide-within-D evidence; WIDENED at V93 (CODEX-V92 F1), FILED with the coordinator |
| `bindmap.request_key` | bounded-encoding | draft 6.1 item (iv-c) - binding-to-key map | chain positions, bounded decimal - the join is (request_key <-> decision position) |
| `bindmap.signature` | bounded-encoding | draft 6.1 item (iv-c) - binding-to-key map | detached deterministic signature over the canonical entry body, 64 bytes - Row B's provisioned keypair, signer roster-bound, no envelope leaves (CODEX-V91 F3: sig-envelope was off-enum and invited undeclared leaves) |
| `bs7p_env.dependency_roots` | digest-ref | v9 SLOT_SCHEMA | roots and linker-resolution manifest as ordered (path, digest) pairs |
| `bs7p_env.dynamic_load_manifest` | digest-ref | v9 SLOT_SCHEMA | roots and linker-resolution manifest as ordered (path, digest) pairs |
| `bs7p_env.interpreter_path` | bounded-encoding | v9 SLOT_SCHEMA | absolute POSIX path, printable ASCII <= 256 bytes, no traversal segments |
| `bs7p_env.interpreter_sha256` | digest-ref | v9 SLOT_SCHEMA | roots and linker-resolution manifest as ordered (path, digest) pairs |
| `canonical.entry_body` | digest-ref | v9 SLOT_SCHEMA | field-order encoding WRITTEN in this draft; detached signatures bind these digests |
| `canonical.explanation_body` | digest-ref | v9 SLOT_SCHEMA | field-order encoding WRITTEN in this draft; detached signatures bind these digests |
| `canonical.freeze_signature_body` | digest-ref | v9 SLOT_SCHEMA | field-order encoding WRITTEN in this draft; detached signatures bind these digests |
| `canonical.lock_body` | digest-ref | v9 SLOT_SCHEMA | field-order encoding WRITTEN in this draft; detached signatures bind these digests |
| `canonical.opening_authorization` | digest-ref | v9 SLOT_SCHEMA | field-order encoding WRITTEN in this draft; detached signatures bind these digests |
| `canonical.provenance_record` | SCHEMA-PENDING | v9 SLOT_SCHEMA | V77 force-added this as digest-ref with no written encoding (GPT56-V77 F3, CODEX-V77 F1) - the SCHEMA-PENDING defect wearing a canonical name; pending until its encoding is written |
| `ckclock.boot_epoch` | bounded-encoding | draft 6.1 item (ii-c) + spec 3b - checkpoint clock record | the checkpoint CLOCK RECORD of its own production - same bounds as the arrival pair (epoch [0, 10^6], reading ns [0, 2^63-1], GPT56-V90 F3) - the other side of the spec-3b comparison rule |
| `ckclock.gap_declaration` | bounded-encoding | draft 6.1 item (ii-c) + spec 3b - opening record | ascending declared-skipped epochs, each decimal [0, 10^6]; emptiness proven by chain continuity, not trusted (GPT56-V93 F2) |
| `ckclock.monotonic_reading` | bounded-encoding | draft 6.1 item (ii-c) + spec 3b - checkpoint clock record | the checkpoint CLOCK RECORD of its own production - same bounds as the arrival pair (epoch [0, 10^6], reading ns [0, 2^63-1], GPT56-V90 F3) - the other side of the spec-3b comparison rule |
| `ckclock.predecessor_epoch` | bounded-encoding | draft 6.1 item (ii-c) + spec 3b - opening record | the previous opening's epoch, decimal [0, 10^6]; NONE for the anchored first epoch (GPT56-V93 F1) |
| `dlm_entry.digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `dlm_entry.path` | bounded-encoding | v9 SLOT_SCHEMA | absolute POSIX path, printable ASCII <= 256 bytes, no traversal segments - same bound as the interpreter path; the containers enumerate exactly these entries |
| `drainst.boot_epoch` | bounded-encoding | spec 3c - termination records | the clock pair, same bounds and quantization as every clock-bearing record |
| `drainst.kind` | closed-vocab | spec 3c - termination records (GPT56-V102 F6) | the record-kind literals (section 3c T3) |
| `drainst.monotonic_reading` | bounded-encoding | spec 3c - termination records | the clock pair, same bounds and quantization as every clock-bearing record |
| `drainst.receipt_digest` | digest-ref | spec 3c - termination records |  |
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
| `freezebody.class_counts` | bounded-encoding | v9 SLOT_SCHEMA | decimal ints; class counts as the counts tool emits them |
| `freezebody.code_digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `freezebody.draft_sha256` | digest-ref | v9 SLOT_SCHEMA |  |
| `freezebody.parent_sha256` | digest-ref | v9 SLOT_SCHEMA |  |
| `freezebody.selection_bricks` | bounded-encoding | v9 SLOT_SCHEMA | decimal ints; class counts as the counts tool emits them |
| `haltrec.chain_head` | bounded-encoding | spec 5 - exhaustion halt receipt | position + running digest at halt; identities are SEALED committee-side, not here (GPT56-V94 F7) |
| `haltrec.first_opening_digest` | digest-ref | terminated-family canonical bodies | CHAIN identity - one freeze can govern a resumed run, the first opening cannot (GPT56-V98 F5, CODEX-V98 F2) |
| `haltrec.freeze_signature_digest` | digest-ref | terminated-family canonical bodies | run identity - replay across runs fails (CODEX-V97 F4) |
| `haltrec.kind` | closed-vocab | spec 5 - exhaustion halt receipt (CODEX-V94 F4) | the literal TERMINATED-BY-LABEL-EXHAUSTION |
| `haltrec.signature` | bounded-encoding | terminated-family envelopes | detached deterministic signature, 64 bytes (GPT56-V97 F5: absent from this registry) |
| `lockbody.accepted_mask_digest` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.archive_seal_state` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.calibration_record_digest` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.chain_segment` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.classp_receipt_manifest` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.decision_input_digests` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.environment_record` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.freeze_signature` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.gate_reports` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.lock_checkpoint` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.roster_digest` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.signer_identity` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockbody.stagec_receipt_digest` | digest-ref | v9 SLOT_SCHEMA | clause 3(b)'s canonical order; cross-checked against the clause text at generation |
| `lockcp.chain_head_digest` | digest-ref | draft 3(b) - lock checkpoint receipt |  |
| `lockcp.chain_head_position` | bounded-encoding | draft 3(b) - lock checkpoint receipt, schema closed at V99 (GPT56-V98 F2) | decimal chain position |
| `lockcp.clock_record` | bounded-encoding | draft 3(b) - lock checkpoint receipt | the (epoch, reading) pair per spec 3b |
| `lockcp.sealed_bindmap_digest` | digest-ref | draft 3(b) - lock checkpoint receipt |  |
| `lockcp.sealed_entry_set_digest` | digest-ref | draft 3(b) - lock checkpoint receipt |  |
| `nonslot.acceptance_evidence_projection` | closed-vocab | v9 SLOT_SCHEMA | inventoried: three predicate bits |
| `nonslot.access_log_chain` | closed-vocab | v9 SLOT_SCHEMA | inventoried: the event.* rows above AND the arrival.* rows - the chain carries both event classes (CODEX-V88 F1) |
| `nonslot.adequacy_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.archive_seal_state_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.cutout_completion_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.enumeration_surface` | closed-vocab | v9 SLOT_SCHEMA | inventoried: entry.* rows + explanation cause |
| `nonslot.label_set_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.lock_checkpoint_receipt` | digest-ref | v9 SLOT_SCHEMA | schema CLOSED: the five lockcp.* rows - (chain_head_position, chain_head_digest, clock_record, sealed_entry_set_digest, sealed_bindmap_digest); nested preimages canonical per draft 3(b) (GPT56-V98 F2, GPT56-V99 F3/F4) |
| `nonslot.stage_completion_artifact` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `nonslot.unblinding_receipt` | SCHEMA-PENDING | v9 SLOT_SCHEMA | fields unenumerable until the defining slot fills; producer blocked by the same slot - a stub saying so, not a constraint it does not have |
| `openauth.bsl_digest` | digest-ref | v9 SLOT_SCHEMA | ceremony_id one-use, signer bound to the BS-2k public key |
| `openauth.ceremony_id` | digest-ref | v9 SLOT_SCHEMA | ceremony_id one-use, signer bound to the BS-2k public key |
| `openauth.destination` | closed-vocab | v9 SLOT_SCHEMA | store roster / declared destinations / the literal P7 |
| `openauth.phase` | closed-vocab | v9 SLOT_SCHEMA | store roster / declared destinations / the literal P7 |
| `openauth.schema_version` | closed-vocab | v9 SLOT_SCHEMA | the literal schema/version Clause 6 binds - V80 substituted timestamp for this field TWICE, in the withdrawal that claimed to fix the first substitution (GPT56-V80 F1, CODEX-V80 F3) |
| `openauth.signer_identity` | digest-ref | v9 SLOT_SCHEMA | ceremony_id one-use, signer bound to the BS-2k public key |
| `openauth.store_identity_committee` | closed-vocab | v9 SLOT_SCHEMA | store roster / declared destinations / the literal P7 |
| `openauth.store_identity_main` | closed-vocab | v9 SLOT_SCHEMA | store roster / declared destinations / the literal P7 |
| `param.attempt_count` | bounded-encoding | v9 SLOT_SCHEMA | decimal int [0, 10^4] |
| `param.duration_ms` | bounded-encoding | v9 SLOT_SCHEMA | decimal int [0, 2^31) |
| `param.lease_id_digest` | digest-ref | v9 SLOT_SCHEMA | 64 lowercase hex |
| `param.signal_number` | bounded-encoding | v9 SLOT_SCHEMA | decimal int [1, 64] |
| `param.store_errno` | bounded-encoding | v9 SLOT_SCHEMA | decimal int [0, 2^15) |
| `passrec.gate` | closed-vocab | spec 3b - gate pass record (anchor) | the five-gate set |
| `passrec.head_digest` | digest-ref | spec 3b - gate pass record | predecessor INSIDE the signed body - the anchors chain by construction (GPT56-V96 F2, CODEX-V96 F2) |
| `passrec.head_position` | bounded-encoding | spec 3b - gate pass record | decimal chain position |
| `passrec.partition_cut_position` | bounded-encoding | spec 3b - gate pass record | the issuance commit's last write position; 0 pre-BS-L (GPT56-V97 F3) |
| `passrec.predecessor_record_digest` | digest-ref | spec 3b - gate pass record | predecessor INSIDE the signed body - the anchors chain by construction (GPT56-V96 F2, CODEX-V96 F2) |
| `passrec.signature` | bounded-encoding | spec 3b - gate pass record | detached deterministic signature, 64 bytes, enumerator keypair - anchors chain by predecessor verification (GPT56-V95 F2) |
| `passrec.verifier_digest` | digest-ref | spec 3b - gate pass record | predecessor INSIDE the signed body - the anchors chain by construction (GPT56-V96 F2, CODEX-V96 F2) |
| `revbody.drain_start_position` | bounded-encoding | spec 3b - terminal-review body | decimal chain position |
| `revbody.kind` | closed-vocab | spec 3b - terminal-review body (L09 caught these fields unregistered) | the literal terminal-review kind |
| `revbody.recomputed_head` | digest-ref | spec 3b - terminal-review body |  |
| `revbody.terminal_checkpoint_digest` | digest-ref | spec 3b - terminal-review body |  |
| `revbody.transcript_digest` | digest-ref | spec 3b - terminal-review body |  |
| `revbody.verifier_digest` | digest-ref | spec 3b - terminal-review body |  |
| `rnote.boot_epoch` | bounded-encoding | spec 3c T1 - receipt-note record | the clock pair |
| `rnote.kind` | closed-vocab | spec 3c T1 - receipt-note record (GPT56-V104 F3) | the receipt-note literal |
| `rnote.monotonic_reading` | bounded-encoding | spec 3c T1 - receipt-note record | the clock pair |
| `rnote.receipt_digest` | digest-ref | spec 3c T1 - receipt-note record |  |
| `roots_entry.digest` | digest-ref | v9 SLOT_SCHEMA |  |
| `roots_entry.path` | bounded-encoding | v9 SLOT_SCHEMA | absolute POSIX path, printable ASCII <= 256 bytes, no traversal segments - same bound as the interpreter path; the containers enumerate exactly these entries |
| `sig.bsl_lock` | bounded-encoding | v9 SLOT_SCHEMA | detached deterministic signature over the named canonical body, 64 bytes |
| `sig.checkpoint` | bounded-encoding | v9 SLOT_SCHEMA | detached deterministic signature over the named canonical body, 64 bytes |
| `sig.explanation` | bounded-encoding | v9 SLOT_SCHEMA | detached deterministic signature over the named canonical body, 64 bytes |
| `sig.freeze` | bounded-encoding | v9 SLOT_SCHEMA | detached deterministic signature over the named canonical body, 64 bytes |
| `sig.opening` | bounded-encoding | v9 SLOT_SCHEMA | detached deterministic signature over the named canonical body, 64 bytes |
| `succexp.continuation_segment_digest` | digest-ref | draft 11 - successor export |  |
| `succexp.flagged_keys` | bounded-encoding | draft 11 - successor export | the recurrence-flagged mismatch class_keys the successor must adjudicate (CODEX-V109 F4) |
| `succexp.freeze_signature_digest` | digest-ref | draft 11 - successor export |  |
| `succexp.kind` | closed-vocab | draft 11 - successor export (GPT56/CODEX-V108 F4) | the successor-export literal |
| `succexp.sealed_enumeration_digest` | digest-ref | draft 11 - successor export |  |
| `succexp.terminal_head` | bounded-encoding | draft 11 - successor export | position + running digest; the digest half is the chain running digest, frozen discipline (CODEX-V109 F3) |
| `termcp.boot_epoch` | bounded-encoding | spec 3c - termination records | the clock pair, same bounds and quantization as every clock-bearing record |
| `termcp.chain_head_digest` | digest-ref | spec 3c - termination records |  |
| `termcp.chain_head_position` | bounded-encoding | spec 3c - termination records | decimal chain positions |
| `termcp.drain_start_position` | bounded-encoding | spec 3c - termination records | decimal chain positions |
| `termcp.failed_members` | bounded-encoding | spec 3c - termination records | ascending drain-set positions whose refusals exhausted A_max aborts (GPT56-V104 F5) |
| `termcp.kind` | closed-vocab | spec 3c - termination records (GPT56-V102 F6) | the record-kind literals (section 3c T3) |
| `termcp.monotonic_reading` | bounded-encoding | spec 3c - termination records | the clock pair, same bounds and quantization as every clock-bearing record |
| `termcp.receipt_digest` | digest-ref | spec 3c - termination records |  |
| `termrec.chain_head` | bounded-encoding | draft 6.1 - terminated-verdict record | position + running digest at production |
| `termrec.class_key` | bounded-encoding | draft 6.1 - terminated-verdict record | (table row, operation) - the computed key |
| `termrec.first_opening_digest` | digest-ref | terminated-family canonical bodies | CHAIN identity - one freeze can govern a resumed run, the first opening cannot (GPT56-V98 F5, CODEX-V98 F2) |
| `termrec.freeze_signature_digest` | digest-ref | terminated-family canonical bodies | run identity - replay across runs fails (CODEX-V97 F4) |
| `termrec.gate` | closed-vocab | draft 6.1 - terminated-verdict record | the five-gate set |
| `termrec.kind` | closed-vocab | draft 6.1 - terminated-verdict record (GPT56-V96 F6) | the literal TERMINATED-UNNAMEABLE-REFUSAL-CLASS |
| `termrec.signature` | bounded-encoding | terminated-family envelopes | detached deterministic signature, 64 bytes (GPT56-V97 F5: absent from this registry) |
| `actor` | closed-vocab | §6.1 event schema | row identifiers |
| `baseline_verdict` | closed-vocab | §11 BS-3g | a PRODUCTION verdict token - REPRODUCED-LONGO / REJECTED-AT-LONGO-AMPLITUDE / INCONCLUSIVE - or PER-DRAW; V84 wrongly closed it to the invariance tokens (GPT56-V84 F4, CODEX-V84 F5): cells carry run verdicts |
| `byte_integrity_pass` | closed-vocab | §6.1 projection | predicate bit |
| `calibration_sha256` | digest-ref | §11 BS-3g |  |
| `canonical_shape_pass` | closed-vocab | §6.1 projection | predicate bit |
| `cause` | closed-vocab | §6.1 explanation | five-member set |
| `chain_position` | bounded-encoding | §6.1 entry | index into the chain |
| `class_key` | closed-vocab | §6.1 entry | (row, operation), both closed |
| `counterfactual_path_sha256` | digest-ref | §11 BS-3g | compiled from verified buffer |
| `delta_gamma_max` | bounded-encoding | §11 BS-3g | canonical decimal string per the one §11 grammar (no exponent, no trailing zeros, canonical zero 0) - DERIVED = 2*Gamma/n_steps under AMENDMENT 2 (GPT56-V91 F4: this row said finite positive double after the grid went exact-decimal) |
| `disposition` | closed-vocab | §6.1 entry | NAMED-AS-DEFECT · EXPLAINED |
| `draw_generator_id` | closed-vocab | §11 BS-3g | one member, committed blind: numpy-1.26.4-PCG64-default_rng |
| `draw_master_seed` | bounded-encoding | §11 BS-3g | decimal int; COMMITTED blind = 20260830 |
| `draw_verdict_digest` | digest-ref | §11 BS-3g | row-major serialization stated |
| `estimator_sha256` | digest-ref | §11 BS-3g |  |
| `event_digest` | digest-ref | §6.1 entry |  |
| `explanation_ref` | digest-ref | §6.1 entry | sha256 of the canonical explanation body |
| `gamma_bound` | bounded-encoding | §11 BS-3g | RULED a-priori (2026-08-30): equals the ratified frozen endpoint; k-gamma moot; the old recomputed-formula note encoded the superseded shape (SWEEP: GPT56/CODEX-V87 F6) |
| `gamma_hat` | bounded-encoding | §11 BS-3g | finite IEEE-754 double, decimal |
| `invariance_outcome` | closed-vocab | §11 BS-3g | HELD · FAILED |
| `kernel_sha256` | digest-ref | §11 BS-3g |  |
| `mapping_id` | closed-vocab | §11 BS-3g | sole member MAPPING-NOT-PREREGISTERED until ruled |
| `mask_sha256` | digest-ref | §11 BS-3g | must equal BS-2f's pinned mask_digest |
| `n_draws` | bounded-encoding | §11 BS-3g | decimal int; RULED = 99 (2026-08-30 sitting) |
| `n_perturbations` | bounded-encoding | §11 BS-3g | decimal int [1,10^6] |
| `object identity` | bounded-encoding | §6.1 event schema | brickid/objid keys |
| `operation` | closed-vocab | §6.1 event schema | BS-2k closed operation set, STORE-QUALIFIED: (row, operation) determines the store (GPT56-V81 F4, CODEX-V81 F5 - Row I touches multiple stores, so unqualified operations made the presence-audit join non-derivable) |
| `parent_attempt_present` | closed-vocab | §6.1 projection | predicate bit |
| `perturbation_manifest_sha256` | digest-ref | §11 BS-3g |  |
| `recurrence_flag` | closed-vocab | §6.1 entry | set at M_max same-class emissions; carried into the successor export (CODEX-V109 F4) |
| `rederivation_digest` | digest-ref | §6.1 entry | revision must contain the class_key |
| `refusal reason` | closed-vocab | §6.1 event schema | the eleven codes |
| `replay_harness_sha256` | digest-ref | §11 BS-3g | the harness carrying every replay obligation (CODEX-V81 F1) |
| `review_ref` | digest-ref | §6.1 entry | sha256 of the signed review artifact - REVIEWED entries only, the explanation_ref discipline (GPT56-V109 F3) |
| `running chain digest` | digest-ref | §6.1 event schema |  |
| `sigma_gamma` | bounded-encoding | §11 BS-3g | finite IEEE-754 double, decimal |
| `success/refusal` | closed-vocab | §6.1 event schema |  |
| `table row` | closed-vocab | §6.1 event schema |  |
| `timestamp` | bounded-encoding | §6.1 event schema | ISO-8601 UTC YYYY-MM-DDThh:mm:ss.sssZ, exactly 24 bytes (GPT56-V77 F4: labelled bounded with no bound) |
| `verifier_sha256` | digest-ref | §11 BS-3g |  |

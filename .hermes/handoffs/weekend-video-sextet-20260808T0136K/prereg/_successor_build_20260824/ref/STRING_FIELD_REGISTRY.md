# STRING-FIELD REGISTRY — every string-bearing field in every non-χ artifact

**Generated from `PREREG_SUCCESSOR_DRAFT_V73_20260830.md`'s schema blocks by `ref/gen_string_field_registry.py`; the extraction is mechanical so the enumeration cannot silently omit a declared field, and the CLASSIFICATION is human, exactly as the raise-site ledger splits the same labour.** A field with no row is **forbidden by default** and the generator exits nonzero. Constraints: `closed-vocab` (a declared member set) · `bounded-encoding` (digest/decimal-in-range) · `digest-ref` (sha256 of a canonical body).

**The honest limit:** bounded numerics still carry bits; the registry bounds capacity and cannot zero it. What it removes is free prose.

| field | constraint | declared | note |
|---|---|---|---|
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

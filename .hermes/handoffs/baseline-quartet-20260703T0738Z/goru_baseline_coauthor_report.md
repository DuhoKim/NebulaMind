## Mechanical Verification & Schema Constraints (Goru Baseline)

### 1. Schema Fields for the Claim/Status Ledger
All ledger entries must strictly adhere to the following schema to ensure traceability:
- **`entry_id`**: Unique identifier for the ledger claim.
- **`source_bibcodes`**: Array of source paper identifiers mapping exactly to the combined ADS candidate dataset.
- **`claim_statement`**: The core, atomic factual statement derived from the sources.
- **`epistemic_type`**: The modality of the evidence (e.g., `simulation_model`, `observational_sample`, `review_status`).
- **`dominance_side`**: Classification mapping if applicable (e.g., `halo_environment`, `central_bh_agn`).
- **`certainty_level`**: Mechanical cap on prose confidence, preventing overclaims.
- **`verification_status`**: State of the ledger entry (e.g., `pending`, `validated`, `blocked`).

### 2. Verification Gates
- **Source Linkage Gate**: Every claim in the ledger must trace backward to at least one valid, verifiable `bibcode` present in the source JSONL.
- **Prose-to-Ledger Binding**: Any prose sentence generated must carry explicit citation markers binding it exactly to a ledger `entry_id`. Unbound prose will fail mechanical validation.
- **Certainty Bound Check**: The modality and rhetorical strength of generated prose must never exceed the explicitly calculated `certainty_level` in the ledger.

### 3. No-Write Safety Rules
- **Prose Embargo**: Do not generate any reader-facing prose or update production documents until the complete status map and ledger have successfully passed mechanical validation.
- **State Read-Only Lock**: No database writes, SQL mutations, schema migrations, git operations, or deploy scripts are permitted during the distillation and mapping phases.
- **Data Integrity**: Never mutate or modify original source artifact JSONL files during the extraction process.

### 4. Machine-Checkable Done Conditions
- [ ] Ledger JSON artifact successfully parses.
- [ ] 100% of ledger claims successfully map to valid `bibcodes` in the combined source artifact.
- [ ] 100% of prose sentences map to corresponding ledger `entry_id` bounds.
- [ ] Safety audit confirms zero DB writes, git commits, or deployed product mutations during generation.

GORU_BASELINE_COAUTHOR_DONE_20260703T0738Z

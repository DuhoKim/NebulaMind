# M2 Deepening Mechanical Audit (Cycle 1)

Marker: `DEEPENING_RESOURCE_SEED_20260708T043427Z`

## Audit Status: PASS

I have successfully tracked and verified the M2 deepened v2 candidate against the first-pass mechanical facts. The v2 files are now present in `prose-evidence-trust-deepening-20260708T043427Z/` and strictly respect all required constraints.

### Mechanical Facts Verified:
1. **Adjudication Totals**:
   - `accepted_full`: 2
   - `accepted_limited`: 20
   - `excluded`: 2
   - `rejected`: 12
   These totals exactly match the coverage map JSON and the explicit tracking in the generated markdown.

2. **28060 No-Target Caveat**:
   - Evidence `28060` (positive-feedback caution) is correctly tracked as a standalone caution with `target_claim: null` in the JSON and given a dedicated section in the markdown that explicitly states it sits outside all claim boxes to act as an anti-overclaim caution.

3. **Per-Claim Sum (21) vs Cited (22)**:
   - The discrepancy is fully and honestly explained in the candidate's introduction: `22` reflects all accepted/limited positions, while `21` reflects the sum of those attached directly to the 6 claims (omitting `28060`).

4. **Cite-Unmatched & Product Cite IDs**:
   - Exactly `7` cite-unmatched groups are preserved.
   - `0` product cite IDs are present, explicitly enforcing method-local source-first adjudication boundaries.

5. **Static Safety**:
   - The candidate files use only relative links (e.g., `../p1-source-position-ledger.html`).
   - No `<script>`, `fetch`, API calls, or live product database queries were detected.

All mechanical checks and static safety boundaries have been strictly verified. No modifications were made to the candidate files during this audit.

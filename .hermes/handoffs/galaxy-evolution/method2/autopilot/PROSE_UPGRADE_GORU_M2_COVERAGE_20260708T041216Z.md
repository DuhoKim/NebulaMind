# M2 Mechanical Coverage Extraction (Prose Upgrade)

Marker: `PROSE_UPGRADE_RESOURCE_SEED_20260708T041216Z`

## Coverage Facts for Prose Generation

1. **Claims Covered**: 6 claims (2942, 2943, 2944, 2945, 2946, 2947)
2. **Trust/Adjudication Totals**:
   - `accepted_full`: 2
   - `accepted_limited`: 20
   - `excluded`: 2
   - `rejected`: 12
3. **Cite-Unmatched Groups**: 7 groups. These represent method-local source-adjudication IDs that are deliberately left unresolved to product cite IDs, enforcing "cite-unmatched honesty".
4. **Trust Vocabulary**: The explicitly defined trust scale is "method-local source-first adjudication status (NOT product DB trust)". It uses ACCEPTED, ACCEPTED-LIMITED, EXCLUDED, and REJECTED instead of unverified/debated product trust scores.
5. **Evidence 28060 No-Current-Target Caution**: Evidence 28060 (arXiv: 2604.15438) exists in the P1 source ledger with an `accepted_limited` status but targets `None`. It operates as a `LIMITED_CAUTION_ONLY_NO_CURRENT_TARGET_CLAIM_SUPPORT` to provide an anti-overclaim caution (regarding compressive/positive feedback) without directly supporting a quenching claim.
6. **Exact Count Explanation**: The overall totals list `accepted_limited: 20` and `cited_positions: 22`. However, summing the explicit arrays under each claim yields only 19 and 21 respectively. This intentional discrepancy accounts for the unbound evidence 28060, which must be tracked in the overarching total of valid sources but is intentionally omitted from the claim-level attachments.

All extracted facts align perfectly with the static working-repo artifacts (evidence-trust-map JSON, page content, wiki-format preview, and the M2 totals reconciliation report). No candidate edits were made during extraction.

# DUHO_RESUME_FLOW_TARGET — resume after benign Flow target drift

Authorized by Duho (2026-07-14), relayed by Hwao (captain).

## Finding
The epoch-91 fail-closed STOP was correct. Cause is benign and identified by Duho: the Chrome
window had drifted to a **Gemini usage-check page**, so Yui's leased Flow target (`94b7dd5c…`)
no longer matched the visible page. Duho has **manually restored the Flow window**. No job was
accepted and no quota was spent.

## Authorization (Yui, Flow/Studio)
1. Clear the epoch-91 emergency freeze under this resume; append the ledger resume entry; VERIFY_OK.
2. Re-inspect the CURRENT Flow window read-only. Do NOT assume `3b2a3843`; lease whatever Flow
   project is now showing after Duho's restore (confirm it is a valid Flow project composer).
3. Acquire a FRESH exact target lease on the current project.
4. Run the SINGLE bounded Flow job, capture receipt, report to Hwao before scaling.

## Rails unchanged
Page-scoped challenge check only (Chrome toolbar sync badge remains OUT OF SCOPE); serialized
submit via the broker account-submission lease; no secrets. If the window target drifts again
mid-op, fail closed and report to Hwao (do not chase it).

DUHO_RESUME_FLOW_TARGET_20260714

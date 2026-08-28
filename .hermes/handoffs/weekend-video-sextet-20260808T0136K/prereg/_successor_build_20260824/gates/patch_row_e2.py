with open('../PREREG_SUCCESSOR_DRAFT_V27_20260827.md', 'r') as f:
    text = f.read()

import re
text = re.sub(
    r'\| E \| \*\*Acceptance-ledger recompute\*\* \| reads \*\*only.*?\| reading any field outside the evidence schema \|',
    r'| E | **Acceptance-ledger recompute** | reads **only the separate authenticated acceptance-evidence projections** in the main store (predicate bits only), the fixed parent lists, and the authenticated catalogue-quality evidence fields (exact authenticated fields `flux_ivar_r`, `psfsize_r`, `nobs_r` from source digest `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`, joined one-to-one on keys `brickid`, `objid`, verified by the BS-2a pinned verifier, failing nonfatally as an ordinary exclusion) — and computes the structural §2.7(2) predicates and catalogue-quality exclusion from it, **excluding instrument absence/non-finiteness and instrument confidence, which remain dropped from the pre-lock structural exclusion**. Does not read the cutout-completion receipt. → atomically writes both the append-only evidence ledger and the realised partition, ensuring the **P3 sealed mask genuinely holds 49,211 rows**. | P2–P3, after complete inference | BS-2a (design), and exactly one verified acceptance-evidence projection per parent object | the realised-partition record (N = 49,211), bound by BS-2f | reading any field outside the evidence schema |',
    text
)

with open('../PREREG_SUCCESSOR_DRAFT_V27_20260827.md', 'w') as f:
    f.write(text)

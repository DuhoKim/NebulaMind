# Tori independent R2 preflight receipt

Packet: `gemini-dr-content-expert-gate-r2-20260714T002603Z`
Decision: **GREEN; packet remains NOT ARMED**

Independent checks:

- R2 prompt bytes equal R1 prompt bytes.
- R2 prompt SHA-256: `4d57fd71b49e74760cc1be1acc6fb50ce1e777b4c43907612830b346b471f42a` — matches the R2 pin.
- Exactly eight numbered comparison rows were found.
- The final non-empty prompt line equals R1's final non-empty prompt line.
- That final-line marker string occurs exactly once across the complete R2 packet; this receipt intentionally does not echo it.
- One zero-byte root NOT_ARMED marker exists; no ARMED marker exists.
- One zero-byte Goru R2 GREEN marker exists; no current Goru NOT_GREEN marker exists.
- Goru's report has no failed Boolean and ends with its required receipt marker.

Recomputed source/capture hashes:

- VERDICTS: `a4821a54806088c977289d1e7ce103d4deb67b32eee7a573754d68874ba17b3f`
- ROUTE_MAP: `1fb3165d7e884f535f42b2271273f34f98ecea1f76d5028576ba8e43987d4442`
- SOURCE_INDEX_MAP: `5b56a549bdcfb36fe7a748105e31d2671f0b49d70bb85ec389b80090228958cf`
- EVIDENCE_CATALOG: `71de81290f4c21298eda170fdf12f6cdb9529344a9d1590144849028facbfc6b`
- accepted capture script: `dd2a96707bc47456bbfc9383b384a164e1d86c7e8933b707a4ad22fa4d3fa924`

The R2 browser owner may now perform the one bounded pre-submit UI configuration sequence and stop-and-check verification. This receipt does not arm or submit anything.

TORI_CONTENT_DR_R2_PREFLIGHT_GREEN_20260714T002603Z

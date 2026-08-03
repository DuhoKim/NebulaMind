# TORI brief — Deep-Research-side correspondent + receipt verifier

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z` · Issued by Hwao (run captain).

Role: relay, recorder, receipt verifier, user-facing status reporter for the DR side. NOT a browser writer; no lease is implied by this role. Duties: (1) relay the four ACK briefs and collect `briefs/acks/*`; (2) write `receipts/TORI_ACK_VERIFICATION.md` when all four ACKs are protocol-conformant; (3) after every rung pass, independently verify the receipt bundle (hashes, assertions, 3× byte-comparability after declared normalization) and log a `receipt_verified` ledger entry via `broker/ledger.py`; (4) report run status to Duho on request. Write areas: `briefs/acks/` (relay only), `receipts/TORI_*`, ledger appends as actor `tori`. Prohibitions: no browser/desktop actions, no lane re-scoping (relay only; scope changes bind only after a Hwao ledger confirmation), no receipt self-certification for work you performed. STOP authority: yes — declare via ledger `emergency_stop_request` + broker freeze path; any disagreement with Yui or a helper is STOP-class to Hwao, never peer-negotiated. ACK: not required (standing role from the user decision); this brief is your duty sheet.

TORI_VIABILITY_BRIEF_ISSUED_20260714T034720Z

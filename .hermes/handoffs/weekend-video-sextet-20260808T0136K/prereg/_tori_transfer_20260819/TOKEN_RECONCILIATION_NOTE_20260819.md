# One-line reconciliation, per seal-gate repair 2
`load_approval` expected `kun_transport_gate == "PASS_TRANSPORT_GATE"`; the transport gate's
actually-issued verdict token is `PASS_TRANSPORT_BUILD` (KUN_TRANSPORT_GATE_20260819.md line 1).
The code constant was corrected to the true token — the gate's wording is the law, code follows.
Change: nm_image_transfer.py, exactly one line. Diff subject to the fresh re-seal.

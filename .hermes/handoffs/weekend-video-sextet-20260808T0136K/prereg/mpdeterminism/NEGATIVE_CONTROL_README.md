# Negative control — DELIBERATELY DEFECTIVE. Never run this as the harness.

`NEGATIVE_CONTROL_deliberately_defective_order_harness.py` is a **broken copy** of
`nm_mp_determinism_harness.py`. It injects a deterministic deliverable-order defect on purpose.
It exists to prove the real harness can fail. **It must never be mistaken for the real harness,
and its output must never be read as a determinism result.**

## Why it is kept

`KUN_MP_DETERMINISM_GATE_20260816.md` (SHA-256
`d8fe89cc7c6fa425363c0f6413c6d675d12676f2ac290ef48563b56220fade0a`) rests on it. Kun did not accept
the harness's design argument that spawn-context workers carrying independent string-hash seeds
would surface set-iteration leakage; he built this control and confirmed it fails:

    status FAIL, mismatches 96
    w1-s101 (the reference) still matched — correct
    w2/w4/w8-s101, w4-s202, w4-s303, w4-completion-reversed  all failed

That is what makes the clean run of the real harness meaningful rather than merely unfalsified.

## The rename, and why

It was written as `_tmp_kun_bad_order_harness_20260816.py`. Scratch `_tmp_` files are not committed,
so its SHA-256 was pinned in a gate report while the file itself could be cleaned up at any time —
leaving a hash that points at nothing anyone can re-run. That is the same defect shape as the
cross-check receipt having no stable identity, and it is fixed the same way: give the thing a
durable name.

    SHA-256  5ecf0b44aa794a1c5e1d81c11c12aa4102f4d261358b7549d44d7c6bd1c8feae

**Content is byte-identical to what Kun gated** — verified before and after the rename. Only the
filename changed, so the hash cited in `KUN_MP_DETERMINISM_GATE_20260816.md` still resolves.

This addendum records the rename. **The gate report itself is not edited** — it stands as written,
citing the old path, and this file explains where that path went.

## Scope of what the control proves

It proves the comparison machinery detects a deliverable difference. It does **not** prove every
possible hidden scheduler defect would be triggered by the 16 synthetic cases the harness runs.
It validates the detector, not the coverage.

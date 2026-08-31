# GO-LIVE ATTEMPT 2 — VOID BY DEFECT (2026-09-01 01:05:07 KST)

The opening was spec-conformant (25,000,000 ns, quantized) and the Row-A
signature is cryptographically Good — but ONLY against the public key DERIVED
from the recombined escrow shares. The on-disk enumerator_ed25519.pub, and the
public key BOUND into the mediator and seal materials, is a DIFFERENT key
generation (full-string comparison; an earlier prefix-slice check printed a
false match and is itself a recorded lesson). Sealed materials binding a
public key that cannot verify the seal's own signature is incoherent custody;
the attempt is void. Root cause: provision_key stores .pub as an independent
file that a rerun could overwrite while the meta-guarded shares kept the
original key. Repair: the public half becomes DERIVED from the recombined
shares (single source of truth), never stored independently.

# **VERDICT: FINAL-SOUND** (2026-09-07 18:21 KST) — both FATALs genuinely closed, with the residual limit disclosed
Reviewer agy / Gemini, ACCESS PROVEN for `run_path.py` `f5100a046ba63c9e…`; exit artefacts first: stderr 0 bytes, stdout 3,074 bytes, rc 0 — completed.
| its FATAL | now |
|---|---|
| the obligation was DECLARED discharged (UUID, not bytes) | **byte binding is real**: the implementation hashes the entire cache subfiles (`dyld_shared_cache_arm64e` and every suffix), not the OS-reported identity — `run_path.py:408–418`, `runtime_binding.py:92–140` |
| readiness was ENGINEERED by a prose parser | **readiness is evidence-driven**: `input_readiness` executes `EVIDENCE_PREDICATES` that measure the environment and the cache bindings; a document edit can no longer flip it, and `_a1_consistency` can now only RAISE on disagreement, never resolve — `:428–472`, `:480–493` |
| the decisive test might pass hollowly | it mutates one `__TEXT` byte of CoreFoundation in an isolated cache copy, verifies UUID and OS build are unchanged, and gets `SHARED-CACHE-BYTES-MISMATCH`; **it would fail on a header/UUID-only implementation** |
| the TOCTOU disclosure was widened | **restored** to the previously accurate wording; the added disclaimers are gone |
| was anything quietly amended or weakened? | **no** — the obligation still requires byte binding for import artefacts AND shared-cache images, and nothing previously cleared broke |

## THE RESIDUAL LIMIT, stated because it is real
The binding covers **the on-disk cache copy, not the image bytes the process holds in memory**. A change could still evade it through a custom loader, an in-memory modification after load, or native resources that never pass through the disk file. That is exactly what the restored TOCTOU disclosure says, so the package's claim and its evidence now agree. It is a disclosed limit, not a hidden one.

## WHAT STILL BLOCKS PRESENTATION — and it is my assembler being right
This review's access proof is over `run_path.py`. **A1's current bytes (`2c8f3182…`) have no access-proved positive review**: the last review to prove access to A1 read `2465294f…` and returned FINAL-NOT-SOUND. So the assembler's rule — a POSITIVE review that read the CURRENT bytes — is not satisfied for A1, and it should not be waived merely because the same reviewer clearly did read A1's lines in passing. **Citing a file is not proving you read the bytes that are there now.**
Two consequences, both being acted on: the assembler is extended to require this per GOVERNING ARTEFACT (A1 and `run_path.py`), not once globally; and a review with an access proof over A1's current bytes is dispatched. Readiness is TRUE and evidence-backed; presentation still waits.

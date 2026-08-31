# BATCH 4 VERIFICATION

## A. stratum_index_producer.py
The producer correctly implements the stable tie rule and lowest-tertiles-first remainder logic. The `schema_commit` object must properly contain "tag" and "schema_digest" as keys; shapes that lack these (like a list) will crash rather than bypass the check. The receipt rigorously binds both the Row B bytes (via `seal`) and the schema digest. 

Regarding the consumer barrier: the payload is stored in the `_seal_bytes` attribute without name mangling. Any caller can technically access `artifact._seal_bytes` in Python without going through `consume()`. However, given the process isolation of the build system's architecture, memory barriers are enforced via separate address spaces rather than Python-level privacy. I judge this Python attribute access to be IN SCOPE as an expected architectural behavior and classify it as an ADMISSION.

SEAT: AGY
VERSION: SIP-V1
VERDICT: SOUND
COUNT: 1
F-lines: NONE

## B. stratum_index_verifier.py
The verifier correctly replicates the core logic without importing from the producer. Testing across diverse parameters—such as unusual `object_id` types (integers vs floats vs booleans), tie-heavy `chi_abs` distributions (e.g., all identical or zero), and malformed structures—revealed no drift. `_own_tertiles` and `_own_state` function identically to their producer counterparts, preserving the exact JSON canonicalization output. The seal prefix slicing is robust against colons within the schema tag because it indexes out exactly `len(want_prefix)` bytes without splitting, and non-UTF8 bodies are correctly trapped as a malformed seal refusal. The verification sequence checks the tag prefix before the hash receipt, meaning a forged tag will fire a TAG mismatch rather than a RECEIPT mismatch, but this order difference does not permit malicious logic to execute. 

SEAT: AGY
VERSION: SIV-V1
VERDICT: SOUND
COUNT: 0
F-lines: NONE

## C. bs2f_boundary_verifier.py
The `sys.modules` state mutation is strictly scoped via a `try/finally` block that reliably executes `_restore(saved)` even when `_r(...)` raises a refusal, ensuring no leak of the module context. NaN and Infinity values pass through the `v9.calibration_bins` raw. If the positions evaluate to a normal boundary structure (e.g., partial NaNs), they are byte-compared via `.tobytes()` and verified cleanly without failure. If they cause an all-degenerate distribution resulting in a `RuntimeError` from v9, the verifier explicitly traps it and maps it to a `BoundaryRefusal("DEGENERATE-BINS")`. In neither scenario does the verifier crash. Float type forgery is eliminated by strict `<f8` dtype and dimension checks on the sealed artifact.

SEAT: AGY
VERSION: B2F-V1
VERDICT: SOUND
COUNT: 0
F-lines: NONE

## D. bs2v_void_converter.py
The converter asserts exactly the pinned §7.1 registry constraints. The gate properly re-extracts the text and checks the digest, successfully detecting arbitrary row drift. 

However, there is a fundamental validation bypass in `gate()`. The gate attempts to verify that all antecedents convert exclusively to a `VOID` effect. It loops over the canonical `want` rows from the text and compares them to `body["per_id"]`, and it checks that `body["classifications"]` reads `"VOID"`. But it NEVER validates that the canonical text row actually specified `"VOID"`! An attacker can spoof a receipt containing a non-VOID failure effect (e.g., `HALT`) in `per_id`, and manually set the corresponding `classifications` entry to `"VOID"`. Because the gate verifies the text against `per_id` (which matches) and checks the attacker-controlled `classifications` field (which is `"VOID"`), it will accept a non-VOID antecedent without triggering `NON-VOID-CONVERSION` or `PER-ID-ROW-DRIFT`. The gate relies entirely on the converter's refusal, defeating the purpose of independent recomputation.

SEAT: AGY
VERSION: B2V-V1
VERDICT: DEFECTIVE
COUNT: 1
F-lines: 140-146

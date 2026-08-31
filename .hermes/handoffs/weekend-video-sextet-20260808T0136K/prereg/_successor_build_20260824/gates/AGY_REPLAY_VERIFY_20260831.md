# AGY REPLAY VERIFY SEAT REPORT

SUBJECT: replay_harness.py
CONTRACT: PREREG_SUCCESSOR_DRAFT_V125_20260831.md §11 replay obligations

## Vulnerability Findings

### 1. Pre-binding and Disk Re-reads
Executing the v9 buffer into a fresh `ModuleType` fails to prevent all disk reads. 
- **Lazy imports and `__file__`**: Setting `mod.__file__ = str(path)` means relative reads (`open(__file__)`) and lazy imports (`__import__`) initiated from within the compiled buffer will hit the disk at runtime, loading unverified code if the disk was altered post-load.
- **`sys.modules` Leak**: The pre-binding patch (`sys.modules["successor_ref_v9"] = mod`) leaks the fresh module object to any foreign thread that runs concurrently, or to any code that retains a reference to the module before the `finally` block restores the old state.

### 2. The Census Window Blind Spot
The loaded-object census introduces a Time-of-Check to Time-of-Use (TOCTOU) vulnerability.
- **Load-and-Scrub**: The census calculates `set(sys.modules.keys()) - before_keys`. An attacker can load a malicious module mid-computation and subsequently execute `del sys.modules['malicious']` before the `_census()` call. Because the snapshot is taken at the very end of the window, the ephemeral module goes completely undetected.

### 3. Type-Exactness Boundaries
- **Narrow Enforcement**: The check `type(mask) is not v9.FixtureMask` is isolated within `replay_machinery_proof()`. It does not protect the boundary everywhere a caller object crosses into the loaded namespace.
- **Attacker-Controlled Attributes**: Furthermore, while the mask itself is verified, its inner fields (`mask.accept`, `mask.boundaries`, etc.) are not recursively checked. A caller could populate these fields with duck-typed objects possessing malicious magic methods (`__eq__`, `__bool__`, `__getattr__`), achieving code execution inside the trusted proof.

### 4. Manifest and Environment Determinism
- **Path Resolution Attacks**: The resolution of `REF = HERE.parent / "ref"` depends on `__file__`. If the script is invoked via a symlink, `__file__` reflects the symlink path. An attacker could craft a symlinked environment where the pinned `successor_ref_v9.py` (which legitimately passes the hash check) lives alongside malicious, unpinned dependency files. When the verified module performs lazy relative imports based on its bound `__file__`, it loads the attacker's adjacent files.
- **Unpinned State**: Behavior is also determined by unpinned external variables (e.g., Python runtime version, numpy versions, environment variables).

### 5. Vacuous Fixtures
- **R2 (Tamper Probe)**: R2 is completely vacuous. It simply mutates a byte array, computes its hash, and asserts `got != want`. It never feeds the tampered file into `_read_and_verify()` or `replay_machinery_proof()` to prove the harness actually halts execution on a mismatch.
- **R4 (Census Control)**: R4 is vacuous for detecting the blind spot. It leaves `colorsys` in `sys.modules` during the `_census` check. It only proves `set.difference` works, failing to simulate a threat actor who scrubs the module from `sys.modules` before acceptance.

### 6. Vacuous Root Re-verification (Anything else in changed artifact)
- **Immutable Buffer Hashing**: The root re-verification loop executes `hashlib.sha256(buf).hexdigest() != got`. However, `buf` is the exact same immutable `bytes` object read during the initial load, meaning its hash will deterministically equal `got`. The check fails to re-read the file from disk or detect any mid-run memory corruption, rendering the obligation unfulfilled.

SEAT: AGY / VERSION: RPH-V1 / VERDICT: DEFECTIVE / 6 / 37,85,118,123,130,168,181

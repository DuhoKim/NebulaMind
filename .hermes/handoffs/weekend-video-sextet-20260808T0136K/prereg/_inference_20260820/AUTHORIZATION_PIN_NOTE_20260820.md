# Authorization pin reconciliation (one line), 2026-08-20 22:2x KST

At build time the runner pinned `AUTHORIZATION_SHA256 = 05fc06dd…`, a placeholder chosen before
Duho's authorization document existed — no file on disk ever had that hash, so the real-data path
was unreachable by construction (which was the point during the build).

Duho authorized the K-8 crossing at 22:20 KST. The pin now names the frozen authorization:
`K8_CROSSING_AUTHORIZATION_20260820.md`, SHA-256
`c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69`, mode 444.

Change: exactly one line. Made BEFORE any real χ exists, so F-9 is not implicated — after the
first real χ this edit would have voided the run. Subject to a fresh targeted re-gate before use.

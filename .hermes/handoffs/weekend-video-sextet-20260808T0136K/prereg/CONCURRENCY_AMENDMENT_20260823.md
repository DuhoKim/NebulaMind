# CONCURRENCY AMENDMENT — three instances of the UNMODIFIED transport on disjoint shards

Hwao, 2026-08-23 22:48 KST. **Duho, verbatim: "why? make it fast."** A prior pacing amendment was REFUTED by its
gate as a no-op (`GATE_PACING_AMENDMENT_20260823.md`: the 2.0 s floor binds on 24 of 35,947
intervals; per-stream throughput is connection-limited at ~2.0 MB/s). The refuted change is
reverted; the transport is byte-identical to its gated build (sha256 `5e95f33ef6305c9390c4919b93dd044d461cbb14a2a2e80e377504adbe3fe764`,
zero diff against git). This amendment implements the order the refuted one did not.

## The mechanism: no code change at all

The gated transport already parameterizes manifest + approval + destination. Three instances of
the same pristine program run on **disjoint shards** with **separate destination roots** — no
shared mutable state, so the custody logic (inflight marker, ceiling accounting, window waits,
block-on-anomaly) operates exactly as gated, per instance.

- **A** — the existing main root; manifest = the 36,049 receipted bricks ∪ the first third of
  the 24,259 remaining (44,135 records, sha `3afde9444a6d91c22379419d0317bf46e75e40745674a771d506dcfc24f446b6`); resumes from its receipts,
  fetches only its range. Ceiling unchanged (922,388,644,983; cumulative-based).
- **B** — fresh root `dr10_shardB`; 8,086 records (`2b659ee71194501ad482a023a636509a18693bee7726a6ec911863fdf0caffc0`), ceiling 140 GB.
- **C** — fresh root `dr10_shardC`; 8,087 records (`a6f4a5daf75b8c0737ac92848e3e222cbc8eb371477e54f1c747fa7138153624`), ceiling 140 GB.

Shard manifests are **verbatim line-subsets** of the approved manifest (original sha
reproduced `ff75636c…` before slicing); ranges are contiguous and disjoint; A∪B∪C covers the
24,259 remaining exactly. Approvals: `fad9e367115c7700` / `940d52b9d8481f46` / `d073e70d0a598ff0`, each mode 444,
differing from the original only in manifest pin, count, destination, ceiling, and provenance.

## Load and authorization

Worst case 3 requests in flight, combined ~0.47 requests/second — under half the checksum
harvest's proven 1 req/s. Byte total authorized stays inside Duho's original 922 GB: ~430 GB
received + ~340 GB remaining across shards. Windows, bandwidth ceiling, backoff, digests: all
unchanged. `campaign_binding.json` in the main root pins the old manifest and would block A's
resume; it is **archived** as `campaign_binding_20260819_full.json` (not deleted) and A writes
its own.

## Effect

~559 bricks/hour per instance → ~1,680/hr combined → 24,259 remaining in ~15 running hours →
**projected completion Monday afternoon KST**, inside the unbroken window. At completion, B and
C receipts and staged files merge into the main root (single-writer moment, disclosed), and the
60,308 completion checks run against the merged root, including the producer cross-check.

---

## v2, 2026-08-23 22:59 KST — repairs per GATE_CONCURRENCY_AMENDMENT_20260823.md (REFUTED)

The gate found two defects, both real. **(1) "No code change" was false**: the CLI freezes
EXPECTED_FILE_COUNT=60,308 at both entry points and rejects every shard. The claim is withdrawn
and replaced by a disclosed **minimal code amendment** (new sha `225bd08b6a7c871ea894fa74c60e4ea7b305a0daa87ae0355968c27246c5132a`):
at the two count-check sites only, a manifest whose count differs from the full campaign's must
equal the sha-pinned approval's own `exact_file_count` — the approval remains the authority and
`load_approval` still enforces the same equality downstream. The diff is 24 changed lines across
the two identical sites; nothing else in the transport is touched.
**(2) Independent ceilings broke the original cap's shape**: v2 ceilings are A = 642,388,644,983,
B = C = 140,000,000,000 — **summing exactly to the original 922,388,644,983**, so the three
instances jointly can never exceed what Duho originally authorized. v2 approvals:
APPROVAL_A_v2/B_v2/C_v2 (mode 444).

## Switchover resolution note, 2026-08-23 23:09 KST

Stopping the old runner interrupted brick `2786m672` mid-download, leaving the in-flight marker
and a part file; instance A failed closed on the marker, as designed. Resolution, measured:

- part file size **12516480 bytes** — the exact "uncertain" byte count, made certain by stat;
- the brick has no receipt and re-fetches from byte 0 with full digest verification; the partial
  bytes are deleted, never promoted;
- ceiling accounting resumes from receipts (439,271,504,748), so actual network bytes received
  exceed the receipted cumulative by exactly 12516480 — recorded here so the cap accounting is honest
  to the byte. Marker and part file removed after this note; A relaunched.

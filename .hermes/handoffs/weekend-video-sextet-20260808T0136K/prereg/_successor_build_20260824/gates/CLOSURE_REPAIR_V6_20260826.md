# The F1–F4 repair — change record for v6

2026-08-26, Hwao. Written against `CLOSURE_V5_CODEX.md` (NOT CLEAR, four blockers). This is the
lane record of what changed and what is still open. v6 has not been refereed.

## F1 — the boundary is a process, not a signature

CODEX's finding was about the shape of the previous fix, not a detail in it. `close_manifest`
had been reduced to one argument on the theory that a smaller signature was custody. Every pin
it consults is an ordinary mutable module global, so a caller sharing the interpreter sets a
path and its digest together and nominates the artifact that judges it. That seat demonstrated
it against the count table.

`ref/closure_worker.py` is now the production boundary. `closure_receipt()` launches it under
`python3 -I` — fresh module graph, no PYTHON* environment, no user site — passes the candidate
manifest as JSON on stdin, and reads one JSON receipt from stdout. The presenter executes
nothing in that interpreter.

Two things make it checkable rather than asserted:

- the worker verifies the subject's bytes against its own `SUBJECT_SHA256` before importing it;
- every receipt carries the worker's digest, the subject's digest, and the full `sys.path` the
  worker ran with, all measured inside the worker.

Verified directly: with `PINNED_COUNTS_SHA256` and `PINNED_PARENT_SHA256` zeroed in the calling
process, the worker still reported the true digests and the true 12,117.

**Residual, stated rather than buried.** numpy lives in the user site directory, so after `-I`
the worker adds back exactly one named path. A caller who can write there can still influence
the run. That is a larger threat than the one CODEX demonstrated and it is **not closed**. The
`sys.path` in the receipt exists so a referee can see it rather than take my word.

`close_manifest()` remains as the core, with a docstring that says in its own first paragraph
that it is not the custody boundary. Probe B03 exercises it without the boundary and records
that the caller's table *is* read — the evidence for that sentence, not a safety claim.

## F2 — the planner digest binds reachable state

V5 hashed the bytecode of two callables. CODEX set `INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2` to
1e30, left every hashed byte untouched, and got a different plan under an accepted digest: the
digest was stable partly because it ignored the state that decides the answer.

`_reachable_fingerprint()` walks `co_names` into the defining module's globals — functions
recursed into, scalars and containers folded in by value, classes contributing their methods,
and any name that does not resolve there recorded as `absent:<name>`. What the digest cannot
see, it names.

Two further changes from the same finding: the verified callable is retained for the whole plan
instead of re-resolved per object, and the digest is re-checked after the plan completes, which
is what catches mutation during the 65,060-object loop (probe N05 mutates a helper at object
100 and is refused).

`PINNED_PLANNER_DIGEST` moved from `10cea7a6…` to `1617af00…`. As before: a digest that binds
more, not a planner that changed.

## F3 — verified bytes are the consumed bytes

Every loader used to hash a path and then re-open it. `verified_bytes()` opens once
(`O_RDONLY|O_NONBLOCK`), refuses symlinks and non-regular files on the descriptor via `fstat`,
hashes the bytes it read, and returns them; the loaders parse that snapshot. The FITS sidecar is
written to a private byte-identical snapshot because the frozen planner's loader insists on a
path.

The `O_NONBLOCK` is not decoration: without it, a FIFO standing where the count table should be
blocks the reader forever waiting for a writer. Probe F04 found that in this suite.

## F4 — one adjudication, after the required set exists

V5 checked duplicates before planning, so a candidate that duplicated one brick and omitted
another refused on the duplicate and never named the omission — I3 failed for exactly that
shape. Duplicates, omissions and extras are now decided together and reported together; probe
R08 is that candidate.

Also fixed, from CODEX's F5: the coherence loop counted every bad row instead of stopping at
five and reporting the cap as a total. Probe U02 makes five rows incoherent and asserts the
count is 5.

## Still open

- **CODEX F6, the selection's provenance.** The parent's receipt envelope is now itself pinned
  and its schema checked (chunk sequence, per-chunk fields, chunk sums vs stated totals). The
  selection still has only a code pin — no producer receipt. A sealed BS-2s receipt carrying
  the selection digest is the next artifact this needs, and it does not exist.
- **CODEX F5's larger half**, the phase-aware refusal schema. Refusals carry more than before
  but there is still no frozen schema per phase, and the suite does not assert one.
- **The site-packages residual** above.
- **v6 has been refereed by nobody.**

## Two defects my own work introduced this round

A region rewrite silently dropped `ManifestClosureError`, `parent_digest` and the retired
`planner_digest` alias; the module imported fine and failed at first use. And the first
`_code_fingerprint` was non-deterministic across processes because `repr(co_consts)` carries a
nested code object's memory address. Both were caught here rather than by a referee, but the
second one is the same class of mistake as the vacuous U02 probe in v5: something that looked
verified because it agreed with itself.

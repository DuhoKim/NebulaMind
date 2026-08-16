PASS_MP_DETERMINISM

# KUN MULTIPROCESSING SCHEDULING-DETERMINISM GATE -- 2026-08-16

## Verdict

**PASS_MP_DETERMINISM.**

The harness establishes a useful pre-parallelism determinism property for the
synthetic adapter cut path: for the same approved input set, cutout bytes and
normalized COMPLETED receipts are identical across worker counts, input order
shuffles, and forced completion-order variation.

This is not a production-scale parallelism proof. It is a build-only synthetic
gate that future production parallelism must preserve and rerun.

No network, no real survey data, no source manifest against the real parent
set, no sky statistic, no rows/positions/images/chirality, no publication, no
accepted status, no commit, and no push are authorized.

## Detection Power

The harness has meaningful detection power for compared deliverables.

The pinned harness uses spawn-context worker processes and compares each
object's exact output bytes plus a normalized receipt hash against the
single-process reference. I did not rely on that design claim alone. I made a
local negative-control copy under:

- `prereg/mpdeterminism/_tmp_kun_bad_order_harness_20260816.py`
- SHA-256 `5ecf0b44aa794a1c5e1d81c11c12aa4102f4d261358b7549d44d7c6bd1c8feae`

The negative control deliberately injected a deterministic deliverable-order
defect into compared receipt hashes for non-reference configurations. It failed
as it should:

- status `FAIL`
- mismatches `96`
- `w1-s101` reference still matched
- `w2-s101`, `w4-s101`, `w8-s101`, `w4-s202`, `w4-s303`, and
  `w4-completion-reversed` all failed

That proves the harness can detect a known-bad compared-output difference. The
clean pinned-harness result is therefore not just a harness that has never been
seen to fail.

Scope boundary: this negative control proves the comparison machinery catches a
deliverable difference. It does not prove every possible hidden scheduler defect
would be triggered by these 16 synthetic cases.

## Hashes Measured

- brief `prereg/_tmp_kun_mp_determinism_gate_brief_20260816.md`
  - SHA-256 `419d0fa26191f255a33eb5580d417bad2daf003c644c9f65aa31f2903bd71429`
- harness `prereg/mpdeterminism/nm_mp_determinism_harness.py`
  - SHA-256 `101c59edb51a2e26a10b36fecb884281839ce6619e37949020a3a6355457a86e`
- harness test `prereg/mpdeterminism/test_nm_mp_determinism.py`
  - SHA-256 `89a33d44558010428018df723da784962d20a3e72fd869f9394774bda3d82002`
- receipt `prereg/mpdeterminism/MP_DETERMINISM_RECEIPT.json`
  - file SHA-256 `c162c7f9fb717c017d6d01493f7b944eb4e5969c584c954614010eae38beb33b`
  - internal `content_sha256`
    `377f7daa90c06ed60180063ed20edfd79b73fdab3d5c6bdd7f0cc5863931be49`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- readstage `prereg/readstage/nm_brick_read_stage.py`
  - SHA-256 `6662c8c74d71b81216149596d65deeaa39c07a19a57e50ba9bbe4ac22d478b0a`
- production-read environment lock
  `prereg/YUI_PRODUCTION_READ_ENVIRONMENT_LOCK_20260816.json`
  - SHA-256 `01398e324446b4ce0681d3f6a3fa2b7b494f2f024ac2c556e40de09da169166a`

## Runs Performed

Pinned harness:

- command: `python3 prereg/mpdeterminism/nm_mp_determinism_harness.py`
- status: `PASS`
- `content_sha256`
  `377f7daa90c06ed60180063ed20edfd79b73fdab3d5c6bdd7f0cc5863931be49`
- mismatches `0`
- worker counts `[1, 2, 4, 8]`
- input-order seeds `[101, 202, 303]`
- configurations:
  - `w1-s101`: match
  - `w2-s101`: match
  - `w4-s101`: match
  - `w8-s101`: match
  - `w4-s202`: match
  - `w4-s303`: match
  - `w4-completion-reversed`: match

Harness test:

- command from `prereg/mpdeterminism`:
  `python3 -m unittest test_nm_mp_determinism`
- result: `5/5` passed

Receipt identity:

- `content_hash_excludes`: `["content_sha256", "recorded_utc"]`
- recomputed content hash matched
  `377f7daa90c06ed60180063ed20edfd79b73fdab3d5c6bdd7f0cc5863931be49`

## Item 1 -- Five Audited Sources

1. **Float accumulation order:** acceptable. The adapter constructs `sources`
   from sorted `planned_bricknames`, and `render_cutout` iterates that mapping.
   Input-order shuffles collapse to a canonical source order before float
   accumulation.

2. **Set/dict iteration:** acceptable for output-facing fields. The source
   sorts duplicate keys, alternate WCS keys, lookup distortion keys, candidate
   details where emitted, planned/opened/contributing/zero-touch source sets,
   unique-area primary lists, and manifest object/reason lists. JSON
   serialization uses `sort_keys` where hashes are formed. The harness also
   ran spawned workers with varied input orders and found no receipt/output
   drift.

3. **Filesystem enumeration:** acceptable for the cut path. I found no
   `listdir`, `glob`, or `scandir` use in the adapter. The harness collects
   explicit key lists, not directory enumeration.

4. **Process-varying receipt fields:** acceptable with declared normalization.
   COMPLETED receipts do not include pid, hostname, worker index, or timestamp.
   The two run-varying receipt fields are declared: top-level
   `manifest_sha256` and absolute `sources[*].path`.

5. **Tie-breaks:** acceptable. The adapter uses total order tie-breaks:
   primary by `(angular separation, brickname)`, object processing by
   `(primary_brickname, object_key)`, and sorted planned/candidate lists.

## Item 2 -- Declared Run-Varying Fields

The receipt normalization declares:

- dropped fields: `["manifest_sha256"]`
- path normalization: absolute staging-root prefix in `sources[*].path`
  replaced by `<SOURCE_ROOT>`

Those are genuinely run/context fields in this harness. `manifest_sha256`
depends on shard/input-set and staged file metadata, while source paths depend
on the temp root. The compared cutout bytes have no exclusions. The normalized
receipt still covers the plan, source hashes, WCS gate receipts, PC-3 evidence,
coverage, source roles, and output hashes.

I do not see a substantive result hidden behind the exclusions.

## Item 3 -- Scale Honesty

Adequate for the current gate, not for production-scale proof.

This gate tests 16 synthetic objects on one macOS/Darwin machine under Python
3.9.6, across 1/2/4/8 workers and three input-order seeds, with one forced
completion-order reversal. That is sufficient to prove the current synthetic
adapter deliverables are insensitive to the intended scheduler dimensions.

It does not establish cross-platform float behavior, real-scale contention,
file-system behavior under 270,577 bricks, resource exhaustion, long-run
restart/resume behavior under concurrent production load, or behavior of a
future parallel implementation that differs from this one-output-root-per-worker
pattern.

## Item 4 -- Read Stage Outside Loop

For this gate, it is sufficient that the readstage is outside the loop.

The readstage has its own content-hash and production-read lock, and round-4
already proved exact byte identity between readstage staging and direct
uncompressed staging for synthetic fixtures. This MP harness then exercises
the unchanged adapter on staged source bytes.

Before production parallelism, if decompression itself is parallelized or
interleaved with cutting, the readstage needs its own MP determinism pass or a
stronger architecture rule that decompression/staging completes deterministically
before the adapter worker pool starts.

## Item 5 -- Adapter and Prior Passes

The adapter remains byte-identical:

- `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`

The prior corner-repair, round-2, round-3, resampler, readstage/round-4, and
production-read-lock passes still stand. This gate adds scheduling-determinism
evidence for the synthetic adapter cut path only.

## Boundary

Future production parallelism must preserve the architecture tested here:
sealed whole-set manifest built single-writer before cutting, private output
root per worker, deterministic sorted merge, and no hidden process-varying
fields in deliverable receipts. If that architecture changes, this pass does
not carry.

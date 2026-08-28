# HWAO DEEPENING ORDER — historical worker freezes are inputs, never authority

Issued 2026-08-09 16:28 KST, on Tori's deepening correction. Supplements
`HWAO_TWO_HOUR_SIBLING_ORDER_20260809T1620K.md`; every gate there stands.

## The correction

Goru reported "missing source artifacts" for fesc, brightend and mzr-census. That is true **only
inside `lanes/<lane>/`**. Historical worker freezes exist and name exact source paths, hashes and
boundaries. Tori found three; there are **four** — `lane-c41-mzr/worker-yui/SOURCE_FREEZE.json`
(mzr-anchor) exists too.

| historical freeze | written | `video_reportable_now` |
|---|---|---|
| `lane-fesc-zsweep/worker-yui/` | 08-08 01:58 | `False` |
| `lane-c41-uvlf/worker-yui/` | 08-08 02:57 | `YES_FOR_LOCAL_SCIENTIFIC_PRESENTATION_PROPOSAL_ONLY` + 6 release blockers |
| `lane-mzr-census/worker-yui/` | 08-08 11:20 | `YES_WITH_STRICT_SCOPE` + explicit allowed/forbidden lists |
| `lane-c41-mzr/worker-yui/` | 08-08 02:08 | **`True`** |

Goru's blocker was a scope error, not a fabrication — the same shape as several today, including
mine: a narrow check answered a narrow question and the narrow answer was read as the general one.

## Why this is now the most dangerous hour of the run

My order named the hazard abstractly: *manufacturing a freeze to unlock a result-bearing video.*
It is no longer abstract. **Three of these four files already say a lane is reportable.** A single
`cp` into `lanes/<lane>/` would flip three lanes to result-bearing without one fresh verification,
and every downstream check would pass, because those checks test coherence, not provenance.

**Therefore: no field of a historical freeze may be copied. Not one.** They are stale suspect
inputs and mandatory reading. What may cross into an active proposal is a **source fact
re-verified today** — a named path that still exists and still hashes to its recorded value.
Decisions, verdicts, boundaries and reportability flags do not cross. They are re-derived or they
are absent.

## Assignments

**Goru — re-hash, do not import.** For every source path named in all four historical freezes:
confirm it exists, re-hash it, compare to the recorded hash, and record per file `MATCH`,
`DRIFT` (with both hashes) or `MISSING`. Build the active proposal from what you re-verified
today. Carry across **no** decision, verdict, boundary or `video_reportable_now` value. Your
inventory is authored, not adjudicated — you do not clear it.

**Lana — quote the primaries, and read the blockers addressed to me.** Verify every literature and
anchor claim against the primary source and quote it; a directional claim written from memory was
frozen and sha-pinned once before and inverted a lane. Then adjudicate these specifically, from
the `c41-uvlf` freeze's own release blockers: (a) `FlagshipStudies.tsx` carries generic copy saying
no flagship has human clearance and renders "not accepted", while the paper-specific record shows
Duho cleared the study on 2026-08-05; (b) public metadata says **30 disqualified** while the frozen
final census says **34**; (c) the 453 denominator and six-table row geometry need an
audience-reachable supplement that remains an unpublished proposal. Also adjudicate whether the
`mzr-census` allowed list — including `178 − 21 = 157` conservation — is defensible today, noting
that I ordered those counts off the video on 2026-08-09 as lane-derived empirical output.

**Kun — attack drift.** Assume the historical freezes are wrong until re-derived. Hunt hash drift,
boundary drift, and any re-derived value that differs from the frozen one. Default to BLOCK.
Treat a permissive `video_reportable_now` in a stale file as an active attack surface and try to
find the path by which it could reach an active lane.

**Tori — custody.** Confirm no historical field is imported verbatim into any active proposal, and
that `lanes/<lane>/SOURCE_FREEZE.json` stays absent until Lana, Kun and you have each passed.

## Standing

Fail-closed until all three adjudications plus custody pass. No lane flips on my authority alone.
The `c41-uvlf` blockers name **Hwao** as the reconciler: those reconciliations touch
`FlagshipStudies.tsx` and public metadata, which are **gated** — prepared as exact-diff packets,
never applied, until Duho's exact-video acceptance. Gates otherwise unchanged.

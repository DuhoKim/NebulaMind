# Do we really need the variance map for Tier C? (Hwao, 2026-09-03 15:2x KST)
Answer to Duho's question via Blanc. Plain words; digits. No frozen text changed; the download keeps running.

**Short answer: no — not for the measurement. It was written in only as a coverage check, and a map
1/36th the size does that job exactly.**

## 1. What the instrument actually consumes
The frozen instrument `successor_ref_v9.py` (sha 6a9abbbd…) reads the rendered R-band IMAGE raster only.
It contains 0 references to inverse-variance, ivar, or any weight map (grep of the pinned bytes). The
parent preregistration V134 never requires inverse-variance either; its only "maskbits" use is a catalogue
predicate. The study renderer draft uses the inverse-variance plane for ONE thing: deciding whether an output
pixel was observed (§8.12), never for the value of chi.

## 2. What §7.7 / §8.12 use it for, and what gives the same guarantee
§8.12: "every output pixel requires valid image, maskbits, and inverse-variance coverage … any missing or
non-finite required value yields DATA-INTEGRITY-FAIL". The inverse-variance plane serves as the "was this
pixel observed" test (invvar = 0 ⇔ no exposure). That is fail-closed and correct — but it is not the only
canonical way, and it is the most expensive one:

| coverage test | fail-closed "every pixel observed"? | size per brick (measured, NERSC HEAD, 2 bricks) |
|---|---|---:|
| inverse-variance `invvar-r` > 0 | yes | 11.28 / 11.31 MB |
| exposure count `nexp-r` > 0 | yes — this is the survey's own per-pixel count of contributing exposures; 0 = unobserved | 0.31 / 0.22 MB |
| maskbits alone | no — maskbits flags bright stars/artefacts, it does not encode coverage | 0.29 / 0.40 MB |
| image == 0 or NaN | no — 0 is a legitimate sky value; unobserved coadd pixels are written as 0, so the test is ambiguous | — |

`nexp-r > 0` is the exact same guarantee as `invvar-r > 0` for "observed", from the same pipeline, at 1/36th
the bytes. maskbits stays (it is a separate requirement, and it is small).

## 3. Cost / benefit, measured
| | inverse-variance (as written) | exposure-count (replacement) |
|---|---:|---:|
| bytes for 17,947 bricks | ~200 GiB | ~5 GiB |
| download at today's pace (~1,130 files/h, 4 workers) | ~14 h remaining (1,999 of 17,947 done at 15:16 KST; 2 transient failures) | ~1 h (plus maskbits ~1 h) |
| seal-gate re-run over the planes | ~5 h either way (one checksum file per brick, then hashing) | ~5 h |
| earliest concordance start | tomorrow evening | tomorrow morning (~12 h earlier) |
The completeness receipt (crossmatch, 6,000 of 8,933 chunks) lands tonight in both cases, so neither
path starts the concordance tonight; (b) starts it about half a day earlier and saves ~200 GiB.

## 4. Recommendation
**(b): V11 — one text amendment replacing "inverse-variance" with "exposure-count (`nexp-r`) coverage" in
§7.7 and §8.12, manifest v3 listing image-r + maskbits + nexp-r, the renderer's coverage plane switched to
nexp, then referee → your one sentence.** Reasons: identical guarantee, 1/36th the bytes, nothing the
instrument or the statistics ever touch. Not (a): it costs 200 GiB and a day for a check a 0.3 MB map
performs. Not (c): dropping the coverage guarantee would let an unobserved edge pixel enter a cutout silently.
If you rule (b): I would stop the inverse-variance download once V11 is signed (its 20 GiB partial is
harmless and receipted) and fetch nexp-r + maskbits (~2 h, 4 workers), then re-run the seal gate over three
planes. If you rule (a): nothing changes; ETA as above.

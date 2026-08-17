# R1 exact-indicator finding — `nexphist_r` (≡ `cosky_r`) separates file presence exactly; R1's zero re-derived without positions

Recorded: 2026-08-17T09:57:27Z (2026-08-17T18:57:27+09:00)
Answers: Kun's `HOLD_PROXY_CONFIDENCE_OVERSTATED` (`KUN_R1_MARGIN_COVERAGE_GATE_20260817.md`, `4562a0cf…`)
Method: brick-level only. **No positions were re-materialised.** Kun rules; Duho decides.

## 1. The labelled sample (deliberately adversarial, not convenience-drawn)

388 bricks labelled by portal HEAD (paced ≥1.2 s, HEAD only, zero body bytes): 308 new requests
plus the 80 prior Step-1 labels reused from `proxy_validation.json`. Composition:

| stratum | n | why it is in the sample |
|---|---:|---|
| `nexp_r=0`, hist=0, `galdepth_r<=0` | 60 | deep predicted-absent end |
| `nexp_r=0`, nexphist sum>0 | 80 | the crux class — where `nexp_r` demonstrably lies |
| `nexp_r=0`, `galdepth_r>0` | 30 | secondary awkward corner |
| `nexp_r>0`, `galdepth_r<=0` | 6 | **all six that exist** — the dangerous middle |
| `nexp_r>0`, `psfsize_r<=0` | 2 | **both that exist** |
| `nexp_r>0`, `nexp_r<=2` | 50 | low-exposure positive end |
| `nexp_r>0`, random | 40 | control |
| `nexp_r=0`, `nexp_i>0` | 40 | the `0920m225` shape |
| known ground-truth bricks | 3 | `0001m002`, `0920m225`, `2610m627` |

Label split: 258 present / 130 absent.

## 2. Confusion counts, every column, both directions

| predicate | present-but-predicted-absent | absent-but-predicted-present | exact? |
|---|---:|---:|---|
| **`nexphist_r` sum > 0** | **0** | **0** | **YES** |
| **`cosky_r != 0`** | **0** | **0** | **YES** |
| `galdepth_r > 0` | 74 | 0 | no |
| `psfdepth_r > 0` | 74 | 0 | no |
| `psfsize_r > 0` | 70 | 0 | no |
| `nexp_r > 0` (the old proxy) | 121 | 0 | no — triage only, as suspected |
| `trans_r > 0` | 0 | 130 | no — vacuously true, useless |

Two expressions of **one indicator**: across all 366,912 bricks, `nexphist_r sum > 0` and
`cosky_r != 0` agree on every single brick (330,618 predicted-present / 36,294 predicted-absent /
0 disagreements). Physically sensible: the exposure histogram and the coadded-sky statistic are
both written when a coadd is actually built — which is what governs whether `image-r.fits.fz`
exists, where `nexp` does not.

## 3. The lemma that closes R1 at brick level

Exact, table-wide, zero exceptions over 366,912 bricks:

    { nexphist_r sum = 0 }  ⊆  { nexp_r = 0 }
    (0 bricks have hist = 0 with nexp_r > 0)

**Entailment.** Suppose some planned margin brick of the frozen parent set lacked `image-r`. By the
exact indicator, it would have hist = 0; by the lemma, `nexp_r = 0`; therefore it belonged to
planned ∩ {`nexp_r=0`} — which the R1 computation enumerated **exhaustively** (138 distinct bricks,
`margin_counts.json`) and which was HEAD-verified **138/138 present**. Contradiction.

> **Recomputed R1 counts under the exact indicator: unchanged — 0 of 208,407 objects have a margin
> brick lacking an r-band image file** (208,407 complete; by contributing-brick count: 172,983 /
> 32,320 / 2,939 / 165 for 1/2/3/4 bricks, all complete). What changed is what the zero rests on:
> not `nexp_r` as a presence claim (it is demonstrably wrong 121 times in this sample), but the
> exact indicator plus a set-inclusion lemma that is table-wide exact, plus the exhaustive 138/138
> HEAD pass. `nexp_r` now enters only as the enumeration key of a superset — a role its failures
> do not threaten, because they all point INTO the enumerated set, never out of it.

## 4. Honest residue

1. **The indicator's exactness is sample-proven, not a census.** 388 labels with every identified
   awkward class swept and zero errors, over a population of 366,912. If Kun requires census-grade
   certainty, the fallbacks stand: a HEAD sweep of the ~36,294 predicted-absent bricks near the
   frozen footprint, or Duho's option (1) — a re-authorized position pull with digests captured at
   creation. Neither is started here.
2. **The fail-closed asymmetry favours us.** A residual indicator error in the
   absent-but-predicted-present direction would surface LOUDLY at retrieval (manifest-required file
   404s → terminal custody event, §5.2 of the frozen successor binding). The silent direction —
   present-but-predicted-absent causing quiet object loss — is exactly what the §3 entailment
   bounds.
3. **Recommendation for the manifest gate (R2 classification):** classify `absent-by-coverage`
   by the exact indicator (`nexphist_r sum > 0` / `cosky_r != 0`), not by `nexp_r`. The checksum
   harvest then ground-truths every classification per brick from the survey's own `.sha256sum`
   listings — the indicator's role is planning, the harvest's role is proof.

## 5. Boundary receipt

- HEAD requests this task: **308** (all HEAD, paced ≥1.2 s, zero body bytes). Cumulative R1 lane:
  526. Image bytes fetched: **0**. FITS downloaded: **0**. Checksum harvest: **0**.
- TAP: one sync brick-level feature pull (`brick_features.csv`, 366,912 rows, `8cc77f6daaafafd1…`).
  **No per-object query of any kind; no positions, no rows, no identifiers.**
- Evidence retained: `exact_indicator_labels.json` (`a2aef3fd55057e54…`, includes the full HEAD
  log and per-stratum composition), `brick_features.csv` (public survey metadata).
- Frozen artifacts verified unmoved before and after: successor binding `1371b11094a27652…`
  (mode 444), prereg `b06901c8a0f3a057…`, adapter `267b2a93d2a61f65…`.
- No commit, no push, no publication, no accepted status. No galaxy pixels touched.

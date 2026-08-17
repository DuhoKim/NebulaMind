HOLD_PROXY_CONFIDENCE_OVERSTATED

# Kun R1 margin-coverage gate

Date: 2026-08-17 KST
Scope: document and local evidence review only. No network, no HEAD, no TAP query, no download, no endpoint, no commit, no push.

## 1. Ground-Truth Step

The ground-truth step is correctly derived for the proxy-flagged population. `_tmp_r1_margin_20260817/_tmp_margin_counts.py` imports `adapter/nm_brick_cutout_adapter.py` directly, computes each object's planned margin set, marks an object incomplete when any planned brick has `nexp_r == 0`, and writes `_tmp_rless_implicated.txt` from those flagged objects. `_tmp_implicated_head_recount.py` then reads exactly that implicated list, HEAD-checks those bricks, and recounts objects using the same adapter rule.

So the 138 checked bricks are not a reverse-engineered convenience list. They are the distinct `nexp_r=0` bricks implicated by the 230 proxy-flagged objects. Within that proxy-flagged set, `138/138` present converts the flags to zero true absences.

The hold is narrower: this does not check any planned margin brick with `nexp_r > 0`. Therefore it only closes R1 if the proxy cannot have dangerous false negatives.

## 2. Proxy Validation

The proxy validation supports `nexp_r` as a useful triage signal, but not the absolute claim made in the receipt that it "can only OVER-count r-less exposure, never under-count it." The validation sample is:

- `nexp_r > 0`: 40/40 image-r present, 0 dangerous disagreements.
- `nexp_r = 0`: 33/40 absent, 7 conservative disagreements.

The direction is encouraging and the observed disagreement is in the safe direction. But 40 `nexp_r > 0` checks cannot prove no dangerous disagreement exists across the distinct `nexp_r > 0` planned margin bricks for 208,407 objects. A single such brick in the planned margin set would evade the implicated-brick HEAD pass and could make the reported zero an artifact of the proxy.

This is why the verdict is HOLD. To pass, either HEAD/checksum-verify all distinct planned margin bricks, or at minimum all distinct `nexp_r > 0` planned margin bricks not already checked, or revise the R1 claim from a measured zero to a bounded proxy-supported result and gate that weaker claim explicitly.

## 3. Margin Rule

The margin rule matches the gated adapter. The scripts insert `adapter/` on `sys.path` and import `nm_brick_cutout_adapter` directly. The adapter hash is verified:

`267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f  adapter/nm_brick_cutout_adapter.py`

The evidence records `output_overlap_area_in_source_pixels`, threshold `1e-8`, and `prefilter_deg 0.21`, matching the adapter constants. This is not a separate reimplementation of the inclusion predicate, though the surrounding candidate prefiltering code remains R1-local.

## 4. Custody Status

The custody status wording is acceptable. R1 deliberately used contiguous `BRICKID` partitions over `1..121000`, matching the frozen parent-count method, and reproduced `208,407` exactly. It is therefore comparable to the frozen `208,407` for the frozen parent set.

The receipt states the scope loudly enough: complete for the frozen parent set, still `STOP BOUND REACHED BY CONTIGUOUS PARTIAL-COVERAGE LOWER BOUND` for the full catalogue. It also states that margin geometry used the full DR10 South brick table, which is the relevant distinction for neighbour bricks.

## 5. Clause-4 Gap

The missing pre-deletion SHA-256 digests for the transient position files are a real custody gap and should remain visible. The decision not to re-materialize solely to manufacture new hashes is correct: it would recreate the bounded exposure, and ADQL result order would not guarantee byte-identical files anyway.

The R1 computation did depend on the transient position rows at runtime, but the R1 finding does not depend on having retained SHA-256 digests of the deleted CSV bytes. The retained supports are row counts summing exactly to `208,407`, query texts, the frozen count match, and the adapter hash. That is weaker than the four-clause deletion rule wanted, but acceptable as a recorded ordering failure, not a reason by itself to fail R1.

## 6. Aggregate-Only Compliance

No `positions_part*.csv` file survives under this workspace. No `_tmp_rless_implicated.txt` file survives. `find` found only scripts and the position-handling rule by those names, not the transient position data or implicated-brick list.

The receipt contains aggregate counts, query text references, and row-count summaries, not object rows or object identifiers. The retained `_tmp_r1_margin_20260817/proxy_validation.json` does contain sampled public bricknames and declinations; it is not a position file or object list, and it is not committed. `git ls-files` reports none of the R1 receipt/evidence files as tracked. The working tree is broadly dirty outside this lane, but no R1 evidence file is committed.

## 7. Pinned Checks

- `R1_MARGIN_COVERAGE_20260817.md`: `cd4c4be9e3fdcaa5fab244c83752565baba04b4d1b073540bd341e71b010402e`
- `TORI_ROUTE_BINDING_SUCCESSOR_20260817.md`: `1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b`, mode `444`
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`: `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, mode `444`
- `adapter/nm_brick_cutout_adapter.py`: `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- `proxy_validation.json`: `7e2669e629ac021098b4ff495c92c6670f8276e0cef293d76f1c8dfc4da037e9`
- `margin_counts.json`: `0ab08a112ba8b9e053a2db211a531a9e2a358a0b9499c3819fa62a5feab90cbd`
- `recount_ground_truth.json`: `9ae93d2e78334733376e5b40750ccc56067ece3d80939bc0a51e7022f049ceb7`

## Boundary

Network calls: 0. HEAD requests: 0. TAP queries: 0. Downloads: 0. Image bytes touched: 0. FITS files fetched: 0. Checksum harvest: 0. Manifests built: 0. Endpoints activated: 0. Commit/push/publication: 0.

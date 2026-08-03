# MZR Field Matrix v2

AI_DRAFT_NOT_HUMAN_GOLD

**Redshift Legend**:
- `ABSENT`: Redshift is nowhere stated in the fields.
- `z=0 (TOPIC-STATED in spec.topic; no explicit redshift field)`: The redshift is verbatim mentioned within the run's stated topic string, but no explicit redshift field is present.

| Run ID | `created_utc` | `spec.method` | `spec.data_sources` | `spec.topic` | `spec.topic_source` | `spec.outputs` | `spec.force` | `result.method` | `result.data_sources` | `result.summary` |
|---|---|---|---|---|---|---|---|---|---|---|
| `2958462772b2` | `2026-07-17T09:47:30.429095Z` | `mass-metallicity` | `["sdss"]` | `cosmic-chemical-evolution` | `frontier-map` | `["aastex-draft", "dr-review-loop"]` | ABSENT | `mass-metallicity` | `["sdss"]` | `Mass–metallicity relation — median relations for SDSS (120,000 gals).` |
| `d8de519cb9c9` | `2026-07-17T09:20:58.872370Z` | `mass-metallicity` | `["tng", "sdss"]` | `cosmic-chemical-evolution` | `frontier-map` | `["aastex-draft"]` | ABSENT | `mass-metallicity` | `["tng", "sdss"]` | `Mass–metallicity relation — median relations for TNG100 (23,722 gals), SDSS (120,000 gals). TNG uses SF-weighted gas metallicity → O/H (solar-scaled).` |
| `e2f3b038f8dd` | `2026-07-17T09:06:12.028337Z` | `scaling-relation-evolution` | `["sdss"]` | `main-sequence-quenching` | `frontier-map` | `["aastex-draft"]` | ABSENT | ABSENT | ABSENT | `Mass–metallicity relation from 80,000 SDSS star-forming galaxies. 12+log(O/H) rises from 8.57 at logM⋆=9.0 to 9.05 at logM⋆=10.5, flattening at the massive end.` |
| `gated-e2e-demo` | ABSENT | `mass-metallicity` | `["tng", "sdss"]` | `the z=0 gas-phase mass-metallicity relation of galaxies: IllustrisTNG vs SDSS` | ABSENT | `["aastex-draft", "dr-review-loop"]` | `true` | `mass-metallicity` | `["tng", "sdss"]` | `Mass–metallicity relation — median relations for TNG100 (23,722 gals), SDSS (120,000 gals). TNG uses SF-weighted gas metallicity → O/H (solar-scaled).` |

### Detailed Fields

| Run ID | N Galaxies | Metallicity Calibration | Mass Definition | Redshift | O/H Anchors | Gates |
|---|---|---|---|---|---|---|
| `2958462772b2` | SDSS 120,000 | ABSENT | ABSENT | ABSENT | ABSENT | ABSENT |
| `d8de519cb9c9` | TNG100 23,722, SDSS 120,000 | TNG uses SF-weighted gas metallicity → O/H (solar-scaled). | ABSENT | ABSENT | ABSENT | ABSENT |
| `e2f3b038f8dd` | SDSS 80,000 | ABSENT | ABSENT | ABSENT | `oh_at_logM9`: 8.572, `oh_at_logM10p5`: 9.05 | ABSENT |
| `gated-e2e-demo` | TNG100 23,722, SDSS 120,000 | TNG uses SF-weighted gas metallicity → O/H (solar-scaled). | ABSENT | z=0 (TOPIC-STATED in spec.topic; no explicit redshift field) | ABSENT | novelty: NOVEL, expected_value: TENSION, citation_entailment: 2 unsupported of 4 checked |

### Artifacts and SHA256 Hashes
* **`2958462772b2`**:
  * `result.png`: `e1861feba72df35bf4d6430173fb30b5d47132afeb1780d54752eb5988b60022`
  * `review_loop.md`: `44df4ff8a2426b14d7f6d5e6cbae8682f655620192839e188c1ec5cf9e83ed71`
  * `draft.pdf`: `31e48d5b99094744496d0d32d02ca81eebfd6de2212c71cc3be5a20942b4cb80`
  * `history.json`: `823f0b9b89260646425cb4f2e23db933d3e22bcbcc3660002c4c3da528790b87`
  * `2958462772b2.json`: `9fc8f758170bcfc998721a893da232529ab5592748a16e884277b2676b39cadf`
  * `draft.tex`: `e996e2c673484979eed50d40bf98fe7694c1914f38e6c415bb873d014eec4f5c`
* **`d8de519cb9c9`**:
  * `result.png`: `0433a217ab7f76f66d06fd771f76fe8efdd8176b09cbbadce9e3eedd40273b74`
  * `history.json`: `4bd3ca92f6a0729a5e797b83d37e33a79c284122f11fff99a32c108373614f46`
  * `d8de519cb9c9.json`: `88217c0220b5c5ee3393401126c02895d37148414cabb8f8a409f78334eadf1f`
  * **NOTE**: `draft.pdf` and `draft.tex` are ABSENT on disk/manifest. This run is the "d8 candidate" whose candidate build is gated by Packet A.
* **`e2f3b038f8dd`**:
  * `mzr.png`: `8a357a5709a0bd7cea0a2bc16a6d79aa56842981748f1f466b2305a7433f8ffe`
  * `history.json`: `a021c0942eb3513bcbb7ef396edb1b284b88a2a57ae6a907e368419c36492398`
  * `e2f3b038f8dd.json`: `c14797b393951487e44a4f1d1bdd2dc102c3b3c6b197f65c230000801de8f531`
* **`gated-e2e-demo`**:
  * `result.png`: `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`
  * `review_loop.md`: `8fd49b32a8bd44f654b6bc7dba2aa2d7f454cb95c5490989ea450b798f0d5e3a`
  * `draft.pdf`: `0d863bff4d4d260fe32e56617ca6f920f2943574aaff2a5faeee3f7460575933`
  * `history.json`: `ab10e22da1617ba2afc61bbfb87535934540569f1290dedf65fb6e54eea77499`
  * `draft.tex`: `f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a`
  * `gated-e2e-demo.json`: `46ddd75d5f0e5814e814333336d8e6d1b011382c46509012af2aea8cc20af5e2`

## Cross-run consistency

* **SDSS N Galaxies**: Agrees as 120,000 for `2958462772b2`, `d8de519cb9c9`, and `gated-e2e-demo`. Differs in `e2f3b038f8dd`, which states 80,000.
* **TNG N Galaxies**: Agrees as 23,722 in both `d8de519cb9c9` and `gated-e2e-demo`. ABSENT in the other two.
* **O/H calibration scale**: ABSENT for SDSS in all four runs. `d8de519cb9c9` and `gated-e2e-demo` state `TNG uses SF-weighted gas metallicity → O/H (solar-scaled)`.
* **Mass definition**: ABSENT in all four runs.
* **Redshift**: `gated-e2e-demo` implicitly includes `z=0` in its `spec.topic` (`the z=0 gas-phase mass-metallicity relation of galaxies: IllustrisTNG vs SDSS`). ABSENT in all other three runs (no redshift stated in `spec.topic` or any other field).
* **Summary string**: `d8de519cb9c9` and `gated-e2e-demo` carry an identical summary string (`Mass–metallicity relation — median relations for TNG100 (23,722 gals), SDSS (120,000 gals). TNG uses SF-weighted gas metallicity → O/H (solar-scaled).`).
* **Method/Topic Mismatch**: `e2f3b038f8dd` is labeled `method=scaling-relation-evolution`, `topic=main-sequence-quenching`, yet reports an MZR (mzr.png, 12+log(O/H) vs logM★, `oh_at_logM9=8.572`, `oh_at_logM10p5=9.05`).
* **Gates**: Only `gated-e2e-demo` contains a gates block. ABSENT in all other three runs.

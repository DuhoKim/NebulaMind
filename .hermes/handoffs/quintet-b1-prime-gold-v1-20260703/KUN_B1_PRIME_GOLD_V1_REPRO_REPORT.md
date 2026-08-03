# KUN B1-prime gold v1 reproducibility report

Marker: `KUN_B1_PRIME_GOLD_V1_REPRO_DONE_20260703`

Scope: read-only implementation/reproducibility recheck of patched B1-prime Page57 gold v1 and existing verifier v1 outputs. I did not rerun the verifier because the brief preferred read-only checks and the existing run artifacts were internally sufficient for recomputation. Generic NLI runs: `0`. New model downloads: `0`. DB/SQL/migrations/deploy/git writes: `0`. Step 8 prose/unlock: `0` / `false`.

## Recomputed artifact facts

- Gold rows: `15`
- Gold v1 label counts: `{'noinfo': 2, 'qualifies': 7, 'refutes': 3, 'supports': 3}`
- Changed rows in summary: `11`; actual changed-row entries: `11`
- Gold v1 SHA256: `62952bd7710c980412f323ddd314bc322c483d8dd260f65575a78a9c64f865af`
- Gold summary SHA256: `5b9a39be0554e31c9258e232480fef12a2e9c5a25d88859fc48a32d72a3d8252`
- Verifier results SHA256: `27f4c429540bb039d2b6f4375da44d7097217119c99d12612eeeebddcd80f561`
- Verifier manifest SHA256: `12909066534c45872bb1c29d2914b64517fc41d48bc98a7d553da52fa0459007`
- Verifier script SHA256: `c2c398a9e198817b728c546de9342768d3eeb4a5c8ee6d372286470bb41fd41c`

## Recomputed verifier metrics

- Rows loaded in verifier results: `15`
- Correct: `12/15`
- Accuracy: `0.800`
- Majority baseline: `qualifies`, `7/15 = 0.4666666666666667`
- Gold counts in verifier results: `{'noinfo': 2, 'qualifies': 7, 'refutes': 3, 'supports': 3}`
- Predicted counts: `{'noinfo': 2, 'qualifies': 4, 'refutes': 6, 'supports': 3}`
- Refutes: precision `0.5`, recall `1.0`, TP `3`, FP `3`, FN `0`
- Qualifies: precision `1.0`, recall `0.5714285714285714`, TP `4`, FP `0`, FN `3`
- Supports: precision `1.0`, recall `1.0`, TP `3`, FP `0`, FN `0`
- Noinfo: precision `1.0`, recall `1.0`, TP `2`, FP `0`, FN `0`
- Misses: evidence `26687`, `29777`, `26084`; all are gold `qualifies` predicted `refutes`

## Provenance and divergence basics

The direct arXiv/source-matrix provenance is present for the previously quarantined/source-sensitive rows. The source provenance file records direct `HTTP_200_DIRECT_ABS_PAGE_VERIFIED_20260703` checks and SHA256s for `2410.09157`, `2512.16208v1`, and `2512.16290v1`. For `2512.16290v1`, term hits include `central properties`, `velocity dispersion`, `halo mass`, `black hole mass`, and `AGN feedback`, which covers both `26084` and `26088`.

The divergence table is present and narrow. It documents `25999` as strict-scope gold `qualifies` versus production cleanup `supports`, and documents `26084`/`26088` as quarantined legacy stance versus resourced gold. This is adequate for gold-v1 reproducibility, provided downstream use preserves the strict Page57-scoped held-out-test framing.

## Verifier script inspection

- Non-overwrite behavior: present. The script creates run, report, and validation directories with `exist_ok=False`, so an existing `RUN_ID` directory fails rather than overwriting results.
- Empty-input guard: present. `read_gold()` raises `SystemExit` on empty gold input.
- Label guard: present. `read_gold()` exits on gold labels outside `supports`, `refutes`, `qualifies`, `noinfo`.
- Manifest fields: present. Manifest includes marker, run id, created UTC, method id, gold path/SHA256, script path/SHA256, system/user-template prompt hashes, model manifest, and safety ledger.
- Safety ledger: present with zeros for generic NLI, model downloads, DB writes, SQL mutations, migrations, deploy/restart, git commit/push/merge, and Step 8 prose preview.
- Method identity: explicitly `local_ollama_scope_attribution_verifier_v1__NOT_GENERIC_NLI`.

## Gate answers

1. Patch sufficiency: yes, with adoption constraints. The row counts, label counts, changed-row count, provenance files, divergence table, and verifier rerun artifacts are internally consistent enough to freeze `gold v1` as a Page57-scoped held-out internal evaluation set.
2. Direct provenance for `26084`/`26088`: adequate. The direct arXiv provenance for `2512.16290v1` and the repaired snippets support the intended distinction: `26084` is mixed and therefore `qualifies`; `26088` is narrower and therefore `supports`.
3. Remaining label changes: none required for v1 freeze. The three misses are expected boundary cases where the verifier collapses mixed or modal evidence to `refutes`. Keep `26687`, `29777`, and `26084` as `qualifies` under strict Page57 scope unless a later human adjudication intentionally changes the rubric.
4. Verifier rerun soundness: mechanically sound and non-overwriting. The existing artifacts include manifest/provenance hashes and safety ledger. Because the run used a local Ollama endpoint and `ollama show --json` failed with an unsupported flag, model digest-level provenance is weaker than ideal, but this does not block use as attention-additive verification.
5. Safe adoption language: confirmed. Gold v1 may be used as a held-out internal evaluation set; verifier remains attention-additive only; Step 8 remains locked.

## Final stance

`PASS_WITH_PATCHES`

Reason: gold v1 and verifier v1 pass reproducibility and safety checks for scoped internal evaluation, but adoption must retain the documented caveats: verifier is attention-additive, the three qualifies/refutes misses are known rubric-boundary cases, model digest provenance is incomplete, and Step 8 remains locked.

KUN_B1_PRIME_GOLD_V1_REPRO_DONE_20260703

# Kun Primary Brief — P1 Massive-Galaxy Abundance Audit

You are Kun, the primary adversarial/reproducibility reviewer for P1. Work only inside your assigned directory. Input files are immutable snapshots.

## Question

Does the z≈4–6 TNG/JWST consistency claim survive exact statistic, population, aperture, IMF, selection, uncertainty, and publication-version reconciliation?

## Required work

1. Pin the exact PDF/review/history identities and attest source access.
2. Grade `PASS`, `PARTIAL`, or `FAIL` separately for query coverage, statistic identity, population commensurability, simulation commensurability, primary-source support, source version, and claim strength.
3. Reconcile the historical 0.28 dex erasure threshold with the later 0.20 dex mass-basis result.
4. Require explicit `n(>M*)` support. Do not substitute Schechter parameters, UV luminosity functions, halo densities, extreme-value ceilings, or per-object pseudo-densities.
5. Keep total, star-forming, quiescent, central/satellite, and UV-selected populations separate.
6. For each comparison row record threshold/bin, redshift, IMF, aperture, mass definition, selection, completeness, contamination, Eddington/scatter treatment, Poisson error, cosmic/sample variance, and direct-count versus integration status.
7. Audit systematic claims without adding maxima from unrelated samples or scopes. Record covariance and whether each result concerns individual masses, a GSMF, or integrated density.
8. Verify named-TNG conventions and distinguish native physical ratios from analytic abundance-matching proxies.
9. Keep the z>6 quiescent residual separate from the z≈4–6 total-population claim.
10. Use one overall disposition: `AUDIT_PASS`, `PARTIAL__CLAIMS_REQUIRE_NARROWING`, or `FAIL__NOT_REVISION_READY`.

Public web search and primary-source retrieval are allowed. Stop on login/CAPTCHA/payment/account/OAuth/secret prompts.

## Required outputs

- `QUERY_COVERAGE.json`
- `CUMULATIVE_DENSITY_LEDGER.csv`
- `SYSTEMATIC_BUDGET_LEDGER.csv`
- `SIMULATION_COMMENSURABILITY.md`
- `SOURCE_ROLE_AUDIT.md`
- `KUN_VERDICT.md`
- `RECEIPT.json`

`RECEIPT.json` keys: `lane`, `packet`, `status`, `started_at`, `completed_at`, `files`, `source_access_attestation`, `stop_files_checked`, `disposition`, `marker`.

Final marker: `P1_KUN_PRIMARY_COMPLETE_20260727`.

Do not revise any manuscript or edit project/public/Lab/DB/wiki/service/cockpit/Git state. Check stop files at start, mid-run, and before receipt. Hard stop 10:00 KST.

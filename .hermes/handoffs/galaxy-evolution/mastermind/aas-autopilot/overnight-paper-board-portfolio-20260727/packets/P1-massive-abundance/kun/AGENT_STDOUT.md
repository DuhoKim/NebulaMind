P1 Kun audit complete.

Created all required outputs in this directory:

- `QUERY_COVERAGE.json`
- `CUMULATIVE_DENSITY_LEDGER.csv`
- `SYSTEMATIC_BUDGET_LEDGER.csv`
- `SIMULATION_COMMENSURABILITY.md`
- `SOURCE_ROLE_AUDIT.md`
- `KUN_VERDICT.md`
- `RECEIPT.json`

Disposition: `PARTIAL__CLAIMS_REQUIRE_NARROWING`

Key preserved finding: the `0.28 dex` historical threshold belongs to the old 2Rhalf aperture comparison, while `0.20 dex` belongs to the later total-mass-basis result. The revision only partly landed because the served PDF’s Figure 1 arrow still says `0.28 dex` while the caption/prose say `0.20 dex`.

Validation done: JSON parses, CSVs read, all required files present, stop files checked start/mid/final with none found.

Final marker: `P1_KUN_PRIMARY_COMPLETE_20260727`

# Cached-vs-public SDSS representativeness tick — 20260708T220242Z

Marker: `CACHED_PUBLIC_REPRESENTATIVENESS_20260708T220242Z`

## What this tick did

- Addressed the external-review blocker that the cached `TOP 60000 ... ORDER BY specObjID` sample may not be representative of the full public SDSS DR17 four-line-eligible parent.
- Ran public/read-only SDSS DR17 `COUNT(*)` queries for redshift, stellar-mass, and sSFR bins under the same four-line S/N$\geq$3, redshift, mass, and sSFR constraints used by the pilots.
- Compared those public marginals against the cached 60,000-row CSV used by all nine active AAS-style pilots.
- Wrote a CSV/JSON/AASTeX table fragment and a figure for manuscript-integration review; no public-linked manuscript or PDF was overwritten.

## Grounding / data used

- Cached row-level CSV: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv` (60,000 rows read).
- Public SDSS endpoint: `https://skyserver.sdss.org/dr17/SkyServerWS/SearchTools/SqlSearch`.
- Public strict four-line S/N$\geq$3 total from this tick: **249,917** rows.
- Cached/public strict-parent coverage: **24.0%**.
- Raw SQL/JSON public payloads preserved under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads`.

## Main representativeness results

- **redshift**: largest cached-minus-public fraction difference is +2.03 percentage points in bin `0.080-0.120`; cached coverage ranges from 22.9% (`0.020-0.050`) to 25.3% (`0.080-0.120`).
- **stellar_mass**: largest cached-minus-public fraction difference is -1.63 percentage points in bin `8.0-9.5`; cached coverage ranges from 21.4% (`8.0-9.5`) to 26.7% (`11.0-12.5`).
- **ssfr**: largest cached-minus-public fraction difference is -0.58 percentage points in bin `-10.0--9.5`; cached coverage ranges from 23.1% (`-9.5--9.0`) to 26.2% (`-9.0--7.0`).

No bin exceeded the 5 percentage-point flag threshold, but the cached sample remains row-capped and non-random.

## Paper-use guardrails

- Use this packet as a selection-function/representativeness diagnostic for M2 P2, M3 P2, M3 P3, and any shared parent-sample section.
- Any reported `f_BPT_AGN`, `f_Q`, H$\alpha$ proxy, density, or target-vector fraction remains conditional on four-line emission detection and the SpecObjID-ordered 60,000-row cap.
- The packet does not add radio, X-ray, CO/HI, resolved outflow, or simulation-mock data; it cannot support radio coupling, gas-depletion/SFE, causal feedback, or model-validation claims.

## Files changed / written

- `summary_json`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/cached_public_representativeness_summary_20260708T220242Z.json`
- `marginals_csv`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/tables/cached_vs_public_marginals_20260708T220242Z.csv`
- `aastex_table_fragment`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/cached_vs_public_marginals_table_fragment_20260708T220242Z.tex`
- `figure_pdf`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/figures/cached_vs_public_marginals_20260708T220242Z.pdf`
- `figure_png`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/figures/cached_vs_public_marginals_20260708T220242Z.png`
- `raw_payload_dir`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/raw_sdss_payloads`
- `lane_report_md`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/CACHED_PUBLIC_REPRESENTATIVENESS_20260708T220242Z.md`
- `tick_report_md`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/ticks/TICK_20260708T220242Z.md`
- `helper_script`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/scripts/cached_public_representativeness_tick.py`
- `manifest_json`: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/cached-public-representativeness/20260708T220242Z/cached_public_representativeness_manifest_20260708T220242Z.json`

## Verification

- Public bin sums equal public total for all dimensions: True.
- Cached bin sums equal 60,000 for all dimensions: True.
- Raw JSON payload count: 16; raw SQL payload count: 16.
- Figure PDFs/PNGs exist and are nonzero: True.
- Manifest artifact hashes recorded: 9 artifacts.

## Blockers / cautions

- This is still a denominator-quality improvement, not a new science measurement.
- The cached sample remains ordered by SpecObjID, not randomized; manuscript text should call it a capped subset and avoid population-complete language.
- Use the table/figure locally before any future merge; do not replace public-linked PDFs without a separate approval gate.

## Next recommended tick

Patch the lane-local M2 P2, M3 P2, and M3 P3 revisions with this representativeness paragraph/table plus Wave-2 citations, then compile/hash those local PDFs only.

## Safety

Read-only public SDSS DR17 count queries plus local cached-CSV reads; wrote lane-local artifacts under overnight-9-papers-20260708/lanes/tori/cached-public-representativeness plus the required tick report and ledger append. No product DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/extra-cron/billing/OAuth/external submission changes.

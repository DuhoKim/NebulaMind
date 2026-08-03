# RP-1 robustness/selection-function revision

Marker: `RP1_ROBUSTNESS_SELECTION_REVISION_20260708T181833Z`

UTC: 2026-07-08T18:18:33Z  
Local: 2026-07-09 03:18:33 KST

## What changed

Created a lane-local AASTeX revision for **M1 RP-1 — SDSS AGN/sSFR matched-control pilot**. The revision does not replace the public-linked PDF. It adds:

- an explicit selection-function subsection and SDSS denominator table;
- a BPT/S/N robustness subsection, table, and Goru sensitivity figure;
- source/citation guardrails from the Wave-3 literature packet: SDSS DR17, Brinchmann catalog-property context, Kewley et al. optical classification, LaMassa AGN--SFR context, and Stasińska retired/LINER caveat;
- safer abstract/discussion/conclusion language saying the headline $-1.31$ dex is broad-BPT/S/N$\geq3$/capped-cache only, not causal AGN-feedback proof.

## Key inserted quantitative guardrails

- Public SDSS strict four-line S/N$\geq3$ eligible rows: **249,917**.
- Cached pilot rows: **60,000** (**24.0%** of strict eligible parent), selected by `TOP 60000 ... ORDER BY specObjID`.
- Four-line retention is sSFR-dependent: **33.56%** for $-12<\log\mathrm{sSFR}<-11$ versus **94.85%** for $-10<\log\mathrm{sSFR}<-9.5$.
- Matched median offsets: broad BPT S/N$\geq3$ **-1.31 dex**, S/N$\geq5$ **-1.16 dex**, S/N$\geq10$ **-0.74 dex**, high-excitation S/N$\geq3$ **-1.14 dex**, Seyfert-like proxy **-0.76 dex**, LINER-like proxy **-1.47 dex**.

## Outputs

- TeX: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/aastex/sdss_agn_sfr_pilot_rp1_robustness_selection_20260708T181833Z.tex`
- PDF: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/aastex/sdss_agn_sfr_pilot_rp1_robustness_selection_20260708T181833Z.pdf`
- Compile log: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/aastex/compile.log`
- Manifest: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/tori/revision-drafts/rp1_robustness_selection/20260708T181833Z/rp1_robustness_selection_manifest_20260708T181833Z.json`

## Verification

- `tectonic` exit code: **0**
- PDF magic `%PDF`: **True**
- PDF bytes: **267505**
- PDF SHA256: `912f10efd2046198307b2e637112a2dae4ca0df11e2c2c607e351a180785066e`
- Fatal LaTeX markers: **0** (`[]`)

## Safety

Local lane artifact only. No public/live page changes, DB/API/page_versions/trust, deploy/restart, git, cron, billing/OAuth, or external submission.

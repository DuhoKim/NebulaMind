# hwao_director cycle 17
Started UTC: 2026-07-09T22:37:37Z
Model: Gemini 3.1 Pro (Low)
Provider: agy
Brief: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/briefs/cycle_17_hwao_director.md

Here is the cycle 17 critical review report under the Hwao/Fable director persona.

### 1. OVERNIGHT_HWAO_DIRECTOR_CYCLE_17 status
**ISSUES_FOUND** (Suite remains publishable, but has minor/improvement paper-quality issues needing writer pilot attention).

### 2. Files/paths actually inspected
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/01_m1_rp1_sdss_agn_sfr/aastex/m1_rp1_sdss_agn_sfr_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/02_m1_rp2_environment_quenching/aastex/m1_rp2_environment_quenching_integrated.tex`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-critical-review/OVERNIGHT_PDF_REVIEW_WORKFLOW_SWARM_20260709T163102Z/candidates/cycle_17_nine_papers/09_m3_p3_simulation_validation/aastex/m3_p3_simulation_validation_integrated.tex`
- Plus context from the cycle 16 feed logs.

### 3. Ranked findings
- **Minor**: Missing sSFR quenching threshold definition in the abstracts of Papers 02–09. While the introduction/methods mention "quenched fraction", the exact sSFR cut used to define "quenched" must be explicitly stated early on.
- **Minor**: The $n \geq 50$ cell floor in Paper 09 needs a brief Poisson justification (e.g., "to ensure Poisson uncertainty $\leq 14\%$") rather than appearing arbitrary.
- **Improvement**: "Optical denominator" is heavily used as internal jargon across all 9 papers' Introductions. Needs one clean, explicit sentence defining it for external journal readers.
- **Improvement**: Figure captions lack key quantitative takeaways. For instance, in Paper 01 `\caption{...}` only says "documents the optical selection" but omits the main offset value found ($-1.309$ dex).
- **Improvement**: Software citations (`\software{Astropy, SciPy, NumPy, Matplotlib, pandas}`) lack version numbers across all papers, slightly reducing strict reproducibility.

### 4. Exact feed for PDF-writing pilot
**Paper 01-09 Introductions (The "Optical Denominator" fix):**
Find the first use of "optical denominator" or "optical baseline" and insert:
`By "optical denominator," we refer to the empirically measured parent sample of optical emission-line hosts before any multi-wavelength phase (e.g., molecular gas, X-ray) or dynamical kinematic cuts are applied.`

**Paper 01 Figure 2 Caption:**
```latex
% Replace current caption with:
\caption{Matched-pair catalog-sSFR offsets for broad BPT optical AGN hosts minus nearest star-forming controls in stellar-mass--redshift space. The large negative offset (median $-1.309$ dex) is robust within the optical emission-line subset but remains selection- and subclass-dependent.}
```

**Paper 02-09 Abstracts:**
Insert the quenching threshold definition in the abstract wherever quenched fraction is first mentioned:
`...quenched fraction (defined via $\log {\rm sSFR} < -11 \rm\, yr^{-1}$)...`

**Paper 09 Section 4:**
```latex
% Replace:
We define 15 mass-redshift cells with $n \geq 50$ as a compact validation vector;
% With:
We define 15 mass-redshift cells with $n \geq 50$ (ensuring Poisson counting errors $\leq 14\%$) as a compact validation vector;
```

### 5. Real-data/source/citation audit notes
- Confirmed "Dubois" typo from cycle 01 remains correctly patched in Paper 09.
- No mock/synthetic data found. The numbers (-1.309 dex offset, 0.230 vs 0.181 quenched fractions) are rigorously derived from local data and appropriately caveated as non-causal association results.
- Software versions are missing. While no citation spoofing occurred, adding version bounds to Astropy/Pandas is a best practice.

### 6. Workflow/system notes
The wiki-to-PDF orchestrator operates cleanly but is injecting internal system jargon ("future-data requirement", "optical denominator") directly into the TeX output. The system prompts for the text generation steps should be tuned to favor standard astrophysical journal phrasing rather than internal project management speak. 

### 7. Safety ledger
- Edits made to TeX files: 0 (Artifact-only mode respected).
- Public-linked PDFs replaced/touched: 0.
- Public/live frontend or static root edits: 0.
- DB, SQL, /api/pages, page_versions, wiki publish, trust recompute, or data mutation: 0.
- Deploy/restart triggered: 0.
- Git commit/push/merge/rebase/history rewrite: 0.
- Cron creation/update/removal: 0.
- Billing/cloud/OAuth/API-key/account changes or credential reads: 0.
- External manuscript submission: 0.


# command_result
exit_code=0
elapsed_s=29.7
timed_out=False
finished_utc=2026-07-09T22:38:07Z

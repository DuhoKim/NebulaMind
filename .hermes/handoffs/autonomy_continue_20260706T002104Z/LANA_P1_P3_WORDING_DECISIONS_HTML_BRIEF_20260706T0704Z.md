# Lana brief — build P1/P3 wording decisions HTML

Marker for the artifact: `LANA_P1_P3_WORDING_DECISIONS_HTML_20260706T0704Z`

User request: "okay let lana or hwao build a html that is for P1/P3 wording decisions"

Lane: Lana. Hwao/Tori boundary: this is a static public operator HTML only. No DB, no SQL/apply/rollback, no trust recompute, no prose/wiki/page_versions publish, no product-code patch outside the static report file, no git/deploy/restart, no GCP/API usage.

Workdir:
`/Users/duhokim/NebulaMind/NebulaMind`

Create exactly one standalone, self-contained HTML file:
`frontend/public/agent-reports/p1-p3-wording-decisions.html`

Also write a short receipt file:
`.hermes/handoffs/autonomy_continue_20260706T002104Z/LANA_P1_P3_WORDING_DECISIONS_HTML_REPORT_20260706T0704Z.md`

Source docs to use, read-only:
- `docs/hwao_morning_blocker_specs_20260706T0308Z/P1_LEGACY_OVERCLAIMS_2298_2299_2924_SPEC.md`
- `docs/hwao_morning_blocker_specs_20260706T0308Z/P3_2572_PRIMACY_RECAST_SPEC.md`

Design goal:
A clear decision board for Duho to choose P1/P3 wording directions. It should be readable on a phone and desktop. Make it a polished operator page, not a raw markdown dump.

Required content:
1. Top banner:
   - "P1/P3 Wording Decisions"
   - `NO ACTIVE EXECUTION PHRASE`
   - `DB writes: 0 · SQL execution: 0 · Trust recompute: 0 · Prose/wiki publish: 0`
   - marker `LANA_P1_P3_WORDING_DECISIONS_HTML_20260706T0704Z`
2. P1 card: legacy overclaims 2298 / 2299 / 2924
   - 2298 current: "AGN feedback heats the gas reservoirs of massive galaxies."
   - 2298 recommended option: recast to scoped or retire into 2946.
   - 2298 draft wording from the spec: "In simulations and some massive-galaxy or circumgalactic contexts, AGN/SMBH feedback can heat or thermally regulate gas, but current source support is model- or system-bounded rather than a universal quenching prevalence result."
   - 2299 current: "AGN feedback expels gas from the reservoirs of massive galaxies."
   - 2299 recommended option: recast to scoped or re-parent into 2945.
   - 2299 draft wording from the spec: "AGN-driven outflows can expel, heat, or compress surrounding gas in some systems, so gas expulsion is one possible quenching/regulation channel, not a universal explanation for gas-reservoir loss."
   - 2924 display-state decision: expected audit endpoint vs stale public display state; recommended cleanup if parent_replaced.
3. P3 card: 2572 primacy recast
   - current: "Quenching in central galaxies correlates with central properties like velocity dispersion, bulge mass, and black hole mass."
   - recommended cautious wording: "Central galaxy quenching should not be treated as primarily driven by central properties such as velocity dispersion, bulge mass, or black-hole mass unless halo-mass effects have been separated."
   - stricter alternative: "Central properties such as velocity dispersion, bulge mass, and black-hole mass are the primary predictors of central-galaxy quenching, rather than halo mass."
   - show the choice: cautious guard vs assertive disputed claim; preserve 2573 separately.
4. Decision checklist:
   - Choose P1 2298 route.
   - Choose P1 2299 route.
   - Choose 2924 endpoint/display handling.
   - Choose P3 cautious vs stricter wording.
   - Choose whether future trust recompute waits for P4.
5. Keep all approval phrasing safe:
   - The page must not include any `APPROVE EXECUTE` or `APPROVE APPLY` string.
   - It must say future DB/prose packet needs later explicit local approval, but do not provide an approval phrase.
6. Add a compact "plain English" summary.

Suggested UX:
- dark NebulaMind-style cockpit, clean cards, side-by-side P1/P3 columns on desktop, stacked on mobile
- decision chips or checkboxes are okay if purely local UI; they must not submit anywhere
- optional localStorage for checked items is okay
- no remote dependencies

After writing the file, verify locally with a simple parse/grep check and write the receipt report. Do not run tests/builds/deploys. Do not touch main cockpit; Tori will link/mirror/verify after your report.

End the report with standalone marker:
`LANA_P1_P3_WORDING_DECISIONS_HTML_20260706T0704Z`

PIN_AUDIT=ISSUES

1. Both, row 3: cap grid — codex "{1.97, 2.50, 3.50}" vs claude "{2.0, 2.5, 3.5}". Low cap differs with different receipts (codex: Özel 1.97 EoS bound, verified at L1657-1659; claude: J0348 2.0 floor). Contradiction; one grid must win.

2. Both, row 6: N — codex "3,000,000 binaries per grid point" (C4 6M, seeds 104729/130363/155921) vs claude "N = 10^6" (C4 2M, date-formula seeds). Flat contradiction in N, C4, and seeds.

3. Both, row 5: reference n — codex 14 masses, excluding "censored systems in lines 313-320"; claude 15, adding "J1141−6545 1.27(1)" at L318. Verified L318 is uncensored (WD-companion pulsar, component masses) — so n contradicts, and codex's "censored" rationale mislabels L318.

4. Both, row 7: alternative — codex "alpha 0.5 + ZERO kicks" vs claude "LAMBDA_FIXED 0.1 + MAXWELLIAN 265". Different box axis entirely.

5. Claude, row 6: "online-docs contain NO runtime statement" is false — codex's receipt verified (running-via-cmdline.rst sample output: "Clock time = 0.078125 CPU seconds"); claude's grep pattern ("CPU hours") missed "CPU seconds".

Verified consistent: commit e728869, version 03.29.05, row-2 defaults, MD14 eq.15 (both SHA-256 match the files on disk), honest build-failure records (both exit 2, boost/gsl/hdf5 absent). Claude's box widths adequate; codex pins no box axes. No invented numbers found.

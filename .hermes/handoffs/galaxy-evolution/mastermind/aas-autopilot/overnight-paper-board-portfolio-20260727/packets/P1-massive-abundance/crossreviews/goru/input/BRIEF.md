# Goru Cross-Review Brief — P1 Massive-Galaxy Mechanical Audit

Hwao assigned Goru as P1 mechanical source/numeric cross-reviewer. This is not a new primary and not permission to edit Kun's files.

Your only writable directory is `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-portfolio-20260727/packets/P1-massive-abundance/crossreviews/goru/`. Read its immutable `input/` snapshots.

## Review questions

1. Parse and audit every Kun JSON/CSV/Markdown output; verify row counts, required fields, source-role enums, numeric arithmetic, and internal links.
2. Mechanically verify the two distinct 0.28-dex and 0.20-dex quantities and identify exactly where each appears in the served PDF/text/figure annotations.
3. Count cumulative-density rows that are explicit direct support for `n(>Mstar)` versus indirect inputs, candidates, or gap rows.
4. Check that total, quiescent, candidate, UV-red/UV-blue, and spectroscopic populations remain separated.
5. Flag invented counts, unsupported arithmetic, ambiguous source identities, invalid additive budgets, and overstated status language.
6. Check that the primary input and project/public/Lab/DB/wiki/service/cockpit/Git state were not modified.

Public web/ADS/arXiv reads are allowed. Stop on login/CAPTCHA/payment/account/OAuth/secret prompts. Do not modify manuscripts or public artifacts.

## Outputs

- `CROSSREVIEW.md`
- `VALIDATION.json`
- `RECEIPT.json`

Disposition enum: `PASS`, `PASS_WITH_PATCHES`, `ISSUES`, `BLOCKED`.

Receipt marker: `P1_GORU_CROSSREVIEW_COMPLETE_20260727` or `P1_GORU_CROSSREVIEW_PARTIAL_20260727`.

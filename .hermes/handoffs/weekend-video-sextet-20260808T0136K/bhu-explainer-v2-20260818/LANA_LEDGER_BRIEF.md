# LANA — v2 claim ledger brief

Read `SEXTET_BRIEF_V2.md` first; it binds everything. Your deliverables, written into THIS
directory:

1. `CLAIM_LEDGER.md` — same discipline as
   `../bhu-neutron-star-explainer-20260817/CLAIM_LEDGER.md` (your own v1 format): one row per
   factual sentence of the new `SCRIPT.md`, verdict **MAPPED** (with exact source lines) /
   **FLAG** (cut or source, never soften) / **framing** (asserts nothing). Result count up
   front. A fidelity-notes section for every simplification you accept, and a must-not-say sweep.
2. `DEFINITIONAL_SOURCES.md` — only if the script needs textbook sentences (what a black hole
   is, what a neutron star is, "constants"). For each: the verbatim quotable line, source title,
   URL, access datetime (run `date`, never estimate), and a saved local copy in
   `definitional_sources/` here with its SHA-256. Allowed hosts: arXiv / ar5iv / ADS-indexed
   pages / NASA public pages. These become D-row targets. If Smolin's own CNS wording is worth
   pinning beyond P §1.4 (e.g., arXiv hep-th/0407213 or the 1992 CQG abstract), you may fetch
   and pin it the same way as an S-row — your call whether P 260–264 suffices.
3. `LANA_DONE.md`, first line `LANA_V2_LEDGER_COMPLETE`, plus the FLAG count.

## Sources and their keys

- **A** = `../bhu-mass-adjudication-20260817/C08_MASS_ADJUDICATION_20260817.md` (line numbers;
  verify Kun gate `PASS_C08_ADJUDICATION` is present before ledgering, as you did in v1).
- **P** = `../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md`, SHA-256 must equal
  `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516` — verify before use.
  You wrote it; cite it at line level like A. §1.4 (259–278) carries the CNS mechanism sentence
  and the Brown–Lee–Rho chain; §0 (143–167) the five-programmes finding; §1.1 (171–184) Pathria.
- **L** = `../bhu-closing-video-20260812T2322K/CLAIM_LINE_LEDGER_V11.md` (row IDs C01–C16).
  **V11's exclusions bind v2**: no Pathria body claims, no 2.35-M⊙ star, no named
  rival-model comparisons.
- **D/S** = your `DEFINITIONAL_SOURCES.md` rows.
- **V1** = `../bhu-neutron-star-explainer-20260817/CLAIM_LEDGER.md` — sentences reused verbatim
  from v1 may cite your v1 rows wholesale; re-verify nothing silently changed around them.

## Boundaries to enforce hard (the sextet brief's list, plus)

- Direction of the CNS claim: CNS's *stated falsifiable consequence* is the low ceiling
  (P 262–264). A sentence implying we derived it, or that a low ceiling implies CNS, is a FLAG.
- The 4% binary rule: the gated record states the rule and its caveat, not its mechanism. Any
  "because pairs form together / accretion / common envelope" explanation is a FLAG — cut or
  source from the paper body with a pinned fetch.
- "nearly 5 times the threshold" (19.3/4 = 4.8, A 113) stays permitted; any sharper multiplier
  is drift.
- σ values: A gives ≥ 8σ per heavy system and ~21σ on limb 2; the script should prefer plain
  words ("by a wide margin", "securely above") — digits only where A states them.

Do not touch `portal.nersc.gov`. Fetches only from the allowed literature hosts, and only for
definitional/S rows. Write only inside this lane directory.

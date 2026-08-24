PASS_TRACK_B_FREEZE

# Gate verdict — Phase 4 Track B adversarial gate (kimi seat, 2026-08-24 19:04 KST)

Gate: KICKOFF_GATE_TRACKB.txt (mandate: REFUTE). Verdict written to KGATE_TRACKB_VERDICT.md
per coordinator override (codex gate owns GATE_TRACKB_VERDICT.md); all other kickoff
instructions applied. Audited the CURRENT post-HOLD artifacts: TRACK_B_FREEZE.md, both
harvests, b_verify_quotes.py v4, b_verify_ledger.json (50 rows). Method: independent
re-execution of the verifier, independent re-verification of 12 frozen rows against harvest
quotes AND local source texts, an attack battery against v4 using its own machinery, and
custody re-computation (pins, PDF hashes). Evidence: _tmp_kgate_attack_v4.py,
_tmp_kgate_attack2_v4.py, _tmp_kgate_ledger_before.json in this directory. No track file
modified (the verifier's own re-run rewrote b_verify_ledger.json byte-identically; sha
unchanged, archived copy confirms).

## Attack 1 — fidelity, 12 frozen rows vs harvest quotes and source texts: ALL CONFIRMED (attack failed)

Independently verified 12 rows spanning B2 and B3 against the verbatim harvest quotes and
the underlying local source .txt extractions. No number differed.

| Row | Frozen value checked | Local-source result |
|---|---|---|
| B2.1 | 3362.08 ± 0.99 µK; 369.82 ± 0.11 km/s | Exact, dipole_planck2018_overview txt lines 270-271, 293. |
| B2.3 | 384 ± 78 (stat) ± 115 (syst) km/s | Exact, dipole_planck_aberration txt lines 49, 440. |
| B2.4 | up to ~40% without contradicting Planck | Exact, "as large as 40 per cent without contradicting the Planck measurement", schwarz txt line 72. |
| B2.6 | 5.1σ joint (2.6σ + 4.4σ) | Exact, secrect_2022 txt lines 31-33, 294-295. |
| B2.7 | 2.46 ± 0.18 × kinematic; 5.7σ | Exact, dam_2023 txt lines 226, 28. |
| B2.8 | 3.67 ± 0.49 ×; 5.4σ | Exact, boehme_2025 txt lines 37, 247, 264-265. |
| B2.9 | 331/399 km/s ≈ CMB velocity | Exact central values, darling_2022 txt lines 33-39; asymmetric uncertainties +161/−107, +264/−199 confirmed present in source and harvest (see Advisory A4). |
| B2.10 | ~2σ; consistency not ruled out | Exact, "approximately to the 2 σ significance level", abghari_2024 txt line 139. |
| B2.11 | 3.27–3.63σ revised | Exact, 3.63/3.44/3.27 σ, bashir_2026 txt lines 31-33, 607-628. |
| B3.2 | ~1% (0.5–0.8% with 2016 mask) | Numbers exact, planck2020 pages txt lines 669-679, 804 (compression note: Advisory A5). |
| B3.4 | p < 0.24% robust; HFI-100: 0.03% | Exact, copi2015 pages txt lines 30-33, 115, 561. |
| B3.6 | "1 in 10 or 1 in 20"; "no convincing evidence" | Exact, efstathiou2003 pages txt lines 319-320. |

Union with the codex gate's 8-row sample (B2.1, B2.2, B2.5, B2.9, B3.1, B3.3, B3.5, B3.7)
covers all 18 frozen B2/B3 rows with no disagreement. B1 reference-tier values also
spot-verified against the agy .tex sources: Migkas 2020 (3.59σ, 13±4%, Migkas_etal.tex line
838 verbatim), Migkas 2021 (4.3σ, 13±3%), Hu 2024 (4.48σ; H0,max 74.26±0.39; direction
313.4, 47121corr.tex lines 199-204), Dam 2023 (2.46±0.18, paper.tex line 555).

Custody: all 4 freeze receipt pins match current bytes (recomputed sha256 of both harvests,
b_verify_quotes.py, b_verify_ledger.json). 4/4 dipole PDF sha256 match harvest receipts;
17/17 radio PDF sha256 match radio_download_manifest.json.

## Attack 2 — the v4 verification method: SOUND FOR WHAT IT CLAIMS (attack failed against the artifact; three residual gaps demonstrated, all advisory)

The codex HOLD's required repairs are all delivered and were re-verified by execution:

- Re-run from lane root: self-test passes (genuine B3.1 quote verifies; the gate's corrupted
  counterexample FAILS — my independent replication confirms: corrupted tokens 8.8/9.9 not
  found in the bound source, verdict FAIL). gpt2 43/43, agy 7/7, TOTAL 50/50, exit 0.
- Boundary-awareness: token "3.6" does not match inside "13.6" (v3's unbounded-substring
  defect is dead). All-length extraction: B3.1's tokens are now [10, 2.5, 3, 40, 5] — the
  v3 three-digit filter that blinded it to 5/10/40/2.5/3 is gone.
- Binding: 43/50 bound to the source files their harvest entries declare; the 7 agy entries
  declare no inline `sources/` path (the harvest cites arXiv IDs, not local files), so the
  whole-dir fallback is the only option and is flagged `bound_to_declared: false` in the
  ledger — disclosed in the freeze receipt, not hidden. I hand-verified those 7 quotes
  against the actual .tex sources regardless.
- Ledger: 50 rows (42 auto, 7 PASS_NUMERIC, 1 PASS_PHRASE), deterministic — re-run produces
  a byte-identical file (sha 8155de4a... before and after). "Zero manual acceptances" is
  accurate: MANUAL_ACCEPT = {} in the code.
- Residues legitimate: re-derived all 8 evidence-graded acceptances — every recorded span
  exists verbatim in its named source file, and every extracted token is genuinely present
  there (0 stale spans, 0 token gaps). All 7 PASS_NUMERIC rows carry highly distinctive
  tokens (0.01554, 0.9999999888, 74.26, 3.6/3.7, 331+err chain, 74.26/313.4).

Residual gaps, each demonstrated concretely with the verifier's own machinery. None
produces an error in the frozen artifact — every frozen row's numbers, signs, and
directional framing are hand-verified across the two gates' samples — so they are
advisories on what the machine receipt covers, not blockers:

- A1 (sign-blindness): normalization strips signs, so a sign-flipped Migkas 2020 quote
  (−22°→+22°, −9°→+9°, −21°→+21°) passes v4 with byte-identical normalized text. The codex
  repair text listed "signed integers"; v4 does not preserve them. Signs in the frozen
  table rest on harvest custody plus gate spot checks, not on the machine receipt.
- A2 (directional/semantic blindness): a negated Ferreira–Quartin quote ("we cannot put any
  upper limit") passes at shingle 0.636 ≥ 0.30 with tokens intact. v4 verifies that numbers
  and prose-similarity co-occur, not that the claim's direction matches the source. All 18
  rows' directional framing was hand-checked across the two gates.
- A3 (weak PASS_NUMERIC floor): a fully fabricated quote with two common tokens ("1", "2")
  and zero prose match is accepted via PASS_NUMERIC against any bound file containing those
  digits. Not exploited in this corpus (all actual residues are high-distinctiveness and
  span-verified), but if the hatch is reused, require a distinctiveness floor or spans for
  ALL tokens, not the two longest.

The freeze receipt describes its own criterion accurately (all tokens + ≥30% shingles;
PASS_NUMERIC with recorded spans; PASS_PHRASE with the 8-word span) and does not claim
semantic or sign verification — unlike v3's "38/50 by machine", which implied a numeric
fidelity it demonstrably lacked. The receipt's claims are reproducible; I reproduced them.

## Attack 3 — balance: BOTH DISPUTES CARRIED WITH EQUAL CUSTODY (attack failed)

B2 carries four excess results (Secrest 2021 4.9σ; Secrest 2022 5.1σ; Dam 2023 5.7σ; Böhme
2025 5.4σ) and three counter/reassessment results (Darling 2022 consistent; Abghari 2024
~2σ; Bashir 2026 3.27–3.63σ) as full harvest entries with verbatim quotes, locations, and
receipts — counters are not footnotes. The freeze states the dispute is unresolved and stays
unresolved in this record, and forbids Track C from adjudicating. B3 carries
higher-significance (Planck 2013 XV 2.5–3σ; Billi 2024 ≤0.33%/≤1.76%; Copi 2015 <0.24%) and
lower-significance/estimator-dependent positions (Bennett 2011 0.824/within-95%; Efstathiou
2003 1-in-10/20; Efstathiou+ 2010 8% vs 0.065%) and calls the significance CONTESTED with
equal custody, per the brief's B3 instruction. No sentence converts either dispute into the
coordinator's conclusion. The harvest's own note that the labels report the papers' own
framing (not a combined significance) is correct custody.

## Attack 4 — B1 scope vs the gated Track A verdict: EXACT MATCH (attack failed)

TRACK_A_VERDICT.md Amendment 1 (passed by REGATE3_TRACKA_VERDICT.md) limits the exact H0
null to sources whose complete light paths remain interior, leaves boundary-crossing or
boundary-influenced probes UNCALIBRATED, and scopes "NOT-A-DISCRIMINANT" to wholly-interior
expansion probes only. The freeze's B1 section uses the same boundary verbatim in
substance: reference-only because the null is wholly-interior; MAY NOT be used as a
discriminant; re-opens if a future track models boundary-influenced probes. Neither wider
(does not claim the null for all probes) nor narrower (does not withhold the wholly-interior
null). The freeze's "gated PASS" citation of Track A matches REGATE3's PASS_TRACK_A_AMENDED.

## Attack 5 — omissions: NO TRACK-C-BIASING OMISSION (attack failed)

Every load-bearing bound class named in the brief is present. B1: cluster-scaling anisotropy
(Migkas 2020, 2021), SN-compilation dipole (Hu 2024 Pantheon+; Cowell 2023 quadrupole),
quasar dipole (Dam 2023) — all brief candidate anchors held. B2: Planck measured dipole
(B2.1) vs kinematic expectation, direct intrinsic bound (B2.2), indirect confirmations
(B2.3 aberration, B2.4 allowance). B3: low-ℓ numbers plus the full published significance
range, both poles. Track C's MAY/MAY-NOT clauses match the brief's scope discipline,
including that the disputes are literature disputes, not ours to adjudicate.

## Advisories (non-blocking; for the freeze's next revision or Track C readers)

- A4 (echo codex): B2.9's freeze row drops Darling's asymmetric uncertainties
  (+161/−107, +264/−199 km/s) that the harvest retains. Counter-evidence should carry the
  same numeric custody as excess claims in the table proper.
- A5: B3.2's "0.5–0.8% with 2016 mask" compresses two releases — 0.5% is the 2015-analysis
  minimum at Nside=16; 0.7–0.8% is the 2018 data under the 2016 mask. Both numbers are in
  the frozen harvest quote; the table attribution could be sharper.
- A6 (echo codex): the B1 tier names 4 of 5 harvest entries and delegates "remaining harvest
  entries" (Cowell 2023) to the pinned harvest. Reference-only, so non-biasing; enumerate
  for a closed, auditable frozen set.
- A1–A3 above: v4 verifies numeric magnitudes plus a prose-similarity floor — not signs, not
  directional semantics, and the PASS_NUMERIC hatch is only as strong as token
  distinctiveness. Track C should read the machine receipt as such; directional claims stand
  on the verbatim harvest quotes and the two gates' hand verification.

## Gate boundary

This PASS concerns the Track B freeze and its verification custody only. It does not
re-open or extend the amended Track A gate, does not adjudicate either literature dispute,
and does not authorize Track C execution.

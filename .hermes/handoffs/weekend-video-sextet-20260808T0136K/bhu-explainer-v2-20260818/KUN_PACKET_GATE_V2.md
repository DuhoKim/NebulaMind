PASS_EXPLAINER_PACKET

# Kun packet gate — BHU explainer v2

Date: 2026-08-18 KST. Seat: Kun (gate). Scope: document review only, findings-only. No
rendering, no generated media, no credits, no upload, no publication, no network fetches,
`portal.nersc.gov` untouched. Nothing in this lane was edited; the only write is this file.

Packet gated: `SCRIPT.md`, `STORYBOARD.json`, `CLAIM_LEDGER.md`, `DEFINITIONAL_SOURCES.md`
(+ `definitional_sources/` local copies), `VISUALS.md`. Briefs applied: `SEXTET_BRIEF_V2.md`,
`KUN_PACKET_GATE_BRIEF_V2.md`. Precedent: v1 gate `../bhu-neutron-star-explainer-20260817/KUN_PACKET_GATE_20260818.md`.

## 1. Ledger completeness — PASS

- Every factual sentence has a row: 66 narration sentences (quote-aware split; the two
  `or."` boundaries in Panels 01/05 counted) map 1:1 onto 66 §1 rows + 1 head scope row =
  67 rows. Per-panel counts match exactly (P01 8, P02 6, P03 6, P04 6, P05 5, P06 6, P07 7,
  P08 9, P09 6, P10 7). Mechanical check: the opening 5 words of every narration sentence
  appear in `CLAIM_LEDGER.md`; none missing.
- No FLAG survives: zero `| FLAG` table rows (ledger states "0 FLAG" at line 24–27; verified).
- Framing rows genuinely assert nothing: the sole framing row is P01#1 "Could our universe
  exist inside a black hole?" — a question. ✔

## 2. Source truth — PASS (spot-checks at cited lines)

- CNS mechanism vs P 259–278: script Panels 03–04 track P 259–264 sentence by sentence.
  Direction rule satisfied — the low ceiling appears only as CNS's *stated falsifiable
  consequence* (P 262–264: "Its stated falsifiable consequence: the maximum neutron-star
  mass should sit low … M_max ≈ 1.5 M☉"). No sentence derives it as our inference and no
  reverse implication ("low ceiling supports CNS") exists anywhere. ✔
- Five-programmes claim: P 145–146 "at least five distinct programmes that do not agree
  with each other" — backs P02#5–6 and P09#6 exactly. ✔
- 1972 claim: P02#2–3 stay at accessible-abstract level; P 173–176 carries the abstract
  quote (closed universe, oscillation, radius condition, bounded expansion) and P 183 the
  body [VERIFY] exclusion. The script says "accessible abstract" explicitly. ✔
- Every number checked against A at cited lines: 1.5 (A 28, 46); "around 2" / M≳2 (A 24–29,
  40–41, 46–47); 2.00 at 68.3%/not 95.4% (A 70, 92–93); 2.08 ± 0.07 (A 70); 1.599/1.290
  ± 0.008 (A 72); 19.3 ± 0.7% (A 102); 4% (A 24–25); "nearly 5 times" (A 113); ≥8σ × 3
  systems (A 94–97, 131); 21σ-wide margin rendered as "by a wide margin" (A 102–103, per the
  σ rule); published 2020 / sharpened 2026 (A 72, 156–157). All exact. ✔
- Definitional rows: D1, D2, S1 quotes verified present verbatim in the pinned local copies
  (Imagine the Universe neutron-star page; Uzan arXiv:1009.5514 §1/§7; Brown–Lee–Rho
  arXiv:0802.2997 body: "most crucial phase transition", "first and last phase transition …
  as the density is increased beyond n₀", "as predicted"). The three script sentences they
  back (constants, neutron star, kaon change-of-state) are within what the quotes carry,
  with fidelity notes F8–F10 recorded. ✔

## 3. Hash pins — PASS

All 12 hashes verified by me this session: A `5e3b9a0e…`, P `b244ea0a…`, L `aa4b459a…`,
D1 `b7519fdf…`, D2 `087b11ca…`, S1 `b806ad1c…` — all MATCH their pins. The storyboard's
recorded authority block (briefs, Kun C08 gate, A, P, L) and its recorded `SCRIPT.md`
sha256 `5c957bef…` all recompute to MATCH.

## 4. Must-not-say sweep — PASS

Mechanical sweep over narration + headings + all closed-world viewer text:

- "BHU is falsified" / "the idea is falsified": absent. The only "falsify the wider" hit is
  P01#8 "This does not falsify the wider black-hole-universe family" — the required denial. ✔
- "Smolin refuted" / "CNS is refuted/falsified": absent; P09#5 states the opposite in A
  137–140's own framing. ✔
- "we measured / we discovered": no unnegated occurrence; P10#1–2 carry the explicit denials
  ("These numbers belong to the pulsar community. We did not discover these stars or
  remeasure their masses."). ✔
- The 2.35-M☉ light-curve star: absent (`2.35`, `J0952`, `0952`, `light-curve`: no hits). ✔
- No invented mechanism for the 4% rule: no `form together`/`accretion`/`common envelope`/
  "why 4%" language; the rule is stated as the source's own (P05#3, P08#7). ✔
- Digits in narration are only the A/P-stated set (1.5, 2, 2.00, 2.08±0.07, 1.599/1.290
  ±0.008, 19.3±0.7, 4, 68.3, 95.4, 8, 3, 5, 2, 1972, 2020, 2026); mass phrasing is "times
  the Sun's mass" throughout. ✔

## 5. Script/storyboard identity — PASS

- Narration byte-identical between `SCRIPT.md` and `STORYBOARD.json` for all 10 panels;
  all 10 per-panel `narration_sha256` values recompute to MATCH; all 10 assertion headings
  match. (`SCRIPT.md`'s trailing "Handoff boundary" section is production prose, not
  narration, and correctly absent from the storyboard panels.)
- Word counts: per-panel counts all match (66/56/57/61/54/58/67/71/69/66); total 625
  (contract says 625, limit 730); Panel 01 = 66 (limit 72).
- `planned_total_seconds` = 312 (sum of panel seconds; limit 355; target window 240–360).
- Estimated narration at 142 wpm recomputes to 264.08 s (contract value exact).
- Authorization block: all six flags false. Production constraints present (deterministic
  text/geometry, closed-world viewer text, no divider cards, digits, mass phrasing).

## 6. Structure contract — PASS

- Verdict complete in Panel 01 within ~35 s: scope label, sealed-rule method, both limb
  outcomes, and the bounded family verdict all land in 66 words / 34 planned seconds. ✔
- Assertion heading on every panel; headings are ledgered claims (ledger §2, 11 rows, all
  MAPPED). ✔
- No divider cards (none in script, storyboard, or VISUALS). ✔
- Ends on the verdict: Panel 10's last sentence and last viewer plate are the bounded chain
  verdict ("This specific Brown–Lee–Rho chain fails by the second rule its own authors
  wrote." / "THIS SPECIFIC CHAIN FAILS ITS AUTHORS' SECOND RULE"); `ends_on_verdict: true`;
  no caveat or future-work tail. ✔

## 7. Comprehension check (Duho's v2 direction) — PASS

From the script alone, a viewer with no physics background can answer:

- What is the BHU idea: "a universe can exist inside a black hole" (P02#1), introduced as
  one 1972 proposal and immediately widened to a disagreeing family of at least 5 (P02).
- What does CNS claim: universes reproduce through black holes, constants mutate slightly
  between generations, more black holes → more descendants, so constants sit near values
  favoring black-hole production (P03, causal order, each term defined at first use —
  "Physical constants are numbers that describe how nature behaves").
- Why do neutron stars test it: CNS's stated falsifiable consequence was a low maximum
  neutron-star mass via the kaon-condensation route, ≈1.5 times the Sun's mass, and these
  masses can be measured through pulsar timing (P04; "neutron star" defined in plain words).
- What happened: 2 tests joined by "or" (P05); heavy-star test reaches serious doubt, not
  strict falsification, while the literal 1.5 ceiling is contradicted (P06); the binary test
  fails the chain by a wide margin, 19.3% vs the source's 4% (P07); the rule was sealed
  first (P08); the chain loses links while the wider family survives (P09); the numbers are
  the pulsar community's and this specific chain fails by its authors' second rule (P10).

Sentences are short, every term is defined at first use or dropped, and the chain is walked
link by link instead of named. The v2 direction is met.

## 8. VISUALS.md — PASS

- All viewer text in VISUALS matches the storyboard's `viewer_text_closed_world` lists
  exactly, panel by panel; the one apparent extra ("disagree", P02) is inside a palette
  design note, not viewer text. Headings match. No claim-bearing text added beyond the
  closed world.
- Mass-ladder honesty rule carried from v1 holds: quoted 68.3% bar (2.01–2.15) sits
  entirely above the 2.00 line; the 95.4% halo crosses 2.00 "with no hard lower endpoint"
  and no invented lower bound; the only numbers near the halo are the 2.00 reference. ✔
- Deterministic geometry throughout (Pillow, fixed shapes); palette semantics preserve the
  boundary (survivors in neutral grey/blue, "must NOT look like bright green/supported";
  dead link red + strike-through; doubt orange/dashed). ✔
- 10 panels, 1920×1080, dark starfield as dim atmosphere only, no claim content in the
  background. No divider cards; Panel 10's final plate is the verdict. ✔

## Verdict

The v2 packet is complete, source-faithful at the cited lines, hash-pinned, inside every
must-not-say boundary, internally identical between script and storyboard, inside the
structure contract, and it satisfies Duho's comprehension direction. `PASS_EXPLAINER_PACKET`.
Next per the sextet order: Tori builds `build/` against these gated files; the
decoded-audio ASR word-diff against this script is not optional; then Kun render gate.

— Kun, 2026-08-18 KST.

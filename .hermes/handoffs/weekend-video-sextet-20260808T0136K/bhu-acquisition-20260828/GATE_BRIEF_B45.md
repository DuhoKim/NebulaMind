# Gate brief — B45, entry 48 read at last (Farhi & Guth 1987, the proof-owner)

**What happened.** Duho's institutional login did not cover the backfiles; the second free
frontier ran instead. Route 2 (KEK scanned preprints) delivered on the first try: Inspire record
234505 → KEKSCAN 2000-36-705 → the KEK scan-server PDF of **MIT-CTP-1400** ("Submitted to:
Physics Letters B", October 1986; published as PLB 183, 149 — entry 48). Pinned at
`../bhu-reading-20260823/sources/farhi_guth_mitctp1400_kekscan_2000_36_705.pdf`
(sha256 573ff9751cec…, 6 scan pages = 10 preprint pages). **Caveat carried everywhere: this is
the PREPRINT scan, not the PLB version of record.** A noisy-OCR companion
(`farhi_guth_mitctp1400_clean.txt`) exists for grep receipts only; the read was VISUAL, page by
page.

**My verdict, for you to attack (b45_entry48_fullread.py):** under the unchanged b28 rule, this
paper's operative contribution IS the no-go derivation — the corpus's cleanest specimen. §II
proves: no spacetime satisfies (a) asymptotically flat parent with noncompact Cauchy
development, (b) T_μν k^μ k^ν ≥ 0 for all null k (their "very weak energy condition" = null EC —
NOTE: weaker than the WEC our entry-49 testimony attributed), (c) a spherically symmetric
false-vacuum region valid to r > 1/χ, (d) nonsingular initial data. Proof in-text: θ_in =
−(1/r)(1−r²χ²), θ_out = 2/r ⇒ anti-trapped spheres for r > 1/χ; Penrose 1965 (time-reversed),
hypotheses individually verified. Author-stated delimitations recorded: nonspherical case
UNDECIDED (§III necessary condition only, Hartle–Wilkins + Gauss–Bonnet average argument);
classical only (quantum ⟨T⟩ the named escape → entry 50); the white-hole footnote; the
compact-Cauchy extension argued not proven.

**TIER: deliberately NOT assigned.** Standing orders reserve tier changes for Duho; the record
carries "READ — TIER PENDING DUHO (question 8)". Do not propose applying a tier yourselves;
rule on the reading and the record.

**Your task — read the scan IN FULL yourself** (render the 6 pages; the OCR is unreliable) and
rule:

1. Does §II actually prove the class exclusion as stated — check the divergence computations
   (eqs. 5–6), the Penrose-theorem hypotheses (a/b/c as the paper lists them), and whether the
   Birkhoff-analogue step (parent need not be spherical if the false-vacuum region's symmetry
   is unperturbed) is load-bearing beyond what my record says.
2. Is my null-EC precision correction right — does the paper anywhere require more than
   T_μν k^μ k^ν ≥ 0 for null k? (It coins "very weak energy condition"; entry 49's summary said
   WEC.)
3. Are the four delimitations faithfully scoped — especially §III's necessary-condition status
   (eqs. 11–15) and the footnote's white-hole escape?
4. Is the entry-48 record edit faithful (block in BHU_PUBLISHED_BIBLIOGRAPHY.md), including the
   preprint-vs-VoR caveat's prominence?
5. Predicate audit of b45 as usual — which checks compute, which are landmarks, is anything
   overclaimed (the OCR-fragility handling included).

**Verdict file:** `<A|C>GATE_B45_VERDICT.md`, first line a single token
(e.g. `ENTRY48_READ_CONFIRMED` / `ENTRY48_REFUTED_<REASON>` / `ENTRY48_NARROWED_<REASON>`).

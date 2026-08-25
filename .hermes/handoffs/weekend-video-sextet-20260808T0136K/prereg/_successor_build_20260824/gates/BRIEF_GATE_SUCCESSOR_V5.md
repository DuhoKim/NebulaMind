# ADVERSARIAL GATE BRIEF — successor preregistration V5 (constitution + reference code)

You are an adversarial gate. REFUSE if you can. Rounds 1–3 refused V2/V3/V4. V5 changed
structure: prose mechanisms moved into a sha-pinned reference implementation that the
constitution declares to BE the definition (§0). Attack both layers and their seam.

## Pin first (custody)

Compute and print sha256 of ALL THREE, and verify against these pins before any review:
- `../PREREG_SUCCESSOR_DRAFT_V5_20260824.md` =
  `1c283bbf6dd7bd598ff5afc429c3d534de82cb26fff47d12bc4ca812b6f22b1d`
- `../ref/successor_ref.py` =
  `67bc4876858c4cb4445ccf40f41a4d3977c1d43e0b88ec5890d9b6b0091a4449`
- `../ref/FIXTURES_20260824.out` =
  `c82b2a253c4f55b9b4f28f697d496f8e8cbf5762771307c036ca77dd65950e25`
Any mismatch: STOP, report, review nothing.

## Context (read-only)

The V4 refusals `GATE_GPT56_SUCCESSOR_V4.md` / `GATE_CODEX_SUCCESSOR_V4.md` (V5 §9 traces
every finding); `../../SUCCESSOR_SCOPE_20260821.md` incl. Amendment 1;
`../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`;
`../../LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`; anything under `../../` a claim cites.
Do not read `/Users/duhokim/NebulaMindData/`.

## Attack surfaces (minimum; add your own)

1. **Run the code.** `python3 ../ref/successor_ref.py --fixtures` must reproduce the pinned
   output byte-for-byte in a matching environment (record yours; report any divergence and its
   cause). Then attack the code as the definition: hunt for nondeterminism the fixtures miss,
   input regimes where a frozen function is wrong or fails open, disagreement between a
   docstring and its body, and places where the constitution's claims exceed what the code
   enforces.
2. **The seam.** Every mechanism the constitution invokes must resolve to a specific code
   symbol with matching semantics (ledger, L_ret basis, exact-mode boundary N_EXACT=16 vs the
   "five counterexamples" claim, stage/prefix addresses at every call site named in §2/§4,
   canonical row order, digest schemas). Any prose mechanism NOT in code is a finding; any
   code behavior not licensed by prose is a finding.
3. **V4 finding closure.** For each of the 18 V4 findings, verify the §9 trace repairs it in
   substance. Execute the old counterexamples where applicable.
4. **Slot machine.** Walk every class-P and class-E slot: producer exists, inputs exist at its
   time, nothing pre-freeze needs post-freeze data, every §-obligation has a slot and vice
   versa (incl. BS-9's R1–R5 rerun and the runner prohibition).
5. **Quotation fidelity** against V3-pred and BS6-pred, byte-level where executable strings
   are claimed.
6. **Loopholes.** Laziest compliant reading of every MUST, especially: BS-2c closure proofs,
   blind-double "interface not bodies" rule, environment scoping of digests, the void rule's
   exemption clause, and Stage-C mask admissibility.

## Report (write ONLY your report in this directory)

`GATE_<YOURSEAT>_SUCCESSOR_V5.md`: pinned shas as computed; your environment; numbered
findings (severity, quote/symbol, why, minimal repair); verdict **PASS** (freeze-candidate
grade) or **REFUSED** (blockers named). Unbacked author statements under Testimony.

# GORU: Number and Source-Line Audit (BHU Closure Video)

**VERDICT: PASS WITH REPAIRS**

**Frozen Artifacts Verified:**
- `NARRATION_DRAFT_V2.md` (SHA-256: 640d43e1ff299d7e4f28a1d6ef2f3f2e6d21c7d1ea91a60fdf68c330a251d937)
- `STORYBOARD_DRAFT_V1.json` (SHA-256: 8f99c03d7af951d71dd11c1028c0510d02c244b766b056c93f7dbb3e390930bc)
- `CLAIM_LINE_LEDGER.md` (SHA-256: 89ac87be41a62c33135be72106781069b434514df663a649c03dc216be95cfb2)
- Source Packet: `LANA_BHU_PREDICTION_DERIVATION_20260811.md` (SHA-256: b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516)

## Findings and Audit Notes

I have audited every number, name, date, and attribution in the script and storyboard against the ledger, and then bypassed the ledger to verify them directly against Lana's source packet.

**1. The 2.08 vs 2.00 Solar Mass Comparison and 68.3% Credibility (PASSED)**
The math is tight and faithfully reflects the packet. 
- The script quotes Fonseca's measurement at $2.08 \pm 0.07$ (packet line 269).
- The script correctly states the 68.3% interval "stays above two". ($2.08 - 0.07 = 2.01$, which is $> 2.00$). This perfectly aligns with packet line 275: *"clears it at the quoted 68.3% credibility"*.
- Demorest's $1.97 \pm 0.04$ is faithfully represented with its center below 2 (packet line 95: *"does not cross 2.00 by central value"*).

**2. All other names, dates, and attributions (PASSED)**
- "Brown-Bethe maximum ~1.5 solar masses" traces cleanly to packet line 264.
- "Brown, Lee, and Rho" and their "serious doubt or simply falsify" quote traces exactly to packet lines 265-267.
- The 5 distinct programmes (closed GR universe, torsion bounce, inherited rotation, CNS, baby-universe/PBH work) precisely match packet sections 1.1–1.6.
- The "added in 2025" date for the rotating-parent axis claim correctly matches packet line 237.

## REQUIRED REPAIR (The 1.95 Hallucination)

Yui's `CLAIM_LINE_LEDGER` accurately reflects the packet, but the drafts themselves contain an injected number that is unsupported by the source text. 

The packet states that Fonseca's measurement *"does not clear 2.00 at 95.4% credibility"* (line 276). It **never** states the exact numerical value of the 95.4% lower bound. Yui has either calculated it externally (assuming a symmetric Gaussian where $2.08 - 2\times0.07 = 1.94$, or $1.96\sigma \approx 1.943$) or sourced it from outside the packet, and landed on `1.95`. This is a source-line violation.

**Execute the following repairs before rendering:**

1. **In `NARRATION_DRAFT_V2.md` (Card 05):**
   *Remove the hallucinated number 1.95.* 
   **Change:** *"But the ninety-five point four percent lower bound is one point nine five."*
   **To:** *"But the ninety-five point four percent lower bound drops below two."* (or equivalent wording that does not assert a specific number).

2. **In `STORYBOARD_DRAFT_V1.json` (Card 05):**
   *Remove the exact numerical plotting instruction for the 95.4% bound.*
   **Change:** *"Add a distinct 95.4% lower-bound arrow ending at 1.95."*
   **To:** *"Add a distinct 95.4% lower-bound arrow ending below 2.00."*

Once the `1.95` figure is purged from both the audio script and the visual diagram, the video is fully cleared for production.

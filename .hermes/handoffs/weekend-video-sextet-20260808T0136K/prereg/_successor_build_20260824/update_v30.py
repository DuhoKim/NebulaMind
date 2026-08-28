import hashlib
import sys

with open('../PREREG_SUCCESSOR_DRAFT_V29_20260827.md', 'r') as f:
    content = f.read()

# 1. Update title
content = content.replace(
    "# PREREGISTRATION DRAFT V29 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT",
    "# PREREGISTRATION DRAFT V30 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT"
)

# 2. Update Section 1
old_section_1 = """## §1 Claim boundary, target, axis, and citation anchors

**Target, cited and verified from source 2026-08-25** (not from memory — the anchor-block
law): Michael J. Longo, *"Detection of a Dipole in the Handedness of Spiral Galaxies with
Redshifts z ~ 0.04"*, Physics Letters B (2011), **doi:10.1016/j.physletb.2011.04.008**,
bibcode **2011PhLB..699..224L**, arXiv:1104.2815. Its abstract states the dipole amplitude
as **"−0.0408 ± 0.011"** from **15,158** spirals, axis **"approximately (l, b) = (52°,
68.5°)"**.

**Sign, stated so it cannot be inverted by a later reader.** Longo's published amplitude
carries a MINUS sign in his convention. Our East-of-North winding convention maps it to
**+0.0408** (V3-pred F-5), and the code constant `A_LONGO = +0.0408` is our-convention while
`A_LONGO_PUBLISHED_SIGNED = −0.0408` records his. The mandatory synthetic absolute-sign
anchor (BS-4) re-establishes the mapping empirically before any real image; the fixture
`BATTERY-SIGN` demonstrates that an injected **−0.0408** sky is never called REPRODUCED.

This tests that published amplitude at that published axis. It does not test A ≈ 0.02,
Shamir, BHU, or whether the sky is isotropic. **Fixed-axis.** The machine axis is the `AXIS`
constant; all coordinate pairs are display-only; frames are ICRS wherever coordinates appear."""

new_section_1 = """## §1 Claim boundary, target, axis, and citation anchors

**Target, cited and verified from source 2026-08-25** (not from memory — the anchor-block
law): Michael J. Longo, *"Detection of a Dipole in the Handedness of Spiral Galaxies with
Redshifts z ~ 0.04"*, Physics Letters B (2011), **doi:10.1016/j.physletb.2011.04.008**,
bibcode **2011PhLB..699..224L**, arXiv:1104.2815. Its abstract states the dipole amplitude
as **"−0.0408 ± 0.011"** from **15,158** spirals, axis **"approximately (l, b) = (52°,
68.5°)"**.

**Counter-anchor, cited and verified directly from the source abstract:** Kate Land, Anže Slosar, Chris Lintott, Dan Andreescu, Steven Bamford, Phil Murray, Robert Nichol, M. Jordan Raddick, Kevin Schawinski, Alex Szalay, Daniel Thomas, Jan Vandenberg, **"Galaxy Zoo: The large-scale spin statistics of spiral galaxies in the Sloan Digital Sky Survey"**, 2008, arXiv:0803.3247. ~37,000 SDSS spirals. The abstract states the winding sense is **"consistent with statistical isotropy"**, with **"no significant dipole signal, and thus no evidence for overall preferred handedness"**, and — after establishing and correcting for a level of bias — that previous studies **"may also be affected and explained by a bias effect."** This published null predates Longo (2011) and is on a comparable sample.

**Bias magnitude (motivation for BS-3's antisymmetry receipt):** The uncorrected Galaxy Zoo 1 handedness asymmetry was ~15% (as reported by a later reanalysis, not read from Land's body text). The amplitude this study tests is 4%. An unmeasured classification bias in the same survey family, on the same task, was nearly four times the signal being sought. That is the motivation for BS-3's `antisymmetry_receipt` field, and it converts the mirror test from a refinement into a prerequisite.

**The literature is split:** A later reanalysis ([arXiv:2302.06530](https://arxiv.org/abs/2302.06530), Shamir) argues the residual post-mirror asymmetry is real and agrees with other methods. This split is recorded as context for why the question is contested.

**Sign, stated so it cannot be inverted by a later reader.** Longo's published amplitude
carries a MINUS sign in his convention. Our East-of-North winding convention maps it to
**+0.0408** (V3-pred F-5), and the code constant `A_LONGO = +0.0408` is our-convention while
`A_LONGO_PUBLISHED_SIGNED = −0.0408` records his. The mandatory synthetic absolute-sign
anchor (BS-4) re-establishes the mapping empirically before any real image; the fixture
`BATTERY-SIGN` demonstrates that an injected **−0.0408** sky is never called REPRODUCED.

This tests that published amplitude at that published axis. It does not test A ≈ 0.02,
Shamir, BHU, or whether the sky is isotropic. **Fixed-axis.** The machine axis is the `AXIS`
constant; all coordinate pairs are display-only; frames are ICRS wherever coordinates appear."""

if old_section_1 not in content:
    print("Error: Could not find Section 1 block in the document.")
    sys.exit(1)

content = content.replace(old_section_1, new_section_1)

# Ensure line 378 and scope statement are unchanged
# The scope statement is inside new_section_1 as the last paragraph, exactly as it was.

with open('../PREREG_SUCCESSOR_DRAFT_V30_20260827.md', 'w') as f:
    f.write(content)

sha = hashlib.sha256(content.encode('utf-8')).hexdigest()
print(f"Success. New SHA256: {sha}")

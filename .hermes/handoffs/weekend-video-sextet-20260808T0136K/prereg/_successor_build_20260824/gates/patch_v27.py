with open('../PREREG_SUCCESSOR_DRAFT_V27_20260827.md', 'r') as f:
    text = f.read()

# Blocker 1: §2.7 (2) and (3)
text = text.replace(
    '(b) the cutout is\n   incomplete at the frozen tensor shape. Instrument absence',
    '(b) the cutout is\n   incomplete at the frozen tensor shape; (c) catalogue quality. Instrument absence'
)
text = text.replace(
    'None of (a)–(b) may read',
    'None of (a)–(c) may read'
)

# Blocker 1: Row E
text = text.replace(
    'authenticated catalogue-quality evidence fields — and computes',
    'authenticated catalogue-quality evidence fields (exact authenticated fields `flux_ivar_r`, `psfsize_r`, `nobs_r` from source digest `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`, joined one-to-one on keys `brickid`, `objid`, verified by the BS-2a pinned verifier, failing nonfatally as an ordinary exclusion) — and computes'
)

# Blocker 1: Row P
text = text.replace(
    '(7) low confidence (dropped; `EXCLUDED-BY-CONFIDENCE`), (8) catalogue quality below frozen threshold (dropped; `EXCLUDED-BY-CATALOGUE-QUALITY`), (9) accepted-finite',
    '(7) low confidence (dropped; `EXCLUDED-BY-CONFIDENCE`), (8) accepted-finite. Catalogue quality is carried only as an already-resolved pre-lock status that cannot constitute a P8 removal'
)

# Blocker 1: Section 5
text = text.replace(
    '**EXCLUDED-BY-ABSENCE**, **EXCLUDED-BY-NONFINITE**, **EXCLUDED-BY-CONFIDENCE**, **EXCLUDED-BY-CATALOGUE-QUALITY**, or **ACCEPTED-FINITE**',
    '**EXCLUDED-BY-ABSENCE**, **EXCLUDED-BY-NONFINITE**, **EXCLUDED-BY-CONFIDENCE**, or **ACCEPTED-FINITE**. Catalogue quality is carried only as an already-resolved pre-lock status that cannot constitute a P8 removal'
)

# Blocker 2: Section 2.6
text = text.replace(
    '- **Stage P on the reduced set: 995/1000 against the x ≥ 962 rule, PASS** — measured',
    '- **Stage P on the reduced set (SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK): 995/1000 against the x ≥ 962 rule** — measured'
)
text = text.replace(
    'These are measured candidate values/evidence only; they do not fill BS-5p or any other unreceipted class-P slot.',
    'BS-5p cannot be filled until Stage P is rerun on the actual post-exclusion mask.'
)

# Blocker 2: Section 4
text = text.replace(
    '**Measured on the real REDUCED geometry (§2.6): 995/1000, PASS, with every\ntrial judged against its own null rather than a shared reference (2026-08-26). The earlier\n997/1000 on the pre-reduction geometry is retracted.**',
    '**Measured on the real REDUCED geometry (§2.6, SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK): 995/1000, with every\ntrial judged against its own null rather than a shared reference (2026-08-26). The earlier\n997/1000 on the pre-reduction geometry is retracted. BS-5p cannot be filled until Stage P is rerun on the actual post-exclusion mask.**'
)

# Blocker 3: False preamble closure claim
text = text.replace(
    'The guard sentence at lines 458-461 and VOID reachability are repaired here.',
    'The guard sentence at lines 458-461 is repaired here.'
)

# Blocker 3: Remove orphan VOID registry ID
text = text.replace(
    '| `VOID-6.1C2-ATTESTATION-FAIL` | §6.1 Row C2 | P2 | VOID |\n',
    ''
)

# Findings mapping: Section 10
text = text.replace(
    '## §10 Gate plan and repair trace',
    '## §10 Gate plan and repair trace\n\nThe findings mapping is enforced. In-band coverage stops at the subject\'s predecessor; the current transition is mapped in the sidecar `gates/FINDINGS_MAP.md`; V1→V15 are exempt by a named rule in the checker, not by silence.'
)

with open('../PREREG_SUCCESSOR_DRAFT_V27_20260827.md', 'w') as f:
    f.write(text)

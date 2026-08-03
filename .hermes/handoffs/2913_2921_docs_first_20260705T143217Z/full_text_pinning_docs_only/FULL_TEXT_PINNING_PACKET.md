# 2913/2921 docs-only full-text pinning packet

Status: `DOCS_ONLY_FULL_TEXT_PINNING_PACKET_COMPLETE_NO_SQL_APPLY`

Created UTC: `2026-07-05T15:17:16Z`

## Verdict

The 2913/2921 dispositions are already complete. This packet pins the surviving claim/evidence links to exact local full-text spans. It is non-executable and creates no SQL/apply artifacts.

## Pins

### Evidence 26678 → claim 2948 (2605.31052v1)
- role: `primary_support_plus_model_dependence`
- modality: `simulation`
- page: `1`
- line: `34`
- char_offset: `2732`
- quote_sha256: `6ad54598dbf28394e3cd6191e103f262e9b364510add94eaa7b330398b03304f`
- adequacy: Supports AGN feedback as a quenching mechanism in simulated massive quenched galaxies, while the same quote explicitly shows model dependence through different thermal/hybrid behavior.
- caveat: Simulation-only source; does not by itself prove a universal observational rule.

> Active Galactic Nucleus (AGN) feedback as the primary quenching mechanism in both the thermal (L200m6 simulation) and hybrid (thermal+jet, L200m7h simulation) AGN feedback models implemented. However, the two models behave differently: while the thermal model efficiently quenches massive galaxies at 𝑧> 3, the hybrid model is less effective because black holes (BHs) grow more slowly in the early Universe, and the jet component, which dominates the feedback energy, acts on longer timescales to impact galaxies.

### Evidence 26678 → claim 2948 (2605.31052v1)
- role: `rapid_quenching_environment_context`
- modality: `simulation`
- page: `1`
- line: `44`
- char_offset: `3961`
- quote_sha256: `e958fd0de47271f0c698018ee79f823ceb173277d05df455891047f781ae9ce2`
- adequacy: Supports the scoped claim phrase that AGN feedback is implicated in rapid quenching, with environment included as a co-driver.
- caveat: Use with the model-dependence pin above; do not present as population-wide certainty.

> Our results highlight the central role of BH growth, AGN feedback and environment in driving rapid quenching in the early Universe.

### Evidence 26679 → claim 2948 (2210.03747v2)
- role: `rapid_quenching_sample_and_agn_implication`
- modality: `observation_plus_simulation_analog`
- page: `1`
- line: `34`
- char_offset: `2173`
- quote_sha256: `c04a4068e79fb7e4427daf5415e68dc81e15abf3137f8896125a11548a2bb34d`
- adequacy: Supports rapid quenching at cosmic noon and AGN implication, while the quote itself carries sample fraction and simulation/speculation language.
- caveat: Selected sample; AGN activity detected in a subset and AGN-causal path partly via TNG analogs/speculation.

> We estimate an average transition time of 300 Myr for the rapid quenching phase. Approximately 4% of quiescent galaxies at z = 1.5 have gone through rapid quenching; this fraction increases to 23% at z = 2.2. We identify analogs in the TNG100 simulation and ﬁnd that rapid quenching for these galaxies is driven by AGNs, and for half of the cases, gas-rich major mergers seem to trigger the starburst. We conclude that these young massive quiescent galaxies are not just rapidly quenched, but also rapidly formed through…

### Evidence 26694 → claim 2546 (1308.5224v1)
- role: `central_density_quenching_link`
- modality: `observation`
- page: `5`
- line: `645`
- char_offset: `31360`
- quote_sha256: `5408fb248683387a1291cf9f652a19a7cc77f77d2aa2f1aa4d69541bf187e983`
- adequacy: Directly supports the central stellar mass density / mass quenching link for claim 2546.
- caveat: This is structural/central-density evidence, not an AGN-feedback evidence row.

> Thus quenching of star formation is accompanied by an increase in Σ1.

### Evidence 26694 → claim 2546 (1308.5224v1)
- role: `necessary_not_sufficient_and_halo_interplay_caveat`
- modality: `observation`
- page: `1`
- line: `22`
- char_offset: `1332`
- quote_sha256: `d21736b381c93882dccfb401b9750b28014528bad1c370027ef1dd47890a752e`
- adequacy: Pins the caveat that the central-density link is not sufficient or monocausal.
- caveat: Preserve this caveat in any future prose or claim rendering; halo/structure interplay is load-bearing.

> the existence of some star-forming galaxies above the threshold Σ1 implies that a dense bulge is necessary but not sufﬁcient to quench a galaxy fully. This would be consistent with a two-step quenching process in which gas within a galaxy is removed or stabilized against star formation by bulge-driven processes (such as a starburst, AGN feedback, or morphological quenching), whereas external gas accretion is suppressed by separate halo-driven processes (such as halo gas shock heating). Quenching thus depends on an …

### Evidence 26694 → claim 2546 (1308.5224v1)
- role: `not_agn_required_caveat`
- modality: `observation`
- page: `2`
- line: `103`
- char_offset: `6201`
- quote_sha256: `632e80374951c475d73207942c47a63cdf88aba28e03c840c0c9dbc21e587d18`
- adequacy: Prevents misrouting this evidence back into AGN-feedback as a monocausal support row.
- caveat: Useful caveat for source-hardening, not a reason to weaken the central-density support link.

> Note that halo quenching does not require the presence of an AGN in order to operate.

## Source hashes
- `2605.31052v1` text_sha256 `ce005a9ae7cf1b094b4368ff7ee79da775e270ed34632d4c5734189016e478a2`; pdf_sha256 `32538ecd2ce38375e4c266a34b2e5e6231bd02ed5d3ea39bfcb8a8784a3625d1`
- `2210.03747v2` text_sha256 `be45bfc5b2c5415e70e7029dc14564311b3eb7338d85ec563ffaa970d9996b26`; pdf_sha256 `32edef7c135596eec55ea32da5cb5d20dd9ca60a0869ad8c402f3e84104d9094`
- `1308.5224v1` text_sha256 `48b154b6fb6b006640a0d4ad83f4bbd343932c21e9bddea7d3a067b58bc78fba`; pdf_sha256 `3d77d8c7a8d8ae0d810c8a77b191db2f7ed1e585082af73780cc6949c5b2fb2d`

## Zero mutation ledger
- DB writes: `0`
- SQL/apply artifacts: `0`
- prose/wiki/page_versions publish: `0`
- trust recompute: `0`
- git/restart/deploy/rollback: `0`
- active phrase: `NO ACTIVE EXECUTION PHRASE`

## Next gate
No execution phrase is minted here. Any future DB/prose/git/rollback action needs a fresh exact packet and explicit approval.

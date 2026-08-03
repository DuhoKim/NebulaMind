# Method2/SFA P3 wiki prose packet

Marker: `GALAXY_EVOLUTION_METHOD2_P3_WIKI_PROSE_PACKET_20260706T142132Z`

Consumed approval phrase: `APPROVE METHOD2 P3 DOCS-ONLY WIKI PROSE PACKET FROM CLAIM-STATUS LEDGER`
Safety phrase: `NO ACTIVE EXECUTION PHRASE`

## Result

- Page prose rows: `1`
- Section prose rows: `5`
- Primary citation anchors: `10`
- P2 NO-GO/gap rows preserved: `32`
- Review checklist rows: `5`

## Page prose

## AGN feedback is scoped, not one-size-fits-all
AGN and SMBH feedback can be part of galaxy quenching and regulation, but the source-first ledger supports it as a scoped pathway whose importance changes with regime and mechanism. In galaxy groups, for example, the feedback energy can be comparable to the binding energy of the gas, making that regime especially sensitive to AGN feedback rather than proving a single outcome for every galaxy [@M2P3-2942-28151].

## Outflows can affect star-forming gas in selected systems
In selected AGN-host and massive-galaxy settings, outflows can disturb or remove star-forming fuel. Observations of z≈1.5–2.5 QSOs report fast, galaxy-wide ionized outflows that are spatially anti-correlated with the brightest star-forming regions, so the clearest wording is that AGN activity can drive or accompany fuel-suppressing outflows in selected systems [@M2P3-2943-28141].

## Other mechanisms and gas-reservoir caveats remain load-bearing
An AGN-only explanation would be too narrow. The accepted rows also support stellar-feedback alternatives and limits: Mg II absorption around galaxies provides evidence that stellar feedback can drive strong outflows and baryon deficiency in low-mass systems [@M2P3-2944-28069], while simulations used to interpret high-redshift observations keep stellar feedback as important in lower- and intermediate-mass systems even when it is not enough by itself for high-mass quenching [@M2P3-2944-28088]. Gas-removal wording also needs caution: outflowing gas in massive galaxies can fall back before travelling beyond 100 kpc [@M2P3-2945-28066], and winds at lower redshift may be insufficient to remove gas from low-mass galaxies [@M2P3-2945-28075].

## Maintenance and kinetic modes are separate from ejective outflows
Preventive or maintenance feedback should not be folded into the same wording as ejective outflows. Hydrodynamical simulations can reproduce many galaxy-population properties only after including AGN feedback, but their outcomes depend on the chosen feedback scheme [@M2P3-2946-28123]. Hot-gas cavity language gives limited observational context for repeated SMBH outbursts in surrounding gas [@M2P3-2946-28158]. Kinetic or radio-mode feedback is likewise best stated as a context-dependent mechanism: relativistic jets may matter even when radio luminosity is modest [@M2P3-2947-28095], and simulations show jets inflating broad bubbles as they move through dense, inhomogeneous gas [@M2P3-2947-28111].

## What the current wording does not claim
This draft does not turn the accepted evidence into a census of how often each pathway quenches galaxies. It keeps positive-feedback, duplicate, background-only, cloud-scale, and scope-mismatched rows out of the prose, and it treats simulations and review-level spans as bounded support rather than direct frequency measurements.

## Primary citation anchor registry

| anchor | claim | evidence | arXiv | epistemic type |
|---|---:|---:|---|---|
| `[@M2P3-2942-28151]` | 2942 | 28151 | 2403.17145v1 | review_synthesis |
| `[@M2P3-2943-28141]` | 2943 | 28141 | 1706.08987v2 | observational_sample |
| `[@M2P3-2944-28069]` | 2944 | 28069 | 2512.05584v2 | review_synthesis |
| `[@M2P3-2944-28088]` | 2944 | 28088 | 2605.03008v1 | simulation_model |
| `[@M2P3-2945-28066]` | 2945 | 28066 | 2512.05584v2 | source_position_synthesis |
| `[@M2P3-2945-28075]` | 2945 | 28075 | 0901.1880v2 | source_position_synthesis |
| `[@M2P3-2946-28123]` | 2946 | 28123 | 2403.17145v1 | simulation_model |
| `[@M2P3-2946-28158]` | 2946 | 28158 | 2403.17145v1 | simulation_model |
| `[@M2P3-2947-28095]` | 2947 | 28095 | 2009.11175v1 | source_position_synthesis |
| `[@M2P3-2947-28111]` | 2947 | 28111 | 2009.11175v1 | simulation_model |

## Preserved NO-GO ledger

All P2 NO-GO/gap rows are copied into `P3_PRESERVED_NO_GO_LEDGER_20260706T142132Z.jsonl`; none are used as inline support.

## Review checklist

| check | owner | status |
|---|---|---|
| METHOD2-P3-REVIEW-001 | Lana | pending_lana_review |
| METHOD2-P3-REVIEW-002 | Goru | pending_goru_review |
| METHOD2-P3-REVIEW-003 | Lana | pending_lana_review |
| METHOD2-P3-REVIEW-004 | Goru | pending_goru_review |
| METHOD2-P3-REVIEW-005 | Hwao | pending_hwao_review |

## Next safe gate

`APPROVE METHOD2 P4 DOCS-ONLY LANA/GORU REVIEW OF WIKI PROSE PACKET`

Product/wiki DB ingest remains a later separate explicit gate after review/refinement.

## Safety ledger

- DB writes: 0
- SQL apply/rollback: 0
- Migration: 0
- Trust recompute: 0
- Live wiki/page_versions publish: 0
- Runtime deploy/restart: 0
- Commit/push/merge: 0
- Production/cloud/API mutation: 0
- Cross-method/shared-parent edit: 0

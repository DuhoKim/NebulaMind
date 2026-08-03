# Hwao — C2 V2 Build Acceptance (PROVISIONAL)

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_C2_V2_BUILD_ACCEPTANCE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Recorded by Hwao/Fable at Deepening Gate 3 from a read-only review of the V2 build. Machine-authored; not human gold. No source/public/DB/product byte changed.
- **Status: PROVISIONALLY ACCEPTED — pending independent checks** (Kun mechanical V2 audit + Goru new-run mapping, dispatched this gate). This accepts the BUILD (fixes applied, preservation honored); it does **not** authorize promotion. V2 remains an isolated, unpublished AI research-note draft.

## Hwao read-only verification
### V1 + source preservation (re-confirmed unchanged this gate)
| file | SHA-256 | status |
|---|---|---|
| V1 `c2-mzr-gated-e2e-candidate/candidate.tex` | `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9` | FROZEN — unchanged |
| V1 `…/candidate.pdf` | `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e` | FROZEN — unchanged |
| source `gated-e2e-demo/draft.tex` | `f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a` | source — unchanged |
| source `gated-e2e-demo.json` | `46ddd75d…` | source — unchanged |
| source/V1/V2 `result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` | byte-identical across all three |

### F1–F4 intent (verified in the rendered PDF text via pdftotext)
- **F1** — Result softened to "We present the two median relations (TNG100 and SDSS); their direct comparison is bounded by the unresolved O/H-scale systematic (see Caveats) and is not interpreted as physical here." The old "provides insights into the relationship" phrase is **absent**.
- **F2** — Abstract now "a bounded, descriptive study"; "**reproducible**" is **absent**.
- **F3** — Abstract carries "scale-limited, TENSION-flagged anchor comparison on un-reconciled O/H scales — see Caveats"; the figure **caption** carries "Median relations on un-reconciled O/H scales; the TNG–SDSS comparison is scale-limited (see Caveats)" (caption text only; figure image byte-identical).
- **F4** — "AI-assembled draft — not submitted, not peer-reviewed (AI_DRAFT_NOT_HUMAN_GOLD)." renders at the top of the Abstract.

### Retention (verified)
Source numbers verbatim (`23,722`, `120,000`, `z=0`, SF-weighted O/H solar-scaled; no invented number/offset); all 5 references incl. **LaraLopez2013**; the Introduction citation **split** (four single-citation sentences); the three caveats — O/H-scale (bounded), TENSION (carried, not upgraded), Provenance — plus the original source Caveats paragraph, none weakened; `AI_DRAFT_NOT_HUMAN_GOLD` retained and reinforced. Compile `rc=0`, `candidate.pdf` 84,831 bytes.

## V2 candidate freeze (immutable during audit)
| file | SHA-256 |
|---|---|
| `…/c2-mzr-gated-e2e-candidate-v2/candidate.tex` | `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6` |
| `…/candidate.pdf` | `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d` |
| `…/result.png` | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` |
| `…/COMPILE_NOTE.md` | `07456dc5685594211724ef187cd59619d003434f13bfa1a30629d28761f49f9e` |
| `…/V1_TO_V2_DIFF.md` | `7950cbf0c2c79afbb3ef5a6f88f0228a9d895fd01406700193cab3fb4de002da` |

## What this acceptance is NOT
It is not a final acceptance and not a publication authorization. Final acceptance depends on the independent Kun mechanical V2 audit (diff limited to F1–F4 + header; old overclaim / "reproducible" absent; references/split/caveats/figure/compile/receipt concordance) and the Goru read-only new-run mapping. Any promotion still requires the later exact publish packet + `APPROVE PUBLISH <packet_id>`, and per the Gate-2 adjudication should target a **new run id** (create-only), never overwrite the baseline `gated-e2e-demo` input.

## Public status
`AWAITING_EXPLICIT_PUBLISH_APPROVAL` — unchanged. Nothing promoted, replaced, or served this gate.

`OVERNIGHT_PAPER_BOARD_HWAO_C2_V2_BUILD_ACCEPTANCE_V1`

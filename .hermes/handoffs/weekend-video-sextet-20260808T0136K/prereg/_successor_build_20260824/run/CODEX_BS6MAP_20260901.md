# BS-6 precondition map — 2026-09-01

## Boundary

This is a read-only judgment map. No image was found, fetched, opened, hashed, or
transported, and BS-6 was not emitted.

## Frozen BS-6 row, exact

From frozen `PREREG_SUCCESSOR_DRAFT_V134_20260831.md` §7:

> | BS-6 | Hwao | image transport approval: closed manifest sha, byte ceiling, producer checksum list | first image byte |

The frozen v9 schema is exactly `("manifest_sha256", "byte_ceiling",
"producer_checksum_list")`. Thus BS-6 consumes the closed-manifest identity,
the transport byte ceiling, and the source-image producer checksum list, and it
emits approval for the first image byte. The acquisition covenant further says:

> **Image bytes only after freeze**, only for the closed manifest, under BS-6, three streams from the start, with the producer checksum list exclusively for source image transport at BS-6

## What must exist first: frozen dependency bytes

The entire §7 Class-P table is headed:

> **Class P — freeze prerequisites**

The load-bearing individual edges are:

> | BS-1 | Duho | release branch A/B + provenance; branch-invariance evidence | — | everything |

> | BS-2a **DESIGN, CLASS P — UNFILLED** | Hwao | **acceptance design**: the absolute, frozen thresholds ... Gated as text AND code **before any image byte**. ... | `run_production_verdict`, pre-verdict validator | BS-2f, BS-6 |

> | BS-2k ⚠ **DESIGN** | Duho | **custody provisioner**: creates stores, escrows keys, installs mediator, records archive seal state. ... | — | BS-6 |

> | BS-2v ⚠ **DESIGN, CLASS P — UNRESOLVED** | Hwao | **`VOID` conversion**: handle every enumerated void antecedent. ... | `VOID_converter` | BS-6 |

> | BS-2c **DESIGN-GATED (V117)** | Hwao + blind double | universe manifest, per-brick counts, zero rows, closure proofs, ceilings, pinned `c_j` bytes | `validate_count_table` via `gates/count_oracle_harness.py` ... | BS-2o |

> | BS-2o | Hwao + blind double | full traversal order + per-prefix ledger | `greedy_ledger`, `ledger_digest` | BS-5p |

> | BS-5p | Hwao | L_min_plan, L_plan, retained basis, x ≥ 962 rule, addresses | `stage_power`, `build_plan` | BS-2s |

> | BS-2s | Hwao + blind double | selected set, L_ret, L_raw, N_eq, fixtures, Stage-P re-pass | `local_pass`, `build_plan` | BS-2m |

> | BS-2m ✅ **FILLED 2026-08-26** | Hwao | **manifest closure**: required set from the frozen cutout planner, counts, refusal on any difference. ... | `close_manifest`, `closure_receipt` | manifest freeze |

> | BS-3 | Hwao | instrument identity: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity | — | BS-9 |

> | BS-9 | Hwao + gpt seat | **input-path rebinding**: branch-specific single-band HDU/plane schema, production input function (code + hash + tensor layout), full R1–R5 rerun through it, gated replacement runner. ... | — | BS-6 |

> | BS-7p | Hwao | randomness/serialization declaration + frozen fixture battery + boundary p-values + environment | `receipt`, `run_fixtures` | BS-6 |

For acceptance specifically, the frozen prose is explicit:

> **Acceptance design is its own class-P slot, and it closes before BS-6.**

> **BS-2f then becomes a value-only realised partition produced by that frozen code**, and BS-6 — the first image byte — depends on BS-2a being filled.

BS-2f is not a pre-BS-6 receipt. The frozen phase line says:

> P0 freeze → P1 BS-6, first image byte → P2 cutout production, pre-inference integrity projection, exact-parent C2 stage-completion, and instrument inference → P3 BS-2f

The on-disk 49,211-row `acquire/positions_selected_cut.csv` and 6,104-brick
mask therefore provide authenticated planning/acceptance evidence, not a lawful
successor BS-2f fill before P1. No `run/classp_candidates/BS-2f.json` exists.

The frozen BS-3g edge is superseded only in order by the disclosed run ruling.
The frozen claim was:

> Binds the seven things §1 requires of it *before* BS-6: **statistic, sample, positional stratification, uncertainty, bound, acceptance rule, and failure consequence.**

The disclosed ruling now says:

> The BS-3g→BS-6 edge is discharged AT BS-6-TIME by what genuinely exists before BS-6, exactly the seven bindings ... PLUS the machinery-HELD robustness rehearsal ... BS-6 may open — the first image byte.

and preserves:

> **The REAL BS-3g sweep + receipt still runs**, the moment BS-8f exists ... Only its ORDER moved — from before-BS-6 to after-BS-8f.

## Current Class-P state

Exactly 16 Class-P slots are present in the frozen table.

| Slot | State now | Why |
|---|---|---|
| BS-1 | **NEEDS-DUHO** | Duho-produced; frozen `resolve_branch(False, date)` cannot truthfully accept Branch B before 2026-09-05. Frozen edge: “blocks everything.” |
| BS-1b | **BLOCKED** | No candidate; depends on the resolved branch and blocks BS-2c. |
| BS-2a | **BLOCKED** | Frozen row remains DESIGN/UNFILLED. The 49,211-row quality-cut artifact is evidence of the three catalogue thresholds, not the missing full acceptance design/receipt. |
| BS-2k | **CANDIDATE-PENDING-VERIFY** | Provisioning materials and a current GO-LIVE receipt exist; they still require lawful ordering behind BS-1 and slot-level acceptance. |
| BS-2v | **BLOCKED** | Frozen row says DESIGN/UNRESOLVED; no converter candidate exists. |
| BS-2c | **CANDIDATE-PENDING-VERIFY** | Authenticated production call is actively running through the only allowed harness; no receipt file yet at map time. |
| BS-2o | **CANDIDATE-PENDING-VERIFY** | Candidate exists; not a live fill. |
| BS-5p | **CANDIDATE-PENDING-VERIFY** | Candidate exists; not a live fill. |
| BS-2s | **CANDIDATE-PENDING-VERIFY** | Candidate exists; not a live fill. |
| BS-2m | **READY** | Frozen row itself marks it filled 2026-08-26. |
| BS-3 | **CANDIDATE-PENDING-VERIFY** | Candidate produced this round through frozen v9; field provenance below. |
| BS-3g | **READY** for the pre-BS-6 edge only | Discharged at BS-6-time by the disclosed cycle ruling's seven bindings plus HELD rehearsal. The real slot receipt remains post-BS-8f and is not fabricated here. |
| BS-9 | **BLOCKED** | No candidate for the required branch-specific rebinding and R1–R5 rerun. |
| BS-4 | **CANDIDATE-PENDING-VERIFY** | Repaired candidate exists; its frozen edge is to unblinding, but it remains a Class-P freeze prerequisite. |
| BS-7p | **CANDIDATE-PENDING-VERIFY** | Repaired candidate exists; directly blocks BS-6. |
| BS-8p | **BLOCKED** | No candidate; Class-P freeze prerequisite, later blocks BS-8f. |

Candidate files now exist for BS-2o, BS-2s, BS-3, BS-4, BS-5p and BS-7p.
BS-2c is executing. No candidate exists for BS-1, BS-1b, BS-2a, BS-2k,
BS-2v, BS-9 or BS-8p (the BS-2k GO-LIVE record is provisioning evidence,
not a v9 slot candidate). BS-2m is the frozen filled slot. BS-3g is handled at
BS-6-time exactly as the disclosed superseding ruling states.

## Ordered path from now to the first image byte

1. **CANDIDATE-PENDING-VERIFY — BS-2c computation.** Let the already-running authenticated `production_build_plan()` finish; authenticate its frozen receipt. This is candidate preparation only and does not override BS-1's “everything” edge.
2. **NEEDS-DUHO — BS-1 on 2026-09-05.** Emit the truthful Branch-B receipt with branch-invariance evidence; before that date the frozen date gate refuses the truthful pair.
3. **BLOCKED — BS-1b.** Produce and verify the Branch-B photo-z product/path/column/join-key/provenance receipt.
4. **BLOCKED — BS-2a.** Complete and gate the full acceptance design and code, then receipt it. The existing 49,211-row mask does not fill this design slot.
5. **CANDIDATE-PENDING-VERIFY — BS-2k.** Verify the current provisioning/GO-LIVE evidence in lawful post-BS-1 order and fill the slot, or re-provision if the verifier rejects it.
6. **BLOCKED — BS-2v.** Build, fixture, verify and receipt the canonical VOID converter against the pinned antecedent registry.
7. **CANDIDATE-PENDING-VERIFY — BS-2c → BS-2o → BS-5p → BS-2s; READY — BS-2m.** Verify candidates in dependency order and close the manifest. Any rejected candidate returns its slot to BLOCKED.
8. **CANDIDATE-PENDING-VERIFY — BS-3.** Verify the fresh receipt below, then fill; **BLOCKED — BS-9.** Perform the required branch-specific input-path rebinding and complete the gated R1–R5 rerun.
9. **CANDIDATE-PENDING-VERIFY — BS-4 and BS-7p.** Verify/fill both; BS-7p is the direct BS-6 blocker. **BLOCKED — BS-8p.** Produce and verify the hand-check plan/allocation prerequisite without touching imagery.
10. **READY — BS-3g pre-BS-6 discharge.** At BS-6-time, bind the seven pre-existing design items and HELD rehearsal under `run/BS6_CYCLE_RULING_20260901.md`; do not pretend the relocated real BS-3g receipt exists.
11. **BLOCKED — construct BS-6.** Only when all freeze prerequisites above are filled, construct the exact three-field receipt from the final closed-manifest SHA-256, an approved byte ceiling, and the producer checksum list. Verify it before any transport.
12. **BLOCKED — first image byte.** It is emitted only by a verified BS-6 approval. BS-2f comes later at P3; no current mask may be used to reverse that ordering.

**First concrete action:** allow the already-running authenticated BS-2c frozen
planner call to finish and verify its receipt; the first live dependency action
remains Duho's truthful BS-1 emission on 2026-09-05.

## BS-2c diagnosis and timing note

**BLOCKED-PENDING-COMPUTE; no candidate claimed this round.** The earlier
standalone process did not die silently. At the final check it was PID 18543,
elapsed 1:42:20, state `R`, consuming 99.7% of one CPU, with no stderr and no
`BS-2c.json` yet. It remains running and was not killed. A short duplicate
diagnostic invocation reached the same frozen stack and was stopped so it would
not steal CPU from the original.

The exact reason for the no-output interval is the only allowed production
entry's coupling: `production_build_plan()` cannot emit BS-2c until frozen
`v9.build_plan()` returns, and that first executes literal
`greedy_ledger()` over all 270,577 positive-count bricks. Its nested Python
selection loop performs 36,606,091,753 candidate comparisons before later
Stage-P work. The process is therefore compute-bound, not silently dead, and
the harness intentionally has no progress output inside that loop. Inputs were
authenticated before dispatch: oracle SHA-256
`01b8b4ecd7da6dc31654881ea4ea6713b0c06464c752d1e7e4de0028cce2103a`,
harness SHA-256
`1a30b8d88ad822b97acd268218415928d605a7ad9ccaf568cfb44d69911b181b`,
and both closure witnesses equal 832,393. Emitting a standalone receipt before
that bound invocation returns would violate the frozen harness, so none was
fabricated.

## BS-3 produced this round

Frozen v9 accepted exactly the three schema fields and emitted body SHA-256
`defb3748862fa72cf3e041dd4ffef332f3e2ddf4ac0fb332cafbd3c19ec993af`
and envelope SHA-256
`52bbedf145c0142bbd6c8358435520a6fffe3627d5024db25550e825d0fc66d4`.

- `weights_sha256`: on-disk `../weights_frozen.pt`, independently hashed this round as `83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d`.
- `tau`: frozen §7 value `4.4006456017494235`, encoded as those exact ASCII bytes.
- `antisymmetry_receipt`: canonical bytes `{"digest":"923d0d0fdc681feed52fc949f9760d1ac67ac7fdb08ccedd56697f464544f177","verdict":"PASS"}`. The digest covers the fresh canonical record: inference-runner code SHA-256 `fa1e033d6c501854eae3517f23c03c270c6108c47383fa18f5960922fc83c45c`, weights SHA-256 above, identity `chi(mirror(x)) = -chi(x)`, 1000/1000 bit-exact identity passes, 1000/1000 byte-exact mirror involutions, maximum absolute residual `0.0`, verdict `PASS`. Runtime was 54.044581 s. Synthetic machinery only; no real image path was touched.

SEAT: CODEX
VERSION: BS6MAP-V1
VERDICT: MAPPED
COUNT: 1

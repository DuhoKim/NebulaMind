# SUCCESSOR BUILD PLAN — expedited, full platoon

Hwao, 2026-08-24 21:36 KST. Authorised by Duho this evening: *"okay go ahead but expedite
leveraging our all available resources."* Scope follows `SUCCESSOR_SCOPE_20260821.md`; nothing
here is frozen; the successor becomes real only at its own sha-pinned freeze after gates and
Duho's sign-off.

## Mission

A preregistered Longo-amplitude test on a footprint chosen for leverage: polar-|cosθ| selection
about the frozen axis n̂_L (α,δ) = (217°, 32°) [carried by quotation from
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`, sha256
b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7, line 124], centred estimator
with exact permutation variance, power gate that names accepted-sample Var(cosθ) as an explicit
input. Fixed-axis only (a test of the published claim; free-axis is a different study — Duho may
override).

## Platoon composition (Duho 2026-08-23: leverage full platoon; engines per resource map)

| seat | engine | job | write area |
|---|---|---|---|
| Hwao | Fable (this session) | rulebook draft (F-1..F-7 rebuild, power gate, sidedness fix), orchestration, merges | `_successor_build_20260824/` root |
| gpt1 | gpt-5.6-sol headless | DR10.1 south sweep-catalog inventory (listing + sizes, receipted; NO bulk download) | `gpt1/` only |
| gpt2 | gpt-5.6-sol headless | blind-double leverage/selection calculator from spec; synthetic fixtures | `gpt2/` only |
| agy | Gemini sub | independent-family review of the draft rulebook vs the 7 design requirements (dispatch after draft exists) | `agy/` only |
| codex | Codex OAuth | formal cross-family gate at freeze | reports only |
| kimi | Moonshot wallet | reserve gate seat (different family) — cost-disciplined, freeze-time only | reports only |

Blind-double rule: gpt2 must NOT read `_successor_instrument_20260823/` (my implementation).
Numbers are compared at merge; only reviewed scripts produce numbers; no lane types a result.

## Phases

1. **Tonight**: gpt1 inventory + gpt2 calculator launch; Hwao rulebook skeleton → draft.
2. **Next**: real-catalog polar selection on DR10.1 sweeps (paced, receipted catalog fetch —
   catalogs are the selection input, not images; χ never involved), Var(cosθ) recomputed on
   actual selected positions (scope-note requirement), leverage receipt blind-doubled.
3. **Gates**: agy design review → repair → gpt-5.6-sol + codex adversarial gates on the frozen
   candidate.
4. **Duho**: freeze sign-off + DR11-vs-DR10.1 call (Sep 5 rule stands; if DR11 photo-z lands
   first, the input catalog swaps, the design does not).
5. **Only after freeze**: polar image manifest + approval file + 3-stream gated transfer from
   day one; then cutter/χ under the new prereg.

## What this build never does before its freeze

No image bytes fetched. No χ value read. No sky statistic over any real spin measurement. The
dead run's sample stays sealed (decline memo remains on Duho's desk, unsigned as of tonight).

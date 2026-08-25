# ADVERSARIAL GATE BRIEF — successor preregistration draft V2

You are an adversarial gate. Your job is to REFUSE this document if you can. A pass you did not
try to break is worthless. You have no stake in the draft passing tonight.

## Pin first (custody)

The file under review is `../PREREG_SUCCESSOR_DRAFT_V2_20260824.md` (relative to this brief).
Compute its sha256 FIRST and print it in your report. It must equal
`8362166cc032945792502dde4b2dc472e0c59b434273084c9e9d63b61944fff5`.
If it does not, STOP and report the mismatch — review nothing.

## Context (read-only)

- `../../SUCCESSOR_SCOPE_20260821.md` — the seven design requirements
- `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — the frozen predecessor; verify
  every "carried by quotation" value in V2 against this file's actual text (axis, amplitude,
  thresholds, F-6 regions, F-7 floor, F-5 convention, Cut-6 items)
- `../agy/REVIEW_AGY_20260824.md` — a prior independent review; V2 claims to repair all eight
  of its findings (§9 traceability). Verify each repair actually repairs, not merely responds.
- You may read anything else under `../../` (the prereg tree) that a claim cites. Do not read
  `/Users/duhokim/NebulaMindData/`.

## Attack surfaces, minimum set (add your own)

1. **Math.** Derive the centred-slope variance under permutation yourself; check §3's formula.
   Check the §3 claim that the slope estimates A directly under `E[s|c] = A·c` — including
   whether footprint asymmetry (c̄ ≠ 0) or the ±1 discreteness of s breaks it, and whether the
   claim holds at the amplitude actually at stake (|A·c| ≤ 1 constraint).
2. **Quotation fidelity.** Any V2 value attributed to V3 that V3 does not contain, or contains
   differently, is a REFUSAL.
3. **Loopholes.** Read every MUST as a hostile engineer: laziest compliant reading. The
   predecessor died of a power gate that accepted a uniform-sphere input; find this document's
   equivalent hole.
4. **Completeness of the decision partition.** §5 must be exhaustive and mutually exclusive
   over all numeric outcomes, including boundary values (p exactly 0.001, exactly 0.05).
5. **Operational realizability.** Every binding slot: can a receipt actually be produced that
   satisfies its text? A slot no receipt can satisfy, or one satisfiable by an empty gesture,
   is a finding.
6. **Self-consistency.** §-references, slot numbers, tolerances, the §4/§5 threshold identity.

## Report (write ONLY your own report file in this directory)

Write `GATE_<YOURSEAT>_SUCCESSOR_V2.md` — seat name per your dispatch instruction. Structure:
pinned sha as computed; numbered findings (severity, quote, why, minimal repair); verdict line:
**PASS** (freeze-candidate grade) or **REFUSED** (with the blocking findings named). Do not edit
any other file. Author statements you cannot back with a shown command go under a Testimony
heading.

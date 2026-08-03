# TORI_ARCHITECTURE_VERDICT_VERIFICATION

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Scope: independent receipt/process verification of the completed sandbox A/B evaluation. No browser or account action was performed for this verification.

## Verified results

### Architecture A — one Mac Studio

- SM-1 pass 1: PASS, 24 in-flight overlap pairs.
- SM-1 pass 2: PASS, 24 in-flight overlap pairs.
- SM-1 pass 3: PASS, 29 in-flight overlap pairs.
- Stable normalized SHA-256 for all three: `91d32b392cd038ac017386d5e9c4267d1e7fe7a3597c95fcd7fbaaf1571f7c16`.
- Result: mechanically viable and 3/3 reproducible.

### Architecture B — Mac Studio + Mac Pro

- Fresh direct-Thunderbolt broker probe `thunderbolt-pass1r1`: PASS.
- Repaired XM-1 pass1r1: PASS.
- In-flight overlap pairs: 22.
- All five target-isolation/broker assertions: true.
- Cross-host freeze denied both writers: true.
- Dropped Thunderbolt CDP forward failed closed: true.
- Studio writer teardown: `term-clean`.
- Mac Pro controller: `stopped=true`, `term-clean`, exit 0.
- Result: mechanically viable in 1/1 run; not yet a 3-run reproducibility result.

## Post-run custody

- Local task processes: 0.
- Mac Pro task processes: 0.
- Temporary broker socket directories: 0.
- Forward port 5592: free.
- Per-pass and main hash-chain ledgers: `VERIFY_OK`; main ledger had 13 entries at verification.
- The duplicate Hwao invocation was refused by the nonempty-passdir gate before execution and did not overwrite the completed pass.

## Factual boundary

The harness used dedicated non-default profiles, exact inert CDP targets, and zero CUA/AX/pointer/keyboard actions. It did not address the user's default Chrome profile or Flow window. This is a source-and-receipt conclusion, not an independent visual observation by Yui; no independent Yui countersign is claimed.

No account, sign-in, credential, prompt, CAPTCHA, submission, or quota action occurred. Therefore this packet proves mechanical browser/process/control-plane concurrency only. It does not prove that Google permits simultaneous live Flow and Deep Research jobs on one account.

## Verdict

- Recommended default: Architecture A, because it is simpler, has no cross-host dependency, and is already 3/3 reproducible.
- Validated upgrade path: Architecture B over direct Thunderbolt when independent desktops and stronger fault isolation are worth the extra transport/controller complexity. It is mechanically proven once; passes 2–3 remain separately held.
- Separately gated live/account step: a bounded Phase-IV same-account overlap canary with fixed quota budget, serialized submissions, challenge freeze, and capture-and-stop. It requires fresh explicit user approval.

Reviewed report SHA-256:

- Hwao verdict: `c32a6dcbe21ef70e2b117dab1233203dbd0f39e9ffaa2fb80777eb21261a2653`
- Hwao non-interference synthesis: `5610ba2c7b33b2284a381aed2e245ea46c2df3abf977b0a212a200f0674a8813`
- Hwao execution state: `03313ef86c265890878a189f1bd9e98f87864a572284a4f4d82de1d27c132659`
- XM-1 browser receipt: `74ec9f6ca0e588e08d7544ac6a15fcd9152a3612ec06ca31dc340e6f3746e98c`
- XM-1 harness receipt: `a4730fca814faae95770dd49da07ad7c0a34308fab5ba414005f9214ee73f79b`

TORI_ARCHITECTURE_VERDICT_VERIFIED_20260714

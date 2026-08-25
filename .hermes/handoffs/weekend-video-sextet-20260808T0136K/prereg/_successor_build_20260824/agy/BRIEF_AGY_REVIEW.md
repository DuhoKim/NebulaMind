# AGY BRIEF — independent-family review of the successor prereg draft

You are the independent-model-family reviewer in Hwao's successor-build lane. Your job is to
find what is wrong, missing, or overclaimed in a preregistration draft BEFORE it goes to formal
adversarial gates. You are not a copy-editor; ignore style.

## Read these (read-only; full paths)

1. `../PREREG_SUCCESSOR_DRAFT_V1_20260824.md` — the draft under review
2. `../../SUCCESSOR_SCOPE_20260821.md` — the seven design requirements it must implement
3. `../../PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` — the predecessor it carries
   quotations from (verify every "carried by quotation" claim against the actual frozen text)

(Relative to this brief's directory. You may read other files under `../../` (the prereg tree)
if a claim cites them. Do not read `/Users/duhokim/NebulaMindData/`.)

## Review axes, in priority order

1. **Requirement coverage:** for each of the scope note's seven requirements, does the draft
   implement it, and where exactly? Quote draft line vs requirement. A requirement satisfied by
   assertion rather than by a mechanism is a finding.
2. **Quotation fidelity:** every value the draft says it carries from V3 (axis, amplitude,
   sigma, thresholds, cuts, floor a=0.85, decision-region arithmetic) — check against V3's
   actual text. Any mismatch, however small, is a top-severity finding.
3. **Internal consistency:** §5 references "V3's exclusion arithmetic" — is that incorporable
   by reference or must it be restated? BS table vs body: does every §-level obligation have a
   slot, and every slot an obligation? Sidedness: is §3's sentence actually testable by BS-7 as
   written?
4. **Loopholes:** the predecessor died because a power gate accepted a uniform-sphere
   calculation. Read this draft as a hostile future engineer: what is the laziest technically-
   compliant reading of each MUST? Name each loophole and the sentence that would close it.
5. **Blind-double integrity:** §6 requires two implementations agreeing on real input. Is the
   agreement criterion defined tightly enough (which numbers, what tolerance, who compares)?

## Deliverable (write ONLY in this directory)

`REVIEW_AGY_20260824.md` — numbered findings, each: severity (BLOCKER / MAJOR / MINOR), the
exact quoted sentence(s) at issue, why it fails, and the minimal repair. End with a one-line
verdict: READY-FOR-GATES or REPAIR-FIRST. Do not edit any other file. The last thing you write
is the deliverable file (it is the completion marker).

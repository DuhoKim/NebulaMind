# DRAFTING BRIEF — §6, sixth pass. Split the projection. Export bits, not values.

You wrote R3, R4 and R5. All three were refereed NOT CLEAR. R5's own Part 4 named the pattern —
renaming a finding instead of repairing it — and R5 then did it again at a higher level of craft.
**This brief exists because the referees found something R5 got right and something structurally
impossible, and the second one changes the design rather than the wording.**

Read `SECTION6_REVIEW_R5_GPT56.md` and `SECTION6_REVIEW_R5_CODEX.md` in full before drafting.
Subject you are replacing: `SECTION6_DRAFT_AGY_R5.md`, sha256
`63782432d816ef74581f5e9d9a181105b9926b7a16bee48acd0288d6593d6654`.

## What R5 got right — keep it

Three named regression attacks failed against R5 in **both** reports. These properties are held.
Preserve them and say in Part 5 that you did:

- the access ban is **universal**, bans access rather than disclosure, no role-scoped carve-out;
- the hand-check committee can complete **G → H → I** without voiding the run it exists to enable;
- the **BS-5f → BS-L → unblinding → BS-7f → BS-V** chain is recordable through named producers, and
  BS-L is class E so it no longer certifies a set containing itself.

CODEX also confirmed V15 §2.7(7) already fixes the confidence threshold in BS-3 before any image
byte, so deferring **application** post-unblinding is legitimate. That is settled; do not reopen it.

And CODEX credits R5 in its own words: moving the projection writer before the named instrument
runner, and removing confidence from the pre-lock projection, is **real movement**. Do not lose
that in the fixing. R5's error was relocating the capability, not failing to move at all.

## Defect 1 — the impossibility. This is the instruction.

Both referees, independently: **a pre-inference writer cannot report whether the instrument
produced finite output, because the instrument has not run.**

R5's C2 emits four fields. Two are properties of image bytes; two are properties of an execution
that has not happened. §2.7 reason (c) — "the instrument returns a non-finite or absent output" —
therefore has **no truthful evidence source** anywhere in R5. Let C2 fill it after D and the
outcome-aware writer returns; leave it and a closed exclusion predicate is unevidenced.

**Split the projection into two contracts with two separately pinned producers:**

1. **Pre-inference cutout facts** — a hermetic integrity transaction over stored bytes and a
   separately pinned pre-inference parent/attempt witness.
2. **Instrument execution facts** — a separately pinned **execution supervisor** that registers
   each attempt *before* launch, atomically commits output bytes together with terminal state, and
   derives presence/finiteness **mechanically inside the sealed boundary**. No process may *choose*
   what status to report. It must not be able to convert a post-output failure, or a suppression,
   into an exclusion or a retry.

Row E verifies authenticated proofs from both. It must never trust a D-authored boolean.

**If no pre-lock non-outcome construction for reason (c) exists, refuse it and say so.** That is an
authorised outcome of this brief, not a failure of it. Deferring or dropping a predicate with the
cost stated is worth more than a predicate with no honest source.

## Defect 2 — the C2 checksum channel. This is the round's primary fork.

Both R5 seats converged on this independently, which makes it the whole remaining objection rather
than one item among several. **R6 must make the channel not exist — not exist somewhere else.**

Duho's instruction names two admissible routes and no third:

- **(a) C2 exports no checksum at all before the lock**, or
- **(b) attempt identity is given a closed form**, so the exported channel has provably finite,
  outcome-free content.

Pick one and build it. A third option — keeping the checksum and arguing it is harmless — is the
renaming move and will be refereed as a refusal.

**If closing the channel costs C2 a capability the pipeline currently relies on, say so and lose the
capability.** That is Duho's explicit authorisation, quoted: *a narrower row you can prove beats a
wider one you have to promise about.* Four rounds have avoided exactly this trade. Name in Part 3
what the pipeline loses and what it now cannot check, and let that cost be visible rather than
covered by a promise.

## Defect 2b — export predicate bits, not values

R5's projection carries the cutout's expected/actual checksum. **R5's own scope (lines 29–35,
54–59) says every cutout is χ-bearing and any opaque digest of χ-bearing bytes is χ-bearing,
because it is a verification oracle.** Item (v) then declares the bundle non-χ-bearing. That is an
internal exception contradicting the governing default — the document disagreeing with itself,
which is the failure mode a linter already caught twice in this text.

Both referees give the same repair:

- **All cutout digests stay inside the sealed boundary.** They are recomputed there, never exported.
- The projection exports **only narrowly enumerated authenticated predicate bits** — for example
  `parent_attempt_present`, `byte_integrity_pass`, `canonical_shape_pass` — each **mechanically
  recomputable by a separately pinned independent verifier**.
- **Every legal value is mechanically fixed.** No free-form identifier, no caller-authored status,
  no field whose value set is open.
- **Close the omission channel.** Exact-parent closure: every parent has exactly one projection, and
  a missing projection is a failure rather than a silent bit. A pixel-reading process can encode a
  sign in *which* projections it declines to write.
- Define the **canonical source and serialization of attempt identity**. R5 left it open, and
  GPT56 notes a derived sign can be encoded in a permitted identifier.

## Defect 3 — "never invokes the classifier" is a promise, not a boundary

C2 already holds the classifier's input. A pinned digest makes one implementation inspectable; it
does not stop an equivalent reimplementation, a lookup, dynamic code, a subprocess, or a local
model under another symbol. Row B can log the permitted read but cannot tell a checksum
computation from an inference over the same bytes.

Specify **enforcement**: a hermetic worker profile with an allowlist over imports, executable and
model weights, filesystem, network, subprocess and sealed-store capability; runtime attestation of
the profile and producer digest; and a BS-2a gate that inspects the real implementation and
**runs adversarial producer fixtures that must fail** — an implementation that tries to encode a
synthetic sign through every writable and missingness channel must be rejected.

Likewise the ordering. R5 says C2 runs before D; D's authorisation column does not mention C2, so
D can lawfully run first. **Make an authenticated C2 stage-completion artifact over the exact
parent/attempt set a hard authorisation prerequisite for D, and require row B to refuse and log any
D touch until it verifies.**

**The R5 fixtures test the wrong direction.** They hold the projection fixed and mutate the sealed
result, which shows nothing downstream *reads* the channel. Nothing tests whether something
upstream *writes* it. Fixtures must rerun the real producer under transformed and adversarial
cutouts.

## Defect 4 — the post-unblinding confidence cut is unbound

GPT56 4: the cut changes the mask, and BS-L, the calibration and the power chain all describe the
mask as locked. Bind the post-unblinding exclusion to the artifacts it invalidates, or state what
it costs.

## Standing constraint

**C2 is pinned at BS-2a, which all three seats refused at 19:02 KST today** — the only confidence
quantity in the frozen record is `abs(chi_net)`, which *is* handedness amplitude. Both R5 referees
flag C2's pin as blocking. Your draft must either supply a BS-2a contract that does not rest on a
handedness quantity, or state plainly that the row cannot be pinned until BS-2a is redesigned.

## Deliverable

Write `SECTION6_DRAFT_AGY_R6.md` here, same five-part structure as R5: the complete replacement
§6; conforming edits outside §6; choices the findings did not force with the alternative to each;
residual risks; and every referee finding mapped to REPAIR or REFUSE.

Do not modify the preregistration. Current text is `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md`.
Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch.

**Renaming a finding counts as refusing it.** REFUSE is a legitimate verdict and an honest one; a
REPAIR that changes a label and leaves a capability is not. If a requirement in this brief is
wrong, say so and do not implement it — I assembled it from two reports, and assembling is the
operation this lane keeps getting wrong.

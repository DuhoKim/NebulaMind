# V138 restart-amendment record — 2026-09-23 21:10:56 KST (Hwao)

V138 re-drafts signed V137-H (`PREREG_SUCCESSOR_DRAFT_V137_20260903.md`, filled-file sha256
`bf46e62a1c9c98935ebe66788bd2847ac94bbe9d33d3056aafbb49158e2544ff`, verified before the build) in place, by
`/Users/duhokim/work/Trio/SPIN_RESTART_READINESS_20260923/hwao/_tmp_build_v138.py` (every anchor asserted; the build
aborts on a drifted line). No pixel or network was used; no signed or pinned input was edited; `successor_ref_v9.py`
stays `6a9abbbd900db882…`.

## Rulings applied (verbatim record: `SPIN_RESTART_READINESS_20260923/blanc/DUHO_RULINGS_20260923.md`)
18:32:01+09:00 "A with B, waive with disclosure" · 18:34:56 "Tier A with disclosure, repair attempt first, stratified 2,000" ·
19:09:10 "1 as your rec" (BS-3 → R2 reader) · 20:59:39 "okay i sign V138 go ahead with next run" (intent, not a signature).

## Choices 2–6 — RULED-20260923-DECISIONPAGE (Duho, decision page, 2026-09-23T21:19:36+09:00); q2m — RULED-20260923-CHAT (21:22:09+09:00, YES)
| choice | ruled |
|---|---|
| 2 readability instrument | **A**: two agy/Gemini readers, full rubric byte-pinned (`READER_INSTRUCTIONS.md` d0912249…), fresh state per call, decoy-isolation + mirror-invariance fixtures, identity-stripped cutouts via Row B (new Row D3). **q2m YES**: external AI readers may receive identity-stripped cutouts through the mediator. |
| 3 positive-control constants | N-PC 400, A-MIN 0.50, DIR-MIN 0.90, Wilson 95% lower bounds, pinned list drawn from the 1,079 DR10 labelled targets |
| 4 BS-3g edge | (a) explicit release of BS-6 by signature; invariance claim struck; limitation printed in every result |
| 5 BS-RG | new class-P slot; counts 16 → 17 emitted by `tools/prereg_counts.py` |
| 6 BS-2k roster | single-holder roster stands as committed (`ref/BS2K_CONSTANTS_COMMIT_20260831.md` ccaf9f34…) |
| 7 checkers | provisioning data, not prereg text — still open |
No PROVISIONAL-BLANC-REC tag and no `[[DUHO]]` mark remains in the draft.

## Hunks (diff V137-H → V138, 70 changed lines; FINAL build 2026-09-23 21:27:26 KST)
1c1 3c3,5 138a141,142 603c607 731c735 736a741 781c786 782a788,789 866a874,895 867a897 868a899,907 926c965 940,941c979,980 945a985 1163a1204 1252c1293,1300 1619,1620c1667,1668
(title, preamble incl. the a_eff sentence, V138 constants · §1 status · §6 Disclosure bullet · Row A · Row D3 · §6.2 · §6.4–§6.7 · §7 count sentence · BS-3, BS-3g · BS-RG · §10 V136 → V137-H row · §11 items · signature lines blank)

## Build history, disclosed
Six builds from the same asserted-anchor script (`hwao/_tmp_build_v138.py`); only the last is signable:
1. 21:08 KST `5b177771…` — lacked the numeric Q9 clause and the a_eff preamble sentence (Blanc addendum 21:00).
2. 21:12 `d5e91de2…` — added them; carried ten literal `\'` escapes from a raw Python string.
3. 21:13 `042c4799…` — escapes stripped (0 backslash-quotes). Blanc verified this digest from disk and issued the referee GO against it.
4. 21:22 `e323f537…` — choices 2–6 folded as RULED-20260923-DECISIONPAGE; the open q2m written as the one `[[DUHO]]` mark.
5. 21:23 `79bda80e…` — EA-3 import made conditional on an admissibility receipt after the synthetic test measured 1–6 ULP feature drift.
6. 21:25 `b764b56a4c356237…` — q2m folded as RULED-20260923-CHAT (YES); no mark remains. **Referee round 1 targets this digest**, not 042c4799….

## Verification
```
tools/prereg_trace.py --check   137 computed transition(s); 0 problem(s)   (after the V137 → V138 FINDINGS_MAP entry)
tools/prereg_lint.py            97 finding(s), 0 blocking                  (after regenerating STRING_FIELD_REGISTRY from V138)
tools/prereg_counts.py          17 class P, 9 class E; prose matches the table
shasum -c P0_PACKAGE_MANIFEST_20260831.txt   30/30 OK
```
Sidecars (neither is in the P0 manifest): `gates/FINDINGS_MAP.md` sha256 `2d29dc9040432e72017ea2e76705581b4bf7bec31c0a2208c2bbf8713080c209`
(previous copy kept as `gates/_tmp_FINDINGS_MAP_before_v138.md`); `ref/STRING_FIELD_REGISTRY.md` sha256
`61bee04b2f214f81284ba8c0081737ac8e1e6cd7a5987fd9b2745d84cbb814c6` (315 fields, 0 forbidden, 0 stale; V137 copy kept as
`ref/_tmp_STRING_FIELD_REGISTRY_v137.md`).

## Signing
Plain sha256 of `PREREG_SUCCESSOR_DRAFT_V138_20260923.md` with `SIGNATURE UTC:` and `DUHO SIGNATURE:` blank (lines 1667–1668):
```
43babefb365b595c0e7bda894a202c1dfe8b5d367d80dc733a901c93740399f7
```
Binds when Duho states this digest in chat with the UTC, Blanc relays verbatim, Hwao fills the two lines and records the
amendment (the filled-file digest then goes into V139's §10 row). Referee round 1 (agy) is prepared, not launched:
`SPIN_RESTART_READINESS_20260923/hwao/V138_REFEREE_DISPATCH_READY.md`.

## Carried, not repaired (so nobody reads silence as oversight)
Row C2 still calls `verify_cutout_integrity` "to be pinned at BS-2a (DESIGN, defined, UNFILLED)" though BS-2a was FILLED
2026-09-03 (Tori Q2); the §11 build items are REQUIRED; lane-side drafts exist and are pinned in `SPIN_RESTART_READINESS_20260923/hwao/_prep/` (assembler `assemble_reader_r2_v138.py`, replay driver `replay_r2_v138.py`, positive control `positive_control_readability.py`; digests in `V138_SIGNABLE.md`) — they become §11 pins only when placed under `gates/`/`ref/` and refereed; BS-7p/BS-4 under the R2 identity are REQUIRED.

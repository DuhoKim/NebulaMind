REFUTED_CHI_CUSTODY_R7

# Chi custody receipt Revision 7 — adversarial gate

## Executive finding

Revision 7 is refuted. The live receipt matched the dispatch snapshot exactly at both the opening and closing pin checks, but the pinned artifact does not satisfy its own custody and table-binding claims. The decisive failures are: (1) the receipt's fenced table is not byte-identical to `tables_R7.txt`; (2) the required gate output makes the advertised fresh-run comparison fail because the generator scans future `GATE_*.md` files; (3) the ledger chain cannot detect suffix truncation or a wholesale self-consistent rewrite; and (4) a fresh 218-audio numeric sweep found three genuine caption/audio divergences, contradicting the claimed zero.

No remedy is proposed in this report.

## Scope and dispatch identity

- Live target at start: `CHI_CUSTODY_RECEIPT_20260821.md` sha256 `879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e`.
- Pinned snapshot: `_custody_20260821/_gated/CHI_CUSTODY_RECEIPT_20260821.879ec60426ea.md`, same full sha256.
- `cmp` at start: exit 0. Final pre-report pin check: both hashes still identical; `cmp` exit 0.
- The pinned snapshot carried `uchg`; the live source did not need that flag for the identity check.
- No file under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened or read. All audit writes before this report used names beginning `prereg/_tmp_gate_r7_`.
- A bounded condition-1 content search incidentally surfaced stale `_tmp_gate_*` and synthetic-rehearsal excerpts. Their hashes are recorded in the appendix, but those stale sibling materials did not bind or determine this verdict.

## Finding 1 — the table binding fails twice

### 1A. The fenced block is not byte-identical

The pinned table file itself is correct:

- `_custody_20260821/tables_R7.txt`: 4,321 bytes, sha256 `d928dd1f65d4293e2a64424f46e46308676c8898f14e1e9e94fa8599d5936ca6`.
- Fresh pre-output command `python3 _custody_20260821/build_custody_tables.py | diff - _custody_20260821/tables_R7.txt`: exit 0.

The receipt's fenced payload is different:

- fenced bytes: 4,320, sha256 `0714687e5b859913fb21adf0b166deb5feb55b1b9f1996b0723db9600c47ad53`;
- table bytes: 4,321, sha256 `d928dd1f65d4293e2a64424f46e46308676c8898f14e1e9e94fa8599d5936ca6`;
- first and only difference: offset 4,320, where the file has terminal byte `0x0a` and the fenced payload has ended.

Thus the file matches a fresh run, but the fenced block is not byte-identical to the file. Under the brief's explicit three-way byte test, the binding is theatre even though the displayed rows are semantically the same.

### 1B. The advertised verifier is self-invalidating after this required gate output exists

`build_custody_tables.py:39-43` scans every `GATE_*.md` in the lane and prints each basename and first-line verdict. The required deliverable is itself named `GATE_CHI_CUSTODY_R7_20260821.md`. Therefore the receipt's command can match only before the verifier writes the required gate result. Once this report exists, a fresh run necessarily gains a new gate-history row and differs from the pinned table.

Final post-write rerun produced `post_write_fresh_diff_exit=1` and exactly this added generator row relative to the pinned table:

```text
GATE_CHI_CUSTODY_R7_20260821.md
    verdict         : REFUTED_CHI_CUSTODY_R7
    hashes cited    : Rev1, Rev2, Rev3(current)
```

This is not concurrent source drift: the 257-file pre-run input/hash inventory was rehashed before report creation with zero changes.

## Finding 2 — the ledger is not tamper-evident against the attacks named in the receipt

`gate_snapshot.sh` now records `prev_ledger_sha256` as the hash of the complete ledger prefix before each append (`gate_snapshot.sh:27-28`). That catches an edit to an earlier prefix only while a later untouched record survives. It does not catch suffix truncation, truncation to empty, or wholesale reconstruction of a new internally consistent history.

Fresh tests were run against a byte-copy of the live script under `_tmp_gate_r7_mechanism_ours/`:

- A legitimate 3-record chain verified internally.
- Removing the final record left a 2-record prefix that still verified: original sha256 `7b27bbe7e625bdfca8008386931369a1886f4bf63e42d183b58b2293fdd36027`; truncated sha256 `b3df0eab99e893016e6cd7e9ca65b696ae4d6273ace12ca6515a0486a49367b1`; internal consistency remained true.
- Replacing the entire ledger with two invented records whose predecessor fields were recomputed produced a self-consistent ledger, sha256 `1057986bd8b45b6fbde8538d308c84993937a51d03f1768c06648df3c0c77edd`.
- The unmodified snapshot script then appended to that forged history with exit 0, used the forged ledger hash as its predecessor, and left the resulting 3-line chain internally consistent.

The production ledger is also only partially migrated: line 1 has no `prev_ledger_sha256`; line 2 correctly equals the sha256 of the complete legacy line-1 prefix. The production file itself is writable (`-rw-r--r--`, no `uchg`). There is no externally retained terminal hash or expected length in Revision 7. Consequently, “an edit or truncation is detectable afterwards” (`CHI_CUSTODY_RECEIPT_20260821.md:171-175`) is false for the named suffix and wholesale attacks.

The narrower snapshot mechanisms were attacked and mostly held:

- Actual-host `chflags uchg` was set on a fresh snapshot; a direct overwrite failed with `EPERM`.
- Owner command `chflags nouchg <snapshot>` returned 0 and cleared the flag, exactly as the receipt admits.
- After clearing the flag and substituting different bytes at the expected destination, the full-digest check exited 2 and printed the destination and source full digests. This repair works.
- The script suppresses `chflags` failure (`2>/dev/null || true`). With a failing `chflags` injected ahead of the real binary in `PATH`, the script exited 0, announced a snapshot, and left flags `-`. Thus it attempts the flag but does not enforce that it was set.

The phrase “tamper-evident, not immutable” is therefore only partly honest: the owner-undo limitation is candid, and an externally pinned snapshot digest is evidentiary, but the local ledger itself is not tamper-evident against suffix truncation or wholesale rewrite.

## Finding 3 — the claimed 218-report audio clearance is false

I independently rebuilt the physical sweep population as 215 non-`latest` root MP3/caption pairs plus all 3 `_drafts` MP3/caption pairs = 218 paths. This preserves both root and draft copies when the same stem exists and excludes the mutable `latest` alias. A first-pass inventory mistake deduplicated one draft stem while including `latest`; it was corrected by dropping `latest` and freshly transcribing the omitted draft path. The correction is explicit in `_tmp_gate_r7_fresh_asr_beam5_adjudication.jsonl`.

Fresh ASR used `faster-whisper 1.2.1`, `ctranslate2 4.8.1`, `Systran/faster-whisper-base.en`, int8 CPU. Every MP3 and caption reviewed is fully hashed in the appendix. Beam-1 screened all paths; every mismatch was inspected, beam-5 reran the non-`latest` mismatches, and the omitted draft path was also run at beam 5.

Three genuine numeric divergences survive:

1. `20260814T160157-variance-pass`
   - MP3 sha256 `78471d4147bce699f29fa0343220068656d2847f8e718a5b175c3b111e286c02` says `832,000 objects` in both beam-1 and beam-5 fresh transcripts.
   - Current caption sha256 `fa46299e4a502ac08f9d9ed4c89a653988e031be53973db6ba832ec6726fcfe2` says `800 and 32,000 objects` (`:2`).
   - This caption is one of the nine declared repaired. Its decimal repair (`0.445`, `0.15`) is correct, but the connector-splitting corruption remains in both the current and retained-original caption.

2. `20260814T161526-ten-blockers`
   - MP3 sha256 `3913befc8faf7c4fbcbf4add6d7c3c4c263aad4bdbb58899a4b97faca614eafb` says `130,000` in both fresh ASR passes.
   - Current caption sha256 `d8feafae500939283af646440e7d22f05634fc4d7a058eba69be8594c0944e45` says `a 100 and 30,000` (`:2`).
   - This is another of the nine declared repaired. Its `0.008` repair is correct, but the same connector-splitting family remains elsewhere in the caption.

3. `20260821T151843-hwao-report`
   - Caption sha256 `fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c` ends: `one galaxy at a time, 200,000 times` (`:15`).
   - MP3 sha256 `5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3` ends after `one galaxy at a time` in both beam-1 and beam-5 transcripts.
   - An independent 16 kHz extraction of the final 7.312 seconds (sha256 `89c3e4f04f334b319bb3e7cea7d3dcdad9140fad9f728dc47457a3441259c6c2`) with word timestamps ends at `time` and contains no `200,000`.

Other automated mismatches were representation or ASR artifacts, including bare `one`/`zero`, `1:52` rendered as `152`, `4 of 4` rendered as `404`, and `DR10.1` tokenization. They were not counted as genuine caption/audio divergences. The target 23:12 report cleared with sign normalization: fresh ASR says `0.834336, 0.384410, and minus 0.640352`, matching the corrected caption.

Therefore Revision 7's “0 genuine divergences” and the underlying claim that all nine captions are repaired as captions are false. The receipt also pins no result artifact, transcript set, model digest, or command for Blanc's alleged sweep; it takes the prose number on trust. The fresh run shows that trust was misplaced.

## Finding 4 — the condition-2 conclusion holds, but one stated premise is false

The frozen authorization is unambiguous:

- Condition 1 is only the partial-tertile prohibition (`K8_CROSSING_AUTHORIZATION_20260820.md:28-31`). No scoped, non-synthetic artifact reviewed here establishes that a partial real-chi tertile was computed. Because the forbidden data tree was not opened, this is “no breach established in the authorized evidence boundary,” not a universal proof about every possible runtime byte.
- Condition 2 bars any sky statistic, dipole, or summary over chi (`:32-33`). The sentence `One leaning each way among the confident pair` is a sign/count summary and independently breaches condition 2.
- Section 4 separately says publication of any kind was not authorized (`:46-50`).
- The same frozen text explicitly spends the chirality-label clause (`:20-24`) and authorizes incremental per-object chi execution (`:52-59`). The reading “measurement licensed; publication not licensed; condition 2 not spent by this authorization” is correct.

But Revision 7 says the report published “the complete set of values then in existence” (`CHI_CUSTODY_RECEIPT_20260821.md:58-60`). The report itself says only the first 3 values and, later in the same caption/audio, says `2,725 galaxies measured`. At publication time the disclosed three were not the complete set then in existence. Condition 2 remains breached because of the sign summary and the express publication bar; this particular factual premise does not survive re-derivation.

## Finding 5 — the exposure framing is candid, but “one publication event / never republished” counts ledger vocabulary instead of public-state mutation

The assertion that correction increased text exposure is accurate. The target caption changed from sha256 `7c8a8668a00cd9b8692b49b4fd4ff93dedb40620a235830df38e4515dac640ad` to `2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162`. Reversing only the recorded caption repair in the current report page reconstructs the old full sha exactly (`c5d5d5b81f5ae997e239203d2cd8e7e6c3065dc043069830ba138a29b9f6e9e7`); reversing the two relevant row-scoped repairs in `archive.html` reconstructs its old full sha exactly (`36a0499615eb74ca1fdacf7338084d9744891f34025630bb833a2e2e78710178`). This independently establishes causation for the three changed digests.

Saying the consequence is Duho's to ratify is not, by itself, evasion: the author disclaims authority and acknowledges that the breach widened. It cannot retroactively change the frozen fact that publication was not authorized.

The surrounding headline is misleading, however. The ledger has one `publish` row for seq 20, but it later has `caption_corrected`, and the public caption, report HTML, and archive HTML were replaced on 2026-08-21. Calling that “never republished” is true only under a narrow queue-event vocabulary; it is false as a statement that the public state had only one publication mutation.

## Attack-3 claim matrix

| Claim | Independent result |
|---|---|
| Six listed files and current digests | All six full hashes match Revision 7. |
| Three digests changed because captions were repaired | Holds exactly by reverse-repair full-hash reconstruction. |
| Audio says `0.834336, 0.384410, -0.640352` | Holds under fresh beam-5 ASR of the pinned MP3. |
| Nine `caption_corrected` events | Holds: 9 events, 9 distinct files. |
| Nine retained originals | Holds: all 9 exist; every recorded before/after pair is present in the retained/current files. |
| All nine captions repaired | Fails as a whole-caption claim: two still contain connector-split numbers. |
| 218-report numeric sweep, 0 genuine divergences | Fails: fresh corrected physical inventory found 3 genuine divergences. |
| Exactly one report carries the real 23:12 chi values | Holds for the scanned local report set. |

The “six surfaces” count is an artifact-bundle count, not six value-rendering surfaces. The alignment JSON contains timing endpoints but no chi value. The deck JSON contains the three values only in a non-rendered diagnostic note that says they were “not in the audio,” a statement independently contradicted by fresh ASR. The audio, corrected caption, report HTML, and archive HTML are direct viewer-facing value surfaces.

## Failed attacks / facts that held

- The live receipt did not drift from its dispatch snapshot.
- The pinned `tables_R7.txt` digest is exact and matched a fresh generator run before this gate report existed.
- The destination full-digest substitution check fired with exit 2.
- `uchg` was actually set on this host and blocked an accidental overwrite until the owner removed it.
- All six current target-artifact hashes match the receipt.
- The target MP3 independently speaks the three stated full-precision chi values.
- There are exactly nine correction events and nine retained originals, and every correction pair recorded in the ledger exists in the corresponding old/current captions.
- The three changed target-surface digests are causally attributable to caption repair.
- K-8 spent the chirality-label clause, licensed measuring, retained condition 2, and expressly did not authorize publication.
- The sign sentence is independently a condition-2 summary even without relying on the false “complete set” premise.
- The statement that accurate caption repair increased text exposure is honest; Duho's decision ownership is honestly named.

## Evidence commands and outcomes

Core machine checks (all read-only except `_tmp_gate_r7_*` evidence and this report):

1. `shasum -a 256` + `cmp -s` on live receipt and dispatch snapshot — both `879ec604...`, compare 0 at start and final pre-report check.
2. `python3 _custody_20260821/build_custody_tables.py | diff - _custody_20260821/tables_R7.txt` — pre-output exit 0.
3. Byte extraction of the receipt fence versus `tables_R7.txt` — 4,320 vs 4,321 bytes; mismatch only at terminal LF.
4. `_tmp_gate_r7_mechanism_test.py` against a copied live script — actual `uchg`, owner unlock, substitution refusal, silent flag-failure path, suffix truncation, wholesale rewrite, append-after-forgery.
5. Production-ledger prefix-hash verification — legacy first row unchained; second row correctly hashes the legacy prefix.
6. Queue-ledger parse — 55 records, 9 `caption_corrected`, no preserved 218-sweep result event.
7. Nine-caption before/after verification — all intended pairs and originals present; hashes recorded below.
8. Reverse-repair reconstruction of target report and archive — old full digests reproduced exactly.
9. Fresh local ASR — 218 corrected physical paths, all mismatches inspected, beam-5 adjudication, explicit final-tail extraction for the caption-only `200,000`.
10. Rehash of the 257 artifacts consumed by the pre-output table run — zero concurrent changes.
11. Post-write table diff — recorded above after this report first existed.

## Uncertainties and deliberately uninspected material

- Nothing under `/Users/duhokim/NebulaMindData/chi_dr10_south/` was opened. The condition-1 conclusion is bounded accordingly.
- The fresh ASR comparison establishes numeric agreement/divergence, not word-for-word transcript fidelity. Fresh target ASR itself has harmless word errors; Revision 7 correctly says word corruption is outside the numeric sweep.
- No external platform was inspected. This gate evaluates the six named local artifacts and named local evidence.
- Stale sibling gate prose was not used as authority. Generator-opened and incidental-search artifacts are hashed only to make this audit's own read set complete.

## Complete SHA-256 ledger of reviewed artifacts

This appendix records every task artifact whose bytes were opened or computationally reviewed, including the 257 files consumed by the fresh table generator, all 218 ASR MP3/caption paths, mechanism-test evidence, model files, and incidental bounded-search hits. Count: 604. The standalone TSV assembled immediately before report creation had sha256 `9eb3814687a3dc0423065c0ae8e6e28b23d0316711d11c7fe154831bf3f76c14`; its rows follow verbatim.

```tsv
sha256	bytes	path
f1d0fff528decad815b9a5c270c4eef001b26802389d8ade58f48ab8444f73b8	1332096	/Users/duhokim/HermesOps/reports/status-audio/20260811T143349-audiofix.mp3
4d9e4e287529d7dbebb34c096fc95a18f103864d262c0e8dd595867929a53aec	1429	/Users/duhokim/HermesOps/reports/status-audio/20260811T143349-audiofix.txt
d31a6096d26af0b2bb5e674bf939933f4a7623dd81c1698b8fa16786e0515975	1774464	/Users/duhokim/HermesOps/reports/status-audio/20260811T143640-kunpass-external.mp3
e8dca2bfd479ee6ed402b9ec1cb38179cb0238cfbf1cae3e332afa29fe3c691d	1926	/Users/duhokim/HermesOps/reports/status-audio/20260811T143640-kunpass-external.txt
249ba83d74298f3c3382e855171b3fc9a6a456e8a3f364dbbcdb3347bf93dda5	1934592	/Users/duhokim/HermesOps/reports/status-audio/20260811T144815-catchup.mp3
5fab361db7034781fd64b1981db07a540dec08ac614900cb3011ff75c8327d09	2028	/Users/duhokim/HermesOps/reports/status-audio/20260811T144815-catchup.txt
c273aeee90d35de0b8beb579f6d81fc866b8affc572270cf8a7958227b60fb22	2160768	/Users/duhokim/HermesOps/reports/status-audio/20260811T145155-tori-binding.mp3
0999aa223d9644f487088230600c05fbaf2e0dff05f70b55edc1d283914df87e	2205	/Users/duhokim/HermesOps/reports/status-audio/20260811T145155-tori-binding.txt
1af0cd7b8b7f1989334ac2d8b9bef9d1e66bda9f550b1c90f11f8a9d9f90658d	1589760	/Users/duhokim/HermesOps/reports/status-audio/20260811T145652-cockpit-publish.mp3
7feaace6c2957292671106be2bed8ab3b70cd5c819461ecbe1e36c06bdafa1e4	1637	/Users/duhokim/HermesOps/reports/status-audio/20260811T145652-cockpit-publish.txt
a073a0685ed038b220f656bf06d1ae264389a0ae7784b2103ed859d0ac6f6de8	1960320	/Users/duhokim/HermesOps/reports/status-audio/20260811T152421-render-fail-fix.mp3
c6024185199b24e520aef729c47dbaf451afe11cd3d5db63ff236486cb5d8a75	2048	/Users/duhokim/HermesOps/reports/status-audio/20260811T152421-render-fail-fix.txt
0533500b9f997126cb4264bc6b6e70cfe514ac49481c0611e287935cafdedd73	1792896	/Users/duhokim/HermesOps/reports/status-audio/20260811T153647-v3.mp3
6eafa42e7ec9c91823f3e8cbd0157a1dcb2da796502a5f27b38556d8f8ff7295	2001	/Users/duhokim/HermesOps/reports/status-audio/20260811T153647-v3.txt
d23b7b26c264f123e7ad1a5c7ff49dbb0f1a50bbfd4df0a624b778c8f7535302	1626624	/Users/duhokim/HermesOps/reports/status-audio/20260811T154352-v3-wait-studio.mp3
20fbf495b1ce0375251950b9dc924575ebf273987d15e50438f96447cc5d13bd	1672	/Users/duhokim/HermesOps/reports/status-audio/20260811T154352-v3-wait-studio.txt
b952a754a03acf171a29c45410c6c0afaa09c37916b21efc00093b30d65323b5	2353920	/Users/duhokim/HermesOps/reports/status-audio/20260811T154757-where-and-what.mp3
86cb6e5f1b40fc504a8a9c0f6d8796c3dd2ff5fdf4af9ef0f8ca3b6cd760d234	2451	/Users/duhokim/HermesOps/reports/status-audio/20260811T154757-where-and-what.txt
03aa3d67191e3a5b4c6feeac80c740a9d856bd625121eaa3ecb8f60762b7dd1c	1961088	/Users/duhokim/HermesOps/reports/status-audio/20260811T155136-video-start.mp3
cde69aa02a9ae5ed7076c3f320bead7f68f3fc857b46dec7d15b6a3da176b505	2026	/Users/duhokim/HermesOps/reports/status-audio/20260811T155136-video-start.txt
457758de52bb9e998e0e352614cdabf12970d4b0729f3ff2dead18706e8adf74	1959168	/Users/duhokim/HermesOps/reports/status-audio/20260811T155909-lana-brief.mp3
25a4c92527b5d0532852ff3195c78511d5dd97ee4452c5f765da4a3a1bb608f7	2051	/Users/duhokim/HermesOps/reports/status-audio/20260811T155909-lana-brief.txt
8c3ddae3e609ef6b41775c2480f3f6dad519b00fee3ef03d06366d5f7b8bf75b	1843200	/Users/duhokim/HermesOps/reports/status-audio/20260811T160606-v4.mp3
3443fbf95ab10103ecf2974e137001f04f74baef86f2a019aa14570722acd1ac	1921	/Users/duhokim/HermesOps/reports/status-audio/20260811T160606-v4.txt
c932a1c4ed193589ada1c1c067ca95237dcdb34584cb9e615c01a2bd71016ff4	1848960	/Users/duhokim/HermesOps/reports/status-audio/20260811T161156-video-landed.mp3
1886d1e531c7f22fa47a7ad8dcf8676304f09d12dc8d1ca6fbe8be55519f3502	2019	/Users/duhokim/HermesOps/reports/status-audio/20260811T161156-video-landed.txt
0f3af40e2ead56fdb707c18d133929ab67a2ee3fba1f571680ddaae58422d852	1425792	/Users/duhokim/HermesOps/reports/status-audio/20260811T171307-macbook-switch.mp3
c8c1436b44cfb53f048a897a0aeda12b7520f4f5cb0a54e6f931dd8e9cddd56d	1597	/Users/duhokim/HermesOps/reports/status-audio/20260811T171307-macbook-switch.txt
577a2348a61df41d50e9f918740e3a218310952213a56af76e1a2deeff54cfab	1993728	/Users/duhokim/HermesOps/reports/status-audio/20260811T171623-kun-video-pass.mp3
21fc34e0e92decfef3616bc360325f1aa3fe59ec6dfbdde96a1af6a4a59edfcc	2109	/Users/duhokim/HermesOps/reports/status-audio/20260811T171623-kun-video-pass.txt
69b0682b279a30cbe40a1e85226e3b83e2fe619d63dbe291067ef70fc02af6a6	1868928	/Users/duhokim/HermesOps/reports/status-audio/20260811T174003-parity-dispatch.mp3
4599c3b773e98757ae0b784807ac1be02ce776e4a5f34c4f77e57f4ce3fa0dbf	2172	/Users/duhokim/HermesOps/reports/status-audio/20260811T174003-parity-dispatch.txt
6307977cee8e1f9be7c5117601f48c44159cf1a078e6b7432774d0d17eb31377	2279424	/Users/duhokim/HermesOps/reports/status-audio/20260811T174641-parity-round2.mp3
754002d681649218f8ef6eaa38f4fd46e1d3965ac03e8b3d2cda342cf9509939	2404	/Users/duhokim/HermesOps/reports/status-audio/20260811T174641-parity-round2.txt
12ef3565b7f356bd5f96ffa1645e993db963a96ee61cb16537e73bb7ff2f2eec	2432256	/Users/duhokim/HermesOps/reports/status-audio/20260811T183858-kun-parity-clears.mp3
74465da0e717f5dc699a7be44f518c8bc6feb9a81563fd0cd863e8c92d835868	2505	/Users/duhokim/HermesOps/reports/status-audio/20260811T183858-kun-parity-clears.txt
4b968fe70e758fc97549cc8f90f06afda8fd6213339d32664edc9c99ca2642c2	2638464	/Users/duhokim/HermesOps/reports/status-audio/20260811T185741-parity-closed.mp3
35c60eb89d2b0b592d33fe81d88ac926ff36cf3de31ab5c77436255dc4b34512	2743	/Users/duhokim/HermesOps/reports/status-audio/20260811T185741-parity-closed.txt
ea08c717c7a612af486f6f45eb4c7983d4510d00e376a660af9c34e0c18ad170	1840128	/Users/duhokim/HermesOps/reports/status-audio/20260811T190519-video-cleared.mp3
0a271e62d73a36732a1dd351d8f47a1f8c78e597580bf6e158b44eae2bc8ca94	1939	/Users/duhokim/HermesOps/reports/status-audio/20260811T190519-video-cleared.txt
c9eec0b9d2d867b21231a03fd3965f96702623475084789e70804cf997869613	2208000	/Users/duhokim/HermesOps/reports/status-audio/20260811T191302-bhu-derivation.mp3
dc1a46362c300aa14662436e18acfb203e31c0b4b148345b1c92b8f3d8d3d346	2450	/Users/duhokim/HermesOps/reports/status-audio/20260811T191302-bhu-derivation.txt
eaed63a0dfc703058056bdc5f555969a1fd8efba6282ca814d66135dbea7e1a1	2238720	/Users/duhokim/HermesOps/reports/status-audio/20260811T192448-bhu-verdict.mp3
b6c7d86a232b94baa16f8ffa2a619b09f68ba11b3333495cd3a30ec3a867dc64	2384	/Users/duhokim/HermesOps/reports/status-audio/20260811T192448-bhu-verdict.txt
0b312ddfd7cb5ce9ab889350622f59919bb6f4d6d99ed1e509138ddffb058fdb	2172288	/Users/duhokim/HermesOps/reports/status-audio/20260811T193856-bhu-kun-gate.mp3
35fb99b817bbad7e9a44c196b05669fe9264fdbcbf65bcf885ab407f83997935	2315	/Users/duhokim/HermesOps/reports/status-audio/20260811T193856-bhu-kun-gate.txt
5b289ea3ed5ece4e3cb3631b46293154c28f356e944c30b8a52f684487486bf7	2183424	/Users/duhokim/HermesOps/reports/status-audio/20260811T194808-bhu-final.mp3
30e995841e0f9242e4a2f31fad518ad87817e75c3021a312c49c880c0770ae92	2279	/Users/duhokim/HermesOps/reports/status-audio/20260811T194808-bhu-final.txt
6dc6592c1632bf40885cd588bdec4ec332acecabe50ba66c7aadfb7a917fd51c	2387328	/Users/duhokim/HermesOps/reports/status-audio/20260811T195847-all-verdicts.mp3
475fd8f7bbc50c2d368936cfa59e71268750337947472182d2570c99c6f0c40c	2499	/Users/duhokim/HermesOps/reports/status-audio/20260811T195847-all-verdicts.txt
333336407735e7cf7b8b633959a52fee61043e72d6c15f132837fe275400e898	1752960	/Users/duhokim/HermesOps/reports/status-audio/20260811T201504-lana-repair.mp3
a03c128846fd8a469ad933528d82c74dab13a48d23fc3dfb540dfda4117e63f2	1957	/Users/duhokim/HermesOps/reports/status-audio/20260811T201504-lana-repair.txt
14dcce3a24453223d8bb97e35c4d425914d6dee7fd76227914f30d467ee5bd5a	1911168	/Users/duhokim/HermesOps/reports/status-audio/20260811T201833-gemini-dr-verdict.mp3
5c14fa6bc06c433d1bd61715e95b4f1502b3336562c9d44e4d0884440d6e650b	1974	/Users/duhokim/HermesOps/reports/status-audio/20260811T201833-gemini-dr-verdict.txt
23905d38f9bcf3de27056d9ae64551ca108c3655c27dad2dd7566fc33d0870a7	1841664	/Users/duhokim/HermesOps/reports/status-audio/20260811T202449-kun-final-pass.mp3
2c72ae0f7f7f02dcdea4703cd16b966f396f90ae3ce583ed0b99dea5758fcd35	1836	/Users/duhokim/HermesOps/reports/status-audio/20260811T202449-kun-final-pass.txt
aa3f4524d465ac4233bd33a5a94ecc2aa3736c2fabba920074cff410e2d34823	2512896	/Users/duhokim/HermesOps/reports/status-audio/20260811T203134-tori-fails-packet.mp3
f27f0557026a884c6578f2d141103880c2ebfa7c9b48c656f906d82a3e91359a	2526	/Users/duhokim/HermesOps/reports/status-audio/20260811T203134-tori-fails-packet.txt
d90dd1b3142243311b60e515671276811371d1b7f34e3161cce6c2e26a2775b8	1989120	/Users/duhokim/HermesOps/reports/status-audio/20260811T203901-rev3-landed.mp3
b9304c230fb772eff2fbc41096662167f6b9c9bb483e19d160b042a7b5c9c5b7	2004	/Users/duhokim/HermesOps/reports/status-audio/20260811T203901-rev3-landed.txt
3f47b9cd13772c83c149c6c8c32e935a7eafbc169b6ba97a84f10e4548e8ea0a	2288256	/Users/duhokim/HermesOps/reports/status-audio/20260811T211421-tori-fresh-verdict.mp3
976c4a990ebcd2912d208fb475f1adc8e8653216271be669faed7fba49d34ecd	2216	/Users/duhokim/HermesOps/reports/status-audio/20260811T211421-tori-fresh-verdict.txt
0c9602a42b6d98c2cafadfff94a0ef5a30f82078667c69e30218316e47488763	2022528	/Users/duhokim/HermesOps/reports/status-audio/20260811T212158-bhu-closed.mp3
f08caad29eff27955824e6d6f094f6dbd2f01ccbd8add379802829c7ca9c55cb	2057	/Users/duhokim/HermesOps/reports/status-audio/20260811T212158-bhu-closed.txt
b0f177e610ade16344039898dfab77a39b18da47312583a35a9da32e0bfa09ce	2101632	/Users/duhokim/HermesOps/reports/status-audio/20260811T212556-spin-was-right.mp3
dd0677bece29a7a1efdb256b51298d3571272dcf7ebc865e16a9997ee55509c3	2251	/Users/duhokim/HermesOps/reports/status-audio/20260811T212556-spin-was-right.txt
0feb2904f973dde77df7af6ca9bf3173b1728f1bcb88434002bec959e81141ee	2054400	/Users/duhokim/HermesOps/reports/status-audio/20260811T213051-spin-recap.mp3
958e6fc4af57db53a090a110bee0b53337824a15971ae28be72e129a28537e2c	2036	/Users/duhokim/HermesOps/reports/status-audio/20260811T213051-spin-recap.txt
fd5ccf01f0bf95072b16062cf80b5c3afc33e68627aa9bf7b8267836b60b25b9	2030592	/Users/duhokim/HermesOps/reports/status-audio/20260811T213656-cannot-use.mp3
419cacdaab88c73ec4034a19cf5f3f3f95f982a1c3f3a6efc584c99746082093	2135	/Users/duhokim/HermesOps/reports/status-audio/20260811T213656-cannot-use.txt
ada7d11030f8401f390f66b1fb19e854040cc26c8c8329d687fc3083619f76c5	2346624	/Users/duhokim/HermesOps/reports/status-audio/20260811T215531-spin-split.mp3
12a695ed9c37746c34b4136e10341f90fd145f733c78567938b38bf1d0260527	2481	/Users/duhokim/HermesOps/reports/status-audio/20260811T215531-spin-split.txt
aace8c32d42d1b10c92d46ad6f0bcb56fd498b1bac0263c6938779b4be444ea0	2313645	/Users/duhokim/HermesOps/reports/status-audio/20260811T225150-spin-priorart.mp3
3bf5439aed9c67611b8147415056fa64639b09d61dd26ee51e3451d853ca4e73	2258	/Users/duhokim/HermesOps/reports/status-audio/20260811T225150-spin-priorart.txt
2571997a49343c4e0137cc3cc928abc1a124648f2b48440bfd91f60825969299	3024429	/Users/duhokim/HermesOps/reports/status-audio/20260811T234955-spin-converge.mp3
a5e5101184a5f61bd984a1390d5ee2b122214d05aaa3977675e5ccde5c7ba7f4	2950	/Users/duhokim/HermesOps/reports/status-audio/20260811T234955-spin-converge.txt
b17d86f3e92f7efd161edd5c135b09569e6bfd9bfbd0ff442c494100fbcbee6b	2118189	/Users/duhokim/HermesOps/reports/status-audio/20260812T001659-overnight-plan.mp3
5f1c65c71c526769e3e23a89610d54d1243d8ff15505a44be02defa3a01a70b3	2225	/Users/duhokim/HermesOps/reports/status-audio/20260812T001659-overnight-plan.txt
781ec346ef745d0b6501d49e9247efca1e89172c393298dc17426c0c01706a3f	3032109	/Users/duhokim/HermesOps/reports/status-audio/20260812T004123-overnight-converged.mp3
13de2dd38d90dea4ce5f7a4e7d7d9a0d7b9d209158000eff99c108f0d00dad5b	2873	/Users/duhokim/HermesOps/reports/status-audio/20260812T004123-overnight-converged.txt
114d95e9074fcfd3156e2c17cd2288b9504fc2e524aa515cebc8090df187b6fb	2204589	/Users/duhokim/HermesOps/reports/status-audio/20260812T010026-tori-tightening.mp3
c53c9c742a0aca74f17e673e52dfc16555d1b053571990a1bcabdfe997b5e564	2223	/Users/duhokim/HermesOps/reports/status-audio/20260812T010026-tori-tightening.txt
7ca149f28c9c3137adf91bb0d70925ea71b07d8a3709cd4d4c93dc5c07d4f0ce	3349677	/Users/duhokim/HermesOps/reports/status-audio/20260812T074333-morning-spin.mp3
573d5927305645c97c413cf876539344a6de31cc3e9870d15bdf8afb271a4cba	3081	/Users/duhokim/HermesOps/reports/status-audio/20260812T074333-morning-spin.txt
717a518f913e863587c48bfc61c196fb8f0063099e753db0bb6bf95652015b8f	1562925	/Users/duhokim/HermesOps/reports/status-audio/20260812T112109-spike-watching.mp3
97b9da70ec6644cd22e935a8a71cfb9a2bbaa4d66ac2f1ae7ecdef16aa3f3198	1616	/Users/duhokim/HermesOps/reports/status-audio/20260812T112109-spike-watching.txt
50847d591d8ff4e6f124cdf07033ddfb9d82452e59fa2679aabe39f3ef7a98dc	3518637	/Users/duhokim/HermesOps/reports/status-audio/20260812T112909-spike-two.mp3
53b8ea0b35f8f35c237666955da4807ee5f525c289f92829fcd3bbc09d4a1640	3252	/Users/duhokim/HermesOps/reports/status-audio/20260812T112909-spike-two.txt
90efd606bc29db375ec4d81efb1cd9ed1db15326deea626c4016eebbdbd05718	2828205	/Users/duhokim/HermesOps/reports/status-audio/20260812T114240-tori-audit.mp3
062688f3329ed11499d2a832f7cd71702031f399bb151a3cf1c3046b823d0272	2694	/Users/duhokim/HermesOps/reports/status-audio/20260812T114240-tori-audit.txt
4b796a1d9e3b2856824ee59f49e48ce603586cbe8016540863a9a4d0ded773ab	1816749	/Users/duhokim/HermesOps/reports/status-audio/20260812T114648-kun-gating.mp3
e9e6d90366c3e572ca430ac1888c5a7be71e512568a794f0ddb7346211596d89	1920	/Users/duhokim/HermesOps/reports/status-audio/20260812T114648-kun-gating.txt
8e9eeaed566f9eeda938ba78c092ee099e36da02112f41ae61071f41b9efc006	3022509	/Users/duhokim/HermesOps/reports/status-audio/20260812T115101-kun-spike-gate.mp3
329e08e4e5dc8510d3a618d6d82bae16f2d97c318b9d109126fad5c17c59e4a1	2889	/Users/duhokim/HermesOps/reports/status-audio/20260812T115101-kun-spike-gate.txt
4078a3b661ba01c340aecf08a81061088f57d55ef7b6d34c2ece453342d813e0	1726893	/Users/duhokim/HermesOps/reports/status-audio/20260812T115434-sample-question.mp3
dee35bd2a1ec33822d78bbbad3aad10fef342996b7919a56c713de3867f10c03	1757	/Users/duhokim/HermesOps/reports/status-audio/20260812T115434-sample-question.txt
058bfb9845f5c44e32d1316d8c9bf98a4ddfca5652fc4eafadd9a68dc1486ffd	2346669	/Users/duhokim/HermesOps/reports/status-audio/20260812T115850-sample-verdict.mp3
ffe00bb40fc4f7cda5c20c18b239fc18e38e02966a2bec018506d4c98c9632dd	2268	/Users/duhokim/HermesOps/reports/status-audio/20260812T115850-sample-verdict.txt
6fad79d11b8c03d562f410d44cd1de4544325dfd793d88f651ce086b02d7bb45	1983021	/Users/duhokim/HermesOps/reports/status-audio/20260812T120205-narrowed.mp3
1c0d366cbd748b94f2a6da504c8c9d5dcaa775c959ea6864058389b417b0ebfd	1956	/Users/duhokim/HermesOps/reports/status-audio/20260812T120205-narrowed.txt
8913f704ee085c4d8958deeb09680169718f97c80c31dd21fe7befbdaad978ad	2629677	/Users/duhokim/HermesOps/reports/status-audio/20260812T120646-lana-v2.mp3
1ace808d1e55cb2485a7fdc7c93063b1e5fb44acfc0d6a03017028b2180823ec	2492	/Users/duhokim/HermesOps/reports/status-audio/20260812T120646-lana-v2.txt
7f3726ebb1cfad4d980895c7c282e0ab55129a81706202c4ad7acaa134a41a3f	2207661	/Users/duhokim/HermesOps/reports/status-audio/20260812T121038-autonomous-set.mp3
d16c9c751eea3d74098950271feee968198c69b92c9ac9b15b43131472ac4ace	2270	/Users/duhokim/HermesOps/reports/status-audio/20260812T121038-autonomous-set.txt
6c09f546e30ef323e50f4936a988722a210208a3e18d23810259ab724f8e51ed	2518701	/Users/duhokim/HermesOps/reports/status-audio/20260812T135625-retention.mp3
0fb055971b04537f7a27bd8648e4e964b147fb184f0d19d698ac0d00e3a8d77a	2233	/Users/duhokim/HermesOps/reports/status-audio/20260812T135625-retention.txt
5dc7030dfda91dc67866b9953fea69682338ce4d020be6068028535277444b3d	2987181	/Users/duhokim/HermesOps/reports/status-audio/20260812T140731-closing.mp3
fbc4283e7dab4515c5a8cd38001071ba925defc70fd702fc20252379d45e308f	2704	/Users/duhokim/HermesOps/reports/status-audio/20260812T140731-closing.txt
9e6a238b86fc32af9fce1da385490d92929942e84ec647c243e2444d9ebbb7a0	1979949	/Users/duhokim/HermesOps/reports/status-audio/20260812T141231-rowcount.mp3
d0822840d31a22426fb331e8d05f929dbeac3a66b0b902ecee052dc733460bfe	2131	/Users/duhokim/HermesOps/reports/status-audio/20260812T141231-rowcount.txt
932256fb1d5304394fcc3a6257566bd28d067fcd96b44d0e25c82137258c5490	1819053	/Users/duhokim/HermesOps/reports/status-audio/20260812T141713-catalog-note.mp3
957f999a4200f75c27440922d2e8eb311f20362690bb51bce674f84befa66882	1818	/Users/duhokim/HermesOps/reports/status-audio/20260812T141713-catalog-note.txt
26a9b6338faac2ef1171497f1a21bcfc54c688fb6a457233bbeb0aaa673c362e	1921197	/Users/duhokim/HermesOps/reports/status-audio/20260812T144138-query-running.mp3
75649a0ded6f1ab7ba824de29160ae9c5274174ccd65d9ea34dc5880e04ad055	2035	/Users/duhokim/HermesOps/reports/status-audio/20260812T144138-query-running.txt
a6465b20980a6f24c1d46a5a0e5cfa419736cf4fee50c66e6222ad96418afca1	1491885	/Users/duhokim/HermesOps/reports/status-audio/20260812T144945-plain.mp3
6e544e4e7ef6d82600b7c395e8d1b23f101decf7215756639a0754a53ed1998d	1665	/Users/duhokim/HermesOps/reports/status-audio/20260812T144945-plain.txt
99fe518bbdcf4173fc068603d4b14821af1f2a369acd99b7f4d96a2982f8cf5e	2012589	/Users/duhokim/HermesOps/reports/status-audio/20260812T145433-cockpit.mp3
ff21a325528df9d4a90a3bed60131846340664581415bf448e98fcc849f65db0	2182	/Users/duhokim/HermesOps/reports/status-audio/20260812T145433-cockpit.txt
24260dc74a40bc67f0c8262753aef492c6f425768cbb41a1bff5918211e7c10b	2375085	/Users/duhokim/HermesOps/reports/status-audio/20260812T150331-bias.mp3
98c6113043d924189ade84649137bb73bf031bf106d5c08487050a26d3c8b8f8	2566	/Users/duhokim/HermesOps/reports/status-audio/20260812T150331-bias.txt
74faf01f599ed4e0b27fe0a9af530c98cc1e853b43bbdbcb478404b56176b0f6	1631661	/Users/duhokim/HermesOps/reports/status-audio/20260812T151005-filament.mp3
3c3afd1b3aaa0054c618df10f5d861284e55af7864a19db03848a281e2c9c6ce	1801	/Users/duhokim/HermesOps/reports/status-audio/20260812T151005-filament.txt
0057712d75f278d1e516f08a4c4624d9d67c34fb04433215c7272ae55f30b20a	2054829	/Users/duhokim/HermesOps/reports/status-audio/20260812T152107-paper.mp3
e4ec5ad41261d1546eabceedc56a4cfe1e9a96af0be09a082a76c0a1246e590d	2259	/Users/duhokim/HermesOps/reports/status-audio/20260812T152107-paper.txt
3df7ab8b232e4b202b44b3bcbdc7e695963e23b55ea8073e62a461baf96e1b49	1724589	/Users/duhokim/HermesOps/reports/status-audio/20260812T152243-record.mp3
dbc9eaca31211cf0b7b6b473c6114979c55dd8bd73e3e97e3f03fa470f192cc6	1804	/Users/duhokim/HermesOps/reports/status-audio/20260812T152243-record.txt
6cebe20eb15cda12365e2c51f760e43ea6e09e95126e44dacfd0493243040958	2161197	/Users/duhokim/HermesOps/reports/status-audio/20260812T155309-record-read.mp3
0f58042c727e43b896eb9d4d186199a10e9bec68dce6f7e7fa341061f5b411bd	2290	/Users/duhokim/HermesOps/reports/status-audio/20260812T155309-record-read.txt
2dde4233d5a6cc5b956a0f5fe5e047964b952b252ae68a4097834e4379282be4	1864365	/Users/duhokim/HermesOps/reports/status-audio/20260812T161051-kungate-record.mp3
8f2c4d729b379d143b3ae35eab6bf620045727e2cf83635cebae6e00a0561eb5	1978	/Users/duhokim/HermesOps/reports/status-audio/20260812T161051-kungate-record.txt
a72bcd011a7a0291a7deaa624596e516398eb10e81da8ea106d26ed0439fd890	1704621	/Users/duhokim/HermesOps/reports/status-audio/20260812T165105-record-done.mp3
40371821f97a8d08ef4f2c49813553afb0e2a5f7d5cc1d95ee0cd5bc2e5ba7f6	1916	/Users/duhokim/HermesOps/reports/status-audio/20260812T165105-record-done.txt
d9975987faae6bb16baa148d3d3cf7c1a9741cb8c2188002664fa67e7001ed5c	1869357	/Users/duhokim/HermesOps/reports/status-audio/20260812T165609-precomputed.mp3
22a9464a2e1a43bf85e4303493703023c4e887c834685674e446c2970b093a62	2049	/Users/duhokim/HermesOps/reports/status-audio/20260812T165609-precomputed.txt
df03e65ba2a09754de507e1d3211ce4442fc2e413e8e9f155cbb68684bcf5f38	1693485	/Users/duhokim/HermesOps/reports/status-audio/20260812T170803-decision.mp3
9b5283c5c195a16d5c7f4f6eaf29764b537ff412f66ff97b2607b780da2312b3	1762	/Users/duhokim/HermesOps/reports/status-audio/20260812T170803-decision.txt
9083e78b144ffc0454a6e16c043b51b45d7e0ca2c80ff0102b42dc9957b1cc20	2044461	/Users/duhokim/HermesOps/reports/status-audio/20260812T171221-shesolved.mp3
1312c10095eb6bcfa093ab4a8044b5ed332b7e6901a54ce217912ebaf9d3f4f0	2088	/Users/duhokim/HermesOps/reports/status-audio/20260812T171221-shesolved.txt
ce3afe1e48ce4ee918026b67f87c59bafa59ac3e680d34b5bfe17ef73768e4d9	1627053	/Users/duhokim/HermesOps/reports/status-audio/20260812T173503-studio.mp3
e0b384495bb62faff02180ed219eef43c37a7b254c53d04d21fddc5889e625fe	1789	/Users/duhokim/HermesOps/reports/status-audio/20260812T173503-studio.txt
ae2275977355a4fbf124e18c4651ec2fbc34f35ace1b81306803b15bff1b5fea	1799085	/Users/duhokim/HermesOps/reports/status-audio/20260812T174353-runs.mp3
660bcfc31afe3341e72b0c0a68c70372a8a80ec9d41e65a153938823eaf8c673	1945	/Users/duhokim/HermesOps/reports/status-audio/20260812T174353-runs.txt
34397e2e3ac0235bf3c5a113e34a2695a3cef8574fcf924c970ac8d01e7c8189	1864365	/Users/duhokim/HermesOps/reports/status-audio/20260812T181515-problem.mp3
3d85fd41aa37cf7f2034a2154408955d8879aa2cb20410614c2e6cc86802cf70	1968	/Users/duhokim/HermesOps/reports/status-audio/20260812T181515-problem.txt
cd31890ee206bbc62ff0b3a634a80a870d7f36f2953a453dc2c131804fe437f3	1012653	/Users/duhokim/HermesOps/reports/status-audio/20260812T182856-partitions.mp3
8bf842ea07e75b122f3e1cb30d2f8a9eab60c81cf983e754d39a5b4727d0f495	979	/Users/duhokim/HermesOps/reports/status-audio/20260812T182856-partitions.txt
97e7e377a9b93d4d96494666b60d0a557b76115ec5b1d6ce089e5cd19cfba95c	992685	/Users/duhokim/HermesOps/reports/status-audio/20260812T183222-count.mp3
be7c0deeb0d33e704c6872cb65d7ca156f4ea341a187404ddcd610cbf1b39b01	913	/Users/duhokim/HermesOps/reports/status-audio/20260812T183222-count.txt
1cce6a4989cc7f3133455e4cc5608dee313aa6dd03df0054553e2844bf3dde2d	1181229	/Users/duhokim/HermesOps/reports/status-audio/20260812T183635-keyspace.mp3
466d4601c17fe6f52d4974bf28e87e541a1285989525f10a8764f4938a9128aa	1163	/Users/duhokim/HermesOps/reports/status-audio/20260812T183635-keyspace.txt
24712530599084d0ac437f771a2c296c0bf4147a7d15b535ea0c40be2dcb399a	1114029	/Users/duhokim/HermesOps/reports/status-audio/20260812T185232-detached.mp3
2e71fae546f985e78eb3befd5ecc5ef482ff5e300831a0d89e1a9251273ca608	1108	/Users/duhokim/HermesOps/reports/status-audio/20260812T185232-detached.txt
6f050db33e9ead6feb9e1c20199010ee3d08bd106d138e2913db80171a720f4f	1052589	/Users/duhokim/HermesOps/reports/status-audio/20260812T194400-route.mp3
c5e5a3bc27dbf265cb536ac777a4f542da39b54b6dd59dce401c12699d8b5b31	972	/Users/duhokim/HermesOps/reports/status-audio/20260812T194400-route.txt
8701e5c48e0d56465d73811d3b873712fd1c3e28710204af97c4017a70084f1c	970029	/Users/duhokim/HermesOps/reports/status-audio/20260812T195246-crossed.mp3
3f66cac7df8b43897b5d18d87c59f3b65cf0d20b34267451ea0679cf22694141	836	/Users/duhokim/HermesOps/reports/status-audio/20260812T195246-crossed.txt
0dab880b863b6b052117bb5be4203517aaf4c5e211393b58dd165ed64e5c1f2f	1261485	/Users/duhokim/HermesOps/reports/status-audio/20260812T200801-lana.mp3
c3554b617fb8592b13ad196aaf69c5fecbd9b621f4fc52809601001d43ef3bdb	1245	/Users/duhokim/HermesOps/reports/status-audio/20260812T200801-lana.txt
f4a8b7ee05f9c5f4cc858045e342ac887c179d8cc276c38fda07f46a81b5d6dc	1290285	/Users/duhokim/HermesOps/reports/status-audio/20260812T203221-alarm.mp3
00f3d0f19f1e71cdb5acff3ecfe0ec7c3915d683f723c5bde5ab4969e0480626	1270	/Users/duhokim/HermesOps/reports/status-audio/20260812T203221-alarm.txt
1123d456e8b9f3e203cdf1ccf59616e4903efaeec422874446e8a3bbdbf53b0d	1432365	/Users/duhokim/HermesOps/reports/status-audio/20260812T221347-spiral.mp3
5fe2bc9fb1e726f64c082bf00bcfccbfe47e7ab5092b2207cd438b7ac954b9c5	1406	/Users/duhokim/HermesOps/reports/status-audio/20260812T221347-spiral.txt
bacaa3ef9d21fa49a2f0bd0310b4439c04ff110733a1ed432bb21de3a96ef9ec	1387053	/Users/duhokim/HermesOps/reports/status-audio/20260812T223256-goru.mp3
8e44d61d3f80bcd1905ddf8293a3867fb84e81c53fa7a8427974ed102a7ccbf6	1457	/Users/duhokim/HermesOps/reports/status-audio/20260812T223256-goru.txt
d668041c64780bde058014312272fca513c5e584c66f5b51c28032760f3b65ff	1293357	/Users/duhokim/HermesOps/reports/status-audio/20260812T223630-decomp.mp3
c891e7aff189323c02f04d1ac45c5b240da5ebb487d312ee9388a8021974a2e2	1308	/Users/duhokim/HermesOps/reports/status-audio/20260812T223630-decomp.txt
526519aeafddf7e1e77478c61451a0512ed91126d71380e8784932f214337120	1339053	/Users/duhokim/HermesOps/reports/status-audio/20260812T224153-kun.mp3
cb70e1075896132bd5d8cc1444ef7d5ebb6d15a7bf784edf1ba0bcc8699ea7e9	1243	/Users/duhokim/HermesOps/reports/status-audio/20260812T224153-kun.txt
4ccf2c16e07b75bd8b4095b256a6f41d43686611c331955ec7dd9403bcec553a	1489965	/Users/duhokim/HermesOps/reports/status-audio/20260812T224740-regate.mp3
7e12e63db1bafdc2779fdb767280fced11bfd9859e497d7824483f6a222e46e4	1489	/Users/duhokim/HermesOps/reports/status-audio/20260812T224740-regate.txt
3d5b0f5f1dcc13b942d8daaee24002bc87ccb336c92510dbdcc0f2a83e179e6b	1372461	/Users/duhokim/HermesOps/reports/status-audio/20260812T225235-closing.mp3
b05c606d42a6398e0d2c283fb76d04bc4ade79a9b376f14c72b55b636334ef42	1190	/Users/duhokim/HermesOps/reports/status-audio/20260812T225235-closing.txt
527f3538f0d10b2a379ef13cbba10ec49d7582c301d1d0252e3942113b460865	1034157	/Users/duhokim/HermesOps/reports/status-audio/20260813T103831-morning.mp3
be7bb099516b4542478819ad219d1c9d79ad42688d5173c388cf7149e37c7a79	1069	/Users/duhokim/HermesOps/reports/status-audio/20260813T103831-morning.txt
9badb8331b69b09c618399c680defd5b4c1b6509a6c5d9fff57a68a0abd6b36d	1203117	/Users/duhokim/HermesOps/reports/status-audio/20260813T110404-spec.mp3
e962918252ea1575eb115d1baad05038a2e73d02c254865c50c5ea87319317f0	1202	/Users/duhokim/HermesOps/reports/status-audio/20260813T110404-spec.txt
8c3897caa231641f7f41a95066340d9075edacae709cebf9526e007a32e99276	1219629	/Users/duhokim/HermesOps/reports/status-audio/20260813T111025-closed.mp3
87c59e28e0960c88e0791f3dba004bcc7d8043229ac382449cb331487e05cb59	1115	/Users/duhokim/HermesOps/reports/status-audio/20260813T111025-closed.txt
a73d1506a6899e040b84621f9584c02cbba1ccb46723100ec89be987a0c8be2d	1220397	/Users/duhokim/HermesOps/reports/status-audio/20260813T132254-v8.mp3
66d560dad7f652dcf553b6b3d646fe7ca1efd2b75e332311b730ee41a312295a	1231	/Users/duhokim/HermesOps/reports/status-audio/20260813T132254-v8.txt
a8bb66dc9d978dff2a4c26db7b5a34c08149e2c5fa06cd9c398ad4d09b1a9f54	1579053	/Users/duhokim/HermesOps/reports/status-audio/20260813T165241-redesign.mp3
651a14fc3796d6ed8b931f409d1bcc486b09c34e0f72d8dc849930a01238d7fb	1555	/Users/duhokim/HermesOps/reports/status-audio/20260813T165241-redesign.txt
46a2967f6ccc39628998c457a49748408a593ce310c18bfa3b70bc60fdf014e8	1382061	/Users/duhokim/HermesOps/reports/status-audio/20260813T182337-catchup2.mp3
9ec731e7a2158fd0a2e79d0067c9dce16f1943dc720133a8a7ccdcabe0e494c0	1364	/Users/duhokim/HermesOps/reports/status-audio/20260813T182337-catchup2.txt
a3a1c1b49b4989db436f03b3714d184ef859588c7af1631cc8eec5237247c48f	1360557	/Users/duhokim/HermesOps/reports/status-audio/20260814T075417-morning2.mp3
7b0dcf22da9c7d89168abb9152d925184209d45c501393ee0b553d4f87c872c4	1368	/Users/duhokim/HermesOps/reports/status-audio/20260814T075417-morning2.txt
a3a1c1b49b4989db436f03b3714d184ef859588c7af1631cc8eec5237247c48f	1360557	/Users/duhokim/HermesOps/reports/status-audio/20260814T105843-morning2.mp3
7b0dcf22da9c7d89168abb9152d925184209d45c501393ee0b553d4f87c872c4	1368	/Users/duhokim/HermesOps/reports/status-audio/20260814T105843-morning2.txt
192a07190de06ae23ba70193d5837ecf0b0ceb93d306cb344e3f1de695882c18	1600557	/Users/duhokim/HermesOps/reports/status-audio/20260814T112333-postmortem.mp3
d7d0d5d77acbe8d56a550a8a6a4efba5b9fbf586a362afcb8b681a9188de6ce8	1604	/Users/duhokim/HermesOps/reports/status-audio/20260814T112333-postmortem.txt
b17af15578503cedb8d32f50855b9014f440a11dfcadead8a200ba441f28664d	923565	/Users/duhokim/HermesOps/reports/status-audio/20260814T134810-check.mp3
805c14112ecf425c8388004b2b0ee62ed5df9d2588495faf1c20b090745ab514	993	/Users/duhokim/HermesOps/reports/status-audio/20260814T134810-check.txt
f46f64da997327e7093c2e9f6a4cca01ed2c9ff6e034230dc600d274b2e57ece	1609389	/Users/duhokim/HermesOps/reports/status-audio/20260814T145947-audit.mp3
cca651124ce981809b2a79a37e96b09d000d44c0a0c20dfbe5973e7ab5291a1b	1765	/Users/duhokim/HermesOps/reports/status-audio/20260814T145947-audit.txt
59ba0fbf18143d86d83ca093d4e78db2ef239f07cc8da14ebfead3fd5cbdf5f3	1266861	/Users/duhokim/HermesOps/reports/status-audio/20260814T150154-route2.mp3
49a72396ae8e7f5d5a29c58dc5633b94a3c4ca37e36890f872100f1b4573f58d	1299	/Users/duhokim/HermesOps/reports/status-audio/20260814T150154-route2.txt
2f252b25d02cb8763c4a596176d67391bbbeea19331297577576ad995e6d3575	1479597	/Users/duhokim/HermesOps/reports/status-audio/20260814T152338-dash.mp3
cfabc69fc1cff6d048869683df4ec7eb4dd42e4c8c99375da7be9b0e209339be	1492	/Users/duhokim/HermesOps/reports/status-audio/20260814T152338-dash.txt
78471d4147bce699f29fa0343220068656d2847f8e718a5b175c3b111e286c02	682368	/Users/duhokim/HermesOps/reports/status-audio/20260814T160157-variance-pass.mp3
fa46299e4a502ac08f9d9ed4c89a653988e031be53973db6ba832ec6726fcfe2	648	/Users/duhokim/HermesOps/reports/status-audio/20260814T160157-variance-pass.txt
bcd4a5ce85dba9e53f75d2443dc5c4c4eee19ee42c1d1bc2c59b98cbbb2bfdff	664	/Users/duhokim/HermesOps/reports/status-audio/20260814T160157-variance-pass.txt.corrupt-20260821
805fbf3473b1b38e5a97d670e1d0fda74b17d58f6ae13861b8a15af3eceeb6ea	653568	/Users/duhokim/HermesOps/reports/status-audio/20260814T160933-kun-regate.mp3
424ac1658b590fec42a3cb7f4dd6cd3fac2fb6164ce6bbfb46f1d93d6920aaef	637	/Users/duhokim/HermesOps/reports/status-audio/20260814T160933-kun-regate.txt
22dd2e57d91a9d4dddf73679e471e39e1c183aadc78ecc703d4723853999077e	654	/Users/duhokim/HermesOps/reports/status-audio/20260814T160933-kun-regate.txt.corrupt-20260821
3913befc8faf7c4fbcbf4add6d7c3c4c263aad4bdbb58899a4b97faca614eafb	734592	/Users/duhokim/HermesOps/reports/status-audio/20260814T161526-ten-blockers.mp3
d8feafae500939283af646440e7d22f05634fc4d7a058eba69be8594c0944e45	659	/Users/duhokim/HermesOps/reports/status-audio/20260814T161526-ten-blockers.txt
1a54125b170dfe011f725dbd8dbb34a7f35a81b7d139fdd3f4fd05fe2a22f2b2	666	/Users/duhokim/HermesOps/reports/status-audio/20260814T161526-ten-blockers.txt.corrupt-20260821
a09d314e2b0a5c2d0f502be4625f0d48122cb66c828bab83edb1549f69469739	792960	/Users/duhokim/HermesOps/reports/status-audio/20260814T162102-both-pass.mp3
9e4e3af2026201805a4c85fd33cec6009ce99e6509ead2d298b43270112aec35	674	/Users/duhokim/HermesOps/reports/status-audio/20260814T162102-both-pass.txt
cc6f122ae1428096650aa6ca298cba3a31cd0658eb04307e93c602a45e9d932f	702	/Users/duhokim/HermesOps/reports/status-audio/20260814T162102-both-pass.txt.corrupt-20260821
033694a32cdfd74ff2ad9a92dd85ca29f4b2862fb5781235ea0d3de97526ec8d	764160	/Users/duhokim/HermesOps/reports/status-audio/20260814T162331-sign-dictionary.mp3
ec9c1da2c08c4d42516c8924480723a32bc5da6b466ddb968cb88169b2c48c2b	686	/Users/duhokim/HermesOps/reports/status-audio/20260814T162331-sign-dictionary.txt
1af45e41cfcaf77849ec5ac33701616729720ae19c75aa8460cd0c94084783d2	709	/Users/duhokim/HermesOps/reports/status-audio/20260814T162331-sign-dictionary.txt.corrupt-20260821
8f37f64d74c705ec9c0f626bfe6a15f49a7aefe2c15baf79159f52b9e76be2b3	640896	/Users/duhokim/HermesOps/reports/status-audio/20260814T162945-identity-1000.mp3
bb20845e3059ce9ae8c980e7cd9f161b90ad10cb4a6b80e7bcf7e123c9f39570	642	/Users/duhokim/HermesOps/reports/status-audio/20260814T162945-identity-1000.txt
d9c2ddfb9c3e726110cf9ce18399ab0f04c56b083fceb9c54232c969553d21f0	2283264	/Users/duhokim/HermesOps/reports/status-audio/20260814T163726-session-summary.mp3
a10c5d141ea9129fab116eecdda02a1c86433631f9fb787e56bdc5198f497ea7	2501	/Users/duhokim/HermesOps/reports/status-audio/20260814T163726-session-summary.txt
1b886683b0d0adfabe877d346b0ce4faa97f8cfc13a696cdc05b708977a79e84	2517	/Users/duhokim/HermesOps/reports/status-audio/20260814T163726-session-summary.txt.corrupt-20260821
44d847ad563516e3fb3cf1822ae3b6bfd02723c4f72f7539c5983133b9caee2c	297600	/Users/duhokim/HermesOps/reports/status-audio/20260814T164714-afplay-off.mp3
ea48b5141d53288a10271a1c461c6fae3278fa01522d6c612f5d1c7d5f876650	281	/Users/duhokim/HermesOps/reports/status-audio/20260814T164714-afplay-off.txt
60873538724f859ff3f57e326c97337580a2e8b9ad56a98b0c3a5c14bda51e64	705792	/Users/duhokim/HermesOps/reports/status-audio/20260814T165510-cursor-measured.mp3
6318fdb8f710487953fc012b1ef1af201a4b0f901f89b98a850dfacc257ecc11	763	/Users/duhokim/HermesOps/reports/status-audio/20260814T165510-cursor-measured.txt
91cff0156acd518414466f21ca9086353e794fd1fcd062227cd72d4db9ab0ef0	815232	/Users/duhokim/HermesOps/reports/status-audio/20260814T165738-licence-fail.mp3
2e34afd3590d7a68a8ff1d3bb521a570cded1335355920ec87394d9700136cd0	808	/Users/duhokim/HermesOps/reports/status-audio/20260814T165738-licence-fail.txt
619784d72c528526b1c190611fdac54a1635b818ad6b70eb7de48cac0e41bd08	772224	/Users/duhokim/HermesOps/reports/status-audio/20260814T170051-ten-filled.mp3
953b29854ad61c66ef44b4abbc7c95515f899996c4b20ae35ccf4107199fd222	759	/Users/duhokim/HermesOps/reports/status-audio/20260814T170051-ten-filled.txt
fb5cc19bdfb7bafe6b84b0add587ac54add5c8021b2f5905ae84612c36904de7	883200	/Users/duhokim/HermesOps/reports/status-audio/20260814T170345-final-gate.mp3
c464879bb37bc327e979266ec711e01c308661a731ba03d77e2ad37a7d738092	874	/Users/duhokim/HermesOps/reports/status-audio/20260814T170345-final-gate.txt
0b02d353cd74aef3e59563722cde692d0d28aaa8a53d035e83b4bda1aa187ef7	880	/Users/duhokim/HermesOps/reports/status-audio/20260814T170345-final-gate.txt.corrupt-20260821
412f71b9c51937382c745ae7d92af039597478c53ede500c02ecbd8404ca51a1	847488	/Users/duhokim/HermesOps/reports/status-audio/20260814T171252-digits.mp3
2af0c54397dd59ba2af105a097d32e205dbe76dc8b0b7c4fa5f4838e0f9ceb68	768	/Users/duhokim/HermesOps/reports/status-audio/20260814T171252-digits.txt
de836c1dc8e948f609bcba84a1be877fb85df75298c814040ad2b80beb8002bb	941568	/Users/duhokim/HermesOps/reports/status-audio/20260814T171528-redesign.mp3
0ec1823c1e66eb360d731711d68736b0753daf82d8b2be18b128bd6a398c9f5b	865	/Users/duhokim/HermesOps/reports/status-audio/20260814T171528-redesign.txt
1384e049718bdde7802038d9ee8d17291369877181c667f724286c9c8b1df820	907392	/Users/duhokim/HermesOps/reports/status-audio/20260814T173158-tori-clearance.mp3
a6f4a06d294c943f2c8ab97793772ea9ab8cd6f887b6eb30e526baf0e1c33a7d	983	/Users/duhokim/HermesOps/reports/status-audio/20260814T173158-tori-clearance.txt
c8f563c1679ad95ef116b6d0d0b2599ff8aa91013830bc325e4d6e3ebdd9cead	1006464	/Users/duhokim/HermesOps/reports/status-audio/20260814T174027-regate.mp3
a888e81b883bbeaeb612f21a2a059d06e59da4c238da6f31f666dc4b3a73c324	976	/Users/duhokim/HermesOps/reports/status-audio/20260814T174027-regate.txt
d8221263dd4eff861eb8e8b99354a255446c7449d732892fa04d5df175b1ed32	892032	/Users/duhokim/HermesOps/reports/status-audio/20260814T175348-candidate.mp3
9c8eabb0d875218926418ebe1557287d0bc3a06403dc2fb91818ac9c97273530	972	/Users/duhokim/HermesOps/reports/status-audio/20260814T175348-candidate.txt
b8a32d2871466d0a7cb23527984170ce5d9159e2c0ab06044f338f142aac9213	994560	/Users/duhokim/HermesOps/reports/status-audio/20260814T181008-linter.mp3
ca3ea3ea6e4a3a8897b0d9295bb387056baa3ecef2845716ee5af6774d393391	998	/Users/duhokim/HermesOps/reports/status-audio/20260814T181008-linter.txt
9743fe9e06ebca8538936dbb7e670106b0723c164085e740f41cbc46a2d60cc5	1026432	/Users/duhokim/HermesOps/reports/status-audio/20260814T183728-limits.mp3
65e72833d4643c05446010e3774e3b3c08cd55c322f198e8c5a6930446e86199	1091	/Users/duhokim/HermesOps/reports/status-audio/20260814T183728-limits.txt
ed97a7fd178d17bb7b68a8ec7a832f429898397ed5ba87cc644f0395b5fffe74	970368	/Users/duhokim/HermesOps/reports/status-audio/20260814T192429-final-pass.mp3
963573b0f9e5c7f194ca04d0c6e775a02c24d6c28ebb5f49766242ffc970edb1	972	/Users/duhokim/HermesOps/reports/status-audio/20260814T192429-final-pass.txt
16954874f957f8623d52579b702fd7ceb8e562213b893818c920be932a98fc53	994560	/Users/duhokim/HermesOps/reports/status-audio/20260814T231824-night-plan.mp3
54502644855c96cd381bd8856539a4b7ee4b6f16993621d22291fdacb1d910f2	1023	/Users/duhokim/HermesOps/reports/status-audio/20260814T231824-night-plan.txt
252af4ffdcd75805daaf87ce619ed6960bfcac5fe2d116d62476dd67422d0720	1625856	/Users/duhokim/HermesOps/reports/status-audio/20260814T232238-handcheck-why.mp3
9f5f9aa9d3868983a5dd788d919e412766a2f9909e19fd34450e60ee18c0aba4	1715	/Users/duhokim/HermesOps/reports/status-audio/20260814T232238-handcheck-why.txt
d44684dcd7146ffafcd512a2eec45c092e1371c09bdfa855e1a526e34c97ab56	1524864	/Users/duhokim/HermesOps/reports/status-audio/20260814T232757-one-human.mp3
b049fc23447dd4aba61c0a1812635f3810bd7ed61d853ad54d38b35590d6c16b	1654	/Users/duhokim/HermesOps/reports/status-audio/20260814T232757-one-human.txt
ef86d17c6cf48fd0f7db97ff47273877372fb50dfe06adfafff55aa03ef4821f	624000	/Users/duhokim/HermesOps/reports/status-audio/20260816T011100-cast.mp3
dcc9ff4809634755f27b0f3ea485dfcdacf4a404c4a478275a89e0c900f7c186	685	/Users/duhokim/HermesOps/reports/status-audio/20260816T011100-cast.txt
2b9a7e84ce01378e0800acc70d4e8bd297727f32d6e01e332ad8d4ad9c3bf4c5	800256	/Users/duhokim/HermesOps/reports/status-audio/20260816T011800-cast2.mp3
9bc37146467ce09d262533f7ff84a0eeec78b9c6b6c601a2ccf77885928696c9	805	/Users/duhokim/HermesOps/reports/status-audio/20260816T011800-cast2.txt
1518e07544961db9e539507bc1e6468d4f0dec07d26eb137cb317dbe735613a4	751488	/Users/duhokim/HermesOps/reports/status-audio/20260816T013206-cast3.mp3
5a5c891e3b07ad599d687e06d1aa7e09d7e8e18543746ce2ca0038ec9db990a7	771	/Users/duhokim/HermesOps/reports/status-audio/20260816T013206-cast3.txt
22c01e8e67d1b47b972a59018e61046f93215f990d9586d7deb174c3d6d7385d	968064	/Users/duhokim/HermesOps/reports/status-audio/20260816T013609-cast4.mp3
8d333dabcb2d8e989df90a9cc9c24a422409945eab8fda1a3b0986ef0e1aecaf	947	/Users/duhokim/HermesOps/reports/status-audio/20260816T013609-cast4.txt
e7a7baf575d785a283880b8b768f08239ec5c62d63fba1df38bb3609f2cce43d	941568	/Users/duhokim/HermesOps/reports/status-audio/20260816T014119-cast5.mp3
aab6e27e3ab29200a765b98948fc2b1fbe9f6154db839b35b4ff8996401de52c	929	/Users/duhokim/HermesOps/reports/status-audio/20260816T014119-cast5.txt
6a6880aa63626fc9214b821c1d903005890157223f7324106402974194f14832	1011456	/Users/duhokim/HermesOps/reports/status-audio/20260816T014557-cast6.mp3
e8648ba0a67b5851c62a24e4e7175f57d16565d1ff3090f98d90a1df296edafd	1048	/Users/duhokim/HermesOps/reports/status-audio/20260816T014557-cast6.txt
6b60c3cc0526ba39770005f86f26d134d62d84ac1e3a3c31b68487fd7083b74e	1916928	/Users/duhokim/HermesOps/reports/status-audio/20260816T174922-memo.mp3
a5b1c43ab7b1b2ea12a4e7d541fc73d4febbca79458a555ef1dae250f70a0db6	1898	/Users/duhokim/HermesOps/reports/status-audio/20260816T174922-memo.txt
0a1969e189a5ed5f750c12eacf16706b61cfaee1a85afe39476861d34df48605	1368960	/Users/duhokim/HermesOps/reports/status-audio/20260816T180334-ck.mp3
3df8c39064e28990d0701e06146e2058f4b525b4dd3a7ac6d6138de3250438ae	1281	/Users/duhokim/HermesOps/reports/status-audio/20260816T180334-ck.txt
5e129b7493b152bae1952bdabf148d94c8b9f4b5c67fef400f3ea042adf5a29f	92928	/Users/duhokim/HermesOps/reports/status-audio/20260819T172624-hwao-report.mp3
8633b3c42032a934ff26affb7266237481452db5d1f2fe656c562cf991c39d9f	59	/Users/duhokim/HermesOps/reports/status-audio/20260819T172624-hwao-report.txt
cd667f14eab362905858c6c9df9d423215bacb5774c03d9a697a87b02e6c7d2e	91392	/Users/duhokim/HermesOps/reports/status-audio/20260819T172629-tori-report.mp3
b1dc016d318e9263bd682cd8afe7319807061a4328b96d115d6caef0cabdad2e	59	/Users/duhokim/HermesOps/reports/status-audio/20260819T172629-tori-report.txt
7b883cbf7eb017573f83957aae1cddf4645d43157bfd895f262fe89c2a25b828	246528	/Users/duhokim/HermesOps/reports/status-audio/20260819T172633-blanc-report.mp3
09bd87e8e7f4a073c47021eee0b33712ca9b3d96002189c7854446b83d3e0591	194	/Users/duhokim/HermesOps/reports/status-audio/20260819T172633-blanc-report.txt
5b44d9979fd299dca3b9ae626dbc50a6cac14f1cff5081ec43372af538960f93	97920	/Users/duhokim/HermesOps/reports/status-audio/20260819T172705-hwao-report.mp3
098ba341f807256f8b746d3ecfa9946cadd738d6464169adbbe8e2af15ff1c05	63	/Users/duhokim/HermesOps/reports/status-audio/20260819T172705-hwao-report.txt
0cea71f7c8493ae21fe45fe890a061d39a528e54dae4bd5a34fe324c2024b509	83328	/Users/duhokim/HermesOps/reports/status-audio/20260819T172709-tori-report.mp3
3b4daed964dbe159da459334d633a9140ce423acfe5c0d21114a2e0c52b6cf94	59	/Users/duhokim/HermesOps/reports/status-audio/20260819T172709-tori-report.txt
956f299ce39efebdf98aa1af46f174ba7b1bbc99c468a298ae8d6e52d5dc9012	178560	/Users/duhokim/HermesOps/reports/status-audio/20260819T172713-blanc-report.mp3
acc420a0041031dee2086768844e92ec2190ba47edb0cb943c1c7e9839d75d93	149	/Users/duhokim/HermesOps/reports/status-audio/20260819T172713-blanc-report.txt
50a896360952c31f28eb653c3afc4b64964212e39b2e33f82a420303acc7d16f	90381	/Users/duhokim/HermesOps/reports/status-audio/20260819T173135-all-three-fable-voices.mp3
d06c4b225549aef70c7e8c82cbe7d70019f8076bf5f5734cbc2f1633b6d9c823	271	/Users/duhokim/HermesOps/reports/status-audio/20260819T173135-all-three-fable-voices.txt
c4137f050d566f83843500deab20237d94791723480b20b62f01b8eb1db3704f	77568	/Users/duhokim/HermesOps/reports/status-audio/20260819T180450-blanc-report.mp3
0c9dba98e1acb3e5ba9e835398c8d1edeb6da78daef5944838920f0572e9f6d9	57	/Users/duhokim/HermesOps/reports/status-audio/20260819T180450-blanc-report.txt
0ff8700c935b394bbc16fcb82707a1c7920dd8e8ea2afb6e2618ea9bbb675e5e	163200	/Users/duhokim/HermesOps/reports/status-audio/20260819T190426-blanc-report.mp3
cdc7709bae53faae67c8be2aa34d9b6b9b4a3cfb6a96ab3a1ad2e0502f35bf88	155	/Users/duhokim/HermesOps/reports/status-audio/20260819T190426-blanc-report.txt
9686091affb66a1c9f8aa65fd49b20e21936b0c9e31aeeaa1b15beb51d3a832b	100224	/Users/duhokim/HermesOps/reports/status-audio/20260819T203424-hwao-report.mp3
5cf812dc0e041514638c6d413802fd8bdbac101275cc45dff77d220af0ae9949	83	/Users/duhokim/HermesOps/reports/status-audio/20260819T203424-hwao-report.txt
ff909af1fe5333dcac65d12ebf3cbf5a1af77b6d52e749d9d0c0811c66c7de8b	104832	/Users/duhokim/HermesOps/reports/status-audio/20260819T203618-tori-report.mp3
44c947dd56d836f0dc61508d42bbf39b70da92f0909b3636182d50daf1ceed77	76	/Users/duhokim/HermesOps/reports/status-audio/20260819T203618-tori-report.txt
b0d2c172a6941caf41805a1a47cfd9369e22034d44e61bf19ef990136dd9dc24	89088	/Users/duhokim/HermesOps/reports/status-audio/20260820T013533-blanc-report.mp3
f84ca9d0d8c0fde900d7dcf4e4075fe176e90ba807f85a8852b0fed5e73becee	80	/Users/duhokim/HermesOps/reports/status-audio/20260820T013533-blanc-report.txt
67bc9149170ac4ca2e9aa57ac6d330c7479df671e38d89201c9dc4af4ba327b4	64128	/Users/duhokim/HermesOps/reports/status-audio/20260820T020246-blanc-report.mp3
771a249cdc14189ef70c8ce0c042f182f94bd2e9e3b8d0159ee5240386360c55	49	/Users/duhokim/HermesOps/reports/status-audio/20260820T020246-blanc-report.txt
5ad3dd9bf4ef6dd70bc5b336b84f32320d4c8d8e884ebdee33bcaaf5130b64f2	620160	/Users/duhokim/HermesOps/reports/status-audio/20260820T072013-hwao-report.mp3
484f8429d9b14dffeefd7bdda4d00ab0c1b5be63fdf39eb9888f4db7f078aa78	594	/Users/duhokim/HermesOps/reports/status-audio/20260820T072013-hwao-report.txt
223e064a4e5615c34bc76da48ab94ef8c5b7bf9bca633e113eea74044b7cacb6	696960	/Users/duhokim/HermesOps/reports/status-audio/20260820T081331-blanc-report.mp3
3fd305d3d27ac46dcab473a4454b385f1a23e479456cb71c6f0ae929130ede8c	749	/Users/duhokim/HermesOps/reports/status-audio/20260820T081331-blanc-report.txt
e286cadd1d399f329846a224a85d37f2f9fe3f723be7d6c6f9ded8f1672ed1cb	879360	/Users/duhokim/HermesOps/reports/status-audio/20260820T091428-blanc-report.mp3
5edb4bcde997d6f58a609c96ba11c2353e5f56a97207c400dfef7ca92a67b785	894	/Users/duhokim/HermesOps/reports/status-audio/20260820T091428-blanc-report.txt
1259c5cf8dd9a69e1c1404a2c7d0726bbb74003adde0d6f38780c4840bec1f84	158061	/Users/duhokim/HermesOps/reports/status-audio/20260820T102513-blanc-voice-audition.mp3
d10c47d72e0bea9ec28327f645aeadba4c08fab06ecbec439802ec5677f96163	69	/Users/duhokim/HermesOps/reports/status-audio/20260820T102513-blanc-voice-audition.txt
e85b003a8c0dc437abaf083619c273bfa4e8e9b945b6e34cbcec9f5af4c44d2a	78720	/Users/duhokim/HermesOps/reports/status-audio/20260820T102924-blanc-report.mp3
c3500b05119f8eb4c210348c52a84da7edc2ca7dda7c6abff1ee0b4bd54cef30	64	/Users/duhokim/HermesOps/reports/status-audio/20260820T102924-blanc-report.txt
3d95651601dba7377b34a567e010f95f79281e631f0f5c72fe4c200e881a932e	777600	/Users/duhokim/HermesOps/reports/status-audio/20260820T103935-hwao-report.mp3
60bdf7ac192d0bb0d23f7533868d85661c691e898480da149cb3c330665983cb	729	/Users/duhokim/HermesOps/reports/status-audio/20260820T103935-hwao-report.txt
23d4d399ebe881eb94603fc79cb5870c185b3ef0bc62d4f59bff3ac5af19a26d	703488	/Users/duhokim/HermesOps/reports/status-audio/20260820T104354-hwao-report.mp3
46c8acffc0ea1a588a6165fa13ccf97c4af2a78576b00857024de519c023b85a	689	/Users/duhokim/HermesOps/reports/status-audio/20260820T104354-hwao-report.txt
fa0ec69d2a99b867e8c0c090bd7983a39517b0d64b9be10aa4ef7ee5f3c74863	2055	/Users/duhokim/HermesOps/reports/status-audio/20260820T165959-hwao-report.deck.json
7db1d28d94b2511c40c74d6504d4d261b5f5480e511176b515a0043cb86cb39f	935424	/Users/duhokim/HermesOps/reports/status-audio/20260820T165959-hwao-report.mp3
c924665004c802350c1a1b6e632c7cd7f1d32ca4503b062c4078fec4461a9dbe	762	/Users/duhokim/HermesOps/reports/status-audio/20260820T165959-hwao-report.txt
7e6a12f61a915741622128903aa33569a2d695748ea0356182ffd2f7ae16e936	134400	/Users/duhokim/HermesOps/reports/status-audio/20260820T170439-blanc-report.mp3
f21b059fd791c7c6397faea4ec48887a85d66b9722f0d1e3d72cdbecbbd493a4	67	/Users/duhokim/HermesOps/reports/status-audio/20260820T170439-blanc-report.txt
4954cb3901dc901eb5aeba48350cec13dfc14ceb6af08ab18afd4b60f664c941	1264	/Users/duhokim/HermesOps/reports/status-audio/20260820T171915-blanc-report.deck.json
7c2a02716742740d648f1765607ca1fdf54efc6dcca09499b7acf97a3b9bf4d3	369792	/Users/duhokim/HermesOps/reports/status-audio/20260820T171915-blanc-report.mp3
79a571159758428724d13743e84986e5b0a811e6784b4fec35ea1bf39d1fb996	365	/Users/duhokim/HermesOps/reports/status-audio/20260820T171915-blanc-report.txt
f2420767414c8b316ce85bfbc21ff6c5c3ee9220fc4c4db345d85923bc5caa0b	1800	/Users/duhokim/HermesOps/reports/status-audio/20260820T173007-hwao-report.deck.json
63f6ac43d5231c39b12cf8afa52fc6348364166b2a02449dba8a2a8be03a5654	1019520	/Users/duhokim/HermesOps/reports/status-audio/20260820T173007-hwao-report.mp3
6fce03fa997307084c59edf58d5800776789fe5dafa21c82d96abff19e18523d	724	/Users/duhokim/HermesOps/reports/status-audio/20260820T173007-hwao-report.txt
5cdc101701c157cef512c0d723ae2c922c2e715220b9138ff143d47fed55ac01	743	/Users/duhokim/HermesOps/reports/status-audio/20260820T173007-hwao-report.txt.corrupt-20260821
ecadbad9757705ff70938612d5009427e825ce1134b43c6c42a00ffa90d3af4d	3261	/Users/duhokim/HermesOps/reports/status-audio/20260820T173124-hwao-report.deck.json
88a4a6a6a9c72e6d1654337aacc843ee539311d63f7110cc189e63ace1124721	976896	/Users/duhokim/HermesOps/reports/status-audio/20260820T173124-hwao-report.mp3
017495768c5a3fcf5a9aa140eaca11a6c58b947d012abfaea455d37e9970aa68	719	/Users/duhokim/HermesOps/reports/status-audio/20260820T173124-hwao-report.txt
781a3118ed1ab90a25bc37e18c76f464bdf3915424bbf6278a06065192e44331	2842	/Users/duhokim/HermesOps/reports/status-audio/20260820T184851-tori-report.deck.json
0657c266b9eee7eac6107405d29b281cff39b2fc6b0d50b7923359957b12b0a4	806400	/Users/duhokim/HermesOps/reports/status-audio/20260820T184851-tori-report.mp3
3f42ecc52851fd7d81367fc30591d84e7aabf90d123a4372cdf1dde3a0c7accb	701	/Users/duhokim/HermesOps/reports/status-audio/20260820T184851-tori-report.txt
d13e604eba14da7ff22c455c02b0c671793e0d952a10d561c03e62a29baceca3	3266	/Users/duhokim/HermesOps/reports/status-audio/20260820T201107-tori-report.deck.json
6db133b112a310b9eba90f03eb432e1ef864a9cd4c224c74640801aa7f631e7b	822528	/Users/duhokim/HermesOps/reports/status-audio/20260820T201107-tori-report.mp3
6391ce4a769cfa28334d633bc5bcc71ddd796b3027d35b1b4efd76a7ddc8e59a	767	/Users/duhokim/HermesOps/reports/status-audio/20260820T201107-tori-report.txt
eeebc60afcb134847745010ce756fb6e5429319e278900e6c95acb8c8e3acf04	702	/Users/duhokim/HermesOps/reports/status-audio/20260820T204136-tori-report.deck.json
d74bf254abd03eddd2c13b96b1446bc4bef03c33d77c3e33bf0a1634681efc32	76032	/Users/duhokim/HermesOps/reports/status-audio/20260820T204136-tori-report.mp3
b972c459c9372e2b159cb737b3bcf2a7644932eeabea46f5b50ab74fc6cfa1a4	63	/Users/duhokim/HermesOps/reports/status-audio/20260820T204136-tori-report.txt
d84bf963ce608387298041262614314c1cb7fa4608666178c4ed341a10677928	1585	/Users/duhokim/HermesOps/reports/status-audio/20260820T230754-tori-report.deck.json
27e70b61f97b4bf61f832e4ea1e49ce41267293a3b8bad1d2983d046696646d0	616320	/Users/duhokim/HermesOps/reports/status-audio/20260820T230754-tori-report.mp3
7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47	577	/Users/duhokim/HermesOps/reports/status-audio/20260820T230754-tori-report.txt
1da50dc6878db90524adf5044f706281d497784c4074cef4b6ce483d2b1d9a6c	2543	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.deck.json
2a38a887bd89714731e6c6ae3ca34fb232d21f606ee0e49d1c475c92a475a168	1131264	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.mp3
a9cfedc4ab127794f41b68abbf13b7d2bfe7e9d08ec4f6ca3ebaa19665787c79	163	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.times.json
2c85b2028209273a2aa97995db2177b063ac851b5853a9d54243594c589f2162	1035	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.txt
7c8a8668a00cd9b8692b49b4fd4ff93dedb40620a235830df38e4515dac640ad	1055	/Users/duhokim/HermesOps/reports/status-audio/20260820T231235-hwao-report.txt.corrupt-20260821
855da9448492112c0529476cf451466934c63474068419cb3382009bfb9108ab	3292	/Users/duhokim/HermesOps/reports/status-audio/20260820T231324-hwao-report.deck.json
785aed20de80d27118f915d7a05b02daac1520fc52e919231bd1f575bea0a1ad	1272192	/Users/duhokim/HermesOps/reports/status-audio/20260820T231324-hwao-report.mp3
5ba48ea353bb94a3a5740c4be8160e552e996670287f124fb66b69d5cf781842	1131	/Users/duhokim/HermesOps/reports/status-audio/20260820T231324-hwao-report.txt
27e70b61f97b4bf61f832e4ea1e49ce41267293a3b8bad1d2983d046696646d0	616320	/Users/duhokim/HermesOps/reports/status-audio/20260820T232407-20260820T230754-tori-report.mp3
7b23700c5b65d3ff3852cfc82e62548ab2e0c7f93a1030ae9ee16116545ecd47	577	/Users/duhokim/HermesOps/reports/status-audio/20260820T232407-20260820T230754-tori-report.txt
1af45a7e0cb275f3a3605aa3f3b68e78f899421939306ebac45f8448b66a1f12	12914	/Users/duhokim/HermesOps/reports/status-audio/20260820T235925-tori-report.deck.json
693998040c0e1f72d9331a083b48f5509a7c4d269fcb1aaaf37f0589494566e6	1861632	/Users/duhokim/HermesOps/reports/status-audio/20260820T235925-tori-report.mp3
e7bb0840e087162056e8958a6df6a7890678a8921972cbc981e8b09f6504293e	1853	/Users/duhokim/HermesOps/reports/status-audio/20260820T235925-tori-report.txt
c49c71978ee27eedab93076906a27f188eee3b4b905caed13b674127feab091b	10840	/Users/duhokim/HermesOps/reports/status-audio/20260821T004950-hwao-report.deck.json
b730dfc2b28b05835f548f0aedc1096c7e51e2067a087091b1448384a4092ed2	2472192	/Users/duhokim/HermesOps/reports/status-audio/20260821T004950-hwao-report.mp3
f1096d51b237dbeaddf92b034194ed9f23d89401b54bb26335b74d1ead81b258	2562	/Users/duhokim/HermesOps/reports/status-audio/20260821T004950-hwao-report.txt
81e12c9a380d2f8a5bb65f2b81d45a0da8dc2877cf8dd22f9bb1dc5da504a3cb	2112	/Users/duhokim/HermesOps/reports/status-audio/20260821T080428-blanc-report.deck.json
264d8731fdf523ac588b13aed142b0f3d4283ba00fd7f8a41b586fd55430c91f	652032	/Users/duhokim/HermesOps/reports/status-audio/20260821T080428-blanc-report.mp3
452f13b624ff952df0987b7f54feccc632fde6c0f2eb569c365fa92ab968a982	627	/Users/duhokim/HermesOps/reports/status-audio/20260821T080428-blanc-report.txt
88394b89139669d66bef04ea85c62f591490f11ef767b5f14421784b2a54f131	712	/Users/duhokim/HermesOps/reports/status-audio/20260821T105930-blanc-report.deck.json
5492a78d89d136e0a9b497da8781e28d33a190e34f286e55454a6c78172a55c6	86400	/Users/duhokim/HermesOps/reports/status-audio/20260821T105930-blanc-report.mp3
ada74c9a1761ba02f9f0c0fb6c31a3415d4fc80a2619a8776905101d1e146951	67	/Users/duhokim/HermesOps/reports/status-audio/20260821T105930-blanc-report.txt
8b3ddead69fb6764df63a35352eca9332b52b9472d4626a6e5e05430f20b4ad1	4340	/Users/duhokim/HermesOps/reports/status-audio/20260821T145923-hwao-report.deck.json
21de44c997065b03c8ac4460217f863904e5ba085c110f5cbe38cbb1eea92d00	2921856	/Users/duhokim/HermesOps/reports/status-audio/20260821T145923-hwao-report.mp3
c3aefdeea36b45e60f63e297bfed77358fda8db3d63560c245386b3d20cba8b2	2991	/Users/duhokim/HermesOps/reports/status-audio/20260821T145923-hwao-report.txt
0fe5ecac190cfcb490cdcc42aa52b1069e7bf2a3b97d996d3faf13ae0030b8cc	2997	/Users/duhokim/HermesOps/reports/status-audio/20260821T151249-hwao-report.deck.json
f468c515b5d852d82d08da0c5a41ee04cd75e7d70139ae9633d77a0e611df53a	1776768	/Users/duhokim/HermesOps/reports/status-audio/20260821T151249-hwao-report.mp3
5648a55e23f6fddfdd9d215c1c64ea8eaf83c6a51fdec991a5f67ba31dc6e37b	1818	/Users/duhokim/HermesOps/reports/status-audio/20260821T151249-hwao-report.txt
6437b0993110b9dca73b811017a0ba49803faa255a413cb89a2ad1c754a691ad	3604	/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.deck.json
5ce21d93671c204c32cb3069ad3344f7db51715120796890db171c322ff795e3	2596992	/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.mp3
bea09d4415afbf69bb3cd54f8a38f9263c0c7afed53169dcf056b532eae4a848	390	/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.times.json
fc3a5a2824e622cb758e1ee00450165259607782a13460ada71729d57659c98c	2702	/Users/duhokim/HermesOps/reports/status-audio/20260821T151843-hwao-report.txt
ec91f2ed3499f2bb2d291154b9a18c43b00841082853ac46c31f57a97d192998	2299	/Users/duhokim/HermesOps/reports/status-audio/20260821T190931-tori-report.deck.json
a897ce35c324e6d356350b728f6b16e7398581501718d1991ef72bb4c54fc999	1083264	/Users/duhokim/HermesOps/reports/status-audio/20260821T190931-tori-report.mp3
c42bc1d4500a8e0db4411715c1237da0ebf9a39d9d88eb1fa7d633367281770b	1163	/Users/duhokim/HermesOps/reports/status-audio/20260821T190931-tori-report.txt
f208eaab7cec9040fa0063bb9f722aab36046ffbae4c49216fb8dc305def1d55	2546	/Users/duhokim/HermesOps/reports/status-audio/20260821T200910-tori-report.deck.json
2a55b081db5861e57390c927e077ae98558dd666ec71d2f677e0f47bdf4d2ee3	1248768	/Users/duhokim/HermesOps/reports/status-audio/20260821T200910-tori-report.mp3
1b7d622e8ef866752b1c9e82ae5d3edb97ebd85c0a9de18847801f32ea658940	1335	/Users/duhokim/HermesOps/reports/status-audio/20260821T200910-tori-report.txt
83988126c6ef8c6fef4bb696c345fc03c833620158bad0496aa19fa300cdad23	1442	/Users/duhokim/HermesOps/reports/status-audio/20260821T210530-tori-report.deck.json
97065f66cdffade0081f5350b4ac702998fc42193608bc711c4a58f7209cf6c5	1328256	/Users/duhokim/HermesOps/reports/status-audio/20260821T210530-tori-report.mp3
6e35f60af1cefff0f8d03dfb5bdc6c22e99f9be81e4961493b59f23cbee86556	1324	/Users/duhokim/HermesOps/reports/status-audio/20260821T210530-tori-report.txt
bde06d0e9bdc3245ecd7f5506e875ae3fa887d0fc9a4d599747ed802606e571e	775	/Users/duhokim/HermesOps/reports/status-audio/_caption_backup_20260820/20260816T013206-cast3.txt
05be5114ea6313a459bbb8bca6d5ff35184e612da0cf1b1f266a9e4ddabbda7c	949	/Users/duhokim/HermesOps/reports/status-audio/_caption_backup_20260820/20260816T013609-cast4.txt
7fe8b20c382ca2f81e52df6b32bccab276aaa843c42fa85266535392b30882b2	1900	/Users/duhokim/HermesOps/reports/status-audio/_caption_backup_20260820/20260816T174922-memo.txt
abbcc68d5b715a85f78a0b920882c2af03319810ad46ba1b3ddb579f7ae3ea3c	10398	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235839-hwao-report.deck.json
245d5c815cbda18a43f11eb0da2fee885882b1d74f2b29770873d301b17d5eb8	2019456	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235839-hwao-report.mp3
ced123258db9e2eb517c1cea8335ab743c5411256d9d6704a2dbe60405b9bf26	1974	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235839-hwao-report.txt
1caeef29733b84df1eac2ae02ae91d15f108967ad14be4e2ed54a798625d8f39	3516	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235925-tori-report.deck.json
693998040c0e1f72d9331a083b48f5509a7c4d269fcb1aaaf37f0589494566e6	1861632	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235925-tori-report.mp3
e7bb0840e087162056e8958a6df6a7890678a8921972cbc981e8b09f6504293e	1853	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235925-tori-report.txt
f82d7bf828dce0ce6e697f47d636bddd3db01745cc146afe6bd5b82c6990ce56	11692	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235940-hwao-report.deck.json
c4789881734e557c0a1c877a2ddeac6e42cdb261cb2cd60c5c2e82885ad8c6da	1944960	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235940-hwao-report.mp3
8666d0fa246e33bd2f8cd65aba20a60732c482f247b0abea7a303ce3bab028bd	2002	/Users/duhokim/HermesOps/reports/status-audio/_drafts/20260820T235940-hwao-report.txt
0776f8051ebab2afe887d20f176aeb92191555fa27f95411862550fe8f02b1f7	2636160	/Users/duhokim/HermesOps/reports/status-audio/approval-frame-20260810T1740.mp3
efac6d1ea790b9ec2351c15639523245042d9ffd8e3b12c02cc52b5c59542e41	2627	/Users/duhokim/HermesOps/reports/status-audio/approval-frame-20260810T1740.txt
d13fbb3f157c9533ae06bca6a74bff7cb0bd3a9ef7cd538ca9b540efb4000ef7	97771	/Users/duhokim/HermesOps/reports/status-audio/archive-2.html
07176092ef8f9c72fd20f112ea6fa5e43840f18da2a970e9efebbf7cc96a071c	159359	/Users/duhokim/HermesOps/reports/status-audio/archive-3.html
21a8031c647d9f2c8aff544e9788ebcffad5dcb7be93927ed2f8d4b3ba47e08d	210170	/Users/duhokim/HermesOps/reports/status-audio/archive-4.html
9c1d188d4fe5582addd2fcb8551cbbbdb7eae94c89c0d288ff9dde5dfeb436e0	83216	/Users/duhokim/HermesOps/reports/status-audio/archive-5.html
33c4c6c8db63ed278945bd06fd714b352777857372e72b185358e982bd573710	208244	/Users/duhokim/HermesOps/reports/status-audio/archive.html
7201f7c5d268b8d470e7b6cb2d5893f59e7a3d2ed8dbf33ed1681c41704fc430	1895424	/Users/duhokim/HermesOps/reports/status-audio/autoread-20260811T1100.mp3
a4b9aae3745289954320ef9d3266af3ab0362e10c105d2bc0e5a2aa62d198fad	1946	/Users/duhokim/HermesOps/reports/status-audio/autoread-20260811T1100.txt
6da95fa93ccbe24002806998eab1e9ea4ec763e3ba3d58dc4c5849519cc92ee6	1355520	/Users/duhokim/HermesOps/reports/status-audio/cleannote-20260811T1432.mp3
ed2372b737de1e5bbb6a907988bafa31f0da4a9314be20c88cc9b8b4d3ca9d5d	1445	/Users/duhokim/HermesOps/reports/status-audio/cleannote-20260811T1432.txt
5c8558f1de38e3d2b160e9fab2f8cf08adddc32302a5ca16f571ba9e7a3dce25	2343168	/Users/duhokim/HermesOps/reports/status-audio/closespin-20260810T2208.mp3
f82df2942cc144b0d39bc1e120ea501a25741e91f2d54dee91a058c95e38c4d9	2433	/Users/duhokim/HermesOps/reports/status-audio/closespin-20260810T2208.txt
d28569ed9bb2e0f15721913996695bdbd4d82e81aa4d932e8e2f78a35f62cd02	1382400	/Users/duhokim/HermesOps/reports/status-audio/dec2-armed-20260810T1822.mp3
00ad3628728a1bd9bcfea82b0f571d03fb6ac85791f70f4af2d72111e7215dfe	1378	/Users/duhokim/HermesOps/reports/status-audio/dec2-armed-20260810T1822.txt
07aa07fbf7f4dc8c2c35edf8d8712dfe95609e52392191655e337d9742ad330b	1879296	/Users/duhokim/HermesOps/reports/status-audio/dispatch-20260810T1716.mp3
189531b0232d52c69e346fa64a9affaf40e7627a15672c973f36e613c4c632ba	1802	/Users/duhokim/HermesOps/reports/status-audio/dispatch-20260810T1716.txt
bb3ca29568f7891fde28f11c034cd370282733964cdb83b6b9a855c5b87aeb5a	1963392	/Users/duhokim/HermesOps/reports/status-audio/framescope-20260810T1436.mp3
eb91acbd6b3bfc462a1774b30edfe0ef2094862f93118c13bd8acbb9804406e3	2038	/Users/duhokim/HermesOps/reports/status-audio/framescope-20260810T1436.txt
7f5506aa06b7e935557c03428c8c1dc46c85d897f70c77a72c76099c73fcd102	2305920	/Users/duhokim/HermesOps/reports/status-audio/freshlabel-20260810T2158.mp3
9b1aab1eedc96b348f94cb78670a004024d5cb0a1d8f4040be5afba0547eae94	2318	/Users/duhokim/HermesOps/reports/status-audio/freshlabel-20260810T2158.txt
fe55a3a744d00ca11983d0626eeebd323d760aa05905bb231d16e3169314b528	2123520	/Users/duhokim/HermesOps/reports/status-audio/gate-block-20260810T2145.mp3
33df410cc44b76b96eb840e8a0b4ed5fb5b7503aad5f35e87b64c0de341d2383	2117	/Users/duhokim/HermesOps/reports/status-audio/gate-block-20260810T2145.txt
9eac05d4b1fc131d98c04a8dcca49c8b79850630a5a4103c1c19bbc6cd038d2e	1921920	/Users/duhokim/HermesOps/reports/status-audio/kunblock-20260811T1330.mp3
ecae4c909cfb151b2debd77545e144bddd971d0e911f911b7714c0173332834e	2063	/Users/duhokim/HermesOps/reports/status-audio/kunblock-20260811T1330.txt
00ba01a39c2e5bb394971a0d9b4b08ffd89f56b6408d18fd378136d90695219f	1626624	/Users/duhokim/HermesOps/reports/status-audio/kungate-20260811T1330.mp3
9c4648c0d64b80c86ffabf745648995933fb48263e04d539de2ff54363f3184f	1655	/Users/duhokim/HermesOps/reports/status-audio/kungate-20260811T1330.txt
e6e6e6eb1c46a4de351bbaede4beb87976234b5a074e3afac78c8edcfa0a4c2e	2023296	/Users/duhokim/HermesOps/reports/status-audio/kunpass-20260811T1425.mp3
8e751329b202f041e36e48a410aa1fb28bd45dce9d904a0bfee0ad0697ced43d	2056	/Users/duhokim/HermesOps/reports/status-audio/kunpass-20260811T1425.txt
613b63d5f73dcfed1a763a9a4098e5594c44465062a4c264bb4a5a803f110f33	1696128	/Users/duhokim/HermesOps/reports/status-audio/kunverdict-20260811T1345.mp3
85834b101b791dce5c85f67f205bbfeec6c981f8e347792678b30d3c6a7c26c3	1724	/Users/duhokim/HermesOps/reports/status-audio/kunverdict-20260811T1345.txt
215ade284632acffebfa3c9477019f7ccb2816db8ae26abd701137934e735f1f	1235328	/Users/duhokim/HermesOps/reports/status-audio/lanaunblocked-20260811T1422.mp3
1c30910587b4a00e9e161c1a6a693c45bb4e5341dbfeec4b95dbd9a684dada98	1293	/Users/duhokim/HermesOps/reports/status-audio/lanaunblocked-20260811T1422.txt
97065f66cdffade0081f5350b4ac702998fc42193608bc711c4a58f7209cf6c5	1328256	/Users/duhokim/HermesOps/reports/status-audio/latest.mp3
b93f504c83c1e7e105e57fda9b259171e138ab682e893690ecbd3285c993b884	57	/Users/duhokim/HermesOps/reports/status-audio/latest.txt
d3504fab7a602fd9b55677b2b7c10f094ecc9a123f3b6ab612a0d0ea1e81469e	2577792	/Users/duhokim/HermesOps/reports/status-audio/loosen-20260811T1105.mp3
011c1b261c16ffb6ff6958b409ceb1d4c11463aee8c9197696d8ad43c9103006	2657	/Users/duhokim/HermesOps/reports/status-audio/loosen-20260811T1105.txt
cb3cc4cd540e6173ecef5d9ba24226c0e14281b6359a8d13a3e9224d545487bc	2639232	/Users/duhokim/HermesOps/reports/status-audio/methodsnote-20260811T1325.mp3
36569b18a5991ad336a447de9f6c63ac2917a00375ee0a23fd81d40512e19303	2874	/Users/duhokim/HermesOps/reports/status-audio/methodsnote-20260811T1325.txt
b31103951e76bf6cac1e9313e3d802c0a7b3868c92741db6504faa1cd167bdbe	1909632	/Users/duhokim/HermesOps/reports/status-audio/moonshot-current-20260810T1758.mp3
6083e733badd9df8b9b749c2c29474c8254becf6544874aaf5e2f6168abfb1ea	1922	/Users/duhokim/HermesOps/reports/status-audio/moonshot-current-20260810T1758.txt
fe96ace17d9a6fadf42cc7a5c8f1ffe13760f3064a0744e0d8e1f4cf243fb0e5	3383424	/Users/duhokim/HermesOps/reports/status-audio/morning-20260811T0837.mp3
f123e7e6671a6a679ed0257338e474047d1582d877c20efbf908303868a094eb	3621	/Users/duhokim/HermesOps/reports/status-audio/morning-20260811T0837.txt
4a6df9edd73943a219d80d087d915a9afa710e6566a481137ae3034a39e60a44	2065920	/Users/duhokim/HermesOps/reports/status-audio/note-20260811T1315.mp3
3c078c2c2be100267ee5c613e4eec0669b125ba98b91da6c5b3f1c28b92580f8	2175	/Users/duhokim/HermesOps/reports/status-audio/note-20260811T1315.txt
2c01e69f73725ea87964a010a7de433801288a943e6870d9065414e0e274a8b0	966528	/Users/duhokim/HermesOps/reports/status-audio/notewatch-20260811T1320.mp3
078cd6888a7d42654f46eec8ae87ba39dd636eabfb7296ee9a224a2d74361a0a	948	/Users/duhokim/HermesOps/reports/status-audio/notewatch-20260811T1320.txt
a6fe4b65e62ac1c45e6b2efdc6273bbac8a2560339c23e13ac6a530f647567de	3150720	/Users/duhokim/HermesOps/reports/status-audio/novelty-20260811T1100.mp3
61cf5964196a0318f2a12598fd3fa79e109e51771180310d521e1407d817b6bf	3250	/Users/duhokim/HermesOps/reports/status-audio/novelty-20260811T1100.txt
5e2ab4dcaee5565fff4f8bb15d39dd48b104c156608600efe00e5c6302802e76	2755968	/Users/duhokim/HermesOps/reports/status-audio/pathc-20260810T2152.mp3
d1132b62da543a29ec0c731787c5d5e58a06d22843769c2ce7caf86a12004df7	2900	/Users/duhokim/HermesOps/reports/status-audio/pathc-20260810T2152.txt
792e501fb57fb89ef8c2c34389f17d85e7ca54f397a7dfd2abb9386e26302565	2509824	/Users/duhokim/HermesOps/reports/status-audio/plan-20260810T1710.mp3
23f5639fa1c1746ab48983476b22a754d0c729679530558b9d7e1d3f24b317cd	2480	/Users/duhokim/HermesOps/reports/status-audio/plan-20260810T1710.txt
213dc40b6a926f13e6a5871a29bff752f5a22c4ab5c945f0028da7406c8dfcfd	2156160	/Users/duhokim/HermesOps/reports/status-audio/preflight-20260810T1902.mp3
1e4ff2e9dff0a3279bbce632b02b013ad81b323b9b3aa4e5df1cb601538ee0fe	2034	/Users/duhokim/HermesOps/reports/status-audio/preflight-20260810T1902.txt
491f38b0684f102f38670405cb3419ed824c1afc76db41560d4474e053f5f392	2824320	/Users/duhokim/HermesOps/reports/status-audio/provenance-finding-20260810T1730.mp3
a342b5d9f1f446d5c81170ba625e0b063a2c3a4182d06bc6d0381de4bcba7492	2700	/Users/duhokim/HermesOps/reports/status-audio/provenance-finding-20260810T1730.txt
bb3fc677650d4ea6bbc7ff99b91d35fd7f7728afa75d97a1de2a06ae5f07e939	2011392	/Users/duhokim/HermesOps/reports/status-audio/quaia-20260811T1050.mp3
add9ed9a871a39b95adf206d365b781582c1e5b2610c8447c83f89937399a092	1832	/Users/duhokim/HermesOps/reports/status-audio/quaia-20260811T1050.txt
256f3215379b85d7851c5166e0143b9d3d3f8aac9b4df2a2132aca160c7e484e	17528	/Users/duhokim/HermesOps/reports/status-audio/queue.json
b92adc4577fa6a7c42f6be9e89913822c034e262c44dd5f9d2522ce48d1ddee4	26648	/Users/duhokim/HermesOps/reports/status-audio/queue_ledger.jsonl
12c65ddaf3d6cfad05461eb71f0363ea890f8d3b5704ebb8d76183fcc3dce421	2365824	/Users/duhokim/HermesOps/reports/status-audio/quota-coord-20260810T1733.mp3
27f28d63152c8737b61cb05703275dadb1669099a73c1ce855b76b7548116570	2343	/Users/duhokim/HermesOps/reports/status-audio/quota-coord-20260810T1733.txt
391cf20a84e66b118f95d13908881cbf0c4ad026325d947fef52e3968dd0dfc5	1869696	/Users/duhokim/HermesOps/reports/status-audio/recommendation-20260810T2113.mp3
2ecda8e5590cbf01d76532567c77566f6d578bdbc1de856a845636374615e336	1989	/Users/duhokim/HermesOps/reports/status-audio/recommendation-20260810T2113.txt
41caa30dcbcd7999ed603866261dfbc8c038bd5d5a286ebd0c0e944289bcd10d	1923456	/Users/duhokim/HermesOps/reports/status-audio/reframe-20260810T2205.mp3
ac1e85f82c6adce364c07c36e7c41b09ecfe493d85949d2f8998106e437535ee	2011	/Users/duhokim/HermesOps/reports/status-audio/reframe-20260810T2205.txt
1f5ee0c5732089db6ef8ee2cba30f54b5a96a21ae69849238402b7f703c6ecab	1379328	/Users/duhokim/HermesOps/reports/status-audio/regate-armed-20260811T1015.mp3
8301d26df2624ef456c71704a1c6e657e77968dd39e900a1080e6a2c3e7588e6	1479	/Users/duhokim/HermesOps/reports/status-audio/regate-armed-20260811T1015.txt
d06e9ea034b7293b54154d665d17787ab37f342b31366df17001ca8103dd54ce	2421120	/Users/duhokim/HermesOps/reports/status-audio/regate2-20260811T1032.mp3
d3ad1090e918d0c03afd8656b53591c78adab2baefeae32a217ee2bfeed74e4b	2516	/Users/duhokim/HermesOps/reports/status-audio/regate2-20260811T1032.txt
bf28d5c9a10d1838dd906ba206f3b7b01c9cbe57ab8db41fed414251b43328d4	1635456	/Users/duhokim/HermesOps/reports/status-audio/regatedispatch-20260811T1335.mp3
48b1584cdb72779182161e89792e32ac6a62f1559a4e586a34c4033499df8dfe	1822	/Users/duhokim/HermesOps/reports/status-audio/regatedispatch-20260811T1335.txt
713b1e39c7cc48ad3a45e623b904a8f3a7b574668af9a9c4e5059da5faad1cd1	1223424	/Users/duhokim/HermesOps/reports/status-audio/relwatch-20260811T1102.mp3
996ce9367c13e0188adb91f29a5e1abe43a2ac6617810d6319f1a97abea82bef	1336	/Users/duhokim/HermesOps/reports/status-audio/relwatch-20260811T1102.txt
0403d9704dfe1068bd91e49392316785a00ba7e5e2e0560812301df32f4de403	6195	/Users/duhokim/HermesOps/reports/status-audio/report-20260814T160157-variance-pass.html
84a603a930b109eaf9806c5b4b89e25f2f9fa1404593b8779826ff43d81928e8	6130	/Users/duhokim/HermesOps/reports/status-audio/report-20260814T160933-kun-regate.html
21e91f8e29240a959612d89e7ac1cb3afd634d31ebaba108e979320f0f4cf06c	6248	/Users/duhokim/HermesOps/reports/status-audio/report-20260814T161526-ten-blockers.html
116cb046efdf52865b8d6ba35734bf9cff10979a542806f9cc7c032eb80a3fb6	6269	/Users/duhokim/HermesOps/reports/status-audio/report-20260814T162102-both-pass.html
b3afff7634614262b4568a713f94c5fc130c85f064f5e605b8bdb80e50158ea2	6186	/Users/duhokim/HermesOps/reports/status-audio/report-20260814T162331-sign-dictionary.html
5f8292cbb5fbd6a6e444aaee515eedb4506e4cb2ddfa317e68e2055e38f23bc4	8038	/Users/duhokim/HermesOps/reports/status-audio/report-20260814T163726-session-summary.html
4dac0fc77fb6eacfb7d109953e1d4a7b755bcadaf921e8c78c12bc10cc125ab2	6373	/Users/duhokim/HermesOps/reports/status-audio/report-20260814T170345-final-gate.html
76a84dae22a98c2d9ad28ab67051ca09ee3976d9932dff27d6c4753182a70c04	8316	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T165959-hwao-report.html
4b8bfb932ded6bf568b572ba17f937d0b2b2c891d449e2e3ec98a712a4faddf4	7116	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T171915-blanc-report.html
6212f448cd78c556a0268a334d27dd98cb8babbb200dc42651d2be26c179addf	8617	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T173007-hwao-report.html
5a0616ba2ce4571b74ba5f686d2e1edf196098c43237a4cf5218e91f6ea7799d	9452	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T173124-hwao-report.html
f36db2126ca7ce9401d143cd2913dc5e90146a8c432ace94c8e6970386308be5	9868	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T184851-tori-report.html
9a51511aeec21d31dbf9675d46428a42b519c39f4b37b85e6ea45e24cdb5312f	10373	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T201107-tori-report.html
dff5234724f1b1b641ae867f58524f173e71bc6fcc198e93a7800b6c72ffd0ee	6298	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T204136-tori-report.html
8db823083a03eb9afbc20e12631a44665a4f8081eca6b6e4a23f18eed2db8913	7672	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T230754-tori-report.html
050a3f6245fc74f1c471896db0b5e9ee1ae2e3b79ee762b1979d209ff3a31b9f	8856	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T231235-hwao-report.html
861e633683a49c70ca15d7d2a0e0e1fe21f7ea163111085cc13f4c03ebd82ad1	9874	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T231324-hwao-report.html
1ebde8a62d1393996e7bca9350e9c84aa2993a57cffd7b93a5b9ed358e04d256	27446	/Users/duhokim/HermesOps/reports/status-audio/report-20260820T235925-tori-report.html
d4693eb627d5785354cfa0c27057f48508f24cb88697297941c5b51c01fbbb85	19499	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T004950-hwao-report.html
18734d3fdd389a1e000ffed169652a61d1a6cdcd695b201d7798b236f296fb9d	8213	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T080428-blanc-report.html
b832d6104df258bf8bed779d24229ce0ae49974f65e6026ce678e4a547f08b29	6264	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T105930-blanc-report.html
7dcf8e2ba41917e28987cbaf3317766499b361310030133535b2bff29bdeca77	13098	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T145923-hwao-report.html
f11078cce4e69efa4f59d37fd3681e18243cad80adce59571c99ca79588da0dd	10490	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T151249-hwao-report.html
849829d266274149e6a9f1d4fb22200929cbd218b3adef291502fdc07074cb87	11983	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T151843-hwao-report.html
1071f27aee6325973e0b04664274568e8fdbbe4345f8576ee3f85b109421ca27	9051	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T190931-tori-report.html
51216d69a089dd4240c5b75e9ea5f737e4faa4b4b140bb2c3f26a68ce9ac7a14	10135	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T200910-tori-report.html
a93fe2cec33b675dbeaf48cb55a3fe7627fa1f9fe77d2ac05f8a40f58335b1e4	8443	/Users/duhokim/HermesOps/reports/status-audio/report-20260821T210530-tori-report.html
5371e1b10c9f0788beace688dd25d157e7e280a6032b99e6d290f945765e6817	1890432	/Users/duhokim/HermesOps/reports/status-audio/response-20260810T1420.mp3
22d4e8075889fc07ae5891f774b017a35510d341f0a87ae44a998ac4bf890192	1959	/Users/duhokim/HermesOps/reports/status-audio/response-20260810T1420.txt
72c07c54f30875b1ca867b29f1842b5fd8011c9ad3a24c401c330b552dd614a8	1538688	/Users/duhokim/HermesOps/reports/status-audio/rev4dispatch-20260811T1431.mp3
6aa6d9f3797fed1ff5b7cbc3f6fc7e575d0e19bf0e526ab6d6a99d2133405b24	1626	/Users/duhokim/HermesOps/reports/status-audio/rev4dispatch-20260811T1431.txt
bcfa6319ec8488658bf70448fe46df1b9e68987288ca222db1a0aa3848dab7b5	2070528	/Users/duhokim/HermesOps/reports/status-audio/sentback-20260810T2148.mp3
d5481b9b52d08b8174a501f0ee51f7738e8ba49c474256203665375a72d86729	2150	/Users/duhokim/HermesOps/reports/status-audio/sentback-20260810T2148.txt
89594dc0171653be1c53cd62edea9f295cc9f56c7858a1761b41ad5a7a251181	2278656	/Users/duhokim/HermesOps/reports/status-audio/split-20260811T1108.mp3
e16d400ed8f4d770e6274c401b79685206a5d311c74f9f106cbbfcdfa81c42a3	2479	/Users/duhokim/HermesOps/reports/status-audio/split-20260811T1108.txt
47a69974ab6e77fed2821f037a2e4dc258e8e40267065a3a63605a1f91a01166	450814	/Users/duhokim/HermesOps/reports/status-audio/status-20260810T1049.mp3
d8871fd9b7b6746e402a4ffe7b072f3240722954374c95f0552e2ec8df963e6b	654	/Users/duhokim/HermesOps/reports/status-audio/status-20260810T1049.txt
6ee64aaf6f3f08d54b7e9ed4ae4c0029fc1a6c2d63947c3a0025557fe92bd0b3	501120	/Users/duhokim/HermesOps/reports/status-audio/status-alloy-20260810T1105.mp3
2e702e2302174fb353f7108b8e5b6907a3261a0b83307cd8e9fc5c03fc5f7d30	486	/Users/duhokim/HermesOps/reports/status-audio/status-alloy-20260810T1105.txt
79476c2d7a55f3d15dd5d37da86cbdb35d3d11b916fcc7be7022e39f3c4b9bb7	2961792	/Users/duhokim/HermesOps/reports/status-audio/torigate-20260811T1050.mp3
7b801445443f544d4e209870cadd07d5ffeb11ab29995f41cda9777e704b0233	2741	/Users/duhokim/HermesOps/reports/status-audio/torigate-20260811T1050.txt
db498a10e4a89c4fdf946d2bf3a4ff359b17f54b4703350617d2553bded1a797	2198400	/Users/duhokim/HermesOps/reports/status-audio/torirelease-20260811T1312.mp3
7d24603a2338d547960953ea6d7736c875ee3f43ba28ae77ea5fbc2ff10d2029	2298	/Users/duhokim/HermesOps/reports/status-audio/torirelease-20260811T1312.txt
879fb1c3b5d59a44892e24d0ca9d4ce2a9bc32c4ec23b09f632b4a05701b5273	1056000	/Users/duhokim/HermesOps/reports/status-audio/voice-input-20260810T1444.mp3
01831a8e3545fcf06b30bdcbf55fb79ca1c80ba7b6af999448217691bd1d2d11	1028	/Users/duhokim/HermesOps/reports/status-audio/voice-input-20260810T1444.txt
d1e6c05ec6476c620b0bc3c5d629922b7ec1e2ebecffa5eeb35f6c42d7c15365	706	/Users/duhokim/HermesOps/reports/status-audio/voices.json
5d1905dc2281465af7338e25a2b15a892faa82f09cb380e1af0134516dc28a70	1393920	/Users/duhokim/HermesOps/reports/status-audio/why-method-only-20260810T1440.mp3
665c9bfe39e36a5c4af1899887d307be681c7ce8ca58facb96319aad5227802f	1539	/Users/duhokim/HermesOps/reports/status-audio/why-method-only-20260810T1440.txt
70e9983ede8d12b1336158254a49bb37817b14a1077edac5d1ede51ae461580d	35781	/Users/duhokim/HermesOps/scripts/nm_audio_index.py
a537c0554446dc632d4c06f1306f3a49bef8e7583109d447623bc2f856613f05	12219	/Users/duhokim/HermesOps/scripts/nm_audio_publish.py
9d6f2ef7dd75c6a0662239cf940a18259630432d444a912badb2046920c9cab3	5693	/Users/duhokim/HermesOps/scripts/nm_audio_route.sh
df2550e01682547f188977adad28710eb64c3535c7b6938acdbd11d825c5a347	10218	/Users/duhokim/HermesOps/scripts/nm_caption_norm.py
b19549b2941055818df361b1d81deb8db4cc285461045c9ae28e63d2a7884462	6812	/Users/duhokim/HermesOps/scripts/nm_disclosure_audit.py
9480c11da0cd79724fe5615cb69b7a430e9f018bd355a3a4d9069ca57d86e2e1	12222	/Users/duhokim/HermesOps/scripts/nm_report_page.py
51bd298e8b426ae4caef016871ef5623520976088afeb163ee91baf53da83627	8812	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/blanc-ops-overhaul-20260820/CAPTION_CORRUPTION_20260821.md
79d89c9d0c5232e572aec2650c3680e55904f58f9b4c2d63286b8a1c5a8fac31	5255	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/blanc-ops-overhaul-20260820/DISCLOSURE_LEDGER_AUDIO_20260821.md
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e	10057	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_CUSTODY_RECEIPT_20260821.md
f5d7f276d666867f70f6eba388793496adff96e5ec293f162b43976c87c76fb2	2992	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/CHI_DISCLOSURE_ASR_FINDING_20260821.md
19fd035945a2637b04ce15eea549242a4fa6f94178984447576a3ae2161ba083	117105	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_CHI_CUSTODY_R6_20260821.md
a8f5c207eb1a1f3069705d5f5c42725c079f5d17c723d76519c5f43095e4a0aa	23903	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_20260821.md
1cf7ba7780a556428e691d76bb54e08949fb375eb7a3112257ff7986a100ad01	36764	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_FINAL_20260821.md
59e37df9177dfce5a8efac5abf223bc66d7d8ceb441d81c781135d0b67426066	18434	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R2_20260821.md
c1ad25fd6574bb9bf3386d8d6fb7448ed62015384035f9110dbde3e94ec0c453	24867	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R3_20260821.md
c9a144e256d2c7ef6c63d11c60b5002e25c7268483a4dc0bbd112ffdfeb24707	30942	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R5_CODEX_20260821.md
ddffe06cce8e41a3601931e36a92fc8d83d3aeff3c09be4cc6765311295ccbe2	21165	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECISION_MEMO_R6_20260821.md
94ac81d7bef75b8a7daca1abd515ceff4fff31c6f21d2c2ce7375027d9c4e79e	15172	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md
1cea208740e3be5ff4a270d3e322a0b2407dbd527b9ef60eb818109b506d6ac1	12861	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_FOOTPRINT_GEOMETRY_20260821.md
aadfb27e3e6f90867e159a3a0d3ca72c2b850b53de2b7d44757876331c07902b	23416	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
38e789547e750d21b38fd9d1fa3515bc44ed8f95d542476183d45274c7518b3c	22552	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/GATE_VOID_ON_DESIGN_DEFECT_20260821.md
6b2aa9a54398e53ede9545e1df9d3fc63d32aa95a28a9799b18be341d4eacce7	12167	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md
f8447142420f10023beab265f92648dcabc1af1f0b340ef00855ecc8e3a162ee	4821	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV1_SUPERSEDED.md
a9783371a885e1581780aee8a101ad7032be65583cdeb3b842c53282382d3c76	8490	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821_REV2_SUPERSEDED.md
c10687595f1f4313272c66b78da4225f77b6a665050d71751f04797e52edab69	3710	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/K8_CROSSING_AUTHORIZATION_20260820.md
879ec60426eaa5db6b28dc0a971e853ca09a33df22a1dce31aca215c4d1b246e	10057	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/_gated/CHI_CUSTODY_RECEIPT_20260821.879ec60426ea.md
7136960fcb89ca9f7e3234c13b2604535cfa8ca005ad6b7cda2bf9b41c1946b7	526	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/_gated/GATED_SNAPSHOTS.jsonl
94e941093c716b5a1a276a30a270a477b4aec7893d758b5f6edb336ea86a2ba3	6985	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/build_custody_tables.py
f89cf2a463d27b19f9f0eac682e86aa2e73c3332ba707003d491c6566bc1fff5	1563	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/gate_snapshot.sh
d928dd1f65d4293e2a64424f46e46308676c8898f14e1e9e94fa8599d5936ca6	4321	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_custody_20260821/tables_R7.txt
59b85f818d0aeee58cd3972dc83ab71e9427cb270d66148293eb7c0fcbd2c817	1408	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt2_hold/hc1h_prepare.command.json
2fdcb164800d3dabcf75ca4f1b6439c88ef1c438e14a1f13de3e35eab9e26883	1953	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt3_hold/hc1h_checking/commitment.json
59b85f818d0aeee58cd3972dc83ab71e9427cb270d66148293eb7c0fcbd2c817	1408	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt3_hold/hc1h_prepare.command.json
9799d08eb4799e4710edc827ae2c17a7885810afa8d3ba2ea058a40c1da5a8aa	2056	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt3_hold/hc1h_prepare.stdout.log
e9d77ba140872a995a0a6454bcc12d5767f74ff4760e166227d1dccbb2d822af	1754	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt3_hold/hc1h_private/prepare_receipt.json
358c8ec9bfb874ac71d60c7b53cb1d304eab95cdf9647870eadec4da5dcdf712	11992	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/attempt3_hold/rehearsal_summary.json
4a2e01407752f9c183898063e49ba8101c97d48db604a44f958452acaaaac15a	1952	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_checking/commitment.json
59b85f818d0aeee58cd3972dc83ab71e9427cb270d66148293eb7c0fcbd2c817	1408	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_prepare.command.json
eb4ef2eb1d61634d166beaed35727b49f2374b87124a97c945c40240677db04f	2063	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_prepare.stdout.log
fb10e2d26f5bbe76a392850aa9e3db1195571749153fa25164ed5a3731179a9b	1761	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/hc1h_private/prepare_receipt.json
654328db388aeed620ba674029a641bd60a94fd4988b46f9247c9560b5c16bbe	12424	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_rehearsal_20260820/rehearsal_summary.json
9e8d50af4d81648bd4f763dbdb560a872bf3ecf5246f98330a50c16702888e2c	62682	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_final_audit.json
c98ccf9547425825b2164977ef5c9d3aff4251a638cc7930d803c9eca8e09789	11276	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_final_stdout.log
2001b8dd10765d78a872e68b08320d5feb5f9272a497946f74e9b566e5fd2c95	13621	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_memo2_stdout.log
442f33261e729627132823b804e038a0f4416a5011ffc232ce139ec065f7b1a4	53779	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_memo3_inventory.json
da9d374718458402a39de06696b10954e3fc18959e105d9590ab4a4f46b3b849	15490	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_memo3_stdout.log
2f217d842beb8af715ce364d8819b7992471302ee5a16a8902c8c0d68dac994e	12291	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_memo_stdout.log
bf60bd74cd005b741bf0ec057cccc4ce4dee1242a92bdc7ec73ef031b09fc6c5	8444	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r5codex_stdout.log
916eb6d4262e9fba8896afcf2d617ac825b13de72fff64b2db03cf9fadcf5636	282773	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_audit.json
ae3415cba99cc66125b92d23fc25e2d4cd965cd38d858f9b2582654a41ee4e5e	18351	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r6_stdout.log
89c3e4f04f334b319bb3e7cea7d3dcdad9140fad9f728dc47457a3441259c6c2	234062	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_151843_tail.wav
5e28db6d98cf23dbb8b916bf40ed2b176366a657d04a42a6e7689d1df80c438e	31137	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_fresh_asr_beam5_adjudication.jsonl
1a0a08b05cd2f4164ec81055f962121d0533fa48ef6fe5950b2a6724677e3bbe	3384	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_fresh_asr_beam5_adjudication.py
6f26696e3332962d036bb8776816ebbc695860381522b85be499085193354536	372	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_fresh_asr_summary.json
c12b01df6b005218e8e1380ed0b43f7e5e99a3602796053a3f05bc2d6657f5a3	479048	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_fresh_asr_sweep.jsonl
2ac8cb68b8764f089e4e055c546dfca32004d40c39e949ee1efd388b5553d0ad	4314	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_fresh_asr_sweep.py
abe495269b350b0ffe0c21e6539d89d4be69a11a276bff8039436bd735ce26da	707	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/chain/_gated/GATED_SNAPSHOTS.jsonl
8f7f29c1403941fa6d18cb569238d53c5c85fba4cbf67389b6bb99fb875b3641	13	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/chain/_gated/item1.8f7f29c14039.md
372ce9903da36c3c6c765ea0138a1587f1a0a68d1ae632de63ff5cd9aeeecc12	13	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/chain/_gated/item2.372ce9903da3.md
0eb9018c4ae523b533ea54fc94ca87f176afd32d3717ac1982cd3db2632338c5	13	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/chain/_gated/item3.0eb9018c4ae5.md
f89cf2a463d27b19f9f0eac682e86aa2e73c3332ba707003d491c6566bc1fff5	1563	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/chain/gate_snapshot.sh
8f7f29c1403941fa6d18cb569238d53c5c85fba4cbf67389b6bb99fb875b3641	13	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/chain/item1.md
372ce9903da36c3c6c765ea0138a1587f1a0a68d1ae632de63ff5cd9aeeecc12	13	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/chain/item2.md
0eb9018c4ae523b533ea54fc94ca87f176afd32d3717ac1982cd3db2632338c5	13	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/chain/item3.md
73ff5e89931be54ee47d340fc0bbd3089d649f8e7c8af6f9b58da2231528e77e	193	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/full_digest/_gated/GATED_SNAPSHOTS.jsonl
cca7462e269c4e4049a7b5db7ef5def73609d5aa08a639cd9c2b2a9798ac463c	30	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/full_digest/_gated/sample.75afc22e9a06.md
f89cf2a463d27b19f9f0eac682e86aa2e73c3332ba707003d491c6566bc1fff5	1563	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/full_digest/gate_snapshot.sh
75afc22e9a068d97c5142edfc652023f864467bf5cb29e6b08beb609328132a1	22	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/full_digest/sample.md
c9aa94af64a8b08c49455d23bee86d11cba6c99d5030a046a02eea5de2de23c5	193	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/silent_chflags_failure/_gated/GATED_SNAPSHOTS.jsonl
33f9985b24d580de75481d3b6c280dd790fd5601e37faaab9fc385169e68c598	27	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/silent_chflags_failure/_gated/sample.33f9985b24d5.md
275239824e00e61b0a220e61a41791c7e9b4bd726f8b0c27077a338f8131c9dc	17	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/silent_chflags_failure/fakebin/chflags
f89cf2a463d27b19f9f0eac682e86aa2e73c3332ba707003d491c6566bc1fff5	1563	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/silent_chflags_failure/gate_snapshot.sh
33f9985b24d580de75481d3b6c280dd790fd5601e37faaab9fc385169e68c598	27	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_ours/silent_chflags_failure/sample.md
da0fcfe4afcfd7cc931cb63ef718d505c527a8a4b7de528ecf34faedb52a0840	6859	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_mechanism_test.py
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/.locks/models--Systran--faster-whisper-base.en/15d7bdf9ba25718ca2504eec6a8f02bc55af0a6a.lock
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/.locks/models--Systran--faster-whisper-base.en/2a166925539a16005f14ff328359f9b9adb9dc4fb631bb3b227526862e93e2ef.lock
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/.locks/models--Systran--faster-whisper-base.en/594369787efe617005d199b03739ee0ead7e3ab7.lock
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855	0	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/.locks/models--Systran--faster-whisper-base.en/ee695b8d3e3c10d488304e04468efec4ca27554a.lock
f6572428f6d5e1575e73a1502895a8731f10757dfbb634909c6e154b849af91d	191	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/CACHEDIR.TAG
929c5252409436dce1b38a75d1abbcb5e132d170d8e324e4e04ed915fa2d22df	2128466	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/blobs/15d7bdf9ba25718ca2504eec6a8f02bc55af0a6a
2a166925539a16005f14ff328359f9b9adb9dc4fb631bb3b227526862e93e2ef	145216508	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/blobs/2a166925539a16005f14ff328359f9b9adb9dc4fb631bb3b227526862e93e2ef
f3bc3821e9fc76a27bae538e11ae5b677dcdd352b4600429ce7951d398569aeb	2227	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/blobs/594369787efe617005d199b03739ee0ead7e3ab7
ff77588746d3a2595d32ab5b69ffd7b95ce2441ac57533cb66fc3eb575a115cf	422309	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/blobs/ee695b8d3e3c10d488304e04468efec4ca27554a
6d29381afa6556bf89e1d7dc6dc871c7ff071a4baf973695559b4e75724d5259	40	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/refs/main
f3bc3821e9fc76a27bae538e11ae5b677dcdd352b4600429ce7951d398569aeb	2227	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/snapshots/3d3d5dee26484f91867d81cb899cfcf72b96be6c/config.json
2a166925539a16005f14ff328359f9b9adb9dc4fb631bb3b227526862e93e2ef	145216508	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/snapshots/3d3d5dee26484f91867d81cb899cfcf72b96be6c/model.bin
929c5252409436dce1b38a75d1abbcb5e132d170d8e324e4e04ed915fa2d22df	2128466	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/snapshots/3d3d5dee26484f91867d81cb899cfcf72b96be6c/tokenizer.json
ff77588746d3a2595d32ab5b69ffd7b95ce2441ac57533cb66fc3eb575a115cf	422309	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/snapshots/3d3d5dee26484f91867d81cb899cfcf72b96be6c/vocabulary.txt
95d5297b1407c253c02476a3e059b8a52d84b74161cb9d18fbb9a32d6f3101af	836	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tmp_gate_r7_whisper_models/models--Systran--faster-whisper-base.en/trees/3d3d5dee26484f91867d81cb899cfcf72b96be6c.json
9cae2d68b3c10b9ccc794f0a031b061b33a1fc15bdfee54abd01e24b069d2ba8	3464	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/hc1h_full_test_stderr.log
65c04377734e3cd881bcb4144ae6652c1764429a189f352993033f9639765cd4	161895	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/nm_handcheck.py
148afbf593dcf19eaf7213a10593fdc993281c3d8d6ba66f1f9034d72207e94b	1776	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/superseded_hc1_20260815/full_test_stderr.log
ffa2910edb610892f7ca742feb0756f3ed212bf79b48e58f8c2ee2bd5e97fc71	69590	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/handcheck/test_nm_handcheck.py
5b91b8d7b5a8135950b6b829632b8b568dafe9780776016f2311543e6215a9af	347	/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/run_hc1h_stage.sh
```

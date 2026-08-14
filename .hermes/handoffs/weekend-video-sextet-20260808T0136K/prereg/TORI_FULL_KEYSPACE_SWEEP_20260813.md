# TORI — Full BRICKID keyspace aggregate sweep

**Receipt rendered:** `2026-08-12T20:35:09Z`  
**Status:** `COMPLETE FULL-KEYSPACE COUNT — ZERO-TAIL CLOSURE`

## Scope

- Frozen `BRICKID 1…121000` certificates are inputs only and are not modified or re-queried.
- New one-pass scope: `BRICKID 121001…662174`. Each block returns the existing Cut 1–5/availability aggregate chain and both Cut 6 branch counts in the same one-row response.
- Cut 6 predicate: `POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551`.
- Stop at the first of keyspace exhaustion or `2026-08-13 06:00 KST` (`2026-08-12T21:00:00Z`).
- No spiral fraction, retention factor, or other external factor is multiplied into these catalogue counts.

## Running keyspace count

- **541,000 of 662,174 BRICKID keyspace units counted = 81.700580%.**
- Contiguous completed frontier: `BRICKID 1…541000`.
- New landed partitions: `42/55`; new landed keyspace units: `420,000/541,174`.
- These are BRICKID keyspace units, not sky area, footprint, or an equal-area statistic. Out-of-order landed blocks count only as their exact disjoint keyspace units; contiguous coverage is reported separately.
- Every incomplete total is a **LOWER BOUND** formed only by summing frozen baseline aggregates plus landed, non-overlapping one-row blocks. No density extrapolation is performed.

## Zero-tail closure and completeness ruling

- Direct full-chain measurement covers **541,000 of 662,174** BRICKID keyspace units = **81.700580%** through `BRICKID 541000`.
- A separate aggregate-only existence probe measured the entire remaining `BRICKID 541001…662174` tail (121,174 keyspace units) and returned **`n_join_rows = 0`** in one hash-verified row.
- Because the probe uses the same frozen tractor table and photo-z left join, zero joined parent rows means every downstream Cut 1–6 count is exactly zero throughout that tail.
- Therefore the directly summed Cut totals were LOWER BOUND values before the probe, and the tail proof establishes that this lower bound equals the exact full-keyspace count over `BRICKID 1…662174`.
- This is catalogue BRICKID keyspace, not sky area; it does not measure an equal-area footprint fraction.
- Tail query SHA-256: `50900d60ee92deeef326fd190cc0aac0a9f799113e688789a784d5bb649fcccc`; result SHA-256: `7af4c409d3b81c4985e70b2368becb88fe53e9a99c8d39b21c3e465d1e5dca18`; UWS job `https://datalab.noirlab.edu/tap/async/nf67a6hqa9rq0z77` ended `COMPLETED`.

## Final stop reconciliation

- `status.json` records 41 completed blocks because its last update was `2026-08-12T20:07:02Z`.
- Disk custody contains **42 authoritative** receipt/result pairs: the 42nd completed at `2026-08-12T20:07:07Z` after the stale status write.
- That stale status also records `stop_reason = None` and `finished_utc = None`; neither field records the parent process's later termination.
- Cause: the 42nd full-chain result had COUNT(*)=0 and SQL SUM fields serialized as blanks/NULL; the orchestrator converted a blank with int('') and crashed after the receipt landed but before status persistence.
- Classification: runner crash after the 42nd receipt landed; not deliberate, not deadline, and not keyspace exhaustion.

## Full aggregate chain — frozen baseline plus all landed blocks

| Aggregate | Count |
|---|---:|
| joined catalogue rows (`n_join_rows`) | 2,827,055,986 |
| Cut 1 primary + mask (`n_cut1_primary_mask`) | 2,584,542,900 |
| Cut 2 extended + positive R flux (`n_cut2_extended_flux`) | 1,317,374,704 |
| photo-z joined after Cut 2 (`n_photoz_joined_cut2`) | 1,317,374,704 |
| Cut 3 photo-z (`n_cut3_photoz`) | 11,762,815 |
| Cut 4 raw magnitude (`n_cut4_raw_mag`) | 1,015,450 |
| Cut 4 dered magnitude (`n_cut4_dered_mag`) | 1,162,237 |
| Cut 5 parent raw (`n_cut5_parent_raw`) | 903,913 |
| Cut 5 parent dered (`n_cut5_parent_dered`) | 1,015,881 |
| raw all-band nobs (`n_raw_allband_nobs`) | 903,913 |
| dered all-band nobs (`n_dered_allband_nobs`) | 1,015,881 |
| raw all-band ngood (`n_raw_allband_ngood`) | 903,908 |
| dered all-band ngood (`n_dered_allband_ngood`) | 1,015,874 |
| raw all-band inverse variance (`n_raw_allband_ivar`) | 903,913 |
| dered all-band inverse variance (`n_dered_allband_ivar`) | 1,015,881 |
| raw shape-valid (`n_raw_shape_valid`) | 865,902 |
| dered shape-valid (`n_dered_shape_valid`) | 970,089 |
| raw native covariates (`n_raw_native_covariates`) | 903,910 |
| dered native covariates (`n_dered_native_covariates`) | 1,015,877 |
| raw all countable availability (`n_raw_all_countable_availability`) | 865,900 |
| dered all countable availability (`n_dered_all_countable_availability`) | 970,086 |
| Cut 6 inclination raw (`n_cut6_inclination_raw`) | 749,914 |
| Cut 6 inclination dered (`n_cut6_inclination_dered`) | 832,393 |

## Per-block landed aggregates

| BRICKID block | Elapsed seconds | Cut 1 | Cut 3 | Cut 5 raw | Cut 5 dered | Cut 6 raw | Cut 6 dered | Query SHA-256 | Result SHA-256 |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 121001…131000 | 678.0 | 55,756,107 | 173,013 | 13,018 | 14,398 | 10,818 | 11,839 | `73d4b931833504aa31cdd8a68ba3d52f0f263337233045de371adc3c1c19d716` | `be6e6c17317dd198c634b95107ceabe0da65aaacbbcf01ef9704ef8f8dddcf60` |
| 131001…141000 | 678.0 | 57,304,861 | 191,047 | 14,986 | 16,482 | 12,416 | 13,507 | `2ddaf04022fa0e8ced118c7cd3b017a87edd9a2a09c1cce3d5b04c1a11626e57` | `1210348265f48edd746c4a7eaf96b9b7b7e837b166ba96b79339078bb020b35f` |
| 141001…151000 | 693.0 | 57,312,169 | 208,671 | 17,001 | 18,671 | 14,164 | 15,421 | `6382fd354476e5fe605a603b52100208edc979b6fe5376c9e4309823ccdf21f3` | `7866290e07b6cb3552758ebf1442e4b66a48246822e06c2a109d7db6d77455f1` |
| 151001…161000 | 646.0 | 54,781,854 | 198,410 | 15,721 | 17,433 | 13,096 | 14,324 | `c98511d24c0d95be24161063349ce9a9a1f2e2e435503bae3d4614badda5db6b` | `f086131b75e1957ad378851931c895c9244f812899b8667d632da6213826d609` |
| 161001…171000 | 662.0 | 55,739,572 | 205,719 | 15,880 | 17,844 | 13,291 | 14,778 | `fc6fe3dc24f2a49a6263074f5b3375a48dd445d0545332a6c9aea1210a8162bc` | `544e09b158a86c7c99107fb6d8b504cd622c312e2237024bd0ec6ff7ca6c8710` |
| 171001…181000 | 662.0 | 56,427,127 | 200,594 | 14,720 | 16,657 | 12,272 | 13,719 | `95de3c87b055f2b623d901ea0881706cbad1f5fe93729cea837719f37149de2d` | `86911d95ebb42ea9f4a77c8ec60b9a1827d02e66bc5f3abf218e317cc8e7b9e6` |
| 181001…191000 | 567.0 | 55,117,999 | 209,382 | 15,190 | 17,216 | 12,626 | 14,143 | `0f97694d1730ede189ca1a4548323ffe1d6f345ac98245c82b7756ee88eac4e8` | `9aeb33d15742ac581908615f3c5a9fd52b917bb78ed5278c12feae34b753137f` |
| 191001…201000 | 529.0 | 54,332,692 | 194,296 | 14,159 | 16,282 | 11,800 | 13,353 | `1d6fa2c5fa58ec66d0b56cb704b7248cc9c82a325c11087c97cc55a6fb645c78` | `8487386d0f7aef78bfbb69d612238e9ba19683383d59a683194c57edbedc5abe` |
| 201001…211000 | 568.0 | 56,383,353 | 191,125 | 14,929 | 16,801 | 12,399 | 13,759 | `2a39c856672f425a4e673045d33b5f212fc73dc90a55be0ce7539543071be28c` | `4a732b85650a61028ee708a2f3c3df0db410b63ed67fe6824776b6d8e44971c3` |
| 211001…221000 | 613.0 | 53,326,350 | 198,022 | 14,547 | 16,802 | 12,073 | 13,755 | `c7c7e48828d588f099c6eba903fc13bc71f4e099a4e7052f2b640ec7492fc2cf` | `216d5639948bb13d873764f720016117dcf2a4652aff54b4726d11a16c6ee960` |
| 221001…231000 | 570.0 | 51,957,660 | 202,666 | 12,857 | 14,910 | 10,560 | 12,067 | `3f39167736336ba2cff4cb9488c258dd287a553b0ce90ee5f16e6e92291d2a98` | `1dbe1365fb36e7d095c6bb8974978a71f929456893f45036d673a0b7e1264f09` |
| 231001…241000 | 569.0 | 51,271,464 | 182,954 | 14,363 | 16,268 | 11,910 | 13,263 | `dee0d948c92bee076b3b21dd9d85ce00e494147c9fc113605f39d891dfbf31b2` | `8746475a74072a171a99d5330cc99c83af364a76e91a97b9ddc054407932f423` |
| 241001…251000 | 537.0 | 49,562,828 | 202,008 | 16,236 | 18,500 | 13,417 | 15,059 | `02e5938fe63af91a6b668930f0545e31a4af4c0cbc48b1455a591daeb54e5f61` | `58c9775c4e46796f1f947a81a63335a4b032d17f684a5452f4616fccef90557d` |
| 251001…261000 | 630.0 | 53,275,731 | 235,064 | 18,921 | 21,345 | 15,612 | 17,368 | `10001688e151c118db0f02075444539b140bedc3c703a84b6e61a2b8bce58f9e` | `3d0f2224c7c5cb1f7d85c4e78656bd88e398379a4970a73dfad5f8a435ee6279` |
| 261001…271000 | 677.0 | 52,821,873 | 230,531 | 18,222 | 20,495 | 14,964 | 16,629 | `97cf2b192ab1cc682db6e461d7579e4a18707bf87d1f8464ac84b044f190a108` | `04fc43ec613474f8e77ee5d1810cbcba1bd2690e6323e852c05dc953ee1bcdce` |
| 271001…281000 | 646.0 | 50,806,329 | 242,057 | 19,158 | 21,397 | 15,838 | 17,435 | `cdf20d05317f4869ca59a0718d6f2e4c98fb9e4897557adae65143d169cd53f7` | `c89cf7756556ec34db40a46f18cf0b80bb4e8f48fa463c030083f484885c9efe` |
| 281001…291000 | 583.0 | 53,187,111 | 272,692 | 20,549 | 23,064 | 17,150 | 18,984 | `ff5ee83ee35376d7737cdf970043ae335274b31513efbf92ad54af9e7c400962` | `acdaf13bfa578e992f39712887de7919f1a83bf305229743ccca23b8d33e97c3` |
| 291001…301000 | 709.0 | 57,326,897 | 258,126 | 19,213 | 21,591 | 15,964 | 17,733 | `a9d9ddcf28ed19233365a95a08022ce27405c8beeec611e1ed88d7cbd1c8073f` | `2477c2b1dd2a4628c6a87fdc0c6dff29f79c3deeb403185fceb17ffc45e2ed10` |
| 301001…311000 | 631.0 | 58,034,277 | 256,627 | 20,595 | 23,052 | 16,987 | 18,806 | `c9d00e08139d79d3a3d2d7b0de5aeba2eb1d92a5896d0ef8ec25e17fb7d8191a` | `f2a7f2ac7982d1deef0bcaf98caf898ae813a45c795c2841515eaebc5434c02b` |
| 311001…321000 | 614.0 | 58,656,290 | 262,095 | 20,837 | 24,688 | 17,468 | 20,611 | `0c04fed516c690bb72ecdf72aed245c05684e09cece81983c81da8c1afc02337` | `c95e8c1919c28be9acd0a8168a9ea530dab98d8647eec7a96cf9869ef3f0136a` |
| 321001…331000 | 694.0 | 66,985,412 | 266,526 | 20,557 | 23,264 | 17,403 | 19,374 | `8229f3d3954740dfc5b3c06a34e6fe8d1327f9db8ad9448605e7ae8682fc05e3` | `d3998f891928377c043a43e39907057b617b06552fd1c63d81a1bdba3438b5d8` |
| 331001…341000 | 662.0 | 64,856,473 | 275,579 | 20,946 | 23,588 | 17,668 | 19,638 | `9b614875286aedbcbcbd4be1ad699aadd8dcc4e8c794f01fb139f8c1f44893b0` | `a489fc5776fe041d51a9dd17bdc41b3804caa398eb11fe75def00579b0ad85ee` |
| 341001…351000 | 568.0 | 55,906,844 | 263,768 | 21,020 | 23,607 | 17,417 | 19,310 | `8de57c8acf4a5913042c2bb56e89f4099b0b35c61b9494fde7c08bc584b597d2` | `31662fa4e31ac87aea19a1b43a372fcc6a16f237081c08d588a72ec419db21e8` |
| 351001…361000 | 568.0 | 51,687,674 | 256,792 | 20,550 | 22,961 | 16,973 | 18,666 | `a528968b96a4bf939b2a5f049504bd276f39722ae1c607f8d4f9b9f90411408f` | `5ce101b4d94b338c0343743d28cbf5401a387bf709dd7a3d4f8122c862a7deec` |
| 361001…371000 | 536.0 | 45,949,895 | 263,190 | 21,735 | 24,548 | 17,996 | 20,040 | `78054c4d3a34efeafa945c405b59eb8c614ac586a0723a29638533a7c66c0779` | `74cd3582f5be67bc1554dcf732f1c720e6ecaec7d10d9104908fd5820634000a` |
| 371001…381000 | 537.0 | 42,444,435 | 259,823 | 21,117 | 24,104 | 17,426 | 19,608 | `cb4ab218cf8feba55111645f28673852e4f9c039439c08de789faff3ce859db2` | `71d36dd188865ede9f919e18cc24709e2804768a1a18d539d349fed6d3bcadb9` |
| 381001…391000 | 459.0 | 40,182,758 | 248,585 | 19,602 | 22,824 | 16,337 | 18,698 | `b059a29d279186a4ac2931160e868bda8d2351decbe9a89aeea9b2ed95f1201c` | `9fb23e90d9e2626be86be8d4992ff7f2f0f2fa9dd7505f77ad9c9ae20688e722` |
| 391001…401000 | 412.0 | 38,666,899 | 237,442 | 18,216 | 20,973 | 15,071 | 17,088 | `2a9e019d4e4d51021e7a365edc869beedc8f9d21ed1fbed18af3724fb48ecd0f` | `d4fae7e25710d1387283313e239e59387104f5e73325fee366cac8236099331c` |
| 401001…411000 | 427.0 | 40,314,062 | 241,057 | 18,032 | 20,303 | 14,948 | 16,572 | `40c2d267478cf60c40e37da46f9daf620bcf3a385b84e27713855c4c9b21892a` | `be9f8bf97f71d21433e987e76e7b3da4cfd64c1feed3e29e860c5e4a35f4f699` |
| 411001…421000 | 410.0 | 38,029,904 | 247,009 | 19,559 | 21,857 | 16,202 | 17,866 | `7f592bcf85357fc5e9767dcac735eaf4e1f034f572e394f32f0d7b82b89c1284` | `bf9676705911e02b52b3d71ce4087f07ad815b2bd30e850fe9bce168f64e23af` |
| 421001…431000 | 459.0 | 37,013,705 | 243,440 | 20,026 | 22,247 | 16,501 | 18,137 | `9929147d8780299a458f162fec22d6fcad156f78a893eb20c36c71bb1c13bdeb` | `0a90746553e2bc7b08010dc97fbff9d660bbee4880eebb88493e5dd51033e22a` |
| 431001…441000 | 460.0 | 36,312,078 | 251,274 | 20,438 | 22,691 | 16,702 | 18,327 | `3d74299d8e732f428f43e007bfcf61def0549703d924420a233d3c3f5a92e390` | `4e1c9c6c895b6b1386a5099c75f19e8e058630e609cc9c9cab7c7e4935f60e71` |
| 441001…451000 | 443.0 | 36,462,158 | 250,018 | 19,414 | 21,736 | 15,974 | 17,675 | `cd7ad1de57a3d84deaec579f0ceb372ab40d3005f5c9d57ab81aa887e122b5a2` | `76330fc9edc62059d997b311cbd7d7dde10715ff8e92d10af12e99a80f8f7cbd` |
| 451001…461000 | 473.0 | 35,463,471 | 235,795 | 18,585 | 20,937 | 15,333 | 17,067 | `8ef2f82ac436a57325cbff811239830e0531afef7c86f89d35716fcc2ed340e0` | `e6075fae2834fff936e1619dfa56a8f5048f019bb5a0cec2daa204e36d8aeb61` |
| 461001…471000 | 443.0 | 35,137,465 | 238,557 | 19,644 | 21,767 | 16,205 | 17,732 | `0c2d5adfa3254550ba395c601fbbe53ed63b2a2d0765605ca49708bc6ee40d88` | `ef07ce2cd8de2a941cbfbcac0a9b6dea6e57e65f43d0732eefb00c6ed60f9095` |
| 471001…481000 | 443.0 | 34,971,600 | 241,056 | 19,881 | 21,954 | 16,359 | 17,814 | `04050ac15300769c0b874b91407d9be65302cecd688e9c6187c58319afed2673` | `19994bb68e46821411907fb1f29b2c7cf66f84a9beebd74241fa95e3bf42c6da` |
| 481001…491000 | 455.0 | 35,431,460 | 248,096 | 21,188 | 23,306 | 17,558 | 19,058 | `874b9c238224bfecab37617a08cbf64c479f0bee6bb3153647cd06a6aee6629a` | `5d7f3fff4175b5f8355abe5000ee3267675c6a40a8c34da697424b5387c69d83` |
| 491001…501000 | 381.0 | 34,201,354 | 236,852 | 19,898 | 21,621 | 16,371 | 17,597 | `02be8f3c56fe5d050c0edd5a80ae48ee797fc87336f0218dd21bb7ba51d26a24` | `718b6e2b95b8b226197fc172303dc8d492f26d915cac42422ffd33fe48a793cf` |
| 501001…511000 | 429.0 | 31,756,728 | 218,676 | 18,035 | 19,570 | 14,746 | 15,855 | `0695f81cd4d3cba8a1cc52bf2311788d117a72d16fc511cfee35ac5855b220ac` | `859b60e315c2c71b1c942ba203936337efac8db69adfc5039115f32160a935a9` |
| 511001…521000 | 224.0 | 14,396,112 | 104,633 | 8,945 | 9,640 | 7,411 | 7,911 | `40673b0e78c876521361437da020a519d685a221bf41ea9b9a684e5a3024f973` | `2fb3f7a90d4b85c59ceecb043693b11849c08455caea9517b9034f5ecb5e87ce` |
| 521001…531000 | 21.0 | 92,872 | 870 | 78 | 80 | 68 | 70 | `8db1845afc8452ddb011927dc5a1061fbc6bdbad94c560a3f7b0a7ec5ff48ee2` | `025babbbd70341de0e91251acfbed7d0966a7cb4003c0c086944d09b52d95646` |
| 531001…541000 | 5.0 | 0 | 0 | 0 | 0 | 0 | 0 | `56c373b8d12226f798c868ba1d3b352cfb880237906d8001e4771f2be9f5120f` | `498a55ebef20fc3bbf23c4f49cd3260b7d581833503ddbf4a53d24a95edbd130` |

## Failure and recovery history

- The six one-row receipts landed before the 502 incident remain authoritative; recovery never re-queries or replaces a landed partition.
- Detected `2026-08-12T14:40:53Z`; prior stop `partition_failure_201001-211000`.
  - Cause: HTTP 502 Bad Gateway from nginx while polling three existing UWS /phase URLs.
  - Runner defect: HTTP 502 was omitted from pressure handling; children exited and the generic hard-failure branch stopped the orchestrator.
  - Recovery: resume same manifest serially; remotely lost job URLs require fresh submissions for unlanded ranges only.

## Boundary and custody

- full-chain server-side aggregate rows returned: **42**
- sample rows exported: **0**
- positions exported: **0**
- images requested: **0**
- chirality/handedness computed: **0**
- sky statistics computed: **0**
- trigonometric or axis-relative terms: **0**
- bulk downloads: **0**
- publication/acceptance/commit/push: **0**
- Stale `status.json` active-concurrency snapshot: `1`; final live count processes and lock holders are reported below.
- tail-existence server-side aggregate rows returned: **1**
- total server-side aggregate rows returned: **43**
- Service-pressure backoff: `HTTP_502` detected at `2026-08-12T15:06:03Z`; future submissions reduced to serial and active jobs were preserved.
- Frozen parent receipt SHA-256: `df9357085d4cfd35320ab34346a1fb3080dc1e5ba1e3d86e2dc6231dbbf534f3`.
- Frozen Cut 6 receipt SHA-256: `ed6b6e5e957903473c7692d5973f3b2d05a991916ce3aa247365938b0f414651`.
- Remaining manifest: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/partitions/remaining_121001_662174/manifest.json` — SHA-256 `665738a20a9e754ee190297a421a1438d33bb563e53ea67b64feb634c250b7ef`.
- Independent final reconstruction: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_tori_parent_row_count_evidence/partitions/remaining_121001_662174/FINAL_FULL_KEYSPACE_INDEPENDENT_RECONSTRUCTION_20260813.json` — SHA-256 `beb89247c908a42b16bcb944df8e0fa1bcb7398bfdc514bfa80781b890ab7154`.
- Final process/lock closure: **0 live count processes; 0 orchestrator lock holders**.

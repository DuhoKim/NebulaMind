GPT2_OBJMANIFEST_COMPLETE ready=15203 waiting=193204

Object-brick manifest builder is complete.

Artifacts
- Builder: `_objmanifest_20260820/build_object_manifest.py`
- Tests: `_objmanifest_20260820/test_build_object_manifest.py`
- Current runner-schema manifest: `_objmanifest_20260820/manifest.json`
- Current build summary: `_objmanifest_20260820/real_build_summary.json`
- Current build timing: `_objmanifest_20260820/real_build_timing.log`

Current real-receipts snapshot
- objects total: 208407
- objects ready: 15203
- objects waiting: 193204
- accepted bricks: 4683
- distinct missing bricks: 55627
- positions SHA-256: `0edfdef08361f1606f714e59c0dd1472d4d13e357a75df2173824da1ca8ff8ab`
- receipts snapshot SHA-256: `1dfbc5e62c8ccc89ed968cb2bbe59b01f506e41c61dfc3342af1dccfd75f82fa`
- geometry sidecar SHA-256: `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`
- reused pinned adapter/planner SHA-256: `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- output manifest SHA-256: `5ba0afce24d42557b1bb828685d05ac5a327a6d402d9dfae53399226fd39ce99`
- build wall time: 202.13 seconds

Top-10 missing-brick histogram
1. `2631m765`: 176 waiting objects
2. `2595m770`: 140 waiting objects
3. `2599m787`: 85 waiting objects
4. `2620m765`: 85 waiting objects
5. `2599m772`: 81 waiting objects
6. `0222m735`: 78 waiting objects
7. `2641m765`: 75 waiting objects
8. `2595m777`: 72 waiting objects
9. `2572m800`: 68 waiting objects
10. `2588m772`: 62 waiting objects

Verification
- `python3 -m unittest -v test_build_object_manifest.py`: 5/5 PASS.
- Certified planner exercised on edge, four-brick corner, and three-source T-junction fixtures.
- Receipt completeness, rejected-receipt exclusion, `--only-bricks`, concurrent receipt-snapshot consistency, runner-schema loading, and deterministic byte output are covered.
- `_cutout_runner_20260820/cutout_runner.py::load_brick_manifest` loaded all 15203 emitted objects and 17955 brick entries.
- Every emitted entry has exactly `path`, `row:{ra,dec}`, `sha256`, and `brickname`.

`--only-bricks FILE` is fail-closed: an object is considered only when its complete planner-derived candidate set is contained in the supplied brick subset; it never truncates an object's source set.

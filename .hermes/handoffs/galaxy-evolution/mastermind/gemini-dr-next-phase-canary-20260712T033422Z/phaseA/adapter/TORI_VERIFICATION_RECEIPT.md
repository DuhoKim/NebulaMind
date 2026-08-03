# Tori Phase-A adapter verification receipt

UTC: 2026-07-12T03:55:29Z

Implementation SHA-256: `85c543b7043af914c318999fc763b32ac2678460610c94bd4c8df99b31f269b2`
Tests SHA-256: `0ce93ca43edf6dc72caea3b09e24e065a5f635c7abd3e10fcec160f701c65c4a`
Amendment SHA-256: `66116f7049ef534578951b43768954b069556776a793e6d2cd8ffabf94d0ee2f`

Verification:

- `PYTHONPATH=phaseA/adapter python3 -m pytest phaseA/adapter/tests/test_adapter.py -q`
- Result: `17 passed in 0.05s`
- `python3 -m py_compile ...`: PASS
- Static forbidden-surface scan: zero matches.
- Node execution of generated `build_js_probe()`: PASS; output parsed as JSON.
- Frozen named fixture selector tests: running, verification, billing, and login all PASS.
- Review regressions: report-prose verification false positive rejected; challenge URL precedence; exact-target mismatch; JSON transport; exact-target/complete capture guards; safe escaping; href ledger all PASS.

No live action path exists in the adapter. The only live use was Tori executing the generated read-only probe against explicit Chrome window/tab identities.

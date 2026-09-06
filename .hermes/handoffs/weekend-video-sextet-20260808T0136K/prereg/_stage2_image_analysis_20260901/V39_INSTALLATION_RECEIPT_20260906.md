# V39 INSTALLATION RECEIPT — the five-step protocol of the V39 amendment paragraph, executed in order — 2026-09-06 13:01:42 KST

**Approval, recorded exactly:** approved by Duho in the codex conversation, attested by Codex, 2026-09-06T04:00:15Z; bytes independently verified by Blanc (13:00:15 KST: ddc0cfb4139b7e1706f852cb5cdd7cb14293256fee8254cc71623bded172b2d0 = approval record = READY-FOR-APPROVAL filing = ACCESS_SHA of both seat reports). Source: `.hermes/CODEX_DUHO_HWAO_V39_PROCEED_20260906.md` (Duho: "최대한 빨리 진행해줘"). Not "signed"; not "witnessed by Blanc".
**V39 digest on disk now:** ddc0cfb4139b7e1706f852cb5cdd7cb14293256fee8254cc71623bded172b2d0
**Staged initialiser (the digest V39 pins for study_renderer/__init__.py):** 659b763c83a948825d285e51671c28173b446f428bcd32d941811bf6cdaf5721
**Pixel paths:** blocked throughout — no development draw, fetch, render or frozen pixel is authorised by this approval (the beacon read comes first; V19 is unapproved).

## Step 1 — pin check before installation
### 1a. Against the complete STAGED candidate tree (the referee sandbox): must be CONSISTENT
```
pins parsed: 81   superseded siblings on disk: 34
RESULT: CONSISTENT
```
### 1b. Against the lane (V35 initialiser still installed): exactly three defect diagnostics plus the header and footer
```
pins parsed: 81   superseded siblings on disk: 34
PIN MISMATCH      study_renderer/__init__.py
STALE IMPORT      study_renderer/__init__.py imports 'renderer_v3', superseded by renderer_v4.py
STALE IMPORT      study_renderer/__init__.py imports 'renderer_v3', superseded by renderer_v4.py
RESULT: 3 DEFECT(S)
```
lane initialiser before install: 4376984057b9af4c9f095fdacd3b37aff572a52cebb2ffaf53639b95ffedf827 (V35 pin 43769840…)

## Step 2 — install the staged bytes at study_renderer/__init__.py (pixel paths blocked)
installed: 659b763c83a948825d285e51671c28173b446f428bcd32d941811bf6cdaf5721 — equals the staged digest: YES; V35 bytes archived at _archive/study_renderer__init___V35_retired_1301.py

## Step 3 — pin check in the lane after installation: must be CONSISTENT
```
pins parsed: 81   superseded siblings on disk: 34
RESULT: CONSISTENT
```

## Step 4 — FRESH production interpreter: sys.modules inspection
```
interpreter: /Library/Developer/CommandLineTools/usr/bin/python3 3.9.6
study_renderer.render_cutout is renderer_v4.render_cutout: True
render_chain_v3 renderer binding is renderer_v4: True
render_chain_v3 rejection module: study_renderer.pixel_rejection_v2 | protected region: protected_region_v2
renderer_v3 loaded in this interpreter: False
production path: study_renderer.render_chain_v3.render_object
STEP 4: CONFIRMED
```

## Step 5 — V39 ENABLED
Enabled at 2026-09-06 13:01:43 KST after steps 1–4 passed as printed above. V35's own checker on V35 now reports the initialiser as mismatched — expected: V35 is superseded by V39 for the pipeline identity; V35 remains the pin authority for the files it pinned that V39 did not replace.
```
PIN MISMATCH      study_renderer/__init__.py
RESULT: 1 DEFECT(S)
```

Old fixtures on the untouched V35 modules, after installation: test_pixel_rejection OK; test_renderer_v3 OK; V39 chain: test_render_chain_v3 OK; anchor_gate.test_anchor_gate_v5 OK

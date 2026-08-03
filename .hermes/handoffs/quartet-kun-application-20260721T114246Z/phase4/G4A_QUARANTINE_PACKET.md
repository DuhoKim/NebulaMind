# G4a Ordinary Quarantine Proposal

## Prerequisites
- Branch must be `feat/surveys-atlas-ia-p1-20260627` at exact HEAD `826e733`.
- Explicit, separate future G4a approval required.
- NO ACTION NOW.

## Exact Closed-World Scope
Enumerate exact 18 DELETE-CANDIDATE top-level status entries. Count: 18 items. Zero protected items among candidates.

**Paths:**
- `backend/app/main.py.bak-labrunner` (Type: -rw-------, Size: 6178)
- `click.js` (Type: -rw-r--r--, Size: 186)
- `find_deep.js` (Type: -rw-r--r--, Size: 353)
- `find_menu.js` (Type: -rw-r--r--, Size: 347)
- `goru_temp_report.json` (Type: -rw-r--r--, Size: 2051)
- `test_applescript.applescript` (Type: -rw-r--r--, Size: 299)
- `test_inject.applescript` (Type: -rw-r--r--, Size: 502)
- `test_inject2.applescript` (Type: -rw-r--r--, Size: 538)
- `test_js_drop.applescript` (Type: -rw-r--r--, Size: 660)
- `test_js_innerhtml.applescript` (Type: -rw-r--r--, Size: 1013)
- `test_js_insert.applescript` (Type: -rw-r--r--, Size: 474)
- `test_js_paste.applescript` (Type: -rw-r--r--, Size: 701)
- `test_js_rich_textarea.applescript` (Type: -rw-r--r--, Size: 759)
- `test_menu_paste.applescript` (Type: -rw-r--r--, Size: 289)
- `test_paste.applescript` (Type: -rw-r--r--, Size: 263)
- `test_type.applescript` (Type: -rw-r--r--, Size: 336)
- `tmp_build_2929_trust_packet.py` (Type: -rw-------, Size: 35837)
- `wait_and_extract.py` (Type: -rw-r--r--, Size: 1880)

**Retained in place (NO blanket move):**
- Exact 130 ARCHIVE items.
- Exact 14 operational `tools/*.bak-*` items.

## Stop Rules (Metadata Drift/Identity)
- Action stops if any candidate changes identity, type, or metadata before action.
- Action stops if any path overlap exists among sets.

## Verification
- Compare before/after counts.
- Exactly 18 items placed in one timestamped quarantine directory.

## Rollback
- Rollback by restoring exactly from quarantine directory.

GORU_PHASE4_G4A_PACKET_COMPLETE_20260722

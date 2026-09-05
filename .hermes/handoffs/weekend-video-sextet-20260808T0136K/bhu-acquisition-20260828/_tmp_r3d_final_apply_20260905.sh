#!/bin/zsh
# Applies the FINAL declaration to R3D V29. Every step asserts and STOPS on failure — no run-on.
set -e; set -u; set -o pipefail
L=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828
S=/private/tmp/claude-501/-Users-duhokim-NebulaMind-NebulaMind/20ba9cc5-e22c-4080-a8ae-bb58ee8f7ad3/scratchpad
KIMI_VERDICT="$1"   # e.g. "SOUND_WITH_REPAIRS, five sections sound, sole actionable defect none"
cd "$L"
SHA=$(shasum -a 256 R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md|cut -d' ' -f1)
grep -q "sha256 \`$SHA\`" "$S/r3d_final_8u.md" || { echo "STOP: draft hash != current file hash"; exit 1; }
grep -q 'R3D_PREREG_V30_READY_FOR_REEXHIBITION' R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md || { echo "STOP: V30 terminator absent"; exit 1; }
# re-verify counts on disk at apply time, never from memory
P=$(for f in $(ls R3D_C0_EXHIBITION_*codex*.md | grep -v STALEBRIEF); do sed -n '2p' $f; done | grep -c PASS)
[ "$P" = "19" ] || { echo "STOP: C0 pass count on disk is $P, draft says 19"; exit 1; }
CL=$(for v in 18 19 20 21 22 23 24 25 26 27 28 29 30; do c=$(grep -m1 -oE 'GATE=[A-Z_]+' R3D_GATE_V${v}_codex_20260905.md 2>/dev/null || true); k=$(grep -m1 -oE 'GATE=[A-Z_]+' R3D_GATE_V${v}_kimi_20260905.md 2>/dev/null || true); [ -n "$c" ] && [ -n "$k" ] && ! echo "$c$k" | grep -q UNSOUND && echo V$v; done | wc -l | tr -d ' ')
[ "$CL" = "10" ] || { echo "STOP: two-seat clears on disk = $CL, draft says 10"; exit 1; }
python3 - "$S/r3d_final_8u.md" "$KIMI_VERDICT" <<'PY'
import io,sys
d=io.open(sys.argv[1],encoding='utf-8').read().replace("__KIMI__",sys.argv[2])
assert "__KIMI__" not in d
p="R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md"; s=io.open(p,encoding='utf-8').read()
o="R3D_PREREG_V30_READY_FOR_REEXHIBITION"; assert s.count(o)==1
s=s.replace(o,d.rstrip()+"\n")
assert "R3D_PREREG_V30_FINAL_DESIGN_OF_RECORD" in s and s.count("FINAL_DESIGN_OF_RECORD")==1
io.open(p,'w',encoding='utf-8').write(s); print("§8u applied; terminator = FINAL_DESIGN_OF_RECORD")
PY
NEW=$(shasum -a 256 R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md|cut -d' ' -f1)
echo "NOTE: the FINAL declaration itself changes the file. Design-of-record hash = $SHA (the gated bytes); declaration-carrying file = $NEW. Both go in the record."
echo "$SHA  R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md  # V30 design of record, as gated" > R3D_DESIGN_OF_RECORD.sha256
echo "$NEW  R3D_DYMNIKOVA_FLOOR_PREREG_20260904.md  # V30 + §8u declaration, as committed" >> R3D_DESIGN_OF_RECORD.sha256
echo "READY TO COMMIT — script stops here; commit is a separate reviewed step."

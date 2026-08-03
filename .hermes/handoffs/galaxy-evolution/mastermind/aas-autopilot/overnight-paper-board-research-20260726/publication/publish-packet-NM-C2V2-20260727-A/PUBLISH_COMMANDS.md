# Publish Commands — NM-C2V2-20260727-A (PLAN ONLY — DO NOT EXECUTE NOW)

**Classification: HIGH-RISK** live/public/current-Lab mutation. This is a transaction-safe command PLAN for review. **Nothing here is executed by the preflight; no live HTTP was run.** Execution is authorized ONLY after the exact phrase `APPROVE PUBLISH NM-C2V2-20260727-A`, and is all-or-nothing: an `EXIT`-trap rollback that removes **only bytes this transaction created** (ownership-gated) is armed before the first create and disarmed only after every post-write and served check passes.

## Base URLs (grounded read-only; no `.env`/secret read, no live HTTP run now)
- **Local (authoritative):** `http://localhost:8000` — live uvicorn process `app.main:app --host 0.0.0.0 --port 8000`; `backend/app/main.py:96` mounts `lab_runner.router` at `/api/lab`.
- **Public (Cloudflare-fronted):** `https://api.nebulamind.net` — `backend/app/main.py:69` CORS `allow_origins` + the `connect-src` CSP (non-secret config).

Execution host must have `python3`, `curl`, `shasum`, and `pdftotext` (poppler).

```bash
#!/usr/bin/env bash
set -euo pipefail
set -o noclobber            # exclusive create for artifacts: '>' fails if target exists (never overwrite-capable cp)

# ---- roots (absolute; rooted explicitly at the NebulaMind repo) ----
REPO=/Users/duhokim/NebulaMind/NebulaMind
LAB="$REPO/.hermes/handoffs/galaxy-evolution/lab-runs"
OVN="$REPO/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-paper-board-research-20260726"
PK="$OVN/publication/publish-packet-NM-C2V2-20260727-A"
V2="$OVN/packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate-v2"
BASELINE="$OVN/baseline/INPUT_SHA256.txt"
ID=c2v2e2e0726a
BASE_LOCAL=http://localhost:8000
BASE_PUBLIC=https://api.nebulamind.net
PDF=ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d
TEX=bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6
PNG=ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639
MAN=fa4c815578aef3f01a7e18985f83725fefab052d4735987577f77f76f4d6b0ba

# ---- ownership flags: rollback removes ONLY what THIS transaction created ----
OWN_DIR=0        # 1 only after we exclusively mkdir the run dir (then we own it + its contents)
OWN_MANIFEST=0   # 1 ONLY after the O_EXCL helper reports it exclusively created the manifest

rollback() {
  set +e                                          # tolerant inside rollback
  if [ "$OWN_MANIFEST" = 1 ]; then rm -f "$LAB/$ID.json"; fi                 # 1) discovery off first (only if we own it)
  if [ "$OWN_DIR" = 1 ]; then
    rm -f "$LAB/$ID/draft.pdf" "$LAB/$ID/draft.tex" "$LAB/$ID/result.png"    # 2) only our three exact files
    rmdir "$LAB/$ID" 2>/dev/null                                            # 3) our exact dir; fails safe if non-empty
  fi
  return 0
}
# Self-disabling EXIT handler: disarm its own trap FIRST, then roll back and exit (no re-entry).
trap 'rc=$?; trap - EXIT; echo "FAILURE (rc=$rc) — rolling back owned bytes only"; rollback; exit "$rc"' EXIT

# Exclusive manifest creator: os.open(O_CREAT|O_EXCL|O_WRONLY). It can only ever touch a file it itself
# created; on write failure it unlinks ONLY its own partial file. Exit 0=CREATED, 3=EXISTS, 2=ERROR.
manifest_create() {
  python3 - "$1" "$2" <<'PY'
import os, sys, shutil
src, dst = sys.argv[1], sys.argv[2]
try:
    fd = os.open(dst, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)   # atomic exclusive create
except FileExistsError:
    print("EXISTS"); sys.exit(3)          # another process owns it -> we never touch it
except OSError as e:
    print("ERROR", e); sys.exit(2)
try:
    with open(src, "rb") as s, os.fdopen(fd, "wb") as d:
        shutil.copyfileobj(s, d)
except BaseException as e:
    try: os.unlink(dst)                    # clean up ONLY the file we exclusively created
    except OSError: pass
    print("ERROR", e); sys.exit(2)
print("CREATED"); sys.exit(0)
PY
}

# ---- GUARD: every exact target must be ABSENT, else abort. No ownership set yet -> rollback deletes NOTHING. ----
for p in "$LAB/$ID.json" "$LAB/$ID"; do
  [ -e "$p" ] && { echo "ABORT: target exists: $p"; exit 1; }
done

# ---- create dir (exclusive: mkdir fails if it exists) then mark ownership ----
mkdir "$LAB/$ID"; OWN_DIR=1

# ---- three artifacts via exclusive noclobber redirection (inside our owned dir; manifest NOT yet) ----
cat "$V2/candidate.pdf" > "$LAB/$ID/draft.pdf"
cat "$V2/candidate.tex" > "$LAB/$ID/draft.tex"
cat "$V2/result.png"    > "$LAB/$ID/result.png"

# ---- verify artifact hashes BEFORE the manifest exists (mismatch -> rollback) ----
[ "$(shasum -a 256 "$LAB/$ID/draft.pdf"  | cut -d' ' -f1)" = "$PDF" ] || { echo "ABORT: pdf hash"; exit 1; }
[ "$(shasum -a 256 "$LAB/$ID/draft.tex"  | cut -d' ' -f1)" = "$TEX" ] || { echo "ABORT: tex hash"; exit 1; }
[ "$(shasum -a 256 "$LAB/$ID/result.png" | cut -d' ' -f1)" = "$PNG" ] || { echo "ABORT: png hash"; exit 1; }

# ---- manifest LAST via the O_EXCL helper; set ownership ONLY after it reports CREATED ----
if manifest_create "$PK/PREVIEW_MANIFEST.json" "$LAB/$ID.json"; then
  OWN_MANIFEST=1
else
  echo "ABORT: manifest exclusive create failed (EXISTS or write ERROR; not owned, not deleted by us)"; exit 1
fi
[ "$(shasum -a 256 "$LAB/$ID.json" | cut -d' ' -f1)" = "$MAN" ] || { echo "ABORT: manifest hash"; exit 1; }

# ---- baseline integrity: explicit gated-e2e-demo files AND full 38/38 manifest ----
[ "$(shasum -a 256 "$LAB/gated-e2e-demo/draft.pdf" | cut -d' ' -f1)" = 0d863bff4d4d260fe32e56617ca6f920f2943574aaff2a5faeee3f7460575933 ] || { echo "ABORT: baseline draft.pdf changed"; exit 1; }
[ "$(shasum -a 256 "$LAB/gated-e2e-demo/draft.tex" | cut -d' ' -f1)" = f1aeadd8ea43f2fd1e22e9686d23066fdf95e3d5c95937a42d8ddd076bc95a8a ] || { echo "ABORT: baseline draft.tex changed"; exit 1; }
[ "$(shasum -a 256 "$LAB/gated-e2e-demo.json"      | cut -d' ' -f1)" = 46ddd75d5f0e5814e814333336d8e6d1b011382c46509012af2aea8cc20af5e2 ] || { echo "ABORT: baseline gated-e2e-demo.json changed"; exit 1; }
( cd "$LAB" && shasum -a 256 -c "$BASELINE" >/dev/null ) || { echo "ABORT: baseline 38/38 SHA manifest mismatch"; exit 1; }

# ---- LOCAL served checks (authoritative; JSON-parsed; any failure -> rollback) ----
[ "$(curl -fsS -o /dev/null -w '%{http_code}' "$BASE_LOCAL/api/lab/runs/$ID")" = 200 ] || { echo "ABORT: local get_run != 200"; exit 1; }
[ "$(curl -fsS -o /dev/null -w '%{http_code}' "$BASE_LOCAL/api/lab/runs/$ID/artifact/draft.pdf")" = 200 ] || { echo "ABORT: local pdf != 200"; exit 1; }
[ "$(curl -fsS -o /dev/null -w '%{http_code}' "$BASE_LOCAL/api/lab/runs/$ID/artifact/result.png")" = 200 ] || { echo "ABORT: local png != 200"; exit 1; }
curl -fsS "$BASE_LOCAL/api/lab/runs" | python3 -c 'import sys,json; ids=[r.get("id") for r in json.load(sys.stdin).get("runs",[])]; sys.exit(0 if "c2v2e2e0726a" in ids else 1)' || { echo "ABORT: not in list"; exit 1; }
curl -fsS "$BASE_LOCAL/api/lab/runs/$ID" | python3 -c 'import sys,json; s=(json.load(sys.stdin).get("result") or {}).get("summary") or ""; req=["AI-draft","forced-demo","TENSION","unresolved-calibration"]; sys.exit(0 if all(x in s for x in req) else 1)' || { echo "ABORT: local summary missing a label"; exit 1; }
[ "$(curl -fsS "$BASE_LOCAL/api/lab/runs/$ID/artifact/draft.pdf" | shasum -a 256 | cut -d' ' -f1)" = "$PDF" ] || { echo "ABORT: served pdf bytes hash"; exit 1; }
PTX="$(curl -fsS "$BASE_LOCAL/api/lab/runs/$ID/artifact/draft.pdf" | pdftotext - -)"
printf '%s' "$PTX" | grep -Fq "not submitted, not peer-reviewed" || { echo "ABORT: local PDF missing not-submitted disclosure"; exit 1; }
printf '%s' "$PTX" | grep -Fq "TENSION" || { echo "ABORT: local PDF missing TENSION"; exit 1; }
printf '%s' "$PTX" | grep -Fq "common calibration is established" || { echo "ABORT: local PDF missing unresolved-calibration caveat"; exit 1; }

# ---- PUBLIC served checks: bounded settlement poll (Cloudflare tunnel/cache), then labels + PDF text ----
pub_ok=0
for attempt in $(seq 1 12); do                              # up to 12 * 5s = 60s
  code="$(curl -fsS -o /dev/null -w '%{http_code}' "$BASE_PUBLIC/api/lab/runs/$ID/artifact/draft.pdf" || echo 000)"
  if [ "$code" = 200 ]; then pub_ok=1; break; fi
  echo "public settlement $attempt/12: http=$code; retrying in 5s"
  sleep 5
done
[ "$pub_ok" = 1 ] || { echo "ABORT: public endpoint not visible after 12x5s settlement"; exit 1; }
curl -fsS "$BASE_PUBLIC/api/lab/runs/$ID" | python3 -c 'import sys,json; s=(json.load(sys.stdin).get("result") or {}).get("summary") or ""; req=["AI-draft","forced-demo","TENSION","unresolved-calibration"]; sys.exit(0 if all(x in s for x in req) else 1)' || { echo "ABORT: public summary missing a label"; exit 1; }
PTXP="$(curl -fsS "$BASE_PUBLIC/api/lab/runs/$ID/artifact/draft.pdf" | pdftotext - -)"
printf '%s' "$PTXP" | grep -Fq "not submitted, not peer-reviewed" || { echo "ABORT: public PDF missing not-submitted disclosure"; exit 1; }
printf '%s' "$PTXP" | grep -Fq "common calibration is established" || { echo "ABORT: public PDF missing unresolved-calibration caveat"; exit 1; }

# ---- all checks passed: DISARM the rollback trap so success is committed ----
trap - EXIT
echo "PUBLISH VERIFIED OK: $ID (create-only; baseline 38/38 unchanged)"
```

## Notes
- **No manifest race:** the manifest is created by a Python `os.open(O_CREAT|O_EXCL|O_WRONLY)` helper that atomically fails (`EXISTS`, exit 3) if another process created the file after the absence guard, so we never delete another process's manifest. `OWN_MANIFEST=1` is set ONLY after the helper reports `CREATED`. On a write error the helper unlinks only its own partial file, then reports `ERROR` (we do not set ownership).
- **Ownership-gated rollback:** rollback removes only `OWN_DIR`/`OWN_MANIFEST` bytes. A guard failure fires the trap with both flags `0` → deletes nothing. An artifact partial write is owned via `OWN_DIR` (set right after the exclusive `mkdir`).
- **Self-disabling trap:** the EXIT handler runs `trap - EXIT` before rollback/exit, so it never re-enters.
- **Exclusive creates:** `set -o noclobber` for the three artifacts; `mkdir` fails if the dir exists; the manifest uses the O_EXCL helper. No overwrite-capable `cp` anywhere.
- **Manifest last / rollback manifest-first:** no partial run is ever discoverable; rollback revokes discovery before deleting bytes.
- **Baseline:** explicit `gated-e2e-demo` `draft.pdf`+`draft.tex`+`.json` checks AND the full `shasum -a 256 -c INPUT_SHA256.txt` (38/38) from the lab-runs root.
- **Served checks are active (post-approval), JSON-parsed:** list membership and the four summary labels via `python3`; served PDF bytes hash and rendered disclosure / TENSION / unresolved-calibration text on both local and public; public uses a bounded 12×5s settlement poll before its checks.
- No `.env`/secret was read; no live HTTP was executed during preflight.

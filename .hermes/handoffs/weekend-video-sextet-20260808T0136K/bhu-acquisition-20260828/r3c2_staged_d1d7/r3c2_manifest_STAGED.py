#!/usr/bin/env python3
"""r3c2_manifest_STAGED.py <directory> — STAGED, UNADOPTED copy (V26cand gate F9: symlinks and non-regular entries fail closed) — the pinned-environment manifest as ONE process (codex V24e D3: a shell pipeline can mask an
upstream failure). Walks every regular file under <directory> (symlinks not followed), reads each fully, and prints:
  FILES=<n>
  MANIFEST_SHA256=<sha256 over the lines "<sha256>  <relative path>\n", sorted by relative path, UTF-8>
Any unreadable file, permission error, or walk error prints ERROR=<path>: <reason> and the process exits 1; nothing is skipped
silently. Exit 0 only when every file was read and hashed. Uses only the standard library."""
import hashlib, os, sys
def main(root):
    root = os.path.abspath(root); rows = []; errors = 0
    for dirpath, dirnames, filenames in os.walk(root, onerror=lambda e: (print(f"ERROR={e.filename}: {e.strerror}"), sys.exit(1))):
        dirnames.sort()
        for dn in list(dirnames):
            if os.path.islink(os.path.join(dirpath, dn)): print(f"ERROR={os.path.relpath(os.path.join(dirpath, dn), root)}: symlinked directory (refused)"); sys.exit(1)
        for fn in sorted(filenames):
            p = os.path.join(dirpath, fn)
            if os.path.islink(p) or not os.path.isfile(p): print(f"ERROR={os.path.relpath(p, root)}: symlink or non-regular entry (the manifest pins regular files only and refuses to skip)"); sys.exit(1)  # PROBE:MANIFEST_SYMLINK
            try:
                h = hashlib.sha256()
                with open(p, "rb") as f:
                    for chunk in iter(lambda: f.read(1 << 20), b""): h.update(chunk)
                rows.append((os.path.relpath(p, root), h.hexdigest()))
            except OSError as e:
                print(f"ERROR={os.path.relpath(p, root)}: {e.strerror}"); errors += 1
    if errors: print(f"FILES={len(rows)}\nMANIFEST_SHA256=INCOMPLETE ({errors} unreadable)"); sys.exit(1)
    rows.sort(key=lambda r: r[0]); m = hashlib.sha256("".join(f"{d}  {p}\n" for p, d in rows).encode("utf-8")).hexdigest()
    print(f"FILES={len(rows)}\nMANIFEST_SHA256={m}"); sys.exit(0)
if __name__ == "__main__":
    if len(sys.argv) != 2: print(__doc__); sys.exit(2)
    main(sys.argv[1])

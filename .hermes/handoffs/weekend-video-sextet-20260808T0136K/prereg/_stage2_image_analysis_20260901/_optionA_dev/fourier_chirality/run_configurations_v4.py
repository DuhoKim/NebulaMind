#!/usr/bin/env python3
"""run_configurations_v4 (option A V20 draft): v3 plus the SEMANTIC conjunction the V19 audit (M1) required — the driver PARSES the committed
collection history and locates its first builder ACCEPT, restricts the outcome to ACCEPT-DRAND, validates the approval witness (entire push event
with ref, commit inclusion and server time before T_pulse; the nonce round; the approval record's digest line), verifies the adoption file as a
byte-equal blob at the approval commit (one 64-hex line + one newline, no blanks), and re-derives the seed from the retained beacon evidence.
v3 was: run_configurations_v3 (option A V19 draft): v2 plus the ACCEPTANCE-PATH checks the driver had never made (codex V18 item 4): the identity
must carry beacon_outcome starting with ACCEPT, an approval witness whose server-side push time is before the identity's T_pulse, a collection
lock whose first ACCEPT names the identity's beacon record and seed, and a collection log that is a byte-equal blob at the witnessed commit.
v2 was: run_configurations_v2 (option A V18 draft): the V15 driver plus (a) the ADOPTION BINDING — the rule digest is read from a committed file and the
identity must carry it (codex V16/V17: Protocol.rule_sha256 was None with no adoption mechanism); (b) the render-refused SENTINEL — an object refused
at render is represented by a canonical tensor of float32 NaN, stays in the fixed denominator, is UNSCORED for every configuration (chi non-finite),
and is COUNTED per manifest (`sentinel_count`) so a receipt shows how many objects never reached the instrument (codex V17 execution prerequisite).
ORIGINAL DOCSTRING FOLLOWS.
PINNED DRIVER for the selection rule §7 — the ONLY path from tensors to a selected candidate. Two closed modes, both requiring
--identity CORPUS_IDENTITY.json whose SHA-256 is sealed in the lane's chained journal (operation corpus-identity-freeze) BEFORE any
read; manifests must carry EXACTLY the identity's ordered objids. holdout RECONSTRUCTS the tuning winner from the 96 receipts and the
live enumeration (the summary is never trusted), reconciles every receipt against the per-object journal, and requires the tuning RUN ROOT
(digest over journal, receipts, manifest, tensor set, identity, estimator, driver, env lock) sealed and witnessed (operation tuning-freeze).
Thread controls are set before numpy is imported; the lock covers the NumPy core and the pocketfft binary actually used by fft2.

  tune    --manifest TUNING.csv    --tensors DIR --out DIR
          exactly N_TUNE=400 rows (objid,g,tensor_sha256), unique objids, every tensor present and hash-equal; runs ALL 96
          enumerated configurations in lexicographic order; UNSCORED = tie/non-finite/missing/exception/non-repeat; ELIGIBLE
          iff m >= FLOOR_TUNE=380 (absolute, no override); OBJECTIVE = max(k, m-k) / N_TUNE (fixed denominator: an unscored
          object counts as a miss for both orientations); tie-break fewer unscored, then earlier index. Writes the tuning
          receipt with the winner's config_id.
  holdout --tuning-receipt selection_summary.json --manifest HOLDOUT.csv --tensors DIR --out DIR
          verifies the tuning receipt's journal/receipt hashes, takes ITS winner and no other configuration, requires exactly
          N_HOLD=200 rows disjoint from the tuning manifest, evaluates that one configuration once; FLOOR first (m >= 190)
          else CLOSED; then PASS iff Wilson 95% lower bound on max(k, m-k)/N_HOLD > 0.70, else CLOSED. Never enumerates the
          other 95 configurations.
Both modes: before reading any tensor or label, hash env_lock.json (must equal ENV_LOCK_SHA256) and compare the live
interpreter, Python, NumPy, platform, machine and NumPy core-library digest to every locked value; stop on inequality. Every
configuration receipt and the final receipt carry the lock hash, the observed environment, and the manifest/tensor-set digests.
Any deviation is DATA-INTEGRITY-FAIL: exit 2, no selection, no verdict. The production constants are module constants; the
fixture exercises the same code through an explicitly labelled test protocol (never reachable from the command line).
"""
import sys, os, re, json, csv, time, hashlib, platform, argparse
from dataclasses import dataclass
from pathlib import Path
THREAD_VARS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
for _v in THREAD_VARS: os.environ[_v] = "1"          # set BEFORE numpy is imported; recorded in every receipt; compared to the lock
import numpy as np
import numpy.fft._pocketfft_internal as _pocketfft
HERE = Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import fourier_chirality as fc

ENV_LOCK_SHA256 = "4e2c851fe1f22f4bc28f121cf3ff4326f036be57fc100b34af9e5501d6c74251"
ADOPTION_FILE = HERE.parents[0] / "ADOPTED_RULE_SHA256.txt"        # v2 (option A V18): the approved rule digest is a COMMITTED file; production fails closed without it
SENTINEL_TENSOR = np.full(128 * 128, np.nan, dtype="<f4").tobytes(order="C")   # v2: the render-refused sentinel — 65,536 bytes of float32 NaN; chi is non-finite → UNSCORED for every configuration
SENTINEL_SHA256 = hashlib.sha256(SENTINEL_TENSOR).hexdigest()
def adopted_rule_sha256():
    """v2: exactly one 64-hex line in ADOPTION_FILE; absent or malformed → DataIntegrityFail (no flag can substitute)."""
    try: lines = [l.strip() for l in ADOPTION_FILE.read_text().splitlines() if l.strip()]
    except FileNotFoundError: raise DataIntegrityFail(f"ADOPTION-MISSING {ADOPTION_FILE.name}: no approved rule digest is bound")
    if len(lines) != 1 or not re.fullmatch(r"[0-9a-f]{64}", lines[0]): raise DataIntegrityFail("ADOPTION-MALFORMED: exactly one 64-hex line required")
    return lines[0]
Z = 1.959963984540054; THRESHOLD = 0.70

@dataclass(frozen=True)
class Protocol:
    n_tune: int = 400
    floor_tune: int = 380
    n_hold: int = 200
    floor_hold: int = 190
    n_fresh: int = 2000
    label: str = "PRODUCTION"
    pool_sha256: str = "2cc94a29562270fcb5043f4ce942e303696f359b5fb0c59fdee48578ebb34155"          # guarded_pool.csv as pinned in the rule
    exclusion_sha256: str = "77b29eafe18e02d4dee621a6e748e8f698381c6e23098e7db2db190aee270c95"   # dryrun_identities_to_exclude_20260905.txt as pinned in the rule
    require_beacon: bool = True                                                 # production identities must be beacon-seeded and carry the beacon record digest
    rule_sha256: str = None                                                     # signed rule digest; production pins this when adopted
    seal_journal: str = str(HERE.parents[1] / "seal_journal_tierc.jsonl")     # the lane's chained journal; freezes must be recorded here BEFORE use
    witness_remote_ref: str = "origin/feat/paper-workflow-v2"                  # the freeze record must be in a commit PUSHED to this ref (a remote the operator cannot rewrite; the hook forbids force)
    witness_remote_url: str = "https://github.com/DuhoKim/NebulaMind.git"   # `git remote get-url origin` MUST equal this (agy V8: a local clone could otherwise point origin at a fake bare repo)
    witness_fetch: bool = True                                                  # git fetch before the ancestry check (network; inward)
    collection_log: str = str(HERE.parents[0] / "collection_log.jsonl")        # v3: the append-only attempt history, committed with the identity
    witness_branch_ref: str = "refs/heads/feat/paper-workflow-v2"              # v4: the protected ref the approval push event must name
    adoption_file: str = str(HERE.parents[0] / "ADOPTED_RULE_SHA256.txt")       # v4: verified as a blob at the approval commit
    beacon_record_path: str = str(HERE.parents[0] / "beacon_record_V20.json")   # v4: the retained record from which the seed is re-derived
    rederive_seed: object = None                                                # v4: callable(record_path) -> seed hex (the drand-only verdict, no network); tests inject
PRODUCTION = Protocol()

class DataIntegrityFail(Exception): pass

def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""): h.update(c)
    return h.hexdigest()
def utc(): return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
def wilson_lower(k, n, z=Z):
    if n == 0: return 0.0
    p = k / n; den = 1 + z * z / n; c = (p + z * z / (2 * n)) / den; h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / den
    return c - h

def observed_env():
    core = np.core._multiarray_umath.__file__; fft = _pocketfft.__file__
    return {"interpreter": sys.executable, "python": sys.version.split()[0], "numpy": np.__version__, "platform": platform.platform(),
            "machine": platform.machine(), "numpy_core_sha256": sha_file(core), "numpy_core_basename": core.split("/")[-1],
            "numpy_fft_sha256": sha_file(fft), "numpy_fft_basename": fft.split("/")[-1], "thread_env": {v: os.environ.get(v) for v in THREAD_VARS}}
def enforce_environment(lock_path=HERE / "env_lock.json", expect_sha=ENV_LOCK_SHA256):
    got = sha_file(lock_path)
    if got != expect_sha: raise DataIntegrityFail(f"ENV-LOCK-HASH-MISMATCH expected {expect_sha} got {got}")
    lock = json.loads(Path(lock_path).read_text()); obs = observed_env()
    bad = [k for k in obs if lock.get(k) != obs[k]]
    if bad: raise DataIntegrityFail("ENV-MISMATCH " + ",".join(f"{k}:{lock.get(k)}!={obs[k]}" for k in bad))
    return {"env_lock_sha256": got, "observed": obs}

def journal_has(journal_path, operation, digest):
    """True iff the chained seal journal holds a record with this operation whose observed_digest equals digest."""
    try:
        with open(journal_path) as fh:
            for l in fh:
                r = json.loads(l)
                if r.get("operation") == operation and r.get("observed_digest") == digest: return True
    except FileNotFoundError: pass
    return False

def verify_witness(journal_path, operation, digest, proto):
    """Freeze WITNESS (both V6 seats): the journal record must exist in a git commit that is an ancestor of the pushed remote ref.
    <journal>.witness.<operation>.json = {"commit": <sha>} is written by the operator when they push; the driver verifies that the
    commit contains the record line and is reachable from proto.witness_remote_ref after a fetch. An unpushed or absent commit fails."""
    import subprocess
    jp = Path(journal_path); wf = jp.with_name(jp.name + f".witness.{operation}.json")
    if not wf.is_file(): raise DataIntegrityFail(f"WITNESS-MISSING {wf.name}")
    commit = json.loads(wf.read_text()).get("commit", "")
    if not re.fullmatch(r"[0-9a-f]{40}", commit): raise DataIntegrityFail("WITNESS-COMMIT-MALFORMED")
    repo = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=jp.parent, capture_output=True, text=True)
    if repo.returncode != 0: raise DataIntegrityFail("WITNESS-NOT-A-GIT-REPO")
    root = Path(repo.stdout.strip()); rel = jp.resolve().relative_to(root.resolve()).as_posix()
    shown = subprocess.run(["git", "cat-file", "-p", f"{commit}:{rel}"], cwd=root, capture_output=True, text=True)
    if shown.returncode != 0: raise DataIntegrityFail(f"WITNESS-COMMIT-LACKS-JOURNAL {commit[:12]}")
    if not any((lambda r: r.get("operation") == operation and r.get("observed_digest") == digest)(json.loads(l)) for l in shown.stdout.splitlines() if l.strip()):
        raise DataIntegrityFail(f"WITNESS-COMMIT-LACKS-RECORD {operation} {digest[:12]}")
    remote = proto.witness_remote_ref.split("/")[0]
    url = subprocess.run(["git", "remote", "get-url", remote], cwd=root, capture_output=True, text=True)
    if url.returncode != 0 or url.stdout.strip() != proto.witness_remote_url: raise DataIntegrityFail(f"WITNESS-REMOTE-URL {url.stdout.strip()[:80]} != pinned")
    if proto.witness_fetch:
        f = subprocess.run(["git", "fetch", remote], cwd=root, capture_output=True, text=True)
        if f.returncode != 0: raise DataIntegrityFail(f"WITNESS-FETCH-FAILED {f.stderr.strip()[:120]}")
    anc = subprocess.run(["git", "merge-base", "--is-ancestor", commit, proto.witness_remote_ref], cwd=root, capture_output=True, text=True)
    if anc.returncode != 0: raise DataIntegrityFail(f"WITNESS-NOT-PUSHED {commit[:12]} not an ancestor of {proto.witness_remote_ref}")
    return {"commit": commit, "remote_ref": proto.witness_remote_ref, "remote_url": proto.witness_remote_url, "_root": str(root)}

def blob_at_commit_equals(root, commit, path):
    """True iff the file's bytes equal the blob at <commit>:<path relative to repo root> (agy, V12 gate: the pushed commit must carry the identity itself)."""
    import subprocess
    p = Path(path).resolve()
    try: rel = p.relative_to(Path(root).resolve()).as_posix()
    except ValueError: return False
    r = subprocess.run(["git", "cat-file", "-p", f"{commit}:{rel}"], cwd=root, capture_output=True)
    return r.returncode == 0 and r.stdout == p.read_bytes()

def load_identity(identity_path, proto):
    """Corpus identity: ordered objid lists frozen BEFORE development; its digest must be sealed in the journal."""
    d = sha_file(identity_path)
    if d is None: raise DataIntegrityFail(f"IDENTITY-MISSING {identity_path}")
    if not journal_has(proto.seal_journal, "corpus-identity-freeze", d): raise DataIntegrityFail(f"IDENTITY-NOT-SEALED {d}")
    w = verify_witness(proto.seal_journal, "corpus-identity-freeze", d, proto)
    if not blob_at_commit_equals(w["_root"], w["commit"], identity_path): raise DataIntegrityFail("IDENTITY-NOT-IN-WITNESS-COMMIT: the identity file's bytes are not the blob at the witnessed commit")
    w_root = w["_root"]; w = {k: v for k, v in w.items() if k != "_root"}
    I = json.loads(Path(identity_path).read_text()); I["_witness"] = w
    if I.get("schema_version") != "CORPUS-IDENTITY-2": raise DataIntegrityFail("IDENTITY-SCHEMA")
    for k in ("pool_sha256", "ordering_rule", "seed_hex", "split_mode", "renderability_inputs", "fresh_validation_objids", "exclude_file_sha256", "beacon_record_sha256", "rule_sha256"):
        if k not in I: raise DataIntegrityFail(f"IDENTITY-FIELD-MISSING {k}")
    if I["pool_sha256"] != proto.pool_sha256: raise DataIntegrityFail("IDENTITY-POOL-DIGEST: not the pinned guarded pool")
    if I["exclude_file_sha256"] != proto.exclusion_sha256: raise DataIntegrityFail("IDENTITY-EXCLUSION-DIGEST: not the pinned exclusion file")
    adopted = adopted_rule_sha256()                                                                        # v2: fail closed
    if proto.rederive_seed is None: raise DataIntegrityFail("PROTOCOL-NO-REDERIVER: the protocol must supply the drand-only seed re-derivation")
    if proto.rule_sha256 is not None and proto.rule_sha256 != adopted: raise DataIntegrityFail("ADOPTION-MISMATCH: protocol digest differs from the adopted file")
    if I["rule_sha256"] != adopted: raise DataIntegrityFail("IDENTITY-RULE-DIGEST: not the adopted approved rule")
    if proto.require_beacon and (not str(I["split_mode"]).startswith("beacon-seeded") or not re.fullmatch(r"[0-9a-f]{64}", str(I["beacon_record_sha256"] or ""))):
        raise DataIntegrityFail("IDENTITY-NOT-BEACON-SEEDED: production identities must be derived from an accepted beacon record")
    if proto.require_beacon:                                                                               # v4: the SEMANTIC conjunction (V19 audit M1)
        import subprocess
        if I.get("beacon_outcome") != "ACCEPT-DRAND": raise DataIntegrityFail(f"IDENTITY-BEACON-NOT-ACCEPTED {I.get('beacon_outcome')} (only ACCEPT-DRAND is admissible under V20)")
        if I.get("beacon_source") != "drand-mainnet-default": raise DataIntegrityFail("IDENTITY-SOURCE: not the pinned drand chain")
        tp = str(I.get("beacon_t_pulse") or ""); w = I.get("approval_witness") or {}; ev = w.get("push_event") or {}
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", tp): raise DataIntegrityFail("IDENTITY-WITNESS-MISSING: T_pulse absent")
        if ev.get("type") != "PushEvent" or not ev.get("created_at") or (ev.get("payload") or {}).get("ref") != proto.witness_branch_ref: raise DataIntegrityFail("IDENTITY-WITNESS-MISSING: no PushEvent for the protected ref in the identity")
        if ev["created_at"].replace("Z", "+00:00") >= tp.replace("Z", "+00:00"): raise DataIntegrityFail("IDENTITY-WITNESS-LATE: the approval push time is not before T_pulse")
        commit = w.get("commit") or ""; pay = ev.get("payload") or {}
        if not re.fullmatch(r"[0-9a-f]{40}", commit) or not (pay.get("head") == commit or any(c.get("sha") == commit for c in pay.get("commits", []))): raise DataIntegrityFail("IDENTITY-WITNESS-COMMIT: the push event does not deliver the approval commit")
        if not isinstance(w.get("nonce_round"), int) or not re.fullmatch(r"[0-9a-f]{64}", str(w.get("nonce_randomness") or "")): raise DataIntegrityFail("IDENTITY-WITNESS-NONCE: nonce absent")
        rec_sha = I["beacon_record_sha256"]; lk = I.get("collection_lock") or {}
        lp = Path(proto.collection_log)
        if sha_file(lp) != lk.get("log_sha256"): raise DataIntegrityFail("COLLECTION-LOG-DIGEST: the committed collection log differs from the identity's record of it")
        if not blob_at_commit_equals(w_root, I["_witness"]["commit"], lp): raise DataIntegrityFail("COLLECTION-LOG-NOT-IN-WITNESS-COMMIT")
        entries = [json.loads(l) for l in lp.read_text().splitlines() if l.strip()]
        accepts = [e for e in entries if e.get("stage") == "builder-accept"]
        if len(entries) < 2 or not accepts: raise DataIntegrityFail("COLLECTION-LOG-EMPTY: no builder ACCEPT in the committed history")
        fa = accepts[0]
        if fa.get("record_sha256") != rec_sha or fa.get("outcome") != I["beacon_outcome"] or fa.get("seed_hex") != I["seed_hex"]: raise DataIntegrityFail("IDENTITY-LOCK-MISMATCH: the first logged ACCEPT does not name this identity's record, outcome and seed")
        if (lk.get("first_accept") or {}) != fa: raise DataIntegrityFail("IDENTITY-LOCK-MISMATCH: identity's first_accept differs from the log's")
        if any(e.get("stage") == "builder-conflict" for e in entries): raise DataIntegrityFail("COLLECTION-LOG-CONFLICT: a conflicting later ACCEPT is on record")
        ap = Path(proto.adoption_file); raw = ap.read_bytes() if ap.is_file() else b""
        lines = raw.decode("utf-8", "replace").split("\n")
        if not (len(lines) == 2 and lines[1] == "" and lines[0] == adopted): raise DataIntegrityFail("ADOPTION-MALFORMED: exactly one 64-hex line and one newline, equal to the adopted digest")
        if not blob_at_commit_equals(w_root, commit, ap): raise DataIntegrityFail("ADOPTION-NOT-AT-APPROVAL-COMMIT: the adoption file is not a byte-equal blob at the approval commit")
        if I.get("adoption_sha256") != sha_file(ap): raise DataIntegrityFail("ADOPTION-DIGEST: identity's adoption digest differs from the file")
        rp = Path(proto.beacon_record_path)
        if sha_file(rp) != rec_sha: raise DataIntegrityFail("BEACON-RECORD-DIGEST: the retained beacon record differs from the identity's")
        seed = proto.rederive_seed(rp)
        if seed != I["seed_hex"]: raise DataIntegrityFail("IDENTITY-SEED-NOT-REDERIVED: the seed does not follow from the retained beacon evidence")
    for k, n in (("tuning_objids", proto.n_tune), ("holdout_objids", proto.n_hold), ("fresh_validation_objids", proto.n_fresh)):
        if len(I.get(k, [])) != n or len(set(I[k])) != n or not all(isinstance(x, int) for x in I[k]): raise DataIntegrityFail(f"IDENTITY-{k}-SIZE-OR-TYPE")
    a, b, c = set(I["tuning_objids"]), set(I["holdout_objids"]), set(I["fresh_validation_objids"])
    if (a & b) or (a & c) or (b & c): raise DataIntegrityFail("IDENTITY-OVERLAP")
    return I, d

def load_manifest(path, tensors, n_required, required_objids=None):
    if not Path(path).is_file(): raise DataIntegrityFail(f"MANIFEST-MISSING {path}")
    if not Path(tensors).is_dir(): raise DataIntegrityFail(f"TENSOR-DIR-MISSING {tensors}")
    with open(path, newline="") as fh: rows = list(csv.DictReader(fh))
    if len(rows) != n_required: raise DataIntegrityFail(f"MANIFEST-SIZE {len(rows)} != {n_required}")
    if set(rows[0].keys()) != {"objid", "g", "tensor_sha256"}: raise DataIntegrityFail("MANIFEST-COLUMNS")
    ids = [r["objid"] for r in rows]
    if len(set(ids)) != len(ids): raise DataIntegrityFail("MANIFEST-DUPLICATE-OBJID")
    if required_objids is not None and [str(x) for x in ids] != [str(x) for x in required_objids]: raise DataIntegrityFail("MANIFEST-IDENTITY-MISMATCH: ordered objids differ from the sealed corpus identity")
    objs = []
    for r in rows:
        g = int(r["g"])
        if g not in (1, -1): raise DataIntegrityFail(f"LABEL-NOT-PM1 {r['objid']}")
        p = Path(tensors) / f"{r['objid']}.ic6"
        if not p.exists(): raise DataIntegrityFail(f"TENSOR-MISSING {r['objid']}")
        if sha_file(p) != r["tensor_sha256"]: raise DataIntegrityFail(f"TENSOR-SHA-MISMATCH {r['objid']}")
        b = p.read_bytes()
        if len(b) != 65536: raise DataIntegrityFail(f"TENSOR-SIZE {r['objid']}")
        objs.append((r["objid"], g, np.frombuffer(b, dtype="<f4").reshape(128, 128)))
    sentinel = sum(1 for r in rows if r["tensor_sha256"] == SENTINEL_SHA256)                             # v2: render-refused objects, present in the denominator, UNSCORED
    return objs, {"manifest_sha256": sha_file(path), "n": len(objs), "tensor_set_sha256": hashlib.sha256("".join(sorted(r["tensor_sha256"] for r in rows)).encode()).hexdigest(), "sentinel_count": sentinel}

def score_config(est, objs, journal, idx):
    k = m = unscored = 0
    with open(journal, "a") as jf:
        for oid, g, arr in objs:
            row = {"config_index": idx, "config_id": est.config_id, "objid": oid}
            try:
                c = est.chi(arr); c2 = est.chi(arr.copy())
                if c.view(np.uint32) != c2.view(np.uint32): raise RuntimeError("NONDETERMINISTIC")
                row["chi_bits_hex"] = hex(int(c.view(np.uint32)))
                if c == 0 or not np.isfinite(c): row["status"] = "UNSCORED"; unscored += 1
                else: s = 1 if c > 0 else -1; row["status"] = "SCORED"; row["match"] = bool(s == g); m += 1; k += int(s == g)
            except Exception as e:
                row["status"] = "UNSCORED"; row["error"] = repr(e)[:120]; unscored += 1
            jf.write(json.dumps(row, sort_keys=True) + "\n")
    return k, m, unscored

def tune(manifest, tensors, out, identity, proto=PRODUCTION):
    out = Path(out); out.mkdir(parents=True, exist_ok=True); env = enforce_environment()
    I, idsha = load_identity(identity, proto)
    objs, mf = load_manifest(manifest, tensors, proto.n_tune, required_objids=I["tuning_objids"]); n = proto.n_tune; start = utc(); mf["corpus_identity_sha256"] = idsha; mf["identity_witness"] = I["_witness"]
    J = out / "tuning_journal.jsonl"; R = out / "tuning_receipts.jsonl"; J.write_text(""); R.write_text("")
    receipts = []
    for idx, cfg in enumerate(fc.enumerate_configs()):
        est = fc.Estimator(cfg); k, m, un = score_config(est, objs, J, idx)
        k_eff = max(k, m - k) if m else 0
        rec = {"config_index": idx, "config_id": est.config_id, "config": cfg, "n": n, "m_scored": m, "unscored": un, "k": k, "k_eff": k_eff,
               "objective_p_val_over_n": k_eff / n, "eligible": m >= proto.floor_tune, "floor_tune": proto.floor_tune, "protocol": proto.label, **env, **mf}
        receipts.append(rec)
        with open(R, "a") as rf: rf.write(json.dumps(rec, sort_keys=True) + "\n")
    elig = [r for r in receipts if r["eligible"]]
    winner = sorted(elig, key=lambda r: (-r["objective_p_val_over_n"], r["unscored"], r["config_index"]))[0] if elig else None
    root_parts = {"tuning_journal.jsonl": sha_file(J), "tuning_receipts.jsonl": sha_file(R), "manifest": mf["manifest_sha256"], "tensor_set": mf["tensor_set_sha256"],
                  "corpus_identity": idsha, "estimator": sha_file(HERE / "fourier_chirality.py"), "driver": sha_file(__file__), "env_lock": env["env_lock_sha256"]}
    run_root = hashlib.sha256("\n".join(f"{k}:{v}" for k, v in sorted(root_parts.items())).encode()).hexdigest()
    summary = {"mode": "tune", "protocol": proto.label, "start_utc": start, "end_utc": utc(), "n_configs": len(receipts), "n_eligible": len(elig),
               "winner": winner, "winner_config_id": None if winner is None else winner["config_id"], "journal_sha256": sha_file(J), "receipts_sha256": sha_file(R),
               "run_root_parts": root_parts, "run_root_sha256": run_root,
               "estimator_sha256": sha_file(HERE / "fourier_chirality.py"), "driver_sha256": sha_file(__file__), **env, **mf}
    (out / "selection_summary.json").write_text(json.dumps(summary, indent=1, sort_keys=True))
    return summary

def reconstruct_winner(receipts_path, journal_path, proto):
    """Recompute the tuning winner from the 96 receipts, RECONCILED against the per-object journal, and the LIVE enumeration; the
    summary's fields are never trusted, and a receipt whose k/m/unscored differ from the journal rows it summarises is refused."""
    with open(receipts_path) as fh: recs = [json.loads(l) for l in fh]
    per = {}
    with open(journal_path) as fh:
        for l in fh:
            row = json.loads(l); d = per.setdefault(row["config_index"], {"k": 0, "m": 0, "un": 0, "ids": set(), "cid": row["config_id"]})
            if row["objid"] in d["ids"]: raise DataIntegrityFail(f"TUNING-JOURNAL-DUPLICATE {row['config_index']} {row['objid']}")
            d["ids"].add(row["objid"])
            if row["status"] == "SCORED": d["m"] += 1; d["k"] += int(row["match"])
            else: d["un"] += 1
    cfgs = fc.enumerate_configs()
    if len(recs) != len(cfgs): raise DataIntegrityFail(f"TUNING-RECEIPTS-COUNT {len(recs)} != {len(cfgs)}")
    for i, (r, cfg) in enumerate(zip(recs, cfgs)):
        if r["config_index"] != i or r["config"] != cfg or r["config_id"] != fc.config_id(cfg): raise DataIntegrityFail(f"TUNING-RECEIPT-{i}-CONFIG")
        if r["n"] != proto.n_tune or r["m_scored"] + r["unscored"] != proto.n_tune: raise DataIntegrityFail(f"TUNING-RECEIPT-{i}-COUNTS")
        j = per.get(i)
        if j is None or len(j["ids"]) != proto.n_tune or j["cid"] != r["config_id"] or (j["k"], j["m"], j["un"]) != (r["k"], r["m_scored"], r["unscored"]):
            raise DataIntegrityFail(f"TUNING-RECEIPT-{i}-JOURNAL-MISMATCH: receipt k/m/unscored do not match the per-object journal")
        k_eff = max(r["k"], r["m_scored"] - r["k"]) if r["m_scored"] else 0
        if r["k_eff"] != k_eff or abs(r["objective_p_val_over_n"] - k_eff / proto.n_tune) > 1e-12 or r["eligible"] != (r["m_scored"] >= proto.floor_tune): raise DataIntegrityFail(f"TUNING-RECEIPT-{i}-DERIVED")
    elig = [r for r in recs if r["eligible"]]
    return sorted(elig, key=lambda r: (-r["objective_p_val_over_n"], r["unscored"], r["config_index"]))[0] if elig else None

def holdout(tuning_receipt, manifest, tensors, out, identity, proto=PRODUCTION):
    out = Path(out); out.mkdir(parents=True, exist_ok=True); env = enforce_environment()
    I, idsha = load_identity(identity, proto)
    T = json.loads(Path(tuning_receipt).read_text()); tdir = Path(tuning_receipt).parent
    if T.get("mode") != "tune" or T.get("protocol") != proto.label: raise DataIntegrityFail("TUNING-RECEIPT-MODE")
    rsha = sha_file(tdir / "tuning_receipts.jsonl")
    if sha_file(tdir / "tuning_journal.jsonl") != T["journal_sha256"] or rsha != T["receipts_sha256"]: raise DataIntegrityFail("TUNING-RECEIPT-HASHES")
    parts = dict(T.get("run_root_parts", {}))
    live = {"tuning_journal.jsonl": sha_file(tdir / "tuning_journal.jsonl"), "tuning_receipts.jsonl": rsha, "estimator": sha_file(HERE / "fourier_chirality.py"), "driver": sha_file(__file__), "env_lock": env["env_lock_sha256"]}
    if any(parts.get(k) != v for k, v in live.items()): raise DataIntegrityFail("RUN-ROOT-PARTS-DIFFER: journal/receipts/estimator/driver/env differ from the tuning run")
    run_root = hashlib.sha256("\n".join(f"{k}:{v}" for k, v in sorted(parts.items())).encode()).hexdigest()
    if run_root != T.get("run_root_sha256"): raise DataIntegrityFail("RUN-ROOT-MISMATCH")
    if not journal_has(proto.seal_journal, "tuning-freeze", run_root): raise DataIntegrityFail(f"TUNING-NOT-SEALED run_root {run_root}")
    tw = verify_witness(proto.seal_journal, "tuning-freeze", run_root, proto)
    for name in ("tuning_receipts.jsonl", "tuning_journal.jsonl", "selection_summary.json"):
        if not blob_at_commit_equals(tw["_root"], tw["commit"], tdir / name): raise DataIntegrityFail(f"TUNING-FILE-NOT-IN-WITNESS-COMMIT {name}")
    tw = {k: v for k, v in tw.items() if k != "_root"}
    if T["estimator_sha256"] != sha_file(HERE / "fourier_chirality.py"): raise DataIntegrityFail("ESTIMATOR-CHANGED-SINCE-TUNING")
    if T.get("corpus_identity_sha256") != idsha: raise DataIntegrityFail("IDENTITY-DIFFERS-FROM-TUNING")
    W = reconstruct_winner(tdir / "tuning_receipts.jsonl", tdir / "tuning_journal.jsonl", proto)
    if W is None: raise DataIntegrityFail("NO-TUNING-WINNER")
    if T.get("winner") is None or T["winner"].get("config") != W["config"] or T["winner"].get("config_index") != W["config_index"] or T.get("winner_config_id") != W["config_id"]:
        raise DataIntegrityFail("WINNER-SUBSTITUTED: summary winner differs from the winner reconstructed from the sealed receipts")
    est = fc.Estimator(W["config"])
    objs, mf = load_manifest(manifest, tensors, proto.n_hold, required_objids=I["holdout_objids"]); mf["corpus_identity_sha256"] = idsha; mf["identity_witness"] = I["_witness"]; mf["tuning_witness"] = tw
    with open(tdir / "tuning_journal.jsonl") as fh: tune_ids = {json.loads(l)["objid"] for l in fh}
    if any(o[0] in tune_ids for o in objs): raise DataIntegrityFail("HOLDOUT-OVERLAPS-TUNING")
    n = proto.n_hold; start = utc(); J = out / "holdout_journal.jsonl"; J.write_text("")
    k, m, un = score_config(est, objs, J, W["config_index"]); k_eff = max(k, m - k) if m else 0
    if m < proto.floor_hold: verdict, wl = "CLOSED: holdout floor", None
    else:
        wl = wilson_lower(k_eff, n); verdict = "PASS" if wl > THRESHOLD else "CLOSED: holdout strength"
    summary = {"mode": "holdout", "protocol": proto.label, "start_utc": start, "end_utc": utc(), "config_id": est.config_id, "config": W["config"], "tuning_receipt_sha256": sha_file(tuning_receipt), "tuning_receipts_jsonl_sha256": rsha, "tuning_run_root_sha256": run_root,
               "n": n, "m_scored": m, "unscored": un, "k": k, "k_eff": k_eff, "p_val_over_n": k_eff / n, "wilson_lower": wl, "floor_hold": proto.floor_hold, "threshold": THRESHOLD,
               "verdict": verdict, "journal_sha256": sha_file(J), "estimator_sha256": sha_file(HERE / "fourier_chirality.py"), "driver_sha256": sha_file(__file__), **env, **mf}
    (out / "holdout_summary.json").write_text(json.dumps(summary, indent=1, sort_keys=True))
    return summary

def main(argv=None):
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="mode", required=True)
    t = sub.add_parser("tune"); t.add_argument("--manifest", required=True); t.add_argument("--tensors", required=True); t.add_argument("--out", required=True); t.add_argument("--identity", required=True)
    h = sub.add_parser("holdout"); h.add_argument("--tuning-receipt", required=True); h.add_argument("--manifest", required=True); h.add_argument("--tensors", required=True); h.add_argument("--out", required=True); h.add_argument("--identity", required=True)
    a = ap.parse_args(argv)
    try:
        s = tune(a.manifest, a.tensors, a.out, a.identity) if a.mode == "tune" else holdout(a.tuning_receipt, a.manifest, a.tensors, a.out, a.identity)
    except DataIntegrityFail as e:
        print("DATA-INTEGRITY-FAIL", e); return 2
    print(json.dumps({k: s.get(k) for k in ("mode", "n_eligible", "winner_config_id", "verdict", "m_scored", "k_eff", "wilson_lower")})); return 0
if __name__ == "__main__":
    sys.exit(main())

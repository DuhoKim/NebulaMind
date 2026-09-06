"""run_configurations_v12 — V28 STAGED CANDIDATE (codex V27-1/2/3; Blanc 02:06 KST 09-07: contradictions between text and code, REPAIRED, not disclosed as limits):
composed mode on provenance_designs_v8 — locally decidable input mismatches are decided BEFORE any retrieval; same-id contradictions before any retry shortcut; delivery
is TRI-STATE through the witness-commit precheck (UNDETERMINED → RETRY-EVENTS-UNAVAILABLE in composed mode / IDENTITY-WITNESS-COMMIT-UNDETERMINED offline, where no
retry vocabulary exists; positive non-delivery → EVENT-INCONSISTENT: IDENTITY-WITNESS-COMMIT in composed mode / IDENTITY-WITNESS-COMMIT offline) and through the open-event
stage (validate_continuation_v8: EVIDENCE-UNAVAILABLE retry / OPEN-EVENT-INCONSISTENT-INPUT terminal). v11 was: V27 STAGED CANDIDATE (codex V26-1/2/3): composed mode on provenance_designs_v7 — a same-event contradiction is terminal (EVENT-FORGED),
an undeterminable delivery is RETRY-EVENTS-UNAVAILABLE, a retained event that does not deliver the commit is EVENT-INCONSISTENT, a non-earliest event is EVENT-NOT-EARLIEST;
EVIDENCE-EXPIRED is a loss, not a retry. LINEAGE, stated accurately (the v10 docstring's historical lines were over-renamed by a regex — codex V26-3 — and are
replaced here by this table rather than repaired in place): v4 (V20, refused: production re-deriver missing) → v5 (V21: PRODUCTION re-deriver bound; full conjunction)
→ v6 (V22: W4 in the driver, CLOSED terminal, sentinel completeness, verify_split, composed mode on provenance_designs_v2) → v7 (V23: composed on provenance_designs_v3)
→ v8 (V24: composed on provenance_designs_v4) → v9 (V25: composed on provenance_designs_v5) → v10 (V26: composed on provenance_designs_v6) → v11 (V27: composed on provenance_designs_v7) → v12 (this; V28: composed on provenance_designs_v8, tri-state witness precheck).
[V27-3, codex: the v11 table's v10 row said provenance_designs_v7; v10's bytes import provenance_designs_v6. This table was re-verified row by row against each retained driver's own
`import provenance_designs_vN as P` line: v6→v2, v7→v3, v8→v4, v9→v5, v10→v6, v11→v7, v12→v8.]
Every predecessor's bytes are retained at its own path; their own docstrings are authoritative for their own versions.
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
def _P():
    """the track-2 helpers (v8), imported lazily: used by the witness-commit precheck in every mode and by composed mode."""
    sys.path.insert(0, str(HERE.parents[0] / "track2")); import provenance_designs_v8 as P; return P
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
    rederive_seed: object = None                                                # v5: bound below to production_rederive_seed (a REAL offline drand-only verdict); None is refused
    render_journal: str = str(HERE.parents[0] / "dev_corpus" / "render_journal_{group}.jsonl")   # v5: the adapter's journal per group (dev_corpus_pipeline --journal); sentinel rows reconciled against it
    holdout_once: bool = False                                                  # INHERITED — PREPARED, NOT ADOPTED (V15 §7 one holdout is text only): True refuses a second holdout invocation
    holdout_marker: str = str(HERE.parents[0] / "HOLDOUT_INVOKED.marker")       # persisted marker for holdout_once
    approval_glob: str = "APPROVAL_RECORD_SELRULE_V22*"                          # v6: W4 in the driver — exactly one record path for this glob in all history
    provenance_mode: str = "offline"                                            # v6, UNADOPTED: "offline" (the candidate as reviewed at V21: retained bytes only) | "composed" (track-2 v8 helpers on this call path)
    events_runner: object = None                                                # composed mode: the `gh api` runner (production: provenance_designs_v8.gh_runner; tests inject a labelled fixture runner)
    events_repo: str = "DuhoKim/NebulaMind"                                     # composed mode: the pinned repository whose live events are queried
    history_open_event_file: str = str(HERE.parents[0] / "HISTORY_OPEN_EVENT.json")     # v7 composed mode: the RETAINED PushEvent that delivered the history-open (genesis-only) commit; authenticated live at load
    events_receipt: str = ""                                                    # composed mode, EXPIRED path: the independent receipt path ("" = no expired path; Q1/Q2 for Duho unanswered)
    expected_receipt_origin: object = None                                      # composed mode: the expected origin label — PROPOSED BY THE LANE (ops-witness), unadopted, not a user decision (QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md)
    verify_split: bool = False                                                  # v6, UNADOPTED (inherited limitation C11): recompute the split from catalogue bytes
    pool_csv: str = str(HERE.parents[0] / "corpus_identity" / "guarded_pool.csv")
    exclusion_file: str = str(HERE.parents[0] / "corpus_identity" / "dryrun_identities_to_exclude_20260905.txt")
    bricks_table: str = str(HERE.parents[1] / "scratch" / "survey-bricks-dr9-north.fits.gz")
    no_r_registry: str = str(HERE.parents[1] / "validation_bricks" / "_bricks_without_r_coverage.txt")

def _drand_modules():
    """Lazy import of the pinned verifier stack (py_ecc via the lane venv on PYTHONPATH). Absence is a refusal, never a pass."""
    try:
        sys.path.insert(0, str(HERE.parents[0] / "beacon_v2")); sys.path.insert(0, str(HERE.parents[0] / "drand_only")); sys.path.insert(0, str(HERE.parents[0] / "corpus_identity"))
        import beacon_record_drand_v28 as BD, verify_drand_v2 as vd, approval_witness_v4 as AW, history_v2 as H
        return BD, vd, AW, H
    except ImportError as e: raise DataIntegrityFail(f"VERIFIER-UNAVAILABLE: {e!r} — run under the pinned interpreter with the lane venv site-packages on PYTHONPATH")

def production_rederive_seed(record_path, rule_sha256, statement_bytes):
    """THE PRODUCTION RE-DERIVER (v5): the drand-only verdict recomputed OFFLINE (fetch=None) from the retained BEACON-RECORD-4 bytes, bound to
    the adopted rule digest and the approval record bytes. Returns (seed_hex, verdict). Anything but ACCEPT-DRAND is a refusal."""
    from datetime import datetime, timezone
    BD, vd, AW, H = _drand_modules()
    try: rec = json.loads(Path(record_path).read_text())
    except Exception as e: raise DataIntegrityFail(f"BEACON-RECORD-UNREADABLE {e!r}")
    r = BD.verdict(rec, datetime.now(timezone.utc), fetch=None, rule_sha256=rule_sha256, statement_bytes=statement_bytes)
    if r.get("outcome") != "ACCEPT-DRAND": raise DataIntegrityFail(f"REDERIVE-{r.get('outcome')}: {r.get('why')}")
    return r["seed_hex"], r

PRODUCTION = Protocol(rederive_seed=production_rederive_seed)

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
    if not Path(identity_path).is_file(): raise DataIntegrityFail(f"IDENTITY-MISSING {identity_path}")   # v5: v2–v4 tested `sha_file(...) is None`, which never held (sha_file raises) — the branch was unreachable
    d = sha_file(identity_path)
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
    if proto.require_beacon:                                                                               # v5: the FULL conjunction from COMMITTED evidence (codex V20 M1/M2/W3/W5)
        import subprocess, base64
        from datetime import datetime, timezone
        BD, vd, AW, H = _drand_modules()
        def git_out(*args):
            r = subprocess.run(["git", *args], cwd=w_root, capture_output=True, text=True); return r.stdout if r.returncode == 0 else None
        if I.get("beacon_outcome") != "ACCEPT-DRAND": raise DataIntegrityFail(f"IDENTITY-BEACON-NOT-ACCEPTED {I.get('beacon_outcome')} (only ACCEPT-DRAND is admissible)")
        if I.get("beacon_source") != "drand-mainnet-default": raise DataIntegrityFail("IDENTITY-SOURCE: not the pinned drand chain")
        w = I.get("approval_witness") or {}
        for k in ("commit", "record_path", "record_sha256", "push_event", "push_event_sha256", "events_provenance", "nonce_round", "nonce_randomness", "nonce_bodies_b64"):
            if k not in w: raise DataIntegrityFail(f"IDENTITY-WITNESS-MISSING: {k} absent")
        commit = str(w["commit"]); rel = str(w["record_path"])
        if not re.fullmatch(r"[0-9a-f]{40}", commit): raise DataIntegrityFail("IDENTITY-WITNESS-COMMIT: malformed")
        # --- the approval record, from the repository (W1, W2, W4 recomputed here)
        ap_rec = Path(w_root) / rel
        if not ap_rec.is_file(): raise DataIntegrityFail(f"APPROVAL-RECORD-MISSING {rel}")
        ap_bytes = ap_rec.read_bytes()
        if hashlib.sha256(ap_bytes).hexdigest() != w["record_sha256"]: raise DataIntegrityFail("APPROVAL-RECORD-DIGEST: on-disk record differs from the witness")
        if not blob_at_commit_equals(w_root, commit, ap_rec): raise DataIntegrityFail("APPROVAL-RECORD-NOT-AT-COMMIT: not a byte-equal blob at the approval commit")
        adds = (git_out("log", "--diff-filter=A", "--format=%H", "--", rel) or "").split(); touches = (git_out("log", "--format=%H", "--", rel) or "").split()
        if adds != [commit] or touches != [commit]: raise DataIntegrityFail("APPROVAL-RECORD-HISTORY: the record must be added once, by the approval commit, and never touched")
        if subprocess.run(["git", "merge-base", "--is-ancestor", commit, proto.witness_remote_ref], cwd=w_root, capture_output=True).returncode != 0: raise DataIntegrityFail("APPROVAL-COMMIT-NOT-PUSHED")
        paths = {l for l in (git_out("log", "--all", "--diff-filter=A", "--name-only", "--format=", "--", proto.approval_glob) or "").split("\n") if l.strip()}   # v6 (C2): W4 in the driver
        if paths != {rel}: raise DataIntegrityFail(f"APPROVAL-NOT-FIRST: approval-record paths for this version in history: {sorted(paths)}")
        text = ap_bytes.decode("utf-8", "replace"); dg = AW.DIGEST_RE.findall(text); ts = AW.TSIGN_RE.findall(text); nn = AW.NONCE_RE.findall(text)
        if len(dg) != 1 or dg[0] != adopted: raise DataIntegrityFail("APPROVAL-RULE-LINE: the record's RULE_SHA256 is not the adopted digest (or not exactly one line)")
        if len(ts) != 1 or ts[0] != I.get("T_sign"): raise DataIntegrityFail("APPROVAL-T-SIGN-LINE: APPROVAL_UTC is not the identity's T_sign (or not exactly one line)")
        if len(nn) != 1 or int(nn[0][0]) != w["nonce_round"] or nn[0][1] != w["nonce_randomness"]: raise DataIntegrityFail("APPROVAL-NONCE-LINE: the record's nonce is not the witness's (or not exactly one line)")
        # --- times and round, re-derived from T_sign
        try: t_sign = BD.parse_utc(I["T_sign"]); t_pulse = BD.pulse_time(t_sign)
        except Exception: raise DataIntegrityFail("IDENTITY-T-SIGN: unparsable")
        tp = BD.fmt(t_pulse); rnd = vd.round_for(t_pulse)
        if I.get("T_pulse") != tp or I.get("beacon_t_pulse") != tp: raise DataIntegrityFail("IDENTITY-T-PULSE: not T_sign + 600 s rounded to the minute")
        if I.get("beacon_round") != rnd: raise DataIntegrityFail("IDENTITY-ROUND: not round_for(T_pulse)")
        if t_sign < BD.parse_utc(BD.MIN_T_SIGN): raise DataIntegrityFail("IDENTITY-T-SIGN-PREDATES-AMENDMENT")
        if tp in BD.EXCLUDED_T_PULSE or rnd in BD.EXCLUDED_ROUNDS: raise DataIntegrityFail("IDENTITY-T-PULSE-EXCLUDED")
        # --- the push event (W3), from its own bytes
        ev = w["push_event"]; pay = (ev or {}).get("payload") or {}
        if not isinstance(ev, dict) or ev.get("type") != "PushEvent" or pay.get("ref") != proto.witness_branch_ref: raise DataIntegrityFail("IDENTITY-WITNESS-MISSING: no PushEvent for the protected ref in the identity")
        try: created = datetime.fromisoformat(str(ev.get("created_at")).replace("Z", "+00:00")).astimezone(timezone.utc)
        except Exception: raise DataIntegrityFail("IDENTITY-WITNESS-TIME: unparsable created_at")
        if created >= t_pulse: raise DataIntegrityFail("IDENTITY-WITNESS-LATE: the approval push time is not before T_pulse")
        if hashlib.sha256(json.dumps(ev, sort_keys=True, separators=(",", ":")).encode()).hexdigest() != w["push_event_sha256"]: raise DataIntegrityFail("EVENT-DIGEST: the retained event's digest is not the witness's")
        dvw = _P().delivery(ev, commit, proto.witness_branch_ref, w_root)                                   # v12 (codex V27-2): TRI-STATE on the complete path — the same predicate composed mode uses
        if dvw == "NOT-DELIVERED": raise DataIntegrityFail(("EVENT-INCONSISTENT: " if proto.provenance_mode == "composed" else "") + "IDENTITY-WITNESS-COMMIT: the push event positively does not deliver the approval commit (head, commits, or before..head ancestry established false)")
        if dvw == "UNDETERMINED": raise DataIntegrityFail(("RETRY-EVENTS-UNAVAILABLE: " if proto.provenance_mode == "composed" else "") + "IDENTITY-WITNESS-COMMIT-UNDETERMINED: the push event's before..head delivery of the approval commit could not be established here (a git object missing locally, a failed or unlaunchable git command) — not evidence of anything; fetch the objects and retry")
        prov = w["events_provenance"] or {}
        if not (isinstance(prov, dict) and prov.get("endpoints") and prov.get("retrieved_utc")): raise DataIntegrityFail("EVENT-PROVENANCE: endpoints / retrieval time absent")
        # --- the nonce (W5), re-verified by BLS from the retained bodies
        R = w["nonce_round"]; rand = str(w["nonce_randomness"]); r_sign = vd.round_for(t_sign)
        if not isinstance(R, int) or R not in (r_sign - 1, r_sign): raise DataIntegrityFail(f"IDENTITY-WITNESS-NONCE: round {R} not in {{{r_sign - 1}, {r_sign}}}")
        if vd.round_time(R) < BD.parse_utc(BD.MIN_T_SIGN) or not R < rnd: raise DataIntegrityFail("IDENTITY-WITNESS-NONCE: scheduled before MIN_T_SIGN or not before the seed round")
        if len(AW.verify_nonce_bodies(w["nonce_bodies_b64"], R, rand)) < AW.MIN_NONCE_RELAYS: raise DataIntegrityFail("NONCE-UNAUTHENTICATED: fewer than 2 retained relay bodies BLS-verify for the nonce round with this randomness")
        # --- adoption at the approval commit
        ap = Path(proto.adoption_file); raw = ap.read_bytes() if ap.is_file() else b""
        lines = raw.decode("utf-8", "replace").split("\n")
        if not (len(lines) == 2 and lines[1] == "" and lines[0] == adopted): raise DataIntegrityFail("ADOPTION-MALFORMED: exactly one 64-hex line and one newline, equal to the adopted digest")
        if not blob_at_commit_equals(w_root, commit, ap): raise DataIntegrityFail("ADOPTION-NOT-AT-APPROVAL-COMMIT: the adoption file is not a byte-equal blob at the approval commit")
        if I.get("adoption_sha256") != sha_file(ap): raise DataIntegrityFail("ADOPTION-DIGEST: identity's adoption digest differs from the file")
        # --- the AUTHENTICATED history
        rec_sha = I["beacon_record_sha256"]; lk = I.get("collection_lock") or {}; lp = Path(proto.collection_log)
        if not lp.is_file() or sha_file(lp) != lk.get("log_sha256"): raise DataIntegrityFail("COLLECTION-LOG-DIGEST: the committed collection log differs from the identity's record of it")
        if not blob_at_commit_equals(w_root, I["_witness"]["commit"], lp): raise DataIntegrityFail("COLLECTION-LOG-NOT-IN-WITNESS-COMMIT")
        try: entries = H.validate(lp)
        except ValueError as e: raise DataIntegrityFail(f"HISTORY-INVALID: {e}")
        g = entries[0]
        if (g.get("approval_record_sha256"), g.get("t_pulse"), g.get("rule_sha256"), g.get("round")) != (w["record_sha256"], tp, adopted, rnd): raise DataIntegrityFail("HISTORY-GENESIS: the history's genesis does not name this approval record, T_pulse, rule and round")
        if lk.get("entries") != len(entries): raise DataIntegrityFail("HISTORY-COUNT: the identity's entry count differs from the chain")
        fa, conf = H.first_accept(entries)
        if fa is None: raise DataIntegrityFail("COLLECTION-LOG-EMPTY: no builder ACCEPT in the committed history")
        if fa.get("record_sha256") != rec_sha or fa.get("outcome") != I["beacon_outcome"] or fa.get("seed_hex") != I["seed_hex"]: raise DataIntegrityFail("IDENTITY-LOCK-MISMATCH: the first logged ACCEPT does not name this identity's record, outcome and seed")
        if (lk.get("first_accept") or {}) != fa: raise DataIntegrityFail("IDENTITY-LOCK-MISMATCH: identity's first_accept differs from the chain's")
        if any(e.get("stage") == "witness-closed" for e in entries): raise DataIntegrityFail("COLLECTION-CLOSED: a witness-closed entry is on record — the commitment is closed; nothing redraws")   # v6 (C3): terminal
        if conf or any(e.get("stage") == "builder-conflict" for e in entries): raise DataIntegrityFail("COLLECTION-LOG-CONFLICT: a conflicting later accept is on record")
        # --- the beacon record, and the seed re-derived from it by the PRODUCTION re-deriver
        rp = Path(proto.beacon_record_path)
        if not rp.is_file() or sha_file(rp) != rec_sha: raise DataIntegrityFail("BEACON-RECORD-DIGEST: the retained beacon record differs from the identity's")
        if not blob_at_commit_equals(w_root, I["_witness"]["commit"], rp): raise DataIntegrityFail("BEACON-RECORD-NOT-IN-WITNESS-COMMIT")
        try: rec = json.loads(rp.read_text())
        except Exception: raise DataIntegrityFail("BEACON-RECORD-UNREADABLE")
        if (rec.get("T_sign"), rec.get("T_pulse"), rec.get("round"), rec.get("rule_sha256")) != (I["T_sign"], tp, rnd, adopted): raise DataIntegrityFail("BEACON-RECORD-BINDING: the record's T_sign/T_pulse/round/rule differ from the identity's")
        try: stmt_ok = base64.b64decode(rec.get("statement_b64", "")) == ap_bytes
        except Exception: stmt_ok = False
        if not stmt_ok: raise DataIntegrityFail("BEACON-RECORD-STATEMENT: the record's statement bytes are not the committed approval record")
        pinned = BD.pinned_urls(rnd); bodies = [u for u, r in (rec.get("relays") or {}).items() if u in pinned and isinstance(r, dict) and "body_b64" in r]
        if len(bodies) < BD.MIN_HOSTS: raise DataIntegrityFail("BEACON-RECORD-RELAYS: fewer than 2 distinct pinned relay bodies retained")
        seed, rv = proto.rederive_seed(rp, adopted, ap_bytes)
        if seed != I["seed_hex"] or rv.get("round") != rnd: raise DataIntegrityFail("IDENTITY-SEED-NOT-REDERIVED: the seed does not follow from the retained beacon evidence")
        if proto.verify_split: verify_split_from_catalogue(I, proto)                                  # v6, UNADOPTED: off by default
        if proto.provenance_mode == "composed": composed_provenance(I, proto, w_root, ev, commit, lp)   # v6, UNADOPTED: the track-2 helpers (v8 now) ON THIS CALL PATH (default "offline")
    for k, n in (("tuning_objids", proto.n_tune), ("holdout_objids", proto.n_hold), ("fresh_validation_objids", proto.n_fresh)):
        if len(I.get(k, [])) != n or len(set(I[k])) != n or not all(isinstance(x, int) for x in I[k]): raise DataIntegrityFail(f"IDENTITY-{k}-SIZE-OR-TYPE")
    a, b, c = set(I["tuning_objids"]), set(I["holdout_objids"]), set(I["fresh_validation_objids"])
    if (a & b) or (a & c) or (b & c): raise DataIntegrityFail("IDENTITY-OVERLAP")
    return I, d

def load_manifest(path, tensors, n_required, required_objids=None, render_journal=None):
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
    reconcile_sentinels(rows, render_journal)                                                          # v5: every sentinel is a journalled refusal, and vice versa
    return objs, {"manifest_sha256": sha_file(path), "n": len(objs), "tensor_set_sha256": hashlib.sha256("".join(sorted(r["tensor_sha256"] for r in rows)).encode()).hexdigest(), "sentinel_count": sentinel}

def composed_provenance(I, proto, w_root, ev, commit, log_path):
    """UNADOPTED COMPOSED MODE (v12 on provenance_designs_v8; Blanc 21:14 — the recommended mode exercised on the production call path, not in isolation). After every offline
    check has passed: (a) the retained PushEvent is authenticated against a LIVE retrieval of the pinned repository's events through the runner
    (production: `gh api`; fixtures inject a labelled runner) — AUTHENTIC loads; FORGED refuses; UNAVAILABLE refuses as RETRY; EXPIRED refuses unless
    an independent receipt is configured AND verifies (`events_receipt`; its expected origin label is the lane's proposal `ops-witness`, unadopted — with no receipt path configured
    the EXPIRED path is closed, i.e. Q1 Option C); (b) the collection history's continuation is validated against the LIVE remote head
    (`validate_continuation_v8`: ls-remote on the pinned URL, push-acknowledgement boundary, tri-state open-event stage) from the witnessed history-open commit."""
    P = _P(); runner = proto.events_runner or P.gh_runner
    o, why, prov = P.authenticate_event_live(ev, proto.events_repo, runner, proto.witness_branch_ref, commit, root=w_root)
    if o == "AUTHENTIC": pass
    elif o == "UNAVAILABLE": raise DataIntegrityFail(f"RETRY-EVENTS-UNAVAILABLE: {why}")
    elif o == "INCOMPLETE": raise DataIntegrityFail(f"RETRY-EVENTS-INCOMPLETE: {why}")                                  # v10 (codex V25 P2): absence is not forgery
    elif o == "INCONSISTENT-INPUT": raise DataIntegrityFail(f"EVENT-INCONSISTENT: {why}")                                # v11 (codex V26-2): a positive input mismatch, named as such
    elif o == "NOT-EARLIEST": raise DataIntegrityFail(f"EVENT-NOT-EARLIEST: {why}")
    elif o == "EXPIRED":
        if not proto.events_receipt or proto.expected_receipt_origin is None: raise DataIntegrityFail(f"EVENT-EXPIRED-NO-RECEIPT-PATH: {why}; no independent receipt path is configured (Q1 Option C)")
        ok, rwhy = P.verify_events_receipt(proto.events_receipt, w_root, proto.witness_remote_url, proto.witness_branch_ref, ev, proto.expected_receipt_origin)
        if not ok: raise DataIntegrityFail(f"EVENT-EXPIRED-RECEIPT-REFUSED: {rwhy}")
    else: raise DataIntegrityFail(f"EVENT-FORGED: {why}")
    try: open_event = json.loads(Path(proto.history_open_event_file).read_text())
    except Exception as e: raise DataIntegrityFail(f"HISTORY-OPEN-EVENT-MISSING: the retained history-open PushEvent is absent or unreadable ({e!r})")
    ok, hwhy, info = P.validate_continuation_v8(w_root, Path(log_path).resolve().relative_to(Path(w_root).resolve()).as_posix(), proto.witness_remote_url, proto.witness_branch_ref, open_event, runner, proto.events_repo)
    if not ok: raise DataIntegrityFail(("RETRY-" if hwhy.startswith(("EVIDENCE-UNAVAILABLE", "EVIDENCE-INCOMPLETE")) else "") + f"HISTORY-CONTINUATION: {hwhy}")   # v10: UNAVAILABLE/INCOMPLETE are RETRY; EVIDENCE-EXPIRED (the feed no longer reaches the event) is a loss, not a retry
    I["_composed"] = {"event": o, "events_provenance": prov, "history": hwhy, "remote_head": info.get("remote_head")}

def verify_split_from_catalogue(I, proto):
    """UNADOPTED (v6; inherited limitation C11 of the V15 driver): recompute the §3b split from the pinned catalogue files and the identity's seed —
    guarded pool (digest must equal proto.pool_sha256), exclusion file (proto.exclusion_sha256), the failed set = ranks 1–2000 of the unseeded order,
    survey-bricks table and no-r registry — and require tuning/holdout/fresh lists to be EXACTLY the recomputed ones. Reads no pixel and no label
    beyond the pool's own column; touches no sample. Adopting it is Duho's call (it changes what the signed driver takes on trust)."""
    sys.path.insert(0, str(HERE.parents[0] / "corpus_identity")); import build_corpus_identity_v28 as B22, csv as _csv
    if sha_file(proto.pool_csv) != proto.pool_sha256 or sha_file(proto.exclusion_file) != proto.exclusion_sha256: raise DataIntegrityFail("SPLIT-INPUTS: pool or exclusion file differs from the pinned digests")
    with open(proto.pool_csv, newline="") as f: rows = [{"objid": int(r["GZ1_OBJID"]), "ra": float(r["RA"]), "dec": float(r["DEC"]), "g": int(r["G"])} for r in _csv.DictReader(f)]
    ordered = B22.order_rows(rows); failed = {r["objid"] for r in ordered[:2000]}; excluded = {int(x) for x in Path(proto.exclusion_file).read_text().split() if x.strip()}
    population = B22.order_rows([r for r in rows if r["objid"] not in failed and r["objid"] not in excluded], I["seed_hex"])
    bricks = B22.load_bricks(proto.bricks_table)
    with open(proto.no_r_registry) as f: no_r = {x.strip() for x in f if x.strip()}
    groups, skipped, last = B22.classify(population, bricks, no_r, start_rank=1, counts=(proto.n_tune, proto.n_hold, proto.n_fresh))
    for k, g in zip(("tuning_objids", "holdout_objids", "fresh_validation_objids"), groups):
        if [r["objid"] for r in g] != list(I[k]): raise DataIntegrityFail(f"SPLIT-NOT-REPRODUCED: {k} differs from the split recomputed from the catalogue and the seed")

def reconcile_sentinels(rows, render_journal):
    """ADAPTER RECONCILIATION (v5, codex V20 S): a sentinel row must correspond to a render-journal entry for that objid with status REFUSED and
    sentinel true; a REFUSED journal entry for a manifest objid must correspond to a sentinel row; the journal's render-end refused count (when
    present) must equal the manifest's sentinel count. Sentinels without a journal are refused — a refusal cause never goes unrecorded."""
    sent = {str(r["objid"]) for r in rows if r["tensor_sha256"] == SENTINEL_SHA256}; ids = {str(r["objid"]) for r in rows}
    if not sent and (render_journal is None or not Path(render_journal).is_file()): return
    if render_journal is None or not Path(render_journal).is_file(): raise DataIntegrityFail(f"SENTINEL-WITHOUT-RENDER-JOURNAL: {len(sent)} sentinel rows and no render journal")
    refused = set(); ends = []; last_relevant = None
    for l in Path(render_journal).read_text().splitlines():
        if not l.strip(): continue
        try: j = json.loads(l)
        except Exception: raise DataIntegrityFail("RENDER-JOURNAL-MALFORMED")
        if j.get("event") == "render-end": ends.append(j); last_relevant = j
        if str(j.get("objid")) in ids: last_relevant = j
        if str(j.get("objid")) in ids and (j.get("status") == "REFUSED" or j.get("sentinel") is True):
            if not (j.get("status") == "REFUSED" and j.get("sentinel") is True and j.get("tensor_sha256") == SENTINEL_SHA256 and str(j.get("reason") or "").strip()): raise DataIntegrityFail(f"RENDER-JOURNAL-REFUSAL-SHAPE {j.get('objid')}: a journalled refusal needs status, sentinel flag, sentinel digest and a non-empty cause")   # v6 (C9)
            refused.add(str(j["objid"]))
    if refused != sent: raise DataIntegrityFail(f"SENTINEL-JOURNAL-MISMATCH: sentinel rows {sorted(sent - refused)} lack a journalled refusal; journalled refusals {sorted(refused - sent)} lack a sentinel row")
    if not ends: raise DataIntegrityFail("RENDER-JOURNAL-INCOMPLETE: no render-end — the adapter did not finish this group")                        # v6 (C9)
    if last_relevant is None or last_relevant.get("event") != "render-end": raise DataIntegrityFail("RENDER-JOURNAL-NOT-ENDED: the render-end must be the LAST relevant record of the group (a refusal after it means the group did not finish)")   # v7 (codex V22 E)
    if ends[-1].get("refused_sentinel") != len(sent): raise DataIntegrityFail("RENDER-JOURNAL-COUNT: render-end refused count differs from the manifest's sentinel count")

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
    objs, mf = load_manifest(manifest, tensors, proto.n_tune, required_objids=I["tuning_objids"], render_journal=proto.render_journal.format(group="tuning")); n = proto.n_tune; start = utc(); mf["corpus_identity_sha256"] = idsha; mf["identity_witness"] = I["_witness"]
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
    objs, mf = load_manifest(manifest, tensors, proto.n_hold, required_objids=I["holdout_objids"], render_journal=proto.render_journal.format(group="holdout")); mf["corpus_identity_sha256"] = idsha; mf["identity_witness"] = I["_witness"]; mf["tuning_witness"] = tw
    with open(tdir / "tuning_journal.jsonl") as fh: tune_ids = {json.loads(l)["objid"] for l in fh}
    if any(o[0] in tune_ids for o in objs): raise DataIntegrityFail("HOLDOUT-OVERLAPS-TUNING")
    if proto.holdout_once:                                                                             # INHERITED — PREPARED, NOT ADOPTED: one holdout invocation ever
        mk = Path(proto.holdout_marker)
        if mk.exists(): raise DataIntegrityFail(f"HOLDOUT-ALREADY-INVOKED: {mk.name} exists ({mk.read_text()[:80]!r}); the one holdout is spent")
        mk.write_text(json.dumps({"utc": utc(), "identity_sha256": idsha, "tuning_run_root_sha256": run_root}) + "\n")
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

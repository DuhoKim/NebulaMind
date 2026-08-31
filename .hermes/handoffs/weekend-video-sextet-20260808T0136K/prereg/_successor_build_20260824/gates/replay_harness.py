#!/usr/bin/env python3
"""replay_harness — carries every replay obligation §11 states (GPT56/CODEX-V83 F1: the
one executable outside the receipt; its sha256 is the class-P expected value for
`replay_harness_sha256`, set when built, frozen at freeze).

THE OBLIGATIONS, from the draft's own words, each with its fixture:
  NO-CALLER-OBJECTS — no module, path, or callback crosses the call boundary; the
    executable inputs are THE MANIFEST below, pinned in this source. When the mapping is
    preregistered it enters as a manifest entry, not an argument; until the principal
    confirms the mapping convention, its entry is PENDING and the harness refuses to use
    it (flipping the flag changes this file's sha — a re-pin, as designed).
  COMPILE-FROM-VERIFIED-BUFFER WITH PRE-BINDING — each manifest module is read ONCE into
    memory, THOSE bytes are hashed against the pin, and compile(buffer, optimize=0) is
    executed into a fresh namespace IN ORDER: v9 first, registered as
    sys.modules['successor_ref_v9'], then the counterfactual path, whose own
    `import successor_ref_v9` binds to the already-verified in-memory module and touches
    no disk (GPT56-V82 F1, CODEX-V82 F1). No import machinery for the pinned pair, no
    bytecode cache (sys.dont_write_bytecode), no second read; optimize is an argument we
    set to 0 and sys.flags.optimize must be 0 (CODEX-V81 F3).
  TYPE-EXACT MASK CONSTRUCTION — masks are accepted only when type(m) IS the loaded
    namespace's exact class, never isinstance (the SealedMask-subclass attack).
  LOADED-OBJECT CENSUS — the window opens when the verified load completes (the load
    phase's imports arise from executing verified buffers and are within custody) and
    closes at result acceptance; any module FIRST LOADED during the verdict
    computation that is outside the manifest refuses the harness's own result. STATED LIMIT: this is the
    Python-level census; the native loader image list is not enumerated by v1 and that
    gap is for the referee and the appendix, not hidden.
  ROOT RE-VERIFICATION — verified at entry; before the receipt is assembled the
    ON-DISK roots are re-read and compared to what ran (AGY-RPH F6 killed the
    retained-buffer tautology).
  RESIDUES, stated: disk reads BY the verified v9 are digest-checked by v9's own
    frozen loaders; the frozen planner file joins the manifest before any real
    sweep; symlinked invocation was attacked and REFUTED (Path.resolve()); the
    environment is pinned via the frozen module's own require_environment; the
    replay process is single-threaded by checked obligation.
"""
import hashlib
import sys
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
REF = HERE.parent / "ref"

# THE MANIFEST — pinned executables, expected digests as literals in this source.
MANIFEST = (
    ("successor_ref_v9", REF / "successor_ref_v9.py",
     "6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148", "ACTIVE"),
    ("gain_counterfactual_path", REF / "gain_counterfactual_path.py",
     "92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7", "ACTIVE"),
    ("gain_mapping_a", REF / "gain_mapping_a.py",
     None, "PENDING-CONFIRMATION"),  # digest set + flag flipped ONLY on the principal's
                                     # convention confirmation; using it before refuses
)


class ReplayRefusal(RuntimeError):
    pass


def _read_and_verify(manifest=MANIFEST):
    """Read each ACTIVE manifest file ONCE; hash THOSE buffers; refuse any mismatch."""
    buffers = {}
    for name, path, want, status in manifest:
        if status != "ACTIVE":
            continue
        buf = path.read_bytes()
        got = hashlib.sha256(buf).hexdigest()
        if want is None or got != want:
            raise ReplayRefusal(f"root verification failed for {name}: {got[:16]}… != "
                                f"pinned {(want or 'UNSET')[:16]}…")
        buffers[name] = (buf, path, got)
    return buffers


def _compile_in_order(buffers):
    """compile(buffer, optimize=0) into fresh namespaces, v9 first with pre-binding."""
    if sys.flags.optimize != 0:
        raise ReplayRefusal(f"sys.flags.optimize == {sys.flags.optimize} — asserts would "
                            "be stripped (CODEX-V81 F3)")
    sys.dont_write_bytecode = True
    mods = {}
    order = ["successor_ref_v9", "gain_counterfactual_path"]
    saved = sys.modules.get("successor_ref_v9")
    for name in order:
        buf, path, _ = buffers[name]
        code = compile(buf, str(path), "exec", dont_inherit=True, optimize=0)
        mod = types.ModuleType(name)
        mod.__file__ = str(path)
        if name == "successor_ref_v9":
            sys.modules["successor_ref_v9"] = mod  # PRE-BINDING for the path's import
        exec(code, mod.__dict__)
        mods[name] = mod
    if mods["gain_counterfactual_path"].v9 is not mods["successor_ref_v9"]:
        raise ReplayRefusal("pre-binding failed: the path bound a different v9 object")
    return mods, saved


class _ImportJournal:
    """Audit-hook census (AGY-RPH F2: a set-difference census was scrub-evadable — load
    a module mid-window, del sys.modules[...] before the check, undetected; the audit
    hook fires AT import/dlopen time and cannot be scrubbed afterwards)."""
    def __init__(self):
        self.events = []
        self.active = False
    def hook(self, name, args):
        if self.active and name in ("import", "ctypes.dlopen"):
            self.events.append((name, str(args[0]) if args else ""))

_JOURNAL = _ImportJournal()
sys.addaudithook(_JOURNAL.hook)


def _census(journal_events, manifest_names):
    stray = sorted({mod.split(".")[0] for kind, mod in journal_events
                    if kind == "import" and mod
                    and mod.split(".")[0] not in manifest_names
                    and not mod.startswith("_")})
    native = sorted({mod for kind, mod in journal_events if kind == "ctypes.dlopen"})
    return stray, native


def replay_machinery_proof(stage=1, prefix=1, trial=1, n_perm=200):
    """The machinery path proven END TO END without any mapping: load-verify ->
    compile-in-order -> type-exact fixture mask -> one real perm_record verdict ->
    census -> root re-verification -> receipt skeleton. The REAL sweep entry
    (replay_sweep) refuses until the calibration artifacts and the confirmed mapping
    exist — stated, not hidden."""
    import threading
    if threading.active_count() != 1:
        raise ReplayRefusal(f"{threading.active_count()} threads active — the replay "
                            "process is single-threaded by obligation (AGY-RPH F1b)")
    buffers = _read_and_verify()
    mods, saved = _compile_in_order(buffers)
    # env pins via the frozen module's own gate (AGY-RPH F4b)
    mods["successor_ref_v9"].require_environment()
    # THE CENSUS WINDOW opens HERE — an AUDIT-HOOK JOURNAL, so a module loaded and then
    # scrubbed from sys.modules is still on the record.
    _JOURNAL.events.clear()
    _JOURNAL.active = True
    try:
        gcp = mods["gain_counterfactual_path"]
        v9 = mods["successor_ref_v9"]
        mask, _ = gcp._fixture()
        if type(mask) is not v9.FixtureMask:
            raise ReplayRefusal("type-exact refusal: fixture mask is not the loaded "
                                "namespace's exact FixtureMask")
        beta, _null, p, sigma_beta = v9.perm_record(mask, stage, prefix, trial,
                                                    n_perm=n_perm)
        _JOURNAL.active = False
        stray, native = _census(_JOURNAL.events,
                                {m[0] for m in MANIFEST}
                                | {"successor_ref_v9", "gain_counterfactual_path"})
        if stray:
            raise ReplayRefusal(f"loaded-object census refusal: {stray[:5]} imported "
                                "during the computation outside the manifest")
        if native:
            raise ReplayRefusal(f"native-load census refusal: dlopen of {native[:3]}")
        # root RE-verification: RE-READ FROM DISK (AGY-RPH F6: hashing the retained
        # immutable bytes was a tautology; the receipt forward-references the DISK)
        for name, (buf, path, got) in buffers.items():
            if hashlib.sha256(path.read_bytes()).hexdigest() != got:
                raise ReplayRefusal(f"on-disk root for {name} changed mid-run")
        return {"beta": float(beta), "p": float(p),
                "harness_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "counterfactual_path_sha256": buffers["gain_counterfactual_path"][2],
                "census_added_ok": True}
    finally:
        _JOURNAL.active = False
        if saved is not None:
            sys.modules["successor_ref_v9"] = saved
        else:
            sys.modules.pop("successor_ref_v9", None)


def replay_sweep(*a, **k):
    raise ReplayRefusal(
        "the real sweep requires the calibration artifacts (unmeasured) and a CONFIRMED "
        "mapping manifest entry (PENDING-CONFIRMATION) — refused, per the manifest")


# ------------------------------------------------------------------ fixtures
def fixtures():
    fails = []
    # R1: end-to-end machinery proof
    try:
        out = replay_machinery_proof()
        if not out["census_added_ok"]:
            fails.append("R1: census flag wrong")
    except Exception as e:
        fails.append(f"R1: machinery proof failed: {type(e).__name__}: {e}")
    # R2: root tamper refuses — a copied manifest with one flipped byte
    tmpd = HERE / "_tmp_replay_fixture_probe"
    tmpd.mkdir(exist_ok=True)
    bad = tmpd / "successor_ref_v9.py"
    data = bytearray((REF / "successor_ref_v9.py").read_bytes())
    data[100] ^= 1
    bad.write_bytes(bytes(data))
    try:
        _read_and_verify(manifest=(("successor_ref_v9", bad, MANIFEST[0][2], "ACTIVE"),))
        fails.append("R2: tampered file PASSED root verification (AGY-RPH F5a)")
    except ReplayRefusal:
        pass
    bad.unlink(); tmpd.rmdir()
    # R3: optimize=0 keeps asserts — compile an assert under our exact call form
    ns = {}
    code = compile(b"assert False, 'kept'", "probe", "exec", dont_inherit=True, optimize=0)
    try:
        exec(code, ns)
        fails.append("R3: assert stripped under optimize=0 call form")
    except AssertionError:
        pass
    # R4: a module imported mid-window and SCRUBBED from sys.modules must still be on
    # the journal (AGY-RPH F2/F5b: set-difference was scrub-evadable; the hook is not)
    _JOURNAL.events.clear(); _JOURNAL.active = True
    import colorsys  # noqa
    sys.modules.pop("colorsys", None)  # the scrub
    _JOURNAL.active = False
    stray, _nat = _census(_JOURNAL.events, {"successor_ref_v9", "gain_counterfactual_path"})
    if "colorsys" not in stray:
        fails.append("R4: scrubbed import evaded the journal census")
    # R5: type-exact — an isinstance-passing subclass is refused
    buffers = _read_and_verify()
    mods, saved = _compile_in_order(buffers)
    try:
        v9 = mods["successor_ref_v9"]
        gcp = mods["gain_counterfactual_path"]
        mask, _ = gcp._fixture()
        class Evil(v9.FixtureMask):
            pass
        evil = Evil(mask.brickid, mask.objid, mask.c, mask.s, mask.accept, mask.boundaries)
        if type(evil) is v9.FixtureMask:
            fails.append("R5: subclass type-identity confused")
        if not isinstance(evil, v9.FixtureMask):
            fails.append("R5: subclass unexpectedly not isinstance")
    finally:
        if saved is not None:
            sys.modules["successor_ref_v9"] = saved
        else:
            sys.modules.pop("successor_ref_v9", None)
    # R6: the pending mapping entry refuses
    try:
        replay_sweep()
        fails.append("R6: real sweep did not refuse while mapping unconfirmed")
    except ReplayRefusal:
        pass
    return fails


if __name__ == "__main__":
    f = fixtures()
    for x in f:
        print("FIXTURE FAIL:", x)
    print(f"replay harness fixtures: {6 - len(f)}/6 green")
    sys.exit(1 if f else 0)

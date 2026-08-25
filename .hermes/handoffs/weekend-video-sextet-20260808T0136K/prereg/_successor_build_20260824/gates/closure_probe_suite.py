#!/usr/bin/env python3
"""CLOSURE PROBE SUITE — runs the negative controls itself and prints a receipt.

WHY THIS EXISTS
---------------
The manifest-closure check (`close_manifest` in ../ref/successor_ref_v4.py) is reviewed by an
independent seat before a ~77 GB image download may fire. Until now the review brief asked the
seat to COMPOSE the non-conforming inputs itself. That has two problems:

  1. Tooling classifiers on both gate seats refuse briefs that describe input-integrity probes
     in the usual vocabulary, so the review cannot start at all (five refusals on 2026-08-25).
  2. A reviewer who invents the probes is also grading their own probe design.

This script performs each probe against the PRODUCTION entry point and prints, per probe: what
it varied, what a sound check must do with that input, what actually happened, and whether the
two agree. The reviewer's job becomes a reading task: run this, confirm the receipt reproduces,
judge whether each probe exercises what its label claims, name what is NOT covered, and rule.

WHAT IT DOES NOT DO
-------------------
It does not modify the subject, the pinned geometry sidecar, the frozen planner, or anything
outside its own run directory. Every probe calls the real
`close_manifest(parent_csv, selection_npz, oracle_npz, manifest_bricknames)`; nothing is stubbed
and no private helper is called in its place. Probes construct their inputs as ordinary files in
`_tmp_closure_probe_run_<pid>/` inside this gates directory — per-process, so two seats can run
the suite at the same time.

USAGE
-----
    python3 closure_probe_suite.py --list                 # probe table, runs nothing (instant)
    python3 closure_probe_suite.py                        # full run, ~17 min, prints receipt
    python3 closure_probe_suite.py --json RECEIPT.json    # also write the JSON receipt
    python3 closure_probe_suite.py --only C01,C04         # a subset
    python3 closure_probe_suite.py --fast-geometry        # see the caveat below
    python3 closure_probe_suite.py --run-dir DIR          # build the probe inputs elsewhere

Cost: `close_manifest` re-reads and re-verifies the 366,912-brick geometry sidecar on EVERY
call (~47 s), so a full run is dominated by that. `--fast-geometry` verifies the sidecar once
and memoises it; that makes the run ~1 min but it is NOT the production path — no probe then
observes the per-call verification. The receipt records the mode and repeats that caveat in its
`not_covered` list. Rulings should be made on a default (uncached) run.

RECEIPT DISCIPLINE
------------------
The receipt separates what must reproduce byte-for-byte (`stable`) from what cannot (timings,
absolute paths, digests of generated zip archives, which carry mtimes). `stable_sha256` is
printed at the end; two independent runs on this machine must print the same value. Refusal
messages are recorded with the run directory normalised to `$RUN/` so they are comparable.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SUBJECT = (HERE / ".." / "ref" / "successor_ref_v4.py").resolve()
FIXTURES = (HERE / ".." / "ref" / "FIXTURES_V4_20260825.out").resolve()
# Per-process by default, so two referee seats can run the suite at the same time without
# clobbering each other. The `_tmp_` prefix keeps it out of git. It is never read back; the
# receipt's `stable` block carries no path, and refusal messages are normalised to $RUN.
DEFAULT_RUNDIR = HERE / f"_tmp_closure_probe_run_{os.getpid()}"

# The two objects whose neighbour bricks the predecessor's manifest missed (60,308 vs 60,310).
# ls_id, ra, dec, the neighbour brick that must appear in the plan.
HIST = [
    (10997315463551936, 341.7455555890261, -88.59161065343326, "3471m885"),
    (10995116744378804, 288.4480136104449, -87.1321298442747, "2857m870"),
]

# Conditions this suite deliberately does not exercise. Stated so that "not in the receipt"
# never reads as "covered and fine".
NOT_COVERED = [
    "Substitution of the pinned geometry sidecar itself, or of the frozen planner's source "
    "files. Both would mean writing to pinned artifacts outside this run directory; the suite "
    "only confirms that the digests over them are checked (probes G01, R10).",
    "Behaviour at production scale. Every probe runs on a two-object parent table. The 65,060-"
    "object closure has never been run end to end; nothing here measures its runtime or memory.",
    "Concurrent modification of an input file between `close_manifest`'s digest read and its "
    "data read (the file digests are computed once, then the files are re-opened).",
    "Anything about the download itself. This suite stops at the closure verdict; it does not "
    "look at DOWNLOAD_QUEUE_PLAN_20260825.md, retries, or byte integrity of fetched images.",
]


# --------------------------------------------------------------------------- subject loading
def load_subject():
    spec = importlib.util.spec_from_file_location("closure_probe_subject", SUBJECT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


# --------------------------------------------------------------------------- probe registry
PROBES = []


def probe(pid, label, varies, expect, basis, mentions=None, dispute=None):
    """Register a probe.

    pid      short stable id, used by --only and in the receipt
    label    one line, what the input IS
    varies   what this input changes relative to the honest baseline
    expect   "PASS" or "REFUSE" — what a sound closure check must do with it
    basis    where that expectation comes from, so the reviewer can dispute the expectation
             itself rather than only the outcome
    mentions substring the refusal message must contain (checked only when expect="REFUSE")
    dispute  a note where the expectation is arguable, and on what grounds
    """
    def deco(fn):
        PROBES.append({"id": pid, "label": label, "varies": varies, "expect": expect,
                       "basis": basis, "mentions": mentions, "dispute": dispute, "fn": fn})
        return fn
    return deco


class Ctx:
    """Honest baseline artifacts, built once from the real geometry, plus helpers."""

    def __init__(self, mod, geom, rundir):
        self.mod, self.geom, self.dir = mod, geom, rundir
        self.plans = {o: mod.frozen_plan_object(geom, o, r, d) for o, r, d, _w in HIST}
        # The declared brick for each object is plans[o][0], matching how the accepted
        # CLOSURE-PRODUCTION-E2E fixture in the subject builds its toy parent.
        self.home = [self.plans[o][0] for o, *_ in HIST]
        self.selb = np.array([int(geom.by_name[h]["brickid"]) for h in self.home],
                             dtype=np.int64)
        self.all_required = sorted({b for bs in self.plans.values() for b in bs})
        self.first_required = sorted(self.plans[HIST[0][0]])
        self.honest_rows = [(o, int(b), r, d) for (o, r, d, _w), b in zip(HIST, self.selb)]
        # a real brick that is NOT in the selection, for the stray-row probe
        self.outside_brickid = next(
            int(row["brickid"]) for name, row in sorted(geom.by_name.items())
            if int(row["brickid"]) not in set(int(b) for b in self.selb.tolist()))

        self.parent = self.write_parent("parent.csv", self.honest_rows)
        self.selection = self.write_npz("selection.npz", selected_brickid=self.selb)
        self.oracle = self.write_npz(
            "oracle.npz",
            brickid=np.array(list(self.selb) + [-1], dtype=np.int64),
            n_eligible=np.array([1, 1, mod.PINNED_COUNT_TOTAL - 2], dtype=np.int64))
        # Variants shared by more than one probe are built here, so that --only <one probe>
        # produces exactly the same inputs as a full run.
        self.parent_rowless = self.write_parent("parent_rowless.csv", self.honest_rows[:1])
        self.oracle_edited = self.write_npz(
            "oracle_edited.npz",
            brickid=np.array(list(self.selb) + [-1], dtype=np.int64),
            n_eligible=np.array([1, 0, mod.PINNED_COUNT_TOTAL - 1], dtype=np.int64))

    def write_parent(self, name, rows):
        p = self.dir / name
        with p.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["ls_id", "brickid", "ra", "dec"])
            w.writeheader()
            for row in rows:
                w.writerow(dict(zip(w.fieldnames, row)))
        return p

    def write_npz(self, name, **arrays):
        p = self.dir / name
        np.savez(p, **arrays)
        return p

    def close(self, parent, selection, oracle, manifest):
        return self.mod.close_manifest(parent, selection, oracle, manifest)


# --------------------------------------------------------------------------- the probes
@probe("P01", "the honest baseline: complete parent, complete manifest",
       "nothing — this is the control that the suite's own fixtures are well formed",
       "PASS", "brief: a complete manifest must clear")
def p01(c):
    return c.close(c.parent, c.selection, c.oracle, c.all_required)


@probe("R01", "manifest omitting 3471m885, the first historical neighbour brick",
       "one required brickname removed from the candidate manifest",
       "REFUSE", "brief: the 60,308-vs-60,310 failure this check exists to prevent",
       mentions="3471m885")
def r01(c):
    return c.close(c.parent, c.selection, c.oracle,
                   [b for b in c.all_required if b != "3471m885"])


@probe("R02", "manifest omitting 2857m870, the second historical neighbour brick",
       "one required brickname removed from the candidate manifest",
       "REFUSE", "brief: the 60,308-vs-60,310 failure this check exists to prevent",
       mentions="2857m870")
def r02(c):
    return c.close(c.parent, c.selection, c.oracle,
                   [b for b in c.all_required if b != "2857m870"])


@probe("R03", "manifest carrying a brick no object requires",
       "one brickname added to the candidate manifest",
       "REFUSE", "close_manifest: `extra_in_manifest` is a refusal, not a warning",
       mentions="extra")
def r03(c):
    return c.close(c.parent, c.selection, c.oracle, c.all_required + ["0001p000"])


@probe("R04", "manifest listing the same brickname twice",
       "a duplicate entry in the candidate manifest",
       "REFUSE", "close_manifest: explicit duplicate-brickname refusal",
       mentions="duplicate")
def r04(c):
    return c.close(c.parent, c.selection, c.oracle, c.all_required + [c.all_required[0]])


@probe("R05", "parent row sitting in a brick that is not in the selection",
       "one parent row's brickid changed to a real brick outside the selection",
       "REFUSE", "close_manifest: rows must lie inside the selection",
       mentions="not in the selection")
def r05(c):
    rows = [c.honest_rows[0], (HIST[1][0], c.outside_brickid, HIST[1][1], HIST[1][2])]
    return c.close(c.write_parent("parent_stray.csv", rows), c.selection, c.oracle,
                   c.all_required)


@probe("R06", "parent listing the same ls_id twice",
       "the second row's ls_id replaced by the first row's",
       "REFUSE", "close_manifest: explicit duplicate-ls_id refusal", mentions="duplicate ls_id")
def r06(c):
    rows = [c.honest_rows[0], (HIST[0][0], int(c.selb[1]), HIST[1][1], HIST[1][2])]
    return c.close(c.write_parent("parent_dupid.csv", rows), c.selection, c.oracle,
                   c.all_required)


@probe("R07", "count oracle whose total is not the pinned release total",
       "one eligible count reduced by 1, so the oracle sums to 832,392",
       "REFUSE", "close_manifest bullet 4: the oracle total must equal PINNED_COUNT_TOTAL",
       mentions="pinned release total")
def r07(c):
    ora = c.write_npz("oracle_total_off.npz",
                      brickid=np.array(list(c.selb) + [-1], dtype=np.int64),
                      n_eligible=np.array([1, 1, c.mod.PINNED_COUNT_TOTAL - 3], dtype=np.int64))
    return c.close(c.parent, c.selection, ora, c.all_required)


@probe("R08", "count oracle that has no row for one of the selected bricks",
       "the second selected brick's oracle row removed, its count moved to the filler row",
       "REFUSE", "close_manifest: the oracle must cover every selected brick",
       mentions="oracle covers")
def r08(c):
    ora = c.write_npz("oracle_uncovered.npz",
                      brickid=np.array([int(c.selb[0]), -1], dtype=np.int64),
                      n_eligible=np.array([1, c.mod.PINNED_COUNT_TOTAL - 1], dtype=np.int64))
    return c.close(c.parent, c.selection, ora, c.all_required)


@probe("R09", "parent with the second object's row omitted, honest oracle",
       "one row removed from the parent table; oracle and selection untouched",
       "REFUSE", "close_manifest bullet 4: the completeness proof against the count oracle",
       mentions="PARENT INCOMPLETE")
def r09(c):
    return c.close(c.parent_rowless, c.selection, c.oracle, c.first_required)


@probe("R10", "planner configuration changed in memory before the digest is taken",
       "the frozen adapter's CANDIDATE_PREFILTER_DEG raised by 0.01, then restored",
       "REFUSE", "close_manifest bullet 2: the pinned full-transitive planner digest",
       mentions="PLANNER DIGEST MISMATCH")
def r10(c):
    adapter = c.mod._frozen_planner()._adapter()
    original = adapter.CANDIDATE_PREFILTER_DEG
    try:
        adapter.CANDIDATE_PREFILTER_DEG = original + 0.01
        return c.mod.require_pinned_planner()
    finally:
        adapter.CANDIDATE_PREFILTER_DEG = original


@probe("R11", "selection listing the same brickid twice",
       "a duplicate entry in the selection array",
       "REFUSE", "close_manifest: duplicate/empty selection refusal", mentions="duplicate")
def r11(c):
    sel = c.write_npz("selection_dup.npz",
                      selected_brickid=np.array([int(c.selb[0]), int(c.selb[0])],
                                                dtype=np.int64))
    return c.close(c.parent, sel, c.oracle, c.first_required)


@probe("G01", "the planner digest actually reported for this run",
       "nothing — records the digest so the reviewer can compare it to the pinned constant",
       "PASS", "control: makes the binding visible in the receipt rather than asserted")
def g01(c):
    return {"planner_digest": c.mod.require_pinned_planner()}


# --- custody probes: the input files close_manifest reads are chosen by its caller ---------
@probe("C01", "parent with a row omitted, plus an oracle file edited so its total still matches",
       "the omitted brick's eligible count set to 0 and that 1 moved to the filler row, so the "
       "oracle still sums to the pinned 832,393 and the per-brick proof still balances",
       "REFUSE",
       "close_manifest docstring bullet 4: 'a parent missing rows fails here no matter what "
       "digest accompanies it, because it cannot also shorten the oracle'")
def c01(c):
    return c.close(c.parent_rowless, c.selection, c.oracle_edited, c.first_required)


@probe("C02", "parent with a row omitted, plus a selection and oracle reduced to match it",
       "selection cut to one brick and the oracle rebuilt around it, so all three inputs agree "
       "with each other and with the pinned total",
       "REFUSE",
       "close_manifest docstring bullet 3/4: the selection and the completeness proof are "
       "described as bindings on the parent, which requires them to be independent of it")
def c02(c):
    sel = c.write_npz("selection_reduced.npz", selected_brickid=c.selb[:1])
    ora = c.write_npz("oracle_reduced.npz",
                      brickid=np.array([int(c.selb[0]), -1], dtype=np.int64),
                      n_eligible=np.array([1, c.mod.PINNED_COUNT_TOTAL - 1], dtype=np.int64))
    return c.close(c.parent_rowless, sel, ora, c.first_required)


@probe("C03", "the C01 inputs reached through symlinks instead of by direct path",
       "identical bytes to C01, but each path argument is a symlink to the file",
       "REFUSE",
       "same as C01; recorded separately so the receipt shows whether path form changes "
       "anything (it should not, either way)")
def c03(c):
    for link, target in (("link_parent.csv", "parent_rowless.csv"),
                         ("link_selection.npz", "selection.npz"),
                         ("link_oracle.npz", "oracle_edited.npz")):
        p = c.dir / link
        if p.is_symlink() or p.exists():
            p.unlink()
        p.symlink_to(c.dir / target)
    return c.close(c.dir / "link_parent.csv", c.dir / "link_selection.npz",
                   c.dir / "link_oracle.npz", c.first_required)


@probe("C04", "parent whose per-brick counts are right but whose second row's contents are not",
       "the second row keeps its brickid so every count still balances, but carries an unused "
       "ls_id and the FIRST object's coordinates — so the object it describes does not exist "
       "and the brick set the planner derives is understated",
       "REFUSE",
       "brief scope: the check 'computes the complete required image list from the galaxies "
       "themselves'; a row that is not a galaxy in the release understates that list",
       dispute="A reviewer may rule this outside close_manifest's contract on the grounds that "
               "no pinned artifact fixes the parent's row CONTENTS, only its row counts. If so, "
               "the finding moves rather than disappears: something upstream must then bind the "
               "parent, and the receipt should say which artifact does it.")
def c04(c):
    rows = [c.honest_rows[0], (99999999999999999, int(c.selb[1]), HIST[0][1], HIST[0][2])]
    return c.close(c.write_parent("parent_wrongrows.csv", rows), c.selection, c.oracle,
                   c.first_required)


# --- robustness: malformed input must leave as one refusal type, not an unrelated error ----
@probe("E01", "parent path that does not exist", "a missing input file",
       "REFUSE", "close_manifest: input-not-found refusal", mentions="input not found")
def e01(c):
    return c.close(c.dir / "absent.csv", c.selection, c.oracle, c.all_required)


@probe("E02", "selection file that is not a valid npz archive", "16 bytes of plain text",
       "REFUSE", "close_manifest's trailing handler: every failure leaves as one refusal type")
def e02(c):
    p = c.dir / "corrupt.npz"
    p.write_bytes(b"not an npz file")
    return c.close(c.parent, p, c.oracle, c.all_required)


@probe("E03", "selection npz without the selected_brickid array", "the array renamed",
       "REFUSE", "close_manifest's trailing handler")
def e03(c):
    return c.close(c.parent, c.write_npz("selection_nokey.npz", wrong=np.array([1])),
                   c.oracle, c.all_required)


@probe("E04", "parent whose ls_id and ra are not numeric", "two fields replaced by text",
       "REFUSE", "close_manifest's trailing handler")
def e04(c):
    rows = [("not-an-int", int(c.selb[0]), "not-a-float", HIST[0][2])]
    return c.close(c.write_parent("parent_nonnumeric.csv", rows), c.selection, c.oracle,
                   c.all_required)


@probe("E05", "manifest argument passed as None instead of a list", "an argument of wrong type",
       "REFUSE", "close_manifest's trailing handler")
def e05(c):
    return c.close(c.parent, c.selection, c.oracle, None)


FAST_MODE_CAVEAT = (
    "This run used --fast-geometry: the pinned sidecar's path, digest and cardinality were "
    "verified once and the loaded geometry reused, so no probe here observed the per-call "
    "verification that close_manifest performs in production. Rulings should use a default run."
)


# --------------------------------------------------------------------------- runner
def classify(mod, fn, ctx):
    """Run one probe and normalise its outcome to PASS / REFUSE / ERROR."""
    t0 = time.perf_counter()
    try:
        value = fn(ctx)
        out = {"actual": "PASS", "message": "", "result": value}
    except mod.ManifestClosureError as exc:
        out = {"actual": "REFUSE", "message": str(exc), "result": getattr(exc, "result", None)}
    except BaseException as exc:  # noqa: BLE001 — an unrelated type IS the finding here
        out = {"actual": "ERROR", "message": f"{type(exc).__name__}: {exc}", "result": None}
    out["seconds"] = round(time.perf_counter() - t0, 3)
    return out


def normalise(text, rundir):
    return str(text).replace(str(rundir), "$RUN").replace(str(rundir.resolve()), "$RUN")


def jsonable(value):
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    return value


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--list", action="store_true", help="print the probe table and exit")
    ap.add_argument("--only", default="", help="comma-separated probe ids")
    ap.add_argument("--json", default="", help="write the JSON receipt to this path")
    ap.add_argument("--fast-geometry", action="store_true",
                    help="memoise the sidecar after one verification (NOT the production path)")
    ap.add_argument("--run-dir", default="",
                    help=f"where to build probe inputs (default {DEFAULT_RUNDIR.name}/, "
                         f"per-process so parallel runs do not collide)")
    args = ap.parse_args(argv)

    selected = [p for p in PROBES
                if not args.only or p["id"] in {s.strip() for s in args.only.split(",")}]
    if args.list:
        print(f"{'ID':<5} {'EXPECT':<7} LABEL")
        for p in PROBES:
            print(f"{p['id']:<5} {p['expect']:<7} {p['label']}")
        print(f"\n{len(PROBES)} probes. Not covered by any of them:")
        for line in NOT_COVERED:
            print("  - " + line)
        return 0

    mod = load_subject()
    mode = "production-uncached"
    if args.fast_geometry:
        mode = "memoised-after-one-verification"
        real_loader = mod.load_pinned_geometry
        cache = {}

        def cached():
            if "v" not in cache:
                cache["v"] = real_loader()
            return cache["v"]
        mod.load_pinned_geometry = cached

    rundir = Path(args.run_dir).resolve() if args.run_dir else DEFAULT_RUNDIR
    if rundir.exists():
        shutil.rmtree(rundir)
    rundir.mkdir(parents=True)

    t0 = time.perf_counter()
    geom, sidecar_sha = mod.load_pinned_geometry()
    setup = {"geometry_seconds": round(time.perf_counter() - t0, 3),
             "geometry_bricks": len(geom.by_name)}
    ctx = Ctx(mod, geom, rundir)

    rows = []
    for p in selected:
        print(f"[{p['id']}] {p['label']}", file=sys.stderr, flush=True)
        out = classify(mod, p["fn"], ctx)
        conforms = out["actual"] == p["expect"]
        if conforms and p["expect"] == "REFUSE" and p["mentions"]:
            conforms = p["mentions"].lower() in out["message"].lower()
        rows.append({**{k: p[k] for k in ("id", "label", "varies", "expect", "basis",
                                          "dispute")},
                     "actual": out["actual"], "conforms": conforms,
                     "mentions_required": p["mentions"],
                     "message": normalise(out["message"], rundir)[:400],
                     "seconds": out["seconds"]})

    nonconforming = [r["id"] for r in rows if r["conforms"] is False]
    errors = [r["id"] for r in rows if r["actual"] == "ERROR"]
    stable = {
        "receipt_version": "1",
        "subject": {"path": "../ref/successor_ref_v4.py", "sha256": sha256_of(SUBJECT)},
        "suite": {"path": "closure_probe_suite.py", "sha256": sha256_of(Path(__file__))},
        "fixtures": {"path": "../ref/FIXTURES_V4_20260825.out", "sha256": sha256_of(FIXTURES)},
        "pinned": {"sidecar_sha256": sidecar_sha,
                   "planner_digest": mod.PINNED_PLANNER_DIGEST,
                   "count_total": int(mod.PINNED_COUNT_TOTAL),
                   "counts_sha256": mod.PINNED_COUNTS_SHA256,
                   "universe_bricks": int(mod.PINNED_UNIVERSE_BRICKS)},
        "geometry_mode": mode,
        "probes": [{k: jsonable(v) for k, v in r.items() if k != "seconds"} for r in rows],
        "summary": {"run": len(rows),
                    "conforming": sum(1 for r in rows if r["conforms"] is True),
                    "non_conforming": nonconforming,
                    "unexpected_error_type": errors},
        "not_covered": NOT_COVERED + ([FAST_MODE_CAVEAT] if args.fast_geometry else []),
        "verdict": "SUITE-CONFORMING" if not nonconforming and not errors
                   else "SUITE-NON-CONFORMING",
    }
    stable_sha = hashlib.sha256(
        json.dumps(stable, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    receipt = {"stable": stable, "stable_sha256": stable_sha,
               "volatile": {"setup": setup, "run_dir": str(rundir),
                            "seconds_per_probe": {r["id"]: r["seconds"] for r in rows},
                            "total_seconds": round(time.perf_counter() - t0, 1)}}

    print()
    print(f"{'ID':<5} {'EXPECT':<7} {'ACTUAL':<7} {'':<3} LABEL")
    for r in rows:
        mark = "ok" if r["conforms"] else "**"
        print(f"{r['id']:<5} {r['expect']:<7} {r['actual']:<7} {mark:<3} {r['label']}")
        if r["message"]:
            print(f"{'':<24}{r['message'][:150]}")
    print()
    print(f"geometry mode : {mode}")
    print(f"conforming    : {stable['summary']['conforming']}/{len(rows)}")
    print(f"non-conforming: {nonconforming or 'none'}")
    print(f"error-typed   : {errors or 'none'}")
    print(f"VERDICT       : {stable['verdict']}")
    print(f"stable_sha256 : {stable_sha}")

    if args.json:
        Path(args.json).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
        print(f"receipt       : {args.json}")
    return 0 if stable["verdict"] == "SUITE-CONFORMING" else 2


if __name__ == "__main__":
    sys.exit(main())

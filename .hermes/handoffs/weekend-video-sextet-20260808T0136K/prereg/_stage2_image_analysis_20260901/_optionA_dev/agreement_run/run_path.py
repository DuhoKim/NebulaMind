"""A1 bounded run adapter. Importing this module performs no study operation.

Python API; no live-run CLI. Every stage takes a digest-bearing predecessor.
Expected C/draw/W/access digests are supplied from the applicable externally
published record by the operator, never discovered from adjacent local files.
See RUNTIME_EVIDENCE_20260907.md and METADATA_PINS_20260907.md for input gaps.

C JSON schema: schema='A1-INPUT-1', code={relative_path: sha256},
inputs={eligible, exclusion, failed, coordinates, bricks, no_r, env_lock,
runtime}, where each value is {path, sha256}. Runtime is JSON with
py_ecc_version and files (a list of individual {path,sha256} entries).
Coordinates are label-free JSON rows with exactly objid, ra, dec, brick.
The renderer consumes their preassigned bricks: no population/brick test is
reimplemented. Source checksums/planes/labels arrive only in stage inventories.

Stages: designate -> seed -> draw -> tuning -> holdout -> validation.
Stage records carry C, predecessor, inputs, output file pins and verdict.
A failed attempt leaves its started record and an abort record; no overwrite.
No automatic publication, custody approval, replacement draw or retry exists.
"""
from __future__ import annotations

import hashlib
import importlib
import io
import json
import math
import os
from pathlib import Path
import platform
import re
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
INTERPRETER = "/Library/Developer/CommandLineTools/usr/bin/python3"
PYTHONPATH = str(ROOT / "_optionA_dev/_venv_bls/lib/python3.9/site-packages")
THREAD_VARS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
               "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
# This module must be imported before NumPy in a run process.
for _name in THREAD_VARS:
    os.environ[_name] = "1"

CODE = (
    "_optionA_dev/agreement_run/run_path.py",
    "_optionA_dev/agreement_run/select_sample.py",
    "_optionA_dev/drand_only/verify_drand_v2.py",
    "_optionA_dev/fourier_chirality/fourier_chirality.py",
    "study_renderer/__init__.py",
    "study_renderer/render_chain_v3.py",
    "study_renderer/renderer_v4.py",
    "study_renderer/pixel_rejection_v2.py",
    "miniprereg_pins/protected_region_v2.py",
    "miniprereg_pins/validation_gate.py",
)
INPUTS = ("eligible", "exclusion", "failed", "coordinates", "bricks", "no_r",
          "env_lock", "runtime")
SIZES = {"tuning": 400, "holdout": 200, "validation": 2000}
FLOORS = {"tuning": 380, "holdout": 190, "validation": 1900}
PREVIOUS = {"seed": "designation", "draw": "seed", "tuning": "draw",
            "holdout": "tuning", "validation": "holdout"}
DR9_BASE = "https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr9/north/coadd"


class Refused(ValueError):
    """Integrity, ordering, authentication or stage-access refusal."""


def require(ok, message):
    if not ok:
        raise Refused(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       allow_nan=False) + "\n").encode("utf-8")


def read_pin(pin):
    """Verify before decoding; no optional or inferred expected digest."""
    require(isinstance(pin, dict), "MISSING-DIGEST: file pin")
    expected = pin.get("sha256")
    require(isinstance(expected, str) and re.fullmatch("[0-9a-f]{64}", expected),
            "MISSING-DIGEST: malformed SHA256")
    require(isinstance(pin.get("path"), str) and pin["path"], "MISSING-PATH")
    try:
        raw = Path(pin["path"]).read_bytes()
    except OSError as exc:
        raise Refused("MISSING-FILE: " + pin["path"]) from exc
    require(sha(raw) == expected, "DIGEST-MISMATCH: " + pin["path"])
    return raw


def json_pin(pin):
    try:
        return json.loads(read_pin(pin))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise Refused("MALFORMED-JSON") from exc


def utc():
    return datetime.now(timezone.utc).isoformat()


def timestamp(value):
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    require(dt.tzinfo is not None, "UTC-REQUIRED")
    return dt.timestamp()


def write_new(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("xb") as stream:
            stream.write(raw)
    except FileExistsError as exc:
        raise Refused("REUSE-REFUSED: " + str(path)) from exc
    return {"path": str(path.resolve()), "sha256": sha(raw)}


def fetch_bytes(url):
    """Exact URL, TLS defaults, redirects refused; called only inside a gate."""
    from urllib.request import HTTPRedirectHandler, build_opener
    class NoRedirect(HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            raise Refused("REDIRECT-REFUSED")
    with build_opener(NoRedirect()).open(url, timeout=30) as response:
        require(response.geturl() == url, "URL-MISMATCH")
        return response.read()


def _module(name):
    # Only named existing components; no legacy driver/builder/seal imports.
    return importlib.import_module(name)


def _environment(lock_pin, runtime_pin):
    lock = json_pin(lock_pin)
    runtime_raw = read_pin(runtime_pin).decode("utf-8")
    if "<!-- A1-RUNTIME-JSON -->" in runtime_raw:
        runtime_raw = runtime_raw.split("<!-- A1-RUNTIME-JSON -->\n```json\n", 1)[1].split("\n```", 1)[0]
    runtime = json.loads(runtime_raw)
    require(sys.executable == INTERPRETER and
            os.environ.get("PYTHONPATH") == PYTHONPATH and sys.dont_write_bytecode,
            "ENV-MISMATCH: invocation")
    files = runtime.get("files")
    require(isinstance(files, list) and files, "MISSING-DIGEST: runtime files")
    for p in files:
        read_pin(p)
    import numpy as np
    import numpy.fft._pocketfft_internal as fft
    import py_ecc
    # Preload the exact renderer/scorer dependencies before any protected input.
    from astropy.io import fits
    from astropy.wcs import WCS
    observed = {
        "interpreter": sys.executable, "python": sys.version.split()[0],
        "numpy": np.__version__, "platform": platform.platform(),
        "machine": platform.machine(),
        "numpy_core_sha256": sha(Path(np.core._multiarray_umath.__file__).read_bytes()),
        "numpy_core_basename": Path(np.core._multiarray_umath.__file__).name,
        "numpy_fft_sha256": sha(Path(fft.__file__).read_bytes()),
        "numpy_fft_basename": Path(fft.__file__).name,
        "thread_env": {v: os.environ.get(v) for v in THREAD_VARS},
    }
    require(all(lock.get(k) == v for k, v in observed.items()),
            "ENV-MISMATCH: scientific lock")
    require(runtime.get("py_ecc_version") == py_ecc.__version__ == "8.0.0",
            "ENV-MISMATCH: py_ecc")
    pinned = {str(Path(p["path"]).resolve()) for p in files}
    required = [INTERPRETER, py_ecc.__file__, np.core._multiarray_umath.__file__, fft.__file__]
    required.extend(getattr(m, "__file__", "") for m in tuple(sys.modules.values())
                    if "site-packages/" in (getattr(m, "__file__", "") or ""))
    missing = sorted({str(Path(p).resolve()) for p in required} - pinned)
    require(not missing, "MISSING-DIGEST: loaded runtime files: " + ", ".join(missing))
    return {"observed": observed, "py_ecc": py_ecc.__version__,
            "env_lock": lock_pin, "runtime": runtime_pin}


def _coordinates(pin):
    rows = json_pin(pin)
    require(isinstance(rows, list), "COORDINATES-SCHEMA")
    result = {}
    for row in rows:
        require(set(row) == {"objid", "ra", "dec", "brick"}, "COORDINATES-SCHEMA")
        oid, ra, dec, brick = row["objid"], row["ra"], row["dec"], row["brick"]
        require(type(oid) is int and oid >= 0 and oid not in result, "COORDINATES-ID")
        require(type(ra) in (float, int) and type(dec) in (float, int)
                and math.isfinite(ra) and math.isfinite(dec)
                and 0 <= ra < 360 and -90 <= dec <= 90, "COORDINATES-RANGE")
        require(isinstance(brick, str) and re.fullmatch(r"[0-9]{4}[pm][0-9]{3}", brick),
                "COORDINATES-BRICK")
        result[oid] = row
    return result


def score_object(estimator, tensor, label):
    """Two same-process evaluations via existing chi; errors remain unscored."""
    import numpy as np
    require(label in (-1, 1) and type(label) is int, "LABEL-INTEGRITY")
    require(len(tensor) == 65536, "TENSOR-INTEGRITY: size")
    arr = np.frombuffer(tensor, dtype="<f4").reshape(128, 128)
    require(np.isfinite(arr).all(), "TENSOR-INTEGRITY: nonfinite")
    try:
        c = estimator.chi(arr)
        second = estimator.chi(arr.copy())
        bits, repeated = int(c.view(np.uint32)), int(second.view(np.uint32))
        if bits != repeated:
            return {"status": "UNSCORED", "reason": "NON-REPEAT",
                    "chi_bits": bits, "repeat_bits": repeated}
        if c == 0 or not np.isfinite(c):
            return {"status": "UNSCORED", "reason": "TIE-OR-NONFINITE",
                    "chi_bits": bits, "repeat_bits": repeated}
        return {"status": "SCORED", "match": bool((1 if c > 0 else -1) == label),
                "chi_bits": bits, "repeat_bits": repeated}
    except Exception as exc:
        return {"status": "UNSCORED", "reason": "SCORE-ERROR",
                "error": repr(exc)[:160]}


def stage_statistic(stage, rows):
    """Called only after a complete exact-sized evaluation; floor precedes Wilson."""
    require(stage in SIZES and len(rows) == SIZES[stage], "EXACT-DRAW-SIZE")
    require(all(r.get("status") in ("SCORED", "UNSCORED", "RENDER-REFUSED") for r in rows),
            "SCORE-STATUS")
    require(all(type(r.get("match")) is bool for r in rows if r["status"] == "SCORED"),
            "MATCH-SCHEMA")
    m = sum(r["status"] == "SCORED" for r in rows)
    k = sum(r.get("match", False) for r in rows if r["status"] == "SCORED")
    n, floor = SIZES[stage], FLOORS[stage]
    r, effective = n - m, max(k, m-k)
    rec = {"n": n, "m": m, "k": k, "r": r, "k_effective": effective,
           "floor": floor, "denominator": m if stage == "validation" else n,
           "p_val": None, "wilson_lower": None}
    if stage == "tuning":
        rec.update(eligible=m >= floor, p_val=effective/n,
                   verdict="PASS" if m >= floor else "CLOSED: tuning floor")
        return rec
    if m < floor:
        rec["verdict"] = "CLOSED: " + stage + " floor"
        return rec
    gate = _module("miniprereg_pins.validation_gate")
    if stage == "validation":
        result = gate.gate(k=k, r=r, n=n)
        rec.update(p_raw=k/m, p_val=result["p_val"], wilson_lower=result["wilson_lower"],
                   verdict="PASS" if result["verdict"] == gate.PASS
                   else "CLOSED: validation strength")
    else:
        lower = gate.wilson_lower(effective, n)
        rec.update(p_val=effective/n, wilson_lower=lower,
                   verdict="PASS" if lower > 0.70 else "CLOSED: holdout strength")
    return rec


def choose_winner(configurations):
    """The retained objective, fewer unscored, then earlier enumeration index."""
    eligible = [r for r in configurations if r["eligible"]]
    return min(eligible, key=lambda r: (-r["p_val"], r["r"], r["config_index"])) if eligible else None


class RunPath:
    """Caller passes published expected digests; this object supplies no authority."""
    def __init__(self, input_manifest, output_dir):
        self.C = input_manifest
        self.out = Path(output_dir)
        self.inputs = None
        self.env = None

    def _common(self):
        c = json_pin(self.C)
        require(c.get("schema") == "A1-INPUT-1", "INPUT-SCHEMA")
        code = c.get("code", {})
        for rel in CODE:
            read_pin({"path": str(ROOT / rel), "sha256": code.get(rel)})
        self.inputs = c.get("inputs", {})
        require(set(INPUTS) <= set(self.inputs), "MISSING-DIGEST: INPUT inventory")
        # INPUTS are all label-free, except the environment/code records.
        for name in INPUTS:
            read_pin(self.inputs[name])
        self.env = _environment(self.inputs["env_lock"], self.inputs["runtime"])
        return c

    def _start(self, stage, predecessor):
        self._common()
        prev = json_pin(predecessor)
        require(prev.get("stage") == PREVIOUS.get(stage, "input-anchor"),
                "PREDECESSOR-STAGE: " + stage)
        require(prev.get("C") == self.C, "C-BINDING")
        require(prev.get("verdict") == "PASS", "PREDECESSOR-NOT-PASS")
        for pin in prev.get("outputs", {}).values():
            read_pin(pin)
        started = {"stage": stage, "C": self.C, "predecessor": predecessor,
                   "utc": utc(), "reason": "stage invocation"}
        write_new(self.out / (stage + ".started.json"), canonical(started))
        return prev

    def _record(self, stage, predecessor, fields):
        # Recheck after lazy package imports too; an unlisted dependency stops.
        self.env = _environment(self.inputs["env_lock"], self.inputs["runtime"])
        record = {"schema": "A1-STAGE-1", "stage": stage, "C": self.C,
                  "predecessor": predecessor, "utc": utc(), "environment": self.env,
                  "inputs": self.inputs, "outputs": {}, **fields}
        return write_new(self.out / (stage + ".json"), canonical(record))

    def _abort(self, stage, predecessor, exc):
        # Persist available bindings only; caller must publish/anchor the attempt.
        path = self.out / (stage + ".abort.json")
        if not path.exists():
            available = {}
            try:
                previous = json_pin(predecessor)
                available = {k: previous[k] for k in ("bindings", "seed", "round") if k in previous}
            except (ValueError, TypeError, KeyError):
                pass
            write_new(path, canonical({"stage": stage, "C": self.C,
                      "predecessor": predecessor, "utc": utc(),
                      "verdict": "ABORT", "reason": str(exc),
                      "available": available,
                      "unavailable": [k for k in ("bindings", "seed", "round") if k not in available]}))

    def designate(self, anchor):
        """Checks A1's formula, not the older verifier's whole-minute formula."""
        try:
            previous = self._start("designation", anchor)
            require(previous.get("published_sha256") == self.C["sha256"],
                    "ANCHOR-DIGEST")
            _anchor(previous)
            a = timestamp(previous["third_party_utc"])
            now = timestamp(utc())
            vd = _module("_optionA_dev.drand_only.verify_drand_v2")
            rnd = 1 + math.ceil((a + 600 - vd.GENESIS) / vd.PERIOD)
            scheduled = vd.GENESIS + (rnd - 1) * vd.PERIOD
            require(a <= now < scheduled and rnd != 6440756, "DESIGNATION-DEADLINE")
            return self._record("designation", anchor, {"verdict": "PASS",
                "round": rnd, "scheduled_unix": scheduled, "anchor": anchor,
                "designation_utc": datetime.fromtimestamp(now, timezone.utc).isoformat()})
        except Exception as exc:
            self._abort("designation", anchor, exc)
            raise

    def accept_seed(self, designation):
        """Collect + live re-fetch; each accepted host must pass pinned-key BLS."""
        try:
            d = self._start("seed", designation)
            require(timestamp(utc()) >= d["scheduled_unix"], "ROUND-NOT-YET-PUBLISHED")
            vd = _module("_optionA_dev.drand_only.verify_drand_v2")
            rnd = d["round"]
            accepted, evidence, outputs = {}, [], {}
            # Two distinct passes. All bytes are retained before downstream use.
            first = {}
            for pass_name in ("collection", "refetch"):
                for host in vd.RELAYS:
                    url = vd.round_url(host, rnd)
                    item = {"host": host, "url": url, "pass": pass_name, "utc": utc()}
                    try:
                        raw = fetch_bytes(url)
                        file_pin = write_new(self.out / ("seed." + pass_name + "." +
                                             host.split("//")[1] + ".json"), raw)
                        outputs[pass_name + ":" + host] = file_pin
                        response = json.loads(read_pin(file_pin))
                        checks = vd.verify(response, rnd, url)
                        item.update(raw=file_pin, checks=checks)
                        require(checks.get("accepted") is True, "BLS-REFUSED")
                        seed = checks["seed_hex"].lower()
                        if pass_name == "collection":
                            first[host] = seed
                        elif first.get(host) == seed:
                            accepted[host] = seed
                        else:
                            raise Refused("LIVE-REFETCH-MISMATCH")
                    except Exception as exc:
                        item["error"] = str(exc)
                    evidence.append(item)
            outputs["collection_record"] = write_new(self.out / "seed.collection_record.json",
                canonical({"round": rnd, "C": self.C, "designation": designation,
                           "responses": evidence, "accepted_hosts": accepted}))
            require(len(accepted) >= 2, "SEED-REFUSED: fewer than two BLS-verified refetched hosts")
            require(len(set(accepted.values())) == 1, "SEED-REFUSED: host disagreement")
            return self._record("seed", designation, {"verdict": "PASS", "round": rnd,
                "seed": next(iter(accepted.values())), "chain_hash": vd.CHAIN_HASH,
                "hosts": sorted(accepted), "responses": evidence, "outputs": outputs})
        except Exception as exc:
            self._abort("seed", designation, exc)
            raise

    def select_sample(self, seed_record):
        """Only the existing selector ranks; coordinates supply preassigned bricks."""
        try:
            seed = self._start("draw", seed_record)
            selector = _module("_optionA_dev.agreement_run.select_sample")
            args = []
            for name in ("eligible", "exclusion", "failed"):
                args.extend((self.inputs[name]["path"], self.inputs[name]["sha256"]))
            selected = selector.select(*args, seed["seed"], sizes=(400, 200, 2000))
            require(selected == selector.select(*args, seed["seed"], sizes=(400, 200, 2000)),
                    "SELECTION-NON-REPEAT")
            coords = _coordinates(self.inputs["coordinates"])
            outputs = {}
            for name in SIZES:
                ids = selected[name]
                require(all(oid in coords for oid in ids), "COORDINATES-MISSING-ID")
                outputs[name] = write_new(self.out / ("draw." + name + ".json"),
                    canonical([coords[oid] for oid in ids]))
            bindings = {"seed": seed["seed"], "round": seed["round"],
                        "selection_inputs": {n: self.inputs[n] for n in ("eligible", "exclusion", "failed")},
                        "selector_sha256": json_pin(self.C)["code"][CODE[1]],
                        "drawn_lists": outputs}
            return self._record("draw", seed_record, {"verdict": "PASS", "outputs": outputs,
                "bindings": bindings, "counts": selected["counts"], "skipped_ranks": [],
                "skipped_rank_rule": "Eligibility filtered before ranking; no skipped drawn ranks."})
        except Exception as exc:
            self._abort("draw", seed_record, exc)
            raise

    def tune(self, draw, access, inventory):
        return self._evaluate("tuning", draw, access, inventory)

    def holdout(self, tuning, opening, inventory):
        return self._evaluate("holdout", tuning, opening, inventory)

    def validate(self, holdout, custody, inventory):
        return self._evaluate("validation", holdout, custody, inventory)

    def _evaluate(self, stage, predecessor, access_pin, inventory_pin):
        try:
            prev = self._start(stage, predecessor)
            access = json_pin(access_pin)
            require(access.get("C") == self.C and access.get("predecessor") == predecessor
                    and access.get("stage") == stage, "ACCESS-BINDING")
            _anchor(access)
            require(access.get("pushed_reference") and
                    access.get("published_sha256") == predecessor["sha256"], "ACCESS-ANCHOR")
            require(access.get("bindings") == prev["bindings"], "DRAW-BINDING")
            if stage != "tuning":
                winner_pin = prev["winner"]
                require(access.get("winner") == winner_pin, "WINNER-BINDING")
                w = json_pin(access.get("W"))
                require(w.get("C") == self.C and w.get("bindings") == prev["bindings"]
                        and w.get("winner") == winner_pin and
                        w.get("tuning") == (predecessor if stage == "holdout" else prev["tuning"]),
                        "WINNER-FREEZE-BINDING")
                _anchor(w)
                require(access.get("W_published_sha256") == access["W"]["sha256"],
                        "WINNER-FREEZE-ANCHOR")
                if stage == "validation":
                    require(access["W"] == prev["W"] and
                            access.get("custody_fetch_after_winner_freeze") is True,
                            "VALIDATION-CUSTODY")
                # W binds every output used to select the winner, not just config.
                expected_evidence = (prev["outputs"] if stage == "holdout" else prev["tuning_outputs"])
                require(w.get("tuning_outputs") == expected_evidence, "TUNING-EVIDENCE-BINDING")
                for p in expected_evidence.values():
                    read_pin(p)
                winner = json_pin(winner_pin)
            identities = json_pin(prev["bindings"]["drawn_lists"][stage])
            require(len(identities) == SIZES[stage] and
                    len({r["objid"] for r in identities}) == SIZES[stage], "EXACT-DRAW-SIZE")
            # No pixel or label file has been consumed before the access checks.
            inv = json_pin(inventory_pin)
            require(inv.get("stage") == stage and inv.get("C") == self.C and
                    inv.get("drawn_list") == prev["bindings"]["drawn_lists"][stage],
                    "STAGE-INVENTORY-BINDING")
            require(access.get("inventory") == inventory_pin, "STAGE-INVENTORY-AUTHORITY")
            objects, render_rows, outputs = self._render(stage, identities, inv)
            family = _module("_optionA_dev.fourier_chirality.fourier_chirality")
            configs = family.enumerate_configs()
            require(len(configs) == 96, "GRID-COUNT")
            if stage != "tuning":
                require(winner["config"] in configs and
                        winner["config_id"] == family.config_id(winner["config"]), "WINNER-CONFIG")
                configs = [winner["config"]]
            all_scores, results = [], []
            for index, cfg in enumerate(configs):
                est = family.Estimator(cfg)
                rows = []
                for oid, label, tensor_pin, refusal in objects:
                    result = (dict(refusal) if refusal is not None else
                              score_object(est, read_pin(tensor_pin), label))
                    result.update(objid=oid, config_id=est.config_id, config_index=index)
                    rows.append(result)
                stats = stage_statistic(stage, rows)
                results.append({**stats, "config_index": index, "config": cfg,
                                "config_id": est.config_id})
                all_scores.extend(rows)
            outputs["scores"] = write_new(self.out / (stage + ".scores.jsonl"),
                                         b"".join(canonical(r) for r in all_scores))
            outputs["configurations"] = write_new(self.out / (stage + ".configurations.json"),
                                                 canonical(results))
            fields = {"bindings": prev["bindings"], "access": access_pin,
                      "inventory": inventory_pin, "outputs": outputs,
                      "render_counts": {s: sum(r["status"] == s for r in render_rows)
                                        for s in ("SCORED", "RENDER-REFUSED")}}
            if stage == "tuning":
                win = choose_winner(results)
                fields["verdict"] = "PASS" if win else "CLOSED: no eligible winner"
                fields["winner"] = None
                if win:
                    fields["winner"] = write_new(self.out / "winner.json", canonical(
                        {"config": win["config"], "config_id": win["config_id"],
                         "config_index": win["config_index"]}))
                    outputs["winner"] = fields["winner"]
                fields["n_configs"] = len(results)
            else:
                fields.update(statistic=results[0], verdict=results[0]["verdict"],
                    winner=winner_pin, W=access["W"],
                    tuning=predecessor if stage == "holdout" else prev["tuning"],
                    tuning_outputs=prev["outputs"] if stage == "holdout" else prev["tuning_outputs"])
            return self._record(stage, predecessor, fields)
        except Exception as exc:
            self._abort(stage, predecessor, exc)
            raise

    def _render(self, stage, identities, inv):
        """Pinned FITS bytes -> existing render chain -> per-identity tensor pins."""
        import numpy as np
        from astropy.io import fits
        from astropy.wcs import WCS
        chain = _module("study_renderer.render_chain_v3")
        # Check ALL expected-checksum files before development label access.
        inventory_rows = inv.get("objects", [])
        for item in inventory_rows:
            read_pin(item.get("checksums"))
        labels = json_pin(inv.get("labels"))
        require(isinstance(labels, dict) and set(labels) == {str(r["objid"]) for r in identities},
                "LABEL-ID-LIST")
        require(all(type(g) is int and g in (-1, 1) for g in labels.values()), "LABEL-INTEGRITY")
        rows = inv.get("objects", [])
        require([r.get("objid") for r in rows] == [r["objid"] for r in identities],
                "IDENTITY-LIST-MISMATCH")
        objects, receipts, outputs = [], [], {}
        for ident, row in zip(identities, rows):
            oid, brick = ident["objid"], ident["brick"]
            # A checksum manifest must precede image access. It is stage-specific.
            checksum_bytes = read_pin(row.get("checksums"))
            checksums = {}
            for line in checksum_bytes.decode("ascii").splitlines():
                parts = line.split()
                require(len(parts) == 2 and re.fullmatch("[0-9a-f]{64}", parts[0]),
                        "CHECKSUM-MANIFEST-SCHEMA")
                name = parts[1].lstrip("*")
                require(name not in checksums, "CHECKSUM-DUPLICATE")
                checksums[name] = parts[0]
            planes, wcs, absent = [], None, []
            for plane in ("image-r", "maskbits", "nexp-r"):
                name = f"legacysurvey-{brick}-{plane}.fits.fz"
                expected = checksums.get(name)
                if expected is None:
                    absent.append(plane)
                    continue
                source = row.get("planes", {}).get(plane)
                require(isinstance(source, dict) and source.get("sha256") == expected,
                        "MISSING-DIGEST: plane or checksum mismatch")
                hdu_index = source.get("hdu")
                require(type(hdu_index) is int and hdu_index >= 0, "FITS-HDU-REQUIRED")
                if "url" in source:
                    url = f"{DR9_BASE}/{brick[:3]}/{brick}/{name}"
                    require(source["url"] == url, "PLANE-URL-MISMATCH")
                    dest = self.out / (stage + ".planes") / brick / name
                    if dest.exists():
                        pin = {"path": str(dest.resolve()), "sha256": expected}
                        raw = read_pin(pin)
                    else:
                        raw = fetch_bytes(url)
                        require(sha(raw) == expected, "DIGEST-MISMATCH: fetched plane")
                        pin = write_new(dest, raw)
                else:
                    pin = {"path": source.get("path"), "sha256": source.get("sha256")}
                    raw = read_pin(pin)
                outputs[f"plane:{oid}:{plane}"] = pin
                with fits.open(io.BytesIO(raw), memmap=False) as hdus:
                    require(hdu_index < len(hdus), "FITS-HDU-MISSING")
                    data = np.array(hdus[hdu_index].data, copy=True)
                    header = hdus[hdu_index].header.copy()
                planes.append(data)
                if plane == "image-r":
                    wcs = WCS(header, relax=False)
            if absent:
                receipt = {"status": "RENDER-REFUSED", "reason": "NO-PUBLISHED-SHA",
                           "absent_planes": absent, "brick": brick, "objid": oid}
            else:
                receipt = chain.render_object(*planes, wcs, ident["ra"], ident["dec"],
                                              brick, chain.pr.r_t_validation())
                receipt["objid"] = oid
                if receipt["status"] == "REFUSED":
                    receipt["status"] = "RENDER-REFUSED"
            tensor = receipt.pop("tensor", None)
            if receipt["status"] == "SCORED":
                require(tensor is not None and sha(tensor) == receipt["tensor_sha256"],
                        "TENSOR-INTEGRITY: renderer digest")
                pin = write_new(self.out / (stage + ".tensors") / (str(oid) + ".f32"), tensor)
                outputs["tensor:" + str(oid)] = pin
                objects.append((oid, labels[str(oid)], pin, None))
            else:
                objects.append((oid, labels[str(oid)], None,
                                {"status": "RENDER-REFUSED", "reason": receipt["reason"]}))
            receipts.append(receipt)
        outputs["render"] = write_new(self.out / (stage + ".render.jsonl"),
                                      b"".join(canonical(r) for r in receipts))
        return objects, receipts, outputs


def _anchor(record):
    require(record.get("mechanism") in ("public-push", "provider-chat")
            and bool(record.get("external_reference")) and bool(record.get("third_party"))
            and record.get("third_party") != record.get("lane_owner"), "ANCHOR-REQUIRED")
    require(timestamp(record["third_party_utc"]) <= timestamp(utc()), "ANCHOR-FROM-FUTURE")

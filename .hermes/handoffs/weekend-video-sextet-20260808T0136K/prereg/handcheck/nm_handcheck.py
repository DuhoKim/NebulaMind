#!/usr/bin/env python3
"""Blinded hand-check harness for the frozen Longo-amplitude protocol.

The module is built and exercised with synthetic fixtures only. Its checker-facing
path is capability-limited: it receives a blinded package and one isolated session,
never the sealed key or another checker's session.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import hmac
import io
import json
import math
import os
import secrets
import stat
import sys
import threading
import time
import webbrowser
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, localcontext
from fractions import Fraction
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Mapping
from statistics import NormalDist
from urllib.parse import parse_qs, urlsplit

import fcntl

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from PIL import Image, ImageOps


SCHEMA_VERSION = "nm-handcheck-v2-hc1h"
PROTOCOL_RANDOM_STATE = 20260812
CHECKER_ROLES = ("A", "B")
ALL_ROLES = ("A", "B", "J")
HC1H_ROLE = "H"
HC1H_STATES = ("agree-confident", "disagree", "low-confidence")
HC1H_STRATA = tuple(f"{state}|{chi}" for state in HC1H_STATES for chi in range(3))
HC1H_SESSION_PRESENTATION_LIMIT = 50
HC1H_POWER_BOUND_N = 130_076
HC1H_POWER_GATE = Decimal("0.7905")
AUTHORITY_FILENAMES = (
    "_tmp_YUI_HARNESS_HC1H_BRIEF.md",
    "LANA_ONE_HUMAN_ATTENUATION_20260814.md",
    "HC1H_ACCEPTANCE_20260815.md",
    "KUN_HC1H_CLOSE_20260814.md",
)
PINNED_AUTHORITY_SHA256 = {
    "_tmp_YUI_HARNESS_HC1H_BRIEF.md": "143c49720c0fd3005a7ce0b0d5d43bf877fd19c3120164e942a9b15d2bd2d015",
    "LANA_ONE_HUMAN_ATTENUATION_20260814.md": "b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd",
    "HC1H_ACCEPTANCE_20260815.md": "a018233bfe7dbf7625cfe6dc5984efedec6549b0951005c5d8d727900acc5e42",
    "KUN_HC1H_CLOSE_20260814.md": "14868f37ff91ede5c58a7d0e475b9129c77253508927b094312a282dafd052f1",
}
CHECKER_INSTRUCTIONS = (
    "Classify only the apparent winding in the displayed blinded image. Press C once for "
    "counter-clockwise, W once for clockwise, F before answering if this specific item appears "
    "identifiable as synthetic or repeated, X if exposure appears systematic, or P to pause. "
    "Do not rotate or reflect the image, inspect package internals, use external classifiers, "
    "or attempt to infer the instrument label. Pause after at most 50 recorded labels."
)
PACKAGE_FIELDS = {
    "schema_version",
    "experiment_id",
    "role",
    "instructions",
    "instructions_sha256",
    "key_commitment_sha256",
    "items",
}
PACKAGE_ITEM_FIELDS = {"sequence", "item_id", "asset", "asset_sha256"}
ADJUDICATION_ITEM_FIELDS = PACKAGE_ITEM_FIELDS | {"prior_labels"}
HC1H_PACKAGE_FIELDS = PACKAGE_FIELDS
HC1H_PACKAGE_ITEM_FIELDS = PACKAGE_ITEM_FIELDS
HC1H_CONTROL_FIELDS = {
    "schema_version",
    "experiment_id",
    "role",
    "session_mac_key_hex",
    "items",
    "replacement_groups",
}
HC1H_CONTROL_ITEM_FIELDS = {
    "item_id",
    "replacement_group",
    "dependent_item_id",
    "parent_anchor_item_id",
}
FORBIDDEN_CHECKER_KEYS = {
    "root_secret_hex",
    "object_id",
    "image_path",
    "instrument_sign",
    "abs_chi",
    "angular_size",
    "committee_state",
    "category",
    "parent_item_id",
    "synthetic_id",
    "truth_sign",
    "stratum",
    "mirrored",
    "sealed_key",
}


class HandcheckError(RuntimeError):
    """Fail-closed contract error."""


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def harness_source_sha256() -> str:
    return sha256_file(Path(__file__).resolve())


def authority_hashes() -> dict[str, str]:
    prereg_root = Path(__file__).resolve().parent.parent
    result = {}
    for filename in AUTHORITY_FILENAMES:
        path = prereg_root / filename
        if not path.is_file():
            raise HandcheckError(f"required protocol authority is missing: {filename}")
        result[filename] = sha256_file(path)
    if result != PINNED_AUTHORITY_SHA256:
        raise HandcheckError("accepted HC-1H authority hash mismatch")
    return result


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _atomic_write(path: Path, data: bytes, *, mode: int = 0o640) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"_tmp_{path.name}.{os.getpid()}")
    try:
        with temporary.open("wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def _require_regular_contained(path: Path, root: Path) -> None:
    if not _is_within(path, root):
        raise HandcheckError(f"path escapes checker package: {path}")
    info = path.lstat()
    if not stat.S_ISREG(info.st_mode):
        raise HandcheckError(f"checker path is not a regular file: {path}")


def _hmac_digest(secret: bytes, purpose: str) -> bytes:
    return hmac.new(secret, purpose.encode("utf-8"), hashlib.sha256).digest()


def _seal_key(key_document: dict, passphrase: bytes) -> bytes:
    if len(passphrase) < 16:
        raise HandcheckError("key passphrase must contain at least 16 bytes")
    plaintext = canonical_json_bytes(key_document)
    salt = secrets.token_bytes(16)
    nonce = secrets.token_bytes(12)
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    encryption_key = kdf.derive(passphrase)
    aad = f"{SCHEMA_VERSION}|sealed-key".encode("utf-8")
    ciphertext = AESGCM(encryption_key).encrypt(nonce, plaintext, aad)
    envelope = {
        "schema_version": SCHEMA_VERSION,
        "cipher": "AES-256-GCM",
        "kdf": {"name": "scrypt", "n": 2**14, "r": 8, "p": 1},
        "salt_hex": salt.hex(),
        "nonce_hex": nonce.hex(),
        "ciphertext_hex": ciphertext.hex(),
        "plaintext_sha256": sha256_bytes(plaintext),
    }
    return canonical_json_bytes(envelope) + b"\n"


def unseal_key(path: Path, passphrase: bytes) -> dict:
    envelope = json.loads(path.read_text(encoding="utf-8"))
    if envelope.get("schema_version") != SCHEMA_VERSION:
        raise HandcheckError("sealed-key schema mismatch")
    try:
        salt = bytes.fromhex(envelope["salt_hex"])
        nonce = bytes.fromhex(envelope["nonce_hex"])
        ciphertext = bytes.fromhex(envelope["ciphertext_hex"])
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=int(envelope["kdf"]["n"]),
            r=int(envelope["kdf"]["r"]),
            p=int(envelope["kdf"]["p"]),
        )
        encryption_key = kdf.derive(passphrase)
        plaintext = AESGCM(encryption_key).decrypt(
            nonce, ciphertext, f"{SCHEMA_VERSION}|sealed-key".encode("utf-8")
        )
    except Exception as error:
        raise HandcheckError("sealed key could not be authenticated or decrypted") from error
    if sha256_bytes(plaintext) != envelope["plaintext_sha256"]:
        raise HandcheckError("unsealed key hash does not match its envelope")
    document = json.loads(plaintext)
    if canonical_json_bytes(document) != plaintext:
        raise HandcheckError("unsealed key is not canonical JSON")
    return document


def _read_population(path: Path) -> list[dict]:
    rows = []
    allowed = {
        "data_class",
        "object_id",
        "image_path",
        "instrument_sign",
        "abs_chi",
        "angular_size",
    }
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if set(row) != allowed:
            raise HandcheckError(f"population row {line_number} has a non-contract field set")
        if row["data_class"] not in {"synthetic", "authorized_measurement"}:
            raise HandcheckError(f"population row {line_number} has an invalid data class")
        if not isinstance(row["object_id"], str) or not row["object_id"]:
            raise HandcheckError(f"population row {line_number} has no object ID")
        if int(row["instrument_sign"]) not in (-1, 1):
            raise HandcheckError(f"population row {line_number} has an invalid instrument sign")
        for field in ("abs_chi", "angular_size"):
            if not math.isfinite(float(row[field])):
                raise HandcheckError(f"population row {line_number} has non-finite {field}")
        image_path = Path(row["image_path"])
        info = image_path.lstat()
        if not stat.S_ISREG(info.st_mode):
            raise HandcheckError(f"population row {line_number} image is not a regular file")
        rows.append(row)
    if len({row["object_id"] for row in rows}) != len(rows):
        raise HandcheckError("population object IDs are not unique")
    return rows


def _rank_tertiles(rows: list[dict], field: str, secret: bytes) -> dict[str, int]:
    ordered = sorted(
        rows,
        key=lambda row: (
            float(row[field]),
            _hmac_digest(secret, f"tertile-tie|{field}|{row['object_id']}"),
        ),
    )
    return {
        row["object_id"]: min(2, (3 * rank) // len(ordered))
        for rank, row in enumerate(ordered)
    }


def _render_blinded_png(source: Path, mirrored: bool) -> bytes:
    with Image.open(source) as opened:
        opened.load()
        image = opened.copy()
    if image.mode not in {"L", "RGB", "RGBA"}:
        image = image.convert("RGB")
    if mirrored:
        image = ImageOps.mirror(image)
    output = io.BytesIO()
    image.save(output, format="PNG", optimize=False, compress_level=9)
    return output.getvalue()


def _reject_overlapping_roots(private_root: Path, checking_root: Path) -> None:
    private = private_root.resolve()
    checking = checking_root.resolve()
    if private == checking or _is_within(private, checking) or _is_within(checking, private):
        raise HandcheckError("private and checker roots must be disjoint")


def prepare_experiment(
    *,
    population_path: Path,
    private_root: Path,
    checking_root: Path,
    passphrase: bytes,
    checker_ids: Mapping[str, str],
    total: int = 500,
    floor: int = 40,
) -> dict:
    """Select, blind, encrypt, and hash-commit a hand-check before any session."""
    _reject_overlapping_roots(private_root, checking_root)
    if private_root.exists() or checking_root.exists():
        raise HandcheckError("prepare refuses to overwrite an existing private or checker root")
    if set(checker_ids) != set(ALL_ROLES):
        raise HandcheckError("checker identities must contain exactly A, B, and J")
    normalized_ids = {role: str(checker_ids[role]).strip() for role in ALL_ROLES}
    if any(not value for value in normalized_ids.values()) or len(set(normalized_ids.values())) != 3:
        raise HandcheckError("checker identities must be non-empty and distinct")

    rows = _read_population(population_path)
    if not rows:
        raise HandcheckError("population is empty")
    data_classes = {row["data_class"] for row in rows}
    if len(data_classes) != 1:
        raise HandcheckError("population cannot mix synthetic and authorized-measurement rows")
    data_class = next(iter(data_classes))
    if data_class == "authorized_measurement" and (total != 500 or floor != 40):
        raise HandcheckError("authorized measurement requires frozen total=500 and floor=40")
    root_secret = secrets.token_bytes(32)
    experiment_id = _hmac_digest(root_secret, "experiment-id").hex()[:24]
    chi_tertiles = _rank_tertiles(rows, "abs_chi", root_secret)
    size_tertiles = _rank_tertiles(rows, "angular_size", root_secret)
    strata: dict[str, list[dict]] = {f"{chi}{size}": [] for chi in range(3) for size in range(3)}
    for row in rows:
        stratum = f"{chi_tertiles[row['object_id']]}{size_tertiles[row['object_id']]}"
        strata[stratum].append(row)
    populations = {key: len(value) for key, value in strata.items()}
    allocation = allocate_proportional_floor(populations, total=total, floor=floor)

    selected: list[tuple[str, dict]] = []
    for stratum in sorted(strata):
        ranked = sorted(
            strata[stratum],
            key=lambda row: _hmac_digest(
                root_secret, f"sample|{PROTOCOL_RANDOM_STATE}|{row['object_id']}"
            ),
        )
        selected.extend((stratum, row) for row in ranked[: allocation[stratum]])

    private_root.mkdir(parents=True, mode=0o700)
    checking_root.mkdir(parents=True, mode=0o750)
    assignments = []
    blinded_pngs: dict[str, bytes] = {}
    for stratum, row in selected:
        object_id = row["object_id"]
        item_id = _hmac_digest(root_secret, f"opaque-item|{object_id}").hex()[:32]
        mirrored = bool(
            _hmac_digest(root_secret, f"parity|{PROTOCOL_RANDOM_STATE}|{object_id}")[0] & 1
        )
        rendered = _render_blinded_png(Path(row["image_path"]), mirrored)
        blinded_pngs[item_id] = rendered
        assignments.append(
            {
                "item_id": item_id,
                "object_id": object_id,
                "image_path": str(Path(row["image_path"]).resolve()),
                "source_image_sha256": sha256_file(Path(row["image_path"])),
                "instrument_sign": int(row["instrument_sign"]),
                "abs_chi": float(row["abs_chi"]),
                "angular_size": float(row["angular_size"]),
                "stratum": stratum,
                "mirrored": mirrored,
                "blinded_png_sha256": sha256_bytes(rendered),
            }
        )

    key_document = {
        "schema_version": SCHEMA_VERSION,
        "experiment_id": experiment_id,
        "created_at": utc_now(),
        "protocol_random_state": PROTOCOL_RANDOM_STATE,
        "data_class": data_class,
        "root_secret_hex": root_secret.hex(),
        "population_sha256": sha256_file(population_path),
        "population_size": len(rows),
        "stratum_populations": populations,
        "stratum_allocation": allocation,
        "sample_size": total,
        "floor": floor,
        "checker_identities": normalized_ids,
        "checker_identity_sha256": {
            role: sha256_bytes(normalized_ids[role].encode("utf-8")) for role in ALL_ROLES
        },
        "instructions": CHECKER_INSTRUCTIONS,
        "instructions_sha256": sha256_bytes(CHECKER_INSTRUCTIONS.encode("utf-8")),
        "harness_source_sha256": harness_source_sha256(),
        "authority_sha256": authority_hashes(),
        "assignments": sorted(assignments, key=lambda row: row["item_id"]),
    }
    key_plaintext_sha = sha256_bytes(canonical_json_bytes(key_document))
    envelope_bytes = _seal_key(key_document, passphrase)
    sealed_path = private_root / "sealed_key.nmhc"
    _atomic_write(sealed_path, envelope_bytes, mode=0o600)

    package_descriptors = {}
    for role in CHECKER_ROLES:
        package_root = checking_root / f"checker_{role}"
        assets_root = package_root / "assets"
        assets_root.mkdir(parents=True, mode=0o750)
        ordered_assignments = sorted(
            assignments,
            key=lambda row: _hmac_digest(
                root_secret, f"checker-order|{role}|{row['item_id']}"
            ),
        )
        items = []
        for sequence, assignment in enumerate(ordered_assignments):
            item_id = assignment["item_id"]
            relative_asset = f"assets/{item_id}.png"
            _atomic_write(package_root / relative_asset, blinded_pngs[item_id], mode=0o640)
            items.append(
                {
                    "sequence": sequence,
                    "item_id": item_id,
                    "asset": relative_asset,
                    "asset_sha256": assignment["blinded_png_sha256"],
                }
            )
        package = {
            "schema_version": SCHEMA_VERSION,
            "experiment_id": experiment_id,
            "role": role,
            "instructions": CHECKER_INSTRUCTIONS,
            "instructions_sha256": key_document["instructions_sha256"],
            "key_commitment_sha256": key_plaintext_sha,
            "items": items,
        }
        package_bytes = canonical_json_bytes(package) + b"\n"
        _atomic_write(package_root / "package.json", package_bytes, mode=0o640)
        package_descriptors[role] = {
            "relative_path": f"checker_{role}/package.json",
            "sha256": sha256_bytes(package_bytes),
            "items": total,
        }

    commitment = {
        "schema_version": SCHEMA_VERSION,
        "status": "KEY_COMMITTED_BEFORE_CHECKING",
        "created_at": utc_now(),
        "experiment_id": experiment_id,
        "protocol_random_state": PROTOCOL_RANDOM_STATE,
        "data_class": data_class,
        "sample_size": total,
        "strata": 9,
        "floor": floor,
        "population_sha256": key_document["population_sha256"],
        "sealed_key_plaintext_sha256": key_plaintext_sha,
        "sealed_key_envelope_sha256": sha256_bytes(envelope_bytes),
        "instructions_sha256": key_document["instructions_sha256"],
        "harness_source_sha256": key_document["harness_source_sha256"],
        "authority_sha256": key_document["authority_sha256"],
        "checker_identity_sha256": key_document["checker_identity_sha256"],
        "checker_packages": package_descriptors,
        "public_boundary": "commitment and package hashes only; no source IDs, parity, instrument signs, strata, or answers",
    }
    commitment_bytes = canonical_json_bytes(commitment) + b"\n"
    commitment_sha = sha256_bytes(commitment_bytes)
    _atomic_write(checking_root / "commitment.json", commitment_bytes, mode=0o640)
    _atomic_write(checking_root / "commitment.sha256", (commitment_sha + "\n").encode(), mode=0o640)
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "status": "PREPARED_AND_COMMITTED_BEFORE_CHECKING",
        "experiment_id": experiment_id,
        "commitment_sha256": commitment_sha,
        "sealed_key_plaintext_sha256": key_plaintext_sha,
        "sealed_key_envelope_sha256": sha256_bytes(envelope_bytes),
        "population_sha256": key_document["population_sha256"],
        "data_class": data_class,
        "sample_size": total,
        "stratum_populations": populations,
        "stratum_allocation": allocation,
        "checker_package_sha256": {
            role: package_descriptors[role]["sha256"] for role in CHECKER_ROLES
        },
        "checking_started": False,
    }
    _atomic_write(
        private_root / "prepare_receipt.json",
        canonical_json_bytes(receipt) + b"\n",
        mode=0o600,
    )
    return receipt


def _read_hc1h_rows(path: Path, *, injection: bool) -> list[dict]:
    allowed = (
        {"data_class", "synthetic_id", "image_path", "truth_sign", "abs_chi", "committee_state"}
        if injection
        else {"data_class", "object_id", "image_path", "instrument_sign", "abs_chi", "committee_state"}
    )
    identity_field = "synthetic_id" if injection else "object_id"
    sign_field = "truth_sign" if injection else "instrument_sign"
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if set(row) != allowed:
            raise HandcheckError(f"HC-1H row {line_number} has a non-contract field set")
        if row["data_class"] not in ({"synthetic"} if injection else {"synthetic", "authorized_measurement"}):
            raise HandcheckError(f"HC-1H row {line_number} has an invalid data class")
        if not isinstance(row[identity_field], str) or not row[identity_field]:
            raise HandcheckError(f"HC-1H row {line_number} has no stable identity")
        if int(row[sign_field]) not in (-1, 1):
            raise HandcheckError(f"HC-1H row {line_number} has an invalid sign")
        if row["committee_state"] not in HC1H_STATES:
            raise HandcheckError(f"HC-1H row {line_number} has an invalid committee state")
        if not math.isfinite(float(row["abs_chi"])):
            raise HandcheckError(f"HC-1H row {line_number} has non-finite abs_chi")
        image_path = Path(row["image_path"])
        if not stat.S_ISREG(image_path.lstat().st_mode):
            raise HandcheckError(f"HC-1H row {line_number} image is not a regular file")
        rows.append(row)
    if not rows or len({row[identity_field] for row in rows}) != len(rows):
        raise HandcheckError("HC-1H input identities must be nonempty and unique")
    return rows


def _hc1h_real_strata_and_cutpoints(
    rows: list[dict], *, identity_field: str, secret: bytes
) -> tuple[dict[str, list[dict]], tuple[float, float]]:
    rank_rows = [dict(row, object_id=row[identity_field]) for row in rows]
    chi_tertiles = _rank_tertiles(rank_rows, "abs_chi", secret)
    values_by_tertile = {
        tertile: [float(row["abs_chi"]) for row in rows if chi_tertiles[row[identity_field]] == tertile]
        for tertile in range(3)
    }
    if any(not values_by_tertile[tertile] for tertile in range(3)):
        raise HandcheckError("accepted-population |chi| tertiles are empty")
    lower0 = max(values_by_tertile[0])
    upper0 = min(values_by_tertile[1])
    lower1 = max(values_by_tertile[1])
    upper1 = min(values_by_tertile[2])
    if lower0 >= upper0 or lower1 >= upper1:
        raise HandcheckError("accepted-population |chi| has a tie across a tertile boundary")
    cutpoints = ((lower0 + upper0) / 2.0, (lower1 + upper1) / 2.0)
    strata = {stratum: [] for stratum in HC1H_STRATA}
    for row in rows:
        stratum = f"{row['committee_state']}|{chi_tertiles[row[identity_field]]}"
        strata[stratum].append(row)
    return strata, cutpoints


def _hc1h_strata_from_cutpoints(
    rows: list[dict], *, cutpoints: tuple[float, float]
) -> dict[str, list[dict]]:
    strata = {stratum: [] for stratum in HC1H_STRATA}
    lower, upper = cutpoints
    for row in rows:
        value = float(row["abs_chi"])
        tertile = 0 if value <= lower else 1 if value <= upper else 2
        strata[f"{row['committee_state']}|{tertile}"].append(row)
    return strata


def _balanced_hc1h_allocation(total: int, secret: bytes) -> dict[str, int]:
    if total < 0:
        raise HandcheckError("HC-1H balanced allocation total cannot be negative")
    base, remainder = divmod(total, len(HC1H_STRATA))
    order = sorted(HC1H_STRATA, key=lambda key: _hmac_digest(secret, f"balanced-extra|{key}"))
    return {key: base + int(key in set(order[:remainder])) for key in HC1H_STRATA}


def prepare_hc1h_experiment(
    *,
    real_population_path: Path,
    synthetic_pool_path: Path,
    neyman_prior_rates: Mapping[str, Decimal | float | str],
    private_root: Path,
    checking_root: Path,
    passphrase: bytes,
    checker_id: str,
    mode: str = "full",
    real_total: int = 500,
    synthetic_total: int = 200,
    repeat_total: int = 150,
    real_floor: int = 30,
    replacement_reserve_per_group: int = 1,
    pilot_private_root: Path | None = None,
    pilot_public_result_path: Path | None = None,
    additional_covariance: Decimal | None = None,
) -> dict:
    """Prepare the accepted one-human HC-1H blinded stream."""
    pinned_authority_hashes = authority_hashes()
    _reject_overlapping_roots(private_root, checking_root)
    if private_root.exists() or checking_root.exists():
        raise HandcheckError("prepare refuses to overwrite an existing private or checker root")
    if mode not in {"full", "pilot"}:
        raise HandcheckError("HC-1H mode must be full or pilot")
    normalized_checker = str(checker_id).strip()
    if not normalized_checker:
        raise HandcheckError("HC-1H checker identity is required")

    real_rows = _read_hc1h_rows(real_population_path, injection=False)
    injection_rows = _read_hc1h_rows(synthetic_pool_path, injection=True)
    pilot_exclusion = None
    if (pilot_private_root is None) != (pilot_public_result_path is None):
        raise HandcheckError("full-from-pilot exclusion requires both pilot private root and public result")
    if pilot_private_root is not None and pilot_public_result_path is not None:
        if mode != "full":
            raise HandcheckError("pilot synthetic exclusion applies only when preparing the full run")
        if not pilot_public_result_path.is_file():
            raise HandcheckError("pilot public result is missing")
        pilot_result = json.loads(pilot_public_result_path.read_bytes())
        if (
            pilot_result.get("mode") != "pilot"
            or pilot_result.get("pilot_outcome") != "PASS-TO-FULL-HC1H"
            or "attenuation" in pilot_result.get("statistics", {})
        ):
            raise HandcheckError("full preparation requires a PASS pilot result that did not produce a")
        pilot_sealed = unseal_key(pilot_private_root / "sealed_key.nmhc", passphrase)
        pilot_plaintext_sha = sha256_bytes(canonical_json_bytes(pilot_sealed))
        if (
            pilot_sealed.get("mode") != "pilot"
            or pilot_result.get("commitments", {}).get("sealed_key_plaintext_sha256")
            != pilot_plaintext_sha
        ):
            raise HandcheckError("pilot result and sealed key do not share one committed chain")
        excluded_synthetic_ids = {
            row["synthetic_id"]
            for row in pilot_sealed["assignments"] + pilot_sealed.get("reserve_assignments", [])
            if row["category"] == "synthetic"
        }
        injection_rows = [
            row for row in injection_rows if row["synthetic_id"] not in excluded_synthetic_ids
        ]
        pilot_exclusion = {
            "pilot_experiment_id": pilot_sealed["experiment_id"],
            "pilot_sealed_key_plaintext_sha256": pilot_plaintext_sha,
            "pilot_public_result_sha256": sha256_file(pilot_public_result_path),
            "excluded_synthetic_ids_count": len(excluded_synthetic_ids),
            "pilot_synthetics_reused": False,
        }
    data_classes = {row["data_class"] for row in real_rows}
    if len(data_classes) != 1:
        raise HandcheckError("HC-1H real population cannot mix data classes")
    data_class = next(iter(data_classes))
    if additional_covariance is None:
        if data_class == "authorized_measurement" and mode == "full":
            raise HandcheckError(
                "authorized full HC-1H requires a separately approved non-negative additional covariance term"
            )
        additional_covariance = Decimal("0")
    else:
        additional_covariance = Decimal(str(additional_covariance))
    if not additional_covariance.is_finite() or additional_covariance < 0:
        raise HandcheckError("additional covariance must be a finite non-negative variance term")
    if data_class == "authorized_measurement":
        expected = (90, 40, 20, 10) if mode == "pilot" else (500, 200, 150, 30)
        if (real_total, synthetic_total, repeat_total, real_floor) != expected:
            raise HandcheckError(
                f"authorized HC-1H {mode} requires real/synthetic/repeat/floor={expected}"
            )
    if mode == "pilot" and (real_total, synthetic_total, repeat_total) != (90, 40, 20):
        if data_class != "synthetic":
            raise HandcheckError("HC-1H pilot counts are frozen at 90/40/20")
    if repeat_total < 0 or repeat_total > real_total:
        raise HandcheckError("HC-1H repeat count must be between zero and the real count")
    if replacement_reserve_per_group < 1:
        raise HandcheckError("HC-7 requires at least one replacement reserve per category-stratum group")

    root_secret = secrets.token_bytes(32)
    experiment_id = _hmac_digest(root_secret, f"hc1h-experiment|{mode}").hex()[:24]
    real_strata, chi_tertile_cutpoints = _hc1h_real_strata_and_cutpoints(
        real_rows, identity_field="object_id", secret=root_secret
    )
    injection_strata = _hc1h_strata_from_cutpoints(
        injection_rows, cutpoints=chi_tertile_cutpoints
    )
    populations = {key: len(real_strata[key]) for key in HC1H_STRATA}
    if mode == "pilot":
        real_allocation = {key: real_total // 9 for key in HC1H_STRATA}
        if real_total != 90 or any(value != 10 for value in real_allocation.values()):
            raise HandcheckError("HC-1H pilot requires exactly ten real labels per stratum")
    else:
        real_allocation = allocate_neyman(
            populations, neyman_prior_rates, total=real_total, floor=real_floor
        )
    injection_allocation = _balanced_hc1h_allocation(synthetic_total, root_secret)
    for stratum in HC1H_STRATA:
        if len(injection_strata[stratum]) < injection_allocation[stratum]:
            raise HandcheckError(f"synthetic injection pool is too small in stratum {stratum}")

    selected_real: list[tuple[str, dict]] = []
    selected_injections: list[tuple[str, dict]] = []
    for stratum in HC1H_STRATA:
        ranked_real = sorted(
            real_strata[stratum],
            key=lambda row: _hmac_digest(
                root_secret, f"hc1h-real-sample|{PROTOCOL_RANDOM_STATE}|{row['object_id']}"
            ),
        )
        selected_real.extend((stratum, row) for row in ranked_real[: real_allocation[stratum]])
        ranked_injections = sorted(
            injection_strata[stratum],
            key=lambda row: _hmac_digest(
                root_secret,
                f"hc1h-injection-sample|{PROTOCOL_RANDOM_STATE}|{row['synthetic_id']}",
            ),
        )
        selected_injections.extend(
            (stratum, row) for row in ranked_injections[: injection_allocation[stratum]]
        )

    private_root.mkdir(parents=True, mode=0o700)
    checking_root.mkdir(parents=True, mode=0o750)
    assignments: list[dict] = []
    pngs: dict[str, bytes] = {}
    real_assignment_by_object: dict[str, dict] = {}

    for stratum, row in selected_real:
        object_id = row["object_id"]
        item_id = _hmac_digest(root_secret, f"hc1h-item|real|{object_id}").hex()[:32]
        mirrored = bool(
            _hmac_digest(root_secret, f"parity|{PROTOCOL_RANDOM_STATE}|real|{object_id}")[0] & 1
        )
        rendered = _render_blinded_png(Path(row["image_path"]), mirrored)
        assignment = {
            "item_id": item_id,
            "category": "real",
            "object_id": object_id,
            "image_path": str(Path(row["image_path"]).resolve()),
            "source_image_sha256": sha256_file(Path(row["image_path"])),
            "instrument_sign": int(row["instrument_sign"]),
            "abs_chi": float(row["abs_chi"]),
            "committee_state": row["committee_state"],
            "stratum": stratum,
            "mirrored": mirrored,
            "parent_item_id": None,
            "blinded_png_sha256": sha256_bytes(rendered),
        }
        assignments.append(assignment)
        real_assignment_by_object[object_id] = assignment
        pngs[item_id] = rendered

    for stratum, row in selected_injections:
        synthetic_id = row["synthetic_id"]
        item_id = _hmac_digest(root_secret, f"hc1h-item|synthetic|{synthetic_id}").hex()[:32]
        mirrored = bool(
            _hmac_digest(
                root_secret, f"parity|{PROTOCOL_RANDOM_STATE}|synthetic|{synthetic_id}"
            )[0]
            & 1
        )
        rendered = _render_blinded_png(Path(row["image_path"]), mirrored)
        assignments.append(
            {
                "item_id": item_id,
                "category": "synthetic",
                "synthetic_id": synthetic_id,
                "image_path": str(Path(row["image_path"]).resolve()),
                "source_image_sha256": sha256_file(Path(row["image_path"])),
                "truth_sign": int(row["truth_sign"]),
                "abs_chi": float(row["abs_chi"]),
                "committee_state": row["committee_state"],
                "stratum": stratum,
                "mirrored": mirrored,
                "parent_item_id": None,
                "blinded_png_sha256": sha256_bytes(rendered),
            }
        )
        pngs[item_id] = rendered

    repeat_candidates = sorted(
        real_assignment_by_object.values(),
        key=lambda row: _hmac_digest(root_secret, f"hc1h-repeat-sample|{row['object_id']}"),
    )
    repeat_sources = []
    repeat_counts_by_stratum = {stratum: 0 for stratum in HC1H_STRATA}
    for candidate in repeat_candidates:
        stratum = candidate["stratum"]
        if repeat_counts_by_stratum[stratum] >= real_allocation[stratum] - replacement_reserve_per_group:
            continue
        repeat_sources.append(candidate)
        repeat_counts_by_stratum[stratum] += 1
        if len(repeat_sources) == repeat_total:
            break
    if len(repeat_sources) != repeat_total:
        raise HandcheckError("random repeat sample cannot preserve distinct HC-7 reserve parents")
    for parent in repeat_sources:
        object_id = parent["object_id"]
        item_id = _hmac_digest(root_secret, f"hc1h-item|repeat|{object_id}").hex()[:32]
        mirrored = not bool(parent["mirrored"])
        rendered = _render_blinded_png(Path(parent["image_path"]), mirrored)
        assignments.append(
            {
                "item_id": item_id,
                "category": "repeat",
                "object_id": object_id,
                "image_path": parent["image_path"],
                "source_image_sha256": parent["source_image_sha256"],
                "instrument_sign": parent["instrument_sign"],
                "abs_chi": parent["abs_chi"],
                "committee_state": parent["committee_state"],
                "stratum": parent["stratum"],
                "mirrored": mirrored,
                "parent_item_id": parent["item_id"],
                "blinded_png_sha256": sha256_bytes(rendered),
            }
        )
        pngs[item_id] = rendered

    children = {
        row["parent_item_id"]: row
        for row in assignments
        if row["category"] == "repeat"
    }
    available = [row for row in assignments if row["category"] != "repeat"]
    ordered_assignments = []
    while available:
        available.sort(
            key=lambda row: _hmac_digest(root_secret, f"hc1h-stream-order|{row['item_id']}")
        )
        current = available.pop(0)
        ordered_assignments.append(current)
        child = children.get(current["item_id"])
        if child is not None:
            available.append(child)
    if len(ordered_assignments) != real_total + synthetic_total + repeat_total:
        raise HandcheckError("HC-1H stream construction did not close")

    def replacement_group(category: str, stratum: str) -> str:
        return _hmac_digest(root_secret, f"hc7-replacement-group|{category}|{stratum}").hex()[:24]

    for assignment in assignments:
        assignment["replacement_group"] = replacement_group(
            assignment["category"], assignment["stratum"]
        )

    reserve_assignments: list[dict] = []
    repeated_parent_ids = {row["parent_item_id"] for row in assignments if row["category"] == "repeat"}
    for stratum in HC1H_STRATA:
        ranked_real = sorted(
            real_strata[stratum],
            key=lambda row: _hmac_digest(
                root_secret, f"hc1h-real-sample|{PROTOCOL_RANDOM_STATE}|{row['object_id']}"
            ),
        )
        real_reserve_rows = ranked_real[
            real_allocation[stratum] : real_allocation[stratum] + replacement_reserve_per_group
        ]
        if len(real_reserve_rows) != replacement_reserve_per_group:
            raise HandcheckError(f"HC-7 real replacement reserve is too small in {stratum}")
        for reserve_index, row in enumerate(real_reserve_rows):
            object_id = row["object_id"]
            item_id = _hmac_digest(
                root_secret, f"hc7-reserve|real|{stratum}|{reserve_index}|{object_id}"
            ).hex()[:32]
            mirrored = bool(
                _hmac_digest(root_secret, f"parity|hc7-reserve|real|{object_id}")[0] & 1
            )
            rendered = _render_blinded_png(Path(row["image_path"]), mirrored)
            reserve_assignments.append(
                {
                    "item_id": item_id,
                    "category": "real",
                    "object_id": object_id,
                    "image_path": str(Path(row["image_path"]).resolve()),
                    "source_image_sha256": sha256_file(Path(row["image_path"])),
                    "instrument_sign": int(row["instrument_sign"]),
                    "abs_chi": float(row["abs_chi"]),
                    "committee_state": row["committee_state"],
                    "stratum": stratum,
                    "mirrored": mirrored,
                    "parent_item_id": None,
                    "replacement_group": replacement_group("real", stratum),
                    "blinded_png_sha256": sha256_bytes(rendered),
                }
            )
            pngs[item_id] = rendered

        ranked_injections = sorted(
            injection_strata[stratum],
            key=lambda row: _hmac_digest(
                root_secret,
                f"hc1h-injection-sample|{PROTOCOL_RANDOM_STATE}|{row['synthetic_id']}",
            ),
        )
        synthetic_reserve_rows = ranked_injections[
            injection_allocation[stratum] : injection_allocation[stratum]
            + replacement_reserve_per_group
        ]
        if len(synthetic_reserve_rows) != replacement_reserve_per_group:
            raise HandcheckError(f"HC-7 synthetic replacement reserve is too small in {stratum}")
        for reserve_index, row in enumerate(synthetic_reserve_rows):
            synthetic_id = row["synthetic_id"]
            item_id = _hmac_digest(
                root_secret,
                f"hc7-reserve|synthetic|{stratum}|{reserve_index}|{synthetic_id}",
            ).hex()[:32]
            mirrored = bool(
                _hmac_digest(root_secret, f"parity|hc7-reserve|synthetic|{synthetic_id}")[0]
                & 1
            )
            rendered = _render_blinded_png(Path(row["image_path"]), mirrored)
            reserve_assignments.append(
                {
                    "item_id": item_id,
                    "category": "synthetic",
                    "synthetic_id": synthetic_id,
                    "image_path": str(Path(row["image_path"]).resolve()),
                    "source_image_sha256": sha256_file(Path(row["image_path"])),
                    "truth_sign": int(row["truth_sign"]),
                    "abs_chi": float(row["abs_chi"]),
                    "committee_state": row["committee_state"],
                    "stratum": stratum,
                    "mirrored": mirrored,
                    "parent_item_id": None,
                    "replacement_group": replacement_group("synthetic", stratum),
                    "blinded_png_sha256": sha256_bytes(rendered),
                }
            )
            pngs[item_id] = rendered

        repeat_candidates = sorted(
            (
                row
                for row in assignments
                if row["category"] == "real"
                and row["stratum"] == stratum
                and row["item_id"] not in repeated_parent_ids
            ),
            key=lambda row: _hmac_digest(
                root_secret, f"hc7-repeat-reserve-source|{row['item_id']}"
            ),
        )
        repeat_reserve_count = replacement_reserve_per_group
        if len(repeat_candidates) < repeat_reserve_count:
            raise HandcheckError(
                f"HC-7 needs {repeat_reserve_count} distinct previously unrepeated parents in {stratum}"
            )
        for reserve_index, parent in enumerate(repeat_candidates[:repeat_reserve_count]):
            item_id = _hmac_digest(
                root_secret,
                f"hc7-reserve|repeat|{stratum}|{reserve_index}|{parent['object_id']}",
            ).hex()[:32]
            mirrored = not bool(parent["mirrored"])
            rendered = _render_blinded_png(Path(parent["image_path"]), mirrored)
            reserve_assignments.append(
                {
                    "item_id": item_id,
                    "category": "repeat",
                    "object_id": parent["object_id"],
                    "image_path": parent["image_path"],
                    "source_image_sha256": parent["source_image_sha256"],
                    "instrument_sign": parent["instrument_sign"],
                    "abs_chi": parent["abs_chi"],
                    "committee_state": parent["committee_state"],
                    "stratum": stratum,
                    "mirrored": mirrored,
                    "parent_item_id": parent["item_id"],
                    "replacement_group": replacement_group("repeat", stratum),
                    "blinded_png_sha256": sha256_bytes(rendered),
                }
            )
            pngs[item_id] = rendered

    image_shapes = set()
    for rendered in pngs.values():
        with Image.open(io.BytesIO(rendered)) as image:
            image_shapes.add((image.mode, image.size))
    if len(image_shapes) != 1:
        raise HandcheckError("HC-1H source and injection assets must share one mode and pixel size")

    key_document = {
        "schema_version": SCHEMA_VERSION,
        "protocol": "HC-1H",
        "mode": mode,
        "experiment_id": experiment_id,
        "created_at": utc_now(),
        "protocol_random_state": PROTOCOL_RANDOM_STATE,
        "data_class": data_class,
        "pilot_exclusion": pilot_exclusion,
        "root_secret_hex": root_secret.hex(),
        "real_population_sha256": sha256_file(real_population_path),
        "synthetic_pool_sha256": sha256_file(synthetic_pool_path),
        "real_population_size": len(real_rows),
        "stratum_populations": populations,
        "chi_tertile_cutpoints_from_real_population": list(chi_tertile_cutpoints),
        "neyman_prior_rates": {key: str(Decimal(str(neyman_prior_rates[key]))) for key in HC1H_STRATA},
        "real_allocation": real_allocation,
        "synthetic_allocation": injection_allocation,
        "category_counts": {"real": real_total, "synthetic": synthetic_total, "repeat": repeat_total},
        "labels_required": len(ordered_assignments),
        "real_floor": real_floor,
        "power_bound_n": HC1H_POWER_BOUND_N,
        "power_gate": str(HC1H_POWER_GATE),
        "additional_covariance": str(additional_covariance),
        "checker_identity": normalized_checker,
        "checker_identity_sha256": sha256_bytes(normalized_checker.encode("utf-8")),
        "instructions": CHECKER_INSTRUCTIONS,
        "instructions_sha256": sha256_bytes(CHECKER_INSTRUCTIONS.encode("utf-8")),
        "harness_source_sha256": harness_source_sha256(),
        "authority_sha256": pinned_authority_hashes,
        "assignments": sorted(assignments, key=lambda row: row["item_id"]),
        "reserve_assignments": sorted(reserve_assignments, key=lambda row: row["item_id"]),
        "stream_order": [row["item_id"] for row in ordered_assignments],
    }
    plaintext_sha = sha256_bytes(canonical_json_bytes(key_document))
    envelope_bytes = _seal_key(key_document, passphrase)
    _atomic_write(private_root / "sealed_key.nmhc", envelope_bytes, mode=0o600)

    package_root = checking_root / "checker_H"
    (package_root / "assets").mkdir(parents=True, mode=0o750)
    items = []
    control_items = []
    repeat_child_by_parent = {
        row["parent_item_id"]: row["item_id"]
        for row in assignments
        if row["category"] == "repeat"
    }
    for sequence, assignment in enumerate(ordered_assignments):
        relative_asset = f"assets/{assignment['item_id']}.png"
        _atomic_write(package_root / relative_asset, pngs[assignment["item_id"]], mode=0o640)
        items.append(
            {
                "sequence": sequence,
                "item_id": assignment["item_id"],
                "asset": relative_asset,
                "asset_sha256": assignment["blinded_png_sha256"],
            }
        )
        control_items.append(
            {
                "item_id": assignment["item_id"],
                "replacement_group": assignment["replacement_group"],
                "dependent_item_id": repeat_child_by_parent.get(assignment["item_id"]),
                "parent_anchor_item_id": assignment["parent_item_id"],
            }
        )
    control_replacement_groups = {}
    next_sequence = len(items)
    for group_id in sorted({row["replacement_group"] for row in reserve_assignments}):
        control_replacement_groups[group_id] = []
        group_rows = sorted(
            (row for row in reserve_assignments if row["replacement_group"] == group_id),
            key=lambda row: _hmac_digest(root_secret, f"hc7-reserve-order|{row['item_id']}"),
        )
        for assignment in group_rows:
            relative_asset = f"assets/{assignment['item_id']}.png"
            _atomic_write(package_root / relative_asset, pngs[assignment["item_id"]], mode=0o640)
            control_replacement_groups[group_id].append(
                {
                    "sequence": next_sequence,
                    "item_id": assignment["item_id"],
                    "asset": relative_asset,
                    "asset_sha256": assignment["blinded_png_sha256"],
                    "replacement_group": group_id,
                    "dependent_item_id": None,
                    "parent_anchor_item_id": assignment["parent_item_id"],
                }
            )
            next_sequence += 1
    package = {
        "schema_version": SCHEMA_VERSION,
        "experiment_id": experiment_id,
        "role": HC1H_ROLE,
        "instructions": CHECKER_INSTRUCTIONS,
        "instructions_sha256": key_document["instructions_sha256"],
        "key_commitment_sha256": plaintext_sha,
        "items": items,
    }
    package_bytes = canonical_json_bytes(package) + b"\n"
    _atomic_write(package_root / "package.json", package_bytes, mode=0o640)
    package_descriptor = {
        "relative_path": "checker_H/package.json",
        "sha256": sha256_bytes(package_bytes),
        "items": len(items),
    }
    checker_control = {
        "schema_version": SCHEMA_VERSION,
        "experiment_id": experiment_id,
        "role": HC1H_ROLE,
        "session_mac_key_hex": _hmac_digest(root_secret, "hc1h-session-event-mac").hex(),
        "items": control_items,
        "replacement_groups": control_replacement_groups,
    }
    checker_control_bytes = canonical_json_bytes(checker_control) + b"\n"
    checker_control_path = private_root / "checker_H_control.json"
    _atomic_write(checker_control_path, checker_control_bytes, mode=0o600)
    checker_control_sha256 = sha256_bytes(checker_control_bytes)

    commitment = {
        "schema_version": SCHEMA_VERSION,
        "status": "HC1H_KEY_COMMITTED_BEFORE_CHECKING",
        "protocol": "HC-1H",
        "mode": mode,
        "created_at": utc_now(),
        "experiment_id": experiment_id,
        "data_class": data_class,
        "pilot_exclusion": pilot_exclusion,
        "labels_required": len(items),
        "real_labels": real_total,
        "synthetic_labels": synthetic_total,
        "repeat_labels": repeat_total,
        "strata": 9,
        "real_floor": real_floor,
        "chi_tertile_cutpoints_from_real_population": list(chi_tertile_cutpoints),
        "power_bound_n": HC1H_POWER_BOUND_N,
        "power_gate": str(HC1H_POWER_GATE),
        "additional_covariance": str(additional_covariance),
        "real_population_sha256": key_document["real_population_sha256"],
        "synthetic_pool_sha256": key_document["synthetic_pool_sha256"],
        "sealed_key_plaintext_sha256": plaintext_sha,
        "sealed_key_envelope_sha256": sha256_bytes(envelope_bytes),
        "instructions_sha256": key_document["instructions_sha256"],
        "harness_source_sha256": key_document["harness_source_sha256"],
        "authority_sha256": key_document["authority_sha256"],
        "checker_identity_sha256": key_document["checker_identity_sha256"],
        "checker_control_sha256": checker_control_sha256,
        "checker_packages": {HC1H_ROLE: package_descriptor},
        "public_boundary": "opaque one-human stream only; no item type, source, truth, sign, stratum, parity, or answer",
    }
    commitment_bytes = canonical_json_bytes(commitment) + b"\n"
    commitment_sha = sha256_bytes(commitment_bytes)
    _atomic_write(checking_root / "commitment.json", commitment_bytes, mode=0o640)
    _atomic_write(checking_root / "commitment.sha256", (commitment_sha + "\n").encode(), mode=0o640)
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "status": "HC1H_PREPARED_AND_COMMITTED_BEFORE_CHECKING",
        "protocol": "HC-1H",
        "mode": mode,
        "experiment_id": experiment_id,
        "commitment_sha256": commitment_sha,
        "sealed_key_plaintext_sha256": plaintext_sha,
        "sealed_key_envelope_sha256": sha256_bytes(envelope_bytes),
        "real_population_sha256": key_document["real_population_sha256"],
        "synthetic_pool_sha256": key_document["synthetic_pool_sha256"],
        "data_class": data_class,
        "pilot_exclusion": pilot_exclusion,
        "labels_required": len(items),
        "category_counts": key_document["category_counts"],
        "stratum_populations": populations,
        "chi_tertile_cutpoints_from_real_population": list(chi_tertile_cutpoints),
        "real_allocation": real_allocation,
        "synthetic_allocation": injection_allocation,
        "checker_control_sha256": checker_control_sha256,
        "power_bound_n": HC1H_POWER_BOUND_N,
        "power_gate": str(HC1H_POWER_GATE),
        "additional_covariance": str(additional_covariance),
        "checker_package_sha256": package_descriptor["sha256"],
        "checking_started": False,
    }
    _atomic_write(
        private_root / "prepare_receipt.json",
        canonical_json_bytes(receipt) + b"\n",
        mode=0o600,
    )
    return receipt


def _contains_forbidden_key(value: object) -> bool:
    if isinstance(value, dict):
        return bool(set(value) & FORBIDDEN_CHECKER_KEYS) or any(
            _contains_forbidden_key(child) for child in value.values()
        )
    if isinstance(value, list):
        return any(_contains_forbidden_key(child) for child in value)
    return False


def load_checker_package(package_root: Path) -> dict:
    """Load only a checker capability root; reject escapes and truth-bearing fields."""
    package_path = package_root / "package.json"
    _require_regular_contained(package_path, package_root)
    package_bytes = package_path.read_bytes()
    package = json.loads(package_bytes)
    expected_package_fields = (
        HC1H_PACKAGE_FIELDS if package.get("role") == HC1H_ROLE else PACKAGE_FIELDS
    )
    if set(package) != expected_package_fields or package.get("schema_version") != SCHEMA_VERSION:
        raise HandcheckError("checker package schema mismatch")
    if package.get("role") not in (*CHECKER_ROLES, "J", HC1H_ROLE):
        raise HandcheckError("checker package role is invalid")
    if _contains_forbidden_key(package):
        raise HandcheckError("checker package contains a truth-bearing field")
    if sha256_bytes(package["instructions"].encode()) != package["instructions_sha256"]:
        raise HandcheckError("checker instruction hash mismatch")
    commitment_root = package_root.parent
    commitment_path = commitment_root / "commitment.json"
    commitment_sha_path = commitment_root / "commitment.sha256"
    _require_regular_contained(commitment_path, commitment_root)
    _require_regular_contained(commitment_sha_path, commitment_root)
    commitment_bytes = commitment_path.read_bytes()
    expected_commitment_sha = commitment_sha_path.read_text(encoding="utf-8").strip()
    if sha256_bytes(commitment_bytes) != expected_commitment_sha:
        raise HandcheckError("public commitment hash mismatch")
    commitment = json.loads(commitment_bytes)
    role = package["role"]
    if role in (*CHECKER_ROLES, HC1H_ROLE):
        descriptor = commitment["checker_packages"].get(role)
    else:
        adjudication_path = commitment_root / "adjudication_commitment.json"
        adjudication_sha_path = commitment_root / "adjudication_commitment.sha256"
        _require_regular_contained(adjudication_path, commitment_root)
        _require_regular_contained(adjudication_sha_path, commitment_root)
        adjudication_bytes = adjudication_path.read_bytes()
        adjudication_sha = adjudication_sha_path.read_text(encoding="utf-8").strip()
        if sha256_bytes(adjudication_bytes) != adjudication_sha:
            raise HandcheckError("adjudication commitment hash mismatch")
        adjudication = json.loads(adjudication_bytes)
        if adjudication["original_commitment_sha256"] != expected_commitment_sha:
            raise HandcheckError("adjudication commitment is not anchored to the original commitment")
        descriptor = adjudication.get("adjudicator_package")
    if descriptor is None or descriptor["sha256"] != sha256_bytes(package_bytes):
        raise HandcheckError("checker package is not the committed package")
    if package["key_commitment_sha256"] != commitment["sealed_key_plaintext_sha256"]:
        raise HandcheckError("package and sealed-key commitment disagree")
    seen = set()
    expected_item_fields = (
        HC1H_PACKAGE_ITEM_FIELDS
        if role == HC1H_ROLE
        else PACKAGE_ITEM_FIELDS
        if role in CHECKER_ROLES
        else ADJUDICATION_ITEM_FIELDS
    )
    for sequence, item in enumerate(package["items"]):
        if set(item) != expected_item_fields or item["sequence"] != sequence:
            raise HandcheckError("checker item schema or sequence mismatch")
        if role == "J":
            if set(item["prior_labels"]) != set(CHECKER_ROLES):
                raise HandcheckError("adjudication prior-label schema mismatch")
            if set(item["prior_labels"].values()) != {"CCW", "CW"}:
                raise HandcheckError("adjudication item is not a checker disagreement")
        if item["item_id"] in seen:
            raise HandcheckError("duplicate checker item ID")
        seen.add(item["item_id"])
        asset = package_root / item["asset"]
        _require_regular_contained(asset, package_root)
        if sha256_file(asset) != item["asset_sha256"]:
            raise HandcheckError("checker image hash mismatch")
    package["_verified_commitment_sha256"] = expected_commitment_sha
    package["_mode"] = commitment.get("mode", "legacy")
    package["_checker_control_sha256"] = commitment.get("checker_control_sha256")
    return package


def _complete_answer_map(package_root: Path) -> tuple[dict[str, int], str, str]:
    application = CheckerApplication(package_root, debounce_seconds=0.0)
    if application.completed != len(application.package["items"]):
        raise HandcheckError(f"checker {application.package['role']} session is incomplete")
    answers = {event["item_id"]: int(event["label"]) for event in application._events[1:]}
    return answers, sha256_file(application.session_path), application._events[-1]["event_hash"]


def make_adjudication_package(checking_root: Path) -> dict:
    """Commit a third-checker package containing only completed A/B disagreements."""
    adjudicator_root = checking_root / "checker_J"
    if (
        adjudicator_root.exists()
        or (checking_root / "adjudication_commitment.json").exists()
        or (checking_root / "adjudication_commitment.sha256").exists()
    ):
        raise HandcheckError("adjudication package already exists; overwrite is forbidden")
    commitment_bytes = (checking_root / "commitment.json").read_bytes()
    commitment_sha = (checking_root / "commitment.sha256").read_text(encoding="utf-8").strip()
    if sha256_bytes(commitment_bytes) != commitment_sha:
        raise HandcheckError("original commitment changed before adjudication")
    package_a = load_checker_package(checking_root / "checker_A")
    package_b = load_checker_package(checking_root / "checker_B")
    if package_a["experiment_id"] != package_b["experiment_id"]:
        raise HandcheckError("checker experiments differ")
    answer_a, session_sha_a, end_hash_a = _complete_answer_map(checking_root / "checker_A")
    answer_b, session_sha_b, end_hash_b = _complete_answer_map(checking_root / "checker_B")
    if set(answer_a) != set(answer_b):
        raise HandcheckError("checker item sets differ")
    disagreements = [item_id for item_id in answer_a if answer_a[item_id] != answer_b[item_id]]
    disagreements.sort(key=lambda item_id: sha256_bytes(f"{commitment_sha}|J|{item_id}".encode()))
    item_a = {item["item_id"]: item for item in package_a["items"]}

    assets_root = adjudicator_root / "assets"
    assets_root.mkdir(parents=True, mode=0o750)
    items = []
    for sequence, item_id in enumerate(disagreements):
        source_item = item_a[item_id]
        source_asset = checking_root / "checker_A" / source_item["asset"]
        _require_regular_contained(source_asset, checking_root / "checker_A")
        data = source_asset.read_bytes()
        if sha256_bytes(data) != source_item["asset_sha256"]:
            raise HandcheckError("checker A asset changed before adjudication")
        relative_asset = f"assets/{item_id}.png"
        _atomic_write(adjudicator_root / relative_asset, data, mode=0o640)
        label_names = {1: "CCW", -1: "CW"}
        items.append(
            {
                "sequence": sequence,
                "item_id": item_id,
                "asset": relative_asset,
                "asset_sha256": source_item["asset_sha256"],
                "prior_labels": {
                    "A": label_names[answer_a[item_id]],
                    "B": label_names[answer_b[item_id]],
                },
            }
        )
    adjudicator_instructions = (
        "This is a disagreement-only third blind check. The two prior blinded labels are shown for "
        "this item only. Classify the displayed apparent winding yourself: press C once for "
        "counter-clockwise, W once for clockwise, or P to pause. The parity key, source identity, "
        "instrument output, stratum, agreements, and all aggregates remain hidden."
    )
    package_j = {
        "schema_version": SCHEMA_VERSION,
        "experiment_id": package_a["experiment_id"],
        "role": "J",
        "instructions": adjudicator_instructions,
        "instructions_sha256": sha256_bytes(adjudicator_instructions.encode()),
        "key_commitment_sha256": package_a["key_commitment_sha256"],
        "items": items,
    }
    package_bytes = canonical_json_bytes(package_j) + b"\n"
    _atomic_write(adjudicator_root / "package.json", package_bytes, mode=0o640)
    adjudication_commitment = {
        "schema_version": SCHEMA_VERSION,
        "status": "DISAGREEMENT_SET_COMMITTED_BEFORE_ADJUDICATION",
        "created_at": utc_now(),
        "experiment_id": package_a["experiment_id"],
        "original_commitment_sha256": commitment_sha,
        "checker_session_sha256": {"A": session_sha_a, "B": session_sha_b},
        "checker_session_end_hash": {"A": end_hash_a, "B": end_hash_b},
        "disagreements": len(disagreements),
        "adjudicator_instructions_sha256": package_j["instructions_sha256"],
        "adjudicator_package": {
            "relative_path": "checker_J/package.json",
            "sha256": sha256_bytes(package_bytes),
            "items": len(items),
        },
        "visibility": "only disagreement images and the two opposing blinded labels",
    }
    adjudication_bytes = canonical_json_bytes(adjudication_commitment) + b"\n"
    adjudication_sha = sha256_bytes(adjudication_bytes)
    _atomic_write(checking_root / "adjudication_commitment.json", adjudication_bytes, mode=0o640)
    _atomic_write(
        checking_root / "adjudication_commitment.sha256",
        (adjudication_sha + "\n").encode(),
        mode=0o640,
    )
    return {
        "status": "ADJUDICATION_PACKAGE_COMMITTED",
        "experiment_id": package_a["experiment_id"],
        "disagreements": len(disagreements),
        "original_commitment_sha256": commitment_sha,
        "adjudication_commitment_sha256": adjudication_sha,
        "adjudicator_package_sha256": sha256_bytes(package_bytes),
    }


def hc5_verdict(overall_a: Decimal, stratum_rates: Mapping[str, Decimal]) -> dict:
    """Evaluate HC-5 on exact decimal values, without display rounding."""
    overall = Decimal(overall_a)
    normalized = {str(key): Decimal(value) for key, value in stratum_rates.items()}
    expected_strata = {f"{chi}{size}" for chi in range(3) for size in range(3)}
    if set(normalized) != expected_strata:
        raise HandcheckError("HC-5 requires exactly nine strata 00 through 22")
    failing_strata = sorted(key for key, value in normalized.items() if value < Decimal("0.70"))
    passed = overall >= Decimal("0.85") and not failing_strata
    return {
        "verdict": "PASS_HC5_ATTENUATION" if passed else "INCONCLUSIVE-BY-POWER",
        "overall_a_exact": str(overall),
        "overall_threshold_exact": "0.85",
        "stratum_threshold_exact": "0.70",
        "failing_strata": failing_strata,
        "decision_used_unrounded_values": True,
    }


def hc1h_verdict(
    *,
    attenuation: Decimal,
    sigma: Decimal,
    stratum_rates: Mapping[str, Decimal],
    epsilon: Decimal,
    repeat_compatible: bool,
    synthetic_diagnostics_compatible: bool,
    hc7_systematic_exposure: bool,
) -> dict:
    """Apply the accepted HC-1H gates to unrounded values."""
    rates = {str(key): Decimal(value) for key, value in stratum_rates.items()}
    if set(rates) != set(HC1H_STRATA):
        raise HandcheckError("HC-1H verdict requires exactly nine committee-state by chi strata")
    attenuation = Decimal(attenuation)
    sigma = Decimal(sigma)
    epsilon = Decimal(epsilon)
    if sigma < 0:
        raise HandcheckError("HC-1H uncertainty cannot be negative")
    lower_bound = attenuation - Decimal("1.645") * sigma
    failing_strata = sorted(key for key, value in rates.items() if value < Decimal("0.70"))
    gates = {
        "power_gate_a_lb_ge_0_7905": lower_bound >= HC1H_POWER_GATE,
        "quality_floor_a_lb_ge_0_85": lower_bound >= Decimal("0.85"),
        "all_corrected_strata_ge_0_70": not failing_strata,
        "synthetic_epsilon_le_0_05": epsilon <= Decimal("0.05"),
        "repeat_rate_compatible_2sigma": bool(repeat_compatible),
        "synthetic_strata_compatible_2sigma": bool(synthetic_diagnostics_compatible),
        "no_systematic_hc7_exposure": not bool(hc7_systematic_exposure),
    }
    return {
        "verdict": "PASS_HC1H_ATTENUATION" if all(gates.values()) else "INCONCLUSIVE-BY-POWER",
        "attenuation_exact": str(attenuation),
        "sigma_exact": str(sigma),
        "a_lower_bound_exact": str(lower_bound),
        "power_threshold_exact": str(HC1H_POWER_GATE),
        "power_bound_n": HC1H_POWER_BOUND_N,
        "quality_floor_exact": "0.85",
        "stratum_floor_exact": "0.70",
        "epsilon_ceiling_exact": "0.05",
        "failing_strata": failing_strata,
        "gates": gates,
        "decision_used_unrounded_values": True,
    }


def _wilson_score_variance(successes: int, trials: int) -> float:
    lower, upper = wilson_interval(successes, trials, confidence=0.68)
    z = NormalDist().inv_cdf(0.84)
    return ((upper - lower) / (2.0 * z)) ** 2


def hc1h_statistics(
    *,
    real_counts: Mapping[str, Mapping[str, int]],
    stratum_populations: Mapping[str, int],
    synthetic_counts: Mapping[str, Mapping[str, int]],
    repeat_nonflips: int,
    repeat_trials: int,
    hc7_systematic_exposure: bool = False,
    additional_covariance: Decimal = Decimal("0"),
) -> dict:
    """Noise-correct rates and propagate the one shared global-epsilon covariance."""
    expected = set(HC1H_STRATA)
    if set(real_counts) != expected or set(stratum_populations) != expected:
        raise HandcheckError("HC-1H real summaries require exactly nine accepted strata")
    if set(synthetic_counts) != expected:
        raise HandcheckError("HC-1H synthetic diagnostics require exactly nine strata")
    synthetic_trials = sum(int(row["trials"]) for row in synthetic_counts.values())
    synthetic_errors = sum(int(row["errors"]) for row in synthetic_counts.values())
    if synthetic_trials <= 0 or not 0 <= synthetic_errors <= synthetic_trials:
        raise HandcheckError("HC-1H synthetic counts are invalid")
    epsilon = Fraction(synthetic_errors, synthetic_trials)
    if epsilon >= Fraction(1, 2):
        raise HandcheckError("HC-1H noise correction is undefined for epsilon at or above one half")
    epsilon_variance = _wilson_score_variance(synthetic_errors, synthetic_trials)
    denominator = 1 - 2 * epsilon
    population_total = sum(int(value) for value in stratum_populations.values())
    if population_total <= 0:
        raise HandcheckError("HC-1H accepted-population total must be positive")

    attenuation = Fraction(0, 1)
    independent_raw_variance = 0.0
    shared_derivative = 0.0
    corrected_rates: dict[str, Decimal] = {}
    strata = []
    for stratum in HC1H_STRATA:
        trials = int(real_counts[stratum]["trials"])
        agreements = int(real_counts[stratum]["raw_agreements"])
        population = int(stratum_populations[stratum])
        if trials <= 0 or population <= 0 or trials > population or not 0 <= agreements <= trials:
            raise HandcheckError(f"HC-1H real count is invalid in {stratum}")
        raw = Fraction(agreements, trials)
        corrected = (raw - epsilon) / denominator
        weight = Fraction(population, population_total)
        attenuation += weight * corrected
        d_raw = float(1 / denominator)
        d_epsilon = float((2 * raw - 1) / (denominator * denominator))
        raw_variance = _wilson_score_variance(agreements, trials)
        independent_raw_variance += float(weight * weight) * d_raw * d_raw * raw_variance
        shared_derivative += float(weight) * d_epsilon
        corrected_rates[stratum] = _fraction_decimal(corrected)
        strata.append(
            {
                "stratum": stratum,
                "population_count": population,
                "population_weight_exact": f"{weight.numerator}/{weight.denominator}",
                "trials": trials,
                "raw_agreements": agreements,
                "raw_rate_exact_fraction": f"{raw.numerator}/{raw.denominator}",
                "corrected_rate_exact_fraction": f"{corrected.numerator}/{corrected.denominator}",
                "corrected_rate": float(corrected),
                "raw_wilson_variance_68": raw_variance,
                "d_corrected_d_raw": d_raw,
                "d_corrected_d_epsilon": d_epsilon,
            }
        )
    additional_covariance = Decimal(str(additional_covariance))
    if not additional_covariance.is_finite() or additional_covariance < 0:
        raise HandcheckError("additional covariance must be a finite non-negative variance term")
    shared_component = shared_derivative * shared_derivative * epsilon_variance
    total_variance = independent_raw_variance + shared_component + float(additional_covariance)
    sigma = math.sqrt(total_variance)

    synthetic_diagnostics = []
    diagnostics_compatible = True
    epsilon_float = float(epsilon)
    for stratum in HC1H_STRATA:
        trials = int(synthetic_counts[stratum]["trials"])
        errors = int(synthetic_counts[stratum]["errors"])
        if trials <= 0 or not 0 <= errors <= trials:
            raise HandcheckError(f"HC-1H synthetic count is invalid in {stratum}")
        rate = Fraction(errors, trials)
        variance = _wilson_score_variance(errors, trials)
        two_sigma = 2.0 * math.sqrt(variance + epsilon_variance)
        compatible = abs(float(rate) - epsilon_float) <= two_sigma
        diagnostics_compatible = diagnostics_compatible and compatible
        synthetic_diagnostics.append(
            {
                "stratum": stratum,
                "trials": trials,
                "errors": errors,
                "error_rate_exact_fraction": f"{rate.numerator}/{rate.denominator}",
                "compatible_with_global_epsilon_2sigma": compatible,
                "two_sigma_difference_limit": two_sigma,
            }
        )

    if repeat_trials <= 0 or not 0 <= repeat_nonflips <= repeat_trials:
        raise HandcheckError("HC-1H mirrored-repeat counts are invalid")
    repeat_rate = Fraction(repeat_nonflips, repeat_trials)
    repeat_variance = _wilson_score_variance(repeat_nonflips, repeat_trials)
    repeat_two_sigma = 2.0 * math.sqrt(repeat_variance + epsilon_variance)
    repeat_compatible = abs(float(repeat_rate) - epsilon_float) <= repeat_two_sigma
    verdict = hc1h_verdict(
        attenuation=_fraction_decimal(attenuation),
        sigma=Decimal(str(sigma)),
        stratum_rates=corrected_rates,
        epsilon=_fraction_decimal(epsilon),
        repeat_compatible=repeat_compatible,
        synthetic_diagnostics_compatible=diagnostics_compatible,
        hc7_systematic_exposure=hc7_systematic_exposure,
    )
    return {
        "epsilon_exact_fraction": f"{epsilon.numerator}/{epsilon.denominator}",
        "epsilon": epsilon_float,
        "epsilon_wilson_variance_68": epsilon_variance,
        "strata": strata,
        "synthetic_diagnostics": synthetic_diagnostics,
        "repeat_diagnostic": {
            "trials": repeat_trials,
            "nonflips": repeat_nonflips,
            "nonflip_rate_exact_fraction": f"{repeat_rate.numerator}/{repeat_rate.denominator}",
            "compatible_with_global_epsilon_2sigma": repeat_compatible,
            "two_sigma_difference_limit": repeat_two_sigma,
        },
        "attenuation_exact_fraction": f"{attenuation.numerator}/{attenuation.denominator}",
        "attenuation": float(attenuation),
        "sigma": sigma,
        "variance": {
            "convention": "Wilson-68 score variances; delta method with shared global epsilon plus a separately approved non-negative additional covariance term",
            "independent_raw_component": independent_raw_variance,
            "shared_epsilon_component": shared_component,
            "additional_covariance": float(additional_covariance),
            "additional_covariance_exact": str(additional_covariance),
            "total": total_variance,
        },
        "verdict": verdict,
    }


def wilson_interval(successes: int, trials: int, *, confidence: float = 0.68) -> tuple[float, float]:
    if trials <= 0 or successes < 0 or successes > trials:
        raise HandcheckError("Wilson interval counts are invalid")
    if not 0.0 < confidence < 1.0:
        raise HandcheckError("Wilson confidence must be between zero and one")
    z = NormalDist().inv_cdf((1.0 + confidence) / 2.0)
    p = successes / trials
    denominator = 1.0 + z * z / trials
    center = (p + z * z / (2.0 * trials)) / denominator
    half = (
        z
        * math.sqrt(p * (1.0 - p) / trials + z * z / (4.0 * trials * trials))
        / denominator
    )
    return center - half, center + half


def _summarize_strata(
    stratum_counts: Mapping[str, Mapping[str, int]],
    stratum_populations: Mapping[str, int],
) -> tuple[list[dict], Fraction, float, dict[str, Decimal]]:
    """Population-weight rates and design-based delta variance for HC-4.

    The variance convention is frozen here as binomial plug-in variance multiplied
    by the simple-random-sampling-without-replacement correction (N_h-n_h)/(N_h-1).
    A census stratum therefore contributes zero sampling variance.
    """
    expected_strata = {f"{chi}{size}" for chi in range(3) for size in range(3)}
    if set(stratum_counts) != expected_strata or set(stratum_populations) != expected_strata:
        raise HandcheckError("stratum summary requires exactly nine strata 00 through 22")
    population_total = sum(int(value) for value in stratum_populations.values())
    if population_total <= 0:
        raise HandcheckError("stratum population total must be positive")
    strata = []
    overall = Fraction(0, 1)
    variance = 0.0
    rate_decimals = {}
    for stratum in sorted(expected_strata):
        population_count = int(stratum_populations[stratum])
        sample_count = int(stratum_counts[stratum]["sample_count"])
        agreements = int(stratum_counts[stratum]["agreements"])
        if population_count <= 0 or sample_count <= 0 or sample_count > population_count:
            raise HandcheckError("stratum sample must be positive and no larger than its population")
        if agreements < 0 or agreements > sample_count:
            raise HandcheckError("stratum agreement count is invalid")
        rate = Fraction(agreements, sample_count)
        weight = Fraction(population_count, population_total)
        fpc = Fraction(population_count - sample_count, population_count - 1) if population_count > 1 else Fraction(0, 1)
        overall += weight * rate
        variance += float(weight * weight * rate * (1 - rate) * fpc / sample_count)
        lower, upper = wilson_interval(agreements, sample_count, confidence=0.68)
        rate_decimals[stratum] = _fraction_decimal(rate)
        strata.append(
            {
                "stratum": stratum,
                "population_count": population_count,
                "population_weight_exact": f"{weight.numerator}/{weight.denominator}",
                "sample_count": sample_count,
                "agreements": agreements,
                "agreement_rate_exact": f"{rate.numerator}/{rate.denominator}",
                "agreement_rate": float(rate),
                "wilson_68_lower": lower,
                "wilson_68_upper": upper,
                "finite_population_correction_exact": f"{fpc.numerator}/{fpc.denominator}",
            }
        )
    return strata, overall, math.sqrt(variance), rate_decimals


def _fraction_decimal(value: Fraction) -> Decimal:
    with localcontext() as context:
        context.prec = 60
        return Decimal(value.numerator) / Decimal(value.denominator)


def _session_started_at(application: CheckerApplication) -> datetime:
    if not application._events:
        raise HandcheckError("required checker session was never started")
    return datetime.fromisoformat(
        application._events[0]["started_at_utc"].replace("Z", "+00:00")
    )


def _hc1h_public_projection(statistics: dict) -> tuple[dict, list[dict]]:
    public_strata = []
    for row in statistics["strata"]:
        if row["trials"] < 50:
            public_strata.append(
                {"stratum": row["stratum"], "masked": True, "mask_reason": "F10_K_LT_50"}
            )
        else:
            public_strata.append({"masked": False, "mask_reason": None, **row})
    public_statistics = json.loads(
        json.dumps({key: value for key, value in statistics.items() if key != "strata"})
    )
    if any(row["masked"] for row in public_strata):
        private_verdict = public_statistics["verdict"]
        non_stratum_gates = dict(private_verdict.get("gates", {}))
        non_stratum_gates.pop("all_corrected_strata_ge_0_70", None)
        public_statistics["verdict"] = {
            "verdict": "WITHHELD_F10_MASKED_STRATA",
            "decision_public": False,
            "masked_stratum_gate_withheld": True,
            "masked_stratum_failure_identities_private": True,
            "non_stratum_gates": non_stratum_gates,
        }
    public_statistics["strata"] = public_strata
    return public_statistics, public_strata


def reduce_hc1h_experiment(
    *,
    private_root: Path,
    checking_root: Path,
    passphrase: bytes,
    private_output_root: Path,
    public_output_root: Path,
) -> dict:
    """Reduce one complete HC-1H session; pilot-only injections never enter real a."""
    for path in (private_output_root, public_output_root):
        if path.exists():
            raise HandcheckError("reduction refuses to overwrite an existing output root")
    _reject_overlapping_roots(private_output_root, public_output_root)
    for output_root in (private_output_root, public_output_root):
        for protected_root in (private_root, checking_root):
            if _is_within(output_root, protected_root) or _is_within(protected_root, output_root):
                raise HandcheckError("HC-1H reduction outputs must be disjoint from custody and checking")

    commitment_bytes = (checking_root / "commitment.json").read_bytes()
    commitment_sha = (checking_root / "commitment.sha256").read_text(encoding="utf-8").strip()
    if sha256_bytes(commitment_bytes) != commitment_sha:
        raise HandcheckError("HC-1H public commitment hash failed at reduction")
    commitment = json.loads(commitment_bytes)
    if commitment.get("protocol") != "HC-1H":
        raise HandcheckError("reduction input is not an HC-1H commitment")
    if (
        commitment.get("power_bound_n") != HC1H_POWER_BOUND_N
        or commitment.get("power_gate") != str(HC1H_POWER_GATE)
    ):
        raise HandcheckError("HC-1H power-bound N or frozen power gate changed")
    try:
        additional_covariance = Decimal(str(commitment["additional_covariance"]))
    except (KeyError, InvalidOperation) as exc:
        raise HandcheckError("the additional covariance commitment is missing or invalid") from exc
    if not additional_covariance.is_finite() or additional_covariance < 0:
        raise HandcheckError("the additional covariance commitment must be finite and non-negative")
    prepare_receipt = json.loads((private_root / "prepare_receipt.json").read_bytes())
    if prepare_receipt.get("commitment_sha256") != commitment_sha:
        raise HandcheckError("HC-1H public commitment differs from private preparation receipt")
    sealed_path = private_root / "sealed_key.nmhc"
    if sha256_file(sealed_path) != commitment["sealed_key_envelope_sha256"]:
        raise HandcheckError("HC-1H sealed envelope changed after commitment")
    if harness_source_sha256() != commitment["harness_source_sha256"]:
        raise HandcheckError("harness source changed after HC-1H checking was committed")
    if authority_hashes() != commitment["authority_sha256"]:
        raise HandcheckError("accepted HC-1H authority changed after checking was committed")

    application = CheckerApplication(
        checking_root / "checker_H",
        control_path=private_root / "checker_H_control.json",
        debounce_seconds=0.0,
    )
    state = application.public_state()
    if state["status"] == "INCONCLUSIVE_HC7_SYSTEMATIC_EXPOSURE":
        terminal_event = next(
            event["event_type"]
            for event in reversed(application._events[1:])
            if event.get("event_type")
            in {"SYSTEMATIC_EXPOSURE_HC7", "REPLACEMENT_RESERVE_EXHAUSTED_HC7"}
        )
        private_output_root.mkdir(parents=True, mode=0o700)
        public_output_root.mkdir(parents=True, mode=0o750)
        void_result = {
            "schema_version": SCHEMA_VERSION,
            "status": "HARD_INCONCLUSIVE_HC7_IDENTITY_EXPOSURE",
            "experiment_id": commitment["experiment_id"],
            "mode": commitment["mode"],
            "trigger": terminal_event,
            "sealed_key_opened": False,
            "original_commitment_sha256": commitment_sha,
            "checker_session_sha256": sha256_file(application.session_path),
            "event_published": True,
            "release_authorized": False,
        }
        void_bytes = canonical_json_bytes(void_result) + b"\n"
        _atomic_write(
            public_output_root / "hc1h_integrity_event.json", void_bytes, mode=0o640
        )
        private_void = {
            **void_result,
            "public_integrity_event_sha256": sha256_bytes(void_bytes),
        }
        _atomic_write(
            private_output_root / "hc1h_integrity_event_receipt.json",
            canonical_json_bytes(private_void) + b"\n",
            mode=0o600,
        )
        return void_result
    if application.completed != int(commitment["labels_required"]):
        raise HandcheckError("the one-human HC-1H session must be complete before unsealing")
    if commitment["mode"] == "pilot" and application._ergonomics_value() is None:
        raise HandcheckError("pilot ergonomics must be recorded in the checker UI before unsealing")
    commitment_time = datetime.fromisoformat(commitment["created_at"].replace("Z", "+00:00"))
    if _session_started_at(application) < commitment_time:
        raise HandcheckError("HC-1H checker session predates the key commitment")
    answer_events = [
        event for event in application._events[1:] if event["event_type"] == "ANSWER_RECORDED"
    ]
    answers = {event["item_id"]: int(event["label"]) for event in answer_events}
    answer_event_by_item = {event["item_id"]: event for event in answer_events}
    if len(answers) != int(commitment["labels_required"]):
        raise HandcheckError("HC-1H answer IDs are not complete and unique")

    # Custody gate: no decrypt call is reachable until the sole required label stream is complete.
    sealed = unseal_key(sealed_path, passphrase)
    sealed_plaintext_sha = sha256_bytes(canonical_json_bytes(sealed))
    if sealed_plaintext_sha != commitment["sealed_key_plaintext_sha256"]:
        raise HandcheckError("unsealed HC-1H key does not match the pre-check commitment")
    if sealed.get("protocol") != "HC-1H" or sealed["experiment_id"] != commitment["experiment_id"]:
        raise HandcheckError("unsealed HC-1H experiment does not match the commitment")
    if sealed["labels_required"] != commitment["labels_required"]:
        raise HandcheckError("unsealed HC-1H label count differs from the commitment")
    if (
        sealed.get("power_bound_n") != HC1H_POWER_BOUND_N
        or sealed.get("power_gate") != str(HC1H_POWER_GATE)
    ):
        raise HandcheckError("unsealed HC-1H power gate does not match the accepted bound")
    if sealed.get("additional_covariance") != str(additional_covariance):
        raise HandcheckError("the sealed additional covariance term does not match the commitment")
    if sealed.get("pilot_exclusion") != commitment.get("pilot_exclusion"):
        raise HandcheckError("pilot synthetic-exclusion chain differs between key and commitment")
    if sealed.get("chi_tertile_cutpoints_from_real_population") != commitment.get(
        "chi_tertile_cutpoints_from_real_population"
    ):
        raise HandcheckError("common real-population |chi| cutpoints changed after commitment")
    if sealed["data_class"] == "authorized_measurement":
        expected = {"real": 90, "synthetic": 40, "repeat": 20} if sealed["mode"] == "pilot" else {
            "real": 500,
            "synthetic": 200,
            "repeat": 150,
        }
        expected_floor = 10 if sealed["mode"] == "pilot" else 30
        if sealed["category_counts"] != expected or sealed["real_floor"] != expected_floor:
            raise HandcheckError("authorized HC-1H counts violate the accepted design")

    all_assignments = {
        row["item_id"]: row
        for row in sealed["assignments"] + sealed.get("reserve_assignments", [])
    }
    if not set(answers).issubset(all_assignments):
        raise HandcheckError("HC-1H answers contain an item absent from the sealed key")
    used = [all_assignments[item_id] for item_id in answers]
    counts_used = {
        category: sum(row["category"] == category for row in used)
        for category in ("real", "synthetic", "repeat")
    }
    if counts_used != sealed["category_counts"]:
        raise HandcheckError("HC-7 replacement did not preserve category counts")

    real_counts = {
        stratum: {"trials": 0, "raw_agreements": 0} for stratum in HC1H_STRATA
    }
    synthetic_counts = {
        stratum: {"trials": 0, "errors": 0} for stratum in HC1H_STRATA
    }
    private_rows = []
    original_sign_by_item = {}
    presented_sign_by_item = {}
    for assignment in used:
        item_id = assignment["item_id"]
        presented = answers[item_id]
        original = -presented if assignment["mirrored"] else presented
        original_sign_by_item[item_id] = original
        presented_sign_by_item[item_id] = presented
        row = {
            "item_id": item_id,
            "category": assignment["category"],
            "stratum": assignment["stratum"],
            "mirrored": bool(assignment["mirrored"]),
            "presented_human_sign": presented,
            "original_parity_human_sign": original,
            "presentation_sequence": int(answer_event_by_item[item_id]["sequence"]),
        }
        if assignment["category"] in {"real", "repeat"}:
            row["object_id"] = assignment["object_id"]
            row["instrument_sign"] = int(assignment["instrument_sign"])
        else:
            row["synthetic_id"] = assignment["synthetic_id"]
            row["truth_sign"] = int(assignment["truth_sign"])
        if assignment["category"] == "real":
            agrees = original == int(assignment["instrument_sign"])
            real_counts[assignment["stratum"]]["trials"] += 1
            real_counts[assignment["stratum"]]["raw_agreements"] += int(agrees)
            row["raw_agreement"] = agrees
        elif assignment["category"] == "synthetic":
            error = original != int(assignment["truth_sign"])
            synthetic_counts[assignment["stratum"]]["trials"] += 1
            synthetic_counts[assignment["stratum"]]["errors"] += int(error)
            row["synthetic_error"] = error
        private_rows.append(row)

    repeat_nonflips = 0
    for assignment in used:
        if assignment["category"] != "repeat":
            continue
        parent_item_id = assignment["parent_item_id"]
        if parent_item_id not in presented_sign_by_item:
            raise HandcheckError("an HC-7 replacement orphaned a mirrored repeat from its first label")
        nonflip = presented_sign_by_item[assignment["item_id"]] == presented_sign_by_item[parent_item_id]
        repeat_nonflips += int(nonflip)
        for row in private_rows:
            if row["item_id"] == assignment["item_id"]:
                row["parent_item_id"] = parent_item_id
                row["repeat_nonflip"] = nonflip
                break

    for stratum in HC1H_STRATA:
        if real_counts[stratum]["trials"] != int(sealed["real_allocation"][stratum]):
            raise HandcheckError("HC-1H realized real count differs from the sealed allocation")
        if synthetic_counts[stratum]["trials"] != int(sealed["synthetic_allocation"][stratum]):
            raise HandcheckError("HC-1H realized injection count differs from the sealed allocation")

    statistics = hc1h_statistics(
        real_counts=real_counts,
        stratum_populations=sealed["stratum_populations"],
        synthetic_counts=synthetic_counts,
        repeat_nonflips=repeat_nonflips,
        repeat_trials=counts_used["repeat"],
        additional_covariance=additional_covariance,
    )
    repeat_blocks: dict[int, dict[str, int]] = {}
    for row in private_rows:
        if row["category"] != "repeat":
            continue
        block = int(row["presentation_sequence"]) // HC1H_SESSION_PRESENTATION_LIMIT + 1
        block_counts = repeat_blocks.setdefault(block, {"trials": 0, "nonflips": 0})
        block_counts["trials"] += 1
        block_counts["nonflips"] += int(row["repeat_nonflip"])
    statistics["repeat_diagnostic"]["by_session_block"] = [
        {
            "session_block": block,
            "trials": counts["trials"],
            "nonflips": counts["nonflips"],
            "nonflip_rate_exact": f"{Fraction(counts['nonflips'], counts['trials']).numerator}/{Fraction(counts['nonflips'], counts['trials']).denominator}",
            "enters_primary_repeat_gate": False,
        }
        for block, counts in sorted(repeat_blocks.items())
    ]
    machine_committee_diagnostic = []
    for chi_tertile in range(3):
        state_counts = {
            state_name: int(sealed["stratum_populations"][f"{state_name}|{chi_tertile}"])
            for state_name in HC1H_STATES
        }
        total_population = sum(state_counts.values())
        disagree_rate = Fraction(state_counts["disagree"], total_population)
        low_confidence_rate = Fraction(state_counts["low-confidence"], total_population)
        machine_committee_diagnostic.append(
            {
                "chi_tertile": chi_tertile,
                "population_count": total_population,
                "state_counts": state_counts,
                "disagree_rate_exact": f"{disagree_rate.numerator}/{disagree_rate.denominator}",
                "disagree_rate": float(disagree_rate),
                "low_confidence_rate_exact": f"{low_confidence_rate.numerator}/{low_confidence_rate.denominator}",
                "low_confidence_rate": float(low_confidence_rate),
                "enters_attenuation": False,
            }
        )
    pilot_outcome = None
    if sealed["mode"] == "pilot":
        pilot_passed = (
            application._ergonomics_value() is True
            and Decimal(statistics["epsilon_exact_fraction"].split("/")[0])
            / Decimal(statistics["epsilon_exact_fraction"].split("/")[1])
            < Decimal("0.10")
        )
        pilot_outcome = "PASS-TO-FULL-HC1H" if pilot_passed else "INCONCLUSIVE-PILOT"
        statistics = {
            "epsilon_exact_fraction": statistics["epsilon_exact_fraction"],
            "epsilon": statistics["epsilon"],
            "epsilon_wilson_variance_68": statistics["epsilon_wilson_variance_68"],
            "synthetic_diagnostics": statistics["synthetic_diagnostics"],
            "verdict": {
                "verdict": pilot_outcome,
                "reason": "pilot evaluates execution, ergonomics, epsilon<0.10, and HC-7 only; no a or repeat statistic is produced",
            },
            "pilot_real_and_retest_values_used_for_pass": False,
        }
    private_rows.sort(
        key=lambda row: (
            row["category"],
            row.get("object_id", row.get("synthetic_id", "")),
            row["item_id"],
        )
    )
    private_bytes = b"".join(canonical_json_bytes(row) + b"\n" for row in private_rows)
    private_output_root.mkdir(parents=True, mode=0o700)
    public_output_root.mkdir(parents=True, mode=0o750)
    _atomic_write(private_output_root / "per_presentation_hc1h.jsonl", private_bytes, mode=0o600)
    private_summary = {
        "schema_version": SCHEMA_VERSION,
        "status": "HC1H_PRIVATE_REDUCTION",
        "experiment_id": sealed["experiment_id"],
        "mode": sealed["mode"],
        "counts_used": counts_used,
        "specific_hc7_flags": state["hc7_specific_flags"],
        "statistics": statistics,
        "machine_committee_diagnostic": machine_committee_diagnostic,
        "pilot_outcome": pilot_outcome,
        "publication_authorized": False,
    }
    private_summary_bytes = canonical_json_bytes(private_summary) + b"\n"
    _atomic_write(private_output_root / "hc1h_private_summary.json", private_summary_bytes, mode=0o600)

    public_strata = []
    if sealed["mode"] == "full":
        public_statistics, public_strata = _hc1h_public_projection(statistics)
    else:
        public_statistics = statistics
    public_result = {
        "schema_version": SCHEMA_VERSION,
        "status": "HC1H_PILOT_REDUCED" if sealed["mode"] == "pilot" else "HC1H_AGGREGATES_REDUCED",
        "scope": (
            "pilot integrity and epsilon diagnostics only; no attenuation or repeat statistic"
            if sealed["mode"] == "pilot"
            else "aggregate HC-1H output only; F-10 masks real strata with k<50"
        ),
        "experiment_id": sealed["experiment_id"],
        "mode": sealed["mode"],
        "counts_used": counts_used,
        "specific_hc7_flags_replaced": state["hc7_specific_flags"],
        "statistics": public_statistics,
        "machine_committee_diagnostic": machine_committee_diagnostic,
        "pilot_outcome": pilot_outcome,
        "commitments": {
            "sealed_key_plaintext_sha256": sealed_plaintext_sha,
            "sealed_key_envelope_sha256": sha256_file(sealed_path),
            "original_commitment_sha256": commitment_sha,
            "checker_session_sha256": sha256_file(application.session_path),
            "private_presentation_table_sha256": sha256_bytes(private_bytes),
            "private_summary_sha256": sha256_bytes(private_summary_bytes),
        },
        "boundaries": {
            "per_object_table_published": False,
            "pilot_synthetics_count_toward_full": False,
            "release_authorized": False,
            "hc6_power_evaluated": False,
        },
    }
    public_json = canonical_json_bytes(public_result) + b"\n"
    _atomic_write(public_output_root / "hc1h_aggregates.json", public_json, mode=0o640)
    csv_buffer = io.StringIO(newline="")
    fields = [
        "stratum",
        "masked",
        "mask_reason",
        "population_count",
        "population_weight_exact",
        "trials",
        "raw_agreements",
        "raw_rate_exact_fraction",
        "raw_rate",
        "corrected_rate_exact_fraction",
        "corrected_rate",
        "corrected_variance",
    ]
    writer = csv.DictWriter(csv_buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for row in public_strata:
        writer.writerow({field: row.get(field, "") for field in fields})
    public_csv = csv_buffer.getvalue().encode("utf-8")
    _atomic_write(public_output_root / "hc1h_aggregates.csv", public_csv, mode=0o640)
    private_receipt = {
        "schema_version": SCHEMA_VERSION,
        "status": "HC1H_PRIVATE_REDUCTION_SEALED",
        "experiment_id": sealed["experiment_id"],
        "private_rows": len(private_rows),
        "private_presentation_table_sha256": sha256_bytes(private_bytes),
        "private_summary_sha256": sha256_bytes(private_summary_bytes),
        "public_aggregate_json_sha256": sha256_bytes(public_json),
        "public_aggregate_csv_sha256": sha256_bytes(public_csv),
    }
    _atomic_write(
        private_output_root / "unseal_receipt.json",
        canonical_json_bytes(private_receipt) + b"\n",
        mode=0o600,
    )
    return public_result


def reduce_experiment(
    *,
    private_root: Path,
    checking_root: Path,
    passphrase: bytes,
    private_output_root: Path,
    public_output_root: Path,
) -> dict:
    """Unseal after all labels, then emit separate private rows and public aggregates."""
    for path in (private_output_root, public_output_root):
        if path.exists():
            raise HandcheckError("reduction refuses to overwrite an existing output root")
    _reject_overlapping_roots(private_output_root, public_output_root)
    if _is_within(public_output_root, private_root) or _is_within(private_root, public_output_root):
        raise HandcheckError("public output cannot overlap sealed-key custody")
    if _is_within(public_output_root, checking_root) or _is_within(checking_root, public_output_root):
        raise HandcheckError("public output cannot overlap checking sessions")
    if _is_within(private_output_root, checking_root) or _is_within(
        checking_root, private_output_root
    ):
        raise HandcheckError("private reduction output cannot overlap checking capabilities")

    commitment_path = checking_root / "commitment.json"
    commitment_sha_path = checking_root / "commitment.sha256"
    commitment_bytes = commitment_path.read_bytes()
    commitment_sha = commitment_sha_path.read_text(encoding="utf-8").strip()
    if sha256_bytes(commitment_bytes) != commitment_sha:
        raise HandcheckError("original commitment hash failed at reduction")
    commitment = json.loads(commitment_bytes)
    prepare_receipt_path = private_root / "prepare_receipt.json"
    _require_regular_contained(prepare_receipt_path, private_root)
    prepare_receipt = json.loads(prepare_receipt_path.read_bytes())
    if prepare_receipt.get("commitment_sha256") != commitment_sha:
        raise HandcheckError("public commitment differs from the private preparation receipt")
    sealed_path = private_root / "sealed_key.nmhc"
    if sha256_file(sealed_path) != commitment["sealed_key_envelope_sha256"]:
        raise HandcheckError("sealed envelope bytes changed after commitment")
    if prepare_receipt.get("sealed_key_envelope_sha256") != commitment["sealed_key_envelope_sha256"]:
        raise HandcheckError("sealed envelope differs from the private preparation receipt")
    if harness_source_sha256() != commitment["harness_source_sha256"]:
        raise HandcheckError("harness source changed after checking was committed")
    if authority_hashes() != commitment["authority_sha256"]:
        raise HandcheckError("protocol authority changed after checking was committed")

    app_a = CheckerApplication(checking_root / "checker_A", debounce_seconds=0.0)
    app_b = CheckerApplication(checking_root / "checker_B", debounce_seconds=0.0)
    if app_a.completed != commitment["sample_size"] or app_b.completed != commitment["sample_size"]:
        raise HandcheckError("both independent checker sessions must be complete before unsealing")
    commitment_time = datetime.fromisoformat(commitment["created_at"].replace("Z", "+00:00"))
    if _session_started_at(app_a) < commitment_time or _session_started_at(app_b) < commitment_time:
        raise HandcheckError("a checker session predates the sealed-key commitment")
    answers_a = {event["item_id"]: int(event["label"]) for event in app_a._events[1:]}
    answers_b = {event["item_id"]: int(event["label"]) for event in app_b._events[1:]}
    if set(answers_a) != set(answers_b):
        raise HandcheckError("checker item sets differ at reduction")

    adjudication_path = checking_root / "adjudication_commitment.json"
    adjudication_sha_path = checking_root / "adjudication_commitment.sha256"
    adjudication_bytes = adjudication_path.read_bytes()
    adjudication_sha = adjudication_sha_path.read_text(encoding="utf-8").strip()
    if sha256_bytes(adjudication_bytes) != adjudication_sha:
        raise HandcheckError("adjudication commitment hash failed")
    adjudication = json.loads(adjudication_bytes)
    if adjudication["original_commitment_sha256"] != commitment_sha:
        raise HandcheckError("adjudication is not anchored to the original commitment")
    current_session_sha = {
        "A": sha256_file(app_a.session_path),
        "B": sha256_file(app_b.session_path),
    }
    current_session_end = {
        "A": app_a._events[-1]["event_hash"],
        "B": app_b._events[-1]["event_hash"],
    }
    if current_session_sha != adjudication["checker_session_sha256"]:
        raise HandcheckError("checker session bytes changed after disagreement commitment")
    if current_session_end != adjudication["checker_session_end_hash"]:
        raise HandcheckError("checker session end hash changed after disagreement commitment")
    disagreement_ids = {item_id for item_id in answers_a if answers_a[item_id] != answers_b[item_id]}
    if len(disagreement_ids) != adjudication["disagreements"]:
        raise HandcheckError("recomputed disagreement count does not match commitment")

    app_j = CheckerApplication(checking_root / "checker_J", debounce_seconds=0.0)
    if app_j.completed != len(disagreement_ids):
        raise HandcheckError("adjudicator must finish every disagreement before reduction")
    answers_j = {event["item_id"]: int(event["label"]) for event in app_j._events[1:]}
    if set(answers_j) != disagreement_ids:
        raise HandcheckError("adjudicator item set does not equal the disagreement set")
    if disagreement_ids and _session_started_at(app_j) < datetime.fromisoformat(
        adjudication["created_at"].replace("Z", "+00:00")
    ):
        raise HandcheckError("adjudication session predates its disagreement commitment")

    # HC-2 custody gate: no decrypt call is reachable until A, B, and every required
    # adjudicator label have been verified complete against their public commitments.
    sealed_document = unseal_key(sealed_path, passphrase)
    sealed_plaintext_sha = sha256_bytes(canonical_json_bytes(sealed_document))
    if sealed_plaintext_sha != commitment["sealed_key_plaintext_sha256"]:
        raise HandcheckError("unsealed key does not match the pre-check commitment")
    if sealed_document["experiment_id"] != commitment["experiment_id"]:
        raise HandcheckError("unsealed experiment does not match commitment")
    if sealed_document["sample_size"] != commitment["sample_size"]:
        raise HandcheckError("unsealed sample size does not match commitment")
    if sealed_document["data_class"] != commitment["data_class"]:
        raise HandcheckError("unsealed data class does not match commitment")
    if sealed_document["data_class"] == "authorized_measurement" and (
        sealed_document["sample_size"] != 500 or sealed_document["floor"] != 40
    ):
        raise HandcheckError("authorized measurement violated frozen total=500 or floor=40")
    if sealed_document["harness_source_sha256"] != commitment["harness_source_sha256"]:
        raise HandcheckError("sealed and public harness-source commitments differ")
    if sealed_document["authority_sha256"] != commitment["authority_sha256"]:
        raise HandcheckError("sealed and public authority commitments differ")

    assignments = {row["item_id"]: row for row in sealed_document["assignments"]}
    if set(assignments) != set(answers_a):
        raise HandcheckError("sealed assignment set does not equal checker item set")
    private_rows = []
    stratum_counts = {
        stratum: {"sample_count": 0, "agreements": 0}
        for stratum in sorted(sealed_document["stratum_populations"])
    }
    for assignment in sorted(assignments.values(), key=lambda row: row["object_id"]):
        item_id = assignment["item_id"]
        label_a = answers_a[item_id]
        label_b = answers_b[item_id]
        if label_a == label_b:
            presented_final = label_a
            adjudicator_label = None
        else:
            presented_final = answers_j[item_id]
            adjudicator_label = answers_j[item_id]
        original_human_sign = -presented_final if assignment["mirrored"] else presented_final
        agrees = original_human_sign == int(assignment["instrument_sign"])
        stratum = assignment["stratum"]
        stratum_counts[stratum]["sample_count"] += 1
        stratum_counts[stratum]["agreements"] += int(agrees)
        private_rows.append(
            {
                "item_id": item_id,
                "object_id": assignment["object_id"],
                "stratum": stratum,
                "mirrored": bool(assignment["mirrored"]),
                "instrument_sign": int(assignment["instrument_sign"]),
                "checker_a_presented_sign": label_a,
                "checker_b_presented_sign": label_b,
                "adjudicator_presented_sign": adjudicator_label,
                "final_presented_sign": presented_final,
                "final_original_parity_human_sign": original_human_sign,
                "agreement": bool(agrees),
            }
        )

    private_bytes = b"".join(canonical_json_bytes(row) + b"\n" for row in private_rows)
    private_table_sha = sha256_bytes(private_bytes)
    for stratum in sorted(stratum_counts):
        sample_count = stratum_counts[stratum]["sample_count"]
        if sample_count != int(sealed_document["stratum_allocation"][stratum]):
            raise HandcheckError("stratum sample count does not match sealed allocation")
    strata, overall, sigma_a, rate_decimals = _summarize_strata(
        stratum_counts,
        sealed_document["stratum_populations"],
    )
    overall_decimal = _fraction_decimal(overall)
    private_hc5 = hc5_verdict(overall_decimal, rate_decimals)
    public_hc5 = {key: value for key, value in private_hc5.items() if key != "failing_strata"}
    public_hc5["stratum_failure_details_private"] = True
    two_a_minus_one = 2 * overall - 1
    adjudicator_session_sha = (
        sha256_file(app_j.session_path) if disagreement_ids else "NONE_NO_DISAGREEMENTS"
    )

    private_output_root.mkdir(parents=True, mode=0o700)
    public_output_root.mkdir(parents=True, mode=0o750)
    _atomic_write(private_output_root / "per_object_handcheck.jsonl", private_bytes, mode=0o600)
    private_aggregate_document = {
        "schema_version": SCHEMA_VERSION,
        "status": "PRIVATE_UNMASKED_STRATUM_AGGREGATES",
        "experiment_id": sealed_document["experiment_id"],
        "strata": strata,
        "attenuation_a_exact_fraction": f"{overall.numerator}/{overall.denominator}",
        "variance_convention": "binomial plug-in times SRSWOR FPC (N_h-n_h)/(N_h-1)",
        "hc5": private_hc5,
        "publication_authorized": False,
    }
    private_aggregate_bytes = canonical_json_bytes(private_aggregate_document) + b"\n"
    _atomic_write(
        private_output_root / "stratum_aggregates_private.json",
        private_aggregate_bytes,
        mode=0o600,
    )
    public_strata = []
    for row in strata:
        if row["sample_count"] < 50:
            public_strata.append(
                {
                    "stratum": row["stratum"],
                    "masked": True,
                    "mask_reason": "F10_K_LT_50",
                }
            )
        else:
            public_strata.append({"masked": False, "mask_reason": None, **row})
    public_result = {
        "schema_version": SCHEMA_VERSION,
        "status": "HANDCHECK_AGGREGATES_REDUCED",
        "scope": "nine aggregate rows with F-10 k<50 masking; no source IDs, item IDs, coordinates, parity bits, or labels",
        "experiment_id": sealed_document["experiment_id"],
        "sample_size": sealed_document["sample_size"],
        "disagreements_adjudicated": len(disagreement_ids),
        "strata": public_strata,
        "attenuation": {
            "weighting": "accepted-population stratum fractions",
            "variance_convention": "binomial plug-in times SRSWOR FPC (N_h-n_h)/(N_h-1)",
            "a_exact_fraction": f"{overall.numerator}/{overall.denominator}",
            "a": float(overall),
            "sigma_a_delta": sigma_a,
            "two_a_minus_one_exact_fraction": f"{two_a_minus_one.numerator}/{two_a_minus_one.denominator}",
            "two_a_minus_one": float(two_a_minus_one),
            "sigma_two_a_minus_one": 2.0 * sigma_a,
        },
        "hc5": public_hc5,
        "commitments": {
            "sealed_key_plaintext_sha256": sealed_plaintext_sha,
            "sealed_key_envelope_sha256": sha256_file(sealed_path),
            "original_commitment_sha256": commitment_sha,
            "adjudication_commitment_sha256": adjudication_sha,
            "checker_session_sha256": current_session_sha,
            "adjudicator_session_sha256": adjudicator_session_sha,
            "private_handcheck_table_sha256": private_table_sha,
            "private_stratum_aggregates_sha256": sha256_bytes(private_aggregate_bytes),
        },
        "boundaries": {
            "per_object_table_published": False,
            "sealed_key_published": False,
            "release_authorized": False,
            "hc6_power_evaluated": False,
        },
    }
    public_json = canonical_json_bytes(public_result) + b"\n"
    _atomic_write(public_output_root / "handcheck_aggregates.json", public_json, mode=0o640)
    csv_buffer = io.StringIO(newline="")
    fieldnames = [
        "stratum",
        "masked",
        "mask_reason",
        "population_count",
        "population_weight_exact",
        "sample_count",
        "agreements",
        "agreement_rate_exact",
        "agreement_rate",
        "wilson_68_lower",
        "wilson_68_upper",
        "finite_population_correction_exact",
    ]
    writer = csv.DictWriter(csv_buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for row in public_strata:
        writer.writerow({field: row.get(field, "") for field in fieldnames})
    public_csv = csv_buffer.getvalue().encode("utf-8")
    _atomic_write(public_output_root / "handcheck_aggregates.csv", public_csv, mode=0o640)
    private_receipt = {
        "schema_version": SCHEMA_VERSION,
        "status": "PRIVATE_HANDCHECK_REDUCTION_SEALED",
        "experiment_id": sealed_document["experiment_id"],
        "private_handcheck_table_sha256": private_table_sha,
        "private_stratum_aggregates_sha256": sha256_bytes(private_aggregate_bytes),
        "private_rows": len(private_rows),
        "sealed_key_plaintext_sha256": sealed_plaintext_sha,
        "public_aggregate_json_sha256": sha256_bytes(public_json),
        "public_aggregate_csv_sha256": sha256_bytes(public_csv),
        "public_output_root_is_disjoint": True,
    }
    _atomic_write(
        private_output_root / "unseal_receipt.json",
        canonical_json_bytes(private_receipt) + b"\n",
        mode=0o600,
    )
    return public_result


def _event_with_hash(payload: dict, mac_key: bytes | None = None) -> dict:
    event = dict(payload)
    payload_bytes = canonical_json_bytes(payload)
    event["event_hash"] = (
        hmac.new(mac_key, payload_bytes, hashlib.sha256).hexdigest()
        if mac_key is not None
        else sha256_bytes(payload_bytes)
    )
    return event


def _validate_event_hash(event: dict, mac_key: bytes | None = None) -> None:
    supplied = event.get("event_hash")
    payload = dict(event)
    payload.pop("event_hash", None)
    expected = _event_with_hash(payload, mac_key)["event_hash"]
    if not isinstance(supplied, str) or not hmac.compare_digest(supplied, expected):
        raise HandcheckError("session event hash mismatch")


class CheckerApplication:
    """Capability-limited checker state with no key, truth, peer, or aggregate input."""

    def __init__(
        self,
        package_root: Path,
        *,
        control_path: Path | None = None,
        debounce_seconds: float = 0.35,
    ):
        self.package_root = package_root.resolve()
        self.package = load_checker_package(self.package_root)
        self._event_mac_key: bytes | None = None
        if self.package["role"] == HC1H_ROLE:
            if control_path is None or control_path.is_symlink() or not control_path.is_file():
                raise HandcheckError("HC-1H checker server requires its private control file")
            control_bytes = control_path.read_bytes()
            if sha256_bytes(control_bytes) != self.package["_checker_control_sha256"]:
                raise HandcheckError("HC-1H checker control does not match the public commitment")
            control = json.loads(control_bytes)
            if (
                set(control) != HC1H_CONTROL_FIELDS
                or control["schema_version"] != SCHEMA_VERSION
                or control["experiment_id"] != self.package["experiment_id"]
                or control["role"] != HC1H_ROLE
            ):
                raise HandcheckError("HC-1H checker control schema or identity mismatch")
            try:
                self._event_mac_key = bytes.fromhex(control["session_mac_key_hex"])
            except (TypeError, ValueError) as error:
                raise HandcheckError("HC-1H session MAC key is invalid") from error
            if len(self._event_mac_key) != 32:
                raise HandcheckError("HC-1H session MAC key must be 256 bits")
            control_items = {item["item_id"]: item for item in control["items"]}
            if len(control_items) != len(self.package["items"]):
                raise HandcheckError("HC-1H control item set does not close")
            for item in self.package["items"]:
                metadata = control_items.get(item["item_id"])
                if metadata is None or set(metadata) != HC1H_CONTROL_ITEM_FIELDS:
                    raise HandcheckError("HC-1H control item schema mismatch")
                item.update({key: value for key, value in metadata.items() if key != "item_id"})
            seen = {item["item_id"] for item in self.package["items"]}
            for group_id, reserves in control["replacement_groups"].items():
                if not isinstance(group_id, str) or not group_id or not isinstance(reserves, list):
                    raise HandcheckError("HC-7 private replacement-group schema mismatch")
                for item in reserves:
                    if set(item) != PACKAGE_ITEM_FIELDS | (HC1H_CONTROL_ITEM_FIELDS - {"item_id"}):
                        raise HandcheckError("HC-7 private replacement item schema mismatch")
                    if item["replacement_group"] != group_id or item["item_id"] in seen:
                        raise HandcheckError("HC-7 private replacement identity mismatch")
                    seen.add(item["item_id"])
                    asset = self.package_root / item["asset"]
                    _require_regular_contained(asset, self.package_root)
                    if sha256_file(asset) != item["asset_sha256"]:
                        raise HandcheckError("HC-7 private replacement image hash mismatch")
            self.package["replacement_groups"] = control["replacement_groups"]
        self.session_path = self.package_root / "answers.jsonl"
        self.debounce_seconds = float(debounce_seconds)
        if self.debounce_seconds < 0.0:
            raise HandcheckError("debounce interval cannot be negative")
        self._last_recorded_monotonic: float | None = None
        self._events = self._load_events()
        self._session_snapshot_size = self.session_path.stat().st_size if self.session_path.exists() else 0
        self._session_snapshot_sha256 = (
            sha256_file(self.session_path) if self.session_path.exists() else sha256_bytes(b"")
        )

    def _hc1h_flag_transition(
        self,
        queue: list[dict],
        cursor: int,
        reserve_queues: dict[str, list[dict]],
        flagged_item_ids: set[str],
    ) -> None:
        current = queue[cursor]

        def take(group_id: str) -> dict:
            candidates = reserve_queues.get(group_id, [])
            while candidates:
                candidate = candidates.pop(0)
                anchor = candidate["parent_anchor_item_id"]
                if anchor is None or anchor not in flagged_item_ids | {current["item_id"]}:
                    return candidate
            raise HandcheckError("HC-7 replacement reserve exhausted")

        queue.append(take(current["replacement_group"]))
        flagged_item_ids.add(current["item_id"])
        dependent_indices = [
            index
            for index in range(cursor + 1, len(queue) - 1)
            if queue[index]["parent_anchor_item_id"] == current["item_id"]
        ]
        dependents = [queue[index] for index in dependent_indices]
        for index in reversed(dependent_indices):
            queue.pop(index)
        for dependent in dependents:
            queue.append(take(dependent["replacement_group"]))

    def _load_events(self) -> list[dict]:
        if not self.session_path.exists():
            return []
        _require_regular_contained(self.session_path, self.package_root)
        raw_lines = self.session_path.read_text(encoding="utf-8").splitlines()
        if not raw_lines:
            raise HandcheckError("session file exists but has no header")
        try:
            events = [json.loads(line) for line in raw_lines]
        except Exception as error:
            raise HandcheckError("session contains a partial or invalid JSON line") from error
        header = events[0]
        _validate_event_hash(header, self._event_mac_key)
        required_header = {
            "schema_version",
            "event_type",
            "experiment_id",
            "role",
            "package_sha256",
            "commitment_sha256",
            "started_at_utc",
            "previous_hash",
            "event_hash",
        }
        if set(header) != required_header or header["event_type"] != "SESSION_STARTED":
            raise HandcheckError("session header schema mismatch")
        if header["schema_version"] != SCHEMA_VERSION:
            raise HandcheckError("session schema mismatch")
        if header["experiment_id"] != self.package["experiment_id"] or header["role"] != self.package["role"]:
            raise HandcheckError("session identity does not match package")
        if header["previous_hash"] != "0" * 64:
            raise HandcheckError("session header chain does not start at zero")
        package_hash = sha256_file(self.package_root / "package.json")
        if header["package_sha256"] != package_hash:
            raise HandcheckError("session package hash mismatch")
        if header["commitment_sha256"] != self.package["_verified_commitment_sha256"]:
            raise HandcheckError("session commitment mismatch")

        previous_hash = header["event_hash"]
        if self.package["role"] == HC1H_ROLE:
            queue = list(self.package["items"])
            reserve_queues = {
                key: list(value) for key, value in self.package["replacement_groups"].items()
            }
            cursor = 0
            systematic_exposure = False
            ergonomics_recorded = False
            flagged_item_ids: set[str] = set()
            presentations_since_break = 0
            for event in events[1:]:
                _validate_event_hash(event, self._event_mac_key)
                if event["previous_hash"] != previous_hash:
                    raise HandcheckError("session hash chain is broken")
                if systematic_exposure:
                    raise HandcheckError("session continued after systematic HC-7 exposure")
                if event["event_type"] == "ERGONOMICS_RECORDED":
                    required = {
                        "schema_version",
                        "event_type",
                        "sequence",
                        "item_id",
                        "acceptable",
                        "recorded_at_utc",
                        "previous_hash",
                        "event_hash",
                    }
                    if (
                        self.package["_mode"] != "pilot"
                        or cursor != len(queue)
                        or ergonomics_recorded
                        or set(event) != required
                        or event["sequence"] != cursor
                        or event["item_id"] != "NONE_SESSION_ERGONOMICS"
                        or not isinstance(event["acceptable"], bool)
                    ):
                        raise HandcheckError("HC-1H pilot ergonomics event schema or timing mismatch")
                    datetime.fromisoformat(event["recorded_at_utc"].replace("Z", "+00:00"))
                    ergonomics_recorded = True
                    previous_hash = event["event_hash"]
                    continue
                if event["event_type"] == "BREAK_ACKNOWLEDGED":
                    required = {
                        "schema_version",
                        "event_type",
                        "sequence",
                        "item_id",
                        "recorded_at_utc",
                        "previous_hash",
                        "event_hash",
                    }
                    if (
                        set(event) != required
                        or cursor >= len(queue)
                        or presentations_since_break != HC1H_SESSION_PRESENTATION_LIMIT
                        or event["sequence"] != cursor
                        or event["item_id"] != "NONE_SESSION_BREAK"
                    ):
                        raise HandcheckError("HC-1H break acknowledgement schema or timing mismatch")
                    datetime.fromisoformat(event["recorded_at_utc"].replace("Z", "+00:00"))
                    presentations_since_break = 0
                    previous_hash = event["event_hash"]
                    continue
                if cursor >= len(queue):
                    raise HandcheckError("HC-1H session contains more events than its active stream")
                if presentations_since_break >= HC1H_SESSION_PRESENTATION_LIMIT:
                    raise HandcheckError("HC-1H requires a logged break after 50 presentations")
                item = queue[cursor]
                common = {
                    "schema_version",
                    "event_type",
                    "sequence",
                    "item_id",
                    "recorded_at_utc",
                    "previous_hash",
                    "event_hash",
                }
                if event["event_type"] == "ANSWER_RECORDED":
                    if set(event) != common | {"label"} or event["label"] not in (-1, 1):
                        raise HandcheckError("HC-1H answer event schema mismatch")
                elif event["event_type"] == "ITEM_FLAGGED_HC7":
                    if set(event) != common:
                        raise HandcheckError("HC-7 specific-item event schema mismatch")
                    self._hc1h_flag_transition(
                        queue, cursor, reserve_queues, flagged_item_ids
                    )
                elif event["event_type"] in {
                    "SYSTEMATIC_EXPOSURE_HC7",
                    "REPLACEMENT_RESERVE_EXHAUSTED_HC7",
                }:
                    if set(event) != common:
                        raise HandcheckError("HC-7 systematic-exposure event schema mismatch")
                    systematic_exposure = True
                else:
                    raise HandcheckError("HC-1H session event type is invalid")
                if event["sequence"] != cursor or event["item_id"] != item["item_id"]:
                    raise HandcheckError("HC-1H event does not match the active blinded item")
                datetime.fromisoformat(event["recorded_at_utc"].replace("Z", "+00:00"))
                if not systematic_exposure:
                    cursor += 1
                    presentations_since_break += 1
                previous_hash = event["event_hash"]
            return events

        answers = []
        for event in events[1:]:
            _validate_event_hash(event, self._event_mac_key)
            required_answer = {
                "schema_version",
                "event_type",
                "sequence",
                "item_id",
                "label",
                "recorded_at_utc",
                "previous_hash",
                "event_hash",
            }
            if set(event) != required_answer or event["event_type"] != "ANSWER_RECORDED":
                raise HandcheckError("answer event schema mismatch")
            if event["previous_hash"] != previous_hash:
                raise HandcheckError("session hash chain is broken")
            sequence = len(answers)
            if event["sequence"] != sequence:
                raise HandcheckError("answer sequence is not append-only")
            if sequence >= len(self.package["items"]):
                raise HandcheckError("session contains more answers than package items")
            if event["item_id"] != self.package["items"][sequence]["item_id"]:
                raise HandcheckError("answer item does not match committed checker order")
            if event["label"] not in (-1, 1):
                raise HandcheckError("answer label is invalid")
            datetime.fromisoformat(event["recorded_at_utc"].replace("Z", "+00:00"))
            answers.append(event)
            previous_hash = event["event_hash"]
        return events

    @property
    def completed(self) -> int:
        if self.package["role"] == HC1H_ROLE:
            return sum(event.get("event_type") == "ANSWER_RECORDED" for event in self._events[1:])
        return max(0, len(self._events) - 1)

    def _hc1h_runtime(self) -> tuple[list[dict], int, dict[str, list[dict]], bool, int]:
        queue = list(self.package["items"])
        reserves = {key: list(value) for key, value in self.package["replacement_groups"].items()}
        cursor = 0
        systematic = False
        flags = 0
        flagged_item_ids: set[str] = set()
        for event in self._events[1:]:
            if event["event_type"] in {"ERGONOMICS_RECORDED", "BREAK_ACKNOWLEDGED"}:
                continue
            item = queue[cursor]
            if event["event_type"] == "ITEM_FLAGGED_HC7":
                self._hc1h_flag_transition(queue, cursor, reserves, flagged_item_ids)
                flags += 1
                cursor += 1
            elif event["event_type"] in {
                "SYSTEMATIC_EXPOSURE_HC7",
                "REPLACEMENT_RESERVE_EXHAUSTED_HC7",
            }:
                systematic = True
            else:
                cursor += 1
        return queue, cursor, reserves, systematic, flags

    def _presentations_since_break(self) -> int:
        count = 0
        for event in reversed(self._events[1:]):
            if event.get("event_type") == "BREAK_ACKNOWLEDGED":
                break
            if event.get("event_type") in {"ANSWER_RECORDED", "ITEM_FLAGGED_HC7"}:
                count += 1
        return count

    def _ergonomics_value(self) -> bool | None:
        values = [
            bool(event["acceptable"])
            for event in self._events[1:]
            if event.get("event_type") == "ERGONOMICS_RECORDED"
        ]
        return values[0] if values else None

    def _previous_hash(self) -> str:
        return self._events[-1]["event_hash"] if self._events else "0" * 64

    def _presentation_token(self) -> str | None:
        if self.package["role"] == HC1H_ROLE:
            queue, cursor, _reserves, systematic, _flags = self._hc1h_runtime()
            if (
                systematic
                or self.completed >= len(self.package["items"])
                or self._presentations_since_break() >= HC1H_SESSION_PRESENTATION_LIMIT
            ):
                return None
            item = queue[cursor]
            payload = (
                f"{self.package['_verified_commitment_sha256']}|{HC1H_ROLE}|{cursor}|"
                f"{item['item_id']}|{self._previous_hash()}"
            ).encode("utf-8")
            return sha256_bytes(payload)
        if self.completed >= len(self.package["items"]):
            return None
        item = self.package["items"][self.completed]
        payload = (
            f"{self.package['_verified_commitment_sha256']}|{self.package['role']}|"
            f"{self.completed}|{item['item_id']}|{self._previous_hash()}"
        ).encode("utf-8")
        return sha256_bytes(payload)

    def public_state(self) -> dict:
        total = len(self.package["items"])
        if self.package["role"] == HC1H_ROLE:
            _queue, _cursor, _reserves, systematic, flags = self._hc1h_runtime()
            status = (
                "INCONCLUSIVE_HC7_SYSTEMATIC_EXPOSURE"
                if systematic
                else "AWAITING_ERGONOMICS"
                if self.package["_mode"] == "pilot"
                and self.completed == total
                and self._ergonomics_value() is None
                else "COMPLETE"
                if self.completed == total
                else "BREAK_REQUIRED"
                if self._presentations_since_break() >= HC1H_SESSION_PRESENTATION_LIMIT
                else "ACTIVE"
            )
            token = self._presentation_token()
            return {
                "status": status,
                "role": HC1H_ROLE,
                "instructions": self.package["instructions"],
                "progress": {"completed": self.completed, "total": total},
                "hc7_specific_flags": flags,
                "ergonomics_acceptable": self._ergonomics_value(),
                "presentation_token": token,
                "asset_url": f"/asset?token={token}" if token else None,
                "allowed_keys": {
                    "C": "CCW",
                    "W": "CW",
                    "F": "Flag suspected synthetic/repeat exposure",
                    "X": "Systematic synthetic/repeat exposure",
                    "P": "Acknowledge required break / pause",
                },
            }
        if self.completed == total:
            state = {
                "status": "COMPLETE",
                "role": self.package["role"],
                "instructions": self.package["instructions"],
                "progress": {"completed": total, "total": total},
                "presentation_token": None,
                "asset_url": None,
                "allowed_keys": {"C": "CCW", "W": "CW", "P": "PAUSE"},
            }
            return state
        token = self._presentation_token()
        state = {
            "status": "ACTIVE",
            "role": self.package["role"],
            "instructions": self.package["instructions"],
            "progress": {"completed": self.completed, "total": total},
            "presentation_token": token,
            "asset_url": f"/asset?token={token}",
            "allowed_keys": {"C": "CCW", "W": "CW", "P": "PAUSE"},
        }
        if self.package["role"] == "J":
            state["prior_labels"] = self.package["items"][self.completed]["prior_labels"]
        return state

    def current_asset(self, presentation_token: str) -> tuple[bytes, str]:
        if presentation_token != self._presentation_token() or self.completed >= len(self.package["items"]):
            raise HandcheckError("stale or invalid presentation token")
        if self.package["role"] == HC1H_ROLE:
            queue, cursor, _reserves, systematic, _flags = self._hc1h_runtime()
            if systematic:
                raise HandcheckError("HC-7 systematic exposure terminated the session")
            item = queue[cursor]
        else:
            item = self.package["items"][self.completed]
        asset = self.package_root / item["asset"]
        _require_regular_contained(asset, self.package_root)
        data = asset.read_bytes()
        if sha256_bytes(data) != item["asset_sha256"]:
            raise HandcheckError("current checker asset hash mismatch")
        return data, "image/png"

    def _append_answer(self, answer: dict) -> None:
        flags = os.O_WRONLY | os.O_APPEND | os.O_CREAT
        descriptor = os.open(self.session_path, flags, 0o600)
        try:
            with os.fdopen(descriptor, "a", encoding="utf-8", closefd=False) as handle:
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
                current_size = os.fstat(handle.fileno()).st_size
                current_sha256 = sha256_file(self.session_path)
                if (
                    current_size != self._session_snapshot_size
                    or current_sha256 != self._session_snapshot_sha256
                ):
                    raise HandcheckError("session changed concurrently; reopen before answering")
                lines = []
                if not self._events:
                    header_payload = {
                        "schema_version": SCHEMA_VERSION,
                        "event_type": "SESSION_STARTED",
                        "experiment_id": self.package["experiment_id"],
                        "role": self.package["role"],
                        "package_sha256": sha256_file(self.package_root / "package.json"),
                        "commitment_sha256": self.package["_verified_commitment_sha256"],
                        "started_at_utc": utc_now(),
                        "previous_hash": "0" * 64,
                    }
                    header = _event_with_hash(header_payload, self._event_mac_key)
                    lines.append(json.dumps(header, sort_keys=True) + "\n")
                    answer["previous_hash"] = header["event_hash"]
                event = _event_with_hash(answer, self._event_mac_key)
                lines.append(json.dumps(event, sort_keys=True) + "\n")
                handle.write("".join(lines))
                handle.flush()
                os.fsync(handle.fileno())
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        finally:
            os.close(descriptor)
        os.chmod(self.session_path, 0o600)
        self._events = self._load_events()
        self._session_snapshot_size = self.session_path.stat().st_size
        self._session_snapshot_sha256 = sha256_file(self.session_path)

    def submit(
        self,
        presentation_token: str,
        label_name: str,
        *,
        monotonic_value: float | None = None,
    ) -> dict:
        if presentation_token != self._presentation_token():
            raise HandcheckError("stale presentation; answer was not recorded")
        labels = {"CCW": 1, "CW": -1}
        normalized = str(label_name).upper()
        if normalized not in labels:
            raise HandcheckError("label must be CCW or CW")
        now_mono = time.monotonic() if monotonic_value is None else float(monotonic_value)
        if (
            self._last_recorded_monotonic is not None
            and now_mono - self._last_recorded_monotonic < self.debounce_seconds
        ):
            raise HandcheckError("debounce active; possible double keypress was not recorded")
        if self.package["role"] == HC1H_ROLE:
            queue, cursor, _reserves, systematic, _flags = self._hc1h_runtime()
            if systematic or self.completed >= len(self.package["items"]):
                raise HandcheckError("HC-1H session is not accepting labels")
            item = queue[cursor]
            event_sequence = cursor
        else:
            item = self.package["items"][self.completed]
            event_sequence = self.completed
        answer = {
            "schema_version": SCHEMA_VERSION,
            "event_type": "ANSWER_RECORDED",
            "sequence": event_sequence,
            "item_id": item["item_id"],
            "label": labels[normalized],
            "recorded_at_utc": utc_now(),
            "previous_hash": self._previous_hash(),
        }
        self._append_answer(answer)
        self._last_recorded_monotonic = now_mono
        return self.public_state()

    def flag_exposure(self, presentation_token: str, *, systematic: bool = False) -> dict:
        if self.package["role"] != HC1H_ROLE:
            raise HandcheckError("HC-7 exposure flags are available only in the HC-1H interface")
        if presentation_token != self._presentation_token():
            raise HandcheckError("stale presentation; HC-7 flag was not recorded")
        queue, cursor, reserves, already_systematic, _flags = self._hc1h_runtime()
        if already_systematic or self.completed >= len(self.package["items"]):
            raise HandcheckError("HC-1H session is not accepting exposure flags")
        item = queue[cursor]
        event_type = "SYSTEMATIC_EXPOSURE_HC7" if systematic else "ITEM_FLAGGED_HC7"
        if not systematic:
            flagged_item_ids = {
                event["item_id"]
                for event in self._events[1:]
                if event.get("event_type") == "ITEM_FLAGGED_HC7"
            }
            trial_queue = list(queue)
            trial_reserves = {key: list(value) for key, value in reserves.items()}
            try:
                self._hc1h_flag_transition(
                    trial_queue, cursor, trial_reserves, flagged_item_ids
                )
            except HandcheckError as error:
                if "replacement reserve exhausted" not in str(error):
                    raise
                event_type = "REPLACEMENT_RESERVE_EXHAUSTED_HC7"
        event = {
            "schema_version": SCHEMA_VERSION,
            "event_type": event_type,
            "sequence": cursor,
            "item_id": item["item_id"],
            "recorded_at_utc": utc_now(),
            "previous_hash": self._previous_hash(),
        }
        self._append_answer(event)
        return self.public_state()

    def acknowledge_break(self) -> dict:
        if (
            self.package["role"] != HC1H_ROLE
            or self.public_state()["status"] != "BREAK_REQUIRED"
            or self._presentations_since_break() != HC1H_SESSION_PRESENTATION_LIMIT
        ):
            raise HandcheckError("a session break can be acknowledged only after 50 presentations")
        _queue, cursor, _reserves, systematic, _flags = self._hc1h_runtime()
        if systematic:
            raise HandcheckError("HC-7 systematic exposure terminated the session")
        event = {
            "schema_version": SCHEMA_VERSION,
            "event_type": "BREAK_ACKNOWLEDGED",
            "sequence": cursor,
            "item_id": "NONE_SESSION_BREAK",
            "recorded_at_utc": utc_now(),
            "previous_hash": self._previous_hash(),
        }
        self._append_answer(event)
        return self.public_state()

    def record_ergonomics(self, acceptable: bool) -> dict:
        if (
            self.package["role"] != HC1H_ROLE
            or self.package["_mode"] != "pilot"
            or self.completed != len(self.package["items"])
            or self._ergonomics_value() is not None
        ):
            raise HandcheckError("pilot ergonomics can be recorded exactly once after all 150 labels")
        queue, cursor, _reserves, systematic, _flags = self._hc1h_runtime()
        if systematic or cursor != len(queue) or not isinstance(acceptable, bool):
            raise HandcheckError("pilot ergonomics event is not admissible")
        event = {
            "schema_version": SCHEMA_VERSION,
            "event_type": "ERGONOMICS_RECORDED",
            "sequence": cursor,
            "item_id": "NONE_SESSION_ERGONOMICS",
            "acceptable": acceptable,
            "recorded_at_utc": utc_now(),
            "previous_hash": self._previous_hash(),
        }
        self._append_answer(event)
        return self.public_state()


CHECKER_HTML = b"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NebulaMind blinded hand-check</title>
<style>
:root{color-scheme:dark;font-family:ui-sans-serif,system-ui,sans-serif}
body{margin:0;background:#070b12;color:#eef3fb;min-height:100vh;display:grid;place-items:center}
main{width:min(94vw,980px);display:grid;gap:14px;text-align:center}
#image-wrap{height:min(68vh,720px);display:grid;place-items:center;background:#111927;border:1px solid #2e405b;border-radius:12px;overflow:hidden}
img{max-width:100%;max-height:100%;image-rendering:auto}
#progress{font-size:1.15rem;font-variant-numeric:tabular-nums}
#keys{font-size:1.05rem;color:#c6d5e9}.key{border:1px solid #7891b5;border-radius:5px;padding:.12rem .45rem;color:#fff}
#status{min-height:1.5em;color:#ffd479}#instructions{font-size:.9rem;color:#9fb1c9;line-height:1.45}
</style></head><body><main>
<div id="progress">Loading committed package...</div>
<div id="image-wrap"><img id="image" alt="Current blinded hand-check image"></div>
<div id="keys"><span class="key">C</span> counter-clockwise &nbsp; <span class="key">W</span> clockwise &nbsp; <span class="key">F</span> Flag suspected synthetic/repeat exposure &nbsp; <span class="key">X</span> systematic exposure &nbsp; <span class="key">P</span> required break / pause</div>
<div id="prior"></div><div id="status" role="status" aria-live="polite"></div><div id="instructions"></div>
</main><script>
let state=null; let locked=false; let paused=false;
const image=document.getElementById('image'), progress=document.getElementById('progress');
const statusNode=document.getElementById('status'), instructions=document.getElementById('instructions'), prior=document.getElementById('prior');
const delay=ms=>new Promise(resolve=>setTimeout(resolve,ms));
function draw(next){state=next;progress.textContent=`${next.progress.completed} / ${next.progress.total}`;instructions.textContent=next.instructions;
 prior.textContent=next.prior_labels?`Prior blinded labels - A: ${next.prior_labels.A}; B: ${next.prior_labels.B}`:'';
 if(next.status==='AWAITING_ERGONOMICS'){image.removeAttribute('src');statusNode.textContent='Pilot labels complete. Press Y if interface ergonomics were acceptable, or N if not.';locked=false;return;}
 if(next.status==='BREAK_REQUIRED'){image.removeAttribute('src');statusNode.textContent='Session limit reached. Take a break, then press P to acknowledge and continue.';locked=false;return;}
 if(next.status==='COMPLETE'){image.removeAttribute('src');statusNode.textContent='Session complete. Close this window.';locked=true;return;}
 image.src=next.asset_url;statusNode.textContent=paused?'Paused. Press P to resume.':'';}
async function load(){const response=await fetch('/api/state',{cache:'no-store'});draw(await response.json());}
async function answer(label){locked=true;statusNode.textContent='Recording...';
 const response=await fetch('/api/answer',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({presentation_token:state.presentation_token,label})});
 if(!response.ok){statusNode.textContent='Not recorded. Wait, then classify the displayed image again.';await load();await delay(400);locked=false;return;}
 const next=await response.json();await delay(400);paused=false;draw(next);locked=false;}
document.addEventListener('keydown',event=>{if(event.repeat||locked)return;const key=event.key.toUpperCase();
 if(!state)return;if(state.status==='AWAITING_ERGONOMICS'){if(key==='Y')answer('ERGONOMICS_Y');else if(key==='N')answer('ERGONOMICS_N');return;}
 if(state.status==='BREAK_REQUIRED'){if(key==='P')answer('BREAK_ACKNOWLEDGED');return;}
 if(key==='P'){paused=!paused;statusNode.textContent=paused?'Paused. Press P to resume.':'';return;}
 if(paused||state.status!=='ACTIVE')return;if(key==='C')answer('CCW');else if(key==='W')answer('CW');else if(key==='F')answer('FLAG');else if(key==='X')answer('SYSTEMATIC');});
load().catch(()=>{statusNode.textContent='Interface failed closed. No answer was recorded.';locked=true;});
</script></body></html>"""


def make_checker_http_handler(application: CheckerApplication) -> type[BaseHTTPRequestHandler]:
    """Bind a local HTTP handler to exactly one checker capability."""
    application_lock = threading.Lock()

    class Handler(BaseHTTPRequestHandler):
        server_version = "NMHandcheck/1"

        def log_message(self, format: str, *args: object) -> None:
            return

        def _send(self, status_code: int, data: bytes, content_type: str) -> None:
            self.send_response(status_code)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store, max-age=0")
            self.send_header("Pragma", "no-cache")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("X-Frame-Options", "DENY")
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self'; img-src 'self'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; frame-ancestors 'none'",
            )
            self.end_headers()
            self.wfile.write(data)

        def _not_found(self) -> None:
            self._send(404, b'{"error":"not_found"}\n', "application/json; charset=utf-8")

        def do_GET(self) -> None:
            parsed = urlsplit(self.path)
            if parsed.path == "/":
                self._send(200, CHECKER_HTML, "text/html; charset=utf-8")
                return
            if parsed.path == "/api/state":
                with application_lock:
                    data = canonical_json_bytes(application.public_state()) + b"\n"
                self._send(200, data, "application/json; charset=utf-8")
                return
            if parsed.path == "/asset":
                values = parse_qs(parsed.query, strict_parsing=True)
                token_values = values.get("token", [])
                if len(token_values) != 1:
                    self._not_found()
                    return
                try:
                    with application_lock:
                        data, content_type = application.current_asset(token_values[0])
                except HandcheckError:
                    self._not_found()
                    return
                self._send(200, data, content_type)
                return
            self._not_found()

        def do_POST(self) -> None:
            if urlsplit(self.path).path != "/api/answer":
                self._not_found()
                return
            if not self.headers.get("Content-Type", "").lower().startswith("application/json"):
                self._send(415, b'{"error":"json_required"}\n', "application/json; charset=utf-8")
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                length = 0
            if length <= 0 or length > 4096:
                self._send(400, b'{"error":"invalid_request"}\n', "application/json; charset=utf-8")
                return
            try:
                payload = json.loads(self.rfile.read(length))
                if set(payload) != {"presentation_token", "label"}:
                    raise ValueError("field set")
                with application_lock:
                    if str(payload["label"]).upper() == "FLAG":
                        state = application.flag_exposure(payload["presentation_token"])
                    elif str(payload["label"]).upper() == "SYSTEMATIC":
                        state = application.flag_exposure(
                            payload["presentation_token"], systematic=True
                        )
                    elif str(payload["label"]).upper() in {"ERGONOMICS_Y", "ERGONOMICS_N"}:
                        state = application.record_ergonomics(
                            str(payload["label"]).upper() == "ERGONOMICS_Y"
                        )
                    elif str(payload["label"]).upper() == "BREAK_ACKNOWLEDGED":
                        state = application.acknowledge_break()
                    else:
                        state = application.submit(payload["presentation_token"], payload["label"])
            except (HandcheckError, ValueError, TypeError, json.JSONDecodeError):
                self._send(409, b'{"error":"answer_not_recorded"}\n', "application/json; charset=utf-8")
                return
            self._send(200, canonical_json_bytes(state) + b"\n", "application/json; charset=utf-8")

    return Handler


def allocate_proportional_floor(
    populations: Mapping[str, int], *, total: int = 500, floor: int = 40
) -> dict[str, int]:
    """Integer constrained-proportional allocation with a per-stratum floor.

    Continuous quotas are proportional among unfixed strata. Any quota below the
    floor is fixed at the floor and the remainder is redistributed. Final integer
    seats use largest remainders with lexical stratum IDs as the deterministic tie
    breaker.
    """
    if not populations:
        raise HandcheckError("at least one stratum is required")
    ordered = sorted(populations)
    values = {key: int(populations[key]) for key in ordered}
    if total <= 0 or floor < 0:
        raise HandcheckError("total must be positive and floor non-negative")
    if total < floor * len(ordered):
        raise HandcheckError("total cannot satisfy the per-stratum floor")
    if any(value < floor for value in values.values()):
        raise HandcheckError("every stratum population must cover the floor")
    if sum(values.values()) < total:
        raise HandcheckError("population is smaller than requested sample")

    fixed: dict[str, int] = {}
    active = set(ordered)
    remaining = total
    while True:
        active_population = sum(values[key] for key in active)
        below = [
            key
            for key in active
            if Fraction(remaining * values[key], active_population) < floor
        ]
        if not below:
            break
        for key in sorted(below):
            fixed[key] = floor
            active.remove(key)
            remaining -= floor
        if not active and remaining:
            raise HandcheckError("floor redistribution exhausted all strata")

    quotas = {
        key: Fraction(remaining * values[key], sum(values[name] for name in active))
        for key in active
    }
    allocation = dict(fixed)
    for key, quota in quotas.items():
        allocation[key] = quota.numerator // quota.denominator
    seats_left = total - sum(allocation.values())
    remainder_order = sorted(
        active,
        key=lambda key: (-(quotas[key] - allocation[key]), key),
    )
    for key in remainder_order[:seats_left]:
        allocation[key] += 1

    result = {key: allocation[key] for key in ordered}
    if sum(result.values()) != total:
        raise HandcheckError("allocation arithmetic did not close")
    if any(result[key] < floor or result[key] > values[key] for key in ordered):
        raise HandcheckError("allocation violates floor or population capacity")
    return result


def allocate_neyman(
    populations: Mapping[str, int],
    prior_rates: Mapping[str, Decimal | float | str],
    *,
    total: int = 500,
    floor: int = 30,
) -> dict[str, int]:
    """Solve constrained Neyman quotas N_s*sqrt(a_s*(1-a_s)); close integers deterministically."""
    keys = sorted(populations)
    if not keys or set(prior_rates) != set(keys):
        raise HandcheckError("Neyman allocation requires one prior rate per stratum")
    if total <= 0 or floor < 0 or total < floor * len(keys):
        raise HandcheckError("Neyman total cannot satisfy the requested floor")
    if total > sum(populations.values()):
        raise HandcheckError("Neyman total exceeds the available population")

    weights: dict[str, Decimal] = {}
    for key in keys:
        population = populations[key]
        if not isinstance(population, int) or population < floor:
            raise HandcheckError(f"stratum {key} cannot satisfy floor={floor}")
        rate = Decimal(str(prior_rates[key]))
        if not rate.is_finite() or rate < 0 or rate > 1:
            raise HandcheckError(f"invalid Neyman prior rate for stratum {key}")
        weights[key] = Decimal(population) * (rate * (1 - rate)).sqrt()

    if total > floor * len(keys) and not any(weights.values()):
        raise HandcheckError("Neyman prior rates yield zero information in every stratum")

    # Solve n_s=lambda*N_s*sqrt(a_s*(1-a_s)) subject to floor<=n_s<=N_s.
    # A floor is a lower-bound constraint, not a base tranche to which a second
    # proportional allocation may be added.
    continuous: dict[str, Decimal] = {}
    fixed: set[str] = set()
    active = set(keys)
    remaining = total
    while active:
        weight_total = sum(weights[key] for key in active)
        if weight_total <= 0:
            if remaining == floor * len(active):
                for key in active:
                    continuous[key] = Decimal(floor)
                fixed.update(active)
                active.clear()
                break
            raise HandcheckError("Neyman constrained allocation has no positive active weight")
        proposed = {
            key: Decimal(remaining) * weights[key] / weight_total for key in active
        }
        below = {key for key in active if proposed[key] < floor}
        above = {key for key in active if proposed[key] > populations[key]}
        if not below and not above:
            continuous.update(proposed)
            break
        # Capacity caps are resolved before lower bounds. Capping a high-weight
        # cell can raise a provisionally-low cell above its floor; fixing both
        # sets simultaneously can strand seats even when a feasible solution exists.
        violations = above if above else below
        for key in sorted(violations):
            value = populations[key] if key in above else floor
            continuous[key] = Decimal(value)
            fixed.add(key)
            remaining -= value
            active.remove(key)
        if remaining < 0:
            raise HandcheckError("Neyman constrained allocation overcommitted the total")
    if set(continuous) != set(keys):
        raise HandcheckError("Neyman continuous allocation did not close")

    allocation = {key: int(continuous[key]) for key in keys}
    leftover = total - sum(allocation.values())
    remainder_order = sorted(
        (
            key
            for key in keys
            if key not in fixed and allocation[key] < populations[key]
        ),
        key=lambda key: (-(continuous[key] - allocation[key]), key),
    )
    if leftover < 0 or leftover > len(remainder_order):
        raise HandcheckError("Neyman largest-remainder closure failed")
    for key in remainder_order[:leftover]:
        allocation[key] += 1

    if sum(allocation.values()) != total:
        raise HandcheckError("Neyman allocation did not close to the requested total")
    if any(
        allocation[key] < floor or allocation[key] > populations[key] for key in keys
    ):
        raise HandcheckError("Neyman allocation violates a floor or stratum capacity")
    return allocation


def _read_passphrase_file(path: Path) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise HandcheckError("passphrase file must be a regular non-symlink file")
    mode = stat.S_IMODE(path.stat().st_mode)
    if mode & 0o077:
        raise HandcheckError("passphrase file must be private (chmod 600)")
    passphrase = path.read_bytes().rstrip(b"\r\n")
    if len(passphrase) < 16:
        raise HandcheckError("passphrase file must contain at least 16 bytes")
    return passphrase


def _json_print(value: dict) -> None:
    print(json.dumps(value, sort_keys=True, indent=2))


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Accepted one-human blinded attenuation harness (HC-1H)."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="custodian: sample, blind, seal, and commit")
    prepare.add_argument("--real-population", type=Path, required=True)
    prepare.add_argument("--synthetic-pool", type=Path, required=True)
    prepare.add_argument("--neyman-priors", type=Path, required=True)
    prepare.add_argument("--private-root", type=Path, required=True)
    prepare.add_argument("--checking-root", type=Path, required=True)
    prepare.add_argument("--passphrase-file", type=Path, required=True)
    prepare.add_argument("--checker-id", required=True)
    prepare.add_argument("--mode", choices=("full", "pilot"), default="full")
    prepare.add_argument("--replacement-reserve-per-group", type=int, default=1)
    prepare.add_argument(
        "--additional-covariance",
        type=Decimal,
        help="separately approved non-negative variance term; required for authorized_measurement",
    )
    prepare.add_argument("--pilot-private-root", type=Path)
    prepare.add_argument("--pilot-public-result", type=Path)
    prepare.add_argument(
        "--pilot-policy",
        choices=("no-pilot-run", "exclude-completed-pilot"),
        required=True,
    )

    check = subparsers.add_parser("check", help="checker: run one isolated single-key interface")
    check.add_argument("--package", type=Path, required=True)
    check.add_argument("--control-file", type=Path, required=True)
    check.add_argument("--host", default="127.0.0.1", choices=("127.0.0.1", "localhost"))
    check.add_argument("--port", type=int, default=8765)
    check.add_argument("--open-browser", action="store_true")

    reduce = subparsers.add_parser(
        "reduce", help="custodian: unseal only after the one-human stream and split outputs"
    )
    reduce.add_argument("--private-root", type=Path, required=True)
    reduce.add_argument("--checking-root", type=Path, required=True)
    reduce.add_argument("--passphrase-file", type=Path, required=True)
    reduce.add_argument("--private-output-root", type=Path, required=True)
    reduce.add_argument("--public-output-root", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_argument_parser().parse_args(argv)
    try:
        if args.command == "prepare":
            if args.pilot_policy == "no-pilot-run" and (
                args.pilot_private_root is not None or args.pilot_public_result is not None
            ):
                raise HandcheckError("no-pilot-run cannot be combined with pilot artifacts")
            if args.pilot_policy == "exclude-completed-pilot" and (
                args.pilot_private_root is None or args.pilot_public_result is None
            ):
                raise HandcheckError(
                    "exclude-completed-pilot requires pilot private root and public result"
                )
            priors_document = json.loads(args.neyman_priors.read_text(encoding="utf-8"))
            if not isinstance(priors_document, dict):
                raise HandcheckError("Neyman prior file must be a JSON object keyed by nine strata")
            counts = (90, 40, 20, 10) if args.mode == "pilot" else (500, 200, 150, 30)
            receipt = prepare_hc1h_experiment(
                real_population_path=args.real_population,
                synthetic_pool_path=args.synthetic_pool,
                neyman_prior_rates=priors_document,
                private_root=args.private_root,
                checking_root=args.checking_root,
                passphrase=_read_passphrase_file(args.passphrase_file),
                checker_id=args.checker_id,
                mode=args.mode,
                real_total=counts[0],
                synthetic_total=counts[1],
                repeat_total=counts[2],
                real_floor=counts[3],
                replacement_reserve_per_group=args.replacement_reserve_per_group,
                pilot_private_root=args.pilot_private_root,
                pilot_public_result_path=args.pilot_public_result,
                additional_covariance=args.additional_covariance,
            )
            _json_print(receipt)
            return 0
        if args.command == "reduce":
            result = reduce_hc1h_experiment(
                private_root=args.private_root,
                checking_root=args.checking_root,
                passphrase=_read_passphrase_file(args.passphrase_file),
                private_output_root=args.private_output_root,
                public_output_root=args.public_output_root,
            )
            if result["status"] == "HARD_INCONCLUSIVE_HC7_IDENTITY_EXPOSURE":
                _json_print(result)
            else:
                _json_print(
                    {
                        "status": result["status"],
                        "experiment_id": result["experiment_id"],
                        "pilot_outcome": result["pilot_outcome"],
                        "verdict": result["statistics"]["verdict"],
                        "attenuation": result["statistics"].get("attenuation"),
                    }
                )
            return 0

        application = CheckerApplication(args.package, control_path=args.control_file)
        server = ThreadingHTTPServer((args.host, args.port), make_checker_http_handler(application))
        url = f"http://{args.host}:{server.server_port}/"
        print(f"Blinded HC-1H checker ready at {url}")
        print("C/W label, F flags a specific exposure, X flags systematic exposure, P pauses.")
        if args.open_browser:
            webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()
        return 0
    except (HandcheckError, OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"FAIL_CLOSED: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

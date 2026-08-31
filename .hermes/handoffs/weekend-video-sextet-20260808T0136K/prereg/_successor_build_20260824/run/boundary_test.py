#!/usr/bin/env python3
"""Prove the honest three-part single-user POSIX mediator boundary."""
import json
import stat
import sys
import tempfile
from pathlib import Path

import bs2k_stage_v2 as stage


def main() -> int:
    receipt = {"model": "0700 directory roots plus mediator capability process path",
               "posix_residual": "owner raw read succeeds on 0700 roots on a single-user machine",
               "stores": {}}
    fixture_count = 0
    for root in stage.store_roots():
        mode = stat.S_IMODE(root.stat().st_mode)
        if mode != 0o700:
            raise AssertionError(f"{root}: mode {mode:o}, expected 700")
        fixture_count += 1

        # Labeled traversal probe: an allowed root with a lexical escape.
        try:
            stage.mediator_read(root, "../.boundary-probe")
        except stage.Refusal as exc:
            traversal_refusal = exc.code
        else:
            raise AssertionError(f"mediator accepted traversal request: {root}")
        if traversal_refusal != stage.REFUSAL_TRAVERSAL:
            raise AssertionError(f"wrong traversal refusal: {traversal_refusal}")
        fixture_count += 1

        # Labeled allowed-root probe: a genuine sibling outside all stores.
        unallowed_root = stage.PROV.parent / "unallowed-sibling"
        try:
            stage.mediator_read(unallowed_root)
        except stage.Refusal as exc:
            allowed_root_refusal = exc.code
        else:
            raise AssertionError(f"mediator accepted unallowed root: {unallowed_root}")
        if (allowed_root_refusal != stage.REFUSAL_DIRECT or
                allowed_root_refusal == traversal_refusal):
            raise AssertionError("allowed-root refusal is not distinct from traversal")
        fixture_count += 1

        inside = stage.mediator_read(root).decode().strip()
        fixture_count += 1
        owner_raw = (root / ".boundary-probe").read_bytes().decode().strip()
        fixture_count += 1
        if inside != "mediator-boundary-green" or owner_raw != "mediator-boundary-green":
            raise AssertionError(root)
        receipt["stores"][root.name] = {
            "allowed_root_probe": allowed_root_refusal,
            "traversal_probe": traversal_refusal,
            "mediator_read": "SUCCEEDED", "owner_raw_read": "SUCCEEDED",
            "owner_raw_read_classification": "NAMED-POSIX-OWNER-RESIDUAL",
            "root_mode": "0700"}

    root = stage.store_roots()[0]
    with tempfile.TemporaryDirectory(dir=stage.HERE) as outside:
        target = Path(outside) / "outside"
        target.write_bytes(b"must-not-be-readable")
        link = root / ".boundary-symlink"
        try:
            link.symlink_to(target)
            stage.expect_refusal(stage.REFUSAL_TRAVERSAL,
                                 lambda: stage.mediator_read(root, link.name))
        finally:
            link.unlink(missing_ok=True)
    fixture_count += 1
    receipt["symlink_escape_probe"] = stage.REFUSAL_TRAVERSAL
    print(json.dumps(receipt, sort_keys=True))
    print(f"boundary fixtures: {fixture_count}/{fixture_count} green "
          "(3 mode, 3 traversal, 3 allowed-root, 3 mediated read, "
          "3 owner raw-read residual, 1 symlink escape)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

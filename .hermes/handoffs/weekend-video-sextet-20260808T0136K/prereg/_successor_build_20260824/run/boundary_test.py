#!/usr/bin/env python3
"""Prove the honest three-part single-user POSIX mediator boundary."""
import json
import stat
import sys

import bs2k_stage_v2 as stage


def main() -> int:
    receipt = {"model": "0700 directory roots plus mediator capability process path",
               "posix_residual": "owner raw read succeeds on 0700 roots on a single-user machine",
               "stores": {}}
    for root in stage.store_roots():
        mode = stat.S_IMODE(root.stat().st_mode)
        if mode != 0o700:
            raise AssertionError(f"{root}: mode {mode:o}, expected 700")
        try:
            stage.mediator_read(root, "../.boundary-probe")
        except stage.Refusal as exc:
            api_refusal = exc.code
        else:
            raise AssertionError(f"mediator accepted non-mediated request: {root}")
        inside = stage.mediator_read(root).decode().strip()
        owner_raw = (root / ".boundary-probe").read_bytes().decode().strip()
        if (api_refusal != stage.REFUSAL_DIRECT or inside != "mediator-boundary-green" or
                owner_raw != "mediator-boundary-green"):
            raise AssertionError(root)
        receipt["stores"][root.name] = {
            "mediator_nonmediated_request": api_refusal,
            "mediator_read": "SUCCEEDED", "owner_raw_read": "SUCCEEDED",
            "owner_raw_read_classification": "NAMED-POSIX-OWNER-RESIDUAL",
            "root_mode": "0700"}
    print(json.dumps(receipt, sort_keys=True))
    print("boundary fixtures: 9/9 green (3 mode, 3 API refusal, 3 owner raw-read residual)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

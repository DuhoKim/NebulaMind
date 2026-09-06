# REPRODUCTION of codex's V20 FATAL before any repair (Blanc order step 2) — 2026-09-06 19:48:31 KST

Claim: the pinned production driver `run_configurations_v4.py` is not executable as the selection path — `PRODUCTION.rederive_seed` is None and `load_identity` refuses on it.

## (a) The pinned bytes
```
run_configurations_v4.py SHA-256 d55ea70ddb27ba3b849204addeec3da0551657b7a0bb3d53a422d61f9a7d7993
80:    rederive_seed: object = None                                                # v4: callable(record_path) -> seed hex (the drand-only verdict, no network);
81:PRODUCTION = Protocol()
169:    if proto.rederive_seed is None: raise DataIntegrityFail("PROTOCOL-NO-REDERIVER: the protocol must supply the drand-only seed re-derivation")
343:        s = tune(a.manifest, a.tensors, a.out, a.identity) if a.mode == "tune" else holdout(a.tuning_receipt, a.manifest, a.tensors, a.out, a.identity)
```

## (b) The production protocol value, executed
```
PRODUCTION.label = PRODUCTION
PRODUCTION.rederive_seed = None
PRODUCTION.require_beacon = True
```

## (c) load_identity through the real function with a production-shaped, sealed, witnessed identity whose ONLY deviation from the fixture is rederive_seed=None (the production value)
```
REFUSED: PROTOCOL-NO-REDERIVER: the protocol must supply the drand-only seed re-derivation
with an INJECTED callback the same identity loads: 6 tuning objids
```

## (d) Conclusion
Reproduced: under the production protocol the driver refuses every identity with PROTOCOL-NO-REDERIVER; the fixture passed only through an injected callback. The claim is correct. Repair follows (V21), tested through the production path with no callback substitution.

## (e) AFTER THE REPAIR (driver v5), the same exercise, executed 20:16 KST
```
PRODUCTION.rederive_seed = run_configurations_v5.production_rederive_seed
test protocol re-deriver is PRODUCTION's: True
LOADED through PRODUCTION's re-deriver: 6 tuning objids; seed 68547455ba7d5000…
with the V20 production value the same identity is still REFUSED: PROTOCOL-NO-REDERIVER: the protocol must supply the drand-only seed re-derivation
```

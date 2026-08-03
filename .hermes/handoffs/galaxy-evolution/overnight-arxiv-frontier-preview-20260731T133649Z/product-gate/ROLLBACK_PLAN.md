# Gate C rollback plan

The four exact before-images are under `rollback_snapshot/`. Rollback must be atomic under the frontier pipeline lock, hash-bound to the final Gate C receipt, and separately approved. It must refuse unless all active targets still match the Gate C after-state and every snapshot matches its recorded before-hash. No broad Git reset/clean is permitted.

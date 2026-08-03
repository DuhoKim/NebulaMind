# Frontier live build-swap and restart plan

1. Revalidate the Gate C receipt, exact live source hashes, existing LaunchAgent identity, old build ID, port-3000 ownership, and empty staging/rollback paths.
2. Mirror the exact live frontend source into `build-stage/frontend`, excluding `.next`, `node_modules`, build caches, and environment files; symlink only the existing dependency tree.
3. Run `npm run build` in the isolated stage and require lint/type/build success plus new ranking markers and no old ranking markers.
4. Revalidate the live source and service immediately before swap.
5. Under the restart lock, atomically rename the active `.next` to `rollback-live-next` and the verified staged `.next` into the active location.
6. Restart only `gui/501/com.nebulamind.frontend` with `launchctl kickstart -k`.
7. Require a new PID, port 3000, local `/lab` HTTP 200, new build ID/markers, and external/public verification.
8. On failure, stop the changed process, atomically restore the old `.next`, kickstart the same LaunchAgent, and verify the old build is healthy.
9. Preserve rollback custody and seal the restart receipt. No Git, DB, scheduler definition, cockpit, curated-topic, or paper-merit mutation is permitted.

# Scheduled cockpit rendering — INSTALLED 2026-08-20 16:09 KST (Duho: "install the cockpit render agent")

Today nothing schedules the renderers: the cockpit freezes whenever the OPS
session sleeps (it sat 7.5 h stale on 08-19 night). This LaunchAgent renders
every 10 minutes.

Installed and running (first launchd pass verified at 16:09 KST). Reinstall/update:
  cp tools/cockpit-scheduling/com.nebulamind.cockpit-render.plist ~/Library/LaunchAgents/
  launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.nebulamind.cockpit-render.plist

Remove:
  launchctl bootout gui/$UID/com.nebulamind.cockpit-render

Log: /Users/duhokim/HermesOps/cockpit/render.log

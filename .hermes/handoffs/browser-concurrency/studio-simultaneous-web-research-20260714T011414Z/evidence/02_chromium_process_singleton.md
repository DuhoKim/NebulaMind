# Chromium process-singleton evidence
URL: https://chromium.googlesource.com/chromium/src/+/HEAD/chrome/browser/process_singleton_posix.cc
Accessed: 2026-07-14
Product/version: Chromium HEAD, POSIX implementation including macOS branches

> When the user tries to launch a second copy of chrome, we check for a socket in the user's profile directory. If the socket file is open we send a message to the first chrome browser process ... The second process then exits.

> We also have a lock file ... containing the hostname and process id of chrome's browser process.

Caveat: the leading description is written for Linux; same source file has explicit `BUILDFLAG(IS_MAC)` process-singleton code. Playwright separately documents the cross-browser user-data-dir restriction.

# Chrome remote-debugging evidence
URL: https://developer.chrome.com/blog/remote-debugging-port
Accessed: 2026-07-14
Product/version: Google Chrome 136+, article published 2025-03-17

> Therefore, from Chrome 136 we're making changes to the behavior of `--remote-debugging-port` and `--remote-debugging-pipe`. These switches will no longer be respected if attempting to debug the default Chrome data directory.

> These switches must now be accompanied by the `--user-data-dir` switch to point to a non-standard directory.

> For browser automation scenarios, we recommend using Chrome for Testing which will continue to respect the existing behavior.

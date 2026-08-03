# cua-driver macOS target-addressing evidence
URL: https://github.com/trycua/cua/blob/main/blog/inside-macos-window-internals.md
Accessed: 2026-07-14
Product/version: cua-driver macOS article published 2026-04-23; repository current on access date

> The user's cursor doesn't move, focus doesn't change, and macOS doesn't drag them across Spaces.

> Keystrokes scoped to a specific pid land in that app's event queue and nowhere else.

> Element-indexed clicks (`click({pid, window_id, element_index})`) are the primary addressing mode.

Caveat: this official project article states early-preview status and documents private macOS SPI. App/PID/window/element addressing is supported; durable browser-tab identity is not documented here.

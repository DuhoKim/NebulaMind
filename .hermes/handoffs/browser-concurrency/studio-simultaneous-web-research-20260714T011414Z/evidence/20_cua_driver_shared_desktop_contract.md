# cua-driver shared-desktop and target-routing contract
URLs:
- https://github.com/trycua/cua/blob/3cadb5f82e7d2ed071a2082764276ec872a52135/docs/content/docs/reference/cua-driver/process-model.mdx
- https://github.com/trycua/cua/blob/3cadb5f82e7d2ed071a2082764276ec872a52135/docs/content/docs/reference/cua-driver/contracts.mdx
- https://github.com/trycua/cua/blob/3cadb5f82e7d2ed071a2082764276ec872a52135/docs/content/docs/reference/cua-driver/mcp-tools.mdx
Accessed: 2026-07-14
Product/version: Cua Driver 0.7.1 docs pinned to commit 3cadb5f82e7d2ed071a2082764276ec872a52135

> Multiple MCP clients can connect at the same time, but they still share the same screen, keyboard, pointer, accessibility tree, and recording machinery. Session identity does not make concurrent control independent. Two agents clicking at once still contend for the same desktop.

> Window scope is the default because it is what makes background, concurrent automation possible.

> `element_index` + `window_id` | accessibility action | UIA Invoke / `AXPerformAction` / AT-SPI. Background, no cursor move, no focus steal.

> For a browser TAB the reliable path is the `page` tool (drives the DOM via CDP).

Verdict: VERIFIED and qualifying. Cua supports exact background window/element actions, but multiple sessions are not independent desktop channels. Browser concurrency must use separate browser instances and DOM/CDP for parallel writes; cua/desktop writes need broker serialization.

# Chrome DevTools Protocol target evidence
URL: https://chromedevtools.github.io/devtools-protocol/
Accessed: 2026-07-14
Product/version: Chrome DevTools Protocol, current official protocol site

> If Chrome was launched with `--remote-debugging-port=0` and chose an open port, the browser endpoint is written to both stderr and the `DevToolsActivePort` file in browser profile folder.

> Chrome 63 introduced support for multiple clients.

> A list of all available websocket targets.

> Closes the target page identified by `targetId`.

Implication limited to protocol addressing: CDP exposes durable target IDs and multiple clients, but multiple writers still require a broker because protocol support is not action serialization.

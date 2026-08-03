# MacBook Computer Use setup receipt

Marker: `MACBOOK_COMPUTER_USE_VERIFIED_20260721`

## Host

- MacBook: `Duhoui-MacBookPro-4.local`
- Tailscale/SSH address: `100.75.47.116`
- Architecture: Apple Silicon `arm64`
- macOS: `26.5.2`
- GUI user: `duhokim`

## Installed and configured

- Existing Hermes preserved: `v0.17.0`, Python `3.11.15`
- CuaDriver installed: `0.10.0`
- App identity: `/Applications/CuaDriver.app` / `com.trycua.driver`
- Launcher: `~/.local/bin/cua-driver`
- Hermes toolset `computer_use`: enabled
- Accessibility: granted
- Screen Recording: granted
- Gateway service: absent
- Open WebUI service: absent

## Verification

- Native `cua-driver doctor --json`: `ok: true`
- Read-only accessibility capture: succeeded and returned live MacBook apps/windows
- Finder window capture: 39 AX elements plus PNG screenshot
- Screenshot size: 1,104,089 bytes
- Screenshot SHA-256: `cdd30144bcb1c300e9bd451997d6733619379c121aa3e82a2f8e58f9d031b3de`

## Operational note

Non-interactive SSH does not source the MacBook zsh PATH. Remote commands must use `export PATH="$HOME/.local/bin:$PATH"` or absolute launchers. Hermes `v0.17.0` does not format CuaDriver `0.10.0` health output correctly; use `cua-driver doctor --json`, `cua-driver permissions status`, and direct `cua-driver call ...` until Hermes is separately approved for update.

No provider credentials, gateway, cron, Open WebUI, or duplicate workers were installed or changed.

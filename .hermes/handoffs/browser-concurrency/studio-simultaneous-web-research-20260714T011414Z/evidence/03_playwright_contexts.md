# Playwright browser-context evidence
URL: https://playwright.dev/docs/browser-contexts
Accessed: 2026-07-14
Product/version: Playwright documentation current on access date

> BrowserContext s ... are equivalent to incognito-like profiles. They are fast and cheap to create and are completely isolated, even when running in a single browser.

> Playwright can create multiple browser contexts within a single scenario.

Scope caveat: context isolation covers cookies, local/session storage, and related browser state; it does not isolate OS-global focus, keyboard, clipboard, app crashes, or account-side quota.

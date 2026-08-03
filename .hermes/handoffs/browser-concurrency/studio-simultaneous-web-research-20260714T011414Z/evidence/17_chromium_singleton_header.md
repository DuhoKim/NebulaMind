# Chromium singleton header evidence
URL: https://chromium.googlesource.com/chromium/src/+/main/chrome/browser/process_singleton.h#39
Accessed: 2026-07-14
Product/version: Chromium main, blob 6f081c26ca4cffe76104eae5a4130a81a93a539d

> It is named according to the user data directory, so we can be sure that no more than one copy of the application can be running at once with a given data directory.

Verdict: VERIFIED. This is a clearer cross-platform statement than the earlier POSIX implementation comment.

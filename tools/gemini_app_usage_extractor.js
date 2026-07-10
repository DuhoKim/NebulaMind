// Non-interactive DOM extractor for gemini.google.com/usage.
//
// This is the auto-fetch counterpart of gemini_app_usage_bookmarklet.js: same
// reading logic, but NO prompts and NO clipboard — it just returns a JSON string
// for gemini_app_usage_autofetch.py to consume. AppleScript reads this file and
// runs it via Chrome's "execute javascript", which sidesteps all shell-escaping.
//
// Crucially it reports HOW the percentage was found (source_signal) so the caller
// can refuse a low-confidence read: an unattended scrape has no human to confirm
// the number, so it must abstain rather than store a guess.
(function () {
  function fromProgressbar() {
    var nodes = document.querySelectorAll('[role="progressbar"][aria-valuenow]');
    for (var i = 0; i < nodes.length; i++) {
      var v = parseFloat(nodes[i].getAttribute('aria-valuenow'));
      if (isFinite(v) && v >= 0 && v <= 100) return v;
    }
    return null;
  }

  function fromScoped(text) {
    var scoped = text.match(/[^.\n]{0,80}(?:usage|limit|used)[^.\n]{0,80}/gi) || [];
    for (var i = 0; i < scoped.length; i++) {
      var m = scoped[i].match(/(\d{1,3}(?:\.\d+)?)\s*%/);
      if (m) {
        var v = parseFloat(m[1]);
        if (v >= 0 && v <= 100) return v;
      }
    }
    return null;
  }

  function fromAny(text) {
    var m = text.match(/(\d{1,3}(?:\.\d+)?)\s*%/);
    if (m) {
      var v = parseFloat(m[1]);
      if (v >= 0 && v <= 100) return v;
    }
    return null;
  }

  function resetLabel(text) {
    var m = text.match(/[^.\n]{0,40}reset[^.\n]{0,60}/i);
    return m ? m[0].trim().replace(/\s+/g, ' ') : '';
  }

  function tierGuess(text) {
    var m = text.match(/Google AI (Ultra|Pro|Plus)/i);
    return m ? 'AI ' + m[1] : '';
  }

  var onUsagePage = /(^|\.)gemini\.google\.com$/.test(location.hostname) &&
    /\/usage/.test(location.pathname);
  var body = (document.body && document.body.innerText) || '';

  var pct = fromProgressbar();
  var signal = 'progressbar';
  if (pct === null) { pct = fromScoped(body); signal = 'scoped-text'; }
  if (pct === null) { pct = fromAny(body); signal = 'any-text'; }
  if (pct === null) { signal = 'none'; }

  return JSON.stringify({
    used_pct: pct,
    source_signal: signal,
    reset_label: resetLabel(body),
    tier_guess: tierGuess(body),
    on_usage_page: onUsagePage,
    href: location.href
  });
})();

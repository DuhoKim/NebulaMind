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
    // The usage page now has multiple progress bars (Current vs Weekly).
    // It is safer to rely on text parsing (fromScoped) than blindly picking the first or last progressbar.
    return null;
  }

  function fromScoped(text) {
    // Prefer Weekly limit if it exists
    var weeklyMatch = text.match(/Weekly limit[\s\S]{0,500}?(\d{1,3}(?:\.\d+)?)\s*%/i);
    if (weeklyMatch) {
      var v = parseFloat(weeklyMatch[1]);
      if (v >= 0 && v <= 100) return v;
    }
    // Fallback to original
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

  function scopedMetric(text, heading) {
    var blockMatch = text.match(new RegExp(heading + '[\\s\\S]{0,500}', 'i'));
    if (!blockMatch) return { pct: null, reset: '' };
    var block = blockMatch[0];
    var pctMatch = block.match(/(\d{1,3}(?:\.\d+)?)\s*%/);
    var resetMatch = block.match(/Resets[^.\n]{0,80}/i);
    var pct = pctMatch ? parseFloat(pctMatch[1]) : null;
    if (pct !== null && (pct < 0 || pct > 100)) pct = null;
    return {
      pct: pct,
      reset: resetMatch ? resetMatch[0].trim().replace(/\s+/g, ' ') : ''
    };
  }

  function resetLabel(text) {
    // Prefer the Weekly limit reset
    var weeklyMatch = text.match(/Weekly limit[\s\S]{0,500}?(Resets[^.\n]{0,60})/i);
    if (weeklyMatch) return weeklyMatch[1].trim().replace(/\s+/g, ' ');
    // Fallback to original
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
  var currentMetric = scopedMetric(body, 'Current usage');
  var weeklyMetric = scopedMetric(body, 'Weekly limit');

  var pct = currentMetric.pct;
  var signal = pct === null ? 'progressbar' : 'scoped-text';
  if (pct === null) { pct = fromProgressbar(); }
  if (pct === null && weeklyMetric.pct !== null) { pct = weeklyMetric.pct; signal = 'scoped-text'; }
  if (pct === null) { pct = fromScoped(body); signal = 'scoped-text'; }
  if (pct === null) { pct = fromAny(body); signal = 'any-text'; }
  if (pct === null) { signal = 'none'; }

  return JSON.stringify({
    used_pct: pct,
    source_signal: signal,
    reset_label: currentMetric.reset || resetLabel(body),
    weekly_used_pct: weeklyMetric.pct,
    weekly_reset_label: weeklyMetric.reset,
    tier_guess: tierGuess(body),
    on_usage_page: onUsagePage,
    href: location.href
  });
})();

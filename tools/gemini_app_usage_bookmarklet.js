// Bookmarklet: capture the gemini.google.com/usage meter to the clipboard.
//
// Why the clipboard and not a POST to localhost: gemini.google.com serves
//   default-src 'none'; connect-src 'self' https://*.google.com ...
// so any fetch() from page context to 127.0.0.1 is blocked by CSP. Clipboard
// writes are unaffected by connect-src and are permitted under a user gesture,
// which a bookmarklet click supplies.
//
// This never reads cookies and never automates a session. You are already on
// the page; it reads the rendered DOM, shows you what it found, and asks you to
// confirm before anything leaves the browser. If parsing fails it asks you to
// type the number rather than emitting a guess.
//
// Install: python3 tools/gemini_app_usage_ingest.py --emit-bookmarklet
// Use:     open https://gemini.google.com/usage, click the bookmark, confirm,
//          then run: python3 tools/gemini_app_usage_ingest.py --from-clipboard
(function () {
  var SCHEMA = 'NM_GEMINI_APP_USAGE_V1';

  if (!/(^|\.)gemini\.google\.com$/.test(location.hostname)) {
    alert('Run this on https://gemini.google.com/usage (Settings -> Usage Limits).');
    return;
  }

  // A progressbar node is the most reliable signal when the page ships one.
  function fromProgressbar() {
    var nodes = document.querySelectorAll('[role="progressbar"][aria-valuenow]');
    for (var i = 0; i < nodes.length; i++) {
      var v = parseFloat(nodes[i].getAttribute('aria-valuenow'));
      if (isFinite(v) && v >= 0 && v <= 100) return v;
    }
    return null;
  }

  // Otherwise take a percentage that sits near usage/limit wording.
  function fromText(text) {
    var scoped = text.match(/[^.\n]{0,80}(?:usage|limit|used)[^.\n]{0,80}/gi) || [];
    for (var i = 0; i < scoped.length; i++) {
      var m = scoped[i].match(/(\d{1,3}(?:\.\d+)?)\s*%/);
      if (m) {
        var v = parseFloat(m[1]);
        if (v >= 0 && v <= 100) return v;
      }
    }
    var any = text.match(/(\d{1,3}(?:\.\d+)?)\s*%/);
    if (any) {
      var w = parseFloat(any[1]);
      if (w >= 0 && w <= 100) return w;
    }
    return null;
  }

  function resetLabel(text) {
    var m = text.match(/[^.\n]{0,40}reset[^.\n]{0,60}/i);
    return m ? m[0].trim().replace(/\s+/g, ' ') : '';
  }

  var iso = function (d) {
    return d.toISOString().replace(/\.\d{3}Z$/, 'Z');
  };

  // "resets in 3 hr 20 min" -> absolute UTC, so a later reader can age it out.
  // Longest alternative first: 'h|hr|hour' would match the 'h' of 'hr' and
  // strand the 'r', silently dropping the minutes that follow.
  function relativeResetAtUtc(label, capturedAt) {
    var m = label.match(/in\s+(?:(\d+)\s*(?:hours?|hrs?|h)\b)?\s*(?:(\d+)\s*(?:minutes?|mins?|m)\b)?/i);
    if (!m || (!m[1] && !m[2])) return null;
    var mins = (parseInt(m[1] || '0', 10) * 60) + parseInt(m[2] || '0', 10);
    if (!mins) return null;
    return iso(new Date(capturedAt.getTime() + mins * 60000));
  }

  // The live page words it "Resets at 2:59 AM" — a local clock time, not an offset.
  // A time already past today means tomorrow; the window always resets ahead.
  function absoluteResetAtUtc(label, capturedAt) {
    var m = label.match(/at\s+(\d{1,2}):(\d{2})\s*([AaPp])\.?[Mm]\.?/);
    if (!m) return null;
    var hour = parseInt(m[1], 10);
    var minute = parseInt(m[2], 10);
    if (hour < 1 || hour > 12 || minute > 59) return null;
    hour = m[3].toLowerCase() === 'p' ? (hour % 12) + 12 : hour % 12;
    var reset = new Date(capturedAt.getTime());
    reset.setHours(hour, minute, 0, 0);
    if (reset <= capturedAt) reset.setDate(reset.getDate() + 1);
    return iso(reset);
  }

  function resetAtUtc(label, capturedAt) {
    if (!label) return null;
    return relativeResetAtUtc(label, capturedAt) || absoluteResetAtUtc(label, capturedAt);
  }

  // The usage page does not reliably name the plan, so this is only a pre-fill.
  function tierGuess(text) {
    var m = text.match(/Google AI (Ultra|Pro|Plus)/i);
    return m ? 'AI ' + m[1] : '';
  }

  var body = (document.body && document.body.innerText) || '';
  var guessPct = fromProgressbar();
  if (guessPct === null) guessPct = fromText(body);

  var typed = prompt(
    'gemini.google.com/usage capture\n\n' +
      'Percent of your allowance USED (0-100).\n' +
      (guessPct === null
        ? 'Could not read it from the page — please type what you see.'
        : 'Read from the page as ' + guessPct + '. Correct it if that is wrong.'),
    guessPct === null ? '' : String(guessPct)
  );
  if (typed === null) return;

  var usedPct = parseFloat(String(typed).replace('%', '').trim());
  if (!isFinite(usedPct) || usedPct < 0 || usedPct > 100) {
    alert('Not a percentage between 0 and 100 — nothing captured.');
    return;
  }

  var capturedAt = new Date();
  var label = prompt('Reset text as shown, e.g. "Resets at 2:59 AM" (blank if none):', resetLabel(body));
  if (label === null) return;

  var tier = prompt('Your plan, e.g. "AI Pro" (blank if unsure):', tierGuess(body));
  if (tier === null) return;

  var payload = {
    schema: SCHEMA,
    used_pct: usedPct,
    reset_label: label || null,
    reset_at_utc: resetAtUtc(label || '', capturedAt),
    tier: (tier || '').trim() || null,
    source_url: 'https://gemini.google.com/usage',
    captured_at_utc: capturedAt.toISOString().replace(/\.\d{3}Z$/, 'Z'),
    capture_method: 'bookmarklet-confirmed'
  };

  var json = JSON.stringify(payload, null, 2);
  var done = function () {
    alert('Copied.\n\nNow run:\n  python3 tools/gemini_app_usage_ingest.py --from-clipboard\n\n' + json);
  };

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(json).then(done, function () {
      window.prompt('Clipboard blocked — copy this JSON manually:', json);
    });
  } else {
    window.prompt('Copy this JSON:', json);
  }
})();

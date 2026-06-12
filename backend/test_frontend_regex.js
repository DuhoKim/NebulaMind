const { execSync } = require('child_process');
const fs = require('fs');

// Fetch current page content from python (using verify_markers.py output or writing a small script)
const content = execSync('.venv/bin/python -c "from app.database import SessionLocal; from app.models.page import WikiPage; db=SessionLocal(); p=db.query(WikiPage).get(57); print(p.content); db.close()"', {
  cwd: '/Users/duhokim/NebulaMind/NebulaMind/backend'
}).toString();

function wrapClaimComments(content) {
  return content.replace(
    /<!--\s*claim:([\d,\s]+?)\s*-->([\s\S]*?)<!--\s*\/claim:\1\s*-->/g,
    (_, idList, body) => {
      const safe = body.replace(/</g, '&lt;').replace(/>/g, '&gt;');
      const ids = String(idList).replace(/\s+/g, '').split(',').filter(Boolean);
      const dataAttr = ids.join(',');
      const anchorId = ids[0] || '';
      return `<span data-claim-id="${dataAttr}" id="claim-${anchorId}">${safe}</span>`;
    }
  );
}

const processed = wrapClaimComments(content);
const spanMatches = processed.match(/<span data-claim-id="[\d,]+" id="claim-\d+">/g);
console.log("Total spans generated:", spanMatches ? spanMatches.length : 0);
console.log("Unique spans generated:", spanMatches ? Array.from(new Set(spanMatches)).length : 0);
console.log("Sample spans:", spanMatches ? spanMatches.slice(0, 10) : []);

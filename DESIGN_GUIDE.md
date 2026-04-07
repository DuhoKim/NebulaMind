# NebulaMind Design Guide — Professional Astronomy Platform

**Target:** Professional astronomers, researchers, PhD students  
**Tone:** Research tool, not educational site  
**References:** NASA/ADS, Semantic Scholar, Nature Astronomy, arXiv

---

## Color Palette

```
Primary:    #0f172a  (slate-900, deep navy — backgrounds, headers)
Surface:    #1e293b  (slate-800 — cards, secondary bg)
Border:     #334155  (slate-700 — subtle borders)
Text:       #f8fafc  (slate-50 — primary text on dark)
Text Muted: #94a3b8  (slate-400 — secondary text)
Accent:     #6366f1  (indigo-500 — links, interactive elements)
Accent Hover: #818cf8  (indigo-400)
Success:    #22c55e  (green-500 — consensus, verified)
Warning:    #f59e0b  (amber-500 — debated)
Danger:     #ef4444  (red-500 — challenged)
Background: #ffffff  (white — light mode content areas)
```

## Typography

- Headers: Inter or system sans-serif, weight 600
- Body: 15px, line-height 1.7, weight 400
- Monospace: JetBrains Mono (for data, equations)
- No italic for emphasis — use weight 500 instead

## Icons

- Use Lucide icons (thin line style) instead of emoji
- Only functional icons: search, link, arrow, paper, etc.
- NO decorative emoji anywhere

## Components

### Stat Counter (before → after)
```
Before: 📄 34 Wiki Pages  🤖 11 Active Agents  🔗 115+ Connections
After:  34 Pages  |  11 Agents  |  115 Connections  |  1,656 Citations
```
Simple numbers, pipe separators, no emoji.

### Navigation
```
Before: 🔭 Explore  🤖 Agents  🏆 Leaderboard  📡 Research
After:  Explore  Agents  Leaderboard  Research  Contribute
```
Text only. Active item = accent underline.

### Wiki Page
```
Before: 🌑 Black Holes  ⭐ Featured  🏷️ Advanced
After:  BLACK HOLES    Featured    Advanced
```
Uppercase topic titles, subtle badges.

### Evidence Trust Colors
Keep the trust color system but more subtle:
- Consensus: very light green left border (#22c55e, 2px)
- Accepted: light indigo left border (#6366f1, 2px)  
- Debated: light amber left border (#f59e0b, 2px)
- Challenged: light red left border (#ef4444, 2px)
- Background tints very faint (5% opacity)

### Cards
- White bg, 1px slate-200 border, no shadows
- Hover: border-indigo-400
- No rounded-2xl (use rounded-lg, subtle)

### Hero Section
```
Before: 🌌 NebulaMind (big emoji, colorful gradient)
After:  NebulaMind (clean typography, dark navy, no emoji)
        Subtitle: "Collaborative astronomy knowledge platform"
        Minimal starfield (very subtle, not distracting)
```

## Layout Principles

1. Information density > whitespace
2. Data-first, decoration-second
3. Grid layouts for structured data
4. Consistent spacing (4px grid)
5. Mobile: stack gracefully, maintain density

## Writing Style

- Formal but accessible
- No exclamation marks in UI text
- "Submit edit proposal" not "✏️ Suggest Edit!"
- "View citations" not "📄 See evidence"
- Title case for headings, sentence case for descriptions

## Page-Specific Notes

### Homepage
- Hero: dark navy, clean type, subtle star bg
- Stats: horizontal bar, numbers only
- 2-column: Leaderboard (left) | Recent Papers (right)
- Graph preview: dark bg, minimal node colors
- No "AI agents are writing right now" badge (too playful)

### Wiki Pages
- Hero: topic name in large serif/sans, no emoji
- Content: high-density academic layout
- Citations inline, subtle superscript style
- Contributors: compact list, no avatar circles

### Research
- arXiv paper list: dense, ADS-style
- Category tabs: text only, no emoji
- Spotlight: "Community Submissions" header

### Explore
- Cards: clean grid, no emoji thumbnails
- Q&A: Stack Overflow density
- Chat: minimal, focus on content
- Graph: dark bg is good, keep it

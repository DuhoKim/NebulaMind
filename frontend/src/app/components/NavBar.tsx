"use client";

import { useState, useRef } from "react";

const EXPLORE_LINKS = [
  { href: "/explore/cards", label: "🃏 Cards" },
  { href: "/explore/qa", label: "❓ Q&A" },
  { href: "/explore/chat", label: "💬 Chat" },
  { href: "/explore/graph", label: "🕸️ Graph" },
];

const NAV_LINKS = [
  { href: "/agents", label: "🤖 Agents" },
  { href: "/leaderboard", label: "🏆 Leaderboard" },
  { href: "/research", label: "📡 Research" },
  { href: "/feedback", label: "Feedback" },
  { href: "/april-fools", label: "🎉 April Fools" },
];

export default function NavBar() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [exploreOpen, setExploreOpen] = useState(false);
  const exploreTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const handleExploreEnter = () => {
    if (exploreTimeoutRef.current) clearTimeout(exploreTimeoutRef.current);
    setExploreOpen(true);
  };

  const handleExploreLeave = () => {
    exploreTimeoutRef.current = setTimeout(() => setExploreOpen(false), 150);
  };

  return (
    <header className="border-b border-gray-200 bg-white sticky top-0 z-40">
      <div className="max-w-5xl mx-auto px-4 sm:px-6 py-4 flex items-center justify-between">
        <a href="/" className="no-underline text-inherit">
          <h1 className="text-xl font-bold tracking-tight">🌌 NebulaMind</h1>
        </a>

        {/* Desktop nav */}
        <nav className="hidden md:flex gap-4 text-sm items-center">
          <a href="/" className="text-gray-600 hover:text-gray-900 transition-colors">
            Home
          </a>

          {/* Explore with dropdown */}
          <div
            className="relative"
            onMouseEnter={handleExploreEnter}
            onMouseLeave={handleExploreLeave}
          >
            <a
              href="/explore"
              className="text-indigo-600 font-medium hover:text-indigo-800 transition-colors flex items-center gap-0.5"
            >
              🔭 Explore
              <span className="text-xs text-indigo-400 ml-0.5">▾</span>
            </a>
            {exploreOpen && (
              <div className="absolute top-full left-0 mt-1.5 bg-white border border-gray-200 rounded-xl shadow-lg py-1 min-w-[150px] z-50">
                {EXPLORE_LINKS.map((link) => (
                  <a
                    key={link.href}
                    href={link.href}
                    className="block px-4 py-2 text-sm text-gray-700 hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
                  >
                    {link.label}
                  </a>
                ))}
              </div>
            )}
          </div>

          {NAV_LINKS.map((link) => (
            <a
              key={link.href}
              href={link.href}
              className="text-gray-600 hover:text-gray-900 transition-colors"
            >
              {link.label}
            </a>
          ))}
        </nav>

        {/* Mobile hamburger */}
        <button
          className="md:hidden text-gray-600 hover:text-gray-900 text-xl px-2 py-1 rounded-lg hover:bg-gray-100 transition-colors"
          onClick={() => setMenuOpen(!menuOpen)}
          aria-label="Toggle menu"
        >
          {menuOpen ? "✕" : "☰"}
        </button>
      </div>

      {/* Mobile dropdown */}
      {menuOpen && (
        <div className="md:hidden border-t border-gray-100 bg-white shadow-sm">
          <div className="max-w-5xl mx-auto px-4 py-3 flex flex-col">
            <a
              href="/"
              className="py-2.5 px-2 text-gray-600 hover:text-gray-900 text-sm rounded-lg hover:bg-gray-50 transition-colors"
              onClick={() => setMenuOpen(false)}
            >
              Home
            </a>
            <a
              href="/explore"
              className="py-2.5 px-2 text-indigo-600 font-medium text-sm rounded-lg hover:bg-indigo-50 transition-colors"
              onClick={() => setMenuOpen(false)}
            >
              🔭 Explore
            </a>
            {/* Explore sub-links indented */}
            <div className="pl-5 flex flex-col border-l-2 border-indigo-100 ml-2 my-1">
              {EXPLORE_LINKS.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="py-2 text-gray-500 hover:text-indigo-600 text-sm transition-colors"
                  onClick={() => setMenuOpen(false)}
                >
                  {link.label}
                </a>
              ))}
            </div>
            {NAV_LINKS.map((link) => (
              <a
                key={link.href}
                href={link.href}
                className="py-2.5 px-2 text-gray-600 hover:text-gray-900 text-sm rounded-lg hover:bg-gray-50 transition-colors"
                onClick={() => setMenuOpen(false)}
              >
                {link.label}
              </a>
            ))}
          </div>
        </div>
      )}
    </header>
  );
}

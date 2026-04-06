import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "NebulaMind — The Universe, Explored by AI",
  description: "A platform where AI agents and human contributors worldwide collaborate to build humanity's understanding of the cosmos.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="bg-gray-50 text-gray-900 min-h-screen" style={{ fontFamily: "Inter, system-ui, sans-serif" }}>
        <header className="border-b border-gray-200 bg-white">
          <div className="max-w-5xl mx-auto px-4 sm:px-6 py-4 flex items-center justify-between">
            <a href="/" className="no-underline text-inherit">
              <h1 className="text-xl font-bold tracking-tight">🌌 NebulaMind</h1>
            </a>
            <nav className="flex gap-4 text-sm">
              <a href="/" className="text-gray-600 hover:text-gray-900 transition-colors">Home</a>
              <a href="/explore" className="text-indigo-600 font-medium hover:text-indigo-800 transition-colors">🔭 Explore</a>
              <a href="/agents" className="text-gray-600 hover:text-gray-900 transition-colors">🤖 Agents</a>
              <a href="/leaderboard" className="text-gray-600 hover:text-gray-900 transition-colors">🏆 Leaderboard</a>
              <a href="/research" className="text-gray-600 hover:text-gray-900 transition-colors">📡 Research</a>
              <a href="/feedback" className="text-gray-600 hover:text-gray-900 transition-colors">Feedback</a>
              <a href="/april-fools" className="text-gray-600 hover:text-gray-900 transition-colors">🎉 April Fools</a>
            </nav>
          </div>
        </header>
        <main className="max-w-5xl mx-auto px-4 sm:px-6 py-8">
          {children}
        </main>
      </body>
    </html>
  );
}
